# Weak lensing — systematics

Scope: the canonical systematic effects of cosmic shear and galaxy–galaxy
lensing: mechanism, measured size, mitigation, validation test, and the paper
a referee expects.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here.

Convention used throughout: the observed shear is modelled as γ_obs = (1 + m)
γ_true + c, with multiplicative bias m and additive bias c;
redshift-distribution errors are summarised per tomographic bin by a shift Δz
of the mean, n_i(z) → n_i(z − Δz_i) (the STEP convention: Heymans et al. 2006,
arXiv:astro-ph/0506112).

## 1. Shear measurement bias (noise, model, selection)
<!-- key: shear-measurement-bias-noise-model-selection -->

**Mechanism.** Ellipticity is a non-linear function of noisy pixels, so its
expectation is biased (noise bias); an assumed galaxy model that does not
match real morphology biases the fit (model bias); any selection that
correlates with the shear (detection, S/N or size cuts) biases the mean
(selection bias).

**Mitigation.** Two families. (a) Calibrate a given estimator on image
simulations: lensfit in CFHTLenS and KiDS (Miller et al. 2013,
arXiv:1210.8201), calibrated with simulations that emulate the data, where
lensfit is found unbiased within a 2 per cent tolerance (Kannawadi et al.
2019, arXiv:1812.03983) [src], and, for KiDS-Legacy, with the multi-band
SKiLLS simulations that calibrate shear and redshift jointly (Li et al. 2023,
arXiv:2210.07163). (b) Self-calibrate on the data by measuring the response of
the estimator to an artificial shear: metacalibration (Huff & Mandelbaum 2017,
arXiv:1702.02600; Sheldon & Huff 2017, arXiv:1702.02601), used for DES Y1
(alongside im3shape; 1σ uncertainties on m of 0.013 and 0.025 respectively)
and Y3 (arXiv:1708.01533, arXiv:2011.03408) [src], and for DECADE
(arXiv:2502.17674) [src], and metadetection, which also re-runs
detection on the sheared images and so removes shear-dependent detection bias
(Sheldon et al. 2020, arXiv:1911.02505), used for DES Y6 on cell-based coadds
(Yamamoto et al. 2025, arXiv:2501.05665) and planned for Rubin (Sheldon et al.
2023, arXiv:2303.03947). Analytic-response estimators are a third route (Li &
Mandelbaum 2023, arXiv:2208.10522).

**Size.** Metacalibration removes calibration bias to a few tenths of a per
cent on the GREAT3 simulations (arXiv:1702.02600) [src]. Without a detection
step it leaves a bias of a few per cent at the galaxy densities of current
surveys, growing with density, which metadetection reduces to at most a few
tenths of a per cent (arXiv:1911.02505) [src]. The DES Y6 metadetection
catalogue has no detectable multiplicative bias: m = (3.4 ± 6.1) × 10⁻³, the
uncertainty being quoted at 3σ (arXiv:2501.05665) [src]. The Rubin requirement
is at the 0.1% level (arXiv:2303.03947) [src]. Metacalibration applied to
KiDS-1000 and tested on SKiLLS gives |m| < 0.017 in every tomographic bin with
negligible additive bias, and its calibration is nearly insensitive to galaxy
properties; the cosmology does not move (S8 = 0.789 +0.020/−0.024 against
0.776 with lensfit) (Yoon et al. 2025, arXiv:2510.01122) [src].

**Validation.** Image simulations with known shear; mean shear and tangential
shear around random points and stars; shear as a function of galaxy and
observing properties; cross-pipeline comparison on the same data.

**Referee expects:** arXiv:1702.02601 and arXiv:1911.02505 for the method; the
survey's own shape-catalogue and image-simulation papers for m and its
uncertainty.

## 2. Blending
<!-- key: blending -->

**Mechanism.** Overlapping galaxies are detected as one object or contaminate
each other's light. When the blended galaxies are at different redshifts the
shear response is a mixture, so blending couples the shear calibration to the
redshift distribution: m becomes redshift-dependent and the effective n(z)
changes.

