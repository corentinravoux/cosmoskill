# Tensions and anomalies — mundane explanations on the table

Scope: for each tension or anomaly, the mundane explanations and the paper that quantifies each.

Snapshot: 2026-10-07

Flags as in `results.md`: `[src]` read this session in the cited paper; `[sec: X]` taken from the reference files of sibling skill X (abbreviations at the top of `results.md`); `[der]` derived here. Where a row says "ID in sibling", the paper is cited with its arXiv ID in that sibling's files and is not in this skill's `sources.tsv`.

"Mundane" means: an explanation that leaves ΛCDM untouched — a systematic in one data set, an astrophysical nuisance, a statistical choice, or chance. Each row gives the mechanism, the size where a paper quantifies it, and the verdict at the snapshot: **closed** (tested and excluded as the explanation), **open** (quantified, not excluded), or **operative** (shown to have moved the number).

## 1. H0

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Crowding of Cepheids in HST photometry | HST − JWST distance difference −0.01 ± 0.03 mag; crowding as the cause rejected at 8.2σ | closed | Riess et al. 2024, ID in sibling; no bias in 19 JWST hosts, arXiv:2509.01667 | [sec: h0] |
| Calibrator subsample and supernova compilation | CCHP TRGB 70.39 (total error 1.94) against 72.1 to 73.3 ± 1.8 for the complete 35-calibrator TRGB sample; the stellar distances of the two teams agree at about 0.03 mag | open; the gap is in which SNe calibrate, not in the stars | arXiv:2408.06153; Li et al. 2025, ID in sibling | [sec: h0] |
| Implicit flat priors on distance moduli | 70.6 ± 1.0 with uniform-in-volume priors and a wider Gaia offset prior | closed for the Milky Way step: without a selection function the model mis-predicts the observed parallax, magnitude and period distributions; with it the SH0ES calibration is recovered within 0.5σ | arXiv:2601.22215; arXiv:2603.09880 | [sec: h0] |
| Selection of Cepheids and SNe in calibrator galaxies | shifts of −1.4, −0.2 and −1.0 km/s/Mpc from three selection terms | open | Percival 2026, ID in sibling | [sec: h0] |
| A single geometric anchor for the JWST ladders | both JWST ladders rest on NGC 4258; with NGC 4258 anchoring both telescopes SH0ES gets 72.85 ± 1.30 | open until a second JWST anchor exists | arXiv:2509.01667 | [sec: h0] |
| Local void or outflow | the SN Hubble diagram at 0.023 < z < 0.15 excludes density contrasts above 27% on scales > 69 Mpc/h at 5σ; void profiles fitted to Cosmicflows-4 distances prefer a void smaller than 70 Mpc, under 10% of the size required | closed as the main cause | Kenworthy, Scolnic & Riess 2019, arXiv:1901.08681; Stiskalek, Desmond & Banik 2025, arXiv:2506.10518 | [sec: h0] |
| Local density from constrained simulations | about 5% underdensity within 200 Mpc in one reconstruction, "no evidence for a large local underdensity" in another | closed: neither approaches the required size | SIBELIUS-DARK and Manticore-Local, IDs in `cosmo-simulations-mocks` | [sec: sims] |
| Lens mass profile (mass-sheet degeneracy) | 73.3 (+1.7/−1.8) with assumed profiles becomes 71.6 (+3.9/−3.3) with the degeneracy free | operative: lensing no longer discriminates | arXiv:2506.03023 | [sec: h0] |
| Peculiar velocities of megamaser hosts | 73.9 ± 3.0 without flow correction; 66.9 to 68.8 or 71.6 ± 3.7 in two 2026 reanalyses | operative and unresolved | IDs in sibling | [sec: h0] |
| A Planck-specific systematic | SPT-3G D1 alone gives 66.66 ± 0.60; DESI DR2 BAO + BBN gives 68.51 ± 0.58 with no CMB anisotropies | closed | arXiv:2506.20707; arXiv:2503.14738 | [sec: h0, cmb] |
| Underestimated errors in general | treating the scatter of 163 published values (1976–2019) as the true error distribution turns a nominal 4.4σ into 2.1σ | a sociological argument, not a measurement | Lopez-Corredoira 2024, ID in sibling | [sec: h0] |
| Supernova systematics moving the inverse ladder | known systematics shift it by less than 0.1 km/s/Mpc | closed | Popovic & Sullivan 2026, ID in sibling | [sec: h0] |

