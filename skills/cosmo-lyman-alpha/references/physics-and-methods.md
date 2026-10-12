# Lyman-alpha forest — physics, observables, estimators and models

Scope: what the forest measures and why it constrains cosmology; the delta field; the 1D and 3D two-point statistics and their estimators; the theory models and simulations in current use; covariance, likelihood and blinding practice; codes; conventions and units.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper (abstract unless a section is named); `[der]` derived here; `[sec]` secondary. Equations given without a flag are definitions.

## 1. What is measured

### 1.1 Transmission and the Gunn–Peterson optical depth

Neutral hydrogen along the line of sight to a background source absorbs at rest-frame Lyα (1215.67 Å), so absorption at observed wavelength λ maps to an absorber redshift 1 + z = λ / λ_α. The transmitted flux fraction is F = exp(−τ). The optical depth of a smooth, uniformly expanding medium was derived by Gunn & Peterson 1965 (doi:10.1086/148444); the absence of a complete trough in quasar spectra shows that the IGM is highly ionised, and the residual, fluctuating absorption is the forest. Reviews: Rauch 1998 (arXiv:astro-ph/9806286), Weinberg et al. 2003 (arXiv:astro-ph/0301186), Meiksin 2009 (arXiv:0711.3358), McQuinn 2016 (arXiv:1512.00086); for machine-learning methods across the field, Chaves-Montero 2026 (arXiv:2605.22489).

McQuinn's summary of the status is the right prior for a reader: models of the IGM at 2 < z < 5 are "a tremendous success, quantitatively explaining the statistics of Lyman-alpha absorption", while lower and higher redshifts are less understood (arXiv:1512.00086) [src].

### 1.2 The fluctuating Gunn–Peterson approximation (FGPA)

In photo-ionisation equilibrium the neutral density scales as n_HI ∝ n_H² α(T) / Γ_HI, with the recombination coefficient α(T) ∝ T^−0.7 approximately. Low-density photo-heated gas follows a power-law temperature–density relation

    T = T_0 Δ^(γ − 1),   Δ = ρ / ρ̄

shown by Hui & Gnedin 1997 to hold for Δ < 5 after uniform reionisation, with an asymptotic T_0 ∝ (Ω_b h / sqrt(Ω_0))^(1/1.7) for early reionisation and a slope confined to a narrow range (arXiv:astro-ph/9612232) [src]. Combining the two gives the local optical depth

    τ ∝ Δ^(2 − 0.7(γ − 1)) / Γ_HI      (before redshift-space effects)

to which peculiar-velocity gradients and thermal broadening are applied along the line of sight. This "tight correlation between the Lyα optical depth and the underlying matter density" is what makes the forest a tracer of the density field (Croft et al. 1998, arXiv:astro-ph/9708018) [src]. The FGPA is the engine of every fast mock: Gaussian or lognormal fields (arXiv:1912.02763, arXiv:2310.18996), 2LPT fields (arXiv:2607.27412) and N-body fields calibrated on a hydrodynamical simulation (arXiv:2305.08899) [src].

Where it fails: around galaxies and quasars (proximity, feedback); in gas heated in protoclusters, where a galaxy overdensity shows no excess absorption (arXiv:2303.07619) [src]; wherever Γ_HI or T fluctuate on large scales (after reionisation, arXiv:2207.13098; from clustered sources, arXiv:1404.7425) [src].

### 1.3 The three smoothing scales of the small-scale flux power

Small-scale power in F is erased by three effects that must be separated to extract dark-matter physics:

| Effect | Depends on | Acts on |
|---|---|---|
| Thermal (Doppler) broadening | instantaneous temperature T_0, γ | line of sight only |
| Pressure (Jeans) smoothing | the integrated thermal history, i.e. when and how much the gas was heated | three dimensions |
| Free streaming of dark matter (WDM, FDM) | particle mass | three dimensions, in the matter field itself |

The high-z P1D is "highly sensitive to both the instantaneous temperature of the IGM and the total energy injected per unit mass during and after reionization" (arXiv:1809.06980) [src]; the pressure smoothing scale depends on the details of hydrogen and helium reionisation (arXiv:1607.04218) [src]; WDM suppression saturates at k ≳ 0.1 s/km because of peculiar-velocity smearing (arXiv:2209.14220) [src]. The non-linear flux power "has a generic shape determined by a transition scale from linear to non-linear anisotropy, and a Jeans scale below which the power drops rapidly" (arXiv:1506.04519) [src].

### 1.4 Why it constrains cosmology

