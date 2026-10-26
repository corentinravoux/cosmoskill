# Filament-gas stacking — cosmo-cosmic-web dossier

Scope: how a stacked filament or galaxy-pair signal in tSZ, X-ray, kSZ or
radio maps is built, how its covariance and significance are computed, how
the halo, AGN, point-source and CIB contributions are quantified and
removed, and how the profile is turned into a gas density and temperature;
with the tests that separate a filament signal from an artefact.
Snapshot: 2026-10-17.
From: Walker & Lau 2022 review, Sect. 4.7; eROSITA, Planck and ACT filament
papers.

Already in L2, not repeated here: the four observational routes and the
eRASS:4 masking list (`physics-and-methods.md#gas-in-the-web-methods`); the
table of detections with their inferred gas
(`results.md#filament-gas-detections`); the data sets
(`surveys-and-data.md#gas-in-filaments-x-ray-sz-radio-and-frb-data`); the
headline contamination sizes and mitigations
(`systematics.md#filament-gas-stacking-systematics`); the comparison with
simulations (`open-questions.md#do-simulations-get-filament-gas-right`).
Galaxy × y spectra, pressure-profile halo models and the CIB in C_ℓ^gy are
in `cosmo-cmb-lss-cross-correlations/deep/tsz-cross-correlations.md`; how
the skeleton itself is built is in `deep/web-classification.md`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the stacking geometry
<!-- key: step-1-choose-the-stacking-geometry -->

| Geometry | Construction | Background | Analysis | Place read |
|---|---|---|---|---|
| Galaxy pairs | each cutout rescaled and rotated so the two galaxies sit at (X, Y) = (∓1, 0); 151 × 151 pixels over −3 < X, Y < 3 | mean of the annulus 9 < r < 10, r² = X² + Y² | 262,864 LRG pairs, Planck y (Tanimura et al. 2019, arXiv:1709.05024) | Sect. 3.1 |
| Galaxy pairs, radio and X-ray | same normalised frame, pairs along the vertical axis; per-pixel 0/1 validity weights; variance weighting tested, no change | 9 < r < 10 | 390,808 LRG pairs, GLEAM, OVRO-LWA, ROSAT (Vernstrom et al. 2021, arXiv:2101.09331) | Sects. 3.1, 3.4 |
| Filament spines | radial profile of each filament to 25 Mpc in 20 bins, each map pixel attached to the nearest spine point; masked area weights w_i = A_unmask/A_total (Eq. 3) in a weighted mean (Eqs. 1–2) | 15–25 Mpc per filament | 24,544 SDSS DisPerSE filaments, 30–100 Mpc, Planck y and κ (Tanimura et al. 2020, arXiv:1911.09706) | Sect. 3.1 |
| Filament spines, X-ray | count and exposure HEALPix maps, profile against transverse distance | 10–20 Mpc | 7817 filaments, eRASS:4 (Zhang et al. 2024, arXiv:2406.00105) | Sect. 3.1 |
| Oriented clusters in superclusters | galaxy overdensity smoothed with 20 Mpc FWHM; keep clusters with ν = F_g/σ > 2 and ellipticity e = (λ₁ − λ₂)/(2(λ₁ + λ₂)) > 0.3 (Eqs. 2–3), ~20% of clusters; 80 Mpc cutouts rotated to the long axis; Fourier series I(r, θ) = Σ_m [C_m cos mθ + S_m sin mθ] (Eq. 5) | m = 0 only: outer 30–40 Mpc; m > 0 has zero mean | ACT DR6 y × DES Y3 (Lokken et al. 2024, arXiv:2409.04535) | Sects. II, IV.2.3 |
| Oriented galaxies, kSZ | 2D tidal tensor of the projected galaxy field on the sphere (Eqs. 9–11, 1.8′ Gaussian, N_side = 2048), cutout aligned with the smallest eigenvector; C_m^i(r) (Eq. 1); compensated aperture (Eq. 2) for m = 0, mean ring for m = 2 | CAP annulus for m = 0; cos 2θ weighting removes isotropic terms | 7.3 million photometric BGS objects, log M* > 10.5, ACT (Hadzhiyska et al. 2024, arXiv:2412.03631) | Sects. II.3, II.5 |

