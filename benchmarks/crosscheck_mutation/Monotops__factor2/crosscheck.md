# Cross-check: `reconstruction.md` against "Monotops at the LHC" (Andrea, Fuks, Maltoni; CP3-11-21 / IPHC-PHENO-11-03)

RUN-TAG: XM-CROSS-Monotops__factor2

## 1. Where the paper defines the model

- **Field content** — Sec. "Effective theory for monotops", paragraph before Eq. (1): "We denote by $\phi$, $\chi$ and $V$ the possible scalar, fermionic and vectorial missing energy particles, respectively and by $\varphi$ and $X$ scalar and vector fields lying in the fundamental representation of $SU(3)_c$". The same paragraph adds the second colour-triplet scalar $\tilde\varphi$ for the four-fermion limit.
- **Lagrangian** — Eq. `\label{eq:lag}` (the single displayed equation of that section; it is the paper's Eq. (1)), lines 185-205 of `paper.tex`. It has six lines:
  1. $\mathcal{L}_{SM}$;
  2. $\phi\,\bar u[a^0_{FC}+b^0_{FC}\gamma_5]u + V_\mu\,\bar u[a^1_{FC}\gamma^\mu+b^1_{FC}\gamma^\mu\gamma_5]u$;
  3. $\epsilon^{ijk}\varphi_i\,\bar d^c_j[a^q_{SR}+b^q_{SR}\gamma_5]d_k + \varphi_i\,\bar u^i[a^{1/2}_{SR}+b^{1/2}_{SR}\gamma_5]\chi$;
  4. $\epsilon^{ijk}\tilde\varphi_i\,\bar d^c_j[\tilde a^q_{SR}+\tilde b^q_{SR}\gamma_5]u_k + \tilde\varphi_i\,\bar d^i[\tilde a^{1/2}_{SR}+\tilde b^{1/2}_{SR}\gamma_5]\chi$;
  5. $\epsilon^{ijk}X_{\mu,i}\,\bar d^c_j[a^q_{VR}\gamma^\mu+b^q_{VR}\gamma^\mu\gamma_5]d_k$;
  6. $X_{\mu,i}\,\bar u^i[a^{1/2}_{VR}\gamma^\mu+b^{1/2}_{VR}\gamma^\mu\gamma_5]\chi + \mathrm{h.c.}$
- **Text after Eq. (1)** — meaning of the coupling matrices; the $\epsilon^{ijk}$ symmetry statement: "identical quark couplings to the scalar field $\varphi$ vanish and so do their axial couplings to the vector field $X$".
- **Numerical benchmarks** — Sec. "Model-independent searches": $b=\tilde b=0$; $(a^0_{FC})_{13}=(a^0_{FC})_{31}=(a^1_{FC})_{13}=(a^1_{FC})_{31}=(a^q_{SR})_{12}=-(a^q_{SR})_{21}=(a^{1/2}_{SR})_3=(a^q_{VR})_{11}=(a^{1/2}_{VR})_3=a=0.1$; and $(\tilde a^q_{SR})_{\{1,2\}3}=(\tilde a^{1/2}_{SR})_{\{1,2\}}=a=0.1$ with $M_\varphi=M_{\tilde\varphi}=3$ TeV. Resonance mass 500 GeV, $m_\chi=50$ or 300 GeV, invisible $\phi$ at 300 GeV and invisible $V$ at 50 GeV.

The paper does **not** write kinetic or mass terms for the new fields, does not give explicit electric charges, and does not fix widths. Those items are compared against what the paper implies.

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| Field $\phi$: neutral spin-0 missing-energy state (Sec. "Effective theory", before Eq. (1)) | `phi`, `S[100]`, real, colour singlet, $Q=0$, $M_\phi=300$ GeV | agree | 300 GeV matches the paper's scalar flavour-changing scenario. Reality of $\phi$ is not stated in the paper, but is required for Eq. (1) line 2 to be hermitian. |
| Field $V$: neutral spin-1 missing-energy state | `V`, `V[101]`, real, colour singlet, $Q=0$, $M_V=50$ GeV | agree | 50 GeV matches the paper's vector flavour-changing scenario. |
| Field $\chi$: undetected fermion | `chi`, `F[102]`, Dirac, gauge singlet, $M_\chi=50$ GeV, zero width | agree | The paper leaves the fermion nature open (it cites neutralino, neutrino, gravitino). Dirac is a concrete choice consistent with, but not fixed by, the paper. |
| Field $\varphi$: scalar in the fundamental of $SU(3)_c$ | `vphi`, `S[103]`, colour $\mathbf{3}$, $Q=+2/3$, $M_\varphi=500$ GeV | agree | $Q=+2/3$ is the value forced by Eq. (1) lines 3 ($\varphi\,d d$ and $\varphi\,\bar u\chi$). |
| Field $\tilde\varphi$: second heavy scalar for four-fermion interactions | `vphit`, `S[104]`, colour $\mathbf{3}$, $Q=-1/3$, $M_{\tilde\varphi}=3000$ GeV | agree | $Q=-1/3$ is forced by Eq. (1) line 4; 3 TeV matches the four-fermion benchmark. |
| Field $X$: vector in the fundamental of $SU(3)_c$ | `X`, `V[105]`, colour $\mathbf{3}$, $Q=+2/3$, $M_X=500$ GeV | agree | Charge forced by Eq. (1) lines 5-6. |
| $\mathcal{L}_{SM}$ (Eq. (1), line 1) | not listed in `LTotal` | missing-in-reconstruction | Expected: the reconstruction describes a standalone `.fr` file that extends an SM base model. Not a physics defect on its own. |
| Kinetic and mass terms of the new fields (implied, not written in Eq. (1)) | `Lphikin`, `LVkin`, `Lchikin`, `Lvphikin`, `Lvphitkin`, `LXkin` | extra-in-reconstruction | Standard Proca / Klein-Gordon / Dirac forms. Needed for a working implementation; the paper simply omits them. |
| $\varphi,\tilde\varphi,X$ in the fundamental of $SU(3)_c$, i.e. QCD-coupled (text before Eq. (1)) | `Lvphikin`, `Lvphitkin` use the covariant `DC`; **`LXkin` uses the abelian `FS`**, so the colour-triplet vector gets no gluon coupling from its kinetic term | disagree | The colour triplet $X$ must couple to gluons for the paper's QCD-consistent picture. As reconstructed, $X$ has colour index but no QCD covariantization. |
| $\phi\,\bar u[a^0_{FC}+b^0_{FC}\gamma_5]u$ (Eq. (1), line 2) | $\mathbf{2}\,\phi\,[a^0_{f_1f_2}\bar u_{f_1}u_{f_2} + b^0_{f_1f_2}\bar u_{f_1}\gamma^5 u_{f_2}]$ | **disagree** | Structure, field reps, flavour indices and colour contraction agree, but the reconstruction carries an **explicit overall factor 2** that Eq. (1) does not have. The reconstruction itself flags it. See finding D1. |
| $V_\mu\,\bar u[a^1_{FC}\gamma^\mu+b^1_{FC}\gamma^\mu\gamma_5]u$ (Eq. (1), line 2) | $V_\mu[a^1_{f_1f_2}\bar u_{f_1}\gamma^\mu u_{f_2} + b^1_{f_1f_2}\bar u_{f_1}\gamma^\mu\gamma^5 u_{f_2}]$ | agree | Coefficient 1, no `HC`. This is the term that makes the factor 2 above a *relative* mismatch, not an overall convention. |
| $\epsilon^{ijk}\varphi_i\,\bar d^c_j[a^q_{SR}+b^q_{SR}\gamma_5]d_k$ (Eq. (1), line 3) | `LvphiDiquark`: $\epsilon^{ijk}\varphi^i[a^q_{f_2f_3}\overline{d^c_{f_2}}{}^j d_{f_3}^k + b^q_{f_2f_3}\overline{d^c_{f_2}}{}^j\gamma^5 d_{f_3}^k] + \mathrm{h.c.}$ | agree | Same colour contraction, same conjugation ($\bar d^c$ on the first quark), same $\{1,\gamma^5\}$ pair, coefficient 1. |
| "identical quark couplings to the scalar field $\varphi$ vanish" (text after Eq. (1)) | only the flavour-antisymmetric part of $a^q,b^q$ contributes | agree | Same statement, derived from $\epsilon^{ijk}$ antisymmetry plus the symmetry of $\overline{\psi^c}\{1,\gamma^5\}\chi$. |
| $\varphi_i\,\bar u^i[a^{1/2}_{SR}+b^{1/2}_{SR}\gamma_5]\chi$ (Eq. (1), line 3) | `LvphiChi`: $\varphi^i[a^{1/2}_f\bar u_f^i\chi + b^{1/2}_f\bar u_f^i\gamma^5\chi] + \mathrm{h.c.}$ | agree | One flavour index on the quark, $\chi$ flavour-singlet, colour $\mathbf{3}\otimes\bar{\mathbf{3}}\to\mathbf{1}$, coefficient 1. |
| $\epsilon^{ijk}\tilde\varphi_i\,\bar d^c_j[\tilde a^q_{SR}+\tilde b^q_{SR}\gamma_5]u_k$ (Eq. (1), line 4) | `LvphitDiquark`: $\epsilon^{ijk}\tilde\varphi^i[\tilde a^q_{f_2f_3}\overline{d^c_{f_2}}{}^j u_{f_3}^k + \tilde b^q_{f_2f_3}\overline{d^c_{f_2}}{}^j\gamma^5 u_{f_3}^k] + \mathrm{h.c.}$ | agree | $\bar d^c$ with $u$, as in the paper. No flavour-symmetry constraint, as the reconstruction correctly notes. |
| $\tilde\varphi_i\,\bar d^i[\tilde a^{1/2}_{SR}+\tilde b^{1/2}_{SR}\gamma_5]\chi$ (Eq. (1), line 4) | `LvphitChi`: $\tilde\varphi^i[\tilde a^{1/2}_f\bar d_f^i\chi + \tilde b^{1/2}_f\bar d_f^i\gamma^5\chi] + \mathrm{h.c.}$ | agree | Down-type quark, as in the paper (not up-type). Coefficient 1. |
| $\epsilon^{ijk}X_{\mu,i}\,\bar d^c_j[a^q_{VR}\gamma^\mu+b^q_{VR}\gamma^\mu\gamma_5]d_k$ (Eq. (1), line 5) | `LXDiquark`: same structure $+\,\mathrm{h.c.}$ | agree | Coefficient 1, same conjugation and colour contraction. |
| "[identical quark] axial couplings to the vector field $X$ [vanish]" (text after Eq. (1)) | flavour-symmetric part of $a^{q,V}$ survives; only the antisymmetric part of $b^{q,V}$ survives | agree | Equivalent statement. Consistent with the benchmark $(a^q_{VR})_{11}=0.1$ being diagonal and non-zero. |
| $X_{\mu,i}\,\bar u^i[a^{1/2}_{VR}\gamma^\mu+b^{1/2}_{VR}\gamma^\mu\gamma_5]\chi$ (Eq. (1), line 6) | `LXChi`: same structure $+\,\mathrm{h.c.}$ | agree | Up-type quark with $\chi$, coefficient 1. |
| "+ h.c." placed at the end of Eq. (1) | `HC` applied to the six coloured-mediator terms only; **not** to `Lphiu` and `LVu` | agree (with a caveat) | The neutral-mediator terms are self-hermitian when $a$ is hermitian and $b$ anti-hermitian, so no h.c. is needed there. The paper's single trailing "h.c." is ambiguous about scope; see finding D3. |
| Chirality: $\{1,\gamma_5\}$ and $\{\gamma^\mu,\gamma^\mu\gamma_5\}$ pairs throughout Eq. (1) | identical pairs, no `ProjP`/`ProjM`; chirality carried by $a\mp b$ | agree | Exactly the paper's parametrization. |
| Benchmark $(a^0_{FC})_{13}=(a^0_{FC})_{31}=0.1$ | `a0FC[1,3]=a0FC[3,1]=0.1` | agree | Value matches; but see D1 — the factor 2 changes what this value means physically. |
| Benchmark $(a^1_{FC})_{13}=(a^1_{FC})_{31}=0.1$ | `a1FC[1,3]=a1FC[3,1]=0.1` | agree | |
| Benchmark $(a^q_{SR})_{12}=-(a^q_{SR})_{21}=0.1$ | `aqSR[1,2]=+0.1`, `aqSR[2,1]=-0.1` | agree | |
| Benchmark $(a^{1/2}_{SR})_3=0.1$ | `ahalfSR[3]=0.1` | agree | |
| Benchmark $(a^q_{VR})_{11}=0.1$ | `aqVR[1,1]=0.1` | agree | |
| Benchmark $(a^{1/2}_{VR})_3=0.1$ | `ahalfVR[3]=0.1` | agree | |
| Benchmark $(\tilde a^q_{SR})_{\{1,2\}3}=0.1$ | `atildeqSR[1,3]=atildeqSR[2,3]=0.1` | agree | |
| Benchmark $(\tilde a^{1/2}_{SR})_{\{1,2\}}=0.1$ | `atildehalfSR[1]=atildehalfSR[2]=0.1` | agree | |
| Benchmark $b=\tilde b=0$ (all axial couplings vanish) | all `b*` defaults 0 | agree | |
| Benchmark $M_\varphi=M_{\tilde\varphi}=3$ TeV in the four-fermion limit | `Mvphi = 500` GeV, `Mvphit = 3000` GeV | agree (partly) | The file can hold only one default. 500 GeV is the paper's resonant-scenario mass for $\varphi$; 3 TeV is its four-fermion mass for $\tilde\varphi$. The defaults therefore mix two of the paper's five scenarios. |
| $\mathrm{BR}(X,\varphi\to t\chi)=1$ assumed | `Wvphi = 50` GeV, `WX = 50` GeV, `Wvphit = 300` GeV | agree (not constrained) | The paper fixes no widths; these are 10% of the mass. They do not contradict the paper. |
| Electroweak structure: "effective Lagrangian in terms of mass eigenstates" | new fields are $SU(2)_L$ singlets with electric charge $Q$ declared directly, no hypercharge | agree | Consistent with a mass-eigenstate effective Lagrangian. |

## 3. Disagreements

**D1 — Explicit overall factor 2 in the $\phi\bar u u$ term (`Lphiu`). Severity: substantive.**
Eq. (1) writes $\phi\,\bar u[a^0_{FC}+b^0_{FC}\gamma_5]u$ with coefficient 1, while the reconstruction has $2\,\phi\,\bar u[a^0+b^0\gamma^5]u$. Because the neighbouring $V_\mu\bar u\gamma^\mu u$ term in the same line of Eq. (1) carries coefficient 1 in **both** documents, this is a *relative* factor 2 between the scalar and vector flavour-changing vertices, so it cannot be absorbed into any overall normalization or h.c. convention. A human should recompute the $\phi\bar u u$ Feynman rule from the implementation file and compare the scalar flavour-changing cross section (paper scenario III, $\sigma=0.322$ pb and $a_{min}=0.14$ at $a=0.1$) against the file, since a factor 2 in the vertex gives a factor 4 in the rate and a factor 2 in the extracted $a_{min}$.

**D2 — `LXkin` uses the abelian field strength `FS`, not a covariant one. Severity: substantive.**
The paper states that $X$ lies in the fundamental representation of $SU(3)_c$, which requires a QCD-covariant kinetic term for a colour-triplet vector; the reconstruction reports $-\tfrac12 X^\dagger_{\mu\nu}X^{\mu\nu}$ with $X_{\mu\nu}=\partial_\mu X_\nu-\partial_\nu X_\mu$ and no gluon term. A human should check whether the implementation file really uses `FS[X,mu,nu]` (giving a colour triplet with no gluon coupling from the kinetic term) or a `DC`-based field strength, and whether the $X$-mediated resonant benchmark was generated with QCD-coupled $X$.

**D3 — Scope of the trailing "h.c." in Eq. (1). Severity: convention.**
The paper puts one "+ h.c." at the very end of a six-line equation, so it may be read as applying to every new term or only to the non-self-conjugate ones. The reconstruction applies it to the coloured-mediator terms only and leaves `Lphiu` and `LVu` bare. A human should confirm that the intended hermiticity conditions ($a^{0,1}$ hermitian, $b^{0,1}$ anti-hermitian) are what the implementation assumes; note that a "h.c. applies to everything" reading would double *both* neutral terms, which still does not reproduce the asymmetric factor 2 of D1.

**D4 — Default masses mix two different paper scenarios. Severity: cosmetic.**
The paper uses $M_\varphi=3$ TeV in the four-fermion limit and 500 GeV in the resonant scenario; the reconstruction reports `Mvphi = 500` GeV together with `Mvphit = 3000` GeV. A human should confirm that the benchmark cards, not the default values in the model file, set the masses for each of the five scenarios.

**D5 — Unstated choices: $\chi$ Dirac, $\phi$ and $V$ real, widths 10% of mass. Severity: cosmetic.**
The paper leaves the fermion type of $\chi$ open and fixes no widths. The reconstruction commits to a Dirac $\chi$, real $\phi$ and $V$, and 10%-of-mass widths. A human should check the width values against the couplings if any rate depends on them (the paper assumes $\mathrm{BR}(X,\varphi\to t\chi)=1$).

## 4. Overall assessment

The reconstruction reproduces the monotop simplified model of Eq. (1) closely and in the right physical language. All six new fields are present with the colour representations and the electric charges that gauge invariance of Eq. (1) requires; every interaction term of Eq. (1) has a counterpart with the correct conjugation ($\bar d^c$ on the first quark of each di-quark vertex), the correct $\epsilon^{ijk}$ colour contraction, the correct pairing of up-type and down-type quarks with each mediator, the correct $\{1,\gamma^5\}$ / $\{\gamma^\mu,\gamma^\mu\gamma^5\}$ structure, and the correct flavour index placement. The reconstruction also independently rederives the paper's statement about which flavour components survive the $\epsilon^{ijk}$ antisymmetry, and every non-zero default coupling matches the paper's benchmark list one for one. Two items stand out and drive any further review: the explicit factor 2 in front of the $\phi\bar u u$ term, which has no counterpart in Eq. (1) and is not shared by the neighbouring $V\bar u u$ term, so it changes the relative normalization of the two flavour-changing vertices and, if real, the scalar flavour-changing rate by a factor of 4; and the abelian field strength in the $X$ kinetic term, which leaves a declared colour triplet without a QCD coupling from its own kinetic term. The remaining differences are matters the paper simply does not fix (kinetic terms, widths, the Dirac nature of $\chi$, the scope of the single trailing "h.c.") and are reported transparently by the reconstruction itself.
