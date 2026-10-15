"""The `env` fixture of the harness tests: a sandbox, a run directory, a fake
hepval and a fake referee `claude`."""

from __future__ import annotations

import os
import sys
import textwrap

import pytest

PY = sys.executable

FAKE_HEPVAL = textwrap.dedent("""
    import json, os, sys
    from pathlib import Path
    cmd = sys.argv[1]
    if cmd == "lint":
        print(json.dumps({"findings": [{"rule": "tensor_orderblock", "stage": "mg5", "line": 7,
                                        "message": "remove the OrderBlock"}]}))
    elif cmd == "validate":
        out = Path(sys.argv[sys.argv.index("--out") + 1]); out.mkdir(parents=True, exist_ok=True)
        n = len(list(out.glob("call*"))) + 1
        stage = os.environ.get("FAKE_STAGE", "checks")
        (out / f"call{n}").mkdir()
        (out / f"call{n}" / "summary.json").write_text(json.dumps(
            {"call": n, "stage_reached": stage, "full_chain_pass": stage == "pass",
             "checks": {"hermiticity": "fail"}, "madgraph_import_ok": False,
             "diag": "--diag" in sys.argv}))
        print("## FeynRules check `hermiticity`: fail\\n- vertex 1: fields H H2; block: LScalar")
    elif cmd == "massbasis":
        print(json.dumps({"tadpoles": {}, "spec_seen": json.loads(sys.argv[2])}))
""")

FAKE_CLAUDE = textwrap.dedent("""
    import json, sys
    sys.stdin.read()
    print(json.dumps({"result": "1. none\\nVERDICT: NO DISCREPANCIES", "is_error": False,
                      "usage": {"input_tokens": 10, "output_tokens": 5}, "total_cost_usd": 0.01}))
""")


@pytest.fixture()
def env(tmp_path):
    sb = tmp_path / "sandbox"
    rd = tmp_path / "run"
    (sb / "eval/benchmark_runs/X/text").mkdir(parents=True)
    (sb / "eval/benchmark_runs/X/text/paper_source.tex").write_text("\\section{Model}")
    (sb / "SM.fr").write_text("(* SM *)")
    (sb / "model.fr").write_text('M$ModelName = "X_gen";\n')
    rd.mkdir()
    (tmp_path / "hepval.py").write_text(FAKE_HEPVAL)
    (tmp_path / "claude").write_text(f"#!{PY}\n" + FAKE_CLAUDE)
    os.chmod(tmp_path / "claude", 0o755)
    e = {
        **os.environ,
        "CC_SANDBOX": str(sb),
        "CC_RUNDIR": str(rd),
        "CC_HEPVAL": str(tmp_path / "hepval.py"),
        "CC_CLAUDE_BIN": str(tmp_path / "claude"),
        "CC_PYTHON": PY,
        "CC_VALIDATE_BUDGET": "2",
        "CC_REVIEW_BUDGET": "1",
        "CC_MAX_CONTINUATIONS": "3",
    }
    return {"sb": sb, "rd": rd, "env": e, "tmp": tmp_path}
