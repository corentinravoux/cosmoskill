# Physics and methods — how H0 is measured, route by route

Scope: observables, estimators, defining equations, models in use, likelihood
and blinding practice, and public codes for the local distance ladder, the
ladder-independent routes, and the early-Universe / inverse-ladder inference
of the Hubble constant.
Snapshot: 2026-10-13

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. Equations without a flag are textbook
definitions.

## 1. What "H0" means in each route
<!-- key: what-h0-means-in-each-route -->

H0 is not one observable. Verde, Schöneberg & Gil-Marín (2023,
arXiv:2311.13305) count more than a dozen H0's that agree only if the data are
free of systematics and the cosmological model is right, and note that the
values cluster in a low (68) and a high (73) camp: the shape of the expansion
history agrees with the model, the normalisations disagree `[src]`.

| Route | What is measured | What H0 then depends on |
|---|---|---|
| Three-rung ladder | SN Ia absolute magnitude M_B^0, then the Hubble-diagram intercept | geometry of the anchors; low-z kinematics (q0) only |
| Two-rung ladder | stellar distances + host redshifts at cz of a few 1000 km/s | the peculiar-velocity field and sample selection |
| Megamasers | angular-diameter distance from disc dynamics + redshift | peculiar velocities of a handful of galaxies |
| Time delays | time-delay distance D_dt | lens mass profile (mass-sheet degeneracy), Omega_m weakly |
| Standard sirens | GW luminosity distance + redshift | inclination, host velocity, population model |
| Cosmic chronometers | dz/dt, hence H(z) | stellar-population models; extrapolation to z = 0 |
| CMB | angular acoustic scale theta_* | the full model (LCDM) and pre-recombination physics |
| BAO + BBN | h r_d from BAO, r_d from omega_b | pre-recombination physics, late-time model |
| Inverse ladder | SN relative distances anchored on BAO | r_d only; no dark-energy model |

The point that most often decides whether a statement is right: the ladder
measures M_B^0, and the conversion to H0 uses the SN magnitude-redshift
relation itself, so the "CMB versus distance ladder" tension is insensitive to
the late-time expansion history (Efstathiou 2021, arXiv:2103.08723;
Efstathiou 2026, arXiv:2607.29562) `[src]`.

## 2. The three-rung distance ladder
<!-- key: the-three-rung-distance-ladder -->

### 2.1 Formalism (SH0ES)
<!-- key: formalism-sh0es -->

Taken from Section 2.1 of Riess et al. (2022, arXiv:2112.04510) `[src]`;
the equation numbers below are those of that paper. SH0ES cites Leavitt &
Pickering (1912, Harvard College Observatory Circular 173; no DOI, not in
`sources.tsv`) for the period-luminosity law and Madore (1982,
doi:10.1086/159659) for the reddening-free Wesenheit magnitude `[sec]`.
Review of the methods and their systematics up to 2010: Freedman & Madore
(arXiv:1004.1856).

Distance modulus: mu_0 = m_0 - M_0 = 5 log D + 25, D in Mpc.

Cepheid j in host i, in the NIR Wesenheit system:

    m^W_H,i,j = mu_0,i + M^W_H,1 + b_W (log P_i,j - 1) + Z_W [O/H]_i,j   (Eq. 1)

with M^W_H,1 the absolute magnitude at P = 10 d and solar metallicity, b_W the
period slope and Z_W (called gamma elsewhere) the metallicity term.

Wesenheit magnitude (Section 3.4 of the same paper) `[src]`:

    m^W_H = m_F160W - R (m_F555W - m_F814W),   R = A_H / (A_V - A_I)   (Eq. 7)

The baseline R is 0.386, from the Fitzpatrick (1999) law with R_V = 3.3
`[src: Sect. 6.3]`. R is about 0.4 for standard extinction laws; the intrinsic colour-luminosity
relation at fixed period has a slope of about 0.6 in the same sense, so the
same combination also narrows the instability-strip scatter `[src]`.

SN Ia in a Cepheid host: m^0_B,i = mu_0,i + M^0_B (Eq. 3).

Hubble-flow intercept:

    a_B = log{ cz [1 + (1 - q0) z / 2 - (1 - q0 - 3 q0^2 + j0) z^2 / 6] } - 0.2 m^0_B   (Eq. 4)

    log H0 = 0.2 M^0_B + a_B + 5   (Eq. 5)

In the limit z ~ 0, a_B = log cz - 0.2 m^0_B. In 2016 M^0_B and a_B were
fitted separately; since 2022 Eqs. 3 and 5 are optimised simultaneously
because calibrator and Hubble-flow SNe share covariance `[src: Sect. 2.1]`.

