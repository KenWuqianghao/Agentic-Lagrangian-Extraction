# Reconstruction of `sanitized.fr`

All statements below come from the content of the single file `sanitized.fr`.
No model name, author or comment text was available.

## 0. Conventions used here

- Metric signature `(+,-,-,-)` (the FeynRules default). Repeated Lorentz indices in
  the `.fr` source are contracted with this metric, so `X[mu] X[mu]` means
  $X_\mu X^\mu$.
- `Eps[mu,nu,la,rho]` is the totally antisymmetric Levi-Civita tensor
  $\epsilon^{\mu\nu\lambda\rho}$ (FeynRules default sign convention).
- `del[f,mu]` is $\partial_\mu f$. The index written inside `del[...]` is the
  derivative index, **not** the field index.
- `FS[X,mu,nu]` is the field strength of the field `X`.
- `sw`, `cw`, `sw2` are the SM parameters $s_W=\sin\theta_W$, $c_W=\cos\theta_W$,
  $s_W^2$. `MZ`, `MW` are the SM boson masses. `Z[mu]`, `A[mu]` are the SM mass
  eigenstates $Z_\mu$ and the photon $A_\mu$.
- The model is written **after** electroweak symmetry breaking, in terms of the
  mass eigenstates $Z_\mu$ and $A_\mu$.

## 1. Lagrangian

The total Lagrangian in the file is

$$
\mathcal{L}_{\rm Total}
= \mathcal{L}_{\rm SM}
+ \mathcal{L}_{X\rm kin}
+ \mathcal{L}_{\rm PortalNeutral}
+ \big(\mathcal{L}_{\rm PortalCharged}\big)^{\dagger}
$$

(`LTotal := LSM + LXkin + LPortalNeutral + HC[LPortalCharged]`).

**Important defect in the file:** the symbol `LPortalCharged` is used in `LTotal`
but it is **never defined** anywhere in `sanitized.fr`. The file is therefore
incomplete. Section 1.4 reconstructs the missing term from the remaining
evidence (the unused parameter `c2` and the $W$ term in the width `WX`).

### 1.1 `LXkin` — free massive vector

```
LXkin := -1/4 FS[X,mu,nu] FS[X,mu,nu] + 1/2 MX^2 X[mu] X[mu]
```

$$
\mathcal{L}_{X\rm kin}
= -\frac{1}{4}\,X_{\mu\nu}X^{\mu\nu}
  + \frac{1}{2}\,M_X^{2}\,X_\mu X^\mu ,
\qquad
X_{\mu\nu}\equiv \partial_\mu X_\nu-\partial_\nu X_\mu .
$$

This is a Proca Lagrangian. `X` is **not** declared as a gauge boson of any gauge
group, so `FS[X,mu,nu]` is the abelian (linear) field strength with no
self-coupling term. The mass term is put in by hand; there is no Higgs or
Stueckelberg field for `X` in this file.

### 1.2 `LPortalNeutral`, first term — $ZZX$ Chern-Simons coupling

```
-c1 sw Eps[mu,nu,la,rho] Z[mu] X[nu] del[Z[rho],la]
```

$$
\mathcal{L}_{\rm PortalNeutral}^{(ZZX)}
= -\,c_1 s_W\;\epsilon^{\mu\nu\lambda\rho}\,
   Z_\mu\,X_\nu\,\big(\partial_\lambda Z_\rho\big).
$$

Because $\epsilon^{\mu\nu\lambda\rho}$ is antisymmetric in $\lambda\rho$, only the
antisymmetric part of $\partial_\lambda Z_\rho$ contributes, so this is equal to

$$
\mathcal{L}_{\rm PortalNeutral}^{(ZZX)}
= -\,\frac{c_1 s_W}{2}\;\epsilon^{\mu\nu\lambda\rho}\,
   Z_\mu\,X_\nu\,Z_{\lambda\rho},
\qquad Z_{\lambda\rho}=\partial_\lambda Z_\rho-\partial_\rho Z_\lambda .
$$

This is a Chern-Simons (anomalous, $CP$-odd-structure) triple-gauge vertex. It is
**not** of the form $\epsilon\,\partial(ZZ)$, which would vanish; the surviving
structure is $\epsilon\,X\,Z\,\tilde{Z}$-like and is non-zero for two on-shell
$Z$ bosons.

### 1.3 `LPortalNeutral`, second term — $Z\gamma X$ Chern-Simons coupling

```
+c1 cw Eps[mu,nu,la,rho] Z[mu] X[nu] del[A[rho],la]
```

