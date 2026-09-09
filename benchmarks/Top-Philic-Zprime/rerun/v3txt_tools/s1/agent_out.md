I have read the paper, the schema, the renderer, and SM.fr. The model content is entirely in Section 2 (Eqs. 2.1–2.3): one new colour-singlet neutral vector `V1` coupled to top quarks, with parameters `MV1`, `ct`, `theta`.

## Mandatory self-audit

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (=4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) charge sum | L/B sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV1kin (a) | `FS[V1,mu,nu] FS[V1,mu,nu]` | 4 | `-1/4` (pure number) | 0 = 4-4 OK | n/a | 0 | 0 | singlet, no SU(2) index | singlet, no colour index | none declared (V1 is not gauged; no new U(1) in the paper) | 0 | n/a | n/a | real field, term is self-conjugate |
| LV1kin (b) | `V1[mu] V1[mu]` | 2 | `1/2 MV1^2` | 2 = 4-2 OK | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | n/a | real field, self-conjugate |
| LV1int (L) | `tbar . Ga[mu] . ProjM . t  V1[mu]` | 4 | `cV1L = ct Cos[thV1]` | 0 = 4-4 OK | n/a | -2/3 + 2/3 + 0 = 0 | -1/6 + 1/6 + 0 = 0 | no SU(2) index; written in the broken-phase mass basis exactly as Eq.(2.1) (a top-philic simplified model; the left-handed current alone is not an unbroken SU(2)_L singlet, which is the paper's own convention) | `tbar_i t_i` shared Colour index, contracted implicitly (V1 is a colour singlet) | none | B: -1/3 + 1/3 = 0 | n/a (no `psi^c` in the paper) | Eq.(2.2) cross-check, see below | self-Hermitian: `(tbar Ga[mu] ProjM t)^dagger = tbar Ga[mu] ProjM t`, `cV1L` real, `V1` real. No `HC[]` needed |
| LV1int (R) | `tbar . Ga[mu] . ProjP . t  V1[mu]` | 4 | `cV1R = ct Sin[thV1]` | 0 = 4-4 OK | n/a | -2/3 + 2/3 + 0 = 0 | -2/3 + 2/3 + 0 = 0 (fully gauge invariant) | singlet (`tR` is an SU(2) singlet) | shared Colour index | none | 0 | n/a | Eq.(2.2) cross-check | self-Hermitian, no `HC[]` needed |
| free-field row: V1 | `LV1kin` exists with `Mass -> {MV1, 1500.}` and is summed in `LTotal` | - | - | - | - | - | - | - | - | - | - | - | - | - |
| colour-rep row | no field carries a non-fundamental colour index, so no `AddGaugeRepresentation[...]` line is needed | - | - | - | - | - | - | - | - | - | - | - | - | - |

Fraction and root placement (rule 7): no LaTeX source is present in the sandbox, so I cross-checked Eq.(2.2) against two independent facts. (a) The paper's own statement `Gamma/MV1 = ct^2/(8 Pi)` for `mt << MV1` fixes the coefficient as `ct^2 MV1 / (8 Pi)` (numerator `ct^2 MV1`, denominator `8 Pi`), and fixes the square root to cover only `1 - 4 mt^2/MV1^2`. (b) The bracket `[1 - (mt^2/MV1^2)(1 - 3 Sin[2 theta])]` reproduces the known two-body widths: at `theta = Pi/4` (pure vector) it gives `(1 + 2 mt^2/M^2) Sqrt[1-4mt^2/M^2]`, at `theta = 3Pi/4` (pure axial) it gives `(1 - 4mt^2/M^2)^(3/2)`, both with the colour factor `Nc = 3` included. This is the placement I used for `WV1`.

Self-conjugate classes: `V1` is the only `SelfConjugate -> True` class, and it carries no `QuantumNumbers` (it is neutral and a colour singlet).

Names: classes `V1`; parameters `ct`, `thV1`, `cV1L`, `cV1R`, `MV1`, `WV1`; indices: none new. None is a Mathematica built-in, a FeynRules symbol, or a name declared by SM.fr, and none contains a prime or punctuation.

Total Lagrangian: `LTotal := LV1kin + LV1int`, which sums every other term defined (`LV1kin`, `LV1int`).

Eq.(2.3) is deliberately not emitted: it is the contact operator obtained by integrating `V1` out, so adding it next to the resonance would double count the same physics. It is recorded in the description of `ct`.

Reference or cached model file read: none. I read only the paper text, `tools/frgen/frmodel.py`, `tools/frgen/render.py`, and `tools/feynrules/test_files/models/SM.fr` (the SM base file the add-on loads on).

```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": ["J. H. Kim", "K. Kong", "S. J. Lee", "G. Mohlabeng"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": ["KAIST / IBS CTPU", "University of Kansas", "Korea University / KIAS", "Fermilab"],
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
      "description": "Overall top-philic coupling strength, ct = Sqrt[cL^2 + cR^2], Eq.(2.1); dimensionless; benchmark value ct = 2.0 (Fig.2, Tables VI, IX, XII). The contact operator of Eq.(2.3) is ct^2/(2 MV1^2) and is NOT added separately, since it is V1 integrated out."
    },
    {
      "name": "thV1",
      "parameter_type": "External",
      "value": "1.570796326794897",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "theta",
      "description": "Chirality angle theta of Eq.(2.1), Tan[theta] = cR/cL; dimensionless; the paper sets theta = Pi/2 (purely right-handed top coupling); theta = 3Pi/4 is the axial limit."
    },
    {
      "name": "cV1L",
      "parameter_type": "Internal",
      "value": "ct*Cos[thV1]",
      "interaction_order": ["NP", 1],
      "tex": "c_L",
      "description": "Left-handed V1-top-top coupling, cL = ct Cos[theta], Eq.(2.1)"
    },
    {
      "name": "cV1R",
      "parameter_type": "Internal",
      "value": "ct*Sin[thV1]",
      "interaction_order": ["NP", 1],
      "tex": "c_R",
      "description": "Right-handed V1-top-top coupling, cR = ct Sin[theta], Eq.(2.1)"
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2*MV1/(8*Pi)*Sqrt[1 - 4*MT^2/MV1^2]*(1 - MT^2/MV1^2*(1 - 3*Sin[2*thV1]))",
      "tex": "\\Gamma_{V_1}",
      "description": "Total width of V1, Gamma(V1 -> t tbar) of Eq.(2.2), colour factor Nc = 3 included; reduces to ct^2 MV1/(8 Pi) for MT << MV1; about 229 GeV at MV1 = 1500 GeV, ct = 2, theta = Pi/2"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MV1", "value": "1500."},
      "width": {"sym": "WV1", "value": "Internal"},
      "quantum_numbers": {},
      "pdg": 32,
      "particle_name": "V1",
      "full_name": "TopPhilicVectorResonance",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1kin",
      "expression": "-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]",
      "delayed": true
    },
    {
      "name": "LV1int",
      "expression": "cV1L tbar.Ga[mu].ProjM.t V1[mu] + cV1R tbar.Ga[mu].ProjP.t V1[mu]",
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