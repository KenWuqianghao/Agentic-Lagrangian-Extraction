#!/usr/bin/env python3
"""Toolkit vs bare harness on open-weights models, through the opencode harness.

The same 16 single-model papers, the same v3 physics rules and the same
corrected FeynRules -> UFO -> MadGraph chain as ABLATION_2026-09-17, but the
agent is an open-weights model driven by opencode (MIT, github.com/sst/opencode)
instead of Claude Code. Three arms, identical except for the toolkit:

  hand     the agent reads the paper and SM.fr in its sandbox and writes the
           complete model.fr itself. No shell.
  toolkit  the agent writes the FeynRulesModel JSON (spec.json) and may run
           ONE shell command, ``./frgen spec.json``: schema validation, the
           deterministic renderer, and the deterministic lints. It iterates
           on that feedback. The harness re-renders the final spec.json.
  toolkit2 the toolkit arm with the five gaps of OPEN_MODELS_2026-09-24 closed:
           the schema checks mass/width values, bracket balance, External
           block collisions and charged self-conjugate fields, and an opencode
           plugin (frgen_hook.js) runs ./frgen after every change to spec.json
           and appends the report to that tool result.

No arm has Wolfram, MadGraph, the web or anything outside its sandbox.
Validation runs afterwards, serially, in the harness (``validate``).

    open_bench.py prepare  --model nemotron --arm hand --pages all
    open_bench.py run      --model nemotron --arm hand --pages all --jobs 4
    open_bench.py validate --model nemotron --arm hand --pages all
    open_bench.py reaudit  --model nemotron --arm hand --pages all
    report.py

Outputs per run: benchmarks/<page>/rerun/v3o_<model>_<arm>/s<seed>/
    TASK.md  agent_stream.jsonl  agent_out.md  agent_stderr.txt
    model/<page>_gen.fr  spec.json (toolkit)  audit.json  run.json
    validation.json  predicates.json
"""

from __future__ import annotations

import argparse
import functools
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
BENCH = HERE.parent
PAPERS = Path.home() / "Documents/Github/heptapod/eval/benchmark_runs"
HD = Path(os.environ.get("OB_HD", ""))  # heptapod-dev origin/main worktree
VENV_PY = Path(os.environ.get("OB_PY", ""))  # python with pydantic + jinja2
OC_HOME = Path(os.environ.get("OB_OC_HOME", ""))  # isolated HOME for opencode
OPENCODE = Path.home() / ".opencode/bin/opencode"
AGENT_TIMEOUT = int(os.environ.get("OB_AGENT_TIMEOUT", "3600"))

MODELS = {
    "nemotron": "opencode/nemotron-3-ultra-free",
    "mimo": "opencode/mimo-v2.6-flash-free",
}
# Output budget per step, both arms. opencode caps every model at 32k by default and
# the catalog lists MiMo at 32k, but its reasoning alone filled 32k before the first
# write; the endpoint served a 95.7k-token step when asked, so both models get 128k.
OUTPUT_MAX = 128000
MODEL_LIMITS = {"mimo": {"context": 200000, "output": OUTPUT_MAX}}
MAX_NUDGES = int(os.environ.get("OB_MAX_NUDGES", "3"))
TOOLKIT_ARMS = ("toolkit", "toolkit2")
NUDGE = {
    "hand": (
        "You stopped before model.fr exists in the current directory. Write the complete "
        ".fr file to model.fr now with your file-writing tool. If it is long, write a first "
        "part and then append the rest with the edit tool."
    ),
    "toolkit": (
        "You stopped before spec.json exists in the current directory. Write the "
        "FeynRulesModel JSON to spec.json now with your file-writing tool, then run "
        "`./frgen spec.json` and fix what it reports."
    ),
}
PAGES16 = [
    "331",
    "ALRM_general",
    "B-L-SM",
    "ChernSimonsPortal",
    "EffLRSM",
    "GeneralU1",
    "HeavyN",
    "MDMmodel",
    "Monotops",
    "NJLComposite",
    "SLQrules",
    "SMWeinberg",
    "Top-Philic-Zprime",
    "Wprime",
    "pNG",
    "pSPSS",
]

