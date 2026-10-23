# Type Ia supernova cosmology — results

Scope: current headline measurements from SN Ia Hubble diagrams, alone and in
combination, then the history of the key numbers so that superseded values can
be recognised.
Snapshot: 2026-10-13

Flags: `[src]` read in the cited paper this session (abstract unless a table
or section is named); `[sec]` from a named secondary source; `[der]` derived
here. The model is stated in every row. Uncertainties are 68 % and include
systematics unless stated.

## 1. Current SN-only constraints
<!-- key: current-sn-only-constraints -->

### 1.1 Matter density, flat LCDM, SNe alone
<!-- key: matter-density-flat-lcdm-sne-alone -->

| Sample | Omega_m | N (SNe) | Status | Citation | Flag |
|---|---|---|---|---|---|
| Unite | 0.310 (+0.012/-0.011) | 2884 | Current | Camilleri et al. 2026, arXiv:2609.05053 | `[src: abstract]` |
| Unite, z > 0.1 only | 0.290 ± 0.015 | 2884 − 687 | Robustness variant | arXiv:2609.05053 Sec. 9.1 | `[src]` |
| DES-Dovekie | 0.330 ± 0.015 | 1623 DES + 197 low-z (Sect. 8.2) | Current | Popovic et al. 2025, arXiv:2511.07517 | `[src]` |
| Union3.1 + UNITY1.7 (outlier-prior fix, fitted step location); the same UNITY1.7 on Union3 gives 0.352 (+0.026/-0.025) | 0.344 (+0.026/-0.025) | ~2000 | Current | Hoyt et al. 2026, arXiv:2601.19424 | `[src: Table 3]` |
| Union3.1 + UNITY1.8 (two populations) | 0.334 (+0.025/-0.024) | ~2000 | Current, alternative model | Rubin et al. 2026, arXiv:2601.19854 | `[src: abstract]` |
| Pantheon+ | 0.334 ± 0.018 | 1550 | Published 2022; host masses and calibration since revised | Brout et al. 2022, arXiv:2202.04077 | `[src: abstract]` |
| DES-SN5YR | 0.352 ± 0.017 | 1829 (1635 DES + 194 low-z; total as printed in Sect. 2.1) | **Superseded** by DES-Dovekie (shift −0.022) | DES Collaboration 2024, arXiv:2401.02929 | `[src]` |
| Union3 + UNITY1.5 | 0.356 (+0.028/-0.026) | 2087 | **Superseded** by Union3.1 (shift −0.4 sigma) | Rubin et al. 2023, arXiv:2311.12098, results table | `[src]` |

Reading the table: the three current analyses span `Omega_m = 0.310–0.344`
from SNe alone, with errors of 0.012–0.026 and heavily overlapping data. The
Unite authors state that Pantheon+, DES-SN5YR/DES-Dovekie, Union3 and Unite
"are all consistent with each other to well within 1 sigma" and that about
half of each error bar is systematic, so differences between pipelines on the
same data are expected `[src]` (arXiv:2609.05053). Unite's lower value is
driven by SNe at 0.023 <= z <= 0.85, not by the lowest-redshift bins
`[src]`.

### 1.2 Dark-energy equation of state, SNe alone
<!-- key: dark-energy-equation-of-state-sne-alone -->