Reasons given: the ν and e thresholds maximise the S/N of extended oriented
tSZ in simulations [src: arXiv:2409.04535, Sect. II]; the kSZ quadrupole
needs no compensated filter because "the weighting by cos(2θ) naturally
filters out isotropic contributions" and a mean ring is easier to interpret
[src: arXiv:2412.03631, Sect. II.3]. The kSZ stack is weighted by
reconstructed line-of-sight velocities, τ̂_kSZ ∝ Σ_i T_i v_rec,i/Σ_i
v²_rec,i (Eq. 5), with velocities from linear reconstruction, v_rec = f a H
ψ (Eq. 4), ψ the displacement field [src: Sect. II.3].

### Step 2. Mask, and show that the mask has converged
<!-- key: step-2-mask-and-show-that-the-mask-has-converged -->

- **Clusters.** Mask radius varied from 1 to 4 R₅₀₀; the central peak
  disappears and the amplitude stops falling at 3 R₅₀₀, adopted [src:
  arXiv:1911.09706, Sects. 3.2, 4, App. A]; the same plateau is used for
  Planck PR4 [src: Li et al. 2025, arXiv:2507.08561, Sect. 3.2]. In eFEDS
  no change beyond 1 R₅₀₀, 3 R₅₀₀ kept as conservative [src:
  arXiv:2206.00084, Sect. 5]. In eRASS:4, doubling the cluster mask lowers
  the 0–10 Mpc signal by 7%; a stricter source radius (5% instead of 10%
  of background) raises it by 3% [src: arXiv:2406.00105, Sect. 3.1, App.
  B].
- **Unresolved clusters.** DisPerSE maxima and bifurcations with
  overdensity > 5 are masked at 10′ as possible undetected clusters;
  saddles and minima are not, being underdense [src: arXiv:1911.09706,
  Sect. 3.2].
- **Point sources, X-ray.** A 30″ eFEDS mask removes ~90% of stacked
  point-source flux and 45″ ~99%; profiles stop changing above 30″; a
  painted point-source map stacks to zero after background subtraction;
  60″ gives the same result [src: arXiv:2206.00084, Sect. 5].
- **Point sources, radio.** Bright sources do not average down as 1/√N;
  catalogue subtraction risks over- or under-subtraction and a flat
  threshold fails on a variable background, so sources above 5σ in the
  three smallest scales of an undecimated wavelet transform are modelled
  and subtracted; no masking, 5σ blanking and wavelet subtraction give
  results "not significantly different" [src: arXiv:2101.09331, Sect.
  3.2].
- **Mask anisotropy.** Oriented stacks of the mask itself have
  higher-order moments consistent with zero [src: arXiv:2409.04535, Sect.
  IV.1.3].

### Step 3. Remove the halo term in pair stacks
<!-- key: step-3-remove-the-halo-term-in-pair-stacks -->

- **Non-parametric radial profiles.** The stack is solved as
  y_h(p) = y_L,i(p) + y_R,j(p) (Eq. 1), the single-halo signal in radial
  bin i around the left galaxy plus bin j around the right one, Δr = 0.02,
  excluding −1 < X < 1, −2 < Y < 2 "to avoid biasing the profiles with
  non-circular filament signal"; the residual is averaged over
  −0.8 < X < 0.8, −0.2 < Y < 0.2 [src: arXiv:1709.05024, Sect. 3.2].
  Vernstrom et al. take radial averages excluding the region between the
  pair [src: arXiv:2101.09331, Sect. 3.3].
- **Parametric profiles with a stretch nuisance.** de Graaff et al. fit
  F(r₁) = f(r₁) + f(r₂), f a fourth-order polynomial times an exponential,
  within a 60° wedge along the perpendicular direction, residuals at the
  10⁻⁹ level. The filament is at most ~10% of the overlapping halo
  signals, so they free a stretch factor s of the halo profile under the
  no-filament hypothesis: s = 0.94, changing the filament by ~10% [src:
  arXiv:1709.10378, Sect. 3.2].
