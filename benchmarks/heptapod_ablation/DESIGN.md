# Ablation design: what does heptapod add to the loop?

Status: design, code and unit tests are done. One paper ran under three arms
as a smoke test (Wprime: `none` and `compile` fail the chain; `heptapod` passes the chain in 3 calls and the referee then finds 4 physics-changing items, so no arm reaches the endpoint). No arm has run on a paper set. Do not start one before the
design, the cost and the time below are approved.

## The question and the objections

The stored result (one-shot, no tools: 2 of 16; harness: 11 of 16) compares
"no loop" with a bundle. Three objections follow, and `RETRO.md` shows that a
fourth is real:

1. "Any feedback loop does this." The bundle was not compared with a generic
   loop.
2. "The recipe in the prompt does this." The no-tools arm did not have the
   SM-override recipe.
3. "These are ALE's wrappers, not heptapod." The in-loop report has sections
   that heptapod-dev main does not return.
4. A chain pass is not a model. Two of the 11 passes have no vertex for any
   new particle (Monotops, pSPSS), and three have a physics-changing referee
   finding (MDMmodel, NJLComposite, pSPSS).

## Arms

One harness (`cc_harness`), one model, one task prompt, one sandbox, one
validate budget. An arm is a row of `common.ARMS`: the MCP tools the agent
has, and what `validate_model` shows. The chain always runs in full, and the
full verdicts go to `validation/call<k>/summary.json`; the arm only selects
the agent's view. So every arm has the same latency per call, and the hidden
verdicts are there for the analysis.

| arm | MCP tools | what `validate_model` shows | Stop gate asks for |
|---|---|---|---|
| `none` | none | (no tool) | (no gate) |
| `compile` | validate | FeynRules wrote a UFO or not; the log when not | compiled |
| `import` | validate | `compile`, plus MadGraph imported the UFO or not; MadGraph's output when not | compiled and imported |
| `heptapod` | validate | what heptapod-dev main returns: stage, four check verdicts with FeynRules' message, the MadGraph error | full chain |
| `diag` | validate | `heptapod`, plus the ALE sections: non-hermitian vertices by block, mass-matrix entries, MadGraph back-trace to model lines | full chain |
| `lint` | lint, validate | `diag`, plus lint findings | full chain |
| `massbasis` | lint, validate, massbasis | as `lint` | full chain |
| `full` | lint, validate, massbasis, review | as `lint` | full chain |

`full` is the stored harness: its protocol text is byte-identical to the
prompt of the stored `cc_sonnet_harness` runs (a unit test compares the
hash). The SM-override recipe is in the protocol of every arm, so no contrast
between arms can come from the recipe (objection 2). The protocol of an arm
names only that arm's tools.

`compile` and `import` are the generic loops (objection 1). `import` is the
stronger control: a user without heptapod would also try to load the UFO in
MadGraph. `heptapod` against `import` isolates the four FeynRules checks with
verdicts from return values, which is heptapod's `ValidateLagrangian`.
`diag` against `heptapod` isolates the ALE additions that should go upstream
(objection 3).

## Primary endpoint (fixed before any run)

A run reaches the endpoint when all three hold (`endpoint.py`):

1. the scored file passes the full chain (the pristine heptapod-dev main
   driver, as in every stored score);
2. the referee, run after the agent stopped on the scored file
   (`cc_harness/post_review.py`, the same referee for every arm, whether or
   not the arm had `review_model`), reports no physics-changing discrepancy;
3. every new particle is in at least one vertex of the scored UFO.

Condition 3 is new. Without it the stored Monotops pass counts: the referee
reads the `.fr` text and found no discrepancy, and the UFO has 163 vertices,
the Standard Model's, and none with a new particle.

Secondary: full-chain pass; passes per stage; validate calls to the first
pass; cost per endpoint pass. A chain pass with no referee verdict is
reported as missing, not as a pass.

## Design A (recommended): repair from the same first draft

The stored runs hold 18 first drafts that compile and fail at least one
FeynRules check (the list is `power.json`, key `repair.units`; rule: a
failing draft whose failing check a compile + import loop does not report).
They come from four stored arms on 10 papers. Each arm starts from the same
draft (`run_cc.py --draft-from VARIANT`: the draft is `model.fr` in the
sandbox, and one sentence in the task says so) and differs only in the
feedback.

