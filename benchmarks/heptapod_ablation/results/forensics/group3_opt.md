# cc_sonnet_opt (group 3): forensics of the new checks (16 papers, 2026-10-07)

Read-only analysis. No kernel, MadGraph or agent was run. `N/<paper>` = `/home/deck/code/ALE-ablation/benchmarks/heptapod_ablation/runs/<paper>/rerun/cc_sonnet_opt/s1`. `O/<paper>` = `/home/deck/code/heptapod/eval/benchmark_runs/<paper>/rerun/cc_sonnet_harness/s1`. `cK` = `validation/call<K>`. Tags: **[OBS]** = read from a file, **[INF]** = my inference, not tested by a run. Scratch scripts: `/tmp/claude-forensics/scratch/` (`a.py`, `a2.py`, `nl.py`, `pwv.py`).

## Finding 0 (read this first): a statement that continues on the next line is cut at the line end

This is not one of the new checks. It is the largest silent defect in group 3, and no check names it.

- **Mechanism [INF].** Mathematica reads a `.fr` file one expression at a time. A top-level expression that is complete at the end of a line stops there. A next line that starts with `+` or `-` is a separate expression with no effect. Inside `Block[...]` or `(...)` the bracket is open, so the statement continues correctly.
- **Direct evidence [OBS].** `N/ALRM_general/c10/model.fr:284-289` writes `LHp2 :=` on 6 lines. `c10/round0/compile.log:78` shows `HEPTAPOD-HERMBLOCK|block=LHp2|contents=cbar dp2 Hp2;dp3 Hp2 tbar;dp1 Hp2 ubar`: only line 1. Line 75 `block=LA2|contents=A2 n1 n1bar;A2 n2 n2bar;A2 n3 n3bar`: the `dp` half (line 273) is absent.
- **Runs with this defect [OBS, `nl.py` over all snapshots]:**

| run | statement | what is lost | UFO evidence |
|---|---|---|---|
| N/331 (pass) | `model.fr:870-880` `LHchghalf :=` + 9 lines; `:819-820` `LFkin` | 8 of 9 charged-scalar Yukawa lines; the `EH` mass term | `HP`, `HQV` have photon vertices only; no `HEPTAPOD-MASS` row for `Ee/Emu/Etau` (`Dh/Sh/Th` have rows) |
| N/GeneralU1 (pass) | `:348-349` `LTotal := ... + LPhiXPot` / `+ LZpKin + LZpFerm + LZpPhiX + LNkin + LNYukT + LNuYukT;` | all 6 terms of line 2: Z' kinetic and mass, **all Z'-fermion couplings**, all N terms | no `f f Zp` vertex; no mass row for `Zp`; `terms=441` in c3-c10 for 8 different N sectors |
| N/Monotops (pass) | `:331-332` `LTotal := LSM + <6 kinetic terms>` / `+ LFCS + LFCV + ...;` | **all 8 interaction terms** of the paper | `phiS, VecV, chiF, XV` in no vertex |
| N/SMWeinberg (pass) | `:152-153` `LTotal := ... + LNhvGp` / `+ LNhvG0G0 + LNhvG0Gp + LNhvGpGp;` | 3 Goldstone terms | no `Nhv ve G0 G0`, `Nhv e G0 G+`, `G+ G+ l l` vertex |
| N/ALRM_general (fail) | `:272-273` `LA2`, `:284-289` `LHp2` | hermitian partners | this is the hermiticity failure (section C) |
| O/pSPSS (earlier group) | `c10/model.fr:240-243` `LTotal := LSM + LNkin` / `+ LNcc4 ...` | all N interactions | explains the earlier report's "why the terms evaluate to nothing at c10: not determined" (c9 has `LTotal` on one line and fails) |
| O/Monotops (earlier group) | `c6/model.fr:370` `LTotal := LSM` / `+ LkinPhi ...` | everything | 163 vertices, `terms=490`: the earlier "pass at call 6" is SM only |

