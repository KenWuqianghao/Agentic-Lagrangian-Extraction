# Cross-check: `reconstruction.md` against the paper

Paper: *Probing the minimal U(1)_X model at future electron-positron colliders via
fermion pair-production channels* — Das, Dev, Hosotani, Mandal (preprint OU-HET-1085).

---

## 0. Where the paper defines the model

All model content is in Sec. II ("The $U(1)_X$ Model"). Equation numbers below follow
the order of the `equation`/`align`/`eqnarray` environments in `paper.tex`. I also give
the LaTeX label, so the reference stays clear if the printed numbers differ.

| Paper item | Location | Content |
|---|---|---|
| Table I (`tab1`) | Sec. II | Gauge group, particle content, $SU(3)_C$, $SU(2)_L$, $Y$ and $U(1)_X$ charges of $q_L, u_R, d_R, \ell_L, e_R, N_R, H, \Phi$ |
| Eq. (1) (`LYk`) | Sec. II | Full Yukawa Lagrangian: $Y_u$, $Y_d$, $Y_e$, $Y_\nu$ and the Majorana term $Y_N \Phi \overline{N_R^c} N_R$ |
| Eq. (2) | Sec. II | Renormalizable scalar potential $V(H,\Phi)$ with $\lambda$, $\lambda_\Phi$, $\lambda'$ |
| Eq. (3) | Sec. II | Vacuum values $\langle H\rangle$ and $\langle\Phi\rangle=(v_\Phi+\phi)/\sqrt2$ |
| Eq. (4) | Sec. II | $M_{Z'} = g'\sqrt{4v_\Phi^2 + \tfrac14 x_H^2 v^2} \simeq 2g'v_\Phi$ |
| Text after Eq. (4) | Sec. II | $m_{N_\alpha} = Y_N^\alpha v_\Phi/\sqrt2$ and $m_D^{\alpha\beta} = Y_\nu^{\alpha\beta} v/\sqrt2$ |
| Eq. (5) (`num`) | Sec. II | Seesaw mass matrix $\mathcal{M}_\nu$ and $m_\nu \simeq -m_D m_N^{-1} m_D^T$ |
| Eq. (6) (`Lag1`) | Sec. II A | $Z'$ current of the SM quarks and leptons, with $-g'$ in front |
| Eqs. (7)–(9) (`2f`, `2v`, `2N`) | Sec. II A | Partial widths $Z'\to f\bar f$, $\nu\bar\nu$, $NN$ |
| Table II (`tab2`) | Sec. II B | Numeric $U(1)_X$ charges for $x_H=-2\ldots 2$ with $x_\Phi=1$ |
| Table III (`tab3`), text | Sec. II B | Benchmark $M_{Z'}=7.5$ TeV, $g'=0.4$ for $x_H=2$ |

Important reading note. The paper calls the SM doublet $H$ and the new singlet $\Phi$.
The reconstruction calls the SM doublet $\Phi$ and the new singlet $\Phi_X$. The table
below uses the paper's names on the left and the reconstruction's names on the right.

A second reading note. The paper's $H$ is not the doublet of the standard FeynRules SM
file. Eq. (1) writes $\overline{q_L}H u_R$ and $\overline{q_L}\tilde H d_R$, and Eq. (3)
puts the vacuum value in the **upper** component. So the paper's $H$ plays the role of
$\tilde\Phi = \epsilon \Phi^*$ in the FeynRules convention. Every doublet comparison
below uses this map.

---

## 1. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Gauge group $SU(3)_C\otimes SU(2)_L\otimes U(1)_Y\otimes U(1)_X$ (Sec. II, Table I) | Add-on module on an SM base; one new abelian boson `Zp` | **agree** | The module declares no group. The one new gauge boson is the $U(1)_X$ boson. |
| $Z'$ kinetic term (implied by Eq. (4); paper never writes it) | `LZpKin`: $-\frac14 Z'_{\mu\nu}Z'^{\mu\nu}$, abelian field strength | **agree** | No kinetic mixing $Z'_{\mu\nu}B^{\mu\nu}$ on either side. |
| $M_{Z'} = g'\sqrt{4v_\Phi^2+\frac14 x_H^2 v^2}$, Eq. (4) | `MZp` $= g_X\sqrt{x_{S_c}^2 v_\Phi^2 + x_{H_d}^2 v^2}$, with $x_{S_c}=2x_\Phi$, $x_{H_d}=x_H/2$ | **agree** | Identical after substitution. The reconstruction keeps $x_\Phi$ general; the paper fixes $x_\Phi=1$. Numbers: $g_X=0.4$, $v_\Phi=9375$ GeV give $7501$ GeV, which is the paper's $7.5$ TeV benchmark. |
| $x_{q_L}=\frac16 x_H+\frac13 x_\Phi$ (Table I) | `xqL` $=x_H/6+x_\Phi/3$, value $2/3$ | **agree** | Formula matches Table I. The value $2/3$ also matches. Table II of the paper prints $1/3$ in the $x_H=2$ row, which is a typo in the paper (see disagreement D6). |
| $x_{u_R}=\frac23 x_H+\frac13 x_\Phi$ (Table I) | `xuR`, value $5/3$ | **agree** | Matches Table I and Table II. |
| $x_{d_R}=-\frac13 x_H+\frac13 x_\Phi$ (Table I) | `xdR`, value $-1/3$ | **agree** | Matches Table I and Table II. |
| $x_{\ell_L}=-\frac12 x_H-x_\Phi$ (Table I) | `xlL`, value $-2$ | **agree** | Matches Table I and Table II. |
| $x_{e_R}=-x_H-x_\Phi$ (Table I) | `xeR`, value $-3$ | **agree** | Matches Table I and Table II. |
| $x_{N_R}=-x_\Phi$ (Table I) | `xnR` $=-x_\Phi$, value $-1$ | **agree** | Matches. Chirality also matches: right-chiral singlet. |
| $x_H^{(\rm doublet)}=-\frac{x_H}{2}$ (Table I) | `xHd` $=+x_H/2$, value $+1$ | **disagree** (convention) | The magnitude agrees. The sign is opposite because the two texts name opposite doublets. See D1. |
| $x_\Phi^{(\rm singlet)}=2x_\Phi$ (Table I) | `xSc` $=2x_\Phi$, value $2$ | **agree** | Matches. |
| $SU(3)$, $SU(2)$, $Y$ of $N_R$, $\Phi$ (Table I) | Both are full singlets, $Y=0$ | **agree** | Reconstruction: `NX` is $F[100]$, `HX` is $S[100]$, both colour and isospin singlets. |
| $\mathcal{L}^q$, $Z'$ current of SM fermions, Eq. (6) | `LZpF`: $-g_X Z'_\mu \sum_f x_f \bar f\gamma^\mu f$ | **agree** | Same overall sign $-g'$. Same chiral split: each chirality block carries its own charge. The reconstruction writes the current by hand, not through `DC`, which is equivalent. |
| $\nu_L$ part of the $\ell_L$ current, Eq. (8) (`2v`) | $x_{\ell_L}\bar L_L\gamma^\mu L_L$ expanded by `FlavorExpand -> {SU2D}` | **agree** | The doublet expansion gives $\bar\nu_L\gamma^\mu\nu_L + \bar e_L\gamma^\mu e_L$ with one common charge, as Eq. (6) and Eq. (8) require. |
| $Z'$–$N_R$ coupling, implied by Eq. (9) (`2N`) with $g_R^N[g',x_\Phi]$ | $x_{n_R}\bar N_R\gamma^\mu N_R = \bar N_X\gamma^\mu P_R N_X$ | **agree** | Right-chiral projector, charge $-x_\Phi$, no left-chiral piece. This is the correct content of $g_R^N$. |
| Flavour structure of the $Z'$ current (Table I: charges are generation independent) | Flavour diagonal; CKM unitarity rules $V_{ab}V^*_{ac}\to\delta_{bc}$ applied | **agree** | No flavour-changing $Z'$ vertex survives, which the paper's family-universal charges demand. |
| $Z'$ total width, Eqs. (7)+(8), Fig. 1 | $W_{Z'}=1353$ GeV | **agree** | I re-derived it. With $x_H=2$, $x_\Phi=1$, $g'=0.4$, $M_{Z'}=7500$ GeV and $Z'\to NN$ closed, Eqs. (7)+(8) give $\frac{M_{Z'}}{24\pi}g'^2\times 85 = 1353$ GeV. This also confirms $x_{q_L}=2/3$. |
| Assumption $m_N > M_{Z'}$ (text after Eq. (9)) | $M_{N_i}=8000$ GeV, $M_{Z'}=7501$ GeV | **agree** | $8.0$ TeV $>7.5$ TeV, so $Z'\to NN$ is closed, as the paper assumes. |
| RHN kinetic and mass term (implied by Table I and Eq. (1)) | `LNXKin`: $\frac{i}{2}\bar N_X\gamma^\mu\partial_\mu N_X-\frac12\bar N_X (m_N)_{ij}N_X$ | **agree** | Majorana normalisation $\frac12$ is correct. The gauge part of the derivative sits in `LZpF`, so no term is lost and none is double counted. |
| $-Y_N^\alpha \Phi\,\overline{N_R^{\alpha c}}N_R^\alpha$, Eq. (1); $m_{N_\alpha}=Y_N^\alpha v_\Phi/\sqrt2$ | `LNYuk`: $-\frac{1}{2\sqrt2}H_X\bar N_X (y_N)_{ij}N_X$ with $(y_N)_{ij}=\sqrt2 M_{N_i}\delta_{ij}/v_\Phi$ | **agree** | Expanding Eq. (1) with $\Phi=(v_\Phi+\phi)/\sqrt2$ gives exactly $-\frac12 (m_N/v_\Phi)\phi\,\bar N_X N_X$. The inversion $y_N=\sqrt2 m_N/v_\Phi$ is the paper's relation. Value $1.207$ is correct. |
| $-Y_\nu^{\alpha\beta}\overline{\ell_L^\alpha}H N_R^\beta$, Eq. (1); $m_D=Y_\nu v/\sqrt2$ | `LNuYuk`: $-(y_\nu)_{ij}\overline{L_L^i}_a\epsilon_{ab}\Phi^*_b P_R N_X^j+{\rm h.c.}$ | **agree** | Same physics. The paper's $H$ has its vacuum value in the upper component, so it equals $\tilde\Phi=\epsilon\Phi^*$ of the FeynRules base. Both give $m_D=y_\nu v/\sqrt2$. Chirality ($L_L$ with $P_R N$) and the h.c. partner both match. |
| $-Y_u\overline{q_L}Hu_R-Y_d\overline{q_L}\tilde H d_R-Y_e\overline{\ell_L}\tilde H e_R$, Eq. (1) | Taken unchanged from the SM base file (`LSM`) | **agree** | The add-on does not touch the SM Yukawa sector, which is what the paper needs. The doublet naming differs, as noted above. |
| Seesaw matrix $\mathcal{M}_\nu$, Eq. (5) | No explicit light-neutrino mass matrix; $m_\nu$ arises from $m_D$ plus $m_N$ | **agree** | Eq. (5) is a derived result, not a Lagrangian term. The two Lagrangian inputs $m_D$ and $m_N$ are both present. The quoted $m_\nu\simeq 4\times10^{-3}$ eV follows from $y_\nu=10^{-6}$ and $M_N=8$ TeV. |
| $\lambda_\Phi(\Phi^\dagger\Phi)^2$ and $m_\Phi^2(\Phi^\dagger\Phi)$, Eq. (2) | `LPotX`: $-\lambda_\Phi v_\Phi H_X^3-\frac{\lambda_\Phi}{4}H_X^4$, plus $-\frac12 M_{H_X}^2 H_X^2$ in `LHXKin` | **agree** | The reconstruction's shifted form $\lambda_\Phi(|\Phi_X|^2-v_\Phi^2/2)^2$ expands to exactly these cubic and quartic terms. The paper writes $+m_\Phi^2(\Phi^\dagger\Phi)$ with a positive sign, which alone has no broken minimum; see D5. |
| $M_\phi^2 = 2\lambda_\Phi v_\Phi^2$ (implied by Eq. (2) and Eq. (3)) | `MHX` $=1/\sqrt{2\lambda_\Phi v_\Phi^2}$, value $2.4\times10^{-4}\,{\rm GeV}^{-1}$ | **disagree** (substantive) | The implementation stores an inverse mass. The reconstruction flags this itself and gives the correct $4193$ GeV. See D2. |
| $\lambda'(H^\dagger H)(\Phi^\dagger\Phi)$ quartic part, Eq. (2) | $-\frac{\lambda'}{2}H_X^2\,\Phi^\dagger_a\Phi_a$ | **agree** | Correct coefficient: $\lambda'|\Phi_X|^2|\Phi|^2$ gives $\frac{\lambda'}{2}H_X^2\Phi^\dagger\Phi$ in $V$. |
| $\lambda'(H^\dagger H)(\Phi^\dagger\Phi)$ trilinear part $-\lambda' v_\Phi H_X\Phi^\dagger\Phi$, Eq. (2) | absent | **missing-in-reconstruction** | The same operator also gives a trilinear and a constant shift $-\frac{\lambda'}{2}v_\Phi^2\Phi^\dagger\Phi$. Both are absent. See D3. |
| $h$–$\phi$ scalar mixing from $\lambda'$, Eq. (2) and Sec. II text | absent | **missing-in-reconstruction** | The paper says the mixing is negligible "in the limit of small $\lambda^\prime$", so the omission follows the paper's own approximation, but it is not the full potential. |
| $\langle\Phi\rangle=(v_\Phi+\phi)/\sqrt2$, Eq. (3) | $\Phi_X=(v_\Phi+H_X)/\sqrt2$, `vX` $=9375$ GeV | **agree** | Same normalisation. $v_\Phi\gg v$ holds ($9375 \gg 246$), as the paper requires. |
| $|D_\mu\Phi|^2$ $Z'$ part (implied by Eq. (4)) | `LZpHX`: $g_X^2 x_{S_c}^2(v_\Phi H_X+\frac12 H_X^2)Z'_\mu Z'^\mu$ | **agree** | I expanded $|D_\mu\Phi_X|^2$. The constant piece is exactly the $x_{S_c}^2 v_\Phi^2$ part of $M_{Z'}^2$, which `LZpKin` already carries. So the $Z'$ mass is counted once, as the reconstruction states. |
| $|D_\mu H|^2$ $Z'$ part: source of the $\frac14 x_H^2 v^2$ piece of Eq. (4) | Only the $x_{H_d}^2 v^2$ number inside `MZp`; no $Z$–$Z'$ mass mixing, no $Z'Z'h$ or $ZZ'h$ vertex | **missing-in-reconstruction** | The electroweak part of $M_{Z'}$ is inserted by hand without the vertices that produce it. See D4. |
| $Z'$ as a mass eigenstate in the propagators, Eqs. (`prop-1`), (`prop-2`) | $Z'$ treated as a mass eigenstate; no $Z$–$Z'$ rotation | **agree** | The paper uses pure $Z'$ propagators everywhere, so this matches how the paper uses the model. |
| Goldstone of $\Phi$ (implied by Eq. (3), gauge choice not fixed) | Not declared; eaten by $Z'$, that is, unitary gauge for the $Z'$ sector | **missing-in-reconstruction** | Harmless at tree level. It blocks a Feynman-gauge or loop calculation in the $Z'$ sector. See D7. |
| Benchmark $g'=0.4$, $M_{Z'}=7.5$ TeV, $x_H=2$, $x_\Phi=1$ (Sec. II B, Table III) | `gX` $=0.4$, `xH` $=2.0$, `xPhi` $=1.0$, `vX` $=9375$ GeV | **agree** | All four defaults reproduce the paper's strongest benchmark point exactly. |
| — | `MHX`, `WHX` $=0.1$ GeV, `WNX` $=10^{-10}$ GeV, PDG codes 9900032 / 9900025 / 9900012-14-16 | **extra-in-reconstruction** | Implementation data with no paper counterpart. Widths of $H_X$ and $N_i$ are not predicted by the paper. |
| — | `NR` as an `Unphysical -> True` shorthand $N_R=P_R N_X$, `F[110]`, `LeptonNumber -> 1` | **extra-in-reconstruction** | A FeynRules device, not physics. It is the correct way to write a Majorana field's right-chiral part. |
| — | Sign of the $Z'$ term in $D_\mu$: $+ig_X x_f Z'_\mu$, opposite to the SM terms | **extra-in-reconstruction** (convention) | See D8. |

