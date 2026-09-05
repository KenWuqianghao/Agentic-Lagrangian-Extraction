I'll start by reading the paper and the schema.
I read the paper, the schema, the renderer, and `SM.fr`. No reference or cached `.fr` model file for this paper exists in the sandbox, and none was read.

## Physics decisions (before the audit table)

**New U(1)_Y sign convention (rule 5).** Table 5 and Eq. (24) use opposite hypercharge conventions: Eq. (24) writes `f1 (psi1L^a H_a) psi1R` with a shared SU(2) index, which under `SM.fr` (`Phi` has Y = +1/2) needs `Y(psi1R) = Y(psi1L) - 1/2`, while Table 4/5 give `QY(psi1R) = QY(psi1L) + 1`. The paper therefore effectively uses `Y(H) = -1/2`. I re-derived every new hypercharge as **`Y_SM = -QY_paper / 2`**, which makes all five Yukawa terms of Eq. (24) invariant with `SM.fr` fields and the shared-index contraction `Phi[ii]`. All anomaly conditions are invariant under this overall sign flip (I checked `Y^3`, `Y`, `X^3`, `XYY`, `XXY`, `SU(2)^2 Y`, `SU(2)^2 X` all cancel for Table 5).

**Spectrum.** `⟨Phi⟩ = V` pairs the chiral states into 4 heavy Dirac fields (2 SU(2) doublets + 2 singlets) = **6 charge eigenstates**, plus the X boson and the radial mode of `Phi`. U(1)_X is not declared as a gauge group (SM add-on), so its current coupling is written by hand and the Stückelberg pseudoscalar `thetaX` of Eq. (1) is eaten (unitary gauge for X).

## Mandatory self-audit

| term | fields in monomial | d | coupling | coupling dim (=4-d) | 1/Λ^(d-4) | Q sum | Y sum | SU(2) contraction | SU(3) | QX sum | L/B | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LXkin | FS[X]FS[X] ; X X | 4 ; 2 | 1 ; MX^2 | 0 ; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | self-conjugate |
| LhXkin | del[hX]del[hX] ; hX hX | 4 ; 2 | 1 ; MhX^2 | 0 ; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | self-conjugate |
| LXhX | hX X X ; hX hX X X | 3 ; 4 | gX^2 vX ; gX^2 | 1 ; 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (hX real) | n/a | n/a | self-conjugate |
| LXFkin | psibar Ga DC[psi] (8 chiral classes) | 4 | I | 0 ✓ | n/a | 0 | -Y+Y=0 | shared SU2D on bar/field | singlet | -QX+QX=0 | n/a | n/a | self-conjugate sum |
| LXFmass | XD1ubar.XD1u, XD1dbar.XD1d, XS1bar.XS1, XD2ubar.XD2u, XD2dbar.XD2d, XS2bar.XS2 | 3 | MXD1u… | 1 ✓ | n/a | 0 | 0 (L,R share Y) | singlet (mass eigenstates) | singlet | see note ★ | n/a | n/a | self-conjugate |
| LXFX | gX X psibar Ga psi (8 currents) | 4 | gX | 0 ✓ | n/a | 0 | 0 | shared SU2D | singlet | -QX+0+QX=0 | n/a | n/a | self-conjugate |
| LXYukawa | hX Psi1Lbar.Chi1R (+3 more) | 4 | YF1… | 0 ✓ | n/a | 0 | +1/4-1/4=0 (etc.) | shared SU2D (doublet pairs) | singlet | see note ★ | n/a | n/a | HC[yuk] |
| LXHYuk | Psi1Lbar[ii].Psi1R Phi[ii] | 4 | yf1 | 0 ✓ | n/a | 0 | +1/4-3/4+1/2=0 | shared ii with Phi (Y=+1/2) | singlet | +1/6-1/6+0=0 | n/a | n/a | HC[yuk] |
| LDF1 | Phibar DC[Phi] X FS[B] | 6 | c1/vev^2 | -2 ✓ | 1/vev^2 ✝ | 0 | -1/2+1/2=0 | shared ii (Phibar,Phi) | singlet | 0 (X, B neutral) | n/a | n/a | I(A-A†): hermitian |
| LDF2 | Phibar Ta[aa] DC[Phi] X FS[Wi,aa] | 6 | c2/vev^2 | -2 ✓ | 1/vev^2 ✝ | 0 | -1/2+1/2=0 | Ta[aa,ii,jj] joins Phibar[ii],Phi[jj]; aa with FS[Wi] | singlet | 0 | n/a | n/a | I(A-A†): hermitian |

Per-class kinetic+mass confirmation: **X** → LXkin; **hX** → LhXkin; **XD1u, XD1d, XS1, XD2u, XD2d, XS2** → kinetic (through their chiral parents) in LXFkin + Dirac mass in LXFmass. All ten terms enter `LNP`, and `LTotal := LSM + LNP`.

★ QX note: the QX-invariant parent is Eq. (24), `-YF1 Phibar (Psi1Lbar.Chi1R)` with QX(Phibar) = -1: sum = +1/6 - 1 + 5/6 = 0 ✓ (same for the other three: `-YF1t Phi (Psi1Rbar.Chi1L)`: +1/6 + 1 - 7/6 = 0 ✓; `-YF2 Phibar (Psi2Rbar.Chi2L)`: +1/6 - 1 + 5/6 = 0 ✓; `-YF2t Phi (Psi2Lbar.Chi2R)`: +1/6 + 1 - 7/6 = 0 ✓). In unitary gauge `Phi -> (vX + hX)/Sqrt[2]` splits this into LXFmass (the VEV part) and LXYukawa (the hX part), so QX is spontaneously broken there, not violated. No double counting: LXYukawa keeps only the hX piece.

