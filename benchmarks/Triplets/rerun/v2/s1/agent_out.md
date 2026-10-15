I'll start by reading the paper and the schema files.
## Self-audit table

Base file: `SM.fr` (given as the base of this add-on). Physical quark classes `uq[ff,cc]` (Q = 2/3) and `dq[ff,cc]` (Q = −1/3) carry **Q**, not **Y** — the paper's Eq. (2.1) is written after electroweak symmetry breaking, so the Y column is n/a for the interaction terms (Table 1 hypercharges are recorded in the class descriptions instead).

Charge rule used: a field contributes its declared Q; `bar[...]` contributes −Q; `CC[...]` contributes −Q.

| term name | fields in the monomial | d | coupling symbol | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | B/L | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LDQudKin (kinetic) | `DC[phiudbar,mu] DC[phiud,mu]` | 4 | 1 | 0 ✓ | n/a | −1/3+1/3 = 0 ✓ | n/a | singlet | shared `cc` (3̄⊗3) ✓ | none | n/a | n/a | self-Hermitian ✓ |
| LDQudKin (mass) | `MDQud^2 phiudbar phiud` | 2 | `MDQud^2` | 2 = 4−2 ✓ | n/a | 0 ✓ | n/a | singlet | shared `cc` ✓ | none | n/a | n/a | self-Hermitian ✓ |
| LDQddKin | `DC[phiddbar,mu] DC[phidd,mu] − MDQdd^2 phiddbar phidd` | 4 / 2 | 1 / `MDQdd^2` | 0 / 2 ✓ | n/a | 0 ✓ | n/a | singlet | shared `cc` ✓ | none | n/a | n/a | self-Hermitian ✓ |
| LDQuuKin | `DC[phiuubar,mu] DC[phiuu,mu] − MDQuu^2 phiuubar phiuu` | 4 / 2 | 1 / `MDQuu^2` | 0 / 2 ✓ | n/a | 0 ✓ | n/a | singlet | shared `cc` ✓ | none | n/a | n/a | self-Hermitian ✓ |
| LDQudInt | `phiud` (1) · `uqbar` (3/2) · `CC[dq]` (3/2) | 4 | `lamL1`, `lamR1` | 0 ✓ | n/a | +1/3 − 2/3 + 1/3 = 0 ✓ | n/a | n/a (mass eigenstates, Eq. 2.1) | `Eps[cc1,cc2,cc3]` = Clebsch K_abc = ε_abc/√2, Eq. (A.7) ✓ | none | B(φ)=2/3, not declared (SM.fr quarks carry no B) | yes (`CC[dq]`) | `HC[LDQudInt]` ✓ |
| LDQddInt | `phidd` · `dqbar` · `CC[dq]` | 4 | `lamL2`, `lamR2` | 0 ✓ | n/a | −2/3 + 1/3 + 1/3 = 0 ✓ | n/a | n/a | `Eps[cc1,cc2,cc3]` ✓ | none | as above | yes (`CC[dq]`) | `HC[LDQddInt]` ✓ |
| LDQuuInt | `phiuu` · `uqbar` · `CC[uq]` | 4 | `lamL3`, `lamR3` | 0 ✓ | n/a | +4/3 − 2/3 − 2/3 = 0 ✓ | n/a | n/a | `Eps[cc1,cc2,cc3]` ✓ | none | as above | yes (`CC[uq]`) | `HC[LDQuuInt]` ✓ |

Kinetic + mass confirmation, one row per new class: `phiud` → LDQudKin ✓ in `LDiquark`; `phidd` → LDQddKin ✓ in `LDiquark`; `phiuu` → LDQuuKin ✓ in `LDiquark`.

Classes with `SelfConjugate -> True`: **none** (all three diquarks are complex scalars, so all carry `SelfConjugate -> False` and may hold `QuantumNumbers`).

Reference or cached `.fr` model file read: **none**. Only the paper text, the schema, the renderer and the given `SM.fr` base were opened.

