#!/usr/bin/env python3
"""Run the pi agent on benchmark papers, then score every arm the same way.

Two pi arms, one scorer:

  harness   pi + the heptapod extension (lint_model, validate_model, massbasis,
            review_model), file tools confined to a sandbox, no bash, and the
            protocol in prompts/protocol.md appended to the system prompt. The
            agent writes model.fr, validates it with the scored chain and
            repairs it before it hands it in.
  plain     pi with every tool disabled and the exact v3 no-tools prompt of the
            Claude Code ablation arm (paper and SM.fr inlined, one fenced .fr
            in the final message). It separates "pi instead of Claude Code"
            from "the heptapod tools in the loop".

    run_pi.py run   --arm harness --variant pi_harness --pages A,B --model anthropic/claude-sonnet-5
    run_pi.py run   --arm plain   --variant pi_plain   --pages A,B --model anthropic/claude-sonnet-5
    run_pi.py score --variants pi_harness,pi_plain,v3s_notools --pages A,B
    run_pi.py report --variants pi_harness,pi_plain,v3s_notools --pages A,B

``score`` re-validates the delivered .fr of every run with hepval (the
heptapod-dev main driver, verdicts from return values), serially, into
``validation_hepval.json``. It never reads the agent's own validation calls:
the in-loop verdicts are the agent's evidence, the re-run is the score. It
scores stored baseline arms (v3s_notools) with the same code, so the
comparison is one scorer on every arm.

Outputs follow rerun_extract.py's layout so ablation_report.py (field F1,
predicates) reads them unchanged:
    <runs>/<page>/rerun/<variant>/s<k>/
        prompt.txt  agent_stream.jsonl  agent_stderr.txt  agent_out.md
        tool_calls.jsonl  validation/  model/<page>_gen.fr
        run.json  validation.json  validation_hepval.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = Path(
    os.environ.get("PI_HARNESS_RUNS", Path.home() / "Documents/Github/heptapod/eval/benchmark_runs")
)
SM_FR = Path.home() / "Documents/Github/heptapod/tools/feynrules/test_files/models/SM.fr"
ADDENDUM = RUNS / "prompt_addendum_v3.txt"
PI = os.environ.get("PI_BIN", str(Path.home() / ".hermes/node/bin/pi"))
AGENT_DIR = HERE / "pi-agent"
EXTENSION = HERE / "extension" / "heptapod.ts"
PROTOCOL = HERE / "prompts" / "protocol.md"
HEPVAL = HERE / "hepval.py"
AGENT_TIMEOUT = int(os.environ.get("PI_AGENT_TIMEOUT", str(4 * 3600)))

HARNESS_TOOLS = "read,write,edit,grep,find,ls,lint_model,validate_model,massbasis,review_model"

# The 16 single-model papers of ABLATION_2026-09-17.md, section 2.
SINGLE_MODEL = (
    "331,ALRM_general,B-L-SM,ChernSimonsPortal,EffLRSM,GeneralU1,HeavyN,MDMmodel,"
    "Monotops,NJLComposite,SLQrules,SMWeinberg,Top-Philic-Zprime,Wprime,pNG,pSPSS"
)

NOTOOLS_NOTE = """\
NO TOOLS: this run has no file, shell, network or code tools. Everything you need is in
this message: the Standard Model file SM.fr (the file this add-on is loaded on top of:
take field names, index conventions and hypercharges from it) and the paper. Do not ask
for anything; do the extraction and write the model."""

SANDBOX_NOTE = """\
SANDBOX: the working directory contains ONLY the paper (under eval/benchmark_runs/), SM.fr
(the Standard Model file this add-on is loaded on top of: take field names, index
conventions and hypercharges from it), and what you write. Nothing else exists and nothing
outside the working directory may be read. There is no shell."""


# ------------------------------------------------------------------ prompt
def paper_file(page: str) -> Path:
    texs = sorted((RUNS / page / "text").glob("*_source.tex"))
    if texs:
        return texs[0]
    txts = sorted((RUNS / page / "text").glob("*.txt"))
    if not txts:
        raise FileNotFoundError(f"no paper under {RUNS / page / 'text'}")
    return txts[0]


def _sub_once(text: str, pattern: str, repl: str, what: str) -> str:
    new, n = re.subn(pattern, lambda _m: repl, text, count=1, flags=re.M)
    if n != 1:
        raise ValueError(f"prompt template: could not find the {what} line to rewrite")
    return new


def _file_rules(base: str, page: str) -> str:
    """The no-tools arm's substitutions (rerun_extract.build_prompt, notools):
    no schema, the agent writes the whole .fr. Shared by both pi arms, so the
    task text is the same one the Claude Code arm had."""
    base = _sub_once(
        base,
        r"^SCHEMA: .*$",
        "FORMAT: write a complete FeynRules .fr add-on model file yourself "
        "(M$ModelName, M$Information, M$InteractionOrderHierarchy, IndexRange "
        "declarations for new indices, M$Parameters, M$ClassesDescription, the "
        "Lagrangian terms and one LTotal). It is loaded on top of SM.fr, included "
        "verbatim above between the SM.fr markers.",
        "SCHEMA",
    )
    base = _sub_once(
        base,
        r"^3\. Include the main new-physics lagrangian_terms .*$",
        "3. Write the main new-physics Lagrangian terms (FeynRules/Mathematica syntax and idioms).",
        "TASK item 3",
    )
    base = _sub_once(
        base,
        r"^SCHEMA RULES: .*$",
        "FILE RULES: use FeynRules syntax for every value (rationals -1/3, decimals "
        "1500.); SM add-on => no M$GaugeGroups block; the indices Colour, Gluon, "
        "Generation, SU2D and SU2W are declared by SM.fr; any OTHER index (a "
        "colour-sextet index, a new-generation index) needs "
        "`IndexRange[Index[X]] = NoUnfold[Range[n]];` with the correct size; every "
        "class gets a unique label S[n]/F[n]/V[n] with n >= 100; "
        "SelfConjugate -> False for complex fields (distinct antiparticle), True for "
        "real/Majorana fields.",
        "SCHEMA RULES",
    )
    return base


def build_prompt(page: str, arm: str) -> str:
    base = (RUNS / page / "prompt.txt").read_text()
    paper = paper_file(page)
    src = paper.name.endswith("_source.tex")
    src_note = (
        "the paper's LaTeX source: equations, fractions and roots are exact"
        if src
        else "text extracted from the PDF"
    )
    addendum = ADDENDUM.read_text().strip()
    base = _file_rules(base, page)
    if arm == "plain":
        base = _sub_once(
            base,
            r"^PAPER: .*$",
            f"PAPER: {src_note}, included verbatim above between the PAPER "
            "markers; it is authoritative.",
            "PAPER",
        )
        base = _sub_once(
            base,
            r"^OUTPUT: .*$",
            "OUTPUT: your FINAL message must contain exactly one fenced code block "
            "tagged mathematica containing ONLY the complete .fr file (no commentary "
            f'inside the fences). Set M$ModelName = "{page}_gen".',
            "OUTPUT",
        )
        base = base.rstrip() + "\n\n" + NOTOOLS_NOTE + "\n\n" + addendum + "\n"
        docs = (
            f"===== BEGIN SM.fr (tools/feynrules/test_files/models/SM.fr) =====\n"
            f"{SM_FR.read_text()}\n===== END SM.fr =====\n\n"
            f"===== BEGIN PAPER ({paper.name}; {src_note}) =====\n"
            f"{paper.read_text(errors='replace')}\n===== END PAPER =====\n\n"
        )
        return docs + base
    rel = f"eval/benchmark_runs/{page}/text/{paper.name}"
    base = base.replace(
        "included verbatim above between the SM.fr markers", "in the working directory as SM.fr"
    )
    base = _sub_once(
        base,
        r"^PAPER: .*$",
        f'PAPER: {src_note}, at "{rel}" in the working directory (read all of it '
        "with the read tool; it is authoritative).",
        "PAPER",
    )
    base = _sub_once(
        base,
        r"^OUTPUT: .*$",
        "OUTPUT: write the complete .fr file to model.fr in the working directory "
        f'with M$ModelName = "{page}_gen". model.fr as it stands when you stop is '
        "the deliverable. Your final message summarises the model and the last "
        "validate_model verdict.",
        "OUTPUT",
    )
    return base.rstrip() + "\n\n" + SANDBOX_NOTE + "\n\n" + addendum + "\n"


def make_sandbox(page: str, rundir: Path) -> Path:
    """Outside the repo (a sandbox path that names the repo invites reads
    through the real path, which happened once in the September reruns)."""
    sb = Path(tempfile.mkdtemp(prefix=f"pi-{page}-"))
    paper = paper_file(page)
    dst = sb / "eval" / "benchmark_runs" / page / "text" / paper.name
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(paper, dst)
    shutil.copy2(SM_FR, sb / "SM.fr")
    (rundir / "sandbox_path.txt").write_text(str(sb))
    return sb


# ------------------------------------------------------------------- agent
def _agent_env(sandbox: Path, rundir: Path, args) -> dict:
    env = dict(os.environ)
    env.update(
        {
            "PI_CODING_AGENT_DIR": str(AGENT_DIR),
            "PATH": f"{Path(PI).parent}:{env.get('PATH', '')}",
            "HEPTAPOD_SANDBOX": str(sandbox),
            "HEPTAPOD_RUNDIR": str(rundir),
            "HEPTAPOD_HEPVAL": str(HEPVAL),
            "HEPTAPOD_PYTHON": sys.executable,
            "HEPTAPOD_ROLE": "agent",
            "HEPTAPOD_ARM": args.arm,
            "HEPTAPOD_PI": PI,
            "HEPTAPOD_MODEL": args.model,
            "HEPTAPOD_VALIDATE_BUDGET": str(args.validate_budget),
            "HEPTAPOD_REVIEW_BUDGET": str(args.review_budget),
        }
    )
    if args.extra_ext:
        env["HEPTAPOD_REVIEW_EXTRA_EXT"] = args.extra_ext
    return env


def _link_auth() -> None:
    """Share the operator's pi login (``pi`` then ``/login``) with the harness
    agent dir, whose models.json and settings.json are the harness's own."""
    src = Path.home() / ".pi/agent/auth.json"
    dst = AGENT_DIR / "auth.json"
    if src.is_file() and not dst.exists():
        dst.symlink_to(src)


