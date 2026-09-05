I'll start by reading the paper and the schema.
I have the model content (Sec. II). Let me check the rest for any appendix with model details.
I've read the paper's model section (Sec. II, Table I/II, Eqs. 1–9) and the schema. Here is the extracted model.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": [
      "Arindam Das",
      "P. S. Bhupal Dev",
      "Yutaka Hosotani",
      "Sanjoy Mandal"
    ],
    "version": "1.0",
    "date": "2021-04-22",
    "institutions": [
      "Kyungpook National University",
      "Hokkaido University",
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
  "interaction_order_hierarchy": [["NP", 1]],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "GENERALU1",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g'",
      "description": "U(1)X gauge coupling g'"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "GENERALU1",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)X charge parameter of the SM Higgs doublet direction; xH=0 gives B-L, xH=-2 gives U(1)R"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "GENERALU1",
      "order_block": 3,
      "tex": "x_\\Phi",
      "description": "U(1)X charge parameter of the singlet scalar direction; fixed to 1 in the paper"
    },
    {
      "name": "vX",
      "parameter_type": "External",
      "value": "9375.",
      "block_name": "GENERALU1",
      "order_block": 4,
      "tex": "v_\\Phi",
      "description": "U(1)X breaking VEV of the SM-singlet scalar PhiX"
    },
    {
      "name": "lamPhi",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "GENERALU1",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "tex": "\\lambda_\\Phi",
      "description": "quartic self coupling of the singlet scalar"
    },
    {
      "name": "lamHPhi",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "GENERALU1",
      "order_block": 6,
      "interaction_order": ["NP", 1],
      "tex": "\\lambda'",
      "description": "portal quartic coupling between the SM Higgs doublet and the singlet scalar"
    },
    {
      "name": "ynu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "YUKNU",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "ynu[1,1]", "rhs": "1.*^-7"},
        {"lhs": "ynu[2,2]", "rhs": "1.*^-7"},
        {"lhs": "ynu[3,3]", "rhs": "1.*^-7"}
      ],
      "tex": "Y_\\nu",
      "description": "Dirac neutrino Yukawa coupling matrix, lLbar H NR"
    },
    {
      "name": "xqL",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "tex": "q_x^{q_L}",
      "description": "U(1)X charge of the left-handed quark doublet"
    },
    {
      "name": "xuR",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "tex": "q_x^{u_R}",
      "description": "U(1)X charge of the right-handed up-type quarks"
    },
    {
      "name": "xdR",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "tex": "q_x^{d_R}",
      "description": "U(1)X charge of the right-handed down-type quarks"
    },
    {
      "name": "xlL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "tex": "q_x^{\\ell_L}",
      "description": "U(1)X charge of the left-handed lepton doublet"
    },
    {
      "name": "xeR",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "tex": "q_x^{e_R}",
      "description": "U(1)X charge of the right-handed charged leptons"
    },
    {
      "name": "xnR",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "tex": "q_x^{N_R}",
      "description": "U(1)X charge of the right-handed neutrinos"
    },
    {
      "name": "xHX",
      "parameter_type": "Internal",
      "value": "-xH/2",
      "tex": "q_x^{H}",
      "description": "U(1)X charge of the SM Higgs doublet"
    },
    {
      "name": "xPhiX",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "tex": "q_x^{\\Phi}",
      "description": "U(1)X charge of the SM-singlet scalar PhiX"
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "gX*Sqrt[4*xPhi^2*vX^2 + xH^2*vev^2/4]",
      "tex": "M_{Z'}",
      "description": "mass of the U(1)X gauge boson Z', Eq. (4)"
    },
    {
      "name": "muPhi2",
      "parameter_type": "Internal",
      "value": "-lamPhi*vX^2",
      "tex": "m_\\Phi^2",
      "description": "singlet scalar mass-squared term fixed by the minimisation condition"
    },
    {
      "name": "MhX",
      "parameter_type": "Internal",
      "value": "Sqrt[2*lamPhi]*vX",
      "tex": "m_\\phi",
      "description": "mass of the physical CP-even singlet scalar phi"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "yN[1]", "rhs": "Sqrt[2]*MN1/vX"},
        {"lhs": "yN[2]", "rhs": "Sqrt[2]*MN2/vX"},
        {"lhs": "yN[3]", "rhs": "Sqrt[2]*MN3/vX"}
      ],
      "tex": "Y_N",
      "description": "Majorana Yukawa coupling of the right-handed neutrinos to PhiX"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "50."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "Zp",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NR",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MN",
        "members": [["MN1", "10000."], ["MN2", "10000."], ["MN3", "10000."]]
      },
      "width": {
        "sym": "WN",
        "members": [["WN1", "1."], ["WN2", "1."], ["WN3", "1."]]
      },
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["N1", "N2", "N3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "hX",
      "self_conjugate": true,
      "mass": {"sym": "MhX", "value": "Internal"},
      "width": {"sym": "WhX", "value": "1."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900025,
      "particle_name": "hX",
      "full_name": "hX",
      "propagator_label": "hX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "GZp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "Internal"},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900026,
      "particle_name": "GZp",
      "full_name": "GZp",
      "propagator_label": "GZp",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "goldstone": "Zp"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "PhiX",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Q": "0"},
      "definitions": [
        "PhiX -> (vX + hX + I*GZp)/Sqrt[2]"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "expression": "-1/4 FS[Zp, mu, nu] FS[Zp, mu, nu]"
    },
    {
      "name": "LZpFerm",
      "expression": "-gX Zp[mu] ( xqL (uqbar.Ga[mu].ProjM.uq + dqbar.Ga[mu].ProjM.dq) + xuR uqbar.Ga[mu].ProjP.uq + xdR dqbar.Ga[mu].ProjP.dq + xlL (vlbar.Ga[mu].ProjM.vl + lbar.Ga[mu].ProjM.l) + xeR lbar.Ga[mu].ProjP.l + xnR NRbar.Ga[mu].ProjP.NR )"
    },
    {
      "name": "LNKin",
      "expression": "I/2 NRbar.Ga[mu].del[NR, mu]"
    },
    {
      "name": "LPhiXKin",
      "expression": "(del[PhiXbar, mu] + I*gX*xPhiX*Zp[mu]*PhiXbar) (del[PhiX, mu] - I*gX*xPhiX*Zp[mu]*PhiX)"
    },
    {
      "name": "LHX",
      "expression": "I*gX*xHX*Zp[mu] (Phibar[ii] del[Phi[ii], mu] - del[Phibar[ii], mu] Phi[ii]) + gX^2*xHX^2*Zp[mu] Zp[mu] Phibar[ii] Phi[ii]"
    },
    {
      "name": "LPhiXPot",
      "expression": "-muPhi2 PhiXbar PhiX - lamPhi (PhiXbar PhiX)^2 - lamHPhi (Phibar[ii] Phi[ii]) (PhiXbar PhiX)"
    },
    {
      "name": "LYukN",
      "expression": "-1/2 yN[ff] PhiX NRbar[sp, ff].ProjP.NR[sp, ff]"
    },
    {
      "name": "LYukNu",
      "expression": "-ynu[ff1, ff2] Eps[ii, jj] Phibar[jj] LLbar[sp, ii, ff1].ProjP.NR[sp, ff2]"
    },
    {
      "name": "LGeneralU1",
      "expression": "LZpKin + LZpFerm + LNKin + LPhiXKin + LHX + LPhiXPot + LYukN + HC[LYukN] + LYukNu + HC[LYukNu]"
    }
  ]
}
```
I've read the paper's model section (Sec. II, Table I/II, Eqs. 1–9) and the schema. Here is the extracted model.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": [
      "Arindam Das",
      "P. S. Bhupal Dev",
      "Yutaka Hosotani",
      "Sanjoy Mandal"
    ],
    "version": "1.0",
    "date": "2021-04-22",
    "institutions": [
      "Kyungpook National University",
      "Hokkaido University",
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
  "interaction_order_hierarchy": [["NP", 1]],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "GENERALU1",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g'",
      "description": "U(1)X gauge coupling g'"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "GENERALU1",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)X charge parameter of the SM Higgs doublet direction; xH=0 gives B-L, xH=-2 gives U(1)R"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "GENERALU1",
      "order_block": 3,
      "tex": "x_\\Phi",
      "description": "U(1)X charge parameter of the singlet scalar direction; fixed to 1 in the paper"
    },
    {
      "name": "vX",
      "parameter_type": "External",
      "value": "9375.",
      "block_name": "GENERALU1",
      "order_block": 4,
      "tex": "v_\\Phi",
      "description": "U(1)X breaking VEV of the SM-singlet scalar PhiX"
    },
    {
      "name": "lamPhi",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "GENERALU1",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "tex": "\\lambda_\\Phi",
      "description": "quartic self coupling of the singlet scalar"
    },
    {
      "name": "lamHPhi",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "GENERALU1",
      "order_block": 6,
      "interaction_order": ["NP", 1],
      "tex": "\\lambda'",
      "description": "portal quartic coupling between the SM Higgs doublet and the singlet scalar"
    },
    {
      "name": "ynu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "YUKNU",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "ynu[1,1]", "rhs": "1.*^-7"},
        {"lhs": "ynu[2,2]", "rhs": "1.*^-7"},
        {"lhs": "ynu[3,3]", "rhs": "1.*^-7"}
      ],
      "tex": "Y_\\nu",
      "description": "Dirac neutrino Yukawa coupling matrix, lLbar H NR"
    },
    {
      "name": "xqL",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "tex": "q_x^{q_L}",
      "description": "U(1)X charge of the left-handed quark doublet"
    },
    {
      "name": "xuR",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "tex": "q_x^{u_R}",
      "description": "U(1)X charge of the right-handed up-type quarks"
    },
    {
      "name": "xdR",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "tex": "q_x^{d_R}",
      "description": "U(1)X charge of the right-handed down-type quarks"
    },
    {
      "name": "xlL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "tex": "q_x^{\\ell_L}",
      "description": "U(1)X charge of the left-handed lepton doublet"
    },
    {
      "name": "xeR",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "tex": "q_x^{e_R}",
      "description": "U(1)X charge of the right-handed charged leptons"
    },
    {
      "name": "xnR",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "tex": "q_x^{N_R}",
      "description": "U(1)X charge of the right-handed neutrinos"
    },
    {
      "name": "xHX",
      "parameter_type": "Internal",
      "value": "-xH/2",
      "tex": "q_x^{H}",
      "description": "U(1)X charge of the SM Higgs doublet"
    },
    {
      "name": "xPhiX",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "tex": "q_x^{\\Phi}",
      "description": "U(1)X charge of the SM-singlet scalar PhiX"
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "gX*Sqrt[4*xPhi^2*vX^2 + xH^2*vev^2/4]",
      "tex": "M_{Z'}",
      "description": "mass of the U(1)X gauge boson Z', Eq. (4)"
    },
    {
      "name": "muPhi2",
      "parameter_type": "Internal",
      "value": "-lamPhi*vX^2",
      "tex": "m_\\Phi^2",
      "description": "singlet scalar mass-squared term fixed by the minimisation condition"
    },
    {
      "name": "MhX",
      "parameter_type": "Internal",
      "value": "Sqrt[2*lamPhi]*vX",
      "tex": "m_\\phi",
      "description": "mass of the physical CP-even singlet scalar phi"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "yN[1]", "rhs": "Sqrt[2]*MN1/vX"},
        {"lhs": "yN[2]", "rhs": "Sqrt[2]*MN2/vX"},
        {"lhs": "yN[3]", "rhs": "Sqrt[2]*MN3/vX"}
      ],
      "tex": "Y_N",
      "description": "Majorana Yukawa coupling of the right-handed neutrinos to PhiX"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "50."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "Zp",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NR",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MN",
        "members": [["MN1", "10000."], ["MN2", "10000."], ["MN3", "10000."]]
      },
      "width": {
        "sym": "WN",
        "members": [["WN1", "1."], ["WN2", "1."], ["WN3", "1."]]
      },
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["N1", "N2", "N3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "hX",
      "self_conjugate": true,
      "mass": {"sym": "MhX", "value": "Internal"},
      "width": {"sym": "WhX", "value": "1."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900025,
      "particle_name": "hX",
      "full_name": "hX",
      "propagator_label": "hX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "GZp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "Internal"},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900026,
      "particle_name": "GZp",
      "full_name": "GZp",
      "propagator_label": "GZp",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "goldstone": "Zp"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "PhiX",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Q": "0"},
      "definitions": [
        "PhiX -> (vX + hX + I*GZp)/Sqrt[2]"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "expression": "-1/4 FS[Zp, mu, nu] FS[Zp, mu, nu]"
    },
    {
      "name": "LZpFerm",
      "expression": "-gX Zp[mu] ( xqL (uqbar.Ga[mu].ProjM.uq + dqbar.Ga[mu].ProjM.dq) + xuR uqbar.Ga[mu].ProjP.uq + xdR dqbar.Ga[mu].ProjP.dq + xlL (vlbar.Ga[mu].ProjM.vl + lbar.Ga[mu].ProjM.l) + xeR lbar.Ga[mu].ProjP.l + xnR NRbar.Ga[mu].ProjP.NR )"
    },
    {
      "name": "LNKin",
      "expression": "I/2 NRbar.Ga[mu].del[NR, mu]"
    },
    {
      "name": "LPhiXKin",
      "expression": "(del[PhiXbar, mu] + I*gX*xPhiX*Zp[mu]*PhiXbar) (del[PhiX, mu] - I*gX*xPhiX*Zp[mu]*PhiX)"
    },
    {
      "name": "LHX",
      "expression": "I*gX*xHX*Zp[mu] (Phibar[ii] del[Phi[ii], mu] - del[Phibar[ii], mu] Phi[ii]) + gX^2*xHX^2*Zp[mu] Zp[mu] Phibar[ii] Phi[ii]"
    },
    {
      "name": "LPhiXPot",
      "expression": "-muPhi2 PhiXbar PhiX - lamPhi (PhiXbar PhiX)^2 - lamHPhi (Phibar[ii] Phi[ii]) (PhiXbar PhiX)"
    },
    {
      "name": "LYukN",
      "expression": "-1/2 yN[ff] PhiX NRbar[sp, ff].ProjP.NR[sp, ff]"
    },
    {
      "name": "LYukNu",
      "expression": "-ynu[ff1, ff2] Eps[ii, jj] Phibar[jj] LLbar[sp, ii, ff1].ProjP.NR[sp, ff2]"
    },
    {
      "name": "LGeneralU1",
      "expression": "LZpKin + LZpFerm + LNKin + LPhiXKin + LHX + LPhiXPot + LYukN + HC[LYukN] + LYukNu + HC[LYukNu]"
    }
  ]
}
```