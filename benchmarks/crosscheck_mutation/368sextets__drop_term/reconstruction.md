# Reconstruction of `sanitized.fr`

## 0. Conventions used below

* Gauge group: the Standard Model group $SU(3)_C \times SU(2)_L \times U(1)_Y$. The file adds no new gauge group; it only adds a new **colour representation**:
  `AddGaugeRepresentation[SU3C -> {T6, Sextet}]` declares the six–dimensional (sextet) representation of $SU(3)_C$, with generators $(T_6^a)_{st}$, $s,t = 1\ldots 6$ (`IndexRange[Index[Sextet]] = Range[6]`, index style `s`).
* $(T^a)_{ij}$ are the fundamental $SU(3)_C$ generators, $a=1\ldots 8$, $i,j = 1,2,3$.
* $K^s_{\;ij}$ is the sextet Clebsch–Gordan tensor, symmetric in $ij$, that maps a symmetric pair of fundamental indices onto one sextet index; `K6bar[s,i,j]` $=\bar K^s_{\;ij} = (K^s_{\;ij})^{*}$. It satisfies $\bar K^s_{\;ij}K^t_{\;ij} = \delta^{st}$ and fixes the sextet generators in terms of the fundamental ones ($T_6^a \propto \bar K\,T^a K$, with the normalisation of the FeynRules sextet implementation).
* $\varepsilon_{ijk}$ is the totally antisymmetric $SU(3)$ invariant tensor (`Eps`).
* `Ga[mu]` $=\gamma^\mu$; `ProjP` $=P_R=\tfrac12(1+\gamma_5)$; `ProjM` $=P_L=\tfrac12(1-\gamma_5)$.
* The combination `(I/2)(Ga[mu].Ga[nu] - Ga[nu].Ga[mu])` written out in the file is exactly
  $\sigma^{\mu\nu} = \tfrac{i}{2}\,[\gamma^\mu,\gamma^\nu]$.
* `CC[psi]` is the charge conjugate field $\psi^{c} = C\bar\psi^{T}$; `CC[uqbar]` is therefore $\overline{u^{c}}$. Because $(\psi_{L,R})^{c} = (\psi^{c})_{R,L}$, the combination $\overline{u^{c}}\,P_R = \overline{P_L u^{c}} = \overline{(u_R)^{c}}$: **the Standard Model quark always enters through its right‑handed component.**
* Field strengths (`FS`):
  $G^a_{\mu\nu} = \partial_\mu G^a_\nu - \partial_\nu G^a_\mu + g_s f^{abc} G^b_\mu G^c_\nu$, and
  $B_{\mu\nu} = \partial_\mu B_\nu - \partial_\nu B_\mu$.
* `HC[tmp]` adds the Hermitian conjugate of the preceding expression.
* $u_f$, $d_f$ are the SM up- and down-type quarks (generation index $f$), $\ell_x$ the SM charged leptons (generation index $x$).

### Covariant derivative

All four new states are $SU(2)_L$ singlets (no `Index[SU2W]` / `Index[SU2D]` is declared) and colour sextets. `DC` therefore expands to

$$
D_\mu \,\Psi^{s} \;=\; \Big(\partial_\mu \,\delta^{st} \;-\; i\,g_s\,(T_6^a)^{st}\,G^a_\mu \;-\; i\,g_1\,Y\,B_\mu\,\delta^{st}\Big)\Psi^{t},
$$

and identically for the scalars $\Phi^{s}$. Here $g_s$ is the $SU(3)_C$ coupling, $g_1$ the $U(1)_Y$ coupling and $Y$ the hypercharge of the field. Since $T^3 = 0$ for every new field, $Q = T^3 + Y = Y$, which is exactly what the `QuantumNumbers` entries declare. In the mass eigenbasis the $U(1)_Y$ piece is $-i e Q A_\mu + i e \tan\theta_W\, Q\, Z_\mu$; there is **no** $W^\pm$ coupling.

### Colour structure of the interaction terms

