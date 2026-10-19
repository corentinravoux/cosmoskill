# High-redshift galaxies and the age problem — cosmo-tensions-anomalies dossier

Scope: how a JWST abundance "stress test" of ΛCDM is computed (halo mass
function, baryon bound, observed density, Poisson and sample variance,
Eddington bias, stellar-mass systematics, statistic), how much each choice
moves the required star-formation efficiency, how a change of cosmology
enters, and how the ages of the oldest stars are turned into a bound on the
age of the Universe and on H0.
Snapshot: 2026-10-18.
From: CosmoVerse white paper (arXiv:2504.01669), Sect. 2.3.10; Abdalla et
al. 2022 review (arXiv:2203.06142), Sect. VI.4.

Already in L2, not repeated here: the Boylan-Kolchin bound with its Eqs.
1–5 and the observed-side systematics as named in
`physics-and-methods.md#jwst-high-redshift-abundance`; the published
samples and their status (photometric candidates, FRESCO, the revised S1,
the UniverseMachine comparison) in
`results.md#jwst-high-redshift-galaxy-abundance`; the mundane explanations
with verdicts in `systematics.md#jwst-abundance`; the dispute in
`open-questions.md#jwst-is-there-anything-left-for-cosmology`; the samples
in `surveys-and-data.md#jwst-high-redshift-samples`. The reionisation
reading of the same galaxies belongs to `cosmo-reionization-21cm`; early
dark energy physics to `cosmo-early-universe-exotica`.

Notation. M_* is a galaxy stellar mass, M_halo a halo mass, f_b ≡ Ω_b/Ω_m
the cosmic baryon fraction, ε ≤ 1 the fraction of a halo's baryons turned
into stars, so M_* = ε f_b M_halo (arXiv:2208.01611, Sect. 2). n(> M, z) is
a cumulative comoving number density and ρ_*(> M_*, z) the comoving stellar
mass density in galaxies above M_*. σ(M, z) is the rms linear fluctuation
on the mass scale M, ν = δ_c/σ the peak height, D(z) the linear growth
factor with D(0) = 1. t_U is the age of the Universe, z_f the formation
redshift of an old object. "ε" is called f_* in arXiv:2208.10479; this file
writes ε throughout.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the observable
<!-- key: step-1-choose-the-observable -->

Three observables are in use, with different strength:

- Cumulative stellar mass density ρ_*(> M_*): the observed value is
  ρ_*^obs(> M_*, z_eff) = (1/V) Σ_{M_i > M_*} M_i, summed over the galaxies
  above the threshold in a redshift bin of comoving volume V (Comini,
  Vagnozzi & Loeb 2026, arXiv:2604.13866) [src: Eq. 1]. The authors choose it
  because it is "relatively insensitive to individual outliers", compares
  directly with the halo bound "without requiring detailed knowledge of
  galaxy formation physics or galaxy-halo matching prescriptions", and was
  used by the earlier stress tests [src: Sect. 2].
- Cumulative number density n(> M_*), compared with n_halo(> M_*/f_b)
  (arXiv:2208.01611) [src: Eq. 3].
- The single most massive object, compared with the extreme-value
  distribution of the maximum halo or stellar mass in the survey volume
  (Lovell et al. 2023, arXiv:2208.10479) [src: Sects. 2–3].

Boylan-Kolchin states that the stellar-mass-density test is "more stringent
than the requirement that the observed galaxy UV luminosity function not
exceed the theoretical maximum" from instantaneous conversion of the
baryons, "as it is an integral constraint as opposed to a differential one"
(arXiv:2208.01611) [src: Sect. 4].

### Step 2. Predict the halo population
<!-- key: step-2-predict-the-halo-population -->

The Sheth–Tormen mass function as written by Comini et al.
[src: arXiv:2604.13866, Eqs. 2–3]:

