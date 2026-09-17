## Self-audit table

Read only the paper's LaTeX source (`1912.04008_source.tex`), the schema (`frmodel.py`) and `SM.fr`. No cached/reference `.fr` file for pNG was opened — **none**.

**Model construction note.** The pNG model (arXiv:1912.04008, Sec. 2) adds one complex scalar singlet `S` with a softly-broken global (not gauged) U(1). After EWSB, `S=(v_s+s+iχ)/√2` and the SM neutral Higgs component mix, `(φ,s)=R(θ)(h,H)`. I implement this by **overriding** SM.fr's unphysical `Phi` (`S[11]`) so `Phi[2]` carries the mixing, and by declaring a new unphysical complex singlet `Ssing` with the same mixing built into its `Definitions`. `LGauge`, `LFermions`, `LYukawa`, `LGhost` are **not redefined** — they automatically inherit the h/H(2)-mixed couplings to gauge bosons and fermions because they reference `Phi[ii]`, whose definition I changed. I replace only the Higgs potential piece (`LHiggsPortal`, using paper-normalization `μ_Φ²/2`, `λ_Φ/2` so it is not double counted against SM.fr's own differently-normalized `LHiggs`, which is dropped from `LTotal`) and add the singlet kinetic/potential (`LSkin`) and the soft breaking term (`LSoftpNG`). `MH`≡SM.fr's 125 GeV Higgs ≡ paper's `h`; new heavy state named `H2` ≡ paper's `H` (name `H` was already taken by SM.fr).

