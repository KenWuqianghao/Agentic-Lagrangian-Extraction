I'll start by reading the paper, the schema, and the SM file.
I read only the paper, `tools/frgen/frmodel.py`, and `tools/feynrules/test_files/models/SM.fr`. No cached or reference `.fr` file for this model was opened.

## Charge derivation (rule 5)

Table I lists **Y(H) = +1/2** but **X(H) = −x_H/2**, while Eq. (1) writes `qbar_L H u_R`, which needs **Y(H) = −1/2**. The two are inconsistent. Re-deriving from SM.fr conventions (`Phi` has Y = +1/2, `LL` Y = −1/2, `QL` Y = +1/6):

| field | Y (SM.fr) | U(1)_X charge |
|---|---|---|
| QL | 1/6 | `xQL = xH/6 + xPhi/3` |
| uR | 2/3 | `xuR = 2 xH/3 + xPhi/3` |
| dR | −1/3 | `xdR = -xH/3 + xPhi/3` |
| LL | −1/2 | `xLL = -xH/2 - xPhi` |
| lR | −1 | `xlR = -xH - xPhi` |
| NR | 0 | `xNR = -xPhi` |
| **Phi (SM.fr)** | **+1/2** | **`xPhiH = +xH/2`** |
| PhiX | 0 | `xPhiS = 2 xPhi` |

**Sign chosen: X(Phi) = +x_H/2, not the table's −x_H/2.** Reason: with SM.fr's `Phi` (Y = +1/2), the four Yukawas `QLbar.dR Phi`, `LLbar.lR Phi`, `QLbar.uR Phibar Eps`, `LLbar.NR Phibar Eps` all give X-sum 0 only for +x_H/2. The paper's table charge −x_H/2 belongs to its own `H`, which is SM.fr's `Phibar`. All fermion charges are copied unchanged from Table I (verified against Table II rows x_H = −2 and −1).

Z–Z′ mixing (the `xH^2 v^2/4` piece of Eq. 4) is kept in `vevX` but the Higgs-doublet Z′ current is not written, exactly as the paper's own phenomenology does (Eq. 6 lists fermion currents only, Eq. 4 uses M_Z′ ≃ 2g′v_Φ). The U(1)_X sector is written in unitary gauge, so the eaten Goldstone is not a class.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling | coupling dim (4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | X sum (U(1)_X) | L sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin | `FS[Zp]FS[Zp]` | 4 | 1 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LZpkin | `MZp^2 Zp Zp` | 2 | `MZp^2` | 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (from ⟨PhiX⟩, X=2xPhi) | 0 | n/a | self-conjugate |
| LNfree | `Nhbar Ga del Nh` | 4 | 1 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LNfree | `MNh Nhbar Nh` | 3 | `MNh` | 1 ✓ | n/a | 0 | 0 | singlet | singlet | −2xPhi + 2xPhi(⟨PhiX⟩) = 0 | ΔL = 2 (Majorana, intended) | n/a | self-conjugate |
| LZpF (QL) | `Zp QLbar Ga QL` | 4 | `gX xQL` | 0 ✓ | n/a | 0 | −1/6+1/6 = 0 | shared `ii` (SU2D) | shared Colour | −xQL+xQL = 0 | 0 | n/a | self-conjugate current |
| LZpF (uR) | `Zp uRbar Ga uR` | 4 | `gX xuR` | 0 ✓ | n/a | 0 | 0 | singlet | shared Colour | 0 | 0 | n/a | self-conjugate |
| LZpF (dR) | `Zp dRbar Ga dR` | 4 | `gX xdR` | 0 ✓ | n/a | 0 | 0 | singlet | shared Colour | 0 | 0 | n/a | self-conjugate |
| LZpF (LL) | `Zp LLbar Ga LL` | 4 | `gX xLL` | 0 ✓ | n/a | 0 | 0 | shared `ii` (SU2D) | singlet | 0 | 0 | n/a | self-conjugate |
| LZpF (lR) | `Zp lRbar Ga lR` | 4 | `gX xlR` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LZpF (NR) | `Zp NRbar Ga NR` | 4 | `gX xNR` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LZpS | `vevX phiX Zp Zp` | 3 | `gX^2 xPhiS^2 vevX` | 1 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LZpS | `phiX^2 Zp Zp` | 4 | `gX^2 xPhiS^2` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LPhiX | `del[PhiXbar] del[PhiX]` | 4 | 1 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | −xPhiS+xPhiS = 0 | 0 | n/a | self-conjugate |
| LPhiX | `muX^2 PhiXbar PhiX` | 2 | `muX^2` | 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LPhiX | `lamPhi (PhiXbar PhiX)^2` | 4 | `lamPhi` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LPhiX | `lamHP Phibar[ii]Phi[ii] PhiXbar PhiX` | 4 | `lamHP` | 0 ✓ | n/a | 0 | −1/2+1/2+0+0 = 0 | shared `ii` | singlet | −xPhiH+xPhiH−xPhiS+xPhiS = 0 | 0 | n/a | self-conjugate |
| LNYukD | `yNu LLbar.NR Phibar[jj] Eps[ii,jj]` | 4 | `yNu` | 0 ✓ | n/a | 0 | +1/2+0−1/2 = 0 | `Eps[ii,jj]`, `LLbar[ii]` with `Phibar[jj]` | singlet | +xH/2+xPhi −xPhi −xH/2 = 0 | −1+1 = 0 | no (paper writes N_R) | `HC[yuk]` |
| LNYukM | `yN phiX bar[CC[NR]].NR` | 4 | `yN/(2 Sqrt[2])` | 0 ✓ | n/a | 0 | 0+0+0 = 0 | singlet | singlet | 2xPhi(phiX) − xPhi − xPhi = 0 | ΔL = 2 (Majorana, intended) | **yes** | `HC[yuk]` |

