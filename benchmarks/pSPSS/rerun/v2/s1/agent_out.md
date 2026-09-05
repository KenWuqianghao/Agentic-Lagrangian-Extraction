I'll start by reading the paper and the schema.
I read the paper, the schema, the renderer, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content (from arXiv:2210.10738, §4–§5)

New states: two sterile left-chiral Majorana neutrinos `N1L`, `N2L` (interaction eigenstates, SM singlets), which become the two physical self-conjugate mass eigenstates `n4`, `n5` with masses from Eq. (4.17). Auxiliary unphysical fields: `nL` (all five neutrino mass eigenstates, new index of range 5) and `PhiNP` (Higgs doublet with `vevNP`). New parameters: `Mmaj`, `deltaM`, `theta1..3`, `damping` (BLOCK PSPSS, Table 2), plus internal `vevNP`, `yvn`, `Un`, `UnCL`, `Mn4`, `Mn5`.

One deliberate deviation: §5.1 prints the Yukawa with `PhiNPbar[jj] Eps[ii, jj]`. In `SM.fr` conventions (`Phi` has Y = +1/2, `LL` has Y = −1/2) that combination has Y-sum −1. `H̃†ℓ` of Eq. (2.1) is the ε-contraction of two doublets, so the invariant form is `LL[ii] PhiNP[jj] Eps[ii, jj]` (Y-sum 0). I use the unbarred `PhiNP`.

## Self-audit table

| term | fields | d | coupling | coup. dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L sum | CC used | H.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNkin (N1L) | `N1Lbar`, `Ga[mu]`, `del[N1L,mu]` | 3/2+1+3/2 = 4 | 1 (I) | 0 ✓ | n/a | 0 | 0+0 = 0 ✓ | singlet (no index) | singlet | none | +1−1 = 0 ✓ | n/a | self-conjugate ✓ |
| LNkin (N2L) | `N2Lbar`, `Ga[mu]`, `del[N2L,mu]` | 4 | 1 (I) | 0 ✓ | n/a | 0 | 0 ✓ | singlet | singlet | none | −1+1 = 0 ✓ | n/a | self-conjugate ✓ |
| LNmass | `CC[N1Lbar[sp1]]`, `N2L[sp1]` | 3/2+3/2 = 3 | `Mmaj` | 1 ✓ (GeV) | n/a | 0 | 0+0 = 0 ✓ | singlet | singlet | none | −1+1 = 0 ✓ | yes (`CC[N1Lbar]`) | `HC[mass]` ✓ |
| LNYuk | `CC[N1Lbar[sp1]]`, `LL[sp1,ii,ff1]`, `PhiNP[jj]`, `Eps[ii,jj]` | 3/2+3/2+1 = 4 | `yvn[ff1]` | 0 ✓ | n/a | 0 (ν·Φ⁰ and l⁻·G⁺ both 0) | 0−1/2+1/2 = 0 ✓ | `Eps[ii,jj]`, two doublets `LL[ii]`,`PhiNP[jj]` | singlet | none | −1+1 = 0 ✓ | yes (`CC[N1Lbar]`) | `HC[yuk]` ✓ |
| free field: n4 | kinetic + `Mn4` via `N1L`/`N2L` → `Un[4,ii] nL` in LNkin+LNmass, both in `LpSPSS` | 4 / 3 | — | — | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | ✓ |
| free field: n5 | kinetic + `Mn5` via `Un[5,ii] nL` in LNkin+LNmass, both in `LpSPSS` | 4 / 3 | — | — | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | ✓ |

`SelfConjugate -> True` classes: `n4`, `n5`. Both carry no `QuantumNumbers`. ✓
No EFT cutoff appears: every operator has d ≤ 4, so no `1/Lambda^n` factor is needed.
Reference or cached model file read: **none**.

