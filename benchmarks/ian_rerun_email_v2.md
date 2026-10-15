Hi Ian, Konstantin,

Thanks — the Z_R catch was the useful kind, because it was our fault rather
than the model's, and it pointed at something we could fix at the source.

**What caused it.** Eq. (8) of 1610.08985 is

    L = [ -kappa_R^f g / sqrt(1 - (1/kappa_R^f)^2 tan^2 theta_W) ] * ...

with the root in the denominator. The benchmark was feeding the agent
PDF-extracted text, and that extraction flattens a `\frac` into separate
lines: numerator, bar and denominator arrive as three fragments, and a product
and a quotient become indistinguishable. Both agents made the same slip — the
one writing the model and the one checking it — which is exactly why the
crosscheck graded that row "agree". It was not two independent readings; it
was the same corrupted input read twice.

So the fix is upstream of the prompt. Every benchmark paper now carries its
arXiv **LaTeX e-print** next to the PDF text, and the reruns read that. The
`\frac` and `\sqrt` survive intact, and one run even left a comment in the
`.fr` saying it had taken the placement from the LaTeX. Where no e-print
exists, the prompt now tells the agent to settle any fraction or root against
a second equation that depends on the same coefficient — a width or a cross
section — and to name that equation in its self-audit.

**Only papers that define one model.** You asked for this, and it turned out
to matter more than expected. Each of the 28 papers was read by one agent and
then attacked by two more, one re-counting the models from the physics and one
checking what the FeynRules-DB reference file actually implements; a paper is
selected only when all three agree. **18 of 28 qualify.** The exclusions are
real, not bookkeeping:

- `Sextets` and `Triplets` are **the same paper**, 0909.2666, paired with two
  different reference files. The paper explicitly offers antitriplet *or*
  sextet as a choice the implementer must make.
- `HiggsCharacterisation` offers spin-0, spin-1 and spin-2; `DMsimp` spin-0 vs
  spin-1 mediators; `HNLs` Majorana vs Dirac; `VLQ` a vector-like singlet vs a
  fourth generation.

The same pass found **five reference pairings that cannot be scored at all**,
which is worth your attention because we have been quoting numbers against
them:

- `LeptoQuark` is scored against `VLferm.fr`, a vector-like-fermion add-on the
  paper never defines. The paper's U(1)+Z'+G' model is in three other files in
  the same directory.
- `CHEIDI`'s benchmark text is arXiv:1010.3251**v2**, which was retitled and
  stripped of the physics — it is a FeynRules-WHIZARD interface paper with no
  model in it. `HEIDI.fr` implements the withdrawn v1.
- `VLC_LN`'s reference is only a collider subset of the paper's model.
- `MSSMD`'s listed publication is a CMS search, and `topBSM` we had already
  corrected once.

That leaves 16 papers that are both single-model and honestly scorable.

**The reruns.** Four models, two seeds each, three arms that differ in one
thing at a time: the framework as shipped, the framework reading PDF text
instead of LaTeX, and — the ablation you asked for — the same agent with
**every tool taken away**, the paper and `SM.fr` pasted into the prompt, and
the agent writing the whole `.fr` by hand.

Against your findings, with one deterministic check per finding:

| finding | before | with the addendum | v3 rules, PDF text | v3 rules, LaTeX |
|---|---|---|---|---|
| Z' kinetic + mass term | 2/2 | 2/2 | 2/2 | 2/2 |
| sextet explicit 1/Λⁿ | 2/2 | 2/2 | 2/2 | 2/2 |
| sextet `AddGaugeRepresentation` | 0/2 | 0/2 | **2/2** | **2/2** |
| EffLRSM ν^c on the W_R current | 2/2 | 2/2 | 2/2 | 2/2 |
| EffLRSM Z_R root in the denominator | 1/2 | 2/2 | 1/2 | **2/2** |
| General U(1) ε + Higgs charge | 1/2 | 2/2 | 0/2 | 1/2 |

The last two columns run the same rules on the two paper sources, so they
separate the two fixes cleanly. The sextet gauge representation is fixed by
the prompt — 2/2 whichever source it reads. Your Z_R finding is fixed by the
source — 1/2 on the PDF text, 2/2 on the LaTeX, with everything else held
constant. That is the claim in the first paragraph, measured rather than
asserted.

The sextet gauge representation is one we found ourselves rather than one you
reported: without `AddGaugeRepresentation[SU3C -> {T6, Sextet}]` the sextets do
not couple to gluons at all, and no run before this one had ever emitted it.

**The one that still fails, and it is a new disguise of your finding.** One
General U(1) seed writes the Dirac neutrino Yukawa *after* electroweak
symmetry breaking — `H vlbar.ynu.ProjP.NR` — rather than in the doublet form.
With no doublet there is no ε contraction to get wrong, and the charged-lepton
partner of the vertex is silently gone. Same defect class as the one you
reported, reached a different way. The rule that would catch it — write
Yukawas in the symmetric phase, with the doublet, never with the physical
Higgs — is not in the addendum yet. It will be.

**A caution about our own instrument.** Three bugs in those checks were caught
by running them against files the framework did *not* render, and every one of
them would have made the no-tools arm look worse than it is: regexes tuned to
the renderer's indentation; a model that named the Z_R denominator as a
parameter and divided by it later; and statements being split on a semicolon
inside `Block[...]`. They are all fixed and covered by 29 unit tests, and the
verdicts on the previously-scored files are unchanged. I mention it because
the honest version of "the reruns resolve your findings" has to include the
part where the measurement was wrong first.

**The sextets are still the hard case, and this is where I would value your
read.** The gauge representation is there now and both sextet checks pass, but
three of the four seeds run 15 minutes in FeynRules without finishing. The
fourth compiles in 8.6 minutes and MadGraph imports it, and it fails the
Hermiticity check while the kinetic-term and mass-spectrum checks pass. So the
model does get all the way through, and what is left is a genuine
non-Hermitian term rather than a stall. Two questions I cannot answer myself:
is the colour-sextet algebra expected to be this expensive in FeynRules, and
is the non-Hermitian residual the same SU(2)/colour covariant-derivative
commutator we saw on 331 and SLQrules?

**And the ablation you asked for.** With every tool taken away — no schema,
no renderer, the paper and `SM.fr` pasted into the prompt and the agent
writing the whole `.fr` by hand — the results are the same or slightly
better: the same findings resolved, 6 of 8 runs through the full
FeynRules → UFO → MadGraph chain against 5 of 8 with the toolkit, and field
content 0.86 against 0.83. The improvement over where we started (2 of 8
through the chain) is real, but on these four models it comes from the paper
source and the physics rules, not from the structured path. I would rather
tell you that than quote the number that flatters the tooling.

Everything — harness, per-model artifacts, the classification with its
evidence, and the generated tables — is on the `benchmarks/loop-results`
branch of the Agentic-Lagrangian-Extraction repo. `FINDINGS_2026-09.md` is the
entry point; `single_model_papers.md` has the per-paper classification with
quotes; `ablation_report.md` has every run.

Best,
Ken