- **Geometry at z > 2.** The BAO feature in 3D flux correlations gives D_H/r_d and D_M/r_d at z ≈ 2.3, in the matter-dominated era; proposed as a survey goal by McDonald & Eisenstein 2007 (arXiv:astro-ph/0607122), who noted that a percent-level measurement there nearly doubles a dark-energy figure of merit when curvature is free [src], and first detected in BOSS (arXiv:1211.2616). The anisotropy of the broadband adds an Alcock–Paczynski measurement of D_M/D_H (idea in McDonald 2003, arXiv:astro-ph/0108064; realised in arXiv:2209.13942).
- **Small-scale linear power.** P1D probes the amplitude and slope of the linear matter power at k ~ 1 h/Mpc and z ~ 3 (arXiv:2311.16377) [src], a lever arm of two decades in k relative to the CMB; hence the sensitivity to running, Σm_ν, N_eff and to cut-offs from dark-matter free streaming.
- **Thermal history.** The same small-scale power and the line widths measure T_0, γ and the pressure smoothing, which trace H and He II reionisation.

## 2. From spectra to the delta field

### 2.1 Definition

    δ_F(λ) = f(λ) / [ C_q(λ) F̄(z) ] − 1

with f the observed flux, C_q the unabsorbed continuum of quasar q and F̄(z) the mean transmission. In the DESI pipeline the product is assumed to be a universal function of rest-frame wavelength corrected by a first-degree polynomial in Λ ≡ log λ (arXiv:2503.14739, Sect. 2.4) [src]:

    F̄(λ) C_q(λ) = C̄(λ_rf) × [ a_q + b_q (Λ − Λ_min)/(Λ_max − Λ_min) ]

C̄(λ_rf), a_q and b_q are solved by maximum likelihood, with weights that combine the (re-calibrated) pipeline noise and the intrinsic forest variance; the procedure is documented in Ramírez-Pérez et al. 2024 (arXiv:2306.06312). The polynomial absorbs quasar luminosity and spectral diversity **and** the redshift evolution of F̄(z), so the survey δ field carries no absolute mean-flux information.

Because the fit "effectively subtracts the mean δ and the first moment of each forest", the measured field is δ̃_i = η_ik δ_k, with η a projector acting within each forest. The same operation is applied to the model through the distortion matrix D_MN, a linear relation between distorted and undistorted correlation functions in bins M and N (introduced in BOSS DR12, arXiv:1702.00176; tested in arXiv:2506.15262) [src]. In DR2 the distortion matrix includes the redshift evolution of the clustering as ((1+z_k)(1+z_p)/(1+z_ref)²)^(γ_α − 1), the model is computed on 2 h⁻¹Mpc bins (data: 4 h⁻¹Mpc) and extended to 300 h⁻¹Mpc along r_∥ (arXiv:2503.14739, Sect. 3.1) [src].

DESI specifics (arXiv:2503.14739, Sect. 2.4) [src]: observed range 3600–5772 Å; rest-frame region A 1040–1205 Å and region B 920–1020 Å, correlated separately; masks for cosmic rays, BAL locations and DLA cores; forests shorter than 120 Å discarded; the C III region 1600–1850 Å is used to derive a spectro-photometric correction (peaking at 5% at 3650 Å) and a 1.5% correction to the noise variance.

The pipeline used from eBOSS DR16 to DESI is `picca`, public since arXiv:2007.08995 [src]. The DESI EDR Lyα catalogue paper documents the changes relative to SDSS, in particular the weighting scheme that improves the correlation-function precision by more than 20% (arXiv:2306.06312) [src].

### 2.2 Alternative continuum methods

| Method | Principle | Performance | Citation | Flag |
|---|---|---|---|---|
| Mean-flux-regulated PCA | PCA fit redward of Lyα predicts the forest continuum shape; slope and amplitude corrected with an external mean flux | 8% rms at S/N ~ 2, < 5% at S/N > 5; extends usable P1D to ~2× larger scales | arXiv:1108.6080 | [src] |
| LyCAN (CNN) | predicts 1040–1600 Å continuum from 1216–1600 Å, trained on COS-based and DESI mock spectra | median error 1.5% (DESI mocks), 4.1% (COS spectra); 40% better than PCA/NMF | arXiv:2405.06743 | [src] |
| Composite ratios | no per-object continuum; flux ratios of composites at different z | relative F̄(z), anchored at z < 2.5 | arXiv:1208.2584 | [src] |
| Direct spline fitting | high-resolution spectra only | biased low by < 1%, 4%, 12% at z = 2, 3, 4; corrected with mocks | arXiv:0710.4522 | [src] |

### 2.3 Forest regions, masks and catalogues

