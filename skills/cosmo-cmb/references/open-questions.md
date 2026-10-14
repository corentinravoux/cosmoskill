# CMB — open questions, internal tensions and stale claims

Scope: the live controversies in primary-CMB and CMB-lensing cosmology with
both sides cited, the tensions between analyses, what the next data decide,
forecasts, and the claims that still circulate after being corrected.
Snapshot: 2026-10-07

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. Forecasts are labelled **forecast**.

---

## 1. Is the Planck large-scale polarisation value of τ right?
<!-- key: is-the-planck-large-scale-polarisation-value-of -->

**Why it matters.** τ is the least well measured base parameter and every
analysis that includes CMB data takes it from Planck low-ℓ EE. Sailer et
al. 2025 (arXiv:2504.16932) call this a "single-point failure" [src].

**The case that τ could be higher.** DESI BAO prefer a lower Ω_m than the
CMB. Because the CMB-inferred τ is anti-correlated with the matter
fraction, dropping the low-ℓ EE data lets τ rise and absorbs the
discrepancy:

- DESI BAO + high-ℓ CMB + CMB lensing give τ = 0.090 ± 0.012 in ΛCDM,
  described as 3–5σ from Planck low-ℓ polarisation; with τ ≈ 0.09 the
  preference for evolving dark energy drops from about 3σ to about 1.5σ,
  and n_s and H₀ rise to 0.968 ± 0.004 and 67.94 ± 0.44 [src]
  (arXiv:2504.16932).
- Jhaveri, Karwal & Hu 2025 (arXiv:2504.21813) find τ = 0.091 ± 0.011 when
  the lensing and low-ℓ EE constraints are dropped, removing the neutrino
  tension at Σm_ν = 0.06 eV and taking the w₀–w_a preference below 95% CL;
  freedom in the reionisation model alone takes the ΛCDM neutrino tension
  below 95% CL [src].
- If the low-ℓ temperature power deficit is a physical inflationary
  feature, the Planck 95% upper limit on τ rises from 0.0696 to 0.075, and
  to 0.082 with all CMB + BAO data [src] (Jhaveri et al. 2026,
  arXiv:2606.20795).

**The case that τ is about 0.055–0.06.**

- Five reprocessings and likelihood constructions of Planck data between
  2018 and 2023 give 0.051–0.063 (table in `results.md`, Section 5).
  Sailer et al. themselves state there "is no evidence for systematics in
  the large-scale Planck data" [src].
- CLASS × Planck, from the ground with a different instrument and
  modulation scheme: 0.053 (+0.018/−0.019) [src] (Li et al. 2025,
  arXiv:2501.11904). The error is too large to exclude 0.09 on its own:
  (0.090 − 0.053)/0.018 ≈ 2σ [der].
- Reionisation-history data with CMB data that exclude low-ℓ EE:
  τ = 0.0552 with statistical and systematic errors of a few 10⁻³ and a
  2.4σ tension with DESI DR2 remaining (Kageura et al. 2026,
  arXiv:2601.09644); τ = 0.067 ± 0.011 with a ≳2σ dark-energy preference
  remaining (Montero-Camacho & Mao 2026, arXiv:2607.26373) [src]. Both
  conclude that a low-ℓ polarisation systematic is unlikely to be the full
  explanation.

**What decides it.** An independent cosmic-variance-limited low-ℓ EE
measurement. LiteBIRD is the designed instrument and is now scheduled for
JFY2036 (`surveys-and-data.md`); CLASS continues from the ground. Until
then the honest statement is that the BAO-preferred τ and the measured τ
disagree at a level set by which data one drops, and that astrophysical
reionisation probes side with the measured value.

Reionisation astrophysics belongs to `cosmo-reionization-21cm`.

## 2. The fate of the A_L anomaly
<!-- key: the-fate-of-the-al-anomaly -->

