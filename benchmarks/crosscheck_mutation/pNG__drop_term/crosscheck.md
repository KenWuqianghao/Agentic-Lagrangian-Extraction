# Cross-check: `reconstruction.md` against the pNG DM paper

RUN-TAG: XM-CROSS-pNG__drop_term

Paper: *Global fit of pseudo-Nambu-Goldstone Dark Matter*, Arina, Beniwal, Degrande,
Heisig, Scaffidi (arXiv:1912.04008).

## 0. Where the paper defines the model

- **Section 2** ("Pseudo-Nambu-Goldstone Dark Matter") holds the full model definition.
  - Eq. (2.1): `L = L_SM + L_S + L_soft`.
  - Eq. (2.2): `L_S = (∂S)*(∂S) + (μ_S²/2)|S|² − λ_ΦS Φ†Φ|S|² − (λ_S/2)|S|⁴`.
  - Eq. (2.3): `L_soft = (μ_S'²/4)(S² + S*²)`.
  - Eq. (2.4): the global dark `U(1)`, `S → e^{iα}S`; eq. (2.5): the dark `CP`, `S → S*`.
  - Eq. (2.6)–(2.7): the scalar potential, `V = V_SM + V_S + V_soft`.
  - Eq. (2.8): `Φ = (0, v_h+φ)/√2` (unitary gauge) and `S = (v_s + s + iχ)/√2`.
  - Eq. (2.9)–(2.10): the two stationary-point (tadpole) conditions.
  - Eq. (2.11)–(2.15): the CP-even mass matrix, the rotation `O`, `tan 2θ`, and the
    eigenvalues `m_h`, `m_H`.
  - Eq. (2.17): the four free parameters `{m_χ, v_s, θ, m_H}`.
  - Eq. (2.18)–(2.20): `λ_Φ`, `λ_S`, `λ_ΦS`, `μ_S'²`, `μ_Φ²`, `μ_S²` as functions of the
    free parameters.
- **Appendix A** ("Dark matter-nucleon coupling") gives the DM trilinear couplings.
  - Eq. (A.1)–(A.2): `L_S ⊃ −½ χ² (λ_ΦS v_h φ + λ_S v_s s)`.
  - Eq. (A.3): `(φ, s)ᵀ = ((cosθ, sinθ), (−sinθ, cosθ)) (h, H)ᵀ`.
  - Eq. (A.4)–(A.6): `L_S ⊃ −½ χ² (κ_χχh h + κ_χχH H)`, with
    `κ_χχh = −m_h² sinθ / v_s` and `κ_χχH = +m_H² cosθ / v_s`.
  - Eq. (A.7)–(A.9): the scalar couplings to SM fermions, rescaled by `cosθ` (`h`) and
    `sinθ` (`H`).
- **Section 3.3** gives the two invisible widths `Γ(h→χχ)` and `Γ(H→χχ)`.
- **Section 3.5** gives the universal `cos²θ` suppression of `h` production and the extra
  `h → HH` decay mode in the total width.

Symbol map used below: paper `H` = reconstruction `H2`; paper `v_h` = reconstruction `v`;
paper `φ`, `s` = reconstruction `φ₁`, `s₁`; paper `m_χ` = reconstruction `Mx`.

