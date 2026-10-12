#!/usr/bin/env python3
"""Check the shape of the package: names, descriptions, file maps, counts.

Fails when

  - a skill directory name differs from the `name` of its SKILL.md;
  - a description does not start with "Use when" or exceeds 1,024 characters;
  - a SKILL.md exceeds the size kept by the harness after compaction;
  - a file named in a SKILL.md (`references/...`) does not exist;
  - a sibling skill named in a SKILL.md does not exist;
  - a skill lacks one of the standard reference files or its sources.tsv;
  - the README's source count for a skill differs from its sources.tsv;
  - the plugin manifests are not valid JSON or lack a required key.

    python3 tools/check_structure.py

Standard library only. Exit status 1 if anything is wrong.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
HUB = "observational-cosmology"
STANDARD = ["physics-and-methods.md", "surveys-and-data.md", "results.md", "systematics.md", "open-questions.md"]
MAX_DESCRIPTION = 1024
# The harness keeps the first 5,000 tokens of a skill after compaction; at
# about three characters per token for this kind of text, stay below that.
MAX_SKILL_CHARS = 15000

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FILE_REF = re.compile(r"`(references/[A-Za-z0-9_.\-/]+)`")
SKILL_REF = re.compile(r"`((?:cosmoskill:)?(?:cosmo-[a-z0-9\-]+|observational-cosmology))`")


def frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER.match(text)
    fields: dict[str, str] = {}
    if match:
        for line in match.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
    return fields


def check() -> list[str]:
    problems: list[str] = []
    names = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    counts: dict[str, int] = {}

    for name in names:
        skill = SKILLS / name
        skill_md = skill / "SKILL.md"
        if not skill_md.is_file():
            problems.append(f"{name}: no SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        fields = frontmatter(text)
        if fields.get("name") != name:
            problems.append(f"{name}: frontmatter name is {fields.get('name')!r}")
        description = fields.get("description", "")
        if not description.startswith("Use when"):
            problems.append(f"{name}: description does not start with 'Use when'")
        if len(description) > MAX_DESCRIPTION:
            problems.append(f"{name}: description has {len(description)} characters (limit {MAX_DESCRIPTION})")
        if len(text) > MAX_SKILL_CHARS:
            problems.append(f"{name}: SKILL.md has {len(text)} characters (limit {MAX_SKILL_CHARS})")
        for reference in sorted(set(FILE_REF.findall(text))):
            if "<" in reference or "*" in reference:
                continue
            if not (skill / reference).exists():
                problems.append(f"{name}: SKILL.md names {reference}, which does not exist")
        for sibling in sorted(set(SKILL_REF.findall(text))):
            sibling = sibling.removeprefix("cosmoskill:")
            if sibling not in names:
                problems.append(f"{name}: SKILL.md names the skill {sibling}, which does not exist")
        sources = skill / "references" / "sources.tsv"
        if not sources.is_file():
            problems.append(f"{name}: no references/sources.tsv")
        else:
            counts[name] = sum(1 for _ in sources.open(encoding="utf-8")) - 1
        if name != HUB:
            for standard in STANDARD:
                if not (skill / "references" / standard).is_file():
                    problems.append(f"{name}: missing references/{standard}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    listed = dict(re.findall(r"^\| `([a-z0-9\-]+)` \|.*\| (\d+) \|$", readme, re.M))
    for name in names:
        if name not in listed:
            problems.append(f"README.md: no row for {name}")
        elif name in counts and int(listed[name]) != counts[name]:
            problems.append(f"README.md: {name} listed with {listed[name]} sources, sources.tsv has {counts[name]}")
    for name in listed:
        if name not in names:
            problems.append(f"README.md: row for {name}, which is not a skill")
    total = re.search(r"([\d,]+) bibliography rows", readme)
    if total and int(total.group(1).replace(",", "")) != sum(counts.values()):
        problems.append(f"README.md: says {total.group(1)} bibliography rows, the files hold {sum(counts.values())}")

    for manifest, required in ((".claude-plugin/plugin.json", ["name"]),
                               (".claude-plugin/marketplace.json", ["name", "owner", "plugins"])):
        path = ROOT / manifest
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            problems.append(f"{manifest}: {error}")
            continue
        for key in required:
            if key not in data:
                problems.append(f"{manifest}: missing key {key!r}")
    if not (ROOT / "LICENSE").is_file():
        problems.append("LICENSE: missing")
    return problems


def main() -> int:
    problems = check()
    for problem in problems:
        print(problem)
    print(f"{len(problems)} structural problem(s)", file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
