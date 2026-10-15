## Self‑audit (produced before the model)

**Note on scope/method.** ALRSM (arXiv:1911.12883) gauges the SM up to replacing part of hypercharge with `SU(2)_R'×U(1)_{B-L}`. Per the schema's "SM add‑on" convention and the sandbox instruction that this add‑on loads on top of `SM.fr` (whose `U1Y`, `SU2L`, `SU3C`, `Phi`, `QL`, `LL`, `uR/dR/lR` are kept as‑is), I did **not** re‑gauge `SU(2)_R'`/`U(1)_{B-L}` as new `M$GaugeGroups` (`gauge_groups: []`). Instead `Zp`, `Wp` are declared as independent massive vector `ParticleClass`es with their own kinetic+mass terms and simplified NC/CC current couplings — a documented simplification (full non‑abelian `SU(2)_R'` construction plus the 3×3 `A‑Z‑Z'` rotation is out of scope here). The neutral/charged Higgs 3×3 mixing (`U^H_{3×3}`,`U^A_{3×3}`) is transcribed from the LaTeX (`f_i,g_i,D1,D2,ξ`) with an explicit, stated row assignment (row1=`phi2^0`,row2=`chiL0`,row3=`chiR0`; columns `(H,H2,H3)` / `(G0,G2z,A2)`) since the appendix does not spell out which physical row is which. `M_{H_1^\pm}`,`M_{H_2^\pm}` are written in the source without an explicit square on the LHS, but the RHS is dimensionally `GeV^2`; I take the mass to be the square root (documented, not silent).

| term | fields | dim d | coupling | coupling dim (4‑d) | 1/Λ | Q sum | Y sum | SU(2) contraction | SU(3) | new‑U(1) sum | L/B sum | CC[] | frac/root check | HC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LdqpKin | dqpbar,dqp | 4(kin)+ | Mdqpmat | 0 (mass term dim1 coeff GeV) | n/a | 0 | n/a | singlet | triplet | n/a | ΔB=0 | n/a | n/a | self (Dirac, HC implicit in `.` mass term convention) |
| LnlKin | nlbar,nl | – | Mnlmat | GeV | n/a | 0 | n/a | singlet | singlet | n/a | ΔL=0 (n_R has U1S but term is diag mass, S‑conserving) | n/a | n/a | self |
| LZpKin | Zp,Zp | 4 | MZp | GeV | n/a | 0 | – | singlet | singlet | n/a | – | n/a | n/a | self‑conj |
| LWpKin | Wpbar,Wp | 4 | MWp | GeV | n/a | 0(Wbar+W) | – | singlet | singlet | n/a | – | n/a | n/a | HC pair (bar/plain) |
| LZZpMix | Z,Zp | 2 | dMZZp | GeV² | n/a | 0 | – | – | – | n/a | – | n/a | Eq. (2.13) 2nd line, `tan(2ζW)` transcribed from LaTeX | self |
| Lkin(PhiBD) | PhiBDbar,PhiBD | 4 | 1 | 0 | n/a | 0 | 0 | bidoublet self‑contraction | singlet | S:0 | – | n/a | n/a | self‑pair |
| Lkin(ChiL) | ChiLbar,ChiL | 4 | 1 | 0 | n/a | 0 | 0 | doublet·antidoublet | singlet | S:0 | – | n/a | n/a | self‑pair |
| Lkin(ChiR) | ChiRbar,ChiR | 4 | 1 | 0 | n/a | 0 | 0 | doublet·antidoublet | singlet | S:1/2 net cancels vs partner in potential | – | n/a | n/a | self‑pair |
| LHpot (mu1,mu2,lam1‑4,alp1‑3,kap) | PhiBD,ChiL,ChiR (bars) | 4 | mu1,mu2,lam_i,alpha_i,kap | 2,2,0,0,1 resp. | n/a | 0 each term | 0 each term | Eps‑double‑contractions per term (see text) | singlet | S:0 each term | – | n/a | Eq. (2.3), LaTeX `\frac{}{}`,`\sqrt{}` used literally | kap term is HC pair |
| Yuk(a) QLbar.Yu.QR·PhiBDbar | QL,QR,PhiBD | 4.5 | Yu (NP) | -0.5→abs. via k vev(Internal) | n/a | 0 | 0 | double‑Eps (hatted bidoublet) | 3x3bar | S:0 | ΔB=0 | n/a | Eq.(2.2) | HC |
| Yuk(b) QLbar.Yd.dR·ChiL | QL,dR,ChiL | 4.5 | Yd (NP) | derived from Md/vL (Internal) | n/a | 0 | 0 | doublet‑antidoublet direct | 3x3bar | S:0 | ΔB=0 | n/a | Eq.(2.2) | HC |
| Yuk(c) QRbar.Ydp.dpL·ChiR | QR,dpL,ChiR | 4.5 | Ydp (NP) | derived from MDP/MSP/MBP,vR | n/a | 0 | 0 | doublet‑antidoublet direct | 3x3bar | S:0 | ΔB=0 | n/a | Eq.(2.2) | HC |
| Yuk(d) LLbar.Ye.LR·PhiBD | LL,LR,PhiBD | 4.5 | Ye (NP) | derived from Me/Mmu/Mtau,k | n/a | 0 | 0 | doublet‑antidoublet direct (both SU2 factors) | singlet | S:0 | ΔL=0 | n/a | Eq.(2.2) | HC |
| Yuk(e) LLbar.Ynu.nuR·ChiLbar | LL,nuR,ChiL | 4.5 | Ynu (NP) | derived from Mve/Mvm/Mvt,vL | n/a | 0 | 0 | Eps (hatted chiL) | singlet | S:0 | ΔL=0 | n/a | Eq.(2.2) | HC |
| Yuk(f) LRbar.Yn.nlL·ChiRbar | LR,nlL,ChiR | 4.5 | Yn (NP) | derived from Mne/Mnm/Mnt,vR | n/a | 0 | 0 | Eps (hatted chiR) | singlet | S:0 | ΔL=0 | n/a | Eq.(2.2) | HC |
| Leff (ggH,aaH) | H,G,G / H,A,A | 5 | Ghgg,Ghaa | -1 (GeV⁻¹, External) | n/a (loop‑induced eff. op., no explicit Λ quoted by paper) | 0 | 0 | n/a | octet² | n/a | n/a | n/a | text near Eq. after (2.13) | self |
| LZpFcurrent / LWpFcurrent | Zp/Wp + fermion bilinears | 4 | gR,cphiW,sphiW combo | 0 | n/a | 0 (NC), CC conserves Q | – | T3R projections | per fermion | n/a | conserves L | n/a (CC uses right‑chiral fields only, no C‑conjugation needed) | simplified current, documented | self/HC pair |

- New particle classes with kinetic(+mass) term in `LTotal`: `dqp`, `nl`, `Zp`, `Wp`, `PhiBD`(unphysical, substituted), `ChiL`(unphysical), `ChiR`(unphysical) — all confirmed present in `LTotal`.
- No non‑fundamental colour representation is introduced (`dqp` is an ordinary `Colour` triplet); no `AddGaugeRepresentation` needed.
- `SelfConjugate -> True` classes: `nl`? No — `nl` is Dirac (`self_conjugate=false`, U(1)_S forbids a Majorana mass). Self‑conjugate new classes: `Zp`, `A0new` (A1,A2), `h0new` (H1,H2,H3), `G2z`. None carries `QuantumNumbers`.
- Names/indices checked against Mathematica built‑ins, FeynRules symbols and `SM.fr` names (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,...`): none of `dqp,nl,QR,LR,nuR,dpL,nlL,PhiBD,ChiL,ChiR,h0new,A0new,Hpnew,Zp,Wp,SU2Rd,` or any parameter name collide.
- `LTotal` sums: `LdqpKin+LnlKin+LZpKin+LWpKin+LZZpMix+LHiggsKinBD+LHiggsKinChiL+LHiggsKinChiR+LHpot+LYukawaBSM+HC[LYukawaBSM]+LeffHVV+LZpFcurrent+LWpFcurrent`.
- Reference/cached `.fr` file read: **none**.

