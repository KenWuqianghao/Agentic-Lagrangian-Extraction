I'll start by reading the paper and the schema files.
## Self-audit

**Model content (from arXiv:1311.6661, Eqs. (2)–(9)).** The MDM adds to the SM: one real gauge-singlet scalar `S` (the linearized dilaton, vev `f`) and one vector-like fermion `T` with the quantum numbers of the right-handed top (colour triplet, SU(2) singlet, Y = 2/3, Q = 2/3). Physical new states: the dilaton mass eigenstate `s` and the top partner `t'`. The SM Higgs `h` and the SM top `t` stay SM classes.

**Basis choice.** SM.fr is loaded first, so the add-on cannot rotate `Phi` or `QL`. The fields are therefore declared in the gauge basis, with the paper's own input set (`f`, `v`, `thS`, `mh`, `ms`, `thL`, `mt'`): Eq. (5) fixes `kap`, `lamH`, `lamS` so that the CP-even mass matrix has eigenvalues `MH`, `Msd` and mixing angle `thS`; the tadpole conditions fix `mHsq`, `mSsq`. The residual `h`–`s` and `t`–`t'` two-point mixings are the physical mixings of Eqs. (4) and (9) and must be diagonalized by the user. No new U(1) is introduced by the paper, so all new-U(1) columns are empty.

| term | monomial | d | coupling | coup. dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L/B | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LSkin | del[Sng,mu] del[Sng,mu] | 4 | 1/2 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj. |
| LSpot | mSsq Sng^2 | 2 | mSsq | 2 ✓ | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj. |
| LSpot | lamS Sng^4 | 4 | lamS | 0 ✓ | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj. |
| LSpot | kap Sng^2 Phibar[ii] Phi[ii] | 4 | kap | 0 ✓ | n/a | 0 | −1/2+1/2=0 | shared ii | singlet | none | n/a | n/a | self-conj. |
| LSpot | mHsq Phibar[ii] Phi[ii] | 2 | mHsq | 2 ✓ | n/a | 0 | 0 | shared ii | singlet | none | n/a | n/a | self-conj. |
| LSpot | lamH (Phibar[ii]Phi[ii])(Phibar[jj]Phi[jj]) | 4 | lamH | 0 ✓ | n/a | 0 | 0 | shared ii, jj | singlet | none | n/a | n/a | self-conj. |
| LHpotSM (subtracted) | muH^2 Phibar[ii]Phi[ii] | 2 | muH^2 | 2 ✓ | n/a | 0 | 0 | shared ii | singlet | none | n/a | n/a | self-conj. |
| LHpotSM (subtracted) | lam (Phibar Phi)^2 | 4 | lam | 0 ✓ | n/a | 0 | 0 | shared ii, jj | singlet | none | n/a | n/a | self-conj. |
| LTkin | I TLbar.Ga[mu].DC[TL,mu] | 4 | 1 | 0 ✓ | n/a | −2/3+2/3=0 | −2/3+2/3=0 | singlet | shared cc | none | B: −1/3+1/3=0 | n/a | self-conj. |
| LTkin | I TRbar.Ga[mu].DC[TR,mu] | 4 | 1 | 0 ✓ | n/a | 0 | 0 | singlet | shared cc | none | 0 | n/a | self-conj. |
| LTkin | (Mtp/fS) Sng (TLbar.TR + TRbar.TL) | 4 | Mtp/fS | 0 ✓ | n/a | 0 | 0 | singlet | shared cc | none | 0 | n/a | sum is self-conj. |
| LTyuk | yp TRbar[sp,cc].QL[sp,ii,3,cc] Phi[jj] Eps[ii,jj] | 4 | yp | 0 ✓ | n/a | 0 (up+neutral, down+GP) | −2/3+1/6+1/2=0 | Eps[ii,jj], QL[ii] with Phi[jj] (same type) | shared cc | none | B: −1/3+1/3=0 | n/a | HC[yuk] |

Per-class free-field rows:

| class | kinetic | mass | in total sum |
|---|---|---|---|
| S[100] `sdl` (dilaton `s`) | LSkin, through `Sng -> fS + sdl` (canonical 1/2 del[sdl]del[sdl]) | from LSpot; the eigenvalue is the declared symbol `Msd`, enforced by Eq. (5) for `kap`/`lamH`/`lamS` plus the tadpole values of `mSsq`, `mHsq`. No separate free mass term is written, because that would double count the potential. | LMDM ✓ |
| F[100] `tp` (top partner `t'`) | LTkin, through `TL`/`TR` (chiral projections of `tp`, Y = 2/3) | `-(Mtp/fS) Sng (TLbar.TR + TRbar.TL)` gives `-Mtp tpbar.tp` at `<Sng> = fS`; `Mtp` is the declared class mass symbol and equals the paper's scale `M` | LMDM ✓ |

