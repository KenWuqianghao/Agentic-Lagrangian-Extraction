#!/usr/bin/env python3
"""MCP server `heptapod-tools`: the heptapod physics chain as Claude Code tools.

    lint_model      deterministic lints (fr_lint + bracket/comment structure), milliseconds
    validate_model  FeynRules compile, the four consistency checks, MadGraph import:
                    the chain the benchmark scores (budgeted); the report says which
                    call this is and how far the chain got, and adds the non-hermitian
                    vertices, the off-diagonal mass terms and the MadGraph back-trace
    massbasis       tadpoles, mass matrix and inverted couplings for a scalar potential
    review_model    an independent referee (a fresh `claude -p` that did not write the
                    model) compares model.fr with the paper (budgeted)

Every tool calls pi_harness/hepval.py, the back end the pi harness uses. The
server speaks MCP over stdio (newline-delimited JSON-RPC 2.0) without the SDK.
It refuses any path outside CC_SANDBOX, keeps its counters in
CC_RUNDIR/cc_state.json (the Stop hook reads the last verdict there) and logs
every call to CC_RUNDIR/tool_calls.jsonl.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as C  # noqa: E402

PROTOCOL_VERSION = "2025-06-18"

REVIEW_PROMPT = """You are an independent referee. You did not write the model under review.