✝ `1/vev^2` is not an EFT cutoff: it is the paper's own `1/|H|^2` in Eq. (5) evaluated at `|H|^2 -> vev^2/2`, up to the `O(∂h/v)` terms the paper drops in Eq. (25). `c1`, `c2` stay dimensionless, as the paper states.

`SelfConjugate -> True` classes: **X** and **hX** — neither carries `QuantumNumbers` ✓.

Reference/cached model files read: **none** (only `0901.0639.txt`, `frmodel.py`, `render.py`, `SM.fr`).

```json
{
  "model_name": "ChernSimonsPortal_gen",
  "info": {
    "authors": ["I. Antoniadis", "A. Boyarsky", "S. Espahbodi", "O. Ruchayskiy", "J. D. Wells"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["CERN PH-TH", "CPHT Ecole Polytechnique", "ETH Zurich", "MCTP University of Michigan", "EPFL Lausanne"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "c1",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "CSPORTAL",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "c_1",
      "description": "Dimensionless D'Hoker-Farhi coefficient of the (Hdag DH/|H|^2) DthetaX FY term, Eq.(5); generates the XZZ and XZgamma vertices, Eq.(27). Benchmark c1 = 0.1 of Fig.5"
    },
    {
      "name": "c2",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "CSPORTAL",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "tex": "c_2",
      "description": "Dimensionless D'Hoker-Farhi coefficient of the (H FW DHdag/|H|^2) DthetaX term, Eq.(5); generates the XW+W- vertex, Eq.(28). Benchmark c2 = 0.1 of Fig.5"
    },
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.05",
      "block_name": "CSPORTAL",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "tex": "g_X",
      "description": "U(1)_X gauge coupling of the hidden sector, Eq.(1); with vX it gives gX vX = MX"
    },
    {
      "name": "vX",
      "parameter_type": "External",
      "value": "20000.",
      "block_name": "CSPORTAL",
      "order_block": 4,
      "tex": "V",
      "description": "Vacuum expectation value <Phi> = V of the heavy Higgs Phi [GeV], Eq.(12), with v << V; Phi has QX = 1 and Y = 0"
    },
    {
      "name": "YF1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "tex": "F_1",
      "description": "Heavy Yukawa coupling F1 of Eq.(24): Phi psi1L chi1R (SU(2) doublet pair)"
    },
    {
      "name": "YF1t",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 6,
      "interaction_order": ["NP", 1],
      "tex": "F_1t",
      "description": "Heavy Yukawa coupling F1-tilde of Eq.(24): Phi psi1R chi1L (SU(2) singlet pair)"
    },
    {
      "name": "YF2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 7,
      "interaction_order": ["NP", 1],
      "tex": "F_2",
      "description": "Heavy Yukawa coupling F2 of Eq.(24): Phi psi2R chi2L (SU(2) doublet pair)"
    },
    {
      "name": "YF2t",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 8,
      "interaction_order": ["NP", 1],
      "tex": "F_2t",
      "description": "Heavy Yukawa coupling F2-tilde of Eq.(24): Phi psi2L chi2R (SU(2) singlet pair)"
    },
    {
      "name": "yf1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 9,
      "interaction_order": ["NP", 1],
      "tex": "f_1",
      "description": "SM-Higgs Yukawa f1 of Eq.(24); gives the mass splitting m1 = f1 v of the two eigenstates with the same electric charge, Eq.(11)"
    },
    {
      "name": "kappa",
      "parameter_type": "External",
      "value": "6.",
      "block_name": "CSPORTAL",
      "order_block": 10,
      "tex": "\\kappa",
      "description": "Chern-Simons (anomaly) coefficient kappa of Eqs.(8),(19),(21); kappa = 6 for the charge assignment of Table 3. It fixes c1 and c2 in the high-energy completion and is not used directly in the low-energy Lagrangian"
    },
    {
      "name": "MXD1u",
      "parameter_type": "Internal",
      "value": "YF1*vX/Sqrt[2]",
      "description": "Mass of the upper component of the heavy Dirac doublet 1 [GeV] = F1 <Phi>/Sqrt[2], Eq.(24)"
    },
    {
      "name": "MXD1d",
      "parameter_type": "Internal",
      "value": "YF1*vX/Sqrt[2]",
      "description": "Mass of the lower component of the heavy Dirac doublet 1 [GeV] = F1 <Phi>/Sqrt[2]; split by O(f1 v) through LXHYuk, Eq.(11)"
    },
    {
      "name": "MXS1",
      "parameter_type": "Internal",
      "value": "YF1t*vX/Sqrt[2]",
      "description": "Mass of the heavy Dirac singlet 1 [GeV] = F1-tilde <Phi>/Sqrt[2], Eq.(24)"
    },
    {
      "name": "MXD2u",
      "parameter_type": "Internal",
      "value": "YF2*vX/Sqrt[2]",
      "description": "Mass of the upper component of the heavy Dirac doublet 2 [GeV] = F2 <Phi>/Sqrt[2], Eq.(24)"
    },
    {
      "name": "MXD2d",
      "parameter_type": "Internal",
      "value": "YF2*vX/Sqrt[2]",
      "description": "Mass of the lower component of the heavy Dirac doublet 2 [GeV] = F2 <Phi>/Sqrt[2], Eq.(24)"
    },
    {
      "name": "MXS2",
      "parameter_type": "Internal",
      "value": "YF2t*vX/Sqrt[2]",
      "description": "Mass of the heavy Dirac singlet 2 [GeV] = F2-tilde <Phi>/Sqrt[2], Eq.(24)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 50,
      "class_name": "X",
      "self_conjugate": true,
      "mass": {"sym": "MX", "value": "1000."},
      "width": {"sym": "WX", "value": "13.8"},
      "pdg": 9000001,
      "particle_name": "X",
      "full_name": "X boson (anomalous U(1)_X gauge boson)",
      "propagator_label": "X",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 50,
      "class_name": "hX",
      "self_conjugate": true,
      "mass": {"sym": "MhX", "value": "5000."},
      "width": {"sym": "WhX", "value": "10."},
      "pdg": 9000002,
      "particle_name": "hX",
      "full_name": "Radial mode of the heavy Higgs Phi",
      "propagator_label": "hX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 50,
      "class_name": "XD1u",
      "self_conjugate": false,
      "mass": {"sym": "MXD1u", "value": "Internal"},
      "width": {"sym": "WXD1u", "value": "1."},
      "quantum_numbers": {"Q": "1/4"},
      "pdg": 9000011,
      "particle_name": "xd1u",
      "antiparticle_name": "xd1u~",
      "full_name": "Heavy Dirac doublet 1, upper component (psi1L-chi1R)",
      "propagator_label": "XD1u",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 51,
      "class_name": "XD1d",
      "self_conjugate": false,
      "mass": {"sym": "MXD1d", "value": "Internal"},
      "width": {"sym": "WXD1d", "value": "1."},
      "quantum_numbers": {"Q": "-3/4"},
      "pdg": 9000012,
      "particle_name": "xd1d",
      "antiparticle_name": "xd1d~",
      "full_name": "Heavy Dirac doublet 1, lower component (psi1L-chi1R)",
      "propagator_label": "XD1d",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 52,
      "class_name": "XS1",
      "self_conjugate": false,
      "mass": {"sym": "MXS1", "value": "Internal"},
      "width": {"sym": "WXS1", "value": "1."},
      "quantum_numbers": {"Q": "-3/4"},
      "pdg": 9000013,
      "particle_name": "xs1",
      "antiparticle_name": "xs1~",
      "full_name": "Heavy Dirac singlet 1 (chi1L-psi1R)",
      "propagator_label": "XS1",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 53,
      "class_name": "XD2u",
      "self_conjugate": false,
      "mass": {"sym": "MXD2u", "value": "Internal"},
      "width": {"sym": "WXD2u", "value": "1."},
      "quantum_numbers": {"Q": "13/12"},
      "pdg": 9000014,
      "particle_name": "xd2u",
      "antiparticle_name": "xd2u~",
      "full_name": "Heavy Dirac doublet 2, upper component (chi2L-psi2R)",
      "propagator_label": "XD2u",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 54,
      "class_name": "XD2d",
      "self_conjugate": false,
      "mass": {"sym": "MXD2d", "value": "Internal"},
      "width": {"sym": "WXD2d", "value": "1."},
      "quantum_numbers": {"Q": "1/12"},
      "pdg": 9000015,
      "particle_name": "xd2d",
      "antiparticle_name": "xd2d~",
      "full_name": "Heavy Dirac doublet 2, lower component (chi2L-psi2R)",
      "propagator_label": "XD2d",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 55,
      "class_name": "XS2",
      "self_conjugate": false,
      "mass": {"sym": "MXS2", "value": "Internal"},
      "width": {"sym": "WXS2", "value": "1."},
      "quantum_numbers": {"Q": "1/12"},
      "pdg": 9000016,
      "particle_name": "xs2",
      "antiparticle_name": "xs2~",
      "full_name": "Heavy Dirac singlet 2 (psi2L-chi2R)",
      "propagator_label": "XS2",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 60,
      "class_name": "Psi1L",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "-1/4", "QX": "-1/6"},
      "unphysical": true,
      "definitions": [
        "Psi1L[sp1_,1] :> Module[{sp2}, ProjM[sp1,sp2] XD1u[sp2]]",
        "Psi1L[sp1_,2] :> Module[{sp2}, ProjM[sp1,sp2] XD1d[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 61,
      "class_name": "Chi1R",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "-1/4", "QX": "5/6"},
      "unphysical": true,
      "definitions": [
        "Chi1R[sp1_,1] :> Module[{sp2}, ProjP[sp1,sp2] XD1u[sp2]]",
        "Chi1R[sp1_,2] :> Module[{sp2}, ProjP[sp1,sp2] XD1d[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 62,
      "class_name": "Psi1R",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "-3/4", "QX": "-1/6"},
      "unphysical": true,
      "definitions": ["Psi1R[sp1_] :> Module[{sp2}, ProjP[sp1,sp2] XS1[sp2]]"]
    },
    {
      "spin_type": "F",
      "class_index": 63,
      "class_name": "Chi1L",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "-3/4", "QX": "-7/6"},
      "unphysical": true,
      "definitions": ["Chi1L[sp1_] :> Module[{sp2}, ProjM[sp1,sp2] XS1[sp2]]"]
    },
    {
      "spin_type": "F",
      "class_index": 64,
      "class_name": "Psi2R",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "7/12", "QX": "-1/6"},
      "unphysical": true,
      "definitions": [
        "Psi2R[sp1_,1] :> Module[{sp2}, ProjP[sp1,sp2] XD2u[sp2]]",
        "Psi2R[sp1_,2] :> Module[{sp2}, ProjP[sp1,sp2] XD2d[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 65,
      "class_name": "Chi2L",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "7/12", "QX": "5/6"},
      "unphysical": true,
      "definitions": [
        "Chi2L[sp1_,1] :> Module[{sp2}, ProjM[sp1,sp2] XD2u[sp2]]",
        "Chi2L[sp1_,2] :> Module[{sp2}, ProjM[sp1,sp2] XD2d[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 66,
      "class_name": "Psi2L",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "1/12", "QX": "-1/6"},
      "unphysical": true,
      "definitions": ["Psi2L[sp1_] :> Module[{sp2}, ProjM[sp1,sp2] XS2[sp2]]"]
    },
    {
      "spin_type": "F",
      "class_index": 67,
      "class_name": "Chi2R",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "1/12", "QX": "-7/6"},
      "unphysical": true,
      "definitions": ["Chi2R[sp1_] :> Module[{sp2}, ProjP[sp1,sp2] XS2[sp2]]"]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LXkin",
      "expression": "Block[{mu,nu}, -1/4 FS[X,mu,nu] FS[X,mu,nu] + 1/2 MX^2 X[mu] X[mu]]",
      "delayed": true
    },
    {
      "name": "LhXkin",
      "expression": "Block[{mu}, 1/2 del[hX,mu] del[hX,mu] - 1/2 MhX^2 hX^2]",
      "delayed": true
    },
    {
      "name": "LXhX",
      "expression": "Block[{mu}, gX^2 vX hX X[mu] X[mu] + 1/2 gX^2 hX^2 X[mu] X[mu]]",
      "delayed": true
    },
    {
      "name": "LXFkin",
      "expression": "Block[{mu}, ExpandIndices[I*(Psi1Lbar.Ga[mu].DC[Psi1L,mu] + Chi1Rbar.Ga[mu].DC[Chi1R,mu] + Psi1Rbar.Ga[mu].DC[Psi1R,mu] + Chi1Lbar.Ga[mu].DC[Chi1L,mu] + Psi2Rbar.Ga[mu].DC[Psi2R,mu] + Chi2Lbar.Ga[mu].DC[Chi2L,mu] + Psi2Lbar.Ga[mu].DC[Psi2L,mu] + Chi2Rbar.Ga[mu].DC[Chi2R,mu]), FlavorExpand->{SU2W,SU2D}]]",
      "delayed": true
    },
    {
      "name": "LXFmass",
      "expression": "- MXD1u XD1ubar.XD1u - MXD1d XD1dbar.XD1d - MXS1 XS1bar.XS1 - MXD2u XD2ubar.XD2u - MXD2d XD2dbar.XD2d - MXS2 XS2bar.XS2",
      "delayed": true
    },
    {
      "name": "LXFX",
      "expression": "Block[{mu}, ExpandIndices[gX*X[mu]*(-1/6*(Psi1Lbar.Ga[mu].Psi1L + Psi1Rbar.Ga[mu].Psi1R + Psi2Lbar.Ga[mu].Psi2L + Psi2Rbar.Ga[mu].Psi2R) + 5/6*(Chi1Rbar.Ga[mu].Chi1R + Chi2Lbar.Ga[mu].Chi2L) - 7/6*(Chi1Lbar.Ga[mu].Chi1L + Chi2Rbar.Ga[mu].Chi2R)), FlavorExpand->SU2D]]",
      "delayed": true
    },
    {
      "name": "LXYukawa",
      "expression": "Block[{sp,ii,yuk}, yuk = ExpandIndices[-hX/Sqrt[2]*(YF1 Psi1Lbar[sp,ii].Chi1R[sp,ii] + YF1t Psi1Rbar[sp].Chi1L[sp] + YF2 Psi2Rbar[sp,ii].Chi2L[sp,ii] + YF2t Psi2Lbar[sp].Chi2R[sp]), FlavorExpand->SU2D]; yuk + HC[yuk]]",
      "delayed": true
    },
    {
      "name": "LXHYuk",
      "expression": "Block[{sp,ii,yuk}, yuk = ExpandIndices[-yf1*(Psi1Lbar[sp,ii].Psi1R[sp])*Phi[ii], FlavorExpand->SU2D]; yuk + HC[yuk]]",
      "delayed": true
    },
    {
      "name": "LDF1",
      "expression": "Block[{mu,nu,la,rh,ii}, ExpandIndices[c1*(I/vev^2)*Eps[mu,nu,la,rh]*(Phibar[ii]*DC[Phi[ii],mu] - DC[Phibar[ii],mu]*Phi[ii])*X[nu]*FS[B,la,rh], FlavorExpand->{SU2D,SU2W}]]",
      "delayed": true
    },
    {
      "name": "LDF2",
      "expression": "Block[{mu,nu,la,rh,ii,jj,aa}, ExpandIndices[c2*(I/vev^2)*Eps[mu,nu,la,rh]*X[nu]*FS[Wi,la,rh,aa]*(Phibar[ii]*Ta[aa,ii,jj]*DC[Phi[jj],mu] - DC[Phibar[ii],mu]*Ta[aa,ii,jj]*Phi[jj]), FlavorExpand->{SU2D,SU2W}]]",
      "delayed": true
    },
    {
      "name": "LNP",
      "expression": "LXkin + LhXkin + LXhX + LXFkin + LXFmass + LXFX + LXYukawa + LXHYuk + LDF1 + LDF2",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LNP",
      "delayed": true
    }
  ]
}
```
I read the paper, the schema, the renderer, and `SM.fr`. No reference or cached `.fr` model file for this paper exists in the sandbox, and none was read.

