# Distance indicators — cosmo-peculiar-velocities dossier

Scope: how a Fundamental Plane or Tully–Fisher relation is turned into per-galaxy log-distance
ratios in current catalogues — the observables and their corrections, the fitting likelihood and
its selection terms, the per-galaxy η posterior, the zero-point step — and how to choose between
the 3D-Gaussian, direct, inverse and orthogonal fits, the selection treatments and the
calibration samples.
Snapshot: 2026-10-19.
From: Turner 2024 review (arXiv:2411.19484), Sect. 3; Tsagas et al. 2025 review
(arXiv:2510.05340), Sect. 3.2; DESI DR1 PV FP and TF catalogue papers (arXiv:2512.03226,
arXiv:2512.03227); WALLABY pilot TF papers; 4HS FP programme.

Already in L2, not repeated here: why there are three indicators and their scatter in
`surveys-and-data.md#distance-indicators-why-three-and-what-each`; the per-indicator systematic list in
`systematics.md#systematics-by-indicator-the-qualitative-list`; the DESI DR1 FP priors, outlier count, aperture and
evolution parameters, CF4 comparison, TF slope and scatter, and the zero-point in
`systematics.md#desi-dr1-catalogues-and-zero-point-arxiv-2512`; the SDSS PV FP fit, f_n,
mock validation, richness trend and zero-point in
`systematics.md#sdss-pv-catalogue-howlett-et-al-2022-arxiv-2201`; the zero-point anchors and
their propagation in `systematics.md#zero-point-monopole-calibration`; the environment trends in
`systematics.md#environment-dependent-residuals-of-the-scaling`; the joint indicator calibration
inside a velocity–density fit in `deep/velocity-density-comparison.md` (Step 3); the velocity
estimators in `physics-and-methods.md#the-observable-log-distance-ratio-and-the`. SN Ia
standardisation belongs to `cosmo-supernovae`; SN velocities to `deep/supernova-velocities.md`.

Notation (FP, following Howlett et al. 2022, arXiv:2201.03112, and Ross et al. 2025,
arXiv:2512.03226): r = log R_e (effective radius in h⁻¹ kpc), s = log σ0 (central velocity
dispersion in km/s), i = log I_e (mean surface brightness within R_e in L_⊙ pc⁻²); the plane is
r = a s + b i + c. r_z is the radius computed with the observed redshift; r_t the true one. η =
log10[d(z_obs)/d(z̄)] is the log-distance ratio, z̄ the cosmological redshift. TF: M the
absolute magnitude, V or W a rotation velocity or HI linewidth.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Build distance-independent and distance-dependent observables (FP)
<!-- key: step-1-build-distance-independent-and-distance -->

The radius is the only distance-dependent FP quantity. SDSS PV computes it from the angular
effective radius θ_e = r^deV sqrt(b/a) (Eq. 2) as

    r_z = log θ_e + log d(z_group) − log(1 + z_helio) + log(π/648)              (Eq. 3)

with d the comoving distance in h⁻¹Mpc to the **group** redshift; the group redshift is used to
neglect intra-group velocities, "which helps reduce non-linearities", and the heliocentric
redshift for the conversion to angular-diameter distance (Calcino & Davis 2017) [src:
arXiv:2201.03112, Sect. 2.2]. DESI DR1 writes the same expression with the **CMB-frame
galaxy** redshift (Eq. 8) and defines η directly as the offset from the fitted plane,
r_z − a s − b i − c = log d(z_cmb) − log d(z̄) ≡ η (Eq. 9) [src: arXiv:2512.03226, Sect. 5.1]; the
group trend is then corrected afterwards (L2).

The two distance-independent quantities carry the corrections [src: arXiv:2201.03112, Eqs. 4–5;
arXiv:2512.03226, Eqs. 10–11]:

    s = log σ + α_ap [log θ_e − log(8 θ_ap)]                                     (aperture)
    i = 0.4 (M_⊙ − m − Q z + k + A) − log(2π θ_e²) + 4 log(1 + z_helio) + 2 log(64800/π)

