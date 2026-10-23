# Alternative distance probes — quasars, GRBs, HII galaxies, redshift drift, lens statistics

Scope: distance and expansion-rate probes outside the ladder and the SN Ia
Hubble diagram that extend it to z > 2, or test it in real time: the quasar
Hubble diagram from the X-ray–UV relation, gamma-ray bursts, HII galaxies and
giant HII regions, the redshift drift (Sandage–Loeb test), and the statistics
of galaxy-scale strong lenses as a geometric probe. Time-delay H0 is in
`physics-and-methods.md` §4 and `deep/time-delay-cosmography.md`; cosmic
chronometers in `physics-and-methods.md` §5; the SN Ia Hubble diagram in
`cosmo-supernovae`.
Snapshot: 2026-10-20

Flags: `[src]` read this session in the cited paper's abstract;
`[src: <place>]` in its body; `[sec: <source>]` taken from the named
secondary source; `[der]` derived here, with the assumption stated. Forecasts
are labelled **forecast**. Field map: CosmoVerse white paper (Di Valentino et
al. 2025, arXiv:2504.01669) Sects. 2.1.10, 2.1.14–2.1.16; review of the
emerging probes, Moresco et al. 2022 (arXiv:2201.07241).

## 1. What these probes add, and the common caveat
<!-- key: what-these-probes-add-and-the-common-caveat -->

The SN Ia Hubble diagram stops near z ~ 2 and BAO give a handful of
redshifts; the CMB sits at z ~ 1100. Quasars, GRBs and HII galaxies are
bright enough to be seen at z ~ 2–7, so they would test the expansion
history where no other distance indicator exists. All three are
*correlations*, not physically standardised candles: a luminosity is
predicted from another observable through an empirical relation whose
parameters are fitted on the same data, or calibrated on SNe Ia at low
redshift. Two consequences follow for every result below:

- the relation's normalisation is degenerate with H0, so these probes give
  H0 only when the normalisation is calibrated externally (SNe Ia, a ladder,
  or local HII regions with Cepheid distances);
- a redshift evolution of the relation, or a selection effect that changes
  with redshift, is indistinguishable from a change in d_L(z). The test that
  a relation is "standardisable" is that its fitted parameters do not depend
  on the cosmological model assumed (Khadka & Ratra 2020, arXiv:2012.09291)
  `[src]`.

## 2. Quasars: the X-ray–UV (Risaliti–Lusso) Hubble diagram
<!-- key: quasars-the-x-ray-uv-risaliti-lusso-hubble -->

### 2.1 Method
<!-- key: method-2 -->

The method rests on the non-linear relation between the monochromatic
luminosities at 2 keV and 2500 Å, log L_X = γ log L_UV + β, with γ < 1
(Risaliti & Lusso 2015, arXiv:1505.07118) `[src: abstract]`. Writing L = 4π d_L² F
for both bands gives

    log d_L = [log F_X − β − γ log F_UV] / [2 (γ − 1)] − ½ log 4π

`[der: L = 4π d_L² F in both bands, K-corrections absorbed in the
monochromatic fluxes]`, so a fit of γ and β across redshift, with an
intrinsic dispersion δ, yields relative distances. The absolute scale is set
by cross-calibrating the quasar Hubble diagram on SNe Ia in their common
redshift range; a redshift-independent offset in the UV fluxes is absorbed by
that cross-calibration (Lusso et al. 2020, arXiv:2008.08586)
`[src: Sect. 3.1]`. The observed dispersion falls from 0.4 to about 0.2 dex
after selecting sources free of dust reddening, X-ray absorption and
flux-limit (Eddington) bias, which the authors read as evidence that most of
the scatter is observational rather than intrinsic `[src: Sect. 1]`.
CosmoVerse cites sub-samples with the best X-ray data suggesting an intrinsic
scatter below 0.1 dex `[sec: arXiv:2504.01669, Sect. 2.1.15]`.

### 2.2 Samples
<!-- key: samples -->

