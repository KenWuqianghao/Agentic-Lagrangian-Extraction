#!/usr/bin/env python3
"""
# repair_subagent.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

The repair loop of repair_benchmark.py, driven round by round through Claude
Code subagents instead of a headless agent CLI.

Why: on 2026-09-17 both headless CLIs on the benchmark machine were logged
out, and only a human can log them in. An interactive Claude Code session can
still spawn subagents. So each round is split in three: this script prepares
every failing model's workdir and writes a manifest; the session spawns one
subagent per manifest entry; this script reads the transcripts back, audits
them, and re-validates. Validation stays serial, because Wolfram is.

The loop is the same as repair_benchmark.run_page, unrolled by round so that
all agents of one round run in parallel while Wolfram is idle. The report has
the same shape, so repair_summary.py and build_ian_bundle.py read it.

    python repair_subagent.py init    --subdir repair_corrected --pages A,B
    python repair_subagent.py prepare --subdir repair_corrected --round 1
      -> repair_manifest_<subdir>_r1.json, one entry per model still failing
    (spawn one subagent per entry, model claude-sonnet-5, prompt = user_prompt)
    python repair_subagent.py ingest  --subdir repair_corrected --round 1 \
        --transcripts-dir ~/.claude/projects/<proj>/<session>/subagents
      -> audits, re-validates, writes repair_<subdir>_report.{json,md}
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent))

os.environ.setdefault("VBENCH_OUT", "/tmp/repair_corrected")
import repair_benchmark as rb  # noqa: E402
import subagent_bench as sb  # noqa: E402

ENGINE = "claude-code-subagent"
ALLOWED = {"Read", "Grep", "Glob", "Edit", "Write", "MultiEdit"}

# repair_benchmark.REPAIR_PROMPT names the three checks the old harness
# parsed. The corrected harness runs FeynRules' four default checks and reads
# their return values, so the agent is told exactly those.
PROMPT = """\
RUN-TAG: {tag}

Your working directory for this task is {workdir}. Work ONLY there. Tool policy: \
Read, Grep, Glob, Edit, Write and MultiEdit, and only on files under {workdir}. \
No shell, no web, no other directories, no reference files. The directory contains:
  - model.fr              : a FeynRules model file that FAILS the validation tool chain
  - VALIDATION_REPORT.md  : the exact failing output (FeynRules under Wolfram Engine, then MadGraph)
  - REPAIR_HISTORY.md     : (if present) previous repair attempts on this model and the
    validation outcome after each one. Do NOT repeat an approach that already failed;
    if a previous edit made the outcome worse (e.g. introduced a compile timeout),
    prefer reverting that change.
  - UFO/                  : (if present) the UFO the failing tool chain generated FROM
    this model.fr. Inspect it to diagnose MadGraph import failures. Never edit UFO/ files;
    the UFO is regenerated from model.fr each round. Fix the CAUSE in model.fr.

Fix model.fr IN PLACE so the tool chain passes:
  1. FeynRules WriteUFO produces a complete UFO (no $Aborted, no syntax errors, no
     undefined Lagrangian symbol);
  2. the four FeynRules consistency checks pass, read from their return values:
     CheckHermiticity (L - HC[L] has no vertices), CheckDiagonalKineticTerms,
     CheckDiagonalMassTerms, and CheckMassSpectrum (the masses computed from the
     Lagrangian agree with the declared Mass values). An inconclusive mass spectrum
     almost always means the mass terms are not diagonal: fix that first.
  3. MadGraph `import model` of the generated UFO succeeds.

Hard rules:
  - Preserve the physics content: keep the fields, their quantum numbers, the operator
    structure, and parameter values. Fix TECHNICAL defects only, e.g.: FeynRules or
    Mathematica syntax errors; class/parameter names that collide with Mathematica
    built-ins (never use N, C, D, E, I, K, O as a ClassName or parameter); symbols used
    before they are defined; malformed class or parameter declarations; wrong or missing
    index declarations; a non-Hermitian Lagrangian missing its `+ HC[...]` conjugate (or
    double-counting one); mass terms that mix fields which are declared as separate mass
    eigenstates (rotate to the mass basis, or declare the mixing); a declared Mass that
    does not match the mass term; self-conjugate (Majorana/real) fields declared with
    quantum numbers; duplicate ParticleName/AntiParticleName entries; mixing declarations
    whose identifier is not a string.
  - The total Lagrangian must be the LAST top-level assignment in the file, of the form
    `LTot := Lterm1 + Lterm2 + ...;`, built only from symbols defined above it. It is the
    BSM piece only: the tool chain adds the Standard Model Lagrangian LSM itself, unless
    your total already contains LSM.
  - Do not add particle Decay declarations.
  - If a check failure is inherently physical (e.g. Hermiticity genuinely violated by a
    term as extracted), make the minimal correction that restores consistency and note it.

