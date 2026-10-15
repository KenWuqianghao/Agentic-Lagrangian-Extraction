# Reconstruction of `sanitized.fr`

## 0. Conventions and setup read off the file

**Colour sextet representation.** The file calls

```
AddGaugeRepresentation[SU3C -> {T6, Sextet}];
IndexRange[Index[Sextet]] = NoUnfold[Range[6]];
```

so a new 6-dimensional index type `Sextet` is registered as a representation of
$SU(3)_C$, with generators $T^a_6$ (the $6\times 6$ sextet generators,
$\mathrm{Tr}(T^a_6T^b_6)=\tfrac{5}{2}\delta^{ab}$ in the usual normalisation).
All four new fields carry exactly one `Sextet` index.

**Covariant derivative.** `DC[...,mu]` is the Standard-Model covariant derivative
of FeynRules. None of the new fields declares an `SU2W` index, so all of them are
weak singlets and only $SU(3)_C$ and $U(1)_Y$ act:

$$
D_\mu \;=\; \partial_\mu \;-\; i\,g_s\,G^a_\mu\,T^a_{(R)} \;-\; i\,g_1\,Y\,B_\mu ,
\qquad
T^a_{(R)} \;=\; T^a_6 \ \ \text{for every new field},
$$

with $Y$ the declared hypercharge of the field. Because $T^3=0$ for a weak
singlet, $Q=T^3+Y=Y$, which is exactly what the `QuantumNumbers` entries show
($Q=Y$ for all four states). For the Standard-Model quark and lepton fields that
appear in the interactions ($u_R$, $d_R$, $l_R$) the derivative is the ordinary
SM one with $T^a_{(3)}=T^a$ (fundamental) or nothing (lepton singlet).

**Lorentz structure.** The file writes the tensor bilinear out by hand:

$$
\tfrac{i}{2}\big(\gamma^\mu\gamma^\nu-\gamma^\nu\gamma^\mu\big)
\;=\;\tfrac{i}{2}\,[\gamma^\mu,\gamma^\nu]\;\equiv\;\sigma^{\mu\nu}.
$$

`FS[G,mu,nu,aa]` $=G^a_{\mu\nu}$ (gluon field strength) and `FS[B,mu,nu]`
$=B_{\mu\nu}$ (hypercharge field strength).

**Charge conjugation.** `CC[uR][tt,mm,ii]` $=(u_R)^c = C\,\overline{u_R}^{\,T}$,
a *left-handed* field, $P_L (u_R)^c=(u_R)^c$. Since $\sigma^{\mu\nu}P_L=P_L\sigma^{\mu\nu}$,
every bilinear below satisfies

$$
\overline{\psi}\,\Gamma\,(q_R)^c \;=\; \overline{(P_R\psi)}\,\Gamma\,(q_R)^c ,
\qquad \Gamma\in\{1,\sigma^{\mu\nu}\},
$$

i.e. **only the right-handed component of the new sextet fermion** (and only the
right-handed charged lepton $l_R$, through $\overline{l_R}=\bar l\,P_L$) takes
part. The quark is always the $SU(2)$-singlet right-handed field, charge
conjugated.

**Colour tensor.** $6\otimes 3 = 8\oplus 10$ contains no singlet, so a sextet
field cannot couple to a single quark at the renormalisable level. The unique
invariant needs one adjoint index, and that is precisely the contraction used
everywhere in this file. Write it once as

$$
\boxed{\;
\mathcal{K}^{a}{}_{k\,i}\;\equiv\;\sqrt{2}\;
(K_6)_{k}{}^{yz}\,(T^a)_{z}{}^{x}\,(\bar K_3)_{i\,xy}\;}
$$

where $(K_6)_{k}{}^{yz}$ is the $6\to 3\otimes 3$ Clebsch–Gordan tensor
(symmetric in $y,z$) and $(\bar K_3)_{i\,xy}\propto \varepsilon_{ixy}$ is the
antitriplet tensor; $k$ is the sextet index, $a$ the adjoint index and $i$ the
quark colour index. Its conjugate, written in the file as
`K3[ii,xx,yy] T[aa,xx,zz] K6bar[kk,zz,yy]`, is

$$
\big(\mathcal{K}^{a}{}_{k\,i}\big)^{*}\;=\;\sqrt{2}\;
(K_3)_{i}{}^{xy}\,(T^a)_{x}{}^{z}\,(\bar K_6)^{k}{}_{zy}.
$$

`K6`, `K6bar`, `K3`, `K3bar`, `T` and `T6` are not defined in the file; they come
from the FeynRules colour module.

**Coupling-order counting.** `M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,2}}`
and every new parameter carries `InteractionOrder -> {QCD,1}`, so each new vertex
counts as one power of the strong coupling.

