#!/usr/bin/env python3
"""Move a layer entry into the package's working tree, for its owner to review.

    promote.py <skill> source <arXiv id | doi:... | key> [--offline]
    promote.py <skill> dossier <name> [--with-sources] [--offline]
    promote.py <skill> note <file>#<key> | general

The entry is read from the personal layer, or from the project layer with
`--project`. What is promoted goes to the package the layers are read
against (its own `skills/`, or COSMOSKILL_BASE):

  source    the row is appended to `skills/<skill>/references/sources.tsv`.
            It needs a public identifier (arXiv or `doi:`), and an arXiv row
            must match arXiv in title and first author (skipped with
            --offline, which says so).
  dossier   copied to `skills/<skill>/deep/<name>.md`. Refused when the
            dossier is private, lacks `Scope:` or `Snapshot:`, a dossier of
            that name exists, or a cited identifier has no row in the
            package (unless --with-sources promotes the layer's rows with
            it). Prints the file-map row, the subtopics.tsv row and the
            checks to run.
  note      a note cannot be merged into prose automatically: it is written
            as a proposal, `docs/proposals/<date>_<skill>_<file>_<key>.md`,
            holding the base section, the entry and its mode, for the owner
            to fold in by hand.

Entries under a `private/` folder of the layer, or marked `private: yes`,
are never promoted. Every refusal exits 1 and writes nothing. Nothing is
committed. The layer entry is kept; `--remove` deletes it after a
successful promotion. Standard library only.
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layers  # noqa: E402
import verify_sources as bibliography  # noqa: E402

# the repository root: the skills are in plugin/skills/ since 1.0.3, in skills/ before
PACKAGE = layers.SKILLS.parent.parent if layers.SKILLS.parent.name == "plugin" else layers.SKILLS.parent
SKILLS_PATH = layers.SKILLS.relative_to(PACKAGE).as_posix()


def refuse(message: str) -> SystemExit:
    return SystemExit(f"{message}\nnothing written")


def public(ident: str) -> bool:
    return bool(bibliography.ARXIV_ID.match(ident) or ident.lower().startswith("doi:10."))


def normal(ident: str) -> str:
    ident = re.sub(r"^arxiv:", "", ident.strip(), flags=re.IGNORECASE)
    return re.sub(r"v\d+$", "", ident) if bibliography.ARXIV_ID.match(re.sub(r"v\d+$", "", ident)) else ident


def layer_rows(layer: Path, skill: str) -> list[dict]:
    """Rows of the layer's bibliographies for a skill, each with its file and privacy."""
    rows = []
    for folder, private in layers.skill_folders(layer, skill):
        path = folder / layers.SOURCES
        if path.is_file():
            found, _ = bibliography.read_sources(path)
            for row in found:
                row["_private"], row["_path"] = private, path
            rows += found
    return rows


def base_table(skill: str) -> tuple[Path, list[dict]]:
    path = layers.SKILLS / skill / "references" / layers.SOURCES
    if not path.is_file():
        return path, []
    rows, problems = bibliography.read_sources(path)
    if problems:
        raise refuse("\n".join(problems) + f"\nthe package's bibliography for {skill} must be repaired first")
    return path, rows


def vet_rows(rows: list[dict], skill: str, offline: bool) -> list[str]:
    """Refusal reasons for rows about to enter the package's bibliography."""
    path, base = base_table(skill)
    base_ids = {row["id"].lower() for row in base}
    base_keys = {row["key"] for row in base}
    reasons = []
    for row in rows:
        label = f"{row['key']} ({row['id']})"
        if row["_private"]:
            reasons.append(f"{label} is in a private/ folder of the layer: never promoted")
        if not public(row["id"]):
            reasons.append(f"{label} has no public identifier (arXiv or doi:10....): it cannot enter the package")
        if not all(row[name] for name in bibliography.COLUMNS) or row["role"] not in bibliography.ROLES \
                or not re.fullmatch(r"\d{4}", row["year"]):
            reasons.append(f"{label}: empty field, unknown role or malformed year in {row['_path']}:{row['_line']}")
        if row["id"].lower() in base_ids:
            reasons.append(f"{label} is already in {path}")
        elif row["key"] in base_keys:
            reasons.append(f"{label}: key {row['key']} is already used in {path}; rename the row in the layer first")
    arxiv = {row["id"].lower(): row for row in rows if bibliography.ARXIV_ID.match(row["id"])}
    if reasons or not arxiv:
        return reasons
    if offline:
        print("not compared with arXiv (--offline): run verify_sources.py on the skill before committing")
        return reasons
    bibliography.ATTEMPTS = 3
    return reasons + bibliography.compare_with_arxiv(arxiv, rows[0]["_path"])