The measurement is therefore Gaussian in 5 log H0 and slightly skewed in H0:
5 log H0 = 9.318 ± 0.031, i.e. -0.98 / +1.03 `[src]`.

An anchor enters as an external constraint (Eq. 2):
M^W_H,j = m^W_H,N4258,j - mu_0,N4258 + Delta mu_N4258, with the extra
equation 0 = Delta mu_N4258 ± sigma(mu_0,N4258): its Cepheid magnitudes are
converted with the geometric modulus plus a nuisance offset Delta mu
constrained by the anchor's error. This lets several anchors and several
indicators share one geometric constraint with their covariance tracked.

The fit is linear: data vector y, covariance C, design matrix L, parameters q,
with chi^2 = (y - Lq)^T C^-1 (y - Lq) (Eq. 6), best fit
q = (L^T C^-1 L)^-1 L^T C^-1 y and parameter covariance (L^T C^-1 L)^-1; the
last entry of q is 5 log H0. The free parameters are the host distances plus
the fiducial Cepheid and SN Ia luminosities, b_W, Z_W and H0 (and the anchor
offsets, the M31 modulus and a ground-HST zero-point offset in the parameter
vector) `[src: Sect. 2.1]`. C carries three kinds of off-diagonal terms: the
crowding-background floor between Cepheids of one host (Eq. 8), the
metallicity-scale covariance (Eq. 9) and the SN covariance between
calibrators and Hubble flow `[src: Sect. 2.1]`. The fit is cross-checked with
MCMC (emcee, 100 walkers, more than 120 million samples to trace the 5 sigma
tail) `[src]`.

Samples and cuts of the 2022 baseline (arXiv:2112.04510):

| Item | Value | Place | Flag |
|---|---|---|---|
| Fit quality | chi^2/dof = 1.03, 3445 degrees of freedom | Sect. 5 | [src: Sect. 5] |
| Calibrators | 42 SNe Ia in 37 Cepheid hosts | Sect. 5 | [src: Sect. 5] |
| Hubble flow | 277 SNe Ia, 0.0233 < z < 0.15, Pantheon+ | Sect. 5 | [src: Sect. 5] |
| Hubble-flow hosts | visually classified spirals Sa to Sd, inclination below 75 degrees, to match the calibrators | Sect. 6.8 | [src: Sect. 6.8] |
| SN cuts | abs(c) <= 0.15, abs(x1) < 2, first epoch earlier than 5 d after maximum, distance error <= 0.2 mag, 3.5 sigma outliers removed | Sect. 6.8 | [src: Sect. 6.8] |
| Without the host cut | 482 SNe, H0 unchanged (Fit 33); to z < 0.8, more than 1300 SNe, +0.5 (Fit 34) | Sect. 6.8 | [src: Sect. 6.8] |
| Cepheid periods | none below 5 d; single slope, no break | Sect. 6.4 | [src: Sect. 6.4] |
| Anchor priors | NGC 4258 29.398 ± 0.032; LMC 18.477 ± 0.0263; SMC as LMC-SMC = 0.500 ± 0.017 mag; MW parallaxes | Sect. 4.7 | [src: Sect. 4.7] |
| Best fit | b_W = -3.299 ± 0.015 mag/dex; Z_W = -0.217 ± 0.046 mag/dex; M^W_H,1 = -5.894 ± 0.017; M^0_B = -19.253 ± 0.027 | Sect. 5 | [src: Sect. 5] |
| Anchor offsets | Delta mu_N4258 = -0.013 ± 0.022; Delta mu_LMC = 0.010 ± 0.019 mag | Sect. 5 | [src: Sect. 5] |
| H0 | 73.04 ± 1.01 from the fit; ± 1.04 with the variant dispersion | Sect. 5 | [src: Sect. 5] |

Other ladders, read in their bodies. CCHP (arXiv:2408.06153): 287 CSP SNe Ia
at z > 0.01 in the Hubble diagram, calibrators constraining the intercept
only `[src: Sect. X.3]`; 8-parameter MCMC (P0, P1, P2, beta, alpha, Vpec,
sigma, H0, plus a calibrator scatter) `[src: Sect. X.4]`; Cepheids minus
TRGB = -0.025 ± 0.021 mag over 17 common hosts, scatter 0.08 mag
`[src: Sect. IX.1]`. JAGB 2.0 applies Eq. 5 with an adopted intercept,
a_B = 0.71448 ± 0.0012 `[src: Sect. IV.1]` (arXiv:2502.05259); CATS writes
the same relation as its Eq. 8 (arXiv:2304.06693). H0DN uses
four Hubble-flow SN sets (Pantheon+ SALT2, CSP I + II with SNooPy, NIR,
BayeSN) `[src: Sect. III]` (arXiv:2510.23823).

