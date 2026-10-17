# Estimator codes — cosmo-software-ecosystem dossier

Scope: how the numerical settings of clustering and sphere estimator codes
are chosen (FFT mesh, mass assignment, interlacing and shot noise for power
spectra; pair-count tolerance and binning for correlation functions; map
resolution, apodisation, bandpowers, deprojection and purification for
pseudo-C_ℓ), what error each setting leaves, and how to choose between
exact, tree, FFT, map-based and catalogue-based estimators.
Snapshot: 2026-10-17.
From: Snowmass2021 CompF white paper (arXiv:2203.07347), Sect. 5.2
(scalable analysis approaches); DESI (cosmodesi pypower, pycorr) and LSST
DESC and CMB (TreeCorr, NaMaster) code families.

Already in L2, not repeated here: what each estimator code computes in
`physics-and-methods.md#two-point-and-higher-order-estimators`; pypower,
TreeCorr, NaMaster and healpy defaults in
`systematics.md#estimator-conventions` and
`systematics.md#sphere-and-lensing-conventions`; the Corrfunc–TreeCorr
benchmark and the NaMaster validation in
`systematics.md#code-comparisons-read-in-paper-bodies`. Survey-level
choices (line of sight, window, wide-angle terms, integral constraints)
are in the sibling dossier `cosmo-galaxy-clustering/deep/estimators-window.md`.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Pick the estimator family from the data and the observable
<!-- key: step-1-pick-the-estimator-family-from-the-data -->

| Data and observable | Family | Code examples | What sets the accuracy |
|---|---|---|---|
| 3D catalogue, P_ℓ(k) to near the mesh scale | FFT on a mesh | pypower, nbodykit | mesh size, assignment order, interlacing, shot-noise model |
| 3D catalogue, ξ(s, μ), w_p(r_p), with pairwise weights | exact pair counting | Corrfunc, pycorr | none beyond binning (exact counts) |
| Angular or shear correlations over decades in θ | tree pair counting | TreeCorr | `bin_slop` relative to bin size |
| Masked sky maps, C_ℓ of spin-0 and spin-2 fields | pseudo-C_ℓ | NaMaster | pixelisation and band limit, mask treatment, bandpower binning |
| Fields sampled at galaxy positions, C_ℓ without pixelisation | catalogue-based pseudo-C_ℓ | NaMaster (catalogue mode) | random catalogue or continuous selection map |

The last row is recent: a formalism computing C_ℓ directly from field
values at discrete positions, avoiding pixelised maps, aliasing and
finite-resolution effects, now with template deprojection and implemented
in NaMaster (Cornish et al. 2025, arXiv:2510.19912) [src].

### Step 2. FFT power spectra: mesh, assignment, interlacing
<!-- key: step-2-fft-power-spectra-mesh-assignment -->

**Mesh and Nyquist.** With N_G cells per side of a box of side L, cell size
H = L/N_G, the largest wavenumber is k_Nyq = πN_G/L = π/H (Sefusatti et
al. 2016, arXiv:1512.07295, Sect. 2.3) [src]. Aliasing then adds images of
the field shifted by multiples of the sampling frequency k_s = 2k_Nyq:
δ̃^G(k) = Σ_n δ̃(k − n k_s) (Eq. 32) [src: Sect. 3.1].

**Mass assignment.** Particles are assigned to p grid points per dimension
with B-spline weights W^(p): NGP (p = 1), CIC (2), TSC (3), PCS (4)
(Eqs. 15–18); each is a top-hat convolved with itself p − 1 times, and the
separable form makes window correction in Fourier space straightforward
[src: Sect. 2.3]. The gridded field is corrected by dividing by the
window, δ^G(k) = δ̃^G(k)/W(k) [src: Sect. 3.1].

**Interlacing.** A second assignment on a grid shifted by H/2 in all three
directions, averaged with the first, multiplies image n by
θ_n = ½[1 + (−1)^{n_x+n_y+n_z}], removing all odd images including the
dominant |n| = 1 ones (Eq. 35); the interlaced, window-corrected power is
P^G(k) = Σ_n θ_n |w_n(k)|² P_tot(|k − n k_s|) (Eq. 39) [src: Sect. 3.1].
More than two grids would remove the next order [src].

**Shot noise with interlacing.** Interlacing also changes the shot-noise
term: it becomes C^int(k) = Σ_n θ_n |W(k + 2k_N n)|² (Wang & Yu 2024,
arXiv:2403.13561, Sect. 2.3) [src]. Subtracting a constant 1/n̄ instead
(their Eq. 17) biases P(k) beyond the statistical error above
≈ 0.85 k_Nyq for CIC on a 3 h⁻¹ Mpc mesh with number densities
10⁻² to 10⁻⁴ h³ Mpc⁻³; their aliasing-aware form (Eq. 16) keeps the bias
under control to k_Nyq; with TSC both forms stay well below the
statistical error [src: Sect. 4].

