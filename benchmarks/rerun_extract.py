#!/usr/bin/env python3
"""
# rerun_extract.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Re-run the extraction agent on chosen benchmark models under a different
engine mode, paper source and/or prompt variant, then render, validate and
score the result.

    python eval/benchmark_runs/rerun_extract.py --pages A,B --variant v3_tools \
        --engine-mode tools --paper-source tex \
        --addendum eval/benchmark_runs/prompt_addendum_v3.txt --seeds 2
    python eval/benchmark_runs/rerun_extract.py --pages A,B --variant v3_notools \
        --engine-mode notools --paper-source tex \
        --addendum eval/benchmark_runs/prompt_addendum_v3.txt --seeds 2

Two engine modes, so the same model, paper and physics rules can be compared
with and without tool support:

  * ``tools`` — the fleet architecture. The agent has file-reading tools only
    (Read/Grep/Glob; no shell, no network, no MCP servers), reads the paper
    and the schema (frmodel.py) inside a sandbox, and emits a fenced
    model_json; the deterministic GenerateFeynRulesModelTool renders the .fr
    afterwards, so schema validation genuinely executes.
  * ``notools`` — the ablation arm. Every built-in tool is disabled
    (``--tools ""``); the paper and SM.fr are inlined into the prompt; the
    agent writes the complete .fr file itself in one fenced block. No schema,
    no renderer, nothing to read.

Two paper sources:

  * ``tex`` — the paper's LaTeX source (``text/<id>_source.tex``, fetched with
    ArxivSourceTool). Fractions, roots and sub/superscripts are exact. The
    EffLRSM Z_R normalisation error (root multiplied instead of divided) came
    from the PDF text flattening ``\\frac{-\\kappa g}{\\sqrt{...}}`` into three
    lines.
  * ``txt`` — the PDF-extracted text the original fleet and the v1/v2 reruns
    used. Kept so the effect of the source can be isolated.

The agent runs inside a per-run SANDBOX directory that mirrors the repo
layout but contains only the chosen paper file, the schema (frmodel.py), the
renderer (render.py) and SM.fr. The original fleet ran with the whole repo
visible, and the physicist reference files under eval/reference_cache/ were
one Glob away: the 368sextets run opened its own reference and copied it. A
benchmark of "extract the model from the paper" is void if the answer key is
readable. ``--setting-sources ""`` keeps the operator's own CLAUDE.md and
settings out of the agent as well.

Three things are recorded that the original fleet did not, because each
decides whether a result means anything:

  * did the agent actually READ the paper (a Read of the paper file in the
    tool stream; in notools mode the paper is inlined, recorded as such)?
  * did it reach OUTSIDE the sandbox (an absolute path elsewhere, or anything
    naming reference_cache)? Flagged as contaminated, never silently kept.
    In notools mode ANY tool call is an anomaly and is recorded.
  * per-finding predicates (rerun_predicates.py, optional): deterministic
    checks on the .fr text for the specific defects a physicist reported.

Outputs, per run:
    eval/benchmark_runs/<page>/rerun/<variant>/s<k>/
        prompt.txt  agent_stream.jsonl  agent_out.md  agent_stderr.txt
        model/<page>_gen.fr  validation.json  predicates.json  run.json
and eval/benchmark_runs/rerun_report_<variant>.json
Scratch (UFO dirs, MG5 runs): $RERUN_OUT (default /tmp/rerun_bench).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import signal
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(HERE))

os.environ.setdefault("VBENCH_COMPILE_TIMEOUT", "600")
os.environ.setdefault("VBENCH_OUT", os.environ.get("RERUN_OUT", "/tmp/rerun_bench"))

import validation_benchmark as vb  # noqa: E402
from db_collect import recover_json  # noqa: E402
from tools.frgen.frgen_tool import GenerateFeynRulesModelTool  # noqa: E402

AGENT_TIMEOUT = int(os.environ.get("RERUN_AGENT_TIMEOUT", "1800"))
AGENT_MODEL = os.environ.get("RERUN_AGENT_MODEL", "claude-opus-5")
# Prompt goes on stdin: --disallowedTools is variadic and swallows a trailing
# positional as another tool name. --setting-sources "" keeps the operator's
# CLAUDE.md, settings and hooks out of the benchmarked agent.
_COMMON = ("claude -p --output-format stream-json --verbose --model {model} "
           "--mcp-config {mcp} --strict-mcp-config --setting-sources '' ")
AGENT_CMDS = {
    "tools": _COMMON + "--allowedTools Read,Grep,Glob "
             "--disallowedTools Bash,WebFetch,WebSearch,Edit,Write,MultiEdit,NotebookEdit,Agent,TodoWrite",
    "notools": _COMMON + "--tools ''",
}
OUTROOT = Path(os.environ["VBENCH_OUT"])

# Everything the agent may see, as repo-relative paths mirrored into the sandbox.
SANDBOX_SHARED = [
    "tools/frgen/frmodel.py",
    "tools/frgen/render.py",
    "tools/feynrules/test_files/models/SM.fr",
]
SM_FR = REPO / "tools/feynrules/test_files/models/SM.fr"
SANDBOX_NOTE = """\
SANDBOX: your working directory contains ONLY the paper, tools/frgen/frmodel.py
(the schema), tools/frgen/render.py (the renderer), and
tools/feynrules/test_files/models/SM.fr (the Standard Model file this add-on is loaded
on top of: take field names, index conventions and hypercharges from it). Nothing else
exists here and nothing outside this directory may be read."""
NOTOOLS_NOTE = """\
NO TOOLS: this run has no file, shell, network or code tools. Everything you need is in
this message: the Standard Model file SM.fr (the file this add-on is loaded on top of:
take field names, index conventions and hypercharges from it) and the paper. Do not ask
for anything; do the extraction and write the model."""


# ------------------------------------------------------------------ paper
def paper_file(page: str, source: str) -> tuple[Path, str]:
    """(absolute path, source actually used). ``tex`` falls back to ``txt``
    when no LaTeX source was fetched for the page, and says so."""
    text_dir = HERE / page / "text"
    if source == "tex":
        texs = sorted(text_dir.glob("*_source.tex"))
        if texs:
            return texs[0], "tex"
        source = "txt"
    txts = sorted(text_dir.glob("*.txt"))
    if not txts:
        raise FileNotFoundError(f"no paper text under {text_dir}")
    return txts[0], "txt"


def _sub_once(text: str, pattern: str, repl: str, what: str) -> str:
    new, n = re.subn(pattern, lambda _m: repl, text, count=1, flags=re.M)
    if n != 1:
        raise ValueError(f"prompt template: could not find the {what} line to rewrite")
    return new


# ------------------------------------------------------------------ prompt
def build_prompt(page: str, addendum: str | None, mode: str,
                 paper_abs: Path, paper_src: str) -> str:
    """The fleet prompt, adapted to the engine mode and paper source, plus the
    variant's addendum."""
    base = (HERE / page / "prompt.txt").read_text()
    paper_rel = f"eval/benchmark_runs/{page}/text/{paper_abs.name}"
    src_note = ("the paper's LaTeX source: equations, fractions and roots are exact"
                if paper_src == "tex" else "text extracted from the PDF")

    if mode == "tools":
        base = _sub_once(base, r"^PAPER: .*$",
                         f'PAPER: full text at "{paper_rel}" (read it with your '
                         f"file-reading tool; it is {src_note}; it is authoritative).",
                         "PAPER")
        base = base.rstrip() + "\n\n" + SANDBOX_NOTE + "\n"
        if addendum:
            base = base.rstrip() + "\n\n" + addendum.strip() + "\n"
        return base

    # notools: same task, no schema, the .fr written directly, documents first.
    base = _sub_once(base, r"^PAPER: .*$",
                     f"PAPER: {src_note}, included verbatim above between the PAPER "
                     "markers; it is authoritative.", "PAPER")
    base = _sub_once(base, r"^SCHEMA: .*$",
                     "FORMAT: write a complete FeynRules .fr add-on model file yourself "
                     "(M$ModelName, M$Information, M$InteractionOrderHierarchy, IndexRange "
                     "declarations for new indices, M$Parameters, M$ClassesDescription, the "
                     "Lagrangian terms and one LTotal). It is loaded on top of SM.fr, included "
                     "verbatim above between the SM.fr markers.", "SCHEMA")
    base = _sub_once(base, r"^3\. Include the main new-physics lagrangian_terms .*$",
                     "3. Write the main new-physics Lagrangian terms (FeynRules/Mathematica "
                     "syntax and idioms).", "TASK item 3")
    base = _sub_once(base, r"^SCHEMA RULES: .*$",
                     "FILE RULES: use FeynRules syntax for every value (rationals -1/3, decimals "
                     "1500.); SM add-on => no M$GaugeGroups block; the indices Colour, Gluon, "
                     "Generation, SU2D and SU2W are declared by SM.fr; any OTHER index (a "
                     "colour-sextet index, a new-generation index) needs "
                     "`IndexRange[Index[X]] = NoUnfold[Range[n]];` with the correct size; every "
                     "class gets a unique label S[n]/F[n]/V[n] with n >= 100; "
                     "SelfConjugate -> False for complex fields (distinct antiparticle), True for "
                     "real/Majorana fields.", "SCHEMA RULES")
    base = _sub_once(base, r"^OUTPUT: .*$",
                     "OUTPUT: your FINAL message must contain exactly one fenced code block "
                     "tagged mathematica containing ONLY the complete .fr file (no commentary "
                     f'inside the fences). Set M$ModelName = "{page}_gen".', "OUTPUT")
    base = base.rstrip() + "\n\n" + NOTOOLS_NOTE + "\n"
    if addendum:
        base = base.rstrip() + "\n\n" + addendum.strip() + "\n"

    docs = (f"===== BEGIN SM.fr (tools/feynrules/test_files/models/SM.fr) =====\n"
            f"{SM_FR.read_text()}\n===== END SM.fr =====\n\n"
            f"===== BEGIN PAPER ({paper_abs.name}; {src_note}) =====\n"
            f"{paper_abs.read_text(errors='replace')}\n===== END PAPER =====\n\n")
    return docs + base


