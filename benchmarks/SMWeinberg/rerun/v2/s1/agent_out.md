I'll start by reading the paper and the schema.
I read the paper, the schema, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content

The paper extends the SM by **one** new state: an *unphysical* Majorana neutrino `N` (colour singlet, SU(2) singlet, Q = 0, Y = 0) that models the LN-violating `(ν_ℓ ν^c_ℓ')` current of the d = 5 Weinberg operator. Its interactions are Eq. (23)–(29). The 1/Λ suppression enters through the internal mass `mN = |ΣC5| v²/Λ` (Eq. 9).

One deviation from the generic rule set, stated up front: I give `Lambda` and `Cll` **no** `InteractionOrder`. The paper's own MadGraph5 syntax is `QED=4 QCD=0` for `p p > mu+ mu+ j j`, which counts 2 `Wqq` plus 2 `WℓN` vertices and zero QED order on the mass insertion. `{QED,-1}` on `Lambda` would force `QED=5` and contradict the paper.

## Self-audit table

Field dims: S 1, V 1, F 3/2, `del` 1. `Q` uses SM.fr charges (W⁺=+1, GP=+1, ℓ⁻=−1, ℓ^c=+1 so `bar[CC[l]]`=−1, N=0, ν=0). All terms are written after EWSB in the mass-eigenstate basis, so `Y` is not a symmetry of the individual monomials (Y sum = n/a); electroweak invariance is guaranteed by construction from Eqs. (18)–(22). There is no new U(1) and no new colour/SU(2) index.

| term | fields | d | coupling | coupling dim (=4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) | new U(1) | L sum | CC[] used | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNkin (kin) | `Nbar`,`del N` | 4 | 1 | 0 | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | self-conjugate |
| LNkin (mass) | `Nbar`,`N` | 3 | `mN` | 1 | n/a (mN∝1/Λ) | 0 | n/a | singlet | singlet | none | ΔL=2 (Majorana) | n/a | self-conjugate |
| LNW, Eq.(23) | `W`,`Nbar`,`l` | 4 | `gw/Sqrt[2]` | 0 | n/a | +1+0−1=0 | n/a | mass basis, singlet | singlet | none | ΔL=1 (N has no L) | no | `HC[LNint]` |
| LNZ, Eq.(24) | `Z`,`Nbar`,`vl` | 4 | `gw/(2cw)` | 0 | n/a | 0 | n/a | mass basis, singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNH, Eq.(25) h | `H`,`Nbar`,`vl` | 4 | `gw mN/(2MW)` | 0 | absorbed in `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNH, Eq.(25) hh | `H`,`H`,`Nbar`,`vl` | 5 | `gw^2 mN/(8MW^2)` | −1 | 1/Λ¹ via `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNGP, Eq.(26) G⁺ | `GP`,`Nbar`,`l` / `GP`,`bar[CC[l]]`,`N` | 4 | `gw mN/(2Sqrt[2]MW)` | 0 | absorbed in `mN` | +1+0−1=0 / +1−1+0=0 | n/a | singlet | singlet | none | ΔL=1 | **yes** | `HC[LNint]` |
| LNGP, Eq.(26) G⁺h | `GP`,`H`,`Nbar`,`l` / +`bar[CC[l]]`,`N` | 5 | `gw^2 mN/(4Sqrt[2]MW^2)` | −1 | 1/Λ¹ via `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | **yes** | `HC[LNint]` |
| LNG0, Eq.(27) G⁰ | `G0`,`Nbar`,`vl` | 4 | `gw mN/(2MW)` | 0 | absorbed in `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNG0, Eq.(27) G⁰h | `G0`,`H`,`Nbar`,`vl` | 5 | `gw^2 mN/(4MW^2)` | −1 | 1/Λ¹ via `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNGG, Eq.(28) G⁺G⁺ | `GP`,`GP`,`bar[CC[l]]`,`l` | 5 | `gw^2 mN/(4MW^2)` | −1 | 1/Λ¹ via `mN` | +1+1−1−1=0 | n/a | singlet | singlet | none | ΔL=2 | **yes** | `HC[LNint]` |
| LNGG, Eq.(28) G⁰G⁰ | `G0`,`G0`,`Nbar`,`vl` | 5 | `gw^2 mN/(8MW^2)` | −1 | 1/Λ¹ via `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNG0GP, Eq.(29) | `G0`,`GP`,`Nbar`,`l` / +`bar[CC[l]]`,`N` | 5 | `gw^2 mN/(4Sqrt[2]MW^2)` | −1 | 1/Λ¹ via `mN` | 0 / 0 | n/a | singlet | singlet | none | ΔL=1 | **yes** | `HC[LNint]` |

