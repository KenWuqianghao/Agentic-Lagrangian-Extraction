Now I'll produce the mandatory self-audit table and final message:

---

## Self-Audit Table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4-d) | 1/Lambda power present (d-4 or n/a) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) charges | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV1kin (kinetic) | FS[V1,μ,ν] FS[V1,μ,ν] | 4 | 1 (implicit) | 0 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a (no frac/root) | self-conjugate |
| LV1kin (mass) | V1[μ] V1[μ] | 4 | MV1² | 2 | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self-conjugate |
| LV1int (cL term) | uqbar[3,cc] uq[3,cc] V1[μ] | 4 | cL | 0 | n/a | 0 | 0 | singlet | δ_{cc} (color singlet) | n/a | 0 | n/a | n/a | self-conjugate |
| LV1int (cR term) | uqbar[3,cc] uq[3,cc] V1[μ] | 4 | cR | 0 | n/a | 0 | 0 | singlet | δ_{cc} (color singlet) | n/a | 0 | n/a | n/a | self-conjugate |

**Additional audit rows:**

- **Kinetic+mass term for new particle V1**: LV1kin exists and is included in LTotal ✓
- **Non-fundamental color representations**: none (V1 is color singlet) ✓
- **SelfConjugate=True classes with no QuantumNumbers**: V1 (SelfConjugate=True, QuantumNumbers={}) ✓
- **Name conflicts**: Class names (V1), parameter names (MV1, ct, theta, cL, cR, WV1), term names (LV1kin, LV1int, LTotal) — none are Mathematica built-ins, FeynRules symbols (N, C, D, E, I, K, O, HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM), or SM.fr names (H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, MZ, MW, etc.) ✓
- **Single total Lagrangian**: LTotal := LV1kin + LV1int (sums all terms) ✓
- **Reference/cached model file read**: none (only paper/1604.07421_source.tex and SM.fr were read) ✓

---

`./frgen spec.json` → **SCHEMA OK: 1 particle classes, 5 parameters, Lagrangian terms ['LV1kin', 'LV1int', 'LTotal']; RENDERED: model.fr (83 lines); LINT: no findings.**