I'll start by reading the paper and the schema.
Let me read the rest of the paper, especially the appendices about the FeynRules implementation.
I read the paper end to end (Secs. 2–6, Tables 1–7, Appendices A–D). No cached or reference `.fr` file for this model was opened — only `2007.03701.txt`, `frmodel.py`, `render.py` and `SM.fr`.

## Model content extracted

The paper adds **one heavy neutral lepton** (Dirac, Eq. 2.3 / App. B; Sec. 6 states "we will assume a Dirac HNL") plus the **effective meson fields** that carry the operators of Sec. 3. The mesons are genuinely new fields: `SM.fr` has no hadron fields, and Eqs. (3.12)–(3.50) and Table 7 are written directly in terms of `pi0, pi+, eta, eta', K+, K0, D+, Ds+, rho0, rho+, omega, phi, K*+`. All of them are declared as separate particle classes.

## Mandatory self-audit table

| term name | fields in the monomial | d | coupling symbol | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | Lepton number sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LN4kin | `N4bar.Ga[mu].DC[N4,mu]` | 4 | 1 | 0 | n/a | 0+0=0 | none declared → 0 | singlet (no SU2 index) | singlet | none | −1+1=0 | n/a (Dirac) | self-conjugate |
| LN4kin (mass) | `N4bar.N4` | 3 | `MN4` | 1 ✓ | n/a | 0 | 0 | singlet | singlet | none | −1+1=0 | n/a | self-conjugate |
| LmesonPSkin0 | `del[pi0,mu] del[pi0,mu]`, `Mpi0^2 pi0^2` (also eta, etap) | 4 / 2 | 1 / `M^2` | 0 / 2 ✓ | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field, self-conjugate |
| LmesonPSkinC | `del[pipbar,mu] del[pip,mu]`, `Mpip^2 pipbar pip` (also Kp, K0, Dp, Dsp) | 4 / 2 | 1 / `M^2` | 0 / 2 ✓ | n/a | +1−1=0 | 0 | singlet | singlet | none | 0 | n/a | manifestly hermitian |
| LmesonVkin0 | `FS[rho0,mu,nu]^2`, `Mrho^2 rho0[mu] rho0[mu]` (also omega, phiM) | 4 / 2 | 1 / `M^2` | 0 / 2 ✓ | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field, self-conjugate |
| LmesonVkinC | `FS[rhopbar]FS[rhop]`, `Mrhop^2 rhopbar[mu] rhop[mu]` (also Kstarp) | 4 / 2 | 1 / `M^2` | 0 / 2 ✓ | n/a | +1−1=0 | 0 | singlet | singlet | none | 0 | n/a | manifestly hermitian |
| LNCP (NN) | `N4bar.Ga[mu].ProjM.N4 del[pi0,mu]` (η, η′ alike) | 5 | `Gf fpi CNN` | −2+1=−1 ✓ | carried by `Gf` (GeV⁻²) × `fpi` (GeV); no new cutoff | 0+0+0=0 | 0 | singlet | singlet | none | −1+1=0 | n/a | `(n̄γ^μP_L n)†=n̄γ^μP_L n`: self-hermitian |
| LNCP (Nν) | `N4bar.Ga[mu].ProjM.vl[ff] del[pi0,mu]` | 5 | `Gf fpi Conjugate[UaN[ff]]` | −1 ✓ | via `Gf`×`fpi` | 0 | 0 | singlet | singlet | none | −1+1=0 | n/a | h.c. partner `UaN[ff] vlbar.Ga.ProjM.N4` written explicitly in same sum |
| LCCP | `lbar[ff].Ga[mu].ProjM.N4 del[pipbar,mu]` (K, D, Ds alike) | 5 | `Sqrt[2] Gf CKM[1,1] fpi UaN[ff]` | −1 ✓ | via `Gf`×`fpi` | +1+0−1=0 | 0 | singlet | singlet | none | +1(ℓ̄:−1, N:+1)→0 | n/a | `HC[tmp]` |
| LNCV | `rho0[mu] N4bar.Ga[mu].ProjM.N4` (ω, φ alike) | 4 | `Gf grho frho CNN` | −2+2=0 ✓ | n/a (d=4) | 0 | 0 | singlet | singlet | none | 0 | n/a | self-hermitian sum (Nν and νN both present) |
| LCCV | `rhopbar[mu] lbar[ff].Ga[mu].ProjM.N4` (K*± alike) | 4 | `Sqrt[2] Gf CKM[1,1] frho UaN[ff]` | 0 ✓ | n/a | +1+0−1=0 | 0 | singlet | singlet | none | −1+1=0 | n/a | `HC[tmp]` |
| LSL | `lbar[ff].Ga[mu].ProjM.N4 del[pi0,mu] Kpbar` (+ K0π±, D+K0) | 6 | `Sqrt[2] Gf CKM fpKpi0` | −2 ✓ | via `Gf` (GeV⁻²); form factors dimensionless | +1+0+0−1=0 | 0 | singlet | singlet | none | −1+1=0 | n/a | `HC[tmp]` |
| LNWZ (W) | `W[mu] N4bar.Ga[mu].ProjM.l[ff]` | 4 | `gw Conjugate[UaN[ff]]/Sqrt[2]` | 0 ✓ | n/a | +1+0−1=0 | 0 | physical mass basis, singlet | singlet | none | −1+1=0 | n/a | `HC[tmp]` |
| LNWZ (Z) | `Z[mu] N4bar.Ga[mu].ProjM.N4`, `Z[mu] N4bar.Ga[mu].ProjM.vl[ff]` | 4 | `gw CNN/(4 cw)`, `gw Conjugate[UaN[ff]]/(4 cw)` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Nν and νN both written: self-hermitian |

Kinetic + mass confirmation, one row per new class: `N4` → LN4kin; `pi0, eta, etap` → LmesonPSkin0; `pip, Kp, K0, Dp, Dsp` → LmesonPSkinC; `rho0, omega, phiM` → LmesonVkin0; `rhop, Kstarp` → LmesonVkinC. All five free-field terms are summed into `LHNLfree`, which enters the total `LHNL`.

`SelfConjugate -> True` classes: `pi0`, `eta`, `etap`, `rho0`, `omega`, `phiM`. None of them carries `QuantumNumbers` (all are electrically neutral real fields).

Reference or cached model file read: **none**.

Two notes on conventions. First, all operators of Sec. 3 are written after electroweak symmetry breaking in the physical mass basis, so only `Q` is a good quantum number; no field in these terms carries a declared hypercharge, and every `Y` sum is therefore 0. Second, no new EFT cutoff parameter is declared: the paper's suppression is `G_F` (external SM parameter in `SM.fr`, GeV⁻²) times the meson decay constants (GeV for pseudoscalars, GeV² for vectors, Table 1), so every dimensionful coefficient has an explicit physical meaning, units, and a measured value in its `Description`. The derivative operators are written after one integration by parts, which moves `∂_μ` from the leptonic current onto the meson field; this is equivalent up to a total derivative and gives the Feynman rules of Table 7.