dn/dM = (ρ̄_m/M) A sqrt(2a/π) [1 + (aν²)^(−p)] ν exp(−aν²/2) |dν/dM|,
σ²(M, z) = D²(z) ∫ dk/(2π²) k² P(k) W²(kR), R = (3M/4πρ̄_m)^(1/3),

with A = 0.3222, a = 0.707, p = 0.3, δ_c ≃ 1.686 and W the top-hat window;
predictions through the `hmf` package [src: Sect. 3.2]. Lovell et al. use
the Behroozi et al. 2013 mass functions, calibrated for 2 ≤ z ≤ 8 and
extrapolated above z = 8 because their parameter evolution "has smoothed
off"; other forms changed their conclusions little [src: Sect. 2.1].

How good the mass function is at the relevant masses: at z ≈ 7–10 the
Sheth–Tormen function "overestimates the abundance of massive halos by
20–50% relative to numerical simulations", so a bound computed with it is
conservative, and the lack of high-mass, high-redshift calibrations is named
as an open problem (arXiv:2208.01611) [src: Sect. 4]. A 2026 comparison of
Sheth–Tormen with a Bolshoi-calibrated variant finds that the calibration
"can materially affect the inferred host supply, particularly toward large z
(10)" (Yogeswaren & Schaefer 2026, arXiv:2610.08731) [src: abstract].

### Step 3. Convert halos to stars
<!-- key: step-3-convert-halos-to-stars -->

ρ_*^th(> M_*, z) = ε f_b ∫_{M_*/(ε f_b)}^∞ dM M dn/dM, and consistency
requires ρ_*^obs ≤ ρ_*^th (arXiv:2604.13866) [src: Eqs. 5–6]. Three ways to
treat ε:

- Fixed values, ε = 1 as the absolute bound and two smaller values (0.32,
  0.1) for realism (arXiv:2208.01611) [src: Sect. 3].
- A distribution: a lognormal ε truncated to [0, 1] with μ = e⁻² and σ = 1,
  meant to cover halo-model and observed values, "ignor[ing] the dependence
  of the stellar fraction on redshift and halo mass" (arXiv:2208.10479)
  [src: Eq. 9, Sect. 2.2].
- A free parameter, constrained jointly with cosmology
  (arXiv:2604.13866) [src: Sect. 2].

f_b is not one number across papers: 0.156 (Planck 2018; arXiv:2208.01611)
[src: Sect. 2], 0.158 (arXiv:2309.02492) [src: Fig. 1 caption], 0.16
(Planck 2015; arXiv:2208.10479) [src: Sect. 2.2]; Comini et al. recompute
f_b = ω_b/(Ω_m h²) at every MCMC step with ω_b = 0.02233 and H0 = 67.4
fixed, because Ω_m is sampled [src: Sect. 3.2].

### Step 4. Build the observed side
<!-- key: step-4-build-the-observed-side -->

What the published tests used:

| Sample | Area | Bin | Objects entering | Source |
|---|---|---|---|---|
| CEERS photometric candidates (Labbé et al.) | 38 arcmin², V ≈ 10⁵ Mpc³ per bin | 7 < z < 8.5 and 8.5 < z < 10 | the two most massive at z ≈ 7.5 and 9.1 | arXiv:2208.01611 [src: Sect. 3] |
| Same, Bayesian reanalysis | ~40 arcmin² | 8.5 < z < 10, z_eff ≃ 9.1 | three most extreme, two above 10¹⁰ M_⊙; two thresholds | arXiv:2604.13866 [src: Sect. 3.1] |
| FRESCO spectroscopic (Xiao et al.) | ~124 arcmin², GOODS-N and S | 5 < z < 6, z_eff ≃ 5.5 | S1, S2, S3 above 10¹¹ M_⊙; thresholds 1.096, 1.514, 2.344 × 10¹¹ M_⊙ | arXiv:2604.13866 [src: Sect. 3.1] |

