# Requirements flow-down — cosmo-surveys-facilities dossier

Scope: how a cosmological goal is turned into survey, data-set and
instrument requirements (levels, allocations, margins), how a systematics
budget is set and split among subsystems, and how requirements are verified
and renegotiated when the data miss them, as read in the requirement
papers of DESI, LSST (the 2008 science drivers and the DESC Science
Requirements Document), Euclid and the weak-lensing allocation papers
behind it, Roman's spectroscopic survey, PFS, SPHEREx and LiteBIRD (2022,
2026). CMB ground-survey flow-downs (CMB-S4, SO, CMB-HD) are in
`deep/cmb-survey-design.md`.
Snapshot: 2026-10-22.
From: Euclid overview (arXiv:2405.13491), Sects. 2–3 (primary probes to
spacecraft and instruments); Flaugher et al. 2022 Snowmass report
(arXiv:2209.08654), Sect. 3.3.

Already in L2, not repeated here: the DESI requirement values for redshift
success, redshift accuracy and fibre completeness in
`systematics.md#fibre-collisions-and-assignment-incompleteness`,
`systematics.md#redshift-success-and-its-dependence-on-the` and
`systematics.md#redshift-accuracy`; the DESI imaging requirements in
`systematics.md#target-selection-inherited-from-imaging`; LSST calibration
and image-quality requirements and the Euclid top-level shear requirement
in `systematics.md#photometric-calibration` and
`systematics.md#point-spread-function`; Euclid NISP requirements in
`systematics.md#slitless-spectroscopy-and-spectrophotometry`; the LiteBIRD
null-map requirement in `systematics.md#cmb-experiments`; LSST design and
minimum-specification depths in `surveys-and-data.md#imaging-surveys`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. State the top-level goal as a number
<!-- key: step-1-state-the-top-level-goal-as-a-number -->

- **DESI.** Four Level 1 requirements: area at least 9000 deg² (baseline
  with margin 14,000 deg²); isotropic BAO distance R(z) to 0.28% over
  0 < z < 1.1 and 0.39% over 1.1 < z < 1.9; H(z) to 1.05% over
  1.9 < z < 3.7; instrument and method systematics below 0.16% on D_A and
  0.26% on H at z < 1.5 [src: arXiv:2205.10939, Sect. II.2, Table 3].
  The text of Sect. II.2 writes 1.9 < z < 3.9 for the H(z) range where
  Table 3 writes 3.7 [src].
- **Euclid.** There should be at most a 0.01 chance that the weak-lensing
  data wrongly accept ΛCDM, a Bayes factor of 1:100 for w = −1 against any
  deviation; this requires a figure of merit (FoM) ≥ 375, with the FoM
  proportional to the inverse area of the (w0, wa) error ellipse of
  w(a) = w0 + wa(1 − a), and σ(w0) < 0.01, σ(wa) < 0.1, for weak lensing
  and clustering combined [src: arXiv:2405.13492, Sect. 2.1]. Weak-lensing
  requirements were therefore derived with a prior equal to the expected
  clustering constraints [src].
- **LSST.** No single goal: four science drivers lead to twelve shared
  constraints on data properties (single-visit depth r ~ 24.5, image
  quality set by the 0.65″ median site seeing, photometric repeatability,
  astrometry, visit time, six filters, revisit distribution, about 1000
  visits per field, coadd r ~ 27.5, visits per filter, at least about
  18,000 deg², near-optimal processing) [src: arXiv:0805.2366,
  Sect. II.1.5]. "Any one of the four main science drivers could be
  removed, and the remaining three would still yield very similar
  requirements for most system parameters" [src].
- **LSST DESC.** RH1: a combined FoM above 500 (about ten times the
  Stage II FoM of 54) with the Y10 data, statistical and systematic
  errors included, with Stage III priors (BOSS, Planck, Stage III
  supernovae, an H₀ prior) [src: arXiv:1809.01669, Sect. 4]. Goal G1:
  each probe in the joint likelihood above twice its Stage III FoM, that
  is 12, 1.5, 1.3, 19 and 40 for clusters, LSS, strong lensing,
  supernovae and weak lensing [src: same]. The goal is relative to
  earlier experiments, where Euclid's FoM ≥ 375 is absolute.
- **Roman.** Two dark-energy questions flow to three Science Objectives
  (NIR imaging deeper than 26.5 AB; expansion history to z = 2 with SN,
  WL and redshift surveys; growth history to z = 2 with WL, RSD and
  clusters, each with cross-checks), then to Level 2 requirements for
  the spectroscopic survey [src: arXiv:2110.01829, Sect. II.1].
- **PFS.** Science-yield requirements: ≲ 3% on D_A(z) and H(z) in each
  of six BAO bins over 0.8 < z < 2.4, ≲ 7% on Ω_de(z), Ω_K to ≲ 0.3%,
  ≲ 6% on the growth rate per bin from RSD [src: arXiv:1206.0737,
  Table 4]. They were written to provide "key science requirements for
  the technical design" and reproduce the conceptual and preliminary
  design reviews (2012, 2013) [src: Sect. I].
