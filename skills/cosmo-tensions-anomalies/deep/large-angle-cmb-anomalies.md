# Large-angle CMB anomalies — cosmo-tensions-anomalies dossier

Scope: how the hemispherical asymmetry (dipolar modulation and local
variance), the Cold Spot and the low-multipole alignments are measured
anomaly by anomaly — estimators, smoothing kernels, masks, constrained
simulations, profile and lensing tests — what the mask and kernel choices
do to each significance, and which physical models were fitted and how
they were tested.
Snapshot: 2026-10-18.
From: CosmoVerse white paper (arXiv:2504.01669), Sects. 2.3.3, 2.3.9.d;
Abdalla et al. 2022 (arXiv:2203.06142), Sect. VIII.3; Planck isotropy and
statistics papers (arXiv:1906.02552).

Already in L2 or in the sister dossier, not repeated here: the definitions
of S_1/2, R^TT, σ²_16 and S_QO and the table of anomalies
(`physics-and-methods.md#large-angle-cmb-anomalies`); published p-values,
PR4 status and the supervoid odds (`results.md#large-angle-cmb-anomalies`);
mundane explanations (`systematics.md#large-angle-cmb-anomalies`); the
dispute (`open-questions.md#large-angle-cmb-anomalies-evidence-or-flukes`).
`deep/anomaly-significance.md` holds the null ensemble, tail conventions,
the ℓ_max and angle scans, the joint counting, the look-elsewhere
correction over statistics and the general polarisation tests; this file
holds what is specific to each anomaly.

Notation. T(ê) is the temperature in direction ê; a dipolar modulation is
T(ê) = T_0(ê)[1 + A ê·d̂], with A the amplitude and d̂ the direction
(Schwarz et al. 2016, arXiv:1510.07929, Eq. 9). (l, b) are Galactic
coordinates. C_ℓ is the angular power, and C_ℓℓ′ an off-diagonal element of
the multipole covariance. R is a smoothing (wavelet or Gaussian) scale.
"Common mask" is the Planck 2018 temperature mask, about 26% of the sky
(arXiv:2509.03720, Sect. IV).

## How it is done
<!-- key: how-it-is-done -->

### Hemispherical asymmetry I: dipolar modulation in multipole space
<!-- key: hemispherical-asymmetry-i-dipolar-modulation-in -->

A dipolar modulation couples ℓ to ℓ ± 1. Planck 2018 uses a quadratic
maximum-likelihood (QML) estimator for the modulation multipoles
[src: arXiv:1906.02552, Sect. 7.2, Eqs. 54–58]:

X̃_0^WZ = 6 Σ_ℓm δC_ℓℓ+1^WZ A_ℓm S_ℓm,ℓ+1,m+M^(WZ) / Σ_ℓ (δC_ℓℓ+1^WZ)² (ℓ+1)
F_ℓ^(W F_ℓ+1^Z), with S_ℓmℓ′m′^WZ ≡ W*_ℓm Z_ℓ′m′ − ⟨W*_ℓm Z_ℓ′m′⟩
(the second term is the mean-field correction), A_ℓm and B_ℓm the coupling
coefficients of Eqs. 57–58, W, Z ∈ {T, E} inverse-covariance filtered, and
δC_ℓℓ′ = 2(C_ℓ + C_ℓ′) for a scale-invariant modulation to ℓ_max.

Amplitude and direction follow as Ã = sqrt(ΔX̃_0² + 2|ΔX̃_1|²) [src: Eq. 59]
and Eqs. 60–61. TT, TE and EE are combined by inverse-variance weighting
(Eq. 62), with variances from the scatter of the FFP10 simulations, which
"agree closely with the Fisher errors" [src: Sect. 7.2].

What it gives [src: Tables 24–25]:

| Data | ℓ range | A | (l, b) |
|---|---|---|---|
| 2015 TT, four maps | 2–64 | 0.062–0.064 (+0.025–0.027 / −0.013) | (209–213, −25 to −26) ± 28° |
| 2018 TT, four maps | 2–64 | 0.069–0.070 (+0.032 / −0.015) | (221, −22 to −24) ± 31° |
| 2018 EE alone | 2–64 | 0.066–0.137 with errors of order +0.9 / −0.5 | directions ± 103–108° |
| 2018 TT, TE, EE | 2–64 | 0.068–0.072 (+0.031–0.032 / −0.015) | (218–225, −17 to −23) ± 29–31° |
| 2018 TT, TE, EE | 2–220 | 0.022–0.023 (+0.008 / −0.004) | (220–228, −2 to −5) ± 25–26° |