Notes on scope and choices:
- The paper gives one interaction, Eq. (2.1). Its diquark charge is the sum of the two quark charges. Table 1 gives |Q| = 1/3, 2/3, 4/3, and Sec. 5 names the final-state charges −2/3, +1/3 (antitriplet) and +4/3. So the colour-antitriplet spectrum is three complex scalars, Q = +1/3 (u d), −2/3 (d d) and +4/3 (u u). The SU(2) triplet row of Table 1 adds no new charge; its three components are the same three charges.
- The couplings for identical quark types are antisymmetric in flavour (Sec. 2), so `lamL2/lamR2` and `lamL3/lamR3` have zero diagonal. This reproduces the paper's statement that the antitriplet has no identical initial partons.
- Colour Clebsch: for the antitriplet K_abc = ε_abc/√2 (Eq. A.7), so the prefactor 2√2 K of Eq. (2.1) becomes the factor 2 with `Eps[cc1,cc2,cc3]`.
- The colour-**sextet** option of the same paper is not in this file. A sextet needs a new `Sextet` index plus an SU(3)_C sextet representation in `M$GaugeGroups`, which an SM add-on with `gauge_groups: []` cannot declare. It belongs in the companion sextet model file.
- All coupling values are 0.1, the benchmark size stated in Sec. 2. Masses are 1000. GeV, the benchmark of Table 2.

