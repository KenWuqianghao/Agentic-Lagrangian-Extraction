#!/usr/bin/env python3
"""Cost and time of one seed of each ablation arm, estimated from the stored
harness run (cc_sonnet_harness, budget 10) by cutting each run where the arm
would have stopped:

  none      at the start of the first validate call (the first draft)
  compile   at the end of the first call whose compile was good
  heptapod, full   at the end of the first passing call, or of call B

The cost up to a cut is the run's cost times the fraction of its agent time
before the cut (wall time minus the time inside validate_model and
review_model calls, which is kernel queue and referee, not agent tokens).
That is an estimate with a known bias: the cost per minute rises during a
run (the context grows), so a time fraction overstates an early cut.
The heptapod arm has no stored run: it is costed as the full arm without the
referee calls. Kernel seconds are the stored compile seconds times the local
time ratio measured by local_rescore.py.

    design_cost.py --budget 6 --ratio 1.45 --papers B-L-SM,ChernSimonsPortal,...
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import retro  # noqa: E402

REFEREE_USD = 0.65        # mean cost of one stored referee call (see main)


def cuts(d: Path, calls: list[dict], budget: int) -> dict | None:
    hooks = retro._jsonl(d / "hook_log.jsonl")
    tools = retro._jsonl(d / "tool_calls.jsonl")
    agent = (retro._json(d / "run.json") or {}).get("agent") or {}
    if not hooks or not agent.get("seconds") or not calls:
        return None
    t0, t1 = hooks[0]["t"], hooks[0]["t"] + agent["seconds"]
    v_start = [e["t"] for e in tools if e.get("event") == "call" and e.get("tool") == "validate_model"]
    v_end = [e["t"] for e in tools if e.get("event") in ("result", "error") and e.get("tool") == "validate_model"]
    waits, open_call = [], None
    for e in tools:
        if e.get("tool") in ("validate_model", "review_model"):
            if e.get("event") == "call":
                open_call = e["t"]
            elif open_call is not None:
                waits.append((open_call, e["t"]))
                open_call = None

    def active(t):
        return (t - t0) - sum(min(b, t) - a for a, b in waits if a < t)

    def frac(t):
        return max(0.0, min(1.0, active(t) / active(t1)))

    first_compile = next((i for i, c in enumerate(calls) if c["state"]["compile"] == "pass"), None)
    first_pass = next((i for i, c in enumerate(calls) if c["pass"]), None)
    stop_compile = min(first_compile if first_compile is not None else budget - 1, budget - 1, len(calls) - 1)
    stop_loop = min(first_pass if first_pass is not None else budget - 1, budget - 1, len(calls) - 1)
    # A run that passes keeps working after the call (the referee, the summary): cost it in full.
    loop_frac = 1.0 if (first_pass is not None and first_pass <= budget - 1 and len(calls) <= budget) else frac(v_end[stop_loop])
    return {"none": frac(v_start[0]), "compile": frac(v_end[stop_compile]), "loop": loop_frac,
            "calls_compile": stop_compile + 1, "calls_loop": stop_loop + 1,
            "kernel_compile": sum(c["seconds"] or 0 for c in calls[:stop_compile + 1]),
            "kernel_loop": sum(c["seconds"] or 0 for c in calls[:stop_loop + 1])}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--budget", type=int, default=6)
    ap.add_argument("--ratio", type=float, required=True, help="local / stored compile time (local_rescore.py)")
    ap.add_argument("--papers", required=True)
    ap.add_argument("--runs", default=os.environ.get(
        "PI_HARNESS_RUNS", str(Path.home() / "Documents/Github/heptapod/eval/benchmark_runs")))
    args = ap.parse_args()
    rows = []
    for paper in args.papers.split(","):
        d = Path(args.runs) / paper / "rerun" / "cc_sonnet_harness" / "s1"
        run = retro.load_run(Path(args.runs), paper, "cc_sonnet_harness")
        agent = (retro._json(d / "run.json") or {}).get("agent") or {}
        c = cuts(d, run["calls"], args.budget)
        if not c:
            continue
        agent_usd = float(agent.get("cost_usd") or 0)
        review_usd = sum(float(r.get("cost_usd") or 0) for r in agent.get("reviews") or [])
        score_s = (retro._json(d / "validation_hepval.json") or {}).get("seconds") or 0
        rows.append({"paper": paper, "stored_usd": round(agent_usd + review_usd, 2), "stored_minutes": round(agent["seconds"] / 60),
                     "usd": {"none": round(agent_usd * c["none"], 2), "compile": round(agent_usd * c["compile"], 2),
                             "heptapod": round(agent_usd * c["loop"], 2),
                             "full": round(agent_usd * c["loop"] + review_usd, 2)},
                     "validate_calls": {"none": 0, "compile": c["calls_compile"], "heptapod": c["calls_loop"], "full": c["calls_loop"]},
                     "kernel_seconds": {"none": 0, "compile": c["kernel_compile"], "heptapod": c["kernel_loop"], "full": c["kernel_loop"]},
                     "score_seconds": score_s})
    arms = ("none", "compile", "heptapod", "full")
    n = len(rows)
    per_seed = {}
    for a in arms:
        in_loop = sum(r["kernel_seconds"][a] for r in rows) * args.ratio
        scoring = sum(r["score_seconds"] for r in rows) * args.ratio
        per_seed[a] = {"agent_usd": round(sum(r["usd"][a] for r in rows), 1),
                       # The endpoint needs a referee verdict on every chain pass, in every arm.
                       "post_hoc_referee_usd_at_most": round(REFEREE_USD * n, 1),
                       "validate_calls": sum(r["validate_calls"][a] for r in rows),
                       "kernel_hours": round((in_loop + scoring) / 3600, 2)}
    total_usd = sum(v["agent_usd"] + v["post_hoc_referee_usd_at_most"] for v in per_seed.values())
    total_kernel = sum(v["kernel_hours"] for v in per_seed.values())
    print(json.dumps({"papers": n, "budget": args.budget, "local_time_ratio": args.ratio, "per_seed": per_seed,
                      "all_arms_one_seed_usd": round(total_usd, 1), "all_arms_one_seed_kernel_hours": round(total_kernel, 1),
                      "rows": rows}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