with θ_ap the fibre aperture radius, Q the luminosity-evolution coefficient, k the k-correction,
A the Galactic extinction and 4 log(1 + z_helio) the surface-brightness dimming. SDSS PV takes
α_ap = −0.04 (Jørgensen et al. 1995) and Q = 0.85 (Bernardi et al. 2003); DESI DR1 takes θ_ap =
0.75″, α_ap = −0.06 ± 0.03 and Q = 1.1 ± 0.4. The DESI reason for α_ap: literature values span
−0.066 ± 0.035 to −0.033 ± 0.003, the choice moves single η by only Δη ≈ 0.005 against σ_η ≈ 0.12,
but it "can introduce a redshift-dependent tilt" across the sample, and −0.06 "flattens this tilt
while encapsulating the range of literature values"; Q is the mean of six literature values
with their standard deviation as error [src: arXiv:2512.03226, Sect. 5.1]. The reason for the
aperture correction at all: a fixed fibre covers more of a distant galaxy, which lowers the
measured σ [src: same].

A historical slip to know: Springob et al. 2014 included an extra log(1 + z̄) − log(1 + z_group)
term; Howlett et al. call it "a common misconception" that "actually vanishes", producing a
relative error Δv_p/v_p ≈ ln(10) z/(1 + z), "generally < 10 % of the typical statistical
uncertainty" for 6dFGSv [src: arXiv:2201.03112, Sect. 2.3 and App. D].

### Step 2. Fit the plane as a censored 3D Gaussian
<!-- key: step-2-fit-the-plane-as-a-censored-3d-gaussian -->

The method is the maximum-likelihood Gaussian of Saglia et al. 2001 and Colless et al. 2001
(EFAR), used for 6dFGSv, SDSS PV and DESI DR1 [src: arXiv:2201.03112, Sect. 4;
arXiv:2512.03226, Sect. 5.2]. With x_n = {r_n, s_n, i_n} and mean x̄:

    L = Π_n ( exp[−½ (x_n − x̄) C_n⁻¹ (x_n − x̄)ᵀ] / [(2π)^{3/2} |C_n|^{1/2} f_n] )^{1/S_n}  (Eq. 16 / 12)
    C_n = Σ + E_n                                                                   (Eq. 17)
    E_n = [[e_r² + ε_r², 0, −e_r e_i], [0, e_s², 0], [−e_r e_i, 0, e_i²]],   ε_r = log(1 + 300/cz_n)

[src: arXiv:2201.03112, Eqs. 16–17]. Σ is the intrinsic scatter, written through orthogonal
eigenvectors with scatters σ1, σ2, σ3, with the a-priori assumption that the longest axis lies
"exactly in the r–i plane"; 8 free parameters a, b, r̄, s̄, ī, σ1, σ2, σ3; c = r̄ − a s̄ − b ī
[src: arXiv:2201.03112, Sect. 4; arXiv:1409.6161, Sect. 3.2]. The stated reasons for the
error-matrix choices: a perfect r–i anticorrelation of the photometric errors (both come from
θ_e), no photometric–spectroscopic correlation, and ε_r "to account for non-linear velocities
that may bias the fit when the uncertainty on the effective radius for a given galaxy is small"
[src: arXiv:2201.03112, Sect. 4].

The fit is unanchored, under the assumption of no net radial flow; maximisation by scipy
differential evolution, "less than a minute" on one core once the 3×3 determinants and
inverses are written analytically and vectorised [src: arXiv:2201.03112, Sect. 4]. Outliers: an
iterative p < 0.01 clip on each galaxy's χ² (5 iterations and 503 rejections for SDSS PV; 6 and
1 534 for DESI DR1). The SDSS reason: before clipping the reduced χ² is ~0.9, i.e. "the best-fit
intrinsic scatter is being overestimated to accommodate the outliers"; it converges to 1.005
[src: arXiv:2201.03112, Sect. 4.2; arXiv:2512.03226, Sect. 5.2.1].

