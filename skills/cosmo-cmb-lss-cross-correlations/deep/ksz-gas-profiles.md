# kSZ gas profiles — cosmo-cmb-lss-cross-correlations dossier

Scope: how a stacked or harmonic-space kSZ measurement is turned into a gas
profile or a feedback statement — the forward model of the filtered signal,
the gas model (GNFW, baryonification) with its priors and truncation, the
HOD and halo-mass inputs, how simulations are stacked for a like-for-like
comparison, the lensing-to-kSZ ratio, and the projected-field estimator —
and how to choose between these routes.
Snapshot: 2026-10-18.
From: Baxter 2022 Snowmass review (arXiv:2203.06795), Sect. II.2
("Constraining baryonic feedback"); SO science goals 2025
(arXiv:2503.00636), Sect. 3.4 (kSZ gas and feedback paragraph).

Already in L2, not repeated here: the estimator families, the CAP formula
and the DESI Y1 stacking estimator with r = 0.65
(`physics-and-methods.md#estimators`); the pairwise estimator, its bins and
the τ̄ model dependence (`physics-and-methods.md#estimators`,
`systematics.md#ksz-the-optical-depth-degeneracy`); r and photometric
velocities (`systematics.md#ksz-velocity-reconstruction-errors`);
foreground nulls (`systematics.md#ksz-foregrounds-and-map-systematics`);
satellites and selection (`systematics.md#ksz-and-tsz-host-haloes-satellites-and`);
the detections and feedback numbers
(`results.md#detections-by-estimator`,
`results.md#gas-what-the-ksz-profile-says-about-baryons-and`) and the
feedback debate (`open-questions.md#how-strong-is-baryonic-feedback-as-seen-by-the`).
Velocity reconstruction by quadratic estimator is in
`deep/ksz-velocity-reconstruction.md`; the cosmic-shear use of a kSZ-fitted
baryon model is in `cosmo-weak-lensing/deep/baryonic-feedback.md`.

Symbols: θ_d aperture radius of the filter; 𝒯(θ_d) CAP output in
μK·arcmin²; τ optical depth; n_e free-electron density; ρ_gas gas density;
v_r line-of-sight velocity, v_rms its root mean square; r correlation
coefficient between stacking and true velocities; X_H = 0.76 hydrogen mass
fraction; μ_e mean molecular weight per free electron; f_b = Ω_b/Ω_m;
R_200, r_200c, M_200c radius and mass at 200 times the critical density;
M_500 the same at 500; d_A angular-diameter distance; P_eg electron–galaxy
power spectrum; A_k2h free amplitude of the two-halo term.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Choose the observable
<!-- key: step-1-choose-the-observable -->

| Observable | Output | Analyses read |
|---|---|---|
| Velocity-weighted CAP stack in real space | 𝒯(θ_d) at 1′–6′ | Amodeo 2020 (arXiv:2009.05558); Ried Guachalla 2025 (arXiv:2503.19870); Qu 2026 (arXiv:2604.19744), Sect. III.5 |
| Velocity-weighted stack with a ΔΣ filter | mean temperature in μK, directly comparable with lensing ΔΣ | Liu 2026 (arXiv:2609.22466), Sect. III.2.4 |
| Momentum template × T in harmonic space | bandpowers C_ℓ^{π̂T}, nearly uncorrelated | Qu 2026, Sect. III.3 |
| Squared filtered T × projected galaxies (no redshifts) | C_ℓ^{kSZ²×δ_g}, amplitude A_kSZ² ∝ f_b² f_free² | Kusiak 2021 (arXiv:2102.01068), Sect. II.1 |

The stacked estimators need a velocity per galaxy; the projected field
needs none but measures the square of the signal.

### Step 2. Forward-model the filtered signal
<!-- key: step-2-forward-model-the-filtered-signal -->