USER_MSG = (
    "Your task is in the file TASK.md in the current directory. Read all of it first "
    "(it is long; read it to the end), then do exactly what it says. Work only inside "
    "the current directory."
)

SANDBOX_NOTE = {
    "hand": """\
SANDBOX: the current directory contains ONLY the paper ({paper}), SM.fr (the Standard
Model file this add-on is loaded on top of: take field names, index conventions and
hypercharges from it) and this TASK.md. Nothing else exists here and nothing outside this
directory may be read. You have file read, search and write tools. You have NO shell, no
web, no FeynRules, no Mathematica and no MadGraph.""",
    "toolkit": """\
SANDBOX: the current directory contains ONLY the paper ({paper}), SM.fr (the Standard
Model file this add-on is loaded on top of: take field names, index conventions and
hypercharges from it), the schema tools/frgen/frmodel.py, the renderer
tools/frgen/render.py, the lints tools/fr_lint.py and the command ./frgen. Nothing else
exists here and nothing outside this directory may be read. You have file read, search and
write tools, and ONE shell command: `./frgen spec.json`. No other shell command, no web,
no FeynRules, no Mathematica and no MadGraph.

TOOLKIT: `./frgen spec.json` (1) validates spec.json against the FeynRulesModel schema and
prints every schema error, (2) renders model.fr with the deterministic renderer, and (3)
lints model.fr with deterministic rules, each tagged with the stage it predicts will fail.
Run it after you write spec.json, fix what it reports, and run it again until the schema
is OK and every remaining lint finding is one you have checked and judged harmless.""",
}

OUTPUT_LINE = {
    "hand": (
        "OUTPUT: write the complete .fr file to model.fr in the current directory with "
        'your file-writing tool (ONLY the .fr content). Set M$ModelName = "{page}_gen". '
        "Your final message: the self-audit table and one line saying model.fr is written. "
        "model.fr as it is on disk when you stop is what gets scored."
    ),
    "toolkit": (
        "OUTPUT: write the FeynRulesModel JSON object to spec.json in the current "
        "directory with your file-writing tool (ONLY the JSON). Set model_name to "
        '"{page}_gen". Run `./frgen spec.json` and iterate as described under TOOLKIT. '
        "Your final message: the self-audit table and one line with the last ./frgen "
        "result. spec.json as it is on disk when you stop is rendered and scored."
    ),
}


def _sub_once(text: str, pattern: str, repl: str, what: str) -> str:
    new, n = re.subn(pattern, lambda _m: repl, text, count=1, flags=re.M)
    if n != 1:
        raise ValueError(f"prompt template: no unique {what} line")
    return new


def paper_file(page: str) -> Path:
    texs = sorted((PAPERS / page / "text").glob("*_source.tex"))
    if not texs:
        raise FileNotFoundError(f"no LaTeX source for {page}")
    return texs[0]


def variant(model: str, arm: str) -> str:
    return f"v3o_{model}_{arm}"


def rundir(page: str, model: str, arm: str, seed: int) -> Path:
    return BENCH / page / "rerun" / variant(model, arm) / f"s{seed}"


AUTO_CHECK_NOTE = """\
AUTOMATIC CHECK: after every write or edit of spec.json the toolkit runs by itself and
its report is appended to that tool's result. Read it after each change and fix what it
reports. You may still run `./frgen spec.json` yourself."""


