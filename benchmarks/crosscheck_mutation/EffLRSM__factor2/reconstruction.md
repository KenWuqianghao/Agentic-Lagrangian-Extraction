# Reconstruction of `sanitized.fr`

## 0. Conventions used below

- `ProjP` $= P_R = \tfrac{1+\gamma^5}{2}$, `ProjM` $= P_L = \tfrac{1-\gamma^5}{2}$ (FeynRules convention).
- `Ga[mu]` $=\gamma^\mu$. `HC[...]` $=$ hermitian conjugate. `CC[\psi]` $=\psi^c$, so `CC[vlbar]` $=\overline{\nu^c}$.
- `FS[V,mu,nu]` for a field with **no** gauge index is the abelian field strength $V_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu$.
- `WRbar` is the conjugate of `WR`; the particle named `wr+` carries $Q=+1$, so I write the field as $W_R^{+\mu}$ and its conjugate as $W_R^{-\mu}$.
- Flavour indices $i,j$ run over `Generation` $=1,2,3$. Colour is summed implicitly inside the SM quark fields.
- $g_w$ (`gw`), $s_w$ (`sw`), $c_w$ (`cw`), the SM fields $u$, $d$, $\ell$, $\nu_\ell$ and $\mathcal{L}_{\rm SM}$ all come from the imported SM model file; they are not redefined here.

### Gauge content of the covariant derivative

**No `DC` appears anywhere in this file.** This is important and is a statement about the model, not an omission:

- The two new vectors $W_R^\pm$ and $Z_R$ are **not gauge fields of a new gauged group**. They enter only through abelian field strengths and explicit Proca mass terms, so they have **no triple or quartic self-couplings** and no coupling to the SM gauge sector. They are massive vector resonances coupled to fixed fermion currents — an *effective* (current-coupled) left-right construction rather than a linearly realised $SU(2)_R\times U(1)_{B-L}$ model.
- $N_R$ is a complete singlet of $SU(3)_C\times SU(2)_L\times U(1)_Y$ (no colour index, no $SU(2)$ rep, no $Q$ declared), so its covariant derivative reduces to the plain partial derivative, which is exactly what the file writes: `del[NR, mu]` $=\partial_\mu N$.
- The only covariant derivative in the full model is the SM one, inherited through `LSM`:
  $$D_\mu = \partial_\mu - i g_s T^a G^a_\mu - i g_w T^k W^k_\mu - i g_1 Y B_\mu .$$

---

## 1. Lagrangian

### 1.1 `LWRkin` — $W_R$ kinetic + mass (complex Proca field)

$$
\mathcal{L}_{W_R}^{\rm kin}
= -\frac{1}{2}\,W^{-}_{R\,\mu\nu}\,W_R^{+\,\mu\nu}
\;+\; M_{W_R}^{2}\, W^{-}_{R\,\mu}\, W_R^{+\,\mu},
\qquad
W_R^{\pm}{}_{\mu\nu}=\partial_\mu W^{\pm}_{R\,\nu}-\partial_\nu W^{\pm}_{R\,\mu}.
$$

(The $-\tfrac12$ and the unit-coefficient mass term are the standard normalisation for a *complex* vector, equivalent to $-\tfrac14 F^2 + \tfrac12 M^2 V^2$ per real degree of freedom.)

### 1.2 `LZRkin` — $Z_R$ kinetic + mass (real Proca field)

$$
\mathcal{L}_{Z_R}^{\rm kin}
= -\frac{1}{4}\, Z_{R\,\mu\nu} Z_R^{\mu\nu}
\;+\; \frac{1}{2} M_{Z_R}^{2}\, Z_{R\,\mu} Z_R^{\mu},
\qquad
Z_{R\,\mu\nu}=\partial_\mu Z_{R\,\nu}-\partial_\nu Z_{R\,\mu}.
$$

### 1.3 `LNkin` — heavy neutral lepton kinetic + Majorana mass

$$
\mathcal{L}_{N}^{\rm kin}
= \frac{i}{2}\,\overline{N_f}\,\gamma^\mu \partial_\mu N_f
\;-\; \frac{1}{2}\, M_{N_f}\, \overline{N_f} N_f ,
\qquad f=1,2,3 \;\; (\text{summed}).
$$

The $\tfrac12$ factors are the Majorana normalisation; `SelfConjugate -> True` means $N_f^c=N_f$, so the mass term is a genuine Majorana mass and lepton number is violated by two units.

