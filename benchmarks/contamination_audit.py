#!/usr/bin/env python3
"""
# contamination_audit.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Did the extraction agent read the answer key?

The original benchmark fleet (db_launch.sh) ran codex with the whole repo
visible, and the physicist reference .fr files sit under
eval/reference_cache/<page>/. This audit walks each run's codex_events.jsonl
for shell commands that READ (cat/sed/head/grep/...) a reference file, and
classifies the run:

    OWN REFERENCE READ    the agent read its own model's reference -> the
                          extraction score measures copying, not extraction
    other reference read  read some other model's reference (idiom leakage)
    listed only           reference paths appeared in a listing, never read
    clean                 no reference path in any command

Writes contamination_audit.json next to this file.

    python eval/benchmark_runs/contamination_audit.py
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
READ = re.compile(r"\b(cat|sed|head|tail|less|more|awk|grep|rg|python3?|bat|nl)\b")


def commands(events_path: Path) -> list[str]:
    out: list[str] = []
    for line in events_path.read_text(errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        blob = json.dumps(rec)
        for m in re.finditer(r'"command"\s*:\s*(\[[^\]]*\]|"(?:[^"\\]|\\.)*")', blob):
            try:
                v = json.loads(m.group(1))
                out.append(" ".join(v) if isinstance(v, list) else v)
            except Exception:                               # noqa: BLE001
                out.append(m.group(1))
    return out


def audit() -> list[dict]:
    cands = json.loads((HERE / "db_candidates.json").read_text())["candidates"]
    rows = []
    for c in sorted(cands, key=lambda c: c["page"]):
        page = c["page"]
        ev = HERE / page / "codex_events.jsonl"
        if not ev.is_file():
            rows.append({"page": page, "verdict": "no log"})
            continue
        cmds = commands(ev)
        own = f"reference_cache/{page}/"
        own_read = [x for x in cmds if own in x and READ.search(x)]
        other_read = [x for x in cmds if "reference_cache/" in x and READ.search(x) and own not in x]
        listed = [x for x in cmds if "reference_cache" in x and not READ.search(x)]
        verdict = ("OWN REFERENCE READ" if own_read else "other reference read" if other_read
                   else "listed only" if listed else "clean")
        rows.append({"page": page, "verdict": verdict, "own_read": len(own_read),
                     "other_read": len(other_read), "listed": len(listed),
                     "example": (own_read or other_read or [""])[0][:200]})
    return rows


def main() -> int:
    rows = audit()
    (HERE / "contamination_audit.json").write_text(json.dumps(rows, indent=1))
    for r in rows:
        print(f"{r['page']:24} {r['verdict']:22} own={r.get('own_read', 0):>2} other={r.get('other_read', 0):>2}")
    print("\nSUMMARY:", dict(Counter(r["verdict"] for r in rows)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
