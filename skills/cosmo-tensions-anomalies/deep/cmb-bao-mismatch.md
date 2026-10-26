# CMB–BAO mismatch — cosmo-tensions-anomalies dossier

Scope: how the ΛCDM distance between the CMB and DESI BAO is computed (which
posteriors, which subspace, which conversion to σ), how much each input
choice moves it, whether one redshift bin carries it, in which direction
τ, Σm_ν, A_L, Ω_K and w0wa move the CMB side, and how to test whether an
extension fits new physics or only absorbs this one inconsistency.
Snapshot: 2026-10-17.
From: CosmoVerse white paper (arXiv:2504.01669), Sects. 2.3.4–2.3.5;
Abdalla et al. 2022 (arXiv:2203.06142), Sect. VI.2; DESI DR2 cosmology
working group (arXiv:2503.14738), Sects. VI–VII.

Already in L2, not repeated here: distances by CMB set and parameter
values (`results.md#cmb-desi-discrepancy-within-lcdm`); A_L, τ and "one
mismatch, five names"
(`physics-and-methods.md#cmb-internal-al-tau-cmb-bao-discrepancy`); w0wa
and neutrino-mass significances (`results.md#dynamical-dark-energy-preference`,
`results.md#negative-effective-neutrino-mass`); verdicts on mundane
explanations (`systematics.md#al-tau-and-the-cmb-bao-discrepancy`); the two
readings (`open-questions.md#one-omegam-mismatch-or-five-anomalies`).
Tension metrics in general (parameter shifts, suspiciousness, the
multi-set Q_DM, Ong et al.'s dimensionality) are in
`cosmo-statistics-inference` (`deep/tension-metrics.md`); the τ
measurement itself in `cosmo-cmb` (`deep/low-ell-polarisation-tau.md`);
BAO fitting and its systematics in `cosmo-galaxy-clustering`
(`deep/bao-reconstruction-fitting.md`); w(z) reconstructions in
`cosmo-dark-energy-modified-gravity` (`deep/wz-reconstruction.md`).

Notation. Ω_m is the present matter fraction; h = H0/(100 km s⁻¹ Mpc⁻¹);
r_d the comoving sound horizon at the baryon drag epoch; D_M/r_d and
D_H/r_d = c/(H r_d) the transverse and radial BAO distances; θ* =
r*/D_M(z*) the CMB acoustic angle; ω_b = Ω_b h², ω_bc = (Ω_b + Ω_c)h²,
ω_m = Ω_m h² (ω_bc plus massive neutrinos); τ the reionisation optical
depth; A_s the primordial amplitude; M_ν or Σm_ν the summed neutrino mass;
Δχ²_MAP the difference of χ² at the maximum a posteriori points of two
models. <!-- num: not a value -->

## How it is done
<!-- key: how-it-is-done -->

### Step 1. Fix the two posteriors
<!-- key: step-1-fix-the-two-posteriors -->

BAO side: DESI DR2 BAO alone, fitted in flat ΛCDM. In this model BAO
constrain only Ω_m and the combination H0 r_d [src: arXiv:2503.14738,
Sect. III.3.1]: Ω_m = 0.2975 ± 0.0086, h r_d = 101.54 ± 0.73 Mpc, with
correlation coefficient r = −0.92 [src: Eq. 17]. SPT's rerun of the same
data gives 100 Ω_m = 29.76 ± 0.87 and h r_d = 101.52 ± 0.73 Mpc [src:
arXiv:2506.20707, Sect. VII.3, table of Fig. 25]; the small difference is
a rerun difference, not a different data set.

CMB side, DESI's baseline ("CMB" in all DESI DR2 papers) [src:
arXiv:2503.14738, Sect. IV.2]:

- Planck simall and Commander for ℓ < 30, CamSpec (NPIPE PR4) for ℓ ≥ 30,
  plus the Planck + ACT DR6 lensing likelihood, version 1.2 [src:
  arXiv:2503.14738, Sect. IV.2].
- Reason for CamSpec over HiLLiPoP/LoLLiPoP: "the speed of evaluation of
  the likelihood code"; both PR4 likelihoods reduce the A_L anomaly and use
  more sky than Plik.
- Its ΛCDM result: Ω_m = 0.3169 ± 0.0065, H0 = 67.14 ± 0.47 [src:
  arXiv:2503.14738, Table 5].

