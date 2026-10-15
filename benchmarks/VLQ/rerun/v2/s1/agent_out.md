I'll start by reading the paper and the schema.
I've read the paper, the schema, the renderer, and SM.fr. No reference or cached `.fr` model file for this model exists in the sandbox, and none was read.

## Physics content extracted from arXiv:hep-ph/0607115

The paper gives **two** minimal SM extensions that relax 3×3 CKM unitarity:

1. **Vector-like Q = +2/3 iso-singlet quark t′** (Sec. 2.1): new parameters = the t−t′ mixing angle θ (Eqs. 5, 8–10) and m_t′ (Eq. 12). New interactions: 4×3 charged current (Eq. 7), tree-level FCNC Z (Eq. 14) and Higgs (Eq. 15) with VV† of Eq. (16).
2. **Vector-like down-type b′** (Sec. 2.1, Eq. 17): mixing angle θ_d, sin θ_d ≲ 0.06.
3. **Fourth generation** (Sec. 2.2): t′ and b′ with a 4×4 unitary CKM parametrised by θ_u, θ_v, θ_w (Eqs. 31–35), plus the fourth-generation leptons required by anomaly cancellation (end of Sec. 2.2.1).

## Mandatory self-audit table

Field mass dimensions: fermion 3/2, scalar 1, vector 1, `del`/`DC` 1. All new-physics operators here have d ≤ 4, so no EFT cutoff is needed anywhere (rule 2 does not apply: the paper contains no 1/Λⁿ operator).

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L/B number | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LTPkin (kin) | `tpLbar Ga DC[tpL]`, `tpRbar Ga DC[tpR]` | 4 | none (gauge coupling inside `DC`) | 0 ✓ | n/a | −2/3+2/3=0 ✓ | −2/3+2/3=0 ✓ | singlet (no SU2D index) | `tpLbar[cc] … tpL[cc]` shared Colour | none | B: −1/3+1/3=0 | n/a | self-conjugate |
| LTPkin (mass) | `MTP tpbar.tp` | 3 | MTP | 1 ✓ | n/a | 0 ✓ | −2/3+2/3=0 ✓ (vector-like ⇒ bare Dirac mass invariant, Eq. 12) | singlet | shared Colour | none | 0 | n/a | self-conjugate |
| LBPkin (kin) | `bpLbar Ga DC[bpL]`, `bpRbar Ga DC[bpR]` | 4 | none | 0 ✓ | n/a | +1/3−1/3=0 ✓ | +1/3−1/3=0 ✓ | singlet | shared Colour | none | 0 | n/a | self-conjugate |
| LBPkin (mass) | `MBP bpbar.bp` | 3 | MBP | 1 ✓ | n/a | 0 ✓ | 0 ✓ (vector-like) | singlet | shared Colour | none | 0 | n/a | self-conjugate |
| LL4kin | `LL4bar Ga DC[LL4]`, `lR4bar Ga DC[lR4]`, `vR4bar Ga DC[vR4]` | 4 | none | 0 ✓ | n/a | 0 ✓ | +1/2−1/2=0; +1−1=0; 0+0=0 ✓ | doublet·anti-doublet on shared `SU2D` index | colour singlet | none | L: −1+1=0 | n/a | self-conjugate |
| LY4 (charged) | `yl4 LL4bar[sp,ii].lR4[sp] Phi[ii]` | 4 | yl4 | 0 ✓ | n/a | 0−1+1=0 ✓ | +1/2−1+1/2=0 ✓ | `LL4bar[ii]` with `Phi[ii]`, shared index ✓ | singlet | none | 0 | n/a | `HC[...]` |
| LY4 (neutral) | `yv4 LL4bar[sp,ii].vR4[sp] Phibar[jj] Eps[ii,jj]` | 4 | yv4 | 0 ✓ | n/a | 0+0+0=0 ✓ | +1/2+0−1/2=0 ✓ | same conjugation type ⇒ `Eps[ii,jj]` on two distinct indices ✓ | singlet | none | 0 | n/a | `HC[...]` |
| LCCtp | `gw CKM[3,ff] tpbar Ga ProjM dq W`, `+ (Cos[th]−1)` top piece | 4 | gw Sin[th] / gw (Cos[th]−1) | 0 ✓ | n/a | −2/3−1/3+1=0 ✓ | mass basis after EWSB — see note below | rotation of the SU(2)-invariant Eq. (11)/(12) Lagrangian | `tpbar[cc] … dq[cc]` shared Colour | none | B: −1/3+1/3=0 | n/a | `HC[...]` |
| LNCtp | `gw uqbar Ga ProjM tp Z`, `tpbar … uq Z`, diagonal pieces | 4 | gw SinCos[th], gw(Cos²−1), gw Sin² | 0 ✓ | n/a | −2/3+2/3+0=0 ✓ | mass basis (Eq. 14) | descends from Eq. (16) VV† | shared Colour | none | 0 | n/a | Hermitian by construction (the two FCNC pieces are mutual conjugates) |
| LHtp | `gw/(2 MW) MTP uqbar ProjP tp H` and partners | 4 | gw MTP/(2 MW) (dimensionless) | 0 ✓ | n/a | −2/3+2/3+0=0 ✓ | mass basis (Eq. 15) | — | shared Colour | none | 0 | n/a | `HC[...]` |
| LCCbp | `gw CKM[ff,3] uqbar Ga ProjM bp W`, `+ (Cos[thd]−1)` b piece | 4 | gw Sin[thd] | 0 ✓ | n/a | −2/3−1/3+1=0 ✓ | mass basis (Eq. 17 model) | — | shared Colour | none | 0 | n/a | `HC[...]` |
| LNCbp | `gw dqbar Ga ProjM bp Z` + diagonal pieces | 4 | gw SinCos[thd] | 0 ✓ | n/a | +1/3−1/3+0=0 ✓ | mass basis | — | shared Colour | none | 0 | n/a | Hermitian by construction |
| LHbp | `gw/(2 MW) MBP dqbar ProjP bp H` and partners | 4 | gw MBP/(2 MW) | 0 ✓ | n/a | +1/3−1/3+0=0 ✓ | mass basis | — | shared Colour | none | 0 | n/a | `HC[...]` |
| LCC4 | `gw CKM4[4,j] tpbar Ga ProjM dq W`, `gw CKM4[i,4] uqbar Ga ProjM bp W`, `gw CKM4[4,4] tpbar Ga ProjM bp W` | 4 | gw CKM4[i,j] | 0 ✓ | n/a | −2/3−1/3+1=0 ✓ (every monomial) | mass basis (Eqs. 31–35) | — | shared Colour | none | B: 0 | n/a | `HC[...]` |

