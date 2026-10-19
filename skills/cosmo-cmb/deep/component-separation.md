# Component separation — cosmo-cmb dossier

Scope: how a foreground-cleaned CMB temperature or E-mode map (and a
Compton-y map from the same machinery) is produced at map level — Bayesian
parametric fit, template cleaning, spectral matching, needlet ILC,
constrained ILC — what each method assumes, how its output is validated
(confidence mask, effective transfer function, ILC bias, residual
stacking), and when to work at map level or at spectrum level; B-mode
foreground separation for r and the multi-frequency spectrum likelihoods
are treated elsewhere.
Snapshot: 2026-10-18.
From: Planck 2018 IV (arXiv:1807.06208); SO science goals, Sect. II.5;
Komatsu 2022 review (arXiv:2202.13919), section on polarised Galactic
foreground emission.

Already in L2 or a sibling, not repeated here: the four Planck method
papers, the mean polarised indices β_d and β_s, and the BICEP/Keck
foreground model (`physics-and-methods.md#foregrounds-and-component-separation`);
spectrum-level foreground models and lite compression
(`deep/high-ell-likelihoods.md`); Commander cleaning for low-ℓ
polarisation (`deep/low-ell-polarisation-tau.md`); foreground-hardened
and gradient-cleaned lensing estimators (`deep/lensing-reconstruction.md`);
B-mode separation pipelines and their residuals in the r likelihood
(`cosmo-inflation-primordial/deep/bmode-foreground-separation.md`);
y-map science and CIB maps (`cosmo-cmb-lss-cross-correlations/deep/`).

## How it is done
<!-- key: how-it-is-done -->

Notation. d_ν is the map (or harmonic or needlet coefficients) at
frequency ν; r_ν⁰ (or **a**) the frequency response ("SED") of the
component of interest, equal to 1 for the CMB and kSZ in thermodynamic
units; **C** the frequency–frequency covariance of the data; **w** the
weights of a linear combination. "Deprojection" means imposing zero
response to a contaminant SED. "HMHS" and "HMHD" are half-mission
half-sum and half-difference maps (Planck).

### Step 1. Pick the family of method
<!-- key: step-1-pick-the-family-of-method -->

| Method | Data model | What is fitted | Output | Place |
|---|---|---|---|---|
| Commander (Bayesian parametric) | d_ν(p) = g_ν Σ_c F_ν(β_c) T(p) a_c + n_ν(p) (Eq. 1) | amplitudes a_c of each component, spectral parameters β_c, calibration g_ν, by Gibbs sampling | CMB and foreground maps, full posterior | [src: arXiv:1807.06208, Sect. 2.1] |
| SEVEM (internal templates) | CMB-dominated channels minus a linear combination of CMB-free difference templates | template coefficients by minimising the cleaned-map variance outside a mask | cleaned maps per frequency (70–217 GHz) and a coadd | [src: Sect. 2.3, App. C.1] |
| SMICA (spectral matching) | ŝ_ℓm = **w**_ℓ† **x**_ℓm, **w**_ℓ = **C**_ℓ⁻¹**a**/(**a**†**C**_ℓ⁻¹**a**) (Eq. 2) | at low ℓ, a parametric C_ℓ(θ) with an unconstrained N_fg-dimensional foreground block (Eqs. 4–5); at high ℓ the empirical C_ℓ | CMB T, E, B maps | [src: Sect. 2.4] |
| NILC (needlet ILC) | minimum-variance linear combination in each needlet band, weights local in pixel space | **w** = **C**⁻¹**r**⁰/(**r**⁰†**C**⁻¹**r**⁰), C estimated locally | CMB T, E, B (separately; E and B from full-sky decomposition) | [src: Sect. 2.2; arXiv:2307.01258, Eq. 7] |
| Constrained ILC | d = r⁰s + Σ_i r^i c^i + ñ (Eq. 8), extra constraints Σ w r^α = 0 | weights of Eq. 9 | CMB with chosen contaminants nulled, or y with CMB/CIB nulled | [src: arXiv:2307.01258, Sect. III.3.1; Remazeilles et al. 2010, arXiv:1006.5599] |

