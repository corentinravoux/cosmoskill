# Systematics — multi-messenger cosmology

Scope: the canonical systematics of siren, FRB and lensed-transient cosmology — mechanism, size where a paper quantifies it, mitigation, validation test, and the reference a referee expects.
Snapshot: 2026-10-13 (deepening pass, 12–13 October; first build 2026-10-07, searches 2026-10-10)

Provenance flags as in the other files. Sizes are quoted from the cited abstract unless
a section, table, figure or equation is named inside the flag.

## 1. Peculiar velocity of the host (bright sirens)
<!-- key: peculiar-velocity-of-the-host-bright-sirens -->

**Mechanism.** At low redshift `c z_obs = H0 d + v_p`. The siren gives `d`; H0 needs
the Hubble-flow part of the recession velocity, so `v_p` must be subtracted and its
error propagated: `δH0 / H0 ≈ σ_v / (H0 d)`.

**Size.**

| Statement | Value | Source |
|---|---|---|
| Typical peculiar velocity and its share of the recession velocity at 40 Mpc | 300 km/s, about 10% | arXiv:1710.05835 Methods [src: Sect. "Finding the Hubble velocity of NGC 4993"] |
| LVC 2017 correction for NGC 4993 | 310 ± 69 km/s from 6dFGSv; error inflated to 150 km/s, 250 km/s as a robustness test | [sec: arXiv:1909.00587 §3.2]; confirmed in arXiv:1710.05835 [src: Methods] |
| Where the 150 km/s comes from | it is the uncertainty of the 2MASS Redshift Survey reconstruction used as a cross-check (Hubble velocity 3047 km/s against 3017 from 6dFGSv), adopted because the 6dFGSv estimate "may represent an imperfect model of the true bulk flow" | arXiv:1710.05835 [src: Methods] |
| Hubble velocity used | 3017 ± 166 km/s, that is 5.5% [der: 166/3017], against about 15% on the GW distance | arXiv:1710.05835 [src: Methods] |
| Size in H0 of widening the velocity error from 150 to 250 km/s | MAP interval from 70.0 (+12.0/−8.0) to 70.0 (+14.0/−9.0); symmetric interval from 74.0 (+16.0/−8.0) to 74.0 (+16.0/−9.0) | arXiv:1710.05835 [src: Extended Data Table 1] |
| After a jet prior | the H0 error is "dominated by both the GW data and the peculiar motion of NGC 4993", no longer by the viewing angle | arXiv:1806.10596 [src: main text] |
| BORG reconstruction on 2M++ | mean 373 km/s, mode 385 km/s; field σ ≈ 82 km/s, virial term ≈ 100 km/s, total ≈ 130 km/s; mean 24% higher and σ 13% smaller than LVC | arXiv:1909.08627 §6.1 [src] |
| Sensitivity | 200 km/s on `v_p` ↔ about 4 km/s/Mpc on H0 | arXiv:1909.09609 [src: abstract] |
| Dependence on the velocity source, same siren data | H0 = 70.9 (+6.4/−8.5) with DESI Fundamental Plane velocities, 73.4 (+3.3/−3.9) with the Cosmicflows-4 SBF velocity | arXiv:2512.08818 [src: abstract] |
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
<!-- key: inclination-distance-degeneracy-and -->

**Mechanism.** The amplitude constrains a combination of `d_L` and `cos i`. External
viewing-angle information removes most of the H0 error and replaces it by a model of
the jet or the ejecta.

**Size.**

- GW170817 alone: 14% on H0; with a jet prior 6–7% (arXiv:2305.19914, arXiv:1806.10596)
  [src].
- Budget of the distance in LVC 2017: `d = 43.8 (+2.9/−6.9)` Mpc, "∼15%" from detector
  noise, calibration and the correlation with inclination together, not separated;
  `cos i` in [−1.00, −0.81] (144°–180°) at 68.3%. The degeneracy is called "one of the
  main sources of uncertainty" on H0 (arXiv:1710.05835) [src: main text].
