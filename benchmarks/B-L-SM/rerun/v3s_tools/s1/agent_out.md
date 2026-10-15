## Self-audit (produced before the model, per the mandatory rules)

**Particle content identified from the paper (Sec. 2):** an Abelian gauge boson `Zp` ($B'_\mu$, real vector, SM-gauge singlet, $Q=Y=0$, new charge $Y_{B-L}=0$ for the boson itself), a complex SM-singlet scalar `chi` ($Y_{B-L}=+2$) whose real part mixes with the SM Higgs into two mass eigenstates ($h_1\equiv$ SM `H`, and a new physical `h2` with mass $M_{H_2}$/mixing $\sin\alpha$), an eaten Goldstone `GZp`, and three generations of right-handed/Majorana neutrinos `HN_i` ($Y_{B-L}=-1$ before symmetry breaking). Reference/cached `.fr` files: **none read** — only the paper's `.tex` source, `frmodel.py`, and `SM.fr` were opened, as instructed (rule 6).

**Hypercharge/BL-charge convention used:** SM.fr's own $Y(\Phi)=+1/2$, $Y(LL)=-1/2$, $Y(QL)=+1/6$ conventions are kept unchanged; the paper's $Y_{B-L}$ assignments (quarks $+1/3$, leptons $-1$, $\chi$: $+2$, $\nu_R$: $-1$) are consistent with these and require no re-derivation of SM hypercharges (unlike models with a shifted $H$-hypercharge convention).

**Fraction/root placements**, all read literally from the `\frac{...}{...}`/`\sqrt{...}` LaTeX source (authoritative, rule 7): Eq. (2.9) seesaw relations, Eq. (2.11) $\tan(2\alpha)=\lambda_3 vx/(\lambda_2x^2-\lambda_1v^2)$, Eq. (3.1) $\lambda_{1,2,3}$ quartic-coupling formulas, Eq. (Higgs mass) $M^2_{h_{1(2)}}$. These feed directly into the Internal parameters `xBL`, `CA`, `lamX`, `lamHX`, `muX2` below.

**No EFT operator / cutoff appears in this paper** (all new terms are renormalizable, $d=4$); rule 2 is n/a throughout.

| term | fields | d | coupling | coupling dim (4-d) | 1/Λ | Q sum | Y sum | SU(2) | SU(3) | ΣY_BL | L/B | CC[] | frac/root check | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LZpKin` | Zp,Zp (+FS,FS) | 4 | — | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj. |
| `LScalarBL` (χ kinetic+potential incl. portal) | chi,chibar,Phi,Phibar | 4 | lamX,lamHX,muX2 | 0 | n/a | 0 | 0 (Phibar[ii]Phi[ii] shared-index singlet) | singlet | singlet | 0 (chibar χ) | 0 | n/a | Eq.(2.2),(3.1), \frac/\sqrt read from tex | self-conj. |
| `LHNKin` (HN kinetic+mass+axial Zp coupling) | HN,HN,Zp | 4 | gp, MHN | 0 | n/a | n/a (self-conj.) | n/a | singlet | singlet | n/a (self-conj., rule 5) | n/a | n/a | n/a | self-conj. |
| `LZpFermions` (SM current × Zp) | uq,dq,l,vl (×2 each)+Zp | 4 | gp | 0 | n/a | 0 | 0 | singlet(post-EWSB) | singlet | 0 (e.g. $-1/3-1/3+0$ etc., or $+1+1+0$ for leptons w/ overall sign) | 0 | n/a | n/a | self-conj. |
| `LYukNu` (Dirac ν Yukawa) | LLbar,HNR,Phibar | 4 | yv | 0 | n/a | 0 (Eps[ii,jj] singlet picks Q=0 component) | Y: $+1/2-1/2+0=0$ | Eps[ii,jj] contraction (opposite-conj. types) | 0 | +1 (see note) | n/a | Eq.(2.5) | HC[yuk] |
| `LYukNMaj` (Majorana Yukawa) | bar[CC[HNR]],HNR,chi | 4 | yM | 0 | n/a | 0 | 0 | singlet | singlet | $-1-1+2=0$ | violated by 2 (Majorana) | **yes**, `bar[CC[HNR]]` used per rule 3 | Eq.(2.5) | HC[yukM] |
| `LTotal` | sums all six terms above | — | — | — | — | — | — | — | — | — | — | — | — | is the declared total |

Notes on flagged cells: LYukNu lepton-number bookkeeping — $L(LL)=+1$, $L(HNR)=0$ (sterile), so this term explicitly breaks lepton number only through the Majorana term (as physically required for seesaw); this is intentional and matches the paper. `SelfConjugate -> True` classes with **no** `QuantumNumbers`: `Zp`, `h2`, `GZp`, `HN` — confirmed. Names checked against the forbidden list and against every SM.fr-declared symbol (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,B,Wi,vl,l,uq,dq,LL,lR,QL,uR,dR,CKM,cabi,yl,yu,yd,lam,muH,...`): `Zp, h2, GZp, chi, HN, HNR, gp, SA, mnu, xBL, CA, lamX, lamHX, muX2, yv, yM, DCBL` — no collisions. Single declared total: `LTotal := LZpKin + LScalarBL + LHNKin + LZpFermions + LYukNu + LYukNMaj`. `h2`/`GZp` free kinetic+mass terms are supplied by `LScalarBL` via the mixing `Definitions` of Unphysical `chi` (rule 8), not by a separate duplicate term, to avoid double-counting the `H`-sector kinetic term already present in `SM.fr`'s `LHiggs`.

