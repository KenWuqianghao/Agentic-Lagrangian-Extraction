```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:2104.10902 (A. Das, P. S. B. Dev, Y. Hosotani, S. Mandal)"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gpX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "U1XINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "U(1)X gauge coupling g-prime, Eq. Lag1; LEP-allowed benchmark 0.4 for M_Zp = 7.5 TeV"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "U1XINPUTS",
      "order_block": 2,
      "description": "U(1)X charge parameter x_H, Table I; benchmarks -2, -1, -0.5, 0, 0.5, 1, 2; x_H = 0 is the B-L case"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "U1XINPUTS",
      "order_block": 3,
      "description": "U(1)X charge parameter x_Phi, Table I; fixed to 1 without loss of generality in the paper"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.001",
      "block_name": "U1XINPUTS",
      "order_block": 4,
      "interaction_order": ["NP", 1],
      "description": "Higgs portal quartic lambda-prime of (Hdag H)(Phidag Phi); the paper takes it small so that h-phi mixing is negligible"
    },
    {
      "name": "ynu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "YNU",
      "value_rules": [
        {"lhs": "ynu[1,1]", "rhs": "1.*^-6"},
        {"lhs": "ynu[1,2]", "rhs": "0."},
        {"lhs": "ynu[1,3]", "rhs": "0."},
        {"lhs": "ynu[2,1]", "rhs": "0."},
        {"lhs": "ynu[2,2]", "rhs": "1.*^-6"},
        {"lhs": "ynu[2,3]", "rhs": "0."},
        {"lhs": "ynu[3,1]", "rhs": "0."},
        {"lhs": "ynu[3,2]", "rhs": "0."},
        {"lhs": "ynu[3,3]", "rhs": "1.*^-6"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Dirac neutrino Yukawa Y_nu of Eq.(1); m_D = Y_nu v/Sqrt[2]"
    },
    {
      "name": "xQL",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)X charge of the quark doublet q_L, Table I"
    },
    {
      "name": "xuR",
      "parameter_type": "Internal",
      "value": "2 xH/3 + xPhi/3",
      "description": "U(1)X charge of u_R, Table I"
    },
    {
      "name": "xdR",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)X charge of d_R, Table I"
    },
    {
      "name": "xLL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)X charge of the lepton doublet l_L, Table I"
    },
    {
      "name": "xlR",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)X charge of e_R, Table I"
    },
    {
      "name": "xNR",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)X charge of the right-handed neutrino N_R, Table I"
    },
    {
      "name": "xPhiH",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)X charge of the SM.fr Higgs doublet Phi with Y = +1/2. Table I lists -x_H/2 for the papers H, which is the conjugate doublet i tau2 H* used in its Yukawa equation; re-derived from invariance of all Yukawas in SM.fr conventions"
    },
    {
      "name": "xChi",
      "parameter_type": "Internal",
      "value": "2 xPhi",
      "description": "U(1)X charge of the SM-singlet scalar Phi, Table I"
    },
    {
      "name": "vX",
      "parameter_type": "Internal",
      "value": "Sqrt[MZp^2/gpX^2 - xH^2 vev^2/4]/2",
      "interaction_order": ["NP", -1],
      "description": "U(1)X vacuum expectation value v_Phi, inverted from M_Zp = gpX Sqrt[4 v_Phi^2 + x_H^2 v^2/4]; about 9375 GeV for the benchmark"
    },
    {
      "name": "WZp",
      "parameter_type": "Internal",
      "value": "MZp gpX^2/(24 Pi) (9 (xQL^2 + xuR^2) + 9 (xQL^2 + xdR^2) + 3 (xLL^2 + xlR^2) + 3 xLL^2)",
      "description": "Total Zp width into SM fermions from Eqs.(5) and (6); the N N channel is closed because m_N > M_Zp"
    },
    {
      "name": "MNm",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "MNm[1,1]", "rhs": "MN1"},
        {"lhs": "MNm[1,2]", "rhs": "0"},
        {"lhs": "MNm[1,3]", "rhs": "0"},
        {"lhs": "MNm[2,1]", "rhs": "0"},
        {"lhs": "MNm[2,2]", "rhs": "MN2"},
        {"lhs": "MNm[2,3]", "rhs": "0"},
        {"lhs": "MNm[3,1]", "rhs": "0"},
        {"lhs": "MNm[3,2]", "rhs": "0"},
        {"lhs": "MNm[3,3]", "rhs": "MN3"}
      ],
      "description": "Diagonal Majorana mass matrix of the right-handed neutrinos in GeV"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yN[1,1]", "rhs": "Sqrt[2] MN1/vX"},
        {"lhs": "yN[1,2]", "rhs": "0"},
        {"lhs": "yN[1,3]", "rhs": "0"},
        {"lhs": "yN[2,1]", "rhs": "0"},
        {"lhs": "yN[2,2]", "rhs": "Sqrt[2] MN2/vX"},
        {"lhs": "yN[2,3]", "rhs": "0"},
        {"lhs": "yN[3,1]", "rhs": "0"},
        {"lhs": "yN[3,2]", "rhs": "0"},
        {"lhs": "yN[3,3]", "rhs": "Sqrt[2] MN3/vX"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Majorana Yukawa Y_N of Eq.(1), diagonal in generation space; m_N = Y_N v_Phi/Sqrt[2], hence Y_N = Sqrt[2] m_N/v_Phi"
    },
    {
      "name": "lamX",
      "parameter_type": "Internal",
      "value": "MphiX^2/(2 vX^2)",
      "interaction_order": ["NP", 2],
      "description": "Quartic coupling lambda_Phi of the singlet potential; m_phi^2 = 2 lambda_Phi v_Phi^2"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "Internal"},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "U1X gauge boson Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "phiX",
      "self_conjugate": true,
      "mass": {"sym": "MphiX", "value": "2000."},
      "width": {"sym": "WphiX", "value": "1."},
      "pdg": 9900025,
      "particle_name": "phiX",
      "full_name": "U1X Higgs boson",
      "propagator_label": "phiX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NR",
      "self_conjugate": true,
      "class_members": ["N1", "N2", "N3"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "mass": {"sym": "MN", "members": [["MN1", "10000."], ["MN2", "10000."], ["MN3", "10000."]]},
      "width": {"sym": "WN", "members": [["WN1", "1."], ["WN2", "1."], ["WN3", "1."]]},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["Heavy neutrino 1", "Heavy neutrino 2", "Heavy neutrino 3"],
      "propagator_label": "NR",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu, nu}, ExpandIndices[-1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]]"
    },
    {
      "name": "LphiXKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[1/2 del[phiX, mu] del[phiX, mu] - 1/2 MphiX^2 phiX^2]]"
    },
    {
      "name": "LphiXPot",
      "delayed": true,
      "expression": "-lamX vX phiX^3 - lamX/4 phiX^4"
    },
    {
      "name": "LphiXZp",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[gpX^2 xChi^2 (vX phiX + phiX^2/2) Zp[mu] Zp[mu]]]"
    },
    {
      "name": "LHZp",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[gpX^2 xPhiH^2 (vev H + H^2/2) Zp[mu] Zp[mu]]]"
    },
    {
      "name": "LPortalX",
      "delayed": true,
      "expression": "-lamHX/2 vev H phiX^2 - lamHX/2 vX H^2 phiX - lamHX/4 H^2 phiX^2"
    },
    {
      "name": "LNKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I/2 NRbar.Ga[mu].del[NR, mu] - 1/2 NRbar.MNm.NR]]"
    },
    {
      "name": "LNphiX",
      "delayed": true,
      "expression": "-1/(2 Sqrt[2]) phiX NRbar.yN.NR"
    },
    {
      "name": "LNuYuk",
      "delayed": true,
      "expression": "Block[{yuk}, yuk = -1/Sqrt[2] H vlbar.ynu.ProjP.NR; ExpandIndices[yuk + HC[yuk]]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gpX Zp[mu] (xQL (uqbar.Ga[mu].ProjM.uq + dqbar.Ga[mu].ProjM.dq) + xuR uqbar.Ga[mu].ProjP.uq + xdR dqbar.Ga[mu].ProjP.dq + xLL (vlbar.Ga[mu].ProjM.vl + lbar.Ga[mu].ProjM.l) + xlR lbar.Ga[mu].ProjP.l + xNR NRbar.Ga[mu].ProjP.NR)]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LZpKin + LphiXKin + LphiXPot + LphiXZp + LHZp + LPortalX + LNKin + LNphiX + LNuYuk + LZpF"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```