Sample purity matters for the plane itself: in SDSS PV the ~20 % of objects rejected as spirals
or by inspection occupy distinct regions of the space, and including them shifts the fitted
plane, which "would lead to biased log-distance ratios for the rejects, and for the clean
early-types if they were left in" [src: arXiv:2201.03112, Sect. 4.3]. DESI DR1 selects early
types by colour cuts, a de Vaucouleurs or Sérsic n_s > 2.5 profile and b/a > 0.3, and keeps
50 < σ < 420 km/s; the lower bound sits "slightly above the DESI blue camera resolution limit"
because dispersions near it are inflated, the upper removes failed fits [src: arXiv:2512.03226,
Sect. 2 Table 1, Sect. 4.1].

### Step 3. Put the selection into the likelihood: S_n and f_n
<!-- key: step-3-put-the-selection-into-the-likelihood-sn -->

Two devices, used for different cuts and differently at the two stages [src: arXiv:2201.03112,
Sects. 4.1, 5, 5.1]:

- **S_n**, a 1/V_max-type weight, up-weights galaxies of an apparent magnitude that is observable
  only in part of the volume:

      S_n = [d_L³(z_lim,n) − d_L³(z_min)] / [d_L³(z_max) − d_L³(z_min)]   for z_min < z_lim,n < z_max
                                                                            (Eq. 18; 1 or 0 outside)

  with d_L(z_lim,n) = d_L(z_group,n) × 10^{(17 − m_n)/5}. It replaces the full integral of the PDF
  times the selection probability, which is expensive; following Eadie et al. 1971 it "results in
  the same maximum likelihood FP values, but underestimates the variance", acceptable because
  errors come from mocks [src: Sect. 4, 4.1.1].
- **f_n** renormalises each galaxy's Gaussian over the observable part of parameter space. When
  fitting the plane, SDSS PV uses it only for the s_min = log 70 cut, because modelling the
  magnitude cut that way "requires knowledge of the magnitudes and log-distance ratios of
  galaxies that by definition have not been observed"; 99 % of galaxies have f_n ≥ 0.998 [src:
  Sect. 4.1.2]. DESI DR1 includes an upper s cut and states S_n covers the redshift, magnitude and
  velocity-dispersion cuts (s_min = log 50, s_max = log 420, 10 ≤ m ≤ 18) [src:
  arXiv:2512.03226, Sect. 5.2, Eqs. 12–14].

When fitting η for each galaxy (plane fixed), S_n is a constant and drops, but f_n now depends on
the trial distance and must be kept:

    f_n = (2π)^{−3/2} |C_n|^{−1/2} ∫ di ∫_{r_min−i/2}^{r_max−i/2} dr ∫_{s_min} ds exp[…]   (Eq. 21)

with r_min, r_max the radii corresponding to the bright and faint magnitude limits at the trial
distance (Eqs. 22–23). Its effect is "to up-weight larger distances" for incompleteness at the
faint end and for the larger volume — i.e. f_n is the homogeneous Malmquist correction [src:
Sect. 5.1]. SDSS PV reduces the integral to elementary functions (App. C), all 1 001 trial
distances for 34 059 galaxies in under a minute; 6dFGSv had evaluated it by Monte Carlo on
mocks with one correction for all galaxies, inaccurate at large distance "where … the number of
mock galaxies … quickly goes to zero"; ~95 % of SDSS galaxies share nearly the same curve,
which "validates" that approximation for most objects [src: Sect. 5.1, Fig. 9].

Why only homogeneous Malmquist bias here: 6dFGSv argues that velocities placed at the
**redshift-space** position make inhomogeneous Malmquist bias "negligible", because redshift
errors are small, while it "is most pronounced when one is measuring galaxy distances in real
space" [src: arXiv:1409.6161, Sect. 4.2]. Analyses that place galaxies at their inferred
distance must add the density prior (velocity–density dossier, Step 3).

