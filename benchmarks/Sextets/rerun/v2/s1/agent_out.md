I'll start by reading the paper and the schema.
I read the paper, the schema, the renderer, and SM.fr. No reference or cached `.fr` file for this model exists in the sandbox, and none was read.

## Physics summary

The paper (Han, Lewis, McElmurry, arXiv:0909.2666) adds **scalar diquarks**. Section 2 + Table 1 give the full new-physics content:

- Colour: **6** or **3̄** of SU(3)_C, independently of the electroweak assignment.
- Electroweak options: SU(2) singlet Y=1/3 (couples QQ, UD), SU(2) triplet Y=1/3 (couples QQ), singlet Y=2/3 (couples DD), singlet Y=4/3 (couples UU).
- Coupling, Eq. (2.1), written **after** electroweak symmetry breaking with physical quarks: `L = 2 Sqrt[2] Kbar[i,a,b] D[i] qbar[a] (lamL PL + lamR PR) q^C[b] + h.c.`

**Charge re-derivation (rule 5).** In `D qbar Γ q^C` the bilinear carries −2Q_q, so Q(D) = +2Q_q. Therefore the complete set of diquark charge eigenstates is Q = 4/3 (uu), 1/3 (ud), −2/3 (dd) — exactly the charges spanned by all four rows of Table 1 (the triplet row supplies 4/3, 1/3, −2/3). Table 1 quotes |Q| and lists the DD state as Y = 2/3; the field that appears in Eq. (2.1) has **Q = Y = −2/3**. I use the re-derived sign.

