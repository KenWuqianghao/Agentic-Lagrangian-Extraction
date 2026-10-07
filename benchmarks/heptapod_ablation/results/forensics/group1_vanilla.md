# Vanilla arm (`cc_vanilla`, s1): forensics of the 9 failed papers

Sources per paper: `runs/<paper>/rerun/cc_vanilla/s1/` (`VALIDATION_REPORT_final.md` = VR, `model/<paper>_gen.fr` = FR, `agent_stream.jsonl` = AS, `agent_out.md` = AO, `run.json`).
`[n]` = event index in my extract of AS (`/tmp/claude-forensics/x/<paper>.txt`). OBSERVED = quoted from a file. INFERRED = my conclusion.
Classes: (a) self-test gap, (b) known failure, (c) interface, (d) resource.

## Three causes that explain most failures

1. **The scorer adds `LSM` when `LTotal` does not name `LSM`.** OBSERVED, `benchmarks/validation_benchmark.py:318`: `return lag if "LSM" in reached else f"LSM + {lag}"`. The prompt says only "Define the total Lagrangian as LTotal" and "checks pass on LTotal". Five failed models build `LTotal` from SM pieces (`LGauge`, `LFermions`, ...) or a full replacement, without the symbol `LSM`. The scorer then counts the SM two times. All 7 passes write `LTotal := LSM + ...`. Affected: 331, ALRM_general, B-L-SM, GeneralU1, MDMmodel.
2. **One Wolfram kernel for all runs.** The harness wrapper `.bin/wolframscript` takes a file lock (`run_vanilla.py`, WRAPPER: "One Wolfram kernel at a time on this machine"). Agents waited behind other runs. The agent's own `timeout N wolframscript` also counts the wait time.
3. **A headless session stops when the agent yields to wait.** In 8 of 9 failures the agent ended a turn with "I'll wait for the monitor". `run.json` shows 3 to 7 `result` events for these runs; all 7 passes and B-L-SM have 1. In 331, GeneralU1, Monotops, SLQrules the last stream events are `task_notification status=stopped`: the pending job was stopped and the agent never saw its result.

## 331 — compile_failed
1. OBSERVED VR: `[INFO] Lagrangian: LSM + LTotal`, then `Inner::incom: Length 2 of dimension 1 in {Generation, Colour} is incommensurate with length 1 ...` and `$RecursionLimit::reclim: Recursion depth of 2500 exceeded.` Direct construct INFERRED: `LEW` (FR 299-371) uses dot bilinears with a number for the generation and a free colour symbol, for example FR 354 `uRbar[1,cc].Ga[mu].uR[1,cc]`. Also FR 411 `LTotal := LGauge331 + LGluon + LGhostG + LDirac + LEW + ...` is a full replacement, and the scorer adds `LSM` to it. VR also shows `HEPTAPOD-RESIDUAL|count=12|fields=lR,uR,dR,QL1,...`.
2. Own last test, OBSERVED AS [120]: the same `Inner::incom` lines and `QN::NonConserv: Warning: non quantum number conserving vertex encountered!` in `CheckHermiticity[LTotal]`; [139] `All kinetic terms are diagonal.` / `All mass terms are diagonal.`; `CheckMassSpectrum` did not finish. AO: "Hermiticity: still shows the `Inner::incom` index error and `QN::NonConserv` warnings, which are open." Class **(b)**, with (d): the session stopped while the job ran. At [126] the agent judged the missing colour slot "fine" (INFERRED: wrong).
3. Ran: CheckHermiticity (errors), CheckDiagonalKineticTerms (pass), CheckDiagonalMassTerms (pass), CheckMassSpectrum (started, no result). WriteUFO script written, not run. No MadGraph. 15 wolframscript runs (most were pure Mathematica mass-matrix checks). Model load alone: "did not complete within its 600s timeout" [109].
4. A check tool that returns a verdict per check in bounded time, plus the rule "the scorer evaluates `LSM + LTotal` unless `LTotal` contains `LSM`".

## ALRM_general — compile_failed
1. OBSERVED VR: `[INFO] Lagrangian: LSM + LTotal` ... `Running consistency checks` ... `$RecursionLimit::reclim: Recursion depth of 2500 exceeded.` `TerminatedEvaluation[RecursionLimit]`. Construct in FR: not determined. FR 912 `LTotal := LGaugeALRM + LFermionsALRM + LHiggsALRM + LYukawaALRM + LEffALRM;` is a full replacement (FR 859 has its own gluon term), so `LSM` is added on top.
2. Own test, OBSERVED AS [139]: the same message in `CheckHermiticity[LTotal]`: `$RecursionLimit::reclim: Recursion depth of 2500 exceeded.` AO: "`model.fr` loads in FeynRules, but it is not finished. The UFO is not written" and "`WriteUFO` | Fails ... the UFO writer hits the unphysical triplet `WL` in some vertex". Class **(b)**: the agent knew, and the session ended at a wait.
3. Ran: CheckHermiticity (recursion error), CheckDiagonalKineticTerms (True), CheckDiagonalMassTerms (True), CheckMassSpectrum (partial table), WriteUFO (failed). No MadGraph. 24 wolframscript runs; only 2 were full FeynRules runs of the model, both in the last minutes.
4. An early compile of a small model (the agent spent about 2000 s on potential algebra before the first FeynRules load), and a pointer to the unexpanded `WL` vertex.