### Step 4. Turn the fixed plane into a posterior on η per galaxy
<!-- key: step-4-turn-the-fixed-plane-into-a-posterior-on -->

Substitute x_n = {r_n − η_n, s_n, i_n}, evaluate Eq. 16 with N = 1, S_n = 1, x̄ and C_n fixed, on
1 001 uniform trial values of η in [−1.5, 1.5], multiply by a flat prior and normalise [src:
arXiv:2201.03112, Sect. 5; arXiv:2512.03226, Sect. 5.2.2]. The tabulated posterior is summarised
by a skew-normal (Eq. 19) with location ξ, scale ω and shape α obtained from its mean,
standard deviation and skewness (Eq. 20); the skew "arises from the f_n correction" and is
"small enough that it will likely have a negligible effect", "but we recommend confirming this"
[src: arXiv:2201.03112, Sect. 5]. DESI DR1 stores the same three numbers per galaxy
(logdist, logdist_err, logdist_alpha) for all 108 810 targets, of which only primaryVdisp = True
should enter a cosmological analysis [src: arXiv:2512.03226, Sect. 5.2.2].

The reason η, not v, is the delivered quantity: "if the FP is treated as Gaussian, and the
uncertainties in each of the input parameters are Gaussian, then η is also Gaussian
distributed" up to the selection-induced skew; the exact velocity requires inverting the
redshift–distance relation and a non-Gaussian PDF with a Jacobian [src: arXiv:2201.03112,
Sect. 2.3]. The log-normal velocity distribution that follows from Gaussian FP offsets is
derived in arXiv:1409.6161, App. A [src: outline].

### Step 5. Tully–Fisher: rotation measure, corrections, fit
<!-- key: step-5-tully-fisher-rotation-measure -->

Two current practices differ at every step.

**DESI DR1 (optical, single fibre).** The rotation is the line-of-sight velocity at 0.4 R26
(R26 the 26 mag arcsec⁻² isophotal radius), V′/c = [1 + z(0.4R26)]/(1 + z_center) − 1 (Eq. 8),
deprojected by V = V′/sin i (Eq. 9) with cos² i = [(b/a)² − q0²]/(1 − q0²) and q0 = 0.2 (Eq. 10);
7 km/s is added in quadrature to each Redrock redshift error [src: arXiv:2512.03227, Sect. III].
Against MaNGA Hα velocity fields (207 galaxies) the single-radius velocity has a normalised
scatter of 0.15 and a pull distribution of mean −0.07 and width 1.25 [src: Sect. III.1.3, Fig. 4].
Magnitudes are corrected as m_corr = m − A_MW − A_internal + A_k + A_sys (Eq. 4), with internal dust
A_internal = d (b/a − 1), d = −0.90 +0.15/−0.18, fitted to the magnitude–axis-ratio trend of the
DR1 sample itself; BASS magnitudes are shifted by 0.0234 to DECaLS; k-corrections to z = 0.1 to
match the FP [src: Sect. II.2]. Calibration: 4 050 galaxies in 14 bins of Δz = 0.005 over
0.03–0.1, one common slope, one intercept b_i per bin, fitted with HyperFit:

    m_r = a log(V/V0) + b_i                                                        (Eq. 16)
    ln L = ½ Σ_i Σ_j [ ln((a² + 1)/s_j²) − (a log(V_j/V0) + b_i − m_r,j)² / s_j² ]   (Eq. 17)
    s_j² = σ² + a² σ²_log V,j + σ²_m,j

