# Reconstruction of `sanitized.fr`

## 0. Conventions used below

**Gauge group and covariant derivative.**
The file adds no new gauge group. It only adds a new colour representation:

```
AddGaugeRepresentation[SU3C -> {T6, Sextet}];   IndexRange[Index[Sextet]] = Range[6]
```

So `T6` are the generators $T^a_{(6)}$ of the **6** (sextet) of $SU(3)_C$, and every new
field carries one `Sextet` index $s=1\ldots6$.

All new fields declare only `Q` and `Y` (no `Index[SU2W]`), so they are **weak singlets**
with $Q=Y$. The FeynRules `DC[φ, mu]` therefore expands to

$$
D_\mu \;=\; \partial_\mu \;-\; i\,g_s\,G^a_\mu\,T^a_{(6)} \;-\; i\,g'\,Y\,B_\mu ,
\qquad Y=Q \ \ (\text{no } SU(2)_L \text{ term, no } W^\pm/W^3).
$$

For the conjugate fields $\bar\Phi$, $\bar\Psi$ the generator and hypercharge flip sign
($T^a_{(6)}\to -(T^a_{(6)})^{*}$, $Y\to-Y$). After electroweak symmetry breaking the $B_\mu$
piece is the usual photon/$Z$ combination with electric charge $Q$.

**FeynRules idioms expanded.**

| `.fr` idiom | Standard notation |
|---|---|
| `Ga[mu]` | $\gamma^\mu$ |
| `(I/2)(Ga[mu].Ga[nu] - Ga[nu].Ga[mu])` | $\sigma^{\mu\nu}=\tfrac{i}{2}[\gamma^\mu,\gamma^\nu]$ |
| `ProjP` / `ProjM` | $P_R=\tfrac{1+\gamma_5}{2}$ / $P_L=\tfrac{1-\gamma_5}{2}$ |
| `CC[uqbar]` | $\overline{u^{c}}$, with $u^{c}=C\,\bar u^{T}$ |
| `FS[G, mu, nu, aa]` | $G^{a}_{\mu\nu}=\partial_\mu G^a_\nu-\partial_\nu G^a_\mu+g_s f^{abc}G^b_\mu G^c_\nu$ |
| `FS[B, mu, nu]` | $B_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu$ (hypercharge, **not** the photon) |
| `HC[tmp]` | $+\,\mathrm{h.c.}$ |
| `K6bar[s,i,j]` | $(\bar K^{s})_{ij}$, the sextet Clebsch–Gordan tensor (symmetric in $ij$) that intertwines the **6** with $\mathbf{3}\otimes\mathbf{3}$ |
| `Eps[i1,i2,i3]` | $\varepsilon_{i_1i_2i_3}$, the $SU(3)$ invariant tensor |
| `l[sp,x]` | SM charged lepton $\ell_x$ ($x$ = generation) |
| `uq`, `dq` | SM up-type / down-type quarks, generation index $f$ |

**The common colour structure.** Every interaction term uses the same tensor

$$
\mathcal{C}^{a,s}_{\,i}\;\equiv\;\varepsilon_{i\,i_2\,i_3}\;T^{a}_{i_2 i_4}\;(\bar K^{s})_{i_4 i_3},
$$

which is the unique $SU(3)_C$ invariant coupling **one fundamental quark**, **one colour
sextet** and **one gluon (adjoint) field strength**, i.e. $\mathbf{3}\otimes\mathbf{6}\otimes\mathbf{8}\supset\mathbf{1}$.
Here $T^a$ is the fundamental generator and $\bar K^s$ converts the sextet index into the
symmetric pair of fundamental indices.

**Chirality bookkeeping.** In all terms the quark enters as $\overline{u^{c}}\,P_R$ (or
$\overline{d^{c}}\,P_R$). Using $\bar\chi P_R=\overline{P_L\chi}$ and $P_L\psi^c=(\psi_R)^c$,

$$
\overline{q^{c}}\,P_R \;=\; \overline{(q_R)^{c}},
$$

so **only the right-handed quark field participates**, and because $[\sigma^{\mu\nu},\gamma_5]=0$
the projector may equivalently be moved to the right, picking the right-handed component of
$\Psi$ or of $\ell$. The bilinear is of the $\psi^{T}C\,\Gamma\,\chi$ ("same-charge-flow") type,
not of the $\bar\psi\Gamma\chi$ type: the vertex annihilates a quark *together with* the new
state, rather than converting one into the other.