```json
{
  "model_name": "pSPSS_gen",
  "info": {
    "authors": ["S. Antusch", "J. Hajer", "J. Rosskopp"],
    "version": "1.0",
    "date": "05. 10. 2023",
    "institutions": ["Universitaet Basel", "CFTP, Instituto Superior Tecnico, Universidade de Lisboa"],
    "emails": ["stefan.antusch@unibas.ch", "jan.hajer@tecnico.ulisboa.pt", "johannes.rosskopp@unibas.ch"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "NuGeneration",
      "range_kind": "NoUnfold",
      "size": 5,
      "style_symbol": "nf"
    }
  ],
  "parameters": [
    {
      "name": "Mmaj",
      "parameter_type": "External",
      "value": "100.",
      "block_name": "PSPSS",
      "order_block": 1,
      "tex": "m_M",
      "description": "Majorana mass parameter mM of the sterile neutrino pair [GeV], Eq. (4.2)"
    },
    {
      "name": "deltaM",
      "parameter_type": "External",
      "value": "1.*^-12",
      "block_name": "PSPSS",
      "order_block": 2,
      "tex": "\\Delta m",
      "description": "Mass splitting Delta m of the pseudo-Dirac heavy neutrino pair [GeV], Eq. (4.17)"
    },
    {
      "name": "theta1",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "PSPSS",
      "order_block": 3,
      "tex": "\\theta_e",
      "description": "Active-sterile mixing parameter theta_e, Eq. (4.6), dimensionless"
    },
    {
      "name": "theta2",
      "parameter_type": "External",
      "value": "1.*^-3",
      "block_name": "PSPSS",
      "order_block": 4,
      "tex": "\\theta_\\mu",
      "description": "Active-sterile mixing parameter theta_mu, Eq. (4.6), dimensionless"
    },
    {
      "name": "theta3",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "PSPSS",
      "order_block": 5,
      "tex": "\\theta_\\tau",
      "description": "Active-sterile mixing parameter theta_tau, Eq. (4.6), dimensionless"
    },
    {
      "name": "damping",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "PSPSS",
      "order_block": 6,
      "tex": "\\lambda",
      "description": "Damping parameter lambda of the heavy neutrino-antineutrino oscillations, Eq. (3.1), dimensionless"
    },
    {
      "name": "thetasq",
      "parameter_type": "Internal",
      "value": "theta1^2 + theta2^2 + theta3^2",
      "tex": "|\\theta|^2",
      "description": "Squared modulus of the active-sterile mixing vector, |theta|^2"
    },
    {
      "name": "Mn4",
      "parameter_type": "Internal",
      "value": "Mmaj (1 + thetasq/2) - deltaM/2",
      "tex": "m_4",
      "description": "Mass of the lighter heavy neutrino mass eigenstate n4 [GeV], Eq. (4.17)"
    },
    {
      "name": "Mn5",
      "parameter_type": "Internal",
      "value": "Mmaj (1 + thetasq/2) + deltaM/2",
      "tex": "m_5",
      "description": "Mass of the heavier heavy neutrino mass eigenstate n5 [GeV], Eq. (4.17)"
    },
    {
      "name": "vevNP",
      "parameter_type": "Internal",
      "value": "2*MW*sw/ee",
      "interaction_order": ["NP", -1],
      "tex": "v_{NP}",
      "description": "Higgs vacuum expectation value [GeV] with NP instead of QED interaction order, Sec. 5.1"
    },
    {
      "name": "yvn",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "yvn[1]", "rhs": "Sqrt[2] theta1 Mmaj / vevNP"},
        {"lhs": "yvn[2]", "rhs": "Sqrt[2] theta2 Mmaj / vevNP"},
        {"lhs": "yvn[3]", "rhs": "Sqrt[2] theta3 Mmaj / vevNP"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "y_{\\nu N}",
      "description": "Neutrino Yukawa coupling vector y_{alpha 1} = Sqrt[2] theta_alpha mM / vevNP, dimensionless, Eqs. (4.2) and (4.6)"
    },
    {
      "name": "Un",
      "parameter_type": "Internal",
      "indices": ["NuGeneration", "NuGeneration"],
      "complex": true,
      "value_rules": [
        {"lhs": "Un[1,1]", "rhs": "1 - theta1^2/2"},
        {"lhs": "Un[1,2]", "rhs": "-theta1 theta2/2"},
        {"lhs": "Un[1,3]", "rhs": "-theta1 theta3/2"},
        {"lhs": "Un[1,4]", "rhs": "-I theta1/Sqrt[2]"},
        {"lhs": "Un[1,5]", "rhs": "theta1/Sqrt[2]"},
        {"lhs": "Un[2,1]", "rhs": "-theta2 theta1/2"},
        {"lhs": "Un[2,2]", "rhs": "1 - theta2^2/2"},
        {"lhs": "Un[2,3]", "rhs": "-theta2 theta3/2"},
        {"lhs": "Un[2,4]", "rhs": "-I theta2/Sqrt[2]"},
        {"lhs": "Un[2,5]", "rhs": "theta2/Sqrt[2]"},
        {"lhs": "Un[3,1]", "rhs": "-theta3 theta1/2"},
        {"lhs": "Un[3,2]", "rhs": "-theta3 theta2/2"},
        {"lhs": "Un[3,3]", "rhs": "1 - theta3^2/2"},
        {"lhs": "Un[3,4]", "rhs": "-I theta3/Sqrt[2]"},
        {"lhs": "Un[3,5]", "rhs": "theta3/Sqrt[2]"},
        {"lhs": "Un[4,1]", "rhs": "0"},
        {"lhs": "Un[4,2]", "rhs": "0"},
        {"lhs": "Un[4,3]", "rhs": "0"},
        {"lhs": "Un[4,4]", "rhs": "I/Sqrt[2]"},
        {"lhs": "Un[4,5]", "rhs": "1/Sqrt[2]"},
        {"lhs": "Un[5,1]", "rhs": "-theta1"},
        {"lhs": "Un[5,2]", "rhs": "-theta2"},
        {"lhs": "Un[5,3]", "rhs": "-theta3"},
        {"lhs": "Un[5,4]", "rhs": "-I (1 - thetasq/2)/Sqrt[2]"},
        {"lhs": "Un[5,5]", "rhs": "(1 - thetasq/2)/Sqrt[2]"}
      ],
      "tex": "U_n",
      "description": "5x5 neutrino mixing matrix relating the interaction eigenstates (nue, numu, nutau, N1, N2) to the mass eigenstates (n1, n2, n3, n4, n5) up to second order in theta, Eqs. (4.8) and (5.1)"
    },
    {
      "name": "UnCL",
      "parameter_type": "Internal",
      "indices": ["Generation", "NuGeneration"],
      "complex": true,
      "value_rules": [
        {"lhs": "UnCL[1,1]", "rhs": "Un[1,1]"},
        {"lhs": "UnCL[1,2]", "rhs": "Un[1,2]"},
        {"lhs": "UnCL[1,3]", "rhs": "Un[1,3]"},
        {"lhs": "UnCL[1,4]", "rhs": "Un[1,4]"},
        {"lhs": "UnCL[1,5]", "rhs": "Un[1,5]"},
        {"lhs": "UnCL[2,1]", "rhs": "Un[2,1]"},
        {"lhs": "UnCL[2,2]", "rhs": "Un[2,2]"},
        {"lhs": "UnCL[2,3]", "rhs": "Un[2,3]"},
        {"lhs": "UnCL[2,4]", "rhs": "Un[2,4]"},
        {"lhs": "UnCL[2,5]", "rhs": "Un[2,5]"},
        {"lhs": "UnCL[3,1]", "rhs": "Un[3,1]"},
        {"lhs": "UnCL[3,2]", "rhs": "Un[3,2]"},
        {"lhs": "UnCL[3,3]", "rhs": "Un[3,3]"},
        {"lhs": "UnCL[3,4]", "rhs": "Un[3,4]"},
        {"lhs": "UnCL[3,5]", "rhs": "Un[3,5]"}
      ],
      "tex": "U^{\\prime}_{CL}",
      "description": "Upper 3x5 charged lepton block of Un, used for the automatic index contraction nu_alpha = UnCL[alpha,i] n_i, Eqs. (4.9) and (5.2)"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "n4",
      "self_conjugate": true,
      "mass": {"sym": "Mn4", "value": "Internal"},
      "width": {"sym": "Wn4", "value": "1."},
      "pdg": 9900012,
      "particle_name": "n4",
      "full_name": "Lighter pseudo-Dirac heavy neutrino mass eigenstate",
      "propagator_label": "n4",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "n5",
      "self_conjugate": true,
      "mass": {"sym": "Mn5", "value": "Internal"},
      "width": {"sym": "Wn5", "value": "1."},
      "pdg": 9900014,
      "particle_name": "n5",
      "full_name": "Heavier pseudo-Dirac heavy neutrino mass eigenstate",
      "propagator_label": "n5",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "nL",
      "self_conjugate": false,
      "unphysical": true,
      "indices": ["NuGeneration"],
      "flavor_index": "NuGeneration",
      "definitions": [
        "nL[sp_, 1] :> vl[sp, 1]",
        "nL[sp_, 2] :> vl[sp, 2]",
        "nL[sp_, 3] :> vl[sp, 3]",
        "nL[sp_, 4] :> n4[sp]",
        "nL[sp_, 5] :> n5[sp]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 103,
      "class_name": "N1L",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0", "LeptonNumber": "-1"},
      "definitions": [
        "N1L[sp1_] :> Module[{sp2, ii}, ProjM[sp1, sp2] Un[4, ii] nL[sp2, ii]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 104,
      "class_name": "N2L",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0", "LeptonNumber": "1"},
      "definitions": [
        "N2L[sp1_] :> Module[{sp2, ii}, ProjM[sp1, sp2] Un[5, ii] nL[sp2, ii]]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "PhiNP",
      "self_conjugate": false,
      "unphysical": true,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "1/2"},
      "definitions": [
        "PhiNP[1] -> -I GP",
        "PhiNP[2] -> (vevNP + H + I G0)/Sqrt[2]"
      ]
    }
  ],
  "raw_blocks": [
    "(* ****************************************************************** *)\n(* *****   Auxiliary definitions of the pSPSS model file        ***** *)\n(* ****************************************************************** *)\n\n(* Rotation of the SM neutrino interaction eigenstates onto the five     *)\n(* neutrino mass eigenstates, Eq. (5.2): nu_alpha = UnCL[alpha, i] n_i.  *)\nMixNeutrinos = {\n  vl[sp_, ff_]    :> Module[{ii}, UnCL[ff, ii] nL[sp, ii]],\n  vlbar[sp_, ff_] :> Module[{ii}, Conjugate[UnCL[ff, ii]] nLbar[sp, ii]]\n};\n\n(* The mixing matrix Un is valid up to second order in theta only.       *)\n(* Expand the Lagrangian in theta and drop all terms beyond O(|theta|^2).*)\nRemoveHigherOrder[expr_] := Module[{eps, res},\n  res = expr /. MR$Definitions;\n  res = res /. {theta1 -> eps theta1, theta2 -> eps theta2, theta3 -> eps theta3};\n  Normal[Series[res, {eps, 0, 2}]] /. eps -> 1\n];"
  ],
  "lagrangian_terms": [
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I (N1Lbar.Ga[mu].del[N1L, mu] + N2Lbar.Ga[mu].del[N2L, mu]), FlavorExpand -> {NuGeneration}]]"
    },
    {
      "name": "LNmass",
      "delayed": true,
      "expression": "Block[{sp1, mass}, mass = ExpandIndices[- Mmaj CC[N1Lbar[sp1]].N2L[sp1], FlavorExpand -> {NuGeneration}]; mass + HC[mass]]"
    },
    {
      "name": "LNYuk",
      "delayed": true,
      "expression": "Block[{sp1, ii, jj, ff1, yuk}, yuk = ExpandIndices[yvn[ff1] (CC[N1Lbar[sp1]].LL[sp1, ii, ff1] PhiNP[jj] Eps[ii, jj]), FlavorExpand -> {SU2D, NuGeneration}]; yuk + HC[yuk]]"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LNmass + LNYuk"
    },
    {
      "name": "LpSPSS",
      "delayed": true,
      "expression": "RemoveHigherOrder[(LSM + LNkin + LNP) /. MixNeutrinos]"
    }
  ]
}
```
I read the paper, the schema, the renderer, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content (from arXiv:2210.10738, §4–§5)

