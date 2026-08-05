#!/usr/bin/env python3
"""
Check how much of each model's Lagrangian actually reached the UFO.

The validation harness picks the model's total-Lagrangian symbol
positionally: `total_lag_symbol()` in validation_benchmark.py takes the LAST
line matching `^L<name> :?=`. That symbol is what UFO_generator.wl compiles,
as `LSM + <symbol>`.

That rule is only correct when a model's last L-assignment is its total. When
a model defines its total Lagrangian and then defines anything else starting
with `L`, or keeps several alternative operator bases, the harness picks the
wrong symbol and FeynRules compiles a fragment. The fragment can be perfectly
Hermitian, pass every check and import into MadGraph — so the model counts as
passing while most of its physics never reached the UFO.

This script recomputes, per model, which defined Lagrangian terms are
reachable from the symbol the harness actually used, and writes
LAGRANGIAN_COVERAGE.md.

Usage:
    python benchmarks/audit_lagrangian_coverage.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, "/Users/kenwu/Documents/Github/heptapod")

from tools.frgen.fr_parser import parse_lagrangian_terms  # noqa: E402

IDENT = re.compile(r"\b([A-Za-z][A-Za-z0-9$]*)\b")
SKIP = {"ian_review_bundle", "review_bundle", "__pycache__"}
FAILED = {"ALRM_general", "HNLs", "SLQrules"}


def total_lag_symbol(text: str) -> str | None:
    """Exactly the harness rule: the last top-level `L... =` in the file."""
    sym = None
    for line in text.splitlines():
        m = re.match(r"^(L[A-Za-z0-9]*)\s*:?=", line)
        if m:
            sym = m.group(1)
    return sym


def final_fr(model: str) -> tuple[Path | None, str]:
    for p in ("repair3", "repair2", "repair"):
        f = HERE / model / p / "final.fr"
        if f.is_file():
            return f, p
    g = HERE / model / "model" / f"{model}_gen.fr"
    return (g, "one-shot") if g.is_file() else (None, "")


def audit() -> list[dict]:
    rows = []
    for d in sorted(x for x in HERE.iterdir() if x.is_dir() and x.name not in SKIP):
        model = d.name
        fr, src = final_fr(model)
        if not fr:
            continue
        text = fr.read_text(encoding="utf-8", errors="replace")
        root = total_lag_symbol(text)
        body = {t["name"]: t["expression"] for t in parse_lagrangian_terms(text)}
        if not root or root not in body:
            continue
        seen, stack = set(), [root]
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            for tok in IDENT.findall(body.get(cur, "")):
                if tok in body:
                    stack.append(tok)
        orphan = sorted(n for n in body if n not in seen and n.startswith("L"))
        rows.append({
            "model": model, "source": src, "root": root,
            "defined": len([n for n in body if n.startswith("L")]),
            "reached": len([n for n in seen if n.startswith("L")]),
            "orphaned": orphan,
            "passed_chain": model not in FAILED,
        })
    return rows


def render(rows: list[dict]) -> str:
    hit = [r for r in rows if r["orphaned"]]
    hit.sort(key=lambda r: r["reached"] / max(r["defined"], 1))
    passing_hit = [r for r in hit if r["passed_chain"]]

    L = [
        "# How much of each Lagrangian actually reached the UFO",
        "",
        "**Read this before trusting the pass rate.**",
        "",
        "The validation harness chooses each model's total-Lagrangian symbol "
        "positionally: it takes the **last** line matching `^L<name> =` in "
        "the `.fr`, and compiles `LSM + <that symbol>`.",
        "",
        "That is correct only when a model's last `L` assignment really is "
        "its total. Where a model defines its total and then defines anything "
        "else beginning with `L`, or carries several alternative operator "
        "bases, the harness compiles a **fragment** of the model. A fragment "
        "can be perfectly Hermitian, pass every FeynRules check and import "
        "into MadGraph — so it counts as passing while most of the physics "
        "never reached the UFO.",
        "",
        f"**{len(hit)} of {len(rows)} models are affected, "
        f"{len(passing_hit)} of them among those counted as passing.**",
        "",
        "This does not mean those models are wrong. It means the benchmark "
        "did not test as much of them as the pass rate implies, and the gap "
        "should be closed before the number is quoted anywhere.",
        "",
        "## Affected models",
        "",
        "| model | source | symbol compiled | L-terms reached | omitted |",
        "|---|---|---|---:|---|",
    ]
    for r in hit:
        mark = "" if r["passed_chain"] else " *(failed anyway)*"
        L.append(
            f"| `{r['model']}`{mark} | {r['source']} | `{r['root']}` | "
            f"{r['reached']}/{r['defined']} | "
            + ", ".join(f"`{o}`" for o in r["orphaned"]) + " |"
        )

    L += [
        "",
        "## Worth checking first",
        "",
        "- `VLQ` compiled `L4Mass` alone — 1 of 11 terms. Every vector-like "
        "quark interaction (`LWTP`, `LZTP`, `LHTP`, `LyTP`, ...) was left "
        "out, yet the model passed the full chain.",
        "- `topBSM` compiled `LO1`, reaching 5 of 26 terms. Its cross-check "
        "independently flagged 20 substantive disagreements, including that "
        "the paper's master EFT Lagrangian was not reproduced — consistent "
        "with this.",
        "- `331` compiled `LTot := LGaugeSelf331`, so the Higgs potential, "
        "gauge masses and scalar-fermion couplings are all absent.",
        "",
        "## The fix",
        "",
        "Do not infer the total Lagrangian from file position. Either require "
        "the generator to emit a known symbol name, or resolve the root by "
        "reference analysis — the term no other term refers to — and fail "
        "loudly when that is ambiguous. `UFO_generator.wl` already accepts a "
        "`LagName` parameter and already fails when the symbol is undefined; "
        "the weakness is purely in how the harness chooses what to pass it.",
        "",
        "## Reproducing",
        "",
        "```bash",
        "python benchmarks/audit_lagrangian_coverage.py",
        "```",
        "",
    ]
    return "\n".join(L)


def main() -> int:
    rows = audit()
    (HERE / "lagrangian_coverage.json").write_text(
        json.dumps(rows, indent=1), encoding="utf-8")
    (HERE / "LAGRANGIAN_COVERAGE.md").write_text(render(rows), encoding="utf-8")
    hit = [r for r in rows if r["orphaned"]]
    passing = [r for r in hit if r["passed_chain"]]
    print(f"[coverage] {len(rows)} models audited")
    print(f"[coverage] {len(hit)} omit defined L-terms "
          f"({len(passing)} of them counted as passing)")
    for r in sorted(hit, key=lambda r: r["reached"] / max(r["defined"], 1))[:5]:
        print(f"[coverage]   {r['model']:16} {r['reached']}/{r['defined']} "
              f"via {r['root']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
