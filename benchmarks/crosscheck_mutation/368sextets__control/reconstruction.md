# Reconstruction of `sanitized.fr`

## 0. Conventions and notation

The file declares a **new SU(3)$_c$ representation**:

```
IndexRange[Index[Sextet]] = NoUnfold[Range[6]];
AddGaugeRepresentation[SU3C -> {T6, Sextet}];
```

so every new field carries one index of the **colour sextet** $\mathbf{6}$ of SU(3)$_c$, with
generators $T^a_{(6)}$ (`T6`).

Index names used below:

| symbol | meaning | range |
| --- | --- | --- |
| $i,j,k,l$ | SU(3)$_c$ fundamental (triplet) index | 1..3 |
| $a$ | SU(3)$_c$ adjoint index | 1..8 |
| $s$ | SU(3)$_c$ sextet index (`Sextet`) | 1..6 |
| $f$ | quark generation (`ff`) | 1..3 |
| $x$ | lepton generation (`xx`) | 1..3 |
| $\mu,\nu$ | Lorentz index | 0..3 |

FeynRules idioms expanded:

* `Ga[mu]` $=\gamma^\mu$; `ProjP` $=P_R=\tfrac{1}{2}(1+\gamma_5)$; `ProjM` $=P_L$.
* $\tfrac{i}{2}\left(\gamma^\mu\gamma^\nu-\gamma^\nu\gamma^\mu\right)=\sigma^{\mu\nu}$.
  Every `(I/2)(Ga[mu].Ga[nu] - Ga[nu].Ga[mu])` block in the file is exactly $\sigma^{\mu\nu}$.
* `CC[uqbar]` $=\overline{u^{c}}$ with $u^{c}=C\,\bar u^{\,T}$, $\overline{u^{c}}=-u^{T}C^{-1}$.
  Because $\bar a P_R b=\overline{(P_L a)}\,b_R$ and $(\psi^{c})_L=(\psi_R)^{c}$, the chain
  $\overline{u^{c}}\,\Gamma P_R\,\chi$ (with $\Gamma=1$ or $\sigma^{\mu\nu}$, both of which
  commute with $\gamma_5$) equals $\overline{(u_R)^{c}}\,\Gamma\,\chi_R$.
  **All new couplings are therefore purely right-handed in both the quark and the partner field.**
* `Eps[i1,i2,i3]` $=\varepsilon_{ijk}$ is the SU(3)$_c$ Levi-Civita tensor on *fundamental*
  indices (not the Lorentz $\epsilon$).
* `T[aa,i,j]` $=T^{a}_{ij}$, the fundamental SU(3) generators.
* `K6bar[s,i,j]` $=\left(K^{s}_{ij}\right)^{*}$, the conjugate Clebsch–Gordan tensor that maps
  the sextet index onto a **symmetric** pair of triplet indices, $K^{s}_{ij}=K^{s}_{ji}$,
  $\mathrm{Tr}\!\left[K^{s}K^{t\dagger}\right]=\delta^{st}$.
* `FS[G,mu,nu,aa]` $=G^{a}_{\mu\nu}=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_s f^{abc}G^b_\mu G^c_\nu$.
* `FS[B,mu,nu]` $=B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu$ (abelian hypercharge field strength).
* `HC[tmp]` $=$ hermitian conjugate, added explicitly to every interaction term.
* `uq`, `dq`, `l` are the Standard-Model up-type quark, down-type quark and charged-lepton
  classes of the host SM model file.

### The colour tensor

Every interaction term contains the same SU(3)$_c$ structure

$$
\mathcal{C}^{\,a,s}_{\;i}\;=\;\varepsilon_{ijk}\,T^{a}_{jl}\,\bigl(K^{s}_{lk}\bigr)^{*} .
$$