Kinetic + mass check: the only new class is `F[100] == N`; its kinetic and mass term is `LNkin`, and `LNkin` is in the total sum `LTotal := LSM + LNP`.

`SelfConjugate -> True` classes: `N` only. It carries **no** `QuantumNumbers`.

Reference / cached model file read: **none**.

Every dimension-5 row carries `1/Λ` through the internal parameter `mN == Abs[ΣC5] vev^2/Lambda` (Eq. 9), with `Lambda` declared External in GeV at the paper benchmark 200 TeV and `Cll` kept dimensionless at the benchmark `C5 = δ_ℓμ δ_ℓ'μ`.

```json
{
  "model_name": "SMWeinberg_gen",
  "info": {
    "authors": [
      "B. Fuks",
      "J. Neundorf",
      "K. Peters",
      "R. Ruiz",
      "M. Saimpert"
    ],
    "version": "1.0",
    "date": "15. 06. 2021",
    "institutions": [
      "LPTHE, Sorbonne Universite / CNRS",
      "DESY Hamburg",
      "Institute of Nuclear Physics PAN, Cracow",
      "CP3, Universite catholique de Louvain",
      "CERN"
    ],
    "emails": [
      "fuks@lpthe.jussieu.fr",
      "jonas.neundorf@desy.de",
      "krisztian.peters@desy.de",
      "rruiz@ifj.edu.pl",
      "matthias.saimpert@cern.ch"
    ]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Lambda",
      "parameter_type": "External",
      "value": "200000.",
      "block_name": "NUPHYSICS",
      "order_block": 1,
      "tex": "\\[CapitalLambda]",
      "description": "EFT cutoff [GeV] of the d=5 Weinberg operator, Eq.(2); benchmark Lambda = 200 TeV. The operator coefficient is C5/Lambda, mass dimension -1."
    },
    {
      "name": "Cll",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "Cll[1,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[1,2]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[1,3]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[2,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[2,2]",
          "rhs": "1.",
          "delayed": false
        },
        {
          "lhs": "Cll[2,3]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[3,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[3,2]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[3,3]",
          "rhs": "0.",
          "delayed": false
        }
      ],
      "block_name": "NUPHYSICS",
      "tex": "Subscript[C,5]",
      "description": "Flavour-dependent dimensionless Wilson coefficient C5^{ll'} of the Weinberg operator, Eq.(2). Symmetric in its two Generation indices, so only the six entries (ee, emu, etau, mumu, mutau, tautau) are independent (Les Houches counters 2-7). Benchmark C5^{ll'} = delta_{l mu} delta_{l' mu}."
    },
    {
      "name": "mN",
      "parameter_type": "Internal",
      "value": "Abs[Cll[1,1] + Cll[1,2] + Cll[1,3] + Cll[2,2] + Cll[2,3] + Cll[3,3]] vev^2/Lambda",
      "tex": "Subscript[m,N]",
      "description": "Mass [GeV] of the unphysical Majorana neutrino N, Eq.(9): mN = |Cee + Cemu + Cetau + Cmumu + Cmutau + Ctautau| v^2/Lambda. It carries the whole 1/Lambda suppression of the d=5 operator."
    },
    {
      "name": "wN",
      "parameter_type": "Internal",
      "value": "0.",
      "tex": "Subscript[\\[CapitalGamma],N]",
      "description": "Width [GeV] of the unphysical Majorana neutrino N. N models the off-shell (nu_l nu^c_l') current of Eq.(6)-(7) and never goes on shell, so its width is set to zero."
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "N",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "mN",
        "value": "Internal",
        "members": []
      },
      "width": {
        "massless": false,
        "sym": "wN",
        "value": "Internal",
        "members": []
      },
      "quantum_numbers": {},
      "pdg": 9900012,
      "particle_name": "n1",
      "full_name": "Unphysical Majorana neutrino",
      "propagator_label": "N",
      "propagator_type": "S",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LNkin",
      "expression": "Block[{mu1}, I/2 Nbar.Ga[mu1].del[N, mu1] - 1/2 mN Nbar.N]",
      "delayed": true
    },
    {
      "name": "LNW",
      "expression": "Block[{mu1}, -gw/Sqrt[2] W[mu1] (Nbar.Ga[mu1].ProjM.e + Nbar.Ga[mu1].ProjM.mu + Nbar.Ga[mu1].ProjM.ta)]",
      "delayed": true
    },
    {
      "name": "LNZ",
      "expression": "Block[{mu1}, -gw/(2 cw) Z[mu1] (Nbar.Ga[mu1].ProjM.ve + Nbar.Ga[mu1].ProjM.vm + Nbar.Ga[mu1].ProjM.vt)]",
      "delayed": true
    },
    {
      "name": "LNH",
      "expression": "-gw mN/(2 MW) H (1 + gw/(4 MW) H) (Nbar.ProjM.ve + Nbar.ProjM.vm + Nbar.ProjM.vt)",
      "delayed": true
    },
    {
      "name": "LNGP",
      "expression": "Block[{feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; (-I gw mN/(2 Sqrt[2] MW) GP (1 + gw/(2 MW) H) (Nbar.ProjM.e + Nbar.ProjM.mu + Nbar.ProjM.ta + bar[CC[e]].ProjM.N + bar[CC[mu]].ProjM.N + bar[CC[ta]].ProjM.N)) /. feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LNG0",
      "expression": "Block[{feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; (-I gw mN/(2 MW) G0 (1 + gw/(2 MW) H) (Nbar.ProjM.ve + Nbar.ProjM.vm + Nbar.ProjM.vt)) /. feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LNGG",
      "expression": "Block[{feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; (gw^2 mN/(8 MW^2) (2 GP GP (bar[CC[e]].ProjM.e + bar[CC[e]].ProjM.mu + bar[CC[e]].ProjM.ta + bar[CC[mu]].ProjM.e + bar[CC[mu]].ProjM.mu + bar[CC[mu]].ProjM.ta + bar[CC[ta]].ProjM.e + bar[CC[ta]].ProjM.mu + bar[CC[ta]].ProjM.ta) + G0 G0 (Nbar.ProjM.ve + Nbar.ProjM.vm + Nbar.ProjM.vt))) /. feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LNG0GP",
      "expression": "Block[{feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; (gw^2 mN/(4 Sqrt[2] MW^2) G0 GP (Nbar.ProjM.e + Nbar.ProjM.mu + Nbar.ProjM.ta + bar[CC[e]].ProjM.N + bar[CC[mu]].ProjM.N + bar[CC[ta]].ProjM.N)) /. feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LNint",
      "expression": "LNW + LNZ + LNH + LNGP + LNG0 + LNGG + LNG0GP",
      "delayed": true
    },
    {
      "name": "LNP",
      "expression": "LNkin + LNint + HC[LNint]",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LNP",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper, the schema, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content

The paper extends the SM by **one** new state: an *unphysical* Majorana neutrino `N` (colour singlet, SU(2) singlet, Q = 0, Y = 0) that models the LN-violating `(ν_ℓ ν^c_ℓ')` current of the d = 5 Weinberg operator. Its interactions are Eq. (23)–(29). The 1/Λ suppression enters through the internal mass `mN = |ΣC5| v²/Λ` (Eq. 9).

One deviation from the generic rule set, stated up front: I give `Lambda` and `Cll` **no** `InteractionOrder`. The paper's own MadGraph5 syntax is `QED=4 QCD=0` for `p p > mu+ mu+ j j`, which counts 2 `Wqq` plus 2 `WℓN` vertices and zero QED order on the mass insertion. `{QED,-1}` on `Lambda` would force `QED=5` and contradict the paper.

## Self-audit table

Field dims: S 1, V 1, F 3/2, `del` 1. `Q` uses SM.fr charges (W⁺=+1, GP=+1, ℓ⁻=−1, ℓ^c=+1 so `bar[CC[l]]`=−1, N=0, ν=0). All terms are written after EWSB in the mass-eigenstate basis, so `Y` is not a symmetry of the individual monomials (Y sum = n/a); electroweak invariance is guaranteed by construction from Eqs. (18)–(22). There is no new U(1) and no new colour/SU(2) index.

| term | fields | d | coupling | coupling dim (=4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) | new U(1) | L sum | CC[] used | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNkin (kin) | `Nbar`,`del N` | 4 | 1 | 0 | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | self-conjugate |
| LNkin (mass) | `Nbar`,`N` | 3 | `mN` | 1 | n/a (mN∝1/Λ) | 0 | n/a | singlet | singlet | none | ΔL=2 (Majorana) | n/a | self-conjugate |
| LNW, Eq.(23) | `W`,`Nbar`,`l` | 4 | `gw/Sqrt[2]` | 0 | n/a | +1+0−1=0 | n/a | mass basis, singlet | singlet | none | ΔL=1 (N has no L) | no | `HC[LNint]` |
| LNZ, Eq.(24) | `Z`,`Nbar`,`vl` | 4 | `gw/(2cw)` | 0 | n/a | 0 | n/a | mass basis, singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNH, Eq.(25) h | `H`,`Nbar`,`vl` | 4 | `gw mN/(2MW)` | 0 | absorbed in `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNH, Eq.(25) hh | `H`,`H`,`Nbar`,`vl` | 5 | `gw^2 mN/(8MW^2)` | −1 | 1/Λ¹ via `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNGP, Eq.(26) G⁺ | `GP`,`Nbar`,`l` / `GP`,`bar[CC[l]]`,`N` | 4 | `gw mN/(2Sqrt[2]MW)` | 0 | absorbed in `mN` | +1+0−1=0 / +1−1+0=0 | n/a | singlet | singlet | none | ΔL=1 | **yes** | `HC[LNint]` |
| LNGP, Eq.(26) G⁺h | `GP`,`H`,`Nbar`,`l` / +`bar[CC[l]]`,`N` | 5 | `gw^2 mN/(4Sqrt[2]MW^2)` | −1 | 1/Λ¹ via `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | **yes** | `HC[LNint]` |
| LNG0, Eq.(27) G⁰ | `G0`,`Nbar`,`vl` | 4 | `gw mN/(2MW)` | 0 | absorbed in `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNG0, Eq.(27) G⁰h | `G0`,`H`,`Nbar`,`vl` | 5 | `gw^2 mN/(4MW^2)` | −1 | 1/Λ¹ via `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNGG, Eq.(28) G⁺G⁺ | `GP`,`GP`,`bar[CC[l]]`,`l` | 5 | `gw^2 mN/(4MW^2)` | −1 | 1/Λ¹ via `mN` | +1+1−1−1=0 | n/a | singlet | singlet | none | ΔL=2 | **yes** | `HC[LNint]` |
| LNGG, Eq.(28) G⁰G⁰ | `G0`,`G0`,`Nbar`,`vl` | 5 | `gw^2 mN/(8MW^2)` | −1 | 1/Λ¹ via `mN` | 0 | n/a | singlet | singlet | none | ΔL=1 | no | `HC[LNint]` |
| LNG0GP, Eq.(29) | `G0`,`GP`,`Nbar`,`l` / +`bar[CC[l]]`,`N` | 5 | `gw^2 mN/(4Sqrt[2]MW^2)` | −1 | 1/Λ¹ via `mN` | 0 / 0 | n/a | singlet | singlet | none | ΔL=1 | **yes** | `HC[LNint]` |

Kinetic + mass check: the only new class is `F[100] == N`; its kinetic and mass term is `LNkin`, and `LNkin` is in the total sum `LTotal := LSM + LNP`.

`SelfConjugate -> True` classes: `N` only. It carries **no** `QuantumNumbers`.

Reference / cached model file read: **none**.

Every dimension-5 row carries `1/Λ` through the internal parameter `mN == Abs[ΣC5] vev^2/Lambda` (Eq. 9), with `Lambda` declared External in GeV at the paper benchmark 200 TeV and `Cll` kept dimensionless at the benchmark `C5 = δ_ℓμ δ_ℓ'μ`.

```json
{
  "model_name": "SMWeinberg_gen",
  "info": {
    "authors": [
      "B. Fuks",
      "J. Neundorf",
      "K. Peters",
      "R. Ruiz",
      "M. Saimpert"
    ],
    "version": "1.0",
    "date": "15. 06. 2021",
    "institutions": [
      "LPTHE, Sorbonne Universite / CNRS",
      "DESY Hamburg",
      "Institute of Nuclear Physics PAN, Cracow",
      "CP3, Universite catholique de Louvain",
      "CERN"
    ],
    "emails": [
      "fuks@lpthe.jussieu.fr",
      "jonas.neundorf@desy.de",
      "krisztian.peters@desy.de",
      "rruiz@ifj.edu.pl",
      "matthias.saimpert@cern.ch"
    ]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Lambda",
      "parameter_type": "External",
      "value": "200000.",
      "block_name": "NUPHYSICS",
      "order_block": 1,
      "tex": "\\[CapitalLambda]",
      "description": "EFT cutoff [GeV] of the d=5 Weinberg operator, Eq.(2); benchmark Lambda = 200 TeV. The operator coefficient is C5/Lambda, mass dimension -1."
    },
    {
      "name": "Cll",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "value_rules": [
        {
          "lhs": "Cll[1,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[1,2]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[1,3]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[2,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[2,2]",
          "rhs": "1.",
          "delayed": false
        },
        {
          "lhs": "Cll[2,3]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[3,1]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[3,2]",
          "rhs": "0.",
          "delayed": false
        },
        {
          "lhs": "Cll[3,3]",
          "rhs": "0.",
          "delayed": false
        }
      ],
      "block_name": "NUPHYSICS",
      "tex": "Subscript[C,5]",
      "description": "Flavour-dependent dimensionless Wilson coefficient C5^{ll'} of the Weinberg operator, Eq.(2). Symmetric in its two Generation indices, so only the six entries (ee, emu, etau, mumu, mutau, tautau) are independent (Les Houches counters 2-7). Benchmark C5^{ll'} = delta_{l mu} delta_{l' mu}."
    },
    {
      "name": "mN",
      "parameter_type": "Internal",
      "value": "Abs[Cll[1,1] + Cll[1,2] + Cll[1,3] + Cll[2,2] + Cll[2,3] + Cll[3,3]] vev^2/Lambda",
      "tex": "Subscript[m,N]",
      "description": "Mass [GeV] of the unphysical Majorana neutrino N, Eq.(9): mN = |Cee + Cemu + Cetau + Cmumu + Cmutau + Ctautau| v^2/Lambda. It carries the whole 1/Lambda suppression of the d=5 operator."
    },
    {
      "name": "wN",
      "parameter_type": "Internal",
      "value": "0.",
      "tex": "Subscript[\\[CapitalGamma],N]",
      "description": "Width [GeV] of the unphysical Majorana neutrino N. N models the off-shell (nu_l nu^c_l') current of Eq.(6)-(7) and never goes on shell, so its width is set to zero."
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "N",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "mN",
        "value": "Internal",
        "members": []
      },
      "width": {
        "massless": false,
        "sym": "wN",
        "value": "Internal",
        "members": []
      },
      "quantum_numbers": {},
      "pdg": 9900012,
      "particle_name": "n1",
      "full_name": "Unphysical Majorana neutrino",
      "propagator_label": "N",
      "propagator_type": "S",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LNkin",
      "expression": "Block[{mu1}, I/2 Nbar.Ga[mu1].del[N, mu1] - 1/2 mN Nbar.N]",
      "delayed": true
    },
    {
      "name": "LNW",
      "expression": "Block[{mu1}, -gw/Sqrt[2] W[mu1] (Nbar.Ga[mu1].ProjM.e + Nbar.Ga[mu1].ProjM.mu + Nbar.Ga[mu1].ProjM.ta)]",
      "delayed": true
    },
    {
      "name": "LNZ",
      "expression": "Block[{mu1}, -gw/(2 cw) Z[mu1] (Nbar.Ga[mu1].ProjM.ve + Nbar.Ga[mu1].ProjM.vm + Nbar.Ga[mu1].ProjM.vt)]",
      "delayed": true
    },
    {
      "name": "LNH",
      "expression": "-gw mN/(2 MW) H (1 + gw/(4 MW) H) (Nbar.ProjM.ve + Nbar.ProjM.vm + Nbar.ProjM.vt)",
      "delayed": true
    },
    {
      "name": "LNGP",
      "expression": "Block[{feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; (-I gw mN/(2 Sqrt[2] MW) GP (1 + gw/(2 MW) H) (Nbar.ProjM.e + Nbar.ProjM.mu + Nbar.ProjM.ta + bar[CC[e]].ProjM.N + bar[CC[mu]].ProjM.N + bar[CC[ta]].ProjM.N)) /. feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LNG0",
      "expression": "Block[{feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; (-I gw mN/(2 MW) G0 (1 + gw/(2 MW) H) (Nbar.ProjM.ve + Nbar.ProjM.vm + Nbar.ProjM.vt)) /. feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LNGG",
      "expression": "Block[{feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; (gw^2 mN/(8 MW^2) (2 GP GP (bar[CC[e]].ProjM.e + bar[CC[e]].ProjM.mu + bar[CC[e]].ProjM.ta + bar[CC[mu]].ProjM.e + bar[CC[mu]].ProjM.mu + bar[CC[mu]].ProjM.ta + bar[CC[ta]].ProjM.e + bar[CC[ta]].ProjM.mu + bar[CC[ta]].ProjM.ta) + G0 G0 (Nbar.ProjM.ve + Nbar.ProjM.vm + Nbar.ProjM.vt))) /. feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LNG0GP",
      "expression": "Block[{feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0|GP|GPbar -> 0}, {}]; (gw^2 mN/(4 Sqrt[2] MW^2) G0 GP (Nbar.ProjM.e + Nbar.ProjM.mu + Nbar.ProjM.ta + bar[CC[e]].ProjM.N + bar[CC[mu]].ProjM.N + bar[CC[ta]].ProjM.N)) /. feynmangaugerules]",
      "delayed": true
    },
    {
      "name": "LNint",
      "expression": "LNW + LNZ + LNH + LNGP + LNG0 + LNGG + LNG0GP",
      "delayed": true
    },
    {
      "name": "LNP",
      "expression": "LNkin + LNint + HC[LNint]",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LNP",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```