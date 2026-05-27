"""Download arXiv PDFs and extract text with PyMuPDF."""

from __future__ import annotations

import hashlib
import time
from pathlib import Path

import pymupdf

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import PathConfig
from lagrangian_extraction.models import LocalPDF, PaperRecord


def _safe_arxiv_filename(arxiv_id: str) -> str:
    return arxiv_id.replace("/", "_")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _is_valid_pdf(path: Path) -> bool:
    with path.open("rb") as fh:
        header = fh.read(5)
    return header == b"%PDF-"


def download_pdf(
    http: RateLimitedClient,
    paper: PaperRecord,
    paths: PathConfig,
) -> LocalPDF:
    """Download a single PDF, using cache when available."""
    if not paper.arxiv_id:
        return LocalPDF(arxiv_id="unknown", error="No arXiv ID available for download")

    arxiv_id = paper.arxiv_id
    filename = _safe_arxiv_filename(arxiv_id)
    pdf_path = paths.pdf_dir / f"{filename}.pdf"
    paths.pdf_dir.mkdir(parents=True, exist_ok=True)

    if pdf_path.exists() and _is_valid_pdf(pdf_path):
        return LocalPDF(
            arxiv_id=arxiv_id,
            pdf_path=str(pdf_path),
            bytes=pdf_path.stat().st_size,
            sha256=_sha256(pdf_path),
            cached=True,
        )

    pdf_url = paper.pdf_url or f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    try:
        response = http.get(pdf_url)
        pdf_path.write_bytes(response.content)
        if not _is_valid_pdf(pdf_path):
            pdf_path.unlink(missing_ok=True)
            return LocalPDF(arxiv_id=arxiv_id, error="Downloaded file is not a valid PDF")
        return LocalPDF(
            arxiv_id=arxiv_id,
            pdf_path=str(pdf_path),
            bytes=pdf_path.stat().st_size,
            sha256=_sha256(pdf_path),
            cached=False,
        )
    except Exception as exc:  # noqa: BLE001 - surface per-paper errors in audit log
        return LocalPDF(arxiv_id=arxiv_id, error=str(exc))


def extract_text(local_pdf: LocalPDF, paths: PathConfig) -> LocalPDF:
    """Extract plain text from a downloaded PDF."""
    if local_pdf.error or not local_pdf.pdf_path:
        return local_pdf

    pdf_path = Path(local_pdf.pdf_path)
    text_path = paths.text_dir / f"{_safe_arxiv_filename(local_pdf.arxiv_id)}.txt"
    paths.text_dir.mkdir(parents=True, exist_ok=True)

    if text_path.exists() and text_path.stat().st_size > 0:
        return local_pdf.model_copy(update={"text_path": str(text_path), "cached": True})

    start = time.perf_counter()
    try:
        doc = pymupdf.open(pdf_path)
        pages_text = [page.get_text("text") for page in doc]
        doc.close()
        text = "\n\n".join(pages_text)
        text_path.write_text(text, encoding="utf-8")
        elapsed = time.perf_counter() - start
        return local_pdf.model_copy(
            update={
                "text_path": str(text_path),
                "pages": len(pages_text),
                "extract_seconds": round(elapsed, 4),
            }
        )
    except Exception as exc:  # noqa: BLE001
        return local_pdf.model_copy(update={"error": str(exc)})


def fetch_pdfs_and_extract(
    http: RateLimitedClient,
    papers: list[PaperRecord],
    paths: PathConfig,
    *,
    download: bool = True,
    extract: bool = True,
) -> list[LocalPDF]:
    """Download and optionally extract text for all papers with arXiv IDs."""
    results: list[LocalPDF] = []
    for paper in papers:
        if not paper.arxiv_id:
            continue
        if not download:
            results.append(LocalPDF(arxiv_id=paper.arxiv_id, error="Download skipped"))
            continue
        local = download_pdf(http, paper, paths)
        if extract and local.pdf_path and not local.error:
            local = extract_text(local, paths)
        results.append(local)
    return results