The FRESCO reanalysis keeps the lowest bin "since the stellar masses
derived for galaxies in this bin are significantly more robust than those
of galaxies at higher redshifts" [src: Sect. 3.1]. Two consequences of
Eq. 1: only the most massive object enters the highest threshold [src:
Sect. 3.1], and V depends on the cosmology, so the observed density must be
recomputed when cosmology is varied [src: Sect. 2].

### Step 5. Put errors on the observed side
<!-- key: step-5-put-errors-on-the-observed-side -->

Poisson and sample variance. The field-to-field variance of counts in a
cone of radius Θ_s (small-angle form, after Hu & Kravtsov) is
(⟨n_i²⟩ − n̄²)/n̄² = [b_i²/(δr_i r_i²)] ∫ dℓ/(2π) ℓ [2J₁(ℓΘ_s)/(ℓΘ_s)]²
P(ℓ/r_i, z_i), with b_i the linear halo bias and δr_i the comoving depth of
the bin (Krishnan & Abazajian 2025, arXiv:2511.13708) [src: Eq. 8]. For
their sample of 31 galaxies, sample variance is "minimal" for nearly all
objects [src: Sect. II.2, Fig. 5]. Boylan-Kolchin includes both and finds
Poisson noise "always being dominant in the regime considered" [src:
arXiv:2208.01611, Sect. 4]. Xiao et al. note that two of their three
ultra-massive galaxies lie in a forming large-scale structure, so "the
potential effects of cosmic variance need to be carefully taken into
account before designing new models" [src: arXiv:2309.02492, main text].

Eddington bias. On a steep mass function more low-mass objects scatter up
than high-mass objects scatter down. Two corrections:

- Correct the data (Lovell et al.): ln M_edd = ln M_obs + ½ ε_slope
  σ²_lnM, with ε_slope the local slope of the halo mass function evaluated
  at M_obs/f_b and σ_lnM the mass error [src: arXiv:2208.10479, Eq. 13; the
  paper writes the slope as ε, renamed here].
- Convolve the model (Krishnan & Abazajian, after Lima & Hu):
  ρ_*^LH(> M_*) = ε f_b ∫ dM (dn̄/d ln M) ½ erfc{[ln(M_*/ε f_b) − ln M −
  ln M_sys]/sqrt(2σ²_lnM)} [src: arXiv:2511.13708, Eq. 11]. The resulting
  shift is on average about three times smaller than the exponential-tail
  formula ln M_edd − ln M_obs = −½ k σ²_lnM (their Eq. 10), because the mass
  function is not purely exponential [src: Sect. II.3]. For the z = 9.08
  CEERS galaxy at ε = 1, upscattering dominates by about 4 and raises
  ρ_*^LH by 80% [src: Fig. 3 caption].

Stellar-mass systematics. Krishnan & Abazajian take the median of the
central masses of all available SED pipelines and the largest deviation
from it as asymmetric systematic bounds; a single-pipeline object gets the
mean fractional systematic of the multi-pipeline objects [src: Sect. II.4].
They propagate the systematic as the shift M_sys inside Eq. 11, "rather
than inaccurately combining with random errors in quadrature" [src: Sect.
II.4].

### Step 6. Choose the statistic
<!-- key: step-6-choose-the-statistic -->

- Binary test: does the observed point lie below the ε = 1 curve
  (arXiv:2208.01611) [src: Sect. 3].
- Extreme-value confidence contours: for N independent draws from the halo
  mass distribution F, the density of the maximum is Φ(M_max = m; N) = N
  f(m) [F(m)]^(N−1) [src: arXiv:2208.10479, Eq. 4], with f and F built from
  dn/dM over the survey cone (their Eqs. 10–12); 1, 2 and 3σ intervals are
  integrated from narrow Δz = 0.2 bins [src: Sect. 2.1]; the EVS
  predictions of the most massive halo in EAGLE (100 Mpc)³ and FLARES (550
  Mpc)³ all lie within 3σ [src: Sect. 2.1, Fig. 2].
