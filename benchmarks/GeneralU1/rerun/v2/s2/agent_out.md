I'll start by reading the paper and the schema files.
I read the paper, the schema, the renderer, and `SM.fr`. Nothing else — **no cached or reference `.fr` file for this model was read** (the paper cites one in Ref. [49]; I did not open it, and none exists in the sandbox).

## Model content found (Sec. II, Table I, Eqs. 1–9)

Gauge group `SU(3)c x SU(2)L x U(1)Y x U(1)X`. New states: the `U(1)X` gauge boson `Z'`, three RH neutrinos `N^i_R` (Majorana after `U(1)X` breaking), and one SM-singlet complex scalar `Phi` (real scalar `phiX` + Goldstone `GZp`).

**U(1)X charge sign (rule 5).** Eq. (1) writes `-Y_u qL H uR - Y_d qL H~ dR`, which needs `Y(H) = -1/2`, i.e. the paper's `H` is `SM.fr`'s `Phibar`. Table I instead gives `Y(H) = +1/2`. I re-derived `x(H)` from all five Yukawas in `SM.fr` conventions (`Phi` with `Y = +1/2`):

| term (SM.fr form) | condition |
|---|---|
| `QLbar.dR Phi` | `x(Phi) = xH/2` |
| `QLbar.uR Phibar Eps` | `x(Phi) = xH/2` |
| `LLbar.lR Phi` | `x(Phi) = xH/2` |
| `LLbar.NR Phibar Eps` | `x(Phi) = xH/2` |
| `Phi_X Nbar^c N` | `x(chix) = 2 xPhi` |

All five agree: **`x(Phi_SM.fr) = +xH/2`**, exactly Table I's entry. So Table I is consistent with `SM.fr`; only Eq. (1)'s `H`/`H~` placement is swapped. I use `+xH/2`.

