#!/usr/bin/env python3
"""Report the layer entries whose base section changed, moved or disappeared.

Each entry of a layer (`<layer>/<skill>/notes.md`, private ones included)
attaches to a section of the package by its key and records `base:`, the
fingerprint of that section when the entry was written (docs/layers-v1.md).
After an update of the package, this script compares every entry of every
layer found (project, then personal) with the base:

  ok          key present, fingerprint unchanged                exit 0
  unstamped   a v0 note without `base:`                         exit 0
  changed     key present, the base text changed since          exit 2, 3 for an override
  moved       key listed in references/retired-keys.tsv with    exit 2, 3 for an override
              a replacement
  retired     key retired with no replacement                   exit 2, 3 for an override
  missing     key absent and not listed as retired              exit 2, 3 for an override
  malformed   an entry or a layer folder the script cannot read exit 1

The exit status is the highest found. A `changed` override exits 3: the
researcher's value may now be the older of the two.

    sync_layers.py                       report every entry
    sync_layers.py --json                the same, machine-readable
    sync_layers.py --stamp <skill>/<file>#<key>
                                         re-stamp the entries on that section,
                                         after the researcher has reviewed them
    sync_layers.py --stamp-all           re-stamp every ok, unstamped and
                                         changed entry
    sync_layers.py --follow              rewrite the heading of each moved
                                         entry to its replacement, and stamp it

No option touches a `retired` or `missing` entry: the researcher edits or
deletes it. After any rewrite, the report is printed again and the exit
status is that of the new report. COSMOSKILL_HOME and COSMOSKILL_BASE apply
as for layers.py. Standard library only.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layers  # noqa: E402

SEVERE = ("changed", "moved", "retired", "missing")
ADVICE = {
    "changed": "review it with: layers.py resolve {skill} {stem}#{key}; then: sync_layers.py --stamp {skill}/{stem}#{key}",
    "moved": "re-attach it with: sync_layers.py --follow",
    "retired": "edit or delete the entry: its section is gone",
    "missing": "a typing error, or a section removed without a record: edit or delete the entry",
    "unstamped": "review it, then: sync_layers.py --stamp-all",
}


def skill_folders(layer: Path) -> list[Path]:
    """The folders of a layer that hold entries."""
    return sorted(path for path in layer.iterdir()
                  if path.is_dir() and any((place / layers.NOTES).is_file() for place in (path, path / layers.PRIVATE)))


def survey() -> list[dict]:
    """Return one record per entry of every layer found, with its status."""
    records = []
    for kind, layer in layers.layers():
        for folder in skill_folders(layer):
            skill = folder.name
            if not (layers.SKILLS / skill / "SKILL.md").is_file():
                records.append({"layer": kind, "skill": skill, "attach": "", "mode": "", "path": str(folder),
                                "line": 0, "status": "malformed", "detail": f"no skill named {skill} in the base"})
                continue
            keyed = layers.base_sections(skill)
            retired = layers.retired_keys(skill)
            for entry in layers.read_notes(layer, skill):
                state = layers.entry_status(entry, keyed, retired)
                if state["status"] == "general":
                    continue
                records.append({"layer": kind, "skill": skill, "attach": entry["attach"], "mode": entry["mode"],
                                "path": entry["path"], "line": entry["line"], "private": entry["private"],
                                "base": entry["base"], **state, "_entry": entry, "_keyed": keyed})
    return records


def severity(record: dict) -> int:
    if record["status"] == "malformed":
        return 1
    if record["status"] in SEVERE:
        return 3 if record["mode"] == "override" else 2
    return 0


def report(records: list[dict], as_json: bool) -> int:
    worst = max((severity(record) for record in records), default=0)
    if as_json:
        print(json.dumps([{name: value for name, value in record.items() if not name.startswith("_")}
                          for record in records], ensure_ascii=False, indent=2))
        return worst
    for record in records:
        where = f"{record['path']}:{record['line'] + 1}"
        mode = record["mode"] or "entry"
        what = f"{record['layer']} {mode} {record['skill']}/{record['attach']}" if record["attach"] else record["skill"]
        line = f"{record['status']:<10} {what}"
        if record["status"] == "moved":
            line += f" -> {record['target'] or '?'}"
        if record["detail"]:
            line += f" ({record['detail']})"
        print(f"{line}  [{where}]")
        if record["status"] == "changed" and record["mode"] == "override":
            print("           the base section under this override changed: the override may now be the older value")
        advice = ADVICE.get(record["status"])
        if record["status"] == "moved" and not record.get("target"):
            advice = "its replacement is not in the base: edit or delete the entry"
        if advice:
            print("           " + advice.format(skill=record["skill"], stem=record.get("stem"), key=record.get("key")))
    counts = {}
    for record in records:
        counts[record["status"]] = counts.get(record["status"], 0) + 1
    summary = ", ".join(f"{counts[name]} {name}" for name in
                        ("ok", "unstamped", "changed", "moved", "retired", "missing", "malformed") if name in counts)
    print(f"{len(records)} entr{'y' if len(records) == 1 else 'ies'}: {summary or 'none'}; exit {worst}", file=sys.stderr)
    return worst


def rewrite(actions: list[tuple[dict, str | None, str]], stream) -> None:
    """Apply (record, new heading or None, new stamp), last line first so earlier lines keep their number."""
    for record, attach, stamp in sorted(actions, key=lambda item: (item[0]["path"], item[0]["line"]), reverse=True):
        layers.rewrite_entry(record["_entry"], attach=attach, stamp=stamp)
        verb = f"re-attached to {attach} and stamped:" if attach else "stamped:"
        print(f"{verb} {record['layer']} {record['mode']} {record['skill']}/{record['attach']}", file=stream)


def stamp_of(record: dict, attach: str | None = None) -> str:
    stem, key = (attach.split("#", 1) if attach else (record["stem"], record["key"]))
    return layers.fingerprint(record["_keyed"][stem][key])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--stamp", metavar="SKILL/FILE#KEY", help="re-stamp the entries on one section")
    action.add_argument("--stamp-all", action="store_true", help="re-stamp every ok, unstamped and changed entry")
    parser.add_argument("--follow", action="store_true", help="re-attach each moved entry to its replacement")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    records = survey()
    actions: list[tuple[dict, str | None, str]] = []
    if args.stamp:
        skill, _, target = layers.clean(args.stamp).partition("/")
        stem, _, key = target.partition("#")
        if not (skill and stem and key):
            raise SystemExit(f"'{args.stamp}' is not <skill>/<file>#<key>")
        chosen = [record for record in records if record["skill"] == skill and record["attach"] and (
            record["attach"] == target or (record.get("stem"), record.get("key")) == (stem, key))]
        if not chosen:
            raise SystemExit(f"no layer entry on {skill}/{target}; nothing written")
        refused = [record for record in chosen if record["status"] not in ("ok", "unstamped", "changed")]
        if refused:
            raise SystemExit("\n".join(f"{record['status']}: {record['layer']} {record['mode']} {skill}/{record['attach']} "
                                       f"cannot be stamped ({record['detail']})" for record in refused)
                             + "\nnothing written; use --follow for a moved entry, edit a retired or missing one")
        actions += [(record, None, stamp_of(record)) for record in chosen if record["status"] != "ok"]
    if args.stamp_all:
        actions += [(record, None, stamp_of(record)) for record in records if record["status"] in ("unstamped", "changed")]
    if args.follow:
        actions += [(record, record["target"], stamp_of(record, record["target"]))
                    for record in records if record["status"] == "moved" and record.get("target")]
    if actions:
        rewrite(actions, sys.stderr if args.json else sys.stdout)
        records = survey()
    return report(records, args.json)


if __name__ == "__main__":
    sys.exit(main())
