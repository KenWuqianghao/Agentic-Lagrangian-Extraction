I'll start by reading the paper and the schema.
I read the paper and the schema. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content found in the paper

Table X (plus Eqs. 12–13) fixes the complete new-physics field content: two color-sextet complex scalars **Φ_u (6,1,1/3)**, **Φ_d (6,1,4/3)** with L = −1, and two color-sextet Dirac fermions **Ψ_u (6,1,−2/3)**, **Ψ_d (6,1,1/3)** with L = 0. All are SU(2)_L singlets, so Q = Y.

Sign convention note: the paper writes the bilinear as `(q^c_R Γ X)`, which is `\bar{q^c_R} Γ X`. `\bar{q^c_R}` carries the *same* hypercharge as `q_R`. With SM.fr charges Y(uR)=2/3, Y(dR)=−1/3, Y(lR)=−1 this reproduces Table X exactly (Y(Ψ_u)=−2/3, Y(Ψ_d)=+1/3, Y(Φ_u)=+1/3, Y(Φ_d)=+4/3). I use SM.fr hypercharges unchanged; no new U(1) exists.

The color structure J^{sia} is not hard-coded in FeynRules. Appendix A, Eq. (A18) gives it from objects FeynRules already has: J^{sia} = −i ε^{ijk} [t^a]_j{}^l K̄^s_{lk}, using √2 L^{ijk} = ε^{ijk}. I write it verbatim as `-I Eps[ii,jj,kk] T[aa,jj,ll] K6bar[ss,ll,kk]`.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling symbol | coupling mass dim (=4−d) | 1/Λ power (=d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L sum | CC[] where paper writes ψ^c | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LPhiukin | DC[Φu†]DC[Φu]; MΦu² Φu†Φu | 4 (kin) / 2 (mass) | 1 / MPhiu² | 0 / 2 ✓ | n/a | 1/3−1/3=0 | 0 | all singlets | 6⊗6̄ singlet | none | −1+1=0 | n/a | self-conjugate (real) |
| LPhidkin | DC[Φd†]DC[Φd]; MΦd² Φd†Φd | 4 / 2 | 1 / MPhid² | 0 / 2 ✓ | n/a | 4/3−4/3=0 | 0 | singlets | 6⊗6̄ | none | 0 | n/a | self-conjugate |
| LPsiukin | i Ψ̄u γ^μ D_μ Ψu; MΨu Ψ̄uΨu | 4 / 3 | 1 / MPsiu | 0 / 1 ✓ | n/a | −(−2/3)+(−2/3)=0 | 0 | singlets | 6̄⊗6 | none | 0 | n/a | self-conjugate |
| LPsidkin | i Ψ̄d γ^μ D_μ Ψd; MΨd Ψ̄dΨd | 4 / 3 | 1 / MPsid | 0 / 1 ✓ | n/a | 0 | 0 | singlets | 6̄⊗6 | none | 0 | n/a | self-conjugate |
| LPsiuG | \bar{u_R^c} σ^{μν} Ψu G_{μν}^a | 5 | kapu[ff] (dimensionless) | 0 → needs 1/Λ¹ | 1/LamPsiu ✓ | +2/3−2/3+0=0 | +2/3−2/3=0 | singlet (no SU(2) fields) | J^{sia}: 3⊗6⊗8 → 1 | none | 0+0=0 | yes, `CC[uRbar]` | HC[lag] |
| LPsidG | \bar{d_R^c} σ^{μν} Ψd G_{μν}^a | 5 | kapd[ff] | 0 → 1/Λ¹ | 1/LamPsid ✓ | −1/3+1/3=0 | −1/3+1/3=0 | singlet | J^{sia} | none | 0 | yes | HC[lag] |
| LPsiuB | \bar{u_R^c} Ψu B_{μν} G^{μν a} | 7 | kapuB[ff] | 0 → 1/Λ³ | 1/LamPsiuB^3 ✓ | 0 | 0 | singlet | J^{sia} | none | 0 | yes | HC[lag] |
| LPsidB | \bar{d_R^c} Ψd B_{μν} G^{μν a} | 7 | kapdB[ff] | 0 → 1/Λ³ | 1/LamPsidB^3 ✓ | 0 | 0 | singlet | J^{sia} | none | 0 | yes | HC[lag] |
| LPhiuG | Φu \bar{u_R^c} σ^{μν} ℓ_R G_{μν}^a | 6 | lamu[xx,ff] | 0 → 1/Λ² | 1/LamPhiu^2 ✓ | 1/3+2/3−1=0 | 1/3+2/3−1=0 | singlet (lR is SU(2) singlet) | J^{sia} | none | −1+0+1=0 | yes | HC[lag] |
| LPhidG | Φd \bar{d_R^c} σ^{μν} ℓ_R G_{μν}^a | 6 | lamd[xx,ff] | 0 → 1/Λ² | 1/LamPhid^2 ✓ | 4/3−1/3−1=0 | 4/3−1/3−1=0 | singlet | J^{sia} | none | 0 | yes | HC[lag] |

Kinetic + mass confirmation, one row per new class: **Phiu** → `LPhiukin` ✓ in `LNP`; **Phid** → `LPhidkin` ✓; **Psiu** → `LPsiukin` ✓; **Psid** → `LPsidkin` ✓. All ten terms are summed in `LNP`, and `LSextet := LSM + LNP`.

`SelfConjugate -> True` classes: **none** — all four new fields are complex (distinct antiparticle), so no class carries a forbidden `QuantumNumbers` block.

Reference or cached model file read: **none**.

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
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "raw_preamble": [
    "(* SimpleExtensions add-on for SM.fr: color-sextet scalars and fermions,          *)\n(* arXiv:2110.11359 (Carpenter, Murphy, Tait), Eqs. (12), (13) and Table X.       *)\n(* The new fields carry Index[Sextet]; SM.fr's SU3C gauge group must include the  *)\n(* sextet representation {T6, Sextet} so that DC[] below builds the QCD gauge     *)\n(* interactions of Phiu, Phid, Psiu, Psid.                                        *)\n(* The Clebsch-Gordan coefficients J^{sia} of Table I are NOT hard-coded in       *)\n(* FeynRules. Per Eq. (A18) they are built from objects that are:                 *)\n(*   J[s,i,a] = -I Eps[i,j,k] T[a,j,l] K6bar[s,l,k],   using Sqrt[2] L^{ijk} = Eps[i,j,k]. *)"
  ],
  "index_decls": [
    {"name": "Sextet", "range_kind": "NoUnfold", "size": 6, "style_symbol": "s"}
  ],
  "parameters": [
    {
      "name": "LamPsiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Psi_u}",
      "description": "EFT cutoff [GeV] of the dimension-five up-type sextet fermion - quark - gluon operator, Eq.(12); benchmark 1 TeV"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 2,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Psi_d}",
      "description": "EFT cutoff [GeV] of the dimension-five down-type sextet fermion - quark - gluon operator, Eq.(12); benchmark 1 TeV"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 3,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Psi_u B}",
      "description": "EFT cutoff [GeV] of the dimension-seven up-type sextet fermion - quark - gluon - B operator, Eq.(12); benchmark 1 TeV"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 4,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Psi_d B}",
      "description": "EFT cutoff [GeV] of the dimension-seven down-type sextet fermion - quark - gluon - B operator, Eq.(12); benchmark 1 TeV"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 5,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Phi_u}",
      "description": "EFT cutoff [GeV] of the dimension-six up-type sextet scalar - quark - lepton - gluon operator, Eq.(13); benchmark 1 TeV"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 6,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Phi_d}",
      "description": "EFT cutoff [GeV] of the dimension-six down-type sextet scalar - quark - lepton - gluon operator, Eq.(13); benchmark 1 TeV"
    },
    {
      "name": "kapu",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "KAPPAU",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05"},
        {"lhs": "kapu[2]", "rhs": "0.05"},
        {"lhs": "kapu[3]", "rhs": "0.05"}
      ],
      "tex": "\\kappa^I_u",
      "description": "Dimensionless coupling of the sextet fermion Psiu to an up-type quark and a gluon, Eq.(12); benchmark 0.05 for every quark generation"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "KAPPAD",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05"},
        {"lhs": "kapd[2]", "rhs": "0.05"},
        {"lhs": "kapd[3]", "rhs": "0.05"}
      ],
      "tex": "\\kappa^I_d",
      "description": "Dimensionless coupling of the sextet fermion Psid to a down-type quark and a gluon, Eq.(12); benchmark 0.05 for every quark generation"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "KAPPAUB",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.10"},
        {"lhs": "kapuB[2]", "rhs": "0.10"},
        {"lhs": "kapuB[3]", "rhs": "0.10"}
      ],
      "tex": "\\kappa^I_{uB}",
      "description": "Dimensionless coupling of Psiu to an up-type quark, a gluon and the B boson, Eq.(12); benchmark 0.10 for every quark generation"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "KAPPADB",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.10"},
        {"lhs": "kapdB[2]", "rhs": "0.10"},
        {"lhs": "kapdB[3]", "rhs": "0.10"}
      ],
      "tex": "\\kappa^I_{dB}",
      "description": "Dimensionless coupling of Psid to a down-type quark, a gluon and the B boson, Eq.(12); benchmark 0.10 for every quark generation"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "LAMBDAU",
      "interaction_order": ["NP", 1],
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
      "tex": "\\lambda^{XI}_u",
      "description": "Dimensionless coupling of the sextet scalar Phiu to an up-type quark, a charged lepton and a gluon, Eq.(13); first index is the lepton generation X, second is the quark generation I; benchmark 0.1 times the identity"
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "LAMBDAD",
      "interaction_order": ["NP", 1],
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
      "tex": "\\lambda^{XI}_d",
      "description": "Dimensionless coupling of the sextet scalar Phid to a down-type quark, a charged lepton and a gluon, Eq.(13); first index is the lepton generation X, second is the quark generation I; benchmark 0.1 times the identity"
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
      "full_name": "Color-sextet scalar coupling to up-type quarks",
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
      "full_name": "Color-sextet scalar coupling to down-type quarks",
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
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3"},
      "pdg": 6000011,
      "particle_name": "psiu",
      "antiparticle_name": "psiu~",
      "full_name": "Color-sextet Dirac fermion coupling to up-type quarks",
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
      "quantum_numbers": {"Q": "1/3", "Y": "1/3"},
      "pdg": 6000012,
      "particle_name": "psid",
      "antiparticle_name": "psid~",
      "full_name": "Color-sextet Dirac fermion coupling to down-type quarks",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LPhiukin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phiubar[ss], mu] DC[Phiu[ss], mu] - MPhiu^2 Phiubar[ss] Phiu[ss]]]"
    },
    {
      "name": "LPhidkin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phidbar[ss], mu] DC[Phid[ss], mu] - MPhid^2 Phidbar[ss] Phid[ss]]]"
    },
    {
      "name": "LPsiukin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I Psiubar.Ga[mu].DC[Psiu, mu] - MPsiu Psiubar.Psiu]]"
    },
    {
      "name": "LPsidkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I Psidbar.Ga[mu].DC[Psid, mu] - MPsid Psidbar.Psid]]"
    },
    {
      "name": "LPsiuG",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(kapu[ff]/LamPsiu) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (I/2) (CC[uRbar[ff, ii]].Ga[mu].Ga[nu].Psiu[ss] - CC[uRbar[ff, ii]].Ga[nu].Ga[mu].Psiu[ss]) FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPsidG",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(kapd[ff]/LamPsid) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (I/2) (CC[dRbar[ff, ii]].Ga[mu].Ga[nu].Psid[ss] - CC[dRbar[ff, ii]].Ga[nu].Ga[mu].Psid[ss]) FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPsiuB",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(kapuB[ff]/LamPsiuB^3) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (CC[uRbar[ff, ii]].Psiu[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPsidB",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(kapdB[ff]/LamPsidB^3) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (CC[dRbar[ff, ii]].Psid[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPhiuG",
      "delayed": true,
      "expression": "Block[{mu, nu, xx, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(lamu[xx, ff]/LamPhiu^2) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] Phiu[ss] (I/2) (CC[uRbar[ff, ii]].Ga[mu].Ga[nu].lR[xx] - CC[uRbar[ff, ii]].Ga[nu].Ga[mu].lR[xx]) FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPhidG",
      "delayed": true,
      "expression": "Block[{mu, nu, xx, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(lamd[xx, ff]/LamPhid^2) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] Phid[ss] (I/2) (CC[dRbar[ff, ii]].Ga[mu].Ga[nu].lR[xx] - CC[dRbar[ff, ii]].Ga[nu].Ga[mu].lR[xx]) FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LPhiukin + LPhidkin + LPsiukin + LPsidkin + LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuG + LPhidG"
    },
    {
      "name": "LSextet",
      "delayed": true,
      "expression": "LSM + LNP"
    }
  ]
}
```
I read the paper and the schema. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content found in the paper

Table X (plus Eqs. 12–13) fixes the complete new-physics field content: two color-sextet complex scalars **Φ_u (6,1,1/3)**, **Φ_d (6,1,4/3)** with L = −1, and two color-sextet Dirac fermions **Ψ_u (6,1,−2/3)**, **Ψ_d (6,1,1/3)** with L = 0. All are SU(2)_L singlets, so Q = Y.

Sign convention note: the paper writes the bilinear as `(q^c_R Γ X)`, which is `\bar{q^c_R} Γ X`. `\bar{q^c_R}` carries the *same* hypercharge as `q_R`. With SM.fr charges Y(uR)=2/3, Y(dR)=−1/3, Y(lR)=−1 this reproduces Table X exactly (Y(Ψ_u)=−2/3, Y(Ψ_d)=+1/3, Y(Φ_u)=+1/3, Y(Φ_d)=+4/3). I use SM.fr hypercharges unchanged; no new U(1) exists.

The color structure J^{sia} is not hard-coded in FeynRules. Appendix A, Eq. (A18) gives it from objects FeynRules already has: J^{sia} = −i ε^{ijk} [t^a]_j{}^l K̄^s_{lk}, using √2 L^{ijk} = ε^{ijk}. I write it verbatim as `-I Eps[ii,jj,kk] T[aa,jj,ll] K6bar[ss,ll,kk]`.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling symbol | coupling mass dim (=4−d) | 1/Λ power (=d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L sum | CC[] where paper writes ψ^c | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LPhiukin | DC[Φu†]DC[Φu]; MΦu² Φu†Φu | 4 (kin) / 2 (mass) | 1 / MPhiu² | 0 / 2 ✓ | n/a | 1/3−1/3=0 | 0 | all singlets | 6⊗6̄ singlet | none | −1+1=0 | n/a | self-conjugate (real) |
| LPhidkin | DC[Φd†]DC[Φd]; MΦd² Φd†Φd | 4 / 2 | 1 / MPhid² | 0 / 2 ✓ | n/a | 4/3−4/3=0 | 0 | singlets | 6⊗6̄ | none | 0 | n/a | self-conjugate |
| LPsiukin | i Ψ̄u γ^μ D_μ Ψu; MΨu Ψ̄uΨu | 4 / 3 | 1 / MPsiu | 0 / 1 ✓ | n/a | −(−2/3)+(−2/3)=0 | 0 | singlets | 6̄⊗6 | none | 0 | n/a | self-conjugate |
| LPsidkin | i Ψ̄d γ^μ D_μ Ψd; MΨd Ψ̄dΨd | 4 / 3 | 1 / MPsid | 0 / 1 ✓ | n/a | 0 | 0 | singlets | 6̄⊗6 | none | 0 | n/a | self-conjugate |
| LPsiuG | \bar{u_R^c} σ^{μν} Ψu G_{μν}^a | 5 | kapu[ff] (dimensionless) | 0 → needs 1/Λ¹ | 1/LamPsiu ✓ | +2/3−2/3+0=0 | +2/3−2/3=0 | singlet (no SU(2) fields) | J^{sia}: 3⊗6⊗8 → 1 | none | 0+0=0 | yes, `CC[uRbar]` | HC[lag] |
| LPsidG | \bar{d_R^c} σ^{μν} Ψd G_{μν}^a | 5 | kapd[ff] | 0 → 1/Λ¹ | 1/LamPsid ✓ | −1/3+1/3=0 | −1/3+1/3=0 | singlet | J^{sia} | none | 0 | yes | HC[lag] |
| LPsiuB | \bar{u_R^c} Ψu B_{μν} G^{μν a} | 7 | kapuB[ff] | 0 → 1/Λ³ | 1/LamPsiuB^3 ✓ | 0 | 0 | singlet | J^{sia} | none | 0 | yes | HC[lag] |
| LPsidB | \bar{d_R^c} Ψd B_{μν} G^{μν a} | 7 | kapdB[ff] | 0 → 1/Λ³ | 1/LamPsidB^3 ✓ | 0 | 0 | singlet | J^{sia} | none | 0 | yes | HC[lag] |
| LPhiuG | Φu \bar{u_R^c} σ^{μν} ℓ_R G_{μν}^a | 6 | lamu[xx,ff] | 0 → 1/Λ² | 1/LamPhiu^2 ✓ | 1/3+2/3−1=0 | 1/3+2/3−1=0 | singlet (lR is SU(2) singlet) | J^{sia} | none | −1+0+1=0 | yes | HC[lag] |
| LPhidG | Φd \bar{d_R^c} σ^{μν} ℓ_R G_{μν}^a | 6 | lamd[xx,ff] | 0 → 1/Λ² | 1/LamPhid^2 ✓ | 4/3−1/3−1=0 | 4/3−1/3−1=0 | singlet | J^{sia} | none | 0 | yes | HC[lag] |

Kinetic + mass confirmation, one row per new class: **Phiu** → `LPhiukin` ✓ in `LNP`; **Phid** → `LPhidkin` ✓; **Psiu** → `LPsiukin` ✓; **Psid** → `LPsidkin` ✓. All ten terms are summed in `LNP`, and `LSextet := LSM + LNP`.

`SelfConjugate -> True` classes: **none** — all four new fields are complex (distinct antiparticle), so no class carries a forbidden `QuantumNumbers` block.

Reference or cached model file read: **none**.

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
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "raw_preamble": [
    "(* SimpleExtensions add-on for SM.fr: color-sextet scalars and fermions,          *)\n(* arXiv:2110.11359 (Carpenter, Murphy, Tait), Eqs. (12), (13) and Table X.       *)\n(* The new fields carry Index[Sextet]; SM.fr's SU3C gauge group must include the  *)\n(* sextet representation {T6, Sextet} so that DC[] below builds the QCD gauge     *)\n(* interactions of Phiu, Phid, Psiu, Psid.                                        *)\n(* The Clebsch-Gordan coefficients J^{sia} of Table I are NOT hard-coded in       *)\n(* FeynRules. Per Eq. (A18) they are built from objects that are:                 *)\n(*   J[s,i,a] = -I Eps[i,j,k] T[a,j,l] K6bar[s,l,k],   using Sqrt[2] L^{ijk} = Eps[i,j,k]. *)"
  ],
  "index_decls": [
    {"name": "Sextet", "range_kind": "NoUnfold", "size": 6, "style_symbol": "s"}
  ],
  "parameters": [
    {
      "name": "LamPsiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Psi_u}",
      "description": "EFT cutoff [GeV] of the dimension-five up-type sextet fermion - quark - gluon operator, Eq.(12); benchmark 1 TeV"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 2,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Psi_d}",
      "description": "EFT cutoff [GeV] of the dimension-five down-type sextet fermion - quark - gluon operator, Eq.(12); benchmark 1 TeV"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 3,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Psi_u B}",
      "description": "EFT cutoff [GeV] of the dimension-seven up-type sextet fermion - quark - gluon - B operator, Eq.(12); benchmark 1 TeV"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 4,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Psi_d B}",
      "description": "EFT cutoff [GeV] of the dimension-seven down-type sextet fermion - quark - gluon - B operator, Eq.(12); benchmark 1 TeV"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 5,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Phi_u}",
      "description": "EFT cutoff [GeV] of the dimension-six up-type sextet scalar - quark - lepton - gluon operator, Eq.(13); benchmark 1 TeV"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 6,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda_{\\Phi_d}",
      "description": "EFT cutoff [GeV] of the dimension-six down-type sextet scalar - quark - lepton - gluon operator, Eq.(13); benchmark 1 TeV"
    },
    {
      "name": "kapu",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "KAPPAU",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05"},
        {"lhs": "kapu[2]", "rhs": "0.05"},
        {"lhs": "kapu[3]", "rhs": "0.05"}
      ],
      "tex": "\\kappa^I_u",
      "description": "Dimensionless coupling of the sextet fermion Psiu to an up-type quark and a gluon, Eq.(12); benchmark 0.05 for every quark generation"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "KAPPAD",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05"},
        {"lhs": "kapd[2]", "rhs": "0.05"},
        {"lhs": "kapd[3]", "rhs": "0.05"}
      ],
      "tex": "\\kappa^I_d",
      "description": "Dimensionless coupling of the sextet fermion Psid to a down-type quark and a gluon, Eq.(12); benchmark 0.05 for every quark generation"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "KAPPAUB",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.10"},
        {"lhs": "kapuB[2]", "rhs": "0.10"},
        {"lhs": "kapuB[3]", "rhs": "0.10"}
      ],
      "tex": "\\kappa^I_{uB}",
      "description": "Dimensionless coupling of Psiu to an up-type quark, a gluon and the B boson, Eq.(12); benchmark 0.10 for every quark generation"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "indices": ["Generation"],
      "block_name": "KAPPADB",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.10"},
        {"lhs": "kapdB[2]", "rhs": "0.10"},
        {"lhs": "kapdB[3]", "rhs": "0.10"}
      ],
      "tex": "\\kappa^I_{dB}",
      "description": "Dimensionless coupling of Psid to a down-type quark, a gluon and the B boson, Eq.(12); benchmark 0.10 for every quark generation"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "LAMBDAU",
      "interaction_order": ["NP", 1],
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
      "tex": "\\lambda^{XI}_u",
      "description": "Dimensionless coupling of the sextet scalar Phiu to an up-type quark, a charged lepton and a gluon, Eq.(13); first index is the lepton generation X, second is the quark generation I; benchmark 0.1 times the identity"
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "LAMBDAD",
      "interaction_order": ["NP", 1],
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
      "tex": "\\lambda^{XI}_d",
      "description": "Dimensionless coupling of the sextet scalar Phid to a down-type quark, a charged lepton and a gluon, Eq.(13); first index is the lepton generation X, second is the quark generation I; benchmark 0.1 times the identity"
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
      "full_name": "Color-sextet scalar coupling to up-type quarks",
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
      "full_name": "Color-sextet scalar coupling to down-type quarks",
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
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3"},
      "pdg": 6000011,
      "particle_name": "psiu",
      "antiparticle_name": "psiu~",
      "full_name": "Color-sextet Dirac fermion coupling to up-type quarks",
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
      "quantum_numbers": {"Q": "1/3", "Y": "1/3"},
      "pdg": 6000012,
      "particle_name": "psid",
      "antiparticle_name": "psid~",
      "full_name": "Color-sextet Dirac fermion coupling to down-type quarks",
      "propagator_label": "Psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LPhiukin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phiubar[ss], mu] DC[Phiu[ss], mu] - MPhiu^2 Phiubar[ss] Phiu[ss]]]"
    },
    {
      "name": "LPhidkin",
      "delayed": true,
      "expression": "Block[{mu, ss}, ExpandIndices[DC[Phidbar[ss], mu] DC[Phid[ss], mu] - MPhid^2 Phidbar[ss] Phid[ss]]]"
    },
    {
      "name": "LPsiukin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I Psiubar.Ga[mu].DC[Psiu, mu] - MPsiu Psiubar.Psiu]]"
    },
    {
      "name": "LPsidkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I Psidbar.Ga[mu].DC[Psid, mu] - MPsid Psidbar.Psid]]"
    },
    {
      "name": "LPsiuG",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(kapu[ff]/LamPsiu) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (I/2) (CC[uRbar[ff, ii]].Ga[mu].Ga[nu].Psiu[ss] - CC[uRbar[ff, ii]].Ga[nu].Ga[mu].Psiu[ss]) FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPsidG",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(kapd[ff]/LamPsid) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (I/2) (CC[dRbar[ff, ii]].Ga[mu].Ga[nu].Psid[ss] - CC[dRbar[ff, ii]].Ga[nu].Ga[mu].Psid[ss]) FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPsiuB",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(kapuB[ff]/LamPsiuB^3) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (CC[uRbar[ff, ii]].Psiu[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPsidB",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(kapdB[ff]/LamPsidB^3) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] (CC[dRbar[ff, ii]].Psid[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPhiuG",
      "delayed": true,
      "expression": "Block[{mu, nu, xx, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(lamu[xx, ff]/LamPhiu^2) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] Phiu[ss] (I/2) (CC[uRbar[ff, ii]].Ga[mu].Ga[nu].lR[xx] - CC[uRbar[ff, ii]].Ga[nu].Ga[mu].lR[xx]) FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LPhidG",
      "delayed": true,
      "expression": "Block[{mu, nu, xx, ff, ii, jj, kk, ll, aa, ss}, Module[{lag}, lag = ExpandIndices[(lamd[xx, ff]/LamPhid^2) (-I) Eps[ii, jj, kk] T[aa, jj, ll] K6bar[ss, ll, kk] Phid[ss] (I/2) (CC[dRbar[ff, ii]].Ga[mu].Ga[nu].lR[xx] - CC[dRbar[ff, ii]].Ga[nu].Ga[mu].lR[xx]) FS[G, mu, nu, aa]]; lag + HC[lag]]]"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LPhiukin + LPhidkin + LPsiukin + LPsidkin + LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuG + LPhidG"
    },
    {
      "name": "LSextet",
      "delayed": true,
      "expression": "LSM + LNP"
    }
  ]
}
```