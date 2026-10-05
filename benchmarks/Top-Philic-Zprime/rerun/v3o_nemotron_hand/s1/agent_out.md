Now let me produce the mandatory self-audit table and confirm the model is written.

## Self-Audit Table

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L/B sum | CC[] used | fraction/root checked | Hermitian partner |
|-----------|------------------------|---------------------------|-----------------|-------------------------------|----------------|-------|-------|-------------------|-------------------|--------------|---------|-----------|----------------------|-------------------|
| LV1kin    | V1, V1                 | 4                         | (canonical kinetic, mass MV1) | 0 / 1 (mass)              | n/a (d=4)      | 0     | 0     | singlet (no index) | singlet (no index) | n/a          | 0/0     | n/a       | n/a                  | self-conjugate    |
| LV1int    | uqbar[3], uq[3], V1    | 4 (3/2+3/2+1)             | ct, Cos[θ], Sin[θ] | 0                           | n/a (d=4)      | 0     | 0     | effective (physical top field) | colour index cc contracted → singlet | n/a          | 0/0     | n/a       | θ=π/2 exact in paper (Sec. 2.2, footnote) | self-conjugate (real ct, θ; Hermitian current) |

**Additional audit rows:**

- **New particle class V1**: Kinetic+mass term LV1kin exists and is in LTotal. V1 is color singlet, SU(2) singlet, Q=0, Y=0, spin-1. `SelfConjugate -> True`, carries **no QuantumNumbers** (confirmed).
- **Non-fundamental colour representation**: None (V1 is color singlet; top uses SM Colour index).
- **Name conflicts check**: `V1`, `MV1`, `ct`, `theta`, `cL`, `cR`, `LV1kin`, `LV1int`, `LTotal` — none are Mathematica built-ins, FeynRules symbols (`N`, `C`, `D`, `E`, `I`, `K`, `O`, `HC`, `CC`, `FS`, `DC`, `del`, `Eps`, `Ga`, `ProjP`, `ProjM`), or SM.fr names (`H`, `Phi`, `Z`, `W`, `A`, `G`, `ee`, `gs`, `gw`, `sw`, `cw`, `vev`, `MZ`, `MW`, `uq`, `dq`, `LL`, `QL`, `uR`, `dR`, `lR`, `vl`).
- **Single total Lagrangian**: `LTotal = LV1kin + LV1int` (sums both terms).
- **Reference model read**: **none** (only paper/1604.07421_source.tex and SM.fr read).

`model.fr` is written.