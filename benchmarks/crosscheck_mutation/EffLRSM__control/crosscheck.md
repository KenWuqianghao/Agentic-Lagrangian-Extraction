# Crosscheck: `reconstruction.md` against the paper

RUN-TAG: XM-CROSS-EffLRSM__control

Paper: *Automated Neutrino Jet and Top Jet Predictions at Next-to-Leading-Order with
Parton Shower Matching in Effective Left-Right Symmetric Models*
(Mattelaer, Mitra, Ruiz; IPPP-16-102, CP3-16-51).

---

## 1. Where the paper defines the model

The paper defines the model in Sec. II, "Effective Left-Right Symmetric Model".
The relevant places are:

| Location | Content |
|---|---|
| Sec. I, first displayed equation | Gauge group `SU(3)_c x SU(2)_L x SU(2)_R x U(1)_{B-L}` |
| Sec. II, opening paragraph | Field content: SM states, `W_R^±`, `Z_R`, three heavy Majorana neutrinos `N_i` aligned with the RH chiral states |
| Eq. (chcurrent) | `W_R` charged current to quarks |
| Sec. II, unnumbered equation after Eq. (chcurrent) | `W_R` charged current to leptons, `L_{W_R-l-nu/N}` |
| Eq. (eq:lrsmNuMixing) | Default lepton mixing: `Y` diagonal with unit entries, `X = 0` |
| Table I (`tb:qNumbers`) | `T_L^3`, `T_R^3` and `Q` for each chiral fermion |
| Eq. (neucurrent) | `Z_R` neutral current, with the normalisation factor |
| Two unnumbered equations after Eq. (neucurrent) | `g_L^{Z_R,f}` and `g_R^{Z_R,f}` |
| Eq. (eq:massRelationship) | `M_{Z_R} = sqrt(2 cos^2θ_W / cos2θ_W) × M_{W_R} ≈ 1.7 M_{W_R}` |
| Eq. (eq:lrsmInputs) | `M_{W_R} = 3 TeV`, `m_{N_1} = m_t = 173.3 GeV`, `m_{N_2}, m_{N_3} = 10^12 GeV` |
| Table II (`tb:lrsmParam`) | Masses and total widths of `W_R`, `Z_R`, `N_1` |
| Sec. II C (`sec:modelLimits`) | No scalar sector; `W_R`/`Z_R` self-interactions are ill-defined |
| App. C (`app:GenCuts`) | Heavy neutrino PID = 9900012 |

The paper writes no explicit kinetic or mass term for `W_R`, `Z_R` or `N`. It gives
only the interaction terms and the mass values.

---

## 2. Term-by-term comparison

