I'll start by reading the paper and the schema.
I read the paper, the schema, the renderer, and `SM.fr`. Nothing else exists here, and I opened no reference or cached `.fr` file.

## Physics content I extracted

The model is the L+N vector-like confinement theory (arXiv:1508.01112). Below the confinement scale the new states are the 9 pseudo-Goldstone bosons of SU(3)×SU(3)/SU(3), eq. (5):

| state | SU(3)c | SU(2)L | Y (SM.fr convention) | Q | mass |
|---|---|---|---|---|---|
| `K2` = (K2+, K2⁰) composite "Kaon" | singlet | doublet | +1/2 | +1, 0 | `MK2`, eq. (9) |
| `pi3` composite "Pion" triplet (π3±, π3⁰) | singlet | triplet | 0 | ±1, 0 | `Mpi3`, eq. (9) |
| `eta` composite singlet | singlet | singlet | 0 | 0 | `Meta`, eq. (9) |
| `etap` (η′, U(1)A anomaly) | singlet | singlet | 0 | 0 | `Metap` = Sqrt[3 a/N] |
| `rlx` relaxion φ, Sec. 4 | singlet | singlet | 0 | 0 | `Mrlx` (free) |

Hypercharge sign (rule 5): the paper's charge table uses Y = −1/2 Diag[1,1,0], but its own labels K2 = (K2+, K2⁰) and the mixing term K2†H both need Y(K2) = Y(H). SM.fr fixes Y(Phi) = +1/2, so I set **Y(K2) = +1/2**. Then Q(K2+) = +1 and Q(K2⁰) = 0, as the paper labels them, and K2bar[ii] Phi[ii] is a singlet.

The relaxion couples only to the hypercolour field strength (eq. 34), which is not a degree of freedom of the effective theory; θ_H enters through the phases of `mL`, `mN`, `y`, `ytilde` (eqs. 3–4, 35). So `rlx` gets only its free-field term.

## Self-audit table

