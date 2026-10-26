# cosmo-statistics-inference — references/results.md, Sect. 1.1 (finite-mock correction factors)

Set aside on 2026-10-24 (numbers run) before the agent-computed values were removed. Verbatim from the working tree (base commit 2b5e381). Every entry of the table, and every number of the paragraph under it, was computed by an agent from the formulae of arXiv:2108.10402 and arXiv:1312.4841; none is a value read in a paper. The section now keeps the formulae (in physics-and-methods.md Sect. 2.1) and the worked examples the papers state (Sect. 1.2).

All entries are `[der]`: computed here from the formulae read in arXiv:2108.10402 and arXiv:1312.4841 (see `physics-and-methods.md` §2.1), with `h = (n_s − 1)/(n_s − n_d − 2)`, `DS = 1 + B (n_d − n_θ)`, and `S'/S = (n_s − 1) DS / (n_s − n_d + n_θ − 1)`. The assumption is Gaussian data and independent mocks. The last column is the factor by which a naive parameter error (Gaussian likelihood with the uncorrected `S^-1`) must be multiplied.

| n_s | n_d | n_θ | Hartlap h (covariance) | 1/h (precision) | DS factor (variance) | S'/S (variance) | sqrt(S'/S) (error bar) |
|---|---|---|---|---|---|---|---|
| 100 | 20 | 5 | 1.269 | 0.788 | 1.195 | 1.408 | 1.187 |
| 200 | 50 | 5 | 1.345 | 0.744 | 1.306 | 1.688 | 1.299 |
| 600 | 50 | 5 | 1.093 | 0.915 | 1.082 | 1.170 | 1.082 |
| 1000 | 13 | 7 | 1.014 | 0.986 | 1.006 | 1.012 | 1.006 |
| 1000 | 50 | 7 | 1.054 | 0.949 | 1.045 | 1.092 | 1.045 |
| 1000 | 100 | 10 | 1.113 | 0.899 | 1.100 | 1.209 | 1.100 |
| 1000 | 200 | 10 | 1.252 | 0.799 | 1.238 | 1.529 | 1.237 |
| 1000 | 400 | 10 | 1.671 | 0.599 | 1.653 | 2.712 | 1.647 |
| 2048 | 200 | 10 | 1.109 | 0.902 | 1.103 | 1.216 | 1.103 |
| 2048 | 400 | 10 | 1.244 | 0.804 | 1.237 | 1.528 | 1.236 |
| 25000 | 5000 | 20 | 1.250 | 0.800 | 1.249 | 1.560 | 1.249 |

Reading the table: the Hartlap factor and the Dodelson–Schneider factor are of similar size and both are needed; two different numbers answer "what does it cost". (i) Against a perfectly known covariance, the scatter of the best fit grows by the Dodelson–Schneider variance factor: 1.10 for 1000 mocks and 100 points, 1.65 for 400 points, that is 5% and 29% on the error bar. (ii) Against a posterior built naively on the raw sample covariance, the error bar must be widened by the last column, which contains the Hartlap term as well: 10% and 65%. The two happen to be numerically close (DS variance 1.100 and 1.653; total error-bar factor 1.100 and 1.647), which invites quoting one for the other. A short data vector (the `n_d = 13` row, chosen as an illustration) is unaffected; a long joint data vector is not.

From Sect. 4.1 of the same file (DESI DR2 table), the agent check under the table:

Checks `[der]`: every significance is reproduced by `p = exp(−abs(Δχ²)/2)` and the two-sided Gaussian equivalent. `Δ(DIC) − Δχ²_MAP` lies between 3.6 and 4.7 in every row, that is about twice the two extra parameters, as expected when both are constrained by the data.
