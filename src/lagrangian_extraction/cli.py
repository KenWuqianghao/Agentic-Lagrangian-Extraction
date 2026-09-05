"""CLI entrypoint for the literature search pipeline."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import typer

from lagrangian_extraction.config import PathConfig, RankConfig, Settings
from lagrangian_extraction.models import SearchQuery
from lagrangian_extraction.pipeline.search import run_search

app = typer.Typer(
    name="lag-extract",
    help="Lagrangian Extraction — Stage 1 literature search (INSPIRE + arXiv).",
    no_args_is_help=True,
)


@app.callback()
def cli_root() -> None:
    """Lagrangian Extraction CLI."""


@app.command("search")
def search_command(
    model_name: str = typer.Argument(..., help="BSM model name to search for."),
    keywords: list[str] = typer.Option(
        [],
        "--keywords",
        "-k",
        help="Additional BSM keywords (repeatable).",
    ),
    top_k: int = typer.Option(10, "--top-k", help="Number of ranked candidates to return."),
    since: str | None = typer.Option(
        None, "--since", help="Earliest publication date (YYYY-MM-DD)."
    ),
    sort: str = typer.Option(
        "combined",
        "--sort",
        help="Ranking mode: combined, mostcited, or mostrecent.",
    ),
    download_pdfs: bool = typer.Option(True, "--download-pdfs/--no-download-pdfs"),
    extract_text: bool = typer.Option(True, "--extract-text/--no-extract-text"),
    skip_arxiv: bool = typer.Option(
        False,
        "--skip-arxiv",
        help="Search INSPIRE only (useful when arXiv API is rate-limiting your IP).",
    ),
    w_cite: float = typer.Option(0.7, "--w-cite", help="Citation weight for combined ranking."),
    w_recent: float = typer.Option(0.3, "--w-recent", help="Recency weight for combined ranking."),
    out: Path = typer.Option(Path("runs"), "--out", help="Directory for audit JSON logs."),
    data_dir: Path = typer.Option(Path("data"), "--data-dir", help="Root data directory."),
) -> None:
    """Search INSPIRE and arXiv, rank candidates, and optionally fetch PDFs."""
    since_date: date | None = None
    if since:
        since_date = date.fromisoformat(since)

    if sort not in {"combined", "mostcited", "mostrecent"}:
        raise typer.BadParameter("sort must be one of: combined, mostcited, mostrecent")

    query = SearchQuery(
        model_name=model_name,
        keywords=keywords,
        top_k=top_k,
        since=since_date,
        sort=sort,  # type: ignore[arg-type]
        download_pdfs=download_pdfs,
        extract_text=extract_text,
        skip_arxiv=skip_arxiv,
    )

    settings = Settings(
        paths=PathConfig(
            data_dir=data_dir,
            pdf_dir=data_dir / "pdfs",
            text_dir=data_dir / "text",
            runs_dir=out,
        ),
        rank=RankConfig(weight_citation=w_cite, weight_recency=w_recent),
    )

    typer.echo(f"Searching for: {model_name!r}")
    if keywords:
        typer.echo(f"Keywords: {', '.join(keywords)}")

    audit = run_search(query, settings)

    typer.echo("")
    typer.echo(f"{'Rank':<5} {'Score':<8} {'arXiv ID':<16} {'Cites':<7} {'Year':<6} Title")
    typer.echo("-" * 90)
    for i, paper in enumerate(audit.candidates, start=1):
        year = str(paper.published.year) if paper.published else "-"
        arxiv = paper.arxiv_id or "-"
        title = paper.title[:50] + ("..." if len(paper.title) > 50 else "")
        typer.echo(
            f"{i:<5} {paper.score:<8.4f} {arxiv:<16} {paper.citation_count:<7} {year:<6} {title}"
        )

    typer.echo("")
    typer.echo(f"INSPIRE hits: {audit.raw_counts.inspire_hits}")
    typer.echo(f"arXiv hits:   {audit.raw_counts.arxiv_hits}")
    typer.echo(f"Merged:       {audit.raw_counts.merged_unique}")
    typer.echo(f"Audit log:    {out / f'{audit.run_id}.json'}")

    if audit.errors:
        typer.echo("")
        typer.echo("Errors:")
        for err in audit.errors:
            typer.echo(f"  - {err}")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
