# Heptapod harness protocol

The heptapod tools are the MCP tools `lint_model`, `validate_model`, `massbasis` and `review_model` (server `heptapod-tools`).

You extract a BSM model from a paper into a FeynRules add-on file, `model.fr`, in the
working directory. The file is loaded on top of `SM.fr` and scored by the chain that
`validate_model` runs: FeynRules compile, the four consistency checks (hermiticity,
kinetic_diagonal, mass_diagonal, mass_spectrum) and MadGraph `import model`. It is also
compared with the paper, field by field and term by term. Both matter.

## Loop

1. Read the whole paper (the LaTeX source; use Read with offset/limit for long files)
   and the parts of `SM.fr` you build on (class names, `Phi`, `LSM`, `LHiggs`, `LYukawa`,
   parameter names). Do not guess SM names.
2. Produce the self-audit table the task asks for, then write `model.fr` with the Write tool.
3. Run `lint_model`. Fix every `compile`, `harness` and `mg5` finding; read the `checks`
   and `warn` findings.
4. For any scalar mixing, run `massbasis` first and use its verified inverted
   parametrisation (see below).
5. Run `validate_model` (budget: 10 calls). Read the stage reached, the verdicts and the
   detail sections. Fix the cause, re-lint, re-validate. Fix everything a report names
   before you spend the next call.
6. When the chain passes, run `review_model`. Fix every physics-changing discrepancy,
   then validate again. A pass that changed the physics is a failure.
7. Finish with a short summary: the fields, the total Lagrangian, the last verdict, and any
   discrepancy you could not resolve.

## Hard rules

- Never delete, zero or weaken a term the paper has in order to pass a check. A check
  failure means the file does not express the paper's model correctly in FeynRules; fix the
  expression. If you cannot, keep the physics and report the failure.
- Keep the paper's benchmark values, normalisations and signs.
- Only the files in the working directory exist. There is no shell, no network and no
  subagent; a hook refuses any path outside the working directory.
- You cannot finish with a failing model. When you stop, a gate checks the last
  `validate_model` verdict: if it did not pass, or `model.fr` changed after it, you are
  sent back with a digest of that report (at most 3 times). If you cannot make it pass,
  say what still fails and why in your final summary.

## Mass mixing with Standard Model fields (the SM-override recipe)

The dominant failure of plain one-shot extraction is `mass_diagonal` (with
`mass_spectrum` then inconclusive): a new scalar mixes with the SM Higgs, a Z' mixes with
the Z, a heavy neutrino mixes with the active ones. The add-on cannot rotate a field that
`SM.fr` declares unless it redeclares it. This works and passes the full chain:

1. Redeclare the SM class with the SAME class, index and names SM.fr uses, and put the
   rotation in its `Definitions`, with SM.fr's physical field names (`H`, `G0`, `GP`) and
   SM.fr's `vev`:
   ```
   S[11] == { ClassName -> Phi, Unphysical -> True, Indices -> {Index[SU2D]},
     FlavorIndex -> SU2D, SelfConjugate -> False, QuantumNumbers -> {Y -> 1/2},
     Definitions -> { Phi[1] -> -I GP, Phi[2] -> (vev + ca H - sa H2 + I G0)/Sqrt[2] } }
   ```
   The new CP-even mass eigenstate (`H2`) is a new physical class; the singlet is an
   `Unphysical` class whose `Definitions` use the same angle (`sa H + ca H2`).
2. Replace the SM term you override rather than adding a second copy: the SM potential
   lives in `LHiggs`, so write the whole scalar potential (SM part included) in your own
   term and declare
   `LTotal := LSM - LHiggs + LScalar + <other new terms>;`
   (the harness adds `LSM` only when your total does not reach it; here it does).
   `LSM`'s Yukawa and gauge terms then use your redeclared `Phi` automatically.
3. Write the potential's couplings as Internal parameters in the INVERTED
   parametrisation: physical masses (SM.fr's `MH` for the SM-like state, your new mass
   symbol for the other) and the mixing angle are External; the quartics and the mass
   parameters are Internal functions of them. Get these from `massbasis` with
   `solve_for`; paste its `solution_mathematica`. Declare `sa`, `ca` as Internal
   (`Sin[alpha]`, `Cos[alpha]`) of an External angle. Then the quadratic terms are
   diagonal symbolically and `mass_diagonal` and `mass_spectrum` pass.
4. Masses in `Mass -> {M, value}` must equal what the Lagrangian's quadratic terms
   produce; `mass_spectrum` compares them.

Heavy neutrinos that mix with the active ones (seesaw, `N`, `NR`): writing
`LLbar.yN.NR Phi` with the vev in `Phi` produces a Dirac mass term `vev yN nubar N` that is
not diagonal. Two consistent ways, choose the one closest to the paper:
- work in the mass basis the way the FeynRules database's HeavyN models do: declare the
  heavy mass eigenstates `N` with their masses, and write the active-heavy mixing as
  couplings `V_lN` in the W, Z and Higgs currents (`lbar.Ga[mu].ProjM.N W[mu]` with
  `gw/Sqrt[2] VlN`, the Z and h analogues), with the paper's mixing expressed through its
  parameters (for example `VlN = yN vev/(Sqrt[2] MN)`); say so in the summary;
- or redeclare the SM lepton doublet class the same way as `Phi` above, which is much
  harder; prefer the first.
A Z-Z' or W-W' mixing is handled the same way as the scalar case: the mass eigenstates
are the physical classes, the gauge eigenstates are Unphysical with `Definitions`.

## Reading a validation report

The first line says which call this is and how far the chain got: `compile` (the model did
not load or not finish), `checks` (a consistency check failed), `mg5` (the checks passed and
MadGraph rejected the UFO) or `pass`.

- `hermiticity: fail`: the report lists every non-zero vertex of `L - HC[L]`: its fields, its
  coefficient, and the named Lagrangian block in model.fr whose terms carry those fields.
  Usually that block lacks its `+ HC[...]` partner, or a self-conjugate term has a complex
  coefficient. Fix that block.
- `kinetic_diagonal: fail` with a cross term `del[A] del[B]`: two fields that you declared
  as physical are mixtures; declare the mass eigenstates and rotate (above).
- `mass_diagonal: fail`: the report lists the off-diagonal mass terms (fields, coefficient,
  numerical value) and any tadpole (a term linear in one field: the vev is not at a minimum).
  Find which term produces them (often a vev inside an interaction) and move to the mass
  basis. `mass_spectrum: inconclusive` follows from it.
- compile timeout: usually huge index expansions. Keep generation couplings as matrices
  (`LLbar.yN.NR`), do not `FlavorExpand` more than needed, avoid explicit sums.
- `undefined symbol(s) in Lagrangian` or `Syntax::`: a name or a bracket; `lint_model`
  usually points at it.
- MadGraph `import model` failure: the report names the UFO file, line and object
  (parameter, coupling or particle) that is not valid Python, shows it, and lists the
  model.fr lines that declare or use the symbols in it. The usual causes, each also a
  `lint_model` rule: a name with `_` (a Mathematica pattern, e.g. a quantum number `B_L`),
  an `OrderBlock` on a tensor parameter, the same explicit spin index on both spinors of a
  chain with a Dirac matrix between them (`Xbar[sp].Ga[mu].Y[sp]`), pattern rules or `/.`
  in a definition, `$` in a name, a missing `InteractionOrder`.
