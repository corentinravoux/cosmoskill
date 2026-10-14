# Weak lensing — open questions, tensions and stale claims

Scope: live controversies in cosmic shear and galaxy–galaxy lensing, with both
sides cited; what the next data decide; claims that still circulate and the
papers that correct them.
Snapshot: 2026-10-12

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. A flag that names a place, as in
`[src: Sect. V.2]`, marks a statement read in the body of the paper.

## 1. Is the S8 tension resolved? Not uniformly
<!-- key: is-the-s8-tension-resolved-not-uniformly -->

The two final Stage-III analyses disagree about it.

- **KiDS-Legacy says yes.** S8 = 0.815 +0.016/−0.021, 0.73σ from Planck
  Legacy; the paper attributes the rise relative to earlier KiDS results
  mainly to improved redshift-distribution estimation and calibration, plus
  new area and improved image reduction (Wright et al. 2025, arXiv:2503.19441)
  [src]. The joint second- and third-order analysis reports "no evidence for
  an S8 tension" (Linke et al. 2026, arXiv:2606.12389) [src].
- **DES Y6 says a mild difference remains.** Cosmic shear alone is 2.0σ (NLA)
  or 2.3σ (TATT) from the combined CMB in S8 (DES Collaboration 2026,
  arXiv:2602.10065) [src]; the 3×2pt is 2.6σ in S8 and 1.8σ in the full
  parameter space, and the combination of all DES probes is 2.8σ from the CMB
  (DES Collaboration 2026, arXiv:2601.14559) [src].
- A 2026 review describes this as a "bifurcation" between DES Y6 (2.4–2.7σ)
  and KiDS-Legacy (<1σ) against a combined-CMB baseline S8 = 0.836
  +0.012/−0.013, and names photometric-redshift calibration,
  intrinsic-alignment modelling and shear pipelines as candidate origins
  (Pantos & Perivolaropoulos 2026, arXiv:2602.12238) [src].

Three facts keep this from being a clean contradiction between the two surveys.

1. The central values are close: 0.815 (KiDS-Legacy), 0.798 (DES Y6 NLA),
   0.804 (HSC Y3 recalibrated, arXiv:2511.18134), 0.805 (DECADE + DES Y3,
   arXiv:2509.03582) [src each]. The difference in quoted tension comes
   largely from the error bars and from the CMB reference: DES compares with
   Planck 2018 + ACT DR6 + SPT-3G DR1, KiDS-Legacy with Planck alone. The
   two references have the same centre and different widths: 0.836
   +0.012/−0.013 for DES (arXiv:2601.14559) [src: Table 4] against 0.834 ±
   0.016 for KiDS-Legacy (arXiv:2503.19441) [src: Sect. 7]. Against Planck
   2018 alone the DES Y6 3×2pt full-parameter difference is 1.0σ, down from
   1.5σ in Y3 (arXiv:2601.14559) [src: Sect. V.2].
2. The DES Y6 number depends on the IA model (0.798 NLA vs 0.783 TATT), and
   the paper says so (arXiv:2602.10065) [src]: the two fiducial posteriors
   differ by 0.6σ, and across all the variants tried the result moves at
   about the 1σ level in the S8–Ωm plane [src: Sect. VII.3.1].
3. A reanalysis of DES Y3 with externally calibrated IA and baryon models
   moves S8 up by 1.5σ to 0.832 +0.013/−0.017 (Bigwood et al. 2025,
   arXiv:2512.04209) [src]; the DES Y3 shear × tSZ analysis gives 0.811
   +0.015/−0.012 (Pandey et al. 2025, arXiv:2506.07432) [src]; the DES Y3 +
   Planck PR4 6×2pt gives 0.8073 ± 0.0094 (Xu et al. 2025, arXiv:2510.25596)
   [src].

A correct one-line statement in October 2026: Stage-III cosmic shear gives S8
between about 0.78 and 0.82 depending on survey and astrophysical modelling,
within about 0.7σ to 2.6σ of the CMB depending on the analysis and on which
CMB combination is the reference; no analysis reaches 3σ on two-point
statistics alone.

Still pulling low: the HSC Y3 two- plus three-point analysis, S8 = 0.736 ±
0.020, 3.2σ from Planck 2018 in the S8–Ωm plane (Sugiyama et al. 2025,
arXiv:2508.14019) [src]; the KiDS-1000 clipped-shear analysis, S8 = 0.724 ±
0.027 in wCDM (Giblin et al. 2026, arXiv:2608.07377) [src]; a tSZ ×
cosmic-shear measurement compared with FLAMINGO that "strongly disfavours" the
Planck S8 independently of feedback strength (Wayland et al. 2026,
arXiv:2609.31774) [src]. The first two use Stage-III data with the older
redshift calibrations.

