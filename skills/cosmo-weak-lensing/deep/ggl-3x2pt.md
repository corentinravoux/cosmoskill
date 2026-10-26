# Galaxy–galaxy lensing in 3×2pt — cosmo-weak-lensing dossier

Scope: how the galaxy–galaxy lensing part of a 3×2pt analysis is built
step by step (lens sample and its n(z), the tangential-shear or ΔΣ
estimator and its corrections, the model terms, the treatment of the
non-local small-scale mass, the scale cuts), how to choose between the
variants in use, and the tests that caught failures in DES, KiDS, HSC and
the DESI DR1 combinations.
Snapshot: 2026-10-18.
From: Pantos 2026 review (arXiv:2602.12238), Sects. 4.2 and 6.6; DES Y6
3×2pt key papers (arXiv:2601.14559, arXiv:2601.15175, arXiv:2601.14833).

Already in L2, not repeated here: the definitions of γ_t, ΔΣ and 3×2pt and
the foundation papers (`physics-and-methods.md#what-is-measured`); the γ_t
Hankel relation (`physics-and-methods.md#estimators`); the DES Y6 R_min
values and the linear or non-linear bias choice
(`physics-and-methods.md#theory-model-of-a-current-analysis`); the DES Y6
magnification coefficients, the factor-2 notation clash and the
magnification share of the S8 width
(`systematics.md#other-effects-a-complete-analysis-treats`); the cross-survey
ΔΣ comparison and "lensing is low" (`open-questions.md#lensing-is-low`);
the 3×2pt results (`results.md#3x2pt-and-multi-probe`). Shear calibration
and IA modelling have their own dossiers (`deep/shear-calibration.md`,
`deep/intrinsic-alignments.md`); the posterior-predictive metric Δ_PPD is
computed in `cosmo-statistics-inference/deep/tension-metrics.md`.

Symbols. γ_t, γ_×: tangential and cross shear around a lens; e_t: tangential
ellipticity of a source; w_l, w_s, w_r: lens, source and random weights;
B(θ): boost factor; ⟨R⟩: mean metacalibration or metadetection response of
a source bin; Σ_crit: critical surface density; ΔΣ(R) = Σ̄(<R) − Σ(R):
excess surface density at projected radius R; b₁, b₂: linear and quadratic
galaxy bias; α: magnification coefficient of a lens bin (notation below);
w(θ) or w_p(R): angular or projected clustering; "2×2pt": clustering plus
galaxy–galaxy lensing; "1×2pt": cosmic shear alone.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the lens sample
<!-- key: step-1-choose-the-lens-sample -->

Three kinds are in use.

- **Photometric, magnitude-limited (MagLim).** DES Y3 optimised the lens
  selection for 2×2pt and chose i < 4 z_phot + 18: about 30% wider n(z)
  than redMaGiC but about 3.5 times more galaxies, giving +40% in the
  figure of merit of (Ωm, w, σ8) pairs in wCDM and +19% and +27% on σ8 and
  Ωm in ΛCDM (Porredon et al. 2020, arXiv:2011.03411) [src]. A flat cut
  i < 22.2, seven times denser, did slightly worse [src]. DES Y6 MagLim++
  keeps a linear cut, 17.5 < i < 18 + 4 z_MEAN with the DNF photo-z, "to
  remove faint, high-redshift galaxies while preserving a roughly constant
  signal-to-noise ratio", adds an unWISE near-infrared star–galaxy
  separation and a SOM-based removal of colour-space regions contaminated
  by interlopers, and bins in DNF z_MEAN with edges 0.2, 0.4, 0.55, 0.7,
  0.85, 0.95, 1.05 over 4031 deg² of joint mask (Giannini et al. 2026,
  arXiv:2601.15175) [src: Sect. II.1, Eq. 1].
- **Photometric red galaxies (redMaGiC).** Tighter photo-z; in DES Y3 it
  failed the clustering–lensing consistency test (Step 7).