| paper term (eq. ref) | reconstruction term | verdict | notes |
|---|---|---|---|
| `W_R` kinetic + mass (not written; implied by Sec. II and Table II) | §1.1 `LWRkin`: `-(1/2) W_R†_{μν} W_R^{μν} + M_{W_R}^2 W_R†_μ W_R^μ` | **agree** | The paper gives `W_R` a mass of 3000 GeV but writes no kinetic term. The reconstruction uses the standard complex-vector (Proca) normalisation. Physics content is the same. |
| `Z_R` kinetic + mass (not written; implied by Sec. II and Table II) | §1.2 `LZRkin`: `-(1/4) Z_{Rμν} Z_R^{μν} + (1/2) M_{Z_R}^2 Z_{Rμ} Z_R^μ` | **agree** | Same point. `Z_R` is real, so the `1/4` and `1/2` factors are correct. |
| Three heavy Majorana neutrinos `N_i` (Sec. II, opening paragraph; masses in Eq. (eq:lrsmInputs)) | §1.3 `LNkin`: `(i/2) N̄_f γ^μ ∂_μ N_f - (1/2) M_{N_f} N̄_f N_f`, `f = 1,2,3` | **agree** | The paper states "three heavy Majorana neutrinos". The `1/2` factors are the correct Majorana normalisation. The diagonal mass matrix matches Eq. (eq:lrsmInputs). |
| Eq. (chcurrent): `(-κ_R^q g / √2) ū_i V_ij^{CKM'} W^+_{Rμ} γ^μ P_R d_j + H.c.` | §1.4 `LWRq`: `-(κ_R^q g_w / √2) ū_i (V^R_CKM)_ij γ^μ P_R d_j W_{Rμ} + h.c.` | **agree** | Same prefactor, same sign, same `P_R` chirality, same index order (`ū` carries the first index of `V`). `V^R_CKM` = `V^{CKM'}`, unitary, identity by default (paper: "both the SM and RH CKM matrices to be diagonal with unit entries"). |
| Sec. II, `L_{W_R-l-nu/N}`, heavy-`N` part: `(-κ_R^l g / √2) N̄_{m'} Y_{l m'} W^+_{Rμ} γ^μ P_R l^-` | §1.5 `LWRl`, first current: `-(κ_R^l g_w / √2) N̄_i (Y_N)_ij γ^μ P_R l_j W_{Rμ} + h.c.` | **agree** | Same prefactor, same chirality, same fields. Index order of `Y` is transposed against the paper; see Disagreement D1. |
| Sec. II, `L_{W_R-l-nu/N}`, light-`ν` part: `(-κ_R^l g / √2) ν̄^c_m X_{l m} W^+_{Rμ} γ^μ P_R l^-` | §1.5 `LWRl`, second current: `-(κ_R^l g_w / √2) ν̄^c_i (X_N)_ij γ^μ P_R l_j W_{Rμ} + h.c.` | **agree** | The conjugation is correct: the paper also uses `ν̄^c`, not `ν̄`. Index order transposed; see D1. |
| Eq. (eq:lrsmNuMixing): `\|Y_{eN}\| = \|Y_{μN_2}\| = \|Y_{τN_3}\| = 1`, all other `Y` and all `X` zero | §3.2: `YN` = identity 3x3, `XN` = zero 3x3 | **agree** | Confirmed by Table II: the paper lists one `l^+ N_1` channel of 8.41 GeV, not three. |
| Eq. (neucurrent) prefactor: `-κ_R^f g / sqrt(1 - (1/κ_R^f)^2 tan^2θ_W)` | §1.6 / §1.7 / §3.2: `-κ_R^{q,l} g_w / n_{Z_R}^{q,l}` with `n_{Z_R} = sqrt(1 - t_W^2 / κ_R^2)` | **agree** | Identical. `t_W^2 = s_W^2/c_W^2 = tan^2θ_W`, as the reconstruction states. Separate `q` and `l` versions match the paper, which says `κ_R^f` are the same `κ_R^{q,l}` as for `W_R`. |
| `g_L^{Z_R,f} = (T_L^{3,f} - Q^f) tan^2θ_W / κ_R^{f2}` with Table I | §3.2: `gLZRu = -(1/6) t_W^2/κ_{R,q}^2`; `gLZRd = -(1/6) t_W^2/κ_{R,q}^2`; `gLZRe = +(1/2) t_W^2/κ_{R,l}^2`; `gLZRv = +(1/2) t_W^2/κ_{R,l}^2` | **agree** | All four values follow from Table I: `u: 1/2 - 2/3 = -1/6`; `d: -1/2 + 1/3 = -1/6`; `e: -1/2 + 1 = +1/2`; `ν: 1/2 - 0 = +1/2`. |
| `g_R^{Z_R,f} = T_R^{3,f} - tan^2θ_W Q^f / κ_R^{f2}` with Table I | §3.2: `gRZRu = 1/2 - (2/3) t_W^2/κ^2`; `gRZRd = -1/2 + (1/3) t_W^2/κ^2`; `gRZRe = -1/2 + t_W^2/κ^2`; `gRZRn = 1/2` | **agree** | All four values follow from Table I. `N_R` has `T_R^3 = +1/2` and `Q = 0`, so `gRZRn = 1/2` with no `t_W` part, as the reconstruction says. |
| Eq. (neucurrent), quark part: `f = u, d` over all flavours, flavour diagonal, no H.c. | §1.6 `LZRq`: four chiral terms `g_L^u, g_R^u, g_L^d, g_R^d`, flavour diagonal, no `HC` | **agree** | The paper also writes no H.c. The expression is already hermitian. |
| Eq. (neucurrent), lepton part: `f = e, ν, N` from Table I | §1.7 `LZRl`: `g_L^e`, `g_R^e`, `g_L^ν` (`P_L` only), `g_R^N` (`P_R` only) | **agree** | The asymmetry matches Table I. The table lists `ν_L` (so `T_R^3 = 0`, `Q = 0`, hence `g_R^ν = 0`) and `N_R` (so `T_L^3 = 0`, `Q = 0`, hence `g_L^N = 0`). |
| Sec. II, `κ_R^q` and `κ_R^l` are two independent real normalisations | §3.1: `kapRq`, `kapRl`, both external, both default 1 | **agree** | The paper says "`κ_R^l ∈ R` independently normalizes the `W_R` coupling strength to leptons". |
| Eq. (eq:lrsmInputs) and Table II: `M_{W_R} = 3000 GeV`, `Γ_{W_R} = 84.3 GeV` | §2 field table: `MWR = 3000.`, `WWR = 84.3` | **agree** | Exact match. |
| Eq. (eq:massRelationship) and Table II: `M_{Z_R} = 5070 GeV`, `Γ_{Z_R} = 114 GeV` | §2 field table: `MZR = 5070.`, `WZR = 114.` | **agree** | `sqrt(2 × 0.76874 / 0.53748) × 3000 = 5074`, which rounds to the paper value 5070. |
| Eq. (eq:lrsmInputs) and Table II: `m_{N_1} = 173.3 GeV`, `Γ_{N_1} = 2.12e-8 GeV`; `m_{N_2}, m_{N_3} = 10^12 GeV` | §2 field table: `mn1 = 173.3`, `Wn1 = 2.12e-8`, `mn2 = mn3 = 1.e12`, widths 0 | **agree** | Exact match. The paper sets `m_{N_1} = m_t` on purpose, to compare `N` jets with top jets. |
| App. C: heavy neutrino PID = 9900012 | §2 field table: `n1` PDG 9900012 | **agree** | The `W_R`, `Z_R`, `n2` and `n3` PDG codes do not appear in the paper. They cannot be checked here. |
| Sec. II C: `W_R` and `Z_R` non-Abelian self-interactions and couplings to SM bosons are ill-defined; pair production and vector boson scattering are not modelled correctly | §0 and §4: the new vectors are not gauge fields of any new group, `FS[V,μ,ν]` is abelian, so no self-interactions, and no `W_R W_R Z_R` or `W_R W_R γ` vertices | **agree** | The reconstruction reaches the same conclusion the paper states as a limitation. See D2 for one point to check. |
| Sec. I and Eqs. (eq:ppWRff), (eq:ppZRff): `pp → W_R → tb` or `N_R l^±`, then `N_R → l^± W_R^{∓*} → l^± q q̄'`; `pp → Z_R → tt̄` or `N_R N_R`; signature `l^± l^± + nj` | §4 physics summary: resonant `W_R` production, `pp → W_R → l^± N`, `N → l^± jj` through off-shell `W_R`, same-sign dilepton plus jets, `Z_R → l^+l^-`, `qq̄`, `NN` | **agree** | App. B (`decay n1 > ee q q`, with `ee = e+ e-`) confirms the Majorana, lepton-number-violating decay. |
| Sec. III A: SM part in Feynman gauge with Goldstone couplings; new terms in Unitary gauge | §0: covariant derivatives come from `LSM`, group `SU(3)_c x SU(2)_L x U(1)_Y` | **agree** | The reconstruction does not state the gauge choice. This is a gap in detail, not a conflict. |
| — | §1.7, extra claim: `N̄ γ^μ P_R N = (1/2) N̄ γ^μ γ_5 N`, so the `Z_R N N` vertex is "purely axial, with half the naive strength" | **extra-in-reconstruction** | The operator identity is correct. The strength claim is not in the paper and does not match the paper's own width. See D3. |
| — | §3.2, extra claim: the `Z_R` couplings follow `g = T_R^3 - [T_R^3 + (B-L)/2] t_W^2/κ_R^2` | **agree** | This is the paper's formula rewritten. Use `Q = T_L^3 + T_R^3 + (B-L)/2`. For a left-handed field `T_R^3 = 0`, so `T_L^3 - Q = -(B-L)/2`. The reconstruction states this correctly. |
| — | §2 and §3.1, extra items: `InteractionOrder -> {NP,1}`, `M$InteractionOrderHierarchy {QCD,1},{QED,2},{NP,1}`, class labels `V[100]`, `V[101]`, `F[100]`, block `LRSMINPUTS` | **extra-in-reconstruction** | These are implementation details. The paper does not mention them. They cannot be checked against the paper. |

