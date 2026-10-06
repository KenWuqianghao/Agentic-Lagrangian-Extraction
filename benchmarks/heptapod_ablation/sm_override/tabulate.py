#!/usr/bin/env python3
"""Run the SM-override test models through the scored chain and tabulate what
reached the UFO.

    tabulate.py --out DIR [--run]     # --run validates each .fr first (serial, about 2 minutes each)

Each model adds one free real scalar H2 to SM.fr and tries one way to put it
into the Higgs doublet, Phi[2] -> (vev + ca H - sa H2 + I G0)/Sqrt[2]. The
override reached the Standard Model's Yukawa term when the UFO has an
H2 t t~ vertex.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HEPVAL = HERE.parents[2] / "pi_harness" / "hepval.py"
VERTEX = re.compile(r"V_\d+ = Vertex\(name = '(V_\d+)',\s*particles = \[([^\]]*)\],.*?couplings = \{([^}]*)\}", re.S)


def row(name: str, out: Path) -> dict:
    s = json.loads((out / name / "call1" / "summary.json").read_text())
    ufo = out / name / "call1" / "round0" / "UFO"
    log = (out / name / "call1" / "round0" / "compile.log").read_text(errors="replace")
    r = {"model": name, "compile_ok": s["compile_ok"], "checks": s["checks"], "madgraph_import_ok": s["madgraph_import_ok"],
         "doubly_defined_particle_class_warnings": log.count("Doubly defined particle classes"),
         "doubly_defined_parameter_warnings": log.count("Doubly defined parameter classes"),
         "feynman_gauge": (re.search(r"HEPTAPOD-GAUGE\|feynman=(\w+)", log) or [None, None])[1]}
    if (ufo / "vertices.py").is_file():
        verts = VERTEX.findall((ufo / "vertices.py").read_text())
        coup = (ufo / "couplings.py").read_text()
        params = (ufo / "parameters.py").read_text()
        tt = [c for _n, parts, cp in verts if "P.H2" in parts and "P.t__tilde__" in parts
              for g in re.findall(r"C\.(GC_\d+)", cp)
              for c in re.findall(rf"{g} = Coupling\(name = '{g}',\s*value = '([^']*)'", coup)]
        r.update(vertices=len(verts), vertices_with_H2=sum("P.H2" in parts for _n, parts, _c in verts),
                 ghost_vertices=sum("P.gh" in parts for _n, parts, _c in verts),
                 H2_t_tbar_couplings=tt,
                 lam_in_ufo=re.findall(r"lam = Parameter\(name = 'lam',\s*nature = '(\w+)',.*?value = ([^,]*),", params, re.S))
    mg = (s["row"].get("mg5_debug_tail") or "")
    m = re.search(r"InvalidModel: (.*)", mg)
    r["madgraph_error"] = m.group(1)[:120] if m else None
    return r


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", required=True)
    ap.add_argument("--run", action="store_true")
    args = ap.parse_args()
    out = Path(args.out)
    rows = []
    for fr in sorted(HERE.glob("*.fr")):
        if args.run and not (out / fr.stem / "call1" / "summary.json").is_file():
            subprocess.run([sys.executable, str(HEPVAL), "validate", str(fr), "--out", str(out / fr.stem)],
                           stdout=subprocess.DEVNULL, check=True)
        if (out / fr.stem / "call1" / "summary.json").is_file():
            rows.append(row(fr.stem, out))
    print(json.dumps(rows, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
