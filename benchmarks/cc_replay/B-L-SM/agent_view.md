# validate_model call 1/10: stage reached = mg5

- compile: OK
- FeynRules check `hermiticity`: pass
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/particles.py` line 25, object `a`: NameError: name 'B_L' is not defined
```
a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0,
             B_L = (B_L)[A])

```
model.fr lines:
- line 252 (use): `QuantumNumbers  -> {B_L -> 2},`
- line 267 (use): `QuantumNumbers   -> {B_L -> -1, LeptonNumber -> 1},`

## lint findings
lint: 7 finding(s)
- [mg5] pattern_symbol_name (line 252): quantum number `B_L` contains `_`, which makes it a Mathematica pattern; FeynRules writes it into particles.py as `B_L = (B_L)[...]` and the UFO does not import. Rename it without the underscore (e.g. `BL`)
- [mg5] pattern_symbol_name (line 267): quantum number `B_L` contains `_`, which makes it a Mathematica pattern; FeynRules writes it into particles.py as `B_L = (B_L)[...]` and the UFO does not import. Rename it without the underscore (e.g. `BL`)
- [checks] mixing_in_definitions (line None): class `chi` is defined as a mixture of ['G02', 'H', 'HH']; the mass basis of the partner fields declared in SM.fr is unchanged
- [checks] mixing_in_definitions (line None): class `Phi` is defined as a mixture of ['G0', 'GP', 'H', 'HH']; the mass basis of the partner fields declared in SM.fr is unchanged
- [warn] sm_class_redeclared (line None): class `Phi` is already declared by SM.fr (doubly-defined class) -- allowed only with the SM-override recipe: keep SM.fr's names and write the total as LSM - L<replaced SM term> + ...
- [warn] low_class_index (line 279): class `Phi` uses index S[11]; SM.fr uses the low indices
- [warn] explicit_index_in_dc (line 305): `LScalar`: covariant derivative on an explicitly indexed field `Phibar`
