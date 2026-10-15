# Reconstruction of `sanitized.fr`

The file extends the FeynRules Standard Model (`SM.fr` field names `uq, dq, l, vl, QL, LL, Phi`)
by one extra abelian gauge group, here called $U(1)_X$, with gauge boson $Z'$ (`Zp`), one
$SU(2)_L$-singlet complex scalar $\Phi_X$ (`PhiX`), and three generations of a self-conjugate
(Majorana) neutral fermion $N_i$ (`N`).

The $X$ charges of all fields are built from two free numbers $x_H$ and $x_\Phi$ as

$$
q_X(f) \;=\; x_H\,Y(f) \;+\; x_\Phi\,(B-L)(f),
$$

so the model interpolates between a pure $B-L$ gauge theory ($x_H=0$, $x_\Phi=1$, the default
values) and a hypercharge-like $U(1)$ direction ($x_\Phi=0$).

Throughout: $P_L=\tfrac{1}{2}(1-\gamma_5)$ = `ProjM`, $P_R=\tfrac{1}{2}(1+\gamma_5)$ = `ProjP`.
Generation indices $i,j$ and color indices are summed unless stated otherwise.

---

## 1. Lagrangian

The total Lagrangian added to the SM is (`LGeneralU1`)

$$
\mathcal{L}_{\rm GeneralU1}
=\mathcal{L}_{Z'F}+\mathcal{L}_{\Phi_X{\rm kin}}+\mathcal{L}_{HX}
-V_{\Phi_X}
+\left(\mathcal{L}_{\nu}^{D}+{\rm h.c.}\right)+\mathcal{L}_{\nu}^{M}.
$$

### Covariant derivatives

The scalar sector uses the FeynRules sign convention

$$
D_\mu \Phi_X=\left(\partial_\mu-i\,g_X\,q^{\Phi}_X\,Z'_\mu\right)\Phi_X ,
\qquad
D_\mu H=\left(\partial_\mu-i g_s\!\cdot\!0-i g\,\tfrac{\sigma^a}{2}W^a_\mu-i g' Y_H B_\mu
-i\,g_X\,q^{H}_X\,Z'_\mu\right)H .
$$

The fermion current term is written with an overall $-g_X$, i.e. it corresponds to

$$
D_\mu \psi=\left(\partial_\mu + i\,g_X\,q_X(\psi)\,Z'_\mu+\dots\right)\psi ,
$$

the SM pieces of the fermion covariant derivative being supplied by the SM model file.
(See the consistency notes in section 5 about this relative sign.)

No $-\tfrac{1}{4}Z'_{\mu\nu}Z'^{\mu\nu}$ field-strength term and no $B_{\mu\nu}Z'^{\mu\nu}$
kinetic-mixing term appear in this file; the gauge-kinetic part of the $Z'$ is assumed to be
supplied elsewhere. Kinetic mixing is instead absorbed into the free parameter $x_H$.

---

### `LZpF` — $Z'$ current coupling to matter

$$
\mathcal{L}_{Z'F}=-g_X\,Z'_\mu
\Big[
q^{Q}_X\big(\bar u\gamma^\mu P_L u+\bar d\gamma^\mu P_L d\big)
+q^{u}_X\,\bar u\gamma^\mu P_R u
+q^{d}_X\,\bar d\gamma^\mu P_R d
$$

$$
\qquad\qquad
+\;q^{L}_X\big(\bar\nu\gamma^\mu P_L \nu+\bar e\gamma^\mu P_L e\big)
+q^{e}_X\,\bar e\gamma^\mu P_R e
+q^{N}_X\,\bar N_i\gamma^\mu P_R N_i
\Big].
$$

Notes:

* The quark and lepton fields are the four-component **mass eigenstates** (`uq`, `dq`, `l`,
  `vl`), color index contracted diagonally, generation index contracted diagonally. The
  coupling is therefore flavour diagonal and generation universal: **no tree-level FCNC**.
* Left-handed pieces carry the doublet charges $q^Q_X$, $q^L_X$; right-handed pieces carry the
  singlet charges $q^u_X$, $q^d_X$, $q^e_X$, $q^N_X$.
* The SM neutrino `vl` appears only through $P_L$ (no right-handed SM neutrino).
* Because $N_i$ is a **Majorana** field, $\bar N\gamma^\mu N\equiv 0$, so
  $\bar N_i\gamma^\mu P_R N_i=\tfrac12\,\bar N_i\gamma^\mu\gamma_5 N_i$: the $Z'N N$ vertex is
  purely axial.

---

### `LPhiXKin` — kinetic term of the $U(1)_X$ breaking scalar

$$
\mathcal{L}_{\Phi_X{\rm kin}}=\left|D_\mu\Phi_X\right|^2
=\partial_\mu\Phi_X^{\dagger}\partial^\mu\Phi_X
+i\,g_X q^{\Phi}_X Z'^{\mu}\!\left(\Phi_X^{\dagger}\partial_\mu\Phi_X-\partial_\mu\Phi_X^{\dagger}\,\Phi_X\right)
+g_X^{2}\,(q^{\Phi}_X)^{2}\,Z'_\mu Z'^{\mu}\,\Phi_X^{\dagger}\Phi_X .
$$

This is exactly $|(\partial_\mu-i g_X q^\Phi_X Z'_\mu)\Phi_X|^2$ written out. After
$\Phi_X\to(v_\Phi+\phi_X+iG_{Z'})/\sqrt2$ the last term gives the $Z'$ mass

$$
M_{Z'}=g_X\,q^{\Phi}_X\,v_\Phi=2x_\Phi\,g_X\,v_\Phi .
$$

---

### `LHiggsX` — $U(1)_X$ part of the SM Higgs kinetic term

Only the pieces **beyond** the SM $|D^{\rm SM}_\mu H|^2$ are given:

$$
\mathcal{L}_{HX}=i\,g_X q^{H}_X Z'^{\mu}
\left(H^{\dagger}_a D^{\rm SM}_\mu H_a-\left(D^{\rm SM}_\mu H_a\right)^{\dagger}H_a\right)
+g_X^{2}\,(q^{H}_X)^{2}\,Z'_\mu Z'^{\mu}\,H^{\dagger}_a H_a ,
$$

with $a$ the $SU(2)_L$ doublet index (`FlavorExpand -> {SU2D, SU2W}`) and
$D^{\rm SM}_\mu=\partial_\mu-i g\tfrac{\sigma^b}{2}W^b_\mu-i g' Y_H B_\mu$ (`DC`).
Together with `LPhiXKin` this is the statement
$|D_\mu H|^2=|D^{\rm SM}_\mu H|^2+\mathcal{L}_{HX}$.

Physical consequence: with $\langle H\rangle=v/\sqrt2$ the first term produces a
**$Z$–$Z'$ mass mixing** proportional to $x_H\,g_X\,g\,v^2/c_W$, which vanishes for $x_H=0$
(pure $B-L$), plus $Z'Z'h$ and $Z'Zh$ vertices.

---

### `VPhiX` — scalar potential (enters as $-V$)

$$
V_{\Phi_X}=m_\Phi^{2}\,\Phi_X^{\dagger}\Phi_X
+\lambda_\Phi\left(\Phi_X^{\dagger}\Phi_X\right)^{2}
+\lambda'\left(H^{\dagger}_a H_a\right)\left(\Phi_X^{\dagger}\Phi_X\right),
\qquad
\mathcal{L}\supset -V_{\Phi_X}.
$$

$\lambda'$ (`lamHP`) is the Higgs portal; it mixes $\phi_X$ with the SM Higgs $h$ after both
vevs are switched on. Default $\lambda'=0$, i.e. no portal mixing.

---

### `LNuDiracYuk` — Dirac (neutrino) Yukawa, plus `HC[LNuDiracYuk]`

As written in the file, with the $SU(2)_L$ index $a$ contracted directly between $\bar L_L$ and
$H^{\dagger}$:

$$
\mathcal{L}_{\nu}^{D}=-\,Y_\nu^{ij}\;
\overline{L^{\,i}_{L,a}}\;P_R\,N_j\;\left(H_a\right)^{*}
\;+\;{\rm h.c.}
$$

In conventional notation this is the Dirac mass operator
$-Y_\nu^{ij}\,\overline{L^i_L}\,\tilde H\,N_{R\,j}+{\rm h.c.}$ (see section 5 on the index
contraction). After electroweak breaking it gives
$m_D^{ij}=Y_\nu^{ij}v/\sqrt2$, which combined with the Majorana mass below realises a
**type-I seesaw**. Default $Y_\nu=0$.

---

### `LNuMajoranaYuk` — Majorana Yukawa of the heavy neutrinos

$$
\mathcal{L}_{\nu}^{M}=
-\frac{1}{2}\,Y_N^{i}\,\Phi_X\;\overline{N_i}\,P_R\,N_i
-\frac{1}{2}\,Y_N^{i}\,\Phi_X^{\dagger}\;\overline{N_i}\,P_L\,N_i ,
\qquad\text{(no sum over repeated }i\text{ beyond the single index; }Y_N\text{ diagonal)} .
$$

The two halves are hermitian conjugates of each other ($Y_N$ is declared real), so no separate
`HC[...]` is added in the total Lagrangian. Replacing
$\Phi_X\to(v_\Phi+\phi_X+iG_{Z'})/\sqrt2$:

$$
\mathcal{L}_{\nu}^{M}\to
-\frac{1}{2}\,\frac{Y_N^{i}v_\Phi}{\sqrt2}\,\overline{N_i}N_i
-\frac{1}{2}\frac{Y_N^{i}}{\sqrt2}\,\phi_X\,\overline{N_i}N_i
+\frac{i}{2}\frac{Y_N^{i}}{\sqrt2}\,G_{Z'}\,\overline{N_i}\gamma_5 N_i ,
$$

so

$$
m_{N_i}=\frac{Y_N^{i}\,v_\Phi}{\sqrt2}
\qquad\Longleftrightarrow\qquad
Y_N^{i}=\frac{\sqrt2\,m_{N_i}}{v_\Phi},
$$

which is exactly the internal definition of `yN` in the file. This term carries $X$ charge
$q^\Phi_X+2q^N_X=2x_\Phi-2x_\Phi=0$: lepton number is broken by two units by
$\langle\Phi_X\rangle$.

---

### Gauge fixing

`FeynmanGauge = True`, `GaugeXi[V[100]] = GaugeXi[Zp]`, and `GZp` is declared as the Goldstone
of `Zp` with mass $M_{Z'}$ — i.e. $R_\xi$ gauge with $\xi=1$ for the $U(1)_X$ sector.

---

## 2. Field table

| Class | Symbol | Spin | $SU(3)_c$ | $SU(2)_L$ | $Y$ | $Q$ | $q_X$ | Self-conj. | Mass (symbol, value) | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `V[100]` | $Z'$ (`Zp`) | 1 | **1** | **1** | 0 | 0 | 0 (gauge boson of $U(1)_X$) | yes (real vector) | $M_{Z'}=7500$ GeV | $\Gamma_{Z'}=10$ GeV | 32 |
| `F[101]` | $N_{1,2,3}$ (`N`) | 1/2 | **1** | **1** (not declared) | 0 | 0 | $-x_\Phi$ | **yes — Majorana** | $m_{N_1}=m_{N_2}=m_{N_3}=10000$ GeV | 1 GeV each | 9900012, 9900014, 9900016 |
| `S[102]` | $\phi_X$ (`phiX`) | 0 | **1** | **1** | 0 | 0 | 0 (after breaking) | yes (real scalar) | $m_{\phi_X}=1000$ GeV | 1 GeV | 9000001 |
| `S[103]` | $G_{Z'}$ (`GZp`) | 0 | **1** | **1** | 0 | 0 | 0 | yes (real) | $M_{Z'}=7500$ GeV | 10 GeV | 9000002 — Goldstone of $Z'$ |
| `S[104]` | $\Phi_X$ (`PhiX`) | 0 | **1** | **1** | 0 | 0 | $+2x_\Phi$ | no (complex) | — (unphysical) | — | — |

`PhiX` is `Unphysical -> True` with
$\Phi_X=\left(v_\Phi+\phi_X+i\,G_{Z'}\right)/\sqrt2$, and `M$vevs = {{PhiX[], vPhi/Sqrt[2]}}`.
$N$ carries a `Generation` flavour index (3 members).

The SM fields are not redefined; they only acquire the $U(1)_X$ charges listed below.

### Induced $X$ charges of the SM fields (internal parameters)

| Field | $Y$ | $B-L$ | $q_X$ (file symbol) |
|---|---|---|---|
| $Q_L=(u_L,d_L)$ | $1/6$ | $1/3$ | `qQLX` $=x_H/6+x_\Phi/3$ |
| $u_R$ | $2/3$ | $1/3$ | `qURX` $=2x_H/3+x_\Phi/3$ |
| $d_R$ | $-1/3$ | $1/3$ | `qDRX` $=-x_H/3+x_\Phi/3$ |
| $L_L=(\nu_L,e_L)$ | $-1/2$ | $-1$ | `qLLX` $=-x_H/2-x_\Phi$ |
| $e_R$ | $-1$ | $-1$ | `qERX` $=-x_H-x_\Phi$ |
| $N_R$ | $0$ | $-1$ | `qNRX` $=-x_\Phi$ |
| $H$ | $-1/2$ (see §5) | $0$ | `qHX` $=-x_H/2$ |
| $\Phi_X$ | $0$ | $-2$ | `qPhiX` $=+2x_\Phi$ |

With three right-handed neutrinos this charge assignment cancels all $U(1)_X$ gauge anomalies
and the mixed gauge–gravitational anomaly for any $x_H,x_\Phi$.

---

## 3. Parameters

### External

| Symbol | LHA block / order | Default | Multiplies | Meaning |
|---|---|---|---|---|
| `gX` ($g_X$) | GENERALU1, 1 | 0.1 | every $Z'$ vertex in `LZpF`, `LPhiXKin`, `LHiggsX` | $U(1)_X$ gauge coupling; `InteractionOrder -> {NP,1}` |
| `xH` ($x_H$) | GENERALU1, 2 | 0. | enters all $q_X$ | weight of the hypercharge direction in $X=x_HY+x_\Phi(B-L)$; equivalently the (tree-level absorbed) kinetic-mixing parameter. $x_H=0$ gives pure $B-L$ |
| `xPhi` ($x_\Phi$) | GENERALU1, 3 | 1. | enters all $q_X$ | weight of the $B-L$ direction; overall normalisation of the $B-L$ charge |
| `lamPhi` ($\lambda_\Phi$) | GENERALU1, 4 | 0.1 | $(\Phi_X^\dagger\Phi_X)^2$ | quartic self-coupling of the $U(1)_X$ breaking scalar |
| `lamHP` ($\lambda'$) | GENERALU1, 5 | 0. | $(H^\dagger H)(\Phi_X^\dagger\Phi_X)$ | Higgs-portal quartic; controls $h$–$\phi_X$ mixing |
| `mPhi2` ($m_\Phi^2$) | GENERALU1, 6 | $10^6$ GeV$^2$ | $\Phi_X^\dagger\Phi_X$ | quadratic term of the $\Phi_X$ potential (mass-squared parameter) |
| `yNu` ($Y_\nu^{ij}$) | YNU, $3\times3$ real | 0. | $\overline{L^i_L}P_R N_j H^*$ | Dirac neutrino Yukawa matrix; sets $m_D=Y_\nu v/\sqrt2$ and the light–heavy mixing |
| `MZp` ($M_{Z'}$) | mass block | 7500 GeV | — | $Z'$ mass (used as input; $v_\Phi$ is derived from it) |
| `mN1,mN2,mN3` | mass block | 10000 GeV | — | heavy Majorana neutrino masses (used as input; $Y_N$ derived) |
| `WZp`, `WN1..3`, `WPhiX` | decay blocks | 10, 1, 1 GeV | — | total widths |
| `mPhiX` | mass block | 1000 GeV | — | mass of the real scalar $\phi_X$ |

### Internal (derived)

| Symbol | Definition | Meaning |
|---|---|---|
| `vPhi` ($v_\Phi$) | $M_{Z'}/(2g_X)$ | vev of $\Phi_X$, from $M_{Z'}=2x_\Phi g_X v_\Phi$ at $x_\Phi=1$ |
| `qQLX, qURX, qDRX, qLLX, qERX, qNRX, qHX, qPhiX` | table in §2 | $U(1)_X$ charges |
| `yN` ($Y_N^i$) | $\sqrt2\,m_{N_i}/v_\Phi$ | diagonal Majorana Yukawa of $N_i$ to $\Phi_X$ |

`M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,3}}` — all $U(1)_X$ vertices count as one
power of the new-physics order `NP`.

---

## 4. Physics summary

This is a minimal **anomaly-free $U(1)_X$ extension of the Standard Model**, where the gauged
charge is the general linear combination $X=x_H Y+x_\Phi(B-L)$; the pure $B-L$ model is the
special case $x_H=0,\;x_\Phi=1$. The new states are a heavy neutral gauge boson $Z'$
($M_{Z'}=7.5$ TeV by default), three heavy Majorana neutrinos $N_{1,2,3}$ (10 TeV), and one
real scalar $\phi_X$ (1 TeV) — the radial mode of the complex scalar $\Phi_X$ whose vev
$v_\Phi=M_{Z'}/2g_X$ breaks $U(1)_X$ and gives both the $Z'$ mass and the Majorana masses
$m_{N_i}=Y_N^i v_\Phi/\sqrt2$.

Phenomenologically the model mediates: Drell–Yan $Z'$ production $q\bar q\to Z'$ with
generation-universal, flavour-diagonal decays to all SM fermions with chirality-dependent
strengths set by $q^{Q,u,d,L,e}_X$, plus $Z'\to N_iN_i$ (purely axial) when kinematically
open; $Z'\to W^+W^-$, $Z'\to Zh$ and $Z$–$Z'$ mass mixing effects proportional to $x_H$;
heavy-neutrino production and decay $N\to \ell W,\nu Z,\nu h$ through the Dirac Yukawa $Y_\nu$
(lepton-number violating same-sign dilepton signatures, since $N$ is Majorana); and a scalar
sector with $\phi_X\to Z'Z',\,NN,\,hh$ and $h$–$\phi_X$ mixing through the Higgs portal
$\lambda'$. Together with $Y_\nu$ the Majorana masses realise a **type-I seesaw** for the light
neutrinos.

---

## 5. Consistency notes (conventions checked term by term)

These are observations about the file as written; they do not change the field content.

1. **Sign of the $Z'$ fermion current relative to the scalar sector.** `LZpF` has the overall
   factor $-g_X$, which corresponds to $D_\mu\psi=(\partial_\mu+i g_X q_X Z'_\mu)\psi$.
   `LPhiXKin` and `LHiggsX` correspond to $D_\mu\Phi=(\partial_\mu-i g_X q_X Z'_\mu)\Phi$, the
   FeynRules default. A single convention for both sectors would require one relative sign
   flip (equivalently $g_X\to-g_X$ in `LZpF`). Rates for $Z'$ production and decay are
   insensitive to this overall sign; interference with $\gamma/Z$ exchange is not.

2. **Sign of $q^H_X$.** The fermion charges follow $X=x_HY+x_\Phi(B-L)$ with the FeynRules
   hypercharge normalisation ($Y_{Q_L}=1/6$, $Y_{L_L}=-1/2$, ...). `qHX` $=-x_H/2$ corresponds
   instead to $Y_H=-1/2$, i.e. to the conjugate doublet $\tilde H$. The FeynRules SM doublet
   `Phi` carries $Y=+1/2$, so $U(1)_X$ invariance of the SM Yukawa couplings
   ($-q^Q_X+q^d_X+q^H_X=0$, $-q^L_X+q^e_X+q^H_X=0$) and of the Dirac neutrino term
   ($-q^L_X+q^N_X-q^H_X=0$) requires $q^H_X=+x_H/2$. With the default $x_H=0$ this has no
   numerical effect.

3. **$SU(2)_L$ contraction in `LNuDiracYuk`.** The file writes
   `LLbar[sp1,ii,ff1].ProjP.N[sp2,ff2] Phibar[ii]`, i.e. $\bar L_a\,P_R N\,(H_a)^*$ with a
   direct $\delta_{ab}$ contraction. The gauge-invariant Dirac operator is
   $\varepsilon_{ab}\bar L_a P_R N\,(H_b)^*$ ($=\bar L\tilde H N$), as used for the up-type
   Yukawa in `SM.fr` (`Phibar[jj] Eps[ii,jj]`). With the default $Y_\nu=0$ this also has no
   numerical effect.

4. **Missing $Z'$ kinetic term.** There is no $-\tfrac14 Z'_{\mu\nu}Z'^{\mu\nu}$ (`FS[Zp,mu,nu]`)
   in this file, and no $U(1)_Y$–$U(1)_X$ kinetic mixing term.

5. **$v_\Phi$ and the potential.** $v_\Phi=M_{Z'}/(2g_X)$ omits the factor $x_\Phi$
   ($M_{Z'}=2x_\Phi g_X v_\Phi$ in general); it is exact only at the default $x_\Phi=1$. The
   vev is supplied as an input rather than obtained by minimising $V_{\Phi_X}$, so $m_\Phi^2$,
   $\lambda_\Phi$, $v_\Phi$ and $m_{\phi_X}$ are not related by the tadpole condition in the
   default numerical values.