- **SPHEREx.** Δf_NL < 0.5, "needed to meaningfully discriminate between
  single-field and multi-field inflation", from many low-accuracy
  redshifts (power spectrum) and fewer high-accuracy ones (bispectrum)
  [src: arXiv:2511.02985, Sects. III, III.2].
- **LiteBIRD.** 2022: Lv1.01, total δr < 10⁻³ including statistical
  noise, systematics, foreground residuals, lensing and observer bias,
  "and shall not rely on future external data sets"; Lv1.02, > 5σ from
  2 ≤ ℓ ≤ 10 and from 11 ≤ ℓ ≤ 200 separately for r = 0.01 and τ = 0.05
  [src: arXiv:2202.02773, Sect. 3.2, Table 1]. After the reformation:
  δr < 0.002 (68%, r = 0), with contingency and margins inside, and a
  statistical target σ_r < 0.001 including foregrounds and lensing; for
  r = 0.01, independent 3σ detections of the reionisation and
  recombination bumps [src: arXiv:2607.25285, Sect. 2.1].

### Step 2. Derive the statistical requirements: sample and survey size
<!-- key: step-2-derive-the-statistical-requirements -->

- **Weak lensing.** Amara & Réfrégier computed the number of galaxies
  needed to shrink the ellipse; with 35 usable galaxies per arcmin², a 1%
  width (FoM = 375) needs 20,000 deg²; this fixed the survey scale and the
  S/N for shape measurement, the first three top-level requirements
  [sec: arXiv:2405.13492, Sect. 2.1, reporting arXiv:0710.5171, Fig. 11].
- **DESI.** Level 2 requirements turn the BAO goals into per-tracer
  densities, redshift errors, catastrophic-failure rates and completeness;
  for example at least 300 LRGs deg⁻² at 0.4 < z < 1.0 and 1280 ELGs deg⁻²
  at 0.6 < z < 1.6, with target densities of 350 and 2400 deg⁻² [src:
  arXiv:2205.10939, Table 3, L2.2.1, L2.3.1, L2.8].
- **LSST area against aperture.** Doubling exposure time and using it to
  double area doubles the source count; spending it on depth at fixed area
  gives about 0.4 mag, which more than doubles counts only if the slope k
  of log N = C + k m exceeds 0.75, while practically all populations have
  k ≤ 0.6 [src: arXiv:0805.2366, Sect. II.2.1, footnote 7]. So the area is
  maximised first, to 18,000 deg² set by an airmass limit of 1.5; the
  field (about 10 deg²) is the largest compatible with seeing-limited image
  quality; a ten-year lifetime is the compromise between a 15 m (3 years)
  or 12 m (5 years) mirror and operations cost; the coadd depth then gives
  a minimum effective aperture of 6.4 m [src].
- **Roman spectroscopy.** HLSS 1: about 1500 deg² (2000 goal), "the
  minimum required to yield robust BAO/RSD measurements", at least 90%
  covered by the imaging survey, contiguous where practical. HLSS 2:
  n > 3 × 10⁻⁴ (h/Mpc)³ at z = 1.6, from shot-noise non-dominance
  nP(k = 0.2 h/Mpc) ~ 1 with 20% margin, bias b(z) = 1 + 0.5z assumed;
  "we cannot require a higher galaxy number density than what nature
  provides" [src: arXiv:2110.01829, Sect. II.1]. The reference survey
  meeting them maps 2000 deg² to 10⁻¹⁶ erg s⁻¹ cm⁻² at 6.5σ in about
  0.6 yr [src: abstract]; the survey to be flown is the community-defined
  wide-area survey (`open-questions.md#cancelled-descoped-or-redefined-projects`).
- **PFS.** Galaxy-catalogue requirements: 0.8 ≤ z ≤ 2.4 (0.8–1.6
  minimum), ≥ 2900 galaxies deg⁻², n̄P > 1 (0.8 < z < 1.6) or > 0.5
  (1.6 < z < 2.4) at k = 0.1 h/Mpc, ≥ 1400 deg², width > 7.5° in at most
  four regions, about 100 clear nights [src: arXiv:1206.0737, Table 4].
  The width is 2.5 BAO lengths at the minimum redshift z = 0.8, to be
  refined by simulation, and the density must exceed SDSS and BOSS LRG
  densities for reconstruction [src: Sect. II.2.4].
- **SPHEREx sensitivity.** The redshift number and accuracy depend on
  point-source sensitivity in bands 1–4, set to better than 18.4 AB
  (5σ) per spectral channel at the end of the survey [src:
  arXiv:2511.02985, Sect. III.2].

### Step 3. Set and split the systematics budget
<!-- key: step-3-set-and-split-the-systematics-budget -->

