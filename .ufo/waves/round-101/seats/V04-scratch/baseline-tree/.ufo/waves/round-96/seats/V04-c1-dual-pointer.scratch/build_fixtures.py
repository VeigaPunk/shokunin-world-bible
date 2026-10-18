#!/usr/bin/env python3
"""Build V04 r96 scratch fixture clusters for the legacy-dialect dual-pointer check."""
import json
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"

BASE_ENTITIES = [{
    "id": "test-entity",
    "first_appearance": "fixture-source",
    "claims": [{"statement": "test claim", "source_id": "fixture-source"}],
}]
BASE_RELATIONS = [{"from": "test-entity", "to": "other", "type": "linked", "source_id": "fixture-source"}]
BASE_TIMELINE = [{"id": "test-event", "source_id": "fixture-source"}]

LEGACY_HEADER = "| ID | JSON fact and fields | In-world source ID |"
CANON_HEADER = "| ID | JSON fact pointer | Source ID |"

LEGACY_CELLS = {
    "E1": "`entities[0].first_appearance`",
    "E2": "`entities[0].claims[0]`",
    "R1": "`relations[0]`",
    "T1": "`timeline[0]`",
}
CANON_CELLS = {
    "E1": "`entities.json#/0/first_appearance`",
    "E2": "`entities.json#/0/claims/0`",
    "R1": "`relations.json#/0`",
    "T1": "`timeline.json#/0`",
}

# name -> (header, cell table, per-row overrides)
CASES = [
    # legacy dialect: single-pointer shapes (must stay PASS)
    ("legacy-base", LEGACY_HEADER, LEGACY_CELLS, {}),
    ("legacy-single-paren", LEGACY_HEADER, LEGACY_CELLS,
     {"E1": "`entities[0].first_appearance` (Aru)"}),
    ("legacy-single-colon", LEGACY_HEADER, LEGACY_CELLS,
     {"E2": "`entities[0].claims[0]`: test claim text"}),
    ("legacy-single-both", LEGACY_HEADER, LEGACY_CELLS,
     {"T1": "`timeline[0]` (`description`, `source_id`): test event"}),
    # legacy dialect: second pointer token in prose (V37-D1; expect dual_pointer exit 1)
    ("legacy-dup-paren", LEGACY_HEADER, LEGACY_CELLS,
     {"E1": "`entities[0].first_appearance` (Aru; also `entities[1].first_appearance`)"}),
    ("legacy-dup-colon", LEGACY_HEADER, LEGACY_CELLS,
     {"E2": "`entities[0].claims[0]`: test claim; also `entities[1].first_appearance`"}),
    # second token that is itself a mapped raw obligation (timeline[0] mapped by T1)
    ("legacy-dup-paren-mapped", LEGACY_HEADER, LEGACY_CELLS,
     {"E2": "`entities[0].claims[0]`: test claim; also `timeline[0]`"}),
    # bare (unbackticked) second token probe
    ("legacy-dup-colon-bare", LEGACY_HEADER, LEGACY_CELLS,
     {"E2": "`entities[0].claims[0]`: test claim; see entities[1].first_appearance"}),
    # canonical-style second token inside a legacy cell probe
    ("legacy-dup-paren-canon", LEGACY_HEADER, LEGACY_CELLS,
     {"E1": "`entities[0].first_appearance` (see also `timeline.json#/0`)"}),
    # canonical fallback inside a legacy-header table (must stay PASS)
    ("legacy-canon-single", LEGACY_HEADER, LEGACY_CELLS,
     {"E1": "`entities.json#/0/first_appearance`"}),
    # canonical dialect controls
    ("canon-base", CANON_HEADER, CANON_CELLS, {}),
    ("canon-single-note", CANON_HEADER, CANON_CELLS,
     {"E1": "`entities.json#/0/first_appearance` (first appearance)"}),
    ("canon-dup-note", CANON_HEADER, CANON_CELLS,
     {"E1": "`entities.json#/0/first_appearance` (`entities.json#/0/claims/0`)"}),
    ("canon-dup-token", CANON_HEADER, CANON_CELLS,
     {"E1": "`entities.json#/0/first_appearance; entities.json#/0/claims/0`"}),
    ("canon-two-tokens", CANON_HEADER, CANON_CELLS,
     {"E1": "`entities.json#/0/first_appearance` `entities.json#/0/claims/0`"}),
    ("canon-note-plain", CANON_HEADER, CANON_CELLS,
     {"E1": "`entities.json#/0/first_appearance` (Aru)"}),
]


def build(name, header, cells, overrides):
    target = FIXTURES / name
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    (target / "entities.json").write_text(json.dumps(BASE_ENTITIES, indent=2) + "\n", encoding="utf-8")
    (target / "relations.json").write_text(json.dumps(BASE_RELATIONS, indent=2) + "\n", encoding="utf-8")
    (target / "timeline.json").write_text(json.dumps(BASE_TIMELINE, indent=2) + "\n", encoding="utf-8")
    lines = ["# V04 scratch mapping fixture: " + name, "", "## JSON facts", "", header, "|---|---|---|"]
    for row_id in ("E1", "E2", "R1", "T1"):
        cell = overrides.get(row_id, cells[row_id])
        lines.append(f"| {row_id} | {cell} | `fixture-source` |")
    (target / "claim-excerpt-map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    if FIXTURES.exists():
        shutil.rmtree(FIXTURES)
    for name, header, cells, overrides in CASES:
        build(name, header, cells, overrides)
    print(f"built {len(CASES)} fixtures under {FIXTURES}")


if __name__ == "__main__":
    main()
