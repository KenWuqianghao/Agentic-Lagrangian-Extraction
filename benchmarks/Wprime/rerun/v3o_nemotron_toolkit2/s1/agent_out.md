**Self-audit table:**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power | Q sum | Y sum* | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpKin | Wpbar, Wp, FS[Wpbar], FS[Wp] | 4 | 1, MWp² | 0, 2 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LNuRKin | nuRbar, nuR, DC[nuR] | 4 | 1, MnuR | 0, 1 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LWpInt (quark) | uqbar, dq, Wp | 4 | gR, gL, VRqq, VLqq, ζ, ω | 0 | n/a | 0 | n/a | singlet | δ_cc (color singlet) | n/a | 0 | n/a | n/a (Cos/Sin from LaTeX) | HC[LWpInt] |
| LWpInt (lepton vl) | vlbar, l, Wp | 4 | gL, VLll, ζ | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | n/a | HC[LWpInt] |
| LWpInt (lepton nuR) | nuRbar, l, Wp | 4 | gR, VRll, ζ, ω | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | n/a | HC[LWpInt] |

*Y sum: Wp and nuR are SU(2)ₗ singlets with no U(1)ᵧ gauge interactions (gauge_groups=[]); only Q is assigned. SM.fr U(1)ᵧ charges are not enforced on new non-gauged vectors/fermions.

**Additional checks:**
- Kinetic+mass terms exist for both new classes (Wp, nuR) and are in LTotal ✓
- No non-fundamental color representations (both are singlets) ✓
- SelfConjugate→True classes: none (Wp self_conjugate=false, nuR self_conjugate=false) ✓
- Name conflicts: Wp, nuR, MWp, WWp, gL, gR, zeta, omega, VLqq, VRqq, VLll, VRll, MnuR, LWpKin, LNuRKin, LWpInt, LTotal — none are Mathematica built-ins, FeynRules symbols, or SM.fr names ✓
- Single total Lagrangian: LTotal = LWpKin + LNuRKin + LWpInt + HC[LWpInt] ✓
- Reference/cached model files read: none ✓

Final `./frgen spec.json` result:
```
SCHEMA OK: 2 particle classes, 11 parameters, Lagrangian terms ['LWpKin', 'LNuRKin', 'LWpInt', 'LTotal']
RENDERED: model.fr (150 lines). You may read it.
LINT: no findings.
```