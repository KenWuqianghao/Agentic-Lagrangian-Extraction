I'll start by reading the paper and the schema.
I read the paper and the schema. The model is a simplified model with one new state: a colour-singlet, electrically neutral, real vector resonance `V1` that couples only to the top quark (Eq. 2.1), with three free parameters `MV1`, `ct`, `theta`.

## Self-audit table

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (must be 4−d) | 1/Λ power (must be d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) charge sum | L/B number sum | CC[] used? | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LV1kin` (kinetic) | `FS[V1,mu,nu] FS[V1,mu,nu]` | 4 | `-1/4` | 0 = 4−4 ✓ | n/a (d≤4) | 0+0 = 0 ✓ | 0+0 = 0 ✓ | singlet (no SU(2) index) | singlet (no Colour index) | none declared (0) ✓ | 0 ✓ | n/a | self-conjugate (real field) |
| `LV1kin` (mass) | `V1[mu] V1[mu]` | 2 | `1/2 MV1^2` | 2 = 4−2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | 0 ✓ | 0 ✓ | n/a | self-conjugate |
| `LV1int` (left) | `tbar . Ga[mu] . ProjM . t V1[mu]` | 3/2+3/2+1 = 4 | `cL` | 0 = 4−4 ✓ | n/a | −2/3 + 2/3 + 0 = 0 ✓ | mass-eigenstate current, vector-like: −2/3+2/3 = 0 ✓ | singlet (physical `t`, no SU2D index) | `tbar[cc] … t[cc]` implicit Dot contraction, `V1` colour singlet ⇒ singlet ✓ | 0 ✓ | B: −1/3 + 1/3 = 0 ✓ | n/a (no `psi^c` in Eq. 2.1) | self-hermitian (`(tbar Ga[mu] ProjM t)† = tbar Ga[mu] ProjM t`), no `HC[]` needed |
| `LV1int` (right) | `tbar . Ga[mu] . ProjP . t V1[mu]` | 4 | `cR` | 0 = 4−4 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet ✓ | 0 ✓ | 0 ✓ | n/a | self-hermitian |
| free-field check: `V1` | `LV1kin` exists (kinetic + `MV1` mass, mass symbol matches `Mass -> {MV1, 1500.}`) and is summed in `LTopPhilic` ✓ | — | — | — | — | — | — | — | — | — | — | — | — |

`SelfConjugate -> True` classes: `V1` only. It carries **no** `QuantumNumbers` (Q = 0, colour singlet, SU(2) singlet). ✓

Reference or cached `.fr` model file for this model read: **none**. Only `SM.fr` (the base Standard Model file named in the task) and the schema/renderer were read.

Notes on choices:
- `PL = (1−γ5)/2 → ProjM`, `PR = (1+γ5)/2 → ProjP`, matching Eq. 2.1.
- `cL = ct Cos[theta]`, `cR = ct Sin[theta]` are Internal, derived from the two External inputs `ct` and `thetaC`.
- The width uses Eq. 2.2 verbatim as an Internal parameter, so it tracks `MV1`, `ct` and `theta`.
- No new U(1) is added: `V1` is not a gauge boson of a new group in this simplified model, so no SM charge re-derivation is needed and `gauge_groups` is empty.
- No EFT cutoff is needed: Eq. 2.1 is renormalisable (d = 4). Eq. 2.3 is only the integrated-out limit used for bounds, not the implemented model.

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
    "date": "02. 09. 2026",
    "institutions": [
      "Korea Advanced Institute of Science and Technology (KAIST)",
      "Center for Theoretical Physics of the Universe, Institute for Basic Science (IBS)",
      "University of Kansas",
      "Korea University",
      "Korea Institute for Advanced Study (KIAS)",
      "Fermi National Accelerator Laboratory"
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
    ["NP", 1]
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
      "tex": "Subscript[c,t]",
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark, ct = Sqrt[cL^2+cR^2], Eq.(2.1). Benchmark value ct = 2.0 (MV1 = 1.5 TeV)."
    },
    {
      "name": "thetaC",
      "parameter_type": "External",
      "value": "1.5707963267948966",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "\\[Theta]",
      "description": "Chirality angle theta of Eq.(2.1), with Tan[theta] = cR/cL. Dimensionless (radians). Benchmark theta = Pi/2, i.e. a purely right-handed coupling; theta = 3 Pi/4 is the axial limit."
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct Cos[thetaC]",
      "interaction_order": ["NP", 1],
      "tex": "Subscript[c,L]",
      "description": "Left-handed coupling of V1 to the top quark, cL = ct Cos[theta], Eq.(2.1)."
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct Sin[thetaC]",
      "interaction_order": ["NP", 1],
      "tex": "Subscript[c,R]",
      "description": "Right-handed coupling of V1 to the top quark, cR = ct Sin[theta], Eq.(2.1)."
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2 MV1/(8 Pi) Sqrt[1 - 4 MT^2/MV1^2] (1 - MT^2/MV1^2 (1 - 3 Sin[2 thetaC]))",
      "tex": "Subscript[\\[CapitalGamma],V1]",
      "description": "Total width of V1 [GeV] from the two-body decay V1 -> t tbar, Eq.(2.2)."
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
      "expression": "Block[{mu, nu}, ExpandIndices[-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]]]",
      "delayed": true
    },
    {
      "name": "LV1int",
      "expression": "Block[{mu}, ExpandIndices[(cL tbar.Ga[mu].ProjM.t + cR tbar.Ga[mu].ProjP.t) V1[mu]]]",
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
I read the paper and the schema. The model is a simplified model with one new state: a colour-singlet, electrically neutral, real vector resonance `V1` that couples only to the top quark (Eq. 2.1), with three free parameters `MV1`, `ct`, `theta`.

## Self-audit table

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (must be 4−d) | 1/Λ power (must be d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) charge sum | L/B number sum | CC[] used? | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LV1kin` (kinetic) | `FS[V1,mu,nu] FS[V1,mu,nu]` | 4 | `-1/4` | 0 = 4−4 ✓ | n/a (d≤4) | 0+0 = 0 ✓ | 0+0 = 0 ✓ | singlet (no SU(2) index) | singlet (no Colour index) | none declared (0) ✓ | 0 ✓ | n/a | self-conjugate (real field) |
| `LV1kin` (mass) | `V1[mu] V1[mu]` | 2 | `1/2 MV1^2` | 2 = 4−2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | 0 ✓ | 0 ✓ | n/a | self-conjugate |
| `LV1int` (left) | `tbar . Ga[mu] . ProjM . t V1[mu]` | 3/2+3/2+1 = 4 | `cL` | 0 = 4−4 ✓ | n/a | −2/3 + 2/3 + 0 = 0 ✓ | mass-eigenstate current, vector-like: −2/3+2/3 = 0 ✓ | singlet (physical `t`, no SU2D index) | `tbar[cc] … t[cc]` implicit Dot contraction, `V1` colour singlet ⇒ singlet ✓ | 0 ✓ | B: −1/3 + 1/3 = 0 ✓ | n/a (no `psi^c` in Eq. 2.1) | self-hermitian (`(tbar Ga[mu] ProjM t)† = tbar Ga[mu] ProjM t`), no `HC[]` needed |
| `LV1int` (right) | `tbar . Ga[mu] . ProjP . t V1[mu]` | 4 | `cR` | 0 = 4−4 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet ✓ | 0 ✓ | 0 ✓ | n/a | self-hermitian |
| free-field check: `V1` | `LV1kin` exists (kinetic + `MV1` mass, mass symbol matches `Mass -> {MV1, 1500.}`) and is summed in `LTopPhilic` ✓ | — | — | — | — | — | — | — | — | — | — | — | — |

