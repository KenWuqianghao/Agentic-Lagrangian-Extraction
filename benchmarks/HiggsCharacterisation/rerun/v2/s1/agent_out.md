I'll start by reading the paper and the schema.
I read the paper, the schema, the renderer, and SM.fr. No cached or reference `.fr` file for this model exists here, and none was read.

## Model content found in the paper

The Higgs Characterisation model adds **three** new bosonic states below the EWSB scale (§2): one spin-0 `X0` (a CP-mixed 0±, one field plus a mixing angle α — not two fields), one spin-1 `X1`, one spin-2 `X2`. All are colour, weak and electromagnetic singlets with mass ≈ 125 GeV, and all are real (self-conjugate). There are no multiplets, no new generations, and no new indices.

## Mandatory self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ power (=d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L/B | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LX0kin | del X0 · del X0 ; MX0²X0² | 4 | 1 ; MX0² | 0 ; 2 ✓ | n/a | 0 | n/a (mass eigenstates, no Y) | singlet | singlet | none | 0 | n/a | self-conj (real) |
| LX1kin | FS[X1]² ; MX1²X1X1 | 4 | 1 ; MX1² | 0 ; 2 ✓ | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | self-conj |
| LX2kin | (del X2)² ; MX2²X2X2 (Fierz–Pauli) | 4 | 1 ; MX2² | 0 ; 2 ✓ | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | self-conj |
| LX0ff | ψ̄f ψf X0 (t,b,τ) | 4 | cα κHff gHff, sα κAff gAff | 0 ✓ (gHff = mf/v) | n/a | −Qf+Qf+0=0 | n/a | singlet (mass eigenstates) | 3̄⊗3 singlet (t,b) | none | 0 | n/a | manifestly hermitian (real κ, i γ5 pair) |
| LX0VV (line 1) | Zμ Zμ X0 ; W+μ W−μ X0 | 3 | cα κSM gHZZ / gHWW | +1 ✓ (2M²/v) | n/a | 0 ; +1−1=0 | n/a | singlet | singlet | none | 0 | n/a | hermitian |
| LX0VV (γγ, Zγ, gg) | Aμν Aμν X0, Zμν Aμν X0, Gaμν Gaμν X0 (+duals) | 5 | κ·gHγγ etc. | −1 ✓ | absorbed in 1/v, **not** 1/Λ — paper's own choice (§2.1, Table 2: "we have chosen v as a reference scale instead of Λ"); Description records dim −1, GeV⁻¹ | 0 | n/a | singlet | δᵃᵇ | none | 0 | n/a | hermitian |
| LX0VV (κHZZ, κAZZ, κHWW, κAWW) | Vμν Vμν X0 | 5 | κ dimensionless | 0 ✓ | 1/Λ¹ present ✓ (External `Lam`, 1000 GeV) | 0 ; +1−1=0 | n/a | singlet | singlet | none | 0 | n/a | hermitian |
| LX0VV (derivative line) | Zν ∂μAμν X0, Zν ∂μZμν X0, W+ν ∂μW−μν X0 | 5 | κH∂γ, κH∂Z, κH∂W (complex) | 0 ✓ | 1/Λ¹ ✓ | 0 ; +1−1=0 | n/a | singlet | singlet | none | 0 | n/a | explicit `Conjugate[kHdw]` h.c. partner written |
| LX1ff | ψ̄f γμ(…)ψf X1μ (q, ℓ) | 4 | κfa af, κfb bf | 0 ✓ | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | hermitian |
| LX1WW | W+μν W−μ X1ν ; W+μW−νX1μν ; W+μW−ν∂X1 ; W+W−X̃1 ; ε W ∂W X1 | 4 | κW1..κW5 (κW1,2 × gWWZ) | 0 ✓ | n/a | +1−1+0=0 | n/a | singlet | singlet | none | 0 | n/a | hermitian (W+/W− paired) |
| LX1ZZ | Zμν Zμ X1ν ; X1μ(∂νZμ)Zν ; ε X1 Z ∂Z | 4 | κZ1, κZ3, κZ5 | 0 ✓ | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | hermitian |
| LX2q, LX2l | T^f_μν X2^μν | 5 | κq, κℓ | 0 ✓ | 1/Λ¹ ✓ | 0 | n/a | singlet | 3̄⊗3 singlet | none | 0 | n/a | hermitian |
| LX2a, LX2z, LX2w, LX2g | T^V_μν X2^μν | 5 | κγ, κZ, κW, κg | 0 ✓ | 1/Λ¹ ✓ | 0 (W+W− paired) | n/a | singlet | δᵃᵇ | none | 0 | n/a | hermitian |
| kinetic+mass present? | X0 → LX0kin ✓, X1 → LX1kin ✓, X2 → LX2kin ✓ | — | — | — | — | — | — | — | — | — | — | — | all three are in the `LHC` sum |

`SelfConjugate -> True` classes: **X0, X1, X2** — none carries `QuantumNumbers` (all are Q = 0 colour/weak singlets).

Reference or cached model file read: **none**. Only the paper, `frmodel.py`, `render.py` and `SM.fr` were opened.

Note on Y: the paper builds the effective lagrangian *below* EWSB, in terms of mass eigenstates (γ, Z, W±, quarks, leptons). SM.fr puts `Y` only on the unphysical chiral fields, so hypercharge is not a quantum number of any field in these terms; the Q sums are the applicable check and all are zero.

