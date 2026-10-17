# Neutrino mass from full-shape clustering — cosmo-neutrinos-dark-matter dossier

Scope: how a full-shape (FS) galaxy-clustering likelihood carries the
neutrino mass (which linear spectrum the bias multiplies, how neutrinos
enter the loop kernels, nuisance priors, how the free-streaming part of
the information is isolated, mock validation), and why the DESI
Collaboration and the external EFT reanalysis reach different limits.
Snapshot: 2026-10-17.
From: Di Valentino et al. 2024, Sect. III.2; DESI DR2 neutrino paper
(arXiv:2503.14744), Sects. II.2, III.2, VI.

Already in L2, not repeated here: the three channels and the
shift-versus-information result of adding the DR1 full shape
(`physics-and-methods.md#the-three-channels`); the DESI data vector,
scale range and X_rsd test in outline
(`physics-and-methods.md#how-the-main-analyses-obtain-the-bound`); the
headline limits (`results.md#cosmological-upper-limits-lambdacdm-sigmamnu`,
`results.md#dependence-on-the-dark-energy-model-desi-dr2`); the prior-volume
caveat in one paragraph
(`systematics.md#full-shape-analyses-nuisance-priors-and`); the
collaboration-versus-external debate (`open-questions.md#method-debates`).

## How it is done
<!-- key: how-it-is-done -->

Notation: M_ν ≡ Σm_ν (the FS papers write M_ν); f_ν ≡ Ω_ν/Ω_m; "cb" is the
cold dark matter + baryon fluid; P_cb its power spectrum; f the
logarithmic growth rate d ln D₊/d ln a; μ the cosine between wavevector and
line of sight; k_max the smallest scale fitted.

### Step 1. The physical effect and its scale
<!-- key: step-1-the-physical-effect-and-its-scale -->

- Abundance: Ω_ν = M_ν / (93.14 h² eV) (Noriega et al. 2022,
  arXiv:2208.02791, Eq. 5).
- Thermal velocity dispersion after the non-relativistic transition,
  σ_ν(z) ≃ 1811 (1 + z)(0.1 eV/m_ν) km/s (Eq. 6), which acts as pressure.
- Free-streaming wavenumber, for one species,
  k_FS(z) ≃ 0.0908 [H(z)/H0] (1 + z)⁻² (m_ν/0.1 eV) h/Mpc (Eq. 7); the
  authors state that several definitions exist and that this one is "never
  used" in their calculation [src: arXiv:2208.02791, Sect. 2]. For
  realistic masses the scale is "currently around 0.1 h/Mpc, at the onset
  of non-linear scales" [src: arXiv:2404.07269, Sect. 7.4, footnote 21].
- Below k_FS neutrinos cluster with the cb fluid; above it they do not, so
  power is suppressed, ΔP_m/P_m ≈ −8 f_ν "with the precise scaling
  dependent on which parameters are kept fixed" [src: arXiv:2503.14744,
  Sect. III.2]. BAO are "blind to neutrino free streaming"; the FS model
  can capture it [src: same].

### Step 2. Choose the field the galaxies trace: cb, not total matter
<!-- key: step-2-choose-the-field-the-galaxies-trace-cb -->

Every FS pipeline read here feeds the perturbation-theory model with the
linear cb spectrum and defines bias relative to δ_cb:

- FOLPSν: P_δδ = b₁² P_cb,δδ^1-loop + 2b₁b₂ P_b1b2 + … + 2b₁b_3nl σ₃²(k) P_cb,δδ^L
  (arXiv:2404.07269, Eq. 18; Eqs. 19–20 for P_δθ and P_θθ); "galaxies are
  biased tracers of the combined cold dark matter plus baryons field, and
  not the total matter field" [src: Sect. 3.1].
- velocileptors in DESI: the linear field "in fact, only baryons and dark
  matter, 'cb'" [src: arXiv:2411.12021, footnote 25].
- CLASS-PT in the external reanalysis: EFT predictions evaluated "with the
  linear matter power spectrum of the baryons and cold dark matter fluid",
  the "cb prescription" [src: arXiv:2601.16165, Sect. 3.1].

