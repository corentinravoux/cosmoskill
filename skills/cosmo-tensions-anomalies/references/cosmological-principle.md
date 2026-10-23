# Cosmological principle — homogeneity, isotropy, inhomogeneous models, local void

Scope: observational tests of the cosmological principle (statistical
homogeneity and isotropy on large scales, hence an FLRW background):
the homogeneity scale from galaxy and quasar surveys; isotropy as a pointer
to the dipole and CMB material of this skill; inhomogeneous alternatives to
dark energy (LTB void models, backreaction, timescape); and the local-void
(KBC) explanation of the Hubble tension with its critiques.
Snapshot: 2026-10-22

Flags as in `results.md`: `[src]` read this session in the cited paper's
abstract; `[src: <place>]` in its body; `[sec: X]` taken from the named
secondary source; `[der]` derived here. Field map: CosmoVerse white paper
(Di Valentino et al. 2025, arXiv:2504.01669), Sects. 4.5.1 (local void) and
4.6 (cosmological principle). Several of the papers below are written by
the proponents of the model they test; each claim is attributed.

## 1. What is tested
<!-- key: what-is-tested -->

The cosmological principle is the assumption that the Universe is
statistically homogeneous and isotropic on large scales, so that distances
and ages are computed in the FLRW metric (CosmoVerse, arXiv:2504.01669,
Sect. 4.6.1; DESI DR1 test, arXiv:2606.07854) `[src]`. The Copernican
principle, that we do not occupy a special place, is the weaker assumption
that turns observed isotropy into homogeneity (textbook). Tests fall in
three groups:

| Group | What is measured | Where in this skill |
|---|---|---|
| Statistical homogeneity | transition of counts-in-spheres to N ∝ r³; fractal dimension D₂ → 3 | §2 below |
| Statistical isotropy | number-count, redshift and SN dipoles against the CMB dipole; large-angle CMB anomalies; bulk flow | §3 below (pointer) |
| Model-based | fits of inhomogeneous metrics or averaged cosmologies (LTB, Λ LTB, timescape) and of a local underdensity | §§4–5 below |

A large single structure does not by itself falsify homogeneity, which is a
statement about averages: the algorithm that found the "Huge-LQG" finds
even larger Gpc-scale groups in homogeneous Poisson simulations of the same
density (Nadathur 2013, arXiv:1306.1700) `[src]`.

## 2. Statistical homogeneity: the homogeneity scale
<!-- key: statistical-homogeneity-the-homogeneity-scale -->

### 2.1 Estimators
<!-- key: estimators -->

For spheres of comoving radius r centred on survey objects, homogeneity
means a mean count N(<r) ∝ r³, i.e. a correlation dimension
D₂(r) = d ln N / d ln r = 3. The homogeneity scale R_H is conventionally the
radius above which D₂ stays within 1% of 3 (D₂ > 2.97); this definition was
introduced with WiggleZ as more robust and comparable between surveys
(Scrimgeour et al. 2012, arXiv:1205.6812) `[src]` and adopted by BOSS
(Ntelis et al. 2017, arXiv:1702.02159) `[src]` and eBOSS quasars (Gonçalves
et al. 2020, arXiv:2010.06635) `[src]`. An angular version θ_H, computed in
thin redshift shells, avoids converting redshifts to distances with a
fiducial cosmology (Lopes-Dias et al. 2026, arXiv:2606.07854) `[src]`.

### 2.2 Measurements
<!-- key: measurements -->