It contracts one **triplet** index (carried by $\overline{q^{c}}$, which transforms as $\mathbf{3}$
because $q^{c}\sim\bar{\mathbf{3}}$), one **adjoint** index (carried by $G^{a}_{\mu\nu}$) and one
**sextet** index (carried by the new field). This is the unique invariant available, since
$\mathbf{3}\otimes\mathbf{6}=\mathbf{8}\oplus\mathbf{10}$ and $\mathbf{8}\otimes\mathbf{8}\supset\mathbf{1}$.
A gluon field strength is therefore **mandatory** in each new vertex: there is no
gauge-invariant $\bar q\,\Psi$ or $\bar q\,\ell\,\Phi$ operator without it.

### Covariant derivative

The new fields are SU(2)$_L$ singlets (no `Index[SU2D]`/`Index[SU2W]` is declared), so `DC`
expands with SU(3)$_c$ in the sextet representation plus U(1)$_Y$ only:

$$
D_\mu\,\Psi_{u,s}=\Bigl(\partial_\mu\,\delta_{st}
-i\,g_s\,G^{a}_\mu\,\bigl(T^{a}_{(6)}\bigr)_{st}
-i\,g'\,Y_{\Psi_u}\,B_\mu\,\delta_{st}\Bigr)\Psi_{u,t},
\qquad
B_\mu=\cos\theta_W A_\mu-\sin\theta_W Z_\mu ,
$$

and identically for $\Psi_d,\Phi_u,\Phi_d$ with their own hypercharges. The declared
quantum numbers obey $Q=T_3+Y=Y$, so the abelian piece is equivalently
$-i\,e\,Q\left(A_\mu-\tan\theta_W Z_\mu\right)$. There is **no** $W^{\pm}$ coupling and **no**
Higgs portal term anywhere in the file.

---

## 1. Lagrangian

$$
\mathcal{L}_{\rm total}=
\mathcal{L}_{\Psi u}^{\rm free}+\mathcal{L}_{\Psi d}^{\rm free}
+\mathcal{L}_{\Phi u}^{\rm free}+\mathcal{L}_{\Phi d}^{\rm free}
+\mathcal{L}_{\Psi u G}+\mathcal{L}_{\Psi d G}
+\mathcal{L}_{\Psi u B}+\mathcal{L}_{\Psi d B}
+\mathcal{L}_{\Phi u G}+\mathcal{L}_{\Phi d G}
$$

(`LTotal`). The SM Lagrangian itself is supplied by the host model file.

### 1.1 Free / kinetic terms

**`LPsiuFree`** — Dirac sextet $\Psi_u$:

$$
\mathcal{L}_{\Psi u}^{\rm free}
= i\,\overline{\Psi}_{u,s}\,\gamma^{\mu}\left(D_\mu\Psi_u\right)_{s}
\;-\;M_{\Psi u}\,\overline{\Psi}_{u,s}\,\Psi_{u,s}
$$

**`LPsidFree`** — Dirac sextet $\Psi_d$:

$$
\mathcal{L}_{\Psi d}^{\rm free}
= i\,\overline{\Psi}_{d,s}\,\gamma^{\mu}\left(D_\mu\Psi_d\right)_{s}
\;-\;M_{\Psi d}\,\overline{\Psi}_{d,s}\,\Psi_{d,s}
$$

**`LPhiuFree`** — complex scalar sextet $\Phi_u$:

$$
\mathcal{L}_{\Phi u}^{\rm free}
= \left(D^{\mu}\Phi_u\right)^{\dagger}_{s}\left(D_\mu\Phi_u\right)_{s}
\;-\;M_{\Phi u}^{2}\,\Phi^{\dagger}_{u,s}\Phi_{u,s}
$$

**`LPhidFree`** — complex scalar sextet $\Phi_d$:

$$
\mathcal{L}_{\Phi d}^{\rm free}
= \left(D^{\mu}\Phi_d\right)^{\dagger}_{s}\left(D_\mu\Phi_d\right)_{s}
\;-\;M_{\Phi d}^{2}\,\Phi^{\dagger}_{d,s}\Phi_{d,s}
$$

No quartic self-interaction and no scalar potential beyond the mass terms is written.

### 1.2 Chromo-magnetic dipole operators, fermionic sextets (dimension 5)

**`LPsiuG`** — $\overline{u^{c}}\,\Psi_u\,G$ dipole:

$$
\mathcal{L}_{\Psi u G}=
-\,\frac{i\,\kappa^{u}_{f}}{\Lambda_{\Psi u}}\;
\varepsilon_{ijk}\,T^{a}_{jl}\,\bigl(K^{s}_{lk}\bigr)^{*}\;
\overline{\left(u^{c}_{f}\right)}_{i}\;P_R\,\sigma^{\mu\nu}\;\Psi_{u,s}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.}
$$