Every interaction term carries the same colour tensor

$$
\mathcal{K}^{\,a,s}_{\;i} \;\equiv\; \varepsilon_{i j k}\,(T^a)_{j l}\,\bar K^{s}_{\;l k}.
$$

This is the unique invariant of $\mathbf{3}\otimes\mathbf{6}\otimes\mathbf{8}$. It must appear because $\mathbf{3}\otimes\mathbf{6} = \mathbf{8}\oplus\mathbf{10}$ contains no singlet: a quark and a colour sextet **cannot** be coupled without an adjoint field. This is why every interaction below is written with a gluon field strength $G^a_{\mu\nu}$ and is therefore a higher‑dimensional (effective) operator suppressed by a cutoff $\Lambda$.

---

## 1. Lagrangian

### 1.1 Free / gauge sector

**`LPsiuFree`** — Dirac kinetic and mass term for the sextet fermion $\Psi_u$:

$$
\mathcal{L}_{\Psi_u}^{\text{free}} \;=\; i\,\bar\Psi_u^{\,s}\,\gamma^\mu \big(D_\mu \Psi_u\big)^{s} \;-\; M_{\Psi_u}\,\bar\Psi_u^{\,s}\,\Psi_u^{\,s},
\qquad D_\mu = \partial_\mu - i g_s T_6^a G^a_\mu - i g_1 \big(-\tfrac23\big) B_\mu .
$$

**`LPsidFree`** — Dirac kinetic and mass term for the sextet fermion $\Psi_d$:

$$
\mathcal{L}_{\Psi_d}^{\text{free}} \;=\; i\,\bar\Psi_d^{\,s}\,\gamma^\mu \big(D_\mu \Psi_d\big)^{s} \;-\; M_{\Psi_d}\,\bar\Psi_d^{\,s}\,\Psi_d^{\,s},
\qquad D_\mu = \partial_\mu - i g_s T_6^a G^a_\mu - i g_1 \big(+\tfrac13\big) B_\mu .
$$

**`LPhiuFree`** — kinetic and mass term for the sextet scalar $\Phi_u$:

$$
\mathcal{L}_{\Phi_u}^{\text{free}} \;=\; \big(D_\mu \Phi_u^{\,s}\big)^{\dagger}\big(D^\mu \Phi_u^{\,s}\big) \;-\; M_{\Phi_u}^{2}\,\Phi_u^{\,s\dagger}\Phi_u^{\,s},
\qquad D_\mu = \partial_\mu - i g_s T_6^a G^a_\mu - i g_1 \big(+\tfrac13\big) B_\mu .
$$

**`LPhidFree`** — kinetic and mass term for the sextet scalar $\Phi_d$:

$$
\mathcal{L}_{\Phi_d}^{\text{free}} \;=\; \big(D_\mu \Phi_d^{\,s}\big)^{\dagger}\big(D^\mu \Phi_d^{\,s}\big) \;-\; M_{\Phi_d}^{2}\,\Phi_d^{\,s\dagger}\Phi_d^{\,s},
\qquad D_\mu = \partial_\mu - i g_s T_6^a G^a_\mu - i g_1 \big(+\tfrac43\big) B_\mu .
$$

No scalar potential beyond the mass terms is written: there is no quartic and no Higgs portal.

### 1.2 Dimension‑5 chromomagnetic quark–sextet‑fermion operators

**`LPsiuG`** — right‑handed up‑type quark, sextet fermion $\Psi_u$ and one gluon field strength:

$$
\mathcal{L}_{\Psi_u G} \;=\; -\,i\,\frac{\kappa^{u}_{f}}{\Lambda_{\Psi_u}}\;
\varepsilon_{ijk}\,(T^a)_{jl}\,\bar K^{s}_{\;lk}\;
\overline{u^{c}_{f}}{}^{\,i}\,P_R\,\sigma^{\mu\nu}\,\Psi_u^{\,s}\;G^a_{\mu\nu}\;+\;\mathrm{h.c.}
$$