- The degeneracy read the other way: with H0 fixed to the Planck value the 68.3%
  range of the inclination is 157°–177°, with the SH0ES value 148°–166°
  (arXiv:1710.05835) [src: main text, Extended Data Table 1].
- Jet-model dependence inside one analysis: 68.9 (+4.6/−4.5), 68.3 (+4.4/−4.3) and
  68.5 (+4.4/−4.3) for a hydrodynamical, a power-law and a Gaussian jet, a spread of
  0.6 [der] called "much smaller than 7%"; the GW-only value of that paper is
  74 (+16/−8), and 78 (+20/−10) against 74 (+15/−8) for the low- and high-spin priors
  of the GW analysis, a dependence that disappears once the jet data are added
  (arXiv:1806.10596, HTML rendering) [src: main text, Methods §0.2].
- Spread between jet-informed analyses of the same event: 64.8 to 75.5 (results file,
  §1) [der].
- Requirement: a viewing-angle bias above about 10° gives more than 3% on H0
  (arXiv:2006.02779) [src].
- Selection: counterparts are easier to find for some viewing angles, which biases H0
  by 2% or more even for mild selection, and the bias "cannot be properly removed" with
  the GW inclination measurement (arXiv:2006.02779) [src].
- Distance prior: volumetric against uniform changes the weighted median by 10
  km/s/Mpc for the GW-only posterior (arXiv:2606.30504) [src].
- Redshift prior in place of the distance prior: LVC 2017 repeat the analysis with a
  prior flat in `z` instead of `p(d) ∝ d²` and find 71.0 (+23.0/−9.0) (MAP) or
  81 (+27/−13) (median), against 70.0 (+12.0/−8.0) and 74.0 (+16.0/−8.0), a change of
  "less than 1σ" of the canonical statistical error (arXiv:1710.05835) [src: Extended
  Data Table 1].

**Mitigation.** Fit the jet geometry with a continuum of models and all VLBI epochs
(arXiv:2605.11437); use an independent distance to the host only as a cross-check
(arXiv:1801.06080); model the electromagnetic selection (arXiv:1908.06050).

**Validation.** H0 with and without the electromagnetic prior; with several jet
structures; re-sampling under each distance prior.

**Expected citations.** arXiv:1806.10596, arXiv:2006.02779, arXiv:2305.19914,
arXiv:2605.11437.

## 3. Detector calibration and waveform systematics
<!-- key: detector-calibration-and-waveform-systematics -->

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
  stays inside after 100 (arXiv:2204.03614) [src: abstract].
- Next-generation golden dark sirens: waveform and calibration accuracy must improve as
  `O(ρ⁻²)` with signal-to-noise `ρ`; waveform bias can change the host ranking
  (arXiv:2602.14898) [src].
- One 2026 analysis carries an explicit calibration term, ±1.56 on 70.5
  (arXiv:2607.03672) [src].

- GW170817: calibration enters the "∼15%" distance error without a separate figure;
  tidal terms in the waveform and the data-processing method change H0 and the
  inclination by "much smaller than the statistical uncertainties" (arXiv:1710.05835)
  [src: main text, Methods].
- Waveform choice in the LVK cosmology sample: one approximant per event
  (IMRPhenomXPHM for O1–O3, IMRPhenomXPHM_SpinTaylor for O4) instead of a mixture, "to
  mitigate potential systematics"; waveform systematics are otherwise not propagated,
  being "expected to be relevant only in population analyses of GW events with SNR
  above 100". One event, GW231123_135430, is excluded because its masses and distance
  "vary dramatically with different waveforms" (arXiv:2605.27227) [src: Sect. III.1].
- Lensing magnification of the distance: weak lensing adds "variance on the luminosity
  distance of individual sirens at the level of a few percent", against a measurement
  error of about 20% for the best GWTC-3 source, and does not bias the mean; the
  probability that a GWTC-3 event is strongly lensed is below one percent. Both are
  ignored (arXiv:2111.03604) [src: Sect. V.3].

