# cosmoskill benchmark — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Measure what the cosmo-* skills change in answers, on two public
benchmarks, in a 2×2 design: reasoning effort (light / deep) × skills (off / on).

**Architecture:** A small harness under `bench/` drives one headless
`claude -p` call per (item, arm, repetition), each a fresh, isolated session
on the alt account. Answers and token usage go to resumable JSONL files.
TPBench is graded by executing the answer code against the reference
implementation; CosmoPaperQA is graded by a blind LLM judge plus a human
spot-check. `bench/analyse.py` writes tables, figures and a report.

**Tech Stack:** Python 3.12 (`~/Software/claude_env/.venv`: pyarrow 25,
pandas 3, numpy 2.4, scipy 1.15, matplotlib 3.8), `unittest` (as in `tests/`),
Claude Code CLI 2.1.301 headless mode.

**Spec:** `~/Software/claude_config/reports/research/2026-10-16_cosmoskill-benchmarks/report.md`
plus the decisions in the next section (taken with Corentin on 2026-10-16).

## Decisions

| Topic | Decision |
|---|---|
| Benchmarks | **A = CosmoPaperQA** (HF `ASTROANTS/CosmoPaperQA`, file `CosmoPaperQA.parquet`, 105 rows, columns `author, question, ideal, source file, doi, Location, key passage`; no licence stated). **B = TPBench public** (HF `ZhiqiGao/TPBench`, file `data/public-00000-of-00001.parquet`, 10 rows, MIT, columns `problem_id, domain, difficulty_level, problem, solution, answer, code_answer_requirements, reference_implementation`; 4 rows have `domain == "Cosmology"`). AstroMLab-1 was rejected: its public set has no answer key. |
| Arms | `L0` effort `low`, skills off · `D0` effort `high`, skills off · `L1` effort `low`, skills on · `D1` effort `high`, skills on. Deep effort is a CLI option (`--deep-effort`, default `high`; `xhigh`/`max` allowed). |
| Model | `claude-opus-5-5` pinned for every arm and for the judge. |
| Skills-on behaviour | The skills-on arms get `--append-system-prompt` with the text in Task 2, so that skill use is tested, not skill triggering. The invocation rate is still recorded. |
| Skill depth | Skills-on arms may read the skill files (levels L1–L3) but have no Bash and no network, so `fetch_paper.py` (L4) is out: on CosmoPaperQA, L4 would turn the test into open-book reading of the source paper. |
| Repetitions | CosmoPaperQA: 1 per arm (105 paired items). TPBench: 5 per arm (avg@5). |
| Judge | Same model, effort `high`, no tools, no skills, blind to arm, items shuffled with seed 20261016. Grades `correct` / `partial` / `incorrect`. |
| Account | All calls on the alt account: `CLAUDE_CONFIG_DIR=$HOME/.claude-alt`. `--bare` is not usable (it refuses OAuth logins). |

## Global Constraints

