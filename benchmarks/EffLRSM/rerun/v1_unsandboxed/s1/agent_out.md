I'll start by reading the paper and the schema.
I've read the paper and the schema. Here is the extracted model.

**Content summary:** the Effective LRSM adds three new states — the charged vector $W_R^\pm$ (Q=+1, colour singlet, mass eigenstate), the neutral vector $Z_R$ (real), and three heavy Majorana neutrinos $N_{1,2,3}$ (colour and SU(2) singlets, Q=0). New parameters are the two chiral normalizations $\kappa^q_R,\kappa^\ell_R$, the RH CKM matrix, the heavy/light neutrino mixing matrices $Y,X$, plus the derived $Z_R$ chiral coefficients from Eqs. (9)–(10). There is no extended scalar sector — the paper states the LRSM Higgs fields are decoupled (15–20 TeV), so no new scalars are included.

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": [
      "Olivier Mattelaer",
      "Manimala Mitra",
      "Richard Ruiz"
    ],
    "version": "1.0",
    "date": "27 October 2016",
    "institutions": [
      "Centre for Cosmology, Particle Physics and Phenomenology (CP3), Universite catholique de Louvain",
      "Indian Institute of Science Education and Research Mohali (IISER Mohali)",
      "Institute for Particle Physics Phenomenology (IPPP), Durham University"
    ],
    "emails": [
      "olivier.mattelaer@uclouvain.be",
      "manimala@iisermohali.ac.in",
      "richard.ruiz@durham.ac.uk"
    ]
  },
  "interaction_order_hierarchy": [
    ["QCD", 1],
    ["QED", 2]
  ],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kq",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSM",
      "order_block": 1,
      "parameter_name": "kq",
      "tex": "\\kappa^q_R",
      "description": "Overall normalization of the WR and ZR coupling strength to quarks"
    },
    {
      "name": "kl",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSM",
      "order_block": 2,
      "parameter_name": "kl",
      "tex": "\\kappa^{\\ell}_R",
      "description": "Overall normalization of the WR and ZR coupling strength to leptons"
    },
    {
      "name": "VRCKM",
      "parameter_type": "Internal",
      "complex": true,
      "unitary": true,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "VRCKM[1,1]", "rhs": "1"},
        {"lhs": "VRCKM[1,2]", "rhs": "0"},
        {"lhs": "VRCKM[1,3]", "rhs": "0"},
        {"lhs": "VRCKM[2,1]", "rhs": "0"},
        {"lhs": "VRCKM[2,2]", "rhs": "1"},
        {"lhs": "VRCKM[2,3]", "rhs": "0"},
        {"lhs": "VRCKM[3,1]", "rhs": "0"},
        {"lhs": "VRCKM[3,2]", "rhs": "0"},
        {"lhs": "VRCKM[3,3]", "rhs": "1"}
      ],
      "tex": "V^{CKM'}",
      "description": "Right-handed CKM matrix; taken diagonal with unit entries"
    },
    {
      "name": "YN",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "YN[1,1]", "rhs": "1"},
        {"lhs": "YN[1,2]", "rhs": "0"},
        {"lhs": "YN[1,3]", "rhs": "0"},
        {"lhs": "YN[2,1]", "rhs": "0"},
        {"lhs": "YN[2,2]", "rhs": "1"},
        {"lhs": "YN[2,3]", "rhs": "0"},
        {"lhs": "YN[3,1]", "rhs": "0"},
        {"lhs": "YN[3,2]", "rhs": "0"},
        {"lhs": "YN[3,3]", "rhs": "1"}
      ],
      "tex": "Y_{\\ell m'}",
      "description": "Mixing between heavy Majorana mass eigenstate Nm' and the RH chiral state of lepton flavour l; diagonal with unit entries"
    },
    {
      "name": "XN",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "XN[1,1]", "rhs": "0"},
        {"lhs": "XN[1,2]", "rhs": "0"},
        {"lhs": "XN[1,3]", "rhs": "0"},
        {"lhs": "XN[2,1]", "rhs": "0"},
        {"lhs": "XN[2,2]", "rhs": "0"},
        {"lhs": "XN[2,3]", "rhs": "0"},
        {"lhs": "XN[3,1]", "rhs": "0"},
        {"lhs": "XN[3,2]", "rhs": "0"},
        {"lhs": "XN[3,3]", "rhs": "0"}
      ],
      "tex": "X_{\\ell m}",
      "description": "Mixing between light neutrino mass eigenstate nu_m and the RH chiral state of lepton flavour l; set to zero"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "-kq*gw*Sqrt[1 - sw^2/(cw^2*kq^2)]",
      "interaction_order": ["QED", 1],
      "tex": "g_{Z_R}^q",
      "description": "Overall ZR coupling strength to quarks, Eq.(8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "-kl*gw*Sqrt[1 - sw^2/(cw^2*kl^2)]",
      "interaction_order": ["QED", 1],
      "tex": "g_{Z_R}^{\\ell}",
      "description": "Overall ZR coupling strength to leptons, Eq.(8)"
    },
    {
      "name": "gLZRu",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3)*sw^2/(cw^2*kq^2)",
      "tex": "g_L^{Z_R,u}",
      "description": "Left chiral ZR coefficient for up-type quarks, Eq.(9)"
    },
    {
      "name": "gRZRu",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3)*sw^2/(cw^2*kq^2)",
      "tex": "g_R^{Z_R,u}",
      "description": "Right chiral ZR coefficient for up-type quarks, Eq.(10)"
    },
    {
      "name": "gLZRd",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3)*sw^2/(cw^2*kq^2)",
      "tex": "g_L^{Z_R,d}",
      "description": "Left chiral ZR coefficient for down-type quarks, Eq.(9)"
    },
    {
      "name": "gRZRd",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3)*sw^2/(cw^2*kq^2)",
      "tex": "g_R^{Z_R,d}",
      "description": "Right chiral ZR coefficient for down-type quarks, Eq.(10)"
    },
    {
      "name": "gLZRe",
      "parameter_type": "Internal",
      "value": "-1/2 + sw^2/(cw^2*kl^2)",
      "tex": "g_L^{Z_R,e}",
      "description": "Left chiral ZR coefficient for charged leptons, Eq.(9)"
    },
    {
      "name": "gRZRe",
      "parameter_type": "Internal",
      "value": "-1/2 + sw^2/(cw^2*kl^2)",
      "tex": "g_R^{Z_R,e}",
      "description": "Right chiral ZR coefficient for charged leptons, Eq.(10)"
    },
    {
      "name": "gLZRv",
      "parameter_type": "Internal",
      "value": "1/2",
      "tex": "g_L^{Z_R,\\nu}",
      "description": "Left chiral ZR coefficient for light neutrinos (T3L = +1/2, Q = 0)"
    },
    {
      "name": "gRZRn",
      "parameter_type": "Internal",
      "value": "1/2",
      "tex": "g_R^{Z_R,N}",
      "description": "Right chiral ZR coefficient for heavy Majorana neutrinos (T3R = +1/2, Q = 0)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 10,
      "class_name": "WR",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MWR", "value": "3000."},
      "width": {"sym": "WWR", "value": "84.3"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9900024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "WR",
      "propagator_label": "WR",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 11,
      "class_name": "ZR",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MZR", "value": "5070."},
      "width": {"sym": "WZR", "value": "114."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "ZR",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 10,
      "class_name": "NHL",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MN",
        "members": [
          ["MN1", "173.3"],
          ["MN2", "1.*^12"],
          ["MN3", "1.*^12"]
        ]
      },
      "width": {
        "sym": "WN",
        "members": [
          ["WN1", "2.12*^-8"],
          ["WN2", "Automatic"],
          ["WN3", "Automatic"]
        ]
      },
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["N1", "N2", "N3"],
      "propagator_label": ["N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWRkin",
      "delayed": true,
      "expression": "-1/2*(del[WRbar[mu],nu] - del[WRbar[nu],mu])*(del[WR[mu],nu] - del[WR[nu],mu]) + MWR^2*WRbar[mu]*WR[mu]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "-1/4*(del[ZR[nu],mu] - del[ZR[mu],nu])*(del[ZR[nu],mu] - del[ZR[mu],nu]) + 1/2*MZR^2*ZR[mu]*ZR[mu]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "I/2*(NHLbar[ff].Ga[mu].del[NHL[ff],mu]) - 1/2*MN[ff]*NHLbar[ff].NHL[ff]"
    },
    {
      "name": "LWRqq",
      "delayed": true,
      "expression": "-(kq*gw/Sqrt[2])*(uqbar.Ga[mu].ProjP.VRCKM.dq)*WR[mu]"
    },
    {
      "name": "LWRlN",
      "delayed": true,
      "expression": "-(kl*gw/Sqrt[2])*YN[ff,nn]*(NHLbar[nn].Ga[mu].ProjP.l[ff])*WR[mu]"
    },
    {
      "name": "LWRlv",
      "delayed": true,
      "expression": "-(kl*gw/Sqrt[2])*XN[ff,mm]*(CC[vlbar[mm]].Ga[mu].ProjP.l[ff])*WR[mu]"
    },
    {
      "name": "LZRqq",
      "delayed": true,
      "expression": "gZRq*(uqbar.Ga[mu].(gLZRu*ProjM + gRZRu*ProjP).uq + dqbar.Ga[mu].(gLZRd*ProjM + gRZRd*ProjP).dq)*ZR[mu]"
    },
    {
      "name": "LZRll",
      "delayed": true,
      "expression": "gZRl*(lbar.Ga[mu].(gLZRe*ProjM + gRZRe*ProjP).l + gLZRv*(vlbar.Ga[mu].ProjM.vl))*ZR[mu]"
    },
    {
      "name": "LZRNN",
      "delayed": true,
      "expression": "1/2*gZRl*gRZRn*(NHLbar[ff].Ga[mu].ProjP.NHL[ff])*ZR[mu]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNkin + LWRqq + HC[LWRqq] + LWRlN + HC[LWRlN] + LWRlv + HC[LWRlv] + LZRqq + LZRll + LZRNN"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I've read the paper and the schema. Here is the extracted model.

**Content summary:** the Effective LRSM adds three new states — the charged vector $W_R^\pm$ (Q=+1, colour singlet, mass eigenstate), the neutral vector $Z_R$ (real), and three heavy Majorana neutrinos $N_{1,2,3}$ (colour and SU(2) singlets, Q=0). New parameters are the two chiral normalizations $\kappa^q_R,\kappa^\ell_R$, the RH CKM matrix, the heavy/light neutrino mixing matrices $Y,X$, plus the derived $Z_R$ chiral coefficients from Eqs. (9)–(10). There is no extended scalar sector — the paper states the LRSM Higgs fields are decoupled (15–20 TeV), so no new scalars are included.

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": [
      "Olivier Mattelaer",
      "Manimala Mitra",
      "Richard Ruiz"
    ],
    "version": "1.0",
    "date": "27 October 2016",
    "institutions": [
      "Centre for Cosmology, Particle Physics and Phenomenology (CP3), Universite catholique de Louvain",
      "Indian Institute of Science Education and Research Mohali (IISER Mohali)",
      "Institute for Particle Physics Phenomenology (IPPP), Durham University"
    ],
    "emails": [
      "olivier.mattelaer@uclouvain.be",
      "manimala@iisermohali.ac.in",
      "richard.ruiz@durham.ac.uk"
    ]
  },
  "interaction_order_hierarchy": [
    ["QCD", 1],
    ["QED", 2]
  ],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kq",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSM",
      "order_block": 1,
      "parameter_name": "kq",
      "tex": "\\kappa^q_R",
      "description": "Overall normalization of the WR and ZR coupling strength to quarks"
    },
    {
      "name": "kl",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSM",
      "order_block": 2,
      "parameter_name": "kl",
      "tex": "\\kappa^{\\ell}_R",
      "description": "Overall normalization of the WR and ZR coupling strength to leptons"
    },
    {
      "name": "VRCKM",
      "parameter_type": "Internal",
      "complex": true,
      "unitary": true,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "VRCKM[1,1]", "rhs": "1"},
        {"lhs": "VRCKM[1,2]", "rhs": "0"},
        {"lhs": "VRCKM[1,3]", "rhs": "0"},
        {"lhs": "VRCKM[2,1]", "rhs": "0"},
        {"lhs": "VRCKM[2,2]", "rhs": "1"},
        {"lhs": "VRCKM[2,3]", "rhs": "0"},
        {"lhs": "VRCKM[3,1]", "rhs": "0"},
        {"lhs": "VRCKM[3,2]", "rhs": "0"},
        {"lhs": "VRCKM[3,3]", "rhs": "1"}
      ],
      "tex": "V^{CKM'}",
      "description": "Right-handed CKM matrix; taken diagonal with unit entries"
    },
    {
      "name": "YN",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "YN[1,1]", "rhs": "1"},
        {"lhs": "YN[1,2]", "rhs": "0"},
        {"lhs": "YN[1,3]", "rhs": "0"},
        {"lhs": "YN[2,1]", "rhs": "0"},
        {"lhs": "YN[2,2]", "rhs": "1"},
        {"lhs": "YN[2,3]", "rhs": "0"},
        {"lhs": "YN[3,1]", "rhs": "0"},
        {"lhs": "YN[3,2]", "rhs": "0"},
        {"lhs": "YN[3,3]", "rhs": "1"}
      ],
      "tex": "Y_{\\ell m'}",
      "description": "Mixing between heavy Majorana mass eigenstate Nm' and the RH chiral state of lepton flavour l; diagonal with unit entries"
    },
    {
      "name": "XN",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "XN[1,1]", "rhs": "0"},
        {"lhs": "XN[1,2]", "rhs": "0"},
        {"lhs": "XN[1,3]", "rhs": "0"},
        {"lhs": "XN[2,1]", "rhs": "0"},
        {"lhs": "XN[2,2]", "rhs": "0"},
        {"lhs": "XN[2,3]", "rhs": "0"},
        {"lhs": "XN[3,1]", "rhs": "0"},
        {"lhs": "XN[3,2]", "rhs": "0"},
        {"lhs": "XN[3,3]", "rhs": "0"}
      ],
      "tex": "X_{\\ell m}",
      "description": "Mixing between light neutrino mass eigenstate nu_m and the RH chiral state of lepton flavour l; set to zero"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "-kq*gw*Sqrt[1 - sw^2/(cw^2*kq^2)]",
      "interaction_order": ["QED", 1],
      "tex": "g_{Z_R}^q",
      "description": "Overall ZR coupling strength to quarks, Eq.(8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "-kl*gw*Sqrt[1 - sw^2/(cw^2*kl^2)]",
      "interaction_order": ["QED", 1],
      "tex": "g_{Z_R}^{\\ell}",
      "description": "Overall ZR coupling strength to leptons, Eq.(8)"
    },
    {
      "name": "gLZRu",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3)*sw^2/(cw^2*kq^2)",
      "tex": "g_L^{Z_R,u}",
      "description": "Left chiral ZR coefficient for up-type quarks, Eq.(9)"
    },
    {
      "name": "gRZRu",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3)*sw^2/(cw^2*kq^2)",
      "tex": "g_R^{Z_R,u}",
      "description": "Right chiral ZR coefficient for up-type quarks, Eq.(10)"
    },
    {
      "name": "gLZRd",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3)*sw^2/(cw^2*kq^2)",
      "tex": "g_L^{Z_R,d}",
      "description": "Left chiral ZR coefficient for down-type quarks, Eq.(9)"
    },
    {
      "name": "gRZRd",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3)*sw^2/(cw^2*kq^2)",
      "tex": "g_R^{Z_R,d}",
      "description": "Right chiral ZR coefficient for down-type quarks, Eq.(10)"
    },
    {
      "name": "gLZRe",
      "parameter_type": "Internal",
      "value": "-1/2 + sw^2/(cw^2*kl^2)",
      "tex": "g_L^{Z_R,e}",
      "description": "Left chiral ZR coefficient for charged leptons, Eq.(9)"
    },
    {
      "name": "gRZRe",
      "parameter_type": "Internal",
      "value": "-1/2 + sw^2/(cw^2*kl^2)",
      "tex": "g_R^{Z_R,e}",
      "description": "Right chiral ZR coefficient for charged leptons, Eq.(10)"
    },
    {
      "name": "gLZRv",
      "parameter_type": "Internal",
      "value": "1/2",
      "tex": "g_L^{Z_R,\\nu}",
      "description": "Left chiral ZR coefficient for light neutrinos (T3L = +1/2, Q = 0)"
    },
    {
      "name": "gRZRn",
      "parameter_type": "Internal",
      "value": "1/2",
      "tex": "g_R^{Z_R,N}",
      "description": "Right chiral ZR coefficient for heavy Majorana neutrinos (T3R = +1/2, Q = 0)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 10,
      "class_name": "WR",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MWR", "value": "3000."},
      "width": {"sym": "WWR", "value": "84.3"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9900024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "WR",
      "propagator_label": "WR",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 11,
      "class_name": "ZR",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MZR", "value": "5070."},
      "width": {"sym": "WZR", "value": "114."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "ZR",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 10,
      "class_name": "NHL",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MN",
        "members": [
          ["MN1", "173.3"],
          ["MN2", "1.*^12"],
          ["MN3", "1.*^12"]
        ]
      },
      "width": {
        "sym": "WN",
        "members": [
          ["WN1", "2.12*^-8"],
          ["WN2", "Automatic"],
          ["WN3", "Automatic"]
        ]
      },
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["N1", "N2", "N3"],
      "propagator_label": ["N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWRkin",
      "delayed": true,
      "expression": "-1/2*(del[WRbar[mu],nu] - del[WRbar[nu],mu])*(del[WR[mu],nu] - del[WR[nu],mu]) + MWR^2*WRbar[mu]*WR[mu]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "-1/4*(del[ZR[nu],mu] - del[ZR[mu],nu])*(del[ZR[nu],mu] - del[ZR[mu],nu]) + 1/2*MZR^2*ZR[mu]*ZR[mu]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "I/2*(NHLbar[ff].Ga[mu].del[NHL[ff],mu]) - 1/2*MN[ff]*NHLbar[ff].NHL[ff]"
    },
    {
      "name": "LWRqq",
      "delayed": true,
      "expression": "-(kq*gw/Sqrt[2])*(uqbar.Ga[mu].ProjP.VRCKM.dq)*WR[mu]"
    },
    {
      "name": "LWRlN",
      "delayed": true,
      "expression": "-(kl*gw/Sqrt[2])*YN[ff,nn]*(NHLbar[nn].Ga[mu].ProjP.l[ff])*WR[mu]"
    },
    {
      "name": "LWRlv",
      "delayed": true,
      "expression": "-(kl*gw/Sqrt[2])*XN[ff,mm]*(CC[vlbar[mm]].Ga[mu].ProjP.l[ff])*WR[mu]"
    },
    {
      "name": "LZRqq",
      "delayed": true,
      "expression": "gZRq*(uqbar.Ga[mu].(gLZRu*ProjM + gRZRu*ProjP).uq + dqbar.Ga[mu].(gLZRd*ProjM + gRZRd*ProjP).dq)*ZR[mu]"
    },
    {
      "name": "LZRll",
      "delayed": true,
      "expression": "gZRl*(lbar.Ga[mu].(gLZRe*ProjM + gRZRe*ProjP).l + gLZRv*(vlbar.Ga[mu].ProjM.vl))*ZR[mu]"
    },
    {
      "name": "LZRNN",
      "delayed": true,
      "expression": "1/2*gZRl*gRZRn*(NHLbar[ff].Ga[mu].ProjP.NHL[ff])*ZR[mu]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNkin + LWRqq + HC[LWRqq] + LWRlN + HC[LWRlN] + LWRlv + HC[LWRlv] + LZRqq + LZRll + LZRNN"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```