**Mitigation.** Marginalise over calibration envelopes in parameter estimation;
compare waveform families (arXiv:2009.14199 does this for GW190521, with H0 moving
from 43 to 62 between three models [src]).

**Expected citations.** arXiv:2005.02531, arXiv:2204.03614.

## 4. Selection effects
<!-- key: selection-effects -->

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

**What the LVK analyses do.** The cosmology sample is cut at a false-alarm rate below
0.25 yr⁻¹ and `ξ` is computed by re-weighting injections passed through the same
threshold (arXiv:2605.27227 [src: Sect. III.1]; arXiv:2509.04348 [src: Appendix A]).

| Check | Result | Place read |
|---|---|---|
| Accuracy of `ξ`: effective number of injections above `4 N_obs` (at least 564 for 141 events); raised to 2000 or removed | "no evidence of systematic bias" | arXiv:2509.04348 [src: Sect. IV.3] |
| Per-event Monte Carlo threshold `n_eff,PE` from 10 to 50, or none; `var(ln L) < 1` instead | effect "negligible for the models considered" | arXiv:2509.04348 [src: Sect. IV.3] |
| Stricter event selection, inverse false-alarm rate above 1 yr | the only GWTC-5.0 variation whose median leaves the 68% interval of the others (it stays inside the 90% interval) | arXiv:2605.27227 [src: Appendix E] |
| Electromagnetic selection of bright sirens | not modelled; GW170817 is combined a posteriori; "will need to be included in expectation of more bright siren events" | arXiv:2605.27227 [src: Sect. V.2] |
| Same, in the 2017 analysis | ignored on the argument that the BNS horizon was about 190 Mpc and the counterpart, about 17 mag in `I` at 40 Mpc, would be about 22 mag at 400 Mpc; redshift corrections to the detectability are below 5% inside the horizon, so the selection term is constant in H0 | arXiv:1710.05835 [src: Methods] |

**Validation.** Mock data challenges with the full chain (arXiv:1908.06050,
arXiv:2103.14663); probability–probability tests on injections.

**Expected citations.** arXiv:1809.02063, arXiv:2212.08694. General statistics:
`cosmo-statistics-inference`.

## 5. Population (mass-spectrum) mis-specification
<!-- key: population-mass-spectrum-mis-specification -->

**Mechanism.** Without a counterpart the redshift information is `m_det / m_src`. Any
error in the assumed source-frame spectrum, or any unmodelled change of that spectrum
with redshift, is absorbed by H0.

**Size.**

| Statement | Source |
|---|---|
| GWTC-3 catalogue result "strongly impacted by assumptions about the BBH source mass distribution"; only GW190814 is not | arXiv:2111.03604 [src] |
| GWTC-5.0: "the main driver of the Hubble constant measurement remains the presence of features in the mass distribution"; H0 "strongly degenerate" with the positions of sharp features; a model lacking high-mass structure shifts redshifts up and H0 higher | arXiv:2605.27227 §4.1 [src] |
| 2000 events analysed with heuristic mass models when the true spectrum evolves or has unmodelled features: H0 biased by up to 3σ | arXiv:2312.11627 [src] |
| Same study, by model: on a population-synthesis catalogue, H0 lies 2σ from the injected value with the multi-peak model and 3σ with Power Law + Peak (σ of each H0 posterior), although both reproduce the detector-frame spectrum; the bias "disappears when the redshift evolution of the source mass spectrum is removed". Direction: an underestimated source-mass spectrum sends events to higher redshift and H0 up | arXiv:2312.11627 [src: Sect. V] |
| Blinded mock challenge at O4 sensitivity: a mild unmodelled redshift dependence gives about 1.5σ | arXiv:2412.14244 [src] |
| Second blinded challenge: the metallicity dependence of the spectrum and its interplay with the delay-time distribution must be captured, to better than the statistical error at all relevant redshifts | arXiv:2604.26273 [src] |
| GWTC-4.0 with evolving mass scales: no compelling evidence for evolution; a modest shift of H0 to lower values that injections reproduce for a non-evolving truth; the systematic from the choice of redshift-independent mass model is larger | arXiv:2605.20112 [src] |
| GWTC-5.0 with a copula mass–redshift dependence: H0 consistent between models, the independent model favoured | arXiv:2609.25662 [src] |
| A new mass feature at 63.3 ± 4.8 M☉ tightens H0 by 30–36% | arXiv:2601.03257 [src] |
| Population prescriptions from synthesis codes: H0 degenerate with the fraction of dynamically formed binaries | arXiv:2603.15332 [src] |
| Fixed population parameters in a catalogue analysis bias H0; joint inference is required | arXiv:2103.14663, arXiv:2308.02281 [src] |

