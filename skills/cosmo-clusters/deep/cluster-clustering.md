# Clustering of clusters — cosmo-clusters dossier

Scope: how a cluster two-point measurement is made and modelled (estimator,
randoms that carry the selection, projection depth, the effective-bias
integral through the mass–observable relation, photometric-redshift and
RSD terms, scale cuts, covariance, blinding), and how to choose between
the projected, redshift-space, angular and multiprobe forms used by
eRASS1, SPT-3G, Planck, AMICO, XXL and DES.
Snapshot: 2026-10-17.
From: eRASS1 clustering paper (arXiv:2402.08460); SPT-3G clustering
(arXiv:2610.08947); Euclid systematics study (arXiv:2510.13509); DES
multiprobe strategy (arXiv:2503.13631).

Already in L2, not repeated here: the measured biases, the list of
statistics in use, the self-calibration forecasts and the debate on how
much clustering adds in `physics-and-methods.md#clustering-of-clusters`
and `open-questions.md#method-debates`; the clustering results in
`results.md`; the Tinker 2010 bias accuracy in
`systematics.md#halo-mass-function-and-bias`; the counts–clustering
independence and the photo-z broadening in
`systematics.md#likelihood-covariance-photometric-redshifts`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Build randoms that carry the selection
<!-- key: step-1-build-randoms-that-carry-the-selection -->

The random catalogue must reproduce the angular and redshift selection of
the clusters; for clusters this means the selection function, not only
the mask.

| Analysis | Randoms | Size | Place read |
|---|---|---|---|
| eRASS1 | Legacy DR10 randoms (50000 deg⁻²) with g, r, z coverage; each point is given a count rate and redshift drawn from a kernel density of the digital twin and kept if the X-ray selection probability (count rate, redshift, exposure, background, n_H) exceeds a uniform random number | ≈ 50 × the data | arXiv:2402.08460, Sect. 2.2 |
| SPT-3G | uniform on the sphere inside the footprint, redshifts by inverse sampling a spline of the data n(z); no angular completeness weighting, since the Main field is uniform and no correlation with noise level was found | > 100 × the data | arXiv:2610.08947, Sect. III |
| Planck | n(z) smoothed with a Gaussian of rms 0.02; positions through the MMF3 survey mask, a hole mask and an ERF completeness at q = 4.5 with sample-mean Y500 and θ500 (Eq. 1); alternatively pair weights 1/σ_Yi^norm, with the same results | 100 × the data | arXiv:2302.14074, Sect. 2.2 |

eRASS1 rejected randoms built from eSASS sensitivity maps, which assume a
β profile for extended sources, because they "may therefore introduce
spurious clustering" [src: arXiv:2402.08460, Sect. 2.2]. It also cut the
sample to 0.1 < z < 0.6 because the data n(z) peaks near z = 0.8 at an
optical filter transition that the randoms do not follow [src: same]. Its
check: the angular correlation scales as θ^−0.82, against the expected
slope −0.8 [src: same].

### Step 2. Measure
<!-- key: step-2-measure -->

All three 3D analyses use the Landy–Szalay estimator, ξ = 1 + (N_RR/N_DD)
DD/RR − 2 (N_RR/N_DR) DR/RR, with N_DD = N_D(N_D − 1)/2, N_RR likewise and
N_DR = N_D N_R (arXiv:2402.08460, Eq. 1; arXiv:2610.08947, Eq. 2;
arXiv:2302.14074, Eq. 2) [src]. They differ in what is kept:

| Analysis | Statistic | Scales | Line-of-sight treatment | Place read |
|---|---|---|---|---|
| eRASS1 | w_p(r_p) = 2 ∫_0^π_max ξ(r_p, π) dπ (Eq. 2) | 10 log bins, 1–80 Mpc/h; Δπ = 1 Mpc/h | π_max = 100 Mpc/h; 80 and 120 do not raise S/N | arXiv:2402.08460, Sect. 3 |
| SPT-3G | w_p(r_p) (Eq. 3) | 10 log bins, 10–100 Mpc/h | π_max = 80 Mpc/h, maximises S/N in simulations; 100 and 120 lose ≈ 10% | arXiv:2610.08947, Sect. III |
| Planck | redshift-space monopole ξ_0(s) in z < 0.2 (407 clusters) and 0.2–0.8 (513) | 10–150 Mpc/h; s < 15 Mpc/h dropped in the high-z bin for lack of pairs | higher multipoles verified negligible | arXiv:2302.14074, Sect. 2.3 |
| AMICO KiDS-DR3 | angular w(θ) and C_ℓ in photometric shells | 5162 clusters, λ* ≥ 15, 0.1 ≤ z ≤ 0.6 | top-hat photo-z windows integrate out the redshift error | arXiv:2310.12224, abstract, Sect. 3.3 |
| DES Y3/Y6 model | projected w_cc, w_cg with w_gg and lensing | cuts at 16 Mpc/h (w_cc) and 8 Mpc/h (w_cg) | projected in photometric bins | arXiv:2503.13631, App. B |

