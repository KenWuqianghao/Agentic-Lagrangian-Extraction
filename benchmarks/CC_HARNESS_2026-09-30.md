# Claude Code with the chain in its loop: 16 papers, Sonnet 5 (2026-09-30)

Question: when Claude Code (Sonnet 5) writes the FeynRules add-on model
itself and can run the scored chain on it while it works (compile, the four
consistency checks, MadGraph import), how many of the 16 single-model
papers reach a full-chain pass? The two arms to beat, scored by the same
code:

- `v3s_notools`: Claude Code, Sonnet 5, no tools, one shot: 2/16;
- `pi_qwen_harness`: Qwen3.8-27B in the pi harness, same tools in the loop:
  4/16 (`PI_HARNESS_2026-09-28.html`).

Code: `cc_harness/` (this note), reusing `pi_harness/hepval.py`,
`run_pi.py`'s prompt, directories and scorer, and `summarize.py`.
Runs: `~/Documents/Github/heptapod/eval/benchmark_runs/<paper>/rerun/cc_sonnet_harness/s1/`.

## What the harness is

Every earlier Claude Code run in this benchmark was one-shot: the agent
wrote the file and stopped, and the harness validated it afterwards. The
repair loop started a new agent per round. Only the pi harness put the
validator inside the agent's loop, and pi cannot run Claude models on the
subscription ("Third-party apps now draw from your extra usage"). The new
parts are therefore an adapter, not a new pipeline:

- **`heptapod_mcp.py`**: an MCP server, `heptapod-tools`, over stdio
  JSON-RPC. Four tools, each a call to `hepval.py`: `lint_model`,
  `validate_model` (budget 10; the report opens with the call number and the
  stage reached: compile, checks, mg5 or pass), `massbasis`, and
  `review_model` (budget 2; a fresh `claude -p` referee in its own sandbox
  with a frozen copy of the model).
- **Sandbox by configuration.** `--tools Read,Write,Edit,Glob,Grep`,
  `--disallowedTools Bash,WebFetch,WebSearch,Task,Agent,NotebookEdit`,
  `--strict-mcp-config`, `--setting-sources ''`, and a PreToolUse hook
  (`hooks/pretool_guard.py`) that denies every path outside the sandbox after
  `..` and symlinks. The sandbox holds the paper, `SM.fr` and the agent's
  `model.fr`.
- **No finishing with a failing model.** A Stop hook (`hooks/stop_gate.py`)
  sends the agent back, with a digest of the last report, while `model.fr` is
  missing, never validated, changed since its last validation, or failed it.
  At most 3 continuations per run; none once the validate budget is spent.
  Every decision is logged with `stop_hook_active`.
- **The prompt** is `run_pi.py`'s harness prompt on stdin, and the protocol
  (`prompts/protocol.md`) is pi's, with the SM-override section verbatim.

## What the reports now say

The validate report had three gaps, each fixed without touching a verdict.

1. **Hermiticity.** The scoring driver reduces `CheckHermiticity`'s return
   value, the Feynman rules of `L - HC[L]`, to pass or fail (`runCheck` ->
   `vHermiticity` in `UFO_generator.wl`) and keeps only the printed prose, cut
   to 400 characters. A copy of the driver (`wl/UFO_generator_diag.wl`; the
   diff against heptapod-dev main 4bcbcf2 is the two check calls and the
   helpers) writes one line per non-zero vertex, its fields and coefficient,
   and the field contents of each named Lagrangian block, so the report says
   which block holds the vertex. A vertex whose coefficient still holds fields
   is one FeynRules could not reduce; the report says so. The copy is used
   only by the in-loop `validate_model` (`hepval validate --diag`); scoring
   keeps the pristine driver.
2. **Mass matrix.** When `mass_diagonal` fails, the same copy writes every
   off-diagonal mass term and every tadpole, with its coefficient and value.
3. **MadGraph import.** The report names the UFO file, line and object that is
   not Python, shows it, and lists the model.fr lines that declare or use the
   symbols in it (tensor parameters by component, particles through SM.fr's
   classes, the vertices that use a broken coupling).

Four constructs behind these failures are visible in the text, so they are
also `fr_lint` rules, each with a unit test. Precision on the 199 stored
models that have a verdict, among compiled files the rule flagged:

