"""Keys: assignment is idempotent and the checks fail on each defect. Blocks: a hand edit is detected."""

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"


def load(name):
    sys.path.insert(0, str(TOOLS))
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class KeysTest(unittest.TestCase):
    def setUp(self):
        self.assign = load("assign_keys")
        self.check = load("check_keys")

    def test_slug(self):
        self.assertEqual(self.assign.slugify("4. Cosmology from P1D"), "cosmology-from-p1d")
        self.assertEqual(self.assign.slugify("4a. Removed as out of scope"), "removed-as-out-of-scope")

    def test_assignment_is_idempotent_and_skips_code_fences(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "file.md"
            path.write_text("# Title\n\n## First\ntext\n\n```\n## not a heading\n```\n\n## First\nmore\n", encoding="utf-8")
            self.assertEqual(self.assign.assign(path, dry_run=False), 2)
            text = path.read_text(encoding="utf-8")
            self.assertIn("## First\n<!-- key: first -->", text)
            self.assertIn("## First\n<!-- key: first-2 -->", text)
            self.assertIn("```\n## not a heading\n```", text)
            self.assertEqual(self.assign.assign(path, dry_run=False), 0)
            self.assertEqual(path.read_text(encoding="utf-8"), text)

    def test_package_keys_are_complete(self):
        self.assertEqual(self.check.check_tree(ROOT), [])

    def test_missing_and_repeated_keys_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "plugin" / "skills" / "cosmo-x"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("## A\n<!-- key: a -->\n\n## B\n\n## C\n<!-- key: a -->\n", encoding="utf-8")
            problems = "\n".join(self.check.check_tree(Path(tmp)))
        self.assertIn("heading without a key: B", problems)
        self.assertIn("key repeated: a", problems)

    def test_a_removed_key_is_reported_unless_retired(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            skill = repo / "plugin" / "skills" / "cosmo-x" / "references"
            skill.mkdir(parents=True)
            (skill / "results.md").write_text("## A\n<!-- key: a -->\n\n## B\n<!-- key: b -->\n", encoding="utf-8")
            git = ["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.org"]
            subprocess.run(git + ["init", "-q"], check=True)
            subprocess.run(git + ["add", "-A"], check=True)
            subprocess.run(git + ["commit", "-q", "-m", "base"], check=True)
            (skill / "results.md").write_text("## A\n<!-- key: a -->\n", encoding="utf-8")
            problems = self.check.check_against("HEAD", repo)
            self.assertEqual(len(problems), 1)
            self.assertIn("key b existed at HEAD and is gone", problems[0])
            (skill / "retired-keys.tsv").write_text(
                "file\tkey\tretired_on\treplaced_by\treason\nresults\tb\t2026-10-12\tresults#a\tmerged\n", encoding="utf-8")
            self.assertEqual(self.check.check_against("HEAD", repo), [])


    def test_check_keys_against_pre_move_ref(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            old = repo / "skills" / "cosmo-x" / "references"
            old.mkdir(parents=True)
            (old / "results.md").write_text("## A\n<!-- key: a -->\n\n## B\n<!-- key: b -->\n", encoding="utf-8")
            git = ["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.org"]
            subprocess.run(git + ["init", "-q"], check=True)
            subprocess.run(git + ["add", "-A"], check=True)
            subprocess.run(git + ["commit", "-q", "-m", "before the move"], check=True)
            (repo / "plugin").mkdir()
            subprocess.run(git + ["mv", "skills", "plugin/skills"], check=True)
            subprocess.run(git + ["commit", "-q", "-m", "the move"], check=True)
            self.assertEqual(self.check.check_against("HEAD~1", repo), [])
            self.assertEqual(self.check.check_tree(repo), [])


class BlocksTest(unittest.TestCase):
    def test_blocks_are_current(self):
        result = subprocess.run([sys.executable, str(TOOLS / "sync_blocks.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_a_hand_edit_is_detected_and_repaired(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "package"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__", "docs"))
            target = copy / "plugin" / "skills" / "cosmo-cmb" / "SKILL.md"
            target.write_text(target.read_text(encoding="utf-8").replace("then stop.", "then carry on."), encoding="utf-8")
            tool = copy / "tools" / "sync_blocks.py"
            stale = subprocess.run([sys.executable, str(tool), "--check"], capture_output=True, text=True)
            self.assertEqual(stale.returncode, 1)
            self.assertIn("cosmo-cmb/SKILL.md", stale.stdout)
            subprocess.run([sys.executable, str(tool)], capture_output=True, text=True, check=True)
            again = subprocess.run([sys.executable, str(tool), "--check"], capture_output=True, text=True)
            self.assertEqual(again.returncode, 0)


if __name__ == "__main__":
    unittest.main()