def build_task(page: str, arm: str, paper_name: str) -> str:
    """The v3s prompt of the same arm type, with the documents moved into the sandbox."""
    paper_rel = f"paper/{paper_name}"
    if arm == "hand":
        src = (BENCH / page / "rerun/v3s_notools/s1/prompt.txt").read_text()
        i = src.index("===== END PAPER =====")
        t = src[i + len("===== END PAPER =====") :].lstrip()
        t = _sub_once(
            t,
            r"^PAPER: .*$",
            f'PAPER: the paper\'s LaTeX source is the file "{paper_rel}" (read it '
            "completely with your file-reading tool; equations, fractions and roots "
            "are exact; it is authoritative).",
            "PAPER",
        )
        t = t.replace(
            "It is loaded on top of SM.fr, included verbatim above between the SM.fr markers.",
            "It is loaded on top of SM.fr, the file SM.fr in the current directory.",
        )
        t = _sub_once(t, r"^OUTPUT: .*$", OUTPUT_LINE["hand"].format(page=page), "OUTPUT")
        t = re.sub(
            r"NO TOOLS: this run has no file.*?write the model\.\n",
            SANDBOX_NOTE["hand"].format(paper=paper_rel) + "\n",
            t,
            count=1,
            flags=re.S,
        )
        if "NO TOOLS" in t or "SANDBOX:" not in t:
            raise ValueError("hand prompt: NO TOOLS note not replaced")
        return t
    src = (BENCH / page / "rerun/v3s_tools/s1/prompt.txt").read_text()
    t = _sub_once(
        src,
        r"^PAPER: .*$",
        f'PAPER: the paper\'s LaTeX source is the file "{paper_rel}" (read it '
        "completely with your file-reading tool; equations, fractions and roots are "
        "exact; it is authoritative).",
        "PAPER",
    )
    t = _sub_once(
        t,
        r"^SCHEMA: .*$",
        "SCHEMA: read tools/frgen/frmodel.py (pydantic FeynRulesModel) before you write the spec.",
        "SCHEMA",
    )
    t = _sub_once(t, r"^OUTPUT: .*$", OUTPUT_LINE["toolkit"].format(page=page), "OUTPUT")
    t = re.sub(
        r"SANDBOX: the sandbox root is .*?may be read\.\n",
        SANDBOX_NOTE["toolkit"].format(paper=paper_rel) + "\n",
        t,
        count=1,
        flags=re.S,
    )
    if "sandbox root is" in t or "TOOLKIT:" not in t:
        raise ValueError("toolkit prompt: SANDBOX note not replaced")
    if arm == "toolkit2":
        t = t.replace(
            SANDBOX_NOTE["toolkit"].format(paper=paper_rel),
            SANDBOX_NOTE["toolkit"].format(paper=paper_rel) + "\n\n" + AUTO_CHECK_NOTE,
            1,
        )
        if "AUTOMATIC CHECK" not in t:
            raise ValueError("toolkit2 prompt: AUTOMATIC CHECK note not added")
    return t


def oc_config(arm: str, model: str) -> dict:
    # The same permissions in every arm. The free tier answers 403 to a request whose tool
    # list lacks bash, and a blanket "deny" drops bash from the list, so bash stays
    # listed with one allowed command. The hand sandbox has no ./frgen, so there the
    # command only prints "no such file". Denied calls return an error and the run goes on.
    bash = {"*": "deny", "./frgen *": "allow", "./frgen": "allow"}
    cfg = {
        "$schema": "https://opencode.ai/config.json",
        "autoupdate": False,
        "share": "disabled",
        "mcp": {},
        "plugin": [],
        "instructions": [],
        "tools": {
            "webfetch": False,
            "websearch": False,
            "codesearch": False,
            "task": False,
            "skill": False,
        },
        "permission": {
            "bash": bash,
            "webfetch": "deny",
            "websearch": "deny",
            "external_directory": "deny",
            "doom_loop": "allow",
            "edit": {
                "*": "allow",
                "frgen": "deny",
                "tools/*": "deny",
                "paper/*": "deny",
                "SM.fr": "deny",
                "TASK.md": "deny",
            },
        },
    }
    if arm == "toolkit2":
        cfg["plugin"] = [f"file://{HERE / 'frgen_hook.js'}"]
    if model in MODEL_LIMITS:
        cfg["provider"] = {
            "opencode": {"models": {MODELS[model].split("/", 1)[1]: {"limit": MODEL_LIMITS[model]}}}
        }
    return cfg