| Sample | Size, redshift | Result as stated | Citation |
|---|---|---|---|
| Risaliti & Lusso 2015 | ~1138 quasars, to z ~ 6 | matches SNe at z = 0–1.4; ΛCDM fit Ω_M = 0.22 (+0.08/−0.10), Ω_Λ = 0.92 (+0.18/−0.30); with SNe Ω_M = 0.28 ± 0.04, Ω_Λ = 0.73 ± 0.08 `[src: abstract]` | arXiv:1505.07118 |
| Risaliti & Lusso 2019 | quasars at 0.5 < z < 5.5 | agreement with SNe at z < 1.4; deviation from ΛCDM at higher z, "~4 sigma"; with an evolving w, dark-energy density increasing with time `[src: abstract]` | arXiv:1811.02590 |
| Lusso et al. 2019 | SNe + quasars + GRBs | tension with flat ΛCDM in the high-z Hubble diagram (title) `[src]` | arXiv:1907.07692 |
| Lusso et al. 2020 | ~2400 quasars with Chandra or XMM X-rays, to z ~ 7.5 | distances match SNe to z ~ 1.5; slope does not evolve to z ~ 5; ΛCDM reproduces the diagram to z ~ 1.5–2, "strong deviations" above `[src: abstract]` | arXiv:2008.08586 |
| eROSITA eFEDS / eRASS1 (Sacchi et al. 2025) | 1248 and 519 quasars, to z ≈ 3 and 1.5 | no significant redshift evolution; dispersion ~0.2 dex; no significant cosmological constraint yet `[src: abstract]` | arXiv:2508.00732 |
| eROSITA × SDSS DR16Q (Prokhorenko et al. 2025) | 2414 quasars, 0.5 < z < 2.5 | γ = 0.69 ± 0.02; intrinsic scatter σ²_intX = 0.063 ± 0.005 dominates σ²_intUV = 0.002 (+0.003/−0.002) `[src: abstract]` | arXiv:2512.05807 |

### 2.3 The claimed deviation from ΛCDM at z > 1.5
<!-- key: the-claimed-deviation-from-lambdacdm-at-z-1-5 -->

**As the Risaliti–Lusso group states it.** The quasar distance modulus agrees
with SNe and ΛCDM below z ~ 1.4–1.5 and departs from it above, at ~4 sigma
(arXiv:1811.02590) `[src]`; having minimised the systematic effects and shown
the stability of the relation at high redshift, the authors conclude that an
evolution of the expansion rate "should be considered as a possible
explanation ... rather than some systematic (redshift-dependent) effect"
(arXiv:2008.08586) `[src]`. A 2022 proceedings restates "a significant
tension" above z = 1.5 (Signorini et al. 2024, arXiv:2401.07909) `[src]`.
Joint fits with the CMB find that simple dark-energy extensions do not
reconcile the probes and only interacting dark-sector models do (Benetti et
al. 2025, arXiv:2506.21477) `[src]`.

**As the critiques state it.**

- *Cosmographic expansion.* The ~4 sigma figure comes from a log-polynomial
  cosmographic fit, which fails to recover flat ΛCDM beyond z ~ 2; direct
  fits prefer flat ΛCDM over the polynomial, and a flat-ΛCDM fit to the
  quasars alone gives a Universe with no dark energy within 1 sigma, which
  the authors call an "irreconcilable tension" between these quasars and
  flat ΛCDM (Yang et al. 2020, arXiv:1911.01681) `[src]`.
- *Standardisability.* In the 2038-quasar compilation the L_X–L_UV parameters
  depend on the cosmological model assumed, so the full set is not
  standardised; only z ≲ 1.5–1.7 subsets behave model-independently, and
  they give weak constraints consistent with BAO and H(z) (Khadka & Ratra
  2020, arXiv:2012.09291) `[src]`. The SDSS–4XMM sub-sample, about two
  thirds of the quasars, has relations that depend on cosmology and on
  redshift and is the main cause; the SDSS–Chandra and XXL sub-samples
  (about 30%) appear standardisable and are consistent with flat ΛCDM
  (Khadka & Ratra 2021, arXiv:2107.07600) `[src]`. An earlier fit of the
  2015 compilation (808 quasars) with BAO and H(z) was consistent with flat
  ΛCDM (Khadka & Ratra 2019, arXiv:1909.01400) `[src]`.
- *Comparison with reverberation distances.* For 58–59 quasars with both
  measurements (z ≤ 1.686), L_X–L_UV distances are shorter than R–L
  (reverberation) distances and than flat-ΛCDM distances, which explains the
  high Ω_m0 preferred by L_X–L_UV data (Khadka et al. 2022,
  arXiv:2212.10483) `[src]`; dust extinction with E_X−UV = 0.03–0.28 mag can
  produce such a shift (Zajaček et al. 2023, arXiv:2305.08179) `[src]`.
