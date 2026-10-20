"""Shared helpers for the layer tests: a fixture base selected with COSMOSKILL_BASE, a fixture layer, runs.

The fixture base in `tests/fixtures/base/<state>/` stores its skill file as
`SKILL.fixture.md`, so that no checkout of the package lists the fixture as
a skill; `base()` copies it to a temporary package and names it `SKILL.md`.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "skills" / "observational-cosmology" / "scripts"
FIXTURES = ROOT / "tests" / "fixtures"


def base(tmp, state):
    """Copy the fixture base `before` or `after` to <tmp>/<state>/skills and return that directory."""
    skills = Path(tmp) / state / "skills"
    shutil.copytree(FIXTURES / "base" / state, skills)
    for path in skills.glob("*/SKILL.fixture.md"):
        path.rename(path.with_name("SKILL.md"))
    return skills


def layer(tmp, name="v1"):
    """Copy a fixture layer to <tmp>/home and return it."""
    home = Path(tmp) / "home"
    shutil.copytree(FIXTURES / "layers" / name, home)
    return home


def run(script, *arguments, home, skills=None, cwd=None, cache=None):
    environment = dict(os.environ, COSMOSKILL_HOME=str(home))
    environment.pop("COSMOSKILL_BASE", None)
    if skills is not None:
        environment["COSMOSKILL_BASE"] = str(skills)
    if cache is not None:
        environment["XDG_CACHE_HOME"] = str(cache)
    return subprocess.run([sys.executable, str(SCRIPTS / script), *arguments], capture_output=True, text=True,
                          env=environment, cwd=cwd or Path(home).parent)


def snapshot(*roots):
    """Return {path: bytes} of every file under the roots, to show that a command wrote nothing."""
    return {str(path): path.read_bytes() for root in roots for path in sorted(Path(root).rglob("*")) if path.is_file()}