## 2. Photometric redshifts as the origin of the old low S8
<!-- key: photometric-redshifts-as-the-origin-of-the-old -->

The evidence that redshift calibration, not shear measurement, drove the
earlier low values:

- KiDS-Legacy names redshift estimation and calibration as the main cause of
  its upward shift (arXiv:2503.19441) [src].
- HSC Y3 moves from 0.769 +0.031/−0.034 to 0.804 +0.019/−0.018 when DESI
  clustering redshifts replace the original calibration of the high-redshift
  bins (Choppin de Janvry et al. 2025, arXiv:2511.18134) [src].
- Replacing lensfit by metacalibration on KiDS-1000 leaves S8 at 0.789
  +0.020/−0.024, still 1.8σ from Planck: "it is not caused by the shear
  measurements" (Yoon et al. 2025, arXiv:2510.01122) [src].
- An independent DESI-based recalibration finds differences in the KiDS-1000
  mean redshifts, average shift ΔMean(z) = −0.028 across bins (Blanco et al.
  2025, arXiv:2512.15964) [src], and attributes KiDS-1000 differences to
  photometric-noise mismatch between the COSMOS field and the wide survey
  (Lange et al. 2025, arXiv:2510.25419) [src].

The counter-evidence: the unified DESI calibration states that the new KiDS
n(z) "do not significantly change" the growth estimates from cosmic shear, and
it agrees with the published DES Y3 and HSC Y1 calibrations (arXiv:2510.25419)
[src]. The HSC shear-ratio calibration gives S8 = 0.773 ± 0.031, consistent
with the original HSC Y3 value rather than with the clustering-redshift one
(Rana et al. 2025, arXiv:2508.21681) [src]. So "it was all photo-z" is
supported for KiDS by its own analysis and for HSC by clustering redshifts,
and is not established for DES.

## 3. How strong is baryonic feedback?
<!-- key: how-strong-is-baryonic-feedback -->

- **Strong:** kSZ profiles and X-ray gas fractions; the X-ray baryonification
  analysis finds 6% suppression at k = 1 h/Mpc and 23% at k = 5 h/Mpc and
  calls itself consistent with recent kSZ results "hinting at strong feedback"
  (Bucko et al. 2026, arXiv:2609.09144) [src]. The KiDS-Legacy reconstruction
  of P_m(k,z) finds a 30% ± 10% ± 4% suppression at k = 3–20 h/Mpc (Broxterman
  et al. 2025, arXiv:2509.08365) [src]. DES Y3 shear × tSZ prefers stronger
  suppression than mild-feedback simulations at 2–4σ (arXiv:2506.07432) [src].
- **Weak:** the DES Y3 + Planck PR4 6×2pt analysis with a gas-fraction prior
  on the first baryon principal component finds Q1 = 0.025 +0.024/−0.029 and
  excludes Illustris-like and OWLS-AGN-T8.7-like feedback at 2.9–3.3σ and
  4.7–5.9σ (arXiv:2510.25596) [src]. The KiDS-Legacy BNT k-cut analysis finds
  "no significant bias from nonlinear astrophysical feedback at the precision
  of KiDS-Legacy" (Gu et al. 2026, arXiv:2607.04384) [src], which bounds the
  effect on S8, not the feedback strength. KiDS-Legacy itself bounds
  log₁₀(T_AGN/K) ≤ 7.71 at 68% once the cosmology is fixed to Planck, and
  reads it as little evidence for significant feedback (arXiv:2503.19441)
  [src: Sect. 6]; but the HSC Y3 fit with DESI redshifts puts its HMCode 2016
  amplitude at 2.075 +0.243/−0.128, at the end of its prior [2, 3.13]
  farthest from the dark-matter-only value 3.13 (arXiv:2511.18134) [src:
  Table 1 of the ar5iv rendering].