| Sample | Redshift | Result as stated | Citation |
|---|---|---|---|
| SDSS LRGs | z ~ 0.3 (0.2–0.35) | N(R) ∝ R³ above R ~ 70 h⁻¹ Mpc; rms density variation 7% among ten ~2 × 10⁷ h⁻³ Mpc³ regions, consistent with biased ΛCDM `[src]` | Hogg et al. 2004, arXiv:astro-ph/0411197 |
| WiggleZ, > 200,000 blue galaxies, ~1 (h⁻¹ Gpc)³ | 0.2–0.8 | R_H = 71 ± 8, 70 ± 5, 81 ± 5, 75 ± 4 h⁻¹ Mpc at z ~ 0.2, 0.4, 0.6, 0.8; a fractal with D₂ < 2.97 excluded on ~80–300 h⁻¹ Mpc at 99.99% `[src]` | arXiv:1205.6812 |
| BOSS DR12 CMASS, 3 h⁻³ Gpc³ | 0.43–0.7 | R_H = 63.3 ± 0.7 h⁻¹ Mpc against a ΛCDM prediction of 62.0; D₂ compatible with 3 above 300 h⁻¹ Mpc in all bins `[src]` | arXiv:1702.02159 |
| SDSS DR7 quasars | z ~ 1.3 | homogeneous above at most 130 h⁻¹ Mpc `[src]` | arXiv:1306.1700 |
| SDSS-IV DR16 quasars | 2.2–3.2 | R_H decreasing with redshift, in good agreement with ΛCDM `[src]` | arXiv:2010.06635 |
| DESI DR1 LRGs (angular θ_H) | 0.4–1.1 | θ_H identified in all shells, consistent with ΛCDM mocks, with eBOSS DR16 and between the two Galactic caps `[src]` | arXiv:2606.07854 |

### 2.3 How to read these numbers
<!-- key: how-to-read-these-numbers -->

- R_H is a consistency test of ΛCDM, not a model-free proof: its value
  depends on the 1% threshold, the tracer bias and the redshift, and is
  compared with a ΛCDM prediction (arXiv:1702.02159) `[src]`.
- The selection function is estimated from the same data and is partly
  degenerate with the density field; in a toy model with density
  oscillations of the survey's size, conventional selection-function
  estimates bias counts towards homogeneity and underestimate R_H by ~40%,
  a model-dependent figure (Heinesen 2020, arXiv:2006.15022) `[src]`.
- Volume-limited counts measure homogeneity of the tracer, not of the
  matter; isotropy is tested separately (§3).

**What a referee checks.** Definition of R_H (threshold, estimator,
randoms); fiducial cosmology used to convert redshifts, or an angular
statistic; selection-function and mask treatment; comparison with mocks
of the same tracer rather than with an analytic curve; whether a single
"giant structure" is being read as a violation of homogeneity.

## 3. Statistical isotropy (pointer)
<!-- key: statistical-isotropy-pointer -->

Isotropy is covered in this skill and not repeated here: the number-count
(Ellis–Baldwin), redshift and supernova dipoles in `physics-and-methods.md`
§6, `results.md` §7 and `deep/cosmic-dipoles.md`; large-angle CMB
anomalies in `physics-and-methods.md` §7, `results.md` §9 and
`deep/large-angle-cmb-anomalies.md`; the bulk flow in
`physics-and-methods.md` §8 and `results.md` §8. In one line: the
number-count dipole is 4.9–5.7σ above the kinematic expectation for
CatWISE but 3.3–3.6σ with clustering-aware mocks, and
the CMB large-angle anomalies are 2–3σ after look-elsewhere correction
`[sec: this skill, SKILL.md and results.md §§7, 9]`. A detected redshift
drift would also probe isotropy and FLRW directly (Moresco et al. 2022,
arXiv:2201.07241) `[src: Sect. 3.11.5]`; no detection exists (see
`cosmo-distance-ladder-h0`, `references/alternative-distance-probes.md` §5).

## 4. Inhomogeneous cosmologies
<!-- key: inhomogeneous-cosmologies -->

### 4.1 LTB void models: why they were ruled out as an alternative to dark energy
<!-- key: ltb-void-models-why-they-were-ruled-out-as-an -->

