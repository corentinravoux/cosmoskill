# cosmo-galaxy-clustering — references/results.md, Sect. 4.1 (DESI DR1 ShapeFit table)

Set aside on 2026-10-24 (numbers run) before the agent-computed values were removed. Verbatim from the working tree (base commit 2b5e381). The errors on the absolute fσ_s8 (ShapeFit+BAO) column were computed by an agent as the square root of the diagonal covariance element printed in arXiv:2411.12021, App. A; they are not values read in the paper. The table now gives the paper's fσ_s8 values and C_33 elements (App. A, Eqs. 31–42) instead.

Adame et al. 2024, arXiv:2411.12021. Ratios from the ShapeFit results table
(MAP values); absolute values from the appendix that lists the compressed data
vectors and Gaussian covariances, the error being the square root of the
diagonal covariance element [der]. The quantity is
fσ_s8, not fσ8 (see `physics-and-methods.md`).

| Bin | z_eff | fσ_s8/fid (ShapeFit) | fσ_s8/fid (ShapeFit+BAO) | fσ_s8 (ShapeFit+BAO) | Flag |
|---|---|---|---|---|---|
| BGS | 0.30 | 0.80 ± 0.20 | 0.84 ± 0.19 | 0.396 ± 0.090 | [src], error [der] |
| LRG1 | 0.51 | 1.09 (+0.12/−0.14) | 1.16 ± 0.13 | 0.548 ± 0.059 | [src], error [der] |
| LRG2 | 0.71 | 1.05 ± 0.12 | 1.04 (+0.11/−0.092) | 0.480 ± 0.048 | [src], error [der] |
| LRG3 | 0.92 | 0.96 (+0.11/−0.10) | 0.997 (+0.10/−0.084) | 0.438 ± 0.041 | [src], error [der] |
| ELG2 | 1.32 | 0.95 (+0.11/−0.08) | 0.945 (+0.097/−0.077) | 0.373 ± 0.034 | [src], error [der] |
| QSO | 1.49 | 1.16 ± 0.12 | 1.16 ± 0.12 | 0.437 ± 0.046 | [src], error [der] |

Combined precision on the RSD amplitude: 4.7% [src] (arXiv:2411.12021), which
the paper describes as similar to that of twenty years of earlier surveys;
BOSS DR12 alone reached 6% [src] (arXiv:1607.03155).