Equivalently, with the chirality made explicit, $\overline{u^{c}_{f}}\,P_R\,\sigma^{\mu\nu}\Psi_u = \overline{(u_{R\,f})^{c}}\;\sigma^{\mu\nu}\,\Psi_{u\,R}$ (the projector commutes with $\sigma^{\mu\nu}$). Operator dimension 5, suppressed by one power of $\Lambda_{\Psi_u}$. Summation over the generation index $f=1,2,3$ is implied.

**`LPsidG`** — the same with the down-type quark and $\Psi_d$:

$$
\mathcal{L}_{\Psi_d G} \;=\; -\,i\,\frac{\kappa^{d}_{f}}{\Lambda_{\Psi_d}}\;
\varepsilon_{ijk}\,(T^a)_{jl}\,\bar K^{s}_{\;lk}\;
\overline{d^{c}_{f}}{}^{\,i}\,P_R\,\sigma^{\mu\nu}\,\Psi_d^{\,s}\;G^a_{\mu\nu}\;+\;\mathrm{h.c.}
$$

### 1.3 Dimension‑7 $B_{\mu\nu}G^{\mu\nu}$ operators

Here the spinor bilinear carries **no** $\sigma^{\mu\nu}$; the two Lorentz indices are carried by the two field strengths, which are contracted with each other.

**`LPsiuB`**:

$$
\mathcal{L}_{\Psi_u B} \;=\; -\,i\,\frac{\kappa^{Bu}_{f}}{\Lambda_{\Psi_u B}^{3}}\;
\varepsilon_{ijk}\,(T^a)_{jl}\,\bar K^{s}_{\;lk}\;
\overline{u^{c}_{f}}{}^{\,i}\,P_R\,\Psi_u^{\,s}\;B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\mathrm{h.c.}
$$

**`LPsidB`**:

$$
\mathcal{L}_{\Psi_d B} \;=\; -\,i\,\frac{\kappa^{Bd}_{f}}{\Lambda_{\Psi_d B}^{3}}\;
\varepsilon_{ijk}\,(T^a)_{jl}\,\bar K^{s}_{\;lk}\;
\overline{d^{c}_{f}}{}^{\,i}\,P_R\,\Psi_d^{\,s}\;B_{\mu\nu}\,G^{a\,\mu\nu}\;+\;\mathrm{h.c.}
$$

Both are dimension‑7 operators (two field strengths plus a scalar bilinear), suppressed by $\Lambda^{3}$. The scalar bilinear $\overline{u^{c}}P_R\Psi_u$ pairs the right‑handed quark with the left‑handed component of $\Psi_u$ ($\overline{P_L u^c}\,P_R\Psi_u$), unlike the $\sigma^{\mu\nu}$ operators, which are chirality preserving.

### 1.4 Dimension‑6 quark–lepton–scalar (leptoquark) operator

**`LPhiuG`**:

$$
\mathcal{L}_{\Phi_u G} \;=\; -\,i\,\frac{\lambda^{u}_{x f}}{\Lambda_{\Phi_u}^{2}}\;
\varepsilon_{ijk}\,(T^a)_{jl}\,\bar K^{s}_{\;lk}\;\Phi_u^{\,s}\;
\overline{u^{c}_{f}}{}^{\,i}\,\sigma^{\mu\nu}\,P_R\,\ell_{x}\;G^a_{\mu\nu}\;+\;\mathrm{h.c.}
$$

with $\overline{u^{c}_{f}}\,\sigma^{\mu\nu}P_R\,\ell_x = \overline{(u_{R\,f})^{c}}\;\sigma^{\mu\nu}\,\ell_{R\,x}$. Both generation indices are summed, $\lambda^u_{xf}$ being a $3\times3$ matrix in (lepton, quark) generation space. Dimension 6, suppressed by $\Lambda_{\Phi_u}^{2}$. Note the file writes `ProjP` to the *right* of $\sigma^{\mu\nu}$ here and to the *left* in `LPsiuG`/`LPsidG`; the two orderings are identical because $[\sigma^{\mu\nu},\gamma_5]=0$.