- *A redshift trend expected in ΛCDM.* The quasars recover Ω_m ≈ 0.3 at
  z ≲ 0.7 and move to Ω_m ≈ 1 at z ≳ 1; the same trend of rising Ω_m with
  effective redshift is argued to be an intrinsic bias of flat-ΛCDM fits
  (Ó Colgáin et al. 2022, arXiv:2203.10558) `[src: abstract]`.
- *Dispersion model.* Over 1.6 < z < 2.6 a redshift-dependent intrinsic
  dispersion is decisively favoured over a constant one, and shifts the
  flat-ΛCDM Ω_m0 by ≈ 0.025 (Gao et al. 2026, arXiv:2606.27173) `[src: abstract]`.

**Where it stands.** The z > 1.5 departure is claimed by the group that built
the sample and attributed by the critiques to the cosmographic fit, to
sub-sample heterogeneity or redshift evolution of the relation, or to
extinction. The independent eROSITA samples confirm the slope and the ~0.2
dex dispersion but stop at z ≈ 1.5–3 and do not yet constrain cosmology
(arXiv:2508.00732) `[src: abstract]`.

### 2.4 What a referee checks
<!-- key: what-a-referee-checks-3 -->

- Whether γ, β and δ are fitted jointly with cosmology, and whether they
  change with the assumed model or across redshift bins.
- Which sub-samples carry the high-z points (SDSS–4XMM against Chandra/XXL).
- Whether "tension with ΛCDM" comes from a cosmographic expansion or from a
  direct model fit.
- The SN cross-calibration: quasar distances are relative; H0 from quasars
  alone is not meaningful.
- Selection: Eddington bias at the X-ray flux limit, reddening and absorption
  cuts, and their redshift dependence.

## 3. Gamma-ray bursts
<!-- key: gamma-ray-bursts -->

### 3.1 Correlations used
<!-- key: correlations-used -->

| Correlation | Quantities | Origin and stated scatter | Citation |
|---|---|---|---|
| Amati | rest-frame spectral peak energy E_p,i against isotropic energy E_iso (prompt emission) | found in 12 BeppoSAX bursts with redshifts; the authors discuss selection and truncation biases `[src]` | Amati et al. 2002, arXiv:astro-ph/0205230 |
| Yonetoku | E_p against peak isotropic luminosity | "considerably tighter" than earlier relations `[src]` | Yonetoku et al. 2004, arXiv:astro-ph/0309217 |
| Dainotti (2D) | X-ray plateau-end luminosity L_X(T_a) against rest-frame time T_a/(1+z) | σ_int = 0.33; slope and scatter almost independent of Ω_M and w `[src]` | Dainotti et al. 2008, arXiv:0809.1389 |
| Dainotti 3D ("fundamental plane") | adds the prompt peak luminosity | σ_int = 0.18 ± 0.07 for the "platinum" sample after selection and evolution corrections `[src]` | Dainotti et al. 2023, arXiv:2209.08675 |

CosmoVerse notes that the plateau relations can be tied to physical models
(magnetar spin-down, forward/reverse shocks), which the prompt-emission
relations cannot `[sec: arXiv:2504.01669, Sect. 2.1.16]`. That section is
coordinated by the author of the Dainotti relation; read it together with
the independent tests below.

### 3.2 Calibration and the circularity problem
<!-- key: calibration-and-the-circularity-problem -->

Few GRBs lie at z < 0.1, so E_iso or L cannot be computed without a
cosmology: fitting a correlation in an assumed model and then using it to
constrain models is circular. Three answers are in use.

- *Calibration on SNe Ia.* Interpolate the SN Ia distance modulus at each
  GRB redshift in the overlap range, calibrate the relation there, and
  extrapolate; from 42 GRBs at 1.4 < z ≤ 6.6 this gave flat-ΛCDM
  Ω_M = 0.25 (+0.04/−0.05) (Liang et al. 2008, arXiv:0802.4262) `[src]`. A
  2025 version calibrates the Amati relation of the A219 sample on
  Pantheon+ with neural networks and, with H(z) data, finds CPL w0 = −1.02
  (+0.67/−0.50), w_a = −0.98 ± 0.58 (Huang et al. 2025, arXiv:2506.08929)
  `[src]`. The calibrated GRBs then inherit the SN Ia distance scale and its
  systematics; they add only the extrapolation in redshift.
