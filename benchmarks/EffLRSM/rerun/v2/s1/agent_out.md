I'll start by reading the paper and the schema files.
I read the paper, the schema, the renderer, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox and none was opened.

## Model content found in the paper

**New states:** `WR` (complex vector, Q=+1, M=3 TeV, Γ=84.3 GeV), `ZR` (real vector, M=5070 GeV, Γ=114 GeV), and three heavy **Majorana** neutrinos `N1,N2,N3` (colour/SU(2) singlets, Q=0, m = 173.3, 10¹², 10¹² GeV; Γ(N1)=2.12×10⁻⁸ GeV). PDG ids follow the paper's own `cuts.f`, which uses 9900012 for the heavy neutrino.

**New parameters:** `kQR`, `kLR` (Eqs. 4,5,8), RH CKM `VCKMR`, heavy/light neutrino mixing `YN`, `XN` (Eqs. 5–7), and the derived ZR chiral coefficients of Eqs. (8)–(10).

**ZR normalisation:** the OCR of Eq. (8) splits a fraction. The width formula Eq. (14), which divides by `[1 − (1/κ)² tan²θW]`, fixes the coupling as `κ g / Sqrt[1 − tan²θW/κ²]`. Re-deriving the SU(2)_R⊗U(1)_(B−L) → U(1)_Y mixing gives coupling `S[T3R + (tan²θW/κ²)(T3L − Q)]`, which reproduces Eqs. (9) and (10) chirality by chirality.

## Self-audit table

Fermion mass dim 3/2, vector 1, `FS` 2, `del`/`DC` 1. There are **no `1/Λⁿ` operators in this paper** — the word "effective" refers to dropping the LRSM scalar sector, not to higher-dimensional operators. Every term below is dimension 4, so no EFT cutoff parameter is declared. There is **no new gauged U(1)**: SU(2)_R⊗U(1)_(B−L) is broken and only the mass eigenstates WR, ZR appear, so the "new U(1) sum" column is n/a for every row. Y is not a declared quantum number of the physical SM fields in `SM.fr` (only Q), so the Y column is n/a; Q is checked instead.

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L/B sum | CC[] | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin | FS[WRbar]FS[WR]; WRbar·WR | 4 | 1; MWR² | 0; 2 (=4−2) | n/a | −1+1=0 | n/a | singlet | singlet | n/a | 0 | n/a | self-conj. |
| LZRkin | FS[ZR]FS[ZR]; ZR·ZR | 4 | 1; MZR² | 0; 2 (=4−2) | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | self-conj. |
| LNkin | Nbar γ ∂ N; Nbar N | 4 | 1; MN[ff] | 0; 1 (=4−3) | n/a | 0 | n/a | singlet | singlet | n/a | Majorana (L not conserved by mass) | n/a (Majorana class) | self-conj. |
| LWRqq | uqbar dq WR | 4 | kQR gw VCKMR | 0 | n/a | −2/3−1/3+1=0 | n/a | singlet (mass basis) | shared `cc` on uqbar/dq | n/a | B: −1/3+1/3=0 | n/a | HC[LWRqq] |
| LWRlN | Nbar l WR | 4 | kLR gw YN | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | n/a | L: 0+1 ⇒ ΔL=1 (Majorana N, Eq. 2) | n/a | HC[LWRlN] |
| LWRlv | bar[CC[vl]] l WR | 4 | kLR gw XN | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | n/a | L: −1+1=0 | **yes** (paper writes ν^c_m, Eq. 5) | HC[LWRlv] |
| LZRu | uqbar uq ZR | 4 | gZRq·(gZRuL,gZRuR) | 0 | n/a | −2/3+2/3+0=0 | n/a | singlet | shared `cc` | n/a | 0 | n/a | self-hermitian (real NC) |
| LZRd | dqbar dq ZR | 4 | gZRq·(gZRdL,gZRdR) | 0 | n/a | 1/3−1/3=0 | n/a | singlet | shared `cc` | n/a | 0 | n/a | self-hermitian |
| LZRl | lbar l ZR | 4 | gZRl·(gZRlL,gZRlR) | 0 | n/a | +1−1=0 | n/a | singlet | singlet | n/a | 0 | n/a | self-hermitian |
| LZRv | vlbar vl ZR | 4 | gZRl gZRvL | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | self-hermitian |
| LZRN | Nbar N ZR | 4 | gZRl gZRNR | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | self-hermitian |