CMB side, SPT-3G D1 paper [src: arXiv:2506.20707, Sect. VII.1, Table 3]:
"Planck" there means PR3 Plik high-ℓ T&E + low-ℓ TT + PR4 lensing, and every
CMB set carries a Gaussian τ prior N(0.051, 0.006) instead of a low-ℓ EE
likelihood, "based on" the NPIPE τ, because SPT does not measure large-scale
E modes. So "Planck" in the SPT table and "CMB" in DESI are different
likelihoods, with different τ treatments.

Compressed CMB, used by DESI as a more model-independent alternative
[src: arXiv:2503.14738, Sect. IV.2, App. A]: a correlated Gaussian on
(θ*, ω_b, ω_bc) obtained after marginalising over the ISW effect and
lensing, from CamSpec chains, with mean (0.01041, 0.02223, 0.14208) [src:
Eq. 35] and covariance 10⁻⁹ × [[0.006621, 0.12444, −1.1929], [0.12444,
21.344, −94.001], [−1.1929, −94.001, 1488.4]] [src: Eq. 36]. The
alternative shift-parameter compression (R, l_A, ω_b) "gives equivalent
results". A θ*-only prior 100θ* = 1.04110 ± 0.00053 has its width inflated
by about 75% over the Planck error "to account for the (small) variation
seen over different assumed late-time models" [src: Eq. 16].

### Step 2. Choose the subspace
<!-- key: step-2-choose-the-subspace -->

The comparison lives in the (Ω_m, h r_d) plane because those are the only
two parameters BAO constrain in ΛCDM [src: arXiv:2503.14738, Sect. VI;
arXiv:2506.20707, Sect. VII.3]. With a BBN prior on ω_b, BAO also give
H0, and DESI quotes the same 2.3σ in the (Ω_m, H0) plane [src:
arXiv:2503.14738, Sect. VI]. The CMB constrains Ω_m h³ tightly (a proxy for
θ*); DESI + BBN + θ* instead follow constant Ω_m h², so the contours cross
rather than slide along each other [src: Sect. VI].

### Step 3. Compute the distance
<!-- key: step-3-compute-the-distance -->

DESI [src: arXiv:2503.14738, Eq. 18]:

χ² = (p_A − p_B)ᵀ (Cov_A + Cov_B)⁻¹ (p_A − p_B),

with p_A, p_B the (Ω_m, r_d h) posterior values from DESI and the CMB and
Cov_A, Cov_B "the corresponding 2×2 posterior parameter covariances". The
χ² is converted "into a probability-to-exceed (PTE) value", and the PTE into
an equivalent Gaussian σ. The formula assumes Gaussian, independent
posteriors; it ignores the correlation between DESI and CMB that would come
from shared data (there is none here) and any non-Gaussianity.

SPT applies the same two-parameter difference "accounting for the
correlations between the two parameters" and translates it "to equivalent
statistical significances for a one-dimensional Gaussian distribution"
[src: arXiv:2506.20707, Sect. VII.3].

Sailer et al. obtain χ² = 6.55 and 2.07 for τ priors 0.06 and 0.09 and
quote 2.1σ and 0.9σ [src: arXiv:2504.16932, Sect. III].

Converting those χ² values through the probability to exceed for two
degrees of freedom reproduces the quoted σ, which is therefore not the
square root of χ² [der].

DESI and SPT
use posterior means; Sailer et al. use "the best fit (Ω_m, H0 r_d) values"
[src: arXiv:2504.16932, Sect. III].

### Step 4. Decide whether to combine
<!-- key: step-4-decide-whether-to-combine -->

- DESI: "given that this tension is not close to 3σ, it is still valid to
  combine the two datasets within the ΛCDM model" [src: arXiv:2503.14738,
  Sect. VI]; joint Ω_m = 0.3027 ± 0.0036, H0 = 68.17 ± 0.28, r = −0.975
  [src: Eq. 21].
- SPT: data sets are consistent "if they agree to better than 3σ according
  to this metric" [src: arXiv:2506.20707, Sect. VII.3]. It reports SPT +
  DESI and CMB-SPA + DESI but not SPT + ACT + DESI (3.7σ), because combining
  across the threshold would shift H0, σ8 and n_s, the last with
  "consequences for the allowed model space of inflationary theories"
  [src: Sect. VII.3, footnote 46].