- **Spectroscopic lenses.** HSC Y3 uses three luminosity-cut, nearly
  volume-limited SDSS DR11 samples: LOWZ 0.15–0.35 with M_i − 5 log h <
  −21.5, CMASS1 0.43–0.55 (< −21.9) and CMASS2 0.55–0.70 (< −22.2), with
  n̄_g ≃ 1.8, 0.74, 0.45 × 10⁻⁴ (h⁻¹Mpc)⁻³; clustering is measured over
  about 8300 deg², lensing over the 416 deg² overlap (Sugiyama et al. 2023,
  arXiv:2304.00705) [src: Sect. II.2]. KiDS-1000 uses BOSS and 2dFLenS in
  two lens bins (Heymans et al. 2020, arXiv:2007.15632) [src: Sect. 2.4].
  The DESI DR1 combination uses five DESI lens bins, 0.1–0.2, 0.2–0.3,
  0.3–0.4, 0.4–0.6, 0.6–0.8, with clustering over the full DESI area and
  lensing cut to the overlap (Porredon et al. 2025, arXiv:2512.15960) [src:
  Sect. 3.2].

### Step 2. Calibrate the lens n(z)
<!-- key: step-2-calibrate-the-lens-n-z -->

With spectroscopic lenses the lens n(z) is taken from the redshifts
(arXiv:2304.00705) [src: Sect. III.1.2]. For DES Y6 MagLim++, SOMPZ gives
an ensemble of n(z), clustering redshifts (WZ) against spectroscopic
references reweight it by importance sampling, and the ensemble is
compressed into principal modes ranked by their χ² contribution to the
data vector; three modes per lens bin suffice, their amplitudes being
nuisance parameters (arXiv:2601.15175) [src: Sect. II.1]. The 3×2pt
analysis records that this replaced the "more ad hoc 'shift and stretch'
parametrization used in Y3" (DES Collaboration 2026, arXiv:2601.14559)
[src: App. A.2.2].

### Step 3. Measure γ_t
<!-- key: step-3-measure-gammat -->

DES writes the estimator in steps (Prat et al. 2021, arXiv:2105.13541):

1. Tangential ellipticity of each pair, e_t = −e₁ cos 2φ − e₂ sin 2φ [src:
   Eq. 1]; weighted mean over pairs, γ_t = Σ w_LS e_t / Σ w_LS with w_LS =
   w_l w_s, in 20 log bins over 2.5′–250′ (arXiv:2105.13541) [src: Eq. 2]. Lens weights remove
   correlations with observing conditions; the mean weighted ellipticity of
   each source bin, a few 10⁻⁴, is subtracted first [src: Sect. III.1,
   Table 2].
2. **Boost factor.** Sources that overlap the lens in redshift cluster
   around it and are unlensed, diluting the signal. B(θ) = 1 + ω_LS(θ) =
   (Σ_r w_r / Σ_l w_l)(Σ_LS w_LS / Σ_RS w_RS) [src: Eq. 4], so that the
   boosted estimator is the pair sum normalised by random–source pairs
   [src: Eq. 5]. The stated reason for measuring rather than modelling it:
   it is "independent of the estimated redshift distributions, and in
   particular of the tails", and it includes magnification of both samples
   [src: Sect. III.2].
3. **Random-point subtraction.** Additive shear cancels in the tangential
   frame only for isotropic source distributions and constant additive
   shear, which fail near edges and masks; subtracting γ_t around randoms
   removes this and a covariance term from using the overdensity field
   [src: Sect. III.3, Eq. 6]. DES Y3 uses 40 randoms per lens (arXiv:2105.13541) [src: Sect.
   III.3].
4. **Response.** Divide by the mean response ⟨R⟩ = Σ w_s R_s / Σ w_s of the
   source bin [src: Eqs. 17–18]. DES Y6 measures R by finite differences
   with an artificial shear of 0.01 (Δγ = 0.02) and uses one scalar,
   scale-independent mean per bin, 0.857, 0.868, 0.820, 0.692 (arXiv:2601.15175)
   [src: Sect. IV.5, Eq. 22, Table 3]; its final estimator is Eq. 23, the
   same form as the Y3 Eq. 18 [src: Sect. IV.6].

