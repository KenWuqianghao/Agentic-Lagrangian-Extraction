C[nx]≡nx) | mN=YN vΦ/√2 (text after Eq.5) | −1/2 M ψ̄ψ, self-conj |
| LZpF (quark L) | Zp uqbar.Ga.ProjM.uq, Zp dqbar.Ga.ProjM.dq | 4 | gX·qxQ | 0 | n/a | 0 | 0 | mass-eigenstate singlet (f̄…f) | δ_cc singlet | −qxQ+qxQ = 0 | 0 | n/a | Eq.6 | self-conj current (qxQ real) |
| LZpF (uR) | Zp uqbar.Ga.ProjP.uq | 4 | gX·qxU | 0 | n/a | 0 | 0 | singlet | δ_cc | 0 | 0 | n/a | Eq.6, Table II | self-conj |
| LZpF (dR) | Zp dqbar.Ga.ProjP.dq | 4 | gX·qxD | 0 | n/a | 0 | 0 | singlet | δ_cc | 0 | 0 | n/a | Eq.6, Table II | self-conj |
| LZpF (lepton L) | Zp vlbar.Ga.ProjM.vl, Zp lbar.Ga.ProjM.l | 4 | gX·qxL | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Eq.6, Eq.8 (Γ(Z′→νν̄)∝gνL²) | self-conj |
| LZpF (eR) | Zp lbar.Ga.ProjP.l | 4 | gX·qxE | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Eq.6; xH=−1 ⇒ qxE=0 (Sec. II B) | self-conj |
| LZpF (NR) | Zp nxbar.Ga.ProjP.nx | 4 | gX·qxN | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a — for Majorana nx, n̄x γ^μ P_R nx ≡ N̄_R γ^μ N_R | Eq.9 | self-conj |
| LZpS | Zp·Zp sx | 3 | gX² qxS² vX | 1 | n/a | 0 | 0 | singlet | singlet | 0 (from \|D_μΦ\|², Φ charge qxS) | 0 | n/a | Eq.4 (same vX that fixes MZp) | real, self-conj |
| LZpS | Zp·Zp sx² | 4 | gX² qxS² | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Eq.4 | real |
| LNuYuk | LLbar.nx Phibar Eps | 4 | yDN | 0 | n/a | 0 (ν̄·Φ⁰ via Eps[1,2]; ē⁺·GP⁻ via Eps[2,1]) | +1/2+0−1/2 = 0 | Eps[ii,jj], LLbar[ii] with Phibar[jj] (same conjugation type) | singlet | −qxL+qxN−qxH = (xH/2+xΦ)−xΦ−xH/2 = 0 | ΔL=1 (nx carries no L; L broken by mMaj) | n/a — paper writes ℓ̄_L H N_R, no superscript c | Eq.1 4th term; m_D = Y_ν v/√2 | explicit HC[yuk] |
| LNxYuk | sx nxbar.yMN.nx | 4 | yMN/(2√2) | 0 | n/a | 0 | 0 | singlet | singlet | qxS+2qxN = 2xΦ−2xΦ = 0 | ΔL=2 (intended) | yes — paper's Φ N̄^c_R N_R; nx is SelfConjugate so CC[nx]≡nx and N̄^c_R N_R + h.c. = n̄x nx | 1/√2 from ⟨Φ⟩=(vΦ+φ)/√2 Eq.3; normalisation fixed by m_N = Y_N vΦ/√2 (text after Eq.5) | self-conj (real yMN, Majorana bilinear) |
| LSPot | sx³ | 3 | lamX·vX | 1 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Eq.2 λΦ(Φ†Φ)², Φ†Φ=(vX+sx)²/2 | real |
| LSPot | sx⁴ | 4 | lamX/4 | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | Eq.2 | real |
| LSPot | H sx² | 3 | lamHX·vH/2 | 1 | n/a | 0 | 0 | Phibar[ii]Phi[ii] shared index | singlet | 0 | 0 | n/a | Eq.2 λ′(H†H)(Φ†Φ) | real |
| LSPot | sx·(H†H)′ , sx²·(H†H)′ | 3, 4 | lamHX·vX, lamHX/2 | 1, 0 | n/a | 0 | 0 | Phibar[ii]Phi[ii] | singlet | 0 | 0 | n/a | Eq.2 | real |

**Kinetic + mass row per new class:** `Zp` → LZpKin (in LTotal ✓); `sx` → LsxKin (✓); `nx` (3 members) → LNxKin (✓).

