**Self-audit table:**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNKin_kin | NuH, NuH | 4 | 1 (implicit) | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LNKin_mass | NuH, NuH | 4 | MNuH | 1 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LIntW | W, NuH, l | 4 | gw·Vmix* | 0 | n/a | 0 | 0 | charged current (LL[2]·W⁺) | singlet | n/a | 1 (L violated by mixing) | yes | Eq.(2.4), LaTeX l.224-225 | HC[LIntW] |
| LIntZ | Z, NuH, vl | 4 | gw/(2cw)·Vmix* | 0 | n/a | 0 | 0 | neutral current (LL[1]·Z) | singlet | n/a | 1 (L violated) | yes | Eq.(2.4), LaTeX l.226-227 | HC[LIntZ] |
| LIntH | H, NuH, vl | 4 | gw·MNuH/(2MW)·Vmix* | 0 | n/a | 0 | 0 | Yukawa (LL[1]·Φ[2]) | singlet | n/a | 1 (L violated) | yes | Eq.(2.4), LaTeX l.228 | HC[LIntH] |

**SelfConjugate→True classes with no QuantumNumbers:** NuH (F[100]) — confirmed `QuantumNumbers -> {}`.

**Name collision check:** Class `NuH`, parameters `MNuH`, `Vmix`, width symbol `WNuH`, index `HeavyGeneration`/`hg`, class member `N1` — none are Mathematica built-ins (N, C, D, E, I, K, O, HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM), FeynRules symbols, or SM.fr names (H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, MZ, MW, etc.). Note: `N` is a built-in; we used `NuH` instead.

**Total Lagrangian:** `LTotal = LNKin + LIntW + LIntZ + LIntH + HC[LIntW + LIntZ + LIntH]` — single `LTotal` summing all terms.

**Reference model file read:** none.

model.fr is written.