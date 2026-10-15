# Reconstruction of `sanitized.fr`

**Run tag:** XM-RECON-pNG__control

All statements below come only from the content of `sanitized.fr`. The file adds two
real scalar fields, two unphysical rotation placeholders, two external parameters and
four Lagrangian pieces on top of an unmodified `LSM`.

---

## 0. Conventions and notation

The file uses these FeynRules idioms:

| Idiom in file | Meaning used below |
| --- | --- |
| `del[X,mu]` | $\partial_\mu X$ (the repeated `mu` is contracted with $\eta^{\mu\nu}$) |
| `SelfConjugate -> True` | the field is real, $X^\dagger = X$ |
| `Unphysical -> True` with `Definitions` | a substitution rule; the field never survives to a vertex |
| `LSM` | the Standard Model Lagrangian of the base model file |
| `vev` | the SM electroweak vacuum expectation value $v \simeq 246\ \text{GeV}$ |
| `MH` | the SM-file Higgs mass parameter (the mass of `H`) |

**Idioms that are absent.** The file contains no `DC`, no `FS`, no `Ga`, no `HC`, no
`CC`, and no `ProjP`/`ProjM`. There are no fermions, no vectors and no gauge-index
contractions in the new sector. Every new field is a Lorentz scalar and a total
singlet of $SU(3)_C \times SU(2)_L \times U(1)_Y$, so every derivative in the new
terms is an ordinary derivative:

$$
D_\mu \chi = \partial_\mu \chi , \qquad D_\mu H_2 = \partial_\mu H_2 .
$$

For completeness, the gauge content of the covariant derivative that `LSM` supplies,
and which acts only on SM fields, is

$$
D_\mu = \partial_\mu
- i\, g_s\, T^a G^a_\mu
- i\, g\, T^I W^I_\mu
- i\, g'\, Y\, B_\mu ,
$$

with $T^a$ the $SU(3)_C$ generators, $T^I = \sigma^I/2$ the $SU(2)_L$ generators and
$Y$ the $U(1)_Y$ hypercharge. Both new scalars carry $(\mathbf{1},\mathbf{1},0)$, so
all three terms drop out for them.

**Mixing convention.** `phi1` and `s1` are eliminated by the substitutions

$$
\phi_1 \;=\; \cos\theta\, H \;+\; \sin\theta\, H_2 ,
\qquad
s_1 \;=\; -\sin\theta\, H \;+\; \cos\theta\, H_2 ,
$$

with $\theta \equiv$ `thx`, $\cos\theta \equiv$ `cxth`, $\sin\theta \equiv$ `sxth`.
This is the inverse of the mass-diagonalising rotation. Therefore $H$ and $H_2$ are
the two CP-even **mass eigenstates**, and $\phi_1$, $s_1$ are the CP-even **gauge
eigenstates**: $\phi_1$ is the neutral CP-even fluctuation of the $SU(2)_L$ doublet
and $s_1$ is the CP-even fluctuation of a gauge-singlet field.

---

## 1. Lagrangian, term by term

### 1.1 `LX` — free real scalar $\chi$

```
LX := Block[{mu}, 1/2 del[chi,mu] del[chi,mu] - 1/2 Mx^2 chi^2];
```

$$
\boxed{\;
\mathcal{L}_{\chi}
= \tfrac{1}{2}\,\partial_\mu \chi\, \partial^\mu \chi
\;-\; \tfrac{1}{2}\, M_\chi^{2}\, \chi^{2}
\;}
\qquad \text{(`LX`)}
$$

$\chi$ is real, so the kinetic and mass normalisations carry the $1/2$ of a real
scalar. $M_\chi \equiv$ `Mx`.

### 1.2 `LH2` — free real scalar $H_2$

```
LH2 := Block[{mu}, 1/2 del[H2,mu] del[H2,mu] - 1/2 MH2^2 H2^2];
```

$$
\boxed{\;
\mathcal{L}_{H_2}
= \tfrac{1}{2}\,\partial_\mu H_2\, \partial^\mu H_2
\;-\; \tfrac{1}{2}\, M_{H_2}^{2}\, H_2^{2}
\;}
\qquad \text{(`LH2`)}
$$