| Sample | Model | Constraint | Citation | Flag |
|---|---|---|---|---|
| Pantheon+ | flat wCDM | `w = -0.90 ± 0.14` | arXiv:2202.04077 | `[src]` |
| Pantheon+ | flat w0waCDM | `w_a = -0.1 (+0.9/-2.0)` | arXiv:2202.04077 | `[src]` |
| DES-SN5YR | flat wCDM | `(Omega_m, w) = (0.264 (+0.074/-0.096), -0.80 (+0.14/-0.16))` | arXiv:2401.02929 | `[src]` |
| DES-SN5YR | flat w0waCDM | `(Omega_m, w0, w_a) = (0.495 (+0.033/-0.043), -0.36 (+0.36/-0.30), -8.8 (+3.7/-4.5))` | arXiv:2401.02929 | `[src]` |
| DES-Dovekie | flat wCDM | `(Omega_m, w) = (0.263 (+0.064/-0.078), -0.838 (+0.130/-0.142))`; `q0 = -0.423 (+0.063/-0.073)` | arXiv:2511.07517 Sec. 10 | `[src]` |
| DES-Dovekie | flat w0waCDM | `(w0, w_a) = (-0.50 (+0.35/-0.27), -7.5 (+3.6/-4.5))`, widened priors; at the pivot `z_p = 0.52`, `w_p = -1.01 ± 0.13` | arXiv:2511.07517 Sec. 10 | `[src]` |
| Unite | flat wCDM | `(Omega_m, w) = (0.197 (+0.056/-0.054), -0.764 (+0.078/-0.096))`, about 2 sigma from `w = -1`; `Q_H(z=0.2) = -0.418 ± 0.021` | arXiv:2609.05053 | `[src: Sect. 7.0.3]` |
| Unite | flat w0waCDM | `(Omega_m, w0, w_a) = (0.297 (+0.086/-0.141), -0.779 (+0.099/-0.098), -0.86 (+1.01/-1.78))`: consistent with `w_a = 0`, `w0 > -1` preferred | arXiv:2609.05053 | `[src: Sect. 7.0.4]` |

SNe alone do not detect evolving dark energy in any current sample. The
extreme SN-only `w_a` values are a volume effect of an unconstrained
direction (large negative `w_a` goes with `Omega_m > 0.4`), as the
DES-Dovekie paper explains `[src]`. Quoting `w_a = -8.8` or `-7.5` as a
"measurement" is a misreading.

DES-SN5YR also reports that SNe alone require acceleration (`q0 < 0` in
LCDM) at more than 5 sigma `[src]` (arXiv:2401.02929).

## 2. Combined-probe dark-energy results in which the SN sample matters
<!-- key: combined-probe-dark-energy-results-in-which-the -->

All rows: flat `w0waCDM` with `w(a) = w0 + w_a (1 - a)`. "Significance" is
the preference over flat LCDM. The statistic differs between rows (last
column); compare only like with like.

| SN sample | Other data | w0 | w_a | Significance | Statistic | Citation | Flag |
|---|---|---|---|---|---|---|---|
| none | DESI DR2 BAO + CMB | −0.42 ± 0.21 | −1.75 ± 0.58 | 3.1 sigma | Delta chi2_MAP | DESI Collaboration 2025, arXiv:2503.14738 | `[src]` |
| Pantheon+ | DESI DR2 BAO + CMB | −0.838 ± 0.055 | −0.62 (+0.22/−0.19) | 2.8 sigma | Delta chi2_MAP = −10.7 | arXiv:2503.14738 | `[src]` |
| Union3 | DESI DR2 BAO + CMB | −0.667 ± 0.088 | −1.09 (+0.31/−0.27) | 3.8 sigma | Delta chi2_MAP = −17.4 | arXiv:2503.14738 | `[src]` |
| DES-SN5YR | DESI DR2 BAO + CMB | −0.752 ± 0.057 | −0.86 (+0.23/−0.20) | 4.2 sigma | Delta chi2_MAP = −21.0 | arXiv:2503.14738 | `[src]` |
| DES-Dovekie | DESI DR2 BAO + CMB (Planck, ACT, SPT) | −0.803 ± 0.054 | −0.72 ± 0.21 | 3.2 sigma; Bayesian odds ~5:1 ("weak") | Delta chi2 = −13.5; Delta log Z = −1.7 | arXiv:2511.07517 | `[src]` |
| Union3.1 | BAO + CMB "exactly as done by DESI DR2" | −0.719 ± 0.084 | −0.95 (+0.29/−0.26) | 3.4 sigma | as DESI | arXiv:2601.19424 | `[src: abstract]` |
| Union3.1, UNITY1.8 | SNe + BAO + CMB | −0.760 (+0.084/−0.082) | −0.79 (+0.28/−0.30) | ~3 sigma | 2D w0–w_a | arXiv:2601.19854 | `[src: abstract]` |
| DES-Dovekie (Hoyt et al. re-run) | DESI DR2 + Planck | — | — | 3.4 sigma (was 4.2) | as DESI | arXiv:2601.19424 | `[src: abstract]` |
| Pantheon+ with corrected host masses | DESI DR2 + Planck | — | — | 3.2 sigma (was 2.8) | as DESI | arXiv:2601.19424 | `[src: abstract]` |
| DES-Dovekie | DES Y6 3×2pt + DES BAO + DESI DR2 BAO + primary CMB | −0.82 ± 0.05 | −0.63 (+0.21/−0.18) | 3.0 sigma | as stated by DES | DES Collaboration 2026, arXiv:2605.27221 | `[src: abstract]` |
| Unite | DES + DESI DR2 BAO, CMB (Planck, ACT, SPT, lensing) | −0.861 (+0.044/−0.042) | −0.60 (+0.17/−0.19) | 3.3 sigma (MAP), 3.1 sigma (ML); Bayesian evidence "weak" | FoM = 315 (`1/sqrt(det Cov)`) | arXiv:2609.05053 | `[src: abstract]` |