The Lemaître–Tolman–Bondi metric is spherically symmetric and radially
inhomogeneous, ds² = −c²dt² + R′(r,t)²/[1 + 2E(r)] dr² + R(r,t)² dΩ²
(CosmoVerse, arXiv:2504.01669) `[src: Sect. 4.6.2.a, Eq. 4.25]`. An
observer near the centre of a Gpc-scale underdensity sees SN distances that
mimic acceleration without dark energy; the low-redshift shape of d_L(z)
at z ~ 0.1–0.4 discriminates the two (Clifton et al. 2008,
arXiv:0807.1443) `[src]`. The models failed on several independent tests:

- *Kinetic SZ.* Radial inhomogeneity large enough to replace dark energy
  produces a kSZ power spectrum far above the ACT/SPT upper limit, which
  "rules out the adiabatic void model" and confirms the Copernican
  principle at Gpc radial scales (Zhang & Stebbins 2010, arXiv:1009.3967)
  `[src]`. A fully relativistic treatment weakens the kSZ bound but a very
  large class of void models remains ruled out by kSZ combined with other
  methods (Zibin & Moss 2011, arXiv:1105.0909) `[src]`. Freeing the bang
  time function does not reconcile SNe, the small-angle CMB, the local
  Hubble rate and kSZ simultaneously (Bull et al. 2011, arXiv:1108.2222)
  `[src]`.
- *CMB, local H0, age and structure.* With SNe, the full CMB spectrum, radial
  BAO, local H0, age, BBN, the Compton-y distortion and σ8, void models
  predict a very low local Hubble rate, an "old age problem" and too little
  local structure (Moss et al. 2010, arXiv:1007.3725) `[src]`.
- *BAO.* Adding BAO gives Ω_in > 0.2 against Ω_in < 0.15 from SNe, 3σ
  apart, and constrained adiabatic profiles are "ruled out at high
  confidence" by purely geometric probes (Zumalacárregui et al. 2012,
  arXiv:1201.2790) `[src]`.

**Λ LTB (a void plus Λ).** Data now constrain small departures rather than
replacements of dark energy. ΛLTB models confronted with many data sets do
not resolve the Hubble tension; viable inhomogeneities must be a few Gpc
across with the observer close to the centre to avoid large dipoles
`[sec: arXiv:2504.01669, Sect. 4.6.3.d]`. As an alternative to dynamical
dark energy: DESI DR2 BAO + Planck + any of Union3, Pantheon+, DES-SN5YR or
DES-Dovekie show no preference between w0wa and ΛLTB; adding kSZ excludes
much of the parameter space, but a ~300 h⁻¹ Mpc region with ~10% density
excess remains allowed (Zhang & Zhang 2026, arXiv:2610.05729) `[src]`.

### 4.2 Backreaction
<!-- key: backreaction -->

Spatially averaging Einstein's equations gives Friedmann-like equations for
an effective volume scale factor with a backreaction source term that can
act as an effective dark-energy component; the 2008 status report calls the
situation "intermediate" (Buchert 2008, arXiv:0707.2153) `[src]`. The two
positions on whether this matters:

- *Irrelevant.* In a framework where the metric stays close to a background
  but stress-energy fluctuations are arbitrarily large on small scales, and
  matter obeys the weak energy condition, small-scale inhomogeneities can
  only add a traceless effective stress-energy (like gravitational
  radiation) and "cannot mimic the effects of dark energy" (Green & Wald
  2011, arXiv:1011.4920) `[src]`.
- *Not proven irrelevant.* The reply argues that the trace-free theorem does
  not involve averaging, is coordinate-dependent and not mathematically
  general, so Green and Wald have not proven a general result on
  backreaction (Buchert et al. 2015, arXiv:1505.07800) `[src]`.

No observational analysis read this session measures a backreaction
amplitude directly; the observational test in use is the timescape model.

### 4.3 Timescape
<!-- key: timescape -->