`SelfConjugate -> True` classes: `V1` only. It carries **no** `QuantumNumbers` (Q = 0, colour singlet, SU(2) singlet). ✓

Reference or cached `.fr` model file for this model read: **none**. Only `SM.fr` (the base Standard Model file named in the task) and the schema/renderer were read.

Notes on choices:
- `PL = (1−γ5)/2 → ProjM`, `PR = (1+γ5)/2 → ProjP`, matching Eq. 2.1.
- `cL = ct Cos[theta]`, `cR = ct Sin[theta]` are Internal, derived from the two External inputs `ct` and `thetaC`.
- The width uses Eq. 2.2 verbatim as an Internal parameter, so it tracks `MV1`, `ct` and `theta`.
- No new U(1) is added: `V1` is not a gauge boson of a new group in this simplified model, so no SM charge re-derivation is needed and `gauge_groups` is empty.
- No EFT cutoff is needed: Eq. 2.1 is renormalisable (d = 4). Eq. 2.3 is only the integrated-out limit used for bounds, not the implemented model.

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
    "date": "02. 09. 2026",
    "institutions": [
      "Korea Advanced Institute of Science and Technology (KAIST)",
      "Center for Theoretical Physics of the Universe, Institute for Basic Science (IBS)",
      "University of Kansas",
      "Korea University",
      "Korea Institute for Advanced Study (KIAS)",
      "Fermi National Accelerator Laboratory"
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
    ["NP", 1]
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
      "tex": "Subscript[c,t]",
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark, ct = Sqrt[cL^2+cR^2], Eq.(2.1). Benchmark value ct = 2.0 (MV1 = 1.5 TeV)."
    },
    {
      "name": "thetaC",
      "parameter_type": "External",
      "value": "1.5707963267948966",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "\\[Theta]",
      "description": "Chirality angle theta of Eq.(2.1), with Tan[theta] = cR/cL. Dimensionless (radians). Benchmark theta = Pi/2, i.e. a purely right-handed coupling; theta = 3 Pi/4 is the axial limit."
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct Cos[thetaC]",
      "interaction_order": ["NP", 1],
      "tex": "Subscript[c,L]",
      "description": "Left-handed coupling of V1 to the top quark, cL = ct Cos[theta], Eq.(2.1)."
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct Sin[thetaC]",
      "interaction_order": ["NP", 1],
      "tex": "Subscript[c,R]",
      "description": "Right-handed coupling of V1 to the top quark, cR = ct Sin[theta], Eq.(2.1)."
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2 MV1/(8 Pi) Sqrt[1 - 4 MT^2/MV1^2] (1 - MT^2/MV1^2 (1 - 3 Sin[2 thetaC]))",
      "tex": "Subscript[\\[CapitalGamma],V1]",
      "description": "Total width of V1 [GeV] from the two-body decay V1 -> t tbar, Eq.(2.2)."
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
      "expression": "Block[{mu, nu}, ExpandIndices[-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]]]",
      "delayed": true
    },
    {
      "name": "LV1int",
      "expression": "Block[{mu}, ExpandIndices[(cL tbar.Ga[mu].ProjM.t + cR tbar.Ga[mu].ProjP.t) V1[mu]]]",
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