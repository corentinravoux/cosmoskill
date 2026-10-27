# JAGB stars and Miras — cosmo-distance-ladder-h0 dossier

Scope: how a JAGB distance is measured on JWST images (photometry, crowding,
outer-disc selection, colour box, statistic, error terms) and how a Mira
distance is measured on HST time series (period search, sample cuts,
crowding and blending, period range, carbon-star contamination, zero point,
the step to M_B), with the choices that separate the CCHP and SH0ES-side
JAGB procedures.
Snapshot: 2026-10-19.
From: Chen & Wang 2026, Sect. 4.2; Verde et al. 2023, Sects. 2.2.2 and
2.2.3; Freedman & Madore 2023, Sect. 7; CCHP programme; H0DN dataset
classes, Sect. III.

Already in L2: physics and founding calibrations
(`physics-and-methods.md#primary-stellar-indicators`); JAGB and Mira
systematics (`systematics.md#jagb-specific-effects`,
`systematics.md#miras-sbf-tully-fisher-fundamental-plane`); budget lines
(`systematics.md#error-budgets-term-by-term`); H0 values
(`results.md#local-distance-ladder-three-rung-geometry-stars`). TRGB, which
shares GLOESS and the NGC 4258 zero point: `deep/trgb.md`.

Notation. m_JAGB is the apparent JAGB reference magnitude of a field, M_JAGB
its absolute value; mu_0 a true distance modulus; sigma_s the GLOESS
smoothing width; P a Mira period in days; a the apparent PL zero point of a
Mira sample at log P = 2.3 (P = 200 d; arXiv:2312.08423, Eq. 2 and Sect. III.5), a_0 its absolute value; m_B^0 the
standardised SN Ia peak magnitude; a_B the intercept of the SN Hubble
diagram.

## How it is done
<!-- key: how-it-is-done -->

### JAGB step 1. Photometry
<!-- key: jagb-step-1-photometry -->

Both groups run DOLPHOT with its NIRCam module on stage-2 `cal` images, in
"warmstart" mode: a first pass on the short-wavelength band alone, then the
long-wavelength band forced on that source list [src: arXiv:2408.03474,
Sect. II.1; arXiv:2502.05259, Sect. II.2]. Stated reason: running both
channels at once gave source-matching problems, while warmstart "subtracted
stars more cleanly" [src: arXiv:2408.03474, Sect. II.1].

| Item | CCHP (Lee et al. 2024) | SH0ES-side (Li et al. 2025) |
|---|---|---|
| Bands | F115W with F356W or F444W | F150W with F277W |
| Vega system | Sirius-Vega | Vega-Vega; differs from Sirius-Vega by ~0.04 mag in F090W |
| Quality cuts | ERS resolved-stellar-populations cuts, purity over completeness, required in both bands | SN > 3 in F150W, crowd < 0.5, sharp^2 < 0.01, flag ≤ 2, type ≤ 2 per band |
| Blinding | random photometric offsets removed after the radial cut was fixed | not blinded |
| Place read | arXiv:2408.03474, Sect. II.1 | arXiv:2502.05259, Sect. II.2 |

Li et al. show F115W and F150W JAGB measurements agree "given the same
measurement choice" (their App. A) [src: arXiv:2502.05259, Sect. IV.1].

### JAGB step 2. Crowding correction
<!-- key: jagb-step-2-crowding-correction -->

Crowding biases outer-disc stars bright; artificial-star tests correct the
mean bias but not the extra width of the luminosity function [src:
arXiv:2502.05259, Sect. II.3]. Li et al. split each NIRCam chip into a
10 × 10 grid, inject at least 200,000 stars per module at three magnitudes
1 mag apart, centred on the uncorrected JAGB, fit the input-minus-output
offset linearly in magnitude and correct each cell [src: arXiv:2502.05259,
Sect. II.3]. Mean corrections are 0.01 mag in NGC 4258 and 0.02 to 0.05 mag
in F150W in the SN hosts [src: arXiv:2502.05259, Table 2]. The outer-disc
ellipse is chosen so that corrections stay at or below 0.05 mag and internal
reddening is negligible [src: arXiv:2502.05259, Sect. V.1.1].

CCHP applies no artificial-star correction to the JAGB; it avoids crowded
regions instead through the radial cut of step 3 and finds the JAGB on
average 0.21 mag brighter inside the cut than outside it in its seven hosts
[src: arXiv:2408.03474, Sect. III.4.1].

