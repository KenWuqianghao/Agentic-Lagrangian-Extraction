## Mandatory self-audit

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (4 − d) | 1/Lambda power (d−4, or n/a) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used where paper writes ψᶜ | fraction/root placement checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV1kin | V1, V1 (`FS[V1,mu,nu]`²; `V1[mu]V1[mu]`) | 4 (FS-term); V1V1 monomial d=2 | −1/4 ; 1/2 MV1² | 0 ; MV1² = 2 = 4−2 ✓ | n/a | 0 (V1 neutral) | 0 (V1 Y=0) | singlet (V1 SU(2)-singlet, no Eps/shared index) | singlet | n/a (no new U(1)) | n/a | n/a | n/a — rule-1 template form | self-conjugate |
| LV1int | uqbar, uq, V1 (`ct Cos[th] uqbar.Ptop.Ga[mu].ProjP.uq V1[mu] + ct Sin[th] …ProjM…`) | 4 (3/2+3/2+0+1) | ct (with Cos[th], Sin[th] dimensionless) | 0 = 4−4 ✓ | n/a (d = 4) | −2/3+2/3+0 = 0 | −2/3+2/3+0 = 0 | singlet (uq is Y=2/3 SU(2) singlet, V1 singlet; no Eps) | uqbar·uq colour contracted in dot product; V1 colour singlet | n/a | n/a | n/a (paper Eq.(1) has no ψᶜ) | coupling has no fraction/root; θ=π/2 from LaTeX line 244 (Eq.(1) tanθ = c_R/c_L); width formula Ct./frac. placement from LaTeX lines 185–189, Eq.(2) | self-conjugate (Ptop real, V1 real, Cos/Sin real → no HC[]) |

- New particle class V1: kinetic + mass term `LV1kin` exists and is in the total sum ✓. No non-fundamental colour representation → no `AddGaugeRepresentation[...]` required.
- `SelfConjugate -> True` classes: **V1** — carries no `QuantumNumbers` ✓.
- Names chosen: classes `V1` (ParticleName "V1"), class index 100; parameters `ct`, `th`, `Ptop`, `WV1`; no new index names (only SM `Colour`/`Generation`). None is a Mathematica built-in, a FeynRules symbol, or an SM.fr name ✓.
- Single total Lagrangian: `LTotal := LV1kin + LV1int` — sums every other term defined ✓.
- Reference or cached model file read: **none**.

```
SCHEMA OK: 1 particle classes, 4 parameters, Lagrangian terms ['LV1kin', 'LV1int', 'LTotal']
RENDERED: model.fr (64 lines). You may read it.
LINT: no findings.
```