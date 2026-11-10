#!/usr/bin/env python3
"""Find, print and extend the local layers of a cosmoskill skill.

The package is the base layer. A researcher can add two more, without
editing the package:

  personal   $COSMOSKILL_HOME, default ~/.cosmoskill/
  project    .cosmoskill/ in the current directory or one of its parents

A layer holds a `profile.md` and, per skill, notes, papers and dossiers:

  <layer>/profile.md
  <layer>/<skill>/notes.md          sections "## <file>#<key>" or "## general"
  <layer>/<skill>/sources.tsv       the researcher's own papers, same columns
                                    as the package's bibliography
  <layer>/<skill>/deep/<name>.md    the researcher's own dossiers
  <layer>/<skill>/private/...       the same files, never promoted to the package

A note is an entry of one of three modes (docs/layers-v1.md): `add` (the
default), `override` (replaces the base section for this researcher; an
answer shows both) or `suppress` (the base section is skipped). Each entry
records `base:`, the fingerprint of the section it was written against, so
that `sync_layers.py` can report a base section that changed under it.

Reading:

  layers.py <skill>                 print what the layers say for that skill
  layers.py <skill> --json          the same, machine-readable
  layers.py resolve <skill> <file>[#<key>] [--json]
                                    the base text with every entry that applies
  layers.py check [--online]        notes attached to keys the base lacks,
                                    malformed rows, papers cited without a
                                    row; --online compares rows with arXiv

Writing, in the personal layer unless --project is given:

  layers.py init                    create a layer with a profile template
  layers.py note <skill> <file>#<key> <text>
  layers.py note <skill> general <text>
  layers.py override <skill> <file>#<key> <text>
  layers.py suppress <skill> <file>#<key> <reason>
  layers.py source <skill> <arXiv id> --role <role> [--key <key>]
  layers.py found <skill> <doi:...|arXiv id> --via <via>
  layers.py dossier <skill> <name>
  layers.py progress <skill> [--clear]
                                    the state of an extension run of
                                    cosmoskill-refine, in <skill>/_progress.md:
                                    created when absent, printed when a run
                                    is paused, deleted with --clear
  layers.py sweep <skill> [--json]  how far the skill was swept for newer
                                    papers: its snapshot, the package's sweep
                                    record, each layer's, and the date an
                                    extension run starts from
  layers.py sweep <skill> --record --to <YYYY-MM-DD> --adapters <list>
                                    record in the layer that the skill was
                                    swept up to that date with those adapters

`--via valency|arxiv-mcp|web` on `note`, `override`, `suppress` and `source`
records how the paper behind an entry was found: a `via:` line in the entry,
and for `source` a row of `<layer>/<skill>/found-via.tsv` (columns id, via,
found). `found` records it for a row already in the layer's `sources.tsv`,
such as a `doi:` row written by hand.

`source` takes title and first author from arXiv and writes nothing when
arXiv cannot be reached: a bibliography row is never written from memory.
`note`, `override` and `suppress` stamp the entry with the fingerprint of
the section; after an update of the package, `sync_layers.py` reports the
entries whose section changed, moved or was retired. `promote.py` moves an
entry into the package's working tree for its owner to review.

With no layer present, `layers.py <skill>` prints nothing and exits 0.
The project layer is listed before the personal one. COSMOSKILL_BASE, a
`skills/` directory, replaces the package's own as the base (tests, or a
layer checked against another checkout). Standard library only.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_sources as bibliography  # noqa: E402

SKILLS = Path(os.environ.get("COSMOSKILL_BASE") or Path(__file__).resolve().parent.parent.parent).expanduser()
LAYER_DIR = ".cosmoskill"
PROFILE = "profile.md"
NOTES = "notes.md"
SOURCES = "sources.tsv"
DEEP = "deep"
PRIVATE = "private"
MODES = ("add", "override", "suppress")
RETIRED = "retired-keys.tsv"
VIA = ("valency", "arxiv-mcp", "web")
FOUND_VIA = "found-via.tsv"
FOUND_VIA_COLUMNS = ["id", "via", "found"]
PROGRESS = "_progress.md"
SWEEPS = "sweeps.tsv"
SWEEP_COLUMNS = ["skill", "swept_to", "adapters", "recorded"]
HUB = "observational-cosmology"
SNAPSHOT = re.compile(r"Snapshot (\d{4}-\d{2}-\d{2})")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RETIRED_COLUMNS = ["file", "key", "retired_on", "replaced_by", "reason"]
STAMP = re.compile(r"^[0-9a-f]{12}$")
MAX_PROFILE_LINES = 60
# Soft limits of `check` (warnings, not failures): every answer in a skill reads
# all its notes, so a long note or many `general` notes cost every question.
NOTE_WARN_LINES = 4
GENERAL_WARN_COUNT = 3
KEY_LINE = re.compile(r"^<!-- key: ([a-z0-9][a-z0-9\-]*) -->$")
NOTE_HEADING = re.compile(r"^## +(.+?)\s*$")
ANY_HEADING = re.compile(r"^(#{1,6}) +(.+?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
META = re.compile(r"^(mode|base|private|via):\s*(.*?)\s*$", re.IGNORECASE)
ATTACH = re.compile(r"^(?:([A-Za-z0-9\-]+)#)?([a-z0-9][a-z0-9\-]*)$")
SLUG = re.compile(r"^[a-z0-9][a-z0-9\-]*$")

PROFILE_TEMPLATE = """# Profile

Free text. Two optional lines are read by the skills:

home-domains:
conventions:

`home-domains` lists the skills of your own field, separated by commas, for
example `cosmo-weak-lensing, cosmo-cmb-lss-cross-correlations`. There, the assistant
may skip the orientation it would give an outsider.

`conventions` states what you want every answer to follow, for example
`k in h/Mpc; distances in Mpc/h; fiducial Planck 2018`.

Anything else you write here is shown to the assistant as context: your
collaborations, the analysis you are working on, what you already know.
"""

LAYER_HELP = """A layer holds, per skill of the package, three things.

