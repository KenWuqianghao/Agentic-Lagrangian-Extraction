# validate_model call 1/10: stage reached = checks

- compile: OK
- FeynRules check `hermiticity`: fail
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False

## Hermiticity: the non-zero vertices of L - HC[L]
Each row is a vertex that does not cancel against its conjugate. The usual cause is a term without its `+ HC[...]` partner, or a complex coefficient on a self-conjugate combination. `block` is the named Lagrangian term in model.fr whose expanded terms carry these fields (or their conjugates).

- vertex 1: fields Nnubar e G0 GP; block: LG0GP
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(Sqrt[2]*MW^2*sw^2)`
- vertex 2: fields Nnubar e GP H; block: LNGP
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*Sqrt[2]*MW^2*sw^2)`
- vertex 3: fields Nnubar e GP; block: LNGP
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*Sqrt[2]*MW*sw)`
- vertex 4: fields Nnubar mu G0 GP; block: LG0GP
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(Sqrt[2]*MW^2*sw^2)`
- vertex 5: fields Nnubar mu GP H; block: LNGP
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*Sqrt[2]*MW^2*sw^2)`
- vertex 6: fields Nnubar mu GP; block: LNGP
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*Sqrt[2]*MW*sw)`
- vertex 7: fields Nnubar ta G0 GP; block: LG0GP
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(Sqrt[2]*MW^2*sw^2)`
- vertex 8: fields Nnubar ta GP H; block: LNGP
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*Sqrt[2]*MW^2*sw^2)`
- vertex 9: fields Nnubar ta GP; block: LNGP
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*Sqrt[2]*MW*sw)`
- vertex 10: fields Nnubar ve G0; block: LNG0
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 11: fields Nnubar ve G0 H; block: LNG0
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*MW^2*sw^2)`
- vertex 12: fields Nnubar ve H; block: LNh
  coefficient: `((-1/4*I)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 13: fields Nnubar ve G0; block: LNG0
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*MW*sw)`
- vertex 14: fields Nnubar ve H; block: LNh
  coefficient: `((-1/2*I)*ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW*sw)`
- vertex 15: fields Nnubar vm G0; block: LNG0
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 16: fields Nnubar vm G0 H; block: LNG0
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*MW^2*sw^2)`
- vertex 17: fields Nnubar vm H; block: LNh
  coefficient: `((-1/4*I)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 18: fields Nnubar vm G0; block: LNG0
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*MW*sw)`
- vertex 19: fields Nnubar vm H; block: LNh
  coefficient: `((-1/2*I)*ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW*sw)`
- vertex 20: fields Nnubar vt G0; block: LNG0
  coefficient: `((I/4)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 21: fields Nnubar vt G0 H; block: LNG0
  coefficient: `(ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(4*MW^2*sw^2)`
- vertex 22: fields Nnubar vt H; block: LNh
  coefficient: `((-1/4*I)*ee^2*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW^2*sw^2)`
- vertex 23: fields Nnubar vt G0; block: LNG0
  coefficient: `(ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(2*MW*sw)`
- vertex 24: fields Nnubar vt H; block: LNh
  coefficient: `((-1/2*I)*ee*MNu*ProjM[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(MW*sw)`
- vertex 25: fields ebar Nnu G0 GPbar; block: LG0GP
  coefficient: `((-1/4*I)*ee^2*MNu*ProjP[Index[Spin, Ext[1]], Index[Spin, Ext[2]]])/(Sqrt[2]*MW^2*sw^2)`
- ... 35 more vertices

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/parameters.py` line 42, object `Cll1x1`: positional argument follows keyword argument
```
Cll1x1 = Parameter(name = 'Cll1x1',
                   nature = 'external',
                   type = 'complex',
                   value = 0.,
                   texname = '\\text{Cll1x1}',
                   lhablock = 'NUPHYSICS',
ClassAttributeCreation[lhacode, PYList[{1, 1} /. 2], 19]<>)

```
model.fr lines:
- line 56 (declaration): `Cll == {`
  ```
    Cll == {
      ParameterType    -> External,
      BlockName        -> NUPHYSICS,
      OrderBlock       -> 2,
      Indices          -> {Index[Generation], Index[Generation]},
      Value            -> {
        Cll[1, 1] -> 0., Cll[1, 2] -> 0., Cll[1, 3] -> 0.,
        Cll[2, 1] -> 0., Cll[2, 2] -> 1., Cll[2, 3] -> 0.,
        Cll[3, 1] -> 0., Cll[3, 2] -> 0., Cll[3, 3] -> 0.
      },
      InteractionOrder -> {NP, 1},
      Description      -> "Weinberg operator Wilson coefficients C5^{ll'} (dimensionless), paper Eq.(dim5Lag); benchmark C5^{mu mu} = 1, all others 0"
    },
  ```
- line 62 (use): `Cll[1, 1] -> 0., Cll[1, 2] -> 0., Cll[1, 3] -> 0.,`
- line 63 (use): `Cll[2, 1] -> 0., Cll[2, 2] -> 1., Cll[2, 3] -> 0.,`
- line 64 (use): `Cll[3, 1] -> 0., Cll[3, 2] -> 0., Cll[3, 3] -> 0.`
- line 75 (use): `Value         -> Abs[Cll[1, 1] + Cll[1, 2] + Cll[1, 3] + Cll[2, 1] + Cll[2, 2] + Cll[2, 3] + Cll[3, 1] + Cll[3, 2] + Cll[3, 3]] vev^2/Lambda,`

## lint findings
lint: 1 finding(s)
- [mg5] tensor_orderblock (line 56): parameter `Cll` has Indices and an OrderBlock; FeynRules numbers the components of a tensor itself, and the explicit OrderBlock is written unevaluated into parameters.py. Remove the OrderBlock line
