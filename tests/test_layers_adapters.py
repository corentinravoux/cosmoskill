"""Layer additions of 1.1 (docs/layers-v1.md, section 7): provenance, progress files and sweep records."""

import datetime
import json
import tempfile
import unittest
from pathlib import Path

from layer_fixtures import base, layer, run, snapshot

TODAY = datetime.date.today().isoformat()
FOUND_HEADER = "id\tvia\tfound"
SOURCE_HEADER = "key\tid\tfirst_author\tyear\ttitle\trole"


def arxiv_cache(tmp):
    """A cache that serves arXiv:9999.00002 without the network; return the XDG_CACHE_HOME to use."""
    cache = Path(tmp) / "cache"
    (cache / "cosmo-skill-verify").mkdir(parents=True)
    (cache / "cosmo-skill-verify" / "arxiv.json").write_text(json.dumps(
        {"9999.00002": {"title": "A second fixture paper", "authors": ["Ada De Fixture"]}}), encoding="utf-8")
    return cache


class ProvenanceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.skills = base(self.tmp.name, "before")
        self.home = layer(self.tmp.name)
        self.fresh = Path(self.tmp.name) / "fresh"

    def tearDown(self):
        self.tmp.cleanup()

    def layers(self, *arguments, home=None, skills=None, **options):
        return run("layers.py", *arguments, home=home or self.home, skills=skills or self.skills, **options)

    def test_note_with_via_is_written_parsed_and_shown(self):
        written = self.layers("note", "cosmo-fixture", "results#shear-calibration", "FIXTURE-VIA-1", "--via", "valency")
        self.assertEqual(written.returncode, 0, written.stderr)
        notes = (self.home / "cosmo-fixture" / "notes.md").read_text(encoding="utf-8")
        entry = notes[notes.index("FIXTURE-VIA-1") - 60:notes.index("FIXTURE-VIA-1")]
        self.assertIn("via: valency\n", entry)
        shown = self.layers("cosmo-fixture")
        self.assertEqual(shown.returncode, 0, shown.stderr)
        self.assertIn("(found via valency)", shown.stdout)
        self.assertIn("FIXTURE-VIA-1", shown.stdout)
        heading = next(line for line in shown.stdout.splitlines() if "(found via valency)" in line)
        self.assertTrue(heading.startswith("--- personal note on cosmo-fixture/results#shear-calibration"), heading)
        report = json.loads(self.layers("cosmo-fixture", "--json").stdout)
        notes = report[0]["notes"]
        self.assertEqual(next(note for note in notes if "FIXTURE-VIA-1" in note["text"])["via"], "valency")
        self.assertTrue(all(note["via"] == "" for note in notes if "FIXTURE-VIA-1" not in note["text"]))
        self.assertNotIn("via:", next(note for note in notes if "FIXTURE-VIA-1" in note["text"])["text"])

    def test_unknown_via_is_refused_and_writes_nothing(self):
        before = snapshot(self.home)
        for command in (["note", "cosmo-fixture", "general", "text"], ["source", "cosmo-fixture", "9999.00002"]):
            refused = self.layers(*command, "--via", "inspire", "--role", "method")
            self.assertNotEqual(refused.returncode, 0)
            self.assertIn("valency, arxiv-mcp, web", refused.stderr)
        self.assertEqual(snapshot(self.home), before)

    def test_via_survives_restamp(self):
        written = self.layers("override", "cosmo-fixture", "results#optical-depth-tau", "FIXTURE-VIA-2",
                              "--via", "arxiv-mcp", home=self.fresh)
        self.assertEqual(written.returncode, 0, written.stderr)
        path = self.fresh / "cosmo-fixture" / "notes.md"
        old = next(line for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("base: "))
        after = base(self.tmp.name, "after")
        synced = run("sync_layers.py", "--stamp-all", home=self.fresh, skills=after)
        self.assertEqual(synced.returncode, 0, synced.stdout + synced.stderr)
        lines = path.read_text(encoding="utf-8").splitlines()
        self.assertIn("via: arxiv-mcp", lines)
        self.assertIn("mode: override", lines)
        stamps = [line for line in lines if line.startswith("base: ")]
        self.assertEqual(len(stamps), 1)
        self.assertNotEqual(stamps[0], old)
        shown = run("layers.py", "cosmo-fixture", "--json", home=self.fresh, skills=after)
        self.assertEqual(json.loads(shown.stdout)[0]["notes"][0]["via"], "arxiv-mcp")

    def test_source_with_via_writes_found_via_without_version(self):
        cache = arxiv_cache(self.tmp.name)
        added = self.layers("source", "cosmo-fixture", "arXiv:9999.00002v3", "--role", "method", "--via", "valency",
                            cache=cache)
        self.assertEqual(added.returncode, 0, added.stderr)
        rows = (self.home / "cosmo-fixture" / "sources.tsv").read_text(encoding="utf-8").splitlines()
        self.assertEqual(rows[-1].split("\t")[1], "9999.00002")
        found = (self.home / "cosmo-fixture" / "found-via.tsv").read_text(encoding="utf-8").splitlines()
        self.assertEqual(found, [FOUND_HEADER, f"9999.00002\tvalency\t{TODAY}"])
        again = self.layers("source", "cosmo-fixture", "9999.00002", "--role", "method", "--via", "web", cache=cache)
        self.assertEqual(again.returncode, 0, again.stderr)
        self.assertEqual((self.home / "cosmo-fixture" / "found-via.tsv").read_text(encoding="utf-8").splitlines(),
                         found)

    def test_source_refused_writes_no_found_via(self):
        cache = arxiv_cache(self.tmp.name)
        import os
        previous = {name: os.environ.get(name) for name in ("HTTPS_PROXY", "https_proxy")}
        os.environ["HTTPS_PROXY"] = os.environ["https_proxy"] = "http://127.0.0.1:9"
        try:
            refused = self.layers("source", "cosmo-fixture", "9999.00007", "--role", "method", "--via", "valency",
                                  home=self.fresh, cache=cache)
        finally:
            for name, value in previous.items():
                if value is None:
                    os.environ.pop(name, None)
                else:
                    os.environ[name] = value
        self.assertNotEqual(refused.returncode, 0)
        self.assertFalse((self.fresh / "cosmo-fixture" / "found-via.tsv").exists())
        self.assertFalse((self.fresh / "cosmo-fixture" / "sources.tsv").exists())

    def write(self, name, text):
        path = self.fresh / "cosmo-fixture" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def check(self):
        return self.layers("check", home=self.fresh)

    def test_check_validates_found_via(self):
        doi_row = "Doi2099\tdoi:10.1093/mnras/fixture\tFixture\t2099\tA journal-only fixture paper\tmethod\n"
        self.write("sources.tsv", SOURCE_HEADER + "\n" + doi_row)
        self.write("found-via.tsv", "id\thow\tfound\ndoi:10.1093/mnras/fixture\tvalency\t2026-11-10\n")
        bad_header = self.check()
        self.assertEqual(bad_header.returncode, 1)
        self.assertIn("found-via.tsv", bad_header.stdout)
        self.write("found-via.tsv", FOUND_HEADER + "\ndoi:10.1093/mnras/fixture\tvalency\t2026-11-10\n"
                   "9999.00010\tarxiv-mcp\t2026-11-10\n")
        clean = self.check()
        self.assertEqual(clean.returncode, 0, clean.stdout + clean.stderr)
        self.write("found-via.tsv", FOUND_HEADER + "\n9999.00099\tvalency\t2026-11-10\n")
        unknown = self.check()
        self.assertEqual(unknown.returncode, 1)
        self.assertIn("9999.00099", unknown.stdout)
        self.write("found-via.tsv", FOUND_HEADER + "\ndoi:10.1093/mnras/fixture\tinspire\t2026-11-10\n")
        self.assertEqual(self.check().returncode, 1)
        self.write("found-via.tsv", FOUND_HEADER + "\ndoi:10.1093/mnras/fixture\tvalency\tyesterday\n")
        self.assertEqual(self.check().returncode, 1)

    def test_found_records_a_doi_row_once(self):
        doi_row = "Doi2099\tdoi:10.1093/mnras/fixture\tFixture\t2099\tA journal-only fixture paper\tmethod\n"
        self.write("sources.tsv", SOURCE_HEADER + "\n" + doi_row)
        first = self.layers("found", "cosmo-fixture", "doi:10.1093/mnras/fixture", "--via", "valency", home=self.fresh)
        self.assertEqual(first.returncode, 0, first.stderr)
        path = self.fresh / "cosmo-fixture" / "found-via.tsv"
        recorded = path.read_text(encoding="utf-8")
        self.assertEqual(recorded.splitlines(), [FOUND_HEADER, f"doi:10.1093/mnras/fixture\tvalency\t{TODAY}"])
        again = self.layers("found", "cosmo-fixture", "doi:10.1093/mnras/fixture", "--via", "web", home=self.fresh)
        self.assertEqual(again.returncode, 1)
        self.assertEqual(path.read_text(encoding="utf-8"), recorded)
        absent = self.layers("found", "cosmo-fixture", "doi:10.1093/mnras/absent", "--via", "valency", home=self.fresh)
        self.assertEqual(absent.returncode, 1)
        self.assertEqual(path.read_text(encoding="utf-8"), recorded)
        self.assertEqual(self.check().returncode, 0)


class ProgressTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.skills = base(self.tmp.name, "before")
        self.home = Path(self.tmp.name) / "fresh"
        self.path = self.home / "cosmo-fixture" / "_progress.md"

    def tearDown(self):
        self.tmp.cleanup()

    def layers(self, *arguments):
        return run("layers.py", *arguments, home=self.home, skills=self.skills)

    def test_progress_creates_from_template_then_reports_paused(self):
        first = self.layers("progress", "cosmo-fixture")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertIn(f"created {self.path}", first.stdout)
        text = self.path.read_text(encoding="utf-8")
        for heading in ("# Extension run: cosmo-fixture", "Started: ", "Start date: ", "Adapters:", "Stopped:",
                        "## Candidates", "| Paper | Title | Found via | Status | Note |", "## Alerts read",
                        "## Left to do"):
            self.assertIn(heading, text)
        self.assertLess(text.index("## Candidates"), text.index("## Alerts read"))
        self.assertLess(text.index("## Alerts read"), text.index("## Left to do"))
        self.assertIn("`found`, `read`, `proposed`, `accepted`, `rejected`, `skipped`", text)
        self.assertIn(text.strip(), first.stdout)
        self.path.write_text(text + "| arXiv:9999.00009 | A candidate | valency | found | |\n", encoding="utf-8")
        second = self.layers("progress", "cosmo-fixture")
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn(f"paused run: {self.path}", second.stdout)
        self.assertIn("arXiv:9999.00009", second.stdout)

    def test_progress_clear_removes_the_file(self):
        self.layers("progress", "cosmo-fixture")
        cleared = self.layers("progress", "cosmo-fixture", "--clear")
        self.assertEqual(cleared.returncode, 0, cleared.stderr)
        self.assertIn(f"cleared {self.path}", cleared.stdout)
        self.assertFalse(self.path.exists())
        self.assertEqual(self.layers("progress", "cosmo-fixture", "--clear").returncode, 0)

    def test_check_ignores_ids_in_progress(self):
        self.layers("note", "cosmo-fixture", "general", "FIXTURE-PROGRESS-NOTE")
        self.layers("progress", "cosmo-fixture")
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write("| arXiv:9999.00009 | A candidate | valency | found | |\n")
        checked = self.layers("check")
        self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)

    def test_show_does_not_mention_progress(self):
        self.layers("note", "cosmo-fixture", "general", "FIXTURE-PROGRESS-NOTE")
        self.layers("progress", "cosmo-fixture")
        shown = self.layers("cosmo-fixture")
        self.assertEqual(shown.returncode, 0, shown.stderr)
        self.assertIn("FIXTURE-PROGRESS-NOTE", shown.stdout)
        self.assertNotIn("_progress", shown.stdout)
        self.assertNotIn("paused", shown.stdout)


if __name__ == "__main__":
    unittest.main()