- DESI does not combine DESI and supernovae in ΛCDM: Ω_m differs at 1.7σ
  (Pantheon+), 2.1σ (Union3) and 2.9σ (DESY5), all SNe preferring higher
  Ω_m [src: arXiv:2503.14738, Sect. VI, Fig. 10]; no threshold is stated.

### Step 5. DESI's internal checks before any external comparison
<!-- key: step-5-desi-s-internal-checks-before-any -->

[src: arXiv:2503.14738, Sect. III.3.1]

- DR1 against DR2, assuming perfect correlation as the conservative
  choice: joint error σ = √(σ²_DR2 + σ²_DR1 − 2Cσ_DR1) with C = √(N_DR1/N_DR2)
  for galaxies and quasars and C = 0.61 for Lyα (footnote 12 of
  arXiv:2503.14738). Largest
  shifts 1.56σ in α_iso (LRG3 + ELG1) and 1.93σ in α_AP (LRG2);
  Kolmogorov–Smirnov statistic 0.25 for 12 points, p = 0.40.
- Each redshift bin fitted in ΛCDM separately: largest difference 1.8σ
  (LRG1 against LRG3 + ELG1); joint fit χ²/dof = 10.2/(13 − 2)
  (arXiv:2503.14738) [src: Sect. III.3.1].

### Step 6. Localise the mismatch
<!-- key: step-6-localise-the-mismatch -->

Three published ways, all on DR2.

(a) Rotated distances per bin (Efstathiou 2025, arXiv:2505.02658, Sect. 2).
Rotate (D_H/r_d, D_M/r_d) by an angle γ(z) so the Planck ΛCDM degeneracy
line is horizontal [src: Eqs. 4a–4b]:

D^par = (D_H/r_d) sin γ + (D_M/r_d) cos γ,
D^perp = (D_H/r_d) cos γ − (D_M/r_d) sin γ.

Planck predicts D^perp "to all intents and purposes" as a delta function,
so "there is no need to consider nuisance parameters, priors and other
complexities"; D^perp is marginalised over D^par in the Gaussian
approximation [src: Eq. 5]. D^par is read conditionally on D^perp fixed at
the Planck value [src: Eq. 6] and mapped linearly to ω_m, ω_m = 0.14205 +
β(D^par − D^par_Planck) [src: arXiv:2505.02658, Eq. 7]. Results in Numbers below.

(b) SVD modes of the distance data (Zaldarriaga 2026, arXiv:2606.30527,
Sect. II.3). Whiten the DESI ratios (and, separately, the supernova
distances with M_B marginalised), project CMB-chain predictions on the
singular vectors, and define for mode α [src: Eq. 3]

tension_α = (a_α − ⟨c_α⟩) / √(1 + σ²_cα),

a_α the data projection, ⟨c_α⟩ and σ_cα the mean and spread of the chain
projections, "1" the unit measurement variance after whitening. Gaussianity
of c_α checked by Kolmogorov–Smirnov tests [src: Sect. II.3.5]. The CMB
reference is ACT DR6 TT/TE/EE + Planck 2018 low-ℓ, without lensing, 2000
samples drawn from 755,302 [src: arXiv:2606.30527, Sect. II.1.3]; 5000 samples shift the BAO
tension by < 0.1σ (footnote 5).

(c) One parameter at a time with an "update difference in means": Jhaveri
et al. compare Ω_m from CMB alone (0.3163 ± 0.0067) and CMB + BAO (0.3024 ±
0.0036) at M_ν = 0.06 eV and find 2.5σ [src: arXiv:2504.21813, Sect.
III.1]. This compares a posterior with an update of itself, not two
independent data sets.

## Choices and what they cost
<!-- key: choices-and-what-they-cost -->

### Which CMB data
<!-- key: which-cmb-data -->

From arXiv:2506.20707, Sect. VII.3:

| CMB set (SPT's definitions) | 100 Ω_m | h r_d [Mpc] | Distance to DESI | Place read |
|---|---|---|---|---|
| Planck (Plik T&E + PR4 lensing + τ prior) | 31.45 ± 0.67 | 99.18 ± 0.84 | 2.0σ | arXiv:2506.20707, Sect. VII.3 |
| SPT-3G D1 | 32.47 ± 0.91 | 97.9 ± 1.1 | 2.5σ | same |
| CMB-SPA | 31.75 ± 0.55 | 98.77 ± 0.69 | 2.8σ | same |
| SPT + Planck | 31.89 ± 0.54 | 98.63 ± 0.67 | 3.0σ | same |
| ACT DR6 (ACT lensing only) | 33.0 ± 1.0 | 97.2 ± 1.2 | 3.1σ | same |
| SPT + ACT | 32.77 ± 0.72 | 97.51 ± 0.87 | 3.7σ | same |

Why they differ, as the authors state it:

- The ground-based experiments prefer higher Ω_m; Planck's large angular
  scales favour lower Ω_m, so adding them to SPT + ACT lowers the distance
  from 3.7σ to 2.8σ [src: arXiv:2506.20707, Sect. VII.3]. SPT + Planck
  exceeds 3σ although each is below it, "due to the constraining power of
  the combined CMB data sets".
- P-ACT (1.6σ) is closer to DESI than PR4 Planck because of its lower Ω_m,
  "connected to the n_s–Ω_b h² degeneracy-breaking that the new ACT
  small-scale data provide" [src: arXiv:2503.14452, App. H].
- DESI's CamSpec + lensing CMB gives 2.3σ (1.9σ in DR1) [src:
  arXiv:2503.14738, Sect. VI]. App. A of DESI compares CamSpec, Plik and
  HiLLiPoP for w0wa, where HiLLiPoP shifts the posterior by about 0.1σ [src:
  App. A]; the effect of the likelihood choice on the ΛCDM distance itself
  is not reported there.

### τ treatment
<!-- key: tau-treatment -->

From arXiv:2506.20707, App. I, Fig. 47:

| ACT DR6 variant | Distance to DESI | Place read |
|---|---|---|
| ACT lensing, NPIPE τ prior | 3.1σ | arXiv:2506.20707, App. I, Fig. 47 |
| ACT lensing, SRoll2 τ likelihood | 2.9σ | same |
| + Planck lensing, NPIPE τ prior | 2.9σ | same |
| + Planck lensing, SRoll2 (ACT's baseline) | 2.7σ | same |

SPT concludes that "the significance of the ACT DR6–DESI discrepancy is
sensitive to analysis choices" and reports, throughout, values "with
consistent priors" [src: App. I]; it also notes it used the ACT-lite
likelihood, which "may lead to a small difference".

Shifting the τ prior instead of changing its source [src: arXiv:2504.16932,
Sects. II–III]: Planck PR4 CamSpec high-ℓ + PR4 and ACT DR6 lensing, low-ℓ
data replaced by a Gaussian τ prior of width 0.006; the distance falls from
2.1σ (τ = 0.06) to 0.9σ (τ = 0.09). The CMB degeneracy is approximately
Ω_m(τ) = 0.349 − 0.505τ [src: Fig. 1 caption].

Along this degeneracy a
higher τ lowers the CMB Ω_m towards the DESI value, which is how a high τ
absorbs the mismatch [der].

With τ free (uniform 0.02–0.20) and no low-ℓ data, high-ℓ CMB + lensing +
DESI give τ = 0.090 ± 0.012 in ΛCDM and 0.095 ± 0.014 with Σm_ν ≥ 0.06 eV
[src: arXiv:2504.16932, Eq. 2]; Jhaveri et al. find 0.091 ± 0.011 with
M_ν = 0.06 eV, and the 1.4σ agreement between CMB without low-ℓ EE and the
low-ℓ EE data "becomes a 2.7σ tension with the inclusion of BAO" [src:
arXiv:2504.21813, Sect. III.3, Eq. 6]. P-ACT + DESI DR2 already prefer a τ
1.3σ above SRoll2 (1.1σ with DR1) [src: arXiv:2503.14452, App. H, Fig. 44].

Why τ moves Ω_m: the acoustic peaks fix A_s e^(−2τ), so a higher τ raises
A_s and the predicted lensing [src: arXiv:2504.21813, Sect. III.3]; the
lensing reconstruction fixes A_s(Ω_m^0.6 h)^2.3 to about 2%, which with θ*
implies a lensing-only Ω_m h² constraint of 1.2–1.9%, comparable with the
0.8% from the primary anisotropies, so the two can pull the joint value
[src: arXiv:2606.30527, Sect. VII.1].

### CMB lensing reconstruction and compression
<!-- key: cmb-lensing-reconstruction-and-compression -->

- Without CMB lensing, DESI's distance falls from 2.3σ to 2.0σ [src:
  arXiv:2503.14738, Sect. VI].