**Tolerance criterion.** For a Gaussian likelihood of width σ and a bias b,
the overlap between biased and unbiased likelihoods is
p = 1 − erf(|b|/(2√2 σ)) (Massey et al. 2013, arXiv:1210.7690, Eq. 62);
95% (90%) overlap needs |b| < 0.13σ (0.25σ), and a bias equal to σ leaves
62% [src: Sect. 4.1]. If b is instead the 95% limit of an unknown bias and
is marginalised over (Eq. 64), 95% (90%) overlap needs |b| < 0.31σ (0.62σ);
the paper adopts 0.31σ [src]. Euclid's verification uses
|b/σ| ≤ 0.25 on w0, the 90% overlap [src: arXiv:1910.10521, Sect. 4.4].

**Shear bias model.** Measured shear γ̂ = (1 + m)γ + c (Cropper et al.
2013, arXiv:1210.7691, Eq. 1), with m and c the multiplicative and
additive biases; the power spectrum becomes
Ĉ_ij(ℓ) = (1 + 𝓜(ℓ)) C_ij(ℓ) + 𝓐(ℓ) (Eq. 3), with 𝓐 = σ²[|c|] and
𝓜 = 2⟨m⟩ + ⟨m⟩² (Eq. 4), for redshift-bin pairs ij and multipole ℓ.
For a DUNE-like full-sky survey with mild redshift evolution, Amara &
Réfrégier require the additive variance below 10⁻⁷ and m0 below 10⁻³ for
biases sub-dominant to statistical errors [src: arXiv:0710.5171,
abstract].

**Integrated requirement.** Cropper et al. integrate over
10 ≤ ℓ ≤ 5000 with weight ℓ² dlnℓ (Eqs. 21–28) for a 15,000 deg², 30
galaxies arcmin⁻² survey; the requirements of Massey et al. then read
𝓐′ ≤ 2.6 × 10⁻⁷ per bin pair (Eq. 25) and 𝓜′ ≲ 1.4 × 10⁻² (Eq. 28)
[src: Sect. 2.3]. They nevertheless keep the stricter A ≤ 10⁻⁷ and
M ≤ 4 × 10⁻³, that is 2⟨m⟩ ≃ 4 × 10⁻³ (Eq. 31), from the earlier analyses
that extended to ℓ ≤ 20,000, "to allow for a future potential increase of
scope in the use of the non-linear modes" [src]. Note for readers of L2:
the Euclid VIS paper quotes m0 < 10⁻³ after Amara & Réfrégier, while
Cropper's allocation tree caps ⟨m⟩ at 2.0 × 10⁻³ with 𝓜 = 2⟨m⟩; the two
use different definitions [src: arXiv:2405.13492, Sect. 2.1;
arXiv:1210.7691, Table 1].

**Weights per subsystem.** With R_gal = 0.20″ (limit m_AB = 24.5),
convolutive PSF size R_C = 0.22″, non-convolutive R_NC = 0.05″ and
|ε_C| < 0.1, the additive weights are a′₁ = 0.10 and a′₂ = 0.74 (PSF
ellipticity) against a′₃ = 1.0 × 10⁻³ and a′₄ = 4.2 × 10⁻³ (PSF size),
and the multiplicative weights m′₁ = m′₅ = 0.60 (size) and m′₂ = 0.17
(Eqs. 32–33) [src: arXiv:1210.7691, Sect. 2.4]. Conclusion stated there:
ellipticity knowledge drives the additive budget, PSF size knowledge the
multiplicative one [src].

**Allocation tree.** The Euclid example tree of Cropper et al. allocates
σ[|c|] = 1.3 × 10⁻⁴ against a cap of 3.2 × 10⁻⁴ and ⟨m⟩ = 1.5 × 10⁻³
against 2.0 × 10⁻³, then splits downward: PSF-model ellipticity knowledge
2.3 × 10⁻⁴, of which truncation error 2.1 × 10⁻⁴ and coefficient error
9.7 × 10⁻⁵, the latter split into photon noise 7.0 × 10⁻⁵ and calibration
residuals of 3.0 × 10⁻⁵ each (bias, flat field, sky, linearity, cosmic
rays) [src: Table 1]. Contributions combine in quadrature ("Q" in the
table) [src]. Initial values may be placeholders, then revised by
simulation and rebalanced when one factor is disproportionate, for
example by changing technology [src: Sect. 2.4].

