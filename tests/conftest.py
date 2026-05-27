"""Shared test helpers."""

from __future__ import annotations

from pathlib import Path

import pymupdf

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def make_synthetic_pdf(path: Path, pages: list[str]) -> Path:
    """Create a minimal multi-page PDF for extraction tests."""
    doc = pymupdf.open()
    for text in pages:
        page = doc.new_page()
        page.insert_text((72, 72), text)
    doc.save(path)
    doc.close()
    return path
