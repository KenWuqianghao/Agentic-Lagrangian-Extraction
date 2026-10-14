"""Validate one .fr through the corrected chain: compile + 4 checks + MadGraph import."""

import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent))
# The tools packages import orchestral in their __init__; register the two
# modules the validator needs straight from their files instead.
import importlib.util
import types

REPO = HERE.parent.parent


def _load(modname, rel):
    spec = importlib.util.spec_from_file_location(modname, REPO / rel)
    m = importlib.util.module_from_spec(spec)
    sys.modules[modname] = m
    spec.loader.exec_module(m)
    return m


for name in ("tools", "tools.frgen", "tools.feynrules"):
    sys.modules.setdefault(name, types.ModuleType(name))
_load("tools.frgen.fr_parser", "tools/frgen/fr_parser.py")
_load("tools.feynrules.lagrangian_checks", "tools/feynrules/lagrangian_checks.py")
import validation_benchmark as vb

page, fr, tag = sys.argv[1], Path(sys.argv[2]).resolve(), sys.argv[3]
OUT = Path(os.environ["VBENCH_OUT"])
lag, info = vb.total_lag_symbol(fr)
row = {"page": page, "fr": str(fr), "lag_symbol": lag, "lag_resolution": info, "t0": time.time()}
if not lag:
    row["status"] = (
        "ambiguous_lagrangian_symbol" if info.get("ambiguous") else "no_lagrangian_symbol"
    )
else:
    outdir = OUT / tag / f"{page}_UFO"
    comp = vb.compile_to_ufo(page, fr, lag, outdir)
    row.update(comp)
    if comp["compile_ok"]:
        row["n_particles_ufo"] = vb.count_new_particles(outdir)
        row.update(vb.madgraph_import(outdir, OUT / tag / "mg5run"))
        row["status"] = "compiled"
    else:
        row["status"] = "compile_timeout" if comp["timed_out"] else "compile_failed"
    row["full_chain_pass"] = bool(
        comp["compile_ok"] and vb.all_checks_pass(comp["checks"]) and row.get("madgraph_import_ok")
    )
row["seconds_total"] = time.time() - row["t0"]
(OUT / tag / "result.json").parent.mkdir(parents=True, exist_ok=True)
(OUT / tag / "result.json").write_text(json.dumps(row, indent=1, default=str))
print(
    json.dumps(
        {
            k: row.get(k)
            for k in (
                "status",
                "compile_ok",
                "checks",
                "madgraph_import_ok",
                "full_chain_pass",
                "seconds",
                "lagrangian_expression",
            )
        },
        indent=1,
    )
)
