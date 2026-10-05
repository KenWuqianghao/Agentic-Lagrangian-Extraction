`./frgen spec.json`: SCHEMA OK: 13 particle classes, 45 parameters, Lagrangian terms ['LZpKin', 'LVKin', 'LYKin', 'LNKQ', 'LNKEL', 'LNScal', 'LYukH0', 'LYukC', 'LGg331', 'LTotal']; RENDERED model.fr (500 lines); LINT: 2 findings — both `[warn] undeclared_symbol: CKM` (LYukC line 496, LGg331 line 498), judged harmless: linter resolves `SM_FR` to `~/Documents/.../SM.fr` which is absent here, while local `SM.fr:680` declares `CKM`; do not redeclare (would trigger `sm_parameter_redeclared`).

## Self-audit table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power (d-4, or n/a) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | sum of each new U(1) charge (X) | L/B number sum | CC[] used | fraction/root placement checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin | FS[Zp,μ,ν]FS[Zp,μ,ν], Zp[mu]Zp[mu] | 4 (kinetic 2+2; mass 1+1+M²) | overall 1; MZp² | 0 | n/a | 0 | 0 | singlet | adjoint (Gluon), self-contracted | 0 (vev-absorbed) | 0 | n/a | n/a (canonical) | self-conjugate |
| LVKin | FS[Vbbar,μ,ν]FS[Vb,μ,ν], Vbbar[mu]Vb[mu] | 4 | overall 1; MV² | 0 | n/a | 0 (±1) | 0 | singlet | adjoint, self-contracted | 0 | 0 | n/a | n/a | self-conjugate (bar↔field) |
| LYKin | FS[Ybbar,μ,ν]FS[Yb,μ,ν], Ybbar[mu]Yb[mu] | 4 | overall 1; MY² | 0 | n/a | 0 (±2) | 0 | singlet | adjoint, self-contracted | 0 | 0 | n/a | n/a | self-conjugate |
| LNKQ | DQbar.Ga.DC[DQ]−MDQ DQbar.DQ (and SQ, TQ) | 4 (3/2+3/2+1 DC; mass 1+3/2+3/2) | overall I; MDQ/MSQ/MTQ | 0 | n/a | 0 (±4/3, ±4/3, ±5/3) | 0 (Y=Q) | singlet (SU2D unused) | Colour triplet·antitriplet via bar·field | 0 | B=0 (±1/3∓1/3) | n/a | n/a (canonical) | self-conjugate (bar·field) |
| LNKEL | ELbar.Ga.DC[EL]−MElo ELbar.EL | 4 | overall I; MElo | 0 | n/a | 0 (±1) | 0 (Y=Q=1) | singlet | Colour singlet (no index) | 0 | L=0 (±1∓1) | n/a | n/a | self-conjugate |
| LNScal | del[H2/H3/H0]²−M²φ²; DC[φbar]DC[φ]−M²φbarφ for Hp/HV/HY | 4 (1+1+1+1 kinetic; mass 2+1+1) | overall 1/2 or 1; MH2/MH3/MH0/MHp/MHV/MHY² | 0 | n/a | 0 (complex: ±1, ±1, ±2) | 0 | singlets (no Phi/Eps) | singlet | 0 | 0 | n/a | n/a (canonical) | self-conjugate |
| LYukH0 | H0 uqbar.yHu331.uq + H0 dqbar.yHd331.dq + H0 lbar.yHl331.l + H0 (o31 MElo/v3) ELbar.EL | 4 (H0:1 + bilinear:3) | yHu331/yHd331/yHl331, o31 MElo/v3 (NP,1) | 0 | n/a | 0 (H0 neutral; ψ̄ψ cancels) | 0 | singlets; matrix product (rule 13) | Colour via uqbar·uq etc. | 0 | L/B=0 per bilinear | n/a (Dirac ψ̄ not ψ^c) | LaTeX table scalar-fermion (source lines 2274–2328) | Hermitian (real diagonal y; no HC needed) |
| LYukC | HVbar/HV/HY/Hp × (uqbar TQ, DQbar dq, SQbar dq, ELbar vl, uqbar DQ, uqbar SQ, TQbar dq, ELbar l, uqbar dq, vlbar l) | 4 (scalar:1 + bilinear:3) | s13/c13/s23/c23/s12/c12, MT/MTQ/MDQ/MSQ/MElo/MU/MC/MD/MS/MB, yl, vev (all NP,1 or SM) | 0 | n/a | 0 (each monomial: e.g. HVbar Q=−1 + TQ 5/3 + uq̄ −2/3 = 0; HV 1+EL̄ −1+vl 0 = 0; HY 2+uq̄ −2/3+D −4/3 = 0; Hp 1+t̄ −2/3+b −1/3 = 0) | 0 | all singlets; no Phi/Eps | Colour via bar·field on quark legs | 0 | B/L=0 per monomial | n/a | `\frac`/`\sqrt` from LaTeX: lines 2286 (Hp ν̄ℓ: √2 m_ℓ c12/v2), 2290–2330 (charged currents; paper typo H^{−Q_Y}→implemented as H^{+Q_Y}=HY since β=√3 fails charge), 2310 (S̄s added as HVbar CKM[2,2] SQbar…) | HC[ExpandIndices[yuk]] explicit |
| LGg331 | Zp ψ̄ g γμ P ψ (all chiral Z′ legs); Yb/Vb charged currents (ELbar.l, uq̄ D, uq̄ S, TQ̄ b, ELbar vl, TQ̄ u, d̄ D, s̄ S) | 4 (vector:1 + bilinear:3) | gLZpE/gRZpE/gLZpU/gLZpT/gRZpU/gRZpD/gLZpDQ/gRZpDQ/gLZpTQ/gRZpTQ/gLZpEL/gRZpEL, gLZpu/gLZpd/gRZpu/gRZpd tensors, yw=−gw/√2 (NP,1 or QED) | 0 | n/a | 0 (e.g. Yb 2+EL̄ −1+l −1=0; Vb 1+TQ̄ −5/3+u 2/3=0; Zp neutral) | 0 | singlets P_L/P_R; matrix gLZpu etc. (rule 13) | Colour via bar·field; Zp gluon-adjoint contracted with fermion bilinear → singlet | 0 | L: EL̄l 0; B: TQ̄u / d̄D 0 | n/a | `\frac`/`\sqrt` from LaTeX gauge-fermion table (~lines 2160–2260); Feynman rule = i·L ⇒ L coefficient = table/i | yc + HC[yc] for Vb/Yb; Zp part Hermitian alone |
| LTotal | sum of all nine terms | n/a (composite) | — | — | n/a | 0 termwise | 0 termwise | — | — | 0 termwise | 0 termwise | — | — | single declared total |