```json
{
  "model_name": "HiggsCharacterisation_gen",
  "info": {
    "authors": [
      "P. Artoisenet", "P. de Aquino", "F. Demartin", "R. Frederix", "S. Frixione",
      "F. Maltoni", "M. K. Mandal", "P. Mathews", "K. Mawatari", "V. Ravindran",
      "S. Seth", "P. Torrielli", "M. Zaro"
    ],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["Nikhef", "Vrije Universiteit Brussel", "UCLouvain (CP3)", "CERN", "HRI Allahabad", "SINP Kolkata", "IMSc Chennai", "Universitaet Zuerich"],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Lam",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff scale [GeV], Table 1 of arXiv:1306.6464 (reference value 10^3 GeV)"
    },
    {
      "name": "cosa",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 1,
      "tex": "c_{\\alpha}",
      "description": "cos(alpha), CP mixing between the 0+ and 0- components of X0, Eq.(2.3)"
    },
    {
      "name": "kSM",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 2,
      "description": "kappa_SM, dimensionless rescaling of the SM-like X0 Z Z / X0 W W couplings, Eq.(2.4)"
    },
    {
      "name": "kHtt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 3,
      "description": "kappa_Htt, dimensionless scalar coupling of X0 to the top quark, Eq.(2.2)"
    },
    {
      "name": "kAtt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 4,
      "description": "kappa_Att, dimensionless pseudoscalar coupling of X0 to the top quark, Eq.(2.2)"
    },
    {
      "name": "kHbb",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 5,
      "description": "kappa_Hbb, dimensionless scalar coupling of X0 to the bottom quark, Eq.(2.2)"
    },
    {
      "name": "kAbb",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 6,
      "description": "kappa_Abb, dimensionless pseudoscalar coupling of X0 to the bottom quark, Eq.(2.2)"
    },
    {
      "name": "kHll",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 7,
      "description": "kappa_Htautau, dimensionless scalar coupling of X0 to the tau lepton, Eq.(2.2)"
    },
    {
      "name": "kAll",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 8,
      "description": "kappa_Atautau, dimensionless pseudoscalar coupling of X0 to the tau lepton, Eq.(2.2)"
    },
    {
      "name": "kHaa",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 9,
      "description": "kappa_Hgammagamma, dimensionless, multiplies the loop-induced gHaa, Eq.(2.4)"
    },
    {
      "name": "kAaa",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 10,
      "description": "kappa_Agammagamma, dimensionless, multiplies the loop-induced gAaa, Eq.(2.4)"
    },
    {
      "name": "kHza",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 11,
      "description": "kappa_HZgamma, dimensionless, multiplies the loop-induced gHza, Eq.(2.4)"
    },
    {
      "name": "kAza",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 12,
      "description": "kappa_AZgamma, dimensionless, multiplies the loop-induced gAza, Eq.(2.4)"
    },
    {
      "name": "kHgg",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 13,
      "description": "kappa_Hgg, dimensionless, multiplies the loop-induced gHgg, Eq.(2.4)"
    },
    {
      "name": "kAgg",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 14,
      "description": "kappa_Agg, dimensionless, multiplies the loop-induced gAgg, Eq.(2.4)"
    },
    {
      "name": "kHzz",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 15,
      "description": "kappa_HZZ, dimensionless coefficient of the dim-5 operator Zmn Zmn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kAzz",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 16,
      "description": "kappa_AZZ, dimensionless coefficient of the dim-5 operator Zmn ZDualmn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHww",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 17,
      "description": "kappa_HWW, dimensionless coefficient of the dim-5 operator W+mn W-mn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kAww",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 18,
      "description": "kappa_AWW, dimensionless coefficient of the dim-5 operator W+mn W-Dualmn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHda",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 19,
      "description": "kappa_Hdgamma, dimensionless coefficient of the derivative operator Zn dm Amn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHdz",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 20,
      "description": "kappa_HdZ, dimensionless coefficient of the derivative operator Zn dm Zmn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHdwR",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 21,
      "description": "Real part of kappa_HdW, the only complex kappa, derivative operator W+n dm W-mn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHdwI",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 22,
      "description": "Imaginary part of kappa_HdW, the only complex kappa, Eq.(2.4)"
    },
    {
      "name": "kqa",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 1,
      "description": "kappa_qa, dimensionless vector coupling of X1 to quarks, Eq.(2.8); zero for a 1+ state, Eq.(2.14)"
    },
    {
      "name": "kqb",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 2,
      "description": "kappa_qb, dimensionless axial coupling of X1 to quarks, Eq.(2.8); zero for a 1- state, Eq.(2.13)"
    },
    {
      "name": "kla",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 3,
      "description": "kappa_la, dimensionless vector coupling of X1 to leptons, Eq.(2.8)"
    },
    {
      "name": "klb",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 4,
      "description": "kappa_lb, dimensionless axial coupling of X1 to leptons, Eq.(2.8)"
    },
    {
      "name": "kw1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 5,
      "description": "kappa_W1, dimensionless X1 W W coupling, first term of Eq.(2.11)"
    },
    {
      "name": "kw2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 6,
      "description": "kappa_W2, dimensionless X1 W W coupling, second term of Eq.(2.11)"
    },
    {
      "name": "kw3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 7,
      "description": "kappa_W3, dimensionless X1 W W coupling, third term of Eq.(2.11)"
    },
    {
      "name": "kw4",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "SPINONE",
      "order_block": 8,
      "description": "kappa_W4, dimensionless CP-odd X1 W W coupling, fourth term of Eq.(2.11)"
    },
    {
      "name": "kw5",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "SPINONE",
      "order_block": 9,
      "description": "kappa_W5, dimensionless CP-odd X1 W W coupling, fifth term of Eq.(2.11)"
    },
    {
      "name": "kz1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 10,
      "description": "kappa_Z1, dimensionless X1 Z Z coupling, first term of Eq.(2.12)"
    },
    {
      "name": "kz3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 11,
      "description": "kappa_Z3, dimensionless X1 Z Z coupling, second term of Eq.(2.12)"
    },
    {
      "name": "kz5",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "SPINONE",
      "order_block": 12,
      "description": "kappa_Z5, dimensionless CP-odd X1 Z Z coupling, third term of Eq.(2.12)"
    },
    {
      "name": "k2q",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 1,
      "description": "kappa_q, dimensionless coupling of X2 to the quark energy-momentum tensor, Eqs.(2.15) and (4.1)"
    },
    {
      "name": "k2l",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 2,
      "description": "kappa_l, dimensionless coupling of X2 to the lepton energy-momentum tensor, Eq.(2.15)"
    },
    {
      "name": "k2z",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 3,
      "description": "kappa_Z, dimensionless coupling of X2 to the Z energy-momentum tensor, Eq.(2.16)"
    },
    {
      "name": "k2w",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 4,
      "description": "kappa_W, dimensionless coupling of X2 to the W energy-momentum tensor, Eq.(2.16)"
    },
    {
      "name": "k2a",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 5,
      "description": "kappa_gamma, dimensionless coupling of X2 to the photon energy-momentum tensor, Eqs.(2.16) and (2.18)"
    },
    {
      "name": "k2g",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 6,
      "description": "kappa_g, dimensionless coupling of X2 to the gluon energy-momentum tensor, Eqs.(2.16) and (4.1)"
    },
    {
      "name": "sina",
      "parameter_type": "Internal",
      "value": "Sqrt[1 - cosa^2]",
      "tex": "s_{\\alpha}",
      "description": "sin(alpha), CP-mixing angle of the spin-0 state, Eq.(2.3)"
    },
    {
      "name": "kHdw",
      "parameter_type": "Internal",
      "value": "kHdwR + I kHdwI",
      "complex": true,
      "description": "Complex kappa_HdW = kHdwR + I kHdwI, Eq.(2.4); the only kappa that cannot be taken real"
    },
    {
      "name": "gHtt",
      "parameter_type": "Internal",
      "value": "MT/vev",
      "interaction_order": ["QED", 1],
      "description": "= mt/v, dimensionless SM-like scalar top coupling strength, Table 2"
    },
    {
      "name": "gAtt",
      "parameter_type": "Internal",
      "value": "MT/vev",
      "interaction_order": ["QED", 1],
      "description": "= mt/v, dimensionless pseudoscalar top coupling strength (2HDM with tan(beta)=1), Table 2"
    },
    {
      "name": "gHbb",
      "parameter_type": "Internal",
      "value": "MB/vev",
      "interaction_order": ["QED", 1],
      "description": "= mb/v, dimensionless SM-like scalar bottom coupling strength, Table 2"
    },
    {
      "name": "gAbb",
      "parameter_type": "Internal",
      "value": "MB/vev",
      "interaction_order": ["QED", 1],
      "description": "= mb/v, dimensionless pseudoscalar bottom coupling strength, Table 2"
    },
    {
      "name": "gHll",
      "parameter_type": "Internal",
      "value": "MTA/vev",
      "interaction_order": ["QED", 1],
      "description": "= mtau/v, dimensionless SM-like scalar tau coupling strength, Table 2"
    },
    {
      "name": "gAll",
      "parameter_type": "Internal",
      "value": "MTA/vev",
      "interaction_order": ["QED", 1],
      "description": "= mtau/v, dimensionless pseudoscalar tau coupling strength, Table 2"
    },
    {
      "name": "gHzz",
      "parameter_type": "Internal",
      "value": "2 MZ^2/vev",
      "interaction_order": ["QED", 1],
      "description": "= 2 MZ^2/v, mass dimension +1, units GeV, SM-like X0 Z Z coupling, Table 2"
    },
    {
      "name": "gHww",
      "parameter_type": "Internal",
      "value": "2 MW^2/vev",
      "interaction_order": ["QED", 1],
      "description": "= 2 MW^2/v, mass dimension +1, units GeV, SM-like X0 W W coupling, Table 2"
    },
    {
      "name": "gHaa",
      "parameter_type": "Internal",
      "value": "47 aEW/(18 Pi vev)",
      "interaction_order": ["QED", 3],
      "description": "= 47 alphaEM/(18 Pi v), mass dimension -1, units GeV^-1; Table 2 uses v, not Lam, as the reference scale because this operator is loop-induced already in the SM"
    },
    {
      "name": "gAaa",
      "parameter_type": "Internal",
      "value": "4 aEW/(3 Pi vev)",
      "interaction_order": ["QED", 3],
      "description": "= 4 alphaEM/(3 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "Cza",
      "parameter_type": "Internal",
      "value": "Sqrt[aEW Gf MZ^2/(8 Sqrt[2] Pi)]",
      "description": "C = Sqrt[alphaEM GF MZ^2/(8 Sqrt[2] Pi)], dimensionless constant of Table 2"
    },
    {
      "name": "gHza",
      "parameter_type": "Internal",
      "value": "Cza (94 cw^2 - 13)/(9 Pi vev)",
      "interaction_order": ["QED", 3],
      "description": "= C (94 cos^2(thetaW) - 13)/(9 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "gAza",
      "parameter_type": "Internal",
      "value": "2 Cza (8 cw^2 - 5)/(3 Pi vev)",
      "interaction_order": ["QED", 3],
      "description": "= 2 C (8 cos^2(thetaW) - 5)/(3 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "gHgg",
      "parameter_type": "Internal",
      "value": "-aS/(3 Pi vev)",
      "interaction_order": ["QCD", 2],
      "description": "= -alphaS/(3 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "gAgg",
      "parameter_type": "Internal",
      "value": "aS/(2 Pi vev)",
      "interaction_order": ["QCD", 2],
      "description": "= alphaS/(2 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "gWWZ",
      "parameter_type": "Internal",
      "value": "-ee cw/sw",
      "interaction_order": ["QED", 1],
      "description": "gWWZ = -e cot(thetaW), dimensionless, below Eq.(2.11)"
    },
    {
      "name": "aQu",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) (1/2 - 4/3 sw^2)",
      "interaction_order": ["QED", 1],
      "description": "a_u, SM vector coupling of up-type quarks, Eq.(2.9), dimensionless"
    },
    {
      "name": "bQu",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "b_u, SM axial coupling of up-type quarks, Eq.(2.9), dimensionless"
    },
    {
      "name": "aQd",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) (-1/2 + 2/3 sw^2)",
      "interaction_order": ["QED", 1],
      "description": "a_d, SM vector coupling of down-type quarks, Eq.(2.10), dimensionless"
    },
    {
      "name": "bQd",
      "parameter_type": "Internal",
      "value": "-gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "b_d, SM axial coupling of down-type quarks, Eq.(2.10), dimensionless"
    },
    {
      "name": "aLl",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) (-1/2 + 2 sw^2)",
      "interaction_order": ["QED", 1],
      "description": "a_l, SM vector coupling of charged leptons, Eqs.(2.9)-(2.10) applied to leptons, dimensionless"
    },
    {
      "name": "bLl",
      "parameter_type": "Internal",
      "value": "-gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "b_l, SM axial coupling of charged leptons, dimensionless"
    },
    {
      "name": "aLv",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "a_nu, SM vector coupling of neutrinos, dimensionless"
    },
    {
      "name": "bLv",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "b_nu, SM axial coupling of neutrinos, dimensionless"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "X0",
      "self_conjugate": true,
      "mass": { "sym": "MX0", "value": "125." },
      "width": { "sym": "WX0", "value": "0.00407" },
      "quantum_numbers": {},
      "pdg": 5000000,
      "particle_name": "x0",
      "full_name": "X0 spin-0 resonance",
      "propagator_label": "X0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "X1",
      "self_conjugate": true,
      "mass": { "sym": "MX1", "value": "125." },
      "width": { "sym": "WX1", "value": "0.00407" },
      "quantum_numbers": {},
      "pdg": 5000001,
      "particle_name": "x1",
      "full_name": "X1 spin-1 resonance",
      "propagator_label": "X1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "T",
      "class_index": 100,
      "class_name": "X2",
      "self_conjugate": true,
      "mass": { "sym": "MX2", "value": "125." },
      "width": { "sym": "WX2", "value": "0.00407" },
      "quantum_numbers": {},
      "pdg": 5000002,
      "particle_name": "x2",
      "full_name": "X2 spin-2 resonance",
      "propagator_label": "X2",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "raw_blocks": [],
  "lagrangian_terms": [
    {
      "name": "LX0kin",
      "delayed": true,
      "expression": "Block[{mu}, 1/2 del[X0, mu] del[X0, mu] - 1/2 MX0^2 X0^2]"
    },
    {
      "name": "LX1kin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[X1, mu, nu] FS[X1, mu, nu] + 1/2 MX1^2 X1[mu] X1[mu]]"
    },
    {
      "name": "LX2kin",
      "delayed": true,
      "expression": "Block[{mu, nu, ro}, -1/2 del[X2[mu, nu], ro] del[X2[mu, nu], ro] + del[X2[mu, nu], mu] del[X2[ro, nu], ro] - del[X2[mu, nu], mu] del[X2[ro, ro], nu] + 1/2 del[X2[mu, mu], ro] del[X2[nu, nu], ro] - 1/2 MX2^2 (X2[mu, nu] X2[mu, nu] - X2[mu, mu] X2[nu, nu])]"
    },
    {
      "name": "LX0ff",
      "delayed": true,
      "expression": "Block[{}, - ( cosa kHtt gHtt tbar.t + I sina kAtt gAtt tbar.Ga[5].t + cosa kHbb gHbb bbar.b + I sina kAbb gAbb bbar.Ga[5].b + cosa kHll gHll tabar.ta + I sina kAll gAll tabar.Ga[5].ta ) X0]"
    },
    {
      "name": "LX0VV",
      "delayed": true,
      "expression": "Block[{mu, nu, aa}, ( cosa kSM ( 1/2 gHzz Z[mu] Z[mu] + gHww W[mu] Wbar[mu] ) - 1/4 ( cosa kHaa gHaa FS[A, mu, nu] FS[A, mu, nu] + sina kAaa gAaa FS[A, mu, nu] FSDual[A, mu, nu] ) - 1/2 ( cosa kHza gHza FS[Z, mu, nu] FS[A, mu, nu] + sina kAza gAza FS[Z, mu, nu] FSDual[A, mu, nu] ) - 1/4 ( cosa kHgg gHgg FS[G, mu, nu, aa] FS[G, mu, nu, aa] + sina kAgg gAgg FS[G, mu, nu, aa] FSDual[G, mu, nu, aa] ) - 1/(4 Lam) ( cosa kHzz FS[Z, mu, nu] FS[Z, mu, nu] + sina kAzz FS[Z, mu, nu] FSDual[Z, mu, nu] ) - 1/(2 Lam) ( cosa kHww FS[W, mu, nu] FS[Wbar, mu, nu] + sina kAww FS[W, mu, nu] FSDual[Wbar, mu, nu] ) - cosa/Lam ( kHda Z[nu] del[FS[A, mu, nu], mu] + kHdz Z[nu] del[FS[Z, mu, nu], mu] + kHdw W[nu] del[FS[Wbar, mu, nu], mu] + Conjugate[kHdw] Wbar[nu] del[FS[W, mu, nu], mu] ) ) X0]"
    },
    {
      "name": "LX1ff",
      "delayed": true,
      "expression": "Block[{mu}, ( kqa aQu uqbar.Ga[mu].uq - kqb bQu uqbar.Ga[mu].Ga[5].uq + kqa aQd dqbar.Ga[mu].dq - kqb bQd dqbar.Ga[mu].Ga[5].dq + kla aLl lbar.Ga[mu].l - klb bLl lbar.Ga[mu].Ga[5].l + kla aLv vlbar.Ga[mu].vl - klb bLv vlbar.Ga[mu].Ga[5].vl ) X1[mu]]"
    },
    {
      "name": "LX1WW",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, I kw1 gWWZ ( FS[W, mu, nu] Wbar[mu] - FS[Wbar, mu, nu] W[mu] ) X1[nu] + I kw2 gWWZ W[mu] Wbar[nu] FS[X1, mu, nu] - kw3 W[mu] Wbar[nu] ( del[X1[nu], mu] + del[X1[mu], nu] ) + I kw4 W[mu] Wbar[nu] FSDual[X1, mu, nu] - kw5 Eps[mu, nu, ro, si] ( W[mu] del[Wbar[nu], ro] - del[W[mu], ro] Wbar[nu] ) X1[si]]"
    },
    {
      "name": "LX1ZZ",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, - kz1 FS[Z, mu, nu] Z[mu] X1[nu] - kz3 X1[mu] del[Z[mu], nu] Z[nu] - kz5 Eps[mu, nu, ro, si] X1[mu] Z[nu] del[Z[si], ro]]"
    },
    {
      "name": "LX2q",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, sp, ff, cc}, - k2q/Lam X2[mu, nu] ( - ME[mu, nu] ( I uqbar.Ga[ro].DC[uq, ro] - Mu[ff] uqbar[sp, ff, cc].uq[sp, ff, cc] - I/2 ( del[uqbar, ro].Ga[ro].uq + uqbar.Ga[ro].del[uq, ro] ) ) + I/2 uqbar.Ga[mu].DC[uq, nu] + I/2 uqbar.Ga[nu].DC[uq, mu] - I/4 ( del[uqbar, mu].Ga[nu].uq + uqbar.Ga[nu].del[uq, mu] ) - I/4 ( del[uqbar, nu].Ga[mu].uq + uqbar.Ga[mu].del[uq, nu] ) ) - k2q/Lam X2[mu, nu] ( - ME[mu, nu] ( I dqbar.Ga[ro].DC[dq, ro] - Md[ff] dqbar[sp, ff, cc].dq[sp, ff, cc] - I/2 ( del[dqbar, ro].Ga[ro].dq + dqbar.Ga[ro].del[dq, ro] ) ) + I/2 dqbar.Ga[mu].DC[dq, nu] + I/2 dqbar.Ga[nu].DC[dq, mu] - I/4 ( del[dqbar, mu].Ga[nu].dq + dqbar.Ga[nu].del[dq, mu] ) - I/4 ( del[dqbar, nu].Ga[mu].dq + dqbar.Ga[mu].del[dq, nu] ) )]"
    },
    {
      "name": "LX2l",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, sp, ff}, - k2l/Lam X2[mu, nu] ( - ME[mu, nu] ( I lbar.Ga[ro].DC[l, ro] - Ml[ff] lbar[sp, ff].l[sp, ff] - I/2 ( del[lbar, ro].Ga[ro].l + lbar.Ga[ro].del[l, ro] ) ) + I/2 lbar.Ga[mu].DC[l, nu] + I/2 lbar.Ga[nu].DC[l, mu] - I/4 ( del[lbar, mu].Ga[nu].l + lbar.Ga[nu].del[l, mu] ) - I/4 ( del[lbar, nu].Ga[mu].l + lbar.Ga[mu].del[l, nu] ) ) - k2l/Lam X2[mu, nu] ( - ME[mu, nu] ( I vlbar.Ga[ro].DC[vl, ro] - I/2 ( del[vlbar, ro].Ga[ro].vl + vlbar.Ga[ro].del[vl, ro] ) ) + I/2 vlbar.Ga[mu].DC[vl, nu] + I/2 vlbar.Ga[nu].DC[vl, mu] - I/4 ( del[vlbar, mu].Ga[nu].vl + vlbar.Ga[nu].del[vl, mu] ) - I/4 ( del[vlbar, nu].Ga[mu].vl + vlbar.Ga[mu].del[vl, nu] ) )]"
    },
    {
      "name": "LX2a",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, - k2a/Lam X2[mu, nu] ( - ME[mu, nu] ( -1/4 FS[A, ro, si] FS[A, ro, si] + del[del[A[si], si], ro] A[ro] + 1/2 del[A[ro], ro] del[A[si], si] ) - FS[A, mu, ro] FS[A, nu, ro] + del[del[A[ro], ro], mu] A[nu] + del[del[A[ro], ro], nu] A[mu] )]"
    },
    {
      "name": "LX2z",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, - k2z/Lam X2[mu, nu] ( - ME[mu, nu] ( -1/4 FS[Z, ro, si] FS[Z, ro, si] + 1/2 MZ^2 Z[ro] Z[ro] + del[del[Z[si], si], ro] Z[ro] + 1/2 del[Z[ro], ro] del[Z[si], si] ) - FS[Z, mu, ro] FS[Z, nu, ro] + MZ^2 Z[mu] Z[nu] + del[del[Z[ro], ro], mu] Z[nu] + del[del[Z[ro], ro], nu] Z[mu] )]"
    },
    {
      "name": "LX2w",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, - k2w/Lam X2[mu, nu] ( - ME[mu, nu] ( -1/2 FS[W, ro, si] FS[Wbar, ro, si] + MW^2 W[ro] Wbar[ro] + del[del[W[si], si], ro] Wbar[ro] + del[del[Wbar[si], si], ro] W[ro] + del[W[ro], ro] del[Wbar[si], si] ) - FS[W, mu, ro] FS[Wbar, nu, ro] - FS[Wbar, mu, ro] FS[W, nu, ro] + MW^2 ( W[mu] Wbar[nu] + Wbar[mu] W[nu] ) + del[del[W[ro], ro], mu] Wbar[nu] + del[del[Wbar[ro], ro], mu] W[nu] + del[del[W[ro], ro], nu] Wbar[mu] + del[del[Wbar[ro], ro], nu] W[mu] )]"
    },
    {
      "name": "LX2g",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si, aa}, - k2g/Lam X2[mu, nu] ( - ME[mu, nu] ( -1/4 FS[G, ro, si, aa] FS[G, ro, si, aa] + del[del[G[si, aa], si], ro] G[ro, aa] + 1/2 del[G[ro, aa], ro] del[G[si, aa], si] ) - FS[G, mu, ro, aa] FS[G, nu, ro, aa] + del[del[G[ro, aa], ro], mu] G[nu, aa] + del[del[G[ro, aa], ro], nu] G[mu, aa] )]"
    },
    {
      "name": "LX0",
      "delayed": true,
      "expression": "LX0kin + LX0ff + LX0VV"
    },
    {
      "name": "LX1",
      "delayed": true,
      "expression": "LX1kin + LX1ff + LX1WW + LX1ZZ"
    },
    {
      "name": "LX2",
      "delayed": true,
      "expression": "LX2kin + LX2q + LX2l + LX2a + LX2z + LX2w + LX2g"
    },
    {
      "name": "LHC",
      "delayed": true,
      "expression": "LX0 + LX1 + LX2"
    }
  ]
}
```
I read the paper, the schema, the renderer, and SM.fr. No cached or reference `.fr` file for this model exists here, and none was read.

