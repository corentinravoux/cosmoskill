# Systematics — multi-messenger cosmology

Scope: the canonical systematics of siren, FRB and lensed-transient cosmology — mechanism, size where a paper quantifies it, mitigation, validation test, and the reference a referee expects.
Snapshot: 2026-10-07 (suite date; literature searches run 2026-10-10)

Provenance flags as in the other files. Sizes are quoted from the cited abstract unless
a section is named.

## 1. Peculiar velocity of the host (bright sirens)

**Mechanism.** At low redshift `c z_obs = H0 d + v_p`. The siren gives `d`; H0 needs
the Hubble-flow part of the recession velocity, so `v_p` must be subtracted and its
error propagated: `δH0 / H0 ≈ σ_v / (H0 d)`.

**Size.**

| Statement | Value | Source |
|---|---|---|
| Typical peculiar velocity and its share of the recession velocity at 40 Mpc | 300 km/s, about 10% | arXiv:1710.05835 Methods [src] |
| LVC 2017 correction for NGC 4993 | 310 ± 69 km/s from 6dFGSv; error inflated to 150 km/s, 250 km/s as a robustness test | [sec: arXiv:1909.00587 §3.2] |
| BORG reconstruction on 2M++ | mean 373 km/s, mode 385 km/s; field σ ≈ 82 km/s, virial term ≈ 100 km/s, total ≈ 130 km/s; mean 24% higher and σ 13% smaller than LVC | arXiv:1909.08627 §6.1 [src] |
| Sensitivity | 200 km/s on `v_p` ↔ about 4 km/s/Mpc on H0 | arXiv:1909.09609 [src] |
| Dependence on the velocity source, same siren data | H0 = 70.9 (+6.4/−8.5) with DESI Fundamental Plane velocities, 73.4 (+3.3/−3.9) with the Cosmicflows-4 SBF velocity | arXiv:2512.08818 [src] |
| Catalogue disagreement | 2MTF and CF3/6dFGSv velocities at NGC 4993 differ by more than their errors for kernels of 2–10 h⁻¹ Mpc, traced to a global distance-scale offset between catalogues | arXiv:1909.00587 §3.2 [src] |
| Correlated errors | H0 error up to ×2 larger when the velocity covariance is included, for GW170817-like sirens within 50 Mpc with 5% distances | arXiv:2509.03101 [src] |

Scaling with distance, for a fixed velocity error and H0 = 70 [der: `σ_v / (H0 d)`]:

| `σ_v` | 40 Mpc | 100 Mpc | 200 Mpc | 400 Mpc |
|---|---|---|---|---|
| 150 km/s | 5.4% | 2.1% | 1.1% | 0.5% |
| 250 km/s | 8.9% | 3.6% | 1.8% | 0.9% |

**Components to keep apart.**

1. The observed redshift to use: the galaxy, or the centre of mass of its group. LVC
   2017 used the group, assuming all members at the same distance, accurate to 1% for a
   group radius of about 0.4 Mpc (arXiv:1710.05835 Methods) [src]. Group membership of
   NGC 4993 was debated until the DESI observations found 39 members and a halo of order
   `10^13 M☉` (arXiv:2512.08818) [src]. Mukherjee et al. used `10^12 M☉` for the virial
   term (arXiv:1909.08627 §6.1) [src]; the two masses differ by an order of magnitude,
   and the virial dispersion with them.
2. The large-scale flow at the host position, from a reconstruction or from smoothed
   direct distances. The smoothing scale is a free choice with a direct effect
   (arXiv:1909.09609).
3. The non-linear motion inside the halo, added as a dispersion.
4. The zero point of the direct-distance catalogue. Velocities from Tully–Fisher or
   Fundamental-Plane distances depend on the distance zero point of the catalogue: a
   small global offset between the 2MTF and CF3 distance scales produces a large
   difference at NGC 4993 (arXiv:1909.00587 §3.2) [src]. LVC 2017 state that they do not
   use a secondary distance indicator for the Hubble-flow velocity of NGC 4993, so that
   H0 stays independent of the electromagnetic distance scale, and correct the group
   velocity with a peculiar-velocity map instead (arXiv:1710.05835 Methods) [src].