- **Effect.** 4 of the 13 chain passes have a UFO that lacks paper terms. The harness term resolver reads to the `;` (`summary.json` `"roots": ["LTotal"], "ambiguous": false`), so it disagrees with the kernel. The referee reads the text and is blind to it (section E).
- **Fix candidates.** A lint rule: top-level line complete (brackets closed, no trailing operator, no `;`) and the next non-blank line starts with `+ - * /`. Or wrap every `:=` body in parentheses. Or compare `HERMBLOCK` contents with the text.

## A. How often each new check fired, and was it then fixed

Script `a.py` (stream tool results) and `a2.py` (`agent_report.md` + `summary.json`). "Fixed" = absent in a later result of the same type.

| check | runs fired (of 16) | then gone | per paper |
|---|---|---|---|
| lint `partial_index_fermion` | 3 | 3 | GeneralU1 (lint 2, `LLbar[sp,ii]`, `NR[sp]`), HeavyN (lint 1, `vl[ff]`), NJLComposite (lint 1, `FNDbar[ii]`). All before the first validate call. |
| lint `class_outside_list` | 0 | - | never fired |
| lint `duplicate_mass_parameter` | 0 | - | never fired |
| lint `shared_lha_block` | 0 | - | never fired (Monotops gave each tensor its own block at c1) |
| lint `nonpositive_order` | 6 | 6 | GeneralU1 `vPhi`, MDMmodel `fD`, NJLComposite `Lam`, pNG `vs`, SMWeinberg `Lam` (all: line deleted before c1); HeavyN `aEWM1` at c5 (false alarm, see F4) |
| report "no vertex" | 7 | 4 | fixed: 331 (c7 `Y` -> renamed `Yg`, c8), HeavyN (c1-c2 `NN` -> c3), NJLComposite (c1 `FNs` -> c2, by an invented coupling, F3), EffLRSM (c3, a 43-line probe file only). Not fixed: GeneralU1 (9 calls), Monotops (8 calls), ALRM_general (c1 real; c4-c10 false alarm, F1) |
| report "mass rows" | 1 | 1 | B-L-SM c2-c3 (`NR | 4200. | 1400.`) -> split into 3 classes -> pass at c4. The ghost-only hint never fired. |
| report "UFO parameters twice" | 3 | 3 | 331 c5 (`Zer`), HeavyN c5 (`aEWM1, cabi`), Monotops c1-c9 (gone at c10 by removal of all External parameters, F2) |

[OBS] examples. HeavyN lint 1: `partial_index_fermion (line 65): \`vl[ff]\` gives 1 of the 2 indices of \`vl\``; agent: `"I'll use the index-free class members ve, vm, vt and e, mu, ta instead"`. 331 c7: agent: `"the particle Y has no vertex ... Y is FeynRules' hypercharge symbol ... I'll rena[me]"`; c8 is a full pass. This 331 fix is the clearest gain: the earlier harness accepts c7.

## B. 331, GeneralU1, SMWeinberg, pSPSS: what made the difference

In all four the agent wrote the file differently from the start. No new lint rule or report section fired on the earlier root cause. The prompt section is the probable reason [INF]; the agent's thinking text is empty in the stream, so there is no direct quote.