### 2.2 The Local Distance Network generalisation
<!-- key: the-local-distance-network-generalisation -->

The H0 Distance Network (H0DN; arXiv:2510.23823) replaces the single chain by
a network: every geometric anchor, primary indicator and Hubble-flow tracer is
a node, and the solution is a generalised linear least-squares fit that is the
best linear unbiased estimator under the stated covariances `[src]`. The
indicators were voted into a "baseline" set and a set used for robustness
variants. Baseline: Gaia parallaxes, detached eclipsing binaries, NGC 4258
masers; Cepheids and TRGB; SN Ia, SBF and Hubble-flow masers `[src]`. The
baseline chi^2 is 0.9879 per degree of freedom for 119 degrees of freedom
`[src]`. As written in the paper: chi^2 = (Y - AX)^T C^-1 (Y - AX)
`[src: Eq. B1]`, with X holding log H0, the host and group moduli and one
reference magnitude per calibrator type; the baseline has 255 equations for
183 distinct measurements, so C is singular and is inverted with the
Moore-Penrose pseudo-inverse `[src: Sect. B.2]`. Each Hubble-flow tracer
class is first reduced to its intercept, which alone enters the network (the
quoted chi^2 excludes those degrees of freedom) `[src: Sect. IV]`; the
distance-redshift function is a cosmographic expansion at z < 0.15, with
mu = 5 log[D(z_HD) (1 + z_hel) / (1 + z_HD)] + 25 `[src: Eq. B17]`.
Assumptions stated: no special location, negligible evolution over a few
100 Myr, kinematic expansion in H0, q0, j0 `[src: Sect. II.1.2]`. Chen & Wang (2026, arXiv:2606.26831) present the same idea as a
"covariance network" with level-0 anchors, level-1 stellar indicators and
level-2 Hubble-flow probes.

### 2.3 Geometric anchors
<!-- key: geometric-anchors -->

| Anchor | Method | Precision | Citation | Flag |
|---|---|---|---|---|
| Milky Way Cepheids | Gaia EDR3 parallaxes + HST photometry of 75 Cepheids | 1.0% | arXiv:2012.08534 | [src] |
| Milky Way cluster Cepheids | mean Gaia parallax of > 300 stars per cluster, 17 Cepheids | offset -3 ± 4 microarcsec | arXiv:2208.01045 | [src] |
| LMC | 20 late-type detached eclipsing binaries, surface-brightness-colour relation calibrated to 0.8% | 1% | arXiv:1903.08096 | [src] |
| SMC | 15 late-type DEBs; core geometry modelled; 88 HST Cepheids | better than 2% | arXiv:2010.08754; arXiv:2404.08038 | [src] |
| NGC 4258 | VLBI positions, velocities and accelerations of H2O masers in a Keplerian disc | 1.5% | arXiv:1908.05625 | [src] [der] |

Gaia parallaxes carry a zero-point bias that depends on magnitude, colour and
ecliptic latitude; the Gaia team gives tentative correction formulae
(Lindegren et al. 2021, arXiv:2012.01742) `[src]`. SH0ES fits a residual
offset simultaneously with the period-luminosity relation.

Where each anchor comes from:

| Anchor | Founding or defining paper | What it states | Flag |
|---|---|---|---|
| NGC 4258 masers | Miyoshi et al. 1995, doi:10.1038/373127a0 | first disc model, 6.4 ± 0.9 Mpc from one VLBI epoch (Table 1 of arXiv:1908.05625) | [sec] |
| | Herrnstein et al. 1999, arXiv:astro-ph/9907013 | geometric distance from maser proper motions (31.5 microarcsec/yr) and accelerations in a thin Keplerian disc: 7.2 ± 0.3 Mpc | [src] |
| | Humphreys et al. 2013, arXiv:1307.6031 | 18 VLBI epochs, warped disc with eccentric orbits: 7.60 ± 0.17 ± 0.15 Mpc | [src] |
| LMC eclipsing binaries | Pietrzyński et al. 2013, arXiv:1303.2063 | late-type giant systems give both linear and angular sizes and avoid the modelling of hot early-type stars; 8 systems, 49.97 ± 0.19 ± 1.11 kpc (2.2%) | [src] |
| Gaia parallaxes | Lindegren et al. 2021, arXiv:2012.03380 | EDR3 astrometry: 34 months, five-parameter solutions, or six-parameter ones with a pseudocolour | [src] |
| | Riess et al. 2018, arXiv:1804.10655 | offset and distance scale fitted together, with DR2: -46 ± 13 microarcsec for Cepheids, a factor 2.5 lost in precision | [src] |