```json
{
  "model_name": "HNLs_gen",
  "info": {
    "authors": [
      "P. Coloma",
      "E. Fernandez-Martinez",
      "M. Gonzalez-Lopez",
      "J. Hernandez-Garcia",
      "Z. Pavlovic"
    ],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": [
      "IFIC, Universidad de Valencia & CSIC",
      "IFT UAM/CSIC, Madrid",
      "Departamento de Fisica Teorica, UAM, Madrid",
      "ELTE Eotvos Lorand University, Budapest",
      "Fermi National Accelerator Laboratory"
    ],
    "emails": [
      "pilar.coloma@ift.csic.es",
      "enrique.fernandez-martinez@uam.es",
      "manuel.gonzalezl@uam.es",
      "garcia.josu.hernandez@ttk.elte.hu",
      "zarko@fnal.gov"
    ]
  },
  "interaction_order_hierarchy": [
    ["QCD", 1],
    ["QED", 2],
    ["NP", 1]
  ],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Ue4",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "HNLMIX",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "Subscript[U,e4]",
      "description": "Mixing of the HNL with the electron neutrino, U_{e4}, Eq.(2.5)"
    },
    {
      "name": "Umu4",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "HNLMIX",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "tex": "Subscript[U,\\[Mu]4]",
      "description": "Mixing of the HNL with the muon neutrino, U_{mu 4}, Eq.(2.5)"
    },
    {
      "name": "Uta4",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "HNLMIX",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "tex": "Subscript[U,\\[Tau]4]",
      "description": "Mixing of the HNL with the tau neutrino, U_{tau 4}, Eq.(2.5)"
    },
    {
      "name": "UaN",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "UaN[1]", "rhs": "Ue4"},
        {"lhs": "UaN[2]", "rhs": "Umu4"},
        {"lhs": "UaN[3]", "rhs": "Uta4"}
      ],
      "parameter_name": {},
      "tex": "Subscript[U,\\[Alpha]4]",
      "description": "Active-heavy mixing vector U_{alpha 4} in the 3+1 scheme, App.B"
    },
    {
      "name": "CNN",
      "parameter_type": "Internal",
      "value": "Ue4^2 + Umu4^2 + Uta4^2",
      "interaction_order": ["NP", 2],
      "tex": "Subscript[C,44]",
      "description": "C_44 = sum_alpha |U_{alpha 4}|^2, neutral-current coefficient, Eq.(2.7) and Eq.(5.3)"
    },
    {
      "name": "fpi",
      "parameter_type": "External",
      "value": "0.130",
      "block_name": "MESONDC",
      "order_block": 1,
      "tex": "Subscript[f,\\[Pi]]",
      "description": "Pion decay constant [GeV], Tab.1, Eq.(3.1)"
    },
    {
      "name": "fK",
      "parameter_type": "External",
      "value": "0.156",
      "block_name": "MESONDC",
      "order_block": 2,
      "tex": "Subscript[f,K]",
      "description": "Kaon decay constant [GeV], Tab.1"
    },
    {
      "name": "fD",
      "parameter_type": "External",
      "value": "0.212",
      "block_name": "MESONDC",
      "order_block": 3,
      "tex": "Subscript[f,D]",
      "description": "D meson decay constant [GeV], Tab.1"
    },
    {
      "name": "fDs",
      "parameter_type": "External",
      "value": "0.249",
      "block_name": "MESONDC",
      "order_block": 4,
      "tex": "Subscript[f,Ds]",
      "description": "Ds meson decay constant [GeV], Tab.1"
    },
    {
      "name": "f0",
      "parameter_type": "External",
      "value": "0.148",
      "block_name": "MESONDC",
      "order_block": 5,
      "tex": "Subscript[f,0]",
      "description": "eta_0 singlet decay constant [GeV], Tab.1"
    },
    {
      "name": "f8",
      "parameter_type": "External",
      "value": "0.165",
      "block_name": "MESONDC",
      "order_block": 6,
      "tex": "Subscript[f,8]",
      "description": "eta_8 octet decay constant [GeV], Tab.1"
    },
    {
      "name": "th0",
      "parameter_type": "External",
      "value": "-0.1204277",
      "block_name": "MESONDC",
      "order_block": 7,
      "tex": "Subscript[\\[Theta],0]",
      "description": "eta-eta' mixing angle theta_0 [rad] (-6.9 degrees), Tab.1, Eq.(3.16)"
    },
    {
      "name": "th8",
      "parameter_type": "External",
      "value": "-0.3700098",
      "block_name": "MESONDC",
      "order_block": 8,
      "tex": "Subscript[\\[Theta],8]",
      "description": "eta-eta' mixing angle theta_8 [rad] (-21.2 degrees), Tab.1, Eq.(3.16)"
    },
    {
      "name": "frho",
      "parameter_type": "External",
      "value": "0.171",
      "block_name": "MESONDC",
      "order_block": 9,
      "tex": "Subscript[f,\\[Rho]]",
      "description": "rho meson decay constant [GeV^2], Tab.1, Eq.(3.2), App.C"
    },
    {
      "name": "fome",
      "parameter_type": "External",
      "value": "0.155",
      "block_name": "MESONDC",
      "order_block": 10,
      "tex": "Subscript[f,\\[Omega]]",
      "description": "omega meson decay constant [GeV^2], Tab.1, App.C"
    },
    {
      "name": "fphi",
      "parameter_type": "External",
      "value": "0.232",
      "block_name": "MESONDC",
      "order_block": 11,
      "tex": "Subscript[f,\\[Phi]]",
      "description": "phi meson decay constant [GeV^2], Tab.1, App.C"
    },
    {
      "name": "fKst",
      "parameter_type": "External",
      "value": "0.178",
      "block_name": "MESONDC",
      "order_block": 12,
      "tex": "Subscript[f,K*]",
      "description": "K* meson decay constant [GeV^2], Tab.1, Eq.(C.5)"
    },
    {
      "name": "feta",
      "parameter_type": "Internal",
      "value": "Cos[th8] f8/Sqrt[3] + Sin[th0] f0/Sqrt[6]",
      "tex": "Subscript[f,\\[Eta]]",
      "description": "Effective eta decay constant [GeV] = cos(th8) f8/Sqrt[3] + sin(th0) f0/Sqrt[6], Eq.(3.19), Eq.(5.2); numerically 0.0816 GeV"
    },
    {
      "name": "fetap",
      "parameter_type": "Internal",
      "value": "Sin[th8] f8/Sqrt[3] - Cos[th0] f0/Sqrt[6]",
      "tex": "Subscript[f,\\[Eta]']",
      "description": "Effective eta' decay constant [GeV] = sin(th8) f8/Sqrt[3] - cos(th0) f0/Sqrt[6], Eq.(3.20), Eq.(5.2); numerically -0.0946 GeV"
    },
    {
      "name": "grho",
      "parameter_type": "Internal",
      "value": "1 - 2 sw^2",
      "tex": "Subscript[g,\\[Rho]]",
      "description": "Neutral-current coefficient of the rho0, dimensionless, Tab.4 and Eq.(3.36)"
    },
    {
      "name": "gome",
      "parameter_type": "Internal",
      "value": "-2 sw^2/3",
      "tex": "Subscript[g,\\[Omega]]",
      "description": "Neutral-current coefficient of the omega, dimensionless, Tab.4 and Eq.(3.37)"
    },
    {
      "name": "gphi",
      "parameter_type": "Internal",
      "value": "-Sqrt[2] (1/2 - 2 sw^2/3)",
      "tex": "Subscript[g,\\[Phi]]",
      "description": "Neutral-current coefficient of the phi, dimensionless, Tab.4 and Eq.(3.38)"
    },
    {
      "name": "fpKpi0",
      "parameter_type": "External",
      "value": "0.9749",
      "block_name": "FORMFAC",
      "order_block": 1,
      "description": "Constant vector form factor f_+ for K+ -> pi0 l N at <q^2>, dimensionless, Tab.3 and App.D"
    },
    {
      "name": "fmKpi0",
      "parameter_type": "External",
      "value": "0.1151",
      "block_name": "FORMFAC",
      "order_block": 2,
      "description": "Constant scalar form factor f_- for K+ -> pi0 l N at <q^2>, dimensionless, from Eq.(3.51) with Tab.3"
    },
    {
      "name": "fpK0pi",
      "parameter_type": "External",
      "value": "0.9749",
      "block_name": "FORMFAC",
      "order_block": 3,
      "description": "Constant vector form factor f_+ for K0 -> pi- l N at <q^2>, dimensionless, Tab.3 and App.D"
    },
    {
      "name": "fmK0pi",
      "parameter_type": "External",
      "value": "0.1644",
      "block_name": "FORMFAC",
      "order_block": 4,
      "description": "Constant scalar form factor f_- for K0 -> pi- l N at <q^2>, dimensionless, from Eq.(3.51) with Tab.3"
    },
    {
      "name": "fpDK",
      "parameter_type": "External",
      "value": "0.7647",
      "block_name": "FORMFAC",
      "order_block": 5,
      "description": "Constant vector form factor f_+ for D+ -> K0bar l N at <q^2>, dimensionless, Tab.2 and App.D"
    },
    {
      "name": "fmDK",
      "parameter_type": "External",
      "value": "0.2502",
      "block_name": "FORMFAC",
      "order_block": 6,
      "description": "Constant scalar form factor f_- for D+ -> K0bar l N at <q^2>, dimensionless, from Eq.(3.51) with Tab.2"
    },
    {
      "name": "lamKpip",
      "parameter_type": "External",
      "value": "0.0297",
      "block_name": "FORMFAC",
      "order_block": 7,
      "description": "Slope lambda_+ of the linear K+ -> pi0 form factor, dimensionless, Eq.(3.52), Tab.3"
    },
    {
      "name": "lamKpi0",
      "parameter_type": "External",
      "value": "0.0195",
      "block_name": "FORMFAC",
      "order_block": 8,
      "description": "Slope lambda_0 of the linear K+ -> pi0 form factor, dimensionless, Eq.(3.52), Tab.3"
    },
    {
      "name": "lamK0pip",
      "parameter_type": "External",
      "value": "0.0282",
      "block_name": "FORMFAC",
      "order_block": 9,
      "description": "Slope lambda_+ of the linear K0 -> pi- form factor, dimensionless, Eq.(3.52), Tab.3"
    },
    {
      "name": "lamK0pi0",
      "parameter_type": "External",
      "value": "0.0138",
      "block_name": "FORMFAC",
      "order_block": 10,
      "description": "Slope lambda_0 of the linear K0 -> pi- form factor, dimensionless, Eq.(3.52), Tab.3"
    },
    {
      "name": "cpDK",
      "parameter_type": "External",
      "value": "-0.066",
      "block_name": "FORMFAC",
      "order_block": 11,
      "description": "Coefficient c_+ of the pole parametrization for D -> K, dimensionless, Eq.(3.53), Tab.2"
    },
    {
      "name": "c0DK",
      "parameter_type": "External",
      "value": "-2.084",
      "block_name": "FORMFAC",
      "order_block": 12,
      "description": "Coefficient c_0 of the pole parametrization for D -> K, dimensionless, Eq.(3.54), Tab.2"
    },
    {
      "name": "MDsst",
      "parameter_type": "External",
      "value": "2.1122",
      "block_name": "FORMFAC",
      "order_block": 13,
      "description": "Pole mass M_{D*s} [GeV] of the D -> K vector form factor, Eq.(3.53)"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "N4",
      "self_conjugate": false,
      "mass": {"sym": "MN4", "value": "1."},
      "width": {"sym": "WN4", "value": "1.*^-20"},
      "quantum_numbers": {"LeptonNumber": "1"},
      "pdg": 9900012,
      "particle_name": "N4",
      "antiparticle_name": "N4~",
      "full_name": "Heavy neutral lepton",
      "propagator_label": "N4",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "pi0",
      "self_conjugate": true,
      "mass": {"sym": "Mpi0", "value": "0.1349768"},
      "width": {"sym": "Wpi0", "value": "7.81*^-9"},
      "pdg": 111,
      "particle_name": "pi0",
      "full_name": "Neutral pion",
      "propagator_label": "pi0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "pip",
      "self_conjugate": false,
      "mass": {"sym": "Mpip", "value": "0.13957039"},
      "width": {"sym": "Wpip", "value": "2.5284*^-17"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 211,
      "particle_name": "pi+",
      "antiparticle_name": "pi-",
      "full_name": "Charged pion",
      "propagator_label": "pi",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "eta",
      "self_conjugate": true,
      "mass": {"sym": "Meta", "value": "0.547862"},
      "width": {"sym": "Weta", "value": "1.31*^-6"},
      "pdg": 221,
      "particle_name": "eta",
      "full_name": "eta meson",
      "propagator_label": "eta",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "etap",
      "self_conjugate": true,
      "mass": {"sym": "Metap", "value": "0.95778"},
      "width": {"sym": "Wetap", "value": "1.88*^-4"},
      "pdg": 331,
      "particle_name": "eta'",
      "full_name": "eta prime meson",
      "propagator_label": "etap",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "Kp",
      "self_conjugate": false,
      "mass": {"sym": "MKp", "value": "0.493677"},
      "width": {"sym": "WKp", "value": "5.317*^-17"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 321,
      "particle_name": "K+",
      "antiparticle_name": "K-",
      "full_name": "Charged kaon",
      "propagator_label": "K",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "K0",
      "self_conjugate": false,
      "mass": {"sym": "MK0", "value": "0.497611"},
      "width": {"sym": "WK0", "value": "1.*^-16"},
      "pdg": 311,
      "particle_name": "K0",
      "antiparticle_name": "K0~",
      "full_name": "Neutral kaon",
      "propagator_label": "K0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 106,
      "class_name": "Dp",
      "self_conjugate": false,
      "mass": {"sym": "MDp", "value": "1.86966"},
      "width": {"sym": "WDp", "value": "6.33*^-13"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 411,
      "particle_name": "D+",
      "antiparticle_name": "D-",
      "full_name": "Charged D meson",
      "propagator_label": "D",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 107,
      "class_name": "Dsp",
      "self_conjugate": false,
      "mass": {"sym": "MDs", "value": "1.96835"},
      "width": {"sym": "WDs", "value": "1.305*^-12"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 431,
      "particle_name": "Ds+",
      "antiparticle_name": "Ds-",
      "full_name": "Charged Ds meson",
      "propagator_label": "Ds",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "rho0",
      "self_conjugate": true,
      "mass": {"sym": "Mrho", "value": "0.77526"},
      "width": {"sym": "Wrho", "value": "0.1478"},
      "pdg": 113,
      "particle_name": "rho0",
      "full_name": "Neutral rho meson",
      "propagator_label": "rho0",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "rhop",
      "self_conjugate": false,
      "mass": {"sym": "Mrhop", "value": "0.77511"},
      "width": {"sym": "Wrhop", "value": "0.1491"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 213,
      "particle_name": "rho+",
      "antiparticle_name": "rho-",
      "full_name": "Charged rho meson",
      "propagator_label": "rho",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 102,
      "class_name": "omega",
      "self_conjugate": true,
      "mass": {"sym": "Mome", "value": "0.78266"},
      "width": {"sym": "Wome", "value": "0.00868"},
      "pdg": 223,
      "particle_name": "omega",
      "full_name": "omega meson",
      "propagator_label": "omega",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 103,
      "class_name": "phiM",
      "self_conjugate": true,
      "mass": {"sym": "Mphi", "value": "1.019461"},
      "width": {"sym": "Wphi", "value": "0.004249"},
      "pdg": 333,
      "particle_name": "phi",
      "full_name": "phi meson",
      "propagator_label": "phi",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 104,
      "class_name": "Kstarp",
      "self_conjugate": false,
      "mass": {"sym": "MKst", "value": "0.89167"},
      "width": {"sym": "WKst", "value": "0.0514"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 323,
      "particle_name": "K*+",
      "antiparticle_name": "K*-",
      "full_name": "Charged K star meson",
      "propagator_label": "Kst",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LN4kin",
      "expression": "Block[{mu}, I N4bar.Ga[mu].DC[N4, mu] - MN4 N4bar.N4]",
      "delayed": true
    },
    {
      "name": "LmesonPSkin0",
      "expression": "Block[{mu}, 1/2 del[pi0, mu] del[pi0, mu] - 1/2 Mpi0^2 pi0^2 + 1/2 del[eta, mu] del[eta, mu] - 1/2 Meta^2 eta^2 + 1/2 del[etap, mu] del[etap, mu] - 1/2 Metap^2 etap^2]",
      "delayed": true
    },
    {
      "name": "LmesonPSkinC",
      "expression": "Block[{mu}, del[pipbar, mu] del[pip, mu] - Mpip^2 pipbar pip + del[Kpbar, mu] del[Kp, mu] - MKp^2 Kpbar Kp + del[K0bar, mu] del[K0, mu] - MK0^2 K0bar K0 + del[Dpbar, mu] del[Dp, mu] - MDp^2 Dpbar Dp + del[Dspbar, mu] del[Dsp, mu] - MDs^2 Dspbar Dsp]",
      "delayed": true
    },
    {
      "name": "LmesonVkin0",
      "expression": "Block[{mu, nu}, -1/4 FS[rho0, mu, nu] FS[rho0, mu, nu] + 1/2 Mrho^2 rho0[mu] rho0[mu] - 1/4 FS[omega, mu, nu] FS[omega, mu, nu] + 1/2 Mome^2 omega[mu] omega[mu] - 1/4 FS[phiM, mu, nu] FS[phiM, mu, nu] + 1/2 Mphi^2 phiM[mu] phiM[mu]]",
      "delayed": true
    },
    {
      "name": "LmesonVkinC",
      "expression": "Block[{mu, nu}, -1/2 FS[rhopbar, mu, nu] FS[rhop, mu, nu] + Mrhop^2 rhopbar[mu] rhop[mu] - 1/2 FS[Kstarpbar, mu, nu] FS[Kstarp, mu, nu] + MKst^2 Kstarpbar[mu] Kstarp[mu]]",
      "delayed": true
    },
    {
      "name": "LHNLfree",
      "expression": "LN4kin + LmesonPSkin0 + LmesonPSkinC + LmesonVkin0 + LmesonVkinC",
      "delayed": true
    },
    {
      "name": "LNCP",
      "expression": "Block[{mu, ff}, -1/2 Gf (fpi del[pi0, mu] + feta del[eta, mu] + fetap del[etap, mu]) (CNN N4bar.Ga[mu].ProjM.N4 + Conjugate[UaN[ff]] N4bar.Ga[mu].ProjM.vl[ff] + UaN[ff] vlbar[ff].Ga[mu].ProjM.N4 + vlbar[ff].Ga[mu].ProjM.vl[ff])]",
      "delayed": true
    },
    {
      "name": "LCCP",
      "expression": "Block[{mu, ff, tmp}, tmp = -Sqrt[2] Gf (CKM[1,1] fpi del[pipbar, mu] + CKM[1,2] fK del[Kpbar, mu] + CKM[2,1] fD del[Dpbar, mu] + CKM[2,2] fDs del[Dspbar, mu]) (UaN[ff] lbar[ff].Ga[mu].ProjM.N4 + lbar[ff].Ga[mu].ProjM.vl[ff]); tmp + HC[tmp]]",
      "delayed": true
    },
    {
      "name": "LNCV",
      "expression": "Block[{mu, ff}, -1/2 Gf (grho frho rho0[mu] + gome fome omega[mu] + gphi fphi phiM[mu]) (CNN N4bar.Ga[mu].ProjM.N4 + Conjugate[UaN[ff]] N4bar.Ga[mu].ProjM.vl[ff] + UaN[ff] vlbar[ff].Ga[mu].ProjM.N4 + vlbar[ff].Ga[mu].ProjM.vl[ff])]",
      "delayed": true
    },
    {
      "name": "LCCV",
      "expression": "Block[{mu, ff, tmp}, tmp = -Sqrt[2] Gf (CKM[1,1] frho rhopbar[mu] + CKM[1,2] fKst Kstarpbar[mu]) (UaN[ff] lbar[ff].Ga[mu].ProjM.N4 + lbar[ff].Ga[mu].ProjM.vl[ff]); tmp + HC[tmp]]",
      "delayed": true
    },
    {
      "name": "LSL",
      "expression": "Block[{mu, ff, tmp}, tmp = -I Sqrt[2] Gf (UaN[ff] lbar[ff].Ga[mu].ProjM.N4 + lbar[ff].Ga[mu].ProjM.vl[ff]) (CKM[1,2]/Sqrt[2] ((fpKpi0 + fmKpi0) del[pi0, mu] Kpbar - (fpKpi0 - fmKpi0) pi0 del[Kpbar, mu]) + CKM[1,2] ((fpK0pi + fmK0pi) del[pipbar, mu] K0bar - (fpK0pi - fmK0pi) pipbar del[K0bar, mu]) + CKM[2,2] ((fpDK + fmDK) del[K0bar, mu] Dpbar - (fpDK - fmDK) K0bar del[Dpbar, mu])); tmp + HC[tmp]]",
      "delayed": true
    },
    {
      "name": "LHNLmeson",
      "expression": "LNCP + LCCP + LNCV + LCCV + LSL",
      "delayed": true
    },
    {
      "name": "LNWZ",
      "expression": "Block[{mu, ff, tmp}, tmp = gw/Sqrt[2] W[mu] Conjugate[UaN[ff]] N4bar.Ga[mu].ProjM.l[ff]; tmp + HC[tmp] + gw/(4 cw) Z[mu] (CNN N4bar.Ga[mu].ProjM.N4 + Conjugate[UaN[ff]] N4bar.Ga[mu].ProjM.vl[ff] + UaN[ff] vlbar[ff].Ga[mu].ProjM.N4)]",
      "delayed": true
    },
    {
      "name": "LHNL",
      "expression": "LHNLfree + LHNLmeson",
      "delayed": true
    },
    {
      "name": "LHNLcollider",
      "expression": "LHNLfree + LNWZ",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper end to end (Secs. 2–6, Tables 1–7, Appendices A–D). No cached or reference `.fr` file for this model was opened — only `2007.03701.txt`, `frmodel.py`, `render.py` and `SM.fr`.

## Model content extracted

The paper adds **one heavy neutral lepton** (Dirac, Eq. 2.3 / App. B; Sec. 6 states "we will assume a Dirac HNL") plus the **effective meson fields** that carry the operators of Sec. 3. The mesons are genuinely new fields: `SM.fr` has no hadron fields, and Eqs. (3.12)–(3.50) and Table 7 are written directly in terms of `pi0, pi+, eta, eta', K+, K0, D+, Ds+, rho0, rho+, omega, phi, K*+`. All of them are declared as separate particle classes.