## B-L-SM — hermiticity + mass_spectrum fail
1. OBSERVED VR: `[INFO] Lagrangian: LSM + LTotal`; `HEPTAPOD-MASS|particle=t|derived=344.00000000000006|declared=172.|agrees=False`; `particle=W|derived=112.88869216082195|declared=79.82435974619784`. All SM masses are 2x, sqrt(2)x or 4x. Cause: FR 323 `LTotal = LGauge + LGaugeBL + LFermions + LFermionsBL + LGhost + LHiggsBL + LYukawaBL + LNeutrino + LNeutrinoMix;` reuses SM.fr pieces without the name `LSM`. Hermiticity fail (`60 possible non-zero vertices`): INFERRED same cause; exact term not determined.
2. Own last test, OBSERVED AS [166]: `HERM: {}`, `KIN: True`, `MASSDIAG: True`, `t numerical= 172.00000000000003 model-file=172.`; MadGraph `exit=0` [169]. AO: "FeynRules writes a UFO, the four checks pass on `LTotal`, and MadGraph imports the UFO". Class **(c)**. The agent did what the prompt said. The first draft was `LTotal = LSM - LHiggs - LYukawa + ...` [88]; that form names `LSM`, so the scorer would not add it again.
3. Ran all four checks, WriteUFO, MadGraph import (all pass on `LTotal`). 18 wolframscript runs.
4. One prompt line: "`LTotal` must include `LSM`; if it does not, the scorer adds `LSM`".

## GeneralU1 — mass_spectrum fail + MadGraph fail
1. Mass spectrum, OBSERVED VR: `Lagrangian: LSM + LTotal`; `particle=d|derived=0.020160000000000008|declared=0.00504`. Cause: FR 426 `LTotal := LGauge + LFermionsSM + LHiggs + LYukawaSM + LGhost + LU1X;`. MadGraph, OBSERVED VR: `InvalidModel: name MSphi define multiple time.` Cause: FR 89 `Mass -> {MSphi, 2000}` and FR 225 `MSphi == { ParameterType -> External, ...`.
2. Own last result was on an older version (`LTotal := LSM + LU1X`): [197] "Everything now passes." Then the agent found a real 3x error in d-type couplings ([173] "coefficient −3i·y_d/√2") and rebuilt the fermion sector without `LSM` [207]. That version was never tested: its run used `timeout 900` and died in the lock queue ([238] `run7.log` size 0). AO: "my run ... is waiting on the same lock. It hasn't started yet, so there are still no check results." Class **(d)** for the stop, **(c)** for the mass spectrum, **(a)** for MadGraph (never ran WriteUFO or import).
3. Ran all four checks (older version only). No WriteUFO, no MadGraph. 24 wolframscript runs.
4. No kernel queue, and a MadGraph import test. Note: with `LSM` and a `M$MixingsDescription`, the agent measured d,s,b masses 3x too large [143]; the scorer's 4x for d (3 + 1) agrees. So `LSM + ...` alone may also fail here (INFERRED).

## MDMmodel — mass_spectrum fail
1. OBSERVED VR: `Lagrangian: LSM + LTotal`; `particle=H|derived=176.77669529663692|declared=125.`; `particle=W|derived=112.88869216082195`. Cause: FR 337 `LTotal := LGauge + LGhost + LHiggsMDM + LFermKinSM + LFermKinTop` (no `LSM`); the Higgs sector is counted two times.
2. Own test, OBSERVED AS [80]: `CheckHermiticity: {}`, `CheckDiagonalKineticTerms: True`, `CheckDiagonalMassTerms: True`, spectrum `{H, ..., 125.00000000000001, 125.}`. MadGraph import worked after the agent removed its own duplicate `MDil`/`MTp` [163-172]. AO: "passes all four FeynRules checks on `LTotal`, writes a UFO, and imports into MadGraph 3.7.3". Class **(c)**. Small gap: the final re-check after the last edit was reported from a monitor notice; I did not see the agent read the log (INFERRED).
3. Ran all four checks, WriteUFO, MadGraph import. 11 wolframscript runs.
4. The same `LSM` rule as B-L-SM.