**Size.** In the DES Y3 image simulations blending-related effects are the
dominant contribution to a mean multiplicative bias of about −2% (MacCrann et
al. 2022, arXiv:2012.08567) [src], and the blending corrections shift the DES
Y3 best-fit S8 by 0.5σ without a substantial increase in uncertainty (Amon et
al. 2022, arXiv:2105.13543) [src].

**Mitigation and referee reference.** DES Y3 calibrates shear and redshift
biases jointly with image simulations (arXiv:2012.08567); KiDS-Legacy does the
equivalent with SKiLLS (arXiv:2210.07163); DES Y6 uses metadetection plus
full-survey synthetic source injection with Balrog, which shows percent-level
accuracy of the measured object properties (Anbajagane et al. 2025,
arXiv:2501.05683) [src]. Earlier quantifications: ambiguous blends (Dawson et
al. 2016, arXiv:1406.1506), impact on deep surveys (Nourbakhsh et al. 2022,
arXiv:2112.07659).

## 3. PSF modelling and leakage
<!-- key: psf-modelling-and-leakage -->

**Mechanism.** The PSF both circularises (multiplicative) and imprints its
ellipticity (additive) on galaxy shapes; errors in PSF size and ellipticity
models propagate into m and c (Paulin-Henriksson et al. 2008,
arXiv:0711.4886).

**Mitigation.** Empirical PSF models interpolated from stars, with diagnostics
from the correlation functions of PSF residuals (the ρ statistics; Rowe 2010,
arXiv:0904.3056). DES Y3 and Y6 use PIFF (Jarvis et al. 2021,
arXiv:2011.03409; Schutt et al. 2025, arXiv:2501.05781).

**Size.** HSC Y1: fractional PSF size residuals of about 0.003 (requirement
0.004) and ρ1 < 3×10⁻⁷ at 0.5° (requirement 4×10⁻⁷), "narrowly" meeting
requirements (Mandelbaum et al. 2018, arXiv:1705.06745) [src]. KiDS-1000
verifies that its PSF model induces less than a 0.1σ change in S8 (Giblin et
al. 2021, arXiv:2007.01845) [src]. DES Y6 improved PIFF with Gaia and infrared
photometry to purify the star sample (arXiv:2501.05781) [src]. For Rubin,
simulations put the additive PSF-error contribution well below 30% of the
cosmic-shear uncertainty (Hébert et al. 2026, arXiv:2608.21688) [src].

**Validation.** ρ statistics and their propagation into ξ±; star–galaxy
cross-correlation; B modes. UNIONS traced initial B-mode failures to galaxy
size cuts and stellar halo masking, and an oscillatory COSEBI B-mode pattern
to a repeating additive shear bias at the CCD scale, the same detector-level
effect seen in CFHTLenS; after cuts all three E/B statistics pass, minimum PTE
= 0.18 (Daley et al. 2026, arXiv:2604.03227) [src].

## 4. Redshift distributions
<!-- key: redshift-distributions -->

**Mechanism.** The lensing kernel depends on the source n(z); an error in the
mean redshift of a bin maps almost directly into the shear amplitude and hence
S8.

**Mitigation, three independent routes plus one cross-check.**
1. *Colour-space reweighting with self-organising maps (SOM).* Map the
   many-band colour space, populate it with spectroscopic or many-band
   photometric redshifts, and reweight to the wide sample (Masters et al.
   2015, arXiv:1509.03318; KiDS: Wright et al. 2020, arXiv:1909.09632; DES
   SOMPZ: Buchs et al. 2019, arXiv:1901.05005; Myles et al. 2021,
   arXiv:2012.08566). The earlier form is direct reweighting of a
   spectroscopic sample (Lima et al. 2008, arXiv:0801.3822).
2. *Clustering redshifts.* Cross-correlate the photometric sample with
   spectroscopic tracers in thin redshift slices (Newman 2008,
   arXiv:0805.1409; Ménard et al. 2013, arXiv:1303.4722; DES Y3: Gatti et al.
   2022, arXiv:2012.08569; KiDS: van den Busch et al. 2020, arXiv:2007.01846).
