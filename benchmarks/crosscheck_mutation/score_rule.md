# Crosscheck mutation test — rule-based scoring

cases scored: 32 mutants, 8 controls, 3 real-finding files

- mutants where a flagged row or severity line names the mutated symbol: **22/32**
- controls: flagged rows / substantive lines per file: Top-Philic-Zprime 6/0, EffLRSM 2/1, GeneralU1 7/2, 368sextets 4/1, ChernSimonsPortal 8/0, pNG 11/4, 331 25/9, Monotops 9/2

## Judge (subagent reading crosscheck.md against the defect description)

- mutants named: yes 31, partial 0, no 1 of 32
- real findings named: yes 2, partial 1, no 0 of 3
- other substantive disagreements per file: mutants mean 2.1, controls mean 3.0

| operator | yes | partial | no |
|---|---|---|---|
| drop_cc | 2 | 0 | 0 |
| drop_cutoff | 1 | 0 | 0 |
| drop_eps | 1 | 0 | 0 |
| drop_term | 8 | 0 | 0 |
| factor2 | 8 | 0 | 0 |
| flip_charge | 5 | 0 | 0 |
| sqrt_swap | 3 | 0 | 0 |
| swap_chirality | 3 | 0 | 1 |

| case | kind | operator | term | flagged rows | substantive | rule hit | judge | other subst. |
|---|---|---|---|---|---|---|---|---|
| Top-Philic-Zprime__control | control |  |  | 6/30 | 0 | n/a | n/a | 1 |
| Top-Philic-Zprime__factor2 | mutant | factor2 | LV1Top | 5/20 | 2 | yes | yes | 1 |
| Top-Philic-Zprime__drop_term | mutant | drop_term | LV1Top | 4/23 | 1 | no | yes | 0 |
| Top-Philic-Zprime__swap_chirality | mutant | swap_chirality | LV1Kin | 8/19 | 1 | yes | no | 1 |
| EffLRSM__control | control |  |  | 2/23 | 1 | n/a | n/a | 1 |
| EffLRSM__flip_charge | mutant | flip_charge | WR | 7/29 | 1 | yes | yes | 0 |
| EffLRSM__drop_cc | mutant | drop_cc | LWRl | 8/30 | 0 | yes | yes | 0 |
| EffLRSM__sqrt_swap | mutant | sqrt_swap | nZRq | 6/35 | 0 | no | yes | 0 |
| EffLRSM__factor2 | mutant | factor2 | LWRq | 4/26 | 1 | no | yes | 0 |
| EffLRSM__drop_term | mutant | drop_term | LZRl | 3/24 | 0 | no | yes | 0 |
| EffLRSM__swap_chirality | mutant | swap_chirality | LWRq | 6/30 | 2 | yes | yes | 0 |
| GeneralU1__control | control |  |  | 7/40 | 2 | n/a | n/a | 3 |
| GeneralU1__drop_eps | mutant | drop_eps | LNuYuk | 6/32 | 1 | yes | yes | 0 |
| GeneralU1__flip_charge | mutant | flip_charge | NR | 7/43 | 3 | yes | yes | 3 |
| GeneralU1__sqrt_swap | mutant | sqrt_swap | MHX | 6/34 | 4 | yes | yes | 3 |
| GeneralU1__factor2 | mutant | factor2 | LZpF | 6/28 | 3 | yes | yes | 2 |
| GeneralU1__drop_term | mutant | drop_term | LPotX | 4/34 | 0 | no | yes | 1 |
| 368sextets__control | control |  |  | 4/21 | 1 | n/a | n/a | 1 |
| 368sextets__flip_charge | mutant | flip_charge | Phiu | 6/24 | 1 | yes | yes | 0 |
| 368sextets__drop_cutoff | mutant | drop_cutoff | LPsiuG | 4/20 | 1 | yes | yes | 0 |
| 368sextets__drop_cc | mutant | drop_cc | LPsiuG | 4/25 | 1 | yes | yes | 0 |
| 368sextets__factor2 | mutant | factor2 | LPsiuG | 5/26 | 0 | yes | yes | 0 |
| 368sextets__drop_term | mutant | drop_term | LPhidG | 1/11 | 0 | yes | yes | 0 |
| 368sextets__swap_chirality | mutant | swap_chirality | LPsiuG | 8/27 | 1 | yes | yes | 0 |
| ChernSimonsPortal__control | control |  |  | 8/19 | 0 | n/a | n/a | 3 |
| ChernSimonsPortal__factor2 | mutant | factor2 | LPortalNeutral | 8/26 | 1 | no | yes | 2 |
| ChernSimonsPortal__drop_term | mutant | drop_term | LPortalCharged | 8/21 | 1 | yes | yes | 2 |
| pNG__control | control |  |  | 11/32 | 4 | n/a | n/a | 4 |
| pNG__factor2 | mutant | factor2 | LX | 9/25 | 4 | yes | yes | 4 |
| pNG__drop_term | mutant | drop_term | LPortal4 | 12/27 | 4 | no | yes | 3 |
| 331__control | control |  |  | 25/51 | 9 | n/a | n/a | 9 |
| 331__flip_charge | mutant | flip_charge | DQ | 16/44 | 3 | yes | yes | 7 |
| 331__sqrt_swap | mutant | sqrt_swap | v2 | 20/42 | 9 | yes | yes | 8 |
| 331__factor2 | mutant | factor2 | LZp | 28/54 | 0 | no | yes | 7 |
| 331__drop_term | mutant | drop_term | LNPcc | 32/55 | 7 | no | yes | 8 |
| 331__swap_chirality | mutant | swap_chirality | LNPcc | 16/39 | 0 | yes | yes | 10 |
| Monotops__control | control |  |  | 9/32 | 2 | n/a | n/a | 2 |
| Monotops__flip_charge | mutant | flip_charge | vphi | 7/23 | 2 | yes | yes | 1 |
| Monotops__factor2 | mutant | factor2 | Lphiu | 4/30 | 2 | yes | yes | 1 |
| Monotops__drop_term | mutant | drop_term | LXChi | 4/21 | 0 | no | yes | 2 |
| EffLRSM__real | real | physicist_finding |  | 9/31 | 2 | n/a | yes | 0 |
| GeneralU1__real | real | physicist_finding |  | 8/42 | 0 | n/a | partial | 2 |
| 368sextets__real | real | physicist_finding |  | 2/23 | 0 | n/a | yes | 1 |
