I'll start by reading the paper and the schema files.
I read the paper and the schema. Below is the mandatory self-audit, then the JSON.

## Model content (from the paper)

New states are in Table X and Eqs. (12)–(13): two colour‑sextet complex scalars **Φ_u, Φ_d** and two colour‑sextet Dirac fermions **Ψ_u, Ψ_d**, all SU(2)_L singlets.

Hypercharge re‑derivation with SM.fr conventions (uR: Y=2/3, dR: Y=−1/3, lR: Y=−1). The bar of a charge‑conjugated field, `\overline{q^c}` = q^T C, carries the **same** charge as q. So:
- `\overline{u_R^c} Ψ_u G`: 2/3 + Y(Ψ_u) = 0 → Y(Ψ_u) = −2/3 ✓ (Table X)
- `\overline{d_R^c} Ψ_d G`: −1/3 + Y(Ψ_d) = 0 → Y(Ψ_d) = +1/3 ✓
- `Φ_u \overline{u_R^c} l_R G`: Y(Φ_u) + 2/3 − 1 = 0 → Y(Φ_u) = +1/3 ✓
- `Φ_d \overline{d_R^c} l_R G`: Y(Φ_d) − 1/3 − 1 = 0 → Y(Φ_d) = +4/3 ✓

All four are SU(2) singlets, so Q = Y. The sign choice is fixed by SM.fr, not by the paper table; both agree.

Colour contraction: J^{sia} is built from existing FeynRules objects with Eq. (A18), `J = -I Eps[i,j,k] T[a,l,j] K6bar[s,l,k]`, because √2 L^{ijk} = ε^{ijk}.

## Self-audit table

| term | fields | d | coupling | coup. dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | L sum | CC[] | H.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LPsiukin | Ψu̅ D̸ Ψu, MPsiu Ψu̅Ψu | 4 | MPsiu | n/a (mass) | n/a | −2/3+2/3=0 | 0 | singlet | 6⊗6̄ (DC) | 0 | n/a | self-conj. bilinear |
| LPsidkin | Ψd̅ D̸ Ψd, MPsid Ψd̅Ψd | 4 | MPsid | n/a | n/a | 1/3−1/3=0 | 0 | singlet | 6⊗6̄ | 0 | n/a | self-conj. |
| LPhiukin | DΦu† DΦu, MPhiu²Φu†Φu | 4 | MPhiu | n/a | n/a | 1/3−1/3=0 | 0 | singlet | 6⊗6̄ | −1+1=0 | n/a | self-conj. |
| LPhidkin | DΦd† DΦd, MPhid²Φd†Φd | 4 | MPhid | n/a | n/a | 4/3−4/3=0 | 0 | singlet | 6⊗6̄ | 0 | n/a | self-conj. |
| LPsiuG | `bar[u_R^c]` σ Ψu G_{μν} | 5 | kapu/LamPsiu | −1 | 1/Λ¹ ✓ | 2/3−2/3=0 | 0 | singlet | J: 3⊗6⊗8 | 0+0=0 | yes | HC[] |
| LPsidG | `bar[d_R^c]` σ Ψd G_{μν} | 5 | kapd/LamPsid | −1 | 1/Λ¹ ✓ | −1/3+1/3=0 | 0 | singlet | J: 3⊗6⊗8 | 0 | yes | HC[] |
| LPsiuB | `bar[u_R^c]` Ψu B_{μν}G_{μν} | 7 | kapuB/LamPsiuB³ | −3 | 1/Λ³ ✓ | 0 | 0 | singlet | J: 3⊗6⊗8 | 0 | yes | HC[] |
| LPsidB | `bar[d_R^c]` Ψd B_{μν}G_{μν} | 7 | kapdB/LamPsidB³ | −3 | 1/Λ³ ✓ | 0 | 0 | singlet | J: 3⊗6⊗8 | 0 | yes | HC[] |
| LPhiuG | Φu `bar[u_R^c]` σ l_R G_{μν} | 6 | lamu/LamPhiu² | −2 | 1/Λ² ✓ | 1/3+2/3−1=0 | 0 | singlet | J: 3⊗6⊗8 | −1+0+1=0 | yes | HC[] |
| LPhidG | Φd `bar[d_R^c]` σ l_R G_{μν} | 6 | lamd/LamPhid² | −2 | 1/Λ² ✓ | 4/3−1/3−1=0 | 0 | singlet | J: 3⊗6⊗8 | 0 | yes | HC[] |