### 2.4 Primary (stellar) indicators
<!-- key: primary-stellar-indicators -->

**Cepheids.** Period-luminosity (Leavitt) law; young, in star-forming discs;
needs multi-epoch optical discovery plus NIR photometry. JWST resolves the
red-giant background in the NIR and lowers the PL dispersion by a factor of
2.5 `[src]` (arXiv:2401.04773), and to about 0.12 mag in a background-free
host `[src]` (arXiv:2509.01667).
The fit of the Milky Way sample is done in parallax space, where Gaia errors
are Gaussian, with an additive offset zp and a multiplicative luminosity
term `[src: Sect. III.1]` (arXiv:2012.08534).

**TRGB.** The helium-flash luminosity of low-mass red giants, measured as a
discontinuity in the I-band luminosity function of halo fields. Two
measurement families: edge detection on a smoothed luminosity function (CCHP)
and model fitting of the RGB + AGB luminosity function (EDD). The apparent tip
correlates with the "contrast ratio" (stars below versus above the tip), which
the CATS algorithm uses to standardise fields (Scolnic et al. 2023,
arXiv:2304.06693) `[src]`. HST reaches about 20 Mpc with the TRGB and JWST at
least 50 Mpc `[src]` (arXiv:2401.04776). JWST calibrations exist in F090W,
close to F814W
(Anand et al. 2024, arXiv:2401.04776), and in F115W with a colour correction
(Hoyt et al. 2025, arXiv:2503.11769) `[src]`. A Gaia-only calibration through
globular clusters gives M_I = -3.948 (Cruz Reyes et al. 2026,
arXiv:2602.15421) `[src]`.

**JAGB.** Carbon-rich AGB stars selected in a colour box (1.5 < J - K < 2.0),
assumed to have a constant J-band luminosity. The statistic (mode, mean,
median, model fit) is not standardised between groups and gives different
answers when the luminosity function is skewed (Li et al. 2025,
arXiv:2502.05259) `[src]`.

**Miras.** Oxygen-rich long-period variables with P < 400 d, NIR
period-luminosity relation; need year-long monitoring. Anchored on the LMC,
NGC 4258 and, since 2025, 41 Miras in 18 globular clusters with Gaia distances
(Bhardwaj et al. 2025, arXiv:2507.10658) `[src]`.

Where each indicator comes from, and how the main analyses define it:

| Indicator | Paper | What it states | Flag |
|---|---|---|---|
| TRGB | Lee, Freedman & Madore 1993, doi:10.1086/173334 | tip first defined as the maximum response of a one-dimensional Sobel filter {-2, 0, +2} on the I-band luminosity function (arXiv:2503.11769, Sect. IV.1.1) | [sec] |
| | Da Costa & Armandroff 1990, doi:10.1086/115500 | the colour of the giant branch traces metallicity (arXiv:2408.06153, Sect. VI.1) | [sec] |
| | arXiv:2408.06153 | physics: core helium flash at a core mass near 0.5 solar masses, for stars below about 2 solar masses | [src: Sect. VI.1] |
| | Freedman et al. 2019, arXiv:1907.05922; 2020, arXiv:2002.01550 | CCHP zero point on the LMC (DEB modulus 18.477), H0 = 69.8 ± 0.8 ± 1.7; the 2020 paper details the extinction method | [src] |
| | Jang et al. 2021, arXiv:2008.04181 | CCHP zero point on NGC 4258: tip at 25.347 ± 0.014 ± 0.042, M_F814W = -4.050 ± 0.028 ± 0.048 mag | [src] |
| | arXiv:2503.11769 | infrared tip fitted in two dimensions and standardised by colour: mu_i = m_i + beta (c_i - c_0) - M | [src: Eq. 8] |
| | arXiv:2304.06693 | CATS: each tip rectified to a contrast ratio R = 4, slope -0.021 ± 0.004 mag per unit R | [src: Sect. III.1] |
| JAGB | Madore & Freedman 2020, arXiv:2005.10792 | method introduced: ~3300 LMC stars give M_J = -6.22, the SMC -6.18 ± 0.01 ± 0.05, adopted -6.20 ± 0.01 ± 0.04 mag; single-epoch scatter 0.27 mag | [src] |
| | Nikolaev & Weinberg 2000, doi:10.1086/317048 | "J region" first identified in the LMC (arXiv:2408.06153, Sect. VI.2) | [sec] |
| | arXiv:2408.06153; arXiv:2502.05259 | bounded above by carbon burning at the base of the envelope, below by the absence of a third dredge-up; JWST box 1.0 < F150W - F277W < 1.5 | [src: Sect. VI.2; Sect. II.4] |
| Miras | Huang et al. 2018, arXiv:1801.02711 | HST route: 139 oxygen-rich Miras in NGC 4258, scatter ~0.14 mag, mu_4258 - mu_LMC = 10.95 ± 0.01 ± 0.06 mag | [src] |
| SBF | Tonry & Schneider 1988, doi:10.1086/114847 | "A new technique for measuring extragalactic distances", cited as the origin by arXiv:2101.02221 and arXiv:2510.23823 | [sec] |
| Tully-Fisher | Tully & Fisher 1977 (no DOI, not in `sources.tsv`); Kourkchi et al. 2020, arXiv:2009.00733 | HI line width against luminosity, first used for distances in 1977 (arXiv:2510.23823, App. A.6); Cosmicflows-4: 9792 spirals within 15,000 km/s, 75.1 ± 0.2 (stat), systematics up to 3 | [sec] [src] |
| Fundamental Plane | Djorgovski & Davis 1987, doi:10.1086/164948; Dressler et al. 1987, doi:10.1086/164947; Said et al. 2024, arXiv:2408.13842 | introduced in 1987 ("a new distance estimator", titles confirmed); DESI fits it from velocity dispersions and Legacy Survey photometry | [sec] [src] |