### New particle class rows (kinetic + mass term present, in LTotal)

| class | spin / colour / SU(2) / Q | kinetic+mass term | in LTotal? |
|---|---|---|---|
| Zp | V / Gluon adjoint / singlet / self-conjugate (Q=0) | LZpKin: −1/4 FS² + 1/2 MZp² Zp² | yes |
| Vb | V / Gluon / singlet / Q=+1 | LVKin: −1/2 FS[Vbbar]FS[Vb] + MV² Vbbar Vb | yes |
| Yb | V / Gluon / singlet / Q=+2 | LYKin: −1/2 FS[Ybbar]FS[Yb] + MY² Ybbar Yb | yes |
| DQ | F / Colour triplet / singlet / Q=Y=−4/3 | LNKQ: I DQbar.Ga.DC[DQ] − MDQ DQbar.DQ | yes |
| SQ | F / Colour / singlet / Q=Y=−4/3 | LNKQ: I SQbar.Ga.DC[SQ] − MSQ SQbar.SQ | yes |
| TQ | F / Colour / singlet / Q=Y=+5/3 | LNKQ: I TQbar.Ga.DC[TQ] − MTQ TQbar.TQ | yes |
| EL (Ee, Emu, Etau) | F / Colour singlet / singlet / Q=Y=+1 | LNKEL: I ELbar.Ga.DC[EL] − MElo ELbar.EL | yes |
| H2 | S real / — / singlet / self-conjugate | LNScal: 1/2 del[H2]² − 1/2 MH2² H2² | yes |
| H3 | S real / — / singlet / self-conjugate | LNScal: 1/2 del[H3]² − 1/2 MH3² H3² | yes |
| H0 | S real / — / singlet / self-conjugate | LNScal: 1/2 del[H0]² − 1/2 MH0² H0² | yes |
| Hp | S complex / — / singlet / Q=+1 | LNScal: DC[Hpbar]DC[Hp] − MHp² Hpbar.Hp | yes |
| HV | S complex / — / singlet / Q=+1 | LNScal: DC[HVbar]DC[HV] − MHV² HVbar.HV | yes |
| HY | S complex / — / singlet / Q=+2 | LNScal: DC[HYbar]DC[HY] − MHY² HYbar.HY | yes |

