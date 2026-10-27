# Anomaly significance — cosmo-tensions-anomalies dossier

Scope: how the p-value of a CMB anomaly is computed (null ensemble, maps,
mask, tail), how an a posteriori parameter inside one statistic and a
choice among many statistics are corrected for, how several p-values are
combined, what the definition choices (cut or full sky, angle range,
ℓ_max, quadrupole) cost, and which independent data can test an anomaly
and with what power.
Snapshot: 2026-10-17.
From: Abdalla et al. 2022 (arXiv:2203.06142), Sects. VIII.3.7–VIII.3.8;
Planck 2018 isotropy and statistics (arXiv:1906.02552), conclusions;
Schwarz et al. 2016 review (arXiv:1510.07929).

Already in L2, not repeated here: the definitions of S_1/2, R^TT, σ²_16 and
S_QO and the list of anomalies (`physics-and-methods.md#large-angle-cmb-anomalies`);
the published p-values, the joint ≤ 3 × 10⁻⁸ (arXiv:2310.12859) and its 2σ–3σ reassessment (arXiv:2602.10178) [src: abstract of each],
the PR4 status and the Planck caveats (`results.md#large-angle-cmb-anomalies`);
mundane explanations with verdicts (`systematics.md#large-angle-cmb-anomalies`);
the dispute (`open-questions.md#large-angle-cmb-anomalies-evidence-or-flukes`);
the maps (`surveys-and-data.md#large-angle-cmb-maps`). Look-elsewhere
theory in general and Δχ²-to-σ conversion belong to
`cosmo-statistics-inference`; the null of the number-count dipole to
`deep/cosmic-dipoles.md` (Step 4); the parity-odd 4PCF null to
`cosmo-beyond-two-point` (`systematics.md#mock-realism-for-the-four-point-covariance`).

Notation. A p-value (probability to exceed, PTE) is the fraction of null
realisations with a statistic "at least as extreme as the observed one"
[src: arXiv:1906.02552, Sect. 4]; "lower-tail" and "upper-tail" say which
side counts as extreme. C(θ) is the two-point angular correlation function
of the map, C_ℓ its angular power, ℓ the multipole. n_T is the number of
tests considered, n_A the number of most anomalous ones combined.

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Build the null ensemble
<!-- key: step-1-build-the-null-ensemble -->

Planck FFP10, the reference ensemble of the collaboration [src:
arXiv:1906.02552, Sect. 4]:

- 1000 Gaussian CMB skies from one fiducial ΛCDM model (arXiv:1906.02552, Table 2: ω_b =
  0.022166, ω_c = 0.12029, h = 0.67019, n_s = 0.96369, A_s = 2.1196 × 10⁻⁹,
  τ = 0.06018), with lensing, Rayleigh scattering and Doppler boosting, and
  frequency-specific beams.
- 300 end-to-end noise-plus-systematics realisations per frequency, from
  simulated time-ordered data through the map-maker [src: arXiv:1906.02552,
  Sect. 4].
- Signal and noise propagated through each of the four component-
  separation pipelines "using the same weights as derived from the Planck
  full-mission data", then permuted into 999 simulations per method
  (realisation 970 was corrupted and dropped, footnote 7 of arXiv:1906.02552).
- Known mismatch: the FFP10 τ is above the 2018 value; lowering τ from
  0.060 to 0.052 "reduces the polarization variance by approximately 20%"
  at N_side = 16 and 32 [src: arXiv:1906.02552, Sect. 4]. Simulations underestimate the 100–217 GHz noise
  and omit point-source residuals, so half-mission and odd–even difference
  maps are compared with the simulations to define the reliable angular
  scales for each test.

Consequence: "the Planck analysis relies on just 1000 Monte Carlo
simulations … and thus p-values below 0.2% cannot be resolved" [src:
arXiv:1510.07929, Table 1 caption].

Large noise-free ensemble (Jones et al. 2023, arXiv:2310.12859, Methods):
10⁸ CMB-only realisations of the Planck best fit to ℓ_max = 200, generated
in ecliptic coordinates at N_side = 64 (160′ beam) or 16 (640′), with no
noise and no foregrounds. Their reasons: large-scale temperature is
"almost completely cosmic-variance-limited"; the same study on FFP10 gave
"nearly identical results"; WMAP and Planck, with different noise, find
similar p-values; and noise-free maps are what makes 10⁸ realisations
possible. Residual foregrounds are not simulated because four
component-separation methods are unlikely to "leave behind the identical
anomalies". [src: abstract]

