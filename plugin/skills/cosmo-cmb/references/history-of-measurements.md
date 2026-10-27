# CMB measurements — history and how each generation changed the parameters

Scope: the sequence of CMB measurements from the discovery to the Planck
legacy and the first ground-based detections of lensing and B modes: what
each experiment measured first, with which data, and what it changed in the
parameters; the monopole and dipole across missions; the "Stage"
generations. Current experiments and releases are in `surveys-and-data.md`;
the history of the post-2015 values (H₀, τ, A_L, Ω_K, Σm_ν) is in
`results.md`, Sect. 10.
Snapshot: 2026-10-20

Provenance flags: `[src]` and `[src: abstract]` read in the cited paper's
abstract; `[src: <place>]` in its body; `[sec: <source>]` taken from the named
secondary source. Years attached to author names are arXiv submission years
(publication years for papers without an arXiv version). Each value is
given with its data combination; values from different combinations are
not comparable.

## 1. Discovery and the blackbody spectrum
<!-- key: discovery-and-blackbody -->

- **Discovery, 1965.** Planck 2018 I dates the discovery to 1965, citing
  Penzias & Wilson 1965 (doi:10.1086/148307) and Dicke et al. 1965
  (doi:10.1086/148306) [sec: Planck Collaboration 2018, arXiv:1807.06205,
  Sect. 1]. Their titles were checked on Crossref; their texts were not read.
- **COBE/FIRAS.** The full FIRAS data set gives rms deviations from a
  blackbody below 50 parts per million of the peak, a Compton parameter
  of |y| < 15 × 10⁻⁶ and a chemical potential of |μ| < 9 × 10⁻⁵ (95%),
  T = 2.728 ± 0.004 K (95%), and a dipole of 3.372 ± 0.007 mK towards
  (ℓ, b) = (264.14° ± 0.30, 48.26° ± 0.30) (95%) (Fixsen et al. 1996,
  arXiv:astro-ph/9605054) [src: abstract]. The current monopole,
  2.72548 ± 0.00057 K, is Fixsen 2009 (arXiv:0911.1955) [src: abstract].
- **Why it matters.** The CMB spectrum is the best-measured blackbody in
  nature, and the absence of distortions limits energy injection after
  z ≃ 2 × 10⁶ [src: Planck 2018 I, arXiv:1807.06205, Sect. 1]; the blackbody is the best
  evidence that the Universe was once hot and dense [src: Sect. 3.3].
  Distortion physics and current limits belong to
  `cosmo-early-universe-exotica`.

## 2. COBE/DMR: the first anisotropies
<!-- key: cobe-dmr -->

- The anisotropies were first detected by COBE (Smoot et al. 1992,
  doi:10.1086/186504), and the detection "cemented the gravitational
  instability paradigm within a cold dark matter (CDM) model"
  [sec: Planck 2018 I, Sect. 1].
- **Four-year DMR.** The anisotropy is consistent with a scale-invariant
  power law and Gaussian statistics; with the multi-frequency data and a
  Galactic-emission model, n = 1.2 ± 0.3 and Q_rms-PS = 15.3 (+3.8/−2.8) μK,
  and Q_rms-PS = 18 ± 1.6 μK for n = 1; the maps have a signal-to-noise
  ratio of about 2 per 10° patch [src: abstract] (Bennett et al. 1996,
  arXiv:astro-ph/9601067).
- DMR scales are larger than the sound horizon at recombination, so they
  measure the initial conditions directly (the Sachs–Wolfe plateau; see
  `primary-anisotropies.md` §2).

## 3. Balloons and interferometers: the first peak and first polarisation
<!-- key: first-peak-and-polarisation -->

By 2001 Hu & Dodelson tabulated about thirty experiments whose band powers
made up the measured spectrum, from COBE on the largest scales to
interferometers (CBI, DASI, CAT, VLA, BIMA, ATCA) and balloon-borne or
ground bolometers (BOOMERanG, MAXIMA, Saskatoon, TOCO, Python, VIPER,
MSAM, QMAP) [src: Hu & Dodelson 2001, arXiv:astro-ph/0110414, Table 1].
Ground and balloon data established that the Universe has no significant
spatial curvature [sec: Planck 2018 I, Sect. 1].

