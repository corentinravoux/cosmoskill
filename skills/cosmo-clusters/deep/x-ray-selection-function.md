# X-ray selection function — cosmo-clusters dossier

Scope: how the selection of an X-ray cluster sample is built (simulated
twin skies, source matching, the classifier and its input variables),
how it enters the count likelihood together with contaminants and the
optical confirmation, and how it is validated against other surveys;
eROSITA eRASS1 and XMM-XXL compared.
Snapshot: 2026-10-17.
From: Miyatake 2025 review (arXiv:2505.07697), Sect. 3.2; Pierre 2022
review (arXiv:2205.05499), Sects. 1.1 and 2; eRASS1 cosmology paper set
(arXiv:2402.08452, arXiv:2402.08457).

Already in L2, not repeated here: the X-ray selection mechanism and the
cross-match numbers with SPT-3G and AMICO in `systematics.md#x-ray-selection`;
the eRASS1 count-rate–mass relation, contaminant priors, redshift error
model and cosmology priors in
`systematics.md#erass1-cosmology-ghirardini-et-al-2024-arxiv`; the
eRASS1 likelihood split and blinding by selection functions in
`physics-and-methods.md#count-likelihoods-and-covariance` and
`physics-and-methods.md#blinding-practice`; the eRASS1 sample sizes in
`physics-and-methods.md#what-the-main-analyses-did`.

## How it is done
<!-- key: how-it-is-done -->

The general form is the same for every survey: the model count in a bin
is an integral of the mass function times p(Θ_bin, Θ_sel | Θ_model) times
the selection probability p(I | Θ_sel), where I is the Boolean "in the
catalogue" and Θ_sel the variables on which selection is modelled
(arXiv:2402.08457, Eq. 2) [src: Sect. 2]. The design choice is Θ_sel:
"selecting Θ_bin and Θ_sel so the model is accurate and the modelling
effort is well balanced" between the selection model and the population
model [src: same]. The authors add that part of the selection "may result
from human intervention" and so resists analytic formulae, which motivates
empirical models [src: same].

### Step 1. Define the detection and the sample cuts
<!-- key: step-1-define-the-detection-and-the-sample-cuts -->

- **eRASS1.** eSASS detects sources above background in 0.2–2.3 keV and
  fits each with a PSF model, giving a detection likelihood L_det and an
  extent likelihood L_ext; the primary catalogue uses L_ext > 3 to
  maximise completeness, the cosmology sample L_ext > 6 to maximise purity,
  photometric redshifts 0.1–0.8 and the Legacy Survey DR10-South area,
  5259 identified clusters with contamination below 5% [src:
  arXiv:2402.08457, Sect. 3.1]. The cosmology paper quotes the expected
  contamination as 20% after L_ext > 6 in simulations and ≈ 6% after optical
  confirmation, against a Poisson noise of 1.4% [src: arXiv:2402.08458,
  Sect. 4.2]. The two papers' contamination figures (< 5% and ≈ 6%) are
  stated as given.
- **XXL.** The C1 class is defined in the output space of the Xamin
  pipeline (ext, ext_stat); of 365 published clusters, the 191 C1 sources
  have fewer than 5% point sources misclassified as extended; the
  cosmology sample keeps 178 spectroscopically confirmed C1 clusters at
  0.05–1 [src: Garrel et al. 2021, arXiv:2109.13171, Sects. 2.1, 3.2.2].
  XXL covers two 25 deg² fields to ≈ 5e-15 erg s⁻¹ cm⁻² for point sources
  in 0.5–2 keV with 6.9 Ms of XMM time [src: arXiv:2205.05499, Sect. 1.1].

### Step 2. Simulate the survey end to end
<!-- key: step-2-simulate-the-survey-end-to-end -->

- **eRASS1 digital twin.** UNIT1i dark-matter light-cone; AGN and cluster
  emission painted with models built from real clusters, keeping the
  covariance of surface-brightness profile, mass, temperature and
  redshift; a flux rescaling for groups below M500c = 5e13 M_sun; stars and
  Galactic foregrounds; events generated with SIXTE with the real scanning
  law, then processed with the same eSASS version in 3.6° × 3.6° tiles;
  several tens of Poisson realisations of one parent population; more than
  1e6 haloes to z ~ 1.5 per half sky [src: arXiv:2402.08457, Sect. 3.2].
- **XXL.** Circular β = 2/3 clusters over a grid of count rate and core
  radius, for a range of XMM exposures, with PSF distortion, vignetting,
  detector masks, background and Poisson noise, and point sources from a
  log N–log S to 5e-16 erg s⁻¹ cm⁻² [src: arXiv:2109.13171, Sect. 3.2.2,
  following Pacaud et al. 2006].