**Notes**, in `<skill>/notes.md`, one section each:

    ## results#the-cmb-reference-values
    Quote every S8 difference against both CMB references named here.

    ## general
    I work on shear calibration: skip its introduction.

The heading names the section of the package the note attaches to, as
`<file>#<key>`, where the key is the comment under that section's heading in
the package. `## general` attaches to the skill as a whole.

**Papers**, in `<skill>/sources.tsv`: your own papers and the ones you rely
on that the package does not cite. Same columns as the package's
bibliography. Add a row with `layers.py source <skill> <arXiv id> --role
<role>`: title and author then come from arXiv.

**Provenance**, in `<skill>/found-via.tsv`: how each paper you added was
found (`valency`, `arxiv-mcp` or `web`), written by `--via` on `source` or
by `layers.py found`. A note written with `--via` carries a `via:` line.

**Dossiers**, in `<skill>/deep/<name>.md`: a subject you know in more depth
than the package holds. Start one with `layers.py dossier <skill> <name>`.

`layers.py check` lists what no longer attaches after an update of the
package.
"""

DOSSIER_TEMPLATE = """# {title}

Scope: one sentence saying what this dossier answers that the package does not.
Snapshot: {date}.

## How it is done

Methods and derivations. Give an equation as its paper writes it, with the
paper and the equation number.

## Choices and what they cost

The variants of the method, what each buys, who uses which.

## Numbers

| Quantity | Value | Source | Place read |
|---|---|---|---|

## What goes wrong

Failure modes and the tests that catch them.

## Reading list

Papers by role, each cited as `arXiv:<id>` with a row in `../sources.tsv`.

## Not verified

What is written here from experience and not from a paper.
"""


PROGRESS_TEMPLATE = """# Extension run: {skill}

Started: {started}
Start date: {start}
Adapters:
Stopped:

The state of an extension run of cosmoskill-refine. A paused run resumes
from here. This file is not read by `layers.py check`, by answers or by
`promote.py`; `layers.py progress {skill} --clear` deletes it at the end.

## Candidates

| Paper | Title | Found via | Status | Note |
|---|---|---|---|---|

Status: one of `found`, `read`, `proposed`, `accepted`, `rejected`, `skipped`.

## Alerts read

Papers returned by `check_alerts`, written here as soon as they arrive.

## Left to do

"""


def personal_layer() -> Path:
    return Path(os.environ.get("COSMOSKILL_HOME") or Path.home() / LAYER_DIR).expanduser()


def project_layer(start: Path | None = None) -> Path | None:
    here = (start or Path.cwd()).resolve()
    # The home directory's .cosmoskill is a personal layer, never a project one,
    # even when COSMOSKILL_HOME points elsewhere.
    personal = {personal_layer().resolve(), (Path.home() / LAYER_DIR).resolve()}
    for folder in [here, *here.parents]:
        candidate = folder / LAYER_DIR
        if candidate.is_dir() and candidate.resolve() not in personal:
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


def target_layer(project: bool) -> tuple[str, Path]:
    """The layer a writing command writes to."""
    if project:
        return "project", project_layer() or Path.cwd() / LAYER_DIR
    return "personal", personal_layer()


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


def skill_folders(layer: Path, skill: str) -> list[tuple[Path, bool]]:
    """The folders of a layer that hold a skill's entries, with their privacy."""
    return [(layer / skill, False), (layer / skill / PRIVATE, True)]


def parse_entries(path: Path, private: bool = False) -> list[dict]:
    """Return the entries of one notes file, with the line of each heading."""
    entries, current = [], None
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        heading = NOTE_HEADING.match(line)
        if heading:
            current = {"attach": heading.group(1), "mode": "add", "base": "", "via": "", "private": private,
                       "path": str(path), "line": number, "text": [], "in_meta": True}
            entries.append(current)
            continue
        if current is None:
            continue
        meta = META.match(line) if current["in_meta"] else None
        if meta:
            name, value = meta.group(1).lower(), meta.group(2)
            if name == "mode":
                current["mode"] = value.lower()
            elif name == "base":
                current["base"] = value.lower()
            elif name == "via":
                current["via"] = value.lower()
            elif name == "private":
                current["private"] = current["private"] or value.lower() in ("yes", "true")
            continue
        current["in_meta"] = False
        current["text"].append(line)
    for entry in entries:
        entry.pop("in_meta")
        entry["text"] = "\n".join(entry["text"]).strip()
    return [entry for entry in entries if entry["text"] or entry["mode"] == "suppress"]


def read_notes(layer: Path, skill: str) -> list[dict]:
    notes = []
    for folder, private in skill_folders(layer, skill):
        if (folder / NOTES).is_file():
            notes += parse_entries(folder / NOTES, private)
    return notes


def read_sources(layer: Path, skill: str) -> tuple[list[dict], list[str]]:
    """Return (rows, problems) of a layer's own bibliography for a skill."""
    rows, problems = [], []
    for folder, private in skill_folders(layer, skill):
        if (folder / SOURCES).is_file():
            found, issues = bibliography.read_sources(folder / SOURCES)
            for row in found:
                row["_private"] = private
            rows += found
            problems += issues
    return rows, problems


def read_found_via(layer: Path, skill: str) -> tuple[list[dict], list[str]]:
    """Return (rows, problems) of a layer's `found-via.tsv` for a skill; ids are lower-cased."""
    rows, problems = [], []
    for folder, private in skill_folders(layer, skill):
        path = folder / FOUND_VIA
        if not path.is_file():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].split("\t") != FOUND_VIA_COLUMNS:
            problems.append(f"{path}: header must be {', '.join(FOUND_VIA_COLUMNS)}")
            continue
        for number, line in enumerate(lines[1:], start=2):
            if not line.strip():
                continue
            fields = [field.strip() for field in line.split("\t")]
            if len(fields) != len(FOUND_VIA_COLUMNS):
                problems.append(f"{path}:{number}: {len(fields)} columns, expected {len(FOUND_VIA_COLUMNS)}")
                continue
            row = dict(zip(FOUND_VIA_COLUMNS, fields))
            row["id"], row["_path"], row["_line"], row["_private"] = row["id"].lower(), str(path), number, private
            if row["via"] not in VIA:
                problems.append(f"{path}:{number}: via '{row['via']}' is not one of {', '.join(VIA)}")
            if not ISO_DATE.match(row["found"]):
                problems.append(f"{path}:{number}: found '{row['found']}' is not a YYYY-MM-DD date")
            rows.append(row)
    return rows, problems


