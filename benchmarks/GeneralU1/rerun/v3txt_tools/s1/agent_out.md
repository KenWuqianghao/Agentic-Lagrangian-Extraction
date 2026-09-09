Self-audit table (produced before the model)

Conventions used: SM.fr hypercharges (`Phi` Y=+1/2, `LL` Y=−1/2, `QL` Y=+1/6). New U(1)X charges are the Table I values, written as Internal parameters: `xQ = xH/6 + xPhi/3`, `xU = 2xH/3 + xPhi/3`, `xD = −xH/3 + xPhi/3`, `xL = −xH/2 − xPhi`, `xE = −xH − xPhi`, `xN = −xPhi`, `xHd = xH/2`, `xS = 2xPhi`.

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Lambda power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | X sum (must be 0) | L/B sum | CC[] where paper writes psi^c | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin | FS[Zp]FS[Zp] | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | real field, self-Hermitian |
| LZpKin | Zp Zp | 2 | MZp^2 | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Eq.(4) root: `Sqrt[4 vPhi^2 + xH^2 v^2/4]`, fixed by the stated limit `MZ' ~ 2 g' vPhi` | real field, self-Hermitian |
| LZpF (quark doublet) | QLbar Ga QL Zp | 4 | gX xQ | 0 | n/a | 0 | −1/6+1/6=0 | shared SU2D index, singlet | shared Colour index | −xQ+xQ=0 | B: −1/3+1/3=0 | n/a | n/a | self-Hermitian current |
| LZpF (uR) | uRbar Ga uR Zp | 4 | gX xU | 0 | n/a | 0 | −2/3+2/3=0 | singlet | shared Colour | −xU+xU=0 | 0 | n/a | n/a | self-Hermitian |
| LZpF (dR) | dRbar Ga dR Zp | 4 | gX xD | 0 | n/a | 0 | 1/3−1/3=0 | singlet | shared Colour | −xD+xD=0 | 0 | n/a | n/a | self-Hermitian |
| LZpF (lepton doublet) | LLbar Ga LL Zp | 4 | gX xL | 0 | n/a | 0 | 1/2−1/2=0 | shared SU2D index | singlet | −xL+xL=0 | L: 0 | n/a | n/a | self-Hermitian |
| LZpF (lR) | lRbar Ga lR Zp | 4 | gX xE | 0 | n/a | 0 | 1−1=0 | singlet | singlet | −xE+xE=0 | L: 0 | n/a | n/a | self-Hermitian |
| LZpF (RHN) | NXbar Ga ProjP NX Zp | 4 | gX xN | 0 | n/a | 0 | 0 | singlet | singlet | −xN+xN=0 | L: 0 | Majorana class (`SelfConjugate -> True`, so `CC[NX] = NX`); chirality carried by `ProjP` | n/a | self-Hermitian |
| LhXKin | del hX del hX | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | real field |
| LhXKin | hX hX | 2 | MhX^2 | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | real field |
| LhXPot | hX^3 | 3 | lamX vX | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | `lamX = MhX^2/(2 vX^2)` cross-checked against `MhX^2 = 2 lamPhi vPhi^2` from Eq.(2)–(3) | real |
| LhXPot | hX^4 | 4 | lamX/4 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | as above | real |
| LZpS | hX Zp Zp | 3 | gX^2 xS^2 vX | 1 | n/a | 0 | 0 | singlet | singlet | 0 (`hX` is the neutral radial mode of Phi) | 0 | n/a | coefficient checked against `MZp^2/vX`, the same relation as Eq.(4) | real |
| LZpS | hX hX Zp Zp | 4 | gX^2 xS^2/2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | as above | real |
| LNKin | NXbar Ga del NX | 4 | I/2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | Majorana, factor 1/2 present | n/a | self-Hermitian |
| LNKin | NXbar MNdiag NX | 3 | MNdiag | 1 | n/a | 0 | 0 | singlet | singlet | 0 | L violated by 2 (Majorana, as in Eq.(1)) | Majorana mass written `−1/2 M NXbar.NX` | n/a | self-Hermitian |
| LNMaj | hX NXbar ProjP NX | 4 | yN/(2 Sqrt[2]) | 0 | n/a | 0 | 0 | singlet | singlet | X(Phi)+2X(NR) = 2xPhi−2xPhi = 0 | L violated by 2 | yes — paper's `Phi N^c_R N_R`; `NX` is `SelfConjugate -> True` so `CC[NX] = NX`, chirality by `ProjP`; vev piece is in LNKin, no double counting | `mN = YN vPhi/Sqrt[2]` (text after Eq.(4)) fixes the `1/Sqrt[2]`, not `Sqrt[2]` | `HC[...]` present |
| LNDir | LLbar NR PhiFbar Eps | 4 | yNu | 0 | n/a | 0 (nu-N-h0) and +1+0−1=0 (l-N-G+) | 1/2+0−1/2=0 | `Eps[ii,jj]` on two distinct indices, LLbar with PhiFbar (same conjugation type, the paper's `Htilde` contraction) | singlet | −xL+xN−xHd = (xH/2+xPhi) −xPhi −xH/2 = 0 | L: +1 −1 = 0 before the Majorana mass | n/a (no `psi^c` in this term) | n/a | `HC[...]` present |

Per-class kinetic + mass confirmation: `Zp` -> LZpKin; `hX` -> LhXKin; `NX` -> LNKin (kinetic + `−1/2 NXbar.MNdiag.NX`, `MNdiag = diag(MN1, MN2, MN3)`, the class `Mass` symbols). `NR` and `PhiF` are Unphysical classes, so they need no kinetic term. All four terms are in the total sum.

Non-fundamental colour representations: none — every new field is a colour singlet, so no `AddGaugeRepresentation` line is needed.

`SelfConjugate -> True` classes: `Zp`, `hX`, `NX`. None of them carries `QuantumNumbers`. The chiral U(1)X charge sits on Internal parameters (`xQ ... xS`) because it is symbolic (a function of `xH`, `xPhi`) and FeynRules `QuantumNumbers` must be numeric; the Unphysical chiral class `NR` carries only `Y -> 0`.

Name check: classes `Zp, hX, NX, N1, N2, N3, NR, PhiF`; parameters `gX, xH, xPhi, lamHX, yNu, xS, xQ, xU, xD, xL, xE, xN, xHd, vX, lamX, yN, MNdiag, MZp, WZp, MhX, WhX, MN, MN1-3, WN, WN1-3`; indices `Generation, SU2D, Colour` only (all declared by SM.fr, so `index_decls` is empty). None is a Mathematica built-in (`N`, `C`, `D`, `E`, `I`, `K`, `O` are all avoided), none is a FeynRules symbol, none is an SM.fr name, and no name contains a prime or punctuation. All new class indices are 100 or more.

Total Lagrangian: one term, `LTotal`, summing `LZpKin + LZpF + LhXKin + LhXPot + LZpS + LNKin + LNMaj + LNDir` — every other term appears exactly once.

Charge sign choice (rule 5): the paper's Eq.(1) writes `qL H uR` and `qL Htilde dR`, which needs Y(H) = −1/2 and is the opposite of SM.fr. I did not copy that. I re-derived the U(1)X charge of the Higgs from SM.fr invariance: `QLbar.dR Phi` gives X(H) = +xH/2, and `LLbar.lR Phi`, `QLbar.uR Phibar Eps`, `LLbar.NR Phibar Eps`, `Phi N^c N` all give zero with the Table I charges. So Table I is consistent with SM.fr once the Yukawas are written in SM.fr form; only the paper's `H` versus `Htilde` labels are swapped. I therefore keep Table I verbatim and write the new Dirac Yukawa as `LLbar.NR PhiFbar Eps`.

Two deliberate omissions, stated rather than hidden: (1) the seesaw diagonalisation of Eq.(5) is not implemented — the light neutrinos stay massless as in SM.fr, and the Dirac Yukawa uses the vev-free doublet `PhiF` so it produces only the `h/G0/G+` vertices and no undiagonalised nu-N bilinear; (2) the U(1)X current of the SM Higgs doublet is dropped, because it would add a Z-Z' mass mixing of order `v^2/vPhi^2` that the paper neglects (the paper's Z' Lagrangian is Eq.(6), fermions only).

Reference or cached model file read: none. Only the paper text, `frmodel.py`, `render.py` and `SM.fr` were opened. The paper cites a FeynRules file at the GeneralU1 wiki page (Ref. [49]); it is not present in the sandbox and was not fetched.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["A. Das", "P. S. B. Dev", "Y. Hosotani", "S. Mandal"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": ["Extracted from arXiv:2104.10902"],
    "emails": []
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
      "tex": "g_X",
      "description": "U(1)X gauge coupling g-prime; benchmark 0.4 for MZp = 7.5 TeV, Sec. II B"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "2.",
      "block_name": "ZPRIME",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)X charge parameter x_H of Table I; xH = 0 gives B-L, xH = -2 gives U(1)R"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "ZPRIME",
      "order_block": 3,
      "tex": "x_Phi",
      "description": "U(1)X charge parameter x_Phi of Table I; the paper fixes x_Phi = 1"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "ZPRIME",
      "order_block": 4,
      "interaction_order": ["NP", 2],
      "tex": "lambda_prime",
      "description": "Higgs portal quartic lambda-prime of Eq.(2); the paper works in the small lambda-prime limit where H-Phi mixing is negligible, so no portal term enters the Lagrangian"
    },
    {
      "name": "yNu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "YUKNU",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "yNu[1,1]", "rhs": "1.*^-6"},
        {"lhs": "yNu[1,2]", "rhs": "0."},
        {"lhs": "yNu[1,3]", "rhs": "0."},
        {"lhs": "yNu[2,1]", "rhs": "0."},
        {"lhs": "yNu[2,2]", "rhs": "1.*^-6"},
        {"lhs": "yNu[2,3]", "rhs": "0."},
        {"lhs": "yNu[3,1]", "rhs": "0."},
        {"lhs": "yNu[3,2]", "rhs": "0."},
        {"lhs": "yNu[3,3]", "rhs": "1.*^-6"}
      ],
      "tex": "Y_nu",
      "description": "Dirac neutrino Yukawa Y_nu of Eq.(1), dimensionless; default gives m_D = Y_nu v/Sqrt[2] in the seesaw range"
    },
    {
      "name": "xS",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "description": "U(1)X charge of the SM-singlet scalar Phi (Table I)"
    },
    {
      "name": "xQ",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)X charge of the left-handed quark doublet (Table I)"
    },
    {
      "name": "xU",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed up-type quarks (Table I)"
    },
    {
      "name": "xD",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)X charge of the right-handed down-type quarks (Table I)"
    },
    {
      "name": "xL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)X charge of the left-handed lepton doublet (Table I)"
    },
    {
      "name": "xE",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)X charge of the right-handed charged leptons (Table I)"
    },
    {
      "name": "xN",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)X charge of the right-handed neutrinos (Table I)"
    },
    {
      "name": "xHd",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)X charge of the SM Higgs doublet, re-derived from SM.fr Yukawa invariance with Y(Phi) = +1/2 (Table I)"
    },
    {
      "name": "vX",
      "parameter_type": "Internal",
      "value": "Sqrt[MZp^2/gX^2 - xH^2*vev^2/4]/xS",
      "interaction_order": ["NP", -1],
      "tex": "v_Phi",
      "description": "U(1)X vacuum expectation value v_Phi, exact inversion of Eq.(4) MZp = gX Sqrt[4 vPhi^2 + xH^2 v^2/4]"
    },
    {
      "name": "lamX",
      "parameter_type": "Internal",
      "value": "MhX^2/(2*vX^2)",
      "interaction_order": ["NP", 2],
      "tex": "lambda_Phi",
      "description": "Singlet quartic lambda_Phi of Eq.(2), fixed by MhX^2 = 2 lambda_Phi vPhi^2"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "yN[1,1]", "rhs": "Sqrt[2]*MN1/vX"},
        {"lhs": "yN[1,2]", "rhs": "0"},
        {"lhs": "yN[1,3]", "rhs": "0"},
        {"lhs": "yN[2,1]", "rhs": "0"},
        {"lhs": "yN[2,2]", "rhs": "Sqrt[2]*MN2/vX"},
        {"lhs": "yN[2,3]", "rhs": "0"},
        {"lhs": "yN[3,1]", "rhs": "0"},
        {"lhs": "yN[3,2]", "rhs": "0"},
        {"lhs": "yN[3,3]", "rhs": "Sqrt[2]*MN3/vX"}
      ],
      "tex": "Y_N",
      "description": "Majorana Yukawa Y_N of Eq.(1), diagonal and dimensionless; m_N = Y_N vPhi/Sqrt[2]"
    },
    {
      "name": "MNdiag",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "MNdiag[1,1]", "rhs": "MN1"},
        {"lhs": "MNdiag[1,2]", "rhs": "0"},
        {"lhs": "MNdiag[1,3]", "rhs": "0"},
        {"lhs": "MNdiag[2,1]", "rhs": "0"},
        {"lhs": "MNdiag[2,2]", "rhs": "MN2"},
        {"lhs": "MNdiag[2,3]", "rhs": "0"},
        {"lhs": "MNdiag[3,1]", "rhs": "0"},
        {"lhs": "MNdiag[3,2]", "rhs": "0"},
        {"lhs": "MNdiag[3,3]", "rhs": "MN3"}
      ],
      "tex": "M_N",
      "description": "Diagonal Majorana mass matrix of the right-handed neutrinos [GeV], equal to the class mass symbols MN1, MN2, MN3"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
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
      "class_index": 100,
      "class_name": "hX",
      "self_conjugate": true,
      "mass": {"sym": "MhX", "value": "1000."},
      "width": {"sym": "WhX", "value": "1."},
      "pdg": 9900025,
      "particle_name": "hX",
      "full_name": "SingletScalar",
      "propagator_label": "hX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NX",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {
        "sym": "MN",
        "members": [["MN1", "10000."], ["MN2", "10000."], ["MN3", "10000."]]
      },
      "width": {
        "sym": "WN",
        "members": [["WN1", "1."], ["WN2", "1."], ["WN3", "1."]]
      },
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["HeavyNeutrino1", "HeavyNeutrino2", "HeavyNeutrino3"],
      "propagator_label": "N",
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "NR",
      "self_conjugate": false,
      "unphysical": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "quantum_numbers": {"Y": "0"},
      "definitions": [
        "NR[sp1_, ff_] :> Module[{sp2}, ProjP[sp1, sp2] NX[sp2, ff]]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "PhiF",
      "self_conjugate": false,
      "unphysical": true,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "1/2"},
      "definitions": [
        "PhiF[1] -> -I GP",
        "PhiF[2] -> (H + I G0)/Sqrt[2]"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[- gX Zp[mu] (xQ QLbar.Ga[mu].QL + xU uRbar.Ga[mu].uR + xD dRbar.Ga[mu].dR + xL LLbar.Ga[mu].LL + xE lRbar.Ga[mu].lR + xN NXbar.Ga[mu].ProjP.NX), FlavorExpand -> SU2D] /. {CKM[a_, b_] Conjugate[CKM[a_, c_]] -> IndexDelta[b, c], CKM[b_, a_] Conjugate[CKM[c_, a_]] -> IndexDelta[b, c]}]"
    },
    {
      "name": "LhXKin",
      "delayed": true,
      "expression": "Block[{mu}, 1/2 del[hX, mu] del[hX, mu] - 1/2 MhX^2 hX^2]"
    },
    {
      "name": "LhXPot",
      "delayed": true,
      "expression": "- lamX vX hX^3 - lamX/4 hX^4"
    },
    {
      "name": "LZpS",
      "delayed": true,
      "expression": "Block[{mu}, 1/2 gX^2 xS^2 (2 vX hX + hX^2) Zp[mu] Zp[mu]]"
    },
    {
      "name": "LNKin",
      "delayed": true,
      "expression": "Block[{mu}, I/2 NXbar.Ga[mu].del[NX, mu] - 1/2 NXbar.MNdiag.NX]"
    },
    {
      "name": "LNMaj",
      "delayed": true,
      "expression": "Block[{yuk}, yuk = - 1/(2 Sqrt[2]) hX NXbar.yN.ProjP.NX; yuk + HC[yuk]]"
    },
    {
      "name": "LNDir",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, ff1, ff2, yuk, feynmangaugerules}, feynmangaugerules = If[Not[FeynmanGauge], {G0 | GP | GPbar -> 0}, {}]; yuk = ExpandIndices[- yNu[ff1, ff2] LLbar[sp, ii, ff1].NR[sp, ff2] PhiFbar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; yuk + HC[yuk] /. feynmangaugerules]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LZpKin + LZpF + LhXKin + LhXPot + LZpS + LNKin + LNMaj + LNDir"
    }
  ]
}
```