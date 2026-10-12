# Systematics — what can bias an H0 measurement, how large, and how it is tested

Scope: the canonical systematic effects of the local distance ladder and of
the ladder-independent H0 routes; for each, the mechanism, the size where a
paper quantifies it, the standard mitigation, the validation test, and the
paper a referee expects to see cited.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. H0 in km/s/Mpc.

Scale to keep in mind: the SH0ES-Planck difference is 0.176 ± 0.035 mag in
5 log H0 `[src]` (arXiv:2112.04510, Sec. 5). A single effect must reach about
0.18 mag, coherently across all hosts, to remove the tension; 1% in H0 is
0.0216 mag `[der]`.

## 1. Cepheid crowding and blending

**Mechanism.** In HST NIR images of hosts tens of Mpc away a Cepheid sits on an
unresolved background of red giants. If the statistical background correction
were wrong in a distance-dependent way, distant Cepheids would look too
bright, distances too short, H0 too high.

**Mitigation.** Artificial stars are injected near each Cepheid at the
magnitude predicted by its period and the recovered offset corrects the
photometry, iteratively with the PL fit `[src]` (arXiv:2112.04510, Sec. 3.4).

**Size, measured.** JWST resolves the background. For more than 1000 Cepheids
in NGC 4258 and 5 SN hosts the HST minus JWST mean distance difference is
-0.01 ± 0.03 mag, and a crowding bias growing with distance is rejected as the
cause of the tension at 8.2 sigma `[src]` (Riess et al. 2024,
arXiv:2401.04773). Combining all JWST indicators, the linearity of HST
Cepheid distances is 0.994 ± 0.010 `[src]` (arXiv:2408.11770). In NGC 3447,
whose companion has no old stellar background, the two components agree
(sigma < 0.03 mag) and the PL scatter falls to about 0.12 mag; across 19 hosts
there is no bias relative to HST `[src]` (Riess et al. 2025,
arXiv:2509.01667).

**Validation test.** HST versus JWST for the same Cepheids, as a function of
distance and local surface brightness.

**Status.** Closed as an explanation of the tension. A text that still offers
crowding as a candidate is stale. Cite arXiv:2401.04773 and arXiv:2509.01667.

## 2. Cepheid metallicity dependence

**Mechanism.** Metal-rich Cepheids are brighter at fixed period. Anchors and
SN hosts have different mean abundances, so an error in the coefficient gamma
propagates to the zero point.

**Size.** gamma = -0.234 ± 0.052 mag/dex with the SMC doubling the metallicity
lever arm `[src]` (Breuval et al. 2024, arXiv:2404.08038); the 2019 SH0ES
value was -0.17 ± 0.06 `[src]` (as recalled in arXiv:2112.04510, Sec. 5).
Because the metallicities of anchors and hosts are similar in current ladders,
the value of gamma has little impact on H0; it matters for distances to
metal-poor dwarfs such as the Magellanic Clouds `[src]` (Breuval et al. 2025,
arXiv:2507.15936).

**The dispute.** Madore & Freedman argue for no measurable metallicity effect:
their 2026 analysis attributes the achromatic residuals of Milky Way Cepheids
to parallax errors and finds no significant correlation with metallicity over
-0.2 < [Fe/H] < 0.05 `[src]` (Madore & Freedman 2026, arXiv:2602.13397).
Breuval et al. (arXiv:2507.15936) reply that the underlying recalibration of
Gaia parallaxes by a magnitude offset is multiplicative in parallax, unlike
the additive Gaia-team correction, and, extrapolated, places the Pleiades too
close and leaves distant quasars with negative parallaxes `[src]`.

**Validation test.** Fit gamma across MW, LMC, SMC with one photometric
system; check the per-anchor H0 values agree (Section 4).

## 3. Gaia parallax zero point

**Mechanism.** Gaia EDR3 parallaxes are offset by a few tens of microarcsec,
depending on magnitude, colour and ecliptic latitude (Lindegren et al. 2021,
arXiv:2012.01742) `[src]`. Field Cepheids are bright (G < 8), outside the
range where the correction is best calibrated.

**Mitigation and size.** SH0ES fits a residual offset together with the PL
relation (arXiv:2012.08534). Cluster Cepheids use the mean parallax of more
than 300 fainter stars (G > 13) per cluster: residual offset -3 ± 4
microarcsec, and H0 = 72.8 ± 1.3 or 73.2 ± 1.1 from that sample alone with or
without marginalising the offset `[src]` (Riess et al. 2022,
arXiv:2208.01045).

