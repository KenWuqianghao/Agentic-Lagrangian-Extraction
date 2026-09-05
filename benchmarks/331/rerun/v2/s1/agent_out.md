I'll start by reading the paper and the schema.
Let me read the SM.fr conventions and more of the paper.
I have the paper, the schema, and the SM.fr conventions. Below is the mandatory self-audit, then the model.

## Model choices (stated up front)

- **β fixed to +√3** (Table 1, last column). FeynRules `QuantumNumbers` must be numeric, so one benchmark must be chosen: Q(Y)=+2, Q(V)=+1, Q(D)=Q(S)=−4/3, Q(T)=+5/3, Q(E<sub>ℓ</sub>)=+1, Q(H<sup>QY</sup>)=+2, Q(H<sup>QV</sup>)=+1. `bet` stays symbolic (Internal = `Sqrt[3]`) in every coupling, so a different β needs only new charge labels.
- **New U(1)<sub>X</sub> charges re-derived** from the paper's own Q = T³ + βT⁸ + X (Eq. 2.5), not copied from Eq. (2.6). The printed Eq. (2.6) (X<sub>ρ</sub> = 1/2 − √3β/2) contradicts Eq. (2.5); the correct values are X<sub>ρ</sub> = 1/2 − β/(2√3) = 0, X<sub>η</sub> = −1/2 − β/(2√3) = −1, X<sub>χ</sub> = β/√3 = +1, X<sub>q1,q2</sub> = −1/3, X<sub>q3</sub> = +2/3, X<sub>l</sub> = 0, X<sub>fR</sub> = Q<sub>f</sub>. Sign choice: ρ is the Y=+1/2 doublet (SM.fr `Phi` role), η the Y=−1/2 one; all SM and new Yukawas are then invariant.
- **Validation**: my Z′ couplings reproduce Table 11 exactly (e.g. ūuZ′ g<sub>L</sub> = e[(β+√3)s<sub>W</sub>²−√3]/(6c<sub>W</sub>s<sub>W</sub>a₀), D̄DZ′ g<sub>R</sub>, D̄DZ), and my Yukawa expansion reproduces Table 12 (H₃ĒE = U₃₃M<sub>E</sub>/v₃, H₂ūu = U₂₂m<sub>u</sub>/v₂, H⁺ν̄ℓ = √2 m<sub>ℓ</sub>c₁₂/v₂, H<sup>+QY</sup>ūD).
- (Y, V) is an SU(2)<sub>L</sub> doublet with Y = √3β/2 = 3/2, so it is declared as the unphysical doublet `WY`; `DC` then gives the correct γ, Z and W±YV couplings. The heavy fermions and H<sup>QY</sup>, H<sup>QV</sup> are true SU(2) singlets with Y = Q. H± is treated as a singlet with Y = Q: exact QED coupling, approximate Z coupling.
- Scalar triplets are written in unitary gauge **without vevs** (fluctuations only), so the add-on adds to `LSM` with no double counting of the SM Yukawa; the vev pieces are resummed into the declared masses.

## Self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3)c | U(1)X sum | L/B | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin (kin) | FS[Zp]FS[Zp] | 4 | 1/4 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | real field |
| LZpkin (mass) | Zp Zp | 2 | MZp² | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | real field |
| LYVkin (kin) | (D<sub>[μ</sub>WYbar<sub>ν]</sub>)(D<sup>[μ</sup>WY<sup>ν]</sup>) | 4 | 1/2 | 0 | n/a | 0 | −3/2+3/2=0 | doublet · anti-doublet, shared `ii` | singlet | 0 | 0 | n/a | self-conj pair |
| LYVkin (mass) | Ypbar Yp, Vpbar Vp | 2 | MYp², MVp² | 2 | n/a | 0 | 0 | shared | singlet | 0 | 0 | n/a | self-conj pair |
| LNPS (H2,H3,H0) | del·del, φ² | 4 / 2 | 1/2, MH²/2 | 0 / 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | real fields |
| LNPS (Hp,HY,HV) | (DHbar)(DH), Hbar H | 4 / 2 | 1, MH² | 0 / 2 | n/a | 0 | 0 | singlet (Y=Q) | singlet | 0 | 0 | n/a | bar·field |
| LNPF (kin) | ψ̄ γ Dψ, ψ = DQ,SQ,TQ,EL | 4 | 1 | 0 | n/a | 0 | 0 | singlet | 3⊗3̄ | 0 | 0 | n/a | self-conj |
| LNPF (mass) | ψ̄ψ | 3 | M<sub>ψ</sub> | 1 | n/a | 0 | 0 | singlet | 3⊗3̄ | 0 | 0 | n/a | self-conj |
| LZpF (q1L,q2L, ii=1,2) | q̄<sub>L</sub>γq<sub>L</sub>Zp | 4 | gZqL | 0 | n/a | 0 | 0 | same component | 3⊗3̄ | +1/3−1/3=0 | B=0 | n/a | self-conj |
| LZpF (q1L,q2L, ii=3) | D̄<sub>L</sub>γD<sub>L</sub>Zp | 4 | gZqJ | 0 | n/a | 0 | 0 | singlet | 3⊗3̄ | 0 | 0 | n/a | self-conj |
| LZpF (q3L, ii=1,2 / 3) | b̄,t̄,T̄ γ · Zp | 4 | gZq3L, gZq3T | 0 | n/a | 0 | 0 | same component | 3⊗3̄ | 0 | 0 | n/a | self-conj |
| LZpF (lL, ii=1,2 / 3) | ℓ̄,ν̄,Ē γ · Zp | 4 | gZlL, gZlE | 0 | n/a | 0 | 0 | same component | singlet | 0 | L=0 | n/a | self-conj |
| LZpF (RH: uR,dR,lR,DQ,SQ,TQ,EL) | f̄<sub>R</sub>γf<sub>R</sub>Zp | 4 | gZRu…gZRE | 0 | n/a | 0 | 0 | singlet | 3⊗3̄ / singlet | X<sub>fR</sub>−X<sub>fR</sub>=0 | 0 | n/a | self-conj |
| LYVF ūD Y⁺ | ū<sub>L</sub>γD<sub>L</sub>Yp | 4 | gw/√2 | 0 | n/a | −2/3−4/3+2=0 | −1/6−4/3+3/2=0 | doublet(u)·singlet(D)·Y(T³=+1/2) | 3̄⊗3, shared `cc` | +1/3−1/3+0=0 | B=0 | n/a | HC[lag] |
| LYVF d̄D V⁺ | d̄<sub>L</sub>γD<sub>L</sub>Vp | 4 | gw/√2 | 0 | n/a | 1/3−4/3+1=0 | −1/6−4/3+3/2=0 | doublet(d)·singlet·V(T³=−1/2) | shared `cc` | 0 | 0 | n/a | HC[lag] |
| LYVF T̄b Y⁺ | T̄<sub>L</sub>γb<sub>L</sub>Yp | 4 | −gw/√2 | 0 | n/a | −5/3−1/3+2=0 | −5/3+1/6+3/2=0 | singlet·doublet·Y | shared `cc` | −2/3+2/3=0 | 0 | n/a | HC[lag] |
| LYVF T̄t V⁺ | T̄<sub>L</sub>γt<sub>L</sub>Vp | 4 | −gw/√2 | 0 | n/a | −5/3+2/3+1=0 | 0 | singlet·doublet·V | shared `cc` | 0 | 0 | n/a | HC[lag] |
| LYVF Ēℓ Y⁺ | Ē<sub>L</sub>γℓ<sub>L</sub>Yp | 4 | −gw/√2 | 0 | n/a | −1−1+2=0 | −1−1/2+3/2=0 | singlet·doublet·Y | singlet | 0 | L: −1+1=0 | n/a | HC[lag] |
| LYVF Ēν V⁺ | Ē<sub>L</sub>γν<sub>L</sub>Vp | 4 | −gw/√2 | 0 | n/a | −1+0+1=0 | −1−1/2+3/2=0 | singlet·doublet·V | singlet | 0 | L=0 | n/a | HC[lag] |
| LYuk331 q̄1L η u<sub>R</sub> (all 3 comps) | q̄<sub>L</sub>u<sub>R</sub>η | 4 | yu331[1] | 0 | n/a | 0 per component | SSB basis (Q only) | shared `ii` (3̄⊗3) | shared `cc` | +1/3+2/3−1=0 | B=0 | n/a | HC[lag] |
| LYuk331 q̄3L ρ* t<sub>R</sub> | q̄<sub>L</sub>t<sub>R</sub>ρbar | 4 | yu331[3] | 0 | n/a | 0 | SSB | shared `ii` (3⊗3̄) | shared `cc` | −2/3+2/3−0=0 | 0 | n/a | HC[lag] |
| LYuk331 q̄1L ρ d<sub>R</sub> | q̄<sub>L</sub>d<sub>R</sub>ρ | 4 | yd331[1] | 0 | n/a | 0 | SSB | shared `ii` | shared `cc` | 1/3−1/3+0=0 | 0 | n/a | HC[lag] |
| LYuk331 q̄3L η* b<sub>R</sub> | q̄<sub>L</sub>b<sub>R</sub>ηbar | 4 | yd331[3] | 0 | n/a | 0 | SSB | shared `ii` | shared `cc` | −2/3−1/3+1=0 | 0 | n/a | HC[lag] |
| LYuk331 q̄1L χ D<sub>R</sub> | q̄<sub>L</sub>D<sub>R</sub>χ | 4 | yJD | 0 | n/a | 0 | SSB | shared `ii` | shared `cc` | 1/3−4/3+1=0 | 0 | n/a | HC[lag] |
| LYuk331 q̄3L χ* T<sub>R</sub> | q̄<sub>L</sub>T<sub>R</sub>χbar | 4 | yJT | 0 | n/a | 0 | SSB | shared `ii` | shared `cc` | −2/3+5/3−1=0 | 0 | n/a | HC[lag] |
| LYuk331 l̄L η* ℓ<sub>R</sub> | l̄<sub>L</sub>ℓ<sub>R</sub>ηbar | 4 | yl331[ff] | 0 | n/a | 0 | SSB | shared `ii` | singlet | 0−1+1=0 | L=0 | n/a | HC[lag] |
| LYuk331 l̄L χ* E<sub>R</sub> | l̄<sub>L</sub>E<sub>R</sub>χbar | 4 | yE331[ff] | 0 | n/a | 0 | SSB | shared `ii` | singlet | 0+1−1=0 | L=0 | n/a | HC[lag] |

