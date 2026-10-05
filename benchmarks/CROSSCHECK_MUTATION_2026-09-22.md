# Option F: the crosscheck as a defect detector (2026-09-22)

Question: does the toolkit's blank-slate reviewer (`reverselagrangian`:
sanitise the `.fr`, reconstruct the physics with no paper in sight, then
compare the reconstruction against the paper's LaTeX with no `.fr` in sight)
find physics defects that the compile chain passes?

Code: `crosscheck_mutation.py`. Data: `crosscheck_mutation/<case>/` with
`model.fr`, `sanitized.fr`, `reconstruction.md`, `crosscheck.md`,
`judge.json`; `results.json` and `score_rule.md` are the generated scores,
`audit.json` the tool-policy audit.

## Design

- **8 base files.** Stored agent models that resolved every physicist
  predicate: Top-Philic Z', EffLRSM, General U(1), 368 sextets, Chern-Simons
  portal, pNG dark matter, 331, Monotops. Each is also a control.
- **31 mutants.** One injected defect per file, from eight operators:
  drop the SU(2) epsilon (1), flip a quantum number (5), drop a `1/Lambda`
  (1), drop a `CC[]` (2), invert a square-root normalisation (3), multiply a
  term by 2 (8), delete an interaction term from the model and the total (8),
  swap one chiral projector (3). A 32nd mutant changed only a comment and
  is excluded; the generator now rejects that case.
- **3 real-finding files.** The original agent files behind the September
  physicist findings: EffLRSM (bare `ve` for `nu^c`, Z_R root multiplies
  instead of divides), General U(1) (no epsilon, Higgs charge sign),
  368 sextets (no `1/Lambda`).
- **Engine.** Both phases use the toolkit's own prompts and sanitiser. The
  headless CLIs were logged out, so each phase ran as a Claude Code subagent
  (Opus 5) with a Read-only policy on its sandbox and one Write, audited from
  the transcript. 86 phases; one crosscheck (368 sextets, swap chirality)
  used Bash to look around after its prompt file was briefly missing, and is
  marked `audit_ok=False`; its inputs were the same two files.
- **Scoring.** A rule: does a non-agree row or a severity line mention the
  mutated symbol. A judge: a Sonnet subagent reads `crosscheck.md` and the
  defect description and answers whether the document names that defect
  (yes / partial / no), plus how many other substantive disagreements it
  lists.

## Result

| set | n | named by the reviewer (judge) | named by the rule |
|---|---|---|---|
| mutants | 31 | 31 yes | 19 |
| real findings | 3 | 2 yes, 1 partial | — |
| controls | 8 | — | — |

By operator, all named: drop epsilon 1/1, flip charge 5/5, drop cutoff 1/1,
drop conjugation 2/2, invert root 3/3, factor of two 8/8, delete term 8/8,
swap chirality 3/3.

The rule undercounts because the reviewer writes in physics, not in `.fr`
symbols; the judge reads the physics. Two examples of what "named" means:

- EffLRSM, swap chirality in the W_R quark current: "the paper's Eq.
  (chcurrent) gives the W_R quark current with P_R; the reconstruction
  reports P_L", with the note that the LO widths cannot see it and only spin
  observables and W-W_R interference can.
- 368 sextets, dropped cutoff: the reconstruction phase alone noticed that
  `LamPsu` is declared and never used and that the term is dimension five
  with no suppression; the crosscheck then confirmed it against the paper.

**The real findings.** The EffLRSM file: both defects named, and the Z_R
normalisation ranked first. This is the finding the September crosscheck
missed because it read flattened PDF text; on the LaTeX source it is found.
The sextet file: the absorbed cutoff named as the single largest issue. The
General U(1) file: the missing epsilon named and rated substantive; the
Higgs charge sign was argued the wrong way, as in September (the reviewer
concluded `-xH/2` is correct; Ian and Konstantin confirmed `+xH/2`). One of
the five September findings therefore still escapes this reviewer.

**Controls.** The eight unmutated files drew 0 to 9 substantive
disagreements each (mean 3.0, against 2.1 extra ones per mutant). Reading
them, they split three ways:

- Real gaps in the base file that the compile chain and the predicates
  cannot see: the pNG file has no scalar self-interactions, keeps the SM
  Higgs quartic and gives the mass eigenstates no rescaled couplings (it is
  the file whose mass check passes by omission); the 331 file implements 4
  of the paper's currents and none of the Z' couplings; the Chern-Simons
  file drops the Higgs-doublet and non-abelian pieces.
- Reviewer reasoning errors: a Landau-Yang remark on a narrative sentence
  (Top-Philic), a "half strength" claim on a Majorana vertex that the
  paper's own width refutes (EffLRSM), a reading of the scope of "+ h.c."
  (Monotops).
- Convention items correctly labelled as such.

So the false-positive cost is real but legible: a physicist gets a short
list where the injected defect is present and ranked, next to two or three
other items that are either genuine omissions or arguments they can settle
in a minute.

## What this says

- **The reviewer finds what the chain cannot.** Every one of the 31
  injected physics defects compiles, passes the four FeynRules checks and
  imports into MadGraph exactly as the unmutated file does; the crosscheck
  named all 31.
- **On the September findings it is 4 of 5**, with the LaTeX source doing
  the work on the Z_R root and the Higgs charge sign still lost. That single
  miss is a charge-convention argument, the hardest class for a reader who
  has only the paper.
- **The reconstruction phase is not blank about physics.** Several
  reconstructions inferred the paper's model from the file (a 229 GeV width
  pinned the top-philic Z' couplings). The design still separates the two
  readings, but "no memory of the paper" means no memory of this paper's
  text, not of the literature.
- **Cost.** About 80k tokens per reconstruction, 120 to 200k per crosscheck
  (the paper is read whole), 80k per judge; roughly 3 to 6 minutes per
  phase. No Wolfram time.

## What to build from this

1. Run the crosscheck on every model that passes the chain, and ship its
   disagreement list with the model. It is the only stage that reads the
   physics.
2. Give the crosscheck the paper's LaTeX, never the flattened text (already
   the harness default since 2026-09-09).
3. Add a third pass for U(1) charge conventions: re-derive every new-U(1)
   charge from Yukawa invariance under SM.fr conventions and compare, since
   the charge-sign class is what the paper-only reader gets wrong.
4. Keep this harness as the regression test for the reviewer: 31 mutants
   plus 3 real files, rerun whenever the prompts or the engine change.
