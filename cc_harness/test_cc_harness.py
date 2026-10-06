"""Tests for the Claude Code harness that need no Wolfram kernel, MadGraph or
network: the MCP server (with a fake hepval and a fake referee), the
PreToolUse sandbox guard, the Stop gate, and the report diagnostics."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import diagnose  # noqa: E402

PY = sys.executable

FAKE_HEPVAL = textwrap.dedent('''
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
''')

FAKE_CLAUDE = textwrap.dedent('''
    import json, sys
    sys.stdin.read()
    print(json.dumps({"result": "1. none\\nVERDICT: NO DISCREPANCIES", "is_error": False,
                      "usage": {"input_tokens": 10, "output_tokens": 5}, "total_cost_usd": 0.01}))
''')


@pytest.fixture()
def env(tmp_path):
    sb = tmp_path / "sandbox"
    rd = tmp_path / "run"
    (sb / "eval/benchmark_runs/X/text").mkdir(parents=True)
    (sb / "eval/benchmark_runs/X/text/paper_source.tex").write_text("\\section{Model}")
    (sb / "SM.fr").write_text("(* SM *)")
    (sb / "model.fr").write_text("M$ModelName = \"X_gen\";\n")
    rd.mkdir()
    (tmp_path / "hepval.py").write_text(FAKE_HEPVAL)
    (tmp_path / "claude").write_text(f"#!{PY}\n" + FAKE_CLAUDE)
    os.chmod(tmp_path / "claude", 0o755)
    e = {**os.environ, "CC_SANDBOX": str(sb), "CC_RUNDIR": str(rd), "CC_HEPVAL": str(tmp_path / "hepval.py"),
         "CC_CLAUDE_BIN": str(tmp_path / "claude"), "CC_PYTHON": PY,
         "CC_VALIDATE_BUDGET": "2", "CC_REVIEW_BUDGET": "1", "CC_MAX_CONTINUATIONS": "3"}
    return {"sb": sb, "rd": rd, "env": e, "tmp": tmp_path}


def _mcp(env: dict, calls: list) -> list:
    msgs = [{"jsonrpc": "2.0", "id": 0, "method": "initialize",
             "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "t"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"}]
    for i, (name, args) in enumerate(calls, 1):
        if name == "LIST":
            msgs.append({"jsonrpc": "2.0", "id": i, "method": "tools/list"})
        else:
            msgs.append({"jsonrpc": "2.0", "id": i, "method": "tools/call", "params": {"name": name, "arguments": args}})
    r = subprocess.run([PY, str(HERE / "heptapod_mcp.py")], input="\n".join(json.dumps(m) for m in msgs) + "\n",
                       capture_output=True, text=True, env=env, timeout=120)
    return [json.loads(x) for x in r.stdout.splitlines() if x.strip()]


def _text(resp: dict) -> str:
    return resp["result"]["content"][0]["text"]


# ------------------------------------------------------------------ MCP
def test_mcp_lists_the_four_tools_with_budgets(env):
    out = _mcp(env["env"], [("LIST", None)])
    assert out[0]["result"]["serverInfo"]["name"] == "heptapod-tools"
    tools = {t["name"]: t for t in out[1]["result"]["tools"]}
    assert set(tools) == {"lint_model", "validate_model", "massbasis", "review_model"}
    assert "Budget: 2 calls" in tools["validate_model"]["description"]
    assert "Budget: 1 calls" in tools["review_model"]["description"]


def test_lint_model_formats_findings_and_refuses_paths_outside(env):
    out = _mcp(env["env"], [("lint_model", {"path": "model.fr"}), ("lint_model", {"path": "/etc/hosts"}),
                            ("lint_model", {"path": "../run/cc_state.json"})])
    assert "[mg5] tensor_orderblock (line 7)" in _text(out[1])
    assert out[2]["result"]["isError"] and "outside the sandbox" in _text(out[2])
    assert out[3]["result"]["isError"] and "outside the sandbox" in _text(out[3])


def test_validate_model_reports_call_number_stage_and_enforces_budget(env):
    out = _mcp(env["env"], [("validate_model", {"path": "model.fr"})] * 3)
    first, second, third = (_text(o) for o in out[1:])
    assert first.startswith("# validate_model call 1/2: stage reached = checks")
    assert "vertex 1: fields H H2; block: LScalar" in first
    assert "[mg5] tensor_orderblock" in first            # lint findings appended
    assert second.startswith("# validate_model call 2/2")
    assert out[3]["result"]["isError"] and "budget exhausted" in third
    st = json.loads((env["rd"] / "cc_state.json").read_text())
    assert st["validations"] == 2 and st["last_validation"]["stage"] == "checks"
    assert st["last_validation"]["model_sha"]
    summ = json.loads((env["rd"] / "validation/call1/summary.json").read_text())
    assert summ["diag"] is True                          # the in-loop call uses the diagnostic driver
    log = [json.loads(x) for x in (env["rd"] / "tool_calls.jsonl").read_text().splitlines()]
    assert any(r["event"] == "budget" for r in log)


def test_massbasis_passes_the_spec_and_rejects_bad_json(env):
    out = _mcp(env["env"], [("massbasis", {"spec": '{"fields": ["H"]}'}), ("massbasis", {"spec": "{not json"})])
    assert json.loads(_text(out[1]))["spec_seen"] == {"fields": ["H"]}
    assert out[2]["result"]["isError"] and "not valid JSON" in _text(out[2])


def test_review_model_runs_a_sandboxed_referee_within_budget(env):
    out = _mcp(env["env"], [("review_model", {"path": "model.fr"})] * 2)
    assert "VERDICT: NO DISCREPANCIES" in _text(out[1])
    assert out[2]["result"]["isError"] and "review budget exhausted" in _text(out[2])
    assert (env["rd"] / "review/review1.fr").is_file()
    meta = json.loads((env["rd"] / "review/review1_meta.json").read_text())
    assert meta["exit"] == 0 and meta["total_cost_usd"] == 0.01


# ---------------------------------------------------------------- guard
def _guard(env: dict, event: dict) -> dict | None:
    r = subprocess.run([PY, str(HERE / "hooks" / "pretool_guard.py")], input=json.dumps(event),
                       capture_output=True, text=True, env=env, timeout=60)
    return json.loads(r.stdout) if r.stdout.strip() else None


@pytest.mark.parametrize("tool,inp,allowed", [
    ("Read", {"file_path": "model.fr"}, True),
    ("Read", {"file_path": "eval/benchmark_runs/X/text/paper_source.tex"}, True),
    ("Write", {"file_path": "model.fr", "content": "x"}, True),
    ("Read", {"file_path": "/etc/passwd"}, False),
    ("Read", {"file_path": "../run/cc_state.json"}, False),
    ("Write", {"file_path": "new/../../escape.fr", "content": "x"}, False),
    ("Glob", {"pattern": "/Users/**/*.fr"}, False),
    ("Glob", {"pattern": "**/*.fr"}, True),
    ("Grep", {"pattern": "LTotal", "path": "/"}, False),
    ("Bash", {"command": "ls"}, False),
    ("WebFetch", {"url": "https://example.com"}, False),
    ("Task", {"prompt": "read /etc"}, False),
    ("mcp__heptapod-tools__validate_model", {"path": "model.fr"}, True),
    ("mcp__other__read", {}, False),
])
def test_guard_confines_tools_to_the_sandbox(env, tool, inp, allowed):
    ev = {"hook_event_name": "PreToolUse", "tool_name": tool, "tool_input": inp, "cwd": str(env["sb"])}
    out = _guard(env["env"], ev)
    if allowed:
        assert out is None
    else:
        assert out["hookSpecificOutput"]["permissionDecision"] == "deny"
    log = [json.loads(x) for x in (env["rd"] / "hook_log.jsonl").read_text().splitlines()]
    assert log[-1]["decision"] == ("allow" if allowed else "deny")


# ----------------------------------------------------------------- stop
def _stop(env: dict, active: bool) -> dict | None:
    r = subprocess.run([PY, str(HERE / "hooks" / "stop_gate.py")],
                       input=json.dumps({"hook_event_name": "Stop", "stop_hook_active": active}),
                       capture_output=True, text=True, env=env, timeout=60)
    return json.loads(r.stdout) if r.stdout.strip() else None


def _state(env, **last):
    sys.path.insert(0, str(HERE))
    import common as C
    st = C.load_state(env["rd"])
    st["validations"] = last.pop("validations", 1)
    st["validate_budget"] = last.pop("budget", 10)
    rep = env["rd"] / "report.md"
    rep.write_text("# validate_model call 1/10: stage reached = checks\n- hermiticity: fail\n"
                   "## compile log, distinct lines (tail)\nNOISE")
    st["last_validation"] = {"call": 1, "report": str(rep), "model_sha": C.sha(env["sb"] / "model.fr"), **last}
    C.save_state(env["rd"], st)


def test_stop_gate_blocks_a_failing_model_then_releases_after_three(env):
    _state(env, stage="checks", told_pass=False)
    reasons = []
    for i in range(3):
        out = _stop(env["env"], active=i > 0)
        assert out and out["decision"] == "block"
        reasons.append(out["reason"])
    assert "[stop gate 1/3]" in reasons[0] and "stage reached = checks" in reasons[0]
    assert "hermiticity: fail" in reasons[0] and "NOISE" not in reasons[0]   # digest, not the log
    assert _stop(env["env"], active=True) is None                            # 4th stop: released
    log = [json.loads(x) for x in (env["rd"] / "stop_gate_log.jsonl").read_text().splitlines()]
    assert [r["decision"] for r in log] == ["block", "block", "block", "allow"]
    assert "continuation limit" in log[-1]["why"] and log[1]["stop_hook_active"] is True


def test_stop_gate_blocks_missing_or_unvalidated_or_stale_model(env):
    (env["sb"] / "model.fr").unlink()
    assert "does not exist" in _stop(env["env"], False)["reason"]
    (env["sb"] / "model.fr").write_text("M$ModelName = \"X_gen\";\n")
    assert "have not run validate_model" in _stop(env["env"], False)["reason"]
    (env["rd"] / "stop_gate.json").unlink()
    _state(env, stage="pass", told_pass=True)
    (env["sb"] / "model.fr").write_text("edited after the pass\n")
    assert "changed after the last validate_model" in _stop(env["env"], False)["reason"]


def test_stop_gate_allows_a_passing_model_and_a_spent_budget(env):
    _state(env, stage="pass", told_pass=True)
    assert _stop(env["env"], False) is None
    _state(env, stage="mg5", told_pass=False, validations=10, budget=10)
    assert _stop(env["env"], False) is None
    log = [json.loads(x) for x in (env["rd"] / "stop_gate_log.jsonl").read_text().splitlines()]
    assert "budget spent" in log[-1]["why"]


# ------------------------------------------------------------ diagnose
def test_hermiticity_vertices_are_located_in_their_block():
    log = "\n".join([
        "HEPTAPOD-HERM|i=1|fields=vebar,N1,Z|expr=(-I/2) gw VlN1",
        "HEPTAPOD-HERM|i=2|fields=H,H2|expr=I lam3",
        "HEPTAPOD-HERMBLOCK|block=LNZ|contents=N1bar ve Z;ve vebar Z",
        "HEPTAPOD-HERMBLOCK|block=LScalar|contents=H H2;H H",
        "HEPTAPOD-HERMBLOCK|block=LBig|contents=TIMEOUT",
    ])
    d = diagnose.parse_diag_lines(log)
    loc = diagnose.localize_herm(d["herm"], d["blocks"])
    assert loc[0]["blocks"] == ["LNZ"]           # matched through the conjugate fields
    assert loc[1]["blocks"] == ["LScalar"]
    assert d["blocks"]["LBig"] is None
    # an unreduced vertex: a union of fields from several terms of one block
    un = diagnose.parse_diag_lines(
        "HEPTAPOD-HERM|i=1|fields=W,n4,ta,n5,e|unreduced=n4,ta,n5,e|expr=x\n"
        "HEPTAPOD-HERMBLOCK|block=LWN|contents=W n4bar ta;W n5bar e\n"
        "HEPTAPOD-HERMBLOCK|block=LKin|contents=n4bar n4\n")
    assert diagnose.localize_herm(un["herm"], un["blocks"])[0]["blocks"] == ["LWN"]   # not the kinetic block


def test_report_sections_for_mass_terms_and_hermiticity():
    log = ("HEPTAPOD-MASSTERM|fields=H,H2|coefficient=ca sa lam3 vev xBL|numeric=2967.3\n"
           "HEPTAPOD-TADPOLE|field=H|coefficient=muH^2 vev - lam vev^3|numeric=-5.97*^6\n"
           "HEPTAPOD-HERM|i=1|fields=H,H2|expr=I lam3\nHEPTAPOD-HERMBLOCK|block=LScalar|contents=H H2\n")
    row = {"checks": {"hermiticity": "fail", "mass_diagonal": "fail"}, "compile_ok": True, "madgraph_import_ok": True}
    md = diagnose.render_sections(row, log, "")
    assert "| H H2 | `ca sa lam3 vev xBL` | 2967.3 |" in md
    assert "| H | `muH^2 vev - lam vev^3` | -5.97*^6 |" in md
    assert "vertex 1: fields H H2; block: LScalar" in md


RUNS = Path.home() / "Documents/Github/heptapod/eval/benchmark_runs"


@pytest.mark.parametrize("page,expect_line_text", [
    ("B-L-SM", "B_L"), ("HeavyN", "NLbar[sp].Ga[mu].vl[sp, ff]"), ("Wprime", "WpLeR == {")])
def test_mg5_backtrace_points_at_the_fr_line(page, expect_line_text):
    d = RUNS / page / "rerun/pi_qwen_harness/s1"
    calls = sorted((d / "validation").glob("call*/summary.json"), key=lambda x: int(x.parent.name[4:]))
    if not calls:
        pytest.skip("stored run not present")
    row = json.loads(calls[-1].read_text())["row"]
    if not Path(row.get("ufo_dir") or "").is_dir():
        pytest.skip("stored UFO not present")
    fr = (calls[-1].parent / "model.fr").read_text()
    lines = [x["text"] for e in diagnose.mg5_backtrace(row, fr) for x in e["fr_lines"][:3]]
    assert any(expect_line_text in t for t in lines), lines