Lepton number is conserved by this term: $L(\overline{u^{c}})=0$, $L(\ell)=+1$, $L(\Phi_u)=-1$. Electric charge is conserved: $+\tfrac23 - 1 + \tfrac13 = 0$.

### 1.5 Total

**`LTotal`**:

$$
\mathcal{L}_{\text{tot}} = \mathcal{L}_{\Psi_u}^{\text{free}} + \mathcal{L}_{\Psi_d}^{\text{free}} + \mathcal{L}_{\Phi_u}^{\text{free}} + \mathcal{L}_{\Phi_d}^{\text{free}} + \mathcal{L}_{\Psi_u G} + \mathcal{L}_{\Psi_d G} + \mathcal{L}_{\Psi_u B} + \mathcal{L}_{\Psi_d B} + \mathcal{L}_{\Phi_u G}.
$$

### 1.6 Gap in the file (incomplete sector)

The $\Phi_d$ scalar has **only** a free Lagrangian. Two declared external parameters, `lamd` ($\lambda^{d}_{xf}$) and `LamPhd` ($\Lambda_{\Phi_d}$), are never used anywhere in the file, and there is no `LPhidG` in `LTotal`. The pattern of the other three sectors (each up/down pair appears symmetrically) and the quantum numbers of $\Phi_d$ ($Q=4/3$, $L=-1$, which exactly balances $\overline{d^{c}}\,\ell$: $-\tfrac13 - 1 + \tfrac43 = 0$) show that the matching term

$$
\mathcal{L}_{\Phi_d G} \;=\; -\,i\,\frac{\lambda^{d}_{x f}}{\Lambda_{\Phi_d}^{2}}\;
\varepsilon_{ijk}(T^a)_{jl}\bar K^{s}_{\;lk}\;\Phi_d^{\,s}\;
\overline{d^{c}_{f}}{}^{\,i}\,\sigma^{\mu\nu}P_R\,\ell_{x}\;G^a_{\mu\nu} \;+\;\mathrm{h.c.}
$$

is the term the parameter set was written for, but it is **absent from the file as given**. As it stands, $\Phi_d$ is stable and only gauge interacting, and the couplings `lamd` and `LamPhd` have no effect.

---

## 2. Field table

All new fields are colour **sextets** ($\mathbf{6}$ of $SU(3)_C$), $SU(2)_L$ **singlets** (no weak index declared), and **not** self‑conjugate. Because $T^3=0$, hypercharge equals electric charge in the file's convention $Q = T^3 + Y$.

| `.fr` class | Symbol | Spin | $SU(3)_C$ | $SU(2)_L$ | $Q$ | $Y$ | $L$ | Self‑conj. | Mass (symbol, value) | Width (symbol, value) | PDG |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `S[100]` `Phiu` | $\Phi_u^{\,s}$ | 0 | $\mathbf{6}$ | $\mathbf{1}$ | $+1/3$ | $+1/3$ | $-1$ | No | `MPHU` = 1000 GeV | `WPHU` = 10 GeV | 9000001 |
| `S[101]` `Phid` | $\Phi_d^{\,s}$ | 0 | $\mathbf{6}$ | $\mathbf{1}$ | $+4/3$ | $+4/3$ | $-1$ | No | `MPHD` = 1000 GeV | `WPHD` = 10 GeV | 9000002 |
| `F[100]` `Psiu` | $\Psi_u^{\,s}$ | 1/2 (Dirac) | $\mathbf{6}$ | $\mathbf{1}$ | $-2/3$ | $-2/3$ | 0 (not declared) | No | `MPSU` = 1000 GeV | `WPSU` = 10 GeV | 9000011 |
| `F[101]` `Psid` | $\Psi_d^{\,s}$ | 1/2 (Dirac) | $\mathbf{6}$ | $\mathbf{1}$ | $+1/3$ | $+1/3$ | 0 (not declared) | No | `MPSD` = 1000 GeV | `WPSD` = 10 GeV | 9000012 |

