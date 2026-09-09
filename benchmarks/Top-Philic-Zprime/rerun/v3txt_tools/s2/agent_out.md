I read the paper, the schema, the renderer, and SM.fr. The paper (arXiv:1604.07421) adds exactly **one** new state beyond the SM: a colour-singlet, electrically neutral, **real (self-conjugate) massive vector** `V1` that couples only to the top quark, Eq. (2.1), with three free parameters `MV1`, `ct`, `theta`. Eq. (2.3) is the four-top contact operator obtained by *integrating out* `V1` at `theta = Pi/2`; it is a derived low-energy limit of Eq. (2.1), so emitting it as well would double count and it is not implemented.

## Mandatory self-audit table

| term name | fields in the monomial | d | coupling symbol | coupling dim (=4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) charge sum | L/B sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV1Kin (a) | `FS[V1,mu,nu] FS[V1,mu,nu]` | 4 | `-1/4` | 0 ✓ | n/a (d=4) | 0+0=0 ✓ | 0+0=0 ✓ | singlet, no doublet index | singlet, no colour index | none (no new U(1)) | 0 | n/a | n/a | self-conjugate (real field, term real) |
| LV1Kin (b) | `V1[mu] V1[mu]` | 2 | `1/2 MV1^2` | 2 ✓ | n/a (d=2) | 0+0=0 ✓ | 0+0=0 ✓ | singlet | singlet | none | 0 | n/a | n/a | self-conjugate |
| LV1Top (L) | `tbar.Ga[mu].ProjM.t V1[mu]` | 4 | `cLt` | 0 ✓ | n/a (d=4) | -2/3+2/3+0=0 ✓ | -1/6+1/6+0=0 ✓ | singlet: chirality-diagonal bilinear of the physical top, no doublet index, no Eps | `tbar[cc] ... t[cc]`, implicit colour contraction -> singlet | none | B: -1/3+1/3=0 ✓ | n/a (paper writes no `psi^c`) | n/a (no fraction/root in this coefficient) | Hermitian by itself: `(tbar Ga[mu] ProjM t)^dag = tbar Ga[mu] ProjM t`, `V1` real -> no `HC[]` |
| LV1Top (R) | `tbar.Ga[mu].ProjP.t V1[mu]` | 4 | `cRt` | 0 ✓ | n/a (d=4) | -2/3+2/3+0=0 ✓ | -2/3+2/3+0=0 ✓ | singlet, same as above | implicit colour contraction -> singlet | none | B: -1/3+1/3=0 ✓ | n/a | n/a | Hermitian by itself -> no `HC[]` |
| per-class kinetic+mass check | class `V1` | - | - | - | - | - | - | - | - | - | - | - | - | `LV1Kin` exists and is summed in `LTotal` ✓ |
| colour representation check | - | - | - | - | - | - | - | - | only `Colour` (SM triplet) is used; no sextet or other non-fundamental rep -> no `AddGaugeRepresentation[...]` line needed ✓ | - | - | - | - | - |

Fraction/root placement (rule 7) for the one coefficient that has them, the width `WV1` from Eq. (2.2): no `*_source.tex` exists in the sandbox, so I cross-checked the flattened text two ways. (1) The paper's own sentence right below Eq. (2.2): "For mt << MV1, Gamma/MV1 ~ ct^2/(8 Pi)" fixes the prefactor as `ct^2 MV1/(8 Pi)` (numerator `ct^2 MV1`, denominator `8 Pi`), not `ct^2 MV1 8 Pi`. (2) The standard `V -> f fbar` width with `Nc = 3`, `gV^2 = ct^2 (1 + Sin[2 theta])/4`, `gA^2 = ct^2 (1 - Sin[2 theta])/4` reproduces `(ct^2 MV1/(8 Pi)) Sqrt[1 - 4 mt^2/MV1^2] (1 - (mt^2/MV1^2)(1 - 3 Sin[2 theta]))` exactly, confirming both the radical `Sqrt[1 - 4 mt^2/MV1^2]` and the bracket.