```json
{
  "model_name": "B-L-SM_gen",
  "info": {
    "authors": ["GitNexus benchmark extraction"],
    "version": "1.0",
    "date": "2026-09-17",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [["chi", "xBL"]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gp",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "BLINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "U(1)_B-L gauge coupling g_1', Eq.(2.3)"
    },
    {
      "name": "SA",
      "parameter_type": "External",
      "value": "0.2",
      "block_name": "BLINPUTS",
      "order_block": 2,
      "description": "Higgs mixing angle sin(alpha), Eq.(2.10)-(2.11)"
    },
    {
      "name": "mnu",
      "parameter_type": "External",
      "value": "1.*^-10",
      "block_name": "BLINPUTS",
      "order_block": 3,
      "description": "Light neutrino mass scale m_nu = 0.1 eV, used to fix the seesaw Yukawa yv, Sec.3.3"
    },
    {
      "name": "xBL",
      "parameter_type": "Internal",
      "value": "MZp/(2*gp)",
      "description": "B-L breaking vev x = <chi>, x = MZP/(2 gp), Sec.2/Sec.5"
    },
    {
      "name": "CA",
      "parameter_type": "Internal",
      "value": "Sqrt[1-SA^2]",
      "description": "cos(alpha), Higgs mixing angle cosine"
    },
    {
      "name": "lamX",
      "parameter_type": "Internal",
      "value": "(1/(4*xBL^2))*((MH^2+MHH^2)+(1-2*SA^2)*(MHH^2-MH^2))",
      "interaction_order": ["NP", 2],
      "description": "Singlet quartic coupling lambda_2, Eq.(3.1)"
    },
    {
      "name": "lamHX",
      "parameter_type": "Internal",
      "value": "(1/(2*vev*xBL))*(2*SA*CA)*(MHH^2-MH^2)",
      "interaction_order": ["NP", 2],
      "description": "Portal coupling lambda_3, Eq.(3.1)"
    },
    {
      "name": "muX2",
      "parameter_type": "Internal",
      "value": "-2*lamX*xBL^2 - lamHX*vev^2",
      "description": "Singlet mass-squared mu^2 in V(H,chi), Eq.(2.2), fixed by the chi minimisation condition"
    },
    {
      "name": "yv",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yv[1,1]", "rhs": "Sqrt[2*mnu*MHN1]/vev"},
        {"lhs": "yv[1,2]", "rhs": "0"},
        {"lhs": "yv[1,3]", "rhs": "0"},
        {"lhs": "yv[2,1]", "rhs": "0"},
        {"lhs": "yv[2,2]", "rhs": "Sqrt[2*mnu*MHN2]/vev"},
        {"lhs": "yv[2,3]", "rhs": "0"},
        {"lhs": "yv[3,1]", "rhs": "0"},
        {"lhs": "yv[3,2]", "rhs": "0"},
        {"lhs": "yv[3,3]", "rhs": "Sqrt[2*mnu*MHN3]/vev"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Dirac neutrino Yukawa y^nu_ii = sqrt(2) M_Ni V_iN / v, Eq.(2.5)/(3.3), diagonal (no flavour mixing, Sec.2)"
    },
    {
      "name": "yM",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "yM[1,1]", "rhs": "MHN1/(Sqrt[2]*xBL)"},
        {"lhs": "yM[1,2]", "rhs": "0"},
        {"lhs": "yM[1,3]", "rhs": "0"},
        {"lhs": "yM[2,1]", "rhs": "0"},
        {"lhs": "yM[2,2]", "rhs": "MHN2/(Sqrt[2]*xBL)"},
        {"lhs": "yM[2,3]", "rhs": "0"},
        {"lhs": "yM[3,1]", "rhs": "0"},
        {"lhs": "yM[3,2]", "rhs": "0"},
        {"lhs": "yM[3,3]", "rhs": "MHN3/(Sqrt[2]*xBL)"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Majorana Yukawa y^M_ii = M_Ni/(sqrt(2) x), Eq.(2.5)/(2.6)"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "Zp",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MZp", "value": "1500."},
      "width": {"sym": "WZp", "value": "15."},
      "quantum_numbers": {},
      "pdg": 32,
      "particle_name": "Zp",
      "full_name": "B-L gauge boson",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "h2",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MHH", "value": "200."},
      "width": {"sym": "WHH", "value": "2."},
      "quantum_numbers": {},
      "pdg": 35,
      "particle_name": "h2",
      "full_name": "Heavy Higgs (B-L scalar/SM Higgs mixture)",
      "propagator_label": "h2",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "GZp",
      "self_conjugate": true,
      "indices": [],
      "goldstone": "Zp",
      "mass": {"sym": "MZp", "value": "1500."},
      "width": {"sym": "WZp", "value": "15."},
      "quantum_numbers": {},
      "pdg": 252,
      "particle_name": "GZp",
      "full_name": "Goldstone of Zp",
      "propagator_label": "GZp",
      "propagator_type": "D",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "chi",
      "self_conjugate": false,
      "indices": [],
      "quantum_numbers": {"YBL": "2"},
      "unphysical": true,
      "definitions": ["chi -> (xBL + CA*h2 - SA*H + I*GZp)/Sqrt[2]"]
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "HN",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["HN1", "HN2", "HN3"],
      "mass": {"sym": "MHN", "members": [["MHN1", "300."], ["MHN2", "300."], ["MHN3", "300."]]},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["hn1", "hn2", "hn3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["HN", "hn1", "hn2", "hn3"],
      "propagator_type": "S",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "HNR",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "quantum_numbers": {"YBL": "-1"},
      "unphysical": true,
      "definitions": ["HNR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] HN[sp2,ff]]"]
    }
  ],
  "gauge_xi": [["V[101]", "GaugeXi[Zp]"], ["S[101]", "1"], ["S[102]", "GaugeXi[Zp]"]],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]]"
    },
    {
      "name": "LScalarBL",
      "delayed": true,
      "expression": "Block[{mu,ii}, ExpandIndices[DCBL[chibar,mu,-2] DCBL[chi,mu,2] - muX2 chibar chi - lamX (chibar chi)^2 - lamHX Phibar[ii] Phi[ii] chibar chi, FlavorExpand->SU2D]]"
    },
    {
      "name": "LHNKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I/2 HNbar.Ga[mu].del[HN,mu] - 1/2 MHN HNbar.HN - (gp/2) HNbar.Ga[mu].Ga[5].HN Zp[mu], FlavorExpand->Generation]]"
    },
    {
      "name": "LZpFermions",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[-gp Zp[mu] (1/3 (uqbar.Ga[mu].uq + dqbar.Ga[mu].dq) - (lbar.Ga[mu].l + vlbar.Ga[mu].vl))]]"
    },
    {
      "name": "LYukNu",
      "delayed": true,
      "expression": "Block[{sp,ii,jj,ff1,ff2,yuk}, yuk = ExpandIndices[-yv[ff1,ff2] LLbar[sp,ii,ff1].HNR[sp,ff2] Phibar[jj] Eps[ii,jj], FlavorExpand->SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LYukNMaj",
      "delayed": true,
      "expression": "Block[{ff1,ff2,yukM}, yukM = ExpandIndices[-(bar[CC[HNR]].yM.HNR) chi, FlavorExpand->Generation]; yukM + HC[yukM]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LZpKin + LScalarBL + LHNKin + LZpFermions + LYukNu + LYukNMaj"
    }
  ],
  "raw_preamble": [
    "(* Custom covariant derivative for U(1)_B-L: Zp is not registered in M$GaugeGroups (gtilde=0, no kinetic mixing, Eq.2.3 of 1811.11452), so its coupling to any B-L charged field must be added by hand on top of FeynRules' own DC[]. *)",
    "DCBL[field_, mu_, ybl_] := DC[field, mu] + I*gp*ybl*Zp[mu]*field;"
  ],
  "raw_blocks": []
}
```