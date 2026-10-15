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
stages (a heredoc body stays with the stage before it). Only the command word
of a stage counts. A stage reads a reference when its command shows or copies
file contents (READ: cat, sed, rg, diff, cp, inline python) and a file operand
names a reference path. Everything else that names a reference is "listed".

- ls, find, wc and stat only list or measure. In `find reference_cache -name
  cat` the word cat is a value.
- find -exec runs its own command; {} gives it the search paths.
- The pattern of grep, rg, sed or awk is not a path: in `ls reference_cache |
  grep reference_cache` only ls names the cache.
- cp reads its sources, not its destination. It counts because later reads
  of the copy name no reference path.
- A path to the cache itself (eval/reference_cache, reference_cache/*) names
  every model's reference, including the run's own.
- A script file (python3 x.py) can open paths that its command line does not
  name, and the audit cannot see into it. Its reference paths are listed, and
  the run counts in script_runs.

Writes contamination_audit.json next to this file.

    python eval/benchmark_runs/contamination_audit.py
"""

from __future__ import annotations

import json
import re
import shlex
from collections import Counter
from itertools import takewhile
from pathlib import Path

HERE = Path(__file__).resolve().parent
READ = re.compile(
    r"cat|sed|head|tail|less|more|awk|e?grep|fgrep|rg|python[\d.]*|bat|nl|diff|cmp|cp"
)
REF = re.compile(r"reference_cache(?:/([^/\s'\"]+))?")
SCRIPT = re.compile(r"\b(?:python3?|sh|bash|zsh)\s+(?!-)\S+\.(?:py|sh)\b")
SEPARATORS = {"|", "||", "&&", ";", "&"}
# The first operand of these commands is a pattern or a program, not a file,
# unless -e or -f gives it. The options listed take a value as the next word.
PATTERN_FIRST: dict[str, set[str]] = {
    "grep": {"-A", "-B", "-C", "-m", "-d", "-D", "--context"},
    "egrep": {"-A", "-B", "-C", "-m"},
    "fgrep": {"-A", "-B", "-C", "-m"},
    "rg": {"-A", "-B", "-C", "-m", "-g", "-t", "-T", "-M", "-j", "-E", "--glob",
           "--iglob", "--type", "--type-not", "--max-count", "--context"},
    "sed": {"-l"},
    "awk": {"-F", "-v"},
}
PATTERN_OPTS = ("-e", "-f", "--regexp", "--file")
SHELLS = {"sh", "bash", "zsh", "dash"}
# Commands that run the command after them, with the options that take a value.
WRAPPERS: dict[str, set[str]] = {
    "sudo": {"-u", "-g", "-C", "-D", "-h", "-p", "-U", "-r", "-t"},
    "env": {"-u", "-C"},
    "nice": {"-n"},
    "nohup": set(),
    "time": {"-f", "-o"},
    "command": set(),
    "xargs": {"-n", "-I", "-L", "-P", "-d", "-s", "-E", "-a"},
    "timeout": {"-s", "-k", "--signal", "--kill-after"},  # then the duration
}
EXEC = {"-exec", "-execdir", "-ok", "-okdir"}


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
        if len(words) == 3 and Path(words[0]).name in SHELLS and words[1] in ("-c", "-lc"):
            cmd = words[2]
        head, here, body = cmd.partition("<<")  # a heredoc body is code, not shell
        # The lexer drops quotes, so hide find's quoted ; from the separators.
        head = re.sub(r"\\;|';'|\";\"", "\0", head)
        lex = shlex.shlex(head, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        tokens = list(lex)
    except ValueError:
        return [cmd]
    out: list[list[str]] = [[]]
    for t in tokens:
        if t in SEPARATORS:
            out.append([])
        else:
            out[-1].append(";" if t == "\0" else t)
    out = [st for st in out if st]
    if here and out:  # the body stays with the command that reads it
        return [shlex.join(st) for st in out[:-1]] + [shlex.join(out[-1]) + " " + here + body]
    return [shlex.join(st) for st in out]


def command(words: list[str]) -> int:
    """Index of the command word: after VAR=value words and the WRAPPERS with their options."""
    i = 0
    while i < len(words):
        name = Path(words[i]).name
        if re.fullmatch(r"\w+=.*", words[i]):
            i += 1
        elif name in WRAPPERS:
            i += 1
            while i < len(words) and words[i].startswith("-"):
                i += 2 if words[i] in WRAPPERS[name] else 1
            i += name == "timeout"
        else:
            return i
    return i


def roles(stage: str) -> tuple[str, str]:
    """(the words of `stage` whose files it reads, the words it names and does not read).

    A pattern of grep, rg, sed or awk is in neither. The destination of cp is named.
    """
    head = stage.partition("<<")[0]
    try:
        words = shlex.split(head)
    except ValueError:
        return "", stage
    i = command(words)
    if i >= len(words):
        return "", stage
    name = Path(words[i]).name
    if name == "find":  # each -exec command reads what it names; {} names the search paths
        roots = list(takewhile(lambda w: not w.startswith(("-", "(", "!")), words[i + 1:]))
        src, j = [], i + 1
        while j < len(words):
            if words[j] in EXEC:
                end = next((k for k in range(j + 1, len(words)) if words[k] in (";", "+")),
                           len(words))
                run = [r for w in words[j + 1:end] for r in (roots if w == "{}" else [w])]
                src.append(roles(shlex.join(run))[0])
                j = end
            j += 1
        return " ".join(src), stage
    if not READ.fullmatch(name) or SCRIPT.match(" ".join(words[i:])):
        return "", stage  # a script file's reads are unseen
    if head != stage:
        return stage, ""
    args = words[i + 1:]
    if name in PATTERN_FIRST:
        return " ".join(drop_patterns(args, PATTERN_FIRST[name])), ""
    if name == "cp":
        t = next((j for j, w in enumerate(args) if w in ("-t", "--target-directory")), None)
        if t is not None:
            return " ".join(args[:t] + args[t + 2:]), " ".join(args[t:t + 2])
        dest = max((j for j, w in enumerate(args) if not w.startswith("-")), default=None)
        if dest is not None:
            return " ".join(args[:dest] + args[dest + 1:]), args[dest]
    return " ".join(args), ""


def drop_patterns(args: list[str], takes_value: set[str]) -> list[str]:
    """`args` without the patterns: the first operand, or each value of -e and --regexp."""
    given = any(w in PATTERN_OPTS or w.startswith(("--regexp=", "--file=")) for w in args)
    out, i = [], 0
    while i < len(args):
        w = args[i]
        if w in ("-e", "--regexp") or w.startswith("--regexp="):
            i += 1 if "=" in w else 2
        elif w in takes_value:
            out += args[i:i + 2]
            i += 2
        elif w.startswith("-") or given:
            out.append(w)
            i += 1
        else:  # the first operand is the pattern
            given = True
            i += 1
    return out


def refs(stage: str) -> set[str]:
    """Pages whose reference the stage names; "*" for the whole cache."""
    return {m.group(1) if m.group(1) and not re.search(r"[*?\[]", m.group(1)) else "*"
            for m in REF.finditer(stage)}


def reads(cmd: str) -> tuple[set[str], set[str]]:
    """(pages read, pages only listed) by `cmd`."""
    read, listed = set(), set()
    for st in stages(cmd):
        src, named = roles(st)
        read |= refs(src)
        listed |= refs(named)
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