### Numerical check of the couplings against Table II

Every `Z_R` and `W_R` coupling in the reconstruction reproduces the paper's Table II.
The check uses the paper's SM inputs in Eq. (eq:smInputs):
`α = 1/127.940`, `s_W^2 = 0.23126`, so `g^2 = 0.42472` and `t_W^2 = 0.30083`.

| Channel | Paper Table II [GeV] | From the reconstruction couplings [GeV] |
|---|---|---|
| `W_R → q q̄'` (2 channels) | 50.7 | 50.7 |
| `W_R → t b̄` | 25.2 | 25.2 |
| `W_R → l^+ N_1` (1 channel) | 8.41 | 8.41 |
| `W_R` total | 84.3 | 84.3 |
| `Z_R → q q̄` (5 flavours) | 82.3 | 82.3 |
| `Z_R → t t̄` | 11.3 | 11.3 |
| `Z_R → l^+ l^-` (3 flavours) | 7.64 | 7.64 |
| `Z_R → ν ν` (3 flavours) | 2.78 | 2.77 |
| `Z_R → N_1 N_1` | 10.2 | 10.18 |

This is strong evidence that the field content, the charges, the chirality
assignments and the coefficient structure in the reconstruction match the paper.

---

## 3. Disagreements

### D1. Index order of the lepton mixing matrices `Y` and `X`

