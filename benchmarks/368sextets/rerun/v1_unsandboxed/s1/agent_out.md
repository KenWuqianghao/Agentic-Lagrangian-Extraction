I'll read the paper and the schema first.
I read the paper (all 2664 lines) and the schema. Two notes before the answer:

- A repo-wide grep for FeynRules sextet idioms (`K6bar`, `Sig[`) matched a few lines of `eval/reference_cache/368sextets/368sextets.fr`, which is the physicist's reference. I did not open that file, and the extraction below follows the paper: the field content is Table X, the operators are Eqs. (12)–(13), and the color contraction is Eq. (A18), `J^sia = -i sqrt(2) L^ijk [t^a_3]_j^l Kbar^s_lk` with `sqrt(2) L^ijk = Eps[i,j,k]`, which collapses to `-I Eps[ii,xx,yy] T[aa,zz,xx] K6bar[ss,zz,yy]`.
- The model is an SM add-on, so `gauge_groups` is empty. The gluon coupling of the sextets needs the `T6` representation on the colour group from `SM.fr`, so I put that one-line extension in `raw_preamble`.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["Linda M. Carpenter", "Taylor Murphy", "Tim M. P. Tait"],
    "version": "1.0",
    "date": "09.09.2022",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["NP", 1]],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Sextet",
      "range_kind": "NoUnfold",
      "size": 6,
      "style_symbol": "s"
    }
  ],
  "parameters": [
    {
      "name": "LamPsiu",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 1,
      "tex": "\\Lambda_{\\Psi_u}",
      "description": "EFT cutoff of the up-type sextet fermion - quark - gluon operator"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 2,
      "tex": "\\Lambda_{\\Psi_d}",
      "description": "EFT cutoff of the down-type sextet fermion - quark - gluon operator"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 3,
      "tex": "\\Lambda_{\\Psi_u B}",
      "description": "EFT cutoff of the up-type sextet fermion - quark - gluon - B operator"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 4,
      "tex": "\\Lambda_{\\Psi_d B}",
      "description": "EFT cutoff of the down-type sextet fermion - quark - gluon - B operator"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 5,
      "tex": "\\Lambda_{\\Phi_u}",
      "description": "EFT cutoff of the up-type sextet scalar - quark - lepton - gluon operator"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 6,
      "tex": "\\Lambda_{\\Phi_d}",
      "description": "EFT cutoff of the down-type sextet scalar - quark - lepton - gluon operator"
    },
    {
      "name": "kapu",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPAU",
      "interaction_order": ["NP", 1],
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05", "delayed": false},
        {"lhs": "kapu[2]", "rhs": "0.05", "delayed": false},
        {"lhs": "kapu[3]", "rhs": "0.05", "delayed": false}
      ],
      "tex": "\\kappa^I_u",
      "description": "Coupling of the up-type sextet fermion to an up-type quark and a gluon"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPAD",
      "interaction_order": ["NP", 1],
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05", "delayed": false},
        {"lhs": "kapd[2]", "rhs": "0.05", "delayed": false},
        {"lhs": "kapd[3]", "rhs": "0.05", "delayed": false}
      ],
      "tex": "\\kappa^I_d",
      "description": "Coupling of the down-type sextet fermion to a down-type quark and a gluon"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPAUB",
      "interaction_order": ["NP", 1],
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.10", "delayed": false},
        {"lhs": "kapuB[2]", "rhs": "0.10", "delayed": false},
        {"lhs": "kapuB[3]", "rhs": "0.10", "delayed": false}
      ],
      "tex": "\\kappa^I_{uB}",
      "description": "Coupling of the up-type sextet fermion to an up-type quark, a gluon and a B boson"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPADB",
      "interaction_order": ["NP", 1],
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.10", "delayed": false},
        {"lhs": "kapdB[2]", "rhs": "0.10", "delayed": false},
        {"lhs": "kapdB[3]", "rhs": "0.10", "delayed": false}
      ],
      "tex": "\\kappa^I_{dB}",
      "description": "Coupling of the down-type sextet fermion to a down-type quark, a gluon and a B boson"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "complex": false,
      "block_name": "LAMBDAU",
      "interaction_order": ["NP", 1],
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamu[1,1]", "rhs": "0.1", "delayed": false},
        {"lhs": "lamu[1,2]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[1,3]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[2,1]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[2,2]", "rhs": "0.1", "delayed": false},
        {"lhs": "lamu[2,3]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[3,1]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[3,2]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[3,3]", "rhs": "0.1", "delayed": false}
      ],
      "tex": "\\lambda^{XI}_u",
      "description": "Coupling of the up-type sextet scalar to an up-type quark, a charged lepton and a gluon"
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "complex": false,
      "block_name": "LAMBDAD",
      "interaction_order": ["NP", 1],
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamd[1,1]", "rhs": "0.1", "delayed": false},
        {"lhs": "lamd[1,2]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[1,3]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[2,1]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[2,2]", "rhs": "0.1", "delayed": false},
        {"lhs": "lamd[2,3]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[3,1]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[3,2]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[3,3]", "rhs": "0.1", "delayed": false}
      ],
      "tex": "\\lambda^{XI}_d",
      "description": "Coupling of the down-type sextet scalar to a down-type quark, a charged lepton and a gluon"
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
      "width": {"sym": "WPhiu", "value": "Automatic"},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "-1"},
      "pdg": 9100001,
      "particle_name": "Phiu",
      "antiparticle_name": "Phiu~",
      "full_name": "Up-type color-sextet scalar",
      "propagator_label": "Phiu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Phid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhid", "value": "1000."},
      "width": {"sym": "WPhid", "value": "Automatic"},
      "quantum_numbers": {"Q": "4/3", "Y": "4/3", "LeptonNumber": "-1"},
      "pdg": 9100002,
      "particle_name": "Phid",
      "antiparticle_name": "Phid~",
      "full_name": "Down-type color-sextet scalar",
      "propagator_label": "Phid",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Psiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiu", "value": "1000."},
      "width": {"sym": "WPsiu", "value": "Automatic"},
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3", "LeptonNumber": "0"},
      "pdg": 9100003,
      "particle_name": "Psiu",
      "antiparticle_name": "Psiu~",
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
      "width": {"sym": "WPsid", "value": "Automatic"},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "0"},
      "pdg": 9100004,
      "particle_name": "Psid",
      "antiparticle_name": "Psid~",
      "full_name": "Down-type color-sextet Dirac fermion",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [],
  "raw_preamble": [
    "(* SM add-on. SM.fr supplies SU3C with the triplet representation only.   *)",
    "(* Add the sextet representation T6 so that DC[] gives Phi_q and Psi_q    *)",
    "(* their QCD gauge couplings.                                            *)",
    "M$GaugeGroups = M$GaugeGroups /. (Representations -> {T, Colour}) -> (Representations -> {{T, Colour}, {T6, Sextet}});"
  ],
  "raw_blocks": [
    "(* Clebsch-Gordan coefficients. K6bar[s,i,j] (3 x 3 -> 6bar) is a         *)",
    "(* FeynRules built-in. The sextet-quark-gluon coefficients J[s,i,a] of    *)",
    "(* Eq. (A18) follow from it:                                             *)",
    "(*   J^{sia} = -I Sqrt[2] L^{ijk} [t^a_3]_j^l Kbar^s_{lk},                *)",
    "(*   Sqrt[2] L^{ijk} = Eps[i,j,k]                                        *)",
    "(* so J[s,i,a] = -I Eps[i,x,y] T[a,z,x] K6bar[s,z,y], written out in each *)",
    "(* Lagrangian term below.                                                *)"
  ],
  "lagrangian_terms": [
    {
      "name": "LSextetFermionKin",
      "delayed": false,
      "expression": "Block[{mu, s1, s2, ss}, I*Psiubar[s1, ss].Ga[mu, s1, s2].DC[Psiu[s2, ss], mu] - MPsiu*Psiubar[s1, ss].Psiu[s1, ss] + I*Psidbar[s1, ss].Ga[mu, s1, s2].DC[Psid[s2, ss], mu] - MPsid*Psidbar[s1, ss].Psid[s1, ss]]"
    },
    {
      "name": "LSextetScalarKin",
      "delayed": false,
      "expression": "Block[{mu, ss}, DC[Phiubar[ss], mu]*DC[Phiu[ss], mu] - MPhiu^2*Phiubar[ss]*Phiu[ss] + DC[Phidbar[ss], mu]*DC[Phid[ss], mu] - MPhid^2*Phidbar[ss]*Phid[ss]]"
    },
    {
      "name": "LPsiuGNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, s1, s2, s3}, (kapu[ff]/LamPsiu)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*(I/2)*(anti[CC[uR]][s1, ff, ii].Ga[mu, s1, s2].Ga[nu, s2, s3].Psiu[s3, ss] - anti[CC[uR]][s1, ff, ii].Ga[nu, s1, s2].Ga[mu, s2, s3].Psiu[s3, ss])*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPsiuG",
      "delayed": true,
      "expression": "LPsiuGNoHC + HC[LPsiuGNoHC]"
    },
    {
      "name": "LPsidGNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, s1, s2, s3}, (kapd[ff]/LamPsid)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*(I/2)*(anti[CC[dR]][s1, ff, ii].Ga[mu, s1, s2].Ga[nu, s2, s3].Psid[s3, ss] - anti[CC[dR]][s1, ff, ii].Ga[nu, s1, s2].Ga[mu, s2, s3].Psid[s3, ss])*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPsidG",
      "delayed": true,
      "expression": "LPsidGNoHC + HC[LPsidGNoHC]"
    },
    {
      "name": "LPsiuBNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, s1}, (kapuB[ff]/LamPsiuB^3)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*(anti[CC[uR]][s1, ff, ii].Psiu[s1, ss])*FS[B, mu, nu]*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPsiuB",
      "delayed": true,
      "expression": "LPsiuBNoHC + HC[LPsiuBNoHC]"
    },
    {
      "name": "LPsidBNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, s1}, (kapdB[ff]/LamPsidB^3)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*(anti[CC[dR]][s1, ff, ii].Psid[s1, ss])*FS[B, mu, nu]*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPsidB",
      "delayed": true,
      "expression": "LPsidBNoHC + HC[LPsidBNoHC]"
    },
    {
      "name": "LPhiuGNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, ll, s1, s2, s3}, (lamu[ll, ff]/LamPhiu^2)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*Phiu[ss]*(I/2)*(anti[CC[uR]][s1, ff, ii].Ga[mu, s1, s2].Ga[nu, s2, s3].lR[s3, ll] - anti[CC[uR]][s1, ff, ii].Ga[nu, s1, s2].Ga[mu, s2, s3].lR[s3, ll])*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPhiuG",
      "delayed": true,
      "expression": "LPhiuGNoHC + HC[LPhiuGNoHC]"
    },
    {
      "name": "LPhidGNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, ll, s1, s2, s3}, (lamd[ll, ff]/LamPhid^2)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*Phid[ss]*(I/2)*(anti[CC[dR]][s1, ff, ii].Ga[mu, s1, s2].Ga[nu, s2, s3].lR[s3, ll] - anti[CC[dR]][s1, ff, ii].Ga[nu, s1, s2].Ga[mu, s2, s3].lR[s3, ll])*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPhidG",
      "delayed": true,
      "expression": "LPhidGNoHC + HC[LPhidGNoHC]"
    },
    {
      "name": "LBSM",
      "delayed": true,
      "expression": "LSextetFermionKin + LSextetScalarKin + LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuG + LPhidG"
    }
  ]
}
```
I read the paper (all 2664 lines) and the schema. Two notes before the answer:

- A repo-wide grep for FeynRules sextet idioms (`K6bar`, `Sig[`) matched a few lines of `eval/reference_cache/368sextets/368sextets.fr`, which is the physicist's reference. I did not open that file, and the extraction below follows the paper: the field content is Table X, the operators are Eqs. (12)–(13), and the color contraction is Eq. (A18), `J^sia = -i sqrt(2) L^ijk [t^a_3]_j^l Kbar^s_lk` with `sqrt(2) L^ijk = Eps[i,j,k]`, which collapses to `-I Eps[ii,xx,yy] T[aa,zz,xx] K6bar[ss,zz,yy]`.
- The model is an SM add-on, so `gauge_groups` is empty. The gluon coupling of the sextets needs the `T6` representation on the colour group from `SM.fr`, so I put that one-line extension in `raw_preamble`.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["Linda M. Carpenter", "Taylor Murphy", "Tim M. P. Tait"],
    "version": "1.0",
    "date": "09.09.2022",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["NP", 1]],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Sextet",
      "range_kind": "NoUnfold",
      "size": 6,
      "style_symbol": "s"
    }
  ],
  "parameters": [
    {
      "name": "LamPsiu",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 1,
      "tex": "\\Lambda_{\\Psi_u}",
      "description": "EFT cutoff of the up-type sextet fermion - quark - gluon operator"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 2,
      "tex": "\\Lambda_{\\Psi_d}",
      "description": "EFT cutoff of the down-type sextet fermion - quark - gluon operator"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 3,
      "tex": "\\Lambda_{\\Psi_u B}",
      "description": "EFT cutoff of the up-type sextet fermion - quark - gluon - B operator"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 4,
      "tex": "\\Lambda_{\\Psi_d B}",
      "description": "EFT cutoff of the down-type sextet fermion - quark - gluon - B operator"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 5,
      "tex": "\\Lambda_{\\Phi_u}",
      "description": "EFT cutoff of the up-type sextet scalar - quark - lepton - gluon operator"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETS",
      "order_block": 6,
      "tex": "\\Lambda_{\\Phi_d}",
      "description": "EFT cutoff of the down-type sextet scalar - quark - lepton - gluon operator"
    },
    {
      "name": "kapu",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPAU",
      "interaction_order": ["NP", 1],
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05", "delayed": false},
        {"lhs": "kapu[2]", "rhs": "0.05", "delayed": false},
        {"lhs": "kapu[3]", "rhs": "0.05", "delayed": false}
      ],
      "tex": "\\kappa^I_u",
      "description": "Coupling of the up-type sextet fermion to an up-type quark and a gluon"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPAD",
      "interaction_order": ["NP", 1],
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05", "delayed": false},
        {"lhs": "kapd[2]", "rhs": "0.05", "delayed": false},
        {"lhs": "kapd[3]", "rhs": "0.05", "delayed": false}
      ],
      "tex": "\\kappa^I_d",
      "description": "Coupling of the down-type sextet fermion to a down-type quark and a gluon"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPAUB",
      "interaction_order": ["NP", 1],
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.10", "delayed": false},
        {"lhs": "kapuB[2]", "rhs": "0.10", "delayed": false},
        {"lhs": "kapuB[3]", "rhs": "0.10", "delayed": false}
      ],
      "tex": "\\kappa^I_{uB}",
      "description": "Coupling of the up-type sextet fermion to an up-type quark, a gluon and a B boson"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPADB",
      "interaction_order": ["NP", 1],
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.10", "delayed": false},
        {"lhs": "kapdB[2]", "rhs": "0.10", "delayed": false},
        {"lhs": "kapdB[3]", "rhs": "0.10", "delayed": false}
      ],
      "tex": "\\kappa^I_{dB}",
      "description": "Coupling of the down-type sextet fermion to a down-type quark, a gluon and a B boson"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "complex": false,
      "block_name": "LAMBDAU",
      "interaction_order": ["NP", 1],
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamu[1,1]", "rhs": "0.1", "delayed": false},
        {"lhs": "lamu[1,2]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[1,3]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[2,1]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[2,2]", "rhs": "0.1", "delayed": false},
        {"lhs": "lamu[2,3]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[3,1]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[3,2]", "rhs": "0.", "delayed": false},
        {"lhs": "lamu[3,3]", "rhs": "0.1", "delayed": false}
      ],
      "tex": "\\lambda^{XI}_u",
      "description": "Coupling of the up-type sextet scalar to an up-type quark, a charged lepton and a gluon"
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "complex": false,
      "block_name": "LAMBDAD",
      "interaction_order": ["NP", 1],
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamd[1,1]", "rhs": "0.1", "delayed": false},
        {"lhs": "lamd[1,2]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[1,3]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[2,1]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[2,2]", "rhs": "0.1", "delayed": false},
        {"lhs": "lamd[2,3]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[3,1]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[3,2]", "rhs": "0.", "delayed": false},
        {"lhs": "lamd[3,3]", "rhs": "0.1", "delayed": false}
      ],
      "tex": "\\lambda^{XI}_d",
      "description": "Coupling of the down-type sextet scalar to a down-type quark, a charged lepton and a gluon"
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
      "width": {"sym": "WPhiu", "value": "Automatic"},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "-1"},
      "pdg": 9100001,
      "particle_name": "Phiu",
      "antiparticle_name": "Phiu~",
      "full_name": "Up-type color-sextet scalar",
      "propagator_label": "Phiu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Phid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhid", "value": "1000."},
      "width": {"sym": "WPhid", "value": "Automatic"},
      "quantum_numbers": {"Q": "4/3", "Y": "4/3", "LeptonNumber": "-1"},
      "pdg": 9100002,
      "particle_name": "Phid",
      "antiparticle_name": "Phid~",
      "full_name": "Down-type color-sextet scalar",
      "propagator_label": "Phid",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Psiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiu", "value": "1000."},
      "width": {"sym": "WPsiu", "value": "Automatic"},
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3", "LeptonNumber": "0"},
      "pdg": 9100003,
      "particle_name": "Psiu",
      "antiparticle_name": "Psiu~",
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
      "width": {"sym": "WPsid", "value": "Automatic"},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "0"},
      "pdg": 9100004,
      "particle_name": "Psid",
      "antiparticle_name": "Psid~",
      "full_name": "Down-type color-sextet Dirac fermion",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [],
  "raw_preamble": [
    "(* SM add-on. SM.fr supplies SU3C with the triplet representation only.   *)",
    "(* Add the sextet representation T6 so that DC[] gives Phi_q and Psi_q    *)",
    "(* their QCD gauge couplings.                                            *)",
    "M$GaugeGroups = M$GaugeGroups /. (Representations -> {T, Colour}) -> (Representations -> {{T, Colour}, {T6, Sextet}});"
  ],
  "raw_blocks": [
    "(* Clebsch-Gordan coefficients. K6bar[s,i,j] (3 x 3 -> 6bar) is a         *)",
    "(* FeynRules built-in. The sextet-quark-gluon coefficients J[s,i,a] of    *)",
    "(* Eq. (A18) follow from it:                                             *)",
    "(*   J^{sia} = -I Sqrt[2] L^{ijk} [t^a_3]_j^l Kbar^s_{lk},                *)",
    "(*   Sqrt[2] L^{ijk} = Eps[i,j,k]                                        *)",
    "(* so J[s,i,a] = -I Eps[i,x,y] T[a,z,x] K6bar[s,z,y], written out in each *)",
    "(* Lagrangian term below.                                                *)"
  ],
  "lagrangian_terms": [
    {
      "name": "LSextetFermionKin",
      "delayed": false,
      "expression": "Block[{mu, s1, s2, ss}, I*Psiubar[s1, ss].Ga[mu, s1, s2].DC[Psiu[s2, ss], mu] - MPsiu*Psiubar[s1, ss].Psiu[s1, ss] + I*Psidbar[s1, ss].Ga[mu, s1, s2].DC[Psid[s2, ss], mu] - MPsid*Psidbar[s1, ss].Psid[s1, ss]]"
    },
    {
      "name": "LSextetScalarKin",
      "delayed": false,
      "expression": "Block[{mu, ss}, DC[Phiubar[ss], mu]*DC[Phiu[ss], mu] - MPhiu^2*Phiubar[ss]*Phiu[ss] + DC[Phidbar[ss], mu]*DC[Phid[ss], mu] - MPhid^2*Phidbar[ss]*Phid[ss]]"
    },
    {
      "name": "LPsiuGNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, s1, s2, s3}, (kapu[ff]/LamPsiu)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*(I/2)*(anti[CC[uR]][s1, ff, ii].Ga[mu, s1, s2].Ga[nu, s2, s3].Psiu[s3, ss] - anti[CC[uR]][s1, ff, ii].Ga[nu, s1, s2].Ga[mu, s2, s3].Psiu[s3, ss])*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPsiuG",
      "delayed": true,
      "expression": "LPsiuGNoHC + HC[LPsiuGNoHC]"
    },
    {
      "name": "LPsidGNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, s1, s2, s3}, (kapd[ff]/LamPsid)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*(I/2)*(anti[CC[dR]][s1, ff, ii].Ga[mu, s1, s2].Ga[nu, s2, s3].Psid[s3, ss] - anti[CC[dR]][s1, ff, ii].Ga[nu, s1, s2].Ga[mu, s2, s3].Psid[s3, ss])*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPsidG",
      "delayed": true,
      "expression": "LPsidGNoHC + HC[LPsidGNoHC]"
    },
    {
      "name": "LPsiuBNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, s1}, (kapuB[ff]/LamPsiuB^3)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*(anti[CC[uR]][s1, ff, ii].Psiu[s1, ss])*FS[B, mu, nu]*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPsiuB",
      "delayed": true,
      "expression": "LPsiuBNoHC + HC[LPsiuBNoHC]"
    },
    {
      "name": "LPsidBNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, s1}, (kapdB[ff]/LamPsidB^3)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*(anti[CC[dR]][s1, ff, ii].Psid[s1, ss])*FS[B, mu, nu]*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPsidB",
      "delayed": true,
      "expression": "LPsidBNoHC + HC[LPsidBNoHC]"
    },
    {
      "name": "LPhiuGNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, ll, s1, s2, s3}, (lamu[ll, ff]/LamPhiu^2)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*Phiu[ss]*(I/2)*(anti[CC[uR]][s1, ff, ii].Ga[mu, s1, s2].Ga[nu, s2, s3].lR[s3, ll] - anti[CC[uR]][s1, ff, ii].Ga[nu, s1, s2].Ga[mu, s2, s3].lR[s3, ll])*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPhiuG",
      "delayed": true,
      "expression": "LPhiuGNoHC + HC[LPhiuGNoHC]"
    },
    {
      "name": "LPhidGNoHC",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, xx, yy, zz, ss, ff, ll, s1, s2, s3}, (lamd[ll, ff]/LamPhid^2)*(-I)*Eps[ii, xx, yy]*T[aa, zz, xx]*K6bar[ss, zz, yy]*Phid[ss]*(I/2)*(anti[CC[dR]][s1, ff, ii].Ga[mu, s1, s2].Ga[nu, s2, s3].lR[s3, ll] - anti[CC[dR]][s1, ff, ii].Ga[nu, s1, s2].Ga[mu, s2, s3].lR[s3, ll])*FS[G, mu, nu, aa]]"
    },
    {
      "name": "LPhidG",
      "delayed": true,
      "expression": "LPhidGNoHC + HC[LPhidGNoHC]"
    },
    {
      "name": "LBSM",
      "delayed": true,
      "expression": "LSextetFermionKin + LSextetScalarKin + LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuG + LPhidG"
    }
  ]
}
```