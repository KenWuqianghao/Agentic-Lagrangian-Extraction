#!/usr/bin/env python3
"""
# build_ian_bundle.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Build the physicist review bundle: for every benchmark model that passes the
full validation chain, run the blank-slate reverse check (sanitize -> blind
reconstruction -> paper cross-check -> REVIEW.pdf) against the model's own
paper, then assemble ian_review_bundle/<model>/{<model>.fr, REVIEW.pdf} plus
a README inventory, and zip it.

The bundle that was sent (ian_review_bundle/, 25 models) was built from the
withdrawn pre-2026-09-13 verdicts. A rebuild selects from the post-fix
revalidation (revalidation_report.json `full_chain_ok`).

Resumable: a model is skipped on re-run when its REVIEW.pdf exists and its
reverse check finished (crosscheck.md, or reconstruction.md with no paper).
An aborted run still writes REVIEW.pdf, so the PDF alone is not enough.
Reverse checks run serially (each spawns two codex instances).

Usage:
    python benchmarks/build_ian_bundle.py            # run + assemble
    python benchmarks/build_ian_bundle.py --assemble # bundle only
"""

from __future__ import annotations

import glob
import json
import os
import shutil
import sys
import time
import zipfile
from pathlib import Path

HERE = Path(__file__).parent
HEPTAPOD = Path(os.environ.get("HEPTAPOD_REPO", "~/Documents/Github/heptapod")).expanduser()
sys.path.insert(0, str(HEPTAPOD))

import config  # noqa: E402
from tools.reverse.reverse_tool import ReverseLagrangianTool  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_review_bundle as rb  # noqa: E402

BUNDLE = HERE / "ian_review_bundle"
DEFAULT_AGENT = ("codex exec --sandbox read-only --skip-git-repo-check "
                 "--model gpt-5.5 -c model_reasoning_effort=medium "
                 "--output-last-message {output}")


PHASE_TAG = {"repair": "repaired (phase 1)", "repair2": "repaired (phase 2)",
             "repair3": "repaired (phase 3)"}


def passing_models() -> list[tuple[str, Path, str]]:
    """(page, scored .fr path, provenance) for every model that passes the full
    chain in the post-fix revalidation."""
    passing, _, _ = rb._verdicts()
    sources = rb._fr_sources()
    out: list[tuple[str, Path, str]] = []
    for page in passing:
        src = sources[page]
        if src == "one-shot":
            out.append((page, HERE / page / "model" / f"{page}_gen.fr", "passed one-shot"))
        else:
            out.append((page, HERE / page / src, PHASE_TAG[src.split("/")[0]]))
    return out


def paper_for(page: str) -> Path | None:
    hits = sorted(glob.glob(str(HERE / page / "text" / "*.txt")))
    return Path(hits[0]) if hits else None


def _reviews(page: str, name: str) -> list[Path]:
    """REVIEW.* both directly under <page>/review/ and one level deeper."""
    outdir = HERE / page / "review"
    return sorted(outdir.glob(name)) + sorted(outdir.glob(f"*/{name}"))


def run_reverse(page: str, fr: Path) -> dict:
    paper = paper_for(page)
    existing = _reviews(page, "REVIEW.pdf")
    if existing and _reviews(page, "crosscheck.md" if paper else "reconstruction.md"):
        return {"skipped": True, "review_package": str(existing[0].relative_to(HERE))}
    tool = ReverseLagrangianTool(
        base_directory=str(HERE),
        blank_agent_cmd=getattr(config, "blank_agent_cmd", DEFAULT_AGENT),
        model_path=str(fr.relative_to(HERE)),
        action="full" if paper else "reconstruct",
        paper_tex_path=str(paper.relative_to(HERE)) if paper else None,
        output_dir=str(Path(page) / "review"),
        timeout_sec=900,
    )
    raw = tool._run()
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return {"raw": str(raw)[-800:]}


def assemble(results: dict[str, dict]) -> Path:
    if BUNDLE.exists():
        shutil.rmtree(BUNDLE)
    BUNDLE.mkdir()
    rows = []
    for page, fr, tag in passing_models():
        dst = BUNDLE / page
        dst.mkdir()
        shutil.copy2(fr, dst / f"{page}.fr")
        pdfs = _reviews(page, "REVIEW.pdf")
        mds = _reviews(page, "REVIEW.md")
        status = "no review generated"
        if pdfs:
            shutil.copy2(pdfs[0], dst / "REVIEW.pdf")
            status = "REVIEW.pdf"
        elif mds:
            shutil.copy2(mds[0], dst / "REVIEW.md")
            status = "REVIEW.md (PDF compile failed)"
        paper = paper_for(page)
        arxiv = paper.stem if paper else "—"
        rows.append((page, arxiv, tag, status))

    lines = [
        "# Review bundle — agent-extracted FeynRules models",
        "",
        "One directory per model that passes the full validation chain "
        "(FeynRules/Wolfram UFO compile, Hermiticity / kinetic-term / mass-spectrum "
        "checks, MadGraph import):",
        "",
        "- `<model>.fr` — the validated FeynRules file (agent-extracted; where noted, "
        "self-repaired by the closed validation loop with no human input).",
        "- `REVIEW.pdf` — the blank-slate reverse-check package: a fresh agent that saw "
        "ONLY the sanitized `.fr` (no paper, no metadata) reconstructs the physics in "
        "LaTeX; a second fresh agent compares that reconstruction against the paper "
        "term by term and grades every disagreement (convention / substantive / "
        "cosmetic). The final page is a sign-off block — **the tooling never declares "
        "the physics correct; that verdict is yours.**",
        "",
        "Validation means the tool chain accepts the model. It does not certify the "
        "physics — that is exactly what these review packages are for.",
        "",
        "| model | paper (arXiv) | provenance | review |",
        "|---|---|---|---|",
    ]
    for page, arxiv, tag, status in rows:
        lines.append(f"| {page} | {arxiv} | {tag} | {status} |")
    lines += [
        "",
        f"Benchmark context: {len(rows)} of 28 models pass the full chain with the "
        "check verdicts after the 2026-09-13 correction (CORRECTION_2026-09-13.md). "
        "Full analysis is included as REPAIR_BENCHMARK_ANALYSIS.md.",
        "",
    ]
    (BUNDLE / "README.md").write_text("\n".join(lines))
    for top in ("REPAIR_BENCHMARK_ANALYSIS.md", "CORRECTION_2026-09-13.md"):
        shutil.copy2(HERE / top, BUNDLE / top)

    zpath = HERE / "ian_review_bundle.zip"
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(BUNDLE.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(HERE))
    return zpath


def main() -> int:
    models = passing_models()
    print(f"[bundle] {len(models)} full-chain-passing models", flush=True)
    results: dict[str, dict] = {}
    if "--assemble" not in sys.argv:
        for i, (page, fr, tag) in enumerate(models, 1):
            if not fr.is_file():
                print(f"[bundle] ({i}/{len(models)}) {page}: MISSING {fr}", flush=True)
                continue
            t0 = time.time()
            print(f"[bundle] ({i}/{len(models)}) {page} [{tag}] reverse check ...", flush=True)
            res = run_reverse(page, fr)
            dt = round(time.time() - t0, 1)
            note = ("skipped (already done)" if res.get("skipped")
                    else res.get("review_package") or res.get("status")
                    or list(res)[:3])
            print(f"[bundle]     -> {note} ({dt}s)", flush=True)
            results[page] = res
    z = assemble(results)
    print(f"[bundle] wrote {z} ({z.stat().st_size // 1024} KB)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