Companion numbers:

- With `Omega_m`: Unite + BAO + CMB gives `Omega_m = 0.305 ± 0.004` `[src]`
  (arXiv:2609.05053).
- **DES-only multi-probe** (SN + BAO + 3×2pt, no CMB, no DESI): `w0 = -0.84
  ± 0.10`, `w_a = -0.44 (+0.60/-0.55)`, 2.2 sigma. Adding DESI DR2 BAO:
  `w0 = -0.84 (+0.06/-0.07)`, `w_a = -0.53 (+0.33/-0.28)`, 2.3 sigma, quoted
  as the most stringent low-redshift-only test. Leaving SNe out of the full
  combination still gives 2.6 sigma, "a cross-check independent of supernova
  photometric calibration" `[src: abstract]` (arXiv:2605.27221).
- **Host-mass consistency.** Replacing the Pantheon+ data-release host masses
  by consistently remeasured ones raises the Pantheon+-subsample preference
  for evolving dark energy from 3.4 to 4.0 sigma (MAP, with BAO and CMB),
  while DES-Dovekie is essentially unchanged `[src: abstract]` (Lee et al. 2026,
  arXiv:2609.05321).
- **Flat wCDM with CMB is not a clean test.** DES-Dovekie + BAO + CMB gives
  `w = -0.995 (+0.019/-0.020)` but the datasets are in 2.5 sigma tension
  inside that model `[src]` (arXiv:2511.07517); Unite greys out its
  equivalent number for the same reason `[src]` (arXiv:2609.05053).

The interpretation of these results as physics belongs to
`cosmo-dark-energy-modified-gravity`; what belongs here is that **the three
SN samples now agree**: 3.2–3.4 sigma for corrected Pantheon+, DES-Dovekie
and Union3.1 with DESI DR2 and Planck, where the 2025 DESI paper had
2.8–4.2 sigma.

## 3. History of the key numbers
<!-- key: history-of-the-key-numbers -->

### 3.1 Evidence for evolving dark energy (SN + BAO + CMB, flat w0waCDM)
<!-- key: evidence-for-evolving-dark-energy-sn-bao-cmb -->

| Date | Combination | Pantheon+ | Union3(.1) | DES | Citation | Flag |
|---|---|---|---|---|---|---|
| 2024-04 | DESI DR1 BAO + CMB + SN | 2.5 sigma | 3.5 sigma | 3.9 sigma | DESI Collaboration 2024, arXiv:2404.03002 | `[src: abstract]` |
| 2025-03 | DESI DR2 BAO + CMB + SN | 2.8 sigma | 3.8 sigma | 4.2 sigma | arXiv:2503.14738 | `[src: Sect. VII]` |
| 2025-11 | DES-Dovekie recalibration | — | — | 3.2 sigma | arXiv:2511.07517 | `[src]` |
| 2026-01 | Union3.1 host masses; re-runs with DESI DR2 + Planck | 3.2 sigma | 3.4 sigma | 3.4 sigma | arXiv:2601.19424 | `[src: abstract]` |
| 2026-09 | Unite (Pantheon+ ∪ DES) | 3.3 sigma (MAP) for the union | | | arXiv:2609.05053 | `[src]` |

