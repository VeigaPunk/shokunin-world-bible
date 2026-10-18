#!/usr/bin/env python3
"""Materialize W13 isolated wrong-source map-obligation controls."""

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "W13-source-controls"
SOURCE = "m2-record-archive"
OTHER_VALID = "m2-record-other-valid"
UNKNOWN = "m2-record-not-in-catalog"

CASES = {
    "first-appearance-valid-other": ("entities.json#/0/first_appearance", "other-valid"),
    "claim-valid-other": ("entities.json#/0/claims/0", "other-valid"),
    "relation-valid-other": ("relations.json#/0", "other-valid"),
    "timeline-valid-other": ("timeline.json#/0", "other-valid"),
    "first-appearance-unknown-id": ("entities.json#/0/first_appearance", "unknown"),
}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def materialize(name, pointer, replacement):
    case = OUT / name
    case.mkdir(parents=True, exist_ok=True)
    wrong_map_id = {"other-valid": OTHER_VALID, "unknown": UNKNOWN}[replacement]

    entity = {
        "id": "control-entity",
        "kind": "character",
        "name": "Control Entity",
        "first_appearance": SOURCE,
        "claims": [],
    }
    relation = []
    timeline = []
    if pointer == "entities.json#/0/claims/0":
        entity["claims"] = [{"statement": "Isolated control claim.", "source_id": SOURCE}]
    elif pointer == "relations.json#/0":
        relation = [{"from": "control-entity", "to": "control-entity", "type": "control_edge", "source_id": SOURCE}]
    elif pointer == "timeline.json#/0":
        timeline = [{"id": "control-event", "tick": 1, "entity_id": "control-entity", "place_id": "control-entity", "depends_on": [], "description": "Isolated control event.", "source_id": SOURCE}]

    write_json(case / "entities.json", [entity])
    write_json(case / "relations.json", relation)
    write_json(case / "timeline.json", timeline)
    write_json(case / "sources.json", [
        {"id": SOURCE, "title": "Canonical control source"},
        {"id": OTHER_VALID, "title": "Distinct valid control source"},
    ])
    write_json(case / "contradictions.json", [])
    (case / "control-excerpt.md").write_text(
        "# Isolated source-binding excerpt\n\n"
        "Delivery mode (R9): verbatim\n\n"
        "Baseline control anchor.\n"
        "Target control anchor.\n",
        encoding="utf-8",
    )

    obligations = [("BASE", "entities.json#/0/first_appearance", SOURCE, 5, "Baseline control anchor.")]
    if pointer == "entities.json#/0/first_appearance":
        obligations = [("TARGET", pointer, SOURCE, 6, "Target control anchor.")]
    else:
        obligations.append(("TARGET", pointer, SOURCE, 6, "Target control anchor."))

    rows = []
    for label, raw_pointer, raw_source_id, line, anchor in obligations:
        map_source_id = wrong_map_id if label == "TARGET" else raw_source_id
        rows.append(
            f"| {label} | `{raw_pointer}` (source-attributed obligation) | `{map_source_id}` | "
            f"`control-excerpt.md:{line}` | `verbatim` | `{anchor}` |"
        )
    expected = len(obligations)
    map_text = (
        "# Isolated source-binding map\n\n"
        f"**Expected inventory:** {expected} JSON fact{'s' if expected != 1 else ''}; "
        f"0 editorial rows; {expected} total mapped row{'s' if expected != 1 else ''}; "
        f"{expected} distinct excerpt anchor{'s' if expected != 1 else ''}.\n\n"
        "## R9 excerpt declarations\n\n"
        "| Excerpt path and lines | Source | Delivery mode | Status |\n"
        "|---|---|---|---|\n"
        "| `control-excerpt.md:5-6` | `m2-record-archive` | `verbatim` | Isolated control text. |\n\n"
        "## JSON facts\n\n"
        "| ID | JSON fact pointer and fields | In-world source ID | Excerpt path | R9 delivery mode | Exact anchor |\n"
        "|---|---|---|---|---|---|\n"
        + "\n".join(rows)
        + "\n"
    )
    (case / "claim-excerpt-map.md").write_text(map_text, encoding="utf-8")

    raw_id = SOURCE
    sources = {entry["id"] for entry in json.loads((case / "sources.json").read_text(encoding="utf-8"))}
    assert raw_id in sources
    assert (wrong_map_id in sources) == (replacement == "other-valid")
    assert wrong_map_id != raw_id
    return case, pointer, raw_id, wrong_map_id, replacement


def main():
    results = [materialize(name, *spec) for name, spec in CASES.items()]
    print(f"CONTROLS {len(results)} root={OUT.relative_to(Path(__file__).resolve().parents[4])}")
    for case, pointer, raw_id, map_id, validity in results:
        print(
            f"EXPECTED source_id_mismatch pointer={pointer} raw={raw_id} "
            f"map={map_id} map_id_status={validity} input={case.name}"
        )


if __name__ == "__main__":
    main()
