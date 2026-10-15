#!/usr/bin/env python3
"""Re-score stored benchmark runs with return-value check verdicts.

Every check verdict stored before 2026-09-13 came from a prose classifier that
could not report a failure: each branch of its classifier returned True, and
none of its failure markers matched what FeynRules prints. This script re-runs
only the consistency checks (ChecksOnly=true) on the exact .fr and Lagrangian
each run was scored with, and rewrites the verdicts and full_chain_pass in
place. The old values go to a JSONL correction ledger, one line per run, so the
change stays auditable and an interrupted pass resumes where it stopped.

With --report, it re-scores the rows of a report JSON instead (for example
revalidation_report.json, whose rows name the .fr by page and fr_source), and
recomputes the report's pass count.

Runs one model at a time. Never run two Wolfram jobs at once.
"""
import argparse
import json
import sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--harness", required=True, help="eval/benchmark_runs of a main checkout")
ap.add_argument("--root", required=True, help="benchmark tree holding the run dirs")
ap.add_argument("--ledger", required=True)
ap.add_argument("--timeout", type=int, default=1800)
ap.add_argument("--arms", default="v3_tools,v3_notools,v2,v1")
ap.add_argument("--limit", type=int, default=0)
ap.add_argument("--report", default="",
                help="re-score the rows of this report JSON (relative to --root)")
a = ap.parse_args()

harness = Path(a.harness).resolve()
sys.path.insert(0, str(harness.parent.parent))
sys.path.insert(0, str(harness))
import validation_benchmark as vb  # noqa: E402

root = Path(a.root).resolve()
ledger = Path(a.ledger)
done = set()
if ledger.is_file():
    done = {json.loads(line)["run"] for line in ledger.read_text().splitlines() if line.strip()}

def _log(entry: dict) -> None:
    with ledger.open("a") as fh:
        fh.write(json.dumps(entry) + "\n")


def rescore_report(rel_report: str) -> None:
    path = root / rel_report
    rep_d = json.loads(path.read_text())
    for row in rep_d["rows"]:
        key = f"{rel_report}:{row['page']}"
        if key in done:
            continue
        entry = {"run": key, "old_checks": row.get("checks"),
                 "old_full_chain_ok": row.get("full_chain_ok")}
        src = row.get("fr_source") or "one-shot"
        fr = (root / row["page"] / "model" / f"{row['page']}_gen.fr" if src == "one-shot"
              else root / row["page"] / src)
        if row.get("status") != "compiled" or not fr.is_file() or not row.get("lag_symbol"):
            entry["skipped"] = ("did not compile" if row.get("status") != "compiled"
                                else f"no .fr at {fr.relative_to(root)} or no Lagrangian")
            _log(entry)
            print(f"[rescore] skip {key}: {entry['skipped']}", flush=True)
            continue
        print(f"[rescore] {key} ({vb.lagrangian_expression(fr, row['lag_symbol'])}) ...", flush=True)
        res = vb.run_lagrangian_checks(fr, row["lag_symbol"], fr.parent / "checks.log", a.timeout)
        row["checks"] = res["checks"]
        row["checks_source"] = "lagrangian_checks"
        row["lagrangian_expression"] = res["lagrangian_expression"]
        row["checks_run"] = {k: res[k] for k in ("exit", "timed_out", "seconds")}
        row["full_chain_ok"] = bool(row.get("status") == "compiled"
                                    and row.get("madgraph_import_ok")
                                    and vb.all_checks_pass(row["checks"]))
        rep_d["n_pass"] = sum(1 for r in rep_d["rows"] if r.get("full_chain_ok"))
        path.write_text(json.dumps(rep_d, indent=2))
        entry.update({"new_checks": row["checks"], "new_full_chain_ok": row["full_chain_ok"],
                      "lagrangian_expression": res["lagrangian_expression"], **row["checks_run"]})
        _log(entry)
        print(f"[rescore]   -> {row['checks']} full_chain {entry['old_full_chain_ok']} -> "
              f"{row['full_chain_ok']} ({res['seconds']}s exit={res['exit']})", flush=True)
    print(f"[rescore] REPORT DONE {rel_report}: n_pass={rep_d['n_pass']}/{rep_d.get('n_scoreable')}",
          flush=True)


if a.report:
    rescore_report(a.report)
    raise SystemExit(0)

runs = []
for arm in a.arms.split(","):
    runs += sorted(p.parent for p in root.glob(f"*/rerun/{arm}/s*/validation.json"))

n = 0
for run in runs:
    rel = str(run.relative_to(root))
    if rel in done:
        continue
    d = json.loads((run / "validation.json").read_text())
    entry = {"run": rel, "old_checks": d.get("checks"),
             "old_full_chain_pass": d.get("full_chain_pass")}
    fr = sorted((run / "model").glob("*_gen.fr"))
    if not d.get("compile_ok") or not fr or not d.get("lag_symbol"):
        entry["skipped"] = "did not compile" if not d.get("compile_ok") else "no .fr or Lagrangian"
        with ledger.open("a") as fh:
            fh.write(json.dumps(entry) + "\n")
        print(f"[rescore] skip {rel}: {entry['skipped']}", flush=True)
        continue
    print(f"[rescore] {rel} ({vb.lagrangian_expression(fr[0], d['lag_symbol'])}) ...", flush=True)
    res = vb.run_lagrangian_checks(fr[0], d["lag_symbol"], run / "checks.log", a.timeout)
    d["checks"] = res["checks"]
    d["checks_source"] = "lagrangian_checks"
    d["checks_run"] = {k: res[k] for k in ("exit", "timed_out", "seconds")}
    d["lagrangian_expression"] = res["lagrangian_expression"]
    d["full_chain_pass"] = bool(d.get("compile_ok") and vb.all_checks_pass(d["checks"])
                                and d.get("madgraph_import_ok"))
    (run / "validation.json").write_text(json.dumps(d, indent=2))
    entry.update({"new_checks": d["checks"], "new_full_chain_pass": d["full_chain_pass"],
                  "lagrangian_expression": res["lagrangian_expression"],
                  **d["checks_run"]})
    with ledger.open("a") as fh:
        fh.write(json.dumps(entry) + "\n")
    print(f"[rescore]   -> {d['checks']} full_chain {entry['old_full_chain_pass']} -> "
          f"{d['full_chain_pass']} ({res['seconds']}s exit={res['exit']})", flush=True)
    n += 1
    if a.limit and n >= a.limit:
        break
print("[rescore] PASS DONE", flush=True)