def _install_toolkit(root: Path) -> None:
    """Copy the frgen schema, renderer, template and fr_lint.py to root/."""
    fg = root / "frgen"
    (fg / "templates").mkdir(parents=True)
    for f in ("frmodel.py", "render.py"):
        shutil.copy2(HD / "tools/frgen" / f, fg / f)
    shutil.copy2(HD / "tools/frgen/templates/model.fr.j2", fg / "templates/model.fr.j2")
    (fg / "__init__.py").write_text("")
    shutil.copy2(BENCH / "fr_lint.py", root / "fr_lint.py")


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else ""


def prepare_one(page: str, model: str, arm: str, seed: int, force: bool) -> None:
    rd = rundir(page, model, arm, seed)
    if (rd / "run.json").is_file() and not force:
        print(f"[prepare] skip {page} {variant(model, arm)} s{seed}: run.json exists")
        return
    if rd.exists():
        shutil.rmtree(rd)
    rd.mkdir(parents=True)
    paper = paper_file(page)
    sb = Path(tempfile.mkdtemp(prefix=f"ob-{page}-"))
    (sb / "paper").mkdir()
    shutil.copy2(paper, sb / "paper" / paper.name)
    shutil.copy2(HD / "tools/feynrules/test_files/models/SM.fr", sb / "SM.fr")
    if arm in TOOLKIT_ARMS:
        _install_toolkit(sb / "tools")
        wrapper = sb / "frgen"
        wrapper.write_text(
            "#!/bin/sh\n"
            f'FRGEN_TOOLKIT="$(pwd)/tools" exec "{VENV_PY}" "{HERE / "frgen_cli.py"}" "$@"\n'
        )
        wrapper.chmod(0o555)
    task = build_task(page, arm, paper.name)
    (sb / "TASK.md").write_text(task)
    (rd / "TASK.md").write_text(task)
    (rd / "sandbox_path.txt").write_text(str(sb))
    hashes = {str(p.relative_to(sb)): _sha(p) for p in sb.rglob("*") if p.is_file()}
    (rd / "sandbox_hashes.json").write_text(json.dumps(hashes, indent=1))


def _events(path: Path) -> list[dict]:
    out = []
    for line in path.read_text(errors="replace").splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def _tool_calls(events: list[dict]) -> list[dict]:
    calls = []
    for ev in events:
        part = ev.get("part") or {}
        if ev.get("type") == "tool_use" or part.get("type") == "tool":
            st = part.get("state") or {}
            calls.append(
                {
                    "tool": part.get("tool"),
                    "input": st.get("input"),
                    "status": st.get("status"),
                    "output": (st.get("output") or st.get("error") or "")[:400],
                }
            )
    return calls


def _final_text(events: list[dict]) -> str:
    texts = [
        (ev.get("part") or {}).get("text", "")
        for ev in events
        if (ev.get("part") or {}).get("type") == "text"
    ]
    return texts[-1] if texts else ""


