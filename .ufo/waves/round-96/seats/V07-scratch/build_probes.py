#!/usr/bin/env python3
"""Build legacy-dialect / inventory probe clusters for the r96 V07 review.

Scratch-only: writes under .ufo/waves/round-96/scratch/V07/probes/.
Each probe is a self-contained cluster: entities.json, relations.json,
timeline.json, claim-excerpt-map.md.
"""

import json
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE / "probes"

HEADER_LEGACY = "| ID | JSON fact and fields | In-world source ID |"
HEADER_CANON = "| ID | JSON fact pointer | In-world source ID |"

BASE_ROWS = [
    ("E1", "entities[0].claims[0]", "src-a"),
    ("E2", "entities[0].first_appearance", "src-a"),
    ("R1", "relations[0]", "src-a"),
    ("T1", "timeline[0]", "src-a"),
]

# probe name -> (override cell text, header, inventory line, drop row index)
# the override replaces the cell of the row whose pointer it names (row index 1 for
# first_appearance probes, row index 0 otherwise); see override_index() below.
PROBES = {
    # --- legitimate r88-faithful cells: must stay exit 0 ---
    "legit-paren-fieldlist": ("`entities[0].claims[0]` (`statement`, `source_id`): prose", HEADER_LEGACY, None, None),
    "legit-paren-name": ("`entities[0].first_appearance` (Aru)", HEADER_LEGACY, None, None),
    "legit-colon-prose": ("`entities[0].claims[0]`: Aru carries the north lantern at tick 9", HEADER_LEGACY, None, None),
    "legit-paren-empty": ("`entities[0].claims[0]` ()", HEADER_LEGACY, None, None),
    "legit-prose-mentions-file": ("`entities[0].claims[0]`: see timeline.json for the event", HEADER_LEGACY, None, None),
    "legit-bare-text-bracket": ("`entities[0].claims[0]`: the entities[9] row was struck", HEADER_LEGACY, None, None),
    "legit-bare-text-hash": ("`entities[0].claims[0]`: see entities.json#/0/name for the name field", HEADER_LEGACY, None, None),
    "legit-canonical-under-legacy": ("`entities.json#/0/claims/0`", HEADER_LEGACY, None, None),
    "legit-inv-match": (None, HEADER_LEGACY, "**Expected inventory:** 4 JSON facts; 0 editorial rows; 4 total mapped rows; 0 distinct excerpt anchors.", None),
    "legit-canon-under-canon": (None, HEADER_CANON, None, None),
    "legit-backtick-anchor-token": ("`entities[0].claims[0]`: `fictional-excerpts.md:12`", HEADER_LEGACY, None, None),
    "legit-paren-mixed-tokens": ("`entities[0].claims[0]` (Aru, `statement`)", HEADER_LEGACY, None, None),
    "legit-paren-rownote": ("`entities[0].claims[0]` (row E1)", HEADER_LEGACY, None, None),
    "dual-colon-foreign-file": ("`entities[0].claims[0]`: also `sources.json#/0`", HEADER_LEGACY, None, None),

    # --- dual pointers: must become exit 1 dual_pointer ---
    "dual-paren-canonical": ("`entities[0].claims[0]` (also `relations.json#/0`)", HEADER_LEGACY, None, None),
    "dual-paren-legacy-phantom": ("`entities[0].claims[0]` (also `entities[9].claims[0]`)", HEADER_LEGACY, None, None),
    "dual-colon-canonical": ("`entities[0].claims[0]`: also `timeline.json#/0`", HEADER_LEGACY, None, None),
    "dual-colon-legacy-phantom": ("`entities[0].claims[0]`: also `entities[9].claims[0]`", HEADER_LEGACY, None, None),
    "dual-paren-legacy-real-unmapped": ("`entities[0].claims[0]` (also `relations[0]`)", HEADER_LEGACY, None, 2),
    "dual-two-backtick-tokens": ("`entities[0].claims[0]` `relations[0]`", HEADER_LEGACY, None, None),
    "dual-equiv-restated": ("`entities[0].claims[0]` (canonical `entities.json#/0/claims/0`)", HEADER_LEGACY, None, None),
    "dual-canonical-note-pointer": ("`entities.json#/0/claims/0` (also `relations.json#/0`)", HEADER_LEGACY, None, None),

    # --- inventory gating ---
    "inv-declared-high": (None, HEADER_LEGACY, "**Expected inventory:** 9 JSON facts; 0 editorial rows; 9 total mapped rows; 0 distinct excerpt anchors.", None),
    "inv-declared-low": (None, HEADER_LEGACY, "**Expected inventory:** 2 JSON facts; 0 editorial rows; 2 total mapped rows; 0 distinct excerpt anchors.", None),
    "inv-malformed": (None, HEADER_LEGACY, "**Expected inventory:** four JSON facts; no editorial rows.", None),
    "inv-declared-total-wrong": (None, HEADER_LEGACY, "**Expected inventory:** 4 JSON facts; 0 editorial rows; 5 total mapped rows; 0 distinct excerpt anchors.", None),
    "inv-anchors-wrong": (None, HEADER_LEGACY, "**Expected inventory:** 4 JSON facts; 0 editorial rows; 4 total mapped rows; 7 distinct excerpt anchors.", None),
    "inv-absent": (None, HEADER_LEGACY, None, None),
    "inv-editorial-wrong": (None, HEADER_LEGACY, "**Expected inventory:** 4 JSON facts; 3 editorial rows; 7 total mapped rows; 0 distinct excerpt anchors.", None),
    "inv-duplicate-lines": (None, HEADER_LEGACY, "**Expected inventory:** 4 JSON facts; 0 editorial rows; 4 total mapped rows; 0 distinct excerpt anchors.\n\n**Expected inventory:** 9 JSON facts; 0 editorial rows; 9 total mapped rows; 0 distinct excerpt anchors.", None),
}

