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
for shell commands that read a reference file, and classifies the run:

    OWN REFERENCE READ    the agent read its own model's reference -> the
                          extraction score measures copying, not extraction
    other reference read  read some other model's reference (idiom leakage)
    listed only           reference paths appeared in a listing, never read
    clean                 no reference path in any command

What counts as a read: each command is split into its pipeline and list
stages (a heredoc stays one stage). A stage reads a reference when it names a
reference path and runs a command that shows or copies file contents (READ):
cat, sed, rg, diff, cp, an inline python script, find -exec cat. cp counts
because later reads of the copy name no reference path. A stage that only
lists or measures (ls, find, wc, stat) is "listed". A path to the cache itself
(eval/reference_cache, reference_cache/*) names every model's reference,
including the run's own. A script file the agent runs (python3 x.py) can open
paths that its command line does not name; the audit cannot see into it. A
reference path on its command line is "listed", and the run counts in
script_runs. The pattern of grep, rg, sed or awk is not a path: in
`ls reference_cache | grep reference_cache` only ls names the cache.

Writes contamination_audit.json next to this file.

    python eval/benchmark_runs/contamination_audit.py
"""

from __future__ import annotations

import json
import re
import shlex
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
READ = re.compile(r"\b(cat|sed|head|tail|less|more|awk|grep|rg|python3?|bat|nl|diff|cmp|cp)\b")
REF = re.compile(r"reference_cache(?:/([^/\s'\"]+))?")
SCRIPT = re.compile(r"\b(?:python3?|sh|bash|zsh)\s+(?!-)\S+\.(?:py|sh)\b")
SEPARATORS = {"|", "||", "&&", ";", "&"}
# The first operand of these commands is a pattern or a program, not a file,
# unless -e or -f gives it. The options listed take a value as the next word.
PATTERN_FIRST: dict[str, set[str]] = {
    "grep": {"-A", "-B", "-C", "-m", "-d", "-D", "--context"},
    "egrep": {"-A", "-B", "-C", "-m"},
    "fgrep": {"-A", "-B", "-C", "-m"},
    "rg": {"-A", "-B", "-C", "-m", "-g", "-t", "-T", "-M", "-j", "-E", "--glob", "--iglob",
           "--type", "--type-not", "--max-count", "--context"},
    "sed": {"-l"},
    "awk": {"-F", "-v"},
}
PATTERN_OPTS = ("-e", "-f", "--regexp", "--file")


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


def stages(cmd: str) -> list[str]:
    """The pipeline and list stages of `cmd`, after unwrapping `sh -lc "..."`."""
    try:
        words = shlex.split(cmd)
        if len(words) == 3 and words[1] in ("-c", "-lc"):
            cmd = words[2]
        if "<<" in cmd:  # a heredoc body is code, not shell: keep it whole
            return [cmd]
        lex = shlex.shlex(cmd, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        tokens = list(lex)
    except ValueError:
        return [cmd]
    out: list[list[str]] = [[]]
    for t in tokens:
        if t in SEPARATORS:
            out.append([])
        else:
            out[-1].append(t)
    return [" ".join(st) for st in out if st]


def operands(stage: str) -> str:
    """`stage` without the patterns of grep, rg, sed or awk."""
    try:
        words = shlex.split(stage)
    except ValueError:
        return stage
    takes_value = PATTERN_FIRST.get(Path(words[0]).name) if words else None
    if takes_value is None:
        return stage
    given = any(w in PATTERN_OPTS or w.startswith(("--regexp=", "--file=")) for w in words)
    out, i = [words[0]], 1
    while i < len(words):
        w = words[i]
        if w in ("-e", "--regexp") or w.startswith("--regexp="):
            i += 1 if "=" in w else 2
        elif w in takes_value:
            out += words[i:i + 2]
            i += 2
        elif w.startswith("-") or given:
            out.append(w)
            i += 1
        else:  # the first operand is the pattern
            given = True
            i += 1
    return " ".join(out)


def refs(stage: str) -> set[str]:
    """Pages whose reference the stage names; "*" for the whole cache."""
    return {m.group(1) if m.group(1) and not re.search(r"[*?\[]", m.group(1)) else "*"
            for m in REF.finditer(stage)}


def reads(cmd: str) -> tuple[set[str], set[str]]:
    """(pages read, pages only listed) by `cmd`."""
    read, listed = set(), set()
    for st in stages(cmd):
        shows = READ.search(st) and not SCRIPT.match(st)  # a script file's reads are unseen
        (read if shows else listed).update(refs(operands(st)))
    return read, listed - read


def audit() -> list[dict]:
    """One row per benchmark page: the verdict and the command counts."""
    cands = json.loads((HERE / "db_candidates.json").read_text())["candidates"]
    rows = []
    for c in sorted(cands, key=lambda c: c["page"]):
        page = c["page"]
        ev = HERE / page / "codex_events.jsonl"
        if not ev.is_file():
            rows.append({"page": page, "verdict": "no log"})
            continue
        cmds = commands(ev)
        seen = [(x, *reads(x)) for x in cmds]
        own_read = [x for x, r, _ in seen if page in r or "*" in r]
        other_read = [x for x, r, _ in seen if r - {page} and x not in own_read]
        listed = [x for x, r, ls in seen if ls and not r]
        verdict = ("OWN REFERENCE READ" if own_read else "other reference read" if other_read
                   else "listed only" if listed else "clean")
        rows.append({"page": page, "verdict": verdict, "own_read": len(own_read),
                     "other_read": len(other_read), "listed": len(listed),
                     "script_runs": sum(1 for x in cmds if SCRIPT.search(x)),
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