- **Why not a halo model.** A halo model with the universal pressure
  profile and a two-halo term reproduces single-LRG profiles, but for a
  pair it over-predicts the signal because the slowly falling two-halo term
  is counted twice; a three-halo term would be needed [src:
  arXiv:1709.05024, Sect. 4.2].
- **Bound gas between the pair.** Painting UPP haloes on all ~1,100,000
  central LRGs gives Δy = 0.29 × 10⁻⁸ in the bridge (0.36 × 10⁻⁸ out to
  3 r₂₀₀) against the measured 1.31 × 10⁻⁸ [src: arXiv:1709.05024, Sect.
  4.2]. Stacking the CMASS galaxy-density map the same way gives a bridge
  of 1–2% of the halo peaks against ~10% in y, hence < 20% from CMASS
  haloes; a Millennium y map with Y ∝ M^(5/3) gives ~20% [src:
  arXiv:1709.10378, Sect. 4.2].

### Step 4. Model unresolved emitters (X-ray)
<!-- key: step-4-model-unresolved-emitters-x-ray -->

eRASS:4 predicts the emission of every galaxy left unmasked [src:
arXiv:2406.00105, Sects. 4.1–4.2]:

1. Halo gas from the RASS L_X–M* stacking relation of Anderson et al.
   2015, re-derived with the same selection on an eRASS mock and corrected
   for the stellar-mass scheme, because a slope ≳ 3 turns a small mass
   offset into a large luminosity offset; single-temperature CIE spectra
   from an L_X–kT relation.
2. AGN and X-ray binaries from their own relations (Sects. 4.1.2–4.1.3,
   not read).
3. Integrated over 0–10 Mpc: 20% halo, 12% AGN, 5% XRB, total 37%;
   bootstrap relative uncertainties 6.9%, 1.8%, 1.4% (arXiv:2406.00105,
   Table 2).
4. Photo-z losses: recovered-flux fraction f = (D_L²(z_true)/n_MC) Σ_i
   w_i/D_L²(z_i) (Eq. 8), w_i = 1 if 0.15 < z_i < 0.7; ~1 for 11 < log M*
   < 12, ~80% for 9.5 < log M* < 11 at z > 0.3, raising the total to
   "as high as ~40%" [src: arXiv:2406.00105, Sect. 4.2] and leaving ~60%
   WHIM at 5.4σ [src: abstract].
5. In the spectral fit the three contaminant normalisations are coupled
   at these ratios [src: Sect. 5.2].

### Step 5. Estimate errors and covariance
<!-- key: step-5-estimate-errors-and-covariance -->

| Method | What it captures | Analysis | Place read |
|---|---|---|---|
| Bootstrap over filaments (1000) | sample variance of the stack; its rms matched the null rms | arXiv:1911.09706; arXiv:2206.00084; arXiv:2507.08561 | Sect. 3.3; Sect. 3.3; Sect. 3.2 |
| Pixel-wise bootstrap | profile covariance (correlation matrix of the five 0–10 Mpc bins shown) | arXiv:2406.00105 | Sect. 3.1, Fig. 3 |
| Random positions and angles (500 control samples of 7817) | background fluctuations and systematics across the sky | arXiv:2406.00105 | Sect. 3.1 |
| Rotation in Galactic longitude at fixed latitude (1000) | sky noise with the Galactic foreground level held fixed | arXiv:1709.05024; arXiv:1911.09706 | Sect. 3.3; Sect. 3.3 |
| Pseudo-pairs: same 6–10 h⁻¹Mpc transverse, > 30 h⁻¹Mpc radial (1000) | noise, sky and halo-subtraction errors together; adopted as the final error | arXiv:1709.05024 | Sect. 3.3 |
| Non-physical pairs, 40–200 h⁻¹Mpc apart (500 subsamples of 13.6 million) | uncorrelated line-of-sight structure, Galactic dust | arXiv:1709.10378 | Sect. 4.1 |
| Control pairs Δz ≥ 0.05; blank fields shifted ≤ 3°; bootstrap of 75% (500 each) | population, local sky, in-sample variance | arXiv:2101.09331 | Sect. 3.4 |
| Sky jackknife, N_sub = 250 (~40 deg², ~4000 pairs each), Hartlap factor | overlap of cutouts; pixels reused | arXiv:1709.10378 | Sect. 3.3, Eqs. 5–7 |
| 24 k-means sky regions (~160 deg²), N_cl-weighted covariance | sample variance from coherent structure over 20 Mpc, varying noise | arXiv:2409.04535 | Sect. V.1, Eqs. 16–18 |