**History.** A_L was introduced in 2008 on WMAP5+ACBAR, which already
showed a 2.5σ high value (Calabrese et al. 2008, arXiv:0803.2309) [src].
Planck 2018 found A_L = 1.180 ± 0.065 with Plik and noted that CamSpec
gives a value nearer unity (Planck Collaboration 2018, arXiv:1807.06209).
Motloch & Hu 2019 (arXiv:1912.06601) quantified the legacy-release
smoothing as 2σ high relative to the lensing reconstruction and 2.8σ high
relative to the ΛCDM expectation from the unlensed information, and
stressed that it is inconsistent with real lensing because the
reconstruction disagrees independently of the model [src]. Addison et al.
2015 (arXiv:1511.00055) had shown the related ℓ < 1000 versus ℓ ≥ 1000
tension in Planck 2015 TT (Ω_c h² discrepant at 2.5σ; H₀ = 69.7 ± 1.7
against 64.1 ± 1.7) [src]; the Planck Collaboration replied that such
shifts are not unusually large (arXiv:1608.02487) [src].

**The curvature episode.** Di Valentino, Melchiorri & Silk 2019
(arXiv:1911.02087) read the same feature as a preference for a closed
universe at more than 99% CL and a "possible crisis" [src]. Efstathiou &
Gratton 2020 (arXiv:2002.06892) answered with a CamSpec likelihood on more
sky: Planck spectra are consistent with flatness, and with BAO
Ω_K = 0.0004 ± 0.0018 [src].

**Present state** (numbers in `results.md`, Section 3).

- Planck PR4 reanalyses reduce it: 1.095 ± 0.056 (CamSpec) and
  1.039 ± 0.052 (HiLLiPoP).
- ACT DR6 and SPT-3G D1 see none: 1.007 ± 0.057 and, combined,
  1.016 (+0.048/−0.054). ACT does not see the oscillatory TT residual at
  1000 < ℓ < 2000 that drives it in Planck [src] (arXiv:2503.14452).
- It survives at about 2σ in combinations that include full-range Planck
  TT: A_2pt = 1.079 ± 0.038 for CMB-SPA.
- SPT's position: the comparison "may suggest that the features in the
  Planck spectrum … may not be cosmological and rather statistical or
  systematic", but "we cannot make a definitive judgment" [src]
  (arXiv:2506.20707).

**Why it still matters in 2026.** The excess smoothing leaks into
parameters that change lensing. Cozzumbo et al. 2025 (arXiv:2511.01967)
attribute the apparent preference for negative neutrino mass to excess
lensing relative to that inferred from Planck spectra: with two lensing
nuisance parameters freed the effective mass is −0.018 (+0.085/−0.089) eV
[src]. De Cruz Pérez, Park & Ratra 2026 (arXiv:2604.03756) find
A_L = 1.053 ± 0.034 for PR4 with lensing and non-DESI low-redshift data,
and that freeing A_L lowers the w₀w_a preference from about 1.8σ to about
1.5σ in their data combination [src]. Against this, Green & Meyers 2024
(arXiv:2407.07878) argue that the negative-mass preference comes from
larger-than-expected lensing in both the two- and four-point statistics
and is robust to likelihood choices [src], and ACT argues that once
lensing and BAO are included the spectrum smoothing is not the main
driver of the neutrino bound [src] (arXiv:2503.14454).

**Rule.** Do not write "the A_L anomaly is resolved" or "Planck prefers
A_L > 1 at 2.8σ" without naming the likelihood and release.

## 3. How large is the CMB–DESI discrepancy in ΛCDM?
<!-- key: how-large-is-the-cmb-desi-discrepancy-in -->

The quoted significance ranges from 1.6σ to 3.7σ depending on the CMB
data set (`results.md`, Section 2). Two things drive the spread: ACT DR6
and SPT-3G D1 prefer a higher Ω_m (0.330 ± 0.010 and 0.3246 ± 0.0091 in
the SPT rerun) than Planck (0.3145 ± 0.0067) [src] (arXiv:2506.20707), and
P-ACT discards Planck high-ℓ data. Adding Planck large-scale data pulls
the ground-based combination back toward DESI, hence 3.7σ for SPT+ACT but
2.8σ for CMB-SPA [src].

