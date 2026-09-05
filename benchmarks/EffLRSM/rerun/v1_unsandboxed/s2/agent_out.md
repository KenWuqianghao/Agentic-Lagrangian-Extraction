I'll start by reading the paper and the schema.
I have everything I need. Here is the extracted model.

**What the paper contains (Sec. II):** the effective LRSM adds only three kinds of new state — the charged $W_R^\pm$, the neutral $Z_R$, and three heavy Majorana neutrinos $N_{1,2,3}$ aligned with the RH chiral states. The LRSM scalar sector is explicitly decoupled (Sec. II B), so no new scalars enter. New parameters are the two coupling normalizations $\kappa^q_R,\kappa^\ell_R$, the RH CKM matrix $V^{CKM'}$, and the lepton mixing matrices $Y_{\ell m'}$ (heavy) and $X_{\ell m}$ (light). The implemented terms are Eqs. (4), (5) and (8) — see Sec. III A.

One reading note: Eq. (8) as printed shows the square root in the numerator, but the width formula Eq. (14) divides by $[1-(1/\kappa)^2\tan^2\theta_W]$. The two agree only if the coupling is $\kappa g/\sqrt{1-\tan^2\theta_W/\kappa^2}$, which is also what the $SU(2)_R\times U(1)_{B-L}\to U(1)_Y$ rotation gives. I used the denominator form.

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["Olivier Mattelaer", "Manimala Mitra", "Richard Ruiz"],
    "version": "1.0",
    "date": "31. 10. 2016",
    "institutions": [
      "Centre for Cosmology, Particle Physics and Phenomenology (CP3), Universite catholique de Louvain",
      "IISER Mohali",
      "IPPP, Durham University"
    ],
    "emails": [
      "olivier.mattelaer@uclouvain.be",
      "manimala@iisermohali.ac.in",
      "richard.ruiz@durham.ac.uk"
    ]
  },
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kqR",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "LRSM",
      "order_block": 1,
      "tex": "Subscript[\\[Kappa],Rq]",
      "description": "Overall normalization of the WR and ZR coupling strength to quarks"
    },
    {
      "name": "klR",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "LRSM",
      "order_block": 2,
      "tex": "Subscript[\\[Kappa],Rl]",
      "description": "Overall normalization of the WR and ZR coupling strength to leptons"
    },
    {
      "name": "CKMR",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "CKMR[1,1]", "rhs": "1"},
        {"lhs": "CKMR[2,2]", "rhs": "1"},
        {"lhs": "CKMR[3,3]", "rhs": "1"},
        {"lhs": "CKMR[i_,j_]", "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)", "delayed": true}
      ],
      "tex": "Superscript[V,CKMp]",
      "description": "Right-handed CKM matrix of the WR quark current; diagonal with unit entries by default"
    },
    {
      "name": "Ymix",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "Ymix[1,1]", "rhs": "1"},
        {"lhs": "Ymix[2,2]", "rhs": "1"},
        {"lhs": "Ymix[3,3]", "rhs": "1"},
        {"lhs": "Ymix[i_,j_]", "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)", "delayed": true}
      ],
      "tex": "Subscript[Y,lm]",
      "description": "Mixing of the heavy Majorana mass eigenstate N with the RH chiral state of lepton flavour l"
    },
    {
      "name": "Xmix",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "Xmix[_,_]", "rhs": "0"}
      ],
      "tex": "Subscript[X,lm]",
      "description": "Mixing of the light neutrino mass eigenstate with the RH chiral state of lepton flavour l; zero at collider scales"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kqR*gw/Sqrt[1 - sw^2/(cw^2*kqR^2)]",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[g,ZRq]",
      "description": "Overall ZR coupling strength to quarks"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "klR*gw/Sqrt[1 - sw^2/(cw^2*klR^2)]",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[g,ZRl]",
      "description": "Overall ZR coupling strength to leptons"
    },
    {
      "name": "gZRuL",
      "parameter_type": "Internal",
      "value": "-(1/6)*sw^2/(cw^2*kqR^2)",
      "description": "Left chiral ZR coefficient of up-type quarks, (T3L - Q) tan^2thetaW / kqR^2"
    },
    {
      "name": "gZRuR",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3)*sw^2/(cw^2*kqR^2)",
      "description": "Right chiral ZR coefficient of up-type quarks, T3R - Q tan^2thetaW / kqR^2"
    },
    {
      "name": "gZRdL",
      "parameter_type": "Internal",
      "value": "-(1/6)*sw^2/(cw^2*kqR^2)",
      "description": "Left chiral ZR coefficient of down-type quarks"
    },
    {
      "name": "gZRdR",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3)*sw^2/(cw^2*kqR^2)",
      "description": "Right chiral ZR coefficient of down-type quarks"
    },
    {
      "name": "gZRvL",
      "parameter_type": "Internal",
      "value": "(1/2)*sw^2/(cw^2*klR^2)",
      "description": "Left chiral ZR coefficient of light neutrinos"
    },
    {
      "name": "gZReL",
      "parameter_type": "Internal",
      "value": "(1/2)*sw^2/(cw^2*klR^2)",
      "description": "Left chiral ZR coefficient of charged leptons"
    },
    {
      "name": "gZReR",
      "parameter_type": "Internal",
      "value": "-1/2 + sw^2/(cw^2*klR^2)",
      "description": "Right chiral ZR coefficient of charged leptons"
    },
    {
      "name": "gZRNR",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "Right chiral ZR coefficient of the heavy Majorana neutrinos, T3R = +1/2 and Q = 0"
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
      "pdg": 34,
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
      "pdg": 32,
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
        "sym": "MNR",
        "members": [["mN1", "173.3"], ["mN2", "1.*^12"], ["mN3", "1.*^12"]]
      },
      "width": {
        "sym": "WNR",
        "members": [["WN1", "2.12*^-8"], ["WN2", "1.*^-8"], ["WN3", "1.*^-8"]]
      },
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["N1", "N2", "N3"],
      "propagator_label": "N",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "ExpandIndices[-kqR*gw/Sqrt[2]*CKMR[ff1,ff2]*(uqbar[ff1,cc].Ga[mu].ProjP.dq[ff2,cc])*WR[mu]]"
    },
    {
      "name": "LWRl",
      "delayed": true,
      "expression": "ExpandIndices[-klR*gw/Sqrt[2]*(Xmix[ll,mm]*(vlbar[mm].Ga[mu].ProjP.l[ll]) + Ymix[ll,mm]*(NRbar[mm].Ga[mu].ProjP.l[ll]))*WR[mu]]"
    },
    {
      "name": "LWR",
      "delayed": true,
      "expression": "LWRq + LWRl + HC[LWRq + LWRl]"
    },
    {
      "name": "LZRq",
      "delayed": true,
      "expression": "ExpandIndices[-gZRq*(gZRuL*(uqbar[ff,cc].Ga[mu].ProjM.uq[ff,cc]) + gZRuR*(uqbar[ff,cc].Ga[mu].ProjP.uq[ff,cc]) + gZRdL*(dqbar[ff,cc].Ga[mu].ProjM.dq[ff,cc]) + gZRdR*(dqbar[ff,cc].Ga[mu].ProjP.dq[ff,cc]))*ZR[mu]]"
    },
    {
      "name": "LZRl",
      "delayed": true,
      "expression": "ExpandIndices[-gZRl*(gZRvL*(vlbar[ff].Ga[mu].ProjM.vl[ff]) + gZReL*(lbar[ff].Ga[mu].ProjM.l[ff]) + gZReR*(lbar[ff].Ga[mu].ProjP.l[ff]) + 1/2*gZRNR*(NRbar[ff].Ga[mu].ProjP.NR[ff]))*ZR[mu]]"
    },
    {
      "name": "LZR",
      "delayed": true,
      "expression": "LZRq + LZRl"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LWR + LZR"
    }
  ]
}
```
I have everything I need. Here is the extracted model.

**What the paper contains (Sec. II):** the effective LRSM adds only three kinds of new state — the charged $W_R^\pm$, the neutral $Z_R$, and three heavy Majorana neutrinos $N_{1,2,3}$ aligned with the RH chiral states. The LRSM scalar sector is explicitly decoupled (Sec. II B), so no new scalars enter. New parameters are the two coupling normalizations $\kappa^q_R,\kappa^\ell_R$, the RH CKM matrix $V^{CKM'}$, and the lepton mixing matrices $Y_{\ell m'}$ (heavy) and $X_{\ell m}$ (light). The implemented terms are Eqs. (4), (5) and (8) — see Sec. III A.

One reading note: Eq. (8) as printed shows the square root in the numerator, but the width formula Eq. (14) divides by $[1-(1/\kappa)^2\tan^2\theta_W]$. The two agree only if the coupling is $\kappa g/\sqrt{1-\tan^2\theta_W/\kappa^2}$, which is also what the $SU(2)_R\times U(1)_{B-L}\to U(1)_Y$ rotation gives. I used the denominator form.

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["Olivier Mattelaer", "Manimala Mitra", "Richard Ruiz"],
    "version": "1.0",
    "date": "31. 10. 2016",
    "institutions": [
      "Centre for Cosmology, Particle Physics and Phenomenology (CP3), Universite catholique de Louvain",
      "IISER Mohali",
      "IPPP, Durham University"
    ],
    "emails": [
      "olivier.mattelaer@uclouvain.be",
      "manimala@iisermohali.ac.in",
      "richard.ruiz@durham.ac.uk"
    ]
  },
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kqR",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "LRSM",
      "order_block": 1,
      "tex": "Subscript[\\[Kappa],Rq]",
      "description": "Overall normalization of the WR and ZR coupling strength to quarks"
    },
    {
      "name": "klR",
      "parameter_type": "External",
      "value": "1.",
      "complex": false,
      "block_name": "LRSM",
      "order_block": 2,
      "tex": "Subscript[\\[Kappa],Rl]",
      "description": "Overall normalization of the WR and ZR coupling strength to leptons"
    },
    {
      "name": "CKMR",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "CKMR[1,1]", "rhs": "1"},
        {"lhs": "CKMR[2,2]", "rhs": "1"},
        {"lhs": "CKMR[3,3]", "rhs": "1"},
        {"lhs": "CKMR[i_,j_]", "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)", "delayed": true}
      ],
      "tex": "Superscript[V,CKMp]",
      "description": "Right-handed CKM matrix of the WR quark current; diagonal with unit entries by default"
    },
    {
      "name": "Ymix",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "Ymix[1,1]", "rhs": "1"},
        {"lhs": "Ymix[2,2]", "rhs": "1"},
        {"lhs": "Ymix[3,3]", "rhs": "1"},
        {"lhs": "Ymix[i_,j_]", "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)", "delayed": true}
      ],
      "tex": "Subscript[Y,lm]",
      "description": "Mixing of the heavy Majorana mass eigenstate N with the RH chiral state of lepton flavour l"
    },
    {
      "name": "Xmix",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "Xmix[_,_]", "rhs": "0"}
      ],
      "tex": "Subscript[X,lm]",
      "description": "Mixing of the light neutrino mass eigenstate with the RH chiral state of lepton flavour l; zero at collider scales"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kqR*gw/Sqrt[1 - sw^2/(cw^2*kqR^2)]",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[g,ZRq]",
      "description": "Overall ZR coupling strength to quarks"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "klR*gw/Sqrt[1 - sw^2/(cw^2*klR^2)]",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[g,ZRl]",
      "description": "Overall ZR coupling strength to leptons"
    },
    {
      "name": "gZRuL",
      "parameter_type": "Internal",
      "value": "-(1/6)*sw^2/(cw^2*kqR^2)",
      "description": "Left chiral ZR coefficient of up-type quarks, (T3L - Q) tan^2thetaW / kqR^2"
    },
    {
      "name": "gZRuR",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3)*sw^2/(cw^2*kqR^2)",
      "description": "Right chiral ZR coefficient of up-type quarks, T3R - Q tan^2thetaW / kqR^2"
    },
    {
      "name": "gZRdL",
      "parameter_type": "Internal",
      "value": "-(1/6)*sw^2/(cw^2*kqR^2)",
      "description": "Left chiral ZR coefficient of down-type quarks"
    },
    {
      "name": "gZRdR",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3)*sw^2/(cw^2*kqR^2)",
      "description": "Right chiral ZR coefficient of down-type quarks"
    },
    {
      "name": "gZRvL",
      "parameter_type": "Internal",
      "value": "(1/2)*sw^2/(cw^2*klR^2)",
      "description": "Left chiral ZR coefficient of light neutrinos"
    },
    {
      "name": "gZReL",
      "parameter_type": "Internal",
      "value": "(1/2)*sw^2/(cw^2*klR^2)",
      "description": "Left chiral ZR coefficient of charged leptons"
    },
    {
      "name": "gZReR",
      "parameter_type": "Internal",
      "value": "-1/2 + sw^2/(cw^2*klR^2)",
      "description": "Right chiral ZR coefficient of charged leptons"
    },
    {
      "name": "gZRNR",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "Right chiral ZR coefficient of the heavy Majorana neutrinos, T3R = +1/2 and Q = 0"
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
      "pdg": 34,
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
      "pdg": 32,
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
        "sym": "MNR",
        "members": [["mN1", "173.3"], ["mN2", "1.*^12"], ["mN3", "1.*^12"]]
      },
      "width": {
        "sym": "WNR",
        "members": [["WN1", "2.12*^-8"], ["WN2", "1.*^-8"], ["WN3", "1.*^-8"]]
      },
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["N1", "N2", "N3"],
      "propagator_label": "N",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "ExpandIndices[-kqR*gw/Sqrt[2]*CKMR[ff1,ff2]*(uqbar[ff1,cc].Ga[mu].ProjP.dq[ff2,cc])*WR[mu]]"
    },
    {
      "name": "LWRl",
      "delayed": true,
      "expression": "ExpandIndices[-klR*gw/Sqrt[2]*(Xmix[ll,mm]*(vlbar[mm].Ga[mu].ProjP.l[ll]) + Ymix[ll,mm]*(NRbar[mm].Ga[mu].ProjP.l[ll]))*WR[mu]]"
    },
    {
      "name": "LWR",
      "delayed": true,
      "expression": "LWRq + LWRl + HC[LWRq + LWRl]"
    },
    {
      "name": "LZRq",
      "delayed": true,
      "expression": "ExpandIndices[-gZRq*(gZRuL*(uqbar[ff,cc].Ga[mu].ProjM.uq[ff,cc]) + gZRuR*(uqbar[ff,cc].Ga[mu].ProjP.uq[ff,cc]) + gZRdL*(dqbar[ff,cc].Ga[mu].ProjM.dq[ff,cc]) + gZRdR*(dqbar[ff,cc].Ga[mu].ProjP.dq[ff,cc]))*ZR[mu]]"
    },
    {
      "name": "LZRl",
      "delayed": true,
      "expression": "ExpandIndices[-gZRl*(gZRvL*(vlbar[ff].Ga[mu].ProjM.vl[ff]) + gZReL*(lbar[ff].Ga[mu].ProjM.l[ff]) + gZReR*(lbar[ff].Ga[mu].ProjP.l[ff]) + 1/2*gZRNR*(NRbar[ff].Ga[mu].ProjP.NR[ff]))*ZR[mu]]"
    },
    {
      "name": "LZR",
      "delayed": true,
      "expression": "LZRq + LZRl"
    },
    {
      "name": "LEffLRSM",
      "delayed": true,
      "expression": "LWR + LZR"
    }
  ]
}
```