The jackknife was needed because, with ~10⁶ filament rectangles of ~0.12
deg² in 9376 deg², each y pixel enters the stack ~13 times, and the
duplication varies across the map so no single rescaling works [src:
arXiv:1709.10378, Sect. 3.3]. Lokken et al. test the region-to-region
Gaussianity of each bin with a one-sample KS test (fail if p < 0.05); the
lowest p is 0.17 [src: arXiv:2409.04535, Sect. VI]. They do not rescale
simulation errors to the data sample size, since that would understate
the simulations' cosmic variance [src: Sect. V.1].

### Step 6. State a significance, and say which one
<!-- key: step-6-state-a-significance-and-say-which-one -->

| Definition | Analysis | Value | Place read |
|---|---|---|---|
| S/N = (χ²_data − χ²_null)^(1/2), bootstrap covariance, bins to 10 Mpc (Eqs. 4–6) | tSZ along filaments | 4.4 | arXiv:1911.09706, Sect. 3.3 |
| same (Eqs. 2–4) | eFEDS, 0.6–2.3 keV | ~2.8 (p ≈ 0.012) | arXiv:2206.00084, Sect. 3.3 |
| SED in six bands within 2.5 Mpc, overlaps masked | eFEDS | 3.8 (forecast 4.1); p ≈ 0.0017 | arXiv:2206.00084, Sect. 4.1 and abstract |
| S/N = (χ²_data)^(1/2), bootstrap covariance, 0–15 cMpc (Eqs. 4–5) | tSZ along ~30,700 filaments, Planck PR4 | 7.82 (κ: 7.78) | arXiv:2507.08561, Sect. 3.2 |
| excess over 500 random control samples, 0–10 Mpc bins | eRASS:4 | 9.0 | arXiv:2406.00105, Sect. 3.1 |
| χ² → σ with independent pairs (Eq. 4), then jackknife with Hartlap (Eq. 7), n = 12 bins | CMASS pairs | 5.1 → 2.9 (± 0.3 for N_sub = 100–1000); 3.8 with points outside the pair | arXiv:1709.10378, Sect. 3.3 |
| SNR = (χ²_null − χ²_best-fit)^(1/2) against a rescaled Illustris template (Eq. 13) | kSZ oriented | values not read | arXiv:2412.03631, Sect. II.6 |
| box average against the rms of moving-average boxes outside the centre; two-sample KS of data against control distributions | radio and X-ray pairs | ≥ 5σ (3.1σ, 3.6σ for two maps) | arXiv:2101.09331, Sect. 4 |
| null mean and rms of 1000 pseudo-pair stacks | LRG pairs | Δy = (1.31 ± 0.25) × 10⁻⁸ | arXiv:1709.05024, Sect. 3.3 |

The two definitions χ² and χ² − χ²_null differ by the null term, and the
two tSZ filament analyses above also differ in map, sample and radial
range, so their two significances cannot be compared as a gain from the
data alone [der: from the definitions read].

### Step 7. Convert a profile into δ and T
<!-- key: step-7-convert-a-profile-into-delta-and-t -->

**tSZ, cylinder.** y = (σ_T k_B/m_e c²) ∫ n_e T_e dl (arXiv:1709.05024,
Eq. 2), projected for an isothermal cylinder as y(r_⊥) = (σ_T k_B T_e/m_e
c²) ∫_{r_⊥}^{R} 2r n_e(r)/(r² − r_⊥²)^(1/2) dr (Eq. 5), with mean electron
density n̄_e = ρ_b/(μ_e m_p), μ_e ≃ 1.14 (Eq. 4) and constant core
overdensity δ_c so that n_e(0, z) = δ_c n̄_e(0)(1 + z)³ (Eq. 6). Of three
profiles (Eqs. 7–9), simulations prefer r_c/r, giving Δy̅ = 4.9 × 10⁻⁸
(δ_c/10)(T_e/10⁷ K)(r_c/0.5 h⁻¹Mpc) (Eq. 10), hence δ_c T_e r_c = 2.7 ±
0.5 in those units (Eq. 11); with simulated T and morphology, δ ~ 3.2 ±
0.7 [src: Sect. 4.3].

