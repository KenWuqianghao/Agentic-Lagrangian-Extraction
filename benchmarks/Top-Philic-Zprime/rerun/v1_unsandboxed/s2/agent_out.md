I'll start by reading the paper and the schema.
I read the paper and the schema. The paper is a simplified model: one new state, a colour-singlet neutral vector resonance V1 that couples only to the top quark, with three free parameters (MV1, ct, θ).

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
      "KAIST and CTPU, Institute for Basic Science",
      "University of Kansas",
      "Korea University and KIAS",
      "Fermilab"
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
    ["NP", 1],
    ["QED", 2]
  ],
  "interaction_order_limit": [],
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
      "parameter_name": "ct",
      "tex": "c_t",
      "description": "Overall coupling strength of the top-philic vector resonance to the top quark, ct = Sqrt[cL^2 + cR^2]"
    },
    {
      "name": "th",
      "parameter_type": "External",
      "value": "1.570796326794897",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "parameter_name": "th",
      "tex": "\\theta",
      "description": "Chirality angle theta, with Tan[th] = cR/cL. The paper uses th = Pi/2 (pure right-handed); th = 3 Pi/4 is the axial limit"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[th]",
      "interaction_order": ["NP", 1],
      "parameter_name": "cL",
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[th]",
      "interaction_order": ["NP", 1],
      "parameter_name": "cR",
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "mass": {
        "massless": false,
        "sym": "MV1",
        "value": "1500."
      },
      "width": {
        "massless": false,
        "sym": "WV1",
        "value": "229.3"
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 5000001,
      "particle_name": "v1",
      "full_name": "Top-philic vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]",
      "delayed": true
    },
    {
      "name": "LV1Top",
      "expression": "tbar.Ga[mu].(cL ProjM + cR ProjP).t V1[mu]",
      "delayed": true
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1Kin + LV1Top",
      "delayed": true
    }
  ]
}
```
I read the paper and the schema. The paper is a simplified model: one new state, a colour-singlet neutral vector resonance V1 that couples only to the top quark, with three free parameters (MV1, ct, θ).

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
      "KAIST and CTPU, Institute for Basic Science",
      "University of Kansas",
      "Korea University and KIAS",
      "Fermilab"
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
    ["NP", 1],
    ["QED", 2]
  ],
  "interaction_order_limit": [],
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
      "parameter_name": "ct",
      "tex": "c_t",
      "description": "Overall coupling strength of the top-philic vector resonance to the top quark, ct = Sqrt[cL^2 + cR^2]"
    },
    {
      "name": "th",
      "parameter_type": "External",
      "value": "1.570796326794897",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "parameter_name": "th",
      "tex": "\\theta",
      "description": "Chirality angle theta, with Tan[th] = cR/cL. The paper uses th = Pi/2 (pure right-handed); th = 3 Pi/4 is the axial limit"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[th]",
      "interaction_order": ["NP", 1],
      "parameter_name": "cL",
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[th]",
      "interaction_order": ["NP", 1],
      "parameter_name": "cR",
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "mass": {
        "massless": false,
        "sym": "MV1",
        "value": "1500."
      },
      "width": {
        "massless": false,
        "sym": "WV1",
        "value": "229.3"
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 5000001,
      "particle_name": "v1",
      "full_name": "Top-philic vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]",
      "delayed": true
    },
    {
      "name": "LV1Top",
      "expression": "tbar.Ga[mu].(cL ProjM + cR ProjP).t V1[mu]",
      "delayed": true
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1Kin + LV1Top",
      "delayed": true
    }
  ]
}
```