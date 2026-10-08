# Hill climb on the ground-truth metric (2026-10-07 to 2026-10-08)

Stopped: the agent cost reached about $324 against a cap of $250. The
decision log is `decision.tsv` (not committed; its rows are below).

## Metric

`ref_score.py`. For each paper, the new-physics vertex kinds of the
delivered UFO against those of the paper's reference model from the
FeynRules database, compiled here (`ref_ufo/`, 13 of 16 usable). A particle
is what it is (SM by PDG code without generation; new by spin, charge,
colour). Metric = vertex F1 when the scored chain passes, else 0. It does
not compare coupling values, signs or Lorentz structures.

## Results on the 13 papers with a reference

| group | chain pass | metric | F1 without the pass factor |
|---|---|---|---|
| vanilla, run 1 (task without the scorer's two rules; half on the Mac) | 5 | 0.37 | 0.53 |
| vanilla, run 2 (task with the rules; one machine, 5 runs at the 2-hour limit) | 9 | 0.52 | 0.55 |
| harness (stored, 2026-09-30) | 9 | 0.47 | 0.54 |
| optimised harness | 11 | 0.63 | 0.71 |
| shell + tools, seed 1 | 12 | 0.69 | 0.69 |

Shell + tools seed 1 against vanilla run 2, by paper: higher on 6 (Wprime,
EffLRSM, Monotops, 331, GeneralU1, B-L-SM), lower on 0; exact sign test
p = 0.031. The two largest differences (Wprime, EffLRSM) are vanilla runs
that hit the time limit while they waited for the one kernel; without them
the difference is small.

## Attempts

| id | hypothesis | result | verdict |
|---|---|---|---|
| 1 | the agent leaves interactions out because it has no list of what the model must contain (arm `cover`: spec.json first, a spec review, a coverage gate) | 6 dev papers: 0.631 to 0.693 (+0.06), cost +55% | not accepted: inside the noise |
| 2 | a gate on photon and gluon vertices of new charged and coloured particles | not run: 4 of 13 reference models have the same gaps | rejected, $0 |
| 3 | seed noise | shell seed 2 on the 6 dev papers: 0.530 against 0.631; pSPSS passed once and failed once | measurement |
| 4 | replication of vanilla with a fair task | 0.37 to 0.52; cost $244 | measurement; budget exceeded |

## What this supports

- The order vanilla < harness < optimised < shell + tools holds on the
  ground-truth metric with one seed each, and shell + tools is not below
  vanilla on any of the 13 papers.
- The size of the gain over a fairly briefed vanilla agent is about 0.17 on
  a 0-to-1 scale, with a seed-to-seed noise near 0.1 on a 6-paper mean. Two
  seeds per group on 13 papers were planned and not finished.
- On the three large gauge models (331, ALRM_general, GeneralU1) every group
  is far from the reference (0 to 0.4, apart from one 0.81).
- No change tried in this climb moved the metric past the noise.

## What it does not support

- "Clearly superior": one seed per group, an in-sample set of papers, and a
  vanilla replicate confounded by kernel contention.
- Anything about coupling values.

## Costs

Iteration 1 $39.5; noise run $36.4; vanilla run 2 $244.1; two shell seed-2
runs about $3. Vanilla run 2 was estimated at $65. Its runs waited for the
kernel through many long turns; 331 alone cost $69.