| Experiment | What it showed | Values as stated | Source |
|---|---|---|---|
| BOOMERanG (balloon) | first images of resolved anisotropy over a significant part of the sky, four frequencies separating CMB from foregrounds; first peak consistent with a flat universe | ℓ_peak = 197 ± 6, ΔT₂₀₀ = 69 ± 8 μK | de Bernardis et al. 2000, arXiv:astro-ph/0004404 [src] |
| MAXIMA-1 (balloon) | 124 deg² at 10′ resolution, 150–410 GHz, 16 bolometers at 100 mK, calibrated on the CMB dipole; spectrum over 36 < ℓ < 785 | peak of 78 ± 6 μK at ℓ ~ 220; 40–50 μK over 400 < ℓ < 785 | Hanany et al. 2000, arXiv:astro-ph/0005123 [src] |
| DASI (South Pole interferometer) | first detection of CMB polarisation, in two 3.4° fields | E modes at 4.9σ, level 0.80 (0.56–1.10) of the prediction; TE at 95%; B < 0.59 of E (95%) | Kovac et al. 2002, arXiv:astro-ph/0209478 [src] |

The high third peak measured by DASI (Halverson et al. 2001) was read as a
good indication that cold dark matter exists and dominates at
recombination [sec: Hu & Dodelson 2001, Sect. 3.5]. The DASI polarisation
result was consistent with primordial scalar adiabatic fluctuations
[src: Kovac et al. 2002].

## 4. WMAP (launched June 2001; releases 2003–2012)
<!-- key: wmap-history -->

- **Launch.** MAP was launched in June 2001 [src: Hu & Dodelson 2001,
  Sect. 2.2].
- **First year (2003).** Full-sky maps in five bands, 23 to 94 GHz, with
  calibration errors below 0.5%; the TT spectrum over 2 < ℓ < 900 is
  cosmic-variance limited for ℓ < 354 [src: abstract] (Bennett et al. 2003,
  arXiv:astro-ph/0302207). The TE correlation is detected at more than
  10σ; at ℓ > 20 it agrees with the prediction from the temperature
  spectrum with no free parameter, and an excess at large angles was read
  as reionisation with τ = 0.17 ± 0.04 (68%, including systematics and
  foregrounds) [src: abstract] (Kogut et al. 2003, arXiv:astro-ph/0302213).
- **First-year parameters** from WMAP + ACBAR + CBI + 2dFGRS + Lyα forest:
  h = 0.71 (+0.04/−0.03), Ω_b h² = 0.0224 ± 0.0009,
  Ω_m h² = 0.135 (+0.008/−0.009), τ = 0.17 ± 0.06,
  n_s(0.05 Mpc⁻¹) = 0.93 ± 0.03, σ₈ = 0.84 ± 0.04; with external data
  Ω_tot = 1.02 ± 0.02 [src] (Spergel et al. 2003, arXiv:astro-ph/0302209).
  WMAP also showed that the fluctuations are predominantly adiabatic, from
  the phasing of the peaks and polarisation [sec: Planck 2018 I, Sect. 1].
- **Nine-year final release (2012).** WMAP + high-ℓ CMB + BAO + H₀
  measures Ω_b h², Ω_c h² and Ω_Λ to about 1.5%, gives evidence of tilt at
  5σ, r < 0.13 (95%), Ω_K = −0.0027 (+0.0039/−0.0038), Σm_ν < 0.44 eV
  (95%) and N_eff = 3.84 ± 0.40; the nine-year data reduce the allowed
  six-parameter volume by a factor of 68,000 relative to pre-WMAP data
  [src: abstract] (Hinshaw et al. 2012, arXiv:1212.5226). The companion
  maps paper gives n_s = 0.9608 ± 0.0080 and H₀ = 69.32 ± 0.80 km/s/Mpc for
  WMAP + finer-scale CMB + BAO + H₀ [src: abstract] (Bennett et al. 2012,
  arXiv:1212.5225).
- **What did not survive.** The first-year WMAP τ (above) is higher than
  every Planck-era value in `results.md`, Sect. 5 [der: comparison of the
  tabulated values].
- WMAP alone could not break the geometric degeneracy; adding BAO moved its parameters towards the Planck values,
  with ω_m = 0.1398 ± 0.0023 and H₀ = 68.14 ± 0.73 from WMAP + BAO against
  ω_m = 0.14240 ± 0.00087 and H₀ = 67.66 ± 0.42 from Planck + BAO
  [src: Planck 2018 I, arXiv:1807.06205, Sect. 4.1].