def _parse_stream(lines: list[str]) -> dict:
    tools: list[dict] = []
    usage = {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0, "cost": 0.0}
    final, n_turns, errors = "", 0, []
    for line in lines:
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = ev.get("type")
        if t == "tool_execution_start":
            tools.append({"tool": ev.get("toolName"), "args": ev.get("args")})
        elif t == "tool_execution_end" and ev.get("isError") and tools:
            tools[-1]["error"] = True
        elif t == "message_end":
            m = ev.get("message") or {}
            if m.get("role") != "assistant":
                continue
            n_turns += 1
            u = m.get("usage") or {}
            for k in ("input", "output", "cacheRead", "cacheWrite"):
                usage[k] += int(u.get(k) or 0)
            usage["cost"] += float((u.get("cost") or {}).get("total") or 0)
            if m.get("stopReason") == "error":
                errors.append(m.get("errorMessage"))
            texts = [b.get("text", "") for b in m.get("content") or [] if b.get("type") == "text"]
            if texts:
                final = "\n".join(texts)
    return {
        "tools": tools,
        "usage": usage,
        "final_text": final,
        "n_turns": n_turns,
        "errors": errors,
    }


def _audit(rundir: Path, sandbox: Path, parsed: dict) -> dict:
    """Server-side facts: the extension's own log of every call and block."""
    calls = []
    f = rundir / "tool_calls.jsonl"
    if f.is_file():
        calls = [json.loads(x) for x in f.read_text().splitlines() if x.strip()]
    blocked = [c for c in calls if c.get("event") == "blocked"]
    names = [t["tool"] for t in parsed["tools"]]
    return {
        "n_tool_calls": len(names),
        "tool_names": sorted(set(names)),
        "tool_counts": {n: names.count(n) for n in sorted(set(names))},
        "n_validate": names.count("validate_model"),
        "n_review": names.count("review_model"),
        "blocked": [{k: c.get(k) for k in ("tool", "path")} for c in blocked],
        # Paths the harness itself printed (its own output dir) are harness
        # leaks, not attempts to reach the answer key.
        "blocked_harness_paths": sum(
            str(c.get("path") or "").startswith(str(rundir)) for c in blocked
        ),
        # A blocked call never executed, so nothing outside the sandbox was read.
        "contaminated": False,
        "read_paper": any(
            t["tool"] == "read" and "text/" in json.dumps(t.get("args")) for t in parsed["tools"]
        ),
    }