### Step 3. Decide which simulated cluster was detected
<!-- key: step-3-decide-which-simulated-cluster-was -->

eRASS1 compares two matching algorithms: photon-based (which input source
deposited the photons of a detection) and Bayesian positional matching.
They agree over a wide flux range and differ below a few 1e-14 erg s⁻¹
cm⁻², up to a factor 2 in some flux bins; one cause is a bright AGN next to
a faint cluster, which photon matching assigns to the AGN [src:
arXiv:2402.08457, Sect. 3.3.3]. The order of operations also matters: the
positional method starts from sources above the L_ext threshold, the
photon method matches first and applies the threshold after, which changes
the outcome in crowded regions [src: same]. The difference between the two
is used to bracket the matching uncertainty [src: same]. In each twin,
fewer than 4% of haloes are detected and fewer than 1% selected; two thirds
are used for training, one third for testing, and training sets from 11
realisations are concatenated into a set ≈ 7 times the real sky [src:
Sect. 3.4].

### Step 4. Train the selection model
<!-- key: step-4-train-the-selection-model -->

- **Choice of Θ_sel in eRASS1.** The cosmology pipeline uses five
  features: true redshift z, the n_H-corrected, survey-averaged count rate
  C_R in 0.2–2.3 keV within R500 free of shot noise, and three sky-position
  quantities H (n_H, exposure time, background) [src: arXiv:2402.08457,
  Sect. 5.3]. The count rate follows CR = L_X / [4π d_L(z)² ECF(z, k_B T,
  N_H = 0)] (Eq. 7), with ECF the conversion from rest-frame 0.5–2 keV to
  observed 0.2–2.3 keV for an APEC spectrum [src: same]. The reasons given
  for choosing count rate over L_ext, L_det, luminosity, gas mass or Y_X:
  it correlates with mass, can be made nearly sky-independent (exposure and
  absorption corrections), and depends minimally on cosmology, which keeps
  the forward model cheap [src: arXiv:2402.08458, Sect. 2.2]. The cost:
  morphology is marginalised over the distribution in the twin [src:
  arXiv:2402.08457, Sect. 5.3].
- **Classifier.** A Gaussian-process classifier with a probit link and a
  Bernoulli likelihood for the detection flags, squared-exponential kernel,
  stochastic variational GP (SVGP) with 30 inducing points, ≈ 4.8e5
  training clusters, 651 hyperparameters, mini-batches of 2^16 and 12000
  iterations; training restricted to 0.05 < z < 0.85, wider than the
  sample, to allow leakage through redshift errors [src: arXiv:2402.08458,
  Sect. 3.3]. The GP gives confidence levels whose width follows the
  sparsity of the training set [src: Sect. 3.4].
- **XXL form.** A detection probability f[CR, θ_c] in the plane of count
  rate and apparent core radius of a β = 2/3 model, mapped back to the
  intrinsic (CR, θ_c) of the injected clusters, not to the pipeline values
  [src: arXiv:2109.13171, Sects. 3.1, 3.2.2]. The authors stress that
  this is why measured CR from an independent profile fit can be used
  consistently [src: Sect. 3.2.2].
- **What drives detection (eRASS1, interpretive model).** A logistic
  regression on surface brightness in 7 annuli (0–180″) for 5 components
  (cluster, AGN, stars, background, other clusters), η_j = ln(1 + Σ_j/c),
  36 coefficients (Eq. 5): the 20–40″ cluster annulus matters most for
  selection, twice the 0–20″ one, because the source must be classified as
  extended beyond the ≈ 30″ PSF; for detection alone the central 20″
  dominate; AGN photons within 1′ slightly raise the selection
  probability, beyond 1′ lower it, because masking removes cluster photons
  [src: arXiv:2402.08457, Sect. 4.2]. Counts beyond ≈ 1.5′ play a minor
  role [src: Sect. 8].

### Step 5. Put the selection into the likelihood
<!-- key: step-5-put-the-selection-into-the-likelihood -->

eRASS1 marginalises over true count rate, mass and redshift:
dN_C/(dĈ_R dẑ dĤ) P(I | Ĉ_R, ẑ, Ĥ) = P(Ĥ) ∭ P(ẑ | z) P(I | z, C_R, Ĥ)
P(Ĉ_R | C_R) (dN/dM dV)(dV/dz) P(C_R | M, z) dM dC_R dz (Eq. 8), with
P(C_R | M, z) lognormal of width σ_X (Eq. 9), P(ẑ | z) a two-Gaussian
mixture with bias b_z, catastrophic fraction c_z and shift c_shift,z
(Eq. 11), and the total number N_C including the richness cut Θ(λ̂ > 3)
(Eq. 10) [src: arXiv:2402.08458, Sect. 4.3]. The selection is applied on
true quantities, the measurement errors outside it.

