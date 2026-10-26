"""Numbers (plan of 2026-10-21, step 5): the count of numbers without paper and place, and of derived
numbers, never rises above the baseline; the checker recognises what is and is not a number."""

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


if __name__ == "__main__":
    unittest.main()