## 1. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
| --- | --- | --- | --- |
| `L_SM` (eq. 2.1) | `LSM` added through `LTotal` (§1.5) | **agree** | Both take the SM Lagrangian from outside the new-physics file. See the separate coupling-rescaling rows below. |
| `(∂_μ S)*(∂^μ S)` → `½(∂χ)²` (eq. 2.2 with eq. 2.8) | `½ ∂_μχ ∂^μχ` in `LX` (§1.1) | **agree** | Real-scalar normalisation is correct for a self-conjugate field. |
| `(∂_μ S)*(∂^μ S)` → `½(∂s)²` (eq. 2.2 with eq. 2.8) | `½ ∂_μH₂ ∂^μH₂` in `LH2` (§1.2) | **agree** | Convention difference only. The reconstruction writes the kinetic term in the mass basis. The rotation `O` is orthogonal, so `½(∂h)² + ½(∂H₂)² = ½(∂φ)² + ½(∂s)²`. |
| `χ` mass: `m_χ² = μ_S'²` from `(μ_S²/2)\|S\|²`, the quartics and `L_soft` (eqs. 2.2, 2.3, 2.10, 2.18) | `−½ M_χ² χ²` in `LX`, `Mx` external (§1.1) | **agree** | Same physics content. The paper builds `m_χ` from the soft `U(1)`-breaking parameter; the reconstruction uses the physical mass directly. The reconstruction states this correctly in §1.6. |
| `H` mass eigenvalue `m_H` (eq. 2.15) | `−½ M_{H₂}² H₂²` in `LH2`, `MH2` external (§1.2) | **agree** | The paper also treats `m_H` as a free input (eq. 2.17). |
| `−λ_ΦS Φ†Φ\|S\|² ⊃ −½ λ_ΦS v_h φ χ²` (eqs. A.1, A.2) | `−½ λ_ΦS v φ₁ χ²` in `LPortal3` (§1.3) | **agree** | Identical coefficient and identical field direction. |
| `−(λ_S/2)\|S\|⁴ ⊃ −½ λ_S v_s s χ²` (eqs. A.1, A.2) | `−½ λ_S v_s s₁ χ²` in `LPortal3` (§1.3) | **agree** | Identical coefficient and identical field direction. |
| Rotation `(φ, s) → (h, H)` (eqs. 2.13, A.3) | `φ₁ = cosθ h + sinθ H₂`, `s₁ = −sinθ h + cosθ H₂` (§1.3) | **agree** | Same matrix, same angle convention, same sign of `sinθ`. |
| `λ_ΦS = (m_H² − m_h²) sinθ cosθ / (v_h v_s)` (eq. 2.20) | `lamPS` (§3.2) | **agree** | Identical. |
| `λ_S = (m_h² sin²θ + m_H² cos²θ)/v_s²` (eq. 2.19) | `lamS` (§3.2) | **agree** | Identical. |
| `λ_Φ = (m_h² cos²θ + m_H² sin²θ)/v_h²` (eq. 2.18) | — | **missing-in-reconstruction** | The doublet quartic is not re-fixed. The reconstruction keeps the SM-file value, which is `m_h²/v_h²`. The two agree only at `θ = 0` or `m_H = m_h`. |
| `κ_χχh = −m_h² sinθ / v_s` (eq. A.5) | `+ (m_h² sinθ / 2 v_s) χ² h` (§1.4) | **agree** | Same sign and same size, because `L ⊃ −½ κ_χχh χ² h`. The value also reproduces `Γ(h→χχ) = m_h³ sin²θ β /(32π v_s²)` of section 3.3. |
| `κ_χχH = +m_H² cosθ / v_s` (eq. A.6) | `− (m_{H₂}² cosθ / 2 v_s) χ² H₂` (§1.4) | **agree** | Same sign and same size. It reproduces `Γ(H→χχ)` of section 3.3. |
| `μ_Φ²`, `μ_S²` and the tadpole conditions (eqs. 2.9, 2.10, 2.19, 2.20) | — | **missing-in-reconstruction** | These are eliminated at the minimum. Their absence is expected in a mass-basis implementation. |
| `−(λ_ΦS/4) φ² χ²` from `−λ_ΦS Φ†Φ\|S\|²` (eq. 2.2) | — | **missing-in-reconstruction** | The `χχhh`, `χχhH` and `χχH₂H₂` contact vertices from the Higgs-portal quartic. §1.6 states that no such term is present. |
| `−(λ_S/4) s² χ²` from `−(λ_S/2)\|S\|⁴` (eq. 2.2) | — | **missing-in-reconstruction** | The second source of the same contact vertices. §1.6 states it is absent. |
| `−(λ_S/8) χ⁴` from `−(λ_S/2)\|S\|⁴` (eq. 2.2) | — | **missing-in-reconstruction** | DM self-interaction. §1.6 states it is absent. |
| Scalar self-interactions `φ³, φ²s, φs², s³` and the quartics from `V_SM + V_S` (eqs. 2.2, 2.6, 2.7) | — | **missing-in-reconstruction** | These give the `hhh`, `hhH`, `hHH`, `HHH` vertices. The paper needs them for `h → HH` (section 3.5) and for `χχ → hh, hH, HH` (section 3.2). |
| `(v_s + s)² ` part of `L_soft`, i.e. `+(μ_S'²/4)(v_s+s)²` (eq. 2.3) | — | **missing-in-reconstruction** | It shifts the `s` mass term and the `s` tadpole. It is absorbed in the mass basis, so it is bookkeeping only. |
| `κ_hff = (m_f/v_h) cosθ` (eq. A.8) | — | **missing-in-reconstruction** | The reconstruction keeps the SM Yukawa couplings of `h` unchanged, with no `cosθ` factor. |
| `κ_Hff = (m_f/v_h) sinθ` (eq. A.8) | — | **missing-in-reconstruction** | In the reconstruction `H₂` is a pure gauge singlet with no coupling to SM fermions. |
| `hVV` and `HVV` couplings rescaled by `cosθ` and `sinθ` (section 3.5, `σ(pp→h) = cos²θ σ_SM`) | — | **missing-in-reconstruction** | The reconstruction states that `LSM` is inherited unchanged and that the new sector is neutral under `SU(3)×SU(2)×U(1)`. |
| Dark `Z₂ ⊗ CP`; `χ → −χ` makes `χ` stable (eqs. 2.4, 2.5, section 2) | `χ` has `Width → 0` and no decay operator (§2) | **agree** | Same outcome by a different route. The file enforces stability by hand, not by a declared symmetry. |
| Free parameters `{m_χ, v_s, θ, m_H}` (eq. 2.17) | External `vs`, `thx`; masses `Mx`, `MH2` (§3.1, §2) | **agree** | Same four inputs. |
| — | `S[103] = φ₁`, `S[104] = s₁`, `Unphysical → True` (§2) | **extra-in-reconstruction** | Implementation devices, not new physics. FeynRules substitutes their definitions before vertex extraction. |
| — | `PDG 52` (`χ`), `PDG 35` (`H₂`), `WH2` (§2) | **extra-in-reconstruction** | Bookkeeping for the UFO output. The paper fixes no PDG codes. |
| Best-fit point: `m_χ = 62.573` GeV, `θ = 1.53` rad, `m_H = 125.30` GeV, `v_h/v_s = 0.0187` (table 3, column 1) | `Mx = 62.573`, `thx = 1.53`, `MH2 = 125.30`, `vs = 13155.1` GeV (§2, §3.1) | **agree** | `246/0.0187 = 13155` GeV. The numerical values are the paper's global-fit best-fit point. |

