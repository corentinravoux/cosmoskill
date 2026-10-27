#!/usr/bin/env python3
"""Write the release manifest: the section keys added, changed, moved or retired between two refs.

    python3 tools/make_release_manifest.py --from v0.3.0 --version 0.4.0
    python3 tools/make_release_manifest.py --from v0.3.0 --to v0.4.0 --version 0.4.0

`--to` defaults to the working tree. The manifest is written to
`releases/<version>.tsv`, with the columns

    skill  file  key  change  replaced_by  fingerprint

where `change` is `added`, `changed` (the section's fingerprint differs),
`moved` (gone, listed in `references/retired-keys.tsv` with a replacement)
or `retired` (gone, with no replacement). The fingerprint is the one layer
entries are stamped with (docs/layers-v1.md): of the section at `--to`, or
of its replacement for a moved key, empty for a retired one. It tells a
researcher, before updating, which of their layer entries
`sync_layers.py` will report. A key gone without a row in
`retired-keys.tsv` is written as `retired` and reported on stderr: run
`tools/check_keys.py --against <ref>` to fix the package first.

Standard library only. An existing manifest is kept unless --force.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import SKILLS, skills_dir_at  # noqa: E402

sys.path.insert(0, str(ROOT / SKILLS / "observational-cosmology" / "scripts"))
import layers  # noqa: E402

COLUMNS = ["skill", "file", "key", "change", "replaced_by", "fingerprint"]


def tracked(path: str) -> bool:
    """Whether a path under skills/ holds keyed sections, as layers read them."""
    parts = path.split("/")
    if len(parts) == 3 and parts[2] == "SKILL.md":
        return True
    return len(parts) == 4 and parts[2] in ("references", layers.DEEP) and parts[3].endswith(".md")


def stem_of(path: str) -> str:
    return "skill" if path.endswith("/SKILL.md") else Path(path).stem


def read_tree(repo: Path, ref: str | None) -> dict[str, str]:
    """Return {"skills/<skill>/...": text} at a git ref, or in the working tree when ref is None.

    The keys start with "skills/" whatever the layout, so that a ref from
    before the move to plugin/ compares with the current tree.
    """
    if ref is None:
        top = repo / SKILLS
        return {"skills/" + path.relative_to(top).as_posix(): path.read_text(encoding="utf-8")
                for path in sorted(top.rglob("*")) if path.is_file()
                and (tracked("skills/" + path.relative_to(top).as_posix()) or path.name == layers.RETIRED)}
    old_dir = skills_dir_at(repo, ref)
    listing = subprocess.run(["git", "-C", str(repo), "ls-tree", "-r", "--name-only", ref, old_dir],
                             capture_output=True, text=True)
    if listing.returncode != 0:
        raise SystemExit(f"git cannot read {ref!r}: {listing.stderr.strip()}")
    files = {}
    for old_name in listing.stdout.splitlines():
        name = "skills/" + old_name[len(old_dir) + 1:]
        if tracked(name) or name.endswith("/references/" + layers.RETIRED):
            shown = subprocess.run(["git", "-C", str(repo), "show", f"{ref}:{old_name}"], capture_output=True, text=True)
            files[name] = shown.stdout
    return files


def fingerprints(files: dict[str, str]) -> dict[tuple[str, str], dict[str, str]]:
    """Return {(skill, file stem): {key: fingerprint}}; a reference file wins over a dossier of the same stem."""
    found: dict[tuple[str, str], dict[str, str]] = {}
    for name in sorted(files, key=lambda item: ("/deep/" in item, item)):
        if not tracked(name):
            continue
        place = (name.split("/")[1], stem_of(name))
        if place in found:
            continue
        found[place] = {section["key"]: layers.fingerprint(section) for section in layers.sections(files[name])}
    return found


def retired_rows(files: dict[str, str], skill: str) -> dict[tuple[str, str], str]:
    """Return {(file, key): replaced_by} from a skill's retired-keys.tsv."""
    text = files.get(f"skills/{skill}/references/{layers.RETIRED}", "")
    rows = {}
    for line in text.splitlines()[1:]:
        fields = (line.split("\t") + [""] * 5)[:5]
        if fields[0] and fields[1]:
            rows[(fields[0], fields[1])] = fields[3].strip()
    return rows


def manifest(repo: Path, old_ref: str, new_ref: str | None) -> tuple[list[list[str]], list[str]]:
    old_files, new_files = read_tree(repo, old_ref), read_tree(repo, new_ref)
    old, new = fingerprints(old_files), fingerprints(new_files)
    rows, warnings = [], []
    for place in sorted(set(old) | set(new)):
        skill, stem = place
        before, after = old.get(place, {}), new.get(place, {})
        retired = retired_rows(new_files, skill)
        for key in sorted(set(before) | set(after)):
            if key in after and key not in before:
                rows.append([skill, stem, key, "added", "", after[key]])
            elif key in after:
                if after[key] != before[key]:
                    rows.append([skill, stem, key, "changed", "", after[key]])
            elif retired.get((stem, key)):
                target = retired[(stem, key)]
                new_stem, _, new_key = target.partition("#")
                rows.append([skill, stem, key, "moved", target, new.get((skill, new_stem), {}).get(new_key, "")])
            else:
                rows.append([skill, stem, key, "retired", "", ""])
                if (stem, key) not in retired:
                    warnings.append(f"{skill}/{stem}#{key} is gone and not listed in references/{layers.RETIRED}")
    return rows, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--from", dest="old", required=True, metavar="REF", help="the previous release")
    parser.add_argument("--to", dest="new", metavar="REF", help="the new release; default the working tree")
    parser.add_argument("--version", required=True, help="the new version, names releases/<version>.tsv")
    parser.add_argument("--repo", type=Path, default=ROOT, help=argparse.SUPPRESS)
    parser.add_argument("--force", action="store_true", help="replace an existing manifest")
    args = parser.parse_args()
    target = args.repo / "releases" / f"{args.version}.tsv"
    if target.exists() and not args.force:
        raise SystemExit(f"{target} exists; pass --force to replace it")
    rows, warnings = manifest(args.repo, args.old, args.new)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join("\t".join(row) for row in [COLUMNS] + rows) + "\n", encoding="utf-8")
    for warning in warnings:
        print(warning, file=sys.stderr)
    counts = {name: sum(1 for row in rows if row[3] == name) for name in ("added", "changed", "moved", "retired")}
    print(f"wrote {target}: " + ", ".join(f"{count} {name}" for name, count in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
