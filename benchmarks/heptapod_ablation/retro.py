#!/usr/bin/env python3
"""Retrospective ablation from the stored runs: what did the loop fix, which
tool output came before each fix, what stayed broken, and how many passes
survive a smaller validate budget.

    retro.py                 # writes retro.json and RETRO.md next to this file
    retro.py --runs DIR      # another benchmark_runs tree

Nothing here starts an agent or a Wolfram kernel. Inputs per run
(<runs>/<paper>/rerun/<arm>/s1/):

    validation_hepval.json            the score (pristine heptapod-dev driver)
    validation/call<k>/summary.json   the in-loop verdict of validate call k
    validation/call<k>/model.fr       the file that call validated
    validation/call<k>/agent_report.md   what the agent read (cc arm)
    tool_calls.jsonl                  every tool call, in order, with a time
    run.json                          tokens, cost, referee verdicts

Two readings guard the pass counts. A validate call on a file less than half
as long as the run's longest snapshot is a probe (the agent bisecting with
the scarce budget), not a candidate model: its pass does not count in the
budget curve. And a new particle with no vertex in the UFO is reported: the
chain passes such a model.

A chain has six items: compile, the four checks, and the MadGraph import
(mg5). A run's state is a verdict per item; a compile failure hides the other
five ("unknown").
"""

from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALE = HERE.parent.parent
sys.path.insert(0, str(ALE / "benchmarks"))
sys.path.insert(0, str(ALE / "cc_harness"))
sys.path.insert(0, str(ALE / "pi_harness"))
import common  # noqa: E402
import fr_lint  # noqa: E402
import hepval  # noqa: E402

PAPERS = (
    "331,ALRM_general,B-L-SM,ChernSimonsPortal,EffLRSM,GeneralU1,HeavyN,MDMmodel,"
    "Monotops,NJLComposite,SLQrules,SMWeinberg,Top-Philic-Zprime,Wprime,pNG,pSPSS"
).split(",")
CHECKS = ("hermiticity", "kinetic_diagonal", "mass_diagonal", "mass_spectrum")
ITEMS = ("compile", *CHECKS, "mg5")
LOOP_ARMS = {"cc_sonnet_harness": 10, "pi_qwen_harness": 6}
ONE_SHOT_ARMS = ("v3s_notools", "pi_qwen_plain")
BUDGETS = (1, 2, 3, 4, 6, 10)
# What the agent had been told about an item before it went from fail to pass.
# diag_report, lint and massbasis exist only in the ALE wrapper; compile_log,
# mg5_message and verdict_only are what heptapod-dev origin/main also returns.
SOURCES = ("diag_report", "lint", "massbasis", "compile_log", "mg5_message", "verdict_only")
# Which chain items a lint finding of a given stage is about.
LINT_STAGE_ITEMS = {
    "harness": ("compile",),
    "compile": ("compile",),
    "checks": CHECKS,
    "mg5": ("mg5",),
}
# The three check-stage rules each predict specific checks.
LINT_RULE_ITEMS = {
    "mixing_in_definitions": ("mass_diagonal", "mass_spectrum"),
    "numeric_spin_slot": ("hermiticity",),
    "majorana_mass_no_half": ("mass_spectrum",),
}
# The report sections only the ALE diag driver and diagnose.py produce;
# heptapod-dev origin/main returns the verdict and 400 characters of prose.
DIAG_SECTIONS = {
    "hermiticity": "## Hermiticity: the non-zero vertices of L - HC[L]",
    "mass_diagonal": "## Mass matrix: the off-diagonal entries the check found",
    "mg5": "## MadGraph import: where the UFO breaks",
}


def _json(path: Path):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None


def _jsonl(path: Path) -> list[dict]:
    out = []
    if path.is_file():
        for line in path.read_text(errors="replace").splitlines():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def chain_state(compile_ok, checks, mg5_ok) -> dict:
    """A verdict per item. Inconclusive counts as fail: the scorer's
    all_checks_pass accepts only "pass"."""
    if not compile_ok:
        return {"compile": "fail", **{k: "unknown" for k in ITEMS[1:]}}
    s = {"compile": "pass"}
    for k in CHECKS:
        s[k] = "pass" if (checks or {}).get(k) == "pass" else "fail"
    s["mg5"] = "pass" if mg5_ok else "fail"
    return s


def stage_of(state: dict) -> str:
    if state["compile"] != "pass":
        return "compile"
    if any(state[k] != "pass" for k in CHECKS):
        return "checks"
    return "mg5" if state["mg5"] != "pass" else "pass"


def is_pass(state: dict) -> bool:
    return all(state[k] == "pass" for k in ITEMS)


def score_state(v: dict | None) -> dict | None:
    """The state of a scored model; None when nothing was delivered."""
    if not v:
        return None
    return chain_state(v.get("compile_ok"), v.get("checks"), v.get("madgraph_import_ok"))


def compile_kind(row: dict, log: str) -> str:
    """Why a compile did not produce a UFO, from the driver's own log."""
    if row.get("status") == "no_lagrangian_symbol":
        return "no_total_lagrangian"
    if row.get("timed_out"):
        return "timeout"
    if "undefined symbol(s) in Lagrangian" in log:
        return "undefined_symbol"
    if re.search(r"Syntax::|ToExpression::sntx", log):
        return "syntax"
    if "RecursionLimit" in log:
        return "recursion_limit"
    if "UFO is incomplete" in log:
        return "ufo_incomplete"
    return "other"