Extended models relieve it, which is why CMB + DESI shows 2–3σ shifts in
Ω_K, A_lens or (w₀, w_a) [src] (arXiv:2506.20707). SPT notes that the
A_lens > 1 obtained with DESI "is a rephrasing of the marginal agreement
of the two probes in ΛCDM" [src]. With the 2026 SPT lensing the curvature
and dark-energy preferences fall to about 2σ [src] (arXiv:2608.31136).

For ΛCDM+N_eff the CMB and DESI constraints differ by more than 3σ for
SPT+ACT and CMB-SPA, so SPT declines to combine them [src]
(arXiv:2506.20707). This is a case where a joint constraint must not be
quoted without the consistency check.

Interpretation belongs to `cosmo-dark-energy-modified-gravity` and
`cosmo-tensions-anomalies`.

## 4. N_eff: ACT low, SPT at the standard value
<!-- key: neff-act-low-spt-at-the-standard-value -->

ACT DR6 alone gives 2.60 (+0.21/−0.29) and SPT-3G D1 alone 3.18
(+0.29/−0.33); the combinations give 2.73–2.86 with errors of 0.12–0.14
(`results.md`, Section 6). ACT attributes its shift to the DR6 data
preferring "somewhat less damping than the Planck best-fit model" and
works out that the P-ACT central value would need a 12% increase of the
photon energy density after neutrino decoupling, which FIRAS spectral-
distortion limits exclude over most of the relevant redshift range [src]
(arXiv:2503.14454). No combination is more than 2σ from 3.044 [src]
(arXiv:2506.20707). The question for the next data is whether the ACT
damping-tail preference persists in SPT's wider fields and in SO.

Light-relic model constraints belong to `cosmo-neutrinos-dark-matter`.

## 5. Neutrino mass from CMB + BAO
<!-- key: neutrino-mass-from-cmb-bao -->

Limits of 0.064–0.089 eV sit at or below the oscillation minimum, and
analyses that allow an effective negative mass find a preference for it
(Craig et al. 2024, arXiv:2405.00836: −160 ± 90 meV with DESI DR1; Elbers
et al. 2025, arXiv:2503.14744: 3σ tension with the oscillation limit)
[src]. The CMB-side levers are τ (Section 1), the lensing amplitude
(Section 2) and the choice of lensing reconstruction: the 2026 SPT
analysis relaxes the bound to 0.072 eV because its lensing agrees better
with DESI [src] (arXiv:2608.31136). In w₀w_a CDM the limit relaxes to
0.16 eV [src] (arXiv:2503.14738).

## 6. SPT-3G polarised beams
<!-- key: spt-3g-polarised-beams -->

The D1 cosmology relies on a sidelobe-depolarisation model introduced
after unblinding and preferred at 5σ by the spectra within ΛCDM
(arXiv:2506.20707). The direct point-source measurement published in 2026
finds β_pol consistent with no depolarisation and differs from the
spectrum-inferred values at 1.3σ (arXiv:2602.06334) [src]. The discrepancy
is modest and model dependent, but the authors leave open that the
frequency-dependent EE residual has another origin. The D1 paper itself
notes that an independent polarised-beam characterisation "would increase
the constraining power of the EE band powers" [src]. Watch how the next
SPT-3G release treats this, and whether n_s from SPT alone
(0.951 ± 0.011) moves.

## 7. ACT versus Planck at the parameter level
<!-- key: act-versus-planck-at-the-parameter-level -->

ACT reports 1.6σ against PR3 and 2.5σ against NPIPE in the four shape
parameters, with the shift most visible in Ω_b h²–Ω_c h² and Ω_b h²–H₀
[src] (arXiv:2503.14452). P-ACT then excludes the corner of the Planck PR3
posterior with the lowest H₀, Ω_b h² and n_s. Whether 2.5σ against NPIPE
is a fluctuation is open; a full ACT–Planck cross-covariance, which ACT
left for future work, is the missing piece.

## 8. The upward drift of n_s
<!-- key: the-upward-drift-of-ns -->

