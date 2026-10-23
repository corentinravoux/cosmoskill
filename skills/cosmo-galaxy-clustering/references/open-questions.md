# Galaxy clustering — open questions

Scope: live controversies, internal tensions, method debates, what the next
data will decide, forecasts, and stale claims that still circulate.
Snapshot: 2026-10-07.

Flags: `[src]` read this session in the cited paper; `[sec]` from a named
secondary source; `[der]` derived here. Forecasts are labelled.

## 1. Is the DESI BAO–CMB mismatch real, and what does it mean?
<!-- key: is-the-desi-bao-cmb-mismatch-real-and-what-does -->

**The facts.** In flat ΛCDM the DESI DR2 BAO and the CMB disagree at 2.3σ in
the (Ω_m, h r_d) plane, up from 1.9σ in DR1, and at 2.0σ without CMB lensing
[src] (DESI Collaboration 2025, arXiv:2503.14738). DESI is nevertheless
consistent with the CMB acoustic scale θ_* [src]. Opening w0wa absorbs the
mismatch: 3.1σ preference with the CMB, 2.8σ to 4.2σ with supernovae added
[src].

**The collaboration's reading.** "Unless there is an unknown systematic error
associated with one or more datasets", ΛCDM is being challenged and dynamical
dark energy offers a possible solution [src] (arXiv:2503.14738, abstract).

**Critiques from the BAO side.**

- Efstathiou 2025 (arXiv:2505.02658) rotates the BAO distances into
  combinations D_perp and D_par. D_perp is fixed by Planck in ΛCDM, and the
  DR2 values moved into better agreement with Planck ΛCDM than DR1; D_par
  remains consistent. He finds w(z = 0.5) = −0.996 ± 0.046 from DESI BAO +
  CMB, sees no significant evidence for evolving dark energy from Planck +
  DESI BAO, and criticises the statistical methodology [src: abstract].
- Ó Colgáin et al. 2024 (arXiv:2404.08633) traced the DR1 BAO-only preference
  for w0 > −1 to the LRG bin at z_eff = 0.51, which alone implied
  Ω_m = 0.67 (+0.18/−0.17) [src]. For DR2, Ó Colgáin et al. 2025
  (arXiv:2504.04417) find that LRG1 remains the most prominent outlier
  jointly with ELG1, that LRG2 now has the greatest bearing on w0 > −1, and
  that removing any single bin does not restore w0 = −1 within 1σ [src].
- DESI's own checks: the DR2 bins are mutually consistent in ΛCDM (largest
  difference 1.8σ, between LRG1 and LRG3+ELG1; χ²/dof = 10.2/11) [src]
  (arXiv:2503.14738); the unified-tracer reanalysis finds no missed feature
  in 0.8 < z < 1.6 [src] (Sanders et al. 2026, arXiv:2608.27830).

**Critiques from the CMB side.** The mismatch depends on the optical depth:
a τ near 0.09 would reduce the preference for evolving dark energy from about
3σ to about 1.5σ, at the cost of a 3–5σ conflict with Planck low-ℓ
polarisation [src: abstract] (Sailer et al. 2025, arXiv:2504.16932). Detail:
`cosmo-cmb`.

**What the clustering data themselves say when more than BAO is used.**

- DESI DR1 full shape (ShapeFit) + DR2 BAO, no CMB, no supernovae: 1.4σ from
  ΛCDM [src] (Forero-Sánchez et al. 2026, arXiv:2602.18761).
- Adding the LRG bispectrum weakens the evidence in every combination; DESI
  + CMB + DES-Dovekie supernovae gives 3.1σ, "driven primarily by the
  CMB" [src] (Forero-Sánchez et al. 2026, arXiv:2606.23936).
- The Lyα AP measurement gives a higher Ω_m = 0.325 ± 0.018 at z = 2.33 and
  lowers the DESI + CMB preference from 3.1σ to 2.7σ [src] (DESI
  Collaboration 2026, arXiv:2607.27410; the 3.1σ is the DR2 BAO value).
- Simulation-based priors: no statistically significant evidence (2.2σ
  without supernovae, 1.4σ with) [src: abstract] (Chudaykin et al. 2026,
  arXiv:2602.18554).

**Rule of judgment.** The significance of the w0wa preference has not grown
monotonically with added clustering information from the same survey. Quote
it with the exact data combination, and do not describe it as coming from
"DESI" alone: DESI BAO alone is 1.7σ [src] (arXiv:2503.14738). The
interpretation belongs to `cosmo-dark-energy-modified-gravity`; supernova
sample dependence to `cosmo-supernovae`.