Reading rules stated with the tables: the expectation for noise-free
Gaussian skies is "approximately 3%"; the typical amplitude of an isotropic
sky falls as 1/ℓ_max, so the smaller value to ℓ = 220 is what isotropy
predicts; ℓ = 2–220 is quoted because it has the lowest p-value, and the
cumulative statistic makes "apparent trends in the curves ... misleading"
[src: Sect. 7.2, Fig. 34 caption]. Polarisation "on [its] own show[s] no
evidence of modulation" [src: Table 24 caption]. The earlier Planck 2015
Commander value, A = 0.066 ± 0.021 towards (230°, −16°) ± 24°, with most
signal at ℓ ∈ [2, 67] and p = 1% there, is quoted by Schwarz et al.
[src: arXiv:1510.07929, Sect. 2.3].

Why the TT + EE combination is only phenomenological: "modulated
fluctuations that exhibit a 7% dipolar asymmetry in T to ℓ ≈ 65 are not
expected to produce an E-mode asymmetry of the same amplitude and over the
same scales", so the combined ℓ-space model "has no physical basis"; a
k-space model is needed [src: arXiv:1906.02552, Sect. 7.2]. An isotropic
polarisation signal added to a ≈ 3σ temperature signal raises the combined
significance by chance "with 30% probability for Planck" [src: Sect. 7.2].
The τ mismatch between data and simulations changes the amplitude by at
most about 1% [src: Sect. 7.2].

### Hemispherical asymmetry II: local variance
<!-- key: hemispherical-asymmetry-ii-local-variance -->

The local-variance estimator (Planck 2018, after Akrami et al. 2014)
[src: arXiv:1906.02552, Sect. 7.1]: discs of radius r_disc centred on the
pixels of an N_side = 16 map; monopole and dipole removed from the masked
map; variance of the unmasked pixels in each disc; the simulation-mean
variance map subtracted; a dipole fitted with each pixel weighted by the
inverse variance of the simulated variances; only discs more than 10%
unmasked are used. Disc radii below 4° are not used, so that the N_side =
16 centres cover the sky.

The same estimator written out by Herold et al. 2025 (arXiv:2509.03720)
[src: Sect. III.5, Eqs. 13–15]: σ²_θ(n̂) = (1/N) Σ_{i ∈ D_θ(n̂)} [T(n̂_i) −
T̄_θ(n̂)]², normalised as σ̃²_θ = (w̄/w)(σ²_θ − μ)/μ with μ the mean over
10⁵ simulations and w their fractional variance; θ = 8°, "a common choice
in the literature since it gives comparatively significant results"; an
output pixel is masked if more than 90% of its pixels are masked.

Results:

- Planck 2018 full resolution: p < 0.1% for 4°, 6° and 8° discs (no
  simulation exceeds the data), rising to 0.1% (10°), 0.8% (16°) and
  1.3–2.0% (20°) across the four maps [src: arXiv:1906.02552, Table 21].
- The definition matters: with the variance taken about the full-sky or
  cut-sky mean instead of the disc mean, the data agree with isotropic
  ΛCDM "with PTE of the order of tens of percent" [src: arXiv:2509.03720,
  Sect. III.5].
- The mask matters: A_LV has p = 0.13–0.16% (3.2σ) with the common mask and
  p = 2.2–2.8% (2.2–2.3σ) with the 1% mask [src: arXiv:2509.03720, Sect. IV].
- Frequency and scale: in seven cleaned single-frequency maps from Planck
  PR4 and WMAP 9, with a power-law (scale-dependent) modulation, the
  dipolar modulation is present in all cases with consistent direction;
  the authors read this as against an instrumental origin (Sanyal, Aluri
  & Shafieloo 2026, arXiv:2601.13830) [src: abstract].