The reason, from simulations with neutrino particles: bias computed
against total matter is scale dependent on large scales in massive-neutrino
cosmologies, and the scale dependence is reduced when computed against
cold dark matter only; the Tinker large-scale bias is reproduced when the
linear cold dark matter spectrum is used (Villaescusa-Navarro et al. 2014,
arXiv:1311.0866 [src]). In the FOLPSν perturbative model the neutrino field
is not linearised but tied to the non-linear cb field,
δ_ν(k) = [T_ν(k)/T_cb(k)] δ_cb(k) (arXiv:2208.02791, Eq. 9), because a
linear neutrino field "would violate momentum conservation" [src: Sect. 2];
the Poisson equation sources the potential with f_cb δ_cb + f_ν δ_ν
(Eq. 8).

### Step 3. Put neutrinos into the loop kernels, or not
<!-- key: step-3-put-neutrinos-into-the-loop-kernels-or -->

With massive neutrinos D₊ and f depend on k, so Einstein–de Sitter (EdS)
kernels are no longer exact. The linear velocity–density relation becomes
non-local (arXiv:2404.07269, Eq. 31):

  θ^(1)(k, t) = [f(k, t)/f₀(t)] δ^(1)(k, t),

with f₀ the k → 0 limit, where neutrinos behave as cold dark matter. The
"fk-kernels" carry this into G₂ and G₃, for example the advection term
½[(f(k₁)/f₀)(k₁/k₂) + (f(k₂)/f₀)(k₂/k₁)] ∈ G₂ (Eq. 32). f(k)/f₀ is taken
from the Hu–Eisenstein approximation and f₀ from the k = 0 growth equation;
since the shape of f(k) changes little with redshift, loops are computed
at one redshift and rescaled by D₊(k → 0, z) [src: Sect. 4.1]. The fk
kernels keep only the growth-factor pieces of the full kernels, dropping
the slow terms from the failure of f² = Ω_m, which the authors identify as
subdominant (arXiv:2208.02791 [src: abstract]). Cost: 2 × 26 instead of
2 × 24 P22-type and 2 × 11 instead of 2 × 7 P13-type FFTLog matrix products,
which the authors call negligible [src: arXiv:2404.07269, Sect. 4.1].

Three practices in use:

| Code / analysis | Neutrinos in the loops | Place read |
|---|---|---|
| FOLPSν (DESI cross-check) | fk-kernels, scale-dependent f(k) | arXiv:2404.07269, Sect. 4.1 |
| velocileptors EPT (DESI DR1 FS baseline) | a module that "includes the scale-dependent impact of massive neutrinos on the growth rate" (`ept_fullresum_varyDz_nu_fftw.py`) | arXiv:2411.12022, Sect. 2.3.2, footnote 8 |
| CLASS-PT (Ivanov et al. 2026) | EdS kernels and growth factors evaluated in a massless cosmology, cb linear spectrum | arXiv:2601.16165, Sect. 3.1 |

The external analysis justifies EdS by the current error bars and by the
claim that the growth constraint on M_ν comes mainly from breaking the
A_s–M_ν degeneracy through σ₈; its test is that (Ω_m, H0, σ₈) from a fixed
0.06 eV single massive state and from a massless sector agree to ≲ 0.1σ
[src: arXiv:2601.16165, Sect. 3.1]. The authors note this test
"greatly overestimates" the approximation [src: same].

### Step 4. Bias basis, counterterms, stochastic terms and their priors
<!-- key: step-4-bias-basis-counterterms-stochastic-terms -->

DESI DR1 baseline (velocileptors; Lagrangian bias basis; per tracer)
[src: arXiv:2411.12021, Sect. 4.7 and Table 4]:

| Parameter | Prior | Stated reason |
|---|---|---|
| (1 + b₁)σ₈(z) | U[0, 3] | the data constrain these combinations; reduces volume effects that favour low σ₈ |
| b₂σ₈²(z), b_sσ₈²(z) | N(0, 5²) | wide enough that prior-weight effects are negligible; b_s not co-evolved with b₁, because co-evolution would add information on A_s and ω_cdm |
| b₃ | fixed to 0 | cubic bias small for intermediate-mass haloes and degenerate with counterterms; barely changes ΛCDM posteriors |
| α₀, α₂ (counterterms) | N(0, 12.5²) h⁻² Mpc² | width at which the counterterm is 50% of the linear power at k_max = 0.2 h/Mpc (App. E) |
| SN₀ | N(0, 2²) × 1/n̄_g | multiple of Poisson shot noise |
| SN₂ | N(0, 5²) × f_sat σ²_1,eff / n̄_g | satellite fraction × velocity dispersion × shot noise |
| n_s, ω_b without CMB | N(0.9649, 0.042²); N(0.02218, 0.00055²) | n_s at ten times the Planck width ("n_s10"); BBN on ω_b |

Seven nuisance parameters per tracer [src: arXiv:2503.14744, Sect. II.2];
three bias, two counterterm and two stochastic parameters match this
count [der]. The hexadecapole is excluded because its extra, poorly
constrained parameters produce stronger prior-weight effects and, in ΛCDM,
it does not improve the errors [src: arXiv:2411.12021, Sect. 4.5]. These
choices were fixed before unblinding on mocks and noiseless synthetic data
[src: Sect. 4.7].

External reanalysis (CLASS-PT; per redshift bin) [src: arXiv:2601.16165,
Sect. 3.5, Table 2]: sampled b₁σ₈ ~ U[0, 3], b₂σ₈² and b_G2σ₈² ~ N(0, 5²);
b_Γ3 A_AP A_amp² ~ N((23/42)(b₁ − 1), 1²); counterterms ~ N(0, 6²) except
c̃ A_AP A_amp ~ N(16, 16²) for fingers of God; one-loop bispectrum
coefficients with non-linear prefactors; 45 Wilson coefficients per bin in
total, linear ones marginalised analytically. A_AP ≡ (H0^fid/H0)³
(H/H^fid)(D_A^fid/D_A)² and A_amp ≡ σ₈²(z)/σ²_8,fid(z); the rescalings are
there "to reduce prior-volume shifts" [src: Table 2 caption]. Counterterms
are normalised by k_NL = 0.45 h/Mpc; the mean 16 on c̃ reflects
(k_NL/k_FoG)⁴ ~ 10 with k_FoG ≃ 0.25 h/Mpc [src: Sect. 3.5, footnotes
11–12]. Cosmology priors: n_s ~ N(0.9649, 0.0042²), ω_b ~ N(0.02237,
0.00015²) (Eq. 48), chosen "to aid comparison with the DESI+CMB analyses";
DESI-only results are stated unchanged with a BBN ω_b prior [src: same].
Neutrinos: three degenerate states when varied, one massive state at
0.06 eV when fixed [src: same].

### Step 5. Likelihood, covariance and combination with BAO
<!-- key: step-5-likelihood-covariance-and-combination -->

- DESI: P_ℓ (ℓ = 0, 2) of six tracers, 0.02 < k < 0.20 h/Mpc; covariance
  from 1000 EZmocks with corrections from Abacus mocks and RascalC [src:
  arXiv:2503.14744, Sect. II.2]. The joint FS + post-reconstruction BAO
  covariance comes from the EZmocks, with the BAO block replaced by the one
  from the data fits, and HOD and imaging systematic terms added to the
  covariance [src: arXiv:2411.12022, Sect. 2.3.1]. DR1 FS is not combined
  with DR2 BAO because the cross-covariance needs mocks not yet available
  [src: arXiv:2503.14744, Sect. II.2].
- External: P_ℓ (ℓ = 0, 2, 4) for k from 0.005 to 0.20 h/Mpc, B_ℓ
  (ℓ = 0, 2) to 0.16 h/Mpc at one loop (0.08 h/Mpc at tree level), plus
  spectroscopic galaxy × CMB-lensing and photometric galaxy auto and
  cross spectra (Eq. 3) [src: arXiv:2601.16165, Sects. 2.3–2.4]. No
  P–B cross-covariance and Gaussian bispectrum covariance; the authors
  state that an explicit test at k_max^B = 0.16 h/Mpc for the DR1 volume
  "is not yet available" [src: Sect. 2.3].

