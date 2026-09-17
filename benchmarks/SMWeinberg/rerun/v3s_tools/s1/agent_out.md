## Self-audit table

Index convention taken from SM.fr: Generation 1=e, 2=mu, 3=tau. New particle class index NM uses class_index 101 (>=100, per naming rule). "N" is a Mathematica built-in, so the new Majorana state is named `NM` (bar-field auto-named `NMbar`), matching paper Table III's physics but avoiding the forbidden symbol.

| term name | fields in monomial | dim d | coupling | coupling dim (4-d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) | new-U(1) sum | L/B sum | CC[] used | fraction/root check | HC partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LNkin | NMbar,NM,del | 4 (kin) / 3 (mass, coeff mN dim1) | 1 / mN | 0 / 1 | n/a | 0 | n/a | singlet, trivial | singlet | n/a | ΔL=2 (Majorana mass, expected) | n/a | n/a | self-conjugate, real |
| LNCC | W,NMbar,l | 4 | gw/√2 | 0 | n/a | 1+0-1=0 | n/a (post-EWSB basis) | component coupling (post-EWSB); charge-current structure of Atre et al. 2009 phen. Type-I seesaw, cited by paper | singlet | n/a | ΔL=1 per vertex, cancelled by HC | n/a | verbatim, no frac/root | HC[LNCC] included in term |
| LNNC | Z,NMbar,vl | 4 | gw/(2cw) | 0 | n/a | 0 | n/a | as above | singlet | n/a | ΔL=1, cancelled by HC | n/a | n/a | HC included |
| LNH | H,NMbar,vl (+ H² piece, d=5) | 4 / 5 | gwmN/(2MW) / gw²mN/(8MW²) | 0 / -1 | n/a (4) / d-4=1 but expressed via MW, not Lambda (see note) | 0 | n/a | as above | singlet | n/a | ΔL=1, cancelled by HC | n/a | Sqrt[2] placement checked against main-text Eq. dim5Lag normalization | HC included |
| LNGP | GP,(NMbar.l or bar[CC[l]].NM), (+GP·H piece d=5) | 4 / 5 | gwmN/(2√2 MW) / gw²mN/(4√2 MW²) | 0 / -1 | see note | 1+0-1=0 | n/a | as above | singlet | n/a | ΔL=0 (mixed N-l current) | yes (bar[CC[l]]) | Sqrt[2] from doublet contraction Eq.(A2)-(A3), checked | HC included |
| LNG0 | G0,NMbar,vl (+G0·H, d=5) | 4/5 | gwmN/(2MW) / gw²mN/(4MW²) | 0/-1 | see note | 0 | n/a | as above | singlet | n/a | ΔL=1, cancelled by HC | n/a | n/a | HC included |
| LNGPGP | GP,GP,bar[CC[l]],l' | 5 | gw²mN/(4MW²) | -1 | see note | 1+1-1-1=0 (same-sign ℓ+ℓ'+ production, Fig.1) | n/a | as above | singlet | n/a | ΔL=2 per vertex (Majorana/LNV, expected) | yes (bar[CC[l]]) | factor "2" from paper's "2G+G+" absorbed into coefficient, checked against Eq. after (355) | HC included |
| LNG0G0 | G0,G0,NMbar,vl | 5 | gw²mN/(8MW²) | -1 | see note | 0 | n/a | as above | singlet | n/a | ΔL=1, cancelled by HC | n/a | n/a | HC included |
| LNG0GP | G0,GP,(NMbar.l or bar[CC[l]].NM) | 5 | gw²mN/(4√2MW²) | -1 | see note | 0 | n/a | as above | singlet | n/a | ΔL=0/1 mixed, cancelled by HC | yes | Sqrt[2] checked against Eq.(A2)-(A3) | HC included |

