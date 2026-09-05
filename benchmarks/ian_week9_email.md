**Subject:** Week 9 — corrected benchmark numbers, review bundle, and 9 questions for you

Hi Ian,

Short version: the full pipeline now runs end to end, the review bundle is ready
for you, and I have to correct a number I gave you earlier. There are also nine
model-level questions that need a physicist rather than a parser — that is the
main thing I need from you.

---

**A correction first**

I previously reported 25 of 28 models clearing the validation chain. **That number
was wrong and I have withdrawn it.** The corrected figures are:

| outcome | models |
|---|---|
| clear the full chain | 18 |
| fail | 1 |
| cannot be scored | 9 |
| total | 28 |

The cause was a bug in my benchmark harness, not in the models or the physics
tools. The harness picked each model's total Lagrangian by file position — it took
the last `L... =` line in the file. For 11 models that line was a sub-Lagrangian,
not the total, so FeynRules compiled only a fragment of the model.

A fragment is easier to satisfy than a whole model. It can be Hermitian when the
full Lagrangian is not, and it can show a clean mass spectrum simply because most
of the fields are missing. Those fragments passed every check and imported into
MadGraph. The worst case was `VLQ`, which was recorded as passing having compiled
**1 of its 11 Lagrangian terms** — none of the vector-like quark interactions were
present.

The harness now resolves the total by reference analysis, and where a model never
declares one it refuses to guess. I re-ran everything: all 19 scoreable models
reproduced their previous verdict, so the pipeline did not get worse. Nine models
were simply never properly measured.

One consequence: 3 of the 10 repairs I reported the loop making (`331`, `CHEIDI`,
`VLC_LN`) were scored against fragments, so those claims cannot stand. Seven do.

---

**What I need from you: nine decisions**

Nine models define several independent top-level Lagrangians and never say which
one — or which sum — is the model. The harness cannot know, so it leaves them
unscored. **Unscored is not failed** — these models may be perfectly correct.

Five look like complementary sectors where summing is the natural reading:
`331`, `VLQ`, `HNLs`, `ALRM_general`, `VLC_LN`. I have written my proposed total
for each but applied none of them.

Four are genuine physics choices I should not make:

- `ChernSimonsPortal` — the same operator appears twice, once in the symmetric
  phase and once expanded in mass eigenstates. Summing them would double-count.
- `DMsimp` — spin-0 versus spin-1 mediator, published as separate models.
- `topBSM` — four simplified models in one file (colour singlet/octet × spin 0/1).
- `CHEIDI` — full top loop versus heavy-top limit.

`LAGRANGIAN_AMBIGUITY.md` in the bundle lists what each one defines. Each answer
moves a model out of the unscored pile and into a real pass or fail.

---

**The review bundle**

`review_bundle.zip` — 99 files, ~2 MB. Every one of the 28 models has exactly one
PDF; open that and you have everything for that model.

```
README.md                     what to read, in order
LAGRANGIAN_AMBIGUITY.md       the nine decisions above
CONVENTION_DISAGREEMENTS.md   137 graded rows
CORRECTION_2026-08.md         the correction, in full
reports/                      per-stage machine output
passing/    18 models         .fr + review PDF
failing/     1 model
unscored/    9 models
```

On the physics: passing the chain means the tools accept the model. It does not
mean the model matches its paper. To test that, an agent that never saw the paper
reconstructed the Lagrangian from the sanitized `.fr` alone, and a second fresh
agent compared that reconstruction against the paper term by term. It graded 137
differences: **45 convention, 79 substantive, 13 cosmetic.**

Those grades come from an agent, not a physicist. They are the question list, not
the answer. The 79 substantive rows are where your time is best spent.

One caveat: four review packages (`331`, `B-L-SM`, `CHEIDI`, `VLC_LN`) are thin.
Their reverse runs died on agent-transport errors, not on any physics result. I
have since fixed the underlying cause and can regenerate them if useful.

---

**New this week: checking models against experiment**

Everything above asks whether a model matches its paper. I have added tools that
ask the other question — whether the model is already excluded by measurement. A
model can transcribe its source paper perfectly and still sit in a region ruled
out years ago.

The tools search NASA ADS (which reaches the astrophysical and cosmological
literature, and can search paper bodies rather than only abstracts), then extract
the reported bounds with the source sentence attached to each one.

Testing against the live service was worth it. My unit tests all passed while the
tool returned the wrong papers: the first real query for a leptoquark model
returned a theory review rather than an experimental search. Three fixes later it
returns actual ATLAS and CMS leptoquark searches, newest first, because a 2026
limit supersedes a 2015 one.

I want to flag the limitation clearly: these are a reading aid, not a verdict.
Whether a bound applies depends on the assumed production mode, the branching
fractions, and the analysis's own assumptions. Every extracted number keeps the
sentence it came from so you can check it.

---

**Pipeline status**

The whole chain now runs end to end on a real paper: arXiv source → FeynRules
`.fr` → UFO compile with Hermiticity, kinetic-term and mass-spectrum checks →
MadGraph import → independent re-reading → experimental-limit search. Five stages,
about three and a half minutes, all passing.

The one part that does not work yet is the automated reading of the paper itself.
Run against a local 14B model, it produced a model with zero particles from the
raw LaTeX. That is a model-capability gap rather than a broken tool — the pipeline
correctly refused to compile the empty result rather than hiding it. Everything
downstream of that step is solid.

---

**Links**

- Benchmark results and per-model review packages:
  https://github.com/KenWuqianghao/Agentic-Lagrangian-Extraction/tree/benchmarks/loop-results/benchmarks
- Corrected benchmark summary: [artifact link]
- This week's progress summary: [artifact link]

The code is up for review on the HEPTAPOD dev repo.

Happy to walk through any of it on a call, particularly the nine decisions — I
suspect that is faster spoken than written.

Best,
Ken