**tSZ with CMB lensing.** β-model n_e = n_e,0/(1 + (r/r_e,c)²) for r <
R_max = 10 Mpc (arXiv:1911.09706, Eq. 9), or constant density to 5 Mpc
(Eq. 10); n_e,0(z) = (1 + δ_e,0) n̄_e(0)(1 + z)³ (Eq. 11); T_e constant
(Eq. 12) or log T_e = α + β log M_BM with β = 0.315 fixed (Eq. 13); the
amplitude scales as 1/cos θ for a filament inclined by θ from the plane of
the sky [src: Sect. 5.1]. κ = ∫ W(z) δ_m dz (Eq. 15) with the same profile
for δ_m (Eq. 17), suppressed above ℓ = 400 as in the map [src: Sect.
5.2]. Joint χ² = χ²_y + χ²_κ (Eqs. 19–21) assuming gas follows dark
matter, δ_e,0 ≃ δ_m,0 and r_e,c ≃ r_m,c, justified by a simulated
filament baryon fraction ~0.9 of cosmic; emcee sampling [src: Sect. 6.1].
Lensing breaks the δ–T degeneracy left by y alone (see L2).

**Inclination by correction instead of model.** Li et al. multiply y_obs
by sin θ, θ now measured from the line of sight, and correct the
over-integration of the 50 cMpc stacking cylinder beyond the ends of a
filament of length L: bias = 25 cos θ/(2L sin θ) (Eq. 22), y_mod =
y_obs sin θ/(1 − bias) (Eq. 23); filaments with tan θ < 25/L are dropped
(3177 removed), avoiding orientation assumptions and computing cost in the
model [src: arXiv:2507.08561, Sect. 3.3, App. D].

**X-ray, multiphase King model.** Volume-averaged emissivity ε̄_det =
1.20 n_H² f_vol (arXiv:2406.00105, Eq. 13), f_vol the volume fraction of
the detected phase; King profiles for n_H and f_vol with a shared core
radius because they are strongly degenerate (Eqs. 14–15); n_H,0(z) =
Δ_b,0 ρ_crit Ω_b (1 + z)³/(1.43 m_H) with constant spine contrast Δ_b,0
(Eq. 16); outer radius 10 Mpc; Gaussian convolution of width σ_sm for the
skeleton position error (Eq. 17); projection with the APEC cooling
function at 0.2 Z☉ (Eq. 18); 7817 individual profiles averaged with
solid-angle weights (Eq. 19); χ² with the bootstrap covariance after
subtracting the contaminants and multiplying the model by 1.13 for
overlapping filaments (Eq. 20); the tSZ profile of arXiv:1911.09706 added
to the likelihood (Eq. 21) to break Δ_b,0–f_vol; Gaussian priors in Table
3 [src: Sect. 6.1].

**X-ray spectrum.** Source 0–10 Mpc, background 10–20 Mpc Wiener-smoothed
over five channels and scaled by the 6–9 keV ratio; 0.5–6.0 keV, C-stat,
BXA with UltraNest; four components (WHIM, halo, AGN, XRB). A 1T APEC at
Z = 0.2 Z☉, chosen from ≲ 0.3 Z☉ in cluster outskirts and > 0.1 Z☉ in
simulated filaments, gives kT = 0.58 ± 0.10 keV, C-stat 105/111; 0.1 or
0.3 Z☉ leave kT unchanged; 0–4 Mpc gives 0.56 ± 0.09 keV [src:
arXiv:2406.00105, Sect. 5.2]. A 1T fit to multi-temperature gas is
pulled to the Fe XVII peak at 0.8–0.9 keV; an excess at 0.5–0.6 keV (O
VII) points to cooler phases, and a log-normal DEM peaked at log T = 5.9,
width 0.45 dex, fits that range better [src: same].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Pairs, spines or orientation
<!-- key: pairs-spines-or-orientation -->