$$
\mathcal{L}_{\rm PortalNeutral}^{(Z\gamma X)}
= +\,c_1 c_W\;\epsilon^{\mu\nu\lambda\rho}\,
   Z_\mu\,X_\nu\,\big(\partial_\lambda A_\rho\big)
= +\,\frac{c_1 c_W}{2}\;\epsilon^{\mu\nu\lambda\rho}\,
   Z_\mu\,X_\nu\,F_{\lambda\rho},
$$

with $F_{\lambda\rho}=\partial_\lambda A_\rho-\partial_\rho A_\lambda$.

**Compact form of the whole neutral portal.** The two terms have exactly the
weak-mixing structure of the hypercharge field
$B_\rho = c_W A_\rho - s_W Z_\rho$. The full neutral portal is therefore the
single operator

$$
\boxed{\;
\mathcal{L}_{\rm PortalNeutral}
= c_1\,\epsilon^{\mu\nu\lambda\rho}\,Z_\mu\,X_\nu\,\partial_\lambda B_\rho
\;}
$$

i.e. one Chern-Simons term coupling $X$ to one $Z$ and one hypercharge field,
written out in mass eigenstates. There is **no** $\gamma\gamma X$ term in the
file, and no $X$ coupling to gluons, fermions or the Higgs.

### 1.4 `LPortalCharged` — referenced but missing

`LTotal` adds `HC[LPortalCharged]`, but no definition of `LPortalCharged` exists
in the file. Two independent pieces of evidence fix what it must have contained:

- The external parameter `c2` appears in **no** Lagrangian term present in the
  file. It appears only inside the internal width `WX`.
- The `c2` term of `WX` carries $1/M_W^2$ and the phase-space factor
  $(1-4M_W^2/M_X^2)^{5/2}$, i.e. the decay $X\to W^+W^-$ into two equal-mass
  bosons.

The missing term is therefore the charged-current partner of the neutral
Chern-Simons portal, of the form

$$
\mathcal{L}_{\rm PortalCharged}
= c_2\,\epsilon^{\mu\nu\lambda\rho}\,W^-_\mu\,X_\nu\,\partial_\lambda W^+_\rho
\;\;(+\text{h.c.}),
$$

i.e. `c2 Eps[mu,nu,la,rho] W[mu] X[nu] del[Wbar[rho],la]` in FeynRules notation.
The hermitian conjugate exchanges $W^+\leftrightarrow W^-$, which makes the sum
real. The overall normalisation of $c_2$ (a factor of order one) cannot be fixed
from the file alone: the $W$ term of `WX` is 4 times the $ZZ$ term at equal
coupling and equal mass, which is consistent with the loss of the
identical-particle factor $1/2$ together with the h.c. doubling, but the file
gives no direct check.

### 1.5 Covariant derivative content

No `DC[...]` appears anywhere in the file. All derivatives are plain partial
derivatives `del[...]` acting on the mass eigenstates $Z_\mu$ and $A_\mu$.

For the new field, `X` carries no `Indices` and no `QuantumNumbers`, so it is a
complete singlet of $SU(3)_C\times SU(2)_L\times U(1)_Y$ and

$$
D_\mu X_\nu = \partial_\mu X_\nu .
$$

The SM covariant derivative is the unmodified one inherited from `LSM`:

$$
D_\mu = \partial_\mu - i g_s T^a G^a_\mu - i g\,T^i W^i_\mu - i g' Y B_\mu ,
$$

with $Z_\mu = c_W W^3_\mu - s_W B_\mu$ and $A_\mu = s_W W^3_\mu + c_W B_\mu$.
The portal operators are written directly in terms of $Z_\mu$, $A_\mu$ and (for
the missing term) $W^\pm_\mu$; they are not built with `DC`.

## 2. Field table

One new particle class is declared.

| Symbol | Class | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)$ charge / hypercharge | Self-conjugate | Mass | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|
| $X_\mu$ | `V[101]`, `ClassName -> X` | 1 (vector) | singlet (no colour index declared) | not declared — this is a post-EWSB mass eigenstate, an $SU(2)_L$ singlet | 0 (no `QuantumNumbers` declared; electrically neutral) | **True** (real vector field) | `MX` $=1000.$ GeV | `WX`, `Internal` | 5000023 |

Drawing attributes only: `ParticleName -> "X"`, `PropagatorLabel -> "X"`,
`PropagatorType -> Sine`, `PropagatorArrow -> None`. These carry no physics.

