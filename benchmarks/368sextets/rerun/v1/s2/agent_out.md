I'll start by reading the paper and the schema.
I've read the paper, the schema, the renderer, and SM.fr. The physics content is Table X plus Eqs. (12)–(13): four new colour-sextet states (two scalars, two Dirac fermions), all SU(2) singlets, coupled to a quark and a gluon through the 3⊗6⊗8 invariant.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["Linda M. Carpenter", "Taylor Murphy", "Tim M. P. Tait"],
    "version": "1.0",
    "date": "07. 09. 2022",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 3]],
  "feynman_gauge": null,
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Sextet",
      "range_kind": "NoUnfold",
      "size": 6,
      "style_symbol": "sx"
    }
  ],
  "parameters": [
    {
      "name": "LamPsiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 1,
      "tex": "\\Lambda_{\\Psi_u}",
      "description": "EFT cutoff of the dimension-five up-type sextet-fermion / quark / gluon operator, Eq. (12)"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 2,
      "tex": "\\Lambda_{\\Psi_d}",
      "description": "EFT cutoff of the dimension-five down-type sextet-fermion / quark / gluon operator, Eq. (12)"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 3,
      "tex": "\\Lambda_{\\Psi_u B}",
      "description": "EFT cutoff of the dimension-seven up-type sextet-fermion / quark / gluon / B operator, Eq. (12)"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 4,
      "tex": "\\Lambda_{\\Psi_d B}",
      "description": "EFT cutoff of the dimension-seven down-type sextet-fermion / quark / gluon / B operator, Eq. (12)"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 5,
      "tex": "\\Lambda_{\\Phi_u}",
      "description": "EFT cutoff of the dimension-six up-type sextet-scalar / quark / lepton / gluon operator, Eq. (13)"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 6,
      "tex": "\\Lambda_{\\Phi_d}",
      "description": "EFT cutoff of the dimension-six down-type sextet-scalar / quark / lepton / gluon operator, Eq. (13)"
    },
    {
      "name": "kapu",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05"},
        {"lhs": "kapu[2]", "rhs": "0.05"},
        {"lhs": "kapu[3]", "rhs": "0.05"}
      ],
      "block_name": "KAPU",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_u",
      "description": "Coupling of the up-type sextet fermion Psiu to an up-type quark and a gluon, Eq. (12)"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05"},
        {"lhs": "kapd[2]", "rhs": "0.05"},
        {"lhs": "kapd[3]", "rhs": "0.05"}
      ],
      "block_name": "KAPD",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_d",
      "description": "Coupling of the down-type sextet fermion Psid to a down-type quark and a gluon, Eq. (12)"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.1"},
        {"lhs": "kapuB[2]", "rhs": "0.1"},
        {"lhs": "kapuB[3]", "rhs": "0.1"}
      ],
      "block_name": "KAPUB",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{uB}",
      "description": "Coupling of Psiu to an up-type quark, a gluon and a hypercharge boson, Eq. (12)"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.1"},
        {"lhs": "kapdB[2]", "rhs": "0.1"},
        {"lhs": "kapdB[3]", "rhs": "0.1"}
      ],
      "block_name": "KAPDB",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{dB}",
      "description": "Coupling of Psid to a down-type quark, a gluon and a hypercharge boson, Eq. (12)"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamu[1,1]", "rhs": "0.1"},
        {"lhs": "lamu[1,2]", "rhs": "0."},
        {"lhs": "lamu[1,3]", "rhs": "0."},
        {"lhs": "lamu[2,1]", "rhs": "0."},
        {"lhs": "lamu[2,2]", "rhs": "0.1"},
        {"lhs": "lamu[2,3]", "rhs": "0."},
        {"lhs": "lamu[3,1]", "rhs": "0."},
        {"lhs": "lamu[3,2]", "rhs": "0."},
        {"lhs": "lamu[3,3]", "rhs": "0.1"}
      ],
      "block_name": "LAMU",
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_u",
      "description": "Coupling of the up-type sextet scalar Phiu to an up-type quark, a charged lepton and a gluon, Eq. (13). X is the lepton generation, I the quark generation."
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamd[1,1]", "rhs": "0.1"},
        {"lhs": "lamd[1,2]", "rhs": "0."},
        {"lhs": "lamd[1,3]", "rhs": "0."},
        {"lhs": "lamd[2,1]", "rhs": "0."},
        {"lhs": "lamd[2,2]", "rhs": "0.1"},
        {"lhs": "lamd[2,3]", "rhs": "0."},
        {"lhs": "lamd[3,1]", "rhs": "0."},
        {"lhs": "lamd[3,2]", "rhs": "0."},
        {"lhs": "lamd[3,3]", "rhs": "0.1"}
      ],
      "block_name": "LAMD",
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_d",
      "description": "Coupling of the down-type sextet scalar Phid to a down-type quark, a charged lepton and a gluon, Eq. (13). X is the lepton generation, I the quark generation."
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "Phiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhiu", "value": "1000."},
      "width": {"sym": "WPhiu", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "-1"},
      "pdg": 6000001,
      "particle_name": "phiu",
      "antiparticle_name": "phiu~",
      "full_name": "Up-type color-sextet scalar",
      "propagator_label": "Phiu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Phid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhid", "value": "1000."},
      "width": {"sym": "WPhid", "value": "1."},
      "quantum_numbers": {"Q": "4/3", "Y": "4/3", "LeptonNumber": "-1"},
      "pdg": 6000002,
      "particle_name": "phid",
      "antiparticle_name": "phid~",
      "full_name": "Down-type color-sextet scalar",
      "propagator_label": "Phid",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Psiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiu", "value": "1000."},
      "width": {"sym": "WPsiu", "value": "1."},
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3", "LeptonNumber": "0"},
      "pdg": 6000011,
      "particle_name": "psiu",
      "antiparticle_name": "psiu~",
      "full_name": "Up-type color-sextet Dirac fermion",
      "propagator_label": "Psiu",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "Psid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsid", "value": "1000."},
      "width": {"sym": "WPsid", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "0"},
      "pdg": 6000012,
      "particle_name": "psid",
      "antiparticle_name": "psid~",
      "full_name": "Down-type color-sextet Dirac fermion",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "raw_preamble": [
    "(* Color-sextet fields of arXiv:2110.11359 (Table X):                       *)\n(* Phiu ~ (6,1,1/3), Phid ~ (6,1,4/3)   scalars,  L = -1                   *)\n(* Psiu ~ (6,1,-2/3), Psid ~ (6,1,1/3)  Dirac fermions, L = 0              *)\n(* The sextet index carries the 6 of SU(3)c: the SU3C gauge group of SM.fr *)\n(* must list the sextet representation, Representations -> {{T,Colour},    *)\n(* {T6,Sextet}}, so that DC[] builds the correct gluon coupling.           *)"
  ],
  "raw_blocks": [
    "(* sigma^{mu nu} = (I/2) [Ga[mu], Ga[nu]] *)\nSigMN[mu_, nu_] := I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu]);",
    "(* Clebsch-Gordan coefficients J^{s i a} of the 3 x 6 x 8 invariant, Eq. (A18): *)\n(* J^{sia} = -I Sqrt[2] L^{ijk} [T^a]^l_j Kbar^s_{lk}, with Sqrt[2] L^{ijk} = Eps[i,j,k]. *)\n(* Built from the FeynRules objects K6bar (3 x 3 -> 6bar) and T (generators of the 3). *)\nJsix[s_, i_, a_] := Module[{jj, kk, ll}, -I Eps[i, jj, kk] T[a, ll, jj] K6bar[s, ll, kk]];"
  ],
  "lagrangian_terms": [
    {
      "name": "LSextetKin",
      "delayed": true,
      "expression": "Block[{mu, sx}, ExpandIndices[ I*Psiubar[sx].Ga[mu].DC[Psiu[sx], mu] - MPsiu Psiubar[sx].Psiu[sx] + I*Psidbar[sx].Ga[mu].DC[Psid[sx], mu] - MPsid Psidbar[sx].Psid[sx] + DC[Phiubar[sx], mu] DC[Phiu[sx], mu] - MPhiu^2 Phiubar[sx] Phiu[sx] + DC[Phidbar[sx], mu] DC[Phid[sx], mu] - MPhid^2 Phidbar[sx] Phid[sx] ]]"
    },
    {
      "name": "LPsiqG0",
      "delayed": true,
      "expression": "Block[{mu, nu, sx, ii, aa, ff}, ExpandIndices[ (kapu[ff]/LamPsiu) Jsix[sx, ii, aa] (CC[uRbar[ff, ii]].SigMN[mu, nu].Psiu[sx]) FS[G, mu, nu, aa] + (kapd[ff]/LamPsid) Jsix[sx, ii, aa] (CC[dRbar[ff, ii]].SigMN[mu, nu].Psid[sx]) FS[G, mu, nu, aa], FlavorExpand -> {Generation}]]"
    },
    {
      "name": "LPsiqGB0",
      "delayed": true,
      "expression": "Block[{mu, nu, sx, ii, aa, ff}, ExpandIndices[ (kapuB[ff]/LamPsiuB^3) Jsix[sx, ii, aa] (CC[uRbar[ff, ii]].Psiu[sx]) FS[B, mu, nu] FS[G, mu, nu, aa] + (kapdB[ff]/LamPsidB^3) Jsix[sx, ii, aa] (CC[dRbar[ff, ii]].Psid[sx]) FS[B, mu, nu] FS[G, mu, nu, aa], FlavorExpand -> {Generation}]]"
    },
    {
      "name": "LPhiqlG0",
      "delayed": true,
      "expression": "Block[{mu, nu, sx, ii, aa, ff, ffl}, ExpandIndices[ (lamu[ffl, ff]/LamPhiu^2) Jsix[sx, ii, aa] Phiu[sx] (CC[uRbar[ff, ii]].SigMN[mu, nu].lR[ffl]) FS[G, mu, nu, aa] + (lamd[ffl, ff]/LamPhid^2) Jsix[sx, ii, aa] Phid[sx] (CC[dRbar[ff, ii]].SigMN[mu, nu].lR[ffl]) FS[G, mu, nu, aa], FlavorExpand -> {Generation}]]"
    },
    {
      "name": "LSextets",
      "delayed": true,
      "expression": "LSextetKin + LPsiqG0 + HC[LPsiqG0] + LPsiqGB0 + HC[LPsiqGB0] + LPhiqlG0 + HC[LPhiqlG0]"
    }
  ]
}
```
I've read the paper, the schema, the renderer, and SM.fr. The physics content is Table X plus Eqs. (12)–(13): four new colour-sextet states (two scalars, two Dirac fermions), all SU(2) singlets, coupled to a quark and a gluon through the 3⊗6⊗8 invariant.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["Linda M. Carpenter", "Taylor Murphy", "Tim M. P. Tait"],
    "version": "1.0",
    "date": "07. 09. 2022",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 3]],
  "feynman_gauge": null,
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Sextet",
      "range_kind": "NoUnfold",
      "size": 6,
      "style_symbol": "sx"
    }
  ],
  "parameters": [
    {
      "name": "LamPsiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 1,
      "tex": "\\Lambda_{\\Psi_u}",
      "description": "EFT cutoff of the dimension-five up-type sextet-fermion / quark / gluon operator, Eq. (12)"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 2,
      "tex": "\\Lambda_{\\Psi_d}",
      "description": "EFT cutoff of the dimension-five down-type sextet-fermion / quark / gluon operator, Eq. (12)"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 3,
      "tex": "\\Lambda_{\\Psi_u B}",
      "description": "EFT cutoff of the dimension-seven up-type sextet-fermion / quark / gluon / B operator, Eq. (12)"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 4,
      "tex": "\\Lambda_{\\Psi_d B}",
      "description": "EFT cutoff of the dimension-seven down-type sextet-fermion / quark / gluon / B operator, Eq. (12)"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 5,
      "tex": "\\Lambda_{\\Phi_u}",
      "description": "EFT cutoff of the dimension-six up-type sextet-scalar / quark / lepton / gluon operator, Eq. (13)"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SEXTETEFT",
      "order_block": 6,
      "tex": "\\Lambda_{\\Phi_d}",
      "description": "EFT cutoff of the dimension-six down-type sextet-scalar / quark / lepton / gluon operator, Eq. (13)"
    },
    {
      "name": "kapu",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05"},
        {"lhs": "kapu[2]", "rhs": "0.05"},
        {"lhs": "kapu[3]", "rhs": "0.05"}
      ],
      "block_name": "KAPU",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_u",
      "description": "Coupling of the up-type sextet fermion Psiu to an up-type quark and a gluon, Eq. (12)"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05"},
        {"lhs": "kapd[2]", "rhs": "0.05"},
        {"lhs": "kapd[3]", "rhs": "0.05"}
      ],
      "block_name": "KAPD",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_d",
      "description": "Coupling of the down-type sextet fermion Psid to a down-type quark and a gluon, Eq. (12)"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.1"},
        {"lhs": "kapuB[2]", "rhs": "0.1"},
        {"lhs": "kapuB[3]", "rhs": "0.1"}
      ],
      "block_name": "KAPUB",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{uB}",
      "description": "Coupling of Psiu to an up-type quark, a gluon and a hypercharge boson, Eq. (12)"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.1"},
        {"lhs": "kapdB[2]", "rhs": "0.1"},
        {"lhs": "kapdB[3]", "rhs": "0.1"}
      ],
      "block_name": "KAPDB",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{dB}",
      "description": "Coupling of Psid to a down-type quark, a gluon and a hypercharge boson, Eq. (12)"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamu[1,1]", "rhs": "0.1"},
        {"lhs": "lamu[1,2]", "rhs": "0."},
        {"lhs": "lamu[1,3]", "rhs": "0."},
        {"lhs": "lamu[2,1]", "rhs": "0."},
        {"lhs": "lamu[2,2]", "rhs": "0.1"},
        {"lhs": "lamu[2,3]", "rhs": "0."},
        {"lhs": "lamu[3,1]", "rhs": "0."},
        {"lhs": "lamu[3,2]", "rhs": "0."},
        {"lhs": "lamu[3,3]", "rhs": "0.1"}
      ],
      "block_name": "LAMU",
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_u",
      "description": "Coupling of the up-type sextet scalar Phiu to an up-type quark, a charged lepton and a gluon, Eq. (13). X is the lepton generation, I the quark generation."
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamd[1,1]", "rhs": "0.1"},
        {"lhs": "lamd[1,2]", "rhs": "0."},
        {"lhs": "lamd[1,3]", "rhs": "0."},
        {"lhs": "lamd[2,1]", "rhs": "0."},
        {"lhs": "lamd[2,2]", "rhs": "0.1"},
        {"lhs": "lamd[2,3]", "rhs": "0."},
        {"lhs": "lamd[3,1]", "rhs": "0."},
        {"lhs": "lamd[3,2]", "rhs": "0."},
        {"lhs": "lamd[3,3]", "rhs": "0.1"}
      ],
      "block_name": "LAMD",
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_d",
      "description": "Coupling of the down-type sextet scalar Phid to a down-type quark, a charged lepton and a gluon, Eq. (13). X is the lepton generation, I the quark generation."
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "Phiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhiu", "value": "1000."},
      "width": {"sym": "WPhiu", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "-1"},
      "pdg": 6000001,
      "particle_name": "phiu",
      "antiparticle_name": "phiu~",
      "full_name": "Up-type color-sextet scalar",
      "propagator_label": "Phiu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Phid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhid", "value": "1000."},
      "width": {"sym": "WPhid", "value": "1."},
      "quantum_numbers": {"Q": "4/3", "Y": "4/3", "LeptonNumber": "-1"},
      "pdg": 6000002,
      "particle_name": "phid",
      "antiparticle_name": "phid~",
      "full_name": "Down-type color-sextet scalar",
      "propagator_label": "Phid",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Psiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiu", "value": "1000."},
      "width": {"sym": "WPsiu", "value": "1."},
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3", "LeptonNumber": "0"},
      "pdg": 6000011,
      "particle_name": "psiu",
      "antiparticle_name": "psiu~",
      "full_name": "Up-type color-sextet Dirac fermion",
      "propagator_label": "Psiu",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "Psid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsid", "value": "1000."},
      "width": {"sym": "WPsid", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "0"},
      "pdg": 6000012,
      "particle_name": "psid",
      "antiparticle_name": "psid~",
      "full_name": "Down-type color-sextet Dirac fermion",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "raw_preamble": [
    "(* Color-sextet fields of arXiv:2110.11359 (Table X):                       *)\n(* Phiu ~ (6,1,1/3), Phid ~ (6,1,4/3)   scalars,  L = -1                   *)\n(* Psiu ~ (6,1,-2/3), Psid ~ (6,1,1/3)  Dirac fermions, L = 0              *)\n(* The sextet index carries the 6 of SU(3)c: the SU3C gauge group of SM.fr *)\n(* must list the sextet representation, Representations -> {{T,Colour},    *)\n(* {T6,Sextet}}, so that DC[] builds the correct gluon coupling.           *)"
  ],
  "raw_blocks": [
    "(* sigma^{mu nu} = (I/2) [Ga[mu], Ga[nu]] *)\nSigMN[mu_, nu_] := I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu]);",
    "(* Clebsch-Gordan coefficients J^{s i a} of the 3 x 6 x 8 invariant, Eq. (A18): *)\n(* J^{sia} = -I Sqrt[2] L^{ijk} [T^a]^l_j Kbar^s_{lk}, with Sqrt[2] L^{ijk} = Eps[i,j,k]. *)\n(* Built from the FeynRules objects K6bar (3 x 3 -> 6bar) and T (generators of the 3). *)\nJsix[s_, i_, a_] := Module[{jj, kk, ll}, -I Eps[i, jj, kk] T[a, ll, jj] K6bar[s, ll, kk]];"
  ],
  "lagrangian_terms": [
    {
      "name": "LSextetKin",
      "delayed": true,
      "expression": "Block[{mu, sx}, ExpandIndices[ I*Psiubar[sx].Ga[mu].DC[Psiu[sx], mu] - MPsiu Psiubar[sx].Psiu[sx] + I*Psidbar[sx].Ga[mu].DC[Psid[sx], mu] - MPsid Psidbar[sx].Psid[sx] + DC[Phiubar[sx], mu] DC[Phiu[sx], mu] - MPhiu^2 Phiubar[sx] Phiu[sx] + DC[Phidbar[sx], mu] DC[Phid[sx], mu] - MPhid^2 Phidbar[sx] Phid[sx] ]]"
    },
    {
      "name": "LPsiqG0",
      "delayed": true,
      "expression": "Block[{mu, nu, sx, ii, aa, ff}, ExpandIndices[ (kapu[ff]/LamPsiu) Jsix[sx, ii, aa] (CC[uRbar[ff, ii]].SigMN[mu, nu].Psiu[sx]) FS[G, mu, nu, aa] + (kapd[ff]/LamPsid) Jsix[sx, ii, aa] (CC[dRbar[ff, ii]].SigMN[mu, nu].Psid[sx]) FS[G, mu, nu, aa], FlavorExpand -> {Generation}]]"
    },
    {
      "name": "LPsiqGB0",
      "delayed": true,
      "expression": "Block[{mu, nu, sx, ii, aa, ff}, ExpandIndices[ (kapuB[ff]/LamPsiuB^3) Jsix[sx, ii, aa] (CC[uRbar[ff, ii]].Psiu[sx]) FS[B, mu, nu] FS[G, mu, nu, aa] + (kapdB[ff]/LamPsidB^3) Jsix[sx, ii, aa] (CC[dRbar[ff, ii]].Psid[sx]) FS[B, mu, nu] FS[G, mu, nu, aa], FlavorExpand -> {Generation}]]"
    },
    {
      "name": "LPhiqlG0",
      "delayed": true,
      "expression": "Block[{mu, nu, sx, ii, aa, ff, ffl}, ExpandIndices[ (lamu[ffl, ff]/LamPhiu^2) Jsix[sx, ii, aa] Phiu[sx] (CC[uRbar[ff, ii]].SigMN[mu, nu].lR[ffl]) FS[G, mu, nu, aa] + (lamd[ffl, ff]/LamPhid^2) Jsix[sx, ii, aa] Phid[sx] (CC[dRbar[ff, ii]].SigMN[mu, nu].lR[ffl]) FS[G, mu, nu, aa], FlavorExpand -> {Generation}]]"
    },
    {
      "name": "LSextets",
      "delayed": true,
      "expression": "LSextetKin + LPsiqG0 + HC[LPsiqG0] + LPsiqGB0 + HC[LPsiqGB0] + LPhiqlG0 + HC[LPhiqlG0]"
    }
  ]
}
```