- Every call: `--print --model claude-opus-5-5 --output-format stream-json --verbose --no-session-persistence --strict-mcp-config --disallowedTools "mcp__*" --setting-sources project --permission-mode dontAsk`, env `CLAUDE_CONFIG_DIR=$HOME/.claude-alt CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, cwd `bench/workdir/` (an empty directory with no `.claude/`).
- Skills off: add `--tools "" --disable-slash-commands`.
- Skills on: add `--tools "Skill,Read,Grep,Glob" --allowedTools "Skill,Read,Grep,Glob" --add-dir <repo>/skills`.
- Claude binary: `$CLAUDE_BIN`, else `shutil.which("claude")`, else the newest `~/.vscode/extensions/anthropic.claude-code-*/resources/native-binary/claude` (`claude` is not on PATH on this laptop).
- One headless call at a time, no parallelism (session limit).
- Loop order: items outer, arms inner, repetitions innermost, so a run stopped by a usage limit leaves paired data.
- Per-call timeout 1800 s; `--max-budget-usd 5` per call.
- No new Python dependency, no new venv.
- `bench/data/`, `bench/results/`, `bench/workdir/` are gitignored; datasets are never committed.
- Nothing is committed or pushed by the executor; Corentin commits.
- Model-written code runs only through the TPBench grader: subprocess, `python -I`, temporary directory, 60 s timeout.

## Review Focus

1. **Usage limit hit mid-run** → the call returns an error; it is recorded with `status: "error"`, not counted as an answer, retried on the next `run.py` invocation; the loop stops after 3 consecutive errors with a message naming the last error. Test: Task 3.
2. **TPBench answer with no code block, several blocks, or the wrong function name** → graded `fail` with a reason, never a crash; the last ```python block is the one graded. Test: Task 4.
3. **Candidate code that hangs, exits, or raises** → `fail` with reason `timeout` / `error`, grader continues. Test: Task 4.
4. **Skills-on call that never invokes `Skill`** → `skills_invoked == []` in the record; analysis reports the invocation rate per arm. Test: Task 3.
5. **Judge output malformed or refused** → one retry, then grade `unjudged`, excluded from accuracy and listed in the report. Test: Task 5.

---

### Task 1: Data — fetch and normalise

**Files:**
- Create: `bench/__init__.py` (empty), `bench/data.py`
- Modify: `.gitignore` (append `bench/data/`, `bench/results/`, `bench/workdir/`)
- Test: `tests/test_bench_data.py`

**Interfaces:**
- Produces: `normalise_cosmopaperqa(table: pyarrow.Table) -> list[dict]` and `normalise_tpbench(table: pyarrow.Table) -> list[dict]`; item dict keys: `id` (str), `bench` (`"cosmopaperqa"` | `"tpbench"`), `prompt_fields` (dict), `reference` (dict), `domain` (str). `load_items(bench: str, data_dir: Path) -> list[dict]` reads `bench/data/<bench>.jsonl`. CLI `python -m bench.data fetch` downloads both parquet files from `https://huggingface.co/datasets/<repo>/resolve/main/<file>` and writes `bench/data/<bench>.jsonl` plus `bench/data/SHA256SUMS`.
- CosmoPaperQA ids: `cpqa-000` … `cpqa-104` in file order; `prompt_fields = {"question"}`; `reference = {"ideal", "key_passage", "source", "location"}`; `domain = source` arXiv id.
- TPBench ids: `tpb-` + slug of `problem_id`; `prompt_fields = {"problem", "code_answer_requirements"}`; `reference = {"answer", "reference_implementation"}`; `domain` from the `domain` column.

- [ ] **Step 1: Write failing tests** building small `pyarrow.Table`s in-test (2 rows each, same column names as the real files, one CosmoPaperQA row with `key passage = None`):
  - `test_cpqa_ids_are_stable_and_zero_padded`: ids `["cpqa-000", "cpqa-001"]`.
  - `test_cpqa_null_key_passage_becomes_empty_string`.
  - `test_tpbench_id_slug`: `"Bias of a Sampled Halo Field"` → `"tpb-bias-of-a-sampled-halo-field"`.
  - `test_tpbench_domain_kept`: `domain == "Cosmology"`.
  - `test_roundtrip_jsonl`: write then `load_items` returns equal dicts.
- [ ] **Step 2:** Run `python -m unittest tests.test_bench_data -v` → FAIL (module missing).
- [ ] **Step 3:** Implement `bench/data.py` (urllib + pyarrow.parquet, no `datasets` package).
- [ ] **Step 4:** Run the tests → PASS. Run `python -m bench.data fetch` → `bench/data/cosmopaperqa.jsonl` has 105 lines, `tpbench.jsonl` has 10, 4 with `domain == "Cosmology"`.

### Task 2: Arms, command builder, isolation smoke test

**Files:**
- Create: `bench/arms.py`, `bench/prompts.py`, `bench/check_isolation.py`
- Create (captured, not hand-written): `tests/fixtures/bench/stream_skills_off.jsonl`, `tests/fixtures/bench/stream_skills_on.jsonl`
- Test: `tests/test_bench_arms.py`

