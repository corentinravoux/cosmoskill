# physics-and-methods — cosmo-inflation-primordial

Snapshot: 2026-10-14

Scope: what the primordial observables are, how each is estimated from CMB and large-scale-structure data, which models are fitted, how likelihoods, covariances and blinding are handled, the public codes, and the conventions on which papers differ.

Flags: `[src]` read this session in the cited paper; `[sec]` read in a named secondary source; `[der]` derived here. Formulas marked "textbook" are standard definitions and carry no flag. Numerical results are in `results.md`.

## 1. What is measured and why it constrains the early Universe
<!-- key: what-is-measured-and-why-it-constrains-the -->

Inflation (Guth 1981, doi:10.1103/PhysRevD.23.347; Starobinsky 1980, doi:10.1016/0370-2693%2880%2990670-X — the parentheses of this DOI are percent-encoded) makes five generic statements that data can test. The slow-roll "new inflationary universe" scenario followed (Linde 1982, doi:10.1016/0370-2693%2882%2991219-9; Albrecht 1982, doi:10.1103/PhysRevLett.48.1220). The generation of density perturbations in that scenario was worked out in 1982–1983 by Hawking (doi:10.1016/0370-2693%2882%2990373-2), Starobinsky (doi:10.1016/0370-2693%2882%2990541-X), Guth ("Fluctuations in the New Inflationary Universe", doi:10.1103/PhysRevLett.49.1110) and Bardeen ("almost scale-free density perturbations", doi:10.1103/PhysRevD.28.679); Mukhanov 1992 is the standard review of the theory of cosmological perturbations (doi:10.1016/0370-1573%2892%2990044-Z). Titles, first authors and years of these six were confirmed on Crossref; their content was not read this session. The simplest single-field slow-roll models predict perturbations that are adiabatic, nearly Gaussian, nearly but not exactly scale-invariant, on a spatially flat background, with a stochastic background of tensor modes whose amplitude measures the energy scale. Each statement maps to an observable.

| Statement | Observable | Probe | Current status (see `results.md`) |
|---|---|---|---|
| Nearly scale-invariant scalar spectrum | n_s, running α_s = dn_s/dln k, binned P_R(k) | CMB TT/TE/EE; Lyα P1D for the lever arm | n_s < 1 at about 10σ; no running |
| Tensor modes | r, n_t | CMB B modes at degree and larger scales | r < 0.036 (95%) |
| Gaussianity | f_NL^local, f_NL^equil, f_NL^ortho, g_NL, other templates | CMB bispectrum; galaxy scale-dependent bias and bispectrum | consistent with zero; σ(f_NL^local) = 5 |
| Adiabaticity | isocurvature fractions β_iso, α_non-adi | CMB TT/TE/EE | per-cent-level limits |
| Flatness | Ω_K | CMB + BAO | Ω_K = 0.0023 ± 0.0011 with DESI DR2 |
| No preferred scale | feature amplitudes A_lin, A_log | CMB and galaxy power spectra | A < 2–3% |
| Parity (not an inflationary prediction) | birefringence angle β | CMB EB, TB | 0.3° hint, 2.4–4.8σ |

Reviews to start from: Achúcarro et al. 2022 (Snowmass white paper covering gravitational waves, non-Gaussianity and features; arXiv:2203.08128); Kamionkowski and Kovetz 2016 for B modes (arXiv:1510.06042); Chluba, Hamann and Patil 2015 (arXiv:1505.01834) and Slosar et al. 2019 (arXiv:1903.09883) for features; Komatsu 2022 for birefringence and the origin of tensor modes (arXiv:2202.13919); Kallosh and Linde 2025 for the model landscape after ACT (arXiv:2505.13646). The Planck 2018 inflation paper (arXiv:1807.06211) remains the reference for definitions and for the analysis templates that later papers copy.

## 2. Scalar power spectrum
<!-- key: scalar-power-spectrum -->

### Parametrisation (textbook)
<!-- key: parametrisation-textbook -->

ln P_R(k) = ln A_s + (n_s − 1) ln(k/k_*) + ½ α_s ln²(k/k_*) + (1/6) β_s ln³(k/k_*), with α_s = dn_s/dln k and β_s the running of the running. Current CMB papers use the pivot k_* = 0.05 Mpc⁻¹ (arXiv:2503.14454). The pivot matters for n_s as soon as α_s is free.

