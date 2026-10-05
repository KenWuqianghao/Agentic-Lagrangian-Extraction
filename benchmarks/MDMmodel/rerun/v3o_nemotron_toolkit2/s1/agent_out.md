**Self-Audit Table**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4-d) | 1/Lambda power present | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sums | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LSkin | S, del | 4 | (kinetic) | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conj |
| LSmass | S, S | 2 | MSdil^2 | 2 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conj |
| LTkin | TPbar, TP, DC, Ga | 4 | (kinetic) | 0 | n/a | 0 | 0 | singlet | colour singlet (TPbar^cc TP_cc) | n/a | 0 | n/a | n/a | + HC in total |
| LTmass | TPbar, TP | 3 | MTp | 1 | n/a | 0 | 0 | singlet | colour singlet | n/a | 0 | n/a | n/a | self-conj |
| LSpot (S^4) | S^4 | 4 | lambdaS | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conj |
| LSpot (portal) | S^2, Phibar, Phi | 4 | kappa | 0 | n/a | 0 | 0 | Phibar[ii] Phi[ii] shared SU2D index | singlet | n/a | 0 | n/a | n/a | self-conj |
| LTint (combined) | S, TPbar, TP | 4 | MTp/f | 0 | n/a | 0 | 0 | singlet | colour singlet | n/a | 0 | n/a | n/a | self-conj |
| LTyuk | TPbar, QL[3], Phi, Eps | 4 | yp | 0 | n/a | 0 | 0 | QL[ii] Phi[jj] Eps[ii,jj] | colour singlet (TPbar^cc QL_cc) | n/a | 0 | n/a | LaTeX Eq.(1) | + HC |

**Additional audit rows:**

- **Kinetic+mass terms in LTotal**: LSkin, LSmass (S class); LTkin, LTmass (TP class) — all present and summed in LTotal.
- **Non-fundamental colour reps**: none (TP uses fundamental Colour triplet, no sextet/octet).
- **SelfConjugate classes with no QuantumNumbers**: S (class_index 100), sd (class_index 102) — both have empty QuantumNumbers, OK.
- **Name conflict check**: Class names S, TP, sd, tp; parameter names f, thetaS, ms, Mtprime, thetaL, yp, MSdil, lambdaS, kappa, MTp, eta; index names Colour, Generation, SU2D, SU2W, Gluon (all from SM.fr). None are Mathematica built-ins (N, C, D, E, I, K, O, Pi, etc.), FeynRules symbols (HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM), or SM.fr names (H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, MZ, MW, MH, etc.). OK.
- **Single total Lagrangian**: LTotal = LSkin + LSmass + LTkin + LTmass + LSpot + LTint + LTyuk. All 7 terms appear exactly once in the sum.
- **Reference/cached model files read**: none (only paper/1311.6661_source.tex and SM.fr for conventions).

**Last ./frgen result:**
```
SCHEMA OK: 4 particle classes, 11 parameters, Lagrangian terms ['LTotal', 'LSkin', 'LSmass', 'LTkin', 'LTmass', 'LSpot', 'LTint', 'LTyuk']
RENDERED: model.fr (170 lines). You may read it.
LINT: 2 finding(s). Each names the stage it predicts will fail (compile, checks = a FeynRules consistency check, mg5 = MadGraph import, harness = the total Lagrangian cannot be identified, warn = may still pass). Fix the ones that are real defects; do not remove paper physics just to silence one.
- [warn] undeclared_symbol: `LSpot` uses `Phibar` which is neither declared here nor by SM.fr (model.fr line 166)
- [warn] undeclared_symbol: `LTyuk` uses `QL` which is neither declared here nor by SM.fr (model.fr line 170)
```