I do **not** declare a `U(1)X` gauge group: `SM.fr`'s fields carry no `X` quantum number, so `DC[]` could never produce their `Z'` couplings. Eq. (6) is written explicitly instead, and `gauge_groups` is `[]` as the schema rule requires.

## Mandatory self-audit table

X-charges: `xQL=xH/6+xPhi/3`, `xuR=2xH/3+xPhi/3`, `xdR=-xH/3+xPhi/3`, `xLL=-xH/2-xPhi`, `xlR=-xH-xPhi`, `xNR=-xPhi`, `xHd=xH/2`, `xPhis=2xPhi`.

| term | fields in monomial | d | coupling | coupling dim (= 4-d) | 1/Lambda^(d-4) | Q sum | Y sum | SU(2) | SU(3) | U(1)X sum | L number | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin | `FS[Zp]FS[Zp]` (2+2) | 4 | `-1/4` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (Zp neutral) | 0 | n/a | self-conjugate |
| LchiKin | `del[chixbar] del[chix]`; `gX Zp chixbar chix`; `gX^2 Zp Zp chixbar chix` | 4 | `1`, `gX`, `gX^2` | 0 ✓ | n/a | 0 | 0+0 | singlet | singlet | `-xPhis+xPhis = 0` ✓ | 0 | n/a | manifestly real |
| LchiPot | `muX^2 chixbar chix` | 2 | `muX^2` | 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 ✓ | 0 | n/a | real |
| LchiPot | `lamX (chixbar chix)^2` | 4 | `lamX` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 ✓ | 0 | n/a | real |
| LchiPot | `lamHX Phibar[ii]Phi[ii] chixbar chix` | 4 | `lamHX` | 0 ✓ | n/a | 0 | `-1/2+1/2` = 0 | shared `ii` | singlet | 0 ✓ | 0 | n/a | real |
| LZpHiggs | `gX Zp (Phibar[ii] DC[Phi[ii]] - h.c.)` | 4 | `gX xHd` | 0 ✓ | n/a | 0 | `-1/2+1/2` = 0 | shared `ii` | singlet | `-xHd+xHd = 0` ✓ | 0 | n/a | explicit `- h.c.` inside |
| LZpHiggs | `gX^2 Zp Zp Phibar[ii]Phi[ii]` | 4 | `gX^2 xHd^2` | 0 ✓ | n/a | 0 | 0 | shared `ii` | singlet | 0 ✓ | 0 | n/a | real |
| LNKin | `I/2 vRbar.Ga.del[vR]` | 4 | `1/2` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (Majorana) | — | n/a | self-conjugate |
| LZpF (`QL`) | `gX Zp QLbar.Ga.QL` | 4 | `gX xQL` | 0 ✓ | n/a | 0 | `-1/6+1/6` = 0 | shared `ii` | shared `cc` | `-xQL+xQL` = 0 ✓ | 0 | n/a | real current |
| LZpF (`uR`) | `gX Zp uRbar.Ga.uR` | 4 | `gX xuR` | 0 ✓ | n/a | 0 | `-2/3+2/3` = 0 | singlet | shared `cc` | 0 ✓ | 0 | n/a | real current |
| LZpF (`dR`) | `gX Zp dRbar.Ga.dR` | 4 | `gX xdR` | 0 ✓ | n/a | 0 | `1/3-1/3` = 0 | singlet | shared `cc` | 0 ✓ | 0 | n/a | real current |
| LZpF (`LL`) | `gX Zp LLbar.Ga.LL` | 4 | `gX xLL` | 0 ✓ | n/a | 0 | `1/2-1/2` = 0 | shared `ii` | singlet | 0 ✓ | 0 | n/a | real current |
| LZpF (`lR`) | `gX Zp lRbar.Ga.lR` | 4 | `gX xlR` | 0 ✓ | n/a | 0 | `1-1` = 0 | singlet | singlet | 0 ✓ | 0 | n/a | real current |
| LZpF (`NR`) | `gX Zp NRbar.Ga.NR` | 4 | `gX xNR` | 0 ✓ | n/a | 0 | `0+0` = 0 | singlet | singlet | 0 ✓ | 0 | n/a | real current |
| LnuYuk | `ynu LLbar.NR Phibar[jj] Eps[ii,jj]` | 4 | `ynu` | 0 ✓ | n/a | 0 | `1/2+0-1/2` = 0 | `Eps[ii,jj]`, two anti-doublets ✓ | singlet | `-xLL+xNR-xHd` = `xH/2+xPhi-xPhi-xH/2` = 0 ✓ | `-1+1` = 0 | n/a (no `psi^c`) | `HC[yuk]` |
| LNYuk | `yN chix CC[NRbar].NR` | 4 | `yN` | 0 ✓ | n/a | 0 | `0+0+0` = 0 | singlet | singlet | `xPhis + xNR + xNR` = `2xPhi-xPhi-xPhi` = 0 ✓ | `-2` (Majorana, L violated by design) | **yes** (`N^{ac}_R N^a_R`) | `HC[yuk]` |

Free-field rows (one per new class, all inside `LU1X`, which is added to `LSM` in `LTot`):

| class | kinetic term | mass term | check |
|---|---|---|---|
| `Zp` (V[100]) | `LZpKin` | `LchiKin` + `LZpHiggs` at the vevs give `MZp^2 = gX^2 (4 xPhi^2 vevX^2 + xH^2 vev^2/4)` — **exactly Eq. (4)** | ✓ no hand-written mass, which would double-count the Higgs mechanism |
| `phix` (S[100]) | `LchiKin` | `LchiPot` → `Mphix = Sqrt[2 lamX] vevX` | ✓ |
| `GZp` (S[101]) | `LchiKin` | `Mass -> {MZp, 7500.}` (Feynman gauge, as `SM.fr` does for `G0`) | ✓ |
| `vR` (F[100]) | `LNKin` | `LNYuk` at `<chix>` → `MN_i = yN[i] vevX/Sqrt[2]` — **exactly the paper's `m_N = Y_N v_Phi/Sqrt[2]`** | ✓ |

`SelfConjugate -> True` classes: `Zp`, `phix`, `GZp`, `vR` — **none carries `QuantumNumbers`**. The chiral `X`/`Y` bookkeeping sits on the Unphysical classes `NR` and `chix`; the `X` charges themselves are `xH`-dependent parameters, so they enter the Lagrangian as couplings rather than as numeric `QuantumNumbers`.

Reference/cached model file read: **none**.

No cutoff parameters: every operator has `d = 4`, so no `1/Lambda^n` factor is needed anywhere. No new index is used, so `index_decls` is empty (`Generation`, `SU2D`, `SU2W`, `Colour` come from `SM.fr`).

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["Arindam Das", "P. S. Bhupal Dev", "Yutaka Hosotani", "Sanjoy Mandal"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": [
      "Kyungpook National University / Hokkaido University",
      "Washington University in St. Louis",
      "Osaka University",
      "IFIC, CSIC/Universitat de Valencia"
    ],
    "emails": ["arindamdas@oia.hokudai.ac.jp", "bdev@wustl.edu", "hosotani@het.phys.sci.osaka-u.ac.jp", "smandal@ific.uv.es"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "feynman_gauge": true,
  "vevs": [["Phi[2]", "vev"], ["chix", "vevX"]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "U1XINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g'",
      "description": "U(1)_X gauge coupling g', Sec. II; benchmark 0.4 for MZp = 7.5 TeV"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "U1XINPUTS",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)_X charge parameter x_H of the SM Higgs doublet, Table I; benchmarks -2, -1, -0.5, 0, 0.5, 1, 2; x_H = 0 is the B-L case"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "U1XINPUTS",
      "order_block": 3,
      "tex": "x_\\Phi",
      "description": "U(1)_X charge parameter x_Phi of the SM-singlet scalar, Table I; fixed to 1 in the paper"
    },
    {
      "name": "lamX",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "U1XINPUTS",
      "order_block": 4,
      "tex": "\\lambda_\\Phi",
      "description": "Quartic coupling lambda_Phi of the U(1)_X scalar Phi, Eq.(2)"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.001",
      "block_name": "U1XINPUTS",
      "order_block": 5,
      "tex": "\\lambda'",
      "description": "H-Phi portal coupling lambda', Eq.(2); small, so H-Phi mixing is negligible"
    },
    {
      "name": "mD",
      "parameter_type": "External",
      "value": "1.*^-3",
      "block_name": "U1XINPUTS",
      "order_block": 6,
      "tex": "m_D",
      "description": "Dirac neutrino mass scale m_D = Y_nu v/Sqrt[2] in GeV, Eq.(1) and Eq.(5); seesaw benchmark giving m_nu near 0.1 eV for m_N = 10 TeV"
    },
    {
      "name": "vevX",
      "parameter_type": "Internal",
      "value": "Sqrt[MZp^2/gX^2 - xH^2 vev^2/4]/(2 xPhi)",
      "tex": "v_\\Phi",
      "description": "U(1)_X breaking VEV v_Phi, inverted from the Z' mass relation Eq.(4)"
    },
    {
      "name": "muX",
      "parameter_type": "Internal",
      "value": "Sqrt[vevX^2 lamX]",
      "tex": "\\mu_\\Phi",
      "description": "Quadratic coefficient of the Phi potential, Eq.(2), fixed by the minimum condition"
    },
    {
      "name": "Mphix",
      "parameter_type": "Internal",
      "value": "Sqrt[2 lamX] vevX",
      "tex": "m_\\varphi",
      "description": "Mass of the U(1)_X scalar phi, from the potential of Eq.(2)"
    },
    {
      "name": "xQL",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)_X charge of the left-handed quark doublet q_L, Table I"
    },
    {
      "name": "xuR",
      "parameter_type": "Internal",
      "value": "2 xH/3 + xPhi/3",
      "description": "U(1)_X charge of the right-handed up-type quark u_R, Table I"
    },
    {
      "name": "xdR",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)_X charge of the right-handed down-type quark d_R, Table I"
    },
    {
      "name": "xLL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)_X charge of the left-handed lepton doublet l_L, Table I"
    },
    {
      "name": "xlR",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)_X charge of the right-handed charged lepton e_R, Table I"
    },
    {
      "name": "xNR",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)_X charge of the right-handed neutrino N_R, Table I"
    },
    {
      "name": "xHd",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)_X charge of the SM Higgs doublet in SM.fr conventions (Y = +1/2), Table I; sign fixed by requiring all five Yukawa terms of Eq.(1) to be U(1)_X invariant"
    },
    {
      "name": "xPhis",
      "parameter_type": "Internal",
      "value": "2 xPhi",
      "description": "U(1)_X charge of the SM-singlet scalar Phi, Table I"
    },
    {
      "name": "WZp",
      "parameter_type": "Internal",
      "value": "MZp gX^2/(24 Pi) (18 xQL^2 + 9 xuR^2 + 9 xdR^2 + 6 xLL^2 + 3 xlR^2)",
      "tex": "\\Gamma_{Z'}",
      "description": "Total Z' width summed over three generations of SM fermions, Eqs.(7) and (8); the N N mode is closed because m_N > MZp"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "yN[1]", "rhs": "Sqrt[2] MN1/vevX"},
        {"lhs": "yN[2]", "rhs": "Sqrt[2] MN2/vevX"},
        {"lhs": "yN[3]", "rhs": "Sqrt[2] MN3/vevX"}
      ],
      "interaction_order": ["QED", 1],
      "tex": "Y_N",
      "description": "Majorana Yukawa couplings Y_N of the RHNs to Phi, Eq.(1); m_N = Y_N v_Phi/Sqrt[2]"
    },
    {
      "name": "ynu",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "ynu[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "ynu[1,1]", "rhs": "Sqrt[2] mD/vev"},
        {"lhs": "ynu[2,2]", "rhs": "Sqrt[2] mD/vev"},
        {"lhs": "ynu[3,3]", "rhs": "Sqrt[2] mD/vev"}
      ],
      "interaction_order": ["QED", 1],
      "tex": "Y_\\nu",
      "description": "Dirac neutrino Yukawa couplings Y_nu of Eq.(1); m_D = Y_nu v/Sqrt[2]"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "Internal"},
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
      "class_name": "phix",
      "self_conjugate": true,
      "mass": {"sym": "Mphix", "value": "Internal"},
      "width": {"sym": "Wphix", "value": "100."},
      "pdg": 9900025,
      "particle_name": "phiX",
      "full_name": "U1X-Higgs",
      "propagator_label": "phiX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "GZp",
      "self_conjugate": true,
      "goldstone": "Zp",
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "Internal"},
      "pdg": 9900250,
      "particle_name": "GZp",
      "full_name": "GZp",
      "propagator_label": "GZp",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "chix",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0"},
      "definitions": ["chix -> (vevX + phix + I GZp)/Sqrt[2]"]
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "vR",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["vR1", "vR2", "vR3"],
      "mass": {"sym": "MN", "members": [["MN1", "10000."], ["MN2", "10000."], ["MN3", "10000."]]},
      "width": {"massless": true},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["RH-neutrino-1", "RH-neutrino-2", "RH-neutrino-3"],
      "propagator_label": ["vR", "N1", "N2", "N3"],
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
      "definitions": ["NR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] vR[sp2,ff]]"]
    }
  ],
  "gauge_xi": [
    ["V[100]", "GaugeXi[Zp]"],
    ["S[100]", "1"],
    ["S[101]", "GaugeXi[Zp]"]
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu, nu}, ExpandIndices[-1/4 FS[Zp, mu, nu] FS[Zp, mu, nu]]]"
    },
    {
      "name": "LchiKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[(del[chixbar, mu] + I gX xPhis Zp[mu] chixbar) (del[chix, mu] - I gX xPhis Zp[mu] chix)]]"
    },
    {
      "name": "LchiPot",
      "delayed": true,
      "expression": "Block[{ii}, ExpandIndices[muX^2 chixbar chix - lamX chixbar chix chixbar chix - lamHX Phibar[ii] Phi[ii] chixbar chix, FlavorExpand -> SU2D]]"
    },
    {
      "name": "LZpHiggs",
      "delayed": true,
      "expression": "Block[{ii, mu}, ExpandIndices[I gX xHd Zp[mu] (Phibar[ii] DC[Phi[ii], mu] - DC[Phibar[ii], mu] Phi[ii]) + gX^2 xHd^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii], FlavorExpand -> {SU2D, SU2W}]]"
    },
    {
      "name": "LNKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I/2 vRbar.Ga[mu].del[vR, mu]]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gX Zp[mu] (xQL QLbar.Ga[mu].QL + xuR uRbar.Ga[mu].uR + xdR dRbar.Ga[mu].dR + xLL LLbar.Ga[mu].LL + xlR lRbar.Ga[mu].lR + xNR NRbar.Ga[mu].NR), FlavorExpand -> {SU2D}]]"
    },
    {
      "name": "LnuYuk",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, ff1, ff2, yuk}, yuk = -ynu[ff1, ff2] LLbar[sp, ii, ff1].NR[sp, ff2] Phibar[jj] Eps[ii, jj]; ExpandIndices[yuk + HC[yuk], FlavorExpand -> SU2D]]"
    },
    {
      "name": "LNYuk",
      "delayed": true,
      "expression": "Block[{sp, ff, yuk}, yuk = -1/2 yN[ff] chix CC[NRbar[sp, ff]].NR[sp, ff]; ExpandIndices[yuk + HC[yuk]]]"
    },
    {
      "name": "LU1X",
      "delayed": true,
      "expression": "LZpKin + LchiKin + LchiPot + LZpHiggs + LNKin + LZpF + LnuYuk + LNYuk"
    },
    {
      "name": "LTot",
      "delayed": true,
      "expression": "LSM + LU1X"
    }
  ]
}
```
I read the paper, the schema, the renderer, and `SM.fr`. Nothing else — **no cached or reference `.fr` file for this model was read** (the paper cites one in Ref. [49]; I did not open it, and none exists in the sandbox).