Amodeo 2020 lists the chain that later analyses repeat [src:
arXiv:2009.05558, Sect. II.1]: (i) project the 3D gas profile along the line
of sight, τ(θ) = σ_T ∫ n_e(√(l² + d_A²θ²)) dl (Eq. 6); (ii) convolve with the
measured beam of each band (non-Gaussian, FWHM 2.1′ at f090 and 1.3′ at
f150); (iii) for pressure, multiply by the band response to tSZ; (iv) average
inside disks of radius θ_d; (v) subtract the mean in the equal-area ring out
to √2 θ_d. The kSZ temperature is then ΔT/T_CMB = τ_gal (v_r/c) (Eq. 7), with
v_r = 1.06 × 10⁻³ c, the linear-theory rms at the median z = 0.55 of CMASS;
e^−τ is set to 1 because the mean optical depth over 0.4 < z < 0.7 is below
one percent. The gas–electron conversion is n_e = [(X_H + 1)/2] ρ_gas/m_amu
(Eq. 8). Profiles are averaged over the mass distribution of the sample,
"particularly important for the tSZ modeling, as the tSZ signal is
proportional to M^{5/3}, while the kSZ is linearly dependent on mass"; the
redshift distribution is replaced by the median, which the authors checked
on test models; all CMASS galaxies are treated as centrals.

The DESI-era version (Hadzhiyska 2025, arXiv:2507.14136, Eqs. 10–11) writes
T_kSZ(θ) = T_CMB (v_rms^true/c) (σ_T/μ_e m_p) [ρ_gas^2D(θ) ∗ B(θ)], with
μ_e = 2/(X_H + 1), v_rms^true ≈ 300 km/s and an ACT DR6 beam of 1.6′ FWHM,
followed by the same CAP filtering "necessary to account for the signal
attenuation introduced by the filter" [src: Sect. III.5]. The
baryonification fit of Siegel 2025 (arXiv:2512.02954) scales the model by
the reported v_p^rms/r_v of each sample, which assumes that the gas velocity
dispersion does not depend on θ_d; its Appendix D finds this valid only at
small separations, so the kSZ fit is restricted to θ_d < 3′ [src: Sect. 3.1].

### Step 3. Choose the gas model
<!-- key: step-3-choose-the-gas-model -->

**GNFW density** (Amodeo 2020, Eq. 16, after its ref. [53]):
ρ_GNFW(x) = ρ_0 (x/x_c,k)^γ_k [1 + (x/x_c,k)^α_k]^{−(β_k − γ_k)/α_k},
ρ_gas = ρ_GNFW ρ_cr(z) f_b, x = r/R_200. The inner shape is unconstrained by
SZ data, so γ_k = −0.2 and α_k = 1 are fixed; the free parameters are ρ_0,
x_c,k, β_k and A_k2h with uniform priors 1 < log₁₀ρ_0 < 5,
0.1 < x_c,k < 1, 1 < β_k < 5, 0 < A_k2h < 5 [src: Sects. II.3, III.2]. The
total profile is ρ = ρ_1h + A_k2h ρ_2h (Sect. II.4). On CMASS the best fit
has χ² = 20.2, PTE = 0.32, and A_k2h = 1.1 +0.8/−0.7, a 1.6σ two-halo
signal; fixing x_c,k = 0.6 tightens log₁₀ρ_0 from 13% to 7%
(2.9 ± 0.2) without changing χ² [src: Sect. III.2]. The pressure GNFW
(Eq. 17) fixes γ_t = −0.3 and
x_c,t = 0.497 (M_200/10¹⁴ M⊙)^−0.00865 (1 + z)^0.731 from simulations.

**GNFW in harmonic space** (Qu 2026, Eqs. 23–24): the same form with
r/(x_c r_200c), α = 0.88 and γ = −0.2 fixed "to their fiducial values from
Battaglia" because of "strong degeneracies between the five GNFW
parameters"; sampled are log₁₀ρ_0 ∈ [1, 5], x_c,k ∈ [0.1, 1],
β_k ∈ [3.01, 6], A_k2h ∈ [0, 5] [src: Sect. III.3.3, Fig. 6 caption;
Sect. III.4.2]. The profile is **truncated** at r_cut where the enclosed gas
mass equals f_b M_200c, so that more gas (higher ρ_0) gives a smaller r_cut;
the authors stress that "a fitting function that matches the simulated
density profile at small radii can still yield a biased kSZ prediction once
combined with a given truncation scheme", and they add an analytic prior
excluding parameter sets for which the truncation has no solution [src:
Sect. III.4, Appendix F as cited there].

