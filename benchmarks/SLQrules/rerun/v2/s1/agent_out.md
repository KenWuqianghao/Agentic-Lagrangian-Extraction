I'll start by reading the paper and the schema.
Let me continue reading the key sections.
Let me read the appendix on charge-conjugate fermions and the LQ-fermion Feynman rules.
I've read the paper (Secs. 2–4 and the model-file listings), the schema, and `SM.fr`. No cached or reference `.fr` file for SLQrules was opened.

## Model content extracted

Five scalar-leptoquark SU(2) multiplets (Eq. 22) → **9 colour-triplet complex scalar mass eigenstates** (Eqs. 23, 26): three with Q=−1/3, three with Q=+2/3, two with Q=−4/3, one with Q=+5/3, plus the five unphysical multiplets Φ₁, Φ₁̃, Φ₂, Φ₂̃, Φ₃ that carry the Lagrangian and are rotated into the mass basis by W^q (Eqs. 29–30, 50).

## Mandatory self-audit table

Charges below use SM.fr conventions: `Phi` Y=+1/2, `LL` Y=−1/2, `QL` Y=+1/6, `uR` +2/3, `dR` −1/3, `lR` −1. LQ hypercharges: S1m13 −1/3, S1tm43 −4/3, R2 +7/6, R2t +1/6, S3 −1/3. **There is no new U(1)**, so the "new U(1) sum" column is n/a for every row. Every term is written in the unphysical (SU(2)-multiplet) basis, so a vanishing Y sum on an SU(2)-singlet contraction implies a vanishing Q sum; I list Q sum = 0 accordingly.

| term name | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L/B sum | CC[] used | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LQ2PhiDiag r1 | S1m13bar·S1m13 | 2 | m1^2 | 2 | n/a | 0 | −1/3+1/3=0 | singlet×singlet | 3̄⊗3 shared `c1` | n/a | n/a | n/a | self-conj (real) |
| LQ2PhiDiag r2 | S1tm43bar·S1tm43 | 2 | m1t^2 | 2 | n/a | 0 | 0 | singlet | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r3 | R2bar[a1]·R2[a1] | 2 | m2^2 | 2 | n/a | 0 | 0 | shared SU2D `a1` | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r4 | R2tbar[a1]·R2t[a1] | 2 | m2t^2 | 2 | n/a | 0 | 0 | shared SU2D `a1` | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r5 | S3bar[b1]·S3[b1] | 2 | m3^2 | 2 | n/a | 0 | 0 | shared SU2W `b1` | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r6–10 | Phibar[a1]Phi[a1]·Φa†Φa | 4 | Y1,Y1t,Y2,Y2t,Y3 | 0 | n/a | 0 | 1/2−1/2+0=0 | two shared SU2D/SU2W pairs | shared `c1` | n/a | n/a | n/a | self-conj (Y real) |
| LQ2PhiDiag r11 | Phibar Eps R2bar Phi Eps R2 | 4 | Y22 | 0 | n/a | 0 | (−1/2−7/6)+(1/2+7/6)=0 | `Eps[a1,a2]`, `Eps[a3,a4]` (Hᵀiσ₂Φ₂ and h.c.) | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r12 | Phibar Eps R2tbar Phi Eps R2t | 4 | Y2t2t | 0 | n/a | 0 | 0 | two `Eps[·,·]` | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r13 | Eps[b1,b2,b3] Phibar·2Ta·Phi·S3bar S3 | 4 | Y33 | 0 | n/a | 0 | −1/2+1/2+1/3−1/3=0 | `Ta[b1,a1,a2]` + SU2W `Eps[b1,b2,b3]` | shared `c1` | n/a | n/a | n/a | self-conj (I·Y33 real ⇒ herm.) |
| LQ2PhiMix A12t | R2tbar Phi S1m13 | 3 | A12t | 1 (GeV) | n/a | 0 | −1/6+1/2−1/3=0 | shared SU2D `a1` | shared `c1` | n/a | n/a | n/a | `HC[LQ2PhiMixNonHC]` |
| LQ2PhiMix A2t3 | R2tbar·2Ta·Phi·S3 | 3 | A2t3 | 1 (GeV) | n/a | 0 | −1/6−1/3+1/2=0 | `Ta[b1,a1,a2]` | shared `c1` | n/a | n/a | n/a | HC[] |
| LQ2PhiMix Y22t | R2bar Phi · Phi Eps R2t | 4 | Y22t | 0 | n/a | 0 | −7/6+1/2+1/2+1/6=0 | shared `a1`; `Eps[a2,a3]` | shared `c1` | n/a | n/a | n/a | HC[] |
| LQ2PhiMix Y1t3 | Phi Eps 2Ta S3bar Phi S1tm43 | 4 | Y1t3 | 0 | n/a | 0 | 1/2+1/2+1/3−4/3=0 | `Eps[a1,a2]`+`Ta[b1,a2,a3]` (Hᵀiσ₂(σ·Φ₃)†H) | shared `c1` | n/a | n/a | n/a | HC[] |
| LQ2PhiMix Y13 | Phibar 2Ta S3 Phi S1m13bar | 4 | Y13 | 0 | n/a | 0 | −1/2−1/3+1/2+1/3=0 | `Ta[b1,a1,a2]` | shared `c1` | n/a | n/a | n/a | HC[] |
| LQkin (5 rows) | DC[Φabar]DC[Φa] for S1m13, S1tm43, R2, R2t, S3 | 4 | 1 | 0 | n/a | 0 | 0 | shared SU2D/SU2W index | shared `c1` | n/a | n/a | n/a | self-conj; **kinetic+mass term present for all 5 classes ⇒ all 9 physical states** |
| LQf YRR1 | CC[uRbar].lR S1m13bar | 4 | YRR1 | 0 | n/a | 0 | +2/3−1+1/3=0 | all singlets | 3̄(u^c-bar)⊗3̄(Φ₁†)… shared `c1` | n/a | ΔL,ΔB≠0 individually | **yes** (ū′ᶜ) | `HC[LQfNonHC]` |
| LQf YLL1 | CC[QLbar].LL Eps S1m13bar | 4 | YLL1 | 0 | n/a | 0 | 1/6−1/2+1/3=0 | `Eps[a1,a2]` (two same-type doublets) | shared `c1` | n/a | LQ | **yes** | HC[] |
| LQf YQLL1 | CC[QLbar].QL Eps S1m13 Eps[c1,c2,c3] | 4 | YQLL1 (symmetric) | 0 | n/a | 0 | 1/6+1/6−1/3=0 | `Eps[a1,a2]` | colour `Eps[c1,c2,c3]` (3⊗3⊗3→1) | n/a | diquark | **yes** | HC[] |
| LQf YQRR1 | CC[uRbar].dR S1m13 Eps[c1,c2,c3] | 4 | YQRR1 | 0 | n/a | 0 | 2/3−1/3−1/3=0 | singlets | colour `Eps` | n/a | diquark | **yes** | HC[] |
| LQf YRR1t | CC[dRbar].lR S1tm43bar | 4 | YRR1t | 0 | n/a | 0 | −1/3−1+4/3=0 | singlets | shared `c1` | n/a | LQ | **yes** | HC[] |
| LQf YQRR1t | CC[uRbar].uR S1tm43 Eps[c1,c2,c3] | 4 | YQRR1t (antisym.) | 0 | n/a | 0 | 2/3+2/3−4/3=0 | singlets | colour `Eps` | n/a | diquark | **yes** | HC[] |
| LQf YRL2 | uRbar.LL R2 Eps | 4 | YRL2 | 0 | n/a | 0 | −2/3−1/2+7/6=0 | `Eps[a1,a2]` (Φ₂ᵀiσ₂L) | shared `c1` | n/a | LQ | no (no ψᶜ) | HC[] |
| LQf YLR2 | QLbar.lR R2 | 4 | YLR2 | 0 | n/a | 0 | −1/6−1+7/6=0 | shared SU2D `a1` (Q̄ with Φ₂) | shared `c1` | n/a | LQ | no | HC[] |
| LQf YRL2t | dRbar.LL R2t Eps | 4 | YRL2t | 0 | n/a | 0 | 1/3−1/2+1/6=0 | `Eps[a1,a2]` | shared `c1` | n/a | LQ | no | HC[] |
| LQf YLL3 | CC[QLbar].LL Eps 2Ta S3bar | 4 | YLL3 | 0 | n/a | 0 | 1/6−1/2+1/3=0 | `Eps[a1,a2]`+`Ta[b1,a2,a3]` | shared `c1` | n/a | LQ | **yes** | HC[] |
| LQf YQLL3 | CC[QLbar].QL Eps 2Ta S3 Eps[c1,c2,c3] | 4 | YQLL3 (antisym.) | 0 | n/a | 0 | 1/6+1/6−1/3=0 | `Eps`+`Ta` | colour `Eps` | n/a | diquark | **yes** | HC[] |
| L3Φ A12t2t | S1m13 R2t Eps R2t Eps[c1,c2,c3] | 3 | A12t2t | 1 (GeV) | n/a | 0 | −1/3+1/6+1/6=0 | `Eps[a1,a2]` | colour `Eps` | n/a | n/a | n/a | `HC[LQ3PhiNonHC]` |
| L3Φ A1t22t | S1tm43 R2 Eps R2t Eps[c1,c2,c3] | 3 | A1t22t | 1 (GeV) | n/a | 0 | −4/3+7/6+1/6=0 | `Eps[a1,a2]` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y11t2 | S1m13 S1tm43 R2 Eps Phi Eps[c1,c2,c3] | 4 | Y11t2 | 0 | n/a | 0 | −1/3−4/3+7/6+1/2=0 | `Eps[a1,a2]` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y123 | S1m13 Phibar 2Ta S3 R2 Eps[c1,c2,c3] | 4 | Y123 | 0 | n/a | 0 | −1/3−1/2−1/3+7/6=0 | `Ta[b1,a1,a2]` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y12t3 | S1m13 R2t Eps 2Ta S3 Phi Eps[c1,c2,c3] | 4 | Y12t3 | 0 | n/a | 0 | −1/3+1/6−1/3+1/2=0 | `Eps`+`Ta` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y1t23 | S1tm43 R2 Eps 2Ta S3 Phi Eps[c1,c2,c3] | 4 | Y1t23 | 0 | n/a | 0 | −4/3+7/6−1/3+1/2=0 | `Eps`+`Ta` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y233 | Phibar 2Ta R2 S3 I Eps[b] S3 Eps[c1,c2,c3] | 4 | Y233 | 0 | n/a | 0 | −1/2+7/6−1/3−1/3=0 | `Ta` + SU2W `Eps[b1,b2,b3]` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y2t33 | R2t Eps 2Ta Phi S3 I Eps[b] S3 Eps[c] | 4 | Y2t33 | 0 | n/a | 0 | 1/6+1/2−1/3−1/3=0 | `Eps`+`Ta`+SU2W `Eps` | colour `Eps` | n/a | n/a | n/a | HC[] (verbatim Listing 3) |
| L4Φ Yq1a (5 rows: a=1,1̃,2,2̃,3) | (Φa†Φa)(Φa†Φa) | 4 | Yq11…Yq13 | 0 | n/a | 0 | 0 | singlet×singlet | δ_{c1c1}δ_{c2c2} | n/a | n/a | n/a | self-conj |
| L4Φ Yq3a (3 rows: a=2,2̃,3) | (Φa†_{c1}Φa_{c2})(Φa†_{c2}Φa_{c1}) | 4 | Yq32,Yq32t,Yq33 | 0 | n/a | 0 | 0 | singlet×singlet | crossed δ | n/a | n/a | n/a | self-conj |
| L4Φ Yq53 | Φ3^{I†}Φ3^J Φ3^{I†}Φ3^J | 4 | Yq53 | 0 | n/a | 0 | 0 | paired SU2W indices `b1`,`b2` | δ_{c1c1}δ_{c2c2} | n/a | n/a | n/a | self-conj |
| L4Φ Yq1ab / Yp1ab (10 pairs ⇒ 20 rows) | (Φa†Φa)(Φb†Φb), a≠b | 4 | Yq111t…Yp12t3 | 0 | n/a | 0 | 0 | singlet×singlet | δδ (unprimed) / crossed δδ (primed) | n/a | n/a | n/a | self-conj |
| L4Φ Yq322t / Yp322t | (Φ2†Φ2̃)(Φ2̃†Φ2) | 4 | Yq322t, Yp322t | 0 | n/a | 0 | (−7/6+1/6)+(−1/6+7/6)=0 | shared `a1`, shared `a2` | δδ / crossed δδ | n/a | n/a | n/a | self-conj |
| L4Φ Yq3a3 / Yp3a3 (a=2,2̃; 4 rows) | (Φa†σ^IΦa)(Φ3^{J†}iε_{IJK}Φ3^K) | 4 | Yq323…Yp32t3 | 0 | n/a | 0 | 0 | `Ta[b1,a1,a2]` + SU2W `Eps[b1,b2,b3]` | δδ / crossed δδ | n/a | n/a | n/a | self-conj |
| L4Φ Y1aa3 / Yp1aa3 (a=2,2̃; 4 rows) | Φ1†(Φa†(σ·Φ3)Φa) | 4 | Y1223, Yp1223, Y12t2t3, Yp12t2t3 | 0 | n/a | 0 | 1/3−7/6−1/3+7/6=0 (a=2̃: 1/3−1/6−1/3+1/6=0) | `Ta[b1,a1,a2]` | δδ / crossed δδ | n/a | n/a | n/a | `HC[LQ4PhiNonHC]` |
| L4Φ Y1t2t23 / Yp1t2t23 | Φ1̃†(Φ2†(σ·Φ3)Φ2̃) | 4 | Y1t2t23, Yp1t2t23 | 0 | n/a | 0 | 4/3−7/6−1/3+1/6=0 | `Ta` | δδ / crossed δδ | n/a | n/a | n/a | HC[] |
| L4Φ Y11t2t2 / Yp11t2t2 | Φ1†Φ1̃(Φ2̃†Φ2) | 4 | Y11t2t2, Yp11t2t2 | 0 | n/a | 0 | 1/3−4/3−1/6+7/6=0 | singlet×singlet | δδ / crossed δδ | n/a | n/a | n/a | HC[] |
| L4Φ Y1313 | Φ1†Φ3^I Φ1†Φ3^I | 4 | Y1313 | 0 | n/a | 0 | 2(1/3)+2(−1/3)=0 | shared SU2W `b1` | δ_{c1c1}δ_{c2c2} | n/a | n/a | n/a | HC[] |
| L4Φ Y1333 | Φ1†Φ3^I Φ3^{J†}Φ3^K iε_{IJK} | 4 | Y1333 | 0 | n/a | 0 | 1/3−1/3+1/3−1/3=0 | SU2W `Eps[b1,b2,b3]` | δ_{c1c1}δ_{c2c2} | n/a | n/a | n/a | HC[] |

**Kinetic + mass confirmation:** `LQkin` supplies `DC[Φ†]DC[Φ]` and `LQ2PhiDiag` supplies `−m_a² Φ†Φ` for all five multiplet classes S1m13, S1tm43, R2, R2t, S3. Their `Definitions` expand into the nine physical states, whose `Mass -> {…, Internal}` symbols are the diagonalised eigenvalues of Eq. (32); both terms are in the total sum `LQall`.