def mg5_kind(row: dict) -> str:
    """Why MadGraph rejected a UFO. Its last line is the same for every cause
    ("invalid syntax (object_library.py, line 268)", from the fallback import of
    FeynRules' Python 2 library), so the cause is read from MG5_debug and from
    the static syntax check of the UFO files."""
    if row.get("ufo_syntax_errors"):
        return "ufo_not_python"
    dbg = (row.get("mg5_debug_tail") or "") + (row.get("mg5_tail") or "")
    if "define multiple time" in dbg:
        return "duplicate_parameter_name"
    if "'1' order" in dbg:
        return "coupling_without_order"
    if row.get("reason") == "timeout" or "timeout" in str(row.get("mg5_tail"))[:40].lower():
        return "timeout"
    return "other"


def lint_findings(fr: Path) -> list[dict]:
    """hepval's lint (fr_lint plus the comment/bracket structure rules) on a
    stored file, error level only (a stage is predicted)."""
    text = fr.read_text(errors="replace")
    fs = hepval._structure_findings(text) + [f.__dict__ for f in fr_lint.lint_file(str(fr))]
    return [
        {"rule": f["rule"], "stage": f["stage"], "line": f.get("line")}
        for f in fs
        if f["stage"] in LINT_STAGE_ITEMS
    ]


def rule_items(f: dict) -> tuple:
    return LINT_RULE_ITEMS.get(f["rule"]) or LINT_STAGE_ITEMS[f["stage"]]


def lint_items(findings: list[dict]) -> set:
    return {i for f in findings for i in rule_items(f)}


def report_signals(report: str) -> dict:
    """What the report the agent read contained beyond the verdicts."""
    sig = {}
    for item, head in DIAG_SECTIONS.items():
        if head not in report:
            continue
        body = report.split(head, 1)[1].split("\n## ", 1)[0]
        if item == "hermiticity":
            verts = re.findall(r"^- vertex \d+: fields (.*?); block: (.*)$", body, re.M)
            sig[item] = {
                "vertices": len(verts),
                "located": sum(b.strip() != "not located" for _f, b in verts),
                "unreduced": body.count("UNREDUCED:"),
                "blocks": sorted(
                    {
                        x.strip()
                        for _f, b in verts
                        for x in b.split(",")
                        if x.strip() and x.strip() != "not located"
                    }
                ),
            }
        elif item == "mass_diagonal":
            sig[item] = {"rows": len(re.findall(r"^\| (?!fields|field|---)", body, re.M))}
        else:
            objs = body.split("\n### ")[1:]
            sig[item] = {
                "objects": len(objs),
                "with_fr_lines": sum("model.fr lines:\n- line" in o for o in objs),
            }
    return sig


def named(item: str, sig: dict) -> bool:
    """Did the report localise this failing item (a block, a mass-matrix
    entry, or model.fr lines), not only state it?"""
    if item == "hermiticity":
        return bool(sig.get(item, {}).get("located") or sig.get(item, {}).get("unreduced"))
    if item in ("mass_diagonal", "mass_spectrum"):
        return bool(sig.get("mass_diagonal", {}).get("rows"))
    if item == "mg5":
        return bool(sig.get(item, {}).get("with_fr_lines"))
    return False


def load_calls(d: Path) -> list[dict]:
    calls = []
    k = 1
    while (d / "validation" / f"call{k}" / "summary.json").is_file():
        cd = d / "validation" / f"call{k}"
        s = _json(cd / "summary.json") or {}
        row = s.get("row") or {}
        log = cd / "round0" / "compile.log"
        log = log.read_text(errors="replace") if log.is_file() else ""
        state = chain_state(s.get("compile_ok"), s.get("checks"), s.get("madgraph_import_ok"))
        report = next(
            (
                p.read_text(errors="replace")
                for p in (cd / "agent_report.md", d / "validation_agent_view" / f"call{k}.md")
                if p.is_file()
            ),
            "",
        )
        fr = cd / "model.fr"
        calls.append(
            {
                "call": k,
                "state": state,
                "stage": stage_of(state),
                "pass": is_pass(state),
                "compile_kind": None if state["compile"] == "pass" else compile_kind(row, log),
                "mg5_kind": mg5_kind(row) if state["mg5"] == "fail" else None,
                "seconds": s.get("seconds"),
                "lock_wait_seconds": s.get("lock_wait_seconds"),
                "t_end": s.get("t_kernel_end"),
                "diag_driver": s.get("driver") == "diag",
                "signals": report_signals(report),
                "lint": lint_findings(fr) if fr.is_file() else [],
                "sha": common.sha(fr),
                "lines": len(fr.read_text(errors="replace").splitlines()) if fr.is_file() else 0,
                "ufo": str(cd / "round0" / "UFO")
                if (cd / "round0" / "UFO" / "vertices.py").is_file()
                else None,
            }
        )
        k += 1
    longest = max((c["lines"] for c in calls), default=0)
    for c in calls:
        c["probe"] = c["lines"] < 0.5 * longest
        c["pass"] = c["pass"] and not c["probe"]
    return calls


def ufo_particles(ufo: Path) -> set:
    """Python names of the particles a UFO declares (antiparticles excluded)."""
    return set(
        re.findall(r"^(\w+) = Particle\(", (ufo / "particles.py").read_text(errors="replace"), re.M)
    )