The optical step is a second, separate selection: richness and redshift
cuts applied after the X-ray detection, modelled as Heaviside functions in
the integration limits [src: arXiv:2402.08458, Sect. 3.5]. Its stated role
is to model contamination, not completeness, because eROMaPPer identifies
more than 97% of SZ-selected clusters [src: same].

Contaminants enter as a mixture P(Ô) = Σ_{i ∈ {C, AGN, RS}} f_i P(Ô | i)
for every observable (count rate, redshift, richness, shear) (Eq. 7), with
AGN and random sources (RS) given count-rate distributions from the
simulations and richness–redshift distributions from optical runs on point
sources and on random positions; two extra parameters, the fractions [src:
arXiv:2402.08458, Sect. 4.2]. The reason for modelling richness: a high
photometric redshift wrongly attached to a faint X-ray source would be read
as a massive high-z cluster [src: same]. The paper contrasts this with SPT,
where the contamination likelihood is computed only for systems not
optically confirmed [src: same, footnote 8].

XXL instead fits the distribution of clusters in the observable space
(CR, hardness ratio HR, z), the ASpiX method, with the selection applied
in the CR–θ_c plane and θ_c then integrated out (arXiv:2109.13171, Sect.
3.1, Table 1) [src].

### Step 6. Validate
<!-- key: step-6-validate -->

- **Internal.** Precision–recall and calibration curves on held-out twins.
  For the cosmology sample the baseline (CR, z, H) model has average
  precision 70%, about that of a luminosity–redshift model; adding a
  morphological feature (central emission measure EM_0) raises it to 74%.
  For the primary sample: 34% (M500, z), 56% (L_X, z), 67% with H, 71%
  with EM_0 [src: arXiv:2402.08457, Sect. 5.4]. Calibration curves lie
  on the one-to-one line [src: same]. A test sample of 2566057 simulated
  clusters gives the reliability plot of the adopted model [src:
  arXiv:2402.08458, Sect. 3.4, Fig. 3].
- **External.** For each object in a reference catalogue R, the model
  predicts P_i = p(I_T | I_R, Θ_meas) that it is also in the test catalogue
  T (arXiv:2402.08457, Eq. 8), with both selection functions and the
  correlated scatter of their selection variables [src: Sect. 6.1].
  Diagnostics: the expected number of matches from Bernoulli draws, the
  match fraction in bins of P_i, and two leakage fractions δ_1, δ_2 [src:
  same]. Results are in the table below.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Selection variables: mass, luminosity, count rate, or surface brightness
<!-- key: selection-variables-mass-luminosity-count-rate -->

| Θ_sel | Dependence on the twin's assumptions | Cost in the likelihood | Performance | Place read |
|---|---|---|---|---|
| (M500, z) | strong: inherits the twin's scaling relations | cheapest | 34% average precision (primary sample) | arXiv:2402.08457, Sects. 5.4, 8 |
| (L_X, z) | luminosity tied to photons | cheap | 56% | same |
| (CR, z, H) | quasi-independent of the twin's cosmology; sky depth explicit | needs a count-rate–mass relation in the model | 70% (cosmology sample) | Sects. 5.3–5.4 |
| (CR, z, H, EM_0) | adds morphology | needs a morphology model | 74% | Sect. 5.4 |
| surface brightness in 7 × 5 annuli | closest to the pipeline | requires profiles in the forward model | close to 71–74% | Sects. 4.2, 5.4 |

The conclusion drawn: models with at least one morphological feature
perform better, but the less twin-dependent models demand "a heavier
modelling effort in scientific analyses" [src: arXiv:2402.08457, Sect. 8].
eRASS1 took (CR, z, H).

### Count rate and hardness ratio instead of mass
<!-- key: count-rate-and-hardness-ratio-instead-of-mass -->

ASpiX avoids recomputing R500 and scaling relations at each cosmology step,
and lets clusters with 80–100 photons enter, because a hardness ratio needs
far fewer photons than a temperature [src: arXiv:2205.05499, Sect. 2].
On the same 178 C1 clusters and priors, the (CR, HR, z) analysis improves
the σ8–Ω_m constraint by a factor ≈ 2 over dn/dz [src: Sect. 2.1].

