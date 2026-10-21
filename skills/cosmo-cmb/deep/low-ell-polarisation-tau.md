# Low-ℓ polarisation likelihoods and τ — cosmo-cmb dossier

Scope: how τ is obtained from large-scale E-mode polarisation, step by step
(map degradation, foreground cleaning, cross-QML spectra, simulation-based
or approximate likelihoods, transfer-function correction, validation), the
reason each analysis gives for its choices, and how to choose between
SimAll, the SRoll2 likelihood, LoLLiPoP, pixel-based, maximum-entropy,
likelihood-free and ground-based approaches; values and the τ debate are
in the reference files.
Snapshot: 2026-10-16.
From: Planck 2018 V and VI (arXiv:1907.12875, arXiv:1807.06209); Snowmass
CMB white paper (arXiv:2203.07638), Sect. 6.1; CLASS (arXiv:2501.11904).

Already in L2, not repeated here: the τ values and their history
(`results.md#optical-depth-tau`), the systematics history (ADC
non-linearity, SRoll2, NPIPE) and the reionisation-model dependence
(`systematics.md#large-scale-polarisation-systematics-and-tau`), the
summaries of lowE, the SRoll2 likelihood and LoLLiPoP, including Eqs. 4–6
of arXiv:2309.10034
(`systematics.md#large-scale-polarisation-and-tau-planck-2018`,
`physics-and-methods.md#covariance-and-likelihood`), and the debate itself
(`open-questions.md#is-the-planck-large-scale-polarisation-value-of`).

## How it is done
<!-- key: how-it-is-done -->

Notation: C_ℓ is the EE power spectrum and D_ℓ = ℓ(ℓ+1)C_ℓ/2π; m = [Q, U]
is a polarisation map; QML is the quadratic maximum-likelihood
power-spectrum estimator; "cross-QML" is its version for two maps with
independent noise; N_side is the HEALPix resolution parameter.

### Step 1. Degrade the maps
<!-- key: step-1-degrade-the-maps -->

- Planck 2018 HFI works at N_side = 16, ℓ < 30. Maps are degraded in
  harmonic space with a cosine window: f(ℓ) = 1 for ℓ ≤ N_side;
  ½[1 + sin(πℓ/2N_side)] for N_side < ℓ ≤ 3N_side; 0 above
  (arXiv:1907.12875, Eq. 4). Stated reason: to limit aliasing [src:
  Sect. 2.2.1].
- SRoll2 adds 20 nK of diagonal regularisation noise to keep the
  covariances invertible [src: arXiv:1908.09856, Sect. 3].
- PR4 (LoLLiPoP) uses the kernel b_ℓ = ½{1 + cos[π(ℓ − 1)/(3N_side − 1)]}
  at N_side = 16 [src: arXiv:2309.10034, Sect. 3.1]. This is a different
  cosine form from Eq. 4 above.

### Step 2. Remove polarised foregrounds
<!-- key: step-2-remove-polarised-foregrounds -->

**Template fitting** (Planck 2018, SRoll2, CLASS). The cleaned map is
m̂ = (m − α m_sync − β m_dust)/(1 − α − β) (arXiv:1907.12875, Eq. 5). The
amplitudes minimise a χ² with covariance
C = S(C_ℓ) + [N + α² N_sync + β² N_dust]/(1 − α − β)² (Eq. 6), where S is
the signal covariance and N the noise covariance of each map [src:
Sect. 2.2.1].

- In Eq. 5 α multiplies the 30 GHz (synchrotron) map and β the 353 GHz
  (dust) map. Table 2 is consistent with this: an α is fitted only at
  100 GHz. The sentence after Eq. 5 names them in the opposite order
  [src: Sect. 2.2.1, Table 2].
- Planck fits synchrotron only at 100 GHz. Stated reason: to avoid
  auto-correlating residual 30 GHz systematics [src].
- The cleaning mask keeps f_sky = 0.70; spectrum masks go down to 0.30
  [src].
