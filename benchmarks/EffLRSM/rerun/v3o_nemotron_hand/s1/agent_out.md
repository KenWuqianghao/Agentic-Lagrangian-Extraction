## Self-Audit Table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present (must be d - 4, or "n/a" if d <= 4) | Q sum | Y sum | SU(2) contraction (singlet? which Eps or shared index) | SU(3) contraction | sum of each new U(1) charge (one column per U(1), must be 0) | lepton/baryon number sum (if the paper assigns them) | CC[] used where paper writes psi^c (yes/no/n/a) | fraction/root placement checked against (equation, LaTeX line, or "n/a") | Hermitian partner (HC[] or self-conjugate) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin | WR, WRbar (kinetic), WRbar, WR (mass) | 4 | (none) | 0 | n/a | 0 (+1 -1) | 0 | Singlet | Singlet | n/a | 0 | n/a | n/a | Self (real action) |
| LZRkin | ZR, ZR (kinetic), ZR, ZR (mass) | 4 | (none) | 0 | n/a | 0 (0) | 0 | Singlet | Singlet | n/a | 0 | n/a | n/a | Self (real field) |
| LNRkin | NR, NR (kinetic), NR, NR (mass) | 4 | (none) | 0 | n/a | 0 (0) | 0 | Singlet | Singlet | n/a | LeptonNumber=0 | n/a | n/a | Self (Majorana) |
| LWRq | uqbar, dq, WR | 4 | kapRq*gw/√2 | 0 | n/a | 0 (-2/3 -1/3 +1) | 0 | Singlet | δ_cc (color triplet) | n/a | Baryon=0 | n/a | Eq.(1), LaTeX line 281 | HC[LWRq] added |
| LWRl | NRbar, l, WR | 4 | kapRl*gw/√2 | 0 | n/a | 0 (0 -1 +1) | 0 | Singlet | Singlet | n/a | Lepton=0 | n/a | Eq.(2), LaTeX line 293 | HC[LWRl] added |
| LZRq (up) | uqbar, uq, ZR | 4 | normZRq*gL/RZRq | 0 | n/a | 0 (-2/3 +2/3 +0) | 0 | Singlet | δ_cc | n/a | 0 | n/a | Eq.(13), LaTeX line 352 | HC[LZRq] added |
| LZRq (down) | dqbar, dq, ZR | 4 | normZRq*gL/RZRd | 0 | n/a | 0 (+1/3 -1/3 +0) | 0 | Singlet | δ_cc | n/a | 0 | n/a | Eq.(13) | HC[LZRq] added |
| LZRl | lbar, l, ZR | 4 | normZRl*gL/RZRl | 0 | n/a | 0 (+1 -1 +0) | 0 | Singlet | Singlet | n/a | Lepton=0 | n/a | Eq.(13) | HC[LZRl] added |
| LZRnu | vlbar, vl, ZR | 4 | normZRl*gL/RZRnu | 0 | n/a | 0 (0+0+0) | 0 | Singlet | Singlet | n/a | Lepton=0 | n/a | Eq.(13) | HC[LZRnu] added |
| LZRN | NRbar, NR, ZR | 4 | normZRl*gL/RZRN | 0 | n/a | 0 (0+0+0) | 0 | Singlet | Singlet | n/a | Lepton=0 | n/a | Eq.(13) | HC[LZRN] added |
| LTotal | sum of all above | 4 | various | 0 | n/a | 0 | 0 | — | — | n/a | 0 | n/a | — | Single total |

**Additional verification lines:**

- **New index declaration**: `IndexRange[Index[GenerationN]] = Unfold[Range[3]];` present for 3 heavy neutrino generations ✓
- **SelfConjugate → True classes with no QuantumNumbers**: ZR (V[101]), NR (F[100]) — both carry no QuantumNumbers ✓
- **Name collision check**: Class names (WR, ZR, NR), parameter names (kapRq, kapRl, MWR, MZR, MN1, MN2, MN3, MN, WWR, WZR, WN1, WN2, WN3, WN, gLZRq, gRZRq, gLZRd, gRZRd, gLZRl, gRZRl, gLZRnu, gRZRnu, gLZRN, gRZRN, normZRq, normZRl), index (GenerationN) — none are Mathematica built-ins, FeynRules symbols, or SM.fr names ✓
- **Single LTotal**: `LTotal := LWRkin + LZRkin + LNRkin + LWRq + LWRl + LZRq + LZRl + LZRnu + LZRN` — exactly one total Lagrangian summing all terms ✓
- **Reference model file read**: none (only paper/1610.08985_source.tex and SM.fr read) ✓

model.fr is written.