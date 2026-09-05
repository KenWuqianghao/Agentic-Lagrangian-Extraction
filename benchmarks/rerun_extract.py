#!/usr/bin/env python3
"""
# rerun_extract.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Re-run the extraction agent on chosen benchmark models under a different
engine and/or prompt variant, then render, validate and score the result.

    python eval/benchmark_runs/rerun_extract.py --pages A,B --variant v1 --seeds 2
    python eval/benchmark_runs/rerun_extract.py --pages A,B --variant v2 \
        --addendum eval/benchmark_runs/prompt_addendum_v2.txt

Same architecture as the original fleet (db_launch.sh + db_collect.py): the
agent only EXTRACTS — it reads the local paper text and emits a fenced
model_json — and the deterministic GenerateFeynRulesModelTool renders the .fr
afterwards, so schema validation genuinely executes. The agent runs read-only:
file reading tools only, no shell, no network, no MCP servers.

The agent runs inside a per-run SANDBOX directory that mirrors the repo
layout but contains only the paper text, the schema (frmodel.py), the
renderer (render.py) and SM.fr. The original fleet ran with the whole repo
visible, and the physicist reference files under eval/reference_cache/ were
one Glob away: the 368sextets run opened its own reference and copied it,
and two unsandboxed reruns grepped `**/*.fr` across the repo. A benchmark of
"extract the model from the paper" is void if the answer key is readable.

Three things are recorded that the original fleet did not, because each
decides whether a result means anything:

  * did the agent actually READ the paper (a Read of the text file in the
    tool stream)? A correct-looking model produced without reading the paper
    was recalled, not extracted.
  * did it reach OUTSIDE the sandbox (an absolute path elsewhere, or anything
    naming reference_cache)? Flagged as contaminated, never silently kept.
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
# positional as another tool name.
DEFAULT_AGENT_CMD = (
    "claude -p --output-format stream-json --verbose --model {model} "
    "--mcp-config {mcp} --strict-mcp-config "
    "--allowedTools Read,Grep,Glob "
    "--disallowedTools Bash,WebFetch,WebSearch,Edit,Write,MultiEdit,NotebookEdit,Agent,TodoWrite"
)
OUTROOT = Path(os.environ["VBENCH_OUT"])

# Everything the agent may see, as repo-relative paths mirrored into the sandbox.
SANDBOX_SHARED = [
    "tools/frgen/frmodel.py",
    "tools/frgen/render.py",
    "tools/feynrules/test_files/models/SM.fr",
]
SANDBOX_NOTE = """\
SANDBOX: your working directory contains ONLY the paper text, tools/frgen/frmodel.py
(the schema), tools/frgen/render.py (the renderer), and
tools/feynrules/test_files/models/SM.fr (the Standard Model file this add-on is loaded
on top of: take field names, index conventions and hypercharges from it). Nothing else
exists here and nothing outside this directory may be read."""


# ------------------------------------------------------------------ prompt
def build_prompt(page: str, addendum: str | None) -> str:
    """The fleet prompt, adapted to a shell-less engine, plus the variant's addendum."""
    base = (HERE / page / "prompt.txt").read_text()
    base = base.replace("(read it with sed/cat; it is authoritative)",
                        "(read it with your file-reading tool; it is authoritative)")
    base = base.rstrip() + "\n\n" + SANDBOX_NOTE + "\n"
    if addendum:
        base = base.rstrip() + "\n\n" + addendum.strip() + "\n"
    return base


def make_sandbox(page: str, rundir: Path) -> Path:
    """A fresh directory mirroring the repo layout, holding only the allowed files.

    Lives under the system temp dir, NOT inside the repo: a sandbox at
    <repo>/eval/benchmark_runs/<page>/rerun/.../sandbox tells the agent where
    the repo is, and one run promptly read the paper through that real path.
    """
    import shutil
    import tempfile
    sb = Path(tempfile.mkdtemp(prefix=f"rerun-{page}-"))
    (rundir / "sandbox_path.txt").write_text(str(sb))
    text_dir = HERE / page / "text"
    for src in sorted(text_dir.glob("*.txt")):
        dst = sb / "eval" / "benchmark_runs" / page / "text" / src.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
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
    sb = str(sandbox.resolve())
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
                # Reaching the SAME paper text through its real repo path is
                # benign (identical bytes); anything else outside — above all
                # the answer key under reference_cache — taints the run.
                for key in ("file_path", "path", "pattern"):
                    v = str(inp.get(key, "") or "")
                    if not v:
                        continue
                    if "reference_cache" in v or (v.startswith("/") and not v.startswith(sb)):
                        outside.append(f"{block.get('name')}:{v[:120]}")
            elif block.get("type") == "text" and block.get("text"):
                texts.append(block["text"])
    read_paper = any(paper_rel in r for r in reads)
    benign = [o for o in outside
              if "reference_cache" not in o and paper_rel in o and o.endswith(".txt")]
    tainted = [o for o in outside if o not in benign]
    return {"final_text": "\n".join(texts), "n_tool_calls": n_tools,
            "files_read": reads, "read_paper": read_paper,
            "contaminated": bool(tainted), "outside_sandbox": outside,
            "benign_outside": benign}


def run_agent(page: str, prompt: str, rundir: Path) -> dict:
    rundir.mkdir(parents=True, exist_ok=True)
    (rundir / "prompt.txt").write_text(prompt)
    sandbox = make_sandbox(page, rundir)
    mcp = rundir / "mcp_empty.json"
    mcp.write_text('{"mcpServers": {}}')
    cmd = shlex.split(os.environ.get("RERUN_AGENT_CMD", DEFAULT_AGENT_CMD)
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
        import threading
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
    (rundir / "agent_out.md").write_text(parsed["final_text"])
    return {"ok": rc == 0 and not timed_out and bool(parsed["final_text"]),
            "exit": rc, "timed_out": timed_out, "seconds": dt,
            "n_tool_calls": parsed["n_tool_calls"],
            "read_paper": parsed["read_paper"],
            "contaminated": parsed["contaminated"],
            "outside_sandbox": parsed["outside_sandbox"],
            "benign_outside": parsed["benign_outside"],
            "files_read": parsed["files_read"][:40]}


# ------------------------------------------------------- render + validate
def render(page: str, rundir: Path) -> dict:
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
    ap.add_argument("--variant", required=True, help="v1, v2, ...")
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
        print(f"[rerun] agent {page} {args.variant} s{k} ...", flush=True)
        res = run_agent(page, build_prompt(page, addendum), rundir)
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
               "agent": agent_results[(page, k)]}
        rend = render(page, rundir)
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
                                  "rows": keep + rows}, indent=1, default=str))
    print(f"[rerun] wrote {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