Sizes read in the body of the LVK papers (H0 in km s⁻¹ Mpc⁻¹, median and 68.3%
interval unless stated; dark sirens without GW170817):

| Variation | H0 | Place read |
|---|---|---|
| GWTC-5.0, multi-peak BBH-only model (231 events) | 70.6 (+20.3/−16.7) | arXiv:2605.27227 [src: Table 3] |
| GWTC-5.0, FullPop-4.0, fiducial (235 events) | 68.8 (+14.2/−13.2) | same |
| GWTC-5.0, FullPop 3 Peaks (235 events) | 71.1 (+12.9/−12.1) | same |
| GWTC-5.0, spectral, BBH-only, Gaussian spin model against Transition spin model | 72.4 (+22.5/−18.3) against 67.0 (+21.9/−17.6); modelling spins widens the error by 8.8% and 5.3% | arXiv:2605.27227 [src: Sect. IV.1, V.2] |
| GWTC-4.0, single-peak (Power Law + Peak) against multi-peak, BBH only | 124.8 (+45.2/−39.4) against 87.3 (+48.0/−28.2): medians about 47% apart, the first limited by the prior edge at 200 | arXiv:2509.04348 [src: Sect. IV.1] |
| GWTC-4.0, prior on the peak positions | the Bayes factor between those two models goes from `log10 B = 0.30` to 2.3 when the peak priors are narrowed from U(5, 100) M☉ to U(7, 12) and U(20, 50) M☉ | arXiv:2509.04348 [src: Sect. IV.1] |
| GWTC-3, fixed population, peak position `μ_g` moved in steps of about 2.5 M☉ (its uncertainty) | "strong impact": a higher `μ_g` gives a lower H0 and the reverse; raising `m_max` to 150 M☉ has no significant effect; a rate slope `γ = 2.59` instead of 4.59 moves the peak higher and widens it | arXiv:2111.03604 [src: Sect. V.2, Fig. 11] |

The mechanism in the collaboration's words: a model lacking a low-mass peak "prefers
lower masses to account for the missing first peak, which puts GW sources at higher
redshifts, therefore leading to higher H0" (arXiv:2509.04348) [src: Sect. IV.1]. Within
one release the model-to-model shift of the median (about 2 between the three GWTC-5.0
models [der: Table 3]) is far below the statistical error, but between a model that
misses a feature and one that has it the shift was about 37 in GWTC-4.0 [der: 124.8 −
87.3]. Mass-spectrum evolution is not modelled in any LVK result: the GWTC-3 paper
calls mass-model mis-specification "the dominant source of systematic uncertainty" and
states that "any evolution is degenerate with the cosmological inference"
(arXiv:2111.03604) [src: Sect. V.3]. The priors on the population parameters are part
of the result: "significantly extending the prior range of the population parameters
could alter the reconstructed mass spectra" (arXiv:2605.27227) [src: Sect. V.2].

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
<!-- key: galaxy-catalogue-completeness-and-host-weighting -->

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
| Photometric against spectroscopic | precision degraded by up to a factor of about 9 (**forecast**, O5, 100 best events) | arXiv:2312.05302 [src: abstract] |
| Magnitude errors and K-corrections | minor at `z < 0.2` | arXiv:2608.26307 [src] |
| Pipeline dependence | the two LVK pipelines treat completeness differently and find different gains from the catalogue | arXiv:2605.27227 §4.1 [src] |