Remarks:

* $\Psi_u$ carries the electric charge of $\bar u$ and $\Psi_d$ that of $\bar d$; they are sextet analogues of the conjugate right‑handed quarks. Baryon number assignment implied by the interactions: $B(\Psi_u) = B(\Psi_d) = -1/3$.
* $\Phi_u$ and $\Phi_d$ carry $L=-1$ and couple a quark to a charged lepton: they are **leptoquarks in the colour sextet**, i.e. sextet analogues of the $S_1$‑type ($Q=1/3$) and $\tilde S_1$‑type ($Q=4/3$) scalar leptoquarks. Implied $B(\Phi_{u,d}) = -1/3$.
* Propagator types are the FeynRules defaults for a charged scalar (`D`, arrow forward) and a Dirac fermion (`Straight`, arrow forward).

---

## 3. External parameters

### 3.1 Cutoff scales — block `SXTCUTOFF`, `InteractionOrder -> {NP,-1}`, all 1000. (GeV)

| Symbol | `.fr` name | Block order | Multiplies | Meaning |
|---|---|---|---|---|
| $\Lambda_{\Psi_u}$ | `LamPsu` | 1 | $1/\Lambda$ in `LPsiuG` | Cutoff of the dim‑5 $u$–$\Psi_u$–$g$ chromomagnetic operator |
| $\Lambda_{\Psi_d}$ | `LamPsd` | 2 | $1/\Lambda$ in `LPsidG` | Cutoff of the dim‑5 $d$–$\Psi_d$–$g$ chromomagnetic operator |
| $\Lambda_{\Psi_u B}$ | `LamPsuB` | 3 | $1/\Lambda^{3}$ in `LPsiuB` | Cutoff of the dim‑7 $u$–$\Psi_u$–$B_{\mu\nu}G^{\mu\nu}$ operator |
| $\Lambda_{\Psi_d B}$ | `LamPsdB` | 4 | $1/\Lambda^{3}$ in `LPsidB` | Cutoff of the dim‑7 $d$–$\Psi_d$–$B_{\mu\nu}G^{\mu\nu}$ operator |
| $\Lambda_{\Phi_u}$ | `LamPhu` | 5 | $1/\Lambda^{2}$ in `LPhiuG` | Cutoff of the dim‑6 $u$–$\ell$–$\Phi_u$–$g$ leptoquark operator |
| $\Lambda_{\Phi_d}$ | `LamPhd` | 6 | — (**unused**) | Would be the cutoff of the missing $\Phi_d$ operator |

Each cutoff is an energy scale (mass dimension 1). Its negative `NP` interaction order means that a factor $1/\Lambda^{n}$ raises the new‑physics order of a vertex by $n$, so the counting is: `LPsiuG` $\to$ NP $=2$, `LPhiuG` $\to$ NP $=3$, `LPsiuB` $\to$ NP $=4$. The hierarchy is declared as `{QCD,1},{QED,2},{NP,1}`.

### 3.2 Dimensionless couplings, `InteractionOrder -> {NP,1}`