def make_sandbox(page: str, rundir: Path, paper_abs: Path) -> Path:
    """A fresh directory mirroring the repo layout, holding only the allowed files.

    Lives under the system temp dir, NOT inside the repo: a sandbox at
    <repo>/eval/benchmark_runs/<page>/rerun/.../sandbox tells the agent where
    the repo is, and one run promptly read the paper through that real path.
    """
    import shutil
    import tempfile
    sb = Path(tempfile.mkdtemp(prefix=f"rerun-{page}-"))
    (rundir / "sandbox_path.txt").write_text(str(sb))
    dst = sb / "eval" / "benchmark_runs" / page / "text" / paper_abs.name
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(paper_abs, dst)
    for rel in SANDBOX_SHARED:
        src, dst = REPO / rel, sb / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    return sb


# ------------------------------------------------------------------- agent
def _parse_stream(lines: list[str], paper_rel: str, sandbox: Path) -> dict:
    """Final text + tool facts from `claude -p --output-format stream-json`."""
    texts: list[str] = []
    reads: list[str] = []
    outside: list[str] = []
    n_tools = 0
    # Both spellings of the sandbox root: macOS resolves /var to /private/var,
    # so an agent handed the /var path reads files that startswith() the raw
    # prefix but not the resolved one. Comparing against one of them alone
    # marks every legitimate read as an escape.
    sb_prefixes = tuple({str(sandbox), str(sandbox.resolve())})
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        msg = rec.get("message") if isinstance(rec.get("message"), dict) else rec
        content = msg.get("content")
        if not isinstance(content, list):
            # `result` records carry the final text directly
            if rec.get("type") == "result" and isinstance(rec.get("result"), str):
                texts.append(rec["result"])
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                n_tools += 1
                inp = block.get("input") if isinstance(block.get("input"), dict) else {}
                if block.get("name") == "Read":
                    reads.append(str(inp.get("file_path", "")))
                # Any path-like argument that escapes the sandbox is recorded.
                # Reaching the SAME paper file through its real repo path is
                # benign (identical bytes); anything else outside — above all
                # the answer key under reference_cache — taints the run.
                for key in ("file_path", "path", "pattern"):
                    v = str(inp.get(key, "") or "")
                    if not v:
                        continue
                    if "reference_cache" in v or (v.startswith("/")
                                                  and not v.startswith(sb_prefixes)):
                        outside.append(f"{block.get('name')}:{v[:120]}")
            elif block.get("type") == "text" and block.get("text"):
                texts.append(block["text"])
    read_paper = any(paper_rel in r for r in reads)
    benign = [o for o in outside
              if "reference_cache" not in o and paper_rel in o
              and (o.endswith(".txt") or o.endswith(".tex"))]
    tainted = [o for o in outside if o not in benign]
    return {"final_text": "\n".join(texts), "n_tool_calls": n_tools,
            "files_read": reads, "read_paper": read_paper,
            "contaminated": bool(tainted), "outside_sandbox": outside,
            "benign_outside": benign}