### 1.4 `LWRq` — right-handed charged current, quarks

The file builds `tmp` and returns `2 (tmp + HC[tmp])`, i.e. the whole quark charged current (including its h.c.) is multiplied by an **overall factor 2**:

$$
\mathcal{L}_{W_R}^{q}
= 2\left[\;-\frac{\kappa_R^{q} g_w}{\sqrt{2}}\;
\overline{u}_i \,(V^{R}_{\rm CKM})_{ij}\, \gamma^\mu P_R\, d_j \; W^{+}_{R\,\mu}
\;+\;{\rm h.c.}\right]
$$

$$
= -\sqrt{2}\,\kappa_R^{q} g_w \left[
\overline{u}_i (V^{R}_{\rm CKM})_{ij}\gamma^\mu P_R d_j\, W^{+}_{R\,\mu}
+ \overline{d}_j (V^{R\,\dagger}_{\rm CKM})_{ji}\gamma^\mu P_R u_i\, W^{-}_{R\,\mu}\right].
$$

**Note on normalisation.** The natural left-right normalisation, and the one used for the lepton term in the very same file, is $-\dfrac{\kappa_R g_w}{\sqrt2}(\dots)+{\rm h.c.}$ with **no** prefactor. The quark term here carries an extra overall factor of 2, so the quark $W_R$ coupling is twice the lepton one at equal $\kappa_R$. I reproduce it as written; a reader should treat this factor as a deliberate feature of *this* file, not as the conventional left-right normalisation.

### 1.5 `LWRl` — right-handed charged current, leptons

$$
\mathcal{L}_{W_R}^{\ell}
= -\frac{\kappa_R^{\ell} g_w}{\sqrt{2}}
\left[\;\overline{N}_i\,(Y_N)_{ij}\,\gamma^\mu P_R\,\ell_j
\;+\;\overline{\nu^{c}_{i}}\,(X_N)_{ij}\,\gamma^\mu P_R\,\ell_j \right] W^{+}_{R\,\mu}
\;+\;{\rm h.c.}
$$

Two currents couple to $W_R^+$:

- $\overline{N}\,Y_N\,\gamma^\mu P_R\,\ell$ — the heavy Majorana neutrino paired with a right-handed charged lepton. This is the $\Delta L$-violating door (through the Majorana mass of $N$).
- $\overline{\nu^{c}}\,X_N\,\gamma^\mu P_R\,\ell$ — the charge-conjugated light neutrino paired with a right-handed charged lepton, a direct light-neutrino $W_R$ coupling. Its coefficient matrix $X_N$ is set to **zero** numerically, so this current is switched off in the default benchmark point while remaining present in the Feynman rules.

### 1.6 `LZRq` — neutral current, quarks

$$
\mathcal{L}_{Z_R}^{q}
= -\frac{\kappa_R^{q} g_w}{n^{q}_{Z_R}}
\left[
g_L^{u}\,\overline{u}\gamma^\mu P_L u
+ g_R^{u}\,\overline{u}\gamma^\mu P_R u
+ g_L^{d}\,\overline{d}\gamma^\mu P_L d
+ g_R^{d}\,\overline{d}\gamma^\mu P_R d
\right] Z_{R\,\mu}
$$

Flavour diagonal and generation universal (no mixing matrix appears).

### 1.7 `LZRl` — neutral current, leptons

$$
\mathcal{L}_{Z_R}^{\ell}
= -\frac{\kappa_R^{\ell} g_w}{n^{\ell}_{Z_R}}
\left[
g_L^{e}\,\overline{\ell}\gamma^\mu P_L \ell
+ g_R^{e}\,\overline{\ell}\gamma^\mu P_R \ell
+ g_L^{\nu}\,\overline{\nu}\gamma^\mu P_L \nu
+ g_R^{N}\,\overline{N}\gamma^\mu P_R N
\right] Z_{R\,\mu}
$$

The light neutrinos couple only through their **left-handed** component ($P_L$, coefficient $g_L^\nu$); there is no $P_R$ light-neutrino current. The heavy $N$ couples only through its **right-handed** component, with $g_R^{N}=1/2$ exactly, i.e. pure $T^3_R$, independent of $\kappa_R^\ell$ and $\theta_W$.

### 1.8 `LTotal`