The gap to close is 0.176 ± 0.035 mag (arXiv:2112.04510) [sec: h0]. No single quantified systematic above reaches half of it; the open rows (calibrator selection, extragalactic selection, single anchor) are the ones a referee should ask about.

## 2. S8

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Source redshift calibration | KiDS: 0.759 to 0.815, attributed mainly to redshift estimation and calibration; HSC Y3: 0.769 to 0.804 with DESI clustering redshifts | operative; the main driver of the old low values | arXiv:2503.19441; arXiv:2511.18134 | [sec: wl] |
| Shear calibration | replacing lensfit by metacalibration on KiDS-1000 leaves S8 unchanged (0.789) | closed | Yoon et al. 2025, ID in sibling | [sec: wl] |
| Intrinsic-alignment model | 0.798 (NLA) against 0.783 (TATT) on the same DES Y6 data; the choice of IA and baryon model moves S8 by up to 1σ | open | arXiv:2602.10065 | [sec: wl] |
| IA and baryon priors from external data | DES Y3 moves to 0.832 (+0.013/−0.017), up by 1.5σ, with IA priors from spectroscopic measurements and a baryon model informed by X-ray and kSZ data | open; not adopted by the collaboration | Bigwood et al. 2025, arXiv:2512.04209 | [sec: wl] |
| Baryonic feedback strength | disputed: kSZ, X-ray, tSZ and the KiDS P(k) favour strong suppression, DES Y3 6×2pt weak | open | IDs in `cosmo-weak-lensing`, `cosmo-cmb-lss-cross-correlations` | [sec: wl, x] |
| Projection (prior-volume) effects on the point estimate | mean 0.790 against MAP 0.801 in DES Y3 + KiDS-1000 | operative at the half-σ level | ID in sibling | [sec: wl] |
| The CMB reference | Planck S8 0.834 ± 0.016 (PR3) to 0.819 ± 0.014 (PR4); four endpoints in use | operative | arXiv:2309.10034 | [sec: cmb] |
| Metric and subspace | DES Y6 3×2pt: 2.6σ in S8, 1.8σ in full space | operative | arXiv:2601.14559 | [sec: wl] |
| Lensing-map normalisation and redshifts in CMB-lensing tomography | unWISE: +0.6σ from the lensing normalisation and +0.8σ from redshifts; unmitigated foregrounds would bias κ × unWISE by −4.2σ | operative | arXiv:2309.05659 | [sec: x] |
| Neutrino treatment and projection effects in the LRG analysis | +0.017 and +0.014 in S8 | operative | arXiv:2407.04607 | [sec: x] |
| Cluster mass calibration | Planck clusters 3.7σ to 1.6σ with DES shear (arXiv:2509.02068); hydrostatic-bias values depend on the reference, 0.89 against Chandra and 0.76 against XMM with the same lensing (ID in `cosmo-clusters`) | operative | arXiv:2509.02068 | [sec: cl] |
| Selection and projection in optical clusters | richness selection biases stacked lensing high by 20–60% on large scales; DES Y1 clusters gave 0.65 ± 0.04, attributed by the collaboration to lensing-model systematics | operative | IDs in `cosmo-clusters` | [sec: cl] |
| The gas model in tSZ cross-correlations | the same y × galaxy data are fitted with one simulation suite, and ⟨b P_e⟩ scales as about S8³, so a gas-model error of 10% in pressure maps to about 3% in S8 [der: 1/3 of the fractional error, from the quoted scaling] | open | arXiv:2605.11083 | [sec: x] |
| Prior volume in full-shape fits | BOSS EFT σ8 = 0.69–0.73 against DESI DR1 0.842 ± 0.034; frequentist intervals show no BOSS tension | operative | IDs in `cosmo-galaxy-clustering`, `cosmo-statistics-inference` | [sec] |

