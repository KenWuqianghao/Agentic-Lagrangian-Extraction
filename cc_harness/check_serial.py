#!/usr/bin/env python3
"""Evidence that Wolfram validation stayed serial while papers ran in
parallel: every hepval call summary records the interval it held the kernel
(t_kernel_start, t_kernel_end). No two intervals may overlap.

    check_serial.py [--variant cc_sonnet_harness] [extra summary dirs ...]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pi_harness"))
from run_pi import RUNS  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="cc_sonnet_harness")
    ap.add_argument("extra", nargs="*")
    args = ap.parse_args()
    files = list(RUNS.glob(f"*/rerun/{args.variant}/s*/validation/call*/summary.json"))
    for e in args.extra:
        files += list(Path(e).glob("**/summary.json"))
    iv = []
    for f in files:
        s = json.loads(f.read_text())
        if s.get("t_kernel_start") and s.get("t_kernel_end"):
            iv.append(
                (s["t_kernel_start"], s["t_kernel_end"], str(f), s.get("lock_wait_seconds") or 0)
            )
    iv.sort()
    overlaps = [(a[2], b[2], round(a[1] - b[0], 1)) for a, b in zip(iv, iv[1:]) if b[0] < a[1]]
    waited = [x for x in iv if x[3] > 0]
    print(
        json.dumps(
            {
                "intervals": len(iv),
                "overlaps": overlaps,
                "calls_that_waited_for_the_lock_or_a_kernel": len(waited),
                "max_wait_seconds": max((x[3] for x in iv), default=0),
                "kernel_hours": round(sum(b - a for a, b, _f, _w in iv) / 3600, 2),
                "span_hours": round((iv[-1][1] - iv[0][0]) / 3600, 2) if iv else 0,
            },
            indent=1,
        )
    )
    return 1 if overlaps else 0


if __name__ == "__main__":
    raise SystemExit(main())