$$
\mathcal{L}_{\rm tot}=\mathcal{L}_{\rm SM}
+\mathcal{L}_{W_R}^{\rm kin}+\mathcal{L}_{Z_R}^{\rm kin}+\mathcal{L}_{N}^{\rm kin}
+\mathcal{L}_{W_R}^{q}+\mathcal{L}_{W_R}^{\ell}
+\mathcal{L}_{Z_R}^{q}+\mathcal{L}_{Z_R}^{\ell}.
$$

---

## 2. Field table

| `.fr` class | Symbol | Spin | $SU(3)_C$ | $SU(2)_L$ | $U(1)$ charge | Self-conj. | Mass symbol | Mass value (GeV) | Width (GeV) | PDG |
|---|---|---|---|---|---|---|---|---|---|---|
| `V[100]` `WR` | $W_R^{\pm}$ | 1 | singlet (no colour index) | not declared (singlet) | $Q=+1$ | No | `MWR` | 3000. | `WWR` = 84.3 | 9900024 |
| `V[101]` `ZR` | $Z_R$ | 1 | singlet | not declared (singlet) | $Q=0$ | Yes | `MZR` | 5070. | `WZR` = 114. | 9900023 |
| `F[100]` `NR` (`n1,n2,n3`) | $N_{1,2,3}$ | 1/2 | singlet | not declared (singlet) | $Q=0$ | Yes (Majorana) | `MN` = {`mn1`,`mn2`,`mn3`} | 173.3, $10^{12}$, $10^{12}$ | `Wn1` = $2.12\times10^{-8}$, `Wn2` = `Wn3` = 0 | 9900012 / 9900014 / 9900016 |

Notes:

- No class declares `Indices -> {Index[Colour]}` or an $SU(2)$ representation, so **every new state is a complete SM gauge singlet** apart from the electric charge assigned to $W_R$.
- `NR` carries `Index[Generation]` with `FlavorIndex -> Generation`: three Majorana states, hierarchical spectrum (one at the top-quark scale, two effectively decoupled at $10^{12}$ GeV). Only $N_1$ has a non-zero width, so only $N_1$ is a physically propagating resonance at collider energies.

---

## 3. Parameters

### 3.1 External parameters (the only free inputs)

| Symbol | `.fr` name | Block / order | Value | Interaction order | Multiplies | Physical meaning |
|---|---|---|---|---|---|---|
| $\kappa_R^{q}$ | `kapRq` | `LRSMINPUTS`, 1 | 1. | `{NP,1}` | the whole quark $W_R$ current (`LWRq`) and the quark $Z_R$ current (`LZRq`); also enters $n^q_{Z_R}$ and every $g_{L,R}^{u,d}$ | ratio of the right-handed gauge coupling to the SM one in the **quark** sector, $\kappa_R^q = g_R/g_L$ for quarks |
| $\kappa_R^{\ell}$ | `kapRl` | `LRSMINPUTS`, 2 | 1. | `{NP,1}` | the lepton $W_R$ current (`LWRl`) and the lepton $Z_R$ current (`LZRl`); also enters $n^\ell_{Z_R}$ and $g_{L,R}^{e},g_L^{\nu}$ | same ratio in the **lepton** sector; independent of $\kappa_R^q$, so quark and lepton right-handed couplings can be varied separately |

Everything else is `Internal` (derived), including the three flavour matrices.

### 3.2 Internal parameters

