#!/usr/bin/env python3
"""Prototype of the `massbasis` tool (option A): given a scalar potential in
the gauge basis, the vevs and a rotation to the mass basis, derive the
Lagrangian couplings as functions of the physical masses and the mixing
angle, so that the quadratic Lagrangian is diagonal SYMBOLICALLY and
FeynRules' CheckDiagonalMassTerms can pass on an add-on model.

This is the step the extraction and repair agents decline to do blind
("repairs must not change the physics"): it is a derivation, not a change.
The prototype uses sympy; the FeynRules run that confirms the check needs a
Wolfram kernel and is done separately.

Worked case: Higgs-singlet mixing (B-L, pNG dark matter, dilaton models).

    V = -mu1^2 |Phi|^2 + lam1 |Phi|^4 - mu2^2 |chi|^2 + lam2 |chi|^4
        + lam3 |Phi|^2 |chi|^2
    Phi -> (v + h_g)/sqrt(2),  chi -> (x + s_g)/sqrt(2)
    (h_g, s_g) = R(alpha) (h, H2)     with h, H2 the mass eigenstates

Output: the minimisation conditions (mu1^2, mu2^2) and the inverted couplings
(lam1, lam2, lam3) in terms of (mh, mH2, alpha, v, x), plus the FeynRules
Internal-parameter block that encodes them.
"""

from __future__ import annotations

import sympy as sp


def higgs_singlet():
    v, x, a = sp.symbols("vev xBL alpha", positive=True)
    mh, mH = sp.symbols("MH MH2", positive=True)
    lam1, lam2, lam3, mu1s, mu2s = sp.symbols("lam1BL lam2BL lam3BL mu1sq mu2sq", real=True)
    h, H2 = sp.symbols("h H2", real=True)

    # gauge-basis fluctuations as a rotation of the mass eigenstates
    hg = sp.cos(a) * h - sp.sin(a) * H2
    sg = sp.sin(a) * h + sp.cos(a) * H2
    phi2 = (v + hg) ** 2 / 2  # |Phi|^2 in unitary gauge, neutral component
    chi2 = (x + sg) ** 2 / 2
    V = -mu1s * phi2 + lam1 * phi2 ** 2 - mu2s * chi2 + lam2 * chi2 ** 2 + lam3 * phi2 * chi2
    V = sp.expand(V)

    # tadpoles vanish
    t1 = sp.Eq(sp.diff(V, h).subs({h: 0, H2: 0}), 0)
    t2 = sp.Eq(sp.diff(V, H2).subs({h: 0, H2: 0}), 0)
    mus = sp.solve([t1, t2], [mu1s, mu2s], dict=True)[0]
    Vm = sp.expand(V.subs(mus))

    # quadratic sector must be diagonal with the physical masses
    q_hh = sp.diff(Vm, h, 2).subs({h: 0, H2: 0}) / 1  # coefficient of h^2/2 -> mass^2
    q_HH = sp.diff(Vm, H2, 2).subs({h: 0, H2: 0})
    q_hH = sp.diff(Vm, h, H2).subs({h: 0, H2: 0})
    sol = sp.solve([sp.Eq(q_hh, mh ** 2), sp.Eq(q_HH, mH ** 2), sp.Eq(q_hH, 0)],
                   [lam1, lam2, lam3], dict=True)[0]
    sol = {k: sp.simplify(sp.trigsimp(vv)) for k, vv in sol.items()}
    mus = {k: sp.simplify(vv.subs(sol)) for k, vv in mus.items()}

    # verify: with the inverted couplings the cross term vanishes identically
    Vchk = sp.expand(V.subs(mus).subs(sol))
    cross = sp.simplify(sp.diff(Vchk, h, H2).subs({h: 0, H2: 0}))
    assert cross == 0, cross
    assert sp.simplify(sp.diff(Vchk, h, 2).subs({h: 0, H2: 0}) - mh ** 2) == 0
    assert sp.simplify(sp.diff(Vchk, H2, 2).subs({h: 0, H2: 0}) - mH ** 2) == 0
    return sol, mus


def to_feynrules(sol, mus) -> str:
    def mma(e):
        s = sp.mathematica_code(e)
        return s.replace("Sin[alpha]", "sa").replace("Cos[alpha]", "ca")
    lines = []
    for name, expr, desc in [
        ("lam1BL", sol[sp.Symbol("lam1BL", real=True)], "doublet quartic, from (MH, MH2, alpha)"),
        ("lam2BL", sol[sp.Symbol("lam2BL", real=True)], "singlet quartic, from (MH, MH2, alpha)"),
        ("lam3BL", sol[sp.Symbol("lam3BL", real=True)], "portal quartic, from (MH, MH2, alpha)"),
        ("mu1sq", mus[sp.Symbol("mu1sq", real=True)], "doublet mass parameter, tadpole condition"),
        ("mu2sq", mus[sp.Symbol("mu2sq", real=True)], "singlet mass parameter, tadpole condition"),
    ]:
        lines.append(f"""  {name} == {{
    ParameterType -> Internal,
    Value         -> {mma(expr)},
    InteractionOrder -> {{NP, 2}},
    Description   -> "{desc}"
  }},""")
    return "\n".join(lines)


if __name__ == "__main__":
    sol, mus = higgs_singlet()
    print("# inverted parametrisation (cross term vanishes identically)")
    for k, vv in sol.items():
        print(f"{k} = {vv}")
    for k, vv in mus.items():
        print(f"{k} = {vv}")
    print("\n# FeynRules Internal parameters (sa = Sin[alpha], ca = Cos[alpha] declared Internal)")
    print(to_feynrules(sol, mus))
    print("""
# Field declarations the add-on needs (SM `H` stays the physical Higgs from SM.fr):
#   S[102] == { ClassName -> H2, SelfConjugate -> True, Mass -> {MH2, 500.}, ... }
#   S[103] == { ClassName -> hg, Unphysical -> True, SelfConjugate -> True,
#               Definitions -> { hg -> ca H - sa H2 } }
#   S[104] == { ClassName -> sg, Unphysical -> True, SelfConjugate -> True,
#               Definitions -> { sg -> sa H + ca H2 } }
# Write the potential with hg, sg (and the singlet vev xBL), NOT with H, H2, and
# subtract the SM potential SM.fr already adds:  LPot := -(V[hg, sg] - VSM[hg]).""")
