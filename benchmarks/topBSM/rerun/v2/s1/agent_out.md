I'll start by reading the paper and the schema files.
## Extraction summary

The paper is a pure **effective-field-theory** (EFT) add-on to the SM. It adds **no new particles**: the whole new-physics content is a set of dimension-six operators (Eqs. 2–5) with Wilson coefficients `C_i/Λ²` (Eq. 1). The two Lorentz structures are the dimension-six Yukawa operator `O_uφ` and the flavour-changing chromomagnetic operator `O_uG`, each in the flavour structures (1,3), (3,1) and — by the paper's own statement — (2,3), (3,2). The operators `O^(1)`, `O^(2)` of Eqs. (33)–(34) vanish by the equations of motion, so I do not implement them.

I implement `O_uφ` in the Eq. (12) form, `-y_t³(φ†φ − v²/2)(q̄t)φ̃`, because the paper states this form removes the u–t mass mixing while giving the same physics (Eq. 11).

## Mandatory self-audit table

New U(1) groups: none. Lepton/baryon number: not assigned by the paper; every term is B- and L-conserving (one quark in, one quark out).

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (must be 4−d) | 1/Λ power (must be d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sums | L/B sum | CC[] where paper writes ψ^c | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LOuphiqt (1,3) | `QLbar[sp,ii,1,cc] uR[sp,3,cc] Phibar[kk] Phi[kk] Phibar[jj]` | 6 | `Cuphi13 ytop^3/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | −1/6+2/3−1/2+1/2−1/2 = 0 | singlet: `Eps[ii,jj]` on `QLbar[ii]`–`Phibar[jj]`; `Phibar[kk] Phi[kk]` shared index | `QLbar[cc]`–`uR[cc]` shared Colour | n/a (no new U(1)) | B: −1/3+1/3 = 0 | n/a | `HC[op]` |
| LOuphiqt (2,3) | `QLbar[sp,ii,2,cc] uR[sp,3,cc] Phibar[kk] Phi[kk] Phibar[jj]` | 6 | `Cuphi23 ytop^3/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | same as above | shared Colour | n/a | 0 | n/a | `HC[op]` |
| LOuphiQu (3,1) | `QLbar[sp,ii,3,cc] uR[sp,1,cc] Phibar[kk] Phi[kk] Phibar[jj]` | 6 | `Cuphi31 ytop^3/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | same as above | shared Colour | n/a | 0 | n/a | `HC[op]` |
| LOuphiQu (3,2) | `QLbar[sp,ii,3,cc] uR[sp,2,cc] Phibar[kk] Phi[kk] Phibar[jj]` | 6 | `Cuphi32 ytop^3/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | same as above | shared Colour | n/a | 0 | n/a | `HC[op]` |
| LOuGqt (1,3) | `QLbar[sp1,ii,1,cc1] Ga[mu] Ga[nu] uR[sp3,3,cc2] T[aa,cc1,cc2] Phibar[jj] FS[G,mu,nu,aa]` | 6 | `CuG13 ytop gs/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | −1/6+2/3−1/2 = 0 | singlet: `Eps[ii,jj]` on `QLbar[ii]`–`Phibar[jj]` | `T[aa,cc1,cc2]` with `QLbar[cc1]`, `uR[cc2]`, `FS[G,...,aa]` | n/a | 0 | n/a | `HC[op]` |
| LOuGqt (2,3) | same with generation 2 doublet | 6 | `CuG23 ytop gs/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | `Eps[ii,jj]` | `T[aa,cc1,cc2]` | n/a | 0 | n/a | `HC[op]` |
| LOuGQu (3,1) | `QLbar[sp1,ii,3,cc1] Ga[mu] Ga[nu] uR[sp3,1,cc2] T[aa,cc1,cc2] Phibar[jj] FS[G,mu,nu,aa]` | 6 | `CuG31 ytop gs/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | `Eps[ii,jj]` | `T[aa,cc1,cc2]` | n/a | 0 | n/a | `HC[op]` |
| LOuGQu (3,2) | same with `uR[sp3,2,cc2]` | 6 | `CuG32 ytop gs/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | `Eps[ii,jj]` | `T[aa,cc1,cc2]` | n/a | 0 | n/a | `HC[op]` |
| LtopBSM (total) | `LOuphiqt + LOuphiQu + LOuGqt + LOuGQu` | — | — | — | — | 0 | 0 | — | — | n/a | 0 | n/a | each part is `op + HC[op]` |

Notes on the table:
- The `−vev^2/2` piece of Eq. (12) is a subtraction, not an extra operator. It removes the constant part of `φ†φ`, so no u–t mass mixing term is generated. Every remaining monomial holds at least one physical or Goldstone scalar.
- The cutoff `Lam` is an explicit External parameter in GeV with the paper benchmark 1000. GeV (Λ = 1 TeV). All `C_i` stay dimensionless with default 1., the value the paper uses in Fig. 4.
- `σ^{μν} G_{μν} = I γ^μ γ^ν G_{μν}` because `FS[G,mu,nu,aa]` is antisymmetric. This is why the term shows `I Ga[mu].Ga[nu]`.
- New particle classes: **none**. The paper adds no field beyond the SM, so there is no kinetic or mass term to add.
- `SelfConjugate -> True` classes in this model: none. Therefore no such class carries `QuantumNumbers`.
- Reference or cached model file read: **none**. Only the paper text, `frmodel.py`, `render.py` and `SM.fr` were read.

```json
{
  "model_name": "topBSM_gen",
  "info": {
    "authors": ["Cen Zhang", "Fabio Maltoni"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["Centre for Cosmology, Particle Physics and Phenomenology, Universite catholique de Louvain"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "particles": [],
  "vevs": [],
  "gauge_xi": [],
  "parameters": [
    {
      "name": "Lam",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda",
      "description": "EFT cutoff [GeV], Eq.(1); benchmark Lambda = 1 TeV"
    },
    {
      "name": "ytop",
      "parameter_type": "Internal",
      "value": "Sqrt[2]*MT/vev",
      "interaction_order": ["QED", 1],
      "tex": "y_t",
      "description": "Top Yukawa coupling defined with the on-shell top mass, yt = Sqrt[2] mt / v, Eq.(7)"
    },
    {
      "name": "Cuphi13",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "C_{u\\varphi}^{(1,3)}",
      "description": "Dimensionless Wilson coefficient of O_uphi^(1,3) = -yt^3 (phi+ phi)(qbar t) phitilde with q the first-generation left-handed doublet, Eq.(3)"
    },
    {
      "name": "Cuphi23",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "tex": "C_{u\\varphi}^{(2,3)}",
      "description": "Dimensionless Wilson coefficient of O_uphi^(2,3), the charm copy of Eq.(3)"
    },
    {
      "name": "Cuphi31",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "tex": "C_{u\\varphi}^{(3,1)}",
      "description": "Dimensionless Wilson coefficient of O_uphi^(3,1) = -yt^3 (phi+ phi)(Qbar u) phitilde, Eq.(5)"
    },
    {
      "name": "Cuphi32",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 4,
      "interaction_order": ["NP", 1],
      "tex": "C_{u\\varphi}^{(3,2)}",
      "description": "Dimensionless Wilson coefficient of O_uphi^(3,2), the charm copy of Eq.(5)"
    },
    {
      "name": "CuG13",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "tex": "C_{uG}^{(1,3)}",
      "description": "Dimensionless Wilson coefficient of the chromomagnetic operator O_uG^(1,3) = yt gs (qbar sigma^{mu nu} T^A t) phitilde G^A_{mu nu}, Eq.(2)"
    },
    {
      "name": "CuG23",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 6,
      "interaction_order": ["NP", 1],
      "tex": "C_{uG}^{(2,3)}",
      "description": "Dimensionless Wilson coefficient of O_uG^(2,3), the charm copy of Eq.(2)"
    },
    {
      "name": "CuG31",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 7,
      "interaction_order": ["NP", 1],
      "tex": "C_{uG}^{(3,1)}",
      "description": "Dimensionless Wilson coefficient of O_uG^(3,1) = yt gs (Qbar sigma^{mu nu} T^A u) phitilde G^A_{mu nu}, Eq.(4)"
    },
    {
      "name": "CuG32",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 8,
      "interaction_order": ["NP", 1],
      "tex": "C_{uG}^{(3,2)}",
      "description": "Dimensionless Wilson coefficient of O_uG^(3,2), the charm copy of Eq.(4)"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LOuphiqt",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, kk, cc, op}, op = ExpandIndices[-ytop^3/Lam^2 (Phibar[kk] Phi[kk] - vev^2/2) (Cuphi13 QLbar[sp, ii, 1, cc].uR[sp, 3, cc] + Cuphi23 QLbar[sp, ii, 2, cc].uR[sp, 3, cc]) Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; op + HC[op]]"
    },
    {
      "name": "LOuphiQu",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, kk, cc, op}, op = ExpandIndices[-ytop^3/Lam^2 (Phibar[kk] Phi[kk] - vev^2/2) (Cuphi31 QLbar[sp, ii, 3, cc].uR[sp, 1, cc] + Cuphi32 QLbar[sp, ii, 3, cc].uR[sp, 2, cc]) Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; op + HC[op]]"
    },
    {
      "name": "LOuGqt",
      "delayed": true,
      "expression": "Block[{sp1, sp2, sp3, mu, nu, aa, ii, jj, cc1, cc2, op}, op = ExpandIndices[I ytop gs/Lam^2 (CuG13 QLbar[sp1, ii, 1, cc1].Ga[mu, sp1, sp2].Ga[nu, sp2, sp3].uR[sp3, 3, cc2] + CuG23 QLbar[sp1, ii, 2, cc1].Ga[mu, sp1, sp2].Ga[nu, sp2, sp3].uR[sp3, 3, cc2]) T[aa, cc1, cc2] Phibar[jj] Eps[ii, jj] FS[G, mu, nu, aa], FlavorExpand -> SU2D]; op + HC[op]]"
    },
    {
      "name": "LOuGQu",
      "delayed": true,
      "expression": "Block[{sp1, sp2, sp3, mu, nu, aa, ii, jj, cc1, cc2, op}, op = ExpandIndices[I ytop gs/Lam^2 (CuG31 QLbar[sp1, ii, 3, cc1].Ga[mu, sp1, sp2].Ga[nu, sp2, sp3].uR[sp3, 1, cc2] + CuG32 QLbar[sp1, ii, 3, cc1].Ga[mu, sp1, sp2].Ga[nu, sp2, sp3].uR[sp3, 2, cc2]) T[aa, cc1, cc2] Phibar[jj] Eps[ii, jj] FS[G, mu, nu, aa], FlavorExpand -> SU2D]; op + HC[op]]"
    },
    {
      "name": "LtopBSM",
      "delayed": true,
      "expression": "LOuphiqt + LOuphiQu + LOuGqt + LOuGQu"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LtopBSM"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
## Extraction summary

The paper is a pure **effective-field-theory** (EFT) add-on to the SM. It adds **no new particles**: the whole new-physics content is a set of dimension-six operators (Eqs. 2–5) with Wilson coefficients `C_i/Λ²` (Eq. 1). The two Lorentz structures are the dimension-six Yukawa operator `O_uφ` and the flavour-changing chromomagnetic operator `O_uG`, each in the flavour structures (1,3), (3,1) and — by the paper's own statement — (2,3), (3,2). The operators `O^(1)`, `O^(2)` of Eqs. (33)–(34) vanish by the equations of motion, so I do not implement them.

I implement `O_uφ` in the Eq. (12) form, `-y_t³(φ†φ − v²/2)(q̄t)φ̃`, because the paper states this form removes the u–t mass mixing while giving the same physics (Eq. 11).

## Mandatory self-audit table

New U(1) groups: none. Lepton/baryon number: not assigned by the paper; every term is B- and L-conserving (one quark in, one quark out).

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (must be 4−d) | 1/Λ power (must be d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sums | L/B sum | CC[] where paper writes ψ^c | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LOuphiqt (1,3) | `QLbar[sp,ii,1,cc] uR[sp,3,cc] Phibar[kk] Phi[kk] Phibar[jj]` | 6 | `Cuphi13 ytop^3/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | −1/6+2/3−1/2+1/2−1/2 = 0 | singlet: `Eps[ii,jj]` on `QLbar[ii]`–`Phibar[jj]`; `Phibar[kk] Phi[kk]` shared index | `QLbar[cc]`–`uR[cc]` shared Colour | n/a (no new U(1)) | B: −1/3+1/3 = 0 | n/a | `HC[op]` |
| LOuphiqt (2,3) | `QLbar[sp,ii,2,cc] uR[sp,3,cc] Phibar[kk] Phi[kk] Phibar[jj]` | 6 | `Cuphi23 ytop^3/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | same as above | shared Colour | n/a | 0 | n/a | `HC[op]` |
| LOuphiQu (3,1) | `QLbar[sp,ii,3,cc] uR[sp,1,cc] Phibar[kk] Phi[kk] Phibar[jj]` | 6 | `Cuphi31 ytop^3/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | same as above | shared Colour | n/a | 0 | n/a | `HC[op]` |
| LOuphiQu (3,2) | `QLbar[sp,ii,3,cc] uR[sp,2,cc] Phibar[kk] Phi[kk] Phibar[jj]` | 6 | `Cuphi32 ytop^3/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | same as above | shared Colour | n/a | 0 | n/a | `HC[op]` |
| LOuGqt (1,3) | `QLbar[sp1,ii,1,cc1] Ga[mu] Ga[nu] uR[sp3,3,cc2] T[aa,cc1,cc2] Phibar[jj] FS[G,mu,nu,aa]` | 6 | `CuG13 ytop gs/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | −1/6+2/3−1/2 = 0 | singlet: `Eps[ii,jj]` on `QLbar[ii]`–`Phibar[jj]` | `T[aa,cc1,cc2]` with `QLbar[cc1]`, `uR[cc2]`, `FS[G,...,aa]` | n/a | 0 | n/a | `HC[op]` |
| LOuGqt (2,3) | same with generation 2 doublet | 6 | `CuG23 ytop gs/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | `Eps[ii,jj]` | `T[aa,cc1,cc2]` | n/a | 0 | n/a | `HC[op]` |
| LOuGQu (3,1) | `QLbar[sp1,ii,3,cc1] Ga[mu] Ga[nu] uR[sp3,1,cc2] T[aa,cc1,cc2] Phibar[jj] FS[G,mu,nu,aa]` | 6 | `CuG31 ytop gs/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | `Eps[ii,jj]` | `T[aa,cc1,cc2]` | n/a | 0 | n/a | `HC[op]` |
| LOuGQu (3,2) | same with `uR[sp3,2,cc2]` | 6 | `CuG32 ytop gs/Lam^2` | −2 | `1/Lam^2` (=2) | 0 | 0 | `Eps[ii,jj]` | `T[aa,cc1,cc2]` | n/a | 0 | n/a | `HC[op]` |
| LtopBSM (total) | `LOuphiqt + LOuphiQu + LOuGqt + LOuGQu` | — | — | — | — | 0 | 0 | — | — | n/a | 0 | n/a | each part is `op + HC[op]` |

Notes on the table:
- The `−vev^2/2` piece of Eq. (12) is a subtraction, not an extra operator. It removes the constant part of `φ†φ`, so no u–t mass mixing term is generated. Every remaining monomial holds at least one physical or Goldstone scalar.
- The cutoff `Lam` is an explicit External parameter in GeV with the paper benchmark 1000. GeV (Λ = 1 TeV). All `C_i` stay dimensionless with default 1., the value the paper uses in Fig. 4.
- `σ^{μν} G_{μν} = I γ^μ γ^ν G_{μν}` because `FS[G,mu,nu,aa]` is antisymmetric. This is why the term shows `I Ga[mu].Ga[nu]`.
- New particle classes: **none**. The paper adds no field beyond the SM, so there is no kinetic or mass term to add.
- `SelfConjugate -> True` classes in this model: none. Therefore no such class carries `QuantumNumbers`.
- Reference or cached model file read: **none**. Only the paper text, `frmodel.py`, `render.py` and `SM.fr` were read.

```json
{
  "model_name": "topBSM_gen",
  "info": {
    "authors": ["Cen Zhang", "Fabio Maltoni"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["Centre for Cosmology, Particle Physics and Phenomenology, Universite catholique de Louvain"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "particles": [],
  "vevs": [],
  "gauge_xi": [],
  "parameters": [
    {
      "name": "Lam",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "tex": "\\Lambda",
      "description": "EFT cutoff [GeV], Eq.(1); benchmark Lambda = 1 TeV"
    },
    {
      "name": "ytop",
      "parameter_type": "Internal",
      "value": "Sqrt[2]*MT/vev",
      "interaction_order": ["QED", 1],
      "tex": "y_t",
      "description": "Top Yukawa coupling defined with the on-shell top mass, yt = Sqrt[2] mt / v, Eq.(7)"
    },
    {
      "name": "Cuphi13",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "C_{u\\varphi}^{(1,3)}",
      "description": "Dimensionless Wilson coefficient of O_uphi^(1,3) = -yt^3 (phi+ phi)(qbar t) phitilde with q the first-generation left-handed doublet, Eq.(3)"
    },
    {
      "name": "Cuphi23",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "tex": "C_{u\\varphi}^{(2,3)}",
      "description": "Dimensionless Wilson coefficient of O_uphi^(2,3), the charm copy of Eq.(3)"
    },
    {
      "name": "Cuphi31",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "tex": "C_{u\\varphi}^{(3,1)}",
      "description": "Dimensionless Wilson coefficient of O_uphi^(3,1) = -yt^3 (phi+ phi)(Qbar u) phitilde, Eq.(5)"
    },
    {
      "name": "Cuphi32",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 4,
      "interaction_order": ["NP", 1],
      "tex": "C_{u\\varphi}^{(3,2)}",
      "description": "Dimensionless Wilson coefficient of O_uphi^(3,2), the charm copy of Eq.(5)"
    },
    {
      "name": "CuG13",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "tex": "C_{uG}^{(1,3)}",
      "description": "Dimensionless Wilson coefficient of the chromomagnetic operator O_uG^(1,3) = yt gs (qbar sigma^{mu nu} T^A t) phitilde G^A_{mu nu}, Eq.(2)"
    },
    {
      "name": "CuG23",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 6,
      "interaction_order": ["NP", 1],
      "tex": "C_{uG}^{(2,3)}",
      "description": "Dimensionless Wilson coefficient of O_uG^(2,3), the charm copy of Eq.(2)"
    },
    {
      "name": "CuG31",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 7,
      "interaction_order": ["NP", 1],
      "tex": "C_{uG}^{(3,1)}",
      "description": "Dimensionless Wilson coefficient of O_uG^(3,1) = yt gs (Qbar sigma^{mu nu} T^A u) phitilde G^A_{mu nu}, Eq.(4)"
    },
    {
      "name": "CuG32",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "TOPFCNC",
      "order_block": 8,
      "interaction_order": ["NP", 1],
      "tex": "C_{uG}^{(3,2)}",
      "description": "Dimensionless Wilson coefficient of O_uG^(3,2), the charm copy of Eq.(4)"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LOuphiqt",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, kk, cc, op}, op = ExpandIndices[-ytop^3/Lam^2 (Phibar[kk] Phi[kk] - vev^2/2) (Cuphi13 QLbar[sp, ii, 1, cc].uR[sp, 3, cc] + Cuphi23 QLbar[sp, ii, 2, cc].uR[sp, 3, cc]) Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; op + HC[op]]"
    },
    {
      "name": "LOuphiQu",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, kk, cc, op}, op = ExpandIndices[-ytop^3/Lam^2 (Phibar[kk] Phi[kk] - vev^2/2) (Cuphi31 QLbar[sp, ii, 3, cc].uR[sp, 1, cc] + Cuphi32 QLbar[sp, ii, 3, cc].uR[sp, 2, cc]) Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; op + HC[op]]"
    },
    {
      "name": "LOuGqt",
      "delayed": true,
      "expression": "Block[{sp1, sp2, sp3, mu, nu, aa, ii, jj, cc1, cc2, op}, op = ExpandIndices[I ytop gs/Lam^2 (CuG13 QLbar[sp1, ii, 1, cc1].Ga[mu, sp1, sp2].Ga[nu, sp2, sp3].uR[sp3, 3, cc2] + CuG23 QLbar[sp1, ii, 2, cc1].Ga[mu, sp1, sp2].Ga[nu, sp2, sp3].uR[sp3, 3, cc2]) T[aa, cc1, cc2] Phibar[jj] Eps[ii, jj] FS[G, mu, nu, aa], FlavorExpand -> SU2D]; op + HC[op]]"
    },
    {
      "name": "LOuGQu",
      "delayed": true,
      "expression": "Block[{sp1, sp2, sp3, mu, nu, aa, ii, jj, cc1, cc2, op}, op = ExpandIndices[I ytop gs/Lam^2 (CuG31 QLbar[sp1, ii, 3, cc1].Ga[mu, sp1, sp2].Ga[nu, sp2, sp3].uR[sp3, 1, cc2] + CuG32 QLbar[sp1, ii, 3, cc1].Ga[mu, sp1, sp2].Ga[nu, sp2, sp3].uR[sp3, 2, cc2]) T[aa, cc1, cc2] Phibar[jj] Eps[ii, jj] FS[G, mu, nu, aa], FlavorExpand -> SU2D]; op + HC[op]]"
    },
    {
      "name": "LtopBSM",
      "delayed": true,
      "expression": "LOuphiqt + LOuphiQu + LOuGqt + LOuGQu"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LtopBSM"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```