New states: two sterile left-chiral Majorana neutrinos `N1L`, `N2L` (interaction eigenstates, SM singlets), which become the two physical self-conjugate mass eigenstates `n4`, `n5` with masses from Eq. (4.17). Auxiliary unphysical fields: `nL` (all five neutrino mass eigenstates, new index of range 5) and `PhiNP` (Higgs doublet with `vevNP`). New parameters: `Mmaj`, `deltaM`, `theta1..3`, `damping` (BLOCK PSPSS, Table 2), plus internal `vevNP`, `yvn`, `Un`, `UnCL`, `Mn4`, `Mn5`.

One deliberate deviation: §5.1 prints the Yukawa with `PhiNPbar[jj] Eps[ii, jj]`. In `SM.fr` conventions (`Phi` has Y = +1/2, `LL` has Y = −1/2) that combination has Y-sum −1. `H̃†ℓ` of Eq. (2.1) is the ε-contraction of two doublets, so the invariant form is `LL[ii] PhiNP[jj] Eps[ii, jj]` (Y-sum 0). I use the unbarred `PhiNP`.

## Self-audit table

| term | fields | d | coupling | coup. dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L sum | CC used | H.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNkin (N1L) | `N1Lbar`, `Ga[mu]`, `del[N1L,mu]` | 3/2+1+3/2 = 4 | 1 (I) | 0 ✓ | n/a | 0 | 0+0 = 0 ✓ | singlet (no index) | singlet | none | +1−1 = 0 ✓ | n/a | self-conjugate ✓ |
| LNkin (N2L) | `N2Lbar`, `Ga[mu]`, `del[N2L,mu]` | 4 | 1 (I) | 0 ✓ | n/a | 0 | 0 ✓ | singlet | singlet | none | −1+1 = 0 ✓ | n/a | self-conjugate ✓ |
| LNmass | `CC[N1Lbar[sp1]]`, `N2L[sp1]` | 3/2+3/2 = 3 | `Mmaj` | 1 ✓ (GeV) | n/a | 0 | 0+0 = 0 ✓ | singlet | singlet | none | −1+1 = 0 ✓ | yes (`CC[N1Lbar]`) | `HC[mass]` ✓ |
| LNYuk | `CC[N1Lbar[sp1]]`, `LL[sp1,ii,ff1]`, `PhiNP[jj]`, `Eps[ii,jj]` | 3/2+3/2+1 = 4 | `yvn[ff1]` | 0 ✓ | n/a | 0 (ν·Φ⁰ and l⁻·G⁺ both 0) | 0−1/2+1/2 = 0 ✓ | `Eps[ii,jj]`, two doublets `LL[ii]`,`PhiNP[jj]` | singlet | none | −1+1 = 0 ✓ | yes (`CC[N1Lbar]`) | `HC[yuk]` ✓ |
| free field: n4 | kinetic + `Mn4` via `N1L`/`N2L` → `Un[4,ii] nL` in LNkin+LNmass, both in `LpSPSS` | 4 / 3 | — | — | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | ✓ |
| free field: n5 | kinetic + `Mn5` via `Un[5,ii] nL` in LNkin+LNmass, both in `LpSPSS` | 4 / 3 | — | — | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | ✓ |

