# Type Ia supernova cosmology — systematics

Scope: the canonical systematic effects of an SN Ia Hubble-diagram analysis,
one subsection each: mechanism, quantified size, standard mitigation,
validation test, and the paper a referee expects cited. Ends with a referee
checklist.
Snapshot: 2026-10-13

Flags: `[src]` read in the cited paper this session; `[sec]` from a named
secondary source; `[der]` derived here.

## 0. The budget at a glance
<!-- key: the-budget-at-a-glance -->

SN cosmology is a *differential* measurement between low and high redshift.
Any effect that changes brightness, colour or selection as a function of
redshift, or between the anchor surveys and the deep survey, maps directly
onto `Omega_m` and `w`. A constant offset does not: it is absorbed by `M`.

| Analysis | Quantity | Statistical | Systematic | Largest groups | Source |
|---|---|---|---|---|---|
| JLA (2014) | `sigma(Omega_m)`, flat LCDM, SNe only | 0.0241 (51.6 % of the variance) | calibration 0.0203; Milky Way extinction 0.0072; light-curve model 0.0069; bias corrections 0.0040; host relation 0.0038; contamination 0.0008; peculiar velocities 0.0007 | Calibration (36.7 % of the variance); with the SNLS3 calibration errors the total would be 15 % larger | Betoule et al. 2014, arXiv:1401.4064 `[src: Sect. 6.2 and its table]` |
| Pantheon+ | `sigma_w`, flat wCDM, with Planck | about 0.03 (table note); systematic/statistical ratio 0.79 | 0.019 (unbinned); calibration 0.013 in arXiv:2112.03864 | Redshift bias 0.011; calibration through training and fitting 0.009; SALT2 method 0.008; Milky Way `E(B−V)` 0.008. Scatter model and populations are negligible when unbinned | arXiv:2202.04077 `[src: Table 4, Sect. IV.5]`; arXiv:2112.03864 `[src]` |
| DES-SN5YR | `sigma_w`, flat wCDM, SNe only | 0.132 | 0.076 (total 0.152) | "SALT3 + calibration" 0.052; dust-model variants 0.019–0.027 each | arXiv:2401.02945 Table 7 `[src]` |
| DES-SN5YR + CMB prior | `sigma_w` | 0.032 | 0.019 (total 0.036) | same | arXiv:2401.02945 `[src]` |
| DES-Dovekie | `sigma_w`, SNe only | — | photometric group 0.075 (was 0.057 after the weighting error); SALT3 + calibration 0.066; dust group 0.101, "the largest", about twice calibration | Astrophysics, then calibration | arXiv:2511.07517 Sec. 9 `[src]` |
| Unite | `sigma_QH` at z = 0.2 | 0.015 | 0.015 | SALT3 + calibration; SN astrophysics | arXiv:2609.05053 Sec. 6 `[src]` |

Individual entries of the DES tables are evaluated one at a time and do not
add in quadrature to the total; correlations cancel in the full covariance
(see `physics-and-methods.md` Section 7). The situation in one sentence:
DES-SN5YR alone was statistics-dominated, while the largest combined sample
(Unite) is at parity, with calibration and SN astrophysics sharing the
systematic part.

### 0.1 Pantheon+ (Brout et al. 2022, arXiv:2202.04077)
<!-- key: pantheon-brout-et-al-2022-arxiv-2202-04077 -->

Flat wCDM, with Planck 2018; each term alone, `sigma_w = sqrt(sigma_tot^2 -
sigma_stat^2)` `[src: Eq. 17, Table 4]`; "binned": same budget in 20 redshift
bins `[src: Table 6]`. No contamination term: spectroscopic sample `[src: Sect. II.1]`.

| Term (baseline → variant, prior scaling) | sigma_w | Delta w | binned |
|---|---|---|---|
| All systematics | 0.019 (0.79 of statistical) | −0.009 | 0.029 |
| SALT2 training + light-curve fit: Fragilistic best fit → 10 covariance realisations, 1/3 each | 0.009 | 0.000 | 0.019 |
| SALT2 method: SALT2-B22 → JLA surface, 1/3 | 0.008 | +0.003 | 0.009 |
| CSP tertiary stars / HST CALSPEC 2020 update → 5 mmag per 7000 Å | 0.003 / 0.003 | −0.003 / −0.006 | 0.005 / 0.002 |
| Peculiar-velocity map: 2M++ → 2M++ line-of-sight integrated and 2MRS | 0.002 | +0.005 | not run |
| Redshift bias: none → coherent `10^-4` shift (row label; Sect. III.1.2 says `+4 × 10^-5`) | 0.011 | +0.015 | 0.012 |
| Intrinsic scatter: BS21 dust model → G10 and C11 | 0.002 | −0.003 | 0.009 |
| Milky Way `E(B−V)` 4 % scaling (5 % in Sect. III.2.3) / colour law Fitzpatrick 1999 → Cardelli et al. 1989, 1/3 | 0.008 / 0.006 | −0.010 / −0.006 | 0.012 / 0.007 |
| Mass-step location `10^10` → `10^10.2 M_sun` / selection efficiency (exposure time +20 %) / populations (BS21 → 3 P21 sets) | 0.001 / 0.004 / 0.000 | 0.000 / +0.001 / +0.003 | 0.001 / 0.008 / 0.011 |