What the catalogue adds, and how much of the sky volume it covers, as read in the LVK
papers:

| Quantity | Value | Place read |
|---|---|---|
| GLADE+ `K_s` selection | 37 201 deg², 9.9 × 10⁵ galaxies, median `z` 0.08, median `σ_z/(1+z)` 0.014; 77% photometric redshifts | arXiv:2605.27227 [src: Table 1, Sect. III.2] |
| DES Y6 `r` band | 5169 deg², 3.5 × 10⁸ galaxies, median `z` 0.85, median `σ_z/(1+z)` 0.096 | same |
| Share of the total GW localisation volume inside the complete part of the catalogue, `f_cov` | GLADE+ 5% (23% for the twenty best-localised events); DES 7% (17%) | arXiv:2605.27227 [src: Table 1] |
| DES in-catalogue range | `0.05 < z < 0.35`; lower cut for saturated nearby galaxies, upper cut where `n(z)` stops agreeing with uniform-in-comoving-volume within 1σ; 99.9% complete at `z = 0.35` for `m_thr = 23.8`, `M_min = −16.33` | arXiv:2605.27227 [src: Sect. III.2] |
| Gain in H0 precision over the spectral-only result, GWTC-5.0 | DES 3.5% (2% with `icarogw`, 8% with `gwcosmo`); GLADE+ 2.8% | arXiv:2605.27227 [src: Sect. IV.1] |
| Same, GWTC-4.0 with GLADE+ | 8.6% (3.1% for the second, parenthesised figure, which in that paper is the 90% interval) | arXiv:2509.04348 [src: Sect. IV.1] |
| Same, GWTC-3 with fixed population | 67 (+13/−12) with GLADE+ against 67 (+14/−13) with an empty catalogue | arXiv:2111.03604 [src: Sect. IV.2] |
| The one informative event of GWTC-3 | GW190814, about 18 deg²: 67 (+46/−28) (MAP), from an excess of `K`-band galaxies near `z ≈ 0.051` that is not seen in the `B_J` band | arXiv:2111.03604 [src: Sect. IV.2] |
| Weighting on or off, GWTC-5.0 and GWTC-4.0 | "differences well within statistical error"; `log10 B = −0.02` between weighted and unweighted in GWTC-4.0 | arXiv:2605.27227 [src: Sect. IV.1]; arXiv:2509.04348 [src: Sect. IV.1] |
| Galaxies per event | events overlapping a catalogue hold `O(10³–10⁵)` galaxies in their volume | arXiv:2605.27227 [src: Sect. V.2] |

Sizes read in the bodies of the papers of the table above:

| Issue | Size or statement | Place read |
|---|---|---|
| Redshift range kept from a photometric catalogue (GWTC-4.0 × DES Y6, `gwcosmo`, dark sirens only) | median H0 from 72.1 (+24.6/−19.9) at `z_max = 0.20` to 65.7 (+26.9/−19.8) at `z_max = 0.50`, lower cut 0.05; without the lower cut 79.5, 77.5 and 79.8 at `z_max` = 0.20, 0.35, 0.50; empty catalogue 74.5 (+27.3/−20.7), GLADE+ 79.6 (+27.3/−18.5). A range of 14 [der] from catalogue cuts alone, inside the statistical error of about 20 | arXiv:2602.04766 [src: Table 2 of the HTML rendering, an earlier version: its fiducial cut is `0.05 < z < 0.35` and 70.9 (+22.3/−18.6), the current abstract gives `0.05 < z < 0.50` and 71.7 (+22.7/−18.3)] |
| Why the cuts move H0 | above `z ≈ 0.4` the `n(z)` departs from uniform in comoving volume and the prior peak sits at the near side of events with support at `z ≳ 0.5`, which lowers H0; removing `z < z_min` de-weights low redshift and raises H0 | arXiv:2602.04766 [src: Sect. 4, same version] |
| Wrong host weighting, three regimes in the number of galaxies per line of sight `N_GAL` | below about 100: no bias for any weighting; above about 10⁵ ("uninformative"): H0 tends to the value that matches the distance distribution to the wrongly weighted `n(z)`; between: transitional. Mocks are 100% complete | arXiv:2405.14818 [src: Sect. III.1, III.2, V] |
| Why it does not show in LVK results yet | the catalogue result with `K`-band weighting is about 18% and the fixed-population spectral one about 20%: "dominated by uncertainties associated with the GW population" | arXiv:2405.14818 [src: Sect. V, on GWTC-3] |
| Completion scheme | tested on 10⁶ simulated galaxies; variance completion beats homogeneous and multiplicative completion for completeness `f ≥ 0.15`; not propagated to H0 ("the next stage of this work") | arXiv:2310.08991 [src: Sect. 4] |