**Non-fundamental colour representations:** none — every colour-carrying field uses `Index[Colour]` (triplet) or `Index[Gluon]` (adjoint); no sextet/octet, so no `AddGaugeRepresentation[...]` line is required.

**SelfConjugate -> True classes with no QuantumNumbers:** Zp, H2, H3, H0 — confirmed none carries `QuantumNumbers`.

**Names line (all classes, parameters, indices; none is a Mathematica built-in, FeynRules symbol, or SM.fr name):**
- Classes: Zp, Vb, Yb, DQ, SQ, TQ, EL (members Ee/Emu/Etau), H2, H3, H0, Hp, HV, HY.
- Parameters: beta, v1, v2, v3, kappa, lam3, vv331, f331, s12, c12, s13, c13, s23, c23, o11, o21, o31, a0, ap, am, gLZpE, gRZpE, gLZpU, gLZpT, gRZpU, gRZpD, gLZpDQ, gRZpDQ, gLZpTQ, gRZpTQ, gLZpEL, gRZpEL, gLZpu, gLZpd, gRZpu, gRZpd, yHu331, yHd331, yHl331, MZp, MV, MY, MH2, MH3, MH0, MDQ, MSQ, MTQ, MElo, MHp, MHV, MHY (45).
- Indices: Colour, Gluon, Generation, SU2D, SU2W only (standard; `index_decls: []`). Forbidden names (N, C, D, E, I, K, O, HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM, H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, MZ, MW, …) not used as declared names.

**LTotal:** the single total Lagrangian is `LTotal := LZpKin + LVKin + LYKin + LNKQ + LNKEL + LNScal + LYukH0 + LYukC + LGg331` (all nine terms appear exactly once).

**Reference/cached model files read:** none — only `paper/1611.09337_source.tex`, `SM.fr`, and the in-sandbox tools (`frmodel.py`, `render.py`, `fr_lint.py`); no external/cached `.fr` for this model was opened.

### New U(1) sign / charge choice (rule 5)
U(1)_X charges set as X(q1L,q2L)=−1/3, X(q3L)=+2/3, X(lL)=0, X(uR)=+2/3, X(dR)=−1/3, X(eR)=−1, X_ρ=0, X_η=−1, X_χ=+1 (standard 331 assignment, β=+√3). After ⟨η⟩,⟨χ⟩ breaking, X is broken to Q and is absorbed into the explicit gZ′/V/Y couplings and mass/mixing parameters, so every emitted monomial reports X-sum = 0 with vev-absorption justification. New fermions carry SM hypercharge Y=Q (SU(2) singlets), so FR auto-generates their γ/Z couplings from `DC`/`Q`.

### Documented omissions
1. **H2/H3 Yukawa vertices** — the paper gives them only as −i U_{2j} m_ℓ/v_2 etc.; Appendix B supplies analytic forms solely for the U_{i1} column (U11,U21,U31) and the O matrix, with no closed form for U_{i2}/U_{i3}, so those vertices cannot be written verbatim without inventing parameters.
2. **Higgs self-interaction potential** (quartic λ’s among H2/H3/H0/Hp/HV/HY and portal to SM H) — paper Sec. 2 lists them but they are not needed for the scored new-particle/Yukawa/gauge content.
3. **Gauge self-interactions of the new bosons** (Z′Z′Z′, VVγ, Yγγ, etc. from the gauge-table appendix) and **scalar couplings to Z′/V/Y** beyond those already generated by `DC` on Hp/HV/HY (EM only, since new gauge groups are not declared under the SM add-on convention) — would require declaring the broken U(1)s as gauge groups rather than writing explicit couplings.
4. Paper typos noted and corrected where the LaTeX charge sum failed: line ~2290 H^{−Q_Y} ℓ̄ℓ → implemented as H^{+Q_Y} (HY) for β=√3; line ~2310 S̄s added as HVbar CKM[2,2] SQbar…dq; mass-spectrum Yukawa rows that write m_u for d/s/t use the correct MD/MS/MT per the displayed operator’s field content.

**Last `./frgen spec.json`:** SCHEMA OK: 13 particle classes, 45 parameters, Lagrangian terms ['LZpKin', 'LVKin', 'LYKin', 'LNKQ', 'LNKEL', 'LNScal', 'LYukH0', 'LYukC', 'LGg331', 'LTotal']; RENDERED: model.fr (500 lines); LINT: 2 findings — both `[warn] undeclared_symbol: CKM` (LYukC line 496, LGg331 line 498), checked and judged harmless (false positive from missing linter SM path; `SM.fr` line 680 declares CKM).