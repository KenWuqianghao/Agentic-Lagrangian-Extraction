I read the prompt, the schema, the renderer, and the paper LaTeX source, plus `SM.fr` for conventions. No reference or cached `.fr` model file for EffLRSM exists in the sandbox, and none was read.

## Mandatory self-audit table

Numeric cross-checks used below: α(M_Z)=1/127.94, sin²θ_W=0.23126 → g²=0.4247, tan²θ_W=0.30083.

| term name | fields in the monomial | d | coupling symbol | coupling mass dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) sums | L/B sum | CC[] used | fraction/root placement checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LWRkin (kin) | FS[WRbar,mu,nu] FS[WR,mu,nu] | 4 | 1/2 (pure number) | 0 | n/a | −1+1=0 | 0 (mass-basis field, no Y declared) | singlet (no doublet) | singlet | none (no new U(1)) | 0 | n/a | n/a | self-Hermitian |
| LWRkin (mass) | WRbar[mu] WR[mu] | 2 | MWR^2 | 2 | n/a | −1+1=0 | 0 | singlet | singlet | none | 0 | n/a | n/a | self-Hermitian |
| LZRkin (kin) | FS[ZR,mu,nu] FS[ZR,mu,nu] | 4 | 1/4 | 0 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | n/a | self-Hermitian (real field) |
| LZRkin (mass) | ZR[mu] ZR[mu] | 2 | 1/2 MZR^2 | 2 | n/a | 0 | 0 | singlet | singlet | none | 0 | n/a | n/a | self-Hermitian |
| LNHkin (kin) | NHLbar.Ga[mu].del[NHL,mu] | 4 | I/2 | 0 | n/a | 0 | 0 | singlet | singlet | none | Majorana: L not defined (no QuantumNumbers) | n/a | n/a | self-Hermitian (Majorana) |
| LNHkin (mass) | NHLbar[sp,ff].NHL[sp,ff] | 3 | −1/2 MNH[ff] | 1 | n/a | 0 | 0 | singlet | singlet | none | ΔL=2 by construction (Majorana) | n/a | n/a | self-Hermitian (Majorana, −1/2 M psibar.psi) |
| LWRq | uqbar . VCKMR . Ga[mu].ProjP . dq · WR[mu] | 4 | −kapRq·gw/Sqrt[2] · VCKMR | 0 | n/a | −2/3−1/3+1=0 | 0 | singlet (mass eigenstates, no doublet) | 3̄⊗3 identity, implicit Colour contraction in the dot chain | none | B: −1/3+1/3=0 | n/a | LaTeX line 281 `\frac{-\kappa_R^q g}{\sqrt{2}}` (root in denominator); confirmed by Γ(W_R→qq̄′)=N_c κ²g²M/48π → 2×25.35=50.7 GeV = Tbl. II | HC[lag] included |
| LWRl (X piece) | bar[CC[vl]] . XLN . Ga[mu].ProjP . l · WR[mu] | 4 | −kapRl·gw/Sqrt[2] · XLN | 0 | n/a | 0−1+1=0 | 0 | singlet | singlet | none | L: −1+1=0 | yes — paper writes ν̄^c_m (Eq.5) | same Sqrt[2] as Eq.(4); benchmark X=0 (Eq.7) | HC[lag] included |
| LWRl (Y piece) | NHLbar . YLN . Ga[mu].ProjP . l · WR[mu] | 4 | −kapRl·gw/Sqrt[2] · YLN | 0 | n/a | 0−1+1=0 | 0 | singlet | singlet | none | ΔL=1 (Majorana N carries no L) | n/a (paper writes N̄_{m'}, no superscript c) | LaTeX line 293 `\frac{-\kappa_R^\ell g}{\sqrt{2}}`; Γ(W_R→ℓN)=8.41 GeV reproduced | HC[lag] included |
| LZRf (u-type) | uqbar.Ga[mu].(gLZRu ProjM+gRZRu ProjP).uq · ZR[mu] | 4 | −gw·gZRq·gLZRu, −gw·gZRq·gRZRu | 0 | n/a | −2/3+2/3+0=0 | 0 | singlet | 3̄⊗3 identity | none | 0 | n/a | LaTeX line 352: root in the DENOMINATOR, `\frac{-\kappa g}{\sqrt{1-(1/\kappa)^2\tan^2\theta_W}}`; verified with Γ(Z_R→tt̄) Eq.(14) → 11.30 GeV vs 11.3 (Tbl. II) | self-Hermitian (real ZR, real g_L,g_R) |
| LZRf (d-type) | dqbar.Ga[mu].(gLZRd ProjM+gRZRd ProjP).dq · ZR[mu] | 4 | −gw·gZRq·gLZRd, −gw·gZRq·gRZRd | 0 | n/a | 1/3−1/3=0 | 0 | singlet | 3̄⊗3 identity | none | 0 | n/a | same; 2×11.30+3×19.89 = 82.3 GeV vs 82.3 (Tbl. II) | self-Hermitian |
| LZRf (charged leptons) | lbar.Ga[mu].(gLZRe ProjM+gRZRe ProjP).l · ZR[mu] | 4 | −gw·gZRl·gLZRe, −gw·gZRl·gRZRe | 0 | n/a | 1−1=0 | 0 | singlet | singlet | none | −1+1=0 | n/a | same; 3×2.545 = 7.63 GeV vs 7.64 (Tbl. II) | self-Hermitian |
| LZRf (light nu) | vlbar.Ga[mu].(gLZRv ProjM).vl · ZR[mu] | 4 | −gw·gZRl·gLZRv | 0 | n/a | 0 | 0 | singlet | singlet | none | −1+1=0 | n/a | same; 3×0.927 = 2.78 GeV vs 2.78 (Tbl. II) | self-Hermitian |
| LZRf (heavy N) | NHLbar.Ga[mu].(gRZRn ProjP).NHL · ZR[mu] | 4 | −gw·gZRl·gRZRn (g_R^{Z_R,N}=T_R^3=1/2) | 0 | n/a | 0 | 0 | singlet | singlet | none | ΔL=2 (Majorana) | n/a | same; Γ(Z_R→N₁N₁)=10.18 GeV vs 10.2 (Tbl. II) | self-Hermitian |

Per-class kinetic + mass confirmation (rule 1): **WR** → LWRkin (complex vector form, in LTotal); **ZR** → LZRkin (real vector form, in LTotal); **NHL** → LNHkin (Majorana form `I/2 psibar.Ga.del psi − 1/2 M psibar.psi`, in LTotal). Each uses the mass symbol declared in its class (MWR, MZR, MNH[ff] with members mn1, mn2, mn3).

Non-fundamental colour representations: none. All new states are colour singlets, so no `AddGaugeRepresentation[...]` line and no colour index declaration is needed.

SelfConjugate → True classes: **ZR** and **NHL**. Both carry no `QuantumNumbers` (Q=0 for both; the Majorana NHL also carries no LeptonNumber, as lepton number is violated).

Name check (none is a Mathematica built-in, a FeynRules symbol, or an SM.fr name): classes WR, ZR, NHL with members n1, n2, n3; masses/widths MWR, MZR, MNH, mn1, mn2, mn3, WWR, WZR, WNH, Wn1, Wn2, Wn3; parameters kapRq, kapRl, tw2, gZRq, gZRl, gLZRu, gRZRu, gLZRd, gRZRd, gLZRe, gRZRe, gLZRv, gRZRn, VCKMR, YLN, XLN; terms LWRkin, LZRkin, LNHkin, LWRq, LWRl, LZRf, LTotal. Indices used: only Colour and Generation (both declared by SM.fr), so `index_decls` is empty. Particle-name strings "wr+"/"wr-"/"zr"/"n1..n3" match the paper's MG5_aMC syntax and contain no primes.

Single total Lagrangian: **LTotal** = LWRkin + LZRkin + LNHkin + LWRq + LWRl + LZRf. Every other term appears in it; no term is a pure constant; the SM part comes from SM.fr and is not re-summed here.

New U(1) charges (rule 5): the effective model adds no new U(1) gauge group; SU(2)_R × U(1)_{B−L} is integrated out and only W_R, Z_R survive in the mass basis, so every new-U(1) column is "none". Hypercharge is not a good quantum number for these operators (they are written after EWSB in terms of physical mass eigenstates, exactly as Eqs.(4),(5),(8) of the paper), so the Y sums are trivially zero; electric charge Q is conserved in every term. Mass mixing (rule 8): the paper states W_R, Z_R are "aligned with their mass eigenstates" and N_i "aligned with the RH chiral states"; the only mixing retained is ν–N mixing, kept explicitly as the External matrices XLN (light) and YLN (heavy) of Eq.(5) with the benchmark of Eq.(7), and the W_R^3–X_{B−L} mixing already absorbed into the tan²θ_W terms of g_L^{Z_R,f}, g_R^{Z_R,f}. The LRSM scalar sector is deliberately absent — the paper decouples it at 15–20 TeV (Sec. II C).

Reference/cached model file read: **none**.

```json
{
  "model_name": "EffLRSM_gen",
  "info": {
    "authors": ["O. Mattelaer", "M. Mitra", "R. Ruiz"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": ["Universite catholique de Louvain (CP3)", "IISER Mohali", "IPPP Durham University"],
    "emails": ["olivier.mattelaer@uclouvain.be", "manimala@iisermohali.ac.in", "richard.ruiz@durham.ac.uk"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "kapRq",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "kappa_R^q: overall real normalization of the W_R and Z_R coupling strength to quarks, Eq.(4) and Eq.(8)"
    },
    {
      "name": "kapRl",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "LRSMINPUTS",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "kappa_R^l: overall real normalization of the W_R and Z_R coupling strength to leptons, Eq.(5) and Eq.(8)"
    },
    {
      "name": "tw2",
      "parameter_type": "Internal",
      "value": "sw^2/cw^2",
      "description": "tan^2(theta_W), the SM weak mixing combination entering the Z_R chiral couplings, Eqs.(8)-(10)"
    },
    {
      "name": "gZRq",
      "parameter_type": "Internal",
      "value": "kapRq/Sqrt[1 - tw2/kapRq^2]",
      "interaction_order": ["NP", 1],
      "description": "Z_R coupling normalization for quarks: kappa_R^q/Sqrt[1-(1/kappa_R^q)^2 tan^2(theta_W)], denominator root as in Eq.(8)"
    },
    {
      "name": "gZRl",
      "parameter_type": "Internal",
      "value": "kapRl/Sqrt[1 - tw2/kapRl^2]",
      "interaction_order": ["NP", 1],
      "description": "Z_R coupling normalization for leptons: kappa_R^l/Sqrt[1-(1/kappa_R^l)^2 tan^2(theta_W)], denominator root as in Eq.(8)"
    },
    {
      "name": "gLZRu",
      "parameter_type": "Internal",
      "value": "(1/2 - 2/3)*tw2/kapRq^2",
      "description": "g_L^{Z_R,u} = (T_L^3 - Q) tan^2(theta_W)/kappa_R^q^2 for up-type quarks, Eq.(9)"
    },
    {
      "name": "gRZRu",
      "parameter_type": "Internal",
      "value": "1/2 - (2/3)*tw2/kapRq^2",
      "description": "g_R^{Z_R,u} = T_R^3 - Q tan^2(theta_W)/kappa_R^q^2 for up-type quarks, Eq.(10)"
    },
    {
      "name": "gLZRd",
      "parameter_type": "Internal",
      "value": "(-1/2 + 1/3)*tw2/kapRq^2",
      "description": "g_L^{Z_R,d} = (T_L^3 - Q) tan^2(theta_W)/kappa_R^q^2 for down-type quarks, Eq.(9)"
    },
    {
      "name": "gRZRd",
      "parameter_type": "Internal",
      "value": "-1/2 + (1/3)*tw2/kapRq^2",
      "description": "g_R^{Z_R,d} = T_R^3 - Q tan^2(theta_W)/kappa_R^q^2 for down-type quarks, Eq.(10)"
    },
    {
      "name": "gLZRe",
      "parameter_type": "Internal",
      "value": "(-1/2 + 1)*tw2/kapRl^2",
      "description": "g_L^{Z_R,e} = (T_L^3 - Q) tan^2(theta_W)/kappa_R^l^2 for charged leptons, Eq.(9)"
    },
    {
      "name": "gRZRe",
      "parameter_type": "Internal",
      "value": "-1/2 + tw2/kapRl^2",
      "description": "g_R^{Z_R,e} = T_R^3 - Q tan^2(theta_W)/kappa_R^l^2 for charged leptons, Eq.(10)"
    },
    {
      "name": "gLZRv",
      "parameter_type": "Internal",
      "value": "(1/2)*tw2/kapRl^2",
      "description": "g_L^{Z_R,nu} = (T_L^3 - Q) tan^2(theta_W)/kappa_R^l^2 for the LH light neutrinos (Q=0), Eq.(9)"
    },
    {
      "name": "gRZRn",
      "parameter_type": "Internal",
      "value": "1/2",
      "description": "g_R^{Z_R,N} = T_R^3 = 1/2 for the heavy Majorana neutrinos (Q=0), Eq.(10) and Tbl. I"
    },
    {
      "name": "VCKMR",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "RCKMBLOCK",
      "value_rules": [
        {"lhs": "VCKMR[1,1]", "rhs": "1."},
        {"lhs": "VCKMR[1,2]", "rhs": "0."},
        {"lhs": "VCKMR[1,3]", "rhs": "0."},
        {"lhs": "VCKMR[2,1]", "rhs": "0."},
        {"lhs": "VCKMR[2,2]", "rhs": "1."},
        {"lhs": "VCKMR[2,3]", "rhs": "0."},
        {"lhs": "VCKMR[3,1]", "rhs": "0."},
        {"lhs": "VCKMR[3,2]", "rhs": "0."},
        {"lhs": "VCKMR[3,3]", "rhs": "1."}
      ],
      "description": "Right-handed CKM matrix V^{CKM'} of Eq.(4); taken diagonal with unit entries in this study"
    },
    {
      "name": "YLN",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "RNUMIXING",
      "value_rules": [
        {"lhs": "YLN[1,1]", "rhs": "1."},
        {"lhs": "YLN[1,2]", "rhs": "0."},
        {"lhs": "YLN[1,3]", "rhs": "0."},
        {"lhs": "YLN[2,1]", "rhs": "0."},
        {"lhs": "YLN[2,2]", "rhs": "1."},
        {"lhs": "YLN[2,3]", "rhs": "0."},
        {"lhs": "YLN[3,1]", "rhs": "0."},
        {"lhs": "YLN[3,2]", "rhs": "0."},
        {"lhs": "YLN[3,3]", "rhs": "1."}
      ],
      "description": "Heavy-neutrino mixing Y of Eq.(5), stored in matrix-chain order YLN[m',l] = Y_{l m'}; benchmark |Y_eN1|=|Y_muN2|=|Y_tauN3|=1, Eq.(7)"
    },
    {
      "name": "XLN",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "LNUMIXING",
      "value_rules": [
        {"lhs": "XLN[1,1]", "rhs": "0."},
        {"lhs": "XLN[1,2]", "rhs": "0."},
        {"lhs": "XLN[1,3]", "rhs": "0."},
        {"lhs": "XLN[2,1]", "rhs": "0."},
        {"lhs": "XLN[2,2]", "rhs": "0."},
        {"lhs": "XLN[2,3]", "rhs": "0."},
        {"lhs": "XLN[3,1]", "rhs": "0."},
        {"lhs": "XLN[3,2]", "rhs": "0."},
        {"lhs": "XLN[3,3]", "rhs": "0."}
      ],
      "description": "Light-neutrino mixing X of Eq.(5), stored in matrix-chain order XLN[m,l] = X_{l m}; benchmark |X_{lm}|=0, Eq.(7)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "WR",
      "self_conjugate": false,
      "mass": {"sym": "MWR", "value": "3000."},
      "width": {"sym": "WWR", "value": "84.3"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9900024,
      "particle_name": "wr+",
      "antiparticle_name": "wr-",
      "full_name": "WR",
      "propagator_label": "WR",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "ZR",
      "self_conjugate": true,
      "mass": {"sym": "MZR", "value": "5070."},
      "width": {"sym": "WZR", "value": "114."},
      "quantum_numbers": {},
      "pdg": 9900023,
      "particle_name": "zr",
      "full_name": "ZR",
      "propagator_label": "ZR",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "NHL",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["n1", "n2", "n3"],
      "mass": {"sym": "MNH", "members": [["mn1", "173.3"], ["mn2", "1.*^12"], ["mn3", "1.*^12"]]},
      "width": {"sym": "WNH", "members": [["Wn1", "2.12*^-8"], ["Wn2", "1."], ["Wn3", "1."]]},
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["NHL", "n1", "n2", "n3"],
      "propagator_type": "S",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LWRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, ExpandIndices[-1/2 FS[WRbar, mu, nu] FS[WR, mu, nu] + MWR^2 WRbar[mu] WR[mu]]]"
    },
    {
      "name": "LZRkin",
      "delayed": true,
      "expression": "Block[{mu, nu}, ExpandIndices[-1/4 FS[ZR, mu, nu] FS[ZR, mu, nu] + 1/2 MZR^2 ZR[mu] ZR[mu]]]"
    },
    {
      "name": "LNHkin",
      "delayed": true,
      "expression": "Block[{mu, sp, ff}, ExpandIndices[I/2 NHLbar.Ga[mu].del[NHL, mu] - 1/2 MNH[ff] NHLbar[sp, ff].NHL[sp, ff]]]"
    },
    {
      "name": "LWRq",
      "delayed": true,
      "expression": "Block[{mu, lag}, lag = ExpandIndices[-kapRq*gw/Sqrt[2]*(uqbar.VCKMR.Ga[mu].ProjP.dq)*WR[mu]]; lag + HC[lag]]"
    },
    {
      "name": "LWRl",
      "delayed": true,
      "expression": "Block[{mu, lag}, lag = ExpandIndices[-kapRl*gw/Sqrt[2]*(bar[CC[vl]].XLN.Ga[mu].ProjP.l + NHLbar.YLN.Ga[mu].ProjP.l)*WR[mu]]; lag + HC[lag]]"
    },
    {
      "name": "LZRf",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gw*gZRq*(uqbar.Ga[mu].(gLZRu*ProjM + gRZRu*ProjP).uq + dqbar.Ga[mu].(gLZRd*ProjM + gRZRd*ProjP).dq)*ZR[mu] - gw*gZRl*(lbar.Ga[mu].(gLZRe*ProjM + gRZRe*ProjP).l + vlbar.Ga[mu].(gLZRv*ProjM).vl + NHLbar.Ga[mu].(gRZRn*ProjP).NHL)*ZR[mu]]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LWRkin + LZRkin + LNHkin + LWRq + LWRl + LZRf"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```