The dispute matters for Stage IV because the scale-cut strategy saturates:
DECADE finds a residual 0.3σ bias in (S8, Ωm) from current scale cuts and
"negligible improvement" from using all scales with a free baryon model, since
the small scales only self-calibrate the model (arXiv:2509.03582) [src]. A
forecast for LSST finds that with present baryon and redshift-calibration
uncertainty the final-year cosmic-shear constraint "barely improves" on year 1
(Robertson et al. 2026, arXiv:2602.21863) [src, **forecast**]. DES Y6 gives
the size of what is left on the table: with a perfect small-scale model the
S8 error would fall from 0.015 to 0.009, and its cuts would still bias S8 low
by 0.7σ if feedback were as strong as in Illustris (arXiv:2602.10065) [src:
Sect. VI.3, IV.3]. With gas-calibrated priors instead of cuts the DES Y3 blue
sample finds a suppression stronger than FLAMINGO by 2.2σ and BAHAMAS by 1.5σ
at k = 2 h/Mpc (arXiv:2512.04209) [src: Sect. IV].

## 4. NLA or TATT?
<!-- key: nla-or-tatt -->

DES Y6 publishes both and reports that the Bayesian evidence prefers NLA
(arXiv:2602.10065) [src]. In the body the S8 difference is 0.6σ, the evidence
ratio Z_NLA/Z_TATT = 16.9 ± 0.2, "strong" but changing by a factor 2 when the
priors on A₂ and η₂ are scaled by √2, and fifteen model variants span S8 =
0.773 to 0.802 [src: Sect. VII.3.1, Table 4]. DES Y3 had found the model
without alignments weakly preferred (arXiv:2105.13544) [src: Sect. VI.3.2],
and HSC Y3 no significant detection of the amplitude (arXiv:2304.00702) [src:
Sect. V.3.2]. In the DES Y3 + KiDS-1000 joint fit the two surveys' amplitudes
move apart, to −0.02 and 1.04, which the paper takes as a sign that the
parameter may absorb more than alignments (arXiv:2305.17173) [src: Sect.
3.3]. Euclid preparation work
recommends a redshift-dependent TATT ("zTATT") for DR1 3×2pt as the most
flexible choice with constraining power similar to simpler models (Euclid
Collaboration 2026, arXiv:2602.16448) [src, **forecast**-type synthetic
study]. KiDS-Legacy uses neither: it adopts a model tied to halo mass and
spectral type, informed by direct measurements (arXiv:2503.19441) [src]. The
alternative to a more flexible model is a sample with little alignment: DESI
DR1 direct measurements find the bluest galaxies consistent with zero
alignment at 0.05 < z < 0.5 and 0.8 < z < 1.55 (Siegel et al. 2025,
arXiv:2507.11530) [src], and the DES Y3 blue-sample reanalysis exploits this
(arXiv:2512.04209).

## 5. "Lensing is low"
<!-- key: lensing-is-low -->

The claim (Leauthaud et al. 2017, arXiv:1611.08606, from CMASS lenses and 250
deg² of CFHTLenS and CS82 shear) is that galaxy–halo models fitted to BOSS
clustering over-predict the galaxy–galaxy lensing signal at Planck cosmology,
by 20–40% [sec: the range as restated in arXiv:2606.23651], and that lowering
S8 reconciles the two [src]. With DES Y3, HSC Y1 and KiDS-1000 shear around
BOSS, the lensing-to-prediction amplitude was A = 0.79 ± 0.03 (DES + KiDS) and
0.84 ± 0.05 (HSC) at a Planck cosmology with S8 = 0.83, and 0.91 ± 0.04 and
0.97 ± 0.06 at S8 = 0.76; restricted to R > 5.25 h⁻¹Mpc both cosmologies fit
(Amon et al. 2023, arXiv:2202.07440) [src]. A blind cross-survey comparison
concluded that lensing systematics alone are unlikely to explain the effect at
z < 0.54 (Leauthaud et al. 2022, arXiv:2111.13805) [src]. Status in 2026: a
UNIONS × BOSS CMASS measurement over about 2650 deg² does "not find a
significant lensing-is-low effect", while the best joint fits still lower the
matter amplitude slightly relative to Planck, and stresses that large scales
carry the constraint (Campbell et al. 2026, arXiv:2606.23651) [src]. The DESI
DR1 full-scale analysis gives S8 = 0.797 +0.023/−0.024 (DES + KiDS lensing)
and 0.791 +0.020/−0.021 (HSC) with other parameters fixed to CMB values (Lange
et al. 2025, arXiv:2512.15962) [src]. A dynamical-dark-energy background of
the DESI kind would lower the galaxy–galaxy lensing signal by up to 7%
relative to clustering and cosmic shear by 14%, through the distance
dependence of the lensing kernel (Heydenreich et al. 2025, arXiv:2508.05746)
[src].

## 6. Method debates
<!-- key: method-debates -->

