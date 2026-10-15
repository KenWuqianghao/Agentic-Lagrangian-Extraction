# Self-audit table (before the model)

Paper: Andrea, Fuks, Maltoni, "Monotops at the LHC" (arXiv:1106.6199), Eq. (1). All new-physics operators are dimension‑4 (renormalizable simplified model); no `1/Lambda` suppression appears anywhere in the paper, so rule 30 (EFT cutoffs) does not apply to any term.

Charge convention used throughout: for a Dirac field χ of physical charge Q(χ), the barred field contributes −Q(χ), the charge‑conjugate field χ^c contributes −Q(χ), and its bar `bar[CC[χ]]` contributes +Q(χ). Re‑deriving from Eq. (1): φ, V, χ (the "missing energy" fields) are colour‑singlet and electrically neutral; varphi (vphi) has Q=+2/3, colour triplet; tilde‑varphi (vphit) has Q=−1/3, colour triplet; X has Q=+2/3, colour triplet. All are SU(2)×U(1) singlets (paper states the Lagrangian is already "in terms of mass eigenstates" — no doublet structure survives), so Y=Q and rule 4/5 (doublet contractions, new U(1) charges) do not apply.

| term | fields | dim d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new‑U(1) | B/L sum | CC[] used | fraction/root check | HC partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `Lphikin` | phi·phi (real scalar kin+mass) | 4 | n/a | n/a | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self‑conjugate |
| `LVkin` | V·V (real vector kin+mass) | 4 | n/a | n/a | n/a | 0 | 0 | singlet | singlet | n/a | 0 | n/a | n/a | self‑conjugate |
| `Lchikin` | chibar·chi (Dirac kin+mass) | 4 | n/a | n/a | n/a | 0 | 0 | singlet | singlet | n/a | 0 (χ assigned no B/L) | n/a | n/a | HC (Dirac) |
| `Lvphikin` | vphibar·vphi | 4 | n/a | n/a | n/a | 0 | 0 | singlet | 3⊗3̄→1 | n/a | 0 | n/a | n/a | self‑contained (complex field) |
| `Lvphitkin` | vphitbar·vphit | 4 | n/a | n/a | n/a | 0 | 0 | singlet | 3⊗3̄→1 | n/a | 0 | n/a | n/a | self‑contained |
| `LXkin` | Xbar·X | 4 | n/a | n/a | n/a | 0 | 0 | singlet | 3⊗3̄→1 | n/a | 0 | n/a | n/a | self‑contained |
| `Lphiu` | phi, uqbar, uq | 1+3/2+3/2=4 | a0FC,b0FC | 0 (dimensionless) | n/a | 0+(−2/3)+2/3=0 | same | singlet×singlet | 3⊗3̄→1 | n/a | 0 | n/a | n/a (no frac/root, plain matrix) | self‑Hermitian (φ real, a0FC symmetric benchmark) |
| `LVu` | V, uqbar, uq | 4 | a1FC,b1FC | 0 | n/a | 0 | 0 | singlet | 3⊗3̄→1 | n/a | 0 | n/a | n/a | self‑Hermitian |
| `LvphiDiquark` | vphi, bar[CC[dq]], dq, Eps | 1+3/2+3/2=4 | aqSR,bqSR | 0 | n/a | 2/3+(−1/3)+(−1/3)=0 | same | singlet | Eps₃, 3⊗3⊗3→1 | n/a | ΔB=−1 (paper: baryon‑number‑violating, by design) | yes (bar[CC[dq]]) | n/a | +HC[...] |
| `LvphiChi` | vphi, uqbar, chi | 4 | ahalfSR,bhalfSR | 0 | n/a | 2/3+(−2/3)+0=0 | same | singlet | 3⊗3̄→1 | n/a | 0 | n/a | n/a | +HC[...] |
| `LvphitDiquark` | vphit, bar[CC[dq]], uq, Eps | 4 | atildeqSR,btildeqSR | 0 | n/a | −1/3+(−1/3)+2/3=0 | same | singlet | Eps₃ | n/a | ΔB≠0 (4‑fermion BNV limit) | yes | n/a | +HC[...] |
| `LvphitChi` | vphit, dqbar, chi | 4 | atildehalfSR,btildehalfSR | 0 | n/a | −1/3+1/3+0=0 | same | singlet | 3⊗3̄→1 | n/a | 0 | n/a | n/a | +HC[...] |
| `LXDiquark` | X, bar[CC[dq]], dq, Eps | 1+3/2+3/2=4 | aqVR,bqVR | 0 | n/a | 2/3+(−1/3)+(−1/3)=0 | same | singlet | Eps₃ | n/a | ΔB=−1 | yes | n/a | +HC[...] |
| `LXChi` | X, uqbar, chi | 4 | ahalfVR,bhalfVR | 0 | n/a | 2/3+(−2/3)+0=0 | same | singlet | 3⊗3̄→1 | n/a | 0 | n/a | n/a | +HC[...] |