## Mandatory self-audit table

| term name | fields in the monomial | d | coupling symbol | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sum | Lepton number sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LN4kin | `N4bar.Ga[mu].DC[N4,mu]` | 4 | 1 | 0 | n/a | 0+0=0 | none declared → 0 | singlet (no SU2 index) | singlet | none | −1+1=0 | n/a (Dirac) | self-conjugate |
| LN4kin (mass) | `N4bar.N4` | 3 | `MN4` | 1 ✓ | n/a | 0 | 0 | singlet | singlet | none | −1+1=0 | n/a | self-conjugate |
| LmesonPSkin0 | `del[pi0,mu] del[pi0,mu]`, `Mpi0^2 pi0^2` (also eta, etap) | 4 / 2 | 1 / `M^2` | 0 / 2 ✓ | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field, self-conjugate |
| LmesonPSkinC | `del[pipbar,mu] del[pip,mu]`, `Mpip^2 pipbar pip` (also Kp, K0, Dp, Dsp) | 4 / 2 | 1 / `M^2` | 0 / 2 ✓ | n/a | +1−1=0 | 0 | singlet | singlet | none | 0 | n/a | manifestly hermitian |
| LmesonVkin0 | `FS[rho0,mu,nu]^2`, `Mrho^2 rho0[mu] rho0[mu]` (also omega, phiM) | 4 / 2 | 1 / `M^2` | 0 / 2 ✓ | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | real field, self-conjugate |
| LmesonVkinC | `FS[rhopbar]FS[rhop]`, `Mrhop^2 rhopbar[mu] rhop[mu]` (also Kstarp) | 4 / 2 | 1 / `M^2` | 0 / 2 ✓ | n/a | +1−1=0 | 0 | singlet | singlet | none | 0 | n/a | manifestly hermitian |
| LNCP (NN) | `N4bar.Ga[mu].ProjM.N4 del[pi0,mu]` (η, η′ alike) | 5 | `Gf fpi CNN` | −2+1=−1 ✓ | carried by `Gf` (GeV⁻²) × `fpi` (GeV); no new cutoff | 0+0+0=0 | 0 | singlet | singlet | none | −1+1=0 | n/a | `(n̄γ^μP_L n)†=n̄γ^μP_L n`: self-hermitian |
| LNCP (Nν) | `N4bar.Ga[mu].ProjM.vl[ff] del[pi0,mu]` | 5 | `Gf fpi Conjugate[UaN[ff]]` | −1 ✓ | via `Gf`×`fpi` | 0 | 0 | singlet | singlet | none | −1+1=0 | n/a | h.c. partner `UaN[ff] vlbar.Ga.ProjM.N4` written explicitly in same sum |
| LCCP | `lbar[ff].Ga[mu].ProjM.N4 del[pipbar,mu]` (K, D, Ds alike) | 5 | `Sqrt[2] Gf CKM[1,1] fpi UaN[ff]` | −1 ✓ | via `Gf`×`fpi` | +1+0−1=0 | 0 | singlet | singlet | none | +1(ℓ̄:−1, N:+1)→0 | n/a | `HC[tmp]` |
| LNCV | `rho0[mu] N4bar.Ga[mu].ProjM.N4` (ω, φ alike) | 4 | `Gf grho frho CNN` | −2+2=0 ✓ | n/a (d=4) | 0 | 0 | singlet | singlet | none | 0 | n/a | self-hermitian sum (Nν and νN both present) |
| LCCV | `rhopbar[mu] lbar[ff].Ga[mu].ProjM.N4` (K*± alike) | 4 | `Sqrt[2] Gf CKM[1,1] frho UaN[ff]` | 0 ✓ | n/a | +1+0−1=0 | 0 | singlet | singlet | none | −1+1=0 | n/a | `HC[tmp]` |
| LSL | `lbar[ff].Ga[mu].ProjM.N4 del[pi0,mu] Kpbar` (+ K0π±, D+K0) | 6 | `Sqrt[2] Gf CKM fpKpi0` | −2 ✓ | via `Gf` (GeV⁻²); form factors dimensionless | +1+0+0−1=0 | 0 | singlet | singlet | none | −1+1=0 | n/a | `HC[tmp]` |
| LNWZ (W) | `W[mu] N4bar.Ga[mu].ProjM.l[ff]` | 4 | `gw Conjugate[UaN[ff]]/Sqrt[2]` | 0 ✓ | n/a | +1+0−1=0 | 0 | physical mass basis, singlet | singlet | none | −1+1=0 | n/a | `HC[tmp]` |
| LNWZ (Z) | `Z[mu] N4bar.Ga[mu].ProjM.N4`, `Z[mu] N4bar.Ga[mu].ProjM.vl[ff]` | 4 | `gw CNN/(4 cw)`, `gw Conjugate[UaN[ff]]/(4 cw)` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | Nν and νN both written: self-hermitian |

