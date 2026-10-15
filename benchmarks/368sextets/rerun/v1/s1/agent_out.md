I'll start by reading the paper and the schema.
Now the rest of the paper, especially the appendix on the FeynRules implementation.
I've read the paper, the schema, the renderer, and SM.fr. Here is what I extracted.

**New states (Table X, Sec. III).** Four color-sextet, SU(2)-singlet fields: scalars Φ_u (6,1,1/3) and Φ_d (6,1,4/3) with lepton number −1, and Dirac fermions Ψ_u (6,1,−2/3) and Ψ_d (6,1,1/3) with lepton number 0. I checked each hypercharge against the operators in Eqs. (12)–(13) and they close.

**Two notes on the encoding.** The color index is a genuinely new index, so `Sextet` gets an `index_decls` entry with `NoUnfold[Range[6]]`. The Clebsch-Gordan coefficient J^{sia} is not a FeynRules built-in; the paper's Eq. (A18) builds it from objects FeynRules already has, so I put that construction in `raw_blocks` as `JJ[s,i,a] = -I Eps[i,j,k] T[a,l,j] K6bar[s,l,k]`. I kept `gauge_groups` empty per the schema rule; that means SU3C in SM.fr carries only the triplet representation, so a real run of this file must also add `{T6, Sextet}` to the SU3C `Representations` list for `DC[]` to give the sextets their gluon coupling.

