"""
# test_rerun_predicates.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Tests for the physicist-finding predicates.

These predicates are the measurement instrument for the rerun benchmark, so
they are tested two ways: on synthetic minimal cases that isolate one
construct each, and on the real files whose verdict a physicist already
stated (the FeynRules-DB reference, which is right by construction, and the
reviewed agent file, which is wrong in a known way).

    python -m pytest eval/benchmark_runs/test_rerun_predicates.py -q
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))

import rerun_predicates as rp  # noqa: E402

REF_EFFLRSM = REPO / "eval" / "reference_cache" / "EffLRSM" / "effLRSM.fr"
REF_SEXTETS = REPO / "eval" / "reference_cache" / "368sextets" / "368sextets.fr"
REVIEWED_EFFLRSM = HERE / "EffLRSM" / "model" / "EffLRSM_gen.fr"


# ------------------------------------------------------- Z_R normalisation
def _zr(value: str) -> str:
    """A minimal .fr carrying one Z_R normalisation parameter."""
    return f"""M$ModelName = "T";
M$Parameters = {{
  gZR == {{
    ParameterType -> Internal,
    Value -> {value},
    Description -> "Overall ZR coupling, Eq.(8)"
  }}
}};
"""


@pytest.mark.parametrize("value", [
    "kRq*ee/sw/Sqrt[1 - tw2/kRq2]",                 # the reference's own form
    "kQR gw/Sqrt[1 - (sw/cw)^2/kQR^2]",             # spaces, explicit sw/cw
    "-kRq*(ee/sw)/Sqrt[1 - (sw/(cw*kRq))^2]",       # sign and parentheses
    "kRq*ee/(sw Sqrt[1 - tw2/kRq2])",               # root inside a divided group
    "kRq*ee/sw*(1 - tw2/kRq2)^(-1/2)",              # written as a power
])
def test_zr_divisor_forms_pass(value):
    ok, detail = rp.efflrsm_zr_normalisation(_zr(value))
    assert ok, detail


@pytest.mark.parametrize("value", [
    "-kRquark*(ee/sw)*Sqrt[1 - (sw/(cw*kRquark))^2]",   # the reviewed file's error
    "-kqR*gw*Sqrt[1 - tw2/kqR^2]",                      # same error, other names
    "kRq*ee/sw Sqrt[1 - tw2/kRq2]",                     # implicit multiplication
    "kRq*ee/sw*(1 - tw2/kRq2)^(1/2)",                   # positive power
])
def test_zr_multiplied_root_fails(value):
    ok, detail = rp.efflrsm_zr_normalisation(_zr(value))
    assert not ok
    assert "divides" in detail


def test_zr_absent_root_is_not_a_pass():
    ok, detail = rp.efflrsm_zr_normalisation(_zr("kRq*ee/sw"))
    assert not ok
    assert "no Z_R normalisation root" in detail


def test_zr_ignores_unrelated_roots():
    """A Sqrt[1 - x] with no weak-mixing symbol is some other physics."""
    ok, _ = rp.efflrsm_zr_normalisation(_zr("Sqrt[1 - 4 mtop^2/MZ^2]"))
    assert not ok  # no Z_R root found at all, rather than a false pass


def test_zr_reference_file_passes():
    ok, detail = rp.efflrsm_zr_normalisation(REF_EFFLRSM.read_text(errors="replace"))
    assert ok, detail


def test_zr_reviewed_agent_file_fails():
    """The file the physicists reviewed multiplies by the root (arXiv:1610.08985 Eq. 8)."""
    if not REVIEWED_EFFLRSM.is_file():
        pytest.skip("reviewed EffLRSM model not present in this checkout")
    ok, detail = rp.efflrsm_zr_normalisation(REVIEWED_EFFLRSM.read_text(errors="replace"))
    assert not ok
    assert "divides" in detail


# --------------------------------------------------- sextet gauge rep
def _sextet(index_decl: str, add_rep: str = "") -> str:
    return f"""M$ModelName = "T";
{index_decl}
{add_rep}
M$ClassesDescription = {{
  S[100] == {{
    ClassName -> Phiu,
    SelfConjugate -> False,
    Indices -> {{Index[Sextet]}},
    Mass -> {{MPhiu, 1000.}}
  }}
}};
"""


IDX = "IndexRange[Index[Sextet]] = NoUnfold[Range[6]];"
REP = "AddGaugeRepresentation[SU3C -> {T6, Sextet}];"


def test_sextet_with_gauge_representation_passes():
    ok, detail = rp.sextets_gauge_representation(_sextet(IDX, REP))
    assert ok, detail


def test_sextet_without_gauge_representation_fails():
    ok, detail = rp.sextets_gauge_representation(_sextet(IDX))
    assert not ok
    assert "AddGaugeRepresentation" in detail


def test_sextet_declared_but_unused_index_is_not_a_finding():
    """An index declared and never put on a field cannot break gluon couplings."""
    fr = f'M$ModelName = "T";\n{IDX}\nM$ClassesDescription = {{}};\n'
    ok, detail = rp.sextets_gauge_representation(fr)
    assert not ok
    assert "no new colour-representation index" in detail


def test_sextet_ignores_generation_sized_indices():
    """Range[3] is a generation index, not a colour representation."""
    fr = _sextet("IndexRange[Index[Sextet]] = NoUnfold[Range[3]];")
    ok, detail = rp.sextets_gauge_representation(fr)
    assert not ok
    assert "no new colour-representation index" in detail


def test_sextet_commented_out_representation_does_not_count():
    fr = _sextet(IDX, "(* " + REP + " *)")
    ok, _ = rp.sextets_gauge_representation(fr)
    assert not ok


def test_sextet_reference_file_passes():
    ok, detail = rp.sextets_gauge_representation(REF_SEXTETS.read_text(errors="replace"))
    assert ok, detail


# ------------------------------------------------ the four original findings
def test_original_predicates_still_agree_with_the_references():
    """The August findings' predicates, on the files whose verdict is known."""
    ok, detail = rp.efflrsm_charge_conjugation(REF_EFFLRSM.read_text(errors="replace"))
    assert ok, detail
    ok, detail = rp.sextets_explicit_cutoffs(REF_SEXTETS.read_text(errors="replace"))
    # Taylor Murphy's reference absorbs kappa/Lambda^n into dimensionful
    # coefficients, so it carries no explicit cutoff: the predicate must say so
    # rather than pass it.
    assert not ok, detail