---

## 1. Lagrangian

### 1.1 Free / gauge-kinetic terms

**`LPsiuFree`** — Dirac kinetic and mass term for the sextet fermion $\Psi_u$:

$$
\mathcal{L}_{\Psi_u}^{\rm free}
= i\,\overline{\Psi}_u^{\,s}\,\gamma^\mu\!\left(D_\mu \Psi_u\right)_{s}
\;-\; M_{\Psi_u}\,\overline{\Psi}_u^{\,s}\,\Psi_{u,s},
\qquad
D_\mu\Psi_u=\Big(\partial_\mu - i g_s G^a_\mu T^a_{(6)} - i g'\,(-\tfrac23)\,B_\mu\Big)\Psi_u .
$$

($M_{\Psi_u}\equiv$ `MPSU`.)

**`LPsidFree`** — same for $\Psi_d$:

$$
\mathcal{L}_{\Psi_d}^{\rm free}
= i\,\overline{\Psi}_d^{\,s}\,\gamma^\mu\!\left(D_\mu \Psi_d\right)_{s}
\;-\; M_{\Psi_d}\,\overline{\Psi}_d^{\,s}\,\Psi_{d,s},
\qquad Y_{\Psi_d}=+\tfrac13 .
$$

**`LPhiuFree`** — complex scalar sextet $\Phi_u$:

$$
\mathcal{L}_{\Phi_u}^{\rm free}
= \left(D^\mu \Phi_u\right)^{\dagger}_{s}\left(D_\mu \Phi_u\right)_{s}
\;-\; M_{\Phi_u}^{2}\,\Phi_{u,s}^{\dagger}\Phi_{u,s},
\qquad Y_{\Phi_u}=+\tfrac13 .
$$

**`LPhidFree`** — complex scalar sextet $\Phi_d$:

$$
\mathcal{L}_{\Phi_d}^{\rm free}
= \left(D^\mu \Phi_d\right)^{\dagger}_{s}\left(D_\mu \Phi_d\right)_{s}
\;-\; M_{\Phi_d}^{2}\,\Phi_{d,s}^{\dagger}\Phi_{d,s},
\qquad Y_{\Phi_d}=+\tfrac43 .
$$

No scalar potential beyond the mass term is written: there is **no quartic self-coupling and
no Higgs portal**.

### 1.2 Chromomagnetic (dipole) transition operators, quark + sextet fermion + gluon

**`LPsiuG`** — as literally written in the file (see the consistency note in §5: the
`/LamPsu` denominator is absent, although `LamPsu` is declared):

$$
\mathcal{L}_{\Psi_u G}
= -\,i\,\kappa^{u}_{f}\;
\varepsilon_{i_1 i_2 i_3}\,T^{a}_{i_2 i_4}\,(\bar K^{s})_{i_4 i_3}\;
\overline{u^{c}_{f,i_1}}\;P_R\,\sigma^{\mu\nu}\,\Psi_{u,s}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.}
$$

Equivalently $-i\,\kappa^{u}_{f}\,\mathcal{C}^{a,s}_{\,i_1}\,\overline{(u_{R})^{c}_{f,i_1}}\,\sigma^{\mu\nu}\,\Psi_{u,s}\,G^{a}_{\mu\nu}+\mathrm{h.c.}$
The intended (dimension-5) form carries $\kappa^{u}_{f}/\Lambda_{\Psi_u}$.

**`LPsidG`**:

$$
\mathcal{L}_{\Psi_d G}
= -\,i\,\frac{\kappa^{d}_{f}}{\Lambda_{\Psi_d}}\;
\varepsilon_{i_1 i_2 i_3}\,T^{a}_{i_2 i_4}\,(\bar K^{s})_{i_4 i_3}\;
\overline{d^{c}_{f,i_1}}\;P_R\,\sigma^{\mu\nu}\,\Psi_{d,s}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.}
$$

### 1.3 Two-field-strength operators, quark + sextet fermion + gluon + $B$

Here there is **no** $\sigma^{\mu\nu}$: the fermion bilinear is a scalar, and the two field
strengths are contracted with each other.

**`LPsiuB`**:

$$
\mathcal{L}_{\Psi_u B}
= -\,i\,\frac{\kappa^{uB}_{f}}{\Lambda_{\Psi_u B}^{3}}\;
\varepsilon_{i_1 i_2 i_3}\,T^{a}_{i_2 i_4}\,(\bar K^{s})_{i_4 i_3}\;
\overline{u^{c}_{f,i_1}}\;P_R\,\Psi_{u,s}\;
B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\mathrm{h.c.}
$$