Choice of averaging: weighting per lens–source pair rather than averaging
per lens first is kept "because of the significant increase in S/N", at the
price of weighting lenses by their number of background sources, which
couples to source clustering and magnification (arXiv:2105.13541) [src:
Sect. V.3.2].

**ΔΣ instead of γ_t.** HSC Y3 measures ΔΣ(R) with a reference cosmology
Ωm^ref = 0.279 used to convert angles to R and to compute ⟨Σ_c⁻¹⟩, and
corrects the template inside the fit: R = [χ(z_l; C)/χ(z_l; C^ref)] R^ref,
Π = [E(z_l; C^ref)/E(z_l; C)] Π^ref, and ΔΣ multiplied by
f_ΔΣ = Σ w_ls ⟨Σ_c⁻¹⟩^{true,C}/⟨Σ_c⁻¹⟩^{est,C^ref} / Σ w_ls, which also
carries the residual photo-z shift Δz_ph (arXiv:2304.00705) [src: Sect.
III.2.2, Eqs. 21–23]. γ_t(θ) needs no such correction. The DESI DR1
combination measures γ_t in 15 log bins over 0.3′–300′ with the dsigma
code, correcting for m and for dilution by source photo-z errors
(arXiv:2512.15960) [src: Sect. 3.2].

**Harmonic space.** KiDS-1000 fits band powers of the galaxy–galaxy lensing
spectrum C_nε(ℓ), with B-mode band powers as a null test (arXiv:2007.15632)
[src: Sect. 2.4]. DES Y3 also ran pseudo-Cℓ 2×2pt for both lens samples
(Faga et al. 2024, arXiv:2406.12675) [src].

### Step 4. Write the model
<!-- key: step-4-write-the-model -->

The observed density–shear spectrum has four terms (arXiv:2601.15175) [src:
Eq. 7]: C_{δg E} = C_{δg κ} + C_{δg I_E} + C_{δμ κ} + C_{δμ I_E}, i.e.
lensing, lens density × source IA (GI), lens magnification × shear, and
magnification × IA. In DES Y6 the IA term is negative for bins that overlap
in redshift, magnification grows with lens redshift and "can exceed the IA
term in several bins", and the mixed term is negligible [src: Sect. III].
DES projects with the curved-sky Legendre sum γ_t^{ij}(θ) = Σ_ℓ (2ℓ+1)/(4π
ℓ(ℓ+1)) P²_ℓ(cos θ) [C_gm^{ij}(ℓ) + 2(α^i − 1) C_mm^{ij}(ℓ)]
(arXiv:2105.13541) [src: Eq. 39], averaged over the angular bin.

- **Galaxy bias.** Linear, P_gm = b₁ P_mm (arXiv:2601.15175) [src: Eq. 6];
  or non-linear: DES Y6 adds b₂ per lens bin with two further terms fixed by
  relations to b₁ (arXiv:2601.14559) [src: Sect. V.1.2]. KiDS-1000 uses the
  perturbative model of Sánchez et al. 2017 extrapolated beyond k = 0.3
  h/Mpc by fitted polynomials, P_gm = b₁ P_m,nl + {b₂ F_b₂ − γ₂ F_γ₂ − γ₃⁻
  F_γ₃⁻} P²_m,lin, because "high-k scales will contribute to all angular
  scales at some level" (arXiv:2007.15632) [src: Eq. 6]. HSC's minimal bias
  model is ΔΣ_gG(R) = b₁ ρ̄_m0 ∫ k dk/2π P^NL_mm(k) J₂(kR) at one
  representative lens redshift (0.26, 0.51, 0.63), within 4% of the
  statistical error of the bin-averaged signal (arXiv:2304.00705) [src:
  Eq. 5, Sect. III.1.1].