DESI + CMB without SNe: 2.6 sigma (DR1) and 3.1 sigma (DR2) `[src]`.
The DES 3.2 sigma (DES analysis, CMB = Planck + ACT + SPT) and 3.4 sigma
(Hoyt et al. re-run, CMB as in DESI DR2) differ because the external data
differ, not the supernovae.

### 3.2 Omega_m and w from successive compilations
<!-- key: omegam-and-w-from-successive-compilations -->

| Year | Sample | N | Result (model) | Citation | Flag |
|---|---|---|---|---|---|
| 1998 | High-Z Team | 16 + 34 | `Omega_Lambda > 0` at 7 and 9 sigma for two light-curve fitters (flat prior); 3.0 and 4.0 sigma with no prior other than `Omega_m > 0` | Riess et al. 1998, arXiv:astro-ph/9805201 | `[src: abstract]` |
| 1999 | SCP | 42 + Calán/Tololo | `Omega_m = 0.28 (+0.09/-0.08) stat (+0.05/-0.04) sys` (flat) | Perlmutter et al. 1999, arXiv:astro-ph/9812133 | `[src]` |
| 1997 | SCP, first seven at z = 0.35–0.46 | 7 | `Omega_m = 0.94 (+0.34/-0.28)` (flat): no acceleration; reversed by the 42-SN sample | Perlmutter et al. 1997, arXiv:astro-ph/9608192 | `[src: abstract]` |
| 2006 | SNLS first year | 71 | `Omega_m = 0.263 ± 0.042 stat ± 0.032 sys` (flat LCDM); `w = -1.023 ± 0.090 stat ± 0.054 sys` with SDSS BAO (flat wCDM) | Astier et al. 2006, arXiv:astro-ph/0510447 | `[src]` |
| 2009 | SDSS-II first year + ESSENCE, SNLS, HST, nearby; with BAO and CMB | 288 (103 new at 0.04 < z < 0.42) | `w = -0.76 ± 0.07 stat ± 0.11 sys` with MLCS2k2 but `-0.96 ± 0.06 ± 0.12` with SALT-II (flat wCDM): the fitter was the systematic, traced to the rest-frame UV model and the colour treatment | Kessler et al. 2009, arXiv:0908.4274 | `[src: abstract]` |
| 2010 | SNLS3, SNLS SNe alone | 231 | `Omega_m = 0.211 ± 0.034 stat ± 0.069 sys` (flat LCDM); calibration dominates, then light-curve fitters (0.026) | Guy et al. 2010, arXiv:1010.4743 | `[src: abstract]` |
| 2008 | Union | 307 of 414 | `Omega_Lambda = 0.713 (+0.027/-0.029) stat (+0.036/-0.039) sys` (flat LCDM); `w = -0.969 (+0.059/-0.063) stat (+0.063/-0.066) sys` with BAO and CMB; one blind procedure for all subsamples | Kowalski et al. 2008, arXiv:0804.4142 | `[src: abstract]` |
| 2011 | SNLS3 joint | 472 | `w = -0.91 (+0.16/-0.20) stat (+0.07/-0.14) sys` (flat wCDM, SNe only) | Conley et al. 2011, arXiv:1104.1443 | `[src: abstract]` |
| 2012 | Union lineage: world sample plus HST Cluster Supernova Survey | 14 of 20 new HST SNe (found at 0.623 < z < 1.415) pass the cuts | `Omega_Lambda = 0.724 (+0.015/-0.016)` (LCDM); `w = -0.985 (+0.071/-0.077)` (flat wCDM); applies the then recently identified host-mass correction | Suzuki et al. 2012, arXiv:1105.3470 | `[src: abstract]` |
| 2014 | JLA | 740 | `Omega_m = 0.295 ± 0.034` (flat LCDM, SNe); `w = -1.018 ± 0.057` with CMB; 1.8 sigma from SNLS3, "due primarily to improvements in the SNLS photometric calibration" | Betoule et al. 2014, arXiv:1401.4064 | `[src]` |
| 2018 | Pantheon | 1048 | With Planck 2015: `Omega_m = 0.307 ± 0.012`, `w = -1.026 ± 0.041` (wCDM); with BAO and local `H0` added: `w0 = -1.007 ± 0.089`, `w_a = -0.222 ± 0.407` | Scolnic et al. 2018, arXiv:1710.00845 | `[src: abstract]` |
| 2019 | DES-SN3YR | 329 | `Omega_m = 0.331 ± 0.038` (flat LCDM); `w = -0.978 ± 0.059` with CMB | Abbott et al. (DES) 2019, arXiv:1811.02374 | `[src: abstract]` |
| 2019 | Foundation + PS1 | 1338 | `w = -0.938 ± 0.053` with CMB (flat wCDM) | Jones et al. 2019, arXiv:1811.09286 | `[src: abstract]` |
| 2022 | Pantheon+ | 1550 | `Omega_m = 0.334 ± 0.018`; with CMB + BAO `w = -0.978 (+0.024/-0.031)` (wCDM) and `w_a = -0.65 (+0.28/-0.32)` (w0waCDM) | arXiv:2202.04077 | `[src: abstract]` |
| 2023 | Union3 | 2087 | `Omega_m = 0.356 (+0.028/-0.026)`; 1.7–2.6 sigma tension with LCDM depending on combination | arXiv:2311.12098 | `[src: abstract]` |
| 2024 | DES-SN5YR | 1829 (1635 + 194) | `Omega_m = 0.352 ± 0.017`; with Planck, SDSS BAO and DES 3×2pt `(Omega_m, w) = (0.321 ± 0.007, -0.941 ± 0.026)` | arXiv:2401.02929 | `[src: abstract]` |
| 2025 | DES-Dovekie | 1684 effective | `Omega_m = 0.330 ± 0.015` | arXiv:2511.07517 | `[src: Sect. 10.5]` |
| 2026 | Union3.1 | ~2000 | `Omega_m = 0.344 (+0.026/-0.025)` | arXiv:2601.19424 | `[src]` |
| 2026 | Unite | 2884 | `Omega_m = 0.310 (+0.012/-0.011)` | arXiv:2609.05053 | `[src: abstract]` |