This is the kinetic and mass term of the second CP-even mass eigenstate. Its mass is
already diagonal, which confirms that $H_2$ (and $H$) are mass eigenstates.

### 1.3 `LPortal3` — cubic scalar portal

```
LPortal3 := -(1/2) chi^2 (lamPS*vev*phi1 + lamS*vs*s1);
```

In the gauge basis:

$$
\boxed{\;
\mathcal{L}_{3}
= -\tfrac{1}{2}\,\lambda_{\Phi S}\, v\, \phi_1\, \chi^{2}
\;-\; \tfrac{1}{2}\,\lambda_{S}\, v_s\, s_1\, \chi^{2}
\;}
\qquad \text{(`LPortal3`)}
$$

Substituting the rotation gives the mass basis:

$$
\mathcal{L}_{3}
= -\tfrac{1}{2}\,\chi^{2}\Big[
\big(\lambda_{\Phi S} v \cos\theta - \lambda_{S} v_s \sin\theta\big) H
+ \big(\lambda_{\Phi S} v \sin\theta + \lambda_{S} v_s \cos\theta\big) H_2
\Big].
$$

With the internal definitions of `lamPS` and `lamS` (Section 3) the two brackets
collapse to

$$
\lambda_{\Phi S} v \cos\theta - \lambda_{S} v_s \sin\theta
= -\,\frac{M_H^{2}\sin\theta}{v_s},
\qquad
\lambda_{\Phi S} v \sin\theta + \lambda_{S} v_s \cos\theta
= +\,\frac{M_{H_2}^{2}\cos\theta}{v_s},
$$

so the physical cubic portal is

$$
\boxed{\;
\mathcal{L}_{3}
= \frac{M_H^{2}\sin\theta}{2\,v_s}\; \chi^{2} H
\;-\; \frac{M_{H_2}^{2}\cos\theta}{2\,v_s}\; \chi^{2} H_2
\;}
$$

This exact form is the key result of the model; see Section 4.

### 1.4 `LPortal4` — quartic scalar portal and $\chi$ self-coupling

```
LPortal4 := -(1/4) lamPS phi1^2 chi^2 - (1/4) lamS s1^2 chi^2 - (1/8) lamS chi^4;
```

$$
\boxed{\;
\mathcal{L}_{4}
= -\tfrac{1}{4}\,\lambda_{\Phi S}\, \phi_1^{2}\, \chi^{2}
\;-\; \tfrac{1}{4}\,\lambda_{S}\, s_1^{2}\, \chi^{2}
\;-\; \tfrac{1}{8}\,\lambda_{S}\, \chi^{4}
\;}
\qquad \text{(`LPortal4`)}
$$

In the mass basis:

$$
\mathcal{L}_{4}
= -\tfrac{1}{4}\big(\lambda_{\Phi S}\cos^{2}\theta + \lambda_{S}\sin^{2}\theta\big) H^{2}\chi^{2}
-\tfrac{1}{2}\sin\theta\cos\theta\big(\lambda_{\Phi S} - \lambda_{S}\big) H H_2 \chi^{2}
-\tfrac{1}{4}\big(\lambda_{\Phi S}\sin^{2}\theta + \lambda_{S}\cos^{2}\theta\big) H_2^{2}\chi^{2}
-\tfrac{1}{8}\lambda_{S}\,\chi^{4}.
$$

### 1.5 `LTotal`

```
LTotal := LSM + LX + LH2 + LPortal3 + LPortal4;
```

$$
\boxed{\;
\mathcal{L}_{\text{tot}}
= \mathcal{L}_{\text{SM}}
+ \mathcal{L}_{\chi}
+ \mathcal{L}_{H_2}
+ \mathcal{L}_{3}
+ \mathcal{L}_{4}
\;}
\qquad \text{(`LTotal`)}
$$

### 1.6 The ultraviolet potential these terms come from

The four portal structures and their relative factors fix the parent potential
uniquely. Write a complex gauge singlet and the doublet as