### Step 2. Prepare the data like the simulations
<!-- key: step-2-prepare-the-data-like-the-simulations -->

Four component-separated maps (Commander, NILC, SEVEM, SMICA), the common
mask, downgraded in harmonic space with beam and pixel windows [src:
arXiv:1906.02552, Sect. 3]. Unmasked fractions of the temperature common
mask: 71.3% at N_side = 64, 68.8% at N_side = 32 [src: Table 1]. Jones et
al. rotate maps and mask to ecliptic coordinates (σ²_16 is defined on the
northern ecliptic sky) and reset downgraded mask pixels with a 0.9 cut-off
[src: arXiv:2310.12859, Methods]. A p-value is quoted per map; the spread
over maps is the component-separation systematic.

### Step 3. Count in the right tail
<!-- key: step-3-count-in-the-right-tail -->

Planck's S^XY tables give the probability of a value "at least as large as
the observed", so "high probabilities would correspond to anomalously low"
values [src: arXiv:1906.02552, Tables 12–15]. Schwarz et al. flip this so
that small means unexpected [src: arXiv:1510.07929, Table 1 caption];
Planck notes that "the sense of the p-values differs between the papers"
[src: Sect. 6.1]. Jones et al. count realisations "at least as anomalous
in the same direction as the data in order to capture the behavior of the
tail" [src: arXiv:2310.12859, Results].

### Step 4. Correct for a free parameter inside one statistic
<!-- key: step-4-correct-for-a-free-parameter-inside-one -->

The global p-value [src: arXiv:1906.02552, Sect. 6.1]: compute
S^XY(θ, 180°) for every lower bound θ on the data and on every simulation;
for each map find the most extreme probability over θ; the global p-value
is the fraction of simulations whose most extreme probability beats the
data's. Temperature: fixed θ = 60° gives > 99.9% for all four maps (Table
12), the global statistic 98.8–99.0% (Table 13), that is a lower-tail p of
about 1%.

The same scan for the parity ratio R^TT(ℓ_max) [src: arXiv:1906.02552, Sect. 6.3, Eqs. 44–45]:
the minimum lower-tail probability with the Lkl-Commander map and its mask
is 0.2% at ℓ_max = 24; 16 of the 999 simulations reach 0.2% or less for at
least one ℓ_max in 3–64, so the corrected probability is about 1.6%.

Dipole modulation: letting ℓ_max vary, "small p-values (of order 0.1–1%)
occur of order 10% of the time" [src: arXiv:1906.02552, Sect. 7.2].

### Step 5. Combine several statistics on one sky
<!-- key: step-5-combine-several-statistics-on-one-sky -->

Joint counting (Jones et al., arXiv:2310.12859, Results, Tables 1–3): the
joint p-value is the fraction of the 10⁸ realisations in which all four
statistics are at least as anomalous as in the data, "not from multiplying
each statistic's individual p-value". The correlation factor
p(S_A, S_B)/[p(S_A) p(S_B)] measures dependence: ≃ 30 for (S_1/2, σ²_16),
close to 1 otherwise (SMICA p(S_1/2, R^TT) = 2.8 × 10⁻⁵, factor 0.6); the
triple (S_1/2, σ²_16, S_QO) adds a factor 0.6–2.1. Joint p_4 ≤ 3 × 10⁻⁸
(> 5.4σ) for Commander, NILC and SMICA, about 5.1σ for SEVEM; the factor
of p_4 over the product of the four single p-values is "consistently
less than 100" (SMICA: p_4 = 1 × 10⁻⁸, factor 64).

Independent "atoms" (Schwarz et al., arXiv:1510.07929, Sect. 2.7): reduce
the anomalies to features independent within ΛCDM, proposed as three —
lack of large-angle correlation, alignment of the lowest multipoles,
hemispherical power asymmetry — on the basis of constrained simulations
showing that a lack of correlation does not raise the chance of
alignments. Two or three of them as flukes would have p "at most ∼10⁻⁵".
The authors add that a test correlating the lack of correlation with the
dipolar modulation "has never been done".

