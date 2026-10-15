Now I'll produce the mandatory self-audit table:

## Self-Audit Table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present (must be d - 4, or "n/a" if d <= 4) | Q sum | Y sum | SU(2) contraction (singlet? which Eps or shared index) | SU(3) contraction | sum of each new U(1) charge (one column per U(1), must be 0) | lepton/baryon number sum (if the paper assigns them) | CC[] used where paper writes psi^c (yes/no/n/a) | fraction/root placement checked against (equation, LaTeX line, or "n/a") | Hermitian partner (HC[] or self-conjugate) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpKin (kinetic) | Wpbar, Wp (FS) | 4 | -1/2 | 0 | n/a | 0 (Q_Wp=1, Q_Wpbar=-1) | n/a (Wp is SM gauge singlet) | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LWpKin (mass) | Wpbar, Wp | 2 | MWp^2 | 2 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LvRKin (kinetic) | vRbar, vR, DC | 4 | I | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 (L_vR=1, L_vRbar=-1) | n/a | n/a | self-conjugate |
| LvRKin (mass) | vRbar, vR | 3 | MvR | 1 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LWpQuark | uqbar, dq, Wp | 4 | gw/Sqrt[2] * CLq/CRq | 0 | n/a | 0 (Q_uqbar=-2/3, Q_dq=-1/3, Q_Wp=1) | n/a (effective operator) | singlet | 3bar * 3 = 1 | n/a | 0 (B_uqbar=-1/3, B_dq=1/3) | no (paper: fbar_i gamma_mu P_{L,R} f_j) | Eq.(1): g/Sqrt[2] | HC[LWpQuark] |
| HC[LWpQuark] | uq, dqbar, Wpbar | 4 | gw/Sqrt[2] * CLq†/CRq† | 0 | n/a | 0 | n/a | singlet | 3 * 3bar = 1 | n/a | 0 | no | Eq.(1) | LWpQuark |
| LWpLeptonLeft | vlbar, l, Wp | 4 | gw/Sqrt[2] * CLl | 0 | n/a | 0 (Q_vl=0, Q_l=-1, Q_Wp=1) | n/a | singlet | singlet | n/a | 0 (L_vl=1, L_l=1, L_vlbar=-1) | no | Eq.(1) | HC[LWpLeptonLeft] |
| HC[LWpLeptonLeft] | vl, lbar, Wpbar | 4 | gw/Sqrt[2] * CLl† | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | no | Eq.(1) | LWpLeptonLeft |
| LWpLeptonRight | vRbar, l, Wp | 4 | gw/Sqrt[2] * CRl | 0 | n/a | 0 (Q_vR=0, Q_l=-1, Q_Wp=1) | n/a | singlet | singlet | n/a | 0 (L_vR=1, L_l=1, L_vRbar=-1) | no | Eq.(1) | HC[LWpLeptonRight] |
| HC[LWpLeptonRight] | vR, lbar, Wpbar | 4 | gw/Sqrt[2] * CRl† | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | no | Eq.(1) | LWpLeptonRight |

**Additional audit rows:**

- **New particle kinetic+mass terms**: Wp (V[100]) has LWpKin in LTotal ✓; vR (F[100]) has LvRKin in LTotal ✓
- **Non-fundamental colour representations**: none (Wp and vR are colour singlets) ✓
- **SelfConjugate -> True classes with no QuantumNumbers**: none (Wp: SelfConjugate->False, Q=1; vR: SelfConjugate->False, LeptonNumber=1) ✓
- **Name conflict check**: Class names (Wp, vR), parameter names (MWp, WWp, CLq, CRq, CLl, CRl, MvR), index names (Generation, Colour, SU2D, SU2W, Gluon from SM.fr) — none are Mathematica built-ins, FeynRules symbols (N, C, D, E, I, K, O, HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM), or SM.fr names (H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, MZ, MW, etc.) ✓
- **Single total Lagrangian**: LTotal = LWpKin + LvRKin + LWpQuark + HC[LWpQuark] + LWpLeptonLeft + HC[LWpLeptonLeft] + LWpLeptonRight + HC[LWpLeptonRight] ✓
- **Reference/cached model file read**: none (only paper/hep-ph_0207290_source.tex and SM.fr read) ✓

model.fr is written.