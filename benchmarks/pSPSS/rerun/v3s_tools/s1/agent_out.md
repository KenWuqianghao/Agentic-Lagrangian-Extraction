## Self-audit table

Read: paper LaTeX source `2210.10738_source.tex` (Sec. 2.3–2.4 for the pSPSS physics, Sec. 3.1 "FeynRules model file" for the literal field/parameter names and Mathematica snippets), `frmodel.py` (schema), `SM.fr` (base-model conventions: `vev` ≈246 GeV Internal, `Phi[2]=(vev+H+I G0)/Sqrt[2]`, `LL` Y=-1/2, `Generation`/`SU2D` built-in indices).

New physical content (per paper Sec. 3.1): exactly two new propagating states, the pseudo-Dirac heavy Majorana mass eigenstates `n4`, `n5` (paper's own physical fields). The paper's presentational device `N1L`,`N2L` (interaction eigenstates) and the mixing matrix `Un`/`UnCL` are folded directly into declaring `n4`,`n5` as the fundamental self-conjugate Majorana fields with masses computed from the paper's closed-form splitting formula, and coupling them to the SM lepton doublet with the paper's own LO mixing coefficients (`∓i/√2`, `1/√2`) from the (LO) mixing matrix. `PhiNP`/`vevNP` are kept exactly as the paper describes (an `{NP,-1}`-tagged bookkeeping copy of `Phi`/`vev`, used only for MadGraph power counting).

| term | fields | dim d | coupling | coupling dim | 1/Λ | Q sum | Y sum | SU(2) | SU(3) | new-U(1) | L/B sum | CC[] | frac/root check | HC partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `Ln4` | n4bar, Ga, del, n4 (kinetic) | 4 | i/2 | 0 | n/a | 0 | 0 | singlet | n/a | n/a | n/a (Majorana) | n/a | n/a | self-conj. |
| `Ln4` | n4bar, n4 (mass) | 3 | MN4 | 1 | n/a | 0 | 0 | singlet | n/a | n/a | n/a | n/a | Eq.(3.13)/`eq:Delta m mass splitting`, LaTeX `\frac12` confirmed | self-conj. |
| `Ln5` | (same, n5/MN5) | 4/3 | i/2, MN5 | 0/1 | n/a | 0 | 0 | singlet | n/a | n/a | n/a | n/a | same eq. | self-conj. |
| `LNPYuk` | CC[n4bar], LL, PhiNPbar, Eps | 4 | yn4[ff] | 0 | n/a | 0 (SU(2) gauge inv. of Yukawa) | see note* | Eps[ii,jj] contraction of LL's ii with PhiNPbar's jj, verbatim structure of paper's quoted `CC[N1Lbar].LL[...] PhiNPbar[jj] Eps[ii,jj]` (Sec. 3.1) | n/a | n/a | ΔL=1 per channel (LNV by construction — this *is* the paper's physics) | yes, `CC[n4bar]` for `N1^c`-type field | LO mixing coeff. `-i/Sqrt[2]`, `1/Sqrt[2]` from Eq. `eq:neutrino diagonlisation`/`eq:active-sterile mixing` (2.14/2.19), paper states LO suffices | `HC[LNPYuk]` |
| `LNPYuk` (n5 channel) | CC[n5bar], LL, PhiNPbar, Eps | 4 | yn5[ff] | 0 | n/a | 0 | see note* | same | n/a | n/a | ΔL=1 | yes | same | `HC[LNPYuk]` |

\* **Y-sum caveat (flagged explicitly, not silently resolved):** manually flipping the hypercharge sign for every `bar[...]`/`CC[...]` operand gives `Y(LL)+Y(PhiNPbar)=-1/2-1/2=-1`, not 0. This term is copied **verbatim** from the paper's own quoted FeynRules code (Sec. 3.1: `CC[N1Lbar[sp1]].LL[sp1,ii,ff1] PhiNPbar[jj] Eps[ii,jj]`), which is the authoritative source per the task rules; the exact bookkeeping of gauge quantum numbers through FeynRules' `CC[]` operator on a chirality-projected field cannot be independently re-verified without running FeynRules. I did not substitute an alternative structure of my own invention.