def run_agent(page: str, prompt: str, rundir: Path, mode: str, paper_abs: Path) -> dict:
    rundir.mkdir(parents=True, exist_ok=True)
    (rundir / "prompt.txt").write_text(prompt)
    sandbox = make_sandbox(page, rundir, paper_abs)
    mcp = rundir / "mcp_empty.json"
    mcp.write_text('{"mcpServers": {}}')
    cmd = shlex.split(os.environ.get("RERUN_AGENT_CMD", AGENT_CMDS[mode])
                      .format(model=AGENT_MODEL, mcp=str(mcp)))
    t0 = time.time()
    timed_out = False
    try:
        p = subprocess.Popen(cmd, cwd=str(sandbox), stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             text=True, start_new_session=True)
        # Wall-clock watchdog in addition to communicate's own timeout: the
        # latter counts monotonic time, which stops while the machine sleeps,
        # so a laptop that dozed off mid-run let an agent stalled on HTTP 429
        # live for three hours. time.time() jumps across sleep; this does not.
        killed = {"by_watchdog": False}

        def _watchdog():
            while p.poll() is None:
                if time.time() - t0 > AGENT_TIMEOUT:
                    killed["by_watchdog"] = True
                    try:
                        os.killpg(os.getpgid(p.pid), signal.SIGKILL)
                    except (ProcessLookupError, PermissionError):
                        pass
                    return
                time.sleep(15)
        threading.Thread(target=_watchdog, daemon=True).start()
        try:
            out, err = p.communicate(input=prompt, timeout=AGENT_TIMEOUT)
            rc = p.returncode
            if killed["by_watchdog"]:
                rc, timed_out = 124, True
        except subprocess.TimeoutExpired:
            os.killpg(os.getpgid(p.pid), signal.SIGKILL)
            out, err = p.communicate()
            rc, timed_out = 124, True
    except FileNotFoundError as e:
        return {"ok": False, "error": f"engine not found: {e}"}
    dt = round(time.time() - t0, 1)
    (rundir / "agent_stream.jsonl").write_text(out or "")
    (rundir / "agent_stderr.txt").write_text(err or "")
    paper_rel = f"eval/benchmark_runs/{page}/text/"
    parsed = _parse_stream((out or "").splitlines(), paper_rel, sandbox)
    if parsed["final_text"].strip():
        (rundir / "agent_out.md").write_text(parsed["final_text"])
    else:
        # A logged-out CLI, a usage limit or a transport error leaves no text.
        # Writing an empty agent_out.md would make --skip-existing treat the
        # failure as a finished run for ever.
        (rundir / "agent_out.md").unlink(missing_ok=True)
    facts = {"ok": rc == 0 and not timed_out and bool(parsed["final_text"]),
             "exit": rc, "timed_out": timed_out, "seconds": dt, "mode": mode,
             "n_tool_calls": parsed["n_tool_calls"],
             "read_paper": parsed["read_paper"],
             "contaminated": parsed["contaminated"],
             "outside_sandbox": parsed["outside_sandbox"],
             "benign_outside": parsed["benign_outside"],
             "files_read": parsed["files_read"][:40],
             "prompt_chars": len(prompt)}
    if mode == "notools":
        # The paper is in the prompt; a tool call of any kind is an anomaly.
        facts["paper_inlined"] = True
        facts["read_paper"] = True
        facts["anomalous_tool_calls"] = parsed["n_tool_calls"]
    err_tail = (err or "").strip()[-400:]
    if err_tail and not facts["ok"]:
        facts["stderr_tail"] = err_tail
    if rc == 0 and not parsed["final_text"]:
        facts["error"] = "empty final text"
    return facts