- In w0wa, compressed (θ*, ω_b, ω_bc), CMB without lensing and full CMB give
  "remarkably similar" posteriors, because the CMB mainly anchors Ω_m; but
  lensing "does appreciably change the Δχ²_MAP values and thus the
  significance of rejection of ΛCDM" [src: App. A].

### Subspace and statistic
<!-- key: subspace-and-statistic -->

| Statistic | What it compares | DR2 value | Place read |
|---|---|---|---|
| 2D Gaussian PTE in (Ω_m, h r_d), posterior means | DESI vs CamSpec + lensing | 2.3σ | arXiv:2503.14738, Eq. 18 |
| Same, best-fit values, τ = 0.06 prior | DESI vs CamSpec + lensing | 2.1σ | arXiv:2504.16932, Sect. III |
| 1D update difference in Ω_m | CMB vs CMB + BAO, Plik PR3 + three lensing sets | 2.5σ | arXiv:2504.21813, Sect. III.1 |
| Leading SVD mode c₀ (≈ Ω_m h²) | DESI vs ACT DR6 without lensing | +2.2σ | arXiv:2606.30527, Sect. IV.4 |
| Bin-averaged ω_m from D^par | DESI vs Planck TTTEEE | 2.1σ (DR1 1.9σ) | arXiv:2505.02658, Sect. 2 |

Same data family, five statistics, five values (table above). Quote the
statistic with the number.

## Is it carried by one redshift bin?
<!-- key: is-it-carried-by-one-redshift-bin -->

D^perp, the direction the Planck ΛCDM model predicts exactly [src:
arXiv:2505.02658, Table 1]:

| Bin | z_eff | γ [rad] | D^perp Planck | DR1 (N_σ) | DR2 (N_σ) |
|---|---|---|---|---|---|
| LRG1 | 0.510 | 0.816 | 5.74 | 4.45 ± 0.52 (2.48) | 5.08 ± 0.37 (1.78) |
| LRG2 | 0.706 | 0.500 | 9.22 | 9.54 ± 0.60 (−0.53) | 8.76 ± 0.34 (1.35) |
| LRG3 + ELG1 | 0.934 | 0.243 | 11.76 | 12.12 ± 0.37 (−0.97) | 11.92 ± 0.21 (−0.76) |
| ELG2 | 1.321 | 0.0274 | 13.30 | 13.06 ± 0.43 (0.56) | 13.42 ± 0.22 (−0.54) |
| QSO | 1.484 | −0.0177 | 13.42 | — | 13.35 ± 0.51 (0.14) |
| Lyα | 2.33 | −0.0991 | 12.46 | 12.51 ± 0.15 (−0.33) | 12.448 ± 0.091 (0.14) |

N_σ is in units of the DESI error only (the Planck value has negligible
error). BGS is left out because only D_V/r_d is published for it.

ω_m from D^par [src: arXiv:2505.02658, Table 2, Sect. 2]: LRG2 gives
0.1371 ± 0.0015 against Planck 0.14205 ± 0.00123, about 2.6σ low; the other
DR2 bins give 0.1387–0.1441. Averaged over bins, 0.13909 ± 0.00073 (DR2)
and 0.1384 ± 0.0015 (DR1), 2.1σ and 1.9σ from Planck. P-ACT gives ω_m =
0.1425 ± 0.0012, "very close to the Planck result".

Reading. In this decomposition the mismatch is a ω_m (equivalently Ω_m h²)
offset spread over the z < 1 bins, largest in LRG2, while the
direction the CMB fixes agrees bin by bin. DESI's own Hubble-diagram
reading is that DESI distances are 1–2% below the Planck ΛCDM prediction at
z ≤ 1 [src: arXiv:2503.14738, Sect. VII.2, Fig. 13]. Zaldarriaga finds no
second measurable direction in ΛCDM (σ_c1 = 0.06 for BAO) [src:
arXiv:2606.30527, Sect. IV.4]. The author of the rotation argues that DR2 is
"substantially more consistent with the Planck ΛCDM cosmology in the
perpendicular direction and only marginally worse in the parallel
direction" than DR1 [src: arXiv:2505.02658, Sect. 2]; DESI reads the same
DR1-to-DR2 change as an increase from 1.9σ to 2.3σ [src:
arXiv:2503.14738, Sect. VI]. Both are correct about different projections.

## In which direction each extension moves the CMB side
<!-- key: in-which-direction-each-extension-moves-the-cmb -->

