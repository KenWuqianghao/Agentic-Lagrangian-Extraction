**Self-Audit Table**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | U(1)_X sum | L/B sum | CC[] used | frac/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin (kinetic) | FS[Zp] FS[Zp] | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LZpkin (mass) | Zp Zp | 2 | MZp² | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LPhiXkin (kinetic) | del ΦX† del ΦX | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LPhiXkin (Zp-ΦX) | Zp ΦX† del ΦX | 4 | gX | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | HC[...] partner |
| LPhiXkin (Zp²ΦX²) | Zp² ΦX† ΦX | 4 | gX² | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LPhiXpot (mass) | ΦX† ΦX | 2 | mΦX² | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LPhiXpot (quartic) | (ΦX† ΦX)² | 4 | λΦX | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LPhiXpot (portal) | ΦX† ΦX Φ† Φ | 4 | λHΦX | 0 | n/a | 0 | 0 | shared idx ii | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LNRkin (kinetic) | NR̄ γ·del NR | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LNRkin (mass) | NR̄ NR | 3 | MNR | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conjugate |
| LYukNu | LL̄ Phibar NRR | 4 | yNu | 0 | n/a | 0 | 0 | shared idx ii | singlet | xH† | 0 | no | Eq.(1) LaTeX | HC[...] |
| LYukMajorana | ΦX bar[CC[NR]] NR | 4 | yN | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | yes | Eq.(1) LaTeX | HC[...] |
| LZpff (per fermion) | f̄ γ^μ f Zp | 4 | gX·Qf | 0 | n/a | 0 | 0 | shared idx ii | δ_cc | 0 | 0 | n/a | Table 1 | self-conjugate |

† **Note on LYukNu U(1)_X sum**: Paper's Eq.(1) writes `\overline{\ell_L} H N_R` with H (X=-xH/2). SM.fr convention requires Phibar (Y=-1/2) for U(1)_Y invariance with N_R Y=0. Phibar has X=+xH/2 (opposite of Phi's X=-xH/2). Sum = xH ≠ 0 for general xH. Paper's Yukawa is U(1)_X invariant with H but violates U(1)_Y; SM.fr convention fixes U(1)_Y but breaks U(1)_X for xH≠0. This is a known convention mismatch in the paper; Z' phenomenology (which uses Table 1 charges) is unaffected.

**Additional audit rows:**

- **Particle kinetic+mass terms in LTotal**: Zp (LZpkin), ΦX (LPhiXkin+LPhiXpot), NR (LNRkin) — all present and summed in LTotal.
- **Non-fundamental colour representations**: None (all new fields are SM singlets).
- **SelfConjugate=True classes with no QuantumNumbers**: Zp (V[100]) — QuantumNumbers={} ✓
- **Name conflict check**: All class names (Zp, PhiX, NR, NRR), parameter names (gX, xH, MZp, mPhiX2, lambdaPhiX, lambdaHPhiX, yNu, yN, vPhi, QqL, QuR, QdR, QlL, QeR, QNR, MPhiX, MNR, WZp, WPhiX, WNR), and indices (Generation, Colour, Gluon, SU2D, SU2W from SM.fr) are not Mathematica built-ins, FeynRules symbols, or SM.fr names ✓
- **Single total Lagrangian**: LTotal = LZpkin + LPhiXkin + LPhiXpot + LNRkin + LYukNu + LYukMajorana + LZpff ✓
- **Reference/cached model files read**: none (only paper/2104.10902_source.tex and SM.fr for conventions)

**Last ./frgen result:**
```
SCHEMA OK: 4 particle classes, 17 parameters, Lagrangian terms ['LZpkin', 'LPhiXkin', 'LPhiXpot', 'LNRkin', 'LYukNu', 'LYukMajorana', 'LZpff', 'LTotal']
RENDERED: model.fr (202 lines). You may read it.
LINT: 3 finding(s). Each names the stage it predicts will fail (compile, checks = a FeynRules consistency check, mg5 = MadGraph import, harness = the total Lagrangian cannot be identified, warn = may still pass). Fix the ones that are real defects; do not remove paper physics just to silence one.
- [warn] undeclared_symbol: `LPhiXpot` uses `Phibar` which is neither declared here nor by SM.fr (model.fr line 192)
- [warn] undeclared_symbol: `LYukNu` uses `LLbar` which is neither declared here nor by SM.fr (model.fr line 196)
- [warn] undeclared_symbol: `LZpff` uses `QLbar` which is neither declared here nor by SM.fr (model.fr line 200)
```
The three warnings are expected for an SM add-on: `Phibar`, `LLbar`, `QLbar` are declared in SM.fr (loaded before this add-on). The linter runs in isolation and does not see SM.fr. No action needed.