- SRoll2 cleans with its own 353 GHz map for dust, and WMAP K (for
  100 GHz) and Ka (for 143 GHz) for synchrotron [src: arXiv:1908.09856,
  Sect. 3, Table 1].
  - Its masks threshold the sum of dust intensity scaled to 143 GHz and
    synchrotron intensity scaled to 100 GHz, smoothed at 7.5°.
  - The masks are binary, without apodisation [src: Sect. 3, Fig. 6
    caption].
- CLASS adds the template uncertainties to the covariance:
  C = S + [N_c + α² N_s + β² N_d + σ_α² m_sᵀm_s + σ_β² m_dᵀm_d]/(1 − α − β)²
  (arXiv:2501.11904, Eq. 10) [src: Sect. V.3].

**Component separation** (PR4). LoLLiPoP cleans each detector-set map, and
each PR4 simulation, with Commander, using CMB, synchrotron and thermal
dust components. Stated reason: foregrounds are stronger relative to the
CMB in polarisation than in temperature, and C_ℓ templates in the
likelihood "is not accurate enough, especially at large angular scales"
[src: arXiv:2309.10034, Sect. 3.1].

### Step 3. Estimate a cross-spectrum with a quadratic estimator
<!-- key: step-3-estimate-a-cross-spectrum-with-a -->

- The QML estimator (Tegmark 1996, arXiv:astro-ph/9611174) is stated to be
  "unbeatable": no method gives smaller error bars on C_ℓ. Its crucial
  steps scale as n² in the number of pixels, and it handles any mask and
  noise [src]. Its polarisation extension disentangles E and B on a cut
  sky (Tegmark & de Oliveira-Costa 2000, arXiv:astro-ph/0012120) [src].
- The cross-spectrum version, xQML (Vanneste et al. 2018,
  arXiv:1807.02484), removes the noise bias and mitigates uncorrelated
  systematics. It is more optimal than pure pseudo-spectra, especially on
  large scales [src].
- Planck 2018: quasi-QML cross-spectrum of cleaned 100 × 143 GHz maps on
  the 50% mask [src: arXiv:1907.12875, Sect. 2.2.2].
  - The temperature map is Commander, smoothed to 440′ with 2 μK
    regularisation noise.
  - The signal covariance assumes an earlier Planck best fit.
  - The noise covariances are FFP8 matrices, which miss systematics.
    Stated reason this is acceptable: it costs variance, not bias [src].
- Stated reason for the cross-spectrum rather than an auto-spectrum: lower
  vulnerability to inaccurate noise bias, and no auto-correlation of
  systematics within a channel [src: arXiv:1907.12875, Sect. 2.2.6].
- CLASS coadds the cleaned Planck 100 and 143 GHz maps with diagonal
  weights and cross-correlates them with its 90 GHz map. Its xQML is
  modified to correct a pixel-space transfer matrix F for either map [src:
  arXiv:2501.11904, Sect. V.3].

### Step 4. Correct for map-making suppression where needed
<!-- key: step-4-correct-for-map-making-suppression-where -->

- NPIPE calibrates the 44–217 GHz channels with a polarised sky model
  built from 30 and 353 GHz. That model contains essentially only
  foregrounds, so the calibration partly suppresses CMB polarisation [src:
  arXiv:2007.04997, Sect. 4.3].
- The suppression is measured in simulations as
  C_ℓ^{CMB×output} = k_ℓ C_ℓ^{CMB×CMB} (Eq. 16). Here k_ℓ is a scale-,
  frequency- and mask-dependent factor, which must be squared for a power
  spectrum [src].
- About 64% of the EE quadrupole and 73% of the octupole are missing,
  about 30% at ℓ = 4–5 and 20% at ℓ = 6 [src].
- Stated reason for accepting it: a compromise between noisy but unbiased
  large-scale polarisation and filtering out the modes most compromised
  by calibration uncertainty under the Planck scan [src].
- The paper notes that LFI 2018 may also have been filtered, but its
  simulations cannot show it [src].
- PR4 spectra are divided by this transfer function before LoLLiPoP [src:
  arXiv:2309.10034, Sect. 3.1].
- CLASS's time-domain filtering leaves essentially zero power at the
  lowest ℓ before correction [src: arXiv:2501.11904, Sect. V.5].