I left out the 3⊗3⊗6̄ "sextet diquark" operators of Table VIII on purpose: they are gauge-allowed for these hypercharges but break the L = −1 assignment the paper gives the scalars, and they are not part of the implemented model.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["Linda M. Carpenter", "Taylor Murphy", "Tim M. P. Tait"],
    "version": "1.0",
    "date": "09. 09. 2022",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
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
      "name": "kapu",
      "parameter_type": "External",
      "block_name": "KAPU",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05"},
        {"lhs": "kapu[2]", "rhs": "0.05"},
        {"lhs": "kapu[3]", "rhs": "0.05"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_u",
      "description": "Coupling of the up-type sextet fermion to an up-type quark and a gluon"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "block_name": "KAPD",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05"},
        {"lhs": "kapd[2]", "rhs": "0.05"},
        {"lhs": "kapd[3]", "rhs": "0.05"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_d",
      "description": "Coupling of the down-type sextet fermion to a down-type quark and a gluon"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "block_name": "KAPUB",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.10"},
        {"lhs": "kapuB[2]", "rhs": "0.10"},
        {"lhs": "kapuB[3]", "rhs": "0.10"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{uB}",
      "description": "Coupling of the up-type sextet fermion to an up-type quark, a gluon and a hypercharge boson"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "block_name": "KAPDB",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.10"},
        {"lhs": "kapdB[2]", "rhs": "0.10"},
        {"lhs": "kapdB[3]", "rhs": "0.10"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{dB}",
      "description": "Coupling of the down-type sextet fermion to a down-type quark, a gluon and a hypercharge boson"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "block_name": "LAMU",
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
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_u",
      "description": "Coupling of the up-type sextet scalar to an up-type quark, a lepton and a gluon"
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "block_name": "LAMD",
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
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_d",
      "description": "Coupling of the down-type sextet scalar to a down-type quark, a lepton and a gluon"
    },
    {
      "name": "LambPsiu",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 1,
      "value": "1000.",
      "tex": "\\Lambda_{\\Psi u}",
      "description": "EFT cutoff scale of the up-type sextet fermion quark-gluon operator"
    },
    {
      "name": "LambPsid",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 2,
      "value": "1000.",
      "tex": "\\Lambda_{\\Psi d}",
      "description": "EFT cutoff scale of the down-type sextet fermion quark-gluon operator"
    },
    {
      "name": "LambPsiuB",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 3,
      "value": "1000.",
      "tex": "\\Lambda_{\\Psi uB}",
      "description": "EFT cutoff scale of the up-type sextet fermion quark-gluon-hypercharge operator"
    },
    {
      "name": "LambPsidB",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 4,
      "value": "1000.",
      "tex": "\\Lambda_{\\Psi dB}",
      "description": "EFT cutoff scale of the down-type sextet fermion quark-gluon-hypercharge operator"
    },
    {
      "name": "LambPhiu",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 5,
      "value": "1000.",
      "tex": "\\Lambda_{\\Phi u}",
      "description": "EFT cutoff scale of the up-type sextet scalar quark-lepton-gluon operator"
    },
    {
      "name": "LambPhid",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 6,
      "value": "1000.",
      "tex": "\\Lambda_{\\Phi d}",
      "description": "EFT cutoff scale of the down-type sextet scalar quark-lepton-gluon operator"
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
      "quantum_numbers": {"Y": "1/3", "Q": "1/3", "LeptonNumber": "-1"},
      "pdg": 9000001,
      "particle_name": "phiu",
      "antiparticle_name": "phiu~",
      "full_name": "Up-type color-sextet scalar",
      "propagator_label": "Phiu",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Phid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhid", "value": "1000."},
      "width": {"sym": "WPhid", "value": "1."},
      "quantum_numbers": {"Y": "4/3", "Q": "4/3", "LeptonNumber": "-1"},
      "pdg": 9000002,
      "particle_name": "phid",
      "antiparticle_name": "phid~",
      "full_name": "Down-type color-sextet scalar",
      "propagator_label": "Phid",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Psiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiu", "value": "1000."},
      "width": {"sym": "WPsiu", "value": "1."},
      "quantum_numbers": {"Y": "-2/3", "Q": "-2/3", "LeptonNumber": "0"},
      "pdg": 9000003,
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
      "quantum_numbers": {"Y": "1/3", "Q": "1/3", "LeptonNumber": "0"},
      "pdg": 9000004,
      "particle_name": "psid",
      "antiparticle_name": "psid~",
      "full_name": "Down-type color-sextet Dirac fermion",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "raw_blocks": [
    "(* sigma^{mu nu} = I/2 [Ga[mu], Ga[nu]] with explicit spin indices *)\nSigMuNu[mu_, nu_][sp1_, sp2_] := I/2 (TensDot[Ga[mu], Ga[nu]][sp1, sp2] - TensDot[Ga[nu], Ga[mu]][sp1, sp2]);",
    "(* Clebsch-Gordan coefficients J^{s i a} of the 3 x 6 x 8 invariant, built from *)\n(* the hard-coded FeynRules objects Eps, T and K6bar as in Eq. (A18):            *)\n(* J^{sia} = -I Sqrt[2] L^{ijk} [T^a]^l_j Kbar^s_{lk},  Sqrt[2] L^{ijk} = Eps^{ijk} *)\nJJ[ss_, ii_, aa_] := Module[{jj, kk, ll}, -I Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk]];"
  ],
  "lagrangian_terms": [
    {
      "name": "LPsiKin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[I*Psiubar[ss].Ga[mu].DC[Psiu[ss], mu] - MPsiu Psiubar[ss].Psiu[ss] + I*Psidbar[ss].Ga[mu].DC[Psid[ss], mu] - MPsid Psidbar[ss].Psid[ss]]]"
    },
    {
      "name": "LPhiKin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phiubar[ss], mu] DC[Phiu[ss], mu] - MPhiu^2 Phiubar[ss] Phiu[ss] + DC[Phidbar[ss], mu] DC[Phid[ss], mu] - MPhid^2 Phidbar[ss] Phid[ss]]]"
    },
    {
      "name": "LPsiqG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, ii, aa, ss, ff, res}, res = ExpandIndices[kapu[ff]/LambPsiu JJ[ss, ii, aa] SigMuNu[mu, nu][sp1, sp2] CC[uR[sp1, ff, ii]] Psiu[sp2, ss] FS[G, mu, nu, aa] + kapd[ff]/LambPsid JJ[ss, ii, aa] SigMuNu[mu, nu][sp1, sp2] CC[dR[sp1, ff, ii]] Psid[sp2, ss] FS[G, mu, nu, aa]]; res + HC[res]]"
    },
    {
      "name": "LPsiqBG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, ii, aa, ss, ff, res}, res = ExpandIndices[kapuB[ff]/LambPsiuB^3 JJ[ss, ii, aa] CC[uR[sp1, ff, ii]] Psiu[sp1, ss] FS[B, mu, nu] FS[G, mu, nu, aa] + kapdB[ff]/LambPsidB^3 JJ[ss, ii, aa] CC[dR[sp1, ff, ii]] Psid[sp1, ss] FS[B, mu, nu] FS[G, mu, nu, aa]]; res + HC[res]]"
    },
    {
      "name": "LPhiqlG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, ii, aa, ss, ff, xx, res}, res = ExpandIndices[lamu[xx, ff]/LambPhiu^2 JJ[ss, ii, aa] Phiu[ss] SigMuNu[mu, nu][sp1, sp2] CC[uR[sp1, ff, ii]] lR[sp2, xx] FS[G, mu, nu, aa] + lamd[xx, ff]/LambPhid^2 JJ[ss, ii, aa] Phid[ss] SigMuNu[mu, nu][sp1, sp2] CC[dR[sp1, ff, ii]] lR[sp2, xx] FS[G, mu, nu, aa]]; res + HC[res]]"
    },
    {
      "name": "LSextet",
      "delayed": true,
      "expression": "LPsiKin + LPhiKin + LPsiqG + LPsiqBG + LPhiqlG"
    }
  ]
}
```
I've read the paper, the schema, the renderer, and SM.fr. Here is what I extracted.

**New states (Table X, Sec. III).** Four color-sextet, SU(2)-singlet fields: scalars Φ_u (6,1,1/3) and Φ_d (6,1,4/3) with lepton number −1, and Dirac fermions Ψ_u (6,1,−2/3) and Ψ_d (6,1,1/3) with lepton number 0. I checked each hypercharge against the operators in Eqs. (12)–(13) and they close.

**Two notes on the encoding.** The color index is a genuinely new index, so `Sextet` gets an `index_decls` entry with `NoUnfold[Range[6]]`. The Clebsch-Gordan coefficient J^{sia} is not a FeynRules built-in; the paper's Eq. (A18) builds it from objects FeynRules already has, so I put that construction in `raw_blocks` as `JJ[s,i,a] = -I Eps[i,j,k] T[a,l,j] K6bar[s,l,k]`. I kept `gauge_groups` empty per the schema rule; that means SU3C in SM.fr carries only the triplet representation, so a real run of this file must also add `{T6, Sextet}` to the SU3C `Representations` list for `DC[]` to give the sextets their gluon coupling.

I left out the 3⊗3⊗6̄ "sextet diquark" operators of Table VIII on purpose: they are gauge-allowed for these hypercharges but break the L = −1 assignment the paper gives the scalars, and they are not part of the implemented model.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["Linda M. Carpenter", "Taylor Murphy", "Tim M. P. Tait"],
    "version": "1.0",
    "date": "09. 09. 2022",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
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
      "name": "kapu",
      "parameter_type": "External",
      "block_name": "KAPU",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05"},
        {"lhs": "kapu[2]", "rhs": "0.05"},
        {"lhs": "kapu[3]", "rhs": "0.05"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_u",
      "description": "Coupling of the up-type sextet fermion to an up-type quark and a gluon"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "block_name": "KAPD",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05"},
        {"lhs": "kapd[2]", "rhs": "0.05"},
        {"lhs": "kapd[3]", "rhs": "0.05"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_d",
      "description": "Coupling of the down-type sextet fermion to a down-type quark and a gluon"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "block_name": "KAPUB",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.10"},
        {"lhs": "kapuB[2]", "rhs": "0.10"},
        {"lhs": "kapuB[3]", "rhs": "0.10"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{uB}",
      "description": "Coupling of the up-type sextet fermion to an up-type quark, a gluon and a hypercharge boson"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "block_name": "KAPDB",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.10"},
        {"lhs": "kapdB[2]", "rhs": "0.10"},
        {"lhs": "kapdB[3]", "rhs": "0.10"}
      ],
      "interaction_order": ["NP", 1],
      "tex": "\\kappa^I_{dB}",
      "description": "Coupling of the down-type sextet fermion to a down-type quark, a gluon and a hypercharge boson"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "block_name": "LAMU",
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
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_u",
      "description": "Coupling of the up-type sextet scalar to an up-type quark, a lepton and a gluon"
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "block_name": "LAMD",
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
      "interaction_order": ["NP", 1],
      "tex": "\\lambda^{XI}_d",
      "description": "Coupling of the down-type sextet scalar to a down-type quark, a lepton and a gluon"
    },
    {
      "name": "LambPsiu",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 1,
      "value": "1000.",
      "tex": "\\Lambda_{\\Psi u}",
      "description": "EFT cutoff scale of the up-type sextet fermion quark-gluon operator"
    },
    {
      "name": "LambPsid",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 2,
      "value": "1000.",
      "tex": "\\Lambda_{\\Psi d}",
      "description": "EFT cutoff scale of the down-type sextet fermion quark-gluon operator"
    },
    {
      "name": "LambPsiuB",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 3,
      "value": "1000.",
      "tex": "\\Lambda_{\\Psi uB}",
      "description": "EFT cutoff scale of the up-type sextet fermion quark-gluon-hypercharge operator"
    },
    {
      "name": "LambPsidB",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 4,
      "value": "1000.",
      "tex": "\\Lambda_{\\Psi dB}",
      "description": "EFT cutoff scale of the down-type sextet fermion quark-gluon-hypercharge operator"
    },
    {
      "name": "LambPhiu",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 5,
      "value": "1000.",
      "tex": "\\Lambda_{\\Phi u}",
      "description": "EFT cutoff scale of the up-type sextet scalar quark-lepton-gluon operator"
    },
    {
      "name": "LambPhid",
      "parameter_type": "External",
      "block_name": "SXTCUT",
      "order_block": 6,
      "value": "1000.",
      "tex": "\\Lambda_{\\Phi d}",
      "description": "EFT cutoff scale of the down-type sextet scalar quark-lepton-gluon operator"
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
      "quantum_numbers": {"Y": "1/3", "Q": "1/3", "LeptonNumber": "-1"},
      "pdg": 9000001,
      "particle_name": "phiu",
      "antiparticle_name": "phiu~",
      "full_name": "Up-type color-sextet scalar",
      "propagator_label": "Phiu",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Phid",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhid", "value": "1000."},
      "width": {"sym": "WPhid", "value": "1."},
      "quantum_numbers": {"Y": "4/3", "Q": "4/3", "LeptonNumber": "-1"},
      "pdg": 9000002,
      "particle_name": "phid",
      "antiparticle_name": "phid~",
      "full_name": "Down-type color-sextet scalar",
      "propagator_label": "Phid",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Psiu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiu", "value": "1000."},
      "width": {"sym": "WPsiu", "value": "1."},
      "quantum_numbers": {"Y": "-2/3", "Q": "-2/3", "LeptonNumber": "0"},
      "pdg": 9000003,
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
      "quantum_numbers": {"Y": "1/3", "Q": "1/3", "LeptonNumber": "0"},
      "pdg": 9000004,
      "particle_name": "psid",
      "antiparticle_name": "psid~",
      "full_name": "Down-type color-sextet Dirac fermion",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "raw_blocks": [
    "(* sigma^{mu nu} = I/2 [Ga[mu], Ga[nu]] with explicit spin indices *)\nSigMuNu[mu_, nu_][sp1_, sp2_] := I/2 (TensDot[Ga[mu], Ga[nu]][sp1, sp2] - TensDot[Ga[nu], Ga[mu]][sp1, sp2]);",
    "(* Clebsch-Gordan coefficients J^{s i a} of the 3 x 6 x 8 invariant, built from *)\n(* the hard-coded FeynRules objects Eps, T and K6bar as in Eq. (A18):            *)\n(* J^{sia} = -I Sqrt[2] L^{ijk} [T^a]^l_j Kbar^s_{lk},  Sqrt[2] L^{ijk} = Eps^{ijk} *)\nJJ[ss_, ii_, aa_] := Module[{jj, kk, ll}, -I Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk]];"
  ],
  "lagrangian_terms": [
    {
      "name": "LPsiKin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[I*Psiubar[ss].Ga[mu].DC[Psiu[ss], mu] - MPsiu Psiubar[ss].Psiu[ss] + I*Psidbar[ss].Ga[mu].DC[Psid[ss], mu] - MPsid Psidbar[ss].Psid[ss]]]"
    },
    {
      "name": "LPhiKin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phiubar[ss], mu] DC[Phiu[ss], mu] - MPhiu^2 Phiubar[ss] Phiu[ss] + DC[Phidbar[ss], mu] DC[Phid[ss], mu] - MPhid^2 Phidbar[ss] Phid[ss]]]"
    },
    {
      "name": "LPsiqG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, ii, aa, ss, ff, res}, res = ExpandIndices[kapu[ff]/LambPsiu JJ[ss, ii, aa] SigMuNu[mu, nu][sp1, sp2] CC[uR[sp1, ff, ii]] Psiu[sp2, ss] FS[G, mu, nu, aa] + kapd[ff]/LambPsid JJ[ss, ii, aa] SigMuNu[mu, nu][sp1, sp2] CC[dR[sp1, ff, ii]] Psid[sp2, ss] FS[G, mu, nu, aa]]; res + HC[res]]"
    },
    {
      "name": "LPsiqBG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, ii, aa, ss, ff, res}, res = ExpandIndices[kapuB[ff]/LambPsiuB^3 JJ[ss, ii, aa] CC[uR[sp1, ff, ii]] Psiu[sp1, ss] FS[B, mu, nu] FS[G, mu, nu, aa] + kapdB[ff]/LambPsidB^3 JJ[ss, ii, aa] CC[dR[sp1, ff, ii]] Psid[sp1, ss] FS[B, mu, nu] FS[G, mu, nu, aa]]; res + HC[res]]"
    },
    {
      "name": "LPhiqlG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp1, sp2, ii, aa, ss, ff, xx, res}, res = ExpandIndices[lamu[xx, ff]/LambPhiu^2 JJ[ss, ii, aa] Phiu[ss] SigMuNu[mu, nu][sp1, sp2] CC[uR[sp1, ff, ii]] lR[sp2, xx] FS[G, mu, nu, aa] + lamd[xx, ff]/LambPhid^2 JJ[ss, ii, aa] Phid[ss] SigMuNu[mu, nu][sp1, sp2] CC[dR[sp1, ff, ii]] lR[sp2, xx] FS[G, mu, nu, aa]]; res + HC[res]]"
    },
    {
      "name": "LSextet",
      "delayed": true,
      "expression": "LPsiKin + LPhiKin + LPsiqG + LPsiqBG + LPhiqlG"
    }
  ]
}
```