Note on "1/Lambda power": the paper's own UFO (Appendix, Table III) trades the explicit `C5/Lambda` coefficient for the internally-computed mass `mN` (Eq. 9), so every d>4 term above is written with the extra Higgs/Goldstone field(s) suppressed by `1/MW` powers, not by an explicit `1/Lambda` factor — dimensional counting still closes (coefficient dim = 4-d) because `mN` (dim 1) and `MW` (dim 1) are both already-dimensionful parameters. `Lambda` itself appears nowhere in a Lagrangian term; it enters only inside the Internal parameter `mN`'s formula. This matches the paper's explicit statement that it extends the SM "by a single Majorana neutrino N with mass m_N ... governed by Eq. (lagCC)" and Table III listing only `Lambda`, `Cll` (inputs) and `mN`, `wN` (derived).

Per-particle kinetic+mass check: NM (F[101]) has a named free-field term `LNkin` (Majorana form `I/2 NMbar.Ga[mu].del[NM,mu] - 1/2 mN NMbar.NM`), included in `LWeinberg` → `LTotal`. Confirmed.

Non-fundamental colour representations: none used (NM is a colour singlet) — no `AddGaugeRepresentation[...]` needed.

SelfConjugate -> True classes: `NM` only; it carries no `QuantumNumbers` (Q, Y both physically zero and omitted from the class entry).

