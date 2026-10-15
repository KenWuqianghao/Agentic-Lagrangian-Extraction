# validate_model call 1/10: stage reached = checks

- compile: OK
- FeynRules check `hermiticity`: fail
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False

## Hermiticity: the non-zero vertices of L - HC[L]
Each row is a vertex that does not cancel against its conjugate. The usual cause is a term without its `+ HC[...]` partner, or a complex coefficient on a self-conjugate combination. `block` is the named Lagrangian term in model.fr whose expanded terms carry these fields (or their conjugates).

- vertex 1: fields WRbar lbar NR1 b c d NR2 NR3; block: LWRlepton, LWRquark, LWRkin
  UNREDUCED: FeynRules could not strip lbar, NR1, b, c, d, NR2, NR3 from this vertex; its coefficient still holds a spinor chain (Ga[0] from the conjugate). The usual cause is an explicit spin or flavour index on the spinors of that chain (see lint rule explicit_spin_in_chain); write the chain with implicit indices (`Xbar.Ga[mu].ProjP.Y`).
  coefficient: `((-1/2*I)*ee*kappaRell*(Conjugate[Ymix[Index[Generation, 1], Index[Generation, 1]]]*(lbar[Index[Spin, a]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1*Ga[0, r$18608, 1] + lbar[Index[Spin, b]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[5] . NR1*Ga[0, r$18609, 1] - lbar[Index[Spin, c]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . NR1*Ga[0, r$22487, Index[Spin, 1]] - lbar[Index[Spin, d]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[5] . NR1*Ga[0, r$22488, Index[Spin, 1]]) + Conjugate[Ymix[Index[Generation, 2],`
