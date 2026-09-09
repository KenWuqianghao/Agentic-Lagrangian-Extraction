I read the paper's LaTeX source, the schema, the renderer and SM.fr. No reference or cached `.fr` file for this model exists in the sandbox, and none was read.

## Model content extracted (Sec. III, Eqs. (sFmodel), (sSmodel), Table X, Eq. (Jdef))

Four new weak-singlet colour-sextet states: scalars `Phi_u (6,1,1/3)`, `Phi_d (6,1,4/3)` with L = -1; Dirac fermions `Psi_u (6,1,-2/3)`, `Psi_d (6,1,1/3)` with L = 0. Clebsch-Gordan tensor `J^{s i a}` taken verbatim from Eq. (Jdef) (all 144 components, 29 non-zero).

## Mandatory self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4-d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L sum | CC[] used | fraction/root checked against | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LPhiuKin | DC[PhiUbar]DC[PhiU]; MPhiu^2 PhiUbar PhiU | 4 (mass piece 2) | 1; MPhiu^2 | 0; +2 | n/a | 1/3-1/3=0 | 1/3-1/3=0 | singlet (no SU(2) index) | 6 x 6bar, Sextet index auto-contracted | none | -1+1=0 | n/a | n/a | self-conjugate (real) |
| LPhidKin | DC[PhiDbar]DC[PhiD]; MPhid^2 PhiDbar PhiD | 4 (mass 2) | 1; MPhid^2 | 0; +2 | n/a | 4/3-4/3=0 | 4/3-4/3=0 | singlet | 6 x 6bar | none | -1+1=0 | n/a | n/a | self-conjugate |
| LPsiuKin | PsiUbar Ga DC[PsiU]; MPsiu PsiUbar.PsiU | 4 (mass 3) | 1; MPsiu | 0; +1 | n/a | -2/3+2/3=0 | -2/3+2/3=0 | singlet | 6 x 6bar | none | 0 | n/a | n/a | self-conjugate |
| LPsidKin | PsiDbar Ga DC[PsiD]; MPsid PsiDbar.PsiD | 4 (mass 3) | 1; MPsid | 0; +1 | n/a | 1/3-1/3=0 | 1/3-1/3=0 | singlet | 6 x 6bar | none | 0 | n/a | n/a | self-conjugate |
| LPsiuG | bar(u_R^c) sigma^{mu nu} PsiU G_{mu nu} | 5 | kapu/LamPsiu | -1 | 1/Λ^1 | +2/3-2/3+0=0 | +2/3-2/3=0 | singlet | Jsix[ss,ii,aa]: 6 x 3 x 8 | none | 0 | yes | Eq.(sFmodel) `\frac{1}{\Lambda_{\Psi_q}}`; Jsix from Eq.(Jdef) `\frac{1}{2}`,`\frac{1}{4}`,`\sqrt{2}`,`\sqrt{6}` | HC[tmp] |
| LPsidG | bar(d_R^c) sigma^{mu nu} PsiD G_{mu nu} | 5 | kapd/LamPsid | -1 | 1/Λ^1 | -1/3+1/3=0 | -1/3+1/3=0 | singlet | Jsix: 6 x 3 x 8 | none | 0 | yes | same LaTeX lines | HC[tmp] |
| LPsiuB | bar(u_R^c) PsiU B_{mu nu} G_{mu nu} | 7 | kapuB/LamPsiuB^3 | -3 | 1/Λ^3 | +2/3-2/3=0 | +2/3-2/3=0 | singlet | Jsix: 6 x 3 x 8 | none | 0 | yes | Eq.(sFmodel) `\frac{1}{\Lambda_{\Psi_{qB}}^3}` | HC[tmp] |
| LPsidB | bar(d_R^c) PsiD B_{mu nu} G_{mu nu} | 7 | kapdB/LamPsidB^3 | -3 | 1/Λ^3 | -1/3+1/3=0 | -1/3+1/3=0 | singlet | Jsix: 6 x 3 x 8 | none | 0 | yes | same | HC[tmp] |
| LPhiuL | PhiU bar(u_R^c) sigma^{mu nu} l_R G_{mu nu} | 6 | lamu/LamPhiu^2 | -2 | 1/Λ^2 | 1/3+2/3-1+0=0 | 1/3+2/3-1=0 | singlet (l_R, PhiU are SU(2) singlets) | Jsix: 6 x 3 x 8 | none | -1+0+1=0 | yes | Eq.(sSmodel) `\frac{1}{\Lambda^2_{\Phi_q}}` | HC[tmp] |
| LPhidL | PhiD bar(d_R^c) sigma^{mu nu} l_R G_{mu nu} | 6 | lamd/LamPhid^2 | -2 | 1/Λ^2 | 4/3-1/3-1=0 | 4/3-1/3-1=0 | singlet | Jsix: 6 x 3 x 8 | none | -1+0+1=0 | yes | same | HC[tmp] |

