# Physics and methods — statistics beyond the two-point function

Scope: definitions, estimators, theory models, covariance, blinding and codes for the bispectrum and trispectrum, cosmic voids, density-split and other alternative clustering statistics, higher-order lensing statistics, field-level inference and simulation-based inference.
Snapshot: 2026-10-13

Status lines use three levels: data, blinded or mock-validated; data, not
blind; simulations only. The full status table is `results.md` §0.

## 1. Bispectrum, trispectrum and N-point functions
<!-- key: bispectrum-trispectrum-and-n-point-functions -->

### 1.1 Definitions
<!-- key: definitions -->

The bispectrum is the Fourier-space three-point function,
⟨δ(k1) δ(k2) δ(k3)⟩ = (2π)³ δ_D(k1 + k2 + k3) B(k1, k2, k3); the trispectrum T
is the connected four-point analogue. In redshift space B depends on the
triangle shape and on two angles to the line of sight, and is expanded in
multipoles (monopole, quadrupole, hexadecapole). A Gaussian field has B = 0 and
T = 0; gravity, non-linear galaxy bias and primordial non-Gaussianity all
generate them. The practical value of B is that it separates quantities which
the power spectrum measures only as products: b1, b2, f and σ8 (Gil-Marín et
al. 2014, arXiv:1407.5668), and that it is the large-scale-structure probe of
the non-local (equilateral, orthogonal) shapes of f_NL (Chudaykin, Ivanov &
Philcox 2025, arXiv:2512.04266).

Founding papers (abstracts read):

| Step | What the paper established | Reference |
|---|---|---|
| Shape dependence as the signature of gravity | Tree-level perturbation theory fixes how B depends on triangle shape; departures in galaxy catalogues are read as bias. One-loop corrections computed and compared with N-body; the reduced bispectrum loses its shape dependence in the strongly non-linear regime | Scoccimarro et al. 1997, arXiv:astro-ph/9704075 |
| Bias from the bispectrum | Second-order perturbation theory and a likelihood for B lift the degeneracy between b and Ω_0 left by β = Ω_0^0.6/b; the covariance of B needs the six-point function | Matarrese, Verde & Heavens 1997, arXiv:astro-ph/9706059 |
| Redshift space | Perturbative multipole expansion of the redshift-space bispectrum plus a phenomenological model for the non-linear transition; the hierarchical model does not hold in redshift space | Scoccimarro, Couchman & Frieman 1998, arXiv:astro-ph/9808305 |
| From theory to a survey | Survey geometry and sparse sampling correlate triangles and break the Gaussian-likelihood approximation; likelihood built on bispectrum eigenmodes from mock surveys | Scoccimarro 2000, arXiv:astro-ph/0004086 |
| First survey measurements | IRAS QDOT, 2 Jy and 1.2 Jy at 0.05 < k < 0.2 h Mpc⁻¹ (Scoccimarro et al. 2000, arXiv:astro-ph/0004087); 2dFGRS at 0.1 < k < 0.5 h Mpc⁻¹: b_1 = 1.04 ± 0.11, b_2 = −0.054 ± 0.08, Ω_m = 0.27 ± 0.06 at z = 0.17 [src] | Verde et al. 2001, arXiv:astro-ph/0112161 |
| Information content with P | Joint P + B covariance including beat coupling; amplitude and effective spectral index improve by almost a factor of two (**forecast**) | Sefusatti et al. 2006, arXiv:astro-ph/0604505 |

Review of perturbation theory, estimators and their errors: Bernardeau et al.
2001 (arXiv:astro-ph/0112551).

### 1.2 Estimators in use
<!-- key: estimators-in-use -->

| Estimator | What it does | Reference |
|---|---|---|
| Binned-triangle estimator of the bispectrum monopole | Number of triangles limited by the number of mocks | arXiv:1407.5668; Gil-Marín et al. 2016, arXiv:1606.00439 |
| FFT-based estimators with a radial line of sight | Power-spectrum and bispectrum multipoles (ℓ = 0, 2, 4) from FFTs of overdensity multipoles for a survey geometry; for BOSS about fifteen minutes on one core for B_ℓ of all triangles up to k = 0.2 h Mpc⁻¹ [src], which is what makes covariances from many mocks affordable | Scoccimarro 2015, arXiv:1506.02729 |
| Interlaced grids and high-order mass assignment | Interlacing removes the odd aliasing images; with fourth-order interpolation the bias on P and B is below 0.01% up to the Nyquist frequency [src] | Sefusatti et al. 2015, arXiv:1512.07295 |
| 3PCF multipoles in O(N²) | Spherical-harmonic expansion around each galaxy, no triplet counting; exact in angle, with edge correction | Slepian & Eisenstein 2015, arXiv:1506.02040 |
| Linear compression (MOPED) | M linear combinations of the data keep the Fisher information on M parameters when the noise does not depend on them; the idea behind the compressions below | Heavens, Jimenez & Lahav 1999, arXiv:astro-ph/9911102 |
| Maximal (Karhunen–Loève) and geometrical compression | Raises the usable triangle count from 116 to 2734 [src] on BOSS CMASS | Gualdi et al. 2018, arXiv:1806.02853; Gualdi et al. 2019, arXiv:1901.00987 |
| Window-free (quasi-optimal, maximum-likelihood) estimators | Deconvolve the survey window in the measurement, so the theory is not window-convolved; extended to ℓ = 2, 4 multipoles | Philcox & Ivanov 2021, arXiv:2112.04515; Ivanov et al. 2023, arXiv:2302.04414 |
| Tripolar spherical harmonic (TripoSH) decomposition | Introduced by Sugiyama et al. 2018 (arXiv:1803.02132): zero-total-angular-momentum expansion, measurable with FFTs, with a simple window correction; L > 0 modes arise only from RSD or AP; 14σ detection of the L = 2 mode in BOSS DR12 [src]. Window convolution becomes a linear transformation of theory multipoles | Guandalin et al. 2026, arXiv:2610.01836 |
| ShapeFit compression of P + B0 | Compress to α_iso, α_AP, fσ_s8, m+n, then infer cosmology; mitigates prior-volume effects | Novell-Masot et al. 2025, arXiv:2503.09714; Novell-Masot et al. 2026, arXiv:2603.19356 |
| Trispectrum as a test of Gaussianity | Connected four-point function in Fourier space, weak non-linear growth; a statistic τ independent of cosmology, power spectrum and (linear) bias in real space | Verde & Heavens 2001, arXiv:astro-ph/0101143 |
| Integrated trispectrum with P and B | Monopole and quadrupoles of P, B and i-trispectrum of the redshift-space *matter* field: 68% regions smaller by 72%, 78%, 72%, 47%, 46% on (f, σ8, f_nl, α_∥, α_⊥) than P_0,2 + B_0, for 25 (h⁻¹Gpc)³, n = 5 × 10⁻⁴ h³Mpc⁻³, z = 0.5 [src]; simulations only | Gualdi, Gil-Marín & Verde 2021, arXiv:2104.03976 |
| Isotropic N-point basis and the O(N_g²) estimator | Basis of rotation-invariant functions from spherical harmonics and Clebsch–Gordan coefficients (Cahn & Slepian 2020, arXiv:2010.14418); NPCFs by pair counting, 3PCF to 6PCF of a BOSS-like survey in about 100 CPU-hours [src] | Philcox et al. 2021 (ENCORE), arXiv:2105.08722 |
| Connected (parity-even) 4PCF | Disconnected part subtracted at the estimator level; compression to about 100 basis vectors; 8.1σ in BOSS CMASS, 4.7σ once tetrahedron sides below 14 h⁻¹Mpc are excluded [src] | Philcox, Hou & Slepian 2021, arXiv:2108.01670 |
| Isotropic-basis 4PCF, parity-odd modes | Lowest-order statistic sensitive to scalar parity violation; the test was proposed by Cahn, Slepian & Hou 2021 (arXiv:2110.12004) | Hou, Slepian & Cahn 2022, arXiv:2206.03625; Philcox 2022, arXiv:2206.04227 |
| Kurto spectra (composite-field spectra P_2×2, P_3×1) | Compress the parity-odd trispectrum to a low-dimensional vector so that the covariance can come directly from mocks | Gao et al. 2026, arXiv:2604.06021 |

### 1.3 Theory models
<!-- key: theory-models -->