### Step 6. Correct for the choice among statistics
<!-- key: step-6-correct-for-the-choice-among-statistics -->

Guth & Namjoo 2026 (arXiv:2602.10178, Sects. II–III). Under the null each
p-value is uniform. For n_T independent tests, the density of x, the
product of the four smallest p-values, is [src: Eq. 12]

P_4(x) = n_T! / (12 n_d!) · J_nd(x),  J_nd(x) = ∫_{x^{1/4}}^{1} dp (1 − p)^{n_d} p⁻¹ ln²(p⁴/x)  [src: arXiv:2602.10178, Eq. 8],

with n_d = n_T − 4; Eq. 11 of arXiv:2602.10178 gives J in closed form. Generalised to the n_A
smallest p-values [src: Eq. 15]. Dependence is folded in through an
effective number of combined tests: with the correlation factor C ≡
x_JCSA/(p_1 p_2 p_3 p_4) ≃ 51 [src: Eq. 13] and the geometric mean p̄ of
the four, p̄^{n_eff} = x_JCSA gives n_eff ≃ 3.26 [src: Eq. 14]. The
reported 3 × 10⁻⁸ then falls to 2σ for n_T ≃ 50 and to 3σ for n_T ≃ 16.
Other read-outs: for n_T = 100 there is a 33.8% chance of a product below
3 × 10⁻⁸; with n_T = 133 it is the median outcome; P_4 is so skewed that
the median, not the mean, is the typical value [src: Sect. II, Figs. 2–3].
The result is checked against 10⁵ Monte Carlo draws per n_T [src: Fig. 3].

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Cut sky or full sky for S_1/2
<!-- key: cut-sky-or-full-sky-for-s1-2 -->

Against the cut-sky number (Efstathiou, Ma & Hanson 2010,
arXiv:0911.5399, Sects. 4.2, 5): with WMAP 5-year ILC maps and ΛCDM
realisations, the full-sky p of S_1/2 < 7373 μK⁴ is 8%, while with the
KQ75 mask the p of S_1/2 < 647 μK⁴ is 0.065%. The low multipoles that set
C(θ) at large angles "can be reconstructed accurately, independent of any
assumptions concerning statistical isotropy, from the data that lie
outside the sky cuts", and the reconstructed C(θ) agrees with the full-sky
one. The generalised statistic S^p_μ [src: Eq. 32] shows that p-values can
move "by an order of magnitude or more by selecting the parameters in
response to the data". Subtracting a local ISW map from 2MASS (z < 0.3)
gives S_1/2 = 10360 (all sky), 6463 (KQ85) and 5257 μK⁴ (KQ75), "consistent
with the concordance ΛCDM model at the few percent level".

For the cut-sky number (Schwarz et al. 2016, arXiv:1510.07929, Sect. 2.1):
"it is the cut-sky two-point correlation function which is observed to be
strikingly anomalous, and which begs an explanation"; most large-angle
correlation in reconstructed maps comes from pairs with at least one point
in the most Galaxy-contaminated region, and larger masks give smaller
p-values (≤ 0.1% for Planck 2013 and WMAP 9-year). Jones et al. use the
masked statistic, "following the choices made by previous anomaly
studies", from pseudo-C_ℓ to ℓ_max = 40 [src: arXiv:2310.12859, Eq. 7].

### Fixed or scanned angle range
<!-- key: fixed-or-scanned-angle-range -->

Fixed 60° gives p < 0.1%; scanned, p ≈ 1% (Step 4). Schwarz et al.: the
global statistic "addresses a different question, namely how likely is it
that there is a lack of correlation for an arbitrary μ"; it is "different",
not better [src: arXiv:1510.07929, Sect. 2.1]. Two χ² statistics of
C(θ > 60°) with the ΛCDM covariance give about 3% and 2% in Planck 2015
[src: same].

### With or without the quadrupole
<!-- key: with-or-without-the-quadrupole -->