**Free-field check, one row per new class** — Zp: `LZpkin` (kin+mass, MZp). Yp, Vp: `LYVkin` (kin+mass, MYp, MVp). H2, H3, H0: `LNPS` (kin+mass, MH2, MH3, MH0). Hp, HY, HV: `LNPS` (kin+mass, MHp, MHY, MHV). DQ, SQ, TQ, EL: `LNPF` (kin+mass, MDQ, MSQ, MTQ, MEL[ff]). All are inside the total sum `L331`.

**SelfConjugate → True classes**: `Zp`, `H2`, `H3`, `H0`. None of them carries `QuantumNumbers`.

**Reference/cached model files read: none.** Only the paper text and `SM.fr` (the SM base file, as instructed) were opened.

Two omissions, stated plainly: the Higgs potential of Eq. (2.9) and the scalar-triplet covariant kinetic terms (Tables 7–9 VSS/VVS couplings) are not written, because without the SU(3)<sub>L</sub> gauge group they cannot use `DC`, and adding the potential would double count the SM Higgs mass and self-coupling that `SM.fr` already supplies. All fermion, gauge and Yukawa new-physics content is complete.

```json
{
  "model_name": "331_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:1611.09337 (Q.-H. Cao, D.-M. Zhang)"],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["Peking University"],
    "emails": ["qinghongcao@pku.edu.cn", "zhangdongming@pku.edu.cn"]
  },
  "gauge_groups": [],
  "index_decls": [
    {"name": "SU3L", "range_kind": "Unfold", "size": 3, "style_symbol": "aa"}
  ],
  "parameters": [
    {"name": "v1", "parameter_type": "External", "value": "200.", "block_name": "VEV331", "order_block": 1, "interaction_order": ["QED", -1], "description": "vev of the rho triplet [GeV], Eq.(2.3); v1^2+v2^2 = vev^2"},
    {"name": "v3", "parameter_type": "External", "value": "2000.", "block_name": "VEV331", "order_block": 2, "interaction_order": ["QED", -1], "description": "vev of the chi triplet [GeV], the SU(3)L x U(1)X breaking scale, Eq.(2.3)"},
    {"name": "v2", "parameter_type": "Internal", "value": "Sqrt[vev^2 - v1^2]", "interaction_order": ["QED", -1], "description": "vev of the eta triplet [GeV], Eq.(2.13)"},
    {"name": "bet", "parameter_type": "Internal", "value": "Sqrt[3]", "description": "beta parameter of the 331 model, Eq.(2.4); fixed to Sqrt[3] (Table 1, last column)"},
    {"name": "a0", "parameter_type": "Internal", "value": "Sqrt[1 - (1 + bet^2) sw^2]", "description": "a0 = Sqrt[1-(1+beta^2)sW^2], appears in MZp and in all Z' couplings, Eq.(2.66), Table 11"},
    {"name": "gX", "parameter_type": "Internal", "value": "ee/a0", "interaction_order": ["QED", 1], "description": "U(1)X gauge coupling, from gY = g gX/Sqrt[g^2+beta^2 gX^2], Eq.(2.49)"},
    {"name": "s331", "parameter_type": "Internal", "value": "a0/cw", "description": "sin of the W8-X mixing angle, Eq.(2.45)"},
    {"name": "c331", "parameter_type": "Internal", "value": "bet sw/cw", "description": "cos of the W8-X mixing angle, Eq.(2.45)"},
    {"name": "c12", "parameter_type": "Internal", "value": "v1/vev", "description": "c12 = v1/v, scalar mixing, Eq.(2.16)"},
    {"name": "s12", "parameter_type": "Internal", "value": "v2/vev", "description": "s12 = v2/v, scalar mixing, Eq.(2.16)"},
    {"name": "c13", "parameter_type": "Internal", "value": "v1/Sqrt[v1^2 + v3^2]", "description": "c13, charge QV scalar mixing, Eq.(2.31)"},
    {"name": "s13", "parameter_type": "Internal", "value": "v3/Sqrt[v1^2 + v3^2]", "description": "s13, charge QV scalar mixing, Eq.(2.31)"},
    {"name": "c23", "parameter_type": "Internal", "value": "v2/Sqrt[v2^2 + v3^2]", "description": "c23, charge QY scalar mixing, Eq.(2.27)"},
    {"name": "s23", "parameter_type": "Internal", "value": "v3/Sqrt[v2^2 + v3^2]", "description": "s23, charge QY scalar mixing, Eq.(2.27)"},
    {"name": "MZp", "parameter_type": "Internal", "value": "cw gw v3/(Sqrt[3] a0)", "description": "Z' mass [GeV], Eq.(2.73)"},
    {"name": "MYp", "parameter_type": "Internal", "value": "gw Sqrt[v3^2 + v2^2]/2", "description": "Y boson mass [GeV], Eq.(2.74)"},
    {"name": "MVp", "parameter_type": "Internal", "value": "gw Sqrt[v3^2 + v1^2]/2", "description": "V boson mass [GeV], Eq.(2.74)"},
    {"name": "XQ12", "parameter_type": "Internal", "value": "1/6 - bet/(2 Sqrt[3])", "description": "U(1)X charge of the quark triplets q1L, q2L, from Q = T3 + beta T8 + X, Eq.(2.5)"},
    {"name": "XQ3", "parameter_type": "Internal", "value": "1/6 + bet/(2 Sqrt[3])", "description": "U(1)X charge of the quark anti-triplet q3L, Eq.(2.5)"},
    {"name": "XLL", "parameter_type": "Internal", "value": "-1/2 + bet/(2 Sqrt[3])", "description": "U(1)X charge of the lepton anti-triplets, Eq.(2.5)"},
    {"name": "Xrho", "parameter_type": "Internal", "value": "1/2 - bet/(2 Sqrt[3])", "description": "U(1)X charge of the rho scalar triplet, re-derived from Eq.(2.5)"},
    {"name": "Xeta", "parameter_type": "Internal", "value": "-1/2 - bet/(2 Sqrt[3])", "description": "U(1)X charge of the eta scalar triplet, re-derived from Eq.(2.5)"},
    {"name": "Xchi", "parameter_type": "Internal", "value": "bet/Sqrt[3]", "description": "U(1)X charge of the chi scalar triplet, re-derived from Eq.(2.5)"},
    {"name": "QDS", "parameter_type": "Internal", "value": "1/6 - Sqrt[3] bet/2", "description": "electric charge of the heavy quarks D and S, Eq.(2.57)"},
    {"name": "QTq", "parameter_type": "Internal", "value": "1/6 + Sqrt[3] bet/2", "description": "electric charge of the heavy quark T, Eq.(2.57)"},
    {"name": "QEl", "parameter_type": "Internal", "value": "-1/2 + Sqrt[3] bet/2", "description": "electric charge of the heavy leptons E, Eq.(2.59)"},
    {"name": "UU", "parameter_type": "Internal", "indices": ["SU3L", "SU3L"], "value_rules": [
      {"lhs": "UU[1,1]", "rhs": "c12"}, {"lhs": "UU[1,2]", "rhs": "-s12"}, {"lhs": "UU[1,3]", "rhs": "0"},
      {"lhs": "UU[2,1]", "rhs": "s12"}, {"lhs": "UU[2,2]", "rhs": "c12"}, {"lhs": "UU[2,3]", "rhs": "0"},
      {"lhs": "UU[3,1]", "rhs": "0"}, {"lhs": "UU[3,2]", "rhs": "0"}, {"lhs": "UU[3,3]", "rhs": "1"}],
      "description": "CP-even scalar rotation matrix U, Eq.(2.14), in the decoupling limit v3 >> v1,v2, Eq.(2.15)"},
    {"name": "OO", "parameter_type": "Internal", "indices": ["SU3L", "SU3L"], "value_rules": [
      {"lhs": "OO[1,1]", "rhs": "s12"}, {"lhs": "OO[1,2]", "rhs": "-c12"}, {"lhs": "OO[1,3]", "rhs": "0"},
      {"lhs": "OO[2,1]", "rhs": "c12"}, {"lhs": "OO[2,2]", "rhs": "s12"}, {"lhs": "OO[2,3]", "rhs": "0"},
      {"lhs": "OO[3,1]", "rhs": "0"}, {"lhs": "OO[3,2]", "rhs": "0"}, {"lhs": "OO[3,3]", "rhs": "1"}],
      "description": "CP-odd scalar rotation matrix O, Eq.(2.19), in the decoupling limit, Eq.(2.20)"},
    {"name": "gZqL", "parameter_type": "Internal", "value": "-gw s331/(2 Sqrt[3]) + gX c331 XQ12", "interaction_order": ["QED", 1], "description": "Z' coupling to left-handed u,d,c,s (Table 11)"},
    {"name": "gZqJ", "parameter_type": "Internal", "value": "gw s331/Sqrt[3] + gX c331 XQ12", "interaction_order": ["QED", 1], "description": "Z' coupling to left-handed D and S quarks (Table 11)"},
    {"name": "gZq3L", "parameter_type": "Internal", "value": "gw s331/(2 Sqrt[3]) + gX c331 XQ3", "interaction_order": ["QED", 1], "description": "Z' coupling to left-handed t and b (anti-triplet, Table 11)"},
    {"name": "gZq3T", "parameter_type": "Internal", "value": "-gw s331/Sqrt[3] + gX c331 XQ3", "interaction_order": ["QED", 1], "description": "Z' coupling to the left-handed T quark (Table 11)"},
    {"name": "gZlL", "parameter_type": "Internal", "value": "gw s331/(2 Sqrt[3]) + gX c331 XLL", "interaction_order": ["QED", 1], "description": "Z' coupling to left-handed charged leptons and neutrinos (Table 11)"},
    {"name": "gZlE", "parameter_type": "Internal", "value": "-gw s331/Sqrt[3] + gX c331 XLL", "interaction_order": ["QED", 1], "description": "Z' coupling to the left-handed heavy leptons E (Table 11)"},
    {"name": "gZRu", "parameter_type": "Internal", "value": "2/3 gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed up-type quarks (Table 11)"},
    {"name": "gZRd", "parameter_type": "Internal", "value": "-1/3 gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed down-type quarks (Table 11)"},
    {"name": "gZRl", "parameter_type": "Internal", "value": "-gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed charged leptons (Table 11)"},
    {"name": "gZRD", "parameter_type": "Internal", "value": "QDS gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed D and S quarks (Table 11)"},
    {"name": "gZRT", "parameter_type": "Internal", "value": "QTq gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to the right-handed T quark (Table 11)"},
    {"name": "gZRE", "parameter_type": "Internal", "value": "QEl gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed heavy leptons (Table 11)"},
    {"name": "gZpV", "parameter_type": "Internal", "value": "-Sqrt[3] gw s331/2", "interaction_order": ["QED", 1], "description": "Z' charge of the (Y,V) gauge doublet, = -Sqrt[3] g s331/2 (Table 10: Z'Y+Y- and Z'V+V-)"},
    {"name": "gZHY", "parameter_type": "Internal", "value": "c23^2 (-gw s331/(2 Sqrt[3]) + gX c331 Xchi) + s23^2 (-gw s331/Sqrt[3] - gX c331 Xeta)", "interaction_order": ["QED", 1], "description": "Z' charge of the charged scalar H^QY, from the chi/eta mixing of Eq.(2.26)"},
    {"name": "gZHV", "parameter_type": "Internal", "value": "c13^2 (-gw s331/(2 Sqrt[3]) + gX c331 Xchi) + s13^2 (-gw s331/Sqrt[3] - gX c331 Xrho)", "interaction_order": ["QED", 1], "description": "Z' charge of the charged scalar H^QV, from the chi/rho mixing of Eq.(2.30)"},
    {"name": "gZHp", "parameter_type": "Internal", "value": "c12^2 (gw s331/(2 Sqrt[3]) - gX c331 Xeta) + s12^2 (-gw s331/(2 Sqrt[3]) + gX c331 Xrho)", "interaction_order": ["QED", 1], "description": "Z' charge of the charged scalar H+, from the eta/rho mixing of Eq.(2.23)"},
    {"name": "yJD", "parameter_type": "Internal", "value": "Sqrt[2] MDQ/v3", "interaction_order": ["QED", 1], "description": "Yukawa coupling yJ_11 of the D quark to the chi triplet, Eq.(2.61); MD = yJD v3/Sqrt[2]"},
    {"name": "yJS", "parameter_type": "Internal", "value": "Sqrt[2] MSQ/v3", "interaction_order": ["QED", 1], "description": "Yukawa coupling yJ_22 of the S quark to the chi triplet, Eq.(2.61)"},
    {"name": "yJT", "parameter_type": "Internal", "value": "Sqrt[2] MTQ/v3", "interaction_order": ["QED", 1], "description": "Yukawa coupling yJ_33 of the T quark to the conjugate chi triplet, Eq.(2.61)"},
    {"name": "yE331", "parameter_type": "Internal", "indices": ["Generation"], "value_rules": [
      {"lhs": "yE331[1]", "rhs": "Sqrt[2] MEe/v3"},
      {"lhs": "yE331[2]", "rhs": "Sqrt[2] MEm/v3"},
      {"lhs": "yE331[3]", "rhs": "Sqrt[2] MEt/v3"}],
      "interaction_order": ["QED", 1], "description": "Yukawa couplings yE of the heavy leptons to the conjugate chi triplet, Eq.(2.62)"},
    {"name": "yu331", "parameter_type": "Internal", "indices": ["Generation"], "value_rules": [
      {"lhs": "yu331[1]", "rhs": "Sqrt[2] ymup/v2"},
      {"lhs": "yu331[2]", "rhs": "Sqrt[2] ymc/v2"},
      {"lhs": "yu331[3]", "rhs": "-Sqrt[2] ymt/v1"}],
      "interaction_order": ["QED", 1], "description": "331 up-type Yukawa couplings, Eq.(2.61): u,c from eta (vev v2), t from conjugate rho (vev v1); the minus sign follows the -t entry of the q3L anti-triplet, Eq.(2.56)"},
    {"name": "yd331", "parameter_type": "Internal", "indices": ["Generation"], "value_rules": [
      {"lhs": "yd331[1]", "rhs": "Sqrt[2] ymdo/v1"},
      {"lhs": "yd331[2]", "rhs": "Sqrt[2] yms/v1"},
      {"lhs": "yd331[3]", "rhs": "Sqrt[2] ymb/v2"}],
      "interaction_order": ["QED", 1], "description": "331 down-type Yukawa couplings, Eq.(2.61): d,s from rho (vev v1), b from conjugate eta (vev v2)"},
    {"name": "yl331", "parameter_type": "Internal", "indices": ["Generation"], "value_rules": [
      {"lhs": "yl331[1]", "rhs": "Sqrt[2] yme/v2"},
      {"lhs": "yl331[2]", "rhs": "Sqrt[2] ymm/v2"},
      {"lhs": "yl331[3]", "rhs": "Sqrt[2] ymtau/v2"}],
      "interaction_order": ["QED", 1], "description": "331 charged-lepton Yukawa couplings from the conjugate eta triplet, Eq.(2.62)"}
  ],
  "particles": [
    {"spin_type": "V", "class_index": 20, "class_name": "Zp", "self_conjugate": true,
     "mass": {"sym": "MZp", "value": "Internal"}, "width": {"sym": "WZp", "value": "Automatic"},
     "pdg": 32, "particle_name": "Zp", "full_name": "Zprime boson of SU(3)L x U(1)X", "propagator_label": "Zp", "propagator_type": "Sine", "propagator_arrow": "None"},
    {"spin_type": "V", "class_index": 21, "class_name": "Yp", "self_conjugate": false,
     "mass": {"sym": "MYp", "value": "Internal"}, "width": {"sym": "WYp", "value": "Automatic"},
     "quantum_numbers": {"Q": "2"}, "pdg": 9000034, "particle_name": "Y++", "antiparticle_name": "Y--",
     "full_name": "Y gauge boson, charge QY = (Sqrt[3] beta+1)/2 = 2", "propagator_label": "Y", "propagator_type": "Sine", "propagator_arrow": "Forward"},
    {"spin_type": "V", "class_index": 22, "class_name": "Vp", "self_conjugate": false,
     "mass": {"sym": "MVp", "value": "Internal"}, "width": {"sym": "WVp", "value": "Automatic"},
     "quantum_numbers": {"Q": "1"}, "pdg": 9000035, "particle_name": "V+", "antiparticle_name": "V-",
     "full_name": "V gauge boson, charge QV = (Sqrt[3] beta-1)/2 = 1", "propagator_label": "V", "propagator_type": "Sine", "propagator_arrow": "Forward"},
    {"spin_type": "V", "class_index": 23, "class_name": "WY", "self_conjugate": false, "unphysical": true,
     "indices": ["SU2D"], "flavor_index": "SU2D", "quantum_numbers": {"Y": "3/2"},
     "definitions": ["WY[mu_,1] -> Yp[mu]", "WY[mu_,2] -> Vp[mu]"]},
    {"spin_type": "S", "class_index": 20, "class_name": "H2", "self_conjugate": true,
     "mass": {"sym": "MH2", "value": "2900."}, "width": {"sym": "WH2", "value": "Automatic"},
     "pdg": 35, "particle_name": "H2", "full_name": "second CP-even neutral scalar, Eq.(2.67)", "propagator_label": "H2", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 21, "class_name": "H3", "self_conjugate": true,
     "mass": {"sym": "MH3", "value": "2000."}, "width": {"sym": "WH3", "value": "Automatic"},
     "pdg": 45, "particle_name": "H3", "full_name": "third CP-even neutral scalar (chi-like), Eq.(2.68)", "propagator_label": "H3", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 22, "class_name": "H0", "self_conjugate": true,
     "mass": {"sym": "MH0", "value": "2900."}, "width": {"sym": "WH0", "value": "Automatic"},
     "pdg": 36, "particle_name": "H0", "full_name": "CP-odd neutral scalar, Eq.(2.68)", "propagator_label": "H0", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 23, "class_name": "Hp", "self_conjugate": false,
     "mass": {"sym": "MHp", "value": "2900."}, "width": {"sym": "WHp", "value": "Automatic"},
     "quantum_numbers": {"Q": "1", "Y": "1"}, "pdg": 37, "particle_name": "H+", "antiparticle_name": "H-",
     "full_name": "singly charged scalar, Eq.(2.69)", "propagator_label": "Hp", "propagator_type": "ScalarDash", "propagator_arrow": "Forward"},
    {"spin_type": "S", "class_index": 24, "class_name": "HY", "self_conjugate": false,
     "mass": {"sym": "MHY", "value": "1400."}, "width": {"sym": "WHY", "value": "Automatic"},
     "quantum_numbers": {"Q": "2", "Y": "2"}, "pdg": 9000037, "particle_name": "HY++", "antiparticle_name": "HY--",
     "full_name": "charged scalar of charge QY = 2, Eq.(2.70)", "propagator_label": "HY", "propagator_type": "ScalarDash", "propagator_arrow": "Forward"},
    {"spin_type": "S", "class_index": 25, "class_name": "HV", "self_conjugate": false,
     "mass": {"sym": "MHV", "value": "1300."}, "width": {"sym": "WHV", "value": "Automatic"},
     "quantum_numbers": {"Q": "1", "Y": "1"}, "pdg": 9000038, "particle_name": "HV+", "antiparticle_name": "HV-",
     "full_name": "charged scalar of charge QV = 1, Eq.(2.71)", "propagator_label": "HV", "propagator_type": "ScalarDash", "propagator_arrow": "Forward"},
    {"spin_type": "S", "class_index": 30, "class_name": "rhoT", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L"], "flavor_index": "SU3L",
     "definitions": ["rhoT[1] -> -s12 Hp", "rhoT[2] -> (UU[1,2] H2 + UU[1,3] H3 + I OO[1,1] H0)/Sqrt[2]", "rhoT[3] -> -s13 HVbar"]},
    {"spin_type": "S", "class_index": 31, "class_name": "etaT", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L"], "flavor_index": "SU3L",
     "definitions": ["etaT[1] -> (UU[2,2] H2 + UU[2,3] H3 + I OO[2,1] H0)/Sqrt[2]", "etaT[2] -> c12 Hpbar", "etaT[3] -> -s23 HYbar"]},
    {"spin_type": "S", "class_index": 32, "class_name": "chiT", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L"], "flavor_index": "SU3L",
     "definitions": ["chiT[1] -> c23 HY", "chiT[2] -> c13 HV", "chiT[3] -> (UU[3,2] H2 + UU[3,3] H3 + I OO[3,1] H0)/Sqrt[2]"]},
    {"spin_type": "F", "class_index": 20, "class_name": "DQ", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "MDQ", "value": "1000."}, "width": {"sym": "WDQ", "value": "Automatic"},
     "quantum_numbers": {"Q": "-4/3", "Y": "-4/3"}, "pdg": 9000001, "particle_name": "D", "antiparticle_name": "D~",
     "full_name": "heavy quark D, third member of the q1L triplet, Eq.(2.56)", "propagator_label": "D", "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 21, "class_name": "SQ", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "MSQ", "value": "1000."}, "width": {"sym": "WSQ", "value": "Automatic"},
     "quantum_numbers": {"Q": "-4/3", "Y": "-4/3"}, "pdg": 9000002, "particle_name": "S", "antiparticle_name": "S~",
     "full_name": "heavy quark S, third member of the q2L triplet, Eq.(2.56)", "propagator_label": "S", "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 22, "class_name": "TQ", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "MTQ", "value": "1000."}, "width": {"sym": "WTQ", "value": "Automatic"},
     "quantum_numbers": {"Q": "5/3", "Y": "5/3"}, "pdg": 9000003, "particle_name": "T", "antiparticle_name": "T~",
     "full_name": "heavy quark T, third member of the q3L anti-triplet, Eq.(2.56)", "propagator_label": "T", "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 23, "class_name": "EL", "self_conjugate": false,
     "class_members": ["Ee", "Em", "Et"], "indices": ["Generation"], "flavor_index": "Generation",
     "mass": {"sym": "MEL", "members": [["MEe", "1000."], ["MEm", "1000."], ["MEt", "1000."]]},
     "width": {"sym": "WEL", "members": [["WEe", "Automatic"], ["WEm", "Automatic"], ["WEt", "Automatic"]]},
     "quantum_numbers": {"Q": "1", "Y": "1", "LeptonNumber": "1"},
     "pdg": [9000011, 9000013, 9000015],
     "particle_name": ["Ee+", "Em+", "Et+"], "antiparticle_name": ["Ee-", "Em-", "Et-"],
     "full_name": ["heavy lepton Ee", "heavy lepton Emu", "heavy lepton Etau"],
     "propagator_label": ["EL", "Ee", "Em", "Et"], "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 30, "class_name": "q1L", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L", "Colour"], "flavor_index": "SU3L",
     "definitions": ["q1L[sp1_,1,cc_] :> Module[{sp2}, ProjM[sp1,sp2] uq[sp2,1,cc]]", "q1L[sp1_,2,cc_] :> Module[{sp2}, ProjM[sp1,sp2] dq[sp2,1,cc]]", "q1L[sp1_,3,cc_] :> Module[{sp2}, ProjM[sp1,sp2] DQ[sp2,cc]]"]},
    {"spin_type": "F", "class_index": 31, "class_name": "q2L", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L", "Colour"], "flavor_index": "SU3L",
     "definitions": ["q2L[sp1_,1,cc_] :> Module[{sp2}, ProjM[sp1,sp2] uq[sp2,2,cc]]", "q2L[sp1_,2,cc_] :> Module[{sp2}, ProjM[sp1,sp2] dq[sp2,2,cc]]", "q2L[sp1_,3,cc_] :> Module[{sp2}, ProjM[sp1,sp2] SQ[sp2,cc]]"]},
    {"spin_type": "F", "class_index": 32, "class_name": "q3L", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L", "Colour"], "flavor_index": "SU3L",
     "definitions": ["q3L[sp1_,1,cc_] :> Module[{sp2}, ProjM[sp1,sp2] dq[sp2,3,cc]]", "q3L[sp1_,2,cc_] :> Module[{sp2}, -ProjM[sp1,sp2] uq[sp2,3,cc]]", "q3L[sp1_,3,cc_] :> Module[{sp2}, ProjM[sp1,sp2] TQ[sp2,cc]]"]},
    {"spin_type": "F", "class_index": 33, "class_name": "lL", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L", "Generation"], "flavor_index": "SU3L",
     "definitions": ["lL[sp1_,1,ff_] :> Module[{sp2}, ProjM[sp1,sp2] l[sp2,ff]]", "lL[sp1_,2,ff_] :> Module[{sp2}, -ProjM[sp1,sp2] vl[sp2,ff]]", "lL[sp1_,3,ff_] :> Module[{sp2}, ProjM[sp1,sp2] EL[sp2,ff]]"]}
  ],
  "lagrangian_terms": [
    {"name": "LZpkin", "delayed": true,
     "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]]"},
    {"name": "LYVkin", "delayed": true,
     "expression": "Block[{mu,nu,ii}, ExpandIndices[-1/2 (DC[WYbar[nu,ii],mu] - DC[WYbar[mu,ii],nu] + I gZpV (Zp[mu] WYbar[nu,ii] - Zp[nu] WYbar[mu,ii])) (DC[WY[nu,ii],mu] - DC[WY[mu,ii],nu] - I gZpV (Zp[mu] WY[nu,ii] - Zp[nu] WY[mu,ii])) + MYp^2 Ypbar[mu] Yp[mu] + MVp^2 Vpbar[mu] Vp[mu], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LNPS", "delayed": true,
     "expression": "Block[{mu}, ExpandIndices[1/2 del[H2,mu] del[H2,mu] - 1/2 MH2^2 H2^2 + 1/2 del[H3,mu] del[H3,mu] - 1/2 MH3^2 H3^2 + 1/2 del[H0,mu] del[H0,mu] - 1/2 MH0^2 H0^2 + (DC[Hpbar,mu] + I gZHp Zp[mu] Hpbar) (DC[Hp,mu] - I gZHp Zp[mu] Hp) - MHp^2 Hpbar Hp + (DC[HYbar,mu] + I gZHY Zp[mu] HYbar) (DC[HY,mu] - I gZHY Zp[mu] HY) - MHY^2 HYbar HY + (DC[HVbar,mu] + I gZHV Zp[mu] HVbar) (DC[HV,mu] - I gZHV Zp[mu] HV) - MHV^2 HVbar HV]]"},
    {"name": "LNPF", "delayed": true,
     "expression": "Block[{mu,sp,ff,cc}, ExpandIndices[I DQbar.Ga[mu].DC[DQ,mu] + I SQbar.Ga[mu].DC[SQ,mu] + I TQbar.Ga[mu].DC[TQ,mu] + I ELbar.Ga[mu].DC[EL,mu] - MDQ DQbar[sp,cc].DQ[sp,cc] - MSQ SQbar[sp,cc].SQ[sp,cc] - MTQ TQbar[sp,cc].TQ[sp,cc] - MEL[ff] ELbar[sp,ff].EL[sp,ff]]]"},
    {"name": "LZpF", "delayed": true,
     "expression": "Block[{mu,ff,cc,sp1,sp2,sp3}, ExpandIndices[Zp[mu] (gZqL (q1Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q1L[sp2,1,cc] + q1Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q1L[sp2,2,cc] + q2Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q2L[sp2,1,cc] + q2Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q2L[sp2,2,cc]) + gZqJ (q1Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q1L[sp2,3,cc] + q2Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q2L[sp2,3,cc]) + gZq3L (q3Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q3L[sp2,1,cc] + q3Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q3L[sp2,2,cc]) + gZq3T q3Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q3L[sp2,3,cc] + gZlL (lLbar[sp1,1,ff] Ga[mu,sp1,sp2] lL[sp2,1,ff] + lLbar[sp1,2,ff] Ga[mu,sp1,sp2] lL[sp2,2,ff]) + gZlE lLbar[sp1,3,ff] Ga[mu,sp1,sp2] lL[sp2,3,ff] + gZRu uRbar[sp1,ff,cc] Ga[mu,sp1,sp2] uR[sp2,ff,cc] + gZRd dRbar[sp1,ff,cc] Ga[mu,sp1,sp2] dR[sp2,ff,cc] + gZRl lRbar[sp1,ff] Ga[mu,sp1,sp2] lR[sp2,ff] + gZRD (DQbar[sp1,cc] Ga[mu,sp1,sp2] ProjP[sp2,sp3] DQ[sp3,cc] + SQbar[sp1,cc] Ga[mu,sp1,sp2] ProjP[sp2,sp3] SQ[sp3,cc]) + gZRT TQbar[sp1,cc] Ga[mu,sp1,sp2] ProjP[sp2,sp3] TQ[sp3,cc] + gZRE ELbar[sp1,ff] Ga[mu,sp1,sp2] ProjP[sp2,sp3] EL[sp3,ff])]]"},
    {"name": "LYVF", "delayed": true,
     "expression": "Block[{mu,ff,cc,sp1,sp2,lag}, lag = ExpandIndices[gw/Sqrt[2] Yp[mu] (q1Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q1L[sp2,3,cc] + q2Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q2L[sp2,3,cc]) + gw/Sqrt[2] Vp[mu] (q1Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q1L[sp2,3,cc] + q2Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q2L[sp2,3,cc]) - gw/Sqrt[2] Yp[mu] (q3Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q3L[sp2,1,cc] + lLbar[sp1,3,ff] Ga[mu,sp1,sp2] lL[sp2,1,ff]) - gw/Sqrt[2] Vp[mu] (q3Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q3L[sp2,2,cc] + lLbar[sp1,3,ff] Ga[mu,sp1,sp2] lL[sp2,2,ff])]; lag + HC[lag]]"},
    {"name": "LYuk331", "delayed": true,
     "expression": "Block[{ii,ff,cc,sp,lag}, lag = ExpandIndices[-yu331[1] q1Lbar[sp,ii,cc] uq[sp,1,cc] etaT[ii] - yu331[2] q2Lbar[sp,ii,cc] uq[sp,2,cc] etaT[ii] - yu331[3] q3Lbar[sp,ii,cc] uq[sp,3,cc] rhoTbar[ii] - yd331[1] q1Lbar[sp,ii,cc] dq[sp,1,cc] rhoT[ii] - yd331[2] q2Lbar[sp,ii,cc] dq[sp,2,cc] rhoT[ii] - yd331[3] q3Lbar[sp,ii,cc] dq[sp,3,cc] etaTbar[ii] - yJD q1Lbar[sp,ii,cc] DQ[sp,cc] chiT[ii] - yJS q2Lbar[sp,ii,cc] SQ[sp,cc] chiT[ii] - yJT q3Lbar[sp,ii,cc] TQ[sp,cc] chiTbar[ii] - yl331[ff] lLbar[sp,ii,ff] l[sp,ff] etaTbar[ii] - yE331[ff] lLbar[sp,ii,ff] EL[sp,ff] chiTbar[ii], FlavorExpand -> SU3L]; lag + HC[lag]]"},
    {"name": "L331", "delayed": true,
     "expression": "LSM + LZpkin + LYVkin + LNPS + LNPF + LZpF + LYVF + LYuk331"}
  ]
}
```
I have the paper, the schema, and the SM.fr conventions. Below is the mandatory self-audit, then the model.