def audit(calls: list[dict], sb: Path, arm: str, paper_name: str) -> dict:
    sbs = str(sb.resolve())
    escapes, forbidden, denied, read_paper, frgen_runs = [], [], [], False, 0
    allowed = {
        "read",
        "write",
        "edit",
        "glob",
        "grep",
        "list",
        "todowrite",
        "todoread",
        "patch",
        "multiedit",
        "apply_patch",
        "invalid",
        "bash",
    }
    for c in calls:
        tool, inp = c["tool"] or "", c["input"] or {}
        if c["status"] != "completed":
            if "prevents you from using" in c["output"] or "rejected" in c["output"]:
                denied.append(f"{tool}:{json.dumps(inp)[:80]}")
            continue
        if tool not in allowed:
            forbidden.append(tool)
        # Paths only from the path-like arguments: file contents may quote anything.
        blob = json.dumps(
            {
                k: v
                for k, v in inp.items()
                if k in ("filePath", "path", "pattern", "include", "workdir", "command")
            }
        )
        for m in re.findall(r'(/(?:Users|private|var|tmp|etc|opt|home)[^"\s\\]*)', blob):
            if not str(Path(m).resolve()).startswith(sbs):
                escapes.append(m)
        if "reference_cache" in blob:
            escapes.append("reference_cache")
        if tool == "read" and paper_name in blob:
            read_paper = True
        if tool == "bash":
            cmd = (inp.get("command") or "").strip()
            if re.fullmatch(r"\./frgen( +\S+)?", cmd):
                frgen_runs += 1 if arm in TOOLKIT_ARMS else 0
            else:
                forbidden.append(f"bash:{cmd[:80]}")
    return {
        "tool_calls": len(calls),
        "read_paper": read_paper,
        "escapes": sorted(set(escapes)),
        "forbidden": forbidden,
        "denied_attempts": denied,
        "frgen_runs": frgen_runs,
        "contaminated": bool(escapes),
        "audit_ok": not escapes and not forbidden,
    }


RATE_LIMIT = re.compile(r'"statusCode":\s*429|Rate limit exceeded')


def _run_watched(cmd, sb, env, out, err, left, stream: Path):
    """Run opencode; stop it at the first rate-limit error in its stream.

    On a spent free-tier quota opencode retries the 429 for the whole hour and
    writes nothing, so the run measures the quota, not the model. Returns
    (exit code, timed out, rate limited)."""
    p = subprocess.Popen(cmd, cwd=sb, env=env, stdout=out, stderr=err, stdin=subprocess.DEVNULL)
    t_end = time.time() + left
    while True:
        try:
            return p.wait(timeout=10), False, False
        except subprocess.TimeoutExpired:
            pass
        if RATE_LIMIT.search(stream.read_text(errors="replace")):
            p.terminate()
            p.wait()
            return p.returncode, False, True
        if time.time() > t_end:
            p.terminate()
            p.wait()
            return None, True, False


