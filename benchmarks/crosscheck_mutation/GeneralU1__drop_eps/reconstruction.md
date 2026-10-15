# Reconstruction of `sanitized.fr`

The file adds to the Standard Model (`LSM` is added in `LTotal`) one extra abelian
gauge boson, one extra real scalar, and three Majorana singlet fermions. The
charge assignment is a general linear combination of hypercharge and \(B-L\).

Throughout: \(P_R=\tfrac{1+\gamma^5}{2}\) (FeynRules `ProjP`),
\(P_L=\tfrac{1-\gamma^5}{2}\) (`ProjM`), \(i,j\) are generation indices,
\(a,b\) are `SU2D` doublet indices, \(\Phi\) is the SM Higgs doublet
(`Phi`, `Phibar`\(=\Phi^\dagger\)), \(v\) is `vev`.

---

## 0. Gauge group and covariant derivative

The gauge group is

$$
SU(3)_C \times SU(2)_L \times U(1)_Y \times U(1)_X .
$$

The internal parameters fix the \(U(1)_X\) charge of every field to

$$
x_f \;=\; x_H\,Y_f \;+\; x_\Phi\,(B-L)_f ,
$$

as one reads off `xqL`…`xSc`:

| field | `.fr` symbol | value | \(Y\) | \(B-L\) | numeric (\(x_H=2,\;x_\Phi=1\)) |
|---|---|---|---|---|---|
| \(q_L\) | `xqL` | \(x_H/6+x_\Phi/3\) | \(1/6\) | \(1/3\) | \(2/3\) |
| \(u_R\) | `xuR` | \(2x_H/3+x_\Phi/3\) | \(2/3\) | \(1/3\) | \(5/3\) |
| \(d_R\) | `xdR` | \(-x_H/3+x_\Phi/3\) | \(-1/3\) | \(1/3\) | \(-1/3\) |
| \(\ell_L\) | `xlL` | \(-x_H/2-x_\Phi\) | \(-1/2\) | \(-1\) | \(-2\) |
| \(e_R\) | `xeR` | \(-x_H-x_\Phi\) | \(-1\) | \(-1\) | \(-3\) |
| \(N_R\) | `xnR` | \(-x_\Phi\) | \(0\) | \(-1\) | \(-1\) |
| \(\Phi\) (SM Higgs) | `xHd` | \(x_H/2\) | \(1/2\) | \(0\) | \(1\) |
| \(\Phi_X\) (breaks \(U(1)_X\)) | `xSc` | \(2x_\Phi\) | \(0\) | \(2\) | \(2\) |

\(x_H=0\) is pure \(B-L\); \(x_\Phi=0\) is pure hypercharge ("\(U(1)_R\)-like");
the charge set is anomaly free for any \(x_H,x_\Phi\) once the three
right-handed neutrinos are present.

The covariant derivative acting on a field \(f\) is