**Where it is contested.** A "conservative" wide prior on the residual offset
is one of the two ingredients that move H0 to 70.6 in Högås & Mörtsell (2026,
arXiv:2601.22215) `[src]`.

**Next data.** Gaia DR4, 2 December 2026 (`surveys-and-data.md`).

## 4. Consistency of the geometric anchors

Each anchor alone must return the same H0. Values read this session:

| Anchor alone | H0 | Citation | Flag |
|---|---|---|---|
| NGC 4258 (2016) | 72.25 ± 2.51 | arXiv:1604.01424 | [src] |
| LMC, 8 DEBs (2016) | 72.04 ± 2.67 | arXiv:1604.01424 | [src] |
| MW, 15 parallaxes (2016) | 76.18 ± 2.37 | arXiv:1604.01424 | [src] |
| NGC 4258 (2019 distance) | 72.0 ± 1.9 | arXiv:1908.05625 | [src] |
| LMC, 20 DEBs (2019) | 74.22 ± 1.82 | arXiv:1903.07603 | [src] |
| MW, Gaia EDR3 (2021) | 73.0 ± 1.4 | arXiv:2012.08534 | [src] |
| SMC (2024) | 74.1 ± 2.1 | arXiv:2404.08038 | [src] |
| H0DN without NGC 4258 | 73.084 ± 0.920 | arXiv:2510.23823 | [src] |
| H0DN without Gaia parallaxes | 73.609 ± 0.929 | arXiv:2510.23823 | [src] |

**Critique to know.** Efstathiou (2020, arXiv:2007.10716) pointed to an
inconsistency between the LMC and NGC 4258 relative Cepheid distances in the
2016-2019 data and showed that a 0.1 to 0.15 mag bias in the PL intercept of
the SN hosts would reconcile SH0ES with the early Universe and with the CCHP
TRGB scale `[src]`. The JWST tests of Section 1 were designed to look for an
offset of that size and found none.

**Fragility of the JWST ladders.** Both JWST programmes use NGC 4258 as their
single anchor; its distance error (1.5%, 0.032 mag `[der]` from
arXiv:1908.05625) and the measurement error of each indicator in NGC 4258
enter every JWST H0 fully correlated. Comparisons that neglect the second term
overstate disagreements `[src]` (arXiv:2408.11770).

## 5. Extinction law and the Wesenheit colour term

**Mechanism.** The Wesenheit magnitude removes dust with a fixed R tied to a
Milky-Way-like law (R_V ~ 3.1), while SN Ia colours often prefer R_V ~ 2 in
their hosts.

**Size.** In the 2022 variants the lowest and highest H0 both come from
suboptimal dust treatment (dropping NIR data, or not using colours) `[src]`
(arXiv:2112.04510, Sec. 6.14). A direct measurement from background galaxies
seen through NGC 5584 gives R_V = 3.59 (+0.99/-0.62) (stat) ± 0.19 (syst),
more than 3.5 sigma from R_V = 2 `[src]` (Murakami et al. 2025,
arXiv:2503.09702); a statistical sample of 5 to 10 hosts is announced.

**Validation test.** NIR-only versus optical Wesenheit fits; R varied per
host only after subtracting intrinsic colours.

## 6. Statistical model: distance priors and selection

**Mechanism.** Distances are latent parameters. A flat prior in modulus
favours short distances; unmodelled sample selection has the opposite sign.
Both shift H0 at the level of the tension (Desmond et al. 2025,
arXiv:2511.03394) `[src]`.

**Sizes claimed.**

- Volume prior applied to all hosts and to MW Cepheids, plus a wide Gaia
  offset prior: 73.0 -> 70.6 ± 1.0 `[src]` (arXiv:2601.22215).
- Same prior on MW Cepheids without a selection model: a spurious ~0.05 mag
  zero-point shift; with the two HST selection functions and a Galactic disc
  prior, the PL parameters agree with SH0ES within 0.5 sigma `[src]`
  (Stiskalek et al. 2026, arXiv:2603.09880).
- Truncated selection on a correlated observable: one extra parameter for the
  Cepheid cut-off in SN hosts lowers H0 by 1.4; SN selection terms by 0.2; an
  equal-volume prior by 1.0; evidence for non-zero corrections is 1.3 to 2.3
  sigma `[src]` (Percival 2026, arXiv:2607.22425).

