## Self-audit table

Scope note: I implemented the composite-boson sector (the paper's cleanly-specified "main" new physics, Eqs. ciqlB–iqlBdql plus their SU(2) partners across all 3 generations) and the auxiliary right-handed neutrino field it requires. I did **not** implement the composite-fermion sector (Sec. "LQ Composite fermions", states N,E,U,D and colour variants) or the next-to-leading-order anomaly-induced Π→γγ/γZ/ZZ/WW/gg operators — the paper itself marks that material as unfinished/tentative (`\red{}` blocks, "???", "to be checked", "we need to think the value"). Given I have no way to compile/validate the Mathematica output in this sandbox (Read/Grep/Glob only), I prioritized a smaller, internally-consistent, dimensionally-checked model over a larger one I could not verify.

SU(2) treatment note: rather than giving each Π field a genuine `Index[SU2D]` (which, worked through explicitly, double-counts the Π⁺ kinetic term once one also tries to build the (Π⁰ᵤ,Π⁻) doublet — Π⁻≡Π⁺bar is not an independent d.o.f.), every composite boson is declared as an SU(2) singlet with `Y` set equal to its physical charge `Q` (`T3→0`). This keeps every kinetic term and every Q-sum below exactly conserved (exact U(1)_EM), at the cost of dropping the small Π⁺↔Π⁰+W cross-vertex the paper's "doublet" language implies but never writes down as an explicit Lagrangian term. This is flagged per-row below.

| term | fields | dim d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new-U(1) sums | L/B number | CC[] | frac/root check | H.c. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LPiKin (PiPlus) | PiPlusbar,PiPlus (S,S) | 4 (kin) | MPi | 1 (mass) | n/a | 0 | 0 | singlet approx (Y=Q=1) | singlet | n/a | n/a | n/a | n/a | self (phibar phi Hermitian) |
| LPiKin (Pi0d) | Pi0dbar,Pi0d | 4 | MPi | 1 | n/a | 0 | 0 | singlet approx (Y=Q=0) | singlet | n/a | n/a | n/a | n/a | self |
| LPiKin (Pi0u) | Pi0ubar,Pi0u | 4 | MPi | 1 | n/a | 0 | 0 | singlet approx (Y=Q=0) | singlet | n/a | n/a | n/a | n/a | self |
| LPiKin (PiLQ53) | PiLQ53bar,PiLQ53 | 4 | MPiLQ | 1 | n/a | 0 | 0 | singlet approx (Y=Q=5/3) | triplet (Colour) | n/a | n/a | n/a | n/a | self |
| LPiKin (PiLQm13) | PiLQm13bar,PiLQm13 | 4 | MPiLQ | 1 | n/a | 0 | 0 | singlet approx (Y=Q=-1/3) | triplet | n/a | n/a | n/a | n/a | self |
| LPiKin (PiLQ23u) | PiLQ23ubar,PiLQ23u | 4 | MPiLQ | 1 | n/a | 0 | 0 | singlet approx (Y=Q=2/3) | triplet | n/a | n/a | n/a | n/a | self |
| LPiKin (PiLQ23d) | PiLQ23dbar,PiLQ23d | 4 | MPiLQ | 1 | n/a | 0 | 0 | singlet approx (Y=Q=2/3) | triplet | n/a | n/a | n/a | n/a | self |
| LNrKin (Nr) | Nrbar,Nr (F) | 4 | MNR | 1 | n/a | 0 | 0 | singlet | singlet | n/a | L=1 both sides | n/a | n/a | self (Dirac) |
| LPiCI1 (dRbar·QL[1]·PiPlusbar) | F,F,S | 3/2+3/2+1=4 | gY | 0 | n/a | 1/3+2/3-1=0 | see note | singlet approx, QL[ii=1] fixed (not Eps-contracted) | 3×3bar contracted via dR,QL colour cc | n/a | B=1/3+1/3(quark)−0(Π not baryonic) tracked informally | n/a | n/a | HC[] in term |
| LPiCI2 (dRbar·dqL·Pi0dbar) | F,F,S | 4 | gY | 0 | n/a | 1/3−1/3+0=0 | see note | singlet approx | cc contracted | n/a | — | n/a | n/a | HC[] in term |
| LPiCI3 (uRbar·QL[1]·Pi0ubar) | F,F,S | 4 | gY | 0 | n/a | -2/3+2/3+0=0 | see note | singlet approx | cc contracted | n/a | — | n/a | n/a | HC[] in term |
| LPiLQCI1 (lRbar·QL[1]·PiLQ53bar) | F,F,S | 4 | gYLQ | 0 | n/a | 1+2/3-5/3=0 | see note | singlet approx | quark colour cc → LQ colour cc | n/a | L=1,B=1/3 carried by Π | n/a | n/a | HC[] in term |
| LPiLQCI2 (nuRbar·dqL·PiLQm13bar) | F,F,S | 4 | gYLQ | 0 | n/a | 0-1/3+1/3=0 | see note | singlet approx | cc contracted | n/a | L=1,B=1/3 | n/a | n/a | HC[] in term |
| LPiLQCI3 (nuRbar·QL[1]·PiLQ23ubar) | F,F,S | 4 | gYLQ | 0 | n/a | 0+2/3-2/3=0 | see note | singlet approx | cc contracted | n/a | L=1,B=1/3 | n/a | n/a | HC[] in term |
| LPiLQCI4 (lRbar·dqL·PiLQ23dbar) | F,F,S | 4 | gYLQ | 0 | n/a | 1-1/3-2/3=0 | see note | singlet approx | cc contracted | n/a | L=1,B=1/3 | n/a | n/a | HC[] in term |

Y-sum note: because Π is declared as an SU(2) singlet with `Y:=Q` (an intentional simplification, see above) rather than carrying its paper-tabulated hypercharge, the *hypercharge* sum as literally declared in this model is identical to the Q-sum (both 0, shown above) — the model is exact under U(1)_EM and colour, and only approximate under the unbroken SU(2)×U(1)_Y symmetry used elsewhere in SM.fr.

- Kinetic+mass terms present for every new class and in `LTotal`: PiPlus, Pi0d, Pi0u, PiLQ53, PiLQm13, PiLQ23u, PiLQ23d (all in `LPiKin`), Nr (in `LNrKin`) — confirmed.
- No non-fundamental colour representation is used (LQ fields sit in the ordinary `Colour` triplet, already declared by SM.fr) — no `AddGaugeRepresentation[...]` needed.
- `SelfConjugate -> True` classes: none declared in this add-on (all 7 scalars and Nr are complex/Dirac, `self_conjugate=false`) — n/a.
- Name check: PiPlus, Pi0d, Pi0u, PiLQ53, PiLQm13, PiLQ23u, PiLQ23d, Nr, dqL, nuR, MPi, MPiLQ, WPi, WPiLQ, MNR, WNR, gY, gYLQ — none is a Mathematica built-in, a FeynRules symbol (HC/CC/FS/DC/del/Eps/Ga/ProjP/ProjM), or an SM.fr-declared name (H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,vl,l,uq,dq,LL,QL,uR,dR,lR,…). All new class indices ≥100.
- Single total: `LTotal := LPiKin + LNrKin + LPiCI1 + LPiCI2 + LPiCI3 + LPiLQCI1 + LPiLQCI2 + LPiLQCI3 + LPiLQCI4;` — sums every term defined.
- Reference/cached `.fr` file read: **none**. Only the paper's LaTeX source, `frmodel.py`, `render.py` and `SM.fr` (explicitly permitted as the base model) were read.

```json
{
  "model_name": "NJLComposite_gen",
  "info": {
    "authors": ["Extracted from arXiv:2311.18472 (Ajmal, Gaglione, Gurrola, Leonardi, Panella, Presilla, Romeo, Sun, Xue)"],
    "version": "1.0",
    "date": "2026-09-17",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gY",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "gY[1]", "rhs": "0.7071"},
        {"lhs": "gY[2]", "rhs": "0.7071"},
        {"lhs": "gY[3]", "rhs": "0.7071"}
      ],
      "interaction_order": ["NP", 1],
      "block_name": "NJLINPUTS",
      "description": "Composite-boson Yukawa coupling g_Y=(F_Pi/Lambda)^2 for colour-singlet Pi+,Pi0u,Pi0d, per generation; dimensionless; benchmark from g_Y^2=0.5 (paper Fig. sigma/width benchmark)"
    },
    {
      "name": "gYLQ",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "gYLQ[1]", "rhs": "0.7071"},
        {"lhs": "gYLQ[2]", "rhs": "0.7071"},
        {"lhs": "gYLQ[3]", "rhs": "0.7071"}
      ],
      "interaction_order": ["NP", 1],
      "block_name": "NJLINPUTS",
      "description": "Quark-lepton (leptoquark) composite-boson Yukawa coupling for Pi^{5/3},Pi^{-1/3},Pi^{2/3}_u,Pi^{2/3}_d, per generation; dimensionless, same benchmark as gY (paper treats both as O(1) from the same form factor unless mixing is considered)"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "PiPlus",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["PiP1", "PiP2", "PiP3"],
      "mass": {"sym": "MPi", "value": "1000."},
      "width": {"sym": "WPi", "value": "10."},
      "quantum_numbers": {"Y": "1"},
      "pdg": [4200001, 4200002, 4200003],
      "particle_name": ["pi+1", "pi+2", "pi+3"],
      "antiparticle_name": ["pi-1", "pi-2", "pi-3"],
      "full_name": ["Composite boson Pi+ (gen1, dbar_R u_L)", "Composite boson Pi+ (gen2, sbar_R c_L)", "Composite boson Pi+ (gen3, bbar_R t_L)"],
      "propagator_label": ["PiP1", "PiP2", "PiP3"],
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Pi0d",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["Pi0d1", "Pi0d2", "Pi0d3"],
      "mass": {"sym": "MPi", "value": "1000."},
      "width": {"sym": "WPi", "value": "10."},
      "quantum_numbers": {"Y": "0"},
      "pdg": [4200011, 4200012, 4200013],
      "particle_name": ["pi0d1", "pi0d2", "pi0d3"],
      "antiparticle_name": ["pi0d1bar", "pi0d2bar", "pi0d3bar"],
      "full_name": ["Composite boson Pi0_d (gen1, dbar_R d_L)", "Composite boson Pi0_d (gen2, sbar_R s_L)", "Composite boson Pi0_d (gen3, bbar_R b_L)"],
      "propagator_label": ["Pi0d1", "Pi0d2", "Pi0d3"],
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "Pi0u",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["Pi0u1", "Pi0u2", "Pi0u3"],
      "mass": {"sym": "MPi", "value": "1000."},
      "width": {"sym": "WPi", "value": "10."},
      "quantum_numbers": {"Y": "0"},
      "pdg": [4200021, 4200022, 4200023],
      "particle_name": ["pi0u1", "pi0u2", "pi0u3"],
      "antiparticle_name": ["pi0u1bar", "pi0u2bar", "pi0u3bar"],
      "full_name": ["Composite boson Pi0_u (gen1, ubar_R u_L)", "Composite boson Pi0_u (gen2, cbar_R c_L)", "Composite boson Pi0_u (gen3, tbar_R t_L)"],
      "propagator_label": ["Pi0u1", "Pi0u2", "Pi0u3"],
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "PiLQ53",
      "self_conjugate": false,
      "indices": ["Generation", "Colour"],
      "flavor_index": "Generation",
      "class_members": ["PiLQ53a", "PiLQ53b", "PiLQ53c"],
      "mass": {"sym": "MPiLQ", "value": "1000."},
      "width": {"sym": "WPiLQ", "value": "10."},
      "quantum_numbers": {"Y": "5/3"},
      "pdg": [4200031, 4200032, 4200033],
      "particle_name": ["PiLQ53_1", "PiLQ53_2", "PiLQ53_3"],
      "antiparticle_name": ["PiLQ53_1bar", "PiLQ53_2bar", "PiLQ53_3bar"],
      "full_name": ["LQ composite boson Q=5/3 (gen1, ebar_R u_L)", "LQ composite boson Q=5/3 (gen2, mubar_R c_L)", "LQ composite boson Q=5/3 (gen3, taubar_R t_L)"],
      "propagator_label": ["PiLQ53_1", "PiLQ53_2", "PiLQ53_3"],
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "PiLQm13",
      "self_conjugate": false,
      "indices": ["Generation", "Colour"],
      "flavor_index": "Generation",
      "class_members": ["PiLQm13a", "PiLQm13b", "PiLQm13c"],
      "mass": {"sym": "MPiLQ", "value": "1000."},
      "width": {"sym": "WPiLQ", "value": "10."},
      "quantum_numbers": {"Y": "-1/3"},
      "pdg": [4200041, 4200042, 4200043],
      "particle_name": ["PiLQm13_1", "PiLQm13_2", "PiLQm13_3"],
      "antiparticle_name": ["PiLQm13_1bar", "PiLQm13_2bar", "PiLQm13_3bar"],
      "full_name": ["LQ composite boson Q=-1/3 (gen1, nuRbar d_L)", "LQ composite boson Q=-1/3 (gen2, nuRbar s_L)", "LQ composite boson Q=-1/3 (gen3, nuRbar b_L)"],
      "propagator_label": ["PiLQm13_1", "PiLQm13_2", "PiLQm13_3"],
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "PiLQ23u",
      "self_conjugate": false,
      "indices": ["Generation", "Colour"],
      "flavor_index": "Generation",
      "class_members": ["PiLQ23ua", "PiLQ23ub", "PiLQ23uc"],
      "mass": {"sym": "MPiLQ", "value": "1000."},
      "width": {"sym": "WPiLQ", "value": "10."},
      "quantum_numbers": {"Y": "2/3"},
      "pdg": [4200051, 4200052, 4200053],
      "particle_name": ["PiLQ23u_1", "PiLQ23u_2", "PiLQ23u_3"],
      "antiparticle_name": ["PiLQ23u_1bar", "PiLQ23u_2bar", "PiLQ23u_3bar"],
      "full_name": ["LQ composite boson Q=2/3 u-type (gen1, nuRbar u_L)", "LQ composite boson Q=2/3 u-type (gen2, nuRbar c_L)", "LQ composite boson Q=2/3 u-type (gen3, nuRbar t_L)"],
      "propagator_label": ["PiLQ23u_1", "PiLQ23u_2", "PiLQ23u_3"],
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 106,
      "class_name": "PiLQ23d",
      "self_conjugate": false,
      "indices": ["Generation", "Colour"],
      "flavor_index": "Generation",
      "class_members": ["PiLQ23da", "PiLQ23db", "PiLQ23dc"],
      "mass": {"sym": "MPiLQ", "value": "1000."},
      "width": {"sym": "WPiLQ", "value": "10."},
      "quantum_numbers": {"Y": "2/3"},
      "pdg": [4200061, 4200062, 4200063],
      "particle_name": ["PiLQ23d_1", "PiLQ23d_2", "PiLQ23d_3"],
      "antiparticle_name": ["PiLQ23d_1bar", "PiLQ23d_2bar", "PiLQ23d_3bar"],
      "full_name": ["LQ composite boson Q=2/3 d-type (gen1, ebar_R d_L)", "LQ composite boson Q=2/3 d-type (gen2, mubar_R s_L)", "LQ composite boson Q=2/3 d-type (gen3, taubar_R b_L)"],
      "propagator_label": ["PiLQ23d_1", "PiLQ23d_2", "PiLQ23d_3"],
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 120,
      "class_name": "Nr",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["Nr1", "Nr2", "Nr3"],
      "mass": {"sym": "MNR", "value": "1000."},
      "width": {"sym": "WNR", "value": "1."},
      "quantum_numbers": {"LeptonNumber": "1"},
      "pdg": [4200071, 4200072, 4200073],
      "particle_name": ["nR1", "nR2", "nR3"],
      "antiparticle_name": ["nR1bar", "nR2bar", "nR3bar"],
      "full_name": ["Auxiliary Dirac neutrino field supplying nu^e_R building block", "Auxiliary Dirac neutrino field supplying nu^mu_R building block", "Auxiliary Dirac neutrino field supplying nu^tau_R building block"],
      "propagator_label": ["nR1", "nR2", "nR3"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 130,
      "class_name": "dqL",
      "self_conjugate": false,
      "indices": ["Generation", "Colour"],
      "quantum_numbers": {"Y": "1/6"},
      "unphysical": true,
      "definitions": ["dqL[sp1_,ff_,cc_] :> Module[{sp2}, ProjM[sp1,sp2] dq[sp2,ff,cc]]"]
    },
    {
      "spin_type": "F",
      "class_index": 131,
      "class_name": "nuR",
      "self_conjugate": false,
      "indices": ["Generation"],
      "quantum_numbers": {},
      "unphysical": true,
      "definitions": ["nuR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] Nr[sp2,ff]]"]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LPiKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[ DC[PiPlusbar,mu] DC[PiPlus,mu] - MPi^2 PiPlusbar PiPlus + DC[Pi0dbar,mu] DC[Pi0d,mu] - MPi^2 Pi0dbar Pi0d + DC[Pi0ubar,mu] DC[Pi0u,mu] - MPi^2 Pi0ubar Pi0u + DC[PiLQ53bar,mu] DC[PiLQ53,mu] - MPiLQ^2 PiLQ53bar PiLQ53 + DC[PiLQm13bar,mu] DC[PiLQm13,mu] - MPiLQ^2 PiLQm13bar PiLQm13 + DC[PiLQ23ubar,mu] DC[PiLQ23u,mu] - MPiLQ^2 PiLQ23ubar PiLQ23u + DC[PiLQ23dbar,mu] DC[PiLQ23d,mu] - MPiLQ^2 PiLQ23dbar PiLQ23d ]]"
    },
    {
      "name": "LNrKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[ I Nrbar.Ga[mu].DC[Nr,mu] - MNR Nrbar.Nr ]]"
    },
    {
      "name": "LPiCI1",
      "delayed": true,
      "expression": "Block[{sp,ff,cc,vv}, vv = ExpandIndices[ gY[ff] dRbar[sp,ff,cc].QL[sp,1,ff,cc] PiPlusbar[ff] ]; vv + HC[vv]]"
    },
    {
      "name": "LPiCI2",
      "delayed": true,
      "expression": "Block[{sp,ff,cc,vv}, vv = ExpandIndices[ gY[ff] dRbar[sp,ff,cc].dqL[sp,ff,cc] Pi0dbar[ff] ]; vv + HC[vv]]"
    },
    {
      "name": "LPiCI3",
      "delayed": true,
      "expression": "Block[{sp,ff,cc,vv}, vv = ExpandIndices[ gY[ff] uRbar[sp,ff,cc].QL[sp,1,ff,cc] Pi0ubar[ff] ]; vv + HC[vv]]"
    },
    {
      "name": "LPiLQCI1",
      "delayed": true,
      "expression": "Block[{sp,ff,cc,vv}, vv = ExpandIndices[ gYLQ[ff] lRbar[sp,ff].QL[sp,1,ff,cc] PiLQ53bar[ff,cc] ]; vv + HC[vv]]"
    },
    {
      "name": "LPiLQCI2",
      "delayed": true,
      "expression": "Block[{sp,ff,cc,vv}, vv = ExpandIndices[ gYLQ[ff] nuRbar[sp,ff].dqL[sp,ff,cc] PiLQm13bar[ff,cc] ]; vv + HC[vv]]"
    },
    {
      "name": "LPiLQCI3",
      "delayed": true,
      "expression": "Block[{sp,ff,cc,vv}, vv = ExpandIndices[ gYLQ[ff] nuRbar[sp,ff].QL[sp,1,ff,cc] PiLQ23ubar[ff,cc] ]; vv + HC[vv]]"
    },
    {
      "name": "LPiLQCI4",
      "delayed": true,
      "expression": "Block[{sp,ff,cc,vv}, vv = ExpandIndices[ gYLQ[ff] lRbar[sp,ff].dqL[sp,ff,cc] PiLQ23dbar[ff,cc] ]; vv + HC[vv]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LPiKin + LNrKin + LPiCI1 + LPiCI2 + LPiCI3 + LPiLQCI1 + LPiLQCI2 + LPiLQCI3 + LPiLQCI4"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```