What each assumes and why it is used:

- ILC assumes only that the response of the target is known and that it
  is uncorrelated with everything else ("noise"); for the tSZ the second
  assumption is only approximate [src: arXiv:2307.01258, Sect. III.3.1,
  footnote 6].
- SMICA's foreground model is "agnostic": emissivities and foreground
  spectra are free, **P**_ℓ only positive; it does not try to reconstruct
  temperature foregrounds, because synchrotron, free-free, spinning dust,
  thermal dust and CO are too tightly coupled in intensity [src:
  arXiv:1807.06208, Sect. 2.4].
- Commander needs an explicit sky model. In 2018 the temperature model
  was reduced to CMB, one low-frequency power law, thermal dust and one
  CO component, because the 2018 release has full-frequency maps only and
  no single-detector maps to constrain the 2015 seven-component model;
  polarisation keeps CMB, synchrotron (power law) and thermal dust
  (modified blackbody) [src: Sect. 2.1; App. A.2, Eqs. 19–24].
- Commander spectral parameters carry three priors: hard uniform limits
  (for look-up tables), a Jeffreys prior (against volume effects), and
  informative Gaussian priors (the important one); amplitudes get a
  smoothing prior D_ℓ = A e^{−ℓ(ℓ+1)σ²} (Eq. 25) [src: App. A.2].
- NILC needlets let weights vary slowly on large scales and quickly on
  small ones, which zones cut on the sky cannot do; on large scales the
  weights reject foregrounds, on small scales they tend to inverse-noise
  weighting [src: arXiv:1807.06208, Sects. 2.2, 4.6].

### Step 2. Prepare the inputs
<!-- key: step-2-prepare-the-inputs -->

- Common resolution and units. Planck pipelines output a 5′ FWHM target
  beam at N_side 2048 [src: arXiv:1807.06208, Sect. 4.3]. ACT + Planck
  NILC works in "linearized differential thermodynamic units"; the
  response of a non-CMB component is its SED integrated over the passband
  with the dB/dT conversion and a ν⁻² factor (Eq. 15) [src:
  arXiv:2307.01258, Sect. III.3.3].
- SEVEM templates: 30−44, 44−70 and 545−353 GHz differences, each
  channel convolved with the other's beam, plus 857 GHz convolved with
  the 545 GHz beam, cleaning 100, 143 and 217 GHz; point sources found
  with a Mexican-hat wavelet are inpainted in both maps of a pair before
  differencing [src: arXiv:1807.06208, App. C.1].
- SEVEM 2018 adds 217 GHz to the polarisation coadd for signal-to-noise
  but down-weights it on the largest scales, where it is more prone to
  systematics and calibration error [src: Sect. 2.3].

### Step 3. Choose the needlet bands and the covariance kernel (NILC)
<!-- key: step-3-choose-the-needlet-bands-and-the -->

- ACT DR4/DR6 + Planck NILC uses 26 needlet peaks from ℓ_peak = 0 to
  17,000 with cosine-shaped bands (Eq. 2): narrow bands at low ℓ, where
  Galactic emission varies fast with scale and position, broad bands at
  high ℓ, where tSZ, CIB, sources and noise vary slowly [src:
  arXiv:2307.01258, Sect. III.2].
- The covariance is estimated at each needlet pixel with a smoothed
  top-hat kernel T(θ) = 1/(1 + θ/W_i)⁶ (Eq. 12), with width
  W_i = 2 arccos(1 − 2 × 20 N_elements/N_modes) (Eq. 13), so that
  enough modes enter for the matrix to be invertible; the authors found
  this kernel stable near map edges [src: Sect. III.3.2].
- Each needlet scale uses the coarsest pixelisation that supports it,
  to save time and memory [src: Sect. III.2].