### JAGB step 3. Choose the region
<!-- key: jagb-step-3-choose-the-region -->

**CCHP convergence algorithm** [src: arXiv:2408.03474, Sect. III.4.1]:

1. Colour-select JAGB stars; order them by deprojected galactocentric
   radius (centre, position angle and inclination from the Extragalactic
   Distance Database).
2. Measure the mode of the innermost 500 stars, then of stars 50 to 550,
   and so on in steps of 50, to the outermost 500. Stated reason for 500:
   it gives a 1% statistical distance [src: arXiv:2408.03474, Sect. III.4.1].
3. Smooth the derivative dm_JAGB/dR over one sixth of the points; the
   first zero crossing is the radial cut.
4. Guard against noise: beyond the cut, the extreme values of m_JAGB must
   lie within the median ± 2 sigma of the points; otherwise widen the
   smoothing. This was needed in M101, NGC 2442 and NGC 4258
   [src: arXiv:2408.03474, Sect. III.4.1].
5. Mask spiral arms that block convergence (M101, NGC 2442, NGC 4258,
   NGC 4639), while blinded; unmasking changes H0 by 0.3%
   [src: arXiv:2408.03474, Sect. III.4.1, App. A].
6. Reject hosts that never converge or keep < 500 stars: NGC 3972,
   NGC 4038, NGC 4424 [src: arXiv:2408.03474, Sects. III.4.1, III.5].

The algorithm replaces an earlier one with eight independent radial bins
that kept regions agreeing within 0.05 mag with the outermost bin; overlap
was introduced to see small features such as spiral arms, the zero crossing
to stop small fluctuations from pushing the cut outwards [src:
arXiv:2408.03474, Sect. III.4.1].

**SH0ES-side ellipses.** Li et al. fix one ellipse per host by hand (centre,
position angle, axis ratio, semi-major axis in their Table 2) and keep
stars outside it; NGC 4258 fields are used whole because they already lie
in the outer disc [src: arXiv:2502.05259, Table 2, Sect. II.2]. Their
objection to convergence: the two CCHP fields in NGC 4258, both beyond the
CCHP cut, differ by more than 4 sigma, so "the JAGB reference magnitude
does not level off with radius" [src: arXiv:2502.05259, Sect. V.1.1].

### JAGB step 4. Colour box and magnitude window
<!-- key: jagb-step-4-colour-box-and-magnitude-window -->

| Analysis | Colour box | Magnitude window | Place read |
|---|---|---|---|
| Madore & Freedman 2020, LMC, 2MASS system | 1.30 < J − K < 2.00 | none for the mean | arXiv:2005.10792, Sect. II |
| Milky Way purity survey, Lee boxes | 1.5 < (J − K_s)_0 < 2.0 | — | arXiv:2609.25412, Sect. III.3 |
| CCHP JWST | 2.4 < F115W − F444W < 3.2, or 2.3 < F115W − F356W < 3.0 | ± 0.75 mag about the mode for dispersion and error | arXiv:2408.03474, Sects. III.4, III.6.1 |
| SH0ES-side JWST | 1.0 < F150W − F277W < 1.5 (baseline) | ± 5 to 6 sigma of the luminosity function | arXiv:2502.05259, Sect. II.4 |

Reasons stated. The 1.30 blue edge in the LMC: almost all other populations
are bluer than J − K ~ 1.3; the red edge removes extreme carbon stars of the
"K branch" [src: arXiv:2005.10792, Sect. II]. The wide window of Li et al.:
the luminosity function has a dispersion of 0.4 to 0.5 mag, and a ± 0.75 mag
cut is a 1.5 to 2 sigma truncation that brings it to about 0.3 mag and
underestimates the error on a mean [src: arXiv:2502.05259, Sect. II.4].

### JAGB step 5. The statistic
<!-- key: jagb-step-5-the-statistic -->

**CCHP: mode.** Bin F115W in 0.01 mag, smooth with GLOESS at
sigma_s = 0.25 mag, take the peak [src: arXiv:2408.03474, Sect. III.4].
Stated reason: the mode is "the most robust to outliers", and in
low-reddening, uncrowded regions the luminosity function is close to a
Gaussian, so mode, mean and median should agree [src: arXiv:2408.03474,
App. C].

