I'll start by reading the paper and the schema.
I read the paper and the schema. No cached or reference `.fr` file for this model exists in the sandbox, and none was read — only `1811.11452.txt`, `frmodel.py`, `render.py`, and `SM.fr`.

## New-physics content found in the paper

| Item | Paper source |
|---|---|
| Abelian gauge field `B'` → mass eigenstate `Z'` (real vector, singlet, Q=0, Y=0) | Eq. (2.3), (2.4) |
| Complex SM-singlet scalar `chi`, Y=0, Y_BL=+2 | Sec. 2, Eq. (2.1) |
| CP-even mass eigenstate `h2` (mixes with SM `h1=H`, angle α) | Eq. (2.11), (2.12) |
| 3 RH neutrinos `vR` (singlet, Q=0, Y=0, Y_BL=−1) → Majorana mass eigenstates N1,N2,N3 | Eq. (2.5)–(2.9) |
| B−L charges: quarks +1/3, leptons −1, H 0, chi +2, vR −1 | Sec. 2 |
| Parameters: g1', MZ', Mh2, sinα, MNi, VlN, x, λ1,2,3, yν, yM | Eq. (2.6), (2.13), (3.1), Table 1 |

**New-U(1) charge sign (rule 5).** SM.fr uses Y(Phi)=+1/2, Y(LL)=−1/2, so the Dirac neutrino Yukawa must be the "up-type" contraction `LLbar[ii] . vR Phibar[jj] Eps[ii,jj]`. Invariance of that term fixes Y_BL(vR) = Y_BL(LL) = −1, and invariance of `chi CC[vRbar].vR` then fixes Y_BL(chi) = +2, with Y_BL(H)=0. This is exactly the paper's table, so no sign flip was needed.

**Implementation choice (hard cutover, mass basis).** SM.fr's `Phi` cannot be re-declared from an add-on, so `h2` is written as a physical mass eigenstate with its own kinetic + mass term, and the gauge-eigenstate content is inserted verbatim as `cosa H + sina h2` (doublet direction) and `cosa h2 - sina H` (singlet direction). `LhMix` supplies the sinα couplings of `h2` to W/Z/fermions and the (cosα−1) correction of `H`; `LVBL` adds the λ1,2,3 self-couplings and cancels SM.fr's own `lam` cubic/quartic. No term regenerates a mass that is already declared.

## Mandatory self-audit

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | Y_BL sum | L/B sum | CC[] where ψ^c | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin (kin) | FS[Zp]·FS[Zp] | 4 | −1/4 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| LZpkin (mass) | MZp²·Zp·Zp | 4 | MZp² (dim 2) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lh2kin (kin) | del[h2]·del[h2] | 4 | 1/2 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lh2kin (mass) | Mh2²·h2·h2 | 4 | Mh2² (dim 2) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| LNkin (kin) | NNbar·Ga·del[NN] | 4 | I/2 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | ΔL=0 | Majorana `SelfConjugate->True` | self-conj ✓ |
| LNkin (mass) | MN·NNbar·NN | 4 | MN (dim 1) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 | ΔL=2 (Majorana, by construction) | Majorana field | self-conj ✓ |
| LZpF (quarks) | QLbar·Ga·QL·Zp etc. | 4 | g1p | 0 ✓ | n/a | 0 | 0 | shared SU2D index (singlet) | shared Colour index | +1/3−1/3=0 | 0 | n/a | self-conj ✓ |
| LZpF (leptons) | LLbar·Ga·LL·Zp, lRbar·Ga·lR·Zp, vRbar·Ga·vR·Zp | 4 | g1p | 0 ✓ | n/a | 0 | 0 | shared SU2D index | singlet | −1+1=0 | 0 | n/a | self-conj ✓ |
| LZpS (trilinear) | Zp·Zp·(cosa h2 − sina H) | 4 | MZp²/vBL (dim 1) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 (post-breaking mass basis; from \|Dχ\|², Y_BL(χ)=+2 cancels between χ and χ†) | 0 | n/a | real ✓ |
| LZpS (quartic) | Zp·Zp·(…)² | 4 | MZp²/(2 vBL²) (dim 0) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | real ✓ |
| LhMix (VV) | (cosa H+sina h2)·Wbar·W, ·Z·Z | 4 | MW²/vev, MZ²/vev (dim 1) | ✓ | n/a | 0 | 0 | mass basis (post-EWSB) | singlet | 0 | 0 | n/a | real ✓ |
| LhMix (VVhh) | (…)²·Wbar·W, ·Z·Z | 4 | MW²/vev² (dim 0) | ✓ | n/a | 0 | 0 | mass basis | singlet | 0 | 0 | n/a | real ✓ |
| LhMix (ffh) | (…)·fbar·f | 4 | Mf/vev (dim 0) | ✓ | n/a | 0 | 0 | mass basis | shared Colour (quarks) | 0 | 0 | n/a | real ✓ |
| LVBL (cubic) | vev·φ³, vBL·φ³ | 4 | λi·vev (dim 1) | ✓ | n/a | 0 | 0 | mass basis | singlet | 0 | 0 | n/a | real ✓ |
| LVBL (quartic) | φ⁴ | 4 | λi (dim 0) | ✓ | n/a | 0 | 0 | mass basis | singlet | 0 | 0 | n/a | real ✓ |
| LNYukD | yn·LLbar[ii]·vR·Phibar[jj]·Eps[ii,jj] | 4 | yn | 0 ✓ | n/a | 0 (Eps pairs ν̄·Φ̄₂ and ē·Φ̄₁) | +1/2+0−1/2=0 ✓ | `Eps[ii,jj]`, LLbar and Phibar same conjugation type ✓ | singlet | +1−1+0=0 ✓ | ΔL=0 | n/a (no ψ^c in Eq. 2.6 first term) | `HC[yuk]` ✓ |
| LNYukM | yM·chi·CC[vRbar]·vR | 4 | yM | 0 ✓ | n/a | 0 | 0+0+0=0 | singlet | singlet | +2−1−1=0 ✓ | ΔL=2 (Majorana, intended) | **yes** — `CC[vRbar[sp,ff1]]` for the paper's ν^c_R ✓ | `HC[yuk]` ✓ |
| LhEff (gg) | Cgg·(cosa H+sina h2)·FS[G]·FS[G] | 5 | Cgg | −1 ✓ | absorbed: `Cgg = gs^2/(48 Pi^2 vev)`, dimension −1, units GeV^-1 (stated in Description) | 0 | 0 | mass basis | shared Gluon index | 0 | 0 | n/a | real ✓ |
| LhEff (γγ) | Cgaga·(cosa H+sina h2)·FS[A]·FS[A] | 5 | Cgaga | −1 ✓ | absorbed: `= -6.5 ee^2/(32 Pi^2 vev)`, dimension −1, units GeV^-1 | 0 | 0 | mass basis | singlet | 0 | 0 | n/a | real ✓ |

