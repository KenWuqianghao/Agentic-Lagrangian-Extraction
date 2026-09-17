## Self-audit table

Benchmark point used throughout: β = +1/√3 (one of the paper's four allowed values, Eq. 671/Table 1), giving the numeric charges Q_D=Q_S=−1/3, Q_T=+2/3, Q(E_ℓ)=0, Q_V=0, Q_Y=+1, Q(H^±)=1, Q(H^{Q_Y})=1, Q(H^{Q_V})=0 (Table "tbl:charge", β=1/√3 column). This choice is stated explicitly in the `beta` parameter Description.

Scope note: the 331 gauge group SU(3)_C×SU(3)_L×U(1)_X is **not** re-gauged inside the SM.fr add-on (schema rule: SM add-on ⇒ `gauge_groups: []`). The new heavy vectors Z′, Y, V are therefore implemented as free massive resonances per physics-completeness rule 1, with their masses set equal to the paper's own leading-order (decoupling-limit) formulas (Eqs. "gauge mass", "MVY"). The charged-current couplings of Y, V to the two SU(3)_L-triplet quark generations (q1L, q2L) are unambiguous and are included; the couplings involving the third quark generation and all lepton generations sit on SU(3)_L **anti-triplets**, whose vertex requires a charge-conjugated 4-component treatment (rule 3) that I could not independently re-derive with confidence from the text read — these are **omitted** from `lagrangian_terms` rather than guessed (their free kinetic+mass terms for T and E_e/E_μ/E_τ are still included).

| term | fields | d | coupling | coupling dim (4−d) | 1/Λ | Q sum | Y sum | SU(2) | SU(3) | new-U(1) | L/B | CC[] | frac/root check | HC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZp | FS[Zp]² (d=4); Zp·Zp (d=2) | 4 / 2 | 1 / MZp² | 0 / 2 | n/a | 0 (neutral) | 0 | singlet | singlet | n/a | n/a | n/a | MZp formula = Eq."gauge mass" (1/6(gW8+βgX X)²) | self-conj. |
| LYp | FS[Ypbar]FS[Yp] (d=4); Ypbar·Yp (d=2) | 4/2 | 1/MYp² | 0/2 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | MYp = Eq. MVY | HC via bar |
| LVp | analogous | 4/2 | 1/MVp² | 0/2 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | MVp = Eq. MVY | HC via bar |
| LDQ | DQbar Ga DC DQ (d=4); DQbar DQ (d=3) | 4/3 | 1/MDQ | 0/1 | n/a | 0 | 0 | singlet | triplet | n/a | B=1/3 (analog) | no | n/a (free External mass) | self-conj n/a |
| LSQ | as LDQ | 4/3 | 1/MSQ | 0/1 | n/a | 0 | 0 | singlet | triplet | n/a | 1/3 | no | n/a | – |
| LTQ | as LDQ | 4/3 | 1/MTQ | 0/1 | n/a | 0 | 0 | singlet | triplet | n/a | 1/3 | no | n/a | – |
| LEL | ELbar Ga DC EL (d=4); Eebar·Ee etc (d=3) | 4/3 | 1/MEE,MEM,MET | 0/1 | n/a | 0 | 0 | singlet | singlet | n/a | L=1 (analog) | no | n/a | – |
| LH2 | del H2 del H2 (d=4); H2² (d=2) | 4/2 | 1/MH2² | 0/2 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | MH2 = Eq.(4) | self-conj |
| LH3 | as LH2 | 4/2 | 1/MH3² | 0/2 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | MH3 = Eq.(5) | self-conj |
| LH0 | as LH2 | 4/2 | 1/MH0² | 0/2 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | MH0 = Sec 2.4 formula | self-conj |
| LHpm | DC Hpmbar DC Hpm (d=4); Hpmbar Hpm (d=2) | 4/2 | 1/MHpm² | 0/2 | n/a | 0 (+1−1) | 0 | singlet | singlet | n/a | n/a | n/a | MHpm = Eq. M²_{H±} | HC via bar |
| LHQY | analogous | 4/2 | 1/MHQY² | 0/2 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | MHQY = Eq. M²_{H^{QY}} | HC via bar |
| LHQV | analogous | 4/2 | 1/MHQV² | 0/2 | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | MHQV = Eq. M²_{H^{QV}} | HC via bar |
| LNPcc | ubar Ga ProjM DQ Yp (+cbar…SQ…Yp, dbar…DQ…Vp, sbar…SQ…Vp), d=4 each | 4 | 0 | gw/√2 (dimensionless) | n/a | u−D−Y: 2/3=−1/3+1 ✓; d−D−V: −1/3=−1/3+0 ✓; c−S−Y ✓; s−S−V ✓ | same | singlet (Yp,Vp not gauged) | colour-singlet (triplet·antitriplet) | n/a | conserved | no | n/a | HC[...] added |

- Kinetic+mass confirmation: every new class (Zp, Yp, Vp, DQ, SQ, TQ, EL, H2, H3, H0, Hpm, HQY, HQV) has its own named term above and each appears in `LTotal`.
- No non-fundamental colour representation is used (DQ, SQ, TQ are ordinary colour triplets) — no `AddGaugeRepresentation` needed.
- `SelfConjugate -> True` classes: Zp, H2, H3, H0 — none carries `QuantumNumbers`.
- Name check: Zp, Yp, Vp, DQ, SQ, TQ, EL, H2, H3, H0, Hpm, HQY, HQV, beta, gX, v1, v2, v3, k, f, lam3, lampr12, lampr23, lampr13, MZp, MYp, MVp, MH2, MH3, MH0, MHpm, MHQY, MHQV — none is a Mathematica built-in/FeynRules symbol (avoided bare D, E, S, T, Y, V) and none duplicates an SM.fr name.
- Single total: `LTotal` sums LZp+LYp+LVp+LDQ+LSQ+LTQ+LEL+LH2+LH3+LH0+LHpm+LHQY+LHQV+LNPcc.
- Reference/cached `.fr` file read: **none**.

```json
{
  "model_name": "331_gen",
  "info": {
    "authors": ["Qing-Hong Cao", "Dong-Ming Zhang"],
    "version": "1.0",
    "date": "2026-09-17",
    "institutions": ["Peking University"],
    "emails": ["qinghongcao@pku.edu.cn", "zhangdongming@pku.edu.cn"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "beta",
      "parameter_type": "External",
      "value": "0.5773502691896258",
      "block_name": "NPINPUTS",
      "order_block": 1,
      "description": "331-model beta parameter, benchmark choice beta=+1/Sqrt[3] (paper Sec. 2.5, Table tbl:charge); fixes new-particle electric charges Q_D=Q_S=-1/3, Q_T=2/3, Q_El=0, Q_V=0, Q_Y=1."
    },
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.5",
      "interaction_order": ["NP", 1],
      "block_name": "NPINPUTS",
      "order_block": 2,
      "description": "U(1)_X gauge coupling (paper Eq. Gmu, Dmu). Not fixed by the paper; benchmark perturbative default."
    },
    {
      "name": "v1",
      "parameter_type": "External",
      "value": "173.95",
      "block_name": "NPINPUTS",
      "order_block": 3,
      "description": "VEV of rho triplet [GeV] (paper Eq. after (1)); with v2 satisfies v1^2+v2^2=vev^2=246^2. Benchmark v1=v2 (decoupling-limit U11=U21=1/Sqrt[2])."
    },
    {
      "name": "v3",
      "parameter_type": "External",
      "value": "2000.",
      "block_name": "NPINPUTS",
      "order_block": 4,
      "description": "VEV of chi triplet [GeV], the SU(3)_L x U(1)_X breaking scale (paper Sec. 2.1); benchmark 2 TeV as used in Fig. chi2_1a."
    },
    {
      "name": "k",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NPINPUTS",
      "order_block": 5,
      "description": "O(1) proportionality constant in f = k*v3 (paper Sec. 2.1, below Eq. VHiggs)."
    },
    {
      "name": "lam3",
      "parameter_type": "External",
      "value": "0.1",
      "interaction_order": ["NP", 1],
      "block_name": "NPINPUTS",
      "order_block": 6,
      "description": "Quartic coupling lambda_3 (chi-dagger chi)^2 of the Higgs potential (paper Eq. VHiggs); sets M_H3^2=2*lam3*v3^2 (Eq. 5)."
    },
    {
      "name": "lampr12",
      "parameter_type": "External",
      "value": "0.1",
      "interaction_order": ["NP", 1],
      "block_name": "NPINPUTS",
      "order_block": 7,
      "description": "Quartic coupling lambda'_12 (rho-dagger eta)(eta-dagger rho) (paper Eq. VHiggs); enters M_H{+-}^2 (Eq. M^2_{H+-})."
    },
    {
      "name": "lampr23",
      "parameter_type": "External",
      "value": "0.1",
      "interaction_order": ["NP", 1],
      "block_name": "NPINPUTS",
      "order_block": 8,
      "description": "Quartic coupling lambda'_23 (eta-dagger chi)(chi-dagger eta) (paper Eq. VHiggs); enters M_H{QY}^2."
    },
    {
      "name": "lampr13",
      "parameter_type": "External",
      "value": "0.1",
      "interaction_order": ["NP", 1],
      "block_name": "NPINPUTS",
      "order_block": 9,
      "description": "Quartic coupling lambda'_13 (rho-dagger chi)(chi-dagger rho) (paper Eq. VHiggs); enters M_H{QV}^2."
    },
    {
      "name": "v2",
      "parameter_type": "Internal",
      "value": "Sqrt[vev^2 - v1^2]",
      "description": "VEV of eta triplet [GeV], fixed by v1^2+v2^2=vev^2=246^2 (paper, text after Eq. 5)."
    },
    {
      "name": "f",
      "parameter_type": "Internal",
      "value": "k*v3",
      "description": "Trilinear Higgs-potential coefficient f=k*v3 [GeV] (paper Sec. 2.1)."
    },
    {
      "name": "MZp",
      "parameter_type": "Internal",
      "value": "Sqrt[(gw^2 + beta^2*gX^2)*v3^2/6]",
      "description": "Z' mass, decoupling-limit formula from paper Eq. 'gauge mass' term (1/6)v3^2(-g W8+beta gX X)^2, with g=gw."
    },
    {
      "name": "MYp",
      "parameter_type": "Internal",
      "value": "Sqrt[gw^2*(v3^2+v2^2)/4]",
      "description": "Y boson mass (paper Eq. MVY: M^2_Y=(g^2/4)(v3^2+v2^2))."
    },
    {
      "name": "MVp",
      "parameter_type": "Internal",
      "value": "Sqrt[gw^2*(v3^2+v1^2)/4]",
      "description": "V boson mass (paper Eq. MVY: M^2_V=(g^2/4)(v3^2+v1^2))."
    },
    {
      "name": "MH2",
      "parameter_type": "Internal",
      "value": "Sqrt[(vev^2/(v1*v2))*f*v3]",
      "description": "Heavy CP-even scalar H2 mass (paper Eq. 4: M_H2^2=(v^2/(v1 v2)) f v3)."
    },
    {
      "name": "MH3",
      "parameter_type": "Internal",
      "value": "Sqrt[2*lam3*v3^2]",
      "description": "Heavy CP-even scalar H3 mass (paper Eq. 5: M_H3^2=2 lambda_3 v3^2)."
    },
    {
      "name": "MH0",
      "parameter_type": "Internal",
      "value": "Sqrt[(v1*v2/v3 + v1*v3/v2 + v2*v3/v1)*f]",
      "description": "CP-odd scalar H0 mass (paper Sec. 2.4: M^2_H0=(v1v2/v3+v1v3/v2+v2v3/v1) f)."
    },
    {
      "name": "MHpm",
      "parameter_type": "Internal",
      "value": "Sqrt[(2*f*v3 + lampr12*v1*v2)*vev^2/(2*v1*v2)]",
      "description": "Charged scalar H+- mass (paper Eq. M^2_{H+-}=(2 f v3+lambda'_12 v1 v2) v^2/(2 v1 v2))."
    },
    {
      "name": "MHQY",
      "parameter_type": "Internal",
      "value": "Sqrt[(2*f*v1 + lampr23*v2*v3)*(v2^2+v3^2)/(2*v2*v3)]",
      "description": "Charged scalar H^{+-QY} mass (paper Eq. M^2_{H^{QY}})."
    },
    {
      "name": "MHQV",
      "parameter_type": "Internal",
      "value": "Sqrt[(2*f*v2 + lampr13*v1*v3)*(v1^2+v3^2)/(2*v1*v3)]",
      "description": "Charged scalar H^{+-QV} mass (paper Eq. M^2_{H^{QV}})."
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 101,
      "class_name": "Zp",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MZp", "value": "Internal"},
      "width": {"sym": "WZp", "value": "Automatic"},
      "quantum_numbers": {},
      "pdg": 4000001,
      "particle_name": "Zp",
      "full_name": "Z-prime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 102,
      "class_name": "Yp",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MYp", "value": "Internal"},
      "width": {"sym": "WYp", "value": "Automatic"},
      "quantum_numbers": {"Q": "1"},
      "pdg": 4000002,
      "particle_name": "Yp+",
      "antiparticle_name": "Yp-",
      "full_name": "Y exotic charged gauge boson",
      "propagator_label": "Yp",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "V",
      "class_index": 103,
      "class_name": "Vp",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MVp", "value": "Internal"},
      "width": {"sym": "WVp", "value": "Automatic"},
      "quantum_numbers": {"Q": "0"},
      "pdg": 4000003,
      "particle_name": "Vp",
      "antiparticle_name": "Vp~",
      "full_name": "V exotic gauge boson",
      "propagator_label": "Vp",
      "propagator_type": "Sine",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "DQ",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MDQ", "value": "1000."},
      "width": {"sym": "WDQ", "value": "Automatic"},
      "quantum_numbers": {"Q": "-1/3", "Y": "-1/3"},
      "pdg": 4000004,
      "particle_name": "DQ",
      "antiparticle_name": "DQ~",
      "full_name": "Heavy down-type quark D",
      "propagator_label": "DQ",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 102,
      "class_name": "SQ",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MSQ", "value": "1000."},
      "width": {"sym": "WSQ", "value": "Automatic"},
      "quantum_numbers": {"Q": "-1/3", "Y": "-1/3"},
      "pdg": 4000005,
      "particle_name": "SQ",
      "antiparticle_name": "SQ~",
      "full_name": "Heavy down-type quark S",
      "propagator_label": "SQ",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 103,
      "class_name": "TQ",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MTQ", "value": "1000."},
      "width": {"sym": "WTQ", "value": "Automatic"},
      "quantum_numbers": {"Q": "2/3", "Y": "2/3"},
      "pdg": 4000006,
      "particle_name": "TQ",
      "antiparticle_name": "TQ~",
      "full_name": "Heavy up-type quark T",
      "propagator_label": "TQ",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 104,
      "class_name": "EL",
      "self_conjugate": false,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["Ee", "Emu", "Etau"],
      "mass": {"sym": "MEL", "members": [["MEE", "1000."], ["MEM", "1000."], ["MET", "1000."]]},
      "width": {"sym": "WEL", "members": [["WEE", "Automatic"], ["WEM", "Automatic"], ["WET", "Automatic"]]},
      "quantum_numbers": {"Q": "0", "Y": "0"},
      "pdg": [4000007, 4000008, 4000009],
      "particle_name": ["Ee", "Emu", "Etau"],
      "antiparticle_name": ["Ee~", "Emu~", "Etau~"],
      "full_name": ["Heavy charged lepton (electron partner)", "Heavy charged lepton (muon partner)", "Heavy charged lepton (tau partner)"],
      "propagator_label": ["EL", "Ee", "Emu", "Etau"],
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "H2",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MH2", "value": "Internal"},
      "width": {"sym": "WH2", "value": "Automatic"},
      "quantum_numbers": {},
      "pdg": 4000010,
      "particle_name": "H2",
      "full_name": "Heavy CP-even Higgs H2",
      "propagator_label": "H2",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "H3",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MH3", "value": "Internal"},
      "width": {"sym": "WH3", "value": "Automatic"},
      "quantum_numbers": {},
      "pdg": 4000011,
      "particle_name": "H3",
      "full_name": "Heavy CP-even Higgs H3",
      "propagator_label": "H3",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "H0",
      "self_conjugate": true,
      "indices": [],
      "mass": {"sym": "MH0", "value": "Internal"},
      "width": {"sym": "WH0", "value": "Automatic"},
      "quantum_numbers": {},
      "pdg": 4000012,
      "particle_name": "H0",
      "full_name": "CP-odd Higgs H0",
      "propagator_label": "H0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "Hpm",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MHpm", "value": "Internal"},
      "width": {"sym": "WHpm", "value": "Automatic"},
      "quantum_numbers": {"Q": "1", "Y": "1"},
      "pdg": 4000013,
      "particle_name": "Hp+",
      "antiparticle_name": "Hp-",
      "full_name": "Charged Higgs H+-",
      "propagator_label": "Hpm",
      "propagator_type": "D",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "HQY",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MHQY", "value": "Internal"},
      "width": {"sym": "WHQY", "value": "Automatic"},
      "quantum_numbers": {"Q": "1", "Y": "1"},
      "pdg": 4000014,
      "particle_name": "HQY+",
      "antiparticle_name": "HQY-",
      "full_name": "Charged Higgs H^{QY}",
      "propagator_label": "HQY",
      "propagator_type": "D",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "S",
      "class_index": 106,
      "class_name": "HQV",
      "self_conjugate": false,
      "indices": [],
      "mass": {"sym": "MHQV", "value": "Internal"},
      "width": {"sym": "WHQV", "value": "Automatic"},
      "quantum_numbers": {"Q": "0", "Y": "0"},
      "pdg": 4000015,
      "particle_name": "HQV",
      "antiparticle_name": "HQV~",
      "full_name": "Charged Higgs H^{QV}",
      "propagator_label": "HQV",
      "propagator_type": "D",
      "propagator_arrow": "Forward"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {"name": "LZp", "expression": "Block[{mu,nu}, -1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]", "delayed": true},
    {"name": "LYp", "expression": "Block[{mu,nu}, -1/2 FS[Ypbar,mu,nu] FS[Yp,mu,nu] + MYp^2 Ypbar[mu] Yp[mu]]", "delayed": true},
    {"name": "LVp", "expression": "Block[{mu,nu}, -1/2 FS[Vpbar,mu,nu] FS[Vp,mu,nu] + MVp^2 Vpbar[mu] Vp[mu]]", "delayed": true},
    {"name": "LDQ", "expression": "Block[{mu}, I DQbar.Ga[mu].DC[DQ,mu] - MDQ DQbar.DQ]", "delayed": true},
    {"name": "LSQ", "expression": "Block[{mu}, I SQbar.Ga[mu].DC[SQ,mu] - MSQ SQbar.SQ]", "delayed": true},
    {"name": "LTQ", "expression": "Block[{mu}, I TQbar.Ga[mu].DC[TQ,mu] - MTQ TQbar.TQ]", "delayed": true},
    {"name": "LEL", "expression": "Block[{mu}, I ELbar.Ga[mu].DC[EL,mu] - MEE Eebar.Ee - MEM Emubar.Emu - MET Etaubar.Etau]", "delayed": true},
    {"name": "LH2", "expression": "Block[{mu}, 1/2 del[H2,mu] del[H2,mu] - 1/2 MH2^2 H2^2]", "delayed": true},
    {"name": "LH3", "expression": "Block[{mu}, 1/2 del[H3,mu] del[H3,mu] - 1/2 MH3^2 H3^2]", "delayed": true},
    {"name": "LH0", "expression": "Block[{mu}, 1/2 del[H0,mu] del[H0,mu] - 1/2 MH0^2 H0^2]", "delayed": true},
    {"name": "LHpm", "expression": "Block[{mu}, DC[Hpmbar,mu] DC[Hpm,mu] - MHpm^2 Hpmbar Hpm]", "delayed": true},
    {"name": "LHQY", "expression": "Block[{mu}, DC[HQYbar,mu] DC[HQY,mu] - MHQY^2 HQYbar HQY]", "delayed": true},
    {"name": "LHQV", "expression": "Block[{mu}, DC[HQVbar,mu] DC[HQV,mu] - MHQV^2 HQVbar HQV]", "delayed": true},
    {"name": "LNPcc", "expression": "Block[{mu}, (gw/Sqrt[2]) (ubar.Ga[mu].ProjM.DQ Yp[mu] + cbar.Ga[mu].ProjM.SQ Yp[mu] + dbar.Ga[mu].ProjM.DQ Vp[mu] + sbar.Ga[mu].ProjM.SQ Vp[mu]) + HC[(gw/Sqrt[2]) (ubar.Ga[mu].ProjM.DQ Yp[mu] + cbar.Ga[mu].ProjM.SQ Yp[mu] + dbar.Ga[mu].ProjM.DQ Vp[mu] + sbar.Ga[mu].ProjM.SQ Vp[mu])]]", "delayed": true},
    {"name": "LTotal", "expression": "LZp + LYp + LVp + LDQ + LSQ + LTQ + LEL + LH2 + LH3 + LH0 + LHpm + LHQY + LHQV + LNPcc", "delayed": true}
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```