def append_rows(rows: list[dict], skill: str) -> Path:
    path, _ = base_table(skill)
    path.parent.mkdir(parents=True, exist_ok=True)
    before = path.read_text(encoding="utf-8") if path.is_file() else "\t".join(bibliography.COLUMNS) + "\n"
    if before and not before.endswith("\n"):
        before += "\n"
    added = "".join("\t".join(row[name] for name in bibliography.COLUMNS) + "\n" for row in rows)
    path.write_text(before + added, encoding="utf-8")
    return path


def drop_rows(rows: list[dict]) -> None:
    """Delete rows from the layer files they were read from."""
    for path in {row["_path"] for row in rows}:
        lines = path.read_text(encoding="utf-8").split("\n")
        for number in sorted((row["_line"] for row in rows if row["_path"] == path), reverse=True):
            del lines[number - 1]
        path.write_text("\n".join(lines), encoding="utf-8")


def checks(skill: str) -> str:
    return ("checks to run from the package root, then review and commit by hand:\n"
            "  python3 tools/assign_keys.py\n"
            "  python3 tools/sync_blocks.py\n"
            f"  python3 plugin/skills/observational-cosmology/scripts/verify_sources.py plugin/skills/{skill}\n"
            "  python3 tools/check_keys.py\n"
            "  python3 -m unittest discover -s tests")


def promote_source(skill: str, layer: Path, wanted: str, offline: bool, remove: bool) -> int:
    ident = normal(wanted)
    rows = [row for row in layer_rows(layer, skill) if row["id"].lower() == ident.lower() or row["key"] == wanted]
    if not rows:
        raise refuse(f"no row '{wanted}' in the layer's bibliography for {skill}")
    reasons = vet_rows(rows[:1], skill, offline)
    if reasons:
        raise refuse("\n".join(reasons))
    path = append_rows(rows[:1], skill)
    row = rows[0]
    print(f"appended {row['key']} | {row['id']} | {row['first_author']} {row['year']} | {row['title']}\nto {path}")
    print("cite it in the skill's text: verify_sources.py reports a row that is never cited")
    if remove:
        drop_rows(rows[:1])
        print(f"removed from {row['_path']}")
    print(checks(skill))
    return 0


def promote_dossier(skill: str, layer: Path, name: str, with_sources: bool, offline: bool, remove: bool) -> int:
    found = {dossier["path"]: dossier for dossier in layers.read_dossiers(layer, skill) if dossier["name"] == name}
    if not found:
        raise refuse(f"no dossier '{name}' in the layer for {skill}")
    if any(dossier["private"] for dossier in found.values()):
        raise refuse(f"dossier '{name}' is private (in a private/ folder or marked private: yes): never promoted")
    source = Path(next(iter(found)))
    text = source.read_text(encoding="utf-8")
    lines = text.splitlines()
    reasons = [f"{source.name} has no '{label}:' line" for label in ("Scope", "Snapshot")
               if not any(line.lower().startswith(label.lower() + ":") for line in lines)]
    target = layers.SKILLS / skill / layers.DEEP / f"{name}.md"
    if target.exists():
        reasons.append(f"the package already has a dossier {skill}/{layers.DEEP}/{name}.md")
    known = set(layers.base_ids(skill))
    cited = {match.group(1).lower() for match in bibliography.ARXIV_CITE.finditer(text)}
    cited |= {"doi:" + match.group(1).rstrip(".").lower() for match in bibliography.DOI_CITE.finditer(text)}
    lacking = sorted(ident for ident in cited if ident not in known)
    rows = []
    if lacking and not with_sources:
        reasons.append("cited without a row in the package: " + ", ".join(lacking)
                       + "; promote the layer's rows with --with-sources")
    elif lacking:
        mine = {row["id"].lower(): row for row in layer_rows(layer, skill)}
        absent = [ident for ident in lacking if ident not in mine]
        if absent:
            reasons.append("cited with no row in the layer either: " + ", ".join(absent))
        rows = [mine[ident] for ident in lacking if ident in mine]
    if reasons:
        raise refuse("\n".join(reasons))
    if rows:
        reasons = vet_rows(rows, skill, offline)
        if reasons:
            raise refuse("\n".join(reasons))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
    print(f"copied {source.name} to {target}")
    if rows:
        print(f"appended {len(rows)} row(s) to {append_rows(rows, skill)}: {', '.join(row['key'] for row in rows)}")
    dossier = next(iter(found.values()))
    print("add to the file map of SKILL.md:\n"
          f"  | {dossier['scope'] or dossier['title']} | `{layers.DEEP}/{name}.md` |")
    print("add to references/subtopics.tsv (fill the `from` column with the reviews it rests on):\n"
          f"  {name}\t{dossier['title']}\t\t{layers.DEEP}/{name}.md\tcovered")
    if remove:
        source.unlink()
        print(f"removed {source}")
    print(checks(skill))
    return 0


def block(text: str) -> str:
    return "\n".join(f"> {line}" if line else ">" for line in text.split("\n"))