**`LPsidB`**:

$$
\mathcal{L}_{\Psi_d B}
= -\,i\,\frac{\kappa^{dB}_{f}}{\Lambda_{\Psi_d B}^{3}}\;
\varepsilon_{i_1 i_2 i_3}\,T^{a}_{i_2 i_4}\,(\bar K^{s})_{i_4 i_3}\;
\overline{d^{c}_{f,i_1}}\;P_R\,\Psi_{d,s}\;
B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\mathrm{h.c.}
$$

Both are dimension-7 operators ($3+2+2=7$), correctly suppressed by $\Lambda^{3}$.

### 1.4 Leptoquark dipole operators, quark + lepton + sextet scalar + gluon

**`LPhiuG`**:

$$
\mathcal{L}_{\Phi_u G}
= -\,i\,\frac{\lambda^{u}_{x f}}{\Lambda_{\Phi_u}^{2}}\;
\varepsilon_{i_1 i_2 i_3}\,T^{a}_{i_2 i_4}\,(\bar K^{s})_{i_4 i_3}\;\Phi_{u,s}\;
\overline{u^{c}_{f,i_1}}\;\sigma^{\mu\nu}\,P_R\,\ell_{x}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.}
$$

**`LPhidG`**:

$$
\mathcal{L}_{\Phi_d G}
= -\,i\,\frac{\lambda^{d}_{x f}}{\Lambda_{\Phi_d}^{2}}\;
\varepsilon_{i_1 i_2 i_3}\,T^{a}_{i_2 i_4}\,(\bar K^{s})_{i_4 i_3}\;\Phi_{d,s}\;
\overline{d^{c}_{f,i_1}}\;\sigma^{\mu\nu}\,P_R\,\ell_{x}\;
G^{a}_{\mu\nu}\;+\;\mathrm{h.c.}
$$

Note the index order in the coupling: `lamu[xx, ff]` has the **lepton** generation first and
the **quark** generation second, i.e. $\lambda^{u}_{x f}$ multiplies $\overline{u^{c}_{f}}\ldots\ell_{x}$.
Both operators are dimension-6 ($3+1+2$), suppressed by $\Lambda^{2}$.

### 1.5 Total

$$
\mathcal{L}_{\rm total}
=\mathcal{L}_{\Psi_u}^{\rm free}+\mathcal{L}_{\Psi_d}^{\rm free}
+\mathcal{L}_{\Phi_u}^{\rm free}+\mathcal{L}_{\Phi_d}^{\rm free}
+\mathcal{L}_{\Psi_u G}+\mathcal{L}_{\Psi_d G}
+\mathcal{L}_{\Psi_u B}+\mathcal{L}_{\Psi_d B}
+\mathcal{L}_{\Phi_u G}+\mathcal{L}_{\Phi_d G}.
$$

---

## 2. Field table

| `.fr` class | Symbol | Spin | $SU(3)_C$ | $SU(2)_L$ | $Q=Y$ | Lepton no. | Self-conj. | Mass (symbol, value) | Width | PDG |
|---|---|---|---|---|---|---|---|---|---|---|
| `S[100]` | $\Phi_u$ | 0 (complex scalar) | **6** (sextet) | singlet (not declared) | $+1/3$ | $-1$ | No | `MPHU` $=1000$ GeV | `WPHU` $=10$ GeV | 9000001 |
| `S[101]` | $\Phi_d$ | 0 (complex scalar) | **6** | singlet | $+4/3$ | $-1$ | No | `MPHD` $=1000$ GeV | `WPHD` $=10$ GeV | 9000002 |
| `F[100]` | $\Psi_u$ | 1/2 (Dirac) | **6** | singlet | $-2/3$ | 0 (not declared) | No | `MPSU` $=1000$ GeV | `WPSU` $=10$ GeV | 9000011 |
| `F[101]` | $\Psi_d$ | 1/2 (Dirac) | **6** | singlet | $+1/3$ | 0 | No | `MPSD` $=1000$ GeV | `WPSD` $=10$ GeV | 9000012 |

Remarks:

* $Y$ is set equal to $Q$ for every state, consistent with $Q=T_3+Y$ for weak singlets.
* Baryon number is **not** declared. The interactions fix it: each vertex contains exactly
  one quark, so $B(\Phi_u)=B(\Phi_d)=B(\Psi_u)=B(\Psi_d)=-1/3$ if $B$ is to be conserved.
  With the declared $L(\Phi)=-1$, the $\Phi$ operators conserve both $B$ and $L$.
* Charge balance, vertex by vertex: $u(+\tfrac23)+\Psi_u(-\tfrac23)=0$;
  $d(-\tfrac13)+\Psi_d(+\tfrac13)=0$; $u(+\tfrac23)+\ell^-(-1)+\Phi_u(+\tfrac13)=0$;
  $d(-\tfrac13)+\ell^-(-1)+\Phi_d(+\tfrac43)=0$.
* All four states are sextets, so they couple to gluons through $T^a_{(6)}$ in $D_\mu$ —
  pair production by QCD is automatic.

---

## 3. External parameters

### 3.1 Suppression scales — block `SXTCUTOFF`, all `Value -> 1000.` (GeV), `InteractionOrder -> {NP,-1}`

| Symbol | Block order | Multiplies (as $1/\Lambda^{n}$) | Meaning |
|---|---|---|---|
| `LamPsu` $\Lambda_{\Psi_u}$ | 1 | **nothing — not referenced in any term** | Intended cutoff of the $\Psi_u$–$u$–$g$ dipole operator `LPsiuG` |
| `LamPsd` $\Lambda_{\Psi_d}$ | 2 | $1/\Lambda$ in `LPsidG` | Cutoff of the $\Psi_d$–$d$–$g$ dipole operator |
| `LamPsuB` $\Lambda_{\Psi_u B}$ | 3 | $1/\Lambda^{3}$ in `LPsiuB` | Cutoff of the $\Psi_u$–$u$–$g$–$B$ operator |
| `LamPsdB` $\Lambda_{\Psi_d B}$ | 4 | $1/\Lambda^{3}$ in `LPsidB` | Cutoff of the $\Psi_d$–$d$–$g$–$B$ operator |
| `LamPhu` $\Lambda_{\Phi_u}$ | 5 | $1/\Lambda^{2}$ in `LPhiuG` | Cutoff of the $\Phi_u$–$u$–$\ell$–$g$ operator |
| `LamPhd` $\Lambda_{\Phi_d}$ | 6 | $1/\Lambda^{2}$ in `LPhidG` | Cutoff of the $\Phi_d$–$d$–$\ell$–$g$ operator |

### 3.2 Dimensionless couplings, all `InteractionOrder -> {NP,1}`

| Symbol | Indices | Block | Default value | Multiplies | Meaning |
|---|---|---|---|---|---|
| `kapu` $\kappa^{u}_{f}$ | 1 generation (quark) | `KAPU` | $0.05$ for $f=1,2,3$ | `LPsiuG` | Chromomagnetic transition coupling $u_{R,f}\,\Psi_u\,g$ |
| `kapd` $\kappa^{d}_{f}$ | 1 generation (quark) | `KAPD` | $0.05$ for $f=1,2,3$ | `LPsidG` | Chromomagnetic transition coupling $d_{R,f}\,\Psi_d\,g$ |
| `kapuB` $\kappa^{uB}_{f}$ | 1 generation (quark) | `KAPUB` | $0.10$ for $f=1,2,3$ | `LPsiuB` | Coupling of $u_{R,f}\,\Psi_u$ to $B_{\mu\nu}G^{a\mu\nu}$ |
| `kapdB` $\kappa^{dB}_{f}$ | 1 generation (quark) | `KAPDB` | $0.10$ for $f=1,2,3$ | `LPsidB` | Coupling of $d_{R,f}\,\Psi_d$ to $B_{\mu\nu}G^{a\mu\nu}$ |
| `lamu` $\lambda^{u}_{x f}$ | 2 generations (lepton $x$, quark $f$) | `LAMU` | diagonal $0.1$, off-diagonal $0$ | `LPhiuG` | Leptoquark dipole coupling $u_{R,f}\,\ell_{R,x}\,\Phi_u\,g$; the diagonal default means no lepton-flavour violation |
| `lamd` $\lambda^{d}_{x f}$ | 2 generations (lepton $x$, quark $f$) | `LAMD` | diagonal $0.1$, off-diagonal $0$ | `LPhidG` | Leptoquark dipole coupling $d_{R,f}\,\ell_{R,x}\,\Phi_d\,g$; flavour diagonal by default |