Kinetic + mass confirmation, one row per new class (all are in the total sum `LNP`, and `LGen4` for the fourth-generation option):

| class | kinetic term | mass term | in total sum |
|---|---|---|---|
| F[5] tp | LTPkin (via `tpL`,`tpR`, `DC`) | `− MTP tpbar.tp` in LTPkin, symbol `MTP` from `Mass -> {MTP, 500.}` | yes |
| F[6] bp | LBPkin | `− MBP bpbar.bp`, symbol `MBP` | yes |
| F[7] lp | LL4kin (via `LL4`,`lR4`) | LY4, `yl4 = Sqrt[2] MLP/vev`, symbol `MLP` | yes |
| F[8] vp | LL4kin (via `LL4`,`vR4`) | LY4, `yv4 = Sqrt[2] MVP/vev`, symbol `MVP` | yes |

Notes required by the rules:
- **Y sums in mass-basis terms**: LCCtp, LNCtp, LHtp, LCCbp, LNCbp, LHbp and LCC4 are written with physical (post-EWSB) fields, exactly as the paper writes Eqs. (7), (14), (15). Hypercharge is not a symmetry of a broken-phase monomial; these terms are the rotation (Eqs. 8–10, 16, 31–35) of the manifestly SU(2)×U(1)-invariant gauge-basis Lagrangian of Eqs. (11)–(12), so only the electric charge sum must vanish, and it does in every monomial. All terms written in the unbroken basis (LTPkin, LBPkin, LL4kin, LY4) have Y sum 0.
- **SelfConjugate -> True classes**: none. All eleven new classes are complex Dirac/chiral fields with `self_conjugate = false`, so no quantum number sits on a self-conjugate class.
- **Charge conjugation**: the paper writes no `psi^c`, no `psi^T C`, and no Majorana state, so `CC[...]` is not used anywhere ("n/a" in every row).
- **Reference/cached model file read: none.**