**SH0ES-side: middle of 25 variants.** Five statistics (median, clipped
mean, mode with sigma_s = 0.25 and 0.35, Gaussian-plus-quadratic model fit)
times five colour ranges (baseline 1.0–1.5, narrow 1.05–1.425, wide
0.95–1.575, blue-trimmed 1.05–1.5, red-trimmed 1.0–1.425 mag) [src:
arXiv:2502.05259, Table 3]. For each variant the host-minus-NGC 4258
difference is formed and the middle value is kept [src: arXiv:2502.05259,
Sect. III]. Stated reason: luminosity functions are asymmetric by an amount
that varies from galaxy to galaxy, and without knowing the population,
contamination and metallicity dependence "we cannot justify choosing one
method over another" [src: arXiv:2502.05259, Sects. II.4, V.1.4].

Other groups fit a modified Lorentzian and take its median, then calibrate
on the LMC or the SMC depending on whether the target's skew is LMC- or
SMC-like [src: arXiv:2408.03474, App. C; arXiv:2502.05259, Sect. V.1.4].

### JAGB step 6. Distance and its error
<!-- key: jagb-step-6-distance-and-its-error -->

Both tie each host to NGC 4258 and add the maser modulus (29.398 in Li et
al.; 29.40 ± 0.02 ± 0.02 in CCHP) [src: arXiv:2502.05259, Sect. III;
arXiv:2408.03474, Sect. III.7].

Li et al. (their Eq. 1):

    sigma_dist^2 = sigma_var^2 + sigma_A,N4258^2 + sigma_A,host^2
                   + sigma_stat,N4258^2 + sigma_stat,host^2

with sigma_var the standard deviation over the variants in distance,
sigma_A 15% of the foreground extinction, sigma_stat the largest error on
the mean over the variants; the 0.032 mag maser error is added once at the
H0 step [src: arXiv:2502.05259, Sect. III, Eq. 1].

CCHP statistical terms: error on the mode (dispersion over sqrt(N) within
± 0.75 mag, 0.01 mag in every host); smoothing error, the largest change of
the mode for sigma_s from 0.15 to 0.40 mag, host and NGC 4258 in quadrature;
convergence error, the scatter of m_JAGB beyond the cut over sqrt(number of
bins), 0.002 to 0.005 mag. Systematic terms: 0.02 mag aperture correction;
foreground extinction at 16% of A_F115W when A > 0.1 mag, half of A when
A < 0.02 mag [src: arXiv:2408.03474, Sects. III.6.1, III.6.2]. The
Gaussian assumption behind the error on the mode was tested by splitting
~2800 stars of NGC 4536 into five radial bins: measured errors 0.013 to
0.015 against 0.014 mag expected [src: arXiv:2408.03474, Sect. III.6.1].

### Mira step 1. Time series and period search
<!-- key: mira-step-1-time-series-and-period-search -->

The M101 analysis combines eight archival HST WFC3/IR epochs (2014–2017,
F110W and F160W, cadence 58 to 220 d) with five new ones on a power-law
cadence of 20 to 124 d designed against aliasing; the total baseline is
2871 d and up to 13 epochs per star [src: arXiv:2312.08423, Sect. II.1].
Photometry: DAOPHOT/ALLSTAR on stacks, ALLFRAME with a fixed source list
for the time series [src: arXiv:2312.08423, Sect. II.3]; epoch zero points
from 500 bright stars (offsets 0.0008 to 0.01 mag) [src: arXiv:2312.08423,
Sect. II.4].

Selection [src: arXiv:2312.08423, Sects. III.1, II.2]:

1. Welch-Stetson index L > 0.75 among sources with at least 10 epochs
   [src: arXiv:2312.08423, Sect. III.1].
2. At least 9 F160W epochs; periods by chi^2 on a grid of 100 to 1000 d,
   sine fit with free amplitude, mean and phase (3960 light curves)
   [src: arXiv:2312.08423, Sect. III.1].
3. F-test: sinusoid preferred over a first-order polynomial.
4. Amplitude 0.4 < Delta F160W < 0.8 mag; initial period 200 < P < 500 d
   [src: arXiv:2312.08423, Sect. III.1, Table 2].
5. Colour F110W − F160W < 1.3 to drop the reddest, likely carbon-rich
   stars: 324 candidates [src: arXiv:2312.08423, Sect. III.1].