Redshift-only terms do not shrink when unbinned `[src: Appendix B]`. `H0`
(flat LCDM, with SH0ES): SN part of the error 0.7 km/s/Mpc, of which
systematic 0.29 `[src: Sect. IV.5]`.

### 0.2 DES-SN5YR and DES-Dovekie (arXiv:2401.02945; arXiv:2511.07517)
<!-- key: des-sn5yr-and-des-dovekie-arxiv-2401-02945 -->

Flat wCDM, SNe only, no CMB prior. `sigma_w`: the term alone against statistics
only ("leave-one-out"); `delta w`: shift with it alone ("add-one-in"). Bold rows
are sums of their components `[src: Table 7 of each; arXiv:2401.02945 Sect. VII.1; arXiv:2511.07517 Sect. 9]`.

| Term | 5YR sigma_w | 5YR delta w | Dovekie sigma_w | Dovekie delta w |
|---|---|---|---|---|
| Total / statistical / systematic | 0.152 / 0.132 / 0.076 | −0.032 (total) | 0.142 / 0.11 / not printed | |
| **Calibration and light-curve model**: SALT3 + calibration / HST CALSPEC (5 mmag per 7000 Å) | 0.057: 0.052 / 0.006 | −0.036 / +0.002 | 0.075: 0.066 / 0.009 | −0.073 / −0.001 |
| **SN Ia astrophysics** | 0.133 | | 0.124 | |
| Dust population 1 / 2 / 3 | 0.019 / 0.024 / 0.020 | −0.010 / +0.003 / −0.004 | 0.006 / 0.021 / 0.025 | +0.001 / −0.004 / −0.009 |
| Dust split on host `u−r` colour / dust model as in BS21 / SN-age model (W22) | 0.000 / 0.027 / 0.000 | +0.048 / −0.006 / +0.048 | 0.0 / 0.029 / 0.02 | +0.029 / −0.007 / −0.008 |
| `alpha` / `beta` / `gamma` evolution | 0.020 / 0.000 / 0.011 | −0.008 / −0.007 / −0.001 | 0.013 / 0.0 / 0.003 | −0.002 / −0.001 / 0.0 |
| Mass-step location / `sigma_int` modelling | 0.000 / 0.013 | −0.002 / −0.002 | 0.0 / 0.007 | 0.0 / 0.0 |
| **Milky Way extinction**: 5 % scaling / Cardelli colour law (weight 1/3) | 0.034: 0.020 / 0.014 | −0.011 / −0.003 | 0.041: 0.024 / 0.017 | −0.011 / −0.006 |
| **Survey modelling**: shallower host catalogue / shifted spectroscopic-redshift efficiency | 0.015: 0.009 / 0.005 | +0.002 / +0.002 | 0.002: 0.0 / 0.002 | +0.006 / 0.0 |
| **Contamination**: SCONE / SNIRF / SuperNNova retrained / core-collapse prior | 0.028: 0.006 / 0.013 / 0.006 / 0.003 | 0.000 / −0.003 / 0.000 / 0.000 | 0.018: 0.003 / 0.002 / 0.01 / 0.003 | 0.0 / 0.0 / −0.001 / −0.001 |
| **Redshift**: shift `4 × 10^-5` / peculiar velocities | 0.037: 0.012 / 0.025 | +0.002 / −0.012 | 0.040: 0.011 / 0.029 | 0.0 / −0.016 |

- DES-SN5YR: G10 and C11 are left out, disfavoured by the data (`Delta chi2
  = 102` for G10); only `alpha` evolution is favoured (`−7 ± 2`)
  `[src: Sect. VII.1.1]`. Host mismatch neglected: 7 of 1635 hosts differ
  between two catalogues `[src: Sect. VI.4.1]`.
- DES-Dovekie: `sigma_w(dust) = 0.101` `[src: Sect. 9.2.1]` sums six dust rows;
  total systematic `sqrt(0.142^2 − 0.11^2) = 0.090` `[der]`. Calibration: 9 SALT
  surfaces from the cross-calibration covariance, weight `1/sqrt(9)` each `[src: Sect. 7.1]`.

