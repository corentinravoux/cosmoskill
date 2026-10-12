"""The structure check passes on the package and fails on a broken copy."""

import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(root: Path):
    spec = importlib.util.spec_from_file_location("check_structure", ROOT / "tools" / "check_structure.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = root
    module.SKILLS = root / "skills"
    return module


class StructureTest(unittest.TestCase):
    def test_package_passes(self):
        self.assertEqual(load(ROOT).check(), [])

    def test_broken_copy_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "package"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__", "arxiv-snapshot.json"))
            skill = copy / "skills" / "cosmo-cmb"
            text = (skill / "SKILL.md").read_text(encoding="utf-8")
            (skill / "SKILL.md").write_text(text.replace("name: cosmo-cmb", "name: cosmo-cmbx", 1), encoding="utf-8")
            (skill / "references" / "results.md").unlink()
            with (skill / "references" / "sources.tsv").open("a", encoding="utf-8") as handle:
                handle.write("Extra\t2501.16852\tRavoux\t2025\tA title\tresults\n")
            problems = "\n".join(load(copy).check())
            self.assertIn("frontmatter name is 'cosmo-cmbx'", problems)
            self.assertIn("references/results.md", problems)
            self.assertIn("listed with 91 sources, sources.tsv has 92", problems)


if __name__ == "__main__":
    unittest.main()
