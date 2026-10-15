#!/usr/bin/env python3
"""Score a delivered model with its own LTotal as the whole Lagrangian.

The common scorer adds LSM when the total does not name LSM, and it refuses a
file with two unused top-level L terms. The harness arms are told both rules;
the vanilla task (run_vanilla.TASK) was not. A vanilla model that writes the
whole Lagrangian from SM.fr's pieces (LGauge + LFermions + ...) is then
scored with the Standard Model counted twice. This scores `LTotal` exactly as
written, into validation_intent.json; validation_hepval.json is not touched.

    intent_score.py --variant cc_vanilla --pages B-L-SM,MDMmodel
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "pi_harness"))
import hepval  # noqa: E402
import run_pi  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--variant", default="cc_vanilla")
    ap.add_argument("--pages", required=True)
    args = ap.parse_args()
    rb = hepval._load_validator()
    rb.vb.total_lag_symbol = lambda fr: ("LTotal", {"forced": True})
    rb.vb.lagrangian_expression = lambda fr, lag: "LTotal"
    for page in args.pages.split(","):
        d = run_pi.RUNS / page / "rerun" / args.variant / "s1"
        fr = d / "model" / f"{page}_gen.fr"
        if not fr.is_file() or (d / "validation_intent.json").is_file():
            continue
        rb.OUTROOT = Path(tempfile.mkdtemp(prefix=f"intent-{page}-"))
        with hepval.kernel_slot():
            row = rb.validate("call1", fr, 0)
        v = {
            "status": row.get("status"),
            "compile_ok": row.get("compile_ok"),
            "timed_out": row.get("timed_out"),
            "seconds": row.get("seconds"),
            "checks": row.get("checks"),
            "madgraph_import_ok": row.get("madgraph_import_ok"),
            "full_chain_pass": bool(row.get("full_pass")),
            "lagrangian_expression": "LTotal",
            "scorer": "intent_score.py: the common chain on LTotal as written, no LSM added",
            "scored_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        (d / "validation_intent.json").write_text(json.dumps(v, indent=1, default=str))
        ufo = rb.OUTROOT / "call1" / "round0" / "UFO"
        for name in ("particles.py", "vertices.py"):
            if (ufo / name).is_file():
                (d / "intent_ufo").mkdir(exist_ok=True)
                (d / "intent_ufo" / name).write_bytes((ufo / name).read_bytes())
        print(
            f"{page}: {v['status']} full_chain={v['full_chain_pass']} checks={v['checks']} "
            f"mg5={v['madgraph_import_ok']}",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
