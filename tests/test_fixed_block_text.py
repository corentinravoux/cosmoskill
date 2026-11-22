"""The answering rule for papers the skills do not cite (1.1.1): read first, model knowledge outside L4, labelled."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools" / "templates" / "fixed-block.md"
SKILLS = sorted((ROOT / "plugin" / "skills").glob("*/SKILL.md"))
HUB = ROOT / "plugin" / "skills" / "observational-cosmology" / "SKILL.md"


def flat(path):
    return " ".join(path.read_text(encoding="utf-8").split())


class FixedBlockTextTest(unittest.TestCase):
    def check_rule(self, text):
        self.assertIn("is no evidence about it", text)
        self.assertIn("model knowledge, not in cosmoskill", text)
        self.assertIn("Never confirm from memory that an arXiv ID is a given paper", text)
        self.assertIn("For a manuscript, a proposal or a referee report", text.replace("for a manuscript", "For a manuscript"))
        self.assertIn("give no content from memory", text)

    def test_template(self):
        text = flat(TEMPLATE)
        self.check_rule(text)
        self.assertIn("Read it first", text)
        self.assertIn("[cosmoskill — not in the skills; model knowledge]", text)

    def test_hub_bullet(self):
        self.check_rule(flat(HUB))
        self.assertIn("**Missing is not evidence.**", flat(HUB))

    def test_old_blanket_rule_gone(self):
        self.assertTrue(SKILLS)
        for path in SKILLS + [TEMPLATE]:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertNotIn("never give its content from memory", flat(path))


if __name__ == "__main__":
    unittest.main()
