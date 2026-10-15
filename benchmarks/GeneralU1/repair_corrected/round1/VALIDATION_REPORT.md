# Validation report — model.fr FAILED the tool chain

- FeynRules UFO compile: FAILED
- FeynRules check `hermiticity`: not reached
- FeynRules check `kinetic_diagonal`: not reached
- FeynRules check `mass_diagonal`: not reached
- FeynRules check `mass_spectrum`: not reached
- MadGraph import: not reached
- Heuristic error tags: lag_symbol_undefined, fr_syntax_error, builtin_symbol_collision, selfconjugate_quantum_numbers

## FeynRules / Wolfram Engine output (tail)
```
                                                                                                                                                   ^". (line 233 of "/private/tmp/claude-501/-Users-kenwu-Documents-Github-Agentic-Lagrangian-Extraction/94cf8ff6-6dba-453e-b8ee-ad80d63999c8/scratchpad/hmain/eval/benchmark_runs/GeneralU1/repair_corrected/round0/model.fr")

General::stop: Further output of Syntax::sntx will be suppressed during this calculation.
From kernel 7 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 2 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 6 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 1 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 2 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.
From kernel 5 (Local):
LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.
From kernel 2 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.

General::stop: Further output of Warning: Selfconjugated fields should not carry quantumnumbers. will be suppressed during this calculation.
From kernel 7 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.
From kernel 2 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.
From kernel 3 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.
From kernel 4 (Local):
Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.

General::stop: Further output of Format::nosym will be suppressed during this calculation.
From kernel 2 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.
From kernel 7 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.
From kernel 2 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.
From kernel 3 (Local):
N::argt: N called with 3 arguments; 1 or 2 arguments are expected.

General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 2 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 7 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 3 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 4 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.
From kernel 5 (Local):
General::stop: Further output of N::argt will be suppressed during this calculation.

General::stop: Further output of Further output of `1` will be suppressed during this calculation. will be suppressed during this calculation.
Merging model-files...

Syntax::sntx: Invalid syntax in or before "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^". (line 233 of "/private/tmp/claude-501/-Users-kenwu-Documents-Github-Agentic-Lagrangian-Extraction/94cf8ff6-6dba-453e-b8ee-ad80d63999c8/scratchpad/hmain/eval/benchmark_runs/GeneralU1/repair_corrected/round0/model.fr")
This model implementation was created by
Arindam Das
P. S. Bhupal Dev
Yutaka Hosotani
Sanjoy Mandal
Model Version: 1.0
For more information, type ModelInformation[].

   - Loading particle classes.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.

Format::nosym: PRIVATE`ii$__ does not contain a symbol to attach a rule to.

N::argt: N called with 3 arguments; 1 or 2 arguments are expected.

N::argt: N called with 3 arguments; 1 or 2 arguments are expected.

N::argt: N called with 3 arguments; 1 or 2 arguments are expected.

General::stop: Further output of N::argt will be suppressed during this calculation.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

LoadModel::QN: Warning: Selfconjugated fields should not carry quantumnumbers.

General::stop: Further output of LoadModel::QN will be suppressed during this calculation.
   - Loading gauge group classes.
   - Loading parameter classes.

Model GeneralU1_gen loaded.
Error: undefined symbol(s) in Lagrangian "LSM + LZpF": LZpF
[INFO] Lagrangian-like symbols defined by this model: LFermions, LGauge, LGhost, LHiggs, LSM, LYukawa

```
