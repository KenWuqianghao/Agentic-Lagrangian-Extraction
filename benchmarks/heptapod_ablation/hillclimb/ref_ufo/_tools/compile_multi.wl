(* Multi-file variant of heptapod's UFO_generator.wl, which loads one model file.
   Called by run.py --multi:
     wolframscript -f compile_multi.wl FeynRulesPath=DIR ModelFiles=a.fr,b.fr OutputDir=DIR
       Lagrangian=EXPR [FeynmanGauge=true|false] [ExpandIndices=true|false]
   Prints "[INFO] Done." and exits 0 when the UFO has all its files. *)
frxParams = Association @ Map[Rule @@ StringSplit[#, "=", 2] &, Rest[$ScriptCommandLine]];
$FeynRulesPath = frxParams["FeynRulesPath"];
frxFiles = StringSplit[frxParams["ModelFiles"], ","];
frxOut = frxParams["OutputDir"];
frxLag = frxParams["Lagrangian"];
Get[FileNameJoin[{$FeynRulesPath, "FeynRules.m"}]];
Print["[INFO] Loading model files: ", frxFiles];
LoadModel @@ frxFiles;
If[KeyExistsQ[frxParams, "FeynmanGauge"],
  FeynmanGauge = (ToLowerCase[frxParams["FeynmanGauge"]] === "true");
  Print["[INFO] FeynmanGauge set by caller: ", FeynmanGauge]];
$LTot = If[ToLowerCase[Lookup[frxParams, "ExpandIndices", "true"]] === "true",
  ExpandIndices[ToExpression[frxLag]], ToExpression[frxLag]];
Print["[INFO] Lagrangian: ", frxLag, "  FeynmanGauge=", TrueQ[FeynmanGauge],
      "  terms=", Length[Expand[$LTot]]];
WriteUFO[$LTot, Output -> frxOut, AddDecays -> False];
frxReq = {"particles.py", "vertices.py", "couplings.py", "parameters.py", "coupling_orders.py"};
frxMiss = Select[frxReq, !FileExistsQ[FileNameJoin[{frxOut, #}]] &];
If[Length[frxMiss] > 0, Print["Error: UFO is incomplete; missing ", frxMiss]; Quit[2]];
Print["[INFO] UFO complete: ", StringRiffle[frxReq, ", "], " all present."];
Print["[INFO] Done."];
Quit[0];