| term | monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L/B | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LK2kin` | DC[K2bar]DC[K2]; MK2² K2bar K2 | 4; 2 | 1; MK2² | 0; 2 | n/a | 0 | −1/2+1/2=0 | shared ii | singlet | none | n/a | n/a | self-conj (real) |
| `Lpi3kin` | DC[pi3]DC[pi3]; Mpi3² pi3 pi3 | 4; 2 | 1; Mpi3² | 0; 2 | n/a | 0 | 0 | adjoint aa shared | singlet | none | n/a | n/a | self-conj |
| `Letakin` | del[eta]del[eta]; Meta² eta² | 4; 2 | 1; Meta² | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj |
| `Letapkin` | del[etap]²; Metap² etap² | 4; 2 | 1; Metap² | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj |
| `Lrlxkin` | del[rlx]²; Mrlx² rlx² | 4; 2 | 1; Mrlx² | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj |
| `LKmix0` (eq. 8) | K2bar Phi | 2 | I√2 gRho fpi² BB | 2 | n/a | 0 | −1/2+1/2=0 | shared ii (doublet·anti-doublet) | singlet | none | n/a | n/a | `HC[]` in `LKmix` |
| `LKpi0` (eq. 8) | K2bar Ta[aa,ii,jj] Phi pi3; eta K2bar Phi | 3 | √2 gRho AA fpi | 1 | n/a | 0 | 0 | Ta[aa,ii,jj]; shared ii | singlet | none | n/a | n/a | `HC[]` in `LKpi` |
| `Leta3` a (eq. 8) | eta | 1 | gRho(mLim−mNim)4fpi²/√3 | 3 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | already Hermitian |
| `Leta3` b | eta³ | 3 | gRho(mLim−mNim)·2/(9√3) | 1 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | Hermitian |
| `Leta3` c | eta K2bar K2; eta pi3 pi3 | 3 | 2 gRho mNim/√3; 2 gRho mLim/√3 | 1 | n/a | 0 | 0 | shared ii; shared aa | singlet | none | n/a | n/a | Hermitian |
| `Leta3` d | K2bar Ta[aa,ii,jj] K2 pi3 | 3 | 4/3 gRho(2mLim+mNim) | 1 | n/a | 0 | −1/2+1/2=0 | Ta[aa,ii,jj] | singlet | none | n/a | n/a | Hermitian |
| `Lpi3anom` (eq. 26) | pi3 FS[Wi] FS[B] | 5 | g1 gw NHC/(64π² fpi) | −1 | 1/fpi¹ ✔ | 0 | 0 | adjoint aa shared with W | singlet | none | n/a | n/a | Hermitian |
| `Letaanom` (eq. 26) | eta FS[Wi]FS[Wi]; eta FS[B]FS[B] | 5 | NHC gw²(g1²)/(64√3 π² fpi) | −1 | 1/fpi¹ ✔ | 0 | 0 | aa contracted on W W | singlet | none | n/a | n/a | Hermitian |

Every new class has a kinetic + mass term in the total sum `LVLCLN`. `fpi` is the EFT scale: it is External, in GeV, with `InteractionOrder -> {QED,-1}`, and the two anomaly operators (d = 5) carry `1/fpi`.

`SelfConjugate -> True` classes: `pi3`, `pi30`, `eta`, `etap`, `rlx` — none carries `QuantumNumbers`. The Y charge sits only on the Unphysical doublet `K2`, and Q only on the physical charged states `K2p`, `pi3p`.

Reference or cached model files read: **none**. No `psi^c` appears in the paper's new-physics terms, so no `CC[]` is needed.

```json
{
  "model_name": "VLC_LN_gen",
  "info": {
    "authors": ["O. Antipin", "M. Redi"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["INFN, Sezione di Firenze"],
    "emails": ["oleg.antipin@fi.infn.it", "michele.redi@fi.infn.it"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "fpi",
      "parameter_type": "External",
      "value": "500.",
      "block_name": "VLCLN",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "tex": "f_\\pi",
      "description": "Composite pion decay constant [GeV]; EFT scale of the chiral Lagrangian, Eq.(6). The anomaly operators are dimension 5 and carry 1/fpi."
    },
    {
      "name": "gRho",
      "parameter_type": "External",
      "value": "7.",
      "block_name": "VLCLN",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "tex": "g_\\rho",
      "description": "Strong coupling of the SU(N) sector, gRho ~ 4 Pi/Sqrt[N], about 7 for N = 3, Eq.(6)"
    },
    {
      "name": "NHC",
      "parameter_type": "External",
      "value": "3.",
      "block_name": "VLCLN",
      "order_block": 3,
      "tex": "N",
      "description": "Number of hypercolours N of the confining SU(N) gauge group, Eq.(1)"
    },
    {
      "name": "mLre",
      "parameter_type": "External",
      "value": "20.",
      "block_name": "VLCLN",
      "order_block": 4,
      "tex": "Re m_L",
      "description": "Real part of the vector-like doublet mass mL [GeV], Eq.(2)"
    },
    {
      "name": "mLim",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "VLCLN",
      "order_block": 5,
      "tex": "Im m_L",
      "description": "Imaginary part of mL [GeV] (theta_H phase), Eqs.(3),(4),(8)"
    },
    {
      "name": "mNre",
      "parameter_type": "External",
      "value": "20.",
      "block_name": "VLCLN",
      "order_block": 6,
      "tex": "Re m_N",
      "description": "Real part of the singlet mass mN [GeV], Eq.(2)"
    },
    {
      "name": "mNim",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "VLCLN",
      "order_block": 7,
      "tex": "Im m_N",
      "description": "Imaginary part of mN [GeV] (theta_H phase), Eqs.(3),(4),(8)"
    },
    {
      "name": "yre",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "VLCLN",
      "order_block": 8,
      "interaction_order": ["NP", 1],
      "tex": "Re y",
      "description": "Real part of the Yukawa y of H L N^c, Eq.(2)"
    },
    {
      "name": "yim",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "VLCLN",
      "order_block": 9,
      "interaction_order": ["NP", 1],
      "tex": "Im y",
      "description": "Imaginary part of the Yukawa y, Eq.(2)"
    },
    {
      "name": "ytre",
      "parameter_type": "External",
      "value": "0.09",
      "block_name": "VLCLN",
      "order_block": 10,
      "interaction_order": ["NP", 1],
      "tex": "Re yt",
      "description": "Real part of the Yukawa ytilde of H^dagger L^c N, Eq.(2)"
    },
    {
      "name": "ytim",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "VLCLN",
      "order_block": 11,
      "interaction_order": ["NP", 1],
      "tex": "Im yt",
      "description": "Imaginary part of the Yukawa ytilde, Eq.(2). Im[y ytilde] is the CP violating phase that drives the EDM, Eq.(33)"
    },
    {
      "name": "aAnom",
      "parameter_type": "External",
      "value": "1.*^6",
      "block_name": "VLCLN",
      "order_block": 12,
      "tex": "a",
      "description": "U(1)_A anomaly parameter a [GeV^2], Eq.(6); it fixes the eta-prime mass, m_etap^2 = 3 a/N"
    },
    {
      "name": "thetaH",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "VLCLN",
      "order_block": 13,
      "tex": "\\theta_H",
      "description": "Topological angle of the SU(N) gauge fields, Eq.(1). It is rotated into the phases of mL, mN, y, ytilde by Eqs.(3),(4), and is replaced by rlx/frlx in the relaxion scenario, Eq.(35)"
    },
    {
      "name": "frlx",
      "parameter_type": "External",
      "value": "1.*^9",
      "block_name": "VLCLN",
      "order_block": 14,
      "tex": "f",
      "description": "Relaxion decay constant f [GeV] of the axion-like coupling phi/f GGdual/(32 Pi^2), Eq.(34)"
    },
    {
      "name": "AA",
      "parameter_type": "Internal",
      "value": "yre + ytre + I*(yim - ytim)",
      "complex": true,
      "interaction_order": ["NP", 1],
      "tex": "A",
      "description": "A = y + Conjugate[ytilde], Eq.(2)"
    },
    {
      "name": "BB",
      "parameter_type": "Internal",
      "value": "yre - ytre + I*(yim + ytim)",
      "complex": true,
      "interaction_order": ["NP", 1],
      "tex": "B",
      "description": "B = y - Conjugate[ytilde], Eq.(2); it controls the Higgs-Kaon mixing"
    },
    {
      "name": "Mrho",
      "parameter_type": "Internal",
      "value": "gRho*fpi",
      "tex": "m_\\rho",
      "description": "Mass of the lightest vector resonance, m_rho = gRho fpi, Eq.(6)"
    },
    {
      "name": "MK2",
      "parameter_type": "Internal",
      "value": "Sqrt[9*gw^2*gRho^2*fpi^2/(4*(4*Pi)^2) + 2*(mLre + mNre)*gRho*fpi]",
      "tex": "m_{K_2}",
      "description": "Mass of the composite Kaon doublet K2, Eq.(9)"
    },
    {
      "name": "MK2z",
      "parameter_type": "Internal",
      "value": "MK2",
      "tex": "m_{K_2^0}",
      "description": "Mass of the neutral composite Kaon; degenerate with the charged one at this order, Eq.(9)"
    },
    {
      "name": "Mpi3",
      "parameter_type": "Internal",
      "value": "Sqrt[6*gw^2*gRho^2*fpi^2/(4*Pi)^2 + 4*mLre*gRho*fpi]",
      "tex": "m_{\\pi_3}",
      "description": "Mass of the composite pion triplet pi3, Eq.(9)"
    },
    {
      "name": "Mpi30",
      "parameter_type": "Internal",
      "value": "Mpi3",
      "tex": "m_{\\pi_3^0}",
      "description": "Mass of the neutral pion triplet member; degenerate with the charged one at this order, Eq.(9)"
    },
    {
      "name": "Meta",
      "parameter_type": "Internal",
      "value": "Sqrt[4/3*(mLre + 2*mNre)*gRho*fpi]",
      "tex": "m_\\eta",
      "description": "Mass of the composite singlet eta, Eq.(9)"
    },
    {
      "name": "Metap",
      "parameter_type": "Internal",
      "value": "Sqrt[3*aAnom/NHC]",
      "tex": "m_{\\eta'}",
      "description": "Mass of the eta-prime from the U(1)_A anomaly, m_etap^2 = 3 a/N, Eqs.(5),(6)"
    },
    {
      "name": "epsMix",
      "parameter_type": "Internal",
      "value": "I*Sqrt[2]*BB*gRho*fpi^2/MK2^2",
      "complex": true,
      "interaction_order": ["NP", 1],
      "tex": "\\epsilon",
      "description": "Higgs-Kaon mixing parameter epsilon = I Sqrt[2] (y - ytilde^*) gRho fpi^2/mK2^2, Eq.(12); tan(beta) = Abs[epsMix], Eq.(17)"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "K2p",
      "self_conjugate": false,
      "mass": {"sym": "MK2", "value": "Internal"},
      "width": {"sym": "WK2p", "value": "1."},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9000001,
      "particle_name": "K2+",
      "antiparticle_name": "K2-",
      "full_name": "Charged composite kaon",
      "propagator_label": "K2p",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "K2z",
      "self_conjugate": false,
      "mass": {"sym": "MK2z", "value": "Internal"},
      "width": {"sym": "WK2z", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9000002,
      "particle_name": "K20",
      "antiparticle_name": "K20~",
      "full_name": "Neutral composite kaon",
      "propagator_label": "K2z",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "pi3p",
      "self_conjugate": false,
      "mass": {"sym": "Mpi3", "value": "Internal"},
      "width": {"sym": "Wpi3p", "value": "1."},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9000003,
      "particle_name": "pi3+",
      "antiparticle_name": "pi3-",
      "full_name": "Charged composite pion triplet",
      "propagator_label": "pi3p",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "pi30",
      "self_conjugate": true,
      "mass": {"sym": "Mpi30", "value": "Internal"},
      "width": {"sym": "Wpi30", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9000004,
      "particle_name": "pi30",
      "full_name": "Neutral composite pion triplet",
      "propagator_label": "pi30",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "eta",
      "self_conjugate": true,
      "mass": {"sym": "Meta", "value": "Internal"},
      "width": {"sym": "Weta", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9000005,
      "particle_name": "eta0",
      "full_name": "Composite pion singlet eta",
      "propagator_label": "eta",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "etap",
      "self_conjugate": true,
      "mass": {"sym": "Metap", "value": "Internal"},
      "width": {"sym": "Wetap", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9000006,
      "particle_name": "etap",
      "full_name": "Composite eta-prime of the anomalous U(1)_A",
      "propagator_label": "etap",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 106,
      "class_name": "rlx",
      "self_conjugate": true,
      "mass": {"sym": "Mrlx", "value": "1.*^-9"},
      "width": {"massless": true, "sym": "Wrlx"},
      "quantum_numbers": {},
      "pdg": 9000007,
      "particle_name": "rlx",
      "full_name": "Relaxion",
      "propagator_label": "rlx",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 110,
      "class_name": "K2",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "1/2"},
      "unphysical": true,
      "definitions": ["K2[1] -> K2p", "K2[2] -> K2z"]
    },
    {
      "spin_type": "S",
      "class_index": 111,
      "class_name": "pi3",
      "self_conjugate": true,
      "indices": ["SU2W"],
      "flavor_index": "SU2W",
      "quantum_numbers": {},
      "unphysical": true,
      "definitions": [
        "pi3[1] -> (pi3pbar + pi3p)/Sqrt[2]",
        "pi3[2] -> (pi3pbar - pi3p)/(I*Sqrt[2])",
        "pi3[3] -> pi30"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LK2kin",
      "delayed": true,
      "expression": "Block[{ii, mu}, ExpandIndices[DC[K2bar[ii], mu] DC[K2[ii], mu] - MK2^2 K2bar[ii] K2[ii], FlavorExpand -> {SU2D, SU2W}]]"
    },
    {
      "name": "Lpi3kin",
      "delayed": true,
      "expression": "Block[{aa, mu}, ExpandIndices[1/2 DC[pi3[aa], mu] DC[pi3[aa], mu] - 1/2 Mpi3^2 pi3[aa] pi3[aa], FlavorExpand -> SU2W]]"
    },
    {
      "name": "Letakin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[1/2 del[eta, mu] del[eta, mu] - 1/2 Meta^2 eta eta]]"
    },
    {
      "name": "Letapkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[1/2 del[etap, mu] del[etap, mu] - 1/2 Metap^2 etap etap]]"
    },
    {
      "name": "Lrlxkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[1/2 del[rlx, mu] del[rlx, mu] - 1/2 Mrlx^2 rlx rlx]]"
    },
    {
      "name": "LKmix0",
      "delayed": true,
      "expression": "Block[{ii}, ExpandIndices[-I Sqrt[2] gRho fpi^2 BB K2bar[ii] Phi[ii], FlavorExpand -> SU2D]]"
    },
    {
      "name": "LKmix",
      "delayed": true,
      "expression": "LKmix0 + HC[LKmix0]"
    },
    {
      "name": "LKpi0",
      "delayed": true,
      "expression": "Block[{ii, jj, aa}, ExpandIndices[-Sqrt[2] gRho AA fpi (2 K2bar[ii] Ta[aa, ii, jj] Phi[jj] pi3[aa] - eta K2bar[ii] Phi[ii]/Sqrt[3]), FlavorExpand -> {SU2D, SU2W}]]"
    },
    {
      "name": "LKpi",
      "delayed": true,
      "expression": "LKpi0 + HC[LKpi0]"
    },
    {
      "name": "Leta3",
      "delayed": true,
      "expression": "Block[{ii, jj, aa}, ExpandIndices[gRho (mLim - mNim) eta/Sqrt[3] (4 fpi^2 - 2 eta eta/9) + 2 gRho eta/Sqrt[3] (mNim K2bar[ii] K2[ii] - mLim pi3[aa] pi3[aa]) + 4/3 gRho (2 mLim + mNim) K2bar[ii] Ta[aa, ii, jj] K2[jj] pi3[aa], FlavorExpand -> {SU2D, SU2W}]]"
    },
    {
      "name": "Lpi3anom",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si, aa}, ExpandIndices[g1 gw NHC/(64 Pi^2 fpi) Eps[mu, nu, ro, si] pi3[aa] FS[Wi, mu, nu, aa] FS[B, ro, si], FlavorExpand -> SU2W]]"
    },
    {
      "name": "Letaanom",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si, aa}, ExpandIndices[-NHC/(64 Sqrt[3] Pi^2 fpi) eta Eps[mu, nu, ro, si] (gw^2 FS[Wi, mu, nu, aa] FS[Wi, ro, si, aa] + g1^2 FS[B, mu, nu] FS[B, ro, si]), FlavorExpand -> SU2W]]"
    },
    {
      "name": "LVLCLN",
      "delayed": true,
      "expression": "LK2kin + Lpi3kin + Letakin + Letapkin + Lrlxkin + LKmix + LKpi + Leta3 + Lpi3anom + Letaanom"
    }
  ]
}
```
I read the paper, the schema, the renderer, and `SM.fr`. Nothing else exists here, and I opened no reference or cached `.fr` file.

## Physics content I extracted

The model is the L+N vector-like confinement theory (arXiv:1508.01112). Below the confinement scale the new states are the 9 pseudo-Goldstone bosons of SU(3)×SU(3)/SU(3), eq. (5):

| state | SU(3)c | SU(2)L | Y (SM.fr convention) | Q | mass |
|---|---|---|---|---|---|
| `K2` = (K2+, K2⁰) composite "Kaon" | singlet | doublet | +1/2 | +1, 0 | `MK2`, eq. (9) |
| `pi3` composite "Pion" triplet (π3±, π3⁰) | singlet | triplet | 0 | ±1, 0 | `Mpi3`, eq. (9) |
| `eta` composite singlet | singlet | singlet | 0 | 0 | `Meta`, eq. (9) |
| `etap` (η′, U(1)A anomaly) | singlet | singlet | 0 | 0 | `Metap` = Sqrt[3 a/N] |
| `rlx` relaxion φ, Sec. 4 | singlet | singlet | 0 | 0 | `Mrlx` (free) |

Hypercharge sign (rule 5): the paper's charge table uses Y = −1/2 Diag[1,1,0], but its own labels K2 = (K2+, K2⁰) and the mixing term K2†H both need Y(K2) = Y(H). SM.fr fixes Y(Phi) = +1/2, so I set **Y(K2) = +1/2**. Then Q(K2+) = +1 and Q(K2⁰) = 0, as the paper labels them, and K2bar[ii] Phi[ii] is a singlet.

The relaxion couples only to the hypercolour field strength (eq. 34), which is not a degree of freedom of the effective theory; θ_H enters through the phases of `mL`, `mN`, `y`, `ytilde` (eqs. 3–4, 35). So `rlx` gets only its free-field term.

## Self-audit table

| term | monomial | d | coupling | coupling dim (=4−d) | 1/Λ^(d−4) | Q sum | Y sum | SU(2) | SU(3) | new U(1) | L/B | CC[] | h.c. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `LK2kin` | DC[K2bar]DC[K2]; MK2² K2bar K2 | 4; 2 | 1; MK2² | 0; 2 | n/a | 0 | −1/2+1/2=0 | shared ii | singlet | none | n/a | n/a | self-conj (real) |
| `Lpi3kin` | DC[pi3]DC[pi3]; Mpi3² pi3 pi3 | 4; 2 | 1; Mpi3² | 0; 2 | n/a | 0 | 0 | adjoint aa shared | singlet | none | n/a | n/a | self-conj |
| `Letakin` | del[eta]del[eta]; Meta² eta² | 4; 2 | 1; Meta² | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj |
| `Letapkin` | del[etap]²; Metap² etap² | 4; 2 | 1; Metap² | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj |
| `Lrlxkin` | del[rlx]²; Mrlx² rlx² | 4; 2 | 1; Mrlx² | 0; 2 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | self-conj |
| `LKmix0` (eq. 8) | K2bar Phi | 2 | I√2 gRho fpi² BB | 2 | n/a | 0 | −1/2+1/2=0 | shared ii (doublet·anti-doublet) | singlet | none | n/a | n/a | `HC[]` in `LKmix` |
| `LKpi0` (eq. 8) | K2bar Ta[aa,ii,jj] Phi pi3; eta K2bar Phi | 3 | √2 gRho AA fpi | 1 | n/a | 0 | 0 | Ta[aa,ii,jj]; shared ii | singlet | none | n/a | n/a | `HC[]` in `LKpi` |
| `Leta3` a (eq. 8) | eta | 1 | gRho(mLim−mNim)4fpi²/√3 | 3 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | already Hermitian |
| `Leta3` b | eta³ | 3 | gRho(mLim−mNim)·2/(9√3) | 1 | n/a | 0 | 0 | singlet | singlet | none | n/a | n/a | Hermitian |
| `Leta3` c | eta K2bar K2; eta pi3 pi3 | 3 | 2 gRho mNim/√3; 2 gRho mLim/√3 | 1 | n/a | 0 | 0 | shared ii; shared aa | singlet | none | n/a | n/a | Hermitian |
| `Leta3` d | K2bar Ta[aa,ii,jj] K2 pi3 | 3 | 4/3 gRho(2mLim+mNim) | 1 | n/a | 0 | −1/2+1/2=0 | Ta[aa,ii,jj] | singlet | none | n/a | n/a | Hermitian |
| `Lpi3anom` (eq. 26) | pi3 FS[Wi] FS[B] | 5 | g1 gw NHC/(64π² fpi) | −1 | 1/fpi¹ ✔ | 0 | 0 | adjoint aa shared with W | singlet | none | n/a | n/a | Hermitian |
| `Letaanom` (eq. 26) | eta FS[Wi]FS[Wi]; eta FS[B]FS[B] | 5 | NHC gw²(g1²)/(64√3 π² fpi) | −1 | 1/fpi¹ ✔ | 0 | 0 | aa contracted on W W | singlet | none | n/a | n/a | Hermitian |

Every new class has a kinetic + mass term in the total sum `LVLCLN`. `fpi` is the EFT scale: it is External, in GeV, with `InteractionOrder -> {QED,-1}`, and the two anomaly operators (d = 5) carry `1/fpi`.

`SelfConjugate -> True` classes: `pi3`, `pi30`, `eta`, `etap`, `rlx` — none carries `QuantumNumbers`. The Y charge sits only on the Unphysical doublet `K2`, and Q only on the physical charged states `K2p`, `pi3p`.

Reference or cached model files read: **none**. No `psi^c` appears in the paper's new-physics terms, so no `CC[]` is needed.

```json
{
  "model_name": "VLC_LN_gen",
  "info": {
    "authors": ["O. Antipin", "M. Redi"],
    "version": "1.0",
    "date": "02. 09. 2026",
    "institutions": ["INFN, Sezione di Firenze"],
    "emails": ["oleg.antipin@fi.infn.it", "michele.redi@fi.infn.it"]
  },
  "interaction_order_hierarchy": [["QCD", 1], ["QED", 2], ["NP", 1]],
  "gauge_groups": [],
  "index_decls": [],
  "parameters": [
    {
      "name": "fpi",
      "parameter_type": "External",
      "value": "500.",
      "block_name": "VLCLN",
      "order_block": 1,
      "interaction_order": ["QED", -1],
      "tex": "f_\\pi",
      "description": "Composite pion decay constant [GeV]; EFT scale of the chiral Lagrangian, Eq.(6). The anomaly operators are dimension 5 and carry 1/fpi."
    },
    {
      "name": "gRho",
      "parameter_type": "External",
      "value": "7.",
      "block_name": "VLCLN",
      "order_block": 2,
      "interaction_order": ["NP", 1],
      "tex": "g_\\rho",
      "description": "Strong coupling of the SU(N) sector, gRho ~ 4 Pi/Sqrt[N], about 7 for N = 3, Eq.(6)"
    },
    {
      "name": "NHC",
      "parameter_type": "External",
      "value": "3.",
      "block_name": "VLCLN",
      "order_block": 3,
      "tex": "N",
      "description": "Number of hypercolours N of the confining SU(N) gauge group, Eq.(1)"
    },
    {
      "name": "mLre",
      "parameter_type": "External",
      "value": "20.",
      "block_name": "VLCLN",
      "order_block": 4,
      "tex": "Re m_L",
      "description": "Real part of the vector-like doublet mass mL [GeV], Eq.(2)"
    },
    {
      "name": "mLim",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "VLCLN",
      "order_block": 5,
      "tex": "Im m_L",
      "description": "Imaginary part of mL [GeV] (theta_H phase), Eqs.(3),(4),(8)"
    },
    {
      "name": "mNre",
      "parameter_type": "External",
      "value": "20.",
      "block_name": "VLCLN",
      "order_block": 6,
      "tex": "Re m_N",
      "description": "Real part of the singlet mass mN [GeV], Eq.(2)"
    },
    {
      "name": "mNim",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "VLCLN",
      "order_block": 7,
      "tex": "Im m_N",
      "description": "Imaginary part of mN [GeV] (theta_H phase), Eqs.(3),(4),(8)"
    },
    {
      "name": "yre",
      "parameter_type": "External",
      "value": "0.1",
      "block_name": "VLCLN",
      "order_block": 8,
      "interaction_order": ["NP", 1],
      "tex": "Re y",
      "description": "Real part of the Yukawa y of H L N^c, Eq.(2)"
    },
    {
      "name": "yim",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "VLCLN",
      "order_block": 9,
      "interaction_order": ["NP", 1],
      "tex": "Im y",
      "description": "Imaginary part of the Yukawa y, Eq.(2)"
    },
    {
      "name": "ytre",
      "parameter_type": "External",
      "value": "0.09",
      "block_name": "VLCLN",
      "order_block": 10,
      "interaction_order": ["NP", 1],
      "tex": "Re yt",
      "description": "Real part of the Yukawa ytilde of H^dagger L^c N, Eq.(2)"
    },
    {
      "name": "ytim",
      "parameter_type": "External",
      "value": "0.01",
      "block_name": "VLCLN",
      "order_block": 11,
      "interaction_order": ["NP", 1],
      "tex": "Im yt",
      "description": "Imaginary part of the Yukawa ytilde, Eq.(2). Im[y ytilde] is the CP violating phase that drives the EDM, Eq.(33)"
    },
    {
      "name": "aAnom",
      "parameter_type": "External",
      "value": "1.*^6",
      "block_name": "VLCLN",
      "order_block": 12,
      "tex": "a",
      "description": "U(1)_A anomaly parameter a [GeV^2], Eq.(6); it fixes the eta-prime mass, m_etap^2 = 3 a/N"
    },
    {
      "name": "thetaH",
      "parameter_type": "External",
      "value": "0.",
      "block_name": "VLCLN",
      "order_block": 13,
      "tex": "\\theta_H",
      "description": "Topological angle of the SU(N) gauge fields, Eq.(1). It is rotated into the phases of mL, mN, y, ytilde by Eqs.(3),(4), and is replaced by rlx/frlx in the relaxion scenario, Eq.(35)"
    },
    {
      "name": "frlx",
      "parameter_type": "External",
      "value": "1.*^9",
      "block_name": "VLCLN",
      "order_block": 14,
      "tex": "f",
      "description": "Relaxion decay constant f [GeV] of the axion-like coupling phi/f GGdual/(32 Pi^2), Eq.(34)"
    },
    {
      "name": "AA",
      "parameter_type": "Internal",
      "value": "yre + ytre + I*(yim - ytim)",
      "complex": true,
      "interaction_order": ["NP", 1],
      "tex": "A",
      "description": "A = y + Conjugate[ytilde], Eq.(2)"
    },
    {
      "name": "BB",
      "parameter_type": "Internal",
      "value": "yre - ytre + I*(yim + ytim)",
      "complex": true,
      "interaction_order": ["NP", 1],
      "tex": "B",
      "description": "B = y - Conjugate[ytilde], Eq.(2); it controls the Higgs-Kaon mixing"
    },
    {
      "name": "Mrho",
      "parameter_type": "Internal",
      "value": "gRho*fpi",
      "tex": "m_\\rho",
      "description": "Mass of the lightest vector resonance, m_rho = gRho fpi, Eq.(6)"
    },
    {
      "name": "MK2",
      "parameter_type": "Internal",
      "value": "Sqrt[9*gw^2*gRho^2*fpi^2/(4*(4*Pi)^2) + 2*(mLre + mNre)*gRho*fpi]",
      "tex": "m_{K_2}",
      "description": "Mass of the composite Kaon doublet K2, Eq.(9)"
    },
    {
      "name": "MK2z",
      "parameter_type": "Internal",
      "value": "MK2",
      "tex": "m_{K_2^0}",
      "description": "Mass of the neutral composite Kaon; degenerate with the charged one at this order, Eq.(9)"
    },
    {
      "name": "Mpi3",
      "parameter_type": "Internal",
      "value": "Sqrt[6*gw^2*gRho^2*fpi^2/(4*Pi)^2 + 4*mLre*gRho*fpi]",
      "tex": "m_{\\pi_3}",
      "description": "Mass of the composite pion triplet pi3, Eq.(9)"
    },
    {
      "name": "Mpi30",
      "parameter_type": "Internal",
      "value": "Mpi3",
      "tex": "m_{\\pi_3^0}",
      "description": "Mass of the neutral pion triplet member; degenerate with the charged one at this order, Eq.(9)"
    },
    {
      "name": "Meta",
      "parameter_type": "Internal",
      "value": "Sqrt[4/3*(mLre + 2*mNre)*gRho*fpi]",
      "tex": "m_\\eta",
      "description": "Mass of the composite singlet eta, Eq.(9)"
    },
    {
      "name": "Metap",
      "parameter_type": "Internal",
      "value": "Sqrt[3*aAnom/NHC]",
      "tex": "m_{\\eta'}",
      "description": "Mass of the eta-prime from the U(1)_A anomaly, m_etap^2 = 3 a/N, Eqs.(5),(6)"
    },
    {
      "name": "epsMix",
      "parameter_type": "Internal",
      "value": "I*Sqrt[2]*BB*gRho*fpi^2/MK2^2",
      "complex": true,
      "interaction_order": ["NP", 1],
      "tex": "\\epsilon",
      "description": "Higgs-Kaon mixing parameter epsilon = I Sqrt[2] (y - ytilde^*) gRho fpi^2/mK2^2, Eq.(12); tan(beta) = Abs[epsMix], Eq.(17)"
    }
  ],
  "particles": [
    {
      "spin_type": "S",
      "class_index": 100,
      "class_name": "K2p",
      "self_conjugate": false,
      "mass": {"sym": "MK2", "value": "Internal"},
      "width": {"sym": "WK2p", "value": "1."},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9000001,
      "particle_name": "K2+",
      "antiparticle_name": "K2-",
      "full_name": "Charged composite kaon",
      "propagator_label": "K2p",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 101,
      "class_name": "K2z",
      "self_conjugate": false,
      "mass": {"sym": "MK2z", "value": "Internal"},
      "width": {"sym": "WK2z", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9000002,
      "particle_name": "K20",
      "antiparticle_name": "K20~",
      "full_name": "Neutral composite kaon",
      "propagator_label": "K2z",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 102,
      "class_name": "pi3p",
      "self_conjugate": false,
      "mass": {"sym": "Mpi3", "value": "Internal"},
      "width": {"sym": "Wpi3p", "value": "1."},
      "quantum_numbers": {"Q": "1"},
      "pdg": 9000003,
      "particle_name": "pi3+",
      "antiparticle_name": "pi3-",
      "full_name": "Charged composite pion triplet",
      "propagator_label": "pi3p",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 103,
      "class_name": "pi30",
      "self_conjugate": true,
      "mass": {"sym": "Mpi30", "value": "Internal"},
      "width": {"sym": "Wpi30", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9000004,
      "particle_name": "pi30",
      "full_name": "Neutral composite pion triplet",
      "propagator_label": "pi30",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 104,
      "class_name": "eta",
      "self_conjugate": true,
      "mass": {"sym": "Meta", "value": "Internal"},
      "width": {"sym": "Weta", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9000005,
      "particle_name": "eta0",
      "full_name": "Composite pion singlet eta",
      "propagator_label": "eta",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 105,
      "class_name": "etap",
      "self_conjugate": true,
      "mass": {"sym": "Metap", "value": "Internal"},
      "width": {"sym": "Wetap", "value": "1."},
      "quantum_numbers": {},
      "pdg": 9000006,
      "particle_name": "etap",
      "full_name": "Composite eta-prime of the anomalous U(1)_A",
      "propagator_label": "etap",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 106,
      "class_name": "rlx",
      "self_conjugate": true,
      "mass": {"sym": "Mrlx", "value": "1.*^-9"},
      "width": {"massless": true, "sym": "Wrlx"},
      "quantum_numbers": {},
      "pdg": 9000007,
      "particle_name": "rlx",
      "full_name": "Relaxion",
      "propagator_label": "rlx",
      "propagator_type": "D",
      "propagator_arrow": "None"
    },
    {
      "spin_type": "S",
      "class_index": 110,
      "class_name": "K2",
      "self_conjugate": false,
      "indices": ["SU2D"],
      "flavor_index": "SU2D",
      "quantum_numbers": {"Y": "1/2"},
      "unphysical": true,
      "definitions": ["K2[1] -> K2p", "K2[2] -> K2z"]
    },
    {
      "spin_type": "S",
      "class_index": 111,
      "class_name": "pi3",
      "self_conjugate": true,
      "indices": ["SU2W"],
      "flavor_index": "SU2W",
      "quantum_numbers": {},
      "unphysical": true,
      "definitions": [
        "pi3[1] -> (pi3pbar + pi3p)/Sqrt[2]",
        "pi3[2] -> (pi3pbar - pi3p)/(I*Sqrt[2])",
        "pi3[3] -> pi30"
      ]
    }
  ],
  "lagrangian_terms": [
    {
      "name": "LK2kin",
      "delayed": true,
      "expression": "Block[{ii, mu}, ExpandIndices[DC[K2bar[ii], mu] DC[K2[ii], mu] - MK2^2 K2bar[ii] K2[ii], FlavorExpand -> {SU2D, SU2W}]]"
    },
    {
      "name": "Lpi3kin",
      "delayed": true,
      "expression": "Block[{aa, mu}, ExpandIndices[1/2 DC[pi3[aa], mu] DC[pi3[aa], mu] - 1/2 Mpi3^2 pi3[aa] pi3[aa], FlavorExpand -> SU2W]]"
    },
    {
      "name": "Letakin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[1/2 del[eta, mu] del[eta, mu] - 1/2 Meta^2 eta eta]]"
    },
    {
      "name": "Letapkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[1/2 del[etap, mu] del[etap, mu] - 1/2 Metap^2 etap etap]]"
    },
    {
      "name": "Lrlxkin",
      "delayed": true,
      "expression": "Block[{mu}, ExpandIndices[1/2 del[rlx, mu] del[rlx, mu] - 1/2 Mrlx^2 rlx rlx]]"
    },
    {
      "name": "LKmix0",
      "delayed": true,
      "expression": "Block[{ii}, ExpandIndices[-I Sqrt[2] gRho fpi^2 BB K2bar[ii] Phi[ii], FlavorExpand -> SU2D]]"
    },
    {
      "name": "LKmix",
      "delayed": true,
      "expression": "LKmix0 + HC[LKmix0]"
    },
    {
      "name": "LKpi0",
      "delayed": true,
      "expression": "Block[{ii, jj, aa}, ExpandIndices[-Sqrt[2] gRho AA fpi (2 K2bar[ii] Ta[aa, ii, jj] Phi[jj] pi3[aa] - eta K2bar[ii] Phi[ii]/Sqrt[3]), FlavorExpand -> {SU2D, SU2W}]]"
    },
    {
      "name": "LKpi",
      "delayed": true,
      "expression": "LKpi0 + HC[LKpi0]"
    },
    {
      "name": "Leta3",
      "delayed": true,
      "expression": "Block[{ii, jj, aa}, ExpandIndices[gRho (mLim - mNim) eta/Sqrt[3] (4 fpi^2 - 2 eta eta/9) + 2 gRho eta/Sqrt[3] (mNim K2bar[ii] K2[ii] - mLim pi3[aa] pi3[aa]) + 4/3 gRho (2 mLim + mNim) K2bar[ii] Ta[aa, ii, jj] K2[jj] pi3[aa], FlavorExpand -> {SU2D, SU2W}]]"
    },
    {
      "name": "Lpi3anom",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si, aa}, ExpandIndices[g1 gw NHC/(64 Pi^2 fpi) Eps[mu, nu, ro, si] pi3[aa] FS[Wi, mu, nu, aa] FS[B, ro, si], FlavorExpand -> SU2W]]"
    },
    {
      "name": "Letaanom",
      "delayed": true,
      "expression": "Block[{mu, nu, ro, si, aa}, ExpandIndices[-NHC/(64 Sqrt[3] Pi^2 fpi) eta Eps[mu, nu, ro, si] (gw^2 FS[Wi, mu, nu, aa] FS[Wi, ro, si, aa] + g1^2 FS[B, mu, nu] FS[B, ro, si]), FlavorExpand -> SU2W]]"
    },
    {
      "name": "LVLCLN",
      "delayed": true,
      "expression": "LK2kin + Lpi3kin + Letakin + Letapkin + Lrlxkin + LKmix + LKpi + Leta3 + Lpi3anom + Letaanom"
    }
  ]
}
```