## Model content found in the paper

The Higgs Characterisation model adds **three** new bosonic states below the EWSB scale (§2): one spin-0 `X0` (a CP-mixed 0±, one field plus a mixing angle α — not two fields), one spin-1 `X1`, one spin-2 `X2`. All are colour, weak and electromagnetic singlets with mass ≈ 125 GeV, and all are real (self-conjugate). There are no multiplets, no new generations, and no new indices.

## Mandatory self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ power (=d−4) | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L/B | CC[] | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LX0kin | del X0 · del X0 ; MX0²X0² | 4 | 1 ; MX0² | 0 ; 2 ✓ | n/a | 0 | n/a (mass eigenstates, no Y) | singlet | singlet | none | 0 | n/a | self-conj (real) |
| LX1kin | FS[X1]² ; MX1²X1X1 | 4 | 1 ; MX1² | 0 ; 2 ✓ | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | self-conj |
| LX2kin | (del X2)² ; MX2²X2X2 (Fierz–Pauli) | 4 | 1 ; MX2² | 0 ; 2 ✓ | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | self-conj |
| LX0ff | ψ̄f ψf X0 (t,b,τ) | 4 | cα κHff gHff, sα κAff gAff | 0 ✓ (gHff = mf/v) | n/a | −Qf+Qf+0=0 | n/a | singlet (mass eigenstates) | 3̄⊗3 singlet (t,b) | none | 0 | n/a | manifestly hermitian (real κ, i γ5 pair) |
| LX0VV (line 1) | Zμ Zμ X0 ; W+μ W−μ X0 | 3 | cα κSM gHZZ / gHWW | +1 ✓ (2M²/v) | n/a | 0 ; +1−1=0 | n/a | singlet | singlet | none | 0 | n/a | hermitian |
| LX0VV (γγ, Zγ, gg) | Aμν Aμν X0, Zμν Aμν X0, Gaμν Gaμν X0 (+duals) | 5 | κ·gHγγ etc. | −1 ✓ | absorbed in 1/v, **not** 1/Λ — paper's own choice (§2.1, Table 2: "we have chosen v as a reference scale instead of Λ"); Description records dim −1, GeV⁻¹ | 0 | n/a | singlet | δᵃᵇ | none | 0 | n/a | hermitian |
| LX0VV (κHZZ, κAZZ, κHWW, κAWW) | Vμν Vμν X0 | 5 | κ dimensionless | 0 ✓ | 1/Λ¹ present ✓ (External `Lam`, 1000 GeV) | 0 ; +1−1=0 | n/a | singlet | singlet | none | 0 | n/a | hermitian |
| LX0VV (derivative line) | Zν ∂μAμν X0, Zν ∂μZμν X0, W+ν ∂μW−μν X0 | 5 | κH∂γ, κH∂Z, κH∂W (complex) | 0 ✓ | 1/Λ¹ ✓ | 0 ; +1−1=0 | n/a | singlet | singlet | none | 0 | n/a | explicit `Conjugate[kHdw]` h.c. partner written |
| LX1ff | ψ̄f γμ(…)ψf X1μ (q, ℓ) | 4 | κfa af, κfb bf | 0 ✓ | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | hermitian |
| LX1WW | W+μν W−μ X1ν ; W+μW−νX1μν ; W+μW−ν∂X1 ; W+W−X̃1 ; ε W ∂W X1 | 4 | κW1..κW5 (κW1,2 × gWWZ) | 0 ✓ | n/a | +1−1+0=0 | n/a | singlet | singlet | none | 0 | n/a | hermitian (W+/W− paired) |
| LX1ZZ | Zμν Zμ X1ν ; X1μ(∂νZμ)Zν ; ε X1 Z ∂Z | 4 | κZ1, κZ3, κZ5 | 0 ✓ | n/a | 0 | n/a | singlet | singlet | none | 0 | n/a | hermitian |
| LX2q, LX2l | T^f_μν X2^μν | 5 | κq, κℓ | 0 ✓ | 1/Λ¹ ✓ | 0 | n/a | singlet | 3̄⊗3 singlet | none | 0 | n/a | hermitian |
| LX2a, LX2z, LX2w, LX2g | T^V_μν X2^μν | 5 | κγ, κZ, κW, κg | 0 ✓ | 1/Λ¹ ✓ | 0 (W+W− paired) | n/a | singlet | δᵃᵇ | none | 0 | n/a | hermitian |
| kinetic+mass present? | X0 → LX0kin ✓, X1 → LX1kin ✓, X2 → LX2kin ✓ | — | — | — | — | — | — | — | — | — | — | — | all three are in the `LHC` sum |