**SelfConjugate → True classes:** none. Every new class is a complex scalar (`self_conjugate = false`), so no quantum numbers sit on a self-conjugate field.

**Reference/cached model file read:** none. Only the paper text, `frmodel.py`, `render.py` and the supplied `SM.fr` were opened.

**Convention notes.** (i) The schema forbids `External` + `ComplexParameter -> True`, so the couplings the paper declares complex (Listing 1) are emitted as real External parameters; `HC[...]` still generates the correct hermitian partners. (ii) The five unphysical mass parameters get distinct defaults (1000–1400 GeV) because Eqs. (30)/(32) divide by mass-squared differences. (iii) The Σ_{a≠b} quartics are written once per unordered pair.

```json
{
  "model_name": "SLQrules_gen",
  "info": {
    "authors": ["A. Crivellin", "L. Schnell"],
    "version": "1.0",
    "date": "20. 06. 2022",
    "institutions": ["CERN", "Universitaet Zuerich", "Paul Scherrer Institut", "LPTHE Sorbonne Universite", "ETH Zuerich"],
    "emails": ["schnell@mpp.mpg.de"]
  },
  "gauge_groups": [],
  "index_decls": [
    {"name": "LQ3", "range_kind": "NoUnfold", "size": 3, "style_symbol": "nn"},
    {"name": "LQ2", "range_kind": "NoUnfold", "size": 2, "style_symbol": "pp"}
  ],
  "parameters": [
    {"name": "m1", "parameter_type": "External", "value": "1000.", "block_name": "LQMASS", "order_block": 1, "tex": "m_1", "description": "Mass parameter of the scalar leptoquark Phi1 (SU(2) singlet, Y=-1/3) [GeV], Eq.(25)"},
    {"name": "m1t", "parameter_type": "External", "value": "1100.", "block_name": "LQMASS", "order_block": 2, "tex": "m_{1t}", "description": "Mass parameter of the scalar leptoquark Phi1tilde (SU(2) singlet, Y=-4/3) [GeV], Eq.(25)"},
    {"name": "m2", "parameter_type": "External", "value": "1200.", "block_name": "LQMASS", "order_block": 3, "tex": "m_2", "description": "Mass parameter of the scalar leptoquark Phi2 (SU(2) doublet, Y=7/6) [GeV], Eq.(25)"},
    {"name": "m2t", "parameter_type": "External", "value": "1300.", "block_name": "LQMASS", "order_block": 4, "tex": "m_{2t}", "description": "Mass parameter of the scalar leptoquark Phi2tilde (SU(2) doublet, Y=1/6) [GeV], Eq.(25)"},
    {"name": "m3", "parameter_type": "External", "value": "1400.", "block_name": "LQMASS", "order_block": 5, "tex": "m_3", "description": "Mass parameter of the scalar leptoquark Phi3 (SU(2) triplet, Y=-1/3) [GeV], Eq.(25)"},

    {"name": "Y1", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 1, "interaction_order": ["QED", 2], "description": "Coupling Y1 of (H^dag H)(Phi1^dag Phi1), Eq.(25)"},
    {"name": "Y1t", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 2, "interaction_order": ["QED", 2], "description": "Coupling Y1tilde of (H^dag H)(Phi1t^dag Phi1t), Eq.(25)"},
    {"name": "Y2", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 3, "interaction_order": ["QED", 2], "description": "Coupling Y2 of (H^dag H)(Phi2^dag Phi2), Eq.(25)"},
    {"name": "Y2t", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 4, "interaction_order": ["QED", 2], "description": "Coupling Y2tilde of (H^dag H)(Phi2t^dag Phi2t), Eq.(25)"},
    {"name": "Y3", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 5, "interaction_order": ["QED", 2], "description": "Coupling Y3 of (H^dag H)(Phi3^dag Phi3), Eq.(25)"},
    {"name": "Y22", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 6, "interaction_order": ["QED", 2], "description": "Coupling Y22 of |H^T i sigma2 Phi2|^2, Eq.(25)"},
    {"name": "Y2t2t", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 7, "interaction_order": ["QED", 2], "description": "Coupling Y2tilde2tilde of |H^T i sigma2 Phi2t|^2, Eq.(25)"},
    {"name": "Y33", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 8, "interaction_order": ["QED", 2], "description": "Coupling Y33 of i eps_IJK (H^dag sigma_I H) Phi3^J,dag Phi3^K, Eq.(25)"},
    {"name": "Y22t", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 9, "interaction_order": ["QED", 2], "description": "Phi2-Phi2tilde Higgs mixing coupling Y22tilde, Eq.(25)"},
    {"name": "Y1t3", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 10, "interaction_order": ["QED", 2], "description": "Phi1tilde-Phi3 Higgs mixing coupling Y1tilde3, Eq.(25)"},
    {"name": "Y13", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 11, "interaction_order": ["QED", 2], "description": "S3-S1 scalar leptoquark mixing coupling Y13, Eq.(25)"},

    {"name": "A12t", "parameter_type": "External", "value": "1000.", "block_name": "LQ2PHIA", "order_block": 1, "interaction_order": ["QED", 1], "description": "Trilinear Phi1-Phi2tilde-H coupling A_{1 2tilde}, mass dimension 1, units GeV, Eq.(25)"},
    {"name": "A2t3", "parameter_type": "External", "value": "1000.", "block_name": "LQ2PHIA", "order_block": 2, "interaction_order": ["QED", 1], "description": "Trilinear Phi2tilde-Phi3-H coupling A_{2tilde 3}, mass dimension 1, units GeV, Eq.(25)"},

    {"name": "A12t2t", "parameter_type": "External", "value": "1000.", "block_name": "LQ3PHI", "order_block": 1, "interaction_order": ["QED", 1], "description": "Triple LQ coupling A_{1 2tilde 2tilde}, mass dimension 1, units GeV, Eq.(46)"},
    {"name": "A1t22t", "parameter_type": "External", "value": "1000.", "block_name": "LQ3PHI", "order_block": 2, "interaction_order": ["QED", 1], "description": "Triple LQ coupling A_{1tilde 2 2tilde}, mass dimension 1, units GeV, Eq.(46)"},
    {"name": "Y11t2", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 3, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{1 1tilde 2}, Eq.(46)"},
    {"name": "Y123", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 4, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{123}, Eq.(46)"},
    {"name": "Y12t3", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 5, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{1 2tilde 3}, Eq.(46)"},
    {"name": "Y1t23", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 6, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{1tilde 2 3}, Eq.(46)"},
    {"name": "Y233", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 7, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{233}, Eq.(46)"},
    {"name": "Y2t33", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 8, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{2tilde 3 3}, Eq.(46)"},

    {"name": "Yq11", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 1, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_1, Eq.(49)"},
    {"name": "Yq11t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 2, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_1tilde, Eq.(49)"},
    {"name": "Yq12", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 3, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_2, Eq.(49)"},
    {"name": "Yq12t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 4, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_2tilde, Eq.(49)"},
    {"name": "Yq13", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 5, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_3, Eq.(49)"},
    {"name": "Yq32", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 6, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_2 (crossed colour contraction), Eq.(49)"},
    {"name": "Yq32t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 7, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_2tilde (crossed colour contraction), Eq.(49)"},
    {"name": "Yq33", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 8, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_3 (crossed colour contraction), Eq.(49)"},
    {"name": "Yq53", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 9, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(5)_3, Eq.(49)"},
    {"name": "Yq111t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 10, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1 1tilde}, Eq.(49)"},
    {"name": "Yp111t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 11, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1 1tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq112", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 12, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1 2}, Eq.(49)"},
    {"name": "Yp112", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 13, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1 2} (crossed colour), Eq.(49)"},
    {"name": "Yq112t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 14, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1 2tilde}, Eq.(49)"},
    {"name": "Yp112t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 15, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1 2tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq113", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 16, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1 3}, Eq.(49)"},
    {"name": "Yp113", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 17, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1 3} (crossed colour), Eq.(49)"},
    {"name": "Yq11t2", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 18, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1tilde 2}, Eq.(49)"},
    {"name": "Yp11t2", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 19, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1tilde 2} (crossed colour), Eq.(49)"},
    {"name": "Yq11t2t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 20, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1tilde 2tilde}, Eq.(49)"},
    {"name": "Yp11t2t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 21, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1tilde 2tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq11t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 22, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1tilde 3}, Eq.(49)"},
    {"name": "Yp11t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 23, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1tilde 3} (crossed colour), Eq.(49)"},
    {"name": "Yq122t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 24, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{2 2tilde}, Eq.(49)"},
    {"name": "Yp122t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 25, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{2 2tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq123", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 26, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{2 3}, Eq.(49)"},
    {"name": "Yp123", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 27, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{2 3} (crossed colour), Eq.(49)"},
    {"name": "Yq12t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 28, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{2tilde 3}, Eq.(49)"},
    {"name": "Yp12t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 29, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{2tilde 3} (crossed colour), Eq.(49)"},
    {"name": "Yq322t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 30, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_{2 2tilde}, Eq.(49)"},
    {"name": "Yp322t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 31, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(3)_{2 2tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq323", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 32, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_{2 3}, Eq.(49)"},
    {"name": "Yp323", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 33, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(3)_{2 3} (crossed colour), Eq.(49)"},
    {"name": "Yq32t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 34, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_{2tilde 3}, Eq.(49)"},
    {"name": "Yp32t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 35, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(3)_{2tilde 3} (crossed colour), Eq.(49)"},
    {"name": "Y1223", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 36, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1223}, Eq.(49)"},
    {"name": "Yp1223", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 37, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'_{1223} (crossed colour), Eq.(49)"},
    {"name": "Y12t2t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 38, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1 2tilde 2tilde 3}, Eq.(49)"},
    {"name": "Yp12t2t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 39, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'_{1 2tilde 2tilde 3} (crossed colour), Eq.(49)"},
    {"name": "Y1t2t23", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 40, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1tilde 2tilde 2 3}, Eq.(49)"},
    {"name": "Yp1t2t23", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 41, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'_{1tilde 2tilde 2 3} (crossed colour), Eq.(49)"},
    {"name": "Y11t2t2", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 42, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1 1tilde 2tilde 2}, Eq.(49)"},
    {"name": "Yp11t2t2", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 43, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'_{1 1tilde 2tilde 2} (crossed colour), Eq.(49)"},
    {"name": "Y1313", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 44, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1313}, Eq.(49)"},
    {"name": "Y1333", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 45, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1333}, Eq.(49)"},

    {"name": "YRR1", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YRR1", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YRR1[1,1]", "rhs": "1."}, {"lhs": "YRR1[1,2]", "rhs": "1."}, {"lhs": "YRR1[1,3]", "rhs": "1."},
      {"lhs": "YRR1[2,1]", "rhs": "1."}, {"lhs": "YRR1[2,2]", "rhs": "1."}, {"lhs": "YRR1[2,3]", "rhs": "1."},
      {"lhs": "YRR1[3,1]", "rhs": "1."}, {"lhs": "YRR1[3,2]", "rhs": "1."}, {"lhs": "YRR1[3,3]", "rhs": "1."}],
      "description": "Y^{RR}_1: Phi1 coupling to ubar^c lepton, Eq.(43)"},
    {"name": "YLL1", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YLL1", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YLL1[1,1]", "rhs": "1."}, {"lhs": "YLL1[1,2]", "rhs": "1."}, {"lhs": "YLL1[1,3]", "rhs": "1."},
      {"lhs": "YLL1[2,1]", "rhs": "1."}, {"lhs": "YLL1[2,2]", "rhs": "1."}, {"lhs": "YLL1[2,3]", "rhs": "1."},
      {"lhs": "YLL1[3,1]", "rhs": "1."}, {"lhs": "YLL1[3,2]", "rhs": "1."}, {"lhs": "YLL1[3,3]", "rhs": "1."}],
      "description": "Y^{LL}_1: Phi1 coupling to Qbar^c L, Eq.(43)"},
    {"name": "YQLL1", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YQLL1", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YQLL1[1,1]", "rhs": "1."}, {"lhs": "YQLL1[1,2]", "rhs": "1."}, {"lhs": "YQLL1[1,3]", "rhs": "1."},
      {"lhs": "YQLL1[2,1]", "rhs": "1."}, {"lhs": "YQLL1[2,2]", "rhs": "1."}, {"lhs": "YQLL1[2,3]", "rhs": "1."},
      {"lhs": "YQLL1[3,1]", "rhs": "1."}, {"lhs": "YQLL1[3,2]", "rhs": "1."}, {"lhs": "YQLL1[3,3]", "rhs": "1."}],
      "description": "Y^{Q,LL}_1: Phi1 diquark coupling, symmetric in flavour, Eq.(43)"},
    {"name": "YQRR1", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YQRR1", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YQRR1[1,1]", "rhs": "1."}, {"lhs": "YQRR1[1,2]", "rhs": "1."}, {"lhs": "YQRR1[1,3]", "rhs": "1."},
      {"lhs": "YQRR1[2,1]", "rhs": "1."}, {"lhs": "YQRR1[2,2]", "rhs": "1."}, {"lhs": "YQRR1[2,3]", "rhs": "1."},
      {"lhs": "YQRR1[3,1]", "rhs": "1."}, {"lhs": "YQRR1[3,2]", "rhs": "1."}, {"lhs": "YQRR1[3,3]", "rhs": "1."}],
      "description": "Y^{Q,RR}_1: Phi1 diquark coupling ubar^c d, Eq.(43)"},
    {"name": "YRR1t", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YRR1T", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YRR1t[1,1]", "rhs": "1."}, {"lhs": "YRR1t[1,2]", "rhs": "1."}, {"lhs": "YRR1t[1,3]", "rhs": "1."},
      {"lhs": "YRR1t[2,1]", "rhs": "1."}, {"lhs": "YRR1t[2,2]", "rhs": "1."}, {"lhs": "YRR1t[2,3]", "rhs": "1."},
      {"lhs": "YRR1t[3,1]", "rhs": "1."}, {"lhs": "YRR1t[3,2]", "rhs": "1."}, {"lhs": "YRR1t[3,3]", "rhs": "1."}],
      "description": "Y^{RR}_1tilde: Phi1tilde coupling to dbar^c lepton, Eq.(43)"},
    {"name": "YQRR1t", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YQRR1T", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YQRR1t[1,1]", "rhs": "0."}, {"lhs": "YQRR1t[1,2]", "rhs": "1."}, {"lhs": "YQRR1t[1,3]", "rhs": "1."},
      {"lhs": "YQRR1t[2,1]", "rhs": "-1."}, {"lhs": "YQRR1t[2,2]", "rhs": "0."}, {"lhs": "YQRR1t[2,3]", "rhs": "1."},
      {"lhs": "YQRR1t[3,1]", "rhs": "-1."}, {"lhs": "YQRR1t[3,2]", "rhs": "-1."}, {"lhs": "YQRR1t[3,3]", "rhs": "0."}],
      "description": "Y^{Q,RR}_1tilde: Phi1tilde diquark coupling ubar^c u, antisymmetric in flavour, Eq.(43)"},
    {"name": "YRL2", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YRL2", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YRL2[1,1]", "rhs": "1."}, {"lhs": "YRL2[1,2]", "rhs": "1."}, {"lhs": "YRL2[1,3]", "rhs": "1."},
      {"lhs": "YRL2[2,1]", "rhs": "1."}, {"lhs": "YRL2[2,2]", "rhs": "1."}, {"lhs": "YRL2[2,3]", "rhs": "1."},
      {"lhs": "YRL2[3,1]", "rhs": "1."}, {"lhs": "YRL2[3,2]", "rhs": "1."}, {"lhs": "YRL2[3,3]", "rhs": "1."}],
      "description": "Y^{RL}_2: Phi2 coupling to ubar L, Eq.(43)"},
    {"name": "YLR2", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YLR2", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YLR2[1,1]", "rhs": "1."}, {"lhs": "YLR2[1,2]", "rhs": "1."}, {"lhs": "YLR2[1,3]", "rhs": "1."},
      {"lhs": "YLR2[2,1]", "rhs": "1."}, {"lhs": "YLR2[2,2]", "rhs": "1."}, {"lhs": "YLR2[2,3]", "rhs": "1."},
      {"lhs": "YLR2[3,1]", "rhs": "1."}, {"lhs": "YLR2[3,2]", "rhs": "1."}, {"lhs": "YLR2[3,3]", "rhs": "1."}],
      "description": "Y^{LR}_2: Phi2 coupling to Qbar lepton_R, Eq.(43)"},
    {"name": "YRL2t", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YRL2T", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YRL2t[1,1]", "rhs": "1."}, {"lhs": "YRL2t[1,2]", "rhs": "1."}, {"lhs": "YRL2t[1,3]", "rhs": "1."},
      {"lhs": "YRL2t[2,1]", "rhs": "1."}, {"lhs": "YRL2t[2,2]", "rhs": "1."}, {"lhs": "YRL2t[2,3]", "rhs": "1."},
      {"lhs": "YRL2t[3,1]", "rhs": "1."}, {"lhs": "YRL2t[3,2]", "rhs": "1."}, {"lhs": "YRL2t[3,3]", "rhs": "1."}],
      "description": "Y^{RL}_2tilde: Phi2tilde coupling to dbar L, Eq.(43)"},
    {"name": "YLL3", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YLL3", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YLL3[1,1]", "rhs": "1."}, {"lhs": "YLL3[1,2]", "rhs": "1."}, {"lhs": "YLL3[1,3]", "rhs": "1."},
      {"lhs": "YLL3[2,1]", "rhs": "1."}, {"lhs": "YLL3[2,2]", "rhs": "1."}, {"lhs": "YLL3[2,3]", "rhs": "1."},
      {"lhs": "YLL3[3,1]", "rhs": "1."}, {"lhs": "YLL3[3,2]", "rhs": "1."}, {"lhs": "YLL3[3,3]", "rhs": "1."}],
      "description": "Y^{LL}_3: Phi3 coupling to Qbar^c L, Eq.(43)"},
    {"name": "YQLL3", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YQLL3", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YQLL3[1,1]", "rhs": "0."}, {"lhs": "YQLL3[1,2]", "rhs": "1."}, {"lhs": "YQLL3[1,3]", "rhs": "1."},
      {"lhs": "YQLL3[2,1]", "rhs": "-1."}, {"lhs": "YQLL3[2,2]", "rhs": "0."}, {"lhs": "YQLL3[2,3]", "rhs": "1."},
      {"lhs": "YQLL3[3,1]", "rhs": "-1."}, {"lhs": "YQLL3[3,2]", "rhs": "-1."}, {"lhs": "YQLL3[3,3]", "rhs": "0."}],
      "description": "Y^{Q,LL}_3: Phi3 diquark coupling, antisymmetric in flavour, Eq.(43)"},

    {"name": "msq2t1", "parameter_type": "Internal", "value": "m2t^2 - m1^2", "description": "m^2_{2tilde 1} = m2t^2 - m1^2, Eq.(32)"},
    {"name": "msq2t3", "parameter_type": "Internal", "value": "m2t^2 - m3^2", "description": "m^2_{2tilde 3} = m2t^2 - m3^2, Eq.(32)"},
    {"name": "msq12t", "parameter_type": "Internal", "value": "m1^2 - m2t^2", "description": "m^2_{1 2tilde} = m1^2 - m2t^2, Eq.(30)"},
    {"name": "msq32t", "parameter_type": "Internal", "value": "m3^2 - m2t^2", "description": "m^2_{3 2tilde} = m3^2 - m2t^2, Eq.(30)"},
    {"name": "msq13", "parameter_type": "Internal", "value": "m1^2 - m3^2", "description": "m^2_{13} = m1^2 - m3^2, Eq.(30)"},
    {"name": "msq22t", "parameter_type": "Internal", "value": "m2^2 - m2t^2", "description": "m^2_{2 2tilde} = m2^2 - m2t^2, Eq.(30)"},
    {"name": "msq1t3", "parameter_type": "Internal", "value": "m1t^2 - m3^2", "description": "m^2_{1tilde 3} = m1t^2 - m3^2, Eq.(30)"},

    {"name": "W13mat", "parameter_type": "Internal", "complex": true, "indices": ["LQ3", "LQ3"], "value_rules": [
      {"lhs": "W13mat[1,1]", "rhs": "1 - vev^2 Abs[A12t]^2/(4 msq12t^2)"},
      {"lhs": "W13mat[1,2]", "rhs": "vev Conjugate[A12t]/(Sqrt[2] msq12t)"},
      {"lhs": "W13mat[1,3]", "rhs": "vev^2 (Y13 msq12t + Conjugate[A12t] A2t3)/(2 msq13 msq12t)"},
      {"lhs": "W13mat[2,1]", "rhs": "-vev A12t/(Sqrt[2] msq12t)"},
      {"lhs": "W13mat[2,2]", "rhs": "1 - vev^2/4 (Abs[A12t]^2/msq12t^2 + Abs[A2t3]^2/msq32t^2)"},
      {"lhs": "W13mat[2,3]", "rhs": "-vev A2t3/(Sqrt[2] msq32t)"},
      {"lhs": "W13mat[3,1]", "rhs": "-vev^2 (Conjugate[Y13] msq32t + A12t Conjugate[A2t3])/(2 msq13 msq32t)"},
      {"lhs": "W13mat[3,2]", "rhs": "vev Conjugate[A2t3]/(Sqrt[2] msq32t)"},
      {"lhs": "W13mat[3,3]", "rhs": "1 - vev^2 Abs[A2t3]^2/(4 msq32t^2)"}],
      "description": "Unitary rotation W^{-1/3} to the Q=-1/3 leptoquark mass basis, order v^2, Eq.(30)"},
    {"name": "W23mat", "parameter_type": "Internal", "complex": true, "indices": ["LQ3", "LQ3"], "value_rules": [
      {"lhs": "W23mat[1,1]", "rhs": "1"},
      {"lhs": "W23mat[1,2]", "rhs": "vev^2 Y22t/(2 msq22t)"},
      {"lhs": "W23mat[1,3]", "rhs": "0"},
      {"lhs": "W23mat[2,1]", "rhs": "-vev^2 Conjugate[Y22t]/(2 msq22t)"},
      {"lhs": "W23mat[2,2]", "rhs": "1 - vev^2 Abs[A2t3]^2/(2 msq32t^2)"},
      {"lhs": "W23mat[2,3]", "rhs": "-vev A2t3/msq2t3"},
      {"lhs": "W23mat[3,1]", "rhs": "0"},
      {"lhs": "W23mat[3,2]", "rhs": "vev Conjugate[A2t3]/msq2t3"},
      {"lhs": "W23mat[3,3]", "rhs": "1 - vev^2 Abs[A2t3]^2/(2 msq32t^2)"}],
      "description": "Unitary rotation W^{+2/3} to the Q=+2/3 leptoquark mass basis, order v^2, Eq.(30)"},
    {"name": "W43mat", "parameter_type": "Internal", "complex": true, "indices": ["LQ2", "LQ2"], "value_rules": [
      {"lhs": "W43mat[1,1]", "rhs": "1"},
      {"lhs": "W43mat[1,2]", "rhs": "vev^2 Conjugate[Y1t3]/(Sqrt[2] msq1t3)"},
      {"lhs": "W43mat[2,1]", "rhs": "-vev^2 Y1t3/(Sqrt[2] msq1t3)"},
      {"lhs": "W43mat[2,2]", "rhs": "1"}],
      "description": "Unitary rotation W^{-4/3} to the Q=-4/3 leptoquark mass basis, order v^2, Eq.(30)"},

    {"name": "m1m13hat", "parameter_type": "Internal", "value": "Sqrt[m1^2 + vev^2/2 (Y1 - Abs[A12t]^2/msq2t1)]", "description": "Mass of the Q=-1/3 mass eigenstate S1m13hat [GeV], Eq.(32)"},
    {"name": "m2tm13hat", "parameter_type": "Internal", "value": "Sqrt[m2t^2 + vev^2/2 (Y2t + Abs[A12t]^2/msq2t1 + Abs[A2t3]^2/msq2t3)]", "description": "Mass of the Q=-1/3 mass eigenstate R2tm13hat [GeV], Eq.(32)"},
    {"name": "m3m13hat", "parameter_type": "Internal", "value": "Sqrt[m3^2 + vev^2/2 (Y3 - Abs[A2t3]^2/msq2t3)]", "description": "Mass of the Q=-1/3 mass eigenstate S3m13hat [GeV], Eq.(32)"},
    {"name": "m2p23hat", "parameter_type": "Internal", "value": "Sqrt[m2^2 + vev^2/2 Y2]", "description": "Mass of the Q=+2/3 mass eigenstate R2p23hat [GeV], Eq.(32)"},
    {"name": "m2tp23hat", "parameter_type": "Internal", "value": "Sqrt[m2t^2 + vev^2/2 (Y2t + Y2t2t + 2 Abs[A2t3]^2/msq2t3)]", "description": "Mass of the Q=+2/3 mass eigenstate R2tp23hat [GeV], Eq.(32)"},
    {"name": "m3p23hat", "parameter_type": "Internal", "value": "Sqrt[m3^2 + vev^2/2 (Y3 + Y33 - 2 Abs[A2t3]^2/msq2t3)]", "description": "Mass of the Q=+2/3 mass eigenstate S3p23hat [GeV], Eq.(32)"},
    {"name": "m1tm43hat", "parameter_type": "Internal", "value": "Sqrt[m1t^2 + vev^2/2 Y1t]", "description": "Mass of the Q=-4/3 mass eigenstate S1tm43hat [GeV], Eq.(32)"},
    {"name": "m3m43hat", "parameter_type": "Internal", "value": "Sqrt[m3^2 + vev^2/2 (Y3 - Y33)]", "description": "Mass of the Q=-4/3 mass eigenstate S3m43hat [GeV], Eq.(32)"},
    {"name": "m2p53hat", "parameter_type": "Internal", "value": "Sqrt[m2^2 + vev^2/2 (Y2 + Y22)]", "description": "Mass of the Q=+5/3 mass eigenstate R2p53hat [GeV], Eq.(32)"}
  ],
  "particles": [
    {"spin_type": "S", "class_index": 100, "class_name": "S1m13hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m1m13hat", "value": "Internal"}, "width": {"sym": "W1m13hat", "value": "1."},
     "quantum_numbers": {"Q": "-1/3"}, "pdg": 9000001,
     "particle_name": "S1m13hat", "antiparticle_name": "S1m13hat~", "full_name": "S1m13hat",
     "propagator_label": "S1m13hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 101, "class_name": "R2tm13hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m2tm13hat", "value": "Internal"}, "width": {"sym": "W2tm13hat", "value": "1."},
     "quantum_numbers": {"Q": "-1/3"}, "pdg": 9000002,
     "particle_name": "R2tm13hat", "antiparticle_name": "R2tm13hat~", "full_name": "R2tm13hat",
     "propagator_label": "R2tm13hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 102, "class_name": "S3m13hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m3m13hat", "value": "Internal"}, "width": {"sym": "W3m13hat", "value": "1."},
     "quantum_numbers": {"Q": "-1/3"}, "pdg": 9000003,
     "particle_name": "S3m13hat", "antiparticle_name": "S3m13hat~", "full_name": "S3m13hat",
     "propagator_label": "S3m13hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 103, "class_name": "R2p23hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m2p23hat", "value": "Internal"}, "width": {"sym": "W2p23hat", "value": "1."},
     "quantum_numbers": {"Q": "2/3"}, "pdg": 9000004,
     "particle_name": "R2p23hat", "antiparticle_name": "R2p23hat~", "full_name": "R2p23hat",
     "propagator_label": "R2p23hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 104, "class_name": "R2tp23hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m2tp23hat", "value": "Internal"}, "width": {"sym": "W2tp23hat", "value": "1."},
     "quantum_numbers": {"Q": "2/3"}, "pdg": 9000005,
     "particle_name": "R2tp23hat", "antiparticle_name": "R2tp23hat~", "full_name": "R2tp23hat",
     "propagator_label": "R2tp23hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 105, "class_name": "S3p23hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m3p23hat", "value": "Internal"}, "width": {"sym": "W3p23hat", "value": "1."},
     "quantum_numbers": {"Q": "2/3"}, "pdg": 9000006,
     "particle_name": "S3p23hat", "antiparticle_name": "S3p23hat~", "full_name": "S3p23hat",
     "propagator_label": "S3p23hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 106, "class_name": "S1tm43hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m1tm43hat", "value": "Internal"}, "width": {"sym": "W1tm43hat", "value": "1."},
     "quantum_numbers": {"Q": "-4/3"}, "pdg": 9000007,
     "particle_name": "S1tm43hat", "antiparticle_name": "S1tm43hat~", "full_name": "S1tm43hat",
     "propagator_label": "S1tm43hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 107, "class_name": "S3m43hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m3m43hat", "value": "Internal"}, "width": {"sym": "W3m43hat", "value": "1."},
     "quantum_numbers": {"Q": "-4/3"}, "pdg": 9000008,
     "particle_name": "S3m43hat", "antiparticle_name": "S3m43hat~", "full_name": "S3m43hat",
     "propagator_label": "S3m43hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 108, "class_name": "R2p53hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m2p53hat", "value": "Internal"}, "width": {"sym": "W2p53hat", "value": "1."},
     "quantum_numbers": {"Q": "5/3"}, "pdg": 9000009,
     "particle_name": "R2p53hat", "antiparticle_name": "R2p53hat~", "full_name": "R2p53hat",
     "propagator_label": "R2p53hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},

    {"spin_type": "S", "class_index": 110, "class_name": "S1m13", "self_conjugate": false, "unphysical": true,
     "indices": ["Colour"], "quantum_numbers": {"Y": "-1/3"},
     "definitions": ["S1m13[cc_] :> HC[W13mat[1,1]] S1m13hat[cc] + HC[W13mat[2,1]] R2tm13hat[cc] + HC[W13mat[3,1]] S3m13hat[cc]"]},
    {"spin_type": "S", "class_index": 111, "class_name": "S1tm43", "self_conjugate": false, "unphysical": true,
     "indices": ["Colour"], "quantum_numbers": {"Y": "-4/3"},
     "definitions": ["S1tm43[cc_] :> HC[W43mat[1,1]] S1tm43hat[cc] + HC[W43mat[2,1]] S3m43hat[cc]"]},
    {"spin_type": "S", "class_index": 112, "class_name": "R2", "self_conjugate": false, "unphysical": true,
     "indices": ["SU2D", "Colour"], "flavor_index": "SU2D", "quantum_numbers": {"Y": "7/6"},
     "definitions": [
       "R2[1,cc_] :> R2p53hat[cc]",
       "R2[2,cc_] :> HC[W23mat[1,1]] R2p23hat[cc] + HC[W23mat[2,1]] R2tp23hat[cc] + HC[W23mat[3,1]] S3p23hat[cc]"]},
    {"spin_type": "S", "class_index": 113, "class_name": "R2t", "self_conjugate": false, "unphysical": true,
     "indices": ["SU2D", "Colour"], "flavor_index": "SU2D", "quantum_numbers": {"Y": "1/6"},
     "definitions": [
       "R2t[1,cc_] :> HC[W23mat[1,2]] R2p23hat[cc] + HC[W23mat[2,2]] R2tp23hat[cc] + HC[W23mat[3,2]] S3p23hat[cc]",
       "R2t[2,cc_] :> HC[W13mat[1,2]] S1m13hat[cc] + HC[W13mat[2,2]] R2tm13hat[cc] + HC[W13mat[3,2]] S3m13hat[cc]"]},
    {"spin_type": "S", "class_index": 114, "class_name": "S3", "self_conjugate": false, "unphysical": true,
     "indices": ["SU2W", "Colour"], "flavor_index": "SU2W", "quantum_numbers": {"Y": "-1/3"},
     "definitions": [
       "S3[1,cc_] :> (HC[W23mat[1,3]] R2p23hat[cc] + HC[W23mat[2,3]] R2tp23hat[cc] + HC[W23mat[3,3]] S3p23hat[cc] + HC[W43mat[1,2]] S1tm43hat[cc] + HC[W43mat[2,2]] S3m43hat[cc])/Sqrt[2]",
       "S3[2,cc_] :> I (HC[W23mat[1,3]] R2p23hat[cc] + HC[W23mat[2,3]] R2tp23hat[cc] + HC[W23mat[3,3]] S3p23hat[cc] - HC[W43mat[1,2]] S1tm43hat[cc] - HC[W43mat[2,2]] S3m43hat[cc])/Sqrt[2]",
       "S3[3,cc_] :> HC[W13mat[1,3]] S1m13hat[cc] + HC[W13mat[2,3]] R2tm13hat[cc] + HC[W13mat[3,3]] S3m13hat[cc]"]}
  ],
  "lagrangian_terms": [
    {"name": "LQ2PhiDiag", "delayed": true, "expression": "Module[{a1,a2,a3,a4,b1,b2,b3,c1}, ExpandIndices[ - m1^2 S1m13bar[c1] S1m13[c1] - m1t^2 S1tm43bar[c1] S1tm43[c1] - m2^2 R2bar[a1,c1] R2[a1,c1] - m2t^2 R2tbar[a1,c1] R2t[a1,c1] - m3^2 S3bar[b1,c1] S3[b1,c1] - Y1 Phibar[a1] Phi[a1] S1m13bar[c1] S1m13[c1] - Y1t Phibar[a1] Phi[a1] S1tm43bar[c1] S1tm43[c1] - Y2 Phibar[a1] Phi[a1] R2bar[a2,c1] R2[a2,c1] - Y2t Phibar[a1] Phi[a1] R2tbar[a2,c1] R2t[a2,c1] - Y3 Phibar[a1] Phi[a1] S3bar[b1,c1] S3[b1,c1] - Y22 Phibar[a1] Eps[a1,a2] R2bar[a2,c1] Phi[a3] Eps[a3,a4] R2[a4,c1] - Y2t2t Phibar[a1] Eps[a1,a2] R2tbar[a2,c1] Phi[a3] Eps[a3,a4] R2t[a4,c1] - I Y33 Eps[b1,b2,b3] Phibar[a1] 2 Ta[b1,a1,a2] Phi[a2] S3bar[b2,c1] S3[b3,c1], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ2PhiMixNonHC", "delayed": true, "expression": "Module[{a1,a2,a3,b1,c1}, ExpandIndices[ - A12t R2tbar[a1,c1] Phi[a1] S1m13[c1] + A2t3 R2tbar[a1,c1] 2 Ta[b1,a1,a2] Phi[a2] S3[b1,c1] + Y22t R2bar[a1,c1] Phi[a1] Phi[a2] Eps[a2,a3] R2t[a3,c1] + Y1t3 Phi[a1] Eps[a1,a2] 2 Ta[b1,a2,a3] S3bar[b1,c1] Phi[a3] S1tm43[c1] + Y13 Phibar[a1] 2 Ta[b1,a1,a2] S3[b1,c1] Phi[a2] S1m13bar[c1], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ2Phi", "delayed": true, "expression": "LQ2PhiDiag + LQ2PhiMixNonHC + HC[LQ2PhiMixNonHC]"},
    {"name": "LQkin", "delayed": true, "expression": "Module[{mu,a1,b1,c1}, ExpandIndices[ DC[S1m13bar[c1],mu] DC[S1m13[c1],mu] + DC[S1tm43bar[c1],mu] DC[S1tm43[c1],mu] + DC[R2bar[a1,c1],mu] DC[R2[a1,c1],mu] + DC[R2tbar[a1,c1],mu] DC[R2t[a1,c1],mu] + DC[S3bar[b1,c1],mu] DC[S3[b1,c1],mu], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQfNonHC", "delayed": true, "expression": "Module[{sp,a1,a2,a3,b1,c1,c2,c3,f1,f2}, ExpandIndices[ YRR1[f1,f2] CC[uRbar[sp,f1,c1]].lR[sp,f2] S1m13bar[c1] + YLL1[f1,f2] CC[QLbar[sp,a1,f1,c1]].LL[sp,a2,f2] Eps[a1,a2] S1m13bar[c1] + YQLL1[f1,f2] CC[QLbar[sp,a1,f1,c1]].QL[sp,a2,f2,c2] Eps[a1,a2] S1m13[c3] Eps[c1,c2,c3] + YQRR1[f1,f2] CC[uRbar[sp,f1,c1]].dR[sp,f2,c2] S1m13[c3] Eps[c1,c2,c3] + YRR1t[f1,f2] CC[dRbar[sp,f1,c1]].lR[sp,f2] S1tm43bar[c1] + YQRR1t[f1,f2] CC[uRbar[sp,f1,c1]].uR[sp,f2,c2] S1tm43[c3] Eps[c1,c2,c3] + YRL2[f1,f2] uRbar[sp,f1,c1].LL[sp,a2,f2] R2[a1,c1] Eps[a1,a2] + YLR2[f1,f2] QLbar[sp,a1,f1,c1].lR[sp,f2] R2[a1,c1] + YRL2t[f1,f2] dRbar[sp,f1,c1].LL[sp,a2,f2] R2t[a1,c1] Eps[a1,a2] + YLL3[f1,f2] CC[QLbar[sp,a1,f1,c1]].LL[sp,a3,f2] Eps[a1,a2] 2 Ta[b1,a2,a3] S3bar[b1,c1] + YQLL3[f1,f2] CC[QLbar[sp,a1,f1,c1]].QL[sp,a3,f2,c2] Eps[a1,a2] 2 Ta[b1,a2,a3] S3[b1,c3] Eps[c1,c2,c3], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQf", "delayed": true, "expression": "LQfNonHC + HC[LQfNonHC]"},
    {"name": "LQ3PhiNonHC", "delayed": true, "expression": "Module[{a1,a2,a3,b1,b2,b3,c1,c2,c3}, ExpandIndices[ A12t2t S1m13[c1] R2t[a1,c2] Eps[a1,a2] R2t[a2,c3] Eps[c1,c2,c3] + A1t22t S1tm43[c1] R2[a1,c2] Eps[a1,a2] R2t[a2,c3] Eps[c1,c2,c3] + Y11t2 S1m13[c1] S1tm43[c2] R2[a1,c3] Eps[a1,a2] Phi[a2] Eps[c1,c2,c3] + Y123 S1m13[c1] Phibar[a1] 2 Ta[b1,a1,a2] S3[b1,c3] R2[a2,c2] Eps[c1,c2,c3] + Y12t3 S1m13[c1] R2t[a1,c2] Eps[a1,a2] 2 Ta[b1,a2,a3] S3[b1,c3] Phi[a3] Eps[c1,c2,c3] + Y1t23 S1tm43[c1] R2[a1,c2] Eps[a1,a2] 2 Ta[b1,a2,a3] S3[b1,c3] Phi[a3] Eps[c1,c2,c3] + Y233 Phibar[a1] 2 Ta[b1,a1,a2] R2[a2,c1] S3[b2,c2] I Eps[b1,b2,b3] S3[b3,c3] Eps[c1,c2,c3] + Y2t33 R2t[a1,c1] Eps[a1,a2] 2 Ta[b1,a2,a3] Phi[a3] S3[b2,c2] I Eps[b1,b2,b3] S3[b3,c3] Eps[c1,c2,c3], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ3Phi", "delayed": true, "expression": "LQ3PhiNonHC + HC[LQ3PhiNonHC]"},
    {"name": "LQ4PhiHerm", "delayed": true, "expression": "Module[{a1,a2,b1,b2,b3,c1,c2}, ExpandIndices[ 1/2 Yq11 S1m13bar[c1] S1m13[c1] S1m13bar[c2] S1m13[c2] + 1/2 Yq11t S1tm43bar[c1] S1tm43[c1] S1tm43bar[c2] S1tm43[c2] + 1/2 Yq12 R2bar[a1,c1] R2[a1,c1] R2bar[a2,c2] R2[a2,c2] + 1/2 Yq12t R2tbar[a1,c1] R2t[a1,c1] R2tbar[a2,c2] R2t[a2,c2] + 1/2 Yq13 S3bar[b1,c1] S3[b1,c1] S3bar[b2,c2] S3[b2,c2] + 1/2 Yq32 R2bar[a1,c1] R2[a1,c2] R2bar[a2,c2] R2[a2,c1] + 1/2 Yq32t R2tbar[a1,c1] R2t[a1,c2] R2tbar[a2,c2] R2t[a2,c1] + 1/2 Yq33 S3bar[b1,c1] S3[b1,c2] S3bar[b2,c2] S3[b2,c1] + 1/2 Yq53 S3bar[b1,c1] S3[b2,c1] S3bar[b1,c2] S3[b2,c2] + Yq111t S1m13bar[c1] S1m13[c1] S1tm43bar[c2] S1tm43[c2] + Yp111t S1m13bar[c1] S1m13[c2] S1tm43bar[c2] S1tm43[c1] + Yq112 S1m13bar[c1] S1m13[c1] R2bar[a1,c2] R2[a1,c2] + Yp112 S1m13bar[c1] S1m13[c2] R2bar[a1,c2] R2[a1,c1] + Yq112t S1m13bar[c1] S1m13[c1] R2tbar[a1,c2] R2t[a1,c2] + Yp112t S1m13bar[c1] S1m13[c2] R2tbar[a1,c2] R2t[a1,c1] + Yq113 S1m13bar[c1] S1m13[c1] S3bar[b1,c2] S3[b1,c2] + Yp113 S1m13bar[c1] S1m13[c2] S3bar[b1,c2] S3[b1,c1] + Yq11t2 S1tm43bar[c1] S1tm43[c1] R2bar[a1,c2] R2[a1,c2] + Yp11t2 S1tm43bar[c1] S1tm43[c2] R2bar[a1,c2] R2[a1,c1] + Yq11t2t S1tm43bar[c1] S1tm43[c1] R2tbar[a1,c2] R2t[a1,c2] + Yp11t2t S1tm43bar[c1] S1tm43[c2] R2tbar[a1,c2] R2t[a1,c1] + Yq11t3 S1tm43bar[c1] S1tm43[c1] S3bar[b1,c2] S3[b1,c2] + Yp11t3 S1tm43bar[c1] S1tm43[c2] S3bar[b1,c2] S3[b1,c1] + Yq122t R2bar[a1,c1] R2[a1,c1] R2tbar[a2,c2] R2t[a2,c2] + Yp122t R2bar[a1,c1] R2[a1,c2] R2tbar[a2,c2] R2t[a2,c1] + Yq123 R2bar[a1,c1] R2[a1,c1] S3bar[b1,c2] S3[b1,c2] + Yp123 R2bar[a1,c1] R2[a1,c2] S3bar[b1,c2] S3[b1,c1] + Yq12t3 R2tbar[a1,c1] R2t[a1,c1] S3bar[b1,c2] S3[b1,c2] + Yp12t3 R2tbar[a1,c1] R2t[a1,c2] S3bar[b1,c2] S3[b1,c1] + Yq322t R2bar[a1,c1] R2t[a1,c1] R2tbar[a2,c2] R2[a2,c2] + Yp322t R2bar[a1,c1] R2t[a1,c2] R2tbar[a2,c2] R2[a2,c1] + Yq323 R2bar[a1,c1] 2 Ta[b1,a1,a2] R2[a2,c1] S3bar[b2,c2] I Eps[b1,b2,b3] S3[b3,c2] + Yp323 R2bar[a1,c1] 2 Ta[b1,a1,a2] R2[a2,c2] S3bar[b2,c2] I Eps[b1,b2,b3] S3[b3,c1] + Yq32t3 R2tbar[a1,c1] 2 Ta[b1,a1,a2] R2t[a2,c1] S3bar[b2,c2] I Eps[b1,b2,b3] S3[b3,c2] + Yp32t3 R2tbar[a1,c1] 2 Ta[b1,a1,a2] R2t[a2,c2] S3bar[b2,c2] I Eps[b1,b2,b3] S3[b3,c1], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ4PhiNonHC", "delayed": true, "expression": "Module[{a1,a2,b1,b2,b3,c1,c2}, ExpandIndices[ Y1223 S1m13bar[c1] R2bar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c2] R2[a2,c1] + Yp1223 S1m13bar[c1] R2bar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c1] R2[a2,c2] + Y12t2t3 S1m13bar[c1] R2tbar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c2] R2t[a2,c1] + Yp12t2t3 S1m13bar[c1] R2tbar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c1] R2t[a2,c2] + Y1t2t23 S1tm43bar[c1] R2bar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c2] R2t[a2,c1] + Yp1t2t23 S1tm43bar[c1] R2bar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c1] R2t[a2,c2] + Y11t2t2 S1m13bar[c1] S1tm43[c1] R2tbar[a1,c2] R2[a1,c2] + Yp11t2t2 S1m13bar[c1] S1tm43[c2] R2tbar[a1,c2] R2[a1,c1] + 1/2 Y1313 S1m13bar[c1] S3[b1,c1] S1m13bar[c2] S3[b1,c2] + Y1333 I Eps[b1,b2,b3] S1m13bar[c1] S3[b1,c1] S3bar[b2,c2] S3[b3,c2], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ4Phi", "delayed": true, "expression": "LQ4PhiHerm + LQ4PhiNonHC + HC[LQ4PhiNonHC]"},
    {"name": "LQall", "delayed": true, "expression": "LQ2Phi + LQkin + LQf + LQ3Phi + LQ4Phi"}
  ]
}
```
I've read the paper (Secs. 2–4 and the model-file listings), the schema, and `SM.fr`. No cached or reference `.fr` file for SLQrules was opened.

