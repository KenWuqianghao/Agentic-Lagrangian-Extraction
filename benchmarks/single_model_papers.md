# Which benchmark papers define exactly one model?

One reader plus two adversarial refuters per paper (a physics-content lens and a reference-file lens). A paper is selected only when every vote cast agrees.

`scorable` additionally requires that the benchmark's reference `.fr` implements the paper's model — five pairings do not, and a field-F1 against those measures nothing.

| page | single model | scorable | votes | models (reader) | reference implements | confusion risk |
|---|---|---|---|---|---|---|
| 331 | yes | yes | 3/3 | 1: 331 model with general beta (SU(3)C x SU(3)L x U(1)X; scalar triplets rho, eta,  | 331.fr implements the general-beta 331 model of Sec. 2 with beta as an | medium |
| 368sextets | CONTESTED | no | 2/3 | 2: Sextet fermion qg-portal model (eq. 12: Psi_u, Psi_d); Sextet scalar q-lepton-g  | all-in-one | medium |
| ALRM_general | yes | yes | 3/3 | 1: ALRSM (alternative left-right symmetric model: SU(3)c x SU(2)L x SU(2)R' x U(1)B | ALRSM | low |
| B-L-SM | yes | yes | 3/3 | 1: Minimal gauged U(1)_B-L extension of the SM (Z' gauge boson, SM-singlet scalar c | The paper's single model: the minimal (pure) B-L model with no U(1)_Y- | low |
| CHEIDI | no | no | 0/3 | 0:  | none of the paper's content. HEIDI.fr implements the compact-extra-dim | high |
| ChernSimonsPortal | yes | yes | 3/3 | 1: SM + anomalous U(1)_X vector boson X with D'Hoker-Farhi/Chern-Simons couplings c | The low-energy effective model of Sec. 2 (eq. 1, eq. 5) and Sec. 5 (ve | medium |
| DMsimp | no | no | 0/3 | 2: Spin-0 mediator Y0 (scalar/pseudoscalar couplings) + Dirac DM chi, top-philic; S | none (dm_s_spin2.fr is a spin-2 mediator model the paper never defines | high |
| EffLRSM | yes | yes | 3/3 | 1: Effective LRSM (SM + WR, ZR, three Majorana N) | Effective LRSM (SM + WR, ZR, three Majorana N) | low |
| GeneralU1 | yes | yes | 3/3 | 1: Minimal U(1)X extension (U(1)X = xH*U(1)Y + xPhi*U(1)B-L) with Z', 3 RHNs and si | Minimal U(1)X extension (the only model in the paper) | medium |
| HNLs | no | no | 0/3 | 2: Majorana HNL (type-I seesaw, Eq. 2.1: n singlets N_R with Majorana mass); Dirac  | Dirac HNL model (Eq. 2.3, one heavy N4, mixing matrix of Eq. B.1). The | high |
| HeavyN | yes | yes | 3/3 | 1: SM + heavy (Majorana) neutrino N with phenomenological active-heavy mixing V_lN  | heavyN.fr implements the paper's single model (SM + heavy Majorana N w | medium |
| HiggsCharacterisation | no | no | 0/2 | 3: Spin-0 X0 (CP-mixed scalar, 0+/0- via angle alpha; eqs. 2.2, 2.4); Spin-1 X1 (1+ | all-in-one | high |
| LeptoQuark | yes | no | 3/3 | 1: U1 + Z' + G' phenomenological vector-triplet model (eqs. 9-11, textures eq. 13) | none: VLferm.fr is a vector-like fermion add-on (Ln, Le, Qu, Qd; doubl | high |
| MDMmodel | yes | yes | 3/3 | 1: Minimal Dilaton Model (SM + singlet scalar S + vector-like top partner T) | Minimal Dilaton Model (the only model in the paper) | low |
| MSSMD | no | no | 0/3 | 2: NMSSM benchmark (h1,2 -> 2 a1 -> 4 mu); Dark SUSY benchmark (MSSM + broken U(1)_ | Dark SUSY benchmark (MSSM + broken U(1)_D with dark photon AD and dark | high |
| Monotops | yes | yes | 3/3 | 1: Monotop simplified effective theory (Eq. 1): SM + invisible scalar phi, invisibl | The single Eq. (1) simplified model; all six fields present (SMET=phi, | low |
| NJLComposite | yes | yes | 3/3 | 1: NJL composite scalar leptoquark model (R2 and R2-tilde SU(2) doublets, colour tr | the single NJL composite scalar LQ model of Sec. II (Table I, Eqs. 1-3 | medium |
| SLQrules | yes | yes | 3/3 | 1: SM + all five scalar leptoquarks (Phi1, Phi1~, Phi2, Phi2~, Phi3) with complete  | all-in-one | low |
| SMWeinberg | yes | yes | 3/3 | 1: SMWeinberg: SM + d=5 Weinberg operator, implemented as one auxiliary Majorana ne | SMWeinberg (the paper's single model, via the auxiliary-N prescription | medium |
| Sextets | no | no | 0/3 | 2: Antitriplet scalar diquark (3bar of SU(3)C, Eq. 2.1 with K_abc = eps_abc/sqrt2,  | Sextet scalar diquark only, as an all-in-one file: three colour-sextet | high |
| Top-Philic-Zprime | yes | yes | 3/3 | 1: Top-philic colour-singlet vector resonance V1 (simplified model) | Top-philic colour-singlet vector resonance V1 (simplified model) | low |
| Triplets | no | no | 0/3 | 2: Antitriplet (3bar) scalar diquark D, with Table 1 EW options; Sextet (6) scalar  | Antitriplet scalar diquark only, Table 1 row 1 (SU(2)_L singlet, |Y|=1 | high |
| VLC_LN | undecided | no | 1/1 | 1: L+N half-composite 2HDM: SU(N) confining theory with Dirac fermions L (SM lepton | Only a collider subset of the L+N model: the pion triplet (pi0, pi+) w | high |
| VLQ | no | no | 0/3 | 2: Vector-like SU(2)_L singlet t' (Q=+2/3) with t-t' mixing angle theta (Sec. 2.1); | unclear; closest match is model 1 (vector-like t' singlet) as the T(2/ | high |
| Wprime | yes | yes | 3/3 | 1: General W' with arbitrary left/right (C^L, C^R) couplings to quarks and leptons  | General W' of Eq. (1): weff.fr (M$ModelName 'WEff', cites Sullivan PRD | medium |
| pNG | yes | yes | 3/3 | 1: pNG DM: SM + complex scalar singlet S with softly broken global U(1) (Higgs port | the pNG DM model of Sec. 2 (the only model in the paper) | low |
| pSPSS | yes | yes | 3/3 | 1: pSPSS (phenomenological symmetry protected seesaw scenario: SM + two sterile Maj | pSPSS (section 4.3 / section 5.1 of the paper) | low |
| topBSM | yes | no | 3/3 | 1: SM + flavour-changing top-Higgs dim-6 EFT (O_uphi + O_uG, flavour structures (1, | the single paper model: SM + O_uphi and O_uG for all four flavour stru | low |

**Selected, single-model (18):** 331, ALRM_general, B-L-SM, ChernSimonsPortal, EffLRSM, GeneralU1, HeavyN, LeptoQuark, MDMmodel, Monotops, NJLComposite, SLQrules, SMWeinberg, Top-Philic-Zprime, Wprime, pNG, pSPSS, topBSM

**Of those, scorable against their reference (16):** 331, ALRM_general, B-L-SM, ChernSimonsPortal, EffLRSM, GeneralU1, HeavyN, MDMmodel, Monotops, NJLComposite, SLQrules, SMWeinberg, Top-Philic-Zprime, Wprime, pNG, pSPSS

## Excluded, and why

- **368sextets** (contested): 2 models: Sextet fermion qg-portal model (eq. 12: Psi_u, Psi_d); Sextet scalar q-lepton-g model (eq. 13: Phi_u, Phi_d)
- **CHEIDI** (multi-model): 0 models: 
- **DMsimp** (multi-model): 2 models: Spin-0 mediator Y0 (scalar/pseudoscalar couplings) + Dirac DM chi, top-philic; Spin-1 mediator Y1 (vector/axial-vector couplings) + Dirac DM chi, top (+bottom f
- **HNLs** (multi-model): 2 models: Majorana HNL (type-I seesaw, Eq. 2.1: n singlets N_R with Majorana mass); Dirac / pseudo-Dirac HNL (inverse or linear seesaw, Eq. 2.3: 2n singlets in pairs N_L,
- **HiggsCharacterisation** (multi-model): 3 models: Spin-0 X0 (CP-mixed scalar, 0+/0- via angle alpha; eqs. 2.2, 2.4); Spin-1 X1 (1+/1- via kappa conditions; eqs. 2.8, 2.11, 2.12); Spin-2 X2 (2+, couples to SM en
- **LeptoQuark** (pairing): reference VLferm.fr is a vector-like-fermion add-on the paper never defines; the paper's U1+Z'+G' model is in vector_LQ.fr/Zprime.fr/coloron.fr
- **MSSMD** (multi-model): 2 models: NMSSM benchmark (h1,2 -> 2 a1 -> 4 mu); Dark SUSY benchmark (MSSM + broken U(1)_D: h -> 2 n1 -> 2 nD + 2 gamma_D -> 4 mu + X)
- **Sextets** (multi-model): 2 models: Antitriplet scalar diquark (3bar of SU(3)C, Eq. 2.1 with K_abc = eps_abc/sqrt2, flavour-antisymmetric couplings); Sextet scalar diquark (6 of SU(3)C, Eq. 2.1 wi
- **Triplets** (multi-model): 2 models: Antitriplet (3bar) scalar diquark D, with Table 1 EW options; Sextet (6) scalar diquark D, with Table 1 EW options
- **VLC_LN** (undecided): 1 models: L+N half-composite 2HDM: SU(N) confining theory with Dirac fermions L (SM lepton doublet) and N (singlet); low-energy pion octet = triplet pi3 + composite Higgs
- **VLQ** (multi-model): 2 models: Vector-like SU(2)_L singlet t' (Q=+2/3) with t-t' mixing angle theta (Sec. 2.1); Sequential fourth generation t', b' with unitary 4x4 CKM (Sec. 2.2)
- **topBSM** (pairing): reference now thu.fr (flavour-changing Higgs currents, 0 new fields); the old topBSM.fr pairing was a different paper