## Model choices (stated up front)

- **β fixed to +√3** (Table 1, last column). FeynRules `QuantumNumbers` must be numeric, so one benchmark must be chosen: Q(Y)=+2, Q(V)=+1, Q(D)=Q(S)=−4/3, Q(T)=+5/3, Q(E<sub>ℓ</sub>)=+1, Q(H<sup>QY</sup>)=+2, Q(H<sup>QV</sup>)=+1. `bet` stays symbolic (Internal = `Sqrt[3]`) in every coupling, so a different β needs only new charge labels.
- **New U(1)<sub>X</sub> charges re-derived** from the paper's own Q = T³ + βT⁸ + X (Eq. 2.5), not copied from Eq. (2.6). The printed Eq. (2.6) (X<sub>ρ</sub> = 1/2 − √3β/2) contradicts Eq. (2.5); the correct values are X<sub>ρ</sub> = 1/2 − β/(2√3) = 0, X<sub>η</sub> = −1/2 − β/(2√3) = −1, X<sub>χ</sub> = β/√3 = +1, X<sub>q1,q2</sub> = −1/3, X<sub>q3</sub> = +2/3, X<sub>l</sub> = 0, X<sub>fR</sub> = Q<sub>f</sub>. Sign choice: ρ is the Y=+1/2 doublet (SM.fr `Phi` role), η the Y=−1/2 one; all SM and new Yukawas are then invariant.
- **Validation**: my Z′ couplings reproduce Table 11 exactly (e.g. ūuZ′ g<sub>L</sub> = e[(β+√3)s<sub>W</sub>²−√3]/(6c<sub>W</sub>s<sub>W</sub>a₀), D̄DZ′ g<sub>R</sub>, D̄DZ), and my Yukawa expansion reproduces Table 12 (H₃ĒE = U₃₃M<sub>E</sub>/v₃, H₂ūu = U₂₂m<sub>u</sub>/v₂, H⁺ν̄ℓ = √2 m<sub>ℓ</sub>c₁₂/v₂, H<sup>+QY</sup>ūD).
- (Y, V) is an SU(2)<sub>L</sub> doublet with Y = √3β/2 = 3/2, so it is declared as the unphysical doublet `WY`; `DC` then gives the correct γ, Z and W±YV couplings. The heavy fermions and H<sup>QY</sup>, H<sup>QV</sup> are true SU(2) singlets with Y = Q. H± is treated as a singlet with Y = Q: exact QED coupling, approximate Z coupling.
- Scalar triplets are written in unitary gauge **without vevs** (fluctuations only), so the add-on adds to `LSM` with no double counting of the SM Yukawa; the vev pieces are resummed into the declared masses.

