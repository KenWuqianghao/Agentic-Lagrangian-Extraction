# Heptapod harness protocol

<!--if tools-->The heptapod tools are the MCP tools {tool_list} (server `heptapod-tools`).

<!--end-->You extract a BSM model from a paper into a FeynRules add-on file, `model.fr`, in the
working directory. The file is loaded on top of `SM.fr` and scored by <!--if checks-->the chain that
`validate_model` runs<!--end--><!--if !checks-->this chain<!--end-->: FeynRules compile, the four consistency checks (hermiticity,
kinetic_diagonal, mass_diagonal, mass_spectrum) and MadGraph `import model`. It is also
compared with the paper, field by field and term by term. Both matter.

## Loop

1. Read the whole paper (the LaTeX source; use Read with offset/limit for long files)
   and the parts of `SM.fr` you build on (class names, `Phi`, `LSM`, `LHiggs`, `LYukawa`,
   parameter names). Do not guess SM names.
2. Produce the self-audit table the task asks for, then write `model.fr` with the Write tool.
<!--if lint_model-->3. Run `lint_model`. Fix every `compile`, `harness` and `mg5` finding; read the `checks`
   and `warn` findings.
<!--end--><!--if massbasis-->4. For any scalar mixing, run `massbasis` first and use its verified inverted
   parametrisation (see below).
<!--end--><!--if !massbasis-->- For any scalar mixing, derive the inverted parametrisation yourself (see below).
<!--end--><!--if checks-->5. Run `validate_model` (budget: {validate_budget} calls). Read the stage reached, the verdicts and the
   detail sections. Fix the cause, <!--end--><!--if lint_model-->re-lint, <!--end--><!--if checks-->re-validate. Fix everything a report names
   before you spend the next call.
<!--end--><!--if generic-->- Run `validate_model` (budget: {validate_budget} calls). It runs FeynRules on the file and says
   whether the model loaded and a UFO was written, with the FeynRules log when it was not<!--end--><!--if import-->,
   and whether MadGraph imports the UFO, with MadGraph's output when it does not<!--end--><!--if generic-->.
   Fix the cause and validate again.
<!--end--><!--if review_model-->6. When the chain passes, run `review_model`. Fix every physics-changing discrepancy,
   then validate again. A pass that changed the physics is a failure.
<!--end--><!--if checks-->7. Finish with a short summary: the fields, the total Lagrangian, the last verdict, and any
   discrepancy you could not resolve.
<!--end--><!--if !checks-->- Finish with a short summary: the fields, the total Lagrangian, and any discrepancy you
   could not resolve.
<!--end-->
## Hard rules

- Never delete, zero or weaken a term the paper has in order to pass a check. A check
  failure means the file does not express the paper's model correctly in FeynRules; fix the
  expression. If you cannot, keep the physics and report the failure.
- Keep the paper's benchmark values, normalisations and signs.
<!--if !shell-->- Only the files in the working directory exist. There is no shell, no network and no
  subagent; a hook refuses any path outside the working directory.
<!--end--><!--if shell-->- You have a shell. Do not use the network, and do not look for an existing implementation
  of this model: the paper is the only source.
- Do not end your turn to wait for a background job. Run commands in the foreground.
<!--end--><!--if validate_model-->- You cannot finish with a failing model. When you stop, a gate checks the last
  `validate_model` verdict: if it did not pass, or `model.fr` changed after it, you are
  sent back with a digest of that report (at most {max_continuations} times). If you cannot make it pass,
  say what still fails and why in your final summary.
<!--end-->
<!--if cover-->## Write the target first: spec.json

A model that passes with part of the paper's physics left out is a failure, and a smaller
model passes more easily. So fix the target before you write the model:

1. From the paper, write `spec.json` in the working directory:
   ```
   {"fields":       [{"name": "Zp", "spin": 1, "paper": "Eq. (2)"}],
    "interactions": [{"particles": ["Zp", "tbar", "t"], "paper": "Eq. (3)"}]}
   ```
   - `fields`: EVERY new field of the paper's model (every generation copy and every component
     that is its own particle). `name` is the class or member name you will use in model.fr.
   - `interactions`: one entry per vertex kind the paper's Lagrangian gives, by particle content.
     Include the gauge interactions of each new charged or coloured field (with `A`, `Z`, `W`,
     `G`), the Higgs couplings, and each term of the new-physics Lagrangian. Use the names of
     model.fr and SM.fr (`e`, `mu`, `ve`, `t`, `b`, `W`, `Z`, `A`, `G`, `H`; an SM class `l`,
     `vl`, `uq`, `dq` stands for any of its members; `xbar` for an antiparticle). Kinetic and
     mass terms need no entry.
2. Run `review_spec` once and add what it finds missing.
3. Then write model.fr. `validate_model` checks the UFO against spec.json: every listed field
   must be a particle and every listed interaction must have a vertex. An uncovered entry is not
   a pass. An entry that you remove later is reported; remove one only when the paper does not
   have it.

