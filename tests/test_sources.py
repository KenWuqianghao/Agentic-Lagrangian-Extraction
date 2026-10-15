"""Tests for LaTeX source probing."""

from __future__ import annotations

import gzip
import io
import tarfile
from pathlib import Path

import respx

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import PathConfig, RateLimitConfig
from lagrangian_extraction.models import PaperRecord
from lagrangian_extraction.pipeline.sources import (
    compare_text_fidelity,
    probe_arxiv_source,
    probe_selected_paper,
)


def _make_tex_tar(tex_name: str, content: str) -> bytes:
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        data = content.encode("utf-8")
        info = tarfile.TarInfo(name=tex_name)
        info.size = len(data)
        tar.addfile(info, io.BytesIO(data))
    return buf.getvalue()


def _make_single_tex_gz(content: str) -> bytes:
    return gzip.compress(content.encode("utf-8"))


def test_compare_text_fidelity() -> None:
    tex = "\\section{Model}\n$L = y \\bar{Q} L$\n\\begin{equation} E=mc^2 \\end{equation}"
    pdf = "Model L = y Q L E=mc^2"
    result = compare_text_fidelity(tex, pdf)
    assert result["tex_char_count"] > result["pdf_char_count"]
    assert result["tex_equation_markers"] >= result["pdf_equation_markers"]


@respx.mock
def test_probe_arxiv_source_tex_tar(tmp_path: Path) -> None:
    tex_content = "\\documentclass{article}\n\\section{Lagrangian}\n$L = ...$"
    tar_bytes = _make_tex_tar("main.tex", tex_content)
    respx.get("https://arxiv.org/src/1701.00001").respond(
        content=tar_bytes,
        headers={"content-type": "application/x-eprint-tar"},
    )

    paths = PathConfig(src_dir=tmp_path / "src")
    with RateLimitedClient(RateLimitConfig()) as http:
        result = probe_arxiv_source(http, "1701.00001", paths)

    assert result.available is True
    assert result.format == "tex_tar"
    assert result.main_tex == "main.tex"
    assert result.tex_char_count > 0


@respx.mock
def test_probe_arxiv_source_single_tex(tmp_path: Path) -> None:
    tex_content = "\\documentclass{article}\nScalar leptoquark Lagrangian"
    respx.get("https://arxiv.org/src/2002.12544").respond(
        content=_make_single_tex_gz(tex_content),
        headers={"content-type": "application/x-eprint"},
    )

    paths = PathConfig(src_dir=tmp_path / "src")
    with RateLimitedClient(RateLimitConfig()) as http:
        result = probe_arxiv_source(http, "2002.12544", paths)

    assert result.available is True
    assert result.format == "single_tex"


@respx.mock
def test_probe_selected_paper_with_pdf_text(tmp_path: Path) -> None:
    tex_content = "\\documentclass{article}\n\\section{Model}\n$L = y Q L$"
    tar_bytes = _make_tex_tar("paper.tex", tex_content)
    respx.get("https://arxiv.org/src/1701.00001").respond(
        content=tar_bytes,
        headers={"content-type": "application/x-eprint-tar"},
    )

    text_dir = tmp_path / "text"
    text_dir.mkdir()
    (text_dir / "1701.00001.txt").write_text("Model L = y Q L", encoding="utf-8")

    paths = PathConfig(src_dir=tmp_path / "src", text_dir=text_dir)
    paper = PaperRecord(title="Test", arxiv_id="1701.00001")

    with RateLimitedClient(RateLimitConfig()) as http:
        result = probe_selected_paper(paper, paths, http)

    assert result is not None
    assert result.available is True
    assert result.pdf_text_char_count == len("Model L = y Q L")
