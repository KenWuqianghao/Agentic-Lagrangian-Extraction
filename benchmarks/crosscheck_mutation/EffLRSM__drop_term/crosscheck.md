# Cross-check: `reconstruction.md` against the Effective LRSM paper

**Paper:** "Automated Neutrino Jet and Top Jet Predictions at Next-to-Leading-Order with
Parton Shower Matching in Effective Left-Right Symmetric Models"
(Mattelaer, Mitra, Ruiz; IPPP-16-102, CP3-16-51).

**Reconstruction:** `sanitized.fr`, an independent read of a FeynRules file that I do not have.

---

## 1. Where the paper defines the model

The paper defines the model in Sec. II, "Effective Left-Right Symmetric Model"
(`\label{sec:theory}`). It gives only the *interaction* terms. It does not write the
kinetic terms or the mass terms as equations.

Equation numbers below count `\begin{equation}` / `\begin{eqnarray}` blocks from the start
of the body. I also give the paper's own `\label` so that each reference stays unambiguous.

| Ref. | Label | Content |
|---|---|---|
| Eq. (1) | — | Gauge group $SU(3)_c\otimes SU(2)_L\otimes SU(2)_R\otimes U(1)_{B-L}$ |
| Sec. II, para. 1 | — | Field content: SM states, $W_R^\pm$, $Z_R$ (mass eigenstates), three heavy Majorana $N_i$ |
| Eq. (4) | `chcurrent` | $W_R$ charged current for quarks |
| Eq. (5) | (unlabeled) | $W_R$ charged current for leptons, with $X$ and $Y$ mixing |
| Eq. (6) | — | Scaling of $\vert Y\vert^2$ and $\vert X\vert^2$ |
| Eq. (7) | `eq:lrsmNuMixing` | Default mixing: $Y$ diagonal and unit, $X=0$ |
| Table I | `tb:qNumbers` | $T^{3,f}_L$, $T^{3,f}_R$, $Q^f$ for all chiral fermions |
| Eq. (8) | `neucurrent` | $Z_R$ neutral current for **every** chiral fermion $f$ |
| Eqs. (9), (10) | — | $g^{Z_R,f}_L$ and $g^{Z_R,f}_R$ chiral charges |
| Eqs. (11)–(17) | — | $W_R$, $Z_R$ partial and total widths |
| Eq. (18) | `eq:massRelationship` | $M_{Z_R}=\sqrt{2\cos^2\theta_W/\cos 2\theta_W}\,M_{W_R}$ |
| Eq. (19) | `eq:lrsmInputs` | $M_{W_R}=3$ TeV, $m_{N_1}=173.3$ GeV, $m_{N_2},m_{N_3}=10^{12}$ GeV |
| Table II | `tb:lrsmParam` | Masses, partial widths and total widths |
| Sec. II C | `sec:modelLimits` | Statement that non-Abelian $W_R$, $Z_R$ couplings are absent |
| App. C | `app:GenCuts` | Heavy neutrino PDG code 9900012 |

Two statements in the paper are important for the comparison, and they are prose, not
equations:

* Sec. II, after Table I: "all fermions with $(B-L)$ charges, including $\nu_L$ and $N_R$,
  couple to $\ZR$."
