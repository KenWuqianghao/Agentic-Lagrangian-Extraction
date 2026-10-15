# Reconstruction of `sanitized.fr`

A Standard Model extension with **one new state**: a heavy, electrically neutral,
self-conjugate massive vector $X_\mu$ (a Proca field, SM gauge singlet). It has **no
gauge couplings and no fermion couplings**. It talks to the SM only through two
parity-odd, Levi-Civita ("Chern-Simons"-type) trilinear gauge operators: one in the
neutral sector ($c_1$) and one in the charged sector ($c_2$).

Conventions used below:

- Metric $\eta_{\mu\nu} = (+,-,-,-)$. In FeynRules a repeated index is contracted with
  the metric, so `Eps[mu,nu,la,rho] Z[mu] X[nu] del[Z[rho],la]` means
  $\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \,\partial_\lambda Z_\rho$
  (note the index order: the derivative index `la` is the **third** slot of `Eps`,
  the differentiated field carries the **fourth**).
- `del[f,la]` $= \partial_\lambda f$.
- $s_W \equiv$ `sw` $=\sin\theta_W$, $c_W \equiv$ `cw` $=\cos\theta_W$,
  `sw2` $= s_W^2$.
- SM field names follow the FeynRules SM: `A` = photon, `Z` = $Z^0$,
  `W` = $W^+$, `Wbar` = $W^-$ (so `HC` maps $W^+ \leftrightarrow W^-$).
- $\epsilon^{\mu\nu\lambda\rho}$ is the totally antisymmetric tensor with the
  FeynRules sign convention.

---

## 1. Lagrangian

### 1.1 `LXkin` — free Proca Lagrangian for $X$

`FS[X,mu,nu]` is the abelian field strength of a self-conjugate vector. $X$ carries **no**
gauge quantum numbers, so no covariant derivative is generated:

$$
X_{\mu\nu} \;=\; \partial_\mu X_\nu - \partial_\nu X_\mu .
$$

$$
\boxed{\;
\mathcal{L}_{\texttt{LXkin}}
\;=\;
-\frac{1}{4}\,X_{\mu\nu}X^{\mu\nu}
\;+\;\frac{1}{2}\,M_X^{2}\,X_\mu X^\mu
\;}
$$

The relative sign and the $\tfrac12$ (instead of $M^2 X^\dagger X$) are the correct
normalisation for a **real** (self-conjugate) vector.