Free-field confirmation per new class: `Zp` → `LZpkin` ✓ in `LBSM`; `h2` → `Lh2kin` ✓ in `LBSM`; `NN` (N1,N2,N3) → `LNkin` ✓ in `LBSM`. `vR` and `chi` are `Unphysical -> True`; they carry no independent propagator (they are defined as `ProjP` combinations of `NN`/`vl` and of `h2`/`H`), so they need no separate kinetic term.

`SelfConjugate -> True` classes: `Zp`, `Bp`, `h2`, `NN` — none of them carries `QuantumNumbers` ✓. The new U(1)_{B−L} charges sit on the complex `Unphysical` classes `vR` (Y_BL = −1) and `chi` (Y_BL = +2) ✓.

Reference/cached model file read: **none**.

```json
{
  "model_name": "B-L-SM_gen",
  "info": {
    "authors": ["S. Amrith", "J. M. Butterworth", "F. F. Deppisch", "W. Liu", "A. Varma", "D. Yallup"],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["University College London"],
    "emails": ["j.butterworth@ucl.ac.uk", "f.deppisch@ucl.ac.uk"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "g1p",
      "parameter_type": "External",
      "value": "0.2",
      "block_name": "BLINPUTS",
      "order_block": 1,
      "interaction_order": ["QED", 1],
      "tex": "g_1'",
      "description": "U(1)_{B-L} gauge coupling g'_1, Eq.(2.3); benchmark Case D value 0.2, Table 1"
    },
    {
      "name": "sina",
      "parameter_type": "External",
      "value": "0.2",
      "block_name": "BLINPUTS",
      "order_block": 2,
      "tex": "s_alpha",
      "description": "Sine of the h1-h2 scalar mixing angle alpha, Eq.(2.12)-(2.13); benchmark value 0.2, Table 1"
    },
    {
      "name": "mnu",
      "parameter_type": "External",
      "value": "1.*^-10",
      "block_name": "BLINPUTS",
      "order_block": 3,
      "description": "Light neutrino mass scale 0.1 eV expressed in GeV, used for the seesaw relation VlN = Sqrt[mnu/MN], Sec.3.4"
    },
    {
      "name": "cosa",
      "parameter_type": "Internal",
      "value": "Sqrt[1 - sina^2]",
      "tex": "c_alpha",
      "description": "Cosine of the h1-h2 scalar mixing angle alpha, Eq.(2.12)"
    },
    {
      "name": "vBL",
      "parameter_type": "Internal",
      "value": "MZp/(2 g1p)",
      "interaction_order": ["QED", -1],
      "tex": "x",
      "description": "B-L breaking vacuum expectation value x = MZp/(2 g1p) [GeV], Sec.4; 17.5 TeV for the Case D benchmark"
    },
    {
      "name": "VlN",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "VlN[1]", "rhs": "Sqrt[mnu/MN1]", "delayed": false},
        {"lhs": "VlN[2]", "rhs": "Sqrt[mnu/MN2]", "delayed": false},
        {"lhs": "VlN[3]", "rhs": "Sqrt[mnu/MN3]", "delayed": false}
      ],
      "description": "Active-sterile neutrino mixing V_lN = Sin[theta_nu] = Sqrt[mnu/MN], Eq.(2.9) and Table 1"
    },
    {
      "name": "yn",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yn[1,1]", "rhs": "Sqrt[2] MN1 VlN[1]/vev", "delayed": false},
        {"lhs": "yn[2,2]", "rhs": "Sqrt[2] MN2 VlN[2]/vev", "delayed": false},
        {"lhs": "yn[3,3]", "rhs": "Sqrt[2] MN3 VlN[3]/vev", "delayed": false}
      ],
      "definitions": [
        {"lhs": "yn[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "interaction_order": ["QED", 1],
      "tex": "y^nu",
      "description": "Dirac neutrino Yukawa matrix y^nu, diagonal, y^nu_ii = Sqrt[2] MNi VlN_i/vev, Eq.(2.6) and Sec.2"
    },
    {
      "name": "yM",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yM[1,1]", "rhs": "MN1/(Sqrt[2] vBL)", "delayed": false},
        {"lhs": "yM[2,2]", "rhs": "MN2/(Sqrt[2] vBL)", "delayed": false},
        {"lhs": "yM[3,3]", "rhs": "MN3/(Sqrt[2] vBL)", "delayed": false}
      ],
      "definitions": [
        {"lhs": "yM[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "interaction_order": ["QED", 1],
      "tex": "y^M",
      "description": "Majorana Yukawa matrix y^M of the RH neutrinos to chi, diagonal, MR = Sqrt[2] y^M x, Eq.(2.6)"
    },
    {
      "name": "lam1",
      "parameter_type": "Internal",
      "value": "((MH^2 + Mh2^2) - (1 - 2 sina^2) (Mh2^2 - MH^2))/(4 vev^2)",
      "interaction_order": ["QED", 2],
      "tex": "lambda_1",
      "description": "Quartic coupling lambda_1 of the SM doublet, Eq.(2.2) and Eq.(3.1)"
    },
    {
      "name": "lam2",
      "parameter_type": "Internal",
      "value": "((MH^2 + Mh2^2) + (1 - 2 sina^2) (Mh2^2 - MH^2))/(4 vBL^2)",
      "interaction_order": ["QED", 2],
      "tex": "lambda_2",
      "description": "Quartic coupling lambda_2 of the B-L singlet chi, Eq.(2.2) and Eq.(3.1)"
    },
    {
      "name": "lam3",
      "parameter_type": "Internal",
      "value": "(2 sina cosa (Mh2^2 - MH^2))/(2 vev vBL)",
      "interaction_order": ["QED", 2],
      "tex": "lambda_3",
      "description": "Higgs portal coupling lambda_3 between H and chi, Eq.(2.2) and Eq.(3.1)"
    },
    {
      "name": "Cgg",
      "parameter_type": "Internal",
      "value": "gs^2/(48 Pi^2 vev)",
      "interaction_order": ["QCD", 2],
      "description": "Effective scalar-gluon-gluon coupling from the top loop, = gs^2/(48 Pi^2 vev), mass dimension -1, units GeV^-1, Sec.5"
    },
    {
      "name": "Cgaga",
      "parameter_type": "Internal",
      "value": "-6.5 ee^2/(32 Pi^2 vev)",
      "interaction_order": ["QED", 2],
      "description": "Effective scalar-photon-photon coupling from the W and top loops, = -6.5 ee^2/(32 Pi^2 vev), mass dimension -1, units GeV^-1, Sec.5"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7000."},
      "width": {"sym": "WZp", "value": "1."},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "B-L gauge boson Z prime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 110,
      "class_name": "Bp",
      "self_conjugate": true,
      "unphysical": true,
      "definitions": ["Bp[mu_] -> Zp[mu]"]
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "h2",
      "self_conjugate": true,
      "mass": {"sym": "Mh2", "value": "200."},
      "width": {"sym": "Wh2", "value": "1."},
      "pdg": 9900025,
      "particle_name": "h2",
      "full_name": "Heavy B-L Higgs boson h2",
      "propagator_label": "h2",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 110,
      "class_name": "chi",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0", "YBL": "2"},
      "definitions": ["chi -> (cosa h2 - sina H)/Sqrt[2]"]
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NN",
      "class_members": ["N1", "N2", "N3"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "self_conjugate": true,
      "mass": {"sym": "MN", "members": [["MN1", "1400."], ["MN2", "1400."], ["MN3", "1400."]]},
      "width": {"sym": "WN", "members": [["WN1", "0."], ["WN2", "0."], ["WN3", "0."]]},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 110,
      "class_name": "vR",
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0", "YBL": "-1", "LeptonNumber": "1"},
      "definitions": [
        "vR[sp1_, ff_] :> Module[{sp2}, ProjP[sp1, sp2] (Sqrt[1 - VlN[ff]^2] NN[sp2, ff] + VlN[ff] vl[sp2, ff])]"
      ]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LZpkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]"
    },
    {
      "name": "Lh2kin",
      "delayed": true,
      "expression": "Block[{mu}, 1/2 del[h2, mu] del[h2, mu] - 1/2 Mh2^2 h2 h2]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{mu, sp, ff}, ExpandIndices[I/2 NNbar.Ga[mu].del[NN, mu] - 1/2 MN[ff] NNbar[sp, ff].NN[sp, ff]]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-g1p Zp[mu] (1/3 (QLbar.Ga[mu].QL + uRbar.Ga[mu].uR + dRbar.Ga[mu].dR) - (LLbar.Ga[mu].LL + lRbar.Ga[mu].lR + vRbar.Ga[mu].vR)), FlavorExpand -> {SU2D}]]"
    },
    {
      "name": "LZpS",
      "delayed": true,
      "expression": "Block[{mu}, MZp^2/vBL Zp[mu] Zp[mu] (cosa h2 - sina H) + MZp^2/(2 vBL^2) Zp[mu] Zp[mu] (cosa h2 - sina H)^2]"
    },
    {
      "name": "LhMix",
      "delayed": true,
      "expression": "Block[{mu, sp, ff, cc}, ExpandIndices[2 MW^2/vev (cosa H + sina h2 - H) Wbar[mu] W[mu] + MW^2/vev^2 ((cosa H + sina h2)^2 - H^2) Wbar[mu] W[mu] + MZ^2/vev (cosa H + sina h2 - H) Z[mu] Z[mu] + MZ^2/(2 vev^2) ((cosa H + sina h2)^2 - H^2) Z[mu] Z[mu] - Ml[ff]/vev (cosa H + sina h2 - H) lbar[sp, ff].l[sp, ff] - Mu[ff]/vev (cosa H + sina h2 - H) uqbar[sp, ff, cc].uq[sp, ff, cc] - Md[ff]/vev (cosa H + sina h2 - H) dqbar[sp, ff, cc].dq[sp, ff, cc]]]"
    },
    {
      "name": "LVBL",
      "delayed": true,
      "expression": "-(lam1 vev (cosa H + sina h2)^3 + lam1/4 (cosa H + sina h2)^4 + lam2 vBL (cosa h2 - sina H)^3 + lam2/4 (cosa h2 - sina H)^4 + lam3/2 vev (cosa H + sina h2) (cosa h2 - sina H)^2 + lam3/2 vBL (cosa h2 - sina H) (cosa H + sina h2)^2 + lam3/4 (cosa H + sina h2)^2 (cosa h2 - sina H)^2) + lam vev H^3 + lam/4 H^4"
    },
    {
      "name": "LNYukD",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, ff1, ff2, yuk}, yuk = ExpandIndices[-yn[ff1, ff2] LLbar[sp, ii, ff1].vR[sp, ff2] Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LNYukM",
      "delayed": true,
      "expression": "Block[{sp, ff1, ff2, yuk}, yuk = ExpandIndices[-yM[ff1, ff2] chi CC[vRbar[sp, ff1]].vR[sp, ff2]]; yuk + HC[yuk]]"
    },
    {
      "name": "LhEff",
      "delayed": true,
      "expression": "Block[{mu, nu, aa}, ExpandIndices[Cgg (cosa H + sina h2) FS[G, mu, nu, aa] FS[G, mu, nu, aa] + Cgaga (cosa H + sina h2) FS[A, mu, nu] FS[A, mu, nu]]]"
    },
    {
      "name": "LBSM",
      "delayed": true,
      "expression": "LZpkin + Lh2kin + LNkin + LZpF + LZpS + LhMix + LVBL + LNYukD + LNYukM + LhEff"
    },
    {
      "name": "LBL",
      "delayed": true,
      "expression": "LSM + LBSM"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```
