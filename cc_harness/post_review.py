#!/usr/bin/env python3
"""Referee a delivered model that no in-loop review saw.

The referee is review_model's own code path (same prompt, same model, its
own sandbox with the paper, SM.fr and a frozen copy of the model), run after
the agent stopped, into <rundir>/post_review/. Used for full-chain passes
whose final model.fr changed after the agent's last review_model call.

    post_review.py --variant cc_sonnet_harness --pages MDMmodel
    post_review.py --variant cc_abl_compile --pages all --seeds 3 --chain-pass-only

The ablation's endpoint needs this verdict for every chain pass of every arm,
from the same referee, whether or not the arm had review_model in its loop.
The sandbox of the run must still exist (it is a temp directory).
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
import common as C  # noqa: E402
import heptapod_mcp  # noqa: E402
from run_pi import RUNS, SINGLE_MODEL  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="cc_sonnet_harness")
    ap.add_argument("--pages", required=True)
    ap.add_argument("--model", default="claude-sonnet-5")
    ap.add_argument("--seeds", type=int, default=1)
    ap.add_argument(
        "--chain-pass-only",
        action="store_true",
        help="skip runs whose scored file does not pass the full chain, and runs already refereed",
    )
    args = ap.parse_args()
    pages = (SINGLE_MODEL if args.pages == "all" else args.pages).split(",")
    for page, k in ((p, k) for p in pages for k in range(1, args.seeds + 1)):
        d = RUNS / page / "rerun" / args.variant / f"s{k}"
        final = d / "model" / f"{page}_gen.fr"
        if args.chain_pass_only:
            score = (
                json.loads((d / "validation_hepval.json").read_text())
                if (d / "validation_hepval.json").is_file()
                else {}
            )
            if not score.get("full_chain_pass") or (d / "post_review" / "verdict.json").is_file():
                continue
        sb = Path((d / "sandbox_path.txt").read_text().strip())
        if (sb / "model.fr").read_bytes() != final.read_bytes():
            raise SystemExit(f"{page} s{k}: sandbox model.fr differs from the delivered model")
        os.environ.update(
            {
                "CC_SANDBOX": str(sb),
                "CC_RUNDIR": str(d / "post_review"),
                "CC_REVIEW_BUDGET": "1",
                "CC_REVIEW_MODEL": args.model,
            }
        )
        # review_model reads these from the environment at call time.
        verdict = C.verdict_line(heptapod_mcp.review_model({"path": "model.fr"}))
        (d / "post_review" / "verdict.json").write_text(
            json.dumps(
                {
                    "page": page,
                    "verdict": verdict,
                    "post_hoc": True,
                    "model_sha": C.sha(final),
                },
                indent=1,
            )
        )
        print(f"{page} s{k}: {verdict}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