**Mitigation.** Either a full forward model with explicit selection, or
simulation-based bias corrections with realistic source and selection
distributions; the latter is the SH0ES practice and should already capture
both effects `[src]` (arXiv:2511.03394).

**Validation test.** Posterior predictive checks of the observed parallax,
magnitude and period distributions; mock ladders with known selection.

**What a referee asks.** How were the hosts selected, and is that selection
in the likelihood? The selection criteria of the SH0ES host sample, built
over three decades, are not fully documented; changing the assumption moves a
two-rung H0 from 71.8 to 77.0 `[src]` (Kenworthy et al. 2022,
arXiv:2204.10866).

## 7. SN Ia standardisation between calibrators and the Hubble flow

**Mechanism.** Calibrators live in nearby star-forming hosts; the Hubble-flow
sample must be matched in host type, survey and light-curve properties, or
differences in dust and intrinsic colour leak into M_B.

**Size.** SN systematics make up less than one third of the SH0ES error
budget `[src]` (Brout et al. 2022, arXiv:2202.04077). The dispersions of
calibrators (0.130 mag) and Hubble-flow SNe (0.135 mag) match `[src]`
(arXiv:2112.04510). A two-population model with separate dust laws finds an
R_B ~ 4 for the population that carries distances and H0 = 70.59 ± 1.15, or
71.45 ± 1.03 with equal priors `[src]` (Wojtak & Hjorth 2025,
arXiv:2506.22150). A corrected host-mass step changes 52 of 277 Hubble-flow
magnitudes and moves the H0DN value from 73.50 to 73.26 `[src]`
(arXiv:2607.24443).

**SN compilation dependence.** SN-related choices account for about 2.0 of
the difference between TRGB-based H0 values in the literature, a larger share
than the TRGB calibration itself (~1.4) `[src]` (Scolnic et al. 2023,
arXiv:2304.06693). In the CCHP JWST analysis, enlarging the calibrator set
from 11 to 24 raises H0 by 0.8 with CSP-II magnitudes and by 2 with Pantheon+
`[src]` (Hoyt et al. 2025, arXiv:2503.11769). H0DN reports consistent results
across four optical compilations and NIR-only magnitudes (H band: 72.459 ±
1.099; J band: 72.712 ± 1.164) `[src]` (arXiv:2510.23823).

**Validation test.** Replace SNe Ia altogether: without them H0DN gives
73.434 ± 1.795 `[src]`.

Light-curve models, calibration and host corrections: `cosmo-supernovae`.

## 8. Choice and size of the calibrator sample

**Mechanism.** With 10 to 20 calibrators the mean SN Ia magnitude fluctuates
by more than the systematic budget; which hosts were observed first matters.

**Size.** The 2.5 difference between the CCHP JWST subsample and the full HST
sample is consistent with subsample selection `[src]` (arXiv:2408.11770). The
11 TRGB hosts absent from the CCHP compilation alone give 74.1, 2 sigma above
the selected 24; a peculiar-velocity correction adds 0.6 `[src]` (Li et al.
2025, arXiv:2504.08921).

**Validation test.** Compare distances, not H0 values: for hosts in common,
HST Cepheids agree with JWST Cepheids, TRGB and JAGB at about 0.03 mag
`[src]` (arXiv:2408.11770).

## 9. Peculiar velocities and the definition of the Hubble flow

**Three-rung ladder.** Flow corrections from 2M++ plus group redshifts raise
H0 by about 0.4 relative to CMB-frame redshifts and leave a systematic of
0.06 to 0.11 `[src]` (Peterson et al. 2022, arXiv:2110.03487). In the SH0ES
variants, no flow correction lowers H0 by 0.5 and swapping 2M++ for 2MRS by
0.05 `[src]` (arXiv:2112.04510, Sec. 6.12). H0DN finds changes of up to 0.8
with the redshift selection of the SNe `[src]` (arXiv:2510.23823).

**Two-rung ladders and masers.** At cz of 1000 to 3000 km/s velocities
dominate: SH0ES estimated a 3 to 4% floor for a Cepheid-only H0 `[src]`
(arXiv:2112.04510, Sec. 6.12). For megamasers, a linear reconstruction lowers
H0 by 0.8 to 1.4 and the non-linear Manticore field by 1.6 to 2.1 `[src]`
(arXiv:2609.17684). For 400 TRGB hosts the scatter between posterior
realisations of the velocity field is 5.2 and a free velocity monopole is
5.4 ± 3.4 `[src]` (arXiv:2609.29996).