with σ the intrinsic scatter along the magnitude axis; 16 free parameters [src: Sect. IV.3]. The
bins replace cluster calibration because grouping "requires a reliable cluster catalog and
assumes that the TFR is the same in clusters as in the field"; z ≥ 0.03 avoids galaxies whose
velocities are a large fraction of z [src: Sect. IV.2]. HyperFit "minimizes the distance
perpendicular to the best-fit line", a "hybrid of both the TFR and inverse TFR" [src: Sect.
IV.3]. Each b_i is turned into an absolute zero-point at the bin centre, B_i = b_i − μ(z_c,i)
(Eq. 18), and η = 0.2 [μ(z_CMB) − μ_TF] with μ_TF = m_corr − M_TF (Eqs. 20–21) [src: Sect. V].
The cosmology sample keeps 70 < V < 300 km/s, a velocity–distance-modulus cut and non-dwarfs,
because galaxies scattering above and left of the relation may be ones ("one possibility") whose rotation curve
has not peaked by 0.4 R26 [src: Sect. V.1].

**Cosmicflows-4 (HI linewidths, inverse fit).** The rotation measure is W_mx, built from W_m50
(the width at 50 % of the mean flux over the range holding 90 % of the flux) corrected for
resolution and redshift; ALFALFA widths are shifted by −6 km/s, older catalogues converted; W_mx
error ≤ 20 km/s or ALFALFA S/N > 10; W_mx > 64 km/s [src: Kourkchi et al. 2020,
arXiv:2004.14499, Sect. II.2]. Inclinations > 45° from face-on, set by eye against templates
(Galaxy Inclination Zoo), rms ±4°; kinematic inclinations from interferometry are more face-on by
3.3° at 4σ [src: Sect. II.1]. The relation is fitted **inverse** (errors and residuals in
linewidth): bias errors "are reduced by a factor of 5 with respect to a direct TFR analysis",
because with a direct fit "at a given line width an intrinsically brighter galaxy … is prone to be
included … while an intrinsically fainter galaxy may be lost", whereas "galaxies of a given
magnitude with wider and narrower line widths are equally likely to be included" [src: Sect.
III]. The authors add that the inverse fit is the right one for distances but not for the
physics of the relation, where a bivariate fit is "more informative" [src: Sect. I]. Calibration
uses ~600 spirals in 20 clusters [src: abstract].

### Step 6. Fix the zero-point
<!-- key: step-6-fix-the-zero-point -->

The unanchored fit assumes zero mean radial velocity, which for an all-sky sample removes only
the monopole, but for a one-hemisphere survey also "suppress[es] the polar component of the
dipole" — for a dipole along the pole it "corresponds to calibrating out the entire dipole".
6dFGSv therefore refits r̄ alone on a great-circle sample, the 3 781 galaxies with −20° ≤ δ ≤ 0°:
r̄ = 0.178 against 0.184 ± 0.005 for the full sample, uncertainty 0.003 dex with the other seven
parameters fixed (0.007 if all were free) [src: arXiv:1409.6161, Sect. 3.2]. SDSS PV and DESI
DR1 anchor instead to external distances (L2).

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Direct, inverse or orthogonal TF fit
<!-- key: direct-inverse-or-orthogonal-tf-fit -->

| Fit | Selection it tolerates | Cost | Used by |
|---|---|---|---|
| Inverse (residuals in linewidth) | magnitude selection, to first order | residual bias from the shape of the luminosity function and the curvature of the relation, corrected by simulation | CF4, arXiv:2004.14499 |
| Direct (residuals in magnitude) | a cut in linewidth, not in magnitude | needs the selection modelled where magnitude matters | Boubel et al. 2024, arXiv:2301.12648 |
| Orthogonal (HyperFit) | neither strictly; "hybrid" | slope between the two | DESI DR1, arXiv:2512.03227 |

On the same CF4 i-band data the direct (Boubel) and inverse (Kourkchi) slopes agree at 1.7σ,
because "there is a numerous sample, the fitted range spanned is large relative to the
scatter", although "direct and inverse fits generally give differing results" [src:
arXiv:2301.12648, Sect. 6.1]. The cut must match the fit: Kourkchi cut at M_i = −17 for the
inverse fit; Boubel, fitting the direct relation, cut in linewidth "as it will not result in
biased estimates" and placed it at log W_mx = 2.2 by minimising the standard error of the mean
of the fit, removing 16 % (i) and 11 % (W1) of the samples [src: Sect. 3.2]. Boubel also finds
that the CF4 magnitude distribution is set by the HI flux limit and the linewidth cut, not by the
optical or infrared photometry, and that the ALFALFA flux limit itself depends on linewidth [src:
Sect. 4].