**Baryonification** (Siegel 2025, arXiv:2512.02954, Eqs. 5–9). The gas is a
cored double power law,
ρ_gas ∝ (Ω_b/Ω_m − f_star) / {[1 + r/r_core]^β(M) [1 + (r/r_ej)^γ]^{(δ − β(M))/γ}},
with r_core = 0.1 R_200, r_ej = θ_ej R_200 and
β(M_200) = 3 (M_200/M_c)^μ / [1 + (M_200/M_c)^μ]: groups (M_200 ≪ M_c) lose
their gas (β ≈ 0), clusters keep it (β ≈ 3). Seven parameters
{M_c, μ, θ_ej, δ, γ, η, η_δ}; the stellar ones are fixed (η = 0.1,
η_δ = 0.2) because no stellar fractions exist for the eROSITA bins, and the
others have top-hat priors log₁₀M_c ∈ [11, 15], θ_ej ∈ [2, 8], μ ∈ [0, 2],
γ ∈ [1, 4], δ ∈ [5, 11]. Inference uses the BCemu emulator, trained on 2,700
baryonified simulations of 512³ particles in 256 (Mpc/h)³, accurate to a
percent for 0.1 < k < 10 h/Mpc and 0 < z < 2 [src: Sect. 3, Table 1]. The
kSZ-only posterior is log₁₀M_c = 13.8 +0.6/−0.5; joint with eROSITA gas
fractions 13.6 ± 0.2 [src: Table 1]. The same model yields the matter-power
suppression directly, which is why this route is chosen for
weak-lensing priors.

### Step 4. Harmonic-space measurement and the HOD
<!-- key: step-4-harmonic-space-measurement-and-the-hod -->

Qu 2026 [src: Sects. III.3–III.4, IV.2]:
1. Template π̂(θ) = (Ω_pix n̄_g^2D)⁻¹ Σ_{i∈pix} v_r,i/c on a 0.5′ CAR grid
   (Eq. 10), an intensive quantity whose continuum limit is
   ∫ (dp/dχ)(1 + δ_g) v_r/c dχ (Eq. 11).
2. Pseudo-C_ℓ with NaMaster; the bandpower window is applied to the theory
   instead of inverting the mode coupling (Eqs. 13–14).
3. Theory C_ℓ^τg = ∫ dχ/χ² W_τ W_g P_eg(k_ℓ, z) with W_τ = σ_T a⁻² n̄_e
   (Eqs. 15–16), P_eg from the halo model (one-halo ∫ dn/dM ũ_τ ũ_g, Eq. 17;
   two-halo with halo bias, Eq. 18), computed with class_sz.
4. Gaussian NaMaster covariance (Knox limit Eq. 25); Gaussian likelihood over
   1000 ≤ ℓ ≤ 7000 (Sect. III.4.2; a footnote in Sect. IV.2 names
   ℓ = 1000–5000 as the fitting range); Cobaya until R − 1 < 0.01.
5. HOD marginalisation: the DESI LRG HOD (AbacusHF-v2 baseline, Eqs. 31–32)
   is fitted to the projected correlation function in three bins
   (0.4–0.6, 0.6–0.8, 0.8–1.1). A Gaussian-process emulator trained on 1000
   class_sz runs over the 10-dimensional HOD + gas space (median error
   0.16–0.19%, 0.8% in the prior volume) averages the prediction over
   N_HOD = 100 HOD draws, uniform within the 5th–95th percentiles of the
   clustering posterior, at each step (Eq. 33). The completeness f_cen
   cancels in the n̄_g-normalised spectrum.
