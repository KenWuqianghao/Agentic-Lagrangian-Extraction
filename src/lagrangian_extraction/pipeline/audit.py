"""Audit trail writer for literature search runs."""

from __future__ import annotations

import json
from pathlib import Path

from lagrangian_extraction.models import AuditRun


def write_audit_log(audit: AuditRun, runs_dir: Path) -> Path:
    """Write audit JSON atomically (temp file then rename)."""
    runs_dir.mkdir(parents=True, exist_ok=True)
    final_path = runs_dir / f"{audit.run_id}.json"
    tmp_path = final_path.with_suffix(".json.tmp")

    payload = audit.model_dump(mode="json")
    tmp_path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    tmp_path.replace(final_path)
    return final_path
