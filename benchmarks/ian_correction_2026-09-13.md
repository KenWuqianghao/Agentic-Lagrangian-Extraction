Hi Ian, Konstantin,

A correction to the numbers in my last note. The findings results stand. The full-chain results do not.

**What was wrong.** The benchmark read FeynRules' consistency checks by matching keywords in the printed prose. That classifier could not report a failure: every branch returned "pass", and none of its failure phrases matched what FeynRules prints. So every check verdict we reported was a pass unless the check crashed. Tony Menzo found this while he reviewed the code.

I also found a second fault while re-scoring. Some models define a total Lagrangian that already contains `LSM`, and the harness added `LSM` again. Those runs were checked with the Standard Model counted twice.

**What I did.** The harness now reads each check's return value, not its prose, and adds `LSM` only when the total does not contain it. I re-ran the checks on every stored model.

**What changes in my last note.**

| arm | full chain, as reported | full chain, corrected |
|---|---|---|
| v3, framework | 5/8 | 2/8 |
| v3, no tools | 6/8 | 4/8 |

The v1 and v2 numbers on these four models do not change. The new failures are real Hermiticity or mass-mixing failures, mostly in Top-Philic-Zprime and General U(1). The no-tools arm is still ahead of the framework, so that conclusion holds.

**What does not change.** The findings checks read the `.fr` text and never used FeynRules, so every finding result in my note stands. The field-content scores also stand.

The sextet statement also stands. The seed that compiles fails the Hermiticity check and passes the others, and the corrected parser confirms it.

The full correction, with every run's verdicts and log, is `benchmarks/CORRECTION_2026-09-13.md` on the `benchmarks/loop-results` branch.

Best,
Ken
