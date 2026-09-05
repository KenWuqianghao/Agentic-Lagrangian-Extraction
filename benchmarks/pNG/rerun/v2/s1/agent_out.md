I'll start by reading the paper and the schema.
I read the paper, the schema, and SM.fr. No cached or reference `.fr` file for pNG exists in the sandbox, and none was read.

## Model content (arXiv:1912.04008)

One complex scalar gauge singlet `S` with a softly broken global dark U(1) and a dark CP symmetry. After EWSB, `S = (vs + s + i χ)/√2`. The new physical states are:

| state | spin | colour | SU(2) | Q | Y | mass |
|---|---|---|---|---|---|---|
| `H2` (second CP-even mass eigenstate, mixes with the 125 GeV `H` by angle `th`) | S | singlet | singlet | 0 | 0 | `MH2` = 125.30 |
| `chi` (pNG boson, CP-odd, stable DM) | S | singlet | singlet | 0 | 0 | `Mchi` = 62.573 |

Plus three unphysical fields: the complex singlet `SS`, its CP-even part `sing`, and the rotated CP-even doublet component `phih`. Free parameters: `{Mchi, vsing, th, MH2}`; the potential parameters `lamPhi, lamS, lamPS, muPhi2, muS2, muSp2` are Internal (eqs. 2.18–2.20), as are the DM couplings `kchih, kchiH` (eqs. A.5–A.6).

## Self-audit table