Equivalently, using $[\sigma^{\mu\nu},\gamma_5]=0$ and $(\psi^{c})_L=(\psi_R)^{c}$,

$$
\mathcal{L}_{\Psi u G}=
-\,\frac{i\,\kappa^{u}_{f}}{\Lambda_{\Psi u}}\;
\mathcal{C}^{\,a,s}_{\;i}\;
\overline{\left(u_{R,f}^{\,c}\right)}_{i}\,\sigma^{\mu\nu}\,\Psi_{u,s}^{R}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.}
$$

**`LPsidG`** — same operator with the down-type quarks:

$$
\mathcal{L}_{\Psi d G}=
-\,\frac{i\,\kappa^{d}_{f}}{\Lambda_{\Psi d}}\;
\varepsilon_{ijk}\,T^{a}_{jl}\,\bigl(K^{s}_{lk}\bigr)^{*}\;
\overline{\left(d^{c}_{f}\right)}_{i}\;P_R\,\sigma^{\mu\nu}\;\Psi_{d,s}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.}
$$

Note the flavour index $f$ is summed: $\kappa^{u}_{f}$ and $\kappa^{d}_{f}$ are generation
diagonal (one coupling per quark generation), and the same $\Psi_u$ ($\Psi_d$) couples to all
three generations.

### 1.3 Double field-strength operators, fermionic sextets (dimension 7)

**`LPsiuB`** — $\overline{u^{c}}\,\Psi_u\,B_{\mu\nu}G^{\mu\nu}$, **no** $\sigma^{\mu\nu}$; the two
field strengths are contracted with each other:

$$
\mathcal{L}_{\Psi u B}=
-\,\frac{i\,\kappa^{uB}_{f}}{\Lambda_{\Psi u B}^{3}}\;
\varepsilon_{ijk}\,T^{a}_{jl}\,\bigl(K^{s}_{lk}\bigr)^{*}\;
\overline{\left(u^{c}_{f}\right)}_{i}\,P_R\,\Psi_{u,s}\;
B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\mathrm{h.c.}
$$

**`LPsidB`**:

$$
\mathcal{L}_{\Psi d B}=
-\,\frac{i\,\kappa^{dB}_{f}}{\Lambda_{\Psi d B}^{3}}\;
\varepsilon_{ijk}\,T^{a}_{jl}\,\bigl(K^{s}_{lk}\bigr)^{*}\;
\overline{\left(d^{c}_{f}\right)}_{i}\,P_R\,\Psi_{d,s}\;
B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\mathrm{h.c.}
$$

These are scalar (non-dipole) bilinears: the Lorentz indices live entirely on the two field
strengths, so the operator is a pure $P_R$ bilinear times $B\!\cdot\!G$.

### 1.4 Leptoquark-type operators, scalar sextets (dimension 6)

**`LPhiuG`** — $\overline{u^{c}}\,\ell\,\Phi_u\,G$:

$$
\mathcal{L}_{\Phi u G}=
-\,\frac{i\,\lambda^{u}_{xf}}{\Lambda_{\Phi u}^{2}}\;
\varepsilon_{ijk}\,T^{a}_{jl}\,\bigl(K^{s}_{lk}\bigr)^{*}\;\Phi_{u,s}\;
\overline{\left(u^{c}_{f}\right)}_{i}\,\sigma^{\mu\nu}\,P_R\;\ell_{x}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.}
$$