---

## 2. Disagreements, with severity

**D1 — Sign of the $U(1)_X$ charge of the SM Higgs doublet. Severity: convention.**
Table I gives $-x_H/2$ for the doublet it calls $H$; the reconstruction gives `xHd` $=+x_H/2$.
The two agree once you note that the paper's $H$ carries its vacuum value in the upper
component (Eq. (3)) and couples as $\overline{q_L}Hu_R$ (Eq. (1)), so it is the conjugate
of the FeynRules doublet $\Phi$. A human should confirm that the implementation's
$\Phi$ is the standard $Y=+1/2$ doublet with a lower-component vacuum value, and that
`xHd` is therefore the charge of $\Phi$, not of the paper's $H$.

**D2 — `MHX` is an inverse mass. Severity: substantive.**
The reconstruction reports `MHX -> 1/Sqrt[2 lamX vX^2]`, which gives
$2.4\times10^{-4}\ {\rm GeV}^{-1}$ instead of the $\sqrt{2\lambda_\Phi v_\Phi^2}\simeq 4193$ GeV
that Eq. (2) with Eq. (3) requires. A human should open the implementation file, confirm
that the reciprocal is really there, and correct it, because every $H_X$ propagator,
width and decay chain uses this number.

**D3 — The portal trilinear $-\lambda' v_\Phi H_X\Phi^\dagger\Phi$ is absent. Severity: substantive.**
Eq. (2) contains $\lambda'(H^\dagger H)(\Phi^\dagger\Phi)$, which after Eq. (3) gives a
trilinear term and a constant shift of the SM Higgs mass parameter, not only the
$H_X^2\Phi^\dagger\Phi$ quartic that the file keeps. A human should decide whether the
omission is the paper's own small-$\lambda'$ approximation, which the paper states in
Sec. II, or an accidental truncation, and should check whether any $h$–$H_X$ mixing
matters for the intended study.

