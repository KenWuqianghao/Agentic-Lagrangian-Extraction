"""End-to-end test for the literature search pipeline."""

from __future__ import annotations

import json
from pathlib import Path

import respx

from lagrangian_extraction.config import ARXIV_BASE_URL, INSPIRE_BASE_URL, PathConfig, Settings
from lagrangian_extraction.models import SearchQuery
from lagrangian_extraction.pipeline.audit import write_audit_log
from lagrangian_extraction.pipeline.search import run_search
from tests.conftest import load_fixture, make_synthetic_pdf


@respx.mock
def test_search_e2e_with_mocked_apis(tmp_path: Path) -> None:
    inspire_payload = json.loads(load_fixture("inspire_leptoquark.json"))
    arxiv_payload = load_fixture("arxiv_leptoquark.xml")
    pdf_bytes = make_synthetic_pdf(tmp_path / "sample.pdf", ["Lagrangian terms here"]).read_bytes()

    respx.get(INSPIRE_BASE_URL).respond(json=inspire_payload)
    respx.get(ARXIV_BASE_URL).respond(text=arxiv_payload)
    respx.get(url__regex=r"https://arxiv\.org/pdf/.*").respond(content=pdf_bytes)

    settings = Settings(
        paths=PathConfig(
            data_dir=tmp_path / "data",
            pdf_dir=tmp_path / "data" / "pdfs",
            text_dir=tmp_path / "data" / "text",
            runs_dir=tmp_path / "runs",
        )
    )

    query = SearchQuery(
        model_name="scalar leptoquark",
        keywords=["BSM"],
        top_k=3,
        download_pdfs=True,
        extract_text=True,
    )

    audit = run_search(query, settings)

    assert audit.finished_at is not None
    assert audit.inspire_url is not None
    assert audit.arxiv_url is not None
    assert audit.raw_counts.inspire_hits == 2
    assert audit.raw_counts.arxiv_hits == 2
    assert len(audit.candidates) <= 3
    assert audit.candidates[0].score >= 0

    audit_path = tmp_path / "runs" / f"{audit.run_id}.json"
    assert audit_path.exists()
    saved = json.loads(audit_path.read_text(encoding="utf-8"))
    assert saved["query"]["model_name"] == "scalar leptoquark"
    assert "candidates" in saved


def test_write_audit_log_atomic(tmp_path: Path) -> None:
    from datetime import UTC, datetime

    from lagrangian_extraction.models import AuditRun

    audit = AuditRun(
        query=SearchQuery(model_name="test"),
        started_at=datetime.now(UTC),
        finished_at=datetime.now(UTC),
    )
    path = write_audit_log(audit, tmp_path)
    assert path.exists()
    assert not path.with_suffix(".json.tmp").exists()
