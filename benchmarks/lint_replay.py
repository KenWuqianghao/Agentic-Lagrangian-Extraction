#!/usr/bin/env python3
"""Replay fr_lint over every stored agent .fr that has a validation verdict
(option E) and score each rule against the stage it predicts.

Inventory: <page>/rerun/<variant>/s<k>/model/*.fr with validation.json, and
<page>/repair_corrected/round<k>/model.fr with the rows of
repair_repair_corrected_report.json. Both were validated with the corrected
harness (checks read from return values, 2026-09-13 onward).

Outcome per file, in stage order:
  compile_failed | compile_timeout | harness (no/ambiguous total) |
  checks_failed | mg5_failed | pass

A rule that predicts stage S is a true positive on a file when the file
failed at S or at an earlier stage that hides S (a compile failure hides a
MadGraph failure). Precision is reported both ways: strict (failed exactly at
the predicted stage) and reached (failed at or before it).
"""

from __future__ import annotations

import glob
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fr_lint  # noqa: E402

STAGES = ["harness", "compile", "checks", "mg5", "pass"]


def outcome(v: dict) -> dict:
    """Which stages the file reached and which it failed. checks and mg5 are
    independent: the harness imports the UFO into MadGraph even when a
    FeynRules check fails."""
    st = v.get("status")
    o = {"harness": False, "compile": None, "checks": None, "mg5": None}
    if st in ("no_lagrangian_symbol", "ambiguous_lagrangian_symbol"):
        o["harness"] = True
        o["label"] = "harness"
        return o
    o["compile"] = bool(v.get("compile_ok")) and not v.get("timed_out")
    if not o["compile"]:
        o["label"] = "compile_timeout" if (v.get("timed_out") or st == "compile_timeout") else "compile_failed"
        return o
    checks = v.get("checks") or {}
    o["checks"] = not any(x == "fail" for x in checks.values())
    o["mg5"] = bool(v.get("madgraph_import_ok"))
    o["label"] = "pass" if (o["checks"] and o["mg5"]) else \
        ("checks+mg5_failed" if not o["checks"] and not o["mg5"] else ("checks_failed" if not o["checks"] else "mg5_failed"))
    return o


def failed(o: dict, stage: str) -> bool:
    if stage == "harness":
        return o["harness"]
    if stage == "compile":
        return o["compile"] is False
    return o.get(stage) is False


def reached(o: dict, stage: str) -> bool:
    if stage in ("harness", "compile"):
        return True
    return o["compile"] is True


def inventory():
    items = []
    for vpath in sorted(glob.glob(str(HERE / "*/rerun/*/s*/validation.json"))):
        d = os.path.dirname(vpath)
        frs = sorted(glob.glob(os.path.join(d, "model", "*.fr")))
        if not frs:
            continue
        v = json.load(open(vpath))
        rel = os.path.relpath(d, HERE)
        items.append({"id": rel, "fr": frs[0], "outcome": outcome(v), "checks": v.get("checks") or {},
                      "source": "rerun"})
    rep = json.load(open(HERE / "repair_repair_corrected_report.json"))["results"]
    for r in rep:
        for rd in r["rounds"]:
            local = HERE / r["page"] / "repair_corrected" / f"round{rd['round']}" / "model.fr"
            if not local.is_file():
                continue
            v = dict(rd)
            if "madgraph_import_ok" not in v:
                v["madgraph_import_ok"] = bool(v.get("full_pass")) or v.get("mg5_ok")
            items.append({"id": f"{r['page']}/repair_corrected/round{rd['round']}", "fr": str(local),
                          "outcome": outcome(v), "checks": v.get("checks") or {}, "source": "repair"})
    return items


def main():
    items = inventory()
    rows = []
    for it in items:
        fs = fr_lint.lint_file(it["fr"])
        it["findings"] = [f.__dict__ for f in fs]
        rows.append(it)
    (HERE / "lint_replay.json").write_text(json.dumps(rows, indent=1))

    n = len(rows)
    oc = Counter(r["outcome"]["label"] for r in rows)
    lines = ["# Lint replay over stored agent models", "",
             f"{n} files ({dict(Counter(r['source'] for r in rows))}), outcomes: " +
             ", ".join(f"{k} {v}" for k, v in sorted(oc.items())), "",
             "A rule predicts one stage. Precision counts only files that REACHED that stage "
             "(compiled, for checks and MadGraph); a file that never compiled says nothing "
             "about its UFO.", ""]

    lines += ["## Per rule", "", "| rule | stage | files flagged | reached the stage | failed it | precision |",
              "|---|---|---|---|---|---|"]
    per_rule = defaultdict(list)
    for r in rows:
        seen = set()
        for f in r["findings"]:
            if f["rule"] in seen:
                continue
            seen.add(f["rule"])
            per_rule[(f["rule"], f["stage"])].append(r["outcome"])
    for (rule, stage), outs in sorted(per_rule.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        nf = len(outs)
        if stage == "warn":
            lines.append(f"| {rule} | warn | {nf} | — | — | — |")
            continue
        rch = [o for o in outs if reached(o, stage)]
        fl = sum(1 for o in rch if failed(o, stage))
        prec = f"{fl/len(rch):.2f}" if rch else "n/a"
        lines.append(f"| {rule} | {stage} | {nf} | {len(rch)} | {fl} | {prec} |")

    lines += ["", "## Recall per failure stage", "", "| failure stage | files failing it | with a lint predicting it | with any error-level lint |", "|---|---|---|---|"]
    for stage in ("harness", "compile", "checks", "mg5"):
        fails = [r for r in rows if failed(r["outcome"], stage)]
        if not fails:
            continue
        hit = sum(1 for r in fails if any(f["stage"] == stage for f in r["findings"]))
        anyhit = sum(1 for r in fails if any(f["stage"] != "warn" for f in r["findings"]))
        lines.append(f"| {stage} | {len(fails)} | {hit} | {anyhit} |")
    passes = [r for r in rows if r["outcome"]["label"] == "pass"]
    fp = sum(1 for r in passes if any(f["stage"] != "warn" for f in r["findings"]))
    lines.append(f"| pass (false positives) | {len(passes)} | — | {fp} |")

    # what error-level lints say about passing files
    lines += ["", "## Error-level lints on files that passed the whole chain", ""]
    for r in passes:
        errs = [f for f in r["findings"] if f["stage"] != "warn"]
        if errs:
            lines.append(f"- `{r['id']}`: " + "; ".join(f"{f['rule']} ({f['message'][:90]})" for f in errs))
    # the mass-mixing lint against the mass_diagonal verdict
    mix = [r for r in rows if any(f["rule"] == "mixing_in_definitions" for f in r["findings"])]
    md_fail = [r for r in rows if r["checks"].get("mass_diagonal") == "fail"]
    lines += ["", "## mixing_in_definitions vs CheckDiagonalMassTerms", "",
              f"- files flagged: {len(mix)}; of those with a check verdict, mass_diagonal fail: "
              f"{sum(1 for r in mix if r['checks'].get('mass_diagonal')=='fail')}, pass: "
              f"{sum(1 for r in mix if r['checks'].get('mass_diagonal')=='pass')}",
              f"- files with mass_diagonal fail: {len(md_fail)}; flagged by the lint: "
              f"{sum(1 for r in md_fail if any(f['rule']=='mixing_in_definitions' for f in r['findings']))}"]
    out = "\n".join(lines) + "\n"
    (HERE / "lint_replay.md").write_text(out)
    print(out)


if __name__ == "__main__":
    main()
