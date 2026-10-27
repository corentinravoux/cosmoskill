# Line-intensity mapping in CO, [CII] and optical lines — cosmo-reionization-21cm dossier

Scope: how a CO, [CII] or Hα/[O III] intensity map becomes a power
spectrum, a stack, a one-point statistic or a cross-spectrum, how an upper
limit becomes a statement on L_CO(M_h) and ρ_H2, and how to choose between
estimators and interloper treatments. COMAP supplies the most complete
published chain and is followed step by step; each step also gives what
COPSS and mmIME (CO), CONCERTO, TIME, EXCLAIM and Planck × SDSS ([CII]) and
HETDEX and BOSS (Lyα) do in its place.
Snapshot: 2026-10-21.
From: Bernal & Kovetz 2022 review (arXiv:2206.15377), Sects. 2, 3, 5 and 6;
SKA EoR/CD synergies chapter (arXiv:2606.30947), Sect. 3.3.

Already in L2, not repeated here: the measured values (COPSS, mmIME, COMAP,
Planck × SDSS [CII], tomographic backgrounds) in
`results.md#line-intensity-mapping-co-cii-lyalpha`; the experiment list in
`surveys-and-data.md#line-intensity-mapping-experiments-co-cii`; the origins
of the method and the burstiness boost of shot noise in
`physics-and-methods.md#line-intensity-mapping-in-other-lines`; the COMAP
transfer-function form T(k) = T_f T_b T_p T_ν in
`systematics.md#line-intensity-mapping`. HI intensity mapping (CHIME,
MeerKLASS) has its own L2 entries
(`physics-and-methods.md#post-reionisation-hi-intensity-mapping`); it is
cited here only where a method is shared.

## How it is done
<!-- key: how-it-is-done -->

Notation (COMAP, Chung et al. 2024, arXiv:2406.07512, Sect. 2; followed
throughout). T is the line brightness temperature of a voxel (a
three-dimensional pixel in angle × frequency); ⟨T⟩ its cosmic mean; b the
luminosity-weighted bias of the line emitters; L(M_h) the mean line
luminosity of a halo of virial mass M_h; dn/dM_h the halo mass function;
b_h(M_h) the halo bias; P_m(k) the matter power spectrum. L′_CO is the line
luminosity in observer units (K km s⁻¹ pc²). COMAP quotes k in Mpc⁻¹ (no h);
COPSS and mmIME in h Mpc⁻¹.

### Step 1. Clean the time streams and make maps
<!-- key: step-1-clean-the-time-streams-and-make-maps -->

- Single-dish, millimetre (CCAT EoR-Spec simulations, Dev et al. 2026,
  arXiv:2607.20404, Sects. 3.3–3.4) [src]: polynomial de-trending,
  telescope-motion correction, then a common-mode template C(t), the mean of
  the detector time streams in a spectral bin, is regressed out of each
  detector [src: Eqs. 7–8]; a PCA filter then removes the n_comp leading
  detector-covariance eigenmodes [src: Eqs. 9–10]. The authors remove "the
  minimum number of components" because each one costs signal; three was
  adopted, two left excess 1/f noise and four gave more attenuation for no
  gain, with spectra agreeing within ~5% between the three cases [src:
  Sect. 4.3].
- Interferometric (mmIME, Keating et al. 2020, arXiv:2008.08087, Sect.
  III.2.1) [src]: visibilities are Fourier transformed along frequency into
  delay space (η), and the plane η = 0 is discarded. Reason: spectrally
  smooth point sources sit there; with it the contaminant power would be
  ~200 μK² Hz sr, comparable to the line signal, and ~50 μK² Hz sr even after
  masking sources above ~30 μJy. The cut costs 3% of sensitivity and leaves
  ≲ 0.1 μK² Hz sr.
- Interferometric, ground pickup (COPSS on the SZA, Keating et al. 2016,
  arXiv:1605.03971, Sect. III.2.1) [src]: antenna-orientation-dependent
  signals (telescope environment, cross-talk) correlate between antennas; the
  fields were observed lead–trail, and the variance-weighted average of the
  three fields of a group, per hour angle, channel and baseline, is
  subtracted as a ground model. Cost: 33% fewer independent measurements,
  ~18% sensitivity. Before it 0.2% of modes exceeded the noise by > 5σ, the
  largest ~10³ times; after it none did. Pilot data without lead–trail kept
  only the outrigger baselines that a jackknife showed free of ground.
- Single-dish, millimetre, real data (TIME commissioning, Yang et al. 2025,
  arXiv:2511.09473) [src: abstract]: gains and pointing from Jupiter; common-
  mode subtraction "with correlation-weighted scaling" removes correlated
  noise and a map-domain PCA identifies further systematics; on the Galactic
  Sgr A field the broadband continuum agrees with BGPS to ~5%. This is a
  commissioning test, not a cosmological map.
- Continuum removal, [CII] (CONCERTO simulations, Van Cuyck et al. 2023,
  arXiv:2306.01568) [src]: PCA against arPLS, a per-pixel asymmetric
  penalised-least-squares baseline that fits the frequency-coherent CIB,
  Galactic dust and CMB together, with one regularisation parameter R = 1
  [src: Sect. 3.2, Eqs. 9–11]. arPLS brings the continuum below the z = 7
  [CII] power by a factor > 70; PCA reaches only 0.7 [src: abstract].