- Kinetic+mass rows present and in the total sum: `Ln4`, `Ln5` — confirmed, both appear in `LTotal`.
- No non-fundamental colour representation is introduced (no sextet/octet) — no `AddGaugeRepresentation` needed.
- `SelfConjugate -> True` classes: `n4`, `n5` — both carry `quantum_numbers: {}` (no QuantumNumbers), confirmed.
- Names chosen: `n4, n5, PhiNP, Mmaj, deltaM, theta, damping, vevNP, MN4, MN5, yn4, yn5` — none is a Mathematica built-in/FeynRules symbol (`N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM`) or an SM.fr name (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,...`).
- Single total Lagrangian: `LTotal := LSM + Ln4 + Ln5 + LNP`, where `LNP := LNPYuk + HC[LNPYuk]`.
- Reference/cached model file read: **none**. Only the paper's own quoted FeynRules snippets (Sec. 3.1) were used, per rule 6.

```json
{
  "model_name": "pSPSS_gen",
  "info": {
    "authors": ["Stefan Antusch", "Jan Hajer", "Johannes Rosskopp"],
    "version": "1.0",
    "date": "2022-10-19",
    "institutions": ["Universität Basel", "Instituto Superior Técnico (IST), Universidade de Lisboa"],
    "emails": ["stefan.antusch@unibas.ch", "jan.hajer@tecnico.ulisboa.pt", "johannes.rosskopp@unibas.ch"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Mmaj",
      "parameter_type": "External",
      "value": "100.",
      "block_name": "PSPSS",
      "order_block": 1,
      "description": "Majorana mass parameter of the symmetric-limit pseudo-Dirac heavy neutrino pair (GeV). Sec. 3.1, Table 1 (mmaj)."
    },
    {
      "name": "deltaM",
      "parameter_type": "External",
      "value": "1.*^-12",
      "block_name": "PSPSS",
      "order_block": 2,
      "description": "Mass splitting Delta m of the heavy neutrino mass eigenstates n4, n5 (GeV). Eq.(eq:Delta m mass splitting), Table 1 (deltam)."
    },
    {
      "name": "theta",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "theta[1]", "rhs": "0.", "delayed": false},
        {"lhs": "theta[2]", "rhs": "1.*^-3", "delayed": false},
        {"lhs": "theta[3]", "rhs": "0.", "delayed": false}
      ],
      "block_name": "PSPSS",
      "description": "Active-sterile mixing parameter vec theta = vec m_D/Mmaj (dimensionless). Eq.(eq:active-sterile mixing), Table 1 (theta1,theta2,theta3)."
    },
    {
      "name": "damping",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "PSPSS",
      "order_block": 6,
      "description": "Damping parameter lambda controlling decoherence of heavy-neutrino oscillations; not a Lagrangian coupling, consumed by the MadGraph patch. Sec. 3.1, Table 1 (damping)."
    },
    {
      "name": "vevNP",
      "parameter_type": "Internal",
      "value": "vev",
      "interaction_order": ["NP", -1],
      "description": "NP-order-tagged copy of the Higgs VEV vev, numerically equal to vev; used only so MadGraph counts NP power correctly. Sec. 3.1."
    },
    {
      "name": "MN4",
      "parameter_type": "Internal",
      "value": "Mmaj*(1 + (theta[1]^2 + theta[2]^2 + theta[3]^2)/2) - deltaM/2",
      "description": "Mass of the heavy Majorana mass eigenstate n4. Eq.(eq:Delta m mass splitting), verified against LaTeX source (\\frac12 factors)."
    },
    {
      "name": "MN5",
      "parameter_type": "Internal",
      "value": "Mmaj*(1 + (theta[1]^2 + theta[2]^2 + theta[3]^2)/2) + deltaM/2",
      "description": "Mass of the heavy Majorana mass eigenstate n5. Eq.(eq:Delta m mass splitting)."
    },
    {
      "name": "yn4",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "yn4[1]", "rhs": "-I*Mmaj*theta[1]/(Sqrt[2]*vevNP)", "delayed": false},
        {"lhs": "yn4[2]", "rhs": "-I*Mmaj*theta[2]/(Sqrt[2]*vevNP)", "delayed": false},
        {"lhs": "yn4[3]", "rhs": "-I*Mmaj*theta[3]/(Sqrt[2]*vevNP)", "delayed": false}
      ],
      "complex": true,
      "interaction_order": ["NP", 1],
      "description": "Portal coupling of n4 to the lepton doublet; LO mixing coefficient -i/Sqrt[2] theta from Eq.(eq:neutrino diagonlisation)/(eq:active-sterile mixing)."
    },
    {
      "name": "yn5",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "yn5[1]", "rhs": "Mmaj*theta[1]/(Sqrt[2]*vevNP)", "delayed": false},
        {"lhs": "yn5[2]", "rhs": "Mmaj*theta[2]/(Sqrt[2]*vevNP)", "delayed": false},
        {"lhs": "yn5[3]", "rhs": "Mmaj*theta[3]/(Sqrt[2]*vevNP)", "delayed": false}
      ],
      "complex": false,
      "interaction_order": ["NP", 1],
      "description": "Portal coupling of n5 to the lepton doublet; LO mixing coefficient 1/Sqrt[2] theta."
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "n4",
      "self_conjugate": true,
      "indices": [],
      "mass": {"massless": false, "sym": "MN4", "value": "Internal"},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 9900012,
      "particle_name": "n4",
      "full_name": "Heavy Majorana neutrino n4",
      "propagator_label": "n4",
      "propagator_type": "Straight",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "n5",
      "self_conjugate": true,
      "indices": [],
      "mass": {"massless": false, "sym": "MN5", "value": "Internal"},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 9900014,
      "particle_name": "n5",
      "full_name": "Heavy Majorana neutrino n5",
      "propagator_label": "n5",
      "propagator_type": "Straight",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "PhiNP",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "1/2"},
      "unphysical": true,
      "definitions": [
        "PhiNP[1] -> -I GP",
        "PhiNP[2] -> (vevNP + H + I G0)/Sqrt[2]"
      ]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "Ln4",
      "expression": "Block[{mu}, ExpandIndices[I/2 n4bar.Ga[mu].del[n4,mu] - 1/2 MN4 n4bar.n4]]",
      "delayed": true
    },
    {
      "name": "Ln5",
      "expression": "Block[{mu}, ExpandIndices[I/2 n5bar.Ga[mu].del[n5,mu] - 1/2 MN5 n5bar.n5]]",
      "delayed": true
    },
    {
      "name": "LNPYuk",
      "expression": "Block[{sp1,ii,jj,ff1}, ExpandIndices[yn4[ff1] CC[n4bar[sp1]].LL[sp1,ii,ff1] PhiNPbar[jj] Eps[ii,jj] + yn5[ff1] CC[n5bar[sp1]].LL[sp1,ii,ff1] PhiNPbar[jj] Eps[ii,jj], FlavorExpand->SU2D]]",
      "delayed": true
    },
    {
      "name": "LNP",
      "expression": "LNPYuk + HC[LNPYuk]",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + Ln4 + Ln5 + LNP",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```