I read the paper and the schema. No cached or reference `.fr` file for this model exists in the sandbox, and none was read — only `1811.11452.txt`, `frmodel.py`, `render.py`, and `SM.fr`.

## New-physics content found in the paper

| Item | Paper source |
|---|---|
| Abelian gauge field `B'` → mass eigenstate `Z'` (real vector, singlet, Q=0, Y=0) | Eq. (2.3), (2.4) |
| Complex SM-singlet scalar `chi`, Y=0, Y_BL=+2 | Sec. 2, Eq. (2.1) |
| CP-even mass eigenstate `h2` (mixes with SM `h1=H`, angle α) | Eq. (2.11), (2.12) |
| 3 RH neutrinos `vR` (singlet, Q=0, Y=0, Y_BL=−1) → Majorana mass eigenstates N1,N2,N3 | Eq. (2.5)–(2.9) |
| B−L charges: quarks +1/3, leptons −1, H 0, chi +2, vR −1 | Sec. 2 |
| Parameters: g1', MZ', Mh2, sinα, MNi, VlN, x, λ1,2,3, yν, yM | Eq. (2.6), (2.13), (3.1), Table 1 |

**New-U(1) charge sign (rule 5).** SM.fr uses Y(Phi)=+1/2, Y(LL)=−1/2, so the Dirac neutrino Yukawa must be the "up-type" contraction `LLbar[ii] . vR Phibar[jj] Eps[ii,jj]`. Invariance of that term fixes Y_BL(vR) = Y_BL(LL) = −1, and invariance of `chi CC[vRbar].vR` then fixes Y_BL(chi) = +2, with Y_BL(H)=0. This is exactly the paper's table, so no sign flip was needed.