- One-sided likelihood with cosmology free: −ln L = ½ Σ_i
  (ρ_*,i^th − ρ_*,i^obs)²/σ_i² where ρ^th < ρ^obs, and 0 otherwise
  (arXiv:2604.13866) [src: Eq. 12]. The stated reason for the one-sided form:
  "incompleteness and selection effects may lead to an underestimation of
  the true abundance of massive galaxies", and a symmetric likelihood
  "would instead artificially strengthen the obtained constraints unless
  such effects were modeled explicitly" [src: Sect. 3.2]. Limits on ε are
  one-sided, quoted at the 32nd and 5th percentiles [src: Sect. 3.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Fixed cosmology and threshold, or a likelihood with cosmology free
<!-- key: fixed-cosmology-and-threshold-or-a-likelihood -->

Same CEERS objects. Boylan-Kolchin: at the theoretical limit ε(z ≈ 9) =
0.99 and ε(z ≈ 7.5) = 0.84; within 1σ errors marginally consistent for ε ≥
0.57 (arXiv:2208.01611) [src: Sect. 3]. Comini et al., with Ω_m, σ8 and ε
sampled: ε ≳ 0.39 (68%) and ε ≳ 0.07 (95%); ε = 0.2 within 1.0σ, 0.15 within
1.2σ, 0.1 within 1.4σ [src: arXiv:2604.13866, Sect. 4.1]. Their reading:
"the origin of the discrepancy is entirely in the different choice of
statistical methodology" and in the large CEERS errors [src: Sect. 4.1].
The cost is a weaker test; the gain is that the result no longer depends on
treating the errors as a pass-fail line.

### Photometric or spectroscopic sample
<!-- key: photometric-or-spectroscopic-sample -->

Same likelihood, flat ΛCDM: FRESCO gives ε ≳ 0.79 (68%) and ε ≳ 0.63
(95%), and ε = 0.2, 0.15 and 0.1 are each disfavoured at > 5.0σ
(arXiv:2604.13866) [src: Sect. 4.1]. Krishnan & Abazajian find smaller
systematic errors for spectroscopically confirmed galaxies with several SED
pipelines and name spectroscopic confirmation as "a potential path to
tighten the systematic errors" [src: arXiv:2511.13708, Sect. III]. The FRESCO
bin of Comini et al. includes S1 at its grism redshift [src: Sect. 3.1]; the
2026 multi-line redshift of S1 is z = 3.2439 (arXiv:2602.03030, in
`results.md`), so S1 would leave the 5 < z < 6 bin and the highest threshold
would be empty [der: from the two papers; Comini et al. do not discuss the
revision in the sections read].

### Correct the data or the model for Eddington bias
<!-- key: correct-the-data-or-the-model-for-eddington-bias -->

Correcting the data (Eq. 13 of arXiv:2208.10479) needs a mass error for each
object: for the CEERS candidates, where none was published, assuming 0.3 dex
moves three of the five objects that were above the ε = 1, 3σ limit back
inside, leaving two outside the 3σ contours for the lognormal ε [src: Sect.
3.3]. Convolving the model (Eq. 11 of arXiv:2511.13708) gives a smaller
shift for random errors (factor about 3) but provides the place where an
asymmetric systematic enters [src: Sect. II.3].

### Systematics as a shift or in quadrature
<!-- key: systematics-as-a-shift-or-in-quadrature -->

As a shift: with the full downward systematic and the random error in Eq.
11, the cumulative halo mass density for the example galaxy is about 730
times that from the central mass with a hard threshold, and the required ε
drops "by orders of magnitude" [src: arXiv:2511.13708, Sect. II.4]. The
downward systematic dominates even when the two systematic bounds are equal
[src: Sect. II.4]. For illustration only, adding systematics in quadrature
and fitting one ε to 31 galaxies gives ε_avg = 0.018 ± 0.004 with χ²_min/dof
= 0.94; the authors call combining systematics with random errors "in
general ... inappropriate" [src: Sect. III]. Their headline is therefore a
statement about error bars, not a measured ε.

### Extreme-value statistics: where its assumptions hold
<!-- key: extreme-value-statistics-where-its-assumptions -->

The EVS formula assumes independent, identically distributed halos; this
"will be broken where haloes are significantly clustered", and homogeneity
is reached above about (100 Mpc)³ (arXiv:2208.10479) [src: Sect. 2]. A JWST
bin of V ≈ 10⁵ Mpc³ (arXiv:2208.01611, Sect. 3) is a cube of side about 46
Mpc [der: (10⁵)^(1/3)], below that scale, so clustering of the hosts (the
large-scale structure noted by Xiao et al.) is outside the EVS null as
written [der].

## How cosmology enters
<!-- key: how-cosmology-enters -->

- Within ΛCDM the bound is "robust to uncertainties in cosmological
  parameters", each known to ≲ 1% (arXiv:2208.01611) [src: Sect. 4].
- At fixed σ8 the cosmology acts through the relative growth D(z)/D(0)
  (arXiv:2604.13866) [src: Sects. 2, 5]. Letting w (prior [−2, −0.33]) and
  Ω_K ([−0.2, 0.4]) vary changes the growth factor "at the level of tens of
  percent at best", against order-unity shifts in ε required by FRESCO;
  FRESCO requires ε ≳ 0.3–0.5 in all four models (flat and curved ΛCDM and
  wCDM), with ε = 0.1 excluded at > 5.0σ in each, and no preference for w ≠
  −1 or Ω_K ≠ 0 [src: Sects. 3.2, 5]. Priors used: Ω_m = 0.30 ± 0.03
  Gaussian, chosen to span the BAO-to-supernova spread, σ8 ∈ [0.76, 0.84],
  ε ∈ [0.01, 1.00] [src: Sect. 3.2]. ε and σ8 are anti-correlated, but
  escaping the FRESCO limit "would require implausibly high values of σ8"
  [src: Sect. 4.1].
- Early dark energy: with the best-fit parameters of Smith et al. 2022, the
  baryon density in halos above M_*/f_b for the z ≈ 9.1 candidate is 3.3
  times the ΛCDM value and the required ε falls from 0.99 to 0.72; the same
  cosmology raises the S8 tension and gives an age of about 13 Gyr, "in
  moderate tension with the measured ages of ultra-faint galaxies and
  globular clusters" (arXiv:2208.01611) [src: Sect. 4].
- Scale-limited power enhancement: a transient early-dark-energy-like phase
  in a sub-percent dark-matter fraction, during 10⁻⁷ ≲ a ≲ 10⁻⁵, produces an
  instability-driven growth of perturbations over a limited range of scales
  and lowers the required efficiencies, especially at higher redshift
  (Bhattacharjee et al. 2026, arXiv:2608.20288) [src: abstract]. Such models
  are built to leave CMB and BAO untouched; their test is the shape of the
  enhancement, not the abundance alone.

The same side effects tie the abundance question to the H0 resolutions:
any model that raises early growth must also pass S8 and the stellar-age
bound below (`open-questions.md#what-a-viable-resolution-must-pass`).

## The age problem: oldest stars against the age of the Universe
<!-- key: the-age-problem-oldest-stars-against-the-age-of -->

How it is done. An object of age t formed at z_f bounds H0 through
H0 = (A/t) ∫_0^{z_f} dz′ / [(1 + z′) E(z′)], A = 977.8 to convert Gyr to
km/s/Mpc; for z_f → ∞, t → t_U (Cimatti & Moresco 2023, arXiv:2302.07899)
[src: Eqs. 1–2]. Inputs: an age, a formation-redshift prior and Ω_m.

| Analysis | Data and method | Result | Source |
|---|---|---|---|
| Literature compilation | globular clusters, stars, white dwarfs, dwarf galaxies older than 13.3 Gyr; 11 ≤ z_f ≤ 30; Ω_M = 0.3 ± 0.02 | H0 < 70.6 from the most accurate individual ages; H0 < 73.0 with probability 90.3% from averaged subsamples, errors about 2.5 | arXiv:2302.07899 [src: abstract] |
| Globular clusters, full colour–magnitude diagram, hierarchical Gaussian-mixture model, helium and reddening law free | HST photometry, Gaia distances | t_GC = 13.39 ± 0.10 (stat) ± 0.23 (sys) Gyr; t_U = 13.57 (+0.16/−0.14) ± 0.23; 95% upper limit 13.92 (+0.13/−0.1) ± 0.23 | Valcin et al. 2025, arXiv:2503.19481 [src: abstract] |
| Same with two stellar populations per cluster | 69 clusters, [Fe/H] < −1.5 subsample | multiple populations change ages by 0.6σ; t_GC = 13.61 ± 0.25 ± 0.23; t_U = 13.81 ± 0.25 ± 0.23 | Valcin et al. 2026, arXiv:2603.04872 [src: abstract] |
| Individual Gaia DR3 turn-off and subgiant stars, StarHorse ages on a 0–20 Gyr prior | 160 stars after cuts | age peak 13.6 ± 1.0 (stat) ± 1.3 (syst); with z_f = 20 (delay ∼ 0.2 Gyr) t_U ≥ 13.8 ± 1.0 ± 1.3; none exceeds 14.1 Gyr at its 10th percentile | Tomasetti et al. 2025, arXiv:2509.02692 [src: abstract] |
| LAMOST + Gaia, YY isochrones to 20 Gyr, metal-poor α-enriched stars | 146,810 stars within 5 kpc | oldest star 13.80 (+0.20/−0.16) Gyr, systematic ± 0.4 | Banik et al. 2026, arXiv:2607.00764 [src: abstract] |

The threshold "how old is old" is a choice. Cimatti & Moresco keep objects
older than 13.3 Gyr as "the best trade-off" between taking the oldest and
keeping every class and method, and check that the cut lies within 1σ of
the upper edge of the age distribution, so that it does not select
fluctuations [src: arXiv:2302.07899, Sect. VI.3].

The two readings.

- As a test of ΛCDM: the globular-cluster t_U is "fully compatible" with the
  CMB-derived 13.8 ± 0.02 Gyr in ΛCDM (arXiv:2503.19481) [src: abstract];
  stellar ages contradict neither the CMB nor the ladder at the precision
  of the averaged H0 bound (< 73.0 at 90.3%, arXiv:2302.07899).
- As a test of H0 solutions: Banik et al. argue that pre-recombination
  solutions that match low-redshift probes "generally imply a cosmic age of
  12.9 ± 0.2 Gyr", which their oldest-star age disfavours, and that stellar
  modelling cannot easily close the gap given the low metallicities and
  asteroseismic constraints (arXiv:2607.00764) [src: abstract]; the same
  argument against the EDE cosmology of Smith et al. is made at lower
  precision in arXiv:2208.01611 [src: Sect. 4]. Banik et al. quote 13.6 Gyr
  for CMB-calibrated ΛCDM where Valcin et al. quote 13.8 ± 0.02; the source
  of the difference is not stated in the abstracts.

Systematic error budgets: for globular clusters the systematic (0.23 Gyr)
exceeds the statistical error in every release [src: arXiv:2503.19481,
arXiv:2603.04872, abstracts]; for individual field stars the systematic is
1.3 Gyr [src: arXiv:2509.02692, abstract] and 0.4 Gyr from cuts, isochrones
and helium [src: arXiv:2607.00764, abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Sheth–Tormen parameters | A = 0.3222, a = 0.707, p = 0.3, δ_c ≃ 1.686 | Comini et al. | arXiv:2604.13866 | Eq. 2 |
| ST overabundance of massive halos at z ≈ 7–10 | 20–50% vs simulations | Boylan-Kolchin | arXiv:2208.01611 | Sect. 4 |
| f_b | 0.156; 0.158; 0.16 | three tests | arXiv:2208.01611; arXiv:2309.02492; arXiv:2208.10479 | Sect. 2; Fig. 1; Sect. 2.2 |
| Lognormal ε | μ = e⁻², σ = 1, truncated to [0, 1] | Lovell et al. | arXiv:2208.10479 | Eq. 9 |
| EVS homogeneity volume | ≳ (100 Mpc)³ | Lovell et al. | arXiv:2208.10479 | Sect. 2 |
| EVS redshift bins | Δz = 0.2 | Lovell et al. | arXiv:2208.10479 | Sect. 2.1 |
| CEERS volume per bin | ≈ 10⁵ Mpc³ (38 arcmin²) | Boylan-Kolchin | arXiv:2208.01611 | Sect. 3 |
| Peak height of CEERS hosts | ν ≥ 4.5 (ε = 1); 5.4, 6.4 for ε = 0.32, 0.1 | Boylan-Kolchin | arXiv:2208.01611 | Sect. 3 |
| CEERS ε, fixed cosmology | ε ≥ 0.57 (1σ) | Boylan-Kolchin | arXiv:2208.01611 | Sect. 3 |
| CEERS ε, cosmology marginalised | ≳ 0.39 (68%), ≳ 0.07 (95%) | Comini et al. | arXiv:2604.13866 | Sect. 4.1 |
| FRESCO ε, flat ΛCDM | ≳ 0.79 (68%), ≳ 0.63 (95%); 0.1–0.2 excluded > 5σ | Comini et al. | arXiv:2604.13866 | Sect. 4.1 |
| Eddington shift, LH against exponential formula | about 3 times smaller | Krishnan & Abazajian | arXiv:2511.13708 | Sect. II.3 |
| ρ_* boost from random scatter, z = 9.08 example | +80% | Krishnan & Abazajian | arXiv:2511.13708 | Fig. 3 |
| ρ_* boost from downward SED systematic + random | ≈ 730 | Krishnan & Abazajian | arXiv:2511.13708 | Sect. II.4 |
| EDE halo-baryon boost, z ≈ 9.1 | 3.3; ε 0.99 → 0.72 | Boylan-Kolchin | arXiv:2208.01611 | Sect. 4 |
| H0 conversion constant | A = 977.8 (Gyr to km/s/Mpc) | Cimatti & Moresco | arXiv:2302.07899 | Eq. 1 |
| Oldest-object age cut | > 13.3 Gyr | Cimatti & Moresco | arXiv:2302.07899 | Sect. VI.3 |

## What goes wrong
<!-- key: what-goes-wrong -->

- Photometric redshift degeneracy. A Balmer or 4000 Å break at z ∼ 5 can
  mimic a Lyman break at z ≳ 12 (arXiv:2208.01611, Sect. 4) [src]; the z ∼ 17
  CEERS candidate is in "significant tension" with the EVS PDF at z ∼ 17,
  while its z ∼ 5 solutions are not (arXiv:2208.10479, Sect. 3.3) [src].
  Test: a spectroscopic redshift, or both photometric solutions carried
  through.
- Slitless-grism contamination by a neighbour (S1 in `results.md`). Test:
  multi-line or IFU spectroscopy before the object enters a cumulative bin.
- Eddington bias ignored on the steep tail. Shows up as a deficit of
  allowed ε at the highest masses. Test: apply Eq. 13 of arXiv:2208.10479
  or Eq. 11 of arXiv:2511.13708 and report both.
- Mass errors unpublished. The Eddington correction cannot be done;
  Lovell et al. had to assume 0.3 dex for CEERS [src: Sect. 3.3].
- SED systematics combined in quadrature. Hides the asymmetry that makes
  the downward systematic dominant (arXiv:2511.13708, Sect. II.4). Test:
  propagate the pipeline spread as a shift.
- Cosmology varied with the volume and f_b held fixed. Test: recompute V
  in Eq. 1 and f_b = ω_b/(Ω_m h²) at each sample (arXiv:2604.13866, Sects.
  2, 3.2).
- A symmetric likelihood on an incomplete sample: penalises models that
  predict more massive galaxies than observed, which incompleteness allows
  (arXiv:2604.13866, Sect. 3.2).
- Treating one field as a fair sample. Two of three FRESCO ultra-massive
  galaxies sit in one forming structure (arXiv:2309.02492) [src]; the
  sample-variance term of Eq. 8 of arXiv:2511.13708 uses linear bias and is
  "minimal" for most of their objects [src: Sect. II.2], which a protocluster
  may not respect.
- IMF assumed Salpeter. A different IMF "could affect the derived stellar
  masses" (arXiv:2208.01611, Sect. 4) [src]; not quantified in the papers
  read.
- Ages: the formation delay (0.2 Gyr for z_f = 20) and the age cut are
  priors; quote t_U with them. Comparing a t_U bound with the CMB age
  without naming the model of the CMB value repeats the endpoint error of
  the H0 tension.

## Reading list
<!-- key: reading-list -->

- Foundation: Boylan-Kolchin 2023, arXiv:2208.01611 — the baryon bound,
  peak heights, the EDE and mass-function caveats (Sects. 2–4).
- Method: Lovell et al. 2023, arXiv:2208.10479 — extreme-value statistics
  over a survey cone and the Eddington correction of the data (Sects. 2–3).
- Method: Comini, Vagnozzi & Loeb 2026, arXiv:2604.13866 — one-sided
  likelihood, ε with cosmology free, w and Ω_K (Sects. 2–5).
- Critique: Krishnan & Abazajian 2025, arXiv:2511.13708 — sample variance,
  Lima–Hu convolution, SED systematics as a shift (Sects. II–III).
- Application: Xiao et al. 2024, arXiv:2309.02492 — the FRESCO sample; and
  Xiao et al. 2026, arXiv:2602.03030 — the revision of S1.
- Mass function calibration: Yogeswaren & Schaefer 2026, arXiv:2610.08731
  (abstract).
- Model: Bhattacharjee et al. 2026, arXiv:2608.20288 — scale-limited
  enhancement of early halos (abstract).
- Age method: Cimatti & Moresco 2023, arXiv:2302.07899 — Eq. 1 and the age
  threshold.
- Age data: Valcin et al. 2025, arXiv:2503.19481 and 2026, arXiv:2603.04872
  (globular clusters); Tomasetti et al. 2025, arXiv:2509.02692 and Banik et
  al. 2026, arXiv:2607.00764 (field stars).

## Not verified
<!-- key: not-verified -->

- Hu & Kravtsov (sample variance) and Lima & Hu (convolution) are cited
  through arXiv:2511.13708 only; Smith et al. 2022 (the EDE best fit) and
  Boylan-Kolchin & Weisz 2021 (ultra-faint ages) through arXiv:2208.01611
  only. None was read.
- The Comini et al. limits for wCDM, curved ΛCDM and curved wCDM (Sects.
  4.2–4.4) were read only as summarised in their Sect. 5.
- Whether any analysis has recomputed the FRESCO density with S1 at z =
  3.24; the consequence stated above is derived.
- The bodies of arXiv:2608.20288, arXiv:2610.08731, arXiv:2503.19481,
  arXiv:2603.04872, arXiv:2509.02692 and arXiv:2607.00764: abstracts only
  (for arXiv:2503.19481 also its introduction); the delay assumed between
  the Big Bang and globular-cluster formation in the Valcin et al. papers
  was not read.
- The size of IMF, nebular-line and dust effects on the stellar masses of
  the specific FRESCO and CEERS objects.