`SelfConjugate -> True` classes: **X0, X1, X2** — none carries `QuantumNumbers` (all are Q = 0 colour/weak singlets).

Reference or cached model file read: **none**. Only the paper, `frmodel.py`, `render.py` and `SM.fr` were opened.

Note on Y: the paper builds the effective lagrangian *below* EWSB, in terms of mass eigenstates (γ, Z, W±, quarks, leptons). SM.fr puts `Y` only on the unphysical chiral fields, so hypercharge is not a quantum number of any field in these terms; the Q sums are the applicable check and all are zero.

```json
{
  "model_name": "HiggsCharacterisation_gen",
  "info": {
    "authors": [
      "P. Artoisenet", "P. de Aquino", "F. Demartin", "R. Frederix", "S. Frixione",
      "F. Maltoni", "M. K. Mandal", "P. Mathews", "K. Mawatari", "V. Ravindran",
      "S. Seth", "P. Torrielli", "M. Zaro"
    ],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["Nikhef", "Vrije Universiteit Brussel", "UCLouvain (CP3)", "CERN", "HRI Allahabad", "SINP Kolkata", "IMSc Chennai", "Universitaet Zuerich"],
    "emails": []
  },
  "interaction_order_hierarchy": [],
  "interaction_order_limit": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "Lam",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "CUTOFF",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "description": "EFT cutoff scale [GeV], Table 1 of arXiv:1306.6464 (reference value 10^3 GeV)"
    },
    {
      "name": "cosa",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 1,
      "tex": "c_{\\alpha}",
      "description": "cos(alpha), CP mixing between the 0+ and 0- components of X0, Eq.(2.3)"
    },
    {
      "name": "kSM",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 2,
      "description": "kappa_SM, dimensionless rescaling of the SM-like X0 Z Z / X0 W W couplings, Eq.(2.4)"
    },
    {
      "name": "kHtt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 3,
      "description": "kappa_Htt, dimensionless scalar coupling of X0 to the top quark, Eq.(2.2)"
    },
    {
      "name": "kAtt",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 4,
      "description": "kappa_Att, dimensionless pseudoscalar coupling of X0 to the top quark, Eq.(2.2)"
    },
    {
      "name": "kHbb",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 5,
      "description": "kappa_Hbb, dimensionless scalar coupling of X0 to the bottom quark, Eq.(2.2)"
    },
    {
      "name": "kAbb",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 6,
      "description": "kappa_Abb, dimensionless pseudoscalar coupling of X0 to the bottom quark, Eq.(2.2)"
    },
    {
      "name": "kHll",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 7,
      "description": "kappa_Htautau, dimensionless scalar coupling of X0 to the tau lepton, Eq.(2.2)"
    },
    {
      "name": "kAll",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 8,
      "description": "kappa_Atautau, dimensionless pseudoscalar coupling of X0 to the tau lepton, Eq.(2.2)"
    },
    {
      "name": "kHaa",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 9,
      "description": "kappa_Hgammagamma, dimensionless, multiplies the loop-induced gHaa, Eq.(2.4)"
    },
    {
      "name": "kAaa",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 10,
      "description": "kappa_Agammagamma, dimensionless, multiplies the loop-induced gAaa, Eq.(2.4)"
    },
    {
      "name": "kHza",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 11,
      "description": "kappa_HZgamma, dimensionless, multiplies the loop-induced gHza, Eq.(2.4)"
    },
    {
      "name": "kAza",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 12,
      "description": "kappa_AZgamma, dimensionless, multiplies the loop-induced gAza, Eq.(2.4)"
    },
    {
      "name": "kHgg",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 13,
      "description": "kappa_Hgg, dimensionless, multiplies the loop-induced gHgg, Eq.(2.4)"
    },
    {
      "name": "kAgg",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "HIGGS",
      "order_block": 14,
      "description": "kappa_Agg, dimensionless, multiplies the loop-induced gAgg, Eq.(2.4)"
    },
    {
      "name": "kHzz",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 15,
      "description": "kappa_HZZ, dimensionless coefficient of the dim-5 operator Zmn Zmn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kAzz",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 16,
      "description": "kappa_AZZ, dimensionless coefficient of the dim-5 operator Zmn ZDualmn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHww",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 17,
      "description": "kappa_HWW, dimensionless coefficient of the dim-5 operator W+mn W-mn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kAww",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 18,
      "description": "kappa_AWW, dimensionless coefficient of the dim-5 operator W+mn W-Dualmn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHda",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 19,
      "description": "kappa_Hdgamma, dimensionless coefficient of the derivative operator Zn dm Amn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHdz",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 20,
      "description": "kappa_HdZ, dimensionless coefficient of the derivative operator Zn dm Zmn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHdwR",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 21,
      "description": "Real part of kappa_HdW, the only complex kappa, derivative operator W+n dm W-mn X0 / Lam, Eq.(2.4)"
    },
    {
      "name": "kHdwI",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "HIGGS",
      "order_block": 22,
      "description": "Imaginary part of kappa_HdW, the only complex kappa, Eq.(2.4)"
    },
    {
      "name": "kqa",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 1,
      "description": "kappa_qa, dimensionless vector coupling of X1 to quarks, Eq.(2.8); zero for a 1+ state, Eq.(2.14)"
    },
    {
      "name": "kqb",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 2,
      "description": "kappa_qb, dimensionless axial coupling of X1 to quarks, Eq.(2.8); zero for a 1- state, Eq.(2.13)"
    },
    {
      "name": "kla",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 3,
      "description": "kappa_la, dimensionless vector coupling of X1 to leptons, Eq.(2.8)"
    },
    {
      "name": "klb",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 4,
      "description": "kappa_lb, dimensionless axial coupling of X1 to leptons, Eq.(2.8)"
    },
    {
      "name": "kw1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 5,
      "description": "kappa_W1, dimensionless X1 W W coupling, first term of Eq.(2.11)"
    },
    {
      "name": "kw2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 6,
      "description": "kappa_W2, dimensionless X1 W W coupling, second term of Eq.(2.11)"
    },
    {
      "name": "kw3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 7,
      "description": "kappa_W3, dimensionless X1 W W coupling, third term of Eq.(2.11)"
    },
    {
      "name": "kw4",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "SPINONE",
      "order_block": 8,
      "description": "kappa_W4, dimensionless CP-odd X1 W W coupling, fourth term of Eq.(2.11)"
    },
    {
      "name": "kw5",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "SPINONE",
      "order_block": 9,
      "description": "kappa_W5, dimensionless CP-odd X1 W W coupling, fifth term of Eq.(2.11)"
    },
    {
      "name": "kz1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 10,
      "description": "kappa_Z1, dimensionless X1 Z Z coupling, first term of Eq.(2.12)"
    },
    {
      "name": "kz3",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINONE",
      "order_block": 11,
      "description": "kappa_Z3, dimensionless X1 Z Z coupling, second term of Eq.(2.12)"
    },
    {
      "name": "kz5",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "SPINONE",
      "order_block": 12,
      "description": "kappa_Z5, dimensionless CP-odd X1 Z Z coupling, third term of Eq.(2.12)"
    },
    {
      "name": "k2q",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 1,
      "description": "kappa_q, dimensionless coupling of X2 to the quark energy-momentum tensor, Eqs.(2.15) and (4.1)"
    },
    {
      "name": "k2l",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 2,
      "description": "kappa_l, dimensionless coupling of X2 to the lepton energy-momentum tensor, Eq.(2.15)"
    },
    {
      "name": "k2z",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 3,
      "description": "kappa_Z, dimensionless coupling of X2 to the Z energy-momentum tensor, Eq.(2.16)"
    },
    {
      "name": "k2w",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 4,
      "description": "kappa_W, dimensionless coupling of X2 to the W energy-momentum tensor, Eq.(2.16)"
    },
    {
      "name": "k2a",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 5,
      "description": "kappa_gamma, dimensionless coupling of X2 to the photon energy-momentum tensor, Eqs.(2.16) and (2.18)"
    },
    {
      "name": "k2g",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "SPINTWO",
      "order_block": 6,
      "description": "kappa_g, dimensionless coupling of X2 to the gluon energy-momentum tensor, Eqs.(2.16) and (4.1)"
    },
    {
      "name": "sina",
      "parameter_type": "Internal",
      "value": "Sqrt[1 - cosa^2]",
      "tex": "s_{\\alpha}",
      "description": "sin(alpha), CP-mixing angle of the spin-0 state, Eq.(2.3)"
    },
    {
      "name": "kHdw",
      "parameter_type": "Internal",
      "value": "kHdwR + I kHdwI",
      "complex": true,
      "description": "Complex kappa_HdW = kHdwR + I kHdwI, Eq.(2.4); the only kappa that cannot be taken real"
    },
    {
      "name": "gHtt",
      "parameter_type": "Internal",
      "value": "MT/vev",
      "interaction_order": ["QED", 1],
      "description": "= mt/v, dimensionless SM-like scalar top coupling strength, Table 2"
    },
    {
      "name": "gAtt",
      "parameter_type": "Internal",
      "value": "MT/vev",
      "interaction_order": ["QED", 1],
      "description": "= mt/v, dimensionless pseudoscalar top coupling strength (2HDM with tan(beta)=1), Table 2"
    },
    {
      "name": "gHbb",
      "parameter_type": "Internal",
      "value": "MB/vev",
      "interaction_order": ["QED", 1],
      "description": "= mb/v, dimensionless SM-like scalar bottom coupling strength, Table 2"
    },
    {
      "name": "gAbb",
      "parameter_type": "Internal",
      "value": "MB/vev",
      "interaction_order": ["QED", 1],
      "description": "= mb/v, dimensionless pseudoscalar bottom coupling strength, Table 2"
    },
    {
      "name": "gHll",
      "parameter_type": "Internal",
      "value": "MTA/vev",
      "interaction_order": ["QED", 1],
      "description": "= mtau/v, dimensionless SM-like scalar tau coupling strength, Table 2"
    },
    {
      "name": "gAll",
      "parameter_type": "Internal",
      "value": "MTA/vev",
      "interaction_order": ["QED", 1],
      "description": "= mtau/v, dimensionless pseudoscalar tau coupling strength, Table 2"
    },
    {
      "name": "gHzz",
      "parameter_type": "Internal",
      "value": "2 MZ^2/vev",
      "interaction_order": ["QED", 1],
      "description": "= 2 MZ^2/v, mass dimension +1, units GeV, SM-like X0 Z Z coupling, Table 2"
    },
    {
      "name": "gHww",
      "parameter_type": "Internal",
      "value": "2 MW^2/vev",
      "interaction_order": ["QED", 1],
      "description": "= 2 MW^2/v, mass dimension +1, units GeV, SM-like X0 W W coupling, Table 2"
    },
    {
      "name": "gHaa",
      "parameter_type": "Internal",
      "value": "47 aEW/(18 Pi vev)",
      "interaction_order": ["QED", 3],
      "description": "= 47 alphaEM/(18 Pi v), mass dimension -1, units GeV^-1; Table 2 uses v, not Lam, as the reference scale because this operator is loop-induced already in the SM"
    },
    {
      "name": "gAaa",
      "parameter_type": "Internal",
      "value": "4 aEW/(3 Pi vev)",
      "interaction_order": ["QED", 3],
      "description": "= 4 alphaEM/(3 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "Cza",
      "parameter_type": "Internal",
      "value": "Sqrt[aEW Gf MZ^2/(8 Sqrt[2] Pi)]",
      "description": "C = Sqrt[alphaEM GF MZ^2/(8 Sqrt[2] Pi)], dimensionless constant of Table 2"
    },
    {
      "name": "gHza",
      "parameter_type": "Internal",
      "value": "Cza (94 cw^2 - 13)/(9 Pi vev)",
      "interaction_order": ["QED", 3],
      "description": "= C (94 cos^2(thetaW) - 13)/(9 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "gAza",
      "parameter_type": "Internal",
      "value": "2 Cza (8 cw^2 - 5)/(3 Pi vev)",
      "interaction_order": ["QED", 3],
      "description": "= 2 C (8 cos^2(thetaW) - 5)/(3 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "gHgg",
      "parameter_type": "Internal",
      "value": "-aS/(3 Pi vev)",
      "interaction_order": ["QCD", 2],
      "description": "= -alphaS/(3 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "gAgg",
      "parameter_type": "Internal",
      "value": "aS/(2 Pi vev)",
      "interaction_order": ["QCD", 2],
      "description": "= alphaS/(2 Pi v), mass dimension -1, units GeV^-1, Table 2 (reference scale v, not Lam)"
    },
    {
      "name": "gWWZ",
      "parameter_type": "Internal",
      "value": "-ee cw/sw",
      "interaction_order": ["QED", 1],
      "description": "gWWZ = -e cot(thetaW), dimensionless, below Eq.(2.11)"
    },
    {
      "name": "aQu",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) (1/2 - 4/3 sw^2)",
      "interaction_order": ["QED", 1],
      "description": "a_u, SM vector coupling of up-type quarks, Eq.(2.9), dimensionless"
    },
    {
      "name": "bQu",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "b_u, SM axial coupling of up-type quarks, Eq.(2.9), dimensionless"
    },
    {
      "name": "aQd",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) (-1/2 + 2/3 sw^2)",
      "interaction_order": ["QED", 1],
      "description": "a_d, SM vector coupling of down-type quarks, Eq.(2.10), dimensionless"
    },
    {
      "name": "bQd",
      "parameter_type": "Internal",
      "value": "-gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "b_d, SM axial coupling of down-type quarks, Eq.(2.10), dimensionless"
    },
    {
      "name": "aLl",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) (-1/2 + 2 sw^2)",
      "interaction_order": ["QED", 1],
      "description": "a_l, SM vector coupling of charged leptons, Eqs.(2.9)-(2.10) applied to leptons, dimensionless"
    },
    {
      "name": "bLl",
      "parameter_type": "Internal",
      "value": "-gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "b_l, SM axial coupling of charged leptons, dimensionless"
    },
    {
      "name": "aLv",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "a_nu, SM vector coupling of neutrinos, dimensionless"
    },
    {
      "name": "bLv",
      "parameter_type": "Internal",
      "value": "gw/(2 cw) 1/2",
      "interaction_order": ["QED", 1],
      "description": "b_nu, SM axial coupling of neutrinos, dimensionless"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "X0",
      "self_conjugate": true,
      "mass": { "sym": "MX0", "value": "125." },
      "width": { "sym": "WX0", "value": "0.00407" },
      "quantum_numbers": {},
      "pdg": 5000000,
      "particle_name": "x0",
      "full_name": "X0 spin-0 resonance",
      "propagator_label": "X0",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "X1",
      "self_conjugate": true,
      "mass": { "sym": "MX1", "value": "125." },
      "width": { "sym": "WX1", "value": "0.00407" },
      "quantum_numbers": {},
      "pdg": 5000001,
      "particle_name": "x1",
      "full_name": "X1 spin-1 resonance",
      "propagator_label": "X1",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "T",
      "class_index": 100,
      "class_name": "X2",
      "self_conjugate": true,
      "mass": { "sym": "MX2", "value": "125." },
      "width": { "sym": "WX2", "value": "0.00407" },
      "quantum_numbers": {},
      "pdg": 5000002,
      "particle_name": "x2",
      "full_name": "X2 spin-2 resonance",
      "propagator_label": "X2",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "raw_blocks": [],
  "lagrangian_terms": [
    {
      "name": "LX0kin",
      "delayed": true,
      "expression": "Block[{mu}, 1/2 del[X0, mu] del[X0, mu] - 1/2 MX0^2 X0^2]"
    },
    {
      "name": "LX1kin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[X1, mu, nu] FS[X1, mu, nu] + 1/2 MX1^2 X1[mu] X1[mu]]"
    },
    {
      "name": "LX2kin",
      "delayed": true,
      "expression": "Block[{mu, nu, ro}, -1/2 del[X2[mu, nu], ro] del[X2[mu, nu], ro] + del[X2[mu, nu], mu] del[X2[ro, nu], ro] - del[X2[mu, nu], mu] del[X2[ro, ro], nu] + 1/2 del[X2[mu, mu], ro] del[X2[nu, nu], ro] - 1/2 MX2^2 (X2[mu, nu] X2[mu, nu] - X2[mu, mu] X2[nu, nu])]"
    },
    {
      "name": "LX0ff",
      "delayed": true,
      "expression": "Block[{}, - ( cosa kHtt gHtt tbar.t + I sina kAtt gAtt tbar.Ga[5].t + cosa kHbb gHbb bbar.b + I sina kAbb gAbb bbar.Ga[5].b + cosa kHll gHll tabar.ta + I sina kAll gAll tabar.Ga[5].ta ) X0]"
    },
    {
      "name": "LX0VV",
      "delayed": true,
      "expression": "Block[{mu, nu, aa}, ( cosa kSM ( 1/2 gHzz Z[mu] Z[mu] + gHww W[mu] Wbar[mu] ) - 1/4 ( cosa kHaa gHaa FS[A, mu, nu] FS[A, mu, nu] + sina kAaa gAaa FS[A, mu, nu] FSDual[A, mu, nu] ) - 1/2 ( cosa kHza gHza FS[Z, mu, nu] FS[A, mu, nu] + sina kAza gAza FS[Z, mu, nu] FSDual[A, mu, nu] ) - 1/4 ( cosa kHgg gHgg FS[G, mu, nu, aa] FS[G, mu, nu, aa] + sina kAgg gAgg FS[G, mu, nu, aa] FSDual[G, mu, nu, aa] ) - 1/(4 Lam) ( cosa kHzz FS[Z, mu, nu] FS[Z, mu, nu] + sina kAzz FS[Z, mu, nu] FSDual[Z, mu, nu] ) - 1/(2 Lam) ( cosa kHww FS[W, mu, nu] FS[Wbar, mu, nu] + sina kAww FS[W, mu, nu] FSDual[Wbar, mu, nu] ) - cosa/Lam ( kHda Z[nu] del[FS[A, mu, nu], mu] + kHdz Z[nu] del[FS[Z, mu, nu], mu] + kHdw W[nu] del[FS[Wbar, mu, nu], mu] + Conjugate[kHdw] Wbar[nu] del[FS[W, mu, nu], mu] ) ) X0]"
    },
    {
      "name": "LX1ff",
      "delayed": true,
      "expression": "Block[{mu}, ( kqa aQu uqbar.Ga[mu].uq - kqb bQu uqbar.Ga[mu].Ga[5].uq + kqa aQd dqbar.Ga[mu].dq - kqb bQd dqbar.Ga[mu].Ga[5].dq + kla aLl lbar.Ga[mu].l - klb bLl lbar.Ga[mu].Ga[5].l + kla aLv vlbar.Ga[mu].vl - klb bLv vlbar.Ga[mu].Ga[5].vl ) X1[mu]]"
    },
    {
      "name": "LX1WW",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, I kw1 gWWZ ( FS[W, mu, nu] Wbar[mu] - FS[Wbar, mu, nu] W[mu] ) X1[nu] + I kw2 gWWZ W[mu] Wbar[nu] FS[X1, mu, nu] - kw3 W[mu] Wbar[nu] ( del[X1[nu], mu] + del[X1[mu], nu] ) + I kw4 W[mu] Wbar[nu] FSDual[X1, mu, nu] - kw5 Eps[mu, nu, ro, si] ( W[mu] del[Wbar[nu], ro] - del[W[mu], ro] Wbar[nu] ) X1[si]]"
    },
    {
      "name": "LX1ZZ",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, - kz1 FS[Z, mu, nu] Z[mu] X1[nu] - kz3 X1[mu] del[Z[mu], nu] Z[nu] - kz5 Eps[mu, nu, ro, si] X1[mu] Z[nu] del[Z[si], ro]]"
    },
    {
      "name": "LX2q",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, sp, ff, cc}, - k2q/Lam X2[mu, nu] ( - ME[mu, nu] ( I uqbar.Ga[ro].DC[uq, ro] - Mu[ff] uqbar[sp, ff, cc].uq[sp, ff, cc] - I/2 ( del[uqbar, ro].Ga[ro].uq + uqbar.Ga[ro].del[uq, ro] ) ) + I/2 uqbar.Ga[mu].DC[uq, nu] + I/2 uqbar.Ga[nu].DC[uq, mu] - I/4 ( del[uqbar, mu].Ga[nu].uq + uqbar.Ga[nu].del[uq, mu] ) - I/4 ( del[uqbar, nu].Ga[mu].uq + uqbar.Ga[mu].del[uq, nu] ) ) - k2q/Lam X2[mu, nu] ( - ME[mu, nu] ( I dqbar.Ga[ro].DC[dq, ro] - Md[ff] dqbar[sp, ff, cc].dq[sp, ff, cc] - I/2 ( del[dqbar, ro].Ga[ro].dq + dqbar.Ga[ro].del[dq, ro] ) ) + I/2 dqbar.Ga[mu].DC[dq, nu] + I/2 dqbar.Ga[nu].DC[dq, mu] - I/4 ( del[dqbar, mu].Ga[nu].dq + dqbar.Ga[nu].del[dq, mu] ) - I/4 ( del[dqbar, nu].Ga[mu].dq + dqbar.Ga[mu].del[dq, nu] ) )]"
    },
    {
      "name": "LX2l",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, sp, ff}, - k2l/Lam X2[mu, nu] ( - ME[mu, nu] ( I lbar.Ga[ro].DC[l, ro] - Ml[ff] lbar[sp, ff].l[sp, ff] - I/2 ( del[lbar, ro].Ga[ro].l + lbar.Ga[ro].del[l, ro] ) ) + I/2 lbar.Ga[mu].DC[l, nu] + I/2 lbar.Ga[nu].DC[l, mu] - I/4 ( del[lbar, mu].Ga[nu].l + lbar.Ga[nu].del[l, mu] ) - I/4 ( del[lbar, nu].Ga[mu].l + lbar.Ga[mu].del[l, nu] ) ) - k2l/Lam X2[mu, nu] ( - ME[mu, nu] ( I vlbar.Ga[ro].DC[vl, ro] - I/2 ( del[vlbar, ro].Ga[ro].vl + vlbar.Ga[ro].del[vl, ro] ) ) + I/2 vlbar.Ga[mu].DC[vl, nu] + I/2 vlbar.Ga[nu].DC[vl, mu] - I/4 ( del[vlbar, mu].Ga[nu].vl + vlbar.Ga[nu].del[vl, mu] ) - I/4 ( del[vlbar, nu].Ga[mu].vl + vlbar.Ga[mu].del[vl, nu] ) )]"
    },
    {
      "name": "LX2a",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, - k2a/Lam X2[mu, nu] ( - ME[mu, nu] ( -1/4 FS[A, ro, si] FS[A, ro, si] + del[del[A[si], si], ro] A[ro] + 1/2 del[A[ro], ro] del[A[si], si] ) - FS[A, mu, ro] FS[A, nu, ro] + del[del[A[ro], ro], mu] A[nu] + del[del[A[ro], ro], nu] A[mu] )]"
    },
    {
      "name": "LX2z",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, - k2z/Lam X2[mu, nu] ( - ME[mu, nu] ( -1/4 FS[Z, ro, si] FS[Z, ro, si] + 1/2 MZ^2 Z[ro] Z[ro] + del[del[Z[si], si], ro] Z[ro] + 1/2 del[Z[ro], ro] del[Z[si], si] ) - FS[Z, mu, ro] FS[Z, nu, ro] + MZ^2 Z[mu] Z[nu] + del[del[Z[ro], ro], mu] Z[nu] + del[del[Z[ro], ro], nu] Z[mu] )]"
    },
    {
      "name": "LX2w",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si}, - k2w/Lam X2[mu, nu] ( - ME[mu, nu] ( -1/2 FS[W, ro, si] FS[Wbar, ro, si] + MW^2 W[ro] Wbar[ro] + del[del[W[si], si], ro] Wbar[ro] + del[del[Wbar[si], si], ro] W[ro] + del[W[ro], ro] del[Wbar[si], si] ) - FS[W, mu, ro] FS[Wbar, nu, ro] - FS[Wbar, mu, ro] FS[W, nu, ro] + MW^2 ( W[mu] Wbar[nu] + Wbar[mu] W[nu] ) + del[del[W[ro], ro], mu] Wbar[nu] + del[del[Wbar[ro], ro], mu] W[nu] + del[del[W[ro], ro], nu] Wbar[mu] + del[del[Wbar[ro], ro], nu] W[mu] )]"
    },
    {
      "name": "LX2g",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si, aa}, - k2g/Lam X2[mu, nu] ( - ME[mu, nu] ( -1/4 FS[G, ro, si, aa] FS[G, ro, si, aa] + del[del[G[si, aa], si], ro] G[ro, aa] + 1/2 del[G[ro, aa], ro] del[G[si, aa], si] ) - FS[G, mu, ro, aa] FS[G, nu, ro, aa] + del[del[G[ro, aa], ro], mu] G[nu, aa] + del[del[G[ro, aa], ro], nu] G[mu, aa] )]"
    },
    {
      "name": "LX0",
      "delayed": true,
      "expression": "LX0kin + LX0ff + LX0VV"
    },
    {
      "name": "LX1",
      "delayed": true,
      "expression": "LX1kin + LX1ff + LX1WW + LX1ZZ"
    },
    {
      "name": "LX2",
      "delayed": true,
      "expression": "LX2kin + LX2q + LX2l + LX2a + LX2z + LX2w + LX2g"
    },
    {
      "name": "LHC",
      "delayed": true,
      "expression": "LX0 + LX1 + LX2"
    }
  ]
}
```