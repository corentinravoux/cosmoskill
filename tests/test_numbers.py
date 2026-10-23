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

    def test_classification(self):
        self.assertEqual(check_numbers.classify("τ = 0.054 (arXiv:1807.06209) [src: Sect. 3]", ""), "ok")
        self.assertEqual(check_numbers.classify("τ = 0.054 (arXiv:1807.06209) [src]", ""), "no-place")
        self.assertEqual(check_numbers.classify("τ = 0.054 [src: Sect. 3]", ""), "no-paper")
        self.assertEqual(check_numbers.classify("| 0.054 | Sect. 3 |", "From arXiv:1807.06209:"), "ok")
        self.assertEqual(check_numbers.classify("τ = 0.054", ""), "none")


if __name__ == "__main__":
    unittest.main()