### Step 6. Sample and report
<!-- key: step-6-sample-and-report -->

DESI runs real-data chains without the Taylor emulator, or re-evaluates
every emulated sample with the full model, because the emulator can be
inaccurate far from its calibration point; Cobaya Metropolis–Hastings
without emulator, NUTS (blackjax) with it [src: arXiv:2411.12021,
Sect. 4.7, item 9]. Limits are 95% with Σm_ν > 0 and three degenerate
states [src: arXiv:2411.12022, Table 3 caption].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Isolating the free-streaming information
<!-- key: isolating-the-free-streaming-information -->

DESI's construction, on DR1 FS + BAO + BBN + n_s10, in three switches
[src: arXiv:2503.14744, Sect. VI]:

1. **Background-only neutrinos.** Theory modified so that M_ν affects only
   the background, following Bertólez-Martínez et al. (arXiv:2411.14524).
   Remaining effect at fixed ω_cdm: near scale-independent suppression and
   a BAO change. Constraints "significantly weaker", hence the FS analysis
   uses the scale-dependent effect.
2. **Remove the amplitude.** θ(k) = f(k) δ(k) (Eq. 39) becomes
   θ = X_rsd f(k) δ (Eq. 40), X_rsd marginalised. σ₈ becomes unconstrained
   but the M_ν limit barely moves: the information is not the amplitude.
3. **Anchor the slope.** Replacing n_s10 by U[0.8, 1.2] degrades the limit
   "significantly"; a Planck-width n_s prior gives < 0.300 eV (Eq. 41).
   The free-streaming signal is a change of slope against the large-scale
   spectrum, so it needs an external n_s.

With CMB priors on θ* and n_s only (no CMB ω_cdm or ω_b), DESI DR1
(FS + BAO) + BBN gives < 0.193 eV (Eq. 42); measured by the observed
information I(θ) = −d² log p(θ|y)/dθ², geometry and shape each contribute
about half of it [src: Sect. VI]. Once CMB ω_b and ω_cdm enter, "the
suppression of the power spectrum is unobservable with current
sensitivity" [src: same]. The background-only switch was introduced on
CMB data, where the bound on the perturbation-only mass is < 0.8 eV and
the cosmological bound is "mostly a background measurement"
(arXiv:2411.14524 [src: abstract]).

### Shape (slope) or wiggles
<!-- key: shape-slope-or-wiggles -->

Noriega & Aviles 2024 (arXiv:2407.06117, Sect. V) build four noiseless
data sets mixing the broadband and the wiggles of M_ν = 0 and 0.5 eV
linear spectra at fixed ω_c, ω_b, fitted with FOLPS on a covariance for 25
times the eBOSS volume. Both data sets with 0.5 eV wiggles return
≈ 0.5 eV, including the one with an unsuppressed broadband; both with
massless wiggles return massless neutrinos, including the one with a
suppressed broadband. Their conclusion: the FS fit takes its mass
information from the suppressed wiggles and is "blind to the suppression
of the broadband" [src]. This differs from DESI's reading that the
information is the slope anchored by n_s [src: arXiv:2503.14744,
Sect. VI]. The two tests differ in data (synthetic eBOSS at 25 × volume,
with n_s fixed to Planck in the paper's baseline [src: Sect. IV], against
DR1 with n_s priors) and in the
background treatment, and neither paper confronts the other's test in the
sections read.

### EdS or neutrino kernels
<!-- key: eds-or-neutrino-kernels -->

On noiseless synthetic data from velocileptors with DESI covariances
[src: arXiv:2404.07269, Sect. 7.4, Eqs. 52–55]:

| Volume | EdS kernels | fk-kernels |
|---|---|---|
| DESI Y1 | M_ν < 0.368 eV | M_ν < 0.323 eV |
| DESI Y5 | M_ν < 0.170 eV | M_ν < 0.149 eV |

The authors call this "around 14%" more constraining power with fk-kernels
and find all parameters within 1σ either way; h, ω_cdm, A_s are
essentially unchanged [src: same]. Settings: one massive and two massless
states, M_ν ~ U(0, 5) eV [src: same]. The external analysis keeps EdS
kernels, with the robustness test of Step 3; it does not quote this
comparison in the section read.

