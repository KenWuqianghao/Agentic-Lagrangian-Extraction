# Cross-check: `reconstruction.md` against `paper.tex`

RUN-TAG: XM-CROSS-GeneralU1__drop_term

**Paper.** "Probing the minimal $U(1)_X$ model at future electron-positron colliders
via fermion pair-production channels", Das, Dev, Hosotani, Mandal (OU-HET-1085).

**Reconstruction.** An independent read-back of a FeynRules file (`sanitized.fr`).
The implementation file was not available for this check.

---

## 1. Where the paper defines the model

The full model definition sits in Sec. II ("The $U(1)_X$ Model"), lines 89-215
of `paper.tex`. The relevant items are:

| Item | Location in the paper |
| --- | --- |
| Gauge group $SU(3)_C \otimes SU(2)_L \otimes U(1)_Y \otimes U(1)_X$ | Sec. II, first paragraph after Table I |
| Field content and all $U(1)_Y$, $U(1)_X$ charges | Table I (`tab1`) |
| Yukawa Lagrangian (5 terms) | Eq. (`LYk`) |
| Definition $\tilde{H} \equiv i\tau^2 H^*$ | Text below Eq. (`LYk`) |
| Scalar potential $V$ | Unnumbered `align` in Sec. II ("The renormalizable Higgs potential...") |
| Vacuum expectation values of $H$ and $\Phi$ | Unnumbered `align` below $V$ |
| $Z'$ mass $M_{Z'} = g'\sqrt{4v_\Phi^2 + \tfrac14 x_H^2 v^2}$ | Unnumbered `bea` in Sec. II |
| Dirac and Majorana mass relations $m_D$, $m_{N_\alpha}$ | Text below the $M_{Z'}$ equation |
| Seesaw mass matrix | Eq. (`num`) |
| $Z'$ current to SM quarks and leptons | Eq. (`Lag1`), Sec. II A |
| $Z'$ partial widths (charged fermions, $\nu$, RHN) | Eqs. (`2f`), (`2v`), (`2N`) |
| Charge values for benchmark $x_H$ | Table II (`tab2`) |
| Benchmarks $M_{Z'} = 7.5$ TeV, $g' = 0.4$, $x_\Phi = 1$ | Sec. II B, text near Table III |

The paper does not print the gauge kinetic terms, the covariant derivatives, or
the scalar kinetic terms. Those pieces follow from the gauge group and from
Table I. This check treats them as "implied by the paper" and marks them so.

Symbol map used below: paper $g' \leftrightarrow$ file `gX`; paper $\phi$ (the
real part of $\Phi$) $\leftrightarrow$ file `HX`; paper $N_R \leftrightarrow$
file `NX` / `NR`.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| Gauge group $SU(3)_C\otimes SU(2)_L\otimes U(1)_Y\otimes U(1)_X$ (Sec. II) | Sec. 0, same group, gauge field $Z'$, coupling $g_X$ | **agree** | One extra abelian factor. Same content. |
| $q_L$: $\tfrac16 x_H + \tfrac13 x_\Phi$ (Table I) | `xqL` $= x_H/6 + x_\Phi/3$ | **agree** | Also matches Table II for every benchmark $x_H$. |
| $u_R$: $\tfrac23 x_H + \tfrac13 x_\Phi$ (Table I) | `xuR` $= 2x_H/3 + x_\Phi/3$ | **agree** | |
| $d_R$: $-\tfrac13 x_H + \tfrac13 x_\Phi$ (Table I) | `xdR` $= -x_H/3 + x_\Phi/3$ | **agree** | |
| $\ell_L$: $-\tfrac12 x_H - x_\Phi$ (Table I) | `xlL` $= -x_H/2 - x_\Phi$ | **agree** | |
| $e_R$: $-x_H - x_\Phi$ (Table I) | `xeR` $= -x_H - x_\Phi$ | **agree** | |
| $N_R$: $-x_\Phi$ (Table I) | `xnR` $= -x_\Phi$ | **agree** | |
| $\Phi$: $2 x_\Phi$ (Table I) | `xSc` $= 2 x_\Phi$ | **agree** | |
| $H$: $-\dfrac{x_H}{2}$ (Table I) | `xHd` $= +x_H/2$ | **disagree** | Sign flip. See D1. The reconstruction pairs it with $\tilde{H}$ in the Dirac Yukawa, so the physics stays the same. |
| $U(1)_X$ as a linear combination of $U(1)_Y$ and $U(1)_{B-L}$ (Sec. II text) | $x_f = x_H Y_f + x_\Phi (B-L)_f$ | **agree** | The formula reproduces all fermion and $\Phi$ charges. It fails only for $H$ (see D1). |
| Three generations of RHN for anomaly cancellation (Sec. II) | `NX` with `Generation` index, three members | **agree** | |
| $-Y_u \overline{q_L} H u_R$, $-Y_d \overline{q_L}\tilde{H}d_R$, $-Y_e \overline{\ell_L}\tilde{H}e_R$ (Eq. `LYk`) | contained in the imported `LSM` | **agree** | Content matches the SM. The paper puts the VEV in the upper doublet component, so its $H$ and $\tilde H$ are exchanged relative to the FeynRules SM. Convention only. |
| $-Y_\nu^{\alpha\beta}\overline{\ell_L^\alpha} H N_R^\beta$ (Eq. `LYk`, 4th term) | `LNuYuk` $= -(y_\nu)_{ij}\epsilon_{ab}\bar{L}_L^{a,i}P_R N_X^j H^{*b} + $ h.c. | **agree** | Same operator. The reconstruction uses $\tilde{H}$ because it uses the standard lower-component VEV. Both give $-\tfrac{v+h}{\sqrt2}y_\nu\bar\nu_L N_R$. |
| $-Y_N^\alpha \Phi \overline{N_R^{\alpha c}} N_R^\alpha$ (Eq. `LYk`, 5th term) | split into `LNXKin` mass term $-\tfrac12\bar{N}_X m_N N_X$ and `LNYuk` $-\tfrac{1}{2\sqrt2}H_X \bar{N}_X y_N N_X$ | **agree** | Correct split of the VEV part and the $H_X$ part. Diagonal in generation, as in the paper (single index $\alpha$). |
| $m_{N_\alpha} = \dfrac{Y_N^\alpha}{\sqrt2} v_\Phi$ (text below $M_{Z'}$) | `yN` $= \sqrt2 M_{N_i}\delta_{ij}/v_\Phi$ | **agree** | Same relation, inverted. |
| $m_D^{\alpha\beta} = \dfrac{Y_\nu^{\alpha\beta}}{\sqrt2} v$ (same text) | $-\tfrac{v+h}{\sqrt2}(y_\nu)_{ij}\bar\nu_L^i P_R N_X^j$ | **agree** | |
| Seesaw matrix $\mathcal{M}_\nu$, $m_\nu \simeq -m_D m_N^{-1} m_D^T$ (Eq. `num`) | Sec. 4, $m_\nu \simeq y_\nu^2 v^2/(2M_N)$ | **agree** | Type-I seesaw. Same result. |
| $\langle H\rangle = \tfrac{1}{\sqrt2}(v+h, 0)^T$, $\langle\Phi\rangle = (v_\Phi+\phi)/\sqrt2$ | $\Phi = \tfrac{1}{\sqrt2}(v_\Phi + H_X)$, unitary gauge | **agree** | The $H$ component that holds the VEV differs. Convention only. See D2. |
| $V = -m_h^2(H^\dagger H) + \lambda(H^\dagger H)^2 + m_\Phi^2(\Phi^\dagger\Phi) + \lambda_\Phi(\Phi^\dagger\Phi)^2 + \lambda'(H^\dagger H)(\Phi^\dagger\Phi)$ (Sec. II) | no potential term at all; `lamX` enters only `MHX`, `lamHX` enters nothing | **missing-in-reconstruction** | The whole new-scalar potential is absent. See D3. |
| $m_\phi^2 = 2\lambda_\Phi v_\Phi^2$ (implied by $V$ at its minimum) | `MHX` $= \sqrt{2\lambda_\Phi v_\Phi^2}$ | **agree** | The mass survives. Only the vertices are gone. |
| $M_{Z'} = g'\sqrt{4v_\Phi^2 + \tfrac14 x_H^2 v^2}$ (Sec. II) | `MZp` $= g_X\sqrt{x_{\rm sc}^2 v_\Phi^2 + x_{H_d}^2 v^2}$ | **agree** | Identical once $x_{\rm sc} = 2x_\Phi$, $x_{H_d} = x_H/2$ and $x_\Phi = 1$. The charge sign of $H$ does not matter here, because it is squared. |
| $Z'$ kinetic and mass term (implied by the gauge group) | `LZpKin` $= -\tfrac14 Z'_{\mu\nu}Z'^{\mu\nu} + \tfrac12 M_{Z'}^2 Z'_\mu Z'^\mu$ | **agree** | Standard normalisation, unitary gauge. |
| $\mathcal{L}^q = -g'(\bar q\gamma^\mu q_x^{q_L}P_L q + \bar q\gamma^\mu q_x^{q_R}P_R q)Z'_\mu - g'(\bar\ell\gamma^\mu q_x^{\ell_L}P_L\ell + \bar e\gamma^\mu q_x^{\ell_R}P_R e)Z'_\mu$ (Eq. `Lag1`) | `LZpF`, first five currents | **agree** | Same overall sign $-g'$, same chirality structure, same charges, flavour universal. |
| $Z'$ current to RHN, implied by Table I and used in Eq. (`2N`) | `LZpF`, term $x_{n_R}\bar{N}_R\gamma^\mu N_R$ with $N_R = P_R N_X$ | **agree** | Purely right-chiral, charge $-x_\Phi$. |
| $\Gamma(Z'\to NN)\propto (1-4m_N^2/M_{Z'}^2)^{3/2}$ (Eq. `2N`) | `NX` declared as a self-conjugate (Majorana) fermion | **agree** | The $\beta^3$ threshold factor is the Majorana / $P$-wave form. Consistent. |
| $|D_\mu\Phi|^2$ interactions (implied by gauging $\Phi$ with $2x_\Phi$) | `LZpHX` $= g_X^2 x_{\rm sc}^2(v_\Phi H_X + \tfrac12 H_X^2)Z'_\mu Z'^\mu$ | **agree** | This is exactly the remainder of $|D_\mu\Phi|^2$ after the $H_X$ kinetic term and the $Z'$ mass term are removed. |
| $H_X$ kinetic and mass term (implied) | `LHXKin` $= \tfrac12(\partial H_X)^2 - \tfrac12 M_{H_X}^2 H_X^2$ | **agree** | Real scalar normalisation. |
| RHN kinetic term (implied) | `LNXKin`, $\tfrac{i}{2}\bar{N}_X\gamma^\mu\partial_\mu N_X$ | **agree** | Majorana $\tfrac12$ normalisation. Ordinary derivative, because the $U(1)_X$ current is written by hand. |
| $|D_\mu H|^2$ with $H$ charged under $U(1)_X$: gives $Z$-$Z'$ mass mixing and $ZZ'h$, $Z'Z'h$ vertices (implied by Table I) | no such term; `LSM` is imported unchanged and carries no $Z'$ | **missing-in-reconstruction** | The $x_{H_d}^2 v^2$ piece is kept inside `MZp`, but the matching interaction terms are not. See D4. |
| No kinetic mixing $B^{\mu\nu}Z'_{\mu\nu}$ (the paper treats $Z'$ as a mass eigenstate) | no kinetic mixing declared | **agree** | Both omit it. |
| Benchmarks $x_\Phi = 1$, $x_H \in \{-2,-1,-0.5,0,0.5,1,2\}$, $g' = 0.4$, $M_{Z'} = 7.5$ TeV (Sec. II B) | `xPhi` $=1.0$, `xH` $=2.0$, `gX` $=0.4$, $v_\Phi = 9375$ GeV giving $M_{Z'} = 7500.6$ GeV | **agree** | The defaults sit on the paper's $x_H = 2$ benchmark. |
| $m_N > M_{Z'}$, so $Z'\to NN$ is closed (text below Eq. `2N`) | $M_{N_i} = 8000$ GeV versus $M_{Z'} = 7500$ GeV | **agree** | The spectrum follows the paper's assumption. |
| $\Gamma_{Z'}$ from Eqs. (`2f`), (`2v`) (Fig. 1) | `WZp` $= 1353$ GeV | **agree** | A tree-level sum over SM fermions at $x_H = 2$, $g' = 0.4$ gives about 1260 GeV. The two values agree to roughly 7%. See D5. |
| (no counterpart in the paper) | unphysical field `NR` $= P_R N_X$, `feynmangaugerules`, PDG codes, widths, interaction orders | **extra-in-reconstruction** | Pure implementation bookkeeping. No new physics. |

---

## 3. Disagreements

### D1. Sign of the $U(1)_X$ charge of the Higgs doublet — **convention**

Table I of the paper gives $H$ the charge $-x_H/2$. The reconstruction gives
`xHd` $= +x_H/2$, from the rule $x_f = x_H Y_f + x_\Phi (B-L)_f$ with
$Y_H = +1/2$. The two files then write the Dirac Yukawa with conjugate doublets
($H$ in the paper, $\tilde{H}$ in the reconstruction), so both sets are gauge
invariant and describe the same model. The charge enters `MZp` squared, so no
number changes.

*Human check:* confirm that the implementation file really uses $\tilde{H}$
(that is `Eps[a,b] ... HC[H]`) in `LNuYuk`, and not $H$; with `xHd` $=+x_H/2$
and a plain $H$, the Dirac Yukawa would break $U(1)_X$ by $x_H$.

### D2. Which doublet component carries the vacuum expectation value — **convention**

The paper writes $\langle H\rangle = (v+h, 0)^T/\sqrt2$, that is the upper
component. It therefore writes the up-quark Yukawa with $H$ and the
down-quark and charged-lepton Yukawas with $\tilde{H}$. The reconstruction uses
the standard FeynRules convention, with the VEV in the lower component. The two
are related by $H \leftrightarrow \tilde{H}$.

*Human check:* nothing to fix in the implementation; confirm only that the
reader of the paper does not copy the paper's $H$ / $\tilde{H}$ placement
straight into a standard FeynRules SM file.

### D3. The whole new-scalar potential is absent — **substantive**

The paper's potential holds five terms. The reconstruction keeps none of them
as a Lagrangian term. It keeps $\lambda_\Phi$ only inside the mass
`MHX` $=\sqrt{2\lambda_\Phi v_\Phi^2}$, and it keeps $\lambda'$ as a declared
parameter that multiplies nothing. The reconstruction states this itself, in
its "Note on an absent term".

The consequences are:

* no $H_X^3$ and $H_X^4$ self couplings;
* no $h$-$H_X$ portal, so no $hH_X$, $h^2H_X$, $hH_X^2$, $h^2H_X^2$ vertices;
* no $h$-$H_X$ mixing angle.

The paper works "in the limit of small $\lambda'$", where the $H$-$\Phi$ mixing
is negligible. The paper's own observables ($e^+e^-\to f\bar f$ through $Z'$)
never use the potential. So the omission does not change any number in this
paper. It does make the model file incomplete for scalar-sector work.

*Human check:* open the implementation file and confirm that `lamHX` and `lamX`
appear in no Lagrangian term and in no internal parameter other than `MHX`; if
the total Lagrangian is missing a potential term, decide whether the file is
meant to cover only the $Z'$ sector.

### D4. No $Z'$ coupling from the Standard Model Higgs kinetic term — **substantive**

The Higgs doublet carries a non-zero $U(1)_X$ charge whenever $x_H \neq 0$, and
the default is $x_H = 2$. The gauged kinetic term $|D_\mu H|^2$ must then give a
$Z$-$Z'$ mass mixing and the vertices $Z'Z'h$ and $ZZ'h$. The reconstruction
keeps the $x_{H_d}^2 v^2$ piece inside `MZp`, which comes from that same term,
but adds no interaction. The imported `LSM` has no $Z'$ in it.

The size of the mixing is of order $x_H v^2 / (4 v_\Phi^2) \approx 3\times10^{-4}$
for the default numbers, so it is small. The paper also treats $Z'$ as a pure
mass eigenstate everywhere.

*Human check:* decide whether the model file must reproduce the $Z$-$Z'$ mixing
and the $Z'Z'h$ / $ZZ'h$ vertices, or whether the zero-mixing approximation is
intended; if it is intended, the $x_{H_d}^2 v^2$ term inside `MZp` is the only
trace of the SM Higgs $U(1)_X$ charge, which is inconsistent bookkeeping.

### D5. $Z'$ total width — **cosmetic**

The reconstruction reports `WZp` $= 1353$ GeV. A tree-level sum of Eqs. (`2f`)
and (`2v`) over three generations at $x_H = 2$, $x_\Phi = 1$, $g' = 0.4$ and
$M_{Z'} = 7500.6$ GeV gives about 1260 GeV. Adding the closed $NN$ channel would
give about 1305 GeV. The gap is a few percent.

*Human check:* re-derive the width with the same channel list the file assumes,
and confirm that the $Z'\to N N$ channel is excluded, as the paper requires.

### D6. Collider statements in the reconstruction's summary — **cosmetic**

Section 4 of the reconstruction lists $pp\to Z'\to N_X N_X$ with same-sign
dileptons, "$Z'\to Z'H_X$-type cascades", and $H_X\to Z'Z'$. None of these is
open with the file's own numbers: $2M_N = 16$ TeV and $2M_{Z'} = 15$ TeV both
exceed the parent masses $M_{Z'} = 7.5$ TeV and $M_{H_X} = 4.2$ TeV. The paper
states directly that $Z'\to NN$ is kinematically disallowed. This is a narrative
error in the summary, not an error in the reconstructed Lagrangian.

*Human check:* ignore the phenomenology paragraph, or re-derive the open decay
channels from the mass spectrum in the field table.

---

## 4. Overall assessment

The reconstruction matches the paper closely in the part of the model that the
paper actually defines and uses. Every $U(1)_X$ charge in Table I is reproduced,
and the reconstruction adds the correct reading of those charges as
$x_f = x_H Y_f + x_\Phi (B-L)_f$. The $Z'$ current of Eq. (`Lag1`) agrees in
sign, in chirality structure, and in flavour universality, and the right-handed
neutrino current implied by Eq. (`2N`) is present with the correct chirality and
Majorana nature. The $Z'$ mass formula, the Dirac and Majorana mass relations,
and the type-I seesaw all agree term by term, and the default parameter values
sit exactly on the paper's $x_H = 2$, $g' = 0.4$, $M_{Z'} = 7.5$ TeV benchmark.
Two differences are convention only: the sign of the Higgs $U(1)_X$ charge and
the choice of doublet component for the vacuum expectation value. They cancel
against each other, because the reconstruction writes the Dirac Yukawa with
$\tilde{H}$ where the paper writes $H$. The one clear gap is the scalar
potential: the five terms of the paper's $V$ appear nowhere as Lagrangian terms,
so the $H_X$ self couplings and the whole $\lambda'$ Higgs portal are missing,
and the related gap is the absent $Z'$ interaction from $|D_\mu H|^2$. Both gaps
are consistent with the paper's own small-$\lambda'$, zero-mixing working limit,
and neither changes any number the paper reports; whether they make the model
file unfit for its purpose depends on what the file is meant to be used for.
That judgement, and the checks listed in Sec. 3, belong to the human reviewer.