- **Tree-level EFT bispectrum with one-loop power spectrum.** Used for DESI
  DR1 in arXiv:2610.01836; arXiv:2206.08327 describes its own earlier BOSS
  analysis in the same terms. The window-free BOSS analyses are
  arXiv:2112.04515 and arXiv:2302.04414. The model (galaxy bias, IR
  resummation, non-linear RSD, binning and projection effects) was validated
  on the PT Challenge simulations, 566 h⁻³Gpc³, as valid up to
  k_max = 0.08 h Mpc⁻¹ at z = 0.61, with a gain of 5–15% over P on those
  simulations and an estimated 10% on σ8 at BOSS volume [src] (Ivanov et al.
  2021, arXiv:2110.10161).
- **One-loop EFT bispectrum.** For matter, the counterterms were derived by
  Baldauf et al. 2014 (arXiv:1406.4135; three new operators, agreement with
  N-body to k ≈ 0.22 h Mpc⁻¹ at z = 0 [src]) and Angulo et al. 2014
  (arXiv:1406.4143). For the redshift-space galaxy monopole, Philcox et al.
  2022 (arXiv:2206.02800) find that the one-loop terms extend the scale range
  and tighten the bias parameters but bring no noticeable gain on σ8, because
  of the marginalisation over many nuisance parameters with conservative
  priors. First applied to BOSS by D'Amico et al. 2022
  (arXiv:2206.08327): one-loop for the power spectrum and bispectrum monopole,
  tree level for the bispectrum quadrupole. A systematic power-counting
  derivation and a fast implementation (COBRA) are in Bakx et al. 2025
  (arXiv:2507.22110); the one-loop model is used for the DESI DR1 f_NL
  analysis (arXiv:2512.04266).
- **Hybrid EFT + phenomenological model (FolpsD).** An extension of the FOLPS
  code that combines its one-loop EFT power spectrum with a bispectrum model
  mixing EFT and phenomenological ingredients, exploiting small-scale P and
  large-scale B (Bansal et al. 2026, arXiv:2604.08895).
- **Tree-level EFT trispectrum.** Developed and validated on 25 AbacusSummit
  boxes of total volume 200 h⁻³Gpc³ [src] by Tucci & Philcox 2026
  (arXiv:2610.08908), with k_max up to 0.12 h Mpc⁻¹ [src] depending on tracer.
  The abstract states that no full-shape trispectrum analysis yet exists.
- **Simulation-based priors (EFT-SBP).** EFT nuisance parameters receive priors
  learned from HOD simulations; used with P + B in Chen & Ivanov 2025
  (arXiv:2507.00118) and in the DESI + BOSS f_NL combination of
  arXiv:2512.04266. Whether these priors are safe is disputed; see
  `open-questions.md` §1.

### 1.4 Covariance and likelihood
<!-- key: covariance-and-likelihood -->

The bispectrum data vector is long, so the number of mocks sets the binning:
with 2048 MultiDark-Patchy mocks BOSS analyses kept about 116 triangles before
compression (arXiv:1806.02853). DESI DR1 P + B analyses take the cross-covariance
between P, B and post-reconstruction BAO from mocks (Forero-Sánchez et al.
2026, arXiv:2606.23936). For four-point statistics the covariance is the
dominant risk: the parity-odd 4PCF significance depends on which mocks supply
the noise model (see `systematics.md` §1.3). The parity-odd analyses use
ℓ ≤ 4 and 10 radial bins over 20–160 h⁻¹Mpc (1288 bins), or 18 bins of
8 h⁻¹Mpc over 20–164 h⁻¹Mpc, with an analytic Gaussian-field covariance whose
effective number density and volume are fitted to the mocks, and either a
direct χ² or a projection on N_eig eigenmodes with a T² distribution
[src: Sect. 5.1.3, 5.1.4 of arXiv:2206.03625; Sect. I of arXiv:2401.09523;
Sect. IV of arXiv:2508.09133]. The analytic covariance takes P + 1/n̄ as
input and neglects the higher-order correlations.

### 1.6 What the main analyses did
<!-- key: what-the-main-analyses-did -->
<!-- TABLE-ANCHOR-1.6 -->

Read in the method sections; the place is given in each cell.

| Analysis | Data vector and scales | Model and free parameters | Covariance and likelihood | Gain over the two-point analysis, as stated |
|---|---|---|---|---|
| DESI DR1 LRG ×3 + QSO, collaboration (arXiv:2503.09714) | P_0,2,4 (LRG) or P_0,2 (QSO) at k < 0.15 h Mpc⁻¹, 13 bins per multipole; B_0 at 0.02 < k < 0.12 h Mpc⁻¹, Δk = 0.01, 150 triangles; largest vector 189 elements [src: Sect. 3.2–3.4] | ShapeFit compression (α_iso, α_AP, f, σ_s8, m+n). Bispectrum: GEO-FPT, a tree-level SPT form with P_L replaced by P_NL and the Z_2 kernel multiplied by a geometric factor with five coefficients calibrated on N-body and held fixed [src: Eqs. 8–10]. Nuisance: b_1, b_2, A_P, A_B (prior N(1, 0.3²)), σ_P, σ_B; b_s² and b_3nl at local-Lagrangian values [src: Table 2, Sect. 4.3]. Window applied only to the P_NL factor of the monopole [src: Sect. 3.3] | 1000 EZmocks per bin, Hartlap factor about 0.8, Sellentin–Heavens likelihood [src: Sect. 3.4, Eq. 12]; amplitude rescaled by the factors derived for the power spectrum. Catalogue-level blinding, choices frozen before unblinding [src: Sect. 2] | Against the DESI ShapeFit power-spectrum results, averaged over the four bins: errors smaller by about 10% on α_AP, 20% on fσ_s8, 30% on m+n, and about 5% larger on α_iso [src: Sect. 5.1] |
| DESI DR1, six tracers, independent pipeline (arXiv:2507.13433) | P_0,2,4 and B_0 from window-deconvolved quasi-optimal estimators (PolyBin3D); B_0 at 0.02 ≤ k < 0.08 h Mpc⁻¹, 49 data points per chunk [src: Sect. IV.4] | One-loop EFT P; B = B^tree + B^ct + B^stoch with IR-resummed linear spectrum and a k² counterterm for fingers of God [src: Eq. 55]. Sampled: H_0, ω_c, ln(10¹⁰A_s), ω_b and n_s under Gaussian priors, and b_1σ8, b_2σ8², b_G2σ8² per chunk; the other EFT parameters marginalised analytically with Gaussian priors [src: Table 3] | Gaussian analytic covariance with the mask; P–B cross-covariance and the DR2-BAO correlation neglected [src: Sect. VIII]. Windowed and unwindowed estimators give nearly identical constraints [src: Sect. VII.3] | B_0 tightens ω_cdm, Ω_m and σ8 by 11%, 8% and 10%, moves Ω_m up by 0.8σ and leaves H_0 unchanged, because k_max = 0.08 holds no BAO information [src: Sect. VI.1] |
| DESI DR1 LRG ×3 + QSO, TripoSH pipeline (arXiv:2610.01836) | P_0, P_2 and B_000 to k_max = 0.20 h Mpc⁻¹ for all tracers; B measured with Triumvirate on diagonal configurations k_1 = k_2 only, Δk = 0.005; B_202 tested on LRG1 at k_max = 0.08 and dropped as uninformative [src: Sect. 3.2, 6, 6.2] | One-loop EFT P, tree-level B, emulated; nuisance parameters reparametrised as ψ × amplitude (for example b_1σ8√A_AP) against projection effects [src: Sect. 5.1.2]; window applied to B as a matrix in the TripoSH basis, tested on 25 altMTL mocks [src: App. A.2] | 1000 EZmocks with fast fibre assignment; no θ-cut for B [src: Sect. 4.2, 3.2] | Error change when adding B_000, LRG1 / LRG2 / LRG3 / QSO / LRG combined / all: ln(10¹⁰A_s) −8, −14, −20, −13, −10, −4%; σ8 −2, −12, −14, +1, −5, −1% [src: Table 3]. Single-tracer gains shrink in combination because the power spectra of several tracers already break the bias degeneracies [src: Sect. 6.2] |
| DESI DR1 full shape + DR2 BAO, collaboration (arXiv:2606.23936) | Bispectrum for the three LRG bins only: P_0,2,4 at 0.02–0.15 and B_0 at 0.02–0.12 h Mpc⁻¹, Δk = 0.01. Other tracers and the power-spectrum-only baseline: P_0,2 at 0.02–0.20, Δk = 0.005 [src: Sect. 3.2] | ShapeFit parameters from arXiv:2503.09714 (RPT power spectrum, GEO-FPT bispectrum, co-evolution bias relations), then cosmology from the compressed parameters [src: Sect. 3.2] | P–B cross-covariance from mocks; BAO × ShapeFit correlation from 100 mocks in compressed space, variances from the data posteriors; dropping that block shifts σ8 by 0.44σ [src: Sect. 3.4, 4.1] | σ8 = 0.868 ± 0.025, S8 = 0.880 ± 0.026 with BBN and a wide n_s prior; errors 26.5% and 27.8% smaller and values 1.1σ and 1.2σ higher than the power-spectrum-only combination; h, Ω_m unchanged [src: Sect. 4.2.1, Eq. 18]. The baseline differs in multipoles, scale cuts and binning, so the figure is not the gain at fixed P data vector, a point made by arXiv:2610.01836 [src: Sect. 6.2] |
| BOSS DR12, window-free P + B_0 (arXiv:2112.04515) | Unwindowed quadratic and cubic estimators [src: Sect. III, Eqs. 3–4]; P_ℓ to k = 0.2, the real-space proxy Q_0 to 0.4, B_0 at 0.01–0.08 h Mpc⁻¹ with Δk = 0.01, 62 triangle bins [src: Sect. III, Table 2] | One-loop EFT P, tree-level B; h, ln(10¹⁰A_s), ω_cdm, ω_b, n_s varied, Σm_ν fixed to 0.06 eV; linear nuisance parameters marginalised analytically [src: Sect. IV.3] | 2048 Patchy mocks (999 when BAO parameters are included), Hartlap factor, Gaussian likelihood [src: Eqs. 14–15]. Validation on the mean of 84 Nseries mocks with the covariance scaled to 6 and to 235 h⁻³Gpc³ [src: Sect. V] | 13% on σ8 (abstract) |
| BOSS DR12, one-loop B_0 + tree-level B_2 (arXiv:2206.08327) | FKP P_0,2 with 42 (36) k-bins; B_0 with 150 (62) triangle bins of width 0.0215 (0.0246) h Mpc⁻¹, centres from 0.0215 (0.029) to 0.215 (0.176), for CMASS (LOWZ); B_2 adds 9 bins [src: Sect. 2] | One-loop EFT for P and B_0, tree level for B_2; ω_cdm, h, ln(10¹⁰A_s) free, BBN prior on ω_b, n_s fixed; a linear prior on Ω_m, h, b_1 added against projection effects [src: Sect. 4]. Window: tree-level bispectrum evaluated with the windowed linear spectrum, no window on the loop [src: Eq. 18] | 2048 Patchy mocks, bin width chosen to keep the Hartlap factor at about 0.91 (0.95) [src: Sect. 2]. Scale cut checked by adding next-order counterterms [src: Sect. 5.2] | 30%, 18%, 13% on σ8, h, Ω_m (abstract) |