```json
{
  "model_name": "VLQ_gen",
  "info": {
    "authors": [
      "J. Alwall",
      "R. Frederix",
      "J.-M. Gerard",
      "A. Giammanco",
      "M. Herquet",
      "S. Kalinin",
      "E. Kou",
      "V. Lemaitre",
      "F. Maltoni"
    ],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": [
      "Centre for Particle Physics and Phenomenology (CP3), Universite catholique de Louvain"
    ],
    "emails": []
  },
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Gen4",
      "range_kind": "NoUnfold",
      "size": 4,
      "style_symbol": "g4"
    }
  ],
  "parameters": [
    {
      "name": "th",
      "parameter_type": "External",
      "value": "0.78",
      "block_name": "VLQMIX",
      "order_block": 1,
      "tex": "\\theta",
      "description": "t - t' mixing angle theta of the vector-like model, Eqs.(5),(8)-(10): Vti = V0ti Cos[th], Vt'i = V0ti Sin[th]. Benchmark of Figs.1,8: Cos[th] = 0.71. Rb gives |Cos[th]| > 0.91, Eq.(30)."
    },
    {
      "name": "thd",
      "parameter_type": "External",
      "value": "0.06",
      "block_name": "VLQMIX",
      "order_block": 2,
      "tex": "\\theta_d",
      "description": "b - b' mixing angle theta_d of the down-type vector-like model, Sec.2.1: Vtb = V0tb Cos[thd]. Rb constrains Sin[thd] < 0.06, Eq.(17)."
    },
    {
      "name": "thu",
      "parameter_type": "External",
      "value": "0.37",
      "block_name": "GEN4MIX",
      "order_block": 1,
      "tex": "\\theta_u",
      "description": "Fourth-generation 3-4 mixing angle theta_u of V4x4 = R34(thu) R24(thv) R14(thw), Eq.(31). Rb gives |Cos[thu]| > 0.93, Eq.(42)."
    },
    {
      "name": "thv",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "GEN4MIX",
      "order_block": 2,
      "tex": "\\theta_v",
      "description": "Fourth-generation 2-4 mixing angle theta_v, Eq.(31). Unitarity gives |thv| <= O(lambda) ~ 0.2, Eq.(36); thv = 0.2 is excluded, thv = 0.1 is allowed (Fig.4)."
    },
    {
      "name": "thw",
      "parameter_type": "External",
      "value": "0.05",
      "block_name": "GEN4MIX",
      "order_block": 3,
      "tex": "\\theta_w",
      "description": "Fourth-generation 1-4 mixing angle theta_w, Eq.(31). Unitarity gives |thw| <= O(lambda^2) ~ 0.05, Eq.(36)."
    },
    {
      "name": "CKM4",
      "parameter_type": "Internal",
      "indices": ["Gen4", "Gen4"],
      "value_rules": [
        {"lhs": "CKM4[1,1]", "rhs": "Cos[thw] CKM[1,1]"},
        {"lhs": "CKM4[1,2]", "rhs": "Cos[thw] CKM[1,2]"},
        {"lhs": "CKM4[1,3]", "rhs": "Cos[thw] CKM[1,3]"},
        {"lhs": "CKM4[1,4]", "rhs": "-Sin[thw]"},
        {"lhs": "CKM4[2,1]", "rhs": "Cos[thv] CKM[2,1] - Sin[thv] Sin[thw] CKM[1,1]"},
        {"lhs": "CKM4[2,2]", "rhs": "Cos[thv] CKM[2,2] - Sin[thv] Sin[thw] CKM[1,2]"},
        {"lhs": "CKM4[2,3]", "rhs": "Cos[thv] CKM[2,3] - Sin[thv] Sin[thw] CKM[1,3]"},
        {"lhs": "CKM4[2,4]", "rhs": "-Sin[thv] Cos[thw]"},
        {"lhs": "CKM4[3,1]", "rhs": "Cos[thu] CKM[3,1] - Sin[thu] Sin[thv] CKM[2,1] - Sin[thu] Cos[thv] Sin[thw] CKM[1,1]"},
        {"lhs": "CKM4[3,2]", "rhs": "Cos[thu] CKM[3,2] - Sin[thu] Sin[thv] CKM[2,2] - Sin[thu] Cos[thv] Sin[thw] CKM[1,2]"},
        {"lhs": "CKM4[3,3]", "rhs": "Cos[thu] CKM[3,3] - Sin[thu] Sin[thv] CKM[2,3] - Sin[thu] Cos[thv] Sin[thw] CKM[1,3]"},
        {"lhs": "CKM4[3,4]", "rhs": "-Sin[thu] Cos[thv] Cos[thw]"},
        {"lhs": "CKM4[4,1]", "rhs": "Sin[thu] CKM[3,1] + Cos[thu] Sin[thv] CKM[2,1] + Cos[thu] Cos[thv] Sin[thw] CKM[1,1]"},
        {"lhs": "CKM4[4,2]", "rhs": "Sin[thu] CKM[3,2] + Cos[thu] Sin[thv] CKM[2,2] + Cos[thu] Cos[thv] Sin[thw] CKM[1,2]"},
        {"lhs": "CKM4[4,3]", "rhs": "Sin[thu] CKM[3,3] + Cos[thu] Sin[thv] CKM[2,3] + Cos[thu] Cos[thv] Sin[thw] CKM[1,3]"},
        {"lhs": "CKM4[4,4]", "rhs": "Cos[thu] Cos[thv] Cos[thw]"}
      ],
      "tex": "V^{4x4}",
      "description": "4x4 unitary quark mixing matrix of the fourth-generation model, Eqs.(31)-(35); row/column 4 belong to t' and b'. Built on the SM 3x3 CKM of SM.fr."
    },
    {
      "name": "yl4",
      "parameter_type": "Internal",
      "value": "Sqrt[2] MLP/vev",
      "interaction_order": ["QED", 1],
      "tex": "y_{l4}",
      "description": "Yukawa coupling of the fourth-generation charged lepton; fixes its mass MLP (Sec.2.2.1, anomaly cancellation needs a fourth lepton generation)."
    },
    {
      "name": "yv4",
      "parameter_type": "Internal",
      "value": "Sqrt[2] MVP/vev",
      "interaction_order": ["QED", 1],
      "tex": "y_{v4}",
      "description": "Yukawa coupling of the fourth-generation Dirac neutrino; fixes its mass MVP (Sec.2.2.1)."
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 5,
      "class_name": "tp",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MTP", "value": "500."},
      "width": {"sym": "WTP", "value": "10."},
      "quantum_numbers": {"Q": "2/3"},
      "pdg": 8,
      "particle_name": "tp",
      "antiparticle_name": "tp~",
      "full_name": "t-prime quark",
      "propagator_label": "tp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 6,
      "class_name": "bp",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MBP", "value": "500."},
      "width": {"sym": "WBP", "value": "10."},
      "quantum_numbers": {"Q": "-1/3"},
      "pdg": 7,
      "particle_name": "bp",
      "antiparticle_name": "bp~",
      "full_name": "b-prime quark",
      "propagator_label": "bp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 7,
      "class_name": "lp",
      "self_conjugate": false,
      "mass": {"sym": "MLP", "value": "300."},
      "width": {"sym": "WLP", "value": "1."},
      "quantum_numbers": {"Q": "-1", "LeptonNumber": "1"},
      "pdg": 17,
      "particle_name": "l4-",
      "antiparticle_name": "l4+",
      "full_name": "Fourth-generation charged lepton",
      "propagator_label": "l4",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 8,
      "class_name": "vp",
      "self_conjugate": false,
      "mass": {"sym": "MVP", "value": "150."},
      "width": {"sym": "WVP", "value": "1."},
      "quantum_numbers": {"Q": "0", "LeptonNumber": "1"},
      "pdg": 18,
      "particle_name": "v4",
      "antiparticle_name": "v4~",
      "full_name": "Fourth-generation Dirac neutrino",
      "propagator_label": "v4",
      "propagator_type": "S",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 16,
      "class_name": "tpL",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "2/3"},
      "unphysical": true,
      "definitions": [
        "tpL[sp1_, cc_] :> Module[{sp2}, ProjM[sp1, sp2] tp[sp2, cc]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 17,
      "class_name": "tpR",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "2/3"},
      "unphysical": true,
      "definitions": [
        "tpR[sp1_, cc_] :> Module[{sp2}, ProjP[sp1, sp2] tp[sp2, cc]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 18,
      "class_name": "bpL",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "-1/3"},
      "unphysical": true,
      "definitions": [
        "bpL[sp1_, cc_] :> Module[{sp2}, ProjM[sp1, sp2] bp[sp2, cc]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 19,
      "class_name": "bpR",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "-1/3"},
      "unphysical": true,
      "definitions": [
        "bpR[sp1_, cc_] :> Module[{sp2}, ProjP[sp1, sp2] bp[sp2, cc]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 20,
      "class_name": "LL4",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "-1/2"},
      "unphysical": true,
      "definitions": [
        "LL4[sp1_, 1] :> Module[{sp2}, ProjM[sp1, sp2] vp[sp2]]",
        "LL4[sp1_, 2] :> Module[{sp2}, ProjM[sp1, sp2] lp[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 21,
      "class_name": "lR4",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "-1"},
      "unphysical": true,
      "definitions": [
        "lR4[sp1_] :> Module[{sp2}, ProjP[sp1, sp2] lp[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 22,
      "class_name": "vR4",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "0"},
      "unphysical": true,
      "definitions": [
        "vR4[sp1_] :> Module[{sp2}, ProjP[sp1, sp2] vp[sp2]]"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LTPkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I tpLbar.Ga[mu].DC[tpL, mu] + I tpRbar.Ga[mu].DC[tpR, mu] - MTP tpbar.tp]]"
    },
    {
      "name": "LBPkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I bpLbar.Ga[mu].DC[bpL, mu] + I bpRbar.Ga[mu].DC[bpR, mu] - MBP bpbar.bp]]"
    },
    {
      "name": "LL4kin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I LL4bar.Ga[mu].DC[LL4, mu] + I lR4bar.Ga[mu].DC[lR4, mu] + I vR4bar.Ga[mu].DC[vR4, mu], FlavorExpand -> {SU2W, SU2D}]]"
    },
    {
      "name": "LY4",
      "delayed": true,
      "expression": "Block[{sp1, ii, jj, yuk}, yuk = -yl4 LL4bar[sp1, ii].lR4[sp1] Phi[ii] - yv4 LL4bar[sp1, ii].vR4[sp1] Phibar[jj] Eps[ii, jj]; ExpandIndices[yuk + HC[yuk], FlavorExpand -> SU2D]]"
    },
    {
      "name": "LCCtp",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, ff, cc, cc1}, cc1 = -gw/Sqrt[2] CKM[3, ff] (Sin[th] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, ff, cc] + (Cos[th] - 1) uqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, ff, cc]) W[mu]; ExpandIndices[cc1 + HC[cc1], FlavorExpand -> Generation]]"
    },
    {
      "name": "LNCtp",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, cc}, ExpandIndices[-gw/(2 cw) (Sin[th] Cos[th] (uqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].tp[sp3, cc] + tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].uq[sp3, 3, cc]) + (Cos[th]^2 - 1) uqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].uq[sp3, 3, cc] + Sin[th]^2 tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].tp[sp3, cc]) Z[mu]]]"
    },
    {
      "name": "LHtp",
      "delayed": true,
      "expression": "Block[{sp1, sp2, cc, hh}, hh = -gw/(2 MW) (Sin[th] Cos[th] (MTP uqbar[sp1, 3, cc].ProjP[sp1, sp2].tp[sp2, cc] + MT tpbar[sp1, cc].ProjP[sp1, sp2].uq[sp2, 3, cc]) + (Cos[th]^2 - 1) MT uqbar[sp1, 3, cc].ProjP[sp1, sp2].uq[sp2, 3, cc] + Sin[th]^2 MTP tpbar[sp1, cc].ProjP[sp1, sp2].tp[sp2, cc]) H; ExpandIndices[hh + HC[hh]]]"
    },
    {
      "name": "LCCbp",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, ff, cc, cc2}, cc2 = -gw/Sqrt[2] CKM[ff, 3] (Sin[thd] uqbar[sp1, ff, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + (Cos[thd] - 1) uqbar[sp1, ff, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 3, cc]) W[mu]; ExpandIndices[cc2 + HC[cc2], FlavorExpand -> Generation]]"
    },
    {
      "name": "LNCbp",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, cc}, ExpandIndices[gw/(2 cw) (Sin[thd] Cos[thd] (dqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + bpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 3, cc]) + (Cos[thd]^2 - 1) dqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 3, cc] + Sin[thd]^2 bpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc]) Z[mu]]]"
    },
    {
      "name": "LHbp",
      "delayed": true,
      "expression": "Block[{sp1, sp2, cc, hh}, hh = -gw/(2 MW) (Sin[thd] Cos[thd] (MBP dqbar[sp1, 3, cc].ProjP[sp1, sp2].bp[sp2, cc] + MB bpbar[sp1, cc].ProjP[sp1, sp2].dq[sp2, 3, cc]) + (Cos[thd]^2 - 1) MB dqbar[sp1, 3, cc].ProjP[sp1, sp2].dq[sp2, 3, cc] + Sin[thd]^2 MBP bpbar[sp1, cc].ProjP[sp1, sp2].bp[sp2, cc]) H; ExpandIndices[hh + HC[hh]]]"
    },
    {
      "name": "LCC4",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, cc, cc4}, cc4 = -gw/Sqrt[2] (CKM4[4, 1] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 1, cc] + CKM4[4, 2] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 2, cc] + CKM4[4, 3] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 3, cc] + CKM4[1, 4] uqbar[sp1, 1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + CKM4[2, 4] uqbar[sp1, 2, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + CKM4[3, 4] uqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + CKM4[4, 4] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc]) W[mu]; ExpandIndices[cc4 + HC[cc4]]]"
    },
    {
      "name": "LVLQ",
      "delayed": true,
      "expression": "LTPkin + LBPkin + LL4kin + LY4 + LCCtp + LNCtp + LHtp + LCCbp + LNCbp + LHbp"
    },
    {
      "name": "LGen4",
      "delayed": true,
      "expression": "LTPkin + LBPkin + LL4kin + LY4 + LCC4"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LVLQ"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LNP"
    }
  ]
}
```
I've read the paper, the schema, the renderer, and SM.fr. No reference or cached `.fr` model file for this model exists in the sandbox, and none was read.

