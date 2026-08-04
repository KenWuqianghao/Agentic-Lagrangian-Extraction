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
import zipfile
from pathlib import Path

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

    # ---- passing models: .fr + REVIEW.pdf -----------------------------
    passing = _passing_models()
    (BUNDLE / "passing").mkdir()
    for m in passing:
        src, dst = HERE / "ian_review_bundle" / m, BUNDLE / "passing" / m
        dst.mkdir()
        for f in sorted(src.iterdir()):
            if f.is_file():
                shutil.copy2(f, dst / f.name)

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
        fail_rows.append((m, note))

    # ---- reports and analysis ----------------------------------------
    (BUNDLE / "reports").mkdir()
    for r in REPORTS:
        if (HERE / r).is_file():
            shutil.copy2(HERE / r, BUNDLE / "reports" / r)
    for top in ("REPAIR_BENCHMARK_ANALYSIS.md", "CONVENTION_DISAGREEMENTS.md"):
        if (HERE / top).is_file():
            shutil.copy2(HERE / top, BUNDLE / top)

    (BUNDLE / "README.md").write_text(_readme(passing, fail_rows), encoding="utf-8")

    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(BUNDLE.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(BUNDLE.parent))

    n = sum(1 for f in BUNDLE.rglob("*") if f.is_file())
    print(f"[bundle] {len(passing)} passing, {len(FAILING)} failing")
    print(f"[bundle] {n} files -> {ZIP.name} ({ZIP.stat().st_size // 1024} KB)")


def _readme(passing: list[str], fail_rows: list[tuple[str, str]]) -> str:
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
        "1. `CONVENTION_DISAGREEMENTS.md` — every graded row, grouped by "
        "theme. Start with the substantive ones.",
        "2. `passing/<model>/REVIEW.pdf` — the full review package for any "
        "model whose rows you want to see in context. The last page is a "
        "sign-off block.",
        "3. `REPAIR_BENCHMARK_ANALYSIS.md` — what the loop fixed, what it "
        "could not, and the error taxonomy.",
        "4. `reports/` — the machine-generated per-stage results.",
        "5. `failing/` — the three models the loop could not repair.",
        "",
        "## Contents",
        "",
        f"### passing/ ({len(passing)} models)",
        "",
        "`<model>.fr` is the validated FeynRules file, agent-extracted and, "
        "where the loop repaired it, self-repaired with no human input. "
        "`REVIEW.pdf` is the blank-slate review package.",
        "",
        "| model | review |",
        "|---|---|",
    ]
    for m in passing:
        state = ("reconstruction incomplete — **not yet reviewed**"
                 if m in no_cc else "full term-by-term cross-check")
        L.append(f"| {m} | {state} |")

    L += [
        "",
        f"{len(no_cc)} of these have no cross-check. Their reverse runs hit "
        "agent-transport failures, not a physics result. Treat them as not "
        "yet reviewed.",
        "",
        f"### failing/ ({len(fail_rows)} models)",
        "",
        "The loop could not get these through the chain. Included so the "
        "picture is complete, not only the successes. `<model>_one_shot.fr` "
        "is the first attempt; `<model>.fr` is the best repaired attempt; "
        "`VALIDATION_REPORT.md` is the failure it stopped on.",
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
