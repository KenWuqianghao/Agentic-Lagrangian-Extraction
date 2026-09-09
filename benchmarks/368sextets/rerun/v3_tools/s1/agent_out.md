I have the paper, the schema, the renderer, and SM.fr. No cached or reference `.fr` file for this model exists in the sandbox and none was read.

## Physics extracted (arXiv:2110.11359, Section III + Table X)

Four new states, all colour sextets, all SU(2)_L singlets, no new gauge group:

| field | spin | SU(3)c | SU(2)L | Y = Q | L |
|---|---|---|---|---|---|
| Φ_u → `SXu` | S | 6 | 1 | 1/3 | −1 |
| Φ_d → `SXd` | S | 6 | 1 | 4/3 | −1 |
| Ψ_u → `FXu` | F | 6 | 1 | −2/3 | 0 |
| Ψ_d → `FXd` | F | 6 | 1 | 1/3 | 0 |

Clebsch-Gordan: the LaTeX Eq. (A18) plus its footnote give `Sqrt[2] L^{ijk} = Eps^{ijk}`, so
`J^{s ia} = -I Sqrt[2] L^{ijk} T[a,j,l] Kbar^{s}_{lk} = (-I) Eps[ii,jj,kk] T[aa,jj,ll] K6bar[ss,ll,kk]` — the `Sqrt[2]` cancels exactly. This is the paper's own stated FeynRules/MG5 strategy (build `J` from the hard-coded `K6`/`Eps` objects).

