# Cross-check: `reconstruction.md` against the paper

**Paper:** *Probing the minimal $U(1)_X$ model at future electron-positron colliders via
fermion pair-production channels* — Das, Dev, Hosotani, Mandal (OU-HET-1085).

**Reconstruction:** `reconstruction.md`, an independent read-out of a FeynRules file
(`sanitized.fr`) that I do not have.

---

## 1. Where the paper defines the model

| Item | Location in `paper.tex` |
|---|---|
| Gauge group $SU(3)_C\otimes SU(2)_L\otimes U(1)_Y\otimes U(1)_X$ | Sec. II, first paragraph after Table I |
| Field content and all $U(1)_X$ charges | **Table I** (`\label{tab1}`), lines 92–108 |
| Numeric charges for benchmark $x_H$ values | **Table II** (`\label{tab2}`), lines 254–276 |
| Yukawa Lagrangian (5 terms) | **Eq. (LYk)** (`\label{LYk}`), lines 132–138 |
| Scalar potential $V$ | unnumbered `align`, Sec. II, line 159 |
| Vacuum expectation values of $H$ and $\Phi$ | unnumbered `align`, Sec. II, lines 162–166 |
| $M_{Z'}$ after symmetry breaking | unnumbered `eqnarray`, Sec. II, line 170 |
| Dirac and Majorana neutrino masses | Sec. II text, line 172 |
| Seesaw mass matrix | **Eq. (num)**, line 180 |
| $Z'$ current with SM fermions | **Eq. (Lag1)**, lines 188–191 |
| $Z'$ partial widths | **Eqs. (2f), (2v), (2N)**, lines 199–213 |
| Benchmark point $M_{Z'}=7.5$ TeV, $g'=0.4$, $x_\Phi=1$ | Sec. II B, line 445 |

The paper writes no explicit covariant derivative, no $Z'$ kinetic term, and no
$H_X$ ($=\phi$) interaction Lagrangian. For those rows I compare against the
structure that the paper's own equations imply.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Gauge group: SM $\times\,U(1)_X$, one new neutral boson $Z'$ (Sec. II, Table I) | $U(1)_X$ with boson $Z'$, coupling $g_X$ | **agree** | `gX` $\equiv$ paper's $g'$. |
| $x_{q_L}=\frac{x_H}{6}+\frac{x_\Phi}{3}$ (Table I) | $x_{q_L}=\frac{x_H}{6}+\frac{x_\Phi}{3}$ | **agree** | Table II prints $1/3$ at $x_H=2$; the formula gives $2/3$. See D-4. |
| $x_{u_R}=\frac{2x_H}{3}+\frac{x_\Phi}{3}$ (Table I) | identical | **agree** | $5/3$ at $x_H=2$, matches Table II. |
| $x_{d_R}=-\frac{x_H}{3}+\frac{x_\Phi}{3}$ (Table I) | identical | **agree** | $-1/3$ at $x_H=2$, matches Table II. |
| $x_{\ell_L}=-\frac{x_H}{2}-x_\Phi$ (Table I) | identical | **agree** | $-2$ at $x_H=2$, matches Table II. |
| $x_{e_R}=-x_H-x_\Phi$ (Table I) | identical | **agree** | $-3$ at $x_H=2$, matches Table II. |
| $x_{N_R}=-x_\Phi$ (Table I) | $x_{n_R}=-x_\Phi$ | **agree** | $-1$ at $x_H=2$, matches Table II. |
| $x_{H}=-\frac{x_H}{2}$ for the Higgs doublet (Table I, and $-1$ at $x_H=2$ in Table II) | $x_{H_d}=+\frac{x_H}{2}$ (and $+1$ at $x_H=2$) | **disagree** | **Sign flip.** The one hard numeric conflict. See D-1. |
| $x_\Phi^{\rm scalar}=2x_\Phi$ (Table I) | $x_{Sc}=2x_\Phi$ | **agree** | $2$ at $x_\Phi=1$. |
| Color / isospin / hypercharge assignments (Table I) | field table, Sec. 3 | **agree** | All new states are $SU(3)_C$ and $SU(2)_L$ singlets with $Y=0$, as in Table I. |
| Three generations of RHNs cancel gauge and mixed gauge-gravity anomalies (Sec. I, Sec. II) | three Majorana $N_X^{1,2,3}$, anomaly free for any $x_H,x_\Phi$ | **agree** | Same statement. |
| $U(1)_X$ is a linear combination of $U(1)_Y$ and $U(1)_{B-L}$; $x_H=0$ gives $B-L$ (Sec. II, Table II caption) | $x_f=x_HY_f+x_\Phi(B-L)_f$; $x_H=0$ gives $B-L$ | **agree** | Holds entry by entry for every fermion. For the doublet it is the source of D-1. |
| $x_\Phi=1$ fixed without loss of generality (Sec. II) | `xPhi` kept free, default $1.0$ | **agree** | The reconstruction is a strict generalisation. |
| $-Y_u\overline{q_L}Hu_R-Y_d\overline{q_L}\tilde Hd_R-Y_e\overline{\ell_L}\tilde He_R$ (Eq. LYk) | not written; imported through `LSM` | **agree** | SM Yukawas are unchanged by the extension, so importing them is correct. |
| $-Y_\nu^{\alpha\beta}\overline{\ell_L^\alpha}HN_R^\beta+{\rm H.c.}$ (Eq. LYk) | Term 7: $-(Y_\nu)_{ij}\bar L_L^{\alpha i}N_R^j\epsilon_{\alpha\beta}H^{*\beta}+{\rm h.c.}$ | **agree** | Same operator. The paper's $H$ is the doublet whose **upper** component holds the VEV, so it is the $Y=-1/2$ doublet; the reconstruction's $\epsilon_{\alpha\beta}H^{*\beta}=\tilde H$ is the same object in standard convention. Chirality ($P_R N_X$), generation structure and the h.c. partner all match. |
| $-Y_N^\alpha\Phi\overline{N_R^{\alpha c}}N_R^\alpha+{\rm H.c.}$ (Eq. LYk) | Term 6: $-\frac{1}{2\sqrt2}H_X\bar N_X(Y_N)N_X$ | **agree** | Diagonal in generation in both (paper carries one index $\alpha$). |
| $m_{N_\alpha}=\frac{Y_N^\alpha}{\sqrt2}v_\Phi$ (Sec. II, line 172) | $(Y_N)_{ij}=\frac{\sqrt2 M_{N_i}}{v_X}\delta_{ij}$ | **agree** | Exact inverse of the paper's relation. The residual $H_X\bar NN$ coupling is then $-\frac12\frac{M_N}{v_X}$, the correct partner of $-\frac12 M_N\bar NN$. |
| $m_D^{\alpha\beta}=\frac{Y_\nu^{\alpha\beta}}{\sqrt2}v$ (Sec. II, line 172) | same, stated in Term 7 | **agree** | With `ynu` $=10^{-6}$ and $M_N=8$ TeV the seesaw gives $m_\nu\approx4\times10^{-3}$ eV, a sensible light mass. |
| Seesaw matrix $\mathcal{M}_\nu=\begin{pmatrix}0&m_D\\m_D^T&m_N\end{pmatrix}$ (Eq. num) | type-I seesaw from $Y_\nu$ plus $m_N$ | **agree** | The reconstruction does not diagonalise, which is normal for a FeynRules file. |
| $Y_\nu^{\alpha\beta}$ is a general $3\times3$ matrix with flavour mixing (Sec. II, line 131) | `ynu` $=10^{-6}\,\delta_{ij}$ | **agree** | Structure agrees; the diagonal value is a benchmark choice, not a model statement. |
| $\mathcal{L}^q=-g'\big(\bar q\gamma^\mu q_x^{q_L}P_Lq+\bar q\gamma^\mu q_x^{q_R}P_Rq\big)Z'_\mu-g'\big(\bar\ell\gamma^\mu q_x^{\ell_L}P_L\ell+\bar e\gamma^\mu q_x^{\ell_R}P_Re\big)Z'_\mu$ (Eq. Lag1) | Term 2: $-g_XZ'_\mu\sum_f x_f\,\bar f\gamma^\mu f$ with chiral fields | **agree** | Same overall sign, same chiral projectors, same charges. The reconstruction's $D_\mu\supset+ig_Xx_fZ'_\mu$ reproduces exactly this sign. |
| $Z'$ couples to $N_R$ with $g_R^N[g',x_\Phi]$ (implied by Eq. 2N and Table I) | $N_R$ current in Term 2, reducing to a pure axial $\bar N_X\gamma^\mu\gamma_5N_X$ | **agree** | The paper never writes the term, but Eq. (2N) requires it. The $(1-4m_N^2/M_{Z'}^2)^{3/2}$ factor in Eq. (2N) is the expected behaviour for a Majorana pair from an axial current. |
| Charges and coupling are family universal (Sec. III, line 465) | flavour diagonal, generation universal, CKM unitarity applied | **agree** | No tree-level flavour-changing neutral current in either. |
| $M_{Z'}=g'\sqrt{4v_\Phi^2+\frac14x_H^2v^2}\simeq2g'v_\Phi$ (Sec. II, line 170) | `MZp` $=g_X\sqrt{x_{Sc}^2v_X^2+x_{H_d}^2v^2}$ | **agree** | Identical once $x_\Phi=1$: $x_{Sc}^2=4$ and $x_{H_d}^2=x_H^2/4$. The charge enters squared, so D-1 is invisible here. Numerically $0.4\sqrt{4(9375)^2+(246)^2}=7501$ GeV, the paper's 7.5 TeV benchmark. |
| $Z'$ kinetic term (not written; implied by the gauge group) | Term 1: $-\frac14Z'_{\mu\nu}Z'^{\mu\nu}$, abelian field strength | **agree** | Abelian, so no $Z'$ self interaction, as required. |
| No $B^{\mu\nu}Z'_{\mu\nu}$ kinetic mixing anywhere in the paper | no kinetic mixing | **agree** | Both set the mixing to zero. The paper's whole analysis uses pure $Z'$ exchange. |
| $V=-m_h^2(H^\dag H)+\lambda(H^\dag H)^2+m_\Phi^2(\Phi^\dag\Phi)+\lambda_\Phi(\Phi^\dag\Phi)^2+\lambda'(H^\dag H)(\Phi^\dag\Phi)$ — the $\lambda_\Phi$ part (Sec. II, line 159) | Term 8: $-\lambda_\Phi v_XH_X^3-\frac{\lambda_\Phi}{4}H_X^4$ | **agree** | Exactly the cubic and quartic left after $\Phi=(v_X+H_X)/\sqrt2$ and after the $H_X$ mass term is split off. |
| the $-m_h^2(H^\dag H)+\lambda(H^\dag H)^2$ part of $V$ | not written; imported through `LSM` | **agree** | Unchanged SM sector. |
| the $\lambda'(H^\dag H)(\Phi^\dag\Phi)$ part of $V$ — quartic piece | Term 8: $-\frac{\lambda'}{2}H_X^2(H^\dag H)$ | **agree** | Correct coefficient. |
| the $\lambda'(H^\dag H)(\Phi^\dag\Phi)$ part of $V$ — **trilinear** piece $-\lambda'v_XH_X(H^\dag H)$ | absent | **missing-in-reconstruction** | Removes all tree-level $h$–$H_X$ mass mixing. See D-2. |
| $\langle\Phi\rangle=(v_\Phi+\phi)/\sqrt2$, one real scalar $\phi$ survives (Sec. II, lines 162–166) | $\Phi=\frac{1}{\sqrt2}(v_X+H_X)$; Goldstone eaten by $Z'$; only real $H_X$ | **agree** | `HX` $\equiv$ paper's $\phi$. |
| $M_\phi$ (never given in the paper) | `MHX` $=\sqrt{2\lambda_\Phi v_X^2}\approx4193$ GeV | **agree** | Follows from the paper's $V$ plus the minimum condition. The paper simply never uses $\phi$. |
| $|D_\mu\Phi|^2$ gauge-scalar terms (not written; implied by the Higgs mechanism) | Term 5: $g_X^2x_{Sc}^2\big(v_XH_X+\frac12H_X^2\big)Z'_\mu Z'^\mu$ | **agree** | Exactly the remainder of $|D_\mu\Phi|^2$ after the mass term. Gives $Z'Z'H_X$ and $Z'Z'H_XH_X$. |
| $|D_\mu H|^2$ terms for a $U(1)_X$-charged doublet ($Z$–$Z'$ mass mixing, $Z'Z'h$, $Z'Zh$) — implied by Table I and by the $x_H^2v^2$ piece of $M_{Z'}$ | absent | **missing-in-reconstruction** | $M_{Z'}$ knows about $v$, but no vertex does. See D-3. |
| RHN kinetic and Majorana mass terms (not written; implied by Eq. LYk and Eq. num) | Term 3: $\frac{i}{2}\bar N_X\slashed\partial N_X-\frac12\bar N_X m_NN_X$, $m_N$ diagonal | **agree** | Standard Majorana normalisation; diagonal $m_N$ matches the paper's single-index $Y_N^\alpha$. |
| $m_N>M_{Z'}$, so $Z'\to NN$ is closed (Sec. II A, line 215) | $M_{N_{1,2,3}}=8000$ GeV, $M_{Z'}=7501$ GeV | **agree** | The benchmark satisfies the paper's assumption. |
| $\Gamma(Z')$ from Eqs. (2f) and (2v), Fig. 1, at $M_{Z'}=7.5$ TeV | `WZp` $=1353$ GeV | **agree** | I summed Eqs. (2f) and (2v) over three generations at $x_H=2$, $x_\Phi=1$, $g'=0.4$: $\frac{M_{Z'}}{24\pi}g'^2\times85=1353$ GeV. Exact match, and it independently confirms $x_{q_L}=2/3$ (see D-4). |
| $g'=0.4$ is the LEP-II limit at $M_{Z'}=7.5$ TeV, $x_H=2$ (Sec. II B, line 445) | `gX` $=0.4$, `xH` $=2.0$ | **agree** | The file sits on the paper's benchmark point. |
| $v_\Phi$ free, $v_\Phi^2\gg v^2$ (Sec. II, line 167) | `vX` $=9375$ GeV | **agree** | $9375=7500/(2\times0.4)$, the value implied by $M_{Z'}\simeq2g'v_\Phi$. |
| $L(N_R)=+1$, required by $\overline{\ell_L}HN_R$ in Eq. (LYk) and by $x_{N_R}=-x_\Phi$ (i.e. $B-L=-1$) | `NR` declares `LeptonNumber -> -1` | **disagree** | Bookkeeping only, no vertex changes. See D-5. |
| — | `NR` as an `Unphysical -> True` shorthand for $P_RN_X$ | **extra-in-reconstruction** | Pure FeynRules idiom. No physics content, no new degree of freedom. |
| — | `feynmangaugerules`, `FlavorExpand -> {SU2D}`, interaction orders `{{QCD,1},{QED,2},{NP,1}}`, PDG codes | **extra-in-reconstruction** | Implementation bookkeeping with no counterpart in the paper. |
| — | $\Gamma_{H_X}=0.1$ GeV, $\Gamma_{N_i}=10^{-10}$ GeV | **extra-in-reconstruction** | The paper never computes these widths. |

---

## 3. Disagreements

### D-1. $U(1)_X$ charge of the Higgs doublet: $+x_H/2$ instead of $-x_H/2`
**Severity: substantive.**

The paper states this charge twice and both times with a minus sign: Table I gives
$-\frac{x_H}{2}$, and Table II gives $-1$ in the $x_H=2$ row. The reconstruction gives
$x_{H_d}=+\frac{x_H}{2}$, i.e. $+1$ at $x_H=2$. This is a straight sign flip.

There is a real convention question underneath it, and a human must settle it by reading
the file:

- The paper's $H$ is **not** the standard $Y=+\frac12$ doublet. The paper writes
  $\langle H\rangle=\frac{1}{\sqrt2}\binom{v+h}{0}$ — the VEV sits in the **upper**
  component — and it uses the bare $H$ (not $\tilde H$) in the **up-type** Yukawa
  $\overline{q_L}Hu_R$. Both facts identify the paper's $H$ as the $Y=-\frac12$ doublet.
  With $Y_H=-\frac12$, the paper's $-\frac{x_H}{2}$ obeys the same universal rule
  $x=x_HY+x_\Phi(B-L)$ as every fermion, and all five terms of Eq. (LYk) are $U(1)_X$
  invariant. I checked each one.
- The paper's Table I nevertheless lists $U(1)_Y(H)=+\frac12$ in the row above. That row
  is inconsistent with the paper's own VEV and Yukawa conventions.
- The reconstruction uses the opposite labelling: its $H$ is the standard $Y=+\frac12$
  doublet, and it writes the neutrino Yukawa with $\tilde H=i\sigma^2H^*$. Under that
  labelling $+\frac{x_H}{2}$ is the value the rule $x=x_HY+x_\Phi(B-L)$ produces.

So the two sign choices may describe the same physics under two names for the same
doublet. Three things keep this from being a safe conclusion. First, the sign disagrees
with the only two places where the paper prints the number. Second, the reconstruction
does not flag the relabelling; it presents $+\frac{x_H}{2}$ as the paper's value. Third,
a wrong sign here is numerically inert **only** because $x_{H_d}$ appears exactly once in
the file, inside $M_{Z'}$, where it is squared. Any later extension that puts $x_{H_d}$
into the Higgs covariant derivative would give $Z$–$Z'$ mixing and $Z'Z'h$ vertices of
the wrong sign.

*What a human should check:* open `sanitized.fr`, read the literal sign of `xHd`, and
decide whether it is consistent with the hypercharge of the Higgs doublet that the
imported `SM.fr` actually supplies — then confirm that `xHd` appears nowhere except
inside `MZp`.

### D-2. Missing $H_X(H^\dagger H)$ trilinear
**Severity: substantive.**

The paper's potential contains $\lambda'(H^\dag H)(\Phi^\dag\Phi)$. Substituting
$\Phi=(v_X+H_X)/\sqrt2$ gives **two** interaction terms: $-\lambda'v_XH_X(H^\dag H)$ and
$-\frac{\lambda'}{2}H_X^2(H^\dag H)$. The reconstruction reports only the second. The
missing one is the larger of the two, because $v_X=9375$ GeV. It is also the term that
mixes $h$ with $H_X$ and that lets $H_X$ decay to SM final states. The reconstruction
itself flags this in its Note 2.

The paper does not use this term: it works "in the limit of small $\lambda^\prime$" where
$H$–$\Phi$ mixing is negligible (Sec. II, line 161). So the omission is defensible for
reproducing the paper's results, but it is still an incomplete transcription of the
paper's potential.

*What a human should check:* confirm that `LPotX` in the file really has no
$v_X H_X(H^\dag H)$ term, then decide whether the intended use of the file needs
$h$–$H_X$ mixing at all.

### D-3. Missing $|D_\mu H|^2$ terms for the charged doublet
**Severity: substantive.**

The paper's $M_{Z'}=g'\sqrt{4v_\Phi^2+\frac14x_H^2v^2}$ contains a $v^2$ piece. That piece
exists only because the doublet carries $U(1)_X$ charge. The same covariant derivative
must then also produce $Z$–$Z'$ mass mixing and $Z'Z'h$ and $Z'Zh$ vertices. The
reconstruction reports the $v^2$ piece inside $M_{Z'}$ but no matching vertex, so the mass
and the interactions come from inconsistent sources.

The paper is equally silent: it never discusses $Z$–$Z'$ mixing, and every observable in
Secs. III–V uses pure $\gamma$, $Z$ and $Z'$ exchange with no mixing. The effect is small
($\propto v^2/v_\Phi^2\sim7\times10^{-4}$), so this is a deliberate approximation in both
places rather than a contradiction between them.

*What a human should check:* decide whether the file is meant to reproduce only the
paper's tree-level $Z'$ exchange; if it is meant for general use, the $Z$–$Z'$ mixing that
$M_{Z'}$ already assumes must be added.

### D-4. Paper typo that the reconstruction does not inherit
**Severity: cosmetic (the paper's defect, not the reconstruction's).**

Table II, row $x_H=2$, prints $q_L=\frac13$. The formula in the same table,
$\frac16x_H+\frac13x_\Phi$, gives $\frac23$. The reconstruction gives $\frac23$. Two
independent checks say the reconstruction is right: the formula itself, and the total
$Z'$ width — summing the paper's Eqs. (2f) and (2v) with $x_{q_L}=\frac23$ reproduces the
file's $\Gamma_{Z'}=1353$ GeV exactly, while $\frac13$ does not.

*What a human should check:* nothing in the file; note the paper's Table II typo so that
nobody "fixes" the implementation to match it.

### D-5. Lepton number of `NR` declared as $-1$
**Severity: convention.**

The paper's Eq. (LYk) term $-Y_\nu\overline{\ell_L}HN_R$ conserves lepton number only for
$L(N_R)=+1$, and the paper's own charge $x_{N_R}=-x_\Phi$ is the $B-L=-1$ assignment,
which also means $L=+1$. The file declares `LeptonNumber -> -1`. FeynRules uses this
declaration only for conserved-charge checks, so no vertex and no prediction changes. The
reconstruction correctly identifies the inconsistency in its Note 1.

*What a human should check:* flip the declaration to $+1$ if the file is ever run through
a quantum-number consistency check; confirm first that nothing else reads it.

### D-6. Loose wording in the physics summary
**Severity: cosmetic.**

Sec. 5 of the reconstruction says the model gives "$Z'\to Z'H_X$-type gauge-scalar
vertices". The vertex from Term 5 is $Z'Z'H_X$, which is not a decay of $Z'$. This is a
wording slip, not a Lagrangian error.

*What a human should check:* nothing in the file; correct the sentence if the text is
reused.

---

## 4. Overall assessment

The reconstruction reproduces the paper's model closely and in detail. Every fermion
$U(1)_X$ charge, the scalar charge $2x_\Phi$, the chiral structure and overall sign of the
$Z'$ current in Eq. (Lag1), the Dirac and Majorana Yukawa terms of Eq. (LYk) with their
exact normalisations, the $\lambda_\Phi$ part of the potential, the $|D_\mu\Phi|^2$
gauge-scalar vertices, the seesaw structure, and $M_{Z'}$ all match the paper. Several
numbers agree to the digit and were not simply copied: $M_{Z'}=7501$ GeV from
$v_X=9375$ GeV, and $\Gamma_{Z'}=1353$ GeV, which I recomputed from the paper's Eqs. (2f)
and (2v) and which also settles a typo in the paper's own Table II. The benchmark point
$g'=0.4$, $x_H=2$, $x_\Phi=1$, $M_{Z'}=7.5$ TeV is exactly the one the paper adopts in
Sec. II B. Two omissions stand out — the $H_X(H^\dag H)$ trilinear and the $|D_\mu H|^2$
terms for the $U(1)_X$-charged doublet — and the reconstruction flags both itself; each
is consistent with an approximation the paper also makes, so a reviewer should decide
whether the file is meant to cover only the paper's tree-level $Z'$ exchange. The single
hard numeric conflict is the sign of the Higgs doublet's $U(1)_X$ charge, which the
reconstruction gives as $+x_H/2$ where the paper's Table I and Table II both give
$-x_H/2$; the difference may be no more than a relabelling of $H$ and $\tilde H$, since
the paper puts its VEV in the upper component and uses $H$ in the up-type Yukawa, but the
reconstruction does not say so, and the sign is hidden from every number in the file
because $x_{H_d}$ occurs only squared inside $M_{Z'}$. That one item needs a human to read
the sign in the source file and the hypercharge convention of the imported SM before the
comparison can be closed.