SM_PARTICLES = frozenset(json.loads((HERE / "sm_ufo_particles.json").read_text())["particles"])


def particles_without_vertex(ufo: Path) -> list[str]:
    """New particles (not in the UFO of SM.fr alone) that no vertex contains,
    as particle or antiparticle. Ghosts are skipped: MadGraph does not need
    them. The chain passes a model like this; its new physics is not in the UFO."""
    used = set(re.findall(r"P\.(\w+)", (ufo / "vertices.py").read_text(errors="replace")))
    return sorted(
        n
        for n in ufo_particles(ufo) - SM_PARTICLES
        if n not in used and n + "__tilde__" not in used and not n.startswith("gh")
    )


def tool_segments(d: Path, n_calls: int) -> list[dict]:
    """Tool calls grouped by the validate call they come before: segment 0 is
    before the first validation, segment k is between calls k and k+1."""
    segs = [
        {"lint": 0, "lint_with_findings": 0, "lint_rules": [], "massbasis": 0, "review": 0}
        for _ in range(n_calls + 1)
    ]
    k = 0
    for ev in _jsonl(d / "tool_calls.jsonl"):
        tool = ev.get("tool")
        if ev.get("event") == "call":
            if tool == "validate_model":
                k = min(k + 1, n_calls)
            elif tool in ("massbasis", "review_model"):
                segs[k][tool.replace("_model", "")] += 1
            elif tool == "lint_model":
                segs[k]["lint"] += 1
        elif ev.get("event") == "result" and tool == "lint_model":
            head = ev.get("head") or ev.get("output") or ""
            if (
                isinstance(head, str)
                and not head.startswith("lint: no findings")
                and '"n": 0' not in head
            ):
                segs[k]["lint_with_findings"] += 1
                # The log keeps 400 characters of each result: the first rules only.
                segs[k]["lint_rules"] += re.findall(r"\[(?:\w+)\] (\w+)|\"rule\": \"(\w+)\"", head)
    for s in segs:
        s["lint_rules"] = sorted({a or b for a, b in s["lint_rules"]})
    return segs


def transitions(calls: list[dict], segs: list[dict]) -> list[dict]:
    """One row per item whose verdict changed between consecutive calls, with
    the tool outputs the agent had received in between."""
    out = []
    for a, b, seg in zip(calls, calls[1:], segs[1:]):
        cleared = lint_items(a["lint"]) - lint_items(b["lint"])
        cleared_rules = sorted({f["rule"] for f in a["lint"]} - {f["rule"] for f in b["lint"]})
        for item in ITEMS:
            x, y = a["state"][item], b["state"][item]
            if x == y or "unknown" in (x, y):
                continue
            sources = []
            if x == "fail":
                if named(item, a["signals"]):
                    sources.append("diag_report")
                if item in cleared:
                    sources.append("lint")
                if seg["massbasis"] and item in ("mass_diagonal", "mass_spectrum"):
                    sources.append("massbasis")
                if item == "compile" and a["compile_kind"] in (
                    "undefined_symbol",
                    "syntax",
                    "no_total_lagrangian",
                ):
                    sources.append("compile_log")
                if item == "mg5" and a["mg5_kind"] in (
                    "duplicate_parameter_name",
                    "coupling_without_order",
                ):
                    sources.append("mg5_message")
                if not sources:
                    sources.append("verdict_only")
            out.append(
                {
                    "from_call": a["call"],
                    "to_call": b["call"],
                    "item": item,
                    "change": "fixed" if x == "fail" else "broken",
                    "sources": sources,
                    "lint_rules_cleared": cleared_rules if "lint" in sources else [],
                    "kind": a["compile_kind"]
                    if item == "compile"
                    else a["mg5_kind"]
                    if item == "mg5"
                    else None,
                    "review_between": bool(seg["review"]),
                }
            )
    return out


def referee(d: Path, agent: dict, final_sha: str | None) -> dict | None:
    """The referee's verdict on the model that was scored, if one exists."""
    post = _json(d / "post_review" / "verdict.json")
    if post and post.get("model_sha") == final_sha:
        return {"verdict": post.get("verdict"), "post_hoc": True}
    on_final = [r for r in agent.get("reviews") or [] if r.get("reviewed_final_model")]
    if on_final:
        return {"verdict": on_final[-1].get("verdict"), "post_hoc": False}
    views = (
        sorted((d / "validation_agent_view").glob("review*_model.review.md"))
        if (d / "validation_agent_view").is_dir()
        else []
    )
    for v in reversed(views):
        if common.sha(v.with_name(v.name.replace(".review.md", ".fr"))) == final_sha:
            line = next(
                (
                    x.strip()
                    for x in reversed(v.read_text(errors="replace").splitlines())
                    if x.strip().upper().startswith("VERDICT:")
                ),
                None,
            )
            return {"verdict": line, "post_hoc": False}
    return None


def physics_changing(verdict: str | None) -> int | None:
    if not verdict:
        return None
    if "NO DISCREPANCIES" in verdict.upper():
        return 0
    m = re.search(r"(\d+)\s+PHYSICS-CHANGING", verdict.upper())
    return int(m.group(1)) if m else None