---

## 1. Lagrangian

### 1.1 `LSextetKin` — kinetic and mass terms

$$
\mathcal{L}_{\rm kin}
=\overline{F_u}^{\,k}\big(i\gamma^\mu D_\mu-M_{F_u}\big)F_{u\,k}
+\overline{F_d}^{\,k}\big(i\gamma^\mu D_\mu-M_{F_d}\big)F_{d\,k}
+\big(D_\mu S_u\big)^{\dagger k}\big(D^\mu S_u\big)_k-M_{S_u}^2\,S_u^{\dagger k}S_{u\,k}
+\big(D_\mu S_d\big)^{\dagger k}\big(D^\mu S_d\big)_k-M_{S_d}^2\,S_d^{\dagger k}S_{d\,k}
$$

Here $F_u\equiv$ `sFu`, $F_d\equiv$ `sFd`, $S_u\equiv$ `sSu`, $S_d\equiv$ `sSd`,
and $k$ is the sextet colour index, which is carried through undisturbed (the
gauge interaction sits entirely inside $D_\mu$ with $T^a_6$). Two Dirac kinetic
terms plus two complex-scalar kinetic terms, each with an explicit mass.

### 1.2 `LFu` — chromomagnetic dipole of the up-type sextet fermion

$$
\mathcal{L}_{F_u}^{(\sigma)}
= i\,C_{u}^{\,m}\;\mathcal{K}^{a}{}_{k\,i}\;
\overline{F_u}^{\,k}\,\sigma^{\mu\nu}\,\big(u_R^{\,c}\big)_{m}^{\;i}\;G^a_{\mu\nu}
\;+\;\text{h.c.}
$$

(`CFu[mm]` $=C_u^{\,m}$, $m$ = quark generation; the explicit $\sqrt{2}$ of the
file is absorbed in $\mathcal{K}$; the conjugate piece in the file carries the
factor $-i\sqrt{2}\,C_u^{*}$, which is exactly the hermitian conjugate.)
Chirality: $\overline{F_u}\sigma^{\mu\nu}(u_R)^c=\overline{(P_RF_u)}\,\sigma^{\mu\nu}(u_R)^c$.

$$
\mathcal{L}_{F_u}^{(B)}
= i\,C_{Bu}^{\,m}\;\mathcal{K}^{a}{}_{k\,i}\;
\overline{F_u}^{\,k}\,\big(u_R^{\,c}\big)_{m}^{\;i}\;G^a_{\mu\nu}B^{\mu\nu}
\;+\;\text{h.c.}
$$

(`CFBu[mm]` $=C_{Bu}^{\,m}$; scalar bilinear, no $\sigma^{\mu\nu}$, multiplied by
the product $G^a_{\mu\nu}B^{\mu\nu}$ — a dimension-7 operator.)

### 1.3 `LFd` — chromomagnetic dipole of the down-type sextet fermion

$$
\mathcal{L}_{F_d}^{(\sigma)}
= i\,C_{d}^{\,m}\;\mathcal{K}^{a}{}_{k\,i}\;
\overline{F_d}^{\,k}\,\sigma^{\mu\nu}\,\big(d_R^{\,c}\big)_{m}^{\;i}\;G^a_{\mu\nu}
\;+\;\text{h.c.}
$$

$$
\mathcal{L}_{F_d}^{(B)}
= i\,C_{Bd}^{\,m}\;\mathcal{K}^{a}{}_{k\,i}\;
\overline{F_d}^{\,k}\,\big(d_R^{\,c}\big)_{m}^{\;i}\;G^a_{\mu\nu}B^{\mu\nu}
\;+\;\text{h.c.}
$$

(`CFd[mm]`, `CFBd[mm]`; identical in structure to `LFu` with $u_R\to d_R$,
$F_u\to F_d$.)

### 1.4 `LSu` — sextet scalar, lepton, up-quark, gluon

$$
\mathcal{L}_{S_u}
= i\,C_{S_u}^{\,m\ell}\;\mathcal{K}^{a}{}_{k\,i}\;
S_u^{\dagger\,k}\;
\overline{l_{R\,\ell}}\,\sigma^{\mu\nu}\,\big(u_R^{\,c}\big)_{m}^{\;i}\;
G^a_{\mu\nu}\;+\;\text{h.c.}
$$

(`CSu[mm,ll]`: $m$ = quark generation, $\ell$ = lepton generation. The bilinear is
$\overline{l_R}\,\sigma^{\mu\nu}(u_R)^c$, i.e. both fermions are $SU(2)$
singlets; in the file the whole product, including `FS[G,mu,nu,aa]`, sits inside
`HC[...]` for the conjugate half, which is equivalent because $G^a_{\mu\nu}$ is
hermitian.)

