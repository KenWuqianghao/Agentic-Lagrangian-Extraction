#!/usr/bin/env python3
"""
Assemble the physicist review bundle from benchmark output already on disk.

Produces `review_bundle/` and `review_bundle.zip`:

    README.md                        inventory and reading order
    CONVENTION_DISAGREEMENTS.md      graded reconstruction-vs-paper rows
    REPAIR_BENCHMARK_ANALYSIS.md     full write-up and error taxonomy
    reports/                         the four machine-generated reports
    passing/<model>/                 validated .fr + one PDF      (18 models)
    failing/<model>/                 best .fr + failure log        (1 model)
    unscored/<model>/                .fr + dossier, no declared total (9)

Reads only files in this directory. No FeynRules, no agent, no network.

Usage:
    python benchmarks/build_review_bundle.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import zipfile
from pathlib import Path


def _pages(pdf: Path) -> int:
    """Page count via pdfinfo; 0 if unavailable."""
    try:
        r = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                           text=True, timeout=30)
        for line in r.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split()[1])
    except (OSError, subprocess.SubprocessError, ValueError):
        pass
    return 0

HERE = Path(__file__).parent
BUNDLE = HERE / "review_bundle"
ZIP = HERE / "review_bundle.zip"

ALL_MODELS = 28


def _verdicts() -> tuple[list[str], list[str], list[str]]:
    """(passing, failing, unscored) from the post-fix revalidation run.

    Grouping used to come from the old pass/fail split, which was computed
    before the total-Lagrangian bug was found. It now comes from
    revalidation_report.json, and anything the harness could not score is a
    third category rather than being forced into pass or fail.
    """
    rep = HERE / "revalidation_report.json"
    if not rep.is_file():
        raise SystemExit("revalidation_report.json missing — run "
                         "revalidate_affected.py first")
    rows = json.loads(rep.read_text())["rows"]
    scored = {r["page"]: bool(r.get("full_chain_ok")) for r in rows}
    passing = sorted(p for p, ok in scored.items() if ok)
    failing = sorted(p for p, ok in scored.items() if not ok)
    # db_candidates.json is the authority for what the benchmark covers.
    # Listing directories picks up leftovers from earlier runs — SMScalars
    # has a model/ directory but was never one of the 28 candidates.
    cands = json.loads((HERE / "db_candidates.json").read_text())["candidates"]
    known = {c["page"] for c in cands}
    stray = set(scored) - known
    if stray:
        raise SystemExit(f"scored models outside the candidate set: {stray}")
    unscored = sorted(known - set(scored))
    return passing, failing, unscored

REPORTS = (
    "validation_benchmark_report.md",
    "repair_benchmark_report.md",
    "repair_benchmark_phase2_report.md",
    "repair_benchmark_phase3_report.md",
)


def _passing_models() -> list[str]:
    """Models with a review package, i.e. the ones that passed the full chain."""
    src = HERE / "ian_review_bundle"
    if not src.is_dir():
        return []
    return sorted(p.name for p in src.iterdir() if p.is_dir())


def _last_round(model: str) -> Path | None:
    """Deepest repair round that produced a model.fr, i.e. the best attempt."""
    cands = []
    for phase in ("repair3", "repair2", "repair"):
        d = HERE / model / phase
        if not d.is_dir():
            continue
        for rd in sorted(d.glob("round*"), reverse=True):
            if (rd / "model.fr").is_file():
                cands.append(rd)
        if cands:
            break
    return cands[0] if cands else None


def _crosscheck_counts() -> dict:
    p = HERE / "disagreements.json"
    if not p.is_file():
        return {}
    return json.loads(p.read_text())


def _last_round_label(model: str) -> str:
    rd = _last_round(model)
    return f"{rd.parent.name}/{rd.name}" if rd else "no repair round recorded"


def _place(model: str, dst: Path, have_review: set,
           pdf_pages: dict) -> None:
    """One model directory: the .fr files plus exactly one PDF to open.

    Where the reverse run finished, that PDF is the completed REVIEW.pdf.
    Where it did not, build_model_pdfs.py wrote a DOSSIER.pdf carrying the
    verbatim Lagrangian, the validation result and the repair history; it
    supersedes the 2-3 empty pages the aborted review left behind.
    """
    dst.mkdir(parents=True)
    dossier = HERE / model / "dossier" / "DOSSIER.pdf"

    if model in have_review:
        for f in sorted((HERE / "ian_review_bundle" / model).iterdir()):
            if f.is_file():
                if f.name == "REVIEW.pdf" and dossier.is_file():
                    continue                        # superseded
                shutil.copy2(f, dst / f.name)
    else:
        rd = _last_round(model)
        if rd:
            shutil.copy2(rd / "model.fr", dst / f"{model}.fr")
            for name in ("VALIDATION_REPORT.md", "REPAIR_HISTORY.md"):
                if (rd / name).is_file():
                    shutil.copy2(rd / name, dst / name)

    gen = HERE / model / "model" / f"{model}_gen.fr"
    if gen.is_file() and not (dst / f"{model}.fr").is_file():
        shutil.copy2(gen, dst / f"{model}.fr")
    elif gen.is_file():
        shutil.copy2(gen, dst / f"{model}_one_shot.fr")

    if dossier.is_file():
        shutil.copy2(dossier, dst / "DOSSIER.pdf")

    pdf = dst / ("DOSSIER.pdf" if dossier.is_file() else "REVIEW.pdf")
    pdf_pages[model] = (pdf.name, _pages(pdf)) if pdf.is_file() else ("—", 0)


def assemble() -> None:
    if BUNDLE.exists():
        shutil.rmtree(BUNDLE)
    BUNDLE.mkdir()

    # ---- passing models: .fr + one PDF --------------------------------
    # Where the reverse run did not finish, REVIEW.pdf is 2-3 empty pages.
    # build_model_pdfs.py writes a DOSSIER.pdf for those; it supersedes the
    # empty review, so each model directory holds exactly one PDF to open.
    passing, failing, unscored = _verdicts()
    have_review = set(_passing_models())
    pdf_pages: dict[str, tuple[str, int]] = {}

    for group, members in (("passing", passing), ("failing", failing),
                           ("unscored", unscored)):
        (BUNDLE / group).mkdir()
        for m in members:
            _place(m, BUNDLE / group / m, have_review, pdf_pages)

    fail_rows = [(m, _last_round_label(m)) for m in failing]

    # ---- reports and analysis ----------------------------------------
    (BUNDLE / "reports").mkdir()
    for r in REPORTS:
        if (HERE / r).is_file():
            shutil.copy2(HERE / r, BUNDLE / "reports" / r)
    for top in ("REPAIR_BENCHMARK_ANALYSIS.md", "CONVENTION_DISAGREEMENTS.md",
                "LAGRANGIAN_AMBIGUITY.md", "CORRECTION_2026-08.md"):
        if (HERE / top).is_file():
            shutil.copy2(HERE / top, BUNDLE / top)

    (BUNDLE / "README.md").write_text(
        _readme(passing, fail_rows, unscored, pdf_pages), encoding="utf-8")

    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(BUNDLE.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(BUNDLE.parent))

    n = sum(1 for f in BUNDLE.rglob("*") if f.is_file())
    print(f"[bundle] {len(passing)} passing, {len(failing)} failing, "
          f"{len(unscored)} unscored")
    print(f"[bundle] {n} files -> {ZIP.name} ({ZIP.stat().st_size // 1024} KB)")


def _readme(passing: list[str], fail_rows: list[tuple[str, str]],
            unscored: list[str],
            pdf_pages: dict[str, tuple[str, int]]) -> str:
    d = _crosscheck_counts()
    c = d.get("counts", {})
    no_cc = set(d.get("models_without_crosscheck", []))

    L = [
        "# Review bundle — agent-extracted FeynRules models",
        "",
        "28 published BSM models from the FeynRules model database were "
        "re-derived from their own papers by an agent, then pushed through "
        "the full validation chain: FeynRules/Wolfram UFO compile, "
        "Hermiticity / kinetic-term / mass-spectrum checks, MadGraph import. "
        "Models that failed entered a closed repair loop.",
        "",
        "| outcome | models |",
        "|---|---:|",
        "| clear the full chain | **18** |",
        "| fail the full chain | 1 |",
        "| cannot be scored — see below | 9 |",
        "| **total** | **28** |",
        "",
        "## Read this first",
        "",
        "An earlier version of this bundle reported 25 of 28 passing. That "
        "number was wrong and is withdrawn.",
        "",
        "The harness used to choose each model's total-Lagrangian symbol by "
        "file position — the last `L... =` line. For 11 models that picked a "
        "sub-Lagrangian, so FeynRules compiled only a fragment. A fragment is "
        "easier to satisfy than the whole: it can be Hermitian when the full "
        "Lagrangian is not, and it can show a clean mass spectrum simply by "
        "omitting most fields. Those fragments passed every check and "
        "imported into MadGraph. `VLQ` was scored as passing having compiled "
        "1 of its 11 Lagrangian terms.",
        "",
        "The total is now resolved by reference analysis — the term no other "
        "term refers to — and where a model never declares one, the harness "
        "**refuses to guess** and leaves it unscored. Everything was re-run. "
        "All 19 scoreable models reproduced their previous verdict, so the "
        "pipeline did not get worse; 9 models were simply never measured.",
        "",
        "**Unscoreable is not failed.** Those 9 models may be perfectly "
        "correct. They just never say which symbol is the whole model, so "
        "there is nothing defensible to compile. `LAGRANGIAN_AMBIGUITY.md` "
        "lists what each one defines — it is a short decision list, and four "
        "of the nine are genuine physics choices only you can make.",
        "",
        "Three of the ten repairs the loop claimed are also affected: `331`, "
        "`CHEIDI` and `VLC_LN` were scored `pass_repaired` against fragments, "
        "so those claims cannot be evaluated. Seven repairs stand.",
        "",
        "## What we are asking you to check",
        "",
        "Passing means **the tool chain accepts the model**. It does not mean "
        "the physics matches the paper, and we are not claiming it does.",
        "",
        "To test the physics we ran the chain backwards. For each passing "
        "model, an agent that never saw the paper reconstructed the "
        "Lagrangian from the sanitized `.fr` alone. A second fresh agent then "
        "compared that reconstruction against the paper term by term and "
        "graded every difference.",
        "",
        "**Those grades come from an agent, not a physicist. They are the "
        "question list, not the answer.** That is what your sign-off is for.",
        "",
    ]

    if c:
        L += [
            "| grade | rows | meaning |",
            "|---|---:|---|",
            f"| convention | {c.get('convention', 0)} | probably the same "
            "physics written differently |",
            f"| substantive | {c.get('substantive', 0)} | a real difference "
            "in content — these are the ones worth your time |",
            f"| cosmetic | {c.get('cosmetic', 0)} | presentation only |",
            "",
        ]

    L += [
        "## Reading order",
        "",
        "1. `LAGRANGIAN_AMBIGUITY.md` — the nine unscoreable models and what "
        "each defines. Four need a physics decision from you.",
        "2. `CONVENTION_DISAGREEMENTS.md` — every graded row, grouped by "
        "theme. Start with the substantive ones.",
        "3. `passing/<model>/REVIEW.pdf` — the full review package for any "
        "model whose rows you want to see in context. The last page is a "
        "sign-off block.",
        "4. `REPAIR_BENCHMARK_ANALYSIS.md` — what the loop fixed, what it "
        "could not, and the error taxonomy.",
        "5. `reports/` — the machine-generated per-stage results.",
        "6. `failing/` and `unscored/` — the models that did not clear "
        "the chain, and the nine that could not be scored at all.",
        "",
        "## Contents",
        "",
        f"### passing/ ({len(passing)} models)",
        "",
        "`<model>.fr` is the validated FeynRules file, agent-extracted and, "
        "where the loop repaired it, self-repaired with no human input. "
        "**Every model has exactly one PDF — open that and you have "
        "everything.**",
        "",
        "`REVIEW.pdf` is a completed reverse-check package: verbatim "
        "Lagrangian terms, the blank-slate reconstruction, the term-by-term "
        "paper comparison, and a sign-off block. `DOSSIER.pdf` appears where "
        "the reverse run did not finish — it carries the verbatim Lagrangian, "
        "whatever reconstruction exists, the validation result and the repair "
        "history, so the model is still readable without opening source "
        "files.",
        "",
        "| model | PDF | pages | state |",
        "|---|---|---:|---|",
    ]
    for m in passing:
        name, pages = pdf_pages.get(m, ("—", 0))
        state = ("reverse run unfinished — **not yet reviewed**"
                 if m in no_cc else "full term-by-term cross-check")
        L.append(f"| {m} | `{name}` | {pages} | {state} |")

    L += [
        "",
        f"{len(no_cc)} of these have no cross-check. Their reverse runs hit "
        "agent-transport failures, not a physics result. Treat them as not "
        "yet reviewed — their `DOSSIER.pdf` says so on page 1.",
        "",
        f"### failing/ ({len(fail_rows)} models)",
        "",
        "Scored, and did not clear the chain.",
        "",
        "| model | best attempt | why |",
        "|---|---|---|",
        "| SLQrules | " + dict(fail_rows).get("SLQrules", "—") +
        " | A syntax error at line 660 stops FeynRules loading the model, so "
        "its total Lagrangian is never defined. The repair loop never "
        "produced a working version, so this is the one-shot file. Behind it "
        "sits a residual SU(2)-multiplet covariant-derivative Hermiticity "
        "violation that survived nine rounds — genuinely hard physics rather "
        "than a tooling gap. |",
        "",
        f"### unscored/ ({len(unscored)} models)",
        "",
        "**Neither passed nor failed.** These models define several "
        "independent top-level Lagrangians and never say which one — or "
        "which sum — is the model, so there is nothing defensible to "
        "compile. Earlier numbers scored them by picking whichever came last "
        "in the file, which is how `VLQ` came to be reported as passing on 1 "
        "of its 11 terms.",
        "",
        "`LAGRANGIAN_AMBIGUITY.md` lists the competing definitions for each. "
        "Five look like complementary sectors where a sum is the natural "
        "reading; four are genuine alternatives — `ChernSimonsPortal` "
        "(symmetric versus broken phase), `DMsimp` (spin-0 versus spin-1 "
        "mediator), `topBSM` (four simplified models in one file) and "
        "`CHEIDI` (full top loop versus heavy-top limit). Those four need a "
        "physicist, not a parser.",
        "",
        "| model | competing definitions |",
        "|---|---|",
    ]
    _amb = {
        "331": "LHiggs331, LGauge331Mass, LScalarFermion331, LTot",
        "ALRM_general": "LYALRM, LSALRM, LFALRM, LeffALRM",
        "CHEIDI": "LHEIDI, LHEIDIgg, LTot",
        "ChernSimonsPortal": "LChernSimonsPortal, LChernSimonsPortalBroken",
        "DMsimp": "L0DM, L1DM",
        "HNLs": "LagHeavyN, LHeavyNDiracMass, LHeavyNEW + 4 hadronic terms",
        "VLC_LN": "LChiralFull, LEDM, LTot",
        "VLQ": "11 separate T'/B' coupling terms",
        "topBSM": "LS0, LO0, LS1, LO1",
    }
    for m in unscored:
        L.append(f"| {m} | {_amb.get(m, '—')} |")

    L += [
        "",
        "## Caveats",
        "",
        "- The repair agent ran isolated (no network, no reference files, no "
        "model name), but the underlying model may have seen these public "
        "model files in training.",
        "- Repairs that replaced symbolic values with numerics keep the tool "
        "chain valid while narrowing the model's parameter generality. The "
        "analysis flags them.",
        "- Symbol names survive sanitizing on purpose, so the blank-slate "
        "agent was not perfectly blind.",
        "",
    ]
    return "\n".join(L)


if __name__ == "__main__":
    assemble()