**Implementation choice (hard cutover, mass basis).** SM.fr's `Phi` cannot be re-declared from an add-on, so `h2` is written as a physical mass eigenstate with its own kinetic + mass term, and the gauge-eigenstate content is inserted verbatim as `cosa H + sina h2` (doublet direction) and `cosa h2 - sina H` (singlet direction). `LhMix` supplies the sinα couplings of `h2` to W/Z/fermions and the (cosα−1) correction of `H`; `LVBL` adds the λ1,2,3 self-couplings and cancels SM.fr's own `lam` cubic/quartic. No term regenerates a mass that is already declared.

## Mandatory self-audit

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | Y_BL sum | L/B sum | CC[] where ψ^c | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin (kin) | FS[Zp]·FS[Zp] | 4 | −1/4 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| LZpkin (mass) | MZp²·Zp·Zp | 4 | MZp² (dim 2) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lh2kin (kin) | del[h2]·del[h2] | 4 | 1/2 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| Lh2kin (mass) | Mh2²·h2·h2 | 4 | Mh2² (dim 2) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | self-conj ✓ |
| LNkin (kin) | NNbar·Ga·del[NN] | 4 | I/2 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 | ΔL=0 | Majorana `SelfConjugate->True` | self-conj ✓ |
| LNkin (mass) | MN·NNbar·NN | 4 | MN (dim 1) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 | ΔL=2 (Majorana, by construction) | Majorana field | self-conj ✓ |
| LZpF (quarks) | QLbar·Ga·QL·Zp etc. | 4 | g1p | 0 ✓ | n/a | 0 | 0 | shared SU2D index (singlet) | shared Colour index | +1/3−1/3=0 | 0 | n/a | self-conj ✓ |
| LZpF (leptons) | LLbar·Ga·LL·Zp, lRbar·Ga·lR·Zp, vRbar·Ga·vR·Zp | 4 | g1p | 0 ✓ | n/a | 0 | 0 | shared SU2D index | singlet | −1+1=0 | 0 | n/a | self-conj ✓ |
| LZpS (trilinear) | Zp·Zp·(cosa h2 − sina H) | 4 | MZp²/vBL (dim 1) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 (post-breaking mass basis; from \|Dχ\|², Y_BL(χ)=+2 cancels between χ and χ†) | 0 | n/a | real ✓ |
| LZpS (quartic) | Zp·Zp·(…)² | 4 | MZp²/(2 vBL²) (dim 0) | ✓ | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | real ✓ |
| LhMix (VV) | (cosa H+sina h2)·Wbar·W, ·Z·Z | 4 | MW²/vev, MZ²/vev (dim 1) | ✓ | n/a | 0 | 0 | mass basis (post-EWSB) | singlet | 0 | 0 | n/a | real ✓ |
| LhMix (VVhh) | (…)²·Wbar·W, ·Z·Z | 4 | MW²/vev² (dim 0) | ✓ | n/a | 0 | 0 | mass basis | singlet | 0 | 0 | n/a | real ✓ |
| LhMix (ffh) | (…)·fbar·f | 4 | Mf/vev (dim 0) | ✓ | n/a | 0 | 0 | mass basis | shared Colour (quarks) | 0 | 0 | n/a | real ✓ |
| LVBL (cubic) | vev·φ³, vBL·φ³ | 4 | λi·vev (dim 1) | ✓ | n/a | 0 | 0 | mass basis | singlet | 0 | 0 | n/a | real ✓ |
| LVBL (quartic) | φ⁴ | 4 | λi (dim 0) | ✓ | n/a | 0 | 0 | mass basis | singlet | 0 | 0 | n/a | real ✓ |
| LNYukD | yn·LLbar[ii]·vR·Phibar[jj]·Eps[ii,jj] | 4 | yn | 0 ✓ | n/a | 0 (Eps pairs ν̄·Φ̄₂ and ē·Φ̄₁) | +1/2+0−1/2=0 ✓ | `Eps[ii,jj]`, LLbar and Phibar same conjugation type ✓ | singlet | +1−1+0=0 ✓ | ΔL=0 | n/a (no ψ^c in Eq. 2.6 first term) | `HC[yuk]` ✓ |
| LNYukM | yM·chi·CC[vRbar]·vR | 4 | yM | 0 ✓ | n/a | 0 | 0+0+0=0 | singlet | singlet | +2−1−1=0 ✓ | ΔL=2 (Majorana, intended) | **yes** — `CC[vRbar[sp,ff1]]` for the paper's ν^c_R ✓ | `HC[yuk]` ✓ |
| LhEff (gg) | Cgg·(cosa H+sina h2)·FS[G]·FS[G] | 5 | Cgg | −1 ✓ | absorbed: `Cgg = gs^2/(48 Pi^2 vev)`, dimension −1, units GeV^-1 (stated in Description) | 0 | 0 | mass basis | shared Gluon index | 0 | 0 | n/a | real ✓ |
| LhEff (γγ) | Cgaga·(cosa H+sina h2)·FS[A]·FS[A] | 5 | Cgaga | −1 ✓ | absorbed: `= -6.5 ee^2/(32 Pi^2 vev)`, dimension −1, units GeV^-1 | 0 | 0 | mass basis | singlet | 0 | 0 | n/a | real ✓ |

