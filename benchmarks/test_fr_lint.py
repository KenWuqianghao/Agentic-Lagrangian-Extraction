"""Tests for the fr_lint rules that predict a MadGraph import failure from the
.fr text alone (the three pi Qwen runs that failed only at `import model`)."""

from pathlib import Path

import pytest

import fr_lint

RUNS = Path.home() / "Documents/Github/heptapod/eval/benchmark_runs"


def _rules(text: str) -> dict:
    out: dict = {}
    for f in fr_lint.lint_text(text):
        out.setdefault(f.rule, []).append(f)
    return out


PARAMS = """M$Parameters = {
  %s
};
"""
CLASSES = """M$ClassesDescription = {
  %s
};
"""


def test_quantum_number_with_underscore_is_an_mg5_finding():
    bad = CLASSES % "S[100] == { ClassName -> chi, SelfConjugate -> False, QuantumNumbers -> {B_L -> 2}, Mass -> {Mchi, 100.} }"
    good = CLASSES % "S[100] == { ClassName -> chi, SelfConjugate -> False, QuantumNumbers -> {BL -> 2}, Mass -> {Mchi, 100.} }"
    hits = _rules(bad).get("pattern_symbol_name", [])
    assert [f.stage for f in hits] == ["mg5"]
    assert "B_L" in hits[0].message
    assert "pattern_symbol_name" not in _rules(good)


def test_underscore_in_a_parameter_name_is_only_a_warning():
    # aSRh_u-style names passed the whole chain (Monotops, pi Qwen harness).
    text = PARAMS % "aSRh_u == { ParameterType -> External, Value -> 0.1, InteractionOrder -> {NP, 1} }"
    assert [f.stage for f in _rules(text)["pattern_symbol_name"]] == ["warn"]


def test_orderblock_on_a_tensor_parameter():
    bad = PARAMS % """WpLeR == { ParameterType -> External, BlockName -> WPRIME, OrderBlock -> 7,
    Indices -> {Index[Generation]}, Value -> {WpLeR[1] -> 1., WpLeR[2] -> 1., WpLeR[3] -> 1.} }"""
    good_tensor = PARAMS % """WpLeR == { ParameterType -> External, BlockName -> WPRIME,
    Indices -> {Index[Generation]}, Value -> {WpLeR[1] -> 1., WpLeR[2] -> 1., WpLeR[3] -> 1.} }"""
    good_scalar = PARAMS % "gWp == { ParameterType -> External, BlockName -> WPRIME, OrderBlock -> 1, Value -> 0.6 }"
    hits = _rules(bad)["tensor_orderblock"]
    assert len(hits) == 1 and hits[0].stage == "mg5" and hits[0].line is not None
    assert "tensor_orderblock" not in _rules(good_tensor)
    assert "tensor_orderblock" not in _rules(good_scalar)


def test_same_explicit_spin_index_across_a_dirac_matrix():
    bad = "LNZ := Block[{mu, sp, ff}, -(gw/(2 cw)) Z[mu] VlN[ff] NLbar[sp].Ga[mu].vl[sp, ff]];\n"
    implicit = "LNZ := Block[{mu, ff}, -(gw/(2 cw)) Z[mu] VlN[ff] NLbar.Ga[mu].vl[ff]];\n"
    threaded = "LY := Block[{sp1, sp2, ff1, ff2}, y[ff1, ff2] lbar[sp1, ff1].ProjM[sp1, sp2].uq[sp2, ff2, cc] S];\n"
    no_matrix = "LY := Block[{sp, ii, ff}, y QLbar[sp, ii, ff, cc].uR[sp, ff, cc] Phibar[ii]];\n"
    hits = _rules(bad)["explicit_spin_in_chain"]
    assert len(hits) == 1 and hits[0].stage == "mg5" and hits[0].line == 1
    for ok in (implicit, threaded, no_matrix):
        assert "explicit_spin_in_chain" not in _rules(ok), ok


@pytest.mark.parametrize("page,rule", [("B-L-SM", "pattern_symbol_name"),
                                       ("Wprime", "tensor_orderblock"),
                                       ("HeavyN", "explicit_spin_in_chain")])
def test_rule_names_the_stored_mg5_failure(page, rule):
    fr = RUNS / page / "rerun" / "pi_qwen_harness" / "s1" / "model" / f"{page}_gen.fr"
    if not fr.is_file():
        pytest.skip(f"stored run not present: {fr}")
    assert any(f.rule == rule and f.stage == "mg5" for f in fr_lint.lint_file(str(fr)))