## Monotops — compile_timeout (1350 s)
1. OBSERVED VR: `HEPTAPOD-LAGRANGIAN|expression=LTotal|symbols=LTotal|terms=1381`, last line `Running consistency checks`; also `ReplaceAll::reps: {1} is neither a list of replacement rules...` at load. Direct cause INFERRED: the hermiticity check on the many 3x3 flavour tensors (FR 216-350, `Indices -> {Index[Generation], Index[Generation]}`, values from helper `ParamValues`, FR 152). Exact slow term not determined.
2. Own test, OBSERVED AS [51]: "The Hermiticity check fails. The leftover vertices contain `I*a0FC[...]`". After the fix (`ComplexParameter -> False`), [80]: "The check is still expanding L − HC[L] after 20 minutes." AO: "I can't yet confirm it passes any of the four checks or exports a UFO." Class **(d)**; the agent knew nothing was verified.
3. Ran: CheckHermiticity (1 result: fail; 1 run not finished). Other checks, WriteUFO on the model, MadGraph: no result. 10 wolframscript runs. Own time: first run more than 600 s to the first hermiticity output; second run more than 20 minutes without output. Its first job also held the kernel lock for more than 21 minutes and blocked SLQrules and GeneralU1 (SLQrules AS [99]).
4. A fast per-term hermiticity check, or the knowledge to give flavour matrices fewer free entries and to run with `FlavorExpand` limited.

## SLQrules — compile_timeout (1350 s)
1. OBSERVED VR: `HEPTAPOD-LAGRANGIAN|expression=LTotal|symbols=LTotal|terms=19509`, then `Running consistency checks` and timeout. Cause: size of the expanded Lagrangian (FR 615 `LTotal := LSM + LQall;`, five leptoquarks with all quartic terms). Exact term not determined.
2. Own test: only one FeynRules load completed, on an older file, OBSERVED AS [104]: `Syntax::sntue: Unexpected end of file ... (line 615 ...)`, `Power::infy`, and `$Aborted` in the hermiticity step. The agent fixed both and restarted; the job was stopped in the queue. AO: "The model has not been loaded successfully yet, so I can't report on hermiticity, ... the UFO export or the MadGraph import." Class **(d)**.
3. Ran: CheckHermiticity (aborted, old file). No other check result, no WriteUFO, no MadGraph. 5 wolframscript runs. Own compile time: not visible (never completed). [99]: "The kernel is held by another session's `run_model.wl`, which has been running for about 21 minutes".
4. A kernel of its own from the start, and a term-count report that shows 19509 terms before the checks.

## SMWeinberg — no_lagrangian_symbol
1. OBSERVED VR: `(no compile log)`. The scorer found two top-level terms that no other term uses: FR 117 `LTotal := LSM + LNkin + LNmass + LNint0 + HC[LNint0];` and FR 113 `LNGGlep := Block[{mu},` (kept on purpose, FR 109: "NOT included in LTotal"). Scorer rule, OBSERVED `validation_benchmark.py:102`: "Several roots means the model never declared a single total". The link between the two is INFERRED (I did not run the scorer).
2. Own test: all checks, UFO and import worked. AO: "Hermiticity, diagonal kinetic terms, diagonal mass terms and the mass-spectrum table passed on LTotal before the final `OrderBlock`/`ComplexParameter` edit. I didn't rerun them after that edit." and "`LNGGlep` but not in `LTotal`, because FeynRules can't build its vertex". Class **(c)**. The model was never compiled by the scorer, so its real result is unknown.
3. Ran all four checks, WriteUFO, MadGraph import, and a MadGraph cross-section (1.45x the paper value). 25 wolframscript runs.
4. One prompt line: "no top-level `L... :=` definition other than `LTotal` and its parts" (or put the unused term in a comment).

## pSPSS — hermiticity + kinetic_diagonal + mass_spectrum fail
1. OBSERVED VR: `Lagrangian: LTotal`; hermiticity `39 possible non-zero vertices`; `Non diagonal kinetic term found`; `particle=n4|derived=49.9999749999995|declared=100.0000499999995`; `particle=ghZ|derived=128.95874064025287|declared=91.1876`. Cause: FR 252 `LTotal = RemoveHigherOrder[LSMflav + LYukFlav + LNPkin + LNPmass];` with FR 229 `LSMflav := ExpandIndices[LSM, FlavorExpand -> Generation] /. mixRules;`. The model rotates `vl` inside the SM Lagrangian by text replacement and cuts terms by power of theta; this breaks the pairs of conjugate terms. The n4/n5 mass is half the declared value (INFERRED: Majorana factor 1/2 in `LNPmass`).
2. Own last test, OBSERVED AS [111]: `39 vertices obtained.`, `Non diagonal kinetic term found: (n4bar[...] . del[n5[...`, `All mass terms are diagonal.`, `Getting mass spectrum.` AO: "The kinetic-term check fails on off-diagonal n4–n5 and n–ν_μ terms, and the hermiticity check fails with 39 vertices. ... If you want me to keep going on that, say so." Class **(b)**. Also **(a)** for the mass spectrum: the agent wrote "CheckMassTerms / CheckMassSpectrum | Pass: all mass terms diagonal", but it read the diagonality line, not the mass table.
3. Ran all four checks (2 fail, mass table not read). No WriteUFO, no MadGraph. 19 wolframscript runs.
4. The standard method (declare `n4`, `n5` and put the mixing in the `Definitions` of the gauge fields or in explicit new interaction terms; do not rewrite `LSM`), and a check tool that returns the mass table as data.