## Self-audit table

| term | fields in monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3)c | U(1)X sum | L/B | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpkin (kin) | FS[Zp]FS[Zp] | 4 | 1/4 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | real field |
| LZpkin (mass) | Zp Zp | 2 | MZp² | 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | real field |
| LYVkin (kin) | (D<sub>[μ</sub>WYbar<sub>ν]</sub>)(D<sup>[μ</sup>WY<sup>ν]</sup>) | 4 | 1/2 | 0 | n/a | 0 | −3/2+3/2=0 | doublet · anti-doublet, shared `ii` | singlet | 0 | 0 | n/a | self-conj pair |
| LYVkin (mass) | Ypbar Yp, Vpbar Vp | 2 | MYp², MVp² | 2 | n/a | 0 | 0 | shared | singlet | 0 | 0 | n/a | self-conj pair |
| LNPS (H2,H3,H0) | del·del, φ² | 4 / 2 | 1/2, MH²/2 | 0 / 2 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | real fields |
| LNPS (Hp,HY,HV) | (DHbar)(DH), Hbar H | 4 / 2 | 1, MH² | 0 / 2 | n/a | 0 | 0 | singlet (Y=Q) | singlet | 0 | 0 | n/a | bar·field |
| LNPF (kin) | ψ̄ γ Dψ, ψ = DQ,SQ,TQ,EL | 4 | 1 | 0 | n/a | 0 | 0 | singlet | 3⊗3̄ | 0 | 0 | n/a | self-conj |
| LNPF (mass) | ψ̄ψ | 3 | M<sub>ψ</sub> | 1 | n/a | 0 | 0 | singlet | 3⊗3̄ | 0 | 0 | n/a | self-conj |
| LZpF (q1L,q2L, ii=1,2) | q̄<sub>L</sub>γq<sub>L</sub>Zp | 4 | gZqL | 0 | n/a | 0 | 0 | same component | 3⊗3̄ | +1/3−1/3=0 | B=0 | n/a | self-conj |
| LZpF (q1L,q2L, ii=3) | D̄<sub>L</sub>γD<sub>L</sub>Zp | 4 | gZqJ | 0 | n/a | 0 | 0 | singlet | 3⊗3̄ | 0 | 0 | n/a | self-conj |
| LZpF (q3L, ii=1,2 / 3) | b̄,t̄,T̄ γ · Zp | 4 | gZq3L, gZq3T | 0 | n/a | 0 | 0 | same component | 3⊗3̄ | 0 | 0 | n/a | self-conj |
| LZpF (lL, ii=1,2 / 3) | ℓ̄,ν̄,Ē γ · Zp | 4 | gZlL, gZlE | 0 | n/a | 0 | 0 | same component | singlet | 0 | L=0 | n/a | self-conj |
| LZpF (RH: uR,dR,lR,DQ,SQ,TQ,EL) | f̄<sub>R</sub>γf<sub>R</sub>Zp | 4 | gZRu…gZRE | 0 | n/a | 0 | 0 | singlet | 3⊗3̄ / singlet | X<sub>fR</sub>−X<sub>fR</sub>=0 | 0 | n/a | self-conj |
| LYVF ūD Y⁺ | ū<sub>L</sub>γD<sub>L</sub>Yp | 4 | gw/√2 | 0 | n/a | −2/3−4/3+2=0 | −1/6−4/3+3/2=0 | doublet(u)·singlet(D)·Y(T³=+1/2) | 3̄⊗3, shared `cc` | +1/3−1/3+0=0 | B=0 | n/a | HC[lag] |
| LYVF d̄D V⁺ | d̄<sub>L</sub>γD<sub>L</sub>Vp | 4 | gw/√2 | 0 | n/a | 1/3−4/3+1=0 | −1/6−4/3+3/2=0 | doublet(d)·singlet·V(T³=−1/2) | shared `cc` | 0 | 0 | n/a | HC[lag] |
| LYVF T̄b Y⁺ | T̄<sub>L</sub>γb<sub>L</sub>Yp | 4 | −gw/√2 | 0 | n/a | −5/3−1/3+2=0 | −5/3+1/6+3/2=0 | singlet·doublet·Y | shared `cc` | −2/3+2/3=0 | 0 | n/a | HC[lag] |
| LYVF T̄t V⁺ | T̄<sub>L</sub>γt<sub>L</sub>Vp | 4 | −gw/√2 | 0 | n/a | −5/3+2/3+1=0 | 0 | singlet·doublet·V | shared `cc` | 0 | 0 | n/a | HC[lag] |
| LYVF Ēℓ Y⁺ | Ē<sub>L</sub>γℓ<sub>L</sub>Yp | 4 | −gw/√2 | 0 | n/a | −1−1+2=0 | −1−1/2+3/2=0 | singlet·doublet·Y | singlet | 0 | L: −1+1=0 | n/a | HC[lag] |
| LYVF Ēν V⁺ | Ē<sub>L</sub>γν<sub>L</sub>Vp | 4 | −gw/√2 | 0 | n/a | −1+0+1=0 | −1−1/2+3/2=0 | singlet·doublet·V | singlet | 0 | L=0 | n/a | HC[lag] |
| LYuk331 q̄1L η u<sub>R</sub> (all 3 comps) | q̄<sub>L</sub>u<sub>R</sub>η | 4 | yu331[1] | 0 | n/a | 0 per component | SSB basis (Q only) | shared `ii` (3̄⊗3) | shared `cc` | +1/3+2/3−1=0 | B=0 | n/a | HC[lag] |
| LYuk331 q̄3L ρ* t<sub>R</sub> | q̄<sub>L</sub>t<sub>R</sub>ρbar | 4 | yu331[3] | 0 | n/a | 0 | SSB | shared `ii` (3⊗3̄) | shared `cc` | −2/3+2/3−0=0 | 0 | n/a | HC[lag] |
| LYuk331 q̄1L ρ d<sub>R</sub> | q̄<sub>L</sub>d<sub>R</sub>ρ | 4 | yd331[1] | 0 | n/a | 0 | SSB | shared `ii` | shared `cc` | 1/3−1/3+0=0 | 0 | n/a | HC[lag] |
| LYuk331 q̄3L η* b<sub>R</sub> | q̄<sub>L</sub>b<sub>R</sub>ηbar | 4 | yd331[3] | 0 | n/a | 0 | SSB | shared `ii` | shared `cc` | −2/3−1/3+1=0 | 0 | n/a | HC[lag] |
| LYuk331 q̄1L χ D<sub>R</sub> | q̄<sub>L</sub>D<sub>R</sub>χ | 4 | yJD | 0 | n/a | 0 | SSB | shared `ii` | shared `cc` | 1/3−4/3+1=0 | 0 | n/a | HC[lag] |
| LYuk331 q̄3L χ* T<sub>R</sub> | q̄<sub>L</sub>T<sub>R</sub>χbar | 4 | yJT | 0 | n/a | 0 | SSB | shared `ii` | shared `cc` | −2/3+5/3−1=0 | 0 | n/a | HC[lag] |
| LYuk331 l̄L η* ℓ<sub>R</sub> | l̄<sub>L</sub>ℓ<sub>R</sub>ηbar | 4 | yl331[ff] | 0 | n/a | 0 | SSB | shared `ii` | singlet | 0−1+1=0 | L=0 | n/a | HC[lag] |
| LYuk331 l̄L χ* E<sub>R</sub> | l̄<sub>L</sub>E<sub>R</sub>χbar | 4 | yE331[ff] | 0 | n/a | 0 | SSB | shared `ii` | singlet | 0+1−1=0 | L=0 | n/a | HC[lag] |