def record_found(path: Path, ident: str, via: str) -> None:
    """Append one provenance row, writing the header when the file is new."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.is_file():
        path.write_text("\t".join(FOUND_VIA_COLUMNS) + "\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\t".join([ident, via, datetime.date.today().isoformat()]) + "\n")


def read_dossiers(layer: Path, skill: str) -> list[dict]:
    dossiers = []
    for folder, private in skill_folders(layer, skill):
        for path in sorted((folder / DEEP).glob("*.md")):
            lines = path.read_text(encoding="utf-8").splitlines()
            title = next((line[2:].strip() for line in lines if line.startswith("# ")), path.stem)
            scope = next((line.split(":", 1)[1].strip() for line in lines if line.lower().startswith("scope:")), "")
            marked = any(line.lower().replace(" ", "") in ("private:yes", "private:true") for line in lines[:12])
            dossiers.append({"name": path.stem, "path": str(path), "title": title, "scope": scope,
                             "lines": len(lines), "private": private or marked})
    return dossiers


def sections(text: str) -> list[dict]:
    """Return the keyed sections of a Markdown text.

    Each section has its key, heading, level, `own` text (to the next heading
    of any level) and `full` text (to the next heading of the same or a
    higher level). Headings inside fenced code are ignored.
    """
    lines = text.split("\n")
    marks, fenced = [], False
    for index, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
            continue
        match = None if fenced else ANY_HEADING.match(line)
        if match:
            key = KEY_LINE.match(lines[index + 1].strip()) if index + 1 < len(lines) else None
            marks.append((index, len(match.group(1)), match.group(2), key.group(1) if key else None))

    def body(start: int, end: int) -> str:
        kept = [line.rstrip() for line in lines[start:end]]
        while kept and not kept[-1]:
            kept.pop()
        while kept and not kept[0]:
            kept.pop(0)
        return "\n".join(kept)

    found = []
    for position, (index, level, heading, key) in enumerate(marks):
        if key is None:
            continue
        later = marks[position + 1:]
        own_end = later[0][0] if later else len(lines)
        full_end = next((mark[0] for mark in later if mark[1] <= level), len(lines))
        found.append({"key": key, "heading": heading, "level": level, "line": lines[index].rstrip(),
                      "own": body(index + 2, own_end), "full": body(index + 2, full_end)})
    return found


def fingerprint(section: dict) -> str:
    """First 12 hex digits of the SHA-256 of a section's heading line and full text.

    The full text runs to the next heading of the same or a higher level. Key
    lines (the section's own and those of its subsections) are left out, so
    that giving a subsection its key does not change the fingerprint; line
    ends are stripped and leading or trailing blank lines dropped.
    """
    text = "\n".join(line for line in section["full"].split("\n") if not KEY_LINE.match(line.strip()))
    return hashlib.sha256((section["line"] + "\n" + text).encode("utf-8")).hexdigest()[:12]


def base_file(skill: str, stem: str) -> Path | None:
    folder = SKILLS / skill
    candidates = [folder / "SKILL.md"] if stem == "skill" else [folder / "references" / f"{stem}.md",
                                                               folder / DEEP / f"{stem}.md"]
    return next((path for path in candidates if path.is_file()), None)


def base_sections(skill: str) -> dict[str, dict[str, dict]]:
    """Return {file stem: {key: section}} for a base skill."""
    found = {}
    for stem in base_keys(skill):
        path = base_file(skill, stem)
        if path is not None:
            found[stem] = {section["key"]: section for section in sections(path.read_text(encoding="utf-8"))}
    return found


def locate(attach: str, keyed: dict[str, dict]) -> tuple[str | None, str | None]:
    """Return (stem, key) of an entry's section; the stem is looked up when the entry names none."""
    match = ATTACH.match(attach)
    if not match:
        return None, None
    stem, key = match.groups()
    if stem:
        return stem, key
    return next((name for name, found in keyed.items() if key in found), None), key


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


def base_ids(skill: str) -> dict[str, str]:
    """Return {identifier: key} of a base skill's bibliography."""
    path = SKILLS / skill / "references" / SOURCES
    if not path.is_file():
        return {}
    rows, _ = bibliography.read_sources(path)
    return {row["id"].lower(): row["key"] for row in rows}


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


def retired_keys(skill: str) -> dict[tuple[str, str], dict]:
    """Return {(file stem, key): row} of a base skill's `references/retired-keys.tsv`."""
    path = SKILLS / skill / "references" / RETIRED
    if not path.is_file():
        return {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].split("\t") != RETIRED_COLUMNS:
        raise SystemExit(f"{path}: header must be {', '.join(RETIRED_COLUMNS)}")
    found = {}
    for line in lines[1:]:
        fields = (line.split("\t") + [""] * len(RETIRED_COLUMNS))[:len(RETIRED_COLUMNS)]
        if fields[0] and fields[1]:
            found[(fields[0], fields[1])] = dict(zip(RETIRED_COLUMNS, (field.strip() for field in fields)))
    return found


def entry_status(entry: dict, keyed: dict[str, dict], retired: dict[tuple[str, str], dict]) -> dict:
    """Say where an entry stands against the base: ok, unstamped, changed, moved, retired, missing or malformed.

    Returns {"status", "stem", "key", "detail"}, plus "target" (`<file>#<key>`)
    for a moved entry, None when its replacement is not in the base.
    `general` entries attach to no section and have status "general".
    """
    if entry["attach"].lower() == "general":
        if entry["mode"] != "add":
            return {"status": "malformed", "stem": None, "key": None,
                    "detail": f"a {entry['mode']} entry needs a section, not 'general'"}
        return {"status": "general", "stem": None, "key": None, "detail": ""}
    if entry["mode"] not in MODES:
        return {"status": "malformed", "stem": None, "key": None,
                "detail": f"mode '{entry['mode']}' is not one of {', '.join(MODES)}"}
    if entry["base"] and not STAMP.match(entry["base"]):
        return {"status": "malformed", "stem": None, "key": None,
                "detail": f"base '{entry['base']}' is not a 12-digit fingerprint"}
    if not ATTACH.match(entry["attach"]):
        return {"status": "malformed", "stem": None, "key": None,
                "detail": f"heading '{entry['attach']}' is not <file>#<key> or 'general'"}
    stem, key = locate(entry["attach"], keyed)
    if stem is not None and key in keyed.get(stem, {}):
        if not entry["base"]:
            return {"status": "unstamped", "stem": stem, "key": key, "detail": "written before stamps"}
        if entry["base"] == fingerprint(keyed[stem][key]):
            return {"status": "ok", "stem": stem, "key": key, "detail": ""}
        return {"status": "changed", "stem": stem, "key": key, "detail": "base section changed since the entry was written"}
    row = retired.get((stem, key)) if stem else next((row for (_, name), row in retired.items() if name == key), None)
    if row is None:
        return {"status": "missing", "stem": stem, "key": key, "detail": "key absent and not listed as retired"}
    when = f"retired {row['retired_on']}" + (f": {row['reason']}" if row["reason"] else "")
    if not row["replaced_by"]:
        return {"status": "retired", "stem": row["file"], "key": key, "detail": when + "; no replacement"}
    target, seen = row["replaced_by"], set()
    while True:
        found = ATTACH.match(target)
        if not found or not found.group(1) or target in seen:
            return {"status": "moved", "stem": row["file"], "key": key, "target": None,
                    "detail": f"{when}; replacement '{row['replaced_by']}' not found in the base"}
        seen.add(target)
        new_stem, new_key = found.groups()
        if new_key in keyed.get(new_stem, {}):
            return {"status": "moved", "stem": row["file"], "key": key, "target": target, "detail": when}
        onward = retired.get((new_stem, new_key))
        if onward is None or not onward["replaced_by"]:
            return {"status": "moved", "stem": row["file"], "key": key, "target": None,
                    "detail": f"{when}; replacement '{target}' is not in the base"}
        target = onward["replaced_by"]


def clean(name: str) -> str:
    return name.split(":", 1)[1] if name.startswith("cosmoskill:") else name


def known_skill(name: str) -> str:
    skill = clean(name)
    if not (SKILLS / skill / "SKILL.md").is_file():
        raise SystemExit(f"no skill named {skill} in the package")
    return skill


def show(skill: str, as_json: bool) -> int:
    skill = clean(skill)
    keys = base_keys(skill)
    report = []
    for kind, layer in layers():
        profile = read_profile(layer)
        notes = read_notes(layer, skill)
        sources, _ = read_sources(layer, skill)
        dossiers = read_dossiers(layer, skill)
        if not (profile or notes or sources or dossiers):
            continue
        home = [clean(name.strip()) for name in profile.get("settings", {}).get("home-domains", "").split(",") if name.strip()]
        for note in notes:
            note["known_key"] = attached(note, keys)
        for row in sources:
            row.pop("_line", None)
        report.append({"layer": kind, "path": str(layer), "profile": profile, "home_domain": skill in home,
                       "notes": notes, "sources": sources, "dossiers": dossiers})
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    for entry in report:
        kind = entry["layer"]
        print(f"=== {kind} layer: {entry['path']}")
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
            flag += f" (found via {note['via']})" if note["via"] else ""
            if note["mode"] == "override":
                print(f"--- {kind} override of {skill}/{note['attach']}{flag}: replaces that section for this "
                      f"researcher; quote the package's value beside it, both labelled")
            elif note["mode"] == "suppress":
                print(f"--- {kind} suppress of {skill}/{note['attach']}{flag}: skip that section unless the "
                      f"question is about it")
            else:
                print(f"--- {kind} note on {skill}/{note['attach']}{flag}")
            if note["text"]:
                print(note["text"])
        if entry["sources"]:
            print(f"--- {kind} papers for {skill}: added by this researcher, not checked by the package. "
                  f"Read one before quoting it, and say it comes from the {kind} layer.")
            for row in entry["sources"]:
                ident = row["id"] if row["id"].lower().startswith("doi:") else f"arXiv:{row['id']}"
                print(f"{row['key']} | {ident} | {row['first_author']} {row['year']} | {row['role']} | {row['title']}")
        for dossier in entry["dossiers"]:
            print(f"--- {kind} dossier {skill}/{DEEP}/{dossier['name']}: {dossier['title']} ({dossier['lines']} lines)")
            if dossier["scope"]:
                print(f"Scope: {dossier['scope']}")
            print(f"Read {dossier['path']} when the question is about its subject. An answer drawn from it is "
                  f"level 3 and ends with [cosmoskill L3 · {kind} · {skill}/{DEEP}/{dossier['name']}].")
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
        readme.write_text("# cosmoskill local layer\n\n" + LAYER_HELP, encoding="utf-8")
        print(f"created {readme}")
    return 0


def add_note(skill: str, attach: str, text: str, project: bool, mode: str = "add", via: str = "") -> int:
    skill = known_skill(skill)
    keys = base_keys(skill)
    stamp = ""
    if attach.lower() == "general":
        if mode != "add":
            raise SystemExit(f"{mode} needs a section, <file>#<key>; 'general' takes notes only")
    else:
        match = ATTACH.match(attach)
        if not match or not match.group(1):
            raise SystemExit(f"'{attach}' is not <file>#<key> or 'general'")
        stem, key = match.groups()
        if stem not in keys:
            raise SystemExit(f"{skill} has no file '{stem}'; files: {', '.join(sorted(keys))}")
        if key not in keys[stem]:
            raise SystemExit(f"{skill}/{stem} has no section key '{key}'; keys: {', '.join(sorted(keys[stem]))}")
        stamp = fingerprint(base_sections(skill)[stem][key])
    if not text.strip():
        raise SystemExit("the reason is empty" if mode == "suppress" else f"the {mode if mode != 'add' else 'note'} is empty")
    kind, layer = target_layer(project)
    path = layer / skill / NOTES
    path.parent.mkdir(parents=True, exist_ok=True)
    before = path.read_text(encoding="utf-8") if path.is_file() else ""
    gap = "" if not before else ("\n" if before.endswith("\n") else "\n\n")
    meta = ((f"mode: {mode}\n" if mode != "add" else "") + (f"base: {stamp}\n" if stamp else "")
            + (f"via: {via}\n" if via else ""))
    path.write_text(f"{before}{gap}## {attach}\n{meta}{text.strip()} (noted {datetime.date.today().isoformat()})\n",
                    encoding="utf-8")
    print(f"{kind} {'note on' if mode == 'add' else mode + ' of'} {skill}/{attach} written to {path}")
    return 0


def rewrite_entry(entry: dict, attach: str | None = None, stamp: str | None = None) -> None:
    """Change the heading or the `base:` line of one entry, in place."""
    path = Path(entry["path"])
    lines = path.read_text(encoding="utf-8").split("\n")
    start = entry["line"]
    if attach is not None:
        lines[start] = f"## {attach}"
    if stamp is not None:
        index = start + 1
        while index < len(lines):
            meta = META.match(lines[index])
            if meta is None:
                lines.insert(index, f"base: {stamp}")
                break
            if meta.group(1).lower() == "base":
                lines[index] = f"base: {stamp}"
                break
            index += 1
        else:
            lines.insert(index, f"base: {stamp}")
    path.write_text("\n".join(lines), encoding="utf-8")


def resolve(skill: str, target: str, as_json: bool) -> int:
    """Print the base text of a file or section with every layer entry that applies."""
    skill = known_skill(skill)
    stem, _, wanted = target.partition("#")
    keyed = base_sections(skill)
    if stem not in keyed:
        raise SystemExit(f"{skill} has no file '{stem}'; files: {', '.join(sorted(keyed))}")
    if wanted and wanted not in keyed[stem]:
        raise SystemExit(f"{skill}/{stem} has no section key '{wanted}'")
    entries, general, unread = {}, [], []
    for kind, layer in layers():
        for entry in read_notes(layer, skill):
            entry["layer"] = kind
            if entry["attach"].lower() == "general":
                general.append(entry)
                continue
            where = locate(entry["attach"], keyed)
            if where[0] != stem or (wanted and where[1] != wanted):
                continue
            if entry["mode"] in MODES and where[1] in keyed[stem]:
                entries.setdefault(where[1], []).append(entry)
            else:
                unread.append(entry)
    chosen = [keyed[stem][wanted]] if wanted else list(keyed[stem].values())
    report = []
    for section in chosen:
        found = entries.get(section["key"], [])
        text = section["full"] if wanted else section["own"]
        overrides = [entry for entry in found if entry["mode"] == "override"]
        effective = overrides[0]["layer"] + " override" if overrides else (
            "suppressed" if any(entry["mode"] == "suppress" for entry in found) else "base")
        report.append({"file": stem, "key": section["key"], "heading": section["heading"], "base_text": text,
                       "effective": effective,
                       "entries": [{name: entry[name] for name in ("layer", "mode", "text", "base", "private")}
                                   for entry in found]})
    if as_json:
        print(json.dumps({"skill": skill, "general": [{"layer": entry["layer"], "text": entry["text"]} for entry in general],
                          "sections": report,
                          "unattached": [{name: entry[name] for name in ("layer", "attach", "mode", "text")}
                                         for entry in unread]}, ensure_ascii=False, indent=2))
        return 0
    path = base_file(skill, stem)
    print(f"=== {skill}/{stem} — base: {path.relative_to(SKILLS) if path else None}")
    for entry in general:
        print(f"[{entry['layer']} note on the skill] {entry['text']}")
    for section in report:
        print(f"\n{'#' * keyed[stem][section['key']]['level']} {section['heading']}   [{stem}#{section['key']}]")
        found = section["entries"]
        if not found:
            print(section["base_text"])
            continue
        effective = section["effective"]
        if effective == "suppressed":
            for entry in found:
                if entry["mode"] == "suppress":
                    print(f"[suppressed by the {entry['layer']} layer: {entry['text']}]")
        elif effective == "base":
            print(section["base_text"])
        else:
            print(f"[base] {section['base_text']}")
        shown = False
        for entry in found:
            if entry["mode"] == "override":
                if effective == f"{entry['layer']} override" and not shown:
                    shown = True
                    print(f"[{entry['layer']} override — effective for this researcher] {entry['text']}")
                else:
                    print(f"[{entry['layer']} override — shadowed by the {effective}] {entry['text']}")
            elif entry["mode"] == "add":
                print(f"[{entry['layer']} note] {entry['text']}")
            elif effective != "suppressed":
                print(f"[{entry['layer']} suppress — not applied: an override holds] {entry['text']}")
    for entry in unread:
        problem = "no such section in the base" if entry["mode"] in MODES else f"unknown mode '{entry['mode']}'"
        print(f"\n[{entry['layer']} {entry['mode']} on {entry['attach']}: {problem}; not applied, run sync_layers.py] "
              f"{entry['text']}")
    if any(entry["mode"] == "override" for section in report for entry in section["entries"]):
        print("\nWhere an override is effective, an answer quotes the base value beside it, both labelled, "
              "and says which one it used.")
    return 0


def year_of(ident: str) -> str:
    """Year of submission, read from an arXiv identifier."""
    digits = int(ident.split("/")[-1][:2])
    return str((1900 if "/" in ident and digits >= 91 else 2000) + digits)


def add_source(skill: str, ident: str, role: str | None, key: str | None, project: bool, via: str = "") -> int:
    skill = known_skill(skill)
    ident = re.sub(r"^arxiv:", "", ident.strip(), flags=re.IGNORECASE)
    ident = re.sub(r"v\d+$", "", ident)
    if not bibliography.ARXIV_ID.match(ident):
        raise SystemExit(f"'{ident}' is not an arXiv identifier; a paper without one is added by hand to {SOURCES}")
    role = role or ""
    if role not in bibliography.ROLES:
        raise SystemExit(f"--role must be one of: {', '.join(sorted(bibliography.ROLES))}")
    in_base = base_ids(skill).get(ident.lower())
    if in_base:
        print(f"arXiv:{ident} is already in the package's bibliography for {skill} (key {in_base}); nothing written")
        return 0
    kind, layer = target_layer(project)
    path = layer / skill / SOURCES
    rows, problems = read_sources(layer, skill)
    if problems:
        raise SystemExit("\n".join(problems) + f"\nrepair {path} first")
    if any(row["id"].lower() == ident.lower() for row in rows):
        print(f"arXiv:{ident} is already in {path}; nothing written")
        return 0
    bibliography.ATTEMPTS = 3
    record = bibliography.fetch([ident.lower()]).get(ident.lower())
    if record is None or not record["authors"]:
        raise SystemExit(f"arXiv does not list {ident}; nothing written")
    author = record["authors"][0]
    year = year_of(ident)
    taken = {row["key"] for row in rows}
    if key is None:
        stem = re.sub(r"[^A-Za-z]", "", bibliography.fold(author).split()[-1].capitalize()) + year
        key = next(stem + suffix for suffix in ["", *"bcdefghijklmnopqrstuvwxyz"] if stem + suffix not in taken)
    elif key in taken:
        raise SystemExit(f"key '{key}' is already used in {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.is_file():
        path.write_text("\t".join(bibliography.COLUMNS) + "\n", encoding="utf-8")
    title = " ".join(record["title"].split())
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\t".join([key, ident, author, year, title, role]) + "\n")
    print(f"{kind} paper {key} | arXiv:{ident} | {author} {year} | {title}\nwritten to {path}")
    if via:
        found, _ = read_found_via(layer, skill)
        if not any(row["id"] == ident.lower() for row in found):
            record_found(path.parent / FOUND_VIA, ident, via)
            print(f"found via {via}, recorded in {path.parent / FOUND_VIA}")
    return 0


def add_found(skill: str, ident: str, via: str, project: bool) -> int:
    """Record how a paper already in the layer's bibliography was found."""
    skill = known_skill(skill)
    ident = ident.strip()
    if not ident.lower().startswith("doi:"):
        ident = re.sub(r"v\d+$", "", re.sub(r"^arxiv:", "", ident, flags=re.IGNORECASE))
    kind, layer = target_layer(project)
    rows, problems = read_sources(layer, skill)
    found, issues = read_found_via(layer, skill)
    if problems or issues:
        raise SystemExit("\n".join(problems + issues) + "\nrepair them first; nothing written")
    if not any(row["id"].lower() == ident.lower() for row in rows if not row["_private"]):
        raise SystemExit(f"{ident} has no row in {layer / skill / SOURCES}; add the row first; nothing written")
    if any(row["id"] == ident.lower() for row in found):
        raise SystemExit(f"{ident} is already in {layer / skill / FOUND_VIA}; nothing written")
    record_found(layer / skill / FOUND_VIA, ident, via)
    print(f"{kind}: {ident} found via {via}, recorded in {layer / skill / FOUND_VIA}")
    return 0


def skill_snapshot(skill: str) -> str | None:
    """The first `Snapshot <date>` of a skill's SKILL.md."""
    path = SKILLS / skill / "SKILL.md"
    found = SNAPSHOT.search(path.read_text(encoding="utf-8")) if path.is_file() else None
    return found.group(1) if found else None


def read_sweeps(path: Path) -> tuple[list[dict], list[str]]:
    """Return (rows, problems) of a sweep table; `adapters` becomes a list."""
    if not path.is_file():
        return [], []
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].split("\t") != SWEEP_COLUMNS:
        return [], [f"{path}: header must be {', '.join(SWEEP_COLUMNS)}"]
    rows, problems = [], []
    for number, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        fields = [field.strip() for field in line.split("\t")]
        if len(fields) != len(SWEEP_COLUMNS):
            problems.append(f"{path}:{number}: {len(fields)} columns, expected {len(SWEEP_COLUMNS)}")
            continue
        row = dict(zip(SWEEP_COLUMNS, fields))
        row["adapters"] = [name for name in row["adapters"].split(",") if name]
        for name in ("swept_to", "recorded"):
            if not ISO_DATE.match(row[name]):
                problems.append(f"{path}:{number}: {name} '{row[name]}' is not a YYYY-MM-DD date")
        wrong = [name for name in row["adapters"] if name not in VIA]
        if wrong or not row["adapters"]:
            problems.append(f"{path}:{number}: adapters '{','.join(row['adapters'])}' must be a comma-separated "
                            f"subset of {', '.join(VIA)}")
        rows.append(row)
    return rows, problems


def latest(rows: list[dict], skill: str) -> dict | None:
    rows = [row for row in rows if row["skill"] == skill and ISO_DATE.match(row["swept_to"])]
    return max(rows, key=lambda row: row["swept_to"]) if rows else None


def base_sweep(skill: str) -> dict | None:
    """The package's sweep record for a skill, None when the hub's table is absent or has no row."""
    rows, _ = read_sweeps(SKILLS / HUB / "references" / SWEEPS)
    return latest(rows, skill)


def layer_sweep(layer: Path, skill: str) -> dict | None:
    """The latest sweep a layer recorded for a skill."""
    rows, _ = read_sweeps(layer / skill / SWEEPS)
    return latest(rows, skill)


def sweep_start(skill: str) -> str:
    """The date an extension run of a skill starts from: the latest of its snapshot and every sweep record."""
    dates = [skill_snapshot(skill)] + [(record or {}).get("swept_to") for record in
                                       [base_sweep(skill)] + [layer_sweep(layer, skill) for _, layer in layers()]]
    dates = [date for date in dates if date]
    return max(dates) if dates else "unknown"


def describe(record: dict | None) -> str:
    return f"{record['swept_to']} ({', '.join(record['adapters'])})" if record else "none"


def sweep(skill: str, as_json: bool) -> int:
    skill = known_skill(skill)
    snapshot_date, base_record = skill_snapshot(skill), base_sweep(skill)
    found = [(kind, layer_sweep(layer, skill)) for kind, layer in layers()]
    start = sweep_start(skill)
    if as_json:
        print(json.dumps({"skill": skill, "snapshot": snapshot_date, "base": base_record,
                          "layers": [dict(record or {}, layer=kind) for kind, record in found],
                          "start": start}, ensure_ascii=False, indent=2))
        return 0
    print(f"snapshot: {snapshot_date or 'unknown'}")
    print(f"base: {describe(base_record)}")
    for kind, record in found:
        print(f"{kind}: {describe(record)}")
    print(f"start: {start}")
    return 0


def record_sweep(skill: str, to: str | None, adapters: str | None, project: bool) -> int:
    """Append a sweep record to the layer; refuse a future date, a date before the start, an unknown adapter."""
    skill = known_skill(skill)
    if not to or not ISO_DATE.match(to):
        print("--record needs --to YYYY-MM-DD; nothing written", file=sys.stderr)
        return 1
    names = [name.strip() for name in (adapters or "").split(",") if name.strip()]
    wrong = [name for name in names if name not in VIA]
    if wrong or not names:
        print(f"--adapters must be a comma-separated subset of {', '.join(VIA)}; nothing written", file=sys.stderr)
        return 1
    if to > datetime.date.today().isoformat():
        print(f"--to {to} is after today; nothing written", file=sys.stderr)
        return 1
    start = sweep_start(skill)
    if start != "unknown" and to < start:
        print(f"--to {to} is before the date {skill} is already swept to ({start}); nothing written", file=sys.stderr)
        return 1
    kind, layer = target_layer(project)
    path = layer / skill / SWEEPS
    _, problems = read_sweeps(path)
    if problems:
        print("\n".join(problems) + "\nrepair it first; nothing written", file=sys.stderr)
        return 1
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.is_file():
        path.write_text("\t".join(SWEEP_COLUMNS) + "\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\t".join([skill, to, ",".join(names), datetime.date.today().isoformat()]) + "\n")
    print(f"{kind}: {skill} swept up to {to} with {', '.join(names)}, recorded in {path}")
    return 0


def progress(skill: str, clear: bool, project: bool) -> int:
    """Create, print or delete the state file of an extension run."""
    skill = known_skill(skill)
    kind, layer = target_layer(project)
    path = layer / skill / PROGRESS
    if clear:
        if path.is_file():
            path.unlink()
            print(f"cleared {path}")
        else:
            print(f"no paused run: {path} is absent")
        return 0
    if path.is_file():
        print(f"paused run: {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(PROGRESS_TEMPLATE.format(skill=skill, started=datetime.date.today().isoformat(),
                                                 start=sweep_start(skill)), encoding="utf-8")
        print(f"created {path}")
    print(path.read_text(encoding="utf-8"), end="")
    return 0