## 2. The LRG bins and the SDSS comparison
<!-- key: the-lrg-bins-and-the-sdss-comparison -->

DESI DR1 LRG2 (z = 0.71) gave D_M/r_d = 16.85 ± 0.32 against 17.86 ± 0.33 from
SDSS at z = 0.70, about 3σ for an assumed correlation of 0.21 [src] (DESI
Collaboration 2024, arXiv:2404.03002). DESI suggested an unlucky sample
fluctuation, to be settled by DR2. DR2 gives 17.351 ± 0.177, between the two;
the DESI–SDSS difference is about 2.6σ with the higher correlation (0.57)
that the larger overlap now implies, 2.3σ against DESI's reanalysis of the
SDSS catalogues, and 1.9σ if no correlation is assumed [src]
(arXiv:2503.14738). A global comparison in four matched bins gives a KS
p-value of 0.39 [src].

Status: not a discrepancy by the collaboration's criteria, not entirely gone
either. The honest statement is that the significance depends on an
approximate correlation coefficient. What would settle it: the final DESI
sample, with a still larger effective volume in this bin.

## 3. Prior-volume effects in full-shape analyses
<!-- key: prior-volume-effects-in-full-shape-analyses -->

**Problem.** One-loop EFT fits carry seven nuisance parameters per tracer in
the DESI baseline (three bias, two counterterm, two stochastic) [src]
(arXiv:2411.12021). In ΛCDM with DESI DR1 the effect is small. In w0waCDM it dominates:
Bayesian means and maximum-likelihood values differ by up to 6.6σ for full
shape + BAO without supernovae [src] (Morawetz et al. 2025,
arXiv:2508.11811).

**Positions.**

- Keep full modelling, fix the priors: scale biases with σ8 and drop the
  hexadecapole (Adame et al. 2024, arXiv:2411.12021); use HOD-informed priors
  (Zhang et al. 2025, arXiv:2504.10407), which pull the credible intervals
  back over the baseline posterior maximum.
- Compress: ShapeFit "inherently mitigates" the effect and gives, for the
  first time in a Bayesian framework, reliable DESI-only constraints on
  extensions [src] (arXiv:2602.18761). Counter-argument, from the DR1 key
  paper: compressed parameters in weak bins are themselves affected when
  interpreted with a Gaussian approximation (arXiv:2411.12021).
- Go frequentist (arXiv:2508.11811; for BOSS, Holm et al. 2023,
  arXiv:2309.04468). Counter-argument from the BOSS study: profiles prefer
  extreme values of the EFT parameters, so the two approaches should be shown
  together [src].
- Use simulation-based priors (arXiv:2602.18554): large gains, explicit HOD
  dependence.

**What decides.** Data volume. Simon et al. 2023 (arXiv:2208.05929) and Holm
et al. 2023 both show that the effect shrinks with larger volumes or with CMB
data. DESI DR2 and final full-shape analyses are the test.

## 4. The amplitude from full shape: was σ8 ever low?
<!-- key: the-amplitude-from-full-shape-was-sigma8-ever -->

BOSS EFT analyses gave σ8 = 0.721 ± 0.043 (Ivanov et al. 2020,
arXiv:1909.05277), 0.692 (+0.035/−0.041) with free n_s (Philcox & Ivanov
2022, arXiv:2112.04515) and 0.733 ± 0.047 (Chen et al. 2022,
arXiv:2110.05530), against 0.811 ± 0.006 from Planck (Planck Collaboration
2020, arXiv:1807.06209) [src]. Frequentist reanalysis found no indication of
a BOSS–Planck tension [src] (arXiv:2309.04468). DESI DR1 gives
0.842 ± 0.034 (DESI Collaboration 2024, arXiv:2411.12022), 0.863
(+0.048/−0.040) as a profile-likelihood interval (arXiv:2508.11811), and
0.811 ± 0.030 in an independent P + B analysis (Chudaykin et al. 2025,
arXiv:2507.13433) [src].

Still open: the simulation-based-prior analysis of the same DESI data returns
0.766 ± 0.015, with the shift attributed to quasar HOD assumptions [src]
(arXiv:2602.18554), while the combined-probe analysis from the same group
gives 0.838 ± 0.017 [src] (Ivanov et al. 2026, arXiv:2601.16165). The
amplitude from clustering alone is therefore prior- and model-dependent at
the level of its quoted error. Lensing-side S8: `cosmo-weak-lensing`.

## 5. Mock or analytic covariance at DR2 and beyond
<!-- key: mock-or-analytic-covariance-at-dr2-and-beyond -->