Name check: new symbols `NM`, `NMbar` (auto), `Lambda`, `Cll`, `mN`, `wN`. None is a Mathematica built-in or FeynRules symbol (`N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM` all avoided — in particular the paper's own name "N" was renamed to `NM` for this reason), and none collides with an SM.fr name (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,l,vl,...`).

Single total: `LTotal := LSM + LWeinberg`, where `LWeinberg := LNkin + LNCC + LNNC + LNH + LNGP + LNG0 + LNGPGP + LNG0G0 + LNG0GP`. Every term defined in this model appears in that sum.

Reference/cached model file read: none.

```json
{
  "model_name": "SMWeinberg_gen",
  "info": {
    "authors": ["Benjamin Fuks", "Jonas Neundorf", "Krisztian Peters", "Richard Ruiz", "Matthias Saimpert"],
    "version": "1.0",
    "date": "17. 09. 2026",
    "institutions": ["LPTHE Paris", "DESY Hamburg", "IFJ PAN Krakow", "CERN"],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Lambda",
      "parameter_type": "External",
      "value": "200000.",
      "value_rules": [],
      "complex": false,
      "block_name": "NUPHYSICS",
      "order_block": 1,
      "interaction_order": null,
      "indices": [],
      "definitions": [],
      "description": "Weinberg-operator scale Lambda, GeV. Benchmark Lambda = 200 TeV used throughout the paper's main LHC sensitivity study (Eq. 9, Table III)."
    },
    {
      "name": "Cll",
      "parameter_type": "External",
      "value": null,
      "value_rules": [
        {"lhs": "Cll[1,1]", "rhs": "0.", "delayed": false},
        {"lhs": "Cll[1,2]", "rhs": "0.", "delayed": false},
        {"lhs": "Cll[1,3]", "rhs": "0.", "delayed": false},
        {"lhs": "Cll[2,1]", "rhs": "0.", "delayed": false},
        {"lhs": "Cll[2,2]", "rhs": "1.", "delayed": false},
        {"lhs": "Cll[2,3]", "rhs": "0.", "delayed": false},
        {"lhs": "Cll[3,1]", "rhs": "0.", "delayed": false},
        {"lhs": "Cll[3,2]", "rhs": "0.", "delayed": false},
        {"lhs": "Cll[3,3]", "rhs": "0.", "delayed": false}
      ],
      "complex": false,
      "block_name": "NUPHYSICS",
      "interaction_order": null,
      "indices": ["Generation", "Generation"],
      "definitions": [],
      "description": "Weinberg-operator Wilson coefficient C5^{ll'} in the lepton flavor basis (symmetric 3x3, dimensionless). Benchmark C5^{ll'} = delta_{l,mu} delta_{l',mu} (Eqs. 1-2 and Fig. 2 caption): only the mu-mu entry is nonzero."
    },
    {
      "name": "mN",
      "parameter_type": "Internal",
      "value": "Abs[Cll[1,1] + Cll[1,2] + Cll[1,3] + Cll[2,2] + Cll[2,3] + Cll[3,3]] * vev^2 / Lambda",
      "value_rules": [],
      "complex": null,
      "block_name": null,
      "interaction_order": null,
      "indices": [],
      "definitions": [],
      "description": "Mass of the unphysical Majorana neutrino NM that models the d=5 Weinberg operator: mN = |sum_{l<=l'} C5^{ll'}| v^2 / Lambda (Eq. 9)."
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "NM",
      "self_conjugate": true,
      "indices": [],
      "flavor_index": null,
      "class_members": [],
      "mass": {"massless": false, "sym": "mN", "value": "Internal", "members": []},
      "width": {"massless": false, "sym": "wN", "value": "Automatic", "members": []},
      "quantum_numbers": {},
      "pdg": 9900012,
      "particle_name": "n9",
      "antiparticle_name": null,
      "full_name": "Unphysical Majorana neutrino (Weinberg-operator dim-5 realization)",
      "propagator_label": "n9",
      "propagator_type": "Straight",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": [],
      "ghost": null,
      "goldstone": null,
      "weyl_components": [],
      "majorana_phase": null,
      "chirality": null
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LNkin",
      "expression": "Block[{mu}, ExpandIndices[I/2 NMbar.Ga[mu].del[NM,mu] - 1/2 mN NMbar.NM]]",
      "delayed": true
    },
    {
      "name": "LNCC",
      "expression": "Block[{mu, expr}, expr = ExpandIndices[-(gw/Sqrt[2]) W[mu] NMbar.Ga[mu].ProjM.l, FlavorExpand -> Generation]; expr + HC[expr]]",
      "delayed": true
    },
    {
      "name": "LNNC",
      "expression": "Block[{mu, expr}, expr = ExpandIndices[-(gw/(2 cw)) Z[mu] NMbar.Ga[mu].ProjM.vl, FlavorExpand -> Generation]; expr + HC[expr]]",
      "delayed": true
    },
    {
      "name": "LNH",
      "expression": "Block[{expr}, expr = ExpandIndices[-(gw mN/(2 MW)) H (1 + (gw/(4 MW)) H) NMbar.ProjM.vl, FlavorExpand -> Generation]; expr + HC[expr]]",
      "delayed": true
    },
    {
      "name": "LNGP",
      "expression": "Block[{expr}, expr = ExpandIndices[-I (gw mN/(2 Sqrt[2] MW)) GP (1 + (gw/(2 MW)) H) (NMbar.ProjM.l + bar[CC[l]].ProjM.NM), FlavorExpand -> Generation]; expr + HC[expr]]",
      "delayed": true
    },
    {
      "name": "LNG0",
      "expression": "Block[{expr}, expr = ExpandIndices[-I (gw mN/(2 MW)) G0 (1 + (gw/(2 MW)) H) NMbar.ProjM.vl, FlavorExpand -> Generation]; expr + HC[expr]]",
      "delayed": true
    },
    {
      "name": "LNGPGP",
      "expression": "Block[{ff1, ff2, expr}, expr = ExpandIndices[(gw^2 mN/(4 MW^2)) GP GP bar[CC[l[ff1]]].ProjM.l[ff2], FlavorExpand -> Generation]; expr + HC[expr]]",
      "delayed": true
    },
    {
      "name": "LNG0G0",
      "expression": "Block[{expr}, expr = ExpandIndices[(gw^2 mN/(8 MW^2)) G0 G0 NMbar.ProjM.vl, FlavorExpand -> Generation]; expr + HC[expr]]",
      "delayed": true
    },
    {
      "name": "LNG0GP",
      "expression": "Block[{expr}, expr = ExpandIndices[(gw^2 mN/(4 Sqrt[2] MW^2)) G0 GP (NMbar.ProjM.l + bar[CC[l]].ProjM.NM), FlavorExpand -> Generation]; expr + HC[expr]]",
      "delayed": true
    },
    {
      "name": "LWeinberg",
      "expression": "LNkin + LNCC + LNNC + LNH + LNGP + LNG0 + LNGPGP + LNG0G0 + LNG0GP",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LWeinberg",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```