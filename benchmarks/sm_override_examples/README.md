# Agents editing the SM sector from an add-on file

Each file is an agent-written FeynRules add-on that loads on top of SM.fr. The line numbers point at the SM class or parameter the agent touched.

| file | what the agent did | outcome |
|---|---|---|
| 1_pNG_redeclares_Phi.fr | redeclares `S[11] Phi` with `Phi[2] -> (vh + (ct h + st h2) + I G0)/Sqrt[2]` (line 126) and writes its own Higgs Lagrangian `LHiggsPng` (line 144) | compiles; mass check fails (SM.fr's `LHiggs` still added, so the Higgs sector is counted twice) |
| 1b_pNG_fixed_passes.fr | same file, names fixed to `H`, `vev`, `MH`, total written as `LTotal := LSM - LHiggs + LScalarPng` | passes all checks and MadGraph |
| 2_MDM_redeclares_Phi.fr | redeclares `Phi` with `Phi[2] -> (vev + h cs - sDM ss + I G0)/Sqrt[2]` and its own `LHiggsMDM` | compiles; mass check fails, same cause |
| 3_BL_overrides_lam_rotates_singlet_only.fr | redefines the SM parameter `lam == {Internal, Value -> lambda1BL}` (line 97); rotates only the singlet, `ChiBL -> (xBL - sa H + ca H2 + I GZp)/Sqrt[2]` (line 194); leaves `Phi` alone | compiles; `H`-`H2` cross term survives, mass check fails |
| 4_pSPSS_redeclares_LL.fr | redeclares the SM lepton doublet `LL` as Unphysical with the seesaw mixing in its Definitions (line 200) | compile timeout at 900 s |
| 5_331_embeds_SM_fields_in_new_multiplets.fr | defines new unphysical triplets `q1L`, `lL` whose components are SM `uq`, `dq`, `l`, `vl` plus the new states (lines 534 to 558); nothing redeclared | passes the full chain |
| 6_MDM_names_scalar_s.fr | names its new scalar `s`, which is the strange quark in SM.fr (line 100) | checks fail |
