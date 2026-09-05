I'll start by reading the paper and the schema.
I read the paper, the schema, the renderer, and `SM.fr`. No cached or reference `.fr` model file for DMsimp exists here, and I opened none.

## New-physics content found in the paper

- **Sec. 2, Eq. (1)–(2)**: DM particle χ (Dirac fermion), mediator Y0 (spin-0, scalar/pseudoscalar) and Y1 (spin-1, vector/axial-vector). Both mediators are neutral colour singlets.
- **Sec. 2**: "the implementation of the model is flexible to allow a real or complex scalar" DM ⇒ two more DM states, Xr (real) and Xc (complex).
- **Eq. (2)**: the axial coupling to the bottom quark, fixed to `-gAt`, to cancel the gauge anomaly.
- **Eq. (3)**: the infinite-top-mass (top-EFT) operators `Y0 G G` and `Y0 G G~`, with the paper's own coefficients `aS/(12 Pi vev)` and `aS/(8 Pi vev)`.
- **Tables 1–2**: mass and width benchmarks. I use the "resonant" point: mediator 200 GeV, DM 50 GeV, widths 5.17 GeV.

## Self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L/B sum | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LXdkin (kin) | Xdbar Ga DC[Xd] | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | none in model | 0 | n/a | self-conjugate (Hermitian) |
| LXdkin (mass) | Xdbar Xd | 3 | MXd | 1 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian |
| LXrkin | del[Xr] del[Xr]; Xr Xr | 4; 2 | 1; MXr^2 | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field |
| LXckin | DC[Xcbar] DC[Xc]; Xcbar Xc | 4; 2 | 1; MXc^2 | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian |
| LY0kin | del[Y0] del[Y0]; Y0 Y0 | 4; 2 | 1; MY0^2 | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field |
| LY1kin | FS[Y1] FS[Y1]; Y1 Y1 | 4; 2 | 1; MY1^2 | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field |
| LY0DM | Xdbar Xd Y0; Xdbar Ga[5] Xd Y0 | 4 | gSXd, gPXd | 0 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian (the `I` in front of gPXd makes `I Xdbar.Ga[5].Xd` Hermitian) |
| LY0SM | tbar t Y0; tbar Ga[5] t Y0 | 4 | yt0/Sqrt[2] gSt, gPt | 0 | n/a | −2/3+2/3+0 = 0 | n/a (mass-basis fields carry only Q in SM.fr) | singlet, mass basis as in Eq.(1) | 3⊗3bar = 1 | none | 0 | n/a | Hermitian |
| LY1DM | Xdbar Ga[mu] Xd Y1 | 4 | gVXd, gAXd | 0 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian |
| LY1SM | tbar Ga[mu] t Y1; bbar Ga[mu] Ga[5] b Y1 | 4 | gVt, gAt, −gAt | 0 | n/a | 0 (and −1/3+1/3+0 = 0) | n/a | singlet, mass basis as in Eq.(2) | 3⊗3bar = 1 | none | 0 | n/a | Hermitian |
| LXrY0 | Y0 Xr Xr | 3 | gSXr | 1 (GeV) | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real fields |
| LXcY0 | Y0 Xcbar Xc | 3 | gSXc | 1 (GeV) | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian |
| LXcY1 | Y1 Xcbar del[Xc] | 4 | gVXc | 0 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian (the `I` and the antisymmetric current) |
| LY0GG | FS[G] FS[G] Y0 (and dual) | 5 | gYGGS = aS gSt/(12 Pi vev), gYGGP = aS gPt/(8 Pi vev) | −1 (GeV^-1) | d−4 = 1; the paper's Eq.(3) uses 1/vev, not a free Λ, so no cutoff parameter is invented — the Description states dimension −1 and units GeV^-1 | 0 | 0 | singlet | 8⊗8 = 1 | none | 0 | n/a | Hermitian |

Kinetic + mass term rows above exist for every new class: Xd, Xr, Xc, Y0, Y1. All five are in the total `LDMsimp`.

`SelfConjugate -> True` classes: **Y0, Y1, Xr** — each carries no `QuantumNumbers`.

Reference or cached model file read: **none**.

Two notes on choices. There is no new U(1) gauge group in this model, so rule 5 does not apply; the mediator couplings are written in the mass basis exactly as Eq. (1)–(2) do. The top-EFT operator of Eq. (3) replaces the resolved top loop, so adding it to the main sum would double count; I put it in a separate total `LDMsimpTopEFT`.

