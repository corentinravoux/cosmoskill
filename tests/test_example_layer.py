"""The example layer shipped with cosmoskill-refine stays valid against the package, and the home
directory's layer is never taken for a project layer."""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from layer_fixtures import ROOT, SCRIPTS, run

EXAMPLE = ROOT / "skills" / "cosmoskill-refine" / "example-layer"
BROKEN = ("missing", "retired", "moved", "malformed")


class ExampleLayerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.tmp.cleanup()

    def test_check_passes_without_warnings(self):
        result = run("layers.py", "check", home=EXAMPLE, cwd=self.tmp.name)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 warning(s)", result.stderr)

    def test_every_entry_still_attaches(self):
        result = run("sync_layers.py", home=EXAMPLE, cwd=self.tmp.name)
        broken = [line for line in result.stdout.splitlines() if line.split(" ", 1)[0] in BROKEN]
        self.assertEqual(broken, [], "an entry of the example layer no longer attaches; move it to the new key, "
                                     "then run sync_layers.py --stamp-all with COSMOSKILL_HOME set to the example")

    def test_example_shows_every_kind_of_entry(self):
        notes = "\n".join(path.read_text(encoding="utf-8") for path in EXAMPLE.glob("*/notes.md"))
        for marker in ("mode: override", "mode: suppress", "## general", "private: yes", "base: "):
            self.assertIn(marker, notes)
        self.assertTrue(list(EXAMPLE.glob("*/sources.tsv")))
        self.assertTrue(list(EXAMPLE.glob("*/deep/*.md")))

    def test_home_layer_is_not_a_project_layer(self):
        home = Path(self.tmp.name)
        (home / ".cosmoskill" / "cosmo-cmb").mkdir(parents=True)
        (home / ".cosmoskill" / "cosmo-cmb" / "notes.md").write_text("## general\nHOME-LAYER-NOTE\n", encoding="utf-8")
        work = home / "work"
        work.mkdir()
        environment = dict(os.environ, HOME=str(home), COSMOSKILL_HOME=str(EXAMPLE))
        environment.pop("COSMOSKILL_BASE", None)
        result = subprocess.run([sys.executable, str(SCRIPTS / "layers.py"), "cosmo-cmb"], capture_output=True,
                                text=True, env=environment, cwd=work)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("HOME-LAYER-NOTE", result.stdout)
        self.assertNotIn("project layer", result.stdout)


if __name__ == "__main__":
    unittest.main()