# ------------------------------------------------------- render + validate
_FENCE_RE = re.compile(r"```[ \t]*([A-Za-z0-9_+-]*)[ \t]*\n(.*?)```", re.S)


def _fr_block(md: str) -> str | None:
    """The last fenced block that looks like a FeynRules model file."""
    blocks = [(tag.lower(), body) for tag, body in _FENCE_RE.findall(md)]
    cands = [b for _t, b in blocks if "M$ModelName" in b or "M$ClassesDescription" in b]
    if not cands:
        cands = [b for t, b in blocks if t in ("mathematica", "wolfram", "fr", "feynrules")]
    return cands[-1] if cands else None


def render(page: str, rundir: Path, mode: str) -> dict:
    if mode == "notools":
        md = (rundir / "agent_out.md").read_text(errors="replace")
        body = _fr_block(md)
        if body is None:
            return {"rendered": False, "reason": "no_fr_block"}
        fr = rundir / "model" / f"{page}_gen.fr"
        fr.parent.mkdir(parents=True, exist_ok=True)
        fr.write_text(body.rstrip() + "\n")
        return {"rendered": True, "fr": str(fr), "agent_written": True,
                "has_model_name": "M$ModelName" in body}
    mj, err = recover_json(rundir / "agent_out.md")
    if mj is None:
        return {"rendered": False, "reason": err}
    raw = GenerateFeynRulesModelTool(
        model_json=json.dumps(mj), output_path=f"model/{page}_gen.fr",
        base_directory=str(rundir))._run()
    if not raw.lstrip().startswith("{"):
        return {"rendered": False, "reason": "schema_validation_failed",
                "detail": raw[:600]}
    gen = json.loads(raw)
    return {"rendered": True, "fr": str(rundir / gen["fr_path"])}