### 1.5 Status
<!-- key: status-5 -->

Bispectrum (monopole, tree level or one loop): **data, mock-validated**, in
BOSS and DESI DR1, including inside the DESI collaboration. Trispectrum full
shape: **simulations only**. Parity-odd 4PCF: **data, measured, no accepted
detection**.

## 2. Cosmic voids
<!-- key: cosmic-voids -->

Reviews: Pisani et al. 2019 (arXiv:1903.05161); the void chapter of Moresco et
al. 2022 (arXiv:2201.07241).

### 2.1 Void finders
<!-- key: void-finders -->

A void catalogue is defined by its finder; statistics from different finders
are not interchangeable.

| Finder | Principle | Reference |
|---|---|---|
| VoidFinder (maximal spheres) | Based on the algorithm of El-Ad & Piran; recovers the full volume of near-spherical voids, less for elongated ones; 35 voids above 20 h⁻¹Mpc diameter in PSCz [src] | Hoyle & Vogeley 2001, arXiv:astro-ph/0109357 |
| Watershed Void Finder (WVF) | Watershed transform of the density field, with corrections for sampling noise; no assumption on scale or shape | Platen, van de Weygaert & Jones 2007, arXiv:0706.2788 |
| ZOBOV | Voronoi tessellation density estimate plus watershed; no free parameter, no shape assumption | Neyrinck 2008, arXiv:0712.3049 |
| VIDE | Toolkit built on ZOBOV for surveys and simulations | Sutter et al. 2015, arXiv:1406.1191 |
| REVOLVER, voxel, Pylians3 spherical finder | Three further packages, compared with VIDE in the AP-response study | Radinović et al. 2024, arXiv:2407.02699 |
| VoidFinder, V² | Two algorithms, the second with REVOLVER or VIDE pruning; used for the DESI BGS catalogue | Rincon et al. 2024, arXiv:2411.00148 |
| Spherical-overdensity finder on a Lyα tomographic map | Finder calibrated on hydrodynamical simulations of the intergalactic medium | Krolewski et al. 2018, arXiv:1710.02612 |
| Back-in-time void finder | Dynamical identification after optimal-transport reconstruction | Sartori et al. 2026, arXiv:2601.15378 |

The first systematic comparison ran thirteen finders on one subvolume of the
Millennium simulation: they agree on the main void and on centres below 10% of
the mean density (Colberg et al. 2008, arXiv:0803.0918). The average density
profile of watershed voids follows a two-parameter empirical function,
universal in size and redshift, with a linear-theory velocity profile derived
from it (Hamaus, Sutter & Wandelt 2014, arXiv:1403.5499).

### 2.2 Void size function (VSF)
<!-- key: void-size-function-vsf -->

The VSF is the comoving number density of voids per unit radius. The models in
use descend from the excursion-set model of Sheth & van de Weygaert 2003
(arXiv:astro-ph/0311260), a two-barrier problem: one barrier for voids in
voids, one for voids in clouds, which are squeezed out and give the small-size
cut-off. Jennings, Li & Hu 2013 (arXiv:1304.6087) define voids as spheres of
ρ_v = 0.2 ρ_m, use δ_v = −2.7, and find that this model greatly overpredicts
the abundance in N-body simulations, while a volume-conserving version (Vdn)
matches it within 16% for 1 < r < 15 h⁻¹Mpc [src]; voids in halos are fewer
below 10 h⁻¹Mpc and more numerous above than in the matter. Current
analyses use the volume-conserving (Vdn) modification, extended with nuisance
parameters tied to the large-scale galaxy bias and calibrated on mocks
(Contarini et al. 2022, arXiv:2205.11525; Contarini et al. 2023,
arXiv:2212.03873). An alternative BOSS DR16 analysis fits the linear
underdensity threshold δ_v and an RSD parameter B directly (Song et al. 2025,
arXiv:2501.07817). Void counts are treated as Poisson distributed; this was
checked on simulations by Thiele et al. 2023 (arXiv:2307.07555).

### 2.3 Void–galaxy cross-correlation: AP and RSD
<!-- key: void-galaxy-cross-correlation-ap-and-rsd -->

The observable is the anisotropic cross-correlation ξ_vg(s, μ) between void
centres and galaxies, compressed to multipoles. Two physical inputs:

- **Geometry.** A stack of voids is spherically symmetric in real space if the
  Universe is statistically isotropic, so its apparent ellipticity under a
  fiducial cosmology measures D_M/D_H (the Alcock–Paczynski test).
- **Dynamics.** In linear theory mass conservation gives the mean radial
  outflow v_r(r) = −(1/3) f a H r Δ(r), where Δ(r) is the mean matter density
  contrast inside r. The redshift-space quadrupole therefore measures the
  growth rate, quoted as β = f/b or as fσ8 depending on the analysis.

Founding papers (abstracts read):