**Interfaces:**
- Produces: `ARMS: dict[str, Arm]` with `Arm(name: str, effort: str, skills: bool)` for `L0, D0, L1, D1`; `build_command(arm: Arm, prompt: str, *, claude_bin: str, repo: Path, deep_effort: str = "high") -> list[str]`; `build_env(base: dict) -> dict`; `find_claude_bin() -> str`.
- `bench/prompts.py`: `answer_prompt(item: dict) -> str`, `SKILLS_SYSTEM_APPEND: str`, `judge_prompt(item: dict, answer: str) -> str`.
- Exact texts:
  - `SKILLS_SYSTEM_APPEND` = "Before answering, load the cosmo-* skill or skills relevant to the question with the Skill tool, and read their reference files when the answer needs them."
  - CosmoPaperQA answer prompt = "Answer this question about the cosmology research literature in at most three sentences. Give the answer first. If you do not know, say so instead of guessing.\n\nQuestion: {question}"
  - TPBench answer prompt = "{problem}\n\n{code_answer_requirements}\n\nEnd your reply with a single ```python code block that implements exactly the requested function. Use only the Python standard library, numpy and scipy."

- [ ] **Step 1: Write failing tests:**
  - `test_skills_off_has_no_tools`: command contains `--tools ""` and `--disable-slash-commands`, no `--add-dir`.
  - `test_skills_on_tools_and_add_dir`: contains `--tools Skill,Read,Grep,Glob` and `--add-dir <repo>/skills` and `--append-system-prompt SKILLS_SYSTEM_APPEND`.
  - `test_effort_per_arm`: L0/L1 → `low`; D0/D1 → `high`; D1 with `deep_effort="max"` → `max`.
  - `test_common_flags`: every arm has `--model claude-opus-5-5`, `--no-session-persistence`, `--strict-mcp-config`, `--setting-sources project`.
  - `test_env_isolation`: `build_env({})` sets `CLAUDE_CONFIG_DIR` to `~/.claude-alt` expanded, `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`; an existing `CLAUDE_CONFIG_DIR` in the base env is kept.
- [ ] **Step 2:** Run `python -m unittest tests.test_bench_arms -v` → FAIL.
- [ ] **Step 3:** Implement `bench/arms.py` and `bench/prompts.py`.
- [ ] **Step 4:** Run the tests → PASS.
- [ ] **Step 5:** Implement `bench/check_isolation.py`: for arms L0 and L1, send the prompt "Reply with the word ok.", save the raw stream to the two fixture files, and assert on the `type == "system", subtype == "init"` event:
  - skills off: tool list empty; no MCP server; no skill or slash command whose name starts with `cosmo-`; no hook output events.
  - skills on: tools exactly `Skill, Read, Grep, Glob`; no MCP server; every skill directory under `skills/` present by name (25 on 2026-10-16: 24 `cosmo-*` plus `observational-cosmology`; read the list from the directory, do not hard-code it).
  Print PASS/FAIL per check.
- [ ] **Step 6:** Run `python -m bench.check_isolation` on the alt account → all PASS. If a check fails (for example user skills or hooks still load under `--setting-sources project`), stop and report the init event to Corentin; do not loosen a check. Write the outcome to `bench/results/isolation.md`.

### Task 3: Runner — call, parse, resume

**Files:**
- Create: `bench/run.py`
- Test: `tests/test_bench_run.py` (uses the Task 2 fixtures)

