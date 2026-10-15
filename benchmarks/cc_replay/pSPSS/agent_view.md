# validate_model call 1/10: stage reached = checks

- compile: OK
- FeynRules check `hermiticity`: fail
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: pass
- MadGraph import: False

## Hermiticity: the non-zero vertices of L - HC[L]
Each row is a vertex that does not cancel against its conjugate. The usual cause is a term without its `+ HC[...]` partner, or a complex coefficient on a self-conjugate combination. `block` is the named Lagrangian term in model.fr whose expanded terms carry these fields (or their conjugates).

- vertex 1: fields W n4 ta n5 e mu; block: LmixW
  UNREDUCED: FeynRules could not strip n4, ta, n5, e, mu from this vertex; its coefficient still holds a spinor chain (Ga[0] from the conjugate). The usual cause is an explicit spin or flavour index on the spinors of that chain (see lint rule explicit_spin_in_chain); write the chain with implicit indices (`Xbar.Ga[mu].ProjP.Y`).
  coefficient: `(I*ee*(Conjugate[UnCL[Index[Generation, 3], Index[Neutrino, 4]]]*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . ta[Index[Spin, SP$1]] + Conjugate[UnCL[Index[Generation, 1], Index[Neutrino, 5]]]*n5[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . e[Index[Spin, SP$1]] + Conjugate[UnCL[Index[Generation, 2], Index[Neutrino, 5]]]*n5[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . mu[Index[Spin, SP$1]] + Conjugate[UnCL[Index[Generation, 3], Index[Neutrino, 5]]]*n5[Inde`
- vertex 2: fields Wbar ebar n4 n5 mubar tabar; block: LmixW
  UNREDUCED: FeynRules could not strip ebar, n4, n5, mubar, tabar from this vertex; its coefficient still holds a spinor chain (Ga[0] from the conjugate). The usual cause is an explicit spin or flavour index on the spinors of that chain (see lint rule explicit_spin_in_chain); write the chain with implicit indices (`Xbar.Ga[mu].ProjP.Y`).
  coefficient: `(I*ee*(ebar[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]]*UnCL[Index[Generation, 1], Index[Neutrino, 4]] - ebar[Index[Spin, SP$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . ProjP . n4[Index[Spin, SP$1]]*UnCL[Index[Generation, 1], Index[Neutrino, 4]] + ebar[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n5[Index[Spin, SP$1]]*UnCL[Index[Generation, 1], Index[Neutrino, 5]] - ebar[Index[Spin, SP$1]] . Ga[0] . Ga[Index[Lorentz, Ext[1]]] . Ga[0] . Proj`
- vertex 3: fields Z n4 n5 ve vm vt vebar vmbar vtbar; block: LmixZ
  UNREDUCED: FeynRules could not strip n4, n5, ve, vm, vt, vebar, vmbar, vtbar from this vertex; its coefficient still holds a spinor chain (Ga[0] from the conjugate). The usual cause is an explicit spin or flavour index on the spinors of that chain (see lint rule explicit_spin_in_chain); write the chain with implicit indices (`Xbar.Ga[mu].ProjP.Y`).
  coefficient: `((I/4)*ee*(thetasq*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n4[Index[Spin, SP$1]] + I*thetasq*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . n5[Index[Spin, SP$1]] + 2*Conjugate[UnCL[Index[Generation, 1], Index[Neutrino, 4]]]*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . ve[Index[Spin, SP$1]] + 2*Conjugate[UnCL[Index[Generation, 2], Index[Neutrino, 4]]]*n4[Index[Spin, SP$1]] . Ga[Index[Lorentz, Ext[1]]] . ProjM . vm[Index[Spin, SP$1]] + 2*Conjugate`

## MadGraph import: where the UFO breaks, and the model.fr lines behind it

### `UFO/couplings.py` line 642, object `GC_158`: unterminated string literal (detected at line 642)
```
GC_158 = Coupling(name = 'GC_158',
                  value = 'ReplaceAll((ee*complex(0,1)*UnCL1x4*Dot(n4(-1),Gamma(1),ProjM,e(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL2x4*Dot(n4(-1),Gamma(1),ProjM,mu(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL3x4*Dot(n4(-1),Gamma(1),ProjM,ta(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL1x5*Dot(n5(-1),Gamma(1),ProjM,e(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL2x5*Dot(n5(-1),Gamma(1),ProjM,mu(-1)))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UnCL3x5*Dot(n5(-1),Gamma(1),ProjM,ta(-1)))/(sw*cmath.sqrt(2)),Rule(Ext(Dot(n4(-1),Gamma(1),ProjM,e(-1)),Pattern(opt,BlankNullSequence())),Ext(List,opt),Ext(Slot(2),Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt),Ext(2,Pattern(opt,BlankNullSequence())),Ext(Slot(3),opt)))',
                  order = {'                    I ee UnCL1x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . e[Index[Spin, Int[1]]]   I ee UnCL2x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . mu[Index[Spin, Int[1]]]   I ee UnCL3x4 n4[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]] . L$ProjM . ta[Index[Spin, Int[1]]]   I ee UnCL1x5 n5[Index[Spin, Int[1]]] . L$Ga[Index[Lorentz, Ext[1]]
```
Vertex particles using this coupling: W__minus__
model.fr lines:
- line 148 (declaration): `UnCL == {`
  ```
    UnCL == {
      ParameterType    -> Internal,
      BlockName        -> PSPSS,
      Indices          -> {Index[Generation], Index[Neutrino]},
      InteractionOrder -> {NP, 1},
      Value            -> {
        UnCL[1, 1] -> 1 - thetasq/2,  UnCL[1, 2] -> -theta1 theta2/2,  UnCL[1, 3] -> -theta1 theta3/2,  UnCL[1, 4] -> -I theta1/Sqrt[2],  UnCL[1, 5] -> theta1/Sqrt[2],
        UnCL[2, 1] -> -theta2 theta1/2,  UnCL[2, 2] -> 1 - thetasq/2,  UnCL[2, 3] -> -theta2 theta3/2,  UnCL[2, 4] -> -I theta2/Sqrt[2],  UnCL[2, 5] -> theta2/Sqrt[2],
        UnCL[3, 1] -> -theta3 theta1/2,  UnCL[3, 2] -> -theta3 theta2/2,  UnCL[3, 3] -> 1 - thetasq/2,  UnCL[3, 4] -> -I theta3/Sqrt[2],  UnCL[3, 5] -> theta3/Sqrt[2]
      },
      Description      -> "upper 3x5 block U'_CL of U_n (active-sterile mixing matrix, paper eq.(29)), used for the index contraction of the mixed W and Z couplings"
    }
  ```
