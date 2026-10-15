#!/usr/bin/env python3
"""Aggregate the open-model runs (open_bench.py) next to the Sonnet arms of
ABLATION_2026-09-17 on the same 16 papers.

Reads validation.json, audit.json, run.json and the .fr on disk; never asks a
model whether it succeeded. Writes open_bench/report.json and report.md.

    python3 benchmarks/open_bench/report.py
"""

from __future__ import annotations

import importlib.util
import json
import sys
import types
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
BENCH = HERE.parent
HEPTAPOD = Path.home() / "Documents/Github/heptapod"
sys.path.insert(0, str(BENCH))
sys.path.insert(0, str(HEPTAPOD))
sys.path.insert(0, str(HERE))

import rerun_predicates  # noqa: E402
from open_bench import PAGES16  # noqa: E402

# tools/frgen/__init__ imports orchestral; load only the parser the scorer needs.
for _name in ("tools", "tools.frgen"):
    sys.modules.setdefault(_name, types.ModuleType(_name))
_spec = importlib.util.spec_from_file_location(
    "tools.frgen.fr_parser", HEPTAPOD / "tools/frgen/fr_parser.py"
)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["tools.frgen.fr_parser"] = _mod
_spec.loader.exec_module(_mod)
from eval.reference_bench import score  # noqa: E402

SM_FR = str(HEPTAPOD / "tools/feynrules/test_files/models/SM.fr")
CHECKS = ("hermiticity", "kinetic_diagonal", "mass_diagonal", "mass_spectrum")
OPEN_MODELS = {"nemotron": "Nemotron 3 Ultra", "mimo": "MiMo v2.6 Flash"}
ARMS = [
    (f"v3o_{k}_{a}", name, a)
    for k, name in OPEN_MODELS.items()
    for a in ("hand", "toolkit", "toolkit2")
    if any((BENCH / p / "rerun" / f"v3o_{k}_{a}").is_dir() for p in PAGES16)
]
ARMS += [
    ("v3s_notools", "Sonnet (Sep 17)", "hand"),
    ("v3s_tools", "Sonnet (Sep 17)", "schema one-shot"),
]


def fisher_two_sided(a: int, n1: int, b: int, n2: int) -> float:
    """Fisher exact test, two-sided, for a/n1 vs b/n2."""
    k, n = a + b, n1 + n2
    if n1 == 0 or n2 == 0:
        return float("nan")

    def p(x):
        return comb(n1, x) * comb(n2, k - x) / comb(n, k)

    obs = p(a)
    lo, hi = max(0, k - n2), min(k, n1)
    return min(1.0, sum(p(x) for x in range(lo, hi + 1) if p(x) <= obs * (1 + 1e-9)))


def _cands() -> dict:
    d = json.loads((BENCH / "db_candidates.json").read_text())
    return {c["page"]: c for c in d["candidates"]}


def collect(page: str, var: str, cands: dict) -> dict:
    d = BENCH / page / "rerun" / var / "s1"
    row = {"page": page, "variant": var, "ran": (d / "run.json").is_file()}
    if not row["ran"]:
        return row
    run = json.loads((d / "run.json").read_text())
    au = json.loads((d / "audit.json").read_text()) if (d / "audit.json").is_file() else {}
    v = json.loads((d / "validation.json").read_text()) if (d / "validation.json").is_file() else {}
    fr = d / "model" / f"{page}_gen.fr"
    checks = v.get("checks") or {}
    # A run that ends on provider errors (503 overloaded, 504 idle timeout) without a
    # deliverable measures the free tier, not the model: infra failure, retried, and
    # left out of the denominator if it still fails.
    n_srv = 0
    if (d / "agent_stream.jsonl").is_file():
        for line in (d / "agent_stream.jsonl").read_text(errors="replace").splitlines():
            if '"type":"error"' in line and (
                "[503]" in line or "[504]" in line or "server_error" in line
            ):
                n_srv += 1
    row["provider_errors"] = n_srv
    # A run with no events at all never reached the model (opencode retried a
    # "Rate limit exceeded" free tier for the whole hour): infra as well.
    # A run that hit the free tier's rate limit (429) was cut short by the quota,
    # file or no file: infra too. The driver stops it at the first 429.
    row["infra_fail"] = ((bool(n_srv) or run.get("n_events") == 0) and not fr.is_file()) or bool(
        run.get("rate_limited")
    )
    row.update(
        {
            "audit_ok": au.get("audit_ok", (run.get("agent") or {}).get("audit_ok")),
            "contaminated": au.get("contaminated", (run.get("agent") or {}).get("contaminated")),
            "tampered": bool(au.get("tampered")),
            "timed_out": run.get("timed_out"),
            "seconds": run.get("seconds"),
            "tokens": run.get("tokens"),
            "frgen_runs": au.get("frgen_runs"),
            "tool_calls": au.get("tool_calls"),
            "read_paper": au.get("read_paper"),
            "rendered": fr.is_file(),
            "render_reason": run.get("reason"),
            "validated": bool(v),
            "status": v.get("status"),
            "compile_ok": bool(v.get("compile_ok")),
            "checks": checks,
            "checks_all": bool(checks) and all(checks.get(c) == "pass" for c in CHECKS),
            "mg5_ok": bool(v.get("madgraph_import_ok")),
            "full_chain": bool(v.get("full_chain_pass")),
        }
    )
    if fr.is_file():
        text = fr.read_text(errors="replace")
        preds = {}
        for name, fn in rerun_predicates.PREDICATES.get(page, []):
            try:
                ok, _ = fn(text)
            except Exception:  # noqa: BLE001
                ok = False
            preds[name] = bool(ok)
        row["predicates_all"] = all(preds.values()) if preds else None
        cand = cands.get(page)
        if cand and cand.get("reference_fr"):
            try:
                s = score(str(fr), str(HEPTAPOD / cand["reference_fr"]), sm_fr=SM_FR)
                if cand.get("n_new_fields"):
                    row["field_f1"] = s["field_signature"]["f1"]
            except Exception as e:  # noqa: BLE001
                row["score_error"] = f"{type(e).__name__}: {str(e)[:100]}"
    return row


