"""CLI entrypoint for the literature search pipeline."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import typer

from lagrangian_extraction.config import PathConfig, RankConfig, Settings
from lagrangian_extraction.models import PaperRecord, SearchQuery
from lagrangian_extraction.pipeline.search import run_search

app = typer.Typer(
    name="lex",
    help="Lagrangian Extraction — select one theory paper and prepare it for extraction.",
    no_args_is_help=True,
)


@app.callback()
def cli_root() -> None:
    """Lagrangian Extraction CLI."""


def _format_paper_line(paper: PaperRecord, rank: int) -> str:
    year = str(paper.published.year) if paper.published else "-"
    arxiv = paper.arxiv_id or "-"
    inspire = str(paper.inspire_id) if paper.inspire_id is not None else "-"
    title = paper.title[:60] + ("..." if len(paper.title) > 60 else "")
    return (
        f"{rank:<5} {paper.score:<8.4f} {arxiv:<16} {inspire:<7} "
        f"{paper.citation_count:<13} {year:<6} {title}"
    )


def _print_selected_paper(paper: PaperRecord, downloads_by_arxiv: dict[str, str | None]) -> None:
    typer.echo("Selected paper for Lagrangian extraction")
    typer.echo("-" * 60)
    typer.echo(f"Title:    {paper.title}")
    typer.echo(f"arXiv:    {paper.arxiv_id or '-'}")
    typer.echo(f"INSPIRE:  {paper.inspire_id or '-'}")
    typer.echo(f"INSPIRE cites: {paper.citation_count}")
    typer.echo(f"Score:    {paper.score:.4f}")
    if paper.score_breakdown:
        breakdown = ", ".join(f"{k}={v}" for k, v in paper.score_breakdown.items())
        typer.echo(f"Breakdown: {breakdown}")
    if paper.arxiv_id and paper.arxiv_id in downloads_by_arxiv:
        text_path = downloads_by_arxiv[paper.arxiv_id]
        if text_path:
            typer.echo(f"Text:     {text_path}")


@app.command("search")
def search_command(
    model_name: str = typer.Argument(..., help="BSM model name to search for."),
    keywords: list[str] = typer.Option(
        [],
        "--keywords",
        "-k",
        help="Additional BSM keywords (repeatable).",
    ),
    exclude_keywords: list[str] = typer.Option(
        [],
        "--exclude-keywords",
        "-K",
        help="Exclude papers containing these keywords (repeatable).",
    ),
    authors: list[str] = typer.Option(
        [],
        "--author",
        "-a",
        help="Require papers by these authors (repeatable).",
    ),
    exclude_authors: list[str] = typer.Option(
        [],
        "--exclude-author",
        "-A",
        help="Exclude papers by these authors (repeatable).",
    ),
    top_k: int = typer.Option(
        1,
        "--top-k",
        help="Number of papers to select (default 1 for Lagrangian extraction).",
    ),
    runners_up: int = typer.Option(
        0,
        "--runners-up",
        help="Also show this many alternate candidates in the output/audit log.",
    ),
    since: str | None = typer.Option(
        None, "--since", help="Earliest publication date (YYYY-MM-DD)."
    ),
    until: str | None = typer.Option(
        None, "--until", help="Latest publication date (YYYY-MM-DD)."
    ),
    sort: str = typer.Option(
        "relevance",
        "--sort",
        help="Ranking mode: relevance, combined, mostcited, mostrecent, or semantic.",
    ),
    search_mode: str = typer.Option(
        "keyword",
        "--search-mode",
        help="Query mode: keyword (title-focused) or semantic (free-text).",
    ),
    theory_only: bool = typer.Option(
        True,
        "--theory-only/--include-experiment",
        help="Keep only theory papers (hep-ph / Theory-HEP).",
    ),
    use_ads: bool = typer.Option(
        True,
        "--use-ads/--no-ads",
        help="Include NASA ADS as a third source (requires ADS_API_TOKEN).",
    ),
    require_abstract: bool = typer.Option(
        False,
        "--require-abstract",
        help="Drop papers without a sufficiently long abstract.",
    ),
    abstract_keyword_match: bool = typer.Option(
        False,
        "--abstract-keyword-match",
        help="Require at least one include-keyword to appear in the abstract.",
    ),
    abstract_exclude_only: bool = typer.Option(
        False,
        "--abstract-exclude-only",
        help="Apply exclude-keywords only against abstract text.",
    ),
    semantic_scope: str = typer.Option(
        "combined",
        "--semantic-scope",
        help="Semantic scoring scope: full, abstract, or combined.",
    ),
    probe_latex_source: bool = typer.Option(
        False,
        "--probe-latex-source",
        help="Probe arXiv LaTeX source availability for the selected paper.",
    ),
    download_pdfs: bool = typer.Option(True, "--download-pdfs/--no-download-pdfs"),
    extract_text: bool = typer.Option(True, "--extract-text/--no-extract-text"),
    w_cite: float = typer.Option(0.7, "--w-cite", help="Citation weight for combined ranking."),
    w_recent: float = typer.Option(0.3, "--w-recent", help="Recency weight for combined ranking."),
    out: Path = typer.Option(Path("runs"), "--out", help="Directory for audit JSON logs."),
    data_dir: Path = typer.Option(Path("data"), "--data-dir", help="Root data directory."),
) -> None:
    """Search INSPIRE and arXiv, select the best theory paper, and fetch its PDF/text."""
    since_date: date | None = None
    if since:
        since_date = date.fromisoformat(since)

    until_date: date | None = None
    if until:
        until_date = date.fromisoformat(until)

    if sort not in {"relevance", "combined", "mostcited", "mostrecent", "semantic"}:
        raise typer.BadParameter(
            "sort must be one of: relevance, combined, mostcited, mostrecent, semantic"
        )

    if search_mode not in {"keyword", "semantic"}:
        raise typer.BadParameter("search-mode must be one of: keyword, semantic")

    if semantic_scope not in {"full", "abstract", "combined"}:
        raise typer.BadParameter("semantic-scope must be one of: full, abstract, combined")

    query = SearchQuery(
        model_name=model_name,
        keywords=keywords,
        exclude_keywords=exclude_keywords,
        authors=authors,
        exclude_authors=exclude_authors,
        top_k=top_k,
        runners_up=runners_up,
        since=since_date,
        until=until_date,
        sort=sort,  # type: ignore[arg-type]
        search_mode=search_mode,  # type: ignore[arg-type]
        theory_only=theory_only,
        use_ads=use_ads,
        require_abstract=require_abstract,
        abstract_keyword_match=abstract_keyword_match,
        abstract_exclude_only=abstract_exclude_only,
        semantic_scope=semantic_scope,  # type: ignore[arg-type]
        probe_latex_source=probe_latex_source,
        download_pdfs=download_pdfs,
        extract_text=extract_text,
    )

    settings = Settings(
        paths=PathConfig(
            data_dir=data_dir,
            pdf_dir=data_dir / "pdfs",
            text_dir=data_dir / "text",
            src_dir=data_dir / "src",
            runs_dir=out,
        ),
        rank=RankConfig(weight_citation=w_cite, weight_recency=w_recent),
    )

    typer.echo(f"Selecting source paper for: {model_name!r}")
    if keywords:
        typer.echo(f"Keywords: {', '.join(keywords)}")
    if exclude_keywords:
        typer.echo(f"Exclude keywords: {', '.join(exclude_keywords)}")
    if authors:
        typer.echo(f"Authors: {', '.join(authors)}")
    if exclude_authors:
        typer.echo(f"Exclude authors: {', '.join(exclude_authors)}")
    if theory_only:
        typer.echo("Filter: theory papers only")
    if require_abstract:
        typer.echo("Filter: require abstract")
    if abstract_keyword_match:
        typer.echo("Filter: keyword must appear in abstract")
    if semantic_scope != "combined":
        typer.echo(f"Semantic scope: {semantic_scope}")

    audit = run_search(query, settings)

    downloads_by_arxiv = {
        item.arxiv_id: item.text_path for item in audit.downloads if item.text_path
    }

    typer.echo("")
    if audit.selected_paper is not None:
        _print_selected_paper(audit.selected_paper, downloads_by_arxiv)
    else:
        typer.echo("No suitable paper found.")

    if audit.runners_up:
        typer.echo("")
        typer.echo("Runners-up")
        header = (
            f"{'Rank':<5} {'Score':<8} {'arXiv ID':<16} {'INSPIRE':<7} "
            f"{'INSPIRE cites':<13} {'Year':<6} Title"
        )
        typer.echo(header)
        typer.echo("-" * 98)
        for i, paper in enumerate(audit.runners_up, start=2):
            typer.echo(_format_paper_line(paper, i))

    if top_k > 1:
        typer.echo("")
        typer.echo("Additional selections")
        typer.echo(header)
        typer.echo("-" * 98)
        for i, paper in enumerate(audit.candidates[1:], start=2):
            typer.echo(_format_paper_line(paper, i))

    typer.echo("")
    typer.echo(f"Pool searched: {audit.raw_counts.merged_unique} unique papers")
    typer.echo(f"INSPIRE hits:  {audit.raw_counts.inspire_hits}")
    typer.echo(f"arXiv hits:    {audit.raw_counts.arxiv_hits}")
    typer.echo(f"ADS hits:      {audit.raw_counts.ads_hits}")
    if audit.latex_probe is not None:
        probe = audit.latex_probe
        typer.echo(
            f"LaTeX source:  available={probe.available}, format={probe.format}, "
            f"main_tex={probe.main_tex or '-'}"
        )
    typer.echo(f"Audit log:     {out / f'{audit.run_id}.json'}")

    if audit.errors:
        typer.echo("")
        typer.echo("Errors:")
        for err in audit.errors:
            typer.echo(f"  - {err}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