def run_one(page: str, model: str, arm: str, seed: int) -> dict:
    rd = rundir(page, model, arm, seed)
    sb = Path((rd / "sandbox_path.txt").read_text().strip())
    env = {
        k: v for k, v in os.environ.items() if not k.startswith(("ANTHROPIC", "OPENAI", "CLAUDE"))
    }
    env.update(
        {
            "PWD": str(sb),
            "HOME": str(OC_HOME),
            "XDG_CONFIG_HOME": str(OC_HOME / ".config"),
            "XDG_DATA_HOME": str(OC_HOME / ".local/share"),
            "XDG_CACHE_HOME": str(OC_HOME / ".cache"),
            "OPENCODE_CONFIG_CONTENT": json.dumps(oc_config(arm, model)),
            "OPENCODE_DISABLE_CLAUDE_CODE": "1",
            "OPENCODE_DISABLE_EXTERNAL_SKILLS": "1",
            "OPENCODE_DISABLE_PROJECT_CONFIG": "1",
            "OPENCODE_DISABLE_AUTOUPDATE": "1",
            "OPENCODE_DISABLE_SHARE": "1",
            "OPENCODE_DISABLE_LSP_DOWNLOAD": "1",
            "OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX": str(OUTPUT_MAX),
            "FRGEN_HOOK_LOG": str(rd / "hook_log.jsonl"),
        }
    )
    # Default plugins stay on: without them the free tier answers 403
    # "OpenCode's free tier can only be used from within OpenCode".
    # --dir and PWD both: opencode takes its project directory from PWD, not from the
    # process cwd, and a stale PWD pointed the first smoke run at the repo.
    # --pure blocks every non-default plugin, the toolkit2 hook included; the
    # isolated HOME and config list no other plugin, so dropping it adds only ours.
    pure = [] if arm == "toolkit2" else ["--pure"]
    base = [str(OPENCODE), "run", *pure, "--format", "json", "--dir", str(sb), "-m", MODELS[model]]
    deliverable = sb / ("model.fr" if arm == "hand" else "spec.json")
    t0 = time.time()
    rc, timed_out, nudges, rate_limited = None, False, 0, False
    with open(rd / "agent_stream.jsonl", "w") as out, open(rd / "agent_stderr.txt", "w") as err:
        cmd = base + ["--title", f"{variant(model, arm)}/{page}/s{seed}", USER_MSG]
        while True:
            left = AGENT_TIMEOUT - (time.time() - t0)
            if left <= 0:
                timed_out = True
                break
            rc, timed_out, rate_limited = _run_watched(
                cmd, sb, env, out, err, left, rd / "agent_stream.jsonl"
            )
            if timed_out or rate_limited:
                break
            if deliverable.is_file() or nudges >= MAX_NUDGES:
                break
            sid = next(
                (
                    e.get("sessionID")
                    for e in _events(rd / "agent_stream.jsonl")
                    if e.get("sessionID")
                ),
                None,
            )
            if not sid:
                break
            # Same session, same nudge in both arms: the run stopped (output cap, or the
            # model ended its turn) before the deliverable existed.
            nudges += 1
            cmd = base + ["--session", sid, NUDGE["hand" if arm == "hand" else "toolkit"]]
    secs = round(time.time() - t0, 1)
    events = _events(rd / "agent_stream.jsonl")
    calls = _tool_calls(events)
    final = _final_text(events)
    (rd / "agent_out.md").write_text(final)
    (rd / "tool_calls.json").write_text(json.dumps(calls, indent=1))
    paper_name = paper_file(page).name
    au = audit(calls, sb, arm, paper_name)
    before = json.loads((rd / "sandbox_hashes.json").read_text())
    au["tampered"] = sorted(k for k, h in before.items() if _sha(sb / k) != h)
    au["audit_ok"] = au["audit_ok"] and not au["tampered"]
    (rd / "audit.json").write_text(json.dumps(au, indent=1))
    tokens = {"input": 0, "output": 0, "reasoning": 0}
    stops = [
        ((ev.get("part") or {}).get("reason"))
        for ev in events
        if (ev.get("part") or {}).get("type") == "step-finish"
    ]
    for ev in events:
        tk = (ev.get("part") or {}).get("tokens") or {}
        for k in tokens:
            tokens[k] += int(tk.get(k) or 0)
    fr = produce_fr(page, arm, rd, sb, final)
    row = {
        "page": page,
        "model": model,
        "model_id": MODELS[model],
        "arm": arm,
        "seed": seed,
        "variant": variant(model, arm),
        "harness": "opencode " + oc_version(),
        "exit": rc,
        "timed_out": timed_out,
        "nudges": nudges,
        "seconds": secs,
        "tokens": tokens,
        "rate_limited": rate_limited
        or bool(RATE_LIMIT.search((rd / "agent_stream.jsonl").read_text(errors="replace"))),
        "output_max": OUTPUT_MAX,
        "hook_runs": (
            sum(1 for _ in open(rd / "hook_log.jsonl")) if (rd / "hook_log.jsonl").is_file() else 0
        ),
        "n_events": len(events),
        "length_stops": stops.count("length"),
        "audit": au,
        **fr,
    }
    (rd / "run.json").write_text(json.dumps(row, indent=1))
    print(
        f"[run] {page} {variant(model, arm)} s{seed}: {secs}s rc={rc} nudges={nudges} "
        f"rate_limited={row['rate_limited']} "
        f"length_stops={stops.count('length')} calls={au['tool_calls']} "
        f"frgen={au['frgen_runs']} hook={row['hook_runs']} fr={fr.get('rendered')} "
        f"({fr.get('reason', '')}) "
        f"audit_ok={au['audit_ok']}",
        flush=True,
    )
    return row