### 0.3 Union3 and Union3.1 (arXiv:2311.12098; arXiv:2601.19424)
<!-- key: union3-and-union3-1-arxiv-2311-12098-arxiv-2601 -->

UNITY samples every nuisance parameter; "impact" = `Cov(cosmological
parameter, parameter) / sigma_parameter` `[src: Eq. 21]`, quadrature sum slightly
above the total `[src: Sect. V.1]`. Columns: flat-LCDM `Omega_m`, SNe alone `[src: Table 3]`; `w_a` with BAO and CMB `[src: Table 4]`.

| Term | on Omega_m | on w_a |
|---|---|---|
| Absolute magnitude `M_B` (weight of the nearby sample) / peculiar-velocity correlations | 0.0114 / 0.0063 | 0.1321 / 0.1271 |
| SALT calibration / selection effects | 0.0093 / 0.0079 | 0.0673 / 0.0567 |
| Instrument zero points / passbands / Landolt–Smith–PS1 tie / white-dwarf SED model | 0.0072 / 0.0054 / 0.0046 / 0.0058 | 0.0467 / 0.0572 / 0.0502 / 0.0259 |
| Intergalactic dust / Milky Way extinction | 0.0095 / 0.0046 | 0.0354 / 0.0274 |
| Host step at z = 0 / at z = ∞ | 0.0047 / 0.0063 | 0.0393 / 0.0587 |
| Colour population / `x1` population | 0.0058 / 0.0027 | 0.0441 / 0.0216 |
| `beta_R` (mean of two host classes) / `beta_B` / `Delta beta_R` / `alpha` | 0.0054 / 0.0041 / 0.0016 / 0.0020 | 0.0383 / 0.0180 / 0.0110 / 0.0192 |
| Unexplained scatter / outlier model | 0.0050 / 0.0055 | 0.0366 / 0.0246 |
| Weak-lensing bias / redshift calibration / electron scattering | 0.0013 / 0.0006 / 0.0004 | 0.0001 / 0.0118 / 0.0004 |

`M_B` and peculiar velocities carry 0.274 + 0.253 of the `w_a` variance
`[src: Table 4]`. Contamination: outlier mixture, fitted fraction `0.031
(+0.010/−0.011)` `[src: Sect. IV.6]`. Union3.1 prints no budget; it assigns
`Omega_m` biases of about +0.4 sigma (Union3) and −0.6 sigma (Pantheon+) to
inconsistent host masses `[src: arXiv:2601.19424 Sect. VIII]`.

### 0.4 Unite (Camilleri et al. 2026, arXiv:2609.05053)
<!-- key: unite-camilleri-et-al-2026-arxiv-2609-05053 -->

Flat wCDM, SNe only, on `Q_H(z = 0.2)`; each term alone, `sigma = sqrt(sigma_tot^2 − sigma_stat^2)`
`[src: Eq. 10, Table 6]`; budgets on `Omega_m` and `w` are figures only `[src: Appendix A]`.

| Term (variant, weight) | sigma_QH | Delta Q_H |
|---|---|---|
| Total systematic (equal to statistical) | 0.015 | −0.019 |
| SALT3 + calibration (10 realisations) / HST CALSPEC | 0.008 / 0.000 | −0.009 / 0.000 |
| BS21 dust parameters / P23 dust population 1 / 2 / 3 | 0.003 / 0.001 / 0.003 / 0.001 | −0.003 / 0.000 / −0.002 / −0.001 |
| SN-age model / `sigma_int` modelling / initial `alpha`, `beta` | 0.001 / 0.002 / 0.001 | −0.001 / +0.001 / 0.000 |
| `alpha` / `beta` / `gamma` evolution | 0.000 / 0.005 / 0.001 | +0.001 / −0.016 / 0.000 |
| Mass-step location `10^10.2` / host-mass uncertainties (10 realisations) | 0.000 / 0.000 | −0.004 / −0.004 |
| Milky Way 5 % scaling / colour law | 0.003 / 0.004 | 0.000 / −0.002 |
| Shallower host catalogue / ±0.2 mag shift of spectroscopic efficiency | 0.003 / 0.002 | +0.012 / +0.001 |
| Peculiar velocities / redshift shift `10^-4` weighted 1/6 | 0.002 / 0.005 | +0.002 / +0.001 |
| Duplicate SNe (off-diagonal statistical terms) | 0.003 | 0.005 `[src: Sect. 5.2]` |