- Optical IFU spectra, Lyα (HETDEX, Lujan Niemeyer et al. 2025,
  arXiv:2510.11427) [src]: the intensity is taken from spectra containing no
  LAE above S/N 5.5 [src: abstract]; sky residuals that survive masking are
  removed by a PCA per field on normalised IFU spectra (N_λ = 1036; ~7% of
  voxels masked in the remaining fibres) [src: Sect. II.2.7, Eq. 2].

### Step 2. Estimate the power spectrum without a noise bias
<!-- key: step-2-estimate-the-power-spectrum-without-a -->

COMAP Season 2 (Stutzer et al. 2024, arXiv:2406.07511, Sect. 2) [src]:

- Auto-power P(k) = (V_vox/N_vox)⟨|f_i(k)|²⟩ with f_i the Fourier
  coefficients of map m_i, V_vox the voxel volume and N_vox the number of
  voxels [src: Eq. 1]; it contains signal, noise and systematics [Eq. 2].
- A cross-spectrum C_ij(k) = (V_vox/N_vox)⟨Re{f_i* f_j}⟩ [Eq. 3] between
  maps with independent noise and systematics is unbiased for P_CO [Eq. 4].
- Maps are made per feed group (feeds sharing a first down-conversion local
  oscillator; 4 groups from 19 feeds) and per elevation half; only
  cross-spectra that cross both feed group and elevation are averaged with
  inverse-variance weights [src: arXiv:2406.07511, Eqs. 7–8]. Reason: systematics found in
  Season 2 are common to a feed group, so feed–feed crosses within a group
  would not cancel them; elevation split targets ground sidelobe pickup.
  Cost: Eq. 6 predicts ~12% sensitivity loss against feed–feed crosses,
  "a little larger" in practice [src: Sect. 2.1].
- Maps are weighted by 1/(σ_A σ_B) per voxel before the transform, so the
  result is a pseudo-spectrum with coupled modes [src: Eq. 9].
- Errors come from randomised null difference (RND) maps: scans split into
  random halves, Δm = (m_A − m_B)/2, which keeps white and correlated noise
  and filter effects but cancels signal [src: Sect. 2.3, Eq. 13]. Reason:
  white-noise simulations (used in Early Science) miss correlated noise, and
  time-stream simulations through the pipeline were too expensive.
- The spectrum is divided by the transfer function per k bin (L2); limits
  are 95% per bin with a positivity prior [src: arXiv:2406.07511, Sect. 5.4].

Peers for this step:

- COPSS [src: arXiv:1605.03971, Sect. III.2, Eq. 1]: Δ²(k) = k³P(k)/(2π²)
  from gridded delay-visibilities, computed two ways, the product of
  semi-correlated pairs (PSCP) and a maximum-likelihood evaluation of the
  band-averaged power; P in μK² h⁻³ Mpc³, k in h Mpc⁻¹.
- CONCERTO [src: arXiv:2306.01568, abstract]: the P of K EstimatoR (POKER)
  adapted to masked LIM cubes.
- HETDEX [src: arXiv:2510.11427, abstract and Sect. IV.3]: a cross-power of
  Lyα intensity with LAEs, so no noise bias; model and covariance from
  lognormal mocks of the LAE catalogue and the intensity in redshift space,
  with the HETDEX sensitivity, selection and mask. The PCA suppresses but does
  not eliminate power, and sky subtraction suppresses k ≲ 0.4 h Mpc⁻¹; both
  are carried by the mocks into the model rather than divided out of the
  data, the reverse of COMAP's per-bin transfer-function division.

### Step 3. Fit a two-amplitude model
<!-- key: step-3-fit-a-two-amplitude-model -->

P(k) = A_clust P_m(k) + P_shot [src: arXiv:2406.07512, Eq. 1], with

- ⟨Tb⟩ ∝ ∫ dM_h (dn/dM_h) L(M_h) b_h(M_h) [Eq. 2]; b the same integral
  divided by ∫ (dn/dM_h) L [Eq. 3];
- P_shot ∝ ∫ dM_h (dn/dM_h) L²(M_h) b_h(M_h) as printed [Eq. 4], which the
  text calls "the second bias- and abundance-weighted moment"; the SPHEREx
  forecast writes it without b_h (arXiv:2606.10005, Eq. 23). Either way the
  shot term weighs bright haloes as L²;
- in redshift space at low k, with Ω_m(z) ≈ 1,
  A_clust ≈ ⟨Tb⟩² (1 + 2/(3b) + 1/(5b²)) [Eq. 5].

Two variants [src: Sect. 2.2]: "b- and v_eff-agnostic" fits A_clust and
P_shot directly; "informed" maps (⟨Tb⟩², P_shot) to b and to an effective
line width v_eff (fitting functions from Chung et al. 2022) to include RSD
and line-broadening suppression. ⟨T⟩ is bounded only through b > 2, which
the authors call "a fairly conservative lower bound" from prior modelling.
The likelihood is Gaussian and independent between k bins, justified by
≲ 10% bin-to-bin correlation in the Season 2 spectrum [src: arXiv:2406.07512,
Sect. 2.3.2, footnote to Eq. 12].

### Step 4. Fit the halo–line connection with external priors
<!-- key: step-4-fit-the-halo-line-connection-with -->

Five-parameter analysis [src: arXiv:2406.07512, Sect. 2.3.1]:

- L′_CO(M_h) = C / [(M_h/M)^A + (M_h/M)^B] [Eq. 6], with log-normal
  scatter σ (dex); L_CO/L_⊙ = 4.9 × 10⁻⁵ L′_CO for CO(1–0) [src: arXiv:2406.07512,
  Sect. 2.3.1, Eq. 7].
- "UM" priors loosely from UniverseMachine: A = −1.66 ± 2.33, B = 0.04 ±
  1.26, log C = 10.25 ± 5.29, log(M/M_⊙) = 12.41 ± 1.77 [Eqs. 8–11];
  σ = 0.4 ± 0.2 dex, centred on Li et al. 2016 and broadened [src: arXiv:2406.07512,
  Sect. 2.3.1].
- Narrowed by the COLDz CO luminosity function at z ~ 2.4: each MCMC step
  paints peak-patch haloes (161 realisations of 0.16 Gpc³, Tinker 2008 mass
  function), fits a Schechter function, and compares with the COLDz
  Schechter posterior through a kernel density estimate; 250 walkers, 4242
  steps, 1000 burn-in. Reason for replacing Bolshoi–Planck: its cosmology
  is "slightly discrepant" with the fiducial one [src: arXiv:2406.07512, Sect. 2.3.1].
- The LIM data then enter as an additive Gaussian log-likelihood
  [Eq. 12] at z ~ 2.8, without positivity priors (the model is positive) [src:
  arXiv:2406.07512, Sect. 2.3.2].

The model chain these priors descend from (Li et al. 2016,
arXiv:1503.08833, Sect. II.2) [src]: halo → mean SFR(M, z) from Behroozi
et al. 2013 → log-normal scatter σ_SFR = 0.3 ± 0.1 → L_IR from SFR =
δ_MF × 10⁻¹⁰ L_IR [Eq. 1], log δ_MF = 0.0 ± 0.3 → L′_CO from log L_IR = α
log L′_CO + β [Eq. 2] (fiducial α = 1.37, β = −1.74 from Carilli & Walter;
priors α = 1.17 ± 0.37, β = 0.21 ± 3.74, the mean and full range of four
published fits) → scatter σ_LCO = 0.3 ± 0.1 → brightness temperature by
Rayleigh–Jeans [Eq. 5]. The authors note the four (α, β) fits lie on one
line, α ≈ 0.10β + 1.19 [Eq. 3], "as they are generally derived from similar
samples of the most luminous" galaxies.

COPSS fits a single shot-noise amplitude: P_CO = 3.0 ± 1.3 × 10³ μK²
(h⁻¹ Mpc)³, Δ²_CO(k = 1 h Mpc⁻¹) = 1.5 ± 0.7 × 10³ μK², P_CO > 0 at 98.9%,
over k = 0.5–10 h Mpc⁻¹, z = 2.3–3.3, 19 fields, 0.7 deg² [src: Keating et
al. 2016, arXiv:1605.03971, abstract].

### Step 5. Convert to molecular gas density
<!-- key: step-5-convert-to-molecular-gas-density -->

ρ_H2 = α_CO ⟨T⟩ H(z) / (1 + z)² [src: arXiv:2406.07512, Eq. 13], with
α_CO = 3.6 M_⊙ (K km s⁻¹ pc²)⁻¹ at z ~ 2.8. Reason: the value "most
commonly used" by line searches and LIM analyses, first found in three
z ~ 1.5 galaxies; values up to twice as high are advocated [src: Sect.
3.1]. The headline ⟨T⟩ < 2.4 μK gives ρ_H2 < 1.6 × 10⁸ M_⊙ Mpc⁻³.

mmIME instead converts a shot power [src: arXiv:2008.08087, Sect. V]:
the 3 mm spectral shot power is split among CO(2–1) to CO(5–4) with a
modified Li model (Kamenetzky et al. line fits, L_IR = 10¹⁰ SFR [Eq. 12],
0.3 dex scatters) [Eq. 11, Table 4], then each line is fitted with
L_CO = A_CO M²/M_0 below M_0 = 10¹² M_⊙/h and constant above [Eqs. 17–18],
motivated by a molecular fraction peaking near that mass, and converted
with α_CO = 3.6.

COPSS goes through a luminosity-to-halo-mass ratio, A_CO = 6.3 (+1.4/−2.1) ×
10⁻⁷ L_⊙/M_⊙, a molecular gas fraction f_H2 = 5.5 (+3.4/−2.2) × 10⁻² for
~10¹² M_⊙ haloes, and "simple theoretical estimates" of its scaling, to
ρ_H2(z ~ 3) = 1.1 (+0.7/−0.4) × 10⁸ M_⊙ Mpc⁻³ [src: arXiv:1605.03971,
abstract]; the COMAP re-analysis of COPSS under its own L(M_h) is below
(Choices).

### Step 6. Stack on a galaxy catalogue
<!-- key: step-6-stack-on-a-galaxy-catalogue -->

COMAP × eBOSS/DESI quasars (Dunne et al. 2025, arXiv:2510.23568, Sect. 4)
[src]:

- Convert T_b to L′_CO per voxel [Eqs. 13–14]; cut 31 × 31 × 81-voxel
  cubelets (113 × 113 × 337 cMpc) around each quasar, "much larger than the
  expected extent" to include clustering; co-add with inverse-variance
  weights per field [src: arXiv:2510.23568, Sect. 4.1].
