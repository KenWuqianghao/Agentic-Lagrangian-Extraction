#!/usr/bin/env python3
"""Referee a delivered model that no in-loop review saw.

The referee is review_model's own code path (same prompt, same model, its
own sandbox with the paper, SM.fr and a frozen copy of the model), run after
the agent stopped, into <rundir>/post_review/. Used for full-chain passes
whose final model.fr changed after the agent's last review_model call.

    post_review.py --variant cc_sonnet_harness --pages MDMmodel
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "pi_harness"))
from run_pi import RUNS  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="cc_sonnet_harness")
    ap.add_argument("--pages", required=True)
    ap.add_argument("--model", default="claude-sonnet-5")
    args = ap.parse_args()
    for page in args.pages.split(","):
        d = RUNS / page / "rerun" / args.variant / "s1"
        sb = Path((d / "sandbox_path.txt").read_text().strip())
        final = d / "model" / f"{page}_gen.fr"
        if (sb / "model.fr").read_bytes() != final.read_bytes():
            raise SystemExit(f"{page}: sandbox model.fr differs from the delivered model")
        os.environ.update({"CC_SANDBOX": str(sb), "CC_RUNDIR": str(d / "post_review"),
                           "CC_REVIEW_BUDGET": "1", "CC_REVIEW_MODEL": args.model})
        import common  # noqa: E402  (reads the environment at call time)
        import heptapod_mcp  # noqa: E402
        out = heptapod_mcp.review_model({"path": "model.fr"})
        verdict = next((ln.strip() for ln in reversed(out.splitlines()) if ln.strip().upper().startswith("VERDICT:")), None)
        (d / "post_review" / "verdict.json").write_text(json.dumps(
            {"page": page, "verdict": verdict, "post_hoc": True,
             "model_sha": common.sha(final)}, indent=1))
        print(f"{page}: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