**Does it average down?** Howlett & Davis 2019 state that the error decreases as
sirens are found at larger distance and as random directions average. Blake & Turner
2025 show the limit of the second argument: velocities of nearby hosts are correlated
through bulk flows, so `N` sirens within 50 Mpc do not give `1/√N`. Both statements are
correct in their regime; the covariance matters for the nearby, well-measured events
that would otherwise dominate the weight.

**Mitigation.** Marginalise over the kernel scale (arXiv:1909.09609); model-average
over catalogues and group definitions (arXiv:1909.00587); use a posterior ensemble from
a non-linear reconstruction (arXiv:1909.08627); observe the environment
spectroscopically (arXiv:2512.08818); include the full covariance (arXiv:2509.03101).

**Validation.** Compare reconstructions against direct distances at the host position
(arXiv:2502.00121); repeat the H0 inference with each velocity model and report the
spread; check the dependence on the fiducial cosmology used to build the reconstruction.

**Expected citations.** arXiv:1909.00587, arXiv:1909.08627, arXiv:1909.09609,
arXiv:2509.03101. Velocity-field methodology: `cosmo-peculiar-velocities`.

## 2. Inclination–distance degeneracy and electromagnetic viewing-angle priors

**Mechanism.** The amplitude constrains a combination of `d_L` and `cos i`. External
viewing-angle information removes most of the H0 error and replaces it by a model of
the jet or the ejecta.

**Size.**

- GW170817 alone: 14% on H0; with a jet prior 6–7% (arXiv:2305.19914, arXiv:1806.10596)
  [src].
- Spread between jet-informed analyses of the same event: 64.8 to 75.5 (results file,
  §1) [der].
- Requirement: a viewing-angle bias above about 10° gives more than 3% on H0
  (arXiv:2006.02779) [src].
- Selection: counterparts are easier to find for some viewing angles, which biases H0
  by 2% or more even for mild selection, and the bias "cannot be properly removed" with
  the GW inclination measurement (arXiv:2006.02779) [src].
- Distance prior: volumetric against uniform changes the weighted median by 10
  km/s/Mpc for the GW-only posterior (arXiv:2606.30504) [src].

**Mitigation.** Fit the jet geometry with a continuum of models and all VLBI epochs
(arXiv:2605.11437); use an independent distance to the host only as a cross-check
(arXiv:1801.06080); model the electromagnetic selection (arXiv:1908.06050).

**Validation.** H0 with and without the electromagnetic prior; with several jet
structures; re-sampling under each distance prior.

**Expected citations.** arXiv:1806.10596, arXiv:2006.02779, arXiv:2305.19914,
arXiv:2605.11437.

## 3. Detector calibration and waveform systematics

**Mechanism.** A strain-amplitude calibration error is a distance error of the same
fractional size and is common to all events of a run. Waveform errors bias distance
and, for dark sirens, the three-dimensional localisation.

**Size.**

- LIGO in the first half of O3: below 7% in magnitude and 4° in phase (68%), of which
  the systematic part is below 2% and 2° (arXiv:2005.02531) [src]. Chen 2020 quotes
  "≤ 2%" as the calibration contribution to the standard-siren systematic
  (arXiv:2006.02779) [src].
- With the worst O3 calibration error applied to every event, the true H0 leaves the
  90% interval after about 40 binary neutron stars; with 10% of events affected, it
  stays inside after 100 (arXiv:2204.03614) [src].
- Next-generation golden dark sirens: waveform and calibration accuracy must improve as
  `O(ρ⁻²)` with signal-to-noise `ρ`; waveform bias can change the host ranking
  (arXiv:2602.14898) [src].
- One 2026 analysis carries an explicit calibration term, ±1.56 on 70.5
  (arXiv:2607.03672) [src].

**Mitigation.** Marginalise over calibration envelopes in parameter estimation;
compare waveform families (arXiv:2009.14199 does this for GW190521, with H0 moving
from 43 to 62 between three models [src]).

**Expected citations.** arXiv:2005.02531, arXiv:2204.03614.

## 4. Selection effects

**Mechanism.** Detection depends on `d_L`, masses and orientation; the population is
defined in redshift and source-frame mass. The detectable fraction `ξ(Λ)` therefore
depends on H0 (physics file, §5).

**Known failure modes.**