| Extension | Mechanism stated | Effect on the mismatch | Place read |
|---|---|---|---|
| Higher τ | raises A_s, hence lensing; Ω_m anti-correlated with τ | 2.1σ → 0.9σ (τ 0.06 → 0.09); n_s 0.968 ± 0.004, H0 67.94 ± 0.44 at τ ≈ 0.09 | arXiv:2504.16932, Sect. III, abstract |
| Σm_ν free | at fixed θ*, more neutrino mass lowers H0 and raises Ω_m: ΔM_ν ≈ 2.5 ΔΩ_m/Ω_m | BAO's low Ω_m pushes M_ν below zero; 5% of the posterior above 0.06 eV with BAO, 50% without; extrapolated profile minimum −0.035 to −0.022 eV | arXiv:2504.21813, Sect. III.1, Fig. 1–2 |
| A_L free | decouples peak smoothing from peak amplitude | A_L = 1.09 at M_ν = 0.06 eV, Δχ² = −10.05; SVD c₀ tension 2.2σ → 1.1σ | arXiv:2504.21813, Table 1; arXiv:2606.30527, Table 10 |
| Ω_K free | geometric degeneracy along Ω_m h²–Ω_K | DESI + CMB 10³Ω_K = 2.3 ± 1.1 (CMB alone −10.7 +6.4/−5.3); c₀ tension rises 2.2σ → 2.6σ as the CMB prediction broadens (σ_c0 8.8 vs 1.6) but its mean moves away | arXiv:2503.14738, Table 5; arXiv:2606.30527, Sect. VI.3 |
| w0wa | changes late distances; CMB fixes only D_M(z*) | DESI + CMB Ω_m = 0.353 ± 0.021, H0 = 63.6 (+1.6/−2.1) | arXiv:2503.14738, Table 5 |
| wCDM | one constant w | "lacks sufficient flexibility": the DESI + CMB + DESY5 best fit (w = −0.971, Ω_m = 0.310) performs "only slightly better than Planck ΛCDM" | arXiv:2503.14738, Sect. VII.2 |
| EDE (n = 2) | pre-recombination | c₀ tension 1.8σ, "≈ ΛCDM" | arXiv:2606.30527, Table 10 |
| Primordial magnetic field B_PMF | recombination | c₀ tension 1.0σ (broadened) | arXiv:2606.30527, Table 10 |

The degeneracy chain linking three rows [src: arXiv:2504.21813, Eq. 4]:
ΔM_ν ≈ 5Δτ ≈ 2.5 Δln A_L, so a shift of τ from 0.054 to 0.092 "works
comparably well as A_L ∼ 1.09". With A_L or no low-ℓ EE, Δ(χ² − χ²_τ) ≈ −6
in both cases [src: Table 1]. For CMB + BAO, χ²(M_ν = 0) − χ²(0.06) ≈ −4.5,
of which ≈ −1.7 comes from the low-ℓ EE likelihood itself [src: Eq. 2,
Table 1]. Note the different CMB: Plik PR3 + Planck PR4, ACT DR6 and SPT-3G
MUSE lensing [src: Sect. II].

## Testing whether an extension only absorbs the mismatch
<!-- key: testing-whether-an-extension-only-absorbs-the -->

1. Split the χ² by likelihood. SPT tabulates, for each extension, the χ²
   gain of each data set alone and of the joint fit [src:
   arXiv:2506.20707, Table 7]:

   | Model | CMB-SPA alone | DESI alone | CMB-SPA + DESI |
   |---|---|---|---|
   | A_lens | 2.1 (1.5σ) | — | 6.9 (2.6σ) |
   | Ω_K | 2.8 (1.7σ) | 0.3 (0.6σ) | 4.2 (2.1σ) |
   | Σm_ν | 0.7 (0.8σ) | — | 5.1 (2.3σ) |
   | w0wa | — | 4.7 (1.7σ) | 11.6 (3.0σ) |
   | ModRec | 8.5 (1.1σ) | — | 13.2 (1.8σ), no lensing |

   In ΛCDM the CMB χ² is 603.7 in the separate fit and 606.7 in the joint
   fit, and the DESI χ² 10.3 and 14.6; in w0wa the joint DESI χ² drops to
   7.4 and the CMB χ² to 602.3 (arXiv:2506.20707) [src: Table 7].

   A gain that appears mainly in the joint fit is the signature of a model
   that reconciles two data sets rather than one that fits a feature of
   either [der: reading of Table 7].
   SPT's own wording: "differences between CMB and DESI data lead to sizeable
   shifts from the CMB-preferred values in joint constraints and moderate
   departures from ΛCDM" [src: Fig. 26 caption].
