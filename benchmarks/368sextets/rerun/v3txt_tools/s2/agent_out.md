I read the paper, the schema, the renderer, and `SM.fr`. No reference or cached `.fr` model file for this model exists in the sandbox, and none was read.

## Extraction summary

New content (Table X, Eqs. (12)–(13), Tables VIII–IX): four colour-sextet, SU(2)-singlet states — scalars Φ_u (6,1,1/3), Φ_d (6,1,4/3) with L = −1, and Dirac fermions Ψ_u (6,1,−2/3), Ψ_d (6,1,1/3) with L = 0. Three operator families: dim-5 `q^c σ Ψ G` (1/Λ), dim-7 `q^c Ψ B G` (1/Λ³), dim-6 `Φ q^c σ ℓ G` (1/Λ²).

The colour coefficient J^sia is built from Eq. (A18) plus footnote 8 (√2 L^ijk = ε^ijk), i.e. `J = -I Eps[i,j,k] T[a,j,l] K6bar[s,l,k]`, as the paper itself prescribes for FeynRules/MadGraph.

## Mandatory self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ power (=d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LSXukin | DC[SXubar]·DC[SXu]; MSXu² SXubar SXu | 4 (kin), 2 (mass) | MSXu² | 2 = 4−2 | n/a | −1/3+1/3 = 0 | −1/3+1/3 = 0 | singlet | 6̄⊗6 shared Sextet index | none | +1−1 = 0 | n/a | n/a | self-conjugate (real) |
| LSXdkin | DC[SXdbar]·DC[SXd]; MSXd² SXdbar SXd | 4 / 2 | MSXd² | 2 | n/a | −4/3+4/3 = 0 | −4/3+4/3 = 0 | singlet | 6̄⊗6 | none | +1−1 = 0 | n/a | n/a | self-conjugate |
| LFXukin | FXubar Ga DC[FXu]; MFXu FXubar FXu | 4 / 3 | MFXu | 1 = 4−3 | n/a | +2/3−2/3 = 0 | +2/3−2/3 = 0 | singlet | 6̄⊗6 | none | 0 | n/a | n/a | self-conjugate |
| LFXdkin | FXdbar Ga DC[FXd]; MFXd FXdbar FXd | 4 / 3 | MFXd | 1 | n/a | −1/3+1/3 = 0 | −1/3+1/3 = 0 | singlet | 6̄⊗6 | none | 0 | n/a | n/a | self-conjugate |
| LFXuG | bar(u_R^c)(3/2), FXu(3/2), FS[G](2) | 5 | kapFXu/CutFXu | −1 = 4−5 | 1 ✓ | +2/3−2/3+0 = 0 | +2/3−2/3 = 0 | singlet | 3⊗6⊗8 via J = −I Eps[i,j,k] T[a,j,l] K6bar[s,l,k] | none | 0+0 = 0 | yes | Eq.(A18)+fn.8; **numerically verified** against explicit J¹ of Eq.(A15) (J^{1,2,2}=−i/2, J^{1,2,5}=+1/2, J^{1,3,1}=+i/2, J^{1,3,4}=−1/2) — this fixes the generator order to `T[a,j,l]`, not `T[a,l,j]` | HC[] |
| LFXdG | bar(d_R^c), FXd, FS[G] | 5 | kapFXd/CutFXd | −1 | 1 ✓ | −1/3+1/3 = 0 | −1/3+1/3 = 0 | singlet | same J | none | 0 | yes | same as above | HC[] |
| LFXuB | bar(u_R^c), FXu, FS[B](2), FS[G](2) | 7 | kapFXuB/CutFXuB³ | −3 = 4−7 | 3 ✓ | +2/3−2/3 = 0 | +2/3−2/3 = 0 | singlet | same J | none | 0 | yes | 1/Λ³ cross-checked by dimension count d=7 (Table IX, row 2) | HC[] |
| LFXdB | bar(d_R^c), FXd, FS[B], FS[G] | 7 | kapFXdB/CutFXdB³ | −3 | 3 ✓ | −1/3+1/3 = 0 | −1/3+1/3 = 0 | singlet | same J | none | 0 | yes | same | HC[] |
| LSXuG | SXu(1), bar(u_R^c)(3/2), l_R(3/2), FS[G](2) | 6 | lamSXu/CutSXu² | −2 = 4−6 | 2 ✓ | 1/3+2/3−1+0 = 0 | 1/3+2/3−1 = 0 | singlet (all SU(2) singlets) | same J | none | −1+1 = 0 | yes | 1/Λ² cross-checked by dimension count d=6 (Table IX, row 1) | HC[] |
| LSXdG | SXd, bar(d_R^c), l_R, FS[G] | 6 | lamSXd/CutSXd² | −2 | 2 ✓ | 4/3−1/3−1 = 0 | 4/3−1/3−1 = 0 | singlet | same J | none | −1+1 = 0 | yes | same | HC[] |
| *(rep row)* | colour sextet | — | — | — | — | — | — | — | `AddGaugeRepresentation[SU3C -> {T6, Sextet}]` present in `raw_preamble`, with `IndexRange[Index[Sextet]] = NoUnfold[Range[6]]` before it; `index_decls` keeps the Sextet entry | — | — | — | — | — |

