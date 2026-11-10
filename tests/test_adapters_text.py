"""The text contract of the optional adapters: the hub's adapters.md and the extension run of cosmoskill-refine."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HUB = ROOT / "plugin" / "skills" / "observational-cosmology"
ADAPTERS = HUB / "references" / "adapters.md"
REFINE = ROOT / "plugin" / "skills" / "cosmoskill-refine" / "SKILL.md"
KEY = re.compile(r"^<!-- key: [a-z0-9][a-z0-9\-]* -->$")

SECTIONS = ["## Detecting the adapters", "## Routes by task", "## When both are present", "## Refusals",
            "## Day-to-day budget", "## Silence and the status check", "## What each adapter sends"]
ROWS = ["Find papers on a topic", "Papers of the last days", "Who cites a paper", "What a paper cites",
        "Papers not on arXiv", "Read a paper, day-to-day (L4)", "Read a paper, extension mode", "New papers on a topic"]


def sentences(text):
    return [part for part in re.split(r"(?<=[.:;])\s+", " ".join(text.split())) if part]


def section(text, heading):
    start = text.index(heading + "\n")
    end = text.find("\n## ", start + len(heading))
    return text[start:end if end != -1 else len(text)]


class AdaptersTextTest(unittest.TestCase):
    def setUp(self):
        self.text = ADAPTERS.read_text(encoding="utf-8")

    def test_sections_present_and_keyed(self):
        lines = self.text.splitlines()
        for heading in SECTIONS:
            self.assertIn(heading, lines)
            self.assertRegex(lines[lines.index(heading) + 1], KEY)

    def test_routes_table_rows(self):
        routes = section(self.text, "## Routes by task")
        for row in ROWS:
            self.assertIn(f"| {row} |", routes)
        self.assertIn("2501.16852v2", routes)

    def test_budget_and_watch_rules(self):
        self.assertIn("include_abstract=false", self.text)
        alerts = [sentence for sentence in sentences(self.text) if "check_alerts" in sentence]
        self.assertTrue(alerts)
        for sentence in alerts:
            self.assertIn("topic", sentence)
        self.assertIn("watch_topic", self.text)
        self.assertIn("agreement", self.text)

    def test_no_adapter_means_no_new_web_search(self):
        routes = section(self.text, "## Routes by task")
        self.assertIn("no new web search", routes)

    def test_status_line_format(self):
        self.assertIn("arXiv MCP: on|off (suggested)", self.text)
        self.assertIn("Valency: on|off (optional)", self.text)
        self.assertIn("reading: fetch_paper.py", self.text)

    def test_contacts_name_what_leaves_the_machine(self):
        sends = section(self.text, "## What each adapter sends")
        self.assertIn("Semantic Scholar", sends)
        self.assertIn("SEMANTIC_SCHOLAR_API_KEY", self.text)

    def test_hub_description_routes_the_status_check(self):
        # scenario B (docs/history/tests/2026-11-adapters-scenarios.md): without this, no skill loads for "status"
        hub = (HUB / "SKILL.md").read_text(encoding="utf-8")
        description = re.search(r"^description: (.+)$", hub, re.M).group(1)
        self.assertIn("which tools or adapters cosmoskill can use", description)

    def test_hub_file_map_lists_adapters(self):
        hub = (HUB / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/adapters.md", section(hub, "## Hub files"))
        level = " ".join(section(hub, "## Choosing the level").split())
        self.assertIn("get_paper_latex", level)
        self.assertIn("among your tools", level)


class RefineTextTest(unittest.TestCase):
    def setUp(self):
        self.text = REFINE.read_text(encoding="utf-8")

    def extension(self):
        return section(self.text, "## Extension run")

    def test_extension_section_present_and_keyed(self):
        lines = self.text.splitlines()
        self.assertIn("## Extension run", lines)
        self.assertRegex(lines[lines.index("## Extension run") + 1], KEY)
        self.assertLess(self.text.index("## Building a specialised part of a skill"), self.text.index("## Extension run"))

    def test_steps_name_the_commands(self):
        run = self.extension()
        for command in ("layers.py progress", "layers.py sweep", "--record", "--via", "layers.py found", "promote.py",
                        "--clear", "references/adapters.md", "suite-conventions.md"):
            self.assertIn(command, run)

    def test_on_request_only(self):
        run = " ".join(self.extension().split())
        self.assertIn("only when the researcher asks", run)
        self.assertIn("watch_topic", run)
        self.assertIn("agreement", run)
        self.assertIn("Stopped:", run)
        self.assertIn("## Left to do", run)

    def test_announcement_comes_first_and_proposals_are_marked(self):
        # scenario E: the run started searching without announcing itself, and left a proposal marked `read`
        run = " ".join(self.extension().split())
        self.assertIn("before any search", run)
        self.assertIn("in your reply", run)
        self.assertIn("`Extension run on <skill>. <status line>. Start date: <date>.`", run)
        self.assertIn("set its status to `proposed` in the progress file before", run)

    def test_description_mentions_extension(self):
        description = self.text.split("\n---", 1)[0]
        self.assertIn("extension run", description)
        self.assertLessEqual(len(description.split("description:", 1)[1].strip()), 1024)


if __name__ == "__main__":
    unittest.main()