### Step 5. Build the likelihood
<!-- key: step-5-build-the-likelihood -->

**Simulation-based, multipole by multipole** (Planck 2018 "SimAll",
arXiv:1907.12875, Sect. 2.2.3):

1. Clean 100 and 143 GHz, compute the data cross-QML spectrum.
2. Clean 300 FFP10 end-to-end simulations the same way and subtract the
   known input CMB, giving 300 "pure" noise + systematics + foreground-
   residual maps.
3. Draw 1000 parameter sets uniformly in 10⁹A_s = 0.6–3.8, τ = 0–0.14,
   r = 0–1 (Eq. 9), which spans 0–0.30 μK² in D_ℓ^EE and 0–0.20 μK² in
   D_ℓ^BB (Eq. 10).
4. Pair 300 Gaussian CMB maps for each set with the 300 noise maps:
   300 000 samples per multipole.
5. Interpolate the log histogram of C_ℓ^QML for each theory with a
   low-order polynomial f_ℓ^i (Eq. 11), and evaluate it at the data.
6. Interpolate the 1000 pairs in C_ℓ (g_ℓ), and sum:
   log ℒ ≈ Σ_{ℓ=2}^{29} g_ℓ(C_ℓ^data, C_ℓ) + const (Eq. 12).

- ℓ-to-ℓ correlations are ignored: ℒ = Π_ℓ ℒ_ℓ (Eq. 8) [src].
- Stated reasons for a simulation-based likelihood rather than an
  analytic one: the distribution of residual systematics is not known
  analytically; maps cannot be debiased of noise and systematics; and
  reliable noise-plus-systematics covariances cannot be built [src:
  Sect. 2.2.6].
- A direct τ likelihood gave the same constraint as the C_ℓ-based one
  [src: Sect. 2.2.3].
- In the cosmological fit, Ω_b h², Ω_c h², θ* and n_s are fixed; A_s and
  τ are both free [src].

**Simulation-based, on a τ grid** (SRoll2, arXiv:1908.09856, Sect. 4):

- 101 spectra for τ in [0, 0.1], with A_s varied so that
  10⁹A_s e^{−2τ} = 1.875 and other parameters fixed.
- 500 signal maps per grid point are combined with the 500 noise,
  systematics and foreground-residual simulations.
- Histograms are built ℓ by ℓ and τ by τ, and ln 𝒫 is smoothed by
  piecewise polynomials f_ℓ.
- The probability is 𝒫(data | τ) = exp Σ_{ℓ=2}^{29} f_ℓ (Eq. 2), assuming
  negligible correlation between multipoles [src].

CLASS follows the same logic with smoother tools (arXiv:2501.11904,
Sect. V.4, Eq. 11):

- 600 (τ, A_s) pairs, τ uniform in 0–0.3, with
  A_s e^{−2τ} = 1.884 × 10⁻⁹. This value differs from SRoll2's 1.875
  because each is taken from the Planck best fit the paper cites.
- 500 realisations per pair; a kernel density estimate per multipole
  gives the likelihood at the data.
- Gaussian-process interpolation in τ, then emcee with a Gaussian prior on
  10⁹A_s e^{−2τ} [src].

**Approximate analytic likelihood** (LoLLiPoP): the Hamimeche–Lewis
change of variables adapted to cross-spectra (L2). Its covariance comes
from PR4 simulations run through Commander and cross-QML. It is
marginalised over the covariance uncertainty following Sellentin–Heavens.
The foreground model is fixed in the simulations, so foreground-model
error is not included [src: arXiv:2309.10034, Sect. 4].

**Pixel-based likelihood** (LFI 70 GHz, NPIPE checks):
ℒ(C_ℓ) = (2π)^{−N/2} |M|^{−1/2} exp(−½ mᵀM⁻¹m) (arXiv:1907.12875,
Eq. 13). Here m is the foreground-mitigated T, Q, U map array of N pixels
and M its signal-plus-noise covariance [src: Sect. 2.3]. It needs a
reliable noise covariance, which is why HFI did not use it [src:
Sect. 2.2.6].