DESI DR1 needed a rescaling of the EZmock covariance because fast fibre
assignment in mocks underestimates the errors, and found the Fourier-space
analytic covariance inadequate for full shape (Forero-Sánchez et al. 2024,
arXiv:2411.12027). For BAO the semi-analytic 2PCF covariance is already the
baseline (Rashkovetskyi et al. 2024, arXiv:2404.03007). The direction of
travel is analytic or hybrid: the pre/post-reconstruction cross-covariance
can be approximated analytically (Maus et al. 2026, arXiv:2602.12343), and
Euclid validated a semi-analytic estimator usable with only eight mocks
(Euclid Collaboration: Sarpa et al. 2026, arXiv:2605.03446). Open: analytic
covariance for the power spectrum with realistic fibre assignment, and for
the bispectrum.

## 6. Fibre assignment at small scales
<!-- key: fibre-assignment-at-small-scales -->

The θ-cut throws away pairs below 0.05° and with them small-scale
information; PIP weights recover it but need many alternative assignment
realisations and non-zero pair probabilities (Bianchi et al. 2024,
arXiv:2411.12025; Pinon et al. 2024, arXiv:2406.04804). Whether DESI DR2
full-shape fits use PIP weights is not known at the snapshot.

## 7. f_NL from scale-dependent bias
<!-- key: fnl-from-scale-dependent-bias -->

- **The b_φ problem.** Constraints are on f_NL b_φ; marginalising over b_φ
  with wide priors is not conservative and biases the result [src] (Barreira
  2022, arXiv:2205.05673). DESI numbers move from −3.6 to +3.5 with the QSO
  assumption alone [src] (Chaussidon et al. 2024, arXiv:2411.17623). A
  simulation-based prior gives mean p ≈ 1.4 for DESI-like quasars [src]
  (Fondi et al. 2026, arXiv:2602.12357).
- **Imaging systematics** set the floor on the largest scales
  (`systematics.md` Sect. 5).
- **Two-point versus bispectrum.** The DESI DR1 P + B analysis quotes
  f_NL = −0.1 ± 7.4, tighter than the scale-dependent-bias result
  (σ ≈ 9), and −0.0 ± 4.1 with the CMB [src: abstract] (Chudaykin et al. 2025,
  arXiv:2512.04266). It is an independent analysis; no collaboration
  bispectrum f_NL result was found.
- **Next.** DESI DR2 and final samples; SPHEREx all-sky low-resolution
  redshifts (Bock et al. 2025, arXiv:2511.02985). No forecast number was read
  this session.

Full treatment: `cosmo-inflation-primordial`.

## 8. Under-used data
<!-- key: under-used-data -->

- BGS: the DR2 BAO analysis uses 1.19 million of more than 9.1 million BGS
  redshifts at 0.1 < z < 0.4, because the pipeline assumes a roughly constant
  clustering amplitude; using all would add about 20% of effective volume
  [src] (arXiv:2503.14738).
- Hexadecapole and k > 0.20 h Mpc⁻¹ are excluded from the DESI DR1 baseline
  [src] (arXiv:2411.12021).
- Higher-order statistics: the bispectrum is used so far only by supporting
  or independent analyses (arXiv:2606.23936; arXiv:2507.13433; Guandalin et
  al. 2026, arXiv:2610.01836). Detail: `cosmo-beyond-two-point`.

## 9. Reconstruction beyond the standard algorithm
<!-- key: reconstruction-beyond-the-standard-algorithm -->

Field-level and neural reconstructions promise 26% to 35% tighter BAO
parameters on DESI-like LRG mocks (**mock result**, Bayer et al. 2026,
arXiv:2603.15732). Open: robustness to survey systematics, covariance, and
blinding of a forward-model reconstruction. No cosmological result from data
with these methods was verified this session.

## 10. H0 from clustering, with and without r_d
<!-- key: h0-from-clustering-with-and-without-rd -->

BAO + BBN gives 68.51 ± 0.58 km/s/Mpc, 4.5σ from SH0ES, and assumes standard
pre-recombination physics [src] (arXiv:2503.14738). The sound-horizon-free
route through the equality scale gives 69.2 to 70.3 with errors of 1.2 to 1.8
[src] (Zaborowski et al. 2025, arXiv:2510.19149), consistent with the
r_d-based value. Agreement between the two routes is the clustering test of
early-universe modifications of r_d. Detail: `cosmo-distance-ladder-h0`.

## 11. What the next data will decide
<!-- key: what-the-next-data-will-decide -->