6. Cosmology fixed to Planck 2018 TTTEEE; 50 posterior draws spanning ~4σ
   change D_ℓ^kSZ by 2–3%, against ~30% from the gas parameters (footnote 5).

Real-space and harmonic results are linked by the CAP window
W_ℓ(θ_d) = A_disk [4J_1(ℓθ_d) − 2√2 J_1(√2 ℓθ_d)]/(ℓθ_d), A_disk = πθ_d²
(Eq. 36), with ΔT(θ_d) = (r σ_rec)⁻¹ Σ_b Δℓ_b (2ℓ_b + 1)/(4π) W_ℓb C̃_b
(Eq. 37). The Δℓ_b factor is needed because NaMaster bandpower windows are
normalised to unit row sums [src: Sect. V.3].

### Step 5. Stack a simulation like the data
<!-- key: step-5-stack-a-simulation-like-the-data -->

Bigwood 2025 (arXiv:2510.15822) builds the comparison for eight
hydrodynamical runs [src: Sects. 3.1–3.4]:
1. Place a snapshot box at its comoving distance, compute per gas cell the
   Doppler parameter b = v_r σ_T m_g / (μ_e m_p Ω_pix d_A² c) (Eq. 1) with
   μ_e = 1.17, excluding star-forming and T < 10⁵ K gas (no measurable
   change), on ≈ (0.2′)² pixels; ΔT_kSZ = −b T_CMB (Eq. 2). The 100 Mpc/h
   boxes are projected along three axes.
2. Convolve with a 1.6′ Gaussian beam; apply the CAP filter; use the
   inverse-variance, velocity-weighted estimator of Eq. 5 with **r_v = 1**,
   because the true galaxy velocities are used (satellites take the
   velocity of their central). Objects within 6√2′ of the box edge are
   dropped.
3. Correct for cosmic variance: in 64 sub-boxes of 100 Mpc/h from a
   400 Mpc/h BAHAMAS run the amplitude scatters, mainly through the rms
   line-of-sight velocity of the stacked haloes; 200 Mpc/h sub-boxes halve
   the scatter, and 400 Mpc/h boxes show none. Each profile is rescaled by
   the ratio of its stacked v_LOS,rms to the FLAMINGO value, which also puts
   all runs on the FLAMINGO cosmology.
4. Match the selection in **halo mass**, not number density: the minimum
   stellar mass in each simulation is tuned so that the mean halo mass
   equals the galaxy–galaxy-lensing value of Siegel 2025
   (log₁₀⟨M_500/M⊙⟩ = 13.31 for BGS, 13.30 for LRGs); the required cuts
   differ by up to 0.5 dex between simulations [src: Sects. 3.4.2, 4.2].
5. Goodness of fit with the full measurement covariance, because large-radius
   bins are strongly correlated [src: Sect. 4.2].

The alternative of Ried Guachalla 2025 selects galaxies in Illustris and
TNG300 by abundance matching to the photometric LRG number density and to
the HOD mean halo masses (10^13.4 and 10^13.2 M⊙/h) and then either matches
the simulated profile to the largest aperture or leaves its amplitude free,
fitted linearly as Â = mᵀC⁻¹d / mᵀC⁻¹m with σ_A = (mᵀC⁻¹m)^−1/2 [src:
arXiv:2503.19870, Sects. V.2, V.2.1, V.2.2; App. .3, Eqs. 12–15].

### Step 6. Calibrate the halo mass or take a ratio
<!-- key: step-6-calibrate-the-halo-mass-or-take-a-ratio -->

- **CMB lensing of the same galaxies** (arXiv:2507.14136): κ cutouts from the
  ACT DR6 map reprojected to 0.5′ pixels, averaged in 8 annuli of 1.5′ out to
  10.5′ (Eq. 1); an HOD fitted on AbacusSummit gives C_ℓ^gm, converted to a
  "kSZ-like" matter profile ρ_m^2D(θ) = ∫ ℓdℓ/2π J_0(ℓθ) C_ℓ^gm (Eq. 15). The
  ratio gives f_gas(<R)/(Ω_b/Ω_m) after a simulation-calibrated beam
  correction of about 3% [src: Sects. II.3, IV.2].