### 1.5 `LSd` — sextet scalar, lepton, down-quark, gluon

$$
\mathcal{L}_{S_d}
= i\,C_{S_d}^{\,m\ell}\;\mathcal{K}^{a}{}_{k\,i}\;
S_d^{\dagger\,k}\;
\overline{l_{R\,\ell}}\,\sigma^{\mu\nu}\,\big(d_R^{\,c}\big)_{m}^{\;i}\;
G^a_{\mu\nu}\;+\;\text{h.c.}
$$

### 1.6 `LSextet` — total

$$
\mathcal{L}_{\rm Sextet}
=\mathcal{L}_{\rm kin}
+\mathcal{L}_{F_u}^{(\sigma)}+\mathcal{L}_{F_u}^{(B)}
+\mathcal{L}_{F_d}^{(\sigma)}+\mathcal{L}_{F_d}^{(B)}
+\mathcal{L}_{S_u}+\mathcal{L}_{S_d}.
$$

### 1.7 Charge and number bookkeeping (checks)

| Term | $Q$ balance | Colour |
| --- | --- | --- |
| $\overline{F_u}(u_R)^c G$ | $(+2/3)+(-2/3)+0=0$ | $\bar 6\otimes\bar 3\otimes 8\supset 1$ |
| $\overline{F_d}(d_R)^c G$ | $(-1/3)+(+1/3)+0=0$ | same |
| $S_u^\dagger\,\overline{l_R}(u_R)^c G$ | $(-1/3)+(+1)+(-2/3)=0$ | same |
| $S_d^\dagger\,\overline{l_R}(d_R)^c G$ | $(-4/3)+(+1)+(+1/3)=0$ | same |

Lepton number is conserved by the scalar terms with the declared $L(S_u)=L(S_d)=-1$:
$S^\dagger$ carries $L=+1$ and $\overline{l_R}$ carries $L=-1$. Baryon number
forces $B(S_u)=B(S_d)=-1/3$, so both scalars are leptoquark-like.

---

## 2. Field table

| `.fr` symbol | Class | Spin | $SU(3)_C$ | $SU(2)_L$ | $Y$ ( $=Q$ ) | Self-conj. | Mass | Width | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `sFu` | `F[100]` | 1/2 (Dirac) | **6** (sextet, `T6`) | singlet (no `SU2W` index) | $-2/3$ | no | `MFu` = 500. GeV | `WFu` = 4.7740 | 9000001 |
| `sFd` | `F[101]` | 1/2 (Dirac) | **6** | singlet | $+1/3$ | no | `MFd` = 500. GeV | `WFd` = 4.7740 | 9000002 |
| `sSu` | `S[102]` | 0 (complex) | **6** | singlet | $+1/3$ | no | `MSu` = 500. GeV | `WSu` = 4.4108 | 9000003 |
| `sSd` | `S[103]` | 0 (complex) | **6** | singlet | $+4/3$ | no | `MSd` = 500. GeV | `WSd` = 4.0647 | 9000004 |

Extra quantum numbers: `sSu` and `sSd` both declare `LeptonNumber -> -1`.
`sFu` and `sFd` declare no lepton number. No generation index is given to any of
the four states, so each is a single colour-sextet multiplet. Propagator styles
confirm the spins (`Straight`/`Forward` for the fermions, `ScalarDash`/`None` for
the scalars).

---

## 3. Parameters

All twelve external parameters are **real** (`ComplexParameter -> False`), indexed
by generation, and carry `InteractionOrder -> {QCD, 1}`. They are paired into six
complex internal couplings $C = C^R + i\,C^I$.

### External

| Symbol | Indices | Default | LHA block | Role |
| --- | --- | --- | --- | --- |
| `CFBuR` | 1 generation | 0.1 | `SFBUR` | Re part of $C_{Bu}$ |
| `CFBuI` | 1 generation | 0 | `SFBUI` | Im part of $C_{Bu}$ |
| `CFBdR` | 1 generation | 0.1 | `SFBDR` | Re part of $C_{Bd}$ |
| `CFBdI` | 1 generation | 0 | `SFBDI` | Im part of $C_{Bd}$ |
| `CFuR` | 1 generation | 0.1 | `SFUPR` | Re part of $C_u$ |
| `CFuI` | 1 generation | 0 | `SFUPI` | Im part of $C_u$ |
| `CFdR` | 1 generation | 0.1 | `SFDOWNR` | Re part of $C_d$ |
| `CFdI` | 1 generation | 0 | `SFDOWNI` | Im part of $C_d$ |
| `CSuR` | 2 generations | 0.1 | `SSUPR` | Re part of $C_{S_u}$ |
| `CSuI` | 2 generations | 0 | `SSUPI` | Im part of $C_{S_u}$ |
| `CSdR` | 2 generations | 0.1 | `SSDOWNR` | Re part of $C_{S_d}$ |
| `CSdI` | 2 generations | 0 | `SSDOWNI` | Im part of $C_{S_d}$ |

