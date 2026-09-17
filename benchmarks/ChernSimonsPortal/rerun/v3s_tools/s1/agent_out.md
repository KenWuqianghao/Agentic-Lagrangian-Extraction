## Self-audit table

Scope decision: the paper's low-energy, LHC-scale effective theory (Sec. 4, "Phenomenology") is explicitly "the SM plus a massive vector boson X" (text after Eq.(39)). The chiral fermions ψ1,2, χ1,2 of Secs. 2–3 are the UV completion used only to derive the anomaly-cancellation coefficients c1, c2; the paper states their masses are ≳10 TeV and they are integrated out, so they carry no propagating degrees of freedom at collider energies and are not part of the "ChernSimonsPortal" UFO content. The extracted model therefore contains exactly one new particle (X) and two new dimensionless couplings (c1, c2).

| term name | fields in monomial | d | coupling | coupling dim (4-d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | new-U(1) sum | L/B sum | CC[] | fraction/root check | Hermitian partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LXkin | X,X (via FS,FS) and X,X (mass) | 4 | −1/4 (FS·FS), 1/2 MX² | 0 | n/a (d=4) | 0 | n/a | singlet | singlet | n/a (no new U(1) declared) | n/a | n/a | n/a | self-conjugate |
| LXZZ | X, Z, ∂Z | 4 | c1·sw/2 | 0 | n/a | 0 | n/a (mass basis) | n/a — written in EWSB mass-eigenstate basis (X,Z,A,W), matching Eq.(15) after H gets a vev; UV covariant form is Eq.(48) | singlet | n/a | n/a | n/a | matches Eq.(40) Γ_XZZ (½ from identical-Z symmetrization) | self-conjugate (real fields) |
| LXZA | X, Z, ∂A | 4 | c1·cw | 0 | n/a | 0 | n/a | n/a (same as above) | singlet | n/a | n/a | n/a | matches Eq.(40) Γ_XZγ | self-conjugate |
| LXWW | X, Wbar, ∂W (+ h.c.) | 4 | c2 | 0 | n/a | 0+(−1)+(+1)=0 | n/a | n/a (mass basis) | singlet | n/a | n/a | n/a | matches unlabeled Γ_{XW+W-} eq. (line before Eq.(41)) | HC[...] partner included explicitly |

- Kinetic+mass term row: `LXkin` is X's Proca kinetic+mass term, matching rule-1's real-vector-singlet template exactly; it is included in `LTotal`.
- Non-fundamental colour representations: none used — X and all couplings are SU(3) singlets, no `AddGaugeRepresentation[...]` needed.
- `SelfConjugate -> True` classes: `X` only; it carries no `QuantumNumbers` (confirmed — none declared).
- Names chosen: class `X`; parameters `c1`, `c2`, `MX`, `WX`. None is a Mathematica/FeynRules built-in (`N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM`) and none collides with an SM.fr name (`H,Phi,Z,W,A,G,ee,gs,gw,sw,cw,vev,MZ,MW,MH,WW,WZ,WH,aEW,...`). `X` has class index 100 (≥100).
- Single total Lagrangian: `LTotal := LXkin + LXZZ + LXZA + LXWW;` sums every term above.
- Reference/cached model file read: none — only the paper's LaTeX source and the provided `SM.fr` (explicitly allowed for conventions) were read.
- `WX` (Internal) sums the three exact partial-width formulas of Eq.(41)/pre-Eq.(55), with the `(1-4M²/M_X²)^(5/2)` and `(1-M_Z²/M_X²)^3(1+M_Z²/M_X²)` factors taken literally from the LaTeX source (`\frac{4M_Z^2}{M_X^2}` etc.), so no fraction/root placement ambiguity remains.

```json
{
  "model_name": "ChernSimonsPortal_gen",
  "info": {
    "authors": ["I. Antoniadis", "A. Boyarsky", "S. Espahbodi", "O. Ruchayskiy", "J. D. Wells"],
    "version": "1.0",
    "date": "2009-01-06",
    "institutions": ["CERN PH-TH"],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "feynman_gauge": null,
  "vevs": [],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "MX",
      "parameter_type": "External",
      "value": "1000.",
      "block_name": "MASS",
      "description": "X boson mass [GeV]; benchmark M_X=1 TeV used in text near Eq.(100)/Sec.4 discovery discussion."
    },
    {
      "name": "c1",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NPCSPORTAL",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "Chern-Simons portal coupling of X to Z-hypercharge current, from H^dagger D H/|H|^2 D theta_X F_Y, Eq.(48) and Eq.(15); dimensionless, benchmark c1=1 (Figs. lep/tev) or 0.1 (Fig. lhcsigma)."
    },
    {
      "name": "c2",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NPCSPORTAL",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "description": "Chern-Simons portal coupling of X to W+W-, from H F_W D H^dagger/|H|^2 D theta_X, Eq.(48); dimensionless, benchmark c2=1 or 0.1."
    },
    {
      "name": "WX",
      "parameter_type": "Internal",
      "value": "(c1^2 sw2 MX^3)/(192 Pi MZ^2) (1-4 MZ^2/MX^2)^(5/2) + (c2^2 MX^3)/(48 Pi MW^2) (1-4 MW^2/MX^2)^(5/2) + (c1^2 (1-sw2) MX^3)/(96 Pi MZ^2) (1-MZ^2/MX^2)^3 (1+MZ^2/MX^2)",
      "description": "X boson total width [GeV] = Gamma(X->ZZ)+Gamma(X->WW)+Gamma(X->Zgamma), Eq.(41) plus the Zgamma partial width equation preceding Eq.(55); exact fractions/exponents taken from LaTeX source."
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "X",
      "self_conjugate": true,
      "indices": [],
      "mass": {"massless": false, "sym": "MX", "value": "1000."},
      "width": {"massless": false, "sym": "WX", "value": "Internal"},
      "quantum_numbers": {},
      "particle_name": "x1",
      "full_name": "X (Chern-Simons portal vector)",
      "propagator_label": "X",
      "propagator_type": "Sine",
      "propagator_arrow": "None",
      "unphysical": false,
      "definitions": []
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LXkin",
      "expression": "Block[{mu,nu}, -1/4 FS[X,mu,nu] FS[X,mu,nu] + 1/2 MX^2 X[mu] X[mu]]",
      "delayed": true
    },
    {
      "name": "LXZZ",
      "expression": "Block[{mu,nu,ro,si}, (c1 sw)/2 Eps[mu,nu,ro,si] X[mu] Z[nu] del[Z[si],ro]]",
      "delayed": true
    },
    {
      "name": "LXZA",
      "expression": "Block[{mu,nu,ro,si}, c1 cw Eps[mu,nu,ro,si] X[mu] Z[nu] del[A[si],ro]]",
      "delayed": true
    },
    {
      "name": "LXWW",
      "expression": "Block[{mu,nu,ro,si}, c2 Eps[mu,nu,ro,si] X[mu] Wbar[nu] del[W[si],ro] + HC[c2 Eps[mu,nu,ro,si] X[mu] Wbar[nu] del[W[si],ro]]]",
      "delayed": true
    },
    {
      "name": "LTotal",
      "expression": "LXkin + LXZZ + LXZA + LXWW",
      "delayed": true
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```