I'll start by reading the paper, schema, and SM file.
I have the paper, schema, and SM.fr conventions. Here is the extracted model.

**Content check (new physics in the Effective LRSM):**
- **Gauge bosons:** $W_R^\pm$ (complex vector, $Q=1$, $M_{W_R}=3$ TeV) and $Z_R$ (real vector, $M_{Z_R}\simeq5070$ GeV) — mass eigenstates, no non-Abelian self-interactions.
- **Fermions:** three heavy Majorana neutrinos $N_1,N_2,N_3$ (colour singlet, $Q=0$, self-conjugate) with $m_{N_1}=173.3$ GeV and $m_{N_2},m_{N_3}=10^{12}$ GeV.
- **Parameters:** the coupling normalisations $\kappa^q_R,\kappa^\ell_R$, the RH CKM matrix, the heavy ($Y$) and light ($X$) lepton mixing matrices, and the $Z_R$ chiral coefficients of Eqs. (9)–(10).
- **Lagrangian:** free $W_R,Z_R$ kinetic+mass terms, Majorana $N$ kinetic+mass term, and Eqs. (4), (5), (8).

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
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kqR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "EFFLRSM",
      "order_block": 1,
      "tex": "Subscript[\\[Kappa], R]^q",
      "description": "Overall normalization of the WR and ZR coupling strength to quarks"
    },
    {
      "name": "klR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "EFFLRSM",
      "order_block": 2,
      "tex": "Subscript[\\[Kappa], R]^l",
      "description": "Overall normalization of the WR and ZR coupling strength to leptons"
    },
    {
      "name": "tw",
      "parameter_type": "Internal",
      "value": "sw/cw",
      "tex": "Subscript[t,w]",
      "description": "Tangent of the Weinberg angle"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kqR*gw/Sqrt[1 - tw^2/kqR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to quarks, Eq. (8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "klR*gw/Sqrt[1 - tw^2/klR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to leptons, Eq. (8)"
    },
    {
      "name": "gZRLu",
      "parameter_type": "Internal",
      "value": "-tw^2/(6*kqR^2)",
      "description": "Left-handed ZR chiral coefficient of up-type quarks, Eq. (9)"
    },
    {
      "name": "gZRRu",
      "parameter_type": "Internal",
      "value": "1/2 - 2*tw^2/(3*kqR^2)",
      "description": "Right-handed ZR chiral coefficient of up-type quarks, Eq. (10)"
    },
    {
      "name": "gZRLd",
      "parameter_type": "Internal",
      "value": "-tw^2/(6*kqR^2)",
      "description": "Left-handed ZR chiral coefficient of down-type quarks, Eq. (9)"
    },
    {
      "name": "gZRRd",
      "parameter_type": "Internal",
      "value": "-1/2 + tw^2/(3*kqR^2)",
      "description": "Right-handed ZR chiral coefficient of down-type quarks, Eq. (10)"
    },
    {
      "name": "gZRLe",
      "parameter_type": "Internal",
      "value": "tw^2/(2*klR^2)",
      "description": "Left-handed ZR chiral coefficient of charged leptons, Eq. (9)"
    },
    {
      "name": "gZRRe",
      "parameter_type": "Internal",
      "value": "-1/2 + tw^2/klR^2",
      "description": "Right-handed ZR chiral coefficient of charged leptons, Eq. (10)"
    },
    {
      "name": "gZRLv",
      "parameter_type": "Internal",
      "value": "tw^2/(2*klR^2)",
      "description": "Left-handed ZR chiral coefficient of light neutrinos, Eq. (9)"
    },
    {
      "name": "gZRRN",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "Right-handed ZR chiral coefficient of heavy Majorana neutrinos, Eq. (10)"
    },
    {
      "name": "CKMR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "complex": true,
      "unitary": true,
      "value_rules": [
        {"lhs": "CKMR[1,1]", "rhs": "1"},
        {"lhs": "CKMR[1,2]", "rhs": "0"},
        {"lhs": "CKMR[1,3]", "rhs": "0"},
        {"lhs": "CKMR[2,1]", "rhs": "0"},
        {"lhs": "CKMR[2,2]", "rhs": "1"},
        {"lhs": "CKMR[2,3]", "rhs": "0"},
        {"lhs": "CKMR[3,1]", "rhs": "0"},
        {"lhs": "CKMR[3,2]", "rhs": "0"},
        {"lhs": "CKMR[3,3]", "rhs": "1"}
      ],
      "tex": "Superscript[V,CKM']",
      "description": "Right-handed CKM matrix, taken diagonal with unit entries"
    },
    {
      "name": "YN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "YN[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "YN[1,1]", "rhs": "1"},
        {"lhs": "YN[2,2]", "rhs": "1"},
        {"lhs": "YN[3,3]", "rhs": "1"}
      ],
      "parameter_name": "YN",
      "tex": "Subscript[Y, lm]",
      "description": "Mixing between the heavy neutrino mass eigenstate Nm and the RH chiral state of lepton flavor l, Eq. (7)"
    },
    {
      "name": "XL",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "XL[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "XL[1,1]", "rhs": "0"},
        {"lhs": "XL[2,2]", "rhs": "0"},
        {"lhs": "XL[3,3]", "rhs": "0"}
      ],
      "parameter_name": "XL",
      "tex": "Subscript[X, lm]",
      "description": "Mixing between the light neutrino mass eigenstate and the RH chiral state, set to zero, Eq. (7)"
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
      "full_name": "WR",
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
      "quantum_numbers": {},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "ZR",
      "propagator_label": "ZR",
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
        "members": [["MN1", "173.3"], ["MN2", "1.*^12"], ["MN3", "1.*^12"]]
      },
      "width": {
        "sym": "WN",
        "members": [["WN1", "2.12*^-8"], ["WN2", "1.*^-8"], ["WN3", "1.*^-8"]]
      },
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["NR", "n1", "n2", "n3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LVRKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/2*FS[WRbar,mu,nu]*FS[WR,mu,nu] + MWR^2*WRbar[mu]*WR[mu] - 1/4*FS[ZR,mu,nu]*FS[ZR,mu,nu] + 1/2*MZR^2*ZR[mu]*ZR[mu]]]"
    },
    {
      "name": "LNRKin",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff}, ExpandIndices[I/2*NRbar[sp1,ff].Ga[mu,sp1,sp2].del[NR[sp2,ff],mu] - 1/2*MN[ff]*NRbar[sp1,ff].NR[sp1,ff], FlavorExpand->{Generation}]]"
    },
    {
      "name": "LWRQuark",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,sp3,ff1,ff2,cc,lag}, lag = -kqR*gw/Sqrt[2]*CKMR[ff1,ff2]*uqbar[sp1,ff1,cc].Ga[mu,sp1,sp2].ProjP[sp2,sp3].dq[sp3,ff2,cc]*WR[mu]; ExpandIndices[lag + HC[lag], FlavorExpand->{Generation}]]"
    },
    {
      "name": "LWRLepton",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,sp3,ff1,ff2,lag}, lag = -klR*gw/Sqrt[2]*(YN[ff1,ff2]*NRbar[sp1,ff2].Ga[mu,sp1,sp2].ProjP[sp2,sp3].l[sp3,ff1] + XL[ff1,ff2]*CC[vlbar][sp1,ff2].Ga[mu,sp1,sp2].ProjP[sp2,sp3].l[sp3,ff1])*WR[mu]; ExpandIndices[lag + HC[lag], FlavorExpand->{Generation}]]"
    },
    {
      "name": "LZRNC",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,sp3,ff,cc}, ExpandIndices[-gZRq*(uqbar[sp1,ff,cc].Ga[mu,sp1,sp2].(gZRLu*ProjM[sp2,sp3] + gZRRu*ProjP[sp2,sp3]).uq[sp3,ff,cc] + dqbar[sp1,ff,cc].Ga[mu,sp1,sp2].(gZRLd*ProjM[sp2,sp3] + gZRRd*ProjP[sp2,sp3]).dq[sp3,ff,cc])*ZR[mu] - gZRl*(lbar[sp1,ff].Ga[mu,sp1,sp2].(gZRLe*ProjM[sp2,sp3] + gZRRe*ProjP[sp2,sp3]).l[sp3,ff] + gZRLv*vlbar[sp1,ff].Ga[mu,sp1,sp2].ProjM[sp2,sp3].vl[sp3,ff] + 1/2*gZRRN*NRbar[sp1,ff].Ga[mu,sp1,sp2].ProjP[sp2,sp3].NR[sp3,ff])*ZR[mu], FlavorExpand->{Generation}]]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LVRKin + LNRKin + LWRQuark + LWRLepton + LZRNC"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I have the paper, schema, and SM.fr conventions. Here is the extracted model.

