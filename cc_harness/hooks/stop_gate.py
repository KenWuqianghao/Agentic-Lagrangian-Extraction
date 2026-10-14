#!/usr/bin/env python3
"""Stop hook: the agent may not finish with a failing model.

When the agent tries to stop, block (and send it back to work) if
  - model.fr does not exist, or
  - it never ran validate_model, or
  - the last validate_model did not report a pass (the full chain; in the
    compile-feedback arm, the compile), or
  - model.fr changed after the last validate_model (the verdict is stale).
The reason returned to the agent is a digest of the last report.

Two limits keep this from looping:
  - at most CC_MAX_CONTINUATIONS blocks per run (default 3), counted in
    CC_RUNDIR/stop_gate.json across all stops; `stop_hook_active` (true when
    this stop comes right after a block) is recorded with each decision;
  - once the validate_model budget is spent, a block cannot lead to a new
    verdict, so the gate lets the agent stop and records why.
Every decision, block or allow, goes to CC_RUNDIR/stop_gate_log.jsonl.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import common as C  # noqa: E402


def digest(report_path: str | None, limit: int = 2500) -> str:
    """The head of the last report: stage, verdicts and the first detail
    sections, without the long compile log."""
    if not report_path or not Path(report_path).is_file():
        return "(no report on disk)"
    text = Path(report_path).read_text(errors="replace")
    text = text.split("## compile log, distinct lines (tail)")[0]
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text[:limit].rstrip() + ("\n..." if len(text) > limit else "")


def decide(event: dict, sandbox: Path, rundir: Path) -> dict:
    st = C.load_state(rundir)
    gate = {"continuations": 0}
    gf = rundir / "stop_gate.json"
    if gf.is_file():
        try:
            gate = json.loads(gf.read_text())
        except json.JSONDecodeError:
            pass
    k = int(gate.get("continuations", 0))
    limit = C.env_int("CC_MAX_CONTINUATIONS", 3)
    model = sandbox / "model.fr"
    last = st.get("last_validation")
    reason = None
    if not model.is_file():
        reason = "model.fr does not exist in the working directory. Write the model to model.fr, lint it and validate it."
    elif not last:
        reason = "You have not run validate_model. Lint model.fr, then validate it, and fix what the report names."
    elif last.get("model_sha") != C.sha(model):
        reason = (
            f"model.fr changed after the last validate_model (call {last.get('call')}), so its verdict "
            "does not apply to the file you would hand in. Validate the current model.fr."
        )
    elif not last.get("told_pass"):
        reason = (
            f"The last validate_model (call {last.get('call')}) did not pass: stage reached = "
            f"{last.get('stage')}. Fix the cause and validate again. Digest of that report:\n\n"
            + digest(last.get("report"))
        )
    rec = {
        "hook": "Stop",
        "stop_hook_active": bool(event.get("stop_hook_active")),
        "continuations_before": k,
        "limit": limit,
        "validations": st.get("validations"),
        "validate_budget": st.get("validate_budget"),
        "last_call": (last or {}).get("call"),
        "last_stage": (last or {}).get("stage"),
    }
    if reason is None:
        rec.update(decision="allow", why="last validation passed and model.fr is unchanged")
    elif k >= limit:
        rec.update(
            decision="allow",
            why=f"continuation limit reached ({limit}); stopping with: {reason[:200]}",
        )
        reason = None
    elif st.get("validations", 0) >= st.get("validate_budget", 10) and model.is_file() and last:
        rec.update(
            decision="allow",
            why=f"validate_model budget spent; a block cannot produce a new verdict: {reason[:200]}",
        )
        reason = None
    else:
        gate["continuations"] = k + 1
        gf.write_text(json.dumps(gate))
        rec.update(decision="block", why=reason[:300])
        reason = f"[stop gate {k + 1}/{limit}] {reason}"
    C.log(rundir, "stop_gate_log.jsonl", rec)
    return {"block": reason is not None, "reason": reason, "record": rec}


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}
    d = decide(event, C.sandbox(), C.rundir())
    if d["block"]:
        print(json.dumps({"decision": "block", "reason": d["reason"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
