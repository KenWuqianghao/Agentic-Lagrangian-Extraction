```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "27. 10. 2016",
    "institutions": [
      "CP3, Universite catholique de Louvain",
      "IISER Mohali",
      "IPPP, Durham University"
    ]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kQR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSM",
      "order_block": 1,
      "description": "kappa^q_R: normalisation of the WR and ZR couplings to quarks, Eq.(4) and Eq.(8). Dimensionless, interaction order 0 by construction: it appears with a negative power in the ZR chiral coefficients of Eqs.(9)-(10), so the NP order is carried by cWRq, cWRl, cZRq, cZRl. Benchmark 1.0; Fig.3 also uses 0.75"
    },
    {
      "name": "kLR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSM",
      "order_block": 2,
      "description": "kappa^l_R: normalisation of the WR and ZR couplings to leptons and heavy neutrinos, Eq.(5) and Eq.(8). Dimensionless, interaction order 0 by construction (see kQR). Benchmark 1.0"
    },
    {
      "name": "VCKMR",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "CKMR",
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
      "description": "Right-handed CKM matrix V^CKM' of Eq.(4), taken diagonal with unit entries (Sec. II)"
    },
    {
      "name": "YNL",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "YNMIX",
      "value_rules": [
        {"lhs": "YNL[1,1]", "rhs": "1"},
        {"lhs": "YNL[1,2]", "rhs": "0"},
        {"lhs": "YNL[1,3]", "rhs": "0"},
        {"lhs": "YNL[2,1]", "rhs": "0"},
        {"lhs": "YNL[2,2]", "rhs": "1"},
        {"lhs": "YNL[2,3]", "rhs": "0"},
        {"lhs": "YNL[3,1]", "rhs": "0"},
        {"lhs": "YNL[3,2]", "rhs": "0"},
        {"lhs": "YNL[3,3]", "rhs": "1"}
      ],
      "description": "Mixing Y_(l m') of Eq.(5) between the heavy mass eigenstate N_m' and the right-handed chiral state of lepton flavour l. First index = heavy state m', second index = lepton flavour l. Diagonal with unit entries, Eq.(7)"
    },
    {
      "name": "XNL",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "XNMIX",
      "value_rules": [
        {"lhs": "XNL[1,1]", "rhs": "0"},
        {"lhs": "XNL[1,2]", "rhs": "0"},
        {"lhs": "XNL[1,3]", "rhs": "0"},
        {"lhs": "XNL[2,1]", "rhs": "0"},
        {"lhs": "XNL[2,2]", "rhs": "0"},
        {"lhs": "XNL[2,3]", "rhs": "0"},
        {"lhs": "XNL[3,1]", "rhs": "0"},
        {"lhs": "XNL[3,2]", "rhs": "0"},
        {"lhs": "XNL[3,3]", "rhs": "0"}
      ],
      "description": "Light-neutrino mixing X_(l m) of Eq.(5), real, written in the lbar orientation. Set to zero at collider scales, Eq.(7)"
    },
    {
      "name": "cWRq",
      "parameter_type": "Internal",
      "value": "-kQR gw/Sqrt[2]",
      "interaction_order": ["NP", 1],
      "description": "WR charged-current coefficient for quarks, -kappa^q_R g/Sqrt[2], Eq.(4)"
    },
    {
      "name": "cWRl",
      "parameter_type": "Internal",
      "value": "-kLR gw/Sqrt[2]",
      "interaction_order": ["NP", 1],
      "description": "WR charged-current coefficient for leptons, -kappa^l_R g/Sqrt[2], Eq.(5)"
    },
    {
      "name": "cZRq",
      "parameter_type": "Internal",
      "value": "-kQR gw/Sqrt[1 - sw^2/(cw^2 kQR^2)]",
      "interaction_order": ["NP", 1],
      "description": "ZR overall coefficient for quarks, Eq.(8): -kappa^q_R g divided by Sqrt[1 - tan^2(thetaW)/kappa^q_R^2]. The root is in the DENOMINATOR; checked against the width denominator of Eq.(14) and against Tbl. II (82.3 GeV for ZR to qq)"
    },
    {
      "name": "cZRl",
      "parameter_type": "Internal",
      "value": "-kLR gw/Sqrt[1 - sw^2/(cw^2 kLR^2)]",
      "interaction_order": ["NP", 1],
      "description": "ZR overall coefficient for leptons and heavy neutrinos, Eq.(8): -kappa^l_R g divided by Sqrt[1 - tan^2(thetaW)/kappa^l_R^2]. Root in the DENOMINATOR; checked against Eq.(14) and Tbl. II (10.2 GeV for ZR to N1 N1)"
    },
    {
      "name": "gZRuL",
      "parameter_type": "Internal",
      "value": "(1/2 - 2/3) sw^2/(cw^2 kQR^2)",
      "description": "Left chiral ZR coefficient of the up-type quarks, Eq.(9): (T3L - Q) tan^2(thetaW)/kappa^2 with T3L = 1/2, Q = 2/3"
    },
    {
      "name": "gZRuR",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3) sw^2/(cw^2 kQR^2)",
      "description": "Right chiral ZR coefficient of the up-type quarks, Eq.(10): T3R - tan^2(thetaW) Q/kappa^2 with T3R = 1/2, Q = 2/3"
    },
    {
      "name": "gZRdL",
      "parameter_type": "Internal",
      "value": "(-1/2 + 1/3) sw^2/(cw^2 kQR^2)",
      "description": "Left chiral ZR coefficient of the down-type quarks, Eq.(9) with T3L = -1/2, Q = -1/3"
    },
    {
      "name": "gZRdR",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3) sw^2/(cw^2 kQR^2)",
      "description": "Right chiral ZR coefficient of the down-type quarks, Eq.(10) with T3R = -1/2, Q = -1/3"
    },
    {
      "name": "gZReL",
      "parameter_type": "Internal",
      "value": "(-1/2 + 1) sw^2/(cw^2 kLR^2)",
      "description": "Left chiral ZR coefficient of the charged leptons, Eq.(9) with T3L = -1/2, Q = -1"
    },
    {
      "name": "gZReR",
      "parameter_type": "Internal",
      "value": "-1/2 + sw^2/(cw^2 kLR^2)",
      "description": "Right chiral ZR coefficient of the charged leptons, Eq.(10) with T3R = -1/2, Q = -1"
    },
    {
      "name": "gZRvL",
      "parameter_type": "Internal",
      "value": "(1/2) sw^2/(cw^2 kLR^2)",
      "description": "Left chiral ZR coefficient of the light neutrinos, Eq.(9) with T3L = 1/2, Q = 0. The right coefficient is zero, so no ProjP term for vl"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "WR",
      "self_conjugate": false,
      "mass": {"sym": "MWR", "value": "3000."},
      "width": {"sym": "WWR", "value": "84.3"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9900024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "Right-handed charged gauge boson",
      "propagator_label": "WR",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "ZR",
      "self_conjugate": true,
      "mass": {"sym": "MZR", "value": "5070."},
      "width": {"sym": "WZR", "value": "114."},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "Right-handed neutral gauge boson",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NH",
      "self_conjugate": true,
      "class_members": ["N1", "N2", "N3"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "mass": {
        "sym": "MNH",
        "members": [["MN1", "173.3"], ["MN2", "1.*^12"], ["MN3", "1.*^12"]]
      },
      "width": {
        "sym": "WNH",
        "members": [["WN1", "2.12*^-8"], ["WN2", "1."], ["WN3", "1."]]
      },
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino N1", "Heavy Majorana neutrino N2", "Heavy Majorana neutrino N3"],
      "propagator_label": "NH",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/2 FS[WRbar, mu, nu] FS[WR, mu, nu] + MWR^2 WRbar[mu] WR[mu]]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu]]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{mu, ff, sp}, ExpandIndices[I/2 NHbar.Ga[mu].del[NH, mu] - 1/2 MNH[ff] NHbar[sp, ff].NH[sp, ff]]]"
    },
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[cWRq uqbar.VCKMR.Ga[mu].ProjP.dq WR[mu]]]"
    },
    {
      "name": "LWRlN",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[cWRl NHbar.YNL.Ga[mu].ProjP.l WR[mu]]]"
    },
    {
      "name": "LWRlv",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[cWRl lbar.XNL.Ga[mu].ProjP.CC[vl] WRbar[mu]]]"
    },
    {
      "name": "LZRq",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[cZRq (gZRuL uqbar.Ga[mu].ProjM.uq + gZRuR uqbar.Ga[mu].ProjP.uq + gZRdL dqbar.Ga[mu].ProjM.dq + gZRdR dqbar.Ga[mu].ProjP.dq) ZR[mu]]]"
    },
    {
      "name": "LZRl",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[cZRl (gZReL lbar.Ga[mu].ProjM.l + gZReR lbar.Ga[mu].ProjP.l + gZRvL vlbar.Ga[mu].ProjM.vl) ZR[mu]]]"
    },
    {
      "name": "LZRN",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[1/2 cZRl NHbar.Ga[mu].ProjP.NH ZR[mu]]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNkin + LWRq + HC[LWRq] + LWRlN + HC[LWRlN] + LWRlv + HC[LWRlv] + LZRq + LZRl + LZRN"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```