Planck 2018: 0.965 ± 0.004. P-ACT: 0.9709 ± 0.0038. CMB-SPA:
0.9679 ± 0.0033. With DESI: 0.974 ± 0.003 (P-ACT-LB) and 0.9726 ± 0.0028
(CMB-SPA + DESI) [src] (arXiv:1807.06209, arXiv:2503.14452,
arXiv:2506.20707). The CMB + BAO shift follows the same Ω_m–τ–n_s
correlation as in Section 1, so n_s from CMB + DESI in ΛCDM inherits the
CMB–BAO discrepancy. SPT-3G D1 alone gives a low and weak 0.951 ± 0.011.
Consequences for inflation models belong to `cosmo-inflation-primordial`.

## 9. Which Planck likelihood
<!-- key: which-planck-likelihood -->

Jense et al. 2025 (arXiv:2510.09430) find that once ground data are added
the choice of Planck maps and likelihood stops mattering for extended
models, but that a truncated CamSpec with fully marginalised foregrounds
can mislead [src]. The practical split remains: ACT and SPT use PR3 for
high ℓ, while Jense et al. describe CamSpec on NPIPE as the usual
reference for the PR4 cosmology [src]. No PR4-based CMB-SPA was found in
the searches of 2026-10-07.

## 10. Cosmic birefringence (pointer)
<!-- key: cosmic-birefringence-pointer -->

ACT DR6 gives β = 0.215° ± 0.074°, same sign and similar size as earlier
WMAP and Planck results, with the authors' caveat on unexplained
systematics (Diego-Palazuelos & Komatsu 2025, arXiv:2509.13654) [src]. The
2022 review counted the hint at 3σ (Komatsu 2022, arXiv:2202.13919) [src].
Treat as unconfirmed; details in `cosmo-inflation-primordial` and
`cosmo-tensions-anomalies`.

## 11. Primordial B modes after the CMB-S4 cancellation
<!-- key: primordial-b-modes-after-the-cmb-s4-cancellation -->

Current limit: r < 0.036 (BK18) or < 0.032 with Planck PR4 and BAO. The
published forecasts for what replaces CMB-S4:

| Programme | σ(r) (**forecast**) | Assumptions | Source |
|---|---|---|---|
| BICEP/Keck, data through 2024 | ≈ 0.005 | including delensing | arXiv:2606.13942 |
| BICEP Array | ≈ 0.001 by 2034 | — | arXiv:2606.13942 |
| SPT-3G+ with BICEP Array | 0.001 | six-year survey from 2029, 0.5 μK-arcmin | arXiv:2608.20236 |
| SO, three SATs, five years | 0.003 | 2018 baseline | arXiv:1808.07445 |
| SO, six SATs to 2035 | 1.2 × 10⁻³ (7 × 10⁻⁴ optimistic) | 70% delensing, ℓ_knee = 50 | arXiv:2512.15833 |
| LiteBIRD, reformed | δr < 0.002 total | launch JFY2036 | arXiv:2607.25285 |

Lensing B modes already limit the strongest constraint (Nakato et al.
2026, arXiv:2608.06343) [src], so delensing efficiency, not only map
depth, sets the reach. Whether SO can delens 70% and whether dust
complexity allows the "moderately complex" foreground assumption are the
open technical questions.

## 12. What the next data decide
<!-- key: what-the-next-data-decide -->

| Question | Deciding data | When |
|---|---|---|
| Does the absence of excess smoothing hold with more sky? | SPT-3G full 10,000 deg² survey; SO LAT | SPT fields in hand; SO data not yet public |
| Is the ACT damping-tail preference (low N_eff) real? | SPT-3G Summer and Wide fields, SO LAT TT/TE/EE | same |
| Is τ ≈ 0.055? | CLASS; LiteBIRD | LiteBIRD not before JFY2036 |
| Is the CMB–DESI discrepancy growing? | DESI DR3 BAO with CMB-SPA or a PR4-based successor | see `cosmo-galaxy-clustering` |
| r at the 10⁻³ level | BICEP/Keck through 2024 with SPT delensing; SO SATs | next BICEP release; SO to 2035 |

