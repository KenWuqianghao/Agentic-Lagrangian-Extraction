"""Tests for the ablation's endpoint, its exact test and the budget curve.
No Wolfram kernel, MadGraph or network."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import endpoint  # noqa: E402
import retro  # noqa: E402

PASS = {
    "compile_ok": True,
    "madgraph_import_ok": True,
    "full_chain_pass": True,
    "checks": dict.fromkeys(retro.CHECKS, "pass"),
}
PARTICLES = "H = Particle(pdg_code = 25)\nX = Particle(pdg_code = 9000001)\nX__tilde__ = X.anti()\n"


def _run(
    tmp_path,
    score=PASS,
    verdict="VERDICT: NO DISCREPANCIES",
    vertices="particles = [ P.X__tilde__, P.X, P.H ]",
):
    d = tmp_path / "s1"
    (d / "model").mkdir(parents=True)
    fr = d / "model" / "P_gen.fr"
    fr.write_text('M$ModelName = "P_gen";\n')
    (d / "run.json").write_text("{}")
    (d / "validation_hepval.json").write_text(json.dumps(score))
    if verdict:
        (d / "post_review").mkdir()
        (d / "post_review" / "verdict.json").write_text(
            json.dumps(
                {"verdict": verdict, "model_sha": hashlib.sha256(fr.read_bytes()).hexdigest()}
            )
        )
    (d / "score_ufo").mkdir()
    (d / "score_ufo" / "particles.py").write_text(PARTICLES)
    (d / "score_ufo" / "vertices.py").write_text(vertices)
    return d


def test_endpoint_needs_the_chain_a_clean_referee_and_a_vertex_for_every_new_particle(tmp_path):
    assert endpoint.run_outcome(_run(tmp_path / "a"), "P")["endpoint"] is True
    failed_check = {
        **PASS,
        "checks": {**PASS["checks"], "hermiticity": "fail"},
        "full_chain_pass": False,
    }
    assert endpoint.run_outcome(_run(tmp_path / "b", score=failed_check), "P")["endpoint"] is False
    changed = endpoint.run_outcome(
        _run(tmp_path / "c", verdict="VERDICT: 1 PHYSICS-CHANGING, 0 COSMETIC"), "P"
    )
    assert changed["chain"] is True and changed["endpoint"] is False
    inert = endpoint.run_outcome(
        _run(tmp_path / "d", vertices="particles = [ P.H, P.H, P.H ]"), "P"
    )
    assert inert["particles_without_vertex"] == ["X"] and inert["endpoint"] is False


def test_a_chain_pass_without_a_referee_verdict_is_missing_not_a_pass(tmp_path):
    out = endpoint.run_outcome(_run(tmp_path, verdict=None), "P")
    assert out["endpoint"] is False and out["missing"] == ["referee"]


def test_exact_test_on_one_paper_is_fishers_test():
    # 3 of 3 against 0 of 3: one table of 20 is this extreme on each side.
    assert endpoint.exact_stratified([(3, 3, 0, 3)])["p"] == pytest.approx(2 / 20)
    # Papers where the arms tie (all pass, none pass) carry no evidence.
    assert endpoint.exact_stratified([(3, 3, 0, 3), (3, 3, 3, 3), (0, 3, 0, 3)])[
        "p"
    ] == pytest.approx(2 / 20)
    # Two papers in the same direction: (1/20)^2 on each side.
    assert endpoint.exact_stratified([(3, 3, 0, 3), (3, 3, 0, 3)])["p"] == pytest.approx(2 / 400)


def _call(passed: bool, lines: int) -> dict:
    return {"pass": passed, "lines": lines}


def test_budget_curve_counts_the_file_in_hand_at_the_cut():
    run = {
        "paper": "P",
        "score_pass": True,
        "calls": [_call(False, 300), _call(False, 300), _call(True, 300)],
    }
    late = {
        "paper": "Q",
        "score_pass": True,
        "calls": [_call(False, 300)] * 4,
    }  # passes on an unvalidated last edit
    curve = retro.budget_curve([run, late], budgets=(2, 3, 6))
    assert curve["2"]["at_budget"] == [] and curve["3"]["at_budget"] == ["P"]
    assert curve["6"]["at_budget"] == ["P", "Q"] and curve["6"]["first_pass"] == ["P"]