Masses `MPHU`, `MPHD`, `MPSU`, `MPSD` (all $1000$ GeV) and widths `WPHU`, `WPHD`, `WPSU`,
`WPSD` (all $10$ GeV) are the remaining external inputs, declared inside the particle classes.

**Coupling-order counting.** `M$InteractionOrderHierarchy` is `{QCD,1}, {QED,2}, {NP,1}`.
With $\kappa,\lambda$ at $NP^{+1}$ and each $\Lambda$ at $NP^{-1}$, the vertices carry
$NP^{2}$ (`LPsidG`), $NP^{4}$ (`LPsiuB`, `LPsidB`) and $NP^{3}$ (`LPhiuG`, `LPhidG`).

---

## 4. Physics summary

The model adds four heavy ($1$ TeV) **colour-sextet** states that are electroweak singlets:
two complex scalars $\Phi_u$ ($Q=1/3$) and $\Phi_d$ ($Q=4/3$) with lepton number $-1$, and two
Dirac fermions $\Psi_u$ ($Q=-2/3$) and $\Psi_d$ ($Q=1/3$). They have no renormalisable Yukawa
couplings to the Standard Model; instead they connect to it only through **higher-dimensional
gluon-dipole operators** built with the unique $\mathbf{3}\otimes\mathbf{6}\otimes\mathbf{8}$
colour invariant $\varepsilon_{i_1i_2i_3}T^{a}_{i_2i_4}(\bar K^{s})_{i_4i_3}$, always with a
charge-conjugated **right-handed** quark.

The fermionic sextets couple to one right-handed quark and one gluon field strength through a
$\sigma^{\mu\nu}G^{a}_{\mu\nu}$ dipole, and to $B_{\mu\nu}G^{a\mu\nu}$ through a scalar
bilinear at dimension 7. The scalar sextets are **leptoquarks**: they couple to one
right-handed quark, one right-handed charged lepton and one gluon at dimension 6.

Phenomenologically these states are pair-produced by ordinary QCD (sextet colour charge), and
— more characteristically — **singly produced in quark–gluon fusion**, $qg\to\Psi$ and
$qg\to\Phi\,\ell$. The fermions decay back to a quark plus a gluon (and, through the $B$
operators, to quark + gluon + photon/$Z$), giving dijet and jet+$\gamma$ resonances. The
scalars decay to a quark plus a charged lepton plus a gluon, giving lepton+jets signatures with
same-sign lepton–quark charge flow typical of leptoquarks. The default flavour-diagonal
$\lambda$ matrices switch off lepton-flavour violation, and all couplings are generation
independent by default.

---

## 5. Internal-consistency notes (for the checker)

1. **`LPsiuG` is missing its suppression scale.** `LamPsu` is declared in block `SXTCUTOFF`
   (order 1) with `InteractionOrder -> {NP,-1}` but appears in **no** Lagrangian term. Its
   partner `LPsidG` does divide by `LamPsd`. As written, `LPsiuG` is a dimension-5 operator
   multiplied by a dimensionless coupling, so the term has mass dimension 5, not 4 — the
   Lagrangian is not dimensionally homogeneous, and the $u$- and $d$-sector dipole operators
   are not normalised the same way. The consistent form is
   $-i\,(\kappa^{u}_{f}/\Lambda_{\Psi_u})\,\varepsilon T\bar K\;\overline{u^{c}}P_R\sigma^{\mu\nu}\Psi_u\,G^{a}_{\mu\nu}+\mathrm{h.c.}$
   This also changes the $NP$ order of the vertex from $NP^{1}$ to $NP^{2}$, matching `LPsidG`.
2. `Eps`, `T` and `K6bar` are used but not defined in this file; they come from the FeynRules
   colour-sextet machinery loaded together with the SM model file, as do `uq`, `dq`, `l`,
   `G` and `B`.
3. In `LPsiuG`, `LPsidG` the projector sits to the left of $\sigma^{\mu\nu}$ and in `LPhiuG`,
   `LPhidG` to the right; because $[\sigma^{\mu\nu},\gamma_5]=0$ the two orderings are
   physically identical, and every term selects the same chirality combination.
4. `LPsiuB` and `LPsidB` declare the Block variables `i1..i4`, `aa`, `mu`, `nu` and use them
   all; the operator is a genuine dimension-7 structure and is not simply $\Lambda^{-3}$ times
   the dipole term.
