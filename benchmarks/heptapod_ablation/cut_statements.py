#!/usr/bin/env python3
"""Find top-level statements that Mathematica cuts at a line end.

In a file read with Get (a FeynRules .fr), an expression that is complete at
the end of a line ends there. So

    LTotal := LSM
      + LNew;

defines LTotal as LSM; the second line is a separate expression with no
effect. Verified in the kernel on 2026-10-06 (x := a \\n + b \\n + c gives a).
Inside brackets the line end does not end the expression.

    cut_statements.py MODEL.fr ...        # prints the cut lines per file as JSON
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import fr_lint  # noqa: E402

_OPEN, _CLOSE = "([{", ")]}"


def cut_lines(raw: str) -> list[dict]:
    """Lines at bracket depth 0 that start with + or - after a line that ended
    a complete expression (no trailing operator, comma or semicolon)."""
    text = fr_lint.strip_comments(raw)
    out, depth, prev, in_str = [], 0, "", False
    for n, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if s and depth == 0 and re.match(r"[+\-]", s) and prev and not re.search(r"[+\-*/.,;=({\[&|^]$", prev):
            out.append({"line": n, "text": s[:100], "after": prev[:80]})
        for ch in line:
            if ch == '"':
                in_str = not in_str
            elif not in_str and ch in _OPEN:
                depth += 1
            elif not in_str and ch in _CLOSE:
                depth = max(0, depth - 1)
        if s:
            prev = s
    return out


if __name__ == "__main__":
    print(json.dumps({f: cut_lines(Path(f).read_text(errors="replace")) for f in sys.argv[1:]}, indent=1))