def usage_of(agent: dict, d: Path) -> dict:
    u = agent.get("usage") or {}
    if "input_total" in u:  # Claude Code harness
        reviews = agent.get("reviews") or []
        return {
            "input_total": u["input_total"],
            "input_uncached": u["input_tokens"] + u["cache_creation_input_tokens"],
            "output": u["output_tokens"],
            "cost_usd": round(
                float(agent.get("cost_usd") or 0)
                + sum(float(r.get("cost_usd") or 0) for r in reviews),
                4,
            ),
            "seconds": agent.get("seconds"),
        }
    if "input" in u:  # pi: self-hosted, no bill per token
        return {
            "input_total": u["input"] + u.get("cacheRead", 0),
            "input_uncached": u["input"],
            "output": u["output"],
            "cost_usd": None,
            "seconds": agent.get("seconds"),
        }
    # One-shot Claude Code subagent arms: run.json has no usage; the stream's
    # last usage record per message is what the API reported.
    per_msg = {}
    for ev in _jsonl(d / "agent_stream.jsonl"):
        m = ev.get("message") or {}
        if ev.get("type") == "assistant" and m.get("id") and m.get("usage"):
            per_msg[m["id"]] = m["usage"]
    if not per_msg:
        return {
            "input_total": None,
            "input_uncached": None,
            "output": None,
            "cost_usd": None,
            "seconds": None,
        }

    def tot(k: str) -> int:
        return sum(int(x.get(k) or 0) for x in per_msg.values())

    return {
        "input_total": tot("input_tokens")
        + tot("cache_creation_input_tokens")
        + tot("cache_read_input_tokens"),
        "input_uncached": tot("input_tokens") + tot("cache_creation_input_tokens"),
        "output": tot("output_tokens"),
        "cost_usd": None,
        "seconds": None,
    }


def load_run(runs: Path, paper: str, arm: str, scored_ufo: Path | None = None) -> dict:
    d = runs / paper / "rerun" / arm / "s1"
    run = _json(d / "run.json") or {}
    agent = run.get("agent") or {}
    score = _json(d / "validation_hepval.json")
    fr = d / "model" / f"{paper}_gen.fr"
    final_sha = common.sha(fr)
    calls = load_calls(d)
    segs = tool_segments(d, len(calls))
    st = score_state(score)
    ref = referee(d, agent, final_sha)
    return {
        "paper": paper,
        "arm": arm,
        "ran": bool(run),
        "delivered": fr.is_file(),
        "score": st,
        "score_stage": stage_of(st) if st else "no_model",
        "score_pass": bool(st and is_pass(st)),
        "score_status": (score or {}).get("status"),
        "final_lint": lint_findings(fr) if fr.is_file() else [],
        "calls": calls,
        "segments": segs,
        "transitions": transitions(calls, segs),
        "final_validated_in_loop": bool(calls and calls[-1]["sha"] == final_sha),
        # The UFO of the scored file: a local re-score of it, else the in-loop
        # call that validated the same bytes.
        "scored_ufo": next(
            (
                u
                for u in [
                    str(d / "score_ufo"),
                    *([str(scored_ufo / paper / "call1" / "round0" / "UFO")] if scored_ufo else []),
                    *[c["ufo"] for c in reversed(calls) if c["sha"] == final_sha and c["ufo"]],
                ]
                if u and (Path(u) / "vertices.py").is_file()
            ),
            None,
        ),
        "referee": ref,
        "physics_changing": physics_changing((ref or {}).get("verdict")),
        "usage": usage_of(agent, d),
        "api_error": agent.get("api_error"),
        "stop_gate_blocks": (agent.get("stop_gate") or {}).get("blocks"),
    }


def budget_curve(runs: list[dict], budgets=BUDGETS) -> dict:
    """Passes that survive a validate budget of B, two readings.

    first_pass: some call k <= B passed (the agent would have had a passing
        file in hand and the Stop gate would have let it stop).
    at_budget:  the file the run had at its B-th call passes (or the scored
        file, when the run used B calls or fewer): what a hard cut at B hands in.
    """
    out = {}
    for b in budgets:
        first, at = [], []
        for r in runs:
            calls = r["calls"]
            if any(c["pass"] for c in calls[:b]):
                first.append(r["paper"])
            if len(calls) <= b:
                if r["score_pass"]:
                    at.append(r["paper"])
            elif calls[b - 1]["pass"]:
                at.append(r["paper"])
        out[str(b)] = {
            "first_pass": sorted(first),
            "at_budget": sorted(at),
            "n_first_pass": len(first),
            "n_at_budget": len(at),
        }
    return out


def end_state(r: dict) -> list[dict]:
    """For a run that does not pass: each failing item of the scored model,
    and whether the last report or the lint pointed at it."""
    if r["score_pass"] or not r["score"]:
        return []
    last = r["calls"][-1] if r["calls"] else None
    same = bool(last and r["final_validated_in_loop"])
    lint_now = lint_items(r["final_lint"])
    rows = []
    for item in ITEMS:
        if r["score"][item] != "fail":
            continue
        streak = 0
        for c in reversed(r["calls"]):
            if c["state"][item] != "fail":
                break
            streak += 1
        diag = bool(last and named(item, last["signals"]))
        rows.append(
            {
                "item": item,
                "consecutive_failing_calls": streak,
                "kind": (
                    last["compile_kind"]
                    if item == "compile"
                    else last["mg5_kind"]
                    if item == "mg5"
                    else None
                )
                if last
                else None,
                "named_by_last_report": diag,
                "named_by_lint": item in lint_now,
                "lint_rules": sorted({f["rule"] for f in r["final_lint"] if item in rule_items(f)}),
                "last_report_is_for_scored_file": same,
                # A lint rule of the item's stage is a weak signal: it can be about another
                # construct.
                "class": "located_by_report"
                if diag
                else "lint_rule_of_that_item"
                if item in lint_now
                else "nothing",
            }
        )
    return rows


