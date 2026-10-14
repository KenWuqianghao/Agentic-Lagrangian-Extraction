#!/usr/bin/env python3
"""How many seeds does the ablation need? A simulation of endpoint.py's test.

The stored runs give one seed, so the per-paper pass probabilities are
assumptions, derived from retro.json by rule and then varied:

  every arm     a paper that reached the primary endpoint at its first
                validate call in the stored harness run is a predicted pass:
                the loop was not needed.
  none, compile the other papers are predicted fails. All of them compiled at
                their first call, so a compile-only tool and its gate are
                satisfied with a file that fails a check or the import.
  heptapod      a paper that reached the endpoint later is a predicted pass
                when every fix on its way came with information heptapod-dev
                main also returns (verdict, compile log, MadGraph message),
                and uncertain when a fix came with an ALE-only report section
                or lint rule.
  full          every paper that reached the endpoint in the stored run is a
                predicted pass.

A predicted pass passes with probability r, a predicted fail with f, an
uncertain paper with (r + f) / 2. Papers that never passed the chain in any
stored arm are not run and count as fails in every arm.

The repair design asks a narrower question with more units. Every stored
first draft that compiles and fails at least one FeynRules check is a unit;
each arm starts from the same draft (`run_cc.py --draft-from`) and differs
only in the feedback. A generic loop (compile + MadGraph import) cannot see
the failing check, so its repair rate g is low; h is the rate with the check
verdicts, d with the located reports as well. All three are assumptions.

    power.py            # prints the tables as JSON; --md for the markdown tables
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from endpoint import exact_stratified  # noqa: E402

CONTRASTS = (
    ("heptapod", "compile"),
    ("full", "compile"),
    ("compile", "none"),
    ("full", "heptapod"),
)

UPSTREAM_SOURCES = {"verdict_only", "compile_log", "mg5_message"}
SCENARIOS = {"optimistic": (0.9, 0.05), "central": (0.75, 0.10), "pessimistic": (0.6, 0.15)}
SEEDS = (1, 2, 3, 4, 5, 6)


def predictions(retro_json: dict) -> dict:
    """paper -> arm -> "pass" | "fail" | "uncertain", for the papers to run
    (the stored harness chain passes)."""
    runs = retro_json["arms"]["cc_sonnet_harness"]["runs"]
    out = {}
    for r in runs:
        if not r["score_pass"]:
            continue
        endpoint = r["physics_changing"] == 0 and r["particles_without_vertex"] == []
        first = bool(r["calls"]) and r["calls"][0]["pass"]
        fixes = [t for t in r["transitions"] if t["change"] == "fixed"]
        upstream_only = all(set(t["sources"]) <= UPSTREAM_SOURCES for t in fixes)
        if not endpoint:
            pred = dict.fromkeys(("none", "compile", "heptapod", "full"), "fail")
        elif first:
            pred = dict.fromkeys(("none", "compile", "heptapod", "full"), "pass")
        else:
            pred = {
                "none": "fail",
                "compile": "fail",
                "heptapod": "pass" if upstream_only else "uncertain",
                "full": "pass",
            }
        out[r["paper"]] = pred
    return out


GENERIC = "compile + MadGraph import"
REPAIR_RATES = {
    "h 0.30, g 0.10": (0.30, 0.10),
    "h 0.45, g 0.10": (0.45, 0.10),
    "h 0.60, g 0.10": (0.60, 0.10),
    "h 0.45, g 0.20": (0.45, 0.20),
    "d 0.60, h 0.45": (0.60, 0.45),
    "d 0.65, h 0.35": (0.65, 0.35),
}


def repair_units(retro_json: dict) -> list[str]:
    """arm:paper of every stored first draft with a failing check that a
    compile + import loop does not report."""
    return sorted(
        f"{arm}:{p}"
        for arm, a in retro_json["arms"].items()
        for p in a["first_draft_visibility"][GENERIC]["blind_to"]
        + a["first_draft_visibility"][GENERIC]["partly_blind_to"]
    )


def repair_power(
    units: int, pa: float, pb: float, seeds: int, n_sim: int, rng: random.Random
) -> float:
    hits = 0
    for _ in range(n_sim):
        strata = [
            (
                sum(rng.random() < pa for _ in range(seeds)),
                seeds,
                sum(rng.random() < pb for _ in range(seeds)),
                seeds,
            )
            for _ in range(units)
        ]
        t = exact_stratified(strata)
        hits += t["p"] < 0.05 and t["passes_a"] > t["passes_b"]
    return hits / n_sim


def probability(pred: str, r: float, f: float) -> float:
    return {"pass": r, "fail": f, "uncertain": (r + f) / 2}[pred]


def power(
    pred: dict, r: float, f: float, seeds: int, a: str, b: str, n_sim: int, rng: random.Random
) -> float:
    hits = 0
    for _ in range(n_sim):
        strata = []
        for arms in pred.values():
            pa, pb = probability(arms[a], r, f), probability(arms[b], r, f)
            strata.append(
                (
                    sum(rng.random() < pa for _ in range(seeds)),
                    seeds,
                    sum(rng.random() < pb for _ in range(seeds)),
                    seeds,
                )
            )
        t = exact_stratified(strata)
        hits += t["p"] < 0.05 and t["passes_a"] > t["passes_b"]
    return hits / n_sim


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--retro", default=str(HERE / "retro.json"))
    ap.add_argument("--sims", type=int, default=4000)
    ap.add_argument("--md", action="store_true")
    args = ap.parse_args()
    retro_json = json.loads(Path(args.retro).read_text())
    pred = predictions(retro_json)
    rng = random.Random(20261006)
    expected = {
        name: {
            arm: round(sum(probability(p[arm], r, f) for p in pred.values()), 2)
            for arm in ("none", "compile", "heptapod", "full")
        }
        for name, (r, f) in SCENARIOS.items()
    }
    table = [
        {
            "contrast": f"{a} vs {b}",
            "scenario": name,
            "seeds": s,
            "power": round(power(pred, r, f, s, a, b, args.sims, rng), 3),
        }
        for a, b in CONTRASTS
        for name, (r, f) in SCENARIOS.items()
        for s in SEEDS
    ]
    units = repair_units(retro_json)
    repair = [
        {
            "rates": name,
            "seeds": s,
            "power": round(repair_power(len(units), a, b, s, args.sims, rng), 3),
        }
        for name, (a, b) in REPAIR_RATES.items()
        for s in (1, 2, 3)
    ]
    res = {
        "end_to_end": {
            "papers": len(pred),
            "predictions": pred,
            "scenarios": SCENARIOS,
            "expected_endpoint_passes_per_seed": expected,
            "power": table,
        },
        "repair": {"units": units, "rates": REPAIR_RATES, "power": repair},
        "sims": args.sims,
    }
    if not args.md:
        print(json.dumps(res, indent=1))
        return 0
    print(f"Repair design, {len(units)} drafts (first rate against second rate):\n")
    print("| assumed repair rates | 1 seed | 2 seeds | 3 seeds |\n|---|---|---|---|")
    for name in REPAIR_RATES:
        print(
            f"| {name} | "
            + " | ".join(f"{x['power']:.2f}" for x in repair if x["rates"] == name)
            + " |"
        )
    print(f"\nEnd-to-end design, {len(pred)} papers:\n")
    print(
        "| contrast | scenario (r, f) | "
        + " | ".join(f"{s} seed{'s' if s > 1 else ''}" for s in SEEDS)
        + " |"
    )
    print("|---|---|" + "---|" * len(SEEDS))
    for a, b in CONTRASTS:
        for name, (r, f) in SCENARIOS.items():
            cells = [
                next(
                    x["power"]
                    for x in table
                    if x["contrast"] == f"{a} vs {b}" and x["scenario"] == name and x["seeds"] == s
                )
                for s in SEEDS
            ]
            print(
                f"| {a} vs {b} | {name} ({r}, {f}) | "
                + " | ".join(f"{c:.2f}" for c in cells)
                + " |"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