## Physics content extracted from arXiv:hep-ph/0607115

The paper gives **two** minimal SM extensions that relax 3×3 CKM unitarity:

1. **Vector-like Q = +2/3 iso-singlet quark t′** (Sec. 2.1): new parameters = the t−t′ mixing angle θ (Eqs. 5, 8–10) and m_t′ (Eq. 12). New interactions: 4×3 charged current (Eq. 7), tree-level FCNC Z (Eq. 14) and Higgs (Eq. 15) with VV† of Eq. (16).
2. **Vector-like down-type b′** (Sec. 2.1, Eq. 17): mixing angle θ_d, sin θ_d ≲ 0.06.
3. **Fourth generation** (Sec. 2.2): t′ and b′ with a 4×4 unitary CKM parametrised by θ_u, θ_v, θ_w (Eqs. 31–35), plus the fourth-generation leptons required by anomaly cancellation (end of Sec. 2.2.1).

## Mandatory self-audit table

Field mass dimensions: fermion 3/2, scalar 1, vector 1, `del`/`DC` 1. All new-physics operators here have d ≤ 4, so no EFT cutoff is needed anywhere (rule 2 does not apply: the paper contains no 1/Λⁿ operator).

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L/B number | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LTPkin (kin) | `tpLbar Ga DC[tpL]`, `tpRbar Ga DC[tpR]` | 4 | none (gauge coupling inside `DC`) | 0 ✓ | n/a | −2/3+2/3=0 ✓ | −2/3+2/3=0 ✓ | singlet (no SU2D index) | `tpLbar[cc] … tpL[cc]` shared Colour | none | B: −1/3+1/3=0 | n/a | self-conjugate |
| LTPkin (mass) | `MTP tpbar.tp` | 3 | MTP | 1 ✓ | n/a | 0 ✓ | −2/3+2/3=0 ✓ (vector-like ⇒ bare Dirac mass invariant, Eq. 12) | singlet | shared Colour | none | 0 | n/a | self-conjugate |
| LBPkin (kin) | `bpLbar Ga DC[bpL]`, `bpRbar Ga DC[bpR]` | 4 | none | 0 ✓ | n/a | +1/3−1/3=0 ✓ | +1/3−1/3=0 ✓ | singlet | shared Colour | none | 0 | n/a | self-conjugate |
| LBPkin (mass) | `MBP bpbar.bp` | 3 | MBP | 1 ✓ | n/a | 0 ✓ | 0 ✓ (vector-like) | singlet | shared Colour | none | 0 | n/a | self-conjugate |
| LL4kin | `LL4bar Ga DC[LL4]`, `lR4bar Ga DC[lR4]`, `vR4bar Ga DC[vR4]` | 4 | none | 0 ✓ | n/a | 0 ✓ | +1/2−1/2=0; +1−1=0; 0+0=0 ✓ | doublet·anti-doublet on shared `SU2D` index | colour singlet | none | L: −1+1=0 | n/a | self-conjugate |
| LY4 (charged) | `yl4 LL4bar[sp,ii].lR4[sp] Phi[ii]` | 4 | yl4 | 0 ✓ | n/a | 0−1+1=0 ✓ | +1/2−1+1/2=0 ✓ | `LL4bar[ii]` with `Phi[ii]`, shared index ✓ | singlet | none | 0 | n/a | `HC[...]` |
| LY4 (neutral) | `yv4 LL4bar[sp,ii].vR4[sp] Phibar[jj] Eps[ii,jj]` | 4 | yv4 | 0 ✓ | n/a | 0+0+0=0 ✓ | +1/2+0−1/2=0 ✓ | same conjugation type ⇒ `Eps[ii,jj]` on two distinct indices ✓ | singlet | none | 0 | n/a | `HC[...]` |
| LCCtp | `gw CKM[3,ff] tpbar Ga ProjM dq W`, `+ (Cos[th]−1)` top piece | 4 | gw Sin[th] / gw (Cos[th]−1) | 0 ✓ | n/a | −2/3−1/3+1=0 ✓ | mass basis after EWSB — see note below | rotation of the SU(2)-invariant Eq. (11)/(12) Lagrangian | `tpbar[cc] … dq[cc]` shared Colour | none | B: −1/3+1/3=0 | n/a | `HC[...]` |
| LNCtp | `gw uqbar Ga ProjM tp Z`, `tpbar … uq Z`, diagonal pieces | 4 | gw SinCos[th], gw(Cos²−1), gw Sin² | 0 ✓ | n/a | −2/3+2/3+0=0 ✓ | mass basis (Eq. 14) | descends from Eq. (16) VV† | shared Colour | none | 0 | n/a | Hermitian by construction (the two FCNC pieces are mutual conjugates) |
| LHtp | `gw/(2 MW) MTP uqbar ProjP tp H` and partners | 4 | gw MTP/(2 MW) (dimensionless) | 0 ✓ | n/a | −2/3+2/3+0=0 ✓ | mass basis (Eq. 15) | — | shared Colour | none | 0 | n/a | `HC[...]` |
| LCCbp | `gw CKM[ff,3] uqbar Ga ProjM bp W`, `+ (Cos[thd]−1)` b piece | 4 | gw Sin[thd] | 0 ✓ | n/a | −2/3−1/3+1=0 ✓ | mass basis (Eq. 17 model) | — | shared Colour | none | 0 | n/a | `HC[...]` |
| LNCbp | `gw dqbar Ga ProjM bp Z` + diagonal pieces | 4 | gw SinCos[thd] | 0 ✓ | n/a | +1/3−1/3+0=0 ✓ | mass basis | — | shared Colour | none | 0 | n/a | Hermitian by construction |
| LHbp | `gw/(2 MW) MBP dqbar ProjP bp H` and partners | 4 | gw MBP/(2 MW) | 0 ✓ | n/a | +1/3−1/3+0=0 ✓ | mass basis | — | shared Colour | none | 0 | n/a | `HC[...]` |
| LCC4 | `gw CKM4[4,j] tpbar Ga ProjM dq W`, `gw CKM4[i,4] uqbar Ga ProjM bp W`, `gw CKM4[4,4] tpbar Ga ProjM bp W` | 4 | gw CKM4[i,j] | 0 ✓ | n/a | −2/3−1/3+1=0 ✓ (every monomial) | mass basis (Eqs. 31–35) | — | shared Colour | none | B: 0 | n/a | `HC[...]` |