- Omitting or mis-normalising the selection term produces a biased H0 on mocks. The
  bias claimed for the catalogue method by Trott & Huterer (2021, as cited in
  arXiv:2212.08694) is attributed to this and to inconsistent mock generation; Gair et
  al. show an unbiased posterior when the method is applied correctly [src].
- Electromagnetic selection for bright sirens (§2) and the galaxy-catalogue flux limit
  for dark sirens (§6) are selection effects on the redshift side and need their own
  terms (arXiv:1908.06050).
- Bright and dark sirens share a population; treating them as independent biases the
  inferred low-mass end of the mass spectrum (arXiv:2609.12053) [src].

**Validation.** Mock data challenges with the full chain (arXiv:1908.06050,
arXiv:2103.14663); probability–probability tests on injections.

**Expected citations.** arXiv:1809.02063, arXiv:2212.08694. General statistics:
`cosmo-statistics-inference`.

## 5. Population (mass-spectrum) mis-specification

**Mechanism.** Without a counterpart the redshift information is `m_det / m_src`. Any
error in the assumed source-frame spectrum, or any unmodelled change of that spectrum
with redshift, is absorbed by H0.

**Size.**

| Statement | Source |
|---|---|
| GWTC-3 catalogue result "strongly impacted by assumptions about the BBH source mass distribution"; only GW190814 is not | arXiv:2111.03604 [src] |
| GWTC-5.0: "the main driver of the Hubble constant measurement remains the presence of features in the mass distribution"; H0 "strongly degenerate" with the positions of sharp features; a model lacking high-mass structure shifts redshifts up and H0 higher | arXiv:2605.27227 §4.1 [src] |
| 2000 events analysed with heuristic mass models when the true spectrum evolves or has unmodelled features: H0 biased by up to 3σ | arXiv:2312.11627 [src] |
| Blinded mock challenge at O4 sensitivity: a mild unmodelled redshift dependence gives about 1.5σ | arXiv:2412.14244 [src] |
| Second blinded challenge: the metallicity dependence of the spectrum and its interplay with the delay-time distribution must be captured, to better than the statistical error at all relevant redshifts | arXiv:2604.26273 [src] |
| GWTC-4.0 with evolving mass scales: no compelling evidence for evolution; a modest shift of H0 to lower values that injections reproduce for a non-evolving truth; the systematic from the choice of redshift-independent mass model is larger | arXiv:2605.20112 [src] |
| GWTC-5.0 with a copula mass–redshift dependence: H0 consistent between models, the independent model favoured | arXiv:2609.25662 [src] |
| A new mass feature at 63.3 ± 4.8 M☉ tightens H0 by 30–36% | arXiv:2601.03257 [src] |
| Population prescriptions from synthesis codes: H0 degenerate with the fraction of dynamically formed binaries | arXiv:2603.15332 [src] |
| Fixed population parameters in a catalogue analysis bias H0; joint inference is required | arXiv:2103.14663, arXiv:2308.02281 [src] |

**Mitigation.** Infer population and cosmology jointly; allow the mass scales to
evolve; use the whole spectrum so that several features must conspire
(arXiv:2202.08240); use flexible or non-parametric spectra (arXiv:2404.02210); check
that independent features give the same H0 (arXiv:2410.07416).

**Validation.** Repeat with at least two mass-model families and report the shift;
Bayes factors between them (arXiv:2605.27227 reports a mild preference for a three-peak
variant over its fiducial model [src]); blinded mock challenges.

**Also in this class.** The background model: an H0 from sources at `z ≈ 0.4–0.8`
depends on Ω_m and on the assumed expansion history (arXiv:2511.11795,
arXiv:2609.12053), and on general-relativistic propagation (arXiv:2112.05728).

**Expected citations.** arXiv:2103.14663, arXiv:2312.11627, arXiv:2412.14244,
arXiv:2202.08240.

## 6. Galaxy-catalogue completeness and host weighting

**Mechanism.** The catalogue is flux-limited. Beyond its completeness distance the
redshift prior is the completion model, which carries no H0 information by itself and
can carry bias.

**Size.**