**Maximum entropy and likelihood-free** (de Belsunce et al. 2021,
arXiv:2103.14378, Sects. 4.2–4.3):

- momento (from the glass scheme) builds the least-presumptive sampling
  distribution consistent with computed moments of the cross-spectra:
  𝒫(x) ∝ π(x) e^{−λ_x x − λ_xx x²} for one statistic (Eq. 34), where π(x)
  is a reference measure and λ are Lagrange multipliers fixed by the
  moments.
- pydelfi uses density-estimation likelihood-free inference.
- Both extend to joint low-ℓ TT, TE, EE [src: Sect. 7].

### Step 6. Validate
<!-- key: step-6-validate -->

- Planck 2018 recovers input τ = 0.05 and 0.06 from 300 simulations as
  0.05032 ± 0.00048 and 0.05968 ± 0.00044, within 0.1σ of a single
  realisation. Likelihoods built from two halves of the simulations agree
  [src: arXiv:1907.12875, Sect. 2.2.4].
- Data–simulation PTEs ℓ by ℓ (Table 3): TE has outliers, e.g. 0.5% at
  ℓ = 19 [src: Sect. 2.2.2].
- The data scatter is smaller than the simulations predict. This is
  attributed to overestimated ADC non-linearity variance in the
  simulations [src].
- SRoll2 tests [src: arXiv:1908.09856, Sect. 4]:
  - masks of 20–60% (see L2);
  - ℓ_min up to 5, stable;
  - dropping one multipole: removing ℓ = 5 shifts τ by about 0.5σ,
    consistent with a 1.2σ fluctuation in simulations;
  - synchrotron tracers WMAP K, Ka or LFI 30 GHz agree;
  - 217 GHz instead of 353 GHz as dust tracer for 100 GHz agrees, with
    slightly larger errors;
  - TE alone gives τ = 0.057 (+0.012/−0.013).
- de Belsunce et al. test their three likelihoods on 100 SRoll2
  end-to-end simulations kept out of the noise estimation, with inputs
  τ = 0.05, 0.06, 0.07. None is significantly biased (table in Numbers)
  [src: arXiv:2103.14378, Sect. 5, Table 2].
- CLASS checks its pipeline on an unfiltered configuration and finds
  < 0.2σ deviation from the SRoll2 result across masks and multipole
  omissions [src: arXiv:2501.11904, Sect. V.4].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Cross-frequency or within-frequency splits
<!-- key: cross-frequency-or-within-frequency-splits -->

- de Belsunce et al. find that 100 ds1 × 100 ds2 and 143 ds1 × 143 ds2
  give τ higher than the 100 × 143 full-mission baseline by 0.8–2σ, for
  every likelihood [src: arXiv:2103.14378, Sect. 7].
- They read this as correlated systematics within a band that bias τ high
  by about 0.01 [src].
- Hence the stated rule in Planck: cross-frequency spectra only [src:
  arXiv:1907.12875, Sect. 2.2.6].

### Which multipoles carry τ
<!-- key: which-multipoles-carry-tau -->

- In Planck 2018, second-order ADC non-linearity leaves residuals at
  ℓ = 2–3 large enough that the τ constraint comes "almost entirely" from
  ℓ = 4 and 5 [src: arXiv:1907.12875, Sect. 2.2.6].
- SRoll2 halves the quadrupole and octupole errors relative to 2018 [src:
  arXiv:1908.09856, Sect. 3, Fig. 8].
- NPIPE instead suppresses ℓ = 2–3 by calibration and corrects for it
  (Step 4) [src: arXiv:2007.04997, Sect. 4.3].
- These are different trade-offs over the same multipoles.

### Simulation-based or approximate likelihood
<!-- key: simulation-based-or-approximate-likelihood -->