- **Galaxy–galaxy lensing with a ΔΣ filter** (arXiv:2609.22466): the kSZ
  stamp is filtered as ΔΣ_kSZ(R) = Σ̄(<R) − Σ̄(R, R + δR) with δR = 0.75′,
  chosen larger than the diagonal pixel size, at 9 radii from 1′ to 6′
  matching the lensing bins (Eqs. 14–16). The ratio
  f_gas^obs(R) = ΔΣ_kSZ/(α_conv ΔΣ_lens) (Eq. 25) needs no profile model; its
  beam suppression is strongest below ~2′, below ~10% beyond, and nearly the
  same in six simulations spanning Illustris, TNG, SIMBA and FLAMINGO [src:
  Sects. III.2.4, III.3.2, III.3.3].

### Step 7. The projected-field estimator
<!-- key: step-7-the-projected-field-estimator -->

Kusiak 2021 [src: arXiv:2102.01068, Sects. II.1, II.2, IV.1, IV.2]:
1. Filter the cleaned CMB map with F(ℓ) = C_ℓ^kSZ/C_ℓ^tot normalised to a
   unit maximum (Eq. 3), times the 5′ Gaussian beam (Eqs. 4–5); the filter
   removes ℓ < 100, which also removes the ISW, and peaks near ℓ ≈ 2000.
2. Square in real space and cross with δ_g. In Limber,
   C_ℓ = c⁻² ∫ dη/η² W_g g² 𝒯(ℓ/η, η) (Eq. 6), with the triangle power
   spectrum built from the hybrid bispectrum approximated as
   (1/3) v_rms² B_m^NL (Eq. 8); Halofit v_rms raises the signal by ≈ 20%
   over linear theory. Because g ∝ f_b f_free, the amplitude scales as
   f_b² f_free².
3. Model the CMB lensing term (Eq. 9), "the largest term in the overall
   signal"; it is ∝ b_g, so it breaks the b_g–A_kSZ² degeneracy. The fit
   frees A_kSZ², b_g and the magnification slope s.
4. Keep tSZ out by using a tSZ-free map (LGMCA or SMICA-noSZ) in at least one
   leg; remove galaxy-correlated dust by "α-cleaning", a per-ℓ-bin linear
   combination (1 + α)T_LGMCA − αT_545 that nulls the cross with δ_g
   (Eq. 20).
5. NaMaster bandpowers in 13 bins of Δℓ = 200 from 300 to 2900, Gaussian
   covariance, nearly diagonal but used in full.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Free amplitude or mass-matched comparison
<!-- key: free-amplitude-or-mass-matched-comparison -->

- **Free amplitude** discards amplitude information; any model rejected
  this way "would be even more ruled out otherwise". On DESI Y1 it leaves
  TNG at PTE = 0.046 with a rescaling 0.33, which the authors read as an
  unlikely factor-3 mass error rather than as acceptance [src:
  arXiv:2503.19870, Sect. V.2.2, Table 1].
- **Matching the largest aperture** assumes all bound gas is enclosed there,
  but that point has the largest primary-CMB noise and contains a two-halo
  term [src: same, Sect. V.2.1]. Same data: TNG PTE ~ 10⁻⁴⁸ against 0.046 when
  free (Table 1).
- **Lensing mass matching** keeps the amplitude: fiducial BAHAMAS, FABLE and
  FLAMINGO are > 10σ from the LRG profile, and all simulations but FABLE and
  XFABLE are within 2σ of BGS [src: arXiv:2510.15822, Sect. 4.2, Table 2].

### Profile fit, simulation or ratio
<!-- key: profile-fit-simulation-or-ratio -->

