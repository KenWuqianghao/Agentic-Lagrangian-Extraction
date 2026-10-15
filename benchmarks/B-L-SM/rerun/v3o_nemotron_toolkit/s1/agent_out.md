The model is complete. Here is the mandatory self-audit table:

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power (d-4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | BL sum | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin (kin) | Zp, FS[Zp] | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj |
| LZpKin (mass) | Zp, Zp | 2 | MZp² | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj |
| LchiKin | chi, chibar, DC | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | HC |
| Lh2Kin (kin) | h2, del | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj |
| Lh2Kin (mass) | h2, h2 | 2 | MHH² | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj |
| LGpKin (kin) | Gp, del | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj |
| LGpKin (mass) | Gp, Gp | 2 | MZp² | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj |
| LNuRKin | NuR, NuRbar, DC | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | HC |
| LPotential (mH2) | Phi, Phibar | 2 | mH2 | 2 | n/a | 0 | 0 | shared ii | singlet | 0 | 0 | n/a | LaTeX Eq(VHX),Eq(para_quartic) | HC |
| LPotential (mu2) | chi, chibar | 2 | mu2 | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | LaTeX Eq(VHX),Eq(para_quartic) | HC |
| LPotential (lam1) | Phi, Phibar (×2) | 4 | lam1 | 0 | n/a | 0 | 0 | shared ii | singlet | 0 | 0 | n/a | LaTeX Eq(para_quartic) | self-conj |
| LPotential (lam2) | chi, chibar (×2) | 4 | lam2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | LaTeX Eq(para_quartic) | self-conj |
| LPotential (lam3) | Phi, Phibar, chi, chibar | 4 | lam3 | 0 | n/a | 0 | 0 | shared ii | singlet | 0 | 0 | n/a | LaTeX Eq(para_quartic) | HC |
| LYukawaNu | LLbar, NuR, Phibar | 4 | ynu | 0 | n/a | 0 | 0 | Eps[ii,jj] on anti-doublets | singlet | 0 | 0 | no (Dirac) | LaTeX Eq(LY) | HC[LYukawaNu] |
| LYukawaM | CC[NuR], NuR, chi | 4 | yM | 0 | n/a | 0 | 0 | singlet | singlet | 0 | ΔL=2 | yes (CC[NuR]) | LaTeX Eq(LY) | HC[LYukawaM] |
| LZpSM | Zp, uq/dq/vl/l | 4 | gp | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj |

**SelfConjugate classes with no QuantumNumbers:** Zp (BL=0), h2, Gp — all carry no additive quantum numbers (BL=0 for Zp is gauge charge, not additive U(1); h2, Gp have empty QN).

**Name collision check:** Class names {Zp, chi, h2, Gp, NuR, NuR1, NuR2, NuR3}, parameter names {gp, MZp, MHH, SA, MN, x, CA, lam1, lam2, lam3, mH2, mu2, yM, VlN, ynu}, indices {Generation, Colour, Gluon, SU2D, SU2W} — none are Mathematica built-ins, FeynRules symbols (HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM, etc.), or SM.fr names (H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, MZ, MW, etc.).

**Single total Lagrangian:** LTotal = LZpKin + LchiKin + Lh2Kin + LGpKin + LNuRKin + LPotential + LYukawaNu + LYukawaM + LZpSM + HC[LYukawaNu] + HC[LYukawaM] + LSM

**Reference/cached model read:** none

Final `./frgen spec.json` result:
```
SCHEMA OK: 5 particle classes, 15 parameters, Lagrangian terms ['LZpKin', 'LchiKin', 'Lh2Kin', 'LGpKin', 'LNuRKin', 'LPotential', 'LYukawaNu', 'LYukawaM', 'LZpSM', 'LTotal']
RENDERED: model.fr (212 lines). You may read it.
LINT: 2 finding(s). [warn] undeclared_symbol: `LPotential` uses `Phibar` which is neither declared here nor by SM.fr; [warn] undeclared_symbol: `LYukawaNu` uses `LLbar` which is neither declared here nor by SM.fr
```
(These two warnings are false positives — `Phi`/`Phibar` and `LL`/`LLbar` are declared in SM.fr, which this add-on loads on top of.)