The high eRASS1 value (0.86 ± 0.01) is the one S8 number for which no mundane downward correction has been published; its companion result, a growth index of 1.19 ± 0.21, shows that the same data prefer less low-redshift growth when given the freedom [sec: cl].

## 3. A_L, tau and the CMB-BAO discrepancy

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| A_L: a feature of Planck TT at ℓ ≈ 1100–2000, statistical or systematic | Plik PR3 1.180 ± 0.065; CamSpec PR4 1.095 ± 0.056; HiLLiPoP PR4 1.039 ± 0.052; ACT DR6 1.007 ± 0.057; SPT + ACT 1.016 (+0.048/−0.054) | operative; ground data do not show the residual | arXiv:1807.06209; arXiv:2309.10034; arXiv:2503.14452; arXiv:2506.20707 | [sec: cmb] |
| A_L: real excess lensing | excluded by the reconstructions: the smoothing is 2σ high relative to the Planck reconstruction (arXiv:1912.06601); the ACT + SPT + Planck reconstruction amplitude is 1.025 ± 0.017 (Qu et al. 2025, ID in `cosmo-cmb`); the SPT-3G D1 amplitude is unity at 2% (arXiv:2608.31136) | closed | arXiv:1912.06601; arXiv:2608.31136 | [sec: cmb] |
| τ: a systematic in Planck low-ℓ EE | five reprocessings give 0.051–0.063; ground-based CLASS × Planck gives 0.053 (+0.018/−0.019), too wide to exclude 0.09 at more than about 2σ [der, sec: cmb] | open but disfavoured; "no evidence for systematics in the large-scale Planck data" by the authors who raised the question | arXiv:2504.16932 | [sec: cmb] |
| τ: reionisation astrophysics | Planck without low-ℓ EE + reionisation history gives 0.0552 with errors of a few 10⁻³, leaving a 2.4σ tension with DESI DR2 | closes the high-τ door from the astrophysical side | arXiv:2601.09644 | [sec: cmb] |
| CMB–BAO: choice of CMB data | 1.6σ (P-ACT) to 3.7σ (SPT + ACT) | operative; no preferred choice | arXiv:2503.14452; arXiv:2506.20707 | [sec: cmb] |
| CMB–BAO: BAO systematics | systematics add at most 9% to the isotropic BAO error in DESI DR2 | closed at the current precision | arXiv:2503.14738 | [sec: `cosmo-galaxy-clustering`] |
| CMB–BAO: lensing reconstruction | with the 2026 SPT-3G D1 lensing the curvature and w0wa preferences from CMB + DESI fall to about 2σ | operative | arXiv:2608.31136 | [sec: cmb] |
| CMB–BAO: chance | a 2–3σ difference between two data sets in one model | open; the simplest reading | — | — |

