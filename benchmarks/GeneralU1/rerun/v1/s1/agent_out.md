I'll start by reading the paper, schema, and SM file.
I've read the paper (Sec. II is the full model), the schema, and SM.fr. The new physics content: a U(1)X gauge boson Z′, three generations of right-handed Majorana neutrinos, and a SM-singlet complex scalar Φ (physical scalar φ + Goldstone eaten by Z′), with charges parameterised by xH and xΦ.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["Arindam Das", "P. S. Bhupal Dev", "Yutaka Hosotani", "Sanjoy Mandal"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["Kyungpook National University", "Hokkaido University", "Washington University in St. Louis", "Osaka University", "IFIC CSIC/Universitat de Valencia"],
    "emails": ["arindamdas@oia.hokudai.ac.jp", "bdev@wustl.edu", "hosotani@het.phys.sci.osaka-u.ac.jp", "smandal@ific.uv.es"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "feynman_gauge": true,
  "vevs": [["Phi[2]", "vev"], ["PhiX", "vX"]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "ZPRIME",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g'",
      "description": "U(1)X gauge coupling constant g'"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)X charge parameter of the SM Higgs doublet (xH); xH = 0 gives B-L, xH = -2 gives U(1)R"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 3,
      "tex": "x_Phi",
      "description": "U(1)X charge parameter of the SM-singlet scalar Phi (xPhi), fixed to 1 without loss of generality"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.001",
      "block_name": "ZPRIME",
      "order_block": 4,
      "interaction_order": ["NP", 2],
      "tex": "lambda'",
      "description": "Higgs portal quartic coupling lambda' between H and Phi"
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
      "tex": "Y_nu",
      "description": "Dirac neutrino Yukawa coupling matrix Y_nu between LL, H and NR"
    },
    {
      "name": "xQ",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)X charge of the left-handed quark doublet qL"
    },
    {
      "name": "xU",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed up-type quark uR"
    },
    {
      "name": "xD",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed down-type quark dR"
    },
    {
      "name": "xL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)X charge of the left-handed lepton doublet lL"
    },
    {
      "name": "xE",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)X charge of the right-handed charged lepton eR"
    },
    {
      "name": "xN",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)X charge of the right-handed neutrino NR"
    },
    {
      "name": "xHd",
      "parameter_type": "Internal",
      "value": "-xH/2",
      "description": "U(1)X charge of the SM Higgs doublet H"
    },
    {
      "name": "xS",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "description": "U(1)X charge of the SM-singlet scalar Phi"
    },
    {
      "name": "vX",
      "parameter_type": "Internal",
      "value": "Sqrt[MZp^2/gX^2 - xH^2*vev^2/4]/2",
      "tex": "v_Phi",
      "description": "Vacuum expectation value of the U(1)X singlet scalar Phi, from MZp = gX Sqrt[4 vX^2 + xH^2 vev^2/4]"
    },
    {
      "name": "lamX",
      "parameter_type": "Internal",
      "value": "MphiX^2/(2*vX^2)",
      "tex": "lambda_Phi",
      "description": "Quartic self coupling of the U(1)X singlet scalar Phi"
    },
    {
      "name": "muX",
      "parameter_type": "Internal",
      "value": "Sqrt[vX^2*lamX]",
      "tex": "m_Phi",
      "description": "Quadratic mass parameter of the U(1)X singlet scalar potential"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "yN[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "yN[1,1]", "rhs": "Sqrt[2] MN1/vX"},
        {"lhs": "yN[2,2]", "rhs": "Sqrt[2] MN2/vX"},
        {"lhs": "yN[3,3]", "rhs": "Sqrt[2] MN3/vX"}
      ],
      "tex": "Y_N",
      "description": "Majorana Yukawa coupling of the singlet scalar Phi to the right-handed neutrinos"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 5,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "100."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 32,
      "particle_name": "Zp",
      "full_name": "Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "phiX",
      "self_conjugate": true,
      "mass": {"sym": "MphiX", "value": "500."},
      "width": {"sym": "WphiX", "value": "1."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9000025,
      "particle_name": "phiX",
      "full_name": "U1X Higgs boson",
      "propagator_label": "phiX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "GZp",
      "self_conjugate": true,
      "goldstone": "Zp",
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "100."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9000250,
      "particle_name": "GZp",
      "full_name": "GZp",
      "propagator_label": "GZp",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 5,
      "class_name": "N",
      "self_conjugate": true,
      "class_members": ["N1", "N2", "N3"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "mass": {"sym": "MN", "members": [["MN1", "8000."], ["MN2", "8000."], ["MN3", "8000."]]},
      "width": {"sym": "WN", "members": [["WN1", "1."], ["WN2", "1."], ["WN3", "1."]]},
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["Heavy neutrino 1", "Heavy neutrino 2", "Heavy neutrino 3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "U",
      "class_index": 5,
      "class_name": "ghZp",
      "self_conjugate": false,
      "ghost": "Zp",
      "quantum_numbers": {"GhostNumber": "1"},
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "100."},
      "propagator_label": "uZp",
      "propagator_type": "GhostDash",
      "propagator_arrow": "Forward"
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
      "definitions": ["NR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] N[sp2,ff]]"]
    },
    {
      "spin_type": "S",
      "class_index": 12,
      "class_name": "PhiX",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "0"},
      "unphysical": true,
      "definitions": ["PhiX -> (vX + phiX + I GZp)/Sqrt[2]"]
    }
  ],
  "gauge_xi": [
    ["V[5]", "GaugeXi[Zp]"],
    ["S[4]", "1"],
    ["S[5]", "GaugeXi[Zp]"],
    ["U[5]", "GaugeXi[Zp]"]
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu]]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gX Zp[mu] (xQ (uqbar.Ga[mu].ProjM.uq + dqbar.Ga[mu].ProjM.dq) + xU uqbar.Ga[mu].ProjP.uq + xD dqbar.Ga[mu].ProjP.dq + xL (vlbar.Ga[mu].ProjM.vl + lbar.Ga[mu].ProjM.l) + xE lbar.Ga[mu].ProjP.l + xN Nbar.Ga[mu].ProjP.N)]]"
    },
    {
      "name": "LZpH",
      "delayed": true,
      "expression": "Block[{mu,ii}, ExpandIndices[I gX xHd Zp[mu] (Phibar[ii] del[Phi[ii],mu] - Phi[ii] del[Phibar[ii],mu]) + gX^2 xHd^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii], FlavorExpand->SU2D]]"
    },
    {
      "name": "LPhiX",
      "delayed": true,
      "expression": "Block[{mu,ii}, ExpandIndices[(del[PhiXbar,mu] + I gX xS Zp[mu] PhiXbar) (del[PhiX,mu] - I gX xS Zp[mu] PhiX) + muX^2 PhiXbar PhiX - lamX PhiXbar PhiX PhiXbar PhiX - lamHX PhiXbar PhiX Phibar[ii] Phi[ii], FlavorExpand->SU2D]]"
    },
    {
      "name": "LYukN",
      "delayed": true,
      "expression": "Block[{sp1,sp2,ii,jj,ff1,ff2,yuk}, yuk = ExpandIndices[-ynu[ff1,ff2] LLbar[sp1,ii,ff1].NR[sp1,ff2] Phibar[jj] Eps[ii,jj] - 1/2 yN[ff1,ff2] PhiX Nbar[sp1,ff1].ProjP[sp1,sp2].N[sp2,ff2], FlavorExpand->SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LghZp",
      "delayed": true,
      "expression": "Block[{mu}, If[FeynmanGauge, ExpandIndices[-ghZpbar.del[del[ghZp,mu],mu] - gX^2 xS^2 vX (vX + phiX) ghZpbar.ghZp], 0]]"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LZpKin + LZpF + LZpH + LPhiX + LYukN + LghZp"
    }
  ]
}
```
I've read the paper (Sec. II is the full model), the schema, and SM.fr. The new physics content: a U(1)X gauge boson Z′, three generations of right-handed Majorana neutrinos, and a SM-singlet complex scalar Φ (physical scalar φ + Goldstone eaten by Z′), with charges parameterised by xH and xΦ.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["Arindam Das", "P. S. Bhupal Dev", "Yutaka Hosotani", "Sanjoy Mandal"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["Kyungpook National University", "Hokkaido University", "Washington University in St. Louis", "Osaka University", "IFIC CSIC/Universitat de Valencia"],
    "emails": ["arindamdas@oia.hokudai.ac.jp", "bdev@wustl.edu", "hosotani@het.phys.sci.osaka-u.ac.jp", "smandal@ific.uv.es"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "feynman_gauge": true,
  "vevs": [["Phi[2]", "vev"], ["PhiX", "vX"]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "ZPRIME",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g'",
      "description": "U(1)X gauge coupling constant g'"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)X charge parameter of the SM Higgs doublet (xH); xH = 0 gives B-L, xH = -2 gives U(1)R"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 3,
      "tex": "x_Phi",
      "description": "U(1)X charge parameter of the SM-singlet scalar Phi (xPhi), fixed to 1 without loss of generality"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.001",
      "block_name": "ZPRIME",
      "order_block": 4,
      "interaction_order": ["NP", 2],
      "tex": "lambda'",
      "description": "Higgs portal quartic coupling lambda' between H and Phi"
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
      "tex": "Y_nu",
      "description": "Dirac neutrino Yukawa coupling matrix Y_nu between LL, H and NR"
    },
    {
      "name": "xQ",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)X charge of the left-handed quark doublet qL"
    },
    {
      "name": "xU",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed up-type quark uR"
    },
    {
      "name": "xD",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed down-type quark dR"
    },
    {
      "name": "xL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)X charge of the left-handed lepton doublet lL"
    },
    {
      "name": "xE",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)X charge of the right-handed charged lepton eR"
    },
    {
      "name": "xN",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)X charge of the right-handed neutrino NR"
    },
    {
      "name": "xHd",
      "parameter_type": "Internal",
      "value": "-xH/2",
      "description": "U(1)X charge of the SM Higgs doublet H"
    },
    {
      "name": "xS",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "description": "U(1)X charge of the SM-singlet scalar Phi"
    },
    {
      "name": "vX",
      "parameter_type": "Internal",
      "value": "Sqrt[MZp^2/gX^2 - xH^2*vev^2/4]/2",
      "tex": "v_Phi",
      "description": "Vacuum expectation value of the U(1)X singlet scalar Phi, from MZp = gX Sqrt[4 vX^2 + xH^2 vev^2/4]"
    },
    {
      "name": "lamX",
      "parameter_type": "Internal",
      "value": "MphiX^2/(2*vX^2)",
      "tex": "lambda_Phi",
      "description": "Quartic self coupling of the U(1)X singlet scalar Phi"
    },
    {
      "name": "muX",
      "parameter_type": "Internal",
      "value": "Sqrt[vX^2*lamX]",
      "tex": "m_Phi",
      "description": "Quadratic mass parameter of the U(1)X singlet scalar potential"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "yN[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "yN[1,1]", "rhs": "Sqrt[2] MN1/vX"},
        {"lhs": "yN[2,2]", "rhs": "Sqrt[2] MN2/vX"},
        {"lhs": "yN[3,3]", "rhs": "Sqrt[2] MN3/vX"}
      ],
      "tex": "Y_N",
      "description": "Majorana Yukawa coupling of the singlet scalar Phi to the right-handed neutrinos"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 5,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "100."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 32,
      "particle_name": "Zp",
      "full_name": "Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "phiX",
      "self_conjugate": true,
      "mass": {"sym": "MphiX", "value": "500."},
      "width": {"sym": "WphiX", "value": "1."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9000025,
      "particle_name": "phiX",
      "full_name": "U1X Higgs boson",
      "propagator_label": "phiX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "GZp",
      "self_conjugate": true,
      "goldstone": "Zp",
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "100."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9000250,
      "particle_name": "GZp",
      "full_name": "GZp",
      "propagator_label": "GZp",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 5,
      "class_name": "N",
      "self_conjugate": true,
      "class_members": ["N1", "N2", "N3"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "mass": {"sym": "MN", "members": [["MN1", "8000."], ["MN2", "8000."], ["MN3", "8000."]]},
      "width": {"sym": "WN", "members": [["WN1", "1."], ["WN2", "1."], ["WN3", "1."]]},
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["Heavy neutrino 1", "Heavy neutrino 2", "Heavy neutrino 3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "U",
      "class_index": 5,
      "class_name": "ghZp",
      "self_conjugate": false,
      "ghost": "Zp",
      "quantum_numbers": {"GhostNumber": "1"},
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "100."},
      "propagator_label": "uZp",
      "propagator_type": "GhostDash",
      "propagator_arrow": "Forward"
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
      "definitions": ["NR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] N[sp2,ff]]"]
    },
    {
      "spin_type": "S",
      "class_index": 12,
      "class_name": "PhiX",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "0"},
      "unphysical": true,
      "definitions": ["PhiX -> (vX + phiX + I GZp)/Sqrt[2]"]
    }
  ],
  "gauge_xi": [
    ["V[5]", "GaugeXi[Zp]"],
    ["S[4]", "1"],
    ["S[5]", "GaugeXi[Zp]"],
    ["U[5]", "GaugeXi[Zp]"]
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu]]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gX Zp[mu] (xQ (uqbar.Ga[mu].ProjM.uq + dqbar.Ga[mu].ProjM.dq) + xU uqbar.Ga[mu].ProjP.uq + xD dqbar.Ga[mu].ProjP.dq + xL (vlbar.Ga[mu].ProjM.vl + lbar.Ga[mu].ProjM.l) + xE lbar.Ga[mu].ProjP.l + xN Nbar.Ga[mu].ProjP.N)]]"
    },
    {
      "name": "LZpH",
      "delayed": true,
      "expression": "Block[{mu,ii}, ExpandIndices[I gX xHd Zp[mu] (Phibar[ii] del[Phi[ii],mu] - Phi[ii] del[Phibar[ii],mu]) + gX^2 xHd^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii], FlavorExpand->SU2D]]"
    },
    {
      "name": "LPhiX",
      "delayed": true,
      "expression": "Block[{mu,ii}, ExpandIndices[(del[PhiXbar,mu] + I gX xS Zp[mu] PhiXbar) (del[PhiX,mu] - I gX xS Zp[mu] PhiX) + muX^2 PhiXbar PhiX - lamX PhiXbar PhiX PhiXbar PhiX - lamHX PhiXbar PhiX Phibar[ii] Phi[ii], FlavorExpand->SU2D]]"
    },
    {
      "name": "LYukN",
      "delayed": true,
      "expression": "Block[{sp1,sp2,ii,jj,ff1,ff2,yuk}, yuk = ExpandIndices[-ynu[ff1,ff2] LLbar[sp1,ii,ff1].NR[sp1,ff2] Phibar[jj] Eps[ii,jj] - 1/2 yN[ff1,ff2] PhiX Nbar[sp1,ff1].ProjP[sp1,sp2].N[sp2,ff2], FlavorExpand->SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LghZp",
      "delayed": true,
      "expression": "Block[{mu}, If[FeynmanGauge, ExpandIndices[-ghZpbar.del[del[ghZp,mu],mu] - gX^2 xS^2 vX (vX + phiX) ghZpbar.ghZp], 0]]"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LZpKin + LZpF + LZpH + LPhiX + LYukN + LghZp"
    }
  ]
}
```