## Self-audit table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 − d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sums | L/B sum | CC[] where paper writes ψ^c | fraction/root placement checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV1kin | V1 in FS[V1,mu,nu]FS[V1,mu,nu] and MV1²V1[mu]V1[mu] | 4 (2+2; 2+1+1) | −1/4 field-strength norm, MV1 | 0 = 4−4 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a (no fraction/root) | self-conjugate (real vector) |
| LNV1t | tbar (3/2), t (3/2), V1 (1); Ga/Proj dimension 0 | 3/2+3/2+1 = 4 | ct | 0 = 4−4 | n/a | +2/3−2/3+0 = 0 | +2/3−2/3+0 = 0 | all three singlets | 3 ⊗ 3̄ → singlet (colour contracted) | n/a | +1/3−1/3 = 0 | no (paper writes t, not t^c) | no fraction in Eq.(1) itself; √(cL²+cR²), cR/cL and the width √(1−4mt²/M²)·[1−(mt²/M²)(1−3sin2θ)] read literally from LaTeX lines 181, 186–187 | current \bar{t}γ_μ(...)t is Hermitian × real V1 → self-conjugate, no HC[] |
| V1 class | V1 kinetic+mass term LV1kin exists and is included in LTotal | 4 | — | — | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | n/a | yes |
| non-fundamental colour reps | none — paper has no sextet/octet state (line 131 is literature review only), so no AddGaugeRepresentation row | — | — | — | — | — | — | — | — | — | — | — | — | — |

- SelfConjugate → True classes: **V1** — carries no `QuantumNumbers` ✓
- Names chosen — classes: `V1`; parameters: `ct`, `theta`, `WV1`; indices: none. None is a Mathematica built-in, a FeynRules symbol, or an SM.fr name ✓ (class index 100 ≥ 100; ParticleName "V1" has no punctuation)
- Single total: **LTotal = LV1kin + LNV1t** ✓
- Reference or cached model file read: **none** (only the paper, SM.fr, schema, renderer, lints)
- Excluded on purpose: the dimension-6 contact operator ½(c_t²/M_V1²)(t̄_Rγ_μt_R)(t̄_Rγ^μt_R) (LaTeX line 325) is the s→0 limit of V1 exchange; the paper implements Eq. (1) explicitly (line 335), so emitting both would double count. Only one new state exists (V1); unused macros `\Xx`, `\MX` (lines 28–29) introduce no particle.

Last `./frgen` result: `SCHEMA OK: 1 particle classes, 3 parameters, Lagrangian terms ['LV1kin', 'LNV1t', 'LTotal']` / `RENDERED: model.fr (56 lines)` / `LINT: no findings.`