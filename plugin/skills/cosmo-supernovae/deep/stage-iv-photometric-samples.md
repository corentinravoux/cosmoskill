# Stage-IV photometric samples — cosmo-supernovae dossier

Scope: how a Hubble diagram is built when neither the supernova nor most
hosts have a spectrum (SN + host photometric-redshift fit, classifier
trained on simulations, BBC with photo-z and contamination, covariance),
what the Rubin LSST and Roman simulation analyses include and leave out,
which biases they still find, and what the one data test on DES shows.
Snapshot: 2026-10-19.
From: Roman HLTDS simulation (arXiv:2506.04402), Sects. III–IV; LSST fully
photometric analysis (arXiv:2512.06319), Sects. II–IV.

Already in L2, not repeated here: the headline FoM forecasts for LSST and
Roman and the Rubin + DESI follow-up forecast
(`surveys-and-data.md#planned-and-starting-facilities`); the Stage-IV
calibration requirement (`systematics.md#photometric-calibration-and-cross-calibration`,
and `deep/photometric-calibration.md`); DES-SN5YR classification, BEAMS and
host association (`physics-and-methods.md#photometric-classification`,
`physics-and-methods.md#selection-bias-bbc-and-beams`); unbinning and rebinning for photometric
samples (`deep/covariance-likelihood-blinding.md`, Step 4). Cadence and
survey design for SNe are in `cosmo-surveys-facilities/deep/cadence-time-domain.md`.

## How it is done
<!-- key: how-it-is-done -->

Notation: `z_phot` is the redshift fitted from SN plus host photometry,
`P_host(z)` the host photo-z PDF, `P_Ia` a classifier probability, `D_CC`
the simulated core-collapse distance distribution in BEAMS, `Delta_z =
(z_phot − z_true)/(1 + z_true)` in the Roman paper.

### Step 1. Simulate the survey as the data will be analysed
<!-- key: step-1-simulate-the-survey-as-the-data-will-be -->

The LSST analysis (DESC, "M25") is the reference implementation [src:
arXiv:2512.06319, Sect. II.2]:

- SNANA catalogue-level simulation at flat `Omega_M = 0.315`, `w = −1`;
  SALT3 with a NIR extension over 2000–20 000 Å, "linearly extrapolated down
  to zero flux at 500 Å" to avoid classification artefacts from `u`-band
  dropouts at high z [src: arXiv:2512.06319, Sect. II.2].
- Scatter: BS21 dust model with the P23 stretch and colour populations;
  `alpha_true = 0.15`, `beta_int_true = 2.12`, giving an effective fitted
  `beta ~ 3`, for which "there is no true effective beta value to compare
  with".
- Hosts from ELAsTiCC host libraries: correlations measured on 16 000
  Pan-STARRS galaxies mapped onto a few million CosmoDC2 galaxies, with
  separate libraries for Ia, II, Ibc and peculiar Ia; about half the
  galaxies have no neighbour within 10″. Host photometry at one-year
  co-added depth, `i ~ 25.4` [src: arXiv:2512.06319, Sect. II.2].
- Peculiar velocities Gaussian with 300 km/s, corrected in the analysis
  with the true value and a 200 km/s error [src: arXiv:2512.06319, Sect. II.2].
- Trigger: two detections separated by at least 30 minutes; DDF about
  1.0 mag deeper than WFD [src: arXiv:2512.06319, Sect. II.2].
- Rates (Eqs. 1–2): `R(z) = 2.5 × 10^-5 (1+z)^1.5 yr^-1 Mpc^-3` for
  z < 1 and `9.7 × 10^-5 (1+z)^-0.5` above; 91bg-like at ~12 % of the Ia
  rate; Iax following the star-formation history, normalised to
  `6 × 10^-6 yr^-1 Mpc^-3` at z = 0; core collapse split 0.7 Type II,
  0.3 Ibc. The low-z sample is 4200 generated SNe Ia so that selected
  events are ~10 % of the high-z Ia sample [src: arXiv:2512.06319, Sect. II.2].

Roman uses a rest-frame range of 2800–25 000 Å in simulation and fit [src:
arXiv:2506.04402, Sect. IV.1].

### Step 2. Associate hosts
<!-- key: step-2-associate-hosts -->

Directional-light-radius matching: `d_DLR = Delta theta / DLR`; the two
smallest are HOST1 and HOST2; a match needs `d_DLR < 4` [src:
arXiv:2512.06319, Sect. III.2.1]. The simulated hostless fraction is 2 %,
as in DES-SN5YR; at least one match for 98 % of events [src: Sect.
III.2.1, Table 5].

