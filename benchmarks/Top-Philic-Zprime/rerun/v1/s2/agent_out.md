I'll start by reading the paper and the schema.
I have everything I need. The paper defines a single new state: a colour-singlet, electrically neutral massive vector `V1` that couples only to the top quark, with three free parameters (M_V1, c_t, θ).

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
      "value": "2.0",
      "block_name": "TOPPHILIC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "c_t",
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark, ct = Sqrt[cL^2+cR^2]"
    },
    {
      "name": "theta",
      "parameter_type": "External",
      "value": "1.570796326794897",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "\\theta",
      "description": "Chirality angle, tan(theta) = cR/cL; theta = Pi/2 is the purely right-handed case, theta = 3Pi/4 the axial case"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[theta]",
      "interaction_order": ["NP", 1],
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[theta]",
      "interaction_order": ["NP", 1],
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark"
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2*MV1/(8*Pi)*Sqrt[1 - 4*MT^2/MV1^2]*(1 - MT^2/MV1^2*(1 - 3*Sin[2*theta]))",
      "tex": "\\Gamma_{V_1}",
      "description": "Total width of V1, saturated by V1 -> t tbar (Eq. 2.2)"
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
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 32,
      "particle_name": "V1",
      "full_name": "Top-philic vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None",
      "unphysical": false
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "Block[{mu,nu}, -1/4 FS[V1,mu,nu] FS[V1,mu,nu] + 1/2 MV1^2 V1[mu] V1[mu]]",
      "delayed": true
    },
    {
      "name": "LV1Int",
      "expression": "Block[{mu,sp1,sp2,sp3,cc}, ExpandIndices[ct*(Cos[theta]*(tbar[sp1,cc].Ga[mu,sp1,sp2].ProjM[sp2,sp3].t[sp3,cc]) + Sin[theta]*(tbar[sp1,cc].Ga[mu,sp1,sp2].ProjP[sp2,sp3].t[sp3,cc]))*V1[mu]]]",
      "delayed": true
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1Kin + LV1Int",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I have everything I need. The paper defines a single new state: a colour-singlet, electrically neutral massive vector `V1` that couples only to the top quark, with three free parameters (M_V1, c_t, θ).

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
      "value": "2.0",
      "block_name": "TOPPHILIC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "c_t",
      "description": "Overall coupling strength of the top-philic vector resonance V1 to the top quark, ct = Sqrt[cL^2+cR^2]"
    },
    {
      "name": "theta",
      "parameter_type": "External",
      "value": "1.570796326794897",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "\\theta",
      "description": "Chirality angle, tan(theta) = cR/cL; theta = Pi/2 is the purely right-handed case, theta = 3Pi/4 the axial case"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[theta]",
      "interaction_order": ["NP", 1],
      "tex": "c_L",
      "description": "Left-handed coupling of V1 to the top quark"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[theta]",
      "interaction_order": ["NP", 1],
      "tex": "c_R",
      "description": "Right-handed coupling of V1 to the top quark"
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2*MV1/(8*Pi)*Sqrt[1 - 4*MT^2/MV1^2]*(1 - MT^2/MV1^2*(1 - 3*Sin[2*theta]))",
      "tex": "\\Gamma_{V_1}",
      "description": "Total width of V1, saturated by V1 -> t tbar (Eq. 2.2)"
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
      "quantum_numbers": {
        "Q": "0"
      },
      "pdg": 32,
      "particle_name": "V1",
      "full_name": "Top-philic vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None",
      "unphysical": false
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "Block[{mu,nu}, -1/4 FS[V1,mu,nu] FS[V1,mu,nu] + 1/2 MV1^2 V1[mu] V1[mu]]",
      "delayed": true
    },
    {
      "name": "LV1Int",
      "expression": "Block[{mu,sp1,sp2,sp3,cc}, ExpandIndices[ct*(Cos[theta]*(tbar[sp1,cc].Ga[mu,sp1,sp2].ProjM[sp2,sp3].t[sp3,cc]) + Sin[theta]*(tbar[sp1,cc].Ga[mu,sp1,sp2].ProjP[sp2,sp3].t[sp3,cc]))*V1[mu]]]",
      "delayed": true
    },
    {
      "name": "LTopPhilic",
      "expression": "LV1Kin + LV1Int",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```