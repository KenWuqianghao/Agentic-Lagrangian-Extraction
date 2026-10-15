I'll start by reading the paper and the schema.
## Extraction notes

The paper defines a simplified model with **one** new state: a colour-singlet, SU(2)-singlet, electrically neutral **real vector** resonance `V1`, coupled only to the top quark (Eq. 2.1). No new multiplets, no new generations, no new indices, no new gauge group. Eq. (2.3) is the EFT limit of the same field (integrate out `V1` at `θ = π/2`), not an independent operator, so it is not a separate Lagrangian term.

Free parameters (paper §2.2): `MV1`, `ct`, `θ`. Benchmark: `MV1 = 1500 GeV`, `ct = 2.0`, `θ = π/2`. The width follows Eq. (2.2), so `WV1` is Internal.

Charge check: `V1` is self-conjugate, so it carries no `QuantumNumbers`. Its coupling is a top-quark vector/axial current, which is neutral under Q, Y, SU(2) and SU(3), so no new U(1) charge assignment is needed anywhere.

## Self-audit table

| term name | fields in monomial | d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new U(1) sums | L/B sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LV1kin` (kinetic) | `FS[V1,mu,nu] FS[V1,mu,nu]` | 4 | `-1/4` | 0 | n/a | 0 | 0 | singlet | singlet | none declared | 0 | n/a | self-conjugate (real) |
| `LV1kin` (mass) | `MV1^2 V1[mu] V1[mu]` | 2 (+2 from `MV1^2`) | `MV1^2` | 2 | n/a | 0 | 0 | singlet | singlet | none declared | 0 | n/a | self-conjugate (real) |
| `LV1int` (left) | `tbar . Ga[mu] . ProjM . t * V1[mu]` | 4 | `ct Cos[th]` | 0 | n/a | −2/3 + 2/3 + 0 = 0 | 0 (mass eigenstates, Q used) | singlet (physical top) | `3bar ⊗ 3` on the shared implicit Colour index | none declared | B: −1/3 + 1/3 = 0 | n/a (no `psi^c` in paper) | Hermitian by itself (`(tbar Ga PL t)† = tbar Ga PL t`), real `V1` |
| `LV1int` (right) | `tbar . Ga[mu] . ProjP . t * V1[mu]` | 4 | `ct Sin[th]` | 0 | n/a | 0 | 0 | singlet | `3bar ⊗ 3` shared index | none declared | 0 | n/a | Hermitian by itself, real `V1` |

Per-class free-field confirmation: `V[100]` (`V1`) has the kinetic + mass term `LV1kin`, built with the class mass symbol `MV1`, and `LV1kin` is inside the total sum `LTopPhilic`.

`SelfConjugate -> True` classes: `V1` only — it carries **no** `QuantumNumbers`.

Reference or cached model file read: **none**.

```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": [
      "Jeong Han Kim",
      "Kyoungchul Kong",
      "Seung J. Lee",
      "Gopolang Mohlabeng"
    ],
    "version": "1.0",
    "date": "2016-11-03",
    "institutions": [
      "KAIST and CTPU, IBS, Daejeon, Korea",
      "University of Kansas, Lawrence, KS, USA",
      "Korea University and KIAS, Seoul, Korea",
      "Fermilab, Batavia, IL, USA"
    ],
    "emails": [
      "jeonghan.kim@kaist.ac.kr",
      "kckong@ku.edu",
      "sjjlee@korea.edu",
      "gopolang.mohlabeng@ku.edu"
    ]
  },
  "interaction_order_hierarchy": [
    ["QCD", 1],
    ["QED", 2],
    ["NP", 3]
  ],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "ct",
      "parameter_type": "External",
      "value": "2.0",
      "block_name": "TOPPHILIC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "parameter_name": "ct",
      "tex": "c_t",
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark, ct = Sqrt[cL^2 + cR^2], Eq.(2.1). Dimensionless. Benchmark value 2.0 (Fig. 3, Tables VI, IX, XII)."
    },
    {
      "name": "th",
      "parameter_type": "External",
      "value": "1.570796326794897",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "parameter_name": "th",
      "tex": "\\theta",
      "description": "Chirality angle theta with Tan[theta] = cR/cL, Eq.(2.1). Dimensionless, in radians. Benchmark value Pi/2 (pure right-handed coupling), Section 2.2."
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct Cos[th]",
      "interaction_order": ["NP", 1],
      "parameter_name": "cL",
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark, cL = ct Cos[theta], Eq.(2.1)."
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct Sin[th]",
      "interaction_order": ["NP", 1],
      "parameter_name": "cR",
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark, cR = ct Sin[theta], Eq.(2.1)."
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2 MV1/(8 Pi) Sqrt[1 - 4 MT^2/MV1^2] (1 - MT^2/MV1^2 (1 - 3 Sin[2 th]))",
      "parameter_name": "WV1",
      "tex": "\\Gamma_{V_1}",
      "description": "Total width of V1 in GeV, from the two-body decay V1 -> t tbar, Eq.(2.2). MT is the SM top mass."
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "MV1",
        "value": "1500."
      },
      "width": {
        "massless": false,
        "sym": "WV1",
        "value": "Internal"
      },
      "quantum_numbers": {},
      "pdg": 32,
      "particle_name": "V1",
      "full_name": "Top-philic colour-singlet vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1kin",
      "expression": "-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]",
      "delayed": true
    },
    {
      "name": "LV1int",
      "expression": "ct V1[mu] (Cos[th] tbar.Ga[mu].ProjM.t + Sin[th] tbar.Ga[mu].ProjP.t)",
      "delayed": true
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1kin + LV1int",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
## Extraction notes

The paper defines a simplified model with **one** new state: a colour-singlet, SU(2)-singlet, electrically neutral **real vector** resonance `V1`, coupled only to the top quark (Eq. 2.1). No new multiplets, no new generations, no new indices, no new gauge group. Eq. (2.3) is the EFT limit of the same field (integrate out `V1` at `θ = π/2`), not an independent operator, so it is not a separate Lagrangian term.

Free parameters (paper §2.2): `MV1`, `ct`, `θ`. Benchmark: `MV1 = 1500 GeV`, `ct = 2.0`, `θ = π/2`. The width follows Eq. (2.2), so `WV1` is Internal.

Charge check: `V1` is self-conjugate, so it carries no `QuantumNumbers`. Its coupling is a top-quark vector/axial current, which is neutral under Q, Y, SU(2) and SU(3), so no new U(1) charge assignment is needed anywhere.

## Self-audit table

| term name | fields in monomial | d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new U(1) sums | L/B sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LV1kin` (kinetic) | `FS[V1,mu,nu] FS[V1,mu,nu]` | 4 | `-1/4` | 0 | n/a | 0 | 0 | singlet | singlet | none declared | 0 | n/a | self-conjugate (real) |
| `LV1kin` (mass) | `MV1^2 V1[mu] V1[mu]` | 2 (+2 from `MV1^2`) | `MV1^2` | 2 | n/a | 0 | 0 | singlet | singlet | none declared | 0 | n/a | self-conjugate (real) |
| `LV1int` (left) | `tbar . Ga[mu] . ProjM . t * V1[mu]` | 4 | `ct Cos[th]` | 0 | n/a | −2/3 + 2/3 + 0 = 0 | 0 (mass eigenstates, Q used) | singlet (physical top) | `3bar ⊗ 3` on the shared implicit Colour index | none declared | B: −1/3 + 1/3 = 0 | n/a (no `psi^c` in paper) | Hermitian by itself (`(tbar Ga PL t)† = tbar Ga PL t`), real `V1` |
| `LV1int` (right) | `tbar . Ga[mu] . ProjP . t * V1[mu]` | 4 | `ct Sin[th]` | 0 | n/a | 0 | 0 | singlet | `3bar ⊗ 3` shared index | none declared | 0 | n/a | Hermitian by itself, real `V1` |

Per-class free-field confirmation: `V[100]` (`V1`) has the kinetic + mass term `LV1kin`, built with the class mass symbol `MV1`, and `LV1kin` is inside the total sum `LTopPhilic`.

`SelfConjugate -> True` classes: `V1` only — it carries **no** `QuantumNumbers`.

Reference or cached model file read: **none**.

```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": [
      "Jeong Han Kim",
      "Kyoungchul Kong",
      "Seung J. Lee",
      "Gopolang Mohlabeng"
    ],
    "version": "1.0",
    "date": "2016-11-03",
    "institutions": [
      "KAIST and CTPU, IBS, Daejeon, Korea",
      "University of Kansas, Lawrence, KS, USA",
      "Korea University and KIAS, Seoul, Korea",
      "Fermilab, Batavia, IL, USA"
    ],
    "emails": [
      "jeonghan.kim@kaist.ac.kr",
      "kckong@ku.edu",
      "sjjlee@korea.edu",
      "gopolang.mohlabeng@ku.edu"
    ]
  },
  "interaction_order_hierarchy": [
    ["QCD", 1],
    ["QED", 2],
    ["NP", 3]
  ],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "ct",
      "parameter_type": "External",
      "value": "2.0",
      "block_name": "TOPPHILIC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "parameter_name": "ct",
      "tex": "c_t",
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark, ct = Sqrt[cL^2 + cR^2], Eq.(2.1). Dimensionless. Benchmark value 2.0 (Fig. 3, Tables VI, IX, XII)."
    },
    {
      "name": "th",
      "parameter_type": "External",
      "value": "1.570796326794897",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "parameter_name": "th",
      "tex": "\\theta",
      "description": "Chirality angle theta with Tan[theta] = cR/cL, Eq.(2.1). Dimensionless, in radians. Benchmark value Pi/2 (pure right-handed coupling), Section 2.2."
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct Cos[th]",
      "interaction_order": ["NP", 1],
      "parameter_name": "cL",
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark, cL = ct Cos[theta], Eq.(2.1)."
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct Sin[th]",
      "interaction_order": ["NP", 1],
      "parameter_name": "cR",
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark, cR = ct Sin[theta], Eq.(2.1)."
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2 MV1/(8 Pi) Sqrt[1 - 4 MT^2/MV1^2] (1 - MT^2/MV1^2 (1 - 3 Sin[2 th]))",
      "parameter_name": "WV1",
      "tex": "\\Gamma_{V_1}",
      "description": "Total width of V1 in GeV, from the two-body decay V1 -> t tbar, Eq.(2.2). MT is the SM top mass."
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {
        "massless": false,
        "sym": "MV1",
        "value": "1500."
      },
      "width": {
        "massless": false,
        "sym": "WV1",
        "value": "Internal"
      },
      "quantum_numbers": {},
      "pdg": 32,
      "particle_name": "V1",
      "full_name": "Top-philic colour-singlet vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1kin",
      "expression": "-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]",
      "delayed": true
    },
    {
      "name": "LV1int",
      "expression": "ct V1[mu] (Cos[th] tbar.Ga[mu].ProjM.t + Sin[th] tbar.Ga[mu].ProjP.t)",
      "delayed": true
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1kin + LV1int",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```