No contamination row: a cut `P_Ia(SCONE) > 0.8` replaces the BEAMS variants
`[src: Sect. 4.9]`. `alpha` and `beta` evolve at ~3 sigma (`alpha_1 = 0.03 ±
0.01`, `beta_1 = 0.3 ± 0.1`); a step at `10^10.2 M_sun` is preferred by `Delta
chi2 = −8.4`; host-mass errors add ~10 % to the systematic on `w` `[src: Sect. 6.2]`.

## 1. Photometric calibration and cross-calibration
<!-- key: photometric-calibration-and-cross-calibration -->

**Mechanism.** Each survey has its own zero points and filter transmissions.
A relative zero-point error between the low-z anchor systems and the high-z
survey, or a colour-dependent (filter-wavelength) error, changes the relative
distance scale with redshift. The error enters twice: through the light-curve
fits and through the training of the light-curve model on the same data.

**Size.**
- Pre-Supercal systems disagreed with Pan-STARRS1 by 10 mmag on average and
  up to 35 mmag; correcting them changed `w` by 2.6 % on average `[src]`
  (Scolnic et al. 2015, arXiv:1508.05361).
- Fragilistic: recalibration plus SALT2 retraining shifts distances by
  `d mu/dz = 0.04 mag` over 0 < z < 1; calibration contributes
  `sigma_w = 0.013`; the contribution to the SH0ES `H0` error is below 0.2
  km/s/Mpc `[src]` (Brout et al. 2022, arXiv:2112.03864).
- Sensitivity: per 25 mmag of inter-survey zero-point error, `Omega_m` and
  `w` in SH0ES + Pantheon+ move by 0.04 and −0.17, while `H0` moves by no
  more than 0.2 km/s/Mpc because calibrator and Hubble-flow SNe share
  surveys `[src: abstract]` (Brownsberger et al. 2023, arXiv:2110.03486).
- Dovekie: small calibration changes are amplified by up to a factor 6 in
  inferred distances through the colour–luminosity relation and SALT
  training; the recalibration gives `d mu/dz = 0.025` and
  `Delta Omega_m ~ 0.01`; the Pantheon+ calibration systematic improves by a
  factor 1.5 with the white-dwarf tie `[src]` (Popovic et al. 2025,
  arXiv:2506.05471). Zero-point errors: 2–5 mmag for PS1, DES, SDSS, SNLS,
  10–12 mmag for CfA3, CfA4, CSP `[src: Table 3]`; mean distance changes per
  survey from −0.035 (SNLS) to +0.030 mag (CfA4) `[src: Table 7]`.
- Realised effect: DES-SN5YR → DES-Dovekie, `Delta Omega_m = -0.022` and
  4.2 → 3.2 sigma for evolving dark energy with DESI DR2 and CMB `[src: abstract]`
  (arXiv:2511.07517).
- New anchors: ATLAS forced photometry starts ~40 mmag from DES Y6 stars and
  needs filter shifts at the ~30 mmag level, reaching 5–10 mmag after
  recalibration `[src]` (Marlin et al. 2025, arXiv:2512.21903); ZTF has a
  flux-dependent PSF effect giving non-linearities of 1 to 7 % in PSF fluxes,
  against a 0.1 % accuracy target `[src: Sect. 6.2]`, and a 90 mmag shift in
  absolute calibration between photometry pipelines `[src]` (Lacroix et al.
  2025, arXiv:2509.04073).

**Mitigation.** Cross-calibrate all systems on common all-sky stars (PS1,
Gaia), fit filter shifts, tie to DA white dwarfs (Axelrod et al. 2023,
doi:10.3847/1538-4357/acd333), retrain the SALT model on the same solution,
and propagate the full calibration covariance through training and fitting
together.

**Validation.** Tertiary-star comparisons between surveys; distance
comparison of SNe observed by several surveys (151 such SNe in Pantheon+,
arXiv:2112.03863); per-survey Hubble-residual offsets; replacing the anchor
by a same-instrument sample (Foundation, DEBASS). [src: abstract]

**Cite.** arXiv:1508.05361, arXiv:2112.03864, arXiv:2506.05471; Stage-IV
requirements: Anumba et al. 2026 (arXiv:2604.19746).

## 2. Light-curve model training
<!-- key: light-curve-model-training -->

**Mechanism.** SALT is trained on the same SNe and calibration that are then
fitted; errors in training spectra, in the rest-frame UV, or in the training
colour distribution propagate into redshift-dependent distance errors,
because a given observer band samples different rest wavelengths with
redshift.

