I read the paper LaTeX source, the schema, the renderer, and `SM.fr`. No reference or cached `.fr` model file for EffLRSM exists in the sandbox, and none was read.

## Mandatory self-audit

| term name | fields in monomial | d | coupling symbol | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] where paper writes ψ^c | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin | FS[WRbar]·FS[WR]; WRbar·WR | 4 | MWR (mass term) | 1 (mass) | n/a | −1+1=0 | n/a (no Y on WR) | singlet (no SU(2) index) | singlet | no new U(1) in model | n/a | n/a | n/a | self-conjugate pair (Xbar X) |
| LZRkin | FS[ZR]·FS[ZR]; ZR·ZR | 4 | MZR (mass term) | 1 (mass) | n/a | 0 | n/a | singlet | singlet | none | n/a | n/a | n/a | real field, self-conjugate |
| LNkin | NNbar Ga del NN; NNbar MNmat NN | 4 | MNmat | 1 (mass) | n/a | 0 | n/a | singlet | singlet | none | Majorana: L not conserved, no L assigned | n/a | n/a | Majorana, self-conjugate |
| LWRq | uqbar, dq, WR | 4 | gWRq = −kapRq·gw/Sqrt[2] | 0 | n/a | −2/3−1/3+1=0 | n/a (physical mass eigenstates carry Q, not Y) | singlet (mass eigenstates, no SU2D index) | 3bar⊗3 singlet, implicit Colour contraction in Dot chain | none | B: −1/3+1/3=0 | n/a | Eq.(3): −κ_R^q g/√2, denominator √2 read from `\frac{-\kappa_R^q g}{\sqrt{2}}` in the LaTeX; cross-checked by Γ(W_R→qq̄′)=N_c κ²g²M/48π → 50.7 GeV reproduced | HC[...] |
| LWRlN | NNbar, l, WR | 4 | gWRl = −kapRl·gw/Sqrt[2] | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | none | not assigned (Majorana N) | n/a (paper writes N̄, not N^c) | Eq.(4) √2 in denominator (LaTeX `\frac{-\kappa_R^\ell g}{\sqrt{2}}`); Γ(W_R→ℓN)=8.41 GeV reproduced | HC[...] |
| LWRlnu | CC[vlbar], l, WR | 4 | gWRl | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | none | not assigned | yes — paper writes ν̄^c_m, written as CC[vlbar] | Eq.(4), same √2 | HC[...] |
| LZRff | uqbar/dqbar/lbar/vlbar/NNbar, same field, ZR | 4 | zRuL,zRuR,zRdL,zRdR,zReL,zReR,zRvL,zRnR | 0 | n/a | −Q+Q+0=0 for every species | n/a | singlet | 3bar⊗3 singlet for quarks | none | 0 (vector-like currents) | n/a | Eq.(7): √ is in the DENOMINATOR, `\frac{-\kappa_R^f g}{\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}}`; confirmed by the width Eq.(11) which carries `[1-(1/κ)^2 tan²θ_W]` to the **first** power in its denominator, and numerically: Γ(Z_R→N₁N₁)=10.18 vs 10.2 GeV, Γ(Z_R→ℓ⁺ℓ⁻)=7.63 vs 7.64 GeV, Γ(Z_R→qq̄)=82.3 GeV, total 114 GeV | self-conjugate (real couplings, real ZR) |

Per-class free-field rows: WR → LWRkin present, in LTotal. ZR → LZRkin present, in LTotal. NN → LNkin present, in LTotal.

Non-fundamental colour representations: none (all new states are colour singlets), so no `AddGaugeRepresentation` line is needed.

SelfConjugate -> True classes: `ZR`, `NN`. Both carry no `QuantumNumbers`.

Names chosen — classes `WR`, `ZR`, `NN`; members `n1,n2,n3`; parameters `kapRq, kapRl, tanW2, gWRq, gWRl, zRuL, zRuR, zRdL, zRdR, zReL, zReR, zRvL, zRnR, VCKMR, YN, XL, MNmat, MWR, WWR, MZR, WZR, MN, MN1, MN2, MN3, WN, WN1, WN2, WN3`; indices used: `Generation` only (declared by SM.fr, no `index_decls` entry needed). None is a Mathematica built-in, a FeynRules symbol, or an SM.fr name.

Single total: `LTotal` sums `LWRkin + LZRkin + LNkin + LWRq + LWRlN + LWRlnu + LZRff`.

Mass mixing (rule 8): the paper states W_R, Z_R are aligned with their mass eigenstates and N with the RH chiral states, and that SM-W interference is neglected; no mixing angle is diagonalised, so none is declared. New U(1) charges (rule 5): the effective model adds no new gauge group (`gauge_groups` empty), so there is no new U(1) charge column. EFT cutoffs (rule 2): every term is dimension 4, so no `1/Lambda^n` appears.

