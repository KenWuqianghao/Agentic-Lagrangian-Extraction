## Self-audit table

Paper: arXiv:2104.10902 (minimal U(1)_X model). Base file: SM.fr (read for field/index/hypercharge conventions only). **No cached or reference `.fr` file for this model was read — none.**

Charge convention note: Table 1's literal "H" column (−x_H/2) is internally consistent with all four Yukawa terms and the RHN Majorana mass **only** if it is identified with the physical field appearing in each term exactly as typeset (bare "H" in the u‑ and ν‑Yukawa terms, "H̃" in the d‑ and e‑terms) — i.e. the paper's tilde placement in Eq. (LYk) is swapped relative to the SU(2)×U(1)_Y‑forced convention used by SM.fr (which needs H̃ for u_R and H for d_R/e_R). I kept the SM Yukawas exactly as already coded in SM.fr (untouched, not new physics) and derived the **new** ν-Dirac term's SU(2) contraction from Y‑invariance (→ H̃), which I verified is simultaneously X‑charge invariant using q_X(H̃)=−x_H/2 (Table 1's tabulated number, reinterpreted as belonging to H̃, not bare H). Verified against the paper's own special case (Table 2: d_R decouples from Z′ at x_H=1, i.e. q_X(d_R)=0) — my formula reproduces exactly q_X(d_R)=0 at x_H=1. x_Φ fixed to 1 per paper ("without loss of generality").

| term | fields | dim d | coupling | coupling dim (4−d) | 1/Λ power | Q sum | Y sum | SU(2) | SU(3) | U(1)_X sum | L/B sum | CC[] | frac/root check | HC partner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LZpKin | Zp,Zp | 4 | — | — | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj. |
| LZpInt (q,ℓ,ν,N pieces) | f̄,f,Zp | 4 | gX (dimless) | 0 | n/a | 0 (vector current) | 0 | singlet current | singlet/triplet-conj | 0 (defines q_X^f) | 0 | n/a | n/a | self-Herm. (real gX·q_X) |
| LNuDirac | L̄L,H̃,NR (+HC) | 4 | ynu (dimless) | 0 | n/a | 0 | 0 | Eps[ii,jj] w/ L̄L,Phibar | singlet | 0 (verified: −q_lL+q_X(H̃)+q_NR=0) | ΔL=0 | n/a (Majorana class NR realizes N_R^c automatically) | \frac{1}{6}x_H etc. read from `\frac{...}{...}` in .tex, exact | HC[] explicit |
| LNRKin | NRbar,NR | 4(kin)/3(mass, post-SSB) | MN[ff] | mass term, hard post-SSB mass | n/a | 0 | 0 | singlet | singlet | n/a (post-SSB hard mass, standard FeynRules practice, cf. MZ/MW) | ΔL=2 (Majorana) | not needed — NR declared SelfConjugate→True, so N_R^c is automatic | n/a | self-conj. |
| LNRYuk | Sx,NRbar,NR | 4 | yN/√2 | 0 | n/a | 0 | 0 | singlet | singlet | 0 (Sx is neutral remnant of Φ) | ΔL=2 | not needed (Majorana class) | \sqrt{2} from \sqrt{2} in Eq. m_N=Y_N v_Φ/√2 | self-Herm. (real) |
| LSxKin | Sx,Sx | 4 | MSx²,lamPhi | 0 | n/a | 0 | 0 | singlet | singlet | 0 | 0 | n/a | n/a | self-conj. |
| LSxPortal | Phibar,Phi,Sx² | 4 | lamP | 0 | n/a | 0 | 0 | Phibar[ii]Phi[ii] singlet | singlet | 0 | 0 | n/a | n/a | self-Herm. |
| kinetic+mass rows | Zp (LZpKin), NR (LNRKin), Sx (LSxKin) all present and included in LTotal | | | | | | | | | | | | | |
| colour reps | none — no sextet/other rep beyond Colour/Gluon used; no `AddGaugeRepresentation` needed | | | | | | | | | | | | | |

SelfConjugate→True classes: **Zp, NR, Sx** — none carries `QuantumNumbers`. Confirmed.

Name check: Zp, NR, Sx, gX, xH, xPhi, qXqL, qXuR, qXdR, qXlL, qXeR, qXNR, vPhiX, lamPhi, lamP, yN, ynu, MN1, MN2, MN3, MSx — none is a Mathematica/FeynRules builtin (N,C,D,E,I,K,O,HC,CC,FS,DC,del,Eps,Ga,ProjP,ProjM) or an SM.fr name; class indices 130 (≥100) used throughout.

Single total Lagrangian: **LTotal := LZpKin + LZpInt + LNRKin + LNuDirac + LNRYuk + LSxKin + LSxPortal** — sums every term defined above, no orphans.

