I'll start by reading the paper and the schema files.
I read the paper, the schema, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content extracted from the paper

**Table I + Eqs. (1)–(4)**: four independent complex scalar leptoquarks, colour triplets, forming two SU(2)_L doublets. Their conjugates give the other four rows of Table I.

| field | constituent | Q | t3L | Y | doublet |
|---|---|---|---|---|---|
| `Pi53` | ēR uL | +5/3 | +1/2 | +7/6 | `Pi76` (upper) |
| `Pi23d` | ēR dL | +2/3 | −1/2 | +7/6 | `Pi76` (lower) |
| `Pi23u` | ν̄R uL | +2/3 | +1/2 | +1/6 | `Pi16` (upper) |
| `Pim13` | ν̄R dL | −1/3 | −1/2 | +1/6 | `Pi16` (lower) |

Key choices:
- The physical states must sit inside SU(2) doublets, or `DC` would give electric charge = Y instead of Q = T3 + Y. So I add two `Unphysical` doublets `Pi76`, `Pi16` (the SM.fr `Phi` idiom) that carry Y and drive the gauge kinetic term; the physical states carry Q and their own masses.
- SM.fr `Phi` has Y = +1/2 and Q = T3 + Y, so the paper's Y = +7/6, +1/6 are used unchanged. No new U(1) exists in this model.
- νR: SM.fr declares `vl` as a full Dirac field whose right-handed part is sterile, so `ν̄R` is `vlbar.ProjM`. No new fermion class is needed.
- Couplings `gΠi = (FΠi/Λ)²` are dimensionless, and the paper states Eqs. (1)–(3) are dimension-4 renormalizable and independent of Λcut. So there is **no** 1/Λⁿ factor anywhere. Λ is declared only as documentation.
- Flavour: Eq. (4) makes each `gΠi` a 3×3 matrix over (lepton generation, quark generation). λ_eu = `gPi53[1,1]`, λ_µc = `gPi53[2,2]`, λ_τb = `gPi23d[3,3]`.
- Eq. (1) prints `+M²Φ†Φ`; the correct sign for a mass term is `−M²Φ†Φ`, which I use.
- Composite fermions F ~ ψRΠ and the colour-singlet Π^{0,±} are explicitly deferred to other papers, so they are out of scope.

## Self-audit table

| term | fields | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L sum | CC[] | HC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LLQKin` (Pi76) | `DC[Pi76bar]·DC[Pi76]` | 1+1+1+1=4 | none | 0 ✓ | n/a | 0 | −7/6+7/6=0 ✓ | doublet ⊗ anti-doublet, shared `ii` | shared `cc` (3⊗3̄) | none | 0 | n/a | self-conjugate |
| `LLQKin` (Pi16) | `DC[Pi16bar]·DC[Pi16]` | 4 | none | 0 ✓ | n/a | 0 | −1/6+1/6=0 ✓ | shared `ii` | shared `cc` | none | 0 | n/a | self-conjugate |
| `LLQMass` (Pi53) | `Pi53bar Pi53` | 2 | `MPi53^2` | 2 ✓ | n/a | −5/3+5/3=0 ✓ | 0 ✓ | singlet | shared `cc` | none | +1−1=0 | n/a | self-conjugate |
| `LLQMass` (Pi23u) | `Pi23ubar Pi23u` | 2 | `MPi23u^2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | shared `cc` | none | 0 | n/a | self-conjugate |
| `LLQMass` (Pi23d) | `Pi23dbar Pi23d` | 2 | `MPi23d^2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | shared `cc` | none | 0 | n/a | self-conjugate |
| `LLQMass` (Pim13) | `Pim13bar Pim13` | 2 | `MPim13^2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | shared `cc` | none | 0 | n/a | self-conjugate |
| `LLQYuk` t1 (Eq. 3a) | `lbar.ProjM.uq Pi53bar` | 3/2+3/2+1=4 | `gPi53[ff1,ff2]` | 0 ✓ | n/a | +1+2/3−5/3=0 ✓ | +1+1/6−7/6=0 ✓ | component of `Pi76`⊗`QL`, singlet | `uq[cc]` with `Pi53bar[cc]` | none | −1+0+1=0 ✓ | n/a (no ψ^c in paper) | `HC[LLQYuk]` |
| `LLQYuk` t2 (Eq. 3c) | `vlbar.ProjM.uq Pi23ubar` | 4 | `gPi23u[ff1,ff2]` | 0 ✓ | n/a | 0+2/3−2/3=0 ✓ | 0+1/6−1/6=0 ✓ | singlet | shared `cc` | none | −1+0+1=0 ✓ | n/a | `HC[LLQYuk]` |
| `LLQYuk` t3 (Eq. 3d) | `lbar.ProjM.dq Pi23dbar` | 4 | `gPi23d[ff1,ff2]` | 0 ✓ | n/a | +1−1/3−2/3=0 ✓ | +1+1/6−7/6=0 ✓ | singlet | shared `cc` | none | −1+0+1=0 ✓ | n/a | `HC[LLQYuk]` |
| `LLQYuk` t4 (Eq. 3b) | `vlbar.ProjM.dq Pim13bar` | 4 | `gPi13[ff1,ff2]` | 0 ✓ | n/a | 0−1/3+1/3=0 ✓ | 0+1/6−1/6=0 ✓ | singlet | shared `cc` | none | −1+0+1=0 ✓ | n/a | `HC[LLQYuk]` |

