I'll start by reading the paper and the schema.
I read the paper (Sec. II holds all the model content) and the pydantic schema. Here is the extraction.

**Model content found in arXiv:2104.10902 (minimal U(1)X extension):**

| New state | Spin | Colour | SU(2)L | Q | Y | U(1)X | Mass |
|---|---|---|---|---|---|---|---|
| Z′ (U(1)X gauge boson) | V | singlet | 1 | 0 | 0 | — | MZp = g′√(4v_Φ²+x_H²v²/4) |
| N_R^i (3 gen. RH neutrinos, Majorana) | F | singlet | 1 | 0 | 0 | −x_Φ | m_N = y_N v_Φ/√2 |
| φ (real scalar from Φ) | S | singlet | 1 | 0 | 0 | 2x_Φ | √(2λ_Φ) v_Φ |
| G_Z′ (Goldstone eaten by Z′) | S | singlet | 1 | 0 | 0 | 2x_Φ | MZp |
| Φ (unphysical complex singlet) | S | singlet | 1 | 0 | 0 | 2x_Φ | — |

New parameters: g′, x_H, x_Φ, v_Φ, λ_Φ, λ′, Y_N (Majorana), Y_ν (Dirac). SM charges under U(1)X are internal combinations of x_H and x_Φ (Table I).

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
    "date": "2026-09-02",
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
  "interaction_order_hierarchy": [["QCD", 1], ["NP", 1], ["QED", 2]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "ZPINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g'",
      "description": "U(1)X gauge coupling g'"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPINPUTS",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)X charge parameter of the SM Higgs doublet (xH = 0 gives B-L, xH = -2 gives U(1)R)"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPINPUTS",
      "order_block": 3,
      "tex": "x_\\Phi",
      "description": "U(1)X charge parameter of the SM-singlet scalar Phi (fixed to 1 in the paper)"
    },
    {
      "name": "vX",
      "parameter_type": "External",
      "value": "9375.",
      "block_name": "ZPINPUTS",
      "order_block": 4,
      "tex": "v_\\Phi",
      "description": "U(1)X breaking vacuum expectation value of the singlet scalar Phi"
    },
    {
      "name": "lamPhi",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "ZPINPUTS",
      "order_block": 5,
      "tex": "\\lambda_\\Phi",
      "description": "Quartic self coupling of the U(1)X singlet scalar Phi"
    },
    {
      "name": "lamMix",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "ZPINPUTS",
      "order_block": 6,
      "tex": "\\lambda'",
      "description": "Portal coupling lambda' between the SM Higgs doublet and the singlet Phi"
    },
    {
      "name": "yN",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "YNMAJ",
      "value_rules": [
        {"lhs": "yN[1]", "rhs": "1.5"},
        {"lhs": "yN[2]", "rhs": "1.5"},
        {"lhs": "yN[3]", "rhs": "1.5"}
      ],
      "tex": "y_N",
      "description": "Majorana Yukawa coupling Y_N of the right-handed neutrinos to Phi"
    },
    {
      "name": "ynu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "YNDIRAC",
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
      "tex": "y_\\nu",
      "description": "Dirac Yukawa coupling Y_nu between the lepton doublet, the SM Higgs and N_R"
    },
    {
      "name": "xq",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "tex": "x_{q}",
      "description": "U(1)X charge of the left-handed quark doublet qL"
    },
    {
      "name": "xu",
      "parameter_type": "Internal",
      "value": "(2*xH)/3 + xPhi/3",
      "tex": "x_{u}",
      "description": "U(1)X charge of the right-handed up-type quark uR"
    },
    {
      "name": "xd",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "tex": "x_{d}",
      "description": "U(1)X charge of the right-handed down-type quark dR"
    },
    {
      "name": "xl",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "tex": "x_{\\ell}",
      "description": "U(1)X charge of the left-handed lepton doublet lL"
    },
    {
      "name": "xe",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "tex": "x_{e}",
      "description": "U(1)X charge of the right-handed charged lepton eR"
    },
    {
      "name": "xn",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "tex": "x_{N}",
      "description": "U(1)X charge of the right-handed neutrino NR"
    },
    {
      "name": "xHd",
      "parameter_type": "Internal",
      "value": "xH/2",
      "tex": "x_{H}/2",
      "description": "U(1)X charge of the SM Higgs doublet H"
    },
    {
      "name": "xPh",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "tex": "2 x_\\Phi",
      "description": "U(1)X charge of the SM-singlet scalar Phi"
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "gX*Sqrt[4*vX^2 + (xH^2*vev^2)/4]",
      "tex": "M_{Z'}",
      "description": "Z' mass from U(1)X and electroweak symmetry breaking (Eq. 4)"
    },
    {
      "name": "muX2",
      "parameter_type": "Internal",
      "value": "-lamPhi*vX^2",
      "tex": "m_\\Phi^2",
      "description": "Quadratic term of the singlet scalar potential at the minimum"
    },
    {
      "name": "Mphi",
      "parameter_type": "Internal",
      "value": "Sqrt[2*lamPhi]*vX",
      "tex": "m_\\phi",
      "description": "Mass of the physical U(1)X scalar phi"
    },
    {
      "name": "Mvr1",
      "parameter_type": "Internal",
      "value": "yN[1]*vX/Sqrt[2]",
      "tex": "m_{N_1}",
      "description": "Majorana mass of the first right-handed neutrino"
    },
    {
      "name": "Mvr2",
      "parameter_type": "Internal",
      "value": "yN[2]*vX/Sqrt[2]",
      "tex": "m_{N_2}",
      "description": "Majorana mass of the second right-handed neutrino"
    },
    {
      "name": "Mvr3",
      "parameter_type": "Internal",
      "value": "yN[3]*vX/Sqrt[2]",
      "tex": "m_{N_3}",
      "description": "Majorana mass of the third right-handed neutrino"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 21,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "10."},
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
      "class_index": 21,
      "class_name": "vr",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["vr1", "vr2", "vr3"],
      "mass": {
        "sym": "Mvr",
        "members": [["Mvr1", "Internal"], ["Mvr2", "Internal"], ["Mvr3", "Internal"]]
      },
      "width": {
        "sym": "Wvr",
        "members": [["Wvr1", "1."], ["Wvr2", "1."], ["Wvr3", "1."]]
      },
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["vr1", "vr2", "vr3"],
      "full_name": ["vr1", "vr2", "vr3"],
      "propagator_label": ["vr1", "vr2", "vr3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 21,
      "class_name": "phi",
      "self_conjugate": true,
      "mass": {"sym": "Mphi", "value": "Internal"},
      "width": {"sym": "Wphi", "value": "1."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900025,
      "particle_name": "phi",
      "full_name": "phi",
      "propagator_label": "phi",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 22,
      "class_name": "GZp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "Internal"},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900021,
      "particle_name": "GZp",
      "full_name": "GZp",
      "propagator_label": "GZp",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None",
      "goldstone": "Zp"
    },
    {
      "spin_type": "S",
      "class_index": 23,
      "class_name": "PhiX",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Q": "0"},
      "definitions": ["PhiX -> (vX + phi + I*GZp)/Sqrt[2]"]
    }
  ],
  "gauge_xi": [["Zp", "1"]],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "expression": "-1/4*FS[Zp,mu,nu]*FS[Zp,mu,nu]",
      "delayed": true
    },
    {
      "name": "LZpFerm",
      "expression": "-gX*Zp[mu]*( xq*(uqbar.Ga[mu].ProjM.uq + dqbar.Ga[mu].ProjM.dq) + xu*uqbar.Ga[mu].ProjP.uq + xd*dqbar.Ga[mu].ProjP.dq + xl*(vlbar.Ga[mu].ProjM.vl + lbar.Ga[mu].ProjM.l) + xe*lbar.Ga[mu].ProjP.l + xn*vrbar.Ga[mu].ProjP.vr )",
      "delayed": true
    },
    {
      "name": "LNRkin",
      "expression": "1/2*(I*vrbar.Ga[mu].del[vr,mu])",
      "delayed": true
    },
    {
      "name": "LNRmaj",
      "expression": "-1/2*yN[ff]*PhiX*vrbar[ff].ProjP.vr[ff] - 1/2*Conjugate[yN[ff]]*PhiXbar*vrbar[ff].ProjM.vr[ff]",
      "delayed": true
    },
    {
      "name": "LNRdirac",
      "expression": "-ynu[ff,gg]*LLbar[sp,ii,ff].vr[sp,gg]*Phibar[ii] + HC[-ynu[ff,gg]*LLbar[sp,ii,ff].vr[sp,gg]*Phibar[ii]]",
      "delayed": true
    },
    {
      "name": "LPhiX",
      "expression": "del[PhiXbar,mu]*del[PhiX,mu] + I*xPh*gX*Zp[mu]*(del[PhiXbar,mu]*PhiX - PhiXbar*del[PhiX,mu]) + xPh^2*gX^2*Zp[mu]*Zp[mu]*PhiXbar*PhiX - muX2*PhiXbar*PhiX - lamPhi*(PhiXbar*PhiX)^2 - lamMix*(PhiXbar*PhiX)*(Phibar[ii]*Phi[ii])",
      "delayed": true
    },
    {
      "name": "LHiggsX",
      "expression": "I*xHd*gX*Zp[mu]*(DC[Phibar[ii],mu]*Phi[ii] - Phibar[ii]*DC[Phi[ii],mu]) + xHd^2*gX^2*Zp[mu]*Zp[mu]*Phibar[ii]*Phi[ii]",
      "delayed": true
    },
    {
      "name": "LGeneralU1",
      "expression": "LZpKin + LZpFerm + LNRkin + LNRmaj + LNRdirac + LPhiX + LHiggsX",
      "delayed": true
    }
  ]
}
```
I read the paper (Sec. II holds all the model content) and the pydantic schema. Here is the extraction.

**Model content found in arXiv:2104.10902 (minimal U(1)X extension):**

| New state | Spin | Colour | SU(2)L | Q | Y | U(1)X | Mass |
|---|---|---|---|---|---|---|---|
| Z′ (U(1)X gauge boson) | V | singlet | 1 | 0 | 0 | — | MZp = g′√(4v_Φ²+x_H²v²/4) |
| N_R^i (3 gen. RH neutrinos, Majorana) | F | singlet | 1 | 0 | 0 | −x_Φ | m_N = y_N v_Φ/√2 |
| φ (real scalar from Φ) | S | singlet | 1 | 0 | 0 | 2x_Φ | √(2λ_Φ) v_Φ |
| G_Z′ (Goldstone eaten by Z′) | S | singlet | 1 | 0 | 0 | 2x_Φ | MZp |
| Φ (unphysical complex singlet) | S | singlet | 1 | 0 | 0 | 2x_Φ | — |

New parameters: g′, x_H, x_Φ, v_Φ, λ_Φ, λ′, Y_N (Majorana), Y_ν (Dirac). SM charges under U(1)X are internal combinations of x_H and x_Φ (Table I).

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
    "date": "2026-09-02",
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
  "interaction_order_hierarchy": [["QCD", 1], ["NP", 1], ["QED", 2]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "ZPINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g'",
      "description": "U(1)X gauge coupling g'"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPINPUTS",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)X charge parameter of the SM Higgs doublet (xH = 0 gives B-L, xH = -2 gives U(1)R)"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPINPUTS",
      "order_block": 3,
      "tex": "x_\\Phi",
      "description": "U(1)X charge parameter of the SM-singlet scalar Phi (fixed to 1 in the paper)"
    },
    {
      "name": "vX",
      "parameter_type": "External",
      "value": "9375.",
      "block_name": "ZPINPUTS",
      "order_block": 4,
      "tex": "v_\\Phi",
      "description": "U(1)X breaking vacuum expectation value of the singlet scalar Phi"
    },
    {
      "name": "lamPhi",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "ZPINPUTS",
      "order_block": 5,
      "tex": "\\lambda_\\Phi",
      "description": "Quartic self coupling of the U(1)X singlet scalar Phi"
    },
    {
      "name": "lamMix",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "ZPINPUTS",
      "order_block": 6,
      "tex": "\\lambda'",
      "description": "Portal coupling lambda' between the SM Higgs doublet and the singlet Phi"
    },
    {
      "name": "yN",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "YNMAJ",
      "value_rules": [
        {"lhs": "yN[1]", "rhs": "1.5"},
        {"lhs": "yN[2]", "rhs": "1.5"},
        {"lhs": "yN[3]", "rhs": "1.5"}
      ],
      "tex": "y_N",
      "description": "Majorana Yukawa coupling Y_N of the right-handed neutrinos to Phi"
    },
    {
      "name": "ynu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "YNDIRAC",
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
      "tex": "y_\\nu",
      "description": "Dirac Yukawa coupling Y_nu between the lepton doublet, the SM Higgs and N_R"
    },
    {
      "name": "xq",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "tex": "x_{q}",
      "description": "U(1)X charge of the left-handed quark doublet qL"
    },
    {
      "name": "xu",
      "parameter_type": "Internal",
      "value": "(2*xH)/3 + xPhi/3",
      "tex": "x_{u}",
      "description": "U(1)X charge of the right-handed up-type quark uR"
    },
    {
      "name": "xd",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "tex": "x_{d}",
      "description": "U(1)X charge of the right-handed down-type quark dR"
    },
    {
      "name": "xl",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "tex": "x_{\\ell}",
      "description": "U(1)X charge of the left-handed lepton doublet lL"
    },
    {
      "name": "xe",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "tex": "x_{e}",
      "description": "U(1)X charge of the right-handed charged lepton eR"
    },
    {
      "name": "xn",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "tex": "x_{N}",
      "description": "U(1)X charge of the right-handed neutrino NR"
    },
    {
      "name": "xHd",
      "parameter_type": "Internal",
      "value": "xH/2",
      "tex": "x_{H}/2",
      "description": "U(1)X charge of the SM Higgs doublet H"
    },
    {
      "name": "xPh",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "tex": "2 x_\\Phi",
      "description": "U(1)X charge of the SM-singlet scalar Phi"
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "gX*Sqrt[4*vX^2 + (xH^2*vev^2)/4]",
      "tex": "M_{Z'}",
      "description": "Z' mass from U(1)X and electroweak symmetry breaking (Eq. 4)"
    },
    {
      "name": "muX2",
      "parameter_type": "Internal",
      "value": "-lamPhi*vX^2",
      "tex": "m_\\Phi^2",
      "description": "Quadratic term of the singlet scalar potential at the minimum"
    },
    {
      "name": "Mphi",
      "parameter_type": "Internal",
      "value": "Sqrt[2*lamPhi]*vX",
      "tex": "m_\\phi",
      "description": "Mass of the physical U(1)X scalar phi"
    },
    {
      "name": "Mvr1",
      "parameter_type": "Internal",
      "value": "yN[1]*vX/Sqrt[2]",
      "tex": "m_{N_1}",
      "description": "Majorana mass of the first right-handed neutrino"
    },
    {
      "name": "Mvr2",
      "parameter_type": "Internal",
      "value": "yN[2]*vX/Sqrt[2]",
      "tex": "m_{N_2}",
      "description": "Majorana mass of the second right-handed neutrino"
    },
    {
      "name": "Mvr3",
      "parameter_type": "Internal",
      "value": "yN[3]*vX/Sqrt[2]",
      "tex": "m_{N_3}",
      "description": "Majorana mass of the third right-handed neutrino"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 21,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "10."},
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
      "class_index": 21,
      "class_name": "vr",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["vr1", "vr2", "vr3"],
      "mass": {
        "sym": "Mvr",
        "members": [["Mvr1", "Internal"], ["Mvr2", "Internal"], ["Mvr3", "Internal"]]
      },
      "width": {
        "sym": "Wvr",
        "members": [["Wvr1", "1."], ["Wvr2", "1."], ["Wvr3", "1."]]
      },
      "quantum_numbers": {"Q": "0"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["vr1", "vr2", "vr3"],
      "full_name": ["vr1", "vr2", "vr3"],
      "propagator_label": ["vr1", "vr2", "vr3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 21,
      "class_name": "phi",
      "self_conjugate": true,
      "mass": {"sym": "Mphi", "value": "Internal"},
      "width": {"sym": "Wphi", "value": "1."},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900025,
      "particle_name": "phi",
      "full_name": "phi",
      "propagator_label": "phi",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 22,
      "class_name": "GZp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "Internal"},
      "quantum_numbers": {"Q": "0"},
      "pdg": 9900021,
      "particle_name": "GZp",
      "full_name": "GZp",
      "propagator_label": "GZp",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None",
      "goldstone": "Zp"
    },
    {
      "spin_type": "S",
      "class_index": 23,
      "class_name": "PhiX",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Q": "0"},
      "definitions": ["PhiX -> (vX + phi + I*GZp)/Sqrt[2]"]
    }
  ],
  "gauge_xi": [["Zp", "1"]],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "expression": "-1/4*FS[Zp,mu,nu]*FS[Zp,mu,nu]",
      "delayed": true
    },
    {
      "name": "LZpFerm",
      "expression": "-gX*Zp[mu]*( xq*(uqbar.Ga[mu].ProjM.uq + dqbar.Ga[mu].ProjM.dq) + xu*uqbar.Ga[mu].ProjP.uq + xd*dqbar.Ga[mu].ProjP.dq + xl*(vlbar.Ga[mu].ProjM.vl + lbar.Ga[mu].ProjM.l) + xe*lbar.Ga[mu].ProjP.l + xn*vrbar.Ga[mu].ProjP.vr )",
      "delayed": true
    },
    {
      "name": "LNRkin",
      "expression": "1/2*(I*vrbar.Ga[mu].del[vr,mu])",
      "delayed": true
    },
    {
      "name": "LNRmaj",
      "expression": "-1/2*yN[ff]*PhiX*vrbar[ff].ProjP.vr[ff] - 1/2*Conjugate[yN[ff]]*PhiXbar*vrbar[ff].ProjM.vr[ff]",
      "delayed": true
    },
    {
      "name": "LNRdirac",
      "expression": "-ynu[ff,gg]*LLbar[sp,ii,ff].vr[sp,gg]*Phibar[ii] + HC[-ynu[ff,gg]*LLbar[sp,ii,ff].vr[sp,gg]*Phibar[ii]]",
      "delayed": true
    },
    {
      "name": "LPhiX",
      "expression": "del[PhiXbar,mu]*del[PhiX,mu] + I*xPh*gX*Zp[mu]*(del[PhiXbar,mu]*PhiX - PhiXbar*del[PhiX,mu]) + xPh^2*gX^2*Zp[mu]*Zp[mu]*PhiXbar*PhiX - muX2*PhiXbar*PhiX - lamPhi*(PhiXbar*PhiX)^2 - lamMix*(PhiXbar*PhiX)*(Phibar[ii]*Phi[ii])",
      "delayed": true
    },
    {
      "name": "LHiggsX",
      "expression": "I*xHd*gX*Zp[mu]*(DC[Phibar[ii],mu]*Phi[ii] - Phibar[ii]*DC[Phi[ii],mu]) + xHd^2*gX^2*Zp[mu]*Zp[mu]*Phibar[ii]*Phi[ii]",
      "delayed": true
    },
    {
      "name": "LGeneralU1",
      "expression": "LZpKin + LZpFerm + LNRkin + LNRmaj + LNRdirac + LPhiX + LHiggsX",
      "delayed": true
    }
  ]
}
```