```json
{
  "model_name": "GeneralU1_gen",
  "info": {
    "authors": ["Automated extraction from arXiv:2104.10902 (Das, Dev, Hosotani, Mandal)"],
    "version": "1.0",
    "date": "2026-09-17",
    "institutions": [],
    "emails": []
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "interaction_order_limit": [],
  "vevs": [],
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
      "description": "U(1)_X gauge coupling g-prime, benchmark value used throughout Sec. II-III"
    },
    {
      "name": "xH",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NPINPUTS",
      "order_block": 2,
      "description": "U(1)_X charge-mixing parameter x_H (Table 1/2 of paper), benchmark xH=1"
    },
    {
      "name": "xPhi",
      "parameter_type": "External",
      "value": "1.",
      "block_name": "NPINPUTS",
      "order_block": 3,
      "description": "U(1)_X charge parameter x_Phi, fixed to 1 without loss of generality (Sec. II)"
    },
    {
      "name": "lamPhi",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "NPINPUTS",
      "order_block": 4,
      "interaction_order": ["NP", 1],
      "description": "New scalar quartic self-coupling lambda_Phi in the Higgs potential V"
    },
    {
      "name": "lamP",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "NPINPUTS",
      "order_block": 5,
      "interaction_order": ["NP", 1],
      "description": "Higgs portal quartic coupling lambda-prime; paper works in its small-lambda-prime decoupling limit"
    },
    {
      "name": "qXqL",
      "parameter_type": "Internal",
      "value": "(1/6)*xH+(1/3)*xPhi",
      "description": "U(1)_X charge of q_L doublet (Table 1)"
    },
    {
      "name": "qXuR",
      "parameter_type": "Internal",
      "value": "(2/3)*xH+(1/3)*xPhi",
      "description": "U(1)_X charge of u_R (Table 1)"
    },
    {
      "name": "qXdR",
      "parameter_type": "Internal",
      "value": "-(1/3)*xH+(1/3)*xPhi",
      "description": "U(1)_X charge of d_R (Table 1)"
    },
    {
      "name": "qXlL",
      "parameter_type": "Internal",
      "value": "-(1/2)*xH-xPhi",
      "description": "U(1)_X charge of l_L doublet (Table 1)"
    },
    {
      "name": "qXeR",
      "parameter_type": "Internal",
      "value": "-xH-xPhi",
      "description": "U(1)_X charge of e_R (Table 1)"
    },
    {
      "name": "qXNR",
      "parameter_type": "Internal",
      "value": "-xPhi",
      "description": "U(1)_X charge of N_R (Table 1)"
    },
    {
      "name": "vPhiX",
      "parameter_type": "Internal",
      "value": "MZp/(2*gX)",
      "description": "U(1)_X-breaking VEV v_Phi, from M_Zp ~ 2 g-prime v_Phi (Sec. II, small-mixing limit)"
    },
    {
      "name": "yN",
      "parameter_type": "External",
      "indices": ["Generation"],
      "value_rules": [
        {"lhs": "yN[1]", "rhs": "1.5"},
        {"lhs": "yN[2]", "rhs": "1.5"},
        {"lhs": "yN[3]", "rhs": "1.5"}
      ],
      "block_name": "NPYUKAWA",
      "interaction_order": ["NP", 1],
      "description": "Majorana Yukawa Y_N^alpha (Eq. LYk); benchmark chosen so m_N > M_Z' as required in Sec. II"
    },
    {
      "name": "ynu",
      "parameter_type": "External",
      "indices": ["Generation", "Generation"],
      "value_rules": [
        {"lhs": "ynu[1,1]", "rhs": "0.01"},
        {"lhs": "ynu[1,2]", "rhs": "0"},
        {"lhs": "ynu[1,3]", "rhs": "0"},
        {"lhs": "ynu[2,1]", "rhs": "0"},
        {"lhs": "ynu[2,2]", "rhs": "0.01"},
        {"lhs": "ynu[2,3]", "rhs": "0"},
        {"lhs": "ynu[3,1]", "rhs": "0"},
        {"lhs": "ynu[3,2]", "rhs": "0"},
        {"lhs": "ynu[3,3]", "rhs": "0.01"}
      ],
      "block_name": "NPYUKAWA",
      "interaction_order": ["NP", 1],
      "description": "Dirac neutrino Yukawa Y_nu^{alpha beta} (Eq. LYk), seesaw Dirac-mass coupling to H-tilde and N_R"
    },
    {
      "name": "MN1",
      "parameter_type": "Internal",
      "value": "yN[1]*vPhiX/Sqrt[2]",
      "description": "RHN generation-1 mass, m_N = Y_N v_Phi/Sqrt[2] (Sec. II)"
    },
    {
      "name": "MN2",
      "parameter_type": "Internal",
      "value": "yN[2]*vPhiX/Sqrt[2]",
      "description": "RHN generation-2 mass, m_N = Y_N v_Phi/Sqrt[2] (Sec. II)"
    },
    {
      "name": "MN3",
      "parameter_type": "Internal",
      "value": "yN[3]*vPhiX/Sqrt[2]",
      "description": "RHN generation-3 mass, m_N = Y_N v_Phi/Sqrt[2] (Sec. II)"
    },
    {
      "name": "MSx",
      "parameter_type": "Internal",
      "value": "Sqrt[2*lamPhi]*vPhiX",
      "description": "Physical mass of the new U(1)_X-breaking singlet scalar Sx"
    }
  ],
  "particles": [
    {
      "spin_type": "V",
      "class_index": 130,
      "class_name": "Zp",
      "self_conjugate": true,
      "mass": {"sym": "MZp", "value": "7500."},
      "width": {"sym": "WZp", "value": "75."},
      "pdg": 9900032,
      "particle_name": "zp",
      "full_name": "Z-prime (U(1)_X gauge boson)",
      "propagator_label": "Zp",
      "propagator_type": "Sine",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "F",
      "class_index": 130,
      "class_name": "NR",
      "self_conjugate": true,
      "indices": ["Generation"],
      "flavor_index": "Generation",
      "class_members": ["N1", "N2", "N3"],
      "mass": {"sym": "MN", "members": [["MN1", "Internal"], ["MN2", "Internal"], ["MN3", "Internal"]]},
      "width": {"massless": true},
      "pdg": [9900012, 9900014, 9900016],
      "particle_name": ["n1", "n2", "n3"],
      "full_name": ["Heavy Majorana neutrino 1", "Heavy Majorana neutrino 2", "Heavy Majorana neutrino 3"],
      "propagator_label": ["N", "N1", "N2", "N3"],
      "propagator_type": "S",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 130,
      "class_name": "Sx",
      "self_conjugate": true,
      "mass": {"sym": "MSx", "value": "Internal"},
      "width": {"sym": "WSx", "value": "100."},
      "pdg": 9900025,
      "particle_name": "sx",
      "full_name": "U(1)_X-breaking singlet scalar",
      "propagator_label": "Sx",
      "propagator_type": "D",
      "propagator_arrow": "None"
    }
  ],
  "gauge_xi": [],
  "lagrangian_terms": [
    {
      "name": "LZpKin",
      "delayed": true,
      "expression": "Block[{mu,nu}, -1/4 FS[Zp,mu,nu] FS[Zp,mu,nu] + 1/2 MZp^2 Zp[mu] Zp[mu]]"
    },
    {
      "name": "LZpInt",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[ -gX ( qXqL uqbar.Ga[mu].ProjM.uq + qXuR uqbar.Ga[mu].ProjP.uq + qXqL dqbar.Ga[mu].ProjM.dq + qXdR dqbar.Ga[mu].ProjP.dq + qXlL lbar.Ga[mu].ProjM.l + qXeR lbar.Ga[mu].ProjP.l + qXlL vlbar.Ga[mu].ProjM.vl + qXNR NRbar.Ga[mu].ProjP.NR ) Zp[mu] ] ]"
    },
    {
      "name": "LNRKin",
      "delayed": true,
      "expression": "Block[{sp,mu,ff}, ExpandIndices[ I/2 NRbar.Ga[mu].del[NR,mu] - 1/2 MN[ff] NRbar[sp,ff].NR[sp,ff] ] ]"
    },
    {
      "name": "LNuDirac",
      "delayed": true,
      "expression": "Block[{sp,ii,jj,ff1,ff2,yukNu}, yukNu = ExpandIndices[ -ynu[ff1,ff2] LLbar[sp,ii,ff1].NR[sp,ff2] Phibar[jj] Eps[ii,jj], FlavorExpand->SU2D]; yukNu + HC[yukNu] ]"
    },
    {
      "name": "LNRYuk",
      "delayed": true,
      "expression": "Block[{sp,ff}, ExpandIndices[ -(yN[ff]/Sqrt[2]) Sx NRbar[sp,ff].NR[sp,ff] ] ]"
    },
    {
      "name": "LSxKin",
      "delayed": true,
      "expression": "Block[{mu}, 1/2 del[Sx,mu] del[Sx,mu] - 1/2 MSx^2 Sx^2 - (lamPhi/4) Sx^4]"
    },
    {
      "name": "LSxPortal",
      "delayed": true,
      "expression": "Block[{ii}, ExpandIndices[ -lamP Phibar[ii] Phi[ii] Sx^2, FlavorExpand->SU2D] ]"
    },
    {
      "name": "LTotal",
      "delayed": true,
      "expression": "LZpKin + LZpInt + LNRKin + LNuDirac + LNRYuk + LSxKin + LSxPortal"
    }
  ],
  "raw_preamble": [],
  "raw_blocks": []
}
```