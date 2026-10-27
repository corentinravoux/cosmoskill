"""The plugin folder holds only what Anthropic's directory should scan, within its limits."""

import json
import re
import subprocess
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


if __name__ == "__main__":
    unittest.main()