### Hemispherical asymmetry III: E-mode tests at Planck noise
<!-- key: hemispherical-asymmetry-iii-e-mode-tests-at -->

Local bandpowers in overlapping patches, E-to-B leakage corrected by
pseudo-C_ℓ deconvolution, dipole directions fitted separately to the two
half-mission maps (same sky, independent noise): for Planck PR3 Commander
at ℓ = 15–40 the two directions are 8.7° apart, closer than in any of 300
isotropic simulations (p < 0.33%), and near the temperature axis; the
coherence appears only in EE and vanishes without the leakage correction
(Lynch 2026, arXiv:2607.28774) [src: abstract]. The test establishes a
CMB-level signal but "cannot distinguish a real modulation from a chance CMB
fluctuation" [src: abstract].

### The Cold Spot
<!-- key: the-cold-spot -->

Detection. Spherical Mexican-hat wavelet (SMHW) coefficients of WMAP
first-year data showed an excess of kurtosis at scales around 5°, with a
p-value of about 1% against Gaussian simulations, traced to a spot at (b,
l) = (−57°, 209°) (Cruz, Martínez-González & Vielva 2009, arXiv:0901.1986)
[src: abstract]. The kurtosis excess was at R = 300′; accounting for the
statistics tried with wavelets that did not return an anomaly gives 1.85%
(as summarised in arXiv:1510.07929, Sect. 2.5) [src]. The SMHW
coefficient at scale R equals the Laplacian of the map smoothed with a
Gaussian of that scale (arXiv:1906.02552, Sect. 6.5, note 12) [src], which
is why later work characterises the spot by its curvature.

Kernel dependence. Repeating the coldest-spot search with top-hat discs and
Gaussian weights of varying width finds "no significant signal at any
scale"; the authors trace the SMHW significance to the fact that the spot's
profile "just happens to favor the particular profile given by the
wavelet", and a statistic that takes the most significant of several
kernels, scales and statistics is also null (Zhang & Huterer 2010,
arXiv:0908.3988) [src: abstract].

Mask dependence. With 100,000 simulated skies, cut and full: the Cold Spot
is the full-sky temperature minimum with 94% probability; about 48% of
full-sky minima fall under the mask; a cut-sky comparison gives about 2.2σ
at R = 5°, a comparison with full-sky minima about 1.9σ and below 2σ for
every R (Naidoo, Benoit-Lévy & Lahav 2017, arXiv:1703.07894) [src:
abstract]. The ΛCDM ISW contribution along the line of sight is on average
about 10% of the profile, about 10 μK and consistent with zero [src:
abstract].

Profile and polarisation test (Planck 2018) [src: arXiv:1906.02552, Sect.
6.5]:

1. Define the Cold Spot as a minimum of the map smoothed with a Gaussian of
   R = 5°; four other large-scale peaks at R = 10°.
2. Average T and the radial Stokes parameter Q_r over azimuth in 1° rings;
   the profile depends only on the peak height and Laplacian.
3. Predict the mean profile analytically, conditional on those two
   quantities; for the masked covariance, generate 2000 simulations
   constrained to have a peak at the same position.
4. Fit an amplitude A = Σ X̂_i C⁻¹_ij X_j / Σ X_i C⁻¹_ij X_j, with σ_A =
   (Σ X_i C⁻¹_ij X_j)^(−1/2) [src: Eqs. 51–52], to angles up to 60°.

Result: Cold Spot T amplitude 1.005 ± 0.003 in all four maps; Q_r
amplitudes −0.598 to +0.152 with errors 0.95–1.04, S/N about 1, "the
polarization signal of the peaks cannot be detected" and all amplitudes are
consistent with ΛCDM [src: Table 20, Sect. 6.5].

Supervoid test with lensing (Owusu et al. 2023, arXiv:2211.16139):

- Void model: LTB curvature k(r) = k_0 exp[−½(r/r_V)²] [src: Eq. 5],
  chosen because it fits the Cold Spot temperature profile; potential
  integrated to r_L = 4.2 r_V (99% of the void mass); linear growth for the
  ΛCDM time dependence [src: Sect. 2.1, Eqs. 4–7].