## Physics decisions (before the audit table)

**New U(1)_Y sign convention (rule 5).** Table 5 and Eq. (24) use opposite hypercharge conventions: Eq. (24) writes `f1 (psi1L^a H_a) psi1R` with a shared SU(2) index, which under `SM.fr` (`Phi` has Y = +1/2) needs `Y(psi1R) = Y(psi1L) - 1/2`, while Table 4/5 give `QY(psi1R) = QY(psi1L) + 1`. The paper therefore effectively uses `Y(H) = -1/2`. I re-derived every new hypercharge as **`Y_SM = -QY_paper / 2`**, which makes all five Yukawa terms of Eq. (24) invariant with `SM.fr` fields and the shared-index contraction `Phi[ii]`. All anomaly conditions are invariant under this overall sign flip (I checked `Y^3`, `Y`, `X^3`, `XYY`, `XXY`, `SU(2)^2 Y`, `SU(2)^2 X` all cancel for Table 5).

**Spectrum.** `⟨Phi⟩ = V` pairs the chiral states into 4 heavy Dirac fields (2 SU(2) doublets + 2 singlets) = **6 charge eigenstates**, plus the X boson and the radial mode of `Phi`. U(1)_X is not declared as a gauge group (SM add-on), so its current coupling is written by hand and the Stückelberg pseudoscalar `thetaX` of Eq. (1) is eaten (unitary gauge for X).