- Inject simulated signal into time-ordered data to get a pipeline-processed
  template t and an unprocessed one r; amplitude a = (tᵀt)⁻¹ tᵀ s by
  matched filter [Eq. 15]; ⟨L′_CO⟩ = a × sum of r over the central 5 × 5
  spaxels and 3 channels [Eq. 16]. Reasons: the template weights the
  voxels with most signal and corrects pipeline signal loss at once; 5 × 5
  rather than 3 × 3 because clustering broadens the stack.
- Errors from 10 000 stacks on catalogues offset by 1–10 spaxels or
  channels [src: arXiv:2510.23568, Sect. 4.3]; this captures correlated noise but not sample
  variance, which is assigned to the model side.
- Attenuation and variance factors applied to models [src: arXiv:2510.23568, Sects. 6.2–6.3]:
  redshift scatter 1669 km/s gives f_VI = 1.21; pointing 1.05; template
  model dependence d_MD = 1.069; interloper scatter d_LI = 1.038.

Lyα and [CII] peers in cross-correlation with spectroscopic tracers:

- BOSS Lyα (Croft et al. 2018, arXiv:1806.06050) [src: abstract]: the
  residual flux of BOSS LRG spectra after subtracting the best-fit galaxy
  model is crossed with BOSS quasars (signal on 1–15 h⁻¹ Mpc) and with the Lyα
  forest (no signal; 95% limit on the global Lyα surface brightness μ < 1.2 ×
  10⁻²² erg s⁻¹ cm⁻² Å⁻¹ arcsec⁻²). Correcting a contamination from quasar
  clustering on cross-fibre light lowers the quasar cross by 50% against the
  DR10 result. The authors conclude that LAEs contribute but quasars dominate
  within 15 h⁻¹ Mpc.
- HETDEX Lyα (arXiv:2510.11427) [src: abstract]: LAE × Lyα intensity over
  1.9 < z < 3.5 gives b_g b_I ⟨I⟩ F̄_RSD/F̄_RSD^fid = 6.7 ± 3.1, 11.7 ± 1.4 and
  8.3 ± 1.5 × 10⁻²² erg s⁻¹ cm⁻² arcsec⁻² Å⁻¹ at z̄ = 2.1, 2.6 and 3.2,
  "reasonably consistent" with hydrodynamical simulations with Lyα radiative
  transfer.
- The comparison as HETDEX states it [src: arXiv:2510.11427, Sect. VII]:
  with b_g = 2 assumed, its b_I⟨I⟩ is "significantly smaller" than the values
  from quasar–Lyα intensity crosses (Croft et al., Lin et al.); the low- and
  high-z bins are consistent with the forest–Lyα upper limit, the medium-z
  bin 2.6σ above it. The suggested cause is that quasar crosses are dominated
  by small-scale physics around quasars, such as an elevated radiation field.
- Planck × SDSS [CII] (Pullen et al. 2018, arXiv:1707.06172) [src: abstract]:
  the three highest-frequency Planck maps crossed with BOSS quasars and CMASS
  galaxies, fitting [CII], CIB and thermal SZ jointly; an anomalous emission
  I_ν = 6.6 (+5.0/−4.8) × 10⁴ Jy/sr (95%) at z = 2–3.2 in the 545 GHz map,
  but the [CII] model and the CIB + SZ-only model are "equally plausible" by
  BIC.
- EXCLAIM (Cataldo et al. 2021, arXiv:2101.11734) [src: abstract]: a
  balloon-borne cryogenic telescope (90-cm primary at ~1.7 K, six μ-Spec
  modules, 420–540 GHz, R = 512) designed to map CO and [CII] over 0 < z <
  3.5 and to "cross-correlate with a spectroscopic galaxy catalog" to detect
  the emission unambiguously; the comparison of estimators above
  (arXiv:2603.13218) uses EXCLAIM-like simulations.

### Step 7. One-point statistics
<!-- key: step-7-one-point-statistics -->

The voxel intensity distribution (VID) 𝒫(T) (Breysse et al. 2017,
arXiv:1609.01728, Sect. 2.2) [src]: T = (X_LT/V_vox) Σ L_i over the N
emitters in a voxel [Eq. 5], X_LT the luminosity-to-temperature factor;
𝒫_1(T) from the luminosity function Φ(L) [Eq. 6]; 𝒫_N by repeated
convolution [Eq. 10]; 𝒫(T) = Σ_N 𝒫_N(T) 𝒫(N) [Eq. 11], with 𝒫(N) a
Poisson draw from a log-normal density field [Eqs. 12–16]; noise and
foregrounds enter by convolution [Eq. 18]. Approximation stated by the
authors: every emitter gets the mean bias, which underestimates the number
of very bright voxels.

The conditional VID (CVID) (Kramer et al. 2026, arXiv:2603.13218, Sect.
3.2) [src]: histogram separately voxels with and without a catalogue object
(plus adjacent voxels); Fourier transform both; their ratio ℛ cancels any
contaminant uncorrelated with the catalogue [Eqs. 8–12]. Voxels are first
divided by their noise σ_i [Eq. 14]; ~40 000 bins over ±5.69; S/N² from
the real and imaginary parts against 1 + 0i [Eq. 15], cut at weighted
Ĩ = 2.5 where the noisy ratio departs from the noiseless one.

No VID or CVID measurement on real LIM data was found (one search,
2021–2026, returned only forecasts and methods).

### Step 8. Cross-spectra with galaxies or with another line
<!-- key: step-8-cross-spectra-with-galaxies-or-with -->