### Classifier form
<!-- key: classifier-form -->

eRASS1 chose GP classification for short response time, few prior
assumptions and meaningful uncertainties [src: arXiv:2402.08458, Sect.
3.3]; a logistic model was kept for interpretation [src:
arXiv:2402.08457, Sect. 4.2]. XXL uses a tabulated detection probability
in two observables [src: arXiv:2109.13171, Sect. 3.2.2].

### Contaminants: mixture model or confirmation only
<!-- key: contaminants-mixture-model-or-confirmation-only -->

eRASS1 fits contaminant fractions on the fly (two parameters) [src:
arXiv:2402.08458, Sect. 4.2]; small earlier samples did not need it because
contamination was below Poisson noise [src: same]. About 12% of the eRASS1
cosmology catalogue lies below 1e14 M_sun, with a 30% spurious fraction
there; no further cut was applied so as not to alter the selection, and
the mixture model is relied on [src: Sect. 8.5].

### Validation and blinding through selection models
<!-- key: validation-and-blinding-through-selection-models -->

Six selection models with thresholds (L_ext, EXTENT) = (3.6, 16.6),
(3.9, 15.4), (4.4, 15.1), (4.8, 13.7), (5.5, 11.6) and (6, 0) were built,
tuned to give similar total numbers; only (6, 0) is the real cut, the
others serve validation and blinding [src: arXiv:2402.08458, Sect. 3.4].
Each was tested against ≈ 2.5e5 held-out clusters and against 10 Poisson
realisations [src: same].

### Morphology and central AGN
<!-- key: morphology-and-central-agn -->

The XXL C1 class misses clusters with centrally peaked profiles. A
dedicated AGN-contaminated (AC) class found 33 objects, 25 of them clusters
at 0.14 ≤ z ≤ 1.03, and seven undetected AC clusters above z > 0.6; the
missed fraction is ≈ 5% over 50 deg² [src: Bhargava et al. 2023,
arXiv:2301.11196, abstract]. The selection with misses is written
C1_selfunc,contam = C1_selfunc − d ⟨C1_selfunc/AC_selfunc⟩ AC_selfunc
(Eq. 6), d = 0.05 from 8 of 178 clusters [src: Sect. 7.2]. Ignoring it is
negligible for XXL but gives ≈ 3σ from the fiducial cosmology for a larger
area (1000 deg² tested) [src: abstract, Sect. 7.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Extent cuts | L_ext > 3 (primary), > 6 (cosmology) | eRASS1 | arXiv:2402.08457 | Sect. 3.1 |
| Contamination | 20% after L_ext > 6 (sims), ≈ 6% after optical confirmation; Poisson 1.4% | eRASS1 | arXiv:2402.08458 | Sect. 4.2 |
| Training set | ≈ 4.8e5 clusters; 30 inducing points; 651 hyperparameters | eRASS1 GP | arXiv:2402.08458 | Sect. 3.3 |
| Detected / selected fraction per twin | < 4% / < 1% of ≈ 1e6 haloes | eRASS1 | arXiv:2402.08457 | Sect. 3.4 |
| Matching difference | up to × 2 per flux bin below ~1e-14 erg s⁻¹ cm⁻² | eRASS1 | arXiv:2402.08457 | Sect. 3.3.3 |
| Average precision | 70% (CR, z, H); 74% with EM_0 | eRASS1 cosmology | arXiv:2402.08457 | Sect. 5.4 |
| Optical completeness | > 97% of SZ clusters identified | eROMaPPer | arXiv:2402.08458 | Sect. 3.5 |
| eFEDS → eRASS1-cosmo | 19.5 ± 3.2 predicted, 35 found (5σ) | external test | arXiv:2402.08457 | Sect. 6.2 |
| eRASS1-cosmo → eFEDS | 35.7 ± 1.3 predicted, 36 found | external test | arXiv:2402.08457 | Sect. 6.3 |
| eFEDS → eRASS1-main | 30.5 ± 4.2 predicted, 61 found (> 7σ) | external test | arXiv:2402.08457 | Sect. 6.4 |
| eRASS1-cosmo vs SPTpol-100d | 11.4 ± 2.4 predicted, 8 found; ρ = 0.2 between ln L_X and ln ζ | external test | arXiv:2402.08457 | Sect. 6.5 |
| Sample variance / shot noise | ≈ 1/5 (eRASS1), ≈ 1/10 (SPT-like) | eRASS1 | arXiv:2402.08458 | Sect. 8.5 |
| XXL C1 purity | < 5% point sources misclassified | XXL | arXiv:2109.13171 | Sect. 2.1 |
| XXL selection blur test | σ = 0.05 CR^−0.6 θ_c^−0.4 | XXL | arXiv:2109.13171 | Eq. 20 |
| XXL missed (AGN-peaked) fraction | ≈ 5%; ≈ 3σ bias at 1000 deg² if ignored | XXL | arXiv:2301.11196 | abstract, Sect. 7.2 |
| ASpiX gain | ≈ × 2 on σ8–Ω_m vs dn/dz, same 178 clusters | XXL | arXiv:2205.05499 | Sect. 2.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Faint clusters under-predicted.** The eRASS1 model predicts too few
  eFEDS clusters in eRASS1 (5σ for the cosmology sample, > 7σ for the
  primary one), with P_i systematically below the observed match
  fractions; no single cause was found, and the test proved highly
  sensitive to small model changes [src: arXiv:2402.08457, Sects. 6.2,
  6.4, 7.2.4]. The bright end matches SPT [src: Sect. 8]. Test: external
  validation against a deeper X-ray field and an SZ sample, both
  directions.
- **Selection tied to the twin's physics.** A (M, z) model inherits the
  scaling relations of the simulation; morphology is marginalised over the
  twin's distribution even in the (CR, z, H) model [src: arXiv:2402.08457,
  Sects. 5.3, 8]. Test: compare models with and without a morphology
  feature; an inject-and-retrieve campaign in real data is named as the
  planned alternative [src: Sect. 8].