_FENCE_RE = re.compile(r"```[ \t]*([A-Za-z0-9_+-]*)[ \t]*\n(.*?)```", re.S)


def _fr_block(md: str) -> str | None:
    """The last fenced block that looks like a FeynRules model file (as
    rerun_extract._fr_block)."""
    blocks = [(tag.lower(), body) for tag, body in _FENCE_RE.findall(md)]
    cands = [b for _t, b in blocks if "M$ModelName" in b or "M$ClassesDescription" in b]
    if not cands:
        cands = [b for t, b in blocks if t in ("mathematica", "wolfram", "fr", "feynrules")]
    return cands[-1] if cands else None


def run_agent(page: str, seed: int, args) -> dict:
    rundir = RUNS / page / "rerun" / args.variant / f"s{seed}"
    if (rundir / "run.json").is_file() and not args.force:
        prev = json.loads((rundir / "run.json").read_text())
        if (prev.get("agent") or {}).get("ok"):
            print(f"[pi] skip {page} s{seed}: done", flush=True)
            return prev
    if rundir.exists():
        shutil.rmtree(rundir)
    rundir.mkdir(parents=True)
    sandbox = make_sandbox(page, rundir)
    prompt = build_prompt(page, args.arm)
    (rundir / "prompt.txt").write_text(prompt)
    cmd = [
        PI,
        "-p",
        "--mode",
        "json",
        "--session-dir",
        str(rundir / "session"),
        "--no-extensions",
        "--no-skills",
        "--no-prompt-templates",
        "--no-context-files",
        "--no-themes",
        "--model",
        args.model,
    ]
    if args.thinking:
        cmd += ["--thinking", args.thinking]
    if args.arm == "harness":
        cmd += [
            "-e",
            str(EXTENSION),
            "--tools",
            HARNESS_TOOLS,
            "--append-system-prompt",
            str(PROTOCOL),
        ]
        for ext in filter(None, (args.extra_ext or "").split(",")):
            cmd += ["-e", ext]
    else:
        cmd += ["--no-tools"]
        for ext in filter(None, (args.extra_ext or "").split(",")):
            cmd += ["-e", ext]
    # The prompt is 100-200 KB in the plain arm: pass it as an @file, not argv.
    pfile = sandbox / "TASK.md" if args.arm == "harness" else rundir / "prompt.txt"
    if args.arm == "harness":
        pfile.write_text(prompt)
        cmd += [f"@{pfile}", "Your task is in TASK.md (attached above). Do it."]
    else:
        cmd += [f"@{pfile}", "Do the task above."]
    env = _agent_env(sandbox, rundir, args)
    print(f"[pi] {args.variant} {page} s{seed} ...", flush=True)
    t0 = time.time()
    with (
        open(rundir / "agent_stream.jsonl", "w") as out,
        open(rundir / "agent_stderr.txt", "w") as err,
    ):
        p = subprocess.Popen(
            cmd,
            cwd=str(sandbox),
            env=env,
            stdout=subprocess.PIPE,
            stderr=err,
            stdin=subprocess.DEVNULL,
            start_new_session=True,
            text=True,
            errors="replace",
        )
        killed = {"t": False}

        def _watchdog():
            while p.poll() is None:
                if time.time() - t0 > AGENT_TIMEOUT:
                    killed["t"] = True
                    os.killpg(os.getpgid(p.pid), signal.SIGTERM)
                    return
                time.sleep(10)

        threading.Thread(target=_watchdog, daemon=True).start()
        for line in p.stdout:
            # message_update carries the whole message so far on every token:
            # kept, one pNG run wrote 6.3 GB. The final message_end has it all.
            if not _STREAM_DROP.match(line):
                out.write(line)
        rc = p.wait()
    return finalize(page, seed, args, rundir, sandbox, rc, round(time.time() - t0, 1), killed["t"])