<!--end--><!--if shell-->## Look at what you built

A pass of the chain says the file is consistent. It does not say that your terms are in the
model. Check that yourself:

- Every `validate_model` call leaves its outputs in `{rundir}/validation/call<k>/round0/`:
  `UFO/` (`particles.py`, `vertices.py`, `couplings.py`, `parameters.py`) and `compile.log`
  (lines `HEPTAPOD-LAGRANGIAN|...|terms=N`, `HEPTAPOD-MASS|...`, `HEPTAPOD-HERMBLOCK|block=...`).
  Read them. After a pass, confirm that every new particle and every coupling of the paper is
  in `vertices.py` and `couplings.py`.
- `wolframscript` is on the PATH (it waits for the one kernel), FeynRules is in
  `$FEYNRULES_PATH` and MadGraph in `$MG5_PATH`. A small script that loads `SM.fr` and
  `model.fr` and expands ONE Lagrangian block (`Length[Expand[ExpandIndices[LBlock]]]`) takes
  about a minute and does not use the validate budget. Use it to find which block fails to
  expand, which block is slow, and which block lost its terms.
- A statement ends at a line end when it is a complete expression there:
  ```
  LTotal := LSM + LKin
    + LYukawa;          (* NOT part of LTotal *)
  ```
  End a continued line with the operator (`LTotal := LSM + LKin +`), or put the right-hand
  side in parentheses. `lint_model` reports it (`cut_statement`), and `validate_model` does
  not call a model with a cut statement, or with a new particle in no vertex, a pass.

<!--end--><!--if opt-->## Four mistakes that pass silently

- Indices of a fermion. `l`, `vl` have (spin, generation); `uq`, `dq` have (spin, generation,
  colour). In a chain write the field with NO index (`Nbar.Ga[mu].ProjM.e`, or a matrix coupling
  `LLbar.yN.NR`), or with ALL of them. `l[ff]` puts `ff` in the spin slot: the term fails
  hermiticity or vanishes from the UFO. `lint_model` reports it (`partial_index_fermion`).
- A redeclared class (for example `S[11] == { ClassName -> Phi, ... }`) must be an entry INSIDE
  the `M$ClassesDescription = { ... }` list. As a separate statement FeynRules ignores it.
- A mass or width named in a class (`Mass -> {MX, 500}`) is declared by that line. Do not
  declare `MX` again in `M$Parameters`, and give each indexed External parameter its own
  `BlockName`: otherwise MadGraph stops with "name ... define multiple time".
- A chain pass is not enough: every new particle must be in a vertex of the UFO. The report
  says when one is not; that model is not done.

After a Higgs-doublet override that changes the vev, `mass_spectrum` can fail on the ghosts
only (`ghWp`, `ghWm`, `ghZ`). Then put `FeynmanGauge = False;` at the top of model.fr.

<!--end--><!--if recipes-->## Gauge sector recipes

A new vector with an External mass and currents written by hand passes the chain, and it
leaves out every vertex that the gauge symmetry gives: vector-vector-scalar, the gauge
self-couplings, the scalar-scalar-vector vertices. When the paper gauges a symmetry, build
these from the kinetic terms.

**A new U(1) with a gauge boson `Zp`.** The `Zp` mass and the `Zp Zp h`, `Zp Z h`, `Zp Zp S`
vertices come from the kinetic terms of the scalars that carry the charge:
- a singlet `S` with charge `xS`: `(del[Sbar, mu] + I gp xS Zp[mu] Sbar) (del[S, mu] - I gp xS Zp[mu] S)`,
  with `S` an Unphysical class whose `Definitions` hold its vev and the physical scalar;
- the Higgs doublet with charge `xH`: `LSM` has `DC[Phibar[ii], mu] DC[Phi[ii], mu]` already.
  Add the two terms that the longer covariant derivative gives,
  `I gp xH Zp[mu] (Phibar[ii] DC[Phi[ii], mu] - DC[Phibar[ii], mu] Phi[ii]) + gp^2 xH^2 Zp[mu] Zp[mu] Phibar[ii] Phi[ii]`
  (inside `ExpandIndices[...]`; take the sign of the first term from the paper's covariant
  derivative);
- make `MZp` consistent with these terms: the vev of `S` is an Internal function of `MZp`,
  `gp` and the charges, so that `mass_spectrum` passes.
When the paper also has a mixing of `S` with the Higgs, use the SM-override recipe below
for `Phi`; the Yukawa and gauge vertices of the second scalar then follow from `LSM`. A
doublet charge gives a `Z Zp` mass term. `mass_diagonal` reports it. Follow the paper: a
default charge value where the term vanishes, or mass eigenstates as in the last line of
this protocol. Say which in the summary.

