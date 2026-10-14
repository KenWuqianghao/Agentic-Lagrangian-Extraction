#!/usr/bin/env python3
"""The toolkit command the agent runs in the open-model benchmark's toolkit arm.

    ./frgen spec.json

1. parse spec.json and validate it against the FeynRulesModel schema
   (heptapod tools/frgen/frmodel.py) -- the Pydantic errors come back verbatim;
2. render model.fr with the deterministic renderer (tools/frgen/render.py);
3. lint model.fr with the deterministic lints (fr_lint.py), each finding tagged
   with the stage it predicts (compile / checks / mg5 / harness / warn).

It never runs Wolfram or MadGraph. It is what GenerateFeynRulesModelTool plus
the lint half of validatemodel give an agent, as a shell command, so any
harness with a restricted shell can call it.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLKIT = Path(os.environ["FRGEN_TOOLKIT"])  # dir holding frgen/ and fr_lint.py
sys.path.insert(0, str(TOOLKIT))

import fr_lint  # noqa: E402
from frgen.frmodel import FeynRulesModel  # noqa: E402
from frgen.render import render_model  # noqa: E402


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: ./frgen spec.json   (writes model.fr next to it, then lints it)")
        return 0
    spec = Path(argv[1])
    if not spec.is_file():
        print(f"ERROR: {spec} not found. Write the FeynRulesModel JSON there first.")
        return 0
    try:
        data = json.loads(spec.read_text())
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON in {spec}: {e}")
        return 0
    if not isinstance(data, dict):
        print("ERROR: the spec must be one JSON object (the FeynRulesModel).")
        return 0
    try:
        model = FeynRulesModel(**data)
    except Exception as e:  # noqa: BLE001  (pydantic ValidationError, validator ValueError)
        print(
            "SCHEMA VALIDATION FAILED. Fix the fields named below and run ./frgen again.\n"
            'Remember: numeric values are strings ("-1/3", "1500.").\n'
        )
        print(str(e))
        return 0
    try:
        fr_text = render_model(model)
    except Exception as e:  # noqa: BLE001
        print(f"RENDER FAILED: {type(e).__name__}: {e}")
        return 0
    out = spec.parent / "model.fr"
    out.write_text(fr_text)
    print(
        f"SCHEMA OK: {len(model.particles)} particle classes, {len(model.parameters)} parameters, "
        f"Lagrangian terms {[t.name for t in model.lagrangian_terms]}"
    )
    print(f"RENDERED: {out.name} ({len(fr_text.splitlines())} lines). You may read it.")
    findings = fr_lint.lint_text(fr_text)
    if not findings:
        print("LINT: no findings.")
        return 0
    print(
        f"LINT: {len(findings)} finding(s). Each names the stage it predicts will fail "
        "(compile, checks = a FeynRules consistency check, mg5 = MadGraph import, "
        "harness = the total Lagrangian cannot be identified, warn = may still pass). "
        "Fix the ones that are real defects; do not remove paper physics just to silence one."
    )
    for f in findings:
        loc = f" (model.fr line {f.line})" if f.line else ""
        print(f"- [{f.stage}] {f.rule}: {f.message}{loc}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
