#!/usr/bin/env python3
"""The hill-climb metric: how much of the reference model's new physics is in
a delivered model's UFO, and is the model usable.

Ground truth is the model file of each paper from the FeynRules model
database, compiled to a UFO (ref_ufo/<paper>/UFO). A vertex is reduced to the
sorted list of what its particles ARE, not what they are called: Standard
Model particles by PDG code with the generation dropped, new particles by
(spin, charge, colour). Ghosts and Goldstones are left out. hepbench's grader
does the same reduction; its functions are used here unchanged.

    vertex F1   between the set of new-physics vertex kinds (a vertex with at
                least one new particle) of the reference and of the model
    metric      vertex F1 when the scored chain passes, else 0

The metric is 0 for a model that passes by leaving physics out of reach of
the chain (low recall) and for one that keeps the physics and does not pass.
New states with the same spin, charge and colour are one kind: the reference
and the paper do not always have the same number of copies (HeavyN).

    ref_score.py --group name=RUNS_ROOT:VARIANT ... [--papers A,B]   # JSON to stdout
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPERS = ("331,ALRM_general,B-L-SM,ChernSimonsPortal,EffLRSM,GeneralU1,HeavyN,MDMmodel,"
          "Monotops,NJLComposite,SLQrules,SMWeinberg,Top-Philic-Zprime,Wprime,pNG,pSPSS").split(",")
_spec = importlib.util.spec_from_file_location(
    "hepbench_checks", Path.home() / "code/hepbench-dev/benchmarks/model_building/_shared/checks.py")
HB = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(HB)


def vertex_kinds(ufo: Path) -> set | None:
    """The new-physics vertex kinds of a UFO; None when the UFO cannot be read."""
    parts = HB._ufo_particles(ufo / "particles.py")
    verts = HB._ufo_vertices(ufo / "vertices.py")
    if not parts or not verts:
        return None
    ident = {n: HB._identity(p) for n, p in parts.items()}
    kinds = set()
    for v in verts:
        ids = [ident.get(n) for n in v]
        if any(i is None for i in ids) or not any(i.startswith("bsm:") for i in ids):
            continue
        kinds.add(tuple(sorted(HB._generation_blind(i) for i in ids)))
    return kinds


def f1(gen: set, ref: set) -> dict:
    tp = len(gen & ref)
    p = tp / len(gen) if gen else 0.0
    r = tp / len(ref) if ref else 0.0
    return {"precision": round(p, 3), "recall": round(r, 3), "f1": round(2 * p * r / (p + r), 3) if p + r else 0.0,
            "matched": tp, "generated": len(gen), "reference": len(ref)}


def score_run(rundir: Path, paper: str, ufo: Path | None = None) -> dict:
    ref = vertex_kinds(HERE / "ref_ufo" / paper / "UFO")
    v = json.loads((rundir / "validation_hepval.json").read_text()) if (rundir / "validation_hepval.json").is_file() else {}
    chain = bool(v.get("full_chain_pass"))
    ufo = ufo or rundir / "score_ufo"
    gen = vertex_kinds(ufo) if (ufo / "vertices.py").is_file() else None
    out = {"paper": paper, "chain": chain, "has_ufo": gen is not None, "reference_ok": ref is not None}
    if ref is None:
        return {**out, "f1": None, "metric": None}
    s = f1(gen or set(), ref)
    return {**out, **s, "metric": s["f1"] if chain else 0.0,
            "missing": sorted(" ".join(k) for k in ref - (gen or set()))[:12],
            "extra": sorted(" ".join(k) for k in (gen or set()) - ref)[:12]}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--group", action="append", required=True, metavar="NAME=ROOT:VARIANT[:UFOROOT]",
                    help="UFOROOT/<paper>/call1/round0/UFO is used when the run has no score_ufo/")
    ap.add_argument("--papers", default=",".join(PAPERS))
    args = ap.parse_args()
    res = {}
    for g in args.group:
        name, rest = g.split("=", 1)
        root, variant, *ufo_root = rest.split(":")
        rows = []
        for p in args.papers.split(","):
            d = Path(root) / p / "rerun" / variant / "s1"
            alt = Path(ufo_root[0]) / p / "call1" / "round0" / "UFO" if ufo_root else None
            rows.append(score_run(d, p, alt if alt and not (d / "score_ufo" / "vertices.py").is_file() else None))
        ok = [r for r in rows if r["metric"] is not None]
        res[name] = {"papers_scored": len(ok), "chain_pass": sum(r["chain"] for r in ok),
                     "mean_metric": round(sum(r["metric"] for r in ok) / len(ok), 3) if ok else None,
                     "mean_f1_any": round(sum(r["f1"] for r in ok) / len(ok), 3) if ok else None,
                     "mean_recall_of_passes": round(sum(r["recall"] for r in ok if r["chain"]) / max(1, sum(r["chain"] for r in ok)), 3),
                     "rows": rows}
    print(json.dumps(res, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