- Kinetic + mass terms exist for all four new classes (rows 1–4) and all four are in the total sum.
- `SelfConjugate -> True` classes: **none**. All four new classes are complex/Dirac (`self_conjugate: false`), so no `QuantumNumbers` conflict arises.
- Names chosen: classes `SXu, SXd, FXu, FXd`; parameters `MSXu, MSXd, MFXu, MFXd, WSXu, WSXd, WFXu, WFXd, kapFXu, kapFXd, kapFXuB, kapFXdB, lamSXu, lamSXd, CutFXu, CutFXd, CutFXuB, CutFXdB, CutSXu, CutSXd`; index `Sextet` (style `sx`). None is a Mathematica built-in, a FeynRules symbol, or a name `SM.fr` declares. Class indices are 100/101.
- Single total: `LTotal` sums `LSXukin, LSXdkin, LFXukin, LFXdkin, LFXuG, LFXdG, LFXuB, LFXdB, LSXuG, LSXdG`. No second total.
- New U(1) groups: the paper adds none, so rule 5 does not apply; hypercharges are taken from Table X and re-derived from `SM.fr` conventions (Y(u_R) = 2/3, Y(d_R) = −1/3, Y(l_R) = −1), which reproduces Table X exactly.
- σ^{μν} is written as `I Ga[mu].Ga[nu]` contracted with the antisymmetric field strength (exact identity σ^{μν}F_{μν} = i γ^μγ^ν F_{μν}), so no non-guaranteed Dirac symbol is used.
- Reference or cached model file read: **none**.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["L. M. Carpenter", "T. Murphy", "T. M. P. Tait"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [
    {"name": "Sextet", "range_kind": "NoUnfold", "size": 6, "style_symbol": "sx"}
  ],
  "raw_preamble": [
    "(* Colour-sextet representation of SU(3)c. The index range must exist before AddGaugeRepresentation, and both must precede the field declarations. *)\nIndexRange[Index[Sextet]] = NoUnfold[Range[6]];\nIndexStyle[Sextet, sx];\nAddGaugeRepresentation[SU3C -> {T6, Sextet}];"
  ],
  "parameters": [
    {
      "name": "CutFXu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Psiu [GeV] of the dimension-5 sextet-fermion / up-type-quark / gluon operator, Eq.(12) second line. Benchmark 1 TeV."
    },
    {
      "name": "CutFXd",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 2,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Psid [GeV] of the dimension-5 sextet-fermion / down-type-quark / gluon operator, Eq.(12) second line. Benchmark 1 TeV."
    },
    {
      "name": "CutFXuB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 3,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_PsiuB [GeV] of the dimension-7 operator with B and G field strengths, Eq.(12) third line. Benchmark 1 TeV."
    },
    {
      "name": "CutFXdB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 4,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_PsidB [GeV] of the dimension-7 operator with B and G field strengths, Eq.(12) third line. Benchmark 1 TeV."
    },
    {
      "name": "CutSXu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 5,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Phiu [GeV] of the dimension-6 sextet-scalar / quark / lepton / gluon operator, Eq.(13). Benchmark 1 TeV."
    },
    {
      "name": "CutSXd",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 6,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Phid [GeV] of the dimension-6 sextet-scalar / quark / lepton / gluon operator, Eq.(13). Benchmark 1 TeV."
    },
    {
      "name": "kapFXu",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapFXu[1]", "rhs": "0.05"},
        {"lhs": "kapFXu[2]", "rhs": "0.05"},
        {"lhs": "kapFXu[3]", "rhs": "0.05"}
      ],
      "block_name": "KAPFXU",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa^I_u of the dimension-5 operator J^sia (u^c_RI sigma^munu Psi_u) G^a_munu, Eq.(12). Benchmark 0.05 per quark generation."
    },
    {
      "name": "kapFXd",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapFXd[1]", "rhs": "0.05"},
        {"lhs": "kapFXd[2]", "rhs": "0.05"},
        {"lhs": "kapFXd[3]", "rhs": "0.05"}
      ],
      "block_name": "KAPFXD",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa^I_d of the dimension-5 operator J^sia (d^c_RI sigma^munu Psi_d) G^a_munu, Eq.(12). Benchmark 0.05 per quark generation."
    },
    {
      "name": "kapFXuB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapFXuB[1]", "rhs": "0.1"},
        {"lhs": "kapFXuB[2]", "rhs": "0.1"},
        {"lhs": "kapFXuB[3]", "rhs": "0.1"}
      ],
      "block_name": "KAPFXUB",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa^I_uB of the dimension-7 operator J^sia (u^c_RI Psi_u) B_munu G^a_munu, Eq.(12). Benchmark 0.10 per quark generation."
    },
    {
      "name": "kapFXdB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapFXdB[1]", "rhs": "0.1"},
        {"lhs": "kapFXdB[2]", "rhs": "0.1"},
        {"lhs": "kapFXdB[3]", "rhs": "0.1"}
      ],
      "block_name": "KAPFXDB",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa^I_dB of the dimension-7 operator J^sia (d^c_RI Psi_d) B_munu G^a_munu, Eq.(12). Benchmark 0.10 per quark generation."
    },
    {
      "name": "lamSXu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamSXu[1,1]", "rhs": "0.1"},
        {"lhs": "lamSXu[1,2]", "rhs": "0."},
        {"lhs": "lamSXu[1,3]", "rhs": "0."},
        {"lhs": "lamSXu[2,1]", "rhs": "0."},
        {"lhs": "lamSXu[2,2]", "rhs": "0.1"},
        {"lhs": "lamSXu[2,3]", "rhs": "0."},
        {"lhs": "lamSXu[3,1]", "rhs": "0."},
        {"lhs": "lamSXu[3,2]", "rhs": "0."},
        {"lhs": "lamSXu[3,3]", "rhs": "0.1"}
      ],
      "block_name": "LAMSXU",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling lambda^XI_u of the dimension-6 operator J^sia Phi_u (u^c_RI sigma^munu l_RX) G^a_munu, Eq.(13). First index X is the lepton generation, second index I is the quark generation. Benchmark 0.1 times delta^XI."
    },
    {
      "name": "lamSXd",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamSXd[1,1]", "rhs": "0.1"},
        {"lhs": "lamSXd[1,2]", "rhs": "0."},
        {"lhs": "lamSXd[1,3]", "rhs": "0."},
        {"lhs": "lamSXd[2,1]", "rhs": "0."},
        {"lhs": "lamSXd[2,2]", "rhs": "0.1"},
        {"lhs": "lamSXd[2,3]", "rhs": "0."},
        {"lhs": "lamSXd[3,1]", "rhs": "0."},
        {"lhs": "lamSXd[3,2]", "rhs": "0."},
        {"lhs": "lamSXd[3,3]", "rhs": "0.1"}
      ],
      "block_name": "LAMSXD",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling lambda^XI_d of the dimension-6 operator J^sia Phi_d (d^c_RI sigma^munu l_RX) G^a_munu, Eq.(13). First index X is the lepton generation, second index I is the quark generation. Benchmark 0.1 times delta^XI."
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "SXu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MSXu", "value": "1000."},
      "width": {"sym": "WSXu", "value": "1."},
      "quantum_numbers": {"Y": "1/3", "Q": "1/3", "LeptonNumber": "-1"},
      "pdg": 9000001,
      "particle_name": "sxu",
      "antiparticle_name": "sxu~",
      "full_name": "SextetScalarUp",
      "propagator_label": "SXu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "SXd",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MSXd", "value": "1000."},
      "width": {"sym": "WSXd", "value": "1."},
      "quantum_numbers": {"Y": "4/3", "Q": "4/3", "LeptonNumber": "-1"},
      "pdg": 9000002,
      "particle_name": "sxd",
      "antiparticle_name": "sxd~",
      "full_name": "SextetScalarDown",
      "propagator_label": "SXd",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "FXu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MFXu", "value": "1000."},
      "width": {"sym": "WFXu", "value": "1."},
      "quantum_numbers": {"Y": "-2/3", "Q": "-2/3"},
      "pdg": 9000003,
      "particle_name": "fxu",
      "antiparticle_name": "fxu~",
      "full_name": "SextetFermionUp",
      "propagator_label": "FXu",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "FXd",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MFXd", "value": "1000."},
      "width": {"sym": "WFXd", "value": "1."},
      "quantum_numbers": {"Y": "1/3", "Q": "1/3"},
      "pdg": 9000004,
      "particle_name": "fxd",
      "antiparticle_name": "fxd~",
      "full_name": "SextetFermionDown",
      "propagator_label": "FXd",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LSXukin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[DC[SXubar, mu] DC[SXu, mu] - MSXu^2 SXubar SXu]]"
    },
    {
      "name": "LSXdkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[DC[SXdbar, mu] DC[SXd, mu] - MSXd^2 SXdbar SXd]]"
    },
    {
      "name": "LFXukin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I FXubar.Ga[mu].DC[FXu, mu] - MFXu FXubar.FXu]]"
    },
    {
      "name": "LFXdkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I FXdbar.Ga[mu].DC[FXd, mu] - MFXd FXdbar.FXd]]"
    },
    {
      "name": "LFXuG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp, ii, jj, kk, ll, ss, aa, ff, op}, op = ExpandIndices[(-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (I kapFXu[ff]/CutFXu) (CC[uq[sp, ff, ii]].ProjP.Ga[mu].Ga[nu].FXu[sp, ss]) FS[G, mu, nu, aa]]; op + HC[op]]"
    },
    {
      "name": "LFXdG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp, ii, jj, kk, ll, ss, aa, ff, op}, op = ExpandIndices[(-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (I kapFXd[ff]/CutFXd) (CC[dq[sp, ff, ii]].ProjP.Ga[mu].Ga[nu].FXd[sp, ss]) FS[G, mu, nu, aa]]; op + HC[op]]"
    },
    {
      "name": "LFXuB",
      "delayed": true,
      "expression": "Block[{mu, nu, sp, ii, jj, kk, ll, ss, aa, ff, op}, op = ExpandIndices[(-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (kapFXuB[ff]/CutFXuB^3) (CC[uq[sp, ff, ii]].ProjP.FXu[sp, ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; op + HC[op]]"
    },
    {
      "name": "LFXdB",
      "delayed": true,
      "expression": "Block[{mu, nu, sp, ii, jj, kk, ll, ss, aa, ff, op}, op = ExpandIndices[(-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (kapFXdB[ff]/CutFXdB^3) (CC[dq[sp, ff, ii]].ProjP.FXd[sp, ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; op + HC[op]]"
    },
    {
      "name": "LSXuG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp, ii, jj, kk, ll, ss, aa, ffq, ffl, op}, op = ExpandIndices[(-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (I lamSXu[ffl, ffq]/CutSXu^2) SXu[ss] (CC[uq[sp, ffq, ii]].ProjP.Ga[mu].Ga[nu].l[sp, ffl]) FS[G, mu, nu, aa]]; op + HC[op]]"
    },
    {
      "name": "LSXdG",
      "delayed": true,
      "expression": "Block[{mu, nu, sp, ii, jj, kk, ll, ss, aa, ffq, ffl, op}, op = ExpandIndices[(-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (I lamSXd[ffl, ffq]/CutSXd^2) SXd[ss] (CC[dq[sp, ffq, ii]].ProjP.Ga[mu].Ga[nu].l[sp, ffl]) FS[G, mu, nu, aa]]; op + HC[op]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSXukin + LSXdkin + LFXukin + LFXdkin + LFXuG + LFXdG + LFXuB + LFXdB + LSXuG + LSXdG"
    }
  ]
}
```