Free-field confirmation per new class: `Zp` → `LZpkin` ✓ in `LBSM`; `h2` → `Lh2kin` ✓ in `LBSM`; `NN` (N1,N2,N3) → `LNkin` ✓ in `LBSM`. `vR` and `chi` are `Unphysical -> True`; they carry no independent propagator (they are defined as `ProjP` combinations of `NN`/`vl` and of `h2`/`H`), so they need no separate kinetic term.

`SelfConjugate -> True` classes: `Zp`, `Bp`, `h2`, `NN` — none of them carries `QuantumNumbers` ✓. The new U(1)_{B−L} charges sit on the complex `Unphysical` classes `vR` (Y_BL = −1) and `chi` (Y_BL = +2) ✓.

Reference/cached model file read: **none**.

```json
{
  "model_name": "B-L-SM_gen",
  "info": {
    "authors": ["S. Amrith", "J. M. Butterworth", "F. F. Deppisch", "W. Liu", "A. Varma", "D. Yallup"],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["University College London"],
    "emails": ["j.butterworth@ucl.ac.uk", "f.deppisch@ucl.ac.uk"]
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "g1p",
      "parameter_type": "External",
      "value": "0.2",
      "block_name": "BLINPUTS",
      "order_block": 1,
      "interaction_order": ["QED", 1],
      "tex": "g_1'",
      "description": "U(1)_{B-L} gauge coupling g'_1, Eq.(2.3); benchmark Case D value 0.2, Table 1"
    },
    {
      "name": "sina",
      "parameter_type": "External",
      "value": "0.2",
      "block_name": "BLINPUTS",
      "order_block": 2,
      "tex": "s_alpha",
      "description": "Sine of the h1-h2 scalar mixing angle alpha, Eq.(2.12)-(2.13); benchmark value 0.2, Table 1"
    },
    {
      "name": "mnu",
      "parameter_type": "External",
      "value": "1.*^-10",
      "block_name": "BLINPUTS",
      "order_block": 3,
      "description": "Light neutrino mass scale 0.1 eV expressed in GeV, used for the seesaw relation VlN = Sqrt[mnu/MN], Sec.3.4"
    },
    {
      "name": "cosa",
      "parameter_type": "Internal",
      "value": "Sqrt[1 - sina^2]",
      "tex": "c_alpha",
      "description": "Cosine of the h1-h2 scalar mixing angle alpha, Eq.(2.12)"
    },
    {
      "name": "vBL",
      "parameter_type": "Internal",
      "value": "MZp/(2 g1p)",
      "interaction_order": ["QED", -1],
      "tex": "x",
      "description": "B-L breaking vacuum expectation value x = MZp/(2 g1p) [GeV], Sec.4; 17.5 TeV for the Case D benchmark"
    },
    {
      "name": "VlN",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "VlN[1]", "rhs": "Sqrt[mnu/MN1]", "delayed": false},
        {"lhs": "VlN[2]", "rhs": "Sqrt[mnu/MN2]", "delayed": false},
        {"lhs": "VlN[3]", "rhs": "Sqrt[mnu/MN3]", "delayed": false}
      ],
      "description": "Active-sterile neutrino mixing V_lN = Sin[theta_nu] = Sqrt[mnu/MN], Eq.(2.9) and Table 1"
    },
    {
      "name": "yn",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yn[1,1]", "rhs": "Sqrt[2] MN1 VlN[1]/vev", "delayed": false},
        {"lhs": "yn[2,2]", "rhs": "Sqrt[2] MN2 VlN[2]/vev", "delayed": false},
        {"lhs": "yn[3,3]", "rhs": "Sqrt[2] MN3 VlN[3]/vev", "delayed": false}
      ],
      "definitions": [
        {"lhs": "yn[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "interaction_order": ["QED", 1],
      "tex": "y^nu",
      "description": "Dirac neutrino Yukawa matrix y^nu, diagonal, y^nu_ii = Sqrt[2] MNi VlN_i/vev, Eq.(2.6) and Sec.2"
    },
    {
      "name": "yM",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yM[1,1]", "rhs": "MN1/(Sqrt[2] vBL)", "delayed": false},
        {"lhs": "yM[2,2]", "rhs": "MN2/(Sqrt[2] vBL)", "delayed": false},
        {"lhs": "yM[3,3]", "rhs": "MN3/(Sqrt[2] vBL)", "delayed": false}
      ],
      "definitions": [
        {"lhs": "yM[i_?NumericQ, j_?NumericQ]", "rhs": "0 /; (i =!= j)", "delayed": true}
      ],
      "interaction_order": ["QED", 1],
      "tex": "y^M",
      "description": "Majorana Yukawa matrix y^M of the RH neutrinos to chi, diagonal, MR = Sqrt[2] y^M x, Eq.(2.6)"
    },
    {
      "name": "lam1",
      "parameter_type": "Internal",
      "value": "((MH^2 + Mh2^2) - (1 - 2 sina^2) (Mh2^2 - MH^2))/(4 vev^2)",
      "interaction_order": ["QED", 2],
      "tex": "lambda_1",
      "description": "Quartic coupling lambda_1 of the SM doublet, Eq.(2.2) and Eq.(3.1)"
    },
    {
      "name": "lam2",
      "parameter_type": "Internal",
      "value": "((MH^2 + Mh2^2) + (1 - 2 sina^2) (Mh2^2 - MH^2))/(4 vBL^2)",
      "interaction_order": ["QED", 2],
      "tex": "lambda_2",
      "description": "Quartic coupling lambda_2 of the B-L singlet chi, Eq.(2.2) and Eq.(3.1)"
    },
    {
      "name": "lam3",
      "parameter_type": "Internal",
      "value": "(2 sina cosa (Mh2^2 - MH^2))/(2 vev vBL)",
      "interaction_order": ["QED", 2],
      "tex": "lambda_3",
      "description": "Higgs portal coupling lambda_3 between H and chi, Eq.(2.2) and Eq.(3.1)"
    },
    {
      "name": "Cgg",
      "parameter_type": "Internal",
      "value": "gs^2/(48 Pi^2 vev)",
      "interaction_order": ["QCD", 2],
      "description": "Effective scalar-gluon-gluon coupling from the top loop, = gs^2/(48 Pi^2 vev), mass dimension -1, units GeV^-1, Sec.5"
    },
    {
      "name": "Cgaga",
      "parameter_type": "Internal",
      "value": "-6.5 ee^2/(32 Pi^2 vev)",
      "interaction_order": ["QED", 2],
      "description": "Effective scalar-photon-photon coupling from the W and top loops, = -6.5 ee^2/(32 Pi^2 vev), mass dimension -1, units GeV^-1, Sec.5"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7000."},
      "width": {"sym": "WZp", "value": "1."},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "B-L gauge boson Z prime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 110,
      "class_name": "Bp",
      "self_conjugate": true,
      "unphysical": true,
      "definitions": ["Bp[mu_] -> Zp[mu]"]
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "h2",
      "self_conjugate": true,
      "mass": {"sym": "Mh2", "value": "200."},
      "width": {"sym": "Wh2", "value": "1."},
      "pdg": 9900025,
      "particle_name": "h2",
      "full_name": "Heavy B-L Higgs boson h2",
      "propagator_label": "h2",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 110,
      "class_name": "chi",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0", "YBL": "2"},
      "definitions": ["chi -> (cosa h2 - sina H)/Sqrt[2]"]
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NN",
      "class_members": ["N1", "N2", "N3"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "self_conjugate": true,
      "mass": {"sym": "MN", "members": [["MN1", "1400."], ["MN2", "1400."], ["MN3", "1400."]]},
      "width": {"sym": "WN", "members": [["WN1", "0."], ["WN2", "0."], ["WN3", "0."]]},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 110,
      "class_name": "vR",
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0", "YBL": "-1", "LeptonNumber": "1"},
      "definitions": [
        "vR[sp1_, ff_] :> Module[{sp2}, ProjP[sp1, sp2] (Sqrt[1 - VlN[ff]^2] NN[sp2, ff] + VlN[ff] vl[sp2, ff])]"
      ]
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LZpkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]"
    },
    {
      "name": "Lh2kin",
      "delayed": true,
      "expression": "Block[{mu}, 1/2 del[h2, mu] del[h2, mu] - 1/2 Mh2^2 h2 h2]"
    },
    {
      "name": "LNkin",
      "delayed": true,
      "expression": "Block[{mu, sp, ff}, ExpandIndices[I/2 NNbar.Ga[mu].del[NN, mu] - 1/2 MN[ff] NNbar[sp, ff].NN[sp, ff]]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-g1p Zp[mu] (1/3 (QLbar.Ga[mu].QL + uRbar.Ga[mu].uR + dRbar.Ga[mu].dR) - (LLbar.Ga[mu].LL + lRbar.Ga[mu].lR + vRbar.Ga[mu].vR)), FlavorExpand -> {SU2D}]]"
    },
    {
      "name": "LZpS",
      "delayed": true,
      "expression": "Block[{mu}, MZp^2/vBL Zp[mu] Zp[mu] (cosa h2 - sina H) + MZp^2/(2 vBL^2) Zp[mu] Zp[mu] (cosa h2 - sina H)^2]"
    },
    {
      "name": "LhMix",
      "delayed": true,
      "expression": "Block[{mu, sp, ff, cc}, ExpandIndices[2 MW^2/vev (cosa H + sina h2 - H) Wbar[mu] W[mu] + MW^2/vev^2 ((cosa H + sina h2)^2 - H^2) Wbar[mu] W[mu] + MZ^2/vev (cosa H + sina h2 - H) Z[mu] Z[mu] + MZ^2/(2 vev^2) ((cosa H + sina h2)^2 - H^2) Z[mu] Z[mu] - Ml[ff]/vev (cosa H + sina h2 - H) lbar[sp, ff].l[sp, ff] - Mu[ff]/vev (cosa H + sina h2 - H) uqbar[sp, ff, cc].uq[sp, ff, cc] - Md[ff]/vev (cosa H + sina h2 - H) dqbar[sp, ff, cc].dq[sp, ff, cc]]]"
    },
    {
      "name": "LVBL",
      "delayed": true,
      "expression": "-(lam1 vev (cosa H + sina h2)^3 + lam1/4 (cosa H + sina h2)^4 + lam2 vBL (cosa h2 - sina H)^3 + lam2/4 (cosa h2 - sina H)^4 + lam3/2 vev (cosa H + sina h2) (cosa h2 - sina H)^2 + lam3/2 vBL (cosa h2 - sina H) (cosa H + sina h2)^2 + lam3/4 (cosa H + sina h2)^2 (cosa h2 - sina H)^2) + lam vev H^3 + lam/4 H^4"
    },
    {
      "name": "LNYukD",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, ff1, ff2, yuk}, yuk = ExpandIndices[-yn[ff1, ff2] LLbar[sp, ii, ff1].vR[sp, ff2] Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LNYukM",
      "delayed": true,
      "expression": "Block[{sp, ff1, ff2, yuk}, yuk = ExpandIndices[-yM[ff1, ff2] chi CC[vRbar[sp, ff1]].vR[sp, ff2]]; yuk + HC[yuk]]"
    },
    {
      "name": "LhEff",
      "delayed": true,
      "expression": "Block[{mu, nu, aa}, ExpandIndices[Cgg (cosa H + sina h2) FS[G, mu, nu, aa] FS[G, mu, nu, aa] + Cgaga (cosa H + sina h2) FS[A, mu, nu] FS[A, mu, nu]]]"
    },
    {
      "name": "LBSM",
      "delayed": true,
      "expression": "LZpkin + Lh2kin + LNkin + LZpF + LZpS + LhMix + LVBL + LNYukD + LNYukM + LhEff"
    },
    {
      "name": "LBL",
      "delayed": true,
      "expression": "LSM + LBSM"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```