Unmodelled choices that the GWTC-5.0 paper lists itself [src: Sect. V.2]: missing
galaxies uniform in comoving volume (no clustering); a redshift-independent Schechter
function even for DES depth; Gaussian redshift errors; GLADE+ being a union of
catalogues with "incongruent magnitude limits", whose effect "is not yet fully
understood"; and overdensities in the DES `n(z)` that persist over the whole footprint
and "may also originate from biased spectroscopic training data". The Bayes factors
between catalogues also compare "the specific choices made in the construction of the
galaxy catalog prior" [src: Sect. IV.1].

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
<!-- key: fast-radio-bursts-host-and-milky-way-dispersion -->

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

**7.7 Sizes read in the bodies.** "σ" in the rows from arXiv:2507.18946 is the
statistical error of that analysis, about 2 km s⁻¹ Mpc⁻¹ on 71.28, for H0 alone.

| Term | Size or statement | Place read |
|---|---|---|
| Host DM model | replacing simulation-based `(μ_host, σ_host)` by a log-normal of median 100 and σ 50 pc cm⁻³ lowers H0 by more than 3σ | arXiv:2507.18946 [src: Sect. IV.4] |
| Host DM form | log-normal "has limited theoretical motivation"; published per-burst estimates of 30–81 and below 70 pc cm⁻³ | arXiv:2005.13161 [src: Methods §0.5] |
| Host outliers | removing FRB 20190520B changes H0 by less than 0.1σ, because the tails of the likelihood are long; one poorly localised burst in the dense part of the sample changes it by about 0.8σ | arXiv:2507.18946 [src: Sect. IV.1] |
| Galactic disc model | NE2001 against YMW16 without a latitude cut: about 1.6σ; range of H0 over latitude cuts 2.1σ (NE2001), 1.3σ (YMW16); converges after a cut, `|b| > 15°` adopted, which removes 18 of 117 bursts | arXiv:2507.18946 [src: Sect. IV.1, IV.2] |
| Galactic disc, selection | at `DM_ISM = 500` pc cm⁻³ the detection rate falls by 20% (Parkes) to 50% (ASKAP at 900 MHz) and the mean detected redshift by up to 17% | arXiv:2208.00819 [src: Appendix A.2] |
| Galactic halo | fixed values in use: 50, 65 or 30 pc cm⁻³; a disc-plus-sphere model gives 30 to 245 across the sky; fixing 50 instead of that model lowers H0 by more than 2.7σ | arXiv:2507.18946 [src: Sect. IV.3] |
| Galactic halo, earlier practice | 50 pc cm⁻³ assumed, expected range 50–100, "largely degenerate" with the host model | arXiv:2005.13161 [src: main text]; arXiv:2208.00819 [src: Sect. 2.1] |
| Scatter of the cosmic term and feedback | `σ_DM = F z^(−0.5)`; `F` = 0.09, 0.15, 0.32 in semi-analytic models where haloes below 10¹⁴, 10¹³, 10¹¹ M☉ are evacuated of gas, that is strong to weak feedback (a smaller `F` is a smoother universe) | arXiv:2005.13161 [src: Methods §0.5]; arXiv:2208.00819 [src: Sect. 7.2] |
| `F` in H0 | from `F = 10^(−0.75)` to 0.32: H0 up by about 2.9σ; to 0.09: down by about 3.9σ | arXiv:2507.18946 [src: Sect. IV.4] |
| `F` measured | `log10 F = −0.48 (+0.26/−0.18)`, obtained only with an H0 prior between the CMB and supernova values; "strong degeneracy" with H0; `F = 0.32` in earlier work was "somewhat arbitrarily" adopted and partly absorbed by `σ_host` | arXiv:2305.07022 [src: Sect. IV.1, IV.2]; arXiv:2208.00819 [src: Sect. 7.2] |
| `f_d` | 30% on the stellar mass density gives 4% on `f_d(z = 0)` and about 2.5% at `z = 1`; H0 scales with the assumed fraction, by 0.93/0.865 between two published values (7.5% [der]) | arXiv:2208.00819 [src: Sect. 7.2]; arXiv:2507.18946 [src: Sect. IV.4] |
| `Ω_b h²` | fixed; its uncertainty is of order 0.5–1%, "negligible" at present | arXiv:2208.00819 [src: Sect. 2.1, 7.2] |
| Feedback in the baryon partition | `f_IGM ≈ 0.6` at `z < 1` in SIMBA without feedback, above 85% with AGN feedback, about 80% in IllustrisTNG; halo gas fraction 0.35 (+0.30/−0.25) of `Ω_b/Ω_M` for 10⁹–5 × 10¹² M☉; the authors name over-fitting to one simulation as a risk | arXiv:2409.16952 [src: main text, Methods] |
| Fixing the nuisance parameters | gives "a biased and artificially too-precise" H0 even at their best-fit values | arXiv:2208.00819 [src: Sect. 5.1] |
| Asymmetric posterior (the "cliff effect") | a void still contributes a minimum `DM_cosmic`, so `P(DM | z)` has a sharp lower edge: a low H0, which raises the minimum DM at each `z`, is excluded by a single low-DM burst, while a high H0 is only mildly penalised; one burst (FRB 20190102) drives the preference of one survey | arXiv:2208.00819 [src: Sect. 5.1] |

