"""Layers v1 (docs/layers-v1.md, section 6): modes, resolve, COSMOSKILL_BASE and sync_layers.py."""

import json
import re
import tempfile
import unittest
from pathlib import Path

from layer_fixtures import FIXTURES, ROOT, base, layer, run


class ResolveTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.skills = base(self.tmp.name, "before")
        self.home = layer(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def resolve(self, target, *options, cwd=None):
        return run("layers.py", "resolve", "cosmo-fixture", target, *options, home=self.home, skills=self.skills, cwd=cwd)

    def test_v0_notes_load_and_resolve_as_add(self):
        shown = run("layers.py", "cosmo-fixture", home=self.home, skills=self.skills)
        self.assertEqual(shown.returncode, 0, shown.stderr)
        self.assertIn("personal note on cosmo-fixture/results#shear-calibration", shown.stdout)
        self.assertIn("FIXTURE-V0-2C", shown.stdout)
        result = self.resolve("results#shear-calibration")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("FIXTURE-BASE-SHEAR", result.stdout)
        self.assertIn("[personal note] FIXTURE-V0-2C", result.stdout)
        self.assertIn("[personal note] FIXTURE-ADD-8P", result.stdout)
        self.assertNotIn("[base]", result.stdout)

    def test_override_prints_base_and_override_both_labelled(self):
        result = self.resolve("results#optical-depth-tau")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[base] FIXTURE-BASE-TAU", result.stdout)
        self.assertIn("[personal override — effective for this researcher] FIXTURE-OVERRIDE-4R", result.stdout)
        self.assertLess(result.stdout.index("[base]"), result.stdout.index("[personal override"))
        self.assertIn("FIXTURE-BASE-LOWELL", result.stdout)  # the section runs to the next heading of its level

    def test_suppress_hides_the_base_text_and_keeps_the_reason(self):
        result = self.resolve("results#introduction")
        self.assertIn("## Introduction", result.stdout)
        self.assertIn("[suppressed by the personal layer: FIXTURE-SUPPRESS-1J", result.stdout)
        self.assertNotIn("FIXTURE-BASE-INTRO", result.stdout)

    def test_whole_file_and_json(self):
        result = self.resolve("results")
        self.assertIn("[personal note on the skill] FIXTURE-GENERAL-3V", result.stdout)
        self.assertIn("FIXTURE-BASE-BAO", result.stdout)
        report = json.loads(self.resolve("results", "--json").stdout)
        sections = {section["key"]: section for section in report["sections"]}
        self.assertEqual(set(sections["optical-depth-tau"]), {"file", "key", "heading", "base_text", "effective", "entries"})
        self.assertEqual(sections["optical-depth-tau"]["effective"], "personal override")
        self.assertEqual(sections["introduction"]["effective"], "suppressed")
        self.assertEqual(sections["shear-calibration"]["effective"], "base")
        self.assertEqual([entry["mode"] for entry in sections["shear-calibration"]["entries"]], ["add", "add"])
        self.assertIn("FIXTURE-BASE-TAU", sections["optical-depth-tau"]["base_text"])

    def test_project_override_wins_and_an_override_beats_a_suppress(self):
        project = Path(self.tmp.name) / "paper" / ".cosmoskill" / "cosmo-fixture"
        project.mkdir(parents=True)
        (project / "notes.md").write_text("## results#optical-depth-tau\nmode: override\nPROJECT-OVERRIDE-6T\n\n"
                                          "## results#introduction\nmode: override\nPROJECT-INTRO-2Q\n", encoding="utf-8")
        result = self.resolve("results", cwd=project.parent.parent)
        self.assertIn("[project override — effective for this researcher] PROJECT-OVERRIDE-6T", result.stdout)
        self.assertIn("[personal override — shadowed by the project override] FIXTURE-OVERRIDE-4R", result.stdout)
        self.assertIn("[base] FIXTURE-BASE-INTRO", result.stdout)
        self.assertIn("[personal suppress — not applied: an override holds] FIXTURE-SUPPRESS-1J", result.stdout)

    def test_an_entry_on_a_missing_section_is_reported(self):
        later = base(self.tmp.name, "after")
        result = run("layers.py", "resolve", "cosmo-fixture", "results", home=self.home, skills=later)
        self.assertIn("results#cmb-lensing-amplitude: no such section in the base", result.stdout)
        self.assertIn("results#sn-host-step: no such section in the base", result.stdout)


class WritingTest(unittest.TestCase):
    def test_modes_are_written_stamped_and_cosmoskill_base_is_respected(self):
        with tempfile.TemporaryDirectory() as tmp:
            skills, home = base(tmp, "before"), Path(tmp) / "layer"
            for command, text in (("override", "OVERRIDE-3W"), ("suppress", "SUPPRESS-8N"), ("note", "NOTE-4F")):
                result = run("layers.py", command, "cosmo-fixture", "results#optical-depth-tau", text, home=home, skills=skills)
                self.assertEqual(result.returncode, 0, result.stderr)
            notes = (home / "cosmo-fixture" / "notes.md").read_text(encoding="utf-8")
            self.assertIn("mode: override\nbase: 6a7fc6c0bc5c\nOVERRIDE-3W", notes)
            self.assertIn("mode: suppress\nbase: 6a7fc6c0bc5c\nSUPPRESS-8N", notes)
            self.assertIn("## results#optical-depth-tau\nbase: 6a7fc6c0bc5c\nNOTE-4F", notes)
            self.assertEqual(run("sync_layers.py", home=home, skills=skills).returncode, 0)
            refused = run("layers.py", "override", "cosmo-fixture", "general", "text", home=home, skills=skills)
            self.assertNotEqual(refused.returncode, 0)
            self.assertIn("needs a section", refused.stderr)
            # Without COSMOSKILL_BASE the package's own skills are the base: the fixture skill is unknown there.
            absent = run("layers.py", "note", "cosmo-fixture", "results#optical-depth-tau", "x", home=home)
            self.assertNotEqual(absent.returncode, 0)
            self.assertIn("no skill named cosmo-fixture", absent.stderr)
            real = run("layers.py", "resolve", "cosmo-lyman-alpha", "results#cosmology-from-p1d", home=home)
            self.assertEqual(real.returncode, 0, real.stderr)
            self.assertNotIn("FIXTURE-BASE", real.stdout)

    def test_check_flags_a_malformed_stamp_and_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            skills, home = base(tmp, "before"), Path(tmp) / "layer"
            (home / "cosmo-fixture").mkdir(parents=True)
            (home / "cosmo-fixture" / "notes.md").write_text(
                "## results#introduction\nmode: hide\nbase: 12ab\ntext\n", encoding="utf-8")
            result = run("layers.py", "check", home=home, skills=skills)
            self.assertEqual(result.returncode, 1)
            self.assertIn("mode 'hide'", result.stdout)
            self.assertIn("base '12ab'", result.stdout)
            sync = run("sync_layers.py", home=home, skills=skills)
            self.assertEqual(sync.returncode, 1)
            self.assertIn("malformed", sync.stdout)


class SyncTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.before = base(self.tmp.name, "before")
        self.after = base(self.tmp.name, "after")
        self.home = layer(self.tmp.name)
        self.notes = self.home / "cosmo-fixture" / "notes.md"

    def tearDown(self):
        self.tmp.cleanup()

    def sync(self, *options, skills=None):
        return run("sync_layers.py", *options, home=self.home, skills=skills or self.after)

    @staticmethod
    def status(result, attach):
        statuses = ("ok", "unstamped", "changed", "moved", "retired", "missing", "malformed")
        line = next(line for line in result.stdout.splitlines() if f"cosmo-fixture/{attach}" in line
                    and line.split()[0] in statuses)
        return line.split()[0]

    def test_unchanged_base_passes(self):
        result = self.sync(skills=self.before)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(self.status(result, "results#optical-depth-tau"), "ok")
        self.assertIn("unstamped", result.stdout)

    def test_base_moved_forward_every_entry_is_reported_and_the_changed_override_exits_3(self):
        result = self.sync()
        self.assertEqual(result.returncode, 3, result.stdout)
        self.assertEqual(self.status(result, "results#optical-depth-tau"), "changed")
        changed = next(line for line in result.stdout.splitlines() if line.startswith("changed"))
        self.assertIn("override cosmo-fixture/results#optical-depth-tau", changed)
        self.assertEqual(self.status(result, "results#cluster-mass-old"), "moved")
        self.assertIn("-> results#cluster-mass-calibration", result.stdout)
        self.assertEqual(self.status(result, "results#sn-host-step"), "retired")
        self.assertEqual(self.status(result, "results#cmb-lensing-amplitude"), "missing")
        self.assertEqual(self.status(result, "results#introduction"), "ok")
        self.assertEqual(self.status(result, "results#bao-scale"), "ok")  # private entries are read too
        records = json.loads(self.sync("--json").stdout)
        self.assertEqual(len(records), 8)
        self.assertEqual({record["status"] for record in records},
                         {"ok", "unstamped", "changed", "moved", "retired", "missing"})

    def test_without_the_override_the_exit_is_2(self):
        text = self.notes.read_text(encoding="utf-8")
        self.notes.write_text(re.sub(r"## results#optical-depth-tau\n.*?(?=\n## )", "", text, flags=re.S), encoding="utf-8")
        self.assertEqual(self.sync().returncode, 2)

    def test_follow_reattaches_and_stamp_clears_changed(self):
        followed = self.sync("--follow")
        self.assertIn("re-attached to results#cluster-mass-calibration", followed.stdout)
        text = self.notes.read_text(encoding="utf-8")
        self.assertIn("## results#cluster-mass-calibration\nbase: a4939b344c53\nFIXTURE-MOVED-6W", text)
        self.assertNotIn("cluster-mass-old", text)
        self.assertEqual(followed.returncode, 3)  # the changed override still stands
        stamped = self.sync("--stamp", "cosmo-fixture/results#optical-depth-tau")
        self.assertEqual(self.status(stamped, "results#optical-depth-tau"), "ok")
        self.assertIn("mode: override\nbase: f66a40618008\nFIXTURE-OVERRIDE-4R", self.notes.read_text(encoding="utf-8"))
        self.assertEqual(stamped.returncode, 2)  # retired and missing remain, for the researcher to edit
        self.assertIn("FIXTURE-GENERAL-3V", self.notes.read_text(encoding="utf-8"))

    def test_stamp_refuses_a_retired_or_missing_entry_and_writes_nothing(self):
        before = self.notes.read_bytes()
        for attach in ("results#sn-host-step", "results#cmb-lensing-amplitude", "results#cluster-mass-old"):
            result = self.sync("--stamp", f"cosmo-fixture/{attach}")
            self.assertEqual(result.returncode, 1, attach)
            self.assertIn("nothing written", result.stderr)
        self.assertEqual(self.notes.read_bytes(), before)

    def test_stamp_all_stamps_unstamped_and_changed_only(self):
        result = self.sync("--stamp-all")
        self.assertNotIn("unstamped", result.stdout)
        self.assertEqual(self.status(result, "results#optical-depth-tau"), "ok")
        self.assertEqual(self.status(result, "results#sn-host-step"), "retired")
        self.assertIn("## results#shear-calibration\nbase: 703b13a73b6d\nFIXTURE-V0-2C", self.notes.read_text(encoding="utf-8"))


class RefineSkillTest(unittest.TestCase):
    def test_workflow_skill_is_short_and_has_no_references(self):
        skill = ROOT / "plugin" / "skills" / "cosmoskill-refine"
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: cosmoskill-refine\n"))
        description = re.search(r"^description: (.+)$", text, re.M).group(1)
        self.assertTrue(description.startswith("Use when"))
        self.assertLess(len(description), 500)
        self.assertFalse((skill / "references").exists())
        self.assertNotIn("cosmoskill:block:start", text)
        for script in ("layers.py", "sync_layers.py", "promote.py"):
            self.assertIn(script, text)

    def test_fixture_base_is_not_a_skill_of_the_package(self):
        self.assertFalse(list((FIXTURES / "base").rglob("SKILL.md")))


if __name__ == "__main__":
    unittest.main()