| Symbol | `.fr` name | Definition | Meaning |
|---|---|---|---|
| $t_W^2$ | `tw2` | $s_w^2/c_w^2$ | $\tan^2\theta_W$ |
| $n^q_{Z_R}$ | `nZRq` | $\sqrt{1-t_W^2/(\kappa_R^{q})^2}$ | normalisation of the quark $Z_R$ coupling; requires $(\kappa_R^{q})^2>t_W^2$ for a real coupling |
| $n^\ell_{Z_R}$ | `nZRl` | $\sqrt{1-t_W^2/(\kappa_R^{\ell})^2}$ | same for leptons |
| $g_L^{u}$ | `gLZRu` | $-\tfrac16\, t_W^2/(\kappa_R^{q})^2$ | left-handed up-quark $Z_R$ charge |
| $g_R^{u}$ | `gRZRu` | $\tfrac12-\tfrac23\, t_W^2/(\kappa_R^{q})^2$ | right-handed up-quark $Z_R$ charge |
| $g_L^{d}$ | `gLZRd` | $-\tfrac16\, t_W^2/(\kappa_R^{q})^2$ | left-handed down-quark $Z_R$ charge (equal to $g_L^u$, as it must be for an $SU(2)_L$ doublet) |
| $g_R^{d}$ | `gRZRd` | $-\tfrac12+\tfrac13\, t_W^2/(\kappa_R^{q})^2$ | right-handed down-quark $Z_R$ charge |
| $g_L^{e}$ | `gLZRe` | $+\tfrac12\, t_W^2/(\kappa_R^{\ell})^2$ | left-handed charged-lepton $Z_R$ charge |
| $g_R^{e}$ | `gRZRe` | $-\tfrac12+ t_W^2/(\kappa_R^{\ell})^2$ | right-handed charged-lepton $Z_R$ charge |
| $g_L^{\nu}$ | `gLZRv` | $+\tfrac12\, t_W^2/(\kappa_R^{\ell})^2$ | left-handed light-neutrino $Z_R$ charge (equal to $g_L^e$, doublet partner) |
| $g_R^{N}$ | `gRZRn` | $\tfrac12$ | right-handed heavy-neutrino $Z_R$ charge, pure $T^3_R$ |
| $V^{R}_{\rm CKM}$ | `VCKMR` | $\mathbb{1}_{3\times3}$, `Unitary -> True` | right-handed quark mixing matrix in the $W_R$ current; set to the identity (no right-handed flavour violation at the default point) |
| $Y_N$ | `YN` | $\mathbb{1}_{3\times3}$ | $N$–$\ell$ mixing in the $W_R$ current; identity, so $N_i$ couples to $\ell_i$ only (one heavy neutrino per lepton flavour) |
| $X_N$ | `XN` | $0_{3\times3}$ | $\nu^c$–$\ell$ mixing in the $W_R$ current; zero, so the light-neutrino right-handed current is switched off numerically |

The $Z_R$ charges follow the standard $SU(2)_R\times U(1)_{B-L}$ pattern:
$$
g_L^{f} = -\,Y_{f_L}\,\frac{t_W^2}{\kappa_R^2},
\qquad
g_R^{f} = T^{3}_{R,f} - Q_f\,\frac{t_W^2}{\kappa_R^2},
$$
with $Y_{q_L}=1/6$, $Y_{\ell_L}=-1/2$, $T^3_R=\pm 1/2$. This is a useful cross-check: all eleven numeric coefficients above reproduce exactly.

### 3.3 Interaction order

`M$InteractionOrderHierarchy` declares `{QCD,1}`, `{QED,2}`, `{NP,1}`. Only $\kappa_R^{q}$ and $\kappa_R^{\ell}$ carry `NP` order, so every $W_R$ / $Z_R$ / $N$ vertex counts as one power of `NP`.

---

## 4. Physics summary

This is an **effective left-right model**: the SM is extended by a heavy charged vector $W_R^\pm$ (3 TeV), a heavy neutral vector $Z_R$ (5.07 TeV), and three Majorana heavy neutral leptons $N_{1,2,3}$ (173.3 GeV, $10^{12}$, $10^{12}$ GeV). The new vectors are not gauged — they appear as Proca fields with abelian field strengths and no self-interactions — and they couple to purely **right-handed** charged currents and to left/right neutral currents whose charges follow the $SU(2)_R\times U(1)_{B-L}$ pattern, with two independent coupling-ratio inputs $\kappa_R^{q}$ and $\kappa_R^{\ell}$ that decouple the quark and lepton sectors.

It mediates the classic right-handed signatures: $s$-channel Drell-Yan $W_R$ production from $\bar q q'$ followed by $W_R\to \ell^\pm N$, with the Majorana $N$ decaying back through an off-shell $W_R$ to $\ell^\pm j j$ — the Keung-Senjanovic same-sign-dilepton plus dijet final state, which violates lepton number by two units. It also gives a $Z_R$ resonance in dilepton, dijet and $N\bar N$ channels, and $W_R$ dijet resonances through $\bar u d$. Because $V^{R}_{\rm CKM}$ and $Y_N$ are the identity and $X_N$ vanishes, the default point has no right-handed flavour violation and no light-neutrino $W_R$ current; only $N_1$ is light enough and has a non-zero width to appear as an on-shell intermediate state.

**One caveat for the reader:** as written, `LWRq` carries an overall factor 2 that `LWRl` does not, so the quark $W_R$ coupling is $\sqrt2\,\kappa_R^q g_w$ rather than the conventional $\kappa_R^q g_w/\sqrt2$. All $W_R$ production rates from quarks are therefore a factor 4 larger than the standard normalisation would give, while the declared $W_R$ width (84.3 GeV) is not correspondingly rescaled.
