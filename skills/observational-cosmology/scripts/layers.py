#!/usr/bin/env python3
"""Find and print the local layers of a cosmoskill skill.

The package is the base layer. A researcher can add two more, without
editing the package:

  personal   $COSMOSKILL_HOME, default ~/.cosmoskill/
  project    .cosmoskill/ in the current directory or one of its parents

A layer holds a `profile.md` and, per skill, a `notes.md`:

  <layer>/profile.md
  <layer>/<skill>/notes.md      sections "## <file>#<key>" or "## general"

Usage:

  layers.py <skill>             print what the layers say for that skill
  layers.py <skill> --json      the same, machine-readable
  layers.py init [--project]    create an empty layer with a profile template
  layers.py check               list notes attached to keys the base lacks

With no layer present, `layers.py <skill>` prints nothing and exits 0.
The project layer is listed before the personal one. Standard library only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

SKILLS = Path(__file__).resolve().parent.parent.parent
LAYER_DIR = ".cosmoskill"
PROFILE = "profile.md"
NOTES = "notes.md"
MAX_PROFILE_LINES = 60
KEY_LINE = re.compile(r"^<!-- key: ([a-z0-9][a-z0-9\-]*) -->$")
NOTE_HEADING = re.compile(r"^## +(.+?)\s*$")
ATTACH = re.compile(r"^(?:([A-Za-z0-9\-]+)#)?([a-z0-9][a-z0-9\-]*)$")

PROFILE_TEMPLATE = """# Profile

Free text. Two optional lines are read by the skills:

home-domains:
conventions:

`home-domains` lists the skills of your own field, separated by commas, for
example `cosmo-lyman-alpha, cosmo-peculiar-velocities`. There, the assistant
may skip the orientation it would give an outsider.

`conventions` states what you want every answer to follow, for example
`k in h/Mpc; distances in Mpc/h; fiducial Planck 2018`.

Anything else you write here is shown to the assistant as context: your
collaborations, the analysis you are working on, what you already know.
"""

NOTES_HELP = """A note is a section of `<layer>/<skill>/notes.md`:

    ## results#cosmology-from-p1d
    The DR2 measurement is in collaboration review; do not quote DR1 as final.

    ## general
    I work on the QMLE estimator: skip its introduction.

