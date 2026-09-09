#!/usr/bin/env python3
"""
# subagent_bench.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Run the agent stage of rerun_extract.py through Claude Code *subagents* of an
interactive session instead of the headless ``claude -p`` CLI, then hand the
outputs to rerun_extract.py (``--skip-existing``) for rendering, predicates
and the FeynRules -> UFO -> MadGraph chain.

Why this exists: on 2026-09-09 the headless CLI on the benchmark machine was
logged out ("OAuth session expired") and only a human can run ``claude
login``. An interactive Claude Code session can still spawn subagents, so the
benchmark stage that needs a model runs there, and everything deterministic
runs here as before.

What is different from the CLI harness, and recorded as such in run.json:

  * Tool restriction is a *policy plus audit*, not a hard limit. A subagent
    cannot be started with ``--tools ''`` or ``--allowedTools``; it is told
    what it may use, and ``ingest`` reads its transcript and marks the run
    ``audit_ok=False`` (and ``contaminated=True`` for sandbox escapes) when
    it used anything else. The report counts audited runs only.
  * ``notools`` runs read exactly ONE file, the input bundle
    ``<sandbox>/PROMPT.md`` (paper + SM.fr + task), because a subagent's
    prompt cannot carry 100-170 KB. After that read no tool of any kind is
    allowed. Everything else is identical to the CLI arm: no schema, no
    renderer, the agent writes the whole .fr.
  * ``tools`` runs read ``<sandbox>/PROMPT.md`` first, then the paper and
    the schema with Read/Grep/Glob under the sandbox root only.

Usage:
    python eval/benchmark_runs/subagent_bench.py prepare --pages A,B \
        --variant v3_tools --engine-mode tools --paper-source tex \
        --addendum eval/benchmark_runs/prompt_addendum_v3.txt --seeds 2
        -> writes <page>/rerun/<variant>/s<k>/{prompt.txt,sandbox_path.txt},
           <sandbox>/PROMPT.md, and subagent_manifest_<variant>.json
           (the list of runs the workflow script iterates over)

    python eval/benchmark_runs/subagent_bench.py ingest --variant v3_tools \
        --workflow-dir <transcript dir of the workflow run>
        -> maps each transcript to its run by the RUN-TAG in its first user
           message, audits tool use, writes agent_out.md, agent_stream.jsonl,
           run.json; then run rerun_extract.py --skip-existing for the variant.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import rerun_extract as rx  # noqa: E402

ENGINE = "claude-code-subagent"
ALLOWED_TOOLS = {"tools": {"Read", "Grep", "Glob"}, "notools": {"Read"}}

USER_PROMPT = {
    "tools": (
        "RUN-TAG: {tag}\n\n"
        "Your task is the file {bundle}. Read it first with the Read tool, then follow it "
        "exactly. Tool policy for this run: only Read, Grep and Glob, and only on files under "
        "{sandbox}. No shell, no web, no edits, no other directories. The task's final "
        "message is your final message."),
    "notools": (
        "RUN-TAG: {tag}\n\n"
        "Your entire task and every input you need are in the single file {bundle}. Read that "
        "ONE file with the Read tool (it is long: read it completely, in chunks with offset and "
        "limit, until you have seen the whole file). After that use NO tool of any kind: no "
        "other file, no search, no shell, no web. Work only from what you read. The task's "
        "final message is your final message."),
}


def _absolutize(prompt: str, page: str, sandbox: Path) -> str:
    """Make the sandbox-relative paths in a tools-mode prompt absolute, and say
    where the sandbox root is (the subagent's cwd is the repo, not the sandbox)."""
    root = str(sandbox)
    prompt = prompt.replace(f'"eval/benchmark_runs/{page}/text/', f'"{root}/eval/benchmark_runs/{page}/text/')
    prompt = prompt.replace("read tools/frgen/frmodel.py", f"read {root}/tools/frgen/frmodel.py")
    prompt = prompt.replace("SANDBOX: your working directory contains ONLY",
                            f"SANDBOX: the sandbox root is {root}. It contains ONLY")
    prompt = prompt.replace("Nothing else\nexists here and nothing outside this directory may be read.",
                            f"Nothing else\nexists there and nothing outside {root} may be read.")
    return prompt


def prepare(args) -> int:
    pages = [p for p in args.pages.split(",") if p]
    addendum = Path(args.addendum).read_text() if args.addendum else None
    runs = []
    for page in pages:
        paper_abs, paper_src = rx.paper_file(page, args.paper_source)
        for k in range(1, args.seeds + 1):
            rundir = HERE / page / "rerun" / args.variant / f"s{k}"
            if (rundir / "agent_out.md").is_file() and not args.force:
                print(f"[prepare] skip {page} s{k}: agent_out.md exists", flush=True)
                continue
            rundir.mkdir(parents=True, exist_ok=True)
            sandbox = rx.make_sandbox(page, rundir, paper_abs)
            prompt = rx.build_prompt(page, addendum, args.engine_mode, paper_abs, paper_src)
            if args.engine_mode == "tools":
                prompt = _absolutize(prompt, page, sandbox)
            (rundir / "prompt.txt").write_text(prompt)
            bundle = sandbox / "PROMPT.md"
            bundle.write_text(prompt)
            tag = f"{args.variant}/{page}/s{k}"
            runs.append({"page": page, "seed": k, "variant": args.variant, "tag": tag,
                         "mode": args.engine_mode, "paper_source": paper_src,
                         "paper_file": paper_abs.name, "sandbox": str(sandbox),
                         "bundle": str(bundle), "rundir": str(rundir),
                         "user_prompt": USER_PROMPT[args.engine_mode].format(
                             tag=tag, bundle=str(bundle), sandbox=str(sandbox))})
    manifest = {"variant": args.variant, "engine_mode": args.engine_mode,
                "paper_source": args.paper_source, "engine": ENGINE,
                "model": args.model, "runs": runs}
    out = HERE / f"subagent_manifest_{args.variant}.json"
    out.write_text(json.dumps(manifest, indent=1))
    print(f"[prepare] {len(runs)} runs -> {out}")
    return 0


# ------------------------------------------------------------------ ingest
def _transcript_tag(path: Path) -> str | None:
    """The RUN-TAG in the first user message of a subagent transcript."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("type") != "user":
                continue
            msg = rec.get("message") or {}
            content = msg.get("content")
            text = content if isinstance(content, str) else " ".join(
                b.get("text", "") for b in content if isinstance(b, dict))
            if "RUN-TAG:" in text:
                return text.split("RUN-TAG:", 1)[1].split()[0].strip()
            return None
    return None


def _tool_uses(lines: list[str]) -> list[tuple[str, dict]]:
    out = []
    for line in lines:
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("type") != "assistant":
            continue
        content = (rec.get("message") or {}).get("content")
        if not isinstance(content, list):
            continue
        for b in content:
            if isinstance(b, dict) and b.get("type") == "tool_use":
                out.append((b.get("name", ""), b.get("input") if isinstance(b.get("input"), dict) else {}))
    return out


def _final_text(lines: list[str]) -> str:
    """The last assistant text block(s) — the deliverable."""
    last = ""
    for line in lines:
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("type") != "assistant":
            continue
        content = (rec.get("message") or {}).get("content")
        if not isinstance(content, list):
            continue
        texts = [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
        if texts:
            last = "\n".join(texts)
    return last


def _delivered(mode: str, text: str) -> tuple[bool, str]:
    """Did the agent actually deliver a model, or did the engine fail?

    A run that ended on a usage limit, a transport error or a refusal leaves a
    short message with no fenced block. Writing that to agent_out.md would
    make ``--skip-existing`` treat the failure as a finished run for ever, so
    it is recorded as a failure and no output file is written.
    """
    if not text.strip():
        return False, "empty final message"
    if mode == "notools":
        ok = "M$ModelName" in text or "M$ClassesDescription" in text
    else:
        ok = "```json" in text or '"model_name"' in text
    if ok:
        return True, ""
    return False, f"no model in the final message: {text.strip()[:160]}"


def _audit(mode: str, uses: list, sandbox: str, bundle: str) -> tuple[bool, list[str]]:
    problems = []
    for name, inp in uses:
        if name not in ALLOWED_TOOLS[mode]:
            problems.append(f"tool {name} not allowed in {mode}")
            continue
        paths = [str(inp.get(k) or "") for k in ("file_path", "path") if inp.get(k)]
        if mode == "notools":
            if paths != [bundle]:
                problems.append(f"Read of {paths} instead of the bundle")
        else:
            for p in paths:
                if p.startswith("/") and not p.startswith(sandbox):
                    problems.append(f"{name} outside the sandbox: {p[:100]}")
            pat = str(inp.get("pattern") or "")
            if "reference_cache" in pat or "reference_cache" in " ".join(paths):
                problems.append(f"{name} names reference_cache")
    return not problems, problems


def ingest(args) -> int:
    manifest = json.loads((HERE / f"subagent_manifest_{args.variant}.json").read_text())
    wdir = Path(args.workflow_dir)
    modes = {r["tag"]: r["mode"] for r in manifest["runs"]}
    by_tag: dict[str, Path] = {}
    for t in sorted(wdir.glob("agent-*.jsonl")):
        tag = _transcript_tag(t)
        if not tag:
            continue
        # An agent that errored and was retried leaves two transcripts under
        # the same tag. Prefer the one that actually delivered a model, so a
        # retry's success is not overwritten by the earlier failure.
        prev = by_tag.get(tag)
        if prev is None:
            by_tag[tag] = t
            continue
        mode = modes.get(tag, "tools")
        prev_ok = _delivered(mode, _final_text(prev.read_text(errors="replace").splitlines()))[0]
        this_ok = _delivered(mode, _final_text(t.read_text(errors="replace").splitlines()))[0]
        if this_ok and not prev_ok:
            by_tag[tag] = t
    n_ok = 0
    for run in manifest["runs"]:
        rundir = Path(run["rundir"])
        t = by_tag.get(run["tag"])
        if t is None:
            print(f"[ingest] {run['tag']}: no transcript found", flush=True)
            continue
        lines = t.read_text(errors="replace").splitlines()
        uses = _tool_uses(lines)
        final = _final_text(lines)
        delivered, why = _delivered(run["mode"], final)
        audit_ok, problems = _audit(run["mode"], uses, run["sandbox"], run["bundle"])
        paper_rel = f"eval/benchmark_runs/{run['page']}/text/"
        parsed = rx._parse_stream(lines, paper_rel, Path(run["sandbox"]))
        bundle_reads = sum(1 for n, i in uses if n == "Read" and str(i.get("file_path")) == run["bundle"])
        facts = {
            "ok": delivered, "error": None if delivered else why,
            "exit": 0, "timed_out": False, "seconds": None,
            "engine": ENGINE, "model": manifest.get("model"), "mode": run["mode"],
            "tool_policy": "instructed+audited", "audit_ok": audit_ok, "audit_problems": problems,
            "n_tool_calls": len(uses), "tool_names": sorted({n for n, _ in uses}),
            "bundle_reads": bundle_reads,
            "read_paper": (parsed["read_paper"] or bundle_reads > 0) if run["mode"] == "tools"
                          else bundle_reads > 0,
            "contaminated": parsed["contaminated"] or not audit_ok,
            "outside_sandbox": parsed["outside_sandbox"],
            "files_read": parsed["files_read"][:40],
            "transcript": str(t),
        }
        if run["mode"] == "notools":
            facts["paper_inlined"] = True
            facts["anomalous_tool_calls"] = len(uses) - bundle_reads
        rundir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(t, rundir / "agent_stream.jsonl")
        if delivered:
            (rundir / "agent_out.md").write_text(final)
        else:
            # No model produced: leave no agent_out.md so --skip-existing and a
            # later `prepare` both treat this run as still owed.
            (rundir / "agent_failed.txt").write_text(final)
            (rundir / "agent_out.md").unlink(missing_ok=True)
        row = {"page": run["page"], "variant": run["variant"], "seed": run["seed"],
               "mode": run["mode"], "paper_source": run["paper_source"],
               "paper_file": run["paper_file"], "agent": facts}
        (rundir / "run.json").write_text(json.dumps(row, indent=1))
        n_ok += delivered
        print(f"[ingest] {run['tag']}: {'MODEL' if delivered else 'FAILED'} "
              f"text={len(final)} tools={len(uses)} {facts['tool_names']} "
              f"audit_ok={audit_ok} contaminated={facts['contaminated']}"
              + (f" problems={problems[:2]}" if problems else "")
              + ("" if delivered else f" | {why[:80]}"), flush=True)
    print(f"[ingest] {n_ok}/{len(manifest['runs'])} runs have a final text; now run\n"
          f"  rerun_extract.py --pages ... --variant {args.variant} --engine-mode "
          f"{manifest['engine_mode']} --paper-source {manifest['paper_source']} "
          f"--seeds N --skip-existing")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--pages", required=True)
    p.add_argument("--variant", required=True)
    p.add_argument("--engine-mode", choices=("tools", "notools"), default="tools")
    p.add_argument("--paper-source", choices=("tex", "txt"), default="tex")
    p.add_argument("--addendum", default="")
    p.add_argument("--seeds", type=int, default=2)
    p.add_argument("--model", default="claude-opus-5")
    p.add_argument("--force", action="store_true", help="re-prepare runs that already have output")
    p.set_defaults(fn=prepare)
    i = sub.add_parser("ingest")
    i.add_argument("--variant", required=True)
    i.add_argument("--workflow-dir", required=True)
    i.set_defaults(fn=ingest)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