**Size.** SALT2 vs SALT3 on identical training data: `Delta w = +0.001 ±
0.005` (SN + CMB) `[src]` (Taylor et al. 2023, arXiv:2301.10644). SALT2.4 vs
SALT3.K21 low-z/high-z distance difference `2 ± 14 mmag` `[src]` (Kenworthy
et al. 2021, arXiv:2104.07795). Calibration shifts of 5 mmag and 5 Å
applied only in training degrade a Stage-IV FoM by ~13 %, against ~50 %
through light-curve fitting (**forecast**, arXiv:2604.19746) — a reversal of
the earlier expectation that training dominates.

**Mitigation.** Retrain per calibration variant; drop poorly calibrated
legacy data from training (done for SALT3.DOV, arXiv:2511.07517).

**Cite.** arXiv:2104.07795, arXiv:2301.10644.

## 3. Selection bias (Malmquist) and its dependence on population models
<!-- key: selection-bias-malmquist-and-its-dependence-on -->

**Mechanism.** Near the flux limit, and under spectroscopic-selection
limits, the sample is biased to bright, blue, slow-declining events; the
bias depends on the assumed parent populations of stretch and colour and on
the intrinsic-scatter model.

**Size.** Up to 0.05 mag in redshift bins, 0.4 mag for single events `[src]`
(Kessler et al. 2019, arXiv:1811.02379). Residual `w` bias of the method on
simulations: `0.006 ± 0.002` `[src]` (Kessler & Scolnic 2017,
arXiv:1610.04677). Parent populations drift with redshift: the stretch
distribution evolves with the young/old progenitor mix at > 5 sigma `[src]`
(Nicolas et al. 2021, arXiv:2005.09441), which "does affect current
Malmquist bias corrections".

**The comparison trap.** The same supernova has different bias-corrected
distances in two analyses if their selection functions differ. Vincenzi et
al. 2025 (arXiv:2501.06664) attribute 38 % of the ~0.04 mag
Pantheon+/DES-SN5YR offset on common objects to exactly this, and 43 % to
DES improvements in scatter and host modelling `[src]`: −0.042 → −0.024 mag
(modelling) → −0.008 mag (selection) `[src: Sect. 6]`. Object-by-object
comparison of bias-corrected distance moduli across compilations is not a
valid null test unless the selection functions match.

**Mitigation and validation.** BBC with 4D corrections; alternative
populations as systematics; a volume-limited subsample where selection is
negligible (ZTF z < 0.06); hierarchical or SBI treatments (UNITY, Steve,
FlowSN) as an independent method.

**Cite.** arXiv:1610.04677, arXiv:1811.02379, Popovic et al. 2021
(arXiv:2102.01776), arXiv:2501.06664.

## 4. Intrinsic scatter and dust modelling
<!-- key: intrinsic-scatter-and-dust-modelling -->

**Mechanism.** The scatter model sets how colour is split between a
luminosity-correlated intrinsic part and dust, hence the simulated bias for
red and blue events, hence the distances at the survey limits.

**Size.** Wrong chromatic model uncertainties: up to ~0.05 mag
redshift-dependent distance bias and `sigma_w ~ 0.02` for SNLS3 `[src]`
(Kessler et al. 2013, arXiv:1209.2482). Switching from older colour models
to the dust model: `|Delta w|` up to 0.04 `[src]` (Brout & Scolnic 2021,
arXiv:2004.10206). Uncertainty of the fitted dust parameters:
`sigma_w = 0.005` `[src]` (Popovic et al. 2023, arXiv:2112.04456). In
DES-Dovekie the dust variants together are the largest group,
`sigma_w(dust) = 0.101` in the one-at-a-time convention `[src]`
(arXiv:2511.07517). Reverting Unite to the original BS21 parameters accounts
for part of the Unite–Pantheon+ low-z/high-z offset (−0.0077 → +0.0002 mag
once host masses are also reverted) `[src]` (arXiv:2609.05053).

**Mitigation.** Fit the dust and colour populations to the sample itself
(Dust2Dust, Stjörnumál); carry several posterior draws and the alternative
models (BS21, age model) as systematics.

**Validation.** Hubble-residual scatter and mean versus colour; fitted
`beta`; `chi2` of each variant (Unite: one dust realisation is disfavoured
by `Delta chi2 = 49.2`, the age model by 23.6 `[src: Sect. 6]`, arXiv:2609.05053).

**Cite.** arXiv:1209.2482, arXiv:2004.10206, arXiv:2112.04456.

## 5. Host-galaxy and environment dependence
<!-- key: host-galaxy-and-environment-dependence -->

**Mechanism.** Standardised brightness correlates with host stellar mass,
local colour and local star formation. Since host demographics change with
redshift and differ between targeted low-z surveys and untargeted deep
surveys, an uncorrected dependence is a redshift-dependent bias.