## 5. Planck (2009–2013 observations; releases 2013–2020)
<!-- key: planck-history -->

ESA selected the combined COBRAS/SAMBA project as its M3 mission in July
1996; Planck launched on 14 May 2009, its cryogenic mission ended on
14 January 2012, and the last command was sent on 23 October 2013
[src: Planck 2018 I, arXiv:1807.06205, Table 1]. Planck was the third-generation space
mission dedicated to CMB anisotropies and operated for over three times its
initially planned duration [src: Sect. 1]. The second release (February
2015) was the first based on the entire mission in temperature and
polarisation [src] (Planck Collaboration 2015, arXiv:1502.01582).

- **2013 (temperature, with WMAP polarisation).** For Planck + WP + highL,
  H₀ = 67.3 ± 1.2 km/s/Mpc [src: Eq. 56], Ω_m = 0.315 ± 0.016,
  σ₈ = 0.828 ± 0.012 and n_s = 0.9585 ± 0.0070, a 6σ departure from scale
  invariance [src: Sect. 7] (Planck Collaboration 2013, arXiv:1303.5076).
  The H₀ was in tension with direct measurements at about 2.5σ, and the
  low-ℓ spectrum over 20 ≲ ℓ ≲ 40 was a poor fit, called an "anomaly" not of
  decisive significance [src: abstract and Sect. 7].
- **2015 and 2018.** The values, and what superseded them, are tabulated in
  `results.md`, Sect. 10, and the release table of `surveys-and-data.md`.
- **The overall gain.** Planck 2018 I (arXiv:1807.06205) plots the evolution of CMB-only
  constraints from the pre-WMAP compilations through WMAP1–9 and Planck
  2013–2018, and states that ω_m, ω_b and h are each now measured at over
  100σ; except τ, the base parameters are simultaneously known to percent
  level [src: Sect. 3.2, Figs. 11–13].
- **After Planck.** Planck dominates TT and EE up to ℓ ≃ 10³, while
  higher-resolution experiments give better secondary anisotropies at high
  ℓ and B modes, Planck still serving as their calibration
  [src: Planck 2018 I, arXiv:1807.06205, Sect. 4.1]. In 2025 the SPT+ACT
  combination matched Planck on H₀ and σ₈ (`results.md`, Sect. 10).

## 6. Ground-based high resolution and the first lensing and B-mode detections
<!-- key: ground-detections -->

| Year | Result | Values as stated | Source |
|---|---|---|---|
| 2011 | First detection of CMB lensing, from the four-point function of ACT temperature maps | 4σ; amplitude of density fluctuations to 12% | Das et al. 2011, arXiv:1103.2124 [src: abstract] |
| 2013 | First detection of lensing B modes, SPTpol E modes × a Herschel-SPIRE CIB lensing template | 7.7σ correlation | Hanson et al. 2013, arXiv:1307.5830 [src: abstract] |
| 2014 | BICEP2 B-mode excess at 30 < ℓ < 150 | > 5σ over lensed ΛCDM; r = 0.20 (+0.07/−0.05) if all tensor; dust models then not constraining enough to exclude it | BICEP2 Collaboration (Ade et al.) 2014, arXiv:1403.3985 [src: abstract] |
| 2015 | Joint BICEP2/Keck + Planck analysis | strong evidence for dust, no significant tensor signal; r_0.05 < 0.12 (95%); lensing B modes at 7.0σ | BICEP2/Keck and Planck 2015, arXiv:1502.00612 [src: abstract] |

The 2014–2015 sequence is the standard example of a foreground mistaken for
a primordial signal; the current limit and the B-mode programme are in
`cosmo-inflation-primordial` and `results.md` §8. The lensing
reconstructions that followed (Planck, ACT DR6, SPT-3G) are in
`deep/lensing-reconstruction.md`.

**Generations.** The Snowmass CMB white paper calls the current ground
experiments "Stage 3": the 10-m SPT and 6-m ACT large-aperture telescopes
with arcminute resolution, and the B-mode experiments BICEP/Keck,
POLARBEAR/Simons Array and ABS/CLASS, at the South Pole or in the Atacama
[src: Chang et al. 2022, arXiv:2203.07638, Sect. 3.1]. SPT observes smaller
always-visible patches more deeply, ACT larger areas more shallowly
[src: Sect. 3.1]. CMB-S4 was designed as an order-of-magnitude step beyond
that generation [src: Sect. 1]; it has since been cancelled
(`surveys-and-data.md` §3).

