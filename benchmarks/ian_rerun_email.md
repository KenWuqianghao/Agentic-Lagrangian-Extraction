Hi Ian,

Thanks for the careful look — this was exactly the review the tool chain
could not give itself. Here is what I found when I went back over the four
models, and what the reruns show.

**First, where your four findings stand.** I re-derived each one from the
files (two independent checks per finding, against the paper, the .fr you
received, and the FeynRules-DB reference):

- **Top-Philic Z′ — not a defect, and my fault for the wording.** The .fr
  you have contains both terms: line 86 `LV1kin = -1/4 (del[V1[nu],mu] -
  del[V1[mu],nu])(...) + 1/2 MV1^2 V1[mu] V1[mu];`, summed into `LBSM` at
  line 94, with `MV1` as the class mass. The row you read in REVIEW.pdf
  ("No explicit kinetic or Proca mass term written in the paper's model
  equations … extra-in-reconstruction") says the *paper* prints only
  L_int; the label made it read as a gap in the model. I have renamed the
  verdicts so that row now says "in-model-not-in-paper (standard
  completion)". For what it is worth, the DB reference Top_Philic.fr is
  the file with no free-field terms.
- **EffLRSM — confirmed.** Line 192 writes the light-neutrino W_R current
  as `bar[ve[nn]].Ga[mu].ProjP.l[ll] WR[mu]` where Eq. (5) has ν^c. The
  bare form is lepton-number conserving; the paper's form violates L by
  two units, as a Majorana ν requires. It is numerically inert at the
  benchmark point (X = 0) and your reference drops the term entirely, but
  it is wrong as written.
- **General U(1) — both parts confirmed**, and your reading is sharper
  than the tool's own crosscheck, which marked the Higgs charge "agree".
  `LLbar[ii] … Phibar[ii]` on a shared index is not an SU(2) singlet, and
  after SM.fr's Φ components it gives charge-violating l̄ N h and ν̄ N G⁺
  vertices; every yNu was set to 0, which is why the UFO/MadGraph chain
  did not trip. The Higgs charge `-xH/2` is what Table I prints, but the
  paper's Eq. (1) and Table I use different Y(H) conventions; `+xH/2` is
  the unique choice for which all five Yukawas are U(1)_X invariant with
  the SM.fr Higgs, which is what U1XGeneric.fr does.
- **368 sextets — real relative to the paper, with a twist.** The file has
  no Λ anywhere, but its Lagrangian block is term-for-term identical to
  Taylor Murphy's reference, which also has no Λ (it absorbs κ/Λ, κ_B/Λ³,
  λ/Λ² into dimensionful CFu, CFBu, CSu with placeholder 0.1). The twist:
  the agent's event log shows it *opened that reference file during the
  run* and copied the convention. That run therefore tells us nothing
  about extracting 1/Λ from a paper, and I have treated explicit External
  cutoffs with the paper's exponents as the target.

  I then audited every run in the original fleet for the same thing, and
  it was not isolated: **18 of the 28 runs read their own reference file**
  (`sed -n '1,260p' eval/reference_cache/<model>/<ref>.fr` and the like),
  one read another model's reference, and 9 were clean. Of your four,
  Top-Philic Z′ and EffLRSM were clean; 368sextets read its own reference;
  General U(1) read others' but not its own. The benchmark numbers I sent
  earlier are therefore not a measure of extraction for those 18 models,
  and I will re-run the whole set sandboxed before quoting any pass rate
  again.

**What I changed.** The rerun harness now sandboxes the agent: it can see
the paper text, the schema, the renderer and SM.fr, and nothing else (the
original fleet had the whole repo, reference files included, one glob
away). Every run records whether the paper was read and whether anything
outside the sandbox was touched. I also wrote a physics-completeness
addendum for the prompt: free-field terms for every new field, explicit
1/Λ^(d−4) with External cutoffs, CC[] wherever the paper writes ψ^c, Eps[i,j]
for same-type doublet pairs, U(1) charges re-derived from Yukawa
invariance rather than copied from a table, and a mandatory per-term
self-audit (mass dimension, coupling dimension, Q/Y/new-U(1) sums).

**Reruns.** Each model was regenerated twice with the original prompt (v1)
and twice with the addendum (v2), sandboxed, under the same engine, so
the prompt is the only variable. All 16 runs read the paper; none touched
a reference file. Against your specific findings (deterministic checks on
the .fr text, written against the construct rather than symbol names):

| model | finding | v1 (original prompt) | v2 (addendum) |
|---|---|---|---|
| Top-Philic Z′ | kinetic + mass term | 2/2 | 2/2 |
| 368 sextets | explicit 1/Λ, 1/Λ², 1/Λ³ with External cutoffs | 2/2 | 2/2 |
| EffLRSM | ν^c on the light-neutrino W_R current | 2/2 (one drops the term as your reference does, one writes `CC[vlbar]`) | 2/2 (both `bar[CC[vl[…]]]`) |
| General U(1) | Eps contraction **and** Higgs charge +xH/2 | 1/2 (Eps 2/2; one run copied `-xH/2` from Table I) | 2/2 (both record the Yukawa-invariance reasoning) |