- The Lyα absorption in the Lyβ region of the spectrum has been used in 3D analyses since eBOSS DR14 (arXiv:1904.03400) [src].
- Masked or corrected before the fit: DLAs (catalogues arXiv:2107.09612, arXiv:2103.10964, arXiv:2503.14740), BAL troughs (arXiv:2111.09439, arXiv:2405.09737), sky lines.
- Background sources other than quasars: Lyman-break galaxies (tomography since arXiv:1409.5632; first 3D correlation with DESI, arXiv:2507.21852) [src].
- Other transitions as forests: C IV (arXiv:2601.08103) [src].

## 3. One-dimensional flux power spectrum

### 3.1 Definition and relation to 3D

P1D is the power spectrum of δ_F along the line of sight, in redshift bins. It is a projection of the 3D flux power:

    P_1D(k_∥) = (1/2π) ∫_{k_∥}^{∞} P_3D(k, μ = k_∥/k) k dk

so every k_∥ receives 3D power from all smaller scales; this is why P1D at modest k is sensitive to thermal and free-streaming cut-offs, and why EFT descriptions of P1D need extra stochastic terms "from the integration over small-scale modes" (arXiv:2604.09407) [src].

### 3.2 Estimators

| Estimator | Principle | Strengths | Weak points | References |
|---|---|---|---|---|
| FFT | Fourier transform each forest chunk, subtract noise power, divide by the squared resolution window, average | fast, transparent | masking bias and continuum bias must be corrected from mocks; needs a noise-power model or a cross-exposure estimate | arXiv:1306.5896, arXiv:1812.03554, arXiv:2306.06311, arXiv:2505.09493 |
| Likelihood / QMLE (optimal quadratic) | band powers from a quadratic estimator with a fiducial power and the full pixel covariance | "robust against … pixel masking, time evolution within spectrum and quasar continuum errors"; resolution matrix per pixel | cost; depends on the fiducial model and the noise model | arXiv:2008.06421, arXiv:2108.10870, arXiv:2306.06316, arXiv:2505.07974 |
| Weighted FFT with window matrix | forward-model the effect of masked pixels and pixel weights on FFT estimates; extends to P× | keeps FFT speed, adds weights | validated on Gaussian and hydrodynamical simulations; not yet the DR1 baseline | arXiv:2505.02904 |
| Forward-modelled (high resolution) | mock spectra with the data's noise, resolution and masks; emulator; MCMC | consistent treatment of masks | tied to the simulation grid | arXiv:1709.07354 |

Two-estimator practice dates from BOSS DR9, where a Fourier-transform and a maximum-likelihood method agreed over 12 redshift bins (arXiv:1306.5896) [src]. In DESI both estimators are run on every data set (EDR: arXiv:2306.06311 and arXiv:2306.06316; DR1: arXiv:2505.09493 and arXiv:2505.07974) with a joint validation paper (arXiv:2509.13593) [src].

DESI DR1 innovations: a cross-exposure estimator that removes the need to model pipeline noise; a covariance-matrix estimator for the FFT measurement; data splits (arXiv:2505.09493, arXiv:2505.07974) [src]. Validation: 20 synthetic realisations for masking and continuum corrections, Kolmogorov–Smirnov tests of the estimators and covariances, and CCD image simulations of 675,000 quasars for resolution (arXiv:2509.13593) [src].

### 3.3 Contaminant handling in P1D

Side-band (red-side) power for metals and noise calibration (arXiv:2306.06316); Si III oscillations modelled since SDSS (arXiv:astro-ph/0405013); DLA and BAL masking; resolution and noise corrections [src]. Details in `systematics.md`.

### 3.4 Higher order in 1D

The 1D bispectrum was first measured robustly on eBOSS DR16 with an FFT estimator (arXiv:2410.09150) [src].

## 4. Three-dimensional correlations

### 4.1 Estimators

- **Auto-correlation** ξ(r_∥, r_⊥): weighted average of δ_i δ_j over pixel pairs from different lines of sight, binned in separation along and across the line of sight computed with a fiducial cosmology.
- **Cross-correlation** with quasars: weighted average of δ_i over quasar–pixel pairs; no random catalogue is needed because δ has zero mean by construction. First BAO measurement in arXiv:1311.1767 [src].
- **Legendre multipoles** of both, as an alternative compression that gives a positive-definite covariance without smoothing (arXiv:2603.04281) [src].
- Fast pair-counting codes for two- and three-point functions exist outside the collaboration pipeline (Lya2pcf, found by search this session; not cited as a source).

The auto- and cross-correlations are complementary "because of the quite different impact of redshift-space distortion on the two measurements" (arXiv:1404.1801) [src].

### 4.2 The model

On large scales the flux power is a Kaiser-like form with two bias parameters,

    P_F(k, μ) = b_F² (1 + β_F μ²)² P_L(k) × D_NL(k, μ),     b_F β_F = b_η f

