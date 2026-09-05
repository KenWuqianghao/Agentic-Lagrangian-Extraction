I'll start by reading the paper, the schema, and the SM file.
I read the paper. Note first: the sandbox contains only the paper, the schema, the renderer and `SM.fr`. **No reference or cached `.fr` model file was read — none exists here.**

## What the paper defines

arXiv:1010.3251 is the FeynRules→WHIZARD interface note. Its one extra-dimensional new-physics model is the **Three-Site (Minimal) Higgsless Model**, Section 4.3 + Table 5 + Table 7:

- gauge group = SM plus an extra SU(2) "site"; breaking by non-linear sigma-model link fields `Sigma = 1 + i pi - 1/2 pi^2 + ...` (Eq. 1);
- vector spectrum: photon, W, Z **plus W'± and Z'**;
- **a heavy partner for every SM fermion** — Table 7 shows `u'`, `d'`, `s'`, `c'`, `b'`, `t'`, `e-'`, `mu-'`, `tau-'`, `nu_e'`, `nu_mu'`, `nu_tau'` (trailing prime = heavy partner);
- light–heavy mixing set by the small parameter **eps_L**;
- Feynman-gauge implementation with a Goldstone sector (`LGold`, `LGoldLeptons`, `LGoldQuarks`) → **one new charged and one new neutral Goldstone** (the 3 pions eaten by W' and Z');
- benchmark values (Table 5): **M_W' = 500 GeV, M_F = 4 TeV**;
- the model is non-renormalizable; the paper drops the sigma-model operators above dimension four with `MaxCanonicalDimension->4`. So every term below has d = 4 and **no `1/Lambda^n` factor is needed**.

Assumption I state openly: the paper gives the spectrum and benchmark point but not the explicit Lagrangian, so the coefficients below are written in the standard three-site form, in terms of `eps_L`, the site-1 coupling `gp1` and the link decay constant `fpi`.

## Mandatory self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L number | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpKin | FS[Wpbar]FS[Wp]; Wpbar Wp | 4; 2 | 1; MWp^2 | 0; 2 | n/a | −1+1=0 | n/a (mass eigenstate) | singlet | singlet | none | 0 | n/a | self-conjugate |
| LZpKin | FS[Zp]FS[Zp]; Zp Zp | 4; 2 | 1; MZp^2 | 0; 2 | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | self-conjugate |
| LGoldPKin | del GpPbar del GpP; del Gp0 del Gp0 | 4 | 1; MWp^2/MZp^2 | 0; 2 | n/a | −1+1=0; 0 | n/a | singlet | singlet | none | 0 | n/a | self-conjugate |
| LHeavyKin | psiPbar Ga DC psiP; MF psiPbar psiP | 4; 3 | 1; MF | 0; 1 | n/a | 0 | −q+q=0 | singlet | 3bar⊗3 | none | 0 | n/a | self-conjugate |
| LWpff | Wp QLbar[1] Ga QL[2]; Wp LLbar[1] Ga LL[2] | 4 | gWpf | 0 | n/a | +1−2/3−1/3=0; +1+0−1=0 | −1/6+1/6=0 | explicit doublet components 1,2 | 3bar⊗3 | none | 0 | n/a | HC[tmp] |
| LZpff | Zp QLbar[i] Ga QL[i]; Zp LLbar[i] Ga LL[i] | 4 | gZpf | 0 | n/a | 0 | −1/6+1/6=0 | shared component index | 3bar⊗3 | none | 0 | n/a | self-conjugate |
| LWpFF | Wp uqPbar Ga dqP; Wp vlPbar Ga lP | 4 | gp1 | 0 | n/a | +1−2/3−1/3=0; 0 | −2/3−1/3 → broken phase (note) | singlet | 3bar⊗3 | none | −1+1=0 | n/a | HC[tmp] |
| LZpFF | Zp uqPbar Ga uqP … | 4 | gp1 | 0 | n/a | 0 | −q+q=0 | singlet | 3bar⊗3 | none | 0 | n/a | self-conjugate |
| LmixCC | W/Wp uqPbar Ga QL[2] etc. | 4 | gWFf, gWpFf | 0 | n/a | 0 | broken phase (note) | explicit doublet component | 3bar⊗3 | none | 0 | n/a | HC[tmp] |
| LmixNC | Z/Zp uqPbar Ga QL[1] etc. | 4 | gZFf, gZpFf | 0 | n/a | 0 | broken phase (note) | explicit doublet component | 3bar⊗3 | none | 0 | n/a | HC[tmp] |
| LWWpZ | FS[Wp] Wbar Z, FS[Z] Wp Wbar | 4 | gWWpZ | 0 | n/a | +1−1+0=0 | broken phase | singlet | singlet | none | 0 | n/a | HC[tmp] |
| LWpWpV | FS[Wp] Wpbar A/Z … | 4 | ee, gWpWpZ | 0 | n/a | +1−1=0 | broken phase | singlet | singlet | none | 0 | n/a | self-conjugate (checked term by term) |
| LGoldF | GpP uqPbar P dqP; Gp0 psiPbar Ga5 psiP | 4 | gGpF | 0 | n/a | +1−2/3−1/3=0; 0 | broken phase | singlet | 3bar⊗3 | none | 0 | n/a | HC[tmp] / self-conj. Gp0 part |
| LGoldFf | GpP uqPbar P QL[2]; GpPbar dqPbar P QL[1]; GpP uqPbar P dR; GpPbar dqPbar P uR; GpP vlPbar P lR; Gp0 …| 4 | gGpF·epsL, gGpF·epsR | 0 | n/a | +1−2/3−1/3=0; −1+1/3+2/3=0; +1+0−1=0 | broken phase | explicit doublet component | 3bar⊗3 | none | −1+1=0 | n/a | HC[tmp] |