* Sec. II C: "non-Abelian $\WR$ and $\ZR$ interactions, as well as their couplings to SM
  bosons, are ill-defined."

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Field content: $W_R^\pm$, $Z_R$ aligned with mass eigenstates; three heavy Majorana $N_i$ aligned with RH chiral states (Sec. II, para. 1) | `V[100]` $W_R^\pm$, `V[101]` $Z_R$, `F[100]` $N_i$ (3 members), $N$ self-conjugate | **agree** | Spin, charge and Majorana nature all match. The paper adds no scalars, and the reconstruction finds none. |
| $W_R$ kinetic + mass term (not written in the paper) | $-\tfrac12 W^\dagger_{R\mu\nu}W_R^{\mu\nu}+M^2_{W_R}W^\dagger_{R\mu}W_R^\mu$, Proca, abelian `FS` | **agree** | Normalization is the standard one for a complex vector. The paper never writes it, but Sec. II C says the non-Abelian parts are absent. This supports the abelian `FS`. |
| $Z_R$ kinetic + mass term (not written in the paper) | $-\tfrac14 Z_{R\mu\nu}Z_R^{\mu\nu}+\tfrac12 M^2_{Z_R}Z_{R\mu}Z_R^\mu$, real vector | **agree** | Same remark. Factors $\tfrac14$ and $\tfrac12$ are correct for a real vector. |
| $N$ kinetic + Majorana mass (not written in the paper) | $\tfrac{i}{2}\overline{N_i}\gamma^\mu\partial_\mu N_i-\tfrac12 M_{N_i}\overline{N_i}N_i$, $N=N^c$, diagonal in flavor | **agree** | The $\tfrac12$ factors are the Majorana normalization. The paper treats $N_i$ as Majorana states with independent masses, so a diagonal mass is correct. |
| No $\gamma W_R^+W_R^-$ and no $Z W_R^+W_R^-$ vertex (Sec. II C) | No `DC` anywhere; abelian `FS[WR,mu,nu]`; no triple gauge vertex | **agree** | The reconstruction reproduces a limitation that the paper states in words. |
| $\mathcal{L}_{W_R qq'}=\frac{-\kappa^q_R g}{\sqrt2}\sum_{ij}\overline{u}_i V^{\rm CKM'}_{ij}W^+_{R\mu}\gamma^\mu P_R d_j+{\rm H.c.}$, Eq. (4) `chcurrent` | `LWRq` $=-\frac{\kappa^q_R g_L}{\sqrt2}\overline{u}_i (V^R_{\rm CKM})_{ij}\gamma^\mu P_R d_j W_{R\mu}+{\rm h.c.}$ | **agree** | Prefactor, $1/\sqrt2$, $P_R$ chirality, index order and the h.c. all match. Color is diagonal in both. |
| $V^{\rm CKM'}$ is the RH CKM matrix, taken diagonal with unit entries (Eq. (4) text; Sec. II para. 4) | `VCKMR`, $3\times3$, `Unitary -> True`, default $\mathbb{1}$ | **agree** | The paper also says the `diagonalCKM.rst` restriction sets this. |
| $\mathcal{L}_{W_R\ell\nu/N}=\frac{-\kappa^\ell_R g}{\sqrt2}\sum_\ell[\sum_m\overline{\nu^c_m}X_{\ell m}+\sum_{m'}\overline{N_{m'}}Y_{\ell m'}]W^+_{R\mu}\gamma^\mu P_R\,\ell^-+{\rm H.c.}$, Eq. (5) | `LWRl` $=-\frac{\kappa^\ell_R g_L}{\sqrt2}[\overline{N}_i(Y_N)_{ij}\gamma^\mu P_R\ell_j+\overline{\nu^c}_i(X_N)_{ij}\gamma^\mu P_R\ell_j]W_{R\mu}+{\rm h.c.}$ | **agree** | Both pieces are present, with the same prefactor, the same $P_R$, and the same conjugated light field $\overline{\nu^c}$. The index order of $Y$ and $X$ is transposed; see disagreement D2. |
| Default mixing $\vert Y_{eN_1}\vert=\vert Y_{\mu N_2}\vert=\vert Y_{\tau N_3}\vert=1$, all other $Y$ and all $X$ zero, Eq. (7) `eq:lrsmNuMixing` | `YN` default $\mathbb{1}$; `XN` default $0$ | **agree** | The reconstruction states that the $X_N$ vertex vanishes by default. This matches Eq. (7). |
| $\mathcal{L}_{Z_R ff}=\frac{-\kappa^f_R g}{\sqrt{1-(1/\kappa^f_R)^2\tan^2\theta_W}}\sum_{f}\overline{f}Z_{R\mu}\gamma^\mu(g^{Z_R,f}_LP_L+g^{Z_R,f}_RP_R)f$, Eq. (8) `neucurrent`, **quark part** $f=u,d$ | `LZRq` $=-\frac{\kappa^q_R g_L}{n^q_{Z_R}}[g^u_L\overline{u}\gamma^\mu P_Lu+g^u_R\overline{u}\gamma^\mu P_Ru+g^d_L\overline{d}\gamma^\mu P_Ld+g^d_R\overline{d}\gamma^\mu P_Rd]Z_{R\mu}$ | **agree** | The prefactor matches: `nZRq` $=\sqrt{1-t_W^2/\kappa_R^{q\,2}}$ is exactly the paper's denominator. Flavor-diagonal in both. |
| $\mathcal{L}_{Z_R ff}$, Eq. (8) `neucurrent`, **lepton part** $f=e,\nu_L,N_R$. The paper says explicitly that $\nu_L$ and $N_R$ couple to $Z_R$, and Table II lists $\Gamma(Z_R\to\ell^+\ell^-)=7.64$, $\Gamma(Z_R\to\nu_e\nu_e)=2.78$, $\Gamma(Z_R\to N_1N_1)=10.2$ GeV | *absent from* `LTotal`. Only the charges `nZRl`, `gLZRe`, `gRZRe`, `gLZRv`, `gRZRn` are declared, and none is used | **missing-in-reconstruction** | This is the one substantive gap; see disagreement D1. |
| $g^{Z_R,u}_L=(T^{3,u}_L-Q^u)\tan^2\theta_W/\kappa_R^{f2}=-\tfrac16 t_W^2/\kappa^{q2}_R$, Eqs. (9)+Table I | `gLZRu` $=-\tfrac16 t_W^2/\kappa^{q\,2}_R$ | **agree** | $(\tfrac12-\tfrac23)=-\tfrac16$. |
| $g^{Z_R,d}_L=(-\tfrac12+\tfrac13)t_W^2/\kappa^{q2}_R=-\tfrac16 t_W^2/\kappa^{q2}_R$, Eqs. (9)+Table I | `gLZRd` $=-\tfrac16 t_W^2/\kappa^{q\,2}_R$ | **agree** | |
| $g^{Z_R,u}_R=T^{3,u}_R-t_W^2Q^u/\kappa^{q2}_R=\tfrac12-\tfrac23 t_W^2/\kappa^{q2}_R$, Eqs. (10)+Table I | `gRZRu` $=\tfrac12-\tfrac23 t_W^2/\kappa^{q\,2}_R$ | **agree** | |
| $g^{Z_R,d}_R=-\tfrac12+\tfrac13 t_W^2/\kappa^{q2}_R$, Eqs. (10)+Table I | `gRZRd` $=-\tfrac12+\tfrac13 t_W^2/\kappa^{q\,2}_R$ | **agree** | |
| $g^{Z_R,e}_L=+\tfrac12 t_W^2/\kappa^{\ell2}_R$, $g^{Z_R,\nu}_L=+\tfrac12 t_W^2/\kappa^{\ell2}_R$, Eqs. (9)+Table I | `gLZRe`, `gLZRv` $=+\tfrac12 t_W^2/\kappa^{\ell\,2}_R$, declared but unused | **agree** (value) | The numbers are right. Only the term that uses them is missing. |
| $g^{Z_R,e}_R=-\tfrac12+t_W^2/\kappa^{\ell2}_R$, $g^{Z_R,N}_R=+\tfrac12$, Eqs. (10)+Table I | `gRZRe` $=-\tfrac12+t_W^2/\kappa^{\ell\,2}_R$, `gRZRn` $=+\tfrac12$, declared but unused | **agree** (value) | $N_R$ has $Q=0$, so only $T^{3,N}_R=+\tfrac12$ survives. |
| General charge rule behind Eqs. (9)–(10) | $g^f_{L,R}=T^f_{3R}-\frac{t_W^2}{\kappa_R^2}Y_f$ with $Y_f=Q_f-T^f_{3L}$ | **agree** | This form is algebraically identical to Eqs. (9) and (10). The reconstruction derived the rule correctly. |
| $\kappa^q_R,\kappa^\ell_R\in\mathds{R}$, independent normalizations of the quark and lepton sectors (Eq. (4) text, Eq. (5) text) | `kapRq`, `kapRl`, block `LRSMINPUTS`, both default 1.0, `InteractionOrder -> {NP,1}` | **agree** | The paper also uses $\kappa^{q,\ell}_R=1$ for the benchmark, and $\kappa^q_R=0.75$ in Fig. 3. |
| $g=\sqrt{4\pi\alpha_{\rm EM}(M_Z)}/\sin\theta_W$, the SM weak coupling | `gw` $=g_L$, plus $s_W$, $c_W$ from the SM sector | **agree** | The new sector adds no new gauge coupling. It only rescales $g_L$. |
| $M_{Z_R}=\sqrt{2\cos^2\theta_W/\cos2\theta_W}\,M_{W_R}\approx1.7\,M_{W_R}$, Eq. (18) | $M_{Z_R}=\sqrt2 M_{W_R}/\sqrt{1-t_W^2}\approx1.69\,M_{W_R}$ | **agree** | The two forms are identical, because $1-t_W^2=\cos2\theta_W/\cos^2\theta_W$. With $\sin^2\theta_W=0.23126$ both give $5074$ GeV, and the file holds $5070$ GeV. |
| $M_{W_R}=3$ TeV, $m_{N_1}=173.3$ GeV, $m_{N_2}=m_{N_3}=10^{12}$ GeV, Eq. (19) | `MWR` $=3000$, `mn1` $=173.3$, `mn2` $=$ `mn3` $=10^{12}$ | **agree** | |
| $\Gamma_{W_R}=84.3$ GeV, $\Gamma_{N_1}=2.12\times10^{-8}$ GeV, Table II | `WWR` $=84.3$, `Wn1` $=2.12\times10^{-8}$ | **agree** | |
| $\Gamma_{Z_R}=114$ GeV, Table II | `WZR` $=114$ | **agree** (number) | The number matches the paper. It does **not** match the Lagrangian the reconstruction describes; see D1. |
| Heavy neutrino PDG code 9900012, App. C | 9900012 / 9900014 / 9900016 | **agree** | |
| (nothing in the paper) | `M$InteractionOrderHierarchy` $=$ `{QCD,1},{QED,2},{NP,1}` | **extra-in-reconstruction** | This is bookkeeping for MG5, not physics. The paper does not discuss coupling orders. Harmless. |
| (nothing in the paper) | Proposed completion $\mathcal{L}_{Z_R\ell}$ written in §1 of the reconstruction | **extra-in-reconstruction** | The reconstruction marks this as its own observation, not as file content. See D3 for one coefficient to check. |

---

## 3. Disagreements

### D1 — The leptonic $Z_R$ current is missing. Severity: **substantive**

The paper's Eq. (8) `neucurrent` sums over *all* chiral fermions $f$, and the text after
Table I says that $\nu_L$ and $N_R$ couple to $Z_R$. Table II gives three leptonic $Z_R$
partial widths: $\ell^+\ell^-=7.64$ GeV, $\nu_e\nu_e=2.78$ GeV, $N_1N_1=10.2$ GeV. The
reconstruction reports that `LTotal` holds `LZRq` only, so $Z_R$ couples to quarks alone.

Two independent signs confirm the gap. First, the file declares `nZRl`, `gLZRe`, `gRZRe`,
`gLZRv` and `gRZRn` with exactly the values Eqs. (9)–(10) predict, and then uses none of
them. Dead parameters of precisely the right shape point to a deleted term. Second, the
widths do not add up: the quark modes in Table II give $82.3+11.3=93.6$ GeV, while the
stored width `WZR` is $114$ GeV. The difference, $20.6$ GeV, equals the sum of the three
leptonic modes, $7.64+2.78+10.2=20.6$ GeV.

The physics effect is large. Without this term $Z_R$ has no dilepton mode, no invisible
mode, and no $N_1N_1$ mode. The paper's $\ell^+\ell^-$ search channel of Eq. (3)
`eq:ppZRff`, $\ZR\to N_RN_R$, cannot be generated at all. The stored `WZR` is also too
large by 18%, which would distort any Breit-Wigner line shape.

*A human should check:* open the `.fr` file, confirm whether an `LZRl` block exists and
whether `LTotal` includes it, and confirm that `WZR` was computed with the leptonic modes
included.

### D2 — Index order of the lepton mixing matrices. Severity: **convention**

The paper writes $Y_{\ell m'}$ and $X_{\ell m}$, with the charged-lepton flavor first and
the neutrino state second. The reconstruction writes $(Y_N)_{ij}$ and $(X_N)_{ij}$ with
the neutrino index first and the charged lepton second. The two forms differ by a
transpose. With the default diagonal $Y$ and $X=0$ of Eq. (7), they agree numerically, so
no benchmark result changes.

*A human should check:* the index order in the `.fr` file, before anyone runs the model
with a non-diagonal $Y$ or a non-zero $X$.

### D3 — Majorana factor in the proposed $Z_R$–$N$ term. Severity: **cosmetic**

The reconstruction's own proposed completion carries a factor $\tfrac12$ on
$g^N_R\overline{N}\gamma^\mu P_R N$. The paper's Eq. (8) is written generically for a Dirac
field $f$ and carries no such factor. A $\tfrac12$ is the normal Majorana normalization,
so the two are probably consistent, but the paper does not state it.

*A human should check:* whether the Majorana $\tfrac12$ is needed to reproduce
$\Gamma(Z_R\to N_1N_1)=10.2$ GeV in Table II.

### D4 — $W_R$ carries $Q=+1$ but has no photon coupling. Severity: **convention**

The reconstruction reports `QuantumNumbers -> {Q -> 1}` on $W_R$ together with an abelian
`FS[WR,mu,nu]`, so no $\gamma W_R^+W_R^-$ vertex exists. This is a real inconsistency with
electromagnetic gauge invariance, but the paper accepts it on purpose: Sec. II C says the
non-Abelian $W_R$ and $Z_R$ interactions and their couplings to SM bosons are ill-defined,
and that pair production and vector boson scattering are not modeled correctly.

*A human should check:* that no planned process needs a photon or a $Z$ attached to a
$W_R$ line, because the model gives a wrong answer for those.

### D5 — Kinetic and mass terms have no counterpart in the paper. Severity: **cosmetic**

The paper never writes the $W_R$, $Z_R$ or $N$ kinetic and mass terms. I graded the four
reconstruction terms as **agree** on normalization grounds alone. They are the standard
Proca and Majorana forms, and they are consistent with Sec. II C.

*A human should check:* the sign and factor of each mass term directly in the `.fr` file,
because the paper gives no equation to compare against.

---

## 4. Overall assessment

The reconstruction tracks the paper closely on everything it does report. The $W_R$ quark
current of Eq. (4), the two-piece $W_R$ lepton current of Eq. (5), the $Z_R$ prefactor
$1/\sqrt{1-t_W^2/\kappa_R^2}$ of Eq. (8), all four quark chiral charges from Eqs. (9)–(10)
and Table I, the $M_{Z_R}$–$M_{W_R}$ relation of Eq. (18), the benchmark inputs of Eq. (19)
and every mass and width in Table II all match, including the derived general rule
$g^f_{L,R}=T^f_{3R}-(t_W^2/\kappa_R^2)Y_f$, which is Eqs. (9)–(10) in compact form. The one
important gap is the leptonic $Z_R$ current: the paper's Eq. (8) runs over every chiral
fermion and Table II lists $\ell^+\ell^-$, $\nu\nu$ and $N_1N_1$ modes, yet the
reconstruction finds the term absent from `LTotal`, with the five matching lepton
parameters left declared and unused and with the stored $\Gamma_{Z_R}=114$ GeV exceeding
the quark-only total of $93.6$ GeV by exactly the sum of the three missing leptonic
partial widths. The reconstruction itself flags this and gives the same reasoning, so the
document is self-consistent and careful rather than confused. The remaining differences
are a transposed mixing-matrix index order, a Majorana $\tfrac12$ in a term the
reconstruction only proposes, and normalization details the paper never wrote down. A
reviewer should therefore focus almost all attention on whether the implementation file
really omits the $Z_R$ lepton term, and on whether the stored $Z_R$ width was taken from
the paper rather than recomputed from the file.