Per-class free-field rows: PhiU -> LPhiuKin, PhiD -> LPhidKin, PsiU -> LPsiuKin, PsiD -> LPsidKin; all four are in the LTotal sum.
Non-fundamental colour representation: `AddGaugeRepresentation[SU3C -> {T6, Sextet}];` is present in `raw_preamble`, together with `IndexRange[Index[Sextet]] = NoUnfold[Range[6]];`, and the `Sextet` entry is kept in `index_decls`.
SelfConjugate -> True classes: none. All four new classes are complex (distinct antiparticle), so the quantum-number restriction does not apply.
Names used: classes PhiU, PhiD, PsiU, PsiD; parameters Jsix, LamPsiu, LamPsid, LamPsiuB, LamPsidB, LamPhiu, LamPhid, kapu, kapd, kapuB, kapdB, lamu, lamd, MPhiu, MPhid, MPsiu, MPsid, WPhiu, WPhid, WPsiu, WPsid; index Sextet. None is a Mathematica built-in, a FeynRules symbol (HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM, Sig), or an SM.fr name (H, Phi, Z, W, A, G, B, lam, ee, gs, gw, sw, cw, vev, MZ, MW, Mu, Md, Ml, l, uq, dq, ...). No primes or punctuation in ParticleName/AntiParticleName.
Single total Lagrangian: `LTotal` = LPhiuKin + LPhidKin + LPsiuKin + LPsidKin + LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuL + LPhidL. No term is a pure constant.
Reference or cached model file read: none.