_STREAM_DROP = re.compile(r'^\{"type":"(message_update|tool_execution_update)"')


def finalize(
    page: str,
    seed: int,
    args,
    rundir: Path,
    sandbox: Path,
    rc: int,
    secs: float | None,
    timed_out: bool,
) -> dict:
    """Build run.json from what the agent left: the filtered event stream,
    the extension's tool log and the sandbox. Also rebuilds a run whose
    runner died (``run_pi.py finalize``)."""
    parsed = _parse_stream((rundir / "agent_stream.jsonl").read_text(errors="replace").splitlines())
    (rundir / "agent_out.md").write_text(parsed["final_text"])
    audit = _audit(rundir, sandbox, parsed)
    fr_dst = rundir / "model" / f"{page}_gen.fr"
    fr_dst.parent.mkdir(parents=True, exist_ok=True)
    if args.arm == "harness":
        src = sandbox / "model.fr"
        delivered = src.is_file()
        if delivered:
            shutil.copy2(src, fr_dst)
        if (sandbox / "validation").is_dir():
            shutil.copytree(
                sandbox / "validation", rundir / "validation_agent_view", dirs_exist_ok=True
            )
    else:
        body = _fr_block(parsed["final_text"])
        delivered = body is not None
        if delivered:
            fr_dst.write_text(body.rstrip() + "\n")
    agent = {
        "ok": rc == 0 and delivered and not timed_out,
        "exit": rc,
        "timed_out": timed_out,
        "seconds": secs,
        "engine": "pi",
        "pi_version": subprocess.run(
            [PI, "--version"], capture_output=True, text=True
        ).stdout.strip(),
        "model": args.model,
        "thinking": args.thinking,
        "arm": args.arm,
        "mode": "pi_harness" if args.arm == "harness" else "notools",
        "tool_policy": "enforced (pi --tools allowlist + sandbox guard)"
        if args.arm == "harness"
        else "enforced (--no-tools)",
        "audit_ok": not audit["blocked"],
        "audit_problems": audit["blocked"],
        "paper_inlined": args.arm == "plain",
        "usage": parsed["usage"],
        "n_turns": parsed["n_turns"],
        "errors": parsed["errors"][:3],
        "validate_budget": args.validate_budget,
        "review_budget": args.review_budget,
        **audit,
    }
    if args.arm == "plain":
        agent["read_paper"] = True
    row = {
        "page": page,
        "variant": args.variant,
        "seed": seed,
        "mode": agent["mode"],
        "paper_source": "tex" if paper_file(page).name.endswith("_source.tex") else "txt",
        "paper_file": paper_file(page).name,
        "agent": agent,
        "render": {"rendered": delivered, "fr": str(fr_dst) if delivered else None},
    }
    (rundir / "run.json").write_text(json.dumps(row, indent=1, default=str))
    print(
        f"[pi]   {page} s{seed}: ok={agent['ok']} delivered={delivered} {secs}s "
        f"tools={audit['tool_counts']} cost=${parsed['usage']['cost']:.2f}",
        flush=True,
    )
    return row