| Step | Content | Reference |
|---|---|---|
| AP test on voids | Voids are elongated in redshift space unless q_0 = −1; proposes their axis ratio and volume against redshift as a measure of q_0, citing Alcock & Paczyński 1979 (doi:10.1038/281358a0; confirmed on Crossref, not read) for the principle [sec]; two-dimensional toy model without peculiar velocities | Ryden 1995, arXiv:astro-ph/9506028 |
| Stacked voids | AP test on the mean sphericity of voids stacked in redshift shells; **forecast** that Euclid stacked voids outperform BAO by an order of magnitude in the dark-energy figure of merit | Lavaux & Wandelt 2011, arXiv:1110.0345 |
| Void outflows in simulations | Outflow velocities peaking further out for larger voids; void–tracer cross-correlation in ξ(σ, π) elongated along the line of sight | Padilla, Ceccarelli & Lambas 2005, arXiv:astro-ph/0508297 |
| Void–galaxy RSD on data | Parametric linear model of the redshift-space cross-correlation applied to SDSS; large voids expand, small voids with overdense shells collapse | Paz et al. 2013, arXiv:1306.5799 |
| Joint AP + RSD model | Linear theory describes void dynamics; modelling peculiar velocities reduces the AP systematic from about 15% to about 5%; **forecast** σ(f/b)/(f/b) ≈ 2% (20%) and σ(D_A H)/D_A H ≈ 0.2% (2%) for SDSS MAIN-like (CMASS-like) densities in 1 h⁻³Gpc³, at which level the linear model is systematics-dominated [src] | Hamaus et al. 2015, arXiv:1507.04363 |
| Multipole estimator | In linear theory ξ_vh has only a monopole and a quadrupole; β from their ratio without knowing the void profile, to 9% in 3 (h⁻¹Gpc)³ with voids above 25 h⁻¹Mpc [src]; voids can look elongated or flattened, which complicates the AP test | Cai et al. 2016, arXiv:1603.05184 |
| First SDSS constraint | ε = 1.003 ± 0.012, Ω_m = 0.281 ± 0.031, f/b = 0.417 ± 0.089 at z̄ = 0.57, with an additional systematic uncertainty of half the statistical one [src] | Hamaus et al. 2016, arXiv:1602.01784 |
| Linear model valid inside the void | Terms neglected before change the sign of the quadrupole inside the void radius; with a velocity dispersion, fits BOSS-CMASS-like mocks over 0 ≤ s ≤ 120 h⁻¹Mpc; f(z = 0.52) to 2.7% in (2.5 h⁻¹Gpc)³ [src]; the linear-bias approximation does not hold within voids | Nadathur & Percival 2017, arXiv:1712.07575 |
| Reconstruction before void finding | The assumptions of the models fail for voids found in redshift space; Zeldovich reconstruction restores them, at the cost of repeating the reconstruction for every tested model; growth rate to 3.4% in the same volume [src] | Nadathur, Carter & Percival 2018, arXiv:1805.09349 |

Two modelling schools exist:

1. **Deprojection, no calibration** (Hamaus et al. 2020, arXiv:2007.07895):
   the real-space profile is inferred from the data by tomographic
   deprojection; the model is linear and has two nuisance parameters;
   optionally calibrated on mocks.
2. **Reconstruction before void finding** (Nadathur et al. 2019,
   arXiv:1904.01030; Nadathur et al. 2020, arXiv:2008.06060; Woodfinden et al.
   2022, arXiv:2205.06258): large-scale RSD are removed from the galaxy field
   with a velocity reconstruction before voids are identified, so that void
   centres carry no RSD-induced selection bias.

What the reference analysis did (arXiv:2205.06258). Reconstruction, then
the ZOBOV-based watershed finder of REVOLVER on the RSD-removed field, on the
combined LOWZ + CMASS sample [src: Sect. 3.2]. Data vector: monopole and
quadrupole of ξ^s; the hexadecapole adds little at current precision. Four
parameters: fσ8, β, α_⊥/α_∥ and a velocity dispersion σ_v; the measured data
vector itself depends on β through the reconstruction, so it is recomputed
across the chain [src: Sect. 3.6]. Covariance from 1000 MGS or Patchy mocks,
fixed with cosmology, with the Percival et al. (2021) posterior
[src: Eqs. 18–22].

Convention trap: arXiv:1904.01030 quotes D_A H/c = 0.4367 at z = 0.57 with D_A
the angular diameter distance, while arXiv:2007.07895 quotes D_A H/c = 0.588 at
z = 0.51 with D_A the *comoving* angular diameter distance. They differ by a
factor (1 + z): 0.4367 × 1.57 = 0.686 [der, assuming the first is the proper
distance]. From 2020 the reconstruction school quotes D_M/D_H.

### 2.4 Void lensing
<!-- key: void-lensing -->

The stacked tangential shear or CMB-lensing convergence around voids measures
the matter profile and hence tests the bias and the mock predictions (Martin
et al. 2025, arXiv:2507.13450; Sartori et al. 2024, arXiv:2412.02761). It has
produced detections and amplitude tests, not cosmological parameters.

### 2.5 Voids in Lyα tomography and the void–forest cross-correlation
<!-- key: voids-in-lyalpha-tomography-and-the-void-forest -->

A tomographic map is a Wiener-filter interpolation of the Lyα flux contrast
between neighbouring sightlines; its resolution is set by the mean transverse
sightline separation. Two regimes exist. Dense galaxy-plus-quasar backgrounds
give about 2–2.5 h⁻¹Mpc over a fraction of a square degree (CLAMATO:
arXiv:1710.02612; Horowitz et al. 2022, arXiv:2109.09660). Quasar-only surveys
give 13 h⁻¹Mpc over 220 deg² at a sightline density of 37 deg⁻² [src]
(arXiv:2004.01448), which also provides a void and protocluster catalogue
from the map.

The void–forest cross-correlation of Ravoux et al. 2022 (arXiv:2203.11045)
correlates void centres from the map with the Lyα flux contrast along the
sightlines. Its quadrupole is fitted with a linear RSD model that includes the
"tomographic effect" of the data lying along parallel lines of sight. The
fitted parameter is the RSD parameter β of the forest around voids. It is not
f/b: the forest β involves the velocity-gradient bias (see
`cosmo-lyman-alpha`), so turning it into a growth-rate measurement requires a
model of that bias. Thesis summary: Ravoux 2022, arXiv:2203.07886.

### 2.6 Voids with simulation-based inference
<!-- key: voids-with-simulation-based-inference -->

Thiele et al. 2023 (arXiv:2307.07555) combine the VSF, the void–galaxy cross
power spectrum and the galaxy power spectrum of BOSS CMASS NGC in an implicit
likelihood analysis with HOD-populated approximate simulations including
particle neutrinos.

### 2.7 Status
<!-- key: status-4 -->

Void–galaxy AP/RSD: **data, mock-validated** (SDSS MGS, BOSS, eBOSS); the
abstracts read this session do not report a blinded analysis, and no DESI
void–galaxy cosmology was found. VSF: **data, with a mock-calibrated model**.
Void lensing: **data, detection level**. Lyα–void: **data, first detection
compared to simulations**, RSD parameter only.

## 3. Alternative clustering statistics: density split, kNN, wavelets, Minkowski functionals, marks
<!-- key: alternative-clustering-statistics-density-split -->

These statistics have no perturbative model on the scales where they gain
information. All data applications so far use **simulation-based emulators**:
N-body boxes at many cosmologies, populated with a halo occupation
distribution (HOD), with the statistic emulated by a neural network over
cosmology and HOD parameters. The cosmological result is therefore conditional
on the simulation suite and on the galaxy–halo model.

| Statistic | Definition | Model in use | Reference |
|---|---|---|---|
| Density-split clustering (DSC) | Rank random query points by the smoothed local galaxy density, split into quantiles, and measure the quantile–galaxy cross-correlation and quantile auto-correlation multipoles | SUNBIRD neural emulator on AbacusSummit HOD mocks, sub-percent accuracy down to 1 h⁻¹Mpc [src] | Cuesta-Lazaro et al. 2023, arXiv:2309.16539; Paillas et al. 2023, arXiv:2309.16541 |
| k-nearest-neighbour CDFs (kNN) | Empirical cumulative distribution of distances from volume-filling random points to the k-th nearest data point; sensitive to all connected N-point functions; contains counts-in-cells and the void probability function | AbacusSummit emulator (in the Beyond-2pt challenge) | Banerjee & Abel 2021, arXiv:2007.13342; Banerjee & Abel 2021, arXiv:2102.01184 |
| Wavelet scattering transform (WST) | Moduli of successive wavelet convolutions of the density field, spatially averaged; a fixed-kernel analogue of a convolutional network | AbacusSummit HOD emulator, or SimBIG forward model | Valogiannis & Dvorkin 2022, arXiv:2204.13717; Valogiannis, Yuan & Dvorkin 2024, arXiv:2310.16116; Régaldo-Saint Blancard et al. 2024, arXiv:2310.15250 |
| Minkowski functionals (MFs) | Volume, surface area, mean curvature and Euler characteristic of excursion sets of the smoothed field as functions of threshold | Hermite expansion on large scales (perturbatively non-Gaussian regime); neural emulator on AbacusSummit HOD mocks for the full information | Appleby et al. 2022, arXiv:2110.06109; Liu et al. 2025, arXiv:2501.01698 |
| Marked power spectrum | Power spectrum of the field weighted by a function ("mark") of the local density; up-weighting low density enhances neutrino sensitivity | One-loop perturbation theory; non-perturbative at z = 0 for small smoothing scales | Massara et al. 2021, arXiv:2001.11024; Philcox, Massara & Spergel 2020, arXiv:2006.10055 |
| Galaxy multiplets | Small groups of nearby galaxies treated as objects and cross-correlated with the galaxy field | Comparison with AbacusSummit HOD mocks | Wang et al. 2025, arXiv:2511.15354 |
| Compressed Lyα forest bispectrum | Three-point statistic of the 3D forest, compressed | proposed estimator; see `cosmo-lyman-alpha` for the forest itself | de Belsunce, Sullivan & McDonald 2025, arXiv:2510.23597 |

