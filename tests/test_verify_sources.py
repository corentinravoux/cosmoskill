"""The bibliography checker must fail on each kind of defect, without network."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKER = ROOT / "skills" / "observational-cosmology" / "scripts" / "verify_sources.py"
HEADER = "key\tid\tfirst_author\tyear\ttitle\trole\n"
PAPER_A = ("2501.16852", "Ravoux", "2025",
           "Generalized framework for likelihood-based field-level inference of growth rate from velocity and density fields")
PAPER_B = ("2503.14738", "DESI Collaboration", "2025",
           "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints")
CACHE = {
    PAPER_A[0]: {"title": PAPER_A[3], "authors": ["Corentin Ravoux"]},
    PAPER_B[0]: {"title": PAPER_B[3], "authors": [" DESI Collaboration"]},
}


def row(key, paper, role="results", **changes):
    ident, author, year, title = paper
    fields = {"key": key, "id": ident, "first_author": author, "year": year, "title": title, "role": role}
    fields.update(changes)
    return "\t".join(fields[name] for name in ("key", "id", "first_author", "year", "title", "role")) + "\n"


class CheckerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        cache = self.base / "cache" / "cosmo-skill-verify"
        cache.mkdir(parents=True)
        (cache / "arxiv.json").write_text(json.dumps(CACHE), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def skill(self, sources, text="See arXiv:2501.16852 and arXiv:2503.14738.\n"):
        skill = self.base / "cosmo-fixture"
        (skill / "references").mkdir(parents=True, exist_ok=True)
        (skill / "SKILL.md").write_text(text, encoding="utf-8")
        (skill / "references" / "sources.tsv").write_text(sources, encoding="utf-8")
        return skill

    def run_checker(self, skill, *options):
        environment = dict(os.environ, XDG_CACHE_HOME=str(self.base / "cache"))
        return subprocess.run([sys.executable, str(CHECKER), *options, str(skill)],
                              capture_output=True, text=True, env=environment)

    def test_good_skill_passes(self):
        result = self.run_checker(self.skill(HEADER + row("A", PAPER_A) + row("B", PAPER_B)))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("2 sources, 0 problem(s) [arXiv-checked]", result.stdout)

    def test_wrong_title_fails(self):
        result = self.run_checker(self.skill(HEADER + row("A", PAPER_A, title="A paper about something else") + row("B", PAPER_B)))
        self.assertEqual(result.returncode, 1)
        self.assertIn("title mismatch", result.stdout)

    def test_wrong_first_author_fails(self):
        result = self.run_checker(self.skill(HEADER + row("A", PAPER_A, first_author="Smith") + row("B", PAPER_B)))
        self.assertEqual(result.returncode, 1)
        self.assertIn("first author 'Smith'", result.stdout)

    def test_citation_without_row_fails(self):
        result = self.run_checker(self.skill(HEADER + row("A", PAPER_A)), "--offline")
        self.assertEqual(result.returncode, 1)
        self.assertIn("arXiv:2503.14738 cited", result.stdout)
        self.assertIn("has no row", result.stdout)

    def test_row_never_cited_fails(self):
        result = self.run_checker(self.skill(HEADER + row("A", PAPER_A) + row("B", PAPER_B), text="See arXiv:2501.16852.\n"), "--offline")
        self.assertEqual(result.returncode, 1)
        self.assertIn("is never cited", result.stdout)

    def test_bad_header_fails(self):
        result = self.run_checker(self.skill("key\tid\tauthor\tyear\ttitle\trole\n" + row("A", PAPER_A)), "--offline")
        self.assertEqual(result.returncode, 1)
        self.assertIn("header is", result.stdout)

    def test_duplicate_key_fails(self):
        result = self.run_checker(self.skill(HEADER + row("A", PAPER_A) + row("A", PAPER_B)), "--offline")
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate key", result.stdout)

    def test_unknown_role_fails(self):
        result = self.run_checker(self.skill(HEADER + row("A", PAPER_A, role="misc") + row("B", PAPER_B)), "--offline")
        self.assertEqual(result.returncode, 1)
        self.assertIn("role 'misc'", result.stdout)


if __name__ == "__main__":
    unittest.main()
