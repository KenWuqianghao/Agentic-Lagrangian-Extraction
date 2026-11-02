#!/usr/bin/env python3
"""Stop gate and referee of the pi harness.

    gate.py review MODEL.fr           the review_model tool (agent's budget)
    gate.py stop --validations N      the agent stopped: may it?

``stop`` prints ``{"message": ...}``. A message goes back to the agent as its
next user turn; null lets the run end. The agent is sent back while model.fr
is missing, never validated, changed since its last validation, or failing
(cc_harness/hooks/stop_gate.py decides, the Claude Code harness's rule). When
the stop is allowed, the referee runs on model.fr unless a review of exactly
that file exists, so the file that gets scored is always reviewed; the agent
does not choose. A review that is not clean goes back to the agent while a
continuation and a validation are left.

Nothing here keeps a state file. The last verdict is the newest
``validation/call<n>/`` that hepval wrote (summary.json, the validated
model.fr, agent_report.md); the reviews are ``review/review<n>.json``. Both
sit in the run directory, which the agent cannot write.

Environment (set by run_pi.py): HEPTAPOD_SANDBOX, HEPTAPOD_RUNDIR,
HEPTAPOD_PI, HEPTAPOD_MODEL, HEPTAPOD_REVIEW_MODEL, HEPTAPOD_REVIEW_EXTRA_EXT,
HEPTAPOD_VALIDATE_BUDGET, HEPTAPOD_REVIEW_BUDGET, HEPTAPOD_MAX_CONTINUATIONS.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "cc_harness"))
sys.path.insert(0, str(HERE.parent / "cc_harness" / "hooks"))
import common as C  # noqa: E402
import stop_gate  # noqa: E402
from heptapod_mcp import REVIEW_PROMPT  # noqa: E402

EXTENSION = HERE / "extension" / "heptapod.ts"
REFEREE_TIMEOUT = 3600


def _num(p: Path) -> int:
    return int(re.search(r"(\d+)", p.name).group(1))


def last_validation(rundir: Path) -> dict | None:
    calls = sorted((rundir / "validation").glob("call*/summary.json"), key=lambda p: _num(p.parent))
    if not calls:
        return None
    d = calls[-1].parent
    s = json.loads(calls[-1].read_text())
    return {"call": s["call"], "stage": s["stage_reached"], "full_chain_pass": s["full_chain_pass"],
            "model_sha": C.sha(d / "model.fr"), "report": str(d / "agent_report.md")}


def reviews(rundir: Path) -> list[dict]:
    return [json.loads(p.read_text()) for p in sorted((rundir / "review").glob("review*.json"), key=_num)]


def review_of(rundir: Path, fr: Path) -> dict | None:
    """The newest completed review of exactly this file."""
    sha = C.sha(fr)
    done = [r for r in reviews(rundir) if r["model_sha"] == sha and r["ok"]]
    return done[-1] if done else None


def clean(verdict: str | None) -> bool:
    """True only when the referee's VERDICT line reports no physics-changing
    discrepancy. A report without the line is not clean."""
    v = (verdict or "").upper()
    return "NO DISCREPANCIES" in v or bool(re.search(r"\b0\s+PHYSICS-CHANGING", v))


def referee(sandbox: Path, rundir: Path, fr: Path, origin: str, env: dict) -> dict:
    """Run a fresh pi agent, in its own directory with the paper, SM.fr and a
    frozen copy of ``fr``, and record its report as review<n>."""
    out = rundir / "review"
    out.mkdir(parents=True, exist_ok=True)
    n = len(reviews(rundir)) + 1
    shutil.copy2(fr, out / f"review{n}.fr")
    rev = C.referee_sandbox(sandbox, fr)
    model = env.get("HEPTAPOD_REVIEW_MODEL") or env.get("HEPTAPOD_MODEL")
    cmd = [env.get("HEPTAPOD_PI") or "pi", "-p", "--no-session", "--no-context-files", "--no-skills",
           "--no-prompt-templates", "--no-extensions", "-e", str(EXTENSION)]
    # Tests load a scripted provider into the referee too.
    for ext in filter(None, (env.get("HEPTAPOD_REVIEW_EXTRA_EXT") or "").split(",")):
        cmd += ["-e", ext]
    cmd += ["--tools", "read,grep,find,ls", *(["--model", model] if model else []),
            REVIEW_PROMPT.replace("MODEL_PATH", C.REVIEW_COPY)]
    t0 = time.time()
    try:
        r = subprocess.run(cmd, cwd=str(rev), capture_output=True, text=True, stdin=subprocess.DEVNULL,
                           timeout=REFEREE_TIMEOUT,
                           env={**env, "HEPTAPOD_ROLE": "reviewer", "HEPTAPOD_SANDBOX": str(rev)})
        code, text, err = r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        code, text, err = -1, "", f"referee timed out after {REFEREE_TIMEOUT} s"
    (out / f"review{n}.md").write_text(text)
    verdict = next((ln.strip() for ln in reversed(text.splitlines())
                    if ln.strip().upper().startswith("VERDICT:")), None)
    rec = {"n": n, "origin": origin, "model_sha": C.sha(fr), "ok": code == 0 and bool(text.strip()),
           "verdict": verdict, "exit": code, "seconds": round(time.time() - t0, 1), "model": model,
           "stderr": err[-800:]}
    (out / f"review{n}.json").write_text(json.dumps(rec, indent=1))
    return {**rec, "text": text}


def final_review(sandbox: Path, rundir: Path, fr: Path, origin: str, env: dict) -> dict:
    """The review of exactly ``fr``: the stored one, or a new one."""
    return review_of(rundir, fr) or referee(sandbox, rundir, fr, origin, env)


def stop(sandbox: Path, rundir: Path, validations: int, env: dict) -> str | None:
    """The message that sends the agent back to work, or None to let it stop."""
    budget = int(env.get("HEPTAPOD_VALIDATE_BUDGET") or 6)
    limit = int(env.get("HEPTAPOD_MAX_CONTINUATIONS") or 3)
    st = {"validations": validations, "validate_budget": budget, "last_validation": last_validation(rundir)}
    d = stop_gate.decide({}, sandbox, rundir, st, limit)
    model = sandbox / "model.fr"
    if d["block"] or not model.is_file() or review_of(rundir, model):
        return d["reason"]
    rev = referee(sandbox, rundir, model, "stop_gate", env)
    gf = rundir / "stop_gate.json"
    k = json.loads(gf.read_text())["continuations"] if gf.is_file() else 0
    why = ("the referee failed" if not rev["ok"] else
           "the review is clean" if clean(rev["verdict"]) else
           "the model failed the chain and the gate already let it stop" if not d["model_ok"] else
           f"continuation limit reached ({limit})" if k >= limit else
           "validate_model budget spent; an edit could not be validated" if validations >= budget else None)
    rec = {"hook": "review", "review": rev["n"], "verdict": rev["verdict"], "continuations_before": k, "limit": limit}
    if why:
        C.log(rundir, "stop_gate_log.jsonl", {**rec, "decision": "allow", "why": why})
        return None
    gf.write_text(json.dumps({"continuations": k + 1}))
    C.log(rundir, "stop_gate_log.jsonl", {**rec, "decision": "block", "why": "the review of the final model is not clean"})
    return (f"[stop gate {k + 1}/{limit}] An independent referee compared the model.fr you handed in with the "
            "paper. Fix every physics-changing discrepancy in model.fr, then lint and validate it again. "
            "If none of them changes the physics, say so and stop. The referee's report:\n\n" + rev["text"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("review")
    p.add_argument("model")
    p = sub.add_parser("stop")
    p.add_argument("--validations", type=int, required=True)
    args = ap.parse_args()
    env = dict(os.environ)
    sandbox, rundir = Path(env["HEPTAPOD_SANDBOX"]).resolve(), Path(env["HEPTAPOD_RUNDIR"]).resolve()
    if args.cmd == "stop":
        print(json.dumps({"message": stop(sandbox, rundir, args.validations, env)}))
        return 0
    budget = int(env.get("HEPTAPOD_REVIEW_BUDGET") or 2)
    used = sum(r["origin"] == "agent" for r in reviews(rundir))
    if used >= budget:
        raise SystemExit(f"review budget exhausted ({budget} calls)")
    rev = referee(sandbox, rundir, Path(args.model), "agent", env)
    if not rev["ok"]:
        raise SystemExit(f"reviewer failed (exit {rev['exit']}): {rev['stderr']}")
    print(f"review {used + 1}/{budget} of {Path(args.model).name}\n\n{rev['text']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