**DESC: calibratable against self-calibrated.** RH2 asks that the total
calibratable systematic uncertainty of each probe be below the
marginalised statistical uncertainty in the (w0, wa) plane; the
statistical error already contains self-calibrated systematics
(intrinsic alignments, galaxy bias, mass–observable scatter), so
astrophysical systematics may exceed the pure statistical error [src:
arXiv:1809.01669, Sect. 4]. RH2 is the only requirement applicable to
the Y1 analysis [src]. The calibratable budget is then scaled so the
final FoM is exactly 500 [src]. Each requirement is placed by biasing the
data vector, refitting by Fisher forecast, and reading the distance to
the edge of the 1σ ellipse, r = sqrt(b · C⁻¹ · b) (Eq. 2), with C the
marginalised (w0, wa) covariance; the requirement s0/r is then rescaled
by the effect's share of the budget, combined in quadrature (two equal
shares get r = 1/√2 each), assuming b linear in s0 [src: App. H2].
For 3×2pt the calibratable budget is split 0.7 (redshift), 0.2 (number
density), 0.7 (multiplicative shear), 0.2 (additive shear), chosen to sum
to 1 in quadrature, the smaller shares going to effects easier to null
test, with f_sys = 0.62 times the marginalised statistical error in Y10;
the two redshift items each get 0.7/√7 ≈ 0.25 [src: Sect. 5.2]. Y10
results: mean source redshift 0.001(1 + z) (Y1 goal 0.002), photo-z
scatter 0.003(1 + z), redshift-dependent shear calibration 0.003, PSF
model size 0.1%, stellar contamination 0.1%; additive-shear requirements
deferred [src: Sect. 5.2]. Compare Euclid: the tolerance there is a
fraction of σ per parameter (|b/σ| ≤ 0.25 on w0, above), in DESC the
ellipse edge in (w0, wa) before rescaling.

**LiteBIRD: an equal split.** The 2022 error budget (Lv2.06) gives equal
amounts to the total statistical error after foreground separation and to
the total systematic error, σ_stat < 0.6 × 10⁻³ and σ_syst < 0.6 × 10⁻³,
with margin for the noise penalty of debiasing; lensing and foreground
uncertainty sit in σ_stat because no external delensing is assumed, and
observer bias must be much smaller than σ_syst [src: arXiv:2202.02773,
Sect. 3.3]. The 2026 statistical target σ_r < 0.001 sits inside a total
of 0.002 (Step 1) [src: arXiv:2607.25285, Sect. 2.1].

**SPHEREx: one number for large-angle errors.** All sources of error
coherent on ~10° scales must be controlled to 0.2% (rms per dex in
wavenumber) to measure f_NL^loc = 1; observing from space removes the
variable atmospheric extinction that limited earlier f_NL studies, and
Galactic extinction at 3.2 μm is an order of magnitude below the i band
[src: arXiv:1412.4872, Sect. VIII]. Spurious power from sky-varying
redshift errors exceeds the requirement and must be corrected by measuring
the variation of redshift bias and scatter over the sky [src: App. A].

### Step 4. Derive the instrument requirements
<!-- key: step-4-derive-the-instrument-requirements -->

DESI's Level 3 requirements, with the reasons given [src:
arXiv:2205.10939, Sect. II.3]:

| Requirement | Value | Reason stated |
|---|---|---|
| Spectral range | 360–980 nm | Balmer break (364.6 nm) of low-z interlopers; Lyα at 377 nm for z = 2.1; whole Lyα forest at z > 2.5; Cd 361.0 nm arc line; [O II] to z = 1.6 (970 nm); 400 nm break of LRGs to z ~ 1.4 |
| Resolution | > 1500, > 3000, > 4000 in three bands | resolve the [O II] doublet at z > 0.49, where it is usually the only feature; lower is allowed at z < 0.49 because Hα is visible |
| [O II] S/N = 7 flux limit | 10, 9, 9, 8, 9 × 10⁻¹⁷ erg s⁻¹ cm⁻² in Δz = 0.2 bins from 0.6 to 1.6 | joint constraint on throughput, resolution, read noise and conditions; binned because sky lines modulate the limit |
| Fibre density, field | from survey area, minimum time per tile and survey duration, with a tile-overlap factor F_over = 1.21 (later replaced by the Hardin tiling) | number of spectra needed for the science |
| Area and duration | — | total operations cost; this in turn set throughput, targets per exposure and a two-minute inter-exposure time affecting "nearly every subsystem" |
| Astrometry of input catalogue | — | target densities and the fibre-positioning error budget; met by the Legacy Surveys |
| Seeing, zenith range, guiding | Mayall historical seeing; 0–60°; 100 mas rms | do not degrade the telescope; footprint flexibility; part of the positioning budget |

Below that, Level 4 corrector requirements: field-weighted FWHM < 0.4″ at
zenith over the band, maxima of 0.6″ (360–450 nm) and 0.5″ (450–980 nm),
coatings at 98.5% transmission per surface, chief-ray deviation < 0.5° on
average, focal-surface radius of curvature > 3000 mm, at most one
aspheric surface per lens; the aspheric-departure limit came from vendors'
interferometric testing [src: Sect. III.1].

In Euclid the chain runs Science Requirements Document → Mission
Requirements Document → system, instrument, processing, operations and
calibration documents; the VIS-specific document is the Payload Elements
Requirements Document, and the VIS flow-down exceeded 4000 requirements
[src: arXiv:2405.13492, Sect. 2.1]. Because Euclid delivers data and not
cosmological parameters, nothing sits above the Science Requirements
Document [src].