| Method | Assumes | Buys | Costs | Used by |
|---|---|---|---|---|
| SimAll / SRoll2 grid | simulations reproduce residual systematics; ℓ independent | no analytic noise model needed | few simulations (300 or 500), so accuracy is limited at low signal; EE only | Planck 2018 lowE; ACT DR6 (SRoll2) [src: arXiv:1907.12875, Sect. 2.2.3; arXiv:1908.09856, Sect. 4] |
| LoLLiPoP (Hamimeche–Lewis on cross-spectra) | near-Gaussian X_ℓ after the change of variable; simulation covariance | ℓ–ℓ′ covariance, analytic form, EE/BB/EB | foreground-model error not propagated | Planck PR4 [src: arXiv:2309.10034, Sect. 4] |
| momento (maximum entropy) | moments computable as a function of parameters | joint TT, TE, EE | Lagrange multipliers costly beyond low order | de Belsunce et al. 2021 [src: arXiv:2103.14378, Sect. 4.2] |
| pydelfi (likelihood-free) | the density estimator converges | flexible | joint TT, TE, EE needed compression, which lost information | de Belsunce et al. 2021 [src: Sect. 7] |
| Pixel-based | accurate noise covariance | exact Gaussian likelihood | needs a reliable systematics model | LFI 70 GHz; NPIPE checks [src: arXiv:1907.12875, Sect. 2.3; arXiv:2007.04997, Sect. 9.1] |

Same-data comparison: on SRoll1 and SRoll2 maps the three de Belsunce
likelihoods agree. With low-ℓ spectra alone they give τ up to about 0.8σ
higher than the simulation-based scheme of Planck. With the high-ℓ
CamSpec likelihood added, the SRoll2 momento EE result is very close to
the SRoll2 value, with a smaller formal error [src: arXiv:2103.14378,
Sect. 7].

### Fixed amplitude or free A_s
<!-- key: fixed-amplitude-or-free-as -->

- SRoll2 and the SimAll grid fix 10⁹A_s e^{−2τ} = 1.875 [src:
  arXiv:1908.09856, Sect. 4].
- The Planck 2018 low-ℓ-only fit leaves A_s and τ free with other
  parameters fixed [src: arXiv:1907.12875, Sect. 2.2.3].
- NPIPE notes that τ depends on whether A_s or r are fixed or
  marginalised, on EE-only versus TT-TE-EE data, and on sharp versus
  extended reionisation [src: arXiv:2007.04997, Sect. 9]. State which
  convention a quoted τ uses.

### Template cleaning or component separation
<!-- key: template-cleaning-or-component-separation -->

- Templates (Planck 2018, SRoll2, CLASS) are simple and checked with
  alternative tracers [src: arXiv:1908.09856, Sect. 4].
- In Planck 2018, the template scalings measured on FFP10 simulations do
  not fully match the data, a limitation that "is not correctable" with
  those data and simulations [src: arXiv:1907.12875, Sect. 2.2.1].
- Commander (PR4) is used because templates in the likelihood are not
  accurate enough at large scales, but the foreground model is then
  fixed in the simulations [src: arXiv:2309.10034, Sects. 3.1, 4].

### Ground-based measurement
<!-- key: ground-based-measurement -->

- CLASS × Planck reaches τ = 0.053 (+0.018/−0.019) over the f050 mask from
  ℓ_min = 2 [src: arXiv:2501.11904, Sect. V.4, Eq. 12].
- Its forecast model relaxes filtering as F → λ + (1 − λ)F (Eq. 16),
  where λ² approximates the improved transfer function at ℓ = 2, and
  scales noise with map depth. This assumes low-ℓ red noise scales with
  depth, which "might not hold" for polarised atmospheric emission; the
  forecast ignores foregrounds (**forecast**) [src: Sect. V.5].

### A τ prior when Planck large scales are not used
<!-- key: a-tau-prior-when-planck-large-scales-are-not -->

No paper read for this skill gives a rule; the published choices, each with
what it implies (details and the case for each side in
`open-questions.md#is-the-planck-large-scale-polarisation-value-of`):

- **Leave τ free.** The other data then set it: DESI BAO + high-ℓ CMB + CMB
  lensing give τ = 0.090 ± 0.012 in ΛCDM, and the evolving-dark-energy
  preference drops from about 3σ to about 1.5σ [src: arXiv:2504.16932].
  The result is a statement about what the other data prefer, not a τ
  measurement.