### Linear or curved TF, constant or varying scatter
<!-- key: linear-or-curved-tf-constant-or-varying-scatter -->

Kourkchi add a quadratic term above log W_m50 = 2.5 for a bright-end flattening; Boubel keep the
break fixed at w = 0 (w ≡ log W_mx − 2.5) because a free break "was under-constrained", the curved
model being only marginally better (reduced χ² 0.98 vs 1.02 in i; 0.97 vs 0.97 in W1) [src:
arXiv:2301.12648, Sect. 3.3, Eq. 18]. Scatter grows towards faint magnitudes, from ~0.40 to ~0.58
mag in the CF4 calibration; Kourkchi model it as quadratic in magnitude, which Boubel find gives
"excessive scatter for the brightest galaxies" of the full sample and replace by σ_TF = ε0 + ε1(w +
2.5) (Eq. 19) [src: arXiv:2004.14499, Sect. III.5; arXiv:2301.12648, Sect. 3.4]. In CF4 the
scatter-plus-luminosity-function bias and the curvature bias act "in opposite senses" with
distance and are simulated jointly [src: arXiv:2004.14499, Sect. III.8].

### Cluster, redshift-bin or Hubble-flow calibration of TF
<!-- key: cluster-redshift-bin-or-hubble-flow-calibration -->

Cluster templates (CF4: ~600 spirals in 20 clusters) give the slope with galaxies at a common
distance but assume field and cluster spirals share one relation and suffer the cluster
luminosity-function bias above [src: arXiv:2004.14499, abstract, Sect. III.6]. Redshift bins
(DESI DR1) use the full sample and need no group catalogue, at the price of intercepts that
absorb any coherent flow within a bin and of a lower redshift limit (0.03) [src:
arXiv:2512.03227, Sect. IV.2].

### Selection by weights or by normalisation (FP)
<!-- key: selection-by-weights-or-by-normalisation-fp -->

S_n weighting is cheap and gives the right best-fit plane but the wrong variance; f_n is exact
for cuts whose effect does not depend on the unobserved galaxies; a full hierarchical model of
plane, distances and cosmology ("as done in Dam (2020) and Said et al. (2020)") "works best when
the goal is … a smaller number of derived parameters", not a catalogue of velocities, and is
"computationally expensive" [src: arXiv:2201.03112, Sects. 4, 4.1.2]. Analytic f_n against
mock-based f_n: same for ~95 % of SDSS galaxies, different for galaxies with unusual
k-corrections, extinction or large e_s [src: Sect. 5.1, Fig. 9].

### Galaxy or group redshift in r_z
<!-- key: galaxy-or-group-redshift-in-rz -->

