**SELF-AUDIT TABLE**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNkin | Nbar, N, del | 4 (kin), 3 (mass) | 1, mN | 0, 1 | n/a (d≤4) | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LW | W, Nbar, l | 4 | gw/Sqrt[2] | 0 | n/a | 0 | 0 | from SU(2) singlet Weinberg op | singlet | n/a | 0 | no | LaTeX Eq.(366): gw/Sqrt[2] exact | HC[LW] |
| LZ | Z, Nbar, vl | 4 | gw/(2*cw) | 0 | n/a | 0 | 0 | from SU(2) singlet Weinberg op | singlet | n/a | 0 | no | LaTeX Eq.(367): gw/(2*cw) exact | HC[LZ] |
| Lh | h, Nbar, vl (+ h²) | 4, 5 | gw·mN/(2·mW), gw²·mN/(8·mW²) | 0, -1 | absorbed in mN (d=5: 1/Λ) | 0 | 0 | from SU(2) singlet Weinberg op | singlet | n/a | 0 | no | LaTeX Eq.(368-369): fractions exact | HC[Lh] |
| LGP | GP, Nbar, l, bar[CC[l]], N (+ GP·h) | 4, 5 | gw·mN/(2√2·mW), gw²·mN/(4√2·mW²) | 0, -1 | absorbed in mN | 0 | 0 | from SU(2) singlet Weinberg op | singlet | n/a | 0 | yes (bar[CC[l]]) | LaTeX Eq.(370-371): fractions exact | HC[LGP] |
| LG0 | G0, Nbar, vl (+ G0·h) | 4, 5 | gw·mN/(2·mW), gw²·mN/(4·mW²) | 0, -1 | absorbed in mN | 0 | 0 | from SU(2) singlet Weinberg op | singlet | n/a | 0 | no | LaTeX Eq.(372-373): fractions exact | HC[LG0] |
| LGPGP | GP², bar[CC[l1]], l2 | 5 | gw²·mN/(4·mW²) | -1 | absorbed in mN | 0 | 0 | from SU(2) singlet Weinberg op | singlet | n/a | 0 | yes (bar[CC[l]]) | LaTeX Eq.(374): fraction exact | HC[LGPGP] |
| LG0G0 | G0², Nbar, vl | 5 | gw²·mN/(8·mW²) | -1 | absorbed in mN | 0 | 0 | from SU(2) singlet Weinberg op | singlet | n/a | 0 | no | LaTeX Eq.(374): fraction exact | HC[LG0G0] |
| LG0GP | G0, GP, Nbar, l, bar[CC[l]], N | 5 | gw²·mN/(4√2·mW²) | -1 | absorbed in mN | 0 | 0 | from SU(2) singlet Weinberg op | singlet | n/a | 0 | yes (bar[CC[l]]) | LaTeX Eq.(375): fraction exact | HC[LG0GP] |

**Additional audit lines:**
- Kinetic+mass term for new class N: LNkin exists and is in LTotal.
- Non-fundamental colour representations: none (N is colour singlet).
- SelfConjugate→True classes with no QuantumNumbers: N (confirmed: no QuantumNumbers entry).
- Name conflict check: Class N (F[100]); Parameters Lambda, Cll_ee, Cll_emu, Cll_etau, Cll_mumu, Cll_mutau, Cll_tautau, mN, wN; Indices: none new. None conflict with Mathematica built-ins, FeynRules symbols, or SM.fr names.
- LTotal = LNkin + Lint + HC[Lint], where Lint = LW + LZ + Lh + LGP + LG0 + LGPGP + LG0G0 + LG0GP. Single total Lagrangian defined.
- Reference/cached model file read: none (only paper/2012.09882_source.tex and SM.fr read as instructed).

model.fr is written.