Why F110W rather than F125W: wider separation from F160W and broader band
for signal-to-noise, hence "somewhat better" C/O separation [src:
arXiv:2312.08423, Sect. II.2]. The 500 d upper limit was allowed by the
long baseline; earlier hosts stopped at 400 d because their baselines were
~400 d and because longer-period Miras may undergo hot-bottom burning
[src: arXiv:2312.08423, Sect. III.1].

| Cut | M101 | NGC 1559 | NGC 4258 (gold) |
|---|---|---|---|
| Period | 200 < P < 500 d | 240 < P < 400 d | P < 300 d |
| Amplitude in F160W | 0.4–0.8 mag | 0.4–0.8 mag | 0.4–0.8 mag |
| Colour | F110W − F160W < 1.3 | — | F125W − F160W < 1.3 |
| Other | F-test | surface brightness < 421 counts/s; F-test | F814W detection > 3 sigma, F814W amplitude > 0.3 mag |

[src: arXiv:2312.08423, Table 2]

### Mira step 2. Crowding and blending
<!-- key: mira-step-2-crowding-and-blending -->

Candidates within one FWHM (2.5 pixels) of a source as bright or brighter
are removed as blends (36 objects), because blending is not corrected by
artificial-star tests [src: arXiv:2312.08423, Sect. III.2]. For the others,
an artificial star at the magnitude predicted by the preliminary PL is
dropped within 20 pixels of each Mira, one per Mira per image over 100
images, and the cycle (correct, refit, re-inject) is iterated to
convergence [src: arXiv:2312.08423, Sect. III.2]. In M101 the corrections
are small but skewed (mean 0.076, median 0.047, sigma 0.171 mag), so a
correction is drawn per star in a bootstrap Monte Carlo and the PL is
refitted with 3 sigma clipping each time; mean-correction linear regression
gives the same modulus [src: arXiv:2312.08423, Sects. III.2, VI.2].

### Mira step 3. Period range and PL fit
<!-- key: mira-step-3-period-range-and-pl-fit -->

The usable period range is set empirically with a 75 d boxcar of PL zero
points: flat for 260 to 400 d in M101; brighter at short periods
(incompleteness, the faint side of the PL is missed) and fainter at long
periods (carbon-rich contamination) [src: arXiv:2312.08423, Sect. III.3].
The baseline uses 240 < P < 400 d in M101 and 260 < P < 400 d in NGC 1559
[src: arXiv:2312.08423, Sect. V.2].

The PL has a fixed slope (their Eq. 2):

    m_F160W = a − 3.35 (log P − 2.3)   (arXiv:2312.08423, Eq. 2)

the H-band slope from LMC data transformed to F160W; a second, LMC-based
slope gave results within ~0.02 mag in earlier hosts [src:
arXiv:2312.08423, Sect. III.4]. Per-star error: sigma_tot^2 = sigma_int^2 +
sigma_phot^2 (Eq. 3), sigma_int ~ 0.13 mag, sigma_phot 0.02 to 0.1 mag
[src: arXiv:2312.08423, Eq. 3]. No Wesenheit index: without K, W_JH has
more scatter than H alone [src: arXiv:2312.08423, Sect. IV.1].

**Carbon-rich contamination.** HST wide NIR bands cannot separate C- and O-rich Miras, so the bias is
modelled: LMC J and H Miras are converted with
m_F160W = m_H + 0.39 (m_H − m_J) (Eq. 4); the zero point of a mixed LMC
sample in 50 d bins, Z_LMC(P), is fitted to the host with
Z_host(P) = alpha Z_LMC(P) + beta (Eq. 5) [src: arXiv:2312.08423,
Sect. III.5]. In M101, alpha = 0.19 ± 0.16 (0.67 ± 0.23 without the last
bin), neither better than no dependence, so no correction is applied; the
whole LMC mixed-minus-O-rich difference in the relevant period range is
0.025 mag [src: arXiv:2312.08423, Sect. III.5]. Stated reason that the
correction is small in hosts: metal-rich galaxies are dominated by O-rich
stars [src: arXiv:2312.08423, Sects. III.5, IV.2].

### Mira step 4. Zero point and SN calibration
<!-- key: mira-step-4-zero-point-and-sn-calibration -->

