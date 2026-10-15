#!/usr/bin/env wolframscript
(* ============ Mass matrix of a FeynRules model, as data ============ *)
(*
   Usage:
     wolframscript -f massmatrix.wl FeynRulesPath=<dir> ModelPath=<model.fr> \
        Lagrangian="LSM + LBSM" Output=<out.json> [FeynmanGauge=true|false]

   Loads SM.fr and the model exactly as tools/feynrules/UFO_generator.wl does,
   expands the same total, and writes what CheckDiagonalMassTerms,
   CheckDiagonalKineticTerms and CheckMassSpectrum look at, as JSON:

     mass_terms      every two-field term without a derivative, grouped by
                     field content (the grouping FeynRules' checks use), with
                     the coefficient in InputForm, split by chiral projector,
                     and its numerical value at the model's parameter point
     kinetic_offdiag two-field derivative terms between different fields
                     (scalar-vector gauge-fixing pairs dropped, as the check does)
     tadpoles        one-field terms without a derivative
     fields          spin, anti-field, declared mass symbol and value
     parameters      numerical value of every parameter the coefficients use

   The zero test is FeynRules' own: |NumericalValue| < 10^-8.
*)

ClearAll["Global`*"];
params = Association @ Map[Rule @@ StringSplit[#, "=", 2] &, Rest[$ScriptCommandLine]];
$FeynRulesPath = params["FeynRulesPath"];
$ModelPath = params["ModelPath"];
$Out = params["Output"];
$LagrangianSpec = params["Lagrangian"];
$Gauge = Lookup[params, "FeynmanGauge", None];

Get[FileNameJoin[{$FeynRulesPath, "FeynRules.m"}]];
smFR = FileNameJoin[{$FeynRulesPath, "Models", "SM", "SM.fr"}];
LoadModel[smFR, $ModelPath];
If[$Gauge =!= None, FeynmanGauge = (ToLowerCase[$Gauge] === "true")];
$LTot = ExpandIndices[ToExpression[$LagrangianSpec]];
Print["[MM] Lagrangian loaded: ", $LagrangianSpec];

zero[x_] := TrueQ[Abs[x] < N[10^-8]];
num[x_] := Module[{v = Quiet[NumericalValue[x]]},
  If[NumericQ[v], v = N[v]; {Re[v], Im[v]}, Null]];
istr[x_] := ToString[x, InputForm];
bare[f_] := If[AtomQ[f], f, Head[f]];
spinOf[f_] := Which[
  GhostFieldQ[f] === True, "U",
  ScalarFieldQ[f] === True, "S",
  VectorFieldQ[f] === True, "V",
  MajoranaFieldQ[f] === True, "M",
  DiracFieldQ[f] === True, "F",
  True, "?"];

(* Coefficient of a group of terms: fields set to 1, spinor chains flattened,
   chiral projectors kept as symbols so a Dirac mass matrix keeps its L and R
   parts. mmP multiplies P_R, mmM multiplies P_L. *)
coefOf[t_] := Module[{c},
  c = t //. {FR$deltat[xx_] -> FR$deltat[xx], psi_?FieldQ -> 1};
  c = c //. {Dot[a___, 1, b___] :> Dot[a, b]} /. {Dot[] -> 1};
  c = c //. {ProjP[__] -> mmP, ProjM[__] -> mmM, Ga[5][__] -> mmG5, Ga[5, __] -> mmG5};
  c = c /. Dot -> Times;
  Expand[c]];

groupTerms[lag_] := Module[{l, fcl, keys},
  l = Expand[lag];
  If[l === 0, Return[{}]];
  l = If[Head[l] === Plus, List @@ l, {l}];
  fcl = Sort /@ (GetFieldContent /@ l);
  keys = DeleteDuplicates[fcl];
  Table[{k, Plus @@ Pick[l, (# === k &) /@ fcl]}, {k, keys}]];

allFields = {};
paramSyms = {};
noteParams[e_] := (paramSyms = Union[paramSyms,
   Cases[e, s_Symbol /; (Context[s] === "Global`" && NumericQ[Quiet[NumericalValue[s]]]), {0, Infinity}]]);

record[{k_, t_}] := Module[{c, c0, cP, cM, cG, chalf, fs},
  fs = bare /@ k;
  allFields = Union[allFields, fs];
  c = coefOf[t];
  c0 = c /. {mmP -> 0, mmM -> 0, mmG5 -> 0};
  cP = Coefficient[c, mmP]; cM = Coefficient[c, mmM]; cG = Coefficient[c, mmG5];
  chalf = c /. {mmP -> 1/2, mmM -> 1/2, mmG5 -> 0};
  noteParams[c];
  <|"fields" -> (istr /@ fs), "spins" -> (spinOf /@ fs),
    "coefficient" -> istr[chalf], "numeric" -> num[chalf],
    "zero" -> zero[Quiet[NumericalValue[chalf]]],
    "no_projector" -> istr[c0], "P_R" -> istr[cP], "P_L" -> istr[cM], "gamma5" -> istr[cG],
    "numeric_no_projector" -> num[c0], "numeric_P_R" -> num[cP], "numeric_P_L" -> num[cM],
    "diagonal" -> (fs[[1]] === anti[fs[[2]]] || fs[[1]] === fs[[2]])|>];

t0 = AbsoluteTime[];
mass = record /@ groupTerms[GetMassTerms[$LTot, FlavorExpand -> True]];
Print["[MM] mass terms: ", Length[mass], " groups, ", Round[AbsoluteTime[] - t0], " s"];

kin = groupTerms[GetKineticTerms[$LTot, FlavorExpand -> True]];
kin = DeleteCases[kin, {{_?ScalarFieldQ, _?VectorFieldQ} | {_?VectorFieldQ, _?ScalarFieldQ}, _}];
kin = Select[kin, (bare[#[[1, 1]]] =!= anti[bare[#[[1, 2]]]] && bare[#[[1, 1]]] =!= bare[#[[1, 2]]]) &];
kinRec = Map[Function[{g}, Module[{v, fs = bare /@ g[[1]]},
    allFields = Union[allFields, fs];
    v = g[[2]] //. del[psi_, mu_] -> psi //. psi_?FieldQ -> 1 //.
        TensDot[Ga[_], ProjM | ProjP][_, _] -> 1/2 //. Ga[__] -> 1 //. (ProjP | ProjM)[_, _] -> 1/2;
    noteParams[v];
    <|"fields" -> (istr /@ fs), "term" -> istr[g[[2]]], "numeric" -> num[v],
      "zero" -> zero[Quiet[NumericalValue[v]]]|>]], kin];
Print["[MM] off-diagonal kinetic groups: ", Length[kinRec]];

lin = Quiet[ExpandIndices[$LTot, FlavorExpand -> True, MaxParticles -> 1, MinParticles -> 1]];
lin = Select[If[Head[Expand[lin]] === Plus, List @@ Expand[lin], {Expand[lin]}], FreeQ[#, del] &];
tad = Map[Function[{g}, Module[{v, fs = bare /@ g[[1]]},
    v = g[[2]] //. psi_?FieldQ -> 1; noteParams[v];
    <|"field" -> istr[fs[[1]]], "coefficient" -> istr[v], "numeric" -> num[v],
      "zero" -> zero[Quiet[NumericalValue[v]]]|>]],
   If[lin === {0} || lin === {}, {}, groupTerms[Plus @@ lin]]];
Print["[MM] tadpole groups: ", Length[tad]];

fieldInfo = Association @ Map[
   istr[#] -> <|"spin" -> spinOf[#], "anti" -> TrueQ[AntiFieldQ[#]],
      "class" -> istr[If[TrueQ[AntiFieldQ[#]], anti[#], #]],
      "mass_symbol" -> istr[Quiet[Mass[If[TrueQ[AntiFieldQ[#]], anti[#], #]]]],
      "mass_value" -> num[Quiet[Mass[If[TrueQ[AntiFieldQ[#]], anti[#], #]]]]|> &,
   allFields];
paramVals = Association @ Map[istr[#] -> num[#] &, paramSyms];

res = <|"model" -> $ModelPath, "lagrangian" -> $LagrangianSpec,
   "feynman_gauge" -> TrueQ[FeynmanGauge],
   "mass_terms" -> mass, "kinetic_offdiag" -> kinRec, "tadpoles" -> tad,
   "fields" -> fieldInfo, "parameters" -> paramVals,
   "seconds" -> Round[AbsoluteTime[] - t0]|>;
Export[$Out, res, "RawJSON"];
Print["[MM] Done. ", $Out];
