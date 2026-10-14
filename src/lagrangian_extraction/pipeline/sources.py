"""Probe arXiv LaTeX source availability and compare with PDF text."""

from __future__ import annotations

import gzip
import io
import re
import tarfile

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import PathConfig
from lagrangian_extraction.models import PaperRecord, SourceProbeResult
from lagrangian_extraction.utils import normalize_arxiv_id

_DOCUMENTCLASS_RE = re.compile(r"\\documentclass")
_SECTION_RE = re.compile(r"\\section\*?\{")
_EQUATION_MARKERS = ("$", "\\begin{equation}", "\\begin{align}")


def _safe_arxiv_filename(arxiv_id: str) -> str:
    return arxiv_id.replace("/", "_")


def _arxiv_src_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/src/{arxiv_id}"


def _count_equation_markers(text: str) -> int:
    return sum(text.count(marker) for marker in _EQUATION_MARKERS)


def _count_sections(text: str) -> int:
    return len(_SECTION_RE.findall(text))


def compare_text_fidelity(tex_text: str, pdf_text: str) -> dict[str, int | float]:
    tex_chars = len(tex_text)
    pdf_chars = len(pdf_text)
    ratio = tex_chars / pdf_chars if pdf_chars else 0.0
    return {
        "tex_char_count": tex_chars,
        "pdf_char_count": pdf_chars,
        "char_ratio": round(ratio, 4),
        "tex_equation_markers": _count_equation_markers(tex_text),
        "pdf_equation_markers": _count_equation_markers(pdf_text),
        "tex_section_count": _count_sections(tex_text),
        "pdf_section_count": _count_sections(pdf_text),
    }


def _pick_main_tex(tex_files: dict[str, str]) -> str | None:
    if not tex_files:
        return None
    with_documentclass = [
        name for name, content in tex_files.items() if _DOCUMENTCLASS_RE.search(content)
    ]
    if with_documentclass:
        return max(with_documentclass, key=lambda n: len(tex_files[n]))
    return max(tex_files, key=lambda n: len(tex_files[n]))


def _extract_tex_from_bytes(data: bytes, content_type: str) -> tuple[str, str, dict[str, str]]:
    """Return (format, main_tex_name, tex_files dict)."""
    tex_files: dict[str, str] = {}

    if "eprint-tar" in content_type or data[:2] == b"\x1f\x8b":
        try:
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
                for member in tar.getmembers():
                    if not member.isfile() or not member.name.endswith(".tex"):
                        continue
                    extracted = tar.extractfile(member)
                    if extracted is None:
                        continue
                    tex_files[member.name] = extracted.read().decode("utf-8", errors="replace")
        except (tarfile.TarError, OSError):
            pass
        if tex_files:
            main = _pick_main_tex(tex_files)
            return "tex_tar", main or "", tex_files

    if "eprint" in content_type or data[:2] == b"\x1f\x8b":
        try:
            decompressed = gzip.decompress(data)
            if decompressed.strip().startswith(b"\\"):
                name = "main.tex"
                tex_files[name] = decompressed.decode("utf-8", errors="replace")
                return "single_tex", name, tex_files
        except OSError:
            pass

    if data.strip().startswith(b"\\"):
        tex_files["main.tex"] = data.decode("utf-8", errors="replace")
        return "single_tex", "main.tex", tex_files

    if data[:4] == b"%PDF":
        return "pdf_only", "", {}

    return "unavailable", "", {}


def probe_arxiv_source(
    http: RateLimitedClient,
    arxiv_id: str,
    paths: PathConfig,
) -> SourceProbeResult:
    """Download and inspect arXiv /src/ bundle for LaTeX content."""
    arxiv_id = normalize_arxiv_id(arxiv_id) or arxiv_id
    src_url = _arxiv_src_url(arxiv_id)
    result = SourceProbeResult(arxiv_id=arxiv_id, src_url=src_url, available=False)

    try:
        response = http.get(src_url)
        content_type = response.headers.get("content-type", "")
        fmt, main_tex, tex_files = _extract_tex_from_bytes(response.content, content_type)

        if fmt in {"tex_tar", "single_tex"} and main_tex and main_tex in tex_files:
            tex_text = tex_files[main_tex]
            cache_dir = paths.src_dir / _safe_arxiv_filename(arxiv_id)
            cache_dir.mkdir(parents=True, exist_ok=True)
            (cache_dir / main_tex).write_text(tex_text, encoding="utf-8")

            return result.model_copy(
                update={
                    "available": True,
                    "format": fmt,  # type: ignore[arg-type]
                    "main_tex": main_tex,
                    "tex_char_count": len(tex_text),
                    "equation_markers": _count_equation_markers(tex_text),
                    "section_count": _count_sections(tex_text),
                }
            )

        if fmt == "pdf_only":
            return result.model_copy(update={"format": "pdf_only", "error": "Source is PDF-only"})

        return result.model_copy(
            update={"format": "unavailable", "error": "No LaTeX content found in source bundle"}
        )
    except Exception as exc:  # noqa: BLE001
        return result.model_copy(update={"format": "error", "error": str(exc)})


def probe_selected_paper(
    paper: PaperRecord,
    paths: PathConfig,
    http: RateLimitedClient,
) -> SourceProbeResult | None:
    """Probe LaTeX source for the selected paper and compare with cached PDF text."""
    if not paper.arxiv_id:
        return None

    probe = probe_arxiv_source(http, paper.arxiv_id, paths)

    text_path = paths.text_dir / f"{_safe_arxiv_filename(paper.arxiv_id)}.txt"
    if text_path.exists():
        pdf_text = text_path.read_text(encoding="utf-8")
        probe = probe.model_copy(update={"pdf_text_char_count": len(pdf_text)})
        if probe.available and probe.main_tex:
            tex_path = paths.src_dir / _safe_arxiv_filename(paper.arxiv_id) / probe.main_tex
            if tex_path.exists():
                tex_text = tex_path.read_text(encoding="utf-8")
                fidelity = compare_text_fidelity(tex_text, pdf_text)
                probe = probe.model_copy(
                    update={
                        "equation_markers": int(fidelity["tex_equation_markers"]),
                        "section_count": int(fidelity["tex_section_count"]),
                    }
                )

    return probe