**Size.** See the step history in `results.md` Section 3.3: 0.04–0.17 mag
depending on tracer and method. Cosmological impact: Kelly et al. 2010
(arXiv:0912.0929) found `1 + w = 0.22 (+0.152/-0.143)` with a low-mass-host
low-z anchor and `-0.03 (+0.217/-0.108)` with a high-mass-host one `[src]`; Rigault et al. 2020 (arXiv:1806.03849) argue a strong
bias on `w` can develop as environment ages evolve.

**Mass or dust or age?**
- Dust: in the BS21 picture the step is a consequence of host-dependent
  `R_V` and reddening distributions and therefore depends on SN colour; the
  original paper reports a 4.5 sigma dependence of `gamma` on colour `[src]`
  (arXiv:2004.10206).
- Not (only) dust: BayeSN on ZTF DR2 finds the step with dust modelled
  jointly (`0.103 ± 0.018 mag`, 5.6 sigma) and nearly equal mean `R_V`
  across environments (`Delta E(R_V) <= 0.2`) `[src]` (Ginolin et al. 2026,
  arXiv:2605.06799); ZTF sees no dependence of the step on colour `[src]`
  (arXiv:2406.02072); BayeSN on 475 SNe finds an intrinsic step with a
  ~2 sigma `R_V` difference `[src]` (Grayling et al. 2024, arXiv:2401.08755).
- Two populations: the step emerges from two SN populations distributed
  differently across hosts (arXiv:2606.17802; arXiv:2601.19854).

**A second-order effect that turned out first-order: host-mass measurement
consistency.** Masses estimated with different photometry and SED codes at
low and high redshift move SNe across the step. Size: redshift-dependent
distance differences of ~0.01 mag `[src]` (Lee et al. 2026,
arXiv:2609.05321); > 0.03 mag between the Union3 and Pantheon+ low-z mean
distance moduli, reduced to 0.01 mag after consistent remeasurement, moving
the dark-energy significance by 0.4 sigma in each `[src]` (Hoyt et al. 2026,
arXiv:2601.19424).

**Mitigation.** One photometric system and one SED-fitting configuration for
all hosts; carry mass uncertainties as realisations (Unite: 10 random
realisations `[src]`); vary the step location; allow `gamma(z)`.

**Validation.** `gamma` evolution fit (DES: `-0.028 ± 0.034 mag` per unit
redshift `[src]`, Wiseman et al. 2026, arXiv:2601.13785); split-sample
cosmology (single host type); siblings.

**Cite.** arXiv:0912.0929, Sullivan et al. 2010 (arXiv:1003.5119),
arXiv:1806.03849, arXiv:2004.10206, Smith et al. 2020 (arXiv:2001.11294),
arXiv:2601.19424.

## 6. Population evolution with redshift (progenitor age)
<!-- key: population-evolution-with-redshift-progenitor -->

**Mechanism.** If standardised luminosity depends on progenitor age and the
mean age changes with look-back time faster than the host-mass step tracks,
distances acquire a redshift-dependent bias degenerate with dark energy.

**Size: disputed by more than an order of magnitude.**
- Claim: a 4.6 sigma dependence of the standardisation zero points on age
  (Lee et al. 2022, arXiv:2107.06288); a 5.5 sigma host-age–residual
  correlation and, after correction, > 9 sigma tension with LCDM and a
  non-accelerating universe (Son et al. 2025, arXiv:2510.13121) `[src]`.
- Rebuttals: an earlier version of the claim (0.05 mag/Gyr, up to 0.25 mag
  when extrapolated) has `<= 2 sigma` significance and the residual age
  dependence is consistent with zero for 254 Pantheon SNe `[src]` (Rose et
  al. 2020, arXiv:2002.12382); the 2025 analysis omits the host-mass
  correction, the ~5 Gyr age difference is overstated by a factor 3–5 by
  conflating host and progenitor age, and the mass step does not evolve
  `[src]` (arXiv:2601.13785); 6983 TITAN hosts give a mean progenitor age of
  3.5 Gyr, a 1.5 Gyr evolution, and a maximum bias `Delta HR = -0.007
  (+0.012/-0.014) mag` `[src]` (Murakami et al. 2026, arXiv:2604.16597).
- Counter-rebuttal: Chung et al. 2026 (arXiv:2605.21586) argue the
  rebuttal's slope is flattened by its wide redshift range.

**Direct tests.** Spectroscopically normal SNe Ia at z > 2 with JWST fall on
the LCDM relation within ~1 sigma (Pierel et al. 2024, arXiv:2411.11953):
two objects, so a sanity check, not a constraint.

