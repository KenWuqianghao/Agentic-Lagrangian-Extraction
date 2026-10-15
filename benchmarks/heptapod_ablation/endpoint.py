#!/usr/bin/env python3
"""The pre-specified endpoint and tests of the heptapod ablation.

Primary endpoint of one run (one paper, one arm, one seed): all three of
  1. the scored file passes the full chain (validation_hepval.json: compile,
     four checks, MadGraph import; the pristine heptapod-dev driver);
  2. the referee, run after the agent stopped on the scored file
     (cc_harness/post_review.py, the same referee for every arm), reports no
     physics-changing discrepancy;
  3. every new particle is in at least one vertex of the scored UFO
     (score_ufo/, kept by `run_cc.py score`).
A run without a delivered model fails. A chain pass without a referee verdict
is reported as missing, not as a pass.

Tests: arms are compared on the same papers with the same number of seeds.
The test is exact and stratified by paper: under the null, the arm labels of
a paper's runs are exchangeable, so the passes of arm A in a paper follow a
hypergeometric law; the statistic is the total over papers. It answers "is A
better than B on these papers"; it does not generalise to other papers.

End to end, a unit is a paper:

    endpoint.py --arms compile,heptapod,full --variant 'cc_abl_{arm}' --seeds 3 \\
                --units B-L-SM,ChernSimonsPortal,...

Repair, a unit is source:paper:

    endpoint.py --arms import,heptapod,diag --variant 'cc_rep_{arm}_from_{source}' --seeds 2 \\
                --units cc_sonnet_harness:B-L-SM,v3s_notools:HeavyN,...

The contrasts are tested in a fixed order (a later one is confirmatory only
if every earlier one is significant at 0.05). Repair design: diag vs import,
heptapod vs import, diag vs heptapod. End to end: heptapod vs compile, full
vs compile, compile vs none, full vs heptapod.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "cc_harness"))
import common  # noqa: E402
import retro  # noqa: E402

CONTRASTS = (
    ("diag", "import"),
    ("heptapod", "import"),
    ("diag", "heptapod"),
    ("heptapod", "compile"),
    ("full", "compile"),
    ("compile", "none"),
    ("full", "heptapod"),
)


def run_outcome(d: Path, paper: str) -> dict:
    fr = d / "model" / f"{paper}_gen.fr"
    score = retro._json(d / "validation_hepval.json")
    state = retro.score_state(score)
    chain = bool(state and retro.is_pass(state))
    post = retro._json(d / "post_review" / "verdict.json") or {}
    reviewed = bool(post) and post.get("model_sha") == common.sha(fr)
    changing = retro.physics_changing(post.get("verdict")) if reviewed else None
    ufo = d / "score_ufo"
    inert = retro.particles_without_vertex(ufo) if (ufo / "vertices.py").is_file() else None
    missing = [
        what
        for what, absent in (
            ("score", fr.is_file() and score is None),
            ("referee", chain and changing is None),
            ("score_ufo", chain and inert is None),
        )
        if absent
    ]
    return {
        "paper": paper,
        "ran": (d / "run.json").is_file(),
        "delivered": fr.is_file(),
        "chain": chain,
        "stage": retro.stage_of(state) if state else "no_model",
        "physics_changing": changing,
        "particles_without_vertex": inert,
        "missing": missing,
        "endpoint": chain and changing == 0 and inert == [],
    }


def exact_stratified(strata: list[tuple[int, int, int, int]]) -> dict:
    """Two-sided exact test of "arm A passes more often than arm B", stratified.

    Each stratum is (passes_a, runs_a, passes_b, runs_b) for one paper. Given a
    paper's total passes, the passes of A are hypergeometric under the null;
    the null law of the total is their convolution. The p-value is the null
    probability of a total at least as far from its mean as the observed one.
    """
    dist = {0: 1.0}
    observed, mean = 0, 0.0
    for a, na, b, nb in strata:
        k, n = a + b, na + nb
        observed += a
        mean += k * na / n
        pmf = {
            x: comb(k, x) * comb(n - k, na - x) / comb(n, na)
            for x in range(max(0, k - nb), min(k, na) + 1)
        }
        dist = _convolve(dist, pmf)
    gap = abs(observed - mean) - 1e-9
    return {
        "passes_a": observed,
        "passes_b": sum(s[2] for s in strata),
        "expected_a_under_null": round(mean, 3),
        "p": min(1.0, sum(p for t, p in dist.items() if abs(t - mean) >= gap)),
    }


def _convolve(d1: dict, d2: dict) -> dict:
    out: dict = {}
    for x, p in d1.items():
        for y, q in d2.items():
            out[x + y] = out.get(x + y, 0.0) + p * q
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--arms", required=True, help="comma-separated arm names")
    ap.add_argument(
        "--variant",
        required=True,
        help="variant name with {arm}, and {source} for the repair design",
    )
    ap.add_argument(
        "--units",
        required=True,
        help="comma-separated papers, or source:paper for the repair design",
    )
    ap.add_argument("--seeds", type=int, required=True)
    ap.add_argument(
        "--runs",
        default=os.environ.get(
            "PI_HARNESS_RUNS", str(Path.home() / "Documents/Github/heptapod/eval/benchmark_runs")
        ),
    )
    args = ap.parse_args()
    arms = args.arms.split(",")
    units = args.units.split(",")

    def outcomes(arm: str, unit: str) -> list[dict]:
        source, _, paper = unit.rpartition(":")
        variant = args.variant.format(arm=arm, source=source)
        return [
            run_outcome(Path(args.runs) / paper / "rerun" / variant / f"s{k}", paper)
            for k in range(1, args.seeds + 1)
        ]

    rows = {arm: {u: outcomes(arm, u) for u in units} for arm in arms}
    res = {"units": units, "seeds": args.seeds, "arms": {}, "contrasts": [], "incomplete": []}
    for arm, per in rows.items():
        flat = [(u, r) for u, rs in per.items() for r in rs]
        res["incomplete"] += [
            f"{arm}/{u}: {'not run' if not r['ran'] else ', '.join(r['missing'])}"
            for u, r in flat
            if not r["ran"] or r["missing"]
        ]
        res["arms"][arm] = {
            "runs": len(flat),
            "delivered": sum(r["delivered"] for _u, r in flat),
            "chain_pass": sum(r["chain"] for _u, r in flat),
            "endpoint": sum(r["endpoint"] for _u, r in flat),
            "per_unit_endpoint": {u: sum(r["endpoint"] for r in rs) for u, rs in per.items()},
            "per_unit_chain": {u: sum(r["chain"] for r in rs) for u, rs in per.items()},
        }
    for a, b in CONTRASTS:
        if a in rows and b in rows:
            for key in ("endpoint", "chain"):
                strata = [
                    (
                        sum(r[key] for r in rows[a][u]),
                        args.seeds,
                        sum(r[key] for r in rows[b][u]),
                        args.seeds,
                    )
                    for u in units
                ]
                res["contrasts"].append(
                    {
                        "a": a,
                        "b": b,
                        "outcome": "primary endpoint" if key == "endpoint" else "full chain",
                        **exact_stratified(strata),
                    }
                )
    print(json.dumps(res, indent=1))
    return 1 if res["incomplete"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
