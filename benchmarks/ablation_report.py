#!/usr/bin/env python3
"""
# ablation_report.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Compare rerun variants side by side: the physicist findings (deterministic
predicates), the validation chain, and the reference scores, per model and
per seed, then aggregated per variant.

    python eval/benchmark_runs/ablation_report.py \
        --variants v1,v2,v3_tools,v3_notools,v3txt_tools \
        --pages Top-Philic-Zprime,368sextets,EffLRSM,GeneralU1 --seeds 2

Reads <page>/rerun/<variant>/s<k>/run.json (written by rerun_extract.py) and
re-runs the predicates on the .fr that exists on disk, so a predicate added
after a run still scores that run. Reference scores use the same scorer as
the fleet (eval.reference_bench.score) against db_candidates.json.

Writes ablation_report.json and ablation_report.md next to this file.
Nothing here asks a model whether it succeeded.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(HERE))

from eval.reference_bench import score  # noqa: E402
import rerun_predicates  # noqa: E402

SM_FR = str(REPO / "tools" / "feynrules" / "test_files" / "models" / "SM.fr")


def _mean(xs):
    xs = [x for x in xs if isinstance(x, (int, float))]
    return round(sum(xs) / len(xs), 3) if xs else None


def _frac(n, d):
    return f"{n}/{d}" if d else "—"


def collect(page: str, variant: str, seed: int, cand: dict) -> dict:
    d = HERE / page / "rerun" / variant / f"s{seed}"
    row = {"page": page, "variant": variant, "seed": seed, "status": "no_run"}
    run = d / "run.json"
    if not run.is_file():
        return row
    r = json.loads(run.read_text())
    a = r.get("agent") or {}
    # Read the chain result from validation.json rather than from run.json.
    # run.json is rewritten by whichever stage ran last — `subagent_bench
    # ingest` writes the agent facts alone, and a `--no-validate` pass writes
    # the render alone — so trusting it silently dropped rows that had in fact
    # compiled and passed, and the aggregate undercounted every arm driven
    # through the subagent path.
    v = r.get("validation") or {}
    vfile = d / "validation.json"
    if not v and vfile.is_file():
        try:
            v = json.loads(vfile.read_text())
        except (OSError, json.JSONDecodeError):
            v = {}
    row.update({
        "status": "ran",
        "mode": r.get("mode") or a.get("mode") or "tools",
        "paper_source": r.get("paper_source") or "txt",
        # How the agent stage was driven, and whether its tool restriction was
        # enforced by the engine or only instructed and then audited. The CLI
        # arm passes --allowedTools/--tools ''; the subagent arm cannot, so it
        # is told the policy and the transcript is checked afterwards.
        "engine": a.get("engine", "claude-cli"),
        "tool_policy": a.get("tool_policy", "enforced"),
        "audit_ok": a.get("audit_ok"),
        "audit_problems": a.get("audit_problems") or [],
        "agent_ok": a.get("ok"), "timed_out": a.get("timed_out"),
        "seconds": a.get("seconds"), "n_tool_calls": a.get("n_tool_calls"),
        "read_paper": a.get("read_paper"), "paper_inlined": a.get("paper_inlined", False),
        "contaminated": a.get("contaminated"),
        # Likewise: the .fr on disk is the fact, not run.json's memory of it.
        "rendered": (d / "model" / f"{page}_gen.fr").is_file(),
        "render_reason": (r.get("render") or {}).get("reason"),
        "validated": bool(v),
        "lag_status": v.get("status"),
        "compile_ok": v.get("compile_ok"), "compile_seconds": v.get("seconds"),
        "checks": v.get("checks"),
        "checks_all": bool(v.get("checks")) and all((v.get("checks") or {}).values()),
        "madgraph_import_ok": v.get("madgraph_import_ok"),
        "full_chain_pass": v.get("full_chain_pass"),
    })
    fr = d / "model" / f"{page}_gen.fr"
    if fr.is_file():
        text = fr.read_text(errors="replace")
        preds = {}
        for name, fn in rerun_predicates.PREDICATES.get(page, []):
            try:
                ok, detail = fn(text)
            except Exception as e:                          # noqa: BLE001
                ok, detail = False, f"predicate raised {type(e).__name__}: {e}"
            preds[name] = {"resolved": bool(ok), "detail": detail}
        row["predicates"] = preds
        row["predicates_all"] = bool(preds) and all(p["resolved"] for p in preds.values())
        try:
            s = score(str(fr), str(REPO / cand["reference_fr"]), sm_fr=SM_FR)
            nf = s["n_fields"]
            n_gen = nf.get("generated") if isinstance(nf, dict) else nf
            if cand["n_new_fields"]:
                row.update({"field_f1": s["field_signature"]["f1"],
                            "qn_f1": s["quantum_number_values"]["f1"],
                            "n_fields": n_gen, "n_ref_fields": cand["n_new_fields"]})
            else:
                row.update({"field_f1": None, "qn_f1": None, "n_fields": n_gen,
                            "n_ref_fields": 0})
            row["param_jaccard"] = s["parameter_name_jaccard"]
        except Exception as e:                              # noqa: BLE001
            row["score_error"] = f"{type(e).__name__}: {str(e)[:120]}"
    return row


def aggregate(rows: list) -> dict:
    ran = [r for r in rows if r["status"] == "ran"]
    scored = [r for r in ran if isinstance(r.get("field_f1"), (int, float))]
    val = [r for r in ran if r.get("validated")]
    return {
        "n_runs": len(ran),
        "agent_ok": sum(1 for r in ran if r.get("agent_ok")),
        "read_paper": sum(1 for r in ran if r.get("read_paper")),
        "contaminated": sum(1 for r in ran if r.get("contaminated")),
        "rendered": sum(1 for r in ran if r.get("rendered")),
        "predicates_all": sum(1 for r in ran if r.get("predicates_all")),
        "n_validated": len(val),
        "compiled": sum(1 for r in val if r.get("compile_ok")),
        "checks_all": sum(1 for r in val if r.get("checks_all")),
        "madgraph": sum(1 for r in val if r.get("madgraph_import_ok")),
        "full_chain": sum(1 for r in val if r.get("full_chain_pass")),
        "mean_field_f1": _mean([r.get("field_f1") for r in scored]),
        "mean_qn_f1": _mean([r.get("qn_f1") for r in scored]),
        "n_scored": len(scored),
        "mean_agent_seconds": _mean([r.get("seconds") for r in ran]),
        "mean_tool_calls": _mean([r.get("n_tool_calls") for r in ran]),
        "mode": sorted({r.get("mode") for r in ran}),
        "paper_source": sorted({r.get("paper_source") for r in ran}),
        "engine": sorted({r.get("engine") for r in ran if r.get("engine")}),
        "tool_policy": sorted({r.get("tool_policy") for r in ran if r.get("tool_policy")}),
        "audit_failures": sum(1 for r in ran if r.get("audit_ok") is False),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variants", required=True, help="comma-separated variant labels")
    ap.add_argument("--pages", required=True, help="comma-separated pages")
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("--out", default="ablation_report", help="basename for .json/.md")
    args = ap.parse_args()

    variants = [v for v in args.variants.split(",") if v]
    pages = [p for p in args.pages.split(",") if p]
    cands = {c["page"]: c for c in json.loads((HERE / "db_candidates.json").read_text())["candidates"]}

    rows = [collect(p, v, k, cands[p]) for v in variants for p in pages
            for k in range(1, args.seeds + 1)]
    agg = {v: aggregate([r for r in rows if r["variant"] == v]) for v in variants}

    # per-finding table: model x predicate, cell = resolved seeds / seeds that produced a file
    findings = []
    for p in pages:
        for name, _fn in rerun_predicates.PREDICATES.get(p, []):
            cell = {}
            for v in variants:
                sel = [r for r in rows if r["variant"] == v and r["page"] == p and r.get("predicates")]
                n_ok = sum(1 for r in sel if r["predicates"].get(name, {}).get("resolved"))
                cell[v] = _frac(n_ok, len(sel))
            findings.append({"page": p, "finding": name, **cell})

    out = {"variants": variants, "pages": pages, "seeds": args.seeds,
           "aggregate": agg, "findings": findings, "rows": rows}
    (HERE / f"{args.out}.json").write_text(json.dumps(out, indent=1, default=str))

    # Headline, generated rather than hand-copied, so no number can drift.
    n_findings = len(findings)
    head = ["# Rerun ablation report\n",
            f"Variants: {', '.join(variants)}. Models: {', '.join(pages)}. "
            f"Seeds per model: {args.seeds}.\n",
            "## Headline\n",
            "| variant | findings resolved | full chain | mean field F1 |",
            "|---|---|---|---|"]
    for v in variants:
        a = agg[v]
        n = a["n_runs"]
        cells = [v, _frac(a["predicates_all"], n),
                 _frac(a["full_chain"], a["n_validated"]),
                 str(a["mean_field_f1"])]
        head.append("| " + " | ".join(cells) + " |")
    head.append("\n*findings resolved* counts runs where every predicate for that model passed; "
                f"there are {n_findings} predicates across {len(pages)} models. *full chain* is "
                "FeynRules compile + all three consistency checks + MadGraph import, over the runs "
                "that reached validation.\n")

    md = head + [
          "## Physicist findings (deterministic predicates; resolved seeds / seeds with a file)\n",
          "| model | finding | " + " | ".join(variants) + " |",
          "|---|---|" + "---|" * len(variants)]
    for f in findings:
        md.append(f"| {f['page']} | {f['finding']} | " + " | ".join(f[v] for v in variants) + " |")

    md += ["\n## Validation chain and reference score, per run\n",
           "| model | seed | variant | mode/source | agent | tools | paper read | tainted | rendered | predicates | lag | compile | checks H/K/M | MG5 | full chain | field F1 | QN F1 | fields gen/ref |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    def _num(x):
        return f"{x:.2f}" if isinstance(x, (int, float)) else "—"

    def _val(r, key):
        return str(r.get(key)) if r.get("validated") else "—"

    for r in rows:
        if r["status"] != "ran":
            md.append(f"| {r['page']} | {r['seed']} | {r['variant']} | — | no run |"
                      + " |" * 13)
            continue
        ch = r.get("checks") or {}
        chs = "".join("✓" if ch.get(k) else ("✗" if k in ch else "·")
                      for k in ("hermiticity", "kinetic_terms", "mass_spectrum")) if ch else "—"
        preds = r.get("predicates") or {}
        ps = ("—" if not preds else
              f"{sum(1 for p in preds.values() if p['resolved'])}/{len(preds)}")
        agent = "ok" if r.get("agent_ok") else ("timeout" if r.get("timed_out") else "fail")
        paper = "inlined" if r.get("paper_inlined") else str(r.get("read_paper"))
        cells = [r["page"], str(r["seed"]), r["variant"],
                 f"{r.get('mode')}/{r.get('paper_source')}", agent,
                 str(r.get("n_tool_calls")), paper, str(r.get("contaminated")),
                 str(r.get("rendered")), ps, r.get("lag_status") or "—",
                 _val(r, "compile_ok"), chs, _val(r, "madgraph_import_ok"),
                 _val(r, "full_chain_pass"), _num(r.get("field_f1")), _num(r.get("qn_f1")),
                 f"{r.get('n_fields', '—')}/{r.get('n_ref_fields', '—')}"]
        md.append("| " + " | ".join(cells) + " |")

    md += ["\n## Aggregate per variant\n",
           "| variant | mode | source | engine | tool policy | runs | agent ok | paper read | tainted | audit fail | rendered | all findings resolved | validated | compiled | all checks | MG5 | full chain | mean field F1 (n) | mean QN F1 | mean tool calls |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for v in variants:
        a = agg[v]
        n = a["n_runs"]
        md.append(f"| {v} | {'/'.join(a['mode'])} | {'/'.join(a['paper_source'])} | "
                  f"{'/'.join(a['engine']) or '—'} | {'/'.join(a['tool_policy']) or '—'} | {n} | "
                  f"{_frac(a['agent_ok'], n)} | {_frac(a['read_paper'], n)} | {a['contaminated']} | "
                  f"{a['audit_failures']} | "
                  f"{_frac(a['rendered'], n)} | {_frac(a['predicates_all'], n)} | {a['n_validated']} | "
                  f"{_frac(a['compiled'], a['n_validated'])} | {_frac(a['checks_all'], a['n_validated'])} | "
                  f"{_frac(a['madgraph'], a['n_validated'])} | {_frac(a['full_chain'], a['n_validated'])} | "
                  f"{a['mean_field_f1']} ({a['n_scored']}) | {a['mean_qn_f1']} | "
                  f"{a['mean_tool_calls']} |")
    md.append("\n`tool policy` says how the agent's tool restriction was imposed: `enforced` when the "
              "engine was started with `--allowedTools` / `--tools ''`, `instructed+audited` when the "
              "policy was given in the prompt and the transcript checked afterwards (`audit fail` counts "
              "runs that broke it). Predicates are evidence, not verdicts: a physicist reading the file decides. "
              "Field F1 compares new-field signatures with the FeynRules-DB reference; it is undefined "
              "for references with no new fields.\n")
    (HERE / f"{args.out}.md").write_text("\n".join(md))
    print(json.dumps(agg, indent=1))
    print(f"wrote {HERE / (args.out + '.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