Where each statistic comes from (abstracts read):

| Statistic | Founding or first-application paper | What it established |
|---|---|---|
| Density split, projected | Friedrich et al. 2017, arXiv:1710.05162; Gruen et al. 2017, arXiv:1710.05045 | Sky split into areas of distinct foreground galaxy density; lensing and counts-in-cells in each, with a perturbation-theory model. DES Y1 + SDSS: Ω_m = 0.26 +0.04/−0.03 or 0.28 +0.05/−0.04 for two stochasticity models; σ8 model dependent (0.97 +0.07/−0.06 or 0.80 +0.06/−0.07) [src] |
| Density split, redshift space | Paillas et al. 2021, arXiv:2101.09854 | Velocities are nearly Gaussian in each density quantile, so the Gaussian streaming model holds; on mocks of (1.5 h⁻¹Gpc)³ with s_min = 15 h⁻¹Mpc, fσ12 improves by about 30% and the AP parameters by about a factor 6 over the 2PCF [src] |
| Scattering transform | Mallat 2011, arXiv:1101.2286; Bruna & Mallat 2012, arXiv:1203.1513 | Cascade of wavelet-modulus operators, translation invariant and stable to deformations; expected values depend on high-order moments and separate processes with the same power spectrum |
| Scattering transform in cosmology | Cheng et al. 2020, arXiv:2006.08561; Valogiannis & Dvorkin 2021, arXiv:2108.07821 | On simulated lensing maps it matches a CNN without training; on the Quijote 3D matter field, Fisher errors 1.2–4 times tighter than P(k) on six parameters [src] (matter field, periodic box) |
| Wavelet phase harmonics | Allys et al. 2020, arXiv:2006.06298 | Low-dimensional statistics of 2D non-Gaussian fields; Fisher errors tighter than P + B for four of five parameters on projected Quijote fields; also generative |
| Minkowski functionals | Mecke, Buchert & Wagner 1993, arXiv:astro-ph/9312028; Schmalzing & Buchert 1997, arXiv:astro-ph/9702130 | Complete family of morphological measures including the Euler characteristic, first for point sets (Abell clusters), then for isodensity contours of a smoothed field, with the genus as one member |
| MFs in perturbation theory and on data | Matsubara 2000, arXiv:astro-ph/0006269; Hikage et al. 2003, arXiv:astro-ph/0304455 | Second-order formulae for genus, level crossings and MFs of smoothed fields, with bias; first SDSS measurement (154 287 galaxies), consistent with ΛCDM mocks |
| Marked statistics | Beisbart & Kerscher 2000, arXiv:astro-ph/0003358; Sheth 2005, arXiv:astro-ph/0511772 | Marked point processes and mark-weighted correlation functions for luminosity and morphology segregation; halo-model description of marked correlations |
| Density-dependent mark for cosmology | White 2016, arXiv:1609.08632 | A density-marked correlation function as a generic test of screened modified gravity, studied at low order in perturbation theory; the marked power spectrum of arXiv:2001.11024 uses a mark of this family |

Information-content studies use the Quijote suite: 44 100 N-body simulations
over more than 7 000 cosmologies in boxes of 1 h⁻¹Gpc [src]
(Villaescusa-Navarro et al. 2020, arXiv:1909.05273). A Fisher forecast from
Quijote is an upper bound for matter or halos in a periodic box; it is not a
survey forecast.

Covariance: from mocks at fixed cosmology (for example 1 500 mocks for DSC in
the Beyond-2pt challenge), with an emulator-error term added (table in
arXiv:2405.02252, Krause et al. 2024).

What the BOSS density-split analysis did (arXiv:2309.16541). Galaxies and
randoms are painted on a grid, δ = G/R − 1, smoothed with a Gaussian of
R_s = 10 h⁻¹Mpc and sampled at query points taken from the random catalogue,
five times the number of galaxies, split into five quintiles [src: Sect.
2.2.2, Eq. 7]. Fitted range 1 < s < 150 h⁻¹Mpc [src: Sect. 4.4.3]. The
covariance is a sum, C = C_data + C_emu + C_sim: 2048 Patchy mocks for the
sample variance, 600 test simulations for the emulator error, 1800
AbacusSummit realisations for the frozen phase of the training boxes, with
the Percival et al. factor on the mock terms [src: Eqs. 15–20]. h is not
free: the training suite fixes 100θ_* = 1.041533, so h and Ω_m are derived,
with ω_ν fixed at 60 meV; ω_b has a BBN prior [src: Sect. 3.5, Eqs. 21–22].
Gain on the data at fixed pipeline: σ8 = 0.792 ± 0.034 with DSC against
0.807 +0.055/−0.049 from the 2PCF alone, ω_cdm ± 0.0022 against ± 0.0034,
n_s ± 0.018 against +0.043/−0.026 [src: Table 3], that is about 1.5 on σ8
and ω_cdm, below the emulator forecast of 1.9 and 2.9 in arXiv:2309.16539
[der: ratios of the quoted errors]. The errors stop shrinking below
s_min ≈ 20 h⁻¹Mpc because the emulator-error term then dominates the
monopoles [src: Sect. 4.4.2].

The Minkowski-functional analysis (arXiv:2501.01698) follows the same
design. The four functionals are the volume fraction W_0, the surface area
W_1, the integrated mean curvature W_2 and the integrated Gaussian curvature
W_3 of the excursion set E_ν = {x : u(x) ≥ ν}, each normalised by the volume
[src: Eqs. 7–8]; for a weakly non-Gaussian field their amplitude is set by
σ_1/σ_0 and the first correction by three skewness parameters times σ_0
[src: Eq. 9], which is why the earlier amplitude-only analysis
(arXiv:2110.06109) carried Gaussian information only. Smallest smoothing
scale 15 h⁻¹Mpc at n̄ = 2.4 × 10⁻⁴ h³Mpc⁻³ [src: Sect. 6.3]. Covariance
C_data + C_emu + C_abacus from 2048 Patchy mocks, 2512 test mocks and 1786
small AbacusSummit boxes; Gaussian likelihood, checked [src: Sect. 3.6,
Eq. 14]. Stated gain of the MFs over the 2PCF multipoles: 2.0, 1.4, 1.7 on
h, n_s, σ8, against 1.9, 2.0, 1.3 in the authors' earlier Fisher forecast
with the power spectrum as baseline [src: Sect. 6.3].

Status. DSC, WST, MFs: **data (BOSS CMASS only), mock-validated, emulator-
and HOD-dependent**. kNN, marked power spectrum: **simulations and mock
challenge only**; no cosmological constraint from survey data was found this
session. Multiplets: **data (DESI DR2 LRG), used for the galaxy–halo
connection, not cosmology**.

## 4. Higher-order weak-lensing statistics
<!-- key: higher-order-weak-lensing-statistics -->

Two-point lensing (ξ±, COSEBIs, pseudo-Cℓ, shear and redshift calibration) is
in `cosmo-weak-lensing`. This section covers what is added on top.

### 4.1 Statistics
<!-- key: statistics -->

