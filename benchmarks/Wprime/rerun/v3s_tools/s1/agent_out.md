Read the paper (hep-ph/0207290, "Fully differential W′ production and decay at NLO in QCD"), the pydantic schema (`frmodel.py`), the renderer (`render.py`), and the SM.fr base model. No cached or reference `.fr` file for this model was present in the sandbox or read.

**Physics content of the paper.** The only new-physics Lagrangian is Eq. (2)/(4) (the left-right-notation rewrite, `\label{eq:lagrangian}`):
`L = (1/√2) f̄_i γ_μ (g_R e^{iω} cosζ V^R_{f_if_j} P_R + g_L sinζ V^L_{f_if_j} P_L) W′ f_j + H.c.`
This requires exactly two new states: (1) a new charged massive vector `W′` (spin V, EM charge +1, colour/SU(2) singlet, not itself gauged — it is a phenomenological resonance, consistent with `gauge_groups: []`), and (2) a new heavy SM-singlet Dirac fermion `NR` representing the paper's right-handed neutrino ν_R (needed so the right-handed lepton current `f̄ γ P_R f` is non-zero, since the SM has no right-handed neutrino component). New parameters: `gR`, `gL` (independent gauge couplings), `zeta` (L-R mixing angle), `omega` (CP phase absorbed into V^R), and two independent generalized-CKM matrices per sector (`VqR`,`VqL` for quarks, `VlR`,`VlL` for leptons), with the paper's own numeric benchmarks: the quark GCKM = the stated average CKM matrix with `|V'_tb|=1` (Eq. 12), and lepton GCKM = identity (paper states "we assume V′_lν is the identity matrix"). All couplings are dimensionless (d=4 vertices, no EFT cutoff needed — this is a renormalizable charged-current extension). Free-field kinetic+mass terms were added for both new states per the physics-completeness rules, and charge/Q-sum audited to zero on every vertex.

**Self-audit table**

| term | fields | d | coupling | coupling dim (4-d) | 1/Λ | Q sum | Y sum | SU(2) | SU(3) | new-U(1) | L/B | CC[] | frac/root check | HC partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpKin (kin) | Wpbar,Wp via FS | 4 | −1/2 | 0 ✓ | n/a | 0 (neutral bilinear) | n/a (ungauged V) | n/a | n/a | none | 0 | n/a | n/a | self-conj. bilinear |
| LWpKin (mass) | Wpbar,Wp | 2 | MWp² | 2 ✓ | n/a | 0 | n/a | n/a | n/a | none | 0 | n/a | n/a | self-conj. |
| LNRKin (kin) | NRbar,NR | 4 | I | 0 ✓ | n/a | 0 | n/a | n/a | singlet | none | 0 | n/a | n/a | self-conj. |
| LNRKin (mass) | NRbar,NR | 3 | MNR | 1 ✓ | n/a | 0 | n/a | n/a | singlet | none | 0 | n/a | n/a | self-conj. |
| LWpInt, uq-dq R | ūq,VqR,dq,Wp | 4 | gR e^{iω}cosζ | 0 ✓ | n/a | −2/3−1/3+1=0 ✓ | n/a | n/a | 3⊗3̄ singlet | none | 0 | n/a | 1/√2 read from `\frac{1}{\sqrt{2}}`, source line 91 | HC[] |
| LWpInt, uq-dq L | ūq,VqL,dq,Wp | 4 | gL sinζ | 0 ✓ | n/a | 0 ✓ | n/a | n/a | 3⊗3̄ singlet | none | 0 | n/a | same as above | HC[] |
| LWpInt, lep R | N̄R,VlR,l,Wp | 4 | gR e^{iω}cosζ | 0 ✓ | n/a | 0−1+1=0 ✓ | n/a | n/a | singlet | none | 0 | n/a | same | HC[] |
| LWpInt, lep L | v̄l,VlL,l,Wp | 4 | gL sinζ | 0 ✓ | n/a | 0−1+1=0 ✓ | n/a | n/a | singlet | none | 0 | n/a | same | HC[] |