Kinetic + mass confirmation, one row per new class (all are in the total sum `LNP`, and `LGen4` for the fourth-generation option):

| class | kinetic term | mass term | in total sum |
|---|---|---|---|
| F[5] tp | LTPkin (via `tpL`,`tpR`, `DC`) | `− MTP tpbar.tp` in LTPkin, symbol `MTP` from `Mass -> {MTP, 500.}` | yes |
| F[6] bp | LBPkin | `− MBP bpbar.bp`, symbol `MBP` | yes |
| F[7] lp | LL4kin (via `LL4`,`lR4`) | LY4, `yl4 = Sqrt[2] MLP/vev`, symbol `MLP` | yes |
| F[8] vp | LL4kin (via `LL4`,`vR4`) | LY4, `yv4 = Sqrt[2] MVP/vev`, symbol `MVP` | yes |

Notes required by the rules:
- **Y sums in mass-basis terms**: LCCtp, LNCtp, LHtp, LCCbp, LNCbp, LHbp and LCC4 are written with physical (post-EWSB) fields, exactly as the paper writes Eqs. (7), (14), (15). Hypercharge is not a symmetry of a broken-phase monomial; these terms are the rotation (Eqs. 8–10, 16, 31–35) of the manifestly SU(2)×U(1)-invariant gauge-basis Lagrangian of Eqs. (11)–(12), so only the electric charge sum must vanish, and it does in every monomial. All terms written in the unbroken basis (LTPkin, LBPkin, LL4kin, LY4) have Y sum 0.
- **SelfConjugate -> True classes**: none. All eleven new classes are complex Dirac/chiral fields with `self_conjugate = false`, so no quantum number sits on a self-conjugate class.
- **Charge conjugation**: the paper writes no `psi^c`, no `psi^T C`, and no Majorana state, so `CC[...]` is not used anywhere ("n/a" in every row).
- **Reference/cached model file read: none.**