def remove_entry(entry: dict) -> None:
    path = Path(entry["path"])
    lines = path.read_text(encoding="utf-8").split("\n")
    end = next((index for index in range(entry["line"] + 1, len(lines)) if layers.NOTE_HEADING.match(lines[index])),
               len(lines))
    del lines[entry["line"]:end]
    path.write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8")


def promote_note(skill: str, kind: str, layer: Path, target: str, remove: bool) -> int:
    keyed = layers.base_sections(skill)
    retired = layers.retired_keys(skill)
    general = target.lower() == "general"
    if general:
        stem, key = "skill", "general"
    else:
        stem, key = layers.locate(target, keyed)
        if stem is None or key not in keyed.get(stem, {}):
            raise refuse(f"{skill} has no section '{target}'; run sync_layers.py and re-attach the entry first")
    chosen = [entry for entry in layers.read_notes(layer, skill)
              if (general and entry["attach"].lower() == "general")
              or (not general and layers.locate(entry["attach"], keyed) == (stem, key))]
    if not chosen:
        raise refuse(f"no entry on {skill}/{target} in the {kind} layer")
    shared = [entry for entry in chosen if not entry["private"]]
    if not shared:
        raise refuse(f"the entries on {skill}/{target} are private (private/ folder or private: yes): never promoted")
    name = f"{datetime.date.today().isoformat()}_{skill}_{'general' if general else stem + '_' + key}.md"
    path = PACKAGE / "docs" / "proposals" / name
    if path.exists():
        raise refuse(f"{path} exists; fold it in or delete it first")
    known = set(layers.base_ids(skill))
    parts = [f"# Proposal: fold a {kind}-layer entry into {skill}/{target}", "",
             f"Written by promote.py on {datetime.date.today().isoformat()} from the {kind} layer. "
             "Fold it into the file by hand, keep the key line, run the checks below, then delete this file.", ""]
    if general:
        parts += ["## Base", "", f"The skill as a whole: `{SKILLS_PATH}/{skill}/SKILL.md`.", ""]
    else:
        section = keyed[stem][key]
        place = layers.base_file(skill, stem).relative_to(layers.SKILLS)
        parts += ["## Base section", "", f"`{SKILLS_PATH}/{place.as_posix()}`, key `{key}`, fingerprint "
                  f"`{layers.fingerprint(section)}`:", "", block(section["line"] + "\n\n" + section["full"]), ""]
    for number, entry in enumerate(shared, start=1):
        state = layers.entry_status(entry, keyed, retired)["status"]
        against = {"ok": "the base section has not changed since", "changed": "the base section changed since: "
                   "check the entry against the text above"}.get(state, "no stamp to compare")
        parts += [f"## Entry {number}", "", f"Mode: `{entry['mode']}`. Written against fingerprint "
                  f"`{entry['base'] or 'none'}` ({against}).", "", block(entry["text"]), ""]
        lacking = sorted({match.group(1).lower() for match in bibliography.ARXIV_CITE.finditer(entry["text"])} - known)
        if lacking:
            parts += ["Cited without a row in the package: " + ", ".join(f"arXiv:{ident}" for ident in lacking)
                      + f". Promote each with `promote.py {skill} source <id>`.", ""]
    parts += ["## Checks", "", "```", checks(skill).split(":\n", 1)[1], "```", ""]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts), encoding="utf-8")
    print(f"proposal written to {path}")
    skipped = len(chosen) - len(shared)
    if skipped:
        print(f"{skipped} private entr{'y' if skipped == 1 else 'ies'} on this section left out")
    if remove:
        for entry in sorted(shared, key=lambda item: (item["path"], item["line"]), reverse=True):
            remove_entry(entry)
        print(f"removed {len(shared)} entr{'y' if len(shared) == 1 else 'ies'} from the {kind} layer")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("skill")
    parser.add_argument("kind", choices=("source", "dossier", "note"))
    parser.add_argument("name", help="the identifier or key of a row, a dossier name, or <file>#<key> / general")
    parser.add_argument("--project", action="store_true", help="take the entry from the project layer")
    parser.add_argument("--with-sources", action="store_true", help="with dossier: promote the layer rows it cites")
    parser.add_argument("--offline", action="store_true", help="do not compare promoted rows with arXiv")
    parser.add_argument("--remove", action="store_true", help="delete the layer entry after a successful promotion")
    args = parser.parse_args()
    skill = layers.known_skill(args.skill)
    kind, layer = layers.target_layer(args.project)
    if not layer.is_dir():
        raise refuse(f"no {kind} layer at {layer}")
    if args.kind == "source":
        return promote_source(skill, layer, args.name, args.offline, args.remove)
    if args.kind == "dossier":
        return promote_dossier(skill, layer, args.name, args.with_sources, args.offline, args.remove)
    return promote_note(skill, kind, layer, args.name, args.remove)


if __name__ == "__main__":
    sys.exit(main())