### 2.5 Secondary indicators and the Hubble flow
<!-- key: secondary-indicators-and-the-hubble-flow -->

**SN Ia.** Standardised peak magnitudes with stretch, colour and host-mass
corrections; see `cosmo-supernovae`. The Pantheon+ compilation (1701 light
curves of 1550 SNe, z = 0.001 to 2.26) carries the covariance between
calibrator and Hubble-flow SNe (Brout et al. 2022, arXiv:2202.04077) `[src]`.

**SBF.** Pixel-to-pixel variance of an early-type galaxy image; reaches
100 Mpc with HST WFC3/IR, 4% per galaxy; calibrated on Cepheids or on TRGB
(Blakeslee et al. 2021, arXiv:2101.02221) `[src]`. It skips SN Ia.

**Tully-Fisher and Fundamental Plane.** Scaling relations with large
per-galaxy scatter but very large samples (origins in the table of
Section 2.4). The modern estimator fits the
relation and a peculiar-velocity model jointly (Boubel et al. 2024,
arXiv:2408.03660) `[src]`. DESI DR1 provides more than 100,000 FP + TF
distances; the zero point is still borrowed from SN Ia or SBF (Carr et al.
2025, arXiv:2512.03232) `[src]`.

**SN II.** Either as standardisable candles on the ladder or, without any
ladder, through the tailored expanding-photosphere method with radiative
transfer models (Vogl et al. 2025, arXiv:2411.04968) `[src]`.

### 2.6 Redshifts and peculiar velocities
<!-- key: redshifts-and-peculiar-velocities -->

The Hubble-flow sample is cut at z > 0.0233 to limit peculiar-velocity noise.
Redshifts are replaced by group redshifts where available and corrected with a
reconstruction of the local flow from 2M++; this lowers the Hubble-residual
scatter from 0.167 to 0.157 mag and raises H0 by about 0.4 (Peterson et al.
2022, arXiv:2110.03487) `[src]`. H0DN uses the 2M++ model in its baseline and
prefers tracers at z > 0.023 `[src]` (arXiv:2510.23823).

Two-rung ladders and megamasers work at cz of 1000 to 3000 km/s, where the
velocity field is the dominant term. The current practice is field-level:
condition on each posterior realisation of a constrained simulation
(Manticore-Local, BORG applied to 2M++; McAlpine et al. 2025,
arXiv:2505.10682) and marginalise (arXiv:2509.09665, arXiv:2609.29996). See
`cosmo-peculiar-velocities` for the reconstruction methods.

### 2.7 Statistical model: priors and selection
<!-- key: statistical-model-priors-and-selection -->

A 2025-2026 line of work treats the ladder as a hierarchical Bayesian model in
which each distance is a latent parameter. Two effects appear (Desmond et al.
2025, arXiv:2511.03394) `[src]`:

1. A uniform prior on distance modulus, often implicit, biases distances low
   because objects are distributed uniformly in volume, which biases H0 high.
   Frequentist chi^2 fits are unbiased for volume- or redshift-limited samples
   only when redshift errors vanish.
2. Selection adds a factor to the posterior (the probability of entering the
   sample) that partly cancels the volume prior.

Applying the prior without the selection term is inconsistent: it shifts the
Milky Way zero point by about 0.05 mag and fails posterior predictive checks
(Stiskalek et al. 2026, arXiv:2603.09880) `[src]`. Selection on one observable
while analysing a correlated one also biases the result (Percival 2026,
arXiv:2607.22425). The SH0ES pipeline corrects through simulation-based bias
terms rather than through the likelihood. This debate is open; see
`open-questions.md`.