**Cost.** For a fixed mesh, FFT time hardly depends on the number of
objects: nbodykit's FFT algorithms took "near-identical time" for 10⁶ and
10⁷ objects on a 1024³ mesh (Hand et al. 2017, arXiv:1712.05834,
Sect. VI) [src]. Survey multipoles with the estimator nbodykit implements
need 2ℓ + 1 FFTs per multipole, 15 for ℓ = 0, 2, 4 [src: Sects. III.4.1,
VI]. Higher-order assignment costs more assignment time but no extra
memory (arXiv:1512.07295, Sect. 5) [src].

### Step 3. Pair counts: exact or approximate, and binning
<!-- key: step-3-pair-counts-exact-or-approximate-and -->

- **Exact counting** is what Corrfunc does; TreeCorr reproduces its counts
  only with `bin_slop` disabled (Sinha et al. 2019, arXiv:1911.03545,
  Sect. 6.5) [src].
- **Tree tolerance.** With `bin_slop` > 0, cell pairs are accepted in a bin
  when their size-to-separation ratio is below `bin_slop` × bin size (the
  criterion is in L2). The effective tolerance therefore depends on the
  binning. KiDS-Legacy measured ξ± in 1000 logarithmic θ-bins between 2′
  and 300′ with TreeCorr 4.2.3 and `bin_slop` = 1.5 (Wright et al. 2025,
  arXiv:2503.19441, Sect. 2.5.1) [src]; the logarithmic bin width is
  ln(150)/1000 ≈ 0.005, so `bin_slop` × bin size ≈ 0.0075
  [der: from the stated range and bin number]. DES Y3 cosmic shear used
  20 logarithmic bins from 2.5′ to 250′ with TreeCorr (Amon et al. 2021,
  arXiv:2105.13543, Sect. VI.1) [src]; its `bin_slop` was not stated in
  the section read.
- **Pixel-based estimator.** DES Y3 lens clustering used a pixelised
  Landy–Szalay form, ŵ(θ) = Σ_ij (N_i − N̄)(N_j − N̄)/N̄² Θ_ij, N_i being
  the galaxy density in HEALPix pixel i corrected for fractional coverage
  and Θ_ij selecting pixel pairs in the θ bin, computed with TreeCorr,
  because its systematics weights are defined per pixel; the difference
  from the random-point estimator was verified negligible on the scales
  used (Rodríguez-Monroy et al. 2021, arXiv:2105.13540, Sect. 5.1, Eq. 6)
  [src].

### Step 4. Pseudo-C_ℓ: resolution, mask, bandpowers
<!-- key: step-4-pseudo-cell-resolution-mask-bandpowers -->

**Resolution and band limit.** The pixel spacing must be smaller than the
shortest wavelength present; smoothing must precede any downgrade, and
masks are applied at the highest resolution before smoothing; power must be
estimated over the whole band, otherwise unconsidered modes inflate the
estimated ones (Alonso et al. 2018, arXiv:1809.09603, App. A.1) [src]. The
HEALPix prescription quoted there: to measure to ℓ_max, use
N_side = ℓ_max/2, estimate bandpowers to 2ℓ_max and discard those above
ℓ_max after pixel-window correction, keeping their covariance contribution
[src]. NaMaster leaves these constraints to the user [src].

**Bandpowers and the theory filter.** The coupled pseudo-C_ℓ are binned with
weights w_q^ℓ (Σ w = 1) and decoupled with the binned coupling matrix
(Eqs. 33–35). The theory must then be passed through the filter
F_qℓ = Σ_q′ (ℳ⁻¹)_qq′ Σ_ℓ′ w_q′^ℓ′ M_ℓ′ℓ (Eq. 37): couple, bin, decouple;
this "can be significantly different from a naïve binning operator"
[src: Sect. 2.1.3].

**Contaminant deprojection.** Template deprojection removes modes and
leaves a deprojection bias (Eq. 44) that depends on the true spectrum; the
paper estimates it iteratively from a first guess rather than through a
modified coupling matrix, which is "significantly more computationally
intensive" [src: Sect. 2.2]. A template must not contain signal (L2). A
transfer function from simple simulations is an alternative that is
insensitive to the guessed spectrum except at ℓ ≲ 3 (arXiv:2510.19912)
[src].