- **Magnification.** δ_g^mag = C κ_l with C = C_area + C_sample and C_area =
  −2 (DES Y6 magnification paper, Legnani et al. 2026, arXiv:2601.14833)
  [src: Eq. 11]; for a pure magnitude cut C_sample = 2α with α = 2.5 d log₁₀
  N(<m)/dm at the cut [src: Eqs. 12–13]. The Y3 papers write C_total =
  2(α − 1) with α = C_flux/2 (arXiv:2105.13541) [src: Sect. IV.3]; that is
  why the Y6 3×2pt prior table lists α ≈ 1.6–2.4 while the magnification
  paper quotes C_sample ≈ 3.2–4.9. (The footnote of arXiv:2601.14833 as
  rendered writes "α = 2C_sample"; the tabulated values and the Y3
  definition both give α = C_sample/2.) Y6 measures C_sample by re-running
  Balrog injections with a constant δμ = 1.02 (δκ ≈ 0.01), "large enough"
  for precision and small enough that κ² terms stay at 10⁻⁴, and checks it
  by perturbing data magnitudes by Δm = −2.5 log₁₀(1 + 2δκ) with the
  photo-z shift propagated through the DNF fit coefficients [src: Sects.
  IV.1–IV.2, Eqs. 26–27].
- **Source magnification and source clustering.** Not in the DES Y3 model;
  tested by n_s(χ) → n_s(χ)[1 + δ_s][1 + C_s κ]: Δχ² = 1.8 (1.3 with
  point-mass marginalisation) and 0.128σ in Ωm–S8, with the remark that
  it may matter for Y6 (arXiv:2105.13541) [src: Sect. V.3.2, Eqs. 55–56].
  The source-clustering × IA term is absorbed by b_TA of TATT [src: Sect.
  V.3.2].

### Step 5. Remove the non-local small-scale mass
<!-- key: step-5-remove-the-non-local-small-scale-mass -->