## 4. w0wa preference

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Supernova photometric calibration and a colour-law implementation error | DES: 4.2σ to 3.2σ | operative | arXiv:2511.07517 | [sec: de] |
| Inconsistent host masses between low and high redshift | Pantheon+ 2.8σ to 3.2σ; Union3 3.8σ to 3.4σ | operative; moves samples towards each other | arXiv:2601.19424 | [sec: de] |
| Heterogeneous low-redshift anchor | cutting z < 0.1 moves Unite by about 2σ; an intercept offset between low-z and DES supernovae reduces the preference "to be less than 2σ" in one external analysis | open | arXiv:2609.05053; external analyses, IDs in sibling | [sec: de] |
| Non-independence of the compilations | the samples share most low-redshift supernovae | operative; three samples are not three confirmations | — | [sec: de] |
| A ΛCDM inconsistency between data sets absorbed by two parameters | DESI DR2 against DES-SN5YR in ΛCDM: 2.95 ± 0.04σ, reduced to 1.96 ± 0.04σ with DES-Dovekie; ln B falls from +3.32 ± 0.27 to −0.30 ± 0.19 | operative in that analysis | arXiv:2511.10631 | [sec: stat] |
| CMB lensing and τ | compressed CMB priors give 2.4σ, the full CMB 3.1σ; τ ≈ 0.09 would leave about 1.5σ | open | arXiv:2503.14738; arXiv:2504.16932 | [sec: de] |
| Statistic | 2.8σ and ln B = −0.66 ± 0.44 for the same DESI DR2 + CMB + Pantheon+ data | operative | arXiv:2503.14743 | [sec: de] |
| Clustering beyond BAO | the DESI DR1 bispectrum weakens the preference; DESI only is within 1σ of Λ | operative | arXiv:2606.23936 | [sec: de] |
| Parameterisation | phantom crossing is preferred within CPL; 3.2% of non-crossing mocks imitate it | open | ID in sibling | [sec: de] |
| Repeated looks at accumulating data | Wilks-based σ read as if the test were done once | open | ID in sibling | [sec: de] |

## 5. Cosmic dipole

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Redshift evolution of the source population (spectral index, magnification bias, luminosity function) | the standard expression "may be inaccurate"; luminosity-function models consistent with the data give dipoles that "can disagree by more than 3σ" | disputed: the reply is that the test is "robust to such effects" | Dalang & Bonvin 2022, arXiv:2111.03616; Guandalin et al. 2023 (abstract read, not in `sources.tsv`); von Hausegger 2024, arXiv:2404.07929 | [src] |
| Clustering dipole of the sources and mode coupling from the mask | 4.9σ becomes 3.63σ (no clustering dipole in the mocks), 3.44σ (random orientation) or 3.27σ (aligned); including an octupole in the fit shifts the dipole and inflates its variance | open; reduces, does not remove | Bashir, Chingangbam & Appleby 2025, arXiv:2511.00822 | [src] |
| Same, as assessed by the discovering group | after the ecliptic-latitude trend is removed, other large-scale power is consistent with noise, no octupole, clustering dipole "marginal" | disputed | von Hausegger et al. 2025, arXiv:2510.23769 | [src] |
| Mask leakage | the Galactic mask moves dipole power to higher multipoles, which makes the discrepancy worse, not better | closed as an explanation | arXiv:2212.07733 | [src] |
| Survey-specific count gradient (ecliptic latitude in CatWISE) | a "known trend of the quasar number counts with ecliptic latitude", accounted for before the multipole analysis | open as to completeness of the correction | arXiv:2510.23769 | [src] |
| Multi-component radio sources (overdispersed counts) | modelled with a negative-binomial likelihood; the excess remains at 3.67 ± 0.49 times the expectation | closed as an explanation | Böhme et al. 2025, arXiv:2509.16732 | [src] |
| Frequency-dependent systematics in radio catalogues | amplitude rising towards low frequency in one four-survey analysis; no frequency dependence in another | open | arXiv:2010.08366; arXiv:2206.05624 | [src] |
| Eddington bias at the flux limit | forward-modelling it raises the CatWISE–Planck tension from ≈ 5.7σ to ≈ 6.7σ | closed as an explanation | Land-Strykowski et al. 2026, arXiv:2607.25703 | [src] |
| Footprint incompleteness and leakage of large-scale power | the DESI DR1 count dipole is enhanced while the redshift dipole of the same quasars gives 358 (+55/−48) km/s | open; shows that a count excess can coexist with a normal velocity in one catalogue | Wu & Xia 2026, arXiv:2608.30914 | [src] |
| A real flow of the sources | excluded at the amplitude needed: kSZ limits at 200–2000 h⁻¹Mpc are consistent with ΛCDM | closed for a ~370 km/s flow at R ~ 1000 h⁻¹Mpc | arXiv:2605.12499 | [sec: pv] |
| Model-dependent residual | with the kinematic part fixed, the residual points 39° ± 8° away from the CMB dipole | suggests a non-kinematic component with its own direction, as expected for a systematic or a clustering term as much as for new physics [the reading is this file's, not the paper's] | arXiv:2503.02470 | [src] |