@functools.cache
def oc_version() -> str:
    return subprocess.run(
        [str(OPENCODE), "--version"], capture_output=True, text=True
    ).stdout.strip()


_FENCE_RE = re.compile(r"```[ \t]*([A-Za-z0-9_+-]*)[ \t]*\n(.*?)```", re.S)


def produce_fr(page: str, arm: str, rd: Path, sb: Path, final: str) -> dict:
    """The scored .fr: hand = model.fr on disk; toolkit = spec.json re-rendered by the
    harness. Fallback for both: the last matching fenced block of the final message."""
    dst = rd / "model" / f"{page}_gen.fr"
    dst.parent.mkdir(exist_ok=True)
    if arm == "hand":
        src = sb / "model.fr"
        if src.is_file() and src.stat().st_size > 0:
            shutil.copy2(src, dst)
            return {"rendered": True, "source": "model.fr", "fr": str(dst)}
        blocks = [b for _t, b in _FENCE_RE.findall(final) if "M$ClassesDescription" in b]
        if blocks:
            dst.write_text(blocks[-1].rstrip() + "\n")
            return {"rendered": True, "source": "final_message", "fr": str(dst)}
        return {"rendered": False, "reason": "no_model_fr"}
    spec = sb / "spec.json"
    source = "spec.json"
    if not (spec.is_file() and spec.stat().st_size > 0):
        blocks = [
            b for t, b in _FENCE_RE.findall(final) if t.lower() == "json" or '"particles"' in b
        ]
        if not blocks:
            return {"rendered": False, "reason": "no_spec"}
        spec = rd / "spec_from_message.json"
        spec.write_text(blocks[-1])
        source = "final_message"
    else:
        shutil.copy2(spec, rd / "spec.json")
    work = rd / "render"
    work.mkdir(exist_ok=True)
    shutil.copy2(spec, work / "spec.json")
    # Render with the pristine toolkit copy, not the sandbox's (tamper-proof).
    pristine = rd / "toolkit"
    if not pristine.exists():
        _install_toolkit(pristine)
    p = subprocess.run(
        [str(VENV_PY), str(HERE / "frgen_cli.py"), str(work / "spec.json")],
        capture_output=True,
        text=True,
        env=dict(os.environ, FRGEN_TOOLKIT=str(pristine)),
    )
    (rd / "render_log.txt").write_text(p.stdout + p.stderr)
    shutil.rmtree(pristine)
    if (work / "model.fr").is_file():
        shutil.copy2(work / "model.fr", dst)
        return {
            "rendered": True,
            "source": source,
            "fr": str(dst),
            "final_lint_findings": p.stdout.count("\n- ["),
        }
    reason = (
        "schema_validation_failed" if "SCHEMA VALIDATION FAILED" in p.stdout else "render_failed"
    )
    return {"rendered": False, "reason": reason, "source": source, "detail": p.stdout[:800]}


