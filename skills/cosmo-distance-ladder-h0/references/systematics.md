# Systematics — what can bias an H0 measurement, how large, and how it is tested

Scope: the canonical systematic effects of the local distance ladder and of
the ladder-independent H0 routes; for each, the mechanism, the size where a
paper quantifies it, the standard mitigation, the validation test, and the
paper a referee expects to see cited.
Snapshot: 2026-10-13

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. H0 in km/s/Mpc.

Scale to keep in mind: the SH0ES-Planck difference is 0.176 ± 0.035 mag in
5 log H0 `[src]` (arXiv:2112.04510, Sec. 5). A single effect must reach about
0.18 mag, coherently across all hosts, to remove the tension; 1% in H0 is
0.0216 mag `[der]`.

## 1. Cepheid crowding and blending
<!-- key: cepheid-crowding-and-blending -->

**Mechanism.** In HST NIR images of hosts tens of Mpc away a Cepheid sits on an
unresolved background of red giants. If the statistical background correction
were wrong in a distance-dependent way, distant Cepheids would look too
bright, distances too short, H0 too high.

**Mitigation.** Artificial stars are injected near each Cepheid at the
magnitude predicted by its period and the recovered offset corrects the
photometry, iteratively with the PL fit `[src]` (arXiv:2112.04510, Sec. 3.4).
A floor of 20% of the background correction is carried as a covariance
between Cepheids j, k of one host, C = 0.2^2 bkgd_j bkgd_k: 0.03 to 0.06 mag
per host, none between hosts `[src: Eq. 8]` (arXiv:2112.04510).

**Size, measured.** JWST resolves the background. For more than 1000 Cepheids
in NGC 4258 and 5 SN hosts the HST minus JWST mean distance difference is
-0.01 ± 0.03 mag, and a crowding bias growing with distance is rejected as the
cause of the tension at 8.2 sigma `[src]` (Riess et al. 2024,
arXiv:2401.04773). Combining all JWST indicators, the linearity of HST
Cepheid distances is 0.994 ± 0.010 `[src]` (arXiv:2408.11770). In NGC 3447,
whose companion has no old stellar background, the two components agree
(sigma < 0.03 mag) and the PL scatter falls to about 0.12 mag; across 19 hosts
there is no bias relative to HST `[src]` (Riess et al. 2025,
arXiv:2509.01667): HST - JWST = -0.022 ± 0.029 mag for 19 hosts, both on
NGC 4258, no trend with distance (-0.005 ± 0.014 mag per mag)
`[src: Sect. III.2.3]`.

**Two small biases of the same family.** Light of cluster stars physically
associated with Cepheids: a 0.23% overestimate of H0 (wide binaries: 0.004%)
(Anderson, arXiv:1712.01065) `[src]`. Time dilation of periods
in SN hosts ("redshift-Leavitt bias"): (0.27 ± 0.01)% on H0 (Anderson 2019,
arXiv:1909.10847) `[src]`.

**Validation test.** HST versus JWST for the same Cepheids, as a function of
distance and local surface brightness.

**Status.** Closed as an explanation of the tension. A text that still offers
crowding as a candidate is stale. Cite arXiv:2401.04773 and arXiv:2509.01667.

## 2. Cepheid metallicity dependence
<!-- key: cepheid-metallicity-dependence -->

**Mechanism.** Metal-rich Cepheids are brighter at fixed period. Anchors and
SN hosts have different mean abundances, so an error in the coefficient gamma
propagates to the zero point.

**Size.** gamma = -0.234 ± 0.052 mag/dex with the SMC doubling the metallicity
lever arm `[src]` (Breuval et al. 2024, arXiv:2404.08038): that value is on
the [Fe/H] scale (optical Wesenheit: -0.264 ± 0.058) `[src: Sect. IV.3]`;
the global fit, on [O/H], gives -0.190 ± 0.047 (± 0.067 without the SMC),
[O/Fe] being ~0.2 in SMC Cepheids `[src: Sect. V]`; no PL break in the LMC
or SMC (2.4 sigma at most, a chance level of 51%) `[src: App. A]`. The 2019 SH0ES
value was -0.17 ± 0.06 `[src]` (as recalled in arXiv:2112.04510, Sec. 5).
The 2022 baseline fit gives Z_W = -0.217 ± 0.046 `[src: Sect. 5]`; its cost
in H0 is in Section 18.
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
<!-- key: gaia-parallax-zero-point -->

