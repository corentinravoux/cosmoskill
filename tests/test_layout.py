"""The plugin folder holds only what Anthropic's directory should scan, within its limits."""

import json
import os
import re
import struct
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugin"
ALLOWED = {".claude-plugin", "skills", "README.md", "LICENSE"}


def plugin_files():
    listing = subprocess.run(["git", "-C", str(ROOT), "ls-files", "plugin"], capture_output=True, text=True, check=True)
    return [line for line in listing.stdout.splitlines() if line]


class PluginFolderTest(unittest.TestCase):
    def test_plugin_folder_holds_only_the_plugin(self):
        top = {Path(name).parts[1] for name in plugin_files()}
        self.assertLessEqual(top, ALLOWED)
        self.assertLessEqual({".claude-plugin", "skills", "LICENSE"}, top)

    def test_plugin_folder_within_directory_limits(self):
        files = plugin_files()
        self.assertLessEqual(len(files), 512)
        for name in files:
            path = ROOT / name
            self.assertFalse(path.is_symlink(), name)
            if path.name == "icon.png":
                continue
            data = path.read_bytes()
            self.assertTrue(data, f"{name} is empty")
            self.assertLess(len(data), 262144, name)
            data.decode("utf-8")

    def test_marketplace_points_to_plugin(self):
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual([entry["source"] for entry in market["plugins"]], ["./plugin"])
        self.assertTrue((PLUGIN / ".claude-plugin" / "plugin.json").is_file())
        self.assertFalse((ROOT / ".claude-plugin" / "plugin.json").exists())

    def test_license_copies_identical(self):
        self.assertEqual((PLUGIN / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())


class PluginReadmeTest(unittest.TestCase):
    def readme(self):
        return (PLUGIN / "README.md").read_text(encoding="utf-8")

    def test_plugin_readme_exists(self):
        self.assertIn("plugin/README.md", plugin_files())

    def test_plugin_readme_long_enough(self):
        prose = re.sub(r"```.*?```", "", self.readme(), flags=re.S)
        self.assertGreaterEqual(len(prose.split()), 40)

    def test_plugin_readme_discloses_network(self):
        text = self.readme()
        for needle in ("export.arxiv.org", "arxiv.org", "ar5iv.labs.arxiv.org", "~/.cache/cosmo-skill-verify"):
            self.assertIn(needle, text)

    def test_plugin_readme_has_no_launcher(self):
        text = self.readme()
        for launcher in ("npx ", "uvx ", "pipx ", "pip install", "curl "):
            self.assertNotIn(launcher, text)

    def test_root_readme_links_plugin_skills(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("cosmoskill/plugin/skills/*/", text)
        self.assertNotIn("cosmoskill/skills/*/", text)


class IconTest(unittest.TestCase):
    def test_icon_meets_directory_rules(self):
        icon = PLUGIN / ".claude-plugin" / "icon.png"
        data = icon.read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(data[12:16], b"IHDR")
        width, height = struct.unpack(">II", data[16:24])
        self.assertEqual(width, height)
        self.assertGreaterEqual(width, 512)
        self.assertLessEqual(width, 2048)
        self.assertLess(len(data), 2_000_000)


OLD_PATH = re.compile(r"(?<![\w./~-])skills/(observational-cosmology|cosmo-|\*|<)")


class MaintainedPathsTest(unittest.TestCase):
    def test_no_maintained_text_points_to_the_old_skills_folder(self):
        files = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *sorted((ROOT / "docs").glob("*.md")),
                 *sorted(PLUGIN.rglob("*.md"))]
        found = [f"{path.relative_to(ROOT)}:{number}: {line.strip()[:80]}"
                 for path in files for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
                 if OLD_PATH.search(line)]
        self.assertEqual(found, [])

    def test_suite_conventions_counts_three_levels_to_the_root(self):
        text = (PLUGIN / "skills" / "observational-cosmology" / "references" / "suite-conventions.md").read_text(
            encoding="utf-8")
        self.assertNotIn("two levels above the hub", text)

    def test_promote_writes_proposals_at_the_repository_root(self):
        scripts = PLUGIN / "skills" / "observational-cosmology" / "scripts"
        environment = {key: value for key, value in os.environ.items() if key != "COSMOSKILL_BASE"}
        result = subprocess.run([sys.executable, "-c", "import promote; print(promote.PACKAGE)"], cwd=scripts,
                                env=environment, capture_output=True, text=True, check=True)
        self.assertEqual(Path(result.stdout.strip()), ROOT)

    def test_changelog_tells_clone_users_what_to_do(self):
        text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        section = text.split("## 1.0.3", 1)[1].split("\n## ", 1)[0]
        self.assertIn("~/.claude/skills/cosmoskill", section)


if __name__ == "__main__":
    unittest.main()