**Mitigation.** Mass-step (or local-environment) correction, `alpha(z)`,
`beta(z)`, `gamma(z)` variants, age-model systematic (Wiseman et al. 2022,
arXiv:2207.05583). In Unite a linear `beta(z)` improves the fit by
`Delta chi2 = -9.5` with `beta_1 = 0.3 ± 0.1` and gives the largest
astrophysical shift, `Delta Q_H = -0.016` `[src]` (arXiv:2609.05053): this is
the nuisance-evolution term to watch.

**Cite.** Both sides: arXiv:2510.13121 and arXiv:2601.13785,
arXiv:2604.16597.

## 7. Photometric classification and contamination
<!-- key: photometric-classification-and-contamination -->

**Mechanism.** Core-collapse and peculiar SNe Ia leak into a photometric
sample with a redshift-dependent rate and a different magnitude
distribution.

**Size.** `w` bias < 0.008, `sigma_w,syst <= 0.004` for DES `[src]`
(Vincenzi et al. 2023, arXiv:2111.10382); classification is less than 10 %
of the DES-SN5YR systematic budget, 9 % `[src: Sect. VII.1.5]` (arXiv:2401.02945); the
alternative-training systematic is 0.010 in DES-Dovekie `[src]`
(arXiv:2511.07517).

**Mitigation and validation.** BEAMS weighting; several classifiers and
training sets; different core-collapse template libraries; a
`P_Ia` cut variant (Unite).

**Cite.** Kunz et al. 2007 (arXiv:astro-ph/0611004), arXiv:1610.04677,
arXiv:1901.06384, arXiv:2111.10382.

## 8. Host association and redshift errors
<!-- key: host-association-and-redshift-errors -->

**Mechanism.** A wrong host gives a wrong redshift (differences up to 0.6)
and wrong host properties; a systematic redshift offset shifts the whole
low-z Hubble diagram.

**Size.** 1.7 % mismatches, `Delta w = 0.0013 ± 0.0026`, up to 0.0032 with
contaminants `[src]` (Qu et al. 2024, arXiv:2307.13696). Catalogue-level
redshift errors: `Delta H0 = -0.11 km/s/Mpc`, `Delta w = -0.001` after the
Pantheon+ redshift review `[src]` (Carr et al. 2022, arXiv:2112.01471).
Redshift systematics of 10^-4 are not negligible for `H0` (Davis et al.
2019, arXiv:1907.12639).

**Cite.** arXiv:2307.13696, arXiv:2112.01471.

## 9. Peculiar velocities
<!-- key: peculiar-velocities -->

**Mechanism.** At z < 0.1 host motions of a few hundred km/s are a
non-negligible, spatially correlated part of the redshift. They add scatter,
and coherent flows bias the anchor.

**Size.** Neglecting the CMB-dipole correction: `Delta w ~ 0.04`; neglecting
coherent velocities: ~2 % in `w` `[src]` (Davis et al. 2011,
arXiv:1012.2912). After optimal flow and group corrections: 0.02–0.03 in
`w`, 0.06–0.11 km/s/Mpc in `H0` `[src]` (Peterson et al. 2022,
arXiv:2110.03487). In DES-Dovekie the redshift group grew slightly,
"driven by an increased uncertainty from the peculiar velocities" `[src]`
(arXiv:2511.07517). At z < 0.008 the mean Pantheon+ residual is positive by
~5 % at ~2 sigma, a volumetric (Eddington-type) redshift bias, ~2 mmag on the
low-z mean `[src: Sect. IV.2.2]` (arXiv:2202.04077); Unite models it in the bias correction `[src: Sect. C.2]` (arXiv:2609.05053).

**Mitigation.** 2M++-based corrections with group assignment; a velocity
floor (240 km/s in Pantheon+); a low-redshift cut (z > 0.025 in DES; tested
at 0.0233 in Unite); alternative flow models (integrated line-of-sight 2M++,
2MRS) as the systematic.

**Validation.** Cosmology stable under the low-z cut; residual sky maps.

**Cite.** arXiv:1012.2912, arXiv:2112.01471, arXiv:2110.03487.

## 10. Milky Way extinction
<!-- key: milky-way-extinction -->

**Mechanism.** Low-z SNe are all-sky; deep fields sit at low extinction. An
error in the dust-map scale or colour law is differential in redshift.

**Size and treatment.** Unite carries a 5 % scaling of the Schlafly &
Finkbeiner 2011 map (arXiv:1012.4804) and a colour-law variant (`R_V = 3.0`,
Cardelli et al. 1989, doi:10.1086/167900, against `R_V = 3.1`, Fitzpatrick
1999, arXiv:astro-ph/9809387, preferred by the map paper) `[src]` (arXiv:2609.05053). Dhawan et al.
2024 (arXiv:2409.18668) show that a change of Milky Way dust law can shift
`w0`–`w_a` by an amount comparable to the DESI 2024 deviation.