Three of these shifts (host model, halo, `F`) are each larger than the quoted
statistical error of the tightest FRB H0, which is why that value is statistical only.

**Validation for §7.** H0 with each Galactic model; with and without the lowest-
redshift bursts; with the host median free; with two forms of `p(DM | z)`; with
unlocalised bursts added through a selection model.

**Expected citations.** arXiv:2005.13161, arXiv:2208.00819, arXiv:2305.07022,
arXiv:2507.07090.

## 8. Lensed transients: lens model, microlensing, mass sheet (pointer)
<!-- key: lensed-transients-lens-model-microlensing-mass -->

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

Sizes read in the bodies (H0 in km s⁻¹ Mpc⁻¹):

| Term | Size or statement | Place read |
|---|---|---|
| Lens model, SN Refsdal | two closely related models carry 0.44 and 0.51 of the weight (0.95 together); budget built on one of them: about 5% on H0, the principal dark-matter halo of the cluster being the largest term; image separation alone gives 5.5% and explains about 92% of the delay variance; the same code applied to a simulated cluster recovers delays with a slope of 1.046 ± 0.021 | arXiv:2305.06367 [src: main text, "Systematic uncertainties and error budget", "Analytical expectation"] |
| Delay against model, SN Refsdal | delay measured to 1.5% [der: 5.6/376]; a 3% delay corresponds to 6% on H0 | same |
| Matter density, SN Refsdal | varying Ω_M with H0 leaves residuals of about 0.7, "likely to be an upper limit" | arXiv:2305.06367 [src: Supplementary] |
| Budget, SN H0pe | about 9% in total: two fifths from photometry and spectroscopy (each delay about 8%, 5.6% effective), three fifths from lens modelling, of which one quarter within the dominant model (6.5% on H0 by itself) and three quarters the spread between models | arXiv:2403.18902 [src: Sect. X.5] |
| Lens model, SN Encore | per-model H0 from 59.5 (+9.8/−6.6) to 106.4 (+31.8/−35.8); two models carry 0.845 and 0.147 of the weight, the others below 0.01 | arXiv:2509.12301 [src: Table 6] |
| Mass sheet, cluster lenses | reduced by multiple-image systems at several redshifts, not eliminated; magnifications measured to about 25% exclude `|Δλ| ≳ 0.1` each, and `Δλ ≈ 0.05` halves the weight of the best SN H0pe model; several models match the magnification ratios and not the absolute magnifications | arXiv:2403.18902 [src: Sect. X.3] |
| Mass sheet, galaxy lenses | same quasar data: 74.2 ± 1.6 with `λ_int = 1` imposed (power-law profiles) against 74.5 (+5.6/−6.1) with `λ_int` free, 2% against 8% [der]; 71.6 (+3.9/−3.3) with the 2025 kinematics (velocity dispersions to 4.0% instead of 7.7%); 73.7 (+4.7/−4.4) with a uniform Ω_m prior on [0.05, 0.5] in place of Pantheon+; `κ_ext` of order 10⁻² | arXiv:2506.03023 [src: Sect. 3.1, 10.1.1] |
| Radial profile, SN 2025wny | 66.7 (+7.6/−6.3) with isothermal profiles, 70.8 (+8.2/−6.1) with free slopes; the constraint is dominated by the spectroscopic A–D delay, measured to about 5% | arXiv:2608.28427 [src: Sect. VI.2] |
| Microlensing, SN Encore | chromatic, because the data lie after the first three rest-frame weeks; 1000 simulated curves per image; added to the delay distribution, of which most of the width comes from the time of peak of the reference image | arXiv:2509.12301 [src: Sect. V.1] |
| Microlensing, SN 2025wny | analysis choices move the delays by at most 2.2 and 2.9 days, 0.7σ of the statistical error, the largest for a peak-only fit, attributed to microlensing not captured by the magnification model | arXiv:2608.28427 [src: Sect. VI.1] |
| Millilensing by subhaloes | 29% added uncertainty on the magnifications of SN Encore for a 5% substructure fraction, against 10% for SN Refsdal; this weakens the standard-candle route to the mass sheet | arXiv:2509.12301 [src: Sect. V.2] |
| Post-unblinding changes | Refsdal: a sign of the magnification in the weights, and a change of weighting observable worth 0.1 | arXiv:2305.06367 [src: main text] |

