## Self-audit table

Fields used below: `uq/dq` (SM quark classes, Generation+Colour), `l` (SM charged lepton), `vl` (SM light neutrino), new classes `Wr` (charged heavy vector, Q=+1), `Zr` (neutral heavy vector, self-conj.), `Nh` (heavy Majorana neutrino, 3 gen, self-conj.). All bilinears below are dotted through the declared `Generation` (and `Colour`, for quarks) index with no explicit index sums, per rule 13.

| term | fields | d | coupling | coupling dim (4-d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new-U(1) | L/B sum | CC[] | frac/root check | HC partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWrkin | Wrbar,Wr (FS²/mass²) | 4 | — (kinetic) | 0 | n/a | 0 (bar/unbar cancel) | n/a | singlet (effective field, no gauge index — paper's own limitation) | singlet | n/a | 0 | n/a | n/a | self-Hermitian by construction |
| LZrkin | Zr (FS²/mass²) | 4 | — | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | n/a | self-Hermitian |
| LNkin | Nhbar,Nh | 4 | — | 0 | n/a | 0 | n/a | singlet | singlet | n/a | n/a (Majorana; L not assigned to Nh) | n/a | n/a | self-Hermitian (Majorana template) |
| LWRqq | uqbar,VCKMR,dq,Wr | 3/2+3/2+1=4 | kappaRq·gw/√2 | 0 | n/a (d≤4) | −2/3+(−1/3)+1=0 | n/a | singlet×singlet×singlet | triplet·antitriplet via `.` | n/a | B: −1/3+1/3=0 | n/a | 1/√2 from Eq.(chcurrent), matches Γ(WR→qq̄′) numerator | HC[cur] |
| LWRlN (N piece) | Nhbar,YR,Wr,lR | 3/2+3/2+1=4 | kappaRl·gw/√2 | 0 | n/a | 0+(−1)+1=0 | n/a | singlet | n/a | n/a | L: N unassigned, lR: +1 (chiral partner of l) | n/a | 1/√2, Eq. above chcurrent | HC[curN+curNu] |
| LWRlN (ν piece) | bar[CC[vl]],XR,Wr,lR | 4 | kappaRl·gw/√2 | 0 | n/a | 0 (ν neutral both legs) | n/a | singlet | n/a | n/a | ΔL=2 (CC flips L; deliberate LNV vertex, cf. Keung–Senjanovic) | **yes** (paper's `X` benchmark = 0, but term kept as CC[vl], not bare vl, per rule 3) | 1/√2 verified against same eq. as N piece | HC[curN+curNu] |
| LZRuu | uqbar,Zr,uq | 4 | kappaRq·gw/normQ | 0 | n/a | trivial 0 | n/a | singlet | triplet/antitriplet | n/a | 0 | n/a | tWSq=sw2/(1−sw2) cross-checked vs Eq.(neucurrent) denominator | self-Hermitian |
| LZRdd | dqbar,Zr,dq | 4 | kappaRq·gw/normQ | 0 | n/a | 0 | n/a | singlet | triplet/antitriplet | n/a | 0 | n/a | same | self-Hermitian |
| LZRee | lbar,Zr,l | 4 | kappaRl·gw/normL | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | same | self-Hermitian |
| LZRnn | vlbar,Zr,vl | 4 | kappaRl·gw/normL | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | same; gRnu=0 since νL has no T_R³ | self-Hermitian |
| LZRNN | Nhbar,Zr,Nh | 4 | kappaRl·gw/normL | 0 | n/a | 0 | n/a | singlet | singlet | n/a | n/a (Majorana) | n/a | same; gLN=0 since N is pure RH (T_R³=1/2, Tbl. qNumbers) | self-Hermitian (Majorana vector current is automatically axial-only) |

Kinetic+mass confirmation: Wr → LWrkin (in LTotal); Zr → LZrkin (in LTotal); Nh → LNkin (in LTotal). No non-fundamental colour representation is used (all new fields are colour singlets except SM quarks reused as-is) — no `AddGaugeRepresentation` needed.

`SelfConjugate -> True` classes: `Zr`, `Nh` — both have empty `quantum_numbers` (confirmed, no `QuantumNumbers` key emitted).

Name collision check: new classes `Wr`, `Zr`, `Nh`; new parameters `kappaRq, kappaRl, tWSq, normQ, normL, gLu, gRu, gLd, gRd, gLe, gRe, gLnu, gRnu, gLN, gRN, VCKMR, YR, XR`; auto-declared mass/width symbols `MWR, WWR, MZR, WZR, MN, WN, MN1, MN2, MN3, WN1, WN2, WN3`. None is a Mathematica built-in, a FeynRules symbol (`N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM`), or an SM.fr name (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,...`).

Single total Lagrangian: `LTotal := LWrkin + LZrkin + LNkin + LWRqq + LWRlN + LZRuu + LZRdd + LZRee + LZRnn + LZRNN` — sums every term above; no alternative total is defined.

Reference/cached model file read: **none** (only the paper's LaTeX source, the schema, and SM.fr were read, as instructed).

Note on U(1) hypercharge (rule 5): this effective model does not gauge a new U(1) or rescale the SM Higgs — `Wr`, `Zr` are introduced directly as their own mass eigenstates and `Nh` as the RH-aligned Majorana mass eigenstate, matching the paper's explicit statement that non-Abelian $W_R,Z_R$ self-interactions "are ill-defined" in this effective description. No SM hypercharge re-derivation was required.

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["heptapod-benchmark"],
    "version": "1.0",
    "date": "2026-09-17",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kappaRq",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "WR/ZR quark coupling normalization kappa_R^q, Eq.(chcurrent)"
    },
    {
      "name": "kappaRl",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRINPUTS",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "WR/ZR lepton coupling normalization kappa_R^l, Eq. above (neucurrent)"
    },
    {
      "name": "tWSq",
      "parameter_type": "Internal",
      "value": "sw2/(1-sw2)",
      "description": "tan^2(theta_W), used in Eq.(neucurrent)"
    },
    {
      "name": "normQ",
      "parameter_type": "Internal",
      "value": "Sqrt[1 - tWSq/kappaRq^2]",
      "description": "ZR neutral-current normalization for quarks, Eq.(neucurrent)"
    },
    {
      "name": "normL",
      "parameter_type": "Internal",
      "value": "Sqrt[1 - tWSq/kappaRl^2]",
      "description": "ZR neutral-current normalization for leptons/N, Eq.(neucurrent)"
    },
    {
      "name": "gLu",
      "parameter_type": "Internal",
      "value": "-(1/6) tWSq/kappaRq^2",
      "description": "ZR left-chiral coefficient for up-type quarks (Tbl. qNumbers, Eq. neucurrent)"
    },
    {
      "name": "gRu",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3) tWSq/kappaRq^2",
      "description": "ZR right-chiral coefficient for up-type quarks"
    },
    {
      "name": "gLd",
      "parameter_type": "Internal",
      "value": "-(1/6) tWSq/kappaRq^2",
      "description": "ZR left-chiral coefficient for down-type quarks"
    },
    {
      "name": "gRd",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3) tWSq/kappaRq^2",
      "description": "ZR right-chiral coefficient for down-type quarks"
    },
    {
      "name": "gLe",
      "parameter_type": "Internal",
      "value": "(1/2) tWSq/kappaRl^2",
      "description": "ZR left-chiral coefficient for charged leptons"
    },
    {
      "name": "gRe",
      "parameter_type": "Internal",
      "value": "-1/2 + tWSq/kappaRl^2",
      "description": "ZR right-chiral coefficient for charged leptons"
    },
    {
      "name": "gLnu",
      "parameter_type": "Internal",
      "value": "(1/2) tWSq/kappaRl^2",
      "description": "ZR left-chiral coefficient for light neutrinos (pure LH SM state)"
    },
    {
      "name": "gRnu",
      "parameter_type": "Internal",
      "value": "0",
      "description": "ZR right-chiral coefficient for light neutrinos (no RH partner at this vertex)"
    },
    {
      "name": "gLN",
      "parameter_type": "Internal",
      "value": "0",
      "description": "ZR left-chiral coefficient for heavy Majorana N (pure RH state)"
    },
    {
      "name": "gRN",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "ZR right-chiral coefficient for heavy Majorana N, T_R^3=1/2 (Tbl. qNumbers)"
    },
    {
      "name": "VCKMR",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "VCKMR[1,1]", "rhs": "1."}, {"lhs": "VCKMR[1,2]", "rhs": "0."}, {"lhs": "VCKMR[1,3]", "rhs": "0."},
        {"lhs": "VCKMR[2,1]", "rhs": "0."}, {"lhs": "VCKMR[2,2]", "rhs": "1."}, {"lhs": "VCKMR[2,3]", "rhs": "0."},
        {"lhs": "VCKMR[3,1]", "rhs": "0."}, {"lhs": "VCKMR[3,2]", "rhs": "0."}, {"lhs": "VCKMR[3,3]", "rhs": "1."}
      ],
      "block_name": "VCKMR",
      "description": "Right-handed CKM matrix V^CKM'_ij, diagonal unit benchmark, Eq.(chcurrent)"
    },
    {
      "name": "YR",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "YR[1,1]", "rhs": "1."}, {"lhs": "YR[1,2]", "rhs": "0."}, {"lhs": "YR[1,3]", "rhs": "0."},
        {"lhs": "YR[2,1]", "rhs": "0."}, {"lhs": "YR[2,2]", "rhs": "1."}, {"lhs": "YR[2,3]", "rhs": "0."},
        {"lhs": "YR[3,1]", "rhs": "0."}, {"lhs": "YR[3,2]", "rhs": "0."}, {"lhs": "YR[3,3]", "rhs": "1."}
      ],
      "block_name": "YRMIX",
      "description": "WR-lepton-N mixing matrix Y_{l,m'}: |Y_eN1|=|Y_muN2|=|Y_tauN3|=1, Eq.(lrsmNuMixing)"
    },
    {
      "name": "XR",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "XR[1,1]", "rhs": "0."}, {"lhs": "XR[1,2]", "rhs": "0."}, {"lhs": "XR[1,3]", "rhs": "0."},
        {"lhs": "XR[2,1]", "rhs": "0."}, {"lhs": "XR[2,2]", "rhs": "0."}, {"lhs": "XR[2,3]", "rhs": "0."},
        {"lhs": "XR[3,1]", "rhs": "0."}, {"lhs": "XR[3,2]", "rhs": "0."}, {"lhs": "XR[3,3]", "rhs": "0."}
      ],
      "block_name": "XRMIX",
      "description": "WR-lepton-nu mixing matrix X_{l,m}, set to zero benchmark, Eq.(lrsmNuMixing)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Wr",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MWR", "value": "3000."},
      "width": {"sym": "WWR", "value": "84.3"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 34,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "W_R",
      "propagator_label": "Wr",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "Zr",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MZR", "value": "5070."},
      "width": {"sym": "WZR", "value": "114."},
      "quantum_numbers": {},
      "pdg": 32,
      "particle_name": "zr",
      "full_name": "Z_R",
      "propagator_label": "Zr",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "Nh",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["n1", "n2", "n3"],
      "mass": {"sym": "MN", "members": [["MN1", "173.3"], ["MN2", "1.*^12"], ["MN3", "1.*^12"]]},
      "width": {"sym": "WN", "members": [["WN1", "2.12*^-8"], ["WN2", "1."], ["WN3", "1."]]},
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["n1", "n2", "n3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LWrkin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[ -1/2 FS[Wrbar,mu,nu] FS[Wr,mu,nu] + MWR^2 Wrbar[mu] Wr[mu] ]]"
    },
    {
      "name": "LZrkin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[ -1/4 FS[Zr,mu,nu] FS[Zr,mu,nu] + 1/2 MZR^2 Zr[mu] Zr[mu] ]]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{sp,mu,ff}, ExpandIndices[ I/2 Nhbar.Ga[mu].del[Nh,mu] - 1/2 MN[ff] Nhbar[sp,ff].Nh[sp,ff], FlavorExpand->Generation ]]"
    },
    {
      "name": "LWRqq",
      "delayed": true,
      "expression": "Block[{mu, cur}, cur = -(kappaRq*gw/Sqrt[2]) uqbar.VCKMR.Ga[mu].ProjP.dq Wr[mu]; ExpandIndices[cur + HC[cur], FlavorExpand->Generation]]"
    },
    {
      "name": "LWRlN",
      "delayed": true,
      "expression": "Block[{mu, curN, curNu}, curN = -(kappaRl*gw/Sqrt[2]) Nhbar.YR.Ga[mu].ProjP.lR Wr[mu]; curNu = -(kappaRl*gw/Sqrt[2]) bar[CC[vl]].XR.Ga[mu].ProjP.lR Wr[mu]; ExpandIndices[curN + curNu + HC[curN + curNu], FlavorExpand->Generation]]"
    },
    {
      "name": "LZRuu",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[ -(kappaRq*gw/normQ) uqbar.Ga[mu].(gLu*ProjM + gRu*ProjP).uq Zr[mu], FlavorExpand->Generation ]]"
    },
    {
      "name": "LZRdd",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[ -(kappaRq*gw/normQ) dqbar.Ga[mu].(gLd*ProjM + gRd*ProjP).dq Zr[mu], FlavorExpand->Generation ]]"
    },
    {
      "name": "LZRee",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[ -(kappaRl*gw/normL) lbar.Ga[mu].(gLe*ProjM + gRe*ProjP).l Zr[mu], FlavorExpand->Generation ]]"
    },
    {
      "name": "LZRnn",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[ -(kappaRl*gw/normL) vlbar.Ga[mu].(gLnu*ProjM + gRnu*ProjP).vl Zr[mu], FlavorExpand->Generation ]]"
    },
    {
      "name": "LZRNN",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[ -(kappaRl*gw/normL) Nhbar.Ga[mu].(gLN*ProjM + gRN*ProjP).Nh Zr[mu], FlavorExpand->Generation ]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LWrkin + LZrkin + LNkin + LWRqq + LWRlN + LZRuu + LZRdd + LZRee + LZRnn + LZRNN"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```