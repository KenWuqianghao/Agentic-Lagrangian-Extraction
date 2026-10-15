## Self‑audit (Top‑Philic‑Zprime, based on arXiv:1604.07421)

The paper defines exactly **one** new state, a colour‑singlet, SU(2)‑singlet, electrically‑neutral real vector `V1` (Eq. 1), with a purely phenomenological chiral coupling to the top‑quark mass eigenstate only. The authors explicitly state they do **not** assume any gauge‑invariant UV completion ("we do not consider any underlying or fundamental theory which might generate Eq. (1)"), so the interaction is written directly in the broken (mass) basis, coupling only to the SM class member `t` (not the `uq` class with a free generation index, and not the `QL`/`uR` SU(2) objects).

| term name | fields in monomial | operator dim d | coupling symbol | coupling dim (4‑d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new‑U(1) sum | B/L sum | CC[] used | fraction/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV1kin | V1, V1 | 4 | none (kinetic norm.) | 0 | n/a (d≤4) | 0 | 0 | singlet | singlet | n/a (no new U(1)) | n/a | n/a | n/a (standard Proca form, Eq. matches schema template) | self‑conjugate |
| LV1int | tbar, t, V1 | 3/2+3/2+1=4 | cL, cR | 0 (=4‑4) | n/a (d≤4) | 0 (Q(t)+Q(tbar)+Q(V1)=2/3‑2/3+0) | n/a — written directly in mass basis, not SU(2)×U(1) covariant (paper's explicit disclaimer, Sec. II) | n/a — no SU(2) structure; term uses mass‑eigenstate `t` only, per paper's stated model‑independence | colour singlet (tbar·t triplet‑antitriplet contraction, Dot notation) | n/a (no new gauge U(1)) | 0 (B(t)+B(tbar)=1/3‑1/3) | no | n/a — cL=ct·Cosθ, cR=ct·Sinθ read verbatim off Eq. (1), no flattened fraction | self‑Hermitian (vector+axial‑vector combination with real cL,cR is automatically Hermitian; no separate HC[] needed) |

Additional required lines:
- Kinetic+mass confirmation: `V1` (the only new particle class) has its free‑field term `LV1kin` (kinetic `-1/4 FS.FS` + mass `1/2 MV1^2 V1.V1`), included in `LTotal`.
- Non‑fundamental colour representations: none used — n/a, no `AddGaugeRepresentation[...]` needed.
- `SelfConjugate -> True` classes: `V1` only; it carries no `QuantumNumbers` (empty).
- Name check: chosen names `V1`, `MV1`, `WV1`, `ct`, `theta`, `cL`, `cR` — none is a Mathematica built‑in, a FeynRules symbol (`N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM`), or an SM.fr name (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,...`).
- Single total Lagrangian: `LTotal := LV1kin + LV1int` — sums both new terms; no alternative total defined.
- Reference/cached model file read: none.

```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:1604.07421 (Kim, Kong, Lee, Mohlabeng)"],
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
      "name": "ct",
      "parameter_type": "External",
      "value": "2.0",
      "block_name": "NPINPUT",
      "order_block": 1,
      "description": "Overall V1-top coupling strength, ct = Sqrt[cL^2+cR^2], Eq.(1)-(2); benchmark value c_t=2.0"
    },
    {
      "name": "theta",
      "parameter_type": "External",
      "value": "Pi/2",
      "block_name": "NPINPUT",
      "order_block": 2,
      "description": "Chirality angle of the V1-t-t coupling, tan(theta)=cR/cL, Eq.(1); paper sets theta=Pi/2 for the main analysis"
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[theta]",
      "interaction_order": ["NP", 1],
      "description": "Left-handed V1-t-t coupling, cL = ct*Cos[theta], Eq.(1)"
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[theta]",
      "interaction_order": ["NP", 1],
      "description": "Right-handed V1-t-t coupling, cR = ct*Sin[theta], Eq.(1)"
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "(ct^2*MV1)/(8*Pi) * Sqrt[1 - 4*MT^2/MV1^2] * (1 - (MT^2/MV1^2)*(1 - 3*Sin[2*theta]))",
      "description": "Total width of V1 (dominant V1 -> t tbar decay), Eq.(2)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "V1",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MV1", "value": "1500."},
      "width": {"sym": "WV1", "value": "Internal"},
      "quantum_numbers": {},
      "pdg": 9000005,
      "particle_name": "V1",
      "full_name": "Top-philic colour-singlet vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LV1kin",
      "expression": "Block[{mu,nu}, -1/4 FS[V1,mu,nu] FS[V1,mu,nu] + 1/2 MV1^2 V1[mu] V1[mu]]",
      "delayed": true
    },
    {
      "name": "LV1int",
      "expression": "Block[{mu}, tbar.Ga[mu].(cL*ProjM + cR*ProjP).t V1[mu]]",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LV1kin + LV1int",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```