Details for lensed quasars and kinematics: `cosmo-distance-ladder-h0`.

## 9. What a referee checks
<!-- key: what-a-referee-checks -->

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

16. Number and independence of lens models, weighting and the share of the weight held
    by one model, mass-sheet or profile-slope treatment, blinding protocol and
    post-unblinding changes, microlensing treatment, Ω_m assumption.

## Not verified
<!-- key: not-verified -->

- The calibration uncertainty of the O4 data was not read; the numbers above are for O3.
- The calibration envelope of the GW170817 strain data: the source-properties paper of
  the event has no HTML rendering and could not be read; §3 gives only what
  arXiv:1710.05835 says.
- Tables 2 to 5 of arXiv:2507.18946 (the H0 value of each variation) and the table of
  microlensing delay shifts of arXiv:2509.12301 were not read; §7.7 and §8 quote the
  shifts in σ and the statements given in the text.
- Table 2 of arXiv:2602.04766 was read in an earlier version of the paper than the
  current abstract (§6); the table of the current version was not read.
- The H0 inference for SN 2025wny is made in a companion paper (Mörtsell et al.) that
  was not fetched; §8 quotes it as reported in arXiv:2608.28427. [src: abstract]
- Weak-lensing magnification of siren distances: §3 now gives the LVK statement for
  GWTC-3 ("a few percent"); no number was read for third-generation or LISA sources
  beyond arXiv:astro-ph/0504616.
- Environmental effects on the waveform (line-of-sight acceleration) appeared in a 2026
  title but were not read.
- The Trott & Huterer paper itself was not fetched.
- Waveform-systematics sizes for current detectors, beyond the GW190521 comparison.