SDSS PV uses group redshifts to suppress intra-group motions [src: arXiv:2201.03112, Sect.
2.2]; DESI DR1 uses galaxy CMB-frame redshifts and corrects a group-richness trend afterwards
(L2). A downstream analysis must know which, since a group redshift already removes part of the
non-linear velocity that σ_v or σ_u models are meant to absorb.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| FP fit time | < 1 min on one core (analytic 3×3, vectorised) | SDSS PV | arXiv:2201.03112 | Sect. 4 |
| Galaxies with f_n ≥ 0.998 in the plane fit | 99 % | SDSS PV | arXiv:2201.03112 | Sect. 4.1.2 |
| Reduced χ² before / after clipping | ~0.9 → 1.005 | SDSS PV | arXiv:2201.03112 | Sect. 4.2 |
| Trial η grid | 1 001 values in [−1.5, 1.5], flat prior | SDSS PV, DESI DR1 | arXiv:2201.03112; arXiv:2512.03226 | Sect. 5; Sect. 5.2.2 |
| ε_r floor | log(1 + 300/cz) | SDSS PV | arXiv:2201.03112 | Eq. 17 |
| Aperture correction α_ap | −0.04 (SDSS PV); −0.06 ± 0.03 (DESI DR1); literature −0.066 to −0.033 | — | arXiv:2201.03112; arXiv:2512.03226 | Eq. 5; Sect. 5.1 |
| Evolution Q | 0.85 (SDSS PV); 1.1 ± 0.4 (DESI DR1) | — | same | Eq. 4; Sect. 5.1 |
| σ cuts | > 70 km/s (SDSS PV); 50–420 km/s (DESI DR1) | — | same | Sect. 4.1; Sect. 4.1 |
| Magnitude cuts | 10.0–17.0 (SDSS PV); 10–18 (DESI DR1) | — | same | Sect. 4.1; Sect. 5.2 |
| DESI σ: sky uniformity / vs SDSS | cell standard deviation 5 % over 1 156 cells, max 16 %; DESI slightly lower than Portsmouth pPXF, within 5 %, on 35 067 galaxies | DESI DR1 | arXiv:2512.03226 | Sects. 4.3–4.4, Figs. 4, 8 |
| Error from the spurious log(1 + z) term | Δv/v ≈ ln(10) z/(1 + z); < 10 % of the statistical error for 6dFGSv | 6dFGSv | arXiv:2201.03112 | Sect. 2.3, App. D |
| 6dFGSv zero-point | r̄ = 0.178 ± 0.003 dex on 3 781 equatorial galaxies | 6dFGSv | arXiv:1409.6161 | Sect. 3.2 |
| TF inclination q0 / min inclination | 0.2 (DESI); > 45°, rms ±4° (CF4) | — | arXiv:2512.03227; arXiv:2004.14499 | Eq. 10; Sect. II.1 |
| Single-fibre vs IFU rotation | normalised scatter 0.15; pull mean −0.07, width 1.25 (207 galaxies) | DESI DR1 | arXiv:2512.03227 | Sect. III.1.3 |
| TF calibration bins | 116–356 galaxies per bin, rms 0.46–0.66 mag | DESI DR1 | arXiv:2512.03227 | Table 1 |
| Inverse vs direct TF bias | factor ~5 smaller with the inverse fit | CF4 | arXiv:2004.14499 | Sect. III |
| TF scatter vs magnitude | ~0.40 (bright) to ~0.58 mag (faint); i band 0.49 on 430, W1 0.58 on 584 | CF4 calibration | arXiv:2004.14499 | Sect. III.5 |
| Direct vs inverse slope on CF4 i band | consistent at 1.7σ (a1 = −8.55 ± 0.05 vs −8.32 ± 0.13) | CF4 TF | arXiv:2301.12648 | Sect. 6.1 |
| Optimal linewidth cut (direct fit) | log W_mx = 2.2; removes 16 % (i), 11 % (W1) | CF4 TF | arXiv:2301.12648 | Sect. 3.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A tilt of mean η with redshift.** A wrong aperture or evolution correction, or residual
  selection, produces a spurious inflow or outflow. Test: the error-weighted mean η of the mocks
  against the truth in redshift bins (SDSS PV: unbiased over the full range on 2 048 mocks) and
  the data's own mean η against z with α_ap and Q varied (DESI DR1) [src: arXiv:2201.03112, Sect.
  5.2.1; arXiv:2512.03226, Sect. 5.1].
- **η correlates with absolute magnitude.** Expected, not a bug, for an r-direction offset from
  a 3D Gaussian: η ∝ r + 0.841 i while M ∝ r + 0.5 i in SDSS PV; Saglia et al. 2001 found this
  method gave "the most unbiased peculiar velocities" among the alternatives they tried. Do not
  "correct" it [src: arXiv:2201.03112, Sect. 5.2.2].
- **Hemispheric zero-point.** Setting ⟨η⟩ = 0 on a one-hemisphere sample removes part of the
  dipole; check the zero-point sample's sky distribution [src: arXiv:1409.6161, Sect. 3.2].