## Mandatory self-audit

| term | fields in monomial | d | coupling | coupling dim (=4-d) | 1/Λ^(d-4) | Q sum | Y sum | SU(2) contraction | SU(3) | QX sum | L/B | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LXkin | FS[X]FS[X] ; X X | 4 ; 2 | 1 ; MX^2 | 0 ; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | self-conjugate |
| LhXkin | del[hX]del[hX] ; hX hX | 4 ; 2 | 1 ; MhX^2 | 0 ; 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | self-conjugate |
| LXhX | hX X X ; hX hX X X | 3 ; 4 | gX^2 vX ; gX^2 | 1 ; 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (hX real) | n/a | n/a | self-conjugate |
| LXFkin | psibar Ga DC[psi] (8 chiral classes) | 4 | I | 0 ✓ | n/a | 0 | -Y+Y=0 | shared SU2D on bar/field | singlet | -QX+QX=0 | n/a | n/a | self-conjugate sum |
| LXFmass | XD1ubar.XD1u, XD1dbar.XD1d, XS1bar.XS1, XD2ubar.XD2u, XD2dbar.XD2d, XS2bar.XS2 | 3 | MXD1u… | 1 ✓ | n/a | 0 | 0 (L,R share Y) | singlet (mass eigenstates) | singlet | see note ★ | n/a | n/a | self-conjugate |
| LXFX | gX X psibar Ga psi (8 currents) | 4 | gX | 0 ✓ | n/a | 0 | 0 | shared SU2D | singlet | -QX+0+QX=0 | n/a | n/a | self-conjugate |
| LXYukawa | hX Psi1Lbar.Chi1R (+3 more) | 4 | YF1… | 0 ✓ | n/a | 0 | +1/4-1/4=0 (etc.) | shared SU2D (doublet pairs) | singlet | see note ★ | n/a | n/a | HC[yuk] |
| LXHYuk | Psi1Lbar[ii].Psi1R Phi[ii] | 4 | yf1 | 0 ✓ | n/a | 0 | +1/4-3/4+1/2=0 | shared ii with Phi (Y=+1/2) | singlet | +1/6-1/6+0=0 | n/a | n/a | HC[yuk] |
| LDF1 | Phibar DC[Phi] X FS[B] | 6 | c1/vev^2 | -2 ✓ | 1/vev^2 ✝ | 0 | -1/2+1/2=0 | shared ii (Phibar,Phi) | singlet | 0 (X, B neutral) | n/a | n/a | I(A-A†): hermitian |
| LDF2 | Phibar Ta[aa] DC[Phi] X FS[Wi,aa] | 6 | c2/vev^2 | -2 ✓ | 1/vev^2 ✝ | 0 | -1/2+1/2=0 | Ta[aa,ii,jj] joins Phibar[ii],Phi[jj]; aa with FS[Wi] | singlet | 0 | n/a | n/a | I(A-A†): hermitian |