Lessons that the history teaches and that a referee will apply to any new
shift:

- The two largest shifts in the record, SNLS3 → JLA (1.8 sigma) and
  DES-SN5YR → DES-Dovekie (`Delta Omega_m = -0.022`, 4.2 → 3.2 sigma), both
  came from photometric calibration.
- Pantheon+ already showed `w_a = -0.65 (+0.28/-0.32)` with CMB and SDSS-era
  BAO in 2022: the direction of the later DESI-era preference was present,
  at about 2 sigma, before DESI `[der: -0.65/0.28 ≈ 2.3, one-parameter
  reading of the quoted error]`.
- Hierarchical reanalyses can move parameters on identical data: BAHAMAS on
  JLA with Planck gave `Omega_m = 0.399 ± 0.027`, 2.8 sigma above the
  standard analysis (flat wCDM) `[src: abstract]` (Shariff et al. 2016,
  arXiv:1510.05954).

### 3.3 The host-mass step
<!-- key: the-host-mass-step -->

| Year | Sample | Step (mag) | Note | Citation | Flag |
|---|---|---|---|---|---|
| 2006 | SNLS, 124 SNe | no step measured: the SN Ia rate depends on host mass and star-formation rate; a rate set by mass alone is excluded at 99 % | The two-component picture behind later environment tracers | Sullivan et al. 2006, arXiv:astro-ph/0605455 | `[src: Sect. II.1]` |
| 2010 | 70 low-z SNe | ~10 % brighter in massive hosts, ~2.5 sigma | Discovery | Kelly et al. 2010, arXiv:0912.0929 | `[src]` |
| 2010 | SNLS | 0.08, ~4.0 sigma | Two-`M` correction proposed | Sullivan et al. 2010, arXiv:1003.5119 | `[src: abstract]` |
| 2010 | SDSS-II | ~0.1 brighter in passive than in star-forming hosts, 2–3 sigma; expressed through stellar mass at > 4 sigma | Cited with the two papers above as the origin of the step (arXiv:2511.07517 Sect. 3.1) | Lampeitl et al. 2010, arXiv:1005.4687 | `[src]` |
| 2013 | SNfactory, 89 SNe | 0.094 ± 0.031 fainter with local Hα emission than without | "First direct study of the local environment" for a large sample | Rigault et al. 2013, arXiv:1309.1182 | `[src: abstract]` |
| 2018 | 882 SNe at 0.01 < z < 1 | local `U−V` colour step as significant as the largest mass step | Local colour as third standardisation variable | Roman et al. 2018, arXiv:1706.07697 | `[src: abstract]` |
| 2018 | 273 SNe at z < 0.1 | 0.06 global; local step larger in untargeted surveys by 0.071 ± 0.036 | Local vs global | Jones et al. 2018, arXiv:1805.05911 | `[src: abstract]` |
| 2020 | SNfactory | 0.163 ± 0.029 in local sSFR (5.7 sigma); 0.119 ± 0.032 in mass on the same SNe | Strongest environmental step to that date | Rigault et al. 2020, arXiv:1806.03849 | `[src: abstract]` |
| 2020 | DES-SN3YR | 0.040 ± 0.019 (5D) or 0.066 ± 0.020 (1D bias correction) | Method dependence | Smith et al. 2020, arXiv:2001.11294 | `[src: abstract]` |
| 2021 | ~1450 SNe | Step explained by host-dependent dust | Dust model | Brout & Scolnic 2021, arXiv:2004.10206 | `[src: abstract]` |
| 2021 | Foundation DR1, BayeSN (157 SNe) | no step quoted; `R_V = 2.84 ± 0.31` (low mass) and `2.58 ± 0.23` (high mass), consistent | Against a dust-law difference; RMS 0.13 mag vs 0.16 with SALT2 | Thorp et al. 2021, arXiv:2102.05678 | `[src: abstract]` |
| 2021 | ~1600 SNe, dust-based BBC | 0.017 ± 0.008 residual | | Popovic et al. 2021, arXiv:2102.01776 | `[src: abstract]` |
| 2024 | DES-SN5YR | 0.038 ± 0.007 residual after dust model | > 5 sigma | Vincenzi et al. 2024, arXiv:2401.02945 | `[src: Sect. V.2]` |
| 2024 | 475 SNe, BayeSN | intrinsic step −0.049 ± 0.016 (3.1 sigma) alongside a ~2 sigma `R_V` difference | Sign convention of that paper | Grayling et al. 2024, arXiv:2401.08755 | `[src: abstract]` |
| 2024 | ZTF DR2 volume-limited | > 0.12 for every tracer; ~0.17 ± 0.01 with non-linear stretch | No colour dependence of the step | Ginolin et al. 2024, arXiv:2405.20965; arXiv:2406.02072 | `[src]` |
| 2026 | Union3.1 + UNITY1.8 | consistent with zero for unreddened SNe | Two populations absorb it | arXiv:2601.19854 | `[src]` |
| 2026 | ZTF DR2, BayeSN (932 SNe) | 0.103 ± 0.010 (mass), 0.086 ± 0.010 (local colour); 0.103 ± 0.018 with dust modelled jointly | Step is not a SALT artefact and not dust | Ginolin et al. 2026, arXiv:2605.06799 | `[src: abstract]` |
| 2026 | Unite | 0.040 ± 0.006 residual | BBC with P23 dust | arXiv:2609.05053 | `[src: Sect. 5]` |