- **A ground-based prior.** CLASS × Planck, 0.053 (+0.018/−0.019) [src:
  arXiv:2501.11904, Sect. V.4]; independent of the Planck low-ℓ
  systematics in instrument and modulation, but its width does not exclude
  0.09 on its own (`open-questions.md`, about 2σ [der]).
- **A prior from reionisation astrophysics.** τ = 0.0552 with errors of a
  few 10⁻³ (arXiv:2601.09644) or 0.067 ± 0.011 (arXiv:2607.26373) [src, as
  quoted in `open-questions.md`]; these import a reionisation model, which
  `cosmo-reionization-21cm` covers.

State which choice was made, and show the result under a second one when
the conclusion depends on τ (dark-energy preference, Σm_ν, n_s).

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Resolution and range | N_side = 16; ℓ = 2–29 | Planck 2018 lowE, SRoll2 | arXiv:1907.12875; arXiv:1908.09856 | Sect. 2.2.1; Sect. 4 |
| Template scalings (×10²) | α = 1.83 ± 0.12 (100); β = 1.950 ± 0.014 (100), 4.078 ± 0.011 (143) | Planck 2018 | arXiv:1907.12875 | Table 2 |
| Template scalings (×10²) | α = 0.95 ± 0.07 (100, WMAP K), 1.63 ± 0.21 (143, Ka); β = 1.86 ± 0.015 (100), 0.0394 ± 0.014 (143) as printed | SRoll2 | arXiv:1908.09856 | Table 1 |
| Cleaning mask | f_sky = 0.70 | Planck 2018; SRoll2 | arXiv:1907.12875; arXiv:1908.09856 | Sect. 2.2.1; Sect. 3 |
| Simulation sets | 300 FFP10 (2018); 500 (SRoll2); 500 (CLASS) | — | arXiv:1907.12875; arXiv:1908.09856; arXiv:2501.11904 | Sects. 2.2.1; 3; V.4 |
| Theory draws | 1000 sets (SimAll); 101 τ values (SRoll2); 600 pairs (CLASS) | — | same | Sect. 2.2.3; Sect. 4; Sect. V.4 |
| MC recovery | 0.05032 ± 0.00048 (input 0.05); 0.05968 ± 0.00044 (input 0.06) | Planck 2018 | arXiv:1907.12875 | Sect. 2.2.4 |
| NPIPE EE suppression | 64% (ℓ = 2), 73% (ℓ = 3), about 30% (ℓ = 4–5), about 20% (ℓ = 6) | Planck PR4 | arXiv:2007.04997 | Sect. 4.3 |
| Likelihood tests, input 0.060 | τ_ML 0.0603 (SimLow), 0.0600 (momento), 0.0597 (pydelfi); mean σ 0.0063, 0.0057, 0.0060 | SRoll2 simulations | arXiv:2103.14378 | Table 2 |
| Within-band split bias | τ higher by 0.8–2σ, about +0.01 | SRoll2 | arXiv:2103.14378 | Sect. 7 |
| SRoll2 TE-only τ | 0.057 (+0.012/−0.013) | SRoll2 | arXiv:1908.09856 | Sect. 4, Eq. 4 |
| Removing ℓ = 5 | about 0.5σ shift; 1.2σ fluctuation in simulations | SRoll2 | arXiv:1908.09856 | Sect. 4 |
| CLASS × Planck | τ = 0.053 (+0.018/−0.019), f050, ℓ_min = 2 | CLASS 90 GHz × Planck | arXiv:2501.11904 | Sect. V.4, Eq. 12 |
| Amplitude held fixed | 10⁹A_s e^{−2τ} = 1.875 (SRoll2); A_s e^{−2τ} = 1.884 × 10⁻⁹ (CLASS) | — | arXiv:1908.09856; arXiv:2501.11904 | Sect. 4; Sect. V.4 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Systematics correlated within a frequency band.** They bias τ high by
  about 0.01 in detector-set auto-band crosses [src: arXiv:2103.14378,
  Sect. 7]. Test: compare inter- and intra-frequency combinations.
