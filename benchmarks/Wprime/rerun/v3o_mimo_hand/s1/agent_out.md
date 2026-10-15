## Self-audit (pre-write, re-verified against written `model.fr`)

| # | Term | Field content | ΣQ | ΣY | B−L | Colour | Lorentz structure | Coefficient | Coupling / order | Paper ref | Hermitian? | New indices | 1/Λⁿ ops | Status |
|---|------|---------------|----|----|-----|--------|-------------------|-------------|------------------|-----------|-----------|------------|----------|--------|
| 1 | LWpkin (kinetic) | Wpbar[mu], Wp[nu] | 1+(−1)=0 | 0+0=0 | 0 | singlet | −½ FS[Wpbar,mu,nu] FS[Wp,mu,nu] | −1/2 | — (free) | Eq.(2) kinetic | yes (real) | none | none | PASS |
| 2 | LWpkin (mass) | Wpbar[mu], Wp[mu] | 1+(−1)=0 | 0+0=0 | 0 | singlet | MWp² Wpbar[mu] Wp[mu] | MWp²=500.² | — (free) | MWp=500 GeV | yes (real) | none | none | PASS |
| 3 | Lnurkin (kinetic) | nurbar, nur | 1+(−1)=0 | 0+0=0 | 1−1=0 | singlet | I nurbar.Ga[mu].DC[nur,mu] | I | — (free) | Dirac ν_R | yes (via DC) | Generation | none | PASS |
| 4 | Lnurkin (mass) | nurbar, nur | 1+(−1)=0 | 0+0=0 | 1−1=0 | singlet | −Mnur nurbar.nur | −Mnur=0. | — (free) | m_νR=0 | yes (real) | Generation | none | PASS |
| 5 | LWpF q q (right) | uqbar, dq, Wp[mu] | −⅔+⅓+1=0 | ⅓−⅓−1+1…→0 | 0 | 3×3̄→1 | uqbar.VRq.Ga[mu].ProjP.dq Wp[mu] | 1/√2 · gR · Cos[zeta] · Exp[I omega] | gR:{NP,1} | Eq.(2) P_R term | yes (+HC) | Generation | none | PASS |
| 6 | LWpF ℓ ℓ (right) | nurbar, l, Wp[mu] | 1+(−1)+1…→0 | 0+0+0…→0 | 1−1=0 | singlet | nurbar.VRl.Ga[mu].ProjP.l Wp[mu] | 1/√2 · gR · Cos[zeta] · Exp[I omega] | gR:{NP,1} | Eq.(2) P_R, V′_lν=1 | yes (+HC) | Generation | none | PASS |
| 7 | LWpF q q (left) | uqbar, dq, Wp[mu] | −⅔+⅓+1=0 | →0 | 0 | 3×3̄→1 | uqbar.VLq.Ga[mu].ProjM.dq Wp[mu] | 1/√2 · gL · Sin[zeta] | gL:{NP,1} | Eq.(2) P_L term | yes (+HC) | Generation | none | PASS |
| 8 | LWpF ℓ ℓ (left) | vlbar, l, Wp[mu] | 0 | →0 | 0 | singlet | vlbar.VLl.Ga[mu].ProjM.l Wp[mu] | 1/√2 · gL · Sin[zeta] | gL:{NP,1} | Eq.(2) P_L, V′_lν=1 | yes (+HC) | Generation | none | PASS |

Additional checks:
- AddGaugeRepresentation: none needed (no non-fundamental colour representations).
- SelfConjugate→True classes: none (Wp complex, nur Dirac → all SelfConjugate->False).
- Names used (no SM/built-in clashes): `Wprime_gen`, `Wp`/`Wpbar`, `nur`/`Nur1..3`/`Nur1bar..3bar`, `gR`,`gL`,`zeta`,`omega`,`VLq`,`VRq`,`VLl`,`VRl`, blocks `WPRIME`/`VLBLOCK`/`VRBLOCK`; no primes/punctuation in ParticleName.
- LTotal := LWpkin + Lnurkin + LWpF (single sum of all other terms).
- Reference/cached .fr files read: none (only `SM.fr`).

model.fr is written.