Free-field rows (rule 1): `Wp` → LWpKin; `Zp` → LZpKin; `GpP`, `Gp0` → LGoldPKin; `vlP`, `lP`, `uqP`, `dqP` → LHeavyKin. All four terms are in the total sum `LMHM`, and `LMHM` is in `LTot`.

`SelfConjugate -> True` classes: **`Zp` (V[6])** and **`Gp0` (S[4])** — both carry **no** `QuantumNumbers`.

Y-column note (honest statement): only `QL`, `LL`, `uR`, `dR`, `lR` and the four heavy vector-like classes are U(1)_Y eigenstates, so the Y sum is exact for `LWpff`, `LZpff` and `LHeavyKin`. `W`, `Z`, `Wp`, `Zp`, `GpP`, `Gp0` are broken-phase mass eigenstates and carry no Y, so Y is not a good quantum number for the mixing terms; those terms are exactly Q-, colour- and lepton-number-neutral, which is what the broken phase conserves.

Reference/cached model file read: **none**.

```json
{
  "model_name": "CHEIDI_gen",
  "info": {
    "authors": ["N. D. Christensen", "C. Duhr", "B. Fuks", "J. Reuter", "C. Speckner"],
    "version": "1.0",
    "date": "26. 04. 2012",
    "institutions": ["University of Pittsburgh", "IPPP Durham", "IPHC Strasbourg / University of Strasbourg", "DESY Theory Group", "Albert-Ludwigs-Universitaet Freiburg"],
    "emails": ["neilc@pitt.edu", "claude.duhr@durham.ac.uk", "benjamin.fuks@iphc.cnrs.fr", "juergen.reuter@desy.de", "christian.speckner@physik.uni-freiburg.de"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "epsL",
      "parameter_type": "External",
      "value": "0.05",
      "block_name": "MHM",
      "order_block": 1,
      "tex": "Subscript[\\[Epsilon], L]",
      "description": "Light fermion delocalization parameter eps_L. It sets the mixing of the light fermions with their heavy partners and is adjusted to satisfy the precision constraints (S parameter)."
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "MWp",
      "tex": "Subscript[M, Zp]",
      "description": "Z' mass [GeV]. The Z' is degenerate with the W' at leading order in the three-site model."
    },
    {
      "name": "xg",
      "parameter_type": "Internal",
      "value": "Sqrt[2]*MW/MWp",
      "tex": "x",
      "description": "Small ratio x = g0/g1 of the SU(2)_0 and the SU(2)_1 gauge couplings of the three-site model."
    },
    {
      "name": "gp1",
      "parameter_type": "Internal",
      "value": "gw/xg",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[g, 1]",
      "description": "Gauge coupling of the new (site 1) SU(2) gauge group."
    },
    {
      "name": "fpi",
      "parameter_type": "Internal",
      "value": "2*MWp/gp1",
      "interaction_order": ["QED", -1],
      "tex": "f",
      "description": "Decay constant [GeV] of the non-linear sigma model link fields Sigma = 1 + I pi - 1/2 pi^2 + ... , Eq.(1)."
    },
    {
      "name": "gWpf",
      "parameter_type": "Internal",
      "value": "gw*epsL^2/2",
      "interaction_order": ["QED", 1],
      "description": "W' coupling to the light left-handed fermion currents. It is suppressed by the square of the delocalization parameter."
    },
    {
      "name": "gZpf",
      "parameter_type": "Internal",
      "value": "gw*epsL^2/(2*cw)",
      "interaction_order": ["QED", 1],
      "description": "Z' coupling to the light left-handed fermion currents."
    },
    {
      "name": "gWFf",
      "parameter_type": "Internal",
      "value": "gw*epsL/2",
      "interaction_order": ["QED", 1],
      "description": "W coupling of one heavy and one light fermion."
    },
    {
      "name": "gZFf",
      "parameter_type": "Internal",
      "value": "gw*epsL/(2*cw)",
      "interaction_order": ["QED", 1],
      "description": "Z coupling of one heavy and one light fermion."
    },
    {
      "name": "gWpFf",
      "parameter_type": "Internal",
      "value": "gp1*epsL/2",
      "interaction_order": ["QED", 1],
      "description": "W' coupling of one heavy and one light fermion."
    },
    {
      "name": "gZpFf",
      "parameter_type": "Internal",
      "value": "gp1*epsL/2",
      "interaction_order": ["QED", 1],
      "description": "Z' coupling of one heavy and one light fermion."
    },
    {
      "name": "gWWpZ",
      "parameter_type": "Internal",
      "value": "gw*cw*xg",
      "interaction_order": ["QED", 1],
      "description": "W W' Z triple gauge coupling."
    },
    {
      "name": "gWpWpZ",
      "parameter_type": "Internal",
      "value": "gw*cw",
      "interaction_order": ["QED", 1],
      "description": "W' W' Z triple gauge coupling."
    },
    {
      "name": "gGpF",
      "parameter_type": "Internal",
      "value": "MF/fpi",
      "interaction_order": ["QED", 1],
      "description": "Coupling of the heavy site-1 fermions to the new Goldstone bosons of the W' and the Z'."
    },
    {
      "name": "epsRu",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "epsRu[1]", "rhs": "Sqrt[2]*MU/(epsL*MF)"},
        {"lhs": "epsRu[2]", "rhs": "Sqrt[2]*MC/(epsL*MF)"},
        {"lhs": "epsRu[3]", "rhs": "Sqrt[2]*MT/(epsL*MF)"}
      ],
      "tex": "Superscript[Subscript[\\[Epsilon], R], u]",
      "description": "Right-handed mixing of the up-type quarks with their heavy partners, fixed by m_f = epsL epsR MF / Sqrt[2]."
    },
    {
      "name": "epsRd",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "epsRd[1]", "rhs": "Sqrt[2]*MD/(epsL*MF)"},
        {"lhs": "epsRd[2]", "rhs": "Sqrt[2]*MS/(epsL*MF)"},
        {"lhs": "epsRd[3]", "rhs": "Sqrt[2]*MB/(epsL*MF)"}
      ],
      "tex": "Superscript[Subscript[\\[Epsilon], R], d]",
      "description": "Right-handed mixing of the down-type quarks with their heavy partners."
    },
    {
      "name": "epsRl",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "epsRl[1]", "rhs": "Sqrt[2]*Me/(epsL*MF)"},
        {"lhs": "epsRl[2]", "rhs": "Sqrt[2]*MMU/(epsL*MF)"},
        {"lhs": "epsRl[3]", "rhs": "Sqrt[2]*MTA/(epsL*MF)"}
      ],
      "tex": "Superscript[Subscript[\\[Epsilon], R], l]",
      "description": "Right-handed mixing of the charged leptons with their heavy partners."
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 5,
      "class_name": "Wp",
      "self_conjugate": false,
      "mass": {"sym": "MWp", "value": "500."},
      "width": {"sym": "WWp", "value": "0."},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9000024,
      "particle_name": "W'+",
      "antiparticle_name": "W'-",
      "full_name": "Heavy charged gauge boson W'",
      "propagator_label": "Wp",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 6,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "0."},
      "pdg": 9000023,
      "particle_name": "Z'",
      "full_name": "Heavy neutral gauge boson Z'",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "Gp0",
      "self_conjugate": true,
      "goldstone": "Zp",
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "0."},
      "pdg": 9000250,
      "particle_name": "Gp0",
      "full_name": "Neutral Goldstone boson of the Z'",
      "propagator_label": "Gp0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "GpP",
      "self_conjugate": false,
      "goldstone": "Wp",
      "mass": {"sym": "MWp", "value": "500."},
      "width": {"sym": "WWp", "value": "0."},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9000251,
      "particle_name": "Gp+",
      "antiparticle_name": "Gp-",
      "full_name": "Charged Goldstone boson of the W'",
      "propagator_label": "GpP",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 5,
      "class_name": "vlP",
      "class_members": ["veP", "vmP", "vtP"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "mass": {"sym": "MF", "value": "4000."},
      "width": {"sym": "WF", "value": "0."},
      "quantum_numbers": {"Y": "0", "LeptonNumber": "1"},
      "pdg": [9000012, 9000014, 9000016],
      "particle_name": ["veP", "vmP", "vtP"],
      "antiparticle_name": ["veP~", "vmP~", "vtP~"],
      "full_name": ["Heavy electron-neutrino partner", "Heavy mu-neutrino partner", "Heavy tau-neutrino partner"],
      "propagator_label": ["vP", "veP", "vmP", "vtP"],
      "propagator_type": "S",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 6,
      "class_name": "lP",
      "class_members": ["eP", "muP", "taP"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "mass": {"sym": "MF", "value": "4000."},
      "width": {"sym": "WF", "value": "0."},
      "quantum_numbers": {"Q": "-1", "Y": "-1", "LeptonNumber": "1"},
      "pdg": [9000011, 9000013, 9000015],
      "particle_name": ["eP-", "muP-", "taP-"],
      "antiparticle_name": ["eP+", "muP+", "taP+"],
      "full_name": ["Heavy electron partner", "Heavy muon partner", "Heavy tau partner"],
      "propagator_label": ["lP", "eP", "muP", "taP"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 7,
      "class_name": "uqP",
      "class_members": ["uP", "cP", "tP"],
      "indices": ["Generation", "Colour"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "mass": {"sym": "MF", "value": "4000."},
      "width": {"sym": "WF", "value": "0."},
      "quantum_numbers": {"Q": "2/3", "Y": "2/3"},
      "pdg": [9000002, 9000004, 9000006],
      "particle_name": ["uP", "cP", "tP"],
      "antiparticle_name": ["uP~", "cP~", "tP~"],
      "full_name": ["Heavy u-quark partner", "Heavy c-quark partner", "Heavy t-quark partner"],
      "propagator_label": ["uqP", "uP", "cP", "tP"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 8,
      "class_name": "dqP",
      "class_members": ["dP", "sP", "bP"],
      "indices": ["Generation", "Colour"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "mass": {"sym": "MF", "value": "4000."},
      "width": {"sym": "WF", "value": "0."},
      "quantum_numbers": {"Q": "-1/3", "Y": "-1/3"},
      "pdg": [9000001, 9000003, 9000005],
      "particle_name": ["dP", "sP", "bP"],
      "antiparticle_name": ["dP~", "sP~", "bP~"],
      "full_name": ["Heavy d-quark partner", "Heavy s-quark partner", "Heavy b-quark partner"],
      "propagator_label": ["dqP", "dP", "sP", "bP"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [
    ["V[5]", "GaugeXi[Wp]"],
    ["V[6]", "GaugeXi[Zp]"],
    ["S[4]", "GaugeXi[Zp]"],
    ["S[5]", "GaugeXi[Wp]"]
  ],
  "lagrangian_terms": [
    {
      "name": "LWpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/2 FS[Wpbar,mu,nu] FS[Wp,mu,nu] + MWp^2 Wpbar[mu] Wp[mu]]]"
    },
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]]"
    },
    {
      "name": "LGoldPKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[del[GpPbar,mu] del[GpP,mu] - MWp^2 GpPbar GpP + 1/2 del[Gp0,mu] del[Gp0,mu] - 1/2 MZp^2 Gp0 Gp0]]"
    },
    {
      "name": "LHeavyKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I vlPbar.Ga[mu].DC[vlP,mu] - MF vlPbar.vlP + I lPbar.Ga[mu].DC[lP,mu] - MF lPbar.lP + I uqPbar.Ga[mu].DC[uqP,mu] - MF uqPbar.uqP + I dqPbar.Ga[mu].DC[dqP,mu] - MF dqPbar.dqP]]"
    },
    {
      "name": "LWpff",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff,cc,tmp}, tmp = ExpandIndices[gWpf/Sqrt[2] Wp[mu] (QLbar[sp1,1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + LLbar[sp1,1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff])]; tmp + HC[tmp]]"
    },
    {
      "name": "LZpff",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff,cc}, ExpandIndices[gZpf/2 Zp[mu] (QLbar[sp1,1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,1,ff,cc] - QLbar[sp1,2,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + LLbar[sp1,1,ff].Ga[mu,sp1,sp2].LL[sp2,1,ff] - LLbar[sp1,2,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff])]]"
    },
    {
      "name": "LWpFF",
      "delayed": true,
      "expression": "Block[{mu,tmp}, tmp = ExpandIndices[gp1/Sqrt[2] Wp[mu] (uqPbar.Ga[mu].dqP + vlPbar.Ga[mu].lP)]; tmp + HC[tmp]]"
    },
    {
      "name": "LZpFF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[gp1/2 Zp[mu] (uqPbar.Ga[mu].uqP - dqPbar.Ga[mu].dqP + vlPbar.Ga[mu].vlP - lPbar.Ga[mu].lP)]]"
    },
    {
      "name": "LmixCC",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff,cc,tmp}, tmp = ExpandIndices[gWFf/Sqrt[2] W[mu] (uqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + QLbar[sp1,1,ff,cc].Ga[mu,sp1,sp2].dqP[sp2,ff,cc] + vlPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff] + LLbar[sp1,1,ff].Ga[mu,sp1,sp2].lP[sp2,ff]) + gWpFf/Sqrt[2] Wp[mu] (uqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + QLbar[sp1,1,ff,cc].Ga[mu,sp1,sp2].dqP[sp2,ff,cc] + vlPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff] + LLbar[sp1,1,ff].Ga[mu,sp1,sp2].lP[sp2,ff])]; tmp + HC[tmp]]"
    },
    {
      "name": "LmixNC",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff,cc,tmp}, tmp = ExpandIndices[gZFf Z[mu] (uqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,1,ff,cc] - dqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + vlPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,1,ff] - lPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff]) + gZpFf Zp[mu] (uqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,1,ff,cc] - dqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + vlPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,1,ff] - lPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff])]; tmp + HC[tmp]]"
    },
    {
      "name": "LWWpZ",
      "delayed": true,
      "expression": "Block[{mu,nu,tmp}, tmp = ExpandIndices[-I gWWpZ ((FS[Wp,mu,nu] Wbar[mu] - FS[Wbar,mu,nu] Wp[mu]) Z[nu] + FS[Z,mu,nu] Wp[mu] Wbar[nu])]; tmp + HC[tmp]]"
    },
    {
      "name": "LWpWpV",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-I ee ((FS[Wp,mu,nu] Wpbar[mu] - FS[Wpbar,mu,nu] Wp[mu]) A[nu] + FS[A,mu,nu] Wp[mu] Wpbar[nu]) - I gWpWpZ ((FS[Wp,mu,nu] Wpbar[mu] - FS[Wpbar,mu,nu] Wp[mu]) Z[nu] + FS[Z,mu,nu] Wp[mu] Wpbar[nu])]]"
    },
    {
      "name": "LGoldF",
      "delayed": true,
      "expression": "Block[{tmp}, tmp = ExpandIndices[-I Sqrt[2] gGpF GpP (uqPbar.ProjP.dqP - uqPbar.ProjM.dqP + vlPbar.ProjP.lP - vlPbar.ProjM.lP)]; tmp + HC[tmp] + ExpandIndices[I gGpF Gp0 (uqPbar.Ga[5].uqP - dqPbar.Ga[5].dqP + vlPbar.Ga[5].vlP - lPbar.Ga[5].lP)]]"
    },
    {
      "name": "LGoldFf",
      "delayed": true,
      "expression": "Block[{sp1,sp2,ff,cc,tmp}, tmp = ExpandIndices[-I Sqrt[2] gGpF epsL (GpP (uqPbar[sp1,ff,cc].ProjM[sp1,sp2].QL[sp2,2,ff,cc] + vlPbar[sp1,ff].ProjM[sp1,sp2].LL[sp2,2,ff]) + GpPbar (dqPbar[sp1,ff,cc].ProjM[sp1,sp2].QL[sp2,1,ff,cc] + lPbar[sp1,ff].ProjM[sp1,sp2].LL[sp2,1,ff])) + I gGpF epsL Gp0 (uqPbar[sp1,ff,cc].ProjM[sp1,sp2].QL[sp2,1,ff,cc] - dqPbar[sp1,ff,cc].ProjM[sp1,sp2].QL[sp2,2,ff,cc] + vlPbar[sp1,ff].ProjM[sp1,sp2].LL[sp2,1,ff] - lPbar[sp1,ff].ProjM[sp1,sp2].LL[sp2,2,ff]) - I gGpF (epsRd[ff] GpP uqPbar[sp1,ff,cc].ProjP[sp1,sp2].dR[sp2,ff,cc] + epsRu[ff] GpPbar dqPbar[sp1,ff,cc].ProjP[sp1,sp2].uR[sp2,ff,cc] + epsRl[ff] GpP vlPbar[sp1,ff].ProjP[sp1,sp2].lR[sp2,ff])]; tmp + HC[tmp]]"
    },
    {
      "name": "LMHM",
      "delayed": true,
      "expression": "LWpKin + LZpKin + LGoldPKin + LHeavyKin + LWpff + LZpff + LWpFF + LZpFF + LmixCC + LmixNC + LWWpZ + LWpWpV + LGoldF + LGoldFf"
    },
    {
      "name": "LTot",
      "delayed": true,
      "expression": "LSM + LMHM"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper. Note first: the sandbox contains only the paper, the schema, the renderer and `SM.fr`. **No reference or cached `.fr` model file was read — none exists here.**

## What the paper defines

arXiv:1010.3251 is the FeynRules→WHIZARD interface note. Its one extra-dimensional new-physics model is the **Three-Site (Minimal) Higgsless Model**, Section 4.3 + Table 5 + Table 7:

- gauge group = SM plus an extra SU(2) "site"; breaking by non-linear sigma-model link fields `Sigma = 1 + i pi - 1/2 pi^2 + ...` (Eq. 1);
- vector spectrum: photon, W, Z **plus W'± and Z'**;
- **a heavy partner for every SM fermion** — Table 7 shows `u'`, `d'`, `s'`, `c'`, `b'`, `t'`, `e-'`, `mu-'`, `tau-'`, `nu_e'`, `nu_mu'`, `nu_tau'` (trailing prime = heavy partner);
- light–heavy mixing set by the small parameter **eps_L**;
- Feynman-gauge implementation with a Goldstone sector (`LGold`, `LGoldLeptons`, `LGoldQuarks`) → **one new charged and one new neutral Goldstone** (the 3 pions eaten by W' and Z');
- benchmark values (Table 5): **M_W' = 500 GeV, M_F = 4 TeV**;
- the model is non-renormalizable; the paper drops the sigma-model operators above dimension four with `MaxCanonicalDimension->4`. So every term below has d = 4 and **no `1/Lambda^n` factor is needed**.

Assumption I state openly: the paper gives the spectrum and benchmark point but not the explicit Lagrangian, so the coefficients below are written in the standard three-site form, in terms of `eps_L`, the site-1 coupling `gp1` and the link decay constant `fpi`.

## Mandatory self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L number | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWpKin | FS[Wpbar]FS[Wp]; Wpbar Wp | 4; 2 | 1; MWp^2 | 0; 2 | n/a | −1+1=0 | n/a (mass eigenstate) | singlet | singlet | none | 0 | n/a | self-conjugate |
| LZpKin | FS[Zp]FS[Zp]; Zp Zp | 4; 2 | 1; MZp^2 | 0; 2 | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | self-conjugate |
| LGoldPKin | del GpPbar del GpP; del Gp0 del Gp0 | 4 | 1; MWp^2/MZp^2 | 0; 2 | n/a | −1+1=0; 0 | n/a | singlet | singlet | none | 0 | n/a | self-conjugate |
| LHeavyKin | psiPbar Ga DC psiP; MF psiPbar psiP | 4; 3 | 1; MF | 0; 1 | n/a | 0 | −q+q=0 | singlet | 3bar⊗3 | none | 0 | n/a | self-conjugate |
| LWpff | Wp QLbar[1] Ga QL[2]; Wp LLbar[1] Ga LL[2] | 4 | gWpf | 0 | n/a | +1−2/3−1/3=0; +1+0−1=0 | −1/6+1/6=0 | explicit doublet components 1,2 | 3bar⊗3 | none | 0 | n/a | HC[tmp] |
| LZpff | Zp QLbar[i] Ga QL[i]; Zp LLbar[i] Ga LL[i] | 4 | gZpf | 0 | n/a | 0 | −1/6+1/6=0 | shared component index | 3bar⊗3 | none | 0 | n/a | self-conjugate |
| LWpFF | Wp uqPbar Ga dqP; Wp vlPbar Ga lP | 4 | gp1 | 0 | n/a | +1−2/3−1/3=0; 0 | −2/3−1/3 → broken phase (note) | singlet | 3bar⊗3 | none | −1+1=0 | n/a | HC[tmp] |
| LZpFF | Zp uqPbar Ga uqP … | 4 | gp1 | 0 | n/a | 0 | −q+q=0 | singlet | 3bar⊗3 | none | 0 | n/a | self-conjugate |
| LmixCC | W/Wp uqPbar Ga QL[2] etc. | 4 | gWFf, gWpFf | 0 | n/a | 0 | broken phase (note) | explicit doublet component | 3bar⊗3 | none | 0 | n/a | HC[tmp] |
| LmixNC | Z/Zp uqPbar Ga QL[1] etc. | 4 | gZFf, gZpFf | 0 | n/a | 0 | broken phase (note) | explicit doublet component | 3bar⊗3 | none | 0 | n/a | HC[tmp] |
| LWWpZ | FS[Wp] Wbar Z, FS[Z] Wp Wbar | 4 | gWWpZ | 0 | n/a | +1−1+0=0 | broken phase | singlet | singlet | none | 0 | n/a | HC[tmp] |
| LWpWpV | FS[Wp] Wpbar A/Z … | 4 | ee, gWpWpZ | 0 | n/a | +1−1=0 | broken phase | singlet | singlet | none | 0 | n/a | self-conjugate (checked term by term) |
| LGoldF | GpP uqPbar P dqP; Gp0 psiPbar Ga5 psiP | 4 | gGpF | 0 | n/a | +1−2/3−1/3=0; 0 | broken phase | singlet | 3bar⊗3 | none | 0 | n/a | HC[tmp] / self-conj. Gp0 part |
| LGoldFf | GpP uqPbar P QL[2]; GpPbar dqPbar P QL[1]; GpP uqPbar P dR; GpPbar dqPbar P uR; GpP vlPbar P lR; Gp0 …| 4 | gGpF·epsL, gGpF·epsR | 0 | n/a | +1−2/3−1/3=0; −1+1/3+2/3=0; +1+0−1=0 | broken phase | explicit doublet component | 3bar⊗3 | none | −1+1=0 | n/a | HC[tmp] |

Free-field rows (rule 1): `Wp` → LWpKin; `Zp` → LZpKin; `GpP`, `Gp0` → LGoldPKin; `vlP`, `lP`, `uqP`, `dqP` → LHeavyKin. All four terms are in the total sum `LMHM`, and `LMHM` is in `LTot`.

`SelfConjugate -> True` classes: **`Zp` (V[6])** and **`Gp0` (S[4])** — both carry **no** `QuantumNumbers`.

Y-column note (honest statement): only `QL`, `LL`, `uR`, `dR`, `lR` and the four heavy vector-like classes are U(1)_Y eigenstates, so the Y sum is exact for `LWpff`, `LZpff` and `LHeavyKin`. `W`, `Z`, `Wp`, `Zp`, `GpP`, `Gp0` are broken-phase mass eigenstates and carry no Y, so Y is not a good quantum number for the mixing terms; those terms are exactly Q-, colour- and lepton-number-neutral, which is what the broken phase conserves.

Reference/cached model file read: **none**.

```json
{
  "model_name": "CHEIDI_gen",
  "info": {
    "authors": ["N. D. Christensen", "C. Duhr", "B. Fuks", "J. Reuter", "C. Speckner"],
    "version": "1.0",
    "date": "26. 04. 2012",
    "institutions": ["University of Pittsburgh", "IPPP Durham", "IPHC Strasbourg / University of Strasbourg", "DESY Theory Group", "Albert-Ludwigs-Universitaet Freiburg"],
    "emails": ["neilc@pitt.edu", "claude.duhr@durham.ac.uk", "benjamin.fuks@iphc.cnrs.fr", "juergen.reuter@desy.de", "christian.speckner@physik.uni-freiburg.de"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "feynman_gauge": true,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "epsL",
      "parameter_type": "External",
      "value": "0.05",
      "block_name": "MHM",
      "order_block": 1,
      "tex": "Subscript[\\[Epsilon], L]",
      "description": "Light fermion delocalization parameter eps_L. It sets the mixing of the light fermions with their heavy partners and is adjusted to satisfy the precision constraints (S parameter)."
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "MWp",
      "tex": "Subscript[M, Zp]",
      "description": "Z' mass [GeV]. The Z' is degenerate with the W' at leading order in the three-site model."
    },
    {
      "name": "xg",
      "parameter_type": "Internal",
      "value": "Sqrt[2]*MW/MWp",
      "tex": "x",
      "description": "Small ratio x = g0/g1 of the SU(2)_0 and the SU(2)_1 gauge couplings of the three-site model."
    },
    {
      "name": "gp1",
      "parameter_type": "Internal",
      "value": "gw/xg",
      "interaction_order": ["QED", 1],
      "tex": "Subscript[g, 1]",
      "description": "Gauge coupling of the new (site 1) SU(2) gauge group."
    },
    {
      "name": "fpi",
      "parameter_type": "Internal",
      "value": "2*MWp/gp1",
      "interaction_order": ["QED", -1],
      "tex": "f",
      "description": "Decay constant [GeV] of the non-linear sigma model link fields Sigma = 1 + I pi - 1/2 pi^2 + ... , Eq.(1)."
    },
    {
      "name": "gWpf",
      "parameter_type": "Internal",
      "value": "gw*epsL^2/2",
      "interaction_order": ["QED", 1],
      "description": "W' coupling to the light left-handed fermion currents. It is suppressed by the square of the delocalization parameter."
    },
    {
      "name": "gZpf",
      "parameter_type": "Internal",
      "value": "gw*epsL^2/(2*cw)",
      "interaction_order": ["QED", 1],
      "description": "Z' coupling to the light left-handed fermion currents."
    },
    {
      "name": "gWFf",
      "parameter_type": "Internal",
      "value": "gw*epsL/2",
      "interaction_order": ["QED", 1],
      "description": "W coupling of one heavy and one light fermion."
    },
    {
      "name": "gZFf",
      "parameter_type": "Internal",
      "value": "gw*epsL/(2*cw)",
      "interaction_order": ["QED", 1],
      "description": "Z coupling of one heavy and one light fermion."
    },
    {
      "name": "gWpFf",
      "parameter_type": "Internal",
      "value": "gp1*epsL/2",
      "interaction_order": ["QED", 1],
      "description": "W' coupling of one heavy and one light fermion."
    },
    {
      "name": "gZpFf",
      "parameter_type": "Internal",
      "value": "gp1*epsL/2",
      "interaction_order": ["QED", 1],
      "description": "Z' coupling of one heavy and one light fermion."
    },
    {
      "name": "gWWpZ",
      "parameter_type": "Internal",
      "value": "gw*cw*xg",
      "interaction_order": ["QED", 1],
      "description": "W W' Z triple gauge coupling."
    },
    {
      "name": "gWpWpZ",
      "parameter_type": "Internal",
      "value": "gw*cw",
      "interaction_order": ["QED", 1],
      "description": "W' W' Z triple gauge coupling."
    },
    {
      "name": "gGpF",
      "parameter_type": "Internal",
      "value": "MF/fpi",
      "interaction_order": ["QED", 1],
      "description": "Coupling of the heavy site-1 fermions to the new Goldstone bosons of the W' and the Z'."
    },
    {
      "name": "epsRu",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "epsRu[1]", "rhs": "Sqrt[2]*MU/(epsL*MF)"},
        {"lhs": "epsRu[2]", "rhs": "Sqrt[2]*MC/(epsL*MF)"},
        {"lhs": "epsRu[3]", "rhs": "Sqrt[2]*MT/(epsL*MF)"}
      ],
      "tex": "Superscript[Subscript[\\[Epsilon], R], u]",
      "description": "Right-handed mixing of the up-type quarks with their heavy partners, fixed by m_f = epsL epsR MF / Sqrt[2]."
    },
    {
      "name": "epsRd",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "epsRd[1]", "rhs": "Sqrt[2]*MD/(epsL*MF)"},
        {"lhs": "epsRd[2]", "rhs": "Sqrt[2]*MS/(epsL*MF)"},
        {"lhs": "epsRd[3]", "rhs": "Sqrt[2]*MB/(epsL*MF)"}
      ],
      "tex": "Superscript[Subscript[\\[Epsilon], R], d]",
      "description": "Right-handed mixing of the down-type quarks with their heavy partners."
    },
    {
      "name": "epsRl",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "epsRl[1]", "rhs": "Sqrt[2]*Me/(epsL*MF)"},
        {"lhs": "epsRl[2]", "rhs": "Sqrt[2]*MMU/(epsL*MF)"},
        {"lhs": "epsRl[3]", "rhs": "Sqrt[2]*MTA/(epsL*MF)"}
      ],
      "tex": "Superscript[Subscript[\\[Epsilon], R], l]",
      "description": "Right-handed mixing of the charged leptons with their heavy partners."
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 5,
      "class_name": "Wp",
      "self_conjugate": false,
      "mass": {"sym": "MWp", "value": "500."},
      "width": {"sym": "WWp", "value": "0."},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9000024,
      "particle_name": "W'+",
      "antiparticle_name": "W'-",
      "full_name": "Heavy charged gauge boson W'",
      "propagator_label": "Wp",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 6,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "0."},
      "pdg": 9000023,
      "particle_name": "Z'",
      "full_name": "Heavy neutral gauge boson Z'",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 4,
      "class_name": "Gp0",
      "self_conjugate": true,
      "goldstone": "Zp",
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "0."},
      "pdg": 9000250,
      "particle_name": "Gp0",
      "full_name": "Neutral Goldstone boson of the Z'",
      "propagator_label": "Gp0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 5,
      "class_name": "GpP",
      "self_conjugate": false,
      "goldstone": "Wp",
      "mass": {"sym": "MWp", "value": "500."},
      "width": {"sym": "WWp", "value": "0."},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9000251,
      "particle_name": "Gp+",
      "antiparticle_name": "Gp-",
      "full_name": "Charged Goldstone boson of the W'",
      "propagator_label": "GpP",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 5,
      "class_name": "vlP",
      "class_members": ["veP", "vmP", "vtP"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "mass": {"sym": "MF", "value": "4000."},
      "width": {"sym": "WF", "value": "0."},
      "quantum_numbers": {"Y": "0", "LeptonNumber": "1"},
      "pdg": [9000012, 9000014, 9000016],
      "particle_name": ["veP", "vmP", "vtP"],
      "antiparticle_name": ["veP~", "vmP~", "vtP~"],
      "full_name": ["Heavy electron-neutrino partner", "Heavy mu-neutrino partner", "Heavy tau-neutrino partner"],
      "propagator_label": ["vP", "veP", "vmP", "vtP"],
      "propagator_type": "S",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 6,
      "class_name": "lP",
      "class_members": ["eP", "muP", "taP"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "mass": {"sym": "MF", "value": "4000."},
      "width": {"sym": "WF", "value": "0."},
      "quantum_numbers": {"Q": "-1", "Y": "-1", "LeptonNumber": "1"},
      "pdg": [9000011, 9000013, 9000015],
      "particle_name": ["eP-", "muP-", "taP-"],
      "antiparticle_name": ["eP+", "muP+", "taP+"],
      "full_name": ["Heavy electron partner", "Heavy muon partner", "Heavy tau partner"],
      "propagator_label": ["lP", "eP", "muP", "taP"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 7,
      "class_name": "uqP",
      "class_members": ["uP", "cP", "tP"],
      "indices": ["Generation", "Colour"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "mass": {"sym": "MF", "value": "4000."},
      "width": {"sym": "WF", "value": "0."},
      "quantum_numbers": {"Q": "2/3", "Y": "2/3"},
      "pdg": [9000002, 9000004, 9000006],
      "particle_name": ["uP", "cP", "tP"],
      "antiparticle_name": ["uP~", "cP~", "tP~"],
      "full_name": ["Heavy u-quark partner", "Heavy c-quark partner", "Heavy t-quark partner"],
      "propagator_label": ["uqP", "uP", "cP", "tP"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 8,
      "class_name": "dqP",
      "class_members": ["dP", "sP", "bP"],
      "indices": ["Generation", "Colour"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "mass": {"sym": "MF", "value": "4000."},
      "width": {"sym": "WF", "value": "0."},
      "quantum_numbers": {"Q": "-1/3", "Y": "-1/3"},
      "pdg": [9000001, 9000003, 9000005],
      "particle_name": ["dP", "sP", "bP"],
      "antiparticle_name": ["dP~", "sP~", "bP~"],
      "full_name": ["Heavy d-quark partner", "Heavy s-quark partner", "Heavy b-quark partner"],
      "propagator_label": ["dqP", "dP", "sP", "bP"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [
    ["V[5]", "GaugeXi[Wp]"],
    ["V[6]", "GaugeXi[Zp]"],
    ["S[4]", "GaugeXi[Zp]"],
    ["S[5]", "GaugeXi[Wp]"]
  ],
  "lagrangian_terms": [
    {
      "name": "LWpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/2 FS[Wpbar,mu,nu] FS[Wp,mu,nu] + MWp^2 Wpbar[mu] Wp[mu]]]"
    },
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]]"
    },
    {
      "name": "LGoldPKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[del[GpPbar,mu] del[GpP,mu] - MWp^2 GpPbar GpP + 1/2 del[Gp0,mu] del[Gp0,mu] - 1/2 MZp^2 Gp0 Gp0]]"
    },
    {
      "name": "LHeavyKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I vlPbar.Ga[mu].DC[vlP,mu] - MF vlPbar.vlP + I lPbar.Ga[mu].DC[lP,mu] - MF lPbar.lP + I uqPbar.Ga[mu].DC[uqP,mu] - MF uqPbar.uqP + I dqPbar.Ga[mu].DC[dqP,mu] - MF dqPbar.dqP]]"
    },
    {
      "name": "LWpff",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff,cc,tmp}, tmp = ExpandIndices[gWpf/Sqrt[2] Wp[mu] (QLbar[sp1,1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + LLbar[sp1,1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff])]; tmp + HC[tmp]]"
    },
    {
      "name": "LZpff",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff,cc}, ExpandIndices[gZpf/2 Zp[mu] (QLbar[sp1,1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,1,ff,cc] - QLbar[sp1,2,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + LLbar[sp1,1,ff].Ga[mu,sp1,sp2].LL[sp2,1,ff] - LLbar[sp1,2,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff])]]"
    },
    {
      "name": "LWpFF",
      "delayed": true,
      "expression": "Block[{mu,tmp}, tmp = ExpandIndices[gp1/Sqrt[2] Wp[mu] (uqPbar.Ga[mu].dqP + vlPbar.Ga[mu].lP)]; tmp + HC[tmp]]"
    },
    {
      "name": "LZpFF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[gp1/2 Zp[mu] (uqPbar.Ga[mu].uqP - dqPbar.Ga[mu].dqP + vlPbar.Ga[mu].vlP - lPbar.Ga[mu].lP)]]"
    },
    {
      "name": "LmixCC",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff,cc,tmp}, tmp = ExpandIndices[gWFf/Sqrt[2] W[mu] (uqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + QLbar[sp1,1,ff,cc].Ga[mu,sp1,sp2].dqP[sp2,ff,cc] + vlPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff] + LLbar[sp1,1,ff].Ga[mu,sp1,sp2].lP[sp2,ff]) + gWpFf/Sqrt[2] Wp[mu] (uqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + QLbar[sp1,1,ff,cc].Ga[mu,sp1,sp2].dqP[sp2,ff,cc] + vlPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff] + LLbar[sp1,1,ff].Ga[mu,sp1,sp2].lP[sp2,ff])]; tmp + HC[tmp]]"
    },
    {
      "name": "LmixNC",
      "delayed": true,
      "expression": "Block[{mu,sp1,sp2,ff,cc,tmp}, tmp = ExpandIndices[gZFf Z[mu] (uqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,1,ff,cc] - dqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + vlPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,1,ff] - lPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff]) + gZpFf Zp[mu] (uqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,1,ff,cc] - dqPbar[sp1,ff,cc].Ga[mu,sp1,sp2].QL[sp2,2,ff,cc] + vlPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,1,ff] - lPbar[sp1,ff].Ga[mu,sp1,sp2].LL[sp2,2,ff])]; tmp + HC[tmp]]"
    },
    {
      "name": "LWWpZ",
      "delayed": true,
      "expression": "Block[{mu,nu,tmp}, tmp = ExpandIndices[-I gWWpZ ((FS[Wp,mu,nu] Wbar[mu] - FS[Wbar,mu,nu] Wp[mu]) Z[nu] + FS[Z,mu,nu] Wp[mu] Wbar[nu])]; tmp + HC[tmp]]"
    },
    {
      "name": "LWpWpV",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-I ee ((FS[Wp,mu,nu] Wpbar[mu] - FS[Wpbar,mu,nu] Wp[mu]) A[nu] + FS[A,mu,nu] Wp[mu] Wpbar[nu]) - I gWpWpZ ((FS[Wp,mu,nu] Wpbar[mu] - FS[Wpbar,mu,nu] Wp[mu]) Z[nu] + FS[Z,mu,nu] Wp[mu] Wpbar[nu])]]"
    },
    {
      "name": "LGoldF",
      "delayed": true,
      "expression": "Block[{tmp}, tmp = ExpandIndices[-I Sqrt[2] gGpF GpP (uqPbar.ProjP.dqP - uqPbar.ProjM.dqP + vlPbar.ProjP.lP - vlPbar.ProjM.lP)]; tmp + HC[tmp] + ExpandIndices[I gGpF Gp0 (uqPbar.Ga[5].uqP - dqPbar.Ga[5].dqP + vlPbar.Ga[5].vlP - lPbar.Ga[5].lP)]]"
    },
    {
      "name": "LGoldFf",
      "delayed": true,
      "expression": "Block[{sp1,sp2,ff,cc,tmp}, tmp = ExpandIndices[-I Sqrt[2] gGpF epsL (GpP (uqPbar[sp1,ff,cc].ProjM[sp1,sp2].QL[sp2,2,ff,cc] + vlPbar[sp1,ff].ProjM[sp1,sp2].LL[sp2,2,ff]) + GpPbar (dqPbar[sp1,ff,cc].ProjM[sp1,sp2].QL[sp2,1,ff,cc] + lPbar[sp1,ff].ProjM[sp1,sp2].LL[sp2,1,ff])) + I gGpF epsL Gp0 (uqPbar[sp1,ff,cc].ProjM[sp1,sp2].QL[sp2,1,ff,cc] - dqPbar[sp1,ff,cc].ProjM[sp1,sp2].QL[sp2,2,ff,cc] + vlPbar[sp1,ff].ProjM[sp1,sp2].LL[sp2,1,ff] - lPbar[sp1,ff].ProjM[sp1,sp2].LL[sp2,2,ff]) - I gGpF (epsRd[ff] GpP uqPbar[sp1,ff,cc].ProjP[sp1,sp2].dR[sp2,ff,cc] + epsRu[ff] GpPbar dqPbar[sp1,ff,cc].ProjP[sp1,sp2].uR[sp2,ff,cc] + epsRl[ff] GpP vlPbar[sp1,ff].ProjP[sp1,sp2].lR[sp2,ff])]; tmp + HC[tmp]]"
    },
    {
      "name": "LMHM",
      "delayed": true,
      "expression": "LWpKin + LZpKin + LGoldPKin + LHeavyKin + LWpff + LZpff + LWpFF + LZpFF + LmixCC + LmixNC + LWWpZ + LWpWpV + LGoldF + LGoldFf"
    },
    {
      "name": "LTot",
      "delayed": true,
      "expression": "LSM + LMHM"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```