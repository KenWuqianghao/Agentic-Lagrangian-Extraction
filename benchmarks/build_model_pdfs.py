#!/usr/bin/env python3
"""
Give every benchmark model a compiled PDF a physicist can read straight
through, with no need to open a `.fr` or a log.

21 of the 28 models already have a full reverse-check `REVIEW.pdf` (6-15
pages: verbatim Lagrangian terms, blank-slate reconstruction, term-by-term
paper cross-check, sign-off). This script fills the seven gaps:

  331, B-L-SM, VLC_LN   passed validation, but the reverse run died on agent
                        transport errors, so REVIEW.pdf is 2-3 empty pages
  CHEIDI                reconstruction present, cross-check never ran
  ALRM_general, HNLs,   never cleared the chain, so no review package exists
  SLQrules              at all

For each it writes a DOSSIER.md and compiles it with the same
pandoc -> xelatex path the real review packages use, so the typography
matches. Each dossier carries the verbatim Lagrangian terms, the model's
status, what failed and why, the repair history, and the same sign-off block.

Usage:
    python benchmarks/build_model_pdfs.py            # build the gap PDFs
    python benchmarks/build_model_pdfs.py --check    # report coverage only
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
HEPTAPOD = Path("/Users/kenwu/Documents/Github/heptapod")
sys.path.insert(0, str(HEPTAPOD))

from tools.frgen.fr_parser import parse_lagrangian_terms  # noqa: E402
from tools.reverse.pdf_build import compile_review_pdf  # noqa: E402

# model -> (why the review package is incomplete, physicist-facing note)
INCOMPLETE = {
    "331": ("reverse run failed",
            "The blank-slate reconstruction aborted on an agent transport "
            "error. This is an infrastructure failure, not a physics result."),
    "B-L-SM": ("reverse run failed",
               "The blank-slate reconstruction aborted on an agent transport "
               "error (connection reset). Infrastructure, not physics."),
    "VLC_LN": ("reverse run failed",
               "The blank-slate reconstruction aborted on an agent transport "
               "error. Infrastructure, not physics."),
    "CHEIDI": ("cross-check missing",
               "The blank-slate reconstruction completed and is included "
               "below, but the paper cross-check never ran, so no term-by-term "
               "comparison exists."),
}

FAILING = {
    "ALRM_general": (
        "never cleared the chain",
        "Multi-member `ClassMembers` scalar classes serialize to invalid UFO "
        "Python (2D-typeset exponents, `PRIVATE\\`` internals). Every attempt "
        "to restructure them either re-broke the model or exceeded the "
        "compile budget. Best fixed deterministically in the generator, not "
        "by a repair agent."),
    "HNLs": (
        "never cleared the chain",
        "A stack of layered semantic UFO leaks: `Mass -> N4` against an "
        "undefined `MN4`, `NoUnfold[..]` inside index ranges, a bare `NP` "
        "interaction order. Each was fixed once the diagnostics named it, but "
        "the stack outlasted the round budget."),
    "SLQrules": (
        "never cleared the chain",
        "A residual SU(2)-multiplet covariant-derivative Hermiticity "
        "violation, surviving nine repair rounds. This one is genuinely hard "
        "physics rather than a tooling gap, and is the most interesting of "
        "the three to look at."),
}


# Captured tool logs carry ANSI colour codes and stray control bytes. xelatex
# rejects them outright ("Text line contains an invalid character"), so strip
# them before anything reaches the LaTeX source.
_ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[ -/]*[@-~]|\x1b[@-Z\\-_]")
_CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def _clean(text: str) -> str:
    return _CTRL_RE.sub("", _ANSI_RE.sub("", text))


def _read(p: Path) -> str:
    if not p.is_file():
        return ""
    return _clean(p.read_text(encoding="utf-8", errors="replace"))


def _final_fr(model: str) -> tuple[Path | None, str]:
    """The authoritative .fr and a human label for where it came from.

    `<phase>/final.fr` is the model the harness actually re-validated, so it
    wins. A `roundN/model.fr` is only that round's agent output, which for a
    failing model is a draft that was never accepted.
    """
    for phase in ("repair3", "repair2", "repair"):
        d = HERE / model / phase
        if not d.is_dir():
            continue
        if (d / "final.fr").is_file():
            return d / "final.fr", f"{phase}/final.fr (re-validated)"
        for rd in sorted(d.glob("round*"), reverse=True):
            if (rd / "model.fr").is_file():
                return rd / "model.fr", f"{phase}/{rd.name}/model.fr (last attempt)"
    gen = HERE / model / "model" / f"{model}_gen.fr"
    return (gen, "one-shot extraction") if gen.is_file() else (None, "")


def _last_round_dir(model: str) -> Path | None:
    for phase in ("repair3", "repair2", "repair"):
        d = HERE / model / phase
        if d.is_dir():
            rounds = sorted(d.glob("round*"), reverse=True)
            if rounds:
                return rounds[0]
    return None


def _fence(text: str, lang: str = "mathematica") -> list[str]:
    """Fenced block.

    Tag the language even for plain output: pandoc only routes *highlighted*
    blocks through the fancyvrb `Highlighting` environment, which is the one
    pdf_build sets `breaklines` on. An untagged fence becomes a plain
    `verbatim` and silently runs off the right margin. FeynRules source is
    Wolfram Language, so `mathematica` is also the honest tag.
    """
    return ["```" + lang, text.rstrip(), "```", ""]


def dossier_md(model: str, status: str, note: str, failing: bool) -> str:
    fr_path, provenance = _final_fr(model)
    fr_text = _read(fr_path) if fr_path else ""
    terms = parse_lagrangian_terms(fr_text) if fr_text else []
    rd = _last_round_dir(model)

    L: list[str] = [
        f"# Model dossier — `{model}`",
        "",
        f"**Status: {status}.** {note}",
        "",
        "This dossier is not a completed reverse-check review package. It "
        "collects what exists for this model so you can read the physics "
        "without opening the source files. Where a full review package does "
        "exist for a model, it is the `REVIEW.pdf` in that model's directory.",
        "",
        "| item | value |",
        "|---|---|",
        f"| model | `{model}` |",
        f"| chain status | {'did not pass' if failing else 'passed the full chain'} |",
        f"| Lagrangian source | `{provenance}` |",
        f"| Lagrangian terms found | {len(terms)} |",
        "",
    ]

    if failing:
        L += [
            "## Why this model matters to you",
            "",
            "The loop could not get this model through the chain. It is "
            "included so the picture is the whole benchmark, not only the "
            "successes. The Lagrangian below is the best attempt the loop "
            "produced; treat it as a draft that is known not to validate.",
            "",
        ]

    if terms:
        L += [
            "## Verbatim Lagrangian terms",
            "",
            "Quoted unmodified from the `.fr`. These are the terms any "
            "reconstruction would have to account for.",
            "",
        ]
        for t in terms:
            L += [f"### `{t['name']}` (`{t['op']}`)", ""]
            L += _fence(t["expression"])
    else:
        L += ["## Verbatim Lagrangian terms", "",
              "*(no top-level Lagrangian assignments parsed from the "
              "`.fr` — see the raw file in this directory)*", ""]

    # An existing reconstruction is the most valuable thing we can show.
    recon = _read(HERE / model / "review" / "reconstruction.md")
    if recon.strip():
        L += [
            "## Blank-slate reconstruction",
            "",
            "Written by an agent that saw only the sanitized `.fr` — no "
            "paper, no model name, no history.",
            "",
            recon.strip(),
            "",
        ]

    if rd:
        vr = _read(rd / "VALIDATION_REPORT.md")
        if vr.strip():
            # roundN/VALIDATION_REPORT.md is the report handed TO the agent at
            # the start of round N — the failure it was asked to fix, not the
            # outcome. Labelling it "final result" would contradict the status
            # line for every model that went on to pass.
            outcome = ("The model **passed** after this round; the report "
                       "below is the state that was repaired, not the final "
                       "one."
                       if not failing else
                       "The model still did not pass after this round.")
            L += [
                "## The last failure the loop worked on",
                "",
                f"This is the validation report handed to the repair agent at "
                f"the start of `{rd.parent.name}/{rd.name}` — the problem it "
                f"was asked to fix. {outcome}",
                "",
                vr.strip(),
                "",
            ]
        rh = _read(rd / "REPAIR_HISTORY.md")
        if rh.strip():
            L += [
                "## Repair history",
                "",
                "What the loop tried, and what each attempt measured.",
                "",
                rh.strip(),
                "",
            ]

    L += [
        "## Physicist sign-off",
        "",
        "- Reviewed by: ______________________  Date: ____________",
        "- Verdict: [ ] approve   [ ] approve with corrections   [ ] reject",
        "- Notes:",
        "",
    ]
    return "\n".join(L)


def coverage() -> list[tuple[str, str, int]]:
    """(model, pdf name, pages) for every model directory."""
    out = []
    for d in sorted(p for p in HERE.iterdir() if p.is_dir()):
        if d.name in ("ian_review_bundle", "review_bundle", "__pycache__"):
            continue
        pdfs = sorted(d.glob("review/*.pdf")) + sorted(d.glob("*.pdf"))
        if pdfs:
            out.append((d.name, pdfs[0].name, _pages(pdfs[0])))
        else:
            out.append((d.name, "—", 0))
    return out


def _pages(pdf: Path) -> int:
    try:
        r = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                           text=True, timeout=30)
        for line in r.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split()[1])
    except (OSError, subprocess.SubprocessError, ValueError):
        pass
    return 0


def main() -> int:
    if "--check" in sys.argv:
        for m, name, pages in coverage():
            print(f"  {m:24} {name:16} {pages:3} pages")
        return 0

    targets = [(m, s, n, False) for m, (s, n) in INCOMPLETE.items()]
    targets += [(m, s, n, True) for m, (s, n) in FAILING.items()]

    rc = 0
    for model, status, note, failing in targets:
        out_dir = HERE / model / "dossier"
        out_dir.mkdir(parents=True, exist_ok=True)
        md = out_dir / "DOSSIER.md"
        md.write_text(dossier_md(model, status, note, failing), encoding="utf-8")
        res = compile_review_pdf(str(md), str(out_dir / "DOSSIER.pdf"))
        if res.get("ok"):
            pages = _pages(out_dir / "DOSSIER.pdf")
            print(f"[pdf] {model:16} -> DOSSIER.pdf  {pages:3} pages "
                  f"({res['seconds']}s)")
        else:
            print(f"[pdf] {model:16} FAILED: {res.get('error')}")
            rc = 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