3. *Shear ratios.* The ratio of tangential shear around the same lenses for
   two source bins is geometric (Jain & Taylor 2003, arXiv:astro-ph/0306046;
   DES Y3: Sánchez et al. 2022, arXiv:2105.13542).
4. *Self-calibration in the cosmological fit.* HSC Y3 applies "a conservative,
   wide, flat prior on the photometric redshift errors on the last two
   tomographic bins" and lets the relative shear amplitudes across bins
   calibrate them (Li et al. 2023, arXiv:2304.00702) [src]; the HSC Y3 3×2pt
   analysis then finds hints that the true mean redshift at z ≳ 0.75 is higher
   than the photo-z estimate (Miyatake et al. 2023, arXiv:2304.00704) [src].

**Size, earlier analyses.** KiDS-1000: SOM-reweighted spectroscopic
calibration in five bins over 0.1 < z_B ≤ 1.2, residual mean-redshift biases ≲
0.01 with uncertainties ~0.01, and ~0.01–0.02 for the clustering-redshift
recalibration (Hildebrandt et al. 2021, arXiv:2007.15635) [src]; on mocks the
SOM method has a maximal bias Δ⟨z⟩ = 0.013 ± 0.006 (arXiv:1909.09632) [src].
DES Y3: combined σ⟨z⟩ ~ 0.01 per bin (arXiv:2012.08566) [src]; clustering
redshifts recover the bin means to an RMS of ~0.014 in simulations
(arXiv:2012.08569) [src]; shear ratios tighten the source-redshift priors by
up to 38% in some bins and the cosmic-shear S8 constraint by up to 31% (10%
for 3×2pt) (arXiv:2105.13542) [src].

