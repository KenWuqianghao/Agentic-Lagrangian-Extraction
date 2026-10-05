# Cross-check: `reconstruction.md` against "Monotops at the LHC"

RUN-TAG: XM-CROSS-Monotops__control

## 1. Where the paper defines the model

* **Paper**: J. Andrea, B. Fuks, F. Maltoni, *Monotops at the LHC* (CP3-11-21; IPHC-PHENO-11-03).
* **Lagrangian**: the single displayed equation with `\label{eq:lag}`, printed as **Eq. (1)** in the
  section *Effective theory for monotops*. It is the only numbered equation in the paper.
* **Field content**: the text just above Eq. (1) in the same section. It names `$\phi$`, `$\chi$` and
  `$V$` as the scalar, fermionic and vectorial missing-energy states, and `$\varphi$` and `$X$` as
  scalar and vector fields "lying in the fundamental representation of $SU(3)_c$". The text just
  below Eq. (1) adds `$\tilde\varphi$` for the four-fermion limit.
* **Symmetry statement**: the sentence below Eq. (1) that starts "Because of the symmetry properties
  of the $\epsilon^{ijk}$ tensor...".
* **Benchmark numbers**: the section *Model-independent searches*, the paragraph that starts "To
  illustrate the main features..." (coupling values, masses, the five scenarios).
* **Colour and charge**: the paper never writes an electric charge or a hypercharge for any new
  field. The charges below are inferred from the operators in Eq. (1).