Timescape explains apparent acceleration within general relativity as the
effect of quasilocal gravitational energy and clock-rate differences between
observers in bound systems and volume-averaged locations in voids, with
Buchert averaging for the evolution (Wiltshire 2007, arXiv:gr-qc/0702082)
`[src]`. It is statistically homogeneous and isotropic but departs from
average FLRW evolution, so it is a test of FLRW, not of statistical
homogeneity (Seifert et al. 2024, arXiv:2412.15143) `[src]`.

| Analysis | Data | Result as stated | Citation |
|---|---|---|---|
| Dam et al. 2017 | JLA SNe | likelihood statistically indistinguishable from flat ΛCDM; apparent q0 = −0.043 (+0.004/−0.000) `[src]` | arXiv:1706.07236 |
| Lane et al. 2023 | Pantheon+, cosmology-independent covariance | "for the first time" evidence that timescape may fit better than ΛCDM `[src]` | arXiv:2311.01438 |
| Seifert et al. 2024 | Pantheon+, Tripp standardisation only | ln B > 5 for timescape over ΛCDM on the full sample; ln B > 1 for z > 0.075 `[src]` | arXiv:2412.15143 |
| DES SN analysis, as quoted by CosmoVerse | DES SNe, z > 0.033 | ln B = 1.7 for timescape; BAO by simple geometric scaling strongly favour ΛCDM `[sec: arXiv:2504.01669, Sect. 4.6.3.c]` | not read |
| Saulder et al. 2019 | SDSS and 2MRS groups vs Millennium mocks | Hubble-flow variations prefer ΛCDM over an approximated timescape `[src]` | arXiv:1811.11976 |

**The disputes.** Wiltshire replies that the deformed simulation of Saulder
et al. omits key geometric features, so it does not approximate timescape
(arXiv:1812.01586) `[src]`. Timescape proponents argue that BAO must be
re-extracted from raw clustering data and recalibrated from the CMB in
timescape before the BAO comparison is meaningful, and that the Buchert
equations need a closure condition whose physical interpretation is debated
`[sec: arXiv:2504.01669, Sect. 4.6.3.c]`. The supernova preference depends
on light-curve choices: Dam et al. found that cuts at the homogeneity scale
and the mean-colour parameter change with the cosmological model
(arXiv:1706.07236) `[src]`. No CMB + BAO + SN timescape fit was read this
session.

**What a referee checks.** Standardisation (Tripp only, or with host and
bias corrections) and whether it was refitted per model; the low-z cut and
peculiar-velocity treatment; whether a Bayes factor from SNe alone is
compared with a combined-probe ΛCDM fit; how BAO and CMB were (or were not)
modelled in the alternative.

## 5. The local void (KBC) claim
<!-- key: the-local-void-kbc-claim -->

**As the proponents state it.** The K-band luminosity density rises by ~1.5
beyond z ~ 0.07, suggesting an underdensity on ~300 Mpc scales sufficient to
resolve the Hubble tension (Keenan et al. 2013, arXiv:1304.2884) `[src]`.
The density contrast δ = 0.46 ± 0.06 between 40 and 300 Mpc is in 6.04σ
tension with ΛCDM using the MXXL simulation, 7.09σ combined with the Hubble
tension, which motivates a MOND cosmology with 11 eV sterile neutrinos that
fits the void and local H0 at 2.53σ (Haslbauer et al. 2020,
arXiv:2009.11292) `[src]`. CosmoVerse (section coordinated by Banik)
estimates cz′/H0 = (1 − δ_obs)^(−1/6), a local excess of 11 ± 2% after
halving the redshift-space underdensity, and states that the outflow from a
local void in ΛCDM "is not sufficient to solve the Hubble tension"
`[sec: arXiv:2504.01669, Sect. 4.5.1, Eq. 4.22]`. A 2026 perspective links
the void to low-redshift BAO deviations (α_iso < 1) and predicts convergence
to the CMB expansion rate above z ≈ 0.2 (Banik et al. 2026,
arXiv:2602.03928) `[src]`. Later tests by the same proponents (all `[src]`,
abstracts):

