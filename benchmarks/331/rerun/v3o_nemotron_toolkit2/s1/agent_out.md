## Self-Audit Table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1)_X sum | L/B sum | CC[] used | frac/root checked | Hermitian partner |
|-----------|------------------------|---------------------------|-----------------|-------------------------------|----------------|-------|-------|-------------------|-------------------|----------------|---------|-----------|-------------------|-------------------|
| LZpKin | Zp, Zp | 4 | MZp | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (mass term) | self-conjugate |
| LVKin | Vp, Vpbar | 4 | MV | 1 | n/a | QV + (-QV)=0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (mass term) | HC[LVKin] |
| LYKin | Yp, Ypbar | 4 | MY | 1 | n/a | QY + (-QY)=0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (mass term) | HC[LYKin] |
| LH0Kin | H0, H0 | 4 | MH0 | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (mass term) | self-conjugate |
| LH2Kin | H2, H2 | 4 | MH2 | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (mass term) | self-conjugate |
| LH3Kin | H3, H3 | 4 | MH3 | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (mass term) | self-conjugate |
| LHpKin | Hp, Hpbar | 4 | MHpm | 1 | n/a | 1 + (-1)=0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (mass term) | HC[LHpKin] |
| LHVKin | HVp, HVpbar | 4 | MHQV | 1 | n/a | QV + (-QV)=0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (mass term) | HC[LHVKin] |
| LHYKin | HYp, HYpbar | 4 | MHQY | 1 | n/a | QY + (-QY)=0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a (mass term) | HC[LHYKin] |
| LDqKin | Dq, Dqbar | 4 | MDq | 1 | n/a | QD + (-QD)=0 | 0 | singlet | δ^a_b | 0 | 1/3 + (-1/3)=0 | n/a | n/a (mass term) | HC[LDqKin] |
| LTqKin | Tq, Tqbar | 4 | MTq | 1 | n/a | QT + (-QT)=0 | 0 | singlet | δ^a_b | 0 | 1/3 + (-1/3)=0 | n/a | n/a (mass term) | HC[LTqKin] |
| LElKin | El, Elbar | 4 | MEe | 1 | n/a | QE + (-QE)=0 | 0 | singlet | singlet | 0 | 1 + (-1)=0 | n/a | n/a (mass term) | HC[LElKin] |
| LZpNewFerm | Zp, Dq, Dqbar, Tq, Tqbar, El, Elbar | 4 | gZp* | 0 | n/a | 0 | 0 | singlet | δ^a_b (quarks) | 0 | 0 | no | n/a (dim-4) | self-conjugate (Zp real) |
| LVNewFerm | Vp, Dq, dqbar, Tq, bqbar | 4 | gV* | 0 | n/a | QV + QD + (-2/3) = 0 | 0 | ProjM | δ^a_b | 0 | 0 | no | n/a (dim-4) | explicit HC[] |
| LYNewFerm | Yp, Dq, uqbar, El, vlbar | 4 | gY* | 0 | n/a | QY + QD + (-2/3) = 0 | 0 | ProjM | δ^a_b | 0 | 0 | no | n/a (dim-4) | explicit HC[] |
| LVSint | Vp, Hp, Hpbar, Yp, HYp, HYpbar | 4 | ee | 0 | n/a | QV + 1 + (-1)=0 | 0 | singlet | singlet | 0 | 0 | no | am, ap from paper Eq.1736 | self-conjugate (real) |
| LVVSint | Vp, Vpbar, Hp, Hpbar, HVp, HVpbar, Yp, Ypbar | 4 | ee^2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | no | n/a (dim-4) | self-conjugate (real) |
| LYukNew | Dq, Dqbar, Tq, Tqbar, El, Elbar | 4 | y* v3 | 1 | n/a | 0 | 0 | singlet | δ^a_b (quarks) | 0 | 0 | no | v3/Sqrt[2] from paper Eq.193 | HC[LYukNew] |

### Additional Verification Rows

| check | result |
|-------|--------|
| **Particle kinetic+mass terms in LTotal** | All 12 new particle classes (Zp, Vp, Yp, H0, H2, H3, Hp, HVp, HYp, Dq, Tq, El) have kinetic+mass terms (LZpKin, LVKin, LYKin, LH0Kin, LH2Kin, LH3Kin, LHpKin, LHVKin, LHYKin, LDqKin, LTqKin, LElKin) and all appear in LTotal |
| **Non-fundamental color representations** | None — all colored fields use fundamental Colour index (triplet); no sextet/octet indices declared |
| **SelfConjugate classes carry no QuantumNumbers** | Zp (Q=0), H0 (Q=0), H2 (Q=0), H3 (Q=0) — all have only Q=0 which is allowed; no charged SelfConjugate fields |
| **Name collision check** | All class names (Zp, Vp, Yp, H0, H2, H3, Hp, HVp, HYp, Dq, Tq, El), parameter names (beta, v1, v2, v3, k, g, gX, lam1, lam2, lam3, lam12, lam13, lam23, lam12p, lam13p, lam23p, yD, yS, yT, yEe, yEmu, yEtau, gZpDqL, gZpDqR, gZpTqL, gZpTqR, gZpElL, gZpElR, gVdqL, gVTqL, gYdqL, gYElL, f, v, gY, sW, cW, ee, a0, ap, am, bp, bm, QV, QY, QD, QT, QE, Xrho, Xeta, Xchi, s12, c12, s23, c23, s13, c13, MZp, MV, MY, MH3, MH2, MH0, MHpm, MHQV, MHQY, MDq, MSq, MTq, MEe, MEmu, MEtau, MEl, U11, U21, U31, U12, U22, U32, U13, U23, U33, O11, O12, O13, O21, O22, O23, O31, O32, O33), and index names (Generation, Colour, Gluon, SU2D, SU2W) are distinct from Mathematica built-ins, FeynRules symbols (HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM), and SM.fr names (A, Z, W, G, B, Wi, Phi, H, G0, GP, vl, l, uq, dq, uR, dR, QL, LL, ee, gs, gw, g1, sw, cw, vev, MZ, MW, MH, MD, MS, MT, MB, MU, MC, Me, MMU, MTA, yu, yd, yl, CKM) |
| **Single total Lagrangian** | LTotal = LZpKin + LVKin + LYKin + LH0Kin + LH2Kin + LH3Kin + LHpKin + LHVKin + LHYKin + LDqKin + LTqKin + LElKin + LZpNewFerm + LVNewFerm + LYNewFerm + LVSint + LVVSint + LYukNew |
| **Reference/cached model files read** | none — only the paper LaTeX source (1611.09337_source.tex) and SM.fr were read |

---

**Last `./frgen spec.json` result:**
```
SCHEMA OK: 12 particle classes, 91 parameters, Lagrangian terms ['LZpKin', 'LVKin', 'LYKin', 'LH0Kin', 'LH2Kin', 'LH3Kin', 'LHpKin', 'LHVKin', 'LHYKin', 'LDqKin', 'LTqKin', 'LElKin', 'LZpNewFerm', 'LVNewFerm', 'LYNewFerm', 'LVSint', 'LVVSint', 'LYukNew', 'LTotal']
RENDERED: model.fr (791 lines). You may read it.
LINT: no findings.
```