**Mechanism.** Gaia EDR3 parallaxes are offset by a few tens of microarcsec,
depending on magnitude, colour and ecliptic latitude (Lindegren et al. 2021,
arXiv:2012.01742) `[src]`. Field Cepheids are bright (G < 8), outside the
range where the correction is best calibrated.

**Size, Gaia team.** Global median quasar parallax -17 microarcsec
`[src: Fig. 2]`. The bias Z_5 (five-parameter solutions) runs from -94 to
+36 microarcsec, RMS 18 (13 weighted by actual colours); Z_6 from -151 to
+130, RMS 21 (15). Estimated from quasars, and differentially from LMC stars
and physical pairs; to be subtracted; "provisional and indicative"
`[src: Sect. 8]` (arXiv:2012.01742).

**Mitigation and size.** SH0ES fits a residual offset together with the PL
relation (arXiv:2012.08534): for 75 MW Cepheids, after the Gaia-team
correction, zp = -14 ± 6 microarcsec (an over-correction) and
M^W_H,1 = -5.915 ± 0.022 mag (chi^2 = 68.2, 66 dof), H0 = 73.0 ± 1.4; with
zp = 0, -5.865 ± 0.013 and 74.7 ± 1.3 (chi^2 = 74.5). Parallaxes spanning 0.2
to 1.5 mas break the offset-luminosity degeneracy; Gaia errors (mean 21
microarcsec) are inflated by 10%; no residual trend with G, colour or
ecliptic latitude (0.4, 1.0, 0.2 sigma) `[src: Sect. III.1]`. Cluster Cepheids use the mean parallax of more
than 300 fainter stars (G > 13) per cluster: residual offset -3 ± 4
microarcsec, and H0 = 72.8 ± 1.3 or 73.2 ± 1.1 from that sample alone with or
without marginalising the offset `[src]` (Riess et al. 2022,
arXiv:2208.01045).

**Where it is contested.** A "conservative" wide prior on the residual offset
is one of the two ingredients that move H0 to 70.6 in Högås & Mörtsell (2026,
arXiv:2601.22215) `[src]`.

**Next data.** Gaia DR4, 2 December 2026 (`surveys-and-data.md`).

## 4. Consistency of the geometric anchors
<!-- key: consistency-of-the-geometric-anchors -->

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
<!-- key: extinction-law-and-the-wesenheit-colour-term -->

**Mechanism.** The Wesenheit magnitude removes dust with a fixed R tied to a
Milky-Way-like law (R_V ~ 3.1), while SN Ia colours often prefer R_V ~ 2 in
their hosts.

**Size.** Baseline R = 0.386 (Fitzpatrick 1999 law, R_V = 3.3); free, it is
0.36 ± 0.04 from MW Cepheids and 0.34 ± 0.02 from all, H0 nearly unchanged
`[src: Sect. 6.3]`. At E(V-I) = 0.4 mag, R_V = 3.3 to 2.5 moves a NIR
Wesenheit distance by 0.01 mag, an optical one by 0.09 `[src: Sect. 6.13]`.
Per-host R is unconstrained beyond the nearest hosts `[src: App. D]`. The
lowest (71.93 ± 1.19, Fit 65: no NIR, MW anchor only) and highest
(74.85 ± 2.33, Fit 22: no colours) variants both come from suboptimal dust
treatment `[src: Sect. 6.14]` (all arXiv:2112.04510). A direct measurement from background galaxies
seen through NGC 5584 gives R_V = 3.59 (+0.99/-0.62) (stat) ± 0.19 (syst),
more than 3.5 sigma from R_V = 2 `[src]` (Murakami et al. 2025,
arXiv:2503.09702); a statistical sample of 5 to 10 hosts is announced.

**Validation test.** NIR-only versus optical Wesenheit fits; R varied per
host only after subtracting intrinsic colours.

## 6. Statistical model: distance priors and selection
<!-- key: statistical-model-distance-priors-and-selection -->

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
<!-- key: sn-ia-standardisation-between-calibrators-and -->

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
<!-- key: choice-and-size-of-the-calibrator-sample -->

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
<!-- key: peculiar-velocities-and-the-definition-of-the -->

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

**Mitigation.** Correct with a linear 2M++ reconstruction and group
redshifts (arXiv:2110.03487), or marginalise over posterior realisations of
a constrained simulation, with the selection of the sample in the likelihood
(arXiv:2509.09665); quote which, since the two differ by the shifts above.
Method details: `cosmo-peculiar-velocities`.