- **Pairs** select bridges of known length between massive haloes but put
  the signal under halo wings it is ~10% of [src: arXiv:1709.10378, Sect.
  3.2]; not every pair is connected — 85% at 5–10 and 70% at 10–15
  h⁻¹Mpc in N-body (Colberg et al. 2005, as cited), which dilutes rather
  than biases [src: arXiv:1709.05024, Sect. 4.1]; LRGs off-centre by ±2
  Mpc change nothing [src: arXiv:2101.09331, Sect. 5.1].
- **Spines** reach 30–100 Mpc filaments but inherit skeleton errors. In
  Horizon-AGN, galaxy and matter skeletons differ by a distance peaking at
  0.37 Mpc (Laigle et al. 2018, as cited), ~1′ at z = 0.47, below the
  Planck beam; a 4 Mpc Gaussian position error would push the tSZ below 3σ
  [src: arXiv:1911.09706, Sect. 4]. eRASS:4 instead fits the broadening
  (σ_sm, Eq. 17) [src: arXiv:2406.00105, Sect. 6.1].
- **Orientation** needs no filament catalogue and its m > 0 moments need
  no background subtraction; the price is that the m = 0 amplitude is
  "adjusted" by an annulus that may remove real signal in rare overdense
  regions [src: arXiv:2409.04535, Sect. IV.2.3].

### Overlapping filaments: mask or correct
<!-- key: overlapping-filaments-mask-or-correct -->

Projected overlap averages 2.5 filaments per pixel within 4 Mpc, 5.5
within 10 Mpc, 11 within 20 Mpc [src: arXiv:2406.00105, Sect. 3.2].
Crossing filaments cancel through the local background; parallel ones
double-count. eRASS:4 measures +13% on 200 mock maps (injected profile
plus a background drawn from the map's angular power spectrum to ℓ =
3000) and divides it out [src: Sect. 3.2, App. C]. eFEDS masks 5′ around
overlaps, "a conservative X-ray signal" [src: arXiv:2206.00084, Sect.
4.1]. Painting model filaments on y and κ maps recovers the input within
10% at the peak [src: arXiv:1911.09706, Sect. 4].

### Background annulus
<!-- key: background-annulus -->

Moving the background from 15–25 to 10–20 cMpc lowers the y and κ
amplitudes and the baryon fraction from 0.127 (+0.019/−0.021) Ω_b
(fiducial, abstract) to 0.086 (+0.016/−0.017), closer to the earlier
analysis; R_max moves to 10 cMpc with it [src: arXiv:2507.08561, App. B
and abstract].

### CIB and beam in tSZ
<!-- key: cib-and-beam-in-tsz -->

- At 30–60′ the CIB is < 10% of the tSZ power (Planck 2016 as cited)
  [src: arXiv:1709.05024, Sect. 4.1]. With leakage 10⁻⁷ < α_CIB < 10⁻⁶ and
  an 857 GHz pair stack of ~10⁻⁵ K, the CIB is 2–3 orders below the
  filament; and since the CIB tracks star-forming haloes, it cannot raise
  the filament-to-halo contrast [src: arXiv:1709.10378, Sect. 4.3].
- In ACT DR6 oriented stacks, CIB-deprojected maps change the y moments
  monotonically with the assumed CIB index β, up to a 2.5-fold depletion
  of the first quadrupole bin at the highest redshift; the authors report
  the non-deprojected map with caveats because deprojection adds noise
  [src: arXiv:2409.04535, Sect. VI].
- The 10′ Planck beam dilutes the mean filament by ~15% in BAHAMAS
  (0.84 against 1.00 × 10⁻⁸) [src: arXiv:1709.05024, Sect. 4.1].

### Redshift-space distortions in the skeleton
<!-- key: redshift-space-distortions-in-the-skeleton -->