| term | fields | d | coupling | coupling dim (=4-d) | 1/Λ^(d-4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) sum | L/B | CC[] | Hermitian |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LSkin` | `del[SSbar,mu] del[SS,mu]` | 1+1+1+1=4 | none (1) | 0 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | dark U(1): −1+1=0 ✓ | n/a | n/a | self-Hermitian |
| `LSmass` | `SSbar SS` | 1+1=2 | `muS2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | −1+1=0 ✓ | n/a | n/a | self-Hermitian |
| `LSquartic` | `(SSbar SS)^2` | 4 | `lamS` | 0 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | 0 ✓ | n/a | n/a | self-Hermitian |
| `LSportal` | `Phibar[ii] Phi[ii] SSbar SS` | 1+1+1+1=4 | `lamPS` | 0 ✓ | n/a | 0 ✓ | −1/2+1/2=0 ✓ | shared index `ii` (anti-doublet × doublet) | singlet | 0 ✓ | n/a | n/a | self-Hermitian |
| `LSsoft` | `SS SS + SSbar SSbar` | 1+1=2 | `muSp2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | ±2 — **soft breaking of the dark U(1), eq. (2.3), by construction** | n/a | n/a | explicit sum of a term and its conjugate ✓ |
| kinetic+mass, `H2` | `H2` sits in `SS` through `sing`; `LSkin` gives its kinetic term, `LSmass`+`LSquartic`+`LSportal` its mass; both are in `LpNG` ✓ |
| kinetic+mass, `chi` | `chi` sits in `SS`; `LSkin` gives its kinetic term, the potential gives `m_chi^2 = muSp2`; both are in `LpNG` ✓ |

`SelfConjugate -> True` classes: `H2`, `chi`, `sing`, `phih` — none carries `QuantumNumbers` ✓.
The only U(1)-violating row is `LSsoft`; this is the paper's soft breaking term, not an error. No EFT cutoff is needed: every operator has d ≤ 4.
Reference or cached model file read: **none**.

```json
{
  "model_name": "pNG_gen",
  "info": {
    "authors": ["C. Arina", "A. Beniwal", "C. Degrande", "J. Heisig", "A. Scaffidi"],
    "version": "1.0",
    "date": "09. 12. 2019",
    "institutions": ["Universite catholique de Louvain (CP3)", "University of Adelaide"],
    "emails": ["chiara.arina@uclouvain.be", "ankit.beniwal@uclouvain.be", "celine.degrande@uclouvain.be", "jan.heisig@uclouvain.be", "andre.scaffidi@adelaide.edu.au"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "raw_preamble": [
    "(* ******************************************************************** *)\n(* pseudo-Nambu-Goldstone dark matter, arXiv:1912.04008, eqs.(2.1)-(2.3) *)\n(* A complex scalar gauge singlet S with a softly broken global dark     *)\n(* U(1) is added to the SM.  This file is an add-on to SM.fr.            *)\n(*                                                                       *)\n(* Field content:  S = (vsing + sing + I chi)/Sqrt[2], eq.(2.8).         *)\n(*   chi : the pNG boson, the CP-odd dark matter candidate.              *)\n(*   H2  : the second CP-even mass eigenstate (the paper calls it H).    *)\n(*   H   : the 125 GeV mass eigenstate of SM.fr (the paper calls it h).  *)\n(*                                                                       *)\n(* IMPORTANT: the CP-even neutral component phi of the SM doublet mixes  *)\n(* with the singlet by the angle th, eqs.(2.12)-(2.13):                  *)\n(*    phi  =  Cos[th] H + Sin[th] H2 = phih,                             *)\n(*    s    = -Sin[th] H + Cos[th] H2 = sing.                             *)\n(* The SM.fr rule  Phi[2] -> (vev + H + I G0)/Sqrt[2]  must therefore be *)\n(* replaced by     Phi[2] -> (vev + phih + I G0)/Sqrt[2],                *)\n(* and the SM.fr quartic lam by lamPhi/2, so that all SM couplings of H  *)\n(* are scaled by Cos[th] and H2 gets the Sin[th] fraction.               *)\n(* ******************************************************************** *)"
  ],
  "parameters": [
    {
      "name": "th",
      "parameter_type": "External",
      "block_name": "PNGINPUTS",
      "order_block": 1,
      "value": "1.53",
      "tex": "\\[Theta]",
      "description": "Mixing angle between the CP-even states H (125 GeV) and H2, eqs.(2.13)-(2.14) [rad]; best-fit value of table 2"
    },
    {
      "name": "vsing",
      "parameter_type": "External",
      "block_name": "PNGINPUTS",
      "order_block": 2,
      "value": "13155.1",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[v,s]",
      "description": "Vacuum expectation value vs of the complex singlet S, eq.(2.8) [GeV]; best-fit vh/vs = 0.0187 of table 2"
    },
    {
      "name": "lamPhi",
      "parameter_type": "Internal",
      "value": "(MH^2*Cos[th]^2 + MH2^2*Sin[th]^2)/vev^2",
      "interaction_order": ["QED", 2],
      "tex": "Subscript[\\[Lambda],\\[CapitalPhi]]",
      "description": "Higgs quartic coupling lambda_Phi, eq.(2.18); in the pNG model the SM.fr coupling lam must be set to lamPhi/2"
    },
    {
      "name": "lamS",
      "parameter_type": "Internal",
      "value": "(MH^2*Sin[th]^2 + MH2^2*Cos[th]^2)/vsing^2",
      "interaction_order": ["QED", 2],
      "tex": "Subscript[\\[Lambda],S]",
      "description": "Quartic coupling lambda_S of the singlet, eq.(2.19); perturbative unitarity requires lamS < 8 Pi/3, eq.(3.2)"
    },
    {
      "name": "lamPS",
      "parameter_type": "Internal",
      "value": "(MH2^2 - MH^2)*Sin[th]*Cos[th]/(vev*vsing)",
      "interaction_order": ["QED", 2],
      "tex": "Subscript[\\[Lambda],\\[CapitalPhi]S]",
      "description": "Higgs portal coupling lambda_PhiS, eq.(2.20)"
    },
    {
      "name": "muSp2",
      "parameter_type": "Internal",
      "value": "Mchi^2",
      "tex": "Superscript[Subscript[\\[Mu],S],\\[Prime]2]",
      "description": "Soft U(1)-breaking mass-squared mu'_S^2 of eq.(2.3), equal to the squared pNG dark matter mass, eq.(2.18) [GeV^2]"
    },
    {
      "name": "muPhi2",
      "parameter_type": "Internal",
      "value": "lamPhi*vev^2 + lamPS*vsing^2",
      "tex": "Superscript[Subscript[\\[Mu],\\[CapitalPhi]],2]",
      "description": "Squared mass parameter mu_Phi^2 of the SM Higgs potential, eqs.(2.9) and (2.19) [GeV^2]"
    },
    {
      "name": "muS2",
      "parameter_type": "Internal",
      "value": "lamS*vsing^2 + lamPS*vev^2 - muSp2",
      "tex": "Superscript[Subscript[\\[Mu],S],2]",
      "description": "Squared mass parameter mu_S^2 of the singlet potential, eqs.(2.10) and (2.20) [GeV^2]"
    },
    {
      "name": "kchih",
      "parameter_type": "Internal",
      "value": "-MH^2*Sin[th]/vsing",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[\\[Kappa],\\[Chi]\\[Chi]h]",
      "description": "Dimensionful chi chi H coupling kappa_chichih, eq.(A.5) [GeV]"
    },
    {
      "name": "kchiH",
      "parameter_type": "Internal",
      "value": "MH2^2*Cos[th]/vsing",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[\\[Kappa],\\[Chi]\\[Chi]H]",
      "description": "Dimensionful chi chi H2 coupling kappa_chichiH, eq.(A.6) [GeV]"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "H2",
      "self_conjugate": true,
      "mass": {"sym": "MH2", "value": "125.30"},
      "width": {"sym": "WH2", "value": "0.00407"},
      "quantum_numbers": {},
      "pdg": 35,
      "particle_name": "H2",
      "full_name": "Second CP-even scalar",
      "propagator_label": "H2",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "chi",
      "self_conjugate": true,
      "mass": {"sym": "Mchi", "value": "62.573"},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 51,
      "particle_name": "chi",
      "full_name": "pseudo-Nambu-Goldstone dark matter",
      "propagator_label": "chi",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 12,
      "class_name": "SS",
      "self_conjugate": false,
      "unphysical": true,
      "definitions": ["SS -> (vsing + sing + I chi)/Sqrt[2]"]
    },
    {
      "spin_type": "S",
      "class_index": 13,
      "class_name": "sing",
      "self_conjugate": true,
      "unphysical": true,
      "definitions": ["sing -> -Sin[th] H + Cos[th] H2"]
    },
    {
      "spin_type": "S",
      "class_index": 14,
      "class_name": "phih",
      "self_conjugate": true,
      "unphysical": true,
      "definitions": ["phih -> Cos[th] H + Sin[th] H2"]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LSkin",
      "expression": "Block[{mu}, ExpandIndices[del[SSbar, mu] del[SS, mu]]]",
      "delayed": true
    },
    {
      "name": "LSmass",
      "expression": "Block[{}, ExpandIndices[muS2/2 SSbar SS]]",
      "delayed": true
    },
    {
      "name": "LSquartic",
      "expression": "Block[{}, ExpandIndices[-lamS/2 (SSbar SS)^2]]",
      "delayed": true
    },
    {
      "name": "LSportal",
      "expression": "Block[{ii}, ExpandIndices[-lamPS Phibar[ii] Phi[ii] SSbar SS, FlavorExpand -> SU2D]]",
      "delayed": true
    },
    {
      "name": "LSsoft",
      "expression": "Block[{}, ExpandIndices[muSp2/4 (SS SS + SSbar SSbar)]]",
      "delayed": true
    },
    {
      "name": "LpNG",
      "expression": "LSkin + LSmass + LSquartic + LSportal + LSsoft",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LpNG",
      "delayed": true
    }
  ],
  "raw_blocks": []
}
```
I read the paper, the schema, and SM.fr. No cached or reference `.fr` file for pNG exists in the sandbox, and none was read.

## Model content (arXiv:1912.04008)

One complex scalar gauge singlet `S` with a softly broken global dark U(1) and a dark CP symmetry. After EWSB, `S = (vs + s + i χ)/√2`. The new physical states are:

| state | spin | colour | SU(2) | Q | Y | mass |
|---|---|---|---|---|---|---|
| `H2` (second CP-even mass eigenstate, mixes with the 125 GeV `H` by angle `th`) | S | singlet | singlet | 0 | 0 | `MH2` = 125.30 |
| `chi` (pNG boson, CP-odd, stable DM) | S | singlet | singlet | 0 | 0 | `Mchi` = 62.573 |

Plus three unphysical fields: the complex singlet `SS`, its CP-even part `sing`, and the rotated CP-even doublet component `phih`. Free parameters: `{Mchi, vsing, th, MH2}`; the potential parameters `lamPhi, lamS, lamPS, muPhi2, muS2, muSp2` are Internal (eqs. 2.18–2.20), as are the DM couplings `kchih, kchiH` (eqs. A.5–A.6).

## Self-audit table

| term | fields | d | coupling | coupling dim (=4-d) | 1/Λ^(d-4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) sum | L/B | CC[] | Hermitian |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LSkin` | `del[SSbar,mu] del[SS,mu]` | 1+1+1+1=4 | none (1) | 0 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | dark U(1): −1+1=0 ✓ | n/a | n/a | self-Hermitian |
| `LSmass` | `SSbar SS` | 1+1=2 | `muS2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | −1+1=0 ✓ | n/a | n/a | self-Hermitian |
| `LSquartic` | `(SSbar SS)^2` | 4 | `lamS` | 0 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | 0 ✓ | n/a | n/a | self-Hermitian |
| `LSportal` | `Phibar[ii] Phi[ii] SSbar SS` | 1+1+1+1=4 | `lamPS` | 0 ✓ | n/a | 0 ✓ | −1/2+1/2=0 ✓ | shared index `ii` (anti-doublet × doublet) | singlet | 0 ✓ | n/a | n/a | self-Hermitian |
| `LSsoft` | `SS SS + SSbar SSbar` | 1+1=2 | `muSp2` | 2 ✓ | n/a | 0 ✓ | 0 ✓ | singlet | singlet | ±2 — **soft breaking of the dark U(1), eq. (2.3), by construction** | n/a | n/a | explicit sum of a term and its conjugate ✓ |
| kinetic+mass, `H2` | `H2` sits in `SS` through `sing`; `LSkin` gives its kinetic term, `LSmass`+`LSquartic`+`LSportal` its mass; both are in `LpNG` ✓ |
| kinetic+mass, `chi` | `chi` sits in `SS`; `LSkin` gives its kinetic term, the potential gives `m_chi^2 = muSp2`; both are in `LpNG` ✓ |

`SelfConjugate -> True` classes: `H2`, `chi`, `sing`, `phih` — none carries `QuantumNumbers` ✓.
The only U(1)-violating row is `LSsoft`; this is the paper's soft breaking term, not an error. No EFT cutoff is needed: every operator has d ≤ 4.
Reference or cached model file read: **none**.

```json
{
  "model_name": "pNG_gen",
  "info": {
    "authors": ["C. Arina", "A. Beniwal", "C. Degrande", "J. Heisig", "A. Scaffidi"],
    "version": "1.0",
    "date": "09. 12. 2019",
    "institutions": ["Universite catholique de Louvain (CP3)", "University of Adelaide"],
    "emails": ["chiara.arina@uclouvain.be", "ankit.beniwal@uclouvain.be", "celine.degrande@uclouvain.be", "jan.heisig@uclouvain.be", "andre.scaffidi@adelaide.edu.au"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "raw_preamble": [
    "(* ******************************************************************** *)\n(* pseudo-Nambu-Goldstone dark matter, arXiv:1912.04008, eqs.(2.1)-(2.3) *)\n(* A complex scalar gauge singlet S with a softly broken global dark     *)\n(* U(1) is added to the SM.  This file is an add-on to SM.fr.            *)\n(*                                                                       *)\n(* Field content:  S = (vsing + sing + I chi)/Sqrt[2], eq.(2.8).         *)\n(*   chi : the pNG boson, the CP-odd dark matter candidate.              *)\n(*   H2  : the second CP-even mass eigenstate (the paper calls it H).    *)\n(*   H   : the 125 GeV mass eigenstate of SM.fr (the paper calls it h).  *)\n(*                                                                       *)\n(* IMPORTANT: the CP-even neutral component phi of the SM doublet mixes  *)\n(* with the singlet by the angle th, eqs.(2.12)-(2.13):                  *)\n(*    phi  =  Cos[th] H + Sin[th] H2 = phih,                             *)\n(*    s    = -Sin[th] H + Cos[th] H2 = sing.                             *)\n(* The SM.fr rule  Phi[2] -> (vev + H + I G0)/Sqrt[2]  must therefore be *)\n(* replaced by     Phi[2] -> (vev + phih + I G0)/Sqrt[2],                *)\n(* and the SM.fr quartic lam by lamPhi/2, so that all SM couplings of H  *)\n(* are scaled by Cos[th] and H2 gets the Sin[th] fraction.               *)\n(* ******************************************************************** *)"
  ],
  "parameters": [
    {
      "name": "th",
      "parameter_type": "External",
      "block_name": "PNGINPUTS",
      "order_block": 1,
      "value": "1.53",
      "tex": "\\[Theta]",
      "description": "Mixing angle between the CP-even states H (125 GeV) and H2, eqs.(2.13)-(2.14) [rad]; best-fit value of table 2"
    },
    {
      "name": "vsing",
      "parameter_type": "External",
      "block_name": "PNGINPUTS",
      "order_block": 2,
      "value": "13155.1",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[v,s]",
      "description": "Vacuum expectation value vs of the complex singlet S, eq.(2.8) [GeV]; best-fit vh/vs = 0.0187 of table 2"
    },
    {
      "name": "lamPhi",
      "parameter_type": "Internal",
      "value": "(MH^2*Cos[th]^2 + MH2^2*Sin[th]^2)/vev^2",
      "interaction_order": ["QED", 2],
      "tex": "Subscript[\\[Lambda],\\[CapitalPhi]]",
      "description": "Higgs quartic coupling lambda_Phi, eq.(2.18); in the pNG model the SM.fr coupling lam must be set to lamPhi/2"
    },
    {
      "name": "lamS",
      "parameter_type": "Internal",
      "value": "(MH^2*Sin[th]^2 + MH2^2*Cos[th]^2)/vsing^2",
      "interaction_order": ["QED", 2],
      "tex": "Subscript[\\[Lambda],S]",
      "description": "Quartic coupling lambda_S of the singlet, eq.(2.19); perturbative unitarity requires lamS < 8 Pi/3, eq.(3.2)"
    },
    {
      "name": "lamPS",
      "parameter_type": "Internal",
      "value": "(MH2^2 - MH^2)*Sin[th]*Cos[th]/(vev*vsing)",
      "interaction_order": ["QED", 2],
      "tex": "Subscript[\\[Lambda],\\[CapitalPhi]S]",
      "description": "Higgs portal coupling lambda_PhiS, eq.(2.20)"
    },
    {
      "name": "muSp2",
      "parameter_type": "Internal",
      "value": "Mchi^2",
      "tex": "Superscript[Subscript[\\[Mu],S],\\[Prime]2]",
      "description": "Soft U(1)-breaking mass-squared mu'_S^2 of eq.(2.3), equal to the squared pNG dark matter mass, eq.(2.18) [GeV^2]"
    },
    {
      "name": "muPhi2",
      "parameter_type": "Internal",
      "value": "lamPhi*vev^2 + lamPS*vsing^2",
      "tex": "Superscript[Subscript[\\[Mu],\\[CapitalPhi]],2]",
      "description": "Squared mass parameter mu_Phi^2 of the SM Higgs potential, eqs.(2.9) and (2.19) [GeV^2]"
    },
    {
      "name": "muS2",
      "parameter_type": "Internal",
      "value": "lamS*vsing^2 + lamPS*vev^2 - muSp2",
      "tex": "Superscript[Subscript[\\[Mu],S],2]",
      "description": "Squared mass parameter mu_S^2 of the singlet potential, eqs.(2.10) and (2.20) [GeV^2]"
    },
    {
      "name": "kchih",
      "parameter_type": "Internal",
      "value": "-MH^2*Sin[th]/vsing",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[\\[Kappa],\\[Chi]\\[Chi]h]",
      "description": "Dimensionful chi chi H coupling kappa_chichih, eq.(A.5) [GeV]"
    },
    {
      "name": "kchiH",
      "parameter_type": "Internal",
      "value": "MH2^2*Cos[th]/vsing",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[\\[Kappa],\\[Chi]\\[Chi]H]",
      "description": "Dimensionful chi chi H2 coupling kappa_chichiH, eq.(A.6) [GeV]"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "H2",
      "self_conjugate": true,
      "mass": {"sym": "MH2", "value": "125.30"},
      "width": {"sym": "WH2", "value": "0.00407"},
      "quantum_numbers": {},
      "pdg": 35,
      "particle_name": "H2",
      "full_name": "Second CP-even scalar",
      "propagator_label": "H2",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "chi",
      "self_conjugate": true,
      "mass": {"sym": "Mchi", "value": "62.573"},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 51,
      "particle_name": "chi",
      "full_name": "pseudo-Nambu-Goldstone dark matter",
      "propagator_label": "chi",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 12,
      "class_name": "SS",
      "self_conjugate": false,
      "unphysical": true,
      "definitions": ["SS -> (vsing + sing + I chi)/Sqrt[2]"]
    },
    {
      "spin_type": "S",
      "class_index": 13,
      "class_name": "sing",
      "self_conjugate": true,
      "unphysical": true,
      "definitions": ["sing -> -Sin[th] H + Cos[th] H2"]
    },
    {
      "spin_type": "S",
      "class_index": 14,
      "class_name": "phih",
      "self_conjugate": true,
      "unphysical": true,
      "definitions": ["phih -> Cos[th] H + Sin[th] H2"]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LSkin",
      "expression": "Block[{mu}, ExpandIndices[del[SSbar, mu] del[SS, mu]]]",
      "delayed": true
    },
    {
      "name": "LSmass",
      "expression": "Block[{}, ExpandIndices[muS2/2 SSbar SS]]",
      "delayed": true
    },
    {
      "name": "LSquartic",
      "expression": "Block[{}, ExpandIndices[-lamS/2 (SSbar SS)^2]]",
      "delayed": true
    },
    {
      "name": "LSportal",
      "expression": "Block[{ii}, ExpandIndices[-lamPS Phibar[ii] Phi[ii] SSbar SS, FlavorExpand -> SU2D]]",
      "delayed": true
    },
    {
      "name": "LSsoft",
      "expression": "Block[{}, ExpandIndices[muSp2/4 (SS SS + SSbar SSbar)]]",
      "delayed": true
    },
    {
      "name": "LpNG",
      "expression": "LSkin + LSmass + LSquartic + LSportal + LSsoft",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LpNG",
      "delayed": true
    }
  ],
  "raw_blocks": []
}
```