**Implementation bug to remember.** SNANA's Fitzpatrick 1999 law was a
polynomial expansion valid near `R_V = 3.1`; used across the `R_V` range of
dust-model simulations it biased bias corrections at the ~0.01 mag level
until fixed in DES-Dovekie `[src]` (arXiv:2511.07517). Analyses built on
SNANA simulations with dust-based scatter models before that fix inherit it.

## 11. Gravitational lensing
<!-- key: gravitational-lensing -->

**Mechanism.** Magnification adds skewed scatter growing with redshift and,
with selection, a bias.

**Size.** `sigma_lens = 0.055 z` is the standard noise term (arXiv:2202.04077).
Detected at 6.0 sigma in DES; delensing shifts flat-wCDM parameters by
~0.3 sigma `[src]` (Shah et al. 2024, arXiv:2406.05047). Unite applies a
delensing term by default and finds the shift small and along the degeneracy
`[src]` (arXiv:2609.05053).

## 12. Reference cosmology in bias corrections
<!-- key: reference-cosmology-in-bias-corrections -->

Size: sub-dominant to statistics even for `Delta Omega_m ~ 0.2` `[src]`
(Camilleri et al. 2024, arXiv:2406.05048); one seventh of the statistical
error with an `Omega_m` prior according to arXiv:1610.04677 as summarised in
arXiv:2401.02945. Matters for exotic models fitted to a public Hubble
diagram.

## 13. Heterogeneity of the low-redshift anchor
<!-- key: heterogeneity-of-the-low-redshift-anchor -->

This is where Sections 1, 3, 5 and 9 compound. Evidence that it is the
controlling systematic for dark energy:

- Foundation residuals fainter than older low-z by `0.046 ± 0.027 mag`
  `[src]` (Jones et al. 2019, arXiv:1811.09286).
- A ~0.04 mag low-z/high-z offset between DES-SN5YR and Pantheon+ on common
  SNe (Efstathiou 2024, arXiv:2408.07175), explained in part by
  arXiv:2501.06664.
- The DESI-era preference weakens to < 2 sigma once the DES-SN5YR low-z
  sample is corrected for an intercept offset (Huang et al. 2025,
  arXiv:2502.04212), and weakens "significantly" when such an offset is
  marginalised (Notari et al. 2024, arXiv:2411.11685); a low-z/high-z magnitude offset is favoured by
  the Bayesian evidence over flexible dark energy, and Dovekie "partially
  alleviates" but does not remove this (Ormondroyd et al. 2025,
  arXiv:2509.13220).
- Cutting z < 0.1 from Unite moves `Omega_m` from 0.310 to 0.290 ± 0.015
  `[src]` (arXiv:2609.05053).

Mitigation is observational: same-instrument anchors (DEBASS for DES;
Foundation for PS1), untargeted discovery (ZTF, ATLAS), consistent host
masses.

## 14. What a referee checks in a results section
<!-- key: what-a-referee-checks-in-a-results-section -->

1. Which sample exactly: name, version (DES-SN5YR or DES-Dovekie; Union3 or
   Union3.1; Pantheon+ with which host masses), number of SNe, redshift
   range, low-z cut.
2. Whether calibration, model training, light-curve fits and bias-correction
   simulations all use the same calibration solution.
3. The scatter and dust model in the bias corrections, and the dimensionality
   of the correction.
4. The systematics budget per source, the convention used to build it, and
   whether the covariance is unbinned.
5. The fitted `alpha`, `beta`, `gamma`, `sigma_int` and Hubble RMS, and
   whether `alpha(z)`, `beta(z)`, `gamma(z)` variants were run.
6. Stability of the cosmology under: low-z cut, removal of the anchor
   surveys one at a time, classifier choice, `P_Ia` cut, host-mass step
   location, peculiar-velocity model.
7. For combined probes: a tension metric between SNe and the other data
   inside the model fitted, before quoting combined errors; which CMB and
   BAO data; which statistic the significance comes from.
8. Whether SN samples that share supernovae are treated as independent (they
   are not).
9. For any claim of redshift evolution or of its absence: whether the
   host-mass correction was applied and whether host age is being used as
   progenitor age.
10. Blinding: what was hidden, and what changed after unblinding.

## Not verified
<!-- key: not-verified -->

- Cardelli et al. 1989: title, authors and year confirmed on Crossref; not read.
- Chromatic (SED-dependent) photometric corrections: not developed here.