Free-field confirmation: every new class (phi, V, chi, vphi, vphit, X) has a kinetic+mass row above, and all six appear in `LTotal`.

No non‑fundamental colour representation is used (vphi/vphit/X are ordinary fundamental triplets like SM quarks), so `AddGaugeRepresentation[...]` is not required and `raw_preamble` is empty.

`SelfConjugate -> True` classes: `phi`, `V`. Both carry no `QuantumNumbers` (Q=0, omitted).

Names chosen: `phi, V, chi, vphi, vphit, X` (particles); `Mphi, MV, Mchi, Mvphi, Mvphit, MX, Wphi, WV, Wchi, Wvphi, Wvphit, WX` (masses/widths); `a0FC, b0FC, a1FC, b1FC, aqSR, bqSR, atildeqSR, btildeqSR, aqVR, bqVR, ahalfSR, bhalfSR, atildehalfSR, btildehalfSR, ahalfVR, bhalfVR` (couplings). None collides with a Mathematica built-in, a FeynRules symbol (`HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM,N,C,D,E,I,K,O`), or an SM.fr name (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,uq,dq,l,vl,QL,LL,uR,dR,lR`).

Single total: `LTotal` sums `Lphikin, LVkin, Lchikin, Lvphikin, Lvphitkin, LXkin, Lphiu, LVu, LvphiDiquark, LvphiChi, LvphitDiquark, LvphitChi, LXDiquark, LXChi`.

Reference/cached model file read: **none**. Only the paper's LaTeX source, `frmodel.py` and `SM.fr` (as instructed) were read.

```json
{
  "model_name": "Monotops_gen",
  "info": {
    "authors": ["J. Andrea", "B. Fuks", "F. Maltoni"],
    "version": "1.0",
    "date": "2011.06.30",
    "institutions": ["IPHC Strasbourg / Universite de Strasbourg", "CP3, Universite catholique de Louvain"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {"name": "a0FC", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "a0FC[1,1]", "rhs": "0."}, {"lhs": "a0FC[1,2]", "rhs": "0."}, {"lhs": "a0FC[1,3]", "rhs": "0.1"},
       {"lhs": "a0FC[2,1]", "rhs": "0."}, {"lhs": "a0FC[2,2]", "rhs": "0."}, {"lhs": "a0FC[2,3]", "rhs": "0."},
       {"lhs": "a0FC[3,1]", "rhs": "0.1"}, {"lhs": "a0FC[3,2]", "rhs": "0."}, {"lhs": "a0FC[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Scalar phi FCNC coupling to u-type quarks, Eq.(1)"},
    {"name": "b0FC", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "b0FC[1,1]", "rhs": "0."}, {"lhs": "b0FC[1,2]", "rhs": "0."}, {"lhs": "b0FC[1,3]", "rhs": "0."},
       {"lhs": "b0FC[2,1]", "rhs": "0."}, {"lhs": "b0FC[2,2]", "rhs": "0."}, {"lhs": "b0FC[2,3]", "rhs": "0."},
       {"lhs": "b0FC[3,1]", "rhs": "0."}, {"lhs": "b0FC[3,2]", "rhs": "0."}, {"lhs": "b0FC[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Scalar phi axial FCNC coupling to u-type quarks; zero at benchmark, Eq.(1)"},
    {"name": "a1FC", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "a1FC[1,1]", "rhs": "0."}, {"lhs": "a1FC[1,2]", "rhs": "0."}, {"lhs": "a1FC[1,3]", "rhs": "0.1"},
       {"lhs": "a1FC[2,1]", "rhs": "0."}, {"lhs": "a1FC[2,2]", "rhs": "0."}, {"lhs": "a1FC[2,3]", "rhs": "0."},
       {"lhs": "a1FC[3,1]", "rhs": "0.1"}, {"lhs": "a1FC[3,2]", "rhs": "0."}, {"lhs": "a1FC[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Vector V FCNC coupling to u-type quarks, Eq.(1)"},
    {"name": "b1FC", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "b1FC[1,1]", "rhs": "0."}, {"lhs": "b1FC[1,2]", "rhs": "0."}, {"lhs": "b1FC[1,3]", "rhs": "0."},
       {"lhs": "b1FC[2,1]", "rhs": "0."}, {"lhs": "b1FC[2,2]", "rhs": "0."}, {"lhs": "b1FC[2,3]", "rhs": "0."},
       {"lhs": "b1FC[3,1]", "rhs": "0."}, {"lhs": "b1FC[3,2]", "rhs": "0."}, {"lhs": "b1FC[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Vector V axial FCNC coupling to u-type quarks; zero at benchmark, Eq.(1)"},
    {"name": "aqSR", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "aqSR[1,1]", "rhs": "0."}, {"lhs": "aqSR[1,2]", "rhs": "0.1"}, {"lhs": "aqSR[1,3]", "rhs": "0."},
       {"lhs": "aqSR[2,1]", "rhs": "-0.1"}, {"lhs": "aqSR[2,2]", "rhs": "0."}, {"lhs": "aqSR[2,3]", "rhs": "0."},
       {"lhs": "aqSR[3,1]", "rhs": "0."}, {"lhs": "aqSR[3,2]", "rhs": "0."}, {"lhs": "aqSR[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Scalar diquark vphi-d-d coupling, antisymmetric, Eq.(1)"},
    {"name": "bqSR", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "bqSR[1,1]", "rhs": "0."}, {"lhs": "bqSR[1,2]", "rhs": "0."}, {"lhs": "bqSR[1,3]", "rhs": "0."},
       {"lhs": "bqSR[2,1]", "rhs": "0."}, {"lhs": "bqSR[2,2]", "rhs": "0."}, {"lhs": "bqSR[2,3]", "rhs": "0."},
       {"lhs": "bqSR[3,1]", "rhs": "0."}, {"lhs": "bqSR[3,2]", "rhs": "0."}, {"lhs": "bqSR[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Scalar diquark vphi-d-d axial coupling; zero at benchmark, Eq.(1)"},
    {"name": "ahalfSR", "parameter_type": "External", "indices": ["Generation"],
     "value_rules": [
       {"lhs": "ahalfSR[1]", "rhs": "0."}, {"lhs": "ahalfSR[2]", "rhs": "0."}, {"lhs": "ahalfSR[3]", "rhs": "0.1"}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "vphi-u-chi scalar coupling, Eq.(1)"},
    {"name": "bhalfSR", "parameter_type": "External", "indices": ["Generation"],
     "value_rules": [
       {"lhs": "bhalfSR[1]", "rhs": "0."}, {"lhs": "bhalfSR[2]", "rhs": "0."}, {"lhs": "bhalfSR[3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "vphi-u-chi axial coupling; zero at benchmark, Eq.(1)"},
    {"name": "atildeqSR", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "atildeqSR[1,1]", "rhs": "0."}, {"lhs": "atildeqSR[1,2]", "rhs": "0."}, {"lhs": "atildeqSR[1,3]", "rhs": "0.1"},
       {"lhs": "atildeqSR[2,1]", "rhs": "0."}, {"lhs": "atildeqSR[2,2]", "rhs": "0."}, {"lhs": "atildeqSR[2,3]", "rhs": "0.1"},
       {"lhs": "atildeqSR[3,1]", "rhs": "0."}, {"lhs": "atildeqSR[3,2]", "rhs": "0."}, {"lhs": "atildeqSR[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Scalar diquark vphitilde-d-u coupling, four-fermion limit, Eq.(1)"},
    {"name": "btildeqSR", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "btildeqSR[1,1]", "rhs": "0."}, {"lhs": "btildeqSR[1,2]", "rhs": "0."}, {"lhs": "btildeqSR[1,3]", "rhs": "0."},
       {"lhs": "btildeqSR[2,1]", "rhs": "0."}, {"lhs": "btildeqSR[2,2]", "rhs": "0."}, {"lhs": "btildeqSR[2,3]", "rhs": "0."},
       {"lhs": "btildeqSR[3,1]", "rhs": "0."}, {"lhs": "btildeqSR[3,2]", "rhs": "0."}, {"lhs": "btildeqSR[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Scalar diquark vphitilde-d-u axial coupling; zero at benchmark, Eq.(1)"},
    {"name": "atildehalfSR", "parameter_type": "External", "indices": ["Generation"],
     "value_rules": [
       {"lhs": "atildehalfSR[1]", "rhs": "0.1"}, {"lhs": "atildehalfSR[2]", "rhs": "0.1"}, {"lhs": "atildehalfSR[3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "vphitilde-d-chi scalar coupling, four-fermion limit, Eq.(1)"},
    {"name": "btildehalfSR", "parameter_type": "External", "indices": ["Generation"],
     "value_rules": [
       {"lhs": "btildehalfSR[1]", "rhs": "0."}, {"lhs": "btildehalfSR[2]", "rhs": "0."}, {"lhs": "btildehalfSR[3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "vphitilde-d-chi axial coupling; zero at benchmark, Eq.(1)"},
    {"name": "aqVR", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "aqVR[1,1]", "rhs": "0.1"}, {"lhs": "aqVR[1,2]", "rhs": "0."}, {"lhs": "aqVR[1,3]", "rhs": "0."},
       {"lhs": "aqVR[2,1]", "rhs": "0."}, {"lhs": "aqVR[2,2]", "rhs": "0."}, {"lhs": "aqVR[2,3]", "rhs": "0."},
       {"lhs": "aqVR[3,1]", "rhs": "0."}, {"lhs": "aqVR[3,2]", "rhs": "0."}, {"lhs": "aqVR[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Vector diquark X-d-d coupling, symmetric, Eq.(1)"},
    {"name": "bqVR", "parameter_type": "External", "indices": ["Generation", "Generation"],
     "value_rules": [
       {"lhs": "bqVR[1,1]", "rhs": "0."}, {"lhs": "bqVR[1,2]", "rhs": "0."}, {"lhs": "bqVR[1,3]", "rhs": "0."},
       {"lhs": "bqVR[2,1]", "rhs": "0."}, {"lhs": "bqVR[2,2]", "rhs": "0."}, {"lhs": "bqVR[2,3]", "rhs": "0."},
       {"lhs": "bqVR[3,1]", "rhs": "0."}, {"lhs": "bqVR[3,2]", "rhs": "0."}, {"lhs": "bqVR[3,3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "Vector diquark X-d-d axial coupling; vanishes for identical quarks, Eq.(1)"},
    {"name": "ahalfVR", "parameter_type": "External", "indices": ["Generation"],
     "value_rules": [
       {"lhs": "ahalfVR[1]", "rhs": "0."}, {"lhs": "ahalfVR[2]", "rhs": "0."}, {"lhs": "ahalfVR[3]", "rhs": "0.1"}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "X-u-chi vector coupling, Eq.(1)"},
    {"name": "bhalfVR", "parameter_type": "External", "indices": ["Generation"],
     "value_rules": [
       {"lhs": "bhalfVR[1]", "rhs": "0."}, {"lhs": "bhalfVR[2]", "rhs": "0."}, {"lhs": "bhalfVR[3]", "rhs": "0."}
     ],
     "block_name": "MONOTOP", "interaction_order": ["NP", 1],
     "description": "X-u-chi axial coupling; zero at benchmark, Eq.(1)"}
  ],
  "particles": [
    {"spin_type": "S", "class_index": 100, "class_name": "phi", "self_conjugate": true,
     "mass": {"sym": "Mphi", "value": "300."}, "width": {"sym": "Wphi", "value": "0."},
     "pdg": 9900001, "particle_name": "phi0", "full_name": "Monotop missing-energy scalar"},
    {"spin_type": "V", "class_index": 101, "class_name": "V", "self_conjugate": true,
     "mass": {"sym": "MV", "value": "50."}, "width": {"sym": "WV", "value": "0."},
     "pdg": 9900002, "particle_name": "V0", "full_name": "Monotop missing-energy vector"},
    {"spin_type": "F", "class_index": 102, "class_name": "chi", "self_conjugate": false,
     "mass": {"sym": "Mchi", "value": "50."}, "width": {"sym": "Wchi", "value": "0."},
     "pdg": 9900003, "particle_name": "chi", "antiparticle_name": "chi~",
     "full_name": "Monotop invisible fermion"},
    {"spin_type": "S", "class_index": 103, "class_name": "vphi", "self_conjugate": false,
     "indices": ["Colour"], "quantum_numbers": {"Q": "2/3"},
     "mass": {"sym": "Mvphi", "value": "500."}, "width": {"sym": "Wvphi", "value": "50."},
     "pdg": 9900004, "particle_name": "vphi", "antiparticle_name": "vphi~",
     "full_name": "Colour-triplet scalar resonance (charge 2/3)"},
    {"spin_type": "S", "class_index": 104, "class_name": "vphit", "self_conjugate": false,
     "indices": ["Colour"], "quantum_numbers": {"Q": "-1/3"},
     "mass": {"sym": "Mvphit", "value": "3000."}, "width": {"sym": "Wvphit", "value": "300."},
     "pdg": 9900005, "particle_name": "vphit", "antiparticle_name": "vphit~",
     "full_name": "Colour-triplet scalar (four-fermion limit, charge -1/3)"},
    {"spin_type": "V", "class_index": 105, "class_name": "X", "self_conjugate": false,
     "indices": ["Colour"], "quantum_numbers": {"Q": "2/3"},
     "mass": {"sym": "MX", "value": "500."}, "width": {"sym": "WX", "value": "50."},
     "pdg": 9900006, "particle_name": "X", "antiparticle_name": "X~",
     "full_name": "Colour-triplet vector resonance (charge 2/3)"}
  ],
  "lagrangian_terms": [
    {"name": "Lphikin", "delayed": true,
     "expression": "1/2 del[phi, mu] del[phi, mu] - 1/2 Mphi^2 phi^2"},
    {"name": "LVkin", "delayed": true,
     "expression": "-1/4 FS[V, mu, nu] FS[V, mu, nu] + 1/2 MV^2 V[mu] V[mu]"},
    {"name": "Lchikin", "delayed": true,
     "expression": "I chibar.Ga[mu].DC[chi, mu] - Mchi chibar.chi"},
    {"name": "Lvphikin", "delayed": true,
     "expression": "DC[vphibar, mu] DC[vphi, mu] - Mvphi^2 vphibar vphi"},
    {"name": "Lvphitkin", "delayed": true,
     "expression": "DC[vphitbar, mu] DC[vphit, mu] - Mvphit^2 vphitbar vphit"},
    {"name": "LXkin", "delayed": true,
     "expression": "-1/2 FS[Xbar, mu, nu] FS[X, mu, nu] + MX^2 Xbar[mu] X[mu]"},
    {"name": "Lphiu", "delayed": true,
     "expression": "Block[{ff1,ff2,cc}, ExpandIndices[phi a0FC[ff1,ff2] uqbar[ff1,cc].uq[ff2,cc] + phi b0FC[ff1,ff2] uqbar[ff1,cc].Ga[5].uq[ff2,cc]]]"},
    {"name": "LVu", "delayed": true,
     "expression": "Block[{mu,ff1,ff2,cc}, ExpandIndices[V[mu] a1FC[ff1,ff2] uqbar[ff1,cc].Ga[mu].uq[ff2,cc] + V[mu] b1FC[ff1,ff2] uqbar[ff1,cc].Ga[mu].Ga[5].uq[ff2,cc]]]"},
    {"name": "LvphiDiquark", "delayed": true,
     "expression": "Block[{cc1,cc2,cc3,ff2,ff3,term}, term = Eps[cc1,cc2,cc3] vphi[cc1] aqSR[ff2,ff3] bar[CC[dq[ff2,cc2]]].dq[ff3,cc3] + Eps[cc1,cc2,cc3] vphi[cc1] bqSR[ff2,ff3] bar[CC[dq[ff2,cc2]]].Ga[5].dq[ff3,cc3]; ExpandIndices[term + HC[term]]]"},
    {"name": "LvphiChi", "delayed": true,
     "expression": "Block[{ff,cc,term}, term = vphi[cc] ahalfSR[ff] uqbar[ff,cc].chi + vphi[cc] bhalfSR[ff] uqbar[ff,cc].Ga[5].chi; ExpandIndices[term + HC[term]]]"},
    {"name": "LvphitDiquark", "delayed": true,
     "expression": "Block[{cc1,cc2,cc3,ff2,ff3,term}, term = Eps[cc1,cc2,cc3] vphit[cc1] atildeqSR[ff2,ff3] bar[CC[dq[ff2,cc2]]].uq[ff3,cc3] + Eps[cc1,cc2,cc3] vphit[cc1] btildeqSR[ff2,ff3] bar[CC[dq[ff2,cc2]]].Ga[5].uq[ff3,cc3]; ExpandIndices[term + HC[term]]]"},
    {"name": "LvphitChi", "delayed": true,
     "expression": "Block[{ff,cc,term}, term = vphit[cc] atildehalfSR[ff] dqbar[ff,cc].chi + vphit[cc] btildehalfSR[ff] dqbar[ff,cc].Ga[5].chi; ExpandIndices[term + HC[term]]]"},
    {"name": "LXDiquark", "delayed": true,
     "expression": "Block[{mu,cc1,cc2,cc3,ff2,ff3,term}, term = Eps[cc1,cc2,cc3] X[mu,cc1] aqVR[ff2,ff3] bar[CC[dq[ff2,cc2]]].Ga[mu].dq[ff3,cc3] + Eps[cc1,cc2,cc3] X[mu,cc1] bqVR[ff2,ff3] bar[CC[dq[ff2,cc2]]].Ga[mu].Ga[5].dq[ff3,cc3]; ExpandIndices[term + HC[term]]]"},
    {"name": "LXChi", "delayed": true,
     "expression": "Block[{mu,ff,cc,term}, term = X[mu,cc] ahalfVR[ff] uqbar[ff,cc].Ga[mu].chi + X[mu,cc] bhalfVR[ff] uqbar[ff,cc].Ga[mu].Ga[5].chi; ExpandIndices[term + HC[term]]]"},
    {"name": "LTotal", "delayed": true,
     "expression": "Lphikin + LVkin + Lchikin + Lvphikin + Lvphitkin + LXkin + Lphiu + LVu + LvphiDiquark + LvphiChi + LvphitDiquark + LvphitChi + LXDiquark + LXChi"}
  ]
}
```