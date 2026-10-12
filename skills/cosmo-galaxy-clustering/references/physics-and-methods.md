# Galaxy clustering — physics and methods

Scope: what spectroscopic galaxy and quasar clustering measures, the
estimators, the theory models in current use, covariance, blinding, codes and
conventions. Snapshot: 2026-10-07.

Flags: `[src]` read this session in the cited paper or official page; `[sec]`
taken from a named secondary source; `[der]` derived here, derivation stated.

## 1. What is measured and why it constrains cosmology

A redshift survey gives angular positions and redshifts. A fiducial cosmology
turns them into comoving coordinates, and the two-point function of the
resulting overdensity field is measured in redshift space. Four pieces of
information are extracted from it.

### 1.1 Baryon acoustic oscillations (standard ruler)

The sound horizon at the baryon drag epoch,

    r_d = ∫_{z_d}^∞ c_s(z) / H(z) dz ,   c_s = c / sqrt(3 (1 + 3ρ_b / 4ρ_γ)) ,

is imprinted as a preferred comoving separation. In the standard model the
drag epoch is at z_d ≈ 1060 [src], slightly later than photon decoupling at
z_* ≈ 1090 [src] (DESI Collaboration 2024, arXiv:2404.03002, Sect. 2.1). For
standard early-time physics DESI uses the approximation

    r_d = 147.05 (ω_m / 0.1432)^-0.23 (N_eff / 3.04)^-0.1 (ω_b / 0.02236)^-0.13 Mpc

[src] (arXiv:2404.03002, Sect. 2.1, with ω_m = Ω_m h² and ω_b = Ω_b h²). The
classical fitting formulae for z_d and the transfer function are those of
Eisenstein & Hu 1998, arXiv:astro-ph/9709112.

Transverse to the line of sight the ruler subtends Δθ and measures the
transverse comoving distance D_M(z) = r_d / Δθ. Along the line of sight it
spans Δz and measures the Hubble distance D_H(z) = c / H(z) = r_d / Δz. BAO
therefore constrain the dimensionless ratios D_M/r_d and D_H/r_d, never a
distance in Mpc and never H0 alone [src] (arXiv:2404.03002, Sect. 2.1). For
low signal-to-noise samples only the angle average is quoted,

    D_V(z) = (z D_M(z)² D_H(z))^(1/3)

[src] (arXiv:2404.03002, Sect. 2.1). The fitted quantities are dilation
parameters relative to the fiducial cosmology (DESI Collaboration 2025,
arXiv:2503.14738, BAO-measurement section) [src]:

    α_∥ = (D_H / r_d) / (D_H / r_d)^fid ,   α_⊥ = (D_M / r_d) / (D_M / r_d)^fid ,
    α_iso = (α_∥ α_⊥²)^(1/3) ,              α_AP = α_∥ / α_⊥ .

DESI samples the posterior in (α_iso, α_AP) because the two are less
correlated than (α_∥, α_⊥) [src] (arXiv:2503.14738). D_M/D_H is
inversely proportional to α_AP [src].

In flat ΛCDM, BAO alone constrain Ω_m and the product h r_d (equivalently
H0 r_d). H0 follows only after r_d is calibrated, by a BBN prior on ω_b, by
the CMB acoustic scale θ_*, or by the full CMB (arXiv:2503.14738).
The BBN prior in current use is Ω_b h² = 0.02218 ± 0.00055 [src] (Schöneberg
2024, arXiv:2401.15054); the DESI DR1 full-shape analysis used the projection
of the joint (ω_b, N_eff) constraint at N_eff = 3.044, ω_b = 0.02198 ± 0.00053
[src] (Adame et al. 2024, arXiv:2411.12021, Sect. 4.7).

### 1.2 Redshift-space distortions (growth)

Peculiar velocities displace galaxies along the line of sight. In linear
theory the redshift-space power spectrum is

    P_s(k, μ) = (b + f μ²)² P_m(k)