`SelfConjugate -> True` classes: `n4`, `n5`. Both carry no `QuantumNumbers`. ✓
No EFT cutoff appears: every operator has d ≤ 4, so no `1/Lambda^n` factor is needed.
Reference or cached model file read: **none**.

```json
{
  "model_name": "pSPSS_gen",
  "info": {
    "authors": ["S. Antusch", "J. Hajer", "J. Rosskopp"],
    "version": "1.0",
    "date": "05. 10. 2023",
    "institutions": ["Universitaet Basel", "CFTP, Instituto Superior Tecnico, Universidade de Lisboa"],
    "emails": ["stefan.antusch@unibas.ch", "jan.hajer@tecnico.ulisboa.pt", "johannes.rosskopp@unibas.ch"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "NuGeneration",
      "range_kind": "NoUnfold",
      "size": 5,
      "style_symbol": "nf"
    }
  ],
  "parameters": [
    {
      "name": "Mmaj",
      "parameter_type": "External",
      "value": "100.",
      "block_name": "PSPSS",
      "order_block": 1,
      "tex": "m_M",
      "description": "Majorana mass parameter mM of the sterile neutrino pair [GeV], Eq. (4.2)"
    },
    {
      "name": "deltaM",
      "parameter_type": "External",
      "value": "1.*^-12",
      "block_name": "PSPSS",
      "order_block": 2,
      "tex": "\\Delta m",
      "description": "Mass splitting Delta m of the pseudo-Dirac heavy neutrino pair [GeV], Eq. (4.17)"
    },
    {
      "name": "theta1",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "PSPSS",
      "order_block": 3,
      "tex": "\\theta_e",
      "description": "Active-sterile mixing parameter theta_e, Eq. (4.6), dimensionless"
    },
    {
      "name": "theta2",
      "parameter_type": "External",
      "value": "1.*^-3",
      "block_name": "PSPSS",
      "order_block": 4,
      "tex": "\\theta_\\mu",
      "description": "Active-sterile mixing parameter theta_mu, Eq. (4.6), dimensionless"
    },
    {
      "name": "theta3",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "PSPSS",
      "order_block": 5,
      "tex": "\\theta_\\tau",
      "description": "Active-sterile mixing parameter theta_tau, Eq. (4.6), dimensionless"
    },
    {
      "name": "damping",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "PSPSS",
      "order_block": 6,
      "tex": "\\lambda",
      "description": "Damping parameter lambda of the heavy neutrino-antineutrino oscillations, Eq. (3.1), dimensionless"
    },
    {
      "name": "thetasq",
      "parameter_type": "Internal",
      "value": "theta1^2 + theta2^2 + theta3^2",
      "tex": "|\\theta|^2",
      "description": "Squared modulus of the active-sterile mixing vector, |theta|^2"
    },
    {
      "name": "Mn4",
      "parameter_type": "Internal",
      "value": "Mmaj (1 + thetasq/2) - deltaM/2",
      "tex": "m_4",
      "description": "Mass of the lighter heavy neutrino mass eigenstate n4 [GeV], Eq. (4.17)"
    },
    {
      "name": "Mn5",
      "parameter_type": "Internal",
      "value": "Mmaj (1 + thetasq/2) + deltaM/2",
      "tex": "m_5",
      "description": "Mass of the heavier heavy neutrino mass eigenstate n5 [GeV], Eq. (4.17)"
    },
    {
      "name": "vevNP",
      "parameter_type": "Internal",
      "value": "2*MW*sw/ee",
      "interaction_order": ["NP", -1],
      "tex": "v_{NP}",
      "description": "Higgs vacuum expectation value [GeV] with NP instead of QED interaction order, Sec. 5.1"
    },
    {
      "name": "yvn",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "yvn[1]", "rhs": "Sqrt[2] theta1 Mmaj / vevNP"},
        {"lhs": "yvn[2]", "rhs": "Sqrt[2] theta2 Mmaj / vevNP"},
        {"lhs": "yvn[3]", "rhs": "Sqrt[2] theta3 Mmaj / vevNP"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "y_{\\nu N}",
      "description": "Neutrino Yukawa coupling vector y_{alpha 1} = Sqrt[2] theta_alpha mM / vevNP, dimensionless, Eqs. (4.2) and (4.6)"
    },
    {
      "name": "Un",
      "parameter_type": "Internal",
      "indices": ["NuGeneration", "NuGeneration"],
      "complex": true,
      "value_rules": [
        {"lhs": "Un[1,1]", "rhs": "1 - theta1^2/2"},
        {"lhs": "Un[1,2]", "rhs": "-theta1 theta2/2"},
        {"lhs": "Un[1,3]", "rhs": "-theta1 theta3/2"},
        {"lhs": "Un[1,4]", "rhs": "-I theta1/Sqrt[2]"},
        {"lhs": "Un[1,5]", "rhs": "theta1/Sqrt[2]"},
        {"lhs": "Un[2,1]", "rhs": "-theta2 theta1/2"},
        {"lhs": "Un[2,2]", "rhs": "1 - theta2^2/2"},
        {"lhs": "Un[2,3]", "rhs": "-theta2 theta3/2"},
        {"lhs": "Un[2,4]", "rhs": "-I theta2/Sqrt[2]"},
        {"lhs": "Un[2,5]", "rhs": "theta2/Sqrt[2]"},
        {"lhs": "Un[3,1]", "rhs": "-theta3 theta1/2"},
        {"lhs": "Un[3,2]", "rhs": "-theta3 theta2/2"},
        {"lhs": "Un[3,3]", "rhs": "1 - theta3^2/2"},
        {"lhs": "Un[3,4]", "rhs": "-I theta3/Sqrt[2]"},
        {"lhs": "Un[3,5]", "rhs": "theta3/Sqrt[2]"},
        {"lhs": "Un[4,1]", "rhs": "0"},
        {"lhs": "Un[4,2]", "rhs": "0"},
        {"lhs": "Un[4,3]", "rhs": "0"},
        {"lhs": "Un[4,4]", "rhs": "I/Sqrt[2]"},
        {"lhs": "Un[4,5]", "rhs": "1/Sqrt[2]"},
        {"lhs": "Un[5,1]", "rhs": "-theta1"},
        {"lhs": "Un[5,2]", "rhs": "-theta2"},
        {"lhs": "Un[5,3]", "rhs": "-theta3"},
        {"lhs": "Un[5,4]", "rhs": "-I (1 - thetasq/2)/Sqrt[2]"},
        {"lhs": "Un[5,5]", "rhs": "(1 - thetasq/2)/Sqrt[2]"}
      ],
      "tex": "U_n",
      "description": "5x5 neutrino mixing matrix relating the interaction eigenstates (nue, numu, nutau, N1, N2) to the mass eigenstates (n1, n2, n3, n4, n5) up to second order in theta, Eqs. (4.8) and (5.1)"
    },
    {
      "name": "UnCL",
      "parameter_type": "Internal",
      "indices": ["Generation", "NuGeneration"],
      "complex": true,
      "value_rules": [
        {"lhs": "UnCL[1,1]", "rhs": "Un[1,1]"},
        {"lhs": "UnCL[1,2]", "rhs": "Un[1,2]"},
        {"lhs": "UnCL[1,3]", "rhs": "Un[1,3]"},
        {"lhs": "UnCL[1,4]", "rhs": "Un[1,4]"},
        {"lhs": "UnCL[1,5]", "rhs": "Un[1,5]"},
        {"lhs": "UnCL[2,1]", "rhs": "Un[2,1]"},
        {"lhs": "UnCL[2,2]", "rhs": "Un[2,2]"},
        {"lhs": "UnCL[2,3]", "rhs": "Un[2,3]"},
        {"lhs": "UnCL[2,4]", "rhs": "Un[2,4]"},
        {"lhs": "UnCL[2,5]", "rhs": "Un[2,5]"},
        {"lhs": "UnCL[3,1]", "rhs": "Un[3,1]"},
        {"lhs": "UnCL[3,2]", "rhs": "Un[3,2]"},
        {"lhs": "UnCL[3,3]", "rhs": "Un[3,3]"},
        {"lhs": "UnCL[3,4]", "rhs": "Un[3,4]"},
        {"lhs": "UnCL[3,5]", "rhs": "Un[3,5]"}
      ],
      "tex": "U^{\\prime}_{CL}",
      "description": "Upper 3x5 charged lepton block of Un, used for the automatic index contraction nu_alpha = UnCL[alpha,i] n_i, Eqs. (4.9) and (5.2)"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "n4",
      "self_conjugate": true,
      "mass": {"sym": "Mn4", "value": "Internal"},
      "width": {"sym": "Wn4", "value": "1."},
      "pdg": 9900012,
      "particle_name": "n4",
      "full_name": "Lighter pseudo-Dirac heavy neutrino mass eigenstate",
      "propagator_label": "n4",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "n5",
      "self_conjugate": true,
      "mass": {"sym": "Mn5", "value": "Internal"},
      "width": {"sym": "Wn5", "value": "1."},
      "pdg": 9900014,
      "particle_name": "n5",
      "full_name": "Heavier pseudo-Dirac heavy neutrino mass eigenstate",
      "propagator_label": "n5",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "nL",
      "self_conjugate": false,
      "unphysical": true,
      "indices": ["NuGeneration"],
      "flavor_index": "NuGeneration",
      "definitions": [
        "nL[sp_, 1] :> vl[sp, 1]",
        "nL[sp_, 2] :> vl[sp, 2]",
        "nL[sp_, 3] :> vl[sp, 3]",
        "nL[sp_, 4] :> n4[sp]",
        "nL[sp_, 5] :> n5[sp]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 103,
      "class_name": "N1L",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0", "LeptonNumber": "-1"},
      "definitions": [
        "N1L[sp1_] :> Module[{sp2, ii}, ProjM[sp1, sp2] Un[4, ii] nL[sp2, ii]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 104,
      "class_name": "N2L",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0", "LeptonNumber": "1"},
      "definitions": [
        "N2L[sp1_] :> Module[{sp2, ii}, ProjM[sp1, sp2] Un[5, ii] nL[sp2, ii]]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "PhiNP",
      "self_conjugate": false,
      "unphysical": true,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "1/2"},
      "definitions": [
        "PhiNP[1] -> -I GP",
        "PhiNP[2] -> (vevNP + H + I G0)/Sqrt[2]"
      ]
    }
  ],
  "raw_blocks": [
    "(* ****************************************************************** *)\n(* *****   Auxiliary definitions of the pSPSS model file        ***** *)\n(* ****************************************************************** *)\n\n(* Rotation of the SM neutrino interaction eigenstates onto the five     *)\n(* neutrino mass eigenstates, Eq. (5.2): nu_alpha = UnCL[alpha, i] n_i.  *)\nMixNeutrinos = {\n  vl[sp_, ff_]    :> Module[{ii}, UnCL[ff, ii] nL[sp, ii]],\n  vlbar[sp_, ff_] :> Module[{ii}, Conjugate[UnCL[ff, ii]] nLbar[sp, ii]]\n};\n\n(* The mixing matrix Un is valid up to second order in theta only.       *)\n(* Expand the Lagrangian in theta and drop all terms beyond O(|theta|^2).*)\nRemoveHigherOrder[expr_] := Module[{eps, res},\n  res = expr /. MR$Definitions;\n  res = res /. {theta1 -> eps theta1, theta2 -> eps theta2, theta3 -> eps theta3};\n  Normal[Series[res, {eps, 0, 2}]] /. eps -> 1\n];"
  ],
  "lagrangian_terms": [
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I (N1Lbar.Ga[mu].del[N1L, mu] + N2Lbar.Ga[mu].del[N2L, mu]), FlavorExpand -> {NuGeneration}]]"
    },
    {
      "name": "LNmass",
      "delayed": true,
      "expression": "Block[{sp1, mass}, mass = ExpandIndices[- Mmaj CC[N1Lbar[sp1]].N2L[sp1], FlavorExpand -> {NuGeneration}]; mass + HC[mass]]"
    },
    {
      "name": "LNYuk",
      "delayed": true,
      "expression": "Block[{sp1, ii, jj, ff1, yuk}, yuk = ExpandIndices[yvn[ff1] (CC[N1Lbar[sp1]].LL[sp1, ii, ff1] PhiNP[jj] Eps[ii, jj]), FlavorExpand -> {SU2D, NuGeneration}]; yuk + HC[yuk]]"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LNmass + LNYuk"
    },
    {
      "name": "LpSPSS",
      "delayed": true,
      "expression": "RemoveHigherOrder[(LSM + LNkin + LNP) /. MixNeutrinos]"
    }
  ]
}
```