- No `SelfConjugate -> True` class is declared (Wp, NR both self_conjugate=False); the line "confirms no QuantumNumbers on a self-conjugate class" is vacuously satisfied.
- Names chosen: `Wp`, `Wpbar`(auto), `NR`, `NRbar`(auto), `gR`, `gL`, `zeta`, `omega`, `VqR`, `VqL`, `VlR`, `VlL`, `MWp`, `WWp`, `MNR` — none is a Mathematica/FeynRules builtin (N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM) or an SM.fr name (H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,...); class indices are ≥100.
- Single total Lagrangian: `LTotal := LWpKin + LNRKin + LWpInt`.
- Reference/cached model file read: **none**.

```json
{
  "model_name": "Wprime_gen",
  "info": {
    "authors": ["Wprime_gen benchmark extraction"],
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
      "name": "gR",
      "parameter_type": "External",
      "value": "0.6532",
      "value_rules": [],
      "complex": null,
      "block_name": "WPRIME",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "indices": [],
      "definitions": [],
      "description": "Right-handed Wprime-fermion gauge coupling g_R, left-right notation Lagrangian (hep-ph/0207290, eq. defining C^R P_R + C^L P_L current); default = SM-size coupling g = sqrt(8 MW^2 GF/Sqrt[2])"
    },
    {
      "name": "gL",
      "parameter_type": "External",
      "value": "0.6532",
      "value_rules": [],
      "complex": null,
      "block_name": "WPRIME",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "indices": [],
      "definitions": [],
      "description": "Left-handed Wprime-fermion gauge coupling g_L, hep-ph/0207290 left-right notation Lagrangian"
    },
    {
      "name": "zeta",
      "parameter_type": "External",
      "value": "0.",
      "value_rules": [],
      "complex": null,
      "block_name": "WPRIME",
      "order_block": 3,
      "indices": [],
      "definitions": [],
      "description": "Left-right mixing angle zeta, hep-ph/0207290; default 0 realizes the paper's purely right-handed Wprime benchmark (cos[zeta]=1, sin[zeta]=0)"
    },
    {
      "name": "omega",
      "parameter_type": "External",
      "value": "0.",
      "value_rules": [],
      "complex": null,
      "block_name": "WPRIME",
      "order_block": 4,
      "indices": [],
      "definitions": [],
      "description": "CP-violating phase omega absorbed into V^R, hep-ph/0207290 left-right notation Lagrangian"
    },
    {
      "name": "VqR",
      "parameter_type": "External",
      "value_rules": [
        {"lhs": "VqR[1,1]", "rhs": "0.9751", "delayed": false},
        {"lhs": "VqR[1,2]", "rhs": "0.2215", "delayed": false},
        {"lhs": "VqR[1,3]", "rhs": "0.0035", "delayed": false},
        {"lhs": "VqR[2,1]", "rhs": "0.2210", "delayed": false},
        {"lhs": "VqR[2,2]", "rhs": "0.9743", "delayed": false},
        {"lhs": "VqR[2,3]", "rhs": "0.0410", "delayed": false},
        {"lhs": "VqR[3,1]", "rhs": "0.0090", "delayed": false},
        {"lhs": "VqR[3,2]", "rhs": "0.0400", "delayed": false},
        {"lhs": "VqR[3,3]", "rhs": "1.0000", "delayed": false}
      ],
      "complex": null,
      "indices": ["Generation", "Generation"],
      "definitions": [],
      "description": "Right-handed generalized CKM matrix V^R_qq' for quark currents, hep-ph/0207290 Eq.(12) average CKM benchmark with |V'_tb|=1 imposed"
    },
    {
      "name": "VqL",
      "parameter_type": "External",
      "value_rules": [
        {"lhs": "VqL[1,1]", "rhs": "0.9751", "delayed": false},
        {"lhs": "VqL[1,2]", "rhs": "0.2215", "delayed": false},
        {"lhs": "VqL[1,3]", "rhs": "0.0035", "delayed": false},
        {"lhs": "VqL[2,1]", "rhs": "0.2210", "delayed": false},
        {"lhs": "VqL[2,2]", "rhs": "0.9743", "delayed": false},
        {"lhs": "VqL[2,3]", "rhs": "0.0410", "delayed": false},
        {"lhs": "VqL[3,1]", "rhs": "0.0090", "delayed": false},
        {"lhs": "VqL[3,2]", "rhs": "0.0400", "delayed": false},
        {"lhs": "VqL[3,3]", "rhs": "1.0000", "delayed": false}
      ],
      "complex": null,
      "indices": ["Generation", "Generation"],
      "definitions": [],
      "description": "Left-handed generalized CKM matrix V^L_qq' for quark currents, hep-ph/0207290 Eq.(12) average CKM benchmark with |V'_tb|=1 imposed"
    },
    {
      "name": "VlR",
      "parameter_type": "External",
      "value_rules": [
        {"lhs": "VlR[1,1]", "rhs": "1.0", "delayed": false},
        {"lhs": "VlR[1,2]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlR[1,3]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlR[2,1]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlR[2,2]", "rhs": "1.0", "delayed": false},
        {"lhs": "VlR[2,3]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlR[3,1]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlR[3,2]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlR[3,3]", "rhs": "1.0", "delayed": false}
      ],
      "complex": null,
      "indices": ["Generation", "Generation"],
      "definitions": [],
      "description": "Right-handed generalized GCKM matrix V^R_lnu for lepton currents; hep-ph/0207290 states V'_lnu is assumed to be the identity matrix"
    },
    {
      "name": "VlL",
      "parameter_type": "External",
      "value_rules": [
        {"lhs": "VlL[1,1]", "rhs": "1.0", "delayed": false},
        {"lhs": "VlL[1,2]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlL[1,3]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlL[2,1]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlL[2,2]", "rhs": "1.0", "delayed": false},
        {"lhs": "VlL[2,3]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlL[3,1]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlL[3,2]", "rhs": "0.0", "delayed": false},
        {"lhs": "VlL[3,3]", "rhs": "1.0", "delayed": false}
      ],
      "complex": null,
      "indices": ["Generation", "Generation"],
      "definitions": [],
      "description": "Left-handed generalized GCKM matrix V^L_lnu for lepton currents; hep-ph/0207290 states V'_lnu is assumed to be the identity matrix"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "Wp",
      "self_conjugate": false,
      "indices": [],
      "flavor_index": null,
      "class_members": [],
      "mass": {"massless": false, "sym": "MWp", "value": "1500.", "members": []},
      "width": {"massless": false, "sym": "WWp", "value": "50.", "members": []},
      "quantum_numbers": {"Q": "1"},
      "pdg": 34,
      "particle_name": "Wp+",
      "antiparticle_name": "Wp-",
      "full_name": "Wprime",
      "propagator_label": "Wp",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": null,
      "chirality": null
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "NR",
      "self_conjugate": false,
      "indices": [],
      "flavor_index": null,
      "class_members": [],
      "mass": {"massless": false, "sym": "MNR", "value": "100.", "members": []},
      "width": {"massless": true, "sym": null, "value": null, "members": []},
      "quantum_numbers": {"LeptonNumber": "1"},
      "pdg": 9900012,
      "particle_name": "nr",
      "antiparticle_name": "nr~",
      "full_name": "Heavy (right-handed) neutrino",
      "propagator_label": "NR",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": null,
      "chirality": null
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LWpKin",
      "expression": "Block[{mu,nu}, ExpandIndices[ -1/2 FS[Wpbar,mu,nu] FS[Wp,mu,nu] + MWp^2 Wpbar[mu] Wp[mu] ] ];",
      "delayed": true
    },
    {
      "name": "LNRKin",
      "expression": "Block[{mu}, ExpandIndices[ I NRbar.Ga[mu].DC[NR,mu] - MNR NRbar.NR ] ];",
      "delayed": true
    },
    {
      "name": "LWpInt",
      "expression": "currWp + HC[currWp];",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LWpKin + LNRKin + LWpInt;",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": [
    "(* Wprime charged current, hep-ph/0207290 Eq.(4): (1/Sqrt[2]) fbar_i Ga[mu] (gR Exp[I omega] Cos[zeta] VR PR + gL Sin[zeta] VL PL) f_j Wp[mu] + H.c. *)\ncurrWp := Block[{mu}, ExpandIndices[ 1/Sqrt[2] ( gR*Exp[I*omega]*Cos[zeta]*uqbar.VqR.Ga[mu].ProjP.dq*Wp[mu] + gL*Sin[zeta]*uqbar.VqL.Ga[mu].ProjM.dq*Wp[mu] + gR*Exp[I*omega]*Cos[zeta]*NRbar.VlR.Ga[mu].ProjP.l*Wp[mu] + gL*Sin[zeta]*vlbar.VlL.Ga[mu].ProjM.l*Wp[mu] ) ] ];"
  ]
}
```