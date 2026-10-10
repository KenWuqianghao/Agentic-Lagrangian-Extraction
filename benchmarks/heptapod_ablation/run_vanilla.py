#!/usr/bin/env python3
"""The vanilla baseline: Claude Code with a shell and nothing else.

No heptapod tool, no skill, no protocol prompt, no Stop gate, no validate
budget. The agent gets the paper, SM.fr and a short task, and it may run
`wolframscript` (FeynRules) and MadGraph itself, as a person without
heptapod would.

    run_vanilla.py run --pages HeavyN [--variant cc_vanilla] [--parallel 2]
    cc_harness/run_cc.py score --variants cc_vanilla --pages all      # the same scorer as every arm

Isolation, so the agent cannot read a stored answer:
  - on Linux bubblewrap hides ~/code, ~/Documents and the session's /tmp; on
    macOS sandbox-exec denies reads under ~/Documents and ~/code; the working
    directory holds the paper and SM.fr only;
  - WebFetch and WebSearch are off, and the task forbids downloads; every
    shell command is in the stream, and `audit` in run.json lists the ones
    that reach for the network.
The licence allows two Wolfram kernels at a time, so `wolframscript` in the
agent's PATH is a wrapper that takes hepval's lock: runs queue instead of
failing with a licence error the agent could not understand.
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
ALE = HERE.parent.parent
sys.path.insert(0, str(ALE / "cc_harness"))
sys.path.insert(0, str(ALE / "pi_harness"))
import common as C  # noqa: E402
import run_cc  # noqa: E402
import run_pi  # noqa: E402

import isolation  # noqa: E402

HOME = Path.home()
FEYNRULES, MG5 = isolation.FEYNRULES, isolation.MG5
LOCK = Path(os.environ.get("HEPVAL_STATE", HOME / ".cache/ale-pi-harness")) / "wolfram.lock"
AGENT_TIMEOUT = int(os.environ.get("VANILLA_AGENT_TIMEOUT", str(2 * 3600)))
NETWORK = re.compile(r"\b(curl|wget|git\s+clone|pip\s+install|pip3\s+install|scp|ssh|nc)\b")

# Two rules of the scorer that the first vanilla run was not told (it cost that run up to four
# papers). `--scorer-rules` adds them; the harness arms have always had them.
SCORER_RULES = """
  The scorer evaluates LTotal as written when it contains LSM, and LSM + LTotal when it does
  not: so write LTotal := LSM + <your terms> (or LSM - <an SM term you replace> + ...), and
  do not rebuild the Standard Model from its pieces. Define no other top-level L... := term
  that LTotal does not use."""

TASK = """\
Implement the beyond-the-Standard-Model theory of the paper in this directory as a FeynRules
model.

- The paper is {paper} ({src_note}). It is the only source: do not download or look for an
  existing implementation of this model.
- Write a FeynRules add-on file, model.fr, in this directory, with M$ModelName = "{page}_gen".
  It is loaded together with the Standard Model file SM.fr (in this directory; do not edit it),
  as LoadModel["SM.fr", "model.fr"]. Define the total Lagrangian as LTotal.{rules}
- The model must reproduce the paper's fields, interactions, parameters and benchmark values.
- It is good when: FeynRules loads it and writes a UFO; FeynRules' CheckHermiticity,
  CheckDiagonalKineticTerms, CheckDiagonalMassTerms and CheckMassSpectrum pass on LTotal;
  and MadGraph imports the UFO with `import model`.