```json
{
  "model_name": "Triplets_gen",
  "info": {
    "authors": ["T. Han", "I. Lewis", "T. McElmurry"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["Department of Physics, University of Wisconsin, Madison"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "lamL1",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQUDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL1[1,1]", "rhs": "0.1"},
        {"lhs": "lamL1[1,2]", "rhs": "0."},
        {"lhs": "lamL1[1,3]", "rhs": "0."},
        {"lhs": "lamL1[2,1]", "rhs": "0."},
        {"lhs": "lamL1[2,2]", "rhs": "0.1"},
        {"lhs": "lamL1[2,3]", "rhs": "0."},
        {"lhs": "lamL1[3,1]", "rhs": "0."},
        {"lhs": "lamL1[3,2]", "rhs": "0."},
        {"lhs": "lamL1[3,3]", "rhs": "0.1"}
      ],
      "description": "Left-chiral coupling of the charge 1/3 antitriplet diquark to one up-type and one down-type quark, Eq. (2.1). Dimensionless. Benchmark 0.1, Sec. 2."
    },
    {
      "name": "lamR1",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQUDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR1[1,1]", "rhs": "0.1"},
        {"lhs": "lamR1[1,2]", "rhs": "0."},
        {"lhs": "lamR1[1,3]", "rhs": "0."},
        {"lhs": "lamR1[2,1]", "rhs": "0."},
        {"lhs": "lamR1[2,2]", "rhs": "0.1"},
        {"lhs": "lamR1[2,3]", "rhs": "0."},
        {"lhs": "lamR1[3,1]", "rhs": "0."},
        {"lhs": "lamR1[3,2]", "rhs": "0."},
        {"lhs": "lamR1[3,3]", "rhs": "0.1"}
      ],
      "description": "Right-chiral coupling of the charge 1/3 antitriplet diquark to one up-type and one down-type quark, Eq. (2.1). Dimensionless. Benchmark 0.1, Sec. 2."
    },
    {
      "name": "lamL2",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQDDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL2[1,1]", "rhs": "0."},
        {"lhs": "lamL2[1,2]", "rhs": "0.1"},
        {"lhs": "lamL2[1,3]", "rhs": "0.1"},
        {"lhs": "lamL2[2,1]", "rhs": "-0.1"},
        {"lhs": "lamL2[2,2]", "rhs": "0."},
        {"lhs": "lamL2[2,3]", "rhs": "0.1"},
        {"lhs": "lamL2[3,1]", "rhs": "-0.1"},
        {"lhs": "lamL2[3,2]", "rhs": "-0.1"},
        {"lhs": "lamL2[3,3]", "rhs": "0."}
      ],
      "description": "Left-chiral coupling of the charge -2/3 antitriplet diquark to two down-type quarks, Eq. (2.1). Antisymmetric in flavour, Sec. 2. Dimensionless."
    },
    {
      "name": "lamR2",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQDDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR2[1,1]", "rhs": "0."},
        {"lhs": "lamR2[1,2]", "rhs": "0.1"},
        {"lhs": "lamR2[1,3]", "rhs": "0.1"},
        {"lhs": "lamR2[2,1]", "rhs": "-0.1"},
        {"lhs": "lamR2[2,2]", "rhs": "0."},
        {"lhs": "lamR2[2,3]", "rhs": "0.1"},
        {"lhs": "lamR2[3,1]", "rhs": "-0.1"},
        {"lhs": "lamR2[3,2]", "rhs": "-0.1"},
        {"lhs": "lamR2[3,3]", "rhs": "0."}
      ],
      "description": "Right-chiral coupling of the charge -2/3 antitriplet diquark to two down-type quarks, Eq. (2.1). Antisymmetric in flavour. Dimensionless."
    },
    {
      "name": "lamL3",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQUUL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL3[1,1]", "rhs": "0."},
        {"lhs": "lamL3[1,2]", "rhs": "0.1"},
        {"lhs": "lamL3[1,3]", "rhs": "0.1"},
        {"lhs": "lamL3[2,1]", "rhs": "-0.1"},
        {"lhs": "lamL3[2,2]", "rhs": "0."},
        {"lhs": "lamL3[2,3]", "rhs": "0.1"},
        {"lhs": "lamL3[3,1]", "rhs": "-0.1"},
        {"lhs": "lamL3[3,2]", "rhs": "-0.1"},
        {"lhs": "lamL3[3,3]", "rhs": "0."}
      ],
      "description": "Left-chiral coupling of the charge 4/3 antitriplet diquark to two up-type quarks, Eq. (2.1). Antisymmetric in flavour, so the uu entry is zero, Sec. 5. Dimensionless."
    },
    {
      "name": "lamR3",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQUUR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR3[1,1]", "rhs": "0."},
        {"lhs": "lamR3[1,2]", "rhs": "0.1"},
        {"lhs": "lamR3[1,3]", "rhs": "0.1"},
        {"lhs": "lamR3[2,1]", "rhs": "-0.1"},
        {"lhs": "lamR3[2,2]", "rhs": "0."},
        {"lhs": "lamR3[2,3]", "rhs": "0.1"},
        {"lhs": "lamR3[3,1]", "rhs": "-0.1"},
        {"lhs": "lamR3[3,2]", "rhs": "-0.1"},
        {"lhs": "lamR3[3,3]", "rhs": "0."}
      ],
      "description": "Right-chiral coupling of the charge 4/3 antitriplet diquark to two up-type quarks, Eq. (2.1). The uc entry follows the bound 0.1 and the cc entry is zero, Eq. (2.2). Dimensionless."
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "phiud",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MDQud", "value": "1000."},
      "width": {"sym": "WDQud", "value": "1."},
      "quantum_numbers": {"Q": "1/3"},
      "pdg": 9000001,
      "particle_name": "phiud",
      "antiparticle_name": "phiud~",
      "full_name": "Colour antitriplet scalar diquark, up-down type",
      "propagator_label": "phiud",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "phidd",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MDQdd", "value": "1000."},
      "width": {"sym": "WDQdd", "value": "1."},
      "quantum_numbers": {"Q": "-2/3"},
      "pdg": 9000002,
      "particle_name": "phidd",
      "antiparticle_name": "phidd~",
      "full_name": "Colour antitriplet scalar diquark, down-down type",
      "propagator_label": "phidd",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "phiuu",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MDQuu", "value": "1000."},
      "width": {"sym": "WDQuu", "value": "1."},
      "quantum_numbers": {"Q": "4/3"},
      "pdg": 9000003,
      "particle_name": "phiuu",
      "antiparticle_name": "phiuu~",
      "full_name": "Colour antitriplet scalar diquark, up-up type",
      "propagator_label": "phiuu",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LDQudKin",
      "delayed": true,
      "expression": "Block[{mu, cc}, DC[phiudbar[cc], mu] DC[phiud[cc], mu] - MDQud^2 phiudbar[cc] phiud[cc]]"
    },
    {
      "name": "LDQddKin",
      "delayed": true,
      "expression": "Block[{mu, cc}, DC[phiddbar[cc], mu] DC[phidd[cc], mu] - MDQdd^2 phiddbar[cc] phidd[cc]]"
    },
    {
      "name": "LDQuuKin",
      "delayed": true,
      "expression": "Block[{mu, cc}, DC[phiuubar[cc], mu] DC[phiuu[cc], mu] - MDQuu^2 phiuubar[cc] phiuu[cc]]"
    },
    {
      "name": "LDQudInt",
      "delayed": true,
      "expression": "Block[{ff1, ff2, cc1, cc2, cc3}, 2 Eps[cc1, cc2, cc3] phiud[cc1] (uqbar[ff1, cc2].(lamL1[ff1, ff2] ProjM + lamR1[ff1, ff2] ProjP).CC[dq][ff2, cc3])]"
    },
    {
      "name": "LDQddInt",
      "delayed": true,
      "expression": "Block[{ff1, ff2, cc1, cc2, cc3}, 2 Eps[cc1, cc2, cc3] phidd[cc1] (dqbar[ff1, cc2].(lamL2[ff1, ff2] ProjM + lamR2[ff1, ff2] ProjP).CC[dq][ff2, cc3])]"
    },
    {
      "name": "LDQuuInt",
      "delayed": true,
      "expression": "Block[{ff1, ff2, cc1, cc2, cc3}, 2 Eps[cc1, cc2, cc3] phiuu[cc1] (uqbar[ff1, cc2].(lamL3[ff1, ff2] ProjM + lamR3[ff1, ff2] ProjP).CC[uq][ff2, cc3])]"
    },
    {
      "name": "LDiquark",
      "delayed": true,
      "expression": "LDQudKin + LDQddKin + LDQuuKin + LDQudInt + HC[LDQudInt] + LDQddInt + HC[LDQddInt] + LDQuuInt + HC[LDQuuInt]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LDiquark"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
## Self-audit table

Base file: `SM.fr` (given as the base of this add-on). Physical quark classes `uq[ff,cc]` (Q = 2/3) and `dq[ff,cc]` (Q = −1/3) carry **Q**, not **Y** — the paper's Eq. (2.1) is written after electroweak symmetry breaking, so the Y column is n/a for the interaction terms (Table 1 hypercharges are recorded in the class descriptions instead).

Charge rule used: a field contributes its declared Q; `bar[...]` contributes −Q; `CC[...]` contributes −Q.

| term name | fields in the monomial | d | coupling symbol | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | B/L | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LDQudKin (kinetic) | `DC[phiudbar,mu] DC[phiud,mu]` | 4 | 1 | 0 ✓ | n/a | −1/3+1/3 = 0 ✓ | n/a | singlet | shared `cc` (3̄⊗3) ✓ | none | n/a | n/a | self-Hermitian ✓ |
| LDQudKin (mass) | `MDQud^2 phiudbar phiud` | 2 | `MDQud^2` | 2 = 4−2 ✓ | n/a | 0 ✓ | n/a | singlet | shared `cc` ✓ | none | n/a | n/a | self-Hermitian ✓ |
| LDQddKin | `DC[phiddbar,mu] DC[phidd,mu] − MDQdd^2 phiddbar phidd` | 4 / 2 | 1 / `MDQdd^2` | 0 / 2 ✓ | n/a | 0 ✓ | n/a | singlet | shared `cc` ✓ | none | n/a | n/a | self-Hermitian ✓ |
| LDQuuKin | `DC[phiuubar,mu] DC[phiuu,mu] − MDQuu^2 phiuubar phiuu` | 4 / 2 | 1 / `MDQuu^2` | 0 / 2 ✓ | n/a | 0 ✓ | n/a | singlet | shared `cc` ✓ | none | n/a | n/a | self-Hermitian ✓ |
| LDQudInt | `phiud` (1) · `uqbar` (3/2) · `CC[dq]` (3/2) | 4 | `lamL1`, `lamR1` | 0 ✓ | n/a | +1/3 − 2/3 + 1/3 = 0 ✓ | n/a | n/a (mass eigenstates, Eq. 2.1) | `Eps[cc1,cc2,cc3]` = Clebsch K_abc = ε_abc/√2, Eq. (A.7) ✓ | none | B(φ)=2/3, not declared (SM.fr quarks carry no B) | yes (`CC[dq]`) | `HC[LDQudInt]` ✓ |
| LDQddInt | `phidd` · `dqbar` · `CC[dq]` | 4 | `lamL2`, `lamR2` | 0 ✓ | n/a | −2/3 + 1/3 + 1/3 = 0 ✓ | n/a | n/a | `Eps[cc1,cc2,cc3]` ✓ | none | as above | yes (`CC[dq]`) | `HC[LDQddInt]` ✓ |
| LDQuuInt | `phiuu` · `uqbar` · `CC[uq]` | 4 | `lamL3`, `lamR3` | 0 ✓ | n/a | +4/3 − 2/3 − 2/3 = 0 ✓ | n/a | n/a | `Eps[cc1,cc2,cc3]` ✓ | none | as above | yes (`CC[uq]`) | `HC[LDQuuInt]` ✓ |

Kinetic + mass confirmation, one row per new class: `phiud` → LDQudKin ✓ in `LDiquark`; `phidd` → LDQddKin ✓ in `LDiquark`; `phiuu` → LDQuuKin ✓ in `LDiquark`.

Classes with `SelfConjugate -> True`: **none** (all three diquarks are complex scalars, so all carry `SelfConjugate -> False` and may hold `QuantumNumbers`).

Reference or cached `.fr` model file read: **none**. Only the paper text, the schema, the renderer and the given `SM.fr` base were opened.

Notes on scope and choices:
- The paper gives one interaction, Eq. (2.1). Its diquark charge is the sum of the two quark charges. Table 1 gives |Q| = 1/3, 2/3, 4/3, and Sec. 5 names the final-state charges −2/3, +1/3 (antitriplet) and +4/3. So the colour-antitriplet spectrum is three complex scalars, Q = +1/3 (u d), −2/3 (d d) and +4/3 (u u). The SU(2) triplet row of Table 1 adds no new charge; its three components are the same three charges.
- The couplings for identical quark types are antisymmetric in flavour (Sec. 2), so `lamL2/lamR2` and `lamL3/lamR3` have zero diagonal. This reproduces the paper's statement that the antitriplet has no identical initial partons.
- Colour Clebsch: for the antitriplet K_abc = ε_abc/√2 (Eq. A.7), so the prefactor 2√2 K of Eq. (2.1) becomes the factor 2 with `Eps[cc1,cc2,cc3]`.
- The colour-**sextet** option of the same paper is not in this file. A sextet needs a new `Sextet` index plus an SU(3)_C sextet representation in `M$GaugeGroups`, which an SM add-on with `gauge_groups: []` cannot declare. It belongs in the companion sextet model file.
- All coupling values are 0.1, the benchmark size stated in Sec. 2. Masses are 1000. GeV, the benchmark of Table 2.

```json
{
  "model_name": "Triplets_gen",
  "info": {
    "authors": ["T. Han", "I. Lewis", "T. McElmurry"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["Department of Physics, University of Wisconsin, Madison"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "lamL1",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQUDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL1[1,1]", "rhs": "0.1"},
        {"lhs": "lamL1[1,2]", "rhs": "0."},
        {"lhs": "lamL1[1,3]", "rhs": "0."},
        {"lhs": "lamL1[2,1]", "rhs": "0."},
        {"lhs": "lamL1[2,2]", "rhs": "0.1"},
        {"lhs": "lamL1[2,3]", "rhs": "0."},
        {"lhs": "lamL1[3,1]", "rhs": "0."},
        {"lhs": "lamL1[3,2]", "rhs": "0."},
        {"lhs": "lamL1[3,3]", "rhs": "0.1"}
      ],
      "description": "Left-chiral coupling of the charge 1/3 antitriplet diquark to one up-type and one down-type quark, Eq. (2.1). Dimensionless. Benchmark 0.1, Sec. 2."
    },
    {
      "name": "lamR1",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQUDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR1[1,1]", "rhs": "0.1"},
        {"lhs": "lamR1[1,2]", "rhs": "0."},
        {"lhs": "lamR1[1,3]", "rhs": "0."},
        {"lhs": "lamR1[2,1]", "rhs": "0."},
        {"lhs": "lamR1[2,2]", "rhs": "0.1"},
        {"lhs": "lamR1[2,3]", "rhs": "0."},
        {"lhs": "lamR1[3,1]", "rhs": "0."},
        {"lhs": "lamR1[3,2]", "rhs": "0."},
        {"lhs": "lamR1[3,3]", "rhs": "0.1"}
      ],
      "description": "Right-chiral coupling of the charge 1/3 antitriplet diquark to one up-type and one down-type quark, Eq. (2.1). Dimensionless. Benchmark 0.1, Sec. 2."
    },
    {
      "name": "lamL2",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQDDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL2[1,1]", "rhs": "0."},
        {"lhs": "lamL2[1,2]", "rhs": "0.1"},
        {"lhs": "lamL2[1,3]", "rhs": "0.1"},
        {"lhs": "lamL2[2,1]", "rhs": "-0.1"},
        {"lhs": "lamL2[2,2]", "rhs": "0."},
        {"lhs": "lamL2[2,3]", "rhs": "0.1"},
        {"lhs": "lamL2[3,1]", "rhs": "-0.1"},
        {"lhs": "lamL2[3,2]", "rhs": "-0.1"},
        {"lhs": "lamL2[3,3]", "rhs": "0."}
      ],
      "description": "Left-chiral coupling of the charge -2/3 antitriplet diquark to two down-type quarks, Eq. (2.1). Antisymmetric in flavour, Sec. 2. Dimensionless."
    },
    {
      "name": "lamR2",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQDDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR2[1,1]", "rhs": "0."},
        {"lhs": "lamR2[1,2]", "rhs": "0.1"},
        {"lhs": "lamR2[1,3]", "rhs": "0.1"},
        {"lhs": "lamR2[2,1]", "rhs": "-0.1"},
        {"lhs": "lamR2[2,2]", "rhs": "0."},
        {"lhs": "lamR2[2,3]", "rhs": "0.1"},
        {"lhs": "lamR2[3,1]", "rhs": "-0.1"},
        {"lhs": "lamR2[3,2]", "rhs": "-0.1"},
        {"lhs": "lamR2[3,3]", "rhs": "0."}
      ],
      "description": "Right-chiral coupling of the charge -2/3 antitriplet diquark to two down-type quarks, Eq. (2.1). Antisymmetric in flavour. Dimensionless."
    },
    {
      "name": "lamL3",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQUUL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL3[1,1]", "rhs": "0."},
        {"lhs": "lamL3[1,2]", "rhs": "0.1"},
        {"lhs": "lamL3[1,3]", "rhs": "0.1"},
        {"lhs": "lamL3[2,1]", "rhs": "-0.1"},
        {"lhs": "lamL3[2,2]", "rhs": "0."},
        {"lhs": "lamL3[2,3]", "rhs": "0.1"},
        {"lhs": "lamL3[3,1]", "rhs": "-0.1"},
        {"lhs": "lamL3[3,2]", "rhs": "-0.1"},
        {"lhs": "lamL3[3,3]", "rhs": "0."}
      ],
      "description": "Left-chiral coupling of the charge 4/3 antitriplet diquark to two up-type quarks, Eq. (2.1). Antisymmetric in flavour, so the uu entry is zero, Sec. 5. Dimensionless."
    },
    {
      "name": "lamR3",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "DQUUR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR3[1,1]", "rhs": "0."},
        {"lhs": "lamR3[1,2]", "rhs": "0.1"},
        {"lhs": "lamR3[1,3]", "rhs": "0.1"},
        {"lhs": "lamR3[2,1]", "rhs": "-0.1"},
        {"lhs": "lamR3[2,2]", "rhs": "0."},
        {"lhs": "lamR3[2,3]", "rhs": "0.1"},
        {"lhs": "lamR3[3,1]", "rhs": "-0.1"},
        {"lhs": "lamR3[3,2]", "rhs": "-0.1"},
        {"lhs": "lamR3[3,3]", "rhs": "0."}
      ],
      "description": "Right-chiral coupling of the charge 4/3 antitriplet diquark to two up-type quarks, Eq. (2.1). The uc entry follows the bound 0.1 and the cc entry is zero, Eq. (2.2). Dimensionless."
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "phiud",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MDQud", "value": "1000."},
      "width": {"sym": "WDQud", "value": "1."},
      "quantum_numbers": {"Q": "1/3"},
      "pdg": 9000001,
      "particle_name": "phiud",
      "antiparticle_name": "phiud~",
      "full_name": "Colour antitriplet scalar diquark, up-down type",
      "propagator_label": "phiud",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "phidd",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MDQdd", "value": "1000."},
      "width": {"sym": "WDQdd", "value": "1."},
      "quantum_numbers": {"Q": "-2/3"},
      "pdg": 9000002,
      "particle_name": "phidd",
      "antiparticle_name": "phidd~",
      "full_name": "Colour antitriplet scalar diquark, down-down type",
      "propagator_label": "phidd",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "phiuu",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MDQuu", "value": "1000."},
      "width": {"sym": "WDQuu", "value": "1."},
      "quantum_numbers": {"Q": "4/3"},
      "pdg": 9000003,
      "particle_name": "phiuu",
      "antiparticle_name": "phiuu~",
      "full_name": "Colour antitriplet scalar diquark, up-up type",
      "propagator_label": "phiuu",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LDQudKin",
      "delayed": true,
      "expression": "Block[{mu, cc}, DC[phiudbar[cc], mu] DC[phiud[cc], mu] - MDQud^2 phiudbar[cc] phiud[cc]]"
    },
    {
      "name": "LDQddKin",
      "delayed": true,
      "expression": "Block[{mu, cc}, DC[phiddbar[cc], mu] DC[phidd[cc], mu] - MDQdd^2 phiddbar[cc] phidd[cc]]"
    },
    {
      "name": "LDQuuKin",
      "delayed": true,
      "expression": "Block[{mu, cc}, DC[phiuubar[cc], mu] DC[phiuu[cc], mu] - MDQuu^2 phiuubar[cc] phiuu[cc]]"
    },
    {
      "name": "LDQudInt",
      "delayed": true,
      "expression": "Block[{ff1, ff2, cc1, cc2, cc3}, 2 Eps[cc1, cc2, cc3] phiud[cc1] (uqbar[ff1, cc2].(lamL1[ff1, ff2] ProjM + lamR1[ff1, ff2] ProjP).CC[dq][ff2, cc3])]"
    },
    {
      "name": "LDQddInt",
      "delayed": true,
      "expression": "Block[{ff1, ff2, cc1, cc2, cc3}, 2 Eps[cc1, cc2, cc3] phidd[cc1] (dqbar[ff1, cc2].(lamL2[ff1, ff2] ProjM + lamR2[ff1, ff2] ProjP).CC[dq][ff2, cc3])]"
    },
    {
      "name": "LDQuuInt",
      "delayed": true,
      "expression": "Block[{ff1, ff2, cc1, cc2, cc3}, 2 Eps[cc1, cc2, cc3] phiuu[cc1] (uqbar[ff1, cc2].(lamL3[ff1, ff2] ProjM + lamR3[ff1, ff2] ProjP).CC[uq][ff2, cc3])]"
    },
    {
      "name": "LDiquark",
      "delayed": true,
      "expression": "LDQudKin + LDQddKin + LDQuuKin + LDQudInt + HC[LDQudInt] + LDQddInt + HC[LDQddInt] + LDQuuInt + HC[LDQuuInt]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LDiquark"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```