γ_t(θ) = ΔΣ/Σ_crit carries all mass inside θ, which is why DES Y1 cut
galaxy–galaxy lensing at 12 h⁻¹Mpc against 8 for clustering
(arXiv:2105.13541) [src: Sect. IV.2]. Point-mass (PM) marginalisation adds
A^{ij}/θ² with A^{ij} ≈ B^i β_ij, β_ij = ∫dz_l ∫dz_s n_l^i n_s^j Σ_crit⁻¹
D⁻²(z_l), one enclosed mass B^i per lens bin under a narrow-bin assumption
[src: Eqs. 29–32]. With a Gaussian prior σ_B the covariance gains
σ²_B β_ij β_i'j' /(θ² θ'²) for i = i' [src: Eq. 33]; DES takes σ_B → ∞
"because for the chosen scale cuts of 6 Mpc/h the point-mass is dominated
by the 2-halo regime", giving C⁻¹_{+PM} = C⁻¹ − C⁻¹V(VᵀC⁻¹V)⁻¹VᵀC⁻¹ with V
the N_d × N_lens matrix of β_ij/θ² [src: Eq. 34]. The PM term cannot be
drawn on a data-vector plot, since it acts on the inverse covariance
(arXiv:2601.15175) [src: Fig. 2 caption]. DES Y6 keeps one parameter per
lens bin (thin-lens approximation) on the strength of Y3 tests
(arXiv:2601.15175) [src: Sect. III]; the DESI DR1 combination reuses the
DES Y3 implementation and priors (arXiv:2512.15960) [src: Sect. 3.1.2].

### Step 6. Set the scale cuts
<!-- key: step-6-set-the-scale-cuts -->

The procedure common to DES Y3, DES Y6 and DESI DR1: build a synthetic data
vector with an unmodelled effect (non-linear bias from one-loop PT or HEFT,
baryons from OWLS or other hydro runs), fit it with the baseline model, and
cut until the shift is below 0.3σ in (S8, Ωm) (arXiv:2105.13541 [src: Sect.
V.1]; arXiv:2601.15175 [src: Sect. III]; arXiv:2512.15960 [src: Sect.
3.5]). In Y6 this gives 24.3′, 17.6′, 13.0′, 10.9′, 9.7′, 8.7′ for the six
lens bins at 6 h⁻¹Mpc and 16.2′ to 5.9′ at 4 h⁻¹Mpc; θ_max = 250′ although
measurements reach about 1000′, because the extra range gave only a
marginal gain and large-scale systematics were not demonstrably controlled
(arXiv:2601.15175) [src: Sect. III]. HSC sets the maximum ΔΣ radius where
the cross signal ΔΣ_× is not significant: R = 12–30, 12–40, 12–80 h⁻¹Mpc
for LOWZ, CMASS1, CMASS2, and w_p over 8–80 h⁻¹Mpc to exclude BAO
information, 74 points in all (arXiv:2304.00705) [src: Sect. III.4].
KiDS-1000 removes the overlapping lens–source pairs (L1–S1, L2–S1 to S3)
because NLA with non-linear bias is "arguably rudimentary" there and these
pairs "carry little cosmological information", and for the others sets
ℓ_max where k > 0.3 h/Mpc becomes significant (arXiv:2007.15632) [src: Sect.
2.4].

### Step 7. Combine and test consistency
<!-- key: step-7-combine-and-test-consistency -->

Fit 1×2pt, 2×2pt and 3×2pt and compare. DES Y6 finds ξ± and 2×2pt
consistent at Δ_PPD = 0.049 although the 2D contours "appear somewhat
offset", and notes that for "two highly covariant data sets, there is no a
priori expectation" that the joint posterior projection be centred between
them (arXiv:2601.14559) [src: Sect. V.1.1]. The shear-ratio test uses the
small scales the 3×2pt discards (row "Shear ratio, Y6" under Numbers).

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

| Choice | Assumes | Buys | Costs | Who | Compared |
|---|---|---|---|---|---|
| MagLim vs redMaGiC lenses | photo-z of a magnitude-limited sample adequate | ×3.5 galaxies; +40% FoM (forecast setup) | 30% wider n(z); selection by photo-z exposes filter transitions | DES Y3, Y6 | redMaGiC Y3 failed X_lens; MagLim Y3 consistent with X_lens = 1 (arXiv:2105.13545) [src: Sect. V.4] |
| Spectroscopic lenses | overlap area enough | exact lens n(z); ΔΣ in physical units | small overlap (416 deg² HSC Y3, arXiv:2304.00702 [src: abstract]); reference-cosmology correction | HSC Y3, KiDS-1000, DESI DR1 | three shear surveys on DESI lenses consistent (arXiv:2512.15960) [src] |
| Linear vs non-linear bias | perturbative bias valid to 4 h⁻¹Mpc | DES Y6: < 10% on S8, +14% FoM; DES Y3 redMaGiC 2×2pt: 17% (arXiv:2105.13545) [src] | prior-volume shifts ≈ 0.5σ vs ≈ 0.2σ (arXiv:2601.14559) [src: Sect. V.1.2]; compute | DES Y6 fiducial linear "because the gain ... is not sufficient to justify the added computational complexity" [src] | means equal, 0.789 both [src: Eqs. 21–22] |
| PM marginalisation vs larger cuts | non-locality is a 1/θ² mode | ≈ 1.3 × tighter S8 for LSST Y1 2×2pt (**forecast**) (Prat et al. 2022, arXiv:2212.03734) [src] | S/N 55 → 28 (redMaGiC), 67 → 32 (MagLim) in Y3 (arXiv:2105.13541) [src: Sect. IV.2] | DES Y3, Y6, DESI DR1 | Υ statistic, Y-transform, "project-out": equivalent posteriors on LSST Y1 synthetic and DES Y3 data; only the removal of the 1/R² mode matters [src: arXiv:2212.03734, Sect. 5] |
| PM with geometric information (one B^i per lens bin) | enclosed mass constant across the lens bin | tighter TATT parameters, especially b_TA | "slightly biased" for LSST Y1; must be retested on stronger data [src: arXiv:2212.03734, Sect. 5] | DES Y3, Y6 | — |
| Boost measured vs modelled | — | independent of n(z) tails | needs randoms and jackknife errors | DES | Δχ² of omitting it: 9.8 (MagLim) all scales, 0.2 above 6 h⁻¹Mpc (arXiv:2105.13541) [src: Table 3]; Y6 ≈ 1–2 after cuts (arXiv:2601.15175) [src: Sect. V.5] |
| Overlapping lens–source bins: model or drop | IA × bias model adequate | IA self-calibration, more pairs | IA model risk | DES models them; KiDS-1000 drops them; HSC Y3 selects sources with photo-z > 0.75 (arXiv:2304.00704) [src: abstract] | — |
| Magnification priors from Balrog vs free | image simulation reproduces selection | tight α | data may prefer another amplitude | DES | Y3: free α preferred a different amplitude; lens cross-clustering allows uninformative priors "without any loss of constraining power" (arXiv:2209.09782) [src] |
| γ_t vs ΔΣ vs band powers | — | γ_t: no cosmology in the measurement; ΔΣ: physical scales; band powers: E/B split | ΔΣ: reference-cosmology factor; band powers: k-leakage | DES / HSC / KiDS-1000 | — |
| Scalar vs scale-dependent response | R isotropic and scale-free | simplicity | — | DES Y3, Y6 | Δχ² < 0.01 (Y6) (arXiv:2601.15175) [src: Sect. V.5]; 0.0078 (Y3) (arXiv:2105.13541) [src: Table 3] |

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Boost correction | ≈ 10% at the smallest θ, ≈ 2% at 6 h⁻¹Mpc | DES Y3 | arXiv:2105.13541 | Sect. III.2 |
| Randoms per lens | 40; two independent sets differ by Δχ² ≈ 16 (400 pts), 7.5 above 6 h⁻¹Mpc (248 pts), in Buzzard | DES Y3 | arXiv:2105.13541 | Sect. III.3 |
| Random realisation Δχ² | ≈ 6 | DES Y6 | arXiv:2601.15175 | Sect. V.5 |
| γ_t S/N | 173 all scales; 75 after cuts and without lens bin 2 | DES Y6 | arXiv:2601.15175 | Sect. IV.6 |
| Mean source responses | 0.857, 0.868, 0.820, 0.692 | DES Y6 | arXiv:2601.15175 | Table 3 |
| Angular cuts, 6 h⁻¹Mpc | 24.3′, 17.6′, 13.0′, 10.9′, 9.7′, 8.7′ | DES Y6 | arXiv:2601.15175 | Sect. III |
| Angular cuts, 4 h⁻¹Mpc | 16.2′, 11.8′, 8.7′, 7.2′, 6.4′, 5.9′ | DES Y6 | arXiv:2601.15175 | Sect. III |
| Scale-cut threshold | 0.3σ in (S8, Ωm) | DES Y3, Y6, DESI DR1 | arXiv:2601.15175; arXiv:2512.15960 | Sect. III; Sect. 3.5 |
| Cuts, DESI DR1 3×2pt | (γ_t, w_p) = (6, 8) h⁻¹Mpc via θ_min = r_p/χ(z_lens); KiDS ξ− cut moved 4′ → 6.06′ | DESI DR1 × DES/KiDS/HSC | arXiv:2512.15960 | Sect. 3.5 |
| Cuts, LSST Y1 synthetic, no mitigation needed in w | w > 12, γ_t > 8 h⁻¹Mpc the only set passing (**forecast**) | LSST Y1 setup | arXiv:2212.03734 | Sect. 3.3 |
| ΔΣ and w_p ranges | ΔΣ 12–30/40/80 h⁻¹Mpc; w_p 8–80 h⁻¹Mpc; Π_max = 100 h⁻¹Mpc; 74 points | HSC Y3 minimal bias | arXiv:2304.00705 | Sect. III.4 |
| HSC source-redshift shift prior | Δz_ph ~ N(−0.05, 0.09), taken from the emulator analysis | HSC Y3 minimal bias | arXiv:2304.00705 | Table 1 caption |
| Finite PM prior used for plots | 5 × 10¹³ M⊙ (the σ_B → ∞ covariance is not invertible) | DES Y3 | arXiv:2105.13541 | Sect. V.1 |
| Magnification measurement step | δμ = 1.02, δκ ≈ 0.01 | DES Y6 | arXiv:2601.14833 | Sect. IV.1 |
| ξ± vs 2×2pt consistency | Δ_PPD = 0.049 | DES Y6 | arXiv:2601.14559 | Sect. V.1.1 |
| Shear ratio, Y6 | 2.5′ to 6 h⁻¹Mpc; two highest source bins with the two lowest lens bins; Ωm = 0.31, H0 = 67 fixed; 10⁵ GGL realisations for the ratio covariance; ratios within 2.5σ of the geometric prediction; SR-only Δz against the n(z) priors 1.68σ (SOMPZ+WZ), 1.59σ (with blending) | DES Y6 | arXiv:2601.15175 | Sects. VI.1–VI.4 |
| redMaGiC decorrelation | X_lens = 0.9 ± 0.03 (2×2pt, Y1 cosmology fixed), 3.5σ from 1; 0.87 ± 0.02 in 3×2pt | DES Y3 | arXiv:2105.13545 | Sects. V.4, V.6 |
| Run times (DES Y3 data, PolyChord) | PM 45 h, Υ 49 h, Y-transform 54 h, project-out 70 h | DES Y3 2×2pt | arXiv:2212.03734 | Sect. 4.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Clustering and lensing want different biases.** DES Y3 redMaGiC gave
  b[w]/b[γ_t] = X_lens ≈ 0.87–0.9, "not expected in any current models",
  scale-, redshift- and area-independent (ten sky patches); it was traced
  to a colour-dependent photometric issue from the tight template threshold
  χ²_RM = 3, and a "broad-χ²" sample (threshold 8) agrees with MagLim
  (arXiv:2105.13545) [src: Sects. V.4–V.7]. Test: free X_lens per bin;
  split by area; vary the selection.
- **One lens bin breaks internal consistency.** In DES Y6 the first n(z)
  mode of lens bin 2 pushed to higher redshift and several Δ_PPD tests
  failed (3×2pt 0.006 to 0.007, threshold 0.01). Widening the redshift and
  α⁶ priors three-fold reached 0.01 but left lens-bin-2 posteriors more
  than 5σ from the fiducial-prior ones; dropping WZ or switching to
  shift-and-stretch did not help (stretch ≈ 0.8, 5σ from its prior);
  removing the bin gave 0.06 (arXiv:2601.14559) [src: App. A.2, A.4]. The
  paper suspects DES filter transitions and colour–redshift degeneracies,
  "exacerbated by sample selection that directly depends on photo-z's",
  which the source sample avoids; restoring the bin after unblinding moved
  Ωm and σ8 by 0.4σ and S8 negligibly [src: App. A.5].
- **Magnification coefficient against its prior.** α⁶ of DES Y6 pushed
  against the Balrog prior; relaxing it raised Δ_PPD only from 0.006 to
  0.01 (arXiv:2601.14559) [src: App. A.4]. In Y3 a free amplitude preferred
  a value different from Balrog and lens cross-clustering pointed to other
  systematics (arXiv:2209.09782) [src].
- **Covariance amplitude moves the consistency metric.** "A few percent
  change could result in the Δ_PPD values changing from 10⁻³ to 10⁻²"; the
  Y6 covariance used Halofit (< 2.5% on diagonal elements) and no IA, both
  checked after unblinding (arXiv:2601.14559) [src: App. A.3].
- **Unmasked large-scale systematics.** γ_× and PSF residual tangential
  shear are tested against a χ² distribution with 20 degrees of freedom over
  2.5′–250′ (arXiv:2601.15175) [src: Fig. 6]; HSC uses ΔΣ_× to set its
  maximum radius (arXiv:2304.00705) [src: Sect. III.4].
- **Overlap of lenses and sources.** Dilution (boost), GI and source
  clustering × IA appear together; DES measures the first and models the
  others, KiDS-1000 discards overlapping pairs (arXiv:2105.13541 [src: Sect.
  V.3.2]; arXiv:2007.15632 [src: Sect. 2.4]). Lens magnification matters
  most when lenses lie behind sources (arXiv:2512.15960) [src: Sect. 3.1.2].
- **Point-mass geometric approximation.** The one-B^i-per-bin variant can
  bias cosmology at LSST Y1 depth (arXiv:2212.03734) [src: Sect. 5].
- **2×2pt pulled low.** The DES Y6 2×2pt S8 sits below cosmic shear (values
  in `results.md#3x2pt-and-multi-probe`); the 3×2pt paper defers the
  lens-bin-2 effect on 2×2pt to a companion paper (arXiv:2601.14559) [src:
  App. A.5].

## Reading list
<!-- key: reading-list -->

- Method: Prat et al. 2021, arXiv:2105.13541 — the full γ_t estimator, PM
  marginalisation, magnification, error budget (Table 5).
- Method: Giannini et al. 2026, arXiv:2601.15175 — DES Y6 γ_t with
  metadetection, scale cuts, shear ratio with the mode-projection n(z).
- Method: Prat et al. 2022, arXiv:2212.03734 — PM, Υ, Y-transform and
  project-out compared.
- Method: Porredon et al. 2020, arXiv:2011.03411 — how the MagLim
  selection was optimised.
- Method: Legnani et al. 2026, arXiv:2601.14833 — magnification
  coefficients from Balrog and flux perturbation; notation.
- Application: DES Collaboration 2026, arXiv:2601.14559 — Y6 3×2pt, model
  choices and the unblinding investigation of lens bin 2.
- Application: Sugiyama et al. 2023, arXiv:2304.00705 — ΔΣ with
  spectroscopic lenses, reference-cosmology correction, minimal bias.
- Application: Heymans et al. 2020, arXiv:2007.15632 — harmonic-space
  galaxy–galaxy lensing, k-based ℓ cuts, overlap exclusion.
- Application: Porredon et al. 2025, arXiv:2512.15960 — DESI DR1 lenses on
  three shear surveys with one pipeline.
- Critique: Pandey et al. 2021, arXiv:2105.13545 — the X_lens
  decorrelation and its photometric origin.
- Critique: Elvin-Poole et al. 2022, arXiv:2209.09782 — magnification
  priors versus what the data prefer.

## Not verified
<!-- key: not-verified -->

- MacCrann et al. 2020 (the PM marginalisation paper), Park et al. 2021
  (Y-transform), Baldauf et al. 2010 (Υ), Sheldon et al. 2004 (boost
  factors) and the DES Y3/Y6 non-linear bias papers: cited as the papers
  above cite them; not read and their identifiers not fetched.
- The DES Y6 2×2pt paper that discusses lens bin 2 (cited as [43] in
  arXiv:2601.14559): not identified.
- The scale cuts and estimator of the KiDS-Legacy galaxy–galaxy lensing and
  of the UNIONS × BOSS measurement: not read.
- The DES Y6 cosmic-shear paper describes its shear-ratio set as the
  lowest lens bin with the two highest source bins
  (`systematics.md#redshift-distributions`), the galaxy–galaxy lensing paper
  as the two lowest lens bins; whether these are the same set was not
  checked.
