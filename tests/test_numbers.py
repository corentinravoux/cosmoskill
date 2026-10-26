"""Numbers (plan of 2026-10-21, step 5; plan of 2026-10-26, step 8): every number names its paper and place,
or a `[doc]` source, or is marked as not a value; no derived number; the baseline is zero; the checker
recognises what is and is not a number."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_numbers  # noqa: E402


class NumbersTest(unittest.TestCase):
    def test_no_skill_above_the_baseline(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools" / "check_numbers.py"), "--check"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_every_number_has_its_source(self):
        """Plan of 2026-10-26, step 8: no statement without paper and place, and no derived number, in any skill.
        `doc` and `marked` statements pass; they are counted, not limited."""
        skills = sorted(path for path in (ROOT / "skills").iterdir() if (path / "references").is_dir())
        failing = [f"{record['file']}:{record['line']}: {record['status']}" for skill in skills
                   for record in check_numbers.scan(skill)
                   if record["status"] not in check_numbers.PASSING or record["derived"]]
        self.assertEqual(failing, [], "\n".join(failing[:20]))

    def test_the_baseline_is_zero(self):
        self.assertTrue(all(counts == (0, 0) for counts in check_numbers.read_baseline().values()))

    def test_what_is_not_a_number(self):
        self.assertEqual(check_numbers.numbers_in("Snapshot of 2026-10-09, Sect. 4.2, Table 3, arXiv:2404.03002"), [])
        self.assertEqual(check_numbers.numbers_in("Planck 2018 [src: Eq. 12], Step 6, L3"), [])
        self.assertEqual(check_numbers.numbers_in("τ = 0.054 ± 0.007"), ["0.054", "0.007"])
        self.assertEqual(check_numbers.numbers_in("see §12; ref. 87 of the paper; arXiv:1907.02973, 2007.15994"), [])
        self.assertEqual(check_numbers.numbers_in("the 21 cm signal from 21cmFAST and 21CMMC"), [])
        self.assertEqual(check_numbers.numbers_in("In section 12; arXiv:1907.02973, 1401.1867"), [])
        self.assertEqual(check_numbers.numbers_in("**9.3 Validation.** z = 7.16"), ["7.16"])
        self.assertEqual(check_numbers.numbers_in("**30 m for CMB-HD.** and **3.5 keV line.**"), ["30", "3.5"])

    def test_the_generated_block_is_skipped(self):
        text = ("x = 0.31 (arXiv:1807.06209) [src: abstract]\n\n"
                "<!-- cosmoskill:block:start — generated -->\nSizes, in thousands of tokens: L1 3k; methods 11k\n"
                "<!-- cosmoskill:block:end -->\n")
        self.assertEqual([s for _, _, s, _ in check_numbers.statements(text)],
                         ["x = 0.31 (arXiv:1807.06209) [src: abstract]"])

    def test_classification(self):
        self.assertEqual(check_numbers.classify("τ = 0.054 (arXiv:1807.06209) [src: Sect. 3]", ""), "ok")
        self.assertEqual(check_numbers.classify("τ = 0.054 (arXiv:1807.06209) [src]", ""), "no-place")
        self.assertEqual(check_numbers.classify("τ = 0.054 [src: Sect. 3]", ""), "no-paper")
        self.assertEqual(check_numbers.classify("| 0.054 | Sect. 3 |", "From arXiv:1807.06209:"), "ok")
        self.assertEqual(check_numbers.classify("τ = 0.054", ""), "none")

    def test_a_place_word_needs_its_locator(self):
        self.assertEqual(check_numbers.classify("FoM gain of 300% in figure of merit (arXiv:2510.13509)", ""),
                         "no-place")
        self.assertEqual(check_numbers.classify("| 0.054 | 0.007 |", "Summary statistics (arXiv:1807.06209):"),
                         "no-place")
        self.assertEqual(check_numbers.classify("10 000 pairs (arXiv:1811.06533) [src: Sect. \"Dataset\"]", ""), "ok")
        self.assertEqual(check_numbers.classify("1.5% (arXiv:2607.14854) [src: Conclusions]", ""), "ok")
        self.assertEqual(check_numbers.classify("A = 0.42 (arXiv:2506.21684) [src: App. B, Fig. 7 caption]", ""), "ok")


    def test_doc_flag(self):
        """A code fact or an official-page fact names its source and read date (owner, 2026-10-26)."""
        classify = check_numbers.classify
        self.assertEqual(classify("camb 2.0.4 [doc: https://pypi.org/project/camb/, 2026-10-26]", ""), "doc")
        self.assertEqual(classify("default 1.0 [doc: installed camb 2.0.4, 2026-10-26]", ""), "doc")
        self.assertEqual(classify("N_K = 167 [doc: pyccl/parameters.py, 2026-10-26]", ""), "doc")
        self.assertEqual(classify("| DR1 | 19 March 2025 |", "From [doc: https://data.desi.lbl.gov/doc/releases/, 2026-10-26]:"),
                         "doc")
        self.assertEqual(classify("camb 2.0.4 [doc: https://pypi.org/project/camb/]", ""), "bad-doc")
        self.assertEqual(classify("camb 2.0.4 [doc: https://pypi.org/project/camb/, 2026-13-40]", ""), "bad-doc")
        self.assertEqual(classify("camb 2.0.4 [doc: the camb page, 2026-10-26]", ""), "bad-doc")
        self.assertEqual(classify("a 1.2 [doc: https://a.org/, 2026-10-26] b 3.4 [doc: https://b.org/]", ""), "bad-doc")
        self.assertEqual(check_numbers.numbers_in("camb 2.0.4 [doc: installed camb 2.0.4, 2026-10-26]"), ["2.0"])

    def test_stale_doc(self):
        """A `[doc]` fact read more than two years ago must be re-read (owner, 2026-10-26)."""
        from datetime import date
        classify = check_numbers.classify
        row = "camb 2.0.4 [doc: https://pypi.org/project/camb/, 2026-10-26]"
        self.assertEqual(classify(row, "", today=date(2028, 10, 26)), "doc")
        self.assertEqual(classify(row, "", today=date(2028, 10, 27)), "stale-doc")
        two = "a 1.2 [doc: https://a.org/, 2026-10-26] b 3.4 [doc: https://b.org/, 2024-01-01]"
        self.assertEqual(classify(two, "", today=date(2026, 10, 26)), "stale-doc")
        self.assertEqual(classify("| 19 March 2025 |", "From [doc: https://x.org/, 2024-01-01]:",
                                  today=date(2026, 10, 26)), "stale-doc")
        self.assertEqual(check_numbers.stale_limit(date(2028, 2, 29)), date(2026, 2, 28))
        self.assertNotIn("stale-doc", check_numbers.PASSING)

    def test_old_src(self):
        """A [src]/[sec] flag that names a code or web source must become [doc] (owner, 2026-10-26)."""
        classify = check_numbers.classify
        for flag in ("[src: installed]", "[src: pyccl 3.3.6 installed, `cosmology.py`]", "[src: PyPI JSON API]",
                     "[src: Cobaya docs via context7]", "[src: repository README]", "[sec: same page]",
                     "[sec: web https://github.com/cmbant/CAMB README, read 2026-10-19]"):
            self.assertEqual(classify(f"default `method='fftlog'` {flag}", ""), "old-src", flag)
        self.assertEqual(classify("τ = 0.054 (arXiv:1807.06209) [src: Sect. 3]", ""), "ok")
        self.assertEqual(classify("x = 1.5 (arXiv:2607.14854) [src: App. B, Fig. 7 caption]", ""), "ok")
        self.assertEqual(classify("x = 1.5 (arXiv:2607.14854) [src: abstract of each]", ""), "ok")
        self.assertEqual(classify("Flags: `[sec: web <url>]` taken from a page; `[src]` read in the paper.", ""), "none")

    def test_marker(self):
        """A statement whose numbers are not values carries the marker (owner, 2026-10-26)."""
        self.assertEqual(check_numbers.classify("triplets are LMC / MW / NGC 4258 <!-- num: not a value -->", ""),
                         "marked")
        self.assertEqual(check_numbers.classify("triplets are LMC / MW / NGC 4258", ""), "none")
        self.assertEqual(check_numbers.classify("| x | 0.054 | <!-- num: not a value", ""), "none")

    def test_doc_and_marked_pass_but_are_counted(self):
        records = [{"status": status, "derived": False} for status in ("ok", "doc", "marked", "bad-doc", "none")]
        self.assertEqual(check_numbers.counts(records), (5, 2, 0))

    def test_names_are_not_numbers(self):
        """Exception rules of 2026-10-26: names with digits; each clears one number, not the statement."""
        numbers_in = check_numbers.numbers_in
        self.assertEqual(numbers_in("triplets are LMC / MW / NGC 4258"), [])
        self.assertEqual(numbers_in("the 1ES 1553+113 lines and J1342+0928"), [])
        self.assertEqual(numbers_in("He I 10830 used; Si II 1260 near the BAO scale"), [])
        self.assertEqual(numbers_in("Stripe 82, LOFAR 2.0 and SPTpol 500d"), [])
        self.assertEqual(numbers_in("NGC 4258 at D = 7.58 Mpc"), ["7.58"])
        self.assertEqual(numbers_in("He I 10830 gives Y_P = 0.245"), ["0.245"])
        self.assertEqual(numbers_in("2400 fibres"), ["2400"])

    def test_confidence_levels_are_not_numbers(self):
        numbers_in = check_numbers.numbers_in
        self.assertEqual(numbers_in("| Quantity | Value (68%) | Data |"), [])
        self.assertEqual(numbers_in("r limits are 95%; f_NL are 68% intervals; isocurvature limits are one-tail 95%"), [])
        self.assertEqual(numbers_in("Σm_ν, 95% upper limits, ΛCDM+Σm_ν unless stated."), [])
        self.assertEqual(numbers_in("TDCOSMO quotes medians with 68% intervals; LVK 68.3% symmetric intervals"), [])
        self.assertEqual(numbers_in("Σm_ν < 0.064 eV at 95% C.L."), ["0.064"])
        self.assertEqual(numbers_in("the sample is 95% complete with a purity of 95%"), ["95", "95"])
        self.assertEqual(numbers_in("WALLABY is around 11.5 % complete"), ["11.5"])
        self.assertEqual(numbers_in("Errors are 68% and limits 95% unless stated."), [])
        self.assertEqual(numbers_in("see §3.4–3.6 here"), [])

if __name__ == "__main__":
    unittest.main()
