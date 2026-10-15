I'll start by reading the paper and the schema.
I read the paper (arXiv:1610.08985) and the schema/renderer. No cached or reference `.fr` file for this model exists in the sandbox, and none was read — only `SM.fr` (the base model, as instructed).

## Physics summary

New states (Sec. II): `W_R^±` and `Z_R` gauge bosons, aligned with their mass eigenstates, and **three** heavy Majorana neutrinos `N_1,2,3` aligned with the RH chiral states. No new scalars: the LRSM Higgs sector is explicitly decoupled (Sec. II B), so no `Δ_L,R` triplets and no new gauge groups — SU(2)_R ⊗ U(1)_{B−L} is *not* gauged here; the currents of Eqs. (4)–(8) are written directly for the mass eigenstates.

New-U(1) charges: **none to derive.** The effective model gauges nothing new, so no field gets a new U(1) charge, and no `SelfConjugate -> True` class carries `QuantumNumbers`. Only `WR` carries `Q -> 1`. `Z_R` chiral charges are internal parameters derived from Eqs. (9)–(10) with Q = T3L + T3R + (B−L)/2, and the Eq. (8) prefactor is `κ g / Sqrt[1 − tan²θW/κ²]` (the OCR lost the fraction bar; the denominator is fixed by the width Eq. (14), where `[1 − (1/κ)² tan²θW]` sits in the denominator, and by the standard LRSM derivation).

## Self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin (kinetic) | FS[WRbar]·FS[WR] | 4 | 1 | 0 | n/a | −1+1=0 | n/a (physical field) | singlet | singlet | n/a (none gauged) | 0 | n/a | self-conjugate pair |
| LWRkin (mass) | WRbar·WR | 2 | MWR² | 2 (GeV²) | n/a | −1+1=0 | n/a | singlet | singlet | n/a | 0 | n/a | self-conjugate pair |
| LZRkin (kinetic) | FS[ZR]·FS[ZR] | 4 | 1 | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | real field |
| LZRkin (mass) | ZR·ZR | 2 | MZR²/2 | 2 (GeV²) | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | real field |
| LNkin (kinetic) | NRbar·Ga·del[NR] | 4 | I/2 | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | Majorana (`SelfConjugate -> True`) | self-conjugate |
| LNkin (mass) | NRbar·NR | 3 | MN[ff]/2 | 1 (GeV) | n/a | 0 | n/a | singlet | singlet | n/a | ΔL=2 allowed (Majorana, paper Eq. 2) | self-conjugate |
| LWRq, Eq.(4) | uqbar·Ga·ProjP·dq · WR | 4 | kqR·gw·CKMR/√2 | 0 | n/a | −2/3−1/3+1=0 | n/a | singlet (mass eigenstates) | `cc` shared 3⊗3̄ | n/a | 0 | n/a | `HC[lag]` |
| LWRl, Eq.(5) N-part | NRbar·Ga·ProjP·l · WR | 4 | klR·gw·Ymix/√2 | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | n/a | ΔL=1 (Majorana N carries no L) | `HC[lag]` |
| LWRl, Eq.(5) ν-part | bar[CC[vl]]·Ga·ProjP·l · WR | 4 | klR·gw·Xmix/√2 | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | n/a | 1+(−1)... ν^c carries L=−1, so ΔL=0 | **yes** — `bar[CC[vl[ff2]]]` for ν^c | `HC[lag]` |
| LZRff, Eq.(8) quarks | uqbar·Ga·(gL PL+gR PR)·uq · ZR (idem dq) | 4 | gZRq·gZR{L,R}{u,d} | 0 | n/a | −2/3+2/3+0=0 | n/a | singlet | `cc` shared 3⊗3̄ | n/a | 0 | n/a | real couplings → self-conjugate |
| LZRff, Eq.(8) leptons | lbar/vlbar/NRbar·Ga·(…)·(l/vl/NR) · ZR | 4 | gZRl·gZR{L,R}{e,v,N} | 0 | n/a | +1−1+0=0 | n/a | singlet | singlet | n/a | 0 (N term: axial Majorana current) | real couplings → self-conjugate |

