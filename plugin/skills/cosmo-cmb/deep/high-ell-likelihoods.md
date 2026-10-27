# High-ℓ likelihoods and foreground modelling — cosmo-cmb dossier

Scope: how a high-ℓ TT/TE/EE likelihood is built from maps (splits, masks,
mode coupling, multipole cuts, foreground model or pre-cleaning, CMB-only
compression, fit checks), the reason each collaboration gives for its
choices, and how to choose between Plik, CamSpec, HiLLiPoP, ACT MFLike and
SPT-3G products; values already in the reference files are pointed to.
Snapshot: 2026-10-16.
From: Planck 2018 V (arXiv:1907.12875), Sect. 3; ACT DR6 foreground working
group (arXiv:2506.06274); Simons Observatory science goals
(arXiv:1808.07445), Sects. II.4 and IV.1.2.

Already in L2, not repeated here: the Gaussian band-power likelihood and
the covariance construction per analysis
(`physics-and-methods.md#covariance-and-likelihood`), the nuisance counts
and the lite caveat (`physics-and-methods.md#foregrounds-and-component-separation`),
the nuisance priors, parameter shifts and Plik–CamSpec and PR4–PR3
comparisons (`systematics.md#nuisance-priors-and-test-sizes-by-analysis`),
the ℓ ranges of ACT, SPT and Planck in P-ACT
(`physics-and-methods.md#from-time-ordered-data-to-band-powers`), and the
question of which Planck likelihood to use
(`open-questions.md#which-planck-likelihood`).

## How it is done
<!-- key: how-it-is-done -->

Notation: C_ℓ is the angular power spectrum, D_ℓ = ℓ(ℓ+1)C_ℓ/2π;
"ν_i × ν_j" denotes the cross-spectrum of frequency channels i and j;
a band power C_b or D_b is a weighted average of C_ℓ over a bin b;
"x-spectrum" is ACT's term for an average of cross-split spectra
(arXiv:2503.14452, Sect. III.3).

### Step 1. Use cross-spectra between independent splits only
<!-- key: step-1-use-cross-spectra-between-independent -->

| Analysis | Splits | Stated reason | Place |
|---|---|---|---|
| Plik (PR3) | half-mission maps HM1 × HM2; no auto-spectra | 2013 detector-set crosses carried correlated noise and a low-level bias; half-mission maps were "immune" at the sensitivity of the tests, at the price of fewer crosses | [src: arXiv:1907.12875, Sect. 3.2.1] |
| CamSpec (PR4) | NPIPE A/B detector-set maps; noise from half-ring differences (PR3 version: half-mission maps, odd–even ring differences) | NPIPE maps have no missing pixels, so none are masked | [src: arXiv:2205.10869, Sects. 3.1–3.2] |
| HiLLiPoP (PR4) | NPIPE detector-set maps at 100, 143, 217 GHz | — | [src: arXiv:2309.10034, Sect. 3.2.1] |
| ACT DR6 | n_d(n_d − 1)/2 cross-split spectra per array-band (n_d data splits); 15 TT, 10 EE and 16 TE x-spectra | avoid noise bias; TE and ET differ for cross array-bands | [src: arXiv:2503.14452, Sect. III.3] |
| SPT-3G D1 | C̄_ℓ = [N(N − 1)]⁻¹ Σ_{i≠j} C_ℓ^{ij} over N bundles (Eq. 27) | avoid noise bias and "co-temporal systematics" | [src: arXiv:2506.20707, Sect. IV.4] |

- A noise model is still needed, for the covariance only. The required
  fidelity is lower than for debiasing auto-spectra [src: arXiv:1907.12875,
  Sect. 3.2.1].
- Plik coadds TE and ET into one "TE" per frequency pair, with weights
  within 20% of 0.5. Stated reason: an unbinned TE+ET covariance would be
  about 8 GB (arXiv:1907.12875) [src: Sect. 3.2.1].