What stays unexplained: two populations with no shared objects (radio galaxies and infrared quasars) both exceed the expectation, with directions near the CMB dipole (arXiv:2206.05624) [src]. What weakens the case: the quoted significance of the single strongest catalogue ranges from 3.3σ to 6.7σ with the null model, and the two measurements that determine the velocity without counting sources agree with 370 km/s.

## 6. Large-angle CMB anomalies

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| A posteriori selection of statistics | the joint ≤ 3 × 10⁻⁸ becomes 3σ for about 16 tests considered and 2σ for about 50 | operative; the authors list that many published tests | Guth & Namjoo 2026, arXiv:2602.10178 | [src] |
| Non-independence of the statistics | hemispherical-asymmetry and dipole-modulation statistics "cannot be considered to be independent of each other" | operative | arXiv:1906.02552 | [src] |
| Chance, tested with polarisation | about a 30% chance that a p-value dip deepens when isotropic polarisation is added; no polarisation counterpart found | open; Planck polarisation is not sensitive enough | arXiv:1906.02552 | [src] |
| Instrumental or processing artefact | present in WMAP and Planck and in PR3 and PR4; the lack-of-power probability does change with release (≤ 0.33% to ≤ 1.76%) | closed for the existence of the features, open for the exact p-values | arXiv:1510.07929; arXiv:2312.09989; arXiv:2406.11543 | [src] |
| Secondary anisotropies from the local Universe | thermal and kinetic SZ from a constrained simulation of the local 500 h⁻¹Mpc box have negligible impact on lack of correlation, quadrupole–octopole alignment and hemispherical asymmetry | closed | Jung et al. 2024, arXiv:2406.11543 | [src] |
| Cold Spot: a supervoid along the line of sight | the Planck lensing signal disfavours a void large enough, with odds 1:13 to 1:20 | closed | Owusu et al. 2023, arXiv:2211.16139 | [src] |
| Cold Spot: the Eridanus supervoid through ΛCDM ISW | accounts for about 10–20% of the temperature depression | closed as the full explanation | Kovács et al. 2022 (abstract read, not in `sources.tsv`) | [src] |
| Mask and component separation | p-values quoted as upper bounds over four component-separated maps | operative at the factor-of-few level in p | arXiv:2312.09989 | [src] |

The mundane explanation that cannot be excluded is cosmic variance: one sky, a handful of modes, statistics chosen after the fact. The only new information can come from large-angle polarisation and from three-dimensional tracers of the same modes.

## 7. Bulk flow

All rows [sec: pv]; IDs for papers not listed in `results.md` §8 are in `cosmo-peculiar-velocities`.

| Explanation | Size | Verdict |
|---|---|---|
| Analytic minimum-variance errors underestimate the uncertainty | CF4 at 150–200 h⁻¹Mpc: errors of 28–36 km/s analytic against 108 km/s from mocks; probability 0.00021% to 0.11% | operative (arXiv:2302.02028; arXiv:2306.11269) |
| Window: an ideal sphere reconstructed from a sparse, anisotropic catalogue | full-range deviation 2.3σ when the ΛCDM prediction is computed for the actual positions and covariances | operative (arXiv:2608.14265) |
| One sub-catalogue: 6dFGS Fundamental Plane | peak-bin deviation 3.40σ, 1.56σ without 6dFGS | open (arXiv:2608.14265) |
| Zero-point (monopole) error leaking into the dipole | a zero-point dipole of 0.087 ± 0.019 mag in CF4 Tully–Fisher is better described by local flow structure | operative (arXiv:2509.14997) |
| Neglected relativistic terms of order vz | bias "toward larger values by ~10%" | operative, small |

