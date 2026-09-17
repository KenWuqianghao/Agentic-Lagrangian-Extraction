## Self-audit table

Fields: scalar dim = 1, `del` dim = 1. All new fields (`chi`, `H2`, `phi1`, `s1`) are real, neutral, colour- and SU(2)-singlets, so every Q-sum, Y-sum and SU(2)/SU(3) contraction below is trivially 0/singlet. No lepton/baryon number, no `CC[...]`, no fermions involved, so those columns are n/a throughout. All couplings are real ⇒ every term is its own Hermitian conjugate (no separate `HC[...]` needed).

| term | fields | d | coupling | coupling dim (4−d) | 1/Λ | Q | Y | SU(2) | SU(3) | new‑U(1) | L/B | CC[] | fraction/root check | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LX` kin | `del[chi]·del[chi]` | 4 | 1/2 (dimensionless) | 0 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | trivial | self-conj. |
| `LX` mass | `chi^2` | 2 | `Mx^2` | 2 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | trivial | self-conj. |
| `LH2` kin | `del[H2]·del[H2]` | 4 | 1/2 | 0 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | trivial | self-conj. |
| `LH2` mass | `H2^2` | 2 | `MH2^2` | 2 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | trivial | self-conj. |
| `LPortal3a` | `phi1·chi^2` | 3 | `-(1/2) lamPS*vev` | 1 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | matches paper eq. (A.1)–(A.3) term-by-term ("keeping only terms ∝ φχ², sχ²") | self-conj. |
| `LPortal3b` | `s1·chi^2` | 3 | `-(1/2) lamS*vs` | 1 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | matches paper eq. (A.1)–(A.3); combined with 3a and the mixing rotation this reduces to eq. (A.5)–(A.6), independently cross-checked against eq. (2.19)–(2.20) (Γ(h/H→χχ)) — placement of sinθ/vs (not vs/sinθ) confirmed | self-conj. |
| `LPortal4` term 1 | `phi1^2·chi^2` | 4 | `-(1/4) lamPS` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | own extension of eq. (2.2)–(2.3) to quadratic order (not explicit in paper appendix; same operators as A.1) | self-conj. |
| `LPortal4` term 2 | `s1^2·chi^2` | 4 | `-(1/4) lamS` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | own extension, same source operator `|S|^4` | self-conj. |
| `LPortal4` term 3 | `chi^4` | 4 | `-(1/8) lamS` | 0 ✓ | n/a | 0 | 0 | singlet | singlet | n/a | n/a | n/a | direct expansion of `-(lamS/2)|S|^4`, unambiguous | self-conj. |
| `lamPS` (Internal) | — | — | — | — | — | — | — | — | — | — | — | — | value = eq. (2.16)/(2.18) `(MH2^2-MH^2) sinθ cosθ/(vev·vs)`, verified dimensionless and → small for large `vs`, matching paper's qualitative statement | — |
| `lamS` (Internal) | — | — | — | — | — | — | — | — | — | — | — | — | value = eq. (2.17) `(MH^2 sin²θ+MH2^2 cos²θ)/vs^2` | — |

- Per-new-class kinetic+mass confirmation: `chi` → `LX` (kin+mass), `H2` → `LH2` (kin+mass); both appear in `LTotal`.
- No non-fundamental colour representation is introduced (no `AddGaugeRepresentation[...]` needed).
- `SelfConjugate -> True` classes: `chi`, `H2`, `phi1`, `s1` — none carries a `QuantumNumbers` field. Confirmed.
- Name check: `chi, H2, phi1, s1, Mx, vs, thx, MH2, WH2, sxth, cxth, lamPS, lamS, LX, LH2, LPortal3, LPortal4, LTotal, NP, PNGDM` — none is a Mathematica built-in, a FeynRules reserved symbol, or a name already declared in SM.fr (checked against `H, Phi, Z, W, A, G, B, Wi, ee, gs, gw, g1, sw, cw, vev, MZ, MW, WZ, WW, MH, WH, lam, muH, yl, yu, yd, CKM, cabi, aEW, aEWM1, Gf, aS, ym*, ...`).
- Single total: `LTotal := LSM + LX + LH2 + LPortal3 + LPortal4;` sums the inherited SM Lagrangian plus every new term defined above.
- Scope caveat (documented, not a rule violation): SM.fr fixes `Phi[2] -> (vev+H+I G0)/Sqrt[2]` and its own Yukawa/gauge terms in terms of the literal field `H`, which this add-on cannot edit; consequently the mixing-induced suppression of the SM-like Higgs' couplings to fermions/gauge bosons (paper's cosθ/sinθ factors on `κ_{hff̄}`, `μ_h`, eqs. 2.20–2.23) is not re-derivable inside this file and is not included — only the genuinely new χ/H2 sector (masses, portal trilinears and quartics) is added, which is the physics that is exactly and completely determined by the paper.
- Reference/cached model file read: none — only the SM.fr and paper text supplied in this message were used.

```mathematica
(* ****************************************************************** *)
(* FeynRules add-on model file for pseudo-Nambu-Goldstone Dark Matter  *)
(* Based on arXiv:1912.04008 (Arina, Beniwal, Degrande, Heisig,        *)
(* Scaffidi). Loaded on top of SM.fr.                                  *)
(* ****************************************************************** *)

M$ModelName = "pNG_gen";

M$Information = {
  Authors      -> {"pNG DM FeynRules add-on (auto-extracted)"},
  Version      -> "1.0",
  Date         -> "17. 09. 2026",
  References   -> {"arXiv:1912.04008"}
};