- **331.** [OBS] No `Phi` redeclaration and no scalar potential: the model is a transcription of the coupling tables (`agent text: "Scope and choices ... Benchmark β = −1/√3"`). So there is no ghost-mass row and no mass in `M$Parameters`. `duplicate_mass_parameter` fired 0 times. The c5 "UFO parameters twice: Zer" came from the agent's own global replace `-> 0` to `-> Zer` and was fixed at c6-c7. The new "no vertex" section caught `Y` at c7 (above). Cost: the referee lists 5 omitted sectors, and Finding 0 removes 8 Yukawa lines.
- **GeneralU1.** [OBS] `c1/model.fr:35` `S[11] == {` is inside the class list (5 `Doubly defined particle classes` warnings in `compile.log`). `class_outside_list` fired 0 times. [OBS] c1 kinetic_diagonal failed on a different error (`1/2 del[PhiX] del[PhiX]`), which the agent fixed at c3 from the report text. `FeynmanGauge = False;` is at line 16 from the start, as the prompt says.
- **SMWeinberg.** [OBS] `c1/model.fr` uses all indices: `Nhvbar[sp1] Ga[mu, sp1, sp2] ProjM[sp2, sp3] l[sp3, ff]` with `+ HC[...]`. `partial_index_fermion` fired 0 times. c1 failed on `bar[CC[l[sp1,ff]]]` (mass_diagonal + MadGraph); the agent used the Majorana identity; pass at c2.
- **pSPSS.** [OBS] Matrix form from the start: `nNbar.UNZ.Ga[mu].ProjM.nN`, `lbar.dUW.Ga[mu].ProjM.vl`; `LTotal` on one line. c1 hermiticity failed on bare matrix bilinears; the report was enough (`1/2 (X + HC[X])`); pass at c2. The UFO has n4/n5 vertices (`particles_without_vertex: []`).

## C. The three chain failures

**ALRM_general (hermiticity, 10 of 10 calls).**
- Root cause [OBS]: Finding 0. `LHp2` and `LA2` lose their conjugate half. Final rows: `fields=ubar,dp1,Hp2 | expr=I*yu1*...ProjM` and `fields=dp1bar,u,Hp2bar | expr=(-I)*yu1*...ProjP` (`c10/round0/compile.log:37-42`).
- Report: named the block (`vertex 1: fields cbar dp2 Hp2; block: LHp2`) with the generic text "a term without its `+ HC[...]` partner". It did not say that the block holds 3 of its 18 terms.
- Agent: 7 different theories (c3-c10): gamma5 form, member-by-member, `Conjugate[Ynm]` matrices, numeric matrices, `P_L = 1 - P_R`, scalar couplings, explicit partners. All kept the multi-line form. c10 text: `"I can't say which feature of these matrices the checker is rejecting"`.
- Stop: budget used (10/10). One call (c2) lost to the MCP 1800 s idle timeout. Also [OBS] c1-c7 MadGraph failed on `'1' order` until `NZp` got `{NP,1}` at c8.