## 7. The dipole across missions
<!-- key: dipole-across-missions -->

Solar-dipole amplitude and direction in Galactic coordinates, as tabulated
by Planck 2018 I [src: Sect. 2.1, Table 2]; uncertainties are dominated by
systematics.

From arXiv:1807.06205, Table 2:

| Experiment | Amplitude [μK_CMB] | l [deg] | b [deg] |
|---|---|---|---|
| COBE | 3358 ± 24 | 264.31 ± 0.20 | 48.05 ± 0.11 |
| WMAP | 3355 ± 8 | 263.99 ± 0.14 | 48.26 ± 0.03 |
| Planck 2015 nominal | 3364.5 ± 2.0 | 264.00 ± 0.03 | 48.24 ± 0.02 |
| LFI 2018 | 3364.4 ± 3.1 | 263.998 ± 0.051 | 48.265 ± 0.015 |
| HFI 2018 (recommended) | 3362.08 ± 0.99 | 264.021 ± 0.011 | 48.253 ± 0.005 |

- The amplitude corresponds to β = (1.23357 ± 0.00036) × 10⁻³, or
  v = 369.82 ± 0.11 km/s, known to about 0.025%, like the monopole; a
  temperature amplitude should carry the T₀ uncertainty as well
  (arXiv:1807.06205) [src: Sect. 2.1].
- The "orbital dipole" from the satellite's motion is known from the orbit
  and was the photometric calibrator from 30 to 353 GHz in 2015
  (arXiv:1807.06205) [src: Sect. 2.1]. The 2018 maps had the 2015 nominal dipole subtracted,
  so a very small residual dipole remains in all released maps
  [src: Sect. 2.1].
- Local Group velocity relative to the CMB: 620 ± 15 km/s towards
  (l, b) = (271.9 ± 2.0, 29.6 ± 1.4), the error dominated by the Sun's
  velocity relative to the Local Group (arXiv:1807.06205) [src: Sect. 2.1,
  Table 3]. Its use
  for bulk flows belongs to `cosmo-peculiar-velocities`; the
  matter-dipole comparisons to `cosmo-tensions-anomalies`.
- The NPIPE (PR4) amplitude is 3366.6 ± 2.7 μK (arXiv:2007.04997) [src:
  abstract]. Second-order boost effects (aberration, modulation, kinematic
  quadrupole) are in `primary-anisotropies.md`, Sect. 10.

## 8. Reading the history
<!-- key: reading-the-history -->

- **Each generation fixed one more feature.** COBE: the plateau and its
  amplitude; BOOMERanG and MAXIMA: the first peak and flatness; DASI:
  polarisation; WMAP: TE, adiabaticity, a precise six-parameter fit, tilt;
  Planck: polarisation over the acoustic peaks, lensing over the full sky, sub-percent
  densities; ACT and SPT: the first lensing detection and lensing B modes
  [der: summary of the rows above].
- **Revisions came mostly from large-angle polarisation and foregrounds**:
  τ from WMAP to Planck, and the BICEP2 excess to dust [der: from §4 and
  §6].
- **H₀ from the CMB in ΛCDM has changed little while its error shrank**,
  from WMAP9 + external data (Sect. 4 above) to Planck 2013 (Sect. 5) and
  the later values of `results.md`, Sect. 10 [der: values above, each with
  its own data combination].

## Not verified
<!-- key: not-verified -->

- Penzias & Wilson 1965, Dicke et al. 1965 and Smoot et al. 1992 are cited
  through Planck 2018 I; their texts were not read.
- The pre-WMAP parameter compilations (Wang et al. 2003; Bond et al. 2003)
  and the Planck 2015 overview numbers were not read.
- The WMAP + BAO σ₈ in Planck 2018 I (arXiv:1807.06205), Sect. 4.1, has an
  error that looks garbled in the rendering read; it is left out until
  checked against the PDF.
- The intermediate WMAP releases (three-, five- and seven-year) were not
  read; the first detection of tilt is attributed to the five-year data by
  Hinshaw et al. 2012 [src], without the value.