where b_F ≡ b_δ is the density bias (negative: more matter, less flux), b_η the bias with respect to the line-of-sight velocity gradient, f the growth rate, and D_NL a non-linear correction. Unlike for galaxies, β_F is not f/b: b_η is an independent parameter (bias parameters computed from simulations in arXiv:astro-ph/0108064 and arXiv:1506.04519) [src]. The first measurement gave 0.16 < b < 0.24 (in absolute value), 0.44 < β < 1.20 and b(1+β) = 0.336 ± 0.012 at z = 2.25 (arXiv:1104.5244) [src]. The bias evolves steeply, ∝ (1+z)^γ with γ_α = 3.05 ± 0.16 (arXiv:2607.19619) or 2.96 ± 0.06 (arXiv:2505.07974) [src].

Components of the fitted model in current analyses, each documented in a dedicated paper:

| Component | What it describes | Reference |
|---|---|---|
| BAO peak / smooth decomposition with (α_∥, α_⊥) | isolates the BAO information; anisotropic non-linear broadening of the peak | arXiv:1301.3456 |
| Distortion matrix | continuum-fitting projection | arXiv:1702.00176, arXiv:2506.15262 |
| HCD term | residual damping wings: Voigt model | arXiv:1711.06275, arXiv:2506.13005 |
| Metal correlations | Si II, Si III, Si IV, C IV with the forest and with quasars | arXiv:1702.00176, arXiv:2404.03003 |
| UV background fluctuations | scale-dependent bias | arXiv:1404.7425, arXiv:1402.0506 |
| Quasar redshift errors and non-linear velocities | radial shift and damping of the cross-correlation | arXiv:1708.02225, arXiv:2205.06648, arXiv:2402.18009 |
| Correlated sky-subtraction and calibration noise | excess at zero line-of-sight separation | arXiv:2404.03003 |
| Non-linear correction D_NL | fitting function of Arinyo-i-Prats et al., valid to k = 10 h/Mpc at < 5% | arXiv:1506.04519, arXiv:2205.00962 |
| Broadband polynomials (optional) | test of robustness of BAO to the smooth model | arXiv:1904.03400 |

The EDR analysis used a 13-parameter model "based on linear perturbation theory" (arXiv:2308.10950) [src]; the DR2 BAO fit has 17 parameters (arXiv:2503.14739) [src]. The fitter used by DESI is `Vega` (`github.com/andreicuceu/vega`, cited as a package, not a paper, in arXiv:2503.14739), with a Gaussian likelihood sampled by PolyChord [src]; BOSS DR9–DR11 used `baofit` (arXiv:1301.3456, arXiv:1311.1767) [src].

The DR2 BAO configuration, as the reference example of current practice (arXiv:2503.14739, Sects. 3–4 and Appendix A) [src]:

- Data vector: four correlation functions (Lyα(A)×Lyα(A), Lyα(A)×Lyα(B), Lyα(A)×QSO, Lyα(B)×QSO) on a rectangular (r_∥, r_⊥) grid with 4 h⁻¹Mpc bins out to 200 h⁻¹Mpc; the cross-correlation keeps the sign of r_∥ (negative when the quasar is behind the pixel). 15,000 points, 9306 after the cut 30 < r < 180 h⁻¹Mpc. DR1 fitted 10 < r < 180 h⁻¹Mpc; the range was narrowed "because the model is not a good fit at smaller scales".
- Fiducial cosmology for coordinates and templates: Planck 2018 flat ΛCDM, Ω_m = 0.31509, h = 0.6736, r_d = 147.09 Mpc = 99.08 h⁻¹Mpc, giving D_H/r_d = 8.6172 and D_M/r_d = 39.1879 at z = 2.33, f = 0.9703.
- BAO parameters: α_∥ = [D_H/r_d]/[D_H/r_d]_fid and α_⊥ = [D_M/r_d]/[D_M/r_d]_fid, applied to the peak component only.
- Nuisance parameters (15): b_α, β_α; five metal biases (Si II 1190, 1193, 1260; Si III 1207; an effective C IV); b_HCD, β_HCD and a filter scale L_HCD for the wings; quasar bias b_Q; Δr_∥ and σ_v for redshift errors and peculiar velocities; ξ_0^TP for the transverse proximity effect; a_noise for noise correlated between fibres of the same focal-plane petal.
- Metal modelling: a "metal matrix" maps true separations to the separations assumed under the Lyα hypothesis; at z = 2.33 the Si III(1207) and Si II(1190, 1193, 1260) correlations with Lyα produce spurious peaks at |Δr_∥| ≈ 21, 59, 52 and 104 h⁻¹Mpc.
- Robustness: adding Legendre-polynomial broadband terms (orders 0, 2, 4, 6 divided by r^0, r^1, r^2; 48 extra parameters) changes χ² from 9304.5 to 9243.6 and has a negligible effect on BAO.
- Not modelled: relativistic effects in the cross-correlation (degenerate with metals and redshift errors; planned for future work).
- Covariance: measured from the data over HEALPix pixels (the paper's bootstrap noise realisations are stacks of HEALPix pixels drawn with replacement); the full description is in the DR1 paper (arXiv:2404.03001).

### 4.3 Full shape and Alcock–Paczynski

Separations are computed from angles and redshifts with the fiducial cosmology, r_∥ = [D_C(z_i) − D_C(z_j)] cos(Δθ/2) and r_⊥ = [D_M(z_i) + D_M(z_j)] sin(Δθ/2); a wrong fiducial rescales them by q_∥ and q_⊥. The analysis isolates

    φ ≡ q_⊥/q_∥ = [D_M/D_H] / [D_M/D_H]_fid,      α ≡ sqrt(q_⊥ q_∥)

and, because the template is still split into peak and smooth components, fits two pairs: (φ_p, α_p) for the BAO peak, with α_p = [sqrt(D_M D_H)/r_d]/[…]_fid, and (φ_s, α_s) for the broadband. φ_s is the new cosmological information; α_s (related to the equality scale) is weak and contaminated and is marginalised (arXiv:2607.27410, Sect. 3.1) [src]. A BAO-only analysis rescales the peak only and keeps the smooth component's coordinates fixed.

Why AP is separable from RSD in the forest: the two anisotropies are degenerate when their functional forms coincide, which is the case for β → 0; the response of a Kaiser model to φ_s departs from the response to β as β grows, so the large β of the forest (about 1.2, against about 0.4 for galaxies) makes the broadband AP measurable (arXiv:2607.27410, Sect. 3.1.2) [src].

Small-scale marginalisation (arXiv:2607.27410, Sect. 3.3) [src]: the distortion matrix mixes information along the line of sight, so correlations at r_∥ < 10 h⁻¹Mpc in the undistorted model leak into all scales of the distorted one, and a cut r > r_min does not remove sensitivity to r < r_min; ignored, this "could lead to percent-level biases in Lyα AP constraints". The remedy adds one free amplitude per small-scale bin of the undistorted model, each multiplying a linear template propagated through the distortion matrix, and marginalises them analytically by a covariance update C̃ = C + Δ̂ S Δ̂ᵀ. All data down to zero separation stay in the χ², so no degrees of freedom are gained or lost. Validation on eBOSS mocks set r_min = 25 h⁻¹Mpc (arXiv:2209.12931) [src]. The DESI DR2 analysis instead marginalises analytically over scales below 10 h⁻¹Mpc and over UV-background fluctuations, with priors on non-linear clustering derived from the DESI P1D through ForestFlow (arXiv:2607.27411, arXiv:2607.27413) [src]. The growth-rate parameter is not recovered without bias on mocks and is excluded (arXiv:2607.27411) [src].

### 4.4 P3D and the cross-spectrum P×

    P_×(k_∥, θ)   — the cross-power between two lines of sight separated by angle θ, as a function of line-of-sight wavenumber

is the natural statistic of forest geometry: Fourier along the well-sampled direction, configuration space across the sparsely sampled one (Font-Ribera et al. 2018, arXiv:1710.11036) [src]. P1D is its zero-separation limit; P3D is its 2D Fourier transform in the transverse plane.

| Estimator | Idea | Status | Citation | Flag |
|---|---|---|---|---|
| P× quadratic estimator | block-diagonal global covariance; likelihood for P3D as a Taylor expansion around a fiducial | algorithm demonstrated | arXiv:1710.11036 | [src] |
| Averaged 1D FFTs | small-scale P3D from products of 1D Fourier modes of neighbouring sightlines; validated on Nyx | eBOSS DR16 proof of principle at z = 2.2, 2.4 | arXiv:2310.09116 | [src] |
| Pair-count spectral estimator | weight pixel pairs by exp(ik·r); tractable window matrix | eBOSS DR16, 0.02 ≤ k ≤ 0.35 h/Mpc | arXiv:2403.08241 | [src] |
| Optimal 3D estimator | exact window deconvolution, marginalisation of continuum modes, conjugate gradient + P³M; flat sky | validated on mocks | arXiv:2503.15619 | [src] |
| MAPLE | maximum a posteriori band powers and covariance, Wiener-filter based | method paper | arXiv:2403.17294 | [src] (title and snippet) |
| Unified HMC reconstruction | P3D from ξ_3D, P1D and P× jointly | forecast on DESI-like mock vector | arXiv:2506.08198 | [src] |

The convergence facts that govern fits of this model to simulation boxes are in §6.

## 5. Tomography and voids

- **Reconstruction.** Wiener filtering of the pixel δ values into a 3D map; the achievable resolution is set by the mean transverse sightline separation (2.5 h⁻¹Mpc in CLAMATO, arXiv:1710.02894; 13 h⁻¹Mpc in Stripe 82, arXiv:2004.01448) [src]. CLAMATO DR2 adds a forward-modelled matter field from a joint galaxy + forest likelihood (arXiv:2109.09660) [src].
- **Voids.** Spherical-overdensity finder calibrated on hydrodynamical simulations (arXiv:1710.02612) [src]; void and protocluster-candidate catalogues from the Stripe 82 map, with performance assessed on simulated eBOSS observations (arXiv:2004.01448) [src].
- **Void–forest cross-correlation.** Stack the δ field around void centres as a function of (r_∥, r_⊥); the quadrupole measures RSD from flows out of voids, with a linear model that includes the tomographic effect of pixels lying along parallel lines of sight; β = 1.21 ± 0.18 at z = 2.49 (arXiv:2203.11045) [src]. The broader void literature belongs to `cosmo-beyond-two-point`.
- **Forest × galaxies** in tomography fields: galaxy bias and redshift systematics from the cross-correlation (arXiv:2509.07453) [src].
- **Forecast** for wide-area critical-point statistics: arXiv:2201.02606.

## 6. Simulations and emulators

### 6.1 Convergence requirements

For flux statistics at 2 ≤ z ≤ 4 with Nyx: 20 h⁻¹kpc cells for 1% convergence up to k = 10 h/Mpc; boxes above 40 h⁻¹Mpc for sub-percent missing-mode errors; "splicing" of several boxes is accurate only at the 10% level; rescaling optical depths to the observed mean flux changes convergence rates (Lukić et al. 2015, arXiv:1406.6361) [src]. For the 3D power, the convergence of large-scale modes that set β is driven by resolution through mode coupling rather than by box size (arXiv:2407.04473) [src]. Earlier hydro-PM work found ~40 h⁻¹Mpc boxes and ~40 h⁻¹kpc resolution for < 5% (arXiv:astro-ph/0108064) [src]. Eulerian (Nyx) and SPH (CRK-HACC) codes agree to ≲ 1% in P1D once SPH densities are reconstructed by tessellation (arXiv:2207.05023) [src]; Nyx and Gadget were compared for DESI-like P1D in arXiv:2012.04008 [src].

### 6.2 UV background and thermal histories

Simulations use spatially uniform photo-ionisation and photo-heating rates from synthesis models (Haardt & Madau 2012, arXiv:1105.2039) [src]. Known issues: canonical tables reionise and heat too early, z ~ 15 (arXiv:1607.04218); HM2012 under-predicts Γ_HI needed at z > 4 and z < 2 (arXiv:1410.1531); Nyx with HM2012 gives T_0 ≈ 10⁴ K and γ ≈ 1.55 at z = 2 (arXiv:1406.6361) [src]. Thermal histories are therefore varied explicitly (rescaled heating rates, reionisation redshift) and marginalised.

### 6.3 Emulators and their parameterisations

| Emulator | Training suite | Inputs | Output and accuracy | Citation | Flag |
|---|---|---|---|---|---|
| LaCE (Gaussian process) | hydrodynamical suite | amplitude and slope of the linear power at small scales + IGM state, per redshift, 2 < z < 4 | P1D; sub-percent for a 0.3 eV neutrino cosmology not in the training set | arXiv:2011.15127 | [src] |
| LaCE (neural network) | same family | same | sub-percent over k_∥ = 0.1–4 Mpc⁻¹, z = 2–4.5; percent level to 8 Mpc⁻¹ | arXiv:2305.19064 | [src] |
| ForestFlow | 30 fixed-and-paired simulations | cosmology + IGM | b_δ, b_η and six non-linear P3D parameters by conditional normalising flows; 3% (P3D) and 1.5% (P1D) to k = 5 Mpc⁻¹, k_∥ = 4 Mpc⁻¹ | arXiv:2409.05682 | [src] |
| PRIYA | 48 + 3 multi-fidelity runs | 9 parameters + 2 in post-processing | P1D and mean T; ≲ 1% interpolation error | arXiv:2306.05471, arXiv:2309.03943 | [src] |
| Lyssa / lym1d | 18 Nyx runs | cosmology + thermal | P1D, percent-level agreement with a previous emulator | arXiv:2412.05372 | [src] |
| Nyx GP emulator study | Nyx grid | — | end-to-end inference on mock eBOSS/DESI data; adaptive sampling advocated over a fixed Latin hypercube | arXiv:2012.04008 | [src] |

Two philosophies coexist: emulate as a function of **cosmological parameters** (PRIYA, Lyssa), or as a function of the **linear power amplitude and slope at the redshift and scale probed** (LaCE, ForestFlow), which lets one emulator serve extended models whose linear power is described by an amplitude and slope; the latter is stated not to cover "models with sharp features in the linear power, such as warm or light axion dark matter" (arXiv:2011.15127) [src].

### 6.4 Perturbative models

One-loop EFT of the flux field, equivalent to a line-of-sight-dependent bias expansion; sub-percent to k = 3 h/Mpc at z = 2.8 on Sherwood for both 3D and 1D (arXiv:2309.10133) [src]; below 2% to k = 2 h/Mpc on ACCEL² (arXiv:2412.06892) [src]; first application to data with simulation-informed priors (arXiv:2405.13208) [src]; field-level forward models (arXiv:2507.00284, arXiv:2606.26234) and a hybrid EFT model (arXiv:2512.13681) [src]; analytic compression for P1D (arXiv:2604.09407) [src]. Simulation-based inference has been tried on CAMELS (arXiv:2603.13011) [src].

## 7. Cosmological inference from P1D

- **Compression.** The information is summarised by the linear-power amplitude Δ²_L = k³ P_L / 2π² and slope n_eff = dlnP_L/dlnk at k_p = 0.009 s/km and z_p = 3, introduced with a χ² table in McDonald et al. 2005 (arXiv:astro-ph/0407377) [src] and used again for DESI DR1 as (Δ²_★, n_★) (arXiv:2601.21432) [src]. External users combine this two-parameter likelihood with CMB and BAO (arXiv:2311.16377, arXiv:2609.22581) [src]. The compression must be re-validated for models with scale-dependent features; it was checked to 0.15% for a sterile-neutrino model (arXiv:2609.22581) [src].
- **Nuisance parameters.** Mean transmission, T_0, γ, pressure smoothing or a thermal-history proxy, per redshift or as smooth functions; HCD and metal contamination amplitudes; resolution and noise. The DESI DR1 analysis corrects the emulator prediction for "astrophysical contaminants and systematics, many of these not considered in previous analyses" (arXiv:2601.21432) [src].
- **The DESI DR1 implementation** (arXiv:2601.21432, Sects. 2, 6–8) [src]: likelihood code `cup1d`; baseline emulator `lace-mpg`, a Gaussian process trained on 30 fixed-and-paired MP-Gadget simulations, cross-checked on mocks built from the high-resolution Lyssa central and Sherwood simulations and against a `lace-lyssa` emulator; emulator covariance included in the likelihood; 16 metal and 8 HCD parameters; systematic errors assumed fully correlated across scales and uncorrelated with each other (assuming them uncorrelated across scales, as in SDSS analyses, doubles the fit probability); combination with CMB and BAO chains by importance sampling of a Gaussian (Δ²_★, n_★) posterior; the compressed parameters are computed over half to twice the pivot scale.
- **Stated limitations of that analysis** (same paper, Sect. 8) [src]: emulator errors are comparable to the DR1 statistical errors up to z = 2.8 and degrade the Δ²_★ and n_★ precision by 30% and 19%; leave-one-out tests overestimate emulator errors; no informative IGM priors are used because unbiased recovery of IGM parameters by `cup1d` was not validated; the metal and HCD models of earlier SDSS analyses "are strongly disfavored by DESI data"; the LLS contamination parameters are strongly correlated with the compressed parameters, so the assumed LLS functional form is a concern; UV-background fluctuations, patchy hydrogen and helium reionisation and galaxy-formation feedback are not modelled; a joint fit with high-resolution data would break the degeneracies among mean flux, T_0, γ and pressure smoothing.
- **Frequentist alternative.** Profile likelihoods with Feldman–Cousins intervals for Σm_ν, including the eBOSS P1D (arXiv:2507.12401) [src].

## 8. Covariance, likelihood and blinding practice

- 3D: covariance from the data (see `systematics.md` D4), Gaussian likelihood on the binned correlation functions, validation on 150 (DR1) and 400 (DR2) mock realisations (arXiv:2404.03004, arXiv:2503.14741) [src].
- P1D: estimator-level covariance, validated on synthetic realisations (arXiv:2509.13593) [src].
- Blinding: applied to DESI Lyα BAO from DR1 (arXiv:2404.03001), to the full-shape analyses (arXiv:2509.15308, arXiv:2607.27411) and to the P1D cosmology (arXiv:2601.21432) [src]; an AP-based catalogue-level scheme is described in arXiv:2607.07875 [src].

## 9. Codes

| Code | Role | Reference paper |
|---|---|---|
| `picca` | delta extraction, correlation functions, distortion matrices, P1D (FFT) | arXiv:2007.08995 (public release statement), arXiv:2306.06312 |
| `baofit` | BAO fitting for BOSS | arXiv:1301.3456, arXiv:1311.1767 |
| `Vega` | DESI correlation-function fitter | used and named in arXiv:2503.13442 |
| QMLE P1D estimator | optimal quadratic estimator | arXiv:2008.06421 |
| `LaCE` | P1D emulators | arXiv:2011.15127, arXiv:2305.19064 |
| `ForestFlow` | P3D + P1D emulator | arXiv:2409.05682 |
| `lym1d` | P1D likelihood with Lyssa emulator | arXiv:2412.05372 |
| PRIYA emulator | multi-fidelity P1D likelihood | arXiv:2306.05471 |
| `LyaCoLoRe`, Saclay mocks, `quickquasars`, CoLoRe-2LPT | mock transmission and synthetic spectra | arXiv:1912.02763, arXiv:2310.18996, arXiv:2401.00303, arXiv:2607.27412 |
| Nyx | Eulerian hydrodynamics | arXiv:1301.4498 |
| LyCAN | CNN continuum prediction | arXiv:2405.06743 |
| DLA finders | CNN, Gaussian process, template Toolkit | arXiv:2107.09612, arXiv:2103.10964, arXiv:2503.14740 |

The methods of arXiv:2004.01448 (tomography and void finding), arXiv:2203.11045 (void cross-correlation), arXiv:1506.04519 (P3D model) and arXiv:2306.06311 (DESI P1D) each have a public implementation by their authors; general software conventions belong to `cosmo-software-ecosystem`.

## 10. Conventions, units and where the community is split

- **Wavenumber units.** Survey P1D is published in velocity units, k in s/km (written (km/s)⁻¹), which needs no fiducial cosmology; simulations and emulators work in comoving Mpc⁻¹ or h/Mpc. The conversion k[s/km] = k[Mpc⁻¹] (1+z)/H(z) depends on redshift and cosmology. The pivot 0.009 s/km at z = 3 corresponds to "~1 h/Mpc" (arXiv:2311.16377) [src]; emulator papers quote pivots of 0.78 Mpc⁻¹ (PRIYA, arXiv:2309.03943) and 0.7 Mpc⁻¹ (arXiv:2604.09407) [src]. Check the unit before comparing amplitudes or slopes.
- **Symbols for the compressed parameters.** (Δ²_L, n_eff), (Δ²_★, n_★), (A_Lyα, n_Lyα), (A_P, n_P), (Δ²_p, n_p) all appear (arXiv:astro-ph/0407377, arXiv:2601.21432, arXiv:2412.05372, arXiv:2309.03943, arXiv:2604.09407) [src]; they are not interchangeable (A_P, n_P are primordial-spectrum parameters at a pivot, the others describe the linear matter power at z = 3).
- **Distances.** Older papers quote D_A/r_d or c/(H r_s) (arXiv:1404.1801, arXiv:1311.1767); since DR12 the convention is D_M/r_d and D_H/r_d, with D_M = (1+z) D_A. The DESI abstracts also give H and D_M normalised to r_d = 147.09 Mpc (arXiv:2404.03001).
- **Bias sign and names.** b_F (or b_α, b_δ) is negative; some papers quote |b|. β_F (or β_α) = b_η f / b_δ.
- **DLA threshold.** log N_HI ≥ 20.3 is the catalogue convention (arXiv:2107.09612, arXiv:2503.14740); a modelling paper uses 20.2 (arXiv:2506.13005) [src].
- **Effective redshift.** 2.33–2.40 for the same kind of sample depending on weighting and on auto versus cross (table in `results.md`).
- **WDM mass.** Limits are for thermal relics; sterile-neutrino masses are model-dependent conversions (arXiv:1512.01981 gives both) [src].
- **Split: emulator inputs** (cosmological parameters versus linear-power parameters), **estimator** (FFT versus QMLE), **3D statistic** (ξ on a 2D grid versus multipoles versus Fourier space), **theory** (empirical Kaiser-based model versus EFT versus emulator). Each choice has a published counterpart to compare with.

## 11. Not verified

- The explicit form of the pixel weights (the variance model with its η, σ_LSS, ε terms) and of the projector η_ik (Eq. 3.3 of the DR1 paper).
- The smoothing applied to the 3D covariance matrix in DESI DR1/DR2 as written in the DR1 paper body.
- A reference paper for `Vega` itself, and for `picca` beyond the release statement.
- The SPH codes behind Sherwood and the LaCE training set (not stated in the abstracts read).
