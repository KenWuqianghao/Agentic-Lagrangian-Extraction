Schema is clean; remaining findings are `warn`-level `Phibar`/`LLbar` undeclared-symbol notes. Judged harmless: `Phi` and `LL` are declared by local `SM.fr` (used in SM.fr's own terms, e.g. lines 706/714), so their conjugates are valid on load. No `spec.json` change needed.

## Self-audit

| term name | fields in the monomial | d | coupling | coupling dim | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | U(1)_X sum | L/B | CC[] | fraction/root checked | HC partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin | FS[Zp]²; MZp² Zp² | 4; 4 | —; MZp² | 0; 2 | n/a | 0 | 0 | singlet | singlet | 0 (Zp gauge boson) | 0 | n/a | n/a | self-conjugate |
| LPhikin | DC[Sphibar]DC[Sphi]; Mphi² Sphibar Sphi | 4; 4 | —; Mphi² | 0; 2 | n/a | 0 | 0 | singlet | singlet | 0 (φ*φ) | 0 | n/a | n/a | self-conjugate |
| LNkin | NRbar Ga del NR; MN NRbar NR | 4; 4 | —; MN | 0; 1 | n/a | 0 | 0 | singlet | singlet | 0 (NRbar NR, Majorana) | 0 | n/a (Y_N absorbed into MN per rule 1) | n/a | self-conjugate (1/2 factors) |
| LZpQuark | uqbar Ga ProjM/P uq Zp; dqbar … | 4 | gp×(xH/6+xPhi/3), (2xH/3+xPhi/3), (xH/6+xPhi/3), (−xH/3+xPhi/3) | 0 | n/a | 0 | 0 | singlets (chiral projectors) | bar·triplet | 0 (barψ ψ Zp) | 1/3 each | n/a | Table 1 LaTeX line 102; Eq. Lag1 line 189 | self-conjugate current |
| LZpLepton | lbar Ga ProjM l Zp; lbar Ga ProjP l Zp | 4 | gp×(−xH/2−xPhi), (−xH−xPhi) | 0 | n/a | 0 | 0 | singlets | singlet | 0 | 1 | n/a | Table 1 line 102 | self-conjugate |
| LZpNeutrino | vlbar Ga ProjM vl Zp | 4 | gp×(−xH/2−xPhi) | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 1 | n/a | Table 1 line 102 | self-conjugate |
| LZpNR | NRbar Ga ProjP NR Zp | 4 | gp×(−xPhi) | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Table 1 line 102 | self-conjugate |
| LZpSphi | Zp(Sphibar del Sphi − Sphi del Sphibar); Zp² Sphibar Sphi | 4; 4 | 2 xPhi gp; 4 xPhi² gp² | 0; 0 | n/a | 0 | 0 | singlet | singlet | 0 (charge 2xPhi) | 0 | n/a | X(Φ)=2x_Φ from Table 1 line 102 | self-conjugate (i-structure) |
| LZpHiggs | Zp(Phibar del Phi − Phi del Phibar); Zp² Phibar Phi | 4; 4 | (xH/2) gp; (xH/2)² gp² | 0; 0 | n/a | 0 | 0 | Phibar[ii]Phi[ii] shared index | singlet | 0 with X(Phi_SMfr)=+xH/2 | 0 | n/a | charge sign choice below | self-conjugate (i-structure) |
| LYnu | LLbar.yv.NR Phibar Eps | 4 | yv (diag 1.*^-5) | 0 | n/a | 0 | 0 | LLbar–Phibar same conjugation, Eps[ii,jj] distinct indices | singlet | 0: (xH/2+xPhi)+(−xPhi)+(−xH/2)=0 | 1 | n/a (paper N^c only in Majorana term, absorbed) | SM.fr Y_ν slot = Phibar+Eps (rule 4); Table 1 sign below | yuk+HC[yuk] explicit |
| LPhiPot | (Sphibar Sphi)²; (Phibar Phi)(Sphibar Sphi) | 4; 4 | lambdaPhi; lambdap | 0; 0 | n/a | 0 | 0 | Phibar[ii]Phi[ii] shared; φ singlets | singlet | 0 | 0 | n/a | V Eq. paper line 159, L=−V | self-conjugate (real λ) |
| LTotal | sum of all above | — | — | — | n/a | 0 | 0 | — | — | 0 | — | — | — | — |
| LZpkin (Zp free) | as row 1 | 4 | MZp | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | in LTotal | yes |
| LPhikin (Sphi free) | as row 2 | 4 | Mphi | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | in LTotal | yes |
| LNkin (NR free) | as row 3 | 4 | MN | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | in LTotal | yes |
| colour sextet+ | n/a — no non-fundamental colour rep | — | — | — | — | — | — | — | — | — | — | — | AddGaugeRepresentation not required | — |

- **SelfConjugate → True, no QuantumNumbers:** `Zp` (V[100]), `NR` (F[101]).
- **Names:** classes `Zp`, `NR`, `Sphi`; members `NR1`,`NR2`,`NR3`; params `gp`,`xH`,`xPhi`,`yv`,`lambdaPhi`,`lambdap`; mass/width `MZp`,`WZp`,`MN`,`Mphi`. None is a Mathematica built-in, FeynRules symbol, or SM.fr name (rule 10). ParticleName `"Zp"`,`"N1"`,`"N2"`,`"N3"`,`"phi"`,`"phibar"` — no primes/punctuation.
- **Charge-sign choice (rule 5):** Paper Table 1 gives X(H)=−x_H/2, but paper's H occupies the up-type Yukawa slot ≡ SM.fr `Phibar` (SM.fr Y_u is `QLbar.uR Phibar Eps`, Y_ν analog uses `Phibar Eps` too because paper's ⟨H⟩ is in the upper component). Re-deriving from SM.fr Yukawa invariance: **X(SM.fr Phi) = +x_H/2** (opposite sign to the table entry for paper H). All SM Yukawas and LYnu sum to U(1)_X charge 0 with this assignment; fermion charges copied as in Table 1 (q_L, u_R, d_R, ℓ_L, e_R, ν_L, N_R = −x_Φ).
- **Fraction/root placement:** all rational coefficients (x_H/6, 2x_H/3, −x_H/3, −x_H/2, x_Φ/3, 2x_Φ) taken literally from Table 1 LaTeX (`\frac{1}{6}x_H + \frac{1}{3}x_Φ` etc., source line 102); chiral structure and −g′ prefactor from Eq. Lag1 (line 189). No radicals in the emitted Lagrangian (MZ′ formula is mass input, not a term).
- **Single total:** `LTotal` = LZpkin + LPhikin + LNkin + LZpQuark + LZpLepton + LZpNeutrino + LZpNR + LZpSphi + LZpHiggs + LYnu + LPhiPot.
- **Reference/cached .fr read:** none (only paper source, local SM.fr, schema/tools).

Last `./frgen spec.json`: `SCHEMA OK: 3 particle classes, 6 parameters, 12 lagrangian terms; RENDERED model.fr (131 lines); LINT: 3 findings — all [warn] undeclared_symbol for Phibar/LLbar, judged harmless (conjugates of SM.fr Phi/LL, which SM.fr itself uses).`