## Model content extracted

Five scalar-leptoquark SU(2) multiplets (Eq. 22) → **9 colour-triplet complex scalar mass eigenstates** (Eqs. 23, 26): three with Q=−1/3, three with Q=+2/3, two with Q=−4/3, one with Q=+5/3, plus the five unphysical multiplets Φ₁, Φ₁̃, Φ₂, Φ₂̃, Φ₃ that carry the Lagrangian and are rotated into the mass basis by W^q (Eqs. 29–30, 50).

## Mandatory self-audit table

Charges below use SM.fr conventions: `Phi` Y=+1/2, `LL` Y=−1/2, `QL` Y=+1/6, `uR` +2/3, `dR` −1/3, `lR` −1. LQ hypercharges: S1m13 −1/3, S1tm43 −4/3, R2 +7/6, R2t +1/6, S3 −1/3. **There is no new U(1)**, so the "new U(1) sum" column is n/a for every row. Every term is written in the unphysical (SU(2)-multiplet) basis, so a vanishing Y sum on an SU(2)-singlet contraction implies a vanishing Q sum; I list Q sum = 0 accordingly.

| term name | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L/B sum | CC[] used | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LQ2PhiDiag r1 | S1m13bar·S1m13 | 2 | m1^2 | 2 | n/a | 0 | −1/3+1/3=0 | singlet×singlet | 3̄⊗3 shared `c1` | n/a | n/a | n/a | self-conj (real) |
| LQ2PhiDiag r2 | S1tm43bar·S1tm43 | 2 | m1t^2 | 2 | n/a | 0 | 0 | singlet | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r3 | R2bar[a1]·R2[a1] | 2 | m2^2 | 2 | n/a | 0 | 0 | shared SU2D `a1` | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r4 | R2tbar[a1]·R2t[a1] | 2 | m2t^2 | 2 | n/a | 0 | 0 | shared SU2D `a1` | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r5 | S3bar[b1]·S3[b1] | 2 | m3^2 | 2 | n/a | 0 | 0 | shared SU2W `b1` | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r6–10 | Phibar[a1]Phi[a1]·Φa†Φa | 4 | Y1,Y1t,Y2,Y2t,Y3 | 0 | n/a | 0 | 1/2−1/2+0=0 | two shared SU2D/SU2W pairs | shared `c1` | n/a | n/a | n/a | self-conj (Y real) |
| LQ2PhiDiag r11 | Phibar Eps R2bar Phi Eps R2 | 4 | Y22 | 0 | n/a | 0 | (−1/2−7/6)+(1/2+7/6)=0 | `Eps[a1,a2]`, `Eps[a3,a4]` (Hᵀiσ₂Φ₂ and h.c.) | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r12 | Phibar Eps R2tbar Phi Eps R2t | 4 | Y2t2t | 0 | n/a | 0 | 0 | two `Eps[·,·]` | shared `c1` | n/a | n/a | n/a | self-conj |
| LQ2PhiDiag r13 | Eps[b1,b2,b3] Phibar·2Ta·Phi·S3bar S3 | 4 | Y33 | 0 | n/a | 0 | −1/2+1/2+1/3−1/3=0 | `Ta[b1,a1,a2]` + SU2W `Eps[b1,b2,b3]` | shared `c1` | n/a | n/a | n/a | self-conj (I·Y33 real ⇒ herm.) |
| LQ2PhiMix A12t | R2tbar Phi S1m13 | 3 | A12t | 1 (GeV) | n/a | 0 | −1/6+1/2−1/3=0 | shared SU2D `a1` | shared `c1` | n/a | n/a | n/a | `HC[LQ2PhiMixNonHC]` |
| LQ2PhiMix A2t3 | R2tbar·2Ta·Phi·S3 | 3 | A2t3 | 1 (GeV) | n/a | 0 | −1/6−1/3+1/2=0 | `Ta[b1,a1,a2]` | shared `c1` | n/a | n/a | n/a | HC[] |
| LQ2PhiMix Y22t | R2bar Phi · Phi Eps R2t | 4 | Y22t | 0 | n/a | 0 | −7/6+1/2+1/2+1/6=0 | shared `a1`; `Eps[a2,a3]` | shared `c1` | n/a | n/a | n/a | HC[] |
| LQ2PhiMix Y1t3 | Phi Eps 2Ta S3bar Phi S1tm43 | 4 | Y1t3 | 0 | n/a | 0 | 1/2+1/2+1/3−4/3=0 | `Eps[a1,a2]`+`Ta[b1,a2,a3]` (Hᵀiσ₂(σ·Φ₃)†H) | shared `c1` | n/a | n/a | n/a | HC[] |
| LQ2PhiMix Y13 | Phibar 2Ta S3 Phi S1m13bar | 4 | Y13 | 0 | n/a | 0 | −1/2−1/3+1/2+1/3=0 | `Ta[b1,a1,a2]` | shared `c1` | n/a | n/a | n/a | HC[] |
| LQkin (5 rows) | DC[Φabar]DC[Φa] for S1m13, S1tm43, R2, R2t, S3 | 4 | 1 | 0 | n/a | 0 | 0 | shared SU2D/SU2W index | shared `c1` | n/a | n/a | n/a | self-conj; **kinetic+mass term present for all 5 classes ⇒ all 9 physical states** |
| LQf YRR1 | CC[uRbar].lR S1m13bar | 4 | YRR1 | 0 | n/a | 0 | +2/3−1+1/3=0 | all singlets | 3̄(u^c-bar)⊗3̄(Φ₁†)… shared `c1` | n/a | ΔL,ΔB≠0 individually | **yes** (ū′ᶜ) | `HC[LQfNonHC]` |
| LQf YLL1 | CC[QLbar].LL Eps S1m13bar | 4 | YLL1 | 0 | n/a | 0 | 1/6−1/2+1/3=0 | `Eps[a1,a2]` (two same-type doublets) | shared `c1` | n/a | LQ | **yes** | HC[] |
| LQf YQLL1 | CC[QLbar].QL Eps S1m13 Eps[c1,c2,c3] | 4 | YQLL1 (symmetric) | 0 | n/a | 0 | 1/6+1/6−1/3=0 | `Eps[a1,a2]` | colour `Eps[c1,c2,c3]` (3⊗3⊗3→1) | n/a | diquark | **yes** | HC[] |
| LQf YQRR1 | CC[uRbar].dR S1m13 Eps[c1,c2,c3] | 4 | YQRR1 | 0 | n/a | 0 | 2/3−1/3−1/3=0 | singlets | colour `Eps` | n/a | diquark | **yes** | HC[] |
| LQf YRR1t | CC[dRbar].lR S1tm43bar | 4 | YRR1t | 0 | n/a | 0 | −1/3−1+4/3=0 | singlets | shared `c1` | n/a | LQ | **yes** | HC[] |
| LQf YQRR1t | CC[uRbar].uR S1tm43 Eps[c1,c2,c3] | 4 | YQRR1t (antisym.) | 0 | n/a | 0 | 2/3+2/3−4/3=0 | singlets | colour `Eps` | n/a | diquark | **yes** | HC[] |
| LQf YRL2 | uRbar.LL R2 Eps | 4 | YRL2 | 0 | n/a | 0 | −2/3−1/2+7/6=0 | `Eps[a1,a2]` (Φ₂ᵀiσ₂L) | shared `c1` | n/a | LQ | no (no ψᶜ) | HC[] |
| LQf YLR2 | QLbar.lR R2 | 4 | YLR2 | 0 | n/a | 0 | −1/6−1+7/6=0 | shared SU2D `a1` (Q̄ with Φ₂) | shared `c1` | n/a | LQ | no | HC[] |
| LQf YRL2t | dRbar.LL R2t Eps | 4 | YRL2t | 0 | n/a | 0 | 1/3−1/2+1/6=0 | `Eps[a1,a2]` | shared `c1` | n/a | LQ | no | HC[] |
| LQf YLL3 | CC[QLbar].LL Eps 2Ta S3bar | 4 | YLL3 | 0 | n/a | 0 | 1/6−1/2+1/3=0 | `Eps[a1,a2]`+`Ta[b1,a2,a3]` | shared `c1` | n/a | LQ | **yes** | HC[] |
| LQf YQLL3 | CC[QLbar].QL Eps 2Ta S3 Eps[c1,c2,c3] | 4 | YQLL3 (antisym.) | 0 | n/a | 0 | 1/6+1/6−1/3=0 | `Eps`+`Ta` | colour `Eps` | n/a | diquark | **yes** | HC[] |
| L3Φ A12t2t | S1m13 R2t Eps R2t Eps[c1,c2,c3] | 3 | A12t2t | 1 (GeV) | n/a | 0 | −1/3+1/6+1/6=0 | `Eps[a1,a2]` | colour `Eps` | n/a | n/a | n/a | `HC[LQ3PhiNonHC]` |
| L3Φ A1t22t | S1tm43 R2 Eps R2t Eps[c1,c2,c3] | 3 | A1t22t | 1 (GeV) | n/a | 0 | −4/3+7/6+1/6=0 | `Eps[a1,a2]` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y11t2 | S1m13 S1tm43 R2 Eps Phi Eps[c1,c2,c3] | 4 | Y11t2 | 0 | n/a | 0 | −1/3−4/3+7/6+1/2=0 | `Eps[a1,a2]` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y123 | S1m13 Phibar 2Ta S3 R2 Eps[c1,c2,c3] | 4 | Y123 | 0 | n/a | 0 | −1/3−1/2−1/3+7/6=0 | `Ta[b1,a1,a2]` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y12t3 | S1m13 R2t Eps 2Ta S3 Phi Eps[c1,c2,c3] | 4 | Y12t3 | 0 | n/a | 0 | −1/3+1/6−1/3+1/2=0 | `Eps`+`Ta` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y1t23 | S1tm43 R2 Eps 2Ta S3 Phi Eps[c1,c2,c3] | 4 | Y1t23 | 0 | n/a | 0 | −4/3+7/6−1/3+1/2=0 | `Eps`+`Ta` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y233 | Phibar 2Ta R2 S3 I Eps[b] S3 Eps[c1,c2,c3] | 4 | Y233 | 0 | n/a | 0 | −1/2+7/6−1/3−1/3=0 | `Ta` + SU2W `Eps[b1,b2,b3]` | colour `Eps` | n/a | n/a | n/a | HC[] |
| L3Φ Y2t33 | R2t Eps 2Ta Phi S3 I Eps[b] S3 Eps[c] | 4 | Y2t33 | 0 | n/a | 0 | 1/6+1/2−1/3−1/3=0 | `Eps`+`Ta`+SU2W `Eps` | colour `Eps` | n/a | n/a | n/a | HC[] (verbatim Listing 3) |
| L4Φ Yq1a (5 rows: a=1,1̃,2,2̃,3) | (Φa†Φa)(Φa†Φa) | 4 | Yq11…Yq13 | 0 | n/a | 0 | 0 | singlet×singlet | δ_{c1c1}δ_{c2c2} | n/a | n/a | n/a | self-conj |
| L4Φ Yq3a (3 rows: a=2,2̃,3) | (Φa†_{c1}Φa_{c2})(Φa†_{c2}Φa_{c1}) | 4 | Yq32,Yq32t,Yq33 | 0 | n/a | 0 | 0 | singlet×singlet | crossed δ | n/a | n/a | n/a | self-conj |
| L4Φ Yq53 | Φ3^{I†}Φ3^J Φ3^{I†}Φ3^J | 4 | Yq53 | 0 | n/a | 0 | 0 | paired SU2W indices `b1`,`b2` | δ_{c1c1}δ_{c2c2} | n/a | n/a | n/a | self-conj |
| L4Φ Yq1ab / Yp1ab (10 pairs ⇒ 20 rows) | (Φa†Φa)(Φb†Φb), a≠b | 4 | Yq111t…Yp12t3 | 0 | n/a | 0 | 0 | singlet×singlet | δδ (unprimed) / crossed δδ (primed) | n/a | n/a | n/a | self-conj |
| L4Φ Yq322t / Yp322t | (Φ2†Φ2̃)(Φ2̃†Φ2) | 4 | Yq322t, Yp322t | 0 | n/a | 0 | (−7/6+1/6)+(−1/6+7/6)=0 | shared `a1`, shared `a2` | δδ / crossed δδ | n/a | n/a | n/a | self-conj |
| L4Φ Yq3a3 / Yp3a3 (a=2,2̃; 4 rows) | (Φa†σ^IΦa)(Φ3^{J†}iε_{IJK}Φ3^K) | 4 | Yq323…Yp32t3 | 0 | n/a | 0 | 0 | `Ta[b1,a1,a2]` + SU2W `Eps[b1,b2,b3]` | δδ / crossed δδ | n/a | n/a | n/a | self-conj |
| L4Φ Y1aa3 / Yp1aa3 (a=2,2̃; 4 rows) | Φ1†(Φa†(σ·Φ3)Φa) | 4 | Y1223, Yp1223, Y12t2t3, Yp12t2t3 | 0 | n/a | 0 | 1/3−7/6−1/3+7/6=0 (a=2̃: 1/3−1/6−1/3+1/6=0) | `Ta[b1,a1,a2]` | δδ / crossed δδ | n/a | n/a | n/a | `HC[LQ4PhiNonHC]` |
| L4Φ Y1t2t23 / Yp1t2t23 | Φ1̃†(Φ2†(σ·Φ3)Φ2̃) | 4 | Y1t2t23, Yp1t2t23 | 0 | n/a | 0 | 4/3−7/6−1/3+1/6=0 | `Ta` | δδ / crossed δδ | n/a | n/a | n/a | HC[] |
| L4Φ Y11t2t2 / Yp11t2t2 | Φ1†Φ1̃(Φ2̃†Φ2) | 4 | Y11t2t2, Yp11t2t2 | 0 | n/a | 0 | 1/3−4/3−1/6+7/6=0 | singlet×singlet | δδ / crossed δδ | n/a | n/a | n/a | HC[] |
| L4Φ Y1313 | Φ1†Φ3^I Φ1†Φ3^I | 4 | Y1313 | 0 | n/a | 0 | 2(1/3)+2(−1/3)=0 | shared SU2W `b1` | δ_{c1c1}δ_{c2c2} | n/a | n/a | n/a | HC[] |
| L4Φ Y1333 | Φ1†Φ3^I Φ3^{J†}Φ3^K iε_{IJK} | 4 | Y1333 | 0 | n/a | 0 | 1/3−1/3+1/3−1/3=0 | SU2W `Eps[b1,b2,b3]` | δ_{c1c1}δ_{c2c2} | n/a | n/a | n/a | HC[] |