The paper gives no kinetic terms and no mass terms for the new states. Eq. (1) lists
`$\lag_{SM}$` plus interaction operators only.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| `$\lag_{SM}$` (Eq. 1, line 1) | absent | **missing-in-reconstruction** | The reconstruction states this in §1.15: the SM part is not in the file. This is normal for a FeynRules add-on model that loads the SM separately. |
| `$\phi\,\bar u[a^0_{FC}+b^0_{FC}\gamma_5]u$` (Eq. 1) | §1.7 `Lphiu` | **agree** | Same Dirac structure, same flavour matrices. The reconstruction makes the colour index explicit and diagonal, which the paper implies by "Assuming QCD interactions to be flavor-conserving". The chiral rewrite `$(a-b)P_L+(a+b)P_R$` is algebraically the same. |
| `$V_\mu\,\bar u[a^1_{FC}\gamma^\mu+b^1_{FC}\gamma^\mu\gamma_5]u$` (Eq. 1) | §1.8 `LVu` | **agree** | Same structure, colour diagonal, flavour matrices understood. |
| `$\epsilon^{ijk}\varphi_i\,\bar d^c_j[a^q_{SR}+b^q_{SR}\gamma_5]d_k$` (Eq. 1) | §1.9 `LvphiDiquark` | **agree** | Same `$\epsilon$` contraction, same conjugated down-type bilinear, same scalar plus pseudo-scalar pair. Baryon number is violated in both. |
| `$\varphi_i\,\bar u^i[a^{1/2}_{SR}+b^{1/2}_{SR}\gamma_5]\chi$` (Eq. 1) | §1.10 `LvphiChi` | **agree** | Same colour contraction (one index on `$\varphi$`, one on the up-type quark), same 3-vector in flavour space. |
| `$\epsilon^{ijk}\tilde\varphi_i\,\bar d^c_j[\tilde a^q_{SR}+\tilde b^q_{SR}\gamma_5]u_k$` (Eq. 1) | §1.11 `LvphitDiquark` | **agree** | Down-type conjugate with up-type, so no flavour symmetry condition. The reconstruction says this and the paper imposes none. |
| `$\tilde\varphi_i\,\bar d^i[\tilde a^{1/2}_{SR}+\tilde b^{1/2}_{SR}\gamma_5]\chi$` (Eq. 1) | §1.12 `LvphitChi` | **agree** | Same field content and same Dirac structure. |
| `$\epsilon^{ijk}X_{\mu,i}\,\bar d^c_j[a^q_{VR}\gamma^\mu+b^q_{VR}\gamma^\mu\gamma_5]d_k$` (Eq. 1) | §1.13 `LXDiquark` | **agree** (operator) | The operator itself matches exactly. The reconstruction's *statement about which flavour part survives* does not match the paper; see the next row. |
| `$X_{\mu,i}\,\bar u^i[a^{1/2}_{VR}\gamma^\mu+b^{1/2}_{VR}\gamma^\mu\gamma_5]\chi$` (Eq. 1) | §1.14 `LXChi` | **agree** | Same structure and same colour contraction. |
| Text below Eq. (1): "identical quark couplings to the scalar field `$\varphi$` vanish" | §1.9: only the antisymmetric part of `$a^q$`, `$b^q$` acts | **agree** | Both statements are the same: the diagonal flavour entries drop out for the scalar diquark. |
| Text below Eq. (1): "and so do their axial couplings to the vector field `$X$`" | §1.13: "only the **symmetric** part of `$a^{qV}$`, `$b^{qV}$` survives" | **disagree** | The paper says the *axial* (`$b^q_{VR}$`) identical-quark coupling vanishes, so `$b^q_{VR}$` keeps its **antisymmetric** part. `$\bar\psi^c\gamma^\mu\gamma_5\psi$` is symmetric under exchange of the two fermions, not antisymmetric. Only the vector part `$a^q_{VR}$` keeps its symmetric part. The reconstruction applies "symmetric" to both. |
| "+ h.c." at the end of Eq. (1) | h.c. added in §1.9-§1.14 only; §1.7 and §1.8 have no h.c. | **disagree** | In the paper the single "+ h.c." sits after the last line of Eq. (1) and can be read as covering the whole block, including the `$\phi$` and `$V$` flavour-changing terms. The reconstruction excludes those two terms and instead requires `$a^0,a^1$` hermitian and `$b^0,b^1$` anti-hermitian. |
| Kinetic and mass terms for `$\phi$`, `$V$`, `$\chi$` | §1.1 `Lphikin`, §1.2 `LVkin`, §1.3 `Lchikin` | **extra-in-reconstruction** | The paper writes no kinetic terms. The forms used (real scalar, Proca vector, Dirac fermion) are the standard ones and are needed for a working model file. |
| Kinetic and mass terms for `$\varphi$`, `$\tilde\varphi$`, `$X$` | §1.4, §1.5, §1.6 | **extra-in-reconstruction** | Same remark. These terms also fix the QCD pair production of the coloured states, which the paper does not discuss. |
| No anomalous magnetic-moment (`$\kappa$`) operator for `$X$` | §1.6: minimal coupling only, "no extra `$\kappa$` operator" | **extra-in-reconstruction** | The paper is silent. For a massive coloured vector that is not a gauge boson, `$\kappa=1$` (minimal) is a choice, not a consequence. |
| Colour: `$\varphi$`, `$\tilde\varphi$`, `$X$` in the fundamental of `$SU(3)_c$` | Field table: `**3**` for all three | **agree** | The paper also says "(anti-)fundamental" in the earlier section, but Eq. (1) with `$\epsilon^{ijk}$` and `$\bar d^c_j$` fixes the fundamental. |
| Colour: `$\phi$`, `$V$`, `$\chi$` singlets | Field table: singlets | **agree** | Implied by the paper, which calls them neutral missing-energy states. |
| Electric charge `$Q(\varphi)=+2/3$`, `$Q(\tilde\varphi)=-1/3$`, `$Q(X)=+2/3$` | Field table | **agree** (inferred) | The paper never states charges. The values follow from charge conservation in each operator of Eq. (1), and the reconstruction's values are the only consistent set. |
| Spin assignment `$\phi$` 0, `$V$` 1, `$\chi$` 1/2, `$\varphi,\tilde\varphi$` 0, `$X$` 1 | Field table | **agree** | Matches the text above Eq. (1). |
| Nature of `$\chi$` (Dirac or Majorana) | Field table: Dirac, not self-conjugate | **extra-in-reconstruction** | The paper does not fix this. It gives a neutralino (Majorana) and a neutrino as examples, but writes `$\bar d\bar s\to t\bar\chi$` and `$\bar d\bar d\to V\to t\bar\nu$`, which read as Dirac. |
| `$\phi$` and `$V$` real | Field table: self-conjugate | **agree** (implied) | Consistent with the paper writing `$\phi$` and `$V_\mu$` with no dagger in Eq. (1). |
| No `$SU(2)_L$` rep; mass eigenstates | §0 and field table: broken phase, `$SU(3)_C\times U(1)_{em}$` | **agree** | The paper says the effective Lagrangian is written "in terms of mass eigenstates". |
| `$b=\tilde b=0$` at the benchmark | §3: every `b`-type coupling is zero | **agree** | Same statement. |
| `$(a^0_{FC})_{13}=(a^0_{FC})_{31}=0.1$` | `a0FC[1,3]=[3,1]=0.1` | **agree** | |
| `$(a^1_{FC})_{13}=(a^1_{FC})_{31}=0.1$` | `a1FC[1,3]=[3,1]=0.1` | **agree** | |
| `$(a^q_{SR})_{12}=-(a^q_{SR})_{21}=0.1$` | `aqSR[1,2]=+0.1`, `[2,1]=-0.1` | **agree** | Antisymmetric, as required. |
| `$(a^{1/2}_{SR})_3=0.1$` | `ahalfSR[3]=0.1` | **agree** | Third generation (top). |
| `$(a^q_{VR})_{11}=0.1$` | `aqVR[1,1]=0.1` | **agree** | Diagonal, allowed for the vector diquark. |
| `$(a^{1/2}_{VR})_3=0.1$` | `ahalfVR[3]=0.1` | **agree** | |
| `$(\tilde a^q_{SR})_{\{1,2\}3}=0.1$` | `atildeqSR[1,3]=[2,3]=0.1` | **agree** | |
| `$(\tilde a^{1/2}_{SR})_{\{1,2\}}=0.1$` | `atildehalfSR[1]=[2]=0.1` | **agree** | |
| Resonance mass 500 GeV (`$\varphi$`, `$X$`) | `Mvphi=500`, `MX=500` | **agree** | |
| `$M_\varphi=M_{\tilde\varphi}=3$` TeV in the four-fermion limit | `Mvphit=3000`, but `Mvphi=500` | **partly agree** | The file keeps one card. It uses the resonant value for `$\varphi$` and the four-fermion value for `$\tilde\varphi$`. No single paper scenario has both. |
| `$m_\chi=50$` (300) GeV for scalar (vector) resonant production; `$m_\chi=0$` for four-fermion | `Mchi=50` | **partly agree** | Only the scalar-resonant value is in the card. |
| Invisible scalar 300 GeV, invisible vector 50 GeV | `Mphi=300`, `MV=50` | **agree** | Matches the flavour-changing scenarios. |
| Widths of the new states | `Wvphi=50`, `Wvphit=300`, `WX=50`; `Wphi=WV=Wchi=0` | **extra-in-reconstruction** | The paper gives no widths. It only assumes BR(`$\varphi,X\to t\chi$`) = 1. The 10% width choice is an implementation input. |
| PDG codes, LHA block `MONOTOP`, `InteractionOrder {NP,1}` | §3 and field table | **extra-in-reconstruction** | Implementation bookkeeping. No counterpart in the paper. |
| Four-fermion (contact) role of `$\varphi$` and `$\tilde\varphi$` (text below Eq. 1) | §4 describes `$\tilde\varphi$` as a resonance made from a down-type quark and a top | **disagree** (description only) | The paper uses `$\tilde\varphi$` at 3 TeV as a heavy `$s,t,u$`-channel exchange that produces the four-fermion operator, with a PDF-enhanced `$dd$`-type initial state. The reconstruction's summary reads it as on-shell resonant production. |