# deletion class: remove the claim from raw AND its map row; inventory declaration left stale
DELETION_PROBES = {
    "deletion-class-stale-declaration": "**Expected inventory:** 4 JSON facts; 0 editorial rows; 4 total mapped rows; 0 distinct excerpt anchors.",
    "deletion-class-redeclared": "**Expected inventory:** 3 JSON facts; 0 editorial rows; 3 total mapped rows; 0 distinct excerpt anchors.",
}


def write_raw(cluster, with_claim=True, extra_key=None):
    entity = {
        "id": "test-entity",
        "kind": "character",
        "name": "Aru",
        "first_appearance": "src-a",
    }
    if with_claim:
        entity["claims"] = [{"statement": "Aru carries the north lantern", "source_id": "src-a"}]
    if extra_key:
        entity[extra_key] = [{"statement": "hidden claim", "source_id": "src-a"}]
    files = {
        "entities.json": [entity],
        "relations.json": [{"from": "test-entity", "to": "other", "type": "linked", "source_id": "src-a"}],
        "timeline.json": [{"id": "test-event", "tick": 9, "description": "Aru carries the lantern", "source_id": "src-a"}],
    }
    for name, value in files.items():
        (cluster / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def override_index(rows, override):
    """Row index whose default cell the override replaces (matches the pointer it names)."""
    for index, (_, pointer, _) in enumerate(rows):
        if override and override.startswith(f"`{pointer}`"):
            return index
    return 0


def write_map(cluster, rows, header, inventory, override=None):
    lines = ["# V07 probe cluster", "", "## JSON facts", "", header, "|---|---|---|"]
    target = override_index(rows, override)
    for index, (row_id, pointer, source_id) in enumerate(rows):
        cell = override if (override is not None and index == target) else f"`{pointer}`"
        lines.append(f"| {row_id} | {cell} | `{source_id}` |")
    if inventory:
        lines += ["", "## Inventory", "", *inventory.split("\n")]
    (cluster / "claim-excerpt-map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    if BASE.exists():
        shutil.rmtree(BASE)
    for name, (override, header, inventory, drop_index) in PROBES.items():
        cluster = BASE / name
        cluster.mkdir(parents=True)
        rows = [row for index, row in enumerate(BASE_ROWS) if index != drop_index]
        write_raw(cluster, with_claim=True)
        write_map(cluster, rows, header, inventory, override)
    for name, inventory in DELETION_PROBES.items():
        cluster = BASE / name
        cluster.mkdir(parents=True)
        rows = [row for index, row in enumerate(BASE_ROWS) if index != 0]
        write_raw(cluster, with_claim=False)
        write_map(cluster, rows, HEADER_LEGACY, inventory)
    print(f"built {len(PROBES) + len(DELETION_PROBES)} probes under {BASE}")


if __name__ == "__main__":
    main()
