I'll start by reading the paper, schema, and SM file.
The physics model is in Section II. Let me check the remainder for any further model details, and read SM.fr.
I have everything I need. Here is the extracted model.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": [
      "A. Das",
      "P. S. Bhupal Dev",
      "Y. Hosotani",
      "S. Mandal"
    ],
    "version": "1.0",
    "date": "21. 06. 2022",
    "institutions": [
      "Kyungpook National University / Hokkaido University",
      "Washington University in St. Louis",
      "Osaka University",
      "IFIC, CSIC/Universitat de Valencia"
    ],
    "emails": [
      "arindamdas@oia.hokudai.ac.jp",
      "bdev@wustl.edu",
      "hosotani@het.phys.sci.osaka-u.ac.jp",
      "smandal@ific.uv.es"
    ]
  },
  "interaction_order_hierarchy": [
    ["QCD", 1],
    ["QED", 2],
    ["NP", 1]
  ],
  "vevs": [
    ["Phi[2]", "vev"],
    ["PhiX", "vevX"]
  ],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "BSMINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g_X",
      "description": "U(1)X gauge coupling g'"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "BSMINPUTS",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)X charge parameter of the SM Higgs doublet"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "BSMINPUTS",
      "order_block": 3,
      "tex": "x_\\Phi",
      "description": "U(1)X charge parameter of the singlet scalar Phi"
    },
    {
      "name": "vevX",
      "parameter_type": "External",
      "value": "9375.",
      "block_name": "BSMINPUTS",
      "order_block": 4,
      "tex": "v_\\Phi",
      "description": "Vacuum expectation value of the U(1)X singlet scalar Phi"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.001",
      "block_name": "BSMINPUTS",
      "order_block": 5,
      "tex": "\\lambda'",
      "description": "Portal quartic coupling between the SM Higgs doublet and Phi"
    },
    {
      "name": "ynu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "YUKNU",
      "value_rules": [
        {"lhs": "ynu[1,1]", "rhs": "1.*^-7"},
        {"lhs": "ynu[1,2]", "rhs": "0."},
        {"lhs": "ynu[1,3]", "rhs": "0."},
        {"lhs": "ynu[2,1]", "rhs": "0."},
        {"lhs": "ynu[2,2]", "rhs": "1.*^-7"},
        {"lhs": "ynu[2,3]", "rhs": "0."},
        {"lhs": "ynu[3,1]", "rhs": "0."},
        {"lhs": "ynu[3,2]", "rhs": "0."},
        {"lhs": "ynu[3,3]", "rhs": "1.*^-7"}
      ],
      "interaction_order": ["QED", 1],
      "tex": "y_\\nu",
      "description": "Dirac Yukawa coupling of the right-handed neutrinos"
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "gX*Sqrt[4*xPhi^2*vevX^2 + xH^2*vev^2/4]",
      "tex": "M_{Z'}",
      "description": "Mass of the Z' gauge boson of U(1)X"
    },
    {
      "name": "lamX",
      "parameter_type": "Internal",
      "value": "MHx^2/(2*vevX^2)",
      "tex": "\\lambda_\\Phi",
      "description": "Quartic self coupling of the U(1)X singlet scalar Phi"
    },
    {
      "name": "muX",
      "parameter_type": "Internal",
      "value": "Sqrt[vevX^2*lamX]",
      "tex": "m_\\Phi",
      "description": "Quadratic mass term of the U(1)X singlet scalar potential"
    },
    {
      "name": "xQ",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)X charge of the left-handed quark doublet"
    },
    {
      "name": "xU",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed up-type quarks"
    },
    {
      "name": "xD",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed down-type quarks"
    },
    {
      "name": "xL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)X charge of the left-handed lepton doublet"
    },
    {
      "name": "xE",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)X charge of the right-handed charged leptons"
    },
    {
      "name": "xN",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)X charge of the right-handed neutrinos"
    },
    {
      "name": "xHd",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)X charge of the SM Higgs doublet"
    },
    {
      "name": "xS",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "description": "U(1)X charge of the singlet scalar Phi"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "yN[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "yN[1,1]", "rhs": "Sqrt[2] MN1/vevX"},
        {"lhs": "yN[2,2]", "rhs": "Sqrt[2] MN2/vevX"},
        {"lhs": "yN[3,3]", "rhs": "Sqrt[2] MN3/vevX"}
      ],
      "interaction_order": ["QED", 1],
      "tex": "y_N",
      "description": "Majorana Yukawa coupling of the right-handed neutrinos to Phi"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 5,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "100."},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "U(1)X gauge boson Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 5,
      "class_name": "vR",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MN",
        "members": [
          ["MN1", "10000."],
          ["MN2", "10000."],
          ["MN3", "10000."]
        ]
      },
      "width": {
        "sym": "WN",
        "members": [
          ["WN1", "1."],
          ["WN2", "1."],
          ["WN3", "1."]
        ]
      },
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": [
        "Right-handed neutrino 1",
        "Right-handed neutrino 2",
        "Right-handed neutrino 3"
      ],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "Hx",
      "self_conjugate": true,
      "mass": {"sym": "MHx", "value": "500."},
      "width": {"sym": "WHx", "value": "1."},
      "pdg": 9900025,
      "particle_name": "Hx",
      "full_name": "U(1)X singlet Higgs boson phi",
      "propagator_label": "Hx",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "G0x",
      "self_conjugate": true,
      "goldstone": "Zp",
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "100."},
      "pdg": 9900250,
      "particle_name": "G0x",
      "full_name": "Goldstone boson of the Zprime",
      "propagator_label": "G0x",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 16,
      "class_name": "NR",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "quantum_numbers": {"Y": "0"},
      "unphysical": true,
      "definitions": [
        "NR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] vR[sp2,ff]]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 12,
      "class_name": "PhiX",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "0"},
      "unphysical": true,
      "definitions": [
        "PhiX -> (vevX + Hx + I G0x)/Sqrt[2]"
      ]
    }
  ],
  "gauge_xi": [
    ["V[5]", "GaugeXi[Zp]"],
    ["S[5]", "GaugeXi[Zp]"]
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu]]]"
    },
    {
      "name": "LNKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I NRbar.Ga[mu].del[NR,mu]]]"
    },
    {
      "name": "LFermionZp",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[- gX Zp[mu] (xQ QLbar.Ga[mu].QL + xU uRbar.Ga[mu].uR + xD dRbar.Ga[mu].dR + xL LLbar.Ga[mu].LL + xE lRbar.Ga[mu].lR + xN NRbar.Ga[mu].NR), FlavorExpand->{SU2W,SU2D}]]"
    },
    {
      "name": "LScalarX",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[(del[PhiXbar,mu] - I gX xS PhiXbar Zp[mu]) (del[PhiX,mu] + I gX xS PhiX Zp[mu]) + muX^2 PhiXbar PhiX - lamX PhiXbar PhiX PhiXbar PhiX]]"
    },
    {
      "name": "LHiggsZp",
      "delayed": true,
      "expression": "Block[{ii,mu}, ExpandIndices[I gX xHd Zp[mu] (Phibar[ii] DC[Phi[ii],mu] - DC[Phibar[ii],mu] Phi[ii]) + gX^2 xHd^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii], FlavorExpand->{SU2D,SU2W}]]"
    },
    {
      "name": "LPortal",
      "delayed": true,
      "expression": "Block[{ii}, ExpandIndices[- lamHX Phibar[ii] Phi[ii] PhiXbar PhiX, FlavorExpand->SU2D]]"
    },
    {
      "name": "LYukawaX",
      "delayed": true,
      "expression": "Block[{sp,ii,jj,ff1,ff2,yuk}, yuk = ExpandIndices[- ynu[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj] - 1/2 yN[ff1,ff2] PhiX NRbar[sp,ff1].NR[sp,ff2], FlavorExpand->SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LU1X",
      "delayed": true,
      "expression": "LZpKin + LNKin + LFermionZp + LScalarX + LHiggsZp + LPortal + LYukawaX"
    }
  ]
}
```
I have everything I need. Here is the extracted model.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": [
      "A. Das",
      "P. S. Bhupal Dev",
      "Y. Hosotani",
      "S. Mandal"
    ],
    "version": "1.0",
    "date": "21. 06. 2022",
    "institutions": [
      "Kyungpook National University / Hokkaido University",
      "Washington University in St. Louis",
      "Osaka University",
      "IFIC, CSIC/Universitat de Valencia"
    ],
    "emails": [
      "arindamdas@oia.hokudai.ac.jp",
      "bdev@wustl.edu",
      "hosotani@het.phys.sci.osaka-u.ac.jp",
      "smandal@ific.uv.es"
    ]
  },
  "interaction_order_hierarchy": [
    ["QCD", 1],
    ["QED", 2],
    ["NP", 1]
  ],
  "vevs": [
    ["Phi[2]", "vev"],
    ["PhiX", "vevX"]
  ],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "BSMINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g_X",
      "description": "U(1)X gauge coupling g'"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "BSMINPUTS",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)X charge parameter of the SM Higgs doublet"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "BSMINPUTS",
      "order_block": 3,
      "tex": "x_\\Phi",
      "description": "U(1)X charge parameter of the singlet scalar Phi"
    },
    {
      "name": "vevX",
      "parameter_type": "External",
      "value": "9375.",
      "block_name": "BSMINPUTS",
      "order_block": 4,
      "tex": "v_\\Phi",
      "description": "Vacuum expectation value of the U(1)X singlet scalar Phi"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.001",
      "block_name": "BSMINPUTS",
      "order_block": 5,
      "tex": "\\lambda'",
      "description": "Portal quartic coupling between the SM Higgs doublet and Phi"
    },
    {
      "name": "ynu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "YUKNU",
      "value_rules": [
        {"lhs": "ynu[1,1]", "rhs": "1.*^-7"},
        {"lhs": "ynu[1,2]", "rhs": "0."},
        {"lhs": "ynu[1,3]", "rhs": "0."},
        {"lhs": "ynu[2,1]", "rhs": "0."},
        {"lhs": "ynu[2,2]", "rhs": "1.*^-7"},
        {"lhs": "ynu[2,3]", "rhs": "0."},
        {"lhs": "ynu[3,1]", "rhs": "0."},
        {"lhs": "ynu[3,2]", "rhs": "0."},
        {"lhs": "ynu[3,3]", "rhs": "1.*^-7"}
      ],
      "interaction_order": ["QED", 1],
      "tex": "y_\\nu",
      "description": "Dirac Yukawa coupling of the right-handed neutrinos"
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "gX*Sqrt[4*xPhi^2*vevX^2 + xH^2*vev^2/4]",
      "tex": "M_{Z'}",
      "description": "Mass of the Z' gauge boson of U(1)X"
    },
    {
      "name": "lamX",
      "parameter_type": "Internal",
      "value": "MHx^2/(2*vevX^2)",
      "tex": "\\lambda_\\Phi",
      "description": "Quartic self coupling of the U(1)X singlet scalar Phi"
    },
    {
      "name": "muX",
      "parameter_type": "Internal",
      "value": "Sqrt[vevX^2*lamX]",
      "tex": "m_\\Phi",
      "description": "Quadratic mass term of the U(1)X singlet scalar potential"
    },
    {
      "name": "xQ",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)X charge of the left-handed quark doublet"
    },
    {
      "name": "xU",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed up-type quarks"
    },
    {
      "name": "xD",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed down-type quarks"
    },
    {
      "name": "xL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)X charge of the left-handed lepton doublet"
    },
    {
      "name": "xE",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)X charge of the right-handed charged leptons"
    },
    {
      "name": "xN",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)X charge of the right-handed neutrinos"
    },
    {
      "name": "xHd",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)X charge of the SM Higgs doublet"
    },
    {
      "name": "xS",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "description": "U(1)X charge of the singlet scalar Phi"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "yN[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "yN[1,1]", "rhs": "Sqrt[2] MN1/vevX"},
        {"lhs": "yN[2,2]", "rhs": "Sqrt[2] MN2/vevX"},
        {"lhs": "yN[3,3]", "rhs": "Sqrt[2] MN3/vevX"}
      ],
      "interaction_order": ["QED", 1],
      "tex": "y_N",
      "description": "Majorana Yukawa coupling of the right-handed neutrinos to Phi"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 5,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "100."},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "U(1)X gauge boson Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 5,
      "class_name": "vR",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MN",
        "members": [
          ["MN1", "10000."],
          ["MN2", "10000."],
          ["MN3", "10000."]
        ]
      },
      "width": {
        "sym": "WN",
        "members": [
          ["WN1", "1."],
          ["WN2", "1."],
          ["WN3", "1."]
        ]
      },
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": [
        "Right-handed neutrino 1",
        "Right-handed neutrino 2",
        "Right-handed neutrino 3"
      ],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "Hx",
      "self_conjugate": true,
      "mass": {"sym": "MHx", "value": "500."},
      "width": {"sym": "WHx", "value": "1."},
      "pdg": 9900025,
      "particle_name": "Hx",
      "full_name": "U(1)X singlet Higgs boson phi",
      "propagator_label": "Hx",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "G0x",
      "self_conjugate": true,
      "goldstone": "Zp",
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "100."},
      "pdg": 9900250,
      "particle_name": "G0x",
      "full_name": "Goldstone boson of the Zprime",
      "propagator_label": "G0x",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 16,
      "class_name": "NR",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "quantum_numbers": {"Y": "0"},
      "unphysical": true,
      "definitions": [
        "NR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] vR[sp2,ff]]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 12,
      "class_name": "PhiX",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "0"},
      "unphysical": true,
      "definitions": [
        "PhiX -> (vevX + Hx + I G0x)/Sqrt[2]"
      ]
    }
  ],
  "gauge_xi": [
    ["V[5]", "GaugeXi[Zp]"],
    ["S[5]", "GaugeXi[Zp]"]
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu]]]"
    },
    {
      "name": "LNKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I NRbar.Ga[mu].del[NR,mu]]]"
    },
    {
      "name": "LFermionZp",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[- gX Zp[mu] (xQ QLbar.Ga[mu].QL + xU uRbar.Ga[mu].uR + xD dRbar.Ga[mu].dR + xL LLbar.Ga[mu].LL + xE lRbar.Ga[mu].lR + xN NRbar.Ga[mu].NR), FlavorExpand->{SU2W,SU2D}]]"
    },
    {
      "name": "LScalarX",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[(del[PhiXbar,mu] - I gX xS PhiXbar Zp[mu]) (del[PhiX,mu] + I gX xS PhiX Zp[mu]) + muX^2 PhiXbar PhiX - lamX PhiXbar PhiX PhiXbar PhiX]]"
    },
    {
      "name": "LHiggsZp",
      "delayed": true,
      "expression": "Block[{ii,mu}, ExpandIndices[I gX xHd Zp[mu] (Phibar[ii] DC[Phi[ii],mu] - DC[Phibar[ii],mu] Phi[ii]) + gX^2 xHd^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii], FlavorExpand->{SU2D,SU2W}]]"
    },
    {
      "name": "LPortal",
      "delayed": true,
      "expression": "Block[{ii}, ExpandIndices[- lamHX Phibar[ii] Phi[ii] PhiXbar PhiX, FlavorExpand->SU2D]]"
    },
    {
      "name": "LYukawaX",
      "delayed": true,
      "expression": "Block[{sp,ii,jj,ff1,ff2,yuk}, yuk = ExpandIndices[- ynu[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj] - 1/2 yN[ff1,ff2] PhiX NRbar[sp,ff1].NR[sp,ff2], FlavorExpand->SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LU1X",
      "delayed": true,
      "expression": "LZpKin + LNKin + LFermionZp + LScalarX + LHiggsZp + LPortal + LYukawaX"
    }
  ]
}
```