- Galaxy cross-power (Kramer et al. 2026, arXiv:2603.13218, Sect. 3.3) [src]: δ_I = Î − Ī
  against δ_QSO = (N − N̄)/N̄ [Eqs. 16–17], computed in 3° × 2.5° patches to
  avoid large-scale 1/f correlations; S/N² = Pᵀ C⁻¹ P with C from 1000
  simulations [Eq. 18].
- Line–line cross-power (SPHEREx forecast, Ambrose et al. 2026,
  arXiv:2606.10005, Sect. 2.7) [src]: δP₁₂² = (P₁₂² + P₁P₂)/(2N_k)
  [Eq. 24], each auto-power the sum of signal, noise σ_N² Ω_pix and
  interlopers; Δk = k/5, Δz = 0.1(1 + z) because wider slices "would require
  temporal modeling". Reason for crossing lines: it "eliminates such
  foreground contamination" from low-z interlopers.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

**Auto-spectrum versus stack versus CVID versus cross-power.** Compared on
the same EXCLAIM-like [CII] simulations with BOSS/eBOSS quasars (Kramer et
al. 2026, arXiv:2603.13218) [src]: mean S/N 8.42 (cross-power), 4.47 (stack), 3.92 (CVID)
[Sects. 4.1–4.3]; yet each constrains a single amplitude A of L_[CII] to
about 50%, two together to 33%, all three to 27% (A = 0 rejected at ~4σ,
~6σ, ~7.3σ) [Sect. 4.4]. Stack and CVID share information through the
imaginary part of ℛ; the cross-power is the least redundant [Sect. 5].
Cost: the stack compresses to one number and becomes degenerate with more
than one parameter; the CVID is sensitive to binning and its covariance has
artefacts that hamper inversion; the authors say it "requires some deeper
thought ... before being applied to real data" [Sect. 5].

**Agnostic two-amplitude fit versus halo model.** The two-amplitude fit
needs no astrophysics but allows clustering and shot noise to trade off
freely; the informed variant reaches "unphysical parameter space" with
high clustering-to-shot ratios; the five-parameter fit ties them through
L(M_h) but imports UM and COLDz priors [src: arXiv:2406.07512, Sects. 2.3
and 3.1]. The halo-model ⟨T⟩ = 0.72 (+0.45/−0.30) μK "should not be
considered a COMAP 'detection' of any kind" [Sect. 3.2].

**Model-dependent ρ_H2.** COPSS's ρ_H2 rested on a linear L_CO–M_h relation,
a linear molecular fraction and a prior on σ that lowered the luminosity
per halo; re-analysed in the COMAP framework COPSS gives ρ_H2 < 6.4–7.4 ×
10⁸ M_⊙ Mpc⁻³ against COMAP S2 < 1.6 × 10⁸ [src: arXiv:2406.07512, Sect.
4]. α_CO differs between analyses: 3.6 (COMAP, mmIME), 4.3 (COPSS), 6.5
(the 850 μm stacking comparison) [src: Fig. 6 caption].

**Interloper treatments.**

| Treatment | Assumes | Cost | Read in |
|---|---|---|---|
| Fit the anisotropy of mis-projected interlopers | interlopers far in z, so α_∥ ≠ α_⊥ | needs low noise "more sensitive instrument than currently planned" for z = 7 [CII] | Lidz & Taylor 2016, arXiv:1604.05737, Sect. II, VII |
| Mask bright voxels (targeted, from a catalogue) | catalogue complete for bright CO | masked voxels lost; FG2 masking at L_*/10 removes a few per cent of voxels | arXiv:1609.01728, Sect. 5.2; arXiv:2606.17210 |
| Blind masking across bands | extra lower-frequency bands | needs bands EoR-Spec lacks today | arXiv:2606.17210 [src: abstract] |
| Cross with galaxies or another line | contaminant uncorrelated with tracer | measures only the correlated part; Galactic foregrounds still leaked into low-k cross-power and ℛ | arXiv:2603.13218, Sect. 4.1; arXiv:2606.10005 |
| Mask low-z galaxies from a stellar-mass catalogue (CO proxy) | stellar mass traces CO power | residual line power 2 × 10² Jy²/sr from faint undetected sources; [CII]/residual = 62 ± 32 at z = 5.2 for 22% area lost, 2.0 ± 1.4 at z = 7; residual CO and [CI] limit z > 7; residuals vary 12–15% field to field | CONCERTO sims, arXiv:2306.01568 [src: abstract] |
| Model in the VID | foreground Φ(L) known in form | shot-noise foreground mildly degrading; clustering foreground leaves only upper limits | arXiv:1609.01728, Sect. 5.2 |

The interloper geometry (Lidz & Taylor 2016, Sect. II) [src]: mapping an
interloper at z_i with the target redshift z_t rescales wavenumbers by
α_∥ = [H(z_t)/H(z_i)] (1 + z_i)/(1 + z_t) and α_⊥ = D_A,co(z_i)/D_A,co(z_t)
[Eqs. 5–6], so P_tot = P_t + P_i(k_∥/α_∥, k_⊥/α_⊥)/(α_∥ α_⊥²) [Eq. 8].
For a target above the interloper, α_∥ > 1 and α_⊥ < 1; if P_i falls with
k, this boosts line-of-sight power relative to transverse power, the
signature the fit uses.