**Mitigation.** Marginalise over posterior realisations of a constrained
simulation, with the selection of the sample in the likelihood
(arXiv:2509.09665). Method details: `cosmo-peculiar-velocities`.

## 10. Local structure and sample variance

**Size.** Sample variance of the local H0 in LCDM with the actual SN
distribution is 0.31 `[src]` (Wu & Huterer 2017, arXiv:1706.09723); the
empirical SN constraint is 0.60% against 0.42% predicted, and density
contrasts above 27% on scales larger than 69 Mpc/h are excluded at 5 sigma
`[src]` (Kenworthy et al. 2019, arXiv:1901.08681). Explaining the tension
would need delta ~ -0.8 over a radius of ~150 Mpc `[src]` (arXiv:1706.09723).

**Validation test.** Fit H0 in redshift shells; fit a void profile to direct
distances (arXiv:2506.10518). See `open-questions.md` for the void debate.

## 11. TRGB-specific effects

- **Tip detection.** Edge-detection responses are multi-peaked; the measured
  tip correlates with the contrast ratio of the field. Algorithm choices add
  0.83 to the H0 error, and none of 108 variants gives H0 below 71.6 `[src]`
  (arXiv:2304.06693).
- **Zero point.** -4.01 ± 0.04 in F814W on NGC 4258 (arXiv:1908.05625);
  -4.362 ± 0.033 ± 0.045 in JWST F090W (arXiv:2401.04776); -3.948
  (+0.037/-0.034) in I from Gaia globular clusters (arXiv:2602.15421), all
  `[src]`. These values refer to different filters, populations and anchors;
  do not mix them, and do not compare them without the colour and metallicity
  terms of each calibration.
- **Colour and band.** F115W needs a colour slope; with it, JWST and HST TRGB
  distances agree to 1% on average and 4% per galaxy `[src]`
  (arXiv:2503.11769).
- **Reach.** About 20 Mpc with HST `[src]` (arXiv:2401.04776): the calibrator
  volume is small and sample fluctuations are large (Section 8).

## 12. JAGB-specific effects

- Field-to-field variation of 0.11 ± 0.02 mag between two NGC 4258 fields in
  the CCHP analysis, also seen in SH0ES fields; the systematic of 2.0 in the
  JAGB H0 is dominated by it `[src]` (Li et al. 2025, arXiv:2502.05259).
- The luminosity function changes shape between galaxies, so mode, mean,
  median and model fits give different H0 `[src]` (arXiv:2502.05259).
- Ground-based JAGB distances to nearby galaxies are offset from HST TRGB
  distances by 0.17 ± 0.04 (stat) ± 0.06 (sys) mag `[src]` (Anand 2025,
  arXiv:2502.07882).
- Purity: of 54 Milky Way stars in the standard colour box, only 13 are
  carbon-rich, a 76 ± 6% oxygen-rich contamination `[src]` (Li et al. 2026,
  arXiv:2609.25412).
- Incompleteness prevented a measurement in one of two hosts at ~40 Mpc
  `[src]` (arXiv:2502.05259).

## 13. Miras, SBF, Tully-Fisher, Fundamental Plane

- **Miras.** Two SN Ia hosts only; the error is dominated by the statistical
  uncertainty of the SN peak magnitude `[src]` (arXiv:2312.08423). Cluster
  Miras show no dependence on iron abundance over -1.7 < [Fe/H] < -0.1
  `[src]` (arXiv:2507.10658).
- **SBF.** Statistical error 0.7, zero-point systematic 2.3 to 2.4 `[src]`
  (arXiv:2101.02221, arXiv:2502.15935). The fluctuation magnitude depends on
  stellar population through colour; the JWST TRGB tie removes the Cepheid
  dependence but keeps NGC 4258.
- **Tully-Fisher.** Fitting uncertainty only 0.2; systematic 3.5 from
  inconsistent zero-point calibrators `[src]` (arXiv:2408.03660). Adding TF
  to the H0DN network pulls the result up (73.957 ± 0.787, and 73.994 against
  73.656 with and without TF in the "everything" solution) `[src]`
  (arXiv:2510.23823).
- **Fundamental Plane.** DESI DR1: statistical 0.06, calibration 1.1 `[src]`
  (arXiv:2512.03232). The FP zero point through Coma gives 76.5 ± 2.2, higher
  than SN-based values `[src]` (arXiv:2409.14546).

## 14. Time-delay cosmography

