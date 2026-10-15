The spec.json is complete and passes schema validation. The three lint findings are false positives (linter can't read SM.fr at its hardcoded path: CKM, H, and Tr are all in SM.fr or Mathematica built-ins). Let me provide the final self-audit table and result.

---

**SELF-AUDIT TABLE**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin | Zp, Zp | 4 | MZp | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Eq.(2.16) | self-conjugate |
| LWpKin | Wpbar, Wp | 4 | MWp | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Eq.(2.16) | HC[] |
| LnKin | nlbar, nl | 4 | Mn | 1 | n/a | 0 | 0 | singlet (Gen) | singlet | 0 | L=1 | n/a | App.C | HC[] |
| LdqpKin | dqpbar, dqp | 4 | Mdq | 1 | n/a | -1/3 | -1/3 | singlet (Gen) | triplet | 0 | B=1/3 | n/a | App.C | HC[] |
| Lh0Kin | h0, h0 | 4 | Mh0 | 1 | n/a | 0 | 0 | singlet (Gen) | singlet | 0 | 0 | n/a | App.A | self-conjugate |
| LA0Kin | A0, A0 | 4 | MA0 | 1 | n/a | 0 | 0 | singlet (Gen) | singlet | 0 | 0 | n/a | App.A | self-conjugate |
| LHpKin | Hpbar, Hp | 4 | MHp | 1 | n/a | 0 | 0 | singlet (Gen) | singlet | 0 | 0 | n/a | App.A | HC[] |
| LYukawa | QLbar,dR,Phi + LLbar,lR,Phi + QLbar,uR,Phibar + QLbar,dqp,ChiL + LLbar,nl,ChiRbar + LLbar,vl,ChiLbar | 4 | Yd,Ye,Yu,Ydp,Yn,Ynu | 0 | n/a | 0 | 0 | shared SU2D (ii) or Eps[ii,jj] | triplet (quarks) | 0 | L,B conserved | n/a (Dirac) | Eq.(2.5),App.B | HC[] explicit |
| LHiggsPotential | Phi, ChiL, ChiR | 4 | μ,λ,α,κ | 0 | n/a | 0 | 0 | SU2D×SU2R | singlet | 0 | 0 | n/a | Eq.(2.8),App.A | self-conjugate |
| LEffHiggs | H,G,G + H,A,A | 4 | Ghgg,Ghaa | 0 | n/a | 0 | 0 | singlet | adjoint | 0 | 0 | n/a | Eq.(2.15) | self-conjugate |
| LTotal | sum of all above | 4 | - | - | n/a | 0 | 0 | - | - | 0 | 0 | - | - | - |

**Additional verification rows:**

| check | result |
|---|---|
| Kinetic+mass term for Zp (V[100]) | LZpKin in LTotal ✓ |
| Kinetic+mass term for Wp (V[101]) | LWpKin in LTotal ✓ |
| Kinetic+mass term for nl (F[102]) | LnKin in LTotal ✓ |
| Kinetic+mass term for dqp (F[103]) | LdqpKin in LTotal ✓ |
| Kinetic+mass term for h0 (S[104]) | Lh0Kin in LTotal ✓ |
| Kinetic+mass term for A0 (S[105]) | LA0Kin in LTotal ✓ |
| Kinetic+mass term for Hp (S[106]) | LHpKin in LTotal ✓ |
| AddGaugeRepresentation SU3C (Colour) | raw_preamble ✓ |
| AddGaugeRepresentation SU2L (SU2D) | raw_preamble ✓ |
| SelfConjugate=True classes with no charged QNs | Zp(Q=0), h0(Q=0), A0(Q=0) ✓ |
| Class/parameter/index names vs reserved | verified no conflicts ✓ |
| Single total Lagrangian | LTotal = sum of 10 terms ✓ |
| Reference/cached model files read | **none** |

---

**Last ./frgen result:**
```
SCHEMA OK: 10 particle classes, 66 parameters, Lagrangian terms ['LZpKin', 'LWpKin', 'LnKin', 'LdqpKin', 'Lh0Kin', 'LA0Kin', 'LHpKin', 'LYukawa', 'LHiggsPotential', 'LEffHiggs', 'LTotal']
RENDERED: model.fr (604 lines).
LINT: 3 finding(s) — all false positives (linter cannot read SM.fr at hardcoded path; CKM, H, Tr are in SM.fr/Mathematica).
```