Per-class free-field confirmation: `Zp` → `LZpkin` ✓ in `LU1X`; `Nh` → `LNfree` ✓ in `LU1X`; `phiX` → `LPhiX` (through the unphysical `PhiX` whose definition is `(vevX + phiX)/Sqrt[2]`, giving `1/2 del[phiX,mu] del[phiX,mu] - 1/2 MphiX^2 phiX^2` with `MphiX == Sqrt[2 lamPhi] vevX`) ✓ in `LU1X`. `NR` and `PhiX` are Unphysical and carry no free term of their own.

`SelfConjugate -> True` classes: `Zp` (V[10]), `phiX` (S[10]), `Nh` (F[10]) — none of them carries `QuantumNumbers`. Confirmed.

Reference or cached model file read: **none**.

No EFT cutoff appears: every operator has d ≤ 4, so no `1/Lambda^n` factor and no cutoff parameter is needed.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["A. Das", "P. S. Bhupal Dev", "Y. Hosotani", "S. Mandal"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": [
      "Kyungpook National University",
      "Hokkaido University",
      "Washington University in St. Louis",
      "Osaka University",
      "IFIC, CSIC/Universitat de Valencia"
    ],
    "emails": [
      "arindamdas@oia.hokudai.ac.jp",
      "bdev@wustl.edu",
      "hosotani@het.phys.sci.osaka-u.ac.jp",
      "smandal@ific.uv.es"
    ]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "ZPRIME",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "Superscript[g,\"\\[Prime]\"]",
      "description": "U(1)X gauge coupling g' [dimensionless], Eq.(6); benchmark g'=0.4 for MZ'=7.5 TeV"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "2.",
      "block_name": "ZPRIME",
      "order_block": 2,
      "tex": "Subscript[x,H]",
      "description": "U(1)X charge parameter x_H [dimensionless], Table I; x_H=0 gives B-L, x_H=-2 gives U(1)R"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 3,
      "tex": "Subscript[x,\\[CapitalPhi]]",
      "description": "U(1)X charge parameter x_Phi [dimensionless], Table I; fixed to 1 in the paper"
    },
    {
      "name": "lamPhi",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "ZPRIME",
      "order_block": 4,
      "interaction_order": ["QED", 2],
      "tex": "Subscript[\\[Lambda],\\[CapitalPhi]]",
      "description": "Quartic self-coupling lambda_Phi of the U(1)X singlet scalar [dimensionless], Eq.(2)"
    },
    {
      "name": "lamHP",
      "parameter_type": "External",
      "value": "0.001",
      "block_name": "ZPRIME",
      "order_block": 5,
      "interaction_order": ["QED", 2],
      "tex": "Superscript[\\[Lambda],\"\\[Prime]\"]",
      "description": "Higgs portal quartic coupling lambda' between H and Phi [dimensionless], Eq.(2); small in the paper"
    },
    {
      "name": "mDnu",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "ZPRIME",
      "order_block": 6,
      "description": "Dirac neutrino mass scale m_D [GeV] of the seesaw, Eq.(5); sets the Dirac Yukawa Y_nu"
    },
    {
      "name": "vevX",
      "parameter_type": "Internal",
      "value": "Sqrt[MZp^2/gX^2 - xH^2 vev^2/4]/(2 xPhi)",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[v,\\[CapitalPhi]]",
      "description": "U(1)X breaking vacuum expectation value v_Phi [GeV], inverted from Eq.(4)"
    },
    {
      "name": "muX",
      "parameter_type": "Internal",
      "value": "Sqrt[vevX^2 lamPhi]",
      "tex": "Subscript[\\[Mu],\\[CapitalPhi]]",
      "description": "Quadratic coefficient of the singlet scalar potential [GeV], Eq.(2), fixed by the minimum condition"
    },
    {
      "name": "MphiX",
      "parameter_type": "Internal",
      "value": "Sqrt[2 lamPhi] vevX",
      "tex": "Subscript[M,\\[CurlyPhi]]",
      "description": "Mass of the physical U(1)X singlet scalar phi [GeV], Eq.(2)-(3)"
    },
    {
      "name": "xQL",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)X charge of the left-handed quark doublet q_L, Table I"
    },
    {
      "name": "xuR",
      "parameter_type": "Internal",
      "value": "2 xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed up-type quark u_R, Table I"
    },
    {
      "name": "xdR",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed down-type quark d_R, Table I"
    },
    {
      "name": "xLL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)X charge of the left-handed lepton doublet l_L, Table I"
    },
    {
      "name": "xlR",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)X charge of the right-handed charged lepton e_R, Table I"
    },
    {
      "name": "xNR",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)X charge of the right-handed neutrino N_R, Table I"
    },
    {
      "name": "xPhiH",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)X charge of the SM.fr Higgs doublet Phi (Y=+1/2); sign re-derived from Yukawa invariance, Table I"
    },
    {
      "name": "xPhiS",
      "parameter_type": "Internal",
      "value": "2 xPhi",
      "description": "U(1)X charge of the SM-singlet scalar Phi, Table I"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yN[1,1]", "rhs": "Sqrt[2] MN1/vevX"},
        {"lhs": "yN[2,2]", "rhs": "Sqrt[2] MN2/vevX"},
        {"lhs": "yN[3,3]", "rhs": "Sqrt[2] MN3/vevX"}
      ],
      "definitions": [
        {"lhs": "yN[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "interaction_order": ["QED", 1],
      "parameter_name": "yN",
      "tex": "Superscript[Y,N]",
      "description": "Majorana Yukawa couplings Y_N of the RHNs to the singlet Phi, Eq.(1); m_N = Y_N v_Phi/Sqrt[2]"
    },
    {
      "name": "yNu",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yNu[1,1]", "rhs": "Sqrt[2] mDnu/vev"},
        {"lhs": "yNu[2,2]", "rhs": "Sqrt[2] mDnu/vev"},
        {"lhs": "yNu[3,3]", "rhs": "Sqrt[2] mDnu/vev"}
      ],
      "definitions": [
        {"lhs": "yNu[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "interaction_order": ["QED", 1],
      "parameter_name": "yNu",
      "tex": "Superscript[Y,\\[Nu]]",
      "description": "Dirac neutrino Yukawa couplings Y_nu of l_L, H and N_R, Eq.(1); m_D = Y_nu v/Sqrt[2]"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 10,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "1353."},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 10,
      "class_name": "phiX",
      "self_conjugate": true,
      "mass": {"sym": "MphiX", "value": "Internal"},
      "width": {"sym": "WphiX", "value": "50."},
      "pdg": 9900025,
      "particle_name": "phiX",
      "full_name": "U1X singlet scalar",
      "propagator_label": "phiX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 10,
      "class_name": "Nh",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MNh",
        "members": [["MN1", "10000."], ["MN2", "10000."], ["MN3", "10000."]]
      },
      "width": {
        "sym": "WNh",
        "members": [["WN1", "10."], ["WN2", "10."], ["WN3", "10."]]
      },
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["Heavy neutrino 1", "Heavy neutrino 2", "Heavy neutrino 3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 11,
      "class_name": "NR",
      "self_conjugate": false,
      "unphysical": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "quantum_numbers": {"Y": "0", "LeptonNumber": "1"},
      "definitions": [
        "NR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] Nh[sp2,ff]]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 11,
      "class_name": "PhiX",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0"},
      "definitions": [
        "PhiX -> (vevX + phiX)/Sqrt[2]"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LZpkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]"
    },
    {
      "name": "LNfree",
      "delayed": true,
      "expression": "Block[{mu, sp, ff}, ExpandIndices[I/2 Nhbar.Ga[mu].del[Nh, mu] - 1/2 MNh[ff] Nhbar[sp, ff].Nh[sp, ff], FlavorExpand -> Generation]]"
    },
    {
      "name": "LPhiX",
      "delayed": true,
      "expression": "Block[{mu, ii}, ExpandIndices[del[PhiXbar, mu] del[PhiX, mu] + muX^2 PhiXbar PhiX - lamPhi PhiXbar PhiX PhiXbar PhiX - lamHP Phibar[ii] Phi[ii] PhiXbar PhiX, FlavorExpand -> SU2D]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gX Zp[mu] (xQL QLbar.Ga[mu].QL + xuR uRbar.Ga[mu].uR + xdR dRbar.Ga[mu].dR + xLL LLbar.Ga[mu].LL + xlR lRbar.Ga[mu].lR + xNR NRbar.Ga[mu].NR), FlavorExpand -> {SU2W, SU2D}] /. {CKM[a_, b_] Conjugate[CKM[a_, c_]] -> IndexDelta[b, c], CKM[b_, a_] Conjugate[CKM[c_, a_]] -> IndexDelta[b, c]}]"
    },
    {
      "name": "LZpS",
      "delayed": true,
      "expression": "Block[{mu}, gX^2 xPhiS^2 (vevX phiX + phiX^2/2) Zp[mu] Zp[mu]]"
    },
    {
      "name": "LNYukD",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, ff1, ff2, yuk}, yuk = ExpandIndices[-yNu[ff1, ff2] LLbar[sp, ii, ff1].NR[sp, ff2] Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LNYukM",
      "delayed": true,
      "expression": "Block[{sp, ff1, ff2, yuk}, yuk = ExpandIndices[-1/(2 Sqrt[2]) yN[ff1, ff2] phiX bar[CC[NR[sp, ff1]]].NR[sp, ff2], FlavorExpand -> Generation]; yuk + HC[yuk]]"
    },
    {
      "name": "LU1X",
      "delayed": true,
      "expression": "LZpkin + LNfree + LPhiX + LZpF + LZpS + LNYukD + LNYukM"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LU1X"
    }
  ]
}
```
I read only the paper, `tools/frgen/frmodel.py`, and `tools/feynrules/test_files/models/SM.fr`. No cached or reference `.fr` file for this model was opened.

## Charge derivation (rule 5)

Table I lists **Y(H) = +1/2** but **X(H) = −x_H/2**, while Eq. (1) writes `qbar_L H u_R`, which needs **Y(H) = −1/2**. The two are inconsistent. Re-deriving from SM.fr conventions (`Phi` has Y = +1/2, `LL` Y = −1/2, `QL` Y = +1/6):

| field | Y (SM.fr) | U(1)_X charge |
|---|---|---|
| QL | 1/6 | `xQL = xH/6 + xPhi/3` |
| uR | 2/3 | `xuR = 2 xH/3 + xPhi/3` |
| dR | −1/3 | `xdR = -xH/3 + xPhi/3` |
| LL | −1/2 | `xLL = -xH/2 - xPhi` |
| lR | −1 | `xlR = -xH - xPhi` |
| NR | 0 | `xNR = -xPhi` |
| **Phi (SM.fr)** | **+1/2** | **`xPhiH = +xH/2`** |
| PhiX | 0 | `xPhiS = 2 xPhi` |

**Sign chosen: X(Phi) = +x_H/2, not the table's −x_H/2.** Reason: with SM.fr's `Phi` (Y = +1/2), the four Yukawas `QLbar.dR Phi`, `LLbar.lR Phi`, `QLbar.uR Phibar Eps`, `LLbar.NR Phibar Eps` all give X-sum 0 only for +x_H/2. The paper's table charge −x_H/2 belongs to its own `H`, which is SM.fr's `Phibar`. All fermion charges are copied unchanged from Table I (verified against Table II rows x_H = −2 and −1).

Z–Z′ mixing (the `xH^2 v^2/4` piece of Eq. 4) is kept in `vevX` but the Higgs-doublet Z′ current is not written, exactly as the paper's own phenomenology does (Eq. 6 lists fermion currents only, Eq. 4 uses M_Z′ ≃ 2g′v_Φ). The U(1)_X sector is written in unitary gauge, so the eaten Goldstone is not a class.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling | coupling dim (4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | X sum (U(1)_X) | L sum | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin | `FS[Zp]FS[Zp]` | 4 | 1 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LZpkin | `MZp^2 Zp Zp` | 2 | `MZp^2` | 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (from ⟨PhiX⟩, X=2xPhi) | 0 | n/a | self-conjugate |
| LNfree | `Nhbar Ga del Nh` | 4 | 1 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LNfree | `MNh Nhbar Nh` | 3 | `MNh` | 1 ✓ | n/a | 0 | 0 | singlet | singlet | −2xPhi + 2xPhi(⟨PhiX⟩) = 0 | ΔL = 2 (Majorana, intended) | n/a | self-conjugate |
| LZpF (QL) | `Zp QLbar Ga QL` | 4 | `gX xQL` | 0 ✓ | n/a | 0 | −1/6+1/6 = 0 | shared `ii` (SU2D) | shared Colour | −xQL+xQL = 0 | 0 | n/a | self-conjugate current |
| LZpF (uR) | `Zp uRbar Ga uR` | 4 | `gX xuR` | 0 ✓ | n/a | 0 | 0 | singlet | shared Colour | 0 | 0 | n/a | self-conjugate |
| LZpF (dR) | `Zp dRbar Ga dR` | 4 | `gX xdR` | 0 ✓ | n/a | 0 | 0 | singlet | shared Colour | 0 | 0 | n/a | self-conjugate |
| LZpF (LL) | `Zp LLbar Ga LL` | 4 | `gX xLL` | 0 ✓ | n/a | 0 | 0 | shared `ii` (SU2D) | singlet | 0 | 0 | n/a | self-conjugate |
| LZpF (lR) | `Zp lRbar Ga lR` | 4 | `gX xlR` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LZpF (NR) | `Zp NRbar Ga NR` | 4 | `gX xNR` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LZpS | `vevX phiX Zp Zp` | 3 | `gX^2 xPhiS^2 vevX` | 1 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LZpS | `phiX^2 Zp Zp` | 4 | `gX^2 xPhiS^2` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LPhiX | `del[PhiXbar] del[PhiX]` | 4 | 1 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | −xPhiS+xPhiS = 0 | 0 | n/a | self-conjugate |
| LPhiX | `muX^2 PhiXbar PhiX` | 2 | `muX^2` | 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LPhiX | `lamPhi (PhiXbar PhiX)^2` | 4 | `lamPhi` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conjugate |
| LPhiX | `lamHP Phibar[ii]Phi[ii] PhiXbar PhiX` | 4 | `lamHP` | 0 ✓ | n/a | 0 | −1/2+1/2+0+0 = 0 | shared `ii` | singlet | −xPhiH+xPhiH−xPhiS+xPhiS = 0 | 0 | n/a | self-conjugate |
| LNYukD | `yNu LLbar.NR Phibar[jj] Eps[ii,jj]` | 4 | `yNu` | 0 ✓ | n/a | 0 | +1/2+0−1/2 = 0 | `Eps[ii,jj]`, `LLbar[ii]` with `Phibar[jj]` | singlet | +xH/2+xPhi −xPhi −xH/2 = 0 | −1+1 = 0 | no (paper writes N_R) | `HC[yuk]` |
| LNYukM | `yN phiX bar[CC[NR]].NR` | 4 | `yN/(2 Sqrt[2])` | 0 ✓ | n/a | 0 | 0+0+0 = 0 | singlet | singlet | 2xPhi(phiX) − xPhi − xPhi = 0 | ΔL = 2 (Majorana, intended) | **yes** | `HC[yuk]` |

Per-class free-field confirmation: `Zp` → `LZpkin` ✓ in `LU1X`; `Nh` → `LNfree` ✓ in `LU1X`; `phiX` → `LPhiX` (through the unphysical `PhiX` whose definition is `(vevX + phiX)/Sqrt[2]`, giving `1/2 del[phiX,mu] del[phiX,mu] - 1/2 MphiX^2 phiX^2` with `MphiX == Sqrt[2 lamPhi] vevX`) ✓ in `LU1X`. `NR` and `PhiX` are Unphysical and carry no free term of their own.

`SelfConjugate -> True` classes: `Zp` (V[10]), `phiX` (S[10]), `Nh` (F[10]) — none of them carries `QuantumNumbers`. Confirmed.

Reference or cached model file read: **none**.

No EFT cutoff appears: every operator has d ≤ 4, so no `1/Lambda^n` factor and no cutoff parameter is needed.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["A. Das", "P. S. Bhupal Dev", "Y. Hosotani", "S. Mandal"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": [
      "Kyungpook National University",
      "Hokkaido University",
      "Washington University in St. Louis",
      "Osaka University",
      "IFIC, CSIC/Universitat de Valencia"
    ],
    "emails": [
      "arindamdas@oia.hokudai.ac.jp",
      "bdev@wustl.edu",
      "hosotani@het.phys.sci.osaka-u.ac.jp",
      "smandal@ific.uv.es"
    ]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "ZPRIME",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "Superscript[g,\"\\[Prime]\"]",
      "description": "U(1)X gauge coupling g' [dimensionless], Eq.(6); benchmark g'=0.4 for MZ'=7.5 TeV"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "2.",
      "block_name": "ZPRIME",
      "order_block": 2,
      "tex": "Subscript[x,H]",
      "description": "U(1)X charge parameter x_H [dimensionless], Table I; x_H=0 gives B-L, x_H=-2 gives U(1)R"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 3,
      "tex": "Subscript[x,\\[CapitalPhi]]",
      "description": "U(1)X charge parameter x_Phi [dimensionless], Table I; fixed to 1 in the paper"
    },
    {
      "name": "lamPhi",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "ZPRIME",
      "order_block": 4,
      "interaction_order": ["QED", 2],
      "tex": "Subscript[\\[Lambda],\\[CapitalPhi]]",
      "description": "Quartic self-coupling lambda_Phi of the U(1)X singlet scalar [dimensionless], Eq.(2)"
    },
    {
      "name": "lamHP",
      "parameter_type": "External",
      "value": "0.001",
      "block_name": "ZPRIME",
      "order_block": 5,
      "interaction_order": ["QED", 2],
      "tex": "Superscript[\\[Lambda],\"\\[Prime]\"]",
      "description": "Higgs portal quartic coupling lambda' between H and Phi [dimensionless], Eq.(2); small in the paper"
    },
    {
      "name": "mDnu",
      "parameter_type": "External",
      "value": "1.*^-4",
      "block_name": "ZPRIME",
      "order_block": 6,
      "description": "Dirac neutrino mass scale m_D [GeV] of the seesaw, Eq.(5); sets the Dirac Yukawa Y_nu"
    },
    {
      "name": "vevX",
      "parameter_type": "Internal",
      "value": "Sqrt[MZp^2/gX^2 - xH^2 vev^2/4]/(2 xPhi)",
      "interaction_order": ["QED", -1],
      "tex": "Subscript[v,\\[CapitalPhi]]",
      "description": "U(1)X breaking vacuum expectation value v_Phi [GeV], inverted from Eq.(4)"
    },
    {
      "name": "muX",
      "parameter_type": "Internal",
      "value": "Sqrt[vevX^2 lamPhi]",
      "tex": "Subscript[\\[Mu],\\[CapitalPhi]]",
      "description": "Quadratic coefficient of the singlet scalar potential [GeV], Eq.(2), fixed by the minimum condition"
    },
    {
      "name": "MphiX",
      "parameter_type": "Internal",
      "value": "Sqrt[2 lamPhi] vevX",
      "tex": "Subscript[M,\\[CurlyPhi]]",
      "description": "Mass of the physical U(1)X singlet scalar phi [GeV], Eq.(2)-(3)"
    },
    {
      "name": "xQL",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)X charge of the left-handed quark doublet q_L, Table I"
    },
    {
      "name": "xuR",
      "parameter_type": "Internal",
      "value": "2 xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed up-type quark u_R, Table I"
    },
    {
      "name": "xdR",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed down-type quark d_R, Table I"
    },
    {
      "name": "xLL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)X charge of the left-handed lepton doublet l_L, Table I"
    },
    {
      "name": "xlR",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)X charge of the right-handed charged lepton e_R, Table I"
    },
    {
      "name": "xNR",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)X charge of the right-handed neutrino N_R, Table I"
    },
    {
      "name": "xPhiH",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)X charge of the SM.fr Higgs doublet Phi (Y=+1/2); sign re-derived from Yukawa invariance, Table I"
    },
    {
      "name": "xPhiS",
      "parameter_type": "Internal",
      "value": "2 xPhi",
      "description": "U(1)X charge of the SM-singlet scalar Phi, Table I"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yN[1,1]", "rhs": "Sqrt[2] MN1/vevX"},
        {"lhs": "yN[2,2]", "rhs": "Sqrt[2] MN2/vevX"},
        {"lhs": "yN[3,3]", "rhs": "Sqrt[2] MN3/vevX"}
      ],
      "definitions": [
        {"lhs": "yN[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "interaction_order": ["QED", 1],
      "parameter_name": "yN",
      "tex": "Superscript[Y,N]",
      "description": "Majorana Yukawa couplings Y_N of the RHNs to the singlet Phi, Eq.(1); m_N = Y_N v_Phi/Sqrt[2]"
    },
    {
      "name": "yNu",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yNu[1,1]", "rhs": "Sqrt[2] mDnu/vev"},
        {"lhs": "yNu[2,2]", "rhs": "Sqrt[2] mDnu/vev"},
        {"lhs": "yNu[3,3]", "rhs": "Sqrt[2] mDnu/vev"}
      ],
      "definitions": [
        {"lhs": "yNu[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "interaction_order": ["QED", 1],
      "parameter_name": "yNu",
      "tex": "Superscript[Y,\\[Nu]]",
      "description": "Dirac neutrino Yukawa couplings Y_nu of l_L, H and N_R, Eq.(1); m_D = Y_nu v/Sqrt[2]"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 10,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "1353."},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 10,
      "class_name": "phiX",
      "self_conjugate": true,
      "mass": {"sym": "MphiX", "value": "Internal"},
      "width": {"sym": "WphiX", "value": "50."},
      "pdg": 9900025,
      "particle_name": "phiX",
      "full_name": "U1X singlet scalar",
      "propagator_label": "phiX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 10,
      "class_name": "Nh",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MNh",
        "members": [["MN1", "10000."], ["MN2", "10000."], ["MN3", "10000."]]
      },
      "width": {
        "sym": "WNh",
        "members": [["WN1", "10."], ["WN2", "10."], ["WN3", "10."]]
      },
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["Heavy neutrino 1", "Heavy neutrino 2", "Heavy neutrino 3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 11,
      "class_name": "NR",
      "self_conjugate": false,
      "unphysical": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "quantum_numbers": {"Y": "0", "LeptonNumber": "1"},
      "definitions": [
        "NR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] Nh[sp2,ff]]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 11,
      "class_name": "PhiX",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0"},
      "definitions": [
        "PhiX -> (vevX + phiX)/Sqrt[2]"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LZpkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]"
    },
    {
      "name": "LNfree",
      "delayed": true,
      "expression": "Block[{mu, sp, ff}, ExpandIndices[I/2 Nhbar.Ga[mu].del[Nh, mu] - 1/2 MNh[ff] Nhbar[sp, ff].Nh[sp, ff], FlavorExpand -> Generation]]"
    },
    {
      "name": "LPhiX",
      "delayed": true,
      "expression": "Block[{mu, ii}, ExpandIndices[del[PhiXbar, mu] del[PhiX, mu] + muX^2 PhiXbar PhiX - lamPhi PhiXbar PhiX PhiXbar PhiX - lamHP Phibar[ii] Phi[ii] PhiXbar PhiX, FlavorExpand -> SU2D]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gX Zp[mu] (xQL QLbar.Ga[mu].QL + xuR uRbar.Ga[mu].uR + xdR dRbar.Ga[mu].dR + xLL LLbar.Ga[mu].LL + xlR lRbar.Ga[mu].lR + xNR NRbar.Ga[mu].NR), FlavorExpand -> {SU2W, SU2D}] /. {CKM[a_, b_] Conjugate[CKM[a_, c_]] -> IndexDelta[b, c], CKM[b_, a_] Conjugate[CKM[c_, a_]] -> IndexDelta[b, c]}]"
    },
    {
      "name": "LZpS",
      "delayed": true,
      "expression": "Block[{mu}, gX^2 xPhiS^2 (vevX phiX + phiX^2/2) Zp[mu] Zp[mu]]"
    },
    {
      "name": "LNYukD",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, ff1, ff2, yuk}, yuk = ExpandIndices[-yNu[ff1, ff2] LLbar[sp, ii, ff1].NR[sp, ff2] Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LNYukM",
      "delayed": true,
      "expression": "Block[{sp, ff1, ff2, yuk}, yuk = ExpandIndices[-1/(2 Sqrt[2]) yN[ff1, ff2] phiX bar[CC[NR[sp, ff1]]].NR[sp, ff2], FlavorExpand -> Generation]; yuk + HC[yuk]]"
    },
    {
      "name": "LU1X",
      "delayed": true,
      "expression": "LZpkin + LNfree + LPhiX + LZpF + LZpS + LNYukD + LNYukM"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LSM + LU1X"
    }
  ]
}
```