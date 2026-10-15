I'll start by reading the paper and the schema.
I've read the paper, the schema, and SM.fr. Here is the extracted model.

**New states:** `WR±` (V, colour singlet, Q=+1, MWR=3000), `ZR` (V, real, MZR=5070), and three heavy Majorana neutrinos `N1,N2,N3` (F, self-conjugate, colour/SU(2) singlets, Q=0) as a 3-member `Generation` class.

**New parameters:** `kqR`, `klR` (External normalizations of Eq. 4/5/8), the RH CKM matrix `VCKMR`, the heavy-neutrino mixing matrix `YLN` (Eq. 5/7), and the derived `ZR` chiral coefficients of Eqs. (9)–(10).

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "27. 10. 2016",
    "institutions": [
      "Universite catholique de Louvain (CP3)",
      "IISER Mohali",
      "IPPP, Durham University"
    ],
    "emails": [
      "olivier.mattelaer@uclouvain.be",
      "manimala@iisermohali.ac.in",
      "richard.ruiz@durham.ac.uk"
    ]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kqR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "EFFLRSM",
      "order_block": 1,
      "tex": "Subscript[\\[Kappa],R]^q",
      "description": "Overall normalization of the right-handed gauge boson coupling to quarks"
    },
    {
      "name": "klR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "EFFLRSM",
      "order_block": 2,
      "tex": "Subscript[\\[Kappa],R]^l",
      "description": "Overall normalization of the right-handed gauge boson coupling to leptons"
    },
    {
      "name": "tw2",
      "parameter_type": "Internal",
      "value": "sw^2/cw^2",
      "tex": "Subsuperscript[t,w,2]",
      "description": "Squared tangent of the Weinberg angle"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "-kqR*gw*Sqrt[1 - tw2/kqR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to quarks, Eq. (8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "-klR*gw*Sqrt[1 - tw2/klR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to leptons, Eq. (8)"
    },
    {
      "name": "gZRLu",
      "parameter_type": "Internal",
      "value": "-tw2/(6*kqR^2)",
      "description": "Left-handed ZR chiral coefficient for up-type quarks, Eq. (9)"
    },
    {
      "name": "gZRRu",
      "parameter_type": "Internal",
      "value": "1/2 - 2/3*tw2/kqR^2",
      "description": "Right-handed ZR chiral coefficient for up-type quarks, Eq. (10)"
    },
    {
      "name": "gZRLd",
      "parameter_type": "Internal",
      "value": "-tw2/(6*kqR^2)",
      "description": "Left-handed ZR chiral coefficient for down-type quarks, Eq. (9)"
    },
    {
      "name": "gZRRd",
      "parameter_type": "Internal",
      "value": "-1/2 + 1/3*tw2/kqR^2",
      "description": "Right-handed ZR chiral coefficient for down-type quarks, Eq. (10)"
    },
    {
      "name": "gZRLe",
      "parameter_type": "Internal",
      "value": "tw2/(2*klR^2)",
      "description": "Left-handed ZR chiral coefficient for charged leptons, Eq. (9)"
    },
    {
      "name": "gZRRe",
      "parameter_type": "Internal",
      "value": "-1/2 + tw2/klR^2",
      "description": "Right-handed ZR chiral coefficient for charged leptons, Eq. (10)"
    },
    {
      "name": "gZRLv",
      "parameter_type": "Internal",
      "value": "tw2/(2*klR^2)",
      "description": "Left-handed ZR chiral coefficient for light neutrinos, Eq. (9)"
    },
    {
      "name": "gZRRv",
      "parameter_type": "Internal",
      "value": "0",
      "description": "Right-handed ZR chiral coefficient for light neutrinos, Eq. (10)"
    },
    {
      "name": "gZRLn",
      "parameter_type": "Internal",
      "value": "0",
      "description": "Left-handed ZR chiral coefficient for heavy Majorana neutrinos, Eq. (9)"
    },
    {
      "name": "gZRRn",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "Right-handed ZR chiral coefficient for heavy Majorana neutrinos, Eq. (10)"
    },
    {
      "name": "VCKMR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "unitary": true,
      "complex": true,
      "value_rules": [
        {"lhs": "VCKMR[1,1]", "rhs": "1"},
        {"lhs": "VCKMR[1,2]", "rhs": "0"},
        {"lhs": "VCKMR[1,3]", "rhs": "0"},
        {"lhs": "VCKMR[2,1]", "rhs": "0"},
        {"lhs": "VCKMR[2,2]", "rhs": "1"},
        {"lhs": "VCKMR[2,3]", "rhs": "0"},
        {"lhs": "VCKMR[3,1]", "rhs": "0"},
        {"lhs": "VCKMR[3,2]", "rhs": "0"},
        {"lhs": "VCKMR[3,3]", "rhs": "1"}
      ],
      "tex": "Superscript[V,CKM']",
      "description": "Right-handed CKM matrix, taken diagonal with unit entries"
    },
    {
      "name": "YLN",
      "parameter_type": "External",
      "block_name": "LNMIXING",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "YLN[1,1]", "rhs": "1."},
        {"lhs": "YLN[1,2]", "rhs": "0."},
        {"lhs": "YLN[1,3]", "rhs": "0."},
        {"lhs": "YLN[2,1]", "rhs": "0."},
        {"lhs": "YLN[2,2]", "rhs": "1."},
        {"lhs": "YLN[2,3]", "rhs": "0."},
        {"lhs": "YLN[3,1]", "rhs": "0."},
        {"lhs": "YLN[3,2]", "rhs": "0."},
        {"lhs": "YLN[3,3]", "rhs": "1."}
      ],
      "tex": "Subscript[Y,\\[ScriptL]m]",
      "description": "Mixing between the heavy mass eigenstate N and the RH chiral state of lepton flavour l, Eq. (5)"
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
      "pdg": 9000024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "WR",
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
      "quantum_numbers": {"Q": "0"},
      "pdg": 9000023,
      "particle_name": "zr",
      "full_name": "ZR",
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
        "sym": "MNR",
        "members": [
          ["MN1", "173.3"],
          ["MN2", "1.*^12"],
          ["MN3", "1.*^12"]
        ]
      },
      "width": {
        "sym": "WNR",
        "members": [
          ["WN1", "2.12*^-8"],
          ["WN2", "0."],
          ["WN3", "0."]
        ]
      },
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "antiparticle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["NR", "n1", "n2", "n3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LVRkin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[ -1/2 FS[WRbar,mu,nu] FS[WR,mu,nu] + MWR^2 WRbar[mu] WR[mu] - 1/4 FS[ZR,mu,nu] FS[ZR,mu,nu] + 1/2 MZR^2 ZR[mu] ZR[mu] ]]"
    },
    {
      "name": "LNRkin",
      "delayed": true,
      "expression": "Block[{mu,ff}, ExpandIndices[ I/2 NRbar[ff].Ga[mu].del[NR[ff],mu] - 1/2 MNR[ff] NRbar[ff].NR[ff] ]]"
    },
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "Block[{mu,ff1,ff2,cc}, ExpandIndices[ -(kqR*gw/Sqrt[2]) VCKMR[ff1,ff2] (uqbar[ff1,cc].Ga[mu].ProjP.dq[ff2,cc]) WR[mu] ]]"
    },
    {
      "name": "LWRl",
      "delayed": true,
      "expression": "Block[{mu,ff1,ff2}, ExpandIndices[ -(klR*gw/Sqrt[2]) YLN[ff1,ff2] (NRbar[ff2].Ga[mu].ProjP.l[ff1]) WR[mu] ]]"
    },
    {
      "name": "LZRff",
      "delayed": true,
      "expression": "Block[{mu,ff,cc}, ExpandIndices[ gZRq ( uqbar[ff,cc].Ga[mu].(gZRLu ProjM + gZRRu ProjP).uq[ff,cc] + dqbar[ff,cc].Ga[mu].(gZRLd ProjM + gZRRd ProjP).dq[ff,cc] ) ZR[mu] + gZRl ( lbar[ff].Ga[mu].(gZRLe ProjM + gZRRe ProjP).l[ff] + vlbar[ff].Ga[mu].(gZRLv ProjM + gZRRv ProjP).vl[ff] + 1/2 NRbar[ff].Ga[mu].(gZRLn ProjM + gZRRn ProjP).NR[ff] ) ZR[mu] ]]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LVRkin + LNRkin + LWRq + HC[LWRq] + LWRl + HC[LWRl] + LZRff"
    }
  ]
}
```
I've read the paper, the schema, and SM.fr. Here is the extracted model.

**New states:** `WR±` (V, colour singlet, Q=+1, MWR=3000), `ZR` (V, real, MZR=5070), and three heavy Majorana neutrinos `N1,N2,N3` (F, self-conjugate, colour/SU(2) singlets, Q=0) as a 3-member `Generation` class.

**New parameters:** `kqR`, `klR` (External normalizations of Eq. 4/5/8), the RH CKM matrix `VCKMR`, the heavy-neutrino mixing matrix `YLN` (Eq. 5/7), and the derived `ZR` chiral coefficients of Eqs. (9)–(10).

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "27. 10. 2016",
    "institutions": [
      "Universite catholique de Louvain (CP3)",
      "IISER Mohali",
      "IPPP, Durham University"
    ],
    "emails": [
      "olivier.mattelaer@uclouvain.be",
      "manimala@iisermohali.ac.in",
      "richard.ruiz@durham.ac.uk"
    ]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kqR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "EFFLRSM",
      "order_block": 1,
      "tex": "Subscript[\\[Kappa],R]^q",
      "description": "Overall normalization of the right-handed gauge boson coupling to quarks"
    },
    {
      "name": "klR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "EFFLRSM",
      "order_block": 2,
      "tex": "Subscript[\\[Kappa],R]^l",
      "description": "Overall normalization of the right-handed gauge boson coupling to leptons"
    },
    {
      "name": "tw2",
      "parameter_type": "Internal",
      "value": "sw^2/cw^2",
      "tex": "Subsuperscript[t,w,2]",
      "description": "Squared tangent of the Weinberg angle"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "-kqR*gw*Sqrt[1 - tw2/kqR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to quarks, Eq. (8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "-klR*gw*Sqrt[1 - tw2/klR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to leptons, Eq. (8)"
    },
    {
      "name": "gZRLu",
      "parameter_type": "Internal",
      "value": "-tw2/(6*kqR^2)",
      "description": "Left-handed ZR chiral coefficient for up-type quarks, Eq. (9)"
    },
    {
      "name": "gZRRu",
      "parameter_type": "Internal",
      "value": "1/2 - 2/3*tw2/kqR^2",
      "description": "Right-handed ZR chiral coefficient for up-type quarks, Eq. (10)"
    },
    {
      "name": "gZRLd",
      "parameter_type": "Internal",
      "value": "-tw2/(6*kqR^2)",
      "description": "Left-handed ZR chiral coefficient for down-type quarks, Eq. (9)"
    },
    {
      "name": "gZRRd",
      "parameter_type": "Internal",
      "value": "-1/2 + 1/3*tw2/kqR^2",
      "description": "Right-handed ZR chiral coefficient for down-type quarks, Eq. (10)"
    },
    {
      "name": "gZRLe",
      "parameter_type": "Internal",
      "value": "tw2/(2*klR^2)",
      "description": "Left-handed ZR chiral coefficient for charged leptons, Eq. (9)"
    },
    {
      "name": "gZRRe",
      "parameter_type": "Internal",
      "value": "-1/2 + tw2/klR^2",
      "description": "Right-handed ZR chiral coefficient for charged leptons, Eq. (10)"
    },
    {
      "name": "gZRLv",
      "parameter_type": "Internal",
      "value": "tw2/(2*klR^2)",
      "description": "Left-handed ZR chiral coefficient for light neutrinos, Eq. (9)"
    },
    {
      "name": "gZRRv",
      "parameter_type": "Internal",
      "value": "0",
      "description": "Right-handed ZR chiral coefficient for light neutrinos, Eq. (10)"
    },
    {
      "name": "gZRLn",
      "parameter_type": "Internal",
      "value": "0",
      "description": "Left-handed ZR chiral coefficient for heavy Majorana neutrinos, Eq. (9)"
    },
    {
      "name": "gZRRn",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "Right-handed ZR chiral coefficient for heavy Majorana neutrinos, Eq. (10)"
    },
    {
      "name": "VCKMR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "unitary": true,
      "complex": true,
      "value_rules": [
        {"lhs": "VCKMR[1,1]", "rhs": "1"},
        {"lhs": "VCKMR[1,2]", "rhs": "0"},
        {"lhs": "VCKMR[1,3]", "rhs": "0"},
        {"lhs": "VCKMR[2,1]", "rhs": "0"},
        {"lhs": "VCKMR[2,2]", "rhs": "1"},
        {"lhs": "VCKMR[2,3]", "rhs": "0"},
        {"lhs": "VCKMR[3,1]", "rhs": "0"},
        {"lhs": "VCKMR[3,2]", "rhs": "0"},
        {"lhs": "VCKMR[3,3]", "rhs": "1"}
      ],
      "tex": "Superscript[V,CKM']",
      "description": "Right-handed CKM matrix, taken diagonal with unit entries"
    },
    {
      "name": "YLN",
      "parameter_type": "External",
      "block_name": "LNMIXING",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "YLN[1,1]", "rhs": "1."},
        {"lhs": "YLN[1,2]", "rhs": "0."},
        {"lhs": "YLN[1,3]", "rhs": "0."},
        {"lhs": "YLN[2,1]", "rhs": "0."},
        {"lhs": "YLN[2,2]", "rhs": "1."},
        {"lhs": "YLN[2,3]", "rhs": "0."},
        {"lhs": "YLN[3,1]", "rhs": "0."},
        {"lhs": "YLN[3,2]", "rhs": "0."},
        {"lhs": "YLN[3,3]", "rhs": "1."}
      ],
      "tex": "Subscript[Y,\\[ScriptL]m]",
      "description": "Mixing between the heavy mass eigenstate N and the RH chiral state of lepton flavour l, Eq. (5)"
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
      "pdg": 9000024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "WR",
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
      "quantum_numbers": {"Q": "0"},
      "pdg": 9000023,
      "particle_name": "zr",
      "full_name": "ZR",
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
        "sym": "MNR",
        "members": [
          ["MN1", "173.3"],
          ["MN2", "1.*^12"],
          ["MN3", "1.*^12"]
        ]
      },
      "width": {
        "sym": "WNR",
        "members": [
          ["WN1", "2.12*^-8"],
          ["WN2", "0."],
          ["WN3", "0."]
        ]
      },
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "antiparticle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["NR", "n1", "n2", "n3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LVRkin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[ -1/2 FS[WRbar,mu,nu] FS[WR,mu,nu] + MWR^2 WRbar[mu] WR[mu] - 1/4 FS[ZR,mu,nu] FS[ZR,mu,nu] + 1/2 MZR^2 ZR[mu] ZR[mu] ]]"
    },
    {
      "name": "LNRkin",
      "delayed": true,
      "expression": "Block[{mu,ff}, ExpandIndices[ I/2 NRbar[ff].Ga[mu].del[NR[ff],mu] - 1/2 MNR[ff] NRbar[ff].NR[ff] ]]"
    },
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "Block[{mu,ff1,ff2,cc}, ExpandIndices[ -(kqR*gw/Sqrt[2]) VCKMR[ff1,ff2] (uqbar[ff1,cc].Ga[mu].ProjP.dq[ff2,cc]) WR[mu] ]]"
    },
    {
      "name": "LWRl",
      "delayed": true,
      "expression": "Block[{mu,ff1,ff2}, ExpandIndices[ -(klR*gw/Sqrt[2]) YLN[ff1,ff2] (NRbar[ff2].Ga[mu].ProjP.l[ff1]) WR[mu] ]]"
    },
    {
      "name": "LZRff",
      "delayed": true,
      "expression": "Block[{mu,ff,cc}, ExpandIndices[ gZRq ( uqbar[ff,cc].Ga[mu].(gZRLu ProjM + gZRRu ProjP).uq[ff,cc] + dqbar[ff,cc].Ga[mu].(gZRLd ProjM + gZRRd ProjP).dq[ff,cc] ) ZR[mu] + gZRl ( lbar[ff].Ga[mu].(gZRLe ProjM + gZRRe ProjP).l[ff] + vlbar[ff].Ga[mu].(gZRLv ProjM + gZRRv ProjP).vl[ff] + 1/2 NRbar[ff].Ga[mu].(gZRLn ProjM + gZRRn ProjP).NR[ff] ) ZR[mu] ]]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LVRkin + LNRkin + LWRq + HC[LWRq] + LWRl + HC[LWRl] + LZRff"
    }
  ]
}
```