## 3. Megamasers
<!-- key: megamasers -->

Water masers at 22 GHz in a thin, nearly edge-on, sub-parsec Keplerian disc
around a supermassive black hole. VLBI gives positions, line-of-sight
velocities and centripetal accelerations of the spots; a warped-disc model
returns the angular-diameter distance. For a systemic maser at radius r with
orbital velocity v and acceleration a = v^2 / r, D = r / theta. The fit for
NGC 4258 gives 7.576 Mpc (Reid et al. 2019, arXiv:1908.05625) `[src]`.
The Megamaser Cosmology Project applied the method to five galaxies in the
Hubble flow (UGC 3789, NGC 6264, NGC 6323, NGC 5765b, CGCG 074-064) plus
NGC 4258 (Pesce et al. 2020, arXiv:2001.09213) `[src]`. There the
likelihood is the product of a distance term (the disc-fit posteriors) and a
velocity term, with D(z) in flat LCDM at Omega_m = 0.315 and flat priors,
sampled with dynesty `[src: Sect. 3]`. Each spot gives sky offsets, Doppler
velocity and line-of-sight acceleration (Reid et al. 2019,
arXiv:1908.05625, Sect. II) `[src: Sect. II]`. A 2026 reanalysis
infers distance and disc parameters jointly from the spot catalogues with a
physical distance prior and a selection model (Stiskalek & Desmond 2026,
arXiv:2609.17684) `[src]`.

## 4. Time-delay cosmography
<!-- key: time-delay-cosmography -->

Time delay between images i and j of a variable source:

    Delta t_ij = (D_dt / c) [ phi(theta_i, beta) - phi(theta_j, beta) ],
    D_dt = (1 + z_d) D_d D_s / D_ds   (inversely proportional to H0)