### What the external limit adds, and where its gain comes from
<!-- key: what-the-external-limit-adds-and-where-its-gain -->

The external reanalysis reaches M_ν < 0.049 eV (ΛCDM) and < 0.077 eV
(w0waCDM) with FS + BAO + CMB + Pantheon+ [src: arXiv:2601.16165,
Sect. 4.3]. Differences from DESI, as the papers state them:

| | DESI DR1 FS (arXiv:2411.12022) | External (arXiv:2601.16165) |
|---|---|---|
| Statistics | P₀, P₂ | P₀, P₂, P₄; B₀, B₂ at one loop; κg, photometric gg and κg |
| k range | 0.02–0.20 h/Mpc | P 0.005–0.20, B 0.005–0.16 h/Mpc |
| Kernels | scale-dependent growth module | EdS + cb |
| Bias priors | σ₈-scaled; b₃ = 0 | σ₈-, A_AP-, A_amp-scaled; b_Γ3 centred on co-evolution |
| BAO | DR1, joint covariance | DR2 ("latest DESI BAO") |

Where the gain comes from, in the authors' words: in ΛCDM the improvement
over official numbers is "mainly due to our custom power spectrum and
bispectrum likelihoods"; adding the CMB-lensing auto spectrum leaves the
bound unchanged (0.049 eV both), so "most of our constraining power arises
from three-dimensional correlations and the measurements of the shape and
geometry parameters such as Ω_m and H0" [src: Sect. 4.3]. In w0waCDM the
37% gain is "driven primarily by the full-shape measurement of the
geometric parameters, most notably Ω_m, rather than by an independent
tightening of the growth-of-structure amplitude", since σ₈, w0, wa errors
barely change; in ΛCDM an Ω_m-driven tightening "should be interpreted with
care" because of the CMB–BAO Ω_m tension [src: same]. The authors therefore
regard the w0waCDM bound as "the more reliable arena" [src: same]. DESI
makes the same point for its own 0.071 eV: the gain over BAO + CMB
(0.082 eV) "is not directly associated with the suppression of the power
spectrum, but with a greater pull towards low Ω_m and high H0" [src:
arXiv:2411.12022, Sect. 4.1].

Neither analysis, then, attributes its CMB-combined limit to free
streaming.

### Fixed mass model
<!-- key: fixed-mass-model -->

- DESI and the external analysis vary three degenerate states [src:
  arXiv:2411.12022, Table 3 caption; arXiv:2601.16165, Sect. 3.5].
- FOLPS validation and Noriega & Aviles use one massive and two massless
  states [src: arXiv:2404.07269, Sect. 7.4; arXiv:2407.06117, Sect. IV].
  Limits from different mass models are not interchangeable without a
  stated check.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| DESI DR1 FS + BAO + BBN + n_s10 | M_ν < 0.409 eV (95%) | ΛCDM | arXiv:2411.12022 | Eq. 11 |