- *Calibration on H(z) or HII galaxies.* Cosmic chronometers or HII galaxies
  replace SNe as the low-z anchor (CosmoVerse cites a chronometer-calibrated
  platinum subset at 0.553 ≤ z ≤ 1.96 with σ_int = 0.20 (+0.03/−0.05)
  `[sec: arXiv:2504.01669, Sect. 2.1.16]`). Calibrated on 186 HII galaxy
  distances below z = 2.6, the Amati relation has an intrinsic scatter of
  about 28% and 35% in two data sets, too large for precision cosmology
  (Okazaki & Desai 2025, arXiv:2510.22979) `[src]`.
- *Simultaneous fit.* Fit correlation and cosmological parameters together
  and test that the correlation does not depend on the model. Graziani
  argues that circularity disappears if the correlation is mapped to the
  primitive observables (fluence) and fitted there (Graziani 2010,
  arXiv:1002.3434) `[src]`. Of eight data sets tested this way, only an
  Amati sample of 118 bursts (A118) is judged reliable; its constraints are
  consistent with flat ΛCDM and "significantly weaker" than BAO + H(z), and
  no reliable "Combo"-correlation sample could be defined (Khadka et al.
  2021, arXiv:2105.12692) `[src]`.

### 3.3 Current constraints
<!-- key: current-constraints -->

- No GRB-only result constrains Ω_m or w at a level comparable to SNe Ia or
  BAO; published fits are consistent with flat ΛCDM (arXiv:2105.12692,
  arXiv:2209.08675) `[src]`. An early review already named the lack of
  low-redshift bursts as the limit (Ghirlanda et al. 2006,
  arXiv:astro-ph/0610248) `[src]`.
- A joint fit of GRBs, HII galaxies and quasar angular sizes with H(z) and
  BAO gives Ω_m0 = 0.313 ± 0.013 and H0 = 69.3 ± 1.2 km/s/Mpc, the three
  high-z sets being mutually consistent (Cao et al. 2020,
  arXiv:2009.12953) `[src: abstract]`; most of the weight is in H(z) + BAO.
- H0 from GRBs is set by the calibrator: CosmoVerse quotes 73.23 ± 3.31 and
  72.87 ± 2.92 km/s/Mpc without and with evolution correction, both with
  SN-based priors `[sec: arXiv:2504.01669, Sect. 2.1.16]`; such values are not
  independent of the SN Ia ladder.
- Redshift evolution of the prompt relations: a 241-burst Swift sample shows
  no systematic or significant evolution of the Amati or Yonetoku relations
  (Hasan & Azzam 2026, arXiv:2603.08884) `[src]`; the Dainotti relations are
  corrected for evolution in their own analyses (arXiv:2209.08675) `[src]`.
- **Forecast:** about 66 optical plateau GRBs would give σ_w ≈ 0.47 in wCDM,
  comparable to Planck alone (Dainotti et al. 2026, arXiv:2603.18223)
  `[src]`.

### 3.4 What a referee checks
<!-- key: what-a-referee-checks-2 -->

- Which calibrator sets the distance scale (SNe, H(z), HII galaxies), and
  whether its covariance is propagated.
- Whether the correlation parameters are shown to be independent of the
  cosmology and of redshift bins.
- Sample selection (gold/platinum subsets chosen for small scatter) and the
  instrument mix (Swift, Fermi, BeppoSAX thresholds).
- Whether a "tension with ΛCDM" survives a direct model fit rather than a
  cosmographic expansion (see §2.3).

## 4. HII galaxies and giant HII regions
<!-- key: hii-galaxies-and-giant-hii-regions -->

### 4.1 Method
<!-- key: method -->

HII galaxies are compact starbursts in dwarf galaxies, selected by
EW(Hβ) > 50 Å (ages below ~5 Myr); giant extragalactic HII regions (GEHRs)
are their analogues in the outer discs of late-type spirals
`[sec: arXiv:2504.01669, Sect. 2.1.10]`. The distance indicator is the
L(Hβ)–σ relation between the Balmer-line luminosity and the velocity
dispersion of the ionised gas, log L(Hβ) = α + β log σ. For 128 local
(0.02 ≲ z ≲ 0.2) HII galaxies the relation is stable against sample cuts;
adding the size of the star-forming region, equivalent width, colour or
metallicity gives the smallest scatter, δ log L(Hβ) = 0.233, and the
coefficients are close to those of virialised ionising clusters (Chávez et
al. 2014, arXiv:1405.4010) `[src]`. The zero point α comes from GEHRs in an
"anchor" sample of galaxies with Cepheid (or TRGB) distances, which makes
the probe an alternative third rung for H0 and a Hubble diagram to z ~ 7
and beyond with JWST NIRSpec (Hβ and [OIII] to z ~ 9)
`[sec: arXiv:2504.01669, Sect. 2.1.10]`.

