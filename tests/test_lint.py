"""The lint must flag each kind of personal string and pass clean text."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINT = ROOT / "tools" / "lint_generic.py"
FIXTURES = ROOT / "tests" / "fixtures" / "lint"


def run(path: Path) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(LINT), str(path)], capture_output=True, text=True)


class LintTest(unittest.TestCase):
    def test_clean_text_passes(self):
        result = run(FIXTURES / "clean.md")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_each_bad_fixture_fails(self):
        bad = sorted(p for p in FIXTURES.glob("*.md") if p.name != "clean.md")
        self.assertGreaterEqual(len(bad), 16)
        for fixture in bad:
            with self.subTest(fixture=fixture.name):
                result = run(fixture)
                self.assertEqual(result.returncode, 1, f"{fixture.name} was not flagged")
                self.assertIn(fixture.name, result.stdout)

    def test_paper_authors_and_public_identifiers_are_not_flagged(self):
        result = run(FIXTURES / "clean.md")
        self.assertNotIn("authors", result.stdout)


if __name__ == "__main__":
    unittest.main()