### Step 3. Fit SN + host photometric redshifts
<!-- key: step-3-fit-sn-host-photometric-redshifts -->

- **Five-parameter SALT3 fit** `{t0, x0, x1, c, z_phot}` minimising
  `chi2 = sum_i chi2_F,i + chi2_host + chi2_syst` (Eq. 3), with
  `chi2_F,i = [F_data − F_model]^2 / sigma_F^2 + 2 ln(sigma_F / sigma~_F)`
  (Eq. 4); the log term is needed because `sigma_F` depends on the fitted
  parameters, and `sigma~_F` is fixed after the first iteration. The host
  term is `chi2_host = −2 log P_host(z_phot)` (Eq. 5), from the PZFlow PDF
  stored as quantiles [src: arXiv:2512.06319, Sect. III.1, after the Kessler
  et al. 2010 formalism].
- **Band bookkeeping**: after each iteration a passband whose rest-frame
  central wavelength leaves 2800–17 000 Å is dropped (or re-added), and the
  iteration repeated [src: arXiv:2512.06319, Sect. III.1].
- **Systematic refits**: `chi2_syst = [(p_k − p_k^ref)/sigma_k^ref]^2`
  (Eq. 6) ties each systematic refit to the nominal fit, because "a small
  systematic perturbation ... can lead to an unphysical large change in
  SALT3-fitted values"; this cuts the common-event loss from 12 % to 4 %
  [src: arXiv:2512.06319, Sects. III.1, IV.4].
- **DES implementation on data** (Chen et al. 2024): the host photo-z is a
  prior, not a replacement; full SOMPZ `p(z)` stored as 11 quantiles, or
  Gaussian priors from SOMPZ, DNF and BPZ; extended SALT3 (2000–13 000 Å,
  extrapolated to zero at 500 Å) to avoid "artificially small chi2" fits
  that put low-z SNe at high z. Adding SN information cuts the host-only
  redshift scatter by ~50 % except with DNF, whose host photo-z is already
  more precise than the SN; SN + DNF has median bias −0.003 and scatter
  0.019; the full `p(z)` is not significantly better than its Gaussian
  approximation [src: arXiv:2407.16744, Sect. 4.2].
- **Roman** uses the host PDF mean and rms as a Gaussian prior [src:
  arXiv:2506.04402, Sect. IV.1]. Precision after cuts, `sigma_Delta_z`:
  host only 0.119 (WIDE) / 0.090 (DEEP) at `z_true` 0.3–0.6, where Roman
  bands miss the 4000 Å break; host + SN 0.039 / 0.020; at 0.6–3.0, host
  + SN 0.034 in both tiers [src: arXiv:2506.04402, Sect. IV.2, Table 5].

### Step 4. Apply cuts and freeze the sample
<!-- key: step-4-apply-cuts-and-freeze-the-sample -->

- LSST cuts: three bands with SNR > 4; `|x1| < 3`, `|c| < 0.3`, `sigma_x1 <
  1.0`, `sigma_t0 < 2 d`, fit probability > 0.05; low-z `0.01 < z_spec <
  0.08`; `0.01 < z_phot < 1.4`; fitted bands inside 2800–17 000 Å rest
  frame also at `z_phot ± sigma_z_phot`; valid bias correction in all
  variants; no cut on the classifier [src: arXiv:2512.06319, Sect. III.2].
- The true-Ia fraction goes from 15 % (physical rates) to ~50 % after the
  trigger and ~90 % after cuts [src: arXiv:2512.06319, Sect. III.2,
  Fig. 2].
- The first eight cuts are applied to the nominal analysis only, and
  variants process the same event list; the band-validity cut still costs
  3.3 % and the valid-biasCor requirement 0.51 % [src: arXiv:2512.06319,
  Sect. III.2].
- Roman cuts add SNRSUM > 40 over −15 to +45 rest-frame days and one
  epoch before −5 d and one after +20 d; the selection efficiency is ~1/3
  for SNe Ia and sub-percent for contaminants, largely because fits to
  contaminants land in `{z, x1, c}` cells with no SN Ia bias correction
  ("implicit classification cut") [src: arXiv:2506.04402, Sect. IV.1].

### Step 5. Classify with a network trained on the same simulation
<!-- key: step-5-classify-with-a-network-trained-on-the -->

- LSST: SCONE trained for 150 iterations on ~50 000 SNe Ia and ~50 000
  non-Ia after selection, ~3 hours, 98 % accuracy; the same procedure is
  meant for real data "to ensure that the training data has the same
  redshift range and selection effects as the data". Reason for SCONE: it
  needs photometry only, no accurate redshift, and modest resources [src:
  arXiv:2512.06319, Sect. III.3].