**D4 — No $Z$–$Z'$ mixing and no $Z'Z'h$ or $ZZ'h$ vertices. Severity: substantive, small in size.**
The $\frac14 x_H^2 v^2$ term in Eq. (4) comes from $|D_\mu H|^2$ with the doublet charged
under $U(1)_X$; the same term must also produce $Z$–$Z'$ mass mixing and $Z'$-Higgs
vertices, and the reconstruction says these are not in the file. A human should check
whether the intended study only uses the pure $Z'$ propagators of Eqs. (`prop-1`) and
(`prop-2`), in which case the effect is suppressed by $v^2/v_\Phi^2\sim10^{-3}$ and is
consistent with the paper's own use of the model.

**D5 — Sign of $m_\Phi^2$ in the paper's potential. Severity: cosmetic (paper side).**
Eq. (2) writes $+m_\Phi^2(\Phi^\dagger\Phi)+\lambda_\Phi(\Phi^\dagger\Phi)^2$, which has no
symmetry-breaking minimum as printed, yet Eq. (3) gives $\Phi$ a vacuum value. A human
should read the paper's $m_\Phi^2$ as negative, or read Eq. (2) as already shifted; the
reconstruction's form $\lambda_\Phi(|\Phi_X|^2-v_\Phi^2/2)^2$ is the consistent rewriting
and needs no change.