---

## 3. Disagreements, with severity

1. **Exchange symmetry of the axial diquark coupling `$b^q_{VR}$` (§1.13).**
   *Severity: substantive.*
   A human should check the sign rule `$\bar\psi^c_1\Gamma\psi_2=\eta_\Gamma\,\bar\psi^c_2\Gamma\psi_1$`
   (`$\eta=+1$` for `$1$`, `$\gamma_5$`, `$\gamma^\mu\gamma_5$`; `$\eta=-1$` for `$\gamma^\mu$`,
   `$\sigma^{\mu\nu}$`), because the paper's sentence "and so do their axial couplings to the vector
   field `$X$`" requires `$b^q_{VR}$` to keep its **antisymmetric** flavour part, while the
   reconstruction claims the symmetric part. The error is inert at this benchmark, where
   `$b^q_{VR}=0$`, but it would matter at any point with a non-zero axial diquark coupling.

2. **Scope of the "+ h.c." in Eq. (1) (§1.7, §1.8).**
   *Severity: substantive.*
   A human should check whether the implementation intends the `$\phi\bar u u$` and
   `$V_\mu\bar u\gamma^\mu u$` terms to carry the h.c. too, because adding it would double both
   flavour-changing vertices and change those cross sections by about a factor of four.

3. **Single parameter card mixes the paper's scenarios (masses).**
   *Severity: convention.*
   A human should check which of the five paper scenarios the card is meant to reproduce, because
   `$M_\varphi=500$` GeV (resonant) sits next to `$M_{\tilde\varphi}=3$` TeV (four-fermion) and
   `$m_\chi=50$` GeV, a combination that no single scenario in the paper uses.