Reference or cached model file read: none.

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "28. 10. 2016",
    "institutions": [
      "Universite catholique de Louvain (CP3)",
      "IISER Mohali",
      "IPPP Durham University"
    ],
    "emails": [
      "olivier.mattelaer@uclouvain.be",
      "manimala@iisermohali.ac.in",
      "richard.ruiz@durham.ac.uk"
    ]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kapRq",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Overall normalisation kappa_R^q of the WR and ZR couplings to quarks, Eqs.(3) and (7)"
    },
    {
      "name": "kapRl",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "Overall normalisation kappa_R^l of the WR and ZR couplings to leptons, Eqs.(4) and (7)"
    },
    {
      "name": "tanW2",
      "parameter_type": "Internal",
      "value": "sw^2/cw^2",
      "description": "Square of the tangent of the Weinberg angle"
    },
    {
      "name": "gWRq",
      "parameter_type": "Internal",
      "value": "-kapRq*gw/Sqrt[2]",
      "interaction_order": ["NP", 1],
      "description": "WR coupling to quarks, minus kappa_R^q g over square root of two, Eq.(3)"
    },
    {
      "name": "gWRl",
      "parameter_type": "Internal",
      "value": "-kapRl*gw/Sqrt[2]",
      "interaction_order": ["NP", 1],
      "description": "WR coupling to leptons, minus kappa_R^l g over square root of two, Eq.(4)"
    },
    {
      "name": "zRuL",
      "parameter_type": "Internal",
      "value": "-kapRq*gw/Sqrt[1 - tanW2/kapRq^2]*(1/2 - 2/3)*tanW2/kapRq^2",
      "interaction_order": ["NP", 1],
      "description": "ZR left-handed coupling to up-type quarks, Eqs.(7) and (8)"
    },
    {
      "name": "zRuR",
      "parameter_type": "Internal",
      "value": "-kapRq*gw/Sqrt[1 - tanW2/kapRq^2]*(1/2 - (2/3)*tanW2/kapRq^2)",
      "interaction_order": ["NP", 1],
      "description": "ZR right-handed coupling to up-type quarks, Eqs.(7) and (9)"
    },
    {
      "name": "zRdL",
      "parameter_type": "Internal",
      "value": "-kapRq*gw/Sqrt[1 - tanW2/kapRq^2]*(-1/2 + 1/3)*tanW2/kapRq^2",
      "interaction_order": ["NP", 1],
      "description": "ZR left-handed coupling to down-type quarks, Eqs.(7) and (8)"
    },
    {
      "name": "zRdR",
      "parameter_type": "Internal",
      "value": "-kapRq*gw/Sqrt[1 - tanW2/kapRq^2]*(-1/2 + (1/3)*tanW2/kapRq^2)",
      "interaction_order": ["NP", 1],
      "description": "ZR right-handed coupling to down-type quarks, Eqs.(7) and (9)"
    },
    {
      "name": "zReL",
      "parameter_type": "Internal",
      "value": "-kapRl*gw/Sqrt[1 - tanW2/kapRl^2]*(-1/2 + 1)*tanW2/kapRl^2",
      "interaction_order": ["NP", 1],
      "description": "ZR left-handed coupling to charged leptons, Eqs.(7) and (8)"
    },
    {
      "name": "zReR",
      "parameter_type": "Internal",
      "value": "-kapRl*gw/Sqrt[1 - tanW2/kapRl^2]*(-1/2 + tanW2/kapRl^2)",
      "interaction_order": ["NP", 1],
      "description": "ZR right-handed coupling to charged leptons, Eqs.(7) and (9)"
    },
    {
      "name": "zRvL",
      "parameter_type": "Internal",
      "value": "-kapRl*gw/Sqrt[1 - tanW2/kapRl^2]*(1/2)*tanW2/kapRl^2",
      "interaction_order": ["NP", 1],
      "description": "ZR left-handed coupling to light neutrinos, Eqs.(7) and (8)"
    },
    {
      "name": "zRnR",
      "parameter_type": "Internal",
      "value": "-kapRl*gw/Sqrt[1 - tanW2/kapRl^2]*(1/2)",
      "interaction_order": ["NP", 1],
      "description": "ZR right-handed coupling to heavy Majorana neutrinos, Eqs.(7) and (9)"
    },
    {
      "name": "VCKMR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "unitary": true,
      "value_rules": [
        {"lhs": "VCKMR[1,1]", "rhs": "1"},
        {"lhs": "VCKMR[1,2]", "rhs": "0"},
        {"lhs": "VCKMR[1,3]", "rhs": "0"},
        {"lhs": "VCKMR[2,1]", "rhs": "0"},
        {"lhs": "VCKMR[2,2]", "rhs": "1"},
        {"lhs": "VCKMR[2,3]", "rhs": "0"},
        {"lhs": "VCKMR[3,1]", "rhs": "0"},
        {"lhs": "VCKMR[3,2]", "rhs": "0"},
        {"lhs": "VCKMR[3,3]", "rhs": "1"}
      ],
      "description": "Right-handed CKM matrix of Eq.(3), taken diagonal with unit entries"
    },
    {
      "name": "YN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "YN[1,1]", "rhs": "1"},
        {"lhs": "YN[1,2]", "rhs": "0"},
        {"lhs": "YN[1,3]", "rhs": "0"},
        {"lhs": "YN[2,1]", "rhs": "0"},
        {"lhs": "YN[2,2]", "rhs": "1"},
        {"lhs": "YN[2,3]", "rhs": "0"},
        {"lhs": "YN[3,1]", "rhs": "0"},
        {"lhs": "YN[3,2]", "rhs": "0"},
        {"lhs": "YN[3,3]", "rhs": "1"}
      ],
      "description": "Mixing of the heavy Majorana mass eigenstate with the right-handed chiral lepton state, Eqs.(4) and (6), diagonal with unit entries"
    },
    {
      "name": "XL",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "XL[1,1]", "rhs": "0"},
        {"lhs": "XL[1,2]", "rhs": "0"},
        {"lhs": "XL[1,3]", "rhs": "0"},
        {"lhs": "XL[2,1]", "rhs": "0"},
        {"lhs": "XL[2,2]", "rhs": "0"},
        {"lhs": "XL[2,3]", "rhs": "0"},
        {"lhs": "XL[3,1]", "rhs": "0"},
        {"lhs": "XL[3,2]", "rhs": "0"},
        {"lhs": "XL[3,3]", "rhs": "0"}
      ],
      "description": "Mixing of the light neutrino mass eigenstate with the right-handed chiral lepton state, Eqs.(4) and (6), set to zero in the benchmark"
    },
    {
      "name": "MNmat",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "MNmat[1,1]", "rhs": "MN1"},
        {"lhs": "MNmat[1,2]", "rhs": "0"},
        {"lhs": "MNmat[1,3]", "rhs": "0"},
        {"lhs": "MNmat[2,1]", "rhs": "0"},
        {"lhs": "MNmat[2,2]", "rhs": "MN2"},
        {"lhs": "MNmat[2,3]", "rhs": "0"},
        {"lhs": "MNmat[3,1]", "rhs": "0"},
        {"lhs": "MNmat[3,2]", "rhs": "0"},
        {"lhs": "MNmat[3,3]", "rhs": "MN3"}
      ],
      "description": "Diagonal Majorana mass matrix of the heavy neutrinos in GeV, Eq.(19)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "WR",
      "self_conjugate": false,
      "mass": {"sym": "MWR", "value": "3000."},
      "width": {"sym": "WWR", "value": "84.3"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9900024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "WR",
      "propagator_label": "WR",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "ZR",
      "self_conjugate": true,
      "mass": {"sym": "MZR", "value": "5070."},
      "width": {"sym": "WZR", "value": "114."},
      "quantum_numbers": {},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "ZR",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NN",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["n1", "n2", "n3"],
      "mass": {
        "sym": "MN",
        "members": [["MN1", "173.3"], ["MN2", "1.*^12"], ["MN3", "1.*^12"]]
      },
      "width": {
        "sym": "WN",
        "members": [["WN1", "2.12*^-8"], ["WN2", "1."], ["WN3", "1."]]
      },
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["HeavyNeutrino1", "HeavyNeutrino2", "HeavyNeutrino3"],
      "propagator_label": "N",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/2 FS[WRbar, mu, nu] FS[WR, mu, nu] + MWR^2 WRbar[mu] WR[mu]]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu]]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{mu}, I/2 NNbar.Ga[mu].del[NN, mu] - 1/2 NNbar.MNmat.NN]"
    },
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "Block[{mu}, gWRq uqbar.VCKMR.Ga[mu].ProjP.dq WR[mu] + HC[gWRq uqbar.VCKMR.Ga[mu].ProjP.dq WR[mu]]]"
    },
    {
      "name": "LWRlN",
      "delayed": true,
      "expression": "Block[{mu}, gWRl NNbar.YN.Ga[mu].ProjP.l WR[mu] + HC[gWRl NNbar.YN.Ga[mu].ProjP.l WR[mu]]]"
    },
    {
      "name": "LWRlnu",
      "delayed": true,
      "expression": "Block[{mu}, gWRl CC[vlbar].XL.Ga[mu].ProjP.l WR[mu] + HC[gWRl CC[vlbar].XL.Ga[mu].ProjP.l WR[mu]]]"
    },
    {
      "name": "LZRff",
      "delayed": true,
      "expression": "Block[{mu}, zRuL uqbar.Ga[mu].ProjM.uq ZR[mu] + zRuR uqbar.Ga[mu].ProjP.uq ZR[mu] + zRdL dqbar.Ga[mu].ProjM.dq ZR[mu] + zRdR dqbar.Ga[mu].ProjP.dq ZR[mu] + zReL lbar.Ga[mu].ProjM.l ZR[mu] + zReR lbar.Ga[mu].ProjP.l ZR[mu] + zRvL vlbar.Ga[mu].ProjM.vl ZR[mu] + zRnR NNbar.Ga[mu].ProjP.NN ZR[mu]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNkin + LWRq + LWRlN + LWRlnu + LZRff"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```