- **Statistic.** ξ±, COSEBIs, band powers and pseudo-Cℓ weight scales
  differently; UNIONS finds its configuration- and harmonic-space S8 only
  2.18σ apart on the same catalogue (arXiv:2605.13543) [src], and shows that a
  scale cut defined in one statistic does not map onto another, so null tests
  must pass in all (arXiv:2604.03227) [src].
- **Covariance from data or from theory.** The KiDS-Legacy k-cut analysis
  moves from S8 = 0.798 to 0.717 when the Gaussian covariance term is computed
  from the observed rather than the theoretical data vector (arXiv:2607.04384)
  [src].
- **Scale cuts or modelling.** Two-loop EFT on the scales that survive the
  cuts gives competitive constraints on DES Y3 (Chen et al. 2026,
  arXiv:2603.28761) [src]; baryon models with external priors recover the
  small scales (arXiv:2512.04209).
- **Consistency metrics.** DES Y6 replaces the calibrated posterior-predictive
  tests of Y3 by a Gaussian-mixture PPD metric and warns that tension absorbed
  by nuisance parameters is harder to detect and that projection effects can
  produce spurious tension between disjoint observables (Doux et al. 2026,
  arXiv:2610.03447) [src].

## 7. What the next data decide
<!-- key: what-the-next-data-decide -->

- Euclid DR1 cosmology products: mid-2027 at the earliest (ESA timeline, see
  `surveys-and-data.md`) [src]. Until then every cosmic-shear number is Stage
  III.
- Rubin: survey started 30 June 2026; first shear catalogues appear in data
  previews, not in a cosmology release.
- Roman: launched 30 August 2026, in commissioning.
- Tomographic and 3×2pt UNIONS analyses are announced as next steps
  (arXiv:2605.13543) [src].

## 8. Stale claims and their corrections
<!-- key: stale-claims-and-their-corrections -->

| Claim still seen | Status | Correcting paper |
|---|---|---|
| "Weak lensing is in 2–3σ tension with Planck (S8 ≈ 0.76)." | Superseded for KiDS by KiDS-Legacy (0.815) and for HSC by the DESI recalibration (0.804). | arXiv:2503.19441, arXiv:2511.18134 |
| "The S8 tension is resolved." | Overstated: DES Y6 3×2pt is 2.6σ from the combined CMB in S8. | arXiv:2601.14559 |
| "The low S8 came from shear calibration." | Not supported: metacalibration on KiDS-1000 gives the same S8. | arXiv:2510.01122 |
| "HSC Y3 recalibrated: S8 = 0.805 ± 0.018." | That is the abstract and Table 1 of an earlier version, still served by the ar5iv rendering; the current arXiv abstract gives 0.804 +0.019/−0.018 [src: both read 2026-10-12]. | arXiv:2511.18134 |
| "Euclid DR1 in late 2026 will settle it." | November 2026 is DR1-Foundation only; lensing products follow in mid-2027. | ESA DR1 timeline (15 June 2026) |
| "DES Y3 cosmic shear: S8 = 0.772 +0.018/−0.017" quoted as the DES Y3 result. | That is the ΛCDM-optimised scale-cut variant; the fiducial value is 0.759 +0.025/−0.023. | arXiv:2105.13543 |
| "DES Y3 3×2pt: S8 = 0.779 +0.014/−0.015." | The abstract value is 0.776 ± 0.017; the other figure was not found in any abstract read this session. | arXiv:2105.13549 |
| "Baryons cannot matter for S8 (FLAMINGO)." | True for the 2023 size of the tension; the 2025–2026 values leave a much smaller gap, and gas probes now favour strong feedback. | arXiv:2309.07959, arXiv:2512.04209 |
| "Lensing prefers dynamical dark energy." | Lensing adds little to w0wa; KiDS-Legacy + CMB lensing gives B = 0.07 for w0waCDM. | arXiv:2512.11041, arXiv:2509.03582 |

## Not verified
<!-- key: not-verified -->

- Whether the HSC Y3 third-order result (arXiv:2508.14019) and the KiDS-1000
  clipped-shear result (arXiv:2608.07377) survive the 2025 redshift
  recalibrations: no reanalysis found.
- Why DES Y6 galaxy clustering plus galaxy–galaxy lensing alone gives S8 =
  0.743 ± 0.023 while cosmic shear gives 0.783 (arXiv:2601.14559, Table 4):
  the internal-consistency discussion of that paper was not read.
- Any HSC full-survey (beyond Y3) cosmic-shear cosmology: none found in the
  date-sorted searches.