**D6 — $x_{q_L}$ at $x_H=2$: $2/3$ against Table II's $1/3$. Severity: cosmetic (paper side).**
The reconstruction gives $2/3$, which is what Table I's formula $\frac16 x_H+\frac13 x_\Phi$
gives; Table II of the paper prints $1/3$ in the $x_H=2$ row, and every other entry in
that row follows the formula. The reconstruction's $W_{Z'}=1353$ GeV reproduces the paper's
own width formula only with $2/3$, so a human can treat Table II's $1/3$ as a paper typo,
but should still confirm it against the published version.

**D7 — The $Z'$ Goldstone is not declared. Severity: convention.**
The implementation keeps only the real part $H_X$ of $\Phi_X$, so the $Z'$ sector is in
unitary gauge, while `feynmangaugerules` still removes the SM Goldstones when
`FeynmanGauge` is `False`. A human should confirm that only tree-level $Z'$ results are
wanted, because a Feynman-gauge or loop calculation in the $Z'$ sector needs the
Goldstone field.

**D8 — Sign of the $Z'$ term in the covariant derivative. Severity: cosmetic.**
The reconstruction writes $D_\mu \supset +ig_X x_f Z'_\mu$, opposite in sign to the SM
gauge terms, so that $\bar f i\gamma^\mu D_\mu f$ reproduces the $-g'$ of Eq. (6). A human
can ignore this, because $Z'$ has no tree-level cross terms with the SM gauge bosons and
the sign is removed by $Z'\to -Z'$; but it should be applied to every $Z'$ vertex.

