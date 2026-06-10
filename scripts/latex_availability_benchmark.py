#!/usr/bin/env python3
"""Benchmark LaTeX source availability for papers from an audit log or live search."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Allow running without install
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import PathConfig, RateLimitConfig, Settings
from lagrangian_extraction.models import PaperRecord, SearchQuery
from lagrangian_extraction.pipeline.search import run_search
from lagrangian_extraction.pipeline.sources import compare_text_fidelity, probe_arxiv_source


def _load_papers_from_audit(audit_path: Path, limit: int) -> list[PaperRecord]:
    data = json.loads(audit_path.read_text(encoding="utf-8"))
    papers: list[PaperRecord] = []
    if data.get("selected_paper"):
        papers.append(PaperRecord.model_validate(data["selected_paper"]))
    for item in data.get("runners_up", []):
        papers.append(PaperRecord.model_validate(item))
    for item in data.get("candidates", []):
        papers.append(PaperRecord.model_validate(item))
    seen: set[str] = set()
    unique: list[PaperRecord] = []
    for paper in papers:
        if paper.arxiv_id and paper.arxiv_id not in seen:
            seen.add(paper.arxiv_id)
            unique.append(paper)
    return unique[:limit]


def _markdown_table(rows: list[dict]) -> str:
    if not rows:
        return "No papers to benchmark.\n"

    headers = list(rows[0].keys())
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row[h]) for h in headers) + " |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark arXiv LaTeX source availability")
    parser.add_argument("--audit", type=Path, help="Path to audit JSON from a prior search run")
    parser.add_argument("--limit", type=int, default=10, help="Max papers to probe")
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument(
        "--live-search",
        action="store_true",
        help="Run a fresh scalar leptoquark search instead of using --audit",
    )
    args = parser.parse_args()

    settings = Settings(
        paths=PathConfig(
            data_dir=args.data_dir,
            pdf_dir=args.data_dir / "pdfs",
            text_dir=args.data_dir / "text",
            src_dir=args.data_dir / "src",
        )
    )

    if args.live_search:
        audit = run_search(
            SearchQuery(
                model_name="scalar leptoquark",
                keywords=["BSM", "leptoquark"],
                since=__import__("datetime").date(2015, 1, 1),
                top_k=args.limit,
                runners_up=0,
                download_pdfs=False,
                use_ads=False,
            ),
            settings,
        )
        papers = [p for p in audit.candidates if p.arxiv_id]
    elif args.audit:
        papers = _load_papers_from_audit(args.audit, args.limit)
    else:
        parser.error("Provide --audit PATH or --live-search")

    rows: list[dict] = []
    available = 0

    with RateLimitedClient(RateLimitConfig()) as http:
        for paper in papers:
            if not paper.arxiv_id:
                continue
            probe = probe_arxiv_source(http, paper.arxiv_id, settings.paths)
            if probe.available:
                available += 1

            pdf_chars = None
            tex_path = settings.paths.text_dir / f"{paper.arxiv_id.replace('/', '_')}.txt"
            if tex_path.exists():
                pdf_text = tex_path.read_text(encoding="utf-8")
                pdf_chars = len(pdf_text)
                if probe.available and probe.main_tex:
                    safe_id = paper.arxiv_id.replace("/", "_")
                    src_file = settings.paths.src_dir / safe_id / probe.main_tex
                    if src_file.exists():
                        fidelity = compare_text_fidelity(
                            src_file.read_text(encoding="utf-8"), pdf_text
                        )
                        pdf_chars = fidelity["pdf_char_count"]

            rows.append(
                {
                    "arxiv_id": paper.arxiv_id,
                    "title": paper.title[:50],
                    "latex_available": probe.available,
                    "format": probe.format,
                    "main_tex": probe.main_tex or "-",
                    "tex_chars": probe.tex_char_count,
                    "pdf_chars": pdf_chars or "-",
                }
            )

    total = len(rows)
    rate = (available / total * 100) if total else 0.0

    print("# LaTeX Source Availability Benchmark\n")
    print(_markdown_table(rows))
    print(f"**Availability:** {available}/{total} ({rate:.0f}%)\n")
    print("## Findings\n")
    print(
        "- **arXiv** exposes author LaTeX via "
        "`https://arxiv.org/src/{arxiv_id}` (gzipped tar or single `.tex.gz`)."
    )
    print(
        "- **INSPIRE** does not host downloadable author LaTeX; "
        "it indexes metadata and optional full-text for search only."
    )
    print(
        "- **Recommendation for Stage 2:** use arXiv `/src/` as the primary "
        "structured source; keep PyMuPDF PDF text as fallback.\n"
    )


if __name__ == "__main__":
    main()
