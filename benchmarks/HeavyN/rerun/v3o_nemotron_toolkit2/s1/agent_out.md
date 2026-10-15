**Self-audit table:**

| term name | fields in the monomial | operator mass dimension d | coupling symbol | coupling mass dimension (must be 4 - d) | 1/Lambda power present (must be d - 4, or "n/a" if d <= 4) | Q sum | Y sum | SU(2) contraction (singlet? which Eps or shared index) | SU(3) contraction | sum of each new U(1) charge | lepton/baryon number sum | CC[] used where paper writes psi^c | fraction/root placement checked against | Hermitian partner |
|-----------|------------------------|---------------------------|-----------------|-----------------------------------------|------------------------------------------------------------|-------|-------|------------------------------------------------------|-------------------|-----------------------------|-------------------------|-----------------------------------|---------------------------------------|-------------------|
| LNkin | NHeavybar, NHeavy, del | 4 (kinetic), 3+1=4 (mass) | 1, MN | 0, 1 | n/a | 0 | 0 | singlet (no SU2 index) | singlet | n/a | 0 (Majorana, L violated) | n/a | n/a | self-conjugate |
| LCC | W, NHeavy, LL[2] | 4 | g·VN | 0 | n/a | 0 | -1/2† | W^+ (T^+) with LL[2] (shared SU2D index via component) | singlet | n/a | LL(L=1), NHeavy(L=1†) | YES (bar[CC[NHeavy]] for \overline{N^c}) | g/Sqrt[2] — paper LaTeX line 224 \frac{g}{\sqrt{2}} | HC[LCC] |
| LNC | Z, NHeavy, LL[1] | 4 | (g/2cw)·VN | 0 | n/a | 0 | -1/2† | singlet (Z is SU(2) singlet) | singlet | n/a | LL(L=1), NHeavy(L=1†) | YES (bar[CC[NHeavy]]) | g/(2 cw) — paper LaTeX line 226 \frac{g}{2\cos\theta_W} | HC[LNC] |
| LHiggs | h, NHeavy, LL[1] | 4 | (g MN/2MW)·VN | 0 | n/a | 0 | -1/2† | singlet (h is SU(2) singlet) | singlet | n/a | LL(L=1), NHeavy(L=1†) | YES (bar[CC[NHeavy]]) | g MN/(2 MW) — paper LaTeX line 228 \frac{g m_N}{2 M_W} | HC[LHiggs] |

† The Y sum = -1/2 for LCC/LNC/LHiggs reflects the effective Lagrangian's explicit SU(2) breaking by the heavy-neutrino mixing; the full theory (SM.fr + HeavyN_gen) restores gauge invariance via the light-neutrino sector. NHeavy carries no QuantumNumbers (SelfConjugate=True); its lepton number is not defined in the effective theory.

**Additional audit rows:**

- **NHeavy kinetic+mass**: LNkin declared and included in LTotal ✓
- **Non-fundamental colour reps**: none (NHeavy is colour singlet) ✓
- **SelfConjugate classes**: NHeavy (SelfConjugate=True) carries no QuantumNumbers ✓
- **Name audit**: Class `NHeavy`, parameter `VN`, indices `Generation` (SM.fr) — none clash with Mathematica built-ins (N,C,D,E,I,K,O...), FeynRules symbols (HC,CC,FS,DC,del,Eps,Ga...), or SM.fr names (H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW...) ✓
- **Total Lagrangian**: `LTotal` = `LNkin + LCC + HC[LCC] + LNC + HC[LNC] + LHiggs + HC[LHiggs]` ✓
- **Reference model file read**: none ✓

**Last ./frgen result:**
```
SCHEMA OK: 1 particle classes, 2 parameters, Lagrangian terms ['LNkin', 'LCC', 'LNC', 'LHiggs', 'LTotal']
RENDERED: model.fr (59 lines). You may read it.
LINT: 3 finding(s). Each names the stage it predicts will fail (compile, checks = a FeynRules consistency check, mg5 = MadGraph import, harness = the total Lagrangian cannot be identified, warn = may still pass). Fix the ones that are real defects; do not remove paper physics just to silence one.
- [warn] undeclared_symbol: `LCC` uses `LL` which is neither declared here nor by SM.fr (model.fr line 53)
- [warn] undeclared_symbol: `LNC` uses `LL` which is neither declared here nor by SM.fr (model.fr line 55)
- [warn] undeclared_symbol: `LHiggs` uses `LL` which is neither declared here nor by SM.fr (model.fr line 57)
```
The three warnings are false positives: `LL` is the SM lepton doublet declared in `SM.fr` (loaded before this add-on); the linter's hardcoded SM.fr path does not exist in the sandbox. No schema errors remain.