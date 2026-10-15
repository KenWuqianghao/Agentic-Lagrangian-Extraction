#!/usr/bin/env python3
"""Numbers for the write-up: per-arm stage funnel, paired exact tests, and
whether the agent's own last in-loop verdict matches the independent score.

    summarize.py --variants v3s_notools,pi_qwen_plain,pi_qwen_harness,... > summary.json

Every verdict comes from validation_hepval.json (run_pi.py score), the same
scorer for every arm. A run with no delivered model counts as a failure at
every stage.
"""

from __future__ import annotations

import argparse
import json
from math import comb
from pathlib import Path

from run_pi import RUNS, SINGLE_MODEL

CHECKS = ("hermiticity", "kinetic_diagonal", "mass_diagonal", "mass_spectrum")


def stages(page: str, variant: str) -> dict:
    d = RUNS / page / "rerun" / variant / "s1"
    v = (
        json.loads((d / "validation_hepval.json").read_text())
        if (d / "validation_hepval.json").is_file()
        else {}
    )
    c = v.get("checks") or {}
    run = json.loads((d / "run.json").read_text()) if (d / "run.json").is_file() else {}
    a = run.get("agent") or {}
    return {
        "delivered": bool(v),
        "compiled": bool(v.get("compile_ok")),
        "hermiticity": c.get("hermiticity") == "pass",
        "mass_diagonal": c.get("mass_diagonal") == "pass",
        "all_checks": all(c.get(k) == "pass" for k in CHECKS),
        "madgraph": bool(v.get("madgraph_import_ok")),
        "full_chain": bool(v.get("full_chain_pass")),
        "status": v.get("status") or ("no model" if run else "not run"),
        "checks": c,
        "seconds": a.get("seconds"),
        "tool_counts": a.get("tool_counts"),
        "agent_errors": a.get("errors"),
        "agent_last_verdict": _last_inloop(d),
    }


def _last_inloop(d: Path) -> str | None:
    """The stage of the agent's last validate_model call (harness arms)."""
    calls = (
        sorted((d / "validation").glob("call*/summary.json"), key=lambda p: int(p.parent.name[4:]))
        if (d / "validation").is_dir()
        else []
    )
    return json.loads(calls[-1].read_text()).get("stage") if calls else None


def mcnemar_exact(a: list[bool], b: list[bool]) -> dict:
    """Two-sided exact McNemar on paired outcomes (same papers)."""
    b_only = sum(1 for x, y in zip(a, b) if y and not x)
    a_only = sum(1 for x, y in zip(a, b) if x and not y)
    n = a_only + b_only
    k = min(a_only, b_only)
    p = min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2**n) if n else 1.0
    return {"only_first": a_only, "only_second": b_only, "p": round(p, 4)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variants", required=True)
    args = ap.parse_args()
    pages = SINGLE_MODEL.split(",")
    variants = args.variants.split(",")
    table = {v: {p: stages(p, v) for p in pages} for v in variants}
    keys = (
        "delivered",
        "compiled",
        "hermiticity",
        "mass_diagonal",
        "all_checks",
        "madgraph",
        "full_chain",
    )
    funnel = {v: {k: sum(table[v][p][k] for p in pages) for k in keys} for v in variants}
    tests = {}
    for i, v1 in enumerate(variants):
        for v2 in variants[i + 1 :]:
            tests[f"{v1} vs {v2}"] = {
                k: mcnemar_exact([table[v1][p][k] for p in pages], [table[v2][p][k] for p in pages])
                for k in ("compiled", "mass_diagonal", "all_checks", "full_chain")
            }
    agree = {}
    for v in variants:
        rows = [table[v][p] for p in pages if table[v][p]["agent_last_verdict"]]
        if rows:
            agree[v] = {
                "with_inloop_validation": len(rows),
                "agent_last_pass": sum(r["agent_last_verdict"] == "pass" for r in rows),
                "agent_pass_and_scored_pass": sum(
                    r["agent_last_verdict"] == "pass" and r["full_chain"] for r in rows
                ),
                "agent_pass_scored_fail": [
                    p
                    for p in pages
                    if table[v][p]["agent_last_verdict"] == "pass" and not table[v][p]["full_chain"]
                ],
            }
    print(
        json.dumps(
            {
                "pages": pages,
                "funnel": funnel,
                "tests": tests,
                "inloop_vs_score": agree,
                "table": table,
            },
            indent=1,
            default=str,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