- **Contaminated plane.** Spirals or misfit profiles left in shift the plane for everyone
  [src: arXiv:2201.03112, Sect. 4.3].
- **Rotation not at maximum.** Single-radius optical rotation may underestimate V for galaxies whose
  curve still rises at 0.4 R26 ("one possibility" in the paper); such galaxies would sit above
  and left of the relation; DESI cuts on V and on a
  V–μ relation [src: arXiv:2512.03227, Sect. V.1].
- **Selection mismatched to the fit.** A magnitude cut with a direct TF fit, or a linewidth cut
  with an inverse fit, biases the relation [src: arXiv:2004.14499, Sect. III; arXiv:2301.12648,
  Sect. 3.2].
- **Residuals correlated with density.** In Millennium-TNG the residuals of standard TF and FP
  relations "cannot be described as purely random Gaussian noise, but instead correlate with the
  local density field"; they enter the velocity–galaxy monopole and the small-scale velocity
  auto-correlation (below ~1 h⁻¹Mpc for TF, ~10 h⁻¹Mpc for FP) but not the dipole [src:
  arXiv:2602.23033, Sect. 4.3]. **Null test:** the monopole ξ^{vg}_0 of the velocity–galaxy
  cross-correlation vanishes for true velocities, so a non-zero measured monopole is the residual
  signal; applied to SDSS PV with its 2 048 mocks it gives χ²/dof = 51.1/20, a 3.6σ detection
  [src: App. C]. Extended relations with M_*, gas mass and SFR suppress it in simulation but are
  a proof of principle only, since a real calibration must use distance-independent quantities
  [src: Sect. 5.2].

## Reading list
<!-- key: reading-list -->

- Turner 2024, arXiv:2411.19484, Sect. 3 — review: the TF and FP relations, their physical basis
  and scatter.
- Howlett et al. 2022, arXiv:2201.03112, Sects. 2–5 and App. C — method: the reference
  description of the 3D-Gaussian FP fit, S_n and analytic f_n, skew-normal η posteriors.
- Ross et al. 2025, arXiv:2512.03226, Sects. 2, 4, 5 — application: the same method on DESI DR1,
  with the aperture-correction choice and the σ quality checks.
- Springob et al. 2014, arXiv:1409.6161, Sects. 3–4 — method: 6dFGSv zero-point from an
  equatorial sample, Monte Carlo f_n, redshift- vs real-space Malmquist bias.
- Douglass et al. 2025, arXiv:2512.03227, Sects. II–V — application: optical single-fibre TF,
  redshift-bin HyperFit calibration.
- Kourkchi et al. 2020, arXiv:2004.14499, Sects. II–III — method: HI-linewidth inverse TF, its
  bias argument and residual-bias simulations.
- Boubel et al. 2024, arXiv:2301.12648, Sects. 2–4, 6.1 — alternative: direct TF forward-modelled
  with the selection, compared with the inverse fit on the same data.
- Dumerchat et al. 2026, arXiv:2602.23033, Sects. 4–5, App. C — critique: correlated residuals and
  the ξ^{vg}_0 null test.

## Not verified
<!-- key: not-verified -->

- Saglia et al. 2001, Colless et al. 2001 (EFAR), Magoulas et al. 2012, Dam 2020: cited through
  arXiv:2201.03112 and arXiv:2512.03226 only; no identifier fetched.
- The 6dFGSv f_n details beyond Sect. 4.2 (the mock integration itself) and its App. A
  derivation: outline only.
- The Tsagas et al. 2025 review Sect. 3.2, the WALLABY pilot TF calibrations and the 4HS FP
  programme named in `subtopics.tsv`: not read for this dossier.
- Whether DESI DR1 applies S_n to the velocity-dispersion cut, as its Sect. 5.2 wording says, or
  only f_n, as SDSS PV does: the two sentences of arXiv:2512.03226 Sect. 5.2 can be read either
  way.