## Model content found (Sec. II, Table I, Eqs. 1–9)

Gauge group `SU(3)c x SU(2)L x U(1)Y x U(1)X`. New states: the `U(1)X` gauge boson `Z'`, three RH neutrinos `N^i_R` (Majorana after `U(1)X` breaking), and one SM-singlet complex scalar `Phi` (real scalar `phiX` + Goldstone `GZp`).

**U(1)X charge sign (rule 5).** Eq. (1) writes `-Y_u qL H uR - Y_d qL H~ dR`, which needs `Y(H) = -1/2`, i.e. the paper's `H` is `SM.fr`'s `Phibar`. Table I instead gives `Y(H) = +1/2`. I re-derived `x(H)` from all five Yukawas in `SM.fr` conventions (`Phi` with `Y = +1/2`):

| term (SM.fr form) | condition |
|---|---|
| `QLbar.dR Phi` | `x(Phi) = xH/2` |
| `QLbar.uR Phibar Eps` | `x(Phi) = xH/2` |
| `LLbar.lR Phi` | `x(Phi) = xH/2` |
| `LLbar.NR Phibar Eps` | `x(Phi) = xH/2` |
| `Phi_X Nbar^c N` | `x(chix) = 2 xPhi` |

All five agree: **`x(Phi_SM.fr) = +xH/2`**, exactly Table I's entry. So Table I is consistent with `SM.fr`; only Eq. (1)'s `H`/`H~` placement is swapped. I use `+xH/2`.