**MDMmodel (mass_diagonal fail, mass_spectrum inconclusive, MadGraph fail; 3 calls).**
- Root cause [OBS]: the paper's portal term mixes t and T. `c3/round0/compile.log:92` `Non diagonal mass term found: -((vev*yp*ProjP[...]*tbar[...]*tp[...])/Sqrt[2])`. The file has no rotation of the top sector. MadGraph: `InvalidModel('Odd number of fermion in vertex: [-4, 9000025, 251]')`; cause not determined (candidate [INF]: `tpRbar[sp,cc] QL[sp,ii,3,cc]` at `model.fr:218`, a spinor product without a `.` chain).
- Report: named the term exactly. No new check fired after lint 1 (`nonpositive_order` on `fD`, fixed before c1; this was the earlier group's 8-call problem).
- What happened [OBS `stop_gate_log.jsonl`]: 4 Stop events in 40 s (t=...451, 483, 487, 491). `continuations_before` 0, 1, 2 -> `decision: block`; 3 -> `decision: allow`, `why: "continuation limit reached (3)"`. `validations: 3` in all four, so the agent made **no tool call** between the blocks. It refused each time: `"I'm stopping here rather than making the chain pass by changing the physics"`, `"Nothing has changed since call 3, so validating again would return the same report"`, `"What I need from you. Choose one: 1. Redesign the up-type sector..."`. It did **not** delete physics. 7 validate calls and 1 review were left.
- Compare: O/MDMmodel passed, but without the t-T term (earlier report: "the paper's Eq. 15-16 correction is not in the scored model"). The group-3 failure is the more honest file. The missing piece is permission and a recipe to redeclare generation 3 of `uq`/`QL`/`uR`, not a check.

**SLQrules (compile timeout).**
- c1-c4 [OBS]: `Part::partw: Part 3 of {0, 1} does not exist` + recursion limit (198-208 s). Cause: SU(2) index in the last slot of `PauliSigma`. The report showed the log lines only. The agent found it at c5 by reading SM.fr. c3 was lost to `no_lagrangian_symbol` (`LTotal := LSM` probe).
- c5, c6, c8 [OBS]: `compile_timeout`, 1350.1 s, after `hermiticity: pass, kinetic_diagonal: pass`. c7 (Yukawa, triple and quartic blocks removed): 185 s, `mass_diagonal` fails on the paper's vev mixings (`lR2R2t*vev^2*R2cbar*R2tu`), MadGraph imports.
- Final root cause: (1) the full gauge-basis Lagrangian needs more than the 1350 s limit; (2) behind it, the leptoquark mass mixing has no rotation. Report: "TIMED OUT ... may need simplification"; no time per block.
- Stop [OBS]: 3 gate blocks, then `continuation limit reached (3)`. After block 2 the agent edited two blocks, saw the edit was wrong, and reverted (`"byte-for-byte the file that gave the call-8 timeout"`). 2 calls left. No new check fired in this run.

## D. GeneralU1 and Monotops: new particles with no vertex

| | GeneralU1 | Monotops |
|---|---|---|
| particles [OBS] | `n1, n2, n3` (c1, c3-c10, scored UFO) | `VecV, XV, chiF, phiS` (c1, c2, c5, c8-c10, scored UFO) |
| terms that hold them | `LZpFerm` (`xNR NNbar.Ga[mu].ProjP.NN`), `LNYukT`, `LNuYukT` | `LFCS`, `LFCV`, `LvphiChi`, `LvphitChi`, `LXDq`, `LXChi` |
| why they vanish | Finding 0: all are on line 2 of `LTotal` (`:348-349`). Also lost: every Z'-fermion coupling and the Z' mass. | Finding 0: all interaction terms are on line 2 (`:331-332`). `vphi`, `vphit` have vertices only from `DC` in their kinetic terms. |
| proof inside the run [OBS] | `terms=441`, `134 possible non-zero vertices`, `107 vertices obtained` are the same in c3, c5, c9, c10 | at c7 the agent moved `LFCS + LFCV` to line 1 (`LTotal := LSM + ... + LXKin + LFCS + LFCV` / `+ 0 (...)`) and `phiS`, `VecV` got vertices; c8 put them back on line 2 and they vanished |
| what the agent tried | c4 three non-indexed Majorana classes; c5 Yukawa only; c6 chiral form; c7 restore; c9 Dirac classes; c10 `PropagatorArrow -> Forward`. Final: `"every term that contains an n field is dropped"` | c2 `ExpandIndices`; c4 probe file; c6-c7 `0*(...)` bisect; c8 Internal tensors; c9 External scalars; c10 numbers in Internal values |
| `partial_index_fermion` on them | fired once before c1 on `LLbar[sp,ii].yNu.NR[sp]` (a form the agent wrote because the older rule `explicit_flavour_sum` asked for it). Not the cause. | never fired |
| report hint | "The usual cause is a field written with a partial index list ... or an index that does not match the class": wrong for both | same |

GeneralU1 passed the chain at c3 and spent 7 more calls on this. Monotops had a second defect in the same calls (F2).

## E. Fresh referee on the chain passes

[OBS] `post_review/verdict.json`: **10** of the 13 passes have at least one physics-changing item (not 9): 331 (7), NJLComposite (6), ChernSimonsPortal (3), EffLRSM (2), GeneralU1 (2), Monotops (2), Wprime (2), B-L-SM (1), pNG (1), SMWeinberg (1). Zero: HeavyN, pSPSS, Top-Philic-Zprime. 27 items in total.

Classes: (1) real departure that changes predictions; (2) dropped, weakened or invented to pass a check; (3) input value, convention, scope, paper-internal conflict, or referee reasoning error; (4) cannot tell.

| paper | (1) | (2) | (3) | (4) | items |
|---|---|---|---|---|---|
| 331 | 5 | 0 | 2 | 0 | (1) gauge self-couplings, gauge-scalar vertices, scalar potential, neutral-scalar SM Yukawas, h/H2-E-E omitted. (3) charge of V (paper table and paper vertices disagree), one beta benchmark. |
| NJLComposite | 4 | 1 | 1 | 0 | (1) Pi0u outside its doublet, Pi0u without covariant derivative, composites without SM partner chirality, anomaly vertices absent. (2) singlet coupling invented after the "no vertex" report (F3). (3) `gY` value: the paper's two statements conflict. |
| ChernSimonsPortal | 1 | 0 | 2 | 0 | (1) Re part of the c1 current dropped (no h-X-Z, h-X-gamma). (3) c2 Hermitian completion (referee: "itself ambiguous"); c2 neutral couplings (referee: "the discrepancy lies in the paper's Eqs. (40)-(41)"). |
| EffLRSM | 0 | 0 | 2 | 0 | (3) `MT` 172 vs 173.3 (SM.fr default, 0.1 %); N1 width fixed at the kappa = 1 value (no effect at the benchmark). |
| GeneralU1 | 1 | 0 | 1 | 0 | (1) Dirac Yukawa `LLbar[ii] Phi[ii]` gives an e-N term, not nu-N. (3) Majorana Yukawa factor 2: paper line 172 conflicts with its Eq. LYk. |
| Monotops | 0 | 0 | 2 | 0 | (3) default values are those of one of the paper's two scenarios (tilde couplings 0; `Mvphi` 500, `Mchi` 50). |
| Wprime | 0 | 0 | 2 | 0 | (3) `MT` 172 vs 175 (SM.fr default); NLO QCD not in an LO UFO (scope). |
| B-L-SM | 0 | 1 | 0 | 0 | (2) `LNuYuk` has `(ca H + sa H2)` without `vev`: no Dirac mass. [INF] written so at c1 to keep `mass_diagonal` clean; mixing is put in the W/Z currents by hand. |
| pNG | 0 | 0 | 1 | 0 | (3) `Width -> 0` for H2; the paper gives no number. |
| SMWeinberg | 0 | 0 | 1 | 0 | (3) referee doubts that `bar[CC[l]].ProjM.KLL.l` contracts the generation indices; it says itself "if the toolchain resolves it ... equivalent". [INF] The matrix form does contract them. |
| **total** | **11** | **2** | **14** | **0** | 27 |

Spot-checks against the paper (8, all confirm the referee's citation) [OBS]: B-L-SM tex 129 `- y_{ij}^\nu \overline{L_i}\nu_{Rj}\tilde{H}`; ChernSimons tex 1383-1384 `allows interaction of the $X$ boson with $\gamma H$ and $ZH$, which are generically small`; GeneralU1 tex 136 `\overline{\ell_L^\alpha} H N_R^\beta` and 163 `\begin{pmatrix} v+h\\0` (upper-component vev, so the SM.fr contraction needs the conjugate doublet); 331 tex 684 `$V$ & ... & $-1$`; NJL tex 546 `$\Pi_{-1/2}=(\Pi^0_u,\Pi^-)$`; EffLRSM tex 419 `m_{N_1}=m_t=173.3\GeV`; Wprime tex 356 `we use $m_t=175\pm 5$ GeV`; Monotops tex 284-286.

Weight of the "referee-clean" metric:
1. **About half of the physics-changing items (14 of 27) are not model errors.** Seven papers have only class-3 items, or class 3 plus one. A count of "0 physics-changing" is too strict as a pass line; SM.fr default inputs alone fail EffLRSM and Wprime.
2. **The referee cannot see what the kernel drops.** [OBS] 331 review: "Verified to match ... the H⁺ν̄ℓ, H⁺ūd, H⁺t̄b ... Yukawas (2286–2334 vs 870–880)": those lines are not in the UFO. GeneralU1 review: "Z′–fermion Lagrangian (model lines 295–303) vs Eq. Lag1 ... matching": absent from the UFO. Monotops review: "all eight paper terms are present": none is in the UFO. SMWeinberg: the one disputed term is not in the UFO at all.
3. The class-1 items are real and concentrated: 331 (5) and NJLComposite (4) are partial models. Use the referee as a list of omissions, not as a clean/not-clean bit, and pair it with a UFO-level term check.

## F. Defects and side effects of the new checks

1. **"No vertex" false alarm for a custom antiparticle name [OBS].** `opt_checks.py:140-141` tests `n` and `n + "__tilde__"` only. ALRM declares `AntiParticleName "Hp2m"`; the UFO has `particles = [ P.dp1bar, P.u, P.Hp2m ]`. `pwv.py` (uses the `X = Y.anti()` lines): c4 (`Hp1, Hp2, phi10`), c5-c10 and the scored UFO (`Hp2`) are all false. 8 of ALRM's 9 firings. With hermiticity fixed, this would have blocked the pass.
2. **"UFO parameters twice": wrong cause text and a cut list (Monotops) [OBS].** `c1/model.fr` has 16 different `BlockName`s (as the prompt asks), yet `parameters.py` writes all 99 new External entries twice (second copy from index 113; `a0FC1x3` at lines 140 and 932). At c9 a plain scalar with `BlockName -> MONO_AF0, OrderBlock -> 1` is also written twice, identical. So neither named cause applies. Real cause: not determined. Candidate [INF]: the underscore in `BlockName -> MONO_A0FC` (a Mathematica pattern); Monotops is the only run with one, and O/Monotops passed with `MTOP01`. The section prints `dup[:20]` with no "and N more"; the agent read the cut list as the full list: `"exactly the parameters used in those dropped terms"` (c1), `"The duplicates have moved rather than gone"` (c8). Cost: 7 calls; end state at c10 has 0 External parameters (benchmark numbers fixed in Internal values).
3. **"No vertex" made the agent invent a term (NJLComposite) [OBS].** c1 text: `"FNs has no vertex. The paper gives no operator for the neutral singlet ... I'll couple it through the composite construction"`. Fresh referee item 4: "Singlet coupling added without a paper equation, with the wrong chirality." The section says "Fix the terms until every new particle has a vertex"; a gauge singlet with only kinetic and mass terms is legal. It also fires on probe files (EffLRSM c3).
4. **`nonpositive_order` fires on SM.fr's own parameter [OBS].** HeavyN lint 6: `` `aEWM1` has InteractionOrder {QED, -2} `` after the agent redeclared it. The agent ignored it correctly. In the same call the "twice" section named `aEWM1, cabi` with the two unrelated causes; the real cause was the older rule `sm_parameter_redeclared`.
5. **"No vertex" hint points away from the real cause** (section D): GeneralU1 7 calls, Monotops shares 7 calls with item 2. The hint must list Finding 0 first.
6. **Rule conflict [OBS].** GeneralU1: `explicit_flavour_sum` made the agent write `LLbar[sp,ii].yNu.NR[sp]`; `partial_index_fermion` then rejected it; the file went back and keeps the first finding to the end. Two lint calls, no validate call.
7. **`partial_index_fermion` needs a `.` within 2 characters** (`opt_checks.py:76-77`), so `kN[ff] ... l[ff]` in a product is not seen [INF from code; no such case in group 3].
8. **Three rules never fired** (`class_outside_list`, `duplicate_mass_parameter`, `shared_lha_block`). Group 3 gives no evidence for or against their code. The prompt text did the work.
9. Not from the new checks, but budget lost in group 3 [OBS]: 4 validate calls died on `sent no response or progress for 1800s` (331, ALRM, B-L-SM, ChernSimonsPortal; `331/c1 lock_wait_seconds: 1183.8`), and 3 bisect calls were rejected as `no_lagrangian_symbol` (GeneralU1 c2, Monotops c3, SLQrules c3).

## Summary table

| paper | group-3 result (calls) | what changed vs the earlier group | remaining defect |
|---|---|---|---|
| 331 | pass (9) | was mass_spectrum + MadGraph fail. Different design from c1 (coupling tables, no `Phi` override). "No vertex" caught field `Y` at c7. | Finding 0: 8 Yukawa lines and the `EH` mass are not in the UFO. Referee: 5 sectors omitted. |
| ALRM_general | fail: hermiticity (10) | was no model (64k output cap). Now a full file. | Finding 0 on `LHp2`, `LA2`. `Hp2` "no vertex" is a false alarm (F1). |
| B-L-SM | pass (4) | pass before. "Mass rows" named `NR 4200 vs 1400`. | No Dirac mass (`vev` left out of `LNuYuk`). |
| ChernSimonsPortal | pass (5) | pass before. 2 compile timeouts, 1 idle timeout. | h-X-Z / h-X-gamma part of the c1 current dropped. |
| EffLRSM | pass (8) | pass before (3 calls). 4 compile aborts (`LoadModel::Mass`). | Input values only. |
| GeneralU1 | pass, 3 particles without vertex (10) | was kinetic_diagonal fail. `Phi` inside the list and `FeynmanGauge = False` from c1 (prompt). | Finding 0: no Z'-fermion coupling, no Z' mass, no N term in the UFO. Dirac Yukawa uses the wrong doublet component. |
| HeavyN | pass (6) | pass before (1 call). `partial_index_fermion` fixed `vl[ff]` before c1; "no vertex" fixed `NN` at c3. | None found (referee 0). |
| MDMmodel | fail: mass_diagonal + MadGraph (3) | was pass without the t-T term. `nonpositive_order` fixed `fD` before c1. Agent kept the paper term and refused to continue. | No rotation of the top sector; 7 calls not used. |
| Monotops | pass, 4 particles without vertex (10) | was pass with `LTotal := LSM` only (vacuous). | Finding 0: no interaction term in the UFO. All parameters Internal (F2). |
| NJLComposite | pass (4) | was pass at call 10 with one generation. `partial_index_fermion` + `nonpositive_order` fixed before c1. | Referee: 4 real departures; 1 invented coupling (F3). |
| pNG | pass (1) | pass before. `nonpositive_order` fixed `vs` before c1. | Widths only. |
| pSPSS | pass (3) | was a vacuous pass (Finding 0 in the earlier file). Matrix form from c1. | None found (fresh referee 0; in-loop review 2 disputes the H-N-N term). |
| SLQrules | fail: compile timeout (8) | was a compile crash. Crash cause found by the agent (c5). | Compile > 1350 s; behind it unrotated mass mixing. 2 calls not used. |
| SMWeinberg | pass (2) | was hermiticity fail x10. All indices given from c1. | Finding 0: 3 Goldstone terms not in the UFO. |
| Top-Philic-Zprime | pass (2) | pass before. | None found (referee 0). |
| Wprime | pass (4) | pass before. | Input value (`MT`) and LO scope only. |

Bottom line: the prompt section, not the lint rules, removed the earlier root causes (3 rules never fired). The two report sections that fired often ("no vertex", "parameters twice") found real defects but gave wrong causes, and one has a false-alarm bug. Of the 13 chain passes, 4 lack paper terms in the UFO because of Finding 0, and the referee does not see it. Passes with no defect found at UFO level and no class-1/2 referee item: EffLRSM, HeavyN, pNG, pSPSS, Top-Philic-Zprime, Wprime (6 of 16).