- Bulk flow: the Haslbauer void model, not fitted to bulk flows, agrees
  "qualitatively" with the rising CF4 bulk-flow curve, which is in 4.8σ
  tension with ΛCDM at 200 h⁻¹ Mpc (Mazurenko et al. 2023, arXiv:2311.17988).
- H0(z): Gaussian and exponential profiles reasonably match binned H0(z)
  declining toward Planck; Maxwell–Boltzmann less well (Mazurenko et al.
  2024, arXiv:2412.12245).
- BAO: 42 D_V measurements give χ² = 75.7 without a void and 47.3–51.2
  with void models, 3.3σ → 1.1–1.4σ, assuming independent errors; the
  differences are smaller for angular and radial BAO (Banik & Kalaitzidis
  2025, arXiv:2501.17934).
- Gravitational redshift at z ≳ 0.3: BBN + CMB + BAO + chronometers give
  z₀ = −0.4 (+0.8/−0.9)% (−0.1 ± 0.7% from z > 0.29), preferring 0, yet the
  void value 0.84% fits with Δχ² < 2, so higher-z data cannot rule the void
  out (Banik, Nájera & Desmond 2026, arXiv:2606.02712).

Independent support for an underdensity, smaller in effect:

- 2MRS and 2M++ counts to K < 11.5 over ~90% of the sky: ≈ 21–22%
  underdense at z < 0.075, implying a local H0 ≈ 3% high and a 3σ tension
  with ΛCDM (Wong et al. 2021, Shanks group, arXiv:2107.08505) `[src]`.
- CLASSIX X-ray clusters: matter underdensity −0.3 ± 0.15 within ~100 Mpc,
  local H0 higher by 5.5 (+2.1/−2.8)%, diluted when distance indicators
  outside it are used; ΛCDM probability 1.3–3.7σ (Böhringer et al. 2019,
  arXiv:1907.12402) `[src]`.
- ΛLTB with the KBC profile: consistent with 217 SNe at 0.0233 < z < 0.15
  and with linear kSZ limits (SPT, ACT); the H0 tension falls from 3.4σ to
  2.75σ (Hoscheit & Barger 2018, arXiv:1801.01890) `[src]`.

**As the critiques state it.**

- The SN Ia Hubble diagram (1295 SNe) is inconsistent at 4–5σ with
  |δ| > 20% and bounds δ < 27% on scales > 69 h⁻¹ Mpc at 5σ; the empirical
  σ_H0 = 0.60% matches the 0.42% cosmic variance expected (Kenworthy et al.
  2019, arXiv:1901.08681) `[src]`.
- Field-level fits of void models to Cosmicflows-4 Tully–Fisher distances
  prefer a void smaller than 70 Mpc, under 10% of the KBC size; the local
  H0 is 72.1 (+0.9/−0.8), 70.4 ± 0.4 or 70.2 (+0.5/−0.4) for exponential,
  Gaussian or Maxwell–Boltzmann profiles, the first disfavoured by the
  evidence, and the preferred models disagree with the CF4 bulk flow
  (Stiskalek et al. 2025, arXiv:2506.10518) `[src]`.
- The Manticore-Local BORG reconstruction of 2M++ finds "no evidence for a
  large local underdensity" (McAlpine et al. 2025, arXiv:2505.10682)
  `[src]`.
- Note on attribution: Stiskalek et al. 2025 is co-authored by Banik, and
  the 2026 proponents' perspective by Desmond; the critiques below are
  from other groups.
- N-body sample variance in the local H0 is 0.31 km/s/Mpc; a void solving
  the tension needs δ ≃ −0.8 within ~150 Mpc, "very unlikely" in ΛCDM and
  against observations (Wu & Huterer 2017, arXiv:1706.09723) `[src]`.