### Step 4. Remove the ILC bias
<!-- key: step-4-remove-the-ilc-bias -->

Using the data both for weights and as the data vector produces chance
signal–noise anticorrelations that the ILC up-weights, suppressing the
signal. In a harmonic ILC this matters only at the largest scales; in a
needlet ILC with small covariance kernels it affects all scales [src:
arXiv:2307.01258, Sect. III.3.2, Fig. 3]. Options listed by the authors:
larger kernels (less spatial adaptivity), analytic or simulated
correction, or a different objective [src]. ACT's choice: exclude the
modes being weighted from the covariance that sets their weights. The
needlet-band modes are split into N_subset = 5 subsets (by ℓ below 20,
then by blocks of m), weights for each subset come from the other four,
and the results are summed; adjacent m are kept together because
masking couples them [src: App. C].

### Step 5. Decide what to deproject
<!-- key: step-5-decide-what-to-deproject -->

- tSZ deprojection in a CMB map removes the large tSZ residual seen when
  stacking on ACT DR5 clusters; a small central residual remains, which
  the authors attribute to CIB correlated with clusters and enhanced by
  the deprojection [src: arXiv:2307.01258, Sect. V.1, Fig. 12].
- For y maps, deprojecting a CIB modified blackbody (β = 1.7,
  T_CIB = 10.70 K, Eq. 18) and its first derivative in β ("CIB-δβ")
  adds robustness at the cost of more noise [src: Sect. III.3.3,
  Fig. 15].
- Each constraint costs noise. For ground data this cost is large on
  small scales; a partially constrained ILC trades a tolerated residual
  for variance: accepting a tSZ residual of 20% of the standard-ILC
  residual cuts the CMB-map variance by at least 50% relative to full
  deprojection over ℓ = 3000–4800 for an SO-like setup (**forecast**)
  [src: Abylkairov et al. 2020, arXiv:2012.04032].

### Step 6. Validate the cleaned map
<!-- key: step-6-validate-the-cleaned-map -->

| Check | How | Pass criterion or result | Place |
|---|---|---|---|
| Confidence mask (T) | inter-pipeline standard-deviation map at 80′ thresholded at 3 μK; smoothed 10° and cut at 0.5 to remove islands; 10′ map thresholded at 10 μK for compact objects; union with Commander and SEVEM χ² masks and SEVEM/SMICA inpainting masks | f_T = 0.780 | [src: arXiv:1807.06208, Sect. 4.2] |
| Confidence mask (P) | 80′ standard deviation at 1 μK and at 0.6 μK; Commander, SEVEM masks; cosmic-ray-affected region; CO brighter than 20 μK at 100 GHz (5′ smoothing) as a guard against T→P leakage | f_P = 0.782 | [src: Sect. 4.2] |
| Effective transfer function | f_ℓ = (b_ℓ^{5′} p_ℓ^{2048})⁻¹ √⟨C_ℓ^out/C_ℓ^in⟩ over 50 signal-only simulations, Savitzky–Golay smoothed over Δℓ = 51 (Eq. 9) | TT within ±0.5% for all pipelines; E shows wiggles from T→P beam leakage | [src: Sect. 4.3] |
| Spectra versus the ΛCDM best fit | HMHS minus model minus HMHD | agreement to ℓ ≲ 1500; NILC 10 μK² (0.2%) deficit at ℓ = 100–300 | [src: Sect. 4.6] |
| End-to-end FFP10 polarisation | ΔP = √[(Q_out − Q_in)² + (U_out − U_in)²] at 80′ | rms over the common mask 0.74, 0.86, 0.74, 0.75 μK (Commander, NILC, SEVEM, SMICA) | [src: Sect. 4.10, Eq. 13] |
| Lensing from each map | T-only and MV reconstruction, 8 ≤ L ≤ 2048 | "almost identical constraining power", summary amplitudes consistent; all four slightly tilted versus the fiducial | [src: Sect. 4.8] |
| Residual tSZ (ground NILC) | stack the CMB map on cluster positions | standard ILC shows a large residual; deprojected ILC almost none | [src: arXiv:2307.01258, Sect. V.1] |