As Planck 2018 writes it (arXiv:1807.06211) [src: Sect. 2.1, Eqs. 3–5, Table 1]: ln P_R(k) = ln A_s + (n_s − 1) ln(k/k_*) ≡ ln P_0(k) (Eq. 3); the running and running of running are added as ½ (dn_s/dln k) ln²(k/k_*) + (1/6)(d²n_s/dln k²) ln³(k/k_*) (Eq. 4, where the paper's typesetting reads "d ln n_s"); the tensor spectrum is ln P_t(k) = ln(r A_s) + n_t ln(k/k_*) (Eq. 5). All primordial quantities are at k_* = 0.05 Mpc⁻¹, and r is also quoted as r_0.002 for comparison with earlier work. Observable scales span 10⁻⁴ ≲ k ≲ 10⁻¹ Mpc⁻¹.

### Slow-roll dictionary (textbook)
<!-- key: slow-roll-dictionary-textbook -->

With ε_V = (M_Pl²/2)(V′/V)² and η_V = M_Pl² V″/V: n_s − 1 = 2η_V − 6ε_V, r = 16 ε_V, n_t = −r/8 (the single-field consistency relation), and α_s is second order in slow roll. Planck 2018 defines the potential parameters ε_V, η_V, ξ²_V, ϖ³_V and the Hubble-flow parameters ε_1 = −Ḣ/H², ε_(n+1) = ε̇_n/(H ε_n) (arXiv:1807.06211) [src: Table 1]; it imposes n_t = −r/8, "the case for slow-roll inflation driven by a single scalar field with a canonical kinetic term", and tests its relaxation with r at two scales (r_0.002, r_0.02): the relation is compatible with Planck + BK15, but n_t ≃ 2 with r_0.01 ≃ 0.05 stays inside 68% [src: Sects. 3.5–3.6]. First-order HFF constraints, TT,TE,EE + lowE + lensing (+ BK15): ε_1 < 0.0063 (0.0039) at 95%, ε_2 = 0.030 +0.007/−0.005 (0.031 ± 0.005); η_V = −0.010 +0.004/−0.008 (−0.012 +0.004/−0.005) [src: Sect. 4.1, Eqs. 37–40]. For R² inflation the 95% range 49 < N_* < 59 is compatible with the basic prediction N_* = 54 [src: Sect. 4.2]. ACT reports η_V = (−95 +23/−30) × 10⁻⁴ (arXiv:2503.14454) [src]; ACT writes these definitions and relations as its Eqs. 7–8, sets n_t = −r/8, varies r in [0, 1] with BK18 B modes, and gets η_V for P-ACT-LB-BK18 at 68% (Eq. 9) [src: Sect. IV.4]. A model is compared with data through its predictions as a function of the number of e-folds N between horizon exit of the pivot scale and the end of inflation; N depends on reheating, which is why reheating enters every model comparison (section 1 of `open-questions.md`).

For Starobinsky R² inflation, Higgs inflation and the α-attractors, the leading-order formulas are n_s ≈ 1 − 2/N and r ≈ 12α/N² (α = 1 for Starobinsky): the superconformal α-attractors of Kallosh et al. 2013 converge to n_s = 1 − 2/N, r = 12α/N² at small α (large curvature of the Kähler manifold) and to chaotic-inflation predictions at large α (arXiv:1311.0472) [src]; the α = 1 class was introduced as a universality class of conformal inflation (Kallosh et al. 2013, arXiv:1306.5220). Higgs inflation needs a non-minimal coupling of the Higgs to gravity and no new particle (Bezrukov and Shaposhnikov 2008, arXiv:0710.3755). The formulas give n_s = 0.960 and 0.967 for N = 50 and 60, and r = 0.0048 and 0.0033 [der: direct evaluation of the formulas of arXiv:1311.0472]. Refined predictions beyond these approximations exist and shift the comparison with data (Drees and Xu 2025, arXiv:2504.20757).

The library ASPIC computes reheating-consistent predictions for 118 single-field models (Martin, Ringeval and Vennin 2014, arXiv:1303.3787) [src].

### What actually fixes n_s
<!-- key: what-actually-fixes-ns -->

The CMB measures n_s through the relative heights of the acoustic peaks and the damping tail, in combination with Ω_b h² and Ω_c h². In Planck n_s and Ω_b h² are positively correlated, in ACT anti-correlated, so the combination breaks the degeneracy and moves n_s (arXiv:2503.14452). CMB data also carry a degeneracy between n_s and the parameters that BAO constrain, so a BAO data set in tension with the CMB shifts n_s (Ferreira et al. 2025, arXiv:2507.12459). This is the mechanism behind the "ACT n_s shift" in `results.md`, section 1.

### Model-independent reconstruction
<!-- key: model-independent-reconstruction -->

- Binned spectrum: ACT DR6 fits e^(−2τ) P_R(k) in 30 bins, adding 28 parameters to ΛCDM; neighbouring bins are correlated at 30–40% (arXiv:2503.14454) [src]. The quantity constrained is e^(−2τ) P_R, not P_R: the amplitude is degenerate with the optical depth.
- Planck 2018 used several non-parametric reconstructions and two methods of reconstructing the inflaton potential (arXiv:1807.06211).
- Knot reconstruction from galaxy clustering: N knots interpolated in (log k, log P_R), with a seven-parameter model absorbing broadband and BAO effects, to k = 0.3 h Mpc⁻¹ (Martínez-Somonte et al. 2026, arXiv:2605.18615) [src].

### Running from the Lyα forest
<!-- key: running-from-the-lyalpha-forest -->

The 1D flux power spectrum constrains the amplitude and slope of the linear spectrum near k of order 1 Mpc⁻¹ at z of about 3; combined with the CMB it gives the longest lever arm on α_s (arXiv:1911.09073, arXiv:2601.21432). Estimators, emulators and nuisance parameters are in `cosmo-lyman-alpha`.

## 3. Tensor modes and B-mode polarisation
<!-- key: tensor-modes-and-b-mode-polarisation -->

### Observable (textbook, with the founding papers)
<!-- key: observable-textbook-with-the-founding-papers -->

CMB linear polarisation decomposes into a curl-free E component and a curl B component. Scalar perturbations produce no B modes at linear order, tensor perturbations do, so B modes are not limited by the scalar cosmic variance (Seljak and Zaldarriaga 1997, arXiv:astro-ph/9609169; Kamionkowski, Kosowsky and Stebbins 1997, arXiv:astro-ph/9609132). The tensor-to-scalar ratio is r = P_t(k_*)/P_R(k_*). Graviton creation during inflation (Rubakov 1982, doi:10.1016/0370-2693%2882%2990641-4) and its constraints on inflationary models (Abbott 1984, doi:10.1016/0550-3213%2884%2990329-8) are the classic tensor references; both were confirmed on Crossref, not read. The primordial BB spectrum has a bump at degree scales from recombination and one at the largest angular scales from reionisation; ground-based experiments target the first, satellites both (arXiv:1510.06042; the LiteBIRD requirements are specified over both the reionisation and the recombination multipole ranges, arXiv:2607.25285).

What a detection would mean: observable tensor modes require an inflaton excursion of at least the Planck scale and, for the signal levels discussed in 1996, V^(1/4) = (2–4) × 10¹⁶ GeV (Lyth 1997, arXiv:hep-ph/9606387) [src]. This "Lyth bound" is why r separates large-field from small-field models.

### Contaminants that set the method
<!-- key: contaminants-that-set-the-method -->

1. Lensing B modes: E modes lensed by large-scale structure. Detected at 7.0σ in the BICEP2/Keck × Planck analysis (arXiv:1502.00612) [src]. They act as noise on r and are reduced by delensing (below).
2. Galactic foregrounds: polarised dust at high frequency and synchrotron at low frequency. Every analysis is multi-frequency.
3. Instrumental temperature-to-polarisation leakage, and 1/f noise that sets the lowest usable multipole.

### BICEP/Keck-style likelihood
<!-- key: bicep-keck-style-likelihood -->

The BK18 analysis fits a multi-component parametric model to all auto- and cross-spectra between the BICEP/Keck maps at 95, 150 and 220 GHz and the WMAP and Planck maps, with seven foreground parameters and no external prior on the dust spectral index; the 220 GHz maps constrain polarised dust better than Planck 353 GHz does in that patch (arXiv:2110.00483) [src]. Cosmological parameters other than r are fixed. Tristram et al. 2022 instead free all six ΛCDM parameters and add Planck PR4 and BAO (arXiv:2112.07961).

What BK18 did, as read (arXiv:2110.00483) [src: main text, likelihood paragraph; App. D]: Hamimeche–Lewis likelihood (an approximation for correlated Gaussian fields on part of the sky that keeps the non-Gaussian form of the likelihood; arXiv:0801.0554) on 66 BB auto- and cross-spectra between BICEP/Keck, WMAP and Planck maps, nine bandpowers each over 20 < ℓ < 330; eight-parameter model (lensed ΛCDM + r + dust + synchrotron + noise) sampled with CosmoMC; bandpower covariance from 499 signal + noise simulations with signal–noise and BICEP/Keck–WMAP/Planck noise cross-terms set to zero; r at 0.05 Mpc⁻¹ with n_t = 0; lensing BB fixed to Planck 2018. Goodness of fit: χ² = 541.6 for 594 bandpowers, PTE 0.94 against simulations. The model parameters and priors are tabulated in `systematics.md`, section B9. SPT-3G 2019–2020 BB uses a BK18-like eight-component model on 95, 150 and 220 GHz spectra with the BK18 mask (f_sky = 0.010) or its own 1500 deg² mask (f_sky = 0.037) (arXiv:2505.02827) [src: Sects. IV.3, VI.1].

### Delensing
<!-- key: delensing -->

Foundations (abstracts read): lensing converts E into B and sets a floor; Knox et al. 2002 put the detectability limit, with lensing subtracted, at an energy scale of inflation of 3.2 × 10¹⁵ GeV (arXiv:astro-ph/0202286) [src]; Kesden et al. 2002 showed that higher-order correlations map the lensing and subtract its B modes, with arcminute resolution needed and a floor near 10¹⁵ GeV (arXiv:astro-ph/0202434) [src].

A lensing B-mode template is built from an estimate of the polarised CMB and a tracer of the projected mass (the Planck CIB map in the first demonstration), and enters the likelihood as an extra map. On BK14 data it reduced σ(r) from 0.024 to 0.022, about 10%, against 26% for a perfect template (arXiv:2011.08163) [src]. The SO forecast assumes 70% of the lensing B-mode power removed (arXiv:2512.15833) [src].

### Component separation for the next generation
<!-- key: component-separation-for-the-next-generation -->

The moment expansion was introduced by Chluba et al. 2017: spatial and line-of-sight averaging of emitting volumes distorts the foreground SED, which adds parameters to be measured or modelled (arXiv:1701.00274) [src]. SO uses a cross-spectrum parametric pipeline (BBPower) with a moment expansion to describe spatial variation of the dust spectral index (Liu et al. 2025, arXiv:2508.00073; Dachlythra et al. 2025, arXiv:2503.01791). Time-domain simulations with beam convolution are made with beamconv (arXiv:2503.01791).

### Quoting a limit
<!-- key: quoting-a-limit -->

Limits on r are 95% upper limits from a posterior with a flat prior on r ≥ 0 unless stated. SPIDER quotes both a Feldman–Cousins limit (0.11) and a Bayesian one (0.19) for the same data (arXiv:2103.13334) [src]: the construction must be named. The scale subscript (r_0.05 or r_0.002) must be copied.

## 4. Cosmic birefringence
<!-- key: cosmic-birefringence -->

A uniform rotation β of the polarisation plane between emission and observation mixes E and B: C_ℓ^EB = ½ sin(4β)(C_ℓ^EE − C_ℓ^BB), and similarly C_ℓ^TB = sin(2β) C_ℓ^TE (textbook). A miscalibration α of the detector polarisation angle produces the same signature, so EB alone measures α + β. The Lorentz- and parity-violating modification of electrodynamics behind the effect was bounded by Carroll 1990 (doi:10.1103/PhysRevD.41.1231; confirmed on Crossref, not read). Foundations (abstracts read): Lue et al. 1999 showed that parity-violating interactions leave a signature in CMB temperature and polarisation maps (arXiv:astro-ph/9812088); Feng et al. 2006 searched WMAP and BOOMERANG B03 data for a Chern–Simons rotation and found Δα = −6.0° ± 4.0° (1σ) (arXiv:astro-ph/0601095) [src]; Keating et al. 2013 argued that man-made calibrators are deficient for the angle precision B-mode searches need and proposed self-calibration (arXiv:1211.5734).

Three ways to break the degeneracy are in use:

1. Galactic foregrounds as a calibrator: the foreground emission is rotated by α only, the CMB by α + β, and their different multipole dependence separates the two; the method uses the observed EE − BB difference and needs no prior on the foreground EE and BB spectra (method: Minami et al. 2019, arXiv:1904.12440 [src]; first application: Minami and Komatsu 2020, arXiv:2011.11254). Weakness: any intrinsic EB of dust biases the result (arXiv:2201.07682).
2. Instrument-model priors on α: ACT uses priors from its optics model and marginalises over residual intensity-to-polarisation leakage (Diego-Palazuelos and Komatsu 2025, arXiv:2509.13654).
3. Hardware or cross-experiment calibration: a wire grid for the SO SATs, transferred to other experiments through cross-spectra (Rigouzzo et al. 2026, arXiv:2606.11300).

An experiment that calibrates its angle by nulling EB cannot measure a constant β; it can still measure a multipole-dependent β(ℓ) (BICEP/Keck XXI, arXiv:2603.06812) or an anisotropic rotation, which generates BB and is estimated with quadratic estimators or from the BB spectrum (arXiv:2510.07928, arXiv:2608.27458).

## 5. Primordial non-Gaussianity
<!-- key: primordial-non-gaussianity -->

### Definitions (textbook)
<!-- key: definitions-textbook -->

Local type: Φ(x) = φ(x) + f_NL^local [φ²(x) − ⟨φ²⟩], with φ Gaussian and Φ the primordial (Bardeen) potential; the bispectrum peaks in squeezed triangles (Komatsu and Spergel 2001, arXiv:astro-ph/0005036). Equilateral and orthogonal templates describe single-field models with derivative interactions; the pair spans the cubic operators of the effective field theory of inflation and maps to the sound speed c_s (Senatore, Smith and Zaldarriaga 2010, arXiv:0905.3746).

As Planck 2018 writes them (arXiv:1905.05697) [src: Sects. 2.1–2.2, Eqs. 1–3]: Φ ≡ (3/5) ζ on super-horizon scales, with ζ the comoving curvature perturbation, and P_Φ(k) = A/k^(4−n_s). Then

- B_Φ^local(k_1, k_2, k_3) = 2 f_NL^local [P_Φ(k_1) P_Φ(k_2) + P_Φ(k_1) P_Φ(k_3) + P_Φ(k_2) P_Φ(k_3)] = 2A² f_NL^local [1/(k_1^(4−n_s) k_2^(4−n_s)) + cycl.] (Eq. 3), peaking for k_1 ≪ k_2 ≈ k_3;
- B_Φ^equil = 6A² f_NL^equil {−1/(k_1^(4−n_s) k_2^(4−n_s)) − 2 perms. − 2/(k_1 k_2 k_3)^(2(4−n_s)/3) + [1/(k_1^((4−n_s)/3) k_2^(2(4−n_s)/3) k_3^(4−n_s)) + 5 perms.]} (Eq. 1);
- B_Φ^ortho has the same structure with coefficients −3, −8 and +3 (Eq. 2).

The templates are taken from Creminelli et al. 2006, Chen et al. 2007 and Senatore et al. 2010 (as cited there). Foundations, abstracts read: Babich et al. 2004 sorted models into two nearly orthogonal classes, non-Gaussianity generated at horizon crossing (equilateral) and generated outside the horizon (squeezed, local) (arXiv:astro-ph/0405356); Creminelli et al. 2006 introduced the factorisable equilateral template and showed that with a mask or inhomogeneous noise the optimal estimator needs a term linear in the data, giving −366 < f_NL^equil < 238 (95%) from WMAP (arXiv:astro-ph/0509029) [src]; Chen et al. 2007 showed that for P(X, φ) Lagrangians the bispectrum is fixed by five parameters and grows at small sound speed (arXiv:hep-th/0605045); the effective field theory of inflation (Cheung et al. 2008, arXiv:0709.0293) is the framework in which the equilateral–orthogonal basis is defined. DBI inflation gives f_NL^equil ∝ c_s⁻² for c_s ≪ 1; in the quadratic curvaton f_NL^local = 5/(4r_D) − 5r_D/6 − 5/3 [src: Sects. 2.1–2.2]. The general definition f_NL(k_1, k_2, k_3) = B_Φ/(2[P_Φ(k_1)P_Φ(k_2) + 2 perms.]) is used for scale-dependent (running) non-Gaussianity [src: Sect. 2.4.1].

What the shapes test:

- Single-field slow-roll inflation predicts a local bispectrum fixed by the tilt, of order (1 − n_s) (Maldacena 2003, arXiv:astro-ph/0210603), and the squeezed limit is fixed for any single-field model whatever the Lagrangian (Creminelli and Zaldarriaga 2004, arXiv:astro-ph/0407059). A detection of |f_NL^local| of order one would rule out all single-field models. The SPHEREx mission paper summarises the target as |f_NL^local| < 10⁻² for single-field and about 1 for multi-field models (arXiv:2511.02985) [src].
- f_NL^equil and f_NL^ortho test the interactions and sound speed of the inflaton.
- "Cosmological collider" templates carry oscillations that encode the mass and spin of heavy fields (arXiv:2511.17500).

### CMB bispectrum estimators
<!-- key: cmb-bispectrum-estimators -->

- KSW: a cubic statistic that reduces the cost from N^2.5 to N^1.5 operations for separable templates (Komatsu, Spergel and Wandelt 2005, arXiv:astro-ph/0305189) [src].
- Linear term: needed for optimality with a mask or anisotropic noise (Creminelli et al. 2006, arXiv:astro-ph/0509029); WMAP 3-year gave −36 < f_NL^local < 100 and −256 < f_NL^equil < 332 at 95% (arXiv:astro-ph/0610600) [src].
- Binned estimator: binning in harmonic space generalises KSW with adjustable weights against foregrounds (Bucher et al. 2010, arXiv:0911.1642). Modal estimator: expansion of non-separable bispectra on separable polynomial modes (Fergusson et al. 2010, arXiv:0912.5516).
- Planck uses three estimators in parallel, separable template fitting (KSW), binned and modal, and requires agreement (arXiv:1502.01592, arXiv:1905.05697). PR4 was analysed with the binned and the integrated-bispectrum estimators (arXiv:2504.00884).
- Errors and the linear correction term come from simulations (600 for PR4, arXiv:2504.00884). The lensing–ISW bispectrum and point-source bispectra are fitted jointly or subtracted.
- Planck 2018 set-up (arXiv:1905.05697) [src: Sects. 3.2.1–3.2.2]: SMICA, SEVEM, NILC and Commander maps, 5 arcmin beam; common masks with f_sky = 0.779 (T) and 0.781 (E), diffusively inpainted (2000 iterations); T over 2 ≤ ℓ ≤ 2000 (KSW, modal) or 2500 (binned); E over 4 ≤ ℓ ≤ 1500 (2000 binned), ℓ = 2, 3 removed because they biased local f_NL in simulations; 300 FFP10 noise realisations (160 for modal) for errors and linear terms; a 3% (T, ℓ ≈ 2000) and percent-level (E) noise mismatch between FFP10 and data is shown to be harmless; templates and lensing bias from CAMB at the Planck 2018 best fit. Final numbers: KSW on SMICA with the predicted lensing bias subtracted [src: Sect. 5.1].
- Non-separable models: modal decompositions (the Modal pipeline, arXiv:2511.17500) or a learned separable basis in the PolySpec code, with model bispectra computed by CosmoFlow (Philcox, Zhong and Sirletti 2025, arXiv:2511.19179).

### Scale-dependent bias (large-scale structure)
<!-- key: scale-dependent-bias-large-scale-structure -->

Local non-Gaussianity couples long and short modes and adds a term to the bias of any tracer that grows as 1/k² on large scales (Dalal et al. 2008, arXiv:0710.4560; Slosar et al. 2008, arXiv:0805.3580); Matarrese et al. 2008 derived it analytically from the clustering of high peaks at large separation (arXiv:0801.4826). In the standard form (textbook):

Δb(k, z) = b_φ f_NL / α(k, z), with α(k, z) = 2 c² k² T(k) D(z) / (3 Ω_m H_0²), and b_φ = 2 δ_c (b_1 − p),

where δ_c ≈ 1.686 is the spherical-collapse threshold, T(k) the transfer function and D(z) the growth factor normalised to the scale factor in matter domination. The data constrain the product f_NL · b_φ only (Barreira 2022, arXiv:2205.05673).

As DESI DR1 writes it (arXiv:2411.17623) [src: Sect. 2, Eqs. 2–4, 7]: P(k, z) = [b_1(z) + b_Φ(z) f_NL^loc / T_Φ→δ(k, z)]² P_lin(k, z), with T_Φ→δ = (P_lin/P_Φ)^(1/2), P_Φ(k) = (9/25)(2π²/k³) A_s (k/k_pivot)^(n_s−1), k_pivot = 0.05 Mpc⁻¹, Φ normalised to (3/5)R, so that T_Φ→δ ∝ k² T(k); and b_Φ = 2δ_c (b_1 − p) with δ_c = 1.686.

The parameter p encodes the response of the tracer: p = 1 for a universal mass function, p = 1.6 for objects that live in recent mergers (derived with extended Press–Schechter for quasars, arXiv:0805.3580), about 1.4 for DESI-like quasars selected in IllustrisTNG (Fondi et al. 2026, arXiv:2602.12357). Assembly bias changes b_φ at fixed b_1 and can change its sign (Lazeyras et al. 2023, arXiv:2209.07251).

Estimation practice:

- Power spectrum monopole (and quadrupole) at the largest scales with FKP-type weights. Optimal redshift weights that follow the evolution of the signal improved eBOSS constraints by 15% (DR14, arXiv:1904.08859), 37% (DR16, arXiv:2106.13725) or 10% (arXiv:2309.15814) [src].
- The window function and the integral constraints dominate the modelling at the scales that carry the signal: DESI corrects the window for the radial integral constraint and adds an angular integral-constraint term for the imaging-systematics mitigation (arXiv:2411.17623).
- Configuration space with simulation-based modelling (arXiv:2606.24651); cross-spectra between tracers to cancel non-common systematics (arXiv:2604.05213); cross-correlation with CMB lensing, whose noise and systematics are independent of the galaxy auto-spectrum (arXiv:2504.20992, arXiv:2512.17865).
- kSZ velocity reconstruction gives a second tracer of the same modes (arXiv:2506.21657); see `cosmo-cmb-lss-cross-correlations`.

### Galaxy bispectrum
<!-- key: galaxy-bispectrum -->

Equilateral and orthogonal shapes do not produce a 1/k² bias and need the bispectrum. Current analyses fit the redshift-space power spectrum and bispectrum with the one-loop effective field theory of large-scale structure, varying bias and counterterm parameters (Cabass et al. 2022, arXiv:2201.07238; D'Amico et al. 2022, arXiv:2201.11518; Chudaykin, Ivanov and Philcox 2025, arXiv:2512.04266). The result depends strongly on whether bias parameters are free, fixed, or given simulation-based priors: the BOSS equilateral error goes from 600 to 300 when quadratic bias and cosmology are fixed (arXiv:2201.07238) [src]. Estimators and EFT details are in `cosmo-beyond-two-point` and `cosmo-galaxy-clustering`.

Field-level inference with BORG is forecast to reach σ(f_NL^local) = 2.3 on Euclid-like data (**forecast**, arXiv:2507.15819) [src].

### Abundance of rare objects
<!-- key: abundance-of-rare-objects -->

Non-Gaussianity changes the high-mass tail of the halo mass function (arXiv:0710.4560). Cluster counts probe 5–10 h⁻¹Mpc scales that neither the CMB bispectrum nor scale-dependent bias reach, with a much larger error (arXiv:2602.03917).

## 6. Isocurvature
<!-- key: isocurvature -->

The general regular primordial perturbation has, besides the adiabatic mode, four isocurvature modes: CDM density (CDI), baryon density (BDI), neutrino density (NDI) and neutrino velocity (NVI) (Bucher, Moodley and Turok 2000, arXiv:astro-ph/9904231). BDI and CDI are indistinguishable in the CMB up to a rescaling (arXiv:2503.14454).

Parametrisation used by Planck and ACT: three power-law spectra P_RR, P_II, P_RI specified by amplitudes at k_1 = 0.002 and k_2 = 0.1 Mpc⁻¹, sampled with flat priors on the amplitudes to avoid the prior-volume effect that a flat prior on a tilt produces when the amplitude is unconstrained (arXiv:2503.14454). Derived quantities: β_iso(k) = P_II/(P_RR + P_II) and the non-adiabatic fraction of the temperature variance α_non-adi (arXiv:1807.06211). Special cases: uncorrelated scale-invariant CDI ("axion"), fully correlated or anti-correlated CDI ("curvaton"), and compensated baryon–CDM isocurvature. Axion models with a range of spectral tilts are fitted in arXiv:2606.11312.

Theory codes: ACT uses CLASS, and notes that the HMCode non-linear correction can fail for strongly blue-tilted isocurvature spectra (fewer than 1% of samples, in the Planck-only chains) (arXiv:2503.14454) [src].

## 7. Spatial curvature
<!-- key: spatial-curvature -->

The primary CMB fixes the angular acoustic scale and leaves a geometric degeneracy between Ω_K, Ω_m and H_0 (degeneracies among CMB parameters analysed by Efstathiou et al. 1999, arXiv:astro-ph/9807103, who also showed that a Fisher matrix can overestimate the errors). It is broken weakly by CMB lensing, both through the smoothing of the peaks and through the lensing reconstruction, and strongly by BAO (arXiv:1807.06209). Because closed models predict more lensing, a preference for extra peak smoothing (A_L > 1) appears as a preference for Ω_K < 0 (arXiv:1807.06209, arXiv:1911.02087). Late-time-only determinations use BAO with supernovae, lensing time delays or cosmic chronometers and depend on the dark-energy model assumed (arXiv:2512.19565, arXiv:2604.23492).

## 8. Primordial features
<!-- key: primordial-features -->

Templates multiply the power-law spectrum by 1 + A cos(ω k + φ) (linear) or 1 + A cos(ω ln(k/k_*) + φ) (logarithmic), with variants for localised features and for particle production (arXiv:1505.01834, arXiv:2606.28310). The two classic origins (abstracts read): a sharp step in the inflaton potential produces localised k-dependent oscillations whose amplitude and extent depend on the size and gradient of the step (Adams et al. 2001, arXiv:astro-ph/0102236); periodic instanton modulations in axion monodromy inflation produce resonant, logarithmically spaced oscillations (Flauger et al. 2010, arXiv:0907.2916). Method points:

- The posterior in frequency is multimodal. Nested or sequential Monte Carlo samplers are used; Nerval et al. integrate the pocoMC sampler into Cobaya (arXiv:2606.28310).
- Rapid oscillations are erased by binning, so CMB searches use unbinned likelihoods (arXiv:2605.30236).
- The significance must be global: the best frequency is chosen from many, and the look-elsewhere correction reduces Δχ² = −10 to −15 to at most 2.6σ in Planck (arXiv:2605.30236) [src].
- In galaxy clustering, oscillations are damped by non-linear evolution like the BAO and are modelled with the same resummation; Chen et al. use Lagrangian EFT for the power spectrum and bispectrum (arXiv:1906.08758, arXiv:2610.10530).
- Frequencies close to the BAO frequency are degenerate with the BAO, and a search at fixed cosmology can turn a distance-scale mismatch into a feature (arXiv:2610.10530).

## 9. Covariance, likelihood and blinding practice
<!-- key: covariance-likelihood-and-blinding-practice -->

| Analysis | Covariance and likelihood | Blinding | Citation |
|---|---|---|---|
| BICEP/Keck r | Hamimeche–Lewis likelihood on 66 BB spectra, 20 < ℓ < 330; covariance from 499 signal + noise simulations [src: BK18 main text]; extended to accept a lensing template | not read this session | arXiv:2110.00483, arXiv:2011.08163 |
| SPT-3G BB | foreground-marginalised "CMB-lite" compression, public | not read | arXiv:2510.07928 |
| Planck f_NL | simulation-based errors; three estimators cross-validated; stability across component-separation methods | not stated in the abstracts | arXiv:1905.05697 |
| DESI DR1 f_NL | covariance from 1000 EZmocks; window with radial and angular integral constraints; P_0 + P_2, k = 0.003 (QSO) or 0.006 (LRG) to 0.08 h Mpc⁻¹ [src: Sects. 3.3, 4.2.1] | blinded, "for the first time in this kind of analysis": catalogue-level weights add f_NL^blind ∈ [−15, 15], built with p = 1, multiplied into the completeness weights [src: Sect. 3.1.3, Eq. 9] | arXiv:2411.17623 |
| eBOSS DR16 f_NL | EZmock catalogues reproducing the target selection; monopole to k = 0.121 h Mpc⁻¹, NGC and SGC nuisances [src: Table 1] | not stated | arXiv:2106.13725 |
| ACT DR6 and SPT-3G D1 power spectra | see `cosmo-cmb` | both blinded, both changed after unblinding, per the `cosmo-cmb` skill [sec] | arXiv:2503.14452, arXiv:2506.20707 |
| Birefringence | Gaussian likelihood on EB (and TB) bandpowers with α and β sampled jointly; ACT DR6: five array-bands, Gaussian optics priors on each α_i, full bin-to-bin covariance from the DR6 release, iterative semi-analytic posterior in the small-angle limit [src: arXiv:2509.13654, Sect. III, Eqs. 1–3] | not stated | arXiv:2011.11254, arXiv:2509.13654 |

Significances in this domain are usually conditional: on the b_φ relation (f_NL from large-scale structure), on instrumental priors (birefringence), on a fixed cosmology (features), on the model (n_s, Ω_K). `systematics.md` lists the condition for each.

## 10. Public codes and pipelines
<!-- key: public-codes-and-pipelines -->

| Code | Purpose | Reference |
|---|---|---|
| ASPIC | reheating-consistent slow-roll predictions for 118 models | arXiv:1303.3787 |
| CLASS, CAMB (through Cobaya) | Boltzmann codes for all analyses; the CMB-HD likelihood and Fisher codes support both | arXiv:2609.35964 |
| Cobaya + pocoMC | sampling of multimodal feature posteriors | arXiv:2606.28310 |
| BBPower | cross-spectrum parametric component separation for SO | arXiv:2508.00073, arXiv:2503.01791 |
| beamconv | beam-convolved time-domain simulations | arXiv:2503.01791 |
| candl_data likelihoods | foreground-marginalised SPT-3G D1 and SPTpol BB | arXiv:2510.07928 |
| KSW, binned, modal estimators | CMB bispectrum | arXiv:astro-ph/0305189, arXiv:1905.05697 |
| PolySpec, CosmoFlow | CMB polyspectra estimators; numerical inflationary correlators | arXiv:2511.19179 |
| BORG | field-level inference of f_NL | arXiv:2507.15819 |

## 11. Conventions and where the community is split
<!-- key: conventions-and-where-the-community-is-split -->

- **Pivot.** n_s and α_s at k_* = 0.05 Mpc⁻¹; r at 0.05 Mpc⁻¹ (BICEP/Keck, ACT) or 0.002 Mpc⁻¹ (Planck 2018). Isocurvature amplitudes at 0.002, 0.05 and 0.1 Mpc⁻¹. Units are Mpc⁻¹ without h, except in galaxy-clustering papers.
- **Sign of Ω_K.** Ω_K = 1 − Ω_tot: negative for a closed universe. "Negative curvature" in words means an open universe, Ω_K > 0; arXiv:2607.28445 uses both phrasings in one sentence.
- **f_NL.** The local, equilateral and orthogonal amplitudes are different parameters and must carry their superscript. Large-scale-structure values depend on p (or b_φ). The sign and normalisation convention of f_NL differs between some older large-scale-structure papers and the CMB convention; the conversion factor was not read this session (see "Not verified").
- **Confidence levels.** r limits are 95%; f_NL, n_s, Ω_K, β are 68% intervals; isocurvature limits are one-tail 95%; eBOSS DR14 f_NL intervals are 95% while DR16 ones are 68%.
- **β.** Degrees, positive for the sign found by all current analyses; the sign convention relative to the IAU or HEALPix polarisation convention was not checked.
- **Names of CMB combinations.** P-ACT, P-ACT-LB, CMB-SPA, "CMB-PAS" and DESI's "CMB" differ (see `surveys-and-data.md`, section 2).
- **Slow-roll parameters.** Potential (ε_V, η_V) versus Hubble-flow (ε_1, ε_2, …) definitions differ at second order; check which one a paper fits.
- **Split on b_φ.** DESI collaboration papers fix or tightly prior p (arXiv:2411.17623, arXiv:2606.24651); Barreira argues that f_NL · b_φ is the only quantity measured and that wide priors on b_φ bias the result through projection effects (arXiv:2205.05673); simulation-based priors are the proposed middle way (arXiv:2602.12357).
- **Split on what n_s to compare with models.** CMB + BAO in ΛCDM (ACT practice), CMB only (arXiv:2507.12459), or extended models (arXiv:2607.28445, arXiv:2609.35964).

## 12. Not verified
<!-- key: not-verified -->

- The conversion between the "LSS" and "CMB" conventions for f_NL.
- The map from (f_NL^equil, f_NL^ortho) to (c_s, c̃_3): not read, only the resulting c_s limits (the templates themselves are now in section 5).
- BICEP/Keck blinding practice: not read (the BK18 covariance construction now is, section 3).
- The multipoles of the recombination and reionisation bumps and the relation between r and the energy scale of inflation: standard, but no number was read this session, so none is given.