**Purification.** E/B purification needs a mask differentiable to second
order, normally through apodisation; sharp corners can spoil
differentiability even after apodisation, so mask derivatives should be
inspected before purifying (arXiv:1809.09603, Sect. 5) [src]. When
combined with deprojection, contamination coefficients are fitted on the
non-pure maps [src: Sect. 2.3]. The CMB validation used a C² apodisation
with a 10° scale on a 4000 deg² footprint [src: Sect. 4.1.2].

**Noise bias and covariance (shear).** Nicola et al. 2020 derive an exact
analytical noise bias for inhomogeneous shear noise, Eqs. 22 and 24, and
improve the Gaussian covariance's narrow-kernel approximation by using the
mode-coupled signal spectrum (Sect. 2.5.3) (arXiv:2010.09717, Sect. 5)
[src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Assignment order and interlacing
<!-- key: assignment-order-and-interlacing -->

| Set-up | Usable range | Test | Place read |
|---|---|---|---|
| CIC, no interlacing | ≥ 1 % error above about half k_Nyq; 0.1 % only for k ≲ 0.4 k_Nyq | z = 0 N-body, against direct summation | arXiv:1512.07295, Sect. 5 |
| CIC, no interlacing, Zel'dovich field at high z | 1 % (0.1 %) only for k ≲ 0.3 (0.2) k_Nyq | z = 10, 50 | arXiv:1512.07295, Sect. 5 |
| CIC, no interlacing | "percent-level accuracy only up to 0.6 k_Nyq" | same N-body, Fig. 5 | arXiv:1512.07295, Sect. 3.2 |
| TSC or PCS with two interlaced grids | aliasing below 0.1 % for practically all k up to k_Nyq | N-body, ZA and the mean of 1000 ZA realisations against theory | arXiv:1512.07295, Sect. 5 |

The authors' reason for interlacing is efficiency: without it, the usual
remedy is to restrict k, which requires larger grids than naively expected,
a problem worse for higher-order statistics [src: arXiv:1512.07295,
Sect. 5]. Wang & Yu add that raising the assignment order without
interlacing "does not effectively reduce systematic errors" and is not
recommended (arXiv:2403.13561, Sect. 4) [src]. In the cross-spectrum
diagnostic of Fig. 5, the error on the auto-power is about twice that on
the field (cross-power with direct summation) (arXiv:1512.07295, Sect. 3.2)
[src]. For the bispectrum, Sefusatti et al. measured triangles up to
2k_Nyq/3 (Sect. 5, Fig. 9 caption) [src].

### Exact pairs, tree or FFT
<!-- key: exact-pairs-tree-or-fft -->

- FFT cost is set by the mesh, not by N; pair counting scales with the
  number of pairs (arXiv:1712.05834, Sect. VI) [src]. FFT is the tool when
  the mesh can resolve the scales of interest with the set-ups above.
- Exact pair counts are needed where pairwise weights or exact counts
  matter (L2); a tree code with `bin_slop` tuned to the bin width trades a
  bounded misassignment for speed. The KiDS-Legacy set-up keeps the
  product small by using very fine bins and then compressing [der: from
  Sect. 2.5.1 of arXiv:2503.19441, which bins finely "to reduce
  measurement noise and compress the data"].
- Pixel-based correlation functions are natural when weights live on
  pixels, provided the pixel scale is well below the smallest θ used
  (arXiv:2105.13540, Sect. 5.1) [src for the DES choice; der for the
  condition].

### Apodise or not, purify or not
<!-- key: apodise-or-not-purify-or-not -->

- **Cosmic shear (HSC DR1, DES Y1).** No apodisation and no purification:
  the shear spectrum is not steep enough to benefit from apodisation, the
  patchy weight map would lose too much area, and the E mode carries the
  signal (arXiv:2010.09717, Sect. 4.1) [src]. The weight map is used
  directly as the mask [src].
- **Ground-based CMB B modes.** Purification with an apodised mask
  (arXiv:1809.09603, Sects. 2.3, 4.1.2) [src]; without it, B-mode variance
  is dominated by leaked E modes [src: Sect. 2.3].
- **Cost.** Deprojection adds SHTs linear in the number of templates (5
  in the benchmark), purification adds more accurate mask SHTs and
  real-space operations, and the mode-coupling matrix usually costs more
  than one SHT; all scale as ℓ_max³, timings at other resolutions as
  N_side³ (arXiv:1809.09603, App. F) [src].

### Map resolution for shear catalogues
<!-- key: map-resolution-for-shear-catalogues -->

- Restricting estimation to occupied pixels gives multiplicative biases
  scaling with expected pixel occupancy; after modelling, residuals exceed
  1 % above ℓ* ≈ N_side, mostly from aliasing; a finer grid pushes them
  below the pixel scale (Hall & Tessore 2025, arXiv:2501.08718, Sect. 9)
  [src]. Their recommended estimator uses fixed source positions and
  weights, globally normalised shear maps and catalogue-based noise
  subtraction, and is implemented in the Euclid pipeline [src].
- Ignoring the parallel-transport phase in pixel averaging gives an r.m.s.
  multiplicative bias ≈ 10⁻⁴ at Euclid-like depth, within Stage-IV
  requirements for N_side ≥ 128 [src: Sect. 9].
- Interlaced HEALPix grids mitigate aliasing "reasonably well" but depend
  on the input spectrum and catalogue construction; the authors ask for a
  careful study before use on data [src: Sect. 9].
- Stability test used by Nicola et al.: recompute DES spectra at
  N_side = 512, 1024, 2048 (baseline 4096, ∼ 0.86′ pixels) and HSC with
  doubled pixel size; results consistent on the scales used
  (arXiv:2010.09717, Sect. 4.1) [src].

### Map-based or catalogue-based pseudo-C_ℓ
<!-- key: map-based-or-catalogue-based-pseudo-cell -->

Catalogue-based estimation removes pixelisation and aliasing by
construction and, with deprojection, agrees with the map-based result on
real data (arXiv:2510.19912) [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Nyquist wavenumber | k_Nyq = πN_G/L | FFT estimators | arXiv:1512.07295 | Sect. 2.3 |
| CIC, no interlacing, 1 % / 0.1 % range | ≈ 0.5 / 0.4 k_Nyq (N-body); 0.3 / 0.2 k_Nyq (ZA) | test boxes | arXiv:1512.07295 | Sect. 5 |
| TSC/PCS + interlacing | < 0.1 % to k_Nyq | same | arXiv:1512.07295 | Sect. 5 |
| N-body test box | L = 50 h⁻¹ Mpc, 128³ particles; N_G = 100 and 256 | POWMES test | arXiv:1512.07295 | Sect. 3.2 |
| Constant-shot-noise bias with interlacing | exceeds statistical error above ≈ 0.85 k_Nyq (CIC, 3 h⁻¹ Mpc cells) | n̄ = 10⁻² to 10⁻⁴ h³ Mpc⁻³ | arXiv:2403.13561 | Sect. 4 |
| FFT benchmark | P(k, μ) and P_ℓ (ℓ = 0, 2, 4; 15 FFTs) on 1024³ for 10⁶ and 10⁷ objects | NERSC Cori, 32 ranks per node | arXiv:1712.05834 | Sect. VI |
| KiDS-Legacy ξ± binning | 1000 log bins, 2′–300′, `bin_slop` = 1.5 (TreeCorr 4.2.3) | cosmic shear | arXiv:2503.19441 | Sect. 2.5.1 |
| DES Y3 ξ± binning | 20 log bins, 2.5′–250′ | cosmic shear | arXiv:2105.13543 | Sect. VI.1 |
| HEALPix band-limit rule | N_side = ℓ_max/2; bandpowers to 2ℓ_max, keep ≤ ℓ_max | pseudo-C_ℓ | arXiv:1809.09603 (quoting Leistedt et al. 2013) | App. A.1 |
| DES Y1 shear maps | N_side = 4096; bandpowers used only for ℓ < 2N_side = 8192; linear to ℓ = 240 then logarithmic | NaMaster curved sky | arXiv:2010.09717 | Sect. 4.1, Table 2 |
| HSC DR1 shear maps | 0.5′ flat-sky pixels, 24-pixel masked buffer, piecewise-linear bandpowers 100–15 800 | NaMaster flat sky | arXiv:2010.09717 | Sect. 4.1, Table 2 |
| Pixelisation residual | > 1 % above ℓ* ≈ N_side after modelling | shear catalogues | arXiv:2501.08718 | Sect. 9 |
| Parallel-transport bias | r.m.s. ≈ 10⁻⁴; fine for N_side ≥ 128 | Euclid-like depth | arXiv:2501.08718 | Sect. 9 |
| NaMaster scaling | ℓ_max³; N_side³ for timings | Cori Haswell, 32 threads | arXiv:1809.09603 | App. F |
| B-mode validation mask | C² apodisation, 10°, 4000 deg² | ground CMB | arXiv:1809.09603 | Sect. 4.1.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Aliasing read as signal near the Nyquist scale.** CIC without
  interlacing at k ≳ 0.5 k_Nyq (arXiv:1512.07295, Sect. 5) [src]. Test:
  repeat on a finer mesh or with interlacing; results must not move.
- **Shot noise subtracted as 1/n̄ after interlacing.** Bias above
  ≈ 0.85 k_Nyq with CIC (arXiv:2403.13561, Sect. 4) [src]. Test: measure
  the noise on a Poisson random catalogue with the same set-up (their
  Fig. 1 does this).
- **Window not corrected, or corrected twice.** The grid field must be
  divided by W(k) once (arXiv:1512.07295, Sect. 3.1) [src]. Test: power of
  a Poisson random catalogue should be flat after shot-noise subtraction.
- **Tree counts treated as exact.** `bin_slop` > 0 with coarse bins
  (arXiv:1911.03545, Sect. 6.5; L2) [src]. Test: halve `bin_slop`, or set
  it to zero on a subsample, and compare.
- **Theory binned naively.** Bandpowers compared with a plain average of
  C_ℓ instead of the filter of Eq. 37 (arXiv:1809.09603, Sect. 2.1.3)
  [src]. Test: pass a smooth input spectrum through the full filter and
  through plain binning; the difference is the error.
- **Truncated band.** Estimating C_ℓ only to the ℓ of interest inflates
  power (arXiv:1809.09603, App. A.1) [src]. Test: extend the band and
  check stability of the kept bandpowers.
- **Mask applied after degrading, or degrading before smoothing.** Same
  appendix [src]. healpy's `ud_grade` warning is in L2.
- **Purification on a non-differentiable mask.** Sharp mask corners
  (arXiv:1809.09603, Sect. 5) [src]. Test: inspect first and second mask
  derivatives.
- **Deprojection bias left in.** Iterate the bias estimate or use a
  transfer function (arXiv:1809.09603, Sect. 2.2; arXiv:2510.19912)
  [src]. Test: simulations with and without templates.
- **Shear map pixel occupancy bias.** Occupied-pixel restriction with low
  occupancy (arXiv:2501.08718, Sect. 9) [src]. Test: resolution series as
  in arXiv:2010.09717, Sect. 4.1.
- **Null spectra.** B modes and PSF cross-spectra; Nicola et al. run these
  in Sect. 4.3 and App. B of arXiv:2010.09717 (sections not read here).

## Reading list
<!-- key: reading-list -->

- Foundation and method: Sefusatti et al. 2015, arXiv:1512.07295 —
  aliasing images, B-spline assignment, interlacing, usable k ranges.
- Test: Wang & Yu 2024, arXiv:2403.13561 — shot noise under interlacing,
  bias near Nyquist.
- Code: Hand et al. 2017, arXiv:1712.05834 — nbodykit meshes, FFT
  multipole cost, benchmarks.
- Code: Alonso et al. 2018, arXiv:1809.09603 — pseudo-C_ℓ, bandpowers
  and filter, deprojection bias, purification, band limits, cost.
- Application: Nicola et al. 2020, arXiv:2010.09717 — shear pseudo-C_ℓ
  with NaMaster on HSC and DES: bandpowers, no apodisation, noise bias.
- Critique: Hall & Tessore 2025, arXiv:2501.08718 — pixelisation biases
  of map-based shear spectra and the recommended estimator.
- Method: Cornish et al. 2025, arXiv:2510.19912 — catalogue-based
  pseudo-C_ℓ with deprojection in NaMaster.
- Application: Wright et al. 2025, arXiv:2503.19441 and
  Rodríguez-Monroy et al. 2021, arXiv:2105.13540 — TreeCorr settings and a
  pixel-based w(θ) in survey analyses.
- Code: Sinha et al. 2019, arXiv:1911.03545 — exact pair counting
  (summarised in L2).

## Not verified
<!-- key: not-verified -->

- No paper comparing pypower with nbodykit on the same catalogue was
  found; pypower has no code paper (L2).
- DES Y3 `bin_slop` values were not found in the sections read.
- Leistedt et al. 2013 (HEALPix band-limit prescription) and the first
  catalogue-based pseudo-C_ℓ paper (cited by arXiv:2510.19912) were not
  read; no identifiers recorded.
- Hand et al. 2017b (the FFT multipole estimator nbodykit implements) was
  cited through arXiv:1712.05834, not read.
- Numerical timings of NaMaster tasks (App. F, Fig. 17) are in a figure,
  not transcribed.
- A 2026 paper on analytical covariances for catalogue-based pseudo-C_ℓ
  was seen by title in a search only; not read, not cited.