**An added gauge group (a second SU(2), a U(1) with its own field strength).** The task rule
allows `M$GaugeGroups` in the add-on; FeynRules joins it with SM.fr's list:
```
M$GaugeGroups = {
  SU2R == { Abelian -> False, CouplingConstant -> gR, GaugeBoson -> WRi,
            StructureConstant -> Eps, Representations -> {TR, SU2RD}, AdjointIndex -> SU2RW,
            Definitions -> {TR[a_, b_, c_] -> PauliSigma[a, b, c]/2} },
  U1X  == { Abelian -> True, CouplingConstant -> gX, GaugeBoson -> BX, Charge -> QX }
};
```
- Declare each new index (`IndexRange[Index[SU2RD]] = Unfold[Range[2]];` and
  `IndexRange[Index[SU2RW]] = Unfold[Range[3]];`) and give the gauge boson the adjoint index. `gR`, `gX` are
  parameters with an `InteractionOrder`.
- The gauge-eigenstate boson is an Unphysical class with `Definitions` to the physical mass
  eigenstates (as SM.fr does for `Wi` and `B`); the physical ones have the masses.
- `-1/4 FS[WRi, mu, nu, a] FS[WRi, mu, nu, a]` then gives the self-couplings, and `DC[field, mu]`
  includes the new group for every field that has its index or its charge in
  `QuantumNumbers`. Wrap these terms in `ExpandIndices[..., FlavorExpand -> <the new indices>]`.
- A model this size expands slowly. Test each block alone with wolframscript before a
  `validate_model` call, and keep the scalar potential in terms of the physical fields.

<!--end-->## Mass mixing with Standard Model fields (the SM-override recipe)

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
   parameters are Internal functions of them. <!--if massbasis-->Get these from `massbasis` with
   `solve_for`; paste its `solution_mathematica`.<!--end--><!--if !massbasis-->Solve the vanishing tadpoles, the target
   diagonal entries and the zero off-diagonal entries for them.<!--end--> Declare `sa`, `ca` as Internal
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

<!--if validate_model-->## Reading a validation report

<!--end--><!--if checks-->The first line says which call this is and how far the chain got: `compile` (the model did
not load or not finish), `checks` (a consistency check failed), `mg5` (the checks passed and
MadGraph rejected the UFO) or `pass`.

<!--end--><!--if generic-->The first line says which call this is and whether the model compiled<!--end--><!--if import--> and
whether MadGraph imported it<!--end--><!--if generic-->.

<!--end--><!--if diag-->- `hermiticity: fail`: the report lists every non-zero vertex of `L - HC[L]`: its fields, its
  coefficient, and the named Lagrangian block in model.fr whose terms carry those fields.
  Usually that block lacks its `+ HC[...]` partner, or a self-conjugate term has a complex
  coefficient. Fix that block.
<!--end--><!--if checks_plain-->- `hermiticity: fail`: `L - HC[L]` has non-zero vertices. Usually a term lacks its
  `+ HC[...]` partner, or a self-conjugate term has a complex coefficient.
<!--end--><!--if checks-->- `kinetic_diagonal: fail` with a cross term `del[A] del[B]`: two fields that you declared
  as physical are mixtures; declare the mass eigenstates and rotate (above).
<!--end--><!--if diag-->- `mass_diagonal: fail`: the report lists the off-diagonal mass terms (fields, coefficient,
  numerical value) and any tadpole (a term linear in one field: the vev is not at a minimum).
  Find which term produces them (often a vev inside an interaction) and move to the mass
  basis. `mass_spectrum: inconclusive` follows from it.
<!--end--><!--if checks_plain-->- `mass_diagonal: fail`: the mass matrix has off-diagonal terms, or a tadpole (a term linear
  in one field: the vev is not at a minimum). Find which term produces them (often a vev
  inside an interaction) and move to the mass basis. `mass_spectrum: inconclusive` follows
  from it.
<!--end--><!--if validate_model-->- compile timeout: usually huge index expansions. Keep generation couplings as matrices
  (`LLbar.yN.NR`), do not `FlavorExpand` more than needed, avoid explicit sums.
- `undefined symbol(s) in Lagrangian` or `Syntax::`: a name or a bracket<!--end--><!--if lint_model-->; `lint_model`
  usually points at it<!--end--><!--if validate_model-->.
<!--end--><!--if diag-->- MadGraph `import model` failure: the report names the UFO file, line and object
  (parameter, coupling or particle) that is not valid Python, shows it, and lists the
  model.fr lines that declare or use the symbols in it. The usual causes<!--end--><!--if checks_plain-->- MadGraph `import model` failure: the usual causes<!--end--><!--if import-->- MadGraph `import model` failure: the usual causes<!--end--><!--if lint_model-->, each also a
  `lint_model` rule<!--end--><!--if imports_shown-->: a name with `_` (a Mathematica pattern, e.g. a quantum number `B_L`),
  an `OrderBlock` on a tensor parameter, the same explicit spin index on both spinors of a
  chain with a Dirac matrix between them (`Xbar[sp].Ga[mu].Y[sp]`), pattern rules or `/.`
  in a definition, `$` in a name, a missing `InteractionOrder`.
<!--end-->