| Same with Planck-width n_s | < 0.300 eV | ΛCDM | arXiv:2411.12022 | Eq. 12 |
| Same + BBN + (θ*, n_s)_CMB | < 0.193 eV | ΛCDM | arXiv:2503.14744 | Eq. 42 |
| CMB without lensing reconstruction | < 0.265 eV | Planck PR3 | arXiv:2411.12022 | Sect. 4.1 |
| DESI DR1 BAO + CMB | < 0.082 eV | ACT lensing v1.2 | arXiv:2411.12022 | Eq. 13 |
| DESI DR1 FS + BAO + CMB | < 0.071 eV; 15% stronger than BAO only | ΛCDM | arXiv:2411.12022 | Eq. 14, Sect. 4.1 |
| Normal vs inverted, DESI DR1 + CMB | Δχ²_MAP ≃ −2 | ΛCDM | arXiv:2411.12022 | Sect. 4.1 |
| External, earlier paper: DR1 FS + CMB + DR2 BAO | < 0.059 eV | ΛCDM | arXiv:2601.16165 (citing its ref. 22) | Sect. 4.3 |
| External, effective-mass peaks | −0.06 ± 0.04 eV (ΛCDM), −0.06 ± 0.06 eV (w0waCDM) | truncated-Gaussian fit to chains | arXiv:2601.16165 | Sect. 4.3 |
| External, IO floor exclusion | ≈ 3.5σ (ΛCDM, truncated Gaussian); 98.3%, ≈ 2.4σ (w0waCDM, p(M_ν > 0.098 eV) = 0.017) | — | arXiv:2601.16165 | Sect. 4.3 |
| Counterterm prior width | 12.5 h⁻² Mpc² (= 50% of linear at k_max) | DESI | arXiv:2411.12021 | Sect. 4.5, Table 4 |
| k_max, P and B | 0.20 and 0.16 h/Mpc; P to 0.23 biases σ₈ up 4–5%, B to 0.20 biases it 3% down | External | arXiv:2601.16165 | Sect. 2.4 |
| fk vs EdS gain | ~14% on the 95% limit | synthetic DESI Y1/Y5 | arXiv:2404.07269 | Sect. 7.4 |
| Quijote validation, M_ν = 0.4 eV, z = 0.5, k_max = 0.2 | 0.39 (+0.16/−0.30) eV at 25 (h⁻¹Gpc)³; 0.31 ± 0.11 eV at 100 (h⁻¹Gpc)³ | FOLPSν, P₀ + P₂ | arXiv:2208.02791 | Table 2 |
| Peregrinus mocks | 6000³ cb + 3000³ ν particles, (3 h⁻¹Gpc)³, δf neutrinos; Σm_ν = 0.059 and 0.24 eV | DESI DR2 | arXiv:2503.14744 | Sect. II.8 |

The "official DESI DR1 FS + BAO + CMB" value is given as 0.077 eV in
arXiv:2601.16165 Sect. 4.3 and as 0.071 eV in arXiv:2411.12022 Eq. 14; the
sections read do not say which data combination the 0.077 eV refers to.
The IO floor is 0.098 eV and the NO floor 0.058 eV in arXiv:2601.16165,
against 0.10 and 0.059 eV in the DESI papers [src: both].

## What goes wrong
<!-- key: what-goes-wrong -->

- **Projection (prior-volume) effects masquerading as a mass preference.**
  On eBOSS, M_ν < 1.13 eV is tighter than BOSS z₁ or z₃ (1.67, 1.94 eV)
  although eBOSS is the noisiest; noiseless synthetic eBOSS data with
  M_ν = 0.06 eV give an "almost identical" posterior, < 1.24 eV, peaking
  at zero [src: arXiv:2407.06117, Sect. IV, Eqs. 4–7]. With 25 times the
  volume the peak is still at negative values [src: same]. Test: fit
  noiseless synthetic data at a known mass with the real covariance and
  window, then repeat with a rescaled covariance; compare with a profile
  likelihood (Δχ² = 3.84 for 95%) [src: same, Fig. 6 caption].
- **Prior weight versus prior volume.** DESI's diagnostics: MAP against
  posterior mean for one prior (prior-volume effect); MAP across priors
  (prior-weight effect) [src: arXiv:2411.12021, Sect. 4.5]. On noiseless
  data in w0waCDM the DR1 FS posteriors are "largely dominated by
  projection effects", even with post-reconstruction BAO added; Jeffreys
  priors reduce this but put strong priors on cosmology and fail when b₃
  is free [src: Sect. 4.5.2]. Informative priors from galaxy mocks reduce
  prior-volume effects, but results then "depend on the galaxy-halo model
  used to derive the prior" [src: Sect. 4.5].
- **Geometric information from FS alone is distorted.** DESI states that
  projection effects "significantly distort the geometrical information
  extracted from the full-shape analysis alone, even with a CMB prior on
  θ*", citing arXiv:2407.06117 [src: arXiv:2503.14744, Sect. VI].
