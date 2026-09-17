I fixed the model by correcting the treatment of the right-handed neutrino field `vR`.

What I changed, in `model.fr`:

1. **`vR` class**: changed `SelfConjugate -> False` to `SelfConjugate -> True`, and removed the `AntiParticleName -> {"veR~", "vmR~", "vtR~"}` line.
2. **Mass term**: changed `LkinNuR` from `- MvR bar[vR][sp1,i].vR[sp1,i]` to `- 1/2 MvR bar[vR][sp1,i].vR[sp1,i]`.

Why this was needed. `vR` has only one chirality (`Chirality -> R`) and no left-handed partner class. A field with a single chirality cannot carry a Dirac mass — the bilinear `bar[psi].psi` is identically zero for a purely chiral 4-component spinor. This is why FeynRules could not read the mass term: it saw a term that did not fit its Dirac mass pattern, so it flagged the mass matrix as non-diagonal and could not compute the mass spectrum.

The physical intent here is a heavy Majorana right-handed neutrino, the standard field content for this class of W' + right-handed-neutrino model. Marking `vR` as `SelfConjugate -> True` tells FeynRules to build the full 4-component Majorana field from the right-handed piece and its charge conjugate. With that field structure, `bar[vR].vR` is a valid, non-zero mass bilinear. The standard Majorana mass convention has a `1/2` coefficient (so the pole mass equals the declared `MvR`), so I added that factor. I also removed `AntiParticleName`, because a self-conjugate (Majorana) particle is its own antiparticle — keeping a separate antiparticle name conflicts with `SelfConjugate -> True` and would show up as a duplicate-name error.

No other fields, couplings, or parameter values were touched. The `Wp` mass term, the W'-fermion coupling terms, and quantum numbers are unchanged, so the physics content (charges, couplings, mixing matrices) is preserved.