## 10. Local structure and sample variance
<!-- key: local-structure-and-sample-variance -->

**Size.** Sample variance of the local H0 in LCDM with the actual SN
distribution is 0.31 `[src]` (Wu & Huterer 2017, arXiv:1706.09723); the
empirical SN constraint is 0.60% against 0.42% predicted, and density
contrasts above 27% on scales larger than 69 Mpc/h are excluded at 5 sigma
`[src]` (Kenworthy et al. 2019, arXiv:1901.08681). Explaining the tension
would need delta ~ -0.8 over a radius of ~150 Mpc `[src]` (arXiv:1706.09723).

**Validation test.** Fit H0 in redshift shells; fit a void profile to direct
distances (arXiv:2506.10518). See `open-questions.md` for the void debate.

## 11. TRGB-specific effects
<!-- key: trgb-specific-effects -->

- **Tip detection.** Edge-detection responses are multi-peaked; the measured
  tip correlates with the contrast ratio of the field. Algorithm choices add
  0.83 to the H0 error, and none of 108 variants gives H0 below 71.6 `[src]`
  (arXiv:2304.06693).
- **Zero point.** CCHP: -4.050 ± 0.028 ± 0.048 in F814W on NGC 4258
  (arXiv:2008.04181). -4.01 ± 0.04 in F814W on NGC 4258 (arXiv:1908.05625);
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
<!-- key: jagb-specific-effects -->

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
- Budget terms and the spread between statistics: Section 18.

## 13. Miras, SBF, Tully-Fisher, Fundamental Plane
<!-- key: miras-sbf-tully-fisher-fundamental-plane -->

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
<!-- key: time-delay-cosmography -->

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
<!-- key: megamasers-sirens-chronometers -->

- **Megamasers.** Six galaxies; the result depends on the velocity treatment
  at the 1 to 2 level and beyond (range 71.8 to 76.9 in 2020,
  arXiv:2001.09213; 66.9 to 71.6 in 2026, arXiv:2608.06247,
  arXiv:2609.17684) `[src]`. Disc modelling (warps, eccentricity) is refitted
  in arXiv:2609.17684, whose fiducial 71.6 (+3.8/-3.5) the paper places 1.1
  sigma above the Planck CMB value and 0.4 sigma below the SH0ES value of
  arXiv:2404.08038, computation not given `[src: Sect. 4.3]`; see Section 18.
- **Sirens.** Dark-siren results assume a source-frame mass distribution
  `[src]` (arXiv:2509.04348). See `cosmo-multimessenger`.
- **Chronometers.** Systematic terms of 12 to 17 on H(z) values of 88 to 119
  `[src]` (arXiv:2511.02730).

## 16. The early-Universe side
<!-- key: the-early-universe-side -->

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
<!-- key: what-a-referee-checks-in-a-results-section -->

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

## 18. Error budgets, term by term
<!-- key: error-budgets-term-by-term -->

In percent of H0 unless a unit is given; triplets are LMC / MW / NGC 4258;
an empty first cell continues the analysis above.

