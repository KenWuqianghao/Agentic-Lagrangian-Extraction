# validate_model call 1/10: stage reached = mg5

- compile: OK
- FeynRules check `hermiticity`: pass
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/couplings.py` line 630, object `GC_155`: unterminated string literal (detected at line 630)
```
GC_155 = Coupling(name = 'GC_155',
                  value = 'ReplaceAll(-0.5*(ee*complex(0,1)*VlN1*Dot(vebar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2))*ProjM(-1,-2))/(cw*sw) - (ee*complex(0,1)*VlN2*Dot(vmbar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2))*ProjM(-1,-2))/(2.*cw*sw) - (ee*complex(0,1)*VlN3*Dot(vtbar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2))*ProjM(-1,-2))/(2.*cw*sw) - (ee*complex(0,1)*Dot(NRbar(-1),Gamma(1),ve(-2))*complexconjugate(VlN1)*ProjP(-1,-2))/(2.*cw*sw) - (ee*complex(0,1)*Dot(NRbar(-1),Gamma(1),vm(-2))*complexconjugate(VlN2)*ProjP(-1,-2))/(2.*cw*sw) - (ee*complex(0,1)*Dot(NRbar(-1),Gamma(1),vt(-2))*complexconjugate(VlN3)*ProjP(-1,-2))/(2.*cw*sw),Rule(Ext(PRIVATExdummylist(Part(List(List(Z,1)),Dot(vebar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2))),Part(List(List(Z,1)),PRIVATExhold(SP$1,SP$2))),Pattern(opt,BlankNullSequence())),Ext(Dot(vebar(-1),Gamma(0),Gamma(1),Gamma(0),NR(-2)),opt),Ext(Slot(2),Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt),Ext(2,Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt)))',
                  order = {'                       1                                                                                                                              
```
Vertex particles using this coupling: Z, ve
model.fr lines:
- line 25 (declaration): `ClassName        -> NR,`
- line 54 (declaration): `VlN == {`
  ```
    VlN == {
      ParameterType    -> External,
      Indices          -> {Index[Generation]},
      Value            -> {VlN[1] -> 10.*^-3, VlN[2] -> 0., VlN[3] -> 0.},
      BlockName        -> HNEUTRINO,
      OrderBlock       -> 1,
      InteractionOrder -> {NP, 1},
      TeX              -> Subscript[V, lN],
      Description      -> "Active-heavy neutrino mixing V_lN, Eq. (7) of arXiv:1602.06957"
    }
  ```
- line 73 (use): `-(gw/(2 cw)) Z[mu] Conjugate[VlN[ff]] NLbar[sp].Ga[mu].vl[sp, ff]`
- line 81 (use): `-(mN/vev) Conjugate[VlN[ff]] (H + I G0) NRrbar[sp].vl[sp, ff]`
- line 42 (use): `Definitions    -> { NL[sp1_] :> Module[{sp2}, ProjM[sp1, sp2] NR[sp2]] }`
- line 48 (use): `Definitions    -> { NRr[sp1_] :> Module[{sp2}, ProjP[sp1, sp2] NR[sp2]] }`

### `UFO/parameters.py` line 34, object `VlN1`: positional argument follows keyword argument
```
VlN1 = Parameter(name = 'VlN1',
                 nature = 'external',
                 type = 'complex',
                 value = 0.01,
                 texname = '\\text{VlN1}',
                 lhablock = 'HNEUTRINO',
ClassAttributeCreation[lhacode, PYList[{1} /. 1], 17]<>)

```
model.fr lines:
- line 54 (declaration): `VlN == {`
  ```
    VlN == {
      ParameterType    -> External,
      Indices          -> {Index[Generation]},
      Value            -> {VlN[1] -> 10.*^-3, VlN[2] -> 0., VlN[3] -> 0.},
      BlockName        -> HNEUTRINO,
      OrderBlock       -> 1,
      InteractionOrder -> {NP, 1},
      TeX              -> Subscript[V, lN],
      Description      -> "Active-heavy neutrino mixing V_lN, Eq. (7) of arXiv:1602.06957"
    }
  ```
- line 57 (use): `Value            -> {VlN[1] -> 10.*^-3, VlN[2] -> 0., VlN[3] -> 0.},`
- line 73 (use): `-(gw/(2 cw)) Z[mu] Conjugate[VlN[ff]] NLbar[sp].Ga[mu].vl[sp, ff]`
- line 81 (use): `-(mN/vev) Conjugate[VlN[ff]] (H + I G0) NRrbar[sp].vl[sp, ff]`

### `UFO/vertices.py` line 688, object `V_113`: closing parenthesis ')' does not match opening parenthesis '[' on line 685
```
V_113 = Vertex(name = 'V_113',
               particles = [ P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[ve[Index[Spin, SP$1]]]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[3]], P.Z, P.<>CreateObjectParticleName[PartNameMG[3]] ],
               color = [ '1' ],
               lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>F<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1 ],
               couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>F<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_155})

```
model.fr lines:
- line 73 (use): `-(gw/(2 cw)) Z[mu] Conjugate[VlN[ff]] NLbar[sp].Ga[mu].vl[sp, ff]`
- line 81 (use): `-(mN/vev) Conjugate[VlN[ff]] (H + I G0) NRrbar[sp].vl[sp, ff]`

## lint findings
lint: 2 finding(s)
- [mg5] tensor_orderblock (line 54): parameter `VlN` has Indices and an OrderBlock; FeynRules numbers the components of a tensor itself, and the explicit OrderBlock is written unevaluated into parameters.py. Remove the OrderBlock line
- [mg5] explicit_spin_in_chain (line 73): `NLbar[sp]` and `vl[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`NLbar.Ga[mu].vl`) or thread it through the matrix
