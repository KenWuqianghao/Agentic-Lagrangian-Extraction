I'll start by reading the paper and the schema.
I have the full new-physics content. The paper defines one new state: a colour-singlet, SU(2)-singlet, neutral vector resonance `V1` that couples only to top quarks.

**Content found:**
- **Particle:** `V1` — spin 1, colour singlet, SU(2) singlet, Q = 0, real (self-conjugate) field, mass `MV1` (benchmark 1.5 TeV).
- **Parameters:** overall coupling `ct`, chirality angle `th` (θ), with derived `cL = ct Cos[θ]` and `cR = ct Sin[θ]` from Eq. (2.1).
- **Lagrangian:** Eq. (2.1) plus the Proca kinetic and mass term.

No other new states appear; the rest of the paper is collider analysis (top tagging, cutflows).

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
      "KAIST and Center for Theoretical Physics of the Universe, IBS",
      "University of Kansas",
      "Korea University and Korea Institute for Advanced Study",
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
    ["QED", 2],
    ["NP", 3]
  ],
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
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark, ct = Sqrt[cL^2 + cR^2] (Eq. 2.1)"
    },
    {
      "name": "th",
      "parameter_type": "External",
      "value": "1.5707963",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "parameter_name": "th",
      "tex": "\\theta",
      "description": "Chirality angle, Tan[th] = cR/cL; th = Pi/2 is the pure right-handed benchmark used in the paper (Eq. 2.1)"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[th]",
      "interaction_order": ["NP", 1],
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark (Eq. 2.1)"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[th]",
      "interaction_order": ["NP", 1],
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark (Eq. 2.1)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "massless": false,
        "sym": "MV1",
        "value": "1500."
      },
      "width": {
        "massless": false,
        "sym": "WV1",
        "value": "229."
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 32,
      "particle_name": "V1",
      "antiparticle_name": "V1",
      "full_name": "TopPhilicVector",
      "propagator_label": "V1",
      "propagator_type": "W",
      "propagator_arrow": "None",
      "unphysical": false
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]",
      "delayed": false
    },
    {
      "name": "LV1Int",
      "expression": "ct (tbar.Ga[mu].(Cos[th] ProjM + Sin[th] ProjP).t) V1[mu]",
      "delayed": false
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1Kin + LV1Int",
      "delayed": false
    }
  ]
}
```
I have the full new-physics content. The paper defines one new state: a colour-singlet, SU(2)-singlet, neutral vector resonance `V1` that couples only to top quarks.

**Content found:**
- **Particle:** `V1` — spin 1, colour singlet, SU(2) singlet, Q = 0, real (self-conjugate) field, mass `MV1` (benchmark 1.5 TeV).
- **Parameters:** overall coupling `ct`, chirality angle `th` (θ), with derived `cL = ct Cos[θ]` and `cR = ct Sin[θ]` from Eq. (2.1).
- **Lagrangian:** Eq. (2.1) plus the Proca kinetic and mass term.

No other new states appear; the rest of the paper is collider analysis (top tagging, cutflows).

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
      "KAIST and Center for Theoretical Physics of the Universe, IBS",
      "University of Kansas",
      "Korea University and Korea Institute for Advanced Study",
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
    ["QED", 2],
    ["NP", 3]
  ],
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
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark, ct = Sqrt[cL^2 + cR^2] (Eq. 2.1)"
    },
    {
      "name": "th",
      "parameter_type": "External",
      "value": "1.5707963",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "parameter_name": "th",
      "tex": "\\theta",
      "description": "Chirality angle, Tan[th] = cR/cL; th = Pi/2 is the pure right-handed benchmark used in the paper (Eq. 2.1)"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[th]",
      "interaction_order": ["NP", 1],
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark (Eq. 2.1)"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[th]",
      "interaction_order": ["NP", 1],
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark (Eq. 2.1)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "indices": [],
      "mass": {
        "massless": false,
        "sym": "MV1",
        "value": "1500."
      },
      "width": {
        "massless": false,
        "sym": "WV1",
        "value": "229."
      },
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 32,
      "particle_name": "V1",
      "antiparticle_name": "V1",
      "full_name": "TopPhilicVector",
      "propagator_label": "V1",
      "propagator_type": "W",
      "propagator_arrow": "None",
      "unphysical": false
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]",
      "delayed": false
    },
    {
      "name": "LV1Int",
      "expression": "ct (tbar.Ga[mu].(Cos[th] ProjM + Sin[th] ProjP).t) V1[mu]",
      "delayed": false
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1Kin + LV1Int",
      "delayed": false
    }
  ]
}
```