- **Mass-sheet degeneracy.** H0 scales with 1 - kappa_E; models with few
  parameters (power laws) tie kappa_E to the measured profile curvature and
  return precise but possibly inaccurate values; no time-delay H0 is more
  accurate than ~10% on that argument `[src]` (Kochanek 2020,
  arXiv:1911.05083). TDCOSMO's answer is to free lambda_int and constrain it
  with kinematics: precision went from 2.4% to about 8% for 7 lenses, 5% with
  SLACS `[src]` (arXiv:2007.02941, arXiv:2008.06157), and 4.6% in 2025 with
  the external samples `[src]` (arXiv:2506.03023).
- **Kinematics.** For a 2% H0 one needs Delta sigma^2 / sigma^2 < 2%.
  Quantified biases: PSF scale and shape 1 to 5% (ground-based); measured
  dispersion versus mean square velocity 2 to 6%; anisotropy model 2 to 18%;
  mismatch between light profile and stellar mass 1 to 10% `[src]`
  (Forés-Toribio et al. 2026, arXiv:2602.03934).
- **Population assumption.** lambda_int = 1.12 (+0.05/-0.06), 2 sigma from
  unity, in SDSSJ1433 `[src]` (arXiv:2604.14145): fixing lambda_int = 1, as
  in the three-lens JWST paper (arXiv:2608.27566), does not give a final H0.
- **Cluster lenses.** The spread between independent cluster mass models sets
  the error for lensed SNe (arXiv:2403.18902, arXiv:2509.12301).

## 15. Megamasers, sirens, chronometers

- **Megamasers.** Six galaxies; the result depends on the velocity treatment
  at the 1 to 2 level and beyond (range 71.8 to 76.9 in 2020,
  arXiv:2001.09213; 66.9 to 71.6 in 2026, arXiv:2608.06247,
  arXiv:2609.17684) `[src]`. Disc modelling (warps, eccentricity) is refitted
  in arXiv:2609.17684.
- **Sirens.** Dark-siren results assume a source-frame mass distribution
  `[src]` (arXiv:2509.04348). See `cosmo-multimessenger`.
- **Chronometers.** Systematic terms of 12 to 17 on H(z) values of 88 to 119
  `[src]` (arXiv:2511.02730).

## 16. The early-Universe side

- The CMB value is a LCDM prediction; it moves in extended models
  (`cosmo-cmb`). Planck spectra prefer more lensing than LCDM predicts at
  over 2 sigma `[src]` (arXiv:1807.06209).
- CMB and DESI DR2 BAO differ by 2.3 sigma (DESI's statement) or 2.8 sigma
  (SPT's statement) in LCDM `[src]` (arXiv:2503.14738, arXiv:2506.20707): a
  BAO + CMB H0 inherits that inconsistency.
- BBN: the baryon abundance depends on the assumed deuterium burning rates;
  theoretical rates favour lower omega_b than experimental ones `[src]`
  (Schöneberg 2024, arXiv:2401.15054).

## 17. What a referee checks in a results section

1. Which anchors, and the H0 from each alone.
2. Which SN compilation, redshift range and host cut define the Hubble flow;
   the velocity model used.
3. How calibrator hosts were selected, and whether selection is modelled.
4. Whether distances or H0 values are compared between indicators, and
   whether the NGC 4258 measurement error of each indicator is included.
5. Photometric system homogeneity between anchors and hosts.
6. Treatment of dust (R, NIR versus optical) and metallicity scale.
7. For TRGB and JAGB: the detection statistic, the field selection, the
   zero-point source.
8. For time delays: whether the mass-sheet degeneracy is free, which
   kinematic data break it, and which Omega_m prior was used.
9. For megamasers and two-rung ladders: the velocity reconstruction and its
   posterior variance.
10. The tension figure: both endpoints named, errors combined how, and in
    which variable (H0 or 5 log H0).
11. Blinding, and the list of variants run after unblinding.

## Not verified

- The redshift-Leavitt (time-dilation) bias and the stellar-association bias
  of Cepheids: abstracts were read (0.27% and 0.23% effects on H0) but the
  papers are not in `sources.tsv`; re-fetch before citing.
- The broken or period-dependent PL relation and the anchor-host period
  mismatch (a 2024 reanalysis read this session reports a shift of about -1).
- The local specific-star-formation-rate step of SN Ia and its H0 impact.
- The full SH0ES error-budget table (2022, Table of percent contributions).
- The TRGB zero point adopted by the CCHP (M_I = -4.05 is quoted as "adopted"
  in two CCHP abstracts read this session; the calibration paper and its
  error were not read).