Kinetic + mass terms exist for Ψu, Ψd, Φu, Φd, and all four are in the total sum `LSextet`.

`SelfConjugate -> True` classes: **none**. All four new fields are complex, so no class carries a forbidden quantum number.

Reference or cached model file read: **none**. I read only the paper text, `frmodel.py`, and `SM.fr`.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["Linda M. Carpenter", "Taylor Murphy", "Tim M. P. Tait"],
    "version": "1.0",
    "date": "07. 09. 2022",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [
    {"name": "Sextet", "range_kind": "NoUnfold", "size": 6, "style_symbol": "sxt"}
  ],
  "parameters": [
    {
      "name": "kapu",
      "parameter_type": "External",
      "block_name": "KAPU",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05"},
        {"lhs": "kapu[2]", "rhs": "0.05"},
        {"lhs": "kapu[3]", "rhs": "0.05"}
      ],
      "tex": "Superscript[Subscript[\\[Kappa],u],I]",
      "description": "Dimensionless coupling kappa^I_u of Psiu to up-type quark I and a gluon, Eq.(12) line 2; benchmark 0.05"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "block_name": "KAPD",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05"},
        {"lhs": "kapd[2]", "rhs": "0.05"},
        {"lhs": "kapd[3]", "rhs": "0.05"}
      ],
      "tex": "Superscript[Subscript[\\[Kappa],d],I]",
      "description": "Dimensionless coupling kappa^I_d of Psid to down-type quark I and a gluon, Eq.(12) line 2; benchmark 0.05"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "block_name": "KAPUB",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.10"},
        {"lhs": "kapuB[2]", "rhs": "0.10"},
        {"lhs": "kapuB[3]", "rhs": "0.10"}
      ],
      "tex": "Superscript[Subscript[\\[Kappa],uB],I]",
      "description": "Dimensionless coupling kappa^I_uB of Psiu to up-type quark I, a gluon and a B boson, Eq.(12) line 3; benchmark 0.10"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "block_name": "KAPDB",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.10"},
        {"lhs": "kapdB[2]", "rhs": "0.10"},
        {"lhs": "kapdB[3]", "rhs": "0.10"}
      ],
      "tex": "Superscript[Subscript[\\[Kappa],dB],I]",
      "description": "Dimensionless coupling kappa^I_dB of Psid to down-type quark I, a gluon and a B boson, Eq.(12) line 3; benchmark 0.10"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "block_name": "LAMU",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamu[1,1]", "rhs": "0.1"},
        {"lhs": "lamu[1,2]", "rhs": "0."},
        {"lhs": "lamu[1,3]", "rhs": "0."},
        {"lhs": "lamu[2,1]", "rhs": "0."},
        {"lhs": "lamu[2,2]", "rhs": "0.1"},
        {"lhs": "lamu[2,3]", "rhs": "0."},
        {"lhs": "lamu[3,1]", "rhs": "0."},
        {"lhs": "lamu[3,2]", "rhs": "0."},
        {"lhs": "lamu[3,3]", "rhs": "0.1"}
      ],
      "tex": "Superscript[Subscript[\\[Lambda],u],XI]",
      "description": "Dimensionless coupling lambda^{XI}_u of Phiu to lepton X, up-type quark I and a gluon, Eq.(13); benchmark 0.1 times IndexDelta[X,I]"
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "block_name": "LAMD",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamd[1,1]", "rhs": "0.1"},
        {"lhs": "lamd[1,2]", "rhs": "0."},
        {"lhs": "lamd[1,3]", "rhs": "0."},
        {"lhs": "lamd[2,1]", "rhs": "0."},
        {"lhs": "lamd[2,2]", "rhs": "0.1"},
        {"lhs": "lamd[2,3]", "rhs": "0."},
        {"lhs": "lamd[3,1]", "rhs": "0."},
        {"lhs": "lamd[3,2]", "rhs": "0."},
        {"lhs": "lamd[3,3]", "rhs": "0.1"}
      ],
      "tex": "Superscript[Subscript[\\[Lambda],d],XI]",
      "description": "Dimensionless coupling lambda^{XI}_d of Phid to lepton X, down-type quark I and a gluon, Eq.(13); benchmark 0.1 times IndexDelta[X,I]"
    },
    {
      "name": "LamPsiu",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 1,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPsi]u]",
      "description": "EFT cutoff [GeV] of the Psiu-quark-gluon operator, Eq.(12) line 2; benchmark 1 TeV"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 2,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPsi]d]",
      "description": "EFT cutoff [GeV] of the Psid-quark-gluon operator, Eq.(12) line 2; benchmark 1 TeV"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 3,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPsi]uB]",
      "description": "EFT cutoff [GeV] of the Psiu-quark-gluon-B operator, Eq.(12) line 3; benchmark 1 TeV"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 4,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPsi]dB]",
      "description": "EFT cutoff [GeV] of the Psid-quark-gluon-B operator, Eq.(12) line 3; benchmark 1 TeV"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 5,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPhi]u]",
      "description": "EFT cutoff [GeV] of the Phiu-quark-lepton-gluon operator, Eq.(13); benchmark 1 TeV"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 6,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPhi]d]",
      "description": "EFT cutoff [GeV] of the Phid-quark-lepton-gluon operator, Eq.(13); benchmark 1 TeV"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "Phiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhiu", "value": "1000."},
      "width": {"sym": "WPhiu", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "-1"},
      "pdg": 6000001,
      "particle_name": "Phiu",
      "antiparticle_name": "Phiu~",
      "full_name": "Colour-sextet scalar coupling to up-type quarks",
      "propagator_label": "Phiu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Phid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhid", "value": "1000."},
      "width": {"sym": "WPhid", "value": "1."},
      "quantum_numbers": {"Q": "4/3", "Y": "4/3", "LeptonNumber": "-1"},
      "pdg": 6000002,
      "particle_name": "Phid",
      "antiparticle_name": "Phid~",
      "full_name": "Colour-sextet scalar coupling to down-type quarks",
      "propagator_label": "Phid",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Psiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiu", "value": "1000."},
      "width": {"sym": "WPsiu", "value": "1."},
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3"},
      "pdg": 6000003,
      "particle_name": "Psiu",
      "antiparticle_name": "Psiu~",
      "full_name": "Colour-sextet Dirac fermion coupling to up-type quarks",
      "propagator_label": "Psiu",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "Psid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsid", "value": "1000."},
      "width": {"sym": "WPsid", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3"},
      "pdg": 6000004,
      "particle_name": "Psid",
      "antiparticle_name": "Psid~",
      "full_name": "Colour-sextet Dirac fermion coupling to down-type quarks",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LPsiukin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I Psiubar.Ga[mu].DC[Psiu, mu] - MPsiu Psiubar.Psiu]]"
    },
    {
      "name": "LPsidkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I Psidbar.Ga[mu].DC[Psid, mu] - MPsid Psidbar.Psid]]"
    },
    {
      "name": "LPhiukin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phiubar[ss], mu] DC[Phiu[ss], mu] - MPhiu^2 Phiubar[ss] Phiu[ss]]]"
    },
    {
      "name": "LPhidkin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phidbar[ss], mu] DC[Phid[ss], mu] - MPhid^2 Phidbar[ss] Phid[ss]]]"
    },
    {
      "name": "LPsiuG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, sp3, ii, jj, kk, ll, ss, aa, ff, op}, op = kapu[ff]/LamPsiu (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] (I/2) (Ga[mu, sp1, sp3] Ga[nu, sp3, sp2] - Ga[nu, sp1, sp3] Ga[mu, sp3, sp2]) CC[uRbar[sp1, ff, ii]] Psiu[sp2, ss] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPsidG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, sp3, ii, jj, kk, ll, ss, aa, ff, op}, op = kapd[ff]/LamPsid (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] (I/2) (Ga[mu, sp1, sp3] Ga[nu, sp3, sp2] - Ga[nu, sp1, sp3] Ga[mu, sp3, sp2]) CC[dRbar[sp1, ff, ii]] Psid[sp2, ss] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPsiuB",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, ii, jj, kk, ll, ss, aa, ff, op}, op = kapuB[ff]/LamPsiuB^3 (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] CC[uRbar[sp1, ff, ii]] Psiu[sp1, ss] FS[B, mu, nu] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPsidB",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, ii, jj, kk, ll, ss, aa, ff, op}, op = kapdB[ff]/LamPsidB^3 (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] CC[dRbar[sp1, ff, ii]] Psid[sp1, ss] FS[B, mu, nu] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPhiuG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, sp3, ii, jj, kk, ll, ss, aa, ff, xx, op}, op = lamu[xx, ff]/LamPhiu^2 (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] Phiu[ss] (I/2) (Ga[mu, sp1, sp3] Ga[nu, sp3, sp2] - Ga[nu, sp1, sp3] Ga[mu, sp3, sp2]) CC[uRbar[sp1, ff, ii]] lR[sp2, xx] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPhidG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, sp3, ii, jj, kk, ll, ss, aa, ff, xx, op}, op = lamd[xx, ff]/LamPhid^2 (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] Phid[ss] (I/2) (Ga[mu, sp1, sp3] Ga[nu, sp3, sp2] - Ga[nu, sp1, sp3] Ga[mu, sp3, sp2]) CC[dRbar[sp1, ff, ii]] lR[sp2, xx] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LSextet",
      "delayed": true,
      "expression": "LPsiukin + LPsidkin + LPhiukin + LPhidkin + LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuG + LPhidG"
    }
  ],
  "raw_preamble": [
    "(* Colour-sextet fields carry Index[Sextet]. The Clebsch-Gordan coefficients J^{s i a} of Table I are written with existing FeynRules objects through Eq.(A18): J[s,i,a] = -I Eps[i,j,k] T[a,l,j] K6bar[s,l,k], since Sqrt[2] L^{ijk} = Eps[i,j,k]. *)"
  ]
}
```
I read the paper and the schema. Below is the mandatory self-audit, then the JSON.

## Model content (from the paper)

New states are in Table X and Eqs. (12)–(13): two colour‑sextet complex scalars **Φ_u, Φ_d** and two colour‑sextet Dirac fermions **Ψ_u, Ψ_d**, all SU(2)_L singlets.

Hypercharge re‑derivation with SM.fr conventions (uR: Y=2/3, dR: Y=−1/3, lR: Y=−1). The bar of a charge‑conjugated field, `\overline{q^c}` = q^T C, carries the **same** charge as q. So:
- `\overline{u_R^c} Ψ_u G`: 2/3 + Y(Ψ_u) = 0 → Y(Ψ_u) = −2/3 ✓ (Table X)
- `\overline{d_R^c} Ψ_d G`: −1/3 + Y(Ψ_d) = 0 → Y(Ψ_d) = +1/3 ✓
- `Φ_u \overline{u_R^c} l_R G`: Y(Φ_u) + 2/3 − 1 = 0 → Y(Φ_u) = +1/3 ✓
- `Φ_d \overline{d_R^c} l_R G`: Y(Φ_d) − 1/3 − 1 = 0 → Y(Φ_d) = +4/3 ✓

All four are SU(2) singlets, so Q = Y. The sign choice is fixed by SM.fr, not by the paper table; both agree.

Colour contraction: J^{sia} is built from existing FeynRules objects with Eq. (A18), `J = -I Eps[i,j,k] T[a,l,j] K6bar[s,l,k]`, because √2 L^{ijk} = ε^{ijk}.

## Self-audit table

| term | fields | d | coupling | coup. dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | L sum | CC[] | H.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LPsiukin | Ψu̅ D̸ Ψu, MPsiu Ψu̅Ψu | 4 | MPsiu | n/a (mass) | n/a | −2/3+2/3=0 | 0 | singlet | 6⊗6̄ (DC) | 0 | n/a | self-conj. bilinear |
| LPsidkin | Ψd̅ D̸ Ψd, MPsid Ψd̅Ψd | 4 | MPsid | n/a | n/a | 1/3−1/3=0 | 0 | singlet | 6⊗6̄ | 0 | n/a | self-conj. |
| LPhiukin | DΦu† DΦu, MPhiu²Φu†Φu | 4 | MPhiu | n/a | n/a | 1/3−1/3=0 | 0 | singlet | 6⊗6̄ | −1+1=0 | n/a | self-conj. |
| LPhidkin | DΦd† DΦd, MPhid²Φd†Φd | 4 | MPhid | n/a | n/a | 4/3−4/3=0 | 0 | singlet | 6⊗6̄ | 0 | n/a | self-conj. |
| LPsiuG | `bar[u_R^c]` σ Ψu G_{μν} | 5 | kapu/LamPsiu | −1 | 1/Λ¹ ✓ | 2/3−2/3=0 | 0 | singlet | J: 3⊗6⊗8 | 0+0=0 | yes | HC[] |
| LPsidG | `bar[d_R^c]` σ Ψd G_{μν} | 5 | kapd/LamPsid | −1 | 1/Λ¹ ✓ | −1/3+1/3=0 | 0 | singlet | J: 3⊗6⊗8 | 0 | yes | HC[] |
| LPsiuB | `bar[u_R^c]` Ψu B_{μν}G_{μν} | 7 | kapuB/LamPsiuB³ | −3 | 1/Λ³ ✓ | 0 | 0 | singlet | J: 3⊗6⊗8 | 0 | yes | HC[] |
| LPsidB | `bar[d_R^c]` Ψd B_{μν}G_{μν} | 7 | kapdB/LamPsidB³ | −3 | 1/Λ³ ✓ | 0 | 0 | singlet | J: 3⊗6⊗8 | 0 | yes | HC[] |
| LPhiuG | Φu `bar[u_R^c]` σ l_R G_{μν} | 6 | lamu/LamPhiu² | −2 | 1/Λ² ✓ | 1/3+2/3−1=0 | 0 | singlet | J: 3⊗6⊗8 | −1+0+1=0 | yes | HC[] |
| LPhidG | Φd `bar[d_R^c]` σ l_R G_{μν} | 6 | lamd/LamPhid² | −2 | 1/Λ² ✓ | 4/3−1/3−1=0 | 0 | singlet | J: 3⊗6⊗8 | 0 | yes | HC[] |

Kinetic + mass terms exist for Ψu, Ψd, Φu, Φd, and all four are in the total sum `LSextet`.

`SelfConjugate -> True` classes: **none**. All four new fields are complex, so no class carries a forbidden quantum number.

Reference or cached model file read: **none**. I read only the paper text, `frmodel.py`, and `SM.fr`.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["Linda M. Carpenter", "Taylor Murphy", "Tim M. P. Tait"],
    "version": "1.0",
    "date": "07. 09. 2022",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [
    {"name": "Sextet", "range_kind": "NoUnfold", "size": 6, "style_symbol": "sxt"}
  ],
  "parameters": [
    {
      "name": "kapu",
      "parameter_type": "External",
      "block_name": "KAPU",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05"},
        {"lhs": "kapu[2]", "rhs": "0.05"},
        {"lhs": "kapu[3]", "rhs": "0.05"}
      ],
      "tex": "Superscript[Subscript[\\[Kappa],u],I]",
      "description": "Dimensionless coupling kappa^I_u of Psiu to up-type quark I and a gluon, Eq.(12) line 2; benchmark 0.05"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "block_name": "KAPD",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05"},
        {"lhs": "kapd[2]", "rhs": "0.05"},
        {"lhs": "kapd[3]", "rhs": "0.05"}
      ],
      "tex": "Superscript[Subscript[\\[Kappa],d],I]",
      "description": "Dimensionless coupling kappa^I_d of Psid to down-type quark I and a gluon, Eq.(12) line 2; benchmark 0.05"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "block_name": "KAPUB",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.10"},
        {"lhs": "kapuB[2]", "rhs": "0.10"},
        {"lhs": "kapuB[3]", "rhs": "0.10"}
      ],
      "tex": "Superscript[Subscript[\\[Kappa],uB],I]",
      "description": "Dimensionless coupling kappa^I_uB of Psiu to up-type quark I, a gluon and a B boson, Eq.(12) line 3; benchmark 0.10"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "block_name": "KAPDB",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.10"},
        {"lhs": "kapdB[2]", "rhs": "0.10"},
        {"lhs": "kapdB[3]", "rhs": "0.10"}
      ],
      "tex": "Superscript[Subscript[\\[Kappa],dB],I]",
      "description": "Dimensionless coupling kappa^I_dB of Psid to down-type quark I, a gluon and a B boson, Eq.(12) line 3; benchmark 0.10"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "block_name": "LAMU",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamu[1,1]", "rhs": "0.1"},
        {"lhs": "lamu[1,2]", "rhs": "0."},
        {"lhs": "lamu[1,3]", "rhs": "0."},
        {"lhs": "lamu[2,1]", "rhs": "0."},
        {"lhs": "lamu[2,2]", "rhs": "0.1"},
        {"lhs": "lamu[2,3]", "rhs": "0."},
        {"lhs": "lamu[3,1]", "rhs": "0."},
        {"lhs": "lamu[3,2]", "rhs": "0."},
        {"lhs": "lamu[3,3]", "rhs": "0.1"}
      ],
      "tex": "Superscript[Subscript[\\[Lambda],u],XI]",
      "description": "Dimensionless coupling lambda^{XI}_u of Phiu to lepton X, up-type quark I and a gluon, Eq.(13); benchmark 0.1 times IndexDelta[X,I]"
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "block_name": "LAMD",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamd[1,1]", "rhs": "0.1"},
        {"lhs": "lamd[1,2]", "rhs": "0."},
        {"lhs": "lamd[1,3]", "rhs": "0."},
        {"lhs": "lamd[2,1]", "rhs": "0."},
        {"lhs": "lamd[2,2]", "rhs": "0.1"},
        {"lhs": "lamd[2,3]", "rhs": "0."},
        {"lhs": "lamd[3,1]", "rhs": "0."},
        {"lhs": "lamd[3,2]", "rhs": "0."},
        {"lhs": "lamd[3,3]", "rhs": "0.1"}
      ],
      "tex": "Superscript[Subscript[\\[Lambda],d],XI]",
      "description": "Dimensionless coupling lambda^{XI}_d of Phid to lepton X, down-type quark I and a gluon, Eq.(13); benchmark 0.1 times IndexDelta[X,I]"
    },
    {
      "name": "LamPsiu",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 1,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPsi]u]",
      "description": "EFT cutoff [GeV] of the Psiu-quark-gluon operator, Eq.(12) line 2; benchmark 1 TeV"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 2,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPsi]d]",
      "description": "EFT cutoff [GeV] of the Psid-quark-gluon operator, Eq.(12) line 2; benchmark 1 TeV"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 3,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPsi]uB]",
      "description": "EFT cutoff [GeV] of the Psiu-quark-gluon-B operator, Eq.(12) line 3; benchmark 1 TeV"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 4,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPsi]dB]",
      "description": "EFT cutoff [GeV] of the Psid-quark-gluon-B operator, Eq.(12) line 3; benchmark 1 TeV"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 5,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPhi]u]",
      "description": "EFT cutoff [GeV] of the Phiu-quark-lepton-gluon operator, Eq.(13); benchmark 1 TeV"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "block_name": "CUTOFF",
      "order_block": 6,
      "value": "1000.",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[\\[CapitalLambda],\\[CapitalPhi]d]",
      "description": "EFT cutoff [GeV] of the Phid-quark-lepton-gluon operator, Eq.(13); benchmark 1 TeV"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "Phiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhiu", "value": "1000."},
      "width": {"sym": "WPhiu", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "-1"},
      "pdg": 6000001,
      "particle_name": "Phiu",
      "antiparticle_name": "Phiu~",
      "full_name": "Colour-sextet scalar coupling to up-type quarks",
      "propagator_label": "Phiu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Phid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhid", "value": "1000."},
      "width": {"sym": "WPhid", "value": "1."},
      "quantum_numbers": {"Q": "4/3", "Y": "4/3", "LeptonNumber": "-1"},
      "pdg": 6000002,
      "particle_name": "Phid",
      "antiparticle_name": "Phid~",
      "full_name": "Colour-sextet scalar coupling to down-type quarks",
      "propagator_label": "Phid",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Psiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiu", "value": "1000."},
      "width": {"sym": "WPsiu", "value": "1."},
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3"},
      "pdg": 6000003,
      "particle_name": "Psiu",
      "antiparticle_name": "Psiu~",
      "full_name": "Colour-sextet Dirac fermion coupling to up-type quarks",
      "propagator_label": "Psiu",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "Psid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsid", "value": "1000."},
      "width": {"sym": "WPsid", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3"},
      "pdg": 6000004,
      "particle_name": "Psid",
      "antiparticle_name": "Psid~",
      "full_name": "Colour-sextet Dirac fermion coupling to down-type quarks",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LPsiukin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I Psiubar.Ga[mu].DC[Psiu, mu] - MPsiu Psiubar.Psiu]]"
    },
    {
      "name": "LPsidkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I Psidbar.Ga[mu].DC[Psid, mu] - MPsid Psidbar.Psid]]"
    },
    {
      "name": "LPhiukin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phiubar[ss], mu] DC[Phiu[ss], mu] - MPhiu^2 Phiubar[ss] Phiu[ss]]]"
    },
    {
      "name": "LPhidkin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phidbar[ss], mu] DC[Phid[ss], mu] - MPhid^2 Phidbar[ss] Phid[ss]]]"
    },
    {
      "name": "LPsiuG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, sp3, ii, jj, kk, ll, ss, aa, ff, op}, op = kapu[ff]/LamPsiu (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] (I/2) (Ga[mu, sp1, sp3] Ga[nu, sp3, sp2] - Ga[nu, sp1, sp3] Ga[mu, sp3, sp2]) CC[uRbar[sp1, ff, ii]] Psiu[sp2, ss] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPsidG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, sp3, ii, jj, kk, ll, ss, aa, ff, op}, op = kapd[ff]/LamPsid (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] (I/2) (Ga[mu, sp1, sp3] Ga[nu, sp3, sp2] - Ga[nu, sp1, sp3] Ga[mu, sp3, sp2]) CC[dRbar[sp1, ff, ii]] Psid[sp2, ss] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPsiuB",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, ii, jj, kk, ll, ss, aa, ff, op}, op = kapuB[ff]/LamPsiuB^3 (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] CC[uRbar[sp1, ff, ii]] Psiu[sp1, ss] FS[B, mu, nu] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPsidB",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, ii, jj, kk, ll, ss, aa, ff, op}, op = kapdB[ff]/LamPsidB^3 (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] CC[dRbar[sp1, ff, ii]] Psid[sp1, ss] FS[B, mu, nu] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPhiuG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, sp3, ii, jj, kk, ll, ss, aa, ff, xx, op}, op = lamu[xx, ff]/LamPhiu^2 (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] Phiu[ss] (I/2) (Ga[mu, sp1, sp3] Ga[nu, sp3, sp2] - Ga[nu, sp1, sp3] Ga[mu, sp3, sp2]) CC[uRbar[sp1, ff, ii]] lR[sp2, xx] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPhidG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, sp3, ii, jj, kk, ll, ss, aa, ff, xx, op}, op = lamd[xx, ff]/LamPhid^2 (-I) Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] Phid[ss] (I/2) (Ga[mu, sp1, sp3] Ga[nu, sp3, sp2] - Ga[nu, sp1, sp3] Ga[mu, sp3, sp2]) CC[dRbar[sp1, ff, ii]] lR[sp2, xx] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LSextet",
      "delayed": true,
      "expression": "LPsiukin + LPsidkin + LPhiukin + LPhidkin + LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuG + LPhidG"
    }
  ],
  "raw_preamble": [
    "(* Colour-sextet fields carry Index[Sextet]. The Clebsch-Gordan coefficients J^{s i a} of Table I are written with existing FeynRules objects through Eq.(A18): J[s,i,a] = -I Eps[i,j,k] T[a,l,j] K6bar[s,l,k], since Sqrt[2] L^{ijk} = Eps[i,j,k]. *)"
  ]
}
```