| rule | what it catches | flagged and compiled | failed the predicted stage |
|---|---|---|---|
| `pattern_symbol_name` | a quantum number named `B_L` (a Mathematica pattern) | 1 | 1 |
| `tensor_orderblock` | an `OrderBlock` on a parameter with `Indices` | 9 | 9 |
| `explicit_spin_in_chain` | `Xbar[sp].Ga[mu].Y[sp, ff]` | 8 | 7 |
| `numeric_spin_slot` | `l[1]` for the electron: the first index is spin | 4 | 4 (checks) |

The one miss of `explicit_spin_in_chain` is a self-hermitian current with the
full index list on both spinors (Top-Philic Z', pi Qwen harness), which
passes. Underscores in parameter names (`aSRh_u`) passed the chain in a
stored run, so they only warn.

## Replay: the six near-miss models of the pi Qwen harness

Each model failed only one stage. Replayed through the new
`validate_model` (`cc_replay/<paper>/agent_view.md`):

| paper | failed stage | old report | new report points at | fix |
|---|---|---|---|---|
| B-L-SM | MadGraph | "UFO model not python3 compatible" and a traceback | `particles.py` line 25 `B_L = (B_L)[A]`; model.fr lines 252 and 267, `QuantumNumbers -> {B_L -> ...}`; lint `pattern_symbol_name` on both | rename `B_L` |
| HeavyN | MadGraph | the same, plus a syntax error in `couplings.py` | coupling `GC_155` (vertex Z, ve); model.fr line 73, `NLbar[sp].Ga[mu].vl[sp, ff]` (the Z current); the `VlN` tensor declaration; lint `explicit_spin_in_chain` line 73, `tensor_orderblock` line 54 | implicit spin index; drop the OrderBlock |
| Wprime | MadGraph | the same, plus a syntax error in `parameters.py` | parameter `WpLeR1`; the whole `WpLeR == {...}` declaration with `OrderBlock -> 7`; lint `tensor_orderblock` on four tensors | drop the OrderBlocks |
| EffLRSM | hermiticity | generic "add `+ HC[...]`" text, no vertex | unreduced W_R-lepton vertices, block `LWRlepton` first; lint `numeric_spin_slot` lines 325-327, `NR1bar.Ga[mu].l[1]` | `l` with implicit indices, the member name, or all indices |
| SMWeinberg | hermiticity | the same generic text | vertices N e G0 G+ in block `LG0GP`, N e G+ (H) in `LNGP` | `LG0GP` has no `+ HC[...]` |
| pSPSS | hermiticity | the same generic text | unreduced W and Z vertices in blocks `LmixW` and `LmixZ`; lint `explicit_spin_in_chain` on the same lines | implicit spin indices |

For EffLRSM and pSPSS the old advice ("add `+ HC[...]`") was wrong: the
partners were there; the chains could not be reduced.

## Result: 11 of 16

Scored by `run_cc.py score` (run_pi's scorer: hepval with the heptapod-dev
main driver, never `--diag`), one seed, the same 16 papers for every arm.
A paper without a delivered model fails every stage.

| stage | `v3s_notools` (Sonnet, no tools) | `pi_qwen_harness` (Qwen3.8-27B, pi) | `cc_sonnet_harness` (Sonnet, this harness) |
|---|---|---|---|
| model delivered | 15 | 14 | 15 |
| compiled | 11 | 11 | 14 |
| hermiticity | 7 | 7 | 13 |
| mass_diagonal | 5 | 10 | 14 |
| all four checks | 4 | 7 | 11 |
| MadGraph import | 4 | 4 | 13 |
| **full chain** | **2** | **4** | **11** |

Paired exact McNemar tests on the same papers (two-sided; "only" counts the
papers one arm passes and the other does not):

| comparison | full chain | all four checks | mass_diagonal | compiled |
|---|---|---|---|---|
| cc vs no tools | 9 only cc, 0 only no-tools, **p = 0.004** | 8 vs 1, p = 0.039 | 10 vs 1, p = 0.012 | 4 vs 1, p = 0.38 |
| cc vs pi Qwen | 7 only cc, 0 only pi, **p = 0.016** | 4 vs 0, p = 0.13 | 4 vs 0, p = 0.13 | 3 vs 0, p = 0.25 |
| pi Qwen vs no tools | 2 vs 0, p = 0.50 | 4 vs 1, p = 0.38 | 6 vs 1, p = 0.13 | 2 vs 2, p = 1.0 |

The full-chain difference is significant against both arms at n = 16. The
per-stage differences against pi Qwen are not significant. Every paper
either baseline passes, this arm passes too.

The in-loop verdicts agree with the score: the 10 runs whose last
`validate_model` passed all scored a pass, and none scored a fail. The
eleventh pass, MDMmodel, is a final edit the agent made after its budget was
spent; it was never validated in the loop, and the scorer passes it.

## Per paper

| paper | score | validate calls | referee on the final model | minutes | input tokens | output tokens | cost |
|---|---|---|---|---|---|---|---|
| pNG | pass | 1 | no discrepancies | 13 | 1.45M | 43k | $1.56 |
| HeavyN | pass | 1 | no discrepancies | 7 | 0.74M | 25k | $1.03 |
| Wprime | pass | 2 | no discrepancies | 15 | 1.29M | 32k | $1.34 |
| Top-Philic-Zprime | pass | 2 | no discrepancies | 39 | 0.70M | 12k | $0.77 |
| ChernSimonsPortal | pass | 2 | no discrepancies (review 1 found one; fixed, re-validated) | 36 | 1.64M | 32k | $2.39 |
| EffLRSM | pass | 3 | no discrepancies | 30 | 1.98M | 68k | $1.99 |
| B-L-SM | pass | 4 | 0 physics-changing, 1 cosmetic (review 1 found one; fixed) | 65 | 5.17M | 115k | $4.42 |
| Monotops | pass | 6 | no discrepancies | 129 | 8.49M | 116k | $4.19 |
| pSPSS | pass | 10 | 1 physics-changing | 118 | 8.45M | 117k | $4.68 |
| NJLComposite | pass | 10 | 2 physics-changing, 1 cosmetic | 180 | 9.13M | 107k | $4.63 |
| MDMmodel | pass | 10 | 2 physics-changing (post-hoc review) | 162 | 13.35M | 157k | $5.87 |
| SMWeinberg | fail: hermiticity | 10 | none (no pass) | 134 | 12.96M | 158k | $5.50 |
| GeneralU1 | fail: kinetic_diagonal | 10 | none | 166 | 12.55M | 210k | $5.75 |
| 331 | fail: mass_spectrum, MadGraph | 10 | none | 235 | 16.92M | 295k | $7.79 |
| SLQrules | fail: compile | 10 | none | 89 | 32.89M | 305k | $11.26 |
| ALRM_general | no model (API output cap) | 0 | none | 49 | 0.68M | 282k | $3.82 |

Input tokens include cache reads (the uncached median is 0.21M); cost
includes the referee. Medians: **77 minutes, 6.8M input tokens, 115k output
tokens, $4.31 per paper**; total $67 for 16 papers. The pi Qwen harness
median was 42 minutes and 3.05M input tokens. Much of the extra wall time is
queueing: the Wolfram kernel was busy 4.4 of the 4.8 hours the runs spanned,
and 91 of the 99 in-loop validations waited for it (the longest 19.6
minutes).

**Referee verdicts.** Every full-chain pass has one on the model that was
scored. 8 of the 11 are clean (B-L-SM with one cosmetic item). Three are not,
and the chain cannot see why:

- MDMmodel (post-hoc review of the final edit, same referee code,
  `post_review.py`): the paper's `y' T_R (q3L . H)` top-partner mixing Yukawa
  is dropped, and the internal `kappa`, `lamH`, `lamS` do not match the
  paper's closed forms. This is the "pass by deleting a term" failure the
  protocol forbids; the referee caught it.
- NJLComposite: the Pi+/Pi- sector is declared twice with an extra Yukawa
  term, and a leptoquark width formula may double-count a colour factor.
  The agent had no validation left to fix it.
- pSPSS: the O(theta^2) light-lepton correction to the mixing is dropped; the
  referee calls it physics-changing in principle and about 1e-6 at the
  benchmark.

So the harness's count of chain passes that are also faithful to the paper
is 8 of 16 by the referee's reading. The physicist predicates written for the
September findings agree on EffLRSM (Z_R normalisation divides by the root,
nu^c conjugated; the pi Qwen model misses the Z_R root) and on General U(1)
(the Dirac Yukawa is still written in the broken phase, in this arm too).
The Top-Philic Z' predicate reads "no new vector class" in all three arms
because its parser returns no classes for these files; the model declares
`V[100] Vtp` with its kinetic and mass terms.

## How the failures end

| how the run ended | papers | example |
|---|---|---|
| passed, stopped | 10 | HeavyN: one validation, one review, 7 minutes |
| budget spent, gate released | 5 | SMWeinberg: 10 calls at `checks`; the hermiticity vertices were located in `LNGP` and `LG0GP` every time and never cleared |
| API error, no Stop event | 1 | ALRM_general: "response exceeded the 64000 output token maximum" before any file was written |

- **The Stop gate never had to block.** Every agent kept working until it
  passed or its budget was spent. The gate released 5 runs with "budget
  spent; a block cannot produce a new verdict". The block path is verified by
  the unit tests and a live run (a failing model blocked, then released at the
  limit). An API error ends the session without a Stop event, so the gate
  cannot help there; `run.json` now records `api_error`.
- **Compile failures to the end.** SLQrules (five scalar leptoquarks, a
  quartic sector of about forty terms) never compiled in 10 calls and used
  32.9M input tokens; 331 alternated between compile and check failures.
- **A defect the report names but the agent does not fix.** pSPSS wrote
  `n4bar.Ga[mu].ProjM.l[ff]`: one symbolic index on `l`, which fills the spin
  slot (the report showed `l[Index[Spin, 1]]` and called the chain
  unreduced, with the cause "an explicit spin or flavour index"). It took the
  agent 10 calls. `numeric_spin_slot` catches only a numeric index; widening it
  to any single index on a multi-index fermion is the next rule. The tools
  were not changed during the run.
- **Sandbox.** One call was denied in 16 runs: SMWeinberg tried to write a
  file outside the working directory. No call read outside the sandbox.

## Validation stayed serial

Papers ran up to 6 at a time; every validation took hepval's flock and then
waited for any other WolframKernel. `check_serial.py` reads the kernel-held
interval of every call (99 in-loop validations and replays): no two overlap.

## What this says

- **The chain in the loop is what moves the number.** The same model, Sonnet
  5, goes from 2/16 one-shot to 11/16 with the tools in its loop, and every
  paper the no-tools arm passes, this arm passes too. It also beats the same
  tools around a 27B open model (4/16).
- **The wall moved.** mass_diagonal passes in 14 of 16 (5 without tools):
  B-L-SM, the Higgs-singlet plus seesaw case that stopped every earlier arm,
  passed with the protocol's SM-override recipe (`Phi` redeclared with
  `CA H + SA H2`, `LTotal := LSM - LHiggs + ...`, the seesaw in the mass basis
  through `VlN` couplings). What remains is compile and hermiticity in the
  largest models.
- **A chain pass is not a physics sign-off.** Three of 11 passes carry
  physics-changing referee findings, one of them a term deleted to pass. The
  referee is the part of the harness that sees this, and it should run on the
  final model every time (it did not on MDMmodel, whose last edit came after
  its last review).
- **Cost.** A median of $4.31 and 77 minutes per paper at one Wolfram kernel;
  the kernel, not the agent, set the pace.

Caveats: one seed per arm; the referee is the same model as the agent; the
cc arm's validate budget is 10 (pi Qwen had 6); ALRM_general's output-cap
failure is kept as a failure in the table above.

## ALRM_general with a 128k output cap

A sensitivity rerun (`cc_sonnet_harness_maxout`, `--max-output-tokens 128000`,
same harness otherwise) removes the API failure but not the model failure.
The agent wrote a model, spent all 10 validations (9 stopped at compile, call
9 reached the checks), and edited the file once more after call 10, so the
Stop gate released it with the file unvalidated. Scored with the standard
driver: compiled, hermiticity, kinetic_diagonal and mass_diagonal pass,
mass_spectrum fails, MadGraph import fails. 52 minutes, 29.1M input tokens,
269k output tokens, $10.03. The full-chain count stays 11 of 16 whether this
run or the original is counted.

Files: `cc_summary_2026-09-30.json` (collect.py), `cc_logs/`, `cc_replay/`,
runs under `~/Documents/Github/heptapod/eval/benchmark_runs/*/rerun/cc_sonnet_harness/s1/`.
