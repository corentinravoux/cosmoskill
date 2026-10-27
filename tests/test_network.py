"""Without a route to arXiv the scripts stop at once; a slow arXiv is still retried. No network."""

import contextlib
import importlib.util
import io
import socket
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "skills" / "observational-cosmology" / "scripts"
DNS = urllib.error.URLError(socket.gaierror(-2, "Name or service not known"))


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class NetworkTest(unittest.TestCase):
    def setUp(self):
        self.verify = load("verify_sources")
        self.fetch = load("fetch_paper")
        self.sleeps = []
        self.stderr = io.StringIO()
        cache = tempfile.TemporaryDirectory()
        self.addCleanup(cache.cleanup)
        self.fetch.CACHE = Path(cache.name)
        for module in (self.fetch, self.verify):
            patcher = mock.patch.object(module.time, "sleep", self.sleeps.append)
            patcher.start()
            self.addCleanup(patcher.stop)

    def fail_with(self, module, error):
        patcher = mock.patch.object(module.urllib.request, "urlopen", side_effect=error)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_dns_failure_is_unreachable(self):
        self.assertTrue(self.verify.unreachable(DNS))

    def test_proxy_403_is_unreachable(self):
        self.assertTrue(self.verify.unreachable(urllib.error.HTTPError("u", 403, "Forbidden", {}, None)))

    def test_https_proxy_403_is_unreachable(self):
        # what urllib raises when a CONNECT proxy refuses the host
        tunnel = urllib.error.URLError(OSError("Tunnel connection failed: 403 Forbidden"))
        self.assertTrue(self.verify.unreachable(tunnel))

    def test_main_exits_3_when_the_body_cannot_be_read(self):
        self.fail_with(self.fetch, DNS)
        with mock.patch.object(sys, "argv", ["fetch_paper.py", "1807.06209", "--outline", "--refresh"]), \
                contextlib.redirect_stderr(self.stderr):
            self.assertEqual(self.fetch.main(), 3)
        self.assertEqual(self.sleeps, [])
        self.assertNotIn("\n3\n", self.stderr.getvalue())

    def test_timeout_is_not_unreachable(self):
        self.assertFalse(self.verify.unreachable(TimeoutError()))
        self.assertFalse(self.verify.unreachable(urllib.error.URLError(TimeoutError())))

    def test_abstracts_stop_at_once_without_network(self):
        self.fail_with(self.fetch, DNS)
        with contextlib.redirect_stderr(self.stderr):
            self.assertEqual(self.fetch.abstracts(["1807.06209"]), 3)
        self.assertEqual(self.sleeps, [])
        self.assertIn("https://arxiv.org/abs/1807.06209", self.stderr.getvalue())

    def test_download_stops_at_once_without_network(self):
        self.fail_with(self.fetch, DNS)
        with contextlib.redirect_stderr(self.stderr), self.assertRaises(SystemExit) as caught:
            self.fetch.download("1807.06209", refresh=True)
        self.assertEqual(caught.exception.code, 3)
        self.assertEqual(self.sleeps, [])
        self.assertIn("https://arxiv.org/abs/1807.06209", self.stderr.getvalue())

    def test_query_stops_at_once_without_network(self):
        self.fail_with(self.verify, DNS)
        with contextlib.redirect_stderr(self.stderr), self.assertRaises(SystemExit) as caught:
            self.verify.query(["1807.06209"])
        self.assertEqual(caught.exception.code, 3)
        self.assertEqual(self.sleeps, [])
        self.assertIn("--offline", self.stderr.getvalue())

    def test_a_timeout_still_retries(self):
        self.fail_with(self.fetch, TimeoutError())
        self.fetch.ATTEMPTS = 1
        with contextlib.redirect_stderr(self.stderr):
            self.assertEqual(self.fetch.abstracts(["1807.06209"]), 2)
        self.assertEqual(len(self.sleeps), 3)


if __name__ == "__main__":
    unittest.main()
