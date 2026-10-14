#!/usr/bin/env python3
"""The harness's referee on the vanilla baseline's chain passes: the same
prompt and model as post_review.py, on a staged copy (paper, SM.fr, model).

    vanilla_review.py --variant cc_vanilla
    vanilla_review.py --variant cc_sonnet_harness --source STORED_RUNS --pages A,B   # verdicts go to the
                                                   # writable runs tree; the stored tree is not touched

A fresh referee run is the only verdict that is the same kind in every group:
an in-loop review is the verdict the agent worked against.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "cc_harness"))
sys.path.insert(0, str(HERE.parent.parent / "pi_harness"))
import run_pi  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--variant", default="cc_vanilla")
    ap.add_argument("--model", default="claude-sonnet-5")
    ap.add_argument(
        "--source", default="", help="runs tree that holds the models (default: PI_HARNESS_RUNS)"
    )
    ap.add_argument("--pages", default=run_pi.SINGLE_MODEL)
    args = ap.parse_args()
    for page in args.pages.split(","):
        src = (
            (Path(args.source) if args.source else run_pi.RUNS)
            / page
            / "rerun"
            / args.variant
            / "s1"
        )
        d = run_pi.RUNS / page / "rerun" / args.variant / "s1"
        score = (
            json.loads((src / "validation_hepval.json").read_text())
            if (src / "validation_hepval.json").is_file()
            else {}
        )
        if not score.get("full_chain_pass") or (d / "post_review" / "verdict.json").is_file():
            continue
        sb = Path(tempfile.mkdtemp(prefix="vanilla-referee-"))
        paper = run_pi.paper_file(page)
        (sb / "eval" / "benchmark_runs" / page / "text").mkdir(parents=True)
        shutil.copy2(paper, sb / "eval" / "benchmark_runs" / page / "text" / paper.name)
        shutil.copy2(run_pi.SM_FR, sb / "SM.fr")
        shutil.copy2(src / "model" / f"{page}_gen.fr", sb / "model.fr")
        os.environ.update(
            {
                "CC_SANDBOX": str(sb),
                "CC_RUNDIR": str(d / "post_review"),
                "CC_REVIEW_BUDGET": "1",
                "CC_REVIEW_MODEL": args.model,
            }
        )
        import common  # noqa: E402
        import heptapod_mcp  # noqa: E402

        out = heptapod_mcp.review_model({"path": "model.fr"})
        verdict = next(
            (
                x.strip()
                for x in reversed(out.splitlines())
                if x.strip().upper().startswith("VERDICT:")
            ),
            None,
        )
        (d / "post_review" / "verdict.json").write_text(
            json.dumps(
                {
                    "page": page,
                    "verdict": verdict,
                    "post_hoc": True,
                    "model_sha": common.sha(src / "model" / f"{page}_gen.fr"),
                },
                indent=1,
            )
        )
        print(f"{page}: {verdict}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