| Statistic | Definition | Modelling | Data applications read this session |
|---|---|---|---|
| Third-order aperture mass ⟨M_ap³⟩ | Skewness of the shear field filtered with a compensated aperture; a compression of the shear three-point function | Conventional likelihood; joint covariance from simulated shear maps | DES Y3 (Gomes et al. 2025, arXiv:2508.14018); HSC Y3 (Sugiyama, Gomes & Jain 2025, arXiv:2508.14019); KiDS-Legacy (Linke et al. 2026, arXiv:2606.12389) |
| Moments of the convergence map | Second and third moments of smoothed mass maps | Validated on simulations; simulation-based inference in the 2024 analysis | DES Y3 (Gatti et al. 2022, arXiv:2110.10141; validation in Gatti et al. 2020, arXiv:1911.05568) |
| Peak (and minimum) counts | Number of local maxima (minima) of the aperture-mass or convergence signal-to-noise map as a function of height | N-body simulations | KiDS-450 (Martinet et al. 2018, arXiv:1709.07678); HSC Y1 tomographic peaks (Liu et al. 2023, arXiv:2210.07853); DES Y3 (Jeffrey et al. 2025, arXiv:2403.02314) |
| One-point PDF | Histogram of the smoothed convergence | Simulations | HSC Y1 (Novaes et al. 2025, arXiv:2409.01301) |
| Minkowski functionals | Area, perimeter and genus of excursion sets of the convergence map | Simulations | HSC Y1 (Armijo et al. 2025, arXiv:2410.00401; arXiv:2409.01301) |
| Scattering transform, wavelet phase harmonics | Moduli of iterated wavelet convolutions; phase couplings between scales | Simulations | HSC Y1 (Cheng et al. 2025, arXiv:2404.16085); DES Y3 (Gatti et al. 2024, arXiv:2310.17557; Gatti et al. 2025, arXiv:2405.10881) |
| Persistent homology (Betti numbers) | Birth and death of connected components and holes across thresholds, on the sphere | Simulations | DES Y3 (Prat et al. 2025, arXiv:2506.13439) |
| Map-level neural compression | A convolutional network compresses the tomographic maps to a few numbers | Simulations | KiDS-450 and KiDS-1000 (Fluri et al. 2019, arXiv:1906.03156; Fluri et al. 2022, arXiv:2201.07771); HSC Y1 (Lu, Haiman & Li 2023, arXiv:2301.01354); DES Y3 (arXiv:2403.02314; Williamson et al. 2026, arXiv:2606.11309) |
| Peak steepness | Profile slope of lensing peaks, sensitive to halo profiles and feedback | Simulations | HSC Y1 (Li et al. 2026, arXiv:2608.24591) |

Founding papers (abstracts read):

| Statistic | Reference | Content |
|---|---|---|
| Aperture mass | Schneider 1996, arXiv:astro-ph/9601039; Schneider et al. 1997, arXiv:astro-ph/9708143 | Weighted mass in a circular aperture from the image distortions, used to detect halos as signal-to-noise peaks; ⟨M_ap²⟩ as a localised probe of the projected power spectrum and the third moment as a skewness independent of the power-spectrum normalisation |
| Peak counts | Jain & Van Waerbeke 1999, arXiv:astro-ph/9910459; Kratochvil, Haiman & May 2009, arXiv:0907.0486; Dietrich & Hartlap 2009, arXiv:0906.3512 | Peak distribution as a probe of the halo mass function and of Ω; most of the sensitivity comes from low peaks (κ ≈ 0.03) that are not single halos; a "peak function" from N-body simulations in the Ω_m–σ8 plane, competitive with and complementary to shear tomography |
| Skewness of the convergence | Bernardeau, Van Waerbeke & Mellier 1996, arXiv:astro-ph/9609122 | In the quasi-linear regime the variance scales as P(k) Ω_0^1.5 z_s^1.5 and the skewness as Ω_0^−0.8 z_s^−1.35: used jointly they separate Ω_0 from the amplitude; the strong dependence on source redshift is flagged as the practical concern |
| Shear three-point function | Schneider & Lombardi 2002, arXiv:astro-ph/0207454; Schneider, Kilbinger & Lombardi 2003, arXiv:astro-ph/0308328 | Four complex "natural components" that only pick up a phase under rotation; their relation to the convergence bispectrum, E/B separation, and generalised third-order aperture measures with several filter scales that hold essentially all the bispectrum information |
| ⟨M_ap³⟩ from the three-point function | Jarvis, Bernstein & Jain 2003, arXiv:astro-ph/0307393 | Skewness and kurtosis of the aperture mass insensitive to masks and variable depth, with a tree code for the three-point function; 2σ skewness in the CTIO survey |
| Bispectrum tomography | Takada & Jain 2003, arXiv:astro-ph/0310125 | **Forecast**, 50 < ℓ < 3000, three redshift bins: bispectrum constraints comparable to the power spectrum, a factor three better combined |
| First 2+3-point data analysis | Fu et al. 2014, arXiv:1404.5469 | CFHTLenS: third moment at 2σ; σ8(Ω_m/0.27)^α improved by 10% over second order; tested for source–lens clustering, IA and baryons [src] |
| Modern ⟨M_ap³⟩ pipeline | Heydenreich et al. 2022, arXiv:2208.11686 | Γ^(i) and ⟨M_ap³⟩ from the BiHalofit bispectrum, validated on N-body; on KiDS-1000-like mocks the joint analysis almost doubles the power on S8 and multiplies the Ω_m–σ8 figure of merit by 5.9 [src] (mock, not data) |
| Convergence PDF from theory | Barthelemy et al. 2019, arXiv:1909.02615; Boyle et al. 2020, arXiv:2012.07771 | Large-deviation prediction of the convergence PDF, within 5% in the tails at z_s = 1 and 10′, percent level with nulling; validated against simulations with Σm_ν and w; **forecast** for Euclid-like area better than the 2PCF on M_ν and w0 with a Planck prior |
| Convergence PDF from simulations | Liu & Madhavacheril 2018, arXiv:1809.10747 | **Forecast**, LSST-like, MassiveNuS: the tomographic PDF alone outperforms the power spectrum on M_ν; combining them tightens it by a further 35% |
| First data applications of peaks | Liu et al. 2014, arXiv:1412.0757; Kacprzak et al. 2016, arXiv:1603.05040 | CFHTLenS, 154 deg², emulator on 91 cosmologies accurate to ≤ 5%: peaks + power spectrum halve the area of the (Ω_m, σ8) contour, σ8(Ω_m/0.27)^0.63 = 0.85 ± 0.03 [src]. DES SV, 139 deg², 158 models: σ8(Ω_m/0.3)^0.6 = 0.77 ± 0.07, peaks with S/N > 4 excluded because of IA, blending and cluster-member contamination [src] |

### 4.2 Inference practice
<!-- key: inference-practice -->

The ⟨M_ap³⟩ analyses use a conventional likelihood. The other statistics take
their model from simulations, as an emulator or, in the DES Y3 2024–2026
series and the HSC Y1 combined analysis (arXiv:2409.01301), by
**simulation-based inference**: a suite of N-body lensing
simulations spanning cosmology is turned into mock surveys with the mask,
shape noise, shear calibration, photometric-redshift uncertainty, intrinsic
alignments and source clustering applied; the statistic is compressed by a
neural network; and a neural density estimator gives the likelihood or
posterior. The DES Y3 implementation rests on the Gower Street suite, 791
full-sky PKDGRAV simulations from which more than 3 000 mock DES data sets are
built [src] (arXiv:2403.02314). Validation is by coverage tests and by
contaminating the test vector with baryonic feedback (arXiv:2606.11309,
arXiv:2506.13439).

The DES Y3 "hybrid" analysis compresses the maps to seven summaries, combining
the power spectrum with neural summaries built to add information beyond it
(arXiv:2606.11309).

### 4.3 Status
<!-- key: status-3 -->

Higher-order lensing is the most mature beyond-two-point family on data:
**survey data, collaboration analyses, systematics forward-modelled, validated
by coverage and feedback tests**, for DES Y3, KiDS-Legacy and HSC. Blinding
status is not stated in the abstracts read; check each paper. A combined
lensing-plus-clustering map-level pipeline exists as an analysis design for
DES Y3 (Thomsen et al. 2025, arXiv:2511.04681); its cosmological result was
not found.

## 5. Field-level inference
<!-- key: field-level-inference -->

### 5.1 Three things called "field-level"
<!-- key: three-things-called-field-level -->

The term covers three different methods. A text that does not say which one
it means cannot be checked.