Peers:

- **LiteBIRD** splits requirements into five levels, Lv1 science to Lv5
  unit specifications, with 11 Lv2 measurement requirements (statistical
  and systematic uncertainty, scan strategy, resolution, calibration,
  error and systematic budgets, duration, orbit, observer bias,
  noise-covariance knowledge); Lv2 "do not assume a specific system",
  Lv3 apply to the system chosen in trade-off studies, and programme
  constraints such as the cost cap enter at Lv2 [src: arXiv:2202.02773,
  Sect. 3.3]. Examples: < 80′ FWHM in the lowest band for ℓ = 200, a
  three-year observing phase set by cost cap and cooler lifetime, a
  Lissajous orbit at L2 [src].
- **PFS instrument** (for the cosmology survey): 650–1260 nm (650–1000
  minimum), 2400 fibres, overhead < 0.2 of open-shutter time, mean
  throughput > 22% (red) and > 24% (NIR), R ~ 3000 (red) and ~ 4000
  (NIR) "to resolve out OH lines but limit read noise", read noise ≤ 3 and
  ≤ 4 e⁻, sky subtraction < 1% per resolution element [src:
  arXiv:1206.0737, Table 5].
- **Roman spectroscopy.** HLSS 3: Hα over 1.1 < z < 1.9; two lines are
  needed for a grism redshift, hence 1–1.93 μm, chosen beyond what ground
  surveys reach (z ~ 1) and complementary to Euclid's 1.85 μm cut-off.
  HLSS 4: σ_z < 0.001(1 + z), outliers beyond 0.005 below 10% and known
  to 2 × 10⁻³ [src: arXiv:2110.01829, Sect. II.1].
- **SPHEREx.** Bands 1–4 resolving power and sensitivity come from the
  f_NL theme; the galaxy-formation theme adds control of noise and
  systematics on degree scales, the ices theme higher resolving power to
  5 μm [src: arXiv:2511.02985, Sect. III]; the pixel is the smallest that
  does not degrade point-source sensitivity at fixed pixel count and
  time, 6″ [src: Sect. III.3].

### Step 5. Carry margins
<!-- key: step-5-carry-margins -->

DESI's "baseline with margin" survey (14,000 deg² against the 9000 deg²
requirement) forecasts 0.22% and 0.31% on R(z) and 0.84% on H(z) against
required 0.28%, 0.39% and 1.05% [src: arXiv:2205.10939, Table 3]. Euclid's
survey delivers median S/N above each channel's requirement (`deep/footprint-tiling-depth.md`).
SPHEREx defines margin as the difference between the Maximum Expected
Value performance (each sub-system meeting its specification with
contingency) and the requirement, and carried 300% margin on its driving
point-source sensitivity requirement, with no new technology [src:
arXiv:1412.4872, Sect. I, Fig. 2 caption]. Roman's density requirement
carries 20% margin for the uncertain Hα luminosity function [src:
arXiv:2110.01829, Sect. II.1]; LiteBIRD 2026 puts contingency and margins
inside δr [src: arXiv:2607.25285, Sect. 2.1].

### Step 6. Verify against data
<!-- key: step-6-verify-against-data -->