```json
{
  "model_name": "368sextets_gen",
  "info": {
    "authors": ["L. M. Carpenter", "T. Murphy", "T. M. P. Tait"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": ["The Ohio State University", "University of California, Irvine"],
    "emails": ["lmc@physics.osu.edu", "murphy.1573@osu.edu", "ttait@uci.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "raw_preamble": [
    "IndexRange[Index[Sextet]] = NoUnfold[Range[6]];",
    "AddGaugeRepresentation[SU3C -> {T6, Sextet}];"
  ],
  "index_decls": [
    {"name": "Sextet", "range_kind": "NoUnfold", "size": 6}
  ],
  "parameters": [
    {
      "name": "LamPsiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff of the dimension-5 up-type sextet fermion operator [GeV], Eq.(sFmodel), benchmark 1 TeV"
    },
    {
      "name": "LamPsid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 2,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff of the dimension-5 down-type sextet fermion operator [GeV], Eq.(sFmodel), benchmark 1 TeV"
    },
    {
      "name": "LamPsiuB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 3,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff of the dimension-7 up-type sextet fermion BG operator [GeV], Eq.(sFmodel), benchmark 1 TeV"
    },
    {
      "name": "LamPsidB",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 4,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff of the dimension-7 down-type sextet fermion BG operator [GeV], Eq.(sFmodel), benchmark 1 TeV"
    },
    {
      "name": "LamPhiu",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 5,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff of the dimension-6 up-type sextet scalar operator [GeV], Eq.(sSmodel), benchmark 1 TeV"
    },
    {
      "name": "LamPhid",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 6,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff of the dimension-6 down-type sextet scalar operator [GeV], Eq.(sSmodel), benchmark 1 TeV"
    },
    {
      "name": "kapu",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPAU",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapu[1]", "rhs": "0.05"},
        {"lhs": "kapu[2]", "rhs": "0.05"},
        {"lhs": "kapu[3]", "rhs": "0.05"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa_u^I of the sextet fermion Psiu to up-type quarks and a gluon, Eq.(sFmodel); benchmark 0.05 per generation"
    },
    {
      "name": "kapd",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPAD",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapd[1]", "rhs": "0.05"},
        {"lhs": "kapd[2]", "rhs": "0.05"},
        {"lhs": "kapd[3]", "rhs": "0.05"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa_d^I of the sextet fermion Psid to down-type quarks and a gluon, Eq.(sFmodel); benchmark 0.05 per generation"
    },
    {
      "name": "kapuB",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPAUB",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapuB[1]", "rhs": "0.10"},
        {"lhs": "kapuB[2]", "rhs": "0.10"},
        {"lhs": "kapuB[3]", "rhs": "0.10"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa_uB^I of Psiu to an up-type quark, a gluon and a hypercharge boson, Eq.(sFmodel); benchmark 0.10 per generation"
    },
    {
      "name": "kapdB",
      "parameter_type": "External",
      "complex": false,
      "block_name": "KAPPADB",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "kapdB[1]", "rhs": "0.10"},
        {"lhs": "kapdB[2]", "rhs": "0.10"},
        {"lhs": "kapdB[3]", "rhs": "0.10"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling kappa_dB^I of Psid to a down-type quark, a gluon and a hypercharge boson, Eq.(sFmodel); benchmark 0.10 per generation"
    },
    {
      "name": "lamu",
      "parameter_type": "External",
      "complex": false,
      "block_name": "LAMBDAU",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamu[1,1]", "rhs": "0.1"},
        {"lhs": "lamu[1,2]", "rhs": "0"},
        {"lhs": "lamu[1,3]", "rhs": "0"},
        {"lhs": "lamu[2,1]", "rhs": "0"},
        {"lhs": "lamu[2,2]", "rhs": "0.1"},
        {"lhs": "lamu[2,3]", "rhs": "0"},
        {"lhs": "lamu[3,1]", "rhs": "0"},
        {"lhs": "lamu[3,2]", "rhs": "0"},
        {"lhs": "lamu[3,3]", "rhs": "0.1"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling lambda_u^{XI} (X lepton generation, I quark generation) of Phiu to an up-type quark, a charged lepton and a gluon, Eq.(sSmodel); benchmark 0.1 times delta^{XI}"
    },
    {
      "name": "lamd",
      "parameter_type": "External",
      "complex": false,
      "block_name": "LAMBDAD",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "lamd[1,1]", "rhs": "0.1"},
        {"lhs": "lamd[1,2]", "rhs": "0"},
        {"lhs": "lamd[1,3]", "rhs": "0"},
        {"lhs": "lamd[2,1]", "rhs": "0"},
        {"lhs": "lamd[2,2]", "rhs": "0.1"},
        {"lhs": "lamd[2,3]", "rhs": "0"},
        {"lhs": "lamd[3,1]", "rhs": "0"},
        {"lhs": "lamd[3,2]", "rhs": "0"},
        {"lhs": "lamd[3,3]", "rhs": "0.1"}
      ],
      "interaction_order": ["NP", 1],
      "description": "Dimensionless coupling lambda_d^{XI} (X lepton generation, I quark generation) of Phid to a down-type quark, a charged lepton and a gluon, Eq.(sSmodel); benchmark 0.1 times delta^{XI}"
    },
    {
      "name": "Jsix",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Sextet", "Colour", "Gluon"],
      "value_rules": [
        {"lhs": "Jsix[1,1,1]", "rhs": "0"},
        {"lhs": "Jsix[1,1,2]", "rhs": "0"},
        {"lhs": "Jsix[1,1,3]", "rhs": "0"},
        {"lhs": "Jsix[1,1,4]", "rhs": "0"},
        {"lhs": "Jsix[1,1,5]", "rhs": "0"},
        {"lhs": "Jsix[1,1,6]", "rhs": "0"},
        {"lhs": "Jsix[1,1,7]", "rhs": "0"},
        {"lhs": "Jsix[1,1,8]", "rhs": "0"},
        {"lhs": "Jsix[1,2,1]", "rhs": "0"},
        {"lhs": "Jsix[1,2,2]", "rhs": "-I/2"},
        {"lhs": "Jsix[1,2,3]", "rhs": "0"},
        {"lhs": "Jsix[1,2,4]", "rhs": "0"},
        {"lhs": "Jsix[1,2,5]", "rhs": "1/2"},
        {"lhs": "Jsix[1,2,6]", "rhs": "0"},
        {"lhs": "Jsix[1,2,7]", "rhs": "0"},
        {"lhs": "Jsix[1,2,8]", "rhs": "0"},
        {"lhs": "Jsix[1,3,1]", "rhs": "I/2"},
        {"lhs": "Jsix[1,3,2]", "rhs": "0"},
        {"lhs": "Jsix[1,3,3]", "rhs": "0"},
        {"lhs": "Jsix[1,3,4]", "rhs": "-1/2"},
        {"lhs": "Jsix[1,3,5]", "rhs": "0"},
        {"lhs": "Jsix[1,3,6]", "rhs": "0"},
        {"lhs": "Jsix[1,3,7]", "rhs": "0"},
        {"lhs": "Jsix[1,3,8]", "rhs": "0"},
        {"lhs": "Jsix[2,1,1]", "rhs": "0"},
        {"lhs": "Jsix[2,1,2]", "rhs": "I*Sqrt[2]/4"},
        {"lhs": "Jsix[2,1,3]", "rhs": "0"},
        {"lhs": "Jsix[2,1,4]", "rhs": "0"},
        {"lhs": "Jsix[2,1,5]", "rhs": "-Sqrt[2]/4"},
        {"lhs": "Jsix[2,1,6]", "rhs": "0"},
        {"lhs": "Jsix[2,1,7]", "rhs": "0"},
        {"lhs": "Jsix[2,1,8]", "rhs": "0"},
        {"lhs": "Jsix[2,2,1]", "rhs": "0"},
        {"lhs": "Jsix[2,2,2]", "rhs": "0"},
        {"lhs": "Jsix[2,2,3]", "rhs": "-I*Sqrt[2]/4"},
        {"lhs": "Jsix[2,2,4]", "rhs": "0"},
        {"lhs": "Jsix[2,2,5]", "rhs": "0"},
        {"lhs": "Jsix[2,2,6]", "rhs": "Sqrt[2]/4"},
        {"lhs": "Jsix[2,2,7]", "rhs": "0"},
        {"lhs": "Jsix[2,2,8]", "rhs": "0"},
        {"lhs": "Jsix[2,3,1]", "rhs": "0"},
        {"lhs": "Jsix[2,3,2]", "rhs": "0"},
        {"lhs": "Jsix[2,3,3]", "rhs": "0"},
        {"lhs": "Jsix[2,3,4]", "rhs": "0"},
        {"lhs": "Jsix[2,3,5]", "rhs": "0"},
        {"lhs": "Jsix[2,3,6]", "rhs": "0"},
        {"lhs": "Jsix[2,3,7]", "rhs": "-I*Sqrt[2]/2"},
        {"lhs": "Jsix[2,3,8]", "rhs": "0"},
        {"lhs": "Jsix[3,1,1]", "rhs": "0"},
        {"lhs": "Jsix[3,1,2]", "rhs": "0"},
        {"lhs": "Jsix[3,1,3]", "rhs": "I/2"},
        {"lhs": "Jsix[3,1,4]", "rhs": "0"},
        {"lhs": "Jsix[3,1,5]", "rhs": "0"},
        {"lhs": "Jsix[3,1,6]", "rhs": "-1/2"},
        {"lhs": "Jsix[3,1,7]", "rhs": "0"},
        {"lhs": "Jsix[3,1,8]", "rhs": "0"},
        {"lhs": "Jsix[3,2,1]", "rhs": "0"},
        {"lhs": "Jsix[3,2,2]", "rhs": "0"},
        {"lhs": "Jsix[3,2,3]", "rhs": "0"},
        {"lhs": "Jsix[3,2,4]", "rhs": "0"},
        {"lhs": "Jsix[3,2,5]", "rhs": "0"},
        {"lhs": "Jsix[3,2,6]", "rhs": "0"},
        {"lhs": "Jsix[3,2,7]", "rhs": "0"},
        {"lhs": "Jsix[3,2,8]", "rhs": "0"},
        {"lhs": "Jsix[3,3,1]", "rhs": "-I/2"},
        {"lhs": "Jsix[3,3,2]", "rhs": "0"},
        {"lhs": "Jsix[3,3,3]", "rhs": "0"},
        {"lhs": "Jsix[3,3,4]", "rhs": "-1/2"},
        {"lhs": "Jsix[3,3,5]", "rhs": "0"},
        {"lhs": "Jsix[3,3,6]", "rhs": "0"},
        {"lhs": "Jsix[3,3,7]", "rhs": "0"},
        {"lhs": "Jsix[3,3,8]", "rhs": "0"},
        {"lhs": "Jsix[4,1,1]", "rhs": "0"},
        {"lhs": "Jsix[4,1,2]", "rhs": "0"},
        {"lhs": "Jsix[4,1,3]", "rhs": "0"},
        {"lhs": "Jsix[4,1,4]", "rhs": "0"},
        {"lhs": "Jsix[4,1,5]", "rhs": "0"},
        {"lhs": "Jsix[4,1,6]", "rhs": "0"},
        {"lhs": "Jsix[4,1,7]", "rhs": "I*Sqrt[2]/4"},
        {"lhs": "Jsix[4,1,8]", "rhs": "-I*Sqrt[6]/4"},
        {"lhs": "Jsix[4,2,1]", "rhs": "I*Sqrt[2]/4"},
        {"lhs": "Jsix[4,2,2]", "rhs": "0"},
        {"lhs": "Jsix[4,2,3]", "rhs": "0"},
        {"lhs": "Jsix[4,2,4]", "rhs": "Sqrt[2]/4"},
        {"lhs": "Jsix[4,2,5]", "rhs": "0"},
        {"lhs": "Jsix[4,2,6]", "rhs": "0"},
        {"lhs": "Jsix[4,2,7]", "rhs": "0"},
        {"lhs": "Jsix[4,2,8]", "rhs": "0"},
        {"lhs": "Jsix[4,3,1]", "rhs": "0"},
        {"lhs": "Jsix[4,3,2]", "rhs": "-I*Sqrt[2]/4"},
        {"lhs": "Jsix[4,3,3]", "rhs": "0"},
        {"lhs": "Jsix[4,3,4]", "rhs": "0"},
        {"lhs": "Jsix[4,3,5]", "rhs": "-Sqrt[2]/4"},
        {"lhs": "Jsix[4,3,6]", "rhs": "0"},
        {"lhs": "Jsix[4,3,7]", "rhs": "0"},
        {"lhs": "Jsix[4,3,8]", "rhs": "0"},
        {"lhs": "Jsix[5,1,1]", "rhs": "0"},
        {"lhs": "Jsix[5,1,2]", "rhs": "0"},
        {"lhs": "Jsix[5,1,3]", "rhs": "-I/2"},
        {"lhs": "Jsix[5,1,4]", "rhs": "0"},
        {"lhs": "Jsix[5,1,5]", "rhs": "0"},
        {"lhs": "Jsix[5,1,6]", "rhs": "-1/2"},
        {"lhs": "Jsix[5,1,7]", "rhs": "0"},
        {"lhs": "Jsix[5,1,8]", "rhs": "0"},
        {"lhs": "Jsix[5,2,1]", "rhs": "0"},
        {"lhs": "Jsix[5,2,2]", "rhs": "I/2"},
        {"lhs": "Jsix[5,2,3]", "rhs": "0"},
        {"lhs": "Jsix[5,2,4]", "rhs": "0"},
        {"lhs": "Jsix[5,2,5]", "rhs": "1/2"},
        {"lhs": "Jsix[5,2,6]", "rhs": "0"},
        {"lhs": "Jsix[5,2,7]", "rhs": "0"},
        {"lhs": "Jsix[5,2,8]", "rhs": "0"},
        {"lhs": "Jsix[5,3,1]", "rhs": "0"},
        {"lhs": "Jsix[5,3,2]", "rhs": "0"},
        {"lhs": "Jsix[5,3,3]", "rhs": "0"},
        {"lhs": "Jsix[5,3,4]", "rhs": "0"},
        {"lhs": "Jsix[5,3,5]", "rhs": "0"},
        {"lhs": "Jsix[5,3,6]", "rhs": "0"},
        {"lhs": "Jsix[5,3,7]", "rhs": "0"},
        {"lhs": "Jsix[5,3,8]", "rhs": "0"},
        {"lhs": "Jsix[6,1,1]", "rhs": "-I*Sqrt[2]/4"},
        {"lhs": "Jsix[6,1,2]", "rhs": "0"},
        {"lhs": "Jsix[6,1,3]", "rhs": "0"},
        {"lhs": "Jsix[6,1,4]", "rhs": "Sqrt[2]/4"},
        {"lhs": "Jsix[6,1,5]", "rhs": "0"},
        {"lhs": "Jsix[6,1,6]", "rhs": "0"},
        {"lhs": "Jsix[6,1,7]", "rhs": "0"},
        {"lhs": "Jsix[6,1,8]", "rhs": "0"},
        {"lhs": "Jsix[6,2,1]", "rhs": "0"},
        {"lhs": "Jsix[6,2,2]", "rhs": "0"},
        {"lhs": "Jsix[6,2,3]", "rhs": "0"},
        {"lhs": "Jsix[6,2,4]", "rhs": "0"},
        {"lhs": "Jsix[6,2,5]", "rhs": "0"},
        {"lhs": "Jsix[6,2,6]", "rhs": "0"},
        {"lhs": "Jsix[6,2,7]", "rhs": "I*Sqrt[2]/4"},
        {"lhs": "Jsix[6,2,8]", "rhs": "I*Sqrt[6]/4"},
        {"lhs": "Jsix[6,3,1]", "rhs": "0"},
        {"lhs": "Jsix[6,3,2]", "rhs": "0"},
        {"lhs": "Jsix[6,3,3]", "rhs": "I*Sqrt[2]/4"},
        {"lhs": "Jsix[6,3,4]", "rhs": "0"},
        {"lhs": "Jsix[6,3,5]", "rhs": "0"},
        {"lhs": "Jsix[6,3,6]", "rhs": "Sqrt[2]/4"},
        {"lhs": "Jsix[6,3,7]", "rhs": "0"},
        {"lhs": "Jsix[6,3,8]", "rhs": "0"}
      ],
      "description": "Clebsch-Gordan coefficients J^{s i a} joining a colour sextet, a colour triplet and a gluon into a singlet, Eq.(Jdef) of the paper appendix; dimensionless group-theory factor"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "PhiU",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhiu", "value": "1500."},
      "width": {"sym": "WPhiu", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3", "LeptonNumber": "-1"},
      "pdg": 9000001,
      "particle_name": "phiu",
      "antiparticle_name": "phiu~",
      "full_name": "Colour-sextet scalar coupling to up-type quarks",
      "propagator_label": "phiu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "PhiD",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPhid", "value": "1500."},
      "width": {"sym": "WPhid", "value": "1."},
      "quantum_numbers": {"Q": "4/3", "Y": "4/3", "LeptonNumber": "-1"},
      "pdg": 9000002,
      "particle_name": "phid",
      "antiparticle_name": "phid~",
      "full_name": "Colour-sextet scalar coupling to down-type quarks",
      "propagator_label": "phid",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "PsiU",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsiu", "value": "1500."},
      "width": {"sym": "WPsiu", "value": "1."},
      "quantum_numbers": {"Q": "-2/3", "Y": "-2/3"},
      "pdg": 9000003,
      "particle_name": "psiu",
      "antiparticle_name": "psiu~",
      "full_name": "Colour-sextet Dirac fermion coupling to up-type quarks",
      "propagator_label": "psiu",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    },
    {
      "spin_type": "F",
      "class_index": 101,
      "class_name": "PsiD",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MPsid", "value": "1500."},
      "width": {"sym": "WPsid", "value": "1."},
      "quantum_numbers": {"Q": "1/3", "Y": "1/3"},
      "pdg": 9000004,
      "particle_name": "psid",
      "antiparticle_name": "psid~",
      "full_name": "Colour-sextet Dirac fermion coupling to down-type quarks",
      "propagator_label": "psid",
      "propagator_type": "Straight",
      "propagator_arrow": "Forward"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LPhiuKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[DC[PhiUbar, mu] DC[PhiU, mu] - MPhiu^2 PhiUbar PhiU]]"
    },
    {
      "name": "LPhidKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[DC[PhiDbar, mu] DC[PhiD, mu] - MPhid^2 PhiDbar PhiD]]"
    },
    {
      "name": "LPsiuKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I PsiUbar.Ga[mu].DC[PsiU, mu] - MPsiu PsiUbar.PsiU]]"
    },
    {
      "name": "LPsidKin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[I PsiDbar.Ga[mu].DC[PsiD, mu] - MPsid PsiDbar.PsiD]]"
    },
    {
      "name": "LPsiuG",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, ss, aa, tmp}, tmp = ExpandIndices[1/LamPsiu kapu[ff] Jsix[ss, ii, aa] (CC[uqbar[ff, ii]].Sig[mu, nu].ProjP.PsiU[ss]) FS[G, mu, nu, aa]]; tmp + HC[tmp]]"
    },
    {
      "name": "LPsidG",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, ss, aa, tmp}, tmp = ExpandIndices[1/LamPsid kapd[ff] Jsix[ss, ii, aa] (CC[dqbar[ff, ii]].Sig[mu, nu].ProjP.PsiD[ss]) FS[G, mu, nu, aa]]; tmp + HC[tmp]]"
    },
    {
      "name": "LPsiuB",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, ss, aa, tmp}, tmp = ExpandIndices[1/LamPsiuB^3 kapuB[ff] Jsix[ss, ii, aa] (CC[uqbar[ff, ii]].ProjP.PsiU[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; tmp + HC[tmp]]"
    },
    {
      "name": "LPsidB",
      "delayed": true,
      "expression": "Block[{mu, nu, ff, ii, ss, aa, tmp}, tmp = ExpandIndices[1/LamPsidB^3 kapdB[ff] Jsix[ss, ii, aa] (CC[dqbar[ff, ii]].ProjP.PsiD[ss]) FS[B, mu, nu] FS[G, mu, nu, aa]]; tmp + HC[tmp]]"
    },
    {
      "name": "LPhiuL",
      "delayed": true,
      "expression": "Block[{mu, nu, ff1, ff2, ii, ss, aa, tmp}, tmp = ExpandIndices[1/LamPhiu^2 lamu[ff1, ff2] Jsix[ss, ii, aa] PhiU[ss] (CC[uqbar[ff2, ii]].Sig[mu, nu].ProjP.l[ff1]) FS[G, mu, nu, aa]]; tmp + HC[tmp]]"
    },
    {
      "name": "LPhidL",
      "delayed": true,
      "expression": "Block[{mu, nu, ff1, ff2, ii, ss, aa, tmp}, tmp = ExpandIndices[1/LamPhid^2 lamd[ff1, ff2] Jsix[ss, ii, aa] PhiD[ss] (CC[dqbar[ff2, ii]].Sig[mu, nu].ProjP.l[ff1]) FS[G, mu, nu, aa]]; tmp + HC[tmp]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LPhiuKin + LPhidKin + LPsiuKin + LPsidKin + LPsiuG + LPsidG + LPsiuB + LPsidB + LPhiuL + LPhidL"
    }
  ]
}
```