- Roman: SCONE on 30 000 SNe Ia and 15 000 non-Ia passing cuts; the
  classifier is poorly calibrated in WIDE (true-Ia fraction off the
  diagonal against `P_Ia`) and fairly well in DEEP; surviving contamination
  is mostly core collapse at z > 1, "where current rate measurements have
  large statistical uncertainties"; no LSST non-Ia were simulated in that
  paper [src: arXiv:2506.04402, Sect. IV.3].

### Step 6. Bias-correct with photo-z and contamination
<!-- key: step-6-bias-correct-with-photo-z-and -->

- BEAMS `D_CC` was evaluated in redshift bins; M25 moves it to a 3D grid in
  `{z, c, x1}` because of its "significant dependence on colour and
  stretch", and fixes a bug in which `D_CC` distances were not bias
  corrected (a few mmag) [src: arXiv:2512.06319, Sect. IV.4].
- **No explicit redshift error term.** Chen et al. set `sigma_mu^z = 0`
  because the floated redshift already inflates the errors of `m_x, x1, c`,
  and adding it double-counts through the correlated colour error
  (Eqs. 4–6) [src: arXiv:2407.16744, Sect. 4.7]. The physical reason is a
  self-correction: `z_phot` and colour errors are anti-correlated, so a
  0.01 shift in host `z_phot` moves `mu` nearly along `d mu/dz` of LCDM
  (Eq. 5); Roman finds "qualitative agreement" with the earlier LSST
  result over a wider redshift range [src: arXiv:2506.04402, Sects. IV.1,
  IV.5.1].
- **Error model.** With photo-z, adding the additive floor
  `sigma_floor^2(z, c, M*)` gives a BBC reduced `chi2` well below 1;
  Chen et al. keep only the multiplicative scaling `f(z, c, M*)`,
  hypothesising that corrections computed at the measured rather than true
  redshift cause bin migrations [src: arXiv:2407.16744, Sect. 5.4].
- Ruhlmann-Kleider et al. find that the photo-z and contamination bias "can
  be largely accounted for" if photo-z errors and contamination are put
  into the selection bias correction itself [src: arXiv:2207.03789,
  abstract].

### Step 7. Covariance and cosmology fit
<!-- key: step-7-covariance-and-cosmology-fit -->

- LSST variants (Table 4): Milky Way `E(B−V)` 5 %; HST calibration
  `0.007 × lambda`; LSST zero points 5 mmag; filter shifts 5 Å; `z_spec`
  shift `5 × 10^-5`; `z_phot` shift 0.01, described as "a naive coherent
  shift ... based on previous DES weak lensing" analyses [src:
  arXiv:2512.06319, Sect. III.2]. Fits use a CMB prior over 25 samples
  [src: Sect. IV.1].
- Roman: 30 systematics (12 zero points, 12 wavelengths, global 0.0071
  mag/µm, 0.05 % non-linearity over 4.5 dex, host `z_phot` shift 0.01,
  20 % larger host `z_phot` errors, `z_spec` shift `4 × 10^-5`, 5 % MW
  extinction); `C_stat` includes lensing `0.028 z`; only the nominal
  unbinned covariance is computed because of cost [src: arXiv:2506.04402,
  Sect. IV.5]. Note that this lensing coefficient is half the
  `0.055 z` of Pantheon+ (L2); the Roman paper gives no reason in the
  section read.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Spectroscopic hosts at low redshift or photo-z everywhere
<!-- key: spectroscopic-hosts-at-low-redshift-or-photo-z -->

Roman's photo-z fit efficiency "drops dramatically" for `z_true < 0.6`
relative to a `z_spec` analysis; the authors recommend host `z_spec` to
~0.6 (PRISM, Subaru) and/or bluer external bands (PS1, LSST, Euclid VIS)
[src: arXiv:2506.04402, Sect. IV.2]. The earlier LSST DDF study found that
adding SN + host photo-z events to the `z_spec` subset raised the FoM by
50 % and that a 0.01 photo-z systematic cost only 2 % of it, because most
z < 0.5 events had `z_spec`, the SN + host fit halves the photo-z bias,
and the redshift–colour anti-correlation self-corrects [src:
arXiv:2210.07560, abstract].

### Which host photo-z prior
<!-- key: which-host-photo-z-prior -->