**Where VID beats P(k) for interlopers.** A shot-noise interloper is exactly
degenerate with the target shot noise in P(k) but only weakly degenerate in
the VID (Fisher forecast, CO at z ~ 3) [src: arXiv:1609.01728, Sect. 5.2].

**Cross-spectrum noise splits.** COMAP pays ~12% sensitivity for feed-group
crosses to cancel group-common systematics; mmIME and COPSS use jackknives
instead of a cross-spectrum (below). COPSS pays ~18% sensitivity for its
lead–trail ground subtraction [src: arXiv:1605.03971, Sect. III.2.1].

**Auto-spectrum or cross with a tracer, Lyα case.** A quasar cross samples
only the ~3% of space within 15 h⁻¹ Mpc of a quasar and can be dominated by
the quasars themselves; a cross with the Lyα forest or with LAEs samples the
global emission [src: Croft et al. 2018, arXiv:1806.06050, abstract;
arXiv:2510.11427, Sect. VII]. The HETDEX and quasar-cross amplitudes are
therefore not the same quantity, as HETDEX itself discusses.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| A_clust, agnostic, 95% | < 31 μK² | COMAP S2 | arXiv:2406.07512 | Table 1 |
| P_shot, agnostic / informed, 95% | < 3.7 / < 4.9 × 10³ μK² Mpc³ | COMAP S2 | arXiv:2406.07512 | Table 1 |
| ⟨T⟩ (b > 2), 95% | < 2.4 μK | COMAP S2 | arXiv:2406.07512 | Table 1, Sect. 3.1 |
| ρ_H2, 95% | < 1.6 × 10⁸ M_⊙ Mpc⁻³ (α_CO = 3.6) | COMAP S2 | arXiv:2406.07512 | Table 1 |
| ⟨T⟩, ρ_H2 with priors | 0.72 (+0.45/−0.30) μK; 5.0 (+3.1/−2.1) × 10⁷ M_⊙ Mpc⁻³ | UM+COLDz+COPSS+COMAP S2 | arXiv:2406.07512 | Sect. 3.2 |
| Gain S1 → S2 | ×5 on P_shot, ×2 on A_clust | COMAP | arXiv:2406.07512 | Sect. 3.1 |
| Line-broadening attenuation | ~10% at COMAP k, ~30% at COPSS k | Chung et al. 2021 via COMAP S2 | arXiv:2406.07512 | Sect. 3.1 |
| Mode mixing | < 20% for k ≳ 0.1 Mpc⁻¹ | COMAP | arXiv:2406.07512 | Sect. 2.1 |
| k binning | Δ(log k Mpc) = 0.155 | COMAP S2 | arXiv:2406.07512 | Sect. 2.1 |
| Data volume | 17 500 h, three 2–3 deg² fields, May 2019–Nov 2023 | COMAP S2 | arXiv:2406.07512 | Sect. 2.1 |
| RND maps | 244 per run: 61 for errors, 183 for χ² distribution | COMAP S2 | arXiv:2406.07511 | Sect. 3 |
| Injection test | ≈ 6σ recovery of ×3 boosted signal, 1.5σ from input | COMAP S2 | arXiv:2406.07511 | App. D |
| Stack limit | ⟨L′_CO⟩ = 4.15 ± 2.94 × 10¹⁰ K km s⁻¹ pc² (1.41σ); best-fit a = 0.20 of fiducial | COMAP × eBOSS/DESI | arXiv:2510.23568 | Sect. 5 |
| Extra stack masking | +12.5% voxels masked, +2% stack error | COMAP × eBOSS/DESI | arXiv:2510.23568 | Sect. 2.1.1 |
| Clustered neighbours in a stack | ~50% of stacked intensity | EXCLAIM-like sims | arXiv:2603.13218 | Sect. 4.2 |
| COPSS P_CO | 3.0 ± 1.3 × 10³ μK² (h⁻¹ Mpc)³; Δ²(k = 1) = 1.5 ± 0.7 × 10³ μK²; > 0 at 98.9% | COPSS II | arXiv:1605.03971 | abstract |
| COPSS A_CO, f_H2, ρ_H2 | 6.3 (+1.4/−2.1) × 10⁻⁷ L_⊙/M_⊙; 5.5 (+3.4/−2.2) × 10⁻²; 1.1 (+0.7/−0.4) × 10⁸ M_⊙ Mpc⁻³ | COPSS II | arXiv:1605.03971 | abstract |
| COPSS ground subtraction | −33% independent measurements, −18% sensitivity; modes > 5σ 0.2% → 0 | COPSS II | arXiv:1605.03971 | Sect. III.2.1 |
| Planck × SDSS [CII] | I_ν = 6.6 (+5.0/−4.8) × 10⁴ Jy/sr (95%), z = 2–3.2 | Planck 545 GHz × BOSS | arXiv:1707.06172 | abstract |
| HETDEX b_g b_I⟨I⟩ | 6.7 ± 3.1, 11.7 ± 1.4, 8.3 ± 1.5 × 10⁻²² erg s⁻¹ cm⁻² arcsec⁻² Å⁻¹ at z̄ = 2.1, 2.6, 3.2 | HETDEX LAE × Lyα | arXiv:2510.11427 | abstract |
| BOSS Lyα × forest | μ < 1.2 × 10⁻²² erg s⁻¹ cm⁻² Å⁻¹ arcsec⁻² (95%) | BOSS DR12 | arXiv:1806.06050 | abstract |
| CONCERTO continuum removal | arPLS > 70× below [CII] at z = 7; PCA 0.7 (**forecast**) | SIDES sims | arXiv:2306.01568 | abstract |
| η = 0 cut | contaminant 200 → ≲ 0.1 μK² Hz sr; −3% sensitivity | mmIME | arXiv:2008.08087 | Sect. III.2.1 |
| Line shares of 100 GHz shot power | CO(2–1) 0.43, (3–2) 0.40, (4–3) 0.14, (5–4) 0.03 (model) | mmIME | arXiv:2008.08087 | Table 4 |
| Li model priors | σ_SFR, σ_LCO = 0.3 ± 0.1; log δ_MF = 0.0 ± 0.3; α = 1.17 ± 0.37; β = 0.21 ± 3.74 | Li et al. 2016 | arXiv:1503.08833 | Sects. II.2.2–II.2.4 |
| CCAT transfer function | > 80% at k ≳ 0.5 Mpc⁻¹; < 20% at k ≲ 0.1 Mpc⁻¹ (**forecast**) | EoR-Spec sims | arXiv:2607.20404 | Sect. 4.3 |
| SPHEREx line–line S/N | 35 (Hα × [O III], z = 5, fiducial); up to 99 (no dust, brighter LF); none at z = 7–8 (**forecast**) | sims | arXiv:2606.10005 | Sect. 3.2 |
| SPHEREx interloper masking | 1.2–5.6% of pixels at the 3σ detection mass (**forecast**) | sims | arXiv:2606.10005 | Sect. 2.6 |
| SPHEREx 3σ detection mass, z = 5 | 1 × 10¹¹ M_⊙ (Hα), 9.5 × 10¹⁰ M_⊙ ([O III]) | sims | arXiv:2606.10005 | Sect. 3.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Noise bias in an auto-spectrum.** Shows as positive power everywhere.
  Test: cross-spectra between splits with independent noise; COMAP's
  feed-group × elevation crosses [src: arXiv:2406.07511, Sect. 2.1].
