#!/usr/bin/env python3
"""Replay of one proposed lint rule on the stored validate snapshots: an SM
fermion written in a Dot chain with some, but not all, of its indices.

FeynRules fills index slots from the left and the first slot of a fermion is
spin, so `l[ff]` is `l[Index[Spin, ff]]`, and `uqbar[ff, cc]` puts `ff` in
the spin slot too. The stored lint has this rule only for a numeric index
(`numeric_spin_slot`). This counts, over every in-loop snapshot of the two
loop arms that compiled, how often the wider rule fires and what the chain
then said: hermiticity fails, or a new particle has no vertex in the UFO.

    index_count_replay.py     # prints JSON
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import retro  # noqa: E402

# Index counts of the SM.fr fermion classes (spin first).
N_INDICES = {"vl": 2, "l": 2, "uq": 3, "dq": 3, "LL": 3, "lR": 2, "QL": 4, "uR": 3, "dR": 3}
_USE = re.compile(r"(?<![A-Za-z0-9$])(" + "|".join(N_INDICES) + r")(bar)?\[([^\[\]]*)\]")


def partial_index_uses(text: str) -> list[dict]:
    text = retro.fr_lint.strip_comments(text)
    out = []
    for ln, line in enumerate(text.splitlines(), 1):
        if "." not in line or ":=" not in line and "==" in line:
            continue
        for m in _USE.finditer(line):
            n = len([a for a in m.group(3).split(",") if a.strip()])
            near = line[max(0, m.start() - 2) : m.end() + 2]
            if 0 < n < N_INDICES[m.group(1)] and "." in near:
                out.append({"line": ln, "use": m.group(0)})
    return out


def main() -> int:
    runs = Path.home() / "Documents/Github/heptapod/eval/benchmark_runs"
    rows = []
    for arm in retro.LOOP_ARMS:
        for paper in retro.PAPERS:
            d = runs / paper / "rerun" / arm / "s1"
            for c in retro.load_calls(d):
                fr = d / "validation" / f"call{c['call']}" / "model.fr"
                if c["state"]["compile"] != "pass" or not fr.is_file():
                    continue
                uses = partial_index_uses(fr.read_text(errors="replace"))
                inert = retro.particles_without_vertex(Path(c["ufo"])) if c["ufo"] else []
                rows.append(
                    {
                        "arm": arm,
                        "paper": paper,
                        "call": c["call"],
                        "flagged": bool(uses),
                        "uses": sorted({u["use"] for u in uses})[:4],
                        "hermiticity_fail": c["state"]["hermiticity"] == "fail",
                        "inert_new_particle": bool(inert),
                        "old_rule": any(f["rule"] == "numeric_spin_slot" for f in c["lint"]),
                    }
                )
    flagged = [r for r in rows if r["flagged"]]
    clean = [r for r in rows if not r["flagged"]]

    def bad(r: dict) -> bool:
        return r["hermiticity_fail"] or r["inert_new_particle"]

    print(
        json.dumps(
            {
                "snapshots_compiled": len(rows),
                "flagged": len(flagged),
                "flagged_with_hermiticity_fail_or_inert_particle": sum(bad(r) for r in flagged),
                "flagged_papers": sorted({f"{r['arm']}:{r['paper']}" for r in flagged}),
                "flagged_and_fine": [
                    f"{r['arm']}:{r['paper']}:call{r['call']}" for r in flagged if not bad(r)
                ],
                "not_flagged": len(clean),
                "not_flagged_with_hermiticity_fail_or_inert_particle": sum(bad(r) for r in clean),
                "flagged_where_the_stored_rule_was_silent": sum(not r["old_rule"] for r in flagged),
                "rows": flagged,
            },
            indent=1,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