### 4.2 Samples and results
<!-- key: samples-and-results -->

| Analysis | Sample | Result as stated | Citation |
|---|---|---|---|
| Fernández-Arenas et al. 2018 | 36 GEHRs in 13 anchor galaxies (incl. NGC 4258) + local HII galaxies | H0 = 71.0 ± 2.8 (random) ± 2.1 (systematic) km/s/Mpc `[src: abstract]` | arXiv:1710.05951 |
| Chávez et al. 2016 | 25 HII galaxies to z ~ 2.33, with CMB + BAO | 13% improvement of quintessence constraints over BAO + CMB; **forecast:** substantial gain with 500 high-z objects `[src]` | arXiv:1607.06458 |
| González-Morán et al. 2019 | 15 new Keck/MOSFIRE (1.3 ≤ z ≤ 2.5) + 31 high-z + 107 at z ≤ 0.15 | Ω_m = 0.290 (+0.056/−0.069); flat {Ω_m, w0} = {0.280 (+0.130/−0.100), −1.12 (+0.58/−0.32)} (stat) `[src: abstract]` | arXiv:1906.02195 |
| Chávez et al. 2024 | 231 GEHRs and HII galaxies to z ≈ 7.5, some JWST | flat {h, Ω_m, w0} = {0.731 ± 0.039, 0.302 (+0.12/−0.069), −1.01 (+0.52/−0.29)} (stat) `[src]` | arXiv:2404.16261 |
| Chávez et al. 2026 | 243 objects, z ~ 0 to z ~ 14, JWST and ALMA+JWST, lensing magnification modelled | flat ΛCDM h = 0.725 ± 0.040, Ω_m = 0.308 (+0.043/−0.053); CPL w0 = −0.92 (+0.57/−0.34), w_a = −0.48 (+0.60/−1.50); no evidence of evolution of the relation `[src: abstract]` | arXiv:2607.14254 |

CosmoVerse (Table 2) gives, for 195 HII galaxies alone with the slope
fixed, flat-ΛCDM Ω_m = 0.282 (+0.037/−0.045)
`[sec: arXiv:2504.01669, Sect. 2.1.10, Table 2]`. The H0 values (71–73) rest
on Cepheid-distance anchors and so share the first two rungs of the SH0ES
ladder, not its SNe; an error of 4.0 km/s/Mpc puts 67 and 73 only 1.5 sigma apart
`[der: (73 − 67)/4.0, error of arXiv:2607.14254]`.

### 4.3 Systematics
<!-- key: systematics -->

- *Unexplained scatter.* The scatter of L–σ is significantly larger than
  the observational errors; age differences between bursts do not explain
  it, because most HII galaxies host several bursts of slightly different
  ages and the equivalent width is not a reliable age clock; the authors
  conclude the accuracy is unlikely to improve soon and that larger
  samples "may or may not" help (Melnick & Telles 2024, arXiv:2407.18704)
  `[src]`.
- *Line-width measurement:* instrumental and thermal broadening, profile
  "Gaussianity" cuts (which reduce the sample, arXiv:1405.4010), and at
  high z the conversion from [OIII] to Balmer widths (arXiv:2607.14254)
  `[src]`.
- *Extinction and lensing magnification* at high redshift
  (arXiv:2607.14254) `[src]`.
- *Anchor:* GEHRs in Cepheid hosts against compact HII galaxies, two
  populations assumed to share one relation.

### 4.4 What a referee checks
<!-- key: what-a-referee-checks -->

Slope fitted with or without the high-z points; anchor sample and its
distance scale; whether the constraint is statistical only (most are
labelled "stat"); profile and extinction cuts; for z > 3, the [OIII]-to-Hβ
transformation and magnification model.

## 5. Redshift drift (Sandage–Loeb test)
<!-- key: redshift-drift-sandage-loeb-test -->