Removing the best-fit quadrupole moves S_1/2 from > 99.9% to 96.0–96.2%
(fixed range) and from about 99% to 85.5–87.2% (global), and C^TT(180°)
from about 89% to about 60% [src: arXiv:1906.02552, Tables 12, 13, 15].
Planck: "the anomalous value of the S^TT statistic is connected to the
observed quadrupole". Jones et al. and Schwarz et al. stress instead that
the ℓ = 2–5 terms cancel those of higher ℓ, which a low C_2 alone cannot
do [src: arXiv:2310.12859, Eq. 8 text; arXiv:1510.07929, Sect. 2.1].

### Mask for parity
<!-- key: mask-for-parity -->

R^TT lower-tail probability about 1% at ℓ_max = 20–30 with the 2018 common
mask; the 2015 mask on 2018 data gives 0.3% at ℓ_max = 27; the low-ℓ
likelihood mask gives 0.2% at ℓ_max = 24, and higher-latitude sky
"diminishes the odd point parity preference" [src: arXiv:1906.02552, Sect.
6.3].

### Simulation set
<!-- key: simulation-set -->

From arXiv:1906.02552 (Sect. 4), arXiv:2310.12859 (Methods section) and arXiv:2206.05920 (Sect. II.2); the column of resolvable p-values computed here as 1/N was removed on 2026-10-23:

| Ensemble | Size | Content | Used by |
|---|---|---|---|
| FFP10 | 999 per method | signal + end-to-end noise and systematics, component-separated | Planck 2018 VII |
| Noise-free ΛCDM | 10⁸ | CMB only, Planck best fit | Jones et al. 2023 |
| Signal + noise mix | 10⁴ CMB × 300 noise | combinations "not completely independent" | Shi et al. 2022 |

## Independent tests and their power
<!-- key: independent-tests-and-their-power -->

### Are polarisation estimators independent of temperature?
<!-- key: are-polarisation-estimators-independent-of -->

In 10⁴ ΛCDM realisations the Pearson correlation between temperature and
E-mode anomaly estimators is below 0.1, except point parity (ρ = 0.17,
cosmic-variance-limited case); within temperature, S_1/2 and the parity
ratio correlate at about 0.3, through the quadrupole [src: arXiv:2206.05920,
abstract, Sect. IV.1.2]. Hence an E-mode anomaly that matched a temperature
one "would present an independent challenge to the statistical-fluke
hypothesis".

### Conditional predictions given the temperature sky
<!-- key: conditional-predictions-given-the-temperature -->

Constrained realisations [src: arXiv:2206.05920, App. C, Eq. C3]: fix
a^T_ℓm to the measured SMICA values and draw

a^E_ℓm = (C^TE_ℓ / C^TT_ℓ) a^T,data_ℓm + √(C^EE_ℓ − (C^TE_ℓ)²/C^TT_ℓ) ζ,

ζ a complex standard normal. Conditioning shifts the median of log₁₀ S^EE_1/2
(ideal case) from 0.19 to 0.30, because the E variance acquires the term
(C^TE)²/C^TT (C^TT,data/C^TT − 1) [src: arXiv:2206.05920, Eq. C4]; otherwise the
distributions are "largely consistent" with unconstrained ones.

The Copi et al. 2013 falsification test as applied by Planck [src:
arXiv:1906.02552, Sect. 6.1, Table 14]: under the fluke hypothesis,
S^TQ(48°, 120°) < 1.403 μK⁴ in 99% of constrained realisations, so a larger
measured value would rule the fluke out. Planck measures 0.07–0.26 μK⁴
(probabilities 82.9–97.0%), "so that we cannot rule out the statistical
fluke hypothesis".

### What polarisation data show
<!-- key: what-polarisation-data-show -->

- Planck 2018 component-separated Q, U: no excursion outside the 95% band
  for any polarisation S^XY(θ, 180°), with "notable variations between
  component-separation methods" [src: arXiv:1906.02552, Sect. 6.1, Fig.
  23]. Parity in TE and EE uses the difference D^X = C^X_+ − C^X_− [src:
  Eq. 46] because ratios of noisy spectra can blow up.
- Chiocchetta et al. 2021 (arXiv:2012.00024, Sect. 5): SRoll2 HFI 100 × 143
  and LFI + WMAP, fiducial τ = 0.0591, ℓ_max = 10 (noise-dominated above).
  S_1/2 on Q and U is "largely dominated by the quadrupole" and not
  anomalous (apart from a 2σ LFI + WMAP U case); on local E modes the HFI
  lower-tail probability is 0.4% (unconstrained), and T + E jointly < 0.2%
  in 500 simulations. The authors call it "a mild low power anomaly"
  driven by all ℓ ≤ 10, with "non negligible uncertainties at ℓ = 2". No
  scan correction over ℓ_max is reported in the conclusions read.