- Arms: `import`, `heptapod`, `diag`.
- Contrasts, tested in this order: `diag` against `import`; `heptapod`
  against `import`; `diag` against `heptapod`. A later contrast is
  confirmatory only if every earlier one is significant at 0.05.
- Why this design: every unit is one where the arms can differ, and the
  start is identical, so the draft-to-draft noise of an end-to-end run is
  gone. The end-to-end design has four such papers; this has 18 drafts.
- What it does not show: the end-to-end rate. It shows whether check
  feedback repairs a failing draft that generic feedback does not.

Power (`power.py`; exact test stratified by draft, two-sided 0.05; g, h and
d are the assumed endpoint rates under `import`, `heptapod` and `diag`):

| assumed repair rates | 1 seed | 2 seeds | 3 seeds |
|---|---|---|---|
| h 0.30, g 0.10 | 0.15 | 0.45 | 0.68 |
| h 0.45, g 0.10 | 0.49 | 0.89 | 0.98 |
| h 0.60, g 0.10 | 0.82 | 1.00 | 1.00 |
| h 0.45, g 0.20 | 0.22 | 0.54 | 0.74 |
| d 0.60, h 0.45 | 0.08 | 0.18 | 0.28 |
| d 0.65, h 0.35 | 0.29 | 0.66 | 0.84 |

The first four rows are `heptapod` (or `diag`) against `import`; the last two are `diag` against `heptapod`.

The stored runs give one anchor for d: of the four stored Sonnet drafts with
a failing check, two reached the endpoint with located reports and a budget
of 10 (B-L-SM, EffLRSM), and two did not (SMWeinberg, pSPSS). So d is near
0.5, h is at most that, and g is a guess. **Seeds: 2.** With d = 0.45 to 0.6
and g = 0.1 the first contrast has a power of 0.90 or more; the second needs
h of 0.45 or more for 0.90; the third is underpowered at any affordable seed
count and is descriptive.

## Design B: end to end, 11 papers

- Papers: the 11 that passed the chain in the stored harness run. The other
  five (331, ALRM_general, GeneralU1, SLQrules, SMWeinberg) passed in no
  stored arm, cost $34 of the stored $67, and count as fails in every arm.
  This is an assumption; it biases `full` up against the other arms, and it
  does not bias `heptapod` against `compile`.
- Arms: `compile`, `heptapod`, `full` (and `none`, one seed, descriptive).
- Budget 6: the stored run reaches every one of its endpoint passes by call 3.

Power (per-paper predictions derived from `retro.json` by the rule in
`power.py`; r and f are the assumed pass rates of a predicted pass and a
predicted fail):

| contrast | scenario (r, f) | 1 seed | 2 seeds | 3 seeds | 4 seeds | 5 seeds | 6 seeds |
|---|---|---|---|---|---|---|---|
| heptapod vs compile | optimistic (0.9, 0.05) | 0.01 | 0.42 | 0.69 | 0.86 | 0.94 | 0.97 |
| heptapod vs compile | central (0.75, 0.1) | 0.01 | 0.18 | 0.31 | 0.43 | 0.55 | 0.64 |
| heptapod vs compile | pessimistic (0.6, 0.15) | 0.01 | 0.09 | 0.13 | 0.19 | 0.24 | 0.29 |
| full vs compile | optimistic (0.9, 0.05) | 0.03 | 0.71 | 0.92 | 0.99 | 1.00 | 1.00 |
| full vs compile | central (0.75, 0.1) | 0.03 | 0.33 | 0.53 | 0.71 | 0.83 | 0.88 |
| full vs compile | pessimistic (0.6, 0.15) | 0.02 | 0.15 | 0.21 | 0.32 | 0.41 | 0.48 |
| compile vs none | optimistic (0.9, 0.05) | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 |
| compile vs none | central (0.75, 0.1) | 0.00 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |
| compile vs none | pessimistic (0.6, 0.15) | 0.00 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 |
| full vs heptapod | optimistic (0.9, 0.05) | 0.00 | 0.04 | 0.09 | 0.13 | 0.16 | 0.22 |
| full vs heptapod | central (0.75, 0.1) | 0.00 | 0.03 | 0.05 | 0.07 | 0.09 | 0.09 |
| full vs heptapod | pessimistic (0.6, 0.15) | 0.01 | 0.03 | 0.03 | 0.04 | 0.05 | 0.05 |