`SelfConjugate -> True` classes: `sdl` (S[100]) and `Sng` (S[101]) — both carry no `QuantumNumbers`. 
Reference or cached model file read: **none** (only the paper, the schema/renderer, and the provided SM.fr base model).

```json
{
  "model_name": "MDMmodel_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:1311.6661"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["HEPTAPOD benchmark"],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "fS",
      "parameter_type": "External",
      "value": "500.",
      "block_name": "DILATON",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "description": "Dilaton decay constant f = vev of the singlet S [GeV], Eq.(4); benchmark f/v = eta^-1 approx 2"
    },
    {
      "name": "thS",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "DILATON",
      "order_block": 2,
      "description": "Scalar mixing angle theta_S between the SM Higgs h and the dilaton s, Eq.(4); |tan(thS)| < 2"
    },
    {
      "name": "thL",
      "parameter_type": "External",
      "value": "0.2",
      "block_name": "DILATON",
      "order_block": 3,
      "description": "Left-handed top / top-partner mixing angle theta_L, Eq.(9); EWPD requires sin(thL) < 0.3"
    },
    {
      "name": "NT",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DILATON",
      "order_block": 4,
      "description": "Number N_T of vector-like T fields, Eq.(8); N_T = 1 in the MDM"
    },
    {
      "name": "eta",
      "parameter_type": "Internal",
      "value": "vev/fS*NT",
      "description": "eta = (v/f) N_T, Eq.(8); eta^-1 = f/v is the scan variable of Eq.(12)"
    },
    {
      "name": "kap",
      "parameter_type": "Internal",
      "value": "Abs[MH^2 - Msd^2]*Abs[Sin[2*thS]]/(2*fS*vev)",
      "interaction_order": ["QED", 2],
      "description": "Portal coupling kappa of (kappa/2) S^2 |H|^2, Eq.(3), re-expressed through Eq.(5)"
    },
    {
      "name": "lamH",
      "parameter_type": "Internal",
      "value": "Abs[MH^2 - Msd^2]/vev^2*((MH^2 + Msd^2)/(MH^2 - Msd^2) + Sign[Sin[2*thS]]*Cos[2*thS])",
      "interaction_order": ["QED", 2],
      "description": "Higgs quartic lambda_H of (lambda_H/4) |H|^4, Eq.(3), re-expressed through Eq.(5)"
    },
    {
      "name": "lamS",
      "parameter_type": "Internal",
      "value": "3*Abs[MH^2 - Msd^2]/(2*fS^2)*((MH^2 + Msd^2)/(MH^2 - Msd^2) - Sign[Sin[2*thS]]*Cos[2*thS])",
      "interaction_order": ["QED", 2],
      "description": "Singlet quartic lambda_S of (lambda_S/4!) S^4, Eq.(3), re-expressed through Eq.(5)"
    },
    {
      "name": "mHsq",
      "parameter_type": "Internal",
      "value": "-kap*fS^2/2 - lamH*vev^2/4",
      "description": "m_H^2 of Eq.(3), fixed by the minimum condition <H> = vev/Sqrt[2] of the potential"
    },
    {
      "name": "mSsq",
      "parameter_type": "Internal",
      "value": "-lamS*fS^2/6 - kap*vev^2/2",
      "description": "m_S^2 of Eq.(3), fixed by the minimum condition <S> = fS of the potential"
    },
    {
      "name": "yp",
      "parameter_type": "Internal",
      "value": "Sqrt[2]*Mtp*Tan[thL]/vev",
      "interaction_order": ["QED", 1],
      "description": "New Yukawa y' of Eq.(2); with M = Mtp the mixing of Eq.(9) gives y' = Sqrt[2] M tan(thL)/v, and the physical top-partner mass is Mtp/Cos[thL]"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "sdl",
      "self_conjugate": true,
      "mass": {"sym": "Msd", "value": "500."},
      "width": {"sym": "Wsd", "value": "1."},
      "pdg": 9000001,
      "particle_name": "sdl",
      "full_name": "Dilaton",
      "propagator_label": "sdl",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Sng",
      "self_conjugate": true,
      "unphysical": true,
      "definitions": ["Sng -> fS + sdl"]
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "tp",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "Mtp", "value": "1500."},
      "width": {"sym": "Wtp", "value": "15."},
      "quantum_numbers": {"Q": "2/3"},
      "pdg": 6000006,
      "particle_name": "tp",
      "antiparticle_name": "tp~",
      "full_name": "Top partner",
      "propagator_label": "tp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "TL",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "2/3"},
      "unphysical": true,
      "definitions": ["TL[sp1_, cc_] :> Module[{sp2}, ProjM[sp1, sp2] tp[sp2, cc]]"]
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "TR",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "2/3"},
      "unphysical": true,
      "definitions": ["TR[sp1_, cc_] :> Module[{sp2}, ProjP[sp1, sp2] tp[sp2, cc]]"]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LSkin",
      "expression": "Block[{mu}, ExpandIndices[1/2 del[Sng, mu] del[Sng, mu]]]",
      "delayed": true
    },
    {
      "name": "LSpot",
      "expression": "Block[{ii, jj}, ExpandIndices[-(mSsq/2 Sng^2 + lamS/24 Sng^4 + kap/2 Sng^2 Phibar[ii] Phi[ii] + mHsq Phibar[ii] Phi[ii] + lamH/4 Phibar[ii] Phi[ii] Phibar[jj] Phi[jj]), FlavorExpand -> SU2D]]",
      "delayed": true
    },
    {
      "name": "LHpotSM",
      "expression": "Block[{ii, jj}, ExpandIndices[muH^2 Phibar[ii] Phi[ii] - lam Phibar[ii] Phi[ii] Phibar[jj] Phi[jj], FlavorExpand -> SU2D]]",
      "delayed": true
    },
    {
      "name": "LTkin",
      "expression": "Block[{mu}, ExpandIndices[I TLbar.Ga[mu].DC[TL, mu] + I TRbar.Ga[mu].DC[TR, mu] - Mtp/fS Sng (TLbar.TR + TRbar.TL)]]",
      "delayed": true
    },
    {
      "name": "LTyuk",
      "expression": "Block[{sp, ii, jj, cc, yuk}, yuk = ExpandIndices[-yp TRbar[sp, cc].QL[sp, ii, 3, cc] Phi[jj] Eps[ii, jj], FlavorExpand -> SU2D]; yuk + HC[yuk]]",
      "delayed": true
    },
    {
      "name": "LMDM",
      "expression": "LSM - LHpotSM + LSkin + LSpot + LTkin + LTyuk",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
## Self-audit

**Model content (from arXiv:1311.6661, Eqs. (2)–(9)).** The MDM adds to the SM: one real gauge-singlet scalar `S` (the linearized dilaton, vev `f`) and one vector-like fermion `T` with the quantum numbers of the right-handed top (colour triplet, SU(2) singlet, Y = 2/3, Q = 2/3). Physical new states: the dilaton mass eigenstate `s` and the top partner `t'`. The SM Higgs `h` and the SM top `t` stay SM classes.