Kinetic + mass confirmation, one row per new class: **WR** → LWRkin (in sum); **ZR** → LZRkin (in sum); **NR (N1,N2,N3)** → LNkin (in sum). All three appear in `LEffLRSM`.

`SelfConjugate -> True` classes: `ZR`, `NR`. Neither carries `QuantumNumbers`. ✔

No EFT `1/Λ^n` operator appears in this model (every term is d = 4 or lower), so no cutoff parameter is needed and no dimensionful O(0.1) coefficient exists.

Reference/cached model file read: **none**.

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "31. 10. 2016",
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
      "name": "kqR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 1,
      "tex": "\\kappa^q_R",
      "description": "Overall normalization of the WR/ZR coupling strength to quarks, Eqs.(4),(8)"
    },
    {
      "name": "klR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 2,
      "tex": "\\kappa^l_R",
      "description": "Overall normalization of the WR/ZR coupling strength to leptons, Eqs.(5),(8)"
    },
    {
      "name": "CKMR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "unitary": true,
      "value_rules": [
        {"lhs": "CKMR[1,1]", "rhs": "1"},
        {"lhs": "CKMR[1,2]", "rhs": "0"},
        {"lhs": "CKMR[1,3]", "rhs": "0"},
        {"lhs": "CKMR[2,1]", "rhs": "0"},
        {"lhs": "CKMR[2,2]", "rhs": "1"},
        {"lhs": "CKMR[2,3]", "rhs": "0"},
        {"lhs": "CKMR[3,1]", "rhs": "0"},
        {"lhs": "CKMR[3,2]", "rhs": "0"},
        {"lhs": "CKMR[3,3]", "rhs": "1"}
      ],
      "tex": "V^{CKM'}",
      "description": "Right-handed CKM matrix of Eq.(4); taken diagonal with unit entries"
    },
    {
      "name": "Ymix",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "LRSMMIXN",
      "value_rules": [
        {"lhs": "Ymix[1,1]", "rhs": "1."},
        {"lhs": "Ymix[1,2]", "rhs": "0."},
        {"lhs": "Ymix[1,3]", "rhs": "0."},
        {"lhs": "Ymix[2,1]", "rhs": "0."},
        {"lhs": "Ymix[2,2]", "rhs": "1."},
        {"lhs": "Ymix[2,3]", "rhs": "0."},
        {"lhs": "Ymix[3,1]", "rhs": "0."},
        {"lhs": "Ymix[3,2]", "rhs": "0."},
        {"lhs": "Ymix[3,3]", "rhs": "1."}
      ],
      "tex": "Y_{l m'}",
      "description": "Mixing of heavy neutrino mass eigenstate Nm' with the RH chiral state of flavour l, Eqs.(5),(7); diagonal with unit entries"
    },
    {
      "name": "Xmix",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "LRSMMIXV",
      "value_rules": [
        {"lhs": "Xmix[1,1]", "rhs": "0."},
        {"lhs": "Xmix[1,2]", "rhs": "0."},
        {"lhs": "Xmix[1,3]", "rhs": "0."},
        {"lhs": "Xmix[2,1]", "rhs": "0."},
        {"lhs": "Xmix[2,2]", "rhs": "0."},
        {"lhs": "Xmix[2,3]", "rhs": "0."},
        {"lhs": "Xmix[3,1]", "rhs": "0."},
        {"lhs": "Xmix[3,2]", "rhs": "0."},
        {"lhs": "Xmix[3,3]", "rhs": "0."}
      ],
      "tex": "X_{l m}",
      "description": "Mixing of light neutrino mass eigenstate with the RH chiral state, Eqs.(5),(6); set to zero in the benchmark of Eq.(7)"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kqR gw/Sqrt[1 - sw^2/(cw^2 kqR^2)]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to quarks, prefactor of Eq.(8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "klR gw/Sqrt[1 - sw^2/(cw^2 klR^2)]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to leptons, prefactor of Eq.(8)"
    },
    {
      "name": "gZRLu",
      "parameter_type": "Internal",
      "value": "-(1/6) sw^2/(cw^2 kqR^2)",
      "description": "ZR left-chiral coefficient of up-type quarks, Eq.(9): (T3L-Q) tan^2(thetaW)/kqR^2"
    },
    {
      "name": "gZRRu",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3) sw^2/(cw^2 kqR^2)",
      "description": "ZR right-chiral coefficient of up-type quarks, Eq.(10): T3R - Q tan^2(thetaW)/kqR^2"
    },
    {
      "name": "gZRLd",
      "parameter_type": "Internal",
      "value": "-(1/6) sw^2/(cw^2 kqR^2)",
      "description": "ZR left-chiral coefficient of down-type quarks, Eq.(9)"
    },
    {
      "name": "gZRRd",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3) sw^2/(cw^2 kqR^2)",
      "description": "ZR right-chiral coefficient of down-type quarks, Eq.(10)"
    },
    {
      "name": "gZRLe",
      "parameter_type": "Internal",
      "value": "(1/2) sw^2/(cw^2 klR^2)",
      "description": "ZR left-chiral coefficient of charged leptons, Eq.(9)"
    },
    {
      "name": "gZRRe",
      "parameter_type": "Internal",
      "value": "-1/2 + sw^2/(cw^2 klR^2)",
      "description": "ZR right-chiral coefficient of charged leptons, Eq.(10)"
    },
    {
      "name": "gZRLv",
      "parameter_type": "Internal",
      "value": "(1/2) sw^2/(cw^2 klR^2)",
      "description": "ZR left-chiral coefficient of light neutrinos, Eq.(9)"
    },
    {
      "name": "gZRRN",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "ZR right-chiral coefficient of heavy Majorana neutrinos, Eq.(10): T3R = +1/2, Q = 0"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 20,
      "class_name": "WR",
      "self_conjugate": false,
      "mass": {"sym": "MWR", "value": "3000."},
      "width": {"sym": "WWR", "value": "84.3"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9900024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "Right-handed charged gauge boson WR",
      "propagator_label": "WR",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 21,
      "class_name": "ZR",
      "self_conjugate": true,
      "mass": {"sym": "MZR", "value": "5070."},
      "width": {"sym": "WZR", "value": "114."},
      "quantum_numbers": {},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "Right-handed neutral gauge boson ZR",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 20,
      "class_name": "NR",
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
      "expression": "Block[{mu, nu}, ExpandIndices[-1/2 FS[WRbar, mu, nu] FS[WR, mu, nu] + MWR^2 WRbar[mu] WR[mu]]]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, ExpandIndices[-1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu]]]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{mu, ff}, ExpandIndices[I/2 NRbar[ff].Ga[mu].del[NR[ff], mu] - 1/2 MN[ff] NRbar[ff].NR[ff], FlavorExpand -> Generation]]"
    },
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "Block[{mu, ff1, ff2, cc, lag}, lag = -kqR gw/Sqrt[2] CKMR[ff1, ff2] WR[mu] (uqbar[ff1, cc].Ga[mu].ProjP.dq[ff2, cc]); ExpandIndices[lag + HC[lag], FlavorExpand -> Generation]]"
    },
    {
      "name": "LWRl",
      "delayed": true,
      "expression": "Block[{mu, ff1, ff2, lag}, lag = -klR gw/Sqrt[2] WR[mu] (Xmix[ff1, ff2] (bar[CC[vl[ff2]]].Ga[mu].ProjP.l[ff1]) + Ymix[ff1, ff2] (NRbar[ff2].Ga[mu].ProjP.l[ff1])); ExpandIndices[lag + HC[lag], FlavorExpand -> Generation]]"
    },
    {
      "name": "LZRff",
      "delayed": true,
      "expression": "Block[{mu, ff, cc}, ExpandIndices[-ZR[mu] (gZRq (uqbar[ff, cc].Ga[mu].(gZRLu ProjM + gZRRu ProjP).uq[ff, cc] + dqbar[ff, cc].Ga[mu].(gZRLd ProjM + gZRRd ProjP).dq[ff, cc]) + gZRl (lbar[ff].Ga[mu].(gZRLe ProjM + gZRRe ProjP).l[ff] + gZRLv vlbar[ff].Ga[mu].ProjM.vl[ff] + gZRRN NRbar[ff].Ga[mu].ProjP.NR[ff])), FlavorExpand -> Generation]]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNkin + LWRq + LWRl + LZRff"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LEffLRSM"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper (arXiv:1610.08985) and the schema/renderer. No cached or reference `.fr` file for this model exists in the sandbox, and none was read — only `SM.fr` (the base model, as instructed).

## Physics summary

New states (Sec. II): `W_R^±` and `Z_R` gauge bosons, aligned with their mass eigenstates, and **three** heavy Majorana neutrinos `N_1,2,3` aligned with the RH chiral states. No new scalars: the LRSM Higgs sector is explicitly decoupled (Sec. II B), so no `Δ_L,R` triplets and no new gauge groups — SU(2)_R ⊗ U(1)_{B−L} is *not* gauged here; the currents of Eqs. (4)–(8) are written directly for the mass eigenstates.

New-U(1) charges: **none to derive.** The effective model gauges nothing new, so no field gets a new U(1) charge, and no `SelfConjugate -> True` class carries `QuantumNumbers`. Only `WR` carries `Q -> 1`. `Z_R` chiral charges are internal parameters derived from Eqs. (9)–(10) with Q = T3L + T3R + (B−L)/2, and the Eq. (8) prefactor is `κ g / Sqrt[1 − tan²θW/κ²]` (the OCR lost the fraction bar; the denominator is fixed by the width Eq. (14), where `[1 − (1/κ)² tan²θW]` sits in the denominator, and by the standard LRSM derivation).

## Self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin (kinetic) | FS[WRbar]·FS[WR] | 4 | 1 | 0 | n/a | −1+1=0 | n/a (physical field) | singlet | singlet | n/a (none gauged) | 0 | n/a | self-conjugate pair |
| LWRkin (mass) | WRbar·WR | 2 | MWR² | 2 (GeV²) | n/a | −1+1=0 | n/a | singlet | singlet | n/a | 0 | n/a | self-conjugate pair |
| LZRkin (kinetic) | FS[ZR]·FS[ZR] | 4 | 1 | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | real field |
| LZRkin (mass) | ZR·ZR | 2 | MZR²/2 | 2 (GeV²) | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | real field |
| LNkin (kinetic) | NRbar·Ga·del[NR] | 4 | I/2 | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | Majorana (`SelfConjugate -> True`) | self-conjugate |
| LNkin (mass) | NRbar·NR | 3 | MN[ff]/2 | 1 (GeV) | n/a | 0 | n/a | singlet | singlet | n/a | ΔL=2 allowed (Majorana, paper Eq. 2) | self-conjugate |
| LWRq, Eq.(4) | uqbar·Ga·ProjP·dq · WR | 4 | kqR·gw·CKMR/√2 | 0 | n/a | −2/3−1/3+1=0 | n/a | singlet (mass eigenstates) | `cc` shared 3⊗3̄ | n/a | 0 | n/a | `HC[lag]` |
| LWRl, Eq.(5) N-part | NRbar·Ga·ProjP·l · WR | 4 | klR·gw·Ymix/√2 | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | n/a | ΔL=1 (Majorana N carries no L) | `HC[lag]` |
| LWRl, Eq.(5) ν-part | bar[CC[vl]]·Ga·ProjP·l · WR | 4 | klR·gw·Xmix/√2 | 0 | n/a | 0−1+1=0 | n/a | singlet | singlet | n/a | 1+(−1)... ν^c carries L=−1, so ΔL=0 | **yes** — `bar[CC[vl[ff2]]]` for ν^c | `HC[lag]` |
| LZRff, Eq.(8) quarks | uqbar·Ga·(gL PL+gR PR)·uq · ZR (idem dq) | 4 | gZRq·gZR{L,R}{u,d} | 0 | n/a | −2/3+2/3+0=0 | n/a | singlet | `cc` shared 3⊗3̄ | n/a | 0 | n/a | real couplings → self-conjugate |
| LZRff, Eq.(8) leptons | lbar/vlbar/NRbar·Ga·(…)·(l/vl/NR) · ZR | 4 | gZRl·gZR{L,R}{e,v,N} | 0 | n/a | +1−1+0=0 | n/a | singlet | singlet | n/a | 0 (N term: axial Majorana current) | real couplings → self-conjugate |

Kinetic + mass confirmation, one row per new class: **WR** → LWRkin (in sum); **ZR** → LZRkin (in sum); **NR (N1,N2,N3)** → LNkin (in sum). All three appear in `LEffLRSM`.

`SelfConjugate -> True` classes: `ZR`, `NR`. Neither carries `QuantumNumbers`. ✔

No EFT `1/Λ^n` operator appears in this model (every term is d = 4 or lower), so no cutoff parameter is needed and no dimensionful O(0.1) coefficient exists.

Reference/cached model file read: **none**.

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "31. 10. 2016",
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
      "name": "kqR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 1,
      "tex": "\\kappa^q_R",
      "description": "Overall normalization of the WR/ZR coupling strength to quarks, Eqs.(4),(8)"
    },
    {
      "name": "klR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 2,
      "tex": "\\kappa^l_R",
      "description": "Overall normalization of the WR/ZR coupling strength to leptons, Eqs.(5),(8)"
    },
    {
      "name": "CKMR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "unitary": true,
      "value_rules": [
        {"lhs": "CKMR[1,1]", "rhs": "1"},
        {"lhs": "CKMR[1,2]", "rhs": "0"},
        {"lhs": "CKMR[1,3]", "rhs": "0"},
        {"lhs": "CKMR[2,1]", "rhs": "0"},
        {"lhs": "CKMR[2,2]", "rhs": "1"},
        {"lhs": "CKMR[2,3]", "rhs": "0"},
        {"lhs": "CKMR[3,1]", "rhs": "0"},
        {"lhs": "CKMR[3,2]", "rhs": "0"},
        {"lhs": "CKMR[3,3]", "rhs": "1"}
      ],
      "tex": "V^{CKM'}",
      "description": "Right-handed CKM matrix of Eq.(4); taken diagonal with unit entries"
    },
    {
      "name": "Ymix",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "LRSMMIXN",
      "value_rules": [
        {"lhs": "Ymix[1,1]", "rhs": "1."},
        {"lhs": "Ymix[1,2]", "rhs": "0."},
        {"lhs": "Ymix[1,3]", "rhs": "0."},
        {"lhs": "Ymix[2,1]", "rhs": "0."},
        {"lhs": "Ymix[2,2]", "rhs": "1."},
        {"lhs": "Ymix[2,3]", "rhs": "0."},
        {"lhs": "Ymix[3,1]", "rhs": "0."},
        {"lhs": "Ymix[3,2]", "rhs": "0."},
        {"lhs": "Ymix[3,3]", "rhs": "1."}
      ],
      "tex": "Y_{l m'}",
      "description": "Mixing of heavy neutrino mass eigenstate Nm' with the RH chiral state of flavour l, Eqs.(5),(7); diagonal with unit entries"
    },
    {
      "name": "Xmix",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "LRSMMIXV",
      "value_rules": [
        {"lhs": "Xmix[1,1]", "rhs": "0."},
        {"lhs": "Xmix[1,2]", "rhs": "0."},
        {"lhs": "Xmix[1,3]", "rhs": "0."},
        {"lhs": "Xmix[2,1]", "rhs": "0."},
        {"lhs": "Xmix[2,2]", "rhs": "0."},
        {"lhs": "Xmix[2,3]", "rhs": "0."},
        {"lhs": "Xmix[3,1]", "rhs": "0."},
        {"lhs": "Xmix[3,2]", "rhs": "0."},
        {"lhs": "Xmix[3,3]", "rhs": "0."}
      ],
      "tex": "X_{l m}",
      "description": "Mixing of light neutrino mass eigenstate with the RH chiral state, Eqs.(5),(6); set to zero in the benchmark of Eq.(7)"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kqR gw/Sqrt[1 - sw^2/(cw^2 kqR^2)]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to quarks, prefactor of Eq.(8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "klR gw/Sqrt[1 - sw^2/(cw^2 klR^2)]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to leptons, prefactor of Eq.(8)"
    },
    {
      "name": "gZRLu",
      "parameter_type": "Internal",
      "value": "-(1/6) sw^2/(cw^2 kqR^2)",
      "description": "ZR left-chiral coefficient of up-type quarks, Eq.(9): (T3L-Q) tan^2(thetaW)/kqR^2"
    },
    {
      "name": "gZRRu",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3) sw^2/(cw^2 kqR^2)",
      "description": "ZR right-chiral coefficient of up-type quarks, Eq.(10): T3R - Q tan^2(thetaW)/kqR^2"
    },
    {
      "name": "gZRLd",
      "parameter_type": "Internal",
      "value": "-(1/6) sw^2/(cw^2 kqR^2)",
      "description": "ZR left-chiral coefficient of down-type quarks, Eq.(9)"
    },
    {
      "name": "gZRRd",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3) sw^2/(cw^2 kqR^2)",
      "description": "ZR right-chiral coefficient of down-type quarks, Eq.(10)"
    },
    {
      "name": "gZRLe",
      "parameter_type": "Internal",
      "value": "(1/2) sw^2/(cw^2 klR^2)",
      "description": "ZR left-chiral coefficient of charged leptons, Eq.(9)"
    },
    {
      "name": "gZRRe",
      "parameter_type": "Internal",
      "value": "-1/2 + sw^2/(cw^2 klR^2)",
      "description": "ZR right-chiral coefficient of charged leptons, Eq.(10)"
    },
    {
      "name": "gZRLv",
      "parameter_type": "Internal",
      "value": "(1/2) sw^2/(cw^2 klR^2)",
      "description": "ZR left-chiral coefficient of light neutrinos, Eq.(9)"
    },
    {
      "name": "gZRRN",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "ZR right-chiral coefficient of heavy Majorana neutrinos, Eq.(10): T3R = +1/2, Q = 0"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 20,
      "class_name": "WR",
      "self_conjugate": false,
      "mass": {"sym": "MWR", "value": "3000."},
      "width": {"sym": "WWR", "value": "84.3"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9900024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "Right-handed charged gauge boson WR",
      "propagator_label": "WR",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 21,
      "class_name": "ZR",
      "self_conjugate": true,
      "mass": {"sym": "MZR", "value": "5070."},
      "width": {"sym": "WZR", "value": "114."},
      "quantum_numbers": {},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "Right-handed neutral gauge boson ZR",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 20,
      "class_name": "NR",
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
      "expression": "Block[{mu, nu}, ExpandIndices[-1/2 FS[WRbar, mu, nu] FS[WR, mu, nu] + MWR^2 WRbar[mu] WR[mu]]]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, ExpandIndices[-1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu]]]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{mu, ff}, ExpandIndices[I/2 NRbar[ff].Ga[mu].del[NR[ff], mu] - 1/2 MN[ff] NRbar[ff].NR[ff], FlavorExpand -> Generation]]"
    },
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "Block[{mu, ff1, ff2, cc, lag}, lag = -kqR gw/Sqrt[2] CKMR[ff1, ff2] WR[mu] (uqbar[ff1, cc].Ga[mu].ProjP.dq[ff2, cc]); ExpandIndices[lag + HC[lag], FlavorExpand -> Generation]]"
    },
    {
      "name": "LWRl",
      "delayed": true,
      "expression": "Block[{mu, ff1, ff2, lag}, lag = -klR gw/Sqrt[2] WR[mu] (Xmix[ff1, ff2] (bar[CC[vl[ff2]]].Ga[mu].ProjP.l[ff1]) + Ymix[ff1, ff2] (NRbar[ff2].Ga[mu].ProjP.l[ff1])); ExpandIndices[lag + HC[lag], FlavorExpand -> Generation]]"
    },
    {
      "name": "LZRff",
      "delayed": true,
      "expression": "Block[{mu, ff, cc}, ExpandIndices[-ZR[mu] (gZRq (uqbar[ff, cc].Ga[mu].(gZRLu ProjM + gZRRu ProjP).uq[ff, cc] + dqbar[ff, cc].Ga[mu].(gZRLd ProjM + gZRRd ProjP).dq[ff, cc]) + gZRl (lbar[ff].Ga[mu].(gZRLe ProjM + gZRRe ProjP).l[ff] + gZRLv vlbar[ff].Ga[mu].ProjM.vl[ff] + gZRRN NRbar[ff].Ga[mu].ProjP.NR[ff])), FlavorExpand -> Generation]]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNkin + LWRq + LWRl + LZRff"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LEffLRSM"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```