On DES-SN5YR simulations, SN + SOMPZ or DNF priors recover `w` within
±0.02 against a statistical error of 0.03 [src: arXiv:2407.16744,
abstract]. On the data, relative to the spec-z analysis, `Delta w =
−0.019` (SOMPZ `p(z)`), −0.002 (SOMPZ Gaussian), −0.017 (DNF), consistent
with simulations to ~1 sigma; SN + flat prior and SN + BPZ are
"significantly discrepant" with simulations, without identified cause
[src: Sect. 5.3]. Host masses were still from spectroscopic redshifts and
the dust parameters from a spec-z fit [src: Sect. 6.1].

### Propagating redshift errors: refit, sample or self-correct
<!-- key: propagating-redshift-errors-refit-sample-or -->

On SNLS3 photometric SNe with JLA, refitting photo-z together with
cosmology "fails at correcting the cosmological bias", while sampling the
redshift resolution function "slightly reduces it" [src: arXiv:2207.03789,
abstract]. The reason given: selection keeps light curves compatible with
a SN Ia at their assigned redshift, so redshift outliers are rarely
Hubble-diagram outliers; about 3 % of SNe are 3-sigma Hubble outliers and
only 14 % of those come from 3-sigma redshift outliers; the strongest
outliers sit at z < 0.4, where distance changes fast with redshift [src:
Sect. 5.8]. The BBC analyses rely on the self-correction instead (Step 6).

### Binned, rebinned or unbinned
<!-- key: binned-rebinned-or-unbinned -->

| Analysis | Binned | Rebinned | Unbinned | Source |
|---|---|---|---|---|
| Roman + LSST, FoM with `C_tot` | 364 (HD size 45) | 479 (919) | 507 (14 585) | arXiv:2506.04402, Sect. V |
| LSST M25, FoM stat → stat+syst | 193 → 131 | 196 → 159 | 182 → 156 | arXiv:2512.06319, Table 8 |

Unbinned inversion costs scale as the cube of the HD size: a CPU ratio of
2500 against rebinned, close to the expected 4500 [src: arXiv:2506.04402,
Sect. V]. **Forecast** values throughout.

### P_Ia cut or full BEAMS
<!-- key: pia-cut-or-full-beams -->

Neither M25 nor Roman cuts on `P_Ia`. In M25 the cosmology bias disappears
when all true non-Ia are removed (a perfect classifier); a test with
`P_Ia > 0.01`, which rejects 75 % of non-Ia, was run [src:
arXiv:2512.06319, Sect. IV.4]; the authors state that their bias-test
effort "did not reduce the bias" [src].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| SALT3 SED range in simulation | 2000–20 000 Å, extrapolated to 0 at 500 Å | LSST M25 | arXiv:2512.06319 | Sect. II.2 |
| Fit band range (rest frame) | 2800–17 000 Å (LSST); 2800–25 000 Å (Roman) | M25; Roman | arXiv:2512.06319; arXiv:2506.04402 | Sect. III.1; Sect. IV.1 |
| Host depth | `i ~ 25.4` (1-yr co-add) | M25 | arXiv:2512.06319 | Sect. II.2 |
| Host match / hostless | `d_DLR < 4`; 2 % hostless | M25 | arXiv:2512.06319 | Sect. III.2.1 |
| True-Ia fraction | 15 % → ~50 % → ~90 % | M25 | arXiv:2512.06319 | Sect. III.2 |
| Common-event loss | 12 % → 4 % with `chi2_syst` | M25 | arXiv:2512.06319 | Sect. IV.4 |
| Classifier training | ~50 000 + ~50 000; 98 % accuracy | M25 | arXiv:2512.06319 | Sect. III.3 |
| Classifier training | 30 000 Ia + 15 000 non-Ia | Roman | arXiv:2506.04402 | Sect. IV.3 |
| SN Ia selection efficiency | ~1/3 (contaminants sub-percent) | Roman | arXiv:2506.04402 | Sect. IV.1 |
| Host + SN `sigma_Delta_z` | 0.039 / 0.020 (z 0.3–0.6); 0.034 (0.6–3) | Roman WIDE / DEEP | arXiv:2506.04402 | Table 5 |
| SN + DNF photo-z bias, scatter | −0.003, 0.019 | DES data | arXiv:2407.16744 | Sect. 4.2 |
| `Delta w` photo-z vs spec-z | −0.019 / −0.002 / −0.017 | DES data | arXiv:2407.16744 | Sect. 5.3 |
| Photo-z systematic | 0.01 coherent shift | M25, Roman | arXiv:2512.06319; arXiv:2506.04402 | Table 4; Sect. IV.5 |
| `w` bias, stat only (wCDM + CMB) | 0.0225 / 0.0126 / 0.0256 (binned / unbinned / rebinned) | M25 | arXiv:2512.06319 | Table 7 |
| `w_a` bias, stat+syst | 0.18–0.27 (~3–4 sigma) | M25 | arXiv:2512.06319 | Sect. IV.2 |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Residual bias in the simulations themselves.** M25 finds a stat-only
  `w` bias of 0.01–0.03 at ~3–8 sigma over 25 samples, and `w_a` biases of
  0.12–0.27 [src: arXiv:2512.06319, Sects. IV.1–IV.2]; Roman finds "a small
  but significant bias" for all binning methods, to which the poorly
  calibrated WIDE classifier "may contribute" [src: arXiv:2506.04402,
  Sect. V]. Both pipelines are still in development by their authors'
  statements.
