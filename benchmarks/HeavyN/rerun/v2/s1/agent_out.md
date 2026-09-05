I'll start by reading the paper and the schema.
I read the paper, the schema, and SM.fr. No reference or cached `.fr` file for this model exists in the sandbox, and I opened none.

## Physics summary

The paper adds heavy neutrinos `N` (Eq. 7–9): gauge-singlet Majorana mass eigenstates that mix with the left-handed flavour neutrinos through `V_lN`. The paper keeps one state for its numbers, but Eq. (7) allows `n` heavy states and the MadGraph commands call the particle `n2`, so the implementation carries three states `n1, n2, n3`. All interactions are written in the mass basis (broken phase). The paper states it implements Eq. (9) plus the Goldstone couplings in Feynman gauge; I derive those from the SM.fr conventions (`Phi[1] = -I GP`, `Phi[2] = (vev+H+I G0)/Sqrt[2]`, `vev = 2 MW/gw`).

## Self-audit table

| term | fields | d | coupling | coupling dim (=4-d) | 1/Λ^(d-4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L sum | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNKin (N1,N2,N3) | `Nibar.Ga[mu].del[Ni,mu]`, `Nibar.Ni` | 4 / 3 | 1 / `mNi` | 0 / 1 ✓ | n/a | 0+0=0 ✓ | n/a (gauge singlet, Y=0) | singlet | singlet | none | ΔL=2 by Majorana mass (intended) | n/a (Majorana) | self-conjugate |
| LNW | `W[mu]`, `Nibar`, `l[ff]` | 4 | `gw Conjugate[VNi[ff]]/Sqrt[2]` | 0 ✓ | n/a | +1+0-1=0 ✓ | n/a (mass basis, broken phase) | singlet (physical W) | singlet | none | N carries no L → L violated by design | n/a (N^c = N) | `HC[LNInt]` |
| LNZ | `Z[mu]`, `Nibar`, `vl[ff]` | 4 | `gw Conjugate[VNi[ff]]/(2 cw)` | 0 ✓ | n/a | 0+0+0=0 ✓ | n/a (broken phase) | singlet | singlet | none | same | n/a | `HC[LNInt]` |
| LNH | `H`, `Nibar`, `vl[ff]` | 4 | `gw mNi Conjugate[VNi[ff]]/(2 MW)` | 0 ✓ | n/a | 0 ✓ | n/a (broken phase) | singlet | singlet | none | same | n/a | `HC[LNInt]` |
| LNGP | `GP`, `Nibar`, `l[ff]` | 4 | `gw mNi/(Sqrt[2] MW)`, `gw Ml[ff]/(Sqrt[2] MW)` | 0 ✓ | n/a | +1+0-1=0 ✓ | n/a (broken phase) | singlet | singlet | none | same | n/a | `HC[LNInt]` |
| LNG0 | `G0`, `Nibar`, `vl[ff]` | 4 | `gw mNi Conjugate[VNi[ff]]/(2 MW)` | 0 ✓ | n/a | 0 ✓ | n/a (broken phase) | singlet | singlet | none | same | n/a | `HC[LNInt]` |

Kinetic + mass check: `N1`, `N2`, `N3` each get a Majorana kinetic and mass term in `LNKin`, with the mass symbols `mN1`, `mN2`, `mN3` declared in each class `Mass -> {mNi, 500.}`; `LNKin` enters `LHeavyN`, and `LHeavyN` enters `LTotal`.

`SelfConjugate -> True` classes: `N1`, `N2`, `N3`. None carries `QuantumNumbers` (gauge singlets, Q = 0, Y = 0).

Every operator has d = 4, so no cutoff parameter is needed. Y sums are marked n/a because Eq. (9) is written in the mass basis, where `W`, `Z`, `H`, `GP`, `G0` are not hypercharge eigenstates; electric charge is conserved in every term.

Reference or cached model file read: none.

```json
{
  "model_name": "HeavyN_gen",
  "info": {
    "authors": ["C. Degrande", "O. Mattelaer", "R. Ruiz", "J. Turner"],
    "version": "1.0",
    "date": "12. 09. 2016",
    "institutions": ["Institute for Particle Physics Phenomenology, Durham University"],
    "emails": ["celine.degrande@durham.ac.uk", "o.p.c.mattelaer@durham.ac.uk", "richard.ruiz@durham.ac.uk", "jessica.turner@durham.ac.uk"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "VeN1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 1,
      "tex": "Subscript[V, e N1]",
      "description": "Active-heavy mixing of the electron flavour with N1, Eq.(7)-(9); set to 1 for the bare cross section of Eq.(10)"
    },
    {
      "name": "VeN2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 2,
      "tex": "Subscript[V, e N2]",
      "description": "Active-heavy mixing of the electron flavour with N2, Eq.(7)-(9)"
    },
    {
      "name": "VeN3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 3,
      "tex": "Subscript[V, e N3]",
      "description": "Active-heavy mixing of the electron flavour with N3, Eq.(7)-(9)"
    },
    {
      "name": "VmuN1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 4,
      "tex": "Subscript[V, mu N1]",
      "description": "Active-heavy mixing of the muon flavour with N1, Eq.(7)-(9)"
    },
    {
      "name": "VmuN2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 5,
      "tex": "Subscript[V, mu N2]",
      "description": "Active-heavy mixing of the muon flavour with N2, Eq.(7)-(9)"
    },
    {
      "name": "VmuN3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 6,
      "tex": "Subscript[V, mu N3]",
      "description": "Active-heavy mixing of the muon flavour with N3, Eq.(7)-(9)"
    },
    {
      "name": "VtaN1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 7,
      "tex": "Subscript[V, tau N1]",
      "description": "Active-heavy mixing of the tau flavour with N1, Eq.(7)-(9)"
    },
    {
      "name": "VtaN2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 8,
      "tex": "Subscript[V, tau N2]",
      "description": "Active-heavy mixing of the tau flavour with N2, Eq.(7)-(9)"
    },
    {
      "name": "VtaN3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 9,
      "tex": "Subscript[V, tau N3]",
      "description": "Active-heavy mixing of the tau flavour with N3, Eq.(7)-(9)"
    },
    {
      "name": "VN1",
      "parameter_type": "Internal",
      "complex": false,
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "VN1[1]", "rhs": "VeN1"},
        {"lhs": "VN1[2]", "rhs": "VmuN1"},
        {"lhs": "VN1[3]", "rhs": "VtaN1"}
      ],
      "tex": "Subscript[V, l N1]",
      "description": "Active-heavy mixing vector V_{l N1} of Eq.(8), l = e, mu, tau"
    },
    {
      "name": "VN2",
      "parameter_type": "Internal",
      "complex": false,
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "VN2[1]", "rhs": "VeN2"},
        {"lhs": "VN2[2]", "rhs": "VmuN2"},
        {"lhs": "VN2[3]", "rhs": "VtaN2"}
      ],
      "tex": "Subscript[V, l N2]",
      "description": "Active-heavy mixing vector V_{l N2} of Eq.(8), l = e, mu, tau"
    },
    {
      "name": "VN3",
      "parameter_type": "Internal",
      "complex": false,
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "VN3[1]", "rhs": "VeN3"},
        {"lhs": "VN3[2]", "rhs": "VmuN3"},
        {"lhs": "VN3[3]", "rhs": "VtaN3"}
      ],
      "tex": "Subscript[V, l N3]",
      "description": "Active-heavy mixing vector V_{l N3} of Eq.(8), l = e, mu, tau"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 201,
      "class_name": "N1",
      "self_conjugate": true,
      "mass": {"sym": "mN1", "value": "500."},
      "width": {"sym": "WN1", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9900012,
      "particle_name": "n1",
      "full_name": "Heavy Neutrino 1",
      "propagator_label": "N1",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 202,
      "class_name": "N2",
      "self_conjugate": true,
      "mass": {"sym": "mN2", "value": "500."},
      "width": {"sym": "WN2", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9900014,
      "particle_name": "n2",
      "full_name": "Heavy Neutrino 2",
      "propagator_label": "N2",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 203,
      "class_name": "N3",
      "self_conjugate": true,
      "mass": {"sym": "mN3", "value": "500."},
      "width": {"sym": "WN3", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9900016,
      "particle_name": "n3",
      "full_name": "Heavy Neutrino 3",
      "propagator_label": "N3",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LNKin",
      "delayed": true,
      "expression": "Block[{mu}, I/2 (N1bar.Ga[mu].del[N1, mu] + N2bar.Ga[mu].del[N2, mu] + N3bar.Ga[mu].del[N3, mu]) - 1/2 (mN1 N1bar.N1 + mN2 N2bar.N2 + mN3 N3bar.N3)]"
    },
    {
      "name": "LNW",
      "delayed": true,
      "expression": "Block[{mu, ff}, ExpandIndices[-gw/Sqrt[2] W[mu] (Conjugate[VN1[ff]] N1bar.Ga[mu].ProjM.l[ff] + Conjugate[VN2[ff]] N2bar.Ga[mu].ProjM.l[ff] + Conjugate[VN3[ff]] N3bar.Ga[mu].ProjM.l[ff]), FlavorExpand -> Generation]]"
    },
    {
      "name": "LNZ",
      "delayed": true,
      "expression": "Block[{mu, ff}, ExpandIndices[-gw/(2 cw) Z[mu] (Conjugate[VN1[ff]] N1bar.Ga[mu].ProjM.vl[ff] + Conjugate[VN2[ff]] N2bar.Ga[mu].ProjM.vl[ff] + Conjugate[VN3[ff]] N3bar.Ga[mu].ProjM.vl[ff]), FlavorExpand -> Generation]]"
    },
    {
      "name": "LNH",
      "delayed": true,
      "expression": "Block[{ff}, ExpandIndices[-gw/(2 MW) H (mN1 Conjugate[VN1[ff]] N1bar.ProjM.vl[ff] + mN2 Conjugate[VN2[ff]] N2bar.ProjM.vl[ff] + mN3 Conjugate[VN3[ff]] N3bar.ProjM.vl[ff]), FlavorExpand -> Generation]]"
    },
    {
      "name": "LNGP",
      "delayed": true,
      "expression": "Block[{ff, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {GP | GPbar -> 0}, {}]; ExpandIndices[-I gw/(Sqrt[2] MW) GP (Conjugate[VN1[ff]] (mN1 N1bar.ProjM.l[ff] - Ml[ff] N1bar.ProjP.l[ff]) + Conjugate[VN2[ff]] (mN2 N2bar.ProjM.l[ff] - Ml[ff] N2bar.ProjP.l[ff]) + Conjugate[VN3[ff]] (mN3 N3bar.ProjM.l[ff] - Ml[ff] N3bar.ProjP.l[ff])), FlavorExpand -> Generation] /. feynmangaugerules]"
    },
    {
      "name": "LNG0",
      "delayed": true,
      "expression": "Block[{ff, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0 -> 0}, {}]; ExpandIndices[-I gw/(2 MW) G0 (mN1 Conjugate[VN1[ff]] N1bar.ProjM.vl[ff] + mN2 Conjugate[VN2[ff]] N2bar.ProjM.vl[ff] + mN3 Conjugate[VN3[ff]] N3bar.ProjM.vl[ff]), FlavorExpand -> Generation] /. feynmangaugerules]"
    },
    {
      "name": "LNInt",
      "delayed": true,
      "expression": "LNW + LNZ + LNH + LNGP + LNG0"
    },
    {
      "name": "LHeavyN",
      "delayed": true,
      "expression": "LNKin + LNInt + HC[LNInt]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LHeavyN"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper, the schema, and SM.fr. No reference or cached `.fr` file for this model exists in the sandbox, and I opened none.

## Physics summary

The paper adds heavy neutrinos `N` (Eq. 7–9): gauge-singlet Majorana mass eigenstates that mix with the left-handed flavour neutrinos through `V_lN`. The paper keeps one state for its numbers, but Eq. (7) allows `n` heavy states and the MadGraph commands call the particle `n2`, so the implementation carries three states `n1, n2, n3`. All interactions are written in the mass basis (broken phase). The paper states it implements Eq. (9) plus the Goldstone couplings in Feynman gauge; I derive those from the SM.fr conventions (`Phi[1] = -I GP`, `Phi[2] = (vev+H+I G0)/Sqrt[2]`, `vev = 2 MW/gw`).

## Self-audit table

| term | fields | d | coupling | coupling dim (=4-d) | 1/Λ^(d-4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L sum | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNKin (N1,N2,N3) | `Nibar.Ga[mu].del[Ni,mu]`, `Nibar.Ni` | 4 / 3 | 1 / `mNi` | 0 / 1 ✓ | n/a | 0+0=0 ✓ | n/a (gauge singlet, Y=0) | singlet | singlet | none | ΔL=2 by Majorana mass (intended) | n/a (Majorana) | self-conjugate |
| LNW | `W[mu]`, `Nibar`, `l[ff]` | 4 | `gw Conjugate[VNi[ff]]/Sqrt[2]` | 0 ✓ | n/a | +1+0-1=0 ✓ | n/a (mass basis, broken phase) | singlet (physical W) | singlet | none | N carries no L → L violated by design | n/a (N^c = N) | `HC[LNInt]` |
| LNZ | `Z[mu]`, `Nibar`, `vl[ff]` | 4 | `gw Conjugate[VNi[ff]]/(2 cw)` | 0 ✓ | n/a | 0+0+0=0 ✓ | n/a (broken phase) | singlet | singlet | none | same | n/a | `HC[LNInt]` |
| LNH | `H`, `Nibar`, `vl[ff]` | 4 | `gw mNi Conjugate[VNi[ff]]/(2 MW)` | 0 ✓ | n/a | 0 ✓ | n/a (broken phase) | singlet | singlet | none | same | n/a | `HC[LNInt]` |
| LNGP | `GP`, `Nibar`, `l[ff]` | 4 | `gw mNi/(Sqrt[2] MW)`, `gw Ml[ff]/(Sqrt[2] MW)` | 0 ✓ | n/a | +1+0-1=0 ✓ | n/a (broken phase) | singlet | singlet | none | same | n/a | `HC[LNInt]` |
| LNG0 | `G0`, `Nibar`, `vl[ff]` | 4 | `gw mNi Conjugate[VNi[ff]]/(2 MW)` | 0 ✓ | n/a | 0 ✓ | n/a (broken phase) | singlet | singlet | none | same | n/a | `HC[LNInt]` |

Kinetic + mass check: `N1`, `N2`, `N3` each get a Majorana kinetic and mass term in `LNKin`, with the mass symbols `mN1`, `mN2`, `mN3` declared in each class `Mass -> {mNi, 500.}`; `LNKin` enters `LHeavyN`, and `LHeavyN` enters `LTotal`.

`SelfConjugate -> True` classes: `N1`, `N2`, `N3`. None carries `QuantumNumbers` (gauge singlets, Q = 0, Y = 0).

Every operator has d = 4, so no cutoff parameter is needed. Y sums are marked n/a because Eq. (9) is written in the mass basis, where `W`, `Z`, `H`, `GP`, `G0` are not hypercharge eigenstates; electric charge is conserved in every term.

Reference or cached model file read: none.

```json
{
  "model_name": "HeavyN_gen",
  "info": {
    "authors": ["C. Degrande", "O. Mattelaer", "R. Ruiz", "J. Turner"],
    "version": "1.0",
    "date": "12. 09. 2016",
    "institutions": ["Institute for Particle Physics Phenomenology, Durham University"],
    "emails": ["celine.degrande@durham.ac.uk", "o.p.c.mattelaer@durham.ac.uk", "richard.ruiz@durham.ac.uk", "jessica.turner@durham.ac.uk"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "VeN1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 1,
      "tex": "Subscript[V, e N1]",
      "description": "Active-heavy mixing of the electron flavour with N1, Eq.(7)-(9); set to 1 for the bare cross section of Eq.(10)"
    },
    {
      "name": "VeN2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 2,
      "tex": "Subscript[V, e N2]",
      "description": "Active-heavy mixing of the electron flavour with N2, Eq.(7)-(9)"
    },
    {
      "name": "VeN3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 3,
      "tex": "Subscript[V, e N3]",
      "description": "Active-heavy mixing of the electron flavour with N3, Eq.(7)-(9)"
    },
    {
      "name": "VmuN1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 4,
      "tex": "Subscript[V, mu N1]",
      "description": "Active-heavy mixing of the muon flavour with N1, Eq.(7)-(9)"
    },
    {
      "name": "VmuN2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 5,
      "tex": "Subscript[V, mu N2]",
      "description": "Active-heavy mixing of the muon flavour with N2, Eq.(7)-(9)"
    },
    {
      "name": "VmuN3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 6,
      "tex": "Subscript[V, mu N3]",
      "description": "Active-heavy mixing of the muon flavour with N3, Eq.(7)-(9)"
    },
    {
      "name": "VtaN1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 7,
      "tex": "Subscript[V, tau N1]",
      "description": "Active-heavy mixing of the tau flavour with N1, Eq.(7)-(9)"
    },
    {
      "name": "VtaN2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 8,
      "tex": "Subscript[V, tau N2]",
      "description": "Active-heavy mixing of the tau flavour with N2, Eq.(7)-(9)"
    },
    {
      "name": "VtaN3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NUMIXING",
      "order_block": 9,
      "tex": "Subscript[V, tau N3]",
      "description": "Active-heavy mixing of the tau flavour with N3, Eq.(7)-(9)"
    },
    {
      "name": "VN1",
      "parameter_type": "Internal",
      "complex": false,
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "VN1[1]", "rhs": "VeN1"},
        {"lhs": "VN1[2]", "rhs": "VmuN1"},
        {"lhs": "VN1[3]", "rhs": "VtaN1"}
      ],
      "tex": "Subscript[V, l N1]",
      "description": "Active-heavy mixing vector V_{l N1} of Eq.(8), l = e, mu, tau"
    },
    {
      "name": "VN2",
      "parameter_type": "Internal",
      "complex": false,
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "VN2[1]", "rhs": "VeN2"},
        {"lhs": "VN2[2]", "rhs": "VmuN2"},
        {"lhs": "VN2[3]", "rhs": "VtaN2"}
      ],
      "tex": "Subscript[V, l N2]",
      "description": "Active-heavy mixing vector V_{l N2} of Eq.(8), l = e, mu, tau"
    },
    {
      "name": "VN3",
      "parameter_type": "Internal",
      "complex": false,
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "VN3[1]", "rhs": "VeN3"},
        {"lhs": "VN3[2]", "rhs": "VmuN3"},
        {"lhs": "VN3[3]", "rhs": "VtaN3"}
      ],
      "tex": "Subscript[V, l N3]",
      "description": "Active-heavy mixing vector V_{l N3} of Eq.(8), l = e, mu, tau"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 201,
      "class_name": "N1",
      "self_conjugate": true,
      "mass": {"sym": "mN1", "value": "500."},
      "width": {"sym": "WN1", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9900012,
      "particle_name": "n1",
      "full_name": "Heavy Neutrino 1",
      "propagator_label": "N1",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 202,
      "class_name": "N2",
      "self_conjugate": true,
      "mass": {"sym": "mN2", "value": "500."},
      "width": {"sym": "WN2", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9900014,
      "particle_name": "n2",
      "full_name": "Heavy Neutrino 2",
      "propagator_label": "N2",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 203,
      "class_name": "N3",
      "self_conjugate": true,
      "mass": {"sym": "mN3", "value": "500."},
      "width": {"sym": "WN3", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9900016,
      "particle_name": "n3",
      "full_name": "Heavy Neutrino 3",
      "propagator_label": "N3",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LNKin",
      "delayed": true,
      "expression": "Block[{mu}, I/2 (N1bar.Ga[mu].del[N1, mu] + N2bar.Ga[mu].del[N2, mu] + N3bar.Ga[mu].del[N3, mu]) - 1/2 (mN1 N1bar.N1 + mN2 N2bar.N2 + mN3 N3bar.N3)]"
    },
    {
      "name": "LNW",
      "delayed": true,
      "expression": "Block[{mu, ff}, ExpandIndices[-gw/Sqrt[2] W[mu] (Conjugate[VN1[ff]] N1bar.Ga[mu].ProjM.l[ff] + Conjugate[VN2[ff]] N2bar.Ga[mu].ProjM.l[ff] + Conjugate[VN3[ff]] N3bar.Ga[mu].ProjM.l[ff]), FlavorExpand -> Generation]]"
    },
    {
      "name": "LNZ",
      "delayed": true,
      "expression": "Block[{mu, ff}, ExpandIndices[-gw/(2 cw) Z[mu] (Conjugate[VN1[ff]] N1bar.Ga[mu].ProjM.vl[ff] + Conjugate[VN2[ff]] N2bar.Ga[mu].ProjM.vl[ff] + Conjugate[VN3[ff]] N3bar.Ga[mu].ProjM.vl[ff]), FlavorExpand -> Generation]]"
    },
    {
      "name": "LNH",
      "delayed": true,
      "expression": "Block[{ff}, ExpandIndices[-gw/(2 MW) H (mN1 Conjugate[VN1[ff]] N1bar.ProjM.vl[ff] + mN2 Conjugate[VN2[ff]] N2bar.ProjM.vl[ff] + mN3 Conjugate[VN3[ff]] N3bar.ProjM.vl[ff]), FlavorExpand -> Generation]]"
    },
    {
      "name": "LNGP",
      "delayed": true,
      "expression": "Block[{ff, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {GP | GPbar -> 0}, {}]; ExpandIndices[-I gw/(Sqrt[2] MW) GP (Conjugate[VN1[ff]] (mN1 N1bar.ProjM.l[ff] - Ml[ff] N1bar.ProjP.l[ff]) + Conjugate[VN2[ff]] (mN2 N2bar.ProjM.l[ff] - Ml[ff] N2bar.ProjP.l[ff]) + Conjugate[VN3[ff]] (mN3 N3bar.ProjM.l[ff] - Ml[ff] N3bar.ProjP.l[ff])), FlavorExpand -> Generation] /. feynmangaugerules]"
    },
    {
      "name": "LNG0",
      "delayed": true,
      "expression": "Block[{ff, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0 -> 0}, {}]; ExpandIndices[-I gw/(2 MW) G0 (mN1 Conjugate[VN1[ff]] N1bar.ProjM.vl[ff] + mN2 Conjugate[VN2[ff]] N2bar.ProjM.vl[ff] + mN3 Conjugate[VN3[ff]] N3bar.ProjM.vl[ff]), FlavorExpand -> Generation] /. feynmangaugerules]"
    },
    {
      "name": "LNInt",
      "delayed": true,
      "expression": "LNW + LNZ + LNH + LNGP + LNG0"
    },
    {
      "name": "LHeavyN",
      "delayed": true,
      "expression": "LNKin + LNInt + HC[LNInt]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LHeavyN"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```