## 2. Disagreements, with severity

1. **Missing quartic portal `χ²φ²` and `χ²s²` (substantive).**
   The paper's eq. (2.2) contains `λ_ΦS Φ†Φ|S|²` and `(λ_S/2)|S|⁴` in full. Expanding
   them gives contact vertices `χχhh`, `χχhH` and `χχHH` with coefficients fixed by the
   same `λ_ΦS` and `λ_S`. The reconstruction keeps only the trilinear part of the same
   two operators and says in §1.6 that no quartic portal is present.
   *Human check:* confirm whether the implementation file really dropped the quartic part
   of eqs. (2.2)/(A.1), because these vertices enter `χχ → hh, hH, HH` directly and that
   channel sets the relic density in one of the paper's two favoured regions (section 4.1,
   item 2).

2. **Missing `χ⁴` self-interaction (substantive, low phenomenological weight here).**
   `−(λ_S/2)|S|⁴` also gives `−(λ_S/8)χ⁴`. It does not change the observables in the
   paper's fit, but it is part of the model.
   *Human check:* verify that the omission is deliberate and not a sign that the whole
   `|S|⁴` operator was truncated to its trilinear piece.

3. **Missing scalar self-interactions of `h` and `H` (substantive).**
   The paper uses `Γ(h → HH)` in the total width (section 3.5) and `χχ → hh, hH, HH`
   with `t`- and `u`-channel `χ` exchange plus scalar exchange (section 3.2). The
   reconstruction has no `hhh`, `hhH`, `hHH` or `HHH` vertex.
   *Human check:* look for a separate potential block in the implementation file; if there
   is none, the file cannot reproduce the paper's Higgs-pair results.