Per-class kinetic+mass confirmation: **X** → LXkin; **hX** → LhXkin; **XD1u, XD1d, XS1, XD2u, XD2d, XS2** → kinetic (through their chiral parents) in LXFkin + Dirac mass in LXFmass. All ten terms enter `LNP`, and `LTotal := LSM + LNP`.

★ QX note: the QX-invariant parent is Eq. (24), `-YF1 Phibar (Psi1Lbar.Chi1R)` with QX(Phibar) = -1: sum = +1/6 - 1 + 5/6 = 0 ✓ (same for the other three: `-YF1t Phi (Psi1Rbar.Chi1L)`: +1/6 + 1 - 7/6 = 0 ✓; `-YF2 Phibar (Psi2Rbar.Chi2L)`: +1/6 - 1 + 5/6 = 0 ✓; `-YF2t Phi (Psi2Lbar.Chi2R)`: +1/6 + 1 - 7/6 = 0 ✓). In unitary gauge `Phi -> (vX + hX)/Sqrt[2]` splits this into LXFmass (the VEV part) and LXYukawa (the hX part), so QX is spontaneously broken there, not violated. No double counting: LXYukawa keeps only the hX piece.

✝ `1/vev^2` is not an EFT cutoff: it is the paper's own `1/|H|^2` in Eq. (5) evaluated at `|H|^2 -> vev^2/2`, up to the `O(∂h/v)` terms the paper drops in Eq. (25). `c1`, `c2` stay dimensionless, as the paper states.