```json
{
  "model_name": "DMsimp_gen",
  "info": {
    "authors": ["O. Mattelaer", "E. Vryonidou"],
    "version": "1.0",
    "date": "03. 08. 2015",
    "institutions": ["IPPP, Durham University", "CP3, Universite catholique de Louvain"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "vevs": [],
  "parameters": [
    {
      "name": "gSXd",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Scalar coupling of the spin-0 mediator Y0 to the Dirac dark matter Xd, gS_DM of Eq.(1); benchmark value 1"
    },
    {
      "name": "gPXd",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "Pseudoscalar coupling of Y0 to the Dirac dark matter Xd, gP_DM of Eq.(1); 0 in the scalar benchmark, 1 in the pseudoscalar benchmark"
    },
    {
      "name": "gSt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "description": "Scalar coupling of Y0 to the top quark, gS_t of Eq.(1), normalised by the top Yukawa yt/Sqrt[2]; benchmark value 1"
    },
    {
      "name": "gPt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 4,
      "interaction_order": ["NP", 1],
      "description": "Pseudoscalar coupling of Y0 to the top quark, gP_t of Eq.(1); 0 in the scalar benchmark, 1 in the pseudoscalar benchmark"
    },
    {
      "name": "gVXd",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "description": "Vector coupling of the spin-1 mediator Y1 to the Dirac dark matter Xd, gV_DM of Eq.(2); benchmark value 1"
    },
    {
      "name": "gAXd",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 6,
      "interaction_order": ["NP", 1],
      "description": "Axial-vector coupling of Y1 to the Dirac dark matter Xd, gA_DM of Eq.(2); 0 in the vector benchmark, 1 in the axial-vector benchmark"
    },
    {
      "name": "gVt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 7,
      "interaction_order": ["NP", 1],
      "description": "Vector coupling of Y1 to the top quark, gV_t of Eq.(2); benchmark value 1"
    },
    {
      "name": "gAt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 8,
      "interaction_order": ["NP", 1],
      "description": "Axial-vector coupling of Y1 to the top quark, gA_t of Eq.(2); the bottom quark takes the opposite coupling -gA_t to cancel the gauge anomaly"
    },
    {
      "name": "gSXr",
      "parameter_type": "External",
      "value": "100.",
      "block_name": "DMINPUTS",
      "order_block": 9,
      "interaction_order": ["NP", 1],
      "description": "Trilinear coupling of Y0 to the real scalar dark matter Xr [GeV], mass dimension 1, units GeV; Sec. 2 states the implementation also allows a real or complex scalar dark matter"
    },
    {
      "name": "gSXc",
      "parameter_type": "External",
      "value": "100.",
      "block_name": "DMINPUTS",
      "order_block": 10,
      "interaction_order": ["NP", 1],
      "description": "Trilinear coupling of Y0 to the complex scalar dark matter Xc [GeV], mass dimension 1, units GeV; Sec. 2 states the implementation also allows a real or complex scalar dark matter"
    },
    {
      "name": "gVXc",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 11,
      "interaction_order": ["NP", 1],
      "description": "Vector coupling of Y1 to the conserved current of the complex scalar dark matter Xc; dimensionless, benchmark value 1"
    },
    {
      "name": "yt0",
      "parameter_type": "Internal",
      "value": "ymt/vev",
      "interaction_order": ["QED", 1],
      "tex": "y_t",
      "description": "Top Yukawa coupling yt = mt/v used to normalise the Y0 coupling to the top quark in Eq.(1)"
    },
    {
      "name": "gYGGS",
      "parameter_type": "Internal",
      "value": "aS*gSt/(12*Pi*vev)",
      "description": "Effective Y0-gluon-gluon coupling in the infinite top mass limit, aS gS_t/(12 Pi v) of Eq.(3); mass dimension -1, units GeV^-1"
    },
    {
      "name": "gYGGP",
      "parameter_type": "Internal",
      "value": "aS*gPt/(8*Pi*vev)",
      "description": "Effective Y0-gluon-gluon CP-odd coupling in the infinite top mass limit, aS gP_t/(8 Pi v) of Eq.(3); mass dimension -1, units GeV^-1"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Xd",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MXd", "value": "50."},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 52,
      "particle_name": "xd",
      "antiparticle_name": "xd~",
      "full_name": "Dirac fermion dark matter",
      "propagator_label": "Xd",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Xr",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MXr", "value": "50."},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 51,
      "particle_name": "xr",
      "full_name": "Real scalar dark matter",
      "propagator_label": "Xr",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "Xc",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MXc", "value": "50."},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 53,
      "particle_name": "xc",
      "antiparticle_name": "xc~",
      "full_name": "Complex scalar dark matter",
      "propagator_label": "Xc",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "Y0",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MY0", "value": "200."},
      "width": {"sym": "WY0", "value": "5.17"},
      "quantum_numbers": {},
      "pdg": 54,
      "particle_name": "y0",
      "full_name": "Spin-0 s-channel mediator",
      "propagator_label": "Y0",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Y1",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MY1", "value": "200."},
      "width": {"sym": "WY1", "value": "5.17"},
      "quantum_numbers": {},
      "pdg": 55,
      "particle_name": "y1",
      "full_name": "Spin-1 s-channel mediator",
      "propagator_label": "Y1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LXdkin",
      "expression": "Block[{mu}, I Xdbar.Ga[mu].DC[Xd, mu] - MXd Xdbar.Xd]",
      "delayed": true
    },
    {
      "name": "LXrkin",
      "expression": "Block[{mu}, 1/2 del[Xr, mu] del[Xr, mu] - 1/2 MXr^2 Xr Xr]",
      "delayed": true
    },
    {
      "name": "LXckin",
      "expression": "Block[{mu}, DC[Xcbar, mu] DC[Xc, mu] - MXc^2 Xcbar Xc]",
      "delayed": true
    },
    {
      "name": "LY0kin",
      "expression": "Block[{mu}, 1/2 del[Y0, mu] del[Y0, mu] - 1/2 MY0^2 Y0 Y0]",
      "delayed": true
    },
    {
      "name": "LY1kin",
      "expression": "Block[{mu, nu}, -1/4 FS[Y1, mu, nu] FS[Y1, mu, nu] + 1/2 MY1^2 Y1[mu] Y1[mu]]",
      "delayed": true
    },
    {
      "name": "LY0DM",
      "expression": "gSXd Xdbar.Xd Y0 + I gPXd Xdbar.Ga[5].Xd Y0",
      "delayed": true
    },
    {
      "name": "LY0SM",
      "expression": "yt0/Sqrt[2] (gSt tbar.t + I gPt tbar.Ga[5].t) Y0",
      "delayed": true
    },
    {
      "name": "LY1DM",
      "expression": "Block[{mu}, (gVXd Xdbar.Ga[mu].Xd + gAXd Xdbar.Ga[mu].Ga[5].Xd) Y1[mu]]",
      "delayed": true
    },
    {
      "name": "LY1SM",
      "expression": "Block[{mu}, (gVt tbar.Ga[mu].t + gAt tbar.Ga[mu].Ga[5].t - gAt bbar.Ga[mu].Ga[5].b) Y1[mu]]",
      "delayed": true
    },
    {
      "name": "LXrY0",
      "expression": "1/2 gSXr Y0 Xr Xr",
      "delayed": true
    },
    {
      "name": "LXcY0",
      "expression": "gSXc Y0 Xcbar Xc",
      "delayed": true
    },
    {
      "name": "LXcY1",
      "expression": "Block[{mu}, I gVXc Y1[mu] (Xcbar del[Xc, mu] - del[Xcbar, mu] Xc)]",
      "delayed": true
    },
    {
      "name": "LY0GG",
      "expression": "Block[{mu, nu, ro, si, aa}, gYGGS Y0 FS[G, mu, nu, aa] FS[G, mu, nu, aa] + gYGGP/2 Y0 Eps[mu, nu, ro, si] FS[G, mu, nu, aa] FS[G, ro, si, aa]]",
      "delayed": true
    },
    {
      "name": "LDMsimp",
      "expression": "LXdkin + LXrkin + LXckin + LY0kin + LY1kin + LY0DM + LY0SM + LY1DM + LY1SM + LXrY0 + LXcY0 + LXcY1",
      "delayed": true
    },
    {
      "name": "LDMsimpTopEFT",
      "expression": "LXdkin + LXrkin + LXckin + LY0kin + LY1kin + LY0DM + LY1DM + LY1SM + LXrY0 + LXcY0 + LXcY1 + LY0GG",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper, the schema, the renderer, and `SM.fr`. No cached or reference `.fr` model file for DMsimp exists here, and I opened none.

## New-physics content found in the paper

- **Sec. 2, Eq. (1)–(2)**: DM particle χ (Dirac fermion), mediator Y0 (spin-0, scalar/pseudoscalar) and Y1 (spin-1, vector/axial-vector). Both mediators are neutral colour singlets.
- **Sec. 2**: "the implementation of the model is flexible to allow a real or complex scalar" DM ⇒ two more DM states, Xr (real) and Xc (complex).
- **Eq. (2)**: the axial coupling to the bottom quark, fixed to `-gAt`, to cancel the gauge anomaly.
- **Eq. (3)**: the infinite-top-mass (top-EFT) operators `Y0 G G` and `Y0 G G~`, with the paper's own coefficients `aS/(12 Pi vev)` and `aS/(8 Pi vev)`.
- **Tables 1–2**: mass and width benchmarks. I use the "resonant" point: mediator 200 GeV, DM 50 GeV, widths 5.17 GeV.

## Self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L/B sum | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LXdkin (kin) | Xdbar Ga DC[Xd] | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | none in model | 0 | n/a | self-conjugate (Hermitian) |
| LXdkin (mass) | Xdbar Xd | 3 | MXd | 1 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian |
| LXrkin | del[Xr] del[Xr]; Xr Xr | 4; 2 | 1; MXr^2 | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field |
| LXckin | DC[Xcbar] DC[Xc]; Xcbar Xc | 4; 2 | 1; MXc^2 | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian |
| LY0kin | del[Y0] del[Y0]; Y0 Y0 | 4; 2 | 1; MY0^2 | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field |
| LY1kin | FS[Y1] FS[Y1]; Y1 Y1 | 4; 2 | 1; MY1^2 | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field |
| LY0DM | Xdbar Xd Y0; Xdbar Ga[5] Xd Y0 | 4 | gSXd, gPXd | 0 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian (the `I` in front of gPXd makes `I Xdbar.Ga[5].Xd` Hermitian) |
| LY0SM | tbar t Y0; tbar Ga[5] t Y0 | 4 | yt0/Sqrt[2] gSt, gPt | 0 | n/a | −2/3+2/3+0 = 0 | n/a (mass-basis fields carry only Q in SM.fr) | singlet, mass basis as in Eq.(1) | 3⊗3bar = 1 | none | 0 | n/a | Hermitian |
| LY1DM | Xdbar Ga[mu] Xd Y1 | 4 | gVXd, gAXd | 0 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian |
| LY1SM | tbar Ga[mu] t Y1; bbar Ga[mu] Ga[5] b Y1 | 4 | gVt, gAt, −gAt | 0 | n/a | 0 (and −1/3+1/3+0 = 0) | n/a | singlet, mass basis as in Eq.(2) | 3⊗3bar = 1 | none | 0 | n/a | Hermitian |
| LXrY0 | Y0 Xr Xr | 3 | gSXr | 1 (GeV) | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real fields |
| LXcY0 | Y0 Xcbar Xc | 3 | gSXc | 1 (GeV) | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian |
| LXcY1 | Y1 Xcbar del[Xc] | 4 | gVXc | 0 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Hermitian (the `I` and the antisymmetric current) |
| LY0GG | FS[G] FS[G] Y0 (and dual) | 5 | gYGGS = aS gSt/(12 Pi vev), gYGGP = aS gPt/(8 Pi vev) | −1 (GeV^-1) | d−4 = 1; the paper's Eq.(3) uses 1/vev, not a free Λ, so no cutoff parameter is invented — the Description states dimension −1 and units GeV^-1 | 0 | 0 | singlet | 8⊗8 = 1 | none | 0 | n/a | Hermitian |

Kinetic + mass term rows above exist for every new class: Xd, Xr, Xc, Y0, Y1. All five are in the total `LDMsimp`.

`SelfConjugate -> True` classes: **Y0, Y1, Xr** — each carries no `QuantumNumbers`.

Reference or cached model file read: **none**.

Two notes on choices. There is no new U(1) gauge group in this model, so rule 5 does not apply; the mediator couplings are written in the mass basis exactly as Eq. (1)–(2) do. The top-EFT operator of Eq. (3) replaces the resolved top loop, so adding it to the main sum would double count; I put it in a separate total `LDMsimpTopEFT`.

```json
{
  "model_name": "DMsimp_gen",
  "info": {
    "authors": ["O. Mattelaer", "E. Vryonidou"],
    "version": "1.0",
    "date": "03. 08. 2015",
    "institutions": ["IPPP, Durham University", "CP3, Universite catholique de Louvain"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "vevs": [],
  "parameters": [
    {
      "name": "gSXd",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Scalar coupling of the spin-0 mediator Y0 to the Dirac dark matter Xd, gS_DM of Eq.(1); benchmark value 1"
    },
    {
      "name": "gPXd",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "Pseudoscalar coupling of Y0 to the Dirac dark matter Xd, gP_DM of Eq.(1); 0 in the scalar benchmark, 1 in the pseudoscalar benchmark"
    },
    {
      "name": "gSt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "description": "Scalar coupling of Y0 to the top quark, gS_t of Eq.(1), normalised by the top Yukawa yt/Sqrt[2]; benchmark value 1"
    },
    {
      "name": "gPt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 4,
      "interaction_order": ["NP", 1],
      "description": "Pseudoscalar coupling of Y0 to the top quark, gP_t of Eq.(1); 0 in the scalar benchmark, 1 in the pseudoscalar benchmark"
    },
    {
      "name": "gVXd",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "description": "Vector coupling of the spin-1 mediator Y1 to the Dirac dark matter Xd, gV_DM of Eq.(2); benchmark value 1"
    },
    {
      "name": "gAXd",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 6,
      "interaction_order": ["NP", 1],
      "description": "Axial-vector coupling of Y1 to the Dirac dark matter Xd, gA_DM of Eq.(2); 0 in the vector benchmark, 1 in the axial-vector benchmark"
    },
    {
      "name": "gVt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 7,
      "interaction_order": ["NP", 1],
      "description": "Vector coupling of Y1 to the top quark, gV_t of Eq.(2); benchmark value 1"
    },
    {
      "name": "gAt",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "DMINPUTS",
      "order_block": 8,
      "interaction_order": ["NP", 1],
      "description": "Axial-vector coupling of Y1 to the top quark, gA_t of Eq.(2); the bottom quark takes the opposite coupling -gA_t to cancel the gauge anomaly"
    },
    {
      "name": "gSXr",
      "parameter_type": "External",
      "value": "100.",
      "block_name": "DMINPUTS",
      "order_block": 9,
      "interaction_order": ["NP", 1],
      "description": "Trilinear coupling of Y0 to the real scalar dark matter Xr [GeV], mass dimension 1, units GeV; Sec. 2 states the implementation also allows a real or complex scalar dark matter"
    },
    {
      "name": "gSXc",
      "parameter_type": "External",
      "value": "100.",
      "block_name": "DMINPUTS",
      "order_block": 10,
      "interaction_order": ["NP", 1],
      "description": "Trilinear coupling of Y0 to the complex scalar dark matter Xc [GeV], mass dimension 1, units GeV; Sec. 2 states the implementation also allows a real or complex scalar dark matter"
    },
    {
      "name": "gVXc",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "DMINPUTS",
      "order_block": 11,
      "interaction_order": ["NP", 1],
      "description": "Vector coupling of Y1 to the conserved current of the complex scalar dark matter Xc; dimensionless, benchmark value 1"
    },
    {
      "name": "yt0",
      "parameter_type": "Internal",
      "value": "ymt/vev",
      "interaction_order": ["QED", 1],
      "tex": "y_t",
      "description": "Top Yukawa coupling yt = mt/v used to normalise the Y0 coupling to the top quark in Eq.(1)"
    },
    {
      "name": "gYGGS",
      "parameter_type": "Internal",
      "value": "aS*gSt/(12*Pi*vev)",
      "description": "Effective Y0-gluon-gluon coupling in the infinite top mass limit, aS gS_t/(12 Pi v) of Eq.(3); mass dimension -1, units GeV^-1"
    },
    {
      "name": "gYGGP",
      "parameter_type": "Internal",
      "value": "aS*gPt/(8*Pi*vev)",
      "description": "Effective Y0-gluon-gluon CP-odd coupling in the infinite top mass limit, aS gP_t/(8 Pi v) of Eq.(3); mass dimension -1, units GeV^-1"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Xd",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MXd", "value": "50."},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 52,
      "particle_name": "xd",
      "antiparticle_name": "xd~",
      "full_name": "Dirac fermion dark matter",
      "propagator_label": "Xd",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "Xr",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MXr", "value": "50."},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 51,
      "particle_name": "xr",
      "full_name": "Real scalar dark matter",
      "propagator_label": "Xr",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "Xc",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MXc", "value": "50."},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 53,
      "particle_name": "xc",
      "antiparticle_name": "xc~",
      "full_name": "Complex scalar dark matter",
      "propagator_label": "Xc",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "Y0",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MY0", "value": "200."},
      "width": {"sym": "WY0", "value": "5.17"},
      "quantum_numbers": {},
      "pdg": 54,
      "particle_name": "y0",
      "full_name": "Spin-0 s-channel mediator",
      "propagator_label": "Y0",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Y1",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MY1", "value": "200."},
      "width": {"sym": "WY1", "value": "5.17"},
      "quantum_numbers": {},
      "pdg": 55,
      "particle_name": "y1",
      "full_name": "Spin-1 s-channel mediator",
      "propagator_label": "Y1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LXdkin",
      "expression": "Block[{mu}, I Xdbar.Ga[mu].DC[Xd, mu] - MXd Xdbar.Xd]",
      "delayed": true
    },
    {
      "name": "LXrkin",
      "expression": "Block[{mu}, 1/2 del[Xr, mu] del[Xr, mu] - 1/2 MXr^2 Xr Xr]",
      "delayed": true
    },
    {
      "name": "LXckin",
      "expression": "Block[{mu}, DC[Xcbar, mu] DC[Xc, mu] - MXc^2 Xcbar Xc]",
      "delayed": true
    },
    {
      "name": "LY0kin",
      "expression": "Block[{mu}, 1/2 del[Y0, mu] del[Y0, mu] - 1/2 MY0^2 Y0 Y0]",
      "delayed": true
    },
    {
      "name": "LY1kin",
      "expression": "Block[{mu, nu}, -1/4 FS[Y1, mu, nu] FS[Y1, mu, nu] + 1/2 MY1^2 Y1[mu] Y1[mu]]",
      "delayed": true
    },
    {
      "name": "LY0DM",
      "expression": "gSXd Xdbar.Xd Y0 + I gPXd Xdbar.Ga[5].Xd Y0",
      "delayed": true
    },
    {
      "name": "LY0SM",
      "expression": "yt0/Sqrt[2] (gSt tbar.t + I gPt tbar.Ga[5].t) Y0",
      "delayed": true
    },
    {
      "name": "LY1DM",
      "expression": "Block[{mu}, (gVXd Xdbar.Ga[mu].Xd + gAXd Xdbar.Ga[mu].Ga[5].Xd) Y1[mu]]",
      "delayed": true
    },
    {
      "name": "LY1SM",
      "expression": "Block[{mu}, (gVt tbar.Ga[mu].t + gAt tbar.Ga[mu].Ga[5].t - gAt bbar.Ga[mu].Ga[5].b) Y1[mu]]",
      "delayed": true
    },
    {
      "name": "LXrY0",
      "expression": "1/2 gSXr Y0 Xr Xr",
      "delayed": true
    },
    {
      "name": "LXcY0",
      "expression": "gSXc Y0 Xcbar Xc",
      "delayed": true
    },
    {
      "name": "LXcY1",
      "expression": "Block[{mu}, I gVXc Y1[mu] (Xcbar del[Xc, mu] - del[Xcbar, mu] Xc)]",
      "delayed": true
    },
    {
      "name": "LY0GG",
      "expression": "Block[{mu, nu, ro, si, aa}, gYGGS Y0 FS[G, mu, nu, aa] FS[G, mu, nu, aa] + gYGGP/2 Y0 Eps[mu, nu, ro, si] FS[G, mu, nu, aa] FS[G, ro, si, aa]]",
      "delayed": true
    },
    {
      "name": "LDMsimp",
      "expression": "LXdkin + LXrkin + LXckin + LY0kin + LY1kin + LY0DM + LY0SM + LY1DM + LY1SM + LXrY0 + LXcY0 + LXcY1",
      "delayed": true
    },
    {
      "name": "LDMsimpTopEFT",
      "expression": "LXdkin + LXrkin + LXckin + LY0kin + LY1kin + LY0DM + LY1DM + LY1SM + LXrY0 + LXcY0 + LXcY1 + LY0GG",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```