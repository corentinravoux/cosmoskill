"""The layer script finds layers, attaches notes to keys, and stays silent without a layer."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "skills" / "observational-cosmology" / "scripts" / "layers.py"
FIXTURES = ROOT / "tests" / "fixtures" / "layers"


def run(*arguments, home, cwd=None):
    environment = dict(os.environ, COSMOSKILL_HOME=str(home))
    return subprocess.run([sys.executable, str(SCRIPT), *arguments], capture_output=True, text=True,
                          env=environment, cwd=cwd or tempfile.gettempdir())


class LayersTest(unittest.TestCase):
    def test_no_layer_prints_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run("cosmo-lyman-alpha", home=Path(tmp) / "absent", cwd=tmp)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")

    def test_personal_note_is_found_and_labelled(self):
        result = run("cosmo-lyman-alpha", home=FIXTURES / "home")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("=== personal layer", result.stdout)
        self.assertIn("personal note on cosmo-lyman-alpha/results#cosmology-from-p1d", result.stdout)
        self.assertIn("FIXTURE-NOTE-7Q", result.stdout)
        self.assertIn("home domain", result.stdout)
        self.assertIn("conventions: k in s/km", result.stdout)
        self.assertNotIn("may be out of date", result.stdout)

    def test_plugin_prefix_is_accepted(self):
        result = run("cosmoskill:cosmo-lyman-alpha", home=FIXTURES / "home")
        self.assertIn("FIXTURE-NOTE-7Q", result.stdout)

    def test_other_skill_gets_profile_but_no_note(self):
        result = run("cosmo-cmb", home=FIXTURES / "home")
        self.assertIn("conventions:", result.stdout)
        self.assertNotIn("FIXTURE-NOTE-7Q", result.stdout)
        self.assertNotIn("is a home domain", result.stdout)

    def test_json_output(self):
        result = run("cosmo-lyman-alpha", "--json", home=FIXTURES / "home")
        report = json.loads(result.stdout)
        self.assertEqual(report[0]["layer"], "personal")
        self.assertTrue(report[0]["home_domain"])
        self.assertTrue(all(note["known_key"] for note in report[0]["notes"]))

    def test_project_layer_comes_first(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "paper" / ".cosmoskill" / "cosmo-lyman-alpha"
            project.mkdir(parents=True)
            (project / "notes.md").write_text("## general\nPROJECT-NOTE: this paper uses DR1 only.\n", encoding="utf-8")
            deeper = Path(tmp) / "paper" / "sections" / "results"
            deeper.mkdir(parents=True)
            result = run("cosmo-lyman-alpha", home=FIXTURES / "home", cwd=deeper)
        self.assertLess(result.stdout.index("=== project layer"), result.stdout.index("=== personal layer"))
        self.assertIn("project note on cosmo-lyman-alpha/general", result.stdout)

    def test_check_reports_a_note_on_a_missing_key(self):
        clean = run("check", home=FIXTURES / "home")
        self.assertEqual(clean.returncode, 0, clean.stdout)
        orphan = run("check", home=FIXTURES / "orphan")
        self.assertEqual(orphan.returncode, 1)
        self.assertIn("a-section-that-does-not-exist", orphan.stdout)

    def test_init_creates_a_profile_and_keeps_an_existing_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "layer"
            first = run("init", home=home, cwd=tmp)
            self.assertIn("created", first.stdout)
            (home / "profile.md").write_text("mine\n", encoding="utf-8")
            second = run("init", home=home, cwd=tmp)
            self.assertIn("kept", second.stdout)
            self.assertEqual((home / "profile.md").read_text(encoding="utf-8"), "mine\n")


if __name__ == "__main__":
    unittest.main()
