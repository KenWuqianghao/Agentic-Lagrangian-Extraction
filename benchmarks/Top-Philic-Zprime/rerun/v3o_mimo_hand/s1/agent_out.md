## Self-audit table (final)

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present (must be d-4 or n/a) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | lepton/baryon number sum | CC[] used where paper writes psi^c | fraction/root placement checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV1kin | V1, V1 (FS×FS and MV1² V1 V1) | 4 | canonical + MV1 (in MV1² V1 V1) | 0; MV1 dim 1 (MV1² has dim 2 = 4−2 for V1V1) | n/a (d=4) | 0 | 0 | singlet | singlet (no colour index) | n/a | n/a | n/a (real field) | n/a | self-conjugate (real Proca term) |
| LV1int | tbar, t, V1 | 3/2+3/2+1 = 4 | ct (Cos[thV1], Sin[thV1] dimensionless) | 0 = 4−4 | n/a (d=4) | −2/3+2/3+0 = 0 | −2/3+2/3+0 = 0 | all singlets → singlet | tbar·t: 3×3̄→1 via Dot; V1 singlet | n/a (no new U(1) in paper) | B: −1/3+1/3+0 = 0 | n/a (paper writes no ψ^c) | Eq.(v0inttop) LaTeX lines 175–179: only c_t, cos, sin — exact Cos/Sin, no fraction/root | self-conjugate: (tbar γ_μ P_{L,R} t)† equals itself, V1 real → term = own h.c.; written once, no HC[] |

- Kinetic+mass term exists for **V1** (`LV1kin`) and is in `LTotal` — confirmed.
- Non-fundamental colour representations: **none** (V1 is a colour singlet); no `AddGaugeRepresentation[...]` line required — confirmed.
- **SelfConjugate -> True classes: V1 only; carries no QuantumNumbers** — confirmed.
- Names chosen: class `V1`; parameters `ct`, `thV1`, `MV1`; terms `LV1kin`, `LV1int`, `LTotal`; block `TPZPINPUTS`. None is a Mathematica built-in, a FeynRules symbol (HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM, N, C, D, E, I, K, O), or an SM.fr name (H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, MZ, MW, g1, …) — confirmed.
- Single total: **LTotal = LV1kin + LV1int**; these are all defined terms — confirmed.
- Reference or cached model file read: **none**.

model.fr is written.