def lint_only(r: dict) -> dict:
    """What the lint alone says about a one-shot model, against its score."""
    failing = {i for i in ITEMS if r["score"] and r["score"][i] == "fail"}
    # A compile failure hides the later items, so a lint that predicts them
    # cannot be confirmed or refuted on that file.
    visible = {i for i in ITEMS if r["score"] and r["score"][i] != "unknown"}
    flagged = lint_items(r["final_lint"])
    return {
        "paper": r["paper"],
        "score_pass": r["score_pass"],
        "score_stage": r["score_stage"],
        "failing": sorted(failing),
        "flagged": sorted(flagged),
        "hit": sorted(failing & flagged),
        "missed": sorted(failing - flagged),
        "false_alarm": sorted((flagged & visible) - failing),
        "all_failures_flagged": bool(failing) and failing <= flagged,
        "rules": sorted({f["rule"] for f in r["final_lint"]}),
    }


# What each kind of feedback can see of a failing draft. A loop cannot fix
# what its tool does not report.
FEEDBACK_SEES = {
    "compile": ("compile",),
    "compile + MadGraph import": ("compile", "mg5"),
    "compile + four checks + import (heptapod)": ITEMS,
}


def visibility(states: dict) -> dict:
    """For first drafts (paper -> chain state): how many fail; for each
    feedback level, how many it reports at all, and how many it reports in
    full (every failing item is in its report). A draft that does not compile
    counts as reported in full: its later items are not known yet."""
    failing = {p: {i for i in ITEMS if s[i] == "fail"} for p, s in states.items() if not is_pass(s)}
    out = {"drafts": len(states), "failing": len(failing)}
    for level, items in FEEDBACK_SEES.items():
        some = sorted(p for p, f in failing.items() if f & set(items))
        every = sorted(p for p, f in failing.items() if f <= set(items))
        out[level] = {
            "sees_some": len(some),
            "sees_every_item": len(every),
            "blind_to": sorted(set(failing) - set(some)),
            "partly_blind_to": sorted(set(some) - set(every)),
        }
    return out


def mcnemar(a_only: int, b_only: int) -> float:
    """Two-sided exact McNemar p-value from the discordant pairs."""
    n = a_only + b_only
    if n == 0:
        return 1.0
    k = min(a_only, b_only)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2**n)


