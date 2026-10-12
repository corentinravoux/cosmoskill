# Results — dark energy and modified gravity

Scope: current headline constraints on the dark-energy equation of state and
on modified-gravity parameters, with the history of the key numbers.

Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` taken from a
named secondary source; `[der]` derived here, derivation stated.
Convention throughout: `w(a) = w0 + wa (1 - a)` (CPL), flat geometry unless
stated. "Significance" is the frequentist conversion of `Delta chi2_MAP` with
two extra degrees of freedom unless stated.

## 1. The `w0`–`wa` evidence: DESI collaboration numbers
<!-- key: the-w0-wa-evidence-desi-collaboration-numbers -->

### 1.1 DESI DR2 BAO (March 2025)
<!-- key: desi-dr2-bao-march-2025 -->

All rows are read from Section 7.1 and the table "Summary of the difference in
the effective chi2_MAP" of DESI Collaboration 2025, arXiv:2503.14738. `Delta
chi2_MAP` is `w0waCDM` minus `LCDM`; `Delta DIC = DIC(w0wa) - DIC(LCDM)`.

| Data combination | `w0` | `wa` | `Delta chi2_MAP` | Significance | `Delta DIC` | Flag |
|---|---|---|---|---|---|---|
| DESI BAO alone | −0.48 (+0.35/−0.17) | < −1.34 (68% limit) | −4.7 | 1.7σ | −0.8 | [src] |
| DESI + (θ*, ω_b, ω_bc) CMB priors | −0.43 ± 0.22 | −1.72 ± 0.64 | −8.0 | 2.4σ | −4.4 | [src] |
| DESI + CMB (no lensing) | — | — | −9.7 | 2.7σ | −5.9 | [src] |
| DESI + CMB | −0.42 ± 0.21 | −1.75 ± 0.58 | −12.5 | 3.1σ | −8.7 | [src] |
| DESI + Pantheon+ | — | — | −4.9 | 1.7σ | −0.7 | [src] |
| DESI + Union3 | — | — | −10.1 | 2.7σ | −6.0 | [src] |
| DESI + DESY5 | — | — | −13.6 | 3.3σ | −9.3 | [src] |
| DESI + DES Y3 3×2pt | — | — | −7.3 | 2.2σ | −2.8 | [src] |
| DESI + DES Y3 3×2pt + DESY5 | — | — | −13.8 | 3.3σ | −9.1 | [src] |
| DESI + CMB + Pantheon+ | −0.838 ± 0.055 | −0.62 (+0.22/−0.19) | −10.7 | 2.8σ | −6.8 | [src] |
| DESI + CMB + Union3 | −0.667 ± 0.088 | −1.09 (+0.31/−0.27) | −17.4 | 3.8σ | −13.5 | [src] |
| DESI + CMB + DESY5 | −0.752 ± 0.057 | −0.86 (+0.23/−0.20) | −21.0 | 4.2σ | −17.2 | [src] |

Reading notes, all [src] from the same paper (Sections 7.1 and 7.2 unless the
abstract is named):

- The DESI-alone posterior is cut off by the priors, so the marginalised mean
  and limit are prior-dependent; `wa = 0` is not excluded at 95%.
- The DESI + CMB-priors posterior is still bounded by the `wa > −3` prior at
  the lower end.
- Going from the three compressed CMB priors to the full CMB changes `Delta
  chi2` from −8.0 to −12.5; the paper attributes the change primarily to CMB
  lensing, which the compressed priors do not capture.
- Pivot: for DESI + CMB, `z_p = 0.53` and `w_p = −1.024 ± 0.043`; for DESI +
  CMB + DESY5, `z_p = 0.31` and `w_p = −0.954 ± 0.024`. At the best-measured
  redshift the equation of state is within about 2σ of −1; the signal is in
  the slope.
- In all cases the favoured `w(z)` has `w > −1` at low redshift and crosses to
  `w < −1` above `z ≃ 0.4`.
- ΛCDM comparison in the same paper: DESI BAO prefers `Omega_m = 0.297`
  against 0.317 for the Planck model; the joint fit gives 0.303. DESI
  distances lie 1–2% below the Planck ΛCDM prediction at `z ≤ 1`. The DESY5
  low-redshift (`z < 0.1`) supernovae sit at `mu − mu_fid ≈ 0.03` mag,
  Pantheon+ at only 0.01 mag.
- The best constant-`w` model for DESI + CMB + DESY5 has `w = −0.971`,
  `Omega_m = 0.310` and does only slightly better than Planck ΛCDM: a constant
  `w` does not absorb the signal.
- `w0waCDM` gives a lower `H0` than Planck ΛCDM; it does not help the Hubble
  tension.
- The BAO-versus-CMB tension in ΛCDM is 2.3σ (abstract).
- Neutrinos: `Sum m_nu < 0.064 eV` (95%, ΛCDM), `< 0.16 eV` in `w0wa`
  (abstract).

### 1.2 DESI DR1 BAO (April 2024) — superseded by DR2
<!-- key: desi-dr1-bao-april-2024-superseded-by-dr2 -->

| Data combination | Result | Flag |
|---|---|---|
| DESI BAO alone, `wCDM` | `w = −0.99 (+0.15/−0.13)` | [src] |
| DESI + CMB, `w0wa` | 2.6σ preference | [src] |
| DESI + CMB + Pantheon+ | 2.5σ | [src] |
| DESI + CMB + Union3 | 3.5σ | [src] |
| DESI + CMB + DES-SN5YR | 3.9σ | [src] |

DESI Collaboration 2024, arXiv:2404.03002, abstract. DR1 used over 6 million
objects in seven redshift bins over `0.1 < z < 4.2`; DR2 uses more than 14
million (arXiv:2503.14738, abstract) [src].

### 1.3 DESI extended dark-energy analysis (DR2)
<!-- key: desi-extended-dark-energy-analysis-dr2 -->

Lodha et al. 2025, arXiv:2503.14743, table of `Delta chi2_MAP` and `Delta DIC`
values [src]. Entries are `Delta DIC (Delta chi2)` relative to ΛCDM for DESI +
CMB + the named supernova sample. Negative favours the extended model.

| Dark-energy class | + Pantheon+ | + Union3 | + DESY5 |
|---|---|---|---|
| Thawing, calibrated | +0.4 (−1.6) | −0.6 (−2.5) | −5.8 (−7.1) |
| Thawing, algebraic (`w ≥ −1`, a second extra parameter) | −1.0 (−2.9) | −4.6 (−6.9) | −10.1 (−13.2) |
| Emergent | +2.1 (−0.05) | +1.8 (−0.1) | +0.2 (−1.5) |
| Mirage | −9.1 (−10.5) | −13.8 (−16.2) | −18.7 (−20.7) |
| `w0wa` | −6.8 (−10.7) | −13.5 (−17.4) | −17.2 (−21.0) |

- The scale the paper uses for nested models: a DIC decrease of at least 2 is
  "not insignificant", up to 5 "positive", up to 10 "strong", beyond 10
  "decisive" [src].
- The mirage class matches the `w0wa` fit quality because the mirage direction
  lies along the `w0`–`wa` degeneracy [src].
- Thawing models that respect `w ≥ −1` improve on ΛCDM by `3 ≲ −Delta chi2 ≲
  13` but are "considerably less favored" than `w0wa`; the comparison cannot
  be turned into a sigma level because the models are not nested [src].
- Abstract [src]: a two-parameter `w(z)` is sufficient to capture the trends
  even when binning and Gaussian processes add freedom; the data "indicate a
  clear preference for models that feature a phantom crossing; although
  alternatives lacking this feature are disfavored, they cannot yet be ruled
  out"; the evidence is described as robust "particularly at low redshift (z ≲
  0.3)".

## 2. The `w0`–`wa` evidence after the 2025–2026 supernova revisions
<!-- key: the-w0-wa-evidence-after-the-2025-2026 -->

The 4.2σ of Section 1.1 is superseded. The supernova side is treated in depth
in `cosmo-supernovae`; the rows below are the numbers this skill needs.

| Data combination | `w0` | `wa` | Significance | Source | Flag |
|---|---|---|---|---|---|
| DESI DR2 + CMB + DES-Dovekie | −0.803 ± 0.054 | −0.72 ± 0.21 | 3.2σ | Popovic et al. 2025, arXiv:2511.07517 | [src] |
| DESI DR2 + Planck + Union3.1 | −0.719 ± 0.084 | −0.95 (+0.29/−0.26) | 3.4σ (was 3.8σ) | Hoyt et al. 2026, arXiv:2601.19424 | [src] |
| DESI DR2 + Planck + DES-Dovekie, as recomputed by Hoyt et al. | — | — | 3.4σ (was 4.2σ) | arXiv:2601.19424 | [src] |
| DESI DR2 + Planck + Pantheon+ with corrected host masses | — | — | 3.2σ (was 2.8σ) | arXiv:2601.19424 | [src] |
| Unite (2884 SNe) + CMB + DES and DESI BAO | −0.861 (+0.044/−0.042) | −0.60 (+0.17/−0.19) | 3.3σ (MAP), 3.1σ (maximum likelihood); Bayesian evidence "only weak" | Camilleri et al. 2026, arXiv:2609.05053 | [src] |
| DES Y6 alone: SN + BAO + 3×2pt | −0.84 ± 0.10 | −0.44 (+0.60/−0.55) | 2.2σ | DES Collaboration 2026, arXiv:2605.27221 | [src] |
| DES Y6 + DESI DR2 BAO (low redshift only, no CMB) | −0.84 (+0.06/−0.07) | −0.53 (+0.33/−0.28) | 2.3σ | arXiv:2605.27221 | [src] |
| DES Y6 + DESI DR2 BAO + primary CMB | −0.82 ± 0.05 | −0.63 (+0.21/−0.18) | 3.0σ | arXiv:2605.27221 | [src] |
| Same without supernovae | — | — | 2.6σ | arXiv:2605.27221 | [src] |

- DES-Dovekie is quoted at 3.2σ by its own paper (arXiv:2511.07517) and at
  3.4σ by the Union3.1 paper (arXiv:2601.19424), which reruns the combination
  "exactly as done by DESI DR2". Both are in print; name the paper when
  quoting.
- Unite also gives `Omega_m = 0.305 ± 0.004` in `w0wa` and a dark-energy
  figure of merit of 315, a ~30% smaller `w0`–`wa` area than the DES Y6 + DESI
  DR2 + CMB combination [src].
- In arXiv:2605.27221, adding 3×2pt to SN + DESI BAO + CMB leaves the
  significance essentially unchanged (3.2σ to 3.0σ) and raises the figure of
  merit by ~10%; dropping any one probe gives 2.3–3.2σ, always with `w0 > −1`,
  `wa < 0` [src].
- The convergence is the result: three supernova samples that gave 2.8 / 3.8 /
  4.2σ now give 3.2 / 3.4 / 3.4σ (arXiv:2601.19424) [src].

## 3. DESI clustering beyond BAO
<!-- key: desi-clustering-beyond-bao -->

| Data | Model | Result | Source | Flag |
|---|---|---|---|---|
| DESI DR1 full shape (ShapeFit) + DR2 BAO, BBN and wide `n_s` prior, no CMB | `w0wa` | `wa = −1.52 ± 0.77`; discrepancy with ΛCDM 1.4σ; `w0` printed as "0.49 ± 0.25" in the abstract (the sibling `cosmo-galaxy-clustering` reports that the table gives −0.49) | Forero-Sánchez et al. 2026, arXiv:2602.18761 | [src] for the abstract; [sec] for the sign correction |
| Same data | ΛCDM | `Omega_m = 0.3035 ± 0.0085`, `h = 0.6876 ± 0.0059`, `sigma8 = 0.822 ± 0.034` | arXiv:2602.18761 | [src] |
| DESI DR1 P + LRG bispectrum + DR2 BAO, DESI only | `w0wa` | consistent with a cosmological constant within 1σ | Forero-Sánchez et al. 2026, arXiv:2606.23936 | [src] |
| + CMB | `w0wa` | 2.8σ | arXiv:2606.23936 | [src] |
| + DES-Dovekie only | `w0wa` | 1.6σ | arXiv:2606.23936 | [src] |
| + CMB + DES-Dovekie | `w0wa` | 3.1σ, "driven primarily by the CMB" | arXiv:2606.23936 | [src] |
| DESI only, P + B | μ0 | `mu0 = 0.12 ± 0.49` | arXiv:2606.23936 | [src] |

The bispectrum "consistently weakens evidence for time-varying dark energy
relative to power-spectrum-only analyses" (arXiv:2606.23936, abstract) [src].

## 4. Bayesian evidence for `w0wa` against Λ
<!-- key: bayesian-evidence-for-w0wa-against-lambda -->

`ln B = ln Z(w0wa) − ln Z(Λ)`, computed with PolyChord and anesthetic, same
priors as the posterior analysis (Lodha et al. 2025, arXiv:2503.14743,
appendix "Bayesian Model Comparison") [src]. Positive favours `w0wa`.

| DESI BAO + CMB + | Pantheon+ | Union3 | DESY5 |
|---|---|---|---|
| DR2: `ln B` | −0.66 ± 0.44 | 3.03 ± 0.44 | 4.88 ± 0.44 |
| DR2: `Delta <ln L>` (fit improvement) | 4.53 ± 0.17 | 7.78 ± 0.16 | 9.42 ± 0.16 |
| DR2: Occam penalty `Delta <ln(P/pi)>` | 5.18 ± 0.43 | 4.75 ± 0.43 | 4.54 ± 0.44 |
| DR1: `ln B` | −1.54 ± 0.44 | 1.62 ± 0.44 | 2.35 ± 0.44 |

An independent nested-sampling analysis of the same data gives different
numbers: `ln B = −0.57 ± 0.26` for DESI DR2 + Planck, `+3.32 ± 0.27` adding
DES-SN5YR and `−0.30 ± 0.19` adding DES-Dovekie [src] (arXiv:2511.10631,
abstract for the first; the other two as tabulated in
`cosmo-statistics-inference`). A Bayes factor scales with the prior volume, so
values from analyses with different priors are not comparable row by row; the
sign and the ordering between supernova samples are what the two analyses
share.

- The paper reads these on the Jeffreys scale as "almost a strong preference
  (≤ 5)" for DESY5, "moderate (≤ 2.5)" for Union3 with DR2, and
  "inconclusive", on the side of Λ, for Pantheon+ [src].
- With Pantheon+ the frequentist test gives 2.8σ for `w0wa` while the evidence
  mildly favours Λ: the same data, two opposite headlines.
- To make Λ favoured in the most extreme case (DR2 + CMB + DESY5), the prior
  range on both `w` parameters would have to be widened by more than a factor
  of 10 each, more than 100 in volume [src].
- After the supernova revisions: DES-Dovekie + CMB + DESI DR2 gives odds of
  "approximately 5:1", which the authors call "only a weak preference"
  (arXiv:2511.07517) [src]; that is `ln B ≈ 1.6` [der: natural logarithm of
  5]. Unite: "only weak preference" (arXiv:2609.05053) [src].
- Gu et al. 2025, arXiv:2504.06118 (DESI DR2, shape-function and
  non-parametric reconstructions with a Horndeski-motivated correlation
  prior): "moderate support" for departures from ΛCDM when several degrees of
  freedom in `w(z)` are allowed, corresponding to "≈ 3σ" [src].

## 5. Constant `w` and pre-DESI dynamical dark energy
<!-- key: constant-w-and-pre-desi-dynamical-dark-energy -->

| Quantity | Value | Data | Source | Flag |
|---|---|---|---|---|
| `w` | −0.99 (+0.15/−0.13) | DESI DR1 BAO alone | arXiv:2404.03002 | [src] |
| `w` | −0.971 (best fit) | DESI DR2 + CMB + DESY5 | arXiv:2503.14738 | [src] |
| `w` | −1.12 (+0.26/−0.20) | DES Y6 3×2pt alone | DES Collaboration 2026, arXiv:2601.14559 | [src] |
| `w` | −0.981 (+0.021/−0.022) | DES Y6 3×2pt + CMB + DESI DR2 BAO + DES SN + SPT clusters | arXiv:2601.14559 | [src] |
| `w` | −0.99 (+0.11/−0.13) | KiDS-1000 + BOSS + 2dFLenS 3×2pt | Tröster et al. 2020, arXiv:2010.16416 | [src] |
| (`w_p`, `wa`) | (−0.99 (+0.28/−0.17), −0.9 ± 1.2), `z_p = 0.24` | DES Y3 3×2pt alone | DES Collaboration 2022, arXiv:2207.05766 | [src] |
| (`w_p`, `wa`) | (−1.03 (+0.04/−0.03), −0.4 (+0.4/−0.3)), `z_p = 0.21` | DES Y3 + external data of 2022 | arXiv:2207.05766 | [src] |
| (`w0`, `wa`) | (−0.72 ± 0.21, −0.91 (+0.78/−0.64)) | BOSS DR12 full shape + pre-DESI BAO + DES Y3 3×2pt, no CMB, reparameterised EFT | Tsedrik, Carrilho and Moretti 2025, arXiv:2509.09562 | [src] |
| (`w0`, `wa`) | (−0.16 (+0.10/−0.50), −3.0 (+1.7)) frequentist | DESI DR1 full shape + BAO alone | Morawetz et al. 2025, arXiv:2508.11811 | [src] |

- A constant `w` close to −1 in every data set is what the pivot argument
  predicts and is not evidence against dynamics: Linder 2007, arXiv:0708.0024,
  shows that CMB data consistent with Λ make lower-redshift probes return `w =
  −1` "nearly automatically" unless they are sensitive to `w(z)` [src].
- DES Y6 3×2pt in ΛCDM: `S8 = 0.789 ± 0.012`, `Omega_m = 0.333
  (+0.023/−0.028)`; 1.8σ from the CMB in full parameter space, 2.6σ in `S8`
  alone; all DES probes 2.8σ; with DESI DR2 BAO, DES SN and SPT clusters 2.3σ
  (arXiv:2601.14559) [src]. The weak-lensing side is in `cosmo-weak-lensing`.
- Chen and Ivanov 2025, arXiv:2507.00118: adding the BOSS EFT power spectrum
  and bispectrum likelihood to DESI BAO + Planck + Pantheon+ makes the
  preference for dynamical dark energy "disappear"; simulation-based priors
  improve the figure of merit by ≈ 20% and shrink the posterior around Λ
  [src].
- Lu and Simon 2025, arXiv:2511.10616, find the opposite sign of effect with a
  different data vector: BOSS power spectrum and bispectrum plus DESI LRG ×
  Planck PR4 lensing and temperature angular spectra, combined with Planck
  PR4, DESI DR2 BAO and DES Y5 supernovae, raise the preference from 3.8σ to
  4.6σ; without BAO and supernovae they find 2.3σ [src]. The abstract names
  the DES Y5 supernovae, not DES-Dovekie; check which calibration a given
  version uses before quoting 4.6σ.

## 6. Modified gravity: phenomenological parameters
<!-- key: modified-gravity-phenomenological-parameters -->

Convention in the rows below: general relativity is `mu0 = Sigma0 = 0`. Time
dependence proportional to the dark-energy density, `mu(a) = 1 + mu0
Omega_DE(a)/Omega_DE,0` and the same for Σ (DES and DESI convention; see
`physics-and-methods.md` Section 4).

| Data | Background | `mu0` | `Sigma0` | Source | Flag |
|---|---|---|---|---|---|
| DESI DR1 (FS + BAO) + BBN + wide `n_s` prior | ΛCDM | 0.11 (+0.44/−0.54) | — | Ishak et al. 2024, arXiv:2411.12026 | [src] |
| DESI DR1 (FS + BAO) + CMB + DES Y3 + DESY5 SN | ΛCDM | 0.05 ± 0.22 | 0.008 ± 0.045 | arXiv:2411.12026 | [src] |
| Same | `w0wa` | −0.24 (+0.32/−0.28) | 0.006 ± 0.043 | arXiv:2411.12026 | [src] |
| DESI DR1 P + LRG bispectrum + DR2 BAO, DESI only | ΛCDM | 0.12 ± 0.49 | — | arXiv:2606.23936 | [src] |
| DES Y3 3×2pt alone | ΛCDM | — | 0.6 (+0.4/−0.5) | arXiv:2207.05766 | [src] |
| DES Y3 3×2pt + external data of 2022 | ΛCDM | 0.08 (+0.21/−0.19) | 0.04 ± 0.05 | arXiv:2207.05766 | [src] |
| KiDS-Legacy + CMB (Planck, ACT, SPT) + DESI DR2 BAO + DES-Dovekie | ΛCDM | 0.21 ± 0.21 | 0.149 ± 0.051 (3.0σ from GR) | Du et al. 2026, arXiv:2602.03110 | [src] |
| Same | `w0wa` | — | 2.2σ from GR | arXiv:2602.03110 | [src] |

- arXiv:2602.03110 is not a collaboration analysis. Its authors state that the
  Σ0 deviation "is likely driven by the higher amplitudes in the large-scale
  CMB lensing measurements" [src].
- Planck PR3 gave a tension of Σ0 with general relativity (Planck
  Collaboration 2018, arXiv:1807.06209, is the PR3 parameter paper); the DESI
  analysis finds that it "goes away when using LoLLiPoP+HiLLiPoP likelihoods"
  and relates it to the PR3 lensing anomaly (arXiv:2411.12026) [src]. The
  `A_L` history is in `cosmo-cmb`.
- With binned forms (2 redshift bins, then 2 × 2 bins in redshift and scale, 4
  and 8 parameters), "all MG parameters are found consistent with GR"
  (arXiv:2411.12026) [src].
- ACT DR6 + Planck + lensing + DESI DR1: data consistent with "the late-time
  growth rate predicted by general relativity"; no statistically significant
  preference for any extension (Calabrese et al. 2025, arXiv:2503.14454)
  [src].
- Rebouças et al. 2026, arXiv:2606.00411: in MG scenarios tied to the
  dark-energy sound speed, CMB + DESI DR2 BAO + Pantheon+ show deviations from
  GR at over 95% CL correlated with the dynamical-dark-energy preference; "the
  inclusion of cosmic shear and CMB lensing data significantly shifts the
  constraints towards GR" [src].

### Growth index
<!-- key: growth-index -->

| `gamma` | Data | Significance against 0.55 | Source | Flag |
|---|---|---|---|---|
| 0.633 (+0.025/−0.024) | Planck + weak lensing + clustering + velocities | 3.7σ | Nguyen, Huterer and Wen 2023, arXiv:2302.01331 | [src] |
| 0.639 (+0.024/−0.025) | `f sigma8` + Planck | 4.2σ | arXiv:2302.01331 | [src] |

The same abstract notes that in Planck data the suppressed growth "offsets the
preference for nonzero curvature and fits the data equally well" [src]: the
Planck part of the signal is the PR3 peak-smoothing anomaly in another
parameter. No DESI-collaboration value of γ was read this session (see "Not
verified" in `open-questions.md`).

### Horndeski / EFT of dark energy
<!-- key: horndeski-eft-of-dark-energy -->

| Parameter | Value | Data | Source | Flag |
|---|---|---|---|---|
| `Omega_0` (power-law non-minimal coupling) | 0.012 (+0.001/−0.012) | DESI DR1 (FS + BAO) + DESY5 SN + CMB, ΛCDM background | arXiv:2411.12026 | [src] |
| `s_0` (power-law index) | 0.996 (+0.54/−0.20) | same | arXiv:2411.12026 | [src] |
| `c_M` (α-basis, no braiding) | < 1.14 | DESI DR1 + external | arXiv:2411.12026 | [src] |
| `c_B` (α-basis, braiding free) | "mild yet consistent indication for c_B > 0" | DESI DR1 + external | arXiv:2411.12026 | [src] |
| `alpha_B`, `alpha_M` | compatible with GR at ~2σ; errors reduced by ~40% and ~50% | BOSS P + B, DESI LRG × Planck PR4, Planck PR4, DESI DR2 BAO, DES Y5 | arXiv:2511.10616 | [src] |
| Gravitational-wave speed | `abs(c_g/c − 1) ≤ 5 × 10^-16` | GW170817 + GRB 170817A | Ezquiaga and Zumalacárregui 2017, arXiv:1710.05901 | [src] |
| Gravitational-wave speed | deviations "smaller than a few × 10^-15" | same event | Creminelli and Vernizzi 2017, arXiv:1710.05877 | [src] |
| `G_cosmo/G_N` ("cosmic glitch") | 0.9920 ± 0.0025 (3.3σ) | Planck + ACT + SPT + DESI DR2 | arXiv:2609.40176 | [src] |

The chance probability of the GW170817–GRB 170817A coincidence is `5.0 ×
10^-8` (LIGO Scientific Collaboration et al. 2017, arXiv:1710.05834) [src].

## 7. Specific models and screening
<!-- key: specific-models-and-screening -->

| Model or quantity | Bound | Probe | Source | Flag |
|---|---|---|---|---|
| Hu–Sawicki `f(R)`, `n = 1` | `f_R0 < 1.4 × 10^-8` | galaxy morphology (gas–star offsets, disk warps) | Desmond and Ferreira 2020, arXiv:2009.08743 | [src] |
| Screened fifth force, strength | `Delta G/G_N < 0.8` at `lambda_C = 0.3 Mpc` to `< 3 × 10^-5` at 8 Mpc (1σ) | same | arXiv:2009.08743 | [src] |
| Hu–Sawicki `f(R)`, `n = 1` | `log10 abs(f_R0) < −4.79` (95.4%); the arXiv abstract prints "4.79" without the sign | X-ray cluster abundance + CMB + lensing | Cataneo et al. 2014, arXiv:1412.0133 | [src] |
| Hu–Sawicki `f(R)` | `log10 abs(f_R0) < −4.59` (95%); range `lambda < 17.81 Mpc`; mediator mass `m_phi > 3.60 × 10^-31 eV` | DESI DR1 full-shape power spectrum | Gonzalez et al. 2026, arXiv:2604.26915 | [src] |
| `f(R)` as a chameleon sub-case | `abs(f_R) ≲ (2–5) × 10^-5` (95%) for NFW and Hernquist profiles | lensing + kinematics of nine CLASH clusters | Pizzuti et al. 2026, arXiv:2604.23631 | [src] |
| Hu–Sawicki `f(R)` | unconstrained | KiDS-1000 cosmic shear, fully non-linear | arXiv:2010.16416 | [src] |
| Screened fifth force in the distance ladder | consistent with zero; `H0 = 73.1 ± 1.0 km/s/Mpc`, tension retained at > 5σ | SH0ES Cepheid–SN ladder with environment-dependent screening | Högås et al. 2025, arXiv:2512.14814 | [src] |

The cosmological-scale bounds (10^-5) and the galaxy-scale bound (10^-8)
differ by three orders of magnitude and probe different regimes; quote the one
that matches the claim.

## 8. `E_G` measurements
<!-- key: eg-measurements -->

| `E_G` | Redshift | Data | GR prediction quoted | Source | Flag |
|---|---|---|---|---|---|
| 0.39 ± 0.06 | — | galaxy lensing + clustering + growth rate, tens of Mpc (survey not named in the abstract) | ≈ 0.4 | Reyes et al. 2010, arXiv:1003.2185 | [src] |
| 0.243 ± 0.060 (stat) ± 0.013 (sys) | 0.57 | Planck CMB lensing × CMASS + RSD β, up to 150 Mpc/h | 2.6σ below GR | Pullen et al. 2015, arXiv:1511.04457 | [src] |
| 0.36 (+0.06/−0.05) | 0.555 | Planck lensing × CMASS, new estimator | 0.401 ± 0.005 | Wenzl et al. 2024, arXiv:2401.12971 | [src] |
| 0.40 (+0.11/−0.09) | 0.316 | Planck lensing × LOWZ | 0.452 ± 0.005 | arXiv:2401.12971 | [src] |
| consistent with GR + ΛCDM (no single number in the abstract) | up to z ~ 1 | BOSS and DESI DR1 × KiDS, DES, HSC | Planck cosmology | Rauhut et al. 2025, arXiv:2507.16098 | [src] |
| 0.31 (+0.06/−0.05); 0.34 ± 0.05 adding Planck PR4 lensing | 0.555 | ACT DR6 lensing × BOSS CMASS; GR value 0.401 ± 0.005 | consistent | Wenzl et al. 2024, arXiv:2405.12795 | [src] |
| 0.49 (+0.14/−0.11); 0.43 (+0.11/−0.09) adding Planck PR4 lensing | 0.316 | ACT DR6 lensing × BOSS LOWZ; GR value 0.452 ± 0.005 | consistent | arXiv:2405.12795 | [src] |
| 0.503 ± 0.054 | 0.38 | KiDS-1000 × BOSS/2dFLenS, no Planck prior | consistent | Zhang et al. 2026, arXiv:2604.24631 | [src] |
| 0.444 ± 0.054 | 0.61 | same | consistent | arXiv:2604.24631 | [src] |

- The Pullen et al. deviation appeared only above 80 Mpc/h [src]; the
  reanalysis by Wenzl et al. with matched effective redshifts and a calibrated
  estimator finds agreement and scale independence, with systematic budgets of
  2% (CMASS) and 3% (LOWZ) [src].
- arXiv:2604.24631 also reports the Weyl-potential amplitude `J` for CMASS
  1.50σ below the GR prediction with Planck 2018 priors, LOWZ consistent
  [src].

## 9. History of the key numbers
<!-- key: history-of-the-key-numbers -->

### 9.1 Significance of the `w0wa` preference (DESI BAO + CMB + supernovae)
<!-- key: significance-of-the-w0wa-preference-desi-bao -->

| Date | Release | Pantheon+ | Union3 | DES | Source |
|---|---|---|---|---|---|
| Apr 2024 | DESI DR1 BAO | 2.5σ | 3.5σ | 3.9σ (DES-SN5YR) | arXiv:2404.03002 [src] |
| Mar 2025 | DESI DR2 BAO | 2.8σ | 3.8σ | 4.2σ (DES-SN5YR) | arXiv:2503.14738 [src] |
| Nov 2025 | DES-Dovekie recalibration | — | — | 3.2σ | arXiv:2511.07517 [src] |
| Jan 2026 | Union3.1 and corrected Pantheon+ host masses | 3.2σ | 3.4σ | 3.4σ (Dovekie) | arXiv:2601.19424 [src] |
| May 2026 | DES Y6 SN + BAO + 3×2pt + DESI DR2 + CMB | — | — | 3.0σ | arXiv:2605.27221 [src] |
| Jun 2026 | DESI DR1 P + B + DR2 BAO + CMB + Dovekie | — | — | 3.1σ | arXiv:2606.23936 [src] |
| Sep 2026 | Unite (Pantheon+ ∪ DES) | 3.3σ (single combined sample) | — | — | arXiv:2609.05053 [src] |

Superseded at the snapshot: every DR1 significance; the DR2 values 2.8 / 3.8 /
4.2σ; `Omega_m` and distances of DES-SN5YR before Dovekie; Union3 (by
Union3.1). Still current: the DR2 BAO-only (1.7σ) and BAO + CMB (3.1σ) values,
which do not involve supernovae.

### 9.2 Without supernovae or without CMB
<!-- key: without-supernovae-or-without-cmb -->

| Combination | DR1 | DR2 | Source |
|---|---|---|---|
| DESI + CMB | 2.6σ | 3.1σ | arXiv:2404.03002, arXiv:2503.14738 [src] |
| DESI alone | — | 1.7σ | arXiv:2503.14738 [src] |
| DESI DR1 FS + DR2 BAO, no CMB | — | 1.4σ | arXiv:2602.18761 [src] |
| DES Y6 all probes + DESI DR2 BAO, no CMB | — | 2.3σ | arXiv:2605.27221 [src] |

### 9.3 Modified gravity
<!-- key: modified-gravity -->

- `E_G` at CMASS: 0.243 ± 0.060 (2015, 2.6σ low) → 0.36 (+0.06/−0.05) (2024,
  consistent) (arXiv:1511.04457, arXiv:2401.12971) [src].
- Planck Σ0: in tension with PR3, consistent with the PR4 likelihoods
  (arXiv:2411.12026) [src].
- Before the direct detection of the gravitational-wave speed, quartic and
  quintic Horndeski terms were viable dark-energy models; since October 2017
  only the conformally coupled subclass survives without tuning
  (arXiv:1710.05877, arXiv:1710.05901; Baker et al. 2017, arXiv:1710.06394)
  [src].
- No analysis of DESI DR2 full-shape data for modified gravity exists at the
  snapshot; the DESI numbers above are DR1 full shape, in some cases with DR2
  BAO.
