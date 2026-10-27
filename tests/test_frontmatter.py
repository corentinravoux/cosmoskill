"""Every SKILL.md front matter is valid YAML with a text name and description.

Strict parsers (the skills CLI behind skills.sh, Anthropic's directory) skip
or refuse a skill whose front matter does not parse; Claude Code is lenient,
so the defect does not show there.
"""

import unittest
from pathlib import Path

try:
    import yaml
except ImportError:  # PyYAML is optional for the rest of the suite
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
SKILLS = sorted((ROOT / "skills").glob("*/SKILL.md"))


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: no front matter")
    return text[4:text.index("\n---", 4)]


@unittest.skipIf(yaml is None, "PyYAML not installed")
class FrontMatterTest(unittest.TestCase):
    def test_every_skill_parses(self):
        self.assertEqual(len(SKILLS), 30)
        for path in SKILLS:
            with self.subTest(skill=path.parent.name):
                data = yaml.safe_load(front_matter(path))
                self.assertEqual(data["name"], path.parent.name)
                self.assertIsInstance(data["description"], str)


if __name__ == "__main__":
    unittest.main()