Two-anchor form (M101 paper): a_0 = −6.30 ± 0.053 from the LMC and
−6.28 ± 0.043 from NGC 4258, weighted mean −6.29 ± 0.033 mag (Eq. 7), after
updating the F160W Vega zero point from 24.6949 to 24.662 mag [src:
arXiv:2312.08423, Sect. V.1]. Per host, Delta S = a_host − m_B^0 (Eq. 8);
M_B^0 = a_0 − mean(Delta S) (Eq. 9) = −19.27 ± 0.09 mag with
mean(Delta S) = 12.981 ± 0.082 mag from NGC 1559 and M101 [src:
arXiv:2312.08423, Sect. V.2]. H0 then follows from Eq. 5 of SH0ES with its
a_B, as for every ladder (`physics-and-methods.md#formalism-sh0es`).

Three-anchor form (cluster Miras): 41 O-rich Miras in globular clusters,
ground JHK_s converted to F160W with F160W = H + 0.39 (J − H), give
M_F160W = −6.27(0.02) − 2.76(0.18)(log P − 2.3) (Eq. 3) [src:
arXiv:2507.10658, Sect. IV.1]. A global slope over clusters, LMC and
NGC 4258 (P < 400 d) is −3.29 ± 0.07, and with a metallicity term

    M_F160W = −6.29(0.02) − 3.29(0.07)(log P − 2.3)   (arXiv:2507.10658, Eq. 4)
              + 0.09(0.04)([Fe/H] − [Fe/H]_mean),  [Fe/H]_mean = −0.42   (arXiv:2507.10658, Eq. 4, Sect. IV.2)

[src: arXiv:2507.10658, Sect. IV.2, Eq. 4]. Because the anchor
metallicities are approximations (LMC −0.7 ± 0.1 from age-metallicity
relations; NGC 4258 −0.10 ± 0.15 from H II regions; no Mira metallicities
in SN hosts), the term is not used; instead a metallicity systematic is
added per anchor [src: arXiv:2507.10658, Sect. IV.2]. Zero points with the
fixed slope: clusters −6.294 ± 0.056, LMC −6.319 ± 0.058, NGC 4258
−6.289 ± 0.051, Milky Way field −6.242 ± 0.071 (excluded: mean parallax
error 6%); adopted a_0 = −6.290 ± 0.029 mag [src: arXiv:2507.10658,
Sect. IV.2].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Mode or middle of variants
<!-- key: mode-or-middle-of-variants -->

Same data, two procedures. Re-measuring the CCHP photometry, Li et al.
reproduce the CCHP modes to better than 0.01 mag, yet their host distances
differ by 0.05 mag on average, because the middle of variants puts
NGC 4258 ~0.05 mag fainter than its mode [src: arXiv:2502.05259, Sect. III].
On the full JWST sample, the middle gives 73.3 ± 1.4 and the mode alone
71.2 ± 1.4 [src: arXiv:2502.05259, Sect. IV.1]. In CCHP's own test, mean
and median give moduli 0.030 ± 0.010 and 0.026 ± 0.007 mag closer than the
mode (H0 larger by 1.4% and 1.2%), which CCHP treats as covered by its
0.04 mag smoothing error in NGC 4258 and by a 2% floor in its budget [src:
arXiv:2408.03474, App. C]. Against HST Cepheids in F150W, the mode gives
the distances closest to Cepheids, while in the J band the mean best
reproduces the geometric LMC–SMC difference [src: arXiv:2502.05259,
Sect. V.2]. No metric among skew, mode − mean and J-region slope was found
that standardises the variation; a 0.06 mag floor (~2.0 in H0) is adopted
[src: arXiv:2502.05259, Sect. IV.2].

### Combined or separate anchor fields
<!-- key: combined-or-separate-anchor-fields -->

CCHP measures NGC 4258 on its two fields combined (m_JAGB = 23.44, M_JAGB
= −5.98 ± 0.05 ± 0.04 mag); separately, 23.41 ± 0.04 (inner, ~2300 stars)
and 23.51 ± 0.06 (outer, ~600 stars), "within 1.2 sigma" [src:
arXiv:2408.03474, Sect. III.7, Table 5]. Li et al. find the same difference
at more than 4 sigma, 0.11 ± 0.022 mag, with a smaller error, and call it
"the leading systematic error in JAGB absolute distances" [src:
arXiv:2502.05259, Sect. III]. The two significances differ through the
error assigned to each field: CCHP adds the smoothing error to the error on
the mode [src: arXiv:2408.03474, Sect. III.7]; the place where Li et al.
compute 0.022 mag was not read.

### Which zero point
<!-- key: which-zero-point -->