- Temperature path: Planck 2018 SMICA and NILC rotated to put the spot at
  the pole, mean ΔT in 12 rings of 2° [src: Sect. 4.2].
- Lensing path: off-diagonal ℓ, ℓ + Δℓ correlations; about 53,000
  end-to-end simulations over a grid of 1550 (Θ_0, θ_V) pairs with the void
  painted in, bias removal by random-forest regression, checked on 10,000
  further and 6000 null simulations; repeated for 112 directions within
  5.5° [src: Sect. 4.2].
- Priors: θ_V ≤ 10.1° (computational), D_V + 3 r_V ≤ D_SLS, −1 ≤ δ_0 ≤ 0
  [src: Sect. 5].
- Result: temperature best fit δ_0 = −0.34, r_V = 806 h⁻¹Mpc, D_V = 6910
  h⁻¹Mpc (z ≳ 1, poorly covered by galaxy catalogues), for which the
  expected lensing S/N is about 12 with ℓ_max = 1600 and Δℓ ≤ 40; lensing is
  consistent with no void, and the 2σ regions of temperature and lensing do
  not overlap in 3D [src: Sect. 5].

The local supervoid (Kovács et al. 2022, arXiv:2112.07699) [src: abstract]:
DES Y3 redMaGiC confirms the Eridanus supervoid at z < 0.2 in the Cold Spot
direction, and it is the most prominent large-scale underdensity in the DES
Y3 lensing mass maps (S/N ≳ 5); in ΛCDM its ISW imprint accounts for about
10–20% of the temperature depression; its lensing signal at the spot centre
is about 30% below similar peaks in N-body simulations with Ω_m = 0.279, σ8
= 0.82; supervoids of R ≳ 100 h⁻¹Mpc elsewhere show A_ISW ≈ 5.2 ± 1.6 (the
ratio of measured to ΛCDM ISW). The authors "report no significant
anomalies".

### Low-multipole alignments
<!-- key: low-multipole-alignments -->

Multipole vectors represent multipole ℓ by ℓ unit vectors and an amplitude;
the oriented areas w^(ℓ;i,j) = v̂^(ℓ;i) × v̂^(ℓ;j) [src: arXiv:1510.07929,
Eq. 7] enter S = (1/n) Σ_j |w_j · ê| [src: Eq. 8], with ê either the
quadrupole area vector (quadrupole–octopole alignment) or a fixed direction
(ecliptic pole, Galactic pole, CMB dipole) with n = 4 area vectors.

WMAP and Planck 2013 p-values [src: Sect. 2.2]: quadrupole–octopole
alignment 0.2–2% by map; joint perpendicularity to the ecliptic 2–4%, to the
Galactic pole 0.8–1.6%; alignment with the dipole direction 0.09–0.37%. The
kinetic quadrupole from our motion must be subtracted first; the test needs
full-sky maps, whose phases depend on the cleaning, the beam treatment and
the scan strategy [src: Sect. 2.2]. On the 2025 foreground-cleaned maps,
S_QO has p = 0.05–0.13% (3.2σ–3.5σ), the same full sky and with a 1% mask
[src: arXiv:2509.03720, Sect. IV]. The plane maximising the hemispherical
power asymmetry is close to the ecliptic, which "motivates both systematic
and cosmological proposals", none convincing [src: arXiv:1510.07929, Sect.
2.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Mask size
<!-- key: mask-size -->

Herold et al. (arXiv:2509.03720) [src: Sect. IV] clean WMAP and Planck at
70, 94, 100 and 143 GHz with six archival foreground templates fitted with
free normalisation, which allows a mask of 1% of the sky [src: Sect. II.1];
their stated advantage is that "the smaller mask maintains approximate
orthogonality of the a_ℓm of different ℓ" [src: Sect. IV]:

| Statistic | Common mask (26%) | 1% mask | Effect |
|---|---|---|---|
| S_1/2 | p = 0.19–0.24%, 3.0σ–3.1σ | p = 5.8–7.3%, 1.8σ–1.9σ | notable |
| R^27 (parity) | p = 2.8–5.9%, 1.9σ–2.2σ, all cuts | same | mild; ℓ_max = 27 chosen to maximise it |
| S_QO | — | p = 0.05–0.13%, 3.2σ–3.5σ (full sky agrees) | none |
| σ²_16 | p = 0.14–0.17%, 3.1σ–3.2σ | p = 0.34–0.40%, 2.9σ | mild |
| A_LV (8° discs) | p = 0.13–0.16%, 3.2σ | p = 2.2–2.8%, 2.2σ–2.3σ | notable |

