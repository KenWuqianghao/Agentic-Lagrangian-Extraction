Last `./frgen spec.json` result: **SCHEMA OK** (5 particle classes, 10 parameters, 9 terms); RENDERED model.fr (156 lines); LINT: 3 findings, all `[warn] undeclared_symbol` on `LLbar`/`Phibar` — checked and harmless (FeynRules auto-conjugates of SM.fr `LL`/`Phi`; the linter’s external SM.fr path does not exist in this sandbox, so `SM_CLASSES`/`SM_FIELDS_ALL` are empty and these false positives fire; stage is `warn` = may still pass).

**B-L sign choice:** the paper’s \(Y_{B-L}\) (quarks \(+1/3\), leptons \(-1\), \(\chi\) \(+2\), \(H\)/\(Z'\) \(0\)). Chosen because it is what the paper’s charge table and \(D_\mu\) use, and both Yukawas are then invariant under SM.fr hypercharge conventions (\(L̄\nu_R\tilde H\): \(+1-1+0=0\); \(\bar\nu^c\nu_R\chi\): \(-1-1++2=0\)). Charge lives on Unphysical chiral classes (`Nrg` BL=−1, `Chi` BL=+2), never on `SelfConjugate -> True` classes.

## Mandatory self-audit table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4−d) | 1/Lambda power (must be d−4, or n/a if d≤4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | B−L sum (must be 0) | lepton/baryon sum | CC[] where paper writes ψ^c | fraction/root placement checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin | Zp | 4 | n/a (free) | n/a | n/a | 0 | 0 | singlet | singlet | 0 | 0/0 | n/a | −1/4, 1/2 from paper Eq. (LYM), LaTeX line 112 | self-conjugate (real vector) |
| LHsKin | Hs | 4 | n/a (free) | n/a | n/a | 0 | 0 | singlet | singlet | 0 | 0/0 | n/a | 1/2 canonical real-scalar form, rule 1; mass from paper scalar mass matrix | self-conjugate (real scalar) |
| LNrKin | NR̄, NR | 4 | n/a (free) | n/a | n/a | 0 | 0 | singlet | singlet | 0 | 0/0 (Majorana) | n/a | 1/2 Majorana normalization, rule 1; paper L_f | self-conjugate (Majorana) |
| LZpGauge | uq̄uq, dq̄dq, LL̄LL, lR̄lR, NR̄NR, Zp | 4 | gp | 0 | n/a | 0 | 0 | singlet (LL̄LL shared index; others component singlets) | singlet (uq̄uq, dq̄dq shared Colour; others singlet) | 0 (quarks −1/3+1/3, LL +1−1, lR +1−1, NR bilinear 0, Zp 0) | 0/0 (each bilinear) | n/a | −1/3 from paper charge table (quarks B−L=+1/3); sign from iψ̄γDψ convention; paper Sec. 2 / Eq. (DM) | self-conjugate (vector current, real g′) |
| LYnu | LL̄, Nrg, Phibar, Eps | 4 | yv | 0 | n/a | 0 | 0 (+1/2 + 0 −1/2) | Eps[ii,jj] on distinct indices (both bar-type → H̃) | singlet | 0 (LL̄ +1, Nrg −1, Phibar 0) | 0/0 (LL̄ −1+1) | n/a (paper: no ψ^c in Dirac term) | y^ν_ii = √2 M_Ni V_iN / v vs LaTeX line 177; cross-check m_D = y^ν v/√2 line 134 | yuk + HC[yuk] explicit |
| LYnuM | bar[CC[Nrg]], Nrg, Chi | 4 | yM | 0 | n/a | 0 | 0 | singlet | singlet | 0 (−1 −1 +2) | 0/0 | **yes** (paper \(\overline{\nu^c_{Ri}}\) → bar[CC[Nrg]]) | y^M = M_R/(√2 x) from M_R = √2 y^M x, LaTeX line 134 | Majorana bilinear; paper’s +h.c. absorbed via Majorana condition (no explicit HC) |
| LHportal | Phibar, Phi, bar[Chi], Chi | 4 | lam3 | 0 | n/a | 0 | 0 (−1/2+1/2+0+0) | Phibar[ii]Phi[ii] shared index | singlet | 0 (Phibar 0, Phi 0, bar[Chi] −2, Chi +2) | 0/0 | n/a | lam3 = Sin[2α](MHs²−MH²)/(2 v x) vs paper `para_quartic`, LaTeX lines 244–245; cross-check tan(2α) line 217 | self-conjugate (real λ3, conjugate pairs) |
| Llam2 | bar[Chi], Chi (×2) | 4 | lam2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 (each bar[Chi]Chi pair −2+2) | 0/0 | n/a | lam2 = [(MH²+MHs²)+Cos[2α](MHs²−MH²)]/(4x²) vs `para_quartic`, LaTeX lines 241–242 | self-conjugate (real λ2, conjugate pairs) |
| LTotal | sum of all above | 4 | n/a (sum) | n/a | n/a | 0 | 0 | — | — | 0 | 0/0 | — | — | — |

No term has d > 4: the model is renormalizable (paper is a gauge theory, no \(1/\Lambda^n\) EFT operators), so rule 2 is n/a.

### New particle class rows (kinetic + mass present, in LTotal)

| particle class | class_index | kinetic + mass term | in LTotal? | notes |
|---|---|---|---|---|
| Zp (V) | 100 | LZpKin = −1/4 FS² + 1/2 MZp² Zp² | yes | real vector, SelfConjugate, MZp=1000. |
| Hs / h2 (S) | 101 | LHsKin = 1/2 del² − 1/2 MHs² Hs² | yes | real scalar, SelfConjugate, MHs=200. |
| NR / N1–N3 (F) | 102 | LNrKin = I/2 NR̄ Ga del − 1/2 MN NR̄ NR | yes | Majorana, SelfConjugate, MN=MZp/5 Internal |
| Chi (S, Unphysical) | 103 | free-field n/a — Definitions → −Sin[α] H + Cos[α] Hs; H kinetic in SM.fr, Hs in LHsKin | yes (via H/Hs) | BL=+2 on Unphysical chiral class |
| Nrg (F, Unphysical) | 104 | free-field n/a — Definitions → snv vl + cnv NR; vl kinetic in SM.fr, NR in LNrKin | yes (via vl/NR) | BL=−1 on Unphysical chiral class |

### Non-fundamental colour representation rows

None. No sextet/octet colour representation exists in this model; `index_decls` is empty and no `AddGaugeRepresentation[...]` line is required.

---

**SelfConjugate → True classes:** `Zp`, `Hs`, `NR` — none carries `QuantumNumbers` (all three have `quantum_numbers: {}`).

**Names:** classes `Zp`, `Hs`, `NR`, `Chi`, `Nrg`; members `N1`, `N2`, `N3`; parameters `gp`, `alpha`, `MN`, `xbl`, `snv`, `cnv`, `yv`, `yM`, `lam3`, `lam2`; new indices: none (only SM `Generation` used). None is a Mathematica built-in, a FeynRules symbol (`HC`/`CC`/`FS`/`DC`/`del`/`Eps`/`Ga`/`ProjP`/`ProjM`/`N`/…), or an SM.fr-declared name (`H`/`Phi`/`Z`/`W`/`A`/`G`/`vev`/`MZ`/…); `vev`, `H`, `Phi`, `vl` are referenced from SM.fr, not redeclared. Particle names use no primes/punctuation (`Zp`, `h2`, `N1`–`N3`). Class indices ≥ 100.

**Single total Lagrangian:** `LTotal := LZpKin + LHsKin + LNrKin + LZpGauge + LYnu + LYnuM + LHportal + Llam2` — sums every other term, no second total, no constant-only terms.

**Reference or cached model file read:** none.

**Last ./frgen result:** SCHEMA OK (5 particle classes, 10 parameters, 9 terms including LTotal); RENDERED model.fr (156 lines); LINT 3 findings, all `[warn] undeclared_symbol` on `LLbar`/`Phibar` — checked and judged harmless (SM.fr auto-conjugates; linter cannot see the external SM.fr path in this sandbox).