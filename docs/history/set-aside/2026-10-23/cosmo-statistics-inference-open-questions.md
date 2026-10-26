# cosmo-statistics-inference — references/open-questions.md (values from the agent-computed table)

Set aside on 2026-10-24 (numbers run) before the agent-computed values were removed. Verbatim from the working tree (base commit 2b5e381). These statements quoted the agent-computed table of references/results.md Sect. 1.1 (see cosmo-statistics-inference-results.md).

- Longer data vectors. Joint multi-tracer full shape with bispectrum, or 3×2pt with many tomographic bins, pushes `n_d` into the hundreds or thousands; with 1000 mocks the error inflation reaches tens of per cent (`results.md` §1.1). Compression, denoising and analytic covariances are the three exits, and each has a known failure: compression at a wrong fiducial point, denoised matrices with too-small errors in configuration space (arXiv:2604.13851), analytic matrices without survey realism.

| "With N mocks greater than the number of data points the covariance is fine." | That is the condition for invertibility. Precision needs `n_s` well above `n_d`: with `n_s = 1000` and `n_d = 400` the scatter of the best fit grows by 29% in error bar (variance factor 1.65), and a posterior built on the raw sample covariance must be widened by 65%. | arXiv:1212.4359; `results.md` §1.1 |
