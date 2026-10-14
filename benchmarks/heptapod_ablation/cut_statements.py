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
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "cc_harness"))
from opt_checks import cut_lines  # noqa: E402

if __name__ == "__main__":
    print(
        json.dumps(
            {f: cut_lines(Path(f).read_text(errors="replace")) for f in sys.argv[1:]}, indent=1
        )
    )