**Method.** The redshift of a comoving source changes in real time as
ż = (1 + z) H0 − H(z), or as an apparent acceleration
dv/dt0 = c H0 [1 − E(z)/(1 + z)]; the derivation uses only the null geodesic
and the definitions of z and H (Moresco et al. 2022, arXiv:2201.07241)
`[src: Sect. 3.11.1, Eqs. 133–135]`. Proposed by Sandage (1962) for galaxies
and by Loeb for the Lyα forest of quasars, where the shift is "a few m/s
over a century" (Loeb 1998, arXiv:astro-ph/9802122) `[src]`. It needs no
candle, ruler or ladder, and its sign is a direct test of acceleration.

**Signal size.** The apparent acceleration peaks at about 0.4 cm s⁻¹ yr⁻¹ at
z ≃ 0.76, ż peaks at ~2 × 10⁻¹¹ yr⁻¹ (~H0/3) near z ≃ 1.1, and ż = 0 near
z ≈ 2.5 for Ω_m ≈ 0.27 in flat ΛCDM, so the Lyα forest at z > 2.5 sees
deceleration `[src: arXiv:2201.07241, Sect. 3.11.1]`.

**Current measurement.** The ESPRESSO experiment, three epochs over ~2 yr on
one z = 3.962 quasar, finds v̇ = −3.5 ± 3.6 m s⁻¹ yr⁻¹, a null result
consistent with ΛCDM; systematics are subdominant at that noise
(Trost et al. 2026, arXiv:2603.02318) `[src]`. The error is about three orders
of magnitude above the signal `[der: 3.6 m s⁻¹ yr⁻¹ against ~0.4 cm s⁻¹ yr⁻¹]`.

**Forecasts.** A 42-m telescope would detect the drift in ~20 yr with
4000 h on the Lyα forest at 2 < z < 5 (Liske et al. 2008,
arXiv:0802.1532) **forecast** `[src]`; ESPRESSO + ANDES would reach a first
detection before 2080, about 10 yr sooner with low-z HI 21-cm absorption from
radio facilities (arXiv:2603.02318) **forecast** `[src]`. Radio forecasts:
~800 HI absorbers from one year of the FAST CRAFTS survey (Jiao et al. 2019,
arXiv:1905.01184) **forecast** `[src]`; SKA HI 21-cm emission and absorption
near z ~ 1 (Kang et al. 2025, arXiv:2501.15117) **forecast** `[src]`. A
combined optical + radio programme gives ±2% on H0 and Ω_m in flat ΛCDM but
~40% with Ω_Λ free and 17% on H0, ±0.1 on w0, ±0.3 on w_a in flat w0waCDM
`[src: arXiv:2201.07241, Sect. 3.11.5]` **forecast**.

**Systematics and referee checks.** Wavelength calibration stable over decades
(laser combs, local oscillators); peculiar accelerations of order
1 cm s⁻¹ yr⁻¹ inside galaxies and clusters, with the Solar-System barycentre
at ~0.7 cm s⁻¹ yr⁻¹, which add noise; Lyα-forest peculiar accelerations are
much smaller than the signal except near the zero crossing, gas in galaxies
(21-cm targets) up to 2 dex larger `[src: arXiv:2201.07241, Sect. 3.11.4]`.
A referee asks for the baseline, the calibration chain, the model of
peculiar accelerations, and whether a constraint is measured or forecast; no
detection exists.

## 6. Galaxy-scale strong-lens statistics as a geometric probe
<!-- key: galaxy-scale-strong-lens-statistics-as-a -->

Time-delay H0: `physics-and-methods.md` §4, `deep/time-delay-cosmography.md`.
Without delays, lenses give only distance ratios: Ω_m, Ω_Λ, w, never H0.

**Distance ratio from Einstein radius and velocity dispersion.** For a
singular isothermal sphere θ_E = 4π (σ²/c²) D_ls/D_s (textbook), so a lens
with a measured Einstein radius and stellar velocity dispersion gives
D_ls/D_s. From 53 SLACS lenses, flat Ω_Λ = 0.75 ± 0.17 and γ_PPN = 1.01 ±
0.05, but with the warning that the results are unlikely to become precise
unless mass profile, velocity anisotropy, light profile and the dispersion
measurement are constrained far better (Schwab et al. 2010,
arXiv:0907.4992) `[src]`. A 118-lens catalogue (SLACS, BELLS, LSD, SL2S)
fits w or CPL with a power-law slope γ(z) free to evolve
(Cao et al. 2015, arXiv:1509.07649) `[src]`. Ignoring the redshift evolution
of the mass-density slope biases Ω_m by up to ~10σ in LSST-size mocks;
modelling it recovers the input, ΔΩ_m ≃ 0.01 and Δw ≃ 0.1 for ~10⁴ lenses
(Geng et al. 2026, arXiv:2603.04279) **forecast** `[src]`.