**Non-fundamental colour representations:** none. No `AddGaugeRepresentation[...]` line is needed; `raw_preamble` is empty.

**SelfConjugate -> True classes:** `Zp`, `sx`, `nx` — none carries `QuantumNumbers` ✓. No unphysical chiral class is needed because the paper's `N_R` enters only through `LLbar.nx` (LLbar already projects P_R) and through the Majorana bilinear.

**Name check:** Zp, sx, nx, nx1-3, MZp, WZp, Msx, Wsx, MNx, MNx1-3, WNx, WNx1-3, gX, xH, xPhi, lamX, lamHX, vX, vH, qxQ, qxU, qxD, qxL, qxE, qxN, qxH, qxS, yDN, yMN, mMaj. None is a Mathematica built-in (N, C, D, E, I, K, O), a FeynRules symbol (HC, CC, FS, DC, del, Eps, Ga, ProjP, ProjM), or an SM.fr name (H, Phi, Z, W, A, G, ee, gs, gw, sw, cw, vev, lam, yl, yu, yd, CKM, MZ, MW). No primes or punctuation in any ParticleName. Class indices are 100/101, i.e. ≥ 100. Only `Generation` and `Colour` indices are used, so `index_decls` is empty.

**Single total:** `LTotal := LZpKin + LsxKin + LNxKin + LZpF + LZpS + LNuYuk + LNxYuk + LSPot;` — every other term appears exactly once. No term is a pure constant (the `- vH^2/2` inside LSPot cancels the vev² piece of `Phibar Phi`, leaving only monomials with ≥ 3 fields).

**Deliberate omissions, with the paper's own justification:**
- No Z–Z′ mixing term. Eq. 4 keeps the doublet piece inside MZ′ but the paper uses MZ′ ≃ 2g′vΦ and never diagonalises, so rule 8 is not triggered. Emitting `|D_μ H|²` with `qxH` would produce a Zp–G0 two-point vertex that MadGraph rejects. `qxH` is still declared, as the audited re-derived charge.
- No h–sx mixing. The paper states the H–Φ mixing is negligible for small λ′, so the portal is kept without its two-point piece.
- No U(1)X Goldstone: it is eaten by Z′ (unitary gauge for the X sector).