The honest reading: once the agent cannot see the answer key, three of the
four defects mostly do not recur even under the original prompt. The one
that does — copying a charge table without reconciling conventions — is
exactly what the addendum's charge-derivation rule fixes, and both v2
files say why they chose the sign.

**What the regenerated files still get wrong.** I had two independent
readers go through each file as a whole, not just for your findings. The
important one: every 368sextets rerun omits
`AddGaugeRepresentation[SU3C -> {T6, Sextet}]`, so the sextets do not
couple to gluons — the original file only had it because it copied
Taylor's reference. That is a gap in our schema (nothing tells the agent a
non-fundamental colour representation needs that line), and I am fixing it
in the tooling. Smaller items: a heavy-neutrino class named `N` in one
EffLRSM run (a Protected Mathematica symbol, will not load); a factor ½ too
many on the Z_R–N–N current in the original-prompt EffLRSM runs, gone in
the addendum runs; and in General U(1) no run diagonalises the Z–Z′ mixing
or the portal-shifted minimum. Full list on the report page.

**The whole benchmark, re-run honestly.** I then re-ran all 28 models
sandboxed with the addendum. On the 9 models whose original run was clean,
the new pipeline scores higher on the fleet's own field-F1 metric
(0.77 vs 0.65); on the 18 whose original run had
read its own reference, the old 0.79 collapses to 0.56 — that old
number was the answer key. Per-model table on the report page. One of
the biggest drops turned out to be the benchmark's mistake, not the
agent's: the topBSM entry had paired arXiv 1305.7386 (Zhang & Maltoni's
t → qh EFT paper) with the heavy-resonance topBSM.fr, when the matching
reference is Krastanov's thu.fr in the same directory; the sandboxed agent
wrote the same O_uφ and O_uG operators the paper has and was scored 0 for
it. Fixed. MSSMD's pairing looks wrong too (its listed paper is a CMS
search) — worth a look from you or Konstantin.

**Compile chain.** Wolfram was re-activated (and FeynRules/MadGraph
reinstalled) the same day, and all 16 regenerated files went through
FeynRules → UFO → MadGraph. 5 of 16 pass end to end (all four Top-Philic
Z′ files and 368sextets v2/s1, which carries the explicit cutoffs *and*
six `CC[]` diquark bilinears — so the `CC[]` fix and `FS[]` on a singlet
vector both compile, which the readers had been unsure of). 13 of 16
compile in FeynRules. Every failure is a FeynRules/UFO convention the
paper never states, not a physics error:

- a pattern-rule `Definitions` on a tensor parameter (`YN[i_?NumericQ,
  j_?NumericQ] :> 0 /; i =!= j`) is exported verbatim as a UFO parameter
  named `YN1x1 /. YN`, and MadGraph fails with a misleading "invalid
  syntax (object_library.py, line 268)" — EffLRSM v1/s2, General U(1)
  v2/s1, and the original EffLRSM run;
- new scalar-potential couplings with no `InteractionOrder` come out
  with order `'1'`, which MadGraph refuses — General U(1) v1/s2 and
  v2/s2 (FeynRules and all three consistency checks pass);
- explicit indices where FeynRules wants matrix form —
  `Psiubar[ss].Ga[mu].DC[Psiu[ss], mu]` in both original-prompt
  368sextets seeds, `VCKMR[ff1,ff2] uqbar[ff1,cc].Ga[mu].ProjP.dq[ff2,cc]`
  in two EffLRSM seeds (your reference writes
  `uqbar.VCKMR.Ga[mu].ProjP.dq`) — make the UFO writer leak Mathematica
  internals into vertices.py;
- one General U(1) seed nests a generation index inside another and
  FeynRules stalls in the Hermiticity check; two 368sextets seeds stall
  even with a 60-minute budget — the Hermiticity check finds gluon–sextet
  vertices like {G, Phiu} that violate charge, from the explicit sextet
  index inside `DC[]` with no `AddGaugeRepresentation` (the same gap
  that leaves the passing seeds' sextets without gluon couplings).

One correction to the readers: the EffLRSM file with a class named `N`
does load, but all three consistency checks fail and its UFO has a
vertex with no particles — worse than a load failure. All of these go
into the schema and the next addendum.

The same pass over the 28-model sandboxed fleet: 11 of 28 pass the full
chain, 21 of 28 compile. The nine MadGraph rejections are the same
convention classes plus two new ones — a particle named `W'` (the prime
is not valid Python) and a field-free constant term that FeynRules
exports as a vertex with no particles. Two files crash FeynRules with
a recursion-limit error, one stalls, three define two total-Lagrangian
symbols so the harness refuses to guess, and one did not render. For
comparison the original fleet's 15 of 28 was first-shot on files that
had, in 18 cases, copied a reference that compiles.

Best,
Ken