- Plik keeps the TE cross-frequency spectra separate. A single coadded TE
  (the CamSpec choice) would prevent fitting foreground and nuisance
  parameters together with cosmology [src: Sect. 3.2.1].

### Step 2. Mask, apodise and undo the mode coupling
<!-- key: step-2-mask-apodise-and-undo-the-mode-coupling -->

- **Plik.** Masks are built per frequency by thresholding high-frequency
  HFI maps: T66, T57, T47 in temperature and P70, P50, P41 in polarisation
  at 100, 143, 217 GHz (the number is the sky percentage kept) (arXiv:1907.12875)
  [src: Sect. 3.2.2].
  - Galactic masks are apodised with a 4.71° FWHM Gaussian, point-source
    and CO masks with 30′; the large apodisation costs about 10% of f_sky
    (arXiv:1907.12875) [src: Sect. 3.2.2].
  - Stated reason for apodising: to reduce correlations between C_ℓ
    estimates at different ℓ [src: arXiv:1907.12875, Sect. 3.2.2].
  - Point sources are not masked in polarisation. Masking them changes
    EE 100×100 by less than 3 × 10⁻⁶ μK² in C_ℓ and moves n_s and A_s by
    about 0.1σ with EE alone, and has no detected effect on the joint
    likelihood (arXiv:1907.12875) [src: Sect. 3.2.2].
- **CamSpec PR4.** One diffuse mask keeping 80% of the sky before
  apodisation ("mask80") at all frequencies in T and P. The point-source
  mask is per frequency in T, and the 143 GHz mask is used for all
  frequencies in P [src: arXiv:2205.10869, Sect. 3.2].
- **HiLLiPoP V4.2.** Galactic masks remove 20%, 30% and 45% of the sky at
  100, 143, 217 GHz, leaving effective sky fractions of 75%, 66% and 52%
  after the other masks [src: arXiv:2309.10034, Sect. 3.2.1].
  - Masks are built from smoothed 353 GHz maps; Galactic masks are
    apodised with a 1.0° taper, CO and source masks with 15′
    (arXiv:2309.10034) [src: Sect. 3.2.1].
  - The masks are about 5% larger than in the previous HiLLiPoP. Stated
    reason: Planck is sample-variance limited to ℓ ≃ 1800 in TT and
    ℓ ≃ 1100 in TE (arXiv:2309.10034) [src: Sect. 3.2.1].
  - One point-source mask for all three channels, with higher flux cuts
    (about 340, 250, 200 mJy; arXiv:2309.10034). Stated reason: it preserves Galactic
    compact structures, so the dust spectra stay power laws; the PR3
    source masks remove cirrus and create a knee near ℓ = 200 [src:
    Sects. 3.2.1, 5.2].
  - The same mask is used for T and P, because it simplifies the
    covariance [src: Sect. 3.2.1].
- **ACT DR6.** MASTER pseudo-C_ℓ (Hivon et al. 2001,
  arXiv:astro-ph/0105302) in `pspy`, with harmonic transforms for the CAR
  pixelisation [src: arXiv:2503.14452, Sect. III.3].
  - The sky area (25% after Galactic and > 15 mJy source cuts at f150) is
    large enough to invert the unbinned mode-coupling matrix exactly
    (arXiv:2503.14452) [src: Sect. III.3].
  - Spectra are rebinned with Δℓ_min = 50 (arXiv:2503.14452) [src:
    Sect. III.3].
- **SPT-3G D1.** Polspice on the curved sky with a border-only mask. More
  than 2000 sources and clusters are filled by Gaussian constrained
  realisations (inpainting, Eq. 20) instead of being masked, with the
  covariance increased to account for the simulated signal [src:
  arXiv:2506.20707, Sects. IV.3–IV.4].
  - Stated reason (arXiv:2506.20707): in simulations, source holes raise the variance at
    ℓ = 3000 by 50%, through correlations between large and small scales;
    inpainting raises it much less [src: Sect. IV.3, Fig. 8].
  - The paper states this is the first use of inpainting in a primary-CMB
    analysis [src].