(Kaiser 1987, doi:10.1093/mnras/227.1.1), with f = d ln D / d ln a the growth
rate and μ the cosine of the angle to the line of sight. Because b σ8 and
f σ8 are the measured combinations, the growth observable is fσ8(z). In
general relativity f(z) ≈ Ω_m(z)^γ with γ = 0.55 [src] (arXiv:2411.12021,
Sect. 7.1). The pre-EFT generation of non-linear RSD templates is represented
by the TNS model, which adds the density–velocity coupling terms missing from
phenomenological Kaiser-times-damping forms (Taruya et al. 2010,
arXiv:1006.0699).

### 1.3 The Alcock–Paczynski effect

A wrong fiducial cosmology stretches separations differently along and across
the line of sight (Alcock & Paczynski 1979, doi:10.1038/281358a0). Any feature
of known intrinsic isotropy measures F_AP = D_M / D_H. BAO give it through
α_AP; full-shape fits give it from the whole anisotropic broadband, where it is
degenerate with RSD unless the RSD model is trusted. Ivanov et al. 2020
(arXiv:1909.05277) argue that the AP contribution is marginal in ΛCDM but
becomes important in non-minimal models.

### 1.4 Broadband shape

The turnover and slope of P(k) carry the matter–radiation equality scale
(Ω_m h, i.e. ω_m once h is fixed), the baryon fraction and n_s. The first
generation of analyses used it this way: 2dFGRS measured Ω_m h = 0.168 ± 0.016
and Ω_b/Ω_m = 0.185 ± 0.046 [src] (Cole et al. 2005, arXiv:astro-ph/0501174).
Modern analyses either fit the full power spectrum with a perturbative model
("full modelling") or compress the shape into one extra parameter (ShapeFit,
Sect. 3).

### 1.5 Scale-dependent bias from primordial non-Gaussianity (status only)

Local-type PNG adds a bias term growing as 1/k² on large scales (Dalal et al.
2008, arXiv:0710.4560; Slosar et al. 2008, arXiv:0805.3580). The amplitude is
proportional to f_NL b_φ, and b_φ is not measured by the two-point function:
the common assumption is b_φ = 2 δ_c (b_1 − p), with p = 1 for the universal
mass function and p = 1.6 for a recent-merger population, the usual choice
for quasars [src] (Barreira 2022, arXiv:2205.05673; Chaussidon et al. 2024,
arXiv:2411.17623; Brown et al. 2026, arXiv:2606.24651). Depending on the
assumed b_φ(b_1) relation, the same BOSS data give σ(f_NL) between 16 and 226
[src] (arXiv:2205.05673). Detail belongs to `cosmo-inflation-primordial`.

## 2. Estimators

### 2.1 Configuration space

The standard estimator is

    ξ(s, μ) = (DD − 2DR + RR) / RR

(Landy & Szalay 1993, doi:10.1086/172900), with D the data and R a random
catalogue sampling the selection function. After reconstruction the shifted
randoms S enter, ξ = (DD − 2DS + SS) / RR (Padmanabhan et al. 2012,
arXiv:1202.0090). DESI measures ξ(s, μ) with `pycorr`, a wrapper around a
modified Corrfunc pair counter, in bins of 4 h⁻¹ Mpc in s and 200 bins in μ
over [−1, 1], then projects onto Legendre multipoles; the BAO fit uses the
monopole and quadrupole [src] (arXiv:2503.14738).

### 2.2 Fourier space

The weighted overdensity field F(r) ∝ w(r) [n_g(r) − α n_r(r)] with weights
w = 1 / (1 + n̄(r) P_0) minimises the variance at the scale where P = P_0
(Feldman, Kaiser & Peacock 1994, arXiv:astro-ph/9304022). With a line of sight
that varies across the survey, the multipoles are estimated by assigning to
each pair the line of sight of one of its members (Yamamoto et al. 2006,
arXiv:astro-ph/0505115). That choice makes the estimator a sum of FFTs; the
spherical-harmonic implementation needs 2ℓ + 1 FFTs for multipole ℓ [src]
(Hand et al. 2017, arXiv:1704.02357).

The single-galaxy line of sight breaks pair symmetry and generates wide-angle
terms, including odd multipoles (dipole, octopole), which couple to the window
(Beutler, Castorina & Zhang 2019, arXiv:1810.05051).

