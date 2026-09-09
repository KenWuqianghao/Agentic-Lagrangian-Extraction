Read: paper LaTeX source (all 1092 lines), `frmodel.py`, `render.py`, `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox and none was read.

## Physics content found in the paper

The paper is a simplified model. Section II ("A Top-Philic Resonance: Simplified Model") holds all new-physics content:

- **One new state**: a colour-singlet, SU(2)-singlet, electrically neutral, **real vector** `V_1` (self-conjugate). No other new particle, multiplet, or generation appears anywhere in the paper.
- **Eq. (1)**, LaTeX lines 176-177: `L_int = tbar Ga_mu (cL PL + cR PR) t V1^mu = ct tbar Ga_mu (Cos[th] PL + Sin[th] PR) t V1^mu`.
- Line 181 (authoritative LaTeX): `c_t = Sqrt[(cL)^2 + (cR)^2]`, `Tan[th] = cR/cL`.
- **Eq. (2)**, LaTeX lines 186-187: `Gamma(V1 -> t tbar) = (c_t^2 M_V1/(8 Pi)) Sqrt[1 - 4 m_t^2/M_V1^2] [1 - (m_t^2/M_V1^2)(1 - 3 Sin[2 th])]`.
- Free parameters (line 221-222): `M_V1`, `c_t`, `th`. Benchmark: `M_V1 = 1.5 TeV`, `c_t = 2.0` (line 255), `th = Pi/2` (line 244).
- Eq. (3) (line 325) is **not** a separate operator: it is the four-top contact interaction obtained by integrating `V_1` out at `th = Pi/2`. Implementing it would double count, so it is not emitted; no EFT cutoff parameter is needed.

## Mandatory self-audit table

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV1Kin (kinetic) | `FS[V1,mu,nu] FS[V1,mu,nu]` | 4 | `-1/4` | 0 = 4-4 OK | n/a (d<=4) | 0+0=0 | 0+0=0 | singlet, no SU(2) index | singlet, no colour index | none declared (n/a) | 0 | n/a | n/a | self-conjugate (real field) |
| LV1Kin (mass) | `V1[mu] V1[mu]` | 2 | `1/2 MV1^2` | 2 = 4-2 OK | n/a | 0+0=0 | 0+0=0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LV1Top (L) | `tbar . Ga[mu] . ProjM . t V1[mu]` | 3/2+3/2+1 = 4 | `ctL` | 0 = 4-4 OK | n/a | -2/3 +2/3 +0 = 0 | tbar_L(-1/6)+t_L(+1/6)+0 = 0 | both are physical mass eigenstates, no SU(2) index; singlet | `tbar[cc] t[cc]`, implicit Colour delta (3bar x 3 -> 1) | n/a (no new gauge group) | B: -1/3+1/3 = 0; L: 0 | n/a (paper writes no `psi^c`) | Eq.(1) LaTeX 176-177 and `c_t = Sqrt[(cL)^2+(cR)^2]` LaTeX 181; cross-checked against Eq.(2) LaTeX 186-187, where the coefficient is `\frac{c_t^2 M_{V_1}}{8\pi}\sqrt{1-\frac{4m_t^2}{M_{V_1}^2}}` (root multiplies, not divides) | self-conjugate: `(psibar Ga[mu] ProjM psi)^dag = psibar Ga[mu] ProjM psi` with real `ctL` and real `V1`; no `HC[]` needed |
| LV1Top (R) | `tbar . Ga[mu] . ProjP . t V1[mu]` | 4 | `ctR` | 0 = 4-4 OK | n/a | -2/3 +2/3 +0 = 0 | tbar_R(-2/3)+t_R(+2/3)+0 = 0 | singlet | implicit Colour delta | n/a | 0 | n/a | same as above; `Tan[th] = cR/cL` LaTeX 181 | self-conjugate, real `ctR` |
| per-class free-field row: `V1` | `LV1Kin` gives kinetic + mass with the declared `Mass -> {MV1, 1500.}` | - | - | - | - | - | - | - | - | - | - | - | - | present and summed in `LTotal` |

- Non-fundamental colour representation rows: **none**. `V1` is a colour singlet; no `AddGaugeRepresentation[...]` line is needed.
- `SelfConjugate -> True` classes: `V1` only. It carries **no** `QuantumNumbers` (Q = 0, Y = 0, no new U(1) charge).
- Names chosen: classes `V1`; parameters `MV1`, `WV1`, `ct`, `thV`, `ctL`, `ctR`; indices: none new. None is a Mathematica built-in (`N, C, D, E, I, K, O`), a FeynRules symbol (`HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM`), or an SM.fr name (`A, Z, W, B, G, Wi, H, G0, GP, Phi, vl, l, uq, dq, LL, lR, QL, uR, dR, ee, gs, gw, g1, sw, cw, vev, lam, muH, yl, yu, yd, CKM, MZ, MW, MT, cabi`). Class index is 100 (>= 100). `ParticleName` is `"V1"`, with no prime or punctuation.
- New U(1) charges: the paper introduces **no** new gauge group. `V_1` is a simplified-model massive vector with a direct current coupling, so no re-derivation of SM hypercharges is required and no charge is put on the self-conjugate class.
- Single total: `LTotal := LV1Kin + LV1Top`. It sums every other declared term. No pure-constant term is emitted.
- Reference or cached model file read: **none**.

```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": [
      "Automated extraction from arXiv:1604.07421 (J. H. Kim, K. Kong, S. J. Lee, G. Mohlabeng)"
    ],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [
    ["QCD", 1],
    ["QED", 2],
    ["NP", 1]
  ],
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
      "description": "Overall top-philic coupling strength, c_t = Sqrt[cL^2 + cR^2], Eq.(1); benchmark value 2.0"
    },
    {
      "name": "thV",
      "parameter_type": "External",
      "value": "1.570796326794897",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "\\theta",
      "description": "Chirality angle theta, Tan[theta] = cR/cL, Eq.(1); benchmark theta = Pi/2 (pure right-handed top coupling)"
    },
    {
      "name": "ctL",
      "parameter_type": "Internal",
      "value": "ct*Cos[thV]",
      "interaction_order": ["NP", 1],
      "tex": "c_L",
      "description": "Left-handed top coupling, c_L = c_t Cos[theta], Eq.(1)"
    },
    {
      "name": "ctR",
      "parameter_type": "Internal",
      "value": "ct*Sin[thV]",
      "interaction_order": ["NP", 1],
      "tex": "c_R",
      "description": "Right-handed top coupling, c_R = c_t Sin[theta], Eq.(1)"
    },
    {
      "name": "WV1",
      "parameter_type": "Internal",
      "value": "ct^2*MV1/(8*Pi)*Sqrt[1 - 4*MT^2/MV1^2]*(1 - MT^2/MV1^2*(1 - 3*Sin[2*thV]))",
      "tex": "\\Gamma_{V_1}",
      "description": "Total width of V1, from Gamma(V1 -> t tbar), Eq.(2)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "V1",
      "self_conjugate": true,
      "mass": {
        "sym": "MV1",
        "value": "1500."
      },
      "width": {
        "sym": "WV1",
        "value": "Internal"
      },
      "pdg": 32,
      "particle_name": "V1",
      "full_name": "TopPhilicVector",
      "propagator_label": "V1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LV1Kin",
      "expression": "-1/4 FS[V1, mu, nu] FS[V1, mu, nu] + 1/2 MV1^2 V1[mu] V1[mu]",
      "delayed": true
    },
    {
      "name": "LV1Top",
      "expression": "ctL tbar.Ga[mu].ProjM.t V1[mu] + ctR tbar.Ga[mu].ProjP.t V1[mu]",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LV1Kin + LV1Top",
      "delayed": true
    }
  ]
}
```