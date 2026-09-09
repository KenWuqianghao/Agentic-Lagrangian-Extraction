## Self-audit table

Model: minimal $U(1)_X$ extension (arXiv:2104.10902). New states: $Z'$ (real vector), 3 Majorana RHNs, 1 real singlet scalar. `xH = 2`, `xPhi = 1`, `gpX = 0.4`, `MZp = 7500.` are the paper's benchmark (Sec. II B, Fig. 8). `vX = MZp/(2 gpX xPhi) = 9375.`

**U(1)_X charge re-derivation (rule 5).** The paper's Table I lists $Y(H)=+1/2$, but its Yukawa Eq. (LYk) uses `H` for the up-type quark and for the Dirac neutrino, and `H~` for down-type and charged leptons. That is the opposite of SM.fr, where `Phi` has `Y = +1/2` and couples as `QLbar.dR Phi`, `LLbar.lR Phi`, `QLbar.uR Phibar Eps`. The paper's `H` is therefore SM.fr's `Phibar`. Its tabulated charge $-x_H/2$ belongs to `Phibar`, so the SM.fr doublet `Phi` carries **X = +xH/2** (sign flipped from the table). All fermion charges of Table I are kept unchanged. Check: $X = x_H Y + x_\Phi (B-L)$ with SM.fr hypercharges reproduces every table entry and gives $X(\mathrm{Phi}) = +x_H/2$. Invariance holds for all four Yukawas: (a) $-x_Q+x_d+X_\Phi=0$, (b) $-x_Q+x_u-X_\Phi=0$, (c) $-x_L+x_e+X_\Phi=0$, (d) $-x_L+x_N-X_\Phi=0$, (e) $X_S+2x_N=0 \Rightarrow X_S = 2x_\Phi$.

| term | fields in monomial | d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | U(1)_X sum | L/B | CC[] | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin | FS[Zp]FS[Zp] | 4 | 1 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | n/a | self-conjugate |
| LZpKin | Zp Zp | 2 | MZp^2 | 2 | n/a | 0 | 0 | singlet | singlet | broken (Higgsed by Phi_X) | n/a | n/a | tex L170 `\sqrt{4 v_\Phi^2+\frac14 x_H^2v^2}` (root over whole bracket) → vX=9375. | self-conjugate |
| LSXKin | del[SX] del[SX] | 4 | 1/2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | n/a | self-conjugate |
| LSXKin | SX SX | 2 | MSX^2/2 | 2 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | n/a | self-conjugate |
| LNhKin | Nhbar Ga del Nh | 4 | I/2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | Majorana class | n/a | self-conjugate |
| LNhKin | MNh[ff] Nhbar[ff].Nh[ff] | 3 | −1/2 MNh | 1 | n/a | 0 | 0 | singlet | singlet | broken; symmetric phase $X_S+2x_N=0$ | ΔL=2 (Majorana, intended) | n/a (SelfConjugate → True) | tex L172 `m_{N_\alpha}=\frac{Y^\alpha_N}{\sqrt2}v_\Phi` (√2 in denominator) | self-conjugate |
| LZpSX | SX Zp Zp | 3 | gpX^2 qXSX^2 vX | 1 | n/a | 0 | 0 | singlet | singlet | 0 (broken phase) | n/a | n/a | from `|D_mu Phi_X|^2`, cross-checked against L170 M_Zp | self-conjugate |
| LZpSX | SX SX Zp Zp | 4 | gpX^2 qXSX^2/2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | same | self-conjugate |
| LSXSelf | SX^3 | 3 | −lamX vX | 1 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | tex L159 `\lambda_\Phi(\Phi^\dag\Phi)^2` | self-conjugate |
| LSXSelf | SX^4 | 4 | −lamX/4 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | same | self-conjugate |
| LPortal | (Phibar[ii]Phi[ii]−vev^2/2) SX^2 | 3 and 4 | −lamHX/2 (× vev for the cubic) | 1 / 0 | n/a | 0 | −1/2+1/2=0 | shared index `ii` (Phibar[ii] Phi[ii]) | singlet | 0 | n/a | n/a | tex L159 `\lambda^\prime(H^\dag H)(\Phi^\dag\Phi)` | self-conjugate |
| LZpF (QL) | Zp QLbar Ga QL | 4 | −gpX qXQL | 0 | n/a | 0 | −1/6+1/6=0 | shared SU2D index | 3bar×3 | −x_Q+x_Q=0 | 0 | n/a | Table I L102 `\frac16 x_H+\frac13 x_\Phi` | self-conjugate current |
| LZpF (uR) | Zp uRbar Ga uR | 4 | −gpX qXuR | 0 | n/a | 0 | 0 | singlet | 3bar×3 | 0 | 0 | n/a | Table I L102 | self-conjugate |
| LZpF (dR) | Zp dRbar Ga dR | 4 | −gpX qXdR | 0 | n/a | 0 | 0 | singlet | 3bar×3 | 0 | 0 | n/a | Table I L102 | self-conjugate |
| LZpF (LL) | Zp LLbar Ga LL | 4 | −gpX qXLL | 0 | n/a | 0 | 0 | shared SU2D index | singlet | 0 | 0 | n/a | Table I L102 | self-conjugate |
| LZpF (lR) | Zp lRbar Ga lR | 4 | −gpX qXeR | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Table I L102 | self-conjugate |
| LZpF (Nh) | Zp Nhbar Ga ProjP Nh | 4 | −gpX qXNR | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | Majorana class | Eq. (2N) L211 `g_R^N` (right-handed current only) | self-conjugate |
| LNYuk | yNu LLbar.Nh Phibar Eps | 4 | yNu | 0 | n/a | 0 (Eps pairs ν̄·Phibar[2] and ℓ̄⁺·Phibar[1]) | +1/2+0−1/2=0 | `Eps[ii,jj]`: LLbar[sp,ii,ff1] with Phibar[jj] (same conjugation type) | singlet | −x_L+x_N−X_Phi=0 | ΔL=0 at this vertex | n/a | tex L172 `m_D=\frac{Y_\nu}{\sqrt2}v` | `HC[yuk]` added |
| LNSX | yN SX Nhbar.Nh | 4 | −yN/(2 Sqrt[2]) | 0 | n/a | 0 | 0 | singlet | singlet | symmetric phase: $X_S+2x_N = 2x_\Phi-2x_\Phi = 0$ | ΔL=2 (Majorana) | n/a — see note | tex L172 `\frac{Y^\alpha_N}{\sqrt2}v_\Phi` fixes the 1/(2√2) | operator is Hermitian (real diagonal yN); no HC to avoid double counting |

