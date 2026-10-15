I'll start by reading the paper and the schema.
I've read the paper, the schema, the renderer, and SM.fr. The new-physics content is a single colour-singlet, SU(2)-singlet, neutral vector resonance `V1` with chiral couplings to the top quark only (Eq. 2.1), plus its width (Eq. 2.2).

**Content of the model**

| Item | Value |
|---|---|
| New state | `V1` — spin 1, colour singlet, SU(2) singlet, Q = 0, real (self-conjugate) |
| Mass | `MV1`, benchmark 1500. GeV |
| Width | `WV1`, Internal, from Eq. (2.2) |
| Couplings | `ct` (overall strength), `thV1` (chirality angle θ); `cL = ct Cos[θ]`, `cR = ct Sin[θ]` |
| Lagrangian | kinetic + mass term, and `tbar.Ga[mu].(cL ProjM + cR ProjP).t V1[mu]` |

No other new states appear in the paper: the summary confirms one colour-singlet vector resonance only.

```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": ["Jeong Han Kim", "Kyoungchul Kong", "Seung J. Lee", "Gopolang Mohlabeng"],
    "version": "1.0",
    "date": "03. 11. 2016",
    "institutions": [
      "Korea Advanced Institute of Science and Technology",
      "University of Kansas",
      "Korea University",
      "Fermilab"
    ],
    "emails": [
      "jeonghan.kim@kaist.ac.kr",
      "kckong@ku.edu",
      "sjjlee@korea.edu",
      "gopolang.mohlabeng@ku.edu"
    ]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "ct",
      "parameter_type": "External",
      "value": "2.",
      "block_name": "TOPPHILIC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "c_t",
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark"
    },
    {
      "name": "thV1",
      "parameter_type": "External",
      "value": "1.5707963267948966",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "\\theta",
      "description": "Chirality angle theta, tan(theta) = cR/cL (theta = Pi/2 is the purely right-handed benchmark)"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[thV1]",
      "interaction_order": ["NP", 1],
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[thV1]",
      "interaction_order": ["NP", 1],
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark"
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2*MV1/(8*Pi)*Sqrt[1 - 4*MT^2/MV1^2]*(1 - MT^2/MV1^2*(1 - 3*Sin[2*thV1]))",
      "tex": "\\Gamma_{V_1}",
      "description": "Width of V1 into a top pair, Eq. (2.2)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "mass": {"sym": "MV1", "value": "1500."},
      "width": {"sym": "WV1", "value": "Internal"},
      "quantum_numbers": {"Q": "0"},
      "pdg": 32,
      "particle_name": "V1",
      "full_name": "Top-philic vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[V1,mu,nu] FS[V1,mu,nu] + 1/2 MV1^2 V1[mu] V1[mu]]]",
      "delayed": true
    },
    {
      "name": "LV1Int",
      "expression": "Block[{mu}, ExpandIndices[tbar.Ga[mu].(cL ProjM + cR ProjP).t V1[mu]]]",
      "delayed": true
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1Kin + LV1Int",
      "delayed": true
    }
  ]
}
```
I've read the paper, the schema, the renderer, and SM.fr. The new-physics content is a single colour-singlet, SU(2)-singlet, neutral vector resonance `V1` with chiral couplings to the top quark only (Eq. 2.1), plus its width (Eq. 2.2).

**Content of the model**

| Item | Value |
|---|---|
| New state | `V1` — spin 1, colour singlet, SU(2) singlet, Q = 0, real (self-conjugate) |
| Mass | `MV1`, benchmark 1500. GeV |
| Width | `WV1`, Internal, from Eq. (2.2) |
| Couplings | `ct` (overall strength), `thV1` (chirality angle θ); `cL = ct Cos[θ]`, `cR = ct Sin[θ]` |
| Lagrangian | kinetic + mass term, and `tbar.Ga[mu].(cL ProjM + cR ProjP).t V1[mu]` |

No other new states appear in the paper: the summary confirms one colour-singlet vector resonance only.

```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": ["Jeong Han Kim", "Kyoungchul Kong", "Seung J. Lee", "Gopolang Mohlabeng"],
    "version": "1.0",
    "date": "03. 11. 2016",
    "institutions": [
      "Korea Advanced Institute of Science and Technology",
      "University of Kansas",
      "Korea University",
      "Fermilab"
    ],
    "emails": [
      "jeonghan.kim@kaist.ac.kr",
      "kckong@ku.edu",
      "sjjlee@korea.edu",
      "gopolang.mohlabeng@ku.edu"
    ]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "ct",
      "parameter_type": "External",
      "value": "2.",
      "block_name": "TOPPHILIC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "c_t",
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark"
    },
    {
      "name": "thV1",
      "parameter_type": "External",
      "value": "1.5707963267948966",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "\\theta",
      "description": "Chirality angle theta, tan(theta) = cR/cL (theta = Pi/2 is the purely right-handed benchmark)"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[thV1]",
      "interaction_order": ["NP", 1],
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[thV1]",
      "interaction_order": ["NP", 1],
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark"
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2*MV1/(8*Pi)*Sqrt[1 - 4*MT^2/MV1^2]*(1 - MT^2/MV1^2*(1 - 3*Sin[2*thV1]))",
      "tex": "\\Gamma_{V_1}",
      "description": "Width of V1 into a top pair, Eq. (2.2)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "mass": {"sym": "MV1", "value": "1500."},
      "width": {"sym": "WV1", "value": "Internal"},
      "quantum_numbers": {"Q": "0"},
      "pdg": 32,
      "particle_name": "V1",
      "full_name": "Top-philic vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[V1,mu,nu] FS[V1,mu,nu] + 1/2 MV1^2 V1[mu] V1[mu]]]",
      "delayed": true
    },
    {
      "name": "LV1Int",
      "expression": "Block[{mu}, ExpandIndices[tbar.Ga[mu].(cL ProjM + cR ProjP).t V1[mu]]]",
      "delayed": true
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1Kin + LV1Int",
      "delayed": true
    }
  ]
}
```