## 8. JWST abundance

| Explanation | Size | Verdict | Quantifying paper | Flag |
|---|---|---|---|---|
| Photometric redshifts and masses of the first candidates | the 2022 claim was conditional: "if verified with spectroscopy" | operative: the spectroscopic FRESCO sample shows "no tension with the ΛCDM model" | arXiv:2207.12446; arXiv:2309.02492 | [src] |
| Slitless-grism redshift contamination | one of three ultra-massive objects moves from z = 5.58 to 3.2439 and from an extreme efficiency to log M_* ~ 10.6 | operative for that object | Xiao et al. 2026, arXiv:2602.03030 | [src] |
| AGN light, dust, and the lack of rest-frame near-infrared (MIRI) constraints in the stellar masses | named as the likely drivers of "earlier claims of insufficient stellar masses at z = 8" | operative according to that model comparison | Prada et al. 2026, arXiv:2604.18683 | [src] |
| Star-formation efficiency higher at early times | 2–3% of baryons converted by z = 10–12 suffices for the UV luminosity functions at 7 ≤ z ≤ 14; the three ultra-massive FRESCO galaxies would need about 50% | open as galaxy-formation physics, not as cosmology | arXiv:2604.18683; arXiv:2309.02492 | [src] |
| Cosmic variance of small fields, initial mass function, bursty star formation | not quantified in the papers read | open | — | — |

## 9. Tension-metric pitfalls

Worked cases. Each row is one data situation where two defensible computations give different answers.