def test_every_page_predicate_is_callable():
    for page, checks in rp.PREDICATES.items():
        for name, fn in checks:
            ok, detail = fn('M$ModelName = "empty";\n')
            assert isinstance(ok, bool) and isinstance(detail, str), (page, name)


# --------------------------------------- layout and indirection tolerance
HAND_WRITTEN_ZPRIME = """M$ModelName = "hand";

M$ClassesDescription = {

V[100] == {
  ClassName        -> V1,
  SelfConjugate    -> True,
  Mass             -> {MV1, 1500.},
  Width            -> {WV1, 229.31},
  ParticleName     -> "V1",
  PDG              -> 32
}

};

LV1Kin := Block[{mu, nu},
  ExpandIndices[ -1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu] ]];

LV1Top := Block[{mu}, ExpandIndices[ uqbar.cVL.Ga[mu].ProjM.uq V1[mu] ]];

LTotal := LV1Kin + LV1Top;
"""


def test_zprime_accepts_hand_written_layout():
    """The no-tools arm writes the .fr itself, with its own indentation and
    aligned arrows. A check tuned to the renderer's two-space layout marked
    those files wrong for a whitespace difference."""
    ok, detail = rp.zprime_free_field_terms(HAND_WRITTEN_ZPRIME)
    assert ok, detail