Reasons given: SPT-3G uses w_p rather than an angular correlation because
the projection over π_max ≈ doubles the S/N [src: arXiv:2610.08947, Sect.
III]; cluster photo-z, averaged over members, are precise enough to
measure line-of-sight separations: half the SPT-3G sample has σ_z/(1 + z)
≤ 0.02, ≈ 35 Mpc/h along the line of sight [src: same]. eRASS1 chose
π_max so that it is well beyond the photo-z scatter of 0.005(1 + z),
≈ 25 comoving Mpc at z = 0.3 [src: arXiv:2402.08460, Sect. 3]. The lower
SPT-3G cut of 10 Mpc/h is where the linear bias prescription stops being
viable; the upper cut is where S/N plateaus, smaller than the 130 Mpc/h
used in the Euclid study because the smaller SPT-3G area has more cosmic
variance at large separation [src: arXiv:2610.08947, Sect. III and
footnote 3].

### Step 3. Model the effective bias through the selection
<!-- key: step-3-model-the-effective-bias-through-the -->

The bias of a cluster sample is not fitted freely in a cosmology analysis;
it is predicted from the halo bias b(M, z), the mass function and the
observable–mass relation of the selection observable.

- **SPT-3G** (arXiv:2610.08947, Sect. IV.2):

      b(ln ζ, z) = (1/A) ∫ dM b(M, z) (dn/dM) P(ln ζ | M, z)              (Eq. 11)
      b(ξ_SZ, z) = (1/A) ∫ dζ b(ζ, z) P(ξ_SZ | ζ, z)                        (Eq. 13)

  with P(ξ_SZ | ζ) = N(√(ζ² + 3), 1) (Eq. 9), ⟨ln ζ⟩ = ln A_SZ + B_SZ
  ln(M200c / 1e14 M_sun h⁻¹) + C_SZ ln(E(z)/E(0.6)) (Eq. 10) and A the
  normalisation [src]. The same formalism is used in SPT abundance work
  and in optical cluster clustering [src: same]. Note that the pivot here
  is 1e14 M_sun/h, not the 3e14 M_sun/h of the SPT abundance paper
  (arXiv:2310.12213, Eq. 41), so the ln A_SZ values of the two are not
  directly comparable without conversion.
- **Planck** (arXiv:2302.14074, Sect. 3.2): b_eff is the mean over
  clusters of b(Y^ob_500,j, z_j), each an integral of the Tinker 2010 bias
  times the Tinker 2008 mass function over the lognormal Y–M relation (the
  Planck form with (1 − b_SZ)) and a Gaussian measurement error on Y (Eqs.
  13–17) [src].
- **Euclid study** (arXiv:2510.13509, Sect. 2.2): b_eff per observed
  richness bin, weighting the mass function by halo bias; cross-spectra
  between richness bins as √(P_i P_j) (Eq. 14) [src].
- **eRASS1** replaces the scaling-relation route by an HOD: central
  occupation N_C = f_inc(M) ½[1 + erf(log(M/10^M_min)/σ_logM)], satellites
  N_S = N_C ((M − 10^(M_sat−1))/10^M_sat)^α_sat, and an incompleteness
  term f_inc with slope fixed to 0.55 from the twin (Eq. 9) [src:
  arXiv:2402.08460, Sect. 3.1.1]. The stated reason: halo-bias models
  differ by more than 20% in the cluster regime, and a fixed bias model at
  fixed mass "may bias cosmological results"; the HOD models bias and
  occupation self-consistently with no prior on mass, M_min is sampled
  with cosmology, and σ_logM, α_sat, M_sat are nuisance parameters [src:
  Sect. 3.1.2].
