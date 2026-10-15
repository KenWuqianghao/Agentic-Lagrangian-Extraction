# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: OK
- FeynRules check `hermiticity`: pass
- FeynRules check `kinetic_diagonal`: pass
- FeynRules check `mass_diagonal`: pass
- FeynRules check `mass_spectrum`: fail
- MadGraph import: False
- Heuristic error tags: mass_spectrum_fail, mg5_import_fail, mg5_python_traceback

## FeynRules check `mass_spectrum`: fail
Masses computed from the Lagrangian disagree with the declared values by more than 0.1%. Update the `Mass` entry in the particle class, or fix the mass term it is meant to match. (Neglecting all terms with more than 2 particles. All mass terms are diagonal. Getting mass spectrum. Checking for less then 0.1% agreement with model file values.)

## FeynRules / Wolfram Engine output (tail)
```
not conserved in vertex {H, N1bar, e}.
Quantum number Q not conserved in vertex {H, N1bar, mu}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, mu}.
Quantum number Q not conserved in vertex {H, N1bar, ta}.
Quantum number LeptonNumber not conserved in vertex {H, N1bar, ta}.
Quantum number Q not conserved in vertex {H, N2bar, e}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, e}.
Quantum number Q not conserved in vertex {H, N2bar, mu}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, mu}.
Quantum number Q not conserved in vertex {H, N2bar, ta}.
Quantum number LeptonNumber not conserved in vertex {H, N2bar, ta}.
Quantum number Q not conserved in vertex {H, N3bar, e}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, e}.
Quantum number Q not conserved in vertex {H, N3bar, mu}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, mu}.
Quantum number Q not conserved in vertex {H, N3bar, ta}.
Quantum number LeptonNumber not conserved in vertex {H, N3bar, ta}.
Quantum number Q not conserved in vertex {GPbar, vebar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vebar, N1}.
Quantum number Q not conserved in vertex {GPbar, vebar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vebar, N2}.
Quantum number Q not conserved in vertex {GPbar, vebar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vebar, N3}.
Quantum number Q not conserved in vertex {GPbar, vmbar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vmbar, N1}.
Quantum number Q not conserved in vertex {GPbar, vmbar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vmbar, N2}.
Quantum number Q not conserved in vertex {GPbar, vmbar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vmbar, N3}.
Quantum number Q not conserved in vertex {GPbar, vtbar, N1}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vtbar, N1}.
Quantum number Q not conserved in vertex {GPbar, vtbar, N2}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vtbar, N2}.
Quantum number Q not conserved in vertex {GPbar, vtbar, N3}.
Quantum number LeptonNumber not conserved in vertex {GPbar, vtbar, N3}.
Quantum number Q not conserved in vertex {G0, ebar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, ebar, N1}.
Quantum number Q not conserved in vertex {G0, ebar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, ebar, N2}.
Quantum number Q not conserved in vertex {G0, ebar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, ebar, N3}.
Quantum number Q not conserved in vertex {G0, mubar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, mubar, N1}.
Quantum number Q not conserved in vertex {G0, mubar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, mubar, N2}.
Quantum number Q not conserved in vertex {G0, mubar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, mubar, N3}.
Quantum number Q not conserved in vertex {G0, tabar, N1}.
Quantum number LeptonNumber not conserved in vertex {G0, tabar, N1}.
Quantum number Q not conserved in vertex {G0, tabar, N2}.
Quantum number LeptonNumber not conserved in vertex {G0, tabar, N2}.
Quantum number Q not conserved in vertex {G0, tabar, N3}.
Quantum number LeptonNumber not conserved in vertex {G0, tabar, N3}.
Quantum number Q not conserved in vertex {H, ebar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, ebar, N1}.
Quantum number Q not conserved in vertex {H, ebar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, ebar, N2}.
Quantum number Q not conserved in vertex {H, ebar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, ebar, N3}.
Quantum number Q not conserved in vertex {H, mubar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, mubar, N1}.
Quantum number Q not conserved in vertex {H, mubar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, mubar, N2}.
Quantum number Q not conserved in vertex {H, mubar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, mubar, N3}.
Quantum number Q not conserved in vertex {H, tabar, N1}.
Quantum number LeptonNumber not conserved in vertex {H, tabar, N1}.
Quantum number Q not conserved in vertex {H, tabar, N2}.
Quantum number LeptonNumber not conserved in vertex {H, tabar, N2}.
Quantum number Q not conserved in vertex {H, tabar, N3}.
Quantum number LeptonNumber not conserved in vertex {H, tabar, N3}.
Preparing Python output.
    - Splitting vertices into building blocks.
Splitting of vertices distributed over 8 kernels.
    - Optimizing: Dynamic[PRIVATE`PY$SplitVertexCounter]/281 .
    - Writing files.