Kinetic + mass confirmation, one row per new class: `N4` → LN4kin; `pi0, eta, etap` → LmesonPSkin0; `pip, Kp, K0, Dp, Dsp` → LmesonPSkinC; `rho0, omega, phiM` → LmesonVkin0; `rhop, Kstarp` → LmesonVkinC. All five free-field terms are summed into `LHNLfree`, which enters the total `LHNL`.

`SelfConjugate -> True` classes: `pi0`, `eta`, `etap`, `rho0`, `omega`, `phiM`. None of them carries `QuantumNumbers` (all are electrically neutral real fields).

Reference or cached model file read: **none**.

Two notes on conventions. First, all operators of Sec. 3 are written after electroweak symmetry breaking in the physical mass basis, so only `Q` is a good quantum number; no field in these terms carries a declared hypercharge, and every `Y` sum is therefore 0. Second, no new EFT cutoff parameter is declared: the paper's suppression is `G_F` (external SM parameter in `SM.fr`, GeV⁻²) times the meson decay constants (GeV for pseudoscalars, GeV² for vectors, Table 1), so every dimensionful coefficient has an explicit physical meaning, units, and a measured value in its `Description`. The derivative operators are written after one integration by parts, which moves `∂_μ` from the leptonic current onto the meson field; this is equivalent up to a total derivative and gives the Feynman rules of Table 7.