Three FoG treatments on the SDSS skeleton (cluster-centre replacement,
NFW redistribution, compression onto a 3 R_vir sphere) were propagated
to the y and κ stacks [src: arXiv:2507.08561, App. A]. Short false
filaments from RSD are removed by the 30 Mpc length cut [src:
arXiv:1911.09706, Sect. 4].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Pair separations | 6–10 h⁻¹Mpc transverse; pseudo-pairs > 30 h⁻¹Mpc radial | Planck × LRG | arXiv:1709.05024 | Sect. 3.3 |
| Pair halo-fit exclusion | −1 < X < 1, −2 < Y < 2; Δr = 0.02 | same | arXiv:1709.05024 | Sect. 3.2 |
| Halo-profile stretch | s = 0.94; filament changes by ~10% | CMASS pairs | arXiv:1709.10378 | Sect. 3.2 |
| Bound-gas share of bridge | < 20% (galaxy map), ~20% (Millennium Y ∝ M^5/3) | CMASS pairs | arXiv:1709.10378 | Sect. 4.2 |
| Jackknife regions | 250 × ~40 deg², ~4000 pairs each | CMASS pairs | arXiv:1709.10378 | Sect. 3.3 |
| Spine profile | 0–25 Mpc, 20 bins; background 15–25 Mpc; mask 3 R₅₀₀, critical points 10′ | Planck × SDSS | arXiv:1911.09706 | Sects. 3.1–3.2 |
| Positional error tolerated | 4 Mpc Gaussian brings tSZ below 3σ | same | arXiv:1911.09706 | Sect. 4 |
| X-ray background and controls | 10–20 Mpc; 500 random controls; 200 mock maps | eRASS:4 | arXiv:2406.00105 | Sects. 3.1–3.2 |
| Signal at the spine | ~0.5% of the total background | eRASS:4 | arXiv:2406.00105 | Sect. 3.2 |
| Overlap correction | ×1.13 | eRASS:4 | arXiv:2406.00105 | Sect. 3.2, Eq. 20 |
| Unmasked contaminants | halo 20%, AGN 12%, XRB 5% (37%); ~40% with photo-z | eRASS:4 | arXiv:2406.00105 | Sect. 4.2, Table 2 |
| X-ray profile priors | log Δ_b,0 ~ N(1.5, 0.5); log f_vol,0 ~ N(−2, 0.3); log r_c ~ N(0.3, 0.2) Mpc | eRASS:4 | arXiv:2406.00105 | Table 3 |
| WHIM 1T temperature | kT = 0.58 ± 0.10 keV at 0.2 Z☉ | eRASS:4 | arXiv:2406.00105 | Sect. 5.2 |
| eFEDS masks | clusters 3 R₅₀₀; point sources 30″ (~90% flux removed) | eFEDS | arXiv:2206.00084 | Sect. 5 |
| Oriented-stack selection | ν > 2, e > 0.3; 20 Mpc FWHM; 80 Mpc cutouts; 24 regions | ACT × DES | arXiv:2409.04535 | Sects. II, V.1 |
| kSZ apertures | m = 0: 9 bins, 1–8′; m = 2: 7 bins, 2–14′ | ACT × DESI BGS | arXiv:2412.03631 | Sect. II.3 |
| Inclination cut | tan θ < 25/L removed (3177) | Planck PR4 × SDSS | arXiv:2507.08561 | App. D |
| Joint y + κ fit | δ = 4.18 (+2.01/−1.06), T_e = 2.74 (+0.65/−0.53) × 10⁶ K (standard β-model) | same | arXiv:2507.08561 | abstract |
| Radio pairs | 390,808 LRG pairs; ≥ 5σ in most maps; B = 30–60 nG | GLEAM, OVRO-LWA, ROSAT | arXiv:2101.09331 | Sect. 4, abstract |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Pixel reuse makes errors too small.** Independent-pair errors gave
  5.1σ where a sky jackknife gives 2.9σ [src: arXiv:1709.10378, Sect.
  3.3]. Test: spatial jackknife or region resampling, with convergence in
  the number of regions.
- **Halo wings read as filament.** A too-narrow halo model leaves positive
  residual between the pair. Test: free the halo width (stretch s), check
  residuals outside the pair, and run pseudo-pairs through the same halo
  subtraction [src: arXiv:1709.10378, Sect. 3.2; arXiv:1709.05024, Sect.
  3.3].