**Content check (new physics in the Effective LRSM):**
- **Gauge bosons:** $W_R^\pm$ (complex vector, $Q=1$, $M_{W_R}=3$ TeV) and $Z_R$ (real vector, $M_{Z_R}\simeq5070$ GeV) — mass eigenstates, no non-Abelian self-interactions.
- **Fermions:** three heavy Majorana neutrinos $N_1,N_2,N_3$ (colour singlet, $Q=0$, self-conjugate) with $m_{N_1}=173.3$ GeV and $m_{N_2},m_{N_3}=10^{12}$ GeV.
- **Parameters:** the coupling normalisations $\kappa^q_R,\kappa^\ell_R$, the RH CKM matrix, the heavy ($Y$) and light ($X$) lepton mixing matrices, and the $Z_R$ chiral coefficients of Eqs. (9)–(10).
- **Lagrangian:** free $W_R,Z_R$ kinetic+mass terms, Majorana $N$ kinetic+mass term, and Eqs. (4), (5), (8).

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
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kqR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "EFFLRSM",
      "order_block": 1,
      "tex": "Subscript[\\[Kappa], R]^q",
      "description": "Overall normalization of the WR and ZR coupling strength to quarks"
    },
    {
      "name": "klR",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "EFFLRSM",
      "order_block": 2,
      "tex": "Subscript[\\[Kappa], R]^l",
      "description": "Overall normalization of the WR and ZR coupling strength to leptons"
    },
    {
      "name": "tw",
      "parameter_type": "Internal",
      "value": "sw/cw",
      "tex": "Subscript[t,w]",
      "description": "Tangent of the Weinberg angle"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kqR*gw/Sqrt[1 - tw^2/kqR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to quarks, Eq. (8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "klR*gw/Sqrt[1 - tw^2/klR^2]",
      "interaction_order": ["QED", 1],
      "description": "Overall ZR coupling strength to leptons, Eq. (8)"
    },
    {
      "name": "gZRLu",
      "parameter_type": "Internal",
      "value": "-tw^2/(6*kqR^2)",
      "description": "Left-handed ZR chiral coefficient of up-type quarks, Eq. (9)"
    },
    {
      "name": "gZRRu",
      "parameter_type": "Internal",
      "value": "1/2 - 2*tw^2/(3*kqR^2)",
      "description": "Right-handed ZR chiral coefficient of up-type quarks, Eq. (10)"
    },
    {
      "name": "gZRLd",
      "parameter_type": "Internal",
      "value": "-tw^2/(6*kqR^2)",
      "description": "Left-handed ZR chiral coefficient of down-type quarks, Eq. (9)"
    },
    {
      "name": "gZRRd",
      "parameter_type": "Internal",
      "value": "-1/2 + tw^2/(3*kqR^2)",
      "description": "Right-handed ZR chiral coefficient of down-type quarks, Eq. (10)"
    },
    {
      "name": "gZRLe",
      "parameter_type": "Internal",
      "value": "tw^2/(2*klR^2)",
      "description": "Left-handed ZR chiral coefficient of charged leptons, Eq. (9)"
    },
    {
      "name": "gZRRe",
      "parameter_type": "Internal",
      "value": "-1/2 + tw^2/klR^2",
      "description": "Right-handed ZR chiral coefficient of charged leptons, Eq. (10)"
    },
    {
      "name": "gZRLv",
      "parameter_type": "Internal",
      "value": "tw^2/(2*klR^2)",
      "description": "Left-handed ZR chiral coefficient of light neutrinos, Eq. (9)"
    },
    {
      "name": "gZRRN",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "Right-handed ZR chiral coefficient of heavy Majorana neutrinos, Eq. (10)"
    },
    {
      "name": "CKMR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "complex": true,
      "unitary": true,
      "value_rules": [
        {"lhs": "CKMR[1,1]", "rhs": "1"},
        {"lhs": "CKMR[1,2]", "rhs": "0"},
        {"lhs": "CKMR[1,3]", "rhs": "0"},
        {"lhs": "CKMR[2,1]", "rhs": "0"},
        {"lhs": "CKMR[2,2]", "rhs": "1"},
        {"lhs": "CKMR[2,3]", "rhs": "0"},
        {"lhs": "CKMR[3,1]", "rhs": "0"},
        {"lhs": "CKMR[3,2]", "rhs": "0"},
        {"lhs": "CKMR[3,3]", "rhs": "1"}
      ],
      "tex": "Superscript[V,CKM']",
      "description": "Right-handed CKM matrix, taken diagonal with unit entries"
    },
    {
      "name": "YN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "YN[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "YN[1,1]", "rhs": "1"},
        {"lhs": "YN[2,2]", "rhs": "1"},
        {"lhs": "YN[3,3]", "rhs": "1"}
      ],
      "parameter_name": "YN",
      "tex": "Subscript[Y, lm]",
      "description": "Mixing between the heavy neutrino mass eigenstate Nm and the RH chiral state of lepton flavor l, Eq. (7)"
    },
    {
      "name": "XL",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "XL[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "XL[1,1]", "rhs": "0"},
        {"lhs": "XL[2,2]", "rhs": "0"},
        {"lhs": "XL[3,3]", "rhs": "0"}
      ],
      "parameter_name": "XL",
      "tex": "Subscript[X, lm]",
      "description": "Mixing between the light neutrino mass eigenstate and the RH chiral state, set to zero, Eq. (7)"
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
      "full_name": "WR",
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
      "quantum_numbers": {},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "ZR",
      "propagator_label": "ZR",
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
        "members": [["MN1", "173.3"], ["MN2", "1.*^12"], ["MN3", "1.*^12"]]
      },
      "width": {
        "sym": "WN",
        "members": [["WN1", "2.12*^-8"], ["WN2", "1.*^-8"], ["WN3", "1.*^-8"]]
      },
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["NR", "n1", "n2", "n3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LVRKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/2*FS[WRbar,mu,nu]*FS[WR,mu,nu] + MWR^2*WRbar[mu]*WR[mu] - 1/4*FS[ZR,mu,nu]*FS[ZR,mu,nu] + 1/2*MZR^2*ZR[mu]*ZR[mu]]]"
    },
    {
      "name": "LNRKin",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff}, ExpandIndices[I/2*NRbar[sp1,ff].Ga[mu,sp1,sp2].del[NR[sp2,ff],mu] - 1/2*MN[ff]*NRbar[sp1,ff].NR[sp1,ff], FlavorExpand->{Generation}]]"
    },
    {
      "name": "LWRQuark",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,sp3,ff1,ff2,cc,lag}, lag = -kqR*gw/Sqrt[2]*CKMR[ff1,ff2]*uqbar[sp1,ff1,cc].Ga[mu,sp1,sp2].ProjP[sp2,sp3].dq[sp3,ff2,cc]*WR[mu]; ExpandIndices[lag + HC[lag], FlavorExpand->{Generation}]]"
    },
    {
      "name": "LWRLepton",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,sp3,ff1,ff2,lag}, lag = -klR*gw/Sqrt[2]*(YN[ff1,ff2]*NRbar[sp1,ff2].Ga[mu,sp1,sp2].ProjP[sp2,sp3].l[sp3,ff1] + XL[ff1,ff2]*CC[vlbar][sp1,ff2].Ga[mu,sp1,sp2].ProjP[sp2,sp3].l[sp3,ff1])*WR[mu]; ExpandIndices[lag + HC[lag], FlavorExpand->{Generation}]]"
    },
    {
      "name": "LZRNC",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,sp3,ff,cc}, ExpandIndices[-gZRq*(uqbar[sp1,ff,cc].Ga[mu,sp1,sp2].(gZRLu*ProjM[sp2,sp3] + gZRRu*ProjP[sp2,sp3]).uq[sp3,ff,cc] + dqbar[sp1,ff,cc].Ga[mu,sp1,sp2].(gZRLd*ProjM[sp2,sp3] + gZRRd*ProjP[sp2,sp3]).dq[sp3,ff,cc])*ZR[mu] - gZRl*(lbar[sp1,ff].Ga[mu,sp1,sp2].(gZRLe*ProjM[sp2,sp3] + gZRRe*ProjP[sp2,sp3]).l[sp3,ff] + gZRLv*vlbar[sp1,ff].Ga[mu,sp1,sp2].ProjM[sp2,sp3].vl[sp3,ff] + 1/2*gZRRN*NRbar[sp1,ff].Ga[mu,sp1,sp2].ProjP[sp2,sp3].NR[sp3,ff])*ZR[mu], FlavorExpand->{Generation}]]"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LVRKin + LNRKin + LWRQuark + LWRLepton + LZRNC"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```