**Reference/cached model file read:** none.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["A. Das", "P. S. B. Dev", "Y. Hosotani", "S. Mandal"],
    "version": "1.0",
    "date": "09. 09. 2026",
    "institutions": ["Kyungpook National University", "Hokkaido University", "Washington University in St. Louis", "Osaka University", "IFIC CSIC/Universitat de Valencia"],
    "emails": ["arindamdas@oia.hokudai.ac.jp", "bdev@wustl.edu", "hosotani@het.phys.sci.osaka-u.ac.jp", "smandal@ific.uv.es"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "gX",
      "parameter_type": "External",
      "value": "0.4",
      "block_name": "NPINPUTS",
      "order_block": 1,
      "interaction_order": ["NP", 1],
      "description": "U(1)X gauge coupling g-prime, Sec. II; benchmark 0.4 for MZp = 7.5 TeV, Fig. 3"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "2.",
      "block_name": "NPINPUTS",
      "order_block": 2,
      "description": "U(1)X charge parameter x_H, Table I; benchmark x_H = 2 of Table II, for which every SM charged fermion has a non-vanishing Z-prime coupling"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NPINPUTS",
      "order_block": 3,
      "description": "U(1)X charge parameter x_Phi, Table I; fixed to 1 in the paper without loss of generality"
    },
    {
      "name": "lamX",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "NPINPUTS",
      "order_block": 4,
      "interaction_order": ["NP", 1],
      "description": "Quartic self-coupling lambda_Phi of the U(1)X singlet scalar, Eq.(2)"
    },
    {
      "name": "lamHX",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "NPINPUTS",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "description": "Higgs portal coupling lambda-prime between H and Phi, Eq.(2); small, so that H-Phi mass mixing is negligible"
    },
    {
      "name": "yDN",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "block_name": "NPYUK",
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "yDN[1,1]", "rhs": "5.75*^-6"},
        {"lhs": "yDN[1,2]", "rhs": "0"},
        {"lhs": "yDN[1,3]", "rhs": "0"},
        {"lhs": "yDN[2,1]", "rhs": "0"},
        {"lhs": "yDN[2,2]", "rhs": "5.75*^-6"},
        {"lhs": "yDN[2,3]", "rhs": "0"},
        {"lhs": "yDN[3,1]", "rhs": "0"},
        {"lhs": "yDN[3,2]", "rhs": "0"},
        {"lhs": "yDN[3,3]", "rhs": "5.75*^-6"}
      ],
      "description": "Dirac neutrino Yukawa Y_nu of Eq.(1); seesaw benchmark giving m_D = Y_nu v/Sqrt[2] and light masses m_nu = m_D mN^-1 m_D^T, Eq.(5)"
    },
    {
      "name": "qxQ",
      "parameter_type": "Internal",
      "value": "xH/6 + xPhi/3",
      "description": "U(1)X charge of the quark doublet qL, Table I; 2/3 for xH = 2"
    },
    {
      "name": "qxU",
      "parameter_type": "Internal",
      "value": "2*xH/3 + xPhi/3",
      "description": "U(1)X charge of uR, Table I; vanishes for xH = -1/2"
    },
    {
      "name": "qxD",
      "parameter_type": "Internal",
      "value": "-xH/3 + xPhi/3",
      "description": "U(1)X charge of dR, Table I; vanishes for xH = 1"
    },
    {
      "name": "qxL",
      "parameter_type": "Internal",
      "value": "-xH/2 - xPhi",
      "description": "U(1)X charge of the lepton doublet lL, Table I; vanishes for xH = -2"
    },
    {
      "name": "qxE",
      "parameter_type": "Internal",
      "value": "-xH - xPhi",
      "description": "U(1)X charge of eR, Table I; vanishes for xH = -1"
    },
    {
      "name": "qxN",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)X charge of the right-handed neutrino NR, Table I"
    },
    {
      "name": "qxH",
      "parameter_type": "Internal",
      "value": "xH/2",
      "description": "U(1)X charge of the SM.fr Higgs doublet Phi with Y = +1/2. Sign is opposite to the -xH/2 of Table I because Eq.(1) uses H for the up-type Yukawa, i.e. Y(H) = -1/2, while SM.fr uses Phi for the down-type and lepton Yukawas. With this sign all SM Yukawas and the new Dirac Yukawa are U(1)X invariant"
    },
    {
      "name": "qxS",
      "parameter_type": "Internal",
      "value": "2*xPhi",
      "description": "U(1)X charge of the SM-singlet scalar Phi, Table I"
    },
    {
      "name": "vX",
      "parameter_type": "Internal",
      "value": "MZp/(qxS*gX)",
      "description": "U(1)X vacuum expectation value v_Phi in GeV, from MZp = 2 gX xPhi v_Phi, Eq.(4); 9375 GeV for the benchmark"
    },
    {
      "name": "vH",
      "parameter_type": "Internal",
      "value": "vev",
      "description": "Electroweak vev in GeV, alias of the SM.fr vev used in the new scalar potential so that portal vertices carry a pure NP interaction order"
    },
    {
      "name": "Msx",
      "parameter_type": "Internal",
      "value": "Sqrt[2*lamX]*vX",
      "description": "Mass of the physical U(1)X scalar sx in GeV, from minimising Eq.(2) with Eq.(3)"
    },
    {
      "name": "WZp",
      "parameter_type": "Internal",
      "value": "MZp*gX^2/(24*Pi)*3*(3*(qxQ^2 + qxU^2) + 3*(qxQ^2 + qxD^2) + (qxL^2 + qxE^2) + qxL^2)",
      "description": "Total Z-prime width in GeV, Eqs.(7) and (8) summed over three generations of SM fermions; the NN mode of Eq.(9) is closed because MNx > MZp"
    },
    {
      "name": "yMN",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "interaction_order": ["NP", 1],
      "value_rules": [
        {"lhs": "yMN[1,1]", "rhs": "Sqrt[2]*MNx1/vX"},
        {"lhs": "yMN[1,2]", "rhs": "0"},
        {"lhs": "yMN[1,3]", "rhs": "0"},
        {"lhs": "yMN[2,1]", "rhs": "0"},
        {"lhs": "yMN[2,2]", "rhs": "Sqrt[2]*MNx2/vX"},
        {"lhs": "yMN[2,3]", "rhs": "0"},
        {"lhs": "yMN[3,1]", "rhs": "0"},
        {"lhs": "yMN[3,2]", "rhs": "0"},
        {"lhs": "yMN[3,3]", "rhs": "Sqrt[2]*MNx3/vX"}
      ],
      "description": "Majorana Yukawa Y_N of Eq.(1), diagonal in generation; fixed by mN = Y_N v_Phi/Sqrt[2]"
    },
    {
      "name": "mMaj",
      "parameter_type": "Internal",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "mMaj[1,1]", "rhs": "MNx1"},
        {"lhs": "mMaj[1,2]", "rhs": "0"},
        {"lhs": "mMaj[1,3]", "rhs": "0"},
        {"lhs": "mMaj[2,1]", "rhs": "0"},
        {"lhs": "mMaj[2,2]", "rhs": "MNx2"},
        {"lhs": "mMaj[2,3]", "rhs": "0"},
        {"lhs": "mMaj[3,1]", "rhs": "0"},
        {"lhs": "mMaj[3,2]", "rhs": "0"},
        {"lhs": "mMaj[3,3]", "rhs": "MNx3"}
      ],
      "description": "Diagonal Majorana mass matrix of the heavy neutrinos in GeV; entries are the class masses MNx1, MNx2, MNx3 declared in F[100]"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 100,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "Internal"},
      "pdg": 9900032,
      "particle_name": "Zp",
      "full_name": "Zprime",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "sx",
      "self_conjugate": true,
      "mass": {"sym": "Msx", "value": "Internal"},
      "width": {"sym": "Wsx", "value": "100."},
      "pdg": 9900025,
      "particle_name": "sx",
      "full_name": "XHiggs",
      "propagator_label": "sx",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 100,
      "class_name": "nx",
      "self_conjugate": true,
      "class_members": ["nx1", "nx2", "nx3"],
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "mass": {"sym": "MNx", "members": [["MNx1", "10000."], ["MNx2", "12000."], ["MNx3", "14000."]]},
      "width": {"sym": "WNx", "members": [["WNx1", "1.*^-8"], ["WNx2", "1.*^-8"], ["WNx3", "1.*^-8"]]},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["nx1", "nx2", "nx3"],
      "full_name": ["Heavy neutrino 1", "Heavy neutrino 2", "Heavy neutrino 3"],
      "propagator_label": ["nx", "nx1", "nx2", "nx3"],
      "propagator_type": "Straight",
      "propagator_arrow": "None"
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu, nu}, -1/4 FS[Zp, mu, nu] FS[Zp, mu, nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]"
    },
    {
      "name": "LsxKin",
      "delayed": true,
      "expression": "Block[{mu}, 1/2 del[sx, mu] del[sx, mu] - 1/2 Msx^2 sx^2]"
    },
    {
      "name": "LNxKin",
      "delayed": true,
      "expression": "Block[{mu}, I/2 nxbar.Ga[mu].del[nx, mu] - 1/2 nxbar.mMaj.nx]"
    },
    {
      "name": "LZpF",
      "delayed": true,
      "expression": "Block[{mu}, -gX Zp[mu] (qxQ (uqbar.Ga[mu].ProjM.uq + dqbar.Ga[mu].ProjM.dq) + qxU uqbar.Ga[mu].ProjP.uq + qxD dqbar.Ga[mu].ProjP.dq + qxL (vlbar.Ga[mu].ProjM.vl + lbar.Ga[mu].ProjM.l) + qxE lbar.Ga[mu].ProjP.l + qxN nxbar.Ga[mu].ProjP.nx)]"
    },
    {
      "name": "LZpS",
      "delayed": true,
      "expression": "Block[{mu}, gX^2 qxS^2 Zp[mu] Zp[mu] (vX sx + 1/2 sx^2)]"
    },
    {
      "name": "LNuYuk",
      "delayed": true,
      "expression": "Block[{sp, ii, jj, ff1, ff2, yuk}, yuk = ExpandIndices[-yDN[ff1, ff2] LLbar[sp, ii, ff1].nx[sp, ff2] Phibar[jj] Eps[ii, jj], FlavorExpand -> SU2D]; yuk + HC[yuk]]"
    },
    {
      "name": "LNxYuk",
      "delayed": true,
      "expression": "-1/(2 Sqrt[2]) sx nxbar.yMN.nx"
    },
    {
      "name": "LSPot",
      "delayed": true,
      "expression": "Block[{ii}, ExpandIndices[-lamX vX sx^3 - 1/4 lamX sx^4 - 1/2 lamHX vH H sx^2 - lamHX (vX sx + 1/2 sx^2) (Phibar[ii] Phi[ii] - vH^2/2 - vH H), FlavorExpand -> SU2D]]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LZpKin + LsxKin + LNxKin + LZpF + LZpS + LNuYuk + LNxYuk + LSPot"
    }
  ]
}
```