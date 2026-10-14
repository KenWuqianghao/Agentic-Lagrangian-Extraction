#!/usr/bin/env python3
"""Rebuild what validate_model would hand the agent for each replayed model:
the header (call, stage reached), the verdicts, the diagnostic sections
(re-rendered from the stored compile log with the current diagnose.py), and
the lint findings. No Wolfram: everything comes from the replay's files.

    agent_view.py            writes <page>/agent_view.md and prints a digest
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALE = HERE.parent.parent
sys.path.insert(0, str(ALE / "cc_harness"))
import diagnose  # noqa: E402
import heptapod_mcp  # noqa: E402

PAGES = ("B-L-SM", "HeavyN", "Wprime", "EffLRSM", "SMWeinberg", "pSPSS")


def main() -> int:
    for p in PAGES:
        calls = sorted(
            (HERE / p / "validation").glob("call*/summary.json"),
            key=lambda x: int(x.parent.name[4:]),
        )
        if not calls:
            continue
        s = json.loads(calls[-1].read_text())
        row = s["row"]
        fr = HERE / p / "model.fr"
        log = (
            Path(row["compile_log"]).read_text(errors="replace")
            if Path(row.get("compile_log") or "").is_file()
            else ""
        )
        lint = subprocess.run(
            [sys.executable, str(ALE / "pi_harness" / "hepval.py"), "lint", str(fr)],
            capture_output=True,
            text=True,
        ).stdout
        verdicts = "\n".join(
            f"- FeynRules check `{k}`: {v}" for k, v in (row.get("checks") or {}).items()
        )
        view = (
            f"# validate_model call 1/10: stage reached = {s.get('stage_reached')}\n\n"
            f"- compile: {'OK' if row.get('compile_ok') else 'FAILED'}\n{verdicts}\n"
            f"- MadGraph import: {row.get('madgraph_import_ok')}\n\n"
            + diagnose.render_sections(row, log, fr.read_text(errors="replace"))
            + "\n## lint findings\n"
            + heptapod_mcp._lint_text(lint)
            + "\n"
        )
        (HERE / p / "agent_view.md").write_text(view)
        print(
            f"==== {p}: stage {s.get('stage_reached')}, {len(view)} chars, "
            f"diag lines in log: {sum(ln.startswith('HEPTAPOD-') and not ln.startswith(('HEPTAPOD-CHECK', 'HEPTAPOD-GAUGE', 'HEPTAPOD-LAG', 'HEPTAPOD-RESID', 'HEPTAPOD-MASS|')) for ln in log.splitlines())}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