def add_dossier(skill: str, name: str, project: bool) -> int:
    skill = known_skill(skill)
    if not SLUG.match(name):
        raise SystemExit(f"'{name}' is not a dossier name: lower-case letters, digits and hyphens")
    kind, layer = target_layer(project)
    path = layer / skill / DEEP / f"{name}.md"
    if path.exists():
        print(f"kept    {path}")
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    title = name.replace("-", " ").capitalize()
    path.write_text(DOSSIER_TEMPLATE.format(title=title, date=datetime.date.today().isoformat()), encoding="utf-8")
    print(f"created {path} ({kind} layer); fill it, then run: layers.py check")
    return 0


def holds_content(folder: Path) -> bool:
    return any((place / NOTES).is_file() or (place / SOURCES).is_file() or (place / DEEP).is_dir()
               or (place / FOUND_VIA).is_file() or (place / SWEEPS).is_file()
               for place in (folder, folder / PRIVATE))


def check(online: bool) -> int:
    orphans = faults = warnings = 0
    for kind, layer in layers():
        for folder in sorted(path for path in layer.iterdir() if path.is_dir() and holds_content(path)):
            skill = folder.name
            if not (SKILLS / skill).is_dir():
                print(f"{kind}: {folder}: no skill named {skill} in the package")
                orphans += 1
                continue
            keys = base_keys(skill)
            rows, problems = read_sources(layer, skill)
            for note in read_notes(layer, skill):
                if not attached(note, keys):
                    print(f"{kind}: {note['path']}: note on '{note['attach']}' attaches to no section of {skill}")
                    orphans += 1
                if note["mode"] not in MODES:
                    problems.append(f"{note['path']}: entry on '{note['attach']}' has mode '{note['mode']}', "
                                    f"not one of {', '.join(MODES)}")
                elif note["mode"] != "add" and note["attach"].lower() == "general":
                    problems.append(f"{note['path']}: a {note['mode']} entry needs a section, not 'general'")
                if note["base"] and not STAMP.match(note["base"]):
                    problems.append(f"{note['path']}: entry on '{note['attach']}' has base '{note['base']}', "
                                    f"not a 12-digit fingerprint; repair it with sync_layers.py --stamp")
            notes = read_notes(layer, skill)
            for note in notes:
                length = sum(1 for line in note["text"].splitlines() if line.strip())
                if length > NOTE_WARN_LINES:
                    print(f"{kind}: warning: {note['path']}:{note['line'] + 1}: note on '{note['attach']}' has "
                          f"{length} lines; every answer in {skill} reads it: keep notes to 1-3 lines, move "
                          f"longer content to a dossier (layers.py dossier {skill} <name>)")
                    warnings += 1
            general = [note for note in notes if note["attach"].lower() == "general"]
            if len(general) > GENERAL_WARN_COUNT:
                print(f"{kind}: warning: {folder}: {len(general)} 'general' notes; they apply to every question "
                      f"in {skill}: attach each to the most specific section instead")
                warnings += 1
            known = set(base_ids(skill)) | {row["id"].lower() for row in rows}
            found, issues = read_found_via(layer, skill)
            problems += issues
            sweeps, issues = read_sweeps(folder / SWEEPS)
            problems += issues + [f"{folder / SWEEPS}: row for '{row['skill']}' in the folder of {skill}"
                                  for row in sweeps if row["skill"] != skill]
            for row in found:
                if row["id"] not in known:
                    problems.append(f"{row['_path']}:{row['_line']}: {row['id']} has no row in {SOURCES}, "
                                    f"here or in the package")
            cited_arxiv, cited_doi = bibliography.cited_ids(folder)
            for ident, files in sorted(cited_arxiv.items()):
                if ident not in known:
                    problems.append(f"{folder}: arXiv:{ident} cited in {sorted(files)} has no row, here or in the package; "
                                    f"add it with: layers.py source {skill} {ident} --role <role>")
            for ident, files in sorted(cited_doi.items()):
                if f"doi:{ident}" not in known:
                    problems.append(f"{folder}: doi:{ident} cited in {sorted(files)} has no row, here or in the package")
            if online:
                row_arxiv = {row["id"].lower(): row for row in rows if bibliography.ARXIV_ID.match(row["id"])}
                if row_arxiv:
                    problems += bibliography.compare_with_arxiv(row_arxiv, folder / SOURCES)
            for problem in problems:
                print(f"{kind}: {problem}")
            faults += len(problems)
    print(f"{orphans} note(s) attached to nothing, {faults} problem(s) in papers and citations, "
          f"{warnings} warning(s)", file=sys.stderr)
    return 1 if orphans or faults else 0