**Kinetic + mass confirmation:** `LQkin` supplies `DC[Φ†]DC[Φ]` and `LQ2PhiDiag` supplies `−m_a² Φ†Φ` for all five multiplet classes S1m13, S1tm43, R2, R2t, S3. Their `Definitions` expand into the nine physical states, whose `Mass -> {…, Internal}` symbols are the diagonalised eigenvalues of Eq. (32); both terms are in the total sum `LQall`.

**SelfConjugate → True classes:** none. Every new class is a complex scalar (`self_conjugate = false`), so no quantum numbers sit on a self-conjugate field.

**Reference/cached model file read:** none. Only the paper text, `frmodel.py`, `render.py` and the supplied `SM.fr` were opened.

**Convention notes.** (i) The schema forbids `External` + `ComplexParameter -> True`, so the couplings the paper declares complex (Listing 1) are emitted as real External parameters; `HC[...]` still generates the correct hermitian partners. (ii) The five unphysical mass parameters get distinct defaults (1000–1400 GeV) because Eqs. (30)/(32) divide by mass-squared differences. (iii) The Σ_{a≠b} quartics are written once per unordered pair.

```json
{
  "model_name": "SLQrules_gen",
  "info": {
    "authors": ["A. Crivellin", "L. Schnell"],
    "version": "1.0",
    "date": "20. 06. 2022",
    "institutions": ["CERN", "Universitaet Zuerich", "Paul Scherrer Institut", "LPTHE Sorbonne Universite", "ETH Zuerich"],
    "emails": ["schnell@mpp.mpg.de"]
  },
  "gauge_groups": [],
  "index_decls": [
    {"name": "LQ3", "range_kind": "NoUnfold", "size": 3, "style_symbol": "nn"},
    {"name": "LQ2", "range_kind": "NoUnfold", "size": 2, "style_symbol": "pp"}
  ],
  "parameters": [
    {"name": "m1", "parameter_type": "External", "value": "1000.", "block_name": "LQMASS", "order_block": 1, "tex": "m_1", "description": "Mass parameter of the scalar leptoquark Phi1 (SU(2) singlet, Y=-1/3) [GeV], Eq.(25)"},
    {"name": "m1t", "parameter_type": "External", "value": "1100.", "block_name": "LQMASS", "order_block": 2, "tex": "m_{1t}", "description": "Mass parameter of the scalar leptoquark Phi1tilde (SU(2) singlet, Y=-4/3) [GeV], Eq.(25)"},
    {"name": "m2", "parameter_type": "External", "value": "1200.", "block_name": "LQMASS", "order_block": 3, "tex": "m_2", "description": "Mass parameter of the scalar leptoquark Phi2 (SU(2) doublet, Y=7/6) [GeV], Eq.(25)"},
    {"name": "m2t", "parameter_type": "External", "value": "1300.", "block_name": "LQMASS", "order_block": 4, "tex": "m_{2t}", "description": "Mass parameter of the scalar leptoquark Phi2tilde (SU(2) doublet, Y=1/6) [GeV], Eq.(25)"},
    {"name": "m3", "parameter_type": "External", "value": "1400.", "block_name": "LQMASS", "order_block": 5, "tex": "m_3", "description": "Mass parameter of the scalar leptoquark Phi3 (SU(2) triplet, Y=-1/3) [GeV], Eq.(25)"},

    {"name": "Y1", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 1, "interaction_order": ["QED", 2], "description": "Coupling Y1 of (H^dag H)(Phi1^dag Phi1), Eq.(25)"},
    {"name": "Y1t", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 2, "interaction_order": ["QED", 2], "description": "Coupling Y1tilde of (H^dag H)(Phi1t^dag Phi1t), Eq.(25)"},
    {"name": "Y2", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 3, "interaction_order": ["QED", 2], "description": "Coupling Y2 of (H^dag H)(Phi2^dag Phi2), Eq.(25)"},
    {"name": "Y2t", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 4, "interaction_order": ["QED", 2], "description": "Coupling Y2tilde of (H^dag H)(Phi2t^dag Phi2t), Eq.(25)"},
    {"name": "Y3", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 5, "interaction_order": ["QED", 2], "description": "Coupling Y3 of (H^dag H)(Phi3^dag Phi3), Eq.(25)"},
    {"name": "Y22", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 6, "interaction_order": ["QED", 2], "description": "Coupling Y22 of |H^T i sigma2 Phi2|^2, Eq.(25)"},
    {"name": "Y2t2t", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 7, "interaction_order": ["QED", 2], "description": "Coupling Y2tilde2tilde of |H^T i sigma2 Phi2t|^2, Eq.(25)"},
    {"name": "Y33", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 8, "interaction_order": ["QED", 2], "description": "Coupling Y33 of i eps_IJK (H^dag sigma_I H) Phi3^J,dag Phi3^K, Eq.(25)"},
    {"name": "Y22t", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 9, "interaction_order": ["QED", 2], "description": "Phi2-Phi2tilde Higgs mixing coupling Y22tilde, Eq.(25)"},
    {"name": "Y1t3", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 10, "interaction_order": ["QED", 2], "description": "Phi1tilde-Phi3 Higgs mixing coupling Y1tilde3, Eq.(25)"},
    {"name": "Y13", "parameter_type": "External", "value": "1.", "block_name": "LQ2PHIY", "order_block": 11, "interaction_order": ["QED", 2], "description": "S3-S1 scalar leptoquark mixing coupling Y13, Eq.(25)"},

    {"name": "A12t", "parameter_type": "External", "value": "1000.", "block_name": "LQ2PHIA", "order_block": 1, "interaction_order": ["QED", 1], "description": "Trilinear Phi1-Phi2tilde-H coupling A_{1 2tilde}, mass dimension 1, units GeV, Eq.(25)"},
    {"name": "A2t3", "parameter_type": "External", "value": "1000.", "block_name": "LQ2PHIA", "order_block": 2, "interaction_order": ["QED", 1], "description": "Trilinear Phi2tilde-Phi3-H coupling A_{2tilde 3}, mass dimension 1, units GeV, Eq.(25)"},

    {"name": "A12t2t", "parameter_type": "External", "value": "1000.", "block_name": "LQ3PHI", "order_block": 1, "interaction_order": ["QED", 1], "description": "Triple LQ coupling A_{1 2tilde 2tilde}, mass dimension 1, units GeV, Eq.(46)"},
    {"name": "A1t22t", "parameter_type": "External", "value": "1000.", "block_name": "LQ3PHI", "order_block": 2, "interaction_order": ["QED", 1], "description": "Triple LQ coupling A_{1tilde 2 2tilde}, mass dimension 1, units GeV, Eq.(46)"},
    {"name": "Y11t2", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 3, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{1 1tilde 2}, Eq.(46)"},
    {"name": "Y123", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 4, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{123}, Eq.(46)"},
    {"name": "Y12t3", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 5, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{1 2tilde 3}, Eq.(46)"},
    {"name": "Y1t23", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 6, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{1tilde 2 3}, Eq.(46)"},
    {"name": "Y233", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 7, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{233}, Eq.(46)"},
    {"name": "Y2t33", "parameter_type": "External", "value": "1.", "block_name": "LQ3PHI", "order_block": 8, "interaction_order": ["QED", 1], "description": "Triple LQ - Higgs coupling Y_{2tilde 3 3}, Eq.(46)"},

    {"name": "Yq11", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 1, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_1, Eq.(49)"},
    {"name": "Yq11t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 2, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_1tilde, Eq.(49)"},
    {"name": "Yq12", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 3, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_2, Eq.(49)"},
    {"name": "Yq12t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 4, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_2tilde, Eq.(49)"},
    {"name": "Yq13", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 5, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_3, Eq.(49)"},
    {"name": "Yq32", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 6, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_2 (crossed colour contraction), Eq.(49)"},
    {"name": "Yq32t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 7, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_2tilde (crossed colour contraction), Eq.(49)"},
    {"name": "Yq33", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 8, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_3 (crossed colour contraction), Eq.(49)"},
    {"name": "Yq53", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 9, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(5)_3, Eq.(49)"},
    {"name": "Yq111t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 10, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1 1tilde}, Eq.(49)"},
    {"name": "Yp111t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 11, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1 1tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq112", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 12, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1 2}, Eq.(49)"},
    {"name": "Yp112", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 13, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1 2} (crossed colour), Eq.(49)"},
    {"name": "Yq112t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 14, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1 2tilde}, Eq.(49)"},
    {"name": "Yp112t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 15, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1 2tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq113", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 16, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1 3}, Eq.(49)"},
    {"name": "Yp113", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 17, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1 3} (crossed colour), Eq.(49)"},
    {"name": "Yq11t2", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 18, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1tilde 2}, Eq.(49)"},
    {"name": "Yp11t2", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 19, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1tilde 2} (crossed colour), Eq.(49)"},
    {"name": "Yq11t2t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 20, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1tilde 2tilde}, Eq.(49)"},
    {"name": "Yp11t2t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 21, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1tilde 2tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq11t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 22, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{1tilde 3}, Eq.(49)"},
    {"name": "Yp11t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 23, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{1tilde 3} (crossed colour), Eq.(49)"},
    {"name": "Yq122t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 24, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{2 2tilde}, Eq.(49)"},
    {"name": "Yp122t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 25, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{2 2tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq123", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 26, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{2 3}, Eq.(49)"},
    {"name": "Yp123", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 27, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{2 3} (crossed colour), Eq.(49)"},
    {"name": "Yq12t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 28, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(1)_{2tilde 3}, Eq.(49)"},
    {"name": "Yp12t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 29, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(1)_{2tilde 3} (crossed colour), Eq.(49)"},
    {"name": "Yq322t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 30, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_{2 2tilde}, Eq.(49)"},
    {"name": "Yp322t", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 31, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(3)_{2 2tilde} (crossed colour), Eq.(49)"},
    {"name": "Yq323", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 32, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_{2 3}, Eq.(49)"},
    {"name": "Yp323", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 33, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(3)_{2 3} (crossed colour), Eq.(49)"},
    {"name": "Yq32t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 34, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y^(3)_{2tilde 3}, Eq.(49)"},
    {"name": "Yp32t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 35, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'^(3)_{2tilde 3} (crossed colour), Eq.(49)"},
    {"name": "Y1223", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 36, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1223}, Eq.(49)"},
    {"name": "Yp1223", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 37, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'_{1223} (crossed colour), Eq.(49)"},
    {"name": "Y12t2t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 38, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1 2tilde 2tilde 3}, Eq.(49)"},
    {"name": "Yp12t2t3", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 39, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'_{1 2tilde 2tilde 3} (crossed colour), Eq.(49)"},
    {"name": "Y1t2t23", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 40, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1tilde 2tilde 2 3}, Eq.(49)"},
    {"name": "Yp1t2t23", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 41, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'_{1tilde 2tilde 2 3} (crossed colour), Eq.(49)"},
    {"name": "Y11t2t2", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 42, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1 1tilde 2tilde 2}, Eq.(49)"},
    {"name": "Yp11t2t2", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 43, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y'_{1 1tilde 2tilde 2} (crossed colour), Eq.(49)"},
    {"name": "Y1313", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 44, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1313}, Eq.(49)"},
    {"name": "Y1333", "parameter_type": "External", "value": "1.", "block_name": "LQ4PHI", "order_block": 45, "interaction_order": ["QED", 2], "description": "Quartic LQ coupling Y_{1333}, Eq.(49)"},

    {"name": "YRR1", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YRR1", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YRR1[1,1]", "rhs": "1."}, {"lhs": "YRR1[1,2]", "rhs": "1."}, {"lhs": "YRR1[1,3]", "rhs": "1."},
      {"lhs": "YRR1[2,1]", "rhs": "1."}, {"lhs": "YRR1[2,2]", "rhs": "1."}, {"lhs": "YRR1[2,3]", "rhs": "1."},
      {"lhs": "YRR1[3,1]", "rhs": "1."}, {"lhs": "YRR1[3,2]", "rhs": "1."}, {"lhs": "YRR1[3,3]", "rhs": "1."}],
      "description": "Y^{RR}_1: Phi1 coupling to ubar^c lepton, Eq.(43)"},
    {"name": "YLL1", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YLL1", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YLL1[1,1]", "rhs": "1."}, {"lhs": "YLL1[1,2]", "rhs": "1."}, {"lhs": "YLL1[1,3]", "rhs": "1."},
      {"lhs": "YLL1[2,1]", "rhs": "1."}, {"lhs": "YLL1[2,2]", "rhs": "1."}, {"lhs": "YLL1[2,3]", "rhs": "1."},
      {"lhs": "YLL1[3,1]", "rhs": "1."}, {"lhs": "YLL1[3,2]", "rhs": "1."}, {"lhs": "YLL1[3,3]", "rhs": "1."}],
      "description": "Y^{LL}_1: Phi1 coupling to Qbar^c L, Eq.(43)"},
    {"name": "YQLL1", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YQLL1", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YQLL1[1,1]", "rhs": "1."}, {"lhs": "YQLL1[1,2]", "rhs": "1."}, {"lhs": "YQLL1[1,3]", "rhs": "1."},
      {"lhs": "YQLL1[2,1]", "rhs": "1."}, {"lhs": "YQLL1[2,2]", "rhs": "1."}, {"lhs": "YQLL1[2,3]", "rhs": "1."},
      {"lhs": "YQLL1[3,1]", "rhs": "1."}, {"lhs": "YQLL1[3,2]", "rhs": "1."}, {"lhs": "YQLL1[3,3]", "rhs": "1."}],
      "description": "Y^{Q,LL}_1: Phi1 diquark coupling, symmetric in flavour, Eq.(43)"},
    {"name": "YQRR1", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YQRR1", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YQRR1[1,1]", "rhs": "1."}, {"lhs": "YQRR1[1,2]", "rhs": "1."}, {"lhs": "YQRR1[1,3]", "rhs": "1."},
      {"lhs": "YQRR1[2,1]", "rhs": "1."}, {"lhs": "YQRR1[2,2]", "rhs": "1."}, {"lhs": "YQRR1[2,3]", "rhs": "1."},
      {"lhs": "YQRR1[3,1]", "rhs": "1."}, {"lhs": "YQRR1[3,2]", "rhs": "1."}, {"lhs": "YQRR1[3,3]", "rhs": "1."}],
      "description": "Y^{Q,RR}_1: Phi1 diquark coupling ubar^c d, Eq.(43)"},
    {"name": "YRR1t", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YRR1T", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YRR1t[1,1]", "rhs": "1."}, {"lhs": "YRR1t[1,2]", "rhs": "1."}, {"lhs": "YRR1t[1,3]", "rhs": "1."},
      {"lhs": "YRR1t[2,1]", "rhs": "1."}, {"lhs": "YRR1t[2,2]", "rhs": "1."}, {"lhs": "YRR1t[2,3]", "rhs": "1."},
      {"lhs": "YRR1t[3,1]", "rhs": "1."}, {"lhs": "YRR1t[3,2]", "rhs": "1."}, {"lhs": "YRR1t[3,3]", "rhs": "1."}],
      "description": "Y^{RR}_1tilde: Phi1tilde coupling to dbar^c lepton, Eq.(43)"},
    {"name": "YQRR1t", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YQRR1T", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YQRR1t[1,1]", "rhs": "0."}, {"lhs": "YQRR1t[1,2]", "rhs": "1."}, {"lhs": "YQRR1t[1,3]", "rhs": "1."},
      {"lhs": "YQRR1t[2,1]", "rhs": "-1."}, {"lhs": "YQRR1t[2,2]", "rhs": "0."}, {"lhs": "YQRR1t[2,3]", "rhs": "1."},
      {"lhs": "YQRR1t[3,1]", "rhs": "-1."}, {"lhs": "YQRR1t[3,2]", "rhs": "-1."}, {"lhs": "YQRR1t[3,3]", "rhs": "0."}],
      "description": "Y^{Q,RR}_1tilde: Phi1tilde diquark coupling ubar^c u, antisymmetric in flavour, Eq.(43)"},
    {"name": "YRL2", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YRL2", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YRL2[1,1]", "rhs": "1."}, {"lhs": "YRL2[1,2]", "rhs": "1."}, {"lhs": "YRL2[1,3]", "rhs": "1."},
      {"lhs": "YRL2[2,1]", "rhs": "1."}, {"lhs": "YRL2[2,2]", "rhs": "1."}, {"lhs": "YRL2[2,3]", "rhs": "1."},
      {"lhs": "YRL2[3,1]", "rhs": "1."}, {"lhs": "YRL2[3,2]", "rhs": "1."}, {"lhs": "YRL2[3,3]", "rhs": "1."}],
      "description": "Y^{RL}_2: Phi2 coupling to ubar L, Eq.(43)"},
    {"name": "YLR2", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YLR2", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YLR2[1,1]", "rhs": "1."}, {"lhs": "YLR2[1,2]", "rhs": "1."}, {"lhs": "YLR2[1,3]", "rhs": "1."},
      {"lhs": "YLR2[2,1]", "rhs": "1."}, {"lhs": "YLR2[2,2]", "rhs": "1."}, {"lhs": "YLR2[2,3]", "rhs": "1."},
      {"lhs": "YLR2[3,1]", "rhs": "1."}, {"lhs": "YLR2[3,2]", "rhs": "1."}, {"lhs": "YLR2[3,3]", "rhs": "1."}],
      "description": "Y^{LR}_2: Phi2 coupling to Qbar lepton_R, Eq.(43)"},
    {"name": "YRL2t", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YRL2T", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YRL2t[1,1]", "rhs": "1."}, {"lhs": "YRL2t[1,2]", "rhs": "1."}, {"lhs": "YRL2t[1,3]", "rhs": "1."},
      {"lhs": "YRL2t[2,1]", "rhs": "1."}, {"lhs": "YRL2t[2,2]", "rhs": "1."}, {"lhs": "YRL2t[2,3]", "rhs": "1."},
      {"lhs": "YRL2t[3,1]", "rhs": "1."}, {"lhs": "YRL2t[3,2]", "rhs": "1."}, {"lhs": "YRL2t[3,3]", "rhs": "1."}],
      "description": "Y^{RL}_2tilde: Phi2tilde coupling to dbar L, Eq.(43)"},
    {"name": "YLL3", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YLL3", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YLL3[1,1]", "rhs": "1."}, {"lhs": "YLL3[1,2]", "rhs": "1."}, {"lhs": "YLL3[1,3]", "rhs": "1."},
      {"lhs": "YLL3[2,1]", "rhs": "1."}, {"lhs": "YLL3[2,2]", "rhs": "1."}, {"lhs": "YLL3[2,3]", "rhs": "1."},
      {"lhs": "YLL3[3,1]", "rhs": "1."}, {"lhs": "YLL3[3,2]", "rhs": "1."}, {"lhs": "YLL3[3,3]", "rhs": "1."}],
      "description": "Y^{LL}_3: Phi3 coupling to Qbar^c L, Eq.(43)"},
    {"name": "YQLL3", "parameter_type": "External", "indices": ["Generation", "Generation"], "block_name": "YQLL3", "interaction_order": ["QED", 1], "value_rules": [
      {"lhs": "YQLL3[1,1]", "rhs": "0."}, {"lhs": "YQLL3[1,2]", "rhs": "1."}, {"lhs": "YQLL3[1,3]", "rhs": "1."},
      {"lhs": "YQLL3[2,1]", "rhs": "-1."}, {"lhs": "YQLL3[2,2]", "rhs": "0."}, {"lhs": "YQLL3[2,3]", "rhs": "1."},
      {"lhs": "YQLL3[3,1]", "rhs": "-1."}, {"lhs": "YQLL3[3,2]", "rhs": "-1."}, {"lhs": "YQLL3[3,3]", "rhs": "0."}],
      "description": "Y^{Q,LL}_3: Phi3 diquark coupling, antisymmetric in flavour, Eq.(43)"},

    {"name": "msq2t1", "parameter_type": "Internal", "value": "m2t^2 - m1^2", "description": "m^2_{2tilde 1} = m2t^2 - m1^2, Eq.(32)"},
    {"name": "msq2t3", "parameter_type": "Internal", "value": "m2t^2 - m3^2", "description": "m^2_{2tilde 3} = m2t^2 - m3^2, Eq.(32)"},
    {"name": "msq12t", "parameter_type": "Internal", "value": "m1^2 - m2t^2", "description": "m^2_{1 2tilde} = m1^2 - m2t^2, Eq.(30)"},
    {"name": "msq32t", "parameter_type": "Internal", "value": "m3^2 - m2t^2", "description": "m^2_{3 2tilde} = m3^2 - m2t^2, Eq.(30)"},
    {"name": "msq13", "parameter_type": "Internal", "value": "m1^2 - m3^2", "description": "m^2_{13} = m1^2 - m3^2, Eq.(30)"},
    {"name": "msq22t", "parameter_type": "Internal", "value": "m2^2 - m2t^2", "description": "m^2_{2 2tilde} = m2^2 - m2t^2, Eq.(30)"},
    {"name": "msq1t3", "parameter_type": "Internal", "value": "m1t^2 - m3^2", "description": "m^2_{1tilde 3} = m1t^2 - m3^2, Eq.(30)"},

    {"name": "W13mat", "parameter_type": "Internal", "complex": true, "indices": ["LQ3", "LQ3"], "value_rules": [
      {"lhs": "W13mat[1,1]", "rhs": "1 - vev^2 Abs[A12t]^2/(4 msq12t^2)"},
      {"lhs": "W13mat[1,2]", "rhs": "vev Conjugate[A12t]/(Sqrt[2] msq12t)"},
      {"lhs": "W13mat[1,3]", "rhs": "vev^2 (Y13 msq12t + Conjugate[A12t] A2t3)/(2 msq13 msq12t)"},
      {"lhs": "W13mat[2,1]", "rhs": "-vev A12t/(Sqrt[2] msq12t)"},
      {"lhs": "W13mat[2,2]", "rhs": "1 - vev^2/4 (Abs[A12t]^2/msq12t^2 + Abs[A2t3]^2/msq32t^2)"},
      {"lhs": "W13mat[2,3]", "rhs": "-vev A2t3/(Sqrt[2] msq32t)"},
      {"lhs": "W13mat[3,1]", "rhs": "-vev^2 (Conjugate[Y13] msq32t + A12t Conjugate[A2t3])/(2 msq13 msq32t)"},
      {"lhs": "W13mat[3,2]", "rhs": "vev Conjugate[A2t3]/(Sqrt[2] msq32t)"},
      {"lhs": "W13mat[3,3]", "rhs": "1 - vev^2 Abs[A2t3]^2/(4 msq32t^2)"}],
      "description": "Unitary rotation W^{-1/3} to the Q=-1/3 leptoquark mass basis, order v^2, Eq.(30)"},
    {"name": "W23mat", "parameter_type": "Internal", "complex": true, "indices": ["LQ3", "LQ3"], "value_rules": [
      {"lhs": "W23mat[1,1]", "rhs": "1"},
      {"lhs": "W23mat[1,2]", "rhs": "vev^2 Y22t/(2 msq22t)"},
      {"lhs": "W23mat[1,3]", "rhs": "0"},
      {"lhs": "W23mat[2,1]", "rhs": "-vev^2 Conjugate[Y22t]/(2 msq22t)"},
      {"lhs": "W23mat[2,2]", "rhs": "1 - vev^2 Abs[A2t3]^2/(2 msq32t^2)"},
      {"lhs": "W23mat[2,3]", "rhs": "-vev A2t3/msq2t3"},
      {"lhs": "W23mat[3,1]", "rhs": "0"},
      {"lhs": "W23mat[3,2]", "rhs": "vev Conjugate[A2t3]/msq2t3"},
      {"lhs": "W23mat[3,3]", "rhs": "1 - vev^2 Abs[A2t3]^2/(2 msq32t^2)"}],
      "description": "Unitary rotation W^{+2/3} to the Q=+2/3 leptoquark mass basis, order v^2, Eq.(30)"},
    {"name": "W43mat", "parameter_type": "Internal", "complex": true, "indices": ["LQ2", "LQ2"], "value_rules": [
      {"lhs": "W43mat[1,1]", "rhs": "1"},
      {"lhs": "W43mat[1,2]", "rhs": "vev^2 Conjugate[Y1t3]/(Sqrt[2] msq1t3)"},
      {"lhs": "W43mat[2,1]", "rhs": "-vev^2 Y1t3/(Sqrt[2] msq1t3)"},
      {"lhs": "W43mat[2,2]", "rhs": "1"}],
      "description": "Unitary rotation W^{-4/3} to the Q=-4/3 leptoquark mass basis, order v^2, Eq.(30)"},

    {"name": "m1m13hat", "parameter_type": "Internal", "value": "Sqrt[m1^2 + vev^2/2 (Y1 - Abs[A12t]^2/msq2t1)]", "description": "Mass of the Q=-1/3 mass eigenstate S1m13hat [GeV], Eq.(32)"},
    {"name": "m2tm13hat", "parameter_type": "Internal", "value": "Sqrt[m2t^2 + vev^2/2 (Y2t + Abs[A12t]^2/msq2t1 + Abs[A2t3]^2/msq2t3)]", "description": "Mass of the Q=-1/3 mass eigenstate R2tm13hat [GeV], Eq.(32)"},
    {"name": "m3m13hat", "parameter_type": "Internal", "value": "Sqrt[m3^2 + vev^2/2 (Y3 - Abs[A2t3]^2/msq2t3)]", "description": "Mass of the Q=-1/3 mass eigenstate S3m13hat [GeV], Eq.(32)"},
    {"name": "m2p23hat", "parameter_type": "Internal", "value": "Sqrt[m2^2 + vev^2/2 Y2]", "description": "Mass of the Q=+2/3 mass eigenstate R2p23hat [GeV], Eq.(32)"},
    {"name": "m2tp23hat", "parameter_type": "Internal", "value": "Sqrt[m2t^2 + vev^2/2 (Y2t + Y2t2t + 2 Abs[A2t3]^2/msq2t3)]", "description": "Mass of the Q=+2/3 mass eigenstate R2tp23hat [GeV], Eq.(32)"},
    {"name": "m3p23hat", "parameter_type": "Internal", "value": "Sqrt[m3^2 + vev^2/2 (Y3 + Y33 - 2 Abs[A2t3]^2/msq2t3)]", "description": "Mass of the Q=+2/3 mass eigenstate S3p23hat [GeV], Eq.(32)"},
    {"name": "m1tm43hat", "parameter_type": "Internal", "value": "Sqrt[m1t^2 + vev^2/2 Y1t]", "description": "Mass of the Q=-4/3 mass eigenstate S1tm43hat [GeV], Eq.(32)"},
    {"name": "m3m43hat", "parameter_type": "Internal", "value": "Sqrt[m3^2 + vev^2/2 (Y3 - Y33)]", "description": "Mass of the Q=-4/3 mass eigenstate S3m43hat [GeV], Eq.(32)"},
    {"name": "m2p53hat", "parameter_type": "Internal", "value": "Sqrt[m2^2 + vev^2/2 (Y2 + Y22)]", "description": "Mass of the Q=+5/3 mass eigenstate R2p53hat [GeV], Eq.(32)"}
  ],
  "particles": [
    {"spin_type": "S", "class_index": 100, "class_name": "S1m13hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m1m13hat", "value": "Internal"}, "width": {"sym": "W1m13hat", "value": "1."},
     "quantum_numbers": {"Q": "-1/3"}, "pdg": 9000001,
     "particle_name": "S1m13hat", "antiparticle_name": "S1m13hat~", "full_name": "S1m13hat",
     "propagator_label": "S1m13hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 101, "class_name": "R2tm13hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m2tm13hat", "value": "Internal"}, "width": {"sym": "W2tm13hat", "value": "1."},
     "quantum_numbers": {"Q": "-1/3"}, "pdg": 9000002,
     "particle_name": "R2tm13hat", "antiparticle_name": "R2tm13hat~", "full_name": "R2tm13hat",
     "propagator_label": "R2tm13hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 102, "class_name": "S3m13hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m3m13hat", "value": "Internal"}, "width": {"sym": "W3m13hat", "value": "1."},
     "quantum_numbers": {"Q": "-1/3"}, "pdg": 9000003,
     "particle_name": "S3m13hat", "antiparticle_name": "S3m13hat~", "full_name": "S3m13hat",
     "propagator_label": "S3m13hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 103, "class_name": "R2p23hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m2p23hat", "value": "Internal"}, "width": {"sym": "W2p23hat", "value": "1."},
     "quantum_numbers": {"Q": "2/3"}, "pdg": 9000004,
     "particle_name": "R2p23hat", "antiparticle_name": "R2p23hat~", "full_name": "R2p23hat",
     "propagator_label": "R2p23hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 104, "class_name": "R2tp23hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m2tp23hat", "value": "Internal"}, "width": {"sym": "W2tp23hat", "value": "1."},
     "quantum_numbers": {"Q": "2/3"}, "pdg": 9000005,
     "particle_name": "R2tp23hat", "antiparticle_name": "R2tp23hat~", "full_name": "R2tp23hat",
     "propagator_label": "R2tp23hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 105, "class_name": "S3p23hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m3p23hat", "value": "Internal"}, "width": {"sym": "W3p23hat", "value": "1."},
     "quantum_numbers": {"Q": "2/3"}, "pdg": 9000006,
     "particle_name": "S3p23hat", "antiparticle_name": "S3p23hat~", "full_name": "S3p23hat",
     "propagator_label": "S3p23hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 106, "class_name": "S1tm43hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m1tm43hat", "value": "Internal"}, "width": {"sym": "W1tm43hat", "value": "1."},
     "quantum_numbers": {"Q": "-4/3"}, "pdg": 9000007,
     "particle_name": "S1tm43hat", "antiparticle_name": "S1tm43hat~", "full_name": "S1tm43hat",
     "propagator_label": "S1tm43hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 107, "class_name": "S3m43hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m3m43hat", "value": "Internal"}, "width": {"sym": "W3m43hat", "value": "1."},
     "quantum_numbers": {"Q": "-4/3"}, "pdg": 9000008,
     "particle_name": "S3m43hat", "antiparticle_name": "S3m43hat~", "full_name": "S3m43hat",
     "propagator_label": "S3m43hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 108, "class_name": "R2p53hat", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "m2p53hat", "value": "Internal"}, "width": {"sym": "W2p53hat", "value": "1."},
     "quantum_numbers": {"Q": "5/3"}, "pdg": 9000009,
     "particle_name": "R2p53hat", "antiparticle_name": "R2p53hat~", "full_name": "R2p53hat",
     "propagator_label": "R2p53hat", "propagator_type": "ScalarDash", "propagator_arrow": "None"},

    {"spin_type": "S", "class_index": 110, "class_name": "S1m13", "self_conjugate": false, "unphysical": true,
     "indices": ["Colour"], "quantum_numbers": {"Y": "-1/3"},
     "definitions": ["S1m13[cc_] :> HC[W13mat[1,1]] S1m13hat[cc] + HC[W13mat[2,1]] R2tm13hat[cc] + HC[W13mat[3,1]] S3m13hat[cc]"]},
    {"spin_type": "S", "class_index": 111, "class_name": "S1tm43", "self_conjugate": false, "unphysical": true,
     "indices": ["Colour"], "quantum_numbers": {"Y": "-4/3"},
     "definitions": ["S1tm43[cc_] :> HC[W43mat[1,1]] S1tm43hat[cc] + HC[W43mat[2,1]] S3m43hat[cc]"]},
    {"spin_type": "S", "class_index": 112, "class_name": "R2", "self_conjugate": false, "unphysical": true,
     "indices": ["SU2D", "Colour"], "flavor_index": "SU2D", "quantum_numbers": {"Y": "7/6"},
     "definitions": [
       "R2[1,cc_] :> R2p53hat[cc]",
       "R2[2,cc_] :> HC[W23mat[1,1]] R2p23hat[cc] + HC[W23mat[2,1]] R2tp23hat[cc] + HC[W23mat[3,1]] S3p23hat[cc]"]},
    {"spin_type": "S", "class_index": 113, "class_name": "R2t", "self_conjugate": false, "unphysical": true,
     "indices": ["SU2D", "Colour"], "flavor_index": "SU2D", "quantum_numbers": {"Y": "1/6"},
     "definitions": [
       "R2t[1,cc_] :> HC[W23mat[1,2]] R2p23hat[cc] + HC[W23mat[2,2]] R2tp23hat[cc] + HC[W23mat[3,2]] S3p23hat[cc]",
       "R2t[2,cc_] :> HC[W13mat[1,2]] S1m13hat[cc] + HC[W13mat[2,2]] R2tm13hat[cc] + HC[W13mat[3,2]] S3m13hat[cc]"]},
    {"spin_type": "S", "class_index": 114, "class_name": "S3", "self_conjugate": false, "unphysical": true,
     "indices": ["SU2W", "Colour"], "flavor_index": "SU2W", "quantum_numbers": {"Y": "-1/3"},
     "definitions": [
       "S3[1,cc_] :> (HC[W23mat[1,3]] R2p23hat[cc] + HC[W23mat[2,3]] R2tp23hat[cc] + HC[W23mat[3,3]] S3p23hat[cc] + HC[W43mat[1,2]] S1tm43hat[cc] + HC[W43mat[2,2]] S3m43hat[cc])/Sqrt[2]",
       "S3[2,cc_] :> I (HC[W23mat[1,3]] R2p23hat[cc] + HC[W23mat[2,3]] R2tp23hat[cc] + HC[W23mat[3,3]] S3p23hat[cc] - HC[W43mat[1,2]] S1tm43hat[cc] - HC[W43mat[2,2]] S3m43hat[cc])/Sqrt[2]",
       "S3[3,cc_] :> HC[W13mat[1,3]] S1m13hat[cc] + HC[W13mat[2,3]] R2tm13hat[cc] + HC[W13mat[3,3]] S3m13hat[cc]"]}
  ],
  "lagrangian_terms": [
    {"name": "LQ2PhiDiag", "delayed": true, "expression": "Module[{a1,a2,a3,a4,b1,b2,b3,c1}, ExpandIndices[ - m1^2 S1m13bar[c1] S1m13[c1] - m1t^2 S1tm43bar[c1] S1tm43[c1] - m2^2 R2bar[a1,c1] R2[a1,c1] - m2t^2 R2tbar[a1,c1] R2t[a1,c1] - m3^2 S3bar[b1,c1] S3[b1,c1] - Y1 Phibar[a1] Phi[a1] S1m13bar[c1] S1m13[c1] - Y1t Phibar[a1] Phi[a1] S1tm43bar[c1] S1tm43[c1] - Y2 Phibar[a1] Phi[a1] R2bar[a2,c1] R2[a2,c1] - Y2t Phibar[a1] Phi[a1] R2tbar[a2,c1] R2t[a2,c1] - Y3 Phibar[a1] Phi[a1] S3bar[b1,c1] S3[b1,c1] - Y22 Phibar[a1] Eps[a1,a2] R2bar[a2,c1] Phi[a3] Eps[a3,a4] R2[a4,c1] - Y2t2t Phibar[a1] Eps[a1,a2] R2tbar[a2,c1] Phi[a3] Eps[a3,a4] R2t[a4,c1] - I Y33 Eps[b1,b2,b3] Phibar[a1] 2 Ta[b1,a1,a2] Phi[a2] S3bar[b2,c1] S3[b3,c1], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ2PhiMixNonHC", "delayed": true, "expression": "Module[{a1,a2,a3,b1,c1}, ExpandIndices[ - A12t R2tbar[a1,c1] Phi[a1] S1m13[c1] + A2t3 R2tbar[a1,c1] 2 Ta[b1,a1,a2] Phi[a2] S3[b1,c1] + Y22t R2bar[a1,c1] Phi[a1] Phi[a2] Eps[a2,a3] R2t[a3,c1] + Y1t3 Phi[a1] Eps[a1,a2] 2 Ta[b1,a2,a3] S3bar[b1,c1] Phi[a3] S1tm43[c1] + Y13 Phibar[a1] 2 Ta[b1,a1,a2] S3[b1,c1] Phi[a2] S1m13bar[c1], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ2Phi", "delayed": true, "expression": "LQ2PhiDiag + LQ2PhiMixNonHC + HC[LQ2PhiMixNonHC]"},
    {"name": "LQkin", "delayed": true, "expression": "Module[{mu,a1,b1,c1}, ExpandIndices[ DC[S1m13bar[c1],mu] DC[S1m13[c1],mu] + DC[S1tm43bar[c1],mu] DC[S1tm43[c1],mu] + DC[R2bar[a1,c1],mu] DC[R2[a1,c1],mu] + DC[R2tbar[a1,c1],mu] DC[R2t[a1,c1],mu] + DC[S3bar[b1,c1],mu] DC[S3[b1,c1],mu], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQfNonHC", "delayed": true, "expression": "Module[{sp,a1,a2,a3,b1,c1,c2,c3,f1,f2}, ExpandIndices[ YRR1[f1,f2] CC[uRbar[sp,f1,c1]].lR[sp,f2] S1m13bar[c1] + YLL1[f1,f2] CC[QLbar[sp,a1,f1,c1]].LL[sp,a2,f2] Eps[a1,a2] S1m13bar[c1] + YQLL1[f1,f2] CC[QLbar[sp,a1,f1,c1]].QL[sp,a2,f2,c2] Eps[a1,a2] S1m13[c3] Eps[c1,c2,c3] + YQRR1[f1,f2] CC[uRbar[sp,f1,c1]].dR[sp,f2,c2] S1m13[c3] Eps[c1,c2,c3] + YRR1t[f1,f2] CC[dRbar[sp,f1,c1]].lR[sp,f2] S1tm43bar[c1] + YQRR1t[f1,f2] CC[uRbar[sp,f1,c1]].uR[sp,f2,c2] S1tm43[c3] Eps[c1,c2,c3] + YRL2[f1,f2] uRbar[sp,f1,c1].LL[sp,a2,f2] R2[a1,c1] Eps[a1,a2] + YLR2[f1,f2] QLbar[sp,a1,f1,c1].lR[sp,f2] R2[a1,c1] + YRL2t[f1,f2] dRbar[sp,f1,c1].LL[sp,a2,f2] R2t[a1,c1] Eps[a1,a2] + YLL3[f1,f2] CC[QLbar[sp,a1,f1,c1]].LL[sp,a3,f2] Eps[a1,a2] 2 Ta[b1,a2,a3] S3bar[b1,c1] + YQLL3[f1,f2] CC[QLbar[sp,a1,f1,c1]].QL[sp,a3,f2,c2] Eps[a1,a2] 2 Ta[b1,a2,a3] S3[b1,c3] Eps[c1,c2,c3], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQf", "delayed": true, "expression": "LQfNonHC + HC[LQfNonHC]"},
    {"name": "LQ3PhiNonHC", "delayed": true, "expression": "Module[{a1,a2,a3,b1,b2,b3,c1,c2,c3}, ExpandIndices[ A12t2t S1m13[c1] R2t[a1,c2] Eps[a1,a2] R2t[a2,c3] Eps[c1,c2,c3] + A1t22t S1tm43[c1] R2[a1,c2] Eps[a1,a2] R2t[a2,c3] Eps[c1,c2,c3] + Y11t2 S1m13[c1] S1tm43[c2] R2[a1,c3] Eps[a1,a2] Phi[a2] Eps[c1,c2,c3] + Y123 S1m13[c1] Phibar[a1] 2 Ta[b1,a1,a2] S3[b1,c3] R2[a2,c2] Eps[c1,c2,c3] + Y12t3 S1m13[c1] R2t[a1,c2] Eps[a1,a2] 2 Ta[b1,a2,a3] S3[b1,c3] Phi[a3] Eps[c1,c2,c3] + Y1t23 S1tm43[c1] R2[a1,c2] Eps[a1,a2] 2 Ta[b1,a2,a3] S3[b1,c3] Phi[a3] Eps[c1,c2,c3] + Y233 Phibar[a1] 2 Ta[b1,a1,a2] R2[a2,c1] S3[b2,c2] I Eps[b1,b2,b3] S3[b3,c3] Eps[c1,c2,c3] + Y2t33 R2t[a1,c1] Eps[a1,a2] 2 Ta[b1,a2,a3] Phi[a3] S3[b2,c2] I Eps[b1,b2,b3] S3[b3,c3] Eps[c1,c2,c3], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ3Phi", "delayed": true, "expression": "LQ3PhiNonHC + HC[LQ3PhiNonHC]"},
    {"name": "LQ4PhiHerm", "delayed": true, "expression": "Module[{a1,a2,b1,b2,b3,c1,c2}, ExpandIndices[ 1/2 Yq11 S1m13bar[c1] S1m13[c1] S1m13bar[c2] S1m13[c2] + 1/2 Yq11t S1tm43bar[c1] S1tm43[c1] S1tm43bar[c2] S1tm43[c2] + 1/2 Yq12 R2bar[a1,c1] R2[a1,c1] R2bar[a2,c2] R2[a2,c2] + 1/2 Yq12t R2tbar[a1,c1] R2t[a1,c1] R2tbar[a2,c2] R2t[a2,c2] + 1/2 Yq13 S3bar[b1,c1] S3[b1,c1] S3bar[b2,c2] S3[b2,c2] + 1/2 Yq32 R2bar[a1,c1] R2[a1,c2] R2bar[a2,c2] R2[a2,c1] + 1/2 Yq32t R2tbar[a1,c1] R2t[a1,c2] R2tbar[a2,c2] R2t[a2,c1] + 1/2 Yq33 S3bar[b1,c1] S3[b1,c2] S3bar[b2,c2] S3[b2,c1] + 1/2 Yq53 S3bar[b1,c1] S3[b2,c1] S3bar[b1,c2] S3[b2,c2] + Yq111t S1m13bar[c1] S1m13[c1] S1tm43bar[c2] S1tm43[c2] + Yp111t S1m13bar[c1] S1m13[c2] S1tm43bar[c2] S1tm43[c1] + Yq112 S1m13bar[c1] S1m13[c1] R2bar[a1,c2] R2[a1,c2] + Yp112 S1m13bar[c1] S1m13[c2] R2bar[a1,c2] R2[a1,c1] + Yq112t S1m13bar[c1] S1m13[c1] R2tbar[a1,c2] R2t[a1,c2] + Yp112t S1m13bar[c1] S1m13[c2] R2tbar[a1,c2] R2t[a1,c1] + Yq113 S1m13bar[c1] S1m13[c1] S3bar[b1,c2] S3[b1,c2] + Yp113 S1m13bar[c1] S1m13[c2] S3bar[b1,c2] S3[b1,c1] + Yq11t2 S1tm43bar[c1] S1tm43[c1] R2bar[a1,c2] R2[a1,c2] + Yp11t2 S1tm43bar[c1] S1tm43[c2] R2bar[a1,c2] R2[a1,c1] + Yq11t2t S1tm43bar[c1] S1tm43[c1] R2tbar[a1,c2] R2t[a1,c2] + Yp11t2t S1tm43bar[c1] S1tm43[c2] R2tbar[a1,c2] R2t[a1,c1] + Yq11t3 S1tm43bar[c1] S1tm43[c1] S3bar[b1,c2] S3[b1,c2] + Yp11t3 S1tm43bar[c1] S1tm43[c2] S3bar[b1,c2] S3[b1,c1] + Yq122t R2bar[a1,c1] R2[a1,c1] R2tbar[a2,c2] R2t[a2,c2] + Yp122t R2bar[a1,c1] R2[a1,c2] R2tbar[a2,c2] R2t[a2,c1] + Yq123 R2bar[a1,c1] R2[a1,c1] S3bar[b1,c2] S3[b1,c2] + Yp123 R2bar[a1,c1] R2[a1,c2] S3bar[b1,c2] S3[b1,c1] + Yq12t3 R2tbar[a1,c1] R2t[a1,c1] S3bar[b1,c2] S3[b1,c2] + Yp12t3 R2tbar[a1,c1] R2t[a1,c2] S3bar[b1,c2] S3[b1,c1] + Yq322t R2bar[a1,c1] R2t[a1,c1] R2tbar[a2,c2] R2[a2,c2] + Yp322t R2bar[a1,c1] R2t[a1,c2] R2tbar[a2,c2] R2[a2,c1] + Yq323 R2bar[a1,c1] 2 Ta[b1,a1,a2] R2[a2,c1] S3bar[b2,c2] I Eps[b1,b2,b3] S3[b3,c2] + Yp323 R2bar[a1,c1] 2 Ta[b1,a1,a2] R2[a2,c2] S3bar[b2,c2] I Eps[b1,b2,b3] S3[b3,c1] + Yq32t3 R2tbar[a1,c1] 2 Ta[b1,a1,a2] R2t[a2,c1] S3bar[b2,c2] I Eps[b1,b2,b3] S3[b3,c2] + Yp32t3 R2tbar[a1,c1] 2 Ta[b1,a1,a2] R2t[a2,c2] S3bar[b2,c2] I Eps[b1,b2,b3] S3[b3,c1], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ4PhiNonHC", "delayed": true, "expression": "Module[{a1,a2,b1,b2,b3,c1,c2}, ExpandIndices[ Y1223 S1m13bar[c1] R2bar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c2] R2[a2,c1] + Yp1223 S1m13bar[c1] R2bar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c1] R2[a2,c2] + Y12t2t3 S1m13bar[c1] R2tbar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c2] R2t[a2,c1] + Yp12t2t3 S1m13bar[c1] R2tbar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c1] R2t[a2,c2] + Y1t2t23 S1tm43bar[c1] R2bar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c2] R2t[a2,c1] + Yp1t2t23 S1tm43bar[c1] R2bar[a1,c2] 2 Ta[b1,a1,a2] S3[b1,c1] R2t[a2,c2] + Y11t2t2 S1m13bar[c1] S1tm43[c1] R2tbar[a1,c2] R2[a1,c2] + Yp11t2t2 S1m13bar[c1] S1tm43[c2] R2tbar[a1,c2] R2[a1,c1] + 1/2 Y1313 S1m13bar[c1] S3[b1,c1] S1m13bar[c2] S3[b1,c2] + Y1333 I Eps[b1,b2,b3] S1m13bar[c1] S3[b1,c1] S3bar[b2,c2] S3[b3,c2], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LQ4Phi", "delayed": true, "expression": "LQ4PhiHerm + LQ4PhiNonHC + HC[LQ4PhiNonHC]"},
    {"name": "LQall", "delayed": true, "expression": "LQ2Phi + LQkin + LQf + LQ3Phi + LQ4Phi"}
  ]
}
```