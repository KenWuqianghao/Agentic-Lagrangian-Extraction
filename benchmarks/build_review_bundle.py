#!/usr/bin/env python3
"""
Assemble the physicist review bundle from benchmark output already on disk.

Produces `review_bundle/` and `review_bundle.zip`:

    README.md                        inventory and reading order
    CONVENTION_DISAGREEMENTS.md      graded reconstruction-vs-paper rows
    REPAIR_BENCHMARK_ANALYSIS.md     full write-up and error taxonomy
    reports/                         the four machine-generated reports
    passing/<model>/                 validated .fr + REVIEW.pdf   (25 models)
    failing/<model>/                 best .fr + last failure log  (3 models)

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

FAILING = ("ALRM_general", "HNLs", "SLQrules")

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


def assemble() -> None:
    if BUNDLE.exists():
        shutil.rmtree(BUNDLE)
    BUNDLE.mkdir()

    # ---- passing models: .fr + one PDF --------------------------------
    # Where the reverse run did not finish, REVIEW.pdf is 2-3 empty pages.
    # build_model_pdfs.py writes a DOSSIER.pdf for those; it supersedes the
    # empty review, so each model directory holds exactly one PDF to open.
    passing = _passing_models()
    (BUNDLE / "passing").mkdir()
    pdf_pages: dict[str, tuple[str, int]] = {}
    for m in passing:
        src, dst = HERE / "ian_review_bundle" / m, BUNDLE / "passing" / m
        dst.mkdir()
        dossier = HERE / m / "dossier" / "DOSSIER.pdf"
        for f in sorted(src.iterdir()):
            if f.is_file():
                if f.name == "REVIEW.pdf" and dossier.is_file():
                    continue  # superseded
                shutil.copy2(f, dst / f.name)
        if dossier.is_file():
            shutil.copy2(dossier, dst / "DOSSIER.pdf")
        pdf = dst / ("DOSSIER.pdf" if dossier.is_file() else "REVIEW.pdf")
        pdf_pages[m] = (pdf.name, _pages(pdf)) if pdf.is_file() else ("—", 0)

    # ---- failing models: best .fr + the log that says why -------------
    (BUNDLE / "failing").mkdir()
    fail_rows = []
    for m in FAILING:
        dst = BUNDLE / "failing" / m
        dst.mkdir()
        rd = _last_round(m)
        note = "no repair round recorded"
        if rd:
            shutil.copy2(rd / "model.fr", dst / f"{m}.fr")
            for name in ("VALIDATION_REPORT.md", "REPAIR_HISTORY.md"):
                if (rd / name).is_file():
                    shutil.copy2(rd / name, dst / name)
            note = f"{rd.parent.name}/{rd.name}"
        gen = HERE / m / "model" / f"{m}_gen.fr"
        if gen.is_file():
            shutil.copy2(gen, dst / f"{m}_one_shot.fr")
        dossier = HERE / m / "dossier" / "DOSSIER.pdf"
        if dossier.is_file():
            shutil.copy2(dossier, dst / "DOSSIER.pdf")
            pdf_pages[m] = ("DOSSIER.pdf", _pages(dst / "DOSSIER.pdf"))
        fail_rows.append((m, note))

    # ---- reports and analysis ----------------------------------------
    (BUNDLE / "reports").mkdir()
    for r in REPORTS:
        if (HERE / r).is_file():
            shutil.copy2(HERE / r, BUNDLE / "reports" / r)
    for top in ("REPAIR_BENCHMARK_ANALYSIS.md", "CONVENTION_DISAGREEMENTS.md",
                "LAGRANGIAN_COVERAGE.md"):
        if (HERE / top).is_file():
            shutil.copy2(HERE / top, BUNDLE / top)

    (BUNDLE / "README.md").write_text(
        _readme(passing, fail_rows, pdf_pages), encoding="utf-8")

    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(BUNDLE.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(BUNDLE.parent))

    n = sum(1 for f in BUNDLE.rglob("*") if f.is_file())
    print(f"[bundle] {len(passing)} passing, {len(FAILING)} failing")
    print(f"[bundle] {n} files -> {ZIP.name} ({ZIP.stat().st_size // 1024} KB)")


def _readme(passing: list[str], fail_rows: list[tuple[str, str]],
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
        "| stage | passing | rate |",
        "|---|---:|---:|",
        "| one-shot | 15/28 | 54% |",
        "| + repair phase 1 | 20/28 | 71% |",
        "| + repair phase 2 | 24/28 | 86% |",
        "| **+ repair phase 3** | **25/28** | **89%** |",
        "",
        "## Read this first",
        "",
        "**The pass rate above overstates coverage for 9 of the 25 passing "
        "models.** The harness picks each model's total-Lagrangian symbol by "
        "file position — the last `L... =` line — and for those 9 that symbol "
        "is not the model's total, so FeynRules compiled a fragment. A "
        "fragment can be Hermitian, pass every check and import into "
        "MadGraph. `VLQ` passed on 1 of its 11 Lagrangian terms; `topBSM` on "
        "5 of 23; `331` on 2 of 5.",
        "",
        "This is our bug, not a defect in the models, and it is unfixed as of "
        "this bundle. `LAGRANGIAN_COVERAGE.md` lists every affected model and "
        "what was omitted. Please weigh the pass rate accordingly.",
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
        "1. `LAGRANGIAN_COVERAGE.md` — which models were only partly "
        "compiled, and what was left out. This bounds what the rest means.",
        "2. `CONVENTION_DISAGREEMENTS.md` — every graded row, grouped by "
        "theme. Start with the substantive ones.",
        "3. `passing/<model>/REVIEW.pdf` — the full review package for any "
        "model whose rows you want to see in context. The last page is a "
        "sign-off block.",
        "4. `REPAIR_BENCHMARK_ANALYSIS.md` — what the loop fixed, what it "
        "could not, and the error taxonomy.",
        "5. `reports/` — the machine-generated per-stage results.",
        "6. `failing/` — the three models the loop could not repair.",
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
        "The loop could not get these through the chain. Included so the "
        "picture is complete, not only the successes. Read `DOSSIER.pdf`; "
        "`<model>_one_shot.fr` is the first attempt, `<model>.fr` the best "
        "repaired attempt, and `VALIDATION_REPORT.md` the failure it stopped "
        "on.",
        "",
        "| model | best attempt | why it resisted |",
        "|---|---|---|",
        "| ALRM_general | " + dict(fail_rows).get("ALRM_general", "—") +
        " | multi-member `ClassMembers` scalar classes serialize to invalid "
        "UFO Python; restructuring re-breaks or times out the compile |",
        "| HNLs | " + dict(fail_rows).get("HNLs", "—") +
        " | layered semantic UFO leaks; each was fixed once named, but the "
        "stack outlasted the round budget |",
        "| SLQrules | " + dict(fail_rows).get("SLQrules", "—") +
        " | residual SU(2)-multiplet covariant-derivative Hermiticity "
        "violation — genuinely hard physics, not a tooling gap |",
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
