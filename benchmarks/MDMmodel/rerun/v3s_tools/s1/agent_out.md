## Mandatory self-audit table

Read files: paper LaTeX source (`1311.6661_source.tex`, full text), `frmodel.py` schema, and `SM.fr` (allowed reference for field/index conventions). No cached or reference `.fr` file for MDMmodel itself was read: **none**.

**Naming note on the dilaton scale**: SM.fr already uses the bare symbol `f` as the SU(3) structure constant (`SU3C == {... StructureConstant -> f ...}`). The paper's dilaton scale (also called `f`) is therefore renamed `fS` throughout to avoid the collision (rule 10).

**Modelling choice (documented)**: `H` (SM.fr's physical Higgs, mass `MH`=125) is identified with the paper's mass eigenstate `h`; a new physical real scalar `s` is the dilaton mass eigenstate. The gauge-eigenstate singlet field `S = fS + h·sinθ_S + s·cosθ_S` is implemented as a genuinely new **Unphysical** class `Sgauge` (index ≥100, rule 8), used only in undifferentiated (non-kinetic) positions, so it never distorts `s`'s or `H`'s own canonical kinetic normalization. `s` gets its own standalone canonical kinetic+mass term. This is an add-on-level simplification (SM.fr's own Higgs potential/kinetic term is not rewritten, consistent with "SM add-on ⇒ gauge_groups []"); it is stated here rather than silently assumed.

| term | fields | d | coupling | coupling dim (4−d) | 1/Λ | Q Σ | Y Σ | SU(2) | SU(3) | new-U(1) | L/B | CC[] | fraction/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LSkin (kinetic+mass, new class `s`) | s,s (∂s∂s / s²) | 4 | none / `Ms` | 0 / 1 ✓ | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | n/a | self-conjugate |
| LT (kinetic+mass+portal, new class `Tp`) | Tpbar,Ga,DC,Tp / Tpbar,Sgauge,Tp | 4 | none / `gTS` | 0 / 0 ✓ | n/a | 0 | 0 | singlet | 3⊗3̄ | none | n/a | n/a | n/a | auto-Hermitian (Dirac bilinear) |
| LYT (y′ Yukawa, Eq. MDM) | QLbar,TpR,Phibar,Eps | 4 | `yprime` | 0 ✓ | n/a | 0 (structurally identical to SM up-Yukawa, uR→TpR, same Y=2/3) | 0 | Eps[ii,jj] with QLbar,Phibar (rule 4) | 3⊗3̄ | none | n/a | n/a (no ψ^c in this term) | n/a (no fraction) | HC[yuk] included |
| LPortal (κ/2 S²\|H\|², Eq. potential) | Sgauge,Sgauge,Phibar,Phi | 4 | `kappa` | 0 ✓ | n/a | 0 | 0 | Phibar[ii]Phi[ii] singlet | singlet | none | n/a | n/a | κ formula: `Abs[MH^2-Ms^2]/(2 fS vev) Abs[Sin[2 thetaS]]` taken literally from Eq.(4) LaTeX (`\frac{...}{...}`) | self-conjugate combination |
| LSself (λ_S/4! S⁴) | Sgauge×4 | 4 | `lambdaS` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | λ_S formula taken literally from Eq.(4) LaTeX | self-conjugate |
| LTotal | sums LSM+LSkin+LT+LYT+LPortal+LSself | — | — | — | — | — | — | — | — | — | — | — | — | single declared total |

- Per-new-particle-class kinetic+mass confirmation: `s` → LSkin ✓ (in LTotal); `Tp` → LT ✓ (in LTotal).
- No non-fundamental colour representation introduced (Tp is a fundamental colour triplet); no `AddGaugeRepresentation` needed.
- `SelfConjugate -> True` classes: `s`, `Sgauge` — both carry no `QuantumNumbers` ✓.
- Names chosen: classes `s`, `Sgauge`, `Tp`, `TpR`; parameters `fS`, `thetaS`, `Ms`, `MTp`, `yprime`, `eta`, `kappa`, `lambdaH`, `lambdaS`, `gTS`. None is a Mathematica/FeynRules builtin (`N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM`) or an SM.fr name (checked against SM.fr's full symbol list, including avoiding `f`).
- Single total Lagrangian: `LTotal`, summing `LSM + LSkin + LT + LYT + LPortal + LSself`.
- Reference/cached model file read: **none**.
- `yprime` has no explicit numeric benchmark in the paper; an O(1) placeholder (`1.`) is used and documented in its `description`.

```json
{
  "model_name": "MDMmodel_gen",
  "info": {
    "authors": ["Automated FeynRules extraction (benchmark run)"],
    "version": "1.0",
    "date": "2026-09-17",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "fS",
      "parameter_type": "External",
      "value": "615.",
      "block_name": "MDM",
      "order_block": 1,
      "description": "Dilaton decay constant f [GeV] (renamed from paper's f to avoid clash with SM.fr's SU(3) structure constant f); benchmark eta^-1=f/v=2.5, Eq. eta"
    },
    {
      "name": "thetaS",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "MDM",
      "order_block": 2,
      "description": "Higgs-dilaton mixing angle theta_S [rad], Eq. mixing; benchmark in the |tan(thetaS)|<=2 favored region"
    },
    {
      "name": "Ms",
      "parameter_type": "External",
      "value": "400.",
      "block_name": "MDM",
      "order_block": 3,
      "description": "Physical dilaton mass [GeV], heavy-dilaton benchmark point quoted in the paper's discovery discussion (m_s=400 GeV)"
    },
    {
      "name": "MTp",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "MDM",
      "order_block": 4,
      "description": "Physical top-partner (T) mass [GeV]; benchmark within the scanned range 700-3000 GeV"
    },
    {
      "name": "yprime",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "MDM",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "description": "y' Yukawa coupling of T_R to q3L.H, Eq. MDM; no explicit numeric benchmark given in the paper, O(1) placeholder used"
    },
    {
      "name": "eta",
      "parameter_type": "Internal",
      "value": "vev/fS",
      "description": "eta = v/f * N_T with N_T=1 for the MDM, Eq. eta"
    },
    {
      "name": "kappa",
      "parameter_type": "Internal",
      "value": "Abs[MH^2 - Ms^2]/(2*fS*vev) * Abs[Sin[2*thetaS]]",
      "interaction_order": ["NP", 1],
      "description": "S^2|H|^2/2 portal coupling, re-expressed via mh, ms, thetaS (Eq. potential mixing relations, LaTeX-verified fraction placement)"
    },
    {
      "name": "lambdaH",
      "parameter_type": "Internal",
      "value": "(Abs[MH^2 - Ms^2]/vev^2) * (Abs[(MH^2+Ms^2)/(MH^2-Ms^2)] + Sign[Sin[2*thetaS]]*Cos[2*thetaS])",
      "description": "Higgs quartic implied by the h-s mixing relations (Eq. potential mixing); recorded for completeness, not separately imposed on H's own SM.fr potential (which stays fixed by MH, vev, lam)"
    },
    {
      "name": "lambdaS",
      "parameter_type": "Internal",
      "value": "(3*Abs[MH^2 - Ms^2]/(2*fS^2)) * (Abs[(MH^2+Ms^2)/(MH^2-Ms^2)] - Sign[Sin[2*thetaS]]*Cos[2*thetaS])",
      "interaction_order": ["NP", 1],
      "description": "Dilaton quartic self-coupling S^4/4!, re-expressed via mh, ms, thetaS (Eq. potential mixing relations)"
    },
    {
      "name": "gTS",
      "parameter_type": "Internal",
      "value": "MTp/fS",
      "interaction_order": ["NP", 1],
      "description": "M/f coupling of the top partner to the dilaton field S = fS + h sin(thetaS) + s cos(thetaS), Eq. MDM"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "s",
      "self_conjugate": true,
      "indices": [],
      "mass": {"massless": false, "sym": "Ms", "value": "400.", "members": []},
      "width": {"massless": false, "sym": "Ws", "value": "Automatic", "members": []},
      "quantum_numbers": {},
      "pdg": 35,
      "particle_name": "s",
      "full_name": "Dilaton",
      "propagator_label": "s",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Sgauge",
      "self_conjugate": true,
      "indices": [],
      "quantum_numbers": {},
      "unphysical": true,
      "definitions": ["Sgauge -> fS + H*Sin[thetaS] + s*Cos[thetaS]"]
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Tp",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"massless": false, "sym": "MTp", "value": "1000.", "members": []},
      "width": {"massless": false, "sym": "Wtp", "value": "Automatic", "members": []},
      "quantum_numbers": {"Q": "2/3"},
      "pdg": 8000006,
      "particle_name": "tp",
      "antiparticle_name": "tpbar",
      "full_name": "Top-quark partner",
      "propagator_label": "Tp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "TpR",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "2/3"},
      "unphysical": true,
      "definitions": ["TpR[sp1_,cc_] :> Module[{sp2}, ProjP[sp1,sp2] Tp[sp2,cc]]"]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LSkin",
      "expression": "Block[{mu}, ExpandIndices[1/2 del[s,mu] del[s,mu] - 1/2 Ms^2 s^2]]",
      "delayed": true
    },
    {
      "name": "LT",
      "expression": "Block[{mu}, ExpandIndices[I*Tpbar.Ga[mu].DC[Tp,mu] - gTS*Sgauge*Tpbar.Tp]]",
      "delayed": true
    },
    {
      "name": "LYT",
      "expression": "Block[{sp,ii,jj,cc,yuk}, yuk = ExpandIndices[-yprime*QLbar[sp,ii,3,cc].TpR[sp,cc]*Phibar[jj]*Eps[ii,jj], FlavorExpand->SU2D]; yuk + HC[yuk]]",
      "delayed": true
    },
    {
      "name": "LPortal",
      "expression": "Block[{ii}, ExpandIndices[(kappa/2)*Sgauge^2*Phibar[ii]*Phi[ii], FlavorExpand->SU2D]]",
      "delayed": true
    },
    {
      "name": "LSself",
      "expression": "(lambdaS/24)*Sgauge^4",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LSkin + LT + LYT + LPortal + LSself",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```