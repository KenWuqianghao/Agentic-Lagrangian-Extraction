#!/usr/bin/env python3
"""Which named Lagrangian block does FeynRules fail on?

A compile failure in the scored chain names no block: the driver expands the
whole total and the log ends in a kernel message. This runs the pristine
driver once per named block of the total (ChecksOnly, no checks, no UFO): a
block is good when the driver reports its term count.

    compile_bisect.py MODEL.fr --out DIR

Serial in one hepval kernel slot. Prints one JSON object. This is the
prototype of the per-block localisation proposed for heptapod's
ValidateLagrangian.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "pi_harness"))
import hepval  # noqa: E402

_NOISE = re.compile(
    r"^(\[INFO\]|\[WARN\]|HEPTAPOD-| - FeynRules|Version:|Authors:|Please cite|\s+- |http"
    r"|The FeynRules palette|Merging model-files|This model implementation|Model Version"
    r"|For more information|Model .* loaded|From kernel|General::stop|heptapod extraction|\s*$)"
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("model")
    ap.add_argument("--out", required=True)
    ap.add_argument("--timeout", type=int, default=600)
    args = ap.parse_args()
    rb = hepval._load_validator()
    vb = rb.vb
    fr = Path(args.model).resolve()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    total, _info = vb.total_lag_symbol(fr)
    terms = {
        t["name"]: t["expression"]
        for t in vb.parse_lagrangian_terms(fr.read_text(errors="replace"))
    }
    blocks = (
        sorted(
            n
            for n in vb._reach(total, terms)
            if n in terms and n != total and not vb._is_pure_alias(n, terms)
        )
        if total
        else []
    )
    rows = []
    with hepval.kernel_slot():
        for b in blocks:
            log, rc, timed_out, dt = vb._run_driver(
                [
                    f"ModelPath={fr}",
                    f"OutputDir={out / 'unused_UFO'}",
                    "Checks=false",
                    "ChecksOnly=true",
                    "LoadSM=true",
                    f"Lagrangian={b}",
                ],
                args.timeout,
            )
            (out / f"{b}.log").write_text(log)
            m = re.search(r"HEPTAPOD-LAGRANGIAN\|.*\|terms=(\d+)", log)
            messages = []
            for ln in log.splitlines():
                s = ln.strip()[:240]
                if not _NOISE.match(ln) and s not in messages:
                    messages.append(s)
            rows.append(
                {
                    "block": b,
                    "ok": bool(m) and rc == 0 and not timed_out,
                    "terms": int(m.group(1)) if m else None,
                    "exit": rc,
                    "timed_out": timed_out,
                    "seconds": dt,
                    "messages": [] if m else messages[:6],
                }
            )
            print(
                f"{b}: {'ok' if rows[-1]['ok'] else 'FAILS'} {dt:.0f} s",
                file=sys.stderr,
                flush=True,
            )
    print(
        json.dumps(
            {
                "model": str(fr),
                "total": total,
                "blocks": len(blocks),
                "failing": [r["block"] for r in rows if not r["ok"]],
                "rows": rows,
            },
            indent=1,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