Files in the working directory: the paper (LaTeX source under eval/benchmark_runs/*/text/),
SM.fr (the Standard Model file the add-on is loaded on top of), and the model under review, MODEL_PATH.

Read the paper's model-defining sections and the whole model file. Report every place where the
model does not implement the paper's model. Check, term by term:
- every new field of the paper is present, with the paper's spin, colour/SU(2) representation,
  hypercharge/charge and any new U(1) charge;
- every Lagrangian term of the paper is present with the paper's coefficient, sign,
  normalisation (fractions, roots, 1/Lambda powers) and index/chirality structure;
- nothing the paper has was dropped or set to zero, and nothing was added that the paper does not have
  (kinetic and mass terms for new fields, SM-override bookkeeping such as LSM - LHiggs, and
  mixing-angle reparametrisations that are equivalent to the paper's are fine);
- mixing: the mass eigenstates and the angle match the paper's definitions.

Do not comment on FeynRules syntax or style. Output a numbered list of discrepancies, each with the
paper equation or LaTeX line and the model line, and a severity (physics-changing / cosmetic).
If you find none, say "NO DISCREPANCIES". End with one line: VERDICT: NO DISCREPANCIES, or
VERDICT: <n> PHYSICS-CHANGING, <m> COSMETIC."""  # noqa: E501

TOOL_SPECS = [
    {
        "name": "lint_model",
        "description": "Deterministic lints for a FeynRules add-on .fr file (milliseconds). Each "
        "finding names the rule, the stage it predicts (compile, checks, mg5, harness, warn) and "
        "the line. Run it after every edit and before validate_model; it does not use the budget.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "the .fr file, e.g. model.fr"}
            },
            "required": ["path"],
        },
    },
    {
        "name": "validate_model",
        "description": "{validate_description}",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "the .fr file, e.g. model.fr"}
            },
            "required": ["path"],
        },
    },
    {
        "name": "review_spec",
        "description": "An independent referee reads the paper and spec.json (your list of the "
        "new fields and of the interaction vertices the model must have) and lists what the "
        "paper has and the list lacks, "
        "and what the list has and the paper lacks. Run it once, after you write spec.json and "
        "before you write model.fr. Budget: 1 call.",
        "inputSchema": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "spec.json"}},
            "required": ["path"],
        },
    },
    {
        "name": "massbasis",
        "description": "Symbolic quadratic-sector analysis of a scalar potential (sympy, about 1 "
        "s). Give the potential V (the Lagrangian contains -V) in gauge-basis symbols, the "
        "substitutions that express each gauge-basis field through the vev and the mass-basis REAL "
        "fields, the mixing angles as sine/cosine symbol pairs, the target physical masses, and "
        "the parameters to solve for. Returns the tadpoles, the mass-squared matrix at the vacuum, "
        "the non-zero off-diagonal entries, and with solve_for the inverted parametrisation in "
        'Mathematica syntax, verified. Example spec: {"potential": "-muPsq/2*p**2 + lambdaP/8*p**4 '
        '- muSsq/2*s**2 + lambdaS/8*s**4 + lambdaPS/4*p**2*s**2", "substitutions": {"p": "vev + '
        'ct*H + st*h2", "s": "vs - st*H + ct*h2"}, "fields": ["H", "h2"], "angles": {"theta": '
        '["st", "ct"]}, "targets": {"H": "MH", "h2": "Mh2"}, "solve_for": ["muPsq", "muSsq", '
        '"lambdaP", "lambdaS", "lambdaPS"]}',
        "inputSchema": {
            "type": "object",
            "properties": {
                "spec": {
                    "type": "string",
                    "description": "JSON object: potential, substitutions, fields, angles, "
                    "targets, solve_for",
                }
            },
            "required": ["spec"],
        },
    },
    {
        "name": "review_model",
        "description": "An independent referee (a fresh agent that did not write the model) reads "
        "the paper and the .fr file and lists every place the model departs from the paper: "
        "missing or extra fields and terms, wrong coefficients, signs, normalisations, charges, "
        "mixing. Run it once the chain passes. Budget: {review_budget} calls per run. A "
        "physics-changing discrepancy must be fixed even if the chain passes.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "the .fr file, e.g. model.fr"}
            },
            "required": ["path"],
        },
    },
]


_CHAIN = (
    "Run the scored chain on a .fr file: FeynRules compile (Wolfram), the four FeynRules "
    "consistency checks (hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum), "
    "then MadGraph 'import model'. 1 to 15 minutes; calls queue for one Wolfram kernel. "
    "Budget: {budget} calls per run. The report states the call number, the stage the "
    "chain reached (compile / checks / mg5 / pass), the verdicts"
)
VALIDATE_DESCRIPTIONS = {
    "real": _CHAIN
    + (
        ", the non-zero vertices of L - HC[L] with the Lagrangian block that holds them, the "
        "off-diagonal mass terms and tadpoles, the mass-spectrum rows that disagree, statements "
        "cut at a line end and new particles that are in no vertex of the UFO (a model with "
        "either is not a pass), UFO parameters defined twice, and for a MadGraph failure the UFO "
        "object that broke with the model.fr lines behind it."
    ),
    "opt": _CHAIN
    + (
        ", the non-zero vertices "
        "of L - HC[L] with the Lagrangian block that holds them, the off-diagonal mass terms "
        "and tadpoles, the mass-spectrum rows that disagree, new particles that are in no "
        "vertex of the UFO (such a model is not a pass), UFO parameters defined twice, and "
        "for a MadGraph failure the UFO object that broke with the model.fr lines behind it."
    ),
    "diag": _CHAIN
    + (
        ", the non-zero vertices "
        "of L - HC[L] with the Lagrangian block that holds them, the off-diagonal mass terms "
        "and tadpoles, and for a MadGraph failure the UFO object that broke with the model.fr "
        "lines behind it."
    ),
    "checks": _CHAIN + ", FeynRules' own message for each failing check, and the MadGraph error.",
    "compile": "Run FeynRules (Wolfram) on a .fr file loaded on top of SM.fr and write the UFO. 1 "
    "to 15 minutes; calls queue for one Wolfram kernel. Budget: {budget} calls per run. The report "
    "states the call number and whether the UFO was written, with the FeynRules log when it was "
    "not.",
    "import": "Run FeynRules (Wolfram) on a .fr file loaded on top of SM.fr, write the UFO, and "
    "run MadGraph 'import model' on it. 1 to 15 minutes; calls queue for one Wolfram kernel. "
    "Budget: {budget} calls per run. The report states the call number, whether the UFO was "
    "written (with the FeynRules log when it was not) and whether MadGraph imported it (with "
    "MadGraph's output when it did not).",
}


class ToolError(Exception):
    pass


def _path(arg: str) -> Path:
    ok, real = C.inside(arg or "model.fr", C.sandbox())
    if not ok:
        raise ToolError(
            f"path {arg} is outside the sandbox; only files under the working directory exist"
        )
    if not real.is_file():
        raise ToolError(f"{arg} does not exist; write it first")
    return real


def _run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, stdin=subprocess.DEVNULL, **kw)


def lint_model(args: dict) -> str:
    fr = _path(args.get("path", "model.fr"))
    r = _run([C.PYTHON, str(C.HEPVAL), "lint", str(fr), *_lint_flags()])
    if r.returncode != 0:
        raise ToolError(r.stderr[-1500:] or "lint failed")
    return _lint_text(r.stdout)


def _lint_flags() -> list[str]:
    arm = C.arm()
    flags = {"opt": ["--opt"], "real": ["--real"], "cover": ["--real"]}.get(arm.feedback, [])
    return flags + (["--chain-head"] if arm.recipes else [])


def _lint_text(raw: str) -> str:
    try:
        d = json.loads(raw)
    except json.JSONDecodeError:
        return raw
    fs = d.get("findings") or []
    if not fs:
        return "lint: no findings"
    order = {"harness": 0, "compile": 1, "mg5": 2, "checks": 3, "warn": 4}
    fs.sort(key=lambda f: (order.get(f.get("stage"), 9), f.get("line") or 0))
    lines = [f"lint: {len(fs)} finding(s)"]
    lines += [
        f"- [{f.get('stage')}] {f.get('rule')} (line {f.get('line')}): {f.get('message')}"
        for f in fs
    ]
    return "\n".join(lines)


def validate_model(args: dict) -> str:
    rd = C.rundir()
    st = C.load_state(rd)
    fr = _path(args.get("path", "model.fr"))
    if st["validations"] >= st["validate_budget"]:
        C.log(rd, "tool_calls.jsonl", {"event": "budget", "tool": "validate_model"})
        lint = "Use lint_model, fix" if "lint_model" in C.arm().tools else "Fix"
        raise ToolError(
            f"validation budget exhausted ({st['validate_budget']} calls). {lint} what "
            "the last report named, and finish."
        )
    n = st["validations"] + 1
    st["validations"] = n
    C.save_state(rd, st)
    arm = C.arm()
    view = {
        "diag": ["--diag"],
        "opt": ["--opt"],
        "real": ["--real"],
        "cover": ["--cover"],
        "checks": [],
        "compile": ["--view", "compile"],
        "import": ["--view", "import"],
    }[arm.feedback]
    # hepval numbers its call directories itself; `n` runs ahead of that once a call
    # fails before hepval makes its directory.
    k = len(list((rd / "validation").glob("call*"))) + 1
    t0 = time.time()
    r = _run([C.PYTHON, str(C.HEPVAL), "validate", str(fr), "--out", str(rd / "validation"), *view])
    if r.returncode != 0:
        C.log(rd, "tool_calls.jsonl", {"event": "validator_error", "n": n, "err": r.stderr[-800:]})
        raise ToolError(f"validator error (not a model verdict): {r.stderr[-1500:]}")
    summ_file = rd / "validation" / f"call{k}" / "summary.json"
    summ = json.loads(summ_file.read_text()) if summ_file.is_file() else {}
    stage = summ.get("stage_reached") or "unknown"
    if arm.feedback in ("compile", "import"):
        # These arms are told only what a generic build loop sees; that is
        # also all their Stop gate can ask for.
        compiled = bool(summ.get("compile_ok"))
        told_pass = compiled and (arm.feedback == "compile" or bool(summ.get("madgraph_import_ok")))
        outcome = (
            "compile failed"
            if not compiled
            else "compiled"
            if arm.feedback == "compile"
            else "compiled and imported"
            if told_pass
            else "compiled, MadGraph import failed"
        )
        head = (
            f"# validate_model call {n}/{st['validate_budget']}: {outcome}\n"
            f"Calls left: {st['validate_budget'] - n}.\n"
        )
    else:
        # In the optimisation arm a chain pass with a vertex-less new particle is not a pass.
        covered = summ.get("coverage", {"complete": True})["complete"]
        told_pass = (
            bool(summ.get("full_chain_pass"))
            and not summ.get("particles_without_vertex")
            and covered
        )
        if summ.get("full_chain_pass") and not told_pass:
            stage = (
                "pass, but spec.json is not covered by the UFO"
                if not covered
                else "pass, but the model is not done: "
                + ", ".join(summ["particles_without_vertex"][:6])
                if arm.feedback in ("real", "cover")
                else "pass, but new particles have no vertex"
            )
        head = (
            f"# validate_model call {n}/{st['validate_budget']}: stage reached = {stage}"
            f"{' (FULL CHAIN PASS)' if told_pass else ''}\n"
            f"Stages: compile -> checks -> mg5 -> pass. Calls left: {st['validate_budget'] - n}.\n"
        )
    report = head + "\n" + r.stdout + "\n"
    if "lint_model" in arm.tools:
        lint = _run([C.PYTHON, str(C.HEPVAL), "lint", str(fr), *_lint_flags()])
        report += "\n## lint findings\n" + _lint_text(lint.stdout) + "\n"
    (rd / "validation" / f"call{k}").mkdir(parents=True, exist_ok=True)
    (rd / "validation" / f"call{k}" / "agent_report.md").write_text(report)
    st = C.load_state(rd)
    st["last_validation"] = {
        "call": n,
        "stage": stage,
        "full_chain_pass": bool(summ.get("full_chain_pass")),
        "told_pass": told_pass,
        "model_sha": C.sha(fr),
        "path": str(fr),
        "report": str(rd / "validation" / f"call{k}" / "agent_report.md"),
        "checks": summ.get("checks"),
        "madgraph_import_ok": summ.get("madgraph_import_ok"),
        "seconds": round(time.time() - t0, 1),
    }
    C.save_state(rd, st)
    return report


def massbasis(args: dict) -> str:
    spec = args.get("spec") or ""
    try:
        json.loads(spec)
    except json.JSONDecodeError as e:
        raise ToolError(f"spec is not valid JSON: {e}")
    r = _run([C.PYTHON, str(C.HEPVAL), "massbasis", spec], timeout=600)
    if r.returncode != 0:
        raise ToolError(r.stderr[-2000:])
    return r.stdout


def _referee(rd: Path, target: Path, tag: str, prompt: str, frozen_name: str) -> str:
    """A fresh `claude -p` in its own sandbox with the paper, SM.fr and a frozen copy of
    `target`; writes review/<tag>.md and review/<tag>_meta.json and returns the text."""
    rev = Path(tempfile.mkdtemp(prefix="cc-referee-"))
    sb = C.sandbox()
    for p in sb.rglob("*"):
        if p.is_file() and (p.name == "SM.fr" or "/text/" in str(p)):
            dst = rev / p.relative_to(sb)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dst)
    shutil.copy2(target, rev / frozen_name)
    (rd / "review").mkdir(parents=True, exist_ok=True)
    settings = {
        "hooks": {
            "PreToolUse": [
                {
                    "matcher": "*",
                    "hooks": [
                        {
                            "type": "command",
                            "command": f"{C.PYTHON} {C.HERE / 'hooks' / 'pretool_guard.py'}",
                        }
                    ],
                }
            ]
        }
    }
    (rd / "review" / f"{tag}_settings.json").write_text(json.dumps(settings))
    (rd / "review" / f"{tag}_mcp.json").write_text('{"mcpServers": {}}')
    model = (
        os.environ.get("CC_REVIEW_MODEL") or os.environ.get("CC_AGENT_MODEL") or "claude-sonnet-5"
    )
    cmd = [
        C.CLAUDE,
        "-p",
        "--output-format",
        "json",
        "--model",
        model,
        "--setting-sources",
        "",
        "--settings",
        str(rd / "review" / f"{tag}_settings.json"),
        "--mcp-config",
        str(rd / "review" / f"{tag}_mcp.json"),
        "--strict-mcp-config",
        "--tools",
        "Read,Glob,Grep",
        "--allowedTools",
        "Read,Glob,Grep",
        "--permission-mode",
        "dontAsk",
        "--disallowedTools",
        "Bash,WebFetch,WebSearch,Write,Edit,NotebookEdit,Task,Agent",
    ]
    env = {
        **os.environ,
        "CC_SANDBOX": str(rev),
        "CC_RUNDIR": str(rd / "review" / f"{tag}_run"),
        "CC_ROLE": "referee",
        "CC_ARM": "full",
    }
    t0 = time.time()
    r = subprocess.run(
        cmd,
        cwd=str(rev),
        env=env,
        input=prompt.replace("MODEL_PATH", frozen_name),
        capture_output=True,
        text=True,
        timeout=3600,
    )
    try:
        out = json.loads(r.stdout)
    except json.JSONDecodeError:
        out = {"result": r.stdout, "is_error": True}
    text = out.get("result") or ""
    (rd / "review" / f"{tag}.md").write_text(text)
    (rd / "review" / f"{tag}_meta.json").write_text(
        json.dumps(
            {
                "exit": r.returncode,
                "seconds": round(time.time() - t0, 1),
                "usage": out.get("usage"),
                "total_cost_usd": out.get("total_cost_usd"),
                "model": model,
                "stderr": r.stderr[-800:],
                "model_sha": C.sha(target),
            },
            indent=1,
        )
    )
    if r.returncode != 0 or not text:
        raise ToolError(f"referee failed (exit {r.returncode}): {r.stderr[-800:]}")
    return text


def review_model(args: dict) -> str:
    rd = C.rundir()
    st = C.load_state(rd)
    fr = _path(args.get("path", "model.fr"))
    if st["reviews"] >= st["review_budget"]:
        raise ToolError(f"review budget exhausted ({st['review_budget']} calls)")
    n = st["reviews"] + 1
    st["reviews"] = n
    C.save_state(rd, st)
    (rd / "review").mkdir(parents=True, exist_ok=True)
    shutil.copy2(fr, rd / "review" / f"review{n}.fr")
    text = _referee(rd, fr, f"review{n}", REVIEW_PROMPT, "model_under_review.fr")
    st = C.load_state(rd)
    st["review_log"].append(
        {"n": n, "model_sha": C.sha(fr), "verdict": C.verdict_line(text), "exit": 0}
    )
    C.save_state(rd, st)
    return f"review {n}/{st['review_budget']} of model.fr\n\n{text}"


SPEC_REVIEW_PROMPT = """You are an independent referee. You did not write the list under review.

Files in the working directory: the paper (LaTeX source under eval/benchmark_runs/*/text/), SM.fr (the Standard
Model file a FeynRules add-on model is loaded on top of), and MODEL_PATH, a JSON list of the NEW fields and of
the interaction vertices (by particle content) that an implementation of the paper's model must have.