### 2.3 Window function and integral constraints

The measured power spectrum is the true one convolved with the survey window.
Current practice is a window matrix W that maps theory multipoles to observed
ones, P_obs = W · P_theory, with wide-angle terms included (Beutler &
McDonald 2021, arXiv:2106.06324). The same paper shows that deconvolved
multipoles give the same BAO likelihood as the standard analysis for BOSS.

Because the mean density, and usually the radial selection function, are
measured from the data, the estimated overdensity integrates to zero over the
survey (global integral constraint) or along each line of sight shell (radial
integral constraint). The complete derivation, including shot-noise and
wide-angle terms, is de Mattia & Ruhlmann-Kleider 2019, arXiv:1904.08851.
Regressing the target density against imaging maps adds an angular integral
constraint, which DESI models as a correction to the window for its f_NL
analysis (arXiv:2411.17623).

### 2.4 Fibre-assignment weights

Missing targets are clustered. The unbiased correction weights each observed
pair by the inverse of its probability of being observed over many reruns of
the targeting algorithm (pairwise inverse probability, PIP), provided every
pair has non-zero probability (Bianchi & Percival 2017, arXiv:1703.02070);
pairs with zero probability are restored by angular up-weighting. The method
was applied to eBOSS down to about 0.1 h⁻¹ Mpc [src] (Mohammad et al. 2020,
arXiv:2007.09005). DESI DR1 chose a different route for its cosmology fits:
removing all pairs below 0.05° ("θ-cut") and propagating the cut into the
window [src] (Pinon et al. 2024, arXiv:2406.04804; arXiv:2411.12021,
Sect. 5.4). See `systematics.md`.

### 2.5 Reconstruction

Non-linear bulk flows smear the acoustic peak. Reconstruction estimates the
displacement field from the smoothed galaxy density and moves galaxies and
randoms back (Eisenstein et al. 2007, arXiv:astro-ph/0604362). Its first
application to data reduced the non-linear smoothing scale from 8.1 to
4.4 h⁻¹ Mpc and gave a 1.9% distance to z = 0.35 [src] (arXiv:1202.0090).
DESI uses the iterative FFT algorithm of Burden et al. 2015
(arXiv:1504.02591) as implemented in `pyrecon`, with settings fixed in
Paillas et al. 2024 (arXiv:2404.03005) [src] (arXiv:2503.14738).
Reconstruction also removes most of the small non-linear shift of the BAO
scale, which is below 0.3% before reconstruction [src] (arXiv:2404.03002,
Sect. 2.3). On Euclid-like mocks reconstruction raises the figure of merit on
{Ω_m, H0 r_s} by about 3 [src] (Euclid Collaboration: Sarpa et al. 2026,
arXiv:2605.03446).

Two developments of 2026: explicit field-level inference improves the BAO
parameters of DESI-like LRG mocks by 26% and a neural augmentation of standard
reconstruction by 35% relative to standard reconstruction [src] (Bayer et al.
2026, arXiv:2603.15732, mocks only); and overlapping tracers are merged into
one bias-weighted catalogue before reconstruction (Sanders et al. 2026,
arXiv:2608.27830).

## 3. Theory models in current analyses

| Model class | What is fitted | Range of validity as used | Reference |
|---|---|---|---|
| BAO template fit | α_iso, α_AP on a post-reconstruction ξ_0, ξ_2 with a spline broadband | s > s_min, with s_min = 60 h⁻¹ Mpc in DR2 and 50 in DR1 [src] | Chen et al. 2024, arXiv:2402.14070; arXiv:2503.14738 |
| Standard compression | α_∥, α_⊥, fσ8 with a fixed template | BOSS and eBOSS consensus results | Alam et al. 2017, arXiv:1607.03155 |
| ShapeFit | α_iso, α_AP, fσ_s8, slope m | same scales as full modelling | Brieden et al. 2021, arXiv:2106.07641 |
| Full modelling (EFT) | cosmological parameters directly, one-loop EFT with bias, counterterms, stochastic terms | DESI DR1: 0.02 < k < 0.20 h Mpc⁻¹, ℓ = 0, 2 [src] | arXiv:2411.12021 |