So: 3 charge states × 2 colour reps = **6 new scalars**. Eq. (2.1) is deliberately not SU(2)×U(1) invariant (a Y=4/3 singlet cannot couple to u_L u_L), so `Y` is **not** declared as a quantum number; only `Q` is, and the hypercharge-singlet gauge coupling is written explicitly through the photon.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling symbol | coupling dim (=4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L/B number | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LD6Kin (kin, ×3 states) | `del[D6xxbar]del[D6xx]` | 4 | – | 0 | n/a | −Q+Q=0 | n/a (post-EWSB) | singlet | `ii` shared Sextet | none | B: −2/3+2/3=0 | n/a | self-conjugate pair |
| LD6Kin (mass, ×3) | `M^2 D6xxbar D6xx` | 2 | `MD6xx^2` | 2 ✓ | n/a | 0 | n/a | singlet | Sextet `ii` | none | 0 | n/a | real, self-Hermitian |
| LD6Kin (1-gluon, ×3) | `gs T6 G D6bar del[D6]` | 4 | `gs` | 0 ✓ | n/a | 0 | n/a | singlet | `T6[gg,ii,jj]` | none | 0 | n/a | Hermitian by construction |
| LD6Kin (2-gluon, ×3) | `gs^2 T6 T6 G G D6bar D6` | 4 | `gs^2` | 0 ✓ | n/a | 0 | n/a | singlet | `T6 T6` on Sextet | none | 0 | n/a | Hermitian |
| LD6EM (γ, γγ, γg; ×3) | `ee Q A D6bar del[D6]` etc. | 4 | `ee` | 0 ✓ | n/a | 0 | n/a | singlet | δ / `T6` | none | 0 | n/a | Hermitian |
| LD3Kin (kin+mass+gluon, ×3) | `DC[D3bar]DC[D3]`, `M^2 D3bar D3` | 4 / 2 | – / `MD3xx^2` | 0 / 2 ✓ | n/a | 0 | n/a | singlet | `DC` on Index[Colour] | none | 0 | n/a | Hermitian |
| LD3EM (γ, γγ, γg; ×3) | `ee Q A D3bar del[D3]` etc. | 4 | `ee` | 0 ✓ | n/a | 0 | n/a | singlet | δ / `T[gg,cc,dd]` | none | 0 | n/a | Hermitian |
| LDQ6 uu | `K6 D6uu uqbar.Proj.CC[uq]` | 4 | `lamL6uu`,`lamR6uu` | 0 ✓ | n/a | 4/3−2/3−2/3=0 | n/a (Eq. 2.1 post-EWSB) | none (mass eigenstates) | `K6[ii,aa,bb]`, 6 ⊗ 3̄ ⊗ 3̄ | none | B: 2/3−1/3−1/3=0 | **yes** | `HC[...]` |
| LDQ6 ud | `K6 D6ud uqbar.Proj.CC[dq]` | 4 | `lamL6ud`,`lamR6ud` | 0 ✓ | n/a | 1/3−2/3+1/3=0 | n/a | none | `K6[ii,aa,bb]` | none | 0 | **yes** | `HC[...]` |
| LDQ6 dd | `K6 D6dd dqbar.Proj.CC[dq]` | 4 | `lamL6dd`,`lamR6dd` | 0 ✓ | n/a | −2/3+1/3+1/3=0 | n/a | none | `K6[ii,aa,bb]` | none | 0 | **yes** | `HC[...]` |
| LDQ3 uu | `Eps D3uu uqbar.Proj.CC[uq]` | 4 | `lamL3uu`,`lamR3uu` (antisym.) | 0 ✓ | n/a | 4/3−2/3−2/3=0 | n/a | none | `Eps[aa,bb,cc]/Sqrt[2]` | none | 0 | **yes** | `HC[...]` |
| LDQ3 ud | `Eps D3ud uqbar.Proj.CC[dq]` | 4 | `lamL3ud`,`lamR3ud` | 0 ✓ | n/a | 1/3−2/3+1/3=0 | n/a | none | `Eps[aa,bb,cc]/Sqrt[2]` | none | 0 | **yes** | `HC[...]` |
| LDQ3 dd | `Eps D3dd dqbar.Proj.CC[dq]` | 4 | `lamL3dd`,`lamR3dd` (antisym.) | 0 ✓ | n/a | −2/3+1/3+1/3=0 | n/a | none | `Eps[aa,bb,cc]/Sqrt[2]` | none | 0 | **yes** | `HC[...]` |

Per-class free-field check (all six appear in the total sum `LDiquark`): `D6uu` (LD6Kin), `D6ud` (LD6Kin), `D6dd` (LD6Kin), `D3uu` (LD3Kin), `D3ud` (LD3Kin), `D3dd` (LD3Kin). Every class uses the mass symbol from its own `Mass -> {M, value}` spec.

`SelfConjugate -> True` classes: **none** — all six diquarks are complex, so none carries the forbidden combination of quantum numbers on a self-conjugate class.

No EFT cutoff is needed: every operator has d = 4 or less, so all couplings are dimensionless (`lam*`) or of dimension 2 (`M^2`).

Reference or cached model file read: **none**.

```json
{
  "model_name": "Sextets_gen",
  "info": {
    "authors": ["Tao Han", "Ian Lewis", "Thomas McElmurry"],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["Department of Physics, University of Wisconsin, Madison"],
    "emails": ["than@hep.wisc.edu", "ilewis@wisc.edu", "mcelmurry@hep.wisc.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Sextet",
      "range_kind": "NoUnfold",
      "size": 6,
      "style_symbol": "st"
    }
  ],
  "parameters": [
    {
      "name": "K6",
      "parameter_type": "Internal",
      "complex": false,
      "indices": ["Sextet", "Colour", "Colour"],
      "value_rules": [
        {"lhs": "K6[1,1,1]", "rhs": "1"},
        {"lhs": "K6[1,1,2]", "rhs": "0"},
        {"lhs": "K6[1,1,3]", "rhs": "0"},
        {"lhs": "K6[1,2,1]", "rhs": "0"},
        {"lhs": "K6[1,2,2]", "rhs": "0"},
        {"lhs": "K6[1,2,3]", "rhs": "0"},
        {"lhs": "K6[1,3,1]", "rhs": "0"},
        {"lhs": "K6[1,3,2]", "rhs": "0"},
        {"lhs": "K6[1,3,3]", "rhs": "0"},
        {"lhs": "K6[2,1,1]", "rhs": "0"},
        {"lhs": "K6[2,1,2]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[2,1,3]", "rhs": "0"},
        {"lhs": "K6[2,2,1]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[2,2,2]", "rhs": "0"},
        {"lhs": "K6[2,2,3]", "rhs": "0"},
        {"lhs": "K6[2,3,1]", "rhs": "0"},
        {"lhs": "K6[2,3,2]", "rhs": "0"},
        {"lhs": "K6[2,3,3]", "rhs": "0"},
        {"lhs": "K6[3,1,1]", "rhs": "0"},
        {"lhs": "K6[3,1,2]", "rhs": "0"},
        {"lhs": "K6[3,1,3]", "rhs": "0"},
        {"lhs": "K6[3,2,1]", "rhs": "0"},
        {"lhs": "K6[3,2,2]", "rhs": "1"},
        {"lhs": "K6[3,2,3]", "rhs": "0"},
        {"lhs": "K6[3,3,1]", "rhs": "0"},
        {"lhs": "K6[3,3,2]", "rhs": "0"},
        {"lhs": "K6[3,3,3]", "rhs": "0"},
        {"lhs": "K6[4,1,1]", "rhs": "0"},
        {"lhs": "K6[4,1,2]", "rhs": "0"},
        {"lhs": "K6[4,1,3]", "rhs": "0"},
        {"lhs": "K6[4,2,1]", "rhs": "0"},
        {"lhs": "K6[4,2,2]", "rhs": "0"},
        {"lhs": "K6[4,2,3]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[4,3,1]", "rhs": "0"},
        {"lhs": "K6[4,3,2]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[4,3,3]", "rhs": "0"},
        {"lhs": "K6[5,1,1]", "rhs": "0"},
        {"lhs": "K6[5,1,2]", "rhs": "0"},
        {"lhs": "K6[5,1,3]", "rhs": "0"},
        {"lhs": "K6[5,2,1]", "rhs": "0"},
        {"lhs": "K6[5,2,2]", "rhs": "0"},
        {"lhs": "K6[5,2,3]", "rhs": "0"},
        {"lhs": "K6[5,3,1]", "rhs": "0"},
        {"lhs": "K6[5,3,2]", "rhs": "0"},
        {"lhs": "K6[5,3,3]", "rhs": "1"},
        {"lhs": "K6[6,1,1]", "rhs": "0"},
        {"lhs": "K6[6,1,2]", "rhs": "0"},
        {"lhs": "K6[6,1,3]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[6,2,1]", "rhs": "0"},
        {"lhs": "K6[6,2,2]", "rhs": "0"},
        {"lhs": "K6[6,2,3]", "rhs": "0"},
        {"lhs": "K6[6,3,1]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[6,3,2]", "rhs": "0"},
        {"lhs": "K6[6,3,3]", "rhs": "0"}
      ],
      "tex": "K",
      "description": "Clebsch-Gordan coefficients K^{i a b} that couple the colour sextet to two colour triplets, Eq.(A.6). Symmetric in the two Colour indices. The antitriplet case uses K_{abc} = Eps[a,b,c]/Sqrt[2], Eq.(A.7), written directly in the Lagrangian."
    },
    {
      "name": "T6",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Gluon", "Sextet", "Sextet"],
      "definitions": [
        {
          "lhs": "T6[gg_?NumericQ, ii_?NumericQ, jj_?NumericQ]",
          "rhs": "2 Sum[K6[ii,aa,bb] T[gg,bb,cc] K6[jj,aa,cc], {aa,3}, {bb,3}, {cc,3}]",
          "delayed": true
        }
      ],
      "tex": "\\mathcal{T}",
      "description": "SU(3)_C generators in the colour-sextet (diquark) representation, Eq.(A.12): T^A_{ij} = 2 Tr(K^i t^A Kbar^j). They satisfy [T^A,T^B] = I f^{ABC} T^C and T^A T^A = CD = 10/3, Eq.(A.14)."
    },
    {
      "name": "lamL6uu",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6UUL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL6uu[1,1]", "rhs": "0.1"},
        {"lhs": "lamL6uu[1,2]", "rhs": "0.1"},
        {"lhs": "lamL6uu[1,3]", "rhs": "0.1"},
        {"lhs": "lamL6uu[2,1]", "rhs": "0.1"},
        {"lhs": "lamL6uu[2,2]", "rhs": "0.1"},
        {"lhs": "lamL6uu[2,3]", "rhs": "0.1"},
        {"lhs": "lamL6uu[3,1]", "rhs": "0.1"},
        {"lhs": "lamL6uu[3,2]", "rhs": "0.1"},
        {"lhs": "lamL6uu[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_L^{6,uu}",
      "description": "Left-chirality diquark Yukawa of the colour-sextet Q=4/3 state to two up-type quarks, Eq.(2.1). Symmetric in generation because the sextet colour tensor K6 is symmetric. Dimensionless; benchmark 0.1. The left-handed couplings are tightly constrained by minimal flavour violation."
    },
    {
      "name": "lamR6uu",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6UUR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR6uu[1,1]", "rhs": "0.1"},
        {"lhs": "lamR6uu[1,2]", "rhs": "0.1"},
        {"lhs": "lamR6uu[1,3]", "rhs": "0.1"},
        {"lhs": "lamR6uu[2,1]", "rhs": "0.1"},
        {"lhs": "lamR6uu[2,2]", "rhs": "0."},
        {"lhs": "lamR6uu[2,3]", "rhs": "0.1"},
        {"lhs": "lamR6uu[3,1]", "rhs": "0.1"},
        {"lhs": "lamR6uu[3,2]", "rhs": "0.1"},
        {"lhs": "lamR6uu[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_R^{6,uu}",
      "description": "Right-chirality diquark Yukawa of the colour-sextet Q=4/3 state to two up-type quarks, Eq.(2.1). Symmetric in generation. Benchmark from Eq.(2.2): lamR[uu], lamR[uc] <~ 0.1 and lamR[cc] ~ 0 from D0-D0bar mixing and D -> pi pi."
    },
    {
      "name": "lamL6ud",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6UDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL6ud[1,1]", "rhs": "0.1"},
        {"lhs": "lamL6ud[1,2]", "rhs": "0.1"},
        {"lhs": "lamL6ud[1,3]", "rhs": "0.1"},
        {"lhs": "lamL6ud[2,1]", "rhs": "0.1"},
        {"lhs": "lamL6ud[2,2]", "rhs": "0.1"},
        {"lhs": "lamL6ud[2,3]", "rhs": "0.1"},
        {"lhs": "lamL6ud[3,1]", "rhs": "0.1"},
        {"lhs": "lamL6ud[3,2]", "rhs": "0.1"},
        {"lhs": "lamL6ud[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_L^{6,ud}",
      "description": "Left-chirality diquark Yukawa of the colour-sextet Q=1/3 state to one up-type and one down-type quark, Eq.(2.1) (Table 1 rows QQ and UD). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR6ud",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6UDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR6ud[1,1]", "rhs": "0.1"},
        {"lhs": "lamR6ud[1,2]", "rhs": "0.1"},
        {"lhs": "lamR6ud[1,3]", "rhs": "0.1"},
        {"lhs": "lamR6ud[2,1]", "rhs": "0.1"},
        {"lhs": "lamR6ud[2,2]", "rhs": "0.1"},
        {"lhs": "lamR6ud[2,3]", "rhs": "0.1"},
        {"lhs": "lamR6ud[3,1]", "rhs": "0.1"},
        {"lhs": "lamR6ud[3,2]", "rhs": "0.1"},
        {"lhs": "lamR6ud[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_R^{6,ud}",
      "description": "Right-chirality diquark Yukawa of the colour-sextet Q=1/3 state to one up-type and one down-type quark, Eq.(2.1). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamL6dd",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6DDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL6dd[1,1]", "rhs": "0.1"},
        {"lhs": "lamL6dd[1,2]", "rhs": "0.1"},
        {"lhs": "lamL6dd[1,3]", "rhs": "0.1"},
        {"lhs": "lamL6dd[2,1]", "rhs": "0.1"},
        {"lhs": "lamL6dd[2,2]", "rhs": "0.1"},
        {"lhs": "lamL6dd[2,3]", "rhs": "0.1"},
        {"lhs": "lamL6dd[3,1]", "rhs": "0.1"},
        {"lhs": "lamL6dd[3,2]", "rhs": "0.1"},
        {"lhs": "lamL6dd[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_L^{6,dd}",
      "description": "Left-chirality diquark Yukawa of the colour-sextet Q=-2/3 state to two down-type quarks, Eq.(2.1) (Table 1 row DD). Symmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR6dd",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6DDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR6dd[1,1]", "rhs": "0.1"},
        {"lhs": "lamR6dd[1,2]", "rhs": "0.1"},
        {"lhs": "lamR6dd[1,3]", "rhs": "0.1"},
        {"lhs": "lamR6dd[2,1]", "rhs": "0.1"},
        {"lhs": "lamR6dd[2,2]", "rhs": "0.1"},
        {"lhs": "lamR6dd[2,3]", "rhs": "0.1"},
        {"lhs": "lamR6dd[3,1]", "rhs": "0.1"},
        {"lhs": "lamR6dd[3,2]", "rhs": "0.1"},
        {"lhs": "lamR6dd[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_R^{6,dd}",
      "description": "Right-chirality diquark Yukawa of the colour-sextet Q=-2/3 state to two down-type quarks, Eq.(2.1). Symmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamL3uu",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3UUL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL3uu[1,1]", "rhs": "0."},
        {"lhs": "lamL3uu[1,2]", "rhs": "0.1"},
        {"lhs": "lamL3uu[1,3]", "rhs": "0.1"},
        {"lhs": "lamL3uu[2,1]", "rhs": "-0.1"},
        {"lhs": "lamL3uu[2,2]", "rhs": "0."},
        {"lhs": "lamL3uu[2,3]", "rhs": "0.1"},
        {"lhs": "lamL3uu[3,1]", "rhs": "-0.1"},
        {"lhs": "lamL3uu[3,2]", "rhs": "-0.1"},
        {"lhs": "lamL3uu[3,3]", "rhs": "0."}
      ],
      "tex": "\\lambda_L^{3,uu}",
      "description": "Left-chirality diquark Yukawa of the colour-antitriplet Q=4/3 state to two up-type quarks, Eq.(2.1). Antisymmetric in generation because the antitriplet colour tensor Eps is antisymmetric (Section 2). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR3uu",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3UUR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR3uu[1,1]", "rhs": "0."},
        {"lhs": "lamR3uu[1,2]", "rhs": "0.1"},
        {"lhs": "lamR3uu[1,3]", "rhs": "0.1"},
        {"lhs": "lamR3uu[2,1]", "rhs": "-0.1"},
        {"lhs": "lamR3uu[2,2]", "rhs": "0."},
        {"lhs": "lamR3uu[2,3]", "rhs": "0.1"},
        {"lhs": "lamR3uu[3,1]", "rhs": "-0.1"},
        {"lhs": "lamR3uu[3,2]", "rhs": "-0.1"},
        {"lhs": "lamR3uu[3,3]", "rhs": "0."}
      ],
      "tex": "\\lambda_R^{3,uu}",
      "description": "Right-chirality diquark Yukawa of the colour-antitriplet Q=4/3 state to two up-type quarks, Eq.(2.1). Antisymmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamL3ud",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3UDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL3ud[1,1]", "rhs": "0.1"},
        {"lhs": "lamL3ud[1,2]", "rhs": "0.1"},
        {"lhs": "lamL3ud[1,3]", "rhs": "0.1"},
        {"lhs": "lamL3ud[2,1]", "rhs": "0.1"},
        {"lhs": "lamL3ud[2,2]", "rhs": "0.1"},
        {"lhs": "lamL3ud[2,3]", "rhs": "0.1"},
        {"lhs": "lamL3ud[3,1]", "rhs": "0.1"},
        {"lhs": "lamL3ud[3,2]", "rhs": "0.1"},
        {"lhs": "lamL3ud[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_L^{3,ud}",
      "description": "Left-chirality diquark Yukawa of the colour-antitriplet Q=1/3 state to one up-type and one down-type quark, Eq.(2.1). This is the state produced from the du and ds initial states of Figs. 4(a), 5(a). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR3ud",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3UDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR3ud[1,1]", "rhs": "0.1"},
        {"lhs": "lamR3ud[1,2]", "rhs": "0.1"},
        {"lhs": "lamR3ud[1,3]", "rhs": "0.1"},
        {"lhs": "lamR3ud[2,1]", "rhs": "0.1"},
        {"lhs": "lamR3ud[2,2]", "rhs": "0.1"},
        {"lhs": "lamR3ud[2,3]", "rhs": "0.1"},
        {"lhs": "lamR3ud[3,1]", "rhs": "0.1"},
        {"lhs": "lamR3ud[3,2]", "rhs": "0.1"},
        {"lhs": "lamR3ud[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_R^{3,ud}",
      "description": "Right-chirality diquark Yukawa of the colour-antitriplet Q=1/3 state to one up-type and one down-type quark, Eq.(2.1). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamL3dd",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3DDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL3dd[1,1]", "rhs": "0."},
        {"lhs": "lamL3dd[1,2]", "rhs": "0.1"},
        {"lhs": "lamL3dd[1,3]", "rhs": "0.1"},
        {"lhs": "lamL3dd[2,1]", "rhs": "-0.1"},
        {"lhs": "lamL3dd[2,2]", "rhs": "0."},
        {"lhs": "lamL3dd[2,3]", "rhs": "0.1"},
        {"lhs": "lamL3dd[3,1]", "rhs": "-0.1"},
        {"lhs": "lamL3dd[3,2]", "rhs": "-0.1"},
        {"lhs": "lamL3dd[3,3]", "rhs": "0."}
      ],
      "tex": "\\lambda_L^{3,dd}",
      "description": "Left-chirality diquark Yukawa of the colour-antitriplet Q=-2/3 state to two down-type quarks, Eq.(2.1). Antisymmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR3dd",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3DDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR3dd[1,1]", "rhs": "0."},
        {"lhs": "lamR3dd[1,2]", "rhs": "0.1"},
        {"lhs": "lamR3dd[1,3]", "rhs": "0.1"},
        {"lhs": "lamR3dd[2,1]", "rhs": "-0.1"},
        {"lhs": "lamR3dd[2,2]", "rhs": "0."},
        {"lhs": "lamR3dd[2,3]", "rhs": "0.1"},
        {"lhs": "lamR3dd[3,1]", "rhs": "-0.1"},
        {"lhs": "lamR3dd[3,2]", "rhs": "-0.1"},
        {"lhs": "lamR3dd[3,3]", "rhs": "0."}
      ],
      "tex": "\\lambda_R^{3,dd}",
      "description": "Right-chirality diquark Yukawa of the colour-antitriplet Q=-2/3 state to two down-type quarks, Eq.(2.1). Antisymmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "CD6",
      "parameter_type": "Internal",
      "value": "10/3",
      "tex": "C_D^{(6)}",
      "description": "Quadratic Casimir of SU(3)_C in the colour-sextet diquark representation, Eq.(A.14) with NC=3. Used in the NLO K-factor, Eqs.(4.5) and (4.6)."
    },
    {
      "name": "CD3",
      "parameter_type": "Internal",
      "value": "4/3",
      "tex": "C_D^{(\\bar 3)}",
      "description": "Quadratic Casimir of SU(3)_C in the colour-antitriplet diquark representation, Eq.(A.14) with NC=3; equal to CF."
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "D6uu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MD6uu", "value": "1000."},
      "width": {"sym": "WD6uu", "value": "Automatic"},
      "quantum_numbers": {"Q": "4/3"},
      "pdg": 9000001,
      "particle_name": "d6uu",
      "antiparticle_name": "d6uu~",
      "full_name": "Colour-sextet scalar diquark, Q=4/3 (UU)",
      "propagator_label": "d6uu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "D6ud",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MD6ud", "value": "1000."},
      "width": {"sym": "WD6ud", "value": "Automatic"},
      "quantum_numbers": {"Q": "1/3"},
      "pdg": 9000002,
      "particle_name": "d6ud",
      "antiparticle_name": "d6ud~",
      "full_name": "Colour-sextet scalar diquark, Q=1/3 (QQ, UD)",
      "propagator_label": "d6ud",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "D6dd",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MD6dd", "value": "1000."},
      "width": {"sym": "WD6dd", "value": "Automatic"},
      "quantum_numbers": {"Q": "-2/3"},
      "pdg": 9000003,
      "particle_name": "d6dd",
      "antiparticle_name": "d6dd~",
      "full_name": "Colour-sextet scalar diquark, Q=-2/3 (DD)",
      "propagator_label": "d6dd",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "D3uu",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MD3uu", "value": "1000."},
      "width": {"sym": "WD3uu", "value": "Automatic"},
      "quantum_numbers": {"Q": "4/3"},
      "pdg": 9000004,
      "particle_name": "d3uu",
      "antiparticle_name": "d3uu~",
      "full_name": "Colour-antitriplet scalar diquark, Q=4/3 (UU)",
      "propagator_label": "d3uu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "D3ud",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MD3ud", "value": "1000."},
      "width": {"sym": "WD3ud", "value": "Automatic"},
      "quantum_numbers": {"Q": "1/3"},
      "pdg": 9000005,
      "particle_name": "d3ud",
      "antiparticle_name": "d3ud~",
      "full_name": "Colour-antitriplet scalar diquark, Q=1/3 (QQ, UD)",
      "propagator_label": "d3ud",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "D3dd",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MD3dd", "value": "1000."},
      "width": {"sym": "WD3dd", "value": "Automatic"},
      "quantum_numbers": {"Q": "-2/3"},
      "pdg": 9000006,
      "particle_name": "d3dd",
      "antiparticle_name": "d3dd~",
      "full_name": "Colour-antitriplet scalar diquark, Q=-2/3 (DD)",
      "propagator_label": "d3dd",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LD6Kin",
      "delayed": true,
      "expression": "Block[{mu, ii, jj, kk, gg, hh},\n ExpandIndices[\n   del[D6uubar[ii], mu] del[D6uu[ii], mu] - MD6uu^2 D6uubar[ii] D6uu[ii]\n + I gs T6[gg,ii,jj] G[mu,gg] (D6uubar[ii] del[D6uu[jj], mu] - del[D6uubar[ii], mu] D6uu[jj])\n + gs^2 T6[gg,ii,jj] T6[hh,jj,kk] G[mu,gg] G[mu,hh] D6uubar[ii] D6uu[kk]\n + del[D6udbar[ii], mu] del[D6ud[ii], mu] - MD6ud^2 D6udbar[ii] D6ud[ii]\n + I gs T6[gg,ii,jj] G[mu,gg] (D6udbar[ii] del[D6ud[jj], mu] - del[D6udbar[ii], mu] D6ud[jj])\n + gs^2 T6[gg,ii,jj] T6[hh,jj,kk] G[mu,gg] G[mu,hh] D6udbar[ii] D6ud[kk]\n + del[D6ddbar[ii], mu] del[D6dd[ii], mu] - MD6dd^2 D6ddbar[ii] D6dd[ii]\n + I gs T6[gg,ii,jj] G[mu,gg] (D6ddbar[ii] del[D6dd[jj], mu] - del[D6ddbar[ii], mu] D6dd[jj])\n + gs^2 T6[gg,ii,jj] T6[hh,jj,kk] G[mu,gg] G[mu,hh] D6ddbar[ii] D6dd[kk]\n ]]"
    },
    {
      "name": "LD6EM",
      "delayed": true,
      "expression": "Block[{mu, ii, jj, gg},\n ExpandIndices[\n   I ee (4/3) A[mu] (D6uubar[ii] del[D6uu[ii], mu] - del[D6uubar[ii], mu] D6uu[ii])\n + ee^2 (4/3)^2 A[mu] A[mu] D6uubar[ii] D6uu[ii]\n + 2 gs ee (4/3) T6[gg,ii,jj] G[mu,gg] A[mu] D6uubar[ii] D6uu[jj]\n + I ee (1/3) A[mu] (D6udbar[ii] del[D6ud[ii], mu] - del[D6udbar[ii], mu] D6ud[ii])\n + ee^2 (1/3)^2 A[mu] A[mu] D6udbar[ii] D6ud[ii]\n + 2 gs ee (1/3) T6[gg,ii,jj] G[mu,gg] A[mu] D6udbar[ii] D6ud[jj]\n + I ee (-2/3) A[mu] (D6ddbar[ii] del[D6dd[ii], mu] - del[D6ddbar[ii], mu] D6dd[ii])\n + ee^2 (2/3)^2 A[mu] A[mu] D6ddbar[ii] D6dd[ii]\n + 2 gs ee (-2/3) T6[gg,ii,jj] G[mu,gg] A[mu] D6ddbar[ii] D6dd[jj]\n ]]"
    },
    {
      "name": "LD3Kin",
      "delayed": true,
      "expression": "Block[{mu, cc},\n ExpandIndices[\n   DC[D3uubar[cc], mu] DC[D3uu[cc], mu] - MD3uu^2 D3uubar[cc] D3uu[cc]\n + DC[D3udbar[cc], mu] DC[D3ud[cc], mu] - MD3ud^2 D3udbar[cc] D3ud[cc]\n + DC[D3ddbar[cc], mu] DC[D3dd[cc], mu] - MD3dd^2 D3ddbar[cc] D3dd[cc]\n ]]"
    },
    {
      "name": "LD3EM",
      "delayed": true,
      "expression": "Block[{mu, cc, dd, gg},\n ExpandIndices[\n   I ee (4/3) A[mu] (D3uubar[cc] del[D3uu[cc], mu] - del[D3uubar[cc], mu] D3uu[cc])\n + ee^2 (4/3)^2 A[mu] A[mu] D3uubar[cc] D3uu[cc]\n + 2 gs ee (4/3) T[gg,cc,dd] G[mu,gg] A[mu] D3uubar[cc] D3uu[dd]\n + I ee (1/3) A[mu] (D3udbar[cc] del[D3ud[cc], mu] - del[D3udbar[cc], mu] D3ud[cc])\n + ee^2 (1/3)^2 A[mu] A[mu] D3udbar[cc] D3ud[cc]\n + 2 gs ee (1/3) T[gg,cc,dd] G[mu,gg] A[mu] D3udbar[cc] D3ud[dd]\n + I ee (-2/3) A[mu] (D3ddbar[cc] del[D3dd[cc], mu] - del[D3ddbar[cc], mu] D3dd[cc])\n + ee^2 (2/3)^2 A[mu] A[mu] D3ddbar[cc] D3dd[cc]\n + 2 gs ee (-2/3) T[gg,cc,dd] G[mu,gg] A[mu] D3ddbar[cc] D3dd[dd]\n ]]"
    },
    {
      "name": "LDQ6",
      "delayed": true,
      "expression": "Block[{sp1, sp2, ff1, ff2, ii, aa, bb, ldq6},\n ldq6 = 2 Sqrt[2] K6[ii,aa,bb] (\n     D6uu[ii] ( lamL6uu[ff1,ff2] uqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[uq][sp2,ff2,bb]\n              + lamR6uu[ff1,ff2] uqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[uq][sp2,ff2,bb] )\n   + D6ud[ii] ( lamL6ud[ff1,ff2] uqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[dq][sp2,ff2,bb]\n              + lamR6ud[ff1,ff2] uqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[dq][sp2,ff2,bb] )\n   + D6dd[ii] ( lamL6dd[ff1,ff2] dqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[dq][sp2,ff2,bb]\n              + lamR6dd[ff1,ff2] dqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[dq][sp2,ff2,bb] ) );\n ExpandIndices[ldq6 + HC[ldq6]]]"
    },
    {
      "name": "LDQ3",
      "delayed": true,
      "expression": "Block[{sp1, sp2, ff1, ff2, aa, bb, cc, ldq3},\n ldq3 = 2 Sqrt[2] (Eps[aa,bb,cc]/Sqrt[2]) (\n     D3uu[cc] ( lamL3uu[ff1,ff2] uqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[uq][sp2,ff2,bb]\n              + lamR3uu[ff1,ff2] uqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[uq][sp2,ff2,bb] )\n   + D3ud[cc] ( lamL3ud[ff1,ff2] uqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[dq][sp2,ff2,bb]\n              + lamR3ud[ff1,ff2] uqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[dq][sp2,ff2,bb] )\n   + D3dd[cc] ( lamL3dd[ff1,ff2] dqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[dq][sp2,ff2,bb]\n              + lamR3dd[ff1,ff2] dqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[dq][sp2,ff2,bb] ) );\n ExpandIndices[ldq3 + HC[ldq3]]]"
    },
    {
      "name": "LDiquark",
      "delayed": true,
      "expression": "LD6Kin + LD6EM + LD3Kin + LD3EM + LDQ6 + LDQ3"
    }
  ]
}
```
I read the paper, the schema, the renderer, and SM.fr. No reference or cached `.fr` file for this model exists in the sandbox, and none was read.

## Physics summary

The paper (Han, Lewis, McElmurry, arXiv:0909.2666) adds **scalar diquarks**. Section 2 + Table 1 give the full new-physics content:

- Colour: **6** or **3̄** of SU(3)_C, independently of the electroweak assignment.
- Electroweak options: SU(2) singlet Y=1/3 (couples QQ, UD), SU(2) triplet Y=1/3 (couples QQ), singlet Y=2/3 (couples DD), singlet Y=4/3 (couples UU).
- Coupling, Eq. (2.1), written **after** electroweak symmetry breaking with physical quarks: `L = 2 Sqrt[2] Kbar[i,a,b] D[i] qbar[a] (lamL PL + lamR PR) q^C[b] + h.c.`

**Charge re-derivation (rule 5).** In `D qbar Γ q^C` the bilinear carries −2Q_q, so Q(D) = +2Q_q. Therefore the complete set of diquark charge eigenstates is Q = 4/3 (uu), 1/3 (ud), −2/3 (dd) — exactly the charges spanned by all four rows of Table 1 (the triplet row supplies 4/3, 1/3, −2/3). Table 1 quotes |Q| and lists the DD state as Y = 2/3; the field that appears in Eq. (2.1) has **Q = Y = −2/3**. I use the re-derived sign.

So: 3 charge states × 2 colour reps = **6 new scalars**. Eq. (2.1) is deliberately not SU(2)×U(1) invariant (a Y=4/3 singlet cannot couple to u_L u_L), so `Y` is **not** declared as a quantum number; only `Q` is, and the hypercharge-singlet gauge coupling is written explicitly through the photon.

## Mandatory self-audit table

| term name | fields in monomial | d | coupling symbol | coupling dim (=4−d) | 1/Λ power | Q sum | Y sum | SU(2) contraction | SU(3) contraction | new U(1) | L/B number | CC[] used | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LD6Kin (kin, ×3 states) | `del[D6xxbar]del[D6xx]` | 4 | – | 0 | n/a | −Q+Q=0 | n/a (post-EWSB) | singlet | `ii` shared Sextet | none | B: −2/3+2/3=0 | n/a | self-conjugate pair |
| LD6Kin (mass, ×3) | `M^2 D6xxbar D6xx` | 2 | `MD6xx^2` | 2 ✓ | n/a | 0 | n/a | singlet | Sextet `ii` | none | 0 | n/a | real, self-Hermitian |
| LD6Kin (1-gluon, ×3) | `gs T6 G D6bar del[D6]` | 4 | `gs` | 0 ✓ | n/a | 0 | n/a | singlet | `T6[gg,ii,jj]` | none | 0 | n/a | Hermitian by construction |
| LD6Kin (2-gluon, ×3) | `gs^2 T6 T6 G G D6bar D6` | 4 | `gs^2` | 0 ✓ | n/a | 0 | n/a | singlet | `T6 T6` on Sextet | none | 0 | n/a | Hermitian |
| LD6EM (γ, γγ, γg; ×3) | `ee Q A D6bar del[D6]` etc. | 4 | `ee` | 0 ✓ | n/a | 0 | n/a | singlet | δ / `T6` | none | 0 | n/a | Hermitian |
| LD3Kin (kin+mass+gluon, ×3) | `DC[D3bar]DC[D3]`, `M^2 D3bar D3` | 4 / 2 | – / `MD3xx^2` | 0 / 2 ✓ | n/a | 0 | n/a | singlet | `DC` on Index[Colour] | none | 0 | n/a | Hermitian |
| LD3EM (γ, γγ, γg; ×3) | `ee Q A D3bar del[D3]` etc. | 4 | `ee` | 0 ✓ | n/a | 0 | n/a | singlet | δ / `T[gg,cc,dd]` | none | 0 | n/a | Hermitian |
| LDQ6 uu | `K6 D6uu uqbar.Proj.CC[uq]` | 4 | `lamL6uu`,`lamR6uu` | 0 ✓ | n/a | 4/3−2/3−2/3=0 | n/a (Eq. 2.1 post-EWSB) | none (mass eigenstates) | `K6[ii,aa,bb]`, 6 ⊗ 3̄ ⊗ 3̄ | none | B: 2/3−1/3−1/3=0 | **yes** | `HC[...]` |
| LDQ6 ud | `K6 D6ud uqbar.Proj.CC[dq]` | 4 | `lamL6ud`,`lamR6ud` | 0 ✓ | n/a | 1/3−2/3+1/3=0 | n/a | none | `K6[ii,aa,bb]` | none | 0 | **yes** | `HC[...]` |
| LDQ6 dd | `K6 D6dd dqbar.Proj.CC[dq]` | 4 | `lamL6dd`,`lamR6dd` | 0 ✓ | n/a | −2/3+1/3+1/3=0 | n/a | none | `K6[ii,aa,bb]` | none | 0 | **yes** | `HC[...]` |
| LDQ3 uu | `Eps D3uu uqbar.Proj.CC[uq]` | 4 | `lamL3uu`,`lamR3uu` (antisym.) | 0 ✓ | n/a | 4/3−2/3−2/3=0 | n/a | none | `Eps[aa,bb,cc]/Sqrt[2]` | none | 0 | **yes** | `HC[...]` |
| LDQ3 ud | `Eps D3ud uqbar.Proj.CC[dq]` | 4 | `lamL3ud`,`lamR3ud` | 0 ✓ | n/a | 1/3−2/3+1/3=0 | n/a | none | `Eps[aa,bb,cc]/Sqrt[2]` | none | 0 | **yes** | `HC[...]` |
| LDQ3 dd | `Eps D3dd dqbar.Proj.CC[dq]` | 4 | `lamL3dd`,`lamR3dd` (antisym.) | 0 ✓ | n/a | −2/3+1/3+1/3=0 | n/a | none | `Eps[aa,bb,cc]/Sqrt[2]` | none | 0 | **yes** | `HC[...]` |

Per-class free-field check (all six appear in the total sum `LDiquark`): `D6uu` (LD6Kin), `D6ud` (LD6Kin), `D6dd` (LD6Kin), `D3uu` (LD3Kin), `D3ud` (LD3Kin), `D3dd` (LD3Kin). Every class uses the mass symbol from its own `Mass -> {M, value}` spec.

`SelfConjugate -> True` classes: **none** — all six diquarks are complex, so none carries the forbidden combination of quantum numbers on a self-conjugate class.

No EFT cutoff is needed: every operator has d = 4 or less, so all couplings are dimensionless (`lam*`) or of dimension 2 (`M^2`).

Reference or cached model file read: **none**.

```json
{
  "model_name": "Sextets_gen",
  "info": {
    "authors": ["Tao Han", "Ian Lewis", "Thomas McElmurry"],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["Department of Physics, University of Wisconsin, Madison"],
    "emails": ["than@hep.wisc.edu", "ilewis@wisc.edu", "mcelmurry@hep.wisc.edu"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [
    {
      "name": "Sextet",
      "range_kind": "NoUnfold",
      "size": 6,
      "style_symbol": "st"
    }
  ],
  "parameters": [
    {
      "name": "K6",
      "parameter_type": "Internal",
      "complex": false,
      "indices": ["Sextet", "Colour", "Colour"],
      "value_rules": [
        {"lhs": "K6[1,1,1]", "rhs": "1"},
        {"lhs": "K6[1,1,2]", "rhs": "0"},
        {"lhs": "K6[1,1,3]", "rhs": "0"},
        {"lhs": "K6[1,2,1]", "rhs": "0"},
        {"lhs": "K6[1,2,2]", "rhs": "0"},
        {"lhs": "K6[1,2,3]", "rhs": "0"},
        {"lhs": "K6[1,3,1]", "rhs": "0"},
        {"lhs": "K6[1,3,2]", "rhs": "0"},
        {"lhs": "K6[1,3,3]", "rhs": "0"},
        {"lhs": "K6[2,1,1]", "rhs": "0"},
        {"lhs": "K6[2,1,2]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[2,1,3]", "rhs": "0"},
        {"lhs": "K6[2,2,1]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[2,2,2]", "rhs": "0"},
        {"lhs": "K6[2,2,3]", "rhs": "0"},
        {"lhs": "K6[2,3,1]", "rhs": "0"},
        {"lhs": "K6[2,3,2]", "rhs": "0"},
        {"lhs": "K6[2,3,3]", "rhs": "0"},
        {"lhs": "K6[3,1,1]", "rhs": "0"},
        {"lhs": "K6[3,1,2]", "rhs": "0"},
        {"lhs": "K6[3,1,3]", "rhs": "0"},
        {"lhs": "K6[3,2,1]", "rhs": "0"},
        {"lhs": "K6[3,2,2]", "rhs": "1"},
        {"lhs": "K6[3,2,3]", "rhs": "0"},
        {"lhs": "K6[3,3,1]", "rhs": "0"},
        {"lhs": "K6[3,3,2]", "rhs": "0"},
        {"lhs": "K6[3,3,3]", "rhs": "0"},
        {"lhs": "K6[4,1,1]", "rhs": "0"},
        {"lhs": "K6[4,1,2]", "rhs": "0"},
        {"lhs": "K6[4,1,3]", "rhs": "0"},
        {"lhs": "K6[4,2,1]", "rhs": "0"},
        {"lhs": "K6[4,2,2]", "rhs": "0"},
        {"lhs": "K6[4,2,3]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[4,3,1]", "rhs": "0"},
        {"lhs": "K6[4,3,2]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[4,3,3]", "rhs": "0"},
        {"lhs": "K6[5,1,1]", "rhs": "0"},
        {"lhs": "K6[5,1,2]", "rhs": "0"},
        {"lhs": "K6[5,1,3]", "rhs": "0"},
        {"lhs": "K6[5,2,1]", "rhs": "0"},
        {"lhs": "K6[5,2,2]", "rhs": "0"},
        {"lhs": "K6[5,2,3]", "rhs": "0"},
        {"lhs": "K6[5,3,1]", "rhs": "0"},
        {"lhs": "K6[5,3,2]", "rhs": "0"},
        {"lhs": "K6[5,3,3]", "rhs": "1"},
        {"lhs": "K6[6,1,1]", "rhs": "0"},
        {"lhs": "K6[6,1,2]", "rhs": "0"},
        {"lhs": "K6[6,1,3]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[6,2,1]", "rhs": "0"},
        {"lhs": "K6[6,2,2]", "rhs": "0"},
        {"lhs": "K6[6,2,3]", "rhs": "0"},
        {"lhs": "K6[6,3,1]", "rhs": "1/Sqrt[2]"},
        {"lhs": "K6[6,3,2]", "rhs": "0"},
        {"lhs": "K6[6,3,3]", "rhs": "0"}
      ],
      "tex": "K",
      "description": "Clebsch-Gordan coefficients K^{i a b} that couple the colour sextet to two colour triplets, Eq.(A.6). Symmetric in the two Colour indices. The antitriplet case uses K_{abc} = Eps[a,b,c]/Sqrt[2], Eq.(A.7), written directly in the Lagrangian."
    },
    {
      "name": "T6",
      "parameter_type": "Internal",
      "complex": true,
      "indices": ["Gluon", "Sextet", "Sextet"],
      "definitions": [
        {
          "lhs": "T6[gg_?NumericQ, ii_?NumericQ, jj_?NumericQ]",
          "rhs": "2 Sum[K6[ii,aa,bb] T[gg,bb,cc] K6[jj,aa,cc], {aa,3}, {bb,3}, {cc,3}]",
          "delayed": true
        }
      ],
      "tex": "\\mathcal{T}",
      "description": "SU(3)_C generators in the colour-sextet (diquark) representation, Eq.(A.12): T^A_{ij} = 2 Tr(K^i t^A Kbar^j). They satisfy [T^A,T^B] = I f^{ABC} T^C and T^A T^A = CD = 10/3, Eq.(A.14)."
    },
    {
      "name": "lamL6uu",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6UUL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL6uu[1,1]", "rhs": "0.1"},
        {"lhs": "lamL6uu[1,2]", "rhs": "0.1"},
        {"lhs": "lamL6uu[1,3]", "rhs": "0.1"},
        {"lhs": "lamL6uu[2,1]", "rhs": "0.1"},
        {"lhs": "lamL6uu[2,2]", "rhs": "0.1"},
        {"lhs": "lamL6uu[2,3]", "rhs": "0.1"},
        {"lhs": "lamL6uu[3,1]", "rhs": "0.1"},
        {"lhs": "lamL6uu[3,2]", "rhs": "0.1"},
        {"lhs": "lamL6uu[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_L^{6,uu}",
      "description": "Left-chirality diquark Yukawa of the colour-sextet Q=4/3 state to two up-type quarks, Eq.(2.1). Symmetric in generation because the sextet colour tensor K6 is symmetric. Dimensionless; benchmark 0.1. The left-handed couplings are tightly constrained by minimal flavour violation."
    },
    {
      "name": "lamR6uu",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6UUR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR6uu[1,1]", "rhs": "0.1"},
        {"lhs": "lamR6uu[1,2]", "rhs": "0.1"},
        {"lhs": "lamR6uu[1,3]", "rhs": "0.1"},
        {"lhs": "lamR6uu[2,1]", "rhs": "0.1"},
        {"lhs": "lamR6uu[2,2]", "rhs": "0."},
        {"lhs": "lamR6uu[2,3]", "rhs": "0.1"},
        {"lhs": "lamR6uu[3,1]", "rhs": "0.1"},
        {"lhs": "lamR6uu[3,2]", "rhs": "0.1"},
        {"lhs": "lamR6uu[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_R^{6,uu}",
      "description": "Right-chirality diquark Yukawa of the colour-sextet Q=4/3 state to two up-type quarks, Eq.(2.1). Symmetric in generation. Benchmark from Eq.(2.2): lamR[uu], lamR[uc] <~ 0.1 and lamR[cc] ~ 0 from D0-D0bar mixing and D -> pi pi."
    },
    {
      "name": "lamL6ud",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6UDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL6ud[1,1]", "rhs": "0.1"},
        {"lhs": "lamL6ud[1,2]", "rhs": "0.1"},
        {"lhs": "lamL6ud[1,3]", "rhs": "0.1"},
        {"lhs": "lamL6ud[2,1]", "rhs": "0.1"},
        {"lhs": "lamL6ud[2,2]", "rhs": "0.1"},
        {"lhs": "lamL6ud[2,3]", "rhs": "0.1"},
        {"lhs": "lamL6ud[3,1]", "rhs": "0.1"},
        {"lhs": "lamL6ud[3,2]", "rhs": "0.1"},
        {"lhs": "lamL6ud[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_L^{6,ud}",
      "description": "Left-chirality diquark Yukawa of the colour-sextet Q=1/3 state to one up-type and one down-type quark, Eq.(2.1) (Table 1 rows QQ and UD). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR6ud",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6UDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR6ud[1,1]", "rhs": "0.1"},
        {"lhs": "lamR6ud[1,2]", "rhs": "0.1"},
        {"lhs": "lamR6ud[1,3]", "rhs": "0.1"},
        {"lhs": "lamR6ud[2,1]", "rhs": "0.1"},
        {"lhs": "lamR6ud[2,2]", "rhs": "0.1"},
        {"lhs": "lamR6ud[2,3]", "rhs": "0.1"},
        {"lhs": "lamR6ud[3,1]", "rhs": "0.1"},
        {"lhs": "lamR6ud[3,2]", "rhs": "0.1"},
        {"lhs": "lamR6ud[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_R^{6,ud}",
      "description": "Right-chirality diquark Yukawa of the colour-sextet Q=1/3 state to one up-type and one down-type quark, Eq.(2.1). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamL6dd",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6DDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL6dd[1,1]", "rhs": "0.1"},
        {"lhs": "lamL6dd[1,2]", "rhs": "0.1"},
        {"lhs": "lamL6dd[1,3]", "rhs": "0.1"},
        {"lhs": "lamL6dd[2,1]", "rhs": "0.1"},
        {"lhs": "lamL6dd[2,2]", "rhs": "0.1"},
        {"lhs": "lamL6dd[2,3]", "rhs": "0.1"},
        {"lhs": "lamL6dd[3,1]", "rhs": "0.1"},
        {"lhs": "lamL6dd[3,2]", "rhs": "0.1"},
        {"lhs": "lamL6dd[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_L^{6,dd}",
      "description": "Left-chirality diquark Yukawa of the colour-sextet Q=-2/3 state to two down-type quarks, Eq.(2.1) (Table 1 row DD). Symmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR6dd",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ6DDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR6dd[1,1]", "rhs": "0.1"},
        {"lhs": "lamR6dd[1,2]", "rhs": "0.1"},
        {"lhs": "lamR6dd[1,3]", "rhs": "0.1"},
        {"lhs": "lamR6dd[2,1]", "rhs": "0.1"},
        {"lhs": "lamR6dd[2,2]", "rhs": "0.1"},
        {"lhs": "lamR6dd[2,3]", "rhs": "0.1"},
        {"lhs": "lamR6dd[3,1]", "rhs": "0.1"},
        {"lhs": "lamR6dd[3,2]", "rhs": "0.1"},
        {"lhs": "lamR6dd[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_R^{6,dd}",
      "description": "Right-chirality diquark Yukawa of the colour-sextet Q=-2/3 state to two down-type quarks, Eq.(2.1). Symmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamL3uu",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3UUL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL3uu[1,1]", "rhs": "0."},
        {"lhs": "lamL3uu[1,2]", "rhs": "0.1"},
        {"lhs": "lamL3uu[1,3]", "rhs": "0.1"},
        {"lhs": "lamL3uu[2,1]", "rhs": "-0.1"},
        {"lhs": "lamL3uu[2,2]", "rhs": "0."},
        {"lhs": "lamL3uu[2,3]", "rhs": "0.1"},
        {"lhs": "lamL3uu[3,1]", "rhs": "-0.1"},
        {"lhs": "lamL3uu[3,2]", "rhs": "-0.1"},
        {"lhs": "lamL3uu[3,3]", "rhs": "0."}
      ],
      "tex": "\\lambda_L^{3,uu}",
      "description": "Left-chirality diquark Yukawa of the colour-antitriplet Q=4/3 state to two up-type quarks, Eq.(2.1). Antisymmetric in generation because the antitriplet colour tensor Eps is antisymmetric (Section 2). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR3uu",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3UUR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR3uu[1,1]", "rhs": "0."},
        {"lhs": "lamR3uu[1,2]", "rhs": "0.1"},
        {"lhs": "lamR3uu[1,3]", "rhs": "0.1"},
        {"lhs": "lamR3uu[2,1]", "rhs": "-0.1"},
        {"lhs": "lamR3uu[2,2]", "rhs": "0."},
        {"lhs": "lamR3uu[2,3]", "rhs": "0.1"},
        {"lhs": "lamR3uu[3,1]", "rhs": "-0.1"},
        {"lhs": "lamR3uu[3,2]", "rhs": "-0.1"},
        {"lhs": "lamR3uu[3,3]", "rhs": "0."}
      ],
      "tex": "\\lambda_R^{3,uu}",
      "description": "Right-chirality diquark Yukawa of the colour-antitriplet Q=4/3 state to two up-type quarks, Eq.(2.1). Antisymmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamL3ud",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3UDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL3ud[1,1]", "rhs": "0.1"},
        {"lhs": "lamL3ud[1,2]", "rhs": "0.1"},
        {"lhs": "lamL3ud[1,3]", "rhs": "0.1"},
        {"lhs": "lamL3ud[2,1]", "rhs": "0.1"},
        {"lhs": "lamL3ud[2,2]", "rhs": "0.1"},
        {"lhs": "lamL3ud[2,3]", "rhs": "0.1"},
        {"lhs": "lamL3ud[3,1]", "rhs": "0.1"},
        {"lhs": "lamL3ud[3,2]", "rhs": "0.1"},
        {"lhs": "lamL3ud[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_L^{3,ud}",
      "description": "Left-chirality diquark Yukawa of the colour-antitriplet Q=1/3 state to one up-type and one down-type quark, Eq.(2.1). This is the state produced from the du and ds initial states of Figs. 4(a), 5(a). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR3ud",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3UDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR3ud[1,1]", "rhs": "0.1"},
        {"lhs": "lamR3ud[1,2]", "rhs": "0.1"},
        {"lhs": "lamR3ud[1,3]", "rhs": "0.1"},
        {"lhs": "lamR3ud[2,1]", "rhs": "0.1"},
        {"lhs": "lamR3ud[2,2]", "rhs": "0.1"},
        {"lhs": "lamR3ud[2,3]", "rhs": "0.1"},
        {"lhs": "lamR3ud[3,1]", "rhs": "0.1"},
        {"lhs": "lamR3ud[3,2]", "rhs": "0.1"},
        {"lhs": "lamR3ud[3,3]", "rhs": "0.1"}
      ],
      "tex": "\\lambda_R^{3,ud}",
      "description": "Right-chirality diquark Yukawa of the colour-antitriplet Q=1/3 state to one up-type and one down-type quark, Eq.(2.1). Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamL3dd",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3DDL",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamL3dd[1,1]", "rhs": "0."},
        {"lhs": "lamL3dd[1,2]", "rhs": "0.1"},
        {"lhs": "lamL3dd[1,3]", "rhs": "0.1"},
        {"lhs": "lamL3dd[2,1]", "rhs": "-0.1"},
        {"lhs": "lamL3dd[2,2]", "rhs": "0."},
        {"lhs": "lamL3dd[2,3]", "rhs": "0.1"},
        {"lhs": "lamL3dd[3,1]", "rhs": "-0.1"},
        {"lhs": "lamL3dd[3,2]", "rhs": "-0.1"},
        {"lhs": "lamL3dd[3,3]", "rhs": "0."}
      ],
      "tex": "\\lambda_L^{3,dd}",
      "description": "Left-chirality diquark Yukawa of the colour-antitriplet Q=-2/3 state to two down-type quarks, Eq.(2.1). Antisymmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "lamR3dd",
      "parameter_type": "External",
      "complex": false,
      "indices": ["Generation", "Generation"],
      "block_name": "DQ3DDR",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "lamR3dd[1,1]", "rhs": "0."},
        {"lhs": "lamR3dd[1,2]", "rhs": "0.1"},
        {"lhs": "lamR3dd[1,3]", "rhs": "0.1"},
        {"lhs": "lamR3dd[2,1]", "rhs": "-0.1"},
        {"lhs": "lamR3dd[2,2]", "rhs": "0."},
        {"lhs": "lamR3dd[2,3]", "rhs": "0.1"},
        {"lhs": "lamR3dd[3,1]", "rhs": "-0.1"},
        {"lhs": "lamR3dd[3,2]", "rhs": "-0.1"},
        {"lhs": "lamR3dd[3,3]", "rhs": "0."}
      ],
      "tex": "\\lambda_R^{3,dd}",
      "description": "Right-chirality diquark Yukawa of the colour-antitriplet Q=-2/3 state to two down-type quarks, Eq.(2.1). Antisymmetric in generation. Dimensionless; benchmark 0.1."
    },
    {
      "name": "CD6",
      "parameter_type": "Internal",
      "value": "10/3",
      "tex": "C_D^{(6)}",
      "description": "Quadratic Casimir of SU(3)_C in the colour-sextet diquark representation, Eq.(A.14) with NC=3. Used in the NLO K-factor, Eqs.(4.5) and (4.6)."
    },
    {
      "name": "CD3",
      "parameter_type": "Internal",
      "value": "4/3",
      "tex": "C_D^{(\\bar 3)}",
      "description": "Quadratic Casimir of SU(3)_C in the colour-antitriplet diquark representation, Eq.(A.14) with NC=3; equal to CF."
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "D6uu",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MD6uu", "value": "1000."},
      "width": {"sym": "WD6uu", "value": "Automatic"},
      "quantum_numbers": {"Q": "4/3"},
      "pdg": 9000001,
      "particle_name": "d6uu",
      "antiparticle_name": "d6uu~",
      "full_name": "Colour-sextet scalar diquark, Q=4/3 (UU)",
      "propagator_label": "d6uu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "D6ud",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MD6ud", "value": "1000."},
      "width": {"sym": "WD6ud", "value": "Automatic"},
      "quantum_numbers": {"Q": "1/3"},
      "pdg": 9000002,
      "particle_name": "d6ud",
      "antiparticle_name": "d6ud~",
      "full_name": "Colour-sextet scalar diquark, Q=1/3 (QQ, UD)",
      "propagator_label": "d6ud",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "D6dd",
      "self_conjugate": false,
      "indices": ["Sextet"],
      "mass": {"sym": "MD6dd", "value": "1000."},
      "width": {"sym": "WD6dd", "value": "Automatic"},
      "quantum_numbers": {"Q": "-2/3"},
      "pdg": 9000003,
      "particle_name": "d6dd",
      "antiparticle_name": "d6dd~",
      "full_name": "Colour-sextet scalar diquark, Q=-2/3 (DD)",
      "propagator_label": "d6dd",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "D3uu",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MD3uu", "value": "1000."},
      "width": {"sym": "WD3uu", "value": "Automatic"},
      "quantum_numbers": {"Q": "4/3"},
      "pdg": 9000004,
      "particle_name": "d3uu",
      "antiparticle_name": "d3uu~",
      "full_name": "Colour-antitriplet scalar diquark, Q=4/3 (UU)",
      "propagator_label": "d3uu",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "D3ud",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MD3ud", "value": "1000."},
      "width": {"sym": "WD3ud", "value": "Automatic"},
      "quantum_numbers": {"Q": "1/3"},
      "pdg": 9000005,
      "particle_name": "d3ud",
      "antiparticle_name": "d3ud~",
      "full_name": "Colour-antitriplet scalar diquark, Q=1/3 (QQ, UD)",
      "propagator_label": "d3ud",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "D3dd",
      "self_conjugate": false,
      "indices": ["Colour"],
      "mass": {"sym": "MD3dd", "value": "1000."},
      "width": {"sym": "WD3dd", "value": "Automatic"},
      "quantum_numbers": {"Q": "-2/3"},
      "pdg": 9000006,
      "particle_name": "d3dd",
      "antiparticle_name": "d3dd~",
      "full_name": "Colour-antitriplet scalar diquark, Q=-2/3 (DD)",
      "propagator_label": "d3dd",
      "propagator_type": "ScalarDash",
      "propagator_arrow": "Forward",
      "definitions": []
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LD6Kin",
      "delayed": true,
      "expression": "Block[{mu, ii, jj, kk, gg, hh},\n ExpandIndices[\n   del[D6uubar[ii], mu] del[D6uu[ii], mu] - MD6uu^2 D6uubar[ii] D6uu[ii]\n + I gs T6[gg,ii,jj] G[mu,gg] (D6uubar[ii] del[D6uu[jj], mu] - del[D6uubar[ii], mu] D6uu[jj])\n + gs^2 T6[gg,ii,jj] T6[hh,jj,kk] G[mu,gg] G[mu,hh] D6uubar[ii] D6uu[kk]\n + del[D6udbar[ii], mu] del[D6ud[ii], mu] - MD6ud^2 D6udbar[ii] D6ud[ii]\n + I gs T6[gg,ii,jj] G[mu,gg] (D6udbar[ii] del[D6ud[jj], mu] - del[D6udbar[ii], mu] D6ud[jj])\n + gs^2 T6[gg,ii,jj] T6[hh,jj,kk] G[mu,gg] G[mu,hh] D6udbar[ii] D6ud[kk]\n + del[D6ddbar[ii], mu] del[D6dd[ii], mu] - MD6dd^2 D6ddbar[ii] D6dd[ii]\n + I gs T6[gg,ii,jj] G[mu,gg] (D6ddbar[ii] del[D6dd[jj], mu] - del[D6ddbar[ii], mu] D6dd[jj])\n + gs^2 T6[gg,ii,jj] T6[hh,jj,kk] G[mu,gg] G[mu,hh] D6ddbar[ii] D6dd[kk]\n ]]"
    },
    {
      "name": "LD6EM",
      "delayed": true,
      "expression": "Block[{mu, ii, jj, gg},\n ExpandIndices[\n   I ee (4/3) A[mu] (D6uubar[ii] del[D6uu[ii], mu] - del[D6uubar[ii], mu] D6uu[ii])\n + ee^2 (4/3)^2 A[mu] A[mu] D6uubar[ii] D6uu[ii]\n + 2 gs ee (4/3) T6[gg,ii,jj] G[mu,gg] A[mu] D6uubar[ii] D6uu[jj]\n + I ee (1/3) A[mu] (D6udbar[ii] del[D6ud[ii], mu] - del[D6udbar[ii], mu] D6ud[ii])\n + ee^2 (1/3)^2 A[mu] A[mu] D6udbar[ii] D6ud[ii]\n + 2 gs ee (1/3) T6[gg,ii,jj] G[mu,gg] A[mu] D6udbar[ii] D6ud[jj]\n + I ee (-2/3) A[mu] (D6ddbar[ii] del[D6dd[ii], mu] - del[D6ddbar[ii], mu] D6dd[ii])\n + ee^2 (2/3)^2 A[mu] A[mu] D6ddbar[ii] D6dd[ii]\n + 2 gs ee (-2/3) T6[gg,ii,jj] G[mu,gg] A[mu] D6ddbar[ii] D6dd[jj]\n ]]"
    },
    {
      "name": "LD3Kin",
      "delayed": true,
      "expression": "Block[{mu, cc},\n ExpandIndices[\n   DC[D3uubar[cc], mu] DC[D3uu[cc], mu] - MD3uu^2 D3uubar[cc] D3uu[cc]\n + DC[D3udbar[cc], mu] DC[D3ud[cc], mu] - MD3ud^2 D3udbar[cc] D3ud[cc]\n + DC[D3ddbar[cc], mu] DC[D3dd[cc], mu] - MD3dd^2 D3ddbar[cc] D3dd[cc]\n ]]"
    },
    {
      "name": "LD3EM",
      "delayed": true,
      "expression": "Block[{mu, cc, dd, gg},\n ExpandIndices[\n   I ee (4/3) A[mu] (D3uubar[cc] del[D3uu[cc], mu] - del[D3uubar[cc], mu] D3uu[cc])\n + ee^2 (4/3)^2 A[mu] A[mu] D3uubar[cc] D3uu[cc]\n + 2 gs ee (4/3) T[gg,cc,dd] G[mu,gg] A[mu] D3uubar[cc] D3uu[dd]\n + I ee (1/3) A[mu] (D3udbar[cc] del[D3ud[cc], mu] - del[D3udbar[cc], mu] D3ud[cc])\n + ee^2 (1/3)^2 A[mu] A[mu] D3udbar[cc] D3ud[cc]\n + 2 gs ee (1/3) T[gg,cc,dd] G[mu,gg] A[mu] D3udbar[cc] D3ud[dd]\n + I ee (-2/3) A[mu] (D3ddbar[cc] del[D3dd[cc], mu] - del[D3ddbar[cc], mu] D3dd[cc])\n + ee^2 (2/3)^2 A[mu] A[mu] D3ddbar[cc] D3dd[cc]\n + 2 gs ee (-2/3) T[gg,cc,dd] G[mu,gg] A[mu] D3ddbar[cc] D3dd[dd]\n ]]"
    },
    {
      "name": "LDQ6",
      "delayed": true,
      "expression": "Block[{sp1, sp2, ff1, ff2, ii, aa, bb, ldq6},\n ldq6 = 2 Sqrt[2] K6[ii,aa,bb] (\n     D6uu[ii] ( lamL6uu[ff1,ff2] uqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[uq][sp2,ff2,bb]\n              + lamR6uu[ff1,ff2] uqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[uq][sp2,ff2,bb] )\n   + D6ud[ii] ( lamL6ud[ff1,ff2] uqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[dq][sp2,ff2,bb]\n              + lamR6ud[ff1,ff2] uqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[dq][sp2,ff2,bb] )\n   + D6dd[ii] ( lamL6dd[ff1,ff2] dqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[dq][sp2,ff2,bb]\n              + lamR6dd[ff1,ff2] dqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[dq][sp2,ff2,bb] ) );\n ExpandIndices[ldq6 + HC[ldq6]]]"
    },
    {
      "name": "LDQ3",
      "delayed": true,
      "expression": "Block[{sp1, sp2, ff1, ff2, aa, bb, cc, ldq3},\n ldq3 = 2 Sqrt[2] (Eps[aa,bb,cc]/Sqrt[2]) (\n     D3uu[cc] ( lamL3uu[ff1,ff2] uqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[uq][sp2,ff2,bb]\n              + lamR3uu[ff1,ff2] uqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[uq][sp2,ff2,bb] )\n   + D3ud[cc] ( lamL3ud[ff1,ff2] uqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[dq][sp2,ff2,bb]\n              + lamR3ud[ff1,ff2] uqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[dq][sp2,ff2,bb] )\n   + D3dd[cc] ( lamL3dd[ff1,ff2] dqbar[sp1,ff1,aa].ProjM[sp1,sp2].CC[dq][sp2,ff2,bb]\n              + lamR3dd[ff1,ff2] dqbar[sp1,ff1,aa].ProjP[sp1,sp2].CC[dq][sp2,ff2,bb] ) );\n ExpandIndices[ldq3 + HC[ldq3]]]"
    },
    {
      "name": "LDiquark",
      "delayed": true,
      "expression": "LD6Kin + LD6EM + LD3Kin + LD3EM + LDQ6 + LDQ3"
    }
  ]
}
```