Only four papers can differ between the arms (B-L-SM, EffLRSM,
Top-Philic-Zprime, Wprime), so this design needs 5 seeds for a power of 0.83
on `full` against `compile` under the central assumption, and more than 6 on
`heptapod` against `compile`. No seed count makes it generalise beyond these
papers; that needs more papers (about 58 per arm for 25% against 50%, as
`OPTIONS_2026-09-22.md` computed).

## Design C: heptapod as released, through toolbase (hepbench)

`hepbench-dev/benchmarks/model_building` has the paired loadouts already:
`core_only` (the agent drives `wolframscript` itself: a generic loop with a
shell) and `tools_model` (heptapod's four tools and its FeynRules skill,
served by toolbase). It has two tasks (heavy_neutrinos,
hidden_abelian_higgs) and grades the UFO against reference vertices, not the
ALE chain. It is the only arm that tests the released toolkit and its skill
text. It cannot run on this machine now: `toolbench` and `toolbase` are not
installed, and `git fetch` from the repositories fails without a login. With
two tasks it needs many seeds per task (the test is the same exact test,
stratified by task), and it answers a different question: does the released
skill and tool set beat a shell.

## Cost and time on this machine

Measured here (2026-10-06, `local_rescore.py` on the 15 stored harness
models, compile limit 3600 s): all 15 verdicts agree with the stored ones, and the compile takes 1.25 to 1.56 times as long as on the Mac (median 1.5).

| design | runs | agent cost | referee | kernel hours | wall time |
|---|---|---|---|---|---|
| A: 18 drafts x 3 arms x 2 seeds | 108 | about $270 | about $25 | about 26 | about 30 h |
| A, two arms (`import`, `diag`) x 2 seeds | 72 | about $180 | about $15 | about 17 | about 20 h |
| B: 11 papers x 3 arms x 3 seeds | 99 | about $205 | about $40 | about 13 | about 16 h |
| B: 11 papers x 3 arms x 5 seeds | 165 | about $345 | about $65 | about 22 | about 27 h |

How the numbers come: design B is `design_cost.py` (the stored harness run
cut where each arm would stop, cost by the fraction of agent time, kernel
seconds times the local time ratio; per seed: `compile` $17, `heptapod` $22,
`full` $30). Design A has no stored run: $2.50 per run is the mean of the
stored runs that needed a repair, cut at budget 6; 4 validate calls per run
at 175 s, plus one scoring run each. The smoke test on Wprime (`results/smoke_Wprime_endpoint.json`) cost $0.88 (`none`), $0.81 (`compile`, 1 validate call) and $1.47 (`heptapod`, 3 calls), plus one referee call; a validate call took 202 to 204 s of kernel time.
Expect these to be wrong by up to 50%. The kernel is serial, so kernel hours
are a floor on wall time; at most 6 agents at a time fit in 14 GB next to
the kernel.

The compile limit stays 900 s for these designs: the slowest of their papers
compiles in 253 s here. 331 needs 1198 s here (805 s on the Mac) and is in
neither design; a run that includes it needs `HEPVAL_COMPILE_TIMEOUT=1350`.

## Commands