with phi the Fermat potential. In TDCOSMO 2025 (arXiv:2506.03023) these are
Eq. 1 (delay), Eq. 2 (Fermat potential tau = (theta - beta)^2 / 2 - phi),
Eq. 3 (D_dt, attributed to Refsdal 1964) and Eq. 4 (H0 proportional to
1 / D_dt); the mass-sheet transform is Eq. 5, under which Fermat-potential
differences and predicted delays scale as lambda (Eqs. 6, 7)
`[src: Sect. 3, 3.1]`. The degeneracy is attributed to Falco et al. (1985)
and its generalisation to Schneider & Sluse (2013) `[sec]`
`[src: Sect. 2.2]`; it splits into an internal part, lambda_int, and an
external one, kappa_ext `[src: Sect. 3.1]`. The mass-sheet transformation
kappa -> lambda kappa + (1 - lambda) leaves image positions and flux ratios
unchanged and rescales H0 by lambda; in Kochanek's formulation H0 scales as
1 - kappa_E, the mean convergence at the Einstein radius, which lensing data
alone do not constrain (Kochanek 2020, arXiv:1911.05083) `[src]`. Stellar
kinematics of the deflector break the degeneracy, with
Delta H0 / H0 proportional to Delta sigma^2 / sigma^2 (Forés-Toribio et al.
2026, arXiv:2602.03934) `[src]`. The review is Birrer et al. (2024,
arXiv:2210.10833); an earlier one is Treu & Marshall (2016,
arXiv:1605.05333). Founding papers: Refsdal (1964,
doi:10.1093/mnras/128.4.307, "On the possibility of determining Hubble's
parameter and the masses of galaxies from the gravitational lens effect");
Falco, Gorenstein & Shapiro (1985, doi:10.1086/184422) for the degeneracy
`[sec]`; Suyu et al. (2010, arXiv:0910.2773), who marginalised the profile
slope and kappa_ext with priors and so turned the main systematics into
statistical errors `[src]`; Schneider & Sluse (2013, arXiv:1306.0901), who
showed that a composite lens can be reproduced by a power law whose H0
differs by about 20% `[src]`.

Current practice (TDCOSMO):

- Hierarchical inference: an internal mass-sheet parameter lambda_int per
  population, constrained only by kinematics, validated on hydrodynamical
  simulations (Birrer et al. 2020, arXiv:2007.02941) `[src]`.
- External non-time-delay lenses (SLACS, SL2S) add kinematic information if
  they are drawn from the same population as the time-delay lenses `[src]`.
- External convergence kappa_ext from the line-of-sight environment.
- Spatially resolved kinematics (Keck KCWI, JWST NIRSpec), with corrections
  for projection, rotation and anisotropy (arXiv:2506.03023,
  arXiv:2604.14145) `[src]`.
- The flat-LCDM H0 needs an Omega_m prior, taken from uncalibrated SNe
  (Pantheon+, DES-SN5YR) or DESI BAO; results are stable across the choice
  `[src]` (arXiv:2506.03023).

Cluster-lensed supernovae (Refsdal, H0pe, Encore) use the same equation with
cluster mass models; a lensed SN Ia adds absolute magnifications that break
the degeneracy between models (Pascale et al. 2025, arXiv:2403.18902) `[src]`.

## 5. Standard sirens and cosmic chronometers (summary)
<!-- key: standard-sirens-and-cosmic-chronometers-summary -->

The GW amplitude gives the luminosity distance without a ladder; the redshift
comes from a counterpart (bright siren: GW170817, Abbott et al. 2017,
arXiv:1710.05835) or statistically from galaxy catalogues and features of the
mass spectrum (dark and spectral sirens; LVK 2025, arXiv:2509.04348). Details
belong to `cosmo-multimessenger`.

Cosmic chronometers (proposed by Jimenez & Loeb 2002,
arXiv:astro-ph/0106145: the age difference of two ensembles of passively
evolving galaxies gives dz/dt, hence H0 at z < 0.2 `[src]`; review of the
emerging probes: Moresco et al. 2022, arXiv:2201.07241):
H(z) = -(1 + z)^-1 dz/dt from the differential ages of
massive passive galaxies; cosmology-independent but dependent on
stellar-population synthesis (Moresco 2024, arXiv:2412.01994). H0 follows only
after extrapolating H(z) to z = 0 with a model or a reconstruction.

## 6. Early-Universe and inverse-ladder inference
<!-- key: early-universe-and-inverse-ladder-inference -->

**CMB.** The acoustic scale theta_* = r_* / D_M(z_*) is measured to 0.03%
(100 theta_* = 1.0411 ± 0.0003) `[src]` (arXiv:1807.06209). Within flat LCDM,
omega_b and omega_c fix r_* and the only freedom left to match theta_* is H0.
The value is model-dependent by construction. See `cosmo-cmb`.

**BAO.** BAO measure distances in units of the drag-epoch sound horizon, so
BAO alone give h r_d. DESI uses

    r_d = 147.05 Mpc (omega_b / 0.02236)^-0.13 (omega_bc / 0.1432)^-0.23 (N_eff / 3.04)^-0.1

`[src]` (arXiv:2503.14738, Eq. 2). A BBN prior on omega_b then yields H0
without CMB anisotropies. See `cosmo-galaxy-clustering`.

**Inverse distance ladder.** SN Ia relative distances are anchored at high
redshift by BAO with r_d from the early Universe, and carried to z = 0 with a
model-agnostic expansion (cosmography or splines). It assumes standard
pre-recombination physics but not a dark-energy model or flatness (Aubourg et
al. 2015, arXiv:1411.1074) `[src]`. It returns M_B as well as H0, which makes
the tension visible as a mismatch of SN absolute magnitudes.
Earlier forms: BAO + SNe alone measure the ruler as 103.9 ± 2.3 Mpc/h with
only a smooth expansion history assumed (Heavens et al. 2014,
arXiv:1409.6217) `[src]`; the same ladder anchored either at z = 0 by the
local H0 or by the CMB sound horizon, the "inverse distance ladder" (Cuesta
et al. 2015, arXiv:1411.1094) `[src]`; r_s and H0 as the two anchors at
opposite ends, BAO + SNe fixing r_s h (Bernal et al. 2016,
arXiv:1607.05617) `[src]`. The sound horizon as a scale of the transfer
function: Eisenstein & Hu (1998, arXiv:astro-ph/9709112). BAO with a
deuterium prior and no CMB anisotropy: 66.98 ± 1.18 (Addison et al. 2018,
arXiv:1707.06547) `[src]`; with deuterium and helium, 3.2 sigma from SH0ES
in LCDM and 2.6 sigma with N_eff free (Schöneberg et al. 2019,
arXiv:1907.11594) `[src]`.

**Sound-horizon-free.** The matter-radiation equality scale k_eq in the
full-shape power spectrum, or CMB lensing with r_d marginalised, gives an H0
that responds differently to pre-recombination physics (Zaborowski et al.
2025, arXiv:2411.16677; García Escudero et al. 2025, arXiv:2509.16202).

**How the solutions are classified.** Since BAO + SNe fix the shape of the
low-z expansion, raising H0 requires lowering r_d by a matching fraction.
With h r_d = 101.54 Mpc, r_d would be 138.1 Mpc for h = 0.735 against 151.0
Mpc for h = 0.6724, a reduction of 8.5% `[der]` (flat LCDM BAO-only value
divided by h; ignores the Omega_m dependence). The least unlikely class of
models raises the expansion rate in the decade of scale factor before
recombination (Knox & Millea 2020, arXiv:1908.03663) `[src]`; reducing r_d
alone runs into BAO or weak-lensing data (Jedamzik et al. 2021,
arXiv:2010.04158) `[src]`. Model rankings: Schöneberg et al. (2022,
arXiv:2107.10291). Details belong to `cosmo-tensions-anomalies` and
`cosmo-dark-energy-modified-gravity`.

## 7. Blinding practice
<!-- key: blinding-practice -->

| Analysis | Blinding | Citation | Flag |
|---|---|---|---|
| CCHP JWST TRGB | catalogue cleaning, colour slope and tip detection blinded | arXiv:2503.11769 | [src] |
| SH0ES LMC Cepheids 2019 | measurements completed before the new LMC distance was known | arXiv:1903.07603 | [src] |
| H0LiCOW | all lenses but the first analysed blind to cosmological parameters | arXiv:1907.04869 | [src] |
| TDCOSMO 2025, XXV | analysis blinded until the pipeline was frozen | arXiv:2506.03023; arXiv:2604.14145 | [src] |
| Lensed SNe | Refsdal blinded; H0pe with a live unblinding; Encore double-blind | arXiv:2305.06367; arXiv:2403.18902; arXiv:2509.12301 | [src] |
| SPT-3G D1 | power spectra validated with blind tests | arXiv:2506.20707 | [src] |

The SH0ES Cepheid-SN fit itself is not blinded end to end; its defence is the
set of about 70 analysis variants (arXiv:2112.04510) `[src]` and, since 2025,
the independent H0DN software.

## 8. Public codes and data products
<!-- key: public-codes-and-data-products -->

| Product | What it is | Reference | Flag |
|---|---|---|---|
| SH0ES data vector y, covariance C, design matrix L | the full linear system of the 2022 fit, written in matrix form for transmission and reused by the reanalyses in `results.md` Section 6 | arXiv:2112.04510 | [src] |
| H0DN software and data products | network solver in IDL and Python, data files, one configuration file per variant of its Table 4; repository address in App. E, public on publication | arXiv:2510.23823, App. E | [src: App. E] |
| Pantheon+ light curves and covariance | 1701 light curves, used by SH0ES and H0DN | arXiv:2202.04077 | [src] |
| Extragalactic Distance Database, TRGB | about 400 hosts with a TRGB distance | as used in arXiv:2609.29996 | [src] |
| Cosmicflows-4 | 55,877 distances, eight methods | arXiv:2209.11238 | [src] |
| Manticore-Local | posterior realisations of the local density and velocity field | arXiv:2505.10682 | [src] |
| TDCOSMO hierarchical pipeline | lens models, kinematics, population inference | arXiv:2007.02941 | [src] |

Software names for lens modelling, light-curve fitting and Boltzmann codes are
in `cosmo-software-ecosystem`; none was verified in this session.

## 9. Conventions and where the community is split
<!-- key: conventions-and-where-the-community-is-split -->

- H0 in km/s/Mpc; h = H0 / 100. Distances in the ladder are quoted as moduli;
  1% in distance is 0.0216 mag `[der]`, and the tension is about 0.18 mag
  `[src]` (arXiv:2112.04510).
- Metallicity term: gamma or Z_W, in mag/dex, negative when metal-rich
  Cepheids are brighter. SH0ES uses [O/H]; stellar work uses [Fe/H].
- "Anchor" means a geometric distance; "calibrator" means an SN Ia with a
  primary-indicator distance; "Hubble flow" means z > 0.0233 in SH0ES usage.
- TDCOSMO quotes medians with 68% intervals in flat LCDM; LVK quotes medians
  with 68.3% symmetric intervals (older papers: maximum a posteriori).
- Split 1: frequentist chi^2 with simulation-based bias corrections (SH0ES,
  H0DN) versus hierarchical Bayesian forward models with explicit selection
  (Section 2.7).
- Split 2: prior on H0 versus prior on M_B when the ladder is combined with
  other data; the M_B form is the correct one (arXiv:2103.08723).
- Split 3: TRGB by edge detection versus luminosity-function fitting; JAGB by
  mode versus mean.
- Split 4: lens mass profiles assumed (power law) versus mass-sheet-free.

## Not verified
<!-- key: not-verified -->

- Reference papers of the lens-modelling and TRGB codes. TDCOSMO names glee
  and lenstronomy for lens models and PyCS3 for time delays `[sec]`
  (arXiv:2506.03023, Sect. 11.1); their papers are not in `sources.tsv`.
- The original Mira period-luminosity paper and Tully & Fisher (1977) were
  not read; Leavitt & Pickering (1912) has no DOI.