Warning: Non positive interaction order QED.
                This might reduce the efficiency of certain matrix element generators.
                See logfile for more details.
Done!
[INFO] UFO complete: particles.py, vertices.py, couplings.py, parameters.py, coupling_orders.py all present.
[INFO] Done.

```

## MadGraph import output (tail)
```
mport_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
[1;31mCommand "import /private/tmp/repair_corrected/GeneralU1/round1/mg5run/mg5_import.txt" interrupted in sub-command:
"import model /tmp/repair_corrected/GeneralU1/round1/UFO" with error:
UFOError : invalid syntax (object_library.py, line 268)
Please report this bug on https://bugs.launchpad.net/mg5amcnlo
More information is found in 'MG5_debug'.
Please attach this file to your report.[0m

```

## MG5_debug (the real MadGraph error)
```
5_aMC/models/import_ufo.py", line 611, in load_model
    self.add_interaction(interaction_info, color_info)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 1840, in add_interaction
    raise InvalidModel('''Some couplings have \'1\' order.
    This is not allowed in MG.
    Please defines an additional coupling to your model''')
models.import_ufo.InvalidModel: Some couplings have '1' order. 
                    This is not allowed in MG. 
                    Please defines an additional coupling to your model

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1570, in onecmd
    return self.onecmd_orig(line, **opt)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1519, in onecmd_orig
    return func(arg, **opt)
  File "/Users/kenwu/MG5_aMC/madgraph/interface/master_interface.py", line 281, in do_import
    self.cmd.do_import(self, *args, **opts)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/madgraph_interface.py", line 5893, in do_import
    self.import_command_file(args[1])
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1718, in import_command_file
    self.exec_cmd(line, precmd=True)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1599, in exec_cmd
    stop = Cmd.onecmd_orig(current_interface, line, **opt)
  File "/Users/kenwu/MG5_aMC/madgraph/interface/extended_cmd.py", line 1519, in onecmd_orig
    return func(arg, **opt)
  File "/Users/kenwu/MG5_aMC/madgraph/interface/master_interface.py", line 281, in do_import
    self.cmd.do_import(self, *args, **opts)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/madgraph/interface/madgraph_interface.py", line 5835, in do_import
    raise err
  File "/Users/kenwu/MG5_aMC/madgraph/interface/madgraph_interface.py", line 5819, in do_import
    self._curr_model = import_ufo.import_model(args[1], prefix=prefix,
                       ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
        complex_mass_scheme=self.options['complex_mass_scheme'],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        options=options)
        ^^^^^^^^^^^^^^^^
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 251, in import_model
    model = import_full_model(model_path, decay, prefix)
  File "/Users/kenwu/MG5_aMC/models/import_ufo.py", line 413, in import_full_model
    ufo_model = ufomodels.load_model(model_path, decay)
  File "/Users/kenwu/MG5_aMC/models/__init__.py", line 101, in load_model
    raise UFOError(str(error))
models.UFOError: invalid syntax (object_library.py, line 268)
Fail to write options with error No model currently active, please import a model!
```