| Issue | Statement | Source |
|---|---|---|
| Depth of the standard catalogue | GLADE+ complete to 47 (+4/−2) Mpc in B-band luminosity | arXiv:2110.06184 [src] |
| Completion model | homogeneous completion underestimates and multiplicative completion overestimates the structure at low completeness | arXiv:2310.08991 [src] |
| Gain from modelling the line of sight | 23% better H0 precision at 24% completeness, 37% at 8%, up to 66% (mocks, `z ≤ 0.4`) | arXiv:2608.24992 [src] |
| How shallow is enough | the brightest 1% suffice for well-localised events if faint hosts cluster around bright galaxies; biased without clustering or for large volumes | arXiv:2511.04786 [src] |
| Features in the photometric `n(z)` | "significant features in the galaxy redshift distribution which can introduce biases"; the DES Y6 analysis cuts to `0.05 < z < 0.50` | arXiv:2602.04766 [src] |
| Host weighting | a wrong weighting scheme biases H0 through the assumed redshift distribution and through favouring wrong hosts | arXiv:2405.14818 [src] |
| Choice of band | B-band against K-band weighting changes the posterior as much as the largest uncertainty effect tested | arXiv:2608.26307 [src] |
| Redshift errors | ignoring photometric-redshift errors gives a bias comparable with other GWTC-3 systematics, still below the statistical error | arXiv:2302.12037 [src] |
| Photometric against spectroscopic | precision degraded by up to a factor of about 9 (**forecast**, O5, 100 best events) | arXiv:2312.05302 [src] |
| Magnitude errors and K-corrections | minor at `z < 0.2` | arXiv:2608.26307 [src] |
| Pipeline dependence | the two LVK pipelines treat completeness differently and find different gains from the catalogue | arXiv:2605.27227 §4.1 [src] |

**Mitigation.** Infer the weighting exponent with the cosmology (arXiv:2609.04991, the
first analysis to do so [src]); use clustering-informed completion; restrict to events
inside the complete volume; obtain spectroscopy for the best-localised events
(arXiv:2607.17284, **forecast**); use cross-correlation, which does not need the host
in the catalogue (arXiv:2007.04271).