- ΛLTB fits to Pantheon over all profile parameters: the tension "cannot
  be saved by a local void alone" (Cai et al. 2020, arXiv:2012.08292)
  `[src]`.
- ΛLTB + Pantheon + BAO + Planck distance priors: binned SNe prefer a −13%
  drop over ~300 Mpc, matching KBC, but the full sample is compatible with
  homogeneity ("a cautionary tale" on binned SNe), and M_B is unchanged
  against ΛCDM, so the void "does not resolve the tension" (Castello et al.
  2021, arXiv:2110.04226) `[src]`.
- Without assuming the Copernican principle, ΛLTB with CMB, BAO, SNe, local
  H0, chronometers, y-distortion and kSZ: the void is favoured only when
  SNe are restricted to 0.023 < z < 0.15; with the full SN sample the
  tension is not solved, and the best fit is a shallow void, δ_L ≈ −0.04,
  r_out ≈ 300 Mpc (Camarena et al. 2022, arXiv:2205.05422) `[src]`.

**The proponents' reply to the SN test.** Kenworthy et al. assumed
Newtonian void dynamics and fixed q̄₀ to the ΛCDM 0.55; a large void raises
q̄₀, so it must be free; the local q̄₀ = 1.08 ± 0.29 they quote from Camarena
& Marra (> 1, impossible
for a standard background) with the high local H0 is read as evidence for
a local effect (Haslbauer et al. 2020, arXiv:2009.11292, Sects. 5.2,
5.3.4, 5.3.6) `[src: those sections]`. They also quote Hoscheit & Barger
as giving H0 higher by 1.27 ± 0.59 in 0.0233 < z < 0.07 than in
0.07 < z < 0.15, "only modestly" reducing the tension (Sect. 5.3.4).

**Where it stands.** The void is measured in redshift-space galaxy counts
(K band, 2MRS, clusters); SN-only ΛLTB fits find it only in binned or
z < 0.15 SN subsets; direct distances and constrained reconstructions do
not find it at the required size, and a void of that size is not expected in ΛCDM, so the
proposal needs enhanced structure growth (MOND in the published models).
The proponents list the decisive tests: field-level fits to distance
catalogues, kSZ limits on coherent outflows, fast radio bursts and redshift
drift (arXiv:2602.03928) `[src]`. The same evidence from the ladder side is
in `cosmo-distance-ladder-h0` (`open-questions.md` §7) and in this skill's
`systematics.md` §1.

## 6. What a referee checks
<!-- key: what-a-referee-checks -->

- Homogeneity: R_H definition and fiducial cosmology; selection-function
  dressing; mocks of the same tracer.
- Isotropy: the dipole and anomaly checks of `systematics.md` §§5–6.
- Inhomogeneous models: whether the model is fitted to SNe alone or to SNe,
  BAO, CMB and kSZ together; whether the alternative's BAO and CMB
  predictions were computed in that model.
- Local void: redshift-space counts against direct-distance and
  velocity-field tests; whether ΛCDM growth can produce the void; the
  resulting local H0 against the ladder value, not against zero.
- Attribution: several analyses here come from the proponents of the model
  tested; quote both sides.

## Not verified
<!-- key: not-verified -->

- The DES supernova timescape analysis cited by CosmoVerse (Sect. 4.6.3.c)
  was not identified and read.
- No 2025–2026 critique of the Seifert et al. timescape result was found in
  the searches made.
- Bianchi and McVittie spacetimes (CosmoVerse Sects. 4.6.2.b, 4.6.3) are
  not covered.
- §5 peers (2026-10-22) read at abstract level only, except Haslbauer et
  al. 2020 Sects. 5.2–5.3; no reply by Kenworthy et al. to that critique,
  and no reply by the proponents to Castello et al. or Camarena et al., was
  searched for.