**Basis choice.** SM.fr is loaded first, so the add-on cannot rotate `Phi` or `QL`. The fields are therefore declared in the gauge basis, with the paper's own input set (`f`, `v`, `thS`, `mh`, `ms`, `thL`, `mt'`): Eq. (5) fixes `kap`, `lamH`, `lamS` so that the CP-even mass matrix has eigenvalues `MH`, `Msd` and mixing angle `thS`; the tadpole conditions fix `mHsq`, `mSsq`. The residual `h`–`s` and `t`–`t'` two-point mixings are the physical mixings of Eqs. (4) and (9) and must be diagonalized by the user. No new U(1) is introduced by the paper, so all new-U(1) columns are empty.

| term | monomial | d | coupling | coup. dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L/B | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LSkin | del[Sng,mu] del[Sng,mu] | 4 | 1/2 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj. |
| LSpot | mSsq Sng^2 | 2 | mSsq | 2 ✓ | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj. |
| LSpot | lamS Sng^4 | 4 | lamS | 0 ✓ | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj. |
| LSpot | kap Sng^2 Phibar[ii] Phi[ii] | 4 | kap | 0 ✓ | n/a | 0 | −1/2+1/2=0 | shared ii | singlet | none | n/a | n/a | self-conj. |
| LSpot | mHsq Phibar[ii] Phi[ii] | 2 | mHsq | 2 ✓ | n/a | 0 | 0 | shared ii | singlet | none | n/a | n/a | self-conj. |
| LSpot | lamH (Phibar[ii]Phi[ii])(Phibar[jj]Phi[jj]) | 4 | lamH | 0 ✓ | n/a | 0 | 0 | shared ii, jj | singlet | none | n/a | n/a | self-conj. |
| LHpotSM (subtracted) | muH^2 Phibar[ii]Phi[ii] | 2 | muH^2 | 2 ✓ | n/a | 0 | 0 | shared ii | singlet | none | n/a | n/a | self-conj. |
| LHpotSM (subtracted) | lam (Phibar Phi)^2 | 4 | lam | 0 ✓ | n/a | 0 | 0 | shared ii, jj | singlet | none | n/a | n/a | self-conj. |
| LTkin | I TLbar.Ga[mu].DC[TL,mu] | 4 | 1 | 0 ✓ | n/a | −2/3+2/3=0 | −2/3+2/3=0 | singlet | shared cc | none | B: −1/3+1/3=0 | n/a | self-conj. |
| LTkin | I TRbar.Ga[mu].DC[TR,mu] | 4 | 1 | 0 ✓ | n/a | 0 | 0 | singlet | shared cc | none | 0 | n/a | self-conj. |
| LTkin | (Mtp/fS) Sng (TLbar.TR + TRbar.TL) | 4 | Mtp/fS | 0 ✓ | n/a | 0 | 0 | singlet | shared cc | none | 0 | n/a | sum is self-conj. |
| LTyuk | yp TRbar[sp,cc].QL[sp,ii,3,cc] Phi[jj] Eps[ii,jj] | 4 | yp | 0 ✓ | n/a | 0 (up+neutral, down+GP) | −2/3+1/6+1/2=0 | Eps[ii,jj], QL[ii] with Phi[jj] (same type) | shared cc | none | B: −1/3+1/3=0 | n/a | HC[yuk] |