**`LPhidG`** — $\overline{d^{c}}\,\ell\,\Phi_d\,G$:

$$
\mathcal{L}_{\Phi d G}=
-\,\frac{i\,\lambda^{d}_{xf}}{\Lambda_{\Phi d}^{2}}\;
\varepsilon_{ijk}\,T^{a}_{jl}\,\bigl(K^{s}_{lk}\bigr)^{*}\;\Phi_{d,s}\;
\overline{\left(d^{c}_{f}\right)}_{i}\,\sigma^{\mu\nu}\,P_R\;\ell_{x}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.}
$$

Index order matters: in `lamu[xx, ff]` the **first** index $x$ is the *lepton* generation and
the **second** index $f$ is the *quark* generation. The scalar enters **unconjugated**
($\Phi_{u,s}$, not $\Phi^{\dagger}_{u,s}$), contracted through $\left(K^{s}\right)^{*}$.
In these two terms the chiral projector sits to the right of $\sigma^{\mu\nu}$, whereas in
`LPsiuG`/`LPsidG` it sits to the left; the two orderings are identical because
$[\sigma^{\mu\nu},P_R]=0$.

### 1.5 Vertices generated

Because $G^{a}_{\mu\nu}$ contains the non-abelian $g_s f^{abc}G^bG^c$ piece, each interaction
term yields both a 3-point (or 4-point) vertex with one gluon and one extra vertex with two
gluons:

| term | vertices |
| --- | --- |
| `LPsiuG`, `LPsidG` | $q\,\Psi\,g$ and $q\,\Psi\,g\,g$ |
| `LPsiuB`, `LPsidB` | $q\,\Psi\,g\,(\gamma/Z)$ and $q\,\Psi\,g\,g\,(\gamma/Z)$ |
| `LPhiuG`, `LPhidG` | $q\,\ell\,\Phi\,g$ and $q\,\ell\,\Phi\,g\,g$ |
| free terms | $\Psi\Psi g$, $\Psi\Psi\gamma/Z$, $\Phi\Phi g$, $\Phi\Phi gg$, $\Phi\Phi\gamma/Z$, ... (sextet QCD + U(1)) |

---

## 2. Field table

| `.fr` class | symbol | spin | SU(3)$_c$ | SU(2)$_L$ | $Q$ | $Y$ | $L$ | $B$ (implied) | self-conj. | mass symbol / value | width / value | PDG |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `S[100]` `Phiu` | $\Phi_u$ | 0 | $\mathbf{6}$ | singlet (not declared) | $+1/3$ | $+1/3$ | $-1$ | $-1/3$ | no (complex) | `MPHU` $=1000$ GeV | `WPHU` $=10$ GeV | 9000001 |
| `S[101]` `Phid` | $\Phi_d$ | 0 | $\mathbf{6}$ | singlet (not declared) | $+4/3$ | $+4/3$ | $-1$ | $-1/3$ | no (complex) | `MPHD` $=1000$ GeV | `WPHD` $=10$ GeV | 9000002 |
| `F[100]` `Psiu` | $\Psi_u$ | 1/2 (Dirac) | $\mathbf{6}$ | singlet (not declared) | $-2/3$ | $-2/3$ | 0 | $-1/3$ | no | `MPSU` $=1000$ GeV | `WPSU` $=10$ GeV | 9000011 |
| `F[101]` `Psid` | $\Psi_d$ | 1/2 (Dirac) | $\mathbf{6}$ | singlet (not declared) | $+1/3$ | $+1/3$ | 0 | $-1/3$ | no | `MPSD` $=1000$ GeV | `WPSD` $=10$ GeV | 9000012 |

Remarks:

* $Q=Y$ for all four states, consistent with $Q=T_3+Y$ for SU(2)$_L$ singlets.
* $L=-1$ is declared for the two scalars only; it is required by $\overline{u^{c}}\,\ell\,\Phi_u$.
* The baryon numbers are **not** declared in the file; they are fixed by demanding that every
  operator conserve $B$, using $B\!\left(\overline{q^{c}}\right)=+1/3$. All operators then
  conserve both $B$ and $L$ (hence also $B-L$); there is no proton-decay operator.
* All four states are degenerate at the default point, $M=1$ TeV, $\Gamma=10$ GeV.
* Only the sextet index is declared; the fields are flavour singlets (the flavour indices live
  on the couplings).

---

## 3. Parameters

### 3.1 Cutoff scales — block `SXTCUTOFF`, `InteractionOrder -> {NP,-1}`

| symbol | `.fr` name | block entry | default | multiplies (appears as) |
| --- | --- | --- | --- | --- |
| $\Lambda_{\Psi u}$ | `LamPsu` | 1 | 1000. GeV | $1/\Lambda_{\Psi u}$ in `LPsiuG` — scale of the $u\Psi_u g$ chromo-dipole |
| $\Lambda_{\Psi d}$ | `LamPsd` | 2 | 1000. GeV | $1/\Lambda_{\Psi d}$ in `LPsidG` — scale of the $d\Psi_d g$ chromo-dipole |
| $\Lambda_{\Psi u B}$ | `LamPsuB` | 3 | 1000. GeV | $1/\Lambda^{3}_{\Psi uB}$ in `LPsiuB` — scale of the $u\Psi_u B G$ operator |
| $\Lambda_{\Psi d B}$ | `LamPsdB` | 4 | 1000. GeV | $1/\Lambda^{3}_{\Psi dB}$ in `LPsidB` — scale of the $d\Psi_d B G$ operator |
| $\Lambda_{\Phi u}$ | `LamPhu` | 5 | 1000. GeV | $1/\Lambda^{2}_{\Phi u}$ in `LPhiuG` — scale of the $u\ell\Phi_u g$ operator |
| $\Lambda_{\Phi d}$ | `LamPhd` | 6 | 1000. GeV | $1/\Lambda^{2}_{\Phi d}$ in `LPhidG` — scale of the $d\ell\Phi_d g$ operator |

All six are effective-theory cutoff (suppression) scales with mass dimension 1.

### 3.2 Dimensionless couplings — `InteractionOrder -> {NP,1}`

| symbol | `.fr` name | block | indices | default | multiplies | meaning |
| --- | --- | --- | --- | --- | --- | --- |
| $\kappa^{u}_{f}$ | `kapu` | `KAPU` | quark generation | $0.05$ (all 3) | $\overline{u^{c}_{f}}\sigma^{\mu\nu}P_R\Psi_u G^{a}_{\mu\nu}$ | chromo-magnetic dipole coupling, up sector |
| $\kappa^{d}_{f}$ | `kapd` | `KAPD` | quark generation | $0.05$ (all 3) | $\overline{d^{c}_{f}}\sigma^{\mu\nu}P_R\Psi_d G^{a}_{\mu\nu}$ | chromo-magnetic dipole coupling, down sector |
| $\kappa^{uB}_{f}$ | `kapuB` | `KAPUB` | quark generation | $0.10$ (all 3) | $\overline{u^{c}_{f}}P_R\Psi_u\,B_{\mu\nu}G^{a\mu\nu}$ | mixed hypercharge–gluon coupling, up sector |
| $\kappa^{dB}_{f}$ | `kapdB` | `KAPDB` | quark generation | $0.10$ (all 3) | $\overline{d^{c}_{f}}P_R\Psi_d\,B_{\mu\nu}G^{a\mu\nu}$ | mixed hypercharge–gluon coupling, down sector |
| $\lambda^{u}_{xf}$ | `lamu` | `LAMU` | (lepton gen., quark gen.) | $0.1\,\delta_{xf}$ | $\Phi_u\,\overline{u^{c}_{f}}\sigma^{\mu\nu}P_R\ell_x\,G^{a}_{\mu\nu}$ | lepton–quark–sextet-scalar (leptoquark) coupling matrix, up sector |
| $\lambda^{d}_{xf}$ | `lamd` | `LAMD` | (lepton gen., quark gen.) | $0.1\,\delta_{xf}$ | $\Phi_d\,\overline{d^{c}_{f}}\sigma^{\mu\nu}P_R\ell_x\,G^{a}_{\mu\nu}$ | lepton–quark–sextet-scalar (leptoquark) coupling matrix, down sector |