**Severity: convention.**

The paper writes `N̄_{m'} Y_{l m'}` and `ν̄^c_m X_{l m}`. The charged-lepton flavour
index `l` comes first, and the neutrino index comes second. The reconstruction
writes `N̄_i (Y_N)_ij l_j` and `ν̄^c_i (X_N)_ij l_j`, so the neutrino index comes
first. The two forms are transposes of each other.

With the default values this makes no difference, because `Y` is the identity and
`X` is zero. It does make a difference for a general off-diagonal `Y` or `X`.

*What a human should check:* open the `.fr` file, find the index order in the
`LWRl` term, and confirm whether `YN[i,j]` has the neutrino index or the lepton
index first. Then check whether a non-diagonal `YN` restriction file would give
the transposed matrix.

### D2. Absence of a `W_R W_R γ` vertex

**Severity: convention.**

The reconstruction states that `W_R` carries electric charge `+1` but is not a
gauge field, so it has no covariant derivative and no self-interactions. It then
concludes that there is no `W_R W_R γ` vertex. A charged vector normally needs a
photon coupling for electromagnetic gauge invariance.

The paper supports the conclusion. Sec. II C says that `W_R` and `Z_R`
self-interactions and their couplings to SM bosons are ill-defined, and that pair
production and vector boson scattering are not modelled correctly. So the
reconstruction agrees with the paper's own statement of the limitation.

*What a human should check:* confirm in the UFO output whether a `W_R W_R γ` vertex
exists, since an electric-charge assignment in FeynRules can still generate one,
and this would change any process with a photon in the initial or final state.

### D3. "Half the naive strength" for the `Z_R N N` vertex

**Severity: substantive.**

The reconstruction says in §1.7 that `N̄ γ^μ P_R N = (1/2) N̄ γ^μ γ_5 N` for a
Majorana field, and concludes that the `Z_R N N` vertex is "purely axial, with
half the naive strength".

The operator identity is correct, because the vector bilinear of a self-conjugate
field vanishes. The strength conclusion does not follow. A Majorana bilinear has
two Wick contractions, and this gives a factor 2 that cancels the `1/2`. The net
vertex is `C γ^μ γ_5`, not `(C/2) γ^μ γ_5`.

The paper's Table II supports the no-reduction result. The quoted
`Γ(Z_R → N_1 N_1) = 10.2 GeV` is reproduced by the paper's own width formula with
`g_R^{Z_R,N} = 1/2` and no extra factor. A literal `1/2` in the vertex would lower
the rate by a factor 4, to about 2.5 GeV.

*What a human should check:* compute `Z_R → N_1 N_1` with the UFO file and compare
it with the 10.2 GeV in Table II, to confirm that the Majorana factor 2 and the
identical-particle phase-space factor `1/2` are both handled correctly.

### D4. Kinetic and mass terms have no paper equation

**Severity: cosmetic.**

The reconstruction gives explicit kinetic and mass terms for `W_R`, `Z_R` and `N`
in §1.1 to §1.3. The paper writes none of them. The paper gives only the
interaction terms, Eqs. (chcurrent) and (neucurrent), the mass values in
Eq. (eq:lrsmInputs), and the widths in Table II.

The normalisations the reconstruction chose are the standard ones, and they are
consistent with the masses and widths in the paper.

*What a human should check:* confirm the `1/2` Majorana factors in `LNkin` against
the `.fr` file, because a wrong factor here would rescale every `N` propagator
normalisation and every `N` width.

---

## 4. Overall assessment

The reconstruction and the paper describe the same model. Every Lagrangian term
the paper writes has a matching term in the reconstruction, with the same
prefactor, the same sign, the same chiral projector, the same field conjugation
and the same mixing matrix. The `Z_R` chiral coefficients in the reconstruction
follow exactly from the paper's two formulas for `g_L^{Z_R,f}` and `g_R^{Z_R,f}`
together with the charges in Table I, and they reproduce all nine partial widths
in Table II to the quoted precision. The masses, the total widths, the two
independent normalisations `κ_R^q` and `κ_R^l`, the default mixing choice
`Y = 1`, `X = 0`, and the heavy neutrino PID all match. The reconstruction also
reaches the paper's own conclusion that the new vectors have no self-interactions,
which Sec. II C states as a limitation of the effective model. Three points remain
open. The lepton mixing matrices are written transposed against the paper, which
only matters away from the default diagonal choice. The absence of a `W_R W_R γ`
vertex agrees with the paper's text but should be confirmed in the UFO output. The
claim that the `Z_R N N` vertex carries "half the naive strength" is a derived
statement that the paper's own `Z_R → N_1 N_1` width does not support, and it is
the one item with a numerical consequence. A human reviewer should resolve these
three points against the implementation file.