| Pitfall | Case | The two numbers | Source | Flag |
|---|---|---|---|---|
| Unnamed reference endpoint | H0, H0DN 2025 | 5.0σ against DESI DR2 + BBN; 7.1σ against Planck + SPT + ACT | arXiv:2510.23823 | [sec: h0] |
| Unnamed reference endpoint | CMB against DESI DR2 in ΛCDM | 1.6σ (P-ACT), 2.3σ (DESI's CMB), 2.8σ (CMB-SPA), 3.7σ (SPT + ACT) | arXiv:2503.14452; arXiv:2503.14738; arXiv:2506.20707 | [sec: cmb] |
| Projection on the most discrepant parameter | DES Y6 3×2pt against the CMB | 2.6σ in S8; 1.8σ in the full shared space | arXiv:2601.14559 | [sec: wl, stat] |
| Choosing the data combination after the fact | LSS against Planck 2015 | 2.55σ for the most discrepant combination; 0.76σ for the most concordant | Charnock, Battye & Moss 2017, arXiv:1703.05959 | [sec: stat] |
| Prior-volume dependence of the evidence ratio | two equal Gaussians 3σ apart | R << 1 with a flat prior on [−10, 10]; R > 1 with [−200, 200] | Lemos et al. 2021, arXiv:2012.09554 | [sec: stat] |
| Frequentist preference against Bayesian evidence | DESI DR2 + CMB + Pantheon+ | 2.8σ for w0wa; ln B = −0.66 ± 0.44, mildly for Λ | arXiv:2503.14743 | [sec: de] |
| Two evidence calculations on nominally the same data | DESI DR2 + CMB + DES-Dovekie | odds about 5:1 for w0wa; ln B = −0.30 ± 0.19 | arXiv:2511.07517; arXiv:2511.10631 | [sec: de, stat] |
| Combining data sets that disagree in the base model | DESI DR2 + DES-SN5YR | a 2.95σ ΛCDM tension between them is what the two extra parameters absorb | arXiv:2511.10631 | [sec: stat] |
| Counting correlated data as independent | three supernova compilations with a common low-z sample | 2.8, 3.8, 4.2σ before two fixes; 3.2, 3.4, 3.4σ after | arXiv:2503.14738; arXiv:2601.19424 | [sec: de] |
| Local significance without a trial factor | four CMB anomaly statistics | joint p ≤ 3 × 10⁻⁸ (above 5σ); 3σ if chosen from 16 tests, 2σ from 50 | arXiv:2310.12859; arXiv:2602.10178 | [src] |
| Null model without the nuisance signal | CatWISE dipole | 4.9σ against mocks with shot noise and the kinematic dipole; 3.27–3.63σ against mocks with clustering, radial selection and the exact mask | arXiv:2009.14826; arXiv:2511.00822 | [src] |
| Analytic errors against mock-calibrated errors | CF4 bulk flow | probability 0.00021%; 0.11% | arXiv:2302.02028; arXiv:2306.11269 | [sec: pv] |
| Mock covariance that lacks the data's higher-order moments | parity-odd 4PCF in BOSS | 7.1σ against Patchy mocks; 0–2.5σ with statistics free of the 8PCF bias | arXiv:2206.03625; arXiv:2407.03397 | [sec: b2p] |
| One-sided against two-sided conversion | CatWISE dipole | p = 5 × 10⁻⁷ is 4.9σ one-sided; the two-sided equivalent of the same p is 5.0σ [der: two-sided Gaussian tail] | arXiv:2009.14826 | [src] |
| Posterior width at a physical boundary read as sensitivity | Σm_ν from DESI DR2 + CMB | σ = 0.020 eV (truncated posterior) against 0.053 eV (effective signed mass) | arXiv:2503.14744 | [sec: nu] |
| Bayesian limit against profile likelihood in a model with a parameter that vanishes at the ΛCDM point | early dark energy | f_EDE < 0.070 at 95% (posterior, SPT + ACT + Planck); f_EDE = 0.09 ± 0.03 and H0 = 71.0 ± 1.1 (profile, ACT DR6 + DESI DR2) | Khalife et al. 2025, arXiv:2507.23355; Poulin et al. 2025, arXiv:2505.08051 | [sec: h0] |
| Comparing the wrong quantity | ladder against CMB + BAO + SN | the H0 World Cup quotes the ΛCDM discrepancy in M_B (above 5.5σ), not in H0 | arXiv:2607.13283 | [src] |

General rules are in `physics-and-methods.md` §1.3; the statistical theory is in `cosmo-statistics-inference`.

## 10. What a referee checks

For any sentence of the form "X is in n σ tension with Y":

1. Are both data sets, with release and likelihood, named? (Planck PR3 or PR4; P-ACT or CMB-SPA; DESI DR1 or DR2; which supernova sample and calibration.)
2. Is the model stated? Every number in `results.md` is a ΛCDM statement unless marked.
3. Is the metric stated, and is it a tension between data sets or a preference between models?
4. Is it projected on one parameter or computed in the shared space? Was the parameter chosen before looking?
5. Are the two data sets independent? Check anchors, calibration, τ prior, shared supernovae, shared sky, shared mocks.
6. Is the value current? Check `results.md` §12 for what superseded it.
7. For an anomaly: was the statistic defined before the data; how many comparable statistics were tried; were the simulations of the null realistic (clustering, mask, selection, noise)?
8. For a combined constraint in an extended model: were the data sets consistent in ΛCDM before being combined, and does the extension do anything other than absorb that inconsistency?
9. Is a mundane explanation that moved the number in the past (redshift calibration, mass calibration, supernova calibration, mock realism, mass-sheet degeneracy) addressed for the new claim?
10. For a proposed resolution: does it survive BAO (Ω_m), uncalibrated supernovae (shape), ACT DR6 (damping tail), S8 and BBN at once (`open-questions.md` §2)?

## Not verified

- Galactic extinction, stellar contamination and photometric zero-point gradients as explanations of the CatWISE dipole: not covered by the abstracts read; the Colloquium review (arXiv:2505.23526) discusses systematics and was read in abstract only.
- The size of cosmic-variance and initial-mass-function effects on the JWST number densities.
- Whether the −1.4, −0.2, −1.0 km/s/Mpc selection shifts of the 2026 ladder reanalysis add linearly.
- The 10% → 3% propagation in the tSZ row is a one-line derivation from the quoted scaling exponent, not a result of the paper.