$\lambda^{u}$ and $\lambda^{d}$ are diagonal in the default point, so lepton flavour is tied to
quark flavour and there is no tree-level lepton-flavour violation at that point; the general
$3\times3$ matrix form allows it.

### 3.3 Masses and widths (internal to the class definitions)

`MPHU`, `MPHD`, `MPSU`, `MPSD` $=1000.$ GeV; `WPHU`, `WPHD`, `WPSU`, `WPSD` $=10.$ GeV.

### 3.4 Interaction-order bookkeeping

```
M$InteractionOrderHierarchy = { {QCD,1}, {QED,2}, {NP,1} };
```

Since each $\Lambda$ carries `{NP,-1}` and appears in a denominator, the NP order of a vertex is
$1+n$ with $n$ the power of $1/\Lambda$: NP $=2$ for `LPsiuG`/`LPsidG`, NP $=3$ for
`LPhiuG`/`LPhidG`, NP $=4$ for `LPsiuB`/`LPsidB`.

---

## 4. Physics summary

This is an **effective (higher-dimensional) extension of the Standard Model by four colour-sextet
states**: two complex scalars $\Phi_u$ ($Q=1/3$) and $\Phi_d$ ($Q=4/3$) carrying $L=-1$, and two
Dirac fermions $\Psi_u$ ($Q=-2/3$) and $\Psi_d$ ($Q=1/3$). All four are electroweak singlets of
mass $1$ TeV, all four have ordinary sextet QCD and U(1) gauge interactions from their covariant
kinetic terms, and all four couple to the SM only through **non-renormalisable operators that
necessarily contain a gluon field strength**, because $\mathbf{3}\otimes\mathbf{6}$ has no
singlet with anything smaller than the adjoint.

The fermionic sextets couple to a single right-handed quark through a dimension-5
chromo-magnetic dipole $\overline{q_R^{\,c}}\,\sigma^{\mu\nu}\Psi\,G^{a}_{\mu\nu}/\Lambda$ and
through a dimension-7 $\overline{q_R^{\,c}}\,\Psi\,B_{\mu\nu}G^{a\mu\nu}/\Lambda^{3}$ operator;
the scalar sextets act as **colour-sextet leptoquarks** through a dimension-6
$\Phi\,\overline{q_R^{\,c}}\,\sigma^{\mu\nu}\ell_R\,G^{a}_{\mu\nu}/\Lambda^{2}$ operator. Every
operator is purely right-handed in both fermions and conserves $B$ and $L$ separately.

Phenomenologically the model gives QCD pair production of sextets at a hadron collider
($gg,q\bar q\to\Psi\bar\Psi,\Phi\Phi^{\dagger}$, with the large sextet colour charge enhancing the
rate), plus **single production in quark–gluon fusion** $qg\to\Psi$ via the dipole vertex and
$qg\to\Phi\,\ell$ via the leptoquark vertex. The decays follow from the same vertices:
$\Psi\to q\,g$ (and $\Psi\to q\,g\,\gamma/Z$ from the $B\!\cdot\!G$ operator), giving dijet and
jet+gluon resonances, and $\Phi\to q\,\ell\,g$, giving lepton+jets final states with a
leptoquark-like $q\ell$ system. The $B_{\mu\nu}G^{a\mu\nu}$ terms additionally mediate
associated $\gamma$ or $Z$ production with the sextet fermion.
