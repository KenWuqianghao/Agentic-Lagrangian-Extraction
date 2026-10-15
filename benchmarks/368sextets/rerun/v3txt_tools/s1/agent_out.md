I read the paper, the schema, the renderer and SM.fr. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content (from Table X, Eq. 12, Eq. 13)

Four new states, all SU(2)_L singlets in the colour sextet: scalars Φ_u (6,1,1/3), Φ_d (6,1,4/3) with L = −1; Dirac fermions Ψ_u (6,1,−2/3), Ψ_d (6,1,1/3) with L = 0. Hypercharge signs re-derived from the operators: the paper's bilinear `(q^c q')` adds both charges, so Eq. (12) needs Y_Ψq = −Y_qR and Eq. (13) needs Y_Φq = −Y_qR + 1. Both reproduce Table X exactly, so no convention clash with SM.fr (Q = T3 + Y, Y(uR)=2/3, Y(dR)=−1/3, Y(lR)=−1).

Colour structure: J^{sia} = −i ε^{ijk} [t^a_3]^l_j K̄^s_{lk} from Eq. (A18) with √2 L^{ijk} = ε^{ijk} (footnote 8), written with the FeynRules built-ins `Eps`, `T` and `K6bar`, exactly the "existing semi-hard-coded objects" route the paper says it used.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling symbol | coupling mass dim (4−d) | 1/Λ power (d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L sum | CC[] where paper writes ψ^c | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LKinPsiU | PsiUbar, Ga, DC[PsiU]; PsiUbar PsiU | 4 (kin) / 3 (mass) | — / MPsiU | 0 / +1 ✓ | n/a | +2/3−2/3=0 | +2/3−2/3=0 | all singlets | 6̄⊗6=1; gauge from DC via T6 | none | 0 | n/a | n/a | self-conjugate (ψ̄ψ real) |
| LKinPsiD | PsiDbar, Ga, DC[PsiD]; PsiDbar PsiD | 4 / 3 | — / MPsiD | 0 / +1 ✓ | n/a | −1/3+1/3=0 | −1/3+1/3=0 | all singlets | 6̄⊗6=1 | none | 0 | n/a | n/a | self-conjugate |
| LKinPhiU | DC[PhiUbar] DC[PhiU]; PhiUbar PhiU | 4 / 2 | — / MPhiU^2 | 0 / +2 ✓ | n/a | −1/3+1/3=0 | −1/3+1/3=0 | all singlets | 6̄⊗6=1 | none | +1−1=0 | n/a | n/a | self-conjugate |
| LKinPhiD | DC[PhiDbar] DC[PhiD]; PhiDbar PhiD | 4 / 2 | — / MPhiD^2 | 0 / +2 ✓ | n/a | −4/3+4/3=0 | −4/3+4/3=0 | all singlets | 6̄⊗6=1 | none | +1−1=0 | n/a | n/a | self-conjugate |
| LPsiUG | CC[uqbar], σ^{μν}, ProjP, PsiU, FS[G] | 3/2+3/2+2 = 5 | kapU[ff]/LamPsiU | 0 for kapU; −1 total ✓ | 1/LamPsiU^1 ✓ | 2/3−2/3=0 | 2/3−2/3=0 | all SU(2) singlets (u_R, Ψ_u, G) | 3⊗6⊗8 via Eps·T·K6bar | none | 0+0=0 | yes | d=5 ⇒ 1/Λ^1; Table IX row (qΨ)G | HC[op] |
| LPsiDG | CC[dqbar], σ^{μν}, ProjP, PsiD, FS[G] | 5 | kapD[ff]/LamPsiD | −1 ✓ | 1/LamPsiD^1 ✓ | −1/3+1/3=0 | −1/3+1/3=0 | all singlets | 3⊗6⊗8 | none | 0 | yes | as above | HC[op] |
| LPsiUB | CC[uqbar], ProjP, PsiU, FS[B], FS[G] | 3/2+3/2+2+2 = 7 | kapUB[ff]/LamPsiUB^3 | −3 ✓ | 1/LamPsiUB^3 ✓ | 2/3−2/3=0 | 2/3−2/3=0 | all singlets (B, G neutral) | 3⊗6⊗8 | none | 0 | yes | d=7 ⇒ 1/Λ^3; Table IX row 1/Λ^3_Ψ | HC[op] |
| LPsiDB | CC[dqbar], ProjP, PsiD, FS[B], FS[G] | 7 | kapDB[ff]/LamPsiDB^3 | −3 ✓ | 1/LamPsiDB^3 ✓ | −1/3+1/3=0 | −1/3+1/3=0 | all singlets | 3⊗6⊗8 | none | 0 | yes | as above | HC[op] |
| LPhiUG | PhiU, CC[uqbar], σ^{μν}, ProjP, l, FS[G] | 1+3/2+3/2+2 = 6 | lamU[ffl,ffq]/LamPhiU^2 | −2 ✓ | 1/LamPhiU^2 ✓ | 1/3+2/3−1=0 | 1/3+2/3−1=0 | all singlets (u_R, l_R, Φ, G) | 3⊗6⊗8 | none | −1+0+1=0 | yes | d=6 ⇒ 1/Λ^2; Table IX row (qℓ)ΦG | HC[op] |
| LPhiDG | PhiD, CC[dqbar], σ^{μν}, ProjP, l, FS[G] | 6 | lamD[ffl,ffq]/LamPhiD^2 | −2 ✓ | 1/LamPhiD^2 ✓ | 4/3−1/3−1=0 | 4/3−1/3−1=0 | all singlets | 3⊗6⊗8 | none | −1+0+1=0 | yes | as above | HC[op] |
| kinetic+mass check PsiU | LKinPsiU | — | Mass -> {MPsiU, 1000.} | — | — | ✓ | ✓ | — | — | — | — | — | — | present and summed in LTotal |
| kinetic+mass check PsiD | LKinPsiD | — | Mass -> {MPsiD, 1000.} | — | — | ✓ | ✓ | — | — | — | — | — | — | present and summed in LTotal |
| kinetic+mass check PhiU | LKinPhiU | — | Mass -> {MPhiU, 1000.} | — | — | ✓ | ✓ | — | — | — | — | — | — | present and summed in LTotal |
| kinetic+mass check PhiD | LKinPhiD | — | Mass -> {MPhiD, 1000.} | — | — | ✓ | ✓ | — | — | — | — | — | — | present and summed in LTotal |
| colour-rep check Sextet | Sextet index on PhiU, PhiD, PsiU, PsiD | — | — | — | — | — | — | — | `AddGaugeRepresentation[SU3C -> {T6, Sextet}];` present in raw_preamble, plus `IndexRange[Index[Sextet]] = NoUnfold[Range[6]];` and the index_decls entry | — | — | — | — | — |

Extra required lines:
- SelfConjugate -> True classes: **none**. All four new classes are complex (distinct antiparticle), so no class carries QuantumNumbers illegally.
- Names used — classes `PhiU`, `PhiD`, `PsiU`, `PsiD`; parameters `MPhiU`, `MPhiD`, `MPsiU`, `MPsiD`, `WPhiU`, `WPhiD`, `WPsiU`, `WPsiD`, `LamPsiU`, `LamPsiD`, `LamPsiUB`, `LamPsiDB`, `LamPhiU`, `LamPhiD`, `kapU`, `kapD`, `kapUB`, `kapDB`, `lamU`, `lamD`; index `Sextet`; term names `LKinPsiU`, `LKinPsiD`, `LKinPhiU`, `LKinPhiD`, `LPsiUG`, `LPsiDG`, `LPsiUB`, `LPsiDB`, `LPhiUG`, `LPhiDG`, `LTotal`. None is a Mathematica built-in, a FeynRules symbol (`HC`, `CC`, `FS`, `DC`, `del`, `Eps`, `Ga`, `ProjP`, `ProjM`, `T`, `K6bar`), or an SM.fr name (`Phi`, `H`, `lam`, `G`, `B`, `l`, `uq`, `dq`, ...). No primes or punctuation in any ParticleName.
- Single total Lagrangian: **LTotal** = LKinPsiU + LKinPsiD + LKinPhiU + LKinPhiD + LPsiUG + LPsiDG + LPsiUB + LPsiDB + LPhiUG + LPhiDG. Every other declared term appears in it; no second total is defined; no term is field-free.
- Reference or cached model file read: **none**. Only the paper text, `frmodel.py`, `render.py` and the supplied `SM.fr` were read.

Note on the CC idiom: the barred charge-conjugate is written `CC[uqbar[ff, ii]]` / `CC[dqbar[ff, ii]]` (CC applied to the barred class field with its Generation and Colour indices), which is the FeynRules spelling of `\bar{q^c}`; the bare field is never used where the paper writes q^c.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["L. M. Carpenter", "T. Murphy", "T. M. P. Tait"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "raw_preamble": [
    "(* Colour sextet: new SU(3)c index and the sextet representation matrices T6. *)\nIndexRange[Index[Sextet]] = NoUnfold[Range[6]];\nAddGaugeRepresentation[SU3C -> {T6, Sextet}];"
  ],
  "index_decls": [
    {"name": "Sextet", "range_kind": "NoUnfold", "size": 6, "style_symbol": "s6"}
  ],
  "parameters": [
    {
      "name": "LamPsiU",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SXTCUT",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_(Psi u) [GeV] of the dimension-5 operator, Eq.(12) second line; paper benchmark 1 TeV"
    },
    {
      "name": "LamPsiD",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SXTCUT",
      "order_block": 2,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_(Psi d) [GeV] of the dimension-5 operator, Eq.(12) second line; paper benchmark 1 TeV"
    },
    {
      "name": "LamPsiUB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SXTCUT",
      "order_block": 3,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_(Psi u B) [GeV] of the dimension-7 operator, Eq.(12) third line; paper benchmark 1 TeV"
    },
    {
      "name": "LamPsiDB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SXTCUT",
      "order_block": 4,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_(Psi d B) [GeV] of the dimension-7 operator, Eq.(12) third line; paper benchmark 1 TeV"
    },
    {
      "name": "LamPhiU",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SXTCUT",
      "order_block": 5,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_(Phi u) [GeV] of the dimension-6 operator, Eq.(13) second line; paper benchmark 1 TeV"
    },
    {
      "name": "LamPhiD",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "SXTCUT",
      "order_block": 6,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_(Phi d) [GeV] of the dimension-6 operator, Eq.(13) second line; paper benchmark 1 TeV"
    },
    {
      "name": "kapU",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapU[1]", "rhs": "0.05"},
        {"lhs": "kapU[2]", "rhs": "0.05"},
        {"lhs": "kapU[3]", "rhs": "0.05"}
      ],
      "complex": false,
      "block_name": "SXTKAPU",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa^I_u of the sextet fermion Psiu to an up-type quark and a gluon, Eq.(12); benchmark 0.05 per quark generation"
    },
    {
      "name": "kapD",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapD[1]", "rhs": "0.05"},
        {"lhs": "kapD[2]", "rhs": "0.05"},
        {"lhs": "kapD[3]", "rhs": "0.05"}
      ],
      "complex": false,
      "block_name": "SXTKAPD",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa^I_d of the sextet fermion Psid to a down-type quark and a gluon, Eq.(12); benchmark 0.05 per quark generation"
    },
    {
      "name": "kapUB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapUB[1]", "rhs": "0.10"},
        {"lhs": "kapUB[2]", "rhs": "0.10"},
        {"lhs": "kapUB[3]", "rhs": "0.10"}
      ],
      "complex": false,
      "block_name": "SXTKAPUB",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa^I_(u B) of the dimension-7 operator with the hypercharge and gluon field strengths, Eq.(12); benchmark 0.10 per quark generation"
    },
    {
      "name": "kapDB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapDB[1]", "rhs": "0.10"},
        {"lhs": "kapDB[2]", "rhs": "0.10"},
        {"lhs": "kapDB[3]", "rhs": "0.10"}
      ],
      "complex": false,
      "block_name": "SXTKAPDB",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa^I_(d B) of the dimension-7 operator with the hypercharge and gluon field strengths, Eq.(12); benchmark 0.10 per quark generation"
    },
    {
      "name": "lamU",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamU[1,1]", "rhs": "0.1"},
        {"lhs": "lamU[1,2]", "rhs": "0"},
        {"lhs": "lamU[1,3]", "rhs": "0"},
        {"lhs": "lamU[2,1]", "rhs": "0"},
        {"lhs": "lamU[2,2]", "rhs": "0.1"},
        {"lhs": "lamU[2,3]", "rhs": "0"},
        {"lhs": "lamU[3,1]", "rhs": "0"},
        {"lhs": "lamU[3,2]", "rhs": "0"},
        {"lhs": "lamU[3,3]", "rhs": "0.1"}
      ],
      "complex": false,
      "block_name": "SXTLAMU",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling lambda^(X I)_u of the sextet scalar Phiu to an up-type quark, a lepton and a gluon, Eq.(13); benchmark 0.1 times the identity in generation space, first index lepton generation X, second index quark generation I"
    },
    {
      "name": "lamD",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamD[1,1]", "rhs": "0.1"},
        {"lhs": "lamD[1,2]", "rhs": "0"},
        {"lhs": "lamD[1,3]", "rhs": "0"},
        {"lhs": "lamD[2,1]", "rhs": "0"},
        {"lhs": "lamD[2,2]", "rhs": "0.1"},
        {"lhs": "lamD[2,3]", "rhs": "0"},
        {"lhs": "lamD[3,1]", "rhs": "0"},
        {"lhs": "lamD[3,2]", "rhs": "0"},
        {"lhs": "lamD[3,3]", "rhs": "0.1"}
      ],
      "complex": false,
      "block_name": "SXTLAMD",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling lambda^(X I)_d of the sextet scalar Phid to a down-type quark, a lepton and a gluon, Eq.(13); benchmark 0.1 times the identity in generation space, first index lepton generation X, second index quark generation I"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "PhiU",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhiU", "value": "1000."},
      "width": {"sym": "WPhiU", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "-1"},
      "pdg": 9000006,
      "particle_name": "phiu",
      "antiparticle_name": "phiu~",
      "full_name": "Color-sextet scalar coupling to up-type quarks",
      "propagator_label": "PhiU",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "PhiD",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhiD", "value": "1000."},
      "width": {"sym": "WPhiD", "value": "1."},
      "quantum_numbers": {"Q": "4/3", "Y": "4/3", "LeptonNumber": "-1"},
      "pdg": 9000007,
      "particle_name": "phid",
      "antiparticle_name": "phid~",
      "full_name": "Color-sextet scalar coupling to down-type quarks",
      "propagator_label": "PhiD",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "PsiU",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiU", "value": "1000."},
      "width": {"sym": "WPsiU", "value": "1."},
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3"},
      "pdg": 9000008,
      "particle_name": "psiu",
      "antiparticle_name": "psiu~",
      "full_name": "Color-sextet Dirac fermion coupling to up-type quarks",
      "propagator_label": "PsiU",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "PsiD",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiD", "value": "1000."},
      "width": {"sym": "WPsiD", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3"},
      "pdg": 9000009,
      "particle_name": "psid",
      "antiparticle_name": "psid~",
      "full_name": "Color-sextet Dirac fermion coupling to down-type quarks",
      "propagator_label": "PsiD",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LKinPsiU",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I PsiUbar.Ga[mu].DC[PsiU, mu] - MPsiU PsiUbar.PsiU]]"
    },
    {
      "name": "LKinPsiD",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I PsiDbar.Ga[mu].DC[PsiD, mu] - MPsiD PsiDbar.PsiD]]"
    },
    {
      "name": "LKinPhiU",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[DC[PhiUbar, mu] DC[PhiU, mu] - MPhiU^2 PhiUbar PhiU]]"
    },
    {
      "name": "LKinPhiD",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[DC[PhiDbar, mu] DC[PhiD, mu] - MPhiD^2 PhiDbar PhiD]]"
    },
    {
      "name": "LPsiUG",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, ss, aa, op}, op = -I kapU[ff]/LamPsiU Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] (CC[uqbar[ff, ii]].(I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu])).ProjP.PsiU[ss]) FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPsiDG",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, ss, aa, op}, op = -I kapD[ff]/LamPsiD Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] (CC[dqbar[ff, ii]].(I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu])).ProjP.PsiD[ss]) FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPsiUB",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, ss, aa, op}, op = -I kapUB[ff]/LamPsiUB^3 Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] (CC[uqbar[ff, ii]].ProjP.PsiU[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPsiDB",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, ss, aa, op}, op = -I kapDB[ff]/LamPsiDB^3 Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] (CC[dqbar[ff, ii]].ProjP.PsiD[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPhiUG",
      "delayed": true,
      "expression": "Block[{mu, nu, ffl, ffq, ii, jj, kk, ll, ss, aa, op}, op = -I lamU[ffl, ffq]/LamPhiU^2 Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] PhiU[ss] (CC[uqbar[ffq, ii]].(I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu])).ProjP.l[ffl]) FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LPhiDG",
      "delayed": true,
      "expression": "Block[{mu, nu, ffl, ffq, ii, jj, kk, ll, ss, aa, op}, op = -I lamD[ffl, ffq]/LamPhiD^2 Eps[ii, jj, kk] T[aa, ll, jj] K6bar[ss, ll, kk] PhiD[ss] (CC[dqbar[ffq, ii]].(I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu])).ProjP.l[ffl]) FS[G, mu, nu, aa]; ExpandIndices[op + HC[op]]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LKinPsiU + LKinPsiD + LKinPhiU + LKinPhiD + LPsiUG + LPsiDG + LPsiUB + LPsiDB + LPhiUG + LPhiDG"
    }
  ]
}
```