(* ************************** *)
(* *** Interaction orders *** *)
(* ************************** *)

M$InteractionOrderHierarchy = {
  {QCD, 1},
  {QED, 2},
  {NP,  1}
};

(* No new indices are required: chi, H2, phi1 and s1 are all          *)
(* colour singlets, SU(2) singlets, with Q = Y = 0.                    *)

(* ************************** *)
(* **** Particle classes **** *)
(* ************************** *)

M$ClassesDescription = {

(* pNG dark matter: pseudo-Goldstone of the softly broken dark U(1),   *)
(* stable real scalar, physical mass eigenstate (Im[S]).               *)
  S[101] == {
    ClassName       -> chi,
    SelfConjugate   -> True,
    Mass            -> {Mx, 62.573},
    Width           -> 0,
    PropagatorLabel -> "chi",
    PropagatorType  -> D,
    PropagatorArrow -> None,
    PDG             -> 52,
    ParticleName    -> "chi",
    FullName        -> "pNG dark matter"
  },

(* Heavy CP-even scalar mass eigenstate (mixture of the singlet real   *)
(* scalar and the SM Higgs doublet fluctuation).                       *)
  S[102] == {
    ClassName       -> H2,
    SelfConjugate   -> True,
    Mass            -> {MH2, 125.30},
    Width           -> {WH2, 0.},
    PropagatorLabel -> "H2",
    PropagatorType  -> D,
    PropagatorArrow -> None,
    PDG             -> 35,
    ParticleName    -> "H2",
    FullName        -> "Heavy CP-even scalar"
  },

(* Unphysical gauge/interaction-eigenstate fluctuations, needed only   *)
(* to encode the h-H2 mixing rotation (eq. 2.11 of the paper) in the   *)
(* portal terms below.                                                  *)
  S[103] == {
    ClassName     -> phi1,
    Unphysical    -> True,
    SelfConjugate -> True,
    Definitions   -> { phi1 -> cxth*H + sxth*H2 }
  },
  S[104] == {
    ClassName     -> s1,
    Unphysical    -> True,
    SelfConjugate -> True,
    Definitions   -> { s1 -> -sxth*H + cxth*H2 }
  }
};

(* ************************** *)
(* *****   Parameters   ***** *)
(* ************************** *)

M$Parameters = {

  (* External parameters: the model's four free parameters are        *)
  (* {Mx, vs, thx, MH2}; MH (=125) is inherited from SM.fr.            *)
  vs == {
    ParameterType -> External,
    BlockName     -> PNGDM,
    OrderBlock    -> 1,
    Value         -> 13155.1,
    TeX           -> Subscript[v,s],
    Description   -> "Dark U(1) singlet scalar vacuum expectation value [GeV]"
  },
  thx == {
    ParameterType -> External,
    BlockName     -> PNGDM,
    OrderBlock    -> 2,
    Value         -> 1.53,
    TeX           -> \[Theta],
    Description   -> "h-H2 mixing angle [rad], range [0,Pi/2]"
  },

  (* Internal parameters *)
  sxth == {
    ParameterType -> Internal,
    Value         -> Sin[thx],
    Description   -> "Sine of the h-H2 mixing angle"
  },
  cxth == {
    ParameterType -> Internal,
    Value         -> Cos[thx],
    Description   -> "Cosine of the h-H2 mixing angle"
  },
  lamPS == {
    ParameterType    -> Internal,
    Value            -> (MH2^2 - MH^2) * sxth * cxth / (vev * vs),
    InteractionOrder -> {NP, 2},
    TeX              -> Subscript[\[Lambda], \[CapitalPhi]S],
    Description      -> "Higgs-portal quartic coupling (doublet-singlet), eq. (2.16)/(2.18)"
  },
  lamS == {
    ParameterType    -> Internal,
    Value            -> (MH^2 * sxth^2 + MH2^2 * cxth^2) / vs^2,
    InteractionOrder -> {NP, 2},
    TeX              -> Subscript[\[Lambda], S],
    Description      -> "Singlet scalar quartic self-coupling, eq. (2.17)"
  }
};

(* ************************** *)
(* *****   Lagrangian   ***** *)
(* ************************** *)

(* Kinetic + mass term for the pNG dark matter field chi *)
LX := Block[{mu}, 1/2 del[chi,mu] del[chi,mu] - 1/2 Mx^2 chi^2];

(* Kinetic + mass term for the heavy scalar mass eigenstate H2 *)
LH2 := Block[{mu}, 1/2 del[H2,mu] del[H2,mu] - 1/2 MH2^2 H2^2];

(* Trilinear chi-chi-scalar portal couplings, from eq. (A.1)-(A.4):    *)
(* -(lamPS vev/2) phi1 chi^2 - (lamS vs/2) s1 chi^2, which after the   *)
(* phi1/s1 -> {H,H2} rotation reduces to kappa_{chi chi h}, kappa_{chi *)
(* chi H} of eq. (A.5)-(A.6).                                          *)
LPortal3 := -(1/2) chi^2 (lamPS*vev*phi1 + lamS*vs*s1);

(* Quartic chi-chi-scalar-scalar contact terms and chi self-coupling,  *)
(* from expanding -lamPS*Phi^dag.Phi.|S|^2 and -(lamS/2)|S|^4 to       *)
(* quadratic order in phi1, s1 (same operators as eq. (2.2)-(2.3)).    *)
LPortal4 := -(1/4) lamPS phi1^2 chi^2 - (1/4) lamS s1^2 chi^2 - (1/8) lamS chi^4;

LTotal := LSM + LX + LH2 + LPortal3 + LPortal4;
```