This machine has: wolframscript (Wolfram Engine) on the PATH; FeynRules 2.3.49 in
{feynrules}; MadGraph5_aMC@NLO 3.7.3 in {mg5} (bin/mg5_aMC). You have a shell. model.fr as it
stands when you stop is the deliverable.
"""

def make_sandbox(page: str, rundir: Path) -> Path:
    sb = Path(tempfile.mkdtemp(prefix=f"vanilla-{page}-")).resolve()
    paper = run_pi.paper_file(page)
    shutil.copy2(paper, sb / paper.name)
    shutil.copy2(run_pi.SM_FR, sb / "SM.fr")
    isolation.write_wolframscript_wrapper(sb, LOCK)
    (rundir / "sandbox_path.txt").write_text(str(sb))
    return sb


def agent_cmd(sandbox: Path, model: str) -> list[str]:
    claude = [C.CLAUDE, "-p", "--output-format", "stream-json", "--verbose", "--model", model,
              "--setting-sources", "", "--strict-mcp-config", "--mcp-config", '{"mcpServers": {}}',
              "--permission-mode", "bypassPermissions",
              "--disallowedTools", "WebFetch,WebSearch,Task,Agent"]
    return isolation.isolate(claude, sandbox, read_write=(LOCK.parent,))


def audit(stream: list[str]) -> dict:
    cmds = []
    for line in stream:
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        for b in ((ev.get("message") or {}).get("content") or []) if ev.get("type") == "assistant" else []:
            if b.get("type") == "tool_use" and b.get("name") == "Bash":
                cmds.append((b.get("input") or {}).get("command") or "")
    net = [c[:300] for c in cmds if NETWORK.search(c)]
    return {"shell_commands": len(cmds), "wolframscript_runs": sum("wolframscript" in c for c in cmds),
            "madgraph_runs": sum("mg5_aMC" in c for c in cmds), "network_commands": net, "audit_ok": not net}


def run_agent(page: str, seed: int, args) -> dict:
    rundir = run_cc.RUNS / page / "rerun" / args.variant / f"s{seed}"
    if (rundir / "run.json").is_file() and not args.force:
        print(f"[vanilla] skip {page} s{seed}: done", flush=True)
        return json.loads((rundir / "run.json").read_text())
    if rundir.exists():
        shutil.rmtree(rundir)
    rundir.mkdir(parents=True)
    sandbox = make_sandbox(page, rundir)
    paper = run_pi.paper_file(page)
    prompt = TASK.format(paper=paper.name, page=page, feynrules=FEYNRULES, mg5=MG5, rules=SCORER_RULES if args.scorer_rules else "",
                         src_note="LaTeX source" if paper.name.endswith("_source.tex") else "text from the PDF")
    (rundir / "prompt.txt").write_text(prompt)
    cmd = agent_cmd(sandbox, args.model)
    (rundir / "command.json").write_text(json.dumps(cmd, indent=1))
    env = {**os.environ, "PATH": f"{sandbox / '.bin'}:{os.environ['PATH']}",
           "FEYNRULES_PATH": str(FEYNRULES), "MG5_PATH": str(MG5)}
    print(f"[vanilla] {args.variant} {page} s{seed} ...", flush=True)
    t0 = time.time()
    timed_out = {"t": False}
    with open(rundir / "agent_stream.jsonl", "w") as out, open(rundir / "agent_stderr.txt", "w") as err:
        p = subprocess.Popen(cmd, cwd=str(sandbox), env=env, stdin=subprocess.PIPE, stdout=out, stderr=err,
                             start_new_session=True, text=True)

        def watchdog():
            while p.poll() is None:
                if time.time() - t0 > AGENT_TIMEOUT:
                    timed_out["t"] = True
                    os.killpg(os.getpgid(p.pid), signal.SIGTERM)
                    return
                time.sleep(10)
        threading.Thread(target=watchdog, daemon=True).start()
        p.stdin.write(prompt)
        p.stdin.close()
        rc = p.wait()
    secs = round(time.time() - t0, 1)
    lines = (rundir / "agent_stream.jsonl").read_text(errors="replace").splitlines()
    parsed = run_cc.parse_stream(lines)
    (rundir / "agent_out.md").write_text(parsed["final_text"] or "")
    fr = rundir / "model" / f"{page}_gen.fr"
    fr.parent.mkdir(exist_ok=True)
    delivered = (sandbox / "model.fr").is_file()
    if delivered:
        shutil.copy2(sandbox / "model.fr", fr)
    names = parsed["tools"]
    agent = {"ok": delivered and not parsed["is_error"], "exit": rc, "timed_out": timed_out["t"], "seconds": secs,
             "engine": "claude-code", "model": args.model, "arm": "vanilla", "mode": "cc_vanilla",
             "tool_policy": "shell allowed; bubblewrap hides the repositories and stored runs; no web tools",
             "usage": parsed["usage"], "cost_usd": parsed["cost_usd"], "num_turns": parsed["num_turns"],
             "api_error": parsed["api_error"], "tool_counts": {n: names.count(n) for n in sorted(set(names))},
             **audit(lines), "init": parsed["init"]}
    row = {"page": page, "variant": args.variant, "seed": seed, "mode": "cc_vanilla", "paper_file": paper.name,
           "agent": agent, "render": {"rendered": delivered, "fr": str(fr) if delivered else None}}
    (rundir / "run.json").write_text(json.dumps(row, indent=1, default=str))
    u = parsed["usage"]
    print(f"[vanilla]   {page} s{seed}: delivered={delivered} {secs}s timed_out={timed_out['t']} "
          f"wolfram={agent['wolframscript_runs']} mg5={agent['madgraph_runs']} net={len(agent['network_commands'])} "
          f"in={u['input_total']:,} out={u['output_tokens']:,} ${parsed['cost_usd']:.2f}", flush=True)
    return row


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--variant", default="cc_vanilla")
    r.add_argument("--pages", required=True)
    r.add_argument("--model", default="claude-sonnet-5")
    r.add_argument("--seeds", type=int, default=1, help="the last seed")
    r.add_argument("--first-seed", type=int, default=1)
    r.add_argument("--parallel", type=int, default=2)
    r.add_argument("--force", action="store_true")
    r.add_argument("--scorer-rules", action="store_true",
                   help="tell the agent the scorer's two interface rules (LSM, one total)")
    args = ap.parse_args()
    pages = (run_pi.SINGLE_MODEL if args.pages == "all" else args.pages).split(",")
    LOCK.parent.mkdir(parents=True, exist_ok=True)
    jobs = [(p, k) for p in pages for k in range(args.first_seed, args.seeds + 1)]
    with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as ex:
        list(ex.map(lambda j: run_agent(j[0], j[1], args), jobs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
