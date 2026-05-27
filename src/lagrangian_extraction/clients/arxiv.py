"""arXiv API client."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from datetime import date
from typing import Literal
from urllib.parse import urlencode

from lagrangian_extraction.clients._http import RateLimitedClient
from lagrangian_extraction.config import ARXIV_BASE_URL
from lagrangian_extraction.models import Author, PaperRecord
from lagrangian_extraction.utils import normalize_arxiv_id

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


class ArxivClient:
    """Search arXiv via the Atom export API."""

    def __init__(self, http: RateLimitedClient) -> None:
        self._http = http

    @staticmethod
    def build_query(model_name: str, keywords: list[str]) -> str:
        model_clause = f'(ti:"{model_name}" OR abs:"{model_name}")'
        if keywords:
            kw_clause = " OR ".join(f"abs:{kw}" for kw in keywords)
            return f"cat:hep-ph AND {model_clause} AND ({kw_clause})"
        return f"cat:hep-ph AND {model_clause}"

    def search(
        self,
        query: str,
        *,
        max_results: int = 25,
        sort_by: Literal["relevance", "lastUpdatedDate", "submittedDate"] = "relevance",
        sort_order: Literal["ascending", "descending"] = "descending",
    ) -> tuple[list[PaperRecord], str, int]:
        params = {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        }
        url = f"{ARXIV_BASE_URL}?{urlencode(params)}"
        response = self._http.get(url)
        records = self._parse_feed(response.text)
        return records, url, len(records)

    def _parse_feed(self, xml_text: str) -> list[PaperRecord]:
        root = ET.fromstring(xml_text)
        records: list[PaperRecord] = []
        for entry in root.findall("atom:entry", ATOM_NS):
            record = self._parse_entry(entry)
            if record is not None:
                records.append(record)
        return records

    def _parse_entry(self, entry: ET.Element) -> PaperRecord | None:
        title_el = entry.find("atom:title", ATOM_NS)
        if title_el is None or not title_el.text:
            return None
        title = " ".join(title_el.text.split())

        summary_el = entry.find("atom:summary", ATOM_NS)
        if summary_el is not None and summary_el.text:
            abstract = " ".join(summary_el.text.split())
        else:
            abstract = None

        authors = []
        for author_el in entry.findall("atom:author", ATOM_NS):
            name_el = author_el.find("atom:name", ATOM_NS)
            if name_el is not None and name_el.text:
                authors.append(Author(name=name_el.text.strip()))

        published = self._parse_date(entry.find("atom:published", ATOM_NS))
        updated = self._parse_date(entry.find("atom:updated", ATOM_NS))

        arxiv_id = self._extract_arxiv_id(entry)
        if not arxiv_id:
            return None
        arxiv_id = normalize_arxiv_id(arxiv_id) or arxiv_id

        categories: list[str] = []
        primary = entry.find("arxiv:primary_category", ATOM_NS)
        if primary is not None and primary.get("term"):
            categories.append(primary.get("term", ""))
        for cat in entry.findall("atom:category", ATOM_NS):
            term = cat.get("term")
            if term and term not in categories:
                categories.append(term)

        pdf_url = None
        abs_url = None
        for link in entry.findall("atom:link", ATOM_NS):
            rel = link.get("rel", "")
            link_type = link.get("type", "")
            href = link.get("href", "")
            if rel == "alternate":
                abs_url = href
            if link_type == "application/pdf":
                pdf_url = href
        if pdf_url is None:
            pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        if abs_url is None:
            abs_url = f"https://arxiv.org/abs/{arxiv_id}"

        return PaperRecord(
            arxiv_id=arxiv_id,
            title=title,
            authors=authors,
            abstract=abstract,
            categories=categories,
            published=published,
            updated=updated,
            pdf_url=pdf_url,
            abs_url=abs_url,
            sources=["arxiv"],
        )

    @staticmethod
    def _parse_date(element: ET.Element | None) -> date | None:
        if element is None or not element.text:
            return None
        return date.fromisoformat(element.text[:10])

    @staticmethod
    def _extract_arxiv_id(entry: ET.Element) -> str | None:
        id_el = entry.find("atom:id", ATOM_NS)
        if id_el is None or not id_el.text:
            return None
        match = re.search(r"arxiv\.org/abs/(.+)$", id_el.text.strip())
        if match:
            return match.group(1)
        return None
