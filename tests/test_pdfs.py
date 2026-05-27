"""Tests for PDF download and text extraction."""

from __future__ import annotations

from pathlib import Path

import respx

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import PathConfig, RateLimitConfig
from lagrangian_extraction.models import LocalPDF, PaperRecord
from lagrangian_extraction.pipeline.pdfs import download_pdf, extract_text, fetch_pdfs_and_extract
from tests.conftest import make_synthetic_pdf


def test_extract_text_from_synthetic_pdf(tmp_path: Path) -> None:
    pdf_path = make_synthetic_pdf(tmp_path / "test.pdf", ["Page one text.", "Page two text."])
    paths = PathConfig(pdf_dir=tmp_path, text_dir=tmp_path / "text")
    local = LocalPDF(arxiv_id="1701.00001", pdf_path=str(pdf_path), bytes=pdf_path.stat().st_size)
    result = extract_text(local, paths)
    assert result.text_path is not None
    assert result.pages == 2
    text = Path(result.text_path).read_text(encoding="utf-8")
    assert "Page one text." in text
    assert "Page two text." in text


@respx.mock
def test_download_pdf_validates_magic_bytes(tmp_path: Path) -> None:
    paths = PathConfig(pdf_dir=tmp_path, text_dir=tmp_path / "text")
    paper = PaperRecord(
        title="Test",
        arxiv_id="1701.00001",
        pdf_url="https://arxiv.org/pdf/1701.00001.pdf",
    )
    respx.get("https://arxiv.org/pdf/1701.00001.pdf").respond(content=b"NOTPDF")

    with RateLimitedClient(RateLimitConfig()) as http:
        result = download_pdf(http, paper, paths)

    assert result.error is not None
    assert "not a valid PDF" in result.error


@respx.mock
def test_download_pdf_caches_valid_file(tmp_path: Path) -> None:
    paths = PathConfig(pdf_dir=tmp_path, text_dir=tmp_path / "text")
    pdf_bytes = make_synthetic_pdf(tmp_path / "source.pdf", ["cached content"]).read_bytes()
    paper = PaperRecord(
        title="Test",
        arxiv_id="1701.00001",
        pdf_url="https://arxiv.org/pdf/1701.00001.pdf",
    )
    respx.get("https://arxiv.org/pdf/1701.00001.pdf").respond(content=pdf_bytes)

    with RateLimitedClient(RateLimitConfig()) as http:
        first = download_pdf(http, paper, paths)
        second = download_pdf(http, paper, paths)

    assert first.error is None
    assert second.cached is True
    assert first.pdf_path == second.pdf_path


@respx.mock
def test_fetch_pdfs_and_extract_end_to_end(tmp_path: Path) -> None:
    paths = PathConfig(pdf_dir=tmp_path / "pdfs", text_dir=tmp_path / "text")
    pdf_bytes = make_synthetic_pdf(tmp_path / "source.pdf", ["Extract me"]).read_bytes()
    paper = PaperRecord(
        title="Test",
        arxiv_id="1701.00001",
        pdf_url="https://arxiv.org/pdf/1701.00001.pdf",
    )
    respx.get("https://arxiv.org/pdf/1701.00001.pdf").respond(content=pdf_bytes)

    with RateLimitedClient(RateLimitConfig()) as http:
        results = fetch_pdfs_and_extract(http, [paper], paths, download=True, extract=True)

    assert len(results) == 1
    assert results[0].text_path is not None
    assert "Extract me" in Path(results[0].text_path).read_text(encoding="utf-8")