- vertex 2: fields WR NR1 l b c d NR2 NR3; block: LWRlepton, LWRquark, LWRkin
  UNREDUCED: FeynRules could not strip NR1, l, b, c, d, NR2, NR3 from this vertex; its coefficient still holds a spinor chain (Ga[0] from the conjugate). The usual cause is an explicit spin or flavour index on the spinors of that chain (see lint rule explicit_spin_in_chain); write the chain with implicit indices (`Xbar.Ga[mu].ProjP.Y`).
  coefficient: `((-1/2*I)*ee*kappaRell*(NR1 . Ga[Index[Lorentz, Ext[1]]] . l[Index[Spin, 1]]*Ymix[Index[Generation, 1], Index[Generation, 1]] + NR1 . Ga[Index[Lorentz, Ext[1]]] . Ga[5] . l[Index[Spin, 1]]*Ymix[Index[Generation, 1], Index[Generation, 1]] - NR1 . Ga[Index[Lorentz, Ext[1]]] . l[Index[Spin, a]]*Ga[0, 1, r$18608]*Ga[0, Index[Spin, b], r$22415]*Ymix[Index[Generation, 1], Index[Generation, 1]] - NR1 . Ga[Index[Lorentz, Ext[1]]] . Ga[5] . l[Index[Spin, c]]*Ga[0, 1, r$18609]*Ga[0, Index[Spin, d], r$2241`

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/couplings.py` line 694, object `GC_171`: unterminated string literal (detected at line 694)
```
GC_171 = Coupling(name = 'GC_171',
                  value = 'ReplaceAll(-0.5*(ee*complex(0,1)*kappaRell*Dot(lbar(-1),Gamma(0),Gamma(1),NR1)*complexconjugate(Ymix1x1)*Gamma(0,r$18608,1))/(sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-2),Gamma(0),Gamma(1),Gamma5(),NR1)*complexconjugate(Ymix1x1)*Gamma(0,r$18609,1))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-1),Gamma(0),Gamma(1),NR2)*complexconjugate(Ymix2x2)*Gamma(0,r$18610,2))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-2),Gamma(0),Gamma(1),Gamma5(),NR2)*complexconjugate(Ymix2x2)*Gamma(0,r$18611,2))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-1),Gamma(0),Gamma(1),NR3)*complexconjugate(Ymix3x3)*Gamma(0,r$18612,3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*kappaRell*Dot(lbar(-2),Gamma(0),Gamma(1),Gamma5(),NR3)*complexconjugate(Ymix3x3)*Gamma(0,r$18613,3))/(2.*sw*cmath.sqrt(2)),Rule(Ext(Dot(lbar(-1),Gamma(0),Gamma(1),NR1),Pattern(opt,BlankNullSequence())),Ext(List,opt),Ext(Slot(2),Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt),Ext(2,Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt)))',
                  order = {'                       1                                 
```
Vertex particles using this coupling: wr__plus__
model.fr lines:
- line 95 (declaration): `ClassName       -> NR1,`
- line 107 (declaration): `ClassName       -> NR2,`
- line 119 (declaration): `ClassName       -> NR3,`
- line 166 (declaration): `kappaRell == {`
  ```
    kappaRell == {
      ParameterType    -> External,
      BlockName        -> EFFLRSM,
      OrderBlock       -> 4,
      Value            -> 1.,
      InteractionOrder -> {NP, 1},
      TeX              -> Superscript[kappa, R^l],
      Description      -> "Overall normalization of the WR/ZR coupling to leptons, Eq.(2), Eq.(neucurrent)"
    },
  ```
- line 223 (declaration): `Ymix == {`
  ```
    Ymix == {
      ParameterType    -> External,
      BlockName        -> EFFLRSM,
      OrderBlock       -> 8,
      InteractionOrder -> {NP, 1},
      Indices          -> {Index[Generation], Index[Generation]},
      Value            -> {Ymix[1,1] -> 1, Ymix[1,2] -> 0, Ymix[1,3] -> 0,
                            Ymix[2,1] -> 0, Ymix[2,2] -> 1, Ymix[2,3] -> 0,
                            Ymix[3,1] -> 0, Ymix[3,2] -> 0, Ymix[3,3] -> 1},
      TeX              -> Superscript[Y, N],
      Description      -> "Y_{l m'}: mixing of the heavy neutrino mass eigenstate N_{m'} with the RH state of lepton flavor l, Eq.(lrsmNuMixing); Ymix[N-index, l-index]"
    },
  ```
- line 302 (use): `LNmass := -1/2 MN1 NR1bar.NR1 - 1/2 MN2 NR2bar.NR2 - 1/2 MN3 NR3bar.NR3;`

### `UFO/parameters.py` line 90, object `Ymix1x1`: positional argument follows keyword argument
```
Ymix1x1 = Parameter(name = 'Ymix1x1',
                    nature = 'external',
                    type = 'complex',
                    value = 1,
                    texname = '\\text{Ymix1x1}',
                    lhablock = 'EFFLRSM',
ClassAttributeCreation[lhacode, PYList[{1, 1} /. 8], 20]<>)

```
model.fr lines:
- line 223 (declaration): `Ymix == {`
  ```
    Ymix == {
      ParameterType    -> External,
      BlockName        -> EFFLRSM,
      OrderBlock       -> 8,
      InteractionOrder -> {NP, 1},
      Indices          -> {Index[Generation], Index[Generation]},
      Value            -> {Ymix[1,1] -> 1, Ymix[1,2] -> 0, Ymix[1,3] -> 0,
                            Ymix[2,1] -> 0, Ymix[2,2] -> 1, Ymix[2,3] -> 0,
                            Ymix[3,1] -> 0, Ymix[3,2] -> 0, Ymix[3,3] -> 1},
      TeX              -> Superscript[Y, N],
      Description      -> "Y_{l m'}: mixing of the heavy neutrino mass eigenstate N_{m'} with the RH state of lepton flavor l, Eq.(lrsmNuMixing); Ymix[N-index, l-index]"
    },
  ```
- line 229 (use): `Value            -> {Ymix[1,1] -> 1, Ymix[1,2] -> 0, Ymix[1,3] -> 0,`
- line 230 (use): `Ymix[2,1] -> 0, Ymix[2,2] -> 1, Ymix[2,3] -> 0,`
- line 231 (use): `Ymix[3,1] -> 0, Ymix[3,2] -> 0, Ymix[3,3] -> 1},`
- line 233 (use): `Description      -> "Y_{l m'}: mixing of the heavy neutrino mass eigenstate N_{m'} with the RH state of lepton flavor l, Eq.(lrsmNuMixing); Ymix[N-index, l-index]"`
- line 319 (use): `the current is therefore omitted.  Ymix is kept as a parameter`

### `UFO/vertices.py` line 580, object `V_95`: closing parenthesis ')' does not match opening parenthesis '[' on line 577
```
V_95 = Vertex(name = 'V_95',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[3]], P.wr__plus__, P.<>CreateObjectParticleName[PartNameMG[3]] ],
              color = [ '1' ],
              lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1 ],
              couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_171})

```
model.fr lines: none matched the symbols (no model symbol in this object)

## lint findings
lint: 15 finding(s)
- [mg5] tensor_orderblock (line 223): parameter `Ymix` has Indices and an OrderBlock; FeynRules numbers the components of a tensor itself, and the explicit OrderBlock is written unevaluated into parameters.py. Remove the OrderBlock line
- [mg5] tensor_orderblock (line 235): parameter `Xmix` has Indices and an OrderBlock; FeynRules numbers the components of a tensor itself, and the explicit OrderBlock is written unevaluated into parameters.py. Remove the OrderBlock line
- [mg5] tensor_orderblock (line 235): parameter `Xmix` has Indices and an OrderBlock; FeynRules numbers the components of a tensor itself, and the explicit OrderBlock is written unevaluated into parameters.py. Remove the OrderBlock line
- [checks] numeric_spin_slot (line 325): `l[1]`: the first index of the fermion `l` is its spin index, so `1` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 1]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 325): `l[1]`: the first index of the fermion `l` is its spin index, so `1` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 1]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 326): `l[2]`: the first index of the fermion `l` is its spin index, so `2` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 2]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 326): `l[2]`: the first index of the fermion `l` is its spin index, so `2` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 2]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 327): `l[3]`: the first index of the fermion `l` is its spin index, so `3` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 3]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 327): `l[3]`: the first index of the fermion `l` is its spin index, so `3` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 3]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 330): `l[1]`: the first index of the fermion `l` is its spin index, so `1` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 1]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 330): `l[1]`: the first index of the fermion `l` is its spin index, so `1` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 1]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 331): `l[2]`: the first index of the fermion `l` is its spin index, so `2` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 2]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 331): `l[2]`: the first index of the fermion `l` is its spin index, so `2` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 2]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 332): `l[3]`: the first index of the fermion `l` is its spin index, so `3` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 3]` with the spin index threaded) or none
- [checks] numeric_spin_slot (line 332): `l[3]`: the first index of the fermion `l` is its spin index, so `3` is read as a spin index, not a generation; FeynRules cannot reduce the spinor chain and hermiticity fails. Give every index (`l[sp, 3]` with the spin index threaded) or none