| Symbol | `.fr` name | Block | Indices | Default value | Multiplies | Meaning |
|---|---|---|---|---|---|---|
| $\kappa^{u}_{f}$ | `kapu` | `KAPU` | 1 generation | $0.05$ for $f=1,2,3$ | `LPsiuG` | Flavour‑diagonal strength of the $\overline{u^c_f}\sigma^{\mu\nu}\Psi_u G_{\mu\nu}$ chromomagnetic transition |
| $\kappa^{d}_{f}$ | `kapd` | `KAPD` | 1 generation | $0.05$ for $f=1,2,3$ | `LPsidG` | Same for the down sector |
| $\kappa^{Bu}_{f}$ | `kapuB` | `KAPUB` | 1 generation | $0.10$ for $f=1,2,3$ | `LPsiuB` | Strength of the dim‑7 $\overline{u^c_f}\,\Psi_u\,B_{\mu\nu}G^{\mu\nu}$ operator |
| $\kappa^{Bd}_{f}$ | `kapdB` | `KAPDB` | 1 generation | $0.10$ for $f=1,2,3$ | `LPsidB` | Same for the down sector |
| $\lambda^{u}_{xf}$ | `lamu` | `LAMU` | 2 generations (lepton $x$, quark $f$) | $0.1\,\delta_{xf}$ | `LPhiuG` | Leptoquark coupling matrix of $\Phi_u$ to $\overline{u^c_f}\,\ell_x$ |
| $\lambda^{d}_{xf}$ | `lamd` | `LAMD` | 2 generations | $0.1\,\delta_{xf}$ | — (**unused**) | Leptoquark coupling matrix that the missing $\Phi_d$ term would need |

All six couplings are dimensionless. The default flavour structure is diagonal and generation universal, so no new flavour violation is switched on at the default point.

Internal/derived quantities used but not declared here (they come from the imported SM model file): $g_s$, $g_1$, the quark fields `uq`, `dq`, the lepton field `l`, the gauge fields `G`, `B`, and the sextet tensors `T6`, `K6`, `K6bar` generated by `AddGaugeRepresentation`.

---

## 4. Physics summary

This is an effective‑field‑theory extension of the Standard Model by four **colour‑sextet** states at the TeV scale: two vector‑like Dirac fermions $\Psi_u\,(\mathbf{6},\mathbf{1},-2/3)$ and $\Psi_d\,(\mathbf{6},\mathbf{1},1/3)$, and two scalars $\Phi_u\,(\mathbf{6},\mathbf{1},1/3)$ and $\Phi_d\,(\mathbf{6},\mathbf{1},4/3)$ that carry lepton number $-1$, all with mass and width fixed to 1000 GeV and 10 GeV. All four couple to gluons, the photon and the $Z$ through the sextet covariant derivative, so they are produced in pairs by QCD with a large sextet colour charge. Because $\mathbf{3}\otimes\mathbf{6}$ contains no colour singlet, none of them can couple to a single quark renormalisably; every non‑gauge interaction in the file is therefore a higher‑dimension operator built with the unique $\mathbf{3}\otimes\mathbf{6}\otimes\mathbf{8}$ tensor $\varepsilon_{ijk}(T^a)_{jl}\bar K^{s}_{\;lk}$ and a gluon (or gluon plus hypercharge) field strength, suppressed by an explicit cutoff $\Lambda = 1$ TeV.

The interactions are all chirally right‑handed and use the charge conjugate quark: a dimension‑5 chromomagnetic transition $\overline{(u_R)^{c}}\,\sigma^{\mu\nu}\Psi_{uR}G^a_{\mu\nu}$ (and its down‑type copy), a dimension‑7 $\overline{u^{c}}\,\Psi_u\,B_{\mu\nu}G^{a\mu\nu}$ operator (and its down‑type copy), and a dimension‑6 leptoquark operator $\overline{(u_R)^{c}}\,\sigma^{\mu\nu}\ell_{R}\,\Phi_u\,G^a_{\mu\nu}$. Phenomenologically this gives single (associated) production of a sextet fermion with a quark and a gluon at hadron colliders, sextet‑fermion decay $\Psi_u \to \bar u\, g$ (plus $\bar u\,\gamma/\bar u\,Z$ through the $B_{\mu\nu}$ operator), QCD pair production of sextets with dijet, di‑photon‑plus‑jet and leptoquark‑like final states, and, from $\Phi_u$, a $\bar u\,\ell\, g$ leptoquark signature — i.e. resonant jet + lepton production correlated with an extra gluon. The $\Phi_d$ sector is incomplete in this file: its coupling matrix `lamd` and cutoff `LamPhd` are declared but no term uses them, so $\Phi_d$ interacts only through gauge couplings and its leptoquark decay is missing.