| Analysis | Term | Size | Flag |
|---|---|---|---|
| SH0ES 2022, arXiv:2112.04510 | anchor distance | 1.2 / 1.0 / 1.5 | [src: Table 7] |
| | mean of the PL relation in the anchor | 0.4 / none / 1.0 | [src: Table 7] |
| | photometric zero points, anchor to hosts | 0.1 / 0.1 / 0.0 | [src: Table 7] |
| | Cepheid metallicity, anchor to hosts | 0.5 / 0.15 / 0.15 | [src: Table 7] |
| | subtotal per anchor; all anchors combined | 1.4 / 1.0 / 1.8; 0.7 | [src: Table 7] |
| | mean PL in the SN hosts; PL slope over the anchor-host period difference | 0.4; 0.3 | [src: Table 7] |
| | mean of the SN Ia calibrators, 42 to 46 SNe (1.3 with 19 SNe in 2016) | 0.9 | [src: Table 7] |
| | SN Ia magnitude-redshift relation | 0.4 | [src: Table 7] |
| | statistical error; the covariance already holds metallicity scale, crowding and SN systematics | 1.3 | [src: Table 7] |
| | analysis systematics: dispersion of the NIR variants (0.3 km/s/Mpc about a 3-sigma-clipped mean); baseline 0.2 below the median variant | 0.3 | [src: Sect. 6.14] |
| | total | 1.35 | [src: Table 7] |
| | systematic common to all host distances after the first two rungs | 0.019 mag (0.9% in distance) | [src: Fig. 16] |
| SH0ES 2024, arXiv:2404.08038 | SMC: anchor distance, mean PL, zero points, metallicity; subtotal | 1.5, 0.5, 0.1, 0.5; 1.7 | [src: Table 4] |
| | MW subtotal with cluster Cepheids; first rung without and with the SMC | 0.8; 0.65 and 0.60 | [src: Table 4] |
| | LMC and SMC distances share a systematic, carried as a covariance | not itemised | [src: Sect. V] |
| Pantheon+ SNe in the ladder, arXiv:2202.04077 | SN part of the H0 error, statistical + systematic; systematic alone; individual systematic shifts in quadrature (H0 = 73.6 ± 1.1 in flat LCDM) | 0.7; 0.29; 0.32 km/s/Mpc | [src: Sect. IV.5] |
| CCHP 2024, arXiv:2408.06153 | TRGB, JWST, 11 SNe Ia: random, systematic, sigma_SN | 2.6, 1.9, 1 | [src: Table 6] |
| | JAGB, JWST, 8 SNe Ia | 3.0, 2.4, 1 | [src: Table 6] |
| | TRGB + JAGB distances combined | 2.4, 1.8, 1 | [src: Table 6] |
| | TRGB, HST + JWST, 24 SNe Ia | 1.7, 1.9, 1 | [src: Table 6] |
| | systematic = 1.5% NGC 4258 distance and the indicator's measurement in NGC 4258, uncorrelated between methods | TRGB 0.025, JAGB 0.041, combined 0.021 mag | [src: Sect. VIII] |
| | sigma_SN: residual SN calibration and peculiar motions; SN photometric zero points | 1%; 0.015 mag | [src: Sect. XIII.1, XIII.2] |
| | foreground-extinction zero point, E(B-V) = 0.02 mag | A_J = 0.016 mag (0.7%) | [src: Sect. XIII.4] |
| | separate calibrator scatter sigma_cal in the 8-parameter fit | +1% in H0, error doubled | [src: Sect. X.4] |
| | TRGB 68.81 ± 1.79 (11 SNe) against 70.39 ± 1.22 (24 SNe, 11 shared), as (70.39 - 68.81) / sqrt(1.8^2 + 0.7^2) | 0.8 sigma | [src: Sect. X.4] |
| Hoyt 2025, F115W zero point, arXiv:2503.11769 | tip measurement in NGC 4258, colour systems F356W / F444W / homogenised | 0.030 / 0.019 / 0.016 mag | [src: Table 4] |
| | photometry; extinction | 0.02; 0.009 mag | [src: Table 4] |
| | colour correction sigma_beta (c_4258 - c_0): the tip is redder in NGC 4258 than in the hosts | 0.036 / 0.020 / 0.023 mag | [src: Table 4, Eq. 11] |
| | total, before the 0.032 mag of the maser distance | 0.052 / 0.035 / 0.036 mag | [src: Table 4] |
| | per host: tip error, slope term, aperture correction, extinction floor | 0.026 to 0.093; sigma_beta (c_i - c_0); 0.02; 0.01 mag in reddening | [src: Eq. 9, Table 2] |
| | scatter of the three NGC 4258 fields before and after colour correction | 0.071 and 0.030 mag | [src: Sect. IV.4] |
| CATS TRGB 2023, arXiv:2304.06693 | NGC 4258 distance; tip in NGC 4258; mean SN - tip difference; 5 a_B | 0.032 (1.1); 0.014 (0.5); 0.050 (1.7); 0.006 (0.2) mag (km/s/Mpc) | [src: Sect. III.2.4] |
| | quadrature total | 0.061 mag, 2.8%, 2.06 | [src: Eq. 9] |
| | tip against contrast ratio R, slope per unit R; tips rectified to R = 4 (hosts: median 4.2) | -0.021 ± 0.004 mag | [src: Sect. III.1] |
| | zero point M_I at R = 4, with and without internal extinction; raw mean tip of NGC 4258 fields | -4.030 ± 0.035, -4.018 ± 0.035; 25.40 ± 0.047 mag | [src: Sect. III.2.1] |
| | algorithm variants: spatial clip, colour-band width, smoothing, threshold (3 x 4 x 3 x 3) | 108 variants | [src: Sect. IV.1] |
| JWST F090W TRGB zero point, arXiv:2401.04776 | tip measurement, m = 25.055: statistical; spread of four techniques | 0.02; 0.02 mag | [src: Table 3] |
| | intrinsic variation with age and metallicity; colour selection; spatial selection | 0.02; 0.01; 0.01 mag | [src: Table 3] |
| | PSF model; PSF stability; foreground extinction (half of it plus 0.01) | 0.02; 0.01; 0.014 mag | [src: Table 3] |
| | NIRCam zero points; photometry set-up (cancel for a like-for-like reduction, not in the total) | 0.02; 0.03 mag | [src: Table 3] |
| | total on M = -4.362: statistical; systematic including the 0.032 mag maser modulus | 0.033; 0.045 mag | [src: Table 3] |
| | runs with and without artificial stars | 25.07 against 25.04 mag | [src: Sect. IV.5] |
| JAGB 2.0, arXiv:2502.05259 | NGC 4258 distance; SN calibration (M_B^0 = -19.25); intercept a_B | 0.032; 0.03; 0.006 mag, giving ± 1.4 | [src: Sect. IV.1] |
| | choice of statistic: mode alone against the middle of five statistics | 71.2 against 73.3 | [src: Sect. IV.1] |
| | mean, median, mode in one field; skew; J-region slope | up to 0.2 mag; 0.07 to 0.48; -0.60 ± 0.13 to 0.36 ± 0.05 mag/mag | [src: Sect. IV.2] |
| | per host: 15% of the extinction, spread of variants, largest statistical error | in quadrature | [src: Table 5] |
| | magnitude cut of ± 0.75 mag on a luminosity function of dispersion 0.4 to 0.5 mag | a 1.5 to 2 sigma truncation | [src: Sect. II.4] |
| Two-method comparison, arXiv:2408.11770 | Delta mu(a - b) is independent of the maser distance; its variance sums the two host-sample means, the two NGC 4258 measurements and the two external systematics, all taken as independent | Eqs. 3 to 5 | [src: Sect. II.2] |
| | per-host error of Cepheids, TRGB or JAGB; mean of 10 hosts; the NGC 4258 terms do not average down and limit the comparison | 0.05 to 0.08; 0.02 to 0.03 mag | [src: Sect. II.2] |
| H0DN 2025, arXiv:2510.23823 | how methods are combined: one generalised least-squares system, Gaussian in magnitude, modulus or log H0; each published error is split into anchor, indicator-in-anchor and per-host terms, and the shared terms become off-diagonal covariance | 255 equations, 183 distinct measurements | [src: Sect. II.1.1, B.2] |
| | singular covariance (72 redundant equations) inverted with the Moore-Penrose pseudo-inverse | equivalent to keeping independent equations | [src: Sect. B.2] |
| | residual offsets of host-distance groups from the network solution | Cepheids per anchor 0.02 mag or less; TRGB subsets about 0.03 mag | [src: Sect. IV] |
| | peculiar-velocity model error sigma_v of the linear reconstructions; tracers at z > 0.01, preferably z > 0.023 | 150 to 250 km/s | [src: Sect. B.3.7] |
| Seven-route summary, arXiv:2606.26831 | "fixed-covariance" average of published routes; the geometric scale (LMC DEBs, NGC 4258, Gaia) is one common component, shared anchors and SN samples are covariance terms, not independent evidence | 73.30 ± 0.92 | [src: Sect. 5.4, Table 4] |
| | propagation Delta H0 / H0 = -0.46 Delta mu: 0.01, 0.03, 0.05 mag; calibrator mean 0.130 / sqrt(42) = 0.020 mag, 0.013 to 0.015 with 80 to 100 calibrators | 0.5, 1.4, 2.3% | [src: Eq. 12, Sect. 5.1] |
| TDCOSMO 2025, arXiv:2506.03023; terms "not yet included in our baseline", stated to be random, uncorrelated and far below the 4.6 to 5% total | composite (stars + NFW) against power-law mass model | 0.2% in H0 | [src: Sect. 11.1] |
| | random error of one lens model (elliptical power law) | 1 to 5% | [src: Sect. 11.1] |
| | dark-matter substructure, scatter in the time-delay distance | ~1% | [src: Sect. 11.1] |
| | peculiar velocities of lenses and observer | ~0.25% | [src: Sect. 11.1] |
| | departure from spherical symmetry after the projection correction (included); triaxiality | 1 to 2% in lambda_int; below 1% | [src: Sect. 11.1] |
| | time-delay measurement (PyCS3), residual bias | below 1% | [src: Sect. 11.1] |
| | selection of quads (7 of 8 lenses) | sub-percent on H0 | [src: Sect. 11.2.1] |
| | external convergence of a generic line of sight | of order 10^-2 | [src: Sect. 3.1] |
| IR SBF 2021, arXiv:2101.02221 | statistical; distance calibration via Cepheids, via TRGB, averaged; velocity scaling; total systematic | 1.0; 4.1, 4.7, 3.1; 1.0; 3.3 (2.41 km/s/Mpc) | [src: Table 2, Sect. IV.4] |
| | zero point via Cepheids: WFC3/IR-optical SBF tie, SBF-Cepheid tie, Cepheid zero point; TRGB minus Cepheid calibration; 2M++ instead of group velocities | 0.03, 0.08, 0.028, total 0.09 mag; 0.007 ± 0.099 mag; +0.5% | [src: Sect. II.4, IV.4] |
| Cosmic chronometers, arXiv:2412.01994 | total covariance = statistical + metallicity + young-population contamination + SPS terms (star-formation history, IMF, stellar library, model); metallicity and SPS dominate | ~5% on H(z) at z ~ 0.5, 10 to 20% at z ~ 2 | [src: Eq. 6, Sect. 5.1] |
| NGC 4258 maser distance, arXiv:1908.05625 | statistical: 0.075 Mpc from the fit, inflated by sqrt(1.2) for chi^2/dof = 1.2 (483 dof) | 0.082 Mpc | [src: Sect. II] |
| | systematic: unmodelled spiral structure only; error floors, eccentricity and second-order warp are now fitted | 0.076 Mpc | [src: Sect. II] |
| | history: 7.2 ± 0.5 (Herrnstein et al. 1999, 4 VLBI epochs), 7.596 ± 0.228 (Humphreys et al. 2013, 18 epochs), 7.576 ± 0.112 | modulus 29.397 ± 0.032 | [src: Table 1] |
| Megamasers 2020, arXiv:2001.09213 | velocity noise added in quadrature (measurement errors are 1 to 2 km/s); fitted instead: 141 (+185/-80) km/s and H0 = 74.4 (+3.9/-3.4) | 250 km/s | [src: Sect. 3.1, 3.2] |
| | Omega_m fixed to 0.315 in D(z); any value in 0 to 0.5 | below ~1% in distance | [src: Sect. 3] |
| Megamasers 2026, arXiv:2609.17684 | spread of the eleven modelling variants on one spot table | 2.4 to 2.7 | [src: Sect. 4.3] |
| | published against updated spot catalogues (NGC 6264, NGC 6323) | 1.8 to 2.1 | [src: Sect. 4.3, 5.2] |
| | selection threshold on distance or on redshift; no selection term at all | 0.7 to 0.8; -2.2 | [src: Sect. 4.3] |
| | warp order (linear or quadratic), per-galaxy distance | at most 0.6 sigma | [src: Sect. 5.2] |

## Not verified
<!-- key: not-verified -->

- The broken or period-dependent PL relation: SH0ES 2022 reads a slope
  difference of 0.10 ± 0.05 across P = 10 d (Fit 24), which lowers H0 by
  0.45; with more M31 Cepheids 0.07 ± 0.04 and -0.3; no Cepheid with
  P < 5 d is used `[src: Sect. 6.4]` (arXiv:2112.04510). Still open: the
  anchor-host period mismatch as treated by later reanalyses: Högås et al.
  2024 (arXiv:2412.07840) is the 2024 study; its shifts are tabulated in its
  Sect. V.1 and not transcribed here; see `deep/cepheid-sn-ladder.md`.
- The local specific-star-formation-rate step of SN Ia and its H0 impact.
- The error budget of the LMC eclipsing-binary distance (arXiv:1903.08096):
  no HTML rendering and no LaTeX source could be read.
- arXiv:2408.11770: the HTML body gives ± 2.0, 2.3, 2.3 for the three
  joint-sample values where the current abstract gives ± 2.1, 2.2, 2.2.