Free-field coverage: `WR` → LWRkin, `ZR` → LZRkin, `N` → LNkin; all three are in the total sum `LEffLRSM`.

`SelfConjugate -> True` classes: `ZR` and `N`. Both carry **no** `QuantumNumbers`.

Reference or cached model file read: **none** (only the paper text, the schema, the renderer, and `SM.fr`).

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "27. 10. 2016",
    "institutions": ["Universite catholique de Louvain (CP3)", "IISER Mohali", "IPPP, Durham University"],
    "emails": ["olivier.mattelaer@uclouvain.be", "manimala@iisermohali.ac.in", "richard.ruiz@durham.ac.uk"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kQR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 1,
      "tex": "\\kappa^q_R",
      "description": "Overall normalization of the right-handed gauge coupling to quarks, kappa_R^q, Eqs.(4),(8)"
    },
    {
      "name": "kLR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 2,
      "tex": "\\kappa^\\ell_R",
      "description": "Overall normalization of the right-handed gauge coupling to leptons, kappa_R^l, Eqs.(5),(8)"
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
      "tex": "V^{CKM'}",
      "description": "Right-handed CKM matrix V^{CKM'}_{ij} of Eq.(4); taken diagonal with unit entries (diagonalCKM restriction)"
    },
    {
      "name": "YN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "YN[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "YN[1,1]", "rhs": "1"},
        {"lhs": "YN[2,2]", "rhs": "1"},
        {"lhs": "YN[3,3]", "rhs": "1"}
      ],
      "tex": "Y_{\\ell m'}",
      "description": "Mixing between the heavy Majorana mass eigenstate N_m' and the RH chiral state of lepton flavour l, Eq.(5); diagonal with unit entries, Eq.(7)"
    },
    {
      "name": "XN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "XN[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "XN[1,1]", "rhs": "0"},
        {"lhs": "XN[2,2]", "rhs": "0"},
        {"lhs": "XN[3,3]", "rhs": "0"}
      ],
      "tex": "X_{\\ell m}",
      "description": "Mixing between the light neutrino mass eigenstate nu_m and the RH chiral state of lepton flavour l, Eq.(5); set to zero at collider scales, Eqs.(6),(7)"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kQR gw/Sqrt[1 - (sw/cw)^2/kQR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to quarks, kappa_R^q g / Sqrt[1 - tan^2(thetaW)/kappa_R^q^2], Eq.(8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "kLR gw/Sqrt[1 - (sw/cw)^2/kLR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to leptons, kappa_R^l g / Sqrt[1 - tan^2(thetaW)/kappa_R^l^2], Eq.(8)"
    },
    {
      "name": "gZRuL",
      "parameter_type": "Internal",
      "value": "-(1/6) (sw/cw)^2/kQR^2",
      "description": "LH ZR chiral coefficient for up-type quarks, (T3L - Q) tan^2(thetaW)/kappa^2, Eq.(9), Tbl.I"
    },
    {
      "name": "gZRuR",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3) (sw/cw)^2/kQR^2",
      "description": "RH ZR chiral coefficient for up-type quarks, T3R - Q tan^2(thetaW)/kappa^2, Eq.(10), Tbl.I"
    },
    {
      "name": "gZRdL",
      "parameter_type": "Internal",
      "value": "-(1/6) (sw/cw)^2/kQR^2",
      "description": "LH ZR chiral coefficient for down-type quarks, Eq.(9), Tbl.I"
    },
    {
      "name": "gZRdR",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3) (sw/cw)^2/kQR^2",
      "description": "RH ZR chiral coefficient for down-type quarks, Eq.(10), Tbl.I"
    },
    {
      "name": "gZRlL",
      "parameter_type": "Internal",
      "value": "(1/2) (sw/cw)^2/kLR^2",
      "description": "LH ZR chiral coefficient for charged leptons, Eq.(9), Tbl.I"
    },
    {
      "name": "gZRlR",
      "parameter_type": "Internal",
      "value": "-1/2 + (sw/cw)^2/kLR^2",
      "description": "RH ZR chiral coefficient for charged leptons, Eq.(10), Tbl.I"
    },
    {
      "name": "gZRvL",
      "parameter_type": "Internal",
      "value": "(1/2) (sw/cw)^2/kLR^2",
      "description": "LH ZR chiral coefficient for light neutrinos, Eq.(9), Tbl.I"
    },
    {
      "name": "gZRNR",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "RH ZR chiral coefficient for the heavy Majorana neutrinos, T3R(NR) = +1/2 and Q = 0, Eq.(10), Tbl.I"
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
      "quantum_numbers": {},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "Right-handed Z boson",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "N",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MN",
        "members": [["MN1", "173.3"], ["MN2", "1.*^12"], ["MN3", "1.*^12"]]
      },
      "width": {
        "sym": "WN",
        "members": [["WN1", "2.12*^-8"], ["WN2", "0."], ["WN3", "0."]]
      },
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LWRkin",
      "delayed": true,
      "expression": "-1/2 FS[WRbar, mu, nu] FS[WR, mu, nu] + MWR^2 WRbar[mu] WR[mu]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "-1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "I/2 Nbar[sp1, ff].Ga[mu, sp1, sp2].del[N[sp2, ff], mu] - 1/2 MN[ff] Nbar[sp1, ff].N[sp1, ff]"
    },
    {
      "name": "LWRqq",
      "delayed": true,
      "expression": "-kQR gw/Sqrt[2] VCKMR[ff1, ff2] uqbar[sp1, ff1, cc].Ga[mu, sp1, sp2].ProjP[sp2, sp3].dq[sp3, ff2, cc] WR[mu]"
    },
    {
      "name": "LWRlN",
      "delayed": true,
      "expression": "-kLR gw/Sqrt[2] YN[ff1, ff2] Nbar[sp1, ff2].Ga[mu, sp1, sp2].ProjP[sp2, sp3].l[sp3, ff1] WR[mu]"
    },
    {
      "name": "LWRlv",
      "delayed": true,
      "expression": "-kLR gw/Sqrt[2] XN[ff1, ff2] bar[CC[vl[sp1, ff2]]].Ga[mu, sp1, sp2].ProjP[sp2, sp3].l[sp3, ff1] WR[mu]"
    },
    {
      "name": "LZRu",
      "delayed": true,
      "expression": "-gZRq uqbar[sp1, ff, cc].Ga[mu, sp1, sp2].(gZRuL ProjM[sp2, sp3] + gZRuR ProjP[sp2, sp3]).uq[sp3, ff, cc] ZR[mu]"
    },
    {
      "name": "LZRd",
      "delayed": true,
      "expression": "-gZRq dqbar[sp1, ff, cc].Ga[mu, sp1, sp2].(gZRdL ProjM[sp2, sp3] + gZRdR ProjP[sp2, sp3]).dq[sp3, ff, cc] ZR[mu]"
    },
    {
      "name": "LZRl",
      "delayed": true,
      "expression": "-gZRl lbar[sp1, ff].Ga[mu, sp1, sp2].(gZRlL ProjM[sp2, sp3] + gZRlR ProjP[sp2, sp3]).l[sp3, ff] ZR[mu]"
    },
    {
      "name": "LZRv",
      "delayed": true,
      "expression": "-gZRl gZRvL vlbar[sp1, ff].Ga[mu, sp1, sp2].ProjM[sp2, sp3].vl[sp3, ff] ZR[mu]"
    },
    {
      "name": "LZRN",
      "delayed": true,
      "expression": "-gZRl gZRNR Nbar[sp1, ff].Ga[mu, sp1, sp2].ProjP[sp2, sp3].N[sp3, ff] ZR[mu]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNkin + (LWRqq + HC[LWRqq]) + (LWRlN + HC[LWRlN]) + (LWRlv + HC[LWRlv]) + LZRu + LZRd + LZRl + LZRv + LZRN"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper, the schema, the renderer, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox and none was opened.

## Model content found in the paper

**New states:** `WR` (complex vector, Q=+1, M=3 TeV, Γ=84.3 GeV), `ZR` (real vector, M=5070 GeV, Γ=114 GeV), and three heavy **Majorana** neutrinos `N1,N2,N3` (colour/SU(2) singlets, Q=0, m = 173.3, 10¹², 10¹² GeV; Γ(N1)=2.12×10⁻⁸ GeV). PDG ids follow the paper's own `cuts.f`, which uses 9900012 for the heavy neutrino.

**New parameters:** `kQR`, `kLR` (Eqs. 4,5,8), RH CKM `VCKMR`, heavy/light neutrino mixing `YN`, `XN` (Eqs. 5–7), and the derived ZR chiral coefficients of Eqs. (8)–(10).

**ZR normalisation:** the OCR of Eq. (8) splits a fraction. The width formula Eq. (14), which divides by `[1 − (1/κ)² tan²θW]`, fixes the coupling as `κ g / Sqrt[1 − tan²θW/κ²]`. Re-deriving the SU(2)_R⊗U(1)_(B−L) → U(1)_Y mixing gives coupling `S[T3R + (tan²θW/κ²)(T3L − Q)]`, which reproduces Eqs. (9) and (10) chirality by chirality.

## Self-audit table

Fermion mass dim 3/2, vector 1, `FS` 2, `del`/`DC` 1. There are **no `1/Λⁿ` operators in this paper** — the word "effective" refers to dropping the LRSM scalar sector, not to higher-dimensional operators. Every term below is dimension 4, so no EFT cutoff parameter is declared. There is **no new gauged U(1)**: SU(2)_R⊗U(1)_(B−L) is broken and only the mass eigenstates WR, ZR appear, so the "new U(1) sum" column is n/a for every row. Y is not a declared quantum number of the physical SM fields in `SM.fr` (only Q), so the Y column is n/a; Q is checked instead.

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L/B sum | CC[] | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin | FS[WRbar]FS[WR]; WRbar·WR | 4 | 1; MWR² | 0; 2 (=4−2) | n/a | −1+1=0 | n/a | singlet | singlet | n/a | 0 | n/a | self-conj. |
| LZRkin | FS[ZR]FS[ZR]; ZR·ZR | 4 | 1; MZR² | 0; 2 (=4−2) | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | self-conj. |
| LNkin | Nbar γ ∂ N; Nbar N | 4 | 1; MN[ff] | 0; 1 (=4−3) | n/a | 0 | n/a | singlet | singlet | n/a | Majorana (L not conserved by mass) | n/a (Majorana class) | self-conj. |
| LWRqq | uqbar dq WR | 4 | kQR gw VCKMR | 0 | n/a | −2/3−1/3+1=0 | n/a | singlet (mass basis) | shared `cc` on uqbar/dq | n/a | B: −1/3+1/3=0 | n/a | HC[LWRqq] |
| LWRlN | Nbar l WR | 4 | kLR gw YN | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | n/a | L: 0+1 ⇒ ΔL=1 (Majorana N, Eq. 2) | n/a | HC[LWRlN] |
| LWRlv | bar[CC[vl]] l WR | 4 | kLR gw XN | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | n/a | L: −1+1=0 | **yes** (paper writes ν^c_m, Eq. 5) | HC[LWRlv] |
| LZRu | uqbar uq ZR | 4 | gZRq·(gZRuL,gZRuR) | 0 | n/a | −2/3+2/3+0=0 | n/a | singlet | shared `cc` | n/a | 0 | n/a | self-hermitian (real NC) |
| LZRd | dqbar dq ZR | 4 | gZRq·(gZRdL,gZRdR) | 0 | n/a | 1/3−1/3=0 | n/a | singlet | shared `cc` | n/a | 0 | n/a | self-hermitian |
| LZRl | lbar l ZR | 4 | gZRl·(gZRlL,gZRlR) | 0 | n/a | +1−1=0 | n/a | singlet | singlet | n/a | 0 | n/a | self-hermitian |
| LZRv | vlbar vl ZR | 4 | gZRl gZRvL | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | self-hermitian |
| LZRN | Nbar N ZR | 4 | gZRl gZRNR | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | self-hermitian |

Free-field coverage: `WR` → LWRkin, `ZR` → LZRkin, `N` → LNkin; all three are in the total sum `LEffLRSM`.

`SelfConjugate -> True` classes: `ZR` and `N`. Both carry **no** `QuantumNumbers`.

Reference or cached model file read: **none** (only the paper text, the schema, the renderer, and `SM.fr`).

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "27. 10. 2016",
    "institutions": ["Universite catholique de Louvain (CP3)", "IISER Mohali", "IPPP, Durham University"],
    "emails": ["olivier.mattelaer@uclouvain.be", "manimala@iisermohali.ac.in", "richard.ruiz@durham.ac.uk"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kQR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 1,
      "tex": "\\kappa^q_R",
      "description": "Overall normalization of the right-handed gauge coupling to quarks, kappa_R^q, Eqs.(4),(8)"
    },
    {
      "name": "kLR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 2,
      "tex": "\\kappa^\\ell_R",
      "description": "Overall normalization of the right-handed gauge coupling to leptons, kappa_R^l, Eqs.(5),(8)"
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
      "tex": "V^{CKM'}",
      "description": "Right-handed CKM matrix V^{CKM'}_{ij} of Eq.(4); taken diagonal with unit entries (diagonalCKM restriction)"
    },
    {
      "name": "YN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "YN[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "YN[1,1]", "rhs": "1"},
        {"lhs": "YN[2,2]", "rhs": "1"},
        {"lhs": "YN[3,3]", "rhs": "1"}
      ],
      "tex": "Y_{\\ell m'}",
      "description": "Mixing between the heavy Majorana mass eigenstate N_m' and the RH chiral state of lepton flavour l, Eq.(5); diagonal with unit entries, Eq.(7)"
    },
    {
      "name": "XN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "XN[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "XN[1,1]", "rhs": "0"},
        {"lhs": "XN[2,2]", "rhs": "0"},
        {"lhs": "XN[3,3]", "rhs": "0"}
      ],
      "tex": "X_{\\ell m}",
      "description": "Mixing between the light neutrino mass eigenstate nu_m and the RH chiral state of lepton flavour l, Eq.(5); set to zero at collider scales, Eqs.(6),(7)"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kQR gw/Sqrt[1 - (sw/cw)^2/kQR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to quarks, kappa_R^q g / Sqrt[1 - tan^2(thetaW)/kappa_R^q^2], Eq.(8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "kLR gw/Sqrt[1 - (sw/cw)^2/kLR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to leptons, kappa_R^l g / Sqrt[1 - tan^2(thetaW)/kappa_R^l^2], Eq.(8)"
    },
    {
      "name": "gZRuL",
      "parameter_type": "Internal",
      "value": "-(1/6) (sw/cw)^2/kQR^2",
      "description": "LH ZR chiral coefficient for up-type quarks, (T3L - Q) tan^2(thetaW)/kappa^2, Eq.(9), Tbl.I"
    },
    {
      "name": "gZRuR",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3) (sw/cw)^2/kQR^2",
      "description": "RH ZR chiral coefficient for up-type quarks, T3R - Q tan^2(thetaW)/kappa^2, Eq.(10), Tbl.I"
    },
    {
      "name": "gZRdL",
      "parameter_type": "Internal",
      "value": "-(1/6) (sw/cw)^2/kQR^2",
      "description": "LH ZR chiral coefficient for down-type quarks, Eq.(9), Tbl.I"
    },
    {
      "name": "gZRdR",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3) (sw/cw)^2/kQR^2",
      "description": "RH ZR chiral coefficient for down-type quarks, Eq.(10), Tbl.I"
    },
    {
      "name": "gZRlL",
      "parameter_type": "Internal",
      "value": "(1/2) (sw/cw)^2/kLR^2",
      "description": "LH ZR chiral coefficient for charged leptons, Eq.(9), Tbl.I"
    },
    {
      "name": "gZRlR",
      "parameter_type": "Internal",
      "value": "-1/2 + (sw/cw)^2/kLR^2",
      "description": "RH ZR chiral coefficient for charged leptons, Eq.(10), Tbl.I"
    },
    {
      "name": "gZRvL",
      "parameter_type": "Internal",
      "value": "(1/2) (sw/cw)^2/kLR^2",
      "description": "LH ZR chiral coefficient for light neutrinos, Eq.(9), Tbl.I"
    },
    {
      "name": "gZRNR",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "RH ZR chiral coefficient for the heavy Majorana neutrinos, T3R(NR) = +1/2 and Q = 0, Eq.(10), Tbl.I"
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
      "quantum_numbers": {},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "Right-handed Z boson",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "N",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MN",
        "members": [["MN1", "173.3"], ["MN2", "1.*^12"], ["MN3", "1.*^12"]]
      },
      "width": {
        "sym": "WN",
        "members": [["WN1", "2.12*^-8"], ["WN2", "0."], ["WN3", "0."]]
      },
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LWRkin",
      "delayed": true,
      "expression": "-1/2 FS[WRbar, mu, nu] FS[WR, mu, nu] + MWR^2 WRbar[mu] WR[mu]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "-1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "I/2 Nbar[sp1, ff].Ga[mu, sp1, sp2].del[N[sp2, ff], mu] - 1/2 MN[ff] Nbar[sp1, ff].N[sp1, ff]"
    },
    {
      "name": "LWRqq",
      "delayed": true,
      "expression": "-kQR gw/Sqrt[2] VCKMR[ff1, ff2] uqbar[sp1, ff1, cc].Ga[mu, sp1, sp2].ProjP[sp2, sp3].dq[sp3, ff2, cc] WR[mu]"
    },
    {
      "name": "LWRlN",
      "delayed": true,
      "expression": "-kLR gw/Sqrt[2] YN[ff1, ff2] Nbar[sp1, ff2].Ga[mu, sp1, sp2].ProjP[sp2, sp3].l[sp3, ff1] WR[mu]"
    },
    {
      "name": "LWRlv",
      "delayed": true,
      "expression": "-kLR gw/Sqrt[2] XN[ff1, ff2] bar[CC[vl[sp1, ff2]]].Ga[mu, sp1, sp2].ProjP[sp2, sp3].l[sp3, ff1] WR[mu]"
    },
    {
      "name": "LZRu",
      "delayed": true,
      "expression": "-gZRq uqbar[sp1, ff, cc].Ga[mu, sp1, sp2].(gZRuL ProjM[sp2, sp3] + gZRuR ProjP[sp2, sp3]).uq[sp3, ff, cc] ZR[mu]"
    },
    {
      "name": "LZRd",
      "delayed": true,
      "expression": "-gZRq dqbar[sp1, ff, cc].Ga[mu, sp1, sp2].(gZRdL ProjM[sp2, sp3] + gZRdR ProjP[sp2, sp3]).dq[sp3, ff, cc] ZR[mu]"
    },
    {
      "name": "LZRl",
      "delayed": true,
      "expression": "-gZRl lbar[sp1, ff].Ga[mu, sp1, sp2].(gZRlL ProjM[sp2, sp3] + gZRlR ProjP[sp2, sp3]).l[sp3, ff] ZR[mu]"
    },
    {
      "name": "LZRv",
      "delayed": true,
      "expression": "-gZRl gZRvL vlbar[sp1, ff].Ga[mu, sp1, sp2].ProjM[sp2, sp3].vl[sp3, ff] ZR[mu]"
    },
    {
      "name": "LZRN",
      "delayed": true,
      "expression": "-gZRl gZRNR Nbar[sp1, ff].Ga[mu, sp1, sp2].ProjP[sp2, sp3].N[sp3, ff] ZR[mu]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNkin + (LWRqq + HC[LWRqq]) + (LWRlN + HC[LWRlN]) + (LWRlv + HC[LWRlv]) + LZRu + LZRd + LZRl + LZRv + LZRN"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```