The Planck authors stress that agreement among codes is "only a necessary
criterion; it is not sufficient", hence the absolute χ²-based masks
added on top [src: arXiv:1807.06208, Sect. 4.2]. They also state that
the end-to-end simulations match the data to ≲ 3% for ℓ ≲ 1500 and show
non-negligible biases above, so detailed statistics at ℓ ≳ 1500 need
caution [src: Sect. 6].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Which Planck pipeline for which purpose
<!-- key: which-planck-pipeline-for-which-purpose -->

| Property | Commander | NILC | SEVEM | SMICA | Place |
|---|---|---|---|---|---|
| Low-ℓ TT noise | lowest, close to white, ∝ ℓ² | highest at ℓ ≲ 300, almost ten times Commander | — | drops near ℓ ≈ 100, where LFI is excluded at high latitude | [src: arXiv:1807.06208, Sect. 4.6] |
| Unresolved-source imprint at high ℓ | largest | smallest | — | — | [src: Sect. 4.6] |
| Polarisation residual pattern (simulations) | less sensitive to high-latitude stripes | lower in the Galactic plane | as Commander | as NILC | [src: Sect. 4.10] |
| Distinctive product | foreground posteriors; per-pixel inverse-variance weighting | — | cleaned single-frequency maps for cross-frequency tests | hybrid map, SZ-free variant | [src: Sects. 2.3–2.4, 4.3] |

- SMICA's temperature map is a hybrid: X = X_full + 𝒫(X_high − X_full)
  (Eq. 6), with X_high from the six HFI channels (N_fg = 4) for clean sky
  and small scales and X_full from all nine channels (N_fg = 8)
  elsewhere [src: Sect. 2.4].
- SEVEM's cleaned single-frequency maps are what one uses to test for
  frequency-dependent effects or to build cross-frequency estimators
  against correlated noise, provided the template contribution is
  accounted for [src: Sect. 2.3].
- For 2018 temperature foregrounds, the Planck team recommends the 2015
  products and did not release 2018 temperature foreground maps; the CMB
  temperature maps are unaffected [src: Sect. 6].
- For large-scale polarisation the 2018 maps are "not consistent with
  uncorrelated white noise at any angular scales", so any analysis needs
  the end-to-end simulations and half-split checks [src: Sect. 6].

### Harmonic ILC or needlet ILC (ground + Planck)
<!-- key: harmonic-ilc-or-needlet-ilc-ground-planck -->

- On ACT + Planck, the harmonic-ILC CMB map is about 10% noisier on the
  smallest scales than NILC; the needlet frame removes strongly varying
  Galactic emission better (y-map comparison) [src: arXiv:2307.01258,
  Sect. V.1, Fig. 13].
- NILC buys spatial adaptivity at the price of an ILC bias on all scales,
  which must be mitigated (Step 4) [src: Sect. III.3.2].
- At ℓ ≈ 2000 the ACT + Planck NILC temperature noise is an order of
  magnitude below Planck SMICA [src: Sect. V.1].

### Map-level deprojection or spectrum-level ILC
<!-- key: map-level-deprojection-or-spectrum-level-ilc -->

- A component-separated map with deprojections is "not necessarily" the
  minimum-variance input for two- or higher-point statistics [src:
  Kwok et al. 2025, arXiv:2509.10604, abstract].
- Spectral ILC combines auto- and cross-spectra with weights W_ℓ^{ij}.
  With the "strong" constraints (unit response to ss, zero to yy and to
  the sy cross term, Eq. 23) it reproduces the constrained ILC; if the CMB
  is known to be uncorrelated with the contaminant, the "weak"
  constraints (Eq. 24) drop the cross term and give equal or lower
  variance [src: Sect. III]. The weak version implicitly assumes certain
  connected four-point functions vanish (Eqs. 28–29) and is sub-optimal
  otherwise [src].
