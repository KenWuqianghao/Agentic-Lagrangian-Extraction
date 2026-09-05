#!/usr/bin/env python3
"""
# rerun_score.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Score a sandboxed rerun (rerun_extract.py) against the physicist references
with the same scorer the original fleet used (eval.reference_bench.score), and
put the original fleet's number beside it.

    python eval/benchmark_runs/rerun_score.py --variant v2 [--seed 1]

The point of the side-by-side: the original fleet could read the reference
files (contamination_audit.py: 18 of 28 runs did). A drop in field F1 for
one of those 18 is not a regression of the agent — it is the first honest
measurement.

Writes rerun_score_<variant>.json and .md next to this file.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))

from eval.reference_bench import score  # noqa: E402

SM_FR = str(REPO / "tools" / "feynrules" / "test_files" / "models" / "SM.fr")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", required=True)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()

    cands = json.loads((HERE / "db_candidates.json").read_text())["candidates"]
    orig = {r["page"]: r for r in json.loads(
        (HERE / "db_benchmark_report.json").read_text()).get("rows", [])} \
        if (HERE / "db_benchmark_report.json").is_file() else {}
    audit = {r["page"]: r for r in json.loads(
        (HERE / "contamination_audit.json").read_text())} \
        if (HERE / "contamination_audit.json").is_file() else {}

    rows = []
    for c in cands:
        page = c["page"]
        d = HERE / page / "rerun" / args.variant / f"s{args.seed}"
        row = {"page": page, "variant": args.variant, "seed": args.seed,
               "original_verdict": (audit.get(page) or {}).get("verdict"),
               "original_field_f1": (orig.get(page) or {}).get("field_f1"),
               "original_qn_f1": (orig.get(page) or {}).get("qn_f1")}
        run = d / "run.json"
        if not run.is_file():
            row["status"] = "no_run"; rows.append(row); continue
        r = json.loads(run.read_text())
        a = r.get("agent") or {}
        row.update({"read_paper": a.get("read_paper"), "contaminated": a.get("contaminated"),
                    "seconds": a.get("seconds"), "n_tool_calls": a.get("n_tool_calls")})
        fr = d / "model" / f"{page}_gen.fr"
        if not fr.is_file():
            row["status"] = "render_failed"
            row["reason"] = (r.get("render") or {}).get("reason")
            rows.append(row); continue
        try:
            s = score(str(fr), str(REPO / c["reference_fr"]), sm_fr=SM_FR)
        except Exception as e:                              # noqa: BLE001
            row["status"] = f"scoring_failed: {type(e).__name__}: {str(e)[:120]}"
            rows.append(row); continue
        if not c["n_new_fields"]:
            # An EFT add-on with no new particle class: the field-signature
            # scorer has nothing to match, so F1 is undefined, not zero.
            row.update({"status": "scored_no_new_fields", "field_f1": None, "qn_f1": None,
                        "param_jaccard": s["parameter_name_jaccard"], "n_fields": s["n_fields"],
                        "n_ref_fields": 0})
            rows.append(row); continue
        row.update({"status": "scored",
                    "field_f1": s["field_signature"]["f1"],
                    "field_precision": s["field_signature"]["precision"],
                    "field_recall": s["field_signature"]["recall"],
                    "qn_f1": s["quantum_number_values"]["f1"],
                    "param_jaccard": s["parameter_name_jaccard"],
                    "n_fields": s["n_fields"], "n_ref_fields": c["n_new_fields"],
                    "missed": [x for x in s["reference_field_signatures"]
                               if x not in s["generated_field_signatures"]][:12]})
        rows.append(row)

    scored = [r for r in rows if r.get("status") == "scored"]
    def mean(k, sel):
        v = [r[k] for r in sel if isinstance(r.get(k), (int, float))]
        return round(sum(v) / len(v), 3) if v else None
    clean_orig = [r for r in scored if r["original_verdict"] == "clean"]
    tainted_orig = [r for r in scored if r["original_verdict"] == "OWN REFERENCE READ"]
    summary = {
        "n_candidates": len(rows), "n_scored": len(scored),
        "n_read_paper": sum(1 for r in rows if r.get("read_paper")),
        "n_contaminated": sum(1 for r in rows if r.get("contaminated")),
        "mean_field_f1_sandboxed": mean("field_f1", scored),
        "mean_field_f1_original_same_models": mean("original_field_f1", scored),
        "mean_field_f1_sandboxed_where_original_clean": mean("field_f1", clean_orig),
        "mean_field_f1_original_where_original_clean": mean("original_field_f1", clean_orig),
        "mean_field_f1_sandboxed_where_original_read_own_ref": mean("field_f1", tainted_orig),
        "mean_field_f1_original_where_original_read_own_ref": mean("original_field_f1", tainted_orig),
    }
    out = {"summary": summary, "rows": rows}
    (HERE / f"rerun_score_{args.variant}.json").write_text(json.dumps(out, indent=1))

    md = [f"# Sandboxed rerun `{args.variant}` vs the original fleet\n",
          "| model | original run | field F1 orig | field F1 sandboxed | QN F1 sandboxed | fields (gen/ref) | read paper | tainted | status |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        f = lambda k: ("—" if r.get(k) is None else f"{r[k]:.2f}") if isinstance(r.get(k), (int, float)) else (r.get(k) or "—")
        md.append(f"| {r['page']} | {r.get('original_verdict') or '—'} | {f('original_field_f1')} | {f('field_f1')} | {f('qn_f1')} | "
                  f"{r.get('n_fields','—')}/{r.get('n_ref_fields','—')} | {r.get('read_paper','—')} | {r.get('contaminated','—')} | {r.get('status')} |")
    md.append("\n## Summary\n")
    for k, v in summary.items():
        md.append(f"- **{k}**: {v}")
    (HERE / f"rerun_score_{args.variant}.md").write_text("\n".join(md) + "\n")
    print(json.dumps(summary, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
