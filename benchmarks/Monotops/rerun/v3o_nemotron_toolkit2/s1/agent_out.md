**Self-Audit Table for Monotops_gen**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power (d-4 or n/a) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LphiKin | phi, phi | 4 | - | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LchiKin | chibar, chi, DC | 4 | - | 0 | n/a | 2/3 + (-2/3)=0 | 2/3 + (-2/3)=0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate (Dirac) |
| LVKin | V, V, FS | 4 | - | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| Lphi3Kin | phi3bar, phi3, DC | 4 | - | 0 | n/a | 0 | 0 | singlet | phi3bar(3bar) phi3(3) | 0 | 0 | n/a | n/a | self-conjugate |
| LphitildeKin | phitildebar, phitilde, DC | 4 | - | 0 | n/a | -1 + 1 = 0 | -1 + 1 = 0 | singlet | phitildebar(3bar) phitilde(3) | 0 | 0 | n/a | n/a | self-conjugate |
| LXKin | Xbar, X, FS | 4 | - | 0 | n/a | 0 | 0 | singlet | Xbar(3bar) X(3) | 0 | 0 | n/a | n/a | self-conjugate |
| LintFCNCscalar | phi, uqbar, uq | 4 | a0FC, b0FC | 0 | n/a | 0 + (-2/3) + 2/3 = 0 | 0 + (-2/3) + 2/3 = 0 | singlet | singlet | 0 | 0 | n/a | LaTeX \bar{u}(a+b\gamma5)u exact | HC[LintFCNCscalar] in LTotal |
| LintFCNCvector | V, uqbar, uq | 4 | a1FC, b1FC | 0 | n/a | 0 + (-2/3) + 2/3 = 0 | 0 + (-2/3) + 2/3 = 0 | singlet | singlet | 0 | 0 | n/a | LaTeX \bar{u}\gamma^\mu(a+b\gamma5)u exact | HC[LintFCNCvector] in LTotal |
| LintPhiDD | phi3, dq^c, dq | 4 | aqSR, bqSR | 0 | n/a | 0 + 1/3 + (-1/3) = 0 | 0 + 1/3 + (-1/3) = 0 | singlet | eps3[i,j,k] 3x3x3->1 | 0 | B: 2/3+2/3=4/3 | yes (CC[dqbar]) | LaTeX \bar{d^c}(a+b\gamma5)d exact | HC[LintPhiDD] in LTotal |
| LintPhiUChi | phi3, uqbar, chi | 4 | ahalfSR, bhalfSR | 0 | n/a | 0 + (-2/3) + 2/3 = 0 | 0 + (-2/3) + 2/3 = 0 | singlet | phi3(3) uqbar(3bar) | 0 | 0 | n/a | LaTeX \bar{u}(a+b\gamma5)\chi exact | HC[LintPhiUChi] in LTotal |
| LintPhiTildeDU | phitilde, dq^c, uq | 4 | aqtildeSR, bqtildeSR | 0 | n/a | -1 + 1/3 + 2/3 = 0 | -1 + 1/3 + 2/3 = 0 | singlet | eps3[i,j,k] 3x3x3->1 | 0 | B: 2/3+2/3=4/3 | yes (CC[dqbar]) | LaTeX \bar{d^c}(a+b\gamma5)u exact | HC[LintPhiTildeDU] in LTotal |
| LintPhiTildeDChi | phitilde, dqbar, chi | 4 | ahalftildeSR, bhalftildeSR | 0 | n/a | -1 + 1/3 + 2/3 = 0 | -1 + 1/3 + 2/3 = 0 | singlet | phitilde(3) dqbar(3bar) | 0 | 0 | n/a | LaTeX \bar{d}(a+b\gamma5)\chi exact | HC[LintPhiTildeDChi] in LTotal |
| LintXDD | X, dq^c, dq | 4 | aqVR, bqVR | 0 | n/a | 0 + 1/3 + (-1/3) = 0 | 0 + 1/3 + (-1/3) = 0 | singlet | eps3[i,j,k] 3x3x3->1 | 0 | B: 2/3+2/3=4/3 | yes (CC[dqbar]) | LaTeX \bar{d^c}\gamma^\mu(a+b\gamma5)d exact | HC[LintXDD] in LTotal |
| LintXUChi | X, uqbar, chi | 4 | ahalfVR, bhalfVR | 0 | n/a | 0 + (-2/3) + 2/3 = 0 | 0 + (-2/3) + 2/3 = 0 | singlet | X(3) uqbar(3bar) | 0 | 0 | n/a | LaTeX \bar{u}\gamma^\mu(a+b\gamma5)\chi exact | HC[LintXUChi] in LTotal |
| LTotal | sum of all above + HC[] | 4 | - | 0 | n/a | 0 | 0 | - | - | 0 | 0 | - | - | single total |

**Additional audit rows:**

| Check | Result |
|---|---|
| Kinetic+mass terms for all 6 new particle classes | All present: LphiKin, LchiKin, LVKin, Lphi3Kin, LphitildeKin, LXKin |
| AddGaugeRepresentation for color triplet | Present in raw_preamble: AddGaugeRepresentation[SU3C -> {T3, Triplet}] |
| SelfConjugate=True classes with no QuantumNumbers | phi (Q=0), V (Q=0) - zero charge acceptable |
| Name collisions with Mathematica/FeynRules/SM.fr | None |
| Single total Lagrangian | LTotal sums all 14 terms + their HC[] |
| Reference/cached model files read | none |

**Last ./frgen result:**
```
SCHEMA OK: 6 particle classes, 23 parameters, Lagrangian terms ['LphiKin', 'LchiKin', 'LVKin', 'Lphi3Kin', 'LphitildeKin', 'LXKin', 'LintFCNCscalar', 'LintFCNCvector', 'LintPhiDD', 'LintPhiUChi', 'LintPhiTildeDU', 'LintPhiTildeDChi', 'LintXDD', 'LintXUChi', 'LTotal']
RENDERED: model.fr (257 lines). You may read it.
LINT: no findings.
```