- In SO-like simulations SpILC gives CMB spectrum error bars more than 7
  times smaller than a tSZ- and CIB-deprojected constrained ILC at
  ℓ ≳ 4000 (**forecast**) [src: abstract].
- Data splits: a SpILC estimator without instrumental noise bias drops
  same-split, same-channel spectra (Eqs. 33–35); correlated atmospheric
  noise across channels needs a stricter version [src: Sect. IV].
- For TT/TE/EE cosmology the collaborations instead fit foregrounds in
  the multi-frequency likelihood (`deep/high-ell-likelihoods.md`); map-level
  cleaning is the input for lensing, low-ℓ polarisation, y and
  cross-correlations (`physics-and-methods.md#foregrounds-and-component-separation`).

### Adding galaxy maps as ILC channels
<!-- key: adding-galaxy-maps-as-ilc-channels -->

Using galaxy number-density maps as extra channels reduces residual
foreground power in the cleaned temperature map at ℓ ≈ 10,000 by about
4%, 22% and 32% for unWISE, Rubin-like and a futuristic sample, but the
ΛCDM error bars improve by under 1% to about 2%, and N_eff by at most
2.2% (**forecast**) [src: Chen & Hill 2026, arXiv:2608.28487, abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Planck confidence-mask sky fractions | f_T = 0.780, f_P = 0.782 (2015: 0.77, 0.78) | Planck 2018 | arXiv:1807.06208 | Sect. 4.2 |
| Mask thresholds | T: 3 μK at 80′, 10 μK at 10′; P: 1 μK and 0.6 μK at 80′; CO > 20 μK at 100 GHz | Planck 2018 | arXiv:1807.06208 | Sect. 4.2 |
| Effective transfer function, TT | within ±0.5%; Commander falls about 0.3% by ℓ ≈ 2000 (≈ 0.05′ FWHM mismatch) | Planck 2018 | arXiv:1807.06208 | Sect. 4.3 |
| End-to-end polarisation residual rms | 0.74 / 0.86 / 0.74 / 0.75 μK | Commander / NILC / SEVEM / SMICA | arXiv:1807.06208 | Sect. 4.10 |
| Simulation fidelity | ≲ 3% for ℓ ≲ 1500 | Planck 2018 | arXiv:1807.06208 | Sect. 6 |
| Dust BB/EE ratio; synchrotron | 0.5; 0.34 | Planck 2018 | arXiv:1807.06208 | Sect. 6 |
| SMICA foreground dimension | N_fg = 4 (6 HFI channels); 8 (9 channels) | Planck 2018 | arXiv:1807.06208 | Sect. 2.4 |
| SEVEM sources inpainted, T, |b| > 20° | 809 / 1093 / 1289 at 100 / 143 / 217 GHz | Planck 2018 | arXiv:1807.06208 | App. C.1, Table 9 |
| NILC needlet peaks | 26, ℓ_peak 0 to 17,000 | ACT + Planck | arXiv:2307.01258 | Sect. III.2 |
| ILC-bias subsets | N_subset = 5 | ACT + Planck | arXiv:2307.01258 | App. C |
| Area of ACT + Planck NILC maps | about 13,000 deg²; y-map beam 1.6′ FWHM | ACT DR4 + DR6 + Planck | arXiv:2307.01258 | abstract; Fig. 14 caption |
| CIB SED used for deprojection | β = 1.7, T_CIB = 10.70 K | ACT + Planck | arXiv:2307.01258 | Sect. III.3.3 |
| tSZ relativistic temperature used | ≈ 8 keV (large scales) to ≈ 2 keV (small) | ACT + Planck | arXiv:2307.01258 | Sect. III.3.3 |
| pcILC trade-off (**forecast**) | 20% tSZ residual → ≥ 50% variance reduction, ℓ = 3000–4800 | SO-like | arXiv:2012.04032 | abstract |
| SpILC versus cILC (**forecast**) | > 7 times smaller errors at ℓ ≳ 4000 | SO-like | arXiv:2509.10604 | abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

| Failure | How it shows | Test | Place |
|---|---|---|---|
| ILC bias (signal suppressed by chance correlations) | cross-correlation of the output with the input CMB below unity on all scales in NILC | simulation input–output cross-spectrum; weights from held-out modes | [src: arXiv:2307.01258, Sect. III.3.2] |
| tSZ residual in a CMB map | dip at cluster positions in stacks; biases cluster-correlated analyses | stack on a cluster catalogue; tSZ deprojection | [src: arXiv:2307.01258, Sect. V.1] |
| CIB enhanced by tSZ deprojection | small central residual in deprojected stacks | add CIB (and CIB-δβ) deprojection, check noise | [src: Sect. V.1, Fig. 15] |
| Wrong tSZ SED for hot clusters | y underestimated at large scales | relativistic, scale-dependent T_e(ℓ) response | [src: Sect. III.3.3] |
| Inter-pipeline agreement mistaken for cleanliness | common residual passes the agreement test | absolute χ² and difference masks | [src: arXiv:1807.06208, Sect. 4.2] |
| Nominal beam used instead of the effective one | sub-percent TT, wiggly E errors | per-pipeline f_ℓ from simulations, re-evaluated for the mask used | [src: Sect. 4.3] |
| Inpainted pixels inside the analysis mask | small change of f_ℓ for aggressive masks | recompute f_ℓ with inpainting for that sky cut | [src: Sect. 4.3, footnote 10] |
| Correlated noise in large-scale polarisation | excess BB at low ℓ in the HMHS spectra | compare with end-to-end simulations; half-splits | [src: Sects. 4.6, 6] |
| Too few modes in the local covariance | non-invertible C, unstable weights near edges | kernel width set by mode counting (Eq. 13) | [src: arXiv:2307.01258, Sect. III.3.2] |

## Reading list
<!-- key: reading-list -->

- Foundation: Remazeilles, Delabrouille & Cardoso 2010, arXiv:1006.5599 —
  the constrained ILC for separating CMB and tSZ.
- Foundation: Delabrouille et al. 2008, arXiv:0807.0773 — NILC on WMAP
  (method paper, already in the bibliography).
- Method and application: Planck Collaboration 2018 IV, arXiv:1807.06208
  — Commander2, NILC, SEVEM, SMICA as run; confidence masks, transfer
  functions, end-to-end tests; read Sects. 2, 4 and 6.
- Application: Coulton et al. 2023, arXiv:2307.01258 — ACT + Planck
  needlet ILC, local covariance, ILC-bias removal by held-out modes,
  deprojections, relativistic tSZ.
- Method: Abylkairov et al. 2020, arXiv:2012.04032 — partially
  constrained ILC: how much noise a deprojection costs and how to trade
  it.
- Critique: Kwok et al. 2025, arXiv:2509.10604 — why a deprojected map
  is not the minimum-variance input for a spectrum; spectral ILC.
- Forecast: Chen & Hill 2026, arXiv:2608.28487 — galaxy maps as ILC
  channels, and the small parameter gain.

## Not verified
<!-- key: not-verified -->

- The ACT DR6-only component-separated maps (if released after
  arXiv:2307.01258) and any SPT-3G or SO component-separation paper were
  not read; the search of 2026-10-18 found method papers only.
- Planck PR4 (NPIPE) component-separated CMB maps were not read; this
  dossier describes the 2018 (PR3) pipelines.
- The SMICA polarisation and SZ-free details (App. D of
  arXiv:1807.06208) and the Commander compact-object sampling (App. A.3)
  were not read beyond what is cited.
- The SO science-goals section and the Komatsu review section named in
  "From" were not re-read for this dossier.