**CC[] note (rule 3).** The paper writes `Phi \overline{N_R^{\alpha c}} N_R^\alpha`. The heavy neutrino class `Nh` is declared `SelfConjugate -> True`, so `\overline{N_R^c} N_R + h.c. = Nhbar.Nh` exactly. The charge conjugation is carried by the Majorana class, not dropped, so no `CC[...]` wrapper is needed. No term keeps a paper conjugation with the conjugation removed.

**Per-particle free-field check.** `Zp` → LZpKin (kinetic + `1/2 MZp^2 Zp Zp`), in LTotal. `SX` → LSXKin (kinetic + `1/2 MSX^2 SX^2`), in LTotal. `Nh` → LNhKin (`I/2` kinetic + `-1/2 MNh[ff] Nhbar[ff].Nh[ff]`, Majorana normalisation), in LTotal. Every mass symbol is the one declared in that class `Mass -> {M, value}`.

**Non-fundamental colour representations.** None. Every new field is a colour singlet, so no `AddGaugeRepresentation` line and no `index_decls` entry are needed. Only `Colour`, `Generation`, `SU2D` are used, all declared by SM.fr.

**SelfConjugate -> True classes:** `Zp`, `Nh`, `SX`. All three carry no `QuantumNumbers`. All three are electrically neutral, colour singlets and SU(2) singlets. The $U(1)_X$ charges are not static numbers (they depend on the continuous parameter `xH`), so they are declared as parameters `qXQL, qXuR, qXdR, qXLL, qXeR, qXNR, qXH, qXSX`, not as `QuantumNumbers`.

**Name check.** Classes `Zp, Nh, SX`; members `nh1, nh2, nh3`; parameters `gpX, xH, xPhi, vX, lamHX, lamX, yNu, yN, qXQL, qXuR, qXdR, qXLL, qXeR, qXNR, qXH, qXSX`; masses/widths `MZp, WZp, MNh, MNh1..3, WNh, WNh1..3, MSX, WSX`; indices used: `Colour, Generation, SU2D` only. None is a Mathematica built-in (`N, C, D, E, I, K, O, HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM`), none is a FeynRules symbol, and none is declared by SM.fr. No primes or punctuation in any `ParticleName`. All class indices are 100 or more.

**Total Lagrangian.** One total, `LTotal`, sums: `LZpKin + LSXKin + LNhKin + LZpSX + LSXSelf + LPortal + LZpF + LNYuk + LNSX`. Every other term appears exactly once. No term is a pure constant (the `vev^2/2` subtraction in LPortal removes the field-free piece).

