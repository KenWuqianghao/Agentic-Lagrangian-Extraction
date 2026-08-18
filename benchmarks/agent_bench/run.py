#!/usr/bin/env python3
"""
Run the agent benchmark: a matrix of (case x driver x model).

    python benchmarks/agent_bench/run.py --list
    python benchmarks/agent_bench/run.py --driver claude_code --tier 1,2
    python benchmarks/agent_bench/run.py --dry-run

Scoring never asks a model whether it succeeded. Each case is judged on an
artifact an independent checker can verify — a .fr that contains what
FeynRules requires, a number that matches a live archive query. A model that
writes a confident summary and no file scores zero.

Two things are recorded that a naive harness would drop, because both are
ways a benchmark lies to you:

  * required-tool coverage — did the run actually call the tools the case
    cannot be solved without, or did it answer from memory?
  * harness/tool-server discrepancy — did the harness claim tool calls the
    tool server never saw?
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))

from benchmarks.agent_bench.cases import Case, default_cases  # noqa: E402
from benchmarks.agent_bench.drivers import (  # noqa: E402
    DRIVERS, DriverUnavailable, availability,
)

HEPTAPOD = Path("/Users/kenwu/Documents/Github/heptapod")
OUT_ROOT = HERE.parent / "agent_bench_runs"


def required_tool_coverage(trace, case: Case) -> Dict[str, Any]:
    """Did the run call what the case cannot be solved without?

    A case answered without its required tools was answered from memory. That
    can still produce correct-looking text, which is exactly why the check
    exists.
    """
    called = set(trace.distinct_tools)

    def norm(n: str) -> str:
        """Compare tool identities across three different spellings.

        A case names the Python class (``ArxivSearchTool``); the MCP server
        serves it as ``Arxivsearch``; the harness reports it prefixed as
        ``mcp__heptapod__Arxivsearch``. Comparing raw strings marks every
        satisfied requirement as missing, which turns the one check that
        catches memory-answers into noise.
        """
        n = n.lower()
        if n.startswith("mcp__"):
            n = n.rsplit("__", 1)[-1]
        return n[:-4] if n.endswith("tool") else n

    called_norm = {norm(c) for c in called}
    missing = [t for t in case.required_tools if norm(t) not in called_norm]
    return {
        "required": case.required_tools,
        "called": sorted(called),
        "missing": missing,
        "satisfied": not missing,
    }


def run_one(case: Case, driver_name: str, model: str,
            out_root: Path) -> Dict[str, Any]:
    driver = DRIVERS.get(driver_name)
    if driver is None:
        return {"case_id": case.case_id, "driver": driver_name,
                "status": "error", "reason": f"unknown driver {driver_name}"}

    reason = driver.available()
    if reason:
        return {"case_id": case.case_id, "driver": driver_name,
                "model": model, "status": "unavailable", "reason": reason}

    workdir = out_root / f"{case.case_id}__{driver_name}__{model or 'default'}"
    print(f"\n[bench] {case.case_id}  driver={driver_name}  model={model}",
          flush=True)
    try:
        trace = driver.run(case, workdir, model)
    except DriverUnavailable as e:
        return {"case_id": case.case_id, "driver": driver_name,
                "status": "unavailable", "reason": str(e)}

    trace.write(workdir / "trace.json")

    final_text = " ".join(e.text or "" for e in trace.events
                          if e.kind == "message")[-4000:]
    score = case.score(workdir, {"heptapod": str(HEPTAPOD),
                                 "final_text": final_text})
    coverage = required_tool_coverage(trace, case)

    row = {
        "case_id": case.case_id,
        "tier": case.tier,
        "driver": driver_name,
        "model": model or "default",
        "status": "ran",
        "wall_seconds": trace.wall_seconds,
        "n_tool_calls": trace.n_tool_calls,
        "n_failed_tool_calls": trace.n_failed_tool_calls,
        "tools_used": trace.distinct_tools,
        "required_tool_coverage": coverage,
        "score": score,
        "notes": trace.notes,
        "workdir": str(workdir),
    }
    print(f"[bench]   tools={trace.n_tool_calls} "
          f"({trace.n_failed_tool_calls} failed)  "
          f"required={'ok' if coverage['satisfied'] else 'MISSING ' + str(coverage['missing'])}  "
          f"score={score.get('passed')}  {trace.wall_seconds}s", flush=True)
    return row


def main() -> int:
    ap = argparse.ArgumentParser(description="Agentic toolkit benchmark")
    ap.add_argument("--driver", default="claude_code",
                    help="comma-separated driver names, or 'all'")
    ap.add_argument("--model", default="", help="model id for the driver")
    ap.add_argument("--tier", default="", help="comma-separated tiers to run")
    ap.add_argument("--case", default="", help="comma-separated case ids")
    ap.add_argument("--list", action="store_true", help="list cases and exit")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would run, and what cannot")
    args = ap.parse_args()

    cases = default_cases()
    if args.tier:
        want = {int(t) for t in args.tier.split(",") if t.strip()}
        cases = [c for c in cases if c.tier in want]
    if args.case:
        want_ids = {c.strip() for c in args.case.split(",") if c.strip()}
        cases = [c for c in cases if c.case_id in want_ids]

    if args.list:
        print(f"{'case':28} {'tier':>4}  {'external':22} description")
        for c in default_cases():
            print(f"{c.case_id:28} {c.tier:>4}  "
                  f"{','.join(c.needs_external) or '-':22} {c.description[:60]}")
        return 0

    drivers = (list(DRIVERS) if args.driver == "all"
               else [d.strip() for d in args.driver.split(",") if d.strip()])

    print("=" * 70)
    print("driver availability")
    print("=" * 70)
    for name, info in availability().items():
        mark = "OK " if info["available"] else "-- "
        print(f"  {mark}{name:14} {info['reason'] or ''}")

    if args.dry_run:
        print(f"\nwould run {len(cases)} case(s) x {len(drivers)} driver(s)")
        for c in cases:
            print(f"  {c.case_id:28} tier {c.tier}  "
                  f"needs {','.join(c.needs_external) or 'nothing'}")
        return 0

    out_root = OUT_ROOT / time.strftime("%Y%m%d-%H%M%S")
    rows: List[Dict[str, Any]] = []
    for d in drivers:
        for c in cases:
            rows.append(run_one(c, d, args.model, out_root))

    out_root.mkdir(parents=True, exist_ok=True)
    report = out_root / "report.json"
    ran = [r for r in rows if r.get("status") == "ran"]
    passed = [r for r in ran if (r.get("score") or {}).get("passed")]
    report.write_text(json.dumps({
        "availability": availability(),
        "n_cases": len(cases), "n_rows": len(rows),
        "n_ran": len(ran), "n_passed": len(passed),
        "rows": rows,
    }, indent=1), encoding="utf-8")

    print("\n" + "=" * 70)
    print(f"{len(passed)}/{len(ran)} scored cases passed "
          f"({len(rows) - len(ran)} could not run)")
    for r in rows:
        if r.get("status") != "ran":
            print(f"  --   {r['case_id']:28} {r['driver']:14} {r.get('reason','')[:44]}")
            continue
        cov = "" if r["required_tool_coverage"]["satisfied"] else "  [required tools MISSING]"
        sc = (r.get("score") or {})
        mark = "PASS" if sc.get("passed") else ("FAIL" if sc.get("scored") else "----")
        print(f"  {mark} {r['case_id']:28} {r['driver']:14} "
              f"{r['n_tool_calls']:>3} calls  {r['wall_seconds']:>6}s{cov}")
    print(f"\nwrote {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
