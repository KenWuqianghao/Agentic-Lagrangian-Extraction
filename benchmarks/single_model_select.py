#!/usr/bin/env python3
"""
# single_model_select.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Turn the paper-classification output (one reader + two adversarial refuters
per paper, single_model_papers_raw.json) into the benchmark selection file
single_model_papers.json.

Two independent filters, because they answer different questions.

**Single-model.** Three votes per paper: the reader's ``single_model`` and
each refuter's ``corrected_single_model``. A paper is selected when every
vote cast agrees and at least two were cast. A split is ``contested`` and is
NOT selected: the whole point is that the extraction agent cannot mix up
which model to write, so a paper two careful readers disagree about does not
qualify. Fewer than two votes is ``undecided`` — the refuters did not finish.

**Scorable.** Separately: does the benchmark's own reference `.fr` actually
implement the paper's model? Three of the pairings do not, and a field-F1
against them measures nothing:

  * the reference implements a different paper's physics (``none``),
  * only a subset of the paper (``reference_is_subset``),
  * or a version of the paper the benchmark text is not.

A paper enters the rerun when it is single-model; it enters the *scored*
comparison only when it is also scorable. Both lists are written out, and
the physicists can override any row by hand.

    python eval/benchmark_runs/single_model_select.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Pairings the classification found broken, with the evidence in one line.
# Kept explicit rather than inferred from free text: a physicist must be able
# to read, check and edit this list.
BAD_PAIRINGS = {
    "LeptoQuark": "reference VLferm.fr is a vector-like-fermion add-on the paper never defines; "
                  "the paper's U1+Z'+G' model is in vector_LQ.fr/Zprime.fr/coloron.fr",
    "CHEIDI": "benchmark text is arXiv:1010.3251v2 (a FeynRules-WHIZARD interface paper, no model); "
              "HEIDI.fr implements the withdrawn v1 physics",
    "VLC_LN": "reference VLC.fr implements only a collider subset (pion + rho triplets) of the "
              "paper's L+N composite model",
    "topBSM": "reference now thu.fr (flavour-changing Higgs currents, 0 new fields); the old "
              "topBSM.fr pairing was a different paper",
    "MSSMD": "listed publication is a CMS search (CMS-HIG-18-003), not the paper that defines "
             "the 39-field MSSMD Lagrangian",
}


def main() -> int:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "single_model_papers_raw.json"
    data = json.loads(src.read_text())
    rows = []
    for r in data:
        c = r.get("classification") or {}
        rp, rr = r.get("refute_physics") or {}, r.get("refute_reference") or {}
        votes = [bool(c.get("single_model")) if c else None,
                 bool(rp.get("corrected_single_model")) if rp else None,
                 bool(rr.get("corrected_single_model")) if rr else None]
        cast = [v for v in votes if v is not None]
        n_yes = sum(1 for v in cast if v)
        unanimous = len(cast) >= 2 and n_yes in (0, len(cast))
        single = unanimous and n_yes == len(cast)
        ref_ok = (str(c.get("reference_implements") or "").strip().lower()
                  not in ("none", "unclear", "")) and r["page"] not in BAD_PAIRINGS
        rows.append({
            "page": r["page"],
            "single_model": single,
            "contested": len(cast) >= 2 and not unanimous,
            "undecided": len(cast) < 2,
            "votes_single": f"{n_yes}/{len(cast)}",
            "n_votes_cast": len(cast),
            "scorable": bool(single and ref_ok),
            "pairing_problem": BAD_PAIRINGS.get(r["page"]),
            "n_models_reader": c.get("n_models"),
            "n_models_refuters": [rp.get("corrected_n_models") if rp else None,
                                  rr.get("corrected_n_models") if rr else None],
            "model_names": c.get("model_names"),
            "reference_implements": c.get("reference_implements"),
            "reference_is_superset": c.get("reference_is_superset"),
            "confusion_risk": c.get("confusion_risk"),
            "reader_confidence": c.get("confidence"),
            "refuted_by": [k for k, v in (("physics", rp), ("reference", rr))
                           if v and v.get("refuted")],
            "evidence": (c.get("evidence") or [])[:4],
            "refuter_reasons": [x.get("reason") for x in (rp, rr) if x and x.get("refuted")],
            "notes": c.get("notes"),
        })
    rows.sort(key=lambda x: x["page"])
    sel = [x["page"] for x in rows if x["single_model"]]
    scorable = [x["page"] for x in rows if x["scorable"]]
    out = {
        "rule": ("single_model: every vote cast agrees and >= 2 were cast; "
                 "scorable: single_model AND the benchmark reference implements the paper's model"),
        "n_papers": len(rows), "n_selected": len(sel), "n_scorable": len(scorable),
        "selected": sel, "scorable": scorable,
        "contested": [x["page"] for x in rows if x["contested"]],
        "undecided": [x["page"] for x in rows if x["undecided"]],
        "multi_model": [x["page"] for x in rows
                        if not x["single_model"] and not x["contested"] and not x["undecided"]],
        "pairing_problems": {k: v for k, v in BAD_PAIRINGS.items()},
        "rows": rows,
    }
    (HERE / "single_model_papers.json").write_text(json.dumps(out, indent=1))

    md = ["# Which benchmark papers define exactly one model?\n",
          "One reader plus two adversarial refuters per paper (a physics-content lens and a "
          "reference-file lens). A paper is selected only when every vote cast agrees.\n",
          "`scorable` additionally requires that the benchmark's reference `.fr` implements the "
          "paper's model — five pairings do not, and a field-F1 against those measures nothing.\n",
          "| page | single model | scorable | votes | models (reader) | reference implements | confusion risk |",
          "|---|---|---|---|---|---|---|"]
    for x in rows:
        verdict = ("yes" if x["single_model"] else
                   "CONTESTED" if x["contested"] else
                   "undecided" if x["undecided"] else "no")
        names = "; ".join(x["model_names"] or [])[:80]
        md.append(f"| {x['page']} | {verdict} | {'yes' if x['scorable'] else 'no'} | "
                  f"{x['votes_single']} | {x['n_models_reader']}: {names} | "
                  f"{str(x['reference_implements'])[:70]} | {x['confusion_risk']} |")
    md.append(f"\n**Selected, single-model ({len(sel)}):** {', '.join(sel)}\n")
    md.append(f"**Of those, scorable against their reference ({len(scorable)}):** {', '.join(scorable)}\n")
    md.append("## Excluded, and why\n")
    for x in rows:
        if x["single_model"] and x["scorable"]:
            continue
        why = (x["pairing_problem"] if x["single_model"] else
               f"{x['n_models_reader']} models: " + "; ".join(x["model_names"] or [])[:160])
        state = ("contested" if x["contested"] else "undecided" if x["undecided"]
                 else "multi-model" if not x["single_model"] else "pairing")
        md.append(f"- **{x['page']}** ({state}): {why}")
    (HERE / "single_model_papers.md").write_text("\n".join(md) + "\n")
    print(json.dumps({k: out[k] for k in
                      ("n_selected", "n_scorable", "selected", "scorable",
                       "contested", "undecided", "multi_model")}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
