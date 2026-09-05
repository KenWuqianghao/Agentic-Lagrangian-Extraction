I'll start by reading the paper and the schema.
I read the paper and the schema. One disclosure first (below the JSON).

**Model content extracted** (Table X + Eqs. 12–13 of arXiv:2110.11359): four new states — two colour-sextet complex scalars Φu (6,1,1/3), Φd (6,1,4/3) with L = −1, and two colour-sextet Dirac fermions Ψu (6,1,−2/3), Ψd (6,1,1/3) with L = 0. New index `Sextet` (range 6). The Clebsch–Gordan tensor J^{sia} is built from Eq. (A18), J^{sia} = −i ε^{ijk} [t^a]^l_j K̄^s_{lk}, using the FeynRules objects `Eps`, `T` and `K6bar`.

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
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 1,
      "tex": "\\Lambda_{\\Psi_u}",
      "description": "EFT cutoff scale of the sextet-fermion-up-quark-gluon operator"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 2,
      "tex": "\\Lambda_{\\Psi_d}",
      "description": "EFT cutoff scale of the sextet-fermion-down-quark-gluon operator"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 3,
      "tex": "\\Lambda_{\\Psi_u B}",
      "description": "EFT cutoff scale of the sextet-fermion-up-quark-gluon-B operator"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 4,
      "tex": "\\Lambda_{\\Psi_d B}",
      "description": "EFT cutoff scale of the sextet-fermion-down-quark-gluon-B operator"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 5,
      "tex": "\\Lambda_{\\Phi_u}",
      "description": "EFT cutoff scale of the sextet-scalar-up-quark-lepton-gluon operator"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 6,
      "tex": "\\Lambda_{\\Phi_d}",
      "description": "EFT cutoff scale of the sextet-scalar-down-quark-lepton-gluon operator"
    },
    {
      "name": "kappau",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kappau[1]", "rhs": "0.05"},
        {"lhs": "kappau[2]", "rhs": "0.05"},
        {"lhs": "kappau[3]", "rhs": "0.05"}
      ],
      "complex": false,
      "block_name": "KAPPAU",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_u",
      "description": "Coupling of the sextet fermion Psiu to an up-type quark and a gluon"
    },
    {
      "name": "kappad",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kappad[1]", "rhs": "0.05"},
        {"lhs": "kappad[2]", "rhs": "0.05"},
        {"lhs": "kappad[3]", "rhs": "0.05"}
      ],
      "complex": false,
      "block_name": "KAPPAD",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_d",
      "description": "Coupling of the sextet fermion Psid to a down-type quark and a gluon"
    },
    {
      "name": "kappauB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kappauB[1]", "rhs": "0.10"},
        {"lhs": "kappauB[2]", "rhs": "0.10"},
        {"lhs": "kappauB[3]", "rhs": "0.10"}
      ],
      "complex": false,
      "block_name": "KAPPAUB",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{uB}",
      "description": "Coupling of Psiu to an up-type quark, a gluon and a hypercharge boson"
    },
    {
      "name": "kappadB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kappadB[1]", "rhs": "0.10"},
        {"lhs": "kappadB[2]", "rhs": "0.10"},
        {"lhs": "kappadB[3]", "rhs": "0.10"}
      ],
      "complex": false,
      "block_name": "KAPPADB",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{dB}",
      "description": "Coupling of Psid to a down-type quark, a gluon and a hypercharge boson"
    },
    {
      "name": "lambdau",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lambdau[1,1]", "rhs": "0.1"},
        {"lhs": "lambdau[2,2]", "rhs": "0.1"},
        {"lhs": "lambdau[3,3]", "rhs": "0.1"},
        {"lhs": "lambdau[i_, j_]", "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)", "delayed": true}
      ],
      "complex": false,
      "block_name": "LAMBDAU",
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_u",
      "description": "Coupling of the sextet scalar Phiu to an up-type quark, a lepton and a gluon"
    },
    {
      "name": "lambdad",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lambdad[1,1]", "rhs": "0.1"},
        {"lhs": "lambdad[2,2]", "rhs": "0.1"},
        {"lhs": "lambdad[3,3]", "rhs": "0.1"},
        {"lhs": "lambdad[i_, j_]", "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)", "delayed": true}
      ],
      "complex": false,
      "block_name": "LAMBDAD",
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_d",
      "description": "Coupling of the sextet scalar Phid to a down-type quark, a lepton and a gluon"
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
      "particle_name": "Phiu",
      "antiparticle_name": "Phiu~",
      "full_name": "Colour-sextet scalar coupling to up-type quarks",
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
      "particle_name": "Phid",
      "antiparticle_name": "Phid~",
      "full_name": "Colour-sextet scalar coupling to down-type quarks",
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
      "pdg": 6000003,
      "particle_name": "Psiu",
      "antiparticle_name": "Psiu~",
      "full_name": "Colour-sextet Dirac fermion coupling to up-type quarks",
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
      "pdg": 6000004,
      "particle_name": "Psid",
      "antiparticle_name": "Psid~",
      "full_name": "Colour-sextet Dirac fermion coupling to down-type quarks",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "raw_preamble": [
    "(* Colour-sextet fields of arXiv:2110.11359 (Carpenter, Murphy, Tait).      *)\n(* Field content (Table X):                                                 *)\n(*   Phiu ~ (6, 1,  1/3), L = -1    Phid ~ (6, 1,  4/3), L = -1             *)\n(*   Psiu ~ (6, 1, -2/3), L =  0    Psid ~ (6, 1,  1/3), L =  0             *)\n(* The Clebsch-Gordan coefficients J^{sia} of the 3 x 6 x 8 invariant are    *)\n(* built from Eq. (A18): J^{sia} = -I Eps[i,j,k] T[a,l,j] K6bar[s,l,k].      *)"
  ],
  "raw_blocks": [
    "AddGaugeRepresentation[SU3C -> {T6, Sextet}];"
  ],
  "lagrangian_terms": [
    {
      "name": "LSextetFermionKin",
      "expression": "Block[{mu}, ExpandIndices[I Psiubar.Ga[mu].DC[Psiu, mu] - MPsiu Psiubar.Psiu + I Psidbar.Ga[mu].DC[Psid, mu] - MPsid Psidbar.Psid]]",
      "delayed": true
    },
    {
      "name": "LSextetScalarKin",
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phiubar[ss], mu] DC[Phiu[ss], mu] - MPhiu^2 Phiubar[ss] Phiu[ss] + DC[Phidbar[ss], mu] DC[Phid[ss], mu] - MPhid^2 Phidbar[ss] Phid[ss]]]",
      "delayed": true
    },
    {
      "name": "LPsiqGnonHC",
      "expression": "Block[{mu, nu, sp1, sp2, ff, ii, jj, kk, ll, ss, aa}, ExpandIndices[-I/LamPsiu kappau[ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] anti[CC[uR]][sp1, ff, ii].Sig[mu, nu, sp1, sp2].Psiu[sp2, ss] FS[G, mu, nu, aa] - I/LamPsid kappad[ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] anti[CC[dR]][sp1, ff, ii].Sig[mu, nu, sp1, sp2].Psid[sp2, ss] FS[G, mu, nu, aa]]]",
      "delayed": true
    },
    {
      "name": "LPsiqG",
      "expression": "LPsiqGnonHC + HC[LPsiqGnonHC]",
      "delayed": true
    },
    {
      "name": "LPsiqBGnonHC",
      "expression": "Block[{mu, nu, sp, ff, ii, jj, kk, ll, ss, aa}, ExpandIndices[-I/LamPsiuB^3 kappauB[ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] anti[CC[uR]][sp, ff, ii].Psiu[sp, ss] FS[B, mu, nu] FS[G, mu, nu, aa] - I/LamPsidB^3 kappadB[ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] anti[CC[dR]][sp, ff, ii].Psid[sp, ss] FS[B, mu, nu] FS[G, mu, nu, aa]]]",
      "delayed": true
    },
    {
      "name": "LPsiqBG",
      "expression": "LPsiqBGnonHC + HC[LPsiqBGnonHC]",
      "delayed": true
    },
    {
      "name": "LPhiqlGnonHC",
      "expression": "Block[{mu, nu, sp1, sp2, ff, xx, ii, jj, kk, ll, ss, aa}, ExpandIndices[-I/LamPhiu^2 lambdau[xx, ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] Phiu[ss] anti[CC[uR]][sp1, ff, ii].Sig[mu, nu, sp1, sp2].lR[sp2, xx] FS[G, mu, nu, aa] - I/LamPhid^2 lambdad[xx, ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] Phid[ss] anti[CC[dR]][sp1, ff, ii].Sig[mu, nu, sp1, sp2].lR[sp2, xx] FS[G, mu, nu, aa]]]",
      "delayed": true
    },
    {
      "name": "LPhiqlG",
      "expression": "LPhiqlGnonHC + HC[LPhiqlGnonHC]",
      "delayed": true
    },
    {
      "name": "LSextet",
      "expression": "LSextetFermionKin + LSextetScalarKin + LPsiqG + LPsiqBG + LPhiqlG",
      "delayed": true
    }
  ]
}
```

**Benchmark-integrity warning.** While searching for the FeynRules idiom for `FS[B,mu,nu]`, my repository-wide grep matched `eval/reference_cache/368sextets/368sextets.fr` — the physicist's reference file — and printed about eight lines of its Lagrangian block. I had already derived the field content, the quantum numbers, the parameters, and the J^{sia} construction from the paper before that grep, and I did not copy the reference naming or expressions. But the leak happened, so treat this run's Lagrangian score as contaminated. Restrict the search paths (or exclude `eval/reference_cache/<model>/`) for a clean re-run.
I read the paper and the schema. One disclosure first (below the JSON).

**Model content extracted** (Table X + Eqs. 12–13 of arXiv:2110.11359): four new states — two colour-sextet complex scalars Φu (6,1,1/3), Φd (6,1,4/3) with L = −1, and two colour-sextet Dirac fermions Ψu (6,1,−2/3), Ψd (6,1,1/3) with L = 0. New index `Sextet` (range 6). The Clebsch–Gordan tensor J^{sia} is built from Eq. (A18), J^{sia} = −i ε^{ijk} [t^a]^l_j K̄^s_{lk}, using the FeynRules objects `Eps`, `T` and `K6bar`.

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
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 1,
      "tex": "\\Lambda_{\\Psi_u}",
      "description": "EFT cutoff scale of the sextet-fermion-up-quark-gluon operator"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 2,
      "tex": "\\Lambda_{\\Psi_d}",
      "description": "EFT cutoff scale of the sextet-fermion-down-quark-gluon operator"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 3,
      "tex": "\\Lambda_{\\Psi_u B}",
      "description": "EFT cutoff scale of the sextet-fermion-up-quark-gluon-B operator"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 4,
      "tex": "\\Lambda_{\\Psi_d B}",
      "description": "EFT cutoff scale of the sextet-fermion-down-quark-gluon-B operator"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 5,
      "tex": "\\Lambda_{\\Phi_u}",
      "description": "EFT cutoff scale of the sextet-scalar-up-quark-lepton-gluon operator"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "value": "1000.",
      "complex": false,
      "block_name": "SEXTETCUTOFF",
      "order_block": 6,
      "tex": "\\Lambda_{\\Phi_d}",
      "description": "EFT cutoff scale of the sextet-scalar-down-quark-lepton-gluon operator"
    },
    {
      "name": "kappau",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kappau[1]", "rhs": "0.05"},
        {"lhs": "kappau[2]", "rhs": "0.05"},
        {"lhs": "kappau[3]", "rhs": "0.05"}
      ],
      "complex": false,
      "block_name": "KAPPAU",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_u",
      "description": "Coupling of the sextet fermion Psiu to an up-type quark and a gluon"
    },
    {
      "name": "kappad",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kappad[1]", "rhs": "0.05"},
        {"lhs": "kappad[2]", "rhs": "0.05"},
        {"lhs": "kappad[3]", "rhs": "0.05"}
      ],
      "complex": false,
      "block_name": "KAPPAD",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_d",
      "description": "Coupling of the sextet fermion Psid to a down-type quark and a gluon"
    },
    {
      "name": "kappauB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kappauB[1]", "rhs": "0.10"},
        {"lhs": "kappauB[2]", "rhs": "0.10"},
        {"lhs": "kappauB[3]", "rhs": "0.10"}
      ],
      "complex": false,
      "block_name": "KAPPAUB",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{uB}",
      "description": "Coupling of Psiu to an up-type quark, a gluon and a hypercharge boson"
    },
    {
      "name": "kappadB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kappadB[1]", "rhs": "0.10"},
        {"lhs": "kappadB[2]", "rhs": "0.10"},
        {"lhs": "kappadB[3]", "rhs": "0.10"}
      ],
      "complex": false,
      "block_name": "KAPPADB",
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{dB}",
      "description": "Coupling of Psid to a down-type quark, a gluon and a hypercharge boson"
    },
    {
      "name": "lambdau",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lambdau[1,1]", "rhs": "0.1"},
        {"lhs": "lambdau[2,2]", "rhs": "0.1"},
        {"lhs": "lambdau[3,3]", "rhs": "0.1"},
        {"lhs": "lambdau[i_, j_]", "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)", "delayed": true}
      ],
      "complex": false,
      "block_name": "LAMBDAU",
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_u",
      "description": "Coupling of the sextet scalar Phiu to an up-type quark, a lepton and a gluon"
    },
    {
      "name": "lambdad",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lambdad[1,1]", "rhs": "0.1"},
        {"lhs": "lambdad[2,2]", "rhs": "0.1"},
        {"lhs": "lambdad[3,3]", "rhs": "0.1"},
        {"lhs": "lambdad[i_, j_]", "rhs": "0 /; NumericQ[i] && NumericQ[j] && (i != j)", "delayed": true}
      ],
      "complex": false,
      "block_name": "LAMBDAD",
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_d",
      "description": "Coupling of the sextet scalar Phid to a down-type quark, a lepton and a gluon"
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
      "particle_name": "Phiu",
      "antiparticle_name": "Phiu~",
      "full_name": "Colour-sextet scalar coupling to up-type quarks",
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
      "particle_name": "Phid",
      "antiparticle_name": "Phid~",
      "full_name": "Colour-sextet scalar coupling to down-type quarks",
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
      "pdg": 6000003,
      "particle_name": "Psiu",
      "antiparticle_name": "Psiu~",
      "full_name": "Colour-sextet Dirac fermion coupling to up-type quarks",
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
      "pdg": 6000004,
      "particle_name": "Psid",
      "antiparticle_name": "Psid~",
      "full_name": "Colour-sextet Dirac fermion coupling to down-type quarks",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "raw_preamble": [
    "(* Colour-sextet fields of arXiv:2110.11359 (Carpenter, Murphy, Tait).      *)\n(* Field content (Table X):                                                 *)\n(*   Phiu ~ (6, 1,  1/3), L = -1    Phid ~ (6, 1,  4/3), L = -1             *)\n(*   Psiu ~ (6, 1, -2/3), L =  0    Psid ~ (6, 1,  1/3), L =  0             *)\n(* The Clebsch-Gordan coefficients J^{sia} of the 3 x 6 x 8 invariant are    *)\n(* built from Eq. (A18): J^{sia} = -I Eps[i,j,k] T[a,l,j] K6bar[s,l,k].      *)"
  ],
  "raw_blocks": [
    "AddGaugeRepresentation[SU3C -> {T6, Sextet}];"
  ],
  "lagrangian_terms": [
    {
      "name": "LSextetFermionKin",
      "expression": "Block[{mu}, ExpandIndices[I Psiubar.Ga[mu].DC[Psiu, mu] - MPsiu Psiubar.Psiu + I Psidbar.Ga[mu].DC[Psid, mu] - MPsid Psidbar.Psid]]",
      "delayed": true
    },
    {
      "name": "LSextetScalarKin",
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phiubar[ss], mu] DC[Phiu[ss], mu] - MPhiu^2 Phiubar[ss] Phiu[ss] + DC[Phidbar[ss], mu] DC[Phid[ss], mu] - MPhid^2 Phidbar[ss] Phid[ss]]]",
      "delayed": true
    },
    {
      "name": "LPsiqGnonHC",
      "expression": "Block[{mu, nu, sp1, sp2, ff, ii, jj, kk, ll, ss, aa}, ExpandIndices[-I/LamPsiu kappau[ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] anti[CC[uR]][sp1, ff, ii].Sig[mu, nu, sp1, sp2].Psiu[sp2, ss] FS[G, mu, nu, aa] - I/LamPsid kappad[ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] anti[CC[dR]][sp1, ff, ii].Sig[mu, nu, sp1, sp2].Psid[sp2, ss] FS[G, mu, nu, aa]]]",
      "delayed": true
    },
    {
      "name": "LPsiqG",
      "expression": "LPsiqGnonHC + HC[LPsiqGnonHC]",
      "delayed": true
    },
    {
      "name": "LPsiqBGnonHC",
      "expression": "Block[{mu, nu, sp, ff, ii, jj, kk, ll, ss, aa}, ExpandIndices[-I/LamPsiuB^3 kappauB[ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] anti[CC[uR]][sp, ff, ii].Psiu[sp, ss] FS[B, mu, nu] FS[G, mu, nu, aa] - I/LamPsidB^3 kappadB[ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] anti[CC[dR]][sp, ff, ii].Psid[sp, ss] FS[B, mu, nu] FS[G, mu, nu, aa]]]",
      "delayed": true
    },
    {
      "name": "LPsiqBG",
      "expression": "LPsiqBGnonHC + HC[LPsiqBGnonHC]",
      "delayed": true
    },
    {
      "name": "LPhiqlGnonHC",
      "expression": "Block[{mu, nu, sp1, sp2, ff, xx, ii, jj, kk, ll, ss, aa}, ExpandIndices[-I/LamPhiu^2 lambdau[xx, ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] Phiu[ss] anti[CC[uR]][sp1, ff, ii].Sig[mu, nu, sp1, sp2].lR[sp2, xx] FS[G, mu, nu, aa] - I/LamPhid^2 lambdad[xx, ff] Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] Phid[ss] anti[CC[dR]][sp1, ff, ii].Sig[mu, nu, sp1, sp2].lR[sp2, xx] FS[G, mu, nu, aa]]]",
      "delayed": true
    },
    {
      "name": "LPhiqlG",
      "expression": "LPhiqlGnonHC + HC[LPhiqlGnonHC]",
      "delayed": true
    },
    {
      "name": "LSextet",
      "expression": "LSextetFermionKin + LSextetScalarKin + LPsiqG + LPsiqBG + LPhiqlG",
      "delayed": true
    }
  ]
}
```

**Benchmark-integrity warning.** While searching for the FeynRules idiom for `FS[B,mu,nu]`, my repository-wide grep matched `eval/reference_cache/368sextets/368sextets.fr` — the physicist's reference file — and printed about eight lines of its Lagrangian block. I had already derived the field content, the quantum numbers, the parameters, and the J^{sia} construction from the paper before that grep, and I did not copy the reference naming or expressions. But the leak happened, so treat this run's Lagrangian score as contaminated. Restrict the search paths (or exclude `eval/reference_cache/<model>/`) for a clean re-run.