- **Choice of b(M, z).** SPT-3G uses the Aemulus bias emulator, accurate to
  better than 3% over its mass–redshift range, instead of Tinker 2010,
  which performs worse for the rare high-mass, high-redshift haloes of
  tSZ samples [src: arXiv:2610.08947, Sect. IV.2]. The DES strategy keeps
  Tinker for both mass function and bias, which carry 5–10% and 10–20%
  uncertainty, and tests against Aemulus (1% and 3%) [src:
  arXiv:2503.13631, Sects. II.3.2, IV.1.2].

### Step 4. Add redshift-space and photo-z terms
<!-- key: step-4-add-redshift-space-and-photo-z-terms -->

- **SPT-3G** folds the n(z) kernel, a Gaussian line-of-sight damping
  e^{−k_∥² σ_χ²(z)} for photo-z, the π_max window 2 sin(k_∥ π_max)/k_∥ and a
  Kaiser term [b_eff + f k_∥²/(k_∥² + k_⊥²)]² into one expression for w_p
  (Eq. 14), then bin-averages over annuli (Eq. 15) [src: arXiv:2610.08947,
  Sect. IV.3].
- **Euclid** writes the photo-z-convolved Kaiser spectrum P_obs = P′ +
  β P″ + β² P‴ with erf kernels in kσ, σ = c σ_z / H(z) and β = f_g/b_eff
  (Eqs. 16–20), IR-resums the BAO (Eqs. 21–22), and neglects fingers of God
  because their shape resembles the photo-z damping and is much smaller
  [src: arXiv:2510.13509, Sect. 2.2].
- **Planck** uses a one-loop TNS-type redshift-space model with Gaussian
  fingers-of-God damping exp(−k′² μ′² f² σ_v²), σ_v² from linear theory
  (Eqs. 9–12), and AP distortions through α_∥ and α_⊥ including the sound
  horizon (Eqs. 4–8), the AP part only in the cosmology fit [src:
  arXiv:2302.14074, Sect. 3.1]. A test adds a redshift-error dispersion
  σ_v,z = c σ_z (1 + z̄)/H(z̄) in quadrature (Eqs. 21–22) [src: Sect. 4.1.1].
- **eRASS1** applies AP via α_∥ = H^fid/H and α_⊥ = D_A/D_A^fid (Eq. 12),
  linear spectrum from Eisenstein & Hu and non-linear from Smith et al.,
  and adds no photo-z term, justified by the mock test below [src:
  arXiv:2402.08460, Sects. 3, 3.1.2].
- **AMICO** convolves the true n(z) with Gaussian P(z_phot | z),
  σ_z = 0.02(1 + z), through the top-hat photometric window (Eqs. 10–14)
  [src: arXiv:2310.12224, Sect. 3.3].

### Step 5. Selection effects on the clustering amplitude (optical)
<!-- key: step-5-selection-effects-on-the-clustering -->

For richness-selected clusters, the environment changes both detection and
richness, which adds bias to every cluster correlation. DES Y6 models it as
a scale-dependent ratio to the original model,
Σ_cA/Σ_cA[Orig](θ) = b_s1 + b_s2 exp(−θ χ(z̄)/r_0), the same ratio for w_cg,
and its square root for w_cc (Eq. 23) [src: arXiv:2503.13631, Sect.
II.3.5]. The square root comes from the selection modulating the cluster
density field, which enters cluster clustering twice (a quadratic boost),
validated in HOD-cylinder mocks [src: same]. Using a scale-independent
model instead, as in DES Y1, biases S8 and Ω_m by 0.45 of the statistical
error at the Y6 scale cuts [src: same].

### Step 6. Covariance and likelihood
<!-- key: step-6-covariance-and-likelihood -->

| Analysis | Covariance | Likelihood | Place read |
|---|---|---|---|
| eRASS1 | jackknife diagonal, removing one HEALPix NSIDE-8 pixel (≈ 54 deg²) at a time (Eq. 3) times the correlation matrix of 1000 GLASS simulations (Eq. 4), because the simulations lack the selection and geometry | Gaussian (Eq. 13); UltraNest | arXiv:2402.08460, Sects. 3, 3.2 |
| SPT-3G | analytic: Gaussian shot noise, Gaussian cosmic variance and leading non-Gaussian term, after the Euclid prescription; validated against jackknife on full-sky simulations rescaled to 1600 deg² with 100 patches (Eqs. 17–18) | Gaussian, χ² of Eq. 16; Gaussianity checked on 500 Poisson realisations (KS p = 0.59); emcee in CosmoSIS | arXiv:2610.08947, Sects. IV.4–IV.5 |
| Planck | bootstrap over 200 angular and 2 redshift regions, 2000 resamplings, Hartlap correction | Gaussian | arXiv:2302.14074, Sect. 2.3 |
| AMICO KiDS-DR3 | jackknife per redshift bin; redshift bins taken as independent | Gaussian (Eqs. 34–36) | arXiv:2310.12224, Sect. 5.1 |
| Euclid study | analytic with fitted parameters, validated on 1000 mocks | Gaussian for counts, clustering and lensing masses | arXiv:2510.13509, Sects. 2.4, 4.4.2 |