| Route | Assumes | Buys | Costs |
|---|---|---|---|
| GNFW + two-halo | a mass distribution and r; a truncation | interpretable shape parameters | strong degeneracies; inner slope fixed; truncation-dependent large-radius signal (arXiv:2604.19744) |
| Baryonification | spherical analytic components; v_rms/r_v independent of radius | direct P(k) suppression | fit limited to θ_d < 3′ (arXiv:2512.02954) |
| Hydrodynamical stacks | the simulation's galaxy–halo connection matches after the mass cut | no gas parametrisation | box size, v_rms scatter, satellite fractions (arXiv:2510.15822) |
| Lensing/kSZ ratio | the same filter on both; beam correction | no profile model; weak dependence on mass normalisation | a differential projected f_gas, not the 3D cumulative one (arXiv:2609.22466, Sect. III.3.2) |

The ratio of arXiv:2507.14136 "compares relative rather than absolute
quantities" and is "less sensitive to uncertainties in normalization and
mean halo mass" [src: Sect. IV.2]; arXiv:2609.22466 replaces its CAP filter
by the ΔΣ filter so that the ratio is taken bin by bin [src: Sect. III.2.4].

### Fixed or marginalised HOD
<!-- key: fixed-or-marginalised-hod -->

Marginalising the HOD degrades ρ_0 by a factor 1.4–3.5, most where the
HOD–gas degeneracy is strongest (z_2), and turns β_k into an upper limit in
every bin [src: arXiv:2604.19744, Table 2 caption]. The authors call fixing
the HOD a neglect of a systematic, and the uniform sampling within the
clustering bounds "conservative" (Sect. IV.2.1).

### Real space or harmonic space
<!-- key: real-space-or-harmonic-space -->

Harmonic bandpowers are nearly uncorrelated and carry a Gaussian analytic
covariance; real-space CAP points are strongly correlated at large radius
and use a bootstrap [src: arXiv:2604.19744, Sects. III.4.1, V.3;
arXiv:2510.15822, Sect. 4.2]. The harmonic analysis uses three redshift bins
matched to the HOD calibration, the configuration-space one four finer bins
for redshift evolution [src: arXiv:2604.19744, Sect. IV.2].

### Which velocity enters the prediction
<!-- key: which-velocity-enters-the-prediction -->