The size of "the mass step" ranges from zero to 0.17 mag depending on sample
selection, bias-correction dimensionality, scatter model and whether the
relation in stretch is linear. A bare number without those four
specifications is not interpretable.

## 4. Hubble constant from the SN Hubble flow (pointer)
<!-- key: hubble-constant-from-the-sn-hubble-flow-pointer -->

Detail belongs to `cosmo-distance-ladder-h0`. The SN-side numbers:

| Hubble-flow sample | H0 (km/s/Mpc) | Note | Citation | Flag |
|---|---|---|---|---|
| Pantheon+ with SH0ES Cepheid hosts | 73.04 ± 1.04 | Baseline, 42 calibrator SNe | Riess et al. 2022, arXiv:2112.04510 | `[src]` |
| Pantheon+ (flat wCDM, with SH0ES) | 73.5 ± 1.1 | SN systematics are less than one third of the `H0` error | arXiv:2202.04077 | `[src: abstract]` |
| Corrected Pantheon+ (revised host-mass correction: 114 of 1701 rows changed, 52 of 277 Hubble-flow rows, no calibrators) | 73.264 ± 0.806 | Against a "H0 Distance Network" baseline of 73.499 ± 0.809 | Roy Choudhury 2026, arXiv:2607.24443 | `[src: abstract]` |
| DES-Dovekie low-z (220 SNe at 0.025 <= z <= 0.151, tied through 196 overlaps) | 73.267 ± 0.828 | First ladder use of DES-Dovekie | arXiv:2607.24443 | `[src: abstract]` |
| Two-population remodelling of Pantheon+ / SH0ES | 70.59 ± 1.15, or 71.45 ± 1.03 with equal priors | Contested; depends on assigning calibrators to a population | Wojtak & Hjorth 2025, arXiv:2506.22150 | `[src: abstract]` |
| DES-Dovekie + CMB, flat LCDM (not a ladder value) | 67.29 ± 0.34 | CMB-driven; shown only to mark the contrast | arXiv:2511.07517 results table | `[src]` |