**Size, final analyses.** DES Y6: σ⟨z⟩ = 0.012, 0.008, 0.009, 0.024 for bins
centred at 0.414, 0.538, 0.846, 1.157; the dominant term is the lack of faint
representative spectra; SOMPZ and clustering redshifts agree, and give
cosmological constraints within 0.1σ of each other (Yin et al. 2025,
arXiv:2510.23566) [src]. Adding clustering redshifts (BOSS and eBOSS
references, 1.5–5 Mpc scales) improves the DES Y6 S8 constraint by about 10%
(d'Assignies et al. 2025, arXiv:2510.23565) [src]. KiDS-Legacy: SOM and
cross-correlation estimates agree on simulations and to better than 2σ in
every bin on data (Wright et al. 2025, arXiv:2503.19440) [src]. HSC Y3:
replacing the original calibration by DESI clustering redshifts moves S8 from
0.769 to 0.804 and shrinks the error by a factor 1.8 (arXiv:2511.18134) [src].
DESI-based unified calibration reaches σ_z̄ ~ 0.01 or better for DES, HSC and
KiDS (Lange et al. 2025, arXiv:2510.25419) [src]; applied to KiDS-1000 it
finds mean shifts averaging −0.028 and shows that spectroscopic incompleteness
within SOM cells can alter n(z) (Blanco et al. 2025, arXiv:2512.15964) [src].

**Referee expects:** two independent methods with a quantitative comparison;
the treatment of spectroscopic incompleteness; how n(z) uncertainty is
propagated (mean shifts, or an ensemble of n(z) realisations as in DES Y3/Y6).
Review: Newman & Gruen 2022, arXiv:2206.13633.

## 5. Intrinsic alignments
<!-- key: intrinsic-alignments -->

**Mechanism.** Galaxy shapes align with the tidal field, adding
intrinsic–intrinsic (II) and gravitational–intrinsic (GI) terms to the shear
correlation (Hirata & Seljak 2004, arXiv:astro-ph/0406275).

**Models.** NLA: linear alignment with the non-linear matter power spectrum,
one amplitude plus an optional redshift power law (Bridle & King 2007,
arXiv:0705.0166). TATT: tidal alignment plus tidal torquing plus density
weighting from perturbation theory (Blazek et al. 2019, arXiv:1708.09247).
Halo models with a satellite term (Fortuna et al. 2021, arXiv:2003.02700).
Reviews: Joachimi et al. 2015, arXiv:1504.05456; Troxel & Ishak 2015,
arXiv:1407.6990; Lamman et al. 2024, arXiv:2309.08605; Chisari 2025,
arXiv:2510.15738.

**Why the model matters.** With alignments included, two or more times as many
tomographic bins are needed to recover 80 per cent of the information
(arXiv:0705.0166) [src]. The quadratic and cross terms of TATT can be
order-unity corrections to the alignment signal at k ~ 0.1 h/Mpc, and in an
LSST-like **forecast** NLA cannot absorb them even with a free redshift
dependence (arXiv:1708.09247) [src]. The halo-model study finds that the model
refinements it tests give negligible biases for Stage-III surveys, but that
for Stage IV at least one additional parameter for the redshift dependence is
essential (arXiv:2003.02700) [src, **forecast**].

**Size.** The NLA/TATT choice moves the DES Y6 cosmic-shear S8 from 0.798 to
0.783 and the precision from 1.8% to 2.5% (arXiv:2602.10065) [src]. In UNIONS
the S8–A_IA degeneracy, with A_IA drawn from a direct-measurement prior, is
one of the largest uncertainties (arXiv:2605.13543) [src].

KiDS-1000 states that its known modelling systematics bias S8 by no more than
0.1σ, "with the caveat that no conclusive validation data exist for models of
intrinsic galaxy alignments" (Joachimi et al. 2021, arXiv:2007.01844) [src].
Type dependence was seen from the start: CFHTLenS found a significant
alignment signal for early-type galaxies and none for late types (Heymans et
al. 2013, arXiv:1303.1808) [src].

**Direct measurements.** DES Y3 redMaGiC, eBOSS LRG and BOSS CMASS: alignments
detected at 5σ–22σ on 6 < r_p < 70 h⁻¹Mpc; eBOSS emission-line galaxies give a
null result, A1 = 0.07 +0.32/−0.42 in NLA (Samuroff et al. 2023,
arXiv:2212.11319) [src]; DESI DR1 with DES, HSC, KiDS and SDSS shapes, over 2
million galaxies: the bluest galaxies are consistent with zero alignment, red
galaxies align more strongly with luminosity, and luminosity and colour
explain the signal at 0 < z < 1.5 without an explicit redshift dependence
(Siegel et al. 2025, arXiv:2507.11530) [src].

**Mitigation in practice.** Marginalise a model; inform it with direct
measurements (KiDS-Legacy, arXiv:2503.19441); or select a low-alignment blue
sample (arXiv:2512.04209).

## 6. Baryonic feedback
<!-- key: baryonic-feedback -->

**Mechanism.** AGN and stellar feedback move gas out of haloes and suppress
the matter power spectrum. The OWLS AGN simulation predicted a decrease
relative to dark-matter-only, at z = 0, of 1% at k ≈ 0.3 h/Mpc, 10% at k ≈ 1
h/Mpc and 30% at k ≈ 10 h/Mpc, so that baryons "cannot be ignored" for k > 0.3
h/Mpc (van Daalen et al. 2011, arXiv:1104.1174) [src]; simulation library: van
Daalen et al. 2020, arXiv:1906.00968. In shear, the baryonic correction model
predicts a 15–25% suppression of the shear power spectrum beyond ℓ ~ 100–600
and 10–25% effects on ξ+ below 5 arcmin and on ξ− below 50 arcmin (Schneider
et al. 2019, arXiv:1810.08629) [src]. Most of the effect on the scales of
cosmic shear comes from group-mass haloes, M ~ 10¹³–10¹⁴ M⊙ (Salcido et al.
2023, arXiv:2305.09710) [src].

**Mitigation.** (a) Scale cuts validated on synthetic data: DES Y3 reports no
bias above 0.3σ in the S8–Ωm plane from theory-model uncertainty (Secco et al.
2022, arXiv:2105.13544; strategy in Krause et al. 2021, arXiv:2105.13548; Y6
in arXiv:2601.14859) [src]. (b) Halo-model parametrisation: HMcode (Mead et
al. 2015, arXiv:1505.07833); HMcode-2020 has a six-parameter feedback model
and a single-parameter variant, matches the hydrodynamical power-spectrum
response to better than 1% for z < 1 and k < 20 h/Mpc, and ships with CAMB
(Mead et al. 2021, arXiv:2009.01858) [src]. (c) Baryonification of N-body
simulations and its emulators (Schneider & Teyssier 2015, arXiv:1510.06034;
Schneider et al. 2019, arXiv:1810.08629; Giri & Schneider 2021,
arXiv:2108.08863; Aricò et al. 2021, arXiv:2011.15018). (d) Principal
components of simulation suites (Huang et al. 2019, arXiv:1809.01146). (e)
Simulation-based fitting functions tied to halo baryon fractions (Salcido et
al. 2023, arXiv:2305.09710). (f) Nulling of small physical scales with the BNT
transform (arXiv:2607.04384). (g) External priors from X-ray gas fractions,
tSZ and kSZ (arXiv:2512.04209, arXiv:2506.07432, arXiv:2609.09144; kSZ
evidence: Bigwood et al. 2024, arXiv:2404.06098; Hadzhiyska et al. 2024,
arXiv:2407.07152; Ried Guachalla et al. 2025, arXiv:2503.19870).

**Earlier lensing-only constraints.** DES Y3 small scales with
baryonification: best-fit suppression ~5% at k = 1 h/Mpc and ~15% at k = 5
h/Mpc, M_c > 10^13.2 h⁻¹M⊙ at 95% (Chen et al. 2023, arXiv:2206.08591) [src];
DES Y3 with the BACCO emulator: log M_c = 14.38 +0.60/−0.56 and S8 = 0.799
+0.023/−0.015, 0.9σ from Planck and 1.4σ above the official DES Y3 value
because of modelling choices (Aricò et al. 2023, arXiv:2303.05537) [src].
X-ray gas fractions through the baryonic emulator imply a suppression
exceeding 1% at k = 0.1–0.4 h/Mpc and peaking at 20–28% near k = 7 h/Mpc
(arXiv:2108.08863) [src].

**External gas probes.** DES Y3 lensing + ACT DR5 kSZ constrain a mean
feedback scenario "more extreme than the predictions from most hydrodynamical
simulations" (arXiv:2404.06098) [src]. Stacked kSZ on DESI imaging galaxies is
detected at 13σ and disfavours low-feedback models of the IllustrisTNG kind
(arXiv:2407.07152) [src]. kSZ around DESI Y1 LRGs gives a tentative preference
for stronger feedback (Illustris z = 0.5, PTE = 0.37, against IllustrisTNG z =
0.8, PTE = 0.045) (arXiv:2503.19870) [src]. Detail belongs to
`cosmo-cmb-lss-cross-correlations`.

**Size.** See `results.md` section 1.5. Current scale cuts leave about 0.3σ
residual bias in (S8, Ωm) for a 13,000 deg² Stage-III data set
(arXiv:2509.03582) [src].

**The "non-linear solution".** Amon & Efstathiou 2022 (arXiv:2206.11794)
fitted a one-parameter suppression of the non-linear spectrum to KiDS-1000 and
argued that lensing and Planck ΛCDM are reconciled if the suppression is
stronger than assumed [src]. Preston et al. 2023 (arXiv:2305.09827) found that
the suppression DES Y3 requires is weaker than for KiDS but still more extreme
than recent simulations, and must reach k ~ 0.2 h/Mpc [src]. The FLAMINGO
simulations (Schaye et al. 2023, arXiv:2306.04024) answered that across their
feedback variations "baryonic effects are not sufficiently large to remove the
S8 tension" (McCarthy et al. 2023, arXiv:2309.07959) [src]. With the 2025–2026
S8 values the amount of suppression that would be "required" is smaller than
these papers assumed; none of the three has been redone on KiDS-Legacy or DES
Y6 as far as the searches of this session show.

## 7. Other effects a complete analysis treats
<!-- key: other-effects-a-complete-analysis-treats -->

| Effect | Standard treatment | Reference |
|---|---|---|
| Magnification of the lens sample | magnification coefficients per lens bin from Balrog source injection, with Gaussian priors. DES Y6 MagLim++ coefficients are 3.16 ± 0.08 to 4.90 ± 0.29 across six bins; neglecting magnification shifts the 2×2pt S8 by 1.37σ and Ωm by −0.84σ (−0.61σ and −0.71σ with cosmic shear included) [src: arXiv:2601.14833] | Elvin-Poole et al. 2023, arXiv:2209.09782; DES Y6: Legnani et al. 2026, arXiv:2601.14833 |
| Non-linear galaxy bias and point-mass term in γ_t | scale cuts, or analytic marginalisation of an enclosed-mass term | Prat et al. 2022, arXiv:2105.13541 |
| Source clustering, reduced shear | modelled explicitly once third-order statistics are used | arXiv:2606.12389 |
| Limber approximation | extended Limber or exact projection at low ℓ | LoVerde & Afshordi 2008, arXiv:0809.5112; Kilbinger et al. 2017, arXiv:1702.05301 |
| Covariance errors | analytic halo-model covariance with super-sample term, validated on mocks. DES Y3: the f_sky approximation for finite area is the largest effect, raising χ² by 3.7% (Δχ² ≈ 18.9) and the scatter of best-fit Ωm, σ8 by about 3% [src: arXiv:2012.08568]. KiDS-Legacy: OneCovariance is accurate at the per cent level; ignoring the survey geometry misestimates cosmic-variance terms by about 10% [src: arXiv:2410.06962] | arXiv:2012.08568, arXiv:2410.06962 |
| Cross-survey galaxy–galaxy lensing amplitude | blind comparison of ΔΣ around the same BOSS lenses from different shear catalogues: systematics above 15% (25%) excluded at 68% (95%) at z < 0.54; a 3–4σ correlation of amplitude with survey depth for z_L > 0.43 [src: arXiv:2111.13805]. With DESI DR1 lenses a trend with source redshift appears and vanishes once the HSC redshift shifts favoured by its cosmology analysis are applied [src: arXiv:2506.21677] | Leauthaud et al. 2022, arXiv:2111.13805; Heydenreich et al. 2025, arXiv:2506.21677 |
| Spatially varying depth | lens-sample weights and masks; variable-depth n(z) | Rodríguez-Monroy et al. 2025, arXiv:2509.07943 |

## 8. What a referee checks in a lensing results section
<!-- key: what-a-referee-checks-in-a-lensing-results -->

1. Which CMB data set the "tension" is measured against, and with which metric
   (S8 difference, full-parameter shift, PPD). References: arXiv:2602.12238
   for the CMB reference that each survey uses, arXiv:2601.14559 for two
   metrics quoted on the same data (2.6σ and 1.8σ).
2. The IA model, its priors, and how much S8 moves under the alternative.
3. The baryon treatment: scale cuts (and the simulation that set them) or a
   model (and its prior), and the residual bias.
4. Two independent redshift calibrations and their agreement per bin; how the
   uncertainty is propagated.
5. Shear calibration m per bin with its uncertainty, including the
   blending-induced redshift dependence.
6. PSF leakage (ρ statistics or equivalent) and B-mode null tests with PTEs,
   in more than one statistic.
7. Covariance: analytic or mocks, super-sample and non-Gaussian terms,
   survey-geometry treatment, and the goodness of fit.
8. Blinding: at which level (catalogue, data vector, parameters) and what
   changed after unblinding. References: Muir et al. 2020, arXiv:1911.05929
   (data-vector level, DES); Kuijken et al. 2015, arXiv:1507.00738
   (shear-catalogue level, KiDS).
9. Prior-volume and projection effects on marginal S8 (mean vs MAP),
   especially with TATT or wide Δz priors. References: arXiv:2305.17173
   (DES Y3 + KiDS-1000: mean 0.790, MAP 0.801); arXiv:2007.01844 (KiDS-1000
   warning on marginal point estimates).
10. Internal consistency splits: redshift bins, scales, colour, sky region,
    statistic.

## Not verified
<!-- key: not-verified -->

- Per-bin m and its uncertainty for DES Y3, HSC Y3 and KiDS-Legacy (in the
  bodies of the shape-catalogue papers; only the DES Y6 global value was
  read).
- ρ-statistic amplitudes and PSF-leakage coefficients for each survey.
