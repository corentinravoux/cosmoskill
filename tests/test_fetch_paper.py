"""The paper reader turns a rendering into sections and finds text in them. No network."""

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "plugin" / "skills" / "observational-cosmology" / "scripts" / "fetch_paper.py"

DOCUMENT = """<html><head><style>p {color: red}</style></head><body>
<nav>Menu that must not appear</nav>
<h1 class="ltx_title">A paper about distances</h1>
<h2>Abstract</h2><p>We measure a distance.</p>
<h2>1 Introduction</h2><p>Baryon acoustic oscillations are a ruler.</p>
<h2>2 Results</h2>
<h3>2.1 Baseline fit</h3>
<p>We find <math alttext="D_H/r_d = 8.632 \\pm 0.098"><mi>D</mi><annotation encoding="application/x-tex">D_H/r_d</annotation></math> at the effective redshift.</p>
<table><tr><td>parameter</td><td>value</td></tr><tr><td>alpha</td><td>1.002</td></tr></table>
<h3>2.2 Goodness of fit</h3><p>The fit is acceptable.</p>
<h2>3 Conclusions</h2><p>The ruler works.</p>
</body></html>"""


def load():
    spec = importlib.util.spec_from_file_location("fetch_paper", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["fetch_paper"] = module
    spec.loader.exec_module(module)
    return module


class PaperReaderTest(unittest.TestCase):
    def setUp(self):
        self.reader = load()
        self.blocks = self.reader.parse(DOCUMENT)

    def test_outline_lists_sections_and_skips_navigation(self):
        titles = [title for _, _, title in self.reader.outline(self.blocks)]
        self.assertEqual(titles, ["Abstract", "1 Introduction", "2 Results", "2.1 Baseline fit", "2.2 Goodness of fit", "3 Conclusions"])
        self.assertFalse(any("Menu" in text for _, _, text in self.blocks))
        self.assertFalse(any("color" in text for _, _, text in self.blocks))

    def test_section_by_title_stops_at_the_next_section_of_the_same_level(self):
        text = " ".join(t for _, _, t in self.reader.section(self.blocks, "results"))
        self.assertIn("Baseline fit", text)
        self.assertIn("Goodness of fit", text)
        self.assertNotIn("The ruler works", text)

    def test_subsection_by_number_in_the_outline(self):
        text = " ".join(t for _, _, t in self.reader.section(self.blocks, "4"))
        self.assertIn("8.632", text)
        self.assertNotIn("acceptable", text)

    def test_a_number_inside_a_formula_is_readable(self):
        hits = [text for kind, _, text in self.blocks if kind == "text" and "8.632" in text]
        self.assertEqual(len(hits), 1)
        self.assertIn("D_H/r_d = 8.632 \\pm 0.098", hits[0])
        self.assertEqual(hits[0].count("D_H/r_d"), 1)

    def test_table_cells_are_kept(self):
        self.assertTrue(any("alpha" in text and "1.002" in text for _, _, text in self.blocks))

    def test_unknown_section_is_an_error(self):
        with self.assertRaises(SystemExit):
            self.reader.section(self.blocks, "no such section")

    def test_identifier_format(self):
        self.assertTrue(self.reader.ARXIV_ID.match("2503.14739v2"))
        self.assertTrue(self.reader.ARXIV_ID.match("astro-ph/0507263"))
        self.assertFalse(self.reader.ARXIV_ID.match("not-an-id"))


if __name__ == "__main__":
    unittest.main()