$$
S = \frac{v_s + s_1 + i\,\chi}{\sqrt{2}},
\qquad
\Phi = \begin{pmatrix} G^{+} \\ \dfrac{v + \phi_1 + i\,G^{0}}{\sqrt{2}} \end{pmatrix},
\qquad
|S|^{2} = \tfrac{1}{2}\big[(v_s+s_1)^{2} + \chi^{2}\big].
$$

Then

$$
V \supset \lambda_{\Phi S}\,|\Phi|^{2}\,|S|^{2} \;+\; \frac{\lambda_{S}}{2}\,|S|^{4}
$$

reproduces every coefficient in `LPortal3` and `LPortal4` exactly:

| Structure | From $\lambda_{\Phi S}|\Phi|^2|S|^2$ | From $\tfrac{\lambda_S}{2}|S|^4$ | In file |
| --- | --- | --- | --- |
| $\phi_1\chi^2$ | $-\tfrac{1}{2}\lambda_{\Phi S} v$ | — | $-\tfrac{1}{2}\lambda_{\Phi S} v$ |
| $s_1\chi^2$ | — | $-\tfrac{1}{2}\lambda_{S} v_s$ | $-\tfrac{1}{2}\lambda_{S} v_s$ |
| $\phi_1^2\chi^2$ | $-\tfrac{1}{4}\lambda_{\Phi S}$ | — | $-\tfrac{1}{4}\lambda_{\Phi S}$ |
| $s_1^2\chi^2$ | — | $-\tfrac{1}{4}\lambda_{S}$ | $-\tfrac{1}{4}\lambda_{S}$ |
| $\chi^4$ | — | $-\tfrac{1}{8}\lambda_{S}$ | $-\tfrac{1}{8}\lambda_{S}$ |

So $\chi$ is the **imaginary (pseudoscalar) part** of a complex gauge-singlet scalar
$S$, and $s_1$ is its real part. The potential above is invariant under a global
$U(1)$ phase rotation of $S$. The mass term $-\tfrac{1}{2}M_\chi^2\chi^2$ of `LX` is
not generated by $\lambda_{\Phi S}$ or $\lambda_S$, and $M_\chi$ is declared as an
independent input. It therefore comes from a separate, soft $U(1)$-breaking term
(of the $S^2 + \text{h.c.}$ type), which the file does not write out because it only
contributes this diagonal mass.

**Caveat on the portal terms.** `LPortal3` and `LPortal4` use $\phi_1$, the CP-even
neutral component only. The would-be Goldstone couplings $G^0 G^0 \chi^2$,
$G^+ G^- \chi^2$ contained in the full $\lambda_{\Phi S}|\Phi|^2|S|^2$ are not
written. The file therefore encodes the portal in the unitary gauge.

**Caveat on the SM sector.** `LSM` is added unchanged, so $H$ keeps full-strength SM
Yukawa and gauge couplings. Strict diagonalisation would instead attach the SM
couplings to $\phi_1 = \cos\theta\,H + \sin\theta\,H_2$, that is, factors $\cos\theta$
for $H$ and $\sin\theta$ for $H_2$. This rescaling is not applied in the file.

---

## 2. Field table

