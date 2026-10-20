"""The release manifest lists the added, reworded, moved and retired keys between two refs (layers-v1, section 3)."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from layer_fixtures import ROOT, base

TOOL = ROOT / "tools" / "make_release_manifest.py"


class ManifestTest(unittest.TestCase):
    def test_manifest_between_the_fixture_bases(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            shutil.copytree(base(tmp, "before"), repo / "skills")
            git = ["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@example.org"]
            subprocess.run(git + ["init", "-q"], check=True)
            subprocess.run(git + ["add", "-A"], check=True)
            subprocess.run(git + ["commit", "-q", "-m", "before"], check=True)
            shutil.rmtree(repo / "skills")
            shutil.copytree(base(tmp, "after"), repo / "skills")

            def make(*options):
                return subprocess.run([sys.executable, str(TOOL), "--repo", str(repo), "--from", "HEAD", *options],
                                      capture_output=True, text=True)

            result = make("--version", "9.9.9")
            self.assertEqual(result.returncode, 0, result.stderr)
            lines = (repo / "releases" / "9.9.9.tsv").read_text(encoding="utf-8").splitlines()
            self.assertEqual(lines[0].split("\t"), ["skill", "file", "key", "change", "replaced_by", "fingerprint"])
            rows = {tuple(line.split("\t")[1:3]): line.split("\t") for line in lines[1:]}
            self.assertEqual(rows[("results", "optical-depth-tau")][3:], ["changed", "", "f66a40618008"])
            self.assertEqual(rows[("results", "cluster-mass-old")][3:],
                             ["moved", "results#cluster-mass-calibration", "a4939b344c53"])
            self.assertEqual(rows[("results", "sn-host-step")][3:5], ["retired", ""])
            self.assertEqual(rows[("results", "neutrino-mass")][3], "added")
            self.assertEqual(rows[("results", "cluster-mass-calibration")][3], "added")
            self.assertNotIn(("results", "introduction"), rows)
            self.assertNotIn(("results", "low-ell-likelihoods"), rows)
            self.assertEqual(rows[("results", "cmb-lensing-amplitude")][3], "retired")
            self.assertIn("cmb-lensing-amplitude is gone and not listed", result.stderr)
            self.assertNotEqual(make("--version", "9.9.9").returncode, 0)  # kept unless --force

            subprocess.run(git + ["add", "-A"], check=True)
            subprocess.run(git + ["commit", "-q", "-m", "after"], check=True)
            between = make("--to", "HEAD", "--version", "9.9.9", "--force")
            self.assertIn("0 added, 0 changed, 0 moved, 0 retired", between.stdout)
            again = subprocess.run([sys.executable, str(TOOL), "--repo", str(repo), "--from", "HEAD~1", "--to", "HEAD",
                                    "--version", "9.9.9", "--force"], capture_output=True, text=True)
            self.assertEqual((repo / "releases" / "9.9.9.tsv").read_text(encoding="utf-8").splitlines(), lines)
            self.assertEqual(again.returncode, 0, again.stderr)


if __name__ == "__main__":
    unittest.main()