### Power of future data (forecasts)
<!-- key: power-of-future-data-forecasts -->

- LiteBIRD-like noise against Planck SMICA: E-mode estimator errors smaller
  by about 3 (hemispherical asymmetry, parity) and about 26 (lack of
  correlation); quadrupole–octopole alignment "pinned down" by ≳ 100 though
  its cosmic variance stays [src: arXiv:2206.05920, abstract] — **forecast**.
  CLASS (15 μK·arcmin white noise, partial sky) is intermediate [src: Sect.
  II.2] — **forecast**.
- AliCPT + Simons Observatory: an injected E-mode dipole modulation A_d =
  0.07 detected at 99% confidence; AliCPT alone, through its sky
  coverage, "might introduce systematic biases or enlarged uncertainties"
  in the alignment and parity estimators [src: arXiv:2604.20699, abstract] —
  **forecast**.
- Temperature–lensing cross-correlation: constrained and unconstrained
  skies are distinguishable "in around 40 per cent of model realizations"
  [src: arXiv:1310.7603, abstract] — **forecast**. Schwarz et al. summarise
  the temperature–polarisation equivalent as a ∼ 50% chance of excluding
  the fluke at > 3σ [src: arXiv:1510.07929, Sect. 5.1].
- Large-scale structure: a lack of large-angle power implies, in ΛCDM, a
  suppression of P(k) at k ≲ 0.001 h Mpc⁻¹, which a very large survey
  could measure "in principle" [src: arXiv:1510.07929, Sect. 5.2].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| FFP10 simulations per method | 999 (1000 CMB × 300 noise, permuted) | Planck 2018 | arXiv:1906.02552 | Sect. 4 |
| Polarisation variance change, τ 0.060 → 0.052 | ≈ −20% at N_side 16, 32 | Planck 2018 | arXiv:1906.02552 | Sect. 4 |
| Common-mask sky fraction, temperature | 71.3% (N_side 64), 68.8% (32) | Planck 2018 | arXiv:1906.02552 | Table 1 |
| S^TT_1/2 values | 1142.4–1209.2 μK⁴ over four maps | Planck 2018, N_side 64 | arXiv:1906.02552 | Table 11 |
| Global p, S^TT(θ, 180°) | 98.8–99.0% (≈ 1% lower tail); 85.5–87.2% without quadrupole | Planck 2018 | arXiv:1906.02552 | Table 13 |
| Parity scan correction | 16/999 ≈ 1.6% for ℓ_max 3–64 | Planck 2018 | arXiv:1906.02552 | Sect. 6.3 |
| Jones ensemble | 10⁸ noise-free, ℓ ≤ 200 | Jones et al. | arXiv:2310.12859 | Methods section |
| Correlation factor (S_1/2, σ²_16) | ≃ 30 | Jones et al. | arXiv:2310.12859 | Table 1 |
| Correlation factor of p_4 | < 100 (SMICA 64); 51 used in reanalysis | Jones et al.; Guth & Namjoo | arXiv:2310.12859; arXiv:2602.10178 | Table 3; Eq. 13 |
| Effective combined tests | n_eff ≃ 3.26 | Guth & Namjoo | arXiv:2602.10178 | Eq. 14 |
| Tests for the median to reach 3 × 10⁻⁸ | 133 | Guth & Namjoo | arXiv:2602.10178 | Sect. II |
| S_1/2 p, full sky vs KQ75 | 8% vs 0.065% | WMAP 5-year | arXiv:0911.5399 | Sect. 4.2 |
| Copi fluke bound | S^TQ(48°, 120°) < 1.403 μK⁴ in 99% | constrained WMAP-7 | arXiv:1906.02552 | Sect. 6.1 |
| Planck S^TQ(48°, 120°) | 0.07–0.26 μK⁴ | Planck 2018 | arXiv:1906.02552 | Table 14 |
| T–E estimator correlation | < 0.1; parity 0.17 | ΛCDM simulations | arXiv:2206.05920 | abstract |
| E-mode local S_1/2 lower tail | 0.4%; T + E < 0.2% | SRoll2 HFI 100 × 143 | arXiv:2012.00024 | Sect. 5 |