def validate(page: str, fr: Path, tag: str) -> dict:
    lag, info = vb.total_lag_symbol(fr)
    row: dict = {"lag_symbol": lag, "lag_resolution": info}
    if not lag:
        row["status"] = ("ambiguous_lagrangian_symbol" if info.get("ambiguous")
                         else "no_lagrangian_symbol")
        return row
    outdir = OUTROOT / tag / f"{page}_UFO"
    comp = vb.compile_to_ufo(page, fr, lag, outdir)
    row.update(comp)
    if comp["compile_ok"]:
        row["n_particles_ufo"] = vb.count_new_particles(outdir)
        row.update(vb.madgraph_import(outdir, OUTROOT / tag / "mg5run"))
        row["status"] = "compiled"
    else:
        row["status"] = "compile_timeout" if comp["timed_out"] else "compile_failed"
    row["full_chain_pass"] = bool(comp["compile_ok"]
                                  and all(comp["checks"].values())
                                  and row.get("madgraph_import_ok"))
    return row


def predicates(page: str, fr_text: str) -> dict:
    try:
        import rerun_predicates  # noqa: WPS433
    except ImportError:
        return {"available": False}
    checks = rerun_predicates.PREDICATES.get(page, [])
    out = {"available": True, "results": {}}
    for name, fn in checks:
        try:
            ok, detail = fn(fr_text)
        except Exception as e:                              # noqa: BLE001
            ok, detail = False, f"predicate raised {type(e).__name__}: {e}"
        out["results"][name] = {"resolved": bool(ok), "detail": detail}
    out["all_resolved"] = bool(checks) and all(
        r["resolved"] for r in out["results"].values())
    return out