```json
{
  "model_name": "ALRM_general_gen",
  "info": {
    "authors": ["Mariana Frank", "Benjamin Fuks", "Ozer Ozdal"],
    "version": "1.0",
    "date": "2026-09-17",
    "institutions": ["Concordia University", "LPTHE Sorbonne Universite/CNRS"],
    "emails": ["fuks@lpthe.jussieu.fr"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [
    {"name": "SU2Rd", "range_kind": "NoUnfold", "size": 2, "style_symbol": "rr"}
  ],
  "vevs": [["PhiBD[2,2]", "k"], ["ChiL[2]", "vL"], ["ChiR[2]", "vR"]],
  "parameters": [
    {"name": "tb", "parameter_type": "External", "value": "4.58", "block_name": "SMINPUTS", "order_block": 5, "description": "tan(beta)=k/vL, Eq.(2.10)"},
    {"name": "gR", "parameter_type": "External", "value": "0.374", "block_name": "SMINPUTS", "order_block": 6, "interaction_order": ["NP", 1], "description": "SU(2)_R' gauge coupling"},
    {"name": "vevp", "parameter_type": "External", "value": "7799.", "block_name": "SMINPUTS", "order_block": 7, "description": "v' [GeV], Sqrt[k^2+vR^2]"},
    {"name": "lam2", "parameter_type": "External", "value": "0.", "block_name": "HPOTINPUTS", "order_block": 1, "interaction_order": ["NP", 1], "description": "Higgs potential lambda2, Eq.(2.3)"},
    {"name": "lam3", "parameter_type": "External", "value": "0.0196", "block_name": "HPOTINPUTS", "order_block": 2, "interaction_order": ["NP", 1], "description": "Higgs potential lambda3, Eq.(2.3)"},
    {"name": "alp1", "parameter_type": "External", "value": "0.0144", "block_name": "HPOTINPUTS", "order_block": 3, "interaction_order": ["NP", 1], "description": "Higgs potential alpha1, Eq.(2.3)"},
    {"name": "alp2", "parameter_type": "External", "value": "0.0144", "block_name": "HPOTINPUTS", "order_block": 4, "interaction_order": ["NP", 1], "description": "Higgs potential alpha2, Eq.(2.3)"},
    {"name": "alp3", "parameter_type": "External", "value": "0.0144", "block_name": "HPOTINPUTS", "order_block": 5, "interaction_order": ["NP", 1], "description": "Higgs potential alpha3, Eq.(2.3)"},
    {"name": "kap", "parameter_type": "External", "value": "-31.08", "block_name": "HPOTINPUTS", "order_block": 6, "interaction_order": ["NP", 1], "description": "Higgs potential kappa [GeV], Eq.(2.3), must be <0"},
    {"name": "Ghgg", "parameter_type": "External", "value": "1.*^-4", "block_name": "EFFECTIVEHIGGS", "order_block": 1, "interaction_order": ["NP", 1], "description": "SM-Higgs-gluon effective coupling [GeV^-1]"},
    {"name": "Ghaa", "parameter_type": "External", "value": "1.*^-4", "block_name": "EFFECTIVEHIGGS", "order_block": 2, "interaction_order": ["NP", 1], "description": "SM-Higgs-photon effective coupling [GeV^-1]"},
    {"name": "MDP", "parameter_type": "External", "value": "1500.", "block_name": "MASS", "order_block": 6000001, "description": "d' exotic quark mass [GeV]"},
    {"name": "MSP", "parameter_type": "External", "value": "1800.", "block_name": "MASS", "order_block": 6000003, "description": "s' exotic quark mass [GeV]"},
    {"name": "MBP", "parameter_type": "External", "value": "2000.", "block_name": "MASS", "order_block": 6000005, "description": "b' exotic quark mass [GeV]"},
    {"name": "Mne", "parameter_type": "External", "value": "756.", "block_name": "MASS", "order_block": 6000012, "description": "scotino n1 mass [GeV]"},
    {"name": "Mnm", "parameter_type": "External", "value": "971.", "block_name": "MASS", "order_block": 6000014, "description": "scotino n2 mass [GeV]"},
    {"name": "Mnt", "parameter_type": "External", "value": "1202.", "block_name": "MASS", "order_block": 6000016, "description": "scotino n3 mass [GeV]"},
    {"name": "Mve", "parameter_type": "External", "value": "1.*^-9", "block_name": "MASS", "order_block": 12, "description": "electron-neutrino Dirac mass [GeV] (placeholder, sub-eV scale not benchmarked numerically in paper)"},
    {"name": "Mvm", "parameter_type": "External", "value": "1.*^-9", "block_name": "MASS", "order_block": 14, "description": "muon-neutrino Dirac mass [GeV]"},
    {"name": "Mvt", "parameter_type": "External", "value": "1.*^-9", "block_name": "MASS", "order_block": 16, "description": "tau-neutrino Dirac mass [GeV]"},
    {"name": "CKMlam", "parameter_type": "External", "value": "0.22537", "block_name": "CKMBLOCK", "order_block": 1, "description": "Wolfenstein lambda"},
    {"name": "CKMA", "parameter_type": "External", "value": "0.814", "block_name": "CKMBLOCK", "order_block": 2, "description": "Wolfenstein A"},
    {"name": "CKMrho", "parameter_type": "External", "value": "0.117", "block_name": "CKMBLOCK", "order_block": 3, "description": "Wolfenstein rho-bar"},
    {"name": "CKMeta", "parameter_type": "External", "value": "0.353", "block_name": "CKMBLOCK", "order_block": 4, "description": "Wolfenstein eta-bar"},
    {"name": "CKMps12", "parameter_type": "External", "value": "0.22537", "block_name": "CKMBLOCK", "order_block": 11, "description": "sin(theta12) of V_CKM', default = SM value per sec.3 scan setup"},
    {"name": "CKMps23", "parameter_type": "External", "value": "0.0415", "block_name": "CKMBLOCK", "order_block": 12, "description": "sin(theta23) of V_CKM'"},
    {"name": "CKMps13", "parameter_type": "External", "value": "0.0035", "block_name": "CKMBLOCK", "order_block": 13, "description": "sin(theta13) of V_CKM'"},
    {"name": "CKMpdel", "parameter_type": "External", "value": "1.2", "block_name": "CKMBLOCK", "order_block": 14, "description": "Dirac phase of V_CKM' [rad]"},
    {"name": "PMNSs12", "parameter_type": "External", "value": "0.554", "block_name": "PMNSBLOCK", "order_block": 1, "description": "sin(theta12) of V_PMNS"},
    {"name": "PMNSs23", "parameter_type": "External", "value": "0.738", "block_name": "PMNSBLOCK", "order_block": 2, "description": "sin(theta23) of V_PMNS"},
    {"name": "PMNSs13", "parameter_type": "External", "value": "0.148", "block_name": "PMNSBLOCK", "order_block": 3, "description": "sin(theta13) of V_PMNS"},
    {"name": "PMNSdel", "parameter_type": "External", "value": "3.86", "block_name": "PMNSBLOCK", "order_block": 4, "description": "Dirac phase of V_PMNS [rad]"},
    {"name": "PMNSps12", "parameter_type": "External", "value": "0.554", "block_name": "PMNSBLOCK", "order_block": 11, "description": "sin(theta12) of V_PMNS', default = V_PMNS per sec.3"},
    {"name": "PMNSps23", "parameter_type": "External", "value": "0.738", "block_name": "PMNSBLOCK", "order_block": 12, "description": "sin(theta23) of V_PMNS'"},
    {"name": "PMNSps13", "parameter_type": "External", "value": "0.148", "block_name": "PMNSBLOCK", "order_block": 13, "description": "sin(theta13) of V_PMNS'"},
    {"name": "PMNSpdel", "parameter_type": "External", "value": "3.86", "block_name": "PMNSBLOCK", "order_block": 14, "description": "Dirac phase of V_PMNS' [rad]"},

    {"name": "alpha12", "parameter_type": "Internal", "value": "alp1+alp2", "description": "alpha_{12}=alpha1+alpha2, Eq.(2.15)"},
    {"name": "vSM", "parameter_type": "Internal", "value": "Sqrt[1/(Sqrt[2]*Gf)]", "description": "v from Fermi constant, appendix C"},
    {"name": "cbeta", "parameter_type": "Internal", "value": "1/Sqrt[1+tb^2]", "description": "cos(beta)"},
    {"name": "sbeta", "parameter_type": "Internal", "value": "tb/Sqrt[1+tb^2]", "description": "sin(beta)"},
    {"name": "vL", "parameter_type": "Internal", "value": "vSM*cbeta", "description": "chiL vev [GeV], appendix C"},
    {"name": "k", "parameter_type": "Internal", "value": "vSM*sbeta", "description": "bidoublet vev [GeV], appendix C"},
    {"name": "vR", "parameter_type": "Internal", "value": "Sqrt[vevp^2-k^2]", "description": "chiR vev [GeV], appendix C"},
    {"name": "czeta", "parameter_type": "Internal", "value": "vR/Sqrt[k^2+vR^2]", "description": "cos(zeta), Eq.(2.11)"},
    {"name": "szeta", "parameter_type": "Internal", "value": "k/Sqrt[k^2+vR^2]", "description": "sin(zeta), Eq.(2.11)"},
    {"name": "gL", "parameter_type": "Internal", "value": "2*MW/Sqrt[k^2+vL^2]", "description": "SU(2)_L coupling derived from Eq.(2.12)"},
    {"name": "gBL", "parameter_type": "Internal", "value": "g1*gR/Sqrt[gR^2-g1^2]", "description": "U(1)_{B-L} coupling from 1/gY^2=1/gR^2+1/gBL^2"},
    {"name": "sphiW", "parameter_type": "Internal", "value": "g1/gR", "description": "sin(phiW), Eq.(2.14)"},
    {"name": "cphiW", "parameter_type": "Internal", "value": "Sqrt[1-sphiW^2]", "description": "cos(phiW)"},
    {"name": "tan2zw", "parameter_type": "Internal", "value": "(2*cphiW*cw*gL*gR*(cphiW^2*k^2-sphiW^2*vL^2))/(-(gL^2-cphiW^2*cw^2*gR^2)*cphiW^2*k^2-(gL^2-cw^2*gBL^2*sphiW^2)*cphiW^2*vL^2+cw^2*gR^2*vR^2)", "description": "tan(2*zetaW), Eq.(2.14) 2nd line"},
    {"name": "zw", "parameter_type": "Internal", "value": "ArcTan[tan2zw]/2", "description": "Z-Z' mixing angle"},
    {"name": "dMZZp", "parameter_type": "Internal", "value": "MZp^2*Tan[2*zw]", "description": "simplified Z-Z' mixing mass-squared insertion, encodes zw (Rule 8)"},
    {"name": "MZp", "parameter_type": "Internal", "value": "(1/2)*Sqrt[gBL^2*sphiW^2*vL^2+gR^2*(cphiW^4*k^2+vR^2)/cphiW^2]", "description": "Z' mass [GeV], Eq.(2.15)"},
    {"name": "MWp", "parameter_type": "Internal", "value": "(1/2)*gR*Sqrt[k^2+vR^2]", "description": "W' mass [GeV], Eq.(2.12)"},
    {"name": "mu1sq", "parameter_type": "Internal", "value": "alpha12*(vL^2+vR^2)+k^2*lam1+kap*vL*vR/(Sqrt[2]*k)", "description": "mu1^2, Eq.(2.16)"},
    {"name": "mu2sq", "parameter_type": "Internal", "value": "alpha12*k^2+lam3*(vL^2+vR^2)", "description": "mu2^2, Eq.(2.16)"},
    {"name": "lam4", "parameter_type": "Internal", "value": "lam3-kap*k/(Sqrt[2]*vL*vR)", "description": "lambda4, Eq.(2.16)"},
    {"name": "mfA4", "parameter_type": "Internal", "value": "-2*Sqrt[2]*k*lam3*vL*vR*(vL^2+vR^2)+kap*(vL^2*vR^2+k^2*(vL^2+vR^2))", "description": "mathfrak a^(4), appendix A"},
    {"name": "mfA2", "parameter_type": "Internal", "value": "2*Sqrt[2]*alpha12^2*k^3*vL*vR*(vL^2+vR^2)+kap*(lam3*vL^2*vR^2*(vL^2+vR^2)+k^2*(4*alpha12*vL^2*vR^2+lam3*(vL^2-vR^2)^2))", "description": "mathfrak a^(2), appendix A"},
    {"name": "lam1", "parameter_type": "Internal", "value": "(1/(2*k^3))*(Sqrt[2]*k*vL*vR*MH^6+mfA4*MH^4-2*mfA2*MH^2-4*alpha12^2*kap*k^4*(vL^2-vR^2)^2)/(Sqrt[2]*vL*vR*MH^4+(kap*k-2*Sqrt[2]*lam3*vL*vR)*(vL^2+vR^2)*MH^2-2*kap*k*lam3*(vL^2-vR^2)^2)", "description": "lambda1 traded for MH (SM Higgs mass), Eq.(A.7)"},
    {"name": "mfA", "parameter_type": "Internal", "value": "(1/(Sqrt[2]*k*vL*vR))*(vL*vR*(2*Sqrt[2]*k^3*lam1-kap*vL*vR)+k*(2*Sqrt[2]*lam3*vL*vR-kap*k)*(vL^2+vR^2))-MH^2", "description": "mathfrak a, appendix A"},
    {"name": "mfB", "parameter_type": "Internal", "value": "(1/(k*vL*vR))*(Sqrt[2]*kap*k^2*(4*alpha12*vL^2*vR^2+lam3*(vL^2-vR^2)^2)+(4*k^3*(alpha12^2-lam1*lam3)*vL*vR+Sqrt[2]*kap*(k^4*lam1+lam3*vL^2*vR^2))*(vL^2+vR^2))", "description": "mathfrak b, appendix A"},
    {"name": "MH1", "parameter_type": "Internal", "value": "Sqrt[-(alp2-alp3)*(vL^2+vR^2)-kap*vL*vR/(Sqrt[2]*k)+2*k^2*lam2]", "description": "H1^0 mass [GeV] (=MA1), Eq.(A.6)"},
    {"name": "MA1", "parameter_type": "Internal", "value": "MH1", "description": "A1^0 mass, mass-degenerate with H1^0, Eq.(A.6)"},
    {"name": "MA2", "parameter_type": "Internal", "value": "Sqrt[-(kap/(Sqrt[2]*k*vL*vR))*(vL^2*vR^2+k^2*(vL^2+vR^2))]", "description": "A2^0 mass [GeV], Eq.(A.8), Sqrt added since RHS is a mass-squared (dimensional check)"},
    {"name": "MH2", "parameter_type": "Internal", "value": "Sqrt[(mfA-Sqrt[mfA^2+4*(mfB+mfA*MH^2)])/2]", "description": "H2^0 mass [GeV], lighter root, Eq.(A.8)"},
    {"name": "MH3", "parameter_type": "Internal", "value": "Sqrt[(mfA+Sqrt[mfA^2+4*(mfB+mfA*MH^2)])/2]", "description": "H3^0 mass [GeV], heavier root, Eq.(A.8)"},
    {"name": "MH1pm", "parameter_type": "Internal", "value": "Sqrt[((k^2+vL^2)/(2*k*vL))*(-2*(alp2-alp3)*k*vL-Sqrt[2]*kap*vR)]", "description": "H1^+- mass [GeV], Eq.(A.3); Sqrt added, dimensional check: RHS is GeV^2 though paper's LHS symbol lacks an explicit square"},
    {"name": "MH2pm", "parameter_type": "Internal", "value": "Sqrt[((k^2+vR^2)/(2*k*vR))*(-2*(alp2-alp3)*k*vR-Sqrt[2]*kap*vL)]", "description": "H2^+- mass [GeV], Eq.(A.3), same Sqrt convention as MH1pm"},
    {"name": "f0", "parameter_type": "Internal", "value": "(2*MH^4*vL*vR+MH^2*(vL^2+vR^2)*(Sqrt[2]*k*kap-4*vL*vR*lam3)-2*Sqrt[2]*k*(vL^2-vR^2)^2*lam3*kap)/(vR*(MH^2*(4*k*vL*vR*alpha12+Sqrt[2]*vL^2*kap)+2*Sqrt[2]*(k^2*alpha12+vL^2*lam3)*(vR^2-vL^2)*kap))", "description": "f_0 (i=0, SM-like Higgs), Eq.(A.9)"},
    {"name": "f2", "parameter_type": "Internal", "value": "(2*MH2^4*vL*vR+MH2^2*(vL^2+vR^2)*(Sqrt[2]*k*kap-4*vL*vR*lam3)-2*Sqrt[2]*k*(vL^2-vR^2)^2*lam3*kap)/(vR*(MH2^2*(4*k*vL*vR*alpha12+Sqrt[2]*vL^2*kap)+2*Sqrt[2]*(k^2*alpha12+vL^2*lam3)*(vR^2-vL^2)*kap))", "description": "f_2 (i=2), Eq.(A.9)"},
    {"name": "f3", "parameter_type": "Internal", "value": "(2*MH3^4*vL*vR+MH3^2*(vL^2+vR^2)*(Sqrt[2]*k*kap-4*vL*vR*lam3)-2*Sqrt[2]*k*(vL^2-vR^2)^2*lam3*kap)/(vR*(MH3^2*(4*k*vL*vR*alpha12+Sqrt[2]*vL^2*kap)+2*Sqrt[2]*(k^2*alpha12+vL^2*lam3)*(vR^2-vL^2)*kap))", "description": "f_3 (i=3), Eq.(A.9)"},
    {"name": "g0", "parameter_type": "Internal", "value": "(vL/vR)*(MH^2*(4*k*vL*vR*alpha12+Sqrt[2]*vR^2*kap)+2*Sqrt[2]*(k^2*alpha12+vR^2*lam3)*(vL^2-vR^2)*kap)/(MH^2*(4*k*vL*vR*alpha12+Sqrt[2]*vL^2*kap)+2*Sqrt[2]*(k^2*alpha12+vL^2*lam3)*(vR^2-vL^2)*kap)", "description": "g_0, Eq.(A.9)"},
    {"name": "g2", "parameter_type": "Internal", "value": "(vL/vR)*(MH2^2*(4*k*vL*vR*alpha12+Sqrt[2]*vR^2*kap)+2*Sqrt[2]*(k^2*alpha12+vR^2*lam3)*(vL^2-vR^2)*kap)/(MH2^2*(4*k*vL*vR*alpha12+Sqrt[2]*vL^2*kap)+2*Sqrt[2]*(k^2*alpha12+vL^2*lam3)*(vR^2-vL^2)*kap)", "description": "g_2, Eq.(A.9)"},
    {"name": "g3", "parameter_type": "Internal", "value": "(vL/vR)*(MH3^2*(4*k*vL*vR*alpha12+Sqrt[2]*vR^2*kap)+2*Sqrt[2]*(k^2*alpha12+vR^2*lam3)*(vL^2-vR^2)*kap)/(MH3^2*(4*k*vL*vR*alpha12+Sqrt[2]*vL^2*kap)+2*Sqrt[2]*(k^2*alpha12+vL^2*lam3)*(vR^2-vL^2)*kap)", "description": "g_3, Eq.(A.9)"},
    {"name": "ffD1", "parameter_type": "Internal", "value": "1+f0^2+g0^2", "description": "D1, Eq.(A.9)"},
    {"name": "ffD2", "parameter_type": "Internal", "value": "f2^2*(1+g0^2)+(g0-g2)^2-2*f0*f2*(1+g0*g2)+f0^2*(1+g2^2)", "description": "D2, Eq.(A.9)"},
    {"name": "xiSign", "parameter_type": "Internal", "value": "Sign[g0*(f2-f3)+g2*(f3-f0)+g3*(f0-f2)]", "description": "xi, Eq.(A.9)"},
    {"name": "UH3", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "value_rules": [
      {"lhs": "UH3[1,1]", "rhs": "f0/Sqrt[ffD1]/Sqrt[2]"},
      {"lhs": "UH3[1,2]", "rhs": "(f2*(1+g0^2)-f0*(1+g0*g2))/Sqrt[ffD1*ffD2]/Sqrt[2]"},
      {"lhs": "UH3[1,3]", "rhs": "xiSign*(g2-g0)/Sqrt[ffD2]/Sqrt[2]"},
      {"lhs": "UH3[2,1]", "rhs": "g0/Sqrt[ffD1]/Sqrt[2]"},
      {"lhs": "UH3[2,2]", "rhs": "(g2*(1+f0^2)-g0*(1+f0*f2))/Sqrt[ffD1*ffD2]/Sqrt[2]"},
      {"lhs": "UH3[2,3]", "rhs": "xiSign*(f0-f2)/Sqrt[ffD2]/Sqrt[2]"},
      {"lhs": "UH3[3,1]", "rhs": "1/Sqrt[ffD1]/Sqrt[2]"},
      {"lhs": "UH3[3,2]", "rhs": "(f0^2+g0^2-f0*f2-g0*g2)/Sqrt[ffD1*ffD2]/Sqrt[2]"},
      {"lhs": "UH3[3,3]", "rhs": "xiSign*(g0*f2-g2*f0)/Sqrt[ffD2]/Sqrt[2]"}
    ], "description": "U^H_{3x3} rows=(phi2^0,chiL0,chiR0), cols=(H,H2,H3), Eq.(A.5)"},
    {"name": "UA3", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "value_rules": [
      {"lhs": "UA3[1,1]", "rhs": "-(k/Sqrt[k^2+vR^2])/Sqrt[2]"},
      {"lhs": "UA3[1,2]", "rhs": "(k*vR^2/Sqrt[(k^2+vR^2)*(vL^2*vR^2+k^2*vL^2+vR^2*k^2)])/Sqrt[2]"},
      {"lhs": "UA3[1,3]", "rhs": "(vR*vL/Sqrt[vL^2*vR^2+k^2*vL^2+vR^2*k^2])/Sqrt[2]"},
      {"lhs": "UA3[2,1]", "rhs": "0"},
      {"lhs": "UA3[2,2]", "rhs": "(vL*Sqrt[k^2+vR^2]/Sqrt[vL^2*vR^2+k^2*vL^2+vR^2*k^2])/Sqrt[2]"},
      {"lhs": "UA3[2,3]", "rhs": "-(k*vR/Sqrt[vL^2*vR^2+k^2*vL^2+vR^2*k^2])/Sqrt[2]"},
      {"lhs": "UA3[3,1]", "rhs": "(vR/Sqrt[vR^2+k^2])/Sqrt[2]"},
      {"lhs": "UA3[3,2]", "rhs": "(k^2*vR/Sqrt[(k^2+vR^2)*(vL^2*vR^2+k^2*vL^2+vR^2*k^2)])/Sqrt[2]"},
      {"lhs": "UA3[3,3]", "rhs": "(k*vL/Sqrt[vL^2*vR^2+k^2*vL^2+vR^2*k^2])/Sqrt[2]"}
    ], "description": "U^A_{3x3} rows=(phi2^0,chiL0,chiR0), cols=(G0,G2z,A2), Eq.(A.4)"},
    {"name": "YuBD", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "interaction_order": ["NP", 1], "value_rules": [
      {"lhs": "YuBD[1,1]", "rhs": "Sqrt[2]*MU/k"}, {"lhs": "YuBD[2,2]", "rhs": "Sqrt[2]*MC/k"}, {"lhs": "YuBD[3,3]", "rhs": "Sqrt[2]*MT/k"},
      {"lhs": "YuBD[1,2]", "rhs": "0"}, {"lhs": "YuBD[1,3]", "rhs": "0"}, {"lhs": "YuBD[2,1]", "rhs": "0"},
      {"lhs": "YuBD[2,3]", "rhs": "0"}, {"lhs": "YuBD[3,1]", "rhs": "0"}, {"lhs": "YuBD[3,2]", "rhs": "0"}
    ], "description": "up-type bidoublet Yukawa, diag from SM up masses / k, Eq.(A.1)"},
    {"name": "YeBD", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "interaction_order": ["NP", 1], "value_rules": [
      {"lhs": "YeBD[1,1]", "rhs": "Sqrt[2]*Me/k"}, {"lhs": "YeBD[2,2]", "rhs": "Sqrt[2]*MMU/k"}, {"lhs": "YeBD[3,3]", "rhs": "Sqrt[2]*MTA/k"},
      {"lhs": "YeBD[1,2]", "rhs": "0"}, {"lhs": "YeBD[1,3]", "rhs": "0"}, {"lhs": "YeBD[2,1]", "rhs": "0"},
      {"lhs": "YeBD[2,3]", "rhs": "0"}, {"lhs": "YeBD[3,1]", "rhs": "0"}, {"lhs": "YeBD[3,2]", "rhs": "0"}
    ], "description": "charged-lepton bidoublet Yukawa, diag, Eq.(A.1)"},
    {"name": "YdBD", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "interaction_order": ["NP", 1], "value_rules": [
      {"lhs": "YdBD[1,1]", "rhs": "Sqrt[2]*MD/vL"}, {"lhs": "YdBD[2,2]", "rhs": "Sqrt[2]*MS/vL"}, {"lhs": "YdBD[3,3]", "rhs": "Sqrt[2]*MB/vL"},
      {"lhs": "YdBD[1,2]", "rhs": "0"}, {"lhs": "YdBD[1,3]", "rhs": "0"}, {"lhs": "YdBD[2,1]", "rhs": "0"},
      {"lhs": "YdBD[2,3]", "rhs": "0"}, {"lhs": "YdBD[3,1]", "rhs": "0"}, {"lhs": "YdBD[3,2]", "rhs": "0"}
    ], "description": "down-quark chiL Yukawa, diag, Eq.(A.1)"},
    {"name": "YnuBD", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "interaction_order": ["NP", 1], "value_rules": [
      {"lhs": "YnuBD[1,1]", "rhs": "Sqrt[2]*Mve/vL"}, {"lhs": "YnuBD[2,2]", "rhs": "Sqrt[2]*Mvm/vL"}, {"lhs": "YnuBD[3,3]", "rhs": "Sqrt[2]*Mvt/vL"},
      {"lhs": "YnuBD[1,2]", "rhs": "0"}, {"lhs": "YnuBD[1,3]", "rhs": "0"}, {"lhs": "YnuBD[2,1]", "rhs": "0"},
      {"lhs": "YnuBD[2,3]", "rhs": "0"}, {"lhs": "YnuBD[3,1]", "rhs": "0"}, {"lhs": "YnuBD[3,2]", "rhs": "0"}
    ], "description": "neutrino Dirac Yukawa via chiL, diag, Eq.(A.1)"},
    {"name": "YdpBD", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "interaction_order": ["NP", 1], "value_rules": [
      {"lhs": "YdpBD[1,1]", "rhs": "Sqrt[2]*MDP/vR"}, {"lhs": "YdpBD[2,2]", "rhs": "Sqrt[2]*MSP/vR"}, {"lhs": "YdpBD[3,3]", "rhs": "Sqrt[2]*MBP/vR"},
      {"lhs": "YdpBD[1,2]", "rhs": "0"}, {"lhs": "YdpBD[1,3]", "rhs": "0"}, {"lhs": "YdpBD[2,1]", "rhs": "0"},
      {"lhs": "YdpBD[2,3]", "rhs": "0"}, {"lhs": "YdpBD[3,1]", "rhs": "0"}, {"lhs": "YdpBD[3,2]", "rhs": "0"}
    ], "description": "exotic down-quark chiR Yukawa, diag, Eq.(A.1)"},
    {"name": "YnBD", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "interaction_order": ["NP", 1], "value_rules": [
      {"lhs": "YnBD[1,1]", "rhs": "Sqrt[2]*Mne/vR"}, {"lhs": "YnBD[2,2]", "rhs": "Sqrt[2]*Mnm/vR"}, {"lhs": "YnBD[3,3]", "rhs": "Sqrt[2]*Mnt/vR"},
      {"lhs": "YnBD[1,2]", "rhs": "0"}, {"lhs": "YnBD[1,3]", "rhs": "0"}, {"lhs": "YnBD[2,1]", "rhs": "0"},
      {"lhs": "YnBD[2,3]", "rhs": "0"}, {"lhs": "YnBD[3,1]", "rhs": "0"}, {"lhs": "YnBD[3,2]", "rhs": "0"}
    ], "description": "scotino chiR Yukawa, diag, Eq.(A.1)"},
    {"name": "Mdqpmat", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "value_rules": [
      {"lhs": "Mdqpmat[1,1]", "rhs": "MDP"}, {"lhs": "Mdqpmat[2,2]", "rhs": "MSP"}, {"lhs": "Mdqpmat[3,3]", "rhs": "MBP"},
      {"lhs": "Mdqpmat[1,2]", "rhs": "0"}, {"lhs": "Mdqpmat[1,3]", "rhs": "0"}, {"lhs": "Mdqpmat[2,1]", "rhs": "0"},
      {"lhs": "Mdqpmat[2,3]", "rhs": "0"}, {"lhs": "Mdqpmat[3,1]", "rhs": "0"}, {"lhs": "Mdqpmat[3,2]", "rhs": "0"}
    ], "description": "diagonal dqp mass matrix for explicit mass term"},
    {"name": "Mnlmat", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "value_rules": [
      {"lhs": "Mnlmat[1,1]", "rhs": "Mne"}, {"lhs": "Mnlmat[2,2]", "rhs": "Mnm"}, {"lhs": "Mnlmat[3,3]", "rhs": "Mnt"},
      {"lhs": "Mnlmat[1,2]", "rhs": "0"}, {"lhs": "Mnlmat[1,3]", "rhs": "0"}, {"lhs": "Mnlmat[2,1]", "rhs": "0"},
      {"lhs": "Mnlmat[2,3]", "rhs": "0"}, {"lhs": "Mnlmat[3,1]", "rhs": "0"}, {"lhs": "Mnlmat[3,2]", "rhs": "0"}
    ], "description": "diagonal nl mass matrix for explicit mass term"},
    {"name": "CKMs13exp", "parameter_type": "Internal", "complex": true, "value": "(CKMA*CKMlam^3*Sqrt[1-CKMA^2*CKMlam^4]*(CKMrho+I*CKMeta))/(Sqrt[1-CKMlam^2]*(1-CKMA^2*CKMlam^4*(CKMrho+I*CKMeta)))", "description": "s13*Exp[I delta] for V_CKM, appendix C Wolfenstein relation"},
    {"name": "VCKM", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "complex": true, "unitary": true, "value_rules": [
      {"lhs": "VCKM[1,1]", "rhs": "Sqrt[1-CKMlam^2]*Sqrt[1-Abs[CKMs13exp]^2]"},
      {"lhs": "VCKM[1,2]", "rhs": "CKMlam*Sqrt[1-Abs[CKMs13exp]^2]"},
      {"lhs": "VCKM[1,3]", "rhs": "Conjugate[CKMs13exp]"},
      {"lhs": "VCKM[2,1]", "rhs": "-CKMlam*Sqrt[1-(CKMA*CKMlam^2)^2]-Sqrt[1-CKMlam^2]*(CKMA*CKMlam^2)*CKMs13exp"},
      {"lhs": "VCKM[2,2]", "rhs": "Sqrt[1-CKMlam^2]*Sqrt[1-(CKMA*CKMlam^2)^2]-CKMlam*(CKMA*CKMlam^2)*CKMs13exp"},
      {"lhs": "VCKM[2,3]", "rhs": "(CKMA*CKMlam^2)*Sqrt[1-Abs[CKMs13exp]^2]"},
      {"lhs": "VCKM[3,1]", "rhs": "CKMlam*(CKMA*CKMlam^2)-Sqrt[1-CKMlam^2]*Sqrt[1-(CKMA*CKMlam^2)^2]*CKMs13exp"},
      {"lhs": "VCKM[3,2]", "rhs": "-Sqrt[1-CKMlam^2]*(CKMA*CKMlam^2)-CKMlam*Sqrt[1-(CKMA*CKMlam^2)^2]*CKMs13exp"},
      {"lhs": "VCKM[3,3]", "rhs": "Sqrt[1-(CKMA*CKMlam^2)^2]*Sqrt[1-Abs[CKMs13exp]^2]"}
    ], "description": "new full 3-angle V_CKM from Wolfenstein params, appendix C"},
    {"name": "VPMNS", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "complex": true, "unitary": true, "value_rules": [
      {"lhs": "VPMNS[1,1]", "rhs": "Sqrt[1-PMNSs12^2]*Sqrt[1-PMNSs13^2]"},
      {"lhs": "VPMNS[1,2]", "rhs": "PMNSs12*Sqrt[1-PMNSs13^2]"},
      {"lhs": "VPMNS[1,3]", "rhs": "PMNSs13*Exp[-I*PMNSdel]"},
      {"lhs": "VPMNS[2,1]", "rhs": "-PMNSs12*Sqrt[1-PMNSs23^2]-Sqrt[1-PMNSs12^2]*PMNSs23*PMNSs13*Exp[I*PMNSdel]"},
      {"lhs": "VPMNS[2,2]", "rhs": "Sqrt[1-PMNSs12^2]*Sqrt[1-PMNSs23^2]-PMNSs12*PMNSs23*PMNSs13*Exp[I*PMNSdel]"},
      {"lhs": "VPMNS[2,3]", "rhs": "PMNSs23*Sqrt[1-PMNSs13^2]"},
      {"lhs": "VPMNS[3,1]", "rhs": "PMNSs12*PMNSs23-Sqrt[1-PMNSs12^2]*Sqrt[1-PMNSs23^2]*PMNSs13*Exp[I*PMNSdel]"},
      {"lhs": "VPMNS[3,2]", "rhs": "-Sqrt[1-PMNSs12^2]*PMNSs23-PMNSs12*Sqrt[1-PMNSs23^2]*PMNSs13*Exp[I*PMNSdel]"},
      {"lhs": "VPMNS[3,3]", "rhs": "Sqrt[1-PMNSs23^2]*Sqrt[1-PMNSs13^2]"}
    ], "description": "new V_PMNS (nu_L-nu_R Dirac mixing), appendix C"},
    {"name": "VCKMp", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "complex": true, "unitary": true, "value_rules": [
      {"lhs": "VCKMp[1,1]", "rhs": "Sqrt[1-CKMps12^2]*Sqrt[1-CKMps13^2]"},
      {"lhs": "VCKMp[1,2]", "rhs": "CKMps12*Sqrt[1-CKMps13^2]"},
      {"lhs": "VCKMp[1,3]", "rhs": "CKMps13*Exp[-I*CKMpdel]"},
      {"lhs": "VCKMp[2,1]", "rhs": "-CKMps12*Sqrt[1-CKMps23^2]-Sqrt[1-CKMps12^2]*CKMps23*CKMps13*Exp[I*CKMpdel]"},
      {"lhs": "VCKMp[2,2]", "rhs": "Sqrt[1-CKMps12^2]*Sqrt[1-CKMps23^2]-CKMps12*CKMps23*CKMps13*Exp[I*CKMpdel]"},
      {"lhs": "VCKMp[2,3]", "rhs": "CKMps23*Sqrt[1-CKMps13^2]"},
      {"lhs": "VCKMp[3,1]", "rhs": "CKMps12*CKMps23-Sqrt[1-CKMps12^2]*Sqrt[1-CKMps23^2]*CKMps13*Exp[I*CKMpdel]"},
      {"lhs": "VCKMp[3,2]", "rhs": "-Sqrt[1-CKMps12^2]*CKMps23-CKMps12*Sqrt[1-CKMps23^2]*CKMps13*Exp[I*CKMpdel]"},
      {"lhs": "VCKMp[3,3]", "rhs": "Sqrt[1-CKMps23^2]*Sqrt[1-CKMps13^2]"}
    ], "description": "V_CKM' (d'_R mixing), appendix B/C"},
    {"name": "VPMNSp", "parameter_type": "Internal", "indices": ["Generation", "Generation"], "complex": true, "unitary": true, "value_rules": [
      {"lhs": "VPMNSp[1,1]", "rhs": "Sqrt[1-PMNSps12^2]*Sqrt[1-PMNSps13^2]"},
      {"lhs": "VPMNSp[1,2]", "rhs": "PMNSps12*Sqrt[1-PMNSps13^2]"},
      {"lhs": "VPMNSp[1,3]", "rhs": "PMNSps13*Exp[-I*PMNSpdel]"},
      {"lhs": "VPMNSp[2,1]", "rhs": "-PMNSps12*Sqrt[1-PMNSps23^2]-Sqrt[1-PMNSps12^2]*PMNSps23*PMNSps13*Exp[I*PMNSpdel]"},
      {"lhs": "VPMNSp[2,2]", "rhs": "Sqrt[1-PMNSps12^2]*Sqrt[1-PMNSps23^2]-PMNSps12*PMNSps23*PMNSps13*Exp[I*PMNSpdel]"},
      {"lhs": "VPMNSp[2,3]", "rhs": "PMNSps23*Sqrt[1-PMNSps13^2]"},
      {"lhs": "VPMNSp[3,1]", "rhs": "PMNSps12*PMNSps23-Sqrt[1-PMNSps12^2]*Sqrt[1-PMNSps23^2]*PMNSps13*Exp[I*PMNSpdel]"},
      {"lhs": "VPMNSp[3,2]", "rhs": "-Sqrt[1-PMNSps12^2]*PMNSps23-PMNSps12*Sqrt[1-PMNSps23^2]*PMNSps13*Exp[I*PMNSpdel]"},
      {"lhs": "VPMNSp[3,3]", "rhs": "Sqrt[1-PMNSps23^2]*Sqrt[1-PMNSps13^2]"}
    ], "description": "V_PMNS' (n_R mixing), appendix B/C"}
  ],
  "particles": [
    {"spin_type": "F", "class_index": 101, "class_name": "dqp", "self_conjugate": false, "indices": ["Generation", "Colour"], "flavor_index": "Generation", "class_members": ["dp", "sp", "bp"], "mass": {"sym": "Mdqp0", "members": [["MDP", "1500."], ["MSP", "1800."], ["MBP", "2000."]]}, "width": {"massless": true}, "quantum_numbers": {"Q": "-1/3"}, "pdg": [6000001, 6000003, 6000005], "particle_name": ["dp", "sp", "bp"], "antiparticle_name": ["dp~", "sp~", "bp~"], "full_name": ["Exotic d-quark", "Exotic s-quark", "Exotic b-quark"], "propagator_label": ["dqp", "dp", "sp", "bp"], "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 102, "class_name": "nl", "self_conjugate": false, "indices": ["Generation"], "flavor_index": "Generation", "class_members": ["n1", "n2", "n3"], "mass": {"sym": "Mnl0", "members": [["Mne", "756."], ["Mnm", "971."], ["Mnt", "1202."]]}, "width": {"massless": true}, "quantum_numbers": {"Q": "0"}, "pdg": [6000012, 6000014, 6000016], "particle_name": ["n1", "n2", "n3"], "antiparticle_name": ["n1~", "n2~", "n3~"], "full_name": ["Scotino 1", "Scotino 2", "Scotino 3"], "propagator_label": ["nl", "n1", "n2", "n3"], "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 110, "class_name": "QR", "self_conjugate": false, "unphysical": true, "indices": ["SU2Rd", "Generation", "Colour"], "flavor_index": "SU2Rd", "quantum_numbers": {"Y": "1/6"}, "definitions": ["QR[sp1_,1,ff_,cc_] :> Module[{sp2}, ProjP[sp1,sp2] uq[sp2,ff,cc]]", "QR[sp1_,2,ff_,cc_] :> Module[{sp2}, ProjP[sp1,sp2] dqp[sp2,ff,cc]]"]},
    {"spin_type": "F", "class_index": 111, "class_name": "LR", "self_conjugate": false, "unphysical": true, "indices": ["SU2Rd", "Generation"], "flavor_index": "SU2Rd", "quantum_numbers": {"Y": "-1/2"}, "definitions": ["LR[sp1_,1,ff_] :> Module[{sp2}, ProjP[sp1,sp2] nl[sp2,ff]]", "LR[sp1_,2,ff_] :> Module[{sp2}, ProjP[sp1,sp2] l[sp2,ff]]"]},
    {"spin_type": "F", "class_index": 112, "class_name": "nuR", "self_conjugate": false, "unphysical": true, "indices": ["Generation"], "flavor_index": "Generation", "quantum_numbers": {"Y": "0"}, "definitions": ["nuR[sp1_,ff_] :> Module[{sp2}, ProjP[sp1,sp2] vl[sp2,ff]]"]},
    {"spin_type": "F", "class_index": 113, "class_name": "dpL", "self_conjugate": false, "unphysical": true, "indices": ["Generation", "Colour"], "flavor_index": "Generation", "quantum_numbers": {"Y": "-1/3"}, "definitions": ["dpL[sp1_,ff_,cc_] :> Module[{sp2}, ProjM[sp1,sp2] dqp[sp2,ff,cc]]"]},
    {"spin_type": "F", "class_index": 114, "class_name": "nlL", "self_conjugate": false, "unphysical": true, "indices": ["Generation"], "flavor_index": "Generation", "quantum_numbers": {"Y": "0"}, "definitions": ["nlL[sp1_,ff_] :> Module[{sp2}, ProjM[sp1,sp2] nl[sp2,ff]]"]},
    {"spin_type": "S", "class_index": 120, "class_name": "PhiBD", "self_conjugate": false, "unphysical": true, "indices": ["SU2D", "SU2Rd"], "flavor_index": "SU2D", "quantum_numbers": {"Y": "0"}, "definitions": [
      "PhiBD[1,1] -> (H1+I*A1)/Sqrt[2]",
      "PhiBD[1,2] -> cbeta*Hp1+sbeta*GP",
      "PhiBD[2,1] -> czeta*Hp2bar+szeta*G2pbar",
      "PhiBD[2,2] -> (k+UH3[1,1]*H+UH3[1,2]*H2+UH3[1,3]*H3+I*(UA3[1,1]*G0+UA3[1,2]*G2z+UA3[1,3]*A2))/Sqrt[2]"
    ]},
    {"spin_type": "S", "class_index": 121, "class_name": "ChiL", "self_conjugate": false, "unphysical": true, "indices": ["SU2D"], "flavor_index": "SU2D", "quantum_numbers": {"Y": "1/2"}, "definitions": [
      "ChiL[1] -> -sbeta*Hp1+cbeta*GP",
      "ChiL[2] -> (vL+UH3[2,1]*H+UH3[2,2]*H2+UH3[2,3]*H3+I*(UA3[2,1]*G0+UA3[2,2]*G2z+UA3[2,3]*A2))/Sqrt[2]"
    ]},
    {"spin_type": "S", "class_index": 122, "class_name": "ChiR", "self_conjugate": false, "unphysical": true, "indices": ["SU2Rd"], "flavor_index": "SU2Rd", "quantum_numbers": {"Y": "1/2"}, "definitions": [
      "ChiR[1] -> -szeta*Hp2+czeta*G2p",
      "ChiR[2] -> (vR+UH3[3,1]*H+UH3[3,2]*H2+UH3[3,3]*H3+I*(UA3[3,1]*G0+UA3[3,2]*G2z+UA3[3,3]*A2))/Sqrt[2]"
    ]},
    {"spin_type": "S", "class_index": 123, "class_name": "h0new", "self_conjugate": true, "class_members": ["H2", "H3"], "mass": {"sym": "MHnew0", "members": [["MH2", "Internal"], ["MH3", "Internal"]]}, "width": {"massless": true}, "pdg": [45, 55], "particle_name": ["H2", "H3"], "full_name": ["Second CP-even Higgs", "Third CP-even Higgs"], "propagator_label": ["h0new", "H2", "H3"], "propagator_type": "D", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 1231, "class_name": "H1", "self_conjugate": true, "mass": {"sym": "MH1", "value": "Internal"}, "width": {"massless": true}, "pdg": 35, "particle_name": "H1", "full_name": "Lightest new CP-even Higgs", "propagator_label": "H1", "propagator_type": "D", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 124, "class_name": "A0new", "self_conjugate": true, "class_members": ["A1", "A2"], "mass": {"sym": "MAnew0", "members": [["MA1", "Internal"], ["MA2", "Internal"]]}, "width": {"massless": true}, "pdg": [36, 46], "particle_name": ["A1", "A2"], "full_name": ["Light pseudoscalar", "Heavy pseudoscalar"], "propagator_label": ["A0new", "A1", "A2"], "propagator_type": "D", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 125, "class_name": "Hpnew", "self_conjugate": false, "class_members": ["Hp1", "Hp2"], "mass": {"sym": "MHpnew", "members": [["MH1pm", "Internal"], ["MH2pm", "Internal"]]}, "width": {"massless": true}, "quantum_numbers": {"Q": "1"}, "pdg": [37, 47], "particle_name": ["Hp1", "Hp2"], "antiparticle_name": ["Hp1bar", "Hp2bar"], "full_name": ["Light charged Higgs", "Heavy charged Higgs"], "propagator_label": ["Hpnew", "Hp1", "Hp2"], "propagator_type": "D", "propagator_arrow": "Forward"},
    {"spin_type": "S", "class_index": 126, "class_name": "G2p", "self_conjugate": false, "goldstone": "Wp", "mass": {"sym": "MWp", "value": "Internal"}, "width": {"massless": true}, "quantum_numbers": {"Q": "1"}, "pdg": 252, "particle_name": "G2p", "antiparticle_name": "G2pbar", "full_name": "Wp Goldstone", "propagator_label": "G2p", "propagator_type": "D", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 127, "class_name": "G2z", "self_conjugate": true, "goldstone": "Zp", "mass": {"sym": "MZp", "value": "Internal"}, "width": {"massless": true}, "pdg": 253, "particle_name": "G2z", "full_name": "Zp Goldstone", "propagator_label": "G2z", "propagator_type": "D", "propagator_arrow": "None"},
    {"spin_type": "V", "class_index": 130, "class_name": "Zp", "self_conjugate": true, "mass": {"sym": "MZp", "value": "Internal"}, "width": {"sym": "WZp", "value": "50."}, "pdg": 32, "particle_name": "zp", "full_name": "Z prime", "propagator_label": "zp", "propagator_type": "Sine", "propagator_arrow": "None"},
    {"spin_type": "V", "class_index": 131, "class_name": "Wp", "self_conjugate": false, "mass": {"sym": "MWp", "value": "Internal"}, "width": {"sym": "WWp", "value": "10."}, "quantum_numbers": {"Q": "1"}, "pdg": 34, "particle_name": "wp+", "antiparticle_name": "wp-", "full_name": "W prime", "propagator_label": "wp", "propagator_type": "Sine", "propagator_arrow": "Forward"}
  ],
  "lagrangian_terms": [
    {"name": "LdqpKin", "delayed": true, "expression": "Block[{sp,sp2,mu,ff,cc}, ExpandIndices[I*dqpbar.Ga[mu].DC[dqp,mu] - dqpbar.Mdqpmat.dqp, FlavorExpand->{SU2W}]]"},
    {"name": "LnlKin", "delayed": true, "expression": "Block[{sp,mu,ff}, ExpandIndices[I*nlbar.Ga[mu].DC[nl,mu] - nlbar.Mnlmat.nl, FlavorExpand->{SU2W}]]"},
    {"name": "LZpKin", "delayed": true, "expression": "Block[{mu,nu}, -1/4*FS[Zp,mu,nu]*FS[Zp,mu,nu] + 1/2*MZp^2*Zp[mu]*Zp[mu]]"},
    {"name": "LWpKin", "delayed": true, "expression": "Block[{mu,nu}, -1/2*FS[Wpbar,mu,nu]*FS[Wp,mu,nu] + MWp^2*Wpbar[mu]*Wp[mu]]"},
    {"name": "LZZpMix", "delayed": true, "expression": "Block[{mu}, -dMZZp*Z[mu]*Zp[mu]]"},
    {"name": "LHiggsKinBD", "delayed": true, "expression": "Block[{ii,kk,mu}, ExpandIndices[DC[PhiBDbar[ii,kk],mu] DC[PhiBD[ii,kk],mu], FlavorExpand->{SU2D,SU2W}]]"},
    {"name": "LHiggsKinChiL", "delayed": true, "expression": "Block[{ii,mu}, ExpandIndices[DC[ChiLbar[ii],mu] DC[ChiL[ii],mu], FlavorExpand->{SU2D,SU2W}]]"},
    {"name": "LHiggsKinChiR", "delayed": true, "expression": "Block[{kk,mu}, DC[ChiRbar[kk],mu] DC[ChiR[kk],mu]]"},
    {"name": "LHpot", "delayed": true, "expression": "Block[{ii,ii2,ii3,jj,jj2,kk,kk2,ll,ll2}, -mu1sq*PhiBDbar[ii,kk]*PhiBD[ii,kk] - mu2sq*(ChiLbar[ii]*ChiL[ii]+ChiRbar[kk]*ChiR[kk]) + lam1*PhiBDbar[ii,kk]*PhiBD[ii,kk]*PhiBDbar[ii2,kk2]*PhiBD[ii2,kk2] + lam2*(Eps[ii,ii2]*Eps[kk,kk2]*PhiBD[ii,kk]*PhiBD[ii2,kk2])*(Eps[jj,jj2]*Eps[ll,ll2]*PhiBDbar[jj,ll]*PhiBDbar[jj2,ll2]) + lam3*((ChiLbar[ii]*ChiL[ii])^2+(ChiRbar[kk]*ChiR[kk])^2) + 2*lam4*(ChiLbar[ii]*ChiL[ii])*(ChiRbar[kk]*ChiR[kk]) + 2*alp1*(PhiBDbar[ii,kk]*PhiBD[ii,kk])*(ChiLbar[jj]*ChiL[jj]+ChiRbar[ll]*ChiR[ll]) + 2*alp2*(ChiLbar[ii]*PhiBD[ii,kk]*ChiL[ii2]*PhiBDbar[ii2,kk] + PhiBDbar[ii,kk]*ChiRbar[kk]*PhiBD[ii,kk2]*ChiR[kk2]) + 2*alp3*(ChiLbar[ii]*Eps[ii,jj]*PhiBDbar[jj,kk]*ChiL[ii2]*Eps[ii2,jj2]*PhiBD[jj2,kk] + Eps[kk,ll]*PhiBD[ii,kk]*ChiRbar[ll]*Eps[kk2,ll2]*PhiBDbar[ii,kk2]*ChiR[ll2]) + kap*(ChiLbar[ii]*PhiBD[ii,kk]*ChiR[kk]) + kap*(ChiRbar[kk]*PhiBDbar[ii,kk]*ChiL[ii])"},
    {"name": "LYukawaBSM", "delayed": true, "expression": "Block[{sp,ii,ii2,kk,kk2,jj,cc,ff1,ff2}, yuk = ExpandIndices[ YuBD[ff1,ff2]*QLbar[sp,ii,ff1,cc].QR[sp,kk,ff2,cc]*Eps[ii,ii2]*Eps[kk,kk2]*PhiBD[ii2,kk2] - YdBD[ff1,ff2]*QLbar[sp,ii,ff1,cc].dR[sp,ff2,cc]*ChiL[ii] - YdpBD[ff1,ff2]*QRbar[sp,kk,ff1,cc].dpL[sp,ff2,cc]*ChiR[kk] - YeBD[ff1,ff2]*LLbar[sp,ii,ff1].LR[sp,kk,ff2]*PhiBD[ii,kk] + YnuBD[ff1,ff2]*LLbar[sp,ii,ff1].nuR[sp,ff2]*ChiLbar[jj]*Eps[ii,jj] + YnBD[ff1,ff2]*LRbar[sp,kk,ff1].nlL[sp,ff2]*ChiRbar[jj]*Eps[kk,jj], FlavorExpand->{SU2D}]; yuk+HC[yuk]"},
    {"name": "LeffHVV", "delayed": true, "expression": "Block[{mu,nu,aa}, -1/4*Ghgg*H*FS[G,mu,nu,aa]*FS[G,mu,nu,aa] - 1/4*Ghaa*H*FS[A,mu,nu]*FS[A,mu,nu]]"},
    {"name": "LZpFcurrent", "delayed": true, "expression": "Block[{sp,mu,ff,cc}, gR*cphiW/2*Zp[mu]*( uqbar.Ga[mu].ProjP.uq - dqpbar.Ga[mu].ProjP.dqp + nlbar.Ga[mu].ProjP.nl - lbar.Ga[mu].ProjP.l )"},
    {"name": "LWpFcurrent", "delayed": true, "expression": "Block[{sp,mu,ff1,ff2,cc}, gR/Sqrt[2]*( Wp[mu]*(uqbar.Ga[mu].ProjP.VCKMp.dqp + nlbar.Ga[mu].ProjP.VPMNSp.l) + Wpbar[mu]*(dqpbar.Ga[mu].ProjP.HC[VCKMp].uq + lbar.Ga[mu].ProjP.HC[VPMNSp].nl) )"},
    {"name": "LTotal", "delayed": true, "expression": "LdqpKin + LnlKin + LZpKin + LWpKin + LZZpMix + LHiggsKinBD + LHiggsKinChiL + LHiggsKinChiR + LHpot + LYukawaBSM + LeffHVV + LZpFcurrent + LWpFcurrent"}
  ],
  "raw_preamble": [
    "(* ALRM_general add-on to SM.fr, extracted from arXiv:1911.12883. No reference/cached .fr file for this model was read; extraction used only the LaTeX source. *)",
    "(* Simplification note: SU(2)_R' x U(1)_{B-L} are NOT re-gauged via M$GaugeGroups; Zp and Wp are declared as independent massive vectors with simplified NC/CC current couplings (gR, cphiW/sphiW) rather than a full non-abelian construction and 3x3 A-Z-Zp rotation. *)",
    "(* UH3/UA3 row convention: row1=phi2^0, row2=chiL0, row3=chiR0; UH3 columns=(H,H2,H3), UA3 columns=(G0,G2z,A2), per Eqs.(A.4)-(A.5) of the source with an explicit row assignment chosen since the appendix text does not spell it out. *)",
    "(* MH1pm, MH2pm: paper writes M_{H1,2^+-} without an explicit square on the LHS while the RHS is dimensionally GeV^2; a Sqrt[...] was added to obtain a mass, and this choice is stated explicitly per the fraction/root rule. *)"
  ],
  "raw_blocks": []
}
```