def cmd_finalize(args) -> int:
    """Rebuild run.json for runs whose runner died after the agent finished.
    The agent's wall time is taken from the first and last tool-log entries."""
    for page in [p for p in args.pages.split(",") if p]:
        rundir = RUNS / page / "rerun" / args.variant / f"s{args.seed}"
        sandbox = Path((rundir / "sandbox_path.txt").read_text().strip())
        stream = rundir / "agent_stream.jsonl"
        if stream.stat().st_size > 50_000_000:
            tmp = stream.with_suffix(".filtered")
            with open(stream, errors="replace") as src, open(tmp, "w") as dst:
                for line in src:
                    if not _STREAM_DROP.match(line):
                        dst.write(line)
            tmp.replace(stream)
        log = [
            json.loads(x)
            for x in (rundir / "tool_calls.jsonl").read_text().splitlines()
            if x.strip()
        ]
        secs = round(log[-1]["t"] - log[0]["t"], 1) if len(log) > 1 else None
        ended = any(r.get("event") == "agent_end" for r in log) or args.arm == "plain"
        finalize(page, args.seed, args, rundir, sandbox, 0 if ended else -1, secs, False)
    return 0


def cmd_run(args) -> int:
    _link_auth()
    pages = [p for p in (SINGLE_MODEL if args.pages == "all" else args.pages).split(",") if p]
    jobs = [(p, k) for p in pages for k in range(1, args.seeds + 1)]
    with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as ex:
        list(ex.map(lambda j: run_agent(j[0], j[1], args), jobs))
    return 0