def validate_one(page: str, model: str, arm: str, seed: int) -> dict:
    rd = rundir(page, model, arm, seed)
    run = json.loads((rd / "run.json").read_text())
    if (rd / "validation.json").is_file():
        return json.loads((rd / "validation.json").read_text())
    if not run.get("rendered"):
        val = {"status": "not_rendered", "full_chain_pass": False}
        (rd / "validation.json").write_text(json.dumps(val, indent=1))
        return val
    fr = rd / "model" / f"{page}_gen.fr"
    tag = f"open/{variant(model, arm)}/{page}/s{seed}"
    out = Path(os.environ.get("VBENCH_OUT", "/tmp/rerun_bench"))
    env = dict(os.environ, VBENCH_OUT=str(out), VBENCH_COMPILE_TIMEOUT="900")
    while subprocess.run(["pgrep", "-f", "[W]olframKernel"], capture_output=True).returncode == 0:
        time.sleep(20)  # another session's compile: one kernel at a time
    t0 = time.time()
    p = subprocess.run(
        [sys.executable, str(HD / "eval/benchmark_runs/run_one_fr.py"), page, str(fr), tag],
        cwd=HD,
        env=env,
        capture_output=True,
        text=True,
    )
    res = out / tag / "result.json"
    if not res.is_file():
        val = {"status": "harness_error", "stderr": p.stderr[-2000:], "full_chain_pass": False}
    else:
        val = json.loads(res.read_text())
    for log in ("compile.log", "checks.log"):
        src = out / tag / log
        if src.is_file():
            shutil.copy2(src, rd / log)
    val["wall_seconds"] = round(time.time() - t0, 1)
    (rd / "validation.json").write_text(json.dumps(val, indent=1, default=str))
    try:
        sys.path.insert(0, str(BENCH))
        import rerun_predicates

        checks = rerun_predicates.PREDICATES.get(page, [])
        txt = fr.read_text(errors="replace")
        pr = {"available": True, "results": {}}
        for name, fn in checks:
            ok, detail = fn(txt)
            pr["results"][name] = {"resolved": bool(ok), "detail": detail}
        pr["all_resolved"] = bool(checks) and all(r["resolved"] for r in pr["results"].values())
        (rd / "predicates.json").write_text(json.dumps(pr, indent=1))
    except Exception as e:  # noqa: BLE001
        (rd / "predicates.json").write_text(json.dumps({"available": False, "error": str(e)}))
    print(
        f"[validate] {page} {variant(model, arm)} s{seed}: {val.get('status')} "
        f"checks={val.get('checks')} mg5={val.get('madgraph_import_ok')} "
        f"full={val.get('full_chain_pass')} ({val['wall_seconds']}s)",
        flush=True,
    )
    return val


def _pages(s: str) -> list[str]:
    return PAGES16 if s == "all" else [p for p in s.split(",") if p]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["prepare", "run", "validate", "reaudit"])
    ap.add_argument("--model", choices=sorted(MODELS), required=True)
    ap.add_argument("--arm", choices=["hand", "toolkit", "toolkit2"], required=True)
    ap.add_argument("--pages", default="all")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    pages = _pages(a.pages)
    if a.cmd == "prepare":
        for p in pages:
            prepare_one(p, a.model, a.arm, a.seed, a.force)
    elif a.cmd == "run":
        todo = [
            p
            for p in pages
            if not (rundir(p, a.model, a.arm, a.seed) / "run.json").is_file()
            and (rundir(p, a.model, a.arm, a.seed) / "sandbox_path.txt").is_file()
        ]

        def _go(ip):
            time.sleep(3 * (ip[0] % a.jobs))  # stagger starts: opencode's sqlite setup races
            return run_one(ip[1], a.model, a.arm, a.seed)

        with ThreadPoolExecutor(a.jobs) as ex:
            list(ex.map(_go, enumerate(todo)))
    elif a.cmd == "reaudit":
        for p in pages:
            rd = rundir(p, a.model, a.arm, a.seed)
            if not (rd / "run.json").is_file():
                continue
            sb = Path((rd / "sandbox_path.txt").read_text().strip())
            au = audit(
                json.loads((rd / "tool_calls.json").read_text()), sb, a.arm, paper_file(p).name
            )
            au["tampered"] = json.loads((rd / "audit.json").read_text()).get("tampered", [])
            au["audit_ok"] = au["audit_ok"] and not au["tampered"]
            (rd / "audit.json").write_text(json.dumps(au, indent=1))
            run = json.loads((rd / "run.json").read_text())
            run["audit"] = au
            (rd / "run.json").write_text(json.dumps(run, indent=1))
            print(
                f"[reaudit] {p} {variant(a.model, a.arm)}: ok={au['audit_ok']} "
                f"forbidden={au['forbidden']} denied={len(au['denied_attempts'])}"
            )
    else:
        for p in pages:  # serial: one Wolfram kernel at a time
            if (rundir(p, a.model, a.arm, a.seed) / "run.json").is_file():
                validate_one(p, a.model, a.arm, a.seed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