The heading names the base section the note attaches to, as
`<file>#<key>`, where the key is the comment under that section's heading in
the package. `## general` attaches to the skill as a whole.
"""


def personal_layer() -> Path:
    return Path(os.environ.get("COSMOSKILL_HOME") or Path.home() / LAYER_DIR).expanduser()


def project_layer(start: Path | None = None) -> Path | None:
    here = (start or Path.cwd()).resolve()
    personal = personal_layer().resolve()
    for folder in [here, *here.parents]:
        candidate = folder / LAYER_DIR
        if candidate.is_dir() and candidate.resolve() != personal:
            return candidate
    return None


def layers() -> list[tuple[str, Path]]:
    found = []
    project = project_layer()
    if project:
        found.append(("project", project))
    personal = personal_layer()
    if personal.is_dir():
        found.append(("personal", personal))
    return found


def read_profile(layer: Path) -> dict:
    path = layer / PROFILE
    if not path.is_file():
        return {}
    text = path.read_text(encoding="utf-8")
    settings = {}
    for line in text.splitlines():
        for name in ("home-domains", "conventions"):
            if line.lower().startswith(name + ":"):
                value = line.split(":", 1)[1].strip()
                if value:
                    settings[name] = value
    return {"path": str(path), "settings": settings, "text": text}


def read_notes(layer: Path, skill: str) -> list[dict]:
    path = layer / skill / NOTES
    if not path.is_file():
        return []
    notes, current = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        heading = NOTE_HEADING.match(line)
        if heading:
            current = {"attach": heading.group(1), "text": []}
            notes.append(current)
        elif current is not None:
            current["text"].append(line)
    for note in notes:
        note["text"] = "\n".join(note["text"]).strip()
    return [note for note in notes if note["text"]]


def base_keys(skill: str) -> dict[str, set[str]]:
    """Return {file stem: keys} for a base skill."""
    keys: dict[str, set[str]] = {}
    folder = SKILLS / skill
    files = [folder / "SKILL.md"] + sorted(folder.glob("references/*.md")) + sorted(folder.glob("deep/*.md"))
    for path in files:
        if path.is_file():
            stem = "skill" if path.name == "SKILL.md" else path.stem
            keys[stem] = {m.group(1) for m in map(KEY_LINE.match, path.read_text(encoding="utf-8").splitlines()) if m}
    return keys


def attached(note: dict, keys: dict[str, set[str]]) -> bool:
    if note["attach"].lower() == "general":
        return True
    match = ATTACH.match(note["attach"])
    if not match:
        return False
    stem, key = match.groups()
    if stem:
        return key in keys.get(stem, set())
    return any(key in found for found in keys.values())


def clean(name: str) -> str:
    return name.split(":", 1)[1] if name.startswith("cosmoskill:") else name


def show(skill: str, as_json: bool) -> int:
    skill = clean(skill)
    keys = base_keys(skill)
    report = []
    for kind, layer in layers():
        profile = read_profile(layer)
        notes = read_notes(layer, skill)
        if not profile and not notes:
            continue
        home = [clean(name.strip()) for name in profile.get("settings", {}).get("home-domains", "").split(",") if name.strip()]
        for note in notes:
            note["known_key"] = attached(note, keys)
        report.append({"layer": kind, "path": str(layer), "profile": profile, "home_domain": skill in home, "notes": notes})
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    for entry in report:
        print(f"=== {entry['layer']} layer: {entry['path']}")
        profile = entry["profile"]
        if profile:
            for name, value in profile["settings"].items():
                print(f"{name}: {value}")
            if entry["home_domain"]:
                print(f"{skill} is a home domain of this researcher: skip the orientation an outsider needs.")
            lines = profile["text"].splitlines()
            if profile["text"].strip() != PROFILE_TEMPLATE.strip():
                print(f"--- profile ({profile['path']})")
                print("\n".join(lines[:MAX_PROFILE_LINES]))
                if len(lines) > MAX_PROFILE_LINES:
                    print(f"... {len(lines) - MAX_PROFILE_LINES} more lines in the file")
        for note in entry["notes"]:
            flag = "" if note["known_key"] else "  (this key is not in the package: the note may be out of date)"
            print(f"--- {entry['layer']} note on {skill}/{note['attach']}{flag}")
            print(note["text"])
        print()
    return 0


def init(project: bool) -> int:
    layer = (Path.cwd() / LAYER_DIR) if project else personal_layer()
    layer.mkdir(parents=True, exist_ok=True)
    profile = layer / PROFILE
    if profile.exists():
        print(f"kept    {profile}")
    else:
        profile.write_text(PROFILE_TEMPLATE, encoding="utf-8")
        print(f"created {profile}")
    readme = layer / "README.md"
    if not readme.exists():
        readme.write_text("# cosmoskill local layer\n\n" + NOTES_HELP, encoding="utf-8")
        print(f"created {readme}")
    return 0


def check() -> int:
    orphans = 0
    for kind, layer in layers():
        for notes_file in sorted(layer.glob(f"*/{NOTES}")):
            skill = notes_file.parent.name
            if not (SKILLS / skill).is_dir():
                print(f"{kind}: {notes_file}: no skill named {skill} in the package")
                orphans += 1
                continue
            keys = base_keys(skill)
            for note in read_notes(layer, skill):
                if not attached(note, keys):
                    print(f"{kind}: {notes_file}: note on '{note['attach']}' attaches to no section of {skill}")
                    orphans += 1
    print(f"{orphans} note(s) attached to nothing", file=sys.stderr)
    return 1 if orphans else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("target", help="a skill name, or 'init', or 'check'")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--project", action="store_true", help="with init: create ./.cosmoskill instead of the personal layer")
    args = parser.parse_args()
    if args.target == "init":
        return init(args.project)
    if args.target == "check":
        return check()
    return show(args.target, args.json)


if __name__ == "__main__":
    sys.exit(main())
