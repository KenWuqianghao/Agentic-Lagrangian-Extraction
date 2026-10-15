I'll start by reading the paper and the schema.
I read the paper and the schema. I did not open any reference or cached `.fr` file for this model — none exists in the sandbox.

## What the paper defines as new physics

The paper (CMS, arXiv:1812.00380) interprets a 4µ search in two benchmark sectors:

- **Dark SUSY (the MSSMD sector).** A broken new U(1)_D gives a massive **dark photon γ_D** (0.25–8.5 GeV) that mixes kinetically with the SM photon through **ε**. The chain is `pp → h → 2 n1 → 2 γ_D + 2 n_D → 4µ + X`, with the **lightest non-dark neutralino n1** (10 GeV, Majorana) and the **dark neutralino n_D** (1 GeV, Majorana, stable/invisible). γ_D → µ⁺µ⁻ at 100%; τ_γD(ε, m_γD) = ε⁻² f(m_γD).
- **NMSSM.** Two CP-even neutral Higgs bosons **h1, h2** (90–150 GeV) decay `h1,2 → 2 a1`, and the CP-odd light boson **a1** (0.25–3.55 GeV) decays to µ⁺µ⁻. tan β = 20 is the paper's benchmark.

All six new states are electrically neutral colour and SU(2) singlets, so no new index is needed.

## Mandatory self-audit

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1)_D sum | L/B sum | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LgaDkin | FS[gaD]·FS[gaD] (2+2); MgaD²·gaD·gaD (1+1) | 4; 2 | 1/4; MgaD² | 0; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (real field) | 0 | n/a | self-conj ✓ |
| LgaDmix | FS[A]·FS[gaD] (2+2) | 4 | epsD | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (mixing operator, U(1)_D broken) | 0 | n/a | self-conj ✓ |
| LgaDff | gaD·f̄·f (1+3/2+3/2) | 4 | epsD·ee | 0 ✓ | n/a | 0 (Q_f − Q_f) | 0 (vector current) | singlet (physical eigenstates) | 3̄⊗3 → singlet | 0 | 0 | n/a | self-conj (real current) ✓ |
| Ln1kin | n1bar·Ga·del·n1 (3/2+1+3/2); Mn1·n1bar·n1 | 4; 3 | 1/2; Mn1 | 0; 1 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | Majorana class, bar = CC by construction | self-conj ✓ |
| LnDkin | nDbar·Ga·del·nD; MnD·nDbar·nD | 4; 3 | 1/2; MnD | 0; 1 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | Majorana class | self-conj ✓ |
| LnDn1 | gaD·nDbar·n1 (1+3/2+3/2) | 4 | gnD | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (off-diagonal transition current) | 0 | Majorana; no ψ^c in paper | HC[…] written ✓ |
| Lhn1 | H·n1bar·n1 (1+3/2+3/2) | 4 | ghn1 | 0 ✓ | n/a | 0 | 0 (post-EWSB eigenstate H) | singlet | singlet | 0 | 0 | Majorana | self-conj ✓ |
| La1kin | del·a1·del·a1; Ma1²·a1·a1 | 4; 2 | 1/2; Ma1² | 0; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lh1kin | del·h1·del·h1; Mh1²·h1·h1 | 4; 2 | 1/2; Mh1² | 0; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lh2kin | del·h2·del·h2; Mh2²·h2·h2 | 4; 2 | 1/2; Mh2² | 0; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lhaa | h1·a1·a1 (1+1+1) | 3 | lamh1aa·vev (and lamh2aa·vev) | 1 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| La1ff | a1·f̄·f (1+3/2+3/2) | 4 | tb·Ml[ff]/vev (and 1/(tb·vev)·Mu[ff]) | 0 ✓ | n/a | 0 | 0 (mass eigenstates) | singlet | 3̄⊗3 → singlet | 0 | 0 | n/a | −I·γ5 bilinear is hermitian ✓ |

Kinetic + mass term present and in the total sum: gaD (LgaDkin), n1 (Ln1kin), nD (LnDkin), a1 (La1kin), h1 (Lh1kin), h2 (Lh2kin). ✓