**Interfaces:**
- Consumes: `ARMS`, `build_command`, `build_env`, `answer_prompt`, `load_items`.
- Produces: `parse_stream(lines: list[str]) -> dict` with keys `answer` (final `result` text), `status` (`"ok"` | `"error"`), `error` (str), `skills_invoked` (list of skill names from `tool_use` blocks with `name == "Skill"`), `tools_used` (list of tool names), `usage` (the result event's `usage` dict), `model_usage` (its `modelUsage` dict), `cost_usd`, `num_turns`, `duration_ms`. Record = parse result + `item_id`, `bench`, `arm`, `rep`, `effort`, `started_at`. Records append to `bench/results/<bench>/answers.jsonl`.
- `done_keys(path: Path) -> set[tuple[str, str, int]]`: `(item_id, arm, rep)` of records with `status == "ok"`.
- CLI: `python -m bench.run --bench {cosmopaperqa,tpbench} [--arms L0,D0,L1,D1] [--reps N] [--limit N] [--items id,id] [--deep-effort high]`. Default reps: 1 for cosmopaperqa, 5 for tpbench.

- [ ] **Step 1: Write failing tests:**
  - `test_parse_skills_off_fixture`: status ok, `skills_invoked == []`, `tools_used == []`, `answer` non-empty, `usage` has `output_tokens`.
  - `test_parse_skills_on_fixture`: status ok; fields present (the smoke prompt may legitimately invoke no skill).
  - `test_parse_skill_invocation`: a synthetic stream with one `tool_use` block `{"name": "Skill", "input": {"skill": "cosmo-cmb"}}` gives `skills_invoked == ["cosmo-cmb"]`.
  - `test_parse_error_result`: a final event with `is_error: true` gives `status == "error"` and the error text.
  - `test_parse_truncated_stream`: no `result` event gives `status == "error"`, `error == "no result event"`.
  - `test_done_keys_ignores_errors`.
  - `test_stop_after_three_consecutive_errors`: with a stub executor returning errors, `run_loop` stops after 3 calls and returns exit code 2.
- [ ] **Step 2:** Run `python -m unittest tests.test_bench_run -v` → FAIL.
- [ ] **Step 3:** Implement `bench/run.py`: `run_loop(items, arms, reps, executor) -> int` with `executor(cmd, env, cwd, timeout) -> list[str]` (injectable for tests; the real one uses `subprocess.run`); skip `done_keys`; flush each record as it completes. On timeout, record `status: "error", error: "timeout"`.
- [ ] **Step 4:** Run the tests → PASS.

### Task 4: TPBench grader

**Files:**
- Create: `bench/grade_tpbench.py`, `bench/tpbench_domains.json` (only if Step 5 needs it)
- Test: `tests/test_bench_grade_tpbench.py`

**Interfaces:**
- Consumes: TPBench items, `answers.jsonl` records.
- Produces: `extract_code(answer: str) -> str | None` (last ```python block); `strip_reference(ref: str) -> str` (removes `\begin{python}` / `\end{python}`); `grade(candidate_code: str, reference_code: str, *, seed: int, trials: int = 20, domains: dict | None = None) -> dict` with keys `verdict` (`"pass"` | `"fail"` | `"ungradable"`), `reason`, `matched`, `valid`. CLI `python -m bench.grade_tpbench` writes `bench/results/tpbench/grades.jsonl`.
- Rules: the function name is that of the first top-level `def` in the reference; the candidate must define the same name. For each parameter: annotation `float` or none → uniform in [0.1, 2.0]; `int` → integer in [1, 5]; any other annotation → `ungradable`. A trial is valid when the reference returns finite values without raising. Match: `numpy.allclose(candidate, reference, rtol=1e-2, atol=1e-10)` elementwise (scalars, tuples, arrays). Pass if `valid >= 5` and `matched / valid >= 0.9`. Both functions run inside one `python -I` subprocess per answer, in a temporary directory, 60 s timeout.

- [ ] **Step 1: Write failing tests** with a toy reference `def speed(v: float, w: float) -> float: return v * w`:
  - `test_identical_code_passes`; `test_algebraically_equal_passes` (`return w * v`); `test_wrong_formula_fails`;
  - `test_no_code_block_fails` (reason `no code`); `test_last_block_graded` (two blocks, the second correct → pass);
  - `test_wrong_function_name_fails`; `test_raising_candidate_fails`; `test_hanging_candidate_times_out` (`while True: pass`, timeout lowered to 2 s in the test);
  - `test_sys_exit_candidate_fails`; `test_tuple_return_compared_elementwise`;
  - `test_strip_reference_removes_latex_wrappers`.
- [ ] **Step 2:** Run `python -m unittest tests.test_bench_grade_tpbench -v` → FAIL.
- [ ] **Step 3:** Implement `bench/grade_tpbench.py`.
- [ ] **Step 4:** Run the tests → PASS.
- [ ] **Step 5:** Self-check on the real data: grade each reference implementation against itself → 10/10 `pass`. For any problem whose reference raises or gives non-finite values on [0.1, 2.0], add a per-parameter range to `bench/tpbench_domains.json` (`{"tpb-…": {"param": [lo, hi]}}`) from the problem statement, and rerun until 10/10.

### Task 5: CosmoPaperQA judge and spot-check sheet

**Files:**
- Create: `bench/judge.py`
- Test: `tests/test_bench_judge.py`

**Interfaces:**
- Consumes: `answers.jsonl` for cosmopaperqa, items, `build_env`, `judge_prompt`.
- Produces: `parse_grade(text: str) -> dict | None` returning `{"grade": "correct"|"partial"|"incorrect", "reason": str}` or `None`; `judge_order(records: list[dict], seed: int = 20261016) -> list[dict]` (shuffled; the arm is never put in the prompt); CLI `python -m bench.judge` writes `bench/results/cosmopaperqa/grades.jsonl` (resumable on `(item_id, arm, rep)`) and `bench/results/cosmopaperqa/spotcheck.csv`.
- Judge call: arm-independent flags as skills off, effort `high`, `--json-schema` for the object above.
- `judge_prompt` text: "You grade an answer to a question about a cosmology paper. Compare the candidate with the reference answer and the key passage from the paper. Grade `correct` if the candidate states the reference answer's content without a factual error, `partial` if it gets part of it or adds a wrong statement next to a right one, `incorrect` otherwise, including refusals. Return JSON {\"grade\": …, \"reason\": one sentence}.\n\nQuestion: {question}\nReference answer: {ideal}\nKey passage: {key_passage or 'not given'}\nCandidate answer: {answer}"
- Spot-check sheet: 40 rows, 10 per arm, drawn with the seed; columns `item_id, question, ideal, candidate, judge_grade, human_grade` (last column empty, for Corentin).

- [ ] **Step 1: Write failing tests:**
  - `test_parse_valid_json`; `test_parse_json_in_code_fence`; `test_parse_bad_grade_returns_none` (`"grade": "maybe"`); `test_parse_garbage_returns_none`.
  - `test_judge_prompt_has_no_arm` (the strings `L0`, `D1`, `skill` absent from the prompt).
  - `test_order_deterministic_for_seed`.
  - `test_unjudged_after_one_retry`: stub executor returning garbage twice → grade record `{"grade": "unjudged"}`, two calls made.
  - `test_spotcheck_stratified`: 40 rows, 10 per arm.
- [ ] **Step 2:** Run `python -m unittest tests.test_bench_judge -v` → FAIL.
- [ ] **Step 3:** Implement `bench/judge.py`.
- [ ] **Step 4:** Run the tests → PASS.

### Task 6: Pilot and budget gate

**Files:**
- Create: `bench/cost.py` (`summarise(records) -> dict` per arm: calls, median and total of `input_tokens + cache_read_input_tokens + cache_creation_input_tokens + output_tokens`, total `cost_usd`, median `duration_ms`; `project(summary, n_calls_per_arm) -> dict`)
- Test: `tests/test_bench_cost.py` (`test_summarise_sums_all_token_kinds`, `test_project_scales_linearly`)

- [ ] **Step 1:** Write and pass the two cost tests (`python -m unittest tests.test_bench_cost -v`).
- [ ] **Step 2:** Pilot: `python -m bench.run --bench cosmopaperqa --limit 10` and `python -m bench.run --bench tpbench --items tpb-blackbody-in-d-dimensions,tpb-bias-of-a-sampled-halo-field --reps 1`. Expected: 40 + 8 records, all `status: ok`.
- [ ] **Step 3:** Grade the pilot (`python -m bench.judge`, `python -m bench.grade_tpbench`) and check by eye 5 judged answers and both TPBench grades.
- [ ] **Step 4:** Run `python -m bench.cost --project` → projected tokens, cost and hours for the full run (420 CosmoPaperQA calls, 200 TPBench calls, 420 judge calls). Write it to `bench/results/pilot.md`.
- [ ] **Step 5: STOP.** Show `pilot.md` to Corentin and wait for go / no-go. Options to cut cost if needed: TPBench reps 5 → 3; deep arms on a 50-item CosmoPaperQA subset.

### Task 7: Full runs

- [ ] **Step 1:** `python -m bench.run --bench cosmopaperqa` until it exits 0 with 420 `ok` records (rerun after each usage-limit stop; resume skips done keys).
- [ ] **Step 2:** `python -m bench.run --bench tpbench` until 200 `ok` records.
- [ ] **Step 3:** `python -m bench.judge` until 420 grades, then `python -m bench.grade_tpbench`.
- [ ] **Step 4:** Corentin fills `human_grade` in `spotcheck.csv`.

### Task 8: Analysis and report

**Files:**
- Create: `bench/analyse.py`
- Test: `tests/test_bench_analyse.py`
- Output: `~/Software/claude_config/reports/research/<YYYY-MM-DD>_cosmoskill-benchmark-results/` with `report.md`, `fig_*.png`, the tables as CSV; add one line to `~/Software/claude_config/reports/README.md`.

**Interfaces:**
- Produces: `accuracy(grades, strict: bool) -> float` (strict: `correct` = 1; lenient: `partial` = 0.5; `unjudged` excluded); `bootstrap_ci(values, n=10000, seed=20261016) -> tuple[float, float]` (95 %, resampling items); `mcnemar_exact(a: list[bool], b: list[bool]) -> float` (two-sided, `scipy.stats.binomtest` on discordant pairs); `avg_at_k(grades) -> float`; `pass_at_k(grades) -> float`.

- [ ] **Step 1: Write failing tests:** `test_accuracy_strict_and_lenient` (grades `[correct, partial, incorrect, unjudged]` → 1/3 and 0.5); `test_mcnemar_no_discordant_is_one`; `test_mcnemar_known_value` (10 discordant all one way → p = 2 × 0.5¹⁰ = 0.001953125); `test_bootstrap_ci_contains_mean`; `test_avg_and_pass_at_k`.
- [ ] **Step 2:** Run `python -m unittest tests.test_bench_analyse -v` → FAIL; implement; → PASS.
- [ ] **Step 3:** Run `python -m bench.analyse`. Tables:
  - CosmoPaperQA: accuracy strict and lenient per arm with 95 % CI; paired contrasts L1−L0, D1−D0 (skills effect), D0−L0, D1−L1 (effort effect) with McNemar p; judge–human agreement and Cohen's κ on the spot-check.
  - TPBench: avg@5 and pass@5 per arm, overall and split Cosmology (4) / other (6), the other domains being a control where the skills should not help; descriptive only, no test (10 problems).
  - Cost per arm and benchmark: median and total tokens, total `cost_usd`, median duration; skill invocation rate and the five most-used skills in L1 and D1.
- [ ] **Step 4:** Figures (load the `dataviz` skill first): `fig_cpqa_accuracy.png` (accuracy per arm with CI), `fig_tpbench.png` (avg@5 per arm, cosmology vs other), `fig_cost_accuracy.png` (accuracy against median tokens per call, one point per arm and benchmark).
- [ ] **Step 5:** Write `report.md`: design, isolation result (Task 2), pilot, results, caveats (same-model judge, CosmoPaperQA built from five papers published before the model cutoff and probably in training data, TPBench n = 10, L4 excluded by design), and the list of `unjudged` items.
