I read the paper's LaTeX source, the schema, and SM.fr. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content found in the paper

Section II ("A Top-Philic Resonance: Simplified Model") is the only new-physics content. One new state: a colour-singlet, SU(2)-singlet, electrically neutral, **real vector** resonance `V_1`. Eq. (1) (LaTeX lines 176-181):

`L_int = tbar Ga_mu (c_L P_L + c_R P_R) t V_1^mu = c_t tbar Ga_mu (cos(th) P_L + sin(th) P_R) t V_1^mu`, with `c_t = Sqrt[c_L^2 + c_R^2]`, `tan(th) = c_R/c_L`.

Three free parameters (line 221-222): `M_V1`, `c_t`, `th`. Benchmark: `M_V1 = 1.5 TeV`, `c_t = 2.0`, `th = Pi/2`. Eq. (2) gives the width. Eq. (3) is the EFT contact operator obtained by integrating out the same `V_1`; it is not a separate state and is not emitted (it would double count). The `\Xx`/`\MX` macros in the preamble are unused leftovers, not particles.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling symbol | coupling dim (4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin (kinetic) | `FS[Zp,mu,nu] FS[Zp,mu,nu]` | 4 | `-1/4` (pure number) | 0 | n/a | 0 | 0 | singlet, no index | singlet, no index | none declared | 0 | n/a | n/a | self-conjugate (real field) |
| LZpKin (mass) | `Zp[mu] Zp[mu]` | 2 | `MZp^2` | 2 | n/a | 0 | 0 | singlet, no index | singlet, no index | none declared | 0 | n/a | n/a | self-conjugate (real `MZp`) |
| LZpTop (P_L piece) | `uqbar . uq . Zp` | 4 | `gLt[3,3] = cL = ct Cos[th]` | 0 | n/a (d=4) | `-2/3 + 2/3 + 0 = 0` | n/a: post-EWSB physical fields; SM.fr gives `uq` only `Q`, and `Zp` is a gauge singlet | n/a: no doublet in the term; `Zp` is an SU(2) singlet | implicit `Colour` contraction `3bar (x) 3 -> 1`; `Zp` colour singlet | none declared | B: `-1/3 + 1/3 = 0` | n/a (paper writes no `psi^c`) | LaTeX line 181: `\tan\theta = \frac{c_R}{c_L}`, `c_t=\sqrt{c_L^2+c_R^2}` -> `cL = ct Cos[th]`, `cR = ct Sin[th]` | self-Hermitian: real diagonal coupling matrix on a vector current with a real `Zp`; no `HC[]` |
| LZpTop (P_R piece) | `uqbar . uq . Zp` | 4 | `gRt[3,3] = cR = ct Sin[th]` | 0 | n/a (d=4) | `-2/3 + 2/3 + 0 = 0` | n/a (same reason) | n/a (same reason) | implicit `Colour` contraction | none declared | B: 0 | n/a | same LaTeX line 181 | self-Hermitian; no `HC[]` |
| per-class free-field row: `Zp` (V[100]) | — | — | — | — | — | — | — | — | — | — | — | — | — | kinetic + mass term `LZpKin` exists, uses the class mass symbol `MZp`, and is summed in `LTotal` |
| colour-representation row | — | — | — | — | — | — | — | — | only `Colour` (triplet, SM.fr) is used; no sextet or other non-fundamental rep, so **no** `AddGaugeRepresentation[...]` line is needed | — | — | — | — | — |

Extra fraction/root check (rule 7): the width Eq. (2), LaTeX lines 186-187, reads `\frac{c_t^2 M_{V_1}}{8\pi}\sqrt{1-\frac{4m_t^2}{M_{V_1}^2}}[1-\frac{m_t^2}{M_{V_1}^2}(1-3\sin 2\theta)]`. Taken literally. Cross-check with line 191: for `m_t << M_V1` the paper states `Gamma/M_V1 = c_t^2/(8 Pi)`, which the literal placement reproduces (`4 x 2 / (8 Pi) = 0.159`). Used for the Internal parameter `WZp`.

- `SelfConjugate -> True` classes: `Zp` (V[100]) only. It carries **no** `QuantumNumbers`.
- Names chosen: classes `Zp`; parameters `MZp`, `WZp`, `ct`, `th`, `cL`, `cR`, `gLt`, `gRt`; indices used `Generation`, `Colour` (both from SM.fr, no declaration needed). None is a Mathematica built-in, a FeynRules symbol, or an SM.fr name. No primes or punctuation in `ParticleName`.
- Single total Lagrangian: `LTotal := LZpKin + LZpTop`. It sums every other term defined. No term is a pure constant.
- Reference or cached model file read: **none**.

```json
{
  "model_name": "Top-Philic-Zprime_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:1604.07421 (J. H. Kim, K. Kong, S. J. Lee, G. Mohlabeng)"],
    "version": "1.0",
    "date": "09. 09. 2026",
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
      "name": "ct",
      "parameter_type": "External",
      "value": "2.0",
      "block_name": "TOPPHILIC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "Subscript[c,t]",
      "description": "Overall coupling strength of the top-philic vector resonance to the top quark, c_t = Sqrt[c_L^2 + c_R^2], Eq.(1). Benchmark value 2.0."
    },
    {
      "name": "th",
      "parameter_type": "External",
      "value": "1.5707963267948966",
      "block_name": "TOPPHILIC",
      "order_block": 2,
      "tex": "\\[Theta]",
      "description": "Chirality angle theta with Tan[theta] = c_R/c_L, Eq.(1). Benchmark theta = Pi/2, i.e. a purely right-handed coupling to the top quark."
    },
    {
      "name": "cL",
      "parameter_type": "Internal",
      "value": "ct*Cos[th]",
      "interaction_order": ["NP", 1],
      "tex": "Subscript[c,L]",
      "description": "Left-handed top coupling c_L = c_t Cos[theta], Eq.(1)."
    },
    {
      "name": "cR",
      "parameter_type": "Internal",
      "value": "ct*Sin[th]",
      "interaction_order": ["NP", 1],
      "tex": "Subscript[c,R]",
      "description": "Right-handed top coupling c_R = c_t Sin[theta], Eq.(1)."
    },
    {
      "name": "gLt",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "gLt[1,1]", "rhs": "0"},
        {"lhs": "gLt[1,2]", "rhs": "0"},
        {"lhs": "gLt[1,3]", "rhs": "0"},
        {"lhs": "gLt[2,1]", "rhs": "0"},
        {"lhs": "gLt[2,2]", "rhs": "0"},
        {"lhs": "gLt[2,3]", "rhs": "0"},
        {"lhs": "gLt[3,1]", "rhs": "0"},
        {"lhs": "gLt[3,2]", "rhs": "0"},
        {"lhs": "gLt[3,3]", "rhs": "cL"}
      ],
      "tex": "Superscript[g,L]",
      "description": "Left-handed coupling matrix of the vector resonance to up-type quarks. Only the (3,3) top entry is non-zero: the resonance is top-philic, Eq.(1)."
    },
    {
      "name": "gRt",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "gRt[1,1]", "rhs": "0"},
        {"lhs": "gRt[1,2]", "rhs": "0"},
        {"lhs": "gRt[1,3]", "rhs": "0"},
        {"lhs": "gRt[2,1]", "rhs": "0"},
        {"lhs": "gRt[2,2]", "rhs": "0"},
        {"lhs": "gRt[2,3]", "rhs": "0"},
        {"lhs": "gRt[3,1]", "rhs": "0"},
        {"lhs": "gRt[3,2]", "rhs": "0"},
        {"lhs": "gRt[3,3]", "rhs": "cR"}
      ],
      "tex": "Superscript[g,R]",
      "description": "Right-handed coupling matrix of the vector resonance to up-type quarks. Only the (3,3) top entry is non-zero: the resonance is top-philic, Eq.(1)."
    },
    {
      "name": "WZp",
      "parameter_type": "Internal",
      "value": "ct^2*MZp/(8*Pi)*Sqrt[1 - 4*MT^2/MZp^2]*(1 - MT^2/MZp^2*(1 - 3*Sin[2*th]))",
      "tex": "Subscript[\\[CapitalGamma],Zp]",
      "description": "Total width of the top-philic vector resonance, Gamma(V1 -> t tbar), Eq.(2), taken verbatim from the LaTeX source. Reproduces Gamma/M = c_t^2/(8 Pi) for m_t << M_V1."
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "indices": [],
      "class_members": [],
      "mass": {"sym": "MZp", "value": "1500."},
      "width": {"sym": "WZp", "value": "Internal"},
      "quantum_numbers": {},
      "pdg": 32,
      "particle_name": "Zp",
      "full_name": "Top-philic colour-singlet vector resonance V1",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None",
      "unphysical": false
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "expression": "Block[{mu, nu}, ExpandIndices[-1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]]",
      "delayed": true
    },
    {
      "name": "LZpTop",
      "expression": "Block[{mu}, ExpandIndices[uqbar.gLt.Ga[mu].ProjM.uq Zp[mu] + uqbar.gRt.Ga[mu].ProjP.uq Zp[mu]]]",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LZpKin + LZpTop",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```