| Data | When | Decides |
|---|---|---|
| DESI DR2 galaxy full shape | not announced; "further papers" in 2026 per the April 2026 release [src] | prior-volume effects at 2–3 times the DR1 volume; fσ8(z); w0wa from clustering alone |
| DESI full five-year BAO | 2027 [src] | the LRG bins; BAO–CMB mismatch at final precision |
| Euclid DR1 clustering products | mid-2027 [src] | independent BAO and RSD at 0.9 < z < 1.8 with slitless systematics |
| PFS, 4MOST CRS | no result yet | z > 1.6 ELG clustering; southern overlap with Rubin and Euclid |
| SPHEREx | during the two-year survey | f_NL from all-sky low-resolution redshifts |
| Roman | after commissioning | dense Hα clustering at z = 1–2 |

**Forecasts** read this session:

- Euclid BAO only, four redshift bins of DR1-like mocks: about 10% on Ω_m
  and 3% on H0 r_s (**forecast** on mocks, arXiv:2605.03446) [src].
- PFS: 3% distances in six bins, 6% growth (**forecast**, 2014 design;
  Takada et al. 2014, arXiv:1206.0737) [src].
- Roman reference survey: 10 million Hα and 2 million [O III] redshifts
  (**forecast**, Wang et al. 2022, arXiv:2110.01829) [src].
- Euclid Fisher forecasts for clustering and lensing: Euclid Collaboration:
  Blanchard et al. 2020, arXiv:1910.09273 (**forecast**; numbers not read).

## 12. Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

1. **"DESI measures H0."** BAO measure D/r_d. H0 needs an r_d calibration
   (arXiv:2404.03002).
2. **"DESI alone prefers dynamical dark energy at 3–4σ."** DESI DR2 BAO alone:
   1.7σ; the 3.1σ needs the CMB and the 4.2σ needs DESY5 supernovae
   (arXiv:2503.14738).
3. **"The DESI BAO–CMB tension is about 3σ."** It is 2.3σ in ΛCDM
   (arXiv:2503.14738); the Lyα AP update quotes 2.4σ before and 2.2σ after
   (arXiv:2607.27410).
4. **"Full-shape analyses find low σ8."** True of BOSS EFT posteriors, not of
   DESI DR1 (Sect. 4).
5. **"DESI DR2 full shape shows …"** There is no DR2 galaxy full-shape
   measurement as of the snapshot. Papers titled "DR1 full shape + DR2 BAO"
   combine releases (arXiv:2602.18761).
6. **"The DR1 fσ8 points can be fitted directly."** They are fσ_s8 converted
   under r_d = r_d^fid, for visualisation only (arXiv:2411.12021).
7. **"The LRG point at z = 0.51 drives everything."** It drove the DR1
   BAO-only w0 > −1 preference (arXiv:2404.08633). In DR2 no single bin does
   (arXiv:2504.04417).
8. **"SDSS and DESI disagree at 3σ at z = 0.7."** That was DR1. DR2: about
   2.6σ, or 2.3σ against the DESI reanalysis of SDSS (arXiv:2503.14738).
9. **"DESI LSS f_NL is now better than Planck."** The scale-dependent-bias
   result has σ ≈ 9 against 5.1 for Planck (Planck Collaboration 2020,
   arXiv:1905.05697); the −0.1 ± 7.4 figure is an independent P + B analysis
   (arXiv:2512.04266).
10. **"Systematics dominate DESI BAO."** The systematic term raises the total
    α_iso error by at most 9% (arXiv:2503.14738).
11. **Abstract of arXiv:2602.18761.** It prints w0 = 0.49; the paper's table
    gives −0.49.
12. **Quoting the eBOSS "final" BAO compilation as current.** DESI DR2 bins
    now exceed the SDSS ones in effective volume at every matched redshift
    and DESI no longer combines with them (arXiv:2503.14738).
13. **"Reconstruction is model-independent."** It assumes a fiducial bias,
    growth rate and distance–redshift relation; the dependence is tested and
    small, not absent (Pérez-Fernández et al. 2024, arXiv:2406.06085).
14. **Euclid DR1 "in October 2026".** The dated ESA timeline gives
    November 2026 for DR1-Foundation and mid-2027 for the clustering
    products (see `surveys-and-data.md`).

## Not verified
<!-- key: not-verified -->

- Whether DESI DR2 full-shape fits will use PIP weights, the hexadecapole or
  a higher k_max.
- SPHEREx and DESI final f_NL forecasts (no number read).
- Any claim about a DESI DR3 data set: no DR3 material was found; the public
  statements refer to "the full five-year data set" with results in 2027.
- Independent reanalyses of DESI DR2 BAO at catalogue level: not possible
  until the DR2 catalogues are public.