Per-class free-field rows:

| class | kinetic | mass | in total sum |
|---|---|---|---|
| S[100] `sdl` (dilaton `s`) | LSkin, through `Sng -> fS + sdl` (canonical 1/2 del[sdl]del[sdl]) | from LSpot; the eigenvalue is the declared symbol `Msd`, enforced by Eq. (5) for `kap`/`lamH`/`lamS` plus the tadpole values of `mSsq`, `mHsq`. No separate free mass term is written, because that would double count the potential. | LMDM ✓ |
| F[100] `tp` (top partner `t'`) | LTkin, through `TL`/`TR` (chiral projections of `tp`, Y = 2/3) | `-(Mtp/fS) Sng (TLbar.TR + TRbar.TL)` gives `-Mtp tpbar.tp` at `<Sng> = fS`; `Mtp` is the declared class mass symbol and equals the paper's scale `M` | LMDM ✓ |

`SelfConjugate -> True` classes: `sdl` (S[100]) and `Sng` (S[101]) — both carry no `QuantumNumbers`. 
Reference or cached model file read: **none** (only the paper, the schema/renderer, and the provided SM.fr base model).

```json
{
  "model_name": "MDMmodel_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:1311.6661"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["HEPTAPOD benchmark"],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "fS",
      "parameter_type": "External",
      "value": "500.",
      "block_name": "DILATON",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "description": "Dilaton decay constant f = vev of the singlet S [GeV], Eq.(4); benchmark f/v = eta^-1 approx 2"
    },
    {
      "name": "thS",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "DILATON",
      "order_block": 2,
      "description": "Scalar mixing angle theta_S between the SM Higgs h and the dilaton s, Eq.(4); |tan(thS)| < 2"
    },
    {
      "name": "thL",
      "parameter_type": "External",
      "value": "0.2",
      "block_name": "DILATON",
      "order_block": 3,
      "description": "Left-handed top / top-partner mixing angle theta_L, Eq.(9); EWPD requires sin(thL) < 0.3"
    },
    {
      "name": "NT",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DILATON",
      "order_block": 4,
      "description": "Number N_T of vector-like T fields, Eq.(8); N_T = 1 in the MDM"
    },
    {
      "name": "eta",
      "parameter_type": "Internal",
      "value": "vev/fS*NT",
      "description": "eta = (v/f) N_T, Eq.(8); eta^-1 = f/v is the scan variable of Eq.(12)"
    },
    {
      "name": "kap",
      "parameter_type": "Internal",
      "value": "Abs[MH^2 - Msd^2]*Abs[Sin[2*thS]]/(2*fS*vev)",
      "interaction_order": ["QED", 2],
      "description": "Portal coupling kappa of (kappa/2) S^2 |H|^2, Eq.(3), re-expressed through Eq.(5)"
    },
    {
      "name": "lamH",
      "parameter_type": "Internal",
      "value": "Abs[MH^2 - Msd^2]/vev^2*((MH^2 + Msd^2)/(MH^2 - Msd^2) + Sign[Sin[2*thS]]*Cos[2*thS])",
      "interaction_order": ["QED", 2],
      "description": "Higgs quartic lambda_H of (lambda_H/4) |H|^4, Eq.(3), re-expressed through Eq.(5)"
    },
    {
      "name": "lamS",
      "parameter_type": "Internal",
      "value": "3*Abs[MH^2 - Msd^2]/(2*fS^2)*((MH^2 + Msd^2)/(MH^2 - Msd^2) - Sign[Sin[2*thS]]*Cos[2*thS])",
      "interaction_order": ["QED", 2],
      "description": "Singlet quartic lambda_S of (lambda_S/4!) S^4, Eq.(3), re-expressed through Eq.(5)"
    },
    {
      "name": "mHsq",
      "parameter_type": "Internal",
      "value": "-kap*fS^2/2 - lamH*vev^2/4",
      "description": "m_H^2 of Eq.(3), fixed by the minimum condition <H> = vev/Sqrt[2] of the potential"
    },
    {
      "name": "mSsq",
      "parameter_type": "Internal",
      "value": "-lamS*fS^2/6 - kap*vev^2/2",
      "description": "m_S^2 of Eq.(3), fixed by the minimum condition <S> = fS of the potential"
    },
    {
      "name": "yp",
      "parameter_type": "Internal",
      "value": "Sqrt[2]*Mtp*Tan[thL]/vev",
      "interaction_order": ["QED", 1],
      "description": "New Yukawa y' of Eq.(2); with M = Mtp the mixing of Eq.(9) gives y' = Sqrt[2] M tan(thL)/v, and the physical top-partner mass is Mtp/Cos[thL]"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "sdl",
      "self_conjugate": true,
      "mass": {"sym": "Msd", "value": "500."},
      "width": {"sym": "Wsd", "value": "1."},
      "pdg": 9000001,
      "particle_name": "sdl",
      "full_name": "Dilaton",
      "propagator_label": "sdl",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Sng",
      "self_conjugate": true,
      "unphysical": true,
      "definitions": ["Sng -> fS + sdl"]
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "tp",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "Mtp", "value": "1500."},
      "width": {"sym": "Wtp", "value": "15."},
      "quantum_numbers": {"Q": "2/3"},
      "pdg": 6000006,
      "particle_name": "tp",
      "antiparticle_name": "tp~",
      "full_name": "Top partner",
      "propagator_label": "tp",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "TL",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "2/3"},
      "unphysical": true,
      "definitions": ["TL[sp1_, cc_] :> Module[{sp2}, ProjM[sp1, sp2] tp[sp2, cc]]"]
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "TR",
      "self_conjugate": false,
      "indices": ["Colour"],
      "quantum_numbers": {"Y": "2/3"},
      "unphysical": true,
      "definitions": ["TR[sp1_, cc_] :> Module[{sp2}, ProjP[sp1, sp2] tp[sp2, cc]]"]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LSkin",
      "expression": "Block[{mu}, ExpandIndices[1/2 del[Sng, mu] del[Sng, mu]]]",
      "delayed": true
    },
    {
      "name": "LSpot",
      "expression": "Block[{ii, jj}, ExpandIndices[-(mSsq/2 Sng^2 + lamS/24 Sng^4 + kap/2 Sng^2 Phibar[ii] Phi[ii] + mHsq Phibar[ii] Phi[ii] + lamH/4 Phibar[ii] Phi[ii] Phibar[jj] Phi[jj]), FlavorExpand -> SU2D]]",
      "delayed": true
    },
    {
      "name": "LHpotSM",
      "expression": "Block[{ii, jj}, ExpandIndices[muH^2 Phibar[ii] Phi[ii] - lam Phibar[ii] Phi[ii] Phibar[jj] Phi[jj], FlavorExpand -> SU2D]]",
      "delayed": true
    },
    {
      "name": "LTkin",
      "expression": "Block[{mu}, ExpandIndices[I TLbar.Ga[mu].DC[TL, mu] + I TRbar.Ga[mu].DC[TR, mu] - Mtp/fS Sng (TLbar.TR + TRbar.TL)]]",
      "delayed": true
    },
    {
      "name": "LTyuk",
      "expression": "Block[{sp, ii, jj, cc, yuk}, yuk = ExpandIndices[-yp TRbar[sp, cc].QL[sp, ii, 3, cc] Phi[jj] Eps[ii, jj], FlavorExpand -> SU2D]; yuk + HC[yuk]]",
      "delayed": true
    },
    {
      "name": "LMDM",
      "expression": "LSM - LHpotSM + LSkin + LSpot + LTkin + LTyuk",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```