CCHP uses NGC 4258 alone. A preliminary transfer from 2MASS J through M33
(J(F115W) = J(2MASS) + 0.205 mag, interpolated between ground J and HST
F110W) puts the LMC, SMC and Milky Way calibrations at −6.015, −5.975 and
−5.985 ± 0.04 mag in F115W, and their mean with NGC 4258 at
−5.99 ± 0.015 (stat), 0.005 mag brighter than the NGC 4258 value; JWST
saturates on Magellanic Cloud JAGB stars [src: arXiv:2408.06153, App. A].

### Mira anchors: two or three
<!-- key: mira-anchors-two-or-three -->

Adding the cluster anchor leaves a_0 unchanged (−6.290 against −6.29) but
moves the metallicity systematic into the anchor term and lowers the M_B^0
error by 14%; the total stays dominated by the 2.3% from two SN
calibrators [src: arXiv:2507.10658, Sect. IV.4]. The Milky Way field
Miras are excluded in both papers: Gaia parallaxes of bright, red,
resolved AGB stars are underestimated by ~30–80% in their errors [src:
arXiv:2312.08423, Sect. V.1].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| NGC 4258 zero point, F115W | −5.98 ± 0.05 ± 0.04 mag | CCHP | arXiv:2408.03474 | Table 5 |
| NGC 4258 budget: smoothing; aperture; NIRCam zero point; A_F115W | 0.04; 0.02; 0.02; 0.01 mag | CCHP | arXiv:2408.03474 | Table 5 |
| H0 with 3 non-converged hosts added | 68.75 ± 2.23 ± 1.65 | CCHP JAGB, CSP | arXiv:2408.03474 | Sect. III.8 |
| Luminosity-function dispersion, wide window | 0.4–0.5 mag (≈ 0.3 with ± 0.75) | JAGB 2.0 | arXiv:2502.05259 | Sect. II.4 |
| JAGB hosts with JWST distances | 13 (about a third of the HST Cepheid sample) | JAGB 2.0 | arXiv:2502.05259 | Sect. V.2 |
| J-region slopes in F115W | significant at 1 to 7 sigma | JAGB 2.0 on CCHP data | arXiv:2502.05259 | Sect. V.1.3 |
| Carbon-Mira contamination of the J region | upper estimate ~0.1 mag | JAGB 2.0 | arXiv:2502.05259 | Sect. V.1.2 |
| Single-epoch / time-averaged JAGB scatter | 0.27 / 0.15 mag; 200 stars for 1% | LMC | arXiv:2005.10792 | Sect. IV |
| Milky Way purity against blue edge | 79% contamination at 1.30, 76% at 1.50, 52% at 1.60 | CHASE | arXiv:2609.25412 | Table 6 |
| Ground JAGB − HST TRGB (13 galaxies) | 0.17 ± 0.04 ± 0.06 mag; 0.21 ± 0.04 with ANGST TRGB | ground JAGB | arXiv:2502.07882 | Sects. II, III |
| Mira intrinsic PL scatter, NIR | ~0.13 mag | M101 | arXiv:2312.08423 | Eq. 3 |
| Mira sample, M101 | 211 Miras, 200–500 d | M101 | arXiv:2312.08423 | Sect. VI.1 |
| Mira modulus, M101 | 29.10 ± 0.06 | M101 | arXiv:2312.08423 | Eq. 13 |
| Mira metallicity allowance | ~0.03 mag statistical | M101 | arXiv:2312.08423 | Sect. IV.2 |
| Mira error budget: anchors; PL in hosts; SNe (2); m–z; slope; extinction | 0.030; 0.019; 0.069; 0.0085; 0.01; 0.02 mag; total 0.081 (3.7%) | cluster Miras | arXiv:2507.10658 | Table 6 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Inner-disc bias (JAGB).** The mode is brightest in the inner,
  high-surface-brightness regions, 0.21 mag on average in CCHP hosts;
  shows up as a radial trend of m_JAGB. Test: the convergence plot, or
  crowding corrections kept below 0.05 mag [src: arXiv:2408.03474,
  Sect. III.4.1; arXiv:2502.05259, Sect. V.1.1].
- **Asymmetric luminosity function.** Mean, median and mode split by up to
  0.2 mag in one field; shows up as variant-to-variant spread. Test: run
  all 25 variants and report their spread; the spread partly cancels
  between host and anchor because asymmetries share a sign [src:
  arXiv:2502.05259, Sects. II.4, II.5].