**Validation.** H0 with weighting on and off and with two bands; with and without the
catalogue (the difference is the catalogue's information); null test with a
randomised or rotated catalogue.

**Expected citations.** arXiv:2110.06184, arXiv:2212.08694, arXiv:2405.14818,
arXiv:2310.08991.

## 7. Fast radio bursts: host and Milky Way dispersion, scatter, selection

**7.1 Host contribution.** Unknown per burst and broad: mean rest-frame 90 (+29/−19)
pc cm⁻³ for FLIMFLAM, median 186 (+59/−48) pc cm⁻³ in the ASKAP analysis
(arXiv:2402.00505, arXiv:2208.00819) [src]. It is degenerate with H0 at low redshift
where `DM_cosmic` is small. Outliers in extreme environments (FRB 20190520B) must be
treated explicitly (arXiv:2507.18946) [src]. Mitigation: fit the host distribution;
use per-burst foreground information (arXiv:2506.04186).

**7.2 Milky Way.** The disc model and the halo term (50–80 pc cm⁻³,
arXiv:1901.11051 [src]) are subtracted from every burst; a common error is a common
shift. Xu et al. 2025 list the Galactic electron-density model and the halo
contribution among the choices that move H0 (arXiv:2507.18946) [src]; the inferred
diffuse baryon fraction is sensitive to the same choice (arXiv:2506.03536) [src].

**7.3 Cosmic scatter.** `p(DM | z)` is skewed and its width depends on feedback. The
fluctuation parameter is degenerate with H0 (arXiv:2305.07022) [src]. Simulation-based
shapes carry method errors: more than 50% on the standard deviation from sparse
snapshot sampling, more than 8% on the DM signal for boxes below 35 h⁻¹ Mpc or coarse
resolution (arXiv:2507.07090) [src]. The choice of a Gaussian or a skewed form changes
cosmographic parameters, the deceleration parameter in particular (Lemos, Gonçalves &
Alcaniz 2026, abstract read; not in the source list, which was already over its cap).

**7.4 The `Ω_b f_d`–H0 degeneracy.** Any H0 from the mean relation is conditional on
`Ω_b h²` and `f_d` (physics file, §7.2). An analysis that fixes `f_d` to a simulation
value quotes a statistical error only.

**7.5 Selection.** High-DM bursts are smeared and scattered and are detected less
often; the telescope beam and the burst width shape the observed `p(z, DM)`. James et
al. 2022 model these and obtain a larger H0 error than fits that do not
(arXiv:2208.00819) [src]. CHIME infers a large population with scattering above 10 ms
at 600 MHz of which it sees a small fraction (arXiv:2106.04352) [src].

**7.6 Host association.** Associations are probabilistic and biased toward bright,
nearby hosts when ambiguous cases are dropped (arXiv:2609.04765) [src]. FRB hosts are
a biased tracer of star formation (arXiv:2409.16964) [src].

**Validation for §7.** H0 with each Galactic model; with and without the lowest-
redshift bursts; with the host median free; with two forms of `p(DM | z)`; with
unlocalised bursts added through a selection model.

**Expected citations.** arXiv:2005.13161, arXiv:2208.00819, arXiv:2305.07022,
arXiv:2507.07090.

## 8. Lensed transients: lens model, microlensing, mass sheet (pointer)

- **Lens-model spread.** Cluster-lensed supernovae use seven or eight independent mass
  models; "the range of admissible H0 values predicted across the lens models limits
  further precision" (arXiv:2403.18902) [src]. Model weighting changes Refsdal from
  64.8 to 66.6 (arXiv:2305.06367) [src].
- **Mass-sheet degeneracy.** For lensed quasars the treatment of the degeneracy sets the
  error: the same siren-plus-lens combination gives 13.6% with the TDCOSMO-2025
  hierarchy and 5.6% with assumed profiles (arXiv:2606.03634) [src]. A lensed Type Ia
  supernova breaks it with its absolute magnification (arXiv:2403.18902).
- **Microlensing and millilensing.** Simulated as additional systematics on the delay
  for SN Encore (arXiv:2509.12301) [src]; a time-dependent relative magnification of one
  image had to be modelled for SN 2025wny (arXiv:2608.28427) [src].
- **Time-delay precision.** 39.8 (+3.9/−3.3) days for Encore, about 9% [der]; template
  imaging would improve it (arXiv:2509.12301) [src].
- **Blinding.** Standard in this subfield (physics file, §8).

Details for lensed quasars and kinematics: `cosmo-distance-ladder-h0`.

## 9. What a referee checks

Bright siren:

1. Which recession velocity (galaxy or group) and which peculiar-velocity model; the
   H0 shift between at least two velocity models; the velocity error and whether the
   virial term is included.
2. Whether the velocity product carries a distance-scale zero point.
3. Covariance between hosts if more than one nearby siren is combined.
4. Viewing-angle information: its source, the jet model, and H0 without it.
5. Distance prior and H0 prior, with the inference re-sampled under the alternative.
6. Summary statistic (MAP or median) and interval definition.

Dark siren:

7. Population fixed or inferred; the mass model family; H0 under a second family.
8. Whether redshift evolution of the mass scales is allowed, and the shift when it is.
9. The spectral-only result next to the catalogue result, so that the catalogue's
   contribution is visible.
10. Catalogue completeness as a function of redshift along the lines of sight used;
    completion scheme; host weighting and band; photometric-redshift treatment.
11. Selection function: injection set, threshold, consistency with the event list.
12. Pipeline (`gwcosmo` or `icarogw`) and whether both were run.
13. Background model and Ω_m prior; whether `Xi_0` is fixed to 1.
14. For a combination with GW170817: which GW170817 posterior, and no double use of
    the event in the dark-siren sample.

FRB:

15. `Ω_b h²` prior, `f_d` assumption, Galactic and halo DM model, host-DM model,
    form of `p(DM | z)`, sample selection and outlier policy, statistical-only or
    total error.

Lensed transient:

16. Number and independence of lens models, weighting, blinding protocol, microlensing
    treatment, Ω_m assumption.

## Not verified

- The calibration uncertainty of the O4 data was not read; the numbers above are for O3.
- Weak-lensing magnification of siren distances (named in arXiv:astro-ph/0504616 for
  LISA sources) was not quantified from a current paper.
- Environmental effects on the waveform (line-of-sight acceleration) appeared in a 2026
  title but were not read.
- The Trott & Huterer paper itself was not fetched.
- Waveform-systematics sizes for current detectors, beyond the GW190521 comparison.
