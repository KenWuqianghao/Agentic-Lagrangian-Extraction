**Self-audit table:**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present (must be d - 4, or "n/a" if d <= 4) | Q sum | Y sum | SU(2) contraction (singlet? which Eps or shared index) | SU(3) contraction | sum of each new U(1) charge (must be 0) | lepton/baryon number sum | CC[] used where paper writes psi^c | fraction/root placement checked against | Hermitian partner (HC[] or self-conjugate) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpKinMass (kinetic) | Wpbar[mu], Wp[nu], FS, FS | 4 | (implicit 1) | 0 | n/a | 0 (1 + -1) | n/a (no Y assigned) | singlet (no SU2W index) | singlet (no colour index) | n/a | B=0, L=0 | n/a | -1/2 from canonical normalization (Eq. 2, paper Lagrangian structure) | self-conjugate (real) |
| LWpKinMass (mass) | Wpbar[mu], Wp[mu] | 2 | Mwp^2 | 2 | n/a | 0 | n/a | singlet | singlet | n/a | B=0, L=0 | n/a | Mwp^2 from particle class Mass spec | self-conjugate (real) |
| LWpInt (quark) | uqbar[ff1,cc], dq[ff2,cc], Wp[mu], Ga[mu], ProjM/ProjP | 4 | gL*Sin[zeta]*VpL[ff1,ff2], gR*Cos[zeta]*Exp[I*omega]*VpR[ff1,ff2] | 0 | n/a | 0 (-2/3 - 1/3 + 1) | n/a | singlet (Wp is SU(2)_L singlet) | 3bar x 3 -> 1 (cc index contracted) | n/a | B=1/3 - 1/3 = 0 | n/a | 1/Sqrt[2] from Eq.(2) in paper: "1/Sqrt[2] fbar gamma_mu (...)" | HC[LWpInt] |
| LWpInt (lepton) | vlbar[ff1], l[ff2], Wp[mu], Ga[mu], ProjM/ProjP | 4 | gL*Sin[zeta]*VpL[ff1,ff2], gR*Cos[zeta]*Exp[I*omega]*VpR[ff1,ff2] | 0 | n/a | 0 (0 - 1 + 1) | n/a | singlet | singlet (no colour) | n/a | L=1 - 1 = 0 | n/a | 1/Sqrt[2] from Eq.(2) | HC[LWpInt] |
| HC[LWpInt] | (conjugate fields) | 4 | (conjugate couplings) | 0 | n/a | 0 | n/a | singlet | singlet | n/a | 0 | n/a | same as LWpInt | LWpInt |

**Additional audit rows:**

| Check | Result |
|---|---|
| New particle class kinetic+mass term | Wp (V[100]): LWpKinMass exists and is included in LTotal ✓ |
| Non-fundamental colour representation | None (Wp is colour singlet) ✓ |
| SelfConjugate -> True classes | None (Wp has SelfConjugate -> False) ✓ |
| Name collision check | Classes: Wp (V[100]). Parameters: Mwp, Wwp, gL, gR, zeta, omega, VpL, VpR. Indices: none new. None conflict with Mathematica built-ins (N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM), FeynRules symbols, or SM.fr names (H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,...) ✓ |
| Single total Lagrangian | LTotal := LWpKinMass + LWpInt + HC[LWpInt] ✓ |
| Reference/cached model files read | none (only paper/hep-ph_0207290_source.tex and SM.fr for conventions) ✓ |

Field mass dimensions used: scalar=1, vector=1, fermion=3/2, FS=2, del/DC=1, Ga=0, ProjP/M=0. All Q sums = 0. All SU(3) contractions are singlets. No new U(1) gauge groups. No charge-conjugation (CC[]) needed as paper uses standard Dirac notation.

**Last ./frgen result:**
```
SCHEMA OK: 1 particle classes, 8 parameters, Lagrangian terms ['LWpKinMass', 'LWpInt', 'LTotal']
RENDERED: model.fr (95 lines). You may read it.
LINT: no findings.
```