## What goes wrong
<!-- key: what-goes-wrong -->

- Tail sense flipped. A "99.9%" in Planck tables (arXiv:1906.02552,
  Table 12) is an anomaly; in Schwarz's table 0.1% is (arXiv:1510.07929,
  Table 1 caption). Test: check the table caption for "at least as
  large" or "at most as large".
- A p-value beyond the resolution of the ensemble quoted as a number. The
  Planck analysis has 999 simulations per method (arXiv:1906.02552) [src:
  Sect. 4], and Schwarz et al. note that with it "p-values below 0.2%
  cannot be resolved" (arXiv:1510.07929) [src: Table 1 caption].
- Multiplying p-values. Jones et al. count joint exceedances; the product
  differs from the joint value by the correlation factor (0.6 to 64 in
  Tables 1–3 of arXiv:2310.12859). Test: report the factor.
- Scanning without a global p. ℓ_max, the angle bound and the mask all
  move p by factors of a few to ten (Steps 4, Choices). Test: repeat the
  scan on every simulation.
- Mask and estimator as hidden choices. Full-sky reconstruction against
  cut-sky estimator: 8% against 0.065% on the same WMAP map (arXiv:0911.5399)
  [src: Sect. 4.2]. Report both.
- Counting the four maps as four measurements: one sky, four cleanings.
- Fiducial mismatch in the simulations: the FFP10 τ biases polarisation
  variance by about 20% (arXiv:1906.02552) [src: Sect. 4]; Chiocchetta et
  al. fix τ = 0.0591 for their ensemble (arXiv:2012.00024) [src: Sect. 5]. State the fiducial.
- Quadrupole double counting: low variance, S_1/2 and C(θ) at the largest angles all lean on
  C_2 (Choices); a combination must count it once.
- Claiming a polarisation confirmation from ℓ ≤ 10 E modes (arXiv:2012.00024
  [src: Sect. 5]) without a correction for the ℓ_max choice and with ℓ = 2
  systematics open.

## Reading list
<!-- key: reading-list -->

- Foundation and practice: Planck 2018 VII, arXiv:1906.02552 — Sect. 4
  (FFP10), Sect. 6.1 (global p-value, Copi test), Sect. 6.3 (ℓ_max scan).
- Review, one side: Schwarz et al. 2016, arXiv:1510.07929 — Sect. 2.1 (cut
  sky), Sect. 2.7 (atoms), Sect. 5 (tests).
- Method, combination: Jones et al. 2023, arXiv:2310.12859, Methods section — 10⁸
  realisations and joint counting.
- Method, look-elsewhere: Guth & Namjoo 2026, arXiv:2602.10178 — Eqs. 8–15.
- Critique: Efstathiou, Ma & Hanson 2010, arXiv:0911.5399 — full-sky
  reconstruction, S^p_μ, local ISW.
- Method, independent tests: Shi et al. 2022, arXiv:2206.05920 — T–E
  correlations, constrained realisations, forecasts.
- Application: Chiocchetta et al. 2021, arXiv:2012.00024 — S_1/2 in E modes.
- Forecast: Yoho et al. 2013, arXiv:1310.7603; Dou & Zhao 2026,
  arXiv:2604.20699.

## Not verified
<!-- key: not-verified -->

- The Copi et al. 2013 constrained-realisation paper itself and the
  temperature–polarisation forecasts summarised in Sect. 5.1 of
  arXiv:1510.07929 (its refs. 167–170): not identified or read.
- The 2015 Planck χ² of C(θ > 60°) tables (cited through Schwarz et al., arXiv:1510.07929):
  not read at source.
- Chiocchetta et al. (arXiv:2012.00024): masks, the ℓ_max dependence of the 0.4% (read for ℓ_max = 10 only [src: Sect. 5]) and the
  constrained-case numbers; only the conclusions (Sect. 5) were read.
- Yoho et al. 2013 and Dou & Zhao 2026: abstracts only.
- The Abdalla et al. 2022 Sects. VIII.3.7–VIII.3.8 named in `from`: not
  reread this session.
