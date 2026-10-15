# Gap analysis: where the shell arm loses score, per paper

Tags: **OBS** = computed with `ref_score.vertex_kinds` or quoted from a file. **INF** = my inference, not run.
Nothing was compiled. Scripts: `/tmp/claude-forensics/scratch/{k,sec,q331,pl}.py` (disposable).
Sector codes: G = gauge self-couplings with a new vector; D1 = new scalar + SM vectors; D2 = new scalar + new vector;
D3 = h + new vector; F1 = new vector + SM fermions; F2 = new vector + new fermion; F3 = SM vector + new fermion;
P = scalar potential; Y1 = new scalar + SM fermions; Y2 = h + new fermion; Y3 = new scalar + new fermion.

## Headline

1. Four of the seven papers lose most of their score to the reference or the metric, not to the agent (OBS).
   - 331: 98 of 174 reference kinds have charge `None`. A perfect model scores 0.42.
   - Monotops: the reference declares the coloured scalars with a typo, so they get colour 1. The delivered model is correct. True F1 is 1.0.
   - B-L-SM: the reference gives the SM-like Higgs PDG 9900025. All 12 extras come from that. True F1 is 0.93.
   - Wprime: the two extras are the paper's own `nu_R`. The reference has no `nu_R`.
2. The real harness gaps are three: no route to an extended gauge group (331, ALRM), no recipe to gauge a new U(1) on the Higgs fields (GeneralU1), and a validate budget smaller than the compile time of a full model (ALRM).

## 331 (metric 0.152; 17 of 174 matched, 50 delivered)

| Sector | Ref (raw) | Shell matched (raw) | Ref (charges at beta=1/sqrt3) | Shell matched (fixed) |
|---|---|---|---|---|
| D2 scalar + Y/V/Z' | 58 | 0 | 55 | 0 |
| D1 scalar + W/Z/A | 39 | 5 | 33 | 5 |
| G self-couplings of Y, V, Z' | 15 | 0 | 29 | 0 |
| P potential | 26 | 1 | 13 | 1 |
| D3 h + new vector | 6 | 0 | 6 | 0 |
| F2 new vector + heavy fermion | 6 | 0 (14 delivered) | 14 | 14 |
| F3 SM vector + heavy fermion | 5 | 0 (8 delivered) | 8 | 8 |
| Y3 scalar + heavy fermion | 6 | 0 (11 delivered) | 14 | 11 |
| Y2 h + heavy fermion | 2 | 0 | 3 | 0 |
| F1, Y1 | 11 | 11 | 11 | 11 |
| Total | 174 | 17 | 186 | 50 (precision 1.0, F1 0.424) |