The stacked signal decomposes into a mean-bulk-flow term ⟨τ⟩ v_rms^0 and
two non-linear terms, a density–bulk-flow covariance and a velocity
decorrelation term (arXiv:2607.23339, Eq. 7). Each can reach ≈ 50% of the
signal; they largely cancel, leaving 10–20% [src: Table 1 caption]. Analytic
models keep only the first term; hydrodynamical predictions use true
velocities while the data use linear reconstruction; either comparison
differs from the measurement by 5–10% in a scale-dependent way, reducible
for analytic models with a reconstruction smoothing R_s ≥ 30 h⁻¹Mpc [src:
Sect. 5.3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| CAP apertures | 1′–6′, ≈ 1–4 R_vir | ACT DR5 × CMASS | arXiv:2009.05558 | Sect. II.1 |
| Beams | 2.1′ (f090), 1.3′ (f150) FWHM | same | arXiv:2009.05558 | Sect. II.1 |
| Assumed v_r | 1.06 × 10⁻³ c at z = 0.55 | same | arXiv:2009.05558 | Sect. II.1, Eq. 7 |
| GNFW fixed shape (density) | γ_k = −0.2, α_k = 1 | same | arXiv:2009.05558 | Sect. II.3 |
| GNFW fixed shape (density) | γ = −0.2, α = 0.88 | DESI DR2 × ACT DR6 | arXiv:2604.19744 | Fig. 6 caption |
| Harmonic fit range | 1000 ≤ ℓ ≤ 7000 (footnote: 1000–5000) | same | arXiv:2604.19744 | Sect. III.4.2; Sect. IV.2 |
| HOD draws per step | 100, uniform in 5th–95th percentiles | same | arXiv:2604.19744 | Sect. IV.2.1 |
| Cosmology sensitivity of D_ℓ^kSZ | 2–3%, against ~30% from gas | same | arXiv:2604.19744 | Sect. IV.2, footnote |
| HOD-marginalised fit, combined | log₁₀ρ_0 = 3.01 +0.17/−0.25; x_c = 0.428 +0.085/−0.21; β < 3.27; χ² = 17.85 for 12 dof | same | arXiv:2604.19744 | Table 2 |
| Simulation beam | 1.6′ Gaussian | DESI Y1 × ACT comparison | arXiv:2510.15822 | Sect. 3.1 |
| Lensing mean halo masses | log₁₀⟨M_500/M⊙⟩ = 13.31 (BGS), 13.30 (LRG) | same | arXiv:2510.15822 | Sect. 4.2 |
| Satellite fractions after the mass cut | ~10–30% by simulation and bin | same | arXiv:2510.15822 | Table 2 |
| Fiducial FLAMINGO against LRG profile | > 10σ; f_gas−8σ variant 2.90σ | same | arXiv:2510.15822 | Table 2 |
| kSZ amplitude vs P(k) suppression | scatter about the median relation < ~5% | ANTILLES + 8 runs | arXiv:2510.15822 | Sect. 5 |
| Baryonification kSZ range | θ_d < 3′ | BOSS + DESI × ACT | arXiv:2512.02954 | Sect. 3.1 |
| BCemu accuracy | percent, 0.1 < k < 10 h/Mpc, 0 < z < 2 | same | arXiv:2512.02954 | Sect. 3 |
| κ profile binning | 8 annuli of 1.5′ to 10.5′ | DESI × ACT DR6 κ | arXiv:2507.14136 | Sect. II.3 |
| Beam correction of the ratio | ≈ 3% | same | arXiv:2507.14136 | Sect. IV.2 |
| Velocity-reconstruction systematic on the gas amplitude | 10–15% | same | arXiv:2507.14136 | Sect. IV.2 |
| f_gas at R ≲ 1′; at R_200m | ~0.3; ≈ 0.3 against ≈ 0.34 from eROSITA | same | arXiv:2507.14136 | Sect. IV.2 |
| ΔΣ filter ring | δR = 0.75′; 9 radii 1′–6′ | DESI DR2 × ACT DR6 × HSC | arXiv:2609.22466 | Sect. III.2.4 |
| Projected-field bins | 13 × Δℓ = 200, ℓ = 300–2900 | Planck × unWISE | arXiv:2102.01068 | Sect. IV.2 |
| Projected-field per-sample significance | 1.4σ, 5.0σ, 2.5σ (blue, green, red) | same | arXiv:2102.01068 | Fig. 5 caption |
| Non-linear velocity terms | each up to ≈ 50%; net 10–20% | simulations | arXiv:2607.23339 | Table 1 caption |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Velocity normalisation.** Every gas amplitude scales as 1/r; L2 holds
  the size (`systematics.md#ksz-velocity-reconstruction-errors`). A
  prediction built with true velocities and r_v = 1 against data built with
  reconstructed ones differs by 5–10% in shape (arXiv:2607.23339,
  Sect. 5.3) [src]. Test: build the simulated stack with the same
  reconstruction as the data. Within current errors the effect is 1–2σ
  (same section).
- **Including only one non-linear term.** Assigning the central's velocity
  to all gas (density–velocity correlation without decorrelation) gives
  ≈ 50% errors, larger than neglecting both (≈ 10–20%), because the two
  cancel (arXiv:2607.23339, Sect. 5.3, Eq. 15) [src].
- **Small boxes.** In 100 Mpc/h volumes the amplitude scatters with the rms
  velocity of the few stacked haloes; uncorrected, it can mimic a feedback
  difference (arXiv:2510.15822, Sect. 3.3) [src]. Test: v_rms rescaling, or
  sub-volume scatter.
- **Massive haloes missing from the simulation.** Illustris volumes do not
  sample the most massive hosts of the sample, which changes the amplitude
  more than the shape (arXiv:2503.19870, Sect. V.2) [src]; this is what
  drives the free-amplitude choice.
- **Truncation.** Two schemes that agree inside r_200c disagree beyond it;
  validate the fit plus truncation against the simulation's forward-modelled
  kSZ, not only its density profile (arXiv:2604.19744, Sect. III.4) [src].
- **Satellites and miscentring.** Varying the satellite fraction from 0 to
  30% did not alter the DESI LRG profile shape (as quoted in
  arXiv:2503.19870, Sect. V.2.2); pruning close pairs closer than 0.5 Mpc
  leaves f_gas^obs unchanged within the noise, the 1.6′ beam already
  smoothing ~0.5 Mpc at z ~ 0.3 (arXiv:2609.22466, App. A) [src]. No
  amplitude for the miscentring bias itself was found.
- **Radius-independent velocity dispersion.** Valid only at small θ_d;
  restrict fits to θ_d < 3′ (arXiv:2512.02954, Sect. 3.1) [src].
- **Projected field: dust and lensing.** The lensing term dominates and
  must be modelled; dust correlated with the galaxies is removed by
  α-cleaning, and the meaningful null is (T_clean T_dust) × δ_g, since
  T_clean × δ_g passes by construction. PTEs for 13 dof: 0.46, 0.61, 0.83
  with the 545 GHz map; 0.83, 0.72, 0.95 with 857 GHz; noise-map nulls
  0.32–1.0; a 40% Planck mask gives consistent results
  (arXiv:2102.01068, Sect. IV.1, Table 3) [src].
- **Real-space ↔ harmonic consistency.** Convert the harmonic best fit to
  CAP with Eq. 37 of arXiv:2604.19744 and fit one amplitude A to the
  bootstrap-covariance profile; A = 1 is the pass criterion (Sect. V.3)
  [src].

## Reading list
<!-- key: reading-list -->

- Foundation: Schaan 2020, arXiv:2009.05557 — CAP stacking, tSZ/dust
  rejection (in L2).
- Method: Amodeo 2020, arXiv:2009.05558 — the forward-model chain, GNFW
  density and pressure, two-halo term, priors.
- Method: Qu 2026, arXiv:2604.19744 — harmonic momentum template, GNFW
  truncation, HOD-marginalised emulator likelihood, CAP window.
- Method: Kusiak 2021, arXiv:2102.01068 — projected-field estimator, lensing
  term, α-cleaning and its nulls.
- Method: Siegel 2025, arXiv:2512.02954 — baryonification fit of kSZ and
  X-ray gas fractions; priors; θ_d < 3′.
- Application: Bigwood 2025, arXiv:2510.15822 — stacking simulations like
  the data; cosmic-variance correction; lensing mass matching.
- Application: Ried Guachalla 2025, arXiv:2503.19870 — the two
  simulation-comparison approaches and their caveats.
- Application: Hadzhiyska 2025, arXiv:2507.14136 — CMB-lensing mass and the
  kSZ/κ gas fraction.
- Method: Liu 2026, arXiv:2609.22466 — ΔΣ filter and model-independent
  f_gas(R); beam and miscentring tests.
- Critique: Ondaro-Mallea 2026, arXiv:2607.23339 — decomposition of the
  stacked signal; consistency of stacking velocities in theory and data.

## Not verified
<!-- key: not-verified -->

- The two-halo term recipe of Amodeo 2020 (its Appendix A) and its pressure
  fit results (Sect. III.3) were not read.
- Qu 2026 Table 1 (fixed-HOD constraints) and Appendix F (allowed GNFW
  region) were not read; the discrepancy between the 1000–7000 and
  1000–5000 fitting ranges is as printed.
- How the "σ" deviation in Table 2 of arXiv:2510.15822 is converted from χ²
  is not stated in the parts read.
- The pairwise-estimator modelling beyond L2, and the HOD of
  arXiv:2507.14136 (its Sect. III.2), were not read for this dossier.