1. **Forward-model inference with sampled initial conditions.** The joint
   posterior P(θ, δ_ini | d) ∝ L(d | F[δ_ini, θ]) P(δ_ini | θ) P(θ) is sampled,
   where F is a structure-formation model plus bias, selection and noise, and
   δ_ini has as many dimensions as the grid (10⁶ or more). Hamiltonian Monte
   Carlo is the standard sampler. This is the only form that accesses all
   non-Gaussian information on the scales modelled.
2. **Gaussian field-level likelihood.** The observed field values (velocities,
   densities) are the data vector of a multivariate Gaussian whose covariance
   is computed from a model power spectrum; no initial conditions are sampled.
   It is optimal for a Gaussian field and uses two-point information only;
   nuisance parameters of the field are fitted with the cosmology. This is
   what `flip` implements, with wide-angle covariance models; the paper
   presents it as the foundation for a non-linear extension (Ravoux et al.
   2025, arXiv:2501.16852). See `cosmo-peculiar-velocities`.
3. **Neural field-level methods.** A network takes the gridded field and
   returns either compressed summaries for simulation-based inference (SimBIG,
   Lemos et al. 2024, arXiv:2310.15256) or a reconstructed linear field (LiFT,
   Parker et al. 2026, arXiv:2609.14862). The information extracted is whatever
   the network learned from the training simulations.

Founding papers of the first meaning (abstracts read, except where stated):

| Step | Content | Reference |
|---|---|---|
| Bayesian reconstruction as an inverse problem | Wiener filter and its relatives unified for a linear data model (ARGO); outlines Gibbs sampling of density, velocity and power spectrum | Kitaura & Enßlin 2007, arXiv:0705.0429 |
| Hamiltonian sampling of the density | HMC on a lognormal-Poisson posterior with survey geometry and selection; shows non-Gaussian sampling is feasible in high dimension | Jasche & Kitaura 2009, arXiv:0911.2496 |
| Sampling the initial conditions | BORG (arXiv:1203.3639). In the same period: Gibbs steps with a Gaussianisation by Hamiltonian sampling and second-order LPT, initial conditions unbiased down to about 5 h⁻¹Mpc on a mock (Kitaura 2012, arXiv:1203.4184); Hamiltonian MCMC with a Gaussian prior, phases recovered to k ≈ 1 h Mpc⁻¹ on a mock SDSS DR7 (Wang et al. 2013, arXiv:1301.1348) | — |
| Marginalising the modes | Likelihood expanded around the maximum-posterior linear modes; a nearly optimal estimator of the initial power spectrum for a fixed forward model, found by optimisation, not sampling | Seljak et al. 2017, arXiv:1706.06645 |
| EFT likelihood | A field-level likelihood under perturbative control once small-scale modes are integrated out; its information equals next-to-leading-order P + leading-order B + BAO reconstruction; first unbiased σ8 from simulated halos | Schmidt et al. 2018, arXiv:1808.02002 |

As written for a perturbative forward model with Gaussian noise of power
P_err (arXiv:2509.09673, Eq. 38), the marginal posterior is
P[θ | δ̂_g] ∝ ∫Dδ exp(−½ ∫_k^{k_max} |δ̂_g(k) − δ_g(k; θ)|²/P_err(k))
× exp(−½ ∫_k^Λ |δ(k)|²/P_lin(k; θ)): a Gaussian likelihood up to k_max times
the Gaussian prior on the initial modes up to a cut-off Λ. That analysis
samples θ and δ jointly with NUTS in NumPyro [src: Sect. III.2.3].

The sampler is Hybrid (Hamiltonian) Monte Carlo, Duane et al. 1987
(doi:10.1016/0370-2693%2887%2991197-X, the parentheses of the DOI written
percent-encoded; title, authors and year confirmed on Crossref, paper not
read). The statement of arXiv:1808.02002 that the EFT
likelihood carries the information of P at next-to-leading order, B at
leading order and reconstruction is the theoretical root of "Side B" in
`open-questions.md` §5.1.

### 5.2 Forward-model families
<!-- key: forward-model-families -->

| Family | Gravity model | Tracer model | Applied to | Reference |
|---|---|---|---|---|
| BORG | second-order Lagrangian perturbation theory | galaxy bias, survey mask and selection function | SDSS DR7-like mocks; valid above about 6 h⁻¹Mpc [src] | Jasche & Wandelt 2013, arXiv:1203.3639 |
| BORG with particle mesh | particle-mesh N-body inside the sampler | hierarchical bias and selection parameters, block sampling + HMC | 2M++ | Jasche & Lavaux 2019, arXiv:1806.11117 |
| BORG on deep surveys | physical structure-formation model (LPT for Quaia) with light-cone effects and RSD | bias, selection and foreground corrections | SDSS-III/BOSS; Quaia quasars | Lavaux, Jasche & Leclercq 2019, arXiv:1909.06396; Andrews et al. 2026, arXiv:2602.02363 |
| Manticore-Local | non-linear gravity solver, physics-informed priors | refined bias model | 2M++; yields a posterior ensemble of constrained simulations ("digital twin") | McAlpine et al. 2025, arXiv:2505.10682 |
| LEFTfield | Lagrangian EFT forward model | EFT bias expansion with noise parameters | simulated halos; Beyond-2pt real-space mock | Nguyen et al. 2024, arXiv:2403.03220 |
| Perturbative forward model, Gaussian likelihood | perturbation theory | EFT bias, Gaussian noise with constant power | mock data from the same model | Akitsu et al. 2025, arXiv:2509.09673; Spezzati, Marinucci & Simonović 2025, arXiv:2507.05378 |
| BORG-WL | gravity model of the BORG-WL framework | TATT or NLA alignments, enthalpy-gradient-descent baryons | synthetic shear data only | Porqueres et al. 2023, arXiv:2304.04785 |
| BORG for f_NL^loc | structure-formation model and resolution varied as tests | bias + initial conditions + f_NL sampled jointly | Quijote halo catalogues, k_max ≈ 0.1 h Mpc⁻¹ | Andrews et al. 2026, arXiv:2603.20855 |

### 5.3 What the outputs are
<!-- key: what-the-outputs-are -->

The BORG runs on data read here deliver **fields** (initial conditions,
density, velocity, with posterior uncertainty) and quote no cosmological
parameter. In the 2M++ run the cosmology is fixed (Ω_m = 0.307, σ8 = 0.8288,
h = 0.705): a 677.77 h⁻¹Mpc box with 256³ nodes, about 1.6 × 10⁷ sampled
amplitudes at 2.65 h⁻¹Mpc Lagrangian resolution, 512³ particle-mesh
particles per step, started from 6783 LPT transitions [src: Sect. 4.2 of
arXiv:1806.11117]; the Poisson likelihood is raised to a power 0 ≤ β ≤ 1
("robust" likelihood) against model misspecification [src: Sect. 3.5,
Eq. 24]. EFT-type runs vary σ8 or A, ω_cdm, H0 and deliver **parameter
posteriors**, so far on simulations.

### 5.4 Status
<!-- key: status-2 -->

Forward-model inference: **reconstructions from survey data (2M++, BOSS,
Quaia); cosmological parameters from simulations only**; no parameter
constraint from survey data was found this session. Neural field-level:
**survey data** (BOSS CMASS subsample, DESI DR1 LRG BAO), validated on mocks
with changed forward models, outside collaboration pipelines. Gaussian
field-level likelihood: **survey data, collaboration result** for fσ8 from
DESI DR1 peculiar velocities (`cosmo-peculiar-velocities`).

## 6. Simulation-based inference with learned summaries
<!-- key: simulation-based-inference-with-learned -->

### 6.1 Method
<!-- key: method -->

Simulation-based (implicit-likelihood, likelihood-free) inference replaces the
analytic likelihood by a neural density estimator, usually a normalising flow,
trained on pairs of parameters and simulated data vectors. The data vector is
a set of summary statistics, optionally compressed by a second network, or the
output of a convolutional network applied to the field. Three checks are
standard: simulation-based calibration (posterior coverage on held-out
simulations), a test set built with a *different* forward model, and
stability under changes of the density-estimator architecture
(arXiv:2211.00660, arXiv:2310.15250).

Founding papers (abstracts read):

