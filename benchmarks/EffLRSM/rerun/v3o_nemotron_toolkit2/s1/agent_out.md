| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power (d-4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sums | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin | WR, WRbar | 4 | -1/2, MWR^2 | 0, 2 | n/a | 0 | 0 | singlet | singlet | — | 0 | n/a | n/a | self-conjugate |
| LZRkin | ZR | 4 | -1/4, MZR^2/2 | 0, 2 | n/a | 0 | 0 | singlet | singlet | — | 0 | n/a | n/a | self-conjugate |
| LNRkin | NR | 4 | I/2, -1/2 mN | 0, 0 | n/a | 0 | 0 | singlet | singlet | — | 0 | n/a (Majorana) | n/a | self-conjugate |
| LWRqq | uqbar, dq, WR | 4 | kRq*gw/√2 | 0 | n/a | 0 | 0 | singlet | cc index | — | 0 | no | √2 from Eq.(2.1) LaTeX | HC[] explicit |
| LWRlep | NRbar, l, WR | 4 | kRl*gw/√2 * Ymix | 0 | n/a | 0 | 0 | singlet | singlet | — | 0 | no (NR self-conj) | √2 from Eq.(2.2) LaTeX | HC[] explicit |
| LZRqq | uqbar, uq, ZR / dqbar, dq, ZR | 4 | kRq*gw/√(1-kRq^-2 tW^2) * gLZu/gRZu | 0 | n/a | 0 | 0 | singlet | cc index | — | 0 | no | √(1-(1/kRq)^2 tW^2) from Eq.(2.4) LaTeX | self-conjugate |
| LZRlep | vbar, vl, ZR / lbar, l, ZR | 4 | kRl*gw/√(1-kRl^-2 tW^2) * gLZv/gRZv | 0 | n/a | 0 | 0 | singlet | singlet | — | 0 | no | √(1-(1/kRl)^2 tW^2) from Eq.(2.4) LaTeX | self-conjugate |
| LZRNR | NRbar, NR, ZR | 4 | kRl*gw/√(1-kRl^-2 tW^2) * gRZN | 0 | n/a | 0 | 0 | singlet | singlet | — | 0 | no (NR self-conj) | √(1-(1/kRl)^2 tW^2) from Eq.(2.4) LaTeX | self-conjugate |
| LTotal | sum of above | 4 | — | — | — | — | — | — | — | — | — | — | — | — |

**Particle kinetic+mass audit:** WR (LWRkin in LTotal) ✓; ZR (LZRkin in LTotal) ✓; NR (LNRkin in LTotal) ✓
**Non-fundamental color reps:** none (all new particles are color singlets)
**SelfConjugate=True no QuantumNumbers:** ZR (Q=0 only) ✓; NR (empty QuantumNumbers) ✓
**Name audit:** Classes {WR,ZR,NR}, params {kRq,kRl,mN1,mN2,mN3,Ymix}, indices {Generation,Colour,Gluon,SU2D,SU2W}, terms {LWRkin,LZRkin,LNRkin,LWRqq,LWRlep,LZRqq,LZRlep,LZRNR,LTotal}, preamble {gLZu,gRZu,gLZd,gRZd,gLZv,gRZv,gLZl,gRZl,gLZN,gRZN} — none conflict with Mathematica/FeynRules/SM.fr built-ins ✓
**Total Lagrangian:** LTotal = LWRkin + LZRkin + LNRkin + LWRqq + LWRlep + LZRqq + LZRlep + LZRNR ✓
**Reference files read:** none ✓

SCHEMA OK: 3 particle classes, 6 parameters, Lagrangian terms ['LWRkin', 'LZRkin', 'LNRkin', 'LWRqq', 'LWRlep', 'LZRqq', 'LZRlep', 'LZRNR', 'LTotal']
RENDERED: model.fr (155 lines). You may read it.
LINT: no findings.