**Covariant-derivative content.** The file contains **no** `DC[...]` at all. The only
derivative structures are the abelian `FS[X,mu,nu]` above and the plain `del[...,la]`
in the portal terms. $X$ is a singlet of $SU(3)_c \times SU(2)_L \times U(1)_Y$, so its
covariant derivative degenerates to $D_\mu X_\nu = \partial_\mu X_\nu$. All SM covariant
derivatives (gluon $g_s T^a G^a_\mu$, weak $i g \,T^a W^a_\mu$, hypercharge
$i g' Y B_\mu$) enter only through the inherited `LSM`, which this file does not modify.

### 1.2 `LPortalNeutral` — neutral Chern-Simons portal ($c_1$)

Source line (verbatim structure):
`2 ( -c1 sw Eps[mu,nu,la,rho] Z[mu] X[nu] del[Z[rho],la] + c1 cw Eps[mu,nu,la,rho] Z[mu] X[nu] del[A[rho],la] )`

$$
\boxed{\;
\mathcal{L}_{\texttt{LPortalNeutral}}
\;=\;
2\,c_1\,\epsilon^{\mu\nu\lambda\rho}\,
\Big[\,
-\,s_W\, Z_\mu\, X_\nu\, \partial_\lambda Z_\rho
\;+\; c_W\, Z_\mu\, X_\nu\, \partial_\lambda A_\rho
\,\Big]
\;}
$$

Written as the two separate vertices it generates:

$$
\mathcal{L}_{ZZX} \;=\; -\,2\,c_1 s_W\,
\epsilon^{\mu\nu\lambda\rho}\, Z_\mu\, X_\nu\, \partial_\lambda Z_\rho ,
\qquad
\mathcal{L}_{Z\gamma X} \;=\; +\,2\,c_1 c_W\,
\epsilon^{\mu\nu\lambda\rho}\, Z_\mu\, X_\nu\, \partial_\lambda A_\rho .
$$

**Compact (weak-basis) form.** Using $A_\rho = s_W W^3_\rho + c_W B_\rho$ and
$Z_\rho = c_W W^3_\rho - s_W B_\rho$, one has the identity
$s_W Z_\rho - c_W A_\rho = -B_\rho$, so the whole neutral portal collapses to a single
operator built on the **hypercharge** field:

$$
\mathcal{L}_{\texttt{LPortalNeutral}}
\;=\; 2\,c_1\, \epsilon^{\mu\nu\lambda\rho}\, Z_\mu\, X_\nu\, \partial_\lambda B_\rho
\;=\; 2\,c_1\, \epsilon^{\mu\nu\lambda\rho}\,
\big(c_W W^3_\mu - s_W B_\mu\big)\, X_\nu\, \partial_\lambda B_\rho .
$$

This is the generalized-Chern-Simons ("anomaly-type") trilinear structure
$\epsilon\, V\, X\, \partial V'$.

**Hermiticity.** $Z$, $A$, $B$ and $X$ are all real fields and $c_1$ is real, so this term
is Hermitian by itself. Consistently, the file does **not** add `HC[LPortalNeutral]`.

**Vertex remark (index antisymmetry).** In $\mathcal{L}_{ZZX}$ the two $Z$ legs are
identical, so both Wick contractions contribute. For $X_\nu \to Z_\alpha(p_1) Z_\beta(p_2)$
the Feynman rule is proportional to
$\epsilon^{\alpha\nu\lambda\beta}\,(p_2-p_1)_\lambda$; the term is **not** a total
derivative, because the candidate total derivative
$\partial_\lambda(\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu Z_\rho)$ vanishes identically
($Z_\mu Z_\rho$ is symmetric against the antisymmetric $\epsilon$).

### 1.3 `LPortalCharged` (+ `HC`) — charged Chern-Simons portal ($c_2$)

$$
\boxed{\;
\mathcal{L}_{\texttt{LPortalCharged}}
\;=\;
c_2\,\epsilon^{\mu\nu\lambda\rho}\,
W^{+}_{\mu}\, X_\nu\, \partial_\lambda W^{-}_{\rho}
\;}
$$

$$
\boxed{\;
\mathcal{L}_{\texttt{HC[LPortalCharged]}}
\;=\;
c_2^{*}\,\epsilon^{\mu\nu\lambda\rho}\,
W^{-}_{\mu}\, X_\nu\, \partial_\lambda W^{+}_{\rho}
\;}
$$

`HC` swaps $W^+ \leftrightarrow W^-$ and conjugates $c_2$; $X$ is self-conjugate and
$\epsilon^{\mu\nu\lambda\rho}$ is real, so the pair above is the full Hermitian
$XW^+W^-$ interaction. With $c_2$ declared real (`Value -> 1.`, real external
parameter) the sum gives the vertex

$$
\mathcal{L}_{XWW}^{\rm tot}
= c_2\,\epsilon^{\mu\nu\lambda\rho}\,X_\nu
\big( W^{+}_{\mu}\partial_\lambda W^{-}_{\rho} + W^{-}_{\mu}\partial_\lambda W^{+}_{\rho}\big),
$$

whose $X_\nu W^+_\alpha(p_1) W^-_\beta(p_2)$ Feynman rule is again proportional to
$\epsilon^{\alpha\nu\lambda\beta}(p_2-p_1)_\lambda$.

### 1.4 `LTotal`

$$
\boxed{\;
\mathcal{L}_{\texttt{LTotal}}
=\mathcal{L}_{\rm SM}
+\mathcal{L}_{\texttt{LXkin}}
+\mathcal{L}_{\texttt{LPortalNeutral}}
+\mathcal{L}_{\texttt{LPortalCharged}}
+\mathcal{L}_{\texttt{LPortalCharged}}^{\dagger}
\;}
$$

No chiral projectors (`ProjP`/`ProjM`), no gamma matrices (`Ga`), no charge conjugation
(`CC`) and no fermion fields appear anywhere in the file: the new sector is purely
bosonic, so there is **no chirality structure to report**.

---

## 2. Field table

| Symbol | Class | Spin | $SU(3)_c$ | $SU(2)_L$ | $U(1)_Y$ / electric charge | Self-conjugate | Mass symbol | Mass value | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|---|
| $X_\mu$ | `V[101]`, `ClassName -> X` | 1 (vector) | **1** (singlet — no `Indices -> {Index[Colour]}`, no colour index) | **1** (singlet — no `SU2D`/`SU2W` index declared) | $Y=0$, $Q=0$ (no `QuantumNumbers` block; `SelfConjugate -> True` forces a neutral field) | **Yes** | `MX` | $1000$ GeV | `WX`, `Internal` (computed, see §3) | `5000023` |

Cosmetic declarations: `ParticleName -> "X"`, `PropagatorLabel -> "X"`,
`PropagatorType -> Sine` (wavy/vector line), `PropagatorArrow -> None` (consistent with a
self-conjugate field).

No other new class is declared; every other field ($A$, $Z$, $W^\pm$) is inherited from
the SM model file.

---

## 3. Parameters

### External

| Symbol | Type / block | Value | Interaction order | Multiplies | Physical meaning |
|---|---|---|---|---|---|
| $c_1$ | External, `NPCOUPLINGS` entry 1 | $1.0$ | `{NP,1}` | $\epsilon^{\mu\nu\lambda\rho} Z_\mu X_\nu \partial_\lambda(-s_W Z_\rho + c_W A_\rho)$, i.e. the $ZZX$ and $Z\gamma X$ vertices (equivalently $\epsilon\,Z X \partial B$) | Dimensionless neutral Chern-Simons portal coupling. The electroweak mixing angle splits one coupling into the two physical vertices: strength $c_1 s_W$ for $ZZX$ and $c_1 c_W$ for $Z\gamma X$. |
| $c_2$ | External, `NPCOUPLINGS` entry 2 | $1.0$ | `{NP,1}` | $\epsilon^{\mu\nu\lambda\rho} W^+_\mu X_\nu \partial_\lambda W^-_\rho + h.c.$ | Dimensionless charged Chern-Simons portal coupling ($XW^+W^-$ vertex). |

Both operators are dimension 4 (three vector fields $+$ one derivative), so $c_1$ and
$c_2$ are **dimensionless**; no new-physics scale $\Lambda$ appears.

Not new parameters, but used: $M_X$ (mass of $X$, declared inside the class, $1000$ GeV),
and the inherited SM quantities $M_Z$, $M_W$, $s_W$, $c_W$.

### Internal

| Symbol | Definition | Meaning |
|---|---|---|
| `WX` | $\displaystyle \Gamma_X=\frac{c_1^{2}s_W^{2}M_X^{3}}{192\pi M_Z^{2}}\Big(1-\frac{4M_Z^{2}}{M_X^{2}}\Big)^{5/2} \;+\;\frac{c_2^{2}M_X^{3}}{48\pi M_W^{2}}\Big(1-\frac{4M_W^{2}}{M_X^{2}}\Big)^{5/2} \;+\;\frac{c_1^{2}c_W^{2}M_X^{3}}{96\pi M_Z^{2}}\Big(1-\frac{M_Z^{2}}{M_X^{2}}\Big)^{3}\Big(1+\frac{M_Z^{2}}{M_X^{2}}\Big)$ | Total width of $X$, written as the sum of its three two-body partial widths. |

Channel-by-channel reading of `WX`:

1. **$X \to ZZ$** — carries $c_1^2 s_W^2$ (the $ZZX$ vertex) and the two-identical-massive-particle threshold factor $\beta^5=(1-4M_Z^2/M_X^2)^{5/2}$.
2. **$X \to W^+W^-$** — carries $c_2^2$ and $\beta^5=(1-4M_W^2/M_X^2)^{5/2}$.
3. **$X \to Z\gamma$** — carries $c_1^2 c_W^2$ (the $Z\gamma X$ vertex) and the one-massless-leg factor $(1-M_Z^2/M_X^2)^3(1+M_Z^2/M_X^2)$.

The $\beta^5$ threshold behaviour and the $1/M_{V}^{2}$ prefactors are the signature of a
derivative (dimension-4 $\epsilon$-tensor) coupling with longitudinally enhanced final
states. There is **no** $X\to f\bar f$ and **no** $X\to \gamma\gamma$ term, consistent
with the Lagrangian: $X$ has no fermion coupling, and no $\epsilon\,A X \partial A$
operator is written (it would vanish identically for two on-shell photons).

`M$InteractionOrderHierarchy` declares `{QCD,1}, {QED,2}, {NP,1}`, so both portal
couplings are counted as one power of the new-physics order `NP`.

---

## 4. Physics summary

This is a **Chern-Simons (anomaly-type) vector portal**: the SM is extended by a single
1 TeV, self-conjugate, gauge-singlet massive spin-1 field $X_\mu$ with a Proca kinetic
and mass term and **no** renormalisable couplings to matter. Its only contact with the SM
is through two parity-odd Levi-Civita trilinear operators,
$\epsilon^{\mu\nu\lambda\rho}Z_\mu X_\nu\partial_\lambda B_\rho$ (strength $c_1$, which
resolves into $ZZX$ with $c_1 s_W$ and $Z\gamma X$ with $c_1 c_W$) and
$\epsilon^{\mu\nu\lambda\rho}W^+_\mu X_\nu\partial_\lambda W^-_\rho + h.c.$
(strength $c_2$).

Phenomenologically $X$ is a purely bosonic resonance: it is produced in
vector-boson fusion and in associated production with an electroweak gauge boson, and it
decays only to electroweak diboson final states, $X\to ZZ$, $X\to W^+W^-$ and
$X\to Z\gamma$, with the branching ratios fixed by $c_1$, $c_2$ and $\theta_W$ through
the internal width `WX`. The same vertices also give an anomalous contribution to
triple-gauge-boson amplitudes with an off-shell $X$ exchanged, so the model is a target
for diboson resonance searches and for anomalous neutral/charged TGC measurements. There
is no direct quark or lepton coupling, hence no dilepton or dijet resonance signal at
tree level.

---

## 5. File-level notes (defects found while reading)

These do not change the physics content above, but a reader checking the file should
know about them.

1. **Unbalanced delimiters in `LPortalNeutral`.** The definition opens
   `LPortalNeutral := 2 (Block[{mu,nu,la,rho},` and then closes with `];` before a stray
   `)` on a later line. The `Block[...]` is closed and the statement terminated by `;`
   *inside* the parentheses, so the parenthesised group evaluates to `Null` and the
   definition does not give the intended expression. The intent is unambiguous
   (`2 * Block[...]`), and that is what §1.2 reports.

2. **The overall factor `2` in `LPortalNeutral` does not match the internal width `WX`.**
   `WX` is written with plain $c_1^2 s_W^2$ and $c_1^2 c_W^2$ numerators. Rescaling the
   neutral portal by 2 rescales the $ZZX$ and $Z\gamma X$ amplitudes by 2 and the
   corresponding partial widths by 4, so with the factor `2` present the stated `WX` is
   too small by a factor 4 in its first and third terms, while the $c_2^2$ ($W^+W^-$)
   term stays consistent. The relative normalisation of the three `WX` terms is
   self-consistent only if the neutral portal carries **no** extra factor of 2. This
   points to the leading `2 (` as a spurious insertion rather than part of the intended
   model.