def analyse(runs_dir: Path, scored_ufo: dict | None = None) -> dict:
    data = {
        arm: [load_run(runs_dir, p, arm, (scored_ufo or {}).get(arm)) for p in PAPERS]
        for arm in (*LOOP_ARMS, *ONE_SHOT_ARMS)
    }
    for runs in data.values():
        for r in runs:
            r["particles_without_vertex"] = (
                particles_without_vertex(Path(r["scored_ufo"])) if r["scored_ufo"] else None
            )
    res = {"runs_dir": str(runs_dir), "papers": list(PAPERS), "arms": {}}
    for arm, runs in data.items():
        a = {
            "n": len(runs),
            "delivered": sum(r["delivered"] for r in runs),
            "pass": sorted(r["paper"] for r in runs if r["score_pass"]),
            "funnel": {
                i: sum(bool(r["score"]) and r["score"][i] == "pass" for r in runs) for i in ITEMS
            },
            "runs": runs,
        }
        if arm in LOOP_ARMS:
            started = [r for r in runs if r["calls"]]
            a["first_call"] = {
                "runs_with_a_call": len(started),
                "stage": {
                    s: sorted(r["paper"] for r in started if r["calls"][0]["stage"] == s)
                    for s in ("compile", "checks", "mg5", "pass")
                },
                "funnel": {
                    i: sum(r["calls"][0]["state"][i] == "pass" for r in started) for i in ITEMS
                },
            }
            a["first_draft_visibility"] = visibility(
                {r["paper"]: r["calls"][0]["state"] for r in started}
            )
            a["budget_curve"] = budget_curve(runs)
            tr = [dict(t, paper=r["paper"]) for r in runs for t in r["transitions"]]
            fixed = [t for t in tr if t["change"] == "fixed"]
            a["transitions"] = {
                "fixed": len(fixed),
                "broken": sum(t["change"] == "broken" for t in tr),
                "fixed_by_item": {i: sum(t["item"] == i for t in fixed) for i in ITEMS},
                "fixed_by_source": {s: sum(s in t["sources"] for t in fixed) for s in SOURCES},
                "fixed_item_x_source": {
                    i: {
                        s: sum(t["item"] == i and s in t["sources"] for t in fixed) for s in SOURCES
                    }
                    for i in ITEMS
                },
                "rows": tr,
            }
            ale = ("diag_report", "lint", "massbasis")
            a["transitions"]["fixed_ale_only_source"] = sum(
                any(x in t["sources"] for x in ale) for t in fixed
            )
            a["transitions"]["fixed_upstream_info"] = sum(
                not any(x in t["sources"] for x in ale) for t in fixed
            )
            cb: dict = {}
            for r in runs:
                for c in r["calls"]:
                    for i in ITEMS:
                        if c["state"][i] == "fail":
                            kind = (
                                c["compile_kind"]
                                if i == "compile"
                                else c["mg5_kind"]
                                if i == "mg5"
                                else None
                            )
                            e = cb.setdefault(
                                i + (f": {kind}" if kind else ""), {"calls": 0, "papers": set()}
                            )
                            e["calls"] += 1
                            e["papers"].add(r["paper"])
            a["calls_by_failure"] = {
                k: {"calls": v["calls"], "papers": sorted(v["papers"])}
                for k, v in sorted(cb.items(), key=lambda kv: -kv[1]["calls"])
            }
            a["end_state"] = {
                r["paper"]: end_state(r) for r in runs if not r["score_pass"] and r["score"]
            }
            a["tool_use"] = {
                "validate_calls": sum(len(r["calls"]) for r in runs),
                "lint_before_first_validate": sum(r["segments"][0]["lint"] for r in runs),
                "lint_with_findings_before_first_validate": sum(
                    r["segments"][0]["lint_with_findings"] for r in runs
                ),
                "runs_massbasis": sorted(
                    r["paper"] for r in runs if any(s["massbasis"] for s in r["segments"])
                ),
                "runs_review": sorted(
                    r["paper"] for r in runs if any(s["review"] for s in r["segments"])
                ),
            }
            a["probes"] = {
                r["paper"]: [c["call"] for c in r["calls"] if c["probe"]]
                for r in runs
                if any(c["probe"] for c in r["calls"])
            }
            passes = [r for r in runs if r["score_pass"]]
            faithful = [r for r in passes if r["physics_changing"] == 0]
            a["fidelity"] = {
                "pass": len(passes),
                "pass_with_referee_verdict": sum(r["referee"] is not None for r in passes),
                "pass_no_physics_change": sorted(r["paper"] for r in faithful),
                "pass_physics_changing": sorted(
                    r["paper"] for r in passes if (r["physics_changing"] or 0) > 0
                ),
                "pass_not_reviewed": sorted(
                    r["paper"] for r in passes if r["physics_changing"] is None
                ),
                "pass_ufo_inspected": sum(
                    r["particles_without_vertex"] is not None for r in passes
                ),
                "pass_with_a_new_particle_without_vertex": {
                    r["paper"]: r["particles_without_vertex"]
                    for r in passes
                    if r["particles_without_vertex"]
                },
                "pass_faithful_and_all_new_particles_interact": sorted(
                    r["paper"] for r in faithful if r["particles_without_vertex"] == []
                ),
            }
        costs = [r["usage"]["cost_usd"] for r in runs if r["usage"]["cost_usd"] is not None]
        ins = [r["usage"]["input_total"] for r in runs if r["usage"]["input_total"] is not None]
        outs = [r["usage"]["output"] for r in runs if r["usage"]["output"] is not None]
        n_pass = len(a["pass"])
        a["cost"] = {
            "runs_with_usage": len(ins),
            "total_cost_usd": round(sum(costs), 2) if costs else None,
            "total_input": sum(ins),
            "total_output": sum(outs),
            "median_cost_usd": round(statistics.median(costs), 2) if costs else None,
            "cost_per_pass_usd": round(sum(costs) / n_pass, 2) if costs and n_pass else None,
            "input_per_pass": round(sum(ins) / n_pass) if ins and n_pass else None,
            "output_per_pass": round(sum(outs) / n_pass) if outs and n_pass else None,
        }
        if arm in LOOP_ARMS and costs and a["fidelity"]["pass_no_physics_change"]:
            a["cost"]["cost_per_faithful_pass_usd"] = round(
                sum(costs) / len(a["fidelity"]["pass_no_physics_change"]), 2
            )
        if arm in ONE_SHOT_ARMS:
            a["first_draft_visibility"] = visibility(
                {r["paper"]: r["score"] for r in runs if r["score"]}
            )
            lo = [lint_only(r) for r in runs if r["score"]]
            fails = [x for x in lo if not x["score_pass"]]
            a["lint_only"] = {
                "scored": len(lo),
                "failing": len(fails),
                "failing_with_a_hit": sum(bool(x["hit"]) for x in fails),
                "failing_all_failures_flagged": sorted(
                    x["paper"] for x in fails if x["all_failures_flagged"]
                ),
                "failing_no_finding": sorted(x["paper"] for x in fails if not x["flagged"]),
                "passing_with_false_alarm": sorted(
                    x["paper"] for x in lo if x["score_pass"] and x["flagged"]
                ),
                "hit_by_item": {i: sum(i in x["hit"] for x in fails) for i in ITEMS},
                "failing_by_item": {i: sum(i in x["failing"] for x in fails) for i in ITEMS},
                "rows": lo,
            }
        res["arms"][arm] = a
    # Paired comparisons at an equal validate budget.
    cc, pi, nt = (res["arms"][k] for k in ("cc_sonnet_harness", "pi_qwen_harness", "v3s_notools"))
    res["paired"] = {}
    for b in BUDGETS:
        for reading in ("first_pass", "at_budget"):
            s = set(cc["budget_curve"][str(b)][reading])
            for name, other in (
                ("v3s_notools", set(nt["pass"])),
                ("pi_qwen_harness", set(pi["pass"])),
            ):
                res["paired"][f"cc@{b}:{reading} vs {name}"] = {
                    "cc": len(s),
                    "other": len(other),
                    "cc_only": len(s - other),
                    "other_only": len(other - s),
                    "p": round(mcnemar(len(s - other), len(other - s)), 4),
                }
    return res