| Ingredient | Content | Reference |
|---|---|---|
| Review | The field of simulation-based inference and why it gained momentum | Cranmer, Brehmer & Louppe 2019, arXiv:1911.01429 |
| Approximate Bayesian Computation | Accept simulations within a distance of the data in summary space; population Monte Carlo implementation applied to image-simulation calibration | Akeret et al. 2015, arXiv:1504.07245 |
| Conditional density estimation | Learn a parametric posterior from simulations, with no ε-ball; earlier inferences guide later simulations | Papamakarios & Murray 2016, arXiv:1605.06376 |
| Score compression | Compression of N data to n numbers, n the number of parameters, through the gradient of the log-likelihood; keeps the Fisher information and generalises Karhunen–Loève and MOPED compression (arXiv:astro-ph/9911102) | Alsing & Wandelt 2017, arXiv:1712.00012 |
| DELFI in cosmology | Compression to one number per parameter, then a density model for the joint distribution of data and parameters; about 10⁴ simulations for the JLA supernova test case [src] | Alsing, Wandelt & Feeney 2018, arXiv:1801.01497 |
| Neural density estimators with active learning | Likelihood learned by neural density estimators, simulations acquired where they matter; O(10³) simulations for typical problems [src]; public code pydelfi | Alsing et al. 2019, arXiv:1903.00007 |
| Learned compression | Networks trained to maximise Fisher information (IMNN) give near-sufficient non-linear summaries | Charnock, Lavaux & Wandelt 2018, arXiv:1802.03537 |
| Networks on the 3D field | 3D convolutional networks on dark-matter simulations estimate parameters as well as, or better than, the summary-based estimates compared | Ravanbakhsh et al. 2017, arXiv:1711.02033 |
| Calibration tests | Simulation-based calibration: rank statistics of posterior samples over the prior predictive (Talts et al. 2018, arXiv:1804.06788); TARP coverage for generative estimators, needing samples only (Lemos et al. 2023, arXiv:2302.03026) | — |

### 6.2 SimBIG
<!-- key: simbig -->

SimBIG forward-models the BOSS CMASS sample from Quijote N-body simulations
and a flexible halo occupation model with survey geometry and fibre collisions
(arXiv:2211.00660). The published analyses use a CMASS subsample that spans
about 10% of the full BOSS volume [src] (Hahn et al.
2024, arXiv:2310.15246), to k_max = 0.5 h Mpc⁻¹. Statistics analysed: power
spectrum multipoles, bispectrum monopole (Hahn et al. 2024, arXiv:2310.15243),
CNN field-level summary (arXiv:2310.15256), wavelet scattering transform
(arXiv:2310.15250), marked power spectrum (Massara et al. 2024,
arXiv:2404.04228).

Read in the SimBIG papers. Training set: the 2000 Quijote Latin-hypercube
simulations, each populated with 10 HOD draws, 20 000 catalogues with survey
geometry and fibre collisions [src: Sect. III.4 of arXiv:2211.00660]. Test
sets: TEST0, 500 catalogues from the same forward model at the fiducial
cosmology; TEST1, 500 with friends-of-friends halos and a simpler HOD
without assembly, concentration or satellite velocity bias; TEST2, 1000 from
AbacusSummit with CompaSO halos and the full HOD [src: Sect. IV of
arXiv:2211.00660; Sect. III.4 of arXiv:2310.15243]. Bispectrum: FFT
estimator on a 360³ grid in a (1800 h⁻¹Mpc)³ box, Δk = 0.0105 h Mpc⁻¹ (three
fundamental modes), 10 052 triangles to k_max = 0.5 h Mpc⁻¹, used as the
reduced bispectrum Q_0 = B_0/(P_0P_0 + 2 perm.) [src: Sect. III.3, Eq. 1 of
arXiv:2310.15243]; no covariance matrix enters, since the density estimator
learns the posterior from the 20 000 catalogues. Fibre collisions are in
the forward model, so no collision weights are applied to the data; angular
systematic and redshift-failure weights are [src: Sect. III.3].

### 6.3 Status
<!-- key: status -->

**Survey data (BOSS CMASS subsample), mock challenge with changed forward
models passed for some statistics and failed for others; no collaboration
blinding.**

## 7. Blinding, codes and conventions
<!-- key: blinding-codes-and-conventions -->

### 7.1 Blinding and validation practice
<!-- key: blinding-and-validation-practice -->

- Parameter-masked mock challenge: Beyond-2pt (arXiv:2405.02252), described in
  `surveys-and-data.md` §6. It blinds the *truth of a mock*, not survey data.
- Blinding read in paper bodies (2026-10-13). DESI DR1 collaboration P + B:
  catalogue-level blinding of the BAO position, of f and of f_NL, analysis
  choices frozen first; the f_NL blinding shifts m+n [src: Sect. 2 of
  arXiv:2503.09714]. KiDS-Legacy third order: three data vectors, the true
  one and two shifted in (σ8, Ω_m), with the key held outside the team
  [src: Sect. 4.2 of arXiv:2606.12389]. DES Y3 hybrid SBI: pipeline trained
  and validated on simulations only, posterior means hidden until
  unblinding; two post-unblinding changes are reported [src: Sect. 7.4, 7.5
  of arXiv:2606.11309]. DES Y3 2+3-point: shifted ellipticities in the
  catalogue and hidden parameter values [src: Sect. V.2 of
  arXiv:2508.14018]. The independent DESI reanalyses work on public,
  unblinded catalogues.
- Blind tests on data stated in the abstracts read: the BOSS parity-odd 4PCF
  rank test (arXiv:2206.04227). For every other data result in this skill the
  abstract does not state whether the data analysis was blinded; the
  collaboration analyses (DESI bispectrum, DES Y3 and KiDS-Legacy lensing)
  are expected to follow the survey blinding schemes described in
  `cosmo-galaxy-clustering` and `cosmo-weak-lensing`; this was not checked
  per paper.
- Changed-forward-model test sets: SimBIG (arXiv:2211.00660), LiFT
  (arXiv:2609.14862), MFs with non-HOD mocks (arXiv:2501.01698).
- Large-volume recovery tests: 84 times the CMASS volume for density split
  (arXiv:2309.16541); 200 h⁻³Gpc³ for the trispectrum (arXiv:2610.08908).

### 7.2 Codes and public products named in the papers read
<!-- key: codes-and-public-products-named-in-the-papers -->

| Code or product | Purpose | Reference |
|---|---|---|
| flip | Gaussian field-level likelihood for velocity and density fields, Fisher forecasts | arXiv:2501.16852 |
| BORG | Bayesian reconstruction of initial conditions | arXiv:1203.3639, arXiv:1806.11117 |
| LEFTfield | Lagrangian EFT forward model for field-level inference | arXiv:2403.03220 |
| FolpsD, COBRA | Fast P + B models for DESI | arXiv:2604.08895, arXiv:2507.22110 |
| SUNBIRD | Density-split emulator, public on GitHub [src] | arXiv:2309.16539 |
| ZOBOV, VIDE, VoidFinder, V², REVOLVER | Void finders | arXiv:0712.3049, arXiv:1406.1191, arXiv:2411.00148, arXiv:2407.02699 |
| TopoS2 | Persistent homology on the sphere | arXiv:2506.13439 |
| Quijote, Gower Street, SimBIG mocks, Beyond-2pt mocks | Simulation suites and challenge data | arXiv:1909.05273, arXiv:2403.02314, arXiv:2211.00660, arXiv:2405.02252 |

### 7.3 Conventions that cause errors
<!-- key: conventions-that-cause-errors -->

- **D_A H/c against D_M/D_H** in void papers: proper or comoving D_A (§2.3).
- **β** means f/b for galaxies around voids, and the forest RSD parameter in
  the void–forest correlation; neither is fσ8.
- **S8** is σ8 (Ω_m/0.3)^0.5 in every lensing paper cited here; always state
  ΛCDM or wCDM with the value.
- **k_max** is in h Mpc⁻¹. The perturbative trispectrum and field-level
  analyses read here stop at 0.10–0.12. For the bispectrum the cut depends on
  the model and the triangles kept: 0.08 for the tree-level EFT monopole
  (arXiv:2110.10161, arXiv:2507.13433), 0.12 for the N-body-calibrated
  GEO-FPT kernel (arXiv:2503.09714), 0.20 for diagonal TripoSH
  configurations (arXiv:2610.01836); see §1.6. SimBIG quotes 0.5;
  emulators quote 1 h⁻¹Mpc in configuration space.
- **"Field-level"** has three meanings (§5.1).
- **"Gain"** must name its baseline: the same pipeline's two-point analysis,
  a perturbative analysis, or a Fisher forecast.