Only the lower scale cut of the DESI BAO fit was read this session; the upper
limit is not given here.

**EFT of large-scale structure.** The framework is that of Baumann et al.
2012 (arXiv:1004.2488) and Carrasco et al. 2012 (arXiv:1206.2926); the first
applications to BOSS were Ivanov et al. 2020 (arXiv:1909.05277) and D'Amico et
al. 2020 (arXiv:1909.05271). Reviews: Ivanov 2022 (arXiv:2212.08488) for the
EFT, Desjacques et al. 2018 (arXiv:1611.09787) for the bias expansion,
Weinberg et al. 2013 (arXiv:1201.2434) for BAO and RSD as dark-energy probes.

**DESI DR1 baseline** (arXiv:2411.12021, Sect. 4.7) [src]:

- model: `velocileptors` in its Eulerian (EPT) mode (Chen et al. 2021,
  arXiv:2012.04636), with LPT, FOLPS (Noriega et al. 2022, arXiv:2208.02791)
  and PyBird (D'Amico et al. 2021, arXiv:2003.07956) as cross-checks;
- bias basis (1 + b_1) σ8, b_2 σ8², b_s σ8², with b_3 = 0; flat prior on the
  first, wide Gaussian priors on the others; Gaussian priors on counterterms
  (α_0, α_2) and stochastic terms (SN_0, SN_2);
- monopole and quadrupole only: the hexadecapole was left out because it
  increases prior-weight effects for little gain;
- covariance from 1000 EZmocks, rescaled (Sect. 4);
- cosmological inference by full modelling, not ShapeFit, because projection
  effects bias the interpretation of compressed parameters in weak bins.

The three EFT codes agree to better than 0.1% in the parameters of interest
when given consistent settings [src] (arXiv:2411.12021, Sect. 5.1; Maus et al.
2024, arXiv:2404.07272). CLASS-PT (Chudaykin et al. 2020, arXiv:2004.10607)
is the code behind the independent "East-coast" analyses.

**ShapeFit.** The classic compression is extended by one parameter, the slope
m of the linear power spectrum at a pivot, which captures the shape
information that full modelling uses, in a model-independent way
(arXiv:2106.07641). The growth parameter it returns is fσ_s8, the amplitude
at 8 h⁻¹ Mpc in the template units; it equals fσ8 only if r_d = r_d^fid
[src] (arXiv:2411.12021, Sect. 7.1). DESI states that its fσ8 values "should
only serve for visualization purposes" and that cosmology must use fσ_s8
[src].

**Where the community is split.**

1. Priors on EFT nuisance parameters. PyBird ("West-coast") and CLASS-PT
   ("East-coast") priors gave BOSS results differing at the 1σ level from the
   same data; posterior means move from the best fit by up to 1σ and 2σ
   respectively [src] (Simon et al. 2023, arXiv:2208.05929).
2. Bayesian or frequentist. Profile likelihoods are prior-independent; for
   BOSS the posterior mean is shifted from the maximum-likelihood point by up
   to 1.0σ and frequentist intervals are up to 1.9 times wider [src] (Holm et
   al. 2023, arXiv:2309.04468). DESI published its own frequentist analysis
   (Morawetz et al. 2025, arXiv:2508.11811).
3. Informative priors from the galaxy–halo connection: HOD-informed priors
   (Zhang et al. 2025, arXiv:2504.10407) and simulation-based priors
   (Chudaykin et al. 2026, arXiv:2602.18554) tighten constraints but import
   HOD assumptions.
4. Compression or full modelling. DESI DR1 chose full modelling; the 2026
   DR1 FS + DR2 BAO analysis chose ShapeFit precisely because it removes
   prior-volume effects (Forero-Sánchez et al. 2026, arXiv:2602.18761).
5. Configuration or Fourier space; mock or analytic covariance (Sect. 4).

## 4. Covariance and likelihood

**Mock-based.** The sample covariance of N_obs approximate mocks. DESI uses
EZmocks (Chuang et al. 2015, arXiv:1409.1124), 1000 realisations for the DR1
full-shape power spectrum [src] (arXiv:2411.12021, Sect. 5.8). High-accuracy
N-body mocks (25 AbacusSummit boxes; Maksimova et al. 2021, arXiv:2110.11398)
validate the model, not the covariance.

**Corrections for a noisy covariance.** The inverse of a sample covariance is
biased; the unbiased estimator multiplies it by

    (N_obs − N_bins − 2) / (N_obs − 1)

(Hartlap et al. 2007, arXiv:astro-ph/0608064). The propagation of the
covariance noise to parameter errors adds a further factor (Percival et al.
2014, arXiv:1312.4841): even 600 mocks can inflate errors by about 20% [src].
The exact treatment marginalises over the true covariance and gives a
multivariate t-distribution (Sellentin & Heavens 2016, arXiv:1511.05969).
DESI DR1 applied Hartlap and Percival factors and kept a Gaussian likelihood
[src] (arXiv:2411.12021, Sect. 5.8).

**Analytic.** For the correlation function, RascalC computes the disconnected
four-point term with survey geometry and calibrates a shot-noise rescaling on
jackknife to mimic non-Gaussian terms (Philcox et al. 2020, arXiv:1904.11070);
on DESI DR1 mocks the projected BAO errors agree with mock covariances to
within 8% [src] (Rashkovetskyi et al. 2024, arXiv:2404.03007). It is the
fiducial covariance of the DESI DR1 and DR2 BAO analyses [src]
(arXiv:2503.14738). For the power spectrum the perturbative calculation is
Wadekar & Scoccimarro 2020 (arXiv:1910.02914); in DESI DR1 the Fourier-space
analytic covariance did not reproduce the mock results for full-shape fits,
which motivated a corrected mock covariance [src] (Forero-Sánchez et al.
2024, arXiv:2411.12027).

**Joint pre- and post-reconstruction.** Combining full shape with
post-reconstruction BAO needs their cross-covariance. DESI DR1 took it from
EZmocks [src] (arXiv:2411.12021). An analytic approximation now exists and
shows the cross-covariance is small enough that approximate treatments
suffice [src] (Maus et al. 2026, arXiv:2602.12343).

**Likelihood for BAO.** DESI publishes a Gaussian likelihood in
(D_M/r_d, D_H/r_d), or D_V/r_d alone, per redshift bin, with the correlation
coefficient within a bin and no correlation between bins; systematic errors
are added in quadrature [src] (arXiv:2404.03002, Sect. 2.3.2).

**Systematics in the full-shape likelihood.** DESI DR1 adds systematic
covariance terms at the power-spectrum level (HOD plus prior-weight term,
imaging template, window-rotation parameter), so that they propagate to any
model [src] (arXiv:2411.12021, Sect. 5.8).

## 5. Blinding

Catalogue-level blinding shifts galaxy positions along the line of sight in
two steps: a geometric shift mimicking an AP distortion and a perturbative
shift mimicking RSD; angular positions are untouched, so angular systematics
tests remain valid (Brieden et al. 2020, arXiv:2006.10857). DESI adds weights
that blind the f_NL signal and validated the scheme on mocks and with a second
blinding layer on data (Andrade et al. 2024, arXiv:2404.07282). The DESI DR1
BAO, DR1 full-shape and DR1 f_NL analyses were all blinded at catalogue level
[src] (DESI Collaboration 2024, arXiv:2404.03000; arXiv:2411.12021;
arXiv:2411.17623). For DR2 the same prescription was reused with a new seed,
and the true catalogues were first processed in December 2024 [src]
(arXiv:2503.14738).

A referee expects, before unblinding: fixed scale cuts and priors, a frozen
systematic budget, mock-recovery tests, and data-split consistency on the
blinded catalogue. DESI DR2 changed s_min from 50 to 60 h⁻¹ Mpc on blinded
data after seeing large χ² values, and documented it [src] (arXiv:2503.14738;
Andrade et al. 2025, arXiv:2503.14742).

## 6. Public codes and pipelines

| Code | Role | Reference |
|---|---|---|
| pycorr | pair counts and ξ multipoles (DESI) | named in arXiv:2503.14738; no paper found |
| pyrecon | reconstruction (IterativeFFT, others) | named in arXiv:2503.14738; algorithm arXiv:1504.02591 |
| RascalC | semi-analytic 2PCF covariance | arXiv:1904.11070; arXiv:2404.03007 |
| velocileptors | one-loop LPT and EPT with EFT terms | arXiv:2012.04636 |
| FOLPS | one-loop EFT with massive-neutrino kernels | arXiv:2208.02791 |
| PyBird | one-loop EFT, West-coast basis | arXiv:2003.07956 |
| CLASS-PT | one-loop EFT inside CLASS, East-coast basis | arXiv:2004.10607 |
| desilike | DESI likelihood and inference framework | named in arXiv:2411.12021; no paper found |
| EZmocks | fast mocks for covariance | arXiv:1409.1124 |
| AbacusSummit | N-body suite for validation | arXiv:2110.11398 |
| AbacusHOD | multi-tracer HOD on AbacusSummit | Yuan et al. 2022, arXiv:2110.11412 |

API-level detail belongs to `cosmo-software-ecosystem`.

## 7. Halo occupation and bias, at analysis level

Mocks are populated with a halo occupation distribution that separates
centrals and satellites (Zheng et al. 2005, arXiv:astro-ph/0408564). DESI
systematics tests vary the HOD around a fit to early data: for LRGs a
5-parameter base model plus incompleteness, velocity bias, assembly bias and
satellite-profile parameters (Mena-Fernández et al. 2024, arXiv:2404.03008);
for ELGs variants with galactic conformity and assembly bias
(Garcia-Quintero et al. 2024, arXiv:2404.03009). In the fits themselves no
HOD is assumed: the perturbative bias expansion (arXiv:1611.09787) absorbs
it, at the price of the nuisance parameters discussed in Sect. 3.

## 8. Conventions and units specific to the domain

- Distances and wavenumbers are in h⁻¹ Mpc and h Mpc⁻¹ in the fiducial
  cosmology; published BAO results are dimensionless ratios to r_d.
- DESI fiducial cosmology: ω_b = 0.02237, ω_cdm = 0.1200, h = 0.6736,
  10⁹ A_s = 2.0830, n_s = 0.9649 [src] (arXiv:2411.12021, Sect. 5.3; the
  AbacusSummit base cosmology).
- r_d, r_s(z_d) and r_drag are the same quantity in different papers.
  Older papers quote r_s/D_V; newer ones D_V/r_d.
- D_V: the DESI form (z D_M² D_H)^(1/3) and the older
  [(1+z)² D_A² c z / H]^(1/3) are identical because D_M = (1+z) D_A and
  D_H = c/H [der].
- "D_A" in BOSS-era papers is sometimes the comoving angular diameter
  distance D_M; check the definition before comparing.
- fσ8 versus fσ_s8 (Sect. 3).
- z_eff is a convention; DESI defines it in arXiv:2404.03000, and
  small changes are inconsequential if the α-to-distance conversion is done
  at the same redshift [src] (arXiv:2503.14738).
- "DESI" in a DR2-era parameter table means BAO only; "DESI (FS+BAO)" is the
  DR1 full-shape combination. The two are not the same dataset.
- Sample counts differ between analyses of the same release: DR1 BAO used
  over 5.7 million redshifts, DR1 full shape over 4.7 million, [src]
  (arXiv:2404.03000; arXiv:2411.12021). The full-shape fit uses six bins
  (BGS, LRG1, LRG2, LRG3, ELG2, QSO) and has no 0.8 < z < 1.1 ELG bin [src];
  that this accounts for the difference in counts is an inference [der].

## Not verified

- The upper scale limit of the DESI BAO fit and the reconstruction smoothing
  scales per tracer.
- Reference papers for pycorr, pypower, pyrecon and desilike (none found;
  the DESI papers cite repositories).
- The FKP P_0 values adopted per DESI tracer.