ZR_BY_NAME = """M$ModelName = "byname";
M$Parameters = {
  nZRq == {
    ParameterType -> Internal,
    Value         -> Sqrt[1 - tw2/kapRq^2],
    Description   -> "ZR quark coupling denominator, Eq.(8)"
  },
  gZRq == {
    ParameterType -> Internal,
    Value         -> 1,
    Description   -> "placeholder"
  }
};

LZRQ := Block[{mu}, ExpandIndices[ -(kapRq gw/nZRq) uqbar.Ga[mu].ProjP.uq ZR[mu] ]];
"""


def test_zr_root_named_then_divided_passes():
    """Defining the root as a parameter and dividing by that name is the same
    physics as dividing inline; reading the root's own position alone called
    it wrong."""
    ok, detail = rp.efflrsm_zr_normalisation(ZR_BY_NAME)
    assert ok, detail


def test_zr_root_named_then_multiplied_fails():
    bad = ZR_BY_NAME.replace("-(kapRq gw/nZRq)", "-(kapRq gw nZRq)")
    ok, detail = rp.efflrsm_zr_normalisation(bad)
    assert not ok
    assert "divides" in detail


# ------------------------------------------------ GeneralU1 robustness
_GU1_HEAD = """M$ModelName = "gu1";
M$Parameters = {
  xQL == {
    ParameterType -> Internal,
    Value         -> xH/6 + xPhi/3,
    Description   -> "U(1)X charge of the quark doublet QL"
  },
  %s
};
"""

_GU1_YUK_DOUBLET = """
LNuYuk := Block[{sp, ii, jj, ff1, ff2, yuk, gaugerules},
  gaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}];
  yuk = ExpandIndices[
    -ynu[ff1, ff2] LLbar[sp, ii, ff1].NR[sp, ff2] Phibar[jj] Eps[ii, jj],
    FlavorExpand -> SU2D];
  yuk + HC[yuk] /. gaugerules];
"""


def _gu1(charge_param, yukawa=_GU1_YUK_DOUBLET):
    return _GU1_HEAD % charge_param + yukawa


HIGGS_OK = """xHd == {
    ParameterType -> Internal,
    Value         -> xH/2,
    Description   -> "U(1)X charge of the SM.fr doublet Phi (Y = +1/2)"
  }"""


def test_generalu1_finds_higgs_charge_named_only_as_doublet_phi():
    """SM.fr calls the scalar doublet Phi, so a model may never write the word
    "Higgs". Matching only "Higgs doublet"/"SM Higgs" missed a correct file."""
    ok, detail = rp.generalu1_eps_and_higgs_charge(_gu1(HIGGS_OK))
    assert ok, detail


def test_generalu1_does_not_mistake_the_quark_doublet_for_the_higgs():
    """xQL is also a doublet charge symbolic in xH; matching "doublet" alone
    graded every file against the quark doublet."""
    ok, detail = rp.generalu1_eps_and_higgs_charge(_gu1(HIGGS_OK))
    assert ok and "xHd" in detail, detail


def test_generalu1_wrong_higgs_sign_still_fails():
    wrong = HIGGS_OK.replace("Value         -> xH/2", "Value         -> -xH/2")
    ok, detail = rp.generalu1_eps_and_higgs_charge(_gu1(wrong))
    assert not ok
    assert "+xH/2" in detail


def test_generalu1_reports_broken_phase_yukawa_distinctly():
    """A Yukawa written with the physical H and a light neutrino has no
    doublet and so no Eps; that is a different defect from a missing term."""
    broken = "LNuYuk := Block[{yuk}, yuk = -1/Sqrt[2] H vlbar.ynu.ProjP.NR; ExpandIndices[yuk + HC[yuk]]];\n"
    ok, detail = rp.generalu1_eps_and_higgs_charge(_gu1(HIGGS_OK, broken))
    assert not ok
    assert "broken phase" in detail


def test_statements_survive_semicolons_inside_block():
    """`Block[{...}, a = ...; b = ...; expr]` must stay one statement."""
    stmts = rp._statements(_GU1_YUK_DOUBLET)
    assert len(stmts) == 1, stmts
    assert "LLbar[" in stmts[0] and "Eps[ii, jj]" in stmts[0]