- **Tidally elongated haloes.** Would also show signal beyond the pair
  along the axis; none was seen [src: arXiv:1709.05024, Sect. 4.1].
- **Unresolved emitters counted as WHIM.** Up to ~40% of an X-ray stack
  [src: arXiv:2406.00105, Sect. 4.2]. Test: a forward model of the
  unmasked galaxies with the same selection, and a mask-radius scan.
- **Galactic foreground correlated with position.** Test: rotate in
  longitude at fixed latitude [src: arXiv:1709.05024, Sect. 3.3].
- **Interferometer sidelobes adding coherently.** Midway between pairs the
  sidelobes are ≤ 0.003 (154 MHz) and 0.01 (88 MHz), below the ~1% and
  ~5% excesses; consistency across instruments and in X-ray and tSZ rules
  it out [src: arXiv:2101.09331, Sect. 5.1].
- **CIB leakage in y.** Test: CIB-deprojected maps for several SED
  parameters and a χ² between deprojected and fiducial moments (Eq. 19 of
  arXiv:2409.04535) [src: Sect. VI]; 857 GHz stack times α_CIB [src:
  arXiv:1709.10378, Sect. 4.3].
- **Single temperature for multiphase gas.** Overestimates T; check for
  O VII residuals and try a DEM [src: arXiv:2406.00105, Sect. 5.2].
- **Comparing σ across papers.** A σ from χ², from χ² − χ²_null, from a
  control-sample scatter or from a broadband against an SED are different
  numbers on one dataset: 2.8 and 3.8 for eFEDS [src: arXiv:2206.00084,
  Sects. 3.3, 4.1].
- **Background annulus inside the signal.** A nearer annulus subtracts
  real gas [src: arXiv:2507.08561, App. B]; the bump near 10 cMpc in
  high-z filaments may be neighbouring filaments [src: Sect. 3.2].

## Reading list
<!-- key: reading-list -->

- Method: Tanimura et al. 2019, arXiv:1709.05024 — pair geometry,
  non-parametric halo subtraction, rotation and pseudo-pair nulls, the
  cylinder δ T r_c scaling.
- Critique: de Graaff et al. 2019, arXiv:1709.10378 — halo stretch
  nuisance, bound-gas share, CIB argument, independent-pair against
  jackknife significance.
- Method: Tanimura et al. 2020, arXiv:1911.09706 — spine stacking with
  mask weights, mask convergence, joint y + κ cylinder model.
- Application: Tanimura et al. 2022, arXiv:2206.00084 — eFEDS
  point-source tests, broadband against SED significance.
- Application: Zhang et al. 2024, arXiv:2406.00105 — mock-map validation,
  unresolved-source model, multiphase King fit with tSZ prior, spectral
  stacking.
- Application: Li et al. 2025, arXiv:2507.08561 — Planck PR4 y + κ,
  inclination correction, FoG and background tests.
- Method: Lokken et al. 2024, arXiv:2409.04535 — oriented multipole
  stacks, region covariance, Gaussianity and CIB-deprojection tests.
- Method: Hadzhiyska et al. 2024, arXiv:2412.03631 — kSZ oriented on 2D
  tidal eigenvectors with velocity weighting.
- Application: Vernstrom et al. 2021, arXiv:2101.09331 — radio and X-ray
  pair stacks, wavelet source removal, three null families.
- Review: Walker & Lau 2022, arXiv:2202.07056 — where stacking sits among
  bridge detections (L2).

## Not verified
<!-- key: not-verified -->

- Colberg et al. 2005 (pair connection fractions), Laigle et al. 2018
  (skeleton offsets), Anderson et al. 2015 (L_X–M*), Vijayan & Li 2022
  (1T bias), Gheller & Vazza 2019 (filament baryon fraction and T–M
  relation) and the Planck CIB studies: read only as cited in the
  dossier's papers.
- The AGN and XRB models of arXiv:2406.00105 (Sects. 4.1.2–4.1.3) and its
  WHIM density posterior were not read.
- The kSZ SNR values and the Lokken et al. per-moment S/N were not read.
- Hincks et al. 2022 (A399–A401 bridge modelling) was not read for
  method.