The 2025–2026 recalibration and host-mass corrections that moved the
dark-energy significance by up to one sigma moved `H0` by about 0.2
km/s/Mpc: the relative low-z/high-z distance scale and the calibrator/Hubble-
flow tie are different systematics.

## 5. Other measurements from SN samples
<!-- key: other-measurements-from-sn-samples -->

| Quantity | Value | Dataset | Citation | Flag |
|---|---|---|---|---|
| Weak-lensing magnification of SNe | Detected at 6.0 sigma by correlating Hubble residuals with foreground galaxies | DES-SN5YR × DES Y3 Gold | Shah et al. 2024, arXiv:2406.05047 | `[src]` |
| Effect of delensing on cosmology (flat wCDM) | `Delta Omega_m = +0.036`, `Delta w = -0.056`, ~0.3 sigma | DES-SN5YR | arXiv:2406.05047 | `[src]` |
| Scatter reduction from delensing | ~5 % at z > 0.5 | Unite (delensing on by default) | arXiv:2609.05053 | `[src]` |
| Redshift evolution of the mass step | `-0.028 ± 0.034 mag per unit z`; changes `w` by < 0.01 | DES SN | Wiseman et al. 2026, arXiv:2601.13785 | `[src]` |
| Progenitor-age redshift bias | `Delta HR = -0.007 (+0.012/-0.014) mag` maximum | 6983 TITAN hosts | Murakami et al. 2026, arXiv:2604.16597 | `[src: abstract]` |
| SN Ia distance at z = 2.15 | ~0.1 sigma from LCDM | SN 2023aeax, JWST | Pierel et al. 2024, arXiv:2411.11953 | `[src: abstract]` |
| Shift of `w` when one analysis step is left out (flat wCDM, SNe only, statistical errors only; not part of the budget) | no bias correction and no BEAMS −1.024; a cut `P_Ia > 0.5` in place of BEAMS −0.033; no Milky Way extinction correction +0.185; deep and shallow fields bias-corrected together −0.136; `gamma` forced to 0 −0.113. Subsamples: only hosts above `10^10 M_sun` −0.071 (scatter over 25 simulations 0.081), only below +0.138 (0.213) | DES-SN5YR | arXiv:2401.02945 | `[src: Table 11]` |
| Coverage of the BBC contours | Bayesian contours agree with approximate Neyman intervals at the > 95 % level over 150 simulated samples (Armstrong et al., as reported) | DES-SN5YR | arXiv:2401.02945 | `[sec: Sect. VII.2]` |
| Non-standard models | 11 of 15 models "moderately preferred" over flat LCDM with external probes; none strongly | DES-SN5YR | Camilleri et al. 2024, arXiv:2406.05048 | `[src]` |

## Not verified
<!-- key: not-verified -->

- No Pantheon+-only or Union3.1-only `w0waCDM` numbers with DESI DR2 after
  the host-mass correction beyond the significances quoted by Hoyt et al.
- The effective DESI-era significance for Unite with exactly the DESI DR2
  external data set (Unite uses DES + DESI BAO and Planck + ACT + SPT).