**Double-source-plane lenses.** The ratio of the two Einstein radii depends
only on distance ratios, is independent of H0, and has an Ω_m–w degeneracy
almost orthogonal to that of the CMB and BAO; a handful of systems would give
~15% on w (Collett et al. 2012, arXiv:1203.2758) **forecast** `[src]`. Euclid
Q1 found four candidates in 63 deg², consistent with a LensPop prediction of
6 ± 3, and the full survey is predicted to find 1700
(Euclid Collaboration: Li et al. 2025, arXiv:2503.15327) **forecast** `[src]`.

**Lens counts.** The fraction of multiply imaged sources grows with the volume
to the source, hence with Ω_Λ. CLASS radio lenses gave flat Ω_m = 0.31
(+0.27/−0.14) (stat) (+0.12/−0.10) (sys) and w < −0.55 (+0.18/−0.11)
(Chae et al. 2002, arXiv:astro-ph/0209602) `[src]`; replacing the
luminosity function plus Faber–Jackson by the measured SDSS velocity-dispersion
function removes a bias toward overconfident constraints, giving flat
Ω_Λ = 0.74–0.78 (Mitchell et al. 2004, arXiv:astro-ph/0401138) `[src]`. The
final SQLS sample, 19 lensed quasars from 50,836 sources, gives flat
Ω_Λ = 0.79 (+0.06/−0.07) (stat) ± 0.06 (sys), assuming a non-evolving velocity
function (Oguri et al. 2012, arXiv:1203.1088) `[src]`. These are
confirmations of acceleration, not competitive measurements: the predicted
counts depend on the evolution of the early-type lens population, so lens
counts are judged unlikely to compete as a dark-energy probe (Weinberg et al.
2013, arXiv:1201.2434) `[src: Sect. 7.10]`.

**Next samples (forecasts).** Euclid Q1 (0.45% of the survey) yielded ~500
high-quality candidates, supporting the forecast of over 100,000 lenses
(Lines et al. 2025, arXiv:2508.14624) **forecast** `[src]`. For LSST, a
photometric sample of 100,000 lenses with up to 50% false positives would give
σ(Ω_m, Ω_Λ, w) = 0.1, 0.03, 0.15 in wCDM, equivalent to 2500–3500
spectroscopic systems (Holloway et al. 2026, arXiv:2609.21699)
**forecast** `[src]`. For CSST, 10,000 lenses with dispersions would give
σ(Ω_m) = 0.01 in ΛCDM and σ(w) = 0.04 (Wu et al. 2025, arXiv:2511.08030)
**forecast** `[src]`.

**What a referee checks.** The mass model (SIS or power law; slope evolution
with redshift); velocity anisotropy and aperture correction of σ; for counts,
the selection function and the velocity-dispersion function and its
evolution; for photometric samples, the purity model; that the claimed
constraint is not H0 (distance ratios only).

## 7. Cosmic chronometers and combinations (pointers)
<!-- key: cosmic-chronometers-and-combinations-pointers -->

Chronometers (H(z) from differential ages of passive galaxies) are covered
in this skill: method in `physics-and-methods.md` §5, data in
`surveys-and-data.md` §7, values in `results.md`, systematic budget in
`systematics.md` §15. Joint fits of quasars, GRBs and HII galaxies are
dominated by the BAO and H(z) data they are combined with (§3.3,
arXiv:2009.12953) `[src]`; state a claimed departure from ΛCDM above z ~ 2
per probe and per calibration. The SN-side reading is in `cosmo-supernovae`
(`open-questions.md`).

## Not verified
<!-- key: not-verified -->

- Sandage (1962) is cited through arXiv:2201.07241 only; its DOI was not
  read.
- No double-source-plane cosmological measurement (as opposed to forecasts)
  was read this session.
- Radio redshift-drift forecasts for CHIME and the Cooke (2020) programme
  are named in arXiv:2201.07241 but were not read.
