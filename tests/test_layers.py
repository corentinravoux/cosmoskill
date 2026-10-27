"""The layer script finds layers, attaches notes to keys, and stays silent without a layer."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "plugin" / "skills" / "observational-cosmology" / "scripts" / "layers.py"
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

    def test_own_papers_and_dossiers_are_listed(self):
        result = run("cosmo-lyman-alpha", home=FIXTURES / "home")
        self.assertIn("personal papers for cosmo-lyman-alpha", result.stdout)
        self.assertIn("Fixture2099 | arXiv:9999.00001", result.stdout)
        self.assertIn("personal dossier cosmo-lyman-alpha/deep/fixture-dossier: Fixture dossier", result.stdout)
        self.assertIn("FIXTURE-SCOPE-3K", result.stdout)
        self.assertIn("[cosmoskill L3 · personal · cosmo-lyman-alpha/deep/fixture-dossier]", result.stdout)
        report = json.loads(run("cosmo-lyman-alpha", "--json", home=FIXTURES / "home").stdout)
        self.assertEqual(report[0]["sources"][0]["key"], "Fixture2099")
        self.assertEqual(report[0]["dossiers"][0]["name"], "fixture-dossier")

    def test_note_is_written_to_a_known_key_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "layer"
            good = run("note", "cosmo-lyman-alpha", "results#cosmology-from-p1d", "NEW-NOTE-5T", "two words", home=home, cwd=tmp)
            self.assertEqual(good.returncode, 0, good.stderr)
            shown = run("cosmo-lyman-alpha", home=home, cwd=tmp)
            self.assertIn("NEW-NOTE-5T two words (noted ", shown.stdout)
            bad = run("note", "cosmo-lyman-alpha", "results#no-such-key", "text", home=home, cwd=tmp)
            self.assertNotEqual(bad.returncode, 0)
            self.assertIn("no section key", bad.stderr)
            self.assertNotIn("no-such-key", (home / "cosmo-lyman-alpha" / "notes.md").read_text(encoding="utf-8"))
            general = run("note", "cosmo-lyman-alpha", "general", "GENERAL-NOTE-2M", home=home, cwd=tmp)
            self.assertEqual(general.returncode, 0, general.stderr)
            self.assertEqual(run("check", home=home, cwd=tmp).returncode, 0)

    def test_source_row_comes_from_arxiv_and_is_written_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "layer"
            cache = Path(tmp) / "cache" / "cosmo-skill-verify"
            cache.mkdir(parents=True)
            (cache / "arxiv.json").write_text(json.dumps(
                {"9999.00002": {"title": "A second  fixture paper", "authors": ["Ada De Fixture", "B. Other"]}}), encoding="utf-8")
            environment = dict(os.environ, COSMOSKILL_HOME=str(home), XDG_CACHE_HOME=str(Path(tmp) / "cache"))

            def source(*arguments):
                return subprocess.run([sys.executable, str(SCRIPT), "source", *arguments], capture_output=True,
                                      text=True, env=environment, cwd=tmp)

            no_role = source("cosmo-lyman-alpha", "9999.00002")
            self.assertNotEqual(no_role.returncode, 0)
            first = source("cosmo-lyman-alpha", "arXiv:9999.00002v3", "--role", "method")
            self.assertEqual(first.returncode, 0, first.stderr)
            table = home / "cosmo-lyman-alpha" / "sources.tsv"
            rows = table.read_text(encoding="utf-8").splitlines()
            self.assertEqual(rows[0].split("\t"), ["key", "id", "first_author", "year", "title", "role"])
            self.assertEqual(rows[1].split("\t"),
                             ["Fixture2099", "9999.00002", "Ada De Fixture", "2099", "A second fixture paper", "method"])
            again = source("cosmo-lyman-alpha", "9999.00002", "--role", "method")
            self.assertIn("nothing written", again.stdout)
            self.assertEqual(len(table.read_text(encoding="utf-8").splitlines()), 2)
            listed = (ROOT / "plugin" / "skills" / "cosmo-lyman-alpha" / "references" / "sources.tsv").read_text(
                encoding="utf-8").splitlines()[1:]
            base = next(row.split("\t")[1] for row in listed if not row.split("\t")[1].startswith("doi:"))
            in_base = source("cosmo-lyman-alpha", base, "--role", "method")
            self.assertIn("already in the package", in_base.stdout)
            self.assertEqual(len(table.read_text(encoding="utf-8").splitlines()), 2)

    def test_dossier_template_and_citation_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp) / "layer"
            made = run("dossier", "cosmo-lyman-alpha", "my-estimator", home=home, cwd=tmp)
            self.assertIn("created", made.stdout)
            path = home / "cosmo-lyman-alpha" / "deep" / "my-estimator.md"
            self.assertIn("## Not verified", path.read_text(encoding="utf-8"))
            self.assertIn("kept", run("dossier", "cosmo-lyman-alpha", "my-estimator", home=home, cwd=tmp).stdout)
            self.assertNotEqual(run("dossier", "cosmo-lyman-alpha", "Bad Name", home=home, cwd=tmp).returncode, 0)
            self.assertEqual(run("check", home=home, cwd=tmp).returncode, 0)
            path.write_text(path.read_text(encoding="utf-8") + "\nSee arXiv:9999.00003.\n", encoding="utf-8")
            unlisted = run("check", home=home, cwd=tmp)
            self.assertEqual(unlisted.returncode, 1)
            self.assertIn("arXiv:9999.00003", unlisted.stdout)
            self.assertIn("layers.py source cosmo-lyman-alpha 9999.00003", unlisted.stdout)

    def test_unknown_skill_is_refused_when_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run("note", "cosmo-no-such-skill", "general", "text", home=Path(tmp) / "layer", cwd=tmp)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((Path(tmp) / "layer").exists())


if __name__ == "__main__":
    unittest.main()