```json
{
  "model_name": "HNLs_gen",
  "info": {
    "authors": [
      "P. Coloma",
      "E. Fernandez-Martinez",
      "M. Gonzalez-Lopez",
      "J. Hernandez-Garcia",
      "Z. Pavlovic"
    ],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": [
      "IFIC, Universidad de Valencia & CSIC",
      "IFT UAM/CSIC, Madrid",
      "Departamento de Fisica Teorica, UAM, Madrid",
      "ELTE Eotvos Lorand University, Budapest",
      "Fermi National Accelerator Laboratory"
    ],
    "emails": [
      "pilar.coloma@ift.csic.es",
      "enrique.fernandez-martinez@uam.es",
      "manuel.gonzalezl@uam.es",
      "garcia.josu.hernandez@ttk.elte.hu",
      "zarko@fnal.gov"
    ]
  },
  "interaction_order_hierarchy": [
    ["QCD", 1],
    ["QED", 2],
    ["NP", 1]
  ],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Ue4",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "HNLMIX",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "Subscript[U,e4]",
      "description": "Mixing of the HNL with the electron neutrino, U_{e4}, Eq.(2.5)"
    },
    {
      "name": "Umu4",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "HNLMIX",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "tex": "Subscript[U,\\[Mu]4]",
      "description": "Mixing of the HNL with the muon neutrino, U_{mu 4}, Eq.(2.5)"
    },
    {
      "name": "Uta4",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "HNLMIX",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "tex": "Subscript[U,\\[Tau]4]",
      "description": "Mixing of the HNL with the tau neutrino, U_{tau 4}, Eq.(2.5)"
    },
    {
      "name": "UaN",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "UaN[1]", "rhs": "Ue4"},
        {"lhs": "UaN[2]", "rhs": "Umu4"},
        {"lhs": "UaN[3]", "rhs": "Uta4"}
      ],
      "parameter_name": {},
      "tex": "Subscript[U,\\[Alpha]4]",
      "description": "Active-heavy mixing vector U_{alpha 4} in the 3+1 scheme, App.B"
    },
    {
      "name": "CNN",
      "parameter_type": "Internal",
      "value": "Ue4^2 + Umu4^2 + Uta4^2",
      "interaction_order": ["NP", 2],
      "tex": "Subscript[C,44]",
      "description": "C_44 = sum_alpha |U_{alpha 4}|^2, neutral-current coefficient, Eq.(2.7) and Eq.(5.3)"
    },
    {
      "name": "fpi",
      "parameter_type": "External",
      "value": "0.130",
      "block_name": "MESONDC",
      "order_block": 1,
      "tex": "Subscript[f,\\[Pi]]",
      "description": "Pion decay constant [GeV], Tab.1, Eq.(3.1)"
    },
    {
      "name": "fK",
      "parameter_type": "External",
      "value": "0.156",
      "block_name": "MESONDC",
      "order_block": 2,
      "tex": "Subscript[f,K]",
      "description": "Kaon decay constant [GeV], Tab.1"
    },
    {
      "name": "fD",
      "parameter_type": "External",
      "value": "0.212",
      "block_name": "MESONDC",
      "order_block": 3,
      "tex": "Subscript[f,D]",
      "description": "D meson decay constant [GeV], Tab.1"
    },
    {
      "name": "fDs",
      "parameter_type": "External",
      "value": "0.249",
      "block_name": "MESONDC",
      "order_block": 4,
      "tex": "Subscript[f,Ds]",
      "description": "Ds meson decay constant [GeV], Tab.1"
    },
    {
      "name": "f0",
      "parameter_type": "External",
      "value": "0.148",
      "block_name": "MESONDC",
      "order_block": 5,
      "tex": "Subscript[f,0]",
      "description": "eta_0 singlet decay constant [GeV], Tab.1"
    },
    {
      "name": "f8",
      "parameter_type": "External",
      "value": "0.165",
      "block_name": "MESONDC",
      "order_block": 6,
      "tex": "Subscript[f,8]",
      "description": "eta_8 octet decay constant [GeV], Tab.1"
    },
    {
      "name": "th0",
      "parameter_type": "External",
      "value": "-0.1204277",
      "block_name": "MESONDC",
      "order_block": 7,
      "tex": "Subscript[\\[Theta],0]",
      "description": "eta-eta' mixing angle theta_0 [rad] (-6.9 degrees), Tab.1, Eq.(3.16)"
    },
    {
      "name": "th8",
      "parameter_type": "External",
      "value": "-0.3700098",
      "block_name": "MESONDC",
      "order_block": 8,
      "tex": "Subscript[\\[Theta],8]",
      "description": "eta-eta' mixing angle theta_8 [rad] (-21.2 degrees), Tab.1, Eq.(3.16)"
    },
    {
      "name": "frho",
      "parameter_type": "External",
      "value": "0.171",
      "block_name": "MESONDC",
      "order_block": 9,
      "tex": "Subscript[f,\\[Rho]]",
      "description": "rho meson decay constant [GeV^2], Tab.1, Eq.(3.2), App.C"
    },
    {
      "name": "fome",
      "parameter_type": "External",
      "value": "0.155",
      "block_name": "MESONDC",
      "order_block": 10,
      "tex": "Subscript[f,\\[Omega]]",
      "description": "omega meson decay constant [GeV^2], Tab.1, App.C"
    },
    {
      "name": "fphi",
      "parameter_type": "External",
      "value": "0.232",
      "block_name": "MESONDC",
      "order_block": 11,
      "tex": "Subscript[f,\\[Phi]]",
      "description": "phi meson decay constant [GeV^2], Tab.1, App.C"
    },
    {
      "name": "fKst",
      "parameter_type": "External",
      "value": "0.178",
      "block_name": "MESONDC",
      "order_block": 12,
      "tex": "Subscript[f,K*]",
      "description": "K* meson decay constant [GeV^2], Tab.1, Eq.(C.5)"
    },
    {
      "name": "feta",
      "parameter_type": "Internal",
      "value": "Cos[th8] f8/Sqrt[3] + Sin[th0] f0/Sqrt[6]",
      "tex": "Subscript[f,\\[Eta]]",
      "description": "Effective eta decay constant [GeV] = cos(th8) f8/Sqrt[3] + sin(th0) f0/Sqrt[6], Eq.(3.19), Eq.(5.2); numerically 0.0816 GeV"
    },
    {
      "name": "fetap",
      "parameter_type": "Internal",
      "value": "Sin[th8] f8/Sqrt[3] - Cos[th0] f0/Sqrt[6]",
      "tex": "Subscript[f,\\[Eta]']",
      "description": "Effective eta' decay constant [GeV] = sin(th8) f8/Sqrt[3] - cos(th0) f0/Sqrt[6], Eq.(3.20), Eq.(5.2); numerically -0.0946 GeV"
    },
    {
      "name": "grho",
      "parameter_type": "Internal",
      "value": "1 - 2 sw^2",
      "tex": "Subscript[g,\\[Rho]]",
      "description": "Neutral-current coefficient of the rho0, dimensionless, Tab.4 and Eq.(3.36)"
    },
    {
      "name": "gome",
      "parameter_type": "Internal",
      "value": "-2 sw^2/3",
      "tex": "Subscript[g,\\[Omega]]",
      "description": "Neutral-current coefficient of the omega, dimensionless, Tab.4 and Eq.(3.37)"
    },
    {
      "name": "gphi",
      "parameter_type": "Internal",
      "value": "-Sqrt[2] (1/2 - 2 sw^2/3)",
      "tex": "Subscript[g,\\[Phi]]",
      "description": "Neutral-current coefficient of the phi, dimensionless, Tab.4 and Eq.(3.38)"
    },
    {
      "name": "fpKpi0",
      "parameter_type": "External",
      "value": "0.9749",
      "block_name": "FORMFAC",
      "order_block": 1,
      "description": "Constant vector form factor f_+ for K+ -> pi0 l N at <q^2>, dimensionless, Tab.3 and App.D"
    },
    {
      "name": "fmKpi0",
      "parameter_type": "External",
      "value": "0.1151",
      "block_name": "FORMFAC",
      "order_block": 2,
      "description": "Constant scalar form factor f_- for K+ -> pi0 l N at <q^2>, dimensionless, from Eq.(3.51) with Tab.3"
    },
    {
      "name": "fpK0pi",
      "parameter_type": "External",
      "value": "0.9749",
      "block_name": "FORMFAC",
      "order_block": 3,
      "description": "Constant vector form factor f_+ for K0 -> pi- l N at <q^2>, dimensionless, Tab.3 and App.D"
    },
    {
      "name": "fmK0pi",
      "parameter_type": "External",
      "value": "0.1644",
      "block_name": "FORMFAC",
      "order_block": 4,
      "description": "Constant scalar form factor f_- for K0 -> pi- l N at <q^2>, dimensionless, from Eq.(3.51) with Tab.3"
    },
    {
      "name": "fpDK",
      "parameter_type": "External",
      "value": "0.7647",
      "block_name": "FORMFAC",
      "order_block": 5,
      "description": "Constant vector form factor f_+ for D+ -> K0bar l N at <q^2>, dimensionless, Tab.2 and App.D"
    },
    {
      "name": "fmDK",
      "parameter_type": "External",
      "value": "0.2502",
      "block_name": "FORMFAC",
      "order_block": 6,
      "description": "Constant scalar form factor f_- for D+ -> K0bar l N at <q^2>, dimensionless, from Eq.(3.51) with Tab.2"
    },
    {
      "name": "lamKpip",
      "parameter_type": "External",
      "value": "0.0297",
      "block_name": "FORMFAC",
      "order_block": 7,
      "description": "Slope lambda_+ of the linear K+ -> pi0 form factor, dimensionless, Eq.(3.52), Tab.3"
    },
    {
      "name": "lamKpi0",
      "parameter_type": "External",
      "value": "0.0195",
      "block_name": "FORMFAC",
      "order_block": 8,
      "description": "Slope lambda_0 of the linear K+ -> pi0 form factor, dimensionless, Eq.(3.52), Tab.3"
    },
    {
      "name": "lamK0pip",
      "parameter_type": "External",
      "value": "0.0282",
      "block_name": "FORMFAC",
      "order_block": 9,
      "description": "Slope lambda_+ of the linear K0 -> pi- form factor, dimensionless, Eq.(3.52), Tab.3"
    },
    {
      "name": "lamK0pi0",
      "parameter_type": "External",
      "value": "0.0138",
      "block_name": "FORMFAC",
      "order_block": 10,
      "description": "Slope lambda_0 of the linear K0 -> pi- form factor, dimensionless, Eq.(3.52), Tab.3"
    },
    {
      "name": "cpDK",
      "parameter_type": "External",
      "value": "-0.066",
      "block_name": "FORMFAC",
      "order_block": 11,
      "description": "Coefficient c_+ of the pole parametrization for D -> K, dimensionless, Eq.(3.53), Tab.2"
    },
    {
      "name": "c0DK",
      "parameter_type": "External",
      "value": "-2.084",
      "block_name": "FORMFAC",
      "order_block": 12,
      "description": "Coefficient c_0 of the pole parametrization for D -> K, dimensionless, Eq.(3.54), Tab.2"
    },
    {
      "name": "MDsst",
      "parameter_type": "External",
      "value": "2.1122",
      "block_name": "FORMFAC",
      "order_block": 13,
      "description": "Pole mass M_{D*s} [GeV] of the D -> K vector form factor, Eq.(3.53)"
    }
  ],
  "particles": [
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "N4",
      "self_conjugate": false,
      "mass": {"sym": "MN4", "value": "1."},
      "width": {"sym": "WN4", "value": "1.*^-20"},
      "quantum_numbers": {"LeptonNumber": "1"},
      "pdg": 9900012,
      "particle_name": "N4",
      "antiparticle_name": "N4~",
      "full_name": "Heavy neutral lepton",
      "propagator_label": "N4",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "pi0",
      "self_conjugate": true,
      "mass": {"sym": "Mpi0", "value": "0.1349768"},
      "width": {"sym": "Wpi0", "value": "7.81*^-9"},
      "pdg": 111,
      "particle_name": "pi0",
      "full_name": "Neutral pion",
      "propagator_label": "pi0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "pip",
      "self_conjugate": false,
      "mass": {"sym": "Mpip", "value": "0.13957039"},
      "width": {"sym": "Wpip", "value": "2.5284*^-17"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 211,
      "particle_name": "pi+",
      "antiparticle_name": "pi-",
      "full_name": "Charged pion",
      "propagator_label": "pi",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "eta",
      "self_conjugate": true,
      "mass": {"sym": "Meta", "value": "0.547862"},
      "width": {"sym": "Weta", "value": "1.31*^-6"},
      "pdg": 221,
      "particle_name": "eta",
      "full_name": "eta meson",
      "propagator_label": "eta",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "etap",
      "self_conjugate": true,
      "mass": {"sym": "Metap", "value": "0.95778"},
      "width": {"sym": "Wetap", "value": "1.88*^-4"},
      "pdg": 331,
      "particle_name": "eta'",
      "full_name": "eta prime meson",
      "propagator_label": "etap",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "Kp",
      "self_conjugate": false,
      "mass": {"sym": "MKp", "value": "0.493677"},
      "width": {"sym": "WKp", "value": "5.317*^-17"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 321,
      "particle_name": "K+",
      "antiparticle_name": "K-",
      "full_name": "Charged kaon",
      "propagator_label": "K",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "K0",
      "self_conjugate": false,
      "mass": {"sym": "MK0", "value": "0.497611"},
      "width": {"sym": "WK0", "value": "1.*^-16"},
      "pdg": 311,
      "particle_name": "K0",
      "antiparticle_name": "K0~",
      "full_name": "Neutral kaon",
      "propagator_label": "K0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 106,
      "class_name": "Dp",
      "self_conjugate": false,
      "mass": {"sym": "MDp", "value": "1.86966"},
      "width": {"sym": "WDp", "value": "6.33*^-13"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 411,
      "particle_name": "D+",
      "antiparticle_name": "D-",
      "full_name": "Charged D meson",
      "propagator_label": "D",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 107,
      "class_name": "Dsp",
      "self_conjugate": false,
      "mass": {"sym": "MDs", "value": "1.96835"},
      "width": {"sym": "WDs", "value": "1.305*^-12"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 431,
      "particle_name": "Ds+",
      "antiparticle_name": "Ds-",
      "full_name": "Charged Ds meson",
      "propagator_label": "Ds",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "rho0",
      "self_conjugate": true,
      "mass": {"sym": "Mrho", "value": "0.77526"},
      "width": {"sym": "Wrho", "value": "0.1478"},
      "pdg": 113,
      "particle_name": "rho0",
      "full_name": "Neutral rho meson",
      "propagator_label": "rho0",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "rhop",
      "self_conjugate": false,
      "mass": {"sym": "Mrhop", "value": "0.77511"},
      "width": {"sym": "Wrhop", "value": "0.1491"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 213,
      "particle_name": "rho+",
      "antiparticle_name": "rho-",
      "full_name": "Charged rho meson",
      "propagator_label": "rho",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 102,
      "class_name": "omega",
      "self_conjugate": true,
      "mass": {"sym": "Mome", "value": "0.78266"},
      "width": {"sym": "Wome", "value": "0.00868"},
      "pdg": 223,
      "particle_name": "omega",
      "full_name": "omega meson",
      "propagator_label": "omega",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 103,
      "class_name": "phiM",
      "self_conjugate": true,
      "mass": {"sym": "Mphi", "value": "1.019461"},
      "width": {"sym": "Wphi", "value": "0.004249"},
      "pdg": 333,
      "particle_name": "phi",
      "full_name": "phi meson",
      "propagator_label": "phi",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 104,
      "class_name": "Kstarp",
      "self_conjugate": false,
      "mass": {"sym": "MKst", "value": "0.89167"},
      "width": {"sym": "WKst", "value": "0.0514"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 323,
      "particle_name": "K*+",
      "antiparticle_name": "K*-",
      "full_name": "Charged K star meson",
      "propagator_label": "Kst",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LN4kin",
      "expression": "Block[{mu}, I N4bar.Ga[mu].DC[N4, mu] - MN4 N4bar.N4]",
      "delayed": true
    },
    {
      "name": "LmesonPSkin0",
      "expression": "Block[{mu}, 1/2 del[pi0, mu] del[pi0, mu] - 1/2 Mpi0^2 pi0^2 + 1/2 del[eta, mu] del[eta, mu] - 1/2 Meta^2 eta^2 + 1/2 del[etap, mu] del[etap, mu] - 1/2 Metap^2 etap^2]",
      "delayed": true
    },
    {
      "name": "LmesonPSkinC",
      "expression": "Block[{mu}, del[pipbar, mu] del[pip, mu] - Mpip^2 pipbar pip + del[Kpbar, mu] del[Kp, mu] - MKp^2 Kpbar Kp + del[K0bar, mu] del[K0, mu] - MK0^2 K0bar K0 + del[Dpbar, mu] del[Dp, mu] - MDp^2 Dpbar Dp + del[Dspbar, mu] del[Dsp, mu] - MDs^2 Dspbar Dsp]",
      "delayed": true
    },
    {
      "name": "LmesonVkin0",
      "expression": "Block[{mu, nu}, -1/4 FS[rho0, mu, nu] FS[rho0, mu, nu] + 1/2 Mrho^2 rho0[mu] rho0[mu] - 1/4 FS[omega, mu, nu] FS[omega, mu, nu] + 1/2 Mome^2 omega[mu] omega[mu] - 1/4 FS[phiM, mu, nu] FS[phiM, mu, nu] + 1/2 Mphi^2 phiM[mu] phiM[mu]]",
      "delayed": true
    },
    {
      "name": "LmesonVkinC",
      "expression": "Block[{mu, nu}, -1/2 FS[rhopbar, mu, nu] FS[rhop, mu, nu] + Mrhop^2 rhopbar[mu] rhop[mu] - 1/2 FS[Kstarpbar, mu, nu] FS[Kstarp, mu, nu] + MKst^2 Kstarpbar[mu] Kstarp[mu]]",
      "delayed": true
    },
    {
      "name": "LHNLfree",
      "expression": "LN4kin + LmesonPSkin0 + LmesonPSkinC + LmesonVkin0 + LmesonVkinC",
      "delayed": true
    },
    {
      "name": "LNCP",
      "expression": "Block[{mu, ff}, -1/2 Gf (fpi del[pi0, mu] + feta del[eta, mu] + fetap del[etap, mu]) (CNN N4bar.Ga[mu].ProjM.N4 + Conjugate[UaN[ff]] N4bar.Ga[mu].ProjM.vl[ff] + UaN[ff] vlbar[ff].Ga[mu].ProjM.N4 + vlbar[ff].Ga[mu].ProjM.vl[ff])]",
      "delayed": true
    },
    {
      "name": "LCCP",
      "expression": "Block[{mu, ff, tmp}, tmp = -Sqrt[2] Gf (CKM[1,1] fpi del[pipbar, mu] + CKM[1,2] fK del[Kpbar, mu] + CKM[2,1] fD del[Dpbar, mu] + CKM[2,2] fDs del[Dspbar, mu]) (UaN[ff] lbar[ff].Ga[mu].ProjM.N4 + lbar[ff].Ga[mu].ProjM.vl[ff]); tmp + HC[tmp]]",
      "delayed": true
    },
    {
      "name": "LNCV",
      "expression": "Block[{mu, ff}, -1/2 Gf (grho frho rho0[mu] + gome fome omega[mu] + gphi fphi phiM[mu]) (CNN N4bar.Ga[mu].ProjM.N4 + Conjugate[UaN[ff]] N4bar.Ga[mu].ProjM.vl[ff] + UaN[ff] vlbar[ff].Ga[mu].ProjM.N4 + vlbar[ff].Ga[mu].ProjM.vl[ff])]",
      "delayed": true
    },
    {
      "name": "LCCV",
      "expression": "Block[{mu, ff, tmp}, tmp = -Sqrt[2] Gf (CKM[1,1] frho rhopbar[mu] + CKM[1,2] fKst Kstarpbar[mu]) (UaN[ff] lbar[ff].Ga[mu].ProjM.N4 + lbar[ff].Ga[mu].ProjM.vl[ff]); tmp + HC[tmp]]",
      "delayed": true
    },
    {
      "name": "LSL",
      "expression": "Block[{mu, ff, tmp}, tmp = -I Sqrt[2] Gf (UaN[ff] lbar[ff].Ga[mu].ProjM.N4 + lbar[ff].Ga[mu].ProjM.vl[ff]) (CKM[1,2]/Sqrt[2] ((fpKpi0 + fmKpi0) del[pi0, mu] Kpbar - (fpKpi0 - fmKpi0) pi0 del[Kpbar, mu]) + CKM[1,2] ((fpK0pi + fmK0pi) del[pipbar, mu] K0bar - (fpK0pi - fmK0pi) pipbar del[K0bar, mu]) + CKM[2,2] ((fpDK + fmDK) del[K0bar, mu] Dpbar - (fpDK - fmDK) K0bar del[Dpbar, mu])); tmp + HC[tmp]]",
      "delayed": true
    },
    {
      "name": "LHNLmeson",
      "expression": "LNCP + LCCP + LNCV + LCCV + LSL",
      "delayed": true
    },
    {
      "name": "LNWZ",
      "expression": "Block[{mu, ff, tmp}, tmp = gw/Sqrt[2] W[mu] Conjugate[UaN[ff]] N4bar.Ga[mu].ProjM.l[ff]; tmp + HC[tmp] + gw/(4 cw) Z[mu] (CNN N4bar.Ga[mu].ProjM.N4 + Conjugate[UaN[ff]] N4bar.Ga[mu].ProjM.vl[ff] + UaN[ff] vlbar[ff].Ga[mu].ProjM.N4)]",
      "delayed": true
    },
    {
      "name": "LHNL",
      "expression": "LHNLfree + LHNLmeson",
      "delayed": true
    },
    {
      "name": "LHNLcollider",
      "expression": "LHNLfree + LNWZ",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```