- **Pathological high-z fits** when the SED model is too red-limited:
  filter dropouts give small `chi2` and push low-z SNe to high z [src:
  arXiv:2407.16744, Sect. 4.2].
- **Asymmetric migration at a redshift cut**: a bias at `z ≳ 0.8` from the
  `z = 1.2` cut, which keeps `z_phot < z_spec` events and rejects the
  others [src: arXiv:2407.16744, Sect. 4.2].
- **Double-counting redshift errors** through `sigma_mu^z` or the additive
  floor: reduced `chi2` well below 1 [src: arXiv:2407.16744, Sects. 4.7,
  5.4].
- **Core-collapse outliers at `z_pho < 0.5`** are mostly faint and bias
  `Omega_M` low; a combined Ia + CC bias correction does not remove it
  [src: arXiv:2207.03789, Sect. 6.3].
- **Systematics not yet modelled.** M25 omits the intrinsic-scatter model,
  classifier and training-set variants, photo-z PDF shapes beyond a shift,
  the rate–redshift model and the bias-correction cosmology [src:
  arXiv:2512.06319, Sect. III.2]; Roman omits SALT3 training zero points
  and model error, the intrinsic-scatter model and the contaminant rate
  versus redshift, "expected to add a significant contribution" [src:
  arXiv:2506.04402, Sect. IV.5]. Chen et al. add host masses and dust
  parameters derived with spec-z [src: arXiv:2407.16744, Sect. 6.1].
- **Discrepancy on the weight of classification in DES-SN5YR.** M25 says
  classification "contributes ~1/3 to the total DES-SN5YR systematic",
  citing Table 7 of arXiv:2401.02945 [src: arXiv:2512.06319, Sect. III.2];
  L2 quotes DES-SN5YR itself as less than 10 % (9 %) [src:
  arXiv:2401.02945, Sect. VII.1.5]. In that Table 7 the contamination
  group is 0.028 against a total systematic 0.076 on `sigma_w` [src:
  arXiv:2401.02945, Table 7]. The two statements may use different
  measures (a ratio of standard deviations or of variances); unresolved
  here.
- **Closure tests that look passed.** A machine-learning audit reports that
  redshift-binned diagnostics explain < 1 % of the residual variance while
  a gradient-boosted model predicts up to 98.2 % in LSST simulations and
  72.5 % on the DES 5YR spectroscopic sample [src: arXiv:2607.06734,
  abstract]; single-author result, abstract only.

## Reading list
<!-- key: reading-list -->

- Mitra et al. 2025, arXiv:2512.06319 — method: the reference fully
  photometric LSST pipeline, Sects. II–IV; read IV.4 for what was tried
  against the bias.
- Kessler et al. 2025, arXiv:2506.04402 — method / forecast: Roman HLTDS
  simulation and analysis, Sects. IV.1–IV.5 and V.
- Chen et al. 2024, arXiv:2407.16744 — application: the only test on real
  data (DES 5YR), with several host photo-z priors.
- Mitra et al. 2023, arXiv:2210.07560 — method: the earlier LSST DDF photo-z
  study and the self-correction argument.
- Ruhlmann-Kleider et al. 2022, arXiv:2207.03789 — critique / alternative:
  SNLS photometric sample, refitting versus sampling of redshift errors.
- Qu et al. 2021, arXiv:2106.04370 — method: SCONE (L2).
- Mitra 2026, arXiv:2607.06734 — critique: residual-closure audit (abstract).

## Not verified
<!-- key: not-verified -->

- Kessler et al. 2010, the SN + host photo-z formalism cited by M25 and
  Chen et al., was not identified or read.
- The outcome of the M25 `P_Ia > 0.01` test was not read beyond the
  authors' summary that the bias was not reduced.
- The reason for Roman's `0.028 z` lensing term.
- ELAsTiCC host-library papers, PZFlow, and the Roman instrument
  parameters (Appendix A of arXiv:2506.04402).
- Body of arXiv:2607.06734 and of arXiv:2210.07560 (abstracts only).
