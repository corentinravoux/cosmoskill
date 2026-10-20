"""promote.py (docs/layers-v1.md, section 2): writes into the working tree, refuses private or unsourced entries."""

import json
import tempfile
import unittest
from pathlib import Path

from layer_fixtures import base, layer, run, snapshot

CACHE = {"9999.00011": {"title": "A fixture layer paper", "authors": ["A. Fixture"]}}


class PromoteTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.skills = base(self.tmp.name, "before")
        self.package = self.skills.parent
        self.home = layer(self.tmp.name)
        self.cache = Path(self.tmp.name) / "cache"
        (self.cache / "cosmo-skill-verify").mkdir(parents=True)
        (self.cache / "cosmo-skill-verify" / "arxiv.json").write_text(json.dumps(CACHE), encoding="utf-8")
        self.table = self.skills / "cosmo-fixture" / "references" / "sources.tsv"

    def tearDown(self):
        self.tmp.cleanup()

    def promote(self, *arguments):
        return run("promote.py", "cosmo-fixture", *arguments, home=self.home, skills=self.skills, cache=self.cache)

    def assert_refused(self, *arguments, reason):
        before = snapshot(self.package, self.home)
        result = self.promote(*arguments)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(reason, result.stderr)
        self.assertIn("nothing written", result.stderr)
        self.assertEqual(snapshot(self.package, self.home), before, "a refusal wrote something")

    def test_private_entries_are_refused(self):
        self.assert_refused("note", "results#bao-scale", reason="private")
        self.assert_refused("source", "9999.00013", reason="private")
        self.assert_refused("dossier", "secret-dossier", reason="private")
        marked = self.home / "cosmo-fixture" / "notes.md"
        marked.write_text(marked.read_text(encoding="utf-8").replace(
            "mode: override\n", "mode: override\nprivate: yes\n"), encoding="utf-8")
        self.assert_refused("note", "results#optical-depth-tau", reason="private")

    def test_a_row_without_a_public_identifier_is_refused(self):
        rows = self.home / "cosmo-fixture" / "sources.tsv"
        rows.write_text(rows.read_text(encoding="utf-8") + "Memo2026\tinternal-memo-12\tFixture\t2026\tA group memo\tmethod\n",
                        encoding="utf-8")
        self.assert_refused("source", "Memo2026", reason="no public identifier")
        self.assert_refused("source", "9999.00099", reason="no row")

    def test_a_dossier_citing_an_identifier_with_no_row_is_refused(self):
        self.assert_refused("dossier", "sourced-dossier", reason="cited without a row in the package: 9999.00011")
        self.assert_refused("dossier", "unsourced-dossier", "--with-sources", reason="no row in the layer either: 9999.00019")
        self.assert_refused("dossier", "no-such-dossier", reason="no dossier")

    def test_a_dossier_without_scope_or_with_a_taken_name_is_refused(self):
        dossier = self.home / "cosmo-fixture" / "deep" / "sourced-dossier.md"
        text = dossier.read_text(encoding="utf-8")
        dossier.write_text(text.replace("Snapshot: 2026-10-20.\n", ""), encoding="utf-8")
        self.assert_refused("dossier", "sourced-dossier", "--with-sources", reason="no 'Snapshot:' line")
        dossier.write_text(text, encoding="utf-8")
        (self.skills / "cosmo-fixture" / "deep").mkdir()
        (self.skills / "cosmo-fixture" / "deep" / "sourced-dossier.md").write_text("# Taken\n", encoding="utf-8")
        self.assert_refused("dossier", "sourced-dossier", "--with-sources", reason="already has a dossier")

    def test_source_is_appended_after_the_arxiv_check(self):
        result = self.promote("source", "arXiv:9999.00011v2")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.table.read_text(encoding="utf-8").splitlines()[-1].split("\t"),
                         ["Fixture2099", "9999.00011", "Fixture", "2099", "A fixture layer paper", "method"])
        self.assertIn("verify_sources.py skills/cosmo-fixture", result.stdout)
        self.assert_refused("source", "9999.00011", reason="already in")
        self.assertTrue((self.home / "cosmo-fixture" / "sources.tsv").read_text(encoding="utf-8").count("9999.00011"))

    def test_source_whose_title_does_not_match_arxiv_is_refused(self):
        (self.cache / "cosmo-skill-verify" / "arxiv.json").write_text(json.dumps(
            {"9999.00011": {"title": "Something else entirely", "authors": ["A. Fixture"]}}), encoding="utf-8")
        self.assert_refused("source", "9999.00011", reason="title mismatch")

    def test_dossier_with_sources_and_remove(self):
        result = self.promote("dossier", "sourced-dossier", "--with-sources", "--remove")
        self.assertEqual(result.returncode, 0, result.stderr)
        copied = self.skills / "cosmo-fixture" / "deep" / "sourced-dossier.md"
        self.assertIn("FIXTURE-DOSSIER-2B", copied.read_text(encoding="utf-8"))
        self.assertIn("9999.00011", self.table.read_text(encoding="utf-8"))
        self.assertIn("| `deep/sourced-dossier.md` |", result.stdout)
        self.assertIn("sourced-dossier\tSourced dossier\t\tdeep/sourced-dossier.md\tcovered", result.stdout)
        self.assertIn("tools/assign_keys.py", result.stdout)
        self.assertFalse((self.home / "cosmo-fixture" / "deep" / "sourced-dossier.md").exists())

    def test_note_becomes_a_proposal(self):
        result = self.promote("note", "results#optical-depth-tau")
        self.assertEqual(result.returncode, 0, result.stderr)
        proposals = list((self.package / "docs" / "proposals").glob("*_cosmo-fixture_results_optical-depth-tau.md"))
        self.assertEqual(len(proposals), 1)
        text = proposals[0].read_text(encoding="utf-8")
        self.assertIn("Mode: `override`", text)
        self.assertIn("> FIXTURE-BASE-TAU", text)
        self.assertIn("> FIXTURE-OVERRIDE-4R", text)
        self.assertNotIn(str(self.home), text)
        self.assertIn("FIXTURE-OVERRIDE-4R", (self.home / "cosmo-fixture" / "notes.md").read_text(encoding="utf-8"))
        self.assert_refused("note", "results#optical-depth-tau", reason="exists")
        proposals[0].unlink()
        removed = self.promote("note", "results#optical-depth-tau", "--remove")
        self.assertEqual(removed.returncode, 0, removed.stderr)
        notes = (self.home / "cosmo-fixture" / "notes.md").read_text(encoding="utf-8")
        self.assertNotIn("FIXTURE-OVERRIDE-4R", notes)
        self.assertIn("FIXTURE-ADD-8P", notes)

    def test_note_on_a_section_the_base_lacks_is_refused(self):
        self.assert_refused("note", "results#no-such-key", reason="has no section")


if __name__ == "__main__":
    unittest.main()