- **Metric fault (OBS).** `ref_ufo/331/UFO/particles.py:79` has `charge = -1/2 - (Sqrt[3]*beta)/2`. `331.fr:1331` sets `beta` to the free symbol `Bet`. The parser returns `None`, so Y, V, E, J, HY, HV get `q=None` and no delivered kind can match them. All 33 shell-arm "extras" are this artefact: with the reference charges evaluated at the agent's beta, precision is 1.0 (50/50). The cover arm used beta=sqrt3 and also gets precision 1.0 (62/62, F1 0.366) on that reading.
- **Ceiling (OBS).** The reference itself, evaluated at beta=1/sqrt3 and scored against the stored reference, gets F1 0.422 (76 matched, 186 generated).
- **Q2. Missing sectors are in the paper (OBS).** `\cL_{Gauge}=-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}-\frac{1}{4}B_{\mu\nu}B^{\mu\nu}` (tex:421), `\cL_{Higgs}=(D_\mu \rho)^\dagger (D^\mu \rho)+...-V_{Higgs}` with the full potential (tex:180-193), and Appendix A tables "VSS", "VVS", "Four-point couplings of two gauge bosons to two scalars", "Gauge boson self-couplings" (tex:1808-2206).
- **Q3. Class (c) plus (a) (OBS).** `agent_out.md`: "Non-abelian SU(3)_L gauge self-couplings ... are absent — new gauge bosons are treated as independent abelian vectors since an SM add-on cannot declare a new `M$GaugeGroups`." and "Gauge–scalar (VSS/VVS/VVSS) vertices from Appendix A are absent". The prompt says "SM add-on => no M$GaugeGroups block". The potential is replaced by `LScalarPortal := -kappaportal H2^2 H3^2`, "an explicitly-flagged non-paper placeholder".
- **What must be redeclared (INF).** SU(2)_L is inside SU(3)_L, so nothing of the SM.fr electroweak sector survives: gauge groups `SU2L` and `U1Y` become `SU3L` (8 generators, triplet and antitriplet) and `U1X`; `Wi` and `B` become `W^1..8` and `X` with `Definitions` to W, Y, V, A, Z, Z'; `LL` and `QL` become triplets with E and J; `Phi` becomes rho, eta, chi; `LGauge`, `LFermions`, `LHiggs`, `LYukawa`, `LGhost` are rewritten. Only QCD is reusable. This is a standalone model, as the reference is (`how.json`: `load_sm: false`).
- **Q7.** Allow a standalone model for a paper that extends the electroweak group, with a recipe for the group declaration. Gain on the current metric is at most 0.15 to 0.42. With the charge fix it is 0.42 to about 0.9. Sure of the diagnosis. Not confirmed that Sonnet can complete it: the reference compile alone took 1109 s (`STATUS.md`), and the validate timeout is 1350 s.

## ALRM_general (metric 0.0; chain fails; no UFO in the shell arm)

| Sector | Ref | `cc_vanilla_v2` (chain FAIL at MG5) | `cc_sonnet_opt` (chain FAIL, hermiticity) |
|---|---|---|---|
| D2 scalar + W'/Z' | 55 | 0 | 0 |
| D1 scalar + SM vectors | 38 | 5 | 0 |
| G self-couplings W', Z' | 24 | 10 | 0 |
| P potential | 13 | 2 | 0 |
| D3 h + new vector | 8 | 0 | 0 |
| Y1, Y2, Y3 Yukawas | 19 | 8 | 5 |
| F1, F2, F3 currents | 15 | 15 | 11 |
| Total | 172 | 40 (precision 1.0) | 16 (precision 1.0) |

- **Why the shell arm is 0 (OBS).** The model is ambitious: it redeclares SM `Phi` (`S[11]`) and `vl`, adds `Phi1`, `chiL`, `chiRp`, `chiR0` with the paper's `UH`/`UA` mixing matrices, sets `FeynmanGauge = True`, and expands to 2633 terms (`validation/call6/VALIDATION_REPORT.md`: `HEPTAPOD-LAGRANGIAN|...|terms=2633`). Calls 3 to 6 each ended with `compile_timeout` at 1350.1 s during the consistency checks. The agent then hit the 4 h limit (`run.json`: `timed_out: true`, 14400 s). Validate used 5713 s of kernel time plus 3443 s of `lock_wait_seconds`.
- **The budget cannot hold a full model (OBS).** The reference UFO export took 1609 s with `Checks=false` (`STATUS.md`). That is longer than the 1350 s validate timeout.
- **Q2. In the paper (OBS).** "based on the SU(3)_c x SU(2)_L x SU(2)_{R'} x U(1)_{B-L} gauge group" (tex:217), "The model Lagrangian includes, on top of standard gauge-invariant kinetic terms for all fields, a Yukawa interaction Lagrangian and a scalar potential" (tex:333), Eq. `eq:yuk`, Eq. `eq:Hpot`, mixing matrices in Appendix A.
- **Q3. Class (c) plus (e) (OBS).** Shell model comment: "chiR+ : SU2L singlet, Q=1 (no SU(2)_L or SU(2)_R' gauging; EM via Y=Q)". W' and Z' are plain vectors with hand-written currents, so G, D2, D3 cannot appear; no potential is written (`LHiggsALRM` has kinetic terms only). Class (e) is the time budget.
- **An add-on can add a gauge group (OBS).** `cc_vanilla_v2/s1/model/ALRM_general_gen.fr:32` declares `M$GaugeGroups = { SU2R == {...} }` in an add-on; it compiled, passed all four checks, and produced 10 gauge self-coupling kinds. It failed only at the MadGraph import. To be exact, U(1)_Y must also become U(1)_{B-L}, with u_R, e_R in SU(2)_R' doublets and `Phi` a bidoublet (INF).
- **Q7.** First raise the validate budget for large models (timeout above the reference compile time, export the UFO before the slow checks, no lock wait). Then drop the "no M$GaugeGroups" rule. INF gain: 0 to about 0.4 (the vanilla_v2 level) with the budget fix and the group, more with the potential. Medium confidence; the shell model never produced a UFO, so its kind count is not confirmed.