- **Contaminants in the colour box.** Carbon Miras sit mostly on the faint
  side of the J region [src: arXiv:2502.05259, Sect. V.1.2]; J- and N-type
  carbon stars have distinct means [src: arXiv:2502.05259, Sect. V.1.4];
  near solar metallicity three quarters of the box is oxygen-rich in the
  solar neighbourhood, a number the authors decline to extrapolate to
  other metallicities [src: arXiv:2609.25412, Sects. III.3, IV.4]. Test:
  spectroscopy; colour-edge scans (Table 6 of arXiv:2609.25412).
- **Incompleteness at ~40 Mpc.** NGC 3147 dropped; NGC 5468 needed
  incompleteness corrections and binned statistics [src: arXiv:2502.05259,
  Sect. II.4]. Test: artificial-star completeness curves (their App. B).
- **Ground-based crowding or calibration.** Ground JAGB distances to
  nearby galaxies are long by ~0.17 mag against three independent HST
  TRGB pipelines; ground NIR-TRGB is also offset by 0.12 mag, pointing to
  calibration as well as crowding [src: arXiv:2502.07882, Sect. III].
  Do not mix ground and JWST JAGB distances without this cross-check.
- **Mira period aliasing and baseline.** Baselines of ~400 d cap the
  period range; uneven cadences alias. Test: power-law cadence, phased
  composite light curves over 6 to 15 cycles [src: arXiv:2312.08423,
  Sects. II.1, VI.1].
- **Mira incompleteness and hot-bottom burning.** Zero point brightens
  below the completeness limit and fades at long periods. Test: boxcar
  zero point against period [src: arXiv:2312.08423, Sect. III.3].
- **Mira blends and band transfer.** Blends survive artificial stars:
  drop stars with a bright neighbour within one FWHM [src: arXiv:2312.08423,
  Sect. III.2]; ground anchors carry 0.02 mag for H to F160W [src:
  arXiv:2507.10658, Table 6].

## Reading list
<!-- key: reading-list -->

- Madore & Freedman 2020, arXiv:2005.10792 (foundation): LMC colour box and
  why its edges sit where they do; single-epoch scatter.
- Lee et al. 2024, arXiv:2408.03474 (method, CCHP): photometry, the
  convergence algorithm, error terms, the NGC 4258 zero point, mode against
  mean. [src: Sect. II]
- Freedman et al. 2024, arXiv:2408.06153 (application, CCHP): JAGB in the
  H0 analysis; App. A for a 2MASS-to-F115W zero-point transfer.
- Li et al. 2025, arXiv:2502.05259 (method, SH0ES side): crowding grid, 25
  variants, Eq. 1, field-to-field difference, J-region slopes, carbon
  Miras.
- Anand 2025, arXiv:2502.07882 (critique): ground JAGB against HST TRGB.
- Li et al. 2026, arXiv:2609.25412 (critique): spectroscopic purity of the
  colour box.
- Huang et al. 2024, arXiv:2312.08423 (method and application): Mira
  cadence, selection, crowding, boxcar, carbon-star model, Delta S.
- Bhardwaj et al. 2025, arXiv:2507.10658 (method): cluster Miras, global
  slope, metallicity term, budget.
- Huang et al. 2018, arXiv:1801.02711 (foundation): the HST NIR Mira PL in
  NGC 4258 (abstract read for L2; its body was not read here).

## Not verified
<!-- key: not-verified -->

- The first JAGB analysis of the SH0ES fields (the paper cited as [28] in
  arXiv:2502.05259), whose variants arXiv:2502.05259 adopts, and the CCHP
  photometry paper (Jang et al., in preparation in arXiv:2408.03474).
- How Li et al. (arXiv:2502.05259) compute the error of the NGC 4258
  field difference.
- The threshold of the F-test in the Mira selection of arXiv:2312.08423: the
  dossier gave chi^2_s / chi^2_l below a fixed ratio, which was not found in
  the HTML body on 2026-10-24.
- The Mira analysis of NGC 1559 (cited as [29] in arXiv:2312.08423): its
  surface-brightness cut and period-range test were read only through
  Table 2 and Sect. III.3 of arXiv:2312.08423.
- The papers that introduced the modified-Lorentzian and
  Gaussian-plus-quadratic JAGB fits; JWST Mira programmes, if any.