def _table(head: list[str], rows: list[list]) -> list[str]:
    return [
        "| " + " | ".join(head) + " |",
        "|" + "---|" * len(head),
        *["| " + " | ".join(str(c) for c in r) + " |" for r in rows],
        "",
    ]


def _seq(r: dict) -> str:
    glyph = {"pass": "P", "fail": "F", "unknown": "-"}
    return " ".join(
        c["stage"][:2] + ":" + "".join(glyph[c["state"][i]] for i in ITEMS) for c in r["calls"]
    )


def render(res: dict) -> str:
    L = [
        "# Retrospective ablation from the stored runs (generated by retro.py)",
        "",
        "Do not edit: run `python benchmarks/heptapod_ablation/retro.py`. Items per call are "
        "compile, hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum, mg5 "
        "(P pass, F fail, - hidden by a compile failure).",
        "",
    ]
    for arm, budget in LOOP_ARMS.items():
        a = res["arms"][arm]
        L += [f"## {arm} (validate budget {budget})", "", "### Per paper", ""]
        rows = []
        for r in a["runs"]:
            fc = r["calls"][0]["stage"] if r["calls"] else "no call"
            first = next((c["call"] for c in r["calls"] if c["pass"]), "")
            seg = r["segments"]
            rows.append(
                [
                    r["paper"],
                    fc,
                    r["score_stage"],
                    len(r["calls"]),
                    first,
                    sum(s["lint"] for s in seg),
                    sum(s["massbasis"] for s in seg),
                    sum(s["review"] for s in seg),
                    "" if r["physics_changing"] is None else r["physics_changing"],
                    f"`{_seq(r)}`",
                ]
            )
        L += _table(
            [
                "paper",
                "first call",
                "scored",
                "calls",
                "first pass at",
                "lint",
                "massbasis",
                "review",
                "referee: physics-changing",
                "in-loop verdicts",
            ],
            rows,
        )
        f1, fs = a["first_call"]["funnel"], a["funnel"]
        L += ["### First validation against the scored file", ""]
        L += _table(
            ["item", "passes at call 1", "passes in the scored file"],
            [[i, f1[i], fs[i]] for i in ITEMS],
        )
        L += [
            f"Runs with at least one call: {a['first_call']['runs_with_a_call']}. First-call "
            "stage: "
            + "; ".join(f"{s} {len(p)}" for s, p in a["first_call"]["stage"].items())
            + ".",
            "",
        ]
        t = a["transitions"]
        L += [
            "### What changed between consecutive calls, and what the agent had just been told",
            "",
            f"{t['fixed']} item verdicts went fail to pass and {t['broken']} went pass to fail. "
            "A fix can have "
            "more than one source, so a row can sum to more than its count.",
            "",
        ]
        L += _table(
            ["item", "fixed", *SOURCES],
            [
                [i, t["fixed_by_item"][i], *[t["fixed_item_x_source"][i][s] for s in SOURCES]]
                for i in ITEMS
            ]
            + [["all", t["fixed"], *[t["fixed_by_source"][s] for s in SOURCES]]],
        )
        L += [
            "Fixes with a source only the ALE wrapper has (diag_report, lint or massbasis): "
            f"{t['fixed_ale_only_source']}. "
            "Fixes where the agent had only what heptapod-dev origin/main also returns: "
            f"{t['fixed_upstream_info']}.",
            "",
        ]
        cb = a["calls_by_failure"]
        L += [
            "Validate calls that ended with each failure (a call with two failing items counts "
            "in both rows):",
            "",
        ]
        L += _table(
            ["failure", "calls", "papers"],
            [[k, v["calls"], ", ".join(v["papers"])] for k, v in cb.items()],
        )
        L += _table(
            ["paper", "calls", "item", "change", "sources", "lint rules cleared"],
            [
                [
                    x["paper"],
                    f"{x['from_call']}->{x['to_call']}",
                    x["item"] + (f" ({x['kind']})" if x["kind"] else ""),
                    x["change"],
                    ", ".join(x["sources"]),
                    ", ".join(x["lint_rules_cleared"]),
                ]
                for x in t["rows"]
            ],
        )
        L += ["### Failures that remain in the scored file", ""]
        L += _table(
            [
                "paper",
                "item",
                "failing for the last n calls",
                "last report located it",
                "lint rules about that item",
                "what the agent had",
            ],
            [
                [
                    p,
                    e["item"] + (f" ({e['kind']})" if e["kind"] else ""),
                    e["consecutive_failing_calls"],
                    e["named_by_last_report"],
                    ", ".join(e["lint_rules"]) or "no",
                    e["class"],
                ]
                for p, es in a["end_state"].items()
                for e in es
            ],
        )
        L += ["### Budget curve", ""]
        L += _table(
            [
                "validate budget",
                "a call up to here passed",
                "the file at this call passes",
                "papers (file at this call)",
            ],
            [
                [b, c["n_first_pass"], c["n_at_budget"], ", ".join(c["at_budget"])]
                for b, c in a["budget_curve"].items()
                if int(b) <= budget
            ],
        )
        fd, c = a["fidelity"], a["cost"]
        cost = (
            f"${c['total_cost_usd']}" if c["total_cost_usd"] is not None else "not billed per token"
        )
        L += [
            "### Fidelity and cost",
            "",
            f"- passes {fd['pass']}; referee verdict on the scored file for "
            f"{fd['pass_with_referee_verdict']}; "
            f"no physics-changing finding: {len(fd['pass_no_physics_change'])} "
            f"({', '.join(fd['pass_no_physics_change'])}); "
            f"physics-changing: {', '.join(fd['pass_physics_changing']) or 'none'}; "
            f"no verdict the script can read: {', '.join(fd['pass_not_reviewed']) or 'none'}",
            f"- UFO of the scored file inspected for {fd['pass_ufo_inspected']} passes; a new "
            "particle with no vertex: "
            + (
                "; ".join(
                    f"{p} ({', '.join(v)})"
                    for p, v in fd["pass_with_a_new_particle_without_vertex"].items()
                )
                or "none"
            )
            + f"; passes with no physics-changing finding and every new particle in a vertex: "
            f"{len(fd['pass_faithful_and_all_new_particles_interact'])}",
            "- probe calls (not counted as passes): "
            + ("; ".join(f"{p} calls {v}" for p, v in a["probes"].items()) or "none"),
            f"- total input tokens {c['total_input']:,}, output {c['total_output']:,}, cost {cost}",
            f"- per pass: input {c['input_per_pass']:,}, output {c['output_per_pass']:,}"
            + (
                f", ${c['cost_per_pass_usd']}; per pass without a physics-changing finding "
                f"${c.get('cost_per_faithful_pass_usd')}"
                if c["cost_per_pass_usd"] is not None
                else ""
            ),
            "",
        ]
    L += ["## Equal-budget comparison (cc_sonnet_harness cut at budget B)", ""]
    L += _table(
        ["comparison", "cc", "other", "cc only", "other only", "exact McNemar p"],
        [
            [k, v["cc"], v["other"], v["cc_only"], v["other_only"], v["p"]]
            for k, v in res["paired"].items()
            if "at_budget" in k
        ],
    )
    L += [
        "## What a feedback loop could have seen in the first drafts",
        "",
        "The first draft is the scored file of a one-shot arm, or the file at the first validate "
        "call of a loop arm. "
        "A failing draft is seen by a feedback level when at least one of its failing items is "
        "in that level's report.",
        "",
    ]
    levels = list(FEEDBACK_SEES)
    L += _table(
        [
            "arm",
            "drafts",
            "failing",
            *[f"{x}: some / every item" for x in levels],
            f"{levels[1]} misses a failing check in",
        ],
        [
            [
                arm,
                v["drafts"],
                v["failing"],
                *[f"{v[x]['sees_some']} / {v[x]['sees_every_item']}" for x in levels],
                ", ".join(v[levels[1]]["blind_to"] + v[levels[1]]["partly_blind_to"]),
            ]
            for arm, v in ((arm, res["arms"][arm]["first_draft_visibility"]) for arm in res["arms"])
        ],
    )
    for arm in ONE_SHOT_ARMS:
        a = res["arms"][arm]
        lo = a["lint_only"]
        L += [
            f"## Lint alone on {arm}",
            "",
            f"{lo['scored']} scored files, {lo['failing']} fail. The lint names at least one "
            "failing item in "
            f"{lo['failing_with_a_hit']}; names every failing item in "
            f"{len(lo['failing_all_failures_flagged'])} "
            f"({', '.join(lo['failing_all_failures_flagged']) or 'none'}); has no error-level "
            "finding on "
            f"{len(lo['failing_no_finding'])} ({', '.join(lo['failing_no_finding']) or 'none'}). "
            "Passing files with an "
            f"error-level finding: {', '.join(lo['passing_with_false_alarm']) or 'none'}.",
            "",
        ]
        L += _table(
            ["item", "files failing it", "of which the lint flags that item"],
            [[i, lo["failing_by_item"][i], lo["hit_by_item"][i]] for i in ITEMS],
        )
        L += _table(
            ["paper", "scored", "failing items", "lint hits", "missed", "false alarms", "rules"],
            [
                [
                    x["paper"],
                    x["score_stage"],
                    ", ".join(x["failing"]),
                    ", ".join(x["hit"]),
                    ", ".join(x["missed"]),
                    ", ".join(x["false_alarm"]),
                    ", ".join(x["rules"]),
                ]
                for x in lo["rows"]
            ],
        )
        c = a["cost"]
        if c["runs_with_usage"]:
            L += [
                f"Tokens ({c['runs_with_usage']} runs with usage): input {c['total_input']:,}, "
                f"output {c['total_output']:,}; "
                f"per pass: "
                + (
                    f"input {c['input_per_pass']:,}, output {c['output_per_pass']:,}"
                    if c["input_per_pass"]
                    else "no pass"
                ),
                "",
            ]
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument(
        "--runs",
        default=os.environ.get(
            "PI_HARNESS_RUNS", str(Path.home() / "Documents/Github/heptapod/eval/benchmark_runs")
        ),
    )
    ap.add_argument("--out", default=str(HERE))
    ap.add_argument(
        "--scored-ufo",
        action="append",
        default=[],
        metavar="ARM=DIR",
        help="a local_rescore.py output directory for an arm: the UFOs of its scored files",
    )
    args = ap.parse_args()
    res = analyse(
        Path(args.runs), {k: Path(v) for k, v in (x.split("=", 1) for x in args.scored_ufo)}
    )
    out = Path(args.out)
    (out / "retro.json").write_text(json.dumps(res, indent=1, default=str))
    (out / "RETRO.md").write_text(render(res))
    print(f"wrote {out / 'retro.json'} and {out / 'RETRO.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