No new fermions, no new scalars, no new gauge group. All SM fields are unchanged
and come from `LSM`.

## 3. Parameters

### External

| Symbol | Block | Value | Interaction order | Multiplies | Physical meaning |
|---|---|---|---|---|---|
| `c1` | `NPCOUPLINGS`, entry 1 | $1.0$ | `{NP,1}` | $\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda Z_\rho$ (with $-s_W$) and $\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda A_\rho$ (with $+c_W$) | Dimensionless Chern-Simons coupling of $X$ to the neutral electroweak bosons; equivalently the coefficient of the single operator $\epsilon\,Z X \partial B$ |
| `c2` | `NPCOUPLINGS`, entry 2 | $1.0$ | `{NP,1}` | nothing in the file as it stands; it belongs to the missing `LPortalCharged` ($\epsilon^{\mu\nu\lambda\rho}W^-_\mu X_\nu\partial_\lambda W^+_\rho$), and it enters the width `WX` | Dimensionless Chern-Simons coupling of $X$ to the charged $W^\pm$ bosons |

Both are dimensionless: the operators $\epsilon\,V V \partial V$ have mass
dimension 4.

`MX` is also an external input, declared inside the particle class:
`Mass -> {MX, 1000.}`, the $X$ pole mass in GeV.

### Internal

`WX` — the total width of $X$, computed at tree level as the sum of three
partial widths:

$$
\Gamma_X
= \underbrace{\frac{c_1^{2}s_W^{2}M_X^{3}}{192\pi M_Z^{2}}
  \Big(1-\frac{4M_Z^{2}}{M_X^{2}}\Big)^{5/2}}_{X\to ZZ}
\;+\;
\underbrace{\frac{c_2^{2}M_X^{3}}{48\pi M_W^{2}}
  \Big(1-\frac{4M_W^{2}}{M_X^{2}}\Big)^{5/2}}_{X\to W^+W^-}
\;+\;
\underbrace{\frac{c_1^{2}c_W^{2}M_X^{3}}{96\pi M_Z^{2}}
  \Big(1-\frac{M_Z^{2}}{M_X^{2}}\Big)^{3}\Big(1+\frac{M_Z^{2}}{M_X^{2}}\Big)}_{X\to Z\gamma}
$$

Channel identification is fixed by the couplings and the phase space:
the $c_1^2 s_W^2$ term with $(1-4M_Z^2/M_X^2)^{5/2}$ is $ZZ$; the $c_2^2$ term
with $(1-4M_W^2/M_X^2)^{5/2}$ is $W^+W^-$; the $c_1^2 c_W^2$ term with the
one-massive-one-massless factor $(1-M_Z^2/M_X^2)^3$ is $Z\gamma$. The $\beta^5$
behaviour of the two-massive-boson channels and the $1/M_V^2$ prefactors are the
longitudinal-enhancement signature of Chern-Simons vertices. There is no
$X\to\gamma\gamma$ term, consistent with the absence of a $\gamma\gamma X$
operator.

### Interaction order hierarchy

```
{QCD,1}, {QED,2}, {NP,1}
```

A new counting label `NP` is introduced; every portal coupling carries `NP = 1`,
so any amplitude with one $X$ leg is first order in `NP`.

## 4. Physics summary

This is a minimal "Chern-Simons portal" model: a single new, electrically
neutral, colour-singlet, self-conjugate massive spin-1 boson $X$ with
$M_X = 1$ TeV, added to the unmodified Standard Model. $X$ has no couplings to
quarks, leptons, gluons or the Higgs; its only interactions are dimension-4
Levi-Civita (Chern-Simons) triple-gauge vertices with the electroweak gauge
bosons: $c_1$ gives $XZZ$ and $XZ\gamma$ (together one operator
$\epsilon\,Z X \partial B$), and $c_2$ gives $XW^+W^-$.

Phenomenologically, $X$ is produced from electroweak vector-boson fusion or from
associated $VX$ production and decays back into gauge-boson pairs, so it would
appear as a TeV resonance in the $ZZ$, $W^+W^-$ and $Z\gamma$ channels, with the
characteristic $\epsilon$-tensor angular structure. The three-channel width
formula in the file assumes exactly these final states.

**Caveat carried forward:** the file as given cannot be loaded as-is. The term
`LPortalCharged` in `LTotal` has no definition, so the $XW^+W^-$ vertex that the
$c_2$ parameter and the second term of `WX` both require is absent from the
Lagrangian. Section 1.4 gives the reconstructed form of that missing term.
