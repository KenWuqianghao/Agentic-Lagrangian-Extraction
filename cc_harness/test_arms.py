"""Tests for the ablation arms (common.ARMS): what each arm's agent is told
and given. No Wolfram kernel, MadGraph or network."""

from __future__ import annotations

import hashlib
import json
import sys
import textwrap
from pathlib import Path
from types import SimpleNamespace

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import common as C  # noqa: E402
import run_cc  # noqa: E402
from test_cc_harness import _mcp, _stop, env  # noqa: E402,F401

TEMPLATE = (HERE / "prompts" / "protocol.md").read_text()
# cc_harness/prompts/protocol.md at 9d0643b: the prompt of the stored cc_sonnet_harness runs.
STORED_PROTOCOL_SHA256 = "925ada087732e355f195d4cb5ef1c165d6c91146120c894bcd60213a1dd02767"

# A fake chain: the compile is good and hermiticity fails. Each view prints
# what hepval's view prints: no verdict, the verdict, or the verdict located.
FAKE_HEPVAL_ARMS = textwrap.dedent('''
    import json, sys
    from pathlib import Path
    if sys.argv[1] == "lint":
        print(json.dumps({"findings": []}))
    elif sys.argv[1] == "validate":
        out = Path(sys.argv[sys.argv.index("--out") + 1])
        n = len(list(out.glob("call*"))) + 1
        (out / f"call{n}").mkdir(parents=True)
        (out / f"call{n}" / "summary.json").write_text(json.dumps(
            {"call": n, "stage_reached": "checks", "full_chain_pass": False, "compile_ok": True}))
        if "--view" in sys.argv:
            print("# Compile report: OK")
        else:
            print("## FeynRules check `hermiticity`: fail")
            if "--diag" in sys.argv:
                print("- vertex 1: fields H H2; block: LScalar")
''')


def _arm_env(env, arm):
    (env["tmp"] / "hepval.py").write_text(FAKE_HEPVAL_ARMS)
    return {**env["env"], "CC_ARM": arm}


def test_full_arm_protocol_is_the_stored_harness_prompt():
    text = C.render_protocol(TEMPLATE, C.ARMS["full"], 10, 3)
    assert hashlib.sha256(text.encode()).hexdigest() == STORED_PROTOCOL_SHA256


@pytest.mark.parametrize("arm", sorted(C.ARMS))
def test_protocol_names_only_the_arms_tools_and_keeps_the_sm_override_recipe(arm):
    text = C.render_protocol(TEMPLATE, C.ARMS[arm], 6, 3)
    for tool in C.TOOLS:
        assert (f"`{tool}`" in text) == (tool in C.ARMS[arm].tools), tool
    assert "LTotal := LSM - LHiggs + LScalar" in text
    assert not any(x in text for x in ("<!--", "{tool_list}", "{validate_budget}", "{max_continuations}"))
    if C.ARMS[arm].feedback != "diag":
        assert "the report lists" not in text


@pytest.mark.parametrize("arm", sorted(C.ARMS))
def test_mcp_serves_only_the_arms_tools(env, arm):
    e = _arm_env(env, arm)
    out = _mcp(e, [("LIST", None), ("lint_model", {"path": "model.fr"})])
    assert tuple(t["name"] for t in out[1]["result"]["tools"]) == tuple(
        t for t in C.TOOLS if t in C.ARMS[arm].tools)
    assert out[2]["result"]["isError"] == ("lint_model" not in C.ARMS[arm].tools)


def test_compile_arm_hides_the_checks_and_its_gate_accepts_a_compiled_model(env):
    e = _arm_env(env, "compile")
    text = _mcp(e, [("validate_model", {"path": "model.fr"})])[1]["result"]["content"][0]["text"]
    assert "compiled" in text.splitlines()[0]
    assert "hermiticity" not in text and "stage reached" not in text and "lint" not in text
    st = C.load_state(env["rd"])["last_validation"]
    assert st["told_pass"] is True and st["full_chain_pass"] is False
    assert _stop(e, False) is None


def test_import_arm_gate_also_needs_the_madgraph_import(env):
    e = _arm_env(env, "import")           # the fake chain compiles and has no MadGraph result
    text = _mcp(e, [("validate_model", {"path": "model.fr"})])[1]["result"]["content"][0]["text"]
    assert "MadGraph import failed" in text.splitlines()[0] and "hermiticity" not in text
    assert _stop(e, False)["decision"] == "block"


@pytest.mark.parametrize("arm,located", [("heptapod", False), ("diag", True)])
def test_check_arms_show_verdicts_and_their_gate_blocks_a_failing_chain(env, arm, located):
    e = _arm_env(env, arm)
    text = _mcp(e, [("validate_model", {"path": "model.fr"})])[1]["result"]["content"][0]["text"]
    assert "stage reached = checks" in text and "hermiticity" in text
    assert ("block: LScalar" in text) == located
    assert "## lint findings" not in text
    assert _stop(e, False)["decision"] == "block"


def test_no_tools_arm_has_no_server_no_gate_and_no_verdict_to_report(tmp_path, monkeypatch):
    monkeypatch.setattr(run_cc.run_pi, "build_prompt", lambda page, arm: "OUTPUT: summarise the model and the last validate_model verdict.")
    args = SimpleNamespace(arm="none", validate_budget=6, review_budget=2, max_continuations=3,
                           model="m", review_model="")
    run_cc.write_configs(tmp_path, tmp_path, args)
    assert json.loads((tmp_path / "mcp.json").read_text()) == {"mcpServers": {}}
    assert "Stop" not in json.loads((tmp_path / "settings.json").read_text())["hooks"]
    cmd = run_cc.agent_cmd(tmp_path, "m", C.ARMS["none"])
    assert "mcp__" not in " ".join(cmd)
    assert "validate_model" not in run_cc.task_prompt("X", C.ARMS["none"])
    assert "validate_model" in run_cc.task_prompt("X", C.ARMS["full"])


def test_a_run_from_a_draft_starts_with_that_file_and_is_told_so(tmp_path, monkeypatch):
    stored = tmp_path / "stored" / "X" / "rerun" / "v_oneshot" / "s1" / "model"
    stored.mkdir(parents=True)
    (stored / "X_gen.fr").write_text("(* draft *)")
    paper = tmp_path / "paper_source.tex"
    paper.write_text("paper")
    monkeypatch.setattr(run_cc, "DRAFT_RUNS", tmp_path / "stored")
    monkeypatch.setattr(run_cc.run_pi, "paper_file", lambda page: paper)
    monkeypatch.setattr(run_cc.run_pi, "SM_FR", paper)
    monkeypatch.setattr(run_cc.run_pi, "build_prompt", lambda page, arm: "TASK and the last validate_model verdict.")
    rundir = tmp_path / "run"
    rundir.mkdir()
    sb = run_cc.make_sandbox("X", rundir, run_cc.draft_file("X", "v_oneshot"))
    assert (sb / "model.fr").read_text() == "(* draft *)"
    assert "first draft" in run_cc.task_prompt("X", C.ARMS["heptapod"], draft=True)
    assert "first draft" not in run_cc.task_prompt("X", C.ARMS["heptapod"])
    assert not (run_cc.make_sandbox("X", rundir) / "model.fr").exists()
