# Cross-check: `reconstruction.md` against the paper

**RUN-TAG:** XM-CROSS-EffLRSM__drop_cc

**Paper:** O. Mattelaer, M. Mitra, R. Ruiz, *Automated Neutrino Jet and Top Jet Predictions at
Next-to-Leading-Order with Parton Shower Matching in Effective Left-Right Symmetric Models*
(IPPP-16-102, CP3-16-51).

**Reconstruction:** an independent read-out of `sanitized.fr`, an add-on FeynRules module on top
of the Standard Model file.

---

## 1. Where the paper defines the model

The paper uses `revtex` labels, not printed numbers. I cite each equation by its LaTeX label and
by its line range in `paper.tex`.

| Reference | Label | `paper.tex` lines | Content |
| --- | --- | --- | --- |
| Sec. I | (unlabeled) | 175-177 | Gauge group $SU(3)_c\otimes SU(2)_L\otimes SU(2)_R\otimes U(1)_{B-L}$ |
| Sec. II, opening | — | 275-277 | Field content: $W_R^\pm$, $Z_R$ aligned with mass eigenstates; three heavy Majorana $N_i$ aligned with the RH chiral states |
| Sec. II | `chcurrent` | 280-283 | $\mathcal{L}_{W_R\text{-}q\text{-}q'}$, the RH charged quark current |
| Sec. II | (unlabeled, follows `chcurrent`) | 292-299 | $\mathcal{L}_{W_R\text{-}\ell\text{-}\nu/N}$, the RH charged lepton current |
| Sec. II | `eq:lrsmNuMixing` | 313-316 | $\vert Y_{eN}\vert=\vert Y_{\mu N_2}\vert=\vert Y_{\tau N_3}\vert=1$, all other $Y$ and all $X$ zero |
| Sec. II | Tbl. `tb:qNumbers` | 323-340 | $T_L^{3,f}$, $T_R^{3,f}$, $Q^f$ for $u_{L,R},d_{L,R},\nu_L,e_{L,R},N_R$ |
| Sec. II | `neucurrent` | 351-355 | $\mathcal{L}_{Z_R\text{-}f\text{-}f}$, the $Z_R$ neutral current |
| Sec. II | (two unlabeled) | 358-362 | $g_L^{Z_R,f}=(T_L^{3,f}-Q^f)\tan^2\theta_W/\kappa_R^{f\,2}$ and $g_R^{Z_R,f}=T_R^{3,f}-\tan^2\theta_W Q^f/\kappa_R^{f\,2}$ |
| Sec. II | 366-383 | 366-383 | LO $W_R,Z_R$ partial widths |
| Sec. II | `eq:massRelationship` | 412-415 | $M_{Z_R}=\sqrt{2\cos^2\theta_W/\cos 2\theta_W}\,M_{W_R}\approx1.7\,M_{W_R}$ |
| Sec. II | `eq:lrsmInputs` | 418-421 | $M_{W_R}=3$ TeV, $m_{N_1}=m_t=173.3$ GeV, $m_{N_2}=m_{N_3}=10^{12}$ GeV |
| Sec. II | Tbl. `tb:lrsmParam` | 392-409 | Masses and widths: $\Gamma_{W_R}=84.3$, $\Gamma_{Z_R}=114$, $\Gamma_{N_1}=2.12\times10^{-8}$ GeV |
| Sec. II C | `sec:modelLimits` | 454-465 | No LRSM scalars; non-abelian $W_R,Z_R$ couplings are ill-defined |
| Sec. III A | — | 480-483 | SM in Feynman gauge with Goldstones; Eqs. (`chcurrent`)-(`neucurrent`) in unitary gauge |
| App. C | `app:GenCuts` | 1101-1114 | Heavy neutrino PDG code `9900012` |

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| Gauge group $SU(3)_c\otimes SU(2)_L\otimes SU(2)_R\otimes U(1)_{B-L}$ (Sec. I, L175-177) | "no gauge group of its own"; only SM covariant derivatives; $W_R,Z_R$ ungauged with hand-written currents (§0) | **agree** | Sec. II C (L462) says the non-abelian $W_R$/$Z_R$ interactions are ill-defined in this effective model. The reconstruction reaches the same conclusion from the file. |
| $W_R^\pm$, $Z_R$ aligned with mass eigenstates (L275-277) | `WR` = `V[100]`, complex, $Q=+1$; `ZR` = `V[101]`, real (§2) | **agree** | No $W$-$W_R$ or $Z$-$Z_R$ mixing in either. |
| Three heavy Majorana $N_i$, aligned with RH chiral states (L276-277) | `NR` = `F[100]`, `SelfConjugate -> True`, `Index[Generation]`, 3 members (§2) | **agree** | |
| $W_R$ kinetic and mass term | $-\tfrac12 W_{R\mu\nu}^\dagger W_R^{\mu\nu}+M_{W_R}^2 W_{R\mu}^\dagger W_R^\mu$ (§1.1) | **extra-in-reconstruction** | The paper never writes the kinetic terms. The normalisation given is the standard one for a complex massive vector in unitary gauge, and is required for consistency. |
| $Z_R$ kinetic and mass term | $-\tfrac14 Z_{R\mu\nu}Z_R^{\mu\nu}+\tfrac12 M_{Z_R}^2 Z_{R\mu}Z_R^{\mu}$ (§1.2) | **extra-in-reconstruction** | Same remark. Real-vector normalisation, consistent with `SelfConjugate -> True`. |
| $N$ kinetic and Majorana mass term | $\tfrac{i}{2}\bar N\gamma^\mu\partial_\mu N-\tfrac12 M_{N_f}\bar N_f N_f$ (§1.3) | **extra-in-reconstruction** | Not written in the paper, but the paper calls $N$ Majorana (L276) and fixes $m_{N_i}$ in `eq:lrsmInputs`. The $\tfrac12$ factors are the correct Majorana normalisation. |
| $\mathcal{L}_{W_R\text{-}q\text{-}q'}=\frac{-\kappa_R^q g}{\sqrt2}\bar u_i V^{\rm CKM'}_{ij}W^+_{R\mu}\gamma^\mu P_R d_j+{\rm H.c.}$ (`chcurrent`) | $-\frac{\kappa_R^q g_L}{\sqrt2}\bar u_i (V^R_{\rm CKM})_{ij}\gamma^\mu P_R d_j W_{R\mu}+{\rm h.c.}$ (§1.4) | **agree** | Prefactor, $1/\sqrt2$, sign, $P_R$ on both fields, matrix position between $\bar u$ and $d$, and the index order $i$ (up) / $j$ (down) all match. |
| $V^{\rm CKM'}$ RH CKM, taken diagonal with unit entries (L286-287) | `VCKMR`, $3\times3$, `Unitary -> True`, value $=\mathbb{1}$ (§3.2) | **agree** | |
| $\mathcal{L}_{W_R\text{-}\ell\text{-}\nu/N}$, heavy piece $\overline{N_{m'}}Y_{\ell m'}W^+_{R\mu}\gamma^\mu P_R\ell^-$ (L292-299) | $-\frac{\kappa_R^\ell g_L}{\sqrt2}\bar N_i (Y_N)_{ij}\gamma^\mu P_R \ell_j W_{R\mu}+{\rm h.c.}$ (§1.5) | **agree** | No conjugation operator is needed here: $N$ is self-conjugate, so $\overline{N^c}=\bar N$, and the paper also writes the plain bilinear. |
| $\mathcal{L}_{W_R\text{-}\ell\text{-}\nu/N}$, light piece $\overline{\nu^{c}_{m}}X_{\ell m}W^+_{R\mu}\gamma^\mu P_R\ell^-$ (L296) | $-\frac{\kappa_R^\ell g_L}{\sqrt2}\bar\nu_i (X_N)_{ij}\gamma^\mu P_R \ell_j W_{R\mu}$ (§1.5), with **no** `CC` in the file (§0, §5.1) | **disagree** | The paper conjugates the light neutrino: $\overline{\nu^c}$, not $\bar\nu$. See D1. |
| Index order $X_{\ell m}$, $Y_{\ell m'}$ (lepton flavour first, neutrino second) | $(X_N)_{ij}$, $(Y_N)_{ij}$ with $i$ = neutrino, $j$ = lepton | **disagree** | The reconstruction's matrices are the transpose of the paper's. See D2. |
| $\vert Y_{eN}\vert=\vert Y_{\mu N_2}\vert=\vert Y_{\tau N_3}\vert=1$, others 0 (`eq:lrsmNuMixing`) | `YN` value $=\mathbb{1}$ (§3.2) | **agree** | Identity, so $N_i$ pairs one-to-one with $\ell_i$. |
| $\vert X_{\ell m}\vert=0$ (`eq:lrsmNuMixing`) | `XN` value $=0$ (§3.2) | **agree** | The light-neutrino piece is switched off at the default point. |
| $\kappa_R^{q},\kappa_R^{\ell}\in\mathbb{R}$, independent normalisations, same $\kappa$ in $W_R$ and $Z_R$ (L288-289, L309, L356) | `kapRq`, `kapRl`, two external reals in block `LRSMINPUTS`, shared between `LWRq`/`LZRq` and `LWRl`/`LZRl` (§3.1) | **agree** | |
| $\mathcal{L}_{Z_R\text{-}f\text{-}f}$ prefactor $\frac{-\kappa_R^f g}{\sqrt{1-(1/\kappa_R^f)^2\tan^2\theta_W}}$ (`neucurrent`) | $-\kappa_R^{q,\ell} g_L/n_{Z_R}^{q,\ell}$ with $n_{Z_R}=\sqrt{1-\tan^2\theta_W/\kappa_R^2}$ (§1.6, §1.7, §3.2) | **agree** | Algebraically identical, including the split into a quark and a lepton normalisation. |
| $Z_R$ chiral structure $\bar f\gamma^\mu(g_L P_L+g_R P_R)f$, flavour diagonal (`neucurrent`) | Separate `ProjM` and `ProjP` bilinears per field, no generation matrix (§1.6, §1.7) | **agree** | Hermitian by itself, so no `HC` is needed. The reconstruction states this. |
| $g_L^{Z_R,f}=(T_L^{3,f}-Q^f)\tan^2\theta_W/\kappa_R^{f\,2}$ with Tbl. `tb:qNumbers` | `gLZRu`$=-\tfrac16 t_W^2/\kappa_q^2$, `gLZRd`$=-\tfrac16 t_W^2/\kappa_q^2$, `gLZRe`$=+\tfrac12 t_W^2/\kappa_\ell^2$, `gLZRv`$=+\tfrac12 t_W^2/\kappa_\ell^2$ (§3.2) | **agree** | I checked all four by hand: $u_L$: $\tfrac12-\tfrac23=-\tfrac16$; $d_L$: $-\tfrac12+\tfrac13=-\tfrac16$; $e_L$: $-\tfrac12+1=+\tfrac12$; $\nu_L$: $\tfrac12-0=+\tfrac12$. |
| $g_R^{Z_R,f}=T_R^{3,f}-\tan^2\theta_W Q^f/\kappa_R^{f\,2}$ with Tbl. `tb:qNumbers` | `gRZRu`$=\tfrac12-\tfrac23 t_W^2/\kappa_q^2$, `gRZRd`$=-\tfrac12+\tfrac13 t_W^2/\kappa_q^2$, `gRZRe`$=-\tfrac12+t_W^2/\kappa_\ell^2$, `gRZRn`$=+\tfrac12$ (§3.2) | **agree** | All four match. $N_R$ has $T_R^3=+\tfrac12$ and $Q=0$, so `gRZRn` is a pure $+\tfrac12$ with no $t_W^2$ piece, exactly as the reconstruction gives. |
| $g_R^{Z_R,\nu}=0$ and $g_L^{Z_R,N}=0$ (implied by Tbl. `tb:qNumbers`) | No `ProjP` term for `vl`, no `ProjM` term for `NR` in `LZRl` (§1.7) | **agree** | The two absent terms are correctly absent, not accidentally dropped. |
| Reconstruction's restatement $g^f=T^{3R}_f-\tan^2\theta_W Y_f/\kappa_R^2$ (§3.2) | — | **agree** | Equivalent to the paper's two formulas, since $Q=T_L^3+Y$ gives $T_L^3-Q=-Y$, and $Y=Q$ for the RH singlets. Different bookkeeping, same numbers. |
| $M_{Z_R}\approx1.7\,M_{W_R}$ (`eq:massRelationship`) | $M_{Z_R}/M_{W_R}=5070/3000=1.69$ (§5.3) | **agree** | |
| $M_{W_R}=3$ TeV, $m_{N_1}=173.3$ GeV, $m_{N_2}=m_{N_3}=10^{12}$ GeV (`eq:lrsmInputs`) | `MWR`$=3000$, `mn1`$=173.3$, `mn2`$=$`mn3`$=1\times10^{12}$ (§2) | **agree** | |
| $\Gamma_{W_R}=84.3$, $\Gamma_{Z_R}=114$, $\Gamma_{N_1}=2.12\times10^{-8}$ GeV; $M_{Z_R}=5070$ GeV (Tbl. `tb:lrsmParam`) | `WWR`$=84.3$, `WZR`$=114$, `Wn1`$=2.12\times10^{-8}$, `MZR`$=5070$ (§2) | **agree** | Every number matches to the quoted precision. |
| $m_{N_2},m_{N_3}$ decoupled (L446) | `mn2`, `mn3` at $10^{12}$ GeV with zero width; only $N_1$ active (§2, §5.6) | **agree** | Consistent with $\Gamma_{W_R}$: the paper's total (L386-387) needs $\Gamma(W_R\to\mu N_2)=\Gamma(W_R\to\tau N_3)=0$ to give 84.3. |
| Heavy neutrino PDG `9900012` (App. C, L1105) | `n1` PDG `9900012` (§2) | **agree** | The other PDG codes (`9900024`, `9900023`, `9900014`, `9900016`) are not stated in the paper. |
| No LRSM scalar sector; $W_R,Z_R$ non-abelian and SM-boson couplings ill-defined (Sec. II C) | Abelian `FS`; no $W_RW_R\gamma$, $W_RW_RZ$ or quartic vertices; no Higgs sector (§5.2, §5.3) | **agree** | The reconstruction independently reproduces the paper's stated limitation. |
| SM sector "fully supported" (L465); SM in Feynman gauge with Goldstones (L480-481) | `LSM` inherited unchanged from the standard FeynRules SM file (§0) | **agree** | The standard FR SM file carries Goldstones in Feynman gauge, so the two statements are consistent. |
| Five massless quarks; `massless.rst` and `diagonalCKM.rst` restrictions (L287, L318-319) | Not mentioned | **missing-in-reconstruction** | Restriction cards are separate files. The reconstruction only had the `.fr` source, so this is out of its scope, not an error. |
| — | New interaction order `NP`, carried once by each $\kappa_R$ (§3.3) | **extra-in-reconstruction** | Implementation bookkeeping. The paper does not discuss coupling orders. |
| — | `nZRq`, `nZRl` turn imaginary for $\kappa_R<\tan\theta_W\approx0.55$ (§5.5) | **extra-in-reconstruction** | A true property of the paper's `neucurrent` prefactor as well. The paper uses $\kappa_R=0.75$ and $1.0$ (L581), both safe. |

### Independent numerical check of the $Z_R$ and $W_R$ charges

I put the reconstruction's `g` values into the paper's own width formulas (L366-383), with the
paper's SM inputs (L497-502: $\alpha^{-1}=127.940$, $\sin^2\theta_W=0.23126$, so
$g^2\simeq0.4247$ and $\tan^2\theta_W\simeq0.3008$). Hand arithmetic to three figures gives:

| channel | from the reconstruction's charges | paper Tbl. `tb:lrsmParam` |
| --- | --- | --- |
| $Z_R\to N_1N_1$ ($g_L=0$, $g_R=\tfrac12$) | 10.2 GeV | 10.2 GeV |
| $Z_R\to\ell^+\ell^-$ (3 flavours) | 7.63 GeV | 7.64 GeV |
| $Z_R\to\nu\bar\nu$ (3 flavours) | 2.77 GeV | 2.78 GeV |
| $Z_R\to t\bar t$ | 11.2 GeV | 11.3 GeV |
| $Z_R\to q\bar q$ (5 light flavours) | 82.2 GeV | 82.3 GeV |
| $Z_R\to$ total | 114 GeV | 114 GeV |
| $W_R\to\ell N_1$ | 8.41 GeV | 8.41 GeV |
| $W_R\to t\bar b$ | 25.2 GeV | 25.2 GeV |
| $W_R\to q\bar q'$ (2 channels) | 50.7 GeV | 50.7 GeV |
| $W_R\to$ total | 84.3 GeV | 84.3 GeV |

Every entry in the reconstruction's §3.2 charge table, its $n_{Z_R}$ normalisation, and its
$W_R$ prefactor are therefore confirmed against the paper's own analytic results. In
particular `gRZRn`$=+\tfrac12$ with no left-handed partner reproduces $\Gamma(Z_R\to N_1N_1)$
exactly. The numbers above are hand calculations; a human should re-run them with a calculator
if the exact digits matter.

---

## 3. Disagreements

### D1. The charge conjugation on the light neutrino is absent — **substantive**

The paper writes the light-neutrino piece of the $W_R$ lepton current as
$\overline{\nu^{c}_{m}}X_{\ell m}\,W^+_{R\mu}\gamma^\mu P_R\,\ell^-$ (L296). The file carries
`vlbar.XN.Ga[mu].ProjP.l`, i.e. $\bar\nu$ with no conjugation, and the reconstruction records
that the file holds **no** `CC` operator anywhere (§0, §5.1).

This is not notation. In the SM FeynRules file `vl` is a not-self-conjugate field whose physical
content is the left-handed $\nu_L$ only. The paper's operator projects
$P_R\nu^c=(\nu_L)^c$, which exists, so the vertex is the lepton-number-violating
$W_R$-$\nu$-$\ell$ coupling that the light-heavy mixing $X$ is meant to parametrise. The file's
operator instead projects $P_R\nu=\nu_R$, a state the model does not contain, so the generated
vertex carries the opposite lepton-number flow and the wrong particle/antiparticle orientation
for the light neutrino.

The heavy piece is unaffected: $N$ is self-conjugate, $\overline{N^c}=\bar N$, and the paper
writes the plain bilinear too.

**What a human should check:** open the model file, confirm whether the light-neutrino bilinear
in `LWRl` should read `CC[vl]bar.XN.Ga[mu].ProjP.l` (or the equivalent `vlbar.CC[...]` form) as
the paper's $\overline{\nu^c_m}$ demands, and if so decide whether the vertex was simply lost or
was deliberately removed.

**Mitigating fact, not an excuse:** `XN` is zero at the default point (`eq:lrsmNuMixing`), so no
numerical result in the paper depends on this term. The paper states at L318-319 that the mixing
assumptions are modifiable by not loading `massless.rst` and `diagonalCKM.rst`, so any user who
turns on light-heavy mixing would hit the defect.

### D2. The mixing matrices are transposed — **convention**

The paper indexes $X_{\ell m}$ and $Y_{\ell m'}$ with the lepton flavour first and the neutrino
mass eigenstate second. The reconstruction contracts them as $\bar N_i (Y_N)_{ij}\ell_j$ and
$\bar\nu_i (X_N)_{ij}\ell_j$, i.e. neutrino first. The two forms differ by a transpose.

**What a human should check:** whether `YN` and `XN` in the file are stored as $Y$ or $Y^{T}$
relative to the paper. It makes no difference at the default point, where $Y_N=\mathbb{1}$ and
$X_N=0$, but it matters as soon as a user supplies a non-symmetric matrix.

### D3. The reconstruction calls $N_R$ a full singlet — **cosmetic**

Section 0 of the reconstruction says $N_R$ is an
$SU(3)_c\times SU(2)_L\times U(1)_Y$ singlet. That is correct and matches the paper (L179). But
the paper also assigns $N_R$ a right-handed isospin $T_R^{3,N}=+\tfrac12$ and a $B-L$ charge
(Tbl. `tb:qNumbers`, L348), and that charge is what produces `gRZRn`$=+\tfrac12$. A reader
skimming the reconstruction could conclude $N_R$ carries no quantum numbers at all.

**What a human should check:** nothing in the file; only that the write-up says clearly that
$N_R$ keeps its $SU(2)_R$ isospin in the $Z_R$ current even though $SU(2)_R$ is not gauged here.

### D4. Missing terms in the paper that the reconstruction supplies — **cosmetic**

The kinetic and mass terms for $W_R$, $Z_R$ and $N$ (§1.1-§1.3) never appear in the paper, which
writes only the three interaction Lagrangians. The reconstruction's normalisations are the
standard ones and are consistent with the paper's $M_{W_R}$, $M_{Z_R}$, $m_{N_i}$ and with
`SelfConjugate` assignments, so there is nothing to reconcile.

**What a human should check:** that the $-\tfrac12$ complex-vector normalisation on `LWRkin` is
really what the file carries, since a $-\tfrac14$ there would halve every $W_R$ propagator
residue and break the width table.

---

## 4. Overall assessment

The reconstruction matches the paper closely across the whole model. Field content, the two
$W_R$ charged currents, the $Z_R$ neutral current with its $\kappa_R$-dependent normalisation,
all eight chiral $Z_R$ charges, the two external knobs $\kappa_R^{q}$ and $\kappa_R^{\ell}$, the
benchmark masses and all four widths line up with Sec. II of the paper. I confirmed the charge
assignments a second way: feeding the reconstruction's `g` values into the paper's own width
formulas reproduces every entry of Table `tb:lrsmParam` to the quoted precision, including
$\Gamma(Z_R\to N_1N_1)=10.2$ GeV, which tests `gRZRn` and the Majorana treatment together. The
reconstruction's description of what the model leaves out — no scalar sector, abelian field
strengths, no $W$-$W_R$ mixing — reproduces the paper's own list of limitations in Sec. II C.
One clear physics difference remains: the paper conjugates the light neutrino in the $W_R$
lepton current, $\overline{\nu^{c}_{m}}X_{\ell m}$, and the file does not, a point the
reconstruction itself flags as an open question in its §5.1. That term is numerically dormant
because $X=0$ at the default point, so it cannot change any published number, but it is a real
structural difference in an operator the paper tells users they may switch on. The transposed
index order on $X$ and $Y$ is a second, smaller item of the same kind. I give no pass/fail
verdict; the decision belongs to the human reviewer.