**Two modelling limits taken from the paper, stated openly.**
1. The paper neglects $Z$–$Z'$ mass mixing ($M_{Z'} \simeq 2 g' v_\Phi$, L170) and lists no $Z' \to Zh$ width (Eqs. 2f, 2v, 2N). The $Z'$ coupling to the SM Higgs doublet is therefore not written, so no $Z$–$Z'$ two-point vertex is produced.
2. The paper works in the small-$\lambda'$ limit where $H$–$\Phi$ mixing is negligible (L161). `lamHX` default is `0.`, and the $\lambda' v_\Phi \phi (H^\dagger H)$ piece that would give the $h$–$\phi$ bilinear is not written. Only the four-field portal operator is kept.
3. The seesaw diagonalisation (Eq. num, L180) is left implicit: `LNYuk` supplies $m_D$ directly. SM.fr fixes `vl` as a physical massless field, and the paper's collider analysis does not use the light-heavy mixing angle ($m_D/m_N \sim 7\cdot10^{-8}$ at this benchmark).

**Reference or cached model file read: none.** The paper cites its own FeynRules file at ref. `[U1X]` (tex L412). No such file exists in the sandbox and none was opened. Only the paper source, `frmodel.py`, `render.py` and `SM.fr` were read.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["A. Das", "P. S. B. Dev", "Y. Hosotani", "S. Mandal"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": ["Hokkaido University", "Washington University in St. Louis", "Osaka University", "IFIC Valencia"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gpX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "U1X",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "U(1)_X gauge coupling g' ; paper benchmark g' = 0.4 for M_Zp = 7.5 TeV, Sec. II B"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "2.",
      "block_name": "U1X",
      "order_block": 2,
      "description": "U(1)_X charge parameter x_H of Table I ; benchmark x_H = 2 (all SM chiralities couple to Zp)"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "U1X",
      "order_block": 3,
      "description": "U(1)_X charge parameter x_Phi of Table I ; fixed to 1 in the paper without loss of generality"
    },
    {
      "name": "vX",
      "parameter_type": "External",
      "value": "9375.",
      "block_name": "U1X",
      "order_block": 4,
      "interaction_order": ["NP", -1],
      "description": "U(1)_X VEV v_Phi [GeV] ; M_Zp = 2 gpX xPhi vX = 7500 GeV, Eq. below Eq.(LYk)"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "U1X",
      "order_block": 5,
      "interaction_order": ["NP", 2],
      "description": "Higgs portal quartic lambda' of the scalar potential ; the paper works in the small lambda' limit where H-Phi mixing is negligible, so the default is 0"
    },
    {
      "name": "yNu",
      "parameter_type": "External",
      "block_name": "YUKNU",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "yNu[1,1]", "rhs": "4.1*^-6"},
        {"lhs": "yNu[1,2]", "rhs": "0"},
        {"lhs": "yNu[1,3]", "rhs": "0"},
        {"lhs": "yNu[2,1]", "rhs": "0"},
        {"lhs": "yNu[2,2]", "rhs": "4.1*^-6"},
        {"lhs": "yNu[2,3]", "rhs": "0"},
        {"lhs": "yNu[3,1]", "rhs": "0"},
        {"lhs": "yNu[3,2]", "rhs": "0"},
        {"lhs": "yNu[3,3]", "rhs": "4.1*^-6"}
      ],
      "description": "Dirac neutrino Yukawa Y_nu of Eq.(LYk) ; m_D = yNu v/Sqrt[2], set for seesaw light masses near 0.05 eV with m_N = 10 TeV"
    },
    {
      "name": "yN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "yN[1,1]", "rhs": "Sqrt[2]*MNh1/vX"},
        {"lhs": "yN[1,2]", "rhs": "0"},
        {"lhs": "yN[1,3]", "rhs": "0"},
        {"lhs": "yN[2,1]", "rhs": "0"},
        {"lhs": "yN[2,2]", "rhs": "Sqrt[2]*MNh2/vX"},
        {"lhs": "yN[2,3]", "rhs": "0"},
        {"lhs": "yN[3,1]", "rhs": "0"},
        {"lhs": "yN[3,2]", "rhs": "0"},
        {"lhs": "yN[3,3]", "rhs": "Sqrt[2]*MNh3/vX"}
      ],
      "description": "Majorana Yukawa Y_N of Eq.(LYk) ; the paper gives m_N = Y_N v_Phi/Sqrt[2], so yN = Sqrt[2] MNh/vX"
    },
    {
      "name": "lamX",
      "parameter_type": "Internal",
      "value": "MSX^2/(2*vX^2)",
      "interaction_order": ["NP", 2],
      "description": "U(1)_X singlet quartic lambda_Phi of the scalar potential ; MSX^2 = 2 lamX vX^2"
    },
    {
      "name": "qXQL",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)_X charge of the SM quark doublet q_L, Table I"
    },
    {
      "name": "qXuR",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "description": "U(1)_X charge of u_R, Table I"
    },
    {
      "name": "qXdR",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)_X charge of d_R, Table I"
    },
    {
      "name": "qXLL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)_X charge of the SM lepton doublet l_L, Table I"
    },
    {
      "name": "qXeR",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)_X charge of e_R, Table I"
    },
    {
      "name": "qXNR",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)_X charge of the right-handed neutrino N_R, Table I"
    },
    {
      "name": "qXH",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)_X charge of the SM Higgs doublet Phi in SM.fr conventions (Y = +1/2). Re-derived from Yukawa invariance: the paper's H in Eq.(LYk) is SM.fr's Phibar, so the tabulated -xH/2 belongs to Phibar and Phi carries +xH/2. Check: X = xH Y + xPhi (B-L)"
    },
    {
      "name": "qXSX",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "description": "U(1)_X charge of the SM-singlet scalar Phi_X, Table I ; fixed by X_S + 2 qXNR = 0"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "1257."},
      "quantum_numbers": {},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "U1X gauge boson Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "Nh",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["nh1", "nh2", "nh3"],
      "mass": {"sym": "MNh", "members": [["MNh1", "10000."], ["MNh2", "10000."], ["MNh3", "10000."]]},
      "width": {"sym": "WNh", "members": [["WNh1", "1."], ["WNh2", "1."], ["WNh3", "1."]]},
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["nh1", "nh2", "nh3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["Nh", "nh1", "nh2", "nh3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "SX",
      "self_conjugate": true,
      "mass": {"sym": "MSX", "value": "1000."},
      "width": {"sym": "WSX", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9900025,
      "particle_name": "sx",
      "full_name": "U1X singlet scalar",
      "propagator_label": "SX",
      "propagator_type": "D",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "-1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]"
    },
    {
      "name": "LSXKin",
      "delayed": true,
      "expression": "1/2 del[SX, mu] del[SX, mu] - 1/2 MSX^2 SX^2"
    },
    {
      "name": "LNhKin",
      "delayed": true,
      "expression": "Block[{mu, ff}, ExpandIndices[I/2 Nhbar.Ga[mu].del[Nh, mu] - 1/2 MNh[ff] Nhbar[ff].Nh[ff]]]"
    },
    {
      "name": "LZpSX",
      "delayed": true,
      "expression": "Block[{mu}, gpX^2 qXSX^2 vX SX Zp[mu] Zp[mu] + 1/2 gpX^2 qXSX^2 SX^2 Zp[mu] Zp[mu]]"
    },
    {
      "name": "LSXSelf",
      "delayed": true,
      "expression": "-lamX vX SX^3 - lamX/4 SX^4"
    },
    {
      "name": "LPortal",
      "delayed": true,
      "expression": "Block[{ii}, ExpandIndices[-lamHX/2 (Phibar[ii] Phi[ii] - vev^2/2) SX^2, FlavorExpand -> SU2D]]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gpX Zp[mu] (qXQL QLbar.Ga[mu].QL + qXuR uRbar.Ga[mu].uR + qXdR dRbar.Ga[mu].dR + qXLL LLbar.Ga[mu].LL + qXeR lRbar.Ga[mu].lR + qXNR Nhbar.Ga[mu].ProjP.Nh), FlavorExpand -> SU2D] /. {CKM[a_, b_] Conjugate[CKM[a_, c_]] -> IndexDelta[b, c], CKM[b_, a_] Conjugate[CKM[c_, a_]] -> IndexDelta[b, c]}]"
    },
    {
      "name": "LNYuk",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, ff1, ff2, yuk}, yuk = ExpandIndices[-yNu[ff1, ff2] LLbar[sp, ii, ff1].Nh[sp, ff2] Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LNSX",
      "delayed": true,
      "expression": "Block[{sp, ff1, ff2}, ExpandIndices[-1/(2 Sqrt[2]) yN[ff1, ff2] SX Nhbar[sp, ff1].Nh[sp, ff2]]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LZpKin + LSXKin + LNhKin + LZpSX + LSXSelf + LPortal + LZpF + LNYuk + LNSX"
    }
  ]
}
```