2. Ask whether the extension opens a new measurable direction. In the SVD
   basis, w0wa makes a second mode measurable; its BAO amplitude is a₁ =
   +1.24 ± 1.0 (+1.2σ), equivalent to w(z = 0.46) = −0.94 ± 0.052, and "the
   dominant +2.2σ DESI tension lives in c₀ (Ω_m h²), not in the dark energy
   mode" [src: arXiv:2606.30527, Sect. V.4, Table 7]. The Planck + DESI w0wa
   chain predicts ⟨c₁⟩ ≈ −3 for supernovae; Union3, Pantheon+ and DES-Dovekie
   measure −1.49, +0.23 and −0.75, so the chain's extrapolation "overshoots
   the SN data" [src: Table 7].
3. Rotate the extension's parameters. Fixing w at a pivot, w_piv = w0 +
   wa z_piv/(1 + z_piv) [src: arXiv:2505.02658, Eq. 8], with z_piv ≈ 0.5
   matched to the DESI + CMB degeneracy, gives w_piv = −0.996 ± 0.046 for
   DESI + compressed CMB [src: Eq. 10]; Δχ²_MAP (−8.0, 2.4σ) is unchanged,
   and a one-parameter model on the same line would be quoted at 2.8σ,
   which the author uses to argue that Δχ²-to-σ conversion carries "no
   measure of contrivedness" [src: Sect. 3]. The pivot value of DESI's own
   combination is in `results.md#frequentist-significance-by-combination`.
4. Replace the anchor. DESI swaps the CMB for DES Y3 3×2pt, which also
   breaks the Ω_m degeneracy with low-redshift data only; with DESY5 it
   "also excludes ΛCDM at high significance" [src: arXiv:2503.14738, Fig.
   14]. Agreement between anchors argues against a CMB-side cause.
5. Compare evidences and the dimensionality of the conflict:
   `cosmo-statistics-inference` `deep/tension-metrics.md` (Ong et al.).

What each side concludes. DESI: the w0wa model "does have sufficient
flexibility to simultaneously achieve good fits to all three datasets",
fitting α_∥ better than any ΛCDM model while resolving the Ω_m mismatch
[src: arXiv:2503.14738, Sect. VII.2]. Critics: the combination of CMB and
BAO is "mired in the swampland of ∼2–3σ statistics, where the
interpretation is strongly dependent on choices of priors" because BAO
follow almost the CMB geometric degeneracy [src: arXiv:2505.02658, Sect.
3]; τ is a "single-point failure" for nearly all CMB analyses [src:
arXiv:2504.16932, abstract]. SPT keeps both open: ΛCDM "provides an
excellent fit to CMB and BAO data separately", yet certain combinations
"differ at a level that is borderline statistically significant" [src:
arXiv:2506.20707, Sect. VII.3].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Analysis | Source | Place read |
|---|---|---|---|---|
| DESI Ω_m–h r_d correlation | r = −0.92 | DESI DR2 BAO | arXiv:2503.14738 | Eq. 17 |
| DESI + CMB joint, ΛCDM | Ω_m 0.3027 ± 0.0036, H0 68.17 ± 0.28, r = −0.975 | DESI DR2 | arXiv:2503.14738 | Eq. 21 |
| SPT τ prior | N(0.051, 0.006) | SPT-3G D1 | arXiv:2506.20707 | Table 3 |
| CMB τ–Ω_m slope | Ω_m = 0.349 − 0.505τ | high-ℓ + lensing | arXiv:2504.16932 | Fig. 1 |
| Combination threshold | 3σ (SPT explicit; DESI "not close to 3σ") | — | arXiv:2506.20707; arXiv:2503.14738 | Sect. VII.3; Sect. VI |
| Largest bin-to-bin ΛCDM difference | 1.8σ (LRG1 vs LRG3 + ELG1) | DESI DR2 | arXiv:2503.14738 | Sect. III.3.1 |
| DESI vs SN Ω_m, ΛCDM | 1.7σ / 2.1σ / 2.9σ (Pantheon+ / Union3 / DESY5) | DESI DR2 | arXiv:2503.14738 | Sect. VI |
| Planck ΛCDM ω_m | 0.14205 ± 0.00123 | Planck TTTEEE | arXiv:2505.02658 | Sect. 2 |
| SVD c₀ tension, CMB extensions | ΛCDM 2.2σ; A_lens 1.1σ; B_PMF 1.0σ; EDE 1.8σ; Ω_K 2.6σ | ACT DR6 chains | arXiv:2606.30527 | Table 10; Sect. VI.3 |
| ΔM_ν–Δτ–ΔA_L chain | ΔM_ν ≈ 5Δτ ≈ 2.5 Δln A_L | CMB without low-ℓ EE + BAO | arXiv:2504.21813 | Eq. 4 |
| H0 with CMB (no low-ℓ EE) + BAO | 68.69 ± 0.31 | M_ν = 0.06 eV | arXiv:2504.21813 | Eq. 7 |