## GeneralU1 (metric 0.40 s1, 0.42 s2; cover 0.54; opt 0.81)

| Sector | Ref | Shell s1 | Shell s2 | Cover | Opt |
|---|---|---|---|---|---|
| D1 H2 + WW/ZZ | 6 | 0 | 0 | 0 | 6 |
| D2 H2 + Z' | 6 | 0 | 0 | 2 | 6 |
| D3 h + Z' (incl. Z'Zh) | 4 | 0 | 0 | 2 | 4 |
| P potential | 7 | 5 | 5 | 5 | 7 |
| Y1 H2 + SM fermions | 3 | 0 | 0 | 0 | 3 |
| G Z'WW | 4 | 0 | 0 | 0 | 0 |
| F1 Z' + SM fermions | 3 | 3 | 3 | 3 | **0** |
| F2 Z'NN, Y3 H2NN | 2 | 2 | 2 | 2 | 0 |
| F3 ZNN, WlN; Y2 hNN | 3 | 0 | 1 | 1 | 0 |
| Total matched | 38 | 10 | 11 | 15 | 26 |

- **Q5. The construct (OBS).** `cc_sonnet_opt` redeclares the SM doublet with the scalar rotation and replaces the SM Higgs Lagrangian: `S[11] ... Phi[2] -> (vev + ca H - sa H2 + I G0)/Sqrt[2]`, `PhiX -> (vPhi + sa H + ca H2)/Sqrt[2]`, `LZpHiggs := I gp xHH Zp[mu] (DC[Phibar[ii],mu] Phi[ii] - Phibar[ii] DC[Phi[ii],mu]) + gp^2 xHH^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii]`, `LZpPhiX := 4 gp^2 PhiX^2 Zp[mu] Zp[mu]`, `LTotal := LSM - LHiggs + LHiggsNew + LZpHiggs + ...`. This gives D1, D2, D3, the two missing P kinds, and Y1 (through `LYukawa`, which uses `Phi`): 21 kinds. The shell models use `PhiX -> (vPhi + HX)/Sqrt[2]` with `del[PhiXbar, mu] del[PhiX, mu]` and an external `MZp`; the cover model adds only the Z'Z'-scalar terms.
- **Warning (OBS).** The opt UFO has no Z'-fermion vertex at all (`grep P.Zp score_ufo/vertices.py`: 10 lines, all scalar). `LZpFerm` is in `LTotal` but did not reach the UFO; cause not confirmed. The metric gives 0.81 to a model without Z' -> f f. The gate saw only the three N without a vertex.
- **Q2 (OBS).** Potential with `\lambda^\prime (H^\dag H)(\Phi^\dag \Phi)` is in the paper (tex:158), but "In the limit of small \lambda^\prime, the mixing between the scalar fields H and \Phi is negligible". So D1 and Y1 (9 kinds) need a mixing angle the paper does not use: reference beyond paper. D2 and D3 (10 kinds) follow from `M_{Z'} = g' \sqrt{4 v_\Phi^2 + \frac{1}{4}x_H^2 v^2}` (tex:169); the paper gives no covariant derivative explicitly. G (4 kinds, Z'WW) needs Z-Z' mass mixing: not in the paper. F3 and Y2 need nu-N mixing; the paper gives only the mass matrix (Eq. `num`).
- **Q3. Class (a) (OBS).** Shell s1: "fixing them (fully gauging U(1)_X on `Phi`) would require introducing Z–Z′ mixing machinery not exercised anywhere in the paper's quantitative results, at real risk to the passing chain." and "Higgs portal quartic λ′ set to 0 per the paper's own 'small λ′, analyzed separately' statement".
- **Q4 (OBS).** Extra `Zp nu nu` is correct physics; the reference gives its light neutrinos PDG 1200/1400/1600, so they count as new fermions. Extra `N h cl` is an error: `LYukNu` uses `LLbar[sp, ii, ff].NMR[sp, ff] Phi[ii]` (prompt rule 4 requires `Phibar[jj] Eps[ii, jj]`), which violates charge.
- **Q7.** A protocol recipe "gauged U(1) with a singlet: redeclare `Phi` with the rotation, write the U(1)_X covariant terms for `Phi` and the singlet, use `LSM - LHiggs`". INF gain: 10 to 31 of 38 matched, F1 about 0.87. High confidence; the opt arm and the shell B-L-SM run already did this.

## Monotops (metric 0.429; 6 of 14 matched, 14 delivered)

| Sector | Ref | Shell matched | Missing | Extra |
|---|---|---|---|---|
| F1, F2 vector currents | 5 | 5 | 0 | 0 |
| Y1 coloured scalar + q q | 5 | 1 | 4 | 4 |
| Y3 coloured scalar + chi + q | 4 | 0 | 4 | 4 |

- **Q4. The reference is wrong (OBS).** `monotops.fr:40,43`: `S[5] == { ClassName->phiC, ..., Indices->{Colour}, ...}` without `Index[...]`; the vector at line 32 has `Indices->{Index[Colour]}`. The reference UFO has `phic ... color = 1` and yet `V_56 ... particles = [ P.d, P.b, P.phic ], color = [ 'Epsilon(1,2,3)' ]`. The paper: "\epsilon^{ijk} \varphi_i \bar d^c_j ... i,j,k are color indices in the fundamental representation" (tex:191-207). The delivered colour 3 is right.
- With the reference scalars relabelled colour 3, the shell arm scores F1 1.0 (14/14). `cc_vanilla_v2` gets recall 1.0 and precision 0.34: its extras are gluon, photon and Z couplings of the coloured states, which are correct physics that the reference has no kinetic terms for.
- **Q7.** No harness change. Fix the reference (or key the colour on the vertex colour structure). Sure.

## pSPSS (metric 0.667 in s1; chain FAIL in s2)

| Sector | Ref | Shell s1 | Note |
|---|---|---|---|
| F3 W l n, Z nu n | 2 | 2 | |
| F3 Z n n | 1 | 0 | second order in theta |
| Y2 h nu n | 0 | 1 (extra) | reference UFO has no Higgs vertex with n4, n5 |

- **Q2/Q3. In the paper; class (d) (OBS).** "The mixing is implemented using Eq. (neutrino rotation) by replacing the neutrino \nu (`vl`) with the transformed neutrino (`UnCL nL`)" (tex:792), "up to second order in \vec\theta". The shell models write first-order mass-basis currents by hand and leave `vl` unrotated, so Z n n is absent. The cover arm added the term by hand and scored 0.857.
- **Q4 (OBS).** The extra `h nu n` is in the paper's Lagrangian (Yukawa of the sterile neutrinos with H and the lepton doublet, tex:226). The reference UFO lacks it; cause not confirmed. Ceiling for a faithful model: 0.857.
- **Q6 (OBS).** s2 call 1 used the gauge basis and failed `mass_diagonal` (lint: "class `N1L` is defined as a mixture of ['n4', 'n5']; the mass basis of the partner fields declared in SM.fr is unchanged"). The agent moved to a multi-member Majorana class with a mixing-matrix parameter and wrote `LnCC` as `-(gw/Sqrt[2]) nH.VlN.Ga[lmu].ProjP.l W[lmu]`: an unbarred Majorana field at the head of the chain. `HC[]` of it gives `PRIVATE`OperatorChain[ebar[...], n4[...]]` and `Ga[0, ...]` in the output; hermiticity fails and `couplings.py` has a Python syntax error (calls 5, 7, 9, 10). Calls 2, 3, 4, 6 each ran to the 1350 s timeout after a load error (`SetDelayed::write: Tag List in {Q, GhostNumber, LeptonNumber, Y}[_] is Protected`). s1 wrote `gCC4e ebar.Ga[mu].ProjM.n4 Wbar[mu]` with scalar couplings and passed. That the unbarred field is the trigger is INF; the agent blames the FeynRules/Wolfram 15 patch.
- **Q7.** A lint for an unbarred fermion at the head of a chain, plus fail-fast on a load error. Gain: s2 0 to 0.667. A neutrino-rotation recipe adds Z n n: 0.667 to 0.857. Medium confidence on the lint, high on the rotation.

## B-L-SM (metric 0.727; recall 0.87, precision 0.625)

| Sector | Ref | Shell matched | Missing | Extra |
|---|---|---|---|---|
| D1, D2, D3 scalar-gauge | 6 | 6 | 0 | 5 |
| P potential | 2 | 2 | 0 | 5 |
| F1, F2, F3 currents | 9 | 7 | Z' N nu; Z N N | 0 |
| Y1, Y2, Y3 Yukawas | 6 | 5 | H nu nu | 2 |

- **Q4. All 12 extras are a metric artefact (OBS).** The reference declares the SM-like Higgs as `H1` with PDG 9900025, so it has the same key as `H2`. Every extra contains `sm:25`. With the delivered `sm:25` mapped to that key: precision 1.0, recall 0.87, F1 0.93 (shell s1, s2, opt alike).
- **Q2/Q3. The 3 missing kinds; class (d) (OBS).** They are second-order effects of the heavy-light neutrino rotation. The paper gives the rotation (tex:145-161) and fixes `V_{lN}`. `LMixing` has only first-order W, Z, h currents: "`V_lN` diagonal, per the paper's seesaw-mass-basis route".
- **Q7.** A full neutrino rotation (redeclare the lepton doublet through the mixing matrix). Gain 0.727 to 0.79 on the current metric, 0.93 to 1.0 after the label fix. High confidence on the cause.

## Wprime (metric 0.80; recall 1.0, precision 0.667)

- **Q4 (OBS).** Extras: `W' nu_R l` (two charge signs). The paper: "right-handed W'_R bosons in which the decay into a right-handed neutrino \nu_R is kinematically allowed" (tex:107), and `m_{\nu_R}` is a parameter of its results. The reference writes `gR/Sqrt[2]*(vlbar.Ga[mu].ProjP.CRl.l + ...)*Wp[mu]` with the SM `vl` (`weff.fr:115`) and has no `nu_R`. The delivered model is closer to the paper.
- **Q7.** No harness change. A faithful model cannot score above 0.80.

## Cross-paper ranking

Gain is on the current metric, shell arm, per paper; divide by 13 for the mean. All gains are INF from the sector counts.

| # | Capability | Papers | Estimated metric gain | Confidence | Evidence |
|---|---|---|---|---|---|
| 1 | Recipe: gauge the new U(1) on `Phi` and the singlet, redeclare `Phi` with the h-H2 rotation, `LSM - LHiggs` | GeneralU1 | 0.40 to about 0.87 (+0.47; mean +0.036) | High | Opt arm gets these 21 kinds with that construct; shell B-L-SM already does it |
| 2 | Validate budget for large models: timeout above 1609 s, UFO export before slow checks, fail fast on a load error, no lock wait | ALRM, pSPSS s2 (4 calls lost), needed by #3 | ALRM 0 to about 0.4 (mean +0.03) | Medium | 4 timeouts at 1350 s; reference export 1609 s; 3443 s lock wait |
| 3 | Task format: allow `M$GaugeGroups` in the add-on, or a standalone model, with a recipe for an extended electroweak group | 331, ALRM | 331 +0.15 to +0.27 (ceiling 0.42); ALRM up to +0.3 above #2 (mean +0.03 to +0.045) | Medium-low | Agent quotes the rule as its reason; vanilla_v2 added `SU2R` and got 10 G kinds; 130 of 186 kinds of 331 are in G, D1, D2, D3, P |
| 4 | Neutrino rotation to all orders (tool or recipe that redeclares `vl`/`LL` through the mixing matrix) | pSPSS, B-L-SM, GeneralU1 | +0.19, +0.06, +0.04 (mean +0.022) | High on cause | Missing kinds are Z n n, Z' N nu, H nu nu, Z N N; cover arm got Z n n by hand |
| 5 | Lint: unbarred fermion at the head of a chain | pSPSS | s2 0 to 0.667 (variance only) | Medium | `nH.VlN.Ga[lmu].ProjP.l` and the `OperatorChain` residue |
| 6 | Gate: each paper Lagrangian term must give at least one UFO vertex | GeneralU1 opt, 331 | No gain on this metric; stops a model with no Z' f f from passing | High | Opt UFO has 0 Z'-fermion vertices and scores 0.81 |

## Score that no harness change can recover

| Paper | Shell metric | Ceiling for a paper-faithful model | Lost (per paper) | Cause |
|---|---|---|---|---|
| 331 | 0.152 | 0.42 | 0.58 | Reference charges are symbolic in beta: 98 of 174 kinds have `q=None` (metric) |
| Monotops | 0.429 | 0.43 | 0.57 | `Indices->{Colour}` typo in the reference: scalars get colour 1 (reference bug) |
| B-L-SM | 0.727 | 0.79 | 0.21 | Reference Higgs has PDG 9900025: 12 false extras (metric) |
| Wprime | 0.80 | 0.80 | 0.20 | Paper has `nu_R`, reference does not (reference below paper) |
| pSPSS | 0.667 | 0.857 | 0.14 | Paper has h nu n, reference UFO does not |
| GeneralU1 | 0.40 | about 0.93 | about 0.07 | Z'WW (4 kinds) needs Z-Z' mixing that the paper does not give; `Zp nu nu` counts as an extra because reference neutrinos have PDG 1200/1400/1600. The ceiling assumes the agent adds the h-Phi mixing (9 kinds, H2 + WW/ZZ/ff) that the paper calls negligible, as the opt arm did; a strictly paper-faithful model stops near 0.75 |
| ALRM_general | 0.0 | not known | not known | No label artefact found. Reference adds `LagHEffective` and takes 1609 s to export |

Sum of the lost column: about 1.77, or 0.14 of the 13-paper mean. The shell arm's 0.69 has a ceiling near 0.86 on this metric before ALRM.
Fixing the metric alone (evaluate symbolic charges, map the reference Higgs to 25, correct the Monotops colour) moves the shell arm with no new run: 331 0.152 to 0.424, B-L-SM 0.727 to 0.93, Monotops 0.429 to 1.0 (OBS, mean +0.08).

## Not confirmed

- Why `LZpFerm` is absent from the GeneralU1 opt UFO. Check: load the model and run `FeynmanRules[LZpFerm]`.
- That the unbarred Majorana field is the cause of the pSPSS s2 failure. Check: compile s2 with `nHbar` in `LnCC`.
- Why the pSPSS reference UFO has no h nu n vertex.
- How many kinds the ALRM shell model yields. Check: export its UFO with `Checks=false` and a longer timeout.
- The 331 beta choice: the reference leaves beta free, so each of the paper's four benchmarks is valid. I scored at the agent's own beta.