When done, write a one-paragraph summary of exactly what you changed and why as your
final message.
"""


def _state_path(subdir: str) -> Path:
    return HERE / f"repair_state_{subdir}.json"


def _reports(subdir: str) -> tuple[Path, Path]:
    return HERE / f"repair_{subdir}_report.json", HERE / f"repair_{subdir}_report.md"


def _load(subdir: str) -> dict:
    return json.loads(_state_path(subdir).read_text())


def _save(subdir: str, state: dict) -> None:
    _state_path(subdir).write_text(json.dumps(state, indent=1, default=str))
    jp, mp = _reports(subdir)
    # write_reports expects a final status on every model; a model still in
    # the loop gets a placeholder in the interim report only.
    rows = [r if r.get("final_status") else {**r, "final_status": "in_progress"}
            for r in state["results"]]
    rb.write_reports(rows, jp, mp)


def _finish(res: dict, status: str, rounds_used: int) -> None:
    res["final_status"], res["rounds_used"] = status, rounds_used
    best = max(res["rounds"], key=rb._score)
    res["best_round"] = best["round"]
    res["best_round_summary"] = rb._round_summary(best)


def _validate_round(page: str, fr: Path, round_no: int) -> dict:
    row = rb.validate(page, fr, round_no)
    # validate() returns early, without a verdict, when the model declares no
    # total Lagrangian. That is a failure the agent can repair, not a pass.
    row.setdefault("full_pass", False)
    row.setdefault("checks", {})
    rb._persist_logs(row, fr.parent)
    return row


def cmd_init(a) -> int:
    pages = [p for p in a.pages.split(",") if p]
    state = {"subdir": a.subdir, "max_rounds": rb.MAX_ROUNDS, "engine": ENGINE,
             "model": a.model, "results": [], "cur": {}}
    print(f"[repair] init {len(pages)} models, subdir={a.subdir}, out={rb.OUTROOT}", flush=True)
    for i, page in enumerate(pages, 1):
        src = HERE / page / "model" / f"{page}_gen.fr"
        res: dict = {"page": page, "seed": str(src), "rounds": [], "agent_runs": []}
        rdir = HERE / page / a.subdir
        if rdir.exists():
            shutil.rmtree(rdir)
        if not src.is_file():
            res["final_status"] = "missing_fr"
            state["results"].append(res)
            continue
        cur = rdir / "round0" / "model.fr"
        cur.parent.mkdir(parents=True)
        shutil.copy2(src, cur)
        print(f"[repair] ({i}/{len(pages)}) {page} round 0 ...", flush=True)
        row = _validate_round(page, cur, 0)
        res["rounds"].append(row)
        if row["full_pass"]:
            res["final_status"], res["rounds_used"] = "pass_oneshot", 0
        state["cur"][page] = str(cur)
        state["results"].append(res)
        print(f"[repair]     -> {rb._round_summary(row)}", flush=True)
        _save(a.subdir, state)
    _save(a.subdir, state)
    return 0


def cmd_prepare(a) -> int:
    state = _load(a.subdir)
    entries = []
    for res in state["results"]:
        if res.get("final_status"):
            continue
        page = res["page"]
        cur = Path(state["cur"][page])
        wd = HERE / page / a.subdir / f"round{a.round}"
        wd.mkdir(parents=True, exist_ok=True)
        nxt = wd / "model.fr"
        shutil.copy2(cur, nxt)
        row = res["rounds"][-1]
        rb.build_report_md(row, wd)
        rb._write_history(res, wd)
        ufo_src = row.get("ufo_dir")
        if ufo_src and Path(ufo_src).is_dir() and not row.get("madgraph_import_ok"):
            shutil.copytree(ufo_src, wd / "UFO", dirs_exist_ok=True)
        tag = f"{a.subdir}/{page}/r{a.round}"
        entries.append({"page": page, "round": a.round, "tag": tag, "workdir": str(wd),
                        "before_sha": rb._sha(nxt), "prev": str(cur),
                        "user_prompt": PROMPT.format(tag=tag, workdir=str(wd))})
    out = HERE / f"repair_manifest_{a.subdir}_r{a.round}.json"
    out.write_text(json.dumps({"subdir": a.subdir, "round": a.round, "model": state["model"],
                               "entries": entries}, indent=1))
    print(f"[repair] round {a.round}: {len(entries)} models need an agent -> {out}", flush=True)
    for e in entries:
        print(f"  {e['tag']}", flush=True)
    return 0


def _audit(uses: list, workdir: str) -> tuple[bool, list[str]]:
    problems = []
    for name, inp in uses:
        if name not in ALLOWED:
            problems.append(f"tool {name}")
            continue
        for key in ("file_path", "path", "pattern"):
            v = inp.get(key)
            if isinstance(v, str) and v.startswith("/") and not v.startswith(workdir):
                problems.append(f"{name} outside workdir: {v}")
    return not problems, problems


def cmd_ingest(a) -> int:
    state = _load(a.subdir)
    man = json.loads((HERE / f"repair_manifest_{a.subdir}_r{a.round}.json").read_text())
    tdir = Path(a.transcripts_dir)
    by_tag: dict[str, Path] = {}
    for t in sorted(tdir.glob("agent-*.jsonl"), key=lambda p: p.stat().st_mtime):
        tag = sb._transcript_tag(t)
        if tag:
            by_tag[tag] = t          # latest transcript for a tag wins (retries)
    by_page = {r["page"]: r for r in state["results"]}
    to_validate = []
    for e in man["entries"]:
        res = by_page[e["page"]]
        wd = Path(e["workdir"])
        nxt = wd / "model.fr"
        shutil.rmtree(wd / "UFO", ignore_errors=True)
        t = by_tag.get(e["tag"])
        agent: dict = {"round": a.round, "engine": ENGINE, "model": man["model"],
                       "tool_policy": "instructed+audited"}
        if t is None:
            print(f"[ingest] {e['tag']}: no transcript", flush=True)
            agent.update({"exit": None, "timed_out": False, "seconds": None, "notes": "",
                          "missing_transcript": True, "changed": False, "diff_lines": 0})
            res["agent_runs"].append(agent)
            _finish(res, "agent_no_change", a.round)
            continue
        lines = t.read_text(errors="replace").splitlines()
        uses = sb._tool_uses(lines)
        audit_ok, problems = _audit(uses, e["workdir"])
        shutil.copy2(t, wd / "agent_stream.jsonl")
        notes = sb._final_text(lines)
        (wd / "agent_notes.md").write_text(notes)
        changed = rb._sha(nxt) != e["before_sha"]
        agent.update({"exit": 0, "timed_out": False, "seconds": None,
                      "notes": notes[-2000:], "n_tool_calls": len(uses),
                      "tool_names": sorted({n for n, _ in uses}),
                      "audit_ok": audit_ok, "audit_problems": problems,
                      "changed": changed,
                      "diff_lines": rb._difflines(Path(e["prev"]), nxt) if changed else 0,
                      "transcript": str(t)})
        res["agent_runs"].append(agent)
        print(f"[ingest] {e['tag']}: changed={changed} diff={agent['diff_lines']} "
              f"tools={agent['tool_names']} audit_ok={audit_ok}"
              + (f" problems={problems[:2]}" if problems else ""), flush=True)
        if not changed:
            _finish(res, "agent_no_change", a.round)
            continue
        to_validate.append((res, e["page"], nxt))
    _save(a.subdir, state)
    for i, (res, page, nxt) in enumerate(to_validate, 1):
        print(f"[repair] ({i}/{len(to_validate)}) validate {page} round {a.round} ...", flush=True)
        row = _validate_round(page, nxt, a.round)
        res["rounds"].append(row)
        state["cur"][page] = str(nxt)
        if row["full_pass"]:
            res["final_status"], res["rounds_used"] = "pass_repaired", a.round
            shutil.copy2(nxt, nxt.parent.parent / "final.fr")
        elif a.round >= state["max_rounds"]:
            _finish(res, "fail_after_repair", a.round)
        print(f"[repair]     -> {rb._round_summary(row)}", flush=True)
        _save(a.subdir, state)
    _save(a.subdir, state)
    left = [r["page"] for r in state["results"] if not r.get("final_status")]
    agg = {s: sum(1 for r in state["results"] if r.get("final_status") == s)
           for s in ("pass_oneshot", "pass_repaired", "fail_after_repair", "agent_no_change")}
    print(f"[repair] after round {a.round}: {json.dumps(agg)}; still open: {left}", flush=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init"); p.add_argument("--subdir", required=True)
    p.add_argument("--pages", required=True); p.add_argument("--model", default="claude-sonnet-5")
    p.set_defaults(fn=cmd_init)
    p = sub.add_parser("prepare"); p.add_argument("--subdir", required=True)
    p.add_argument("--round", type=int, required=True); p.set_defaults(fn=cmd_prepare)
    p = sub.add_parser("ingest"); p.add_argument("--subdir", required=True)
    p.add_argument("--round", type=int, required=True)
    p.add_argument("--transcripts-dir", required=True); p.set_defaults(fn=cmd_ingest)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