- **Simulations that overestimate a systematic.** The data scatter is
  smaller than the simulations, from overestimated ADC non-linearity
  variance. The variance is then slightly overestimated [src:
  arXiv:1907.12875, Sects. 2.2.2, 2.2.6]. Test: data–simulation PTEs per
  multipole.
- **Too few simulations at low signal.** With 300 simulations, a τ-based
  scheme can be inaccurate when low τ is explored [src: Sect. 2.2.3].
  Test: input–output recovery at τ = 0.05 and 0.06, and likelihoods built
  from half the simulations [src: Sect. 2.2.4].
- **Ignoring the map-making transfer function.** In NPIPE, quadrupole and
  octupole power is largely removed [src: arXiv:2007.04997, Sect. 4.3].
  Test: process simulations through the same calibration and measure k_ℓ
  (Eq. 16).
- **Low-ℓ TE.** Poor null PTEs persist in SRoll2, with slightly lower
  significance [src: arXiv:1908.09856, Sect. 4]. Planck 2018 excluded
  low-ℓ TE (L2).
- **Foreground mismatch between data and simulations.** Template
  scalings fitted on FFP10 do not match the data [src: arXiv:1907.12875,
  Sect. 2.2.1]. LoLLiPoP does not propagate foreground-model error [src:
  arXiv:2309.10034, Sect. 4]. Test: alternative tracers (WMAP K/Ka, LFI
  30 GHz; 217 GHz for dust) [src: arXiv:1908.09856, Sect. 4].
- **One multipole driving the result.** Test: leave-one-multipole-out and
  ℓ_min scans, with the expected shifts calibrated on simulations [src:
  Sect. 4].
- **Ground filtering.** It removes the lowest multipoles until the
  transfer matrix is corrected [src: arXiv:2501.11904, Sect. V.5]. Test:
  the transfer matrix built into the estimator (App. A of the paper, not
  read).

## Reading list
<!-- key: reading-list -->

- Foundation: Tegmark 1996, arXiv:astro-ph/9611174: the QML estimator.
- Foundation: Tegmark & de Oliveira-Costa 2000, arXiv:astro-ph/0012120: QML
  for polarisation, E/B separation on a cut sky.
- Method: Vanneste et al. 2018, arXiv:1807.02484: cross-spectrum QML
  (xQML), used by PR4 and CLASS.
- Method: Hamimeche & Lewis 2008, arXiv:0801.0554, and Mangilli et al. 2015,
  arXiv:1503.01347: the change of variable behind LoLLiPoP.
- Application: Planck Collaboration 2019, arXiv:1907.12875, Sect. 2.2: the
  SimAll recipe, its validation and stated caveats.
- Application: Pagano et al. 2019, arXiv:1908.09856: the SRoll2 τ-grid
  likelihood used by ACT DR6, with its stability tests.
- Application: Planck Collaboration 2020, arXiv:2007.04997, Sects. 4.3 and 9:
  the NPIPE large-scale transfer function.
- Application: Tristram et al. 2023, arXiv:2309.10034, Sects. 3.1 and 4:
  Commander cleaning and LoLLiPoP on PR4.
- Application: Li et al. 2025, arXiv:2501.11904: ground-based xQML with a
  transfer matrix, KDE likelihood, forecast.
- Critique: de Belsunce et al. 2021, arXiv:2103.14378: three likelihoods
  compared; within-band split bias.

## Not verified
<!-- key: not-verified -->

- The QML and xQML derivations: abstracts only, read through INSPIRE.
- The NPIPE τ values and their per-frequency comparison
  (arXiv:2007.04997, Sect. 9 beyond the pixel-based setup): not read.
- The density-estimation details of pydelfi (App. C of arXiv:2103.14378):
  not read.
- The CLASS transfer-matrix estimator (App. A of arXiv:2501.11904): not
  read.
- The β value at 143 GHz in Table 1 of arXiv:1908.09856 (0.0394 × 10⁻²)
  is copied as printed. The text uses β = 0.039 for the 353 GHz mask
  scaling, which suggests a typesetting difference not resolved here.