## Mandatory self-audit

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ power (=d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L sum | CC[] where ψ^c | fraction/root checked against | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LSXukin | `DC[SXubar]DC[SXu]`; `SXubar SXu` | 4; 2 | 1; `MSXu^2` | 0; 2 | n/a | −1/3+1/3=0 | 0 | singlet | 6bar⊗6 δ (implicit) | none | 0 | n/a | n/a | self-conj. pairing |
| LSXdkin | `DC[SXdbar]DC[SXd]`; `SXdbar SXd` | 4; 2 | 1; `MSXd^2` | 0; 2 | n/a | −4/3+4/3=0 | 0 | singlet | 6bar⊗6 δ | none | 0 | n/a | n/a | self-conj. pairing |
| LFXukin | `FXubar.Ga.DC[FXu]`; `FXubar.FXu` | 4; 3 | 1; `MFXu` | 0; 1 | n/a | 2/3−2/3=0 | 0 | singlet | 6bar⊗6 δ | none | 0 | n/a | n/a | self-conj. pairing |
| LFXdkin | `FXdbar.Ga.DC[FXd]`; `FXdbar.FXd` | 4; 3 | 1; `MFXd` | 0; 1 | n/a | −1/3+1/3=0 | 0 | singlet | 6bar⊗6 δ | none | 0 | n/a | n/a | self-conj. pairing |
| LFXuG | `CC[uRbar] σ FXu FS[G]` | 5 | `kapFXu/LamFXu` | −1 | `1/LamFXu^1` | +2/3−2/3+0=0 | +2/3−2/3=0 | all singlets | 3⊗6⊗8 via `Eps·T·K6bar` | none | 0+0=0 | yes | LaTeX Eq.(A18)+footnote: `Sqrt[2] L=Eps` ⇒ prefactor exactly `-I` | `HC[lag]` |
| LFXdG | `CC[dRbar] σ FXd FS[G]` | 5 | `kapFXd/LamFXd` | −1 | `1/LamFXd^1` | −1/3+1/3+0=0 | −1/3+1/3=0 | all singlets | same | none | 0 | yes | same | `HC[lag]` |
| LFXuB | `CC[uRbar] FXu FS[B] FS[G]` | 7 | `kapFXuB/LamFXuB^3` | −3 | `1/LamFXuB^3` | +2/3−2/3=0 | 0 | all singlets | same | none | 0 | yes | LaTeX Eq.(sFmodel) line 3: `1/Λ^3` literal | `HC[lag]` |
| LFXdB | `CC[dRbar] FXd FS[B] FS[G]` | 7 | `kapFXdB/LamFXdB^3` | −3 | `1/LamFXdB^3` | −1/3+1/3=0 | 0 | all singlets | same | none | 0 | yes | same | `HC[lag]` |
| LSXuG | `SXu CC[uRbar] σ lR FS[G]` | 6 | `lamSXu/LamSXu^2` | −2 | `1/LamSXu^2` | 1/3+2/3−1=0 | same | all singlets | same | none | −1+0+1=0 | yes | LaTeX Eq.(sSmodel): `1/Λ_Φ^2` literal | `HC[lag]` |
| LSXdG | `SXd CC[dRbar] σ lR FS[G]` | 6 | `lamSXd/LamSXd^2` | −2 | `1/LamSXd^2` | 4/3−1/3−1=0 | same | all singlets | same | none | −1+0+1=0 | yes | same | `HC[lag]` |
| class `SXu` | kinetic+mass `LSXukin` present, in `LTotal` | — | — | — | — | — | — | — | — | — | — | — | — | — |
| class `SXd` | kinetic+mass `LSXdkin` present, in `LTotal` | — | — | — | — | — | — | — | — | — | — | — | — | — |
| class `FXu` | kinetic+mass `LFXukin` present, in `LTotal` | — | — | — | — | — | — | — | — | — | — | — | — | — |
| class `FXd` | kinetic+mass `LFXdkin` present, in `LTotal` | — | — | — | — | — | — | — | — | — | — | — | — | — |
| colour rep `Sextet` | `AddGaugeRepresentation[SU3C -> {T6, Sextet}];` present in `raw_preamble`, together with `IndexRange[Index[Sextet]] = NoUnfold[Range[6]];`, and an `index_decls` entry is kept | — | — | — | — | — | — | — | — | — | — | — | — | — |

- `SelfConjugate -> True` classes: **none** (all four new fields are complex/Dirac), so no class carries forbidden `QuantumNumbers`.
- Names chosen: classes `SXu, SXd, FXu, FXd`; parameters `LamFXu, LamFXd, LamFXuB, LamFXdB, LamSXu, LamSXd, kapFXu, kapFXd, kapFXuB, kapFXdB, lamSXu, lamSXd, MSXu, MSXd, MFXu, MFXd, WSXu, WSXd, WFXu, WFXd`; index `Sextet` (style `sx`). None is a Mathematica built-in (`N, C, D, E, I, K, O`), a FeynRules symbol (`HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM`), or an SM.fr name (`H, Phi, Z, W, A, G, B, ee, gs, gw, g1, sw, cw, vev, lam, MZ, MW, uq, dq, l, vl, QL, uR, dR, LL, lR`). All class indices are ≥ 100.
- Single total: `LTotal` sums `LSXukin + LSXdkin + LFXukin + LFXdkin + LFXuG + LFXdG + LFXuB + LFXdB + LSXuG + LSXdG` — every other declared term appears exactly once, and no term is field-free.
- New U(1) charges: **n/a** — this model adds no new U(1); hypercharges are taken from Table X of the paper and re-derived above from SM.fr conventions (`uR` Y=+2/3, `dR` Y=−1/3, `lR` Y=−1), and they agree.
- Reference / cached model file read: **none**.

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
    "(* Colour sextet: new SU(3)c index and the sextet representation of SU3C. *)\nIndexRange[Index[Sextet]] = NoUnfold[Range[6]];\nAddGaugeRepresentation[SU3C -> {T6, Sextet}];"
  ],
  "index_decls": [
    {"name": "Sextet", "range_kind": "NoUnfold", "size": 6, "style_symbol": "sx"}
  ],
  "parameters": [
    {
      "name": "LamFXu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Psi_u [GeV] of the dimension-5 sextet-fermion operator, Eq. (sFmodel) line 2; paper benchmark 1 TeV"
    },
    {
      "name": "LamFXd",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 2,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Psi_d [GeV] of the dimension-5 sextet-fermion operator, Eq. (sFmodel) line 2; paper benchmark 1 TeV"
    },
    {
      "name": "LamFXuB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 3,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Psi_uB [GeV] of the dimension-7 operator, Eq. (sFmodel) line 3; paper benchmark 1 TeV"
    },
    {
      "name": "LamFXdB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 4,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Psi_dB [GeV] of the dimension-7 operator, Eq. (sFmodel) line 3; benchmark taken equal to the up-type one"
    },
    {
      "name": "LamSXu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 5,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Phi_u [GeV] of the dimension-6 sextet-scalar operator, Eq. (sSmodel); paper benchmark 1 TeV"
    },
    {
      "name": "LamSXd",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 6,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff Lambda_Phi_d [GeV] of the dimension-6 sextet-scalar operator, Eq. (sSmodel); paper benchmark 1 TeV"
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
      "complex": false,
      "block_name": "SXTKAPU",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa_u^I of Psi_u to up-type quark I and a gluon, Eq. (sFmodel); benchmark 0.05 (paper quotes 0.05 for I in 1,2; the quoted BF of Psi_u to top+gluon needs the same value for I=3)"
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
      "complex": false,
      "block_name": "SXTKAPD",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa_d^I of Psi_d to down-type quark I and a gluon, Eq. (sFmodel); benchmark 0.05"
    },
    {
      "name": "kapFXuB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapFXuB[1]", "rhs": "0.10"},
        {"lhs": "kapFXuB[2]", "rhs": "0.10"},
        {"lhs": "kapFXuB[3]", "rhs": "0.10"}
      ],
      "complex": false,
      "block_name": "SXTKAPUB",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa_uB^I of Psi_u to up-type quark I, a gluon and a hypercharge boson, Eq. (sFmodel) line 3; benchmark 0.10"
    },
    {
      "name": "kapFXdB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapFXdB[1]", "rhs": "0.10"},
        {"lhs": "kapFXdB[2]", "rhs": "0.10"},
        {"lhs": "kapFXdB[3]", "rhs": "0.10"}
      ],
      "complex": false,
      "block_name": "SXTKAPDB",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa_dB^I of Psi_d to down-type quark I, a gluon and a hypercharge boson, Eq. (sFmodel) line 3; benchmark 0.10"
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
      "complex": false,
      "block_name": "SXTLAMU",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling lambda_u^XI of Phi_u to lepton X, up-type quark I and a gluon, Eq. (sSmodel); benchmark 0.1 times the identity in generation space"
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
      "complex": false,
      "block_name": "SXTLAMD",
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling lambda_d^XI of Phi_d to lepton X, down-type quark I and a gluon, Eq. (sSmodel); benchmark 0.1 times the identity in generation space"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "SXu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"massless": false, "sym": "MSXu", "value": "1500."},
      "width": {"massless": false, "sym": "WSXu", "value": "1."},
      "quantum_numbers": {"Y": "1/3", "Q": "1/3", "LeptonNumber": "-1"},
      "pdg": 6000001,
      "particle_name": "sxu",
      "antiparticle_name": "sxu~",
      "full_name": "Colour-sextet scalar coupling to up-type quarks",
      "propagator_label": "SXu",
      "propagator_type": "D",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "SXd",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"massless": false, "sym": "MSXd", "value": "1500."},
      "width": {"massless": false, "sym": "WSXd", "value": "1."},
      "quantum_numbers": {"Y": "4/3", "Q": "4/3", "LeptonNumber": "-1"},
      "pdg": 6000002,
      "particle_name": "sxd",
      "antiparticle_name": "sxd~",
      "full_name": "Colour-sextet scalar coupling to down-type quarks",
      "propagator_label": "SXd",
      "propagator_type": "D",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "FXu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"massless": false, "sym": "MFXu", "value": "1500."},
      "width": {"massless": false, "sym": "WFXu", "value": "1."},
      "quantum_numbers": {"Y": "-2/3", "Q": "-2/3"},
      "pdg": 6000011,
      "particle_name": "fxu",
      "antiparticle_name": "fxu~",
      "full_name": "Colour-sextet Dirac fermion coupling to up-type quarks",
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
      "mass": {"massless": false, "sym": "MFXd", "value": "1500."},
      "width": {"massless": false, "sym": "WFXd", "value": "1."},
      "quantum_numbers": {"Y": "1/3", "Q": "1/3"},
      "pdg": 6000012,
      "particle_name": "fxd",
      "antiparticle_name": "fxd~",
      "full_name": "Colour-sextet Dirac fermion coupling to down-type quarks",
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
      "expression": "Block[{mu, nu, aa, ii, jj, kk, ll, ss, ff, lag}, lag = ExpandIndices[(-I) kapFXu[ff]/LamFXu Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (CC[uRbar[ff, ii]].(I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu])).FXu[ss]) FS[G, mu, nu, aa]]; lag + HC[lag]]"
    },
    {
      "name": "LFXdG",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, jj, kk, ll, ss, ff, lag}, lag = ExpandIndices[(-I) kapFXd[ff]/LamFXd Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (CC[dRbar[ff, ii]].(I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu])).FXd[ss]) FS[G, mu, nu, aa]]; lag + HC[lag]]"
    },
    {
      "name": "LFXuB",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, jj, kk, ll, ss, ff, lag}, lag = ExpandIndices[(-I) kapFXuB[ff]/LamFXuB^3 Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (CC[uRbar[ff, ii]].FXu[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; lag + HC[lag]]"
    },
    {
      "name": "LFXdB",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, jj, kk, ll, ss, ff, lag}, lag = ExpandIndices[(-I) kapFXdB[ff]/LamFXdB^3 Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (CC[dRbar[ff, ii]].FXd[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; lag + HC[lag]]"
    },
    {
      "name": "LSXuG",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, jj, kk, ll, ss, ff, xx, lag}, lag = ExpandIndices[(-I) lamSXu[xx, ff]/LamSXu^2 Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] SXu[ss] (CC[uRbar[ff, ii]].(I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu])).lR[xx]) FS[G, mu, nu, aa]]; lag + HC[lag]]"
    },
    {
      "name": "LSXdG",
      "delayed": true,
      "expression": "Block[{mu, nu, aa, ii, jj, kk, ll, ss, ff, xx, lag}, lag = ExpandIndices[(-I) lamSXd[xx, ff]/LamSXd^2 Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] SXd[ss] (CC[dRbar[ff, ii]].(I/2 (Ga[mu].Ga[nu] - Ga[nu].Ga[mu])).lR[xx]) FS[G, mu, nu, aa]]; lag + HC[lag]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSXukin + LSXdkin + LFXukin + LFXdkin + LFXuG + LFXdG + LFXuB + LFXdB + LSXuG + LSXdG"
    }
  ]
}
```