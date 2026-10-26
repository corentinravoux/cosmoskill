# cosmo-distance-ladder-h0 — references/results.md, section 5 (tension significance) and section 8 (derived rows)

Set aside on 2026-10-24 (numbers run) before the agent-computed values were removed. Verbatim from the working tree (base commit 2b5e381). The significances were computed by an agent with the Gaussian rule stated below; the moduli, the ratio and the CCHP total error were converted or combined by an agent. None is a value read in a paper.

## 5. Tension significance, computed uniformly
<!-- key: tension-significance-computed-uniformly -->

Derivation `[der]`: n = (H0_local - H0_early) / sqrt(sigma_local^2 +
sigma_early^2), assuming Gaussian, uncorrelated errors in H0. Asymmetric
errors were symmetrised; the CCHP error is the quadrature total 1.94.

| Local value | vs Planck 2018 (67.4 ± 0.5) | vs SPT-3G D1 (66.66 ± 0.60) | vs CMB-SPA (67.19 ± 0.38) | vs DESI DR2 + BBN (68.51 ± 0.58) |
|---|---|---|---|---|
| SH0ES 2022, 73.04 ± 1.04 | 4.9 | 5.3 | 5.3 | 3.8 |
| SH0ES 2024, 73.17 ± 0.86 | 5.8 | 6.2 | 6.4 | 4.5 |
| SH0ES 2025, 73.18 ± 0.88 | 5.7 | 6.1 | 6.2 | 4.4 |
| H0DN 2025, 73.50 ± 0.81 | 6.4 | 6.8 | 7.1 | 5.0 |
| CCHP TRGB, 70.39 ± 1.94 | 1.5 | 1.8 | 1.6 | 0.9 |
| TDCOSMO-2025, 71.6 ± 3.6 | 1.2 | 1.4 | 1.2 | 0.8 |
| MCP 2020, 73.9 ± 3.0 | 2.1 | 2.4 | 2.2 | 1.8 |
| SBF 2025, 73.8 ± 2.4 | 2.6 | 2.9 | 2.7 | 2.1 |


From section 1 (paragraph under the table):

Reading the table. The CCHP and SH0ES numbers are not independent: they share
the anchor NGC 4258 and many SN Ia calibrators. The CCHP total uncertainty is
1.94 `[der]` (quadrature sum of the three terms quoted in arXiv:2408.06153);
Li et al. (arXiv:2504.08921) quote the same result as 70.4 ± 1.9 `[src]`.

From section 8:

| Quantity | Value | Citation | Flag |
|---|---|---|---|
| LMC distance modulus | 18.477 | from 49.59 kpc | [der] |
| NGC 4258 modulus and total error | 29.397; 1.5% in distance, 0.032 mag | from 7.576 Mpc, errors in quadrature | [der] |

The ratio 111.8 / 98.5 = 1.135 `[der]` is the Coma version of the tension: it
is larger than 73.5 / 67.4 because the DESI FP relation itself returns 76.5.