- `SelfConjugate -> True` classes: `V1` only. It carries **no** `QuantumNumbers` (its Q and Y are both 0). ✓
- Names chosen: classes `V1`; parameters `MV1`, `WV1`, `ct`, `thetat`, `cLt`, `cRt`; indices: none new. None is a Mathematica built-in, a FeynRules symbol (`N C D E I K O HC CC FS DC del Eps Ga ProjP ProjM`), or an SM.fr name (`H Phi Z W A G ee gs gw sw cw vev MZ MW ...`). No primes or punctuation in `ParticleName`. Class index is 100. ✓
- Single total Lagrangian: `LTotal := LV1Kin + LV1Top` — it sums every other term defined (`LV1Kin`, `LV1Top`), and no term is a pure constant. ✓
- Reference or cached model file read: **none**. Only the paper text, `frmodel.py`, `render.py` and `SM.fr` were opened.
- New U(1) charges (rule 5): the paper introduces **no** new gauged U(1); `V1` is a simplified-model massive vector with no charge assignments to SM fields, so no charge table had to be re-derived. Explicit cutoffs (rule 2): none — Eq. (2.1) is renormalizable, every operator has d = 4.

```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": ["J. H. Kim", "K. Kong", "S. J. Lee", "G. Mohlabeng"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": [
      "KAIST and IBS Center for Theoretical Physics of the Universe",
      "University of Kansas",
      "Korea University and KIAS",
      "Fermilab"
    ],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "ct",
      "parameter_type": "External",
      "value": "2.0",
      "block_name": "TOPPHILIC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "c_t",
      "description": "Overall top-philic coupling strength, ct = Sqrt[cL^2 + cR^2], Eq.(2.1); benchmark ct = 2.0 (Fig.2, Tables VI, IX, XII)"
    },
    {
      "name": "thetat",
      "parameter_type": "External",
      "value": "1.570796326794897",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "\\theta",
      "description": "Chirality angle, Tan[thetat] = cR/cL, Eq.(2.1); benchmark thetat = Pi/2 (purely right-handed top coupling), section 2.2"
    },
    {
      "name": "cLt",
      "parameter_type": "Internal",
      "value": "ct Cos[thetat]",
      "interaction_order": ["NP", 1],
      "tex": "c_L",
      "description": "Left-handed top coupling of the vector resonance, cL = ct Cos[thetat], Eq.(2.1)"
    },
    {
      "name": "cRt",
      "parameter_type": "Internal",
      "value": "ct Sin[thetat]",
      "interaction_order": ["NP", 1],
      "tex": "c_R",
      "description": "Right-handed top coupling of the vector resonance, cR = ct Sin[thetat], Eq.(2.1)"
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2 MV1/(8 Pi) Sqrt[1 - 4 MT^2/MV1^2] (1 - MT^2/MV1^2 (1 - 3 Sin[2 thetat]))",
      "tex": "\\Gamma_{V_1}",
      "description": "Total width of V1, equal to Gamma(V1 -> t tbar) of Eq.(2.2); reduces to ct^2 MV1/(8 Pi) for MT << MV1 as stated below Eq.(2.2)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {"massless": false, "sym": "MV1", "value": "1500."},
      "width": {"massless": false, "sym": "WV1", "value": "Internal"},
      "quantum_numbers": {},
      "pdg": 32,
      "particle_name": "v1",
      "full_name": "Topphilic vector resonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None",
      "unphysical": false
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "Block[{mu, nu}, -1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]]",
      "delayed": true
    },
    {
      "name": "LV1Top",
      "expression": "Block[{mu}, cLt tbar.Ga[mu].ProjM.t V1[mu] + cRt tbar.Ga[mu].ProjP.t V1[mu]]",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LV1Kin + LV1Top",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```