4. **Missing `cosθ`/`sinθ` rescaling of the scalar couplings to SM fermions and gauge
   bosons (substantive).**
   Eq. (A.8) and section 3.5 require `h` couplings scaled by `cosθ` and `H` couplings
   scaled by `sinθ`. The reconstruction says `LSM` is unchanged and `H₂` is a total
   singlet, so `H₂` has no tree-level coupling to SM matter at all.
   *Human check:* this is the most important item. Without it the file has no
   `H₂ → b b̄`, no `H₂` production, and no tree-level DM-nucleon amplitude, so the
   momentum-suppression argument of appendix A cannot even be tested in the file. Confirm
   whether the doublet direction `φ₁` was meant to replace the SM Higgs field inside
   `LSM`.

5. **`λ_Φ` not re-fixed (substantive).**
   Eq. (2.18) sets `λ_Φ = (m_h² cos²θ + m_H² sin²θ)/v_h²`. The reconstruction keeps the SM
   value. At the quoted benchmark `θ = 1.53` the two differ by a large factor.
   *Human check:* check the `h` mass and the `h` self-couplings that the file actually
   produces against eq. (2.15).

6. **Internal consistency of the trilinear cancellation claim (convention).**
   §1.4, point 2 of the reconstruction says the zero-momentum DM-nucleon amplitude cancels.
   The paper reaches the same conclusion (appendix A, final equations), but the
   cancellation needs the `cosθ` and `sinθ` factors on the fermion side from eq. (A.8).
   Those factors are absent in the reconstruction.
   *Human check:* the claim is right for the paper's model, but it is not a property the
   reconstructed file can produce on its own.

7. **Identification of `h` and `H₂` at `θ = 1.53` (convention).**
   The reconstruction says `H₂` is almost pure doublet and `h` almost pure singlet. The
   paper fixes `m_h = 125` GeV and calls `h` "a SM-like Higgs" (eq. 2.16), while allowing
   `θ` up to `π/2` when `m_H ≃ m_h` (section 4.1). The two statements are consistent at
   this near-degenerate benchmark, but the words "SM-like" swap between the two documents.
   *Human check:* confirm which state the file gives the SM gauge and Yukawa couplings to.

8. **Notation and bookkeeping (cosmetic).**
   `H` vs `H₂`, `v_h` vs `v`, `m_χ` vs `Mx`; the paper's `μ_Φ²`, `μ_S²`, `μ_S'²` and the
   tadpole conditions are absent because the reconstruction works in the mass basis; the
   `NP` interaction order and the PDG codes have no counterpart in the paper.
   *Human check:* none needed.

## 3. Overall assessment

Everything the reconstruction does contain matches the paper closely. The field content
(one real DM scalar `χ` plus one extra CP-even scalar), the mixing convention, the two
derived couplings `λ_ΦS` and `λ_S`, the trilinear portal `−½χ²(λ_ΦS v_h φ + λ_S v_s s)`,
and the mass-basis couplings `+m_h² sinθ/(2v_s) χ² h` and `−m_H² cosθ/(2v_s) χ² H₂` agree
term by term and sign by sign with eqs. (2.2), (2.13), (2.19), (2.20) and (A.2)–(A.6). The
benchmark numbers are the paper's global-fit best-fit point in table 3. The gap is on the
other side: the reconstruction describes a Lagrangian that keeps only the trilinear part of
the two quartic operators in eq. (2.2), and it keeps the SM sector untouched. As a result
the contact vertices `χχhh`, `χχhH`, `χχHH`, the `χ⁴` term, the `h`/`H` self-couplings,
the `λ_Φ` relation of eq. (2.18), and the `cosθ`/`sinθ` rescaling of the scalar couplings
to SM fermions and gauge bosons (eq. A.8, section 3.5) all have no counterpart. The
reconstruction itself flags most of these absences in its §1.6, which suggests it reports
the file faithfully and that the file, not the reconstruction, is the shorter object. A
human reviewer should decide whether the implementation file was a deliberately reduced
"trilinear-portal only" version, or whether one or more terms of eq. (2.2) were lost.