Kinetic + mass confirmation: `Pi53`, `Pi23u`, `Pi23d`, `Pim13` each get a gauge kinetic term through their parent doublet (`LLQKin`) and an explicit mass term (`LLQMass`); both are in the total sum `LNJLLQ := LLQKin + LLQMass + LLQYuk + HC[LLQYuk]`.

`SelfConjugate -> True` classes: **none**. Every new field is complex, so every class carries `SelfConjugate -> False`, and each `QuantumNumbers` block is therefore allowed.

Reference or cached model file read: **none**. Only the paper text, `frmodel.py`, `render.py` and `SM.fr` were opened.

```json
{
  "model_name": "NJLComposite_gen",
  "info": {
    "authors": [
      "S. Ajmal",
      "J. T. Gaglione",
      "A. Gurrola",
      "O. Panella",
      "M. Presilla",
      "F. Romeo",
      "H. Sun",
      "S.-S. Xue"
    ],
    "version": "1.0",
    "date": "03. 06. 2024",
    "institutions": [
      "Universita degli Studi di Perugia and INFN Sezione di Perugia",
      "Vanderbilt University",
      "Karlsruhe Institute of Technology",
      "Dalian University of Technology",
      "ICRANet Pescara"
    ],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Lam",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "NJLPARS",
      "order_block": 1,
      "description": "NJL composite scale Lambda [GeV]; MPi ~ Lam and FPi ~ Lam. Eqs.(1)-(3) are dimension-4 renormalizable, so Lam does not appear as a 1/Lam^n factor in any operator."
    },
    {
      "name": "gPi53",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "block_name": "GPI53",
      "interaction_order": [
        "QED",
        1
      ],
      "value_rules": [
        {
          "lhs": "gPi53[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "gPi53[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "gPi53[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[3,3]",
          "rhs": "1."
        }
      ],
      "tex": "Subscript[g,\\[CapitalPi]5/3]",
      "description": "Dimensionless composite Yukawa coupling gPi(5/3) = (FPi/Lam)^2 ~ O(1) of Pi53 to (lbar_R^i uq_L^j), Eq.(3) first term. First index = lepton generation, second index = up-quark generation. Off-diagonal entries are the CKM-like mixing factors (UR^dagger UL)_ij of Eq.(4). lambda_eu = gPi53[1,1], lambda_muc = gPi53[2,2]."
    },
    {
      "name": "gPi23u",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "block_name": "GPI23U",
      "interaction_order": [
        "QED",
        1
      ],
      "value_rules": [
        {
          "lhs": "gPi23u[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "gPi23u[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "gPi23u[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[3,3]",
          "rhs": "1."
        }
      ],
      "tex": "Subscript[g,\\[CapitalPi]-2/3u]",
      "description": "Dimensionless composite Yukawa coupling gPi(-2/3) = (FPi/Lam)^2 ~ O(1) of Pi23u to (vlbar_R^i uq_L^j), Eq.(3) third term. First index = neutrino generation, second index = up-quark generation."
    },
    {
      "name": "gPi23d",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "block_name": "GPI23D",
      "interaction_order": [
        "QED",
        1
      ],
      "value_rules": [
        {
          "lhs": "gPi23d[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "gPi23d[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "gPi23d[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[3,3]",
          "rhs": "1."
        }
      ],
      "tex": "Subscript[g,\\[CapitalPi]-2/3d]",
      "description": "Dimensionless composite Yukawa coupling gPi(-2/3) = (FPi/Lam)^2 ~ O(1) of Pi23d to (lbar_R^i dq_L^j), Eq.(3) fourth term. First index = lepton generation, second index = down-quark generation. lambda_taub = gPi23d[3,3]."
    },
    {
      "name": "gPi13",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "block_name": "GPI13",
      "interaction_order": [
        "QED",
        1
      ],
      "value_rules": [
        {
          "lhs": "gPi13[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "gPi13[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "gPi13[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[3,3]",
          "rhs": "1."
        }
      ],
      "tex": "Subscript[g,\\[CapitalPi]1/3]",
      "description": "Dimensionless composite Yukawa coupling gPi(1/3) = (FPi/Lam)^2 ~ O(1) of Pim13 to (vlbar_R^i dq_L^j), Eq.(3) second term. First index = neutrino generation, second index = down-quark generation."
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "Pi53",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "massless": false,
        "sym": "MPi53",
        "value": "1000."
      },
      "width": {
        "massless": false,
        "sym": "WPi53",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "5/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000005,
      "particle_name": "pi53",
      "antiparticle_name": "pi53~",
      "full_name": "Composite leptoquark Pi^(+5/3) ~ (eRbar uL), R2 state",
      "propagator_label": "Pi53",
      "propagator_type": "D",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Pi23u",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "massless": false,
        "sym": "MPi23u",
        "value": "1000."
      },
      "width": {
        "massless": false,
        "sym": "WPi23u",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "2/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000006,
      "particle_name": "pi23u",
      "antiparticle_name": "pi23u~",
      "full_name": "Composite leptoquark Pi^(+2/3)_u ~ (vRbar uL), Rtilde2 state",
      "propagator_label": "Pi23u",
      "propagator_type": "D",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "Pi23d",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "massless": false,
        "sym": "MPi23d",
        "value": "1000."
      },
      "width": {
        "massless": false,
        "sym": "WPi23d",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "2/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000007,
      "particle_name": "pi23d",
      "antiparticle_name": "pi23d~",
      "full_name": "Composite leptoquark Pi^(+2/3)_d ~ (eRbar dL), R2 state",
      "propagator_label": "Pi23d",
      "propagator_type": "D",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "Pim13",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "massless": false,
        "sym": "MPim13",
        "value": "1000."
      },
      "width": {
        "massless": false,
        "sym": "WPim13",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "-1/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000008,
      "particle_name": "pim13",
      "antiparticle_name": "pim13~",
      "full_name": "Composite leptoquark Pi^(-1/3) ~ (vRbar dL), Rtilde2 state",
      "propagator_label": "Pim13",
      "propagator_type": "D",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 110,
      "class_name": "Pi76",
      "self_conjugate": false,
      "indices": [
        "SU2D",
        "Colour"
      ],
      "flavor_index": "SU2D",
      "quantum_numbers": {
        "Y": "7/6"
      },
      "unphysical": true,
      "definitions": [
        "Pi76[1, cc_] -> Pi53[cc]",
        "Pi76[2, cc_] -> Pi23d[cc]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 111,
      "class_name": "Pi16",
      "self_conjugate": false,
      "indices": [
        "SU2D",
        "Colour"
      ],
      "flavor_index": "SU2D",
      "quantum_numbers": {
        "Y": "1/6"
      },
      "unphysical": true,
      "definitions": [
        "Pi16[1, cc_] -> Pi23u[cc]",
        "Pi16[2, cc_] -> Pim13[cc]"
      ]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LLQKin",
      "expression": "Block[{mu, ii, cc}, ExpandIndices[ DC[Pi76bar[ii, cc], mu] DC[Pi76[ii, cc], mu] + DC[Pi16bar[ii, cc], mu] DC[Pi16[ii, cc], mu], FlavorExpand -> {SU2D, SU2W}]]",
      "delayed": true
    },
    {
      "name": "LLQMass",
      "expression": "Block[{cc}, ExpandIndices[ - MPi53^2 Pi53bar[cc] Pi53[cc] - MPi23u^2 Pi23ubar[cc] Pi23u[cc] - MPi23d^2 Pi23dbar[cc] Pi23d[cc] - MPim13^2 Pim13bar[cc] Pim13[cc] ]]",
      "delayed": true
    },
    {
      "name": "LLQYuk",
      "expression": "Block[{sp1, sp2, ff1, ff2, cc}, ExpandIndices[ gPi53[ff1, ff2] (lbar[sp1, ff1].ProjM[sp1, sp2].uq[sp2, ff2, cc]) Pi53bar[cc] + gPi13[ff1, ff2] (vlbar[sp1, ff1].ProjM[sp1, sp2].dq[sp2, ff2, cc]) Pim13bar[cc] + gPi23u[ff1, ff2] (vlbar[sp1, ff1].ProjM[sp1, sp2].uq[sp2, ff2, cc]) Pi23ubar[cc] + gPi23d[ff1, ff2] (lbar[sp1, ff1].ProjM[sp1, sp2].dq[sp2, ff2, cc]) Pi23dbar[cc] ]]",
      "delayed": true
    },
    {
      "name": "LNJLLQ",
      "expression": "LLQKin + LLQMass + LLQYuk + HC[LLQYuk]",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper, the schema, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content extracted from the paper

**Table I + Eqs. (1)–(4)**: four independent complex scalar leptoquarks, colour triplets, forming two SU(2)_L doublets. Their conjugates give the other four rows of Table I.

| field | constituent | Q | t3L | Y | doublet |
|---|---|---|---|---|---|
| `Pi53` | ēR uL | +5/3 | +1/2 | +7/6 | `Pi76` (upper) |
| `Pi23d` | ēR dL | +2/3 | −1/2 | +7/6 | `Pi76` (lower) |
| `Pi23u` | ν̄R uL | +2/3 | +1/2 | +1/6 | `Pi16` (upper) |
| `Pim13` | ν̄R dL | −1/3 | −1/2 | +1/6 | `Pi16` (lower) |

Key choices:
- The physical states must sit inside SU(2) doublets, or `DC` would give electric charge = Y instead of Q = T3 + Y. So I add two `Unphysical` doublets `Pi76`, `Pi16` (the SM.fr `Phi` idiom) that carry Y and drive the gauge kinetic term; the physical states carry Q and their own masses.
- SM.fr `Phi` has Y = +1/2 and Q = T3 + Y, so the paper's Y = +7/6, +1/6 are used unchanged. No new U(1) exists in this model.
- νR: SM.fr declares `vl` as a full Dirac field whose right-handed part is sterile, so `ν̄R` is `vlbar.ProjM`. No new fermion class is needed.
- Couplings `gΠi = (FΠi/Λ)²` are dimensionless, and the paper states Eqs. (1)–(3) are dimension-4 renormalizable and independent of Λcut. So there is **no** 1/Λⁿ factor anywhere. Λ is declared only as documentation.
- Flavour: Eq. (4) makes each `gΠi` a 3×3 matrix over (lepton generation, quark generation). λ_eu = `gPi53[1,1]`, λ_µc = `gPi53[2,2]`, λ_τb = `gPi23d[3,3]`.
- Eq. (1) prints `+M²Φ†Φ`; the correct sign for a mass term is `−M²Φ†Φ`, which I use.
- Composite fermions F ~ ψRΠ and the colour-singlet Π^{0,±} are explicitly deferred to other papers, so they are out of scope.

## Self-audit table

| term | fields | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L sum | CC[] | HC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LLQKin` (Pi76) | `DC[Pi76bar]·DC[Pi76]` | 1+1+1+1=4 | none | 0 ✓ | n/a | 0 | −7/6+7/6=0 ✓ | doublet ⊗ anti-doublet, shared `ii` | shared `cc` (3⊗3̄) | none | 0 | n/a | self-conjugate |
| `LLQKin` (Pi16) | `DC[Pi16bar]·DC[Pi16]` | 4 | none | 0 ✓ | n/a | 0 | −1/6+1/6=0 ✓ | shared `ii` | shared `cc` | none | 0 | n/a | self-conjugate |
| `LLQMass` (Pi53) | `Pi53bar Pi53` | 2 | `MPi53^2` | 2 ✓ | n/a | −5/3+5/3=0 ✓ | 0 ✓ | singlet | shared `cc` | none | +1−1=0 | n/a | self-conjugate |
| `LLQMass` (Pi23u) | `Pi23ubar Pi23u` | 2 | `MPi23u^2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | shared `cc` | none | 0 | n/a | self-conjugate |
| `LLQMass` (Pi23d) | `Pi23dbar Pi23d` | 2 | `MPi23d^2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | shared `cc` | none | 0 | n/a | self-conjugate |
| `LLQMass` (Pim13) | `Pim13bar Pim13` | 2 | `MPim13^2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | shared `cc` | none | 0 | n/a | self-conjugate |
| `LLQYuk` t1 (Eq. 3a) | `lbar.ProjM.uq Pi53bar` | 3/2+3/2+1=4 | `gPi53[ff1,ff2]` | 0 ✓ | n/a | +1+2/3−5/3=0 ✓ | +1+1/6−7/6=0 ✓ | component of `Pi76`⊗`QL`, singlet | `uq[cc]` with `Pi53bar[cc]` | none | −1+0+1=0 ✓ | n/a (no ψ^c in paper) | `HC[LLQYuk]` |
| `LLQYuk` t2 (Eq. 3c) | `vlbar.ProjM.uq Pi23ubar` | 4 | `gPi23u[ff1,ff2]` | 0 ✓ | n/a | 0+2/3−2/3=0 ✓ | 0+1/6−1/6=0 ✓ | singlet | shared `cc` | none | −1+0+1=0 ✓ | n/a | `HC[LLQYuk]` |
| `LLQYuk` t3 (Eq. 3d) | `lbar.ProjM.dq Pi23dbar` | 4 | `gPi23d[ff1,ff2]` | 0 ✓ | n/a | +1−1/3−2/3=0 ✓ | +1+1/6−7/6=0 ✓ | singlet | shared `cc` | none | −1+0+1=0 ✓ | n/a | `HC[LLQYuk]` |
| `LLQYuk` t4 (Eq. 3b) | `vlbar.ProjM.dq Pim13bar` | 4 | `gPi13[ff1,ff2]` | 0 ✓ | n/a | 0−1/3+1/3=0 ✓ | 0+1/6−1/6=0 ✓ | singlet | shared `cc` | none | −1+0+1=0 ✓ | n/a | `HC[LLQYuk]` |

Kinetic + mass confirmation: `Pi53`, `Pi23u`, `Pi23d`, `Pim13` each get a gauge kinetic term through their parent doublet (`LLQKin`) and an explicit mass term (`LLQMass`); both are in the total sum `LNJLLQ := LLQKin + LLQMass + LLQYuk + HC[LLQYuk]`.

`SelfConjugate -> True` classes: **none**. Every new field is complex, so every class carries `SelfConjugate -> False`, and each `QuantumNumbers` block is therefore allowed.

Reference or cached model file read: **none**. Only the paper text, `frmodel.py`, `render.py` and `SM.fr` were opened.

```json
{
  "model_name": "NJLComposite_gen",
  "info": {
    "authors": [
      "S. Ajmal",
      "J. T. Gaglione",
      "A. Gurrola",
      "O. Panella",
      "M. Presilla",
      "F. Romeo",
      "H. Sun",
      "S.-S. Xue"
    ],
    "version": "1.0",
    "date": "03. 06. 2024",
    "institutions": [
      "Universita degli Studi di Perugia and INFN Sezione di Perugia",
      "Vanderbilt University",
      "Karlsruhe Institute of Technology",
      "Dalian University of Technology",
      "ICRANet Pescara"
    ],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Lam",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "NJLPARS",
      "order_block": 1,
      "description": "NJL composite scale Lambda [GeV]; MPi ~ Lam and FPi ~ Lam. Eqs.(1)-(3) are dimension-4 renormalizable, so Lam does not appear as a 1/Lam^n factor in any operator."
    },
    {
      "name": "gPi53",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "block_name": "GPI53",
      "interaction_order": [
        "QED",
        1
      ],
      "value_rules": [
        {
          "lhs": "gPi53[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "gPi53[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "gPi53[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi53[3,3]",
          "rhs": "1."
        }
      ],
      "tex": "Subscript[g,\\[CapitalPi]5/3]",
      "description": "Dimensionless composite Yukawa coupling gPi(5/3) = (FPi/Lam)^2 ~ O(1) of Pi53 to (lbar_R^i uq_L^j), Eq.(3) first term. First index = lepton generation, second index = up-quark generation. Off-diagonal entries are the CKM-like mixing factors (UR^dagger UL)_ij of Eq.(4). lambda_eu = gPi53[1,1], lambda_muc = gPi53[2,2]."
    },
    {
      "name": "gPi23u",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "block_name": "GPI23U",
      "interaction_order": [
        "QED",
        1
      ],
      "value_rules": [
        {
          "lhs": "gPi23u[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "gPi23u[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "gPi23u[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23u[3,3]",
          "rhs": "1."
        }
      ],
      "tex": "Subscript[g,\\[CapitalPi]-2/3u]",
      "description": "Dimensionless composite Yukawa coupling gPi(-2/3) = (FPi/Lam)^2 ~ O(1) of Pi23u to (vlbar_R^i uq_L^j), Eq.(3) third term. First index = neutrino generation, second index = up-quark generation."
    },
    {
      "name": "gPi23d",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "block_name": "GPI23D",
      "interaction_order": [
        "QED",
        1
      ],
      "value_rules": [
        {
          "lhs": "gPi23d[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "gPi23d[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "gPi23d[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi23d[3,3]",
          "rhs": "1."
        }
      ],
      "tex": "Subscript[g,\\[CapitalPi]-2/3d]",
      "description": "Dimensionless composite Yukawa coupling gPi(-2/3) = (FPi/Lam)^2 ~ O(1) of Pi23d to (lbar_R^i dq_L^j), Eq.(3) fourth term. First index = lepton generation, second index = down-quark generation. lambda_taub = gPi23d[3,3]."
    },
    {
      "name": "gPi13",
      "parameter_type": "External",
      "indices": [
        "Generation",
        "Generation"
      ],
      "block_name": "GPI13",
      "interaction_order": [
        "QED",
        1
      ],
      "value_rules": [
        {
          "lhs": "gPi13[1,1]",
          "rhs": "1."
        },
        {
          "lhs": "gPi13[1,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[1,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[2,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[2,2]",
          "rhs": "1."
        },
        {
          "lhs": "gPi13[2,3]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[3,1]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[3,2]",
          "rhs": "0."
        },
        {
          "lhs": "gPi13[3,3]",
          "rhs": "1."
        }
      ],
      "tex": "Subscript[g,\\[CapitalPi]1/3]",
      "description": "Dimensionless composite Yukawa coupling gPi(1/3) = (FPi/Lam)^2 ~ O(1) of Pim13 to (vlbar_R^i dq_L^j), Eq.(3) second term. First index = neutrino generation, second index = down-quark generation."
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "Pi53",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "massless": false,
        "sym": "MPi53",
        "value": "1000."
      },
      "width": {
        "massless": false,
        "sym": "WPi53",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "5/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000005,
      "particle_name": "pi53",
      "antiparticle_name": "pi53~",
      "full_name": "Composite leptoquark Pi^(+5/3) ~ (eRbar uL), R2 state",
      "propagator_label": "Pi53",
      "propagator_type": "D",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Pi23u",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "massless": false,
        "sym": "MPi23u",
        "value": "1000."
      },
      "width": {
        "massless": false,
        "sym": "WPi23u",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "2/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000006,
      "particle_name": "pi23u",
      "antiparticle_name": "pi23u~",
      "full_name": "Composite leptoquark Pi^(+2/3)_u ~ (vRbar uL), Rtilde2 state",
      "propagator_label": "Pi23u",
      "propagator_type": "D",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "Pi23d",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "massless": false,
        "sym": "MPi23d",
        "value": "1000."
      },
      "width": {
        "massless": false,
        "sym": "WPi23d",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "2/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000007,
      "particle_name": "pi23d",
      "antiparticle_name": "pi23d~",
      "full_name": "Composite leptoquark Pi^(+2/3)_d ~ (eRbar dL), R2 state",
      "propagator_label": "Pi23d",
      "propagator_type": "D",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "Pim13",
      "self_conjugate": false,
      "indices": [
        "Colour"
      ],
      "mass": {
        "massless": false,
        "sym": "MPim13",
        "value": "1000."
      },
      "width": {
        "massless": false,
        "sym": "WPim13",
        "value": "Automatic"
      },
      "quantum_numbers": {
        "Q": "-1/3",
        "LeptonNumber": "-1"
      },
      "pdg": 9000008,
      "particle_name": "pim13",
      "antiparticle_name": "pim13~",
      "full_name": "Composite leptoquark Pi^(-1/3) ~ (vRbar dL), Rtilde2 state",
      "propagator_label": "Pim13",
      "propagator_type": "D",
      "propagator_arrow": "Forward",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 110,
      "class_name": "Pi76",
      "self_conjugate": false,
      "indices": [
        "SU2D",
        "Colour"
      ],
      "flavor_index": "SU2D",
      "quantum_numbers": {
        "Y": "7/6"
      },
      "unphysical": true,
      "definitions": [
        "Pi76[1, cc_] -> Pi53[cc]",
        "Pi76[2, cc_] -> Pi23d[cc]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 111,
      "class_name": "Pi16",
      "self_conjugate": false,
      "indices": [
        "SU2D",
        "Colour"
      ],
      "flavor_index": "SU2D",
      "quantum_numbers": {
        "Y": "1/6"
      },
      "unphysical": true,
      "definitions": [
        "Pi16[1, cc_] -> Pi23u[cc]",
        "Pi16[2, cc_] -> Pim13[cc]"
      ]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LLQKin",
      "expression": "Block[{mu, ii, cc}, ExpandIndices[ DC[Pi76bar[ii, cc], mu] DC[Pi76[ii, cc], mu] + DC[Pi16bar[ii, cc], mu] DC[Pi16[ii, cc], mu], FlavorExpand -> {SU2D, SU2W}]]",
      "delayed": true
    },
    {
      "name": "LLQMass",
      "expression": "Block[{cc}, ExpandIndices[ - MPi53^2 Pi53bar[cc] Pi53[cc] - MPi23u^2 Pi23ubar[cc] Pi23u[cc] - MPi23d^2 Pi23dbar[cc] Pi23d[cc] - MPim13^2 Pim13bar[cc] Pim13[cc] ]]",
      "delayed": true
    },
    {
      "name": "LLQYuk",
      "expression": "Block[{sp1, sp2, ff1, ff2, cc}, ExpandIndices[ gPi53[ff1, ff2] (lbar[sp1, ff1].ProjM[sp1, sp2].uq[sp2, ff2, cc]) Pi53bar[cc] + gPi13[ff1, ff2] (vlbar[sp1, ff1].ProjM[sp1, sp2].dq[sp2, ff2, cc]) Pim13bar[cc] + gPi23u[ff1, ff2] (vlbar[sp1, ff1].ProjM[sp1, sp2].uq[sp2, ff2, cc]) Pi23ubar[cc] + gPi23d[ff1, ff2] (lbar[sp1, ff1].ProjM[sp1, sp2].dq[sp2, ff2, cc]) Pi23dbar[cc] ]]",
      "delayed": true
    },
    {
      "name": "LNJLLQ",
      "expression": "LLQKin + LLQMass + LLQYuk + HC[LLQYuk]",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```