The SPT-3G forecast is that the full survey with Planck improves the
early-dark-energy and varying-electron-mass figures of merit by factors
above 90 and 190 (**forecast**) [src] (Vitrier et al. 2025,
arXiv:2510.24669).

## 13. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

| Claim still seen | Correction | Source |
|---|---|---|
| "CMB-S4 will measure σ(N_eff), Σm_ν, r in the 2030s" | CMB-S4 lost DOE and NSF support on 9 July 2025 and is shutting down | cmb-s4.org |
| "LiteBIRD launches in the late 2020s with three telescopes and 15 bands" | Reformed to one telescope and 12 bands; launch JFY2036 | arXiv:2607.25285; ISAS/JAXA page |
| "Planck is the most constraining CMB data set" | SPT+ACT equals Planck on H₀ and σ₈ and is tighter on N_eff; CMB-SPA is the tightest | arXiv:2506.20707 |
| "Planck prefers A_L > 1 at 2.8σ" | True for PR3 Plik only; 0.75–1.7σ for PR4 likelihoods; none in ACT or SPT | arXiv:2309.10034, arXiv:2503.14452 |
| "Planck favours a closed universe" | PR3 Plik spectra alone; PR4 HiLLiPoP gives −0.012 ± 0.010, and any BAO combination is flat | arXiv:2309.10034, arXiv:2002.06892 |
| "ACT and SPT are independent of Planck" | Both are calibrated on Planck and take τ from Planck; only shape information is independent | arXiv:2503.14452, arXiv:2506.20707 |
| "The CMB gives H₀ = 67.4 ± 0.5" | That is Planck 2018. Current: 67.62 ± 0.50 (P-ACT), 66.66 ± 0.60 (SPT-3G D1), 67.19 ± 0.38 (CMB-SPA) | `results.md` |
| "CMB-SPA gives H₀ = 67.24 ± 0.35" | First-version value; the revised paper gives 67.19 ± 0.38 | arXiv:2506.20707 v2 |
| "ACT DR6 gives Σm_ν < 0.082 eV" | First-version abstract; the revised value is < 0.089 eV | arXiv:2503.14454 v2 |
| "ACT DR6 measures n_s = 0.974" | That is P-ACT-LB (with lensing and DESI); P-ACT alone is 0.9709 ± 0.0038 | arXiv:2503.14452 |
| "CMB lensing confirms a low S₈" | All reconstructions are consistent with the primary-CMB prediction (amplitudes 1.00–1.03 with 2% errors) | arXiv:2304.05202, arXiv:2504.20038, arXiv:2608.31136 |
| "S₈ from lensing papers can be compared directly with cosmic shear" | Lensing papers quote σ₈(Ω_m/0.3)^0.25 or σ₈Ω_m^0.25 | arXiv:2304.05202 |
| "A_L measures lensing" | It is a consistency parameter for peak smoothing; the reconstruction amplitude is a different quantity | arXiv:0803.2309, arXiv:2506.20707 |
| "The DESI–CMB tension is 2.3σ" | It is 1.6–3.7σ depending on the CMB data set | `results.md`, Section 2 |
| "Blinded analysis, so no tuning" | Both ACT DR6 and SPT-3G D1 made documented post-unblinding changes | arXiv:2503.14452, arXiv:2506.20707 |
| "N_eff standard value 3.046" | 3.044 in ACT DR6 and SPT-3G D1; 3.046 in Planck 2018 | arXiv:2503.14454, arXiv:1807.06209 |

## Not verified
<!-- key: not-verified -->

- No Simons Observatory cosmology result was found; whether one appeared
  after the searches of 2026-10-07 should be checked before writing about
  SO.
- Forecasts for σ(τ) from LiteBIRD or CLASS and for σ(N_eff), σ(Σm_ν) from
  SO were not read in a cited source and are not quoted.
- The large-angle temperature anomalies (low quadrupole, hemispherical
  asymmetry, cold spot) were not researched here; see
  `cosmo-tensions-anomalies`.
- Modified-recombination and early-dark-energy readings of the CMB–DESI
  discrepancy were seen in abstracts only and are left to the sibling
  skills.