# ------------------------------------------------------------------- score
def cmd_score(args) -> int:
    pages = [p for p in (SINGLE_MODEL if args.pages == "all" else args.pages).split(",") if p]
    for variant in args.variants.split(","):
        for page in pages:
            for k in range(1, args.seeds + 1):
                d = RUNS / page / "rerun" / variant / f"s{k}"
                fr = d / "model" / f"{page}_gen.fr"
                out = d / "validation_hepval.json"
                if not fr.is_file() or (out.is_file() and not args.force):
                    continue
                print(f"[score] {variant} {page} s{k} ...", flush=True)
                work = Path(tempfile.mkdtemp(prefix=f"score-{page}-"))
                r = subprocess.run(
                    [sys.executable, str(HEPVAL), "validate", str(fr), "--out", str(work)],
                    capture_output=True,
                    text=True,
                )
                summ = work / "call1" / "summary.json"
                if not summ.is_file():
                    print(f"[score]   validator error: {r.stderr[-400:]}", flush=True)
                    continue
                s = json.loads(summ.read_text())
                row = s["row"]
                v = {
                    "status": row.get("status"),
                    "compile_ok": row.get("compile_ok"),
                    "timed_out": row.get("timed_out"),
                    "seconds": row.get("seconds"),
                    "checks": row.get("checks"),
                    "madgraph_import_ok": row.get("madgraph_import_ok"),
                    "full_chain_pass": bool(row.get("full_pass")),
                    "lagrangian_expression": row.get("lagrangian_expression"),
                    "lag_symbol": row.get("lag_symbol"),
                    "error_tags": row.get("error_tags"),
                    "scorer": "hepval (heptapod-dev main 4bcbcf2 driver + ALE validation_benchmark)",
                    "scored_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                }
                out.write_text(json.dumps(v, indent=1, default=str))
                if variant.startswith("pi_"):
                    # ablation_report reads validation.json; the pi arms have no other.
                    (d / "validation.json").write_text(json.dumps(v, indent=1, default=str))
                shutil.copy2(
                    work / "call1" / "VALIDATION_REPORT.md", d / "VALIDATION_REPORT_final.md"
                )
                # The scored UFO's particle and vertex lists: a pass whose new
                # particles have no vertex is visible only there.
                for name in ("particles.py", "vertices.py"):
                    if (work / "call1" / "round0" / "UFO" / name).is_file():
                        (d / "score_ufo").mkdir(exist_ok=True)
                        shutil.copy2(
                            work / "call1" / "round0" / "UFO" / name, d / "score_ufo" / name
                        )
                print(
                    f"[score]   -> {v['status']} full_chain={v['full_chain_pass']} "
                    f"checks={v['checks']} mg5={v['madgraph_import_ok']}",
                    flush=True,
                )
    return 0


# ------------------------------------------------------------------ report
def cmd_report(args) -> int:
    pages = [p for p in (SINGLE_MODEL if args.pages == "all" else args.pages).split(",") if p]
    variants = args.variants.split(",")
    lines = ["| page | " + " | ".join(variants) + " |", "|---|" + "---|" * len(variants)]
    tot = {v: [0, 0, 0.0] for v in variants}
    for page in pages:
        cells = []
        for v in variants:
            d = RUNS / page / "rerun" / v / "s1"
            f = d / "validation_hepval.json"
            if not f.is_file():
                cells.append("no model" if (d / "run.json").is_file() else "—")
                if (d / "run.json").is_file():
                    tot[v][1] += 1
                continue
            r = json.loads(f.read_text())
            c = r.get("checks") or {}
            mark = "".join(
                {"pass": "✓", "fail": "✗", "inconclusive": "?"}.get(c.get(k), "·")
                for k in ("hermiticity", "kinetic_diagonal", "mass_diagonal", "mass_spectrum")
            )
            cells.append(
                ("**PASS**" if r.get("full_chain_pass") else r.get("status") or "fail")
                + f" {mark} mg5={'✓' if r.get('madgraph_import_ok') else '✗'}"
            )
            tot[v][0] += bool(r.get("full_chain_pass"))
            tot[v][1] += 1
            run = d / "run.json"
            if run.is_file():
                tot[v][2] += float(
                    ((json.loads(run.read_text()).get("agent") or {}).get("usage") or {}).get(
                        "cost"
                    )
                    or 0
                )
        lines.append(f"| {page} | " + " | ".join(cells) + " |")
    lines.append(
        "| **full chain** | " + " | ".join(f"**{tot[v][0]}/{len(pages)}**" for v in variants) + " |"
    )
    lines.append(
        "| agent cost (pi arms) | "
        + " | ".join(f"${tot[v][2]:.2f}" if v.startswith("pi_") else "—" for v in variants)
        + " |"
    )
    print("\n".join(lines))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--arm", choices=("harness", "plain"), required=True)
    r.add_argument("--variant", required=True)
    r.add_argument(
        "--pages", required=True, help="comma-separated, or 'all' for the 16 single-model papers"
    )
    r.add_argument("--model", default="anthropic/claude-sonnet-5")
    r.add_argument("--thinking", default="", help="pi thinking level; empty = pi default")
    r.add_argument("--seeds", type=int, default=1)
    r.add_argument("--parallel", type=int, default=4)
    r.add_argument("--validate-budget", type=int, default=6)
    r.add_argument("--review-budget", type=int, default=2)
    r.add_argument("--extra-ext", default="", help="extra extension(s), comma-separated (tests)")
    r.add_argument("--force", action="store_true")
    r.set_defaults(fn=cmd_run)
    f = sub.add_parser("finalize", help="rebuild run.json after a runner crash")
    f.add_argument("--arm", choices=("harness", "plain"), required=True)
    f.add_argument("--variant", required=True)
    f.add_argument("--pages", required=True)
    f.add_argument("--seed", type=int, default=1)
    f.add_argument("--model", required=True)
    f.add_argument("--thinking", default="")
    f.add_argument("--validate-budget", type=int, default=6)
    f.add_argument("--review-budget", type=int, default=2)
    f.set_defaults(fn=cmd_finalize)
    s = sub.add_parser("score")
    s.add_argument("--variants", required=True)
    s.add_argument("--pages", required=True)
    s.add_argument("--seeds", type=int, default=1)
    s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_score)
    p = sub.add_parser("report")
    p.add_argument("--variants", required=True)
    p.add_argument("--pages", required=True)
    p.set_defaults(fn=cmd_report)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