Reasons: SPT-3G sized jackknife patches to exceed the largest scale,
100 Mpc/h, which allows only ≈ 25 patches on 1600 deg², too few for a
10-bin data vector; hence the full-sky route [src: arXiv:2610.08947,
Sect. IV.5]. It used Poisson realisations for the Gaussianity check
because its covariance is shot-noise dominated [src: Sect. IV.4,
footnote 5]. The Euclid study also finds the 2PCF covariance largely
shot-noise dominated [src: arXiv:2510.13509, Sect. 4.4.2].

### Step 7. Combine with counts
<!-- key: step-7-combine-with-counts -->

- XXL enters the effective bias from its clustering analysis as an extra
  Gaussian term in the counts likelihood, because b_eff is an output of
  the counts model, depending on the selection in M–z, cosmology and the
  scaling relations [src: arXiv:2109.13171, Sect. 4.2].
- SPT-3G fits only ln A_SZ with cosmology and B_SZ, C_SZ fixed (Table 1),
  as a measure of statistical precision; joint fits with other SPT data
  are deferred [src: arXiv:2610.08947, Sect. IV.4].
- eRASS1 fits ω_c, A_s, ω_DE with n_s and ω_b fixed to Planck values, in an
  h-independent evolution-mapping parametrisation [src: arXiv:2402.08460,
  Sect. 3.1.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Projected, redshift-space or angular
<!-- key: projected-redshift-space-or-angular -->

- w_p is "far less sensitive" to photo-z and RSD modelling errors than 3D
  statistics [src: arXiv:2610.08947, Sect. III]. It still needs a photo-z
  term: with σ_pz ≈ 0.013(1 + z), redshift errors raise σ(ln A_SZ) by
  17.3% in mocks, and input values are recovered within 0.07σ once
  modelled [src: Sect. V.3].
- The 3D monopole keeps the BAO and RSD information but needs a
  redshift-space model; Planck clusters have mostly spectroscopic
  redshifts, and the fitted σ_z = 0.003 ± 0.002 [src: arXiv:2302.14074,
  Sect. 4.1.1].
- Angular statistics avoid line-of-sight modelling; for AMICO KiDS-DR3 the
  angular correlation gave Ω_m = 0.32 +0.05/−0.04, S8 = 0.80 +0.08/−0.06,
  the power spectrum Ω_m = 0.24 +0.05/−0.04, S8 = 0.93 +0.11/−0.12, with
  Gaussian priors on the mass–richness relation from the counts and
  lensing analysis of the same catalogue [src: arXiv:2310.12224,
  abstract].

### Scale range
<!-- key: scale-range -->

| Range tested (Euclid-like) | ΔFoM, clustering + lensing masses | Place read |
|---|---|---|
| 20–130 Mpc/h (reference) | — | arXiv:2510.13509, Table 4 |
| 40–130 | −14% | same |
| 60–130 | −37% | same |
| 20–200 | −3% | same |

Scales of 20–60 Mpc/h carry sizeable information, beyond the BAO adds
almost nothing for Ω_m and σ8 [src: arXiv:2510.13509, Sect. 4.4.3]. For
Planck, s in [15, 150] or [10, 90] Mpc/h moves (1 − b_SZ) by < 0.6σ
[src: arXiv:2302.14074, Sect. 4.1.1]. DES chose a linear cluster bias with
cuts at 16 and 8 Mpc/h because the b_2–b_1 non-linear model agrees worse
with Dark Emulator below 20 Mpc/h [src: arXiv:2503.13631, App. B].

### Which redshift effects to model
<!-- key: which-redshift-effects-to-model -->

Neglecting RSD in the model while the data contain them shifts the
Euclid-like posterior by IoI = 1.16 for clustering + lensing masses and
2.18 with counts, where IoI is the index of inconsistency with respect to
the input cosmology; neglecting IR resummation or geometric distortions
has almost no effect on position, and up to ≈ 10% on the FoM [src:
arXiv:2510.13509, Sects. 2.4, 4.4.2, Table 3]. Photo-z with σ_z0 = 0.005
and 0.01 reduce the FoM by 7% and 22% (clustering + lensing masses), 10%
and 31% with counts [src: Sect. 4.4.1, Table 2]. In eRASS1 mocks,
photo-z scatter of 0.005, 0.008 and 0.01 × (1 + z) shifts w_p by 1.8%,
12.9% and 15.3%, against a 33% relative error, so no photo-z term was
modelled [src: arXiv:2402.08460, Sect. 3, Eq. 5].

### Bias from a scaling relation, an emulator or an HOD
<!-- key: bias-from-a-scaling-relation-an-emulator-or-an -->

- Scaling relation + Tinker 2010 (Planck): the bias definition alone
  (median instead of mean of the bias distribution) moves (1 − b_SZ) by
  ≈ 0.5σ [src: arXiv:2302.14074, Sect. 4.1.1].
- Emulator (SPT-3G, Aemulus): < 3% accuracy in its range [src:
  arXiv:2610.08947, Sect. IV.2].
- HOD (eRASS1): no prior on mass, but the bias is then a derived,
  cosmology-coupled quantity; the flux-limited fit gives b = 3.63
  +1.02/−0.85 [src: arXiv:2402.08460, abstract].

### Assembly bias through the selection observable
<!-- key: assembly-bias-through-the-selection-observable -->

SZ selection at fixed mass favours more concentrated haloes in
hydrodynamical simulations, so mass and redshift alone may not predict the
sample bias. SPT-3G tested a concentration-correlated scatter
ζ_mod = ζ_orig (c_i / ⟨c | M, z⟩)^β with β = 0.1 and 0.3 (Eq. 19) and saw
no visible impact on the recovered ln A_SZ [src: arXiv:2610.08947,
Sect. V.5].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Detection significance | 12.8σ (full z); 11.9σ (low z), 4.7σ (high z) | SPT-3G | arXiv:2610.08947 | Sect. VII.1 |
| ln A_SZ from clustering | 0.43 +0.17/−0.21 (pivot 1e14 M_sun/h); low+high z 0.42 +0.19/−0.21 | SPT-3G | arXiv:2610.08947 | Sect. VII.1 |
| Fixed scaling and cosmology | B_SZ = 1.64, C_SZ = 0.91; σ8 = 0.80, Ω_m = 0.30, h = 0.7 | SPT-3G | arXiv:2610.08947 | Table 1 |
| Blinding offset | ln A_SZ drawn in [0, ln 3] around ln 2; unblind if splits agree at 0.0015 < p < 0.9985 | SPT-3G | arXiv:2610.08947 | Sect. VI.1 |
| Photo-z cost | +17.3% on σ(ln A_SZ) | SPT-3G mocks | arXiv:2610.08947 | Sect. V.3 |
| π_max | 100 Mpc/h (eRASS1); 80 Mpc/h (SPT-3G) | — | arXiv:2402.08460; arXiv:2610.08947 | Sect. 3; Sect. III |
| Flux-limited sample | 6493 clusters, 0.1–0.6, L_X > 5e42 erg/s, 15.16 Gpc³, purity > 96% | eRASS1 | arXiv:2402.08460 | Sect. 3.1.2, abstract |
| ω_c from clustering | 0.12 +0.03/−0.02 | eRASS1 | arXiv:2402.08460 | abstract |
| HOD incompleteness slope | α_inc = 0.55 fixed | eRASS1 | arXiv:2402.08460 | Sect. 3.1.1, Table 2 |
| Planck (1 − b_SZ) variants | 0.65 +0.15/−0.12 with σ_z free; 0.59 +0.12/−0.09 with the union catalogue | Planck clustering | arXiv:2302.14074 | Sect. 4.1.1 |
| Selection-model bias if scale independent | 0.45σ on S8, Ω_m | DES Y6 mocks | arXiv:2503.13631 | Sect. II.3.5 |
| Linear-bias scale cuts | 16 Mpc/h (w_cc), 8 Mpc/h (w_cg) | DES Y6 | arXiv:2503.13631 | App. B |
| RSD neglect | IoI 1.16 (CL+MWL), 2.18 (NC+CL+MWL) | Euclid-like mocks | arXiv:2510.13509 | Table 3 |
| Photo-z (σ_z0 = 0.01) | −22% / −31% FoM | Euclid-like mocks | arXiv:2510.13509 | Table 2 |
| Chain noise | < 4% on FoM, 1% on IoI | Euclid-like mocks | arXiv:2510.13509 | Sect. 2.4 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Randoms without the selection.** Spurious clustering from sensitivity
  maps that assume a β profile [src: arXiv:2402.08460, Sect. 2.2]. Test:
  the angular slope (≈ −0.8) and n(z) agreement of randoms and data.
- **n(z) features the randoms do not follow.** The eRASS1 peak at z ≈ 0.8
  from an optical filter transition; handled by a redshift cut [src:
  same].
- **Bias model outside its calibration.** Tinker-type fits for the rarest
  haloes [src: arXiv:2610.08947, Sect. IV.2]; > 20% spread between bias
  models [src: arXiv:2402.08460, Sect. 3.1.2]. Test: rerun with an
  emulator or simulated data from a different bias model.
- **Pivot or definition mismatch.** Comparing ln A_SZ from clustering
  (pivot 1e14 M_sun/h) with the abundance value (pivot 3e14 M_sun/h)
  without conversion; the SPT-3G paper states consistency with the
  abundance value of its reference catalogue paper [src: arXiv:2610.08947,
  Sect. VII.1].
- **RSD left out of a 3D or photometric model.** Biased posteriors even
  when the FoM barely changes [src: arXiv:2510.13509, Sect. 4.4.2]. Test:
  fit mocks with and without RSD in the model.
- **Scale-independent selection boost for optical clusters.** 0.45σ bias
  at DES Y6 cuts [src: arXiv:2503.13631, Sect. II.3.5]. Test: HOD-cylinder
  or simulation mocks with the finder's selection.
- **Jackknife patches smaller than the largest scale.** Accuracy "drops
  precipitously" [src: arXiv:2610.08947, Sect. IV.5]. Test: compare with
  analytic or simulation covariance.
- **Null tests used by SPT-3G.** Splits in ξ_SZ, redshift and sky,
  π_max and r_p range checks, and correlation with depth, noise, stellar
  density and extinction, all on blinded data, with the 3σ split criterion
  above [src: arXiv:2610.08947, abstract, Sects. VI.1–VI.6].

## Reading list
<!-- key: reading-list -->

- Foundation: Majumdar & Mohr 2004, arXiv:astro-ph/0305341, and Lima & Hu
  2004, arXiv:astro-ph/0401559 — why clustering self-calibrates the
  mass–observable relation.
- Foundation: Tinker et al. 2010, arXiv:1001.3162 — the halo bias fit most
  analyses still use.
- Method: Fumagalli et al. 2025, arXiv:2510.13509 — model with photo-z,
  RSD, IR resummation; which effects and scales matter.
- Application: Seppi et al. 2024, arXiv:2402.08460 — selection-aware
  randoms, w_p, HOD bias, hybrid covariance.
- Application: Martsen et al. 2026, arXiv:2610.08947 — effective bias
  through ξ_SZ, analytic covariance, blinding and null tests.
- Application: Lesci et al. 2023, arXiv:2302.14074 — redshift-space
  monopole with effective bias through the Planck Y–M relation.
- Application: Romanello et al. 2024, arXiv:2310.12224 — angular
  statistics for photometric clusters.
- Method: To et al. 2025, arXiv:2503.13631 — scale-dependent selection
  model for optical cluster correlations in a multiprobe analysis.
- Application: Garrel et al. 2021, arXiv:2109.13171 — clustering bias as a
  likelihood term in X-ray counts.

## Not verified
<!-- key: not-verified -->

- The Aemulus bias emulator paper and the result of the DES
  Tinker-versus-Aemulus test (arXiv:2503.13631, Sect. IV.1.2: the shift
  was not in the passage read).
- The analytic covariance terms of SPT-3G (its Appendix A) and of the
  Euclid study (cited there to an earlier Euclid paper): not read.
- The Euclid result that the counts covariance changes by 15–20% with RSD
  and photo-z is from the abstract of arXiv:2510.13509 only.
- The SPT-3G halo-bias value b_h = 5.30 ± 0.24 is from the abstract; its
  section was not read.
- The XXL cluster clustering measurement that enters arXiv:2109.13171 was
  not read.