### Step 3. Correct for filtering
<!-- key: step-3-correct-for-filtering -->

- ACT removes ground pickup by cutting Fourier modes with |ℓ_x| < 90
  and |ℓ_y| < 50. It measures the bias as a matrix F_ℓ from 800 noise-free
  simulations per array-band, and inverts it [src: arXiv:2503.14452,
  Sect. III.3.1].
  - The ℓ–ℓ′ coupling of the filter is neglected, because its correlation
    length is smaller than a bin [src].
  - The fiducial model behind these corrections matters much less than
    the experimental errors [src: Sect. III.3, footnote 9].
- SPT starts at ℓ_min = 400, where the transfer function exceeds 0.5 (the
  filter's hard limit is ℓ = 300). Stated reason: avoid scales where the
  Monte Carlo precision of the transfer function would limit the analysis
  [src: arXiv:2506.20707, Sect. IV.4].

### Step 4. Choose multipole ranges and binning per spectrum
<!-- key: step-4-choose-multipole-ranges-and-binning-per -->

Plik (arXiv:1907.12875, Table 13) [src: Sect. 3.2.4]:

| Spectrum | TT | TE, EE |
|---|---|---|
| 100×100 | 30–1197 | 30–999 |
| 100×143 | not used | 30–999 |
| 100×217 | not used | 505–999 |
| 143×143 | 30–1996 | 30–1996 |
| 143×217 | 30–2508 | 505–1996 |
| 217×217 | 30–2508 | 505–1996 |

Stated reasons for the Plik cuts [src: Sect. 3.2.4]:

- 100×100 TT stops at 1197 (arXiv:1907.12875, Sect. 3.2.4), kept from 2015 for comparison with the
  detector-set likelihood, and because odd–even and half-mission null
  tests show signs of failure at similar scales.
- 100×143 and 100×217 TT are left out: little extra S/N, more foreground
  complexity (arXiv:1907.12875, Sect. 3.2.4).
- Polarisation: 100 GHz spectra stop at 1000 (noise); 217 GHz spectra
  start at 500 (dust modelling) (arXiv:1907.12875, Sect. 3.2.4).

HiLLiPoP V4.2 (arXiv:2309.10034, Table 1) uses ℓ = 30–2500 in T and
30–2000 in P, with per-pair limits: TT 100×100 [30, 1500], 143×143
[50, 2000], 217×217 [250, 2500]; EE 100×100 [100, 1200]. That gives
29 758 multipoles in total (10 646 TT, 9816 TE, 9296 EE), against 25 597
for its PR3 version. The stated rule: drop low ℓ for spectra involving
217 GHz (dust) and stop at 1500 for spectra involving 100 GHz (noise)
[src: Sect. 3.2.3].

CamSpec PR4 drops 100 GHz from temperature. Stated reasons: CO and
synchrotron at 100 GHz are hard to model, the channel is noisy at high ℓ,
and 143 and 217 GHz already determine TT [src: arXiv:2205.10869,
Sect. 3.3].

SPT-3G D1 stops TT at 3000, where foregrounds dominate all six
cross-frequency spectra, and TE/EE at 4000. Extending TT to 4000 would
reduce the ΛCDM error on Ω_b h² by 10% with TT alone, and those on N_eff
and n_s by 1% and 3% with T&E [src: arXiv:2506.20707, Sect. IV.4].

Binning:

- Plik: Δℓ = 5 (30–99), 9 (100–1503), 17 (1504–2013) and 33 (2014–2508),
  weighted by ℓ(ℓ+1) (arXiv:1907.12875, Eq. 22). Unbinned versions exist
  for feature searches [src: Sect. 3.2.5].
- SPT: Δℓ = 50, uniform in D_ℓ [src: arXiv:2506.20707, Sect. IV.4].
- HiLLiPoP: ℓ by ℓ, with a semi-analytic covariance (Xpol) computed from
  the data without simulations (Eq. 3) [src: arXiv:2309.10034,
  Sects. 3.2.3–3.2.4].

### Step 5. Model or remove the foregrounds
<!-- key: step-5-model-or-remove-the-foregrounds -->

Two strategies are in use.

**(a) Parametric templates fitted in the likelihood** (Plik, HiLLiPoP, ACT
MFLike, SPT-3G). ACT's model, written for delta-function passbands in CMB
thermodynamic units, with pivot ℓ₀ = 3000 and ν₀ = 150 GHz [src:
arXiv:2503.14452, Sect. VI.1.1]:

- radio sources:
  D_ℓ^{X_iY_j,radio} = a_s^XY [ℓ(ℓ+1)/ℓ₀(ℓ₀+1)] [g(ν_i)g(ν_j)/g²(ν₀)]
  (ν_iν_j/ν₀²)^{β_s+2} (Eq. 18). Here g(ν) converts flux to thermodynamic
  units, and TE amplitudes may be negative;
- Poisson CIB (arXiv:2503.14452), a modified blackbody μ(ν; β_p, T_d) ≡ ν^β B_ν(T_d) g(ν) with
  T_d = 9.6 K (Eq. 19); clustered CIB, Planck-measured to ℓ = 3000 and then
  ℓ^0.8 (Eq. 20);
- tSZ: a_tSZ D_ℓ^tSZ (ℓ/ℓ₀)^{α_tSZ} f(ν_i)f(ν_j)/f²(ν₀) (Eq. 21), with
  f(ν) = x coth(x/2) − 4 and x = hν/k_B T_CMB;
- kSZ: a template rescaled by a_kSZ (Eq. 22);
- tSZ × CIB: amplitude −ξ√(a_c a_tSZ) (Eq. 23);
- Galactic dust (arXiv:2503.14452): a power law in ℓ with α^TT = −0.6, α^{TE/EE} = −0.4,
  T_d^eff = 19.6 K and β_d = 1.5, all fixed (Eq. 24).

The tilt α_tSZ is new to this analysis. Stated reason: the nominal
template disagrees in shape with the Agora and BAHAMAS predictions [src].

Plik models extragalactic foregrounds in temperature only (Galactic dust
also in TE and EE, L2): a CIB halo-model template
perfectly correlated across 100–217 GHz, one flat point-source amplitude
per spectrum, kSZ, tSZ and tSZ × CIB templates, and the prior
D^kSZ + 1.6 D^tSZ = (9.5 ± 3) μK² (arXiv:1907.12875, Eq. 23).
Extragalactic foregrounds in TE and EE are ignored, because ground-based
data show polarised sources below Planck's sensitivity. The CIB is named as
the largest modelling uncertainty [src: Sect. 3.3.1].

HiLLiPoP builds its dust template by fitting A ℓ^{α_d} + B to 353 GHz
detector-set cross-spectra for each mask pair, over ℓ = 30–1500 in TT and
30–1000 in TE/EE. The template is extrapolated by
c_dust (a_ν/a_353)(a_ν′/a_353), with a_ν = ν^{β_d} B_ν(19.6 K) (Eq. 8). It
also adds two point-source populations, radio and dusty star-forming
galaxies [src: arXiv:2309.10034, Sect. 5.2].

**(b) Spectrum-level cleaning, then residual power laws** (CamSpec). Each
spectrum is cleaned with a template frequency ν_T, 545 GHz for TT and
353 GHz for TE and EE (arXiv:2205.10869) [src: Sect. 3.3]:

C^{X_ν1Y_ν2, clean} = (1+α^{X_ν1})(1+α^{Y_ν2}) C^{X_ν1Y_ν2}
− (1+α^{X_ν1}) α^{Y_ν2} C^{X_ν1Y_νT} − (1+α^{Y_ν2}) α^{X_ν1} C^{Y_ν2X_νT}
+ α^{X_ν1} α^{Y_ν2} C^{X_νTY_νT} (arXiv:2205.10869, Eq. 1).

- α′ (arXiv:2205.10869) minimises the cleaned auto-spectrum over ℓ = 100–500 (TT, where dust
  dominates over the CIB) or 30–300 (polarisation). The coefficient used
  is α = α′/(1 + α′), because the minimisation is biased [src: Sect. 3.3].
- In polarisation, above ℓ = 150 a power-law fit to the dust is
  subtracted instead, to limit 353 GHz noise (arXiv:2205.10869) [src:
  Sect. 3.3].
- Stated payoff: all TE and EE spectra can be coadded, with no polarised
  foreground nuisance parameters. TT keeps a power-law residual per
  frequency pair [src].

### Step 6. Compress to a CMB-only ("lite") likelihood
<!-- key: step-6-compress-to-a-cmb-only-lite-likelihood -->

The multi-frequency model is written as C_b^th = A C_b^CMB + C_b^sec(θ) +
C_b^sys (arXiv:1907.12875, Eq. 51) [src: Sect. 3.5.2]. Here:

- A is a 0/1 mapping matrix, the same CMB at all frequencies;
- C_b^sec are the foregrounds, with 20 nuisance parameters θ (arXiv:1907.12875,
  Sect. 3.5.2);
- C_b^sys holds fixed residual leakage, sub-pixel and correlated-noise
  terms.

The CMB band powers and θ are Gibbs-sampled: a Gaussian draw of the CMB
band powers given θ, then Metropolis–Hastings for θ given the CMB [src:
arXiv:1907.12875, Sect. 3.5.2; arXiv:2510.09430, Sect. II.2]. Jense et al.
write the conditional Gaussian with covariance Q = Mᵀ Σ⁻¹ M (Eq. 8) and
mean D̂^res = Q⁻¹ Mᵀ Σ⁻¹ (D̂ − D^sec(θ₂)) (Eq. 9). Here M is the mapping
matrix, Σ the multi-frequency covariance, D̂ the multi-frequency data and
θ₂ the nuisance parameters; samples are D̂^res + L y with Q = LLᵀ (Eq. 10)
[src]. The method goes back to the ACT CMB-only likelihood of Dunkley et
al. 2013 (arXiv:1301.0776) [src].

| Product | Band powers | Nuisance kept | Validation | Place |
|---|---|---|---|---|
| Plik_lite | 613 (215 TT, 199 EE, 199 TE) | overall calibration y_P | ΛCDM and +N_eff, +Σm_ν, +A_L within 0.1σ; TT errors up to ×2 at small scales from source marginalisation | [src: arXiv:1907.12875, Sect. 3.5.2, Eq. 54] |
| ACT-lite | 135 (45 each), CMB extracted to ℓ = 6500, foregrounds marginalised with data to 8500 | one calibration, one polarisation efficiency | within 0.1σ, ΛCDM and extensions | [src: arXiv:2503.14452, Sect. VI.2, App. F] |
| SPT-lite | 1392 → 196 data points; 43 → 2 nuisances (A_cal, E_cal); about 50× faster | global T and P calibrations, kept to minimise bin-to-bin correlations; aberration kept | ≲ 0.1σ shifts, widths within 10% | [src: arXiv:2506.20707, Sect. V.4] |
| CamSpec-NPIPE-lite | from the CamSpec model; six TT residual parameters marginalised; A_planck, C^TE, C^EE left to the user | three calibrations | n_s 9% wider; extensions 5–10% wider | [src: arXiv:2510.09430, Sects. II.2, III.2.1] |

SPT exploits the differentiability of its candl likelihood for the
compression [src: arXiv:2506.20707, Sect. V.4].

### Step 7. Check the fit and propagate biases
<!-- key: step-7-check-the-fit-and-propagate-biases -->

- Plik reports χ² against the TT,TE,EE+lowE+lensing best fit, in two
  forms: binned multi-frequency, which is sensitive to inter-frequency
  disagreement, and coadded unbinned, which is sensitive to the ℓ-by-ℓ
  statistical model [src: arXiv:1907.12875, Sect. 3.6.1, Table 20].
  Values are in Numbers.
- SPT translates any band-power bias δD into a parameter bias,
  δθ = F⁻¹ (∂D/∂θ) Σ⁻¹ δD, with F the Fisher matrix and Σ the band-power
  covariance, at the best fit using automatic differentiation. Higher
  orders are negligible [src: arXiv:2506.20707, Sect. V.3]. This
  propagated inpainting residuals, covariance changes and beam models
  quickly; final results still use MCMC [src].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Fit foregrounds per frequency, or pre-clean
<!-- key: fit-foregrounds-per-frequency-or-pre-clean -->

- Per-frequency fit (Plik, HiLLiPoP, ACT, SPT): the CMB is locked across
  frequencies by its blackbody spectrum, which separates it from
  foregrounds whose amplitude changes with frequency.
- Pre-cleaning (CamSpec): the residual power differs from one frequency to
  the next, so that separation is lost. CMB-only marginalisation still
  works, but foreground posteriors become broad and fully degenerate, one
  per spectrum [src: arXiv:2510.09430, Sect. II.2, Fig. 3 caption].
- Jense et al. let amplitudes go negative in the compression. Stated
  reason: a positivity prior truncates one tail of the broadened Gaussian
  posterior [src: Sect. II.2].

### Sky fraction and frequencies
<!-- key: sky-fraction-and-frequencies -->

- CamSpec-NPIPE is more constraining in TE and EE at all scales and in TT
  above ℓ = 1500 [src: arXiv:2510.09430, Sect. III.2.2].
- Plik-Legacy is more constraining in TT below ℓ = 1200, because it
  includes 100×100 (arXiv:2510.09430) [src: Sect. III.2.2].
- Jense et al. attribute the gain to more data in NPIPE and to
  pre-cleaning, which keeps more sky [src].

### Point-source holes or inpainting
<!-- key: point-source-holes-or-inpainting -->

- Holes keep the data unaltered. They raise the variance through mode
  coupling, by 50% at ℓ = 3000 for SPT-3G depth [src: arXiv:2506.20707,
  Sect. IV.3].
- Inpainting needs a covariance correction and a residual-bias check,
  which SPT propagated with its Fisher shortcut [src: Sect. V.3].

### Truncate Planck when combining with ground data
<!-- key: truncate-planck-when-combining-with-ground-data -->

P-ACT keeps Planck PR3 at ℓ < 1000 (TT) and ℓ < 600 (TE/EE). Stated
reasons [src: arXiv:2503.14452, Sect. VI.3]:

- the sky overlap with ACT is substantial;
- ACT has similar or better power at the discarded multipoles;
- the TT correlation over 600 < ℓ < 1000 is neglected because Planck's
  errors are smaller there (arXiv:2503.14452, Sect. VI.3);
- PR3 rather than NPIPE, partly because ACT agrees less well with the
  NPIPE 100 GHz ET spectra (arXiv:2503.14452, Sect. VI.3);
- keeping all of Planck with the cross-covariance was estimated to gain
  less than 5% on σ(N_eff).

On the cut range, Plik-Legacy-lite and CamSpec-NPIPE-lite agree better
than on the full range [src: arXiv:2510.09430, Sects. III.2.2–III.2.3]:

| | Full range | Cut range |
|---|---|---|
| Largest parameter shift | about 1σ in Ω_b h² | about 0.4σ in Ω_b h² |
| Δχ² between the two best fits | 2.88 (CamSpec data), 3.83 (Plik data) | 1.75, 1.76 |

Caveat: when scales are truncated, CamSpec foreground marginalisation can
change parameter inference and model selection; a lite likelihood built
on the full range avoids this [src: arXiv:2510.09430, abstract].

### Lite or multi-frequency
<!-- key: lite-or-multi-frequency -->

- Use a lite likelihood for combinations and extended models [src:
  arXiv:2510.09430, abstract].
- Use the multi-frequency likelihood for single spectra or subsets:
  SPT-lite is built for the full T&E set [src: arXiv:2506.20707,
  Sect. V.4].
- In ACT-lite, EE is better constrained than in MFLike, because foreground
  and calibration parameters shared with T are marginalised once with the
  T block included [src: arXiv:2503.14452, App. F].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| Plik masks (T; P) | T66, T57, T47; P70, P50, P41 | Planck PR3 | arXiv:1907.12875 | Sect. 3.2.2 |
| Plik apodisation | 4.71° FWHM (Galactic), 30′ (sources, CO); about −10% f_sky | Planck PR3 | arXiv:1907.12875 | Sect. 3.2.2 |
| CamSpec mask | 80% before apodisation, all channels | Planck PR4 | arXiv:2205.10869 | Sect. 3.2 |
| HiLLiPoP effective f_sky | 75%, 66%, 52% (100, 143, 217 GHz) | Planck PR4 | arXiv:2309.10034 | Sect. 3.2.1 |
| HiLLiPoP source flux cuts | about 340, 250, 200 mJy; 8.3% of sky | Planck PR4 | arXiv:2309.10034 | Sect. 3.2.1 |
| HiLLiPoP multipoles | 29 758 (PR3 version 25 597) | Planck PR4 | arXiv:2309.10034 | Sect. 3.2.3, Table 1 |
| CamSpec cleaning ranges | TT 100–500; P 30–300; P power-law subtraction above ℓ = 150 | Planck PR4 | arXiv:2205.10869 | Sect. 3.3 |
| ACT sky and source cut | 25%; > 15 mJy at f150 | ACT DR6 | arXiv:2503.14452 | Sect. III.3 |
| ACT ground filter | \|ℓ_x\| < 90, \|ℓ_y\| < 50; 800 simulations per array-band | ACT DR6 | arXiv:2503.14452 | Sect. III.3.1 |
| ACT x-spectra | 15 TT, 10 EE, 16 TE | ACT DR6 | arXiv:2503.14452 | Sect. III.3 |
| SPT ℓ_min | 400 (transfer function > 0.5) | SPT-3G D1 | arXiv:2506.20707 | Sect. IV.4 |
| SPT variance from source holes | +50% at ℓ = 3000 | SPT-3G D1 | arXiv:2506.20707 | Sect. IV.3 |
| Plik χ², binned | TT 760.68/765 (PTE 0.54); TE 857.36/762 (0.0090); EE 742.96/762 (0.68); TTTEEE 2344.94/2289 (0.20) | Planck PR3 | arXiv:1907.12875 | Table 20 |
| Plik χ², coadded unbinned | TTTEEE 6657.02/6413 (PTE 0.016); TE PTE 0.050 | Planck PR3 | arXiv:1907.12875 | Table 20 |
| TE χ² gain 2015 → 2018 | −73.72, half from the beam-leakage correction | Planck PR3 | arXiv:1907.12875 | Sect. 3.6.1 |
| SZ prior | D^kSZ + 1.6 D^tSZ = (9.5 ± 3) μK² | Planck PR3 | arXiv:1907.12875 | Eq. 23 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Inter-frequency disagreement in TE.** It shows as a low binned TE PTE
  (0.009 in Plik) while the coadded spectrum fits better [src:
  arXiv:1907.12875, Sect. 3.6.1]. TE-specific polarisation-efficiency
  corrections improve χ² by only about 9 [src]. Test: report binned and
  coadded χ² separately.
- **Noise correlations between detector sets.** They bias the
  cross-spectra; this drove Plik to half-mission splits (arXiv:1907.12875) [src:
  Sect. 3.2.1].
  Test: odd–even and half-mission null tests by spectrum. Such tests set
  the 100×100 TT cut [src: Sect. 3.2.4].
- **A spurious dust knee near ℓ = 200,** created by source masks that
  remove Galactic structure [src: arXiv:2309.10034, Sect. 5.2]. Test: the
  353 GHz cross-spectra for each mask pair should be power laws.
- **Mode coupling from many small holes.** Variance grows at high ℓ [src:
  arXiv:2506.20707, Sect. IV.3]. Test: simulated covariance with and
  without the source mask.
- **Filter transfer function poorly sampled at low ℓ.** It is the reason
  for SPT's ℓ_min = 400 (arXiv:2506.20707) [src: Sect. IV.4]. Test: the Monte Carlo
  precision of the transfer function.
- **Lite likelihood used outside its range.** Truncating after
  marginalisation, or using a lite likelihood for single spectra, can
  bias results [src: arXiv:2510.09430, abstract; arXiv:2506.20707,
  Sect. V.4]. Test: compare with the multi-frequency likelihood on the
  same range; the published criterion is agreement within 0.1σ.
- **Positivity priors in compression.** They truncate broadened
  posteriors and cause disagreement with the full likelihood [src:
  arXiv:2510.09430, Sect. II.2].
- **A band-power bias of unknown cosmological impact.** Propagate it with
  δθ = F⁻¹ (∂D/∂θ) Σ⁻¹ δD before deciding whether to rerun chains [src:
  arXiv:2506.20707, Sect. V.3].

## Reading list
<!-- key: reading-list -->

- Foundation: Hivon et al. 2001, arXiv:astro-ph/0105302: the MASTER
  pseudo-C_ℓ estimator used by ACT and others.
- Foundation: Dunkley et al. 2013, arXiv:1301.0776: the multi-frequency
  foreground model and the first CMB-only compression.
- Method: Efstathiou & Gratton 2019, arXiv:1910.00483: the CamSpec
  pipeline, 80% sky, temperature cleaning [src: abstract].
- Application: Planck Collaboration 2019, arXiv:1907.12875, Sect. 3: Plik
  splits, masks, cuts, foregrounds, Plik_lite, goodness of fit.
- Application: Rosenberg et al. 2022, arXiv:2205.10869: CamSpec on NPIPE,
  the dust-cleaning equation.
- Application: Tristram et al. 2023, arXiv:2309.10034: HiLLiPoP masks,
  ℓ-by-ℓ likelihood, dust template from 353 GHz. [src: Sect. 1]
- Application: Louis et al. 2025, arXiv:2503.14452: ACT DR6 pseudo-C_ℓ
  pipeline, foreground equations, ACT-lite, Planck truncation.
- Application: Camphuis et al. 2025, arXiv:2506.20707: inpainting,
  differentiable likelihood, SPT-lite.
- Critique: Jense et al. 2025, arXiv:2510.09430: Plik against CamSpec on
  full and cut ranges; marginalisation pitfalls.

## Not verified
<!-- key: not-verified -->

- The Efstathiou & Gratton 2019 and Hivon et al. 2001 bodies: abstracts
  only. Dunkley et al. 2013: abstract only.
- The CamSpec multipole cuts (described only qualitatively in Planck 2018
  V, Sect. 3.2.4) and the CamSpec temperature residual model in detail.
- The ACT DR6 foreground validation on simulations (arXiv:2506.06274):
  not re-read this session; see L2.
- The SPT-3G D1 inpainting residual-bias size and the extra covariance
  term (Eqs. 26 and 36 of arXiv:2506.20707): not read.
