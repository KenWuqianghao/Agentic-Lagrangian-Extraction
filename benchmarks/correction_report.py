#!/usr/bin/env python3
"""Build the 2026-09-13 check-verdict correction from the re-score ledger.

rescore_checks.py writes one JSONL line per run: the stored verdicts, the new
return-value verdicts, and the Lagrangian expression it used. This turns that
ledger into CORRECTION_2026-09-13.{md,json}. It reads nothing else, so the
correction can be rebuilt and checked from the committed ledger alone.

    python correction_report.py --ledger rescore_ledger_2026-09-13.jsonl
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYS = ("hermiticity", "kinetic_diagonal", "mass_diagonal", "mass_spectrum")
SYM = {"pass": "✓", "fail": "✗", "inconclusive": "?"}


def all_pass(checks: dict | None) -> bool:
    checks = checks or {}
    return all(checks.get(k) == "pass" for k in KEYS)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    entries = [json.loads(l) for l in Path(a.ledger).read_text().splitlines() if l.strip()]

    arms: dict = defaultdict(lambda: {"runs": 0, "rescored": 0, "old_full": 0, "new_full": 0})
    verdicts: Counter = Counter()
    flips, doubled, runs, report_rows = [], [], [], []
    for e in entries:
        rescored = "new_checks" in e
        if rescored and not e.get("lagrangian_expression", "").startswith("LSM + "):
            doubled.append(e["run"])
        if ":" in e["run"]:                                   # a report row
            report_rows.append(e)
            if rescored:
                runs.append(e)
            continue
        arm = e["run"].split("/rerun/")[1].split("/")[0]
        s = arms[arm]
        s["runs"] += 1
        old_full = bool(e.get("old_full_chain_pass"))
        new_full = bool(e.get("new_full_chain_pass")) if rescored else old_full
        s["old_full"] += old_full
        s["new_full"] += new_full
        if not rescored:
            continue
        s["rescored"] += 1
        for k in KEYS:
            verdicts[(k, (e["new_checks"] or {}).get(k, "not run"))] += 1
        if old_full != new_full:
            flips.append(e)
        runs.append(e)

    rep_old = sum(1 for e in report_rows if e.get("old_full_chain_ok"))
    rep_new = sum(1 for e in report_rows
                  if (e.get("new_full_chain_ok") if "new_checks" in e else e.get("old_full_chain_ok")))

    out = {"arms": arms, "verdict_tally": {f"{k}={v}": n for (k, v), n in sorted(verdicts.items())},
           "full_chain_flips": [e["run"] for e in flips],
           "lsm_counted_twice_before": doubled,
           "revalidation_report": {"rows": len(report_rows), "old_pass": rep_old, "new_pass": rep_new}}
    Path(a.out, "CORRECTION_2026-09-13.json").write_text(json.dumps(out, indent=2))

    md = ["# Correction 2026-09-13: FeynRules check verdicts", "",
          "Every FeynRules check verdict in this benchmark before 2026-09-13 was a pass "
          "unless the check crashed. The prose classifier (`tools/feynrules/wl_checks.py`) "
          "returned True on every branch, and none of its failure markers matched what "
          "FeynRules prints. Tony Menzo found this while reviewing heptapod-dev #15.", "",
          "A second defect was in the harness. The old generator always sent "
          "`LSM + <total>` to FeynRules. Some models already include `LSM` in their total, "
          "so those runs were checked and compiled with every Standard Model term counted twice.", "",
          "`rescore_checks.py` re-ran only the consistency checks on the same `.fr` and total, "
          "with the generator on heptapod `main` and `tools/feynrules/lagrangian_checks.py`. "
          "Each verdict now comes from the check's return value, and `LSM` is added only when "
          "the total does not already reach it. Every run's log is in its `checks.log`.", "",
          "The field-content scores and the physicist-finding predicates read the `.fr` text. "
          "They do not use these checks and do not change.", "",
          "## Full chain before and after, per arm", "",
          "Full chain means compiled, all four default checks pass, and MadGraph imports the UFO.", "",
          "| arm | runs | re-scored | full chain before | full chain after |",
          "|---|---|---|---|---|"]
    for arm in sorted(arms):
        s = arms[arm]
        md.append(f"| {arm} | {s['runs']} | {s['rescored']} | {s['old_full']}/{s['runs']} | "
                  f"**{s['new_full']}/{s['runs']}** |")
    if report_rows:
        md += ["", "## Repair loop (revalidation_report.json)", "",
               "| rows | full chain before | full chain after |", "|---|---|---|",
               f"| {len(report_rows)} | {rep_old} | **{rep_new}** |"]
    md += ["", "## New verdicts over the re-scored runs", "",
           "| check | pass | fail | inconclusive | not run |", "|---|---|---|---|---|"]
    for k in KEYS:
        md.append(f"| {k} | " + " | ".join(str(verdicts[(k, v)])
                  for v in ("pass", "fail", "inconclusive", "not run")) + " |")
    md += ["", "## Runs whose full-chain result changed", "",
           "| run | before | after | H / Kd / Md / S |", "|---|---|---|---|"]
    for e in flips + [r for r in report_rows if "new_checks" in r
                      and bool(r.get("old_full_chain_ok")) != bool(r.get("new_full_chain_ok"))]:
        before = e.get("old_full_chain_pass", e.get("old_full_chain_ok"))
        after = e.get("new_full_chain_pass", e.get("new_full_chain_ok"))
        md.append(f"| {e['run']} | {before} | {after} | "
                  + " ".join(SYM.get((e['new_checks'] or {}).get(k), "—") for k in KEYS) + " |")
    md += ["", "## Runs that had the Standard Model counted twice before", "",
           f"{len(doubled)} of {len(runs)} re-scored runs define a total that already contains "
           "`LSM`. Their earlier compile and checks used twice the SM Lagrangian. The new "
           "verdicts use the total alone. Their UFOs and MadGraph imports were not rebuilt.", ""]
    md += [f"- `{r}`" for r in doubled]
    md += ["", "`H / Kd / Md / S` is hermiticity, kinetic_diagonal, mass_diagonal, mass_spectrum: "
           "✓ pass, ✗ fail, ? inconclusive. Inconclusive never counts as a pass."]
    Path(a.out, "CORRECTION_2026-09-13.md").write_text("\n".join(md) + "\n")
    print(json.dumps({k: out[k] for k in ("arms", "revalidation_report")}, indent=1, default=dict))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