4. **Widths of the coloured states are invented.**
   *Severity: convention.*
   A human should check the 10%-of-mass widths (`$\Gamma=50$`, 50, 300 GeV) against the paper's
   assumption BR(`$\varphi,X\to t\chi$`) = 1, because the paper fixes a branching ratio but no width,
   and a wrong width changes the resonant line shape and the narrow-width normalisation.

5. **Minimal coupling assumed for the coloured vector `$X$` (§1.6).**
   *Severity: convention.*
   A human should check whether `$\kappa=1$` (no extra chromo-magnetic operator, field strength built
   from the covariant derivative) is what the authors used, because the paper says nothing about the
   `$X$` kinetic term and the QCD pair-production rate of `$X$` depends on this choice.

6. **Dirac nature of `$\chi$`.**
   *Severity: convention.*
   A human should check whether `$\chi$` is Dirac or Majorana, because the paper is silent and the
   choice changes the resonance partial width and the number of contributing final states, although
   the paper's own notation `$t\bar\chi$` favours Dirac.

7. **Phenomenology description of `$\tilde\varphi$` (§4).**
   *Severity: cosmetic.*
   A human should check the production description, because the reconstruction presents
   `$\tilde\varphi$` as an on-shell resonance made with a top in the initial state, while the paper
   uses it only in the heavy-mass four-fermion limit with light-quark initial states. This is a
   narrative point; no Lagrangian term is affected.

8. **Standard Model part absent.**
   *Severity: cosmetic.*
   A human should check that the SM is loaded from a separate file, because Eq. (1) starts with
   `$\lag_{SM}$` and the reconstruction covers only the new sector.

---

## 4. Overall assessment

The reconstruction reproduces every interaction operator of Eq. (1) with the correct field content,
colour structure, conjugation pattern and Dirac structure. All eight interaction terms map one to one
onto the paper, the `$\epsilon^{ijk}$` contractions and the charge-conjugated down-type bilinears are
right, and the electric charges `$+2/3$`, `$-1/3$`, `$+2/3$` for `$\varphi$`, `$\tilde\varphi$`, `$X$`
are the unique set that makes Eq. (1) charge-conserving, even though the paper never prints them.
Every numerical coupling in the reconstruction matches the paper's benchmark list, including the
antisymmetric pair `$(a^q_{SR})_{12}=-(a^q_{SR})_{21}$` and the vanishing of all `$b$`-type couplings.
The kinetic and mass terms, the widths, the PDG codes and the LHA block are additions with no
counterpart in the paper; they are needed for a runnable file, but the `$X$` kinetic term and the
widths encode choices the paper does not fix. Two items need real attention. First, the statement in
§1.13 about which flavour part of the axial vector-diquark coupling survives contradicts the paper's
own sentence below Eq. (1), and the exchange-symmetry sign used there is wrong for
`$\gamma^\mu\gamma_5$`; the benchmark hides this because `$b^q_{VR}=0$`. Second, the reconstruction
restricts the "+ h.c." of Eq. (1) to the diquark and `$\chi$` terms, which is a defensible reading but
not the only one, and the alternative reading changes the flavour-changing rates by a factor of about
four. The mass card also blends the paper's resonant and four-fermion scenarios into one point, which
a reviewer should map back to a named scenario before comparing any cross section.
