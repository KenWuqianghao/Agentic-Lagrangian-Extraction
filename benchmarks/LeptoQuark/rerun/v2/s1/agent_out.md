I'll start by reading the paper and the schema.
I read the paper and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content found in the paper

Section 3, eqs. (9)–(13): three new **massive vectors**, all colour/EW mass eigenstates:

| state | spin | colour | SU(2)L | Y | Q | mass |
|---|---|---|---|---|---|---|
| `U1` vector leptoquark | V | triplet | singlet | 2/3 | 2/3 | `MU1` |
| `Zp` (Z′) | V | singlet | singlet | 0 | 0 | `MZp` |
| `Gp` (coloron G′) | V | octet | singlet | 0 | 0 | `MGp` |

`U1` is complex (`SelfConjugate -> False`); `Zp` and `Gp` are real. The leptoquark mass symbol is `MU1`, not `MU`, because `MU` is already the up-quark mass in `SM.fr`.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling | coupling dim (= 4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L number sum | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LU1Kin | `DC[U1bar]DC[U1]`, `MU1^2 U1bar U1` | 4 | `1`, `MU1^2` | 0 | n/a | −2/3+2/3=0 | −2/3+2/3=0 | singlet×singlet | `cc` shared: 3̄⊗3 | none | 0 | n/a | self-conjugate (real) |
| LU1Gauge | `U1bar U1 FS[G,a]`; `U1bar U1 FS[B]` | 4 | `gs(1−kU)`, `g1 2/3 (1−kUt)` | 0 | n/a | 0 | 0 | singlet | `T[aa,c1,c2]`: 3̄⊗8⊗3 / `c1` shared | none | 0 | n/a | self-Hermitian (F^{μν} antisym.) |
| LU1Int (L) | `U1 QLbar Ga LL` | 4 | `gU betaL` | 0 | n/a | up: −2/3+0+2/3=0; down: +1/3−1+2/3=0 | +1/6−1/2+2/3−1/3… = −1/6−1/2+2/3=0 | shared `ii` (anti-doublet×doublet) | `cc` shared: 3̄⊗3 | none | 0−1+1=0 (U1 has L=−1) | n/a (no ψ^c in paper) | `HC[lag]` |
| LU1Int (R) | `U1 dRbar Ga lR` | 4 | `gU betaR` | 0 | n/a | +1/3−1+2/3=0 | +1/3−1+2/3=0 | all singlets | `cc` shared: 3̄⊗3 | none | 0−1+1=0 | n/a | `HC[lag]` |
| LZpKin | `FS[Zp]^2`, `MZp^2 Zp Zp` | 4 | `1`, `MZp^2` | 0 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field |
| LZpInt | `Zp fbar Ga f` | 4 | `gZp zeta` | 0 | n/a | 0 (vector current) | 0 | shared `ii` per monomial | shared colour per monomial | none | 0 | n/a | Hermitian (ζ Hermitian, Zp real) |
| LGpKin | `DC[Gp]DC[Gp]`, `MGp^2 Gp Gp` | 4 | `1`, `MGp^2` | 0 | n/a | 0 | 0 | singlet | `aa` shared: 8⊗8 | none | 0 | n/a | real field |
| LGpGauge | `del[Gp] FS[G]`; `f Gp Gp FS[G]` | 4 | `kGp`, `gs kGpt` | 0 | n/a | 0 | 0 | singlet | 8⊗8; `f[aa,bb,cc]` | none | 0 | n/a | self-Hermitian |
| LGpInt | `Gp qbar T Ga q` | 4 | `gGp kappa` | 0 | n/a | 0 | 0 | shared `ii` | `T[aa,c1,c2]`: 3̄⊗8⊗3 | none | 0 | n/a | Hermitian (κ real diagonal) |
| U1 free field | kinetic + `MU1` mass present in `LU1Kin`, summed into `LNP` | — | — | — | — | — | — | — | — | — | — | — | ✓ |
| Zp free field | kinetic + `MZp` mass present in `LZpKin`, summed into `LNP` | — | — | — | — | — | — | — | — | — | — | — | ✓ |
| Gp free field | kinetic + `MGp` mass present in `LGpKin`, summed into `LNP` | — | — | — | — | — | — | — | — | — | — | — | ✓ |

`SelfConjugate -> True` classes: `Zp`, `Gp`. Both carry **no** `QuantumNumbers`.

No operator has d > 4, so no EFT cutoff parameter is needed. No charge-conjugated fermion (`ψ^c`) appears in eqs. (9)–(11), so no `CC[...]` is used.

Reference or cached model file read: **none**.

```json
{
  "model_name": "LeptoQuark_gen",
  "info": {
    "authors": ["M. J. Baker", "J. Fuentes-Martin", "G. Isidori", "M. Koenig"],
    "version": "1.0",
    "date": "2019",
    "institutions": ["Physik-Institut, Universitaet Zuerich"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gU",
      "parameter_type": "External",
      "value": "3.",
      "block_name": "LEPTOQUARK",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Overall U1 vector leptoquark coupling, Eq.(9)"
    },
    {
      "name": "kU",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "LEPTOQUARK",
      "order_block": 2,
      "description": "kappa_U, non-minimal U1-gluon coupling, Eq.(9); 0 in gauge models, 1 for minimal coupling"
    },
    {
      "name": "kUt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "LEPTOQUARK",
      "order_block": 3,
      "description": "kappa-tilde_U, non-minimal U1-hypercharge coupling, Eq.(9)"
    },
    {
      "name": "bL13",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "LEPTOQUARK",
      "order_block": 4,
      "description": "beta_L^13, left-handed U1 coupling to first-generation quarks, Eq.(13)"
    },
    {
      "name": "bL23",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "LEPTOQUARK",
      "order_block": 5,
      "description": "beta_L^23, 2-3 quark mixing of the U1, benchmark 0.1, Eq.(14)"
    },
    {
      "name": "bL32",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "LEPTOQUARK",
      "order_block": 6,
      "description": "beta_L^32, U1 coupling to muons, Eq.(13)"
    },
    {
      "name": "bL33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LEPTOQUARK",
      "order_block": 7,
      "description": "beta_L^33, third-generation left-handed U1 coupling, benchmark 1, Eq.(13)"
    },
    {
      "name": "bR33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LEPTOQUARK",
      "order_block": 8,
      "description": "beta_R^33, third-generation right-handed U1 coupling, Eq.(13)"
    },
    {
      "name": "gZp",
      "parameter_type": "External",
      "value": "3.",
      "block_name": "ZPRIME",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Overall Z' coupling g_Z', Eq.(10)"
    },
    {
      "name": "zq11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "ZPRIME",
      "order_block": 2,
      "description": "zeta_q^ll, Z' coupling to light left-handed quark doublets, Eq.(13)"
    },
    {
      "name": "zq33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 3,
      "description": "zeta_q^33, Z' coupling to the third-generation quark doublet, Eq.(13)"
    },
    {
      "name": "zu11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "ZPRIME",
      "order_block": 4,
      "description": "zeta_u^ll, Z' coupling to light right-handed up quarks, Eq.(13)"
    },
    {
      "name": "zu33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 5,
      "description": "zeta_u^33, Z' coupling to the right-handed top quark, Eq.(13)"
    },
    {
      "name": "zd11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "ZPRIME",
      "order_block": 6,
      "description": "zeta_d^ll, Z' coupling to light right-handed down quarks, Eq.(13)"
    },
    {
      "name": "zd33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 7,
      "description": "zeta_d^33, Z' coupling to the right-handed bottom quark, Eq.(13)"
    },
    {
      "name": "zl22",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 8,
      "description": "zeta_l^22, Z' coupling to the second-generation lepton doublet, Eq.(13)"
    },
    {
      "name": "zl23",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "ZPRIME",
      "order_block": 9,
      "description": "zeta_l^23, lepton-flavour violating Z' coupling (tau-mu), Eq.(13)"
    },
    {
      "name": "zl33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 10,
      "description": "zeta_l^33, Z' coupling to the third-generation lepton doublet, Eq.(13)"
    },
    {
      "name": "ze22",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 11,
      "description": "zeta_e^22, Z' coupling to the right-handed muon, Eq.(13)"
    },
    {
      "name": "ze33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 12,
      "description": "zeta_e^33, Z' coupling to the right-handed tau, Eq.(13)"
    },
    {
      "name": "gGp",
      "parameter_type": "External",
      "value": "3.",
      "block_name": "COLORON",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Overall coloron coupling g_G', Eq.(11)"
    },
    {
      "name": "kGp",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 2,
      "description": "kappa_G', G'-gluon kinetic mixing, set to 0 in the paper, Eq.(11)"
    },
    {
      "name": "kGpt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 3,
      "description": "kappa-tilde_G', non-minimal G'G'G coupling, Eq.(11)"
    },
    {
      "name": "kq11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 4,
      "description": "kappa_q^ll, coloron coupling to light left-handed quark doublets, Eq.(13)"
    },
    {
      "name": "kq33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "COLORON",
      "order_block": 5,
      "description": "kappa_q^33, coloron coupling to the third-generation quark doublet, Eq.(13)"
    },
    {
      "name": "ku11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 6,
      "description": "kappa_u^ll, coloron coupling to light right-handed up quarks, Eq.(13)"
    },
    {
      "name": "ku33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "COLORON",
      "order_block": 7,
      "description": "kappa_u^33, coloron coupling to the right-handed top quark, Eq.(13)"
    },
    {
      "name": "kd11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 8,
      "description": "kappa_d^ll, coloron coupling to light right-handed down quarks, Eq.(13)"
    },
    {
      "name": "kd33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "COLORON",
      "order_block": 9,
      "description": "kappa_d^33, coloron coupling to the right-handed bottom quark, Eq.(13)"
    },
    {
      "name": "betaL",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "betaL[1,1]", "rhs": "0"},
        {"lhs": "betaL[1,2]", "rhs": "0"},
        {"lhs": "betaL[1,3]", "rhs": "bL13"},
        {"lhs": "betaL[2,1]", "rhs": "0"},
        {"lhs": "betaL[2,2]", "rhs": "0"},
        {"lhs": "betaL[2,3]", "rhs": "bL23"},
        {"lhs": "betaL[3,1]", "rhs": "0"},
        {"lhs": "betaL[3,2]", "rhs": "bL32"},
        {"lhs": "betaL[3,3]", "rhs": "bL33"}
      ],
      "description": "Left-handed U1 coupling matrix beta_L, Eq.(1) and Eq.(13)"
    },
    {
      "name": "betaR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "betaR[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "betaR[1,1]", "rhs": "0"},
        {"lhs": "betaR[2,2]", "rhs": "0"},
        {"lhs": "betaR[3,3]", "rhs": "bR33"}
      ],
      "description": "Right-handed U1 coupling matrix beta_R = diag(0,0,beta_R^33), Eq.(13)"
    },
    {
      "name": "zetaq",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "zetaq[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "zetaq[1,1]", "rhs": "zq11"},
        {"lhs": "zetaq[2,2]", "rhs": "zq11"},
        {"lhs": "zetaq[3,3]", "rhs": "zq33"}
      ],
      "description": "Z' coupling matrix to left-handed quark doublets, zeta_q = diag(zll,zll,z33), Eq.(13)"
    },
    {
      "name": "zetau",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "zetau[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "zetau[1,1]", "rhs": "zu11"},
        {"lhs": "zetau[2,2]", "rhs": "zu11"},
        {"lhs": "zetau[3,3]", "rhs": "zu33"}
      ],
      "description": "Z' coupling matrix to right-handed up quarks, Eq.(13)"
    },
    {
      "name": "zetad",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "zetad[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "zetad[1,1]", "rhs": "zd11"},
        {"lhs": "zetad[2,2]", "rhs": "zd11"},
        {"lhs": "zetad[3,3]", "rhs": "zd33"}
      ],
      "description": "Z' coupling matrix to right-handed down quarks, Eq.(13)"
    },
    {
      "name": "zetal",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "zetal[1,1]", "rhs": "0"},
        {"lhs": "zetal[1,2]", "rhs": "0"},
        {"lhs": "zetal[1,3]", "rhs": "0"},
        {"lhs": "zetal[2,1]", "rhs": "0"},
        {"lhs": "zetal[2,2]", "rhs": "zl22"},
        {"lhs": "zetal[2,3]", "rhs": "zl23"},
        {"lhs": "zetal[3,1]", "rhs": "0"},
        {"lhs": "zetal[3,2]", "rhs": "zl23"},
        {"lhs": "zetal[3,3]", "rhs": "zl33"}
      ],
      "description": "Z' coupling matrix to left-handed lepton doublets, Hermitian, Eq.(13)"
    },
    {
      "name": "zetae",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "zetae[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "zetae[1,1]", "rhs": "0"},
        {"lhs": "zetae[2,2]", "rhs": "ze22"},
        {"lhs": "zetae[3,3]", "rhs": "ze33"}
      ],
      "description": "Z' coupling matrix to right-handed charged leptons, zeta_e = diag(0,z22,z33), Eq.(13)"
    },
    {
      "name": "kappaq",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "kappaq[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "kappaq[1,1]", "rhs": "kq11"},
        {"lhs": "kappaq[2,2]", "rhs": "kq11"},
        {"lhs": "kappaq[3,3]", "rhs": "kq33"}
      ],
      "description": "Coloron coupling matrix to left-handed quark doublets, Eq.(13)"
    },
    {
      "name": "kappau",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "kappau[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "kappau[1,1]", "rhs": "ku11"},
        {"lhs": "kappau[2,2]", "rhs": "ku11"},
        {"lhs": "kappau[3,3]", "rhs": "ku33"}
      ],
      "description": "Coloron coupling matrix to right-handed up quarks, Eq.(13)"
    },
    {
      "name": "kappad",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "kappad[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "kappad[1,1]", "rhs": "kd11"},
        {"lhs": "kappad[2,2]", "rhs": "kd11"},
        {"lhs": "kappad[3,3]", "rhs": "kd33"}
      ],
      "description": "Coloron coupling matrix to right-handed down quarks, Eq.(13)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "U1",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MU1", "value": "2000."},
      "width": {"sym": "WU1", "value": "500."},
      "quantum_numbers": {"Q": "2/3", "Y": "2/3", "LeptonNumber": "-1"},
      "pdg": 9000001,
      "particle_name": "U1",
      "antiparticle_name": "U1~",
      "full_name": "Vector leptoquark U1 (3,1,2/3)",
      "propagator_label": "U1",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "3000."},
      "width": {"sym": "WZp", "value": "750."},
      "pdg": 9000002,
      "particle_name": "Zp",
      "full_name": "Colour-singlet Z' (1,1,0)",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 102,
      "class_name": "Gp",
      "self_conjugate": true,
      "indices": ["Gluon"],
      "mass": {"sym": "MGp", "value": "2500."},
      "width": {"sym": "WGp", "value": "625."},
      "pdg": 9000003,
      "particle_name": "Gp",
      "full_name": "Coloron G' (8,1,0)",
      "propagator_label": "Gp",
      "propagator_type": "C",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LU1Kin",
      "delayed": true,
      "expression": "Block[{mu,nu,cc}, ExpandIndices[-1/2 (DC[U1bar[nu,cc],mu] - DC[U1bar[mu,cc],nu]) (DC[U1[nu,cc],mu] - DC[U1[mu,cc],nu]) + MU1^2 U1bar[mu,cc] U1[mu,cc]]]"
    },
    {
      "name": "LU1Gauge",
      "delayed": true,
      "expression": "Block[{mu,nu,aa,c1,c2}, ExpandIndices[-I gs (1 - kU) T[aa,c1,c2] U1bar[mu,c1] U1[nu,c2] FS[G,mu,nu,aa] - I g1 2/3 (1 - kUt) U1bar[mu,c1] U1[nu,c1] FS[B,mu,nu]]]"
    },
    {
      "name": "LU1Int",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ii,ff1,ff2,cc,lag}, lag = ExpandIndices[gU/Sqrt[2] (betaL[ff1,ff2] QLbar[sp1,ii,ff1,cc].Ga[mu,sp1,sp2].LL[sp2,ii,ff2] + betaR[ff1,ff2] dRbar[sp1,ff1,cc].Ga[mu,sp1,sp2].lR[sp2,ff2]) U1[mu,cc], FlavorExpand->SU2D]; lag + HC[lag]]"
    },
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]]"
    },
    {
      "name": "LZpInt",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ii,ff1,ff2,cc}, ExpandIndices[gZp/(2 Sqrt[6]) Zp[mu] (zetaq[ff1,ff2] QLbar[sp1,ii,ff1,cc].Ga[mu,sp1,sp2].QL[sp2,ii,ff2,cc] + zetau[ff1,ff2] uRbar[sp1,ff1,cc].Ga[mu,sp1,sp2].uR[sp2,ff2,cc] + zetad[ff1,ff2] dRbar[sp1,ff1,cc].Ga[mu,sp1,sp2].dR[sp2,ff2,cc] - 3 zetal[ff1,ff2] LLbar[sp1,ii,ff1].Ga[mu,sp1,sp2].LL[sp2,ii,ff2] - 3 zetae[ff1,ff2] lRbar[sp1,ff1].Ga[mu,sp1,sp2].lR[sp2,ff2]), FlavorExpand->SU2D]]"
    },
    {
      "name": "LGpKin",
      "delayed": true,
      "expression": "Block[{mu,nu,aa}, ExpandIndices[-1/4 (DC[Gp[nu,aa],mu] - DC[Gp[mu,aa],nu]) (DC[Gp[nu,aa],mu] - DC[Gp[mu,aa],nu]) + 1/2 MGp^2 Gp[mu,aa] Gp[mu,aa]]]"
    },
    {
      "name": "LGpGauge",
      "delayed": true,
      "expression": "Block[{mu,nu,aa,bb,cc}, ExpandIndices[1/2 kGp (del[Gp[nu,aa],mu] - del[Gp[mu,aa],nu]) FS[G,mu,nu,aa] + gs kGpt f[aa,bb,cc] Gp[mu,aa] Gp[nu,bb] FS[G,mu,nu,cc]]]"
    },
    {
      "name": "LGpInt",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ii,ff1,ff2,aa,c1,c2}, ExpandIndices[gGp Gp[mu,aa] (kappaq[ff1,ff2] T[aa,c1,c2] QLbar[sp1,ii,ff1,c1].Ga[mu,sp1,sp2].QL[sp2,ii,ff2,c2] + kappau[ff1,ff2] T[aa,c1,c2] uRbar[sp1,ff1,c1].Ga[mu,sp1,sp2].uR[sp2,ff2,c2] + kappad[ff1,ff2] T[aa,c1,c2] dRbar[sp1,ff1,c1].Ga[mu,sp1,sp2].dR[sp2,ff2,c2]), FlavorExpand->SU2D]]"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LU1Kin + LU1Gauge + LU1Int + LZpKin + LZpInt + LGpKin + LGpGauge + LGpInt"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LNP"
    }
  ]
}
```
I read the paper and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Model content found in the paper

Section 3, eqs. (9)–(13): three new **massive vectors**, all colour/EW mass eigenstates:

| state | spin | colour | SU(2)L | Y | Q | mass |
|---|---|---|---|---|---|---|
| `U1` vector leptoquark | V | triplet | singlet | 2/3 | 2/3 | `MU1` |
| `Zp` (Z′) | V | singlet | singlet | 0 | 0 | `MZp` |
| `Gp` (coloron G′) | V | octet | singlet | 0 | 0 | `MGp` |

`U1` is complex (`SelfConjugate -> False`); `Zp` and `Gp` are real. The leptoquark mass symbol is `MU1`, not `MU`, because `MU` is already the up-quark mass in `SM.fr`.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling | coupling dim (= 4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L number sum | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LU1Kin | `DC[U1bar]DC[U1]`, `MU1^2 U1bar U1` | 4 | `1`, `MU1^2` | 0 | n/a | −2/3+2/3=0 | −2/3+2/3=0 | singlet×singlet | `cc` shared: 3̄⊗3 | none | 0 | n/a | self-conjugate (real) |
| LU1Gauge | `U1bar U1 FS[G,a]`; `U1bar U1 FS[B]` | 4 | `gs(1−kU)`, `g1 2/3 (1−kUt)` | 0 | n/a | 0 | 0 | singlet | `T[aa,c1,c2]`: 3̄⊗8⊗3 / `c1` shared | none | 0 | n/a | self-Hermitian (F^{μν} antisym.) |
| LU1Int (L) | `U1 QLbar Ga LL` | 4 | `gU betaL` | 0 | n/a | up: −2/3+0+2/3=0; down: +1/3−1+2/3=0 | +1/6−1/2+2/3−1/3… = −1/6−1/2+2/3=0 | shared `ii` (anti-doublet×doublet) | `cc` shared: 3̄⊗3 | none | 0−1+1=0 (U1 has L=−1) | n/a (no ψ^c in paper) | `HC[lag]` |
| LU1Int (R) | `U1 dRbar Ga lR` | 4 | `gU betaR` | 0 | n/a | +1/3−1+2/3=0 | +1/3−1+2/3=0 | all singlets | `cc` shared: 3̄⊗3 | none | 0−1+1=0 | n/a | `HC[lag]` |
| LZpKin | `FS[Zp]^2`, `MZp^2 Zp Zp` | 4 | `1`, `MZp^2` | 0 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field |
| LZpInt | `Zp fbar Ga f` | 4 | `gZp zeta` | 0 | n/a | 0 (vector current) | 0 | shared `ii` per monomial | shared colour per monomial | none | 0 | n/a | Hermitian (ζ Hermitian, Zp real) |
| LGpKin | `DC[Gp]DC[Gp]`, `MGp^2 Gp Gp` | 4 | `1`, `MGp^2` | 0 | n/a | 0 | 0 | singlet | `aa` shared: 8⊗8 | none | 0 | n/a | real field |
| LGpGauge | `del[Gp] FS[G]`; `f Gp Gp FS[G]` | 4 | `kGp`, `gs kGpt` | 0 | n/a | 0 | 0 | singlet | 8⊗8; `f[aa,bb,cc]` | none | 0 | n/a | self-Hermitian |
| LGpInt | `Gp qbar T Ga q` | 4 | `gGp kappa` | 0 | n/a | 0 | 0 | shared `ii` | `T[aa,c1,c2]`: 3̄⊗8⊗3 | none | 0 | n/a | Hermitian (κ real diagonal) |
| U1 free field | kinetic + `MU1` mass present in `LU1Kin`, summed into `LNP` | — | — | — | — | — | — | — | — | — | — | — | ✓ |
| Zp free field | kinetic + `MZp` mass present in `LZpKin`, summed into `LNP` | — | — | — | — | — | — | — | — | — | — | — | ✓ |
| Gp free field | kinetic + `MGp` mass present in `LGpKin`, summed into `LNP` | — | — | — | — | — | — | — | — | — | — | — | ✓ |

`SelfConjugate -> True` classes: `Zp`, `Gp`. Both carry **no** `QuantumNumbers`.

No operator has d > 4, so no EFT cutoff parameter is needed. No charge-conjugated fermion (`ψ^c`) appears in eqs. (9)–(11), so no `CC[...]` is used.

Reference or cached model file read: **none**.

```json
{
  "model_name": "LeptoQuark_gen",
  "info": {
    "authors": ["M. J. Baker", "J. Fuentes-Martin", "G. Isidori", "M. Koenig"],
    "version": "1.0",
    "date": "2019",
    "institutions": ["Physik-Institut, Universitaet Zuerich"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gU",
      "parameter_type": "External",
      "value": "3.",
      "block_name": "LEPTOQUARK",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Overall U1 vector leptoquark coupling, Eq.(9)"
    },
    {
      "name": "kU",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "LEPTOQUARK",
      "order_block": 2,
      "description": "kappa_U, non-minimal U1-gluon coupling, Eq.(9); 0 in gauge models, 1 for minimal coupling"
    },
    {
      "name": "kUt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "LEPTOQUARK",
      "order_block": 3,
      "description": "kappa-tilde_U, non-minimal U1-hypercharge coupling, Eq.(9)"
    },
    {
      "name": "bL13",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "LEPTOQUARK",
      "order_block": 4,
      "description": "beta_L^13, left-handed U1 coupling to first-generation quarks, Eq.(13)"
    },
    {
      "name": "bL23",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "LEPTOQUARK",
      "order_block": 5,
      "description": "beta_L^23, 2-3 quark mixing of the U1, benchmark 0.1, Eq.(14)"
    },
    {
      "name": "bL32",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "LEPTOQUARK",
      "order_block": 6,
      "description": "beta_L^32, U1 coupling to muons, Eq.(13)"
    },
    {
      "name": "bL33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LEPTOQUARK",
      "order_block": 7,
      "description": "beta_L^33, third-generation left-handed U1 coupling, benchmark 1, Eq.(13)"
    },
    {
      "name": "bR33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LEPTOQUARK",
      "order_block": 8,
      "description": "beta_R^33, third-generation right-handed U1 coupling, Eq.(13)"
    },
    {
      "name": "gZp",
      "parameter_type": "External",
      "value": "3.",
      "block_name": "ZPRIME",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Overall Z' coupling g_Z', Eq.(10)"
    },
    {
      "name": "zq11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "ZPRIME",
      "order_block": 2,
      "description": "zeta_q^ll, Z' coupling to light left-handed quark doublets, Eq.(13)"
    },
    {
      "name": "zq33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 3,
      "description": "zeta_q^33, Z' coupling to the third-generation quark doublet, Eq.(13)"
    },
    {
      "name": "zu11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "ZPRIME",
      "order_block": 4,
      "description": "zeta_u^ll, Z' coupling to light right-handed up quarks, Eq.(13)"
    },
    {
      "name": "zu33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 5,
      "description": "zeta_u^33, Z' coupling to the right-handed top quark, Eq.(13)"
    },
    {
      "name": "zd11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "ZPRIME",
      "order_block": 6,
      "description": "zeta_d^ll, Z' coupling to light right-handed down quarks, Eq.(13)"
    },
    {
      "name": "zd33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 7,
      "description": "zeta_d^33, Z' coupling to the right-handed bottom quark, Eq.(13)"
    },
    {
      "name": "zl22",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 8,
      "description": "zeta_l^22, Z' coupling to the second-generation lepton doublet, Eq.(13)"
    },
    {
      "name": "zl23",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "ZPRIME",
      "order_block": 9,
      "description": "zeta_l^23, lepton-flavour violating Z' coupling (tau-mu), Eq.(13)"
    },
    {
      "name": "zl33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 10,
      "description": "zeta_l^33, Z' coupling to the third-generation lepton doublet, Eq.(13)"
    },
    {
      "name": "ze22",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 11,
      "description": "zeta_e^22, Z' coupling to the right-handed muon, Eq.(13)"
    },
    {
      "name": "ze33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 12,
      "description": "zeta_e^33, Z' coupling to the right-handed tau, Eq.(13)"
    },
    {
      "name": "gGp",
      "parameter_type": "External",
      "value": "3.",
      "block_name": "COLORON",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Overall coloron coupling g_G', Eq.(11)"
    },
    {
      "name": "kGp",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 2,
      "description": "kappa_G', G'-gluon kinetic mixing, set to 0 in the paper, Eq.(11)"
    },
    {
      "name": "kGpt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 3,
      "description": "kappa-tilde_G', non-minimal G'G'G coupling, Eq.(11)"
    },
    {
      "name": "kq11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 4,
      "description": "kappa_q^ll, coloron coupling to light left-handed quark doublets, Eq.(13)"
    },
    {
      "name": "kq33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "COLORON",
      "order_block": 5,
      "description": "kappa_q^33, coloron coupling to the third-generation quark doublet, Eq.(13)"
    },
    {
      "name": "ku11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 6,
      "description": "kappa_u^ll, coloron coupling to light right-handed up quarks, Eq.(13)"
    },
    {
      "name": "ku33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "COLORON",
      "order_block": 7,
      "description": "kappa_u^33, coloron coupling to the right-handed top quark, Eq.(13)"
    },
    {
      "name": "kd11",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "COLORON",
      "order_block": 8,
      "description": "kappa_d^ll, coloron coupling to light right-handed down quarks, Eq.(13)"
    },
    {
      "name": "kd33",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "COLORON",
      "order_block": 9,
      "description": "kappa_d^33, coloron coupling to the right-handed bottom quark, Eq.(13)"
    },
    {
      "name": "betaL",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "betaL[1,1]", "rhs": "0"},
        {"lhs": "betaL[1,2]", "rhs": "0"},
        {"lhs": "betaL[1,3]", "rhs": "bL13"},
        {"lhs": "betaL[2,1]", "rhs": "0"},
        {"lhs": "betaL[2,2]", "rhs": "0"},
        {"lhs": "betaL[2,3]", "rhs": "bL23"},
        {"lhs": "betaL[3,1]", "rhs": "0"},
        {"lhs": "betaL[3,2]", "rhs": "bL32"},
        {"lhs": "betaL[3,3]", "rhs": "bL33"}
      ],
      "description": "Left-handed U1 coupling matrix beta_L, Eq.(1) and Eq.(13)"
    },
    {
      "name": "betaR",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "betaR[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "betaR[1,1]", "rhs": "0"},
        {"lhs": "betaR[2,2]", "rhs": "0"},
        {"lhs": "betaR[3,3]", "rhs": "bR33"}
      ],
      "description": "Right-handed U1 coupling matrix beta_R = diag(0,0,beta_R^33), Eq.(13)"
    },
    {
      "name": "zetaq",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "zetaq[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "zetaq[1,1]", "rhs": "zq11"},
        {"lhs": "zetaq[2,2]", "rhs": "zq11"},
        {"lhs": "zetaq[3,3]", "rhs": "zq33"}
      ],
      "description": "Z' coupling matrix to left-handed quark doublets, zeta_q = diag(zll,zll,z33), Eq.(13)"
    },
    {
      "name": "zetau",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "zetau[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "zetau[1,1]", "rhs": "zu11"},
        {"lhs": "zetau[2,2]", "rhs": "zu11"},
        {"lhs": "zetau[3,3]", "rhs": "zu33"}
      ],
      "description": "Z' coupling matrix to right-handed up quarks, Eq.(13)"
    },
    {
      "name": "zetad",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "zetad[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "zetad[1,1]", "rhs": "zd11"},
        {"lhs": "zetad[2,2]", "rhs": "zd11"},
        {"lhs": "zetad[3,3]", "rhs": "zd33"}
      ],
      "description": "Z' coupling matrix to right-handed down quarks, Eq.(13)"
    },
    {
      "name": "zetal",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "zetal[1,1]", "rhs": "0"},
        {"lhs": "zetal[1,2]", "rhs": "0"},
        {"lhs": "zetal[1,3]", "rhs": "0"},
        {"lhs": "zetal[2,1]", "rhs": "0"},
        {"lhs": "zetal[2,2]", "rhs": "zl22"},
        {"lhs": "zetal[2,3]", "rhs": "zl23"},
        {"lhs": "zetal[3,1]", "rhs": "0"},
        {"lhs": "zetal[3,2]", "rhs": "zl23"},
        {"lhs": "zetal[3,3]", "rhs": "zl33"}
      ],
      "description": "Z' coupling matrix to left-handed lepton doublets, Hermitian, Eq.(13)"
    },
    {
      "name": "zetae",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "zetae[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "zetae[1,1]", "rhs": "0"},
        {"lhs": "zetae[2,2]", "rhs": "ze22"},
        {"lhs": "zetae[3,3]", "rhs": "ze33"}
      ],
      "description": "Z' coupling matrix to right-handed charged leptons, zeta_e = diag(0,z22,z33), Eq.(13)"
    },
    {
      "name": "kappaq",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "kappaq[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "kappaq[1,1]", "rhs": "kq11"},
        {"lhs": "kappaq[2,2]", "rhs": "kq11"},
        {"lhs": "kappaq[3,3]", "rhs": "kq33"}
      ],
      "description": "Coloron coupling matrix to left-handed quark doublets, Eq.(13)"
    },
    {
      "name": "kappau",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "kappau[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "kappau[1,1]", "rhs": "ku11"},
        {"lhs": "kappau[2,2]", "rhs": "ku11"},
        {"lhs": "kappau[3,3]", "rhs": "ku33"}
      ],
      "description": "Coloron coupling matrix to right-handed up quarks, Eq.(13)"
    },
    {
      "name": "kappad",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "kappad[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "kappad[1,1]", "rhs": "kd11"},
        {"lhs": "kappad[2,2]", "rhs": "kd11"},
        {"lhs": "kappad[3,3]", "rhs": "kd33"}
      ],
      "description": "Coloron coupling matrix to right-handed down quarks, Eq.(13)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "U1",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MU1", "value": "2000."},
      "width": {"sym": "WU1", "value": "500."},
      "quantum_numbers": {"Q": "2/3", "Y": "2/3", "LeptonNumber": "-1"},
      "pdg": 9000001,
      "particle_name": "U1",
      "antiparticle_name": "U1~",
      "full_name": "Vector leptoquark U1 (3,1,2/3)",
      "propagator_label": "U1",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "3000."},
      "width": {"sym": "WZp", "value": "750."},
      "pdg": 9000002,
      "particle_name": "Zp",
      "full_name": "Colour-singlet Z' (1,1,0)",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 102,
      "class_name": "Gp",
      "self_conjugate": true,
      "indices": ["Gluon"],
      "mass": {"sym": "MGp", "value": "2500."},
      "width": {"sym": "WGp", "value": "625."},
      "pdg": 9000003,
      "particle_name": "Gp",
      "full_name": "Coloron G' (8,1,0)",
      "propagator_label": "Gp",
      "propagator_type": "C",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LU1Kin",
      "delayed": true,
      "expression": "Block[{mu,nu,cc}, ExpandIndices[-1/2 (DC[U1bar[nu,cc],mu] - DC[U1bar[mu,cc],nu]) (DC[U1[nu,cc],mu] - DC[U1[mu,cc],nu]) + MU1^2 U1bar[mu,cc] U1[mu,cc]]]"
    },
    {
      "name": "LU1Gauge",
      "delayed": true,
      "expression": "Block[{mu,nu,aa,c1,c2}, ExpandIndices[-I gs (1 - kU) T[aa,c1,c2] U1bar[mu,c1] U1[nu,c2] FS[G,mu,nu,aa] - I g1 2/3 (1 - kUt) U1bar[mu,c1] U1[nu,c1] FS[B,mu,nu]]]"
    },
    {
      "name": "LU1Int",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ii,ff1,ff2,cc,lag}, lag = ExpandIndices[gU/Sqrt[2] (betaL[ff1,ff2] QLbar[sp1,ii,ff1,cc].Ga[mu,sp1,sp2].LL[sp2,ii,ff2] + betaR[ff1,ff2] dRbar[sp1,ff1,cc].Ga[mu,sp1,sp2].lR[sp2,ff2]) U1[mu,cc], FlavorExpand->SU2D]; lag + HC[lag]]"
    },
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]]"
    },
    {
      "name": "LZpInt",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ii,ff1,ff2,cc}, ExpandIndices[gZp/(2 Sqrt[6]) Zp[mu] (zetaq[ff1,ff2] QLbar[sp1,ii,ff1,cc].Ga[mu,sp1,sp2].QL[sp2,ii,ff2,cc] + zetau[ff1,ff2] uRbar[sp1,ff1,cc].Ga[mu,sp1,sp2].uR[sp2,ff2,cc] + zetad[ff1,ff2] dRbar[sp1,ff1,cc].Ga[mu,sp1,sp2].dR[sp2,ff2,cc] - 3 zetal[ff1,ff2] LLbar[sp1,ii,ff1].Ga[mu,sp1,sp2].LL[sp2,ii,ff2] - 3 zetae[ff1,ff2] lRbar[sp1,ff1].Ga[mu,sp1,sp2].lR[sp2,ff2]), FlavorExpand->SU2D]]"
    },
    {
      "name": "LGpKin",
      "delayed": true,
      "expression": "Block[{mu,nu,aa}, ExpandIndices[-1/4 (DC[Gp[nu,aa],mu] - DC[Gp[mu,aa],nu]) (DC[Gp[nu,aa],mu] - DC[Gp[mu,aa],nu]) + 1/2 MGp^2 Gp[mu,aa] Gp[mu,aa]]]"
    },
    {
      "name": "LGpGauge",
      "delayed": true,
      "expression": "Block[{mu,nu,aa,bb,cc}, ExpandIndices[1/2 kGp (del[Gp[nu,aa],mu] - del[Gp[mu,aa],nu]) FS[G,mu,nu,aa] + gs kGpt f[aa,bb,cc] Gp[mu,aa] Gp[nu,bb] FS[G,mu,nu,cc]]]"
    },
    {
      "name": "LGpInt",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ii,ff1,ff2,aa,c1,c2}, ExpandIndices[gGp Gp[mu,aa] (kappaq[ff1,ff2] T[aa,c1,c2] QLbar[sp1,ii,ff1,c1].Ga[mu,sp1,sp2].QL[sp2,ii,ff2,c2] + kappau[ff1,ff2] T[aa,c1,c2] uRbar[sp1,ff1,c1].Ga[mu,sp1,sp2].uR[sp2,ff2,c2] + kappad[ff1,ff2] T[aa,c1,c2] dRbar[sp1,ff1,c1].Ga[mu,sp1,sp2].dR[sp2,ff2,c2]), FlavorExpand->SU2D]]"
    },
    {
      "name": "LNP",
      "delayed": true,
      "expression": "LU1Kin + LU1Gauge + LU1Int + LZpKin + LZpInt + LGpKin + LGpGauge + LGpInt"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LNP"
    }
  ]
}
```