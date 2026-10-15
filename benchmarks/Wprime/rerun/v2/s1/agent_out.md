I'll start by reading the paper and the schema.
I read the paper (all 3134 lines), `frmodel.py`, `render.py`, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Physics content found in the paper

- **W′ boson**: charged spin-1 mass eigenstate, colour singlet, Q = +1, mass m_W′ (200–1000 GeV benchmarks; 500 GeV is the reference point). Eq. (1) gives the general vector/axial current; Eq. (2) rewrites it with g_L, g_R, the left-right mixing angle ζ, the CP phase ω, and the GCKM matrices V^L, V^R. Eq. (24) gives the numeric GCKM benchmark.
- **Right-handed neutrino ν_R**: new fermion with mass m_νR. The paper treats it as a real final state (N_c = 1, m = m_νR in Eq. 28) and splits all tables by whether W′ → l ν_R is open. It is the SU(2)-singlet partner that the right-handed current in Eq. (2) needs, so it enters as a 3-member Dirac class.
- No new scalars, no new colour reps, no new U(1) beyond electric charge, no `1/Λ^n` operator (the W′ current is dimension 4), no ψ^c in any equation.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling | coupling dim (must be 4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L number sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpKin (kinetic) | FS[Wpbar]·FS[Wp] | 4 | 1 | 0 ✓ | n/a | −1+1 = 0 ✓ | n/a (physical mass eigenstate, Q only) | none (W′ is a mass eigenstate, not a doublet) | singlet×singlet ✓ | none declared | 0 ✓ | n/a | self-conjugate combination ✓ |
| LWpKin (mass) | MWp^2 Wpbar[mu] Wp[mu] | 2 (fields) + MWp^2 | 4 total | MWp^2 dim 2 ✓ | n/a | −1+1 = 0 ✓ | n/a | none | singlet ✓ | none | 0 ✓ | n/a | self-conjugate ✓ |
| LNRKin (kinetic) | nRbar Ga del nR | 3/2+1+3/2 = 4 | I | 0 ✓ | n/a | 0+0 = 0 ✓ | n/a (Q=0, Y=0 singlet) | singlet ✓ | singlet ✓ | none | −1+1 = 0 ✓ | n/a (paper writes no ψ^c) | self-conjugate ✓ |
| LNRKin (mass) | MNR[ff] nRbar nR | 3 + MNR | 4 total | MNR dim 1 ✓ | n/a | 0 ✓ | n/a | singlet ✓ | singlet ✓ | none | 0 ✓ | n/a | real Dirac mass ✓ |
| LWpQuarks | uqbar Ga (CRq ProjP + CLq ProjM) dq Wp | 3/2+3/2+1 = 4 | CRq, CLq | 0 ✓ | n/a (d = 4) | −2/3 −1/3 +1 = 0 ✓ | n/a (SM.fr physical quarks carry Q only) | none; W′ is a mass eigenstate | shared index cc: uqbar[cc] … dq[cc] → singlet ✓ | none | 0 ✓ | no (Eq. 1 has no ψ^c) | HC[LWpQuarks] ✓ |
| LWpLeptons (L part) | vlbar Ga ProjM l Wp | 4 | CLl | 0 ✓ | n/a | 0 −1 +1 = 0 ✓ | n/a | none | all singlets ✓ | none | −1+1 = 0 ✓ | no | HC[…] ✓ |
| LWpLeptons (R part) | nRbar Ga ProjP l Wp | 4 | CRl | 0 ✓ | n/a | 0 −1 +1 = 0 ✓ | n/a | none | all singlets ✓ | none | −1+1 = 0 ✓ | no | HC[…] ✓ |
| per-class check: Wp | kinetic + mass term LWpKin present, added to LWprime sum ✓ | | | | | | | | | | | | |
| per-class check: nR | kinetic + mass term LNRKin present, added to LWprime sum ✓ | | | | | | | | | | | | |

Classes with `SelfConjugate -> True`: **none** (Wp is a charged complex vector, nR is a Dirac fermion), so no quantum numbers sit on a self-conjugate class.

Reference or cached model file read: **none**.

No operator has d > 4, so no EFT cutoff parameter is required. The couplings CRq, CLq, CRl, CLl are dimensionless, built from the paper's g_R, g_L, ζ, ω and the GCKM matrices of Eq. (24).

```json
{
  "model_name": "Wprime_gen",
  "info": {
    "authors": ["Z. Sullivan"],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["Theoretical Physics Department, Fermi National Accelerator Laboratory"],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gLp",
      "parameter_type": "External",
      "value": "0.65",
      "block_name": "WPRIME",
      "order_block": 1,
      "interaction_order": ["QED", 1],
      "tex": "g_L",
      "description": "Left-handed gauge coupling gL of the Wprime charged current, Eq.(2); equal to the SM SU(2)L coupling gw"
    },
    {
      "name": "gRp",
      "parameter_type": "External",
      "value": "0.65",
      "block_name": "WPRIME",
      "order_block": 2,
      "interaction_order": ["QED", 1],
      "tex": "g_R",
      "description": "Right-handed gauge coupling gR of the Wprime charged current, Eq.(2)"
    },
    {
      "name": "zetaLR",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "WPRIME",
      "order_block": 3,
      "tex": "\\zeta",
      "description": "Left-right mixing angle zeta of Eq.(2); the paper quotes |zeta| < a few 1e-5 to 1e-2"
    },
    {
      "name": "omegaCP",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "WPRIME",
      "order_block": 4,
      "tex": "\\omega",
      "description": "CP-violating phase omega of Eq.(2); it can be absorbed into the right-handed GCKM matrix"
    },
    {
      "name": "VLq",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "GCKML",
      "value_rules": [
        {"lhs": "VLq[1,1]", "rhs": "0.9751"},
        {"lhs": "VLq[1,2]", "rhs": "0.2215"},
        {"lhs": "VLq[1,3]", "rhs": "0.0035"},
        {"lhs": "VLq[2,1]", "rhs": "0.2210"},
        {"lhs": "VLq[2,2]", "rhs": "0.9743"},
        {"lhs": "VLq[2,3]", "rhs": "0.0410"},
        {"lhs": "VLq[3,1]", "rhs": "0.0090"},
        {"lhs": "VLq[3,2]", "rhs": "0.0400"},
        {"lhs": "VLq[3,3]", "rhs": "1.0000"}
      ],
      "tex": "V^L",
      "description": "Left-handed generalized CKM (GCKM) matrix for quarks, Eq.(2); benchmark values of Eq.(24) with |Vtb| = 1"
    },
    {
      "name": "VRq",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "GCKMR",
      "value_rules": [
        {"lhs": "VRq[1,1]", "rhs": "0.9751"},
        {"lhs": "VRq[1,2]", "rhs": "0.2215"},
        {"lhs": "VRq[1,3]", "rhs": "0.0035"},
        {"lhs": "VRq[2,1]", "rhs": "0.2210"},
        {"lhs": "VRq[2,2]", "rhs": "0.9743"},
        {"lhs": "VRq[2,3]", "rhs": "0.0410"},
        {"lhs": "VRq[3,1]", "rhs": "0.0090"},
        {"lhs": "VRq[3,2]", "rhs": "0.0400"},
        {"lhs": "VRq[3,3]", "rhs": "1.0000"}
      ],
      "tex": "V^R",
      "description": "Right-handed generalized CKM (GCKM) matrix for quarks, Eq.(2); benchmark values of Eq.(24) with |Vtb| = 1"
    },
    {
      "name": "VLl",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "GCKMLL",
      "value_rules": [
        {"lhs": "VLl[1,1]", "rhs": "1.0000"},
        {"lhs": "VLl[1,2]", "rhs": "0."},
        {"lhs": "VLl[1,3]", "rhs": "0."},
        {"lhs": "VLl[2,1]", "rhs": "0."},
        {"lhs": "VLl[2,2]", "rhs": "1.0000"},
        {"lhs": "VLl[2,3]", "rhs": "0."},
        {"lhs": "VLl[3,1]", "rhs": "0."},
        {"lhs": "VLl[3,2]", "rhs": "0."},
        {"lhs": "VLl[3,3]", "rhs": "1.0000"}
      ],
      "tex": "V^L_l",
      "description": "Left-handed GCKM matrix for leptons, Eq.(2); the paper takes it to be the identity matrix"
    },
    {
      "name": "VRl",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "GCKMRL",
      "value_rules": [
        {"lhs": "VRl[1,1]", "rhs": "1.0000"},
        {"lhs": "VRl[1,2]", "rhs": "0."},
        {"lhs": "VRl[1,3]", "rhs": "0."},
        {"lhs": "VRl[2,1]", "rhs": "0."},
        {"lhs": "VRl[2,2]", "rhs": "1.0000"},
        {"lhs": "VRl[2,3]", "rhs": "0."},
        {"lhs": "VRl[3,1]", "rhs": "0."},
        {"lhs": "VRl[3,2]", "rhs": "0."},
        {"lhs": "VRl[3,3]", "rhs": "1.0000"}
      ],
      "tex": "V^R_l",
      "description": "Right-handed GCKM matrix for leptons, Eq.(2); the paper takes it to be the identity matrix"
    },
    {
      "name": "CLq",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "interaction_order": ["QED", 1],
      "definitions": [
        {"lhs": "CLq[i_,j_]", "rhs": "gLp Sin[zetaLR] VLq[i,j]", "delayed": true}
      ],
      "tex": "C^L_q",
      "description": "Left-handed Wprime coupling to quarks, C^L of Eq.(1) written as gL sin(zeta) V^L of Eq.(2)"
    },
    {
      "name": "CRq",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "interaction_order": ["QED", 1],
      "definitions": [
        {"lhs": "CRq[i_,j_]", "rhs": "gRp Cos[zetaLR] Exp[I omegaCP] VRq[i,j]", "delayed": true}
      ],
      "tex": "C^R_q",
      "description": "Right-handed Wprime coupling to quarks, C^R of Eq.(1) written as gR exp(I omega) cos(zeta) V^R of Eq.(2)"
    },
    {
      "name": "CLl",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "interaction_order": ["QED", 1],
      "definitions": [
        {"lhs": "CLl[i_,j_]", "rhs": "gLp Sin[zetaLR] VLl[i,j]", "delayed": true}
      ],
      "tex": "C^L_l",
      "description": "Left-handed Wprime coupling to leptons, C^L of Eq.(1) written as gL sin(zeta) V^L of Eq.(2)"
    },
    {
      "name": "CRl",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "interaction_order": ["QED", 1],
      "definitions": [
        {"lhs": "CRl[i_,j_]", "rhs": "gRp Cos[zetaLR] Exp[I omegaCP] VRl[i,j]", "delayed": true}
      ],
      "tex": "C^R_l",
      "description": "Right-handed Wprime coupling to leptons; it connects a charged lepton to the right-handed neutrino nR"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Wp",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MWp", "value": "500."},
      "width": {"sym": "WWp", "value": "16.701"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 34,
      "particle_name": "W'+",
      "antiparticle_name": "W'-",
      "full_name": "Wprime boson",
      "propagator_label": "Wp",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "nR",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["nR1", "nR2", "nR3"],
      "mass": {
        "sym": "MNR",
        "members": [["MNR1", "100."], ["MNR2", "100."], ["MNR3", "100."]]
      },
      "width": {"massless": true},
      "quantum_numbers": {"LeptonNumber": "1"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["nR1", "nR2", "nR3"],
      "antiparticle_name": ["nR1~", "nR2~", "nR3~"],
      "full_name": ["Right-handed electron-neutrino", "Right-handed mu-neutrino", "Right-handed tau-neutrino"],
      "propagator_label": ["nR", "nR1", "nR2", "nR3"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWpKin",
      "delayed": true,
      "expression": "Block[{mu, nu}, ExpandIndices[-1/2 FS[Wpbar, mu, nu] FS[Wp, mu, nu] + MWp^2 Wpbar[mu] Wp[mu]]]"
    },
    {
      "name": "LNRKin",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, ff}, ExpandIndices[I nRbar[sp1, ff].Ga[mu, sp1, sp2].del[nR[sp2, ff], mu] - MNR[ff] nRbar[sp1, ff].nR[sp1, ff]]]"
    },
    {
      "name": "LWpQuarks",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, ff1, ff2, cc, LWpq}, LWpq = 1/Sqrt[2] Wp[mu] uqbar[sp1, ff1, cc].Ga[mu, sp1, sp2].(CRq[ff1, ff2] ProjP[sp2, sp3] + CLq[ff1, ff2] ProjM[sp2, sp3]).dq[sp3, ff2, cc]; ExpandIndices[LWpq + HC[LWpq]]]"
    },
    {
      "name": "LWpLeptons",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, ff1, ff2, LWpl}, LWpl = 1/Sqrt[2] Wp[mu] (CLl[ff1, ff2] vlbar[sp1, ff1].Ga[mu, sp1, sp2].ProjM[sp2, sp3].l[sp3, ff2] + CRl[ff1, ff2] nRbar[sp1, ff1].Ga[mu, sp1, sp2].ProjP[sp2, sp3].l[sp3, ff2]); ExpandIndices[LWpl + HC[LWpl]]]"
    },
    {
      "name": "LWprime",
      "delayed": true,
      "expression": "LWpKin + LNRKin + LWpQuarks + LWpLeptons"
    }
  ]
}
```
I read the paper (all 3134 lines), `frmodel.py`, `render.py`, and `SM.fr`. No cached or reference `.fr` file for this model exists in the sandbox, and none was read.

## Physics content found in the paper

- **W′ boson**: charged spin-1 mass eigenstate, colour singlet, Q = +1, mass m_W′ (200–1000 GeV benchmarks; 500 GeV is the reference point). Eq. (1) gives the general vector/axial current; Eq. (2) rewrites it with g_L, g_R, the left-right mixing angle ζ, the CP phase ω, and the GCKM matrices V^L, V^R. Eq. (24) gives the numeric GCKM benchmark.
- **Right-handed neutrino ν_R**: new fermion with mass m_νR. The paper treats it as a real final state (N_c = 1, m = m_νR in Eq. 28) and splits all tables by whether W′ → l ν_R is open. It is the SU(2)-singlet partner that the right-handed current in Eq. (2) needs, so it enters as a 3-member Dirac class.
- No new scalars, no new colour reps, no new U(1) beyond electric charge, no `1/Λ^n` operator (the W′ current is dimension 4), no ψ^c in any equation.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling | coupling dim (must be 4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | L number sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpKin (kinetic) | FS[Wpbar]·FS[Wp] | 4 | 1 | 0 ✓ | n/a | −1+1 = 0 ✓ | n/a (physical mass eigenstate, Q only) | none (W′ is a mass eigenstate, not a doublet) | singlet×singlet ✓ | none declared | 0 ✓ | n/a | self-conjugate combination ✓ |
| LWpKin (mass) | MWp^2 Wpbar[mu] Wp[mu] | 2 (fields) + MWp^2 | 4 total | MWp^2 dim 2 ✓ | n/a | −1+1 = 0 ✓ | n/a | none | singlet ✓ | none | 0 ✓ | n/a | self-conjugate ✓ |
| LNRKin (kinetic) | nRbar Ga del nR | 3/2+1+3/2 = 4 | I | 0 ✓ | n/a | 0+0 = 0 ✓ | n/a (Q=0, Y=0 singlet) | singlet ✓ | singlet ✓ | none | −1+1 = 0 ✓ | n/a (paper writes no ψ^c) | self-conjugate ✓ |
| LNRKin (mass) | MNR[ff] nRbar nR | 3 + MNR | 4 total | MNR dim 1 ✓ | n/a | 0 ✓ | n/a | singlet ✓ | singlet ✓ | none | 0 ✓ | n/a | real Dirac mass ✓ |
| LWpQuarks | uqbar Ga (CRq ProjP + CLq ProjM) dq Wp | 3/2+3/2+1 = 4 | CRq, CLq | 0 ✓ | n/a (d = 4) | −2/3 −1/3 +1 = 0 ✓ | n/a (SM.fr physical quarks carry Q only) | none; W′ is a mass eigenstate | shared index cc: uqbar[cc] … dq[cc] → singlet ✓ | none | 0 ✓ | no (Eq. 1 has no ψ^c) | HC[LWpQuarks] ✓ |
| LWpLeptons (L part) | vlbar Ga ProjM l Wp | 4 | CLl | 0 ✓ | n/a | 0 −1 +1 = 0 ✓ | n/a | none | all singlets ✓ | none | −1+1 = 0 ✓ | no | HC[…] ✓ |
| LWpLeptons (R part) | nRbar Ga ProjP l Wp | 4 | CRl | 0 ✓ | n/a | 0 −1 +1 = 0 ✓ | n/a | none | all singlets ✓ | none | −1+1 = 0 ✓ | no | HC[…] ✓ |
| per-class check: Wp | kinetic + mass term LWpKin present, added to LWprime sum ✓ | | | | | | | | | | | | |
| per-class check: nR | kinetic + mass term LNRKin present, added to LWprime sum ✓ | | | | | | | | | | | | |

Classes with `SelfConjugate -> True`: **none** (Wp is a charged complex vector, nR is a Dirac fermion), so no quantum numbers sit on a self-conjugate class.

Reference or cached model file read: **none**.

No operator has d > 4, so no EFT cutoff parameter is required. The couplings CRq, CLq, CRl, CLl are dimensionless, built from the paper's g_R, g_L, ζ, ω and the GCKM matrices of Eq. (24).

```json
{
  "model_name": "Wprime_gen",
  "info": {
    "authors": ["Z. Sullivan"],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["Theoretical Physics Department, Fermi National Accelerator Laboratory"],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gLp",
      "parameter_type": "External",
      "value": "0.65",
      "block_name": "WPRIME",
      "order_block": 1,
      "interaction_order": ["QED", 1],
      "tex": "g_L",
      "description": "Left-handed gauge coupling gL of the Wprime charged current, Eq.(2); equal to the SM SU(2)L coupling gw"
    },
    {
      "name": "gRp",
      "parameter_type": "External",
      "value": "0.65",
      "block_name": "WPRIME",
      "order_block": 2,
      "interaction_order": ["QED", 1],
      "tex": "g_R",
      "description": "Right-handed gauge coupling gR of the Wprime charged current, Eq.(2)"
    },
    {
      "name": "zetaLR",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "WPRIME",
      "order_block": 3,
      "tex": "\\zeta",
      "description": "Left-right mixing angle zeta of Eq.(2); the paper quotes |zeta| < a few 1e-5 to 1e-2"
    },
    {
      "name": "omegaCP",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "WPRIME",
      "order_block": 4,
      "tex": "\\omega",
      "description": "CP-violating phase omega of Eq.(2); it can be absorbed into the right-handed GCKM matrix"
    },
    {
      "name": "VLq",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "GCKML",
      "value_rules": [
        {"lhs": "VLq[1,1]", "rhs": "0.9751"},
        {"lhs": "VLq[1,2]", "rhs": "0.2215"},
        {"lhs": "VLq[1,3]", "rhs": "0.0035"},
        {"lhs": "VLq[2,1]", "rhs": "0.2210"},
        {"lhs": "VLq[2,2]", "rhs": "0.9743"},
        {"lhs": "VLq[2,3]", "rhs": "0.0410"},
        {"lhs": "VLq[3,1]", "rhs": "0.0090"},
        {"lhs": "VLq[3,2]", "rhs": "0.0400"},
        {"lhs": "VLq[3,3]", "rhs": "1.0000"}
      ],
      "tex": "V^L",
      "description": "Left-handed generalized CKM (GCKM) matrix for quarks, Eq.(2); benchmark values of Eq.(24) with |Vtb| = 1"
    },
    {
      "name": "VRq",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "GCKMR",
      "value_rules": [
        {"lhs": "VRq[1,1]", "rhs": "0.9751"},
        {"lhs": "VRq[1,2]", "rhs": "0.2215"},
        {"lhs": "VRq[1,3]", "rhs": "0.0035"},
        {"lhs": "VRq[2,1]", "rhs": "0.2210"},
        {"lhs": "VRq[2,2]", "rhs": "0.9743"},
        {"lhs": "VRq[2,3]", "rhs": "0.0410"},
        {"lhs": "VRq[3,1]", "rhs": "0.0090"},
        {"lhs": "VRq[3,2]", "rhs": "0.0400"},
        {"lhs": "VRq[3,3]", "rhs": "1.0000"}
      ],
      "tex": "V^R",
      "description": "Right-handed generalized CKM (GCKM) matrix for quarks, Eq.(2); benchmark values of Eq.(24) with |Vtb| = 1"
    },
    {
      "name": "VLl",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "GCKMLL",
      "value_rules": [
        {"lhs": "VLl[1,1]", "rhs": "1.0000"},
        {"lhs": "VLl[1,2]", "rhs": "0."},
        {"lhs": "VLl[1,3]", "rhs": "0."},
        {"lhs": "VLl[2,1]", "rhs": "0."},
        {"lhs": "VLl[2,2]", "rhs": "1.0000"},
        {"lhs": "VLl[2,3]", "rhs": "0."},
        {"lhs": "VLl[3,1]", "rhs": "0."},
        {"lhs": "VLl[3,2]", "rhs": "0."},
        {"lhs": "VLl[3,3]", "rhs": "1.0000"}
      ],
      "tex": "V^L_l",
      "description": "Left-handed GCKM matrix for leptons, Eq.(2); the paper takes it to be the identity matrix"
    },
    {
      "name": "VRl",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "GCKMRL",
      "value_rules": [
        {"lhs": "VRl[1,1]", "rhs": "1.0000"},
        {"lhs": "VRl[1,2]", "rhs": "0."},
        {"lhs": "VRl[1,3]", "rhs": "0."},
        {"lhs": "VRl[2,1]", "rhs": "0."},
        {"lhs": "VRl[2,2]", "rhs": "1.0000"},
        {"lhs": "VRl[2,3]", "rhs": "0."},
        {"lhs": "VRl[3,1]", "rhs": "0."},
        {"lhs": "VRl[3,2]", "rhs": "0."},
        {"lhs": "VRl[3,3]", "rhs": "1.0000"}
      ],
      "tex": "V^R_l",
      "description": "Right-handed GCKM matrix for leptons, Eq.(2); the paper takes it to be the identity matrix"
    },
    {
      "name": "CLq",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "interaction_order": ["QED", 1],
      "definitions": [
        {"lhs": "CLq[i_,j_]", "rhs": "gLp Sin[zetaLR] VLq[i,j]", "delayed": true}
      ],
      "tex": "C^L_q",
      "description": "Left-handed Wprime coupling to quarks, C^L of Eq.(1) written as gL sin(zeta) V^L of Eq.(2)"
    },
    {
      "name": "CRq",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "interaction_order": ["QED", 1],
      "definitions": [
        {"lhs": "CRq[i_,j_]", "rhs": "gRp Cos[zetaLR] Exp[I omegaCP] VRq[i,j]", "delayed": true}
      ],
      "tex": "C^R_q",
      "description": "Right-handed Wprime coupling to quarks, C^R of Eq.(1) written as gR exp(I omega) cos(zeta) V^R of Eq.(2)"
    },
    {
      "name": "CLl",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "interaction_order": ["QED", 1],
      "definitions": [
        {"lhs": "CLl[i_,j_]", "rhs": "gLp Sin[zetaLR] VLl[i,j]", "delayed": true}
      ],
      "tex": "C^L_l",
      "description": "Left-handed Wprime coupling to leptons, C^L of Eq.(1) written as gL sin(zeta) V^L of Eq.(2)"
    },
    {
      "name": "CRl",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation", "Generation"],
      "interaction_order": ["QED", 1],
      "definitions": [
        {"lhs": "CRl[i_,j_]", "rhs": "gRp Cos[zetaLR] Exp[I omegaCP] VRl[i,j]", "delayed": true}
      ],
      "tex": "C^R_l",
      "description": "Right-handed Wprime coupling to leptons; it connects a charged lepton to the right-handed neutrino nR"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Wp",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MWp", "value": "500."},
      "width": {"sym": "WWp", "value": "16.701"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 34,
      "particle_name": "W'+",
      "antiparticle_name": "W'-",
      "full_name": "Wprime boson",
      "propagator_label": "Wp",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "nR",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["nR1", "nR2", "nR3"],
      "mass": {
        "sym": "MNR",
        "members": [["MNR1", "100."], ["MNR2", "100."], ["MNR3", "100."]]
      },
      "width": {"massless": true},
      "quantum_numbers": {"LeptonNumber": "1"},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["nR1", "nR2", "nR3"],
      "antiparticle_name": ["nR1~", "nR2~", "nR3~"],
      "full_name": ["Right-handed electron-neutrino", "Right-handed mu-neutrino", "Right-handed tau-neutrino"],
      "propagator_label": ["nR", "nR1", "nR2", "nR3"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWpKin",
      "delayed": true,
      "expression": "Block[{mu, nu}, ExpandIndices[-1/2 FS[Wpbar, mu, nu] FS[Wp, mu, nu] + MWp^2 Wpbar[mu] Wp[mu]]]"
    },
    {
      "name": "LNRKin",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, ff}, ExpandIndices[I nRbar[sp1, ff].Ga[mu, sp1, sp2].del[nR[sp2, ff], mu] - MNR[ff] nRbar[sp1, ff].nR[sp1, ff]]]"
    },
    {
      "name": "LWpQuarks",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, ff1, ff2, cc, LWpq}, LWpq = 1/Sqrt[2] Wp[mu] uqbar[sp1, ff1, cc].Ga[mu, sp1, sp2].(CRq[ff1, ff2] ProjP[sp2, sp3] + CLq[ff1, ff2] ProjM[sp2, sp3]).dq[sp3, ff2, cc]; ExpandIndices[LWpq + HC[LWpq]]]"
    },
    {
      "name": "LWpLeptons",
      "delayed": true,
      "expression": "Block[{mu, sp1, sp2, sp3, ff1, ff2, LWpl}, LWpl = 1/Sqrt[2] Wp[mu] (CLl[ff1, ff2] vlbar[sp1, ff1].Ga[mu, sp1, sp2].ProjM[sp2, sp3].l[sp3, ff2] + CRl[ff1, ff2] nRbar[sp1, ff1].Ga[mu, sp1, sp2].ProjP[sp2, sp3].l[sp3, ff2]); ExpandIndices[LWpl + HC[LWpl]]]"
    },
    {
      "name": "LWprime",
      "delayed": true,
      "expression": "LWpKin + LNRKin + LWpQuarks + LWpLeptons"
    }
  ]
}
```