**D9 — The reconstruction's own claim that `LNuYuk` breaks $U(1)_X$ is wrong. Severity: substantive (commentary, not Lagrangian).**
Section 5 of the reconstruction states that the Dirac Yukawa is $U(1)_X$ invariant only
for $x_H=0$. That conclusion rests on a sign slip: the text says the doublet enters with
charge $-x_{H_d}$ but then adds $+x_{H_d}$ in the sum. The correct sum is
$-x_{\ell_L}-x_{H_d}+x_{n_R}=(x_H/2+x_\Phi)-x_H/2-x_\Phi=0$, so the term is invariant for
every $x_H$, which is what Table I and Eq. (1) of the paper require. A human should
discard this warning, and should not "repair" the Lagrangian term on the strength of it.

---

## 3. Overall assessment

The reconstruction captures the model of Sec. II with good fidelity. Every fermion and
scalar $U(1)_X$ charge follows Table I, the $Z'$ current matches Eq. (6) in sign,
chirality structure and family universality, the Majorana and Dirac Yukawa terms match
Eq. (1) including the $\sqrt2$ factors that define $m_N$ and $m_D$, and $M_{Z'}$ matches
Eq. (4) in a form that is more general than the paper's because it keeps $x_\Phi$ free.
Two independent numeric checks support this: the default parameters reproduce the paper's
benchmark point ($M_{Z'}=7.5$ TeV, $g'=0.4$, $x_H=2$) exactly, and the quoted $Z'$ width of
1353 GeV is what Eqs. (7) and (8) give with $Z'\to NN$ closed, which is the paper's own
assumption because $M_N=8$ TeV exceeds $M_{Z'}$. Three items need human attention. The
`MHX` definition stores an inverse mass and contradicts the potential of Eq. (2); the
reconstruction identifies this clearly and gives the correct value, so the finding is the
document's, not mine, but it remains the largest single defect in the implementation. The
portal trilinear and the $Z'$ couplings of the Higgs doublet are absent, both of which are
small or approximated away in the paper's own treatment but are still not the full content
of Eq. (2) and Eq. (4). Finally, the reconstruction's own closing warning about $U(1)_X$
invariance of the Dirac Yukawa is a sign error and should not be acted on; the two
disagreements in the charge tables (the Higgs doublet sign, and $x_{q_L}$ at $x_H=2$) both
resolve in the reconstruction's favour once the doublet convention and the paper's Table II
typo are taken into account.
