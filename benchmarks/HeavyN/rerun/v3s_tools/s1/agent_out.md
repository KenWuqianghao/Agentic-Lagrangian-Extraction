## Self-audit table

Paper equation used: Eq. (5) (`\label{eq:Lagrangian}`, LaTeX source lines 222–230). Per the paper's own simplification ("we consider only one heavy mass eigenstate, labeled by N", line 220), the new physics content is exactly one heavy Majorana neutrino `Nmaj` (SM-gauge singlet) plus the three active-heavy mixings `VlN[1..3]` (e, mu, tau). No cached or reference `.fr` file was read — only the paper text and `SM.fr` were consulted.

| term name | fields in monomial | d | coupling symbol | coupling dim (4-d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new U(1) sums | L/B sum | CC[] used | frac/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LNmajKin` | `Nmajbar, del, Nmaj` (kin, d=4); `Nmajbar, Nmaj` (mass, d=3) | 4 / 3 | `I/2` ; `MN` | 0 ; 1 | n/a (d≤4) | 0 (singlet) | n/a (singlet, mass-basis) | n/a (SM-singlet) | n/a (colour singlet) | n/a (no new U(1)) | Majorana mass explicitly breaks L by 2 (expected) | n/a (bare Majorana term) | n/a (no fraction) | self-conjugate, automatically Hermitian |
| `LNCC` | `W, bar[CC[Nmaj]], l` | 4 | `gw·VlN` | 0 | n/a | +1(W)+0(N)+(-1)(l)=0 | n/a (broken-phase mass basis, only Q exact) | n/a | n/a | n/a | conserved if L(N)≡1 by convention | yes | `g/Sqrt[2]`, LaTeX line 224 `\frac{g}{\sqrt2}`, literal | `HC[ccterm]` in expression |
| `LNNC` | `Z, bar[CC[Nmaj]], vl` | 4 | `gw/(2 cw)·VlN` | 0 | n/a | 0+0+0=0 | n/a | n/a | n/a | n/a | conserved (both N, ν assigned L=1) | yes | `g/(2 cosθ_W)`, LaTeX line 226, literal | `HC[ncterm]` in expression |
| `LNH` | `H, bar[CC[Nmaj]], vl` | 4 | `gw·MN/(2 MW)·VlN` | 0 | n/a | 0 | n/a | n/a | n/a | n/a | conserved | yes | `g mN/(2 MW)`, LaTeX line 228, literal | `HC[hterm]` in expression |

- SelfConjugate→True classes: `Nmaj` only — carries no `QuantumNumbers` (confirmed empty).
- Name check: `Nmaj`, `VlN`, `MN`, `WN` — none is a Mathematica built-in, FeynRules symbol, or `SM.fr` name (avoided the literal built-in `N`).
- Single total Lagrangian: `LTotal := LNmajKin + LNCC + LNNC + LNH` (all four terms appear).
- Reference/cached model file read: none.

```json
{
  "model_name": "HeavyN_gen",
  "info": {
    "authors": ["C. Degrande", "O. Mattelaer", "R. Ruiz", "J. Turner"],
    "version": "1.0",
    "date": "2016-02-22",
    "institutions": ["Institute for Particle Physics Phenomenology, Durham University"],
    "emails": ["celine.degrande@durham.ac.uk", "o.p.c.mattelaer@durham.ac.uk", "richard.ruiz@durham.ac.uk", "jessica.turner@durham.ac.uk"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "VlN",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {"lhs": "VlN[1]", "rhs": "1.", "delayed": false},
        {"lhs": "VlN[2]", "rhs": "1.", "delayed": false},
        {"lhs": "VlN[3]", "rhs": "1.", "delayed": false}
      ],
      "complex": null,
      "block_name": "NPINPUTS",
      "order_block": null,
      "interaction_order": ["NP", 1],
      "indices": ["Generation"],
      "definitions": [],
      "parameter_name": null,
      "tex": "Subscript[V,lN]",
      "description": "Active-heavy neutrino mixing V_{lN} (e,mu,tau), Eq.(5). Declared real (paper's V*_{lN} phase absorbed); default =1 matches the paper's model-independent bare normalization |V_{lN}|=1 used to define sigma_0.",
      "tensor_class": null,
      "unitary": null,
      "hermitian": null,
      "orthogonal": null,
      "allow_summation": null
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "Nmaj",
      "self_conjugate": true,
      "indices": [],
      "flavor_index": null,
      "class_members": [],
      "mass": {"massless": false, "sym": "MN", "value": "500.", "members": []},
      "width": {"massless": false, "sym": "WN", "value": "Automatic", "members": []},
      "quantum_numbers": {},
      "pdg": 9900012,
      "particle_name": "n2",
      "antiparticle_name": null,
      "full_name": "Heavy Majorana neutrino",
      "propagator_label": "n2",
      "propagator_type": "S",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": "1",
      "chirality": null
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LNmajKin",
      "expression": "Block[{mu}, ExpandIndices[I/2 Nmajbar.Ga[mu].del[Nmaj,mu] - 1/2 MN Nmajbar.Nmaj]]",
      "delayed": true
    },
    {
      "name": "LNCC",
      "expression": "Block[{mu, ll, ccterm}, ccterm = ExpandIndices[-(gw/Sqrt[2]) W[mu] bar[CC[Nmaj]].Ga[mu].ProjM.l[ll] Conjugate[VlN[ll]]]; ccterm + HC[ccterm]]",
      "delayed": true
    },
    {
      "name": "LNNC",
      "expression": "Block[{mu, ll, ncterm}, ncterm = ExpandIndices[-(gw/(2 cw)) Z[mu] bar[CC[Nmaj]].Ga[mu].ProjM.vl[ll] Conjugate[VlN[ll]]]; ncterm + HC[ncterm]]",
      "delayed": true
    },
    {
      "name": "LNH",
      "expression": "Block[{ll, hterm}, hterm = ExpandIndices[-(gw MN/(2 MW)) H bar[CC[Nmaj]].ProjM.vl[ll] Conjugate[VlN[ll]]]; hterm + HC[hterm]]",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LNmajKin + LNCC + LNNC + LNH",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```