def via_value(value: str) -> str:
    if value not in VIA:
        raise argparse.ArgumentTypeError(f"'{value}' is not one of: {', '.join(VIA)}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("target", help="a skill name, or one of: init, check, note, override, suppress, resolve, "
                                       "source, found, dossier, progress, sweep")
    parser.add_argument("rest", nargs="*", help="arguments of the command")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--project", action="store_true", help="write to the project layer instead of the personal one")
    parser.add_argument("--role", help="with source: the role of the paper")
    parser.add_argument("--key", help="with source: the bibliography key, instead of <Author><year>")
    parser.add_argument("--online", action="store_true", help="with check: compare the layer's papers with arXiv")
    parser.add_argument("--clear", action="store_true", help="with progress: delete the state of the run")
    parser.add_argument("--record", action="store_true", help="with sweep: record a sweep in the layer")
    parser.add_argument("--to", help="with sweep --record: the date up to which the skill was swept")
    parser.add_argument("--adapters", help=f"with sweep --record: comma-separated, from {', '.join(VIA)}")
    parser.add_argument("--via", type=via_value, default=None,
                        help=f"with note, override, suppress, source, found: how the paper was found ({', '.join(VIA)})")
    args = parser.parse_args()
    args.via = args.via or ""
    if args.target == "init":
        return init(args.project)
    if args.target == "check":
        return check(args.online)
    if args.target == "note":
        if len(args.rest) < 3:
            raise SystemExit("usage: layers.py note <skill> <file>#<key>|general <text>")
        return add_note(args.rest[0], args.rest[1], " ".join(args.rest[2:]), args.project, via=args.via)
    if args.target in ("override", "suppress"):
        if len(args.rest) < 3:
            raise SystemExit(f"usage: layers.py {args.target} <skill> <file>#<key> <text>")
        return add_note(args.rest[0], args.rest[1], " ".join(args.rest[2:]), args.project, mode=args.target,
                        via=args.via)
    if args.target == "resolve":
        if len(args.rest) != 2:
            raise SystemExit("usage: layers.py resolve <skill> <file>[#<key>]")
        return resolve(args.rest[0], args.rest[1], args.json)
    if args.target == "source":
        if len(args.rest) != 2:
            raise SystemExit("usage: layers.py source <skill> <arXiv id> --role <role>")
        return add_source(args.rest[0], args.rest[1], args.role, args.key, args.project, via=args.via)
    if args.target == "found":
        if len(args.rest) != 2 or not args.via:
            raise SystemExit("usage: layers.py found <skill> <doi:...|arXiv id> --via <via>")
        return add_found(args.rest[0], args.rest[1], args.via, args.project)
    if args.target == "progress":
        if len(args.rest) != 1:
            raise SystemExit("usage: layers.py progress <skill> [--clear]")
        return progress(args.rest[0], args.clear, args.project)
    if args.target == "sweep":
        if len(args.rest) != 1:
            raise SystemExit("usage: layers.py sweep <skill> [--json] | --record --to <date> --adapters <list>")
        if args.record:
            return record_sweep(args.rest[0], args.to, args.adapters, args.project)
        return sweep(args.rest[0], args.json)
    if args.target == "dossier":
        if len(args.rest) != 2:
            raise SystemExit("usage: layers.py dossier <skill> <name>")
        return add_dossier(args.rest[0], args.rest[1], args.project)
    return show(args.target, args.json)


if __name__ == "__main__":
    sys.exit(main())