$$
D_\mu f=\Big(\partial_\mu
 - i g_s T^A G^A_\mu
 - i g\,T^I W^I_\mu
 - i g' Y_f B_\mu
 + i g_X\,x_f\,Z'_\mu \Big) f .
$$

The sign of the last piece is fixed by `LZpF`, which is written with an overall
\(-g_X\); it is a convention (\(Z'\to-Z'\)) and carries no physics.

**Two structural remarks, stated because a term-by-term check will hit them.**

* There is **no kinetic-mixing term** \(-\tfrac{\epsilon}{2}\,\hat B_{\mu\nu}\hat Z'^{\mu\nu}\)
  in the file, and no \(B\)–\(Z'\) rotation. \(Z'\) is the pure \(U(1)_X\) gauge
  eigenstate. The doublet charge \(x_{H_d}\) nevertheless enters \(M_{Z'}\)
  (see below), so the \(Z\)–\(Z'\) mass mixing that goes with it is also not
  written out: the model is used in the limit of vanishing \(Z\)–\(Z'\) mixing.
* The scalar potential contains no \(H\)–`HX` mixing term (see §1.9), so the two
  CP-even scalars are mass eigenstates at tree level.

---

## 1. Lagrangian, term by term

\(\mathcal{L}_{\rm total}\) (`LTotal`):

$$
\mathcal{L}=\mathcal{L}_{\rm SM}
+\mathcal{L}_{Z'{\rm kin}}+\mathcal{L}_{Z'F}+\mathcal{L}_{N{\rm kin}}
+\mathcal{L}_{H_X{\rm kin}}+\mathcal{L}_{Z'H_X}+\mathcal{L}_{N{\rm Yuk}}
+\mathcal{L}_{\nu{\rm Yuk}}+\mathcal{L}_{V_X} .
$$

### 1.1 `LZpKin` — gauge kinetic and mass term

With `FS[Zp,mu,nu]` \(=Z'_{\mu\nu}=\partial_\mu Z'_\nu-\partial_\nu Z'_\mu\)
(abelian, no self-coupling):

$$
\mathcal{L}_{Z'{\rm kin}}
=-\frac14 Z'_{\mu\nu}Z'^{\mu\nu}
+\frac12 M_{Z'}^2\,Z'_\mu Z'^\mu .
$$

The mass is inserted by hand (Proca form) with the value the Higgs mechanism
would give; the \(|D_\mu\Phi_X|^2\) kinetic term itself is not written, only its
\(H_X\)-dependent remainder (§1.6).

### 1.2 `LZpF` — neutral current of the \(Z'\)

$$
\mathcal{L}_{Z'F}=-g_X Z'_\mu\Big[
 x_{q_L}\,\bar q\,\gamma^\mu P_L\,q
+x_{u_R}\,\bar u\,\gamma^\mu P_R\,u
+x_{d_R}\,\bar d\,\gamma^\mu P_R\,d
+x_{\ell_L}\,\bar \ell\,\gamma^\mu P_L\,\ell
+x_{e_R}\,\bar e\,\gamma^\mu P_R\,e
+x_{N_R}\,\bar N\,\gamma^\mu P_R\,N \Big],
$$

summed over the three generations (flavour diagonal and universal) and, for
`QL`/`LL`, over the two members of each \(SU(2)_L\) doublet
(`FlavorExpand -> {SU2D}`). `QLbar.Ga[mu].QL` etc. carry the left chirality of
the SM doublets, hence \(P_L\); `uRbar`, `dRbar`, `lRbar` carry \(P_R\).

The replacement rules
`CKM[a,b] Conjugate[CKM[a,c]] -> IndexDelta[b,c]` (and its transpose) only apply
CKM unitarity after the doublet expansion: the \(Z'\) coupling stays flavour
diagonal, with **no** flavour-changing neutral current.

Since `NX` is Majorana, the last line is equivalently an axial current:

$$
x_{N_R}\,\bar N_i\gamma^\mu P_R N_i
=\frac{x_{N_R}}{2}\,\bar N_i\gamma^\mu\gamma^5 N_i ,
\qquad x_{N_R}=-x_\Phi ,
$$

because \(\bar N\gamma^\mu N\equiv 0\) for a self-conjugate field.
Here \(N_R \equiv P_R N_X\) is the unphysical field `NR` of `F[110]`.

### 1.3 `LNXKin` — Majorana kinetic and mass term

$$
\mathcal{L}_{N{\rm kin}}
=\frac{i}{2}\,\bar N_i\gamma^\mu\partial_\mu N_i
-\frac12\,\bar N_i\,(m_N)_{ij}\,N_j ,
\qquad
(m_N)_{ij}={\rm diag}(M_{N_1},M_{N_2},M_{N_3}) .
$$

The factors \(1/2\) are the Majorana normalisation. The mass term violates
lepton number by two units (`NR` is declared with `LeptonNumber -> 1`).

### 1.4 `LHXKin` — real scalar kinetic and mass term

$$
\mathcal{L}_{H_X{\rm kin}}
=\frac12\,\partial_\mu H_X\,\partial^\mu H_X-\frac12 M_{H_X}^2 H_X^2 .
$$

### 1.5 — (no separate term)

### 1.6 `LZpHX` — \(Z'Z'H_X\) and \(Z'Z'H_XH_X\)

This is the remainder of \(|D_\mu\Phi_X|^2\) with
\(\Phi_X=(v_X+H_X)/\sqrt2\):

$$
\mathcal{L}_{Z'H_X}
=g_X^2\,x_{S}^2\Big(v_X H_X+\frac12 H_X^2\Big) Z'_\mu Z'^\mu ,
\qquad x_S\equiv x_{\Phi_X}=2x_\Phi .
$$

The field-independent piece of the same expansion is the
\(\tfrac12 g_X^2x_S^2v_X^2 Z'^2\) mass term already put in `LZpKin`.

### 1.7 `LNYuk` — Majorana Yukawa coupling to \(H_X\)

$$
\mathcal{L}_{N{\rm Yuk}}
=-\frac{1}{2\sqrt2}\,H_X\,\bar N_i\,(y_N)_{ij}\,N_j
=-\frac12\,\frac{M_{N_i}}{v_X}\,H_X\,\bar N_i N_i ,
$$

using \((y_N)_{ii}=\sqrt2 M_{N_i}/v_X\). This is the \(H_X\) part of
\(-\tfrac{1}{2\sqrt2}(y_N)_{ij}\,(v_X+H_X)\,\bar N_iN_j\); the \(v_X\) part
reproduces exactly the \(m_N\) of §1.3, so the singlet vev is the origin of the
heavy neutrino masses.

### 1.8 `LNuYuk` — Dirac Yukawa of the singlet fermions

Written literally, with the \(SU(2)_L\) index \(a\) of \(\bar L_L\) contracted
**directly** with the index of \(\Phi^\dagger\) (`LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[ii]`):

$$
\mathcal{L}_{\nu{\rm Yuk}}
=-\,(y_\nu)_{ij}\;\bar L_L^{\,a,i}\,P_R\,N^{j}\;(\Phi^\dagger)_a
\;+\;{\rm h.c.}
$$

(`NR` = \(P_R N_X\), so the vertex is \(\bar L_L\,P_R N\); `HC` supplies
\(-(y_\nu)^*_{ij}\,\bar N^{j}P_L L_L^{a,i}\,\Phi_a\). The Goldstones
\(G^0,G^\pm\) are dropped unless `FeynmanGauge` is true.)

**This contraction is not \(SU(2)_L\) invariant.** \(\bar L_L^{\,a}\) and
\((\Phi^\dagger)_a\) both transform in the \(\bar{\mathbf 2}\); the invariant
combination requires the antisymmetric tensor,
\(\epsilon_{ab}\bar L_L^{\,a}N_R\,(\Phi^\dagger)_b\), i.e. the conjugate doublet
\(\tilde\Phi=i\sigma^2\Phi^*\). The \(U(1)_X\) charges do balance
(\(-x_{\ell_L}+x_{N_R}-x_{H_d}=0\)), so only the \(SU(2)_L\) structure is wrong.
The consequence is physical, not cosmetic: in unitary gauge
\((\Phi^\dagger)_a\to(0,(v+h)/\sqrt2)\), so the term becomes

$$
-\frac{(y_\nu)_{ij}}{\sqrt2}\,(v+h)\;\bar e_L^{\,i}P_R N^{j}+{\rm h.c.},
$$

a Dirac mass and a Higgs coupling between the **charged leptons** and \(N\),
and **no** neutrino Dirac mass at all — the seesaw is destroyed. The intended
term is almost certainly

$$
\mathcal{L}_{\nu{\rm Yuk}}
=-\,(y_\nu)_{ij}\,\epsilon_{ab}\,\bar L_L^{\,a,i}P_RN^{j}(\Phi^\dagger)_b+{\rm h.c.}
\;\longrightarrow\;
-\frac{(y_\nu)_{ij}}{\sqrt2}(v+h)\,\bar\nu_L^{\,i}P_RN^{j}+{\rm h.c.},
$$

which with \(y_\nu=10^{-6}\) and \(M_N=8\) TeV gives
\(m_D=y_\nu v/\sqrt2\simeq1.7\times10^{-4}\) GeV and a type-I seesaw mass
\(m_\nu\simeq m_D^2/M_N\simeq4\times10^{-3}\) eV — the right scale, which
confirms the intent. I report the file as written and flag the missing
\(\epsilon_{ab}\).

### 1.9 `LPotX` — scalar potential

$$
\mathcal{L}_{V_X}
=-\lambda_\Phi v_X H_X^3-\frac{\lambda_\Phi}{4}H_X^4
-\frac{\lambda'}{2}\,H_X^2\,(\Phi^\dagger)_a\Phi^a .
$$

These are exactly the terms of
\(V=\lambda_\Phi\big(|\Phi_X|^2-\tfrac{v_X^2}{2}\big)^2+\lambda'|\Phi|^2|\Phi_X|^2\)
that survive after \(\Phi_X\to(v_X+H_X)/\sqrt2\), **minus** the linear-in-\(H_X\)
portal \(\lambda' v_X H_X|\Phi|^2\). Dropping that piece is what removes tree-level
\(h\)–\(H_X\) mixing; the quadratic piece \(\lambda_\Phi v_X^2H_X^2\) is already in
`LHXKin` through \(M_{H_X}^2=2\lambda_\Phi v_X^2\).

---

## 2. Field table

| symbol | class | spin | \(SU(3)_C\) | \(SU(2)_L\) | \(U(1)_Y\) | \(U(1)_X\) | self-conj. | mass symbol | value |
|---|---|---|---|---|---|---|---|---|---|
| \(Z'\) | `V[100]`, `Zp` | 1 | **1** | **1** | 0 | 0 (gauge field) | yes | `MZp` (internal) | \(g_X\sqrt{x_S^2v_X^2+x_{H_d}^2v^2}\approx7.50\) TeV |
| \(H_X\) | `S[100]`, `HX` | 0 | **1** | **1** | 0 | 0 (radial mode of \(\Phi_X\)) | yes | `MHX` (internal) | \(\sqrt{2\lambda_\Phi v_X^2}\approx4.19\) TeV |
| \(N_{1,2,3}\) | `F[100]`, `NX` | 1/2 (Majorana) | **1** | **1** | 0 | \(-x_\Phi=-1\) | yes | `MNX1,2,3` | 8000 GeV each |
| \(N_R\) | `F[110]`, `NR` | 1/2 | **1** | **1** | 0 | \(-x_\Phi\) | no (unphysical) | — | \(N_R=P_RN_X\) |

Extra data:

* \(Z'\): PDG 9900032, `WZp = 1353.` GeV, propagator `Sine`.
* \(H_X\): PDG 9900025, `WHX = 0.1` GeV, propagator `D`.
* \(N_i\): PDG 9900012 / 9900014 / 9900016, `WNXi = 1e-10` GeV, three flavours
  under `Index[Generation]`, names `nx1,nx2,nx3` ("RHN1…3").
* `NR` carries `Y -> 0` and `LeptonNumber -> 1` and exists only to write the
  chiral projection of the Majorana field in `LZpF` and `LNuYuk`.
* The \(U(1)_X\) charges are not declared as `QuantumNumbers`; they enter only
  through the explicit \(x_f\) factors in `LZpF`.
* `M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}}` — new-physics
  couplings are counted in a separate `NP` order.

---

## 3. Parameters

### External

| symbol | block / position | value | multiplies | meaning |
|---|---|---|---|---|
| `gX` | `U1XINPUTS` 1 | 0.4 | \(Z'_\mu J_X^\mu\) in `LZpF`, \(Z'Z'H_X\) in `LZpHX`, \(M_{Z'}\) | \(U(1)_X\) gauge coupling, `NP` order 1 |
| `xH` | `U1XINPUTS` 2 | 2.0 | all \(x_f\) via \(x_H Y_f\) | hypercharge admixture in the \(U(1)_X\) charge (dimensionless) |
| `xPhi` | `U1XINPUTS` 3 | 1.0 | all \(x_f\) via \(x_\Phi (B-L)_f\) | \(B-L\) admixture; also fixes the singlet charge \(x_S=2x_\Phi\) |
| `vX` | `U1XINPUTS` 4 | 9375 GeV | \(M_{Z'}\), \(M_{H_X}\), \(H_X^3\), \(Z'Z'H_X\), \(y_N\) | vev of the \(U(1)_X\)-breaking singlet \(\Phi_X\); `NP` order \(-1\) |
| `lamX` | `U1XINPUTS` 5 | 0.1 | \(H_X^3,\,H_X^4\), and \(M_{H_X}\) | singlet quartic coupling \(\lambda_\Phi\), `NP` order 2 |
| `lamHX` | `U1XINPUTS` 6 | 0.01 | \(H_X^2\Phi^\dagger\Phi\) | Higgs-portal quartic \(\lambda'\), `NP` order 2 |
| `ynu` | `YUKNU`, \(3\times3\) | \(10^{-6}\,\delta_{ij}\) | \(\bar L_L P_R N\,\Phi^\dagger\) in `LNuYuk` | Dirac Yukawa matrix \(Y_\nu\) (diagonal, degenerate), `NP` order 1 |

\(M_{N_1},M_{N_2},M_{N_3}\) (`MNX1..3`, 8000 GeV) are external through the
particle-mass declaration of `F[100]`.

### Internal

| symbol | expression | meaning |
|---|---|---|
| `xqL,xuR,xdR,xlL,xeR,xnR,xHd,xSc` | \(x_H Y+x_\Phi(B-L)\) (table in §0) | \(U(1)_X\) charges |
| `MZp` | \(g_X\sqrt{x_S^2v_X^2+x_{H_d}^2v^2}\) | \(Z'\) mass; the \(v^2\) piece is the SM-doublet contribution |
| `MHX` | \(\sqrt{2\lambda_\Phi v_X^2}\) | mass of the singlet scalar |
| `mNmaj` | \({\rm diag}(M_{N_1},M_{N_2},M_{N_3})\) | Majorana mass matrix |
| `yN` | \({\rm diag}(\sqrt2 M_{N_i}/v_X)\) | Majorana Yukawa; ties \(H_X\bar NN\) to \(M_N\) and \(v_X\) |

With the default inputs: \(x_{S}=2\), \(x_{H_d}=1\),
\(M_{Z'}\simeq7.50\) TeV, \(M_{H_X}\simeq4.19\) TeV, \(M_{N_i}=8\) TeV,
\((y_N)_{ii}\simeq1.21\).

---

## 4. Physics summary

This is a general \(U(1)_X\) extension of the SM, with the charge of every
field a free linear combination \(x_H Y+x_\Phi(B-L)\); it therefore interpolates
between \(B-L\) (\(x_H=0\)) and hypercharge-like (\(x_\Phi=0\)) \(Z'\) models.
The new states are a heavy neutral gauge boson \(Z'\) (\(\sim7.5\) TeV), a real
singlet scalar \(H_X\) (\(\sim4.2\) TeV) that is the radial mode of the
\(U(1)_X\)-breaking scalar \(\Phi_X\) with \(v_X=9.4\) TeV, and three Majorana
singlet ("right-handed") neutrinos of 8 TeV whose masses come from
\(\langle\Phi_X\rangle\) and so break lepton number by two units.

The model mediates Drell-Yan \(Z'\) production with decays to all SM fermion
pairs (flavour diagonal, chirality dependent through \(x_{q_L}\dots x_{e_R}\))
and to \(NN\) pairs, plus \(Z'\to Z'H_X\)-type and \(H_X\to Z'Z'\) vertices
from `LZpHX`, \(H_X\to NN\) from `LNYuk`, and an \(H_X^2|\Phi|^2\) Higgs portal.
Pair-produced Majorana \(N\) decaying through the small \(y_\nu\) coupling gives
the characteristic long-lived, lepton-number-violating same-sign-dilepton
signature; \(y_\nu\sim10^{-6}\) with \(M_N=8\) TeV is chosen to reproduce
light-neutrino masses of a few meV by the type-I seesaw.

**Caveat on the reconstruction.** As written, the `LNuYuk` term contracts the
\(SU(2)_L\) index of \(\bar L_L\) with that of \(\Phi^\dagger\) without the
\(\epsilon_{ab}\) tensor. It is therefore not \(SU(2)_L\) invariant, and it
couples \(N\) to the charged leptons rather than to the neutrinos, so in this
file the seesaw and the neutrino-mass generation described above do not
actually follow from the Lagrangian. Everything else in the file is mutually
consistent.