DESI's Survey Validation was designed to finalise selections and strategy:
targets denser than the main survey to tune boundaries, deep spectra for
parent redshift distributions, repeated exposures for repeatability and
purity, many standard stars and sky fibres, varied conditions to calibrate
the exposure-time calculator, and the redshift-success-versus-depth curve
to fix exposure times [src: arXiv:2306.06307, Sect. II.3]. Its Table 5
sets each Level 2 requirement against performance [src: Sect. V.3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Hierarchical allocation against end-to-end verification
<!-- key: hierarchical-allocation-against-end-to-end -->

An inverted-tree allocation makes each subsystem's budget visible and
contractable, but the Euclid VIS paper states that "the hierarchical
combination of requirements is too restrictive"; a catalogue-level
end-to-end formalism (Paykari et al. 2020) was used for system performance
verification at the Critical Design Review, margins were found, some newly
identified effects remain without allocation, and reviews still compare
outcomes with the formal flow-down because reformulating it, for instance
in industrial contracts, was unfeasible [src: arXiv:2405.13492, Sect. 2.1].
The end-to-end method propagates object-level PSF and charge-transfer
inefficiency (CTI) residuals through tiling, detector layout and PSF
pattern to δC(ℓ), then to w0, wa biases by the Fisher bias formula
b_α = −Σ_β (F⁻¹)_αβ B_β, B_β = Σ 𝓕_jk(ℓ) δC_jk(ℓ) ∂C_jk/∂β (Eqs. 20–21),
with 𝓕_jk = f_sky(2ℓ + 1)/(2[C_jk + N_jk]²) (Eq. 19) [src:
arXiv:1910.10521, Sects. 2.4, 2.5]. Results (90% intervals of b/σ): PSF
alone (−0.024, 0.033) on w0; CTI with fixed model parameters over a
100 deg² patch (−0.328, 0.077), "just outside the tolerable range"; CTI
with resampled parameters (−0.078, 0.152); PSF and CTI together
(−0.046, 0.144), a case the flow-down did not capture [src: Sect. 4.4,
Table 1]. Caveat in the same paper: marginalised one-parameter biases can
be optimistic, since a multi-dimensional constraint may be biased by more
than 1σ along a degeneracy while each marginal stays below [src:
Sect. 2.5].

### Separate or joint budgets for additive and multiplicative bias
<!-- key: separate-or-joint-budgets-for-additive-and -->

Additive and multiplicative biases are degenerate in their effect on w;
the fitted bias plane b/σ ≈ −0.093 − 3.9 m + 3.3 × 10¹⁰ σ²_c gives the
joint requirement |m| + 8.6 × 10⁹ |σ²_c| ≲ 0.10 (Eq. 65) for w alone
[src: arXiv:1210.7690, Sect. 4.3]. Requirements set on one with the other
assumed zero spend "one degenerate error budget ... twice"; they should be
halved and can be traded linearly [src]. A large constant m is tolerable
for w but not for Ω_m or σ8 [src].

### One data set for many drivers, or specialised surveys
<!-- key: one-data-set-for-many-drivers-or-specialised -->

LSST argues that a minimum etendue of about 300 m² deg² lets one data set
serve all drivers; a smaller system would need separate specialised
surveys and lose efficiency, as the Pan-STARRS consortium did [src:
arXiv:0805.2366, Sect. II.3]. The DESI choice is the other extreme:
requirements are set by the dark-time cosmology tracers, and the BGS
requirements were added only after the instrument was complete [src:
arXiv:2205.10939, Sect. II.2].

### What to do when the data miss a requirement
<!-- key: what-to-do-when-the-data-miss-a-requirement -->

DESI Survey Validation against the 2014 requirements [src:
arXiv:2306.06307, Sect. V.3, Table 5]:

- ELG: 860 + 180 deg⁻² (two selections) at 0.6 < z < 1.6 against 1280;
  fibre-assignment efficiency 69% against the assumed 80%; the prime
  selection was cut from 2400 to 1941 deg⁻² because high-redshift
  galaxies could not be picked from grz imaging beyond a certain density,
  and a lower-priority selection filled the rest; the 1.1 < z < 1.6 sample
  still beats the original 400 deg⁻² assumption at 450 deg⁻² [src].
- LRG: redshift success high enough that faint LRGs (to z = 20.6) need
  one epoch instead of two; target density 350 → 624 deg⁻², 80% more
  reliable redshifts for 25 fewer exposures per deg² [src].
- Quasars: target density raised by 20% to 311 deg⁻² for about 20% more
  Lyα quasars at a cost of 30 more exposures per deg² (450 in total) [src].
- Lyα quasars: catastrophic failures 12.2% at 1000 km/s against < 2%;
  1.8% at 3000 km/s, so the requirement is met only "if the definition of
  a catastrophic failure is relaxed" [src].

### The ℓ range of a requirement
<!-- key: the-ell-range-of-a-requirement -->

Restricting to 10 ≤ ℓ ≤ 5000, to avoid non-linear and baryonic scales, is
"the main factor in the relaxation" of the 2013 values relative to the
2008 ones derived to ℓ ≤ 20,000; Cropper et al. kept the stricter values
for future scope [src: arXiv:1210.7691, Sect. 2.3]. A requirement quoted
without its ℓ range, survey area and source density is not comparable
(all three enter the denominator of Eq. 25) [src].

### Revising the top-level number
<!-- key: revising-the-top-level-number -->

LiteBIRD's total requirement went from δr < 10⁻³ (2022, five components,
no external data) [src: arXiv:2202.02773, Table 1] to δr < 0.002 with
σ_r < 0.001 statistical (2026), and its large-r requirement from > 5σ to
independent 3σ bump detections for r = 0.01 [src: arXiv:2202.02773,
Table 1; arXiv:2607.25285, Sect. 2.1]. Roman's spectroscopic
requirements were written for a reference survey "to formulate mission
science requirements", the final survey being defined by a community
process before launch [src: arXiv:2110.01829, Sect. I]. A requirement is
tied to the document version it comes from.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Project | Source | Place read |
|---|---|---|---|---|
| Top-level FoM | ≥ 375 (σ(w0) < 0.01, σ(wa) < 0.1), WL + GC | Euclid | arXiv:2405.13492 | Sect. 2.1 |
| Survey scale behind it | 20,000 deg² at 35 galaxies arcmin⁻² for 1% ellipse width | Euclid (as reported) | arXiv:2405.13492 citing arXiv:0710.5171 | Sect. 2.1 |
| Additive / multiplicative caps | σ²_sys < 10⁻⁷; m0 < 10⁻³ | DUNE-like survey | arXiv:0710.5171 | abstract |
| Adopted integrated caps | A ≤ 10⁻⁷; M = 2⟨m⟩ ≤ 4 × 10⁻³ | Euclid-like | arXiv:1210.7691 | Eq. 31 |
| Example allocation | σ[abs(c)] 1.3 × 10⁻⁴ of 3.2 × 10⁻⁴; ⟨m⟩ 1.5 × 10⁻³ of 2.0 × 10⁻³ | Euclid example | arXiv:1210.7691 | Table 1 |
| Bias tolerance | 0.13σ (95%), 0.25σ (90%); 0.31σ marginalised (95%) | generic | arXiv:1210.7690 | Sect. 4.1, Eqs. 62, 64 |
| Verification tolerance | abs(b/σ) ≤ 0.25 on w0 | Euclid | arXiv:1910.10521 | Sect. 4.4 |
| Level 1 BAO | 0.28% (0 < z < 1.1), 0.39% (1.1–1.9), H 1.05%; with margin 0.22%, 0.31%, 0.84% | DESI | arXiv:2205.10939 | Table 3 |
| Level 1 systematics | 0.16% D_A, 0.26% H at z < 1.5 | DESI | arXiv:2205.10939 | Table 3 |
| Corrector image quality | < 0.4″ field-weighted FWHM at zenith | DESI | arXiv:2205.10939 | Sect. III.1 |
| Inter-exposure time | 2 min | DESI | arXiv:2205.10939 | Sect. II.3 |
| Minimum etendue for one data set | ~300 m² deg² | LSST | arXiv:0805.2366 | Sect. II.3 |
| Minimum effective aperture | 6.4 m from coadd r ~ 27.5 | LSST | arXiv:0805.2366 | Sect. II.2.1 |
| SV ELG density | 860 + 180 = 1040 deg⁻² [der: sum] against 1280 required | DESI | arXiv:2306.06307 | Table 5 |
| VIS flow-down size | > 4000 requirements | Euclid VIS | arXiv:2405.13492 | Sect. 2.1 |
| Top-level FoM | > 500 (Y10, stat + sys, Stage III priors); per probe > 2 × Stage III | LSST DESC | arXiv:1809.01669 | Sect. 4 |
| Calibratable budget | f_sys = 0.62 × stat (Y10, non-SN); 3×2pt shares 0.7/0.2/0.7/0.2 | LSST DESC | arXiv:1809.01669 | Sect. 5.2 |
| 3×2pt Y10 requirements | Δ⟨z⟩ 0.001(1+z); σ_z 0.003(1+z); shear calibration 0.003; PSF size 0.1%; stars 0.1% | LSST DESC | arXiv:1809.01669 | Sect. 5.2 |
| HLSS area, density | ~1500 deg² (2000 goal); n > 3 × 10⁻⁴ (h/Mpc)³ at z = 1.6 | Roman | arXiv:2110.01829 | Sect. II.1 |
| HLSS redshifts | 1.1 < z < 1.9 (Hα); σ_z < 0.001(1+z); outliers < 10% | Roman | arXiv:2110.01829 | Sect. II.1 |
| Cosmology yield | ≲ 3% D_A, H in 6 bins; ≲ 6% growth; Ω_K ≲ 0.3% | PFS | arXiv:1206.0737 | Table 4 |
| Cosmology catalogue | ≥ 1400 deg²; ≥ 2900 deg⁻²; Δz/(1+z) < 0.0007; < 1% wrong z | PFS | arXiv:1206.0737 | Table 4 |
| f_NL requirement | Δf_NL < 0.5 → > 18.4 AB (5σ) per channel, bands 1–4 | SPHEREx | arXiv:2511.02985 | Sect. III.2 |
| Large-angle error budget | 0.2% rms per dex in k for f_NL^loc = 1 | SPHEREx | arXiv:1412.4872 | Sect. VIII |
| δr requirement | 2022: < 10⁻³ total, σ_stat and σ_syst < 0.6 × 10⁻³ each; 2026: < 0.002 total, σ_r < 0.001 | LiteBIRD | arXiv:2202.02773; arXiv:2607.25285 | Sects. 3.2–3.3; Sect. 2.1 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Budget spent twice.** Separate additive and multiplicative
  requirements on a degenerate pair (Massey et al., Sect. 4.3). Check:
  is there a joint requirement, or were the separate ones halved?