Cost: a 1% mask relies on the low-resolution cleaning; Commander and SEVEM
without the common mask, and the 94 GHz map with the 1% mask, give
local-variance dipoles pointing to the Galactic plane and are excluded as
foreground-contaminated [src: Sect. III.5]. Their conclusion: an
alternative model would have to explain several anomalies, or another
measurement, to be "convincingly favored" [src: abstract].

### Cold Spot kernel and comparison ensemble
<!-- key: cold-spot-kernel-and-comparison-ensemble -->

| Choice | Significance | Source |
|---|---|---|
| SMHW kurtosis at R ≈ 5° | p ≈ 1% | arXiv:0901.1986 [src: abstract] |
| Same, after the wavelet statistics tried | 1.85% | as quoted in arXiv:1510.07929 [src: Sect. 2.5] |
| Top-hat discs and Gaussians, any scale | no significant signal | arXiv:0908.3988 [src: abstract] |
| SMHW, cut-sky minima | ≈ 2.2σ at R = 5° | arXiv:1703.07894 [src: abstract] |
| SMHW, full-sky minima | ≈ 1.9σ; < 2σ for all R | arXiv:1703.07894 [src: abstract] |

What the comparison of kernels shows: the significance belongs to the match
between the spot's profile and the kernel, so the kernel is a parameter of
the a posteriori choice, like the angle in S_1/2.

### Multipole-space or k-space modulation
<!-- key: multipole-space-or-k-space-modulation -->

The ℓ-space QML is fast and model-agnostic within temperature but cannot
predict polarisation; a k-space model is needed for a falsifiable E-mode
prediction (arXiv:1906.02552, Sect. 7.2; arXiv:1807.06211, Sect. 10.1.2)
[src]. Planck X fits the model to temperature, predicts polarisation, and
compares the likelihood ratio with simulations (next section).

## Physical models and how they were tested
<!-- key: physical-models-and-how-they-were-tested -->

Dipolar modulation, curvaton (Planck 2018 X, arXiv:1807.06211, Sect.
10.1.1) [src]: a gradient in a background curvaton field modulates a
fraction ξ of the adiabatic modes and produces cold-dark-matter isocurvature
with coupling κ, β_iso = 9κ²ξ/(1 + 9κ²ξ) [src: Eq. 105]. The asymmetry
alone prefers ξ > 0; the isotropic isocurvature limit from TT, TE, EE +
lowE + lensing overlaps it only weakly, and the joint fit shows "no reason
to prefer this model over base ΛCDM" [src: Sect. 10.1.1, Fig. 48].

Dipolar modulation, adiabatic with a long mode [src: Sect. 10.1.2]: a part
of the curvature perturbation is linearly modulated, R̃^lo(x) =
R^lo(x)(1 + A x·d̂/r_LS) [Eq. 106], which adds δC_ℓℓ′/2 Σ_M ΔX_M ξ^M to the
covariance [Eqs. 107–109]. Three spectra are tried: a red power law with
pivot k_0^lo = 1.5 × 10⁻⁴ Mpc⁻¹ [Eq. 110], a tanh cutoff [Eq. 111] and a
gradient in n_s [Eq. 112]; the estimator is Eq. 113 with cosmic variance
σ_X² = 12 [Σ_ℓ (ℓ+1) δC²_ℓℓ+1/(C_ℓ C_ℓ+1)]⁻¹ [Eq. 114]. The test statistic
Ô_j0 (maximum-likelihood ratio, model to ΛCDM) on SMICA polarisation gives
p = 43%, 30% and 57% against 300 isotropic polarisation simulations: "the
data do not help to decide" [src: Fig. 49 and text]. Such models need a
large bispectrum and "appear to require fine tuning" [src: Sect. 10.1.2].

Other routes, as reviewed in arXiv:1510.07929 [src: Sects. 4.4, 4.5]:

