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
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPERS = (
    "331,ALRM_general,B-L-SM,ChernSimonsPortal,EffLRSM,GeneralU1,HeavyN,MDMmodel,"
    "Monotops,NJLComposite,SLQrules,SMWeinberg,Top-Philic-Zprime,Wprime,pNG,pSPSS"
).split(",")
_spec = importlib.util.spec_from_file_location(
    "hepbench_checks", Path.home() / "code/hepbench-dev/benchmarks/model_building/_shared/checks.py"
)
HB = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(HB)


# Three faults of the reference labels, found by reading the references against the papers
# (results/gap_analysis.md). Each one made a correct delivered vertex count as wrong, in
# every group alike. The fixes change labels of the REFERENCE only.
REF_FIXES = {
    # monotops.fr:40,43 has `Indices->{Colour}` (no Index[]) for the two coloured scalars, so
    # the UFO gives them colour 1 while their vertices carry Epsilon(1,2,3). The paper: "i,j,k
    # are color indices in the fundamental representation". (The reader gives an antiparticle
    # the colour of its particle, as for the reference vector vc.)
    "Monotops": {"color": {"phic": 3, "tphic": 3, "phic__tilde__": 3, "tphic__tilde__": 3}},
    # The reference gives the SM-like Higgs the code 9900025, so it reads as a new scalar.
    "B-L-SM": {"pdg": {9900025: 25}},
    # 331.fr leaves beta a free symbol: the charges of the new states are expressions in beta
    # and read as None. The paper's four benchmarks are beta = +-1/sqrt3, +-sqrt3; a delivered
    # model is scored against the reference at the beta that fits it best.
    "331": {"beta": [1 / math.sqrt(3), -1 / math.sqrt(3), math.sqrt(3), -math.sqrt(3)]},
}
_CHARGE = re.compile(r"(q=)(-?\d+\.\d+)")


def _raw_charges(particles_py: Path) -> dict:
    """UFO variable -> the charge expression as written (for charges that are not numbers)."""
    text = particles_py.read_text(errors="replace")
    raw = {}
    for block in re.split(r"\n(?=\w+ = Particle\()", text):
        m, c = re.match(r"(\w+) = Particle\(", block), re.search(r"charge = (.*?),\n", block)
        if m and c:
            raw[m.group(1)] = c.group(1)
    for anti, part in re.findall(r"^(\w+) = (\w+)\.anti\(\)", text, re.M):
        if part in raw:
            raw[anti] = f"-({raw[part]})"
    return raw


def vertex_kinds(ufo: Path, fix: dict | None = None, beta: float | None = None) -> set | None:
    """The new-physics vertex kinds of a UFO; None when the UFO cannot be read."""
    parts = HB._ufo_particles(ufo / "particles.py")
    verts = HB._ufo_vertices(ufo / "vertices.py")
    if not parts or not verts:
        return None
    fix = fix or {}
    raw = _raw_charges(ufo / "particles.py") if beta is not None else {}
    ident = {}
    for n, p in parts.items():
        p = dict(p)
        if n in fix.get("color", {}):
            p["color"] = fix["color"][n]
        if abs(int(p.get("pdg_code") or 0)) in fix.get("pdg", {}):
            p["pdg_code"] = fix["pdg"][abs(int(p["pdg_code"]))]
        if p.get("charge") is None and n in raw:
            p["charge"] = eval(
                raw[n].replace("Sqrt[3]", "math.sqrt(3)").replace("beta", repr(beta)),
                {"math": math, "__builtins__": {}},
            )
        k = HB._identity(p)
        # one spelling for a charge: 2/3 from a rational and from sqrt arithmetic must agree
        ident[n] = (
            _CHARGE.sub(lambda m: m.group(1) + (f"{round(float(m.group(2)), 4):g}"), k) if k else k
        )
    kinds = set()
    for v in verts:
        ids = [ident.get(n) for n in v]
        if any(i is None for i in ids) or not any(i.startswith("bsm:") for i in ids):
            continue
        kinds.add(tuple(sorted(HB._generation_blind(i) for i in ids)))
    return kinds


def reference_kinds(paper: str, fixed: bool = True) -> list[set]:
    """The reference's kinds: one set, or one per allowed beta."""
    ufo = HERE / "ref_ufo" / paper / "UFO"
    fix = REF_FIXES.get(paper, {}) if fixed else {}
    sets = (
        [vertex_kinds(ufo, fix, b) for b in fix["beta"]]
        if "beta" in fix
        else [vertex_kinds(ufo, fix)]
    )
    return [s for s in sets if s is not None]


def f1(gen: set, ref: set) -> dict:
    tp = len(gen & ref)
    p = tp / len(gen) if gen else 0.0
    r = tp / len(ref) if ref else 0.0
    return {
        "precision": round(p, 3),
        "recall": round(r, 3),
        "f1": round(2 * p * r / (p + r), 3) if p + r else 0.0,
        "matched": tp,
        "generated": len(gen),
        "reference": len(ref),
    }


def score_run(rundir: Path, paper: str, ufo: Path | None = None, fixed: bool = True) -> dict:
    refs = reference_kinds(paper, fixed)
    v = (
        json.loads((rundir / "validation_hepval.json").read_text())
        if (rundir / "validation_hepval.json").is_file()
        else {}
    )
    chain = bool(v.get("full_chain_pass"))
    ufo = ufo or rundir / "score_ufo"
    gen = vertex_kinds(ufo) if (ufo / "vertices.py").is_file() else None
    out = {"paper": paper, "chain": chain, "has_ufo": gen is not None, "reference_ok": bool(refs)}
    if not refs:
        return {**out, "f1": None, "metric": None}
    ref = max(refs, key=lambda r: f1(gen or set(), r)["f1"])
    s = f1(gen or set(), ref)
    return {
        **out,
        **s,
        "metric": s["f1"] if chain else 0.0,
        "missing": sorted(" ".join(k) for k in ref - (gen or set()))[:12],
        "extra": sorted(" ".join(k) for k in (gen or set()) - ref)[:12],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument(
        "--group",
        action="append",
        required=True,
        metavar="NAME=ROOT:VARIANT[:UFOROOT]",
        help="UFOROOT/<paper>/call1/round0/UFO is used when the run has no score_ufo/",
    )
    ap.add_argument("--papers", default=",".join(PAPERS))
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument(
        "--raw-reference", action="store_true", help="score without REF_FIXES (the first metric)"
    )
    args = ap.parse_args()
    res = {}
    for g in args.group:
        name, rest = g.split("=", 1)
        root, variant, *ufo_root = rest.split(":")
        rows = []
        for p in args.papers.split(","):
            d = Path(root) / p / "rerun" / variant / f"s{args.seed}"
            alt = Path(ufo_root[0]) / p / "call1" / "round0" / "UFO" if ufo_root else None
            rows.append(
                score_run(
                    d,
                    p,
                    alt if alt and not (d / "score_ufo" / "vertices.py").is_file() else None,
                    fixed=not args.raw_reference,
                )
            )
        ok = [r for r in rows if r["metric"] is not None]
        res[name] = {
            "papers_scored": len(ok),
            "chain_pass": sum(r["chain"] for r in ok),
            "mean_metric": round(sum(r["metric"] for r in ok) / len(ok), 3) if ok else None,
            "mean_f1_any": round(sum(r["f1"] for r in ok) / len(ok), 3) if ok else None,
            "mean_recall_of_passes": round(
                sum(r["recall"] for r in ok if r["chain"]) / max(1, sum(r["chain"] for r in ok)), 3
            ),
            "rows": rows,
        }
    print(json.dumps(res, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
