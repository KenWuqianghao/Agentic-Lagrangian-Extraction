All checks passed on the run: schema OK, `model.fr` rendered, lint clean. Final self-audit:

## Self-audit table

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (=4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used for ψ^c | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNRkin | Nrbar, del[Nr,mu] (kin.); Nrbar, Nr (mass) | 4 (kin.); 3 (mass) | I (kin.); MN (mass) | 0; 1 = 4-3 | n/a | 0 | 0 | singlet (no index) | singlet | n/a | 0 kin.; Majorana mass ΔL=2 (expected) | n/a (rule-1 Majorana form `-1/2 MN Nrbar.Nr`, no ψ^c in source) | n/a (no √/frac beyond 1/2) | self-conjugate (Majorana bilinear) |
| LWN | W[mu], bar[CC[Nr]], l[1..3] | 4 | `-gw/Sqrt[2]` (=g/√2) | 0 | n/a | 1+0+(−1)=0 | 0¹ | singlet (physical fields, no Eps/shared ii) | singlet | n/a | +1 per monomial from l (L=1), N Majorana L=0 ⇒ ΔL=±1 LNV (model is Majorana) | yes — paper `\overline{N^c}`, LaTeX line 225 | `g/√2` ⇒ `gw/Sqrt[2]`, LaTeX line 225 `\frac{g}{\sqrt{2}}` | explicit `+ HC[...]` (paper Eq. Lagrangian, lines 224–228 H.c.) |
| LZN | Z[mu], bar[CC[Nr]], vl[1..3] | 4 | `-gw/(2 cw)` (=g/(2cosθ_W)) | 0 | n/a | 0+0+0=0 | 0¹ | singlet | singlet | n/a | vl L=1, N L=0 ⇒ ΔL=±1 (Majorana) | yes — `\overline{N^c}`, LaTeX line 227 | `g/(2 cosθ_W)` ⇒ `gw/(2 cw)`, LaTeX line 227 `\frac{g}{2\cos\theta_W}` | explicit `+ HC[...]` |
| LhN | H, bar[CC[Nr]], vl[1..3] | 4 | `-gw MN/(2 MW)` (=g m_N/(2M_W)) | 0 (MN/MW dimensionless) | n/a | 0+0+0=0 | 0¹ | singlet | singlet | n/a | same as LZN | yes — `\overline{N^c}`, LaTeX line 228 | `g m_N/(2M_W)` ⇒ `gw MN/(2 MW)`, LaTeX line 228 `\frac{g m_N}{2M_W}` | explicit `+ HC[...]` |
| LTotal | = LNRkin + LWN + LZN + LhN | 4 | (sum) | — | n/a | 0 | 0 | — | — | n/a | — | — | — | sum of above |
| Nr particle class | free-field kinetic+mass exists as LNRkin and is in LTotal | — | — | — | n/a | 0 | 0 | singlet, SelfConjugate→True, no QuantumNumbers | singlet | n/a | Majorana | — | — | Majorana mass term is its own conjugate |
| non-fundamental colour rep | none (no sextet/octet; no `AddGaugeRepresentation[...]` needed) | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

¹ Y sums use declared charges only: SM.fr puts `Y` only on unphysical fields (LL/lR/Phi…); the physical fields used here (W, Z, H, l, vl) declare no `Y`, and Nr is an uncharged Majorana singlet, so all sums are 0. Hypercharge is broken by ⟨Φ⟩ anyway; the unbroken-phase precursors are Y-invariant: LWN/LZN ← `DC[LL, mu]` charged/neutral currents, LhN ← Yukawa `LLbar Phi[tt] ν_R` with physical H.

- **SelfConjugate → True classes:** `Nr` only — carries no `QuantumNumbers` (confirmed in model.fr:47–58).
- **Names:** class `Nr`; parameters `VeN`, `VmN`, `VtN`, `MN`, `WN`; no new indices; `ParticleName "N"` (ClassName is `Nr`, not the builtin `N`) — none are Mathematica/FeynRules builtins or SM.fr names (`MN`/`WN` distinct from SM `MW`/`WZ`/`WW`).
- **Single total:** `LTotal := LNRkin + LWN + LZN + LhN` — exactly one total, every defined term appears in it.
- **Reference/cached model files read:** none.
- **Notes:** paper (line 210ff/eq. Lagrangian) considers only one heavy eigenstate `N`; Majorana commands in the paper's MG pipeline name it `n2`, but the theory text and displayed Lagrangian use `N` — model follows the theory text (single `Nr`). Light-neutrino `U` lines (224, 226) already in SM.fr; Goldstone couplings mentioned at tex line 246 are not displayed in eq. Lagrangian and are omitted; `V*` written as real External `VeN/VmN/VtN` (benchmark σ₀ sets |V|=1, so V*=V).

**Last `./frgen` result:** `SCHEMA OK: 1 particle classes, 3 parameters, Lagrangian terms ['LNRkin', 'LWN', 'LZN', 'LhN', 'LTotal'] / RENDERED: model.fr (69 lines) / LINT: no findings.`