`SelfConjugate -> True` classes: **X** and **hX** — neither carries `QuantumNumbers` ✓.

Reference/cached model files read: **none** (only `0901.0639.txt`, `frmodel.py`, `render.py`, `SM.fr`).

```json
{
  "model_name": "ChernSimonsPortal_gen",
  "info": {
    "authors": ["I. Antoniadis", "A. Boyarsky", "S. Espahbodi", "O. Ruchayskiy", "J. D. Wells"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["CERN PH-TH", "CPHT Ecole Polytechnique", "ETH Zurich", "MCTP University of Michigan", "EPFL Lausanne"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "c1",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "CSPORTAL",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "c_1",
      "description": "Dimensionless D'Hoker-Farhi coefficient of the (Hdag DH/|H|^2) DthetaX FY term, Eq.(5); generates the XZZ and XZgamma vertices, Eq.(27). Benchmark c1 = 0.1 of Fig.5"
    },
    {
      "name": "c2",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "CSPORTAL",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "tex": "c_2",
      "description": "Dimensionless D'Hoker-Farhi coefficient of the (H FW DHdag/|H|^2) DthetaX term, Eq.(5); generates the XW+W- vertex, Eq.(28). Benchmark c2 = 0.1 of Fig.5"
    },
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.05",
      "block_name": "CSPORTAL",
      "order_block": 3,
      "interaction_order": ["NP", 1],
      "tex": "g_X",
      "description": "U(1)_X gauge coupling of the hidden sector, Eq.(1); with vX it gives gX vX = MX"
    },
    {
      "name": "vX",
      "parameter_type": "External",
      "value": "20000.",
      "block_name": "CSPORTAL",
      "order_block": 4,
      "tex": "V",
      "description": "Vacuum expectation value <Phi> = V of the heavy Higgs Phi [GeV], Eq.(12), with v << V; Phi has QX = 1 and Y = 0"
    },
    {
      "name": "YF1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "tex": "F_1",
      "description": "Heavy Yukawa coupling F1 of Eq.(24): Phi psi1L chi1R (SU(2) doublet pair)"
    },
    {
      "name": "YF1t",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 6,
      "interaction_order": ["NP", 1],
      "tex": "F_1t",
      "description": "Heavy Yukawa coupling F1-tilde of Eq.(24): Phi psi1R chi1L (SU(2) singlet pair)"
    },
    {
      "name": "YF2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 7,
      "interaction_order": ["NP", 1],
      "tex": "F_2",
      "description": "Heavy Yukawa coupling F2 of Eq.(24): Phi psi2R chi2L (SU(2) doublet pair)"
    },
    {
      "name": "YF2t",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 8,
      "interaction_order": ["NP", 1],
      "tex": "F_2t",
      "description": "Heavy Yukawa coupling F2-tilde of Eq.(24): Phi psi2L chi2R (SU(2) singlet pair)"
    },
    {
      "name": "yf1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "CSPORTAL",
      "order_block": 9,
      "interaction_order": ["NP", 1],
      "tex": "f_1",
      "description": "SM-Higgs Yukawa f1 of Eq.(24); gives the mass splitting m1 = f1 v of the two eigenstates with the same electric charge, Eq.(11)"
    },
    {
      "name": "kappa",
      "parameter_type": "External",
      "value": "6.",
      "block_name": "CSPORTAL",
      "order_block": 10,
      "tex": "\\kappa",
      "description": "Chern-Simons (anomaly) coefficient kappa of Eqs.(8),(19),(21); kappa = 6 for the charge assignment of Table 3. It fixes c1 and c2 in the high-energy completion and is not used directly in the low-energy Lagrangian"
    },
    {
      "name": "MXD1u",
      "parameter_type": "Internal",
      "value": "YF1*vX/Sqrt[2]",
      "description": "Mass of the upper component of the heavy Dirac doublet 1 [GeV] = F1 <Phi>/Sqrt[2], Eq.(24)"
    },
    {
      "name": "MXD1d",
      "parameter_type": "Internal",
      "value": "YF1*vX/Sqrt[2]",
      "description": "Mass of the lower component of the heavy Dirac doublet 1 [GeV] = F1 <Phi>/Sqrt[2]; split by O(f1 v) through LXHYuk, Eq.(11)"
    },
    {
      "name": "MXS1",
      "parameter_type": "Internal",
      "value": "YF1t*vX/Sqrt[2]",
      "description": "Mass of the heavy Dirac singlet 1 [GeV] = F1-tilde <Phi>/Sqrt[2], Eq.(24)"
    },
    {
      "name": "MXD2u",
      "parameter_type": "Internal",
      "value": "YF2*vX/Sqrt[2]",
      "description": "Mass of the upper component of the heavy Dirac doublet 2 [GeV] = F2 <Phi>/Sqrt[2], Eq.(24)"
    },
    {
      "name": "MXD2d",
      "parameter_type": "Internal",
      "value": "YF2*vX/Sqrt[2]",
      "description": "Mass of the lower component of the heavy Dirac doublet 2 [GeV] = F2 <Phi>/Sqrt[2], Eq.(24)"
    },
    {
      "name": "MXS2",
      "parameter_type": "Internal",
      "value": "YF2t*vX/Sqrt[2]",
      "description": "Mass of the heavy Dirac singlet 2 [GeV] = F2-tilde <Phi>/Sqrt[2], Eq.(24)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 50,
      "class_name": "X",
      "self_conjugate": true,
      "mass": {"sym": "MX", "value": "1000."},
      "width": {"sym": "WX", "value": "13.8"},
      "pdg": 9000001,
      "particle_name": "X",
      "full_name": "X boson (anomalous U(1)_X gauge boson)",
      "propagator_label": "X",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 50,
      "class_name": "hX",
      "self_conjugate": true,
      "mass": {"sym": "MhX", "value": "5000."},
      "width": {"sym": "WhX", "value": "10."},
      "pdg": 9000002,
      "particle_name": "hX",
      "full_name": "Radial mode of the heavy Higgs Phi",
      "propagator_label": "hX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 50,
      "class_name": "XD1u",
      "self_conjugate": false,
      "mass": {"sym": "MXD1u", "value": "Internal"},
      "width": {"sym": "WXD1u", "value": "1."},
      "quantum_numbers": {"Q": "1/4"},
      "pdg": 9000011,
      "particle_name": "xd1u",
      "antiparticle_name": "xd1u~",
      "full_name": "Heavy Dirac doublet 1, upper component (psi1L-chi1R)",
      "propagator_label": "XD1u",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 51,
      "class_name": "XD1d",
      "self_conjugate": false,
      "mass": {"sym": "MXD1d", "value": "Internal"},
      "width": {"sym": "WXD1d", "value": "1."},
      "quantum_numbers": {"Q": "-3/4"},
      "pdg": 9000012,
      "particle_name": "xd1d",
      "antiparticle_name": "xd1d~",
      "full_name": "Heavy Dirac doublet 1, lower component (psi1L-chi1R)",
      "propagator_label": "XD1d",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 52,
      "class_name": "XS1",
      "self_conjugate": false,
      "mass": {"sym": "MXS1", "value": "Internal"},
      "width": {"sym": "WXS1", "value": "1."},
      "quantum_numbers": {"Q": "-3/4"},
      "pdg": 9000013,
      "particle_name": "xs1",
      "antiparticle_name": "xs1~",
      "full_name": "Heavy Dirac singlet 1 (chi1L-psi1R)",
      "propagator_label": "XS1",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 53,
      "class_name": "XD2u",
      "self_conjugate": false,
      "mass": {"sym": "MXD2u", "value": "Internal"},
      "width": {"sym": "WXD2u", "value": "1."},
      "quantum_numbers": {"Q": "13/12"},
      "pdg": 9000014,
      "particle_name": "xd2u",
      "antiparticle_name": "xd2u~",
      "full_name": "Heavy Dirac doublet 2, upper component (chi2L-psi2R)",
      "propagator_label": "XD2u",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 54,
      "class_name": "XD2d",
      "self_conjugate": false,
      "mass": {"sym": "MXD2d", "value": "Internal"},
      "width": {"sym": "WXD2d", "value": "1."},
      "quantum_numbers": {"Q": "1/12"},
      "pdg": 9000015,
      "particle_name": "xd2d",
      "antiparticle_name": "xd2d~",
      "full_name": "Heavy Dirac doublet 2, lower component (chi2L-psi2R)",
      "propagator_label": "XD2d",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 55,
      "class_name": "XS2",
      "self_conjugate": false,
      "mass": {"sym": "MXS2", "value": "Internal"},
      "width": {"sym": "WXS2", "value": "1."},
      "quantum_numbers": {"Q": "1/12"},
      "pdg": 9000016,
      "particle_name": "xs2",
      "antiparticle_name": "xs2~",
      "full_name": "Heavy Dirac singlet 2 (psi2L-chi2R)",
      "propagator_label": "XS2",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 60,
      "class_name": "Psi1L",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "-1/4", "QX": "-1/6"},
      "unphysical": true,
      "definitions": [
        "Psi1L[sp1_,1] :> Module[{sp2}, ProjM[sp1,sp2] XD1u[sp2]]",
        "Psi1L[sp1_,2] :> Module[{sp2}, ProjM[sp1,sp2] XD1d[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 61,
      "class_name": "Chi1R",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "-1/4", "QX": "5/6"},
      "unphysical": true,
      "definitions": [
        "Chi1R[sp1_,1] :> Module[{sp2}, ProjP[sp1,sp2] XD1u[sp2]]",
        "Chi1R[sp1_,2] :> Module[{sp2}, ProjP[sp1,sp2] XD1d[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 62,
      "class_name": "Psi1R",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "-3/4", "QX": "-1/6"},
      "unphysical": true,
      "definitions": ["Psi1R[sp1_] :> Module[{sp2}, ProjP[sp1,sp2] XS1[sp2]]"]
    },
    {
      "spin_type": "F",
      "class_index": 63,
      "class_name": "Chi1L",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "-3/4", "QX": "-7/6"},
      "unphysical": true,
      "definitions": ["Chi1L[sp1_] :> Module[{sp2}, ProjM[sp1,sp2] XS1[sp2]]"]
    },
    {
      "spin_type": "F",
      "class_index": 64,
      "class_name": "Psi2R",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "7/12", "QX": "-1/6"},
      "unphysical": true,
      "definitions": [
        "Psi2R[sp1_,1] :> Module[{sp2}, ProjP[sp1,sp2] XD2u[sp2]]",
        "Psi2R[sp1_,2] :> Module[{sp2}, ProjP[sp1,sp2] XD2d[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 65,
      "class_name": "Chi2L",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "7/12", "QX": "5/6"},
      "unphysical": true,
      "definitions": [
        "Chi2L[sp1_,1] :> Module[{sp2}, ProjM[sp1,sp2] XD2u[sp2]]",
        "Chi2L[sp1_,2] :> Module[{sp2}, ProjM[sp1,sp2] XD2d[sp2]]"
      ]
    },
    {
      "spin_type": "F",
      "class_index": 66,
      "class_name": "Psi2L",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "1/12", "QX": "-1/6"},
      "unphysical": true,
      "definitions": ["Psi2L[sp1_] :> Module[{sp2}, ProjM[sp1,sp2] XS2[sp2]]"]
    },
    {
      "spin_type": "F",
      "class_index": 67,
      "class_name": "Chi2R",
      "self_conjugate": false,
      "quantum_numbers": {"Y": "1/12", "QX": "-7/6"},
      "unphysical": true,
      "definitions": ["Chi2R[sp1_] :> Module[{sp2}, ProjP[sp1,sp2] XS2[sp2]]"]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LXkin",
      "expression": "Block[{mu,nu}, -1/4 FS[X,mu,nu] FS[X,mu,nu] + 1/2 MX^2 X[mu] X[mu]]",
      "delayed": true
    },
    {
      "name": "LhXkin",
      "expression": "Block[{mu}, 1/2 del[hX,mu] del[hX,mu] - 1/2 MhX^2 hX^2]",
      "delayed": true
    },
    {
      "name": "LXhX",
      "expression": "Block[{mu}, gX^2 vX hX X[mu] X[mu] + 1/2 gX^2 hX^2 X[mu] X[mu]]",
      "delayed": true
    },
    {
      "name": "LXFkin",
      "expression": "Block[{mu}, ExpandIndices[I*(Psi1Lbar.Ga[mu].DC[Psi1L,mu] + Chi1Rbar.Ga[mu].DC[Chi1R,mu] + Psi1Rbar.Ga[mu].DC[Psi1R,mu] + Chi1Lbar.Ga[mu].DC[Chi1L,mu] + Psi2Rbar.Ga[mu].DC[Psi2R,mu] + Chi2Lbar.Ga[mu].DC[Chi2L,mu] + Psi2Lbar.Ga[mu].DC[Psi2L,mu] + Chi2Rbar.Ga[mu].DC[Chi2R,mu]), FlavorExpand->{SU2W,SU2D}]]",
      "delayed": true
    },
    {
      "name": "LXFmass",
      "expression": "- MXD1u XD1ubar.XD1u - MXD1d XD1dbar.XD1d - MXS1 XS1bar.XS1 - MXD2u XD2ubar.XD2u - MXD2d XD2dbar.XD2d - MXS2 XS2bar.XS2",
      "delayed": true
    },
    {
      "name": "LXFX",
      "expression": "Block[{mu}, ExpandIndices[gX*X[mu]*(-1/6*(Psi1Lbar.Ga[mu].Psi1L + Psi1Rbar.Ga[mu].Psi1R + Psi2Lbar.Ga[mu].Psi2L + Psi2Rbar.Ga[mu].Psi2R) + 5/6*(Chi1Rbar.Ga[mu].Chi1R + Chi2Lbar.Ga[mu].Chi2L) - 7/6*(Chi1Lbar.Ga[mu].Chi1L + Chi2Rbar.Ga[mu].Chi2R)), FlavorExpand->SU2D]]",
      "delayed": true
    },
    {
      "name": "LXYukawa",
      "expression": "Block[{sp,ii,yuk}, yuk = ExpandIndices[-hX/Sqrt[2]*(YF1 Psi1Lbar[sp,ii].Chi1R[sp,ii] + YF1t Psi1Rbar[sp].Chi1L[sp] + YF2 Psi2Rbar[sp,ii].Chi2L[sp,ii] + YF2t Psi2Lbar[sp].Chi2R[sp]), FlavorExpand->SU2D]; yuk + HC[yuk]]",
      "delayed": true
    },
    {
      "name": "LXHYuk",
      "expression": "Block[{sp,ii,yuk}, yuk = ExpandIndices[-yf1*(Psi1Lbar[sp,ii].Psi1R[sp])*Phi[ii], FlavorExpand->SU2D]; yuk + HC[yuk]]",
      "delayed": true
    },
    {
      "name": "LDF1",
      "expression": "Block[{mu,nu,la,rh,ii}, ExpandIndices[c1*(I/vev^2)*Eps[mu,nu,la,rh]*(Phibar[ii]*DC[Phi[ii],mu] - DC[Phibar[ii],mu]*Phi[ii])*X[nu]*FS[B,la,rh], FlavorExpand->{SU2D,SU2W}]]",
      "delayed": true
    },
    {
      "name": "LDF2",
      "expression": "Block[{mu,nu,la,rh,ii,jj,aa}, ExpandIndices[c2*(I/vev^2)*Eps[mu,nu,la,rh]*X[nu]*FS[Wi,la,rh,aa]*(Phibar[ii]*Ta[aa,ii,jj]*DC[Phi[jj],mu] - DC[Phibar[ii],mu]*Ta[aa,ii,jj]*Phi[jj]), FlavorExpand->{SU2D,SU2W}]]",
      "delayed": true
    },
    {
      "name": "LNP",
      "expression": "LXkin + LhXkin + LXhX + LXFkin + LXFmass + LXFX + LXYukawa + LXHYuk + LDF1 + LDF2",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LSM + LNP",
      "delayed": true
    }
  ]
}
```