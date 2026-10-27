"""Script paths in the skills resolve in Claude Code and in the Claude app.

The app names each skill folder with the plugin prefix (`cosmoskill:cosmo-cmb`)
and passes `${CLAUDE_SKILL_DIR}` unexpanded; Claude Code expands it and, by
route C, uses plain folder names. One path form has to serve both.
"""

import re
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
START = "<!-- cosmoskill:block:start"
COMMAND = re.compile(r"`python3 ([^`]*fetch_paper\.py\"?)")


def skill_files():
    yield from sorted(SKILLS.glob("*/SKILL.md"))
    yield from sorted((SKILLS / "observational-cosmology" / "references").glob("*.md"))


def path_expression() -> str:
    text = (SKILLS / "cosmo-cmb" / "SKILL.md").read_text(encoding="utf-8")
    return COMMAND.search(text).group(1)


class ScriptPathTest(unittest.TestCase):
    def test_no_file_uses_the_unprefixed_sibling_path(self):
        for path in skill_files():
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertNotIn("/../observational-cosmology/", path.read_text(encoding="utf-8"))

    def test_hub_scripts_are_run_with_python3(self):
        # the scripts are not executable (mode 644): a bare path gives "Permission denied"
        text = (SKILLS / "observational-cosmology" / "SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn("`${CLAUDE_SKILL_DIR}/scripts/", text)

    def test_every_block_states_the_unexpanded_rule(self):
        blocks = 0
        for path in SKILLS.glob("*/SKILL.md"):
            text = path.read_text(encoding="utf-8")
            if START not in text:
                continue
            blocks += 1
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIn("reaches you unexpanded", text.split(START, 1)[1])
        self.assertEqual(blocks, 29)

    def layout(self, prefix: str, hub: bool) -> str:
        """A skills folder as one host lays it out; return the expression with the skill folder filled in."""
        tmp = tempfile.TemporaryDirectory(suffix=" with space")
        self.addCleanup(tmp.cleanup)
        base = Path(tmp.name)
        skill = base / f"{prefix}cosmo-cmb"
        skill.mkdir()
        if hub:
            scripts = base / f"{prefix}observational-cosmology" / "scripts"
            scripts.mkdir(parents=True)
            (scripts / "fetch_paper.py").write_text("import sys\nsys.exit(0)\n")
        return path_expression().replace("${CLAUDE_SKILL_DIR}", str(skill))

    def test_the_path_resolves_with_and_without_the_plugin_prefix(self):
        for prefix in ("", "cosmoskill:"):
            with self.subTest(prefix=prefix):
                expression = self.layout(prefix, hub=True)
                result = subprocess.run(["bash", "-c", f"ls -d {expression}"], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue(result.stdout.strip().endswith("scripts/fetch_paper.py"))

    def test_unmatched_glob_fails_loudly(self):
        expression = self.layout("cosmoskill:", hub=False)
        result = subprocess.run(["bash", "-c", f"python3 {expression} --help"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