## Cross-run counts (all 16 runs; script: `/tmp/claude-forensics/x/stats2.py`)

"In a script" = the call text is in a command or file that the agent wrote. "Result on own model" = I read the transcript (9 failures) or the run passed.

| Item | In a script | Result on own model |
|---|---|---|
| CheckHermiticity | 16 | 15 (not SLQrules) |
| CheckDiagonalKineticTerms | 16 | 14 (not Monotops, SLQrules) |
| CheckDiagonalMassTerms | 16 | 14 (not Monotops, SLQrules) |
| CheckMassSpectrum | 16 | 13 (not 331, Monotops, SLQrules; ALRM partial) |
| WriteUFO | 13 (not GeneralU1, SLQrules, pSPSS) | 11 tried, 10 wrote a UFO (ALRM failed; 331 and Monotops never ran it on the model) |
| MadGraph `import model` | 10 | 10 (7 passes + B-L-SM, MDMmodel, SMWeinberg) |

- wolframscript runs (`run.json`, `wolframscript_runs`): median 16 for all; 13 for passes; 18 for failures.
- `LTotal` contains `LSM`: 7 of 7 passes; 4 of 9 failures (Monotops, SLQrules, SMWeinberg, pSPSS).
- `result` events per run: 1 for all 7 passes and B-L-SM; 3 to 7 for the other 8 failures.
- 7 passes, `score_ufo/vertices.py`: all new particles have vertices. Only SM ghosts and Goldstones have none (ChernSimonsPortal, pNG), which is normal in unitary gauge.

## Summary

| Paper | Scored failure | Class | Cause in one line | What would have helped |
|---|---|---|---|---|
| 331 | compile_failed (`Inner::incom`, recursion limit) | b (+d) | Colour index missing in `LEW` bilinears (FR 354); full-replacement `LTotal` gets `LSM` added; agent saw the error, session stopped while it waited | Bounded check tool with verdicts; the `LSM` rule |
| ALRM_general | compile_failed (recursion limit in hermiticity) | b | Same recursion error in the agent's own `CheckHermiticity`; `WL` not expanded in WriteUFO; first FeynRules load came too late | Early compile; pointer to the bad vertex; the `LSM` rule |
| B-L-SM | hermiticity + mass_spectrum | c | `LTotal` uses `LGauge + LFermions + ...` without `LSM` (FR 323); scorer adds `LSM`, SM counted two times; agent's own 4 checks + MadGraph passed | Prompt line: `LTotal` must include `LSM` |
| GeneralU1 | mass_spectrum + MadGraph | d + c + a | Last rewrite (no `LSM`, FR 426) never tested: job died in the kernel queue; `MSphi` declared two times (FR 89, 225); no WriteUFO or import run | Own kernel; MadGraph import test; the `LSM` rule |
| MDMmodel | mass_spectrum | c | `LTotal` without `LSM` (FR 337); Higgs sector counted two times; agent's own chain passed | Prompt line: `LTotal` must include `LSM` |
| Monotops | compile_timeout | d | Hermiticity check on many 3x3 flavour tensors does not finish; agent's own run >20 min, no check verified | Fast hermiticity feedback; leaner flavour structure |
| SLQrules | compile_timeout | d | 19509 terms; agent got one kernel slot (old file with a syntax error); final file never loaded by the agent | Own kernel; early term count |
| SMWeinberg | no_lagrangian_symbol | c | Unused top-level `LNGGlep :=` (FR 113) is a second root next to `LTotal`; model itself passed the agent's checks and MadGraph | Prompt line: only one unused top-level `L` term |
| pSPSS | hermiticity + kinetic_diagonal + mass_spectrum | b (+a) | `LTotal` rewrites `LSM` with replacement rules and a theta cut (FR 229, 252); agent knew 2 checks failed and stopped; read "mass terms diagonal" as a mass-spectrum pass | Standard mixing method; mass table as data |
