## Mandatory self-audit table

Model: EffLRSM (arXiv:1610.08985). New states: `WRp` (complex vector, Q=+1), `ZR` (real vector), `NR` = {n1,n2,n3} (Majorana fermions). No new scalars — the paper explicitly decouples the LRSM Higgs sector (Sec. II B).

| term | fields in monomial | d | coupling symbol | coupling dim (=4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new-U(1) charge sum | L/B sum | CC[] where paper writes psi^c | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin | `FS[WRpbar]FS[WRp]` ; `WRpbar[mu] WRp[mu]` | 4 ; 2 | `-1/2` ; `MWR^2` | 0 ; 2 | n/a | -1+1=0 | n/a (physical basis) | n/a | singlet | none declared | 0 | n/a | n/a | self-Hermitian (bar+field) |
| LZRkin | `FS[ZR]FS[ZR]` ; `ZR[mu] ZR[mu]` | 4 ; 2 | `-1/4` ; `1/2 MZR^2` | 0 ; 2 | n/a | 0 | n/a | n/a | singlet | none declared | 0 | n/a | n/a | real field, Hermitian |
| LNkin | `NRbar.Ga[mu].del[NR,mu]` ; `NRbar.MNmat.NR` | 4 ; 3 | `I/2` ; `MNmat` | 0 ; 1 | n/a | 0 | n/a | n/a | singlet | none declared | Majorana mass, dL=2 by construction (Eq. 2) | n/a | n/a | Majorana, `-1/2 M psibar.psi` |
| LWRq | `WRp[mu] uqbar VCKMR dq` | 4 | `gWRq VCKMR` | 0 | n/a | +1-2/3-1/3=0 | n/a | n/a | 3bar (x) 3 singlet, implicit Colour | none declared | B: -1/3+1/3=0 | n/a | Eq.(11)-(12): reproduces G(WR->qq')=25.4, G(WR->tb)=25.2 GeV (Tbl. II) | `HC[...]` |
| LWRl (Y) | `WRp[mu] NRbar VYN l` | 4 | `gWRl VYN` | 0 | n/a | +1+0-1=0 | n/a | n/a | singlet | none declared | dL=1 (Majorana N, intended LNV) | n/a | Eq.(13): reproduces G(WR->l N1)=8.41 GeV (Tbl. II) | `HC[...]` |
| LWRl (X) | `WRp[mu] CC[vlbar] VXL l` | 4 | `gWRl VXL` (=0, Eq. 7) | 0 | n/a | +1+0-1=0 | n/a | n/a | singlet | none declared | dL=1 | yes — `CC[vlbar]` for the paper's `nu^c_m` bar | n/a | `HC[...]` |
| LZR | `ZR[mu] fbar Ga[mu] Proj f`, f = uq, dq, l, vl, NR | 4 | `gZRq`/`gZRl` x `gZRuL,gZRuR,gZRdL,gZRdR,gZReL,gZReR,gZRvL,gZRnR` | 0 | n/a | 0 for every f | n/a | n/a | quark rows: implicit Colour singlet | none declared | 0 (N Majorana: L not assigned) | see below | Hermitian (neutral current, real couplings) |

Fraction/root resolution for Eq. (8)-(10) (no LaTeX source in the sandbox, so cross-checked against a second equation, per rule 7):
- Eq. (8) prefactor is **divided** by the radical: `kR g / Sqrt[1 - tan^2(thetaW)/kR^2]`, not multiplied. Cross-check: Eq. (14) puts `[1 - (1/kR)^2 tan^2 thetaW]` in the **denominator** of the width, and width ~ coupling^2.
- Eq. (9) is `(T3L - Q) (1/kR^2) tan^2 thetaW` (the big paren binds T3L-Q); Eq. (10) is `T3R - (1/kR^2) tan^2 thetaW Q`.
- Numerical confirmation with Tbl. II (MZR=5070, k=1, sin^2 thetaW=0.23126, aEM=1/127.94): light quarks 82.25 (paper 82.3), tt 11.29 (11.3), l+l- 7.64 (7.64), nu nu 2.77 (2.78), N1N1 10.21 (10.2), total 114.2 (114). All five channels match, so both placements are fixed.

Other required lines:
- SelfConjugate -> True classes: `ZR`, `NR`. Both carry **no** QuantumNumbers. Confirmed.
- Non-fundamental colour representations: none in this model, so no `AddGaugeRepresentation[...]` line is needed.
- New U(1): the add-on declares **no** gauge group. The paper's SU(2)_R x U(1)_(B-L) is broken and only the mass eigenstates WR, ZR survive; their mixing with the hypercharge direction is already absorbed into the `tan^2(thetaW)/kR^2` terms of Eqs. (8)-(10). So no new U(1) charge is put on any SM field, and no charge-table sign choice is needed. Light-heavy neutrino mixing (Eqs. 5-7) is implemented as the matrices `VYN`, `VXL`, not as a comment.
- Names chosen: `WRp, ZR, NR, n1, n2, n3, kqR, klR, tw2, gWRq, gWRl, gZRq, gZRl, gZRuL, gZRuR, gZRdL, gZRdR, gZReL, gZReR, gZRvL, gZRnR, VCKMR, VYN, VXL, MNmat, MWR, MZR, MN, MN1, MN2, MN3, WWR, WZR, WN, WN1, WN2, WN3`. None is a Mathematica built-in, a FeynRules symbol, or an SM.fr name; no primes or punctuation in ParticleName.
- Single total: `LTotal` sums `LWRkin + LZRkin + LNkin + LWRq + LWRl + LZR`. Every other term appears once; no pure-constant term.
- Reference or cached model file read: **none**. Files read: the paper text, `frmodel.py`, `render.py`, and `SM.fr` (the base SM file, as instructed).

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "27. 10. 2016",
    "institutions": [
      "Universite catholique de Louvain (CP3)",
      "IISER Mohali",
      "IPPP, Durham University"
    ]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kqR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSM",
      "order_block": 1,
      "tex": "\\kappa^q_R",
      "description": "Overall normalization of the WR and ZR coupling strength to quarks, Eqs.(4),(8); benchmark kappa^q_R = 1, Eq.(20)"
    },
    {
      "name": "klR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSM",
      "order_block": 2,
      "tex": "\\kappa^l_R",
      "description": "Overall normalization of the WR and ZR coupling strength to leptons, Eqs.(5),(8); benchmark kappa^l_R = 1, Eq.(20)"
    },
    {
      "name": "tw2",
      "parameter_type": "Internal",
      "value": "sw^2/cw^2",
      "description": "tan^2(theta_W), appears in the ZR couplings of Eqs.(8)-(10)"
    },
    {
      "name": "gWRq",
      "parameter_type": "Internal",
      "value": "kqR*gw/Sqrt[2]",
      "interaction_order": ["NP", 1],
      "description": "WR coupling strength to quarks, kappa^q_R g / Sqrt[2], Eq.(4)"
    },
    {
      "name": "gWRl",
      "parameter_type": "Internal",
      "value": "klR*gw/Sqrt[2]",
      "interaction_order": ["NP", 1],
      "description": "WR coupling strength to leptons, kappa^l_R g / Sqrt[2], Eq.(5)"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kqR*gw/Sqrt[1 - tw2/kqR^2]",
      "interaction_order": ["NP", 1],
      "description": "ZR overall coupling to quarks, kappa^q_R g / Sqrt[1 - (1/kappa^q_R)^2 tan^2 thetaW], Eq.(8); radical in the denominator, fixed by the denominator of Eq.(14) and by the widths of Tbl. II"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "klR*gw/Sqrt[1 - tw2/klR^2]",
      "interaction_order": ["NP", 1],
      "description": "ZR overall coupling to leptons, kappa^l_R g / Sqrt[1 - (1/kappa^l_R)^2 tan^2 thetaW], Eq.(8)"
    },
    {
      "name": "gZRuL",
      "parameter_type": "Internal",
      "value": "(1/2 - 2/3)*tw2/kqR^2",
      "description": "Left chiral ZR coefficient for up-type quarks, (T3L - Q)(1/kappa^2) tan^2 thetaW, Eq.(9) with Tbl. I"
    },
    {
      "name": "gZRuR",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3)*tw2/kqR^2",
      "description": "Right chiral ZR coefficient for up-type quarks, T3R - (1/kappa^2) tan^2 thetaW Q, Eq.(10) with Tbl. I"
    },
    {
      "name": "gZRdL",
      "parameter_type": "Internal",
      "value": "(-1/2 + 1/3)*tw2/kqR^2",
      "description": "Left chiral ZR coefficient for down-type quarks, Eq.(9) with Tbl. I"
    },
    {
      "name": "gZRdR",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3)*tw2/kqR^2",
      "description": "Right chiral ZR coefficient for down-type quarks, Eq.(10) with Tbl. I"
    },
    {
      "name": "gZReL",
      "parameter_type": "Internal",
      "value": "(-1/2 + 1)*tw2/klR^2",
      "description": "Left chiral ZR coefficient for charged leptons, Eq.(9) with Tbl. I"
    },
    {
      "name": "gZReR",
      "parameter_type": "Internal",
      "value": "-1/2 + tw2/klR^2",
      "description": "Right chiral ZR coefficient for charged leptons, Eq.(10) with Tbl. I"
    },
    {
      "name": "gZRvL",
      "parameter_type": "Internal",
      "value": "(1/2)*tw2/klR^2",
      "description": "Left chiral ZR coefficient for the light SM neutrinos, Eq.(9) with Tbl. I"
    },
    {
      "name": "gZRnR",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "Right chiral ZR coefficient for the heavy Majorana neutrinos, T3R = +1/2 and Q = 0, Eq.(10) with Tbl. I"
    },
    {
      "name": "VCKMR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
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
      "tex": "V^{CKM\\prime}",
      "description": "Right-handed CKM matrix V^CKM' of Eq.(4); taken diagonal with unit entries (Sec. II)"
    },
    {
      "name": "VYN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "VYN[1,1]", "rhs": "1"},
        {"lhs": "VYN[1,2]", "rhs": "0"},
        {"lhs": "VYN[1,3]", "rhs": "0"},
        {"lhs": "VYN[2,1]", "rhs": "0"},
        {"lhs": "VYN[2,2]", "rhs": "1"},
        {"lhs": "VYN[2,3]", "rhs": "0"},
        {"lhs": "VYN[3,1]", "rhs": "0"},
        {"lhs": "VYN[3,2]", "rhs": "0"},
        {"lhs": "VYN[3,3]", "rhs": "1"}
      ],
      "tex": "Y",
      "description": "Heavy neutrino mixing, VYN[m,l] = Y_{l m} of Eq.(5); diagonal with unit entries, |YeN1| = |YmuN2| = |YtauN3| = 1, Eq.(7)"
    },
    {
      "name": "VXL",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "VXL[1,1]", "rhs": "0"},
        {"lhs": "VXL[1,2]", "rhs": "0"},
        {"lhs": "VXL[1,3]", "rhs": "0"},
        {"lhs": "VXL[2,1]", "rhs": "0"},
        {"lhs": "VXL[2,2]", "rhs": "0"},
        {"lhs": "VXL[2,3]", "rhs": "0"},
        {"lhs": "VXL[3,1]", "rhs": "0"},
        {"lhs": "VXL[3,2]", "rhs": "0"},
        {"lhs": "VXL[3,3]", "rhs": "0"}
      ],
      "tex": "X",
      "description": "Light neutrino mixing, VXL[m,l] = X_{l m} of Eq.(5); set to zero at TeV collider scales, Eq.(7)"
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
      "description": "Diagonal Majorana mass matrix of the heavy neutrinos [GeV], Eq.(19); used in the free-field mass term so no explicit generation index appears in the Lagrangian"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "WRp",
      "self_conjugate": false,
      "mass": {"sym": "MWR", "value": "3000."},
      "width": {"sym": "WWR", "value": "84.3"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 34,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "Right-handed W boson",
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
      "pdg": 32,
      "particle_name": "zr",
      "full_name": "Right-handed Z boson",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NR",
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
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy neutrino 1", "Heavy neutrino 2", "Heavy neutrino 3"],
      "propagator_label": ["NR", "n1", "n2", "n3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/2 FS[WRpbar, mu, nu] FS[WRp, mu, nu] + MWR^2 WRpbar[mu] WRp[mu]]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu]]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{mu}, I/2 NRbar.Ga[mu].del[NR, mu] - 1/2 NRbar.MNmat.NR]"
    },
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "Block[{mu, lag}, lag = -gWRq WRp[mu] uqbar.VCKMR.Ga[mu].ProjP.dq; lag + HC[lag]]"
    },
    {
      "name": "LWRl",
      "delayed": true,
      "expression": "Block[{mu, lag}, lag = -gWRl WRp[mu] (NRbar.VYN.Ga[mu].ProjP.l + CC[vlbar].VXL.Ga[mu].ProjP.l); lag + HC[lag]]"
    },
    {
      "name": "LZR",
      "delayed": true,
      "expression": "Block[{mu}, -gZRq ZR[mu] (gZRuL uqbar.Ga[mu].ProjM.uq + gZRuR uqbar.Ga[mu].ProjP.uq + gZRdL dqbar.Ga[mu].ProjM.dq + gZRdR dqbar.Ga[mu].ProjP.dq) - gZRl ZR[mu] (gZReL lbar.Ga[mu].ProjM.l + gZReR lbar.Ga[mu].ProjP.l + gZRvL vlbar.Ga[mu].ProjM.vl + gZRnR NRbar.Ga[mu].ProjP.NR)]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNkin + LWRq + LWRl + LZR"
    }
  ]
}
```