### Internal (complex)

| Symbol | Definition | Multiplies | Physical meaning |
| --- | --- | --- | --- |
| `CFu[m]` | $C^R_{u,m}+i\,C^I_{u,m}$ | $\overline{F_u}\sigma^{\mu\nu}(u_R)^c_m G^a_{\mu\nu}$ | chromomagnetic (colour-dipole) coupling of the sextet fermion to the right-handed up-type quark of generation $m$; mass dimension $-1$ (a $1/\Lambda$ Wilson coefficient) |
| `CFd[m]` | $C^R_{d,m}+i\,C^I_{d,m}$ | $\overline{F_d}\sigma^{\mu\nu}(d_R)^c_m G^a_{\mu\nu}$ | same, down-type sector |
| `CFBu[m]` | $C^R_{Bu,m}+i\,C^I_{Bu,m}$ | $\overline{F_u}(u_R)^c_m G^a_{\mu\nu}B^{\mu\nu}$ | scalar-bilinear coupling with two field strengths (gluon $\times$ hypercharge); dimension-7 operator, coefficient of mass dimension $-3$ |
| `CFBd[m]` | $C^R_{Bd,m}+i\,C^I_{Bd,m}$ | $\overline{F_d}(d_R)^c_m G^a_{\mu\nu}B^{\mu\nu}$ | same, down-type sector |
| `CSu[m,\ell]` | $C^R_{S_u,m\ell}+i\,C^I_{S_u,m\ell}$ | $S_u^\dagger\,\overline{l_{R\ell}}\sigma^{\mu\nu}(u_R)^c_m G^a_{\mu\nu}$ | lepton–quark–gluon dipole coupling of the sextet scalar; first index = quark generation, second = lepton generation; dimension-6 operator, coefficient of dimension $-2$ |
| `CSd[m,\ell]` | $C^R_{S_d,m\ell}+i\,C^I_{S_d,m\ell}$ | $S_d^\dagger\,\overline{l_{R\ell}}\sigma^{\mu\nu}(d_R)^c_m G^a_{\mu\nu}$ | same, down-type sector |

The couplings are entered as plain numbers (0.1), so the suppression scale is
implicit: FeynRules does not enforce mass dimensions on external parameters.

No new masses or widths are declared in `M$Parameters`; `MFu`, `MFd`, `MSu`,
`MSd`, `WFu`, `WFd`, `WSu`, `WSd` are created by the `M$ClassesDescription`
entries, all at 500 GeV.

---

## 4. Physics summary

This is a colour-**sextet** extension of the Standard Model: two Dirac fermions
($F_u$ with $Q=-2/3$, $F_d$ with $Q=+1/3$) and two complex scalars ($S_u$ with
$Q=+1/3$, $S_d$ with $Q=+4/3$, both with lepton number $-1$), all weak singlets
in the **6** of $SU(3)_C$ and all degenerate at 500 GeV. Because $6\otimes 3$
holds no colour singlet, none of them can have a renormalisable coupling to one
quark; every interaction is therefore an effective operator that carries one
gluon field strength, with the unique $6\otimes 3\otimes 8$ colour tensor
$K_6\,T^a\,\bar K_3$. The fermions couple through a chromomagnetic dipole
$\overline{F}\,\sigma^{\mu\nu}q_R^{\,c}\,G^a_{\mu\nu}$ (plus a higher-dimension
version with an extra $B_{\mu\nu}$), and the scalars couple through a
lepton–quark dipole $S^\dagger\,\overline{l_R}\,\sigma^{\mu\nu}q_R^{\,c}\,
G^a_{\mu\nu}$, so the scalars behave as colour-sextet leptoquarks
($B=-1/3$, $L=-1$).

Phenomenologically these operators give **single** production of a sextet state
in quark–gluon fusion at a hadron collider (for example $u\,g\to \bar F_u$,
$d\,g\to\bar F_d$, since $3\otimes 8\supset \bar 6$), followed by the
charge-conjugate decay back to a quark plus a gluon; the strength is set per
quark generation by `CFu`/`CFd`. The scalar operators mediate lepton-plus-jet
final states — associated production of $S_{u,d}$ with a charged lepton, and
decays such as $S\to q\,\ell\,g$ — with a flavour pattern controlled by the
quark $\times$ lepton generation matrices `CSu`/`CSd`. All new vertices count as
QCD order 1, and the complex phases in the couplings ($C^I$, zero by default)
allow CP-violating effects.
