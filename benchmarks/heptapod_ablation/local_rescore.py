#!/usr/bin/env python3
"""Re-score the stored final models of one arm on this machine and compare
with the stored score: do the verdicts agree, and how much slower is the
compile here? The compile time limit changes scores, so it is measured, not
assumed.

    HEPVAL_COMPILE_TIMEOUT=3600 local_rescore.py --arm cc_sonnet_harness --out /tmp/rescore

Serial (hepval holds the one Wolfram kernel). Resumable: a paper with a
result in --out is skipped. Writes <out>/<paper>/call1/summary.json and
prints one JSON object: per paper the stored and local verdicts and seconds,
and the median time ratio.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import retro  # noqa: E402

HEPVAL = HERE.parent.parent / "pi_harness" / "hepval.py"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--arm", default="cc_sonnet_harness")
    ap.add_argument("--papers", default=",".join(retro.PAPERS))
    ap.add_argument(
        "--runs",
        default=os.environ.get(
            "PI_HARNESS_RUNS", str(Path.home() / "Documents/Github/heptapod/eval/benchmark_runs")
        ),
    )
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out)
    rows = []
    for paper in args.papers.split(","):
        d = Path(args.runs) / paper / "rerun" / args.arm / "s1"
        fr = d / "model" / f"{paper}_gen.fr"
        stored = retro._json(d / "validation_hepval.json")
        if not fr.is_file() or not stored:
            continue
        summ_file = out / paper / "call1" / "summary.json"
        if not summ_file.is_file():
            subprocess.run(
                [sys.executable, str(HEPVAL), "validate", str(fr), "--out", str(out / paper)],
                stdout=subprocess.DEVNULL,
                check=True,
            )
        local = json.loads(summ_file.read_text())
        s_old = retro.score_state(stored)
        s_new = retro.chain_state(
            local.get("compile_ok"), local.get("checks"), local.get("madgraph_import_ok")
        )
        rows.append(
            {
                "paper": paper,
                "stored": s_old,
                "local": s_new,
                "agree": s_old == s_new,
                "stored_pass": retro.is_pass(s_old),
                "local_pass": retro.is_pass(s_new),
                "stored_seconds": stored.get("seconds"),
                "local_seconds": local.get("seconds"),
                "local_timed_out": (local.get("row") or {}).get("timed_out"),
                "ratio": round(local["seconds"] / stored["seconds"], 2)
                if local.get("seconds") and stored.get("seconds")
                else None,
            }
        )
        print(
            f"{paper}: agree={rows[-1]['agree']} {stored.get('seconds')} s -> {local.get('seconds')} s",
            file=sys.stderr,
            flush=True,
        )
    ratios = [
        r["ratio"]
        for r in rows
        if r["ratio"] and r["stored"]["compile"] == "pass" and r["local"]["compile"] == "pass"
    ]
    print(
        json.dumps(
            {
                "arm": args.arm,
                "compile_timeout": os.environ.get("HEPVAL_COMPILE_TIMEOUT", "900"),
                "n": len(rows),
                "agree": sum(r["agree"] for r in rows),
                "stored_pass": sum(r["stored_pass"] for r in rows),
                "local_pass": sum(r["local_pass"] for r in rows),
                "median_time_ratio": round(statistics.median(ratios), 2) if ratios else None,
                "max_time_ratio": max(ratios) if ratios else None,
                "rows": rows,
            },
            indent=1,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
