#!/usr/bin/env python3
"""Build one r96 base copy and five independent mutants. Scratch only."""

import difflib
import shutil
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SRC = LANE / "corpus/fixtures/r96-crossing-response"
SCRATCH = LANE / ".ufo/waves/round-99/seats/V09-scratch"
BASE = SCRATCH / "base" / "r96-crossing-response"
MUTANTS = SCRATCH / "mutants"

EDGE_OLD = """\
    "id": "response-evin-salt-court",
    "tick": 12,
    "entity_id": "evin",
    "place_id": "salt-court",
    "depends_on": [
      "aftermath-missing-evin"
    ],
"""
EDGE_NEW = """\
    "id": "response-evin-salt-court",
    "tick": 12,
    "entity_id": "evin",
    "place_id": "salt-court",
    "depends_on": [],
"""

# Dependency wording inside the J14 exact anchor (fictional-excerpts.md line 20).
PROSE_OLD = "Their tick-10 decision depends on both ninth-bell entries"
PROSE_NEW = "Their tick-10 decision on both ninth-bell entries"

# Non-anchor prose (map paragraph, not a table cell). Isolating control, not one of the five.
PROSE_ISO_OLD = "ordered after and depends on both (`aru-ninth-bell`"
PROSE_ISO_NEW = "ordered after and on both (`aru-ninth-bell`"

SPAN_OLD = "| 33-42 |"
SPAN_NEW = "| 33-36 |"

SOURCE_OLD = '"source_id": "evin-response-note"'
SOURCE_NEW = '"source_id": "paired-clock"'


def once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected 1 occurrence of marker, found {count}")
    return text.replace(old, new, 1)


def copy_base():
    if BASE.exists():
        shutil.rmtree(BASE)
    BASE.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SRC, BASE)
    if MUTANTS.exists():
        shutil.rmtree(MUTANTS)
    MUTANTS.mkdir(parents=True)


def write_mutant(name, edits):
    dest = MUTANTS / name / "r96-crossing-response"
    if dest.exists():
        shutil.rmtree(dest.parent)
    shutil.copytree(BASE, dest)
    notes = []
    for rel, old, new in edits:
        path = dest / rel
        before = path.read_text(encoding="utf-8")
        after = once(before, old, new, f"{name}:{rel}")
        path.write_text(after, encoding="utf-8")
        diff = "".join(difflib.unified_diff(
            before.splitlines(keepends=True),
            after.splitlines(keepends=True),
            fromfile=f"base/{rel}",
            tofile=f"{name}/{rel}",
        ))
        (SCRATCH / f"diff-{name}.txt").write_text(diff, encoding="utf-8")
        notes.append(f"{rel} replacements=1")
    print(f"MUTANT {name}: {'; '.join(notes)}")
    return dest


def drop_j16(name):
    dest = MUTANTS / name / "r96-crossing-response"
    shutil.copytree(BASE, dest)
    path = dest / "claim-excerpt-map.md"
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    hits = [i for i, line in enumerate(lines) if line.startswith("| J16 |")]
    if len(hits) != 1:
        raise SystemExit(f"{name}: expected 1 J16 row, found {len(hits)}")
    before = "".join(lines)
    del lines[hits[0]]
    after = "".join(lines)
    path.write_text(after, encoding="utf-8")
    diff = "".join(difflib.unified_diff(
        before.splitlines(keepends=True),
        after.splitlines(keepends=True),
        fromfile="base/claim-excerpt-map.md",
        tofile=f"{name}/claim-excerpt-map.md",
    ))
    (SCRATCH / f"diff-{name}.txt").write_text(diff, encoding="utf-8")
    print(f"MUTANT {name}: dropped J16 table row; inventory declaration untouched")


def main():
    copy_base()
    print(f"BASE {BASE}")
    write_mutant("edge-reduction", [("timeline.json", EDGE_OLD, EDGE_NEW)])
    write_mutant("prose-word", [("fictional-excerpts.md", PROSE_OLD, PROSE_NEW)])
    drop_j16("map-row-drop")
    write_mutant("span-break", [("claim-excerpt-map.md", SPAN_OLD, SPAN_NEW)])
    write_mutant("source-id", [("timeline.json", SOURCE_OLD, SOURCE_NEW)])
    write_mutant("prose-word-nonanchor", [("claim-excerpt-map.md", PROSE_ISO_OLD, PROSE_ISO_NEW)])
    return 0


if __name__ == "__main__":
    sys.exit(main())
