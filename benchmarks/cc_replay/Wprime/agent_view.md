# validate_model call 1/10: stage reached = mg5

- compile: OK
- FeynRules check `hermiticity`: pass
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/parameters.py` line 90, object `WpLeR1`: positional argument follows keyword argument
```
WpLeR1 = Parameter(name = 'WpLeR1',
                   nature = 'external',
                   type = 'complex',
                   value = 1.,
                   texname = '\\text{WpLeR1}',
                   lhablock = 'WPRIME',
ClassAttributeCreation[lhacode, PYList[{1} /. 7], 19]<>)

```
model.fr lines:
- line 128 (declaration): `WpLeR == {`
  ```
    WpLeR == {
      ParameterType    -> External,
      BlockName        -> WPRIME,
      OrderBlock       -> 7,
      Indices          -> {Index[Generation]},
      InteractionOrder -> {NP, 1},
      TeX              -> "V^R_{l nu}",
      Value -> {
        WpLeR[1] -> 1., WpLeR[2] -> 1., WpLeR[3] -> 1.
      },
      Description -> "Couplings of W' to charged leptons and the right-handed neutrino NR; paper: V'_{l nu} is the identity"
    },
  ```
- line 136 (use): `WpLeR[1] -> 1., WpLeR[2] -> 1., WpLeR[3] -> 1.`
- line 251 (use): `gRp Eom CZ WpLeR NRbar.Ga[mu].ProjP.l +`

## lint findings
lint: 4 finding(s)
- [mg5] tensor_orderblock (line 100): parameter `WpQqR` has Indices and an OrderBlock; FeynRules numbers the components of a tensor itself, and the explicit OrderBlock is written unevaluated into parameters.py. Remove the OrderBlock line
- [mg5] tensor_orderblock (line 114): parameter `WpQqL` has Indices and an OrderBlock; FeynRules numbers the components of a tensor itself, and the explicit OrderBlock is written unevaluated into parameters.py. Remove the OrderBlock line
- [mg5] tensor_orderblock (line 128): parameter `WpLeR` has Indices and an OrderBlock; FeynRules numbers the components of a tensor itself, and the explicit OrderBlock is written unevaluated into parameters.py. Remove the OrderBlock line
- [mg5] tensor_orderblock (line 140): parameter `WpLeL` has Indices and an OrderBlock; FeynRules numbers the components of a tensor itself, and the explicit OrderBlock is written unevaluated into parameters.py. Remove the OrderBlock line