Read the paper's model-defining sections. Report:
- every new field of the paper's model that is not in "fields";
- every interaction term of the paper's Lagrangian whose particle content is not in "interactions" (name the
  equation; give the particles);
- every entry of the list that the paper does not have.
Kinetic and mass terms need no entry. Gauge interactions of a new charged or coloured field DO need one
(for example a coloured scalar with the gluon). Do not comment on names or format.
Output a numbered list, each item with the paper equation or LaTeX line. End with one line:
VERDICT: COMPLETE, or VERDICT: <n> MISSING, <m> EXTRA."""  # noqa: E501


def review_spec(args: dict) -> str:
    """The referee on spec.json, once, before the model is written: it is easier to see
    what a short list leaves out than what a long model file leaves out."""
    rd = C.rundir()
    st = C.load_state(rd)
    if st.get("spec_reviews", 0) >= 1:
        raise ToolError("review_spec budget exhausted (1 call)")
    spec = _path(args.get("path", "spec.json"))
    st["spec_reviews"] = 1
    C.save_state(rd, st)
    text = _referee(rd, spec, "spec_review1", SPEC_REVIEW_PROMPT, "spec_under_review.json")
    return "review of spec.json\n\n" + text


HANDLERS = {
    "lint_model": lint_model,
    "validate_model": validate_model,
    "massbasis": massbasis,
    "review_model": review_model,
    "review_spec": review_spec,
}


def _tool_list() -> list:
    vb = C.env_int("CC_VALIDATE_BUDGET", 10)
    rb = C.env_int("CC_REVIEW_BUDGET", 2)
    arm = C.arm()
    out = []
    for t in TOOL_SPECS:
        if t["name"] not in arm.tools:
            continue
        t = dict(t)
        t["description"] = (
            t["description"]
            .replace("{validate_description}", VALIDATE_DESCRIPTIONS.get(arm.feedback, ""))
            .replace("{budget}", str(vb))
            .replace("{review_budget}", str(rb))
        )
        out.append(t)
    return out


def call_tool(name: str, arguments: dict) -> dict:
    rd = C.rundir()
    C.log(rd, "tool_calls.jsonl", {"event": "call", "tool": name, "input": arguments})
    t0 = time.time()
    try:
        if name not in HANDLERS or name not in C.arm().tools:
            raise ToolError(f"unknown tool {name}")
        text = HANDLERS[name](arguments)
        C.log(
            rd,
            "tool_calls.jsonl",
            {
                "event": "result",
                "tool": name,
                "seconds": round(time.time() - t0, 1),
                "head": text[:400],
            },
        )
        return {"content": [{"type": "text", "text": text}], "isError": False}
    except (ToolError, subprocess.TimeoutExpired) as e:
        C.log(rd, "tool_calls.jsonl", {"event": "error", "tool": name, "error": str(e)[:800]})
        return {"content": [{"type": "text", "text": f"error: {e}"}], "isError": True}


def handle(msg: dict) -> dict | None:
    method, mid = msg.get("method"), msg.get("id")
    if mid is None:  # a notification: no response
        return None
    if method == "initialize":
        pv = (msg.get("params") or {}).get("protocolVersion") or PROTOCOL_VERSION
        res = {
            "protocolVersion": pv,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": C.SERVER_NAME, "version": "1.0"},
        }
    elif method == "tools/list":
        res = {"tools": _tool_list()}
    elif method == "tools/call":
        p = msg.get("params") or {}
        res = call_tool(p.get("name"), p.get("arguments") or {})
    elif method == "ping":
        res = {}
    else:
        return {
            "jsonrpc": "2.0",
            "id": mid,
            "error": {"code": -32601, "message": f"method not found: {method}"},
        }
    return {"jsonrpc": "2.0", "id": mid, "result": res}


def main() -> int:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        resp = handle(msg)
        if resp is not None:
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