```json
{
  "model_name": "VLQ_gen",
  "info": {
    "authors": [
      "J. Alwall",
      "R. Frederix",
      "J.-M. Gerard",
      "A. Giammanco",
      "M. Herquet",
      "S. Kalinin",
      "E. Kou",
      "V. Lemaitre",
      "F. Maltoni"
    ],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": [
      "Centre for Particle Physics and Phenomenology (CP3), Universite catholique de Louvain"
    ],
    "emails": []
  },
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Gen4",
      "range_kind": "NoUnfold",
      "size": 4,
      "style_symbol": "g4"
    }
  ],
  "parameters": [
    {
      "name": "th",
      "parameter_type": "External",
      "value": "0.78",
      "block_name": "VLQMIX",
      "order_block": 1,
      "tex": "\\theta",
      "description": "t - t' mixing angle theta of the vector-like model, Eqs.(5),(8)-(10): Vti = V0ti Cos[th], Vt'i = V0ti Sin[th]. Benchmark of Figs.1,8: Cos[th] = 0.71. Rb gives |Cos[th]| > 0.91, Eq.(30)."
    },
    {
      "name": "thd",
      "parameter_type": "External",
      "value": "0.06",
      "block_name": "VLQMIX",
      "order_block": 2,
      "tex": "\\theta_d",
      "description": "b - b' mixing angle theta_d of the down-type vector-like model, Sec.2.1: Vtb = V0tb Cos[thd]. Rb constrains Sin[thd] < 0.06, Eq.(17)."
    },
    {
      "name": "thu",
      "parameter_type": "External",
      "value": "0.37",
      "block_name": "GEN4MIX",
      "order_block": 1,
      "tex": "\\theta_u",
      "description": "Fourth-generation 3-4 mixing angle theta_u of V4x4 = R34(thu) R24(thv) R14(thw), Eq.(31). Rb gives |Cos[thu]| > 0.93, Eq.(42)."
    },
    {
      "name": "thv",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "GEN4MIX",
      "order_block": 2,
      "tex": "\\theta_v",
      "description": "Fourth-generation 2-4 mixing angle theta_v, Eq.(31). Unitarity gives |thv| <= O(lambda) ~ 0.2, Eq.(36); thv = 0.2 is excluded, thv = 0.1 is allowed (Fig.4)."
    },
    {
      "name": "thw",
      "parameter_type": "External",
      "value": "0.05",
      "block_name": "GEN4MIX",
      "order_block": 3,
      "tex": "\\theta_w",
      "description": "Fourth-generation 1-4 mixing angle theta_w, Eq.(31). Unitarity gives |thw| <= O(lambda^2) ~ 0.05, Eq.(36)."
    },
    {
      "name": "CKM4",
      "parameter_type": "Internal",
      "indices": ["Gen4", "Gen4"],
      "value_rules": [
        {"lhs": "CKM4[1,1]", "rhs": "Cos[thw] CKM[1,1]"},
        {"lhs": "CKM4[1,2]", "rhs": "Cos[thw] CKM[1,2]"},
        {"lhs": "CKM4[1,3]", "rhs": "Cos[thw] CKM[1,3]"},
        {"lhs": "CKM4[1,4]", "rhs": "-Sin[thw]"},
        {"lhs": "CKM4[2,1]", "rhs": "Cos[thv] CKM[2,1] - Sin[thv] Sin[thw] CKM[1,1]"},
        {"lhs": "CKM4[2,2]", "rhs": "Cos[thv] CKM[2,2] - Sin[thv] Sin[thw] CKM[1,2]"},
        {"lhs": "CKM4[2,3]", "rhs": "Cos[thv] CKM[2,3] - Sin[thv] Sin[thw] CKM[1,3]"},
        {"lhs": "CKM4[2,4]", "rhs": "-Sin[thv] Cos[thw]"},
        {"lhs": "CKM4[3,1]", "rhs": "Cos[thu] CKM[3,1] - Sin[thu] Sin[thv] CKM[2,1] - Sin[thu] Cos[thv] Sin[thw] CKM[1,1]"},
        {"lhs": "CKM4[3,2]", "rhs": "Cos[thu] CKM[3,2] - Sin[thu] Sin[thv] CKM[2,2] - Sin[thu] Cos[thv] Sin[thw] CKM[1,2]"},
        {"lhs": "CKM4[3,3]", "rhs": "Cos[thu] CKM[3,3] - Sin[thu] Sin[thv] CKM[2,3] - Sin[thu] Cos[thv] Sin[thw] CKM[1,3]"},
        {"lhs": "CKM4[3,4]", "rhs": "-Sin[thu] Cos[thv] Cos[thw]"},
        {"lhs": "CKM4[4,1]", "rhs": "Sin[thu] CKM[3,1] + Cos[thu] Sin[thv] CKM[2,1] + Cos[thu] Cos[thv] Sin[thw] CKM[1,1]"},
        {"lhs": "CKM4[4,2]", "rhs": "Sin[thu] CKM[3,2] + Cos[thu] Sin[thv] CKM[2,2] + Cos[thu] Cos[thv] Sin[thw] CKM[1,2]"},
        {"lhs": "CKM4[4,3]", "rhs": "Sin[thu] CKM[3,3] + Cos[thu] Sin[thv] CKM[2,3] + Cos[thu] Cos[thv] Sin[thw] CKM[1,3]"},
        {"lhs": "CKM4[4,4]", "rhs": "Cos[thu] Cos[thv] Cos[thw]"}
      ],
      "tex": "V^{4x4}",
      "description": "4x4 unitary quark mixing matrix of the fourth-generation model, Eqs.(31)-(35); row/column 4 belong to t' and b'. Built on the SM 3x3 CKM of SM.fr."
    },
    {
      "name": "yl4",
      "parameter_type": "Internal",
      "value": "Sqrt[2] MLP/vev",
      "interaction_order": ["QED", 1],
      "tex": "y_{l4}",
      "description": "Yukawa coupling of the fourth-generation charged lepton; fixes its mass MLP (Sec.2.2.1, anomaly cancellation needs a fourth lepton generation)."
    },
    {
      "name": "yv4",
      "parameter_type": "Internal",
      "value": "Sqrt[2] MVP/vev",
      "interaction_order": ["QED", 1],
      "tex": "y_{v4}",
      "description": "Yukawa coupling of the fourth-generation Dirac neutrino; fixes its mass MVP (Sec.2.2.1)."
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 5,
      "class_name": "tp",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MTP", "value": "500."},
      "width": {"sym": "WTP", "value": "10."},
      "quantum_numbers": {"Q": "2/3"},
      "pdg": 8,
      "particle_name": "tp",
      "antiparticle_name": "tp~",
      "full_name": "t-prime quark",
      "propagator_label": "tp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 6,
      "class_name": "bp",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MBP", "value": "500."},
      "width": {"sym": "WBP", "value": "10."},
      "quantum_numbers": {"Q": "-1/3"},
      "pdg": 7,
      "particle_name": "bp",
      "antiparticle_name": "bp~",
      "full_name": "b-prime quark",
      "propagator_label": "bp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 7,
      "class_name": "lp",
      "self_conjugate": false,
      "mass": {"sym": "MLP", "value": "300."},
      "width": {"sym": "WLP", "value": "1."},
      "quantum_numbers": {"Q": "-1", "LeptonNumber": "1"},
      "pdg": 17,
      "particle_name": "l4-",
      "antiparticle_name": "l4+",
      "full_name": "Fourth-generation charged lepton",
      "propagator_label": "l4",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 8,
      "class_name": "vp",
      "self_conjugate": false,
      "mass": {"sym": "MVP", "value": "150."},
      "width": {"sym": "WVP", "value": "1."},
      "quantum_numbers": {"Q": "0", "LeptonNumber": "1"},
      "pdg": 18,
      "particle_name": "v4",
      "antiparticle_name": "v4~",
      "full_name": "Fourth-generation Dirac neutrino",
      "propagator_label": "v4",
      "propagator_type": "S",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 16,
      "class_name": "tpL",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "2/3"},
      "unphysical": true,
      "definitions": [
        "tpL[sp1_, cc_] :> Module[{sp2}, ProjM[sp1, sp2] tp[sp2, cc]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 17,
      "class_name": "tpR",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "2/3"},
      "unphysical": true,
      "definitions": [
        "tpR[sp1_, cc_] :> Module[{sp2}, ProjP[sp1, sp2] tp[sp2, cc]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 18,
      "class_name": "bpL",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "-1/3"},
      "unphysical": true,
      "definitions": [
        "bpL[sp1_, cc_] :> Module[{sp2}, ProjM[sp1, sp2] bp[sp2, cc]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 19,
      "class_name": "bpR",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "-1/3"},
      "unphysical": true,
      "definitions": [
        "bpR[sp1_, cc_] :> Module[{sp2}, ProjP[sp1, sp2] bp[sp2, cc]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 20,
      "class_name": "LL4",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "-1/2"},
      "unphysical": true,
      "definitions": [
        "LL4[sp1_, 1] :> Module[{sp2}, ProjM[sp1, sp2] vp[sp2]]",
        "LL4[sp1_, 2] :> Module[{sp2}, ProjM[sp1, sp2] lp[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 21,
      "class_name": "lR4",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "-1"},
      "unphysical": true,
      "definitions": [
        "lR4[sp1_] :> Module[{sp2}, ProjP[sp1, sp2] lp[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 22,
      "class_name": "vR4",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "0"},
      "unphysical": true,
      "definitions": [
        "vR4[sp1_] :> Module[{sp2}, ProjP[sp1, sp2] vp[sp2]]"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LTPkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I tpLbar.Ga[mu].DC[tpL, mu] + I tpRbar.Ga[mu].DC[tpR, mu] - MTP tpbar.tp]]"
    },
    {
      "name": "LBPkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I bpLbar.Ga[mu].DC[bpL, mu] + I bpRbar.Ga[mu].DC[bpR, mu] - MBP bpbar.bp]]"
    },
    {
      "name": "LL4kin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I LL4bar.Ga[mu].DC[LL4, mu] + I lR4bar.Ga[mu].DC[lR4, mu] + I vR4bar.Ga[mu].DC[vR4, mu], FlavorExpand -> {SU2W, SU2D}]]"
    },
    {
      "name": "LY4",
      "delayed": true,
      "expression": "Block[{sp1, ii, jj, yuk}, yuk = -yl4 LL4bar[sp1, ii].lR4[sp1] Phi[ii] - yv4 LL4bar[sp1, ii].vR4[sp1] Phibar[jj] Eps[ii, jj]; ExpandIndices[yuk + HC[yuk], FlavorExpand -> SU2D]]"
    },
    {
      "name": "LCCtp",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, ff, cc, cc1}, cc1 = -gw/Sqrt[2] CKM[3, ff] (Sin[th] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, ff, cc] + (Cos[th] - 1) uqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, ff, cc]) W[mu]; ExpandIndices[cc1 + HC[cc1], FlavorExpand -> Generation]]"
    },
    {
      "name": "LNCtp",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, cc}, ExpandIndices[-gw/(2 cw) (Sin[th] Cos[th] (uqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].tp[sp3, cc] + tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].uq[sp3, 3, cc]) + (Cos[th]^2 - 1) uqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].uq[sp3, 3, cc] + Sin[th]^2 tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].tp[sp3, cc]) Z[mu]]]"
    },
    {
      "name": "LHtp",
      "delayed": true,
      "expression": "Block[{sp1, sp2, cc, hh}, hh = -gw/(2 MW) (Sin[th] Cos[th] (MTP uqbar[sp1, 3, cc].ProjP[sp1, sp2].tp[sp2, cc] + MT tpbar[sp1, cc].ProjP[sp1, sp2].uq[sp2, 3, cc]) + (Cos[th]^2 - 1) MT uqbar[sp1, 3, cc].ProjP[sp1, sp2].uq[sp2, 3, cc] + Sin[th]^2 MTP tpbar[sp1, cc].ProjP[sp1, sp2].tp[sp2, cc]) H; ExpandIndices[hh + HC[hh]]]"
    },
    {
      "name": "LCCbp",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, ff, cc, cc2}, cc2 = -gw/Sqrt[2] CKM[ff, 3] (Sin[thd] uqbar[sp1, ff, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + (Cos[thd] - 1) uqbar[sp1, ff, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 3, cc]) W[mu]; ExpandIndices[cc2 + HC[cc2], FlavorExpand -> Generation]]"
    },
    {
      "name": "LNCbp",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, cc}, ExpandIndices[gw/(2 cw) (Sin[thd] Cos[thd] (dqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + bpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 3, cc]) + (Cos[thd]^2 - 1) dqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 3, cc] + Sin[thd]^2 bpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc]) Z[mu]]]"
    },
    {
      "name": "LHbp",
      "delayed": true,
      "expression": "Block[{sp1, sp2, cc, hh}, hh = -gw/(2 MW) (Sin[thd] Cos[thd] (MBP dqbar[sp1, 3, cc].ProjP[sp1, sp2].bp[sp2, cc] + MB bpbar[sp1, cc].ProjP[sp1, sp2].dq[sp2, 3, cc]) + (Cos[thd]^2 - 1) MB dqbar[sp1, 3, cc].ProjP[sp1, sp2].dq[sp2, 3, cc] + Sin[thd]^2 MBP bpbar[sp1, cc].ProjP[sp1, sp2].bp[sp2, cc]) H; ExpandIndices[hh + HC[hh]]]"
    },
    {
      "name": "LCC4",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, cc, cc4}, cc4 = -gw/Sqrt[2] (CKM4[4, 1] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 1, cc] + CKM4[4, 2] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 2, cc] + CKM4[4, 3] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].dq[sp3, 3, cc] + CKM4[1, 4] uqbar[sp1, 1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + CKM4[2, 4] uqbar[sp1, 2, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + CKM4[3, 4] uqbar[sp1, 3, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc] + CKM4[4, 4] tpbar[sp1, cc].Ga[mu, sp1, sp2].ProjM[sp2, sp3].bp[sp3, cc]) W[mu]; ExpandIndices[cc4 + HC[cc4]]]"
    },
    {
      "name": "LVLQ",
      "delayed": true,
      "expression": "LTPkin + LBPkin + LL4kin + LY4 + LCCtp + LNCtp + LHtp + LCCbp + LNCbp + LHbp"
    },
    {
      "name": "LGen4",
      "delayed": true,
      "expression": "LTPkin + LBPkin + LL4kin + LY4 + LCC4"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LVLQ"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LNP"
    }
  ]
}
```