- **Mock validation that does not test the FS neutrino pipeline.** The
  DR2 massive-neutrino mock test (Peregrinus, BGS-like HOD mocks at
  z = 0.3, M_r < −21.35) fits an isotropic BAO template plus a synthetic
  CMB prior and recovers Ω_m and Σm_ν,eff without bias for 0.059 and
  0.24 eV [src: arXiv:2503.14744, Sect. II.8]. It validates the BAO route,
  not the FS kernels or priors. FS-specific checks read here are the
  Quijote halo fits (FOLPSν: 0.4 eV recovered within 1σ at
  100 (h⁻¹Gpc)³, Table 2 of arXiv:2208.02791; co-evolution b_s² and
  b_3nl relations work "when the biased field is cb", Sect. 5) and
  noiseless synthetic data.
- **Total-matter bias.** Scale-dependent large-scale bias appears if bias
  is defined against total matter; defining it against cb reduces it
  (arXiv:1311.0866 [src]). Check which spectrum the code ingests.
- **Scale cut pushed too far.** One-loop errors grow fast: in PT Challenge
  and Nseries tests, k_max^P from 0.20 to 0.23 h/Mpc biases σ₈ up by 4–5%,
  k_max^B from 0.16 to 0.20 h/Mpc biases it down by 3%; the cancellation
  is "specific to the simulation set" [src: arXiv:2601.16165, Sect. 2.4].
  DESI finds no significant dependence on k_max for its P-only baseline
  [src: arXiv:2411.12021, Sect. 4.7, item 4].
- **Significance from different estimators.** The external 3.5σ (ΛCDM)
  comes from a truncated-Gaussian fit and the 2.4σ (w0waCDM) from the
  chain tail probability [src: arXiv:2601.16165, Sect. 4.3]; they are not
  the same construction.
- **Emulator drift.** Taylor emulators calibrated at one cosmology can be
  wrong far from it; DESI re-evaluates real-data chains with the full
  model [src: arXiv:2411.12021, Sect. 4.7].
- **Missing cross-covariances.** FS from one release with BAO from
  another, or P with B, needs a cross-covariance; DESI declines DR1 FS +
  DR2 BAO for that reason [src: arXiv:2503.14744, Sect. II.2]; the
  external analysis neglects P–B cross-covariance with stated
  justification and an open test [src: arXiv:2601.16165, Sect. 2.3].

## Reading list
<!-- key: reading-list -->

- Foundation (bias): Villaescusa-Navarro et al. 2014, arXiv:1311.0866 —
  why bias is defined against the cb field.
- Method (kernels): Noriega et al. 2022, arXiv:2208.02791 — fk-kernels,
  δ_ν ∝ δ_cb closure, Quijote validation.
- Method (pipeline): DESI 2024 V, arXiv:2411.12021 — bias basis, priors,
  hexadecapole and b₃ choices, prior-weight and prior-volume diagnostics.
- Method (comparison): Noriega et al. 2025, arXiv:2404.07269 — fk versus
  EdS on DESI-like synthetic data.
- Application: DESI 2024 VII, arXiv:2411.12022 — DR1 FS limits with and
  without CMB, and why the CMB-combined gain is geometric.
- Application: Elbers et al. (DESI) 2025, arXiv:2503.14744 — background-
  only, X_rsd and n_s tests; Peregrinus mocks.
- Method (diagnostic): Bertólez-Martínez et al. 2024, arXiv:2411.14524 —
  background versus perturbation masses.
- Critique: Noriega & Aviles 2024, arXiv:2407.06117 — projection effects in
  FS neutrino limits; wiggles carry the information.
- External reanalysis: Ivanov et al. 2026, arXiv:2601.16165 — bispectrum
  and cross-correlations, EdS + cb, and the geometric origin of the gain.

## Not verified
<!-- key: not-verified -->

- The velocileptors massive-neutrino module was read only through its
  file name and the one-line description in arXiv:2411.12022; its kernels
  were not read.
- The source of the 0.077 eV "official" DR1 value quoted in
  arXiv:2601.16165 was not identified.
- The external reanalysis's ref. [145], which justifies EdS kernels at
  current errors, and its ref. [13] on σ₈ as principal component, were not
  read.
- Brieden, Gil-Marín & Verde 2022 (DESI's ref. 41, BAO-amplitude route
  with fewer projection effects) was not read.
- No FS analysis of mocks with massive-neutrino particles through the
  full DESI DR1 FS pipeline was found in the sections read.