- An adiabatic superhorizon gradient cannot produce the asymmetry, because
  its intrinsic dipole is cancelled by the Doppler dipole it induces; an
  isocurvature gradient could, and would also show in large-scale
  structure, where quasar and galaxy distributions show none.
- Anisotropic inflation, P(k) = P(k)[1 + g_*(k·d̂)²] [Eq. 12]: a first ∼ 9σ
  detection came from asymmetric beams; Planck-based g_* = 0.002 ± 0.016
  (68%).
- Non-Gaussianity of a superhorizon mode can mimic a preferred direction,
  "trading" isotropy for f_NL.
- Topology: circles-in-the-sky searches exclude a non-trivial loop shorter
  than 98.5% of the last-scattering diameter; every route "could explain at
  least one 'anomaly atom'" but none is detected, and each has a
  coincidence problem. A 2026 review finds no definitive evidence, current
  constraints excluding "only some topologies, parameter ranges, and
  observer positions", with signals possibly detectable even beyond the
  size of the visible Universe (Copi et al. 2026, arXiv:2606.24886) [src:
  abstract].

Cold Spot: a collapsing cosmic texture was the most probable hypothesis in
a Bayesian template fit to WMAP (arXiv:0901.1986) [src: abstract]; a
supervoid is excluded by lensing (above); the local Eridanus void supplies
10–20% (arXiv:2112.07699) [src: abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Modulation amplitude for isotropic skies | ≈ 3% | Planck 2018 | arXiv:1906.02552 | Sect. 7.2 |
| A, 2018 TT, ℓ = 2–64 | 0.070 (+0.032/−0.015), (221°, −22°) ± 31° (Commander) | Planck 2018 | arXiv:1906.02552 | Table 24 |
| A, TT+TE+EE, ℓ = 2–220 | 0.022–0.023 (+0.008/−0.004) | Planck 2018 | arXiv:1906.02552 | Table 25 |
| Chance boost from isotropic polarisation | 30% for a 3σ T signal | Planck | arXiv:1906.02552 | Sect. 7.2 |
| Local-variance disc radii | 4°–20° (full res.), 4°–90° (N_side 64) | Planck 2018 | arXiv:1906.02552 | Sect. 7.1 |
| Local-variance p, 4°–8° | < 0.1% | Planck 2018 | arXiv:1906.02552 | Table 21 |
| Simulations for A_LV | 10⁵, 8° discs | Herold et al. | arXiv:2509.03720 | Sect. III.5 |
| E-mode half-mission direction offset | 8.7°, p < 0.33% (300 sims), ℓ = 15–40 | Lynch | arXiv:2607.28774 | abstract |
| Cold Spot centre | (l, b) = (209°, −57°) | WMAP | arXiv:0901.1986 | abstract |
| Cold Spot T profile amplitude | 1.005 ± 0.003 | Planck 2018 | arXiv:1906.02552 | Table 20 |
| Cold Spot Q_r amplitude | −0.232 ± 0.951 (Commander) | Planck 2018 | arXiv:1906.02552 | Table 20 |
| Constrained simulations for profiles | 2000 | Planck 2018 | arXiv:1906.02552 | Sect. 6.5 |
| Supervoid fit to temperature | δ_0 = −0.34, r_V = 806, D_V = 6910 h⁻¹Mpc | Owusu et al. | arXiv:2211.16139 | Sect. 5 |
| Expected lensing S/N of that void | ≈ 12 | Owusu et al. | arXiv:2211.16139 | Sect. 5 |
| Eridanus ISW share | 10–20% | DES | arXiv:2112.07699 | abstract |
| Anisotropic-inflation g_* | 0.002 ± 0.016 (68%) | Planck-based | arXiv:1510.07929 | Sect. 4.4 |
| Topology loop bound | > 98.5% of the LSS diameter | circles in the sky | arXiv:1510.07929 | Sect. 4.5 |
| Adiabatic-model polarisation p-values | 43%, 30%, 57% | Planck 2018 X | arXiv:1807.06211 | Sect. 10.1.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- Quoting the modulation amplitude without ℓ_max. A = 0.07 to ℓ = 64 and
  0.022 to ℓ = 220 are the same sky; the isotropic expectation falls as
  1/ℓ_max. Test: quote ℓ range, the 3% isotropic expectation and the
  scanned p-value with its look-elsewhere correction (see
  `deep/anomaly-significance.md`, Step 4).
- Reading a combined T + E p-value dip as confirmation: 30% chance for a
  3σ temperature signal (arXiv:1906.02552, Sect. 7.2). Test: predict E from
  a k-space model fitted to T, as in arXiv:1807.06211, Sect. 10.1.2.
- Mask-driven significance: S_1/2 and A_LV lose about 1σ when the mask
  shrinks from 26% to 1% (arXiv:2509.03720). Test: repeat with the smallest
  mask the cleaning allows, and check that the fitted direction does not
  move to the Galactic plane.
- Statistic definition: the local variance about the disc mean is
  anomalous, about the global mean it is not (arXiv:2509.03720, Sect.
  III.5). State the definition.
- Kernel chosen after seeing the spot: SMHW against discs (arXiv:0908.3988).
  Test: report the result for several kernels or a statistic that
  maximises over them, with its global p-value.
- Cut-sky minima as the null for a feature that is not masked
  (arXiv:1703.07894). Test: compare with full-sky minima.
- An E-mode coherence that disappears without leakage correction or appears
  in one map split only (arXiv:2607.28774). Test: half-mission
  cross-checks and EE against BB.
- Inferring a supervoid from the temperature profile alone: the fit
  prefers z ≳ 1 voids that lensing rules out (arXiv:2211.16139). Test:
  lensing and galaxy counts in the same direction.
- Alignment p-values on maps whose phases changed with cleaning: subtract
  the kinetic quadrupole and compare several full-sky cleanings
  (arXiv:1510.07929, Sect. 2.2).

## Reading list
<!-- key: reading-list -->

- Foundation and practice: Planck 2018 VII, arXiv:1906.02552 — Sects. 6.5
  (Cold Spot profiles), 7.1 (local variance), 7.2 (QML modulation).
- Models: Planck 2018 X, arXiv:1807.06211 — Sect. 10.1 (curvaton and
  adiabatic modulation models, polarisation test).
- Review, one side: Schwarz et al. 2016, arXiv:1510.07929 — Sects. 2.2,
  2.3, 2.5, 4.4, 4.5.
- Masks and cleaning: Herold et al. 2025, arXiv:2509.03720 — five
  statistics with a 1% mask.
- Critique of the Cold Spot: Zhang & Huterer 2010, arXiv:0908.3988;
  Naidoo, Benoit-Lévy & Lahav 2017, arXiv:1703.07894.
- Cold Spot review: Cruz, Martínez-González & Vielva 2009, arXiv:0901.1986.
- Supervoid test: Owusu et al. 2023, arXiv:2211.16139; Kovács et al. 2022,
  arXiv:2112.07699.
- Newer asymmetry tests: Sanyal, Aluri & Shafieloo 2026, arXiv:2601.13830;
  Lynch 2026, arXiv:2607.28774.
- Topology: Copi et al. 2026, arXiv:2606.24886 (abstract).

## Not verified
<!-- key: not-verified -->

- Akrami et al. 2014, Moss et al. 2011, Contreras et al. 2017 and 2018,
  Erickcek et al. 2009, Vielva et al. 2004, Cruz et al. 2005 and the
  look-elsewhere estimate of 1.85% for the Cold Spot ("[69]" of
  arXiv:1510.07929): cited through the papers above, not read.
- The bodies of arXiv:0908.3988, arXiv:0901.1986, arXiv:1703.07894,
  arXiv:2112.07699, arXiv:2601.13830, arXiv:2607.28774 and arXiv:2606.24886:
  abstracts only.
- The Planck 2018 X quadrupolar-modulation limits (Sect. 10.2) and the
  numerical posteriors of the curvaton model (Fig. 48 only described).
- The common-mask S_QO value of arXiv:2509.03720 (the conclusions quote
  the full-sky and 1% results only).
- The Abdalla et al. 2022 Sect. VIII.3 and CosmoVerse Sects. 2.3.3 and
  2.3.9.d named in `from`: not reread this session.