- **Errors that miss correlated noise.** White-noise simulations sufficed in
  Early Science and failed at Season 2 sensitivity [src: arXiv:2406.07511,
  Sect. 2.3]. Test: RND difference maps; mmIME randomises cell phases and
  matches thermal estimates within ~10% [src: arXiv:2008.08087, Sect.
  III.2.2].
- **Systematics surviving the cross.** COMAP pass criteria: 312 difference-
  map null tests (26 variables × 3 fields × 1D/2D × fast/slow scans), PTEs
  numerically from RND maps; lowest PTEs ~0.6% (binomial probability 27%);
  KS uniformity PTE 58.7% overall, lowest 5.5% of 12 [src: arXiv:2406.07511,
  Sect. 6, Table 2]. mmIME and COPSS jackknives: couplet, first–last,
  even–odd, cross-window, plus diff-pol and high-η in mmIME; largest outlier
  2.4σ; first–last 2.9σ over a k range, attributed to disjoint uv coverage
  that skews the noise [src: arXiv:2008.08087, Sect. III.2.2, Table 2].
  COPSS's four jackknives (couplet, even–odd, first–last, cross-window) give
  ~60 noise-like values, largest outlier 2.4σ; its cross-window test pairs
  windows two apart because adjacent windows may share noise [src:
  arXiv:1605.03971, Sect. III.2.3].
- **Filter signal loss.** Test: injection end to end; COMAP used one
  realisation in one field and calls it a "sanity check" [src:
  arXiv:2406.07511, App. D]. More PCA modes, more loss [src:
  arXiv:2607.20404, Sect. 4.3].
- **Excess in one bin read as a detection.** COMAP S2 has a 2.7σ excess at
  0.12 < k < 0.18 Mpc⁻¹ and reports a limit [src: arXiv:2406.07511, Sect.
  5.4]; the upper limit is deepest where a point is −1.5σ, not where
  sensitivity is highest.
- **Cross-survey tension from model choices.** COPSS (≈ 2.3σ) sits above the
  COMAP limit in an overlapping bin, with "no statistically significant
  discrepancy"; ρ_H2 disagreements come from different L–M assumptions,
  not from the data [src: arXiv:2406.07512, Sects. 2.1 and 4].
- **Interloper size quoted inconsistently.** COMAP's power-spectrum paper
  gives ~10% CO(2–1) contamination from z = 6–8; the stack paper quotes
  ~30% "of the luminosity ... in map space" from another COMAP paper, and
  simulates a 10% interloper [src: arXiv:2406.07511, Sect. 2.1 footnote;
  arXiv:2510.23568, Sect. 6.3.3]. State which quantity is meant.
- **Ground pickup in an interferometer.** Correlated between antennas through
  orientation-dependent emission; up to ~10³ times the noise in single modes
  before lead–trail subtraction in COPSS [src: arXiv:1605.03971, Sect.
  III.2.1].
- **Cross-fibre light in a Lyα cross.** Quasar clustering leaks light into
  neighbouring fibres; its removal halved the BOSS quasar × Lyα signal
  [src: arXiv:1806.06050, abstract].
- **Continuum removal by PCA at high z.** On CONCERTO simulations PCA leaves
  the dust continuum above the z = 7 [CII] power, unlike a per-pixel arPLS
  baseline [src: arXiv:2306.01568, abstract].