- **Centrally peaked clusters and AGN.** Missed by an extent-based class;
  ≈ 5% in XXL, and a 3σ effect at 1000 deg² [src: arXiv:2301.11196,
  abstract]. Test: a dedicated point-plus-extended detection class.
- **Selection blurred or mis-sized.** Smoothing the XXL selection with
  Eq. 20 widens S8 and lowers its mean [src: arXiv:2109.13171, Sect. 6.5].
  Test: rerun the cosmology with a degraded selection.
- **Matching ambiguity.** Photon and positional matching disagree at low
  flux [src: arXiv:2402.08457, Sect. 3.3.3]. Test: carry both through to
  the selection model.
- **Optical step treated as completeness.** In eRASS1 it models
  contamination; incompleteness from it is limited to line-of-sight
  overlaps [src: arXiv:2402.08458, Sect. 3.5]. A sample with a high
  richness cut would need it modelled as completeness.
- **Low-mass spurious sources.** 30% spurious below 1e14 M_sun in eRASS1,
  absorbed by the mixture model and the lensing calibration; baryons in the
  mass function will matter for deeper eROSITA samples [src:
  arXiv:2402.08458, Sect. 8.5].

## Reading list
<!-- key: reading-list -->

- Review: Pierre 2022, arXiv:2205.05499 — why X-ray counts are hard and
  the case for observable-space (CR, HR, z) modelling.
- Review: Miyatake 2025, arXiv:2505.07697 — Sect. 3.2 and Eq. 11 for the
  place of S(θ_obs, z) in the count model.
- Method: Clerc et al. 2024, arXiv:2402.08457 — twin, matching,
  classifiers, internal and external validation.
- Application: Ghirardini et al. 2024, arXiv:2402.08458 — Sects. 2.2,
  3.3–3.5, 4.2–4.3: the adopted Θ_sel, GP set-up, optical step, mixture
  model and count integral.
- Data: Bulbul et al. 2024, arXiv:2402.08452 — the extent-selected
  catalogue and its cuts.
- Application: Garrel et al. 2021, arXiv:2109.13171 — XXL C1 selection in
  (CR, θ_c), ASpiX likelihood, selection-blur test.
- Critique: Bhargava et al. 2023, arXiv:2301.11196 — AGN-peaked clusters
  missed by extent selection and their cosmological cost.

## Not verified
<!-- key: not-verified -->

- The eRASS1 digital-twin paper (Seppi et al. 2022) and Pacaud et al. 2006
  (XXL selection procedure): cited by the papers read, not read, no
  identifier recorded.
- The S8 values of the XXL selection-blur test (Table 12 of
  arXiv:2109.13171) and the numbers of the SPTpol-ECS external tests
  (arXiv:2402.08457, Sects. 6.7–6.8): not read.
- How the eRASS1 analysis propagates the GP confidence levels of the
  selection model into the cosmology: Sect. 3.4 of arXiv:2402.08458 says the
  probability is "fully integrated into the likelihood"; whether the
  uncertainty is marginalised was not found in the sections read.
- The XXL selection functions for C2 clusters, and the eFEDS selection
  function used as reference in the external tests.