I do **not** declare a `U(1)X` gauge group: `SM.fr`'s fields carry no `X` quantum number, so `DC[]` could never produce their `Z'` couplings. Eq. (6) is written explicitly instead, and `gauge_groups` is `[]` as the schema rule requires.

## Mandatory self-audit table

X-charges: `xQL=xH/6+xPhi/3`, `xuR=2xH/3+xPhi/3`, `xdR=-xH/3+xPhi/3`, `xLL=-xH/2-xPhi`, `xlR=-xH-xPhi`, `xNR=-xPhi`, `xHd=xH/2`, `xPhis=2xPhi`.

| term | fields in monomial | d | coupling | coupling dim (= 4-d) | 1/Lambda^(d-4) | Q sum | Y sum | SU(2) | SU(3) | U(1)X sum | L number | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin | `FS[Zp]FS[Zp]` (2+2) | 4 | `-1/4` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (Zp neutral) | 0 | n/a | self-conjugate |
| LchiKin | `del[chixbar] del[chix]`; `gX Zp chixbar chix`; `gX^2 Zp Zp chixbar chix` | 4 | `1`, `gX`, `gX^2` | 0 ✓ | n/a | 0 | 0+0 | singlet | singlet | `-xPhis+xPhis = 0` ✓ | 0 | n/a | manifestly real |
| LchiPot | `muX^2 chixbar chix` | 2 | `muX^2` | 2 ✓ | n/a | 0 | 0 | singlet | singlet | 0 ✓ | 0 | n/a | real |
| LchiPot | `lamX (chixbar chix)^2` | 4 | `lamX` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 ✓ | 0 | n/a | real |
| LchiPot | `lamHX Phibar[ii]Phi[ii] chixbar chix` | 4 | `lamHX` | 0 ✓ | n/a | 0 | `-1/2+1/2` = 0 | shared `ii` | singlet | 0 ✓ | 0 | n/a | real |
| LZpHiggs | `gX Zp (Phibar[ii] DC[Phi[ii]] - h.c.)` | 4 | `gX xHd` | 0 ✓ | n/a | 0 | `-1/2+1/2` = 0 | shared `ii` | singlet | `-xHd+xHd = 0` ✓ | 0 | n/a | explicit `- h.c.` inside |
| LZpHiggs | `gX^2 Zp Zp Phibar[ii]Phi[ii]` | 4 | `gX^2 xHd^2` | 0 ✓ | n/a | 0 | 0 | shared `ii` | singlet | 0 ✓ | 0 | n/a | real |
| LNKin | `I/2 vRbar.Ga.del[vR]` | 4 | `1/2` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | 0 (Majorana) | — | n/a | self-conjugate |
| LZpF (`QL`) | `gX Zp QLbar.Ga.QL` | 4 | `gX xQL` | 0 ✓ | n/a | 0 | `-1/6+1/6` = 0 | shared `ii` | shared `cc` | `-xQL+xQL` = 0 ✓ | 0 | n/a | real current |
| LZpF (`uR`) | `gX Zp uRbar.Ga.uR` | 4 | `gX xuR` | 0 ✓ | n/a | 0 | `-2/3+2/3` = 0 | singlet | shared `cc` | 0 ✓ | 0 | n/a | real current |
| LZpF (`dR`) | `gX Zp dRbar.Ga.dR` | 4 | `gX xdR` | 0 ✓ | n/a | 0 | `1/3-1/3` = 0 | singlet | shared `cc` | 0 ✓ | 0 | n/a | real current |
| LZpF (`LL`) | `gX Zp LLbar.Ga.LL` | 4 | `gX xLL` | 0 ✓ | n/a | 0 | `1/2-1/2` = 0 | shared `ii` | singlet | 0 ✓ | 0 | n/a | real current |
| LZpF (`lR`) | `gX Zp lRbar.Ga.lR` | 4 | `gX xlR` | 0 ✓ | n/a | 0 | `1-1` = 0 | singlet | singlet | 0 ✓ | 0 | n/a | real current |
| LZpF (`NR`) | `gX Zp NRbar.Ga.NR` | 4 | `gX xNR` | 0 ✓ | n/a | 0 | `0+0` = 0 | singlet | singlet | 0 ✓ | 0 | n/a | real current |
| LnuYuk | `ynu LLbar.NR Phibar[jj] Eps[ii,jj]` | 4 | `ynu` | 0 ✓ | n/a | 0 | `1/2+0-1/2` = 0 | `Eps[ii,jj]`, two anti-doublets ✓ | singlet | `-xLL+xNR-xHd` = `xH/2+xPhi-xPhi-xH/2` = 0 ✓ | `-1+1` = 0 | n/a (no `psi^c`) | `HC[yuk]` |
| LNYuk | `yN chix CC[NRbar].NR` | 4 | `yN` | 0 ✓ | n/a | 0 | `0+0+0` = 0 | singlet | singlet | `xPhis + xNR + xNR` = `2xPhi-xPhi-xPhi` = 0 ✓ | `-2` (Majorana, L violated by design) | **yes** (`N^{ac}_R N^a_R`) | `HC[yuk]` |

Free-field rows (one per new class, all inside `LU1X`, which is added to `LSM` in `LTot`):

| class | kinetic term | mass term | check |
|---|---|---|---|
| `Zp` (V[100]) | `LZpKin` | `LchiKin` + `LZpHiggs` at the vevs give `MZp^2 = gX^2 (4 xPhi^2 vevX^2 + xH^2 vev^2/4)` — **exactly Eq. (4)** | ✓ no hand-written mass, which would double-count the Higgs mechanism |
| `phix` (S[100]) | `LchiKin` | `LchiPot` → `Mphix = Sqrt[2 lamX] vevX` | ✓ |
| `GZp` (S[101]) | `LchiKin` | `Mass -> {MZp, 7500.}` (Feynman gauge, as `SM.fr` does for `G0`) | ✓ |
| `vR` (F[100]) | `LNKin` | `LNYuk` at `<chix>` → `MN_i = yN[i] vevX/Sqrt[2]` — **exactly the paper's `m_N = Y_N v_Phi/Sqrt[2]`** | ✓ |

`SelfConjugate -> True` classes: `Zp`, `phix`, `GZp`, `vR` — **none carries `QuantumNumbers`**. The chiral `X`/`Y` bookkeeping sits on the Unphysical classes `NR` and `chix`; the `X` charges themselves are `xH`-dependent parameters, so they enter the Lagrangian as couplings rather than as numeric `QuantumNumbers`.

Reference/cached model file read: **none**.

No cutoff parameters: every operator has `d = 4`, so no `1/Lambda^n` factor is needed anywhere. No new index is used, so `index_decls` is empty (`Generation`, `SU2D`, `SU2W`, `Colour` come from `SM.fr`).

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["Arindam Das", "P. S. Bhupal Dev", "Yutaka Hosotani", "Sanjoy Mandal"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": [
      "Kyungpook National University / Hokkaido University",
      "Washington University in St. Louis",
      "Osaka University",
      "IFIC, CSIC/Universitat de Valencia"
    ],
    "emails": ["arindamdas@oia.hokudai.ac.jp", "bdev@wustl.edu", "hosotani@het.phys.sci.osaka-u.ac.jp", "smandal@ific.uv.es"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "feynman_gauge": true,
  "vevs": [["Phi[2]", "vev"], ["chix", "vevX"]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "U1XINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "tex": "g'",
      "description": "U(1)_X gauge coupling g', Sec. II; benchmark 0.4 for MZp = 7.5 TeV"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "U1XINPUTS",
      "order_block": 2,
      "tex": "x_H",
      "description": "U(1)_X charge parameter x_H of the SM Higgs doublet, Table I; benchmarks -2, -1, -0.5, 0, 0.5, 1, 2; x_H = 0 is the B-L case"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "U1XINPUTS",
      "order_block": 3,
      "tex": "x_\\Phi",
      "description": "U(1)_X charge parameter x_Phi of the SM-singlet scalar, Table I; fixed to 1 in the paper"
    },
    {
      "name": "lamX",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "U1XINPUTS",
      "order_block": 4,
      "tex": "\\lambda_\\Phi",
      "description": "Quartic coupling lambda_Phi of the U(1)_X scalar Phi, Eq.(2)"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.001",
      "block_name": "U1XINPUTS",
      "order_block": 5,
      "tex": "\\lambda'",
      "description": "H-Phi portal coupling lambda', Eq.(2); small, so H-Phi mixing is negligible"
    },
    {
      "name": "mD",
      "parameter_type": "External",
      "value": "1.*^-3",
      "block_name": "U1XINPUTS",
      "order_block": 6,
      "tex": "m_D",
      "description": "Dirac neutrino mass scale m_D = Y_nu v/Sqrt[2] in GeV, Eq.(1) and Eq.(5); seesaw benchmark giving m_nu near 0.1 eV for m_N = 10 TeV"
    },
    {
      "name": "vevX",
      "parameter_type": "Internal",
      "value": "Sqrt[MZp^2/gX^2 - xH^2 vev^2/4]/(2 xPhi)",
      "tex": "v_\\Phi",
      "description": "U(1)_X breaking VEV v_Phi, inverted from the Z' mass relation Eq.(4)"
    },
    {
      "name": "muX",
      "parameter_type": "Internal",
      "value": "Sqrt[vevX^2 lamX]",
      "tex": "\\mu_\\Phi",
      "description": "Quadratic coefficient of the Phi potential, Eq.(2), fixed by the minimum condition"
    },
    {
      "name": "Mphix",
      "parameter_type": "Internal",
      "value": "Sqrt[2 lamX] vevX",
      "tex": "m_\\varphi",
      "description": "Mass of the U(1)_X scalar phi, from the potential of Eq.(2)"
    },
    {
      "name": "xQL",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)_X charge of the left-handed quark doublet q_L, Table I"
    },
    {
      "name": "xuR",
      "parameter_type": "Internal",
      "value": "2 xH/3 + xPhi/3",
      "description": "U(1)_X charge of the right-handed up-type quark u_R, Table I"
    },
    {
      "name": "xdR",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)_X charge of the right-handed down-type quark d_R, Table I"
    },
    {
      "name": "xLL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)_X charge of the left-handed lepton doublet l_L, Table I"
    },
    {
      "name": "xlR",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)_X charge of the right-handed charged lepton e_R, Table I"
    },
    {
      "name": "xNR",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)_X charge of the right-handed neutrino N_R, Table I"
    },
    {
      "name": "xHd",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)_X charge of the SM Higgs doublet in SM.fr conventions (Y = +1/2), Table I; sign fixed by requiring all five Yukawa terms of Eq.(1) to be U(1)_X invariant"
    },
    {
      "name": "xPhis",
      "parameter_type": "Internal",
      "value": "2 xPhi",
      "description": "U(1)_X charge of the SM-singlet scalar Phi, Table I"
    },
    {
      "name": "WZp",
      "parameter_type": "Internal",
      "value": "MZp gX^2/(24 Pi) (18 xQL^2 + 9 xuR^2 + 9 xdR^2 + 6 xLL^2 + 3 xlR^2)",
      "tex": "\\Gamma_{Z'}",
      "description": "Total Z' width summed over three generations of SM fermions, Eqs.(7) and (8); the N N mode is closed because m_N > MZp"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "yN[1]", "rhs": "Sqrt[2] MN1/vevX"},
        {"lhs": "yN[2]", "rhs": "Sqrt[2] MN2/vevX"},
        {"lhs": "yN[3]", "rhs": "Sqrt[2] MN3/vevX"}
      ],
      "interaction_order": ["QED", 1],
      "tex": "Y_N",
      "description": "Majorana Yukawa couplings Y_N of the RHNs to Phi, Eq.(1); m_N = Y_N v_Phi/Sqrt[2]"
    },
    {
      "name": "ynu",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "definitions": [
        {"lhs": "ynu[i_?NumericQ, j_?NumericQ]", "rhs": "0  /; (i =!= j)", "delayed": true}
      ],
      "value_rules": [
        {"lhs": "ynu[1,1]", "rhs": "Sqrt[2] mD/vev"},
        {"lhs": "ynu[2,2]", "rhs": "Sqrt[2] mD/vev"},
        {"lhs": "ynu[3,3]", "rhs": "Sqrt[2] mD/vev"}
      ],
      "interaction_order": ["QED", 1],
      "tex": "Y_\\nu",
      "description": "Dirac neutrino Yukawa couplings Y_nu of Eq.(1); m_D = Y_nu v/Sqrt[2]"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "Internal"},
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
      "class_name": "phix",
      "self_conjugate": true,
      "mass": {"sym": "Mphix", "value": "Internal"},
      "width": {"sym": "Wphix", "value": "100."},
      "pdg": 9900025,
      "particle_name": "phiX",
      "full_name": "U1X-Higgs",
      "propagator_label": "phiX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "GZp",
      "self_conjugate": true,
      "goldstone": "Zp",
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "Internal"},
      "pdg": 9900250,
      "particle_name": "GZp",
      "full_name": "GZp",
      "propagator_label": "GZp",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "chix",
      "self_conjugate": false,
      "unphysical": true,
      "quantum_numbers": {"Y": "0"},
      "definitions": ["chix -> (vevX + phix + I GZp)/Sqrt[2]"]
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "vR",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["vR1", "vR2", "vR3"],
      "mass": {"sym": "MN", "members": [["MN1", "10000."], ["MN2", "10000."], ["MN3", "10000."]]},
      "width": {"massless": true},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["N1", "N2", "N3"],
      "full_name": ["RH-neutrino-1", "RH-neutrino-2", "RH-neutrino-3"],
      "propagator_label": ["vR", "N1", "N2", "N3"],
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
      "definitions": ["NR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] vR[sp2,ff]]"]
    }
  ],
  "gauge_xi": [
    ["V[100]", "GaugeXi[Zp]"],
    ["S[100]", "1"],
    ["S[101]", "GaugeXi[Zp]"]
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu, nu}, ExpandIndices[-1/4 FS[Zp, mu, nu] FS[Zp, mu, nu]]]"
    },
    {
      "name": "LchiKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[(del[chixbar, mu] + I gX xPhis Zp[mu] chixbar) (del[chix, mu] - I gX xPhis Zp[mu] chix)]]"
    },
    {
      "name": "LchiPot",
      "delayed": true,
      "expression": "Block[{ii}, ExpandIndices[muX^2 chixbar chix - lamX chixbar chix chixbar chix - lamHX Phibar[ii] Phi[ii] chixbar chix, FlavorExpand -> SU2D]]"
    },
    {
      "name": "LZpHiggs",
      "delayed": true,
      "expression": "Block[{ii, mu}, ExpandIndices[I gX xHd Zp[mu] (Phibar[ii] DC[Phi[ii], mu] - DC[Phibar[ii], mu] Phi[ii]) + gX^2 xHd^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii], FlavorExpand -> {SU2D, SU2W}]]"
    },
    {
      "name": "LNKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I/2 vRbar.Ga[mu].del[vR, mu]]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gX Zp[mu] (xQL QLbar.Ga[mu].QL + xuR uRbar.Ga[mu].uR + xdR dRbar.Ga[mu].dR + xLL LLbar.Ga[mu].LL + xlR lRbar.Ga[mu].lR + xNR NRbar.Ga[mu].NR), FlavorExpand -> {SU2D}]]"
    },
    {
      "name": "LnuYuk",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, ff1, ff2, yuk}, yuk = -ynu[ff1, ff2] LLbar[sp, ii, ff1].NR[sp, ff2] Phibar[jj] Eps[ii, jj]; ExpandIndices[yuk + HC[yuk], FlavorExpand -> SU2D]]"
    },
    {
      "name": "LNYuk",
      "delayed": true,
      "expression": "Block[{sp, ff, yuk}, yuk = -1/2 yN[ff] chix CC[NRbar[sp, ff]].NR[sp, ff]; ExpandIndices[yuk + HC[yuk]]]"
    },
    {
      "name": "LU1X",
      "delayed": true,
      "expression": "LZpKin + LchiKin + LchiPot + LZpHiggs + LNKin + LZpF + LnuYuk + LNYuk"
    },
    {
      "name": "LTot",
      "delayed": true,
      "expression": "LSM + LU1X"
    }
  ]
}
```