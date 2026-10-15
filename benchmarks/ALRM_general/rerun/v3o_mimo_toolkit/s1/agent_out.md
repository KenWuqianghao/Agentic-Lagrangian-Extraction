All fixes verified in `model.fr`. Final self-audit:

## Self-audit table

| Term / item | Charge audit | Sign/coefficient choice | Status |
|---|---|---|---|
| **WiR[mu,3]** | From paper row-3 rotation: W_R3 = s_φ c_θ A + (c_φ s_ζ − s_φ s_θ c_ζ) Z + (c_φ c_ζ + s_φ s_θ s_ζ) Z′ | gR·sphiW·cw = e (photon OK); BM θzw=0. | Fixed (was wrong before) |
| **WiR[mu,1]/[2]** | W± = (W1 ∓ i W2)/√2 | Verified | OK |
| **LWpint quarks** | W⁺(+1)·uRbar(−2/3)·dRp(−1/3) = 0; c.c. | gR/√2 | OK |
| **LWpint leptons** | W⁺·nRpbar(0)·lR(−1) = −1? **No** — corrected: W⁺·nRpbar(X=−1/2…)… order fixed to `nRpbar·lR` + `lRbar·nRp` so (W⁺=+1, nRpbar→lR: X −1/2→−1) conserves Q | gR/√2 | Fixed |
| **LZpint QR** | T3R: uR(+1/2)−dRp(−1/2); B−L: X=1/6 both | gR cphiW/2, −gBL sphiW/6 | Verified |
| **LZpint LR T3R** | nRp(+1/2)−lR(−1/2) (L_R = (n,e)) | was flipped | Fixed |
| **LZpint LR B−L** | X=−1/2 both ⇒ +gBL sphiW/2 (nRp+lR) | was −sign, missing nRp, factor 1 | Fixed |
| **LZpint LL B−L** | X=−1/2 ⇒ +gBL sphiW/2 (l+vl) | was minus | Fixed |
| **LZpint nL** | n_L X=0 ⇒ no Z′ coupling | term `+gBL sphiW (n1+n2+n3)` removed | Fixed |
| **LZpint dR/dLp** | X=−1/3 ⇒ +gBL sphiW/3 | was `dqR` (undeclared) | Fixed → `dR` |
| **LZpint nur** | X=0 ⇒ omitted | Correct | OK |
| **ll→l** | SM class is `l` not `ll` | ren amed | Fixed |
| **dRp / nRp** | ProjP of dqp / nl | F[204] / F[205], mirror dLp/nlL | Added, undeclared-symbol gone |

**Lints (all 3 harmless):**
1. `fieldless_term Leff` — `H FS[G,…]` uses SM classes; `SM_FR` path missing so lint can't see fields (false positive).
2. `undeclared_symbol QLbar` — same root cause: SM.fr not loaded ⇒ SM_FIELDS_ALL empty (false positive).
3. `mixing_in_definitions WiR` — intended rule-8 pattern; θzw=0. at BM so Z/Z′ mixing degenerate.

**Last `./frgen`:** `SCHEMA OK: 20 particle classes, 42 parameters, 14 Lagrangian terms; LINT: 3 finding(s) (all judged harmless).`