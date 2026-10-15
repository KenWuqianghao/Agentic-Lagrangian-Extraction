#!/usr/bin/env python3
"""Unit tests for two rules in validation_benchmark that decide what a number means.

Both were wrong before 2026-09-13. Every stored check verdict was a pass,
because the prose classifier could not report a failure. And ``LSM`` was
added to totals that already contained it, so the Standard Model was counted
twice. Needs a heptapod checkout that has tools/feynrules/lagrangian_checks.py;
no Wolfram kernel.

    python eval/benchmark_runs/test_validation_benchmark.py
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent))
sys.path.insert(0, str(HERE))

import validation_benchmark as vb  # noqa: E402

ALL_PASS = {k: "pass" for k in vb.CHECK_KEYS}


def test_all_pass_counts_as_pass():
    assert vb.all_checks_pass(ALL_PASS)


def test_one_fail_is_not_pass():
    assert not vb.all_checks_pass({**ALL_PASS, "hermiticity": "fail"})


def test_inconclusive_is_not_pass():
    assert not vb.all_checks_pass({**ALL_PASS, "mass_spectrum": "inconclusive"})


def test_missing_check_is_not_pass():
    partial = dict(ALL_PASS)
    partial.pop("mass_diagonal")
    assert not vb.all_checks_pass(partial)


def test_no_checks_is_not_pass():
    assert not vb.all_checks_pass({})
    assert not vb.all_checks_pass(None)


def test_old_boolean_verdicts_are_not_pass():
    # The retired format. Its True meant nothing, so it must never count.
    assert not vb.all_checks_pass(
        {"hermiticity": True, "kinetic_terms": True, "mass_spectrum": True})


def _fr(text: str) -> Path:
    fh = tempfile.NamedTemporaryFile("w", suffix=".fr", delete=False)
    fh.write(text)
    fh.close()
    return Path(fh.name)


def test_bsm_only_total_gets_lsm():
    fr = _fr("LkinS1 := DC[S1bar, mu] DC[S1, mu];\n"
             "LYuk := yS1 S1bar.S1;\n"
             "LBSM := LkinS1 + LYuk;\n")
    assert vb.lagrangian_expression(fr, "LBSM") == "LSM + LBSM"


def test_total_containing_lsm_is_not_doubled():
    fr = _fr("LZp := gZp Zp[mu] tbar.Ga[mu].t;\n"
             "LTotal := LSM + LZp;\n")
    assert vb.lagrangian_expression(fr, "LTotal") == "LTotal"


def test_lsm_reached_through_a_subterm_is_not_doubled():
    fr = _fr("LZp := gZp Zp[mu] tbar.Ga[mu].t;\n"
             "LGauge := LSM + LZp;\n"
             "LTotal := LGauge + LZp;\n")
    assert vb.lagrangian_expression(fr, "LTotal") == "LTotal"


def test_lsm_substring_does_not_count():
    # LSMlike is a different symbol; only the token LSM means the SM.
    fr = _fr("LSMlike := yS1 S1bar.S1;\n"
             "LBSM := LSMlike;\n")
    assert vb.lagrangian_expression(fr, "LBSM") == "LSM + LBSM"


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"[✓] {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"[✗] {t.__name__} {e}")
    print(f"{len(tests) - failed}/{len(tests)} passed")
    raise SystemExit(1 if failed else 0)