| term | fields | dim d | coupling | coupling dim (4-d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | dark-U(1) sum | L/B | CC[] | fraction/root check | Herm. partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LHiggsPortal (kin) | Phibar,Phi | 4 | — | — | n/a | 0 | 0 | Φ†Φ shared-index ii | singlet | n/a (no S field) | n/a | n/a | n/a | self-Herm. |
| LHiggsPortal (mass) | Phibar,Phi | 2 | muPhi2 | 2 | n/a | 0 | 0 | shared idx ii | singlet | n/a | n/a | n/a | Eq.(146), literal | self-Herm. |
| LHiggsPortal (quartic) | Phibar,Phi×2 | 4 | lamPhi | 0 | n/a | 0 | 0 | shared idx ii,jj | singlet | n/a | n/a | n/a | Eq.(146) `λ_Φ/2`, literal | self-Herm. |
| LSkin (kin) | Ssingbar,Ssing | 4 | — | — | n/a | 0 | 0 | singlet | singlet | 0 (S,S† equal) | n/a | n/a | n/a | self-Herm. |
| LSkin (mass) | Ssingbar,Ssing | 2 | muS2 | 2 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | Eq.(125) `μ_S²/2`, literal | self-Herm. |
| LSkin (portal) | Phibar,Phi,Ssingbar,Ssing | 4 | lamPhiS | 0 | n/a | 0 | 0 | Φ shared ii, S singlet | singlet | 0 | n/a | n/a | Eq.(125), no 1/2 prefactor, verified in LaTeX | self-Herm. |
| LSkin (quartic) | Ssingbar,Ssing×2 | 4 | lamS | 0 | n/a | 0 | 0 | singlet | singlet | 0 | n/a | n/a | Eq.(125) `λ_S/2`, literal | self-Herm. |
| LSoftpNG | Ssing²+Ssingbar² | 2 | muSp2 | 2 | n/a | 0 | 0 | singlet | singlet | **+2 / -2** (deliberate: this is the paper's explicit soft breaking of the *global*, non-gauged dark U(1); no dark charge is registered as a FeynRules `QuantumNumbers` since the symmetry is never gauged, cf. `gauge_groups: []`) | n/a | n/a | Eq.(126) `μ_S'²/4`, literal | self-Herm. |
| H2 kinetic+mass | H2 | — | — | — | n/a | — | — | — | — | — | — | — | eigenvalue by construction, Eqs.(194)-(197),(209)-(211) | confirmed in LTotal (via LHiggsPortal+LSkin) |
| chi kinetic+mass | chi | — | — | — | n/a | — | — | — | — | — | — | — | m_χ²=μ_S'², stated directly below Eq.(158) | confirmed in LTotal (via LSkin+LSoftpNG) |

- `SelfConjugate -> True` classes: `H2`, `chi` — both carry empty `QuantumNumbers`. Confirmed.
- No non-fundamental colour representation is used anywhere (H2, chi, Ssing are SU(3) singlets) — no `AddGaugeRepresentation` needed.
- Names chosen — particles: `Phi` (SM.fr override, intentionally reusing its index), `Ssing`, `H2`, `chi`; parameters: `vs`, `thx`, `costh`, `sinth`, `lamPhi`, `lamS`, `lamPhiS`, `muSp2`, `muPhi2`, `muS2`. None is a Mathematica built-in or FeynRules symbol (`N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM`) and none collides with an SM.fr name (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,lam,MH,WH,...` — `H2`≠`H`, `lamPhi/lamS/lamPhiS`≠`lam`, `WH2`≠`WH`).
- Single total: `LTotal := LGauge + LFermions + LYukawa + LGhost + LHiggsPortal + LSkin + LSoftpNG` — sums all three terms defined in this file plus the untouched SM pieces.
- Reference/cached model file read: **none**.

```json
{
  "model_name": "pNG_gen",
  "info": {
    "authors": ["Chiara Arina", "Ankit Beniwal", "Celine Degrande", "Jan Heisig", "Andre Scaffidi"],
    "version": "1.0",
    "date": "17. 09. 2026",
    "institutions": ["Universite catholique de Louvain (CP3)", "University of Adelaide"],
    "emails": ["chiara.arina@uclouvain.be", "ankit.beniwal@uclouvain.be", "celine.degrande@uclouvain.be", "jan.heisig@uclouvain.be", "andre.scaffidi@adelaide.edu.au"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "vs",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "NPINPUTS",
      "order_block": 1,
      "description": "Singlet scalar VEV v_s [GeV], Eq. (149)"
    },
    {
      "name": "thx",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "NPINPUTS",
      "order_block": 2,
      "description": "h-H2 mixing angle theta [rad], Eq. (176); paper scans theta in [0, pi/2]"
    },
    {
      "name": "costh",
      "parameter_type": "Internal",
      "value": "Cos[thx]",
      "description": "Cosine of the h-H2 mixing angle"
    },
    {
      "name": "sinth",
      "parameter_type": "Internal",
      "value": "Sin[thx]",
      "description": "Sine of the h-H2 mixing angle"
    },
    {
      "name": "lamPhi",
      "parameter_type": "Internal",
      "value": "(MH^2*costh^2 + MH2^2*sinth^2)/vev^2",
      "interaction_order": ["NP", 1],
      "description": "SM-like Higgs quartic coupling lambda_Phi, re-derived with h-H2 mixing, Eq. (209)"
    },
    {
      "name": "lamS",
      "parameter_type": "Internal",
      "value": "(MH^2*sinth^2 + MH2^2*costh^2)/vs^2",
      "interaction_order": ["NP", 1],
      "description": "Singlet quartic coupling lambda_S, Eq. (210)"
    },
    {
      "name": "lamPhiS",
      "parameter_type": "Internal",
      "value": "(MH2^2 - MH^2)*sinth*costh/(vev*vs)",
      "interaction_order": ["NP", 1],
      "description": "Higgs-portal quartic coupling lambda_PhiS, Eq. (211)"
    },
    {
      "name": "muSp2",
      "parameter_type": "Internal",
      "value": "Mchi^2",
      "description": "Soft dark-U(1)-breaking mass mu_S'^2 = m_chi^2, Eq. (209); this is the sole explicit breaking of the global dark U(1) discussed after Eq. (132)"
    },
    {
      "name": "muPhi2",
      "parameter_type": "Internal",
      "value": "lamPhi*vev^2 + lamPhiS*vs^2",
      "description": "SM Higgs potential mass-squared mu_Phi^2 (tadpole condition), Eq. (162)"
    },
    {
      "name": "muS2",
      "parameter_type": "Internal",
      "value": "lamS*vs^2 + lamPhiS*vev^2 - muSp2",
      "description": "Singlet potential mass-squared mu_S^2 (tadpole condition), Eq. (163)"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 11,
      "class_name": "Phi",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "1/2"},
      "unphysical": true,
      "definitions": [
        "Phi[1] -> -I GP",
        "Phi[2] -> (vev + costh H + sinth H2 + I G0)/Sqrt[2]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "Ssing",
      "self_conjugate": false,
      "unphysical": true,
      "definitions": [
        "Ssing -> (vs - sinth H + costh H2 + I chi)/Sqrt[2]"
      ]
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "H2",
      "self_conjugate": true,
      "mass": {"sym": "MH2", "value": "300."},
      "width": {"sym": "WH2", "value": "1."},
      "quantum_numbers": {},
      "pdg": 35,
      "particle_name": "H2",
      "full_name": "Heavy CP-even scalar (h-H2 mixing partner of the SM Higgs)",
      "propagator_label": "H2",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "chi",
      "self_conjugate": true,
      "mass": {"sym": "Mchi", "value": "100."},
      "width": {"massless": true},
      "quantum_numbers": {},
      "pdg": 52,
      "particle_name": "chi",
      "full_name": "pseudo-Nambu-Goldstone dark matter",
      "propagator_label": "chi",
      "propagator_type": "D",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LHiggsPortal",
      "delayed": true,
      "expression": "Block[{mu,ii,jj}, ExpandIndices[DC[Phibar[ii],mu] DC[Phi[ii],mu] + (muPhi2/2) Phibar[ii] Phi[ii] - (lamPhi/2) Phibar[ii] Phi[ii] Phibar[jj] Phi[jj], FlavorExpand->{SU2D,SU2W}]]"
    },
    {
      "name": "LSkin",
      "delayed": true,
      "expression": "Block[{mu,ii,jj}, ExpandIndices[DC[Ssingbar,mu] DC[Ssing,mu] + (muS2/2) Ssingbar Ssing - lamPhiS Phibar[ii] Phi[ii] Ssingbar Ssing - (lamS/2) (Ssingbar Ssing)^2, FlavorExpand->{SU2D,SU2W}]]"
    },
    {
      "name": "LSoftpNG",
      "delayed": true,
      "expression": "(muSp2/4) (Ssing^2 + Ssingbar^2)"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LGauge + LFermions + LYukawa + LGhost + LHiggsPortal + LSkin + LSoftpNG"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```