def aggregate(rows: list[dict]) -> dict:
    ran = [r for r in rows if r["ran"]]
    # Valid = no sandbox escape and no tampering. A denied or instructed-away tool call
    # (a policy slip) is reported, not disqualifying, as in ABLATION_2026-09-17.
    ok = [
        r
        for r in ran
        if not r.get("contaminated") and not r.get("tampered") and not r.get("infra_fail")
    ]
    f1 = [r["field_f1"] for r in ok if r.get("field_f1") is not None]
    agg = {
        "runs": len(ran),
        "audited_ok": len(ok),
        "infra_fail": sum(bool(r.get("infra_fail")) for r in ran),
        "policy_slips": sum(r.get("audit_ok") is False for r in ok),
        "rendered": sum(r["rendered"] for r in ok),
        "compiled": sum(r.get("compile_ok", False) for r in ok),
        "mg5": sum(r.get("mg5_ok", False) for r in ok),
        "checks_all": sum(r.get("checks_all", False) for r in ok),
        "full_chain": sum(r.get("full_chain", False) for r in ok),
        "mean_field_f1": round(sum(f1) / len(f1), 3) if f1 else None,
    }
    for c in CHECKS:
        agg[f"{c}_pass"] = sum((r.get("checks") or {}).get(c) == "pass" for r in ok)
    return agg


def main() -> int:
    cands = _cands()
    table, per_page = {}, {}
    for var, model, arm in ARMS:
        rows = [collect(p, var, cands) for p in PAGES16]
        per_page[var] = rows
        table[var] = {"model": model, "arm": arm, **aggregate(rows)}
    tests = {}
    for m in OPEN_MODELS:
        for arm in ("toolkit", "toolkit2"):
            if f"v3o_{m}_hand" not in table or f"v3o_{m}_{arm}" not in table:
                continue
            h, t = table[f"v3o_{m}_hand"], table[f"v3o_{m}_{arm}"]
            for k in ("rendered", "compiled", "mg5", "full_chain"):
                tests[f"{m}:{arm}:{k}"] = round(
                    fisher_two_sided(t[k], t["audited_ok"], h[k], h["audited_ok"]), 3
                )
    out = {"table": table, "fisher_toolkit_vs_hand": tests, "per_page": per_page}
    (HERE / "report.json").write_text(json.dumps(out, indent=1, default=str))

    L = [
        "| model | arm | runs (valid) | .fr produced | compiled | MG5 import | 4 checks pass | "
        "full chain | Herm | Kin | Mass diag | Mass spec | field F1 |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for var, _m, _a in ARMS:
        t = table[var]
        L.append(
            f"| {t['model']} | {t['arm']} | {t['runs']} ({t['audited_ok']}) | {t['rendered']} | "
            f"{t['compiled']} | {t['mg5']} | {t['checks_all']} | **{t['full_chain']}** | "
            f"{t['hermiticity_pass']} | {t['kinetic_diagonal_pass']} | {t['mass_diagonal_pass']} | "
            f"{t['mass_spectrum_pass']} | {t['mean_field_f1']} |"
        )
    L += [
        "",
        "Fisher exact p, toolkit arm vs hand: " + ", ".join(f"{k} {v}" for k, v in tests.items()),
        "",
    ]
    L += ["| page | " + " | ".join(v for v, _m, _a in ARMS) + " |", "|---|" + "---|" * len(ARMS)]

    def cell(r):
        if not r["ran"]:
            return "-"
        if r.get("contaminated") or r.get("tampered"):
            return "contaminated"
        if r.get("infra_fail"):
            return "provider error"
        if not r["rendered"]:
            return f"no .fr ({r.get('render_reason') or '?'})"
        if not r.get("validated"):
            return "not validated"
        if r["full_chain"]:
            return "**PASS**"
        if not r["compile_ok"]:
            return r.get("status") or "compile fail"
        fails = [c for c in CHECKS if (r.get("checks") or {}).get(c) != "pass"]
        return ("MG5 fail; " if not r["mg5_ok"] else "") + (
            "fail " + ",".join(fails) if fails else ""
        )

    for i, p in enumerate(PAGES16):
        L.append(f"| {p} | " + " | ".join(cell(per_page[v][i]) for v, _m, _a in ARMS) + " |")
    (HERE / "report.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[: len(ARMS) + 4]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