| Symbol | Class | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)_Y$ | Self-conjugate | Mass symbol | Mass value | Width | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chi` ($\chi$) | `S[101]` | 0 (real scalar) | $\mathbf{1}$ | $\mathbf{1}$ (not declared) | $0$ (not declared) | yes | `Mx` | $62.573$ GeV | $0$ (stable) | 52 |
| `H2` ($H_2$) | `S[102]` | 0 (real scalar) | $\mathbf{1}$ | $\mathbf{1}$ (not declared) | $0$ (not declared) | yes | `MH2` | $125.30$ GeV | `WH2` $= 0$ | 35 |
| `phi1` ($\phi_1$) | `S[103]` | 0 (real scalar) | — | — | — | yes | none (unphysical) | — | — | — |
| `s1` ($s_1$) | `S[104]` | 0 (real scalar) | — | — | — | yes | none (unphysical) | — | — | — |

Notes:

- No `Indices` entry appears for any class, so `chi` and `H2` are total gauge
  singlets. The $SU(2)_L$ and $U(1)_Y$ columns are blank in the file and are filled
  here with the only consistent assignment.
- `PropagatorType -> D` and `PropagatorArrow -> None` confirm real scalar lines.
- `phi1` and `s1` carry `Unphysical -> True`, so they are pure substitution
  placeholders. They receive no propagator and no quantum numbers. Physically
  $\phi_1$ sits in the $SU(2)_L$ doublet ($\mathbf{1},\mathbf{2},1/2$ before
  symmetry breaking) and $s_1$ in the complex gauge singlet.
- `chi` has zero width and no decay channel in `LTotal`: it is absolutely stable.
  The residual $\mathbb{Z}_2$ symmetry $\chi \to -\chi$ (every $\chi$ in the
  Lagrangian appears in an even power) protects it. That $\mathbb{Z}_2$ is the
  unbroken remnant of the global $U(1)$ acting on $S$.
- $M_\chi = 62.573\ \text{GeV} \simeq M_{H_2}/2 = 62.65\ \text{GeV}$. The benchmark
  point sits on the $H_2$ resonance.

---

## 3. Parameters

### 3.1 External parameters (block `PNGDM`)

| Symbol | Order | Value | What it multiplies | Physical meaning |
| --- | --- | --- | --- | --- |
| `vs` ($v_s$) | 1 | $13155.1$ GeV | enters `lamPS`, `lamS`, and the $s_1\chi^2$ cubic through $\lambda_S v_s$ | vacuum expectation value of the complex gauge singlet $S$; it sets the scale of the hidden sector |
| `thx` ($\theta$) | 2 | $1.53$ (radians) | enters through $\sin\theta$, $\cos\theta$ in the `phi1`/`s1` substitutions and in `lamPS`, `lamS` | mixing angle between the doublet state $\phi_1$ and the singlet state $s_1$; it rotates the gauge basis into the mass basis $(H, H_2)$ |

Numerically $\sin\theta = 0.99917$ and $\cos\theta = 0.04079$, so $\theta$ is close to
$\pi/2$. From $\phi_1 = \cos\theta\,H + \sin\theta\,H_2$, the doublet content sits
almost entirely in $H_2$. So $H_2$ at $125.30$ GeV is the SM-Higgs-like state, and
$H$ is the mostly-singlet state.

Two further external quantities are used but declared elsewhere (in the base SM
file): `vev` ($v$, the electroweak VEV) and `MH` (the mass of `H`). `Mx`, `MH2` and
`WH2` are external mass and width parameters created by the `Mass`/`Width` entries of
the class declarations.

### 3.2 Internal (derived) parameters

| Symbol | Definition | What it multiplies | Physical meaning |
| --- | --- | --- | --- |
| `sxth` | $\sin\theta$ | the `phi1`, `s1` substitutions and both $\lambda$'s | sine of the scalar mixing angle |
| `cxth` | $\cos\theta$ | the `phi1`, `s1` substitutions and both $\lambda$'s | cosine of the scalar mixing angle |
| `lamPS` ($\lambda_{\Phi S}$) | $\dfrac{(M_{H_2}^{2}-M_H^{2})\sin\theta\cos\theta}{v\,v_s}$ | $\phi_1\chi^2$ and $\phi_1^2\chi^2$ | Higgs-portal quartic coupling $\lambda_{\Phi S}|\Phi|^2|S|^2$. It is fixed by the off-diagonal CP-even mass-matrix element: $\lambda_{\Phi S} v\, v_s = (M_{H_2}^2 - M_H^2)\sin\theta\cos\theta$. `InteractionOrder` $\{NP,2\}$ |
| `lamS` ($\lambda_{S}$) | $\dfrac{M_H^{2}\sin^{2}\theta + M_{H_2}^{2}\cos^{2}\theta}{v_s^{2}}$ | $s_1\chi^2$, $s_1^2\chi^2$, $\chi^4$ | singlet quartic self-coupling $\tfrac{\lambda_S}{2}|S|^4$. It is fixed by the singlet diagonal mass-matrix element: $\lambda_S v_s^2 = M_H^2\sin^2\theta + M_{H_2}^2\cos^2\theta$. `InteractionOrder` $\{NP,2\}$ |

Both internal couplings are therefore not free. They are traded for the physical
inputs $(M_H, M_{H_2}, \theta, v_s, v)$ by inverting the CP-even mass matrix

$$
\mathcal{M}^{2}
= \begin{pmatrix}
\lambda_{\Phi S}\,v\,v_s \big/ \tan(2\theta)\text{-fixed diagonal} & \lambda_{\Phi S}\, v\, v_s \\[2pt]
\lambda_{\Phi S}\, v\, v_s & \lambda_{S}\, v_s^{2}
\end{pmatrix}
= R(\theta)\,
\begin{pmatrix} M_H^{2} & 0 \\ 0 & M_{H_2}^{2}\end{pmatrix}\,
R(\theta)^{T},
\qquad
R(\theta)=\begin{pmatrix}\cos\theta & \sin\theta\\ -\sin\theta & \cos\theta\end{pmatrix}.
$$

Reading off the $(s_1,s_1)$ and $(\phi_1,s_1)$ entries of $R\,\text{diag}\,R^T$
reproduces `lamS` and `lamPS` exactly, which is an internal consistency check of the
reconstruction.

### 3.3 Interaction-order hierarchy

```
{QCD, 1}, {QED, 2}, {NP, 1}
```

New-physics vertices are counted with `NP`; both portal couplings carry `NP` order 2.

---

## 4. Physics summary

This is a **pseudo-Nambu-Goldstone scalar dark matter** model. A complex gauge-singlet
scalar $S$ with a global $U(1)$ symmetry is added to the Standard Model. $S$ takes a
large vacuum expectation value $v_s = 13.2$ TeV. Its real part $s_1$ mixes with the
CP-even neutral component $\phi_1$ of the Higgs doublet through the portal coupling
$\lambda_{\Phi S}|\Phi|^2|S|^2$, giving two mass eigenstates: $H_2$ at $125.30$ GeV,
which is doublet-dominated and therefore the observed Higgs boson, and $H$, which is
singlet-dominated. Its imaginary part $\chi$ is the pseudo-Goldstone boson of the
$U(1)$; a soft $U(1)$-breaking term gives it the mass $M_\chi = 62.573$ GeV, and the
residual $\mathbb{Z}_2$ ($\chi \to -\chi$) makes it an absolutely stable dark matter
candidate.

The model mediates dark matter annihilation $\chi\chi \to H/H_2 \to \text{SM}\,\text{SM}$
through the cubic vertices of `LPortal3`, plus the contact processes
$\chi\chi \to HH$, $HH_2$, $H_2H_2$ from `LPortal4`. Because
$M_\chi \simeq M_{H_2}/2$, the benchmark point sits on the $H_2$ resonance, where
annihilation is strongly enhanced. At colliders it produces invisible Higgs decays
$H_2 \to \chi\chi$ (kinematically marginal at this point), invisible decays of the
singlet-like $H$, and Higgs-signal-strength shifts from the $\theta$ mixing.

The defining feature is the behaviour in **direct detection**. Using the mass-basis
cubic couplings of Section 1.3 and the doublet fractions $\cos\theta$ for $H$ and
$\sin\theta$ for $H_2$, the spin-independent $\chi$-quark amplitude at zero momentum
transfer is

$$
\mathcal{A} \;\propto\;
\underbrace{\Big(-\frac{M_H^{2}\sin\theta}{v_s}\Big)}_{\chi\chi H}
\frac{\cos\theta}{M_H^{2}}
\;+\;
\underbrace{\Big(+\frac{M_{H_2}^{2}\cos\theta}{v_s}\Big)}_{\chi\chi H_2}
\frac{\sin\theta}{M_{H_2}^{2}}
\;=\;
-\frac{\sin\theta\cos\theta}{v_s} + \frac{\sin\theta\cos\theta}{v_s}
\;=\; 0 .
$$

The two Higgs exchange diagrams cancel exactly. The tree-level spin-independent
direct-detection cross section vanishes in the zero-momentum-transfer limit and
survives only through the momentum-transfer suppression $\propto t$ and through loop
corrections. This is the standard pseudo-Goldstone mechanism that lets a Higgs-portal
dark matter candidate keep a thermal relic abundance while evading
xenon-target direct-detection limits.