- line 168 (declaration): `ClassName       -> n4,`
- line 180 (declaration): `ClassName       -> n5,`
- line 288 (use): `(UnCL[ff1, 4] lbar[sp, ff1].Ga[mu].ProjM.n4[sp] + UnCL[ff1, 5] lbar[sp, ff1].Ga[mu].ProjM.n5[sp]) Wbar[mu]`
- line 289 (use): `+ (Conjugate[UnCL[ff1, 4]] n4bar[sp].Ga[mu].ProjM.l[sp, ff1] + Conjugate[UnCL[ff1, 5]] n5bar[sp].Ga[mu].ProjM.l[sp, ff1]) W[mu]`
- line 299 (use): `+ I thetasq/2 n4bar[sp].Ga[mu].ProjM.n5[sp]`

### `UFO/vertices.py` line 616, object `V_101`: closing parenthesis ')' does not match opening parenthesis '[' on line 613
```
V_101 = Vertex(name = 'V_101',
               particles = [ P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[anti[MakeIdenticalFermions[#1]] & ]], P.<>CreateObjectParticleName[PartNameMG[3]], P.W__minus__, P.<>CreateObjectParticleName[PartNameMG[3]] ],
               color = [ '1' ],
               lorentz = [ L.<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1 ],
               couplings = {(0,-1 + PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>PRIVATE`ConvertSpinToString[0]<>V<>PRIVATE`ConvertSpinToString[0]<>1):C.GC_158})

```
model.fr lines:
- line 158 (use): `Description      -> "upper 3x5 block U'_CL of U_n (active-sterile mixing matrix, paper eq.(29)), used for the index contraction of the mixed W and Z couplings"`
- line 288 (use): `(UnCL[ff1, 4] lbar[sp, ff1].Ga[mu].ProjM.n4[sp] + UnCL[ff1, 5] lbar[sp, ff1].Ga[mu].ProjM.n5[sp]) Wbar[mu]`
- line 289 (use): `+ (Conjugate[UnCL[ff1, 4]] n4bar[sp].Ga[mu].ProjM.l[sp, ff1] + Conjugate[UnCL[ff1, 5]] n5bar[sp].Ga[mu].ProjM.l[sp, ff1]) W[mu]`

## lint findings
lint: 15 finding(s)
- [mg5] explicit_spin_in_chain (line 288): `lbar[sp]` and `n4[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`lbar.Ga[mu].n4`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 288): `lbar[sp]` and `n5[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`lbar.Ga[mu].n5`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 289): `n4bar[sp]` and `l[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`n4bar.Ga[mu].l`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 289): `n5bar[sp]` and `l[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`n5bar.Ga[mu].l`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 297): `n4bar[sp]` and `n4[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`n4bar.Ga[mu].n4`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 298): `n5bar[sp]` and `n5[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`n5bar.Ga[mu].n5`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 299): `n4bar[sp]` and `n5[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`n4bar.Ga[mu].n5`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 300): `n5bar[sp]` and `n4[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`n5bar.Ga[mu].n4`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 301): `vlbar[sp]` and `n4[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`vlbar.Ga[mu].n4`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 301): `n4bar[sp]` and `vl[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`n4bar.Ga[mu].vl`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 302): `vlbar[sp]` and `n5[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`vlbar.Ga[mu].n5`) or thread it through the matrix
- [mg5] explicit_spin_in_chain (line 302): `n5bar[sp]` and `vl[sp, ...]` carry the same explicit spin index with a Dirac matrix between them; drop the explicit spin index (`n5bar.Ga[mu].vl`) or thread it through the matrix
- [checks] mixing_in_definitions (line None): class `N1L` is defined as a mixture of ['n4', 'n5']; the mass basis of the partner fields declared in SM.fr is unchanged
- [checks] mixing_in_definitions (line None): class `N2L` is defined as a mixture of ['n4', 'n5']; the mass basis of the partner fields declared in SM.fr is unchanged
- [checks] mixing_in_definitions (line None): class `nL` is defined as a mixture of ['n4', 'n5', 'vl']; the mass basis of the partner fields declared in SM.fr is unchanged