## What goes wrong
<!-- key: what-goes-wrong -->

- "The CMB–DESI tension is 2.3σ" (arXiv:2503.14738 [src: Sect. VI]) without
  the CMB set: the same BAO are 2.0σ from SPT's Planck and 3.7σ from SPT +
  ACT (arXiv:2506.20707 [src: Sect. VII.3]). Test: name
  the likelihood, the lensing set and the τ treatment.
- Comparing numbers across statistics (2D PTE with means or best fits, 1D
  update difference, SVD mode, bin average, multi-set Q_DM): they differ on
  the same data family (Subspace table), and the
  multi-set value in `deep/tension-metrics.md` of the statistics skill is
  lower still. Test: recompute with Eq. 18 on the two posteriors.
- Applying Eq. 18 to extension chains. The Gaussian form is a ΛCDM
  approximation; with Ω_K free the CMB prediction is spread over
  H0 ∈ [55, 68] [src: arXiv:2606.30527, Fig. 14 caption]. Test: KS check of
  the projected distribution, as in arXiv:2606.30527, Sect. II.3.5.
- Treating τ variants as independent tests: every combination in the SPT
  and DESI tables uses a Planck-based τ; the "τ resolution" moves all of
  them together [src: arXiv:2504.16932, abstract].
- Combining above the threshold: joint ΛCDM values of H0, σ8 and n_s then
  sit away from both inputs [src: arXiv:2506.20707, Sect. VII.3].
- A ΛCDM fit to data from dynamical dark energy can bias Ω_m (mock SDSS
  study; "more work is needed" for DESI) [src: arXiv:2506.20707, fn. 43].
- Reading DR1 → DR2 as "growing": true in the 2D plane, not in D^perp.

## Reading list
<!-- key: reading-list -->

- Method and result: DESI DR2, arXiv:2503.14738 — Eq. 18, Sect. VI, the
  internal checks of Sect. III.3.1, the compressed prior of App. A, the
  Hubble-diagram reading of Sect. VII.2.
- Application: SPT-3G D1, arXiv:2506.20707 — Sect. VII.3 table and 3σ rule,
  Table 7 χ² split, App. I τ variants.
- Application: ACT DR6, arXiv:2503.14452 — App. H, why P-ACT is closest.
- Critique: Sailer et al. 2025, arXiv:2504.16932 — the τ–Ω_m degeneracy and
  τ from BAO.
- Critique: Jhaveri, Karwal & Hu 2025, arXiv:2504.21813 — degeneracy chain
  M_ν–τ–A_L and the χ² bookkeeping of Table 1.
- Critique: Efstathiou 2025, arXiv:2505.02658 — rotated distances per bin;
  the pivot argument against Δχ²-based significance.
- Method: Zaldarriaga 2026, arXiv:2606.30527 — SVD modes; which extension
  opens a new direction.

## Not verified
<!-- key: not-verified -->

- The mock study of ΛCDM bias under dynamical dark energy cited as
  "Tang et al." (ref. 160 of arXiv:2506.20707): not identified or read. [src: Sect. VII.3]
- The "update difference in means" statistic of Jhaveri et al.
  (arXiv:2504.21813, taken from one of their references): reference not
  identified; formula not read.
- The DESI DR2 distance with Plik or HiLLiPoP in place of CamSpec in ΛCDM:
  not found in arXiv:2503.14738.
- The 2026 SPT-3G D1 lensing reconstruction (arXiv:2608.31136) values of
  Ω_m and of the DESI distance: only the abstract statements in L2 are
  used; its Sect. VII.3 was not read.