**Free-field check, one row per new class** — Zp: `LZpkin` (kin+mass, MZp). Yp, Vp: `LYVkin` (kin+mass, MYp, MVp). H2, H3, H0: `LNPS` (kin+mass, MH2, MH3, MH0). Hp, HY, HV: `LNPS` (kin+mass, MHp, MHY, MHV). DQ, SQ, TQ, EL: `LNPF` (kin+mass, MDQ, MSQ, MTQ, MEL[ff]). All are inside the total sum `L331`.

**SelfConjugate → True classes**: `Zp`, `H2`, `H3`, `H0`. None of them carries `QuantumNumbers`.

**Reference/cached model files read: none.** Only the paper text and `SM.fr` (the SM base file, as instructed) were opened.

Two omissions, stated plainly: the Higgs potential of Eq. (2.9) and the scalar-triplet covariant kinetic terms (Tables 7–9 VSS/VVS couplings) are not written, because without the SU(3)<sub>L</sub> gauge group they cannot use `DC`, and adding the potential would double count the SM Higgs mass and self-coupling that `SM.fr` already supplies. All fermion, gauge and Yukawa new-physics content is complete.

```json
{
  "model_name": "331_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:1611.09337 (Q.-H. Cao, D.-M. Zhang)"],
    "version": "1.0",
    "date": "2026-09-02",
    "institutions": ["Peking University"],
    "emails": ["qinghongcao@pku.edu.cn", "zhangdongming@pku.edu.cn"]
  },
  "gauge_groups": [],
  "index_decls": [
    {"name": "SU3L", "range_kind": "Unfold", "size": 3, "style_symbol": "aa"}
  ],
  "parameters": [
    {"name": "v1", "parameter_type": "External", "value": "200.", "block_name": "VEV331", "order_block": 1, "interaction_order": ["QED", -1], "description": "vev of the rho triplet [GeV], Eq.(2.3); v1^2+v2^2 = vev^2"},
    {"name": "v3", "parameter_type": "External", "value": "2000.", "block_name": "VEV331", "order_block": 2, "interaction_order": ["QED", -1], "description": "vev of the chi triplet [GeV], the SU(3)L x U(1)X breaking scale, Eq.(2.3)"},
    {"name": "v2", "parameter_type": "Internal", "value": "Sqrt[vev^2 - v1^2]", "interaction_order": ["QED", -1], "description": "vev of the eta triplet [GeV], Eq.(2.13)"},
    {"name": "bet", "parameter_type": "Internal", "value": "Sqrt[3]", "description": "beta parameter of the 331 model, Eq.(2.4); fixed to Sqrt[3] (Table 1, last column)"},
    {"name": "a0", "parameter_type": "Internal", "value": "Sqrt[1 - (1 + bet^2) sw^2]", "description": "a0 = Sqrt[1-(1+beta^2)sW^2], appears in MZp and in all Z' couplings, Eq.(2.66), Table 11"},
    {"name": "gX", "parameter_type": "Internal", "value": "ee/a0", "interaction_order": ["QED", 1], "description": "U(1)X gauge coupling, from gY = g gX/Sqrt[g^2+beta^2 gX^2], Eq.(2.49)"},
    {"name": "s331", "parameter_type": "Internal", "value": "a0/cw", "description": "sin of the W8-X mixing angle, Eq.(2.45)"},
    {"name": "c331", "parameter_type": "Internal", "value": "bet sw/cw", "description": "cos of the W8-X mixing angle, Eq.(2.45)"},
    {"name": "c12", "parameter_type": "Internal", "value": "v1/vev", "description": "c12 = v1/v, scalar mixing, Eq.(2.16)"},
    {"name": "s12", "parameter_type": "Internal", "value": "v2/vev", "description": "s12 = v2/v, scalar mixing, Eq.(2.16)"},
    {"name": "c13", "parameter_type": "Internal", "value": "v1/Sqrt[v1^2 + v3^2]", "description": "c13, charge QV scalar mixing, Eq.(2.31)"},
    {"name": "s13", "parameter_type": "Internal", "value": "v3/Sqrt[v1^2 + v3^2]", "description": "s13, charge QV scalar mixing, Eq.(2.31)"},
    {"name": "c23", "parameter_type": "Internal", "value": "v2/Sqrt[v2^2 + v3^2]", "description": "c23, charge QY scalar mixing, Eq.(2.27)"},
    {"name": "s23", "parameter_type": "Internal", "value": "v3/Sqrt[v2^2 + v3^2]", "description": "s23, charge QY scalar mixing, Eq.(2.27)"},
    {"name": "MZp", "parameter_type": "Internal", "value": "cw gw v3/(Sqrt[3] a0)", "description": "Z' mass [GeV], Eq.(2.73)"},
    {"name": "MYp", "parameter_type": "Internal", "value": "gw Sqrt[v3^2 + v2^2]/2", "description": "Y boson mass [GeV], Eq.(2.74)"},
    {"name": "MVp", "parameter_type": "Internal", "value": "gw Sqrt[v3^2 + v1^2]/2", "description": "V boson mass [GeV], Eq.(2.74)"},
    {"name": "XQ12", "parameter_type": "Internal", "value": "1/6 - bet/(2 Sqrt[3])", "description": "U(1)X charge of the quark triplets q1L, q2L, from Q = T3 + beta T8 + X, Eq.(2.5)"},
    {"name": "XQ3", "parameter_type": "Internal", "value": "1/6 + bet/(2 Sqrt[3])", "description": "U(1)X charge of the quark anti-triplet q3L, Eq.(2.5)"},
    {"name": "XLL", "parameter_type": "Internal", "value": "-1/2 + bet/(2 Sqrt[3])", "description": "U(1)X charge of the lepton anti-triplets, Eq.(2.5)"},
    {"name": "Xrho", "parameter_type": "Internal", "value": "1/2 - bet/(2 Sqrt[3])", "description": "U(1)X charge of the rho scalar triplet, re-derived from Eq.(2.5)"},
    {"name": "Xeta", "parameter_type": "Internal", "value": "-1/2 - bet/(2 Sqrt[3])", "description": "U(1)X charge of the eta scalar triplet, re-derived from Eq.(2.5)"},
    {"name": "Xchi", "parameter_type": "Internal", "value": "bet/Sqrt[3]", "description": "U(1)X charge of the chi scalar triplet, re-derived from Eq.(2.5)"},
    {"name": "QDS", "parameter_type": "Internal", "value": "1/6 - Sqrt[3] bet/2", "description": "electric charge of the heavy quarks D and S, Eq.(2.57)"},
    {"name": "QTq", "parameter_type": "Internal", "value": "1/6 + Sqrt[3] bet/2", "description": "electric charge of the heavy quark T, Eq.(2.57)"},
    {"name": "QEl", "parameter_type": "Internal", "value": "-1/2 + Sqrt[3] bet/2", "description": "electric charge of the heavy leptons E, Eq.(2.59)"},
    {"name": "UU", "parameter_type": "Internal", "indices": ["SU3L", "SU3L"], "value_rules": [
      {"lhs": "UU[1,1]", "rhs": "c12"}, {"lhs": "UU[1,2]", "rhs": "-s12"}, {"lhs": "UU[1,3]", "rhs": "0"},
      {"lhs": "UU[2,1]", "rhs": "s12"}, {"lhs": "UU[2,2]", "rhs": "c12"}, {"lhs": "UU[2,3]", "rhs": "0"},
      {"lhs": "UU[3,1]", "rhs": "0"}, {"lhs": "UU[3,2]", "rhs": "0"}, {"lhs": "UU[3,3]", "rhs": "1"}],
      "description": "CP-even scalar rotation matrix U, Eq.(2.14), in the decoupling limit v3 >> v1,v2, Eq.(2.15)"},
    {"name": "OO", "parameter_type": "Internal", "indices": ["SU3L", "SU3L"], "value_rules": [
      {"lhs": "OO[1,1]", "rhs": "s12"}, {"lhs": "OO[1,2]", "rhs": "-c12"}, {"lhs": "OO[1,3]", "rhs": "0"},
      {"lhs": "OO[2,1]", "rhs": "c12"}, {"lhs": "OO[2,2]", "rhs": "s12"}, {"lhs": "OO[2,3]", "rhs": "0"},
      {"lhs": "OO[3,1]", "rhs": "0"}, {"lhs": "OO[3,2]", "rhs": "0"}, {"lhs": "OO[3,3]", "rhs": "1"}],
      "description": "CP-odd scalar rotation matrix O, Eq.(2.19), in the decoupling limit, Eq.(2.20)"},
    {"name": "gZqL", "parameter_type": "Internal", "value": "-gw s331/(2 Sqrt[3]) + gX c331 XQ12", "interaction_order": ["QED", 1], "description": "Z' coupling to left-handed u,d,c,s (Table 11)"},
    {"name": "gZqJ", "parameter_type": "Internal", "value": "gw s331/Sqrt[3] + gX c331 XQ12", "interaction_order": ["QED", 1], "description": "Z' coupling to left-handed D and S quarks (Table 11)"},
    {"name": "gZq3L", "parameter_type": "Internal", "value": "gw s331/(2 Sqrt[3]) + gX c331 XQ3", "interaction_order": ["QED", 1], "description": "Z' coupling to left-handed t and b (anti-triplet, Table 11)"},
    {"name": "gZq3T", "parameter_type": "Internal", "value": "-gw s331/Sqrt[3] + gX c331 XQ3", "interaction_order": ["QED", 1], "description": "Z' coupling to the left-handed T quark (Table 11)"},
    {"name": "gZlL", "parameter_type": "Internal", "value": "gw s331/(2 Sqrt[3]) + gX c331 XLL", "interaction_order": ["QED", 1], "description": "Z' coupling to left-handed charged leptons and neutrinos (Table 11)"},
    {"name": "gZlE", "parameter_type": "Internal", "value": "-gw s331/Sqrt[3] + gX c331 XLL", "interaction_order": ["QED", 1], "description": "Z' coupling to the left-handed heavy leptons E (Table 11)"},
    {"name": "gZRu", "parameter_type": "Internal", "value": "2/3 gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed up-type quarks (Table 11)"},
    {"name": "gZRd", "parameter_type": "Internal", "value": "-1/3 gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed down-type quarks (Table 11)"},
    {"name": "gZRl", "parameter_type": "Internal", "value": "-gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed charged leptons (Table 11)"},
    {"name": "gZRD", "parameter_type": "Internal", "value": "QDS gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed D and S quarks (Table 11)"},
    {"name": "gZRT", "parameter_type": "Internal", "value": "QTq gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to the right-handed T quark (Table 11)"},
    {"name": "gZRE", "parameter_type": "Internal", "value": "QEl gX c331", "interaction_order": ["QED", 1], "description": "Z' coupling to right-handed heavy leptons (Table 11)"},
    {"name": "gZpV", "parameter_type": "Internal", "value": "-Sqrt[3] gw s331/2", "interaction_order": ["QED", 1], "description": "Z' charge of the (Y,V) gauge doublet, = -Sqrt[3] g s331/2 (Table 10: Z'Y+Y- and Z'V+V-)"},
    {"name": "gZHY", "parameter_type": "Internal", "value": "c23^2 (-gw s331/(2 Sqrt[3]) + gX c331 Xchi) + s23^2 (-gw s331/Sqrt[3] - gX c331 Xeta)", "interaction_order": ["QED", 1], "description": "Z' charge of the charged scalar H^QY, from the chi/eta mixing of Eq.(2.26)"},
    {"name": "gZHV", "parameter_type": "Internal", "value": "c13^2 (-gw s331/(2 Sqrt[3]) + gX c331 Xchi) + s13^2 (-gw s331/Sqrt[3] - gX c331 Xrho)", "interaction_order": ["QED", 1], "description": "Z' charge of the charged scalar H^QV, from the chi/rho mixing of Eq.(2.30)"},
    {"name": "gZHp", "parameter_type": "Internal", "value": "c12^2 (gw s331/(2 Sqrt[3]) - gX c331 Xeta) + s12^2 (-gw s331/(2 Sqrt[3]) + gX c331 Xrho)", "interaction_order": ["QED", 1], "description": "Z' charge of the charged scalar H+, from the eta/rho mixing of Eq.(2.23)"},
    {"name": "yJD", "parameter_type": "Internal", "value": "Sqrt[2] MDQ/v3", "interaction_order": ["QED", 1], "description": "Yukawa coupling yJ_11 of the D quark to the chi triplet, Eq.(2.61); MD = yJD v3/Sqrt[2]"},
    {"name": "yJS", "parameter_type": "Internal", "value": "Sqrt[2] MSQ/v3", "interaction_order": ["QED", 1], "description": "Yukawa coupling yJ_22 of the S quark to the chi triplet, Eq.(2.61)"},
    {"name": "yJT", "parameter_type": "Internal", "value": "Sqrt[2] MTQ/v3", "interaction_order": ["QED", 1], "description": "Yukawa coupling yJ_33 of the T quark to the conjugate chi triplet, Eq.(2.61)"},
    {"name": "yE331", "parameter_type": "Internal", "indices": ["Generation"], "value_rules": [
      {"lhs": "yE331[1]", "rhs": "Sqrt[2] MEe/v3"},
      {"lhs": "yE331[2]", "rhs": "Sqrt[2] MEm/v3"},
      {"lhs": "yE331[3]", "rhs": "Sqrt[2] MEt/v3"}],
      "interaction_order": ["QED", 1], "description": "Yukawa couplings yE of the heavy leptons to the conjugate chi triplet, Eq.(2.62)"},
    {"name": "yu331", "parameter_type": "Internal", "indices": ["Generation"], "value_rules": [
      {"lhs": "yu331[1]", "rhs": "Sqrt[2] ymup/v2"},
      {"lhs": "yu331[2]", "rhs": "Sqrt[2] ymc/v2"},
      {"lhs": "yu331[3]", "rhs": "-Sqrt[2] ymt/v1"}],
      "interaction_order": ["QED", 1], "description": "331 up-type Yukawa couplings, Eq.(2.61): u,c from eta (vev v2), t from conjugate rho (vev v1); the minus sign follows the -t entry of the q3L anti-triplet, Eq.(2.56)"},
    {"name": "yd331", "parameter_type": "Internal", "indices": ["Generation"], "value_rules": [
      {"lhs": "yd331[1]", "rhs": "Sqrt[2] ymdo/v1"},
      {"lhs": "yd331[2]", "rhs": "Sqrt[2] yms/v1"},
      {"lhs": "yd331[3]", "rhs": "Sqrt[2] ymb/v2"}],
      "interaction_order": ["QED", 1], "description": "331 down-type Yukawa couplings, Eq.(2.61): d,s from rho (vev v1), b from conjugate eta (vev v2)"},
    {"name": "yl331", "parameter_type": "Internal", "indices": ["Generation"], "value_rules": [
      {"lhs": "yl331[1]", "rhs": "Sqrt[2] yme/v2"},
      {"lhs": "yl331[2]", "rhs": "Sqrt[2] ymm/v2"},
      {"lhs": "yl331[3]", "rhs": "Sqrt[2] ymtau/v2"}],
      "interaction_order": ["QED", 1], "description": "331 charged-lepton Yukawa couplings from the conjugate eta triplet, Eq.(2.62)"}
  ],
  "particles": [
    {"spin_type": "V", "class_index": 20, "class_name": "Zp", "self_conjugate": true,
     "mass": {"sym": "MZp", "value": "Internal"}, "width": {"sym": "WZp", "value": "Automatic"},
     "pdg": 32, "particle_name": "Zp", "full_name": "Zprime boson of SU(3)L x U(1)X", "propagator_label": "Zp", "propagator_type": "Sine", "propagator_arrow": "None"},
    {"spin_type": "V", "class_index": 21, "class_name": "Yp", "self_conjugate": false,
     "mass": {"sym": "MYp", "value": "Internal"}, "width": {"sym": "WYp", "value": "Automatic"},
     "quantum_numbers": {"Q": "2"}, "pdg": 9000034, "particle_name": "Y++", "antiparticle_name": "Y--",
     "full_name": "Y gauge boson, charge QY = (Sqrt[3] beta+1)/2 = 2", "propagator_label": "Y", "propagator_type": "Sine", "propagator_arrow": "Forward"},
    {"spin_type": "V", "class_index": 22, "class_name": "Vp", "self_conjugate": false,
     "mass": {"sym": "MVp", "value": "Internal"}, "width": {"sym": "WVp", "value": "Automatic"},
     "quantum_numbers": {"Q": "1"}, "pdg": 9000035, "particle_name": "V+", "antiparticle_name": "V-",
     "full_name": "V gauge boson, charge QV = (Sqrt[3] beta-1)/2 = 1", "propagator_label": "V", "propagator_type": "Sine", "propagator_arrow": "Forward"},
    {"spin_type": "V", "class_index": 23, "class_name": "WY", "self_conjugate": false, "unphysical": true,
     "indices": ["SU2D"], "flavor_index": "SU2D", "quantum_numbers": {"Y": "3/2"},
     "definitions": ["WY[mu_,1] -> Yp[mu]", "WY[mu_,2] -> Vp[mu]"]},
    {"spin_type": "S", "class_index": 20, "class_name": "H2", "self_conjugate": true,
     "mass": {"sym": "MH2", "value": "2900."}, "width": {"sym": "WH2", "value": "Automatic"},
     "pdg": 35, "particle_name": "H2", "full_name": "second CP-even neutral scalar, Eq.(2.67)", "propagator_label": "H2", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 21, "class_name": "H3", "self_conjugate": true,
     "mass": {"sym": "MH3", "value": "2000."}, "width": {"sym": "WH3", "value": "Automatic"},
     "pdg": 45, "particle_name": "H3", "full_name": "third CP-even neutral scalar (chi-like), Eq.(2.68)", "propagator_label": "H3", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 22, "class_name": "H0", "self_conjugate": true,
     "mass": {"sym": "MH0", "value": "2900."}, "width": {"sym": "WH0", "value": "Automatic"},
     "pdg": 36, "particle_name": "H0", "full_name": "CP-odd neutral scalar, Eq.(2.68)", "propagator_label": "H0", "propagator_type": "ScalarDash", "propagator_arrow": "None"},
    {"spin_type": "S", "class_index": 23, "class_name": "Hp", "self_conjugate": false,
     "mass": {"sym": "MHp", "value": "2900."}, "width": {"sym": "WHp", "value": "Automatic"},
     "quantum_numbers": {"Q": "1", "Y": "1"}, "pdg": 37, "particle_name": "H+", "antiparticle_name": "H-",
     "full_name": "singly charged scalar, Eq.(2.69)", "propagator_label": "Hp", "propagator_type": "ScalarDash", "propagator_arrow": "Forward"},
    {"spin_type": "S", "class_index": 24, "class_name": "HY", "self_conjugate": false,
     "mass": {"sym": "MHY", "value": "1400."}, "width": {"sym": "WHY", "value": "Automatic"},
     "quantum_numbers": {"Q": "2", "Y": "2"}, "pdg": 9000037, "particle_name": "HY++", "antiparticle_name": "HY--",
     "full_name": "charged scalar of charge QY = 2, Eq.(2.70)", "propagator_label": "HY", "propagator_type": "ScalarDash", "propagator_arrow": "Forward"},
    {"spin_type": "S", "class_index": 25, "class_name": "HV", "self_conjugate": false,
     "mass": {"sym": "MHV", "value": "1300."}, "width": {"sym": "WHV", "value": "Automatic"},
     "quantum_numbers": {"Q": "1", "Y": "1"}, "pdg": 9000038, "particle_name": "HV+", "antiparticle_name": "HV-",
     "full_name": "charged scalar of charge QV = 1, Eq.(2.71)", "propagator_label": "HV", "propagator_type": "ScalarDash", "propagator_arrow": "Forward"},
    {"spin_type": "S", "class_index": 30, "class_name": "rhoT", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L"], "flavor_index": "SU3L",
     "definitions": ["rhoT[1] -> -s12 Hp", "rhoT[2] -> (UU[1,2] H2 + UU[1,3] H3 + I OO[1,1] H0)/Sqrt[2]", "rhoT[3] -> -s13 HVbar"]},
    {"spin_type": "S", "class_index": 31, "class_name": "etaT", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L"], "flavor_index": "SU3L",
     "definitions": ["etaT[1] -> (UU[2,2] H2 + UU[2,3] H3 + I OO[2,1] H0)/Sqrt[2]", "etaT[2] -> c12 Hpbar", "etaT[3] -> -s23 HYbar"]},
    {"spin_type": "S", "class_index": 32, "class_name": "chiT", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L"], "flavor_index": "SU3L",
     "definitions": ["chiT[1] -> c23 HY", "chiT[2] -> c13 HV", "chiT[3] -> (UU[3,2] H2 + UU[3,3] H3 + I OO[3,1] H0)/Sqrt[2]"]},
    {"spin_type": "F", "class_index": 20, "class_name": "DQ", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "MDQ", "value": "1000."}, "width": {"sym": "WDQ", "value": "Automatic"},
     "quantum_numbers": {"Q": "-4/3", "Y": "-4/3"}, "pdg": 9000001, "particle_name": "D", "antiparticle_name": "D~",
     "full_name": "heavy quark D, third member of the q1L triplet, Eq.(2.56)", "propagator_label": "D", "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 21, "class_name": "SQ", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "MSQ", "value": "1000."}, "width": {"sym": "WSQ", "value": "Automatic"},
     "quantum_numbers": {"Q": "-4/3", "Y": "-4/3"}, "pdg": 9000002, "particle_name": "S", "antiparticle_name": "S~",
     "full_name": "heavy quark S, third member of the q2L triplet, Eq.(2.56)", "propagator_label": "S", "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 22, "class_name": "TQ", "self_conjugate": false,
     "indices": ["Colour"], "mass": {"sym": "MTQ", "value": "1000."}, "width": {"sym": "WTQ", "value": "Automatic"},
     "quantum_numbers": {"Q": "5/3", "Y": "5/3"}, "pdg": 9000003, "particle_name": "T", "antiparticle_name": "T~",
     "full_name": "heavy quark T, third member of the q3L anti-triplet, Eq.(2.56)", "propagator_label": "T", "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 23, "class_name": "EL", "self_conjugate": false,
     "class_members": ["Ee", "Em", "Et"], "indices": ["Generation"], "flavor_index": "Generation",
     "mass": {"sym": "MEL", "members": [["MEe", "1000."], ["MEm", "1000."], ["MEt", "1000."]]},
     "width": {"sym": "WEL", "members": [["WEe", "Automatic"], ["WEm", "Automatic"], ["WEt", "Automatic"]]},
     "quantum_numbers": {"Q": "1", "Y": "1", "LeptonNumber": "1"},
     "pdg": [9000011, 9000013, 9000015],
     "particle_name": ["Ee+", "Em+", "Et+"], "antiparticle_name": ["Ee-", "Em-", "Et-"],
     "full_name": ["heavy lepton Ee", "heavy lepton Emu", "heavy lepton Etau"],
     "propagator_label": ["EL", "Ee", "Em", "Et"], "propagator_type": "Straight", "propagator_arrow": "Forward"},
    {"spin_type": "F", "class_index": 30, "class_name": "q1L", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L", "Colour"], "flavor_index": "SU3L",
     "definitions": ["q1L[sp1_,1,cc_] :> Module[{sp2}, ProjM[sp1,sp2] uq[sp2,1,cc]]", "q1L[sp1_,2,cc_] :> Module[{sp2}, ProjM[sp1,sp2] dq[sp2,1,cc]]", "q1L[sp1_,3,cc_] :> Module[{sp2}, ProjM[sp1,sp2] DQ[sp2,cc]]"]},
    {"spin_type": "F", "class_index": 31, "class_name": "q2L", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L", "Colour"], "flavor_index": "SU3L",
     "definitions": ["q2L[sp1_,1,cc_] :> Module[{sp2}, ProjM[sp1,sp2] uq[sp2,2,cc]]", "q2L[sp1_,2,cc_] :> Module[{sp2}, ProjM[sp1,sp2] dq[sp2,2,cc]]", "q2L[sp1_,3,cc_] :> Module[{sp2}, ProjM[sp1,sp2] SQ[sp2,cc]]"]},
    {"spin_type": "F", "class_index": 32, "class_name": "q3L", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L", "Colour"], "flavor_index": "SU3L",
     "definitions": ["q3L[sp1_,1,cc_] :> Module[{sp2}, ProjM[sp1,sp2] dq[sp2,3,cc]]", "q3L[sp1_,2,cc_] :> Module[{sp2}, -ProjM[sp1,sp2] uq[sp2,3,cc]]", "q3L[sp1_,3,cc_] :> Module[{sp2}, ProjM[sp1,sp2] TQ[sp2,cc]]"]},
    {"spin_type": "F", "class_index": 33, "class_name": "lL", "self_conjugate": false, "unphysical": true,
     "indices": ["SU3L", "Generation"], "flavor_index": "SU3L",
     "definitions": ["lL[sp1_,1,ff_] :> Module[{sp2}, ProjM[sp1,sp2] l[sp2,ff]]", "lL[sp1_,2,ff_] :> Module[{sp2}, -ProjM[sp1,sp2] vl[sp2,ff]]", "lL[sp1_,3,ff_] :> Module[{sp2}, ProjM[sp1,sp2] EL[sp2,ff]]"]}
  ],
  "lagrangian_terms": [
    {"name": "LZpkin", "delayed": true,
     "expression": "Block[{mu,nu}, ExpandIndices[-1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]]"},
    {"name": "LYVkin", "delayed": true,
     "expression": "Block[{mu,nu,ii}, ExpandIndices[-1/2 (DC[WYbar[nu,ii],mu] - DC[WYbar[mu,ii],nu] + I gZpV (Zp[mu] WYbar[nu,ii] - Zp[nu] WYbar[mu,ii])) (DC[WY[nu,ii],mu] - DC[WY[mu,ii],nu] - I gZpV (Zp[mu] WY[nu,ii] - Zp[nu] WY[mu,ii])) + MYp^2 Ypbar[mu] Yp[mu] + MVp^2 Vpbar[mu] Vp[mu], FlavorExpand -> {SU2D, SU2W}]]"},
    {"name": "LNPS", "delayed": true,
     "expression": "Block[{mu}, ExpandIndices[1/2 del[H2,mu] del[H2,mu] - 1/2 MH2^2 H2^2 + 1/2 del[H3,mu] del[H3,mu] - 1/2 MH3^2 H3^2 + 1/2 del[H0,mu] del[H0,mu] - 1/2 MH0^2 H0^2 + (DC[Hpbar,mu] + I gZHp Zp[mu] Hpbar) (DC[Hp,mu] - I gZHp Zp[mu] Hp) - MHp^2 Hpbar Hp + (DC[HYbar,mu] + I gZHY Zp[mu] HYbar) (DC[HY,mu] - I gZHY Zp[mu] HY) - MHY^2 HYbar HY + (DC[HVbar,mu] + I gZHV Zp[mu] HVbar) (DC[HV,mu] - I gZHV Zp[mu] HV) - MHV^2 HVbar HV]]"},
    {"name": "LNPF", "delayed": true,
     "expression": "Block[{mu,sp,ff,cc}, ExpandIndices[I DQbar.Ga[mu].DC[DQ,mu] + I SQbar.Ga[mu].DC[SQ,mu] + I TQbar.Ga[mu].DC[TQ,mu] + I ELbar.Ga[mu].DC[EL,mu] - MDQ DQbar[sp,cc].DQ[sp,cc] - MSQ SQbar[sp,cc].SQ[sp,cc] - MTQ TQbar[sp,cc].TQ[sp,cc] - MEL[ff] ELbar[sp,ff].EL[sp,ff]]]"},
    {"name": "LZpF", "delayed": true,
     "expression": "Block[{mu,ff,cc,sp1,sp2,sp3}, ExpandIndices[Zp[mu] (gZqL (q1Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q1L[sp2,1,cc] + q1Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q1L[sp2,2,cc] + q2Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q2L[sp2,1,cc] + q2Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q2L[sp2,2,cc]) + gZqJ (q1Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q1L[sp2,3,cc] + q2Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q2L[sp2,3,cc]) + gZq3L (q3Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q3L[sp2,1,cc] + q3Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q3L[sp2,2,cc]) + gZq3T q3Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q3L[sp2,3,cc] + gZlL (lLbar[sp1,1,ff] Ga[mu,sp1,sp2] lL[sp2,1,ff] + lLbar[sp1,2,ff] Ga[mu,sp1,sp2] lL[sp2,2,ff]) + gZlE lLbar[sp1,3,ff] Ga[mu,sp1,sp2] lL[sp2,3,ff] + gZRu uRbar[sp1,ff,cc] Ga[mu,sp1,sp2] uR[sp2,ff,cc] + gZRd dRbar[sp1,ff,cc] Ga[mu,sp1,sp2] dR[sp2,ff,cc] + gZRl lRbar[sp1,ff] Ga[mu,sp1,sp2] lR[sp2,ff] + gZRD (DQbar[sp1,cc] Ga[mu,sp1,sp2] ProjP[sp2,sp3] DQ[sp3,cc] + SQbar[sp1,cc] Ga[mu,sp1,sp2] ProjP[sp2,sp3] SQ[sp3,cc]) + gZRT TQbar[sp1,cc] Ga[mu,sp1,sp2] ProjP[sp2,sp3] TQ[sp3,cc] + gZRE ELbar[sp1,ff] Ga[mu,sp1,sp2] ProjP[sp2,sp3] EL[sp3,ff])]]"},
    {"name": "LYVF", "delayed": true,
     "expression": "Block[{mu,ff,cc,sp1,sp2,lag}, lag = ExpandIndices[gw/Sqrt[2] Yp[mu] (q1Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q1L[sp2,3,cc] + q2Lbar[sp1,1,cc] Ga[mu,sp1,sp2] q2L[sp2,3,cc]) + gw/Sqrt[2] Vp[mu] (q1Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q1L[sp2,3,cc] + q2Lbar[sp1,2,cc] Ga[mu,sp1,sp2] q2L[sp2,3,cc]) - gw/Sqrt[2] Yp[mu] (q3Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q3L[sp2,1,cc] + lLbar[sp1,3,ff] Ga[mu,sp1,sp2] lL[sp2,1,ff]) - gw/Sqrt[2] Vp[mu] (q3Lbar[sp1,3,cc] Ga[mu,sp1,sp2] q3L[sp2,2,cc] + lLbar[sp1,3,ff] Ga[mu,sp1,sp2] lL[sp2,2,ff])]; lag + HC[lag]]"},
    {"name": "LYuk331", "delayed": true,
     "expression": "Block[{ii,ff,cc,sp,lag}, lag = ExpandIndices[-yu331[1] q1Lbar[sp,ii,cc] uq[sp,1,cc] etaT[ii] - yu331[2] q2Lbar[sp,ii,cc] uq[sp,2,cc] etaT[ii] - yu331[3] q3Lbar[sp,ii,cc] uq[sp,3,cc] rhoTbar[ii] - yd331[1] q1Lbar[sp,ii,cc] dq[sp,1,cc] rhoT[ii] - yd331[2] q2Lbar[sp,ii,cc] dq[sp,2,cc] rhoT[ii] - yd331[3] q3Lbar[sp,ii,cc] dq[sp,3,cc] etaTbar[ii] - yJD q1Lbar[sp,ii,cc] DQ[sp,cc] chiT[ii] - yJS q2Lbar[sp,ii,cc] SQ[sp,cc] chiT[ii] - yJT q3Lbar[sp,ii,cc] TQ[sp,cc] chiTbar[ii] - yl331[ff] lLbar[sp,ii,ff] l[sp,ff] etaTbar[ii] - yE331[ff] lLbar[sp,ii,ff] EL[sp,ff] chiTbar[ii], FlavorExpand -> SU3L]; lag + HC[lag]]"},
    {"name": "L331", "delayed": true,
     "expression": "LSM + LZpkin + LYVkin + LNPS + LNPF + LZpF + LYVF + LYuk331"}
  ]
}
```