# --------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", required=True, help="comma-separated pages")
    ap.add_argument("--variant", required=True,
                    help="run label, e.g. v3_tools, v3_notools, v3txt_tools")
    ap.add_argument("--engine-mode", choices=sorted(AGENT_CMDS), default="tools",
                    help="tools: Read/Grep/Glob + schema + renderer (fleet architecture); "
                         "notools: no tools at all, paper and SM.fr inlined, agent writes the .fr")
    ap.add_argument("--paper-source", choices=("tex", "txt"), default="tex",
                    help="tex: LaTeX source (text/<id>_source.tex, falls back to txt if absent); "
                         "txt: PDF-extracted text")
    ap.add_argument("--addendum", default="", help="file appended to the prompt")
    ap.add_argument("--seeds", type=int, default=1)
    ap.add_argument("--parallel", type=int, default=4, help="concurrent agents")
    ap.add_argument("--no-validate", action="store_true")
    ap.add_argument("--skip-existing", action="store_true",
                    help="reuse a run dir whose agent_out.md already exists")
    ap.add_argument("--skip-validated", action="store_true",
                    help="reuse a validation.json that already records a full-chain pass; "
                         "failures and timeouts are redone")
    args = ap.parse_args()

    pages = [p for p in args.pages.split(",") if p]
    addendum = Path(args.addendum).read_text() if args.addendum else None
    jobs = [(page, k) for page in pages for k in range(1, args.seeds + 1)]
    papers = {page: paper_file(page, args.paper_source) for page in pages}
    for page, (pf, used) in papers.items():
        if used != args.paper_source:
            print(f"[rerun] {page}: no LaTeX source, falling back to {pf.name}", flush=True)

    def agent_job(job):
        page, k = job
        rundir = HERE / page / "rerun" / args.variant / f"s{k}"
        if args.skip_existing and (rundir / "agent_out.md").is_file():
            print(f"[rerun] skip {page} {args.variant} s{k} (exists)", flush=True)
            # Keep the recorded agent facts (read_paper, contamination, timing)
            # rather than overwriting them with a stub.
            prev = rundir / "run.json"
            if prev.is_file():
                try:
                    facts = json.loads(prev.read_text()).get("agent") or {}
                    facts["skipped"] = True
                    return job, facts
                except (OSError, json.JSONDecodeError):
                    pass
            return job, {"ok": True, "skipped": True}
        paper_abs, paper_src = papers[page]
        print(f"[rerun] agent {page} {args.variant} s{k} [{args.engine_mode}/{paper_src}] ...",
              flush=True)
        prompt = build_prompt(page, addendum, args.engine_mode, paper_abs, paper_src)
        res = run_agent(page, prompt, rundir, args.engine_mode, paper_abs)
        print(f"[rerun]   {page} s{k}: ok={res.get('ok')} "
              f"read_paper={res.get('read_paper')} "
              f"contaminated={res.get('contaminated')} "
              f"tools={res.get('n_tool_calls')} {res.get('seconds')}s", flush=True)
        return job, res

    with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as ex:
        agent_results = dict(ex.map(agent_job, jobs))

    rows = []
    for page, k in jobs:                       # validation is serial: Wolfram
        rundir = HERE / page / "rerun" / args.variant / f"s{k}"
        row = {"page": page, "variant": args.variant, "seed": k,
               "mode": args.engine_mode, "paper_source": papers[page][1],
               "paper_file": papers[page][0].name,
               "agent": agent_results[(page, k)]}
        rend = render(page, rundir, args.engine_mode)
        row["render"] = rend
        if rend.get("rendered"):
            fr = Path(rend["fr"])
            fr_text = fr.read_text(errors="replace")
            row["predicates"] = predicates(page, fr_text)
            (rundir / "predicates.json").write_text(
                json.dumps(row["predicates"], indent=1))
            prev = rundir / "validation.json"
            if (not args.no_validate and args.skip_validated and prev.is_file()
                    and json.loads(prev.read_text()).get("full_chain_pass")):
                row["validation"] = json.loads(prev.read_text())
                print(f"[rerun] validate {page} {args.variant} s{k}: reused full-chain pass",
                      flush=True)
            elif not args.no_validate:
                print(f"[rerun] validate {page} {args.variant} s{k} ...", flush=True)
                row["validation"] = validate(page, fr, f"{args.variant}_s{k}")
                (rundir / "validation.json").write_text(
                    json.dumps(row["validation"], indent=1))
                print(f"[rerun]   -> {row['validation'].get('status')} "
                      f"full_chain={row['validation'].get('full_chain_pass')}",
                      flush=True)
        (rundir / "run.json").write_text(json.dumps(row, indent=1, default=str))
        rows.append(row)

    report = HERE / f"rerun_report_{args.variant}.json"
    existing = json.loads(report.read_text())["rows"] if report.is_file() else []
    keep = [r for r in existing
            if (r["page"], r["seed"]) not in {(p, k) for p, k in jobs}]
    report.write_text(json.dumps({"variant": args.variant,
                                  "agent_model": AGENT_MODEL,
                                  "engine_mode": args.engine_mode,
                                  "paper_source": args.paper_source,
                                  "rows": keep + rows}, indent=1, default=str))
    print(f"[rerun] wrote {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
