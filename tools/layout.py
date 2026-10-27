"""Where the plugin lives in the repository.

Anthropic's directory scans the folder that holds `.claude-plugin/plugin.json`,
so the plugin sits in `plugin/` and the development material (docs, tests,
tools, releases) stays at the root, outside that scan. Before 1.0.3 the skills
were in `skills/` at the root; `skills_dir_at` lets the tools compare a ref
from before the move with the current layout.

Standard library only.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

PLUGIN = "plugin"
SKILLS = "plugin/skills"
PRE_MOVE_SKILLS = "skills"


def skills_dir_at(repo: Path, ref: str | None) -> str:
    """Return the skills folder, relative to the repository, at a git ref (the working tree when ref is None)."""
    if ref is None:
        return SKILLS
    found = subprocess.run(["git", "-C", str(repo), "cat-file", "-e", f"{ref}:{SKILLS}"], capture_output=True)
    return SKILLS if found.returncode == 0 else PRE_MOVE_SKILLS
