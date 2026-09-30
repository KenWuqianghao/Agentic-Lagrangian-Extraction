#!/usr/bin/env python3
"""Numbers for CC_HARNESS_<date>.md: summarize.py's funnel and paired exact
McNemar tests for the arms, plus the cc arm's per-paper facts (tokens,
minutes, validate/review calls, Stop-gate blocks, referee verdict).

    collect.py --variants v3s_notools,pi_qwen_harness,cc_sonnet_harness > cc_summary.json
"""

from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PI = HERE.parent / "pi_harness"
sys.path.insert(0, str(PI))
from run_pi import RUNS, SINGLE_MODEL  # noqa: E402


def cc_facts(variant: str, page: str) -> dict:
    d = RUNS / page / "rerun" / variant / "s1"
    if not (d / "run.json").is_file():
        return {"page": page, "run": False}
    a = json.loads((d / "run.json").read_text())["agent"]
    v = json.loads((d / "validation_hepval.json").read_text()) if (d / "validation_hepval.json").is_file() else {}
    u = a.get("usage") or {}
    reviews = a.get("reviews") or []
    last_review = reviews[-1] if reviews else None
    return {
        "page": page, "run": True, "delivered": bool((a.get("ok") is not None) and (d / "model" / f"{page}_gen.fr").is_file()),
        "status": v.get("status"), "checks": v.get("checks"), "mg5": v.get("madgraph_import_ok"),
        "full_chain": bool(v.get("full_chain_pass")),
        "inloop_last_stage": (a.get("last_inloop") or {}).get("stage"),
        "validate_calls": a.get("n_validate"), "review_calls": a.get("n_review"),
        "gate_blocks": (a.get("stop_gate") or {}).get("blocks"),
        "referee_verdict": last_review.get("verdict") if last_review else None,
        "referee_on_final_model": last_review.get("reviewed_final_model") if last_review else None,
        "minutes": round((a.get("seconds") or 0) / 60, 1),
        "input_tokens_total": u.get("input_total"), "input_tokens_uncached": (u.get("input_tokens") or 0)
        + (u.get("cache_creation_input_tokens") or 0), "output_tokens": u.get("output_tokens"),
        "referee_input_tokens": sum(int((r.get("usage") or {}).get(k) or 0) for r in reviews
                                    for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")),
        "cost_usd": round(float(a.get("cost_usd") or 0) + sum(float(r.get("cost_usd") or 0) for r in reviews), 2),
        "n_blocked_tool_calls": a.get("n_blocked"), "audit_ok": a.get("audit_ok"),
        "timed_out": a.get("timed_out"), "exit": a.get("exit"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variants", required=True)
    ap.add_argument("--cc-variant", default="cc_sonnet_harness")
    args = ap.parse_args()
    s = subprocess.run([sys.executable, str(PI / "summarize.py"), "--variants", args.variants],
                       capture_output=True, text=True, cwd=str(PI))
    if s.returncode != 0:
        print(s.stderr, file=sys.stderr)
        return 1
    summ = json.loads(s.stdout)
    pages = SINGLE_MODEL.split(",")
    rows = [cc_facts(args.cc_variant, p) for p in pages]
    ran = [r for r in rows if r["run"]]
    med = {k: statistics.median([r[k] for r in ran if r.get(k) is not None]) for k in
           ("minutes", "input_tokens_total", "input_tokens_uncached", "output_tokens", "cost_usd")} if ran else {}
    print(json.dumps({"funnel": summ["funnel"], "tests": summ["tests"], "inloop_vs_score": summ["inloop_vs_score"],
                      "cc_rows": rows, "cc_median": med,
                      "cc_total_cost_usd": round(sum(r.get("cost_usd") or 0 for r in ran), 2),
                      "table": summ["table"]}, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