`SelfConjugate -> True` classes: `gaD`, `n1`, `nD`, `a1`, `h1`, `h2` — all six are electrically neutral, colour and SU(2) singlets, and none carries `QuantumNumbers`. ✓

Reference or cached model file read: **none**.

Two notes on choices: `LgaDmix` (the paper's kinetic-mixing operator with the photon) and `LgaDff` (its post-diagonalisation form, ε·e·γ_D·J_EM) describe the same coupling, so only `LgaDff` enters the total sum. All coefficients are dimensionless or explicitly dimension-1 (`lam·vev`), so no EFT cutoff is needed.

```json
{
  "model_name": "MSSMD_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:1812.00380 (CMS Collaboration)"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "epsD",
      "parameter_type": "External",
      "value": "1.*^-5",
      "block_name": "DARKSUSY",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "\\[Epsilon]",
      "description": "Kinetic mixing parameter between the SM photon and the dark photon, dimensionless. Excluded range of the search: 1*^-9 to 1*^-3."
    },
    {
      "name": "gnD",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "DARKSUSY",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "U(1)D gauge coupling of the n1 - nD - gammaD transition current, dimensionless. It drives n1 -> nD + gammaD."
    },
    {
      "name": "ghn1",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "DARKSUSY",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "description": "Coupling of the 125 GeV Higgs boson to two n1 neutralinos, dimensionless. It sets B(h -> 2 n1), quoted in the range 0.1-40%."
    },
    {
      "name": "WgaD",
      "parameter_type": "Internal",
      "value": "epsD^2 ee^2 MgaD/(12 Pi) (1 + 2 MMU^2/MgaD^2) Sqrt[1 - 4 MMU^2/MgaD^2]",
      "description": "Dark photon width [GeV] for gammaD -> mu- mu+ at 100% branching fraction. The lifetime follows tau = eps^-2 f(MgaD)."
    },
    {
      "name": "tb",
      "parameter_type": "External",
      "value": "20.",
      "block_name": "NMSSMLIGHT",
      "order_block": 1,
      "tex": "Tan[\\[Beta]]",
      "description": "Ratio of the vacuum expectation values of the two Higgs doublets. The paper sets tan(beta) = 20."
    },
    {
      "name": "lamh1aa",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "NMSSMLIGHT",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "Dimensionless h1 a1 a1 coupling. The trilinear vertex is lamh1aa*vev, of mass dimension 1. It sets B(h1 -> 2 a1) = 0.3% in the reference model."
    },
    {
      "name": "lamh2aa",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "NMSSMLIGHT",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "description": "Dimensionless h2 a1 a1 coupling. The trilinear vertex is lamh2aa*vev, of mass dimension 1. It sets B(h2 -> 2 a1) = 0.3% in the reference model."
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "gaD",
      "self_conjugate": true,
      "mass": {"sym": "MgaD", "value": "1."},
      "width": {"sym": "WgaD", "value": "Internal"},
      "pdg": 3000022,
      "particle_name": "gaD",
      "full_name": "Dark photon",
      "propagator_label": "gaD",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "n1",
      "self_conjugate": true,
      "mass": {"sym": "Mn1", "value": "10."},
      "width": {"sym": "Wn1", "value": "1.*^-3"},
      "pdg": 1000022,
      "particle_name": "n1",
      "full_name": "Lightest non-dark neutralino",
      "propagator_label": "n1",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "nD",
      "self_conjugate": true,
      "mass": {"sym": "MnD", "value": "1."},
      "width": {"massless": true, "sym": "WnD"},
      "pdg": 3000023,
      "particle_name": "nD",
      "full_name": "Dark neutralino",
      "propagator_label": "nD",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "a1",
      "self_conjugate": true,
      "mass": {"sym": "Ma1", "value": "2."},
      "width": {"sym": "Wa1", "value": "1.*^-6"},
      "pdg": 36,
      "particle_name": "a1",
      "full_name": "Light CP-odd neutral Higgs boson",
      "propagator_label": "a1",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "h1",
      "self_conjugate": true,
      "mass": {"sym": "Mh1", "value": "90."},
      "width": {"sym": "Wh1", "value": "1.*^-2"},
      "pdg": 35,
      "particle_name": "h1",
      "full_name": "First CP-even neutral Higgs boson",
      "propagator_label": "h1",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "h2",
      "self_conjugate": true,
      "mass": {"sym": "Mh2", "value": "125."},
      "width": {"sym": "Wh2", "value": "4.07*^-3"},
      "pdg": 45,
      "particle_name": "h2",
      "full_name": "Second CP-even neutral Higgs boson",
      "propagator_label": "h2",
      "propagator_type": "D",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LgaDkin",
      "expression": "Block[{mu, nu}, -1/4 FS[gaD, mu, nu] FS[gaD, mu, nu] + 1/2 MgaD^2 gaD[mu] gaD[mu]]",
      "delayed": true
    },
    {
      "name": "LgaDmix",
      "expression": "Block[{mu, nu}, -epsD/2 FS[A, mu, nu] FS[gaD, mu, nu]]",
      "delayed": true
    },
    {
      "name": "LgaDff",
      "expression": "Block[{mu}, ExpandIndices[-epsD ee gaD[mu] (-(lbar.Ga[mu].l) + 2/3 (uqbar.Ga[mu].uq) - 1/3 (dqbar.Ga[mu].dq)), FlavorExpand -> {Generation}]]",
      "delayed": true
    },
    {
      "name": "Ln1kin",
      "expression": "Block[{mu}, I/2 n1bar.Ga[mu].del[n1, mu] - 1/2 Mn1 n1bar.n1]",
      "delayed": true
    },
    {
      "name": "LnDkin",
      "expression": "Block[{mu}, I/2 nDbar.Ga[mu].del[nD, mu] - 1/2 MnD nDbar.nD]",
      "delayed": true
    },
    {
      "name": "LnDn1",
      "expression": "Block[{mu}, gnD gaD[mu] nDbar.Ga[mu].n1 + HC[gnD gaD[mu] nDbar.Ga[mu].n1]]",
      "delayed": true
    },
    {
      "name": "Lhn1",
      "expression": "-1/2 ghn1 H n1bar.n1",
      "delayed": true
    },
    {
      "name": "La1kin",
      "expression": "Block[{mu}, 1/2 del[a1, mu] del[a1, mu] - 1/2 Ma1^2 a1 a1]",
      "delayed": true
    },
    {
      "name": "Lh1kin",
      "expression": "Block[{mu}, 1/2 del[h1, mu] del[h1, mu] - 1/2 Mh1^2 h1 h1]",
      "delayed": true
    },
    {
      "name": "Lh2kin",
      "expression": "Block[{mu}, 1/2 del[h2, mu] del[h2, mu] - 1/2 Mh2^2 h2 h2]",
      "delayed": true
    },
    {
      "name": "Lhaa",
      "expression": "-1/2 lamh1aa vev h1 a1 a1 - 1/2 lamh2aa vev h2 a1 a1",
      "delayed": true
    },
    {
      "name": "La1ff",
      "expression": "Block[{sp1, sp2, ff, cc}, ExpandIndices[-I (tb/vev) a1 (Ml[ff] lbar[sp1, ff] Ga[5, sp1, sp2] l[sp2, ff] + Md[ff] dqbar[sp1, ff, cc] Ga[5, sp1, sp2] dq[sp2, ff, cc]) - I (1/(tb vev)) a1 Mu[ff] uqbar[sp1, ff, cc] Ga[5, sp1, sp2] uq[sp2, ff, cc], FlavorExpand -> {Generation}]]",
      "delayed": true
    },
    {
      "name": "LDarkSUSY",
      "expression": "LgaDkin + LgaDff + Ln1kin + LnDkin + LnDn1 + Lhn1",
      "delayed": true
    },
    {
      "name": "LNMSSM",
      "expression": "La1kin + Lh1kin + Lh2kin + Lhaa + La1ff",
      "delayed": true
    },
    {
      "name": "LMSSMD",
      "expression": "LDarkSUSY + LNMSSM",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LMSSMD",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper and the schema. I did not open any reference or cached `.fr` file for this model — none exists in the sandbox.

## What the paper defines as new physics

The paper (CMS, arXiv:1812.00380) interprets a 4µ search in two benchmark sectors:

- **Dark SUSY (the MSSMD sector).** A broken new U(1)_D gives a massive **dark photon γ_D** (0.25–8.5 GeV) that mixes kinetically with the SM photon through **ε**. The chain is `pp → h → 2 n1 → 2 γ_D + 2 n_D → 4µ + X`, with the **lightest non-dark neutralino n1** (10 GeV, Majorana) and the **dark neutralino n_D** (1 GeV, Majorana, stable/invisible). γ_D → µ⁺µ⁻ at 100%; τ_γD(ε, m_γD) = ε⁻² f(m_γD).
- **NMSSM.** Two CP-even neutral Higgs bosons **h1, h2** (90–150 GeV) decay `h1,2 → 2 a1`, and the CP-odd light boson **a1** (0.25–3.55 GeV) decays to µ⁺µ⁻. tan β = 20 is the paper's benchmark.

All six new states are electrically neutral colour and SU(2) singlets, so no new index is needed.

## Mandatory self-audit

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1)_D sum | L/B sum | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LgaDkin | FS[gaD]·FS[gaD] (2+2); MgaD²·gaD·gaD (1+1) | 4; 2 | 1/4; MgaD² | 0; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (real field) | 0 | n/a | self-conj ✓ |
| LgaDmix | FS[A]·FS[gaD] (2+2) | 4 | epsD | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (mixing operator, U(1)_D broken) | 0 | n/a | self-conj ✓ |
| LgaDff | gaD·f̄·f (1+3/2+3/2) | 4 | epsD·ee | 0 ✓ | n/a | 0 (Q_f − Q_f) | 0 (vector current) | singlet (physical eigenstates) | 3̄⊗3 → singlet | 0 | 0 | n/a | self-conj (real current) ✓ |
| Ln1kin | n1bar·Ga·del·n1 (3/2+1+3/2); Mn1·n1bar·n1 | 4; 3 | 1/2; Mn1 | 0; 1 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | Majorana class, bar = CC by construction | self-conj ✓ |
| LnDkin | nDbar·Ga·del·nD; MnD·nDbar·nD | 4; 3 | 1/2; MnD | 0; 1 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | Majorana class | self-conj ✓ |
| LnDn1 | gaD·nDbar·n1 (1+3/2+3/2) | 4 | gnD | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (off-diagonal transition current) | 0 | Majorana; no ψ^c in paper | HC[…] written ✓ |
| Lhn1 | H·n1bar·n1 (1+3/2+3/2) | 4 | ghn1 | 0 ✓ | n/a | 0 | 0 (post-EWSB eigenstate H) | singlet | singlet | 0 | 0 | Majorana | self-conj ✓ |
| La1kin | del·a1·del·a1; Ma1²·a1·a1 | 4; 2 | 1/2; Ma1² | 0; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lh1kin | del·h1·del·h1; Mh1²·h1·h1 | 4; 2 | 1/2; Mh1² | 0; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lh2kin | del·h2·del·h2; Mh2²·h2·h2 | 4; 2 | 1/2; Mh2² | 0; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lhaa | h1·a1·a1 (1+1+1) | 3 | lamh1aa·vev (and lamh2aa·vev) | 1 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| La1ff | a1·f̄·f (1+3/2+3/2) | 4 | tb·Ml[ff]/vev (and 1/(tb·vev)·Mu[ff]) | 0 ✓ | n/a | 0 | 0 (mass eigenstates) | singlet | 3̄⊗3 → singlet | 0 | 0 | n/a | −I·γ5 bilinear is hermitian ✓ |

Kinetic + mass term present and in the total sum: gaD (LgaDkin), n1 (Ln1kin), nD (LnDkin), a1 (La1kin), h1 (Lh1kin), h2 (Lh2kin). ✓

`SelfConjugate -> True` classes: `gaD`, `n1`, `nD`, `a1`, `h1`, `h2` — all six are electrically neutral, colour and SU(2) singlets, and none carries `QuantumNumbers`. ✓

Reference or cached model file read: **none**.

Two notes on choices: `LgaDmix` (the paper's kinetic-mixing operator with the photon) and `LgaDff` (its post-diagonalisation form, ε·e·γ_D·J_EM) describe the same coupling, so only `LgaDff` enters the total sum. All coefficients are dimensionless or explicitly dimension-1 (`lam·vev`), so no EFT cutoff is needed.

```json
{
  "model_name": "MSSMD_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:1812.00380 (CMS Collaboration)"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "epsD",
      "parameter_type": "External",
      "value": "1.*^-5",
      "block_name": "DARKSUSY",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "\\[Epsilon]",
      "description": "Kinetic mixing parameter between the SM photon and the dark photon, dimensionless. Excluded range of the search: 1*^-9 to 1*^-3."
    },
    {
      "name": "gnD",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "DARKSUSY",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "U(1)D gauge coupling of the n1 - nD - gammaD transition current, dimensionless. It drives n1 -> nD + gammaD."
    },
    {
      "name": "ghn1",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "DARKSUSY",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "description": "Coupling of the 125 GeV Higgs boson to two n1 neutralinos, dimensionless. It sets B(h -> 2 n1), quoted in the range 0.1-40%."
    },
    {
      "name": "WgaD",
      "parameter_type": "Internal",
      "value": "epsD^2 ee^2 MgaD/(12 Pi) (1 + 2 MMU^2/MgaD^2) Sqrt[1 - 4 MMU^2/MgaD^2]",
      "description": "Dark photon width [GeV] for gammaD -> mu- mu+ at 100% branching fraction. The lifetime follows tau = eps^-2 f(MgaD)."
    },
    {
      "name": "tb",
      "parameter_type": "External",
      "value": "20.",
      "block_name": "NMSSMLIGHT",
      "order_block": 1,
      "tex": "Tan[\\[Beta]]",
      "description": "Ratio of the vacuum expectation values of the two Higgs doublets. The paper sets tan(beta) = 20."
    },
    {
      "name": "lamh1aa",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "NMSSMLIGHT",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "Dimensionless h1 a1 a1 coupling. The trilinear vertex is lamh1aa*vev, of mass dimension 1. It sets B(h1 -> 2 a1) = 0.3% in the reference model."
    },
    {
      "name": "lamh2aa",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "NMSSMLIGHT",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "description": "Dimensionless h2 a1 a1 coupling. The trilinear vertex is lamh2aa*vev, of mass dimension 1. It sets B(h2 -> 2 a1) = 0.3% in the reference model."
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "gaD",
      "self_conjugate": true,
      "mass": {"sym": "MgaD", "value": "1."},
      "width": {"sym": "WgaD", "value": "Internal"},
      "pdg": 3000022,
      "particle_name": "gaD",
      "full_name": "Dark photon",
      "propagator_label": "gaD",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "n1",
      "self_conjugate": true,
      "mass": {"sym": "Mn1", "value": "10."},
      "width": {"sym": "Wn1", "value": "1.*^-3"},
      "pdg": 1000022,
      "particle_name": "n1",
      "full_name": "Lightest non-dark neutralino",
      "propagator_label": "n1",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "nD",
      "self_conjugate": true,
      "mass": {"sym": "MnD", "value": "1."},
      "width": {"massless": true, "sym": "WnD"},
      "pdg": 3000023,
      "particle_name": "nD",
      "full_name": "Dark neutralino",
      "propagator_label": "nD",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "a1",
      "self_conjugate": true,
      "mass": {"sym": "Ma1", "value": "2."},
      "width": {"sym": "Wa1", "value": "1.*^-6"},
      "pdg": 36,
      "particle_name": "a1",
      "full_name": "Light CP-odd neutral Higgs boson",
      "propagator_label": "a1",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "h1",
      "self_conjugate": true,
      "mass": {"sym": "Mh1", "value": "90."},
      "width": {"sym": "Wh1", "value": "1.*^-2"},
      "pdg": 35,
      "particle_name": "h1",
      "full_name": "First CP-even neutral Higgs boson",
      "propagator_label": "h1",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "h2",
      "self_conjugate": true,
      "mass": {"sym": "Mh2", "value": "125."},
      "width": {"sym": "Wh2", "value": "4.07*^-3"},
      "pdg": 45,
      "particle_name": "h2",
      "full_name": "Second CP-even neutral Higgs boson",
      "propagator_label": "h2",
      "propagator_type": "D",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LgaDkin",
      "expression": "Block[{mu, nu}, -1/4 FS[gaD, mu, nu] FS[gaD, mu, nu] + 1/2 MgaD^2 gaD[mu] gaD[mu]]",
      "delayed": true
    },
    {
      "name": "LgaDmix",
      "expression": "Block[{mu, nu}, -epsD/2 FS[A, mu, nu] FS[gaD, mu, nu]]",
      "delayed": true
    },
    {
      "name": "LgaDff",
      "expression": "Block[{mu}, ExpandIndices[-epsD ee gaD[mu] (-(lbar.Ga[mu].l) + 2/3 (uqbar.Ga[mu].uq) - 1/3 (dqbar.Ga[mu].dq)), FlavorExpand -> {Generation}]]",
      "delayed": true
    },
    {
      "name": "Ln1kin",
      "expression": "Block[{mu}, I/2 n1bar.Ga[mu].del[n1, mu] - 1/2 Mn1 n1bar.n1]",
      "delayed": true
    },
    {
      "name": "LnDkin",
      "expression": "Block[{mu}, I/2 nDbar.Ga[mu].del[nD, mu] - 1/2 MnD nDbar.nD]",
      "delayed": true
    },
    {
      "name": "LnDn1",
      "expression": "Block[{mu}, gnD gaD[mu] nDbar.Ga[mu].n1 + HC[gnD gaD[mu] nDbar.Ga[mu].n1]]",
      "delayed": true
    },
    {
      "name": "Lhn1",
      "expression": "-1/2 ghn1 H n1bar.n1",
      "delayed": true
    },
    {
      "name": "La1kin",
      "expression": "Block[{mu}, 1/2 del[a1, mu] del[a1, mu] - 1/2 Ma1^2 a1 a1]",
      "delayed": true
    },
    {
      "name": "Lh1kin",
      "expression": "Block[{mu}, 1/2 del[h1, mu] del[h1, mu] - 1/2 Mh1^2 h1 h1]",
      "delayed": true
    },
    {
      "name": "Lh2kin",
      "expression": "Block[{mu}, 1/2 del[h2, mu] del[h2, mu] - 1/2 Mh2^2 h2 h2]",
      "delayed": true
    },
    {
      "name": "Lhaa",
      "expression": "-1/2 lamh1aa vev h1 a1 a1 - 1/2 lamh2aa vev h2 a1 a1",
      "delayed": true
    },
    {
      "name": "La1ff",
      "expression": "Block[{sp1, sp2, ff, cc}, ExpandIndices[-I (tb/vev) a1 (Ml[ff] lbar[sp1, ff] Ga[5, sp1, sp2] l[sp2, ff] + Md[ff] dqbar[sp1, ff, cc] Ga[5, sp1, sp2] dq[sp2, ff, cc]) - I (1/(tb vev)) a1 Mu[ff] uqbar[sp1, ff, cc] Ga[5, sp1, sp2] uq[sp2, ff, cc], FlavorExpand -> {Generation}]]",
      "delayed": true
    },
    {
      "name": "LDarkSUSY",
      "expression": "LgaDkin + LgaDff + Ln1kin + LnDkin + LnDn1 + Lhn1",
      "delayed": true
    },
    {
      "name": "LNMSSM",
      "expression": "La1kin + Lh1kin + Lh2kin + Lhaa + La1ff",
      "delayed": true
    },
    {
      "name": "LMSSMD",
      "expression": "LDarkSUSY + LNMSSM",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LMSSMD",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```