- **Requirement conditional on a prior.** Euclid's weak-lensing
  requirements assume the clustering prior [src: arXiv:2405.13492,
  Sect. 2.1]; quoting them for a lensing-only analysis changes their
  meaning.
- **Joint effects outside the tree.** PSF and CTI together were not in
  the flow-down; the end-to-end test caught it [src: arXiv:1910.10521,
  Sect. 4.4].
- **Unallocated effects.** Some effects identified after the flow-down
  have no allocation [src: arXiv:2405.13492, Sect. 2.1]. Check the list
  against the current systematics inventory, not the design one.
- **Passing by redefinition.** The Lyα catastrophic-failure requirement
  is met only at 3000 km/s [src: arXiv:2306.06307, Sect. V.3]. Check the
  definition used when a requirement is said to be met.
- **Requirements written for nominal conditions.** DESI's [O II] limit
  assumes 1.1″ seeing and median dark photometric sky [src:
  arXiv:2205.10939, Table 4]; delivered depth depends on the conditions
  actually met (`deep/footprint-tiling-depth.md`, Step 5).
- **Requirements that change after the hardware.** DESI added BGS
  requirements after the instrument was complete [src: arXiv:2205.10939,
  Sect. II.2]; such programmes inherit hardware optimised for others.
- **Fixed instead of marginalised parameters.** Taking the (w0, wa) block
  of the Fisher matrix, rather than of its inverse, fixes the other
  parameters and gives "overly small uncertainties and too-conservative
  requirements" [src: arXiv:1809.01669, App. H2, footnote 20].
- **A density nature does not provide.** Roman's density requirement is
  bounded by the Hα luminosity function, uncertain enough to need a 20%
  margin [src: arXiv:2110.01829, Sect. II.1]. Check the luminosity
  function behind a quoted density.
- **Quoting an old version.** LiteBIRD's δr < 10⁻³ is the 2022
  requirement, not the 2026 one (Revising the top-level number).

## Reading list
<!-- key: reading-list -->

| Role | Paper | What for |
|---|---|---|
| Foundation | Amara & Réfrégier 2008, arXiv:0710.5171 | bias Fisher formalism and the 10⁻⁷ / 10⁻³ caps |
| Foundation | Ivezić et al. 2019, arXiv:0805.2366, Sects. II.1.5–II.3 | shared constraints, aperture and etendue derivation |
| Method | Massey et al. 2013, arXiv:1210.7690 | tolerance criterion by likelihood overlap, joint additive–multiplicative requirement |
| Method | Cropper et al. 2013, arXiv:1210.7691 | integration over ℓ, subsystem weights and an allocation tree with Euclid values |
| Method | LSST DESC 2018, arXiv:1809.01669, Sects. 4, 5.2, App. H2 | relative FoM goals, calibratable against self-calibrated, ellipse-edge allocation |
| Application | Euclid Collaboration 2024 (VIS), arXiv:2405.13492, Sect. 2.1 | the Euclid document chain and why the tree was supplemented |
| Application | Abareshi et al. 2022, arXiv:2205.10939, Sects. II–III | DESI Level 1 to Level 4 with reasons |
| Application | DESI Collaboration 2023, arXiv:2306.06307, Sect. V.3 | requirements against Survey Validation performance and the changes made |
| Application | Wang et al. 2022, arXiv:2110.01829, Sect. II.1 | Roman HLSS Level 2 requirements |
| Application | Takada et al. 2014, arXiv:1206.0737, Sect. II.3 | PFS cosmology survey and instrument requirements |
| Application | Doré et al. 2014, arXiv:1412.4872, Sect. VIII; Bock et al. 2025, arXiv:2511.02985, Sect. III | SPHEREx systematics budget; science to requirements |
| Application | LiteBIRD Collaboration 2022, arXiv:2202.02773, Sects. 3.2–3.3; 2026, arXiv:2607.25285, Sect. 2.1 | five-level tree, equal stat/syst split, revised δr |
| Critique | Paykari et al. 2020, arXiv:1910.10521 | end-to-end verification against the flow-down |

## Not verified
<!-- key: not-verified -->

- The Euclid Science Requirements and Mission Requirements Documents and
  the LSST Science Requirements Document are cited by the papers but not
  on arXiv; not read.
- The body of Amara & Réfrégier 2008 (only its abstract); the survey-size
  figure is quoted from the VIS paper [sec].
- Kitching et al. 2019 and Taylor & Kitching 2018 (generalised bias
  propagation), cited by arXiv:1910.10521, not read.
- The DESI Final Design Report (arXiv:1611.00036) derivations of fibre
  number and field from A_survey, T_tile and T_survey.
- 4MOST: the overview (de Jong et al. 2019, arXiv:1903.02464) and the
  Cosmology Redshift Survey paper (Richard et al. 2019, arXiv:1903.02474)
  have no HTML rendering; only the CRS abstract was read (about 8 million
  objects, 0.15 < z < 3.5), so no 4MOST requirement is given. SKA and the
  Simons Observatory flow-downs were not read; CMB-S4 and SO design
  drivers are in `deep/cmb-survey-design.md`.
- The WFIRST-AFTA 2015 report (Spergel et al. 2015, arXiv:1503.03757) has
  no HTML rendering; read at abstract only.