- **Stack attenuation.** Redshift errors, pointing and template shape
  each lower the stack; the stack paper corrects models, not data, and
  keeps sample variance on the model side [src: arXiv:2510.23568, Sects.
  4.3 and 6].
- **Foreground leakage into cross-statistics.** Galactic foregrounds
  correlated spuriously with quasars in simulations; remedy was removing
  patches above ~1 MJy/sr and the k = 0 modes [src: arXiv:2603.13218,
  Sect. 4.1].
- **Quasar hosts not like other haloes.** CVID, stack and cross-power assume
  the same L_[CII](M) in quasar hosts; feedback may break it [src:
  arXiv:2603.13218, Sect. 5].
- **Covariance without super-sample term.** Gaussian or in-data covariances
  omit field-to-field variance, which cannot be estimated from the data and
  matters at intermediate and small scales when noise does not dominate
  [src: Pamuk et al. 2026, arXiv:2609.04488, abstract].
- **Shot-noise-only detections.** SPHEREx and CCAT forecasts are
  shot-noise dominated, so the signal is from bright, individually
  detectable galaxies, not the faint population [src: arXiv:2606.10005,
  Sect. 3.2; arXiv:2607.20404, Sect. 4.3].
- **Spurious line candidates.** ASPECS-Pilot found 14 [CII] candidates, all
  later shown spurious, an argument COMAP gives for statistical single-dish
  measurements [src: arXiv:2406.07512, Sect. 4].

## Reading list
<!-- key: reading-list -->

- Foundation (model): Li et al. 2016, arXiv:1503.08833 — halo → SFR → L_IR →
  L′_CO chain and its priors.
- Foundation (one-point): Breysse et al. 2017, arXiv:1609.01728 — VID
  formalism, line-foreground classes, masking.
- Foundation (interlopers): Lidz & Taylor 2016, arXiv:1604.05737 —
  anisotropy of mis-projected interlopers.
- Method/application: Stutzer et al. 2024, arXiv:2406.07511 — feed-group
  cross-spectrum, RND errors, null-test suite.
- Application: Chung et al. 2024, arXiv:2406.07512 — limits to A_clust,
  P_shot, L(M_h), ρ_H2.
- Application: Keating et al. 2020, arXiv:2008.08087 — interferometric
  delay-space spectrum, jackknives, multi-line shot power.
- Application: Dunne et al. 2025, arXiv:2510.23568 — matched-filter stack
  with attenuation budget.
- Method comparison: Kramer et al. 2026, arXiv:2603.13218 — stack, CVID and
  cross-power on the same simulations.
- Application, CO interferometer: Keating et al. 2016, arXiv:1605.03971 —
  COPSS ground subtraction, PSCP/MLE spectra, jackknives, ρ_H2.
- Application, Lyα: Lujan Niemeyer et al. 2025, arXiv:2510.11427 — HETDEX
  LAE × intensity, mocks for model and covariance, comparison with quasar
  crosses; Croft et al. 2018, arXiv:1806.06050 — BOSS quasar and forest
  crosses, cross-fibre light.
- Application, [CII]: Pullen et al. 2018, arXiv:1707.06172 — Planck × SDSS.
- Method, [CII]: Van Cuyck et al. 2023, arXiv:2306.01568 — CONCERTO
  continuum removal (PCA vs arPLS), catalogue masking, POKER.
- Instrument: Cataldo et al. 2021, arXiv:2101.11734 (EXCLAIM); Yang et al.
  2025, arXiv:2511.09473 (TIME commissioning pipeline).
- Forecast: Ambrose et al. 2026, arXiv:2606.10005 — SPHEREx line–line
  crosses, masking, dust.
- Forecast/method: Dev et al. 2026, arXiv:2607.20404 — [CII] time-stream
  cleaning and transfer function.
- Critique/test: Clarke et al. 2026, arXiv:2606.17210 — masking tested on
  COSMOS2020-based [CII] cubes; Pamuk et al. 2026, arXiv:2609.04488 —
  missing super-sample covariance.

## Not verified
<!-- key: not-verified -->

- Breysse 2022, arXiv:2209.01223 (VID breaking the ⟨T⟩–b degeneracy): no
  HTML or LaTeX sections; abstract only.
- Sato-Polito & Bernal 2022, arXiv:2202.02330 (joint VID–P(k) covariance):
  abstract only; it finds cosmic variance subdominant to Poisson sampling in
  the VID error.
- COMAP Early Science V (Chung et al. 2022): fitting functions for b and
  v_eff not read.
- The paper behind the "~30%" CO(2–1) interloper estimate quoted by arXiv:2510.23568 (Sect. 6.3.3) (Chung et
  al. 2024a) was not identified or read.
- Clarke et al. 2026 masking numbers beyond the abstract; the spectral-line
  de-confusion method of Cheng et al. 2016 and the ancillary-tracer removal
  of Bernal & Baleato Lizancos 2024: titles seen in a search, not read.
- Gong et al. 2017, the Hα/[O III] intensity-mapping foundation: title seen,
  not read.
- HI intensity-mapping estimators: see `hi-intensity-mapping.md`.
- One title search (CONCERTO, EXCLAIM, HETDEX, TIME) returned no CONCERTO,
  TIME or EXCLAIM power spectrum on sky data; CCAT was not searched; SPHEREx LIM appears here through the forecast only. Lin et al.
  (eBOSS quasar × Lyα intensity) is known through HETDEX's comparison, not
  read. mmIME's later multi-line results were not searched.