```bash
source ~/hep-tools/env.sh
cd ~/code/ALE-ablation
export PI_HARNESS_RUNS=$(benchmarks/heptapod_ablation/runs_root.sh)   # writable tree; the stored one is read-only
python cc_harness/run_cc.py check --model claude-sonnet-5

# Design A. One block per draft source; the papers of each source are in power.json (repair.units).
SEEDS=2
run_a() {   # run_a <draft variant> <papers>
  for arm in import heptapod diag; do
    python cc_harness/run_cc.py run --arm $arm --draft-from $1 --variant cc_rep_${arm}_from_$1 \
      --pages $2 --seeds $SEEDS --model claude-sonnet-5 --validate-budget 6 --parallel 2 &
  done; wait
  python cc_harness/run_cc.py score --variants cc_rep_import_from_$1,cc_rep_heptapod_from_$1,cc_rep_diag_from_$1 --pages $2 --seeds $SEEDS
  for arm in import heptapod diag; do
    python cc_harness/post_review.py --variant cc_rep_${arm}_from_$1 --pages $2 --seeds $SEEDS --chain-pass-only
  done
}
run_a cc_sonnet_harness B-L-SM,EffLRSM,SMWeinberg,pSPSS
run_a pi_qwen_harness   B-L-SM,ChernSimonsPortal,SMWeinberg,Top-Philic-Zprime,pSPSS
run_a pi_qwen_plain     HeavyN,Top-Philic-Zprime
run_a v3s_notools       B-L-SM,EffLRSM,GeneralU1,HeavyN,MDMmodel,Monotops,SMWeinberg
python benchmarks/heptapod_ablation/endpoint.py --arms import,heptapod,diag --variant 'cc_rep_{arm}_from_{source}' --seeds $SEEDS \
  --units "$(python -c "import json; print(','.join(json.load(open('benchmarks/heptapod_ablation/power.json'))['repair']['units']))")"

# Design B.
PAPERS=B-L-SM,ChernSimonsPortal,EffLRSM,HeavyN,MDMmodel,Monotops,NJLComposite,Top-Philic-Zprime,Wprime,pNG,pSPSS
for arm in compile heptapod full; do
  python cc_harness/run_cc.py run --arm $arm --variant cc_abl_$arm --pages $PAPERS --seeds 3 \
    --model claude-sonnet-5 --validate-budget 6 --review-budget 2 --max-continuations 3 --parallel 2 &
done; wait
python cc_harness/run_cc.py score --variants cc_abl_compile,cc_abl_heptapod,cc_abl_full --pages $PAPERS --seeds 3
for arm in compile heptapod full; do
  python cc_harness/post_review.py --variant cc_abl_$arm --pages $PAPERS --seeds 3 --chain-pass-only
done
python benchmarks/heptapod_ablation/endpoint.py --arms compile,heptapod,full --variant 'cc_abl_{arm}' --seeds 3 --units $PAPERS
```

Run `post_review.py` before a reboot: it reads the run's sandbox, which is a
temp directory.

Parameters that existed: `run`, `score`, `--variant`, `--pages`, `--model`,
`--review-model`, `--seeds`, `--parallel`, `--validate-budget`,
`--review-budget`, `--max-continuations`, `--max-output-tokens`, `--force`.

New, with unit tests (`cc_harness/test_arms.py`,
`benchmarks/heptapod_ablation/test_ablation.py`):

- `run_cc.py --arm` and `common.ARMS`; the per-arm protocol
  (`common.render_protocol` over `prompts/protocol.md`); the MCP server
  serves only the arm's tools; `hepval.py validate --view compile|import`;
  the Stop gate reads `told_pass` (what the arm's tool reported).
- `run_cc.py --draft-from` (design A) and `--first-seed` (a later batch must
  not re-run a failed run of an earlier seed).
- `run_cc.py` passes `HEPVAL_*` to the MCP server, so one compile limit holds
  in the loop and in the score.
- `run_cc.py score` keeps `score_ufo/particles.py` and `vertices.py`
  (endpoint condition 3).
- `post_review.py --seeds --chain-pass-only`.
- `endpoint.py`: the endpoint and the exact stratified test.

`agent_cmd` changed signature (it takes the arm). It has one caller,
`run_agent` (found with grep; GitNexus is not installed here).

## Threats to validity

- The referee is the agent's model. It reads the `.fr`, not the UFO: it
  called the vertex-less Monotops model clean. Condition 3 covers that case
  and no other.
- Design A's drafts are not independent: several come from one paper, and a
  paper's drafts tend to share a defect (`l[ff]` in every SMWeinberg draft).
  The test is exact for this fixed set of drafts. It does not generalise to
  other drafts.
- A `compile` or `import` agent that is told "OK" may still improve the
  file. The gate lets it stop; nothing stops it from working on.
- The chain runs in Feynman gauge (SM.fr's default). A correct Higgs
  override with a second vev then fails `mass_spectrum` on the ghost masses
  (331). That is a property of the scorer, the same in every arm.
- The Claude Code CLI here is 2.1.290; the stored runs used 2.1.282.
- `sympy` was not in `~/hep-tools/env`; `massbasis` needs it. It was
  installed on 2026-10-06 (1.14.0).
