#!/usr/bin/env python3
"""Independently compare r93 raw source-ID obligations to map rows."""

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CLUSTER = ROOT / "corpus" / "fixtures" / "r93-m2-kojiki-cluster"
MAP = CLUSTER / "claim-excerpt-map.md"
POINTER = re.compile(r"`((?:entities|relations|timeline)\.json#/[^`]+)`")


def load(name):
    return json.loads((CLUSTER / name).read_text(encoding="utf-8"))


def main():
    raw = []
    for index, entity in enumerate(load("entities.json")):
        if isinstance(entity.get("first_appearance"), str):
            pointer = f"entities.json#/{index}/first_appearance"
            raw.append((pointer, pointer, entity["first_appearance"]))
        for claim_index, claim in enumerate(entity.get("claims", [])):
            if isinstance(claim, dict) and "source_id" in claim:
                map_pointer = f"entities.json#/{index}/claims/{claim_index}"
                raw.append((f"{map_pointer}/source_id", map_pointer, claim["source_id"]))
    for name in ("relations.json", "timeline.json"):
        for index, row in enumerate(load(name)):
            if isinstance(row, dict) and "source_id" in row:
                map_pointer = f"{name}#/{index}"
                raw.append((f"{map_pointer}/source_id", map_pointer, row["source_id"]))

    mapped = []
    in_json_facts = False
    for line in MAP.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_json_facts = line == "## JSON facts (12 source-attributed pointers)"
        if not in_json_facts or not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells or cells[0] == "ID":
            continue
        match = POINTER.search(cells[1])
        if match:
            mapped.append((match.group(1), cells[2].strip().strip("`")))

    raw_counts = Counter(map_pointer for _, map_pointer, _ in raw)
    map_counts = Counter(pointer for pointer, _ in mapped)
    raw_by_pointer = {map_pointer: source_id for _, map_pointer, source_id in raw}
    map_by_pointer = dict(mapped)
    pointer_sets_equal = set(raw_by_pointer) == set(map_by_pointer)
    source_ids_equal = raw_by_pointer == map_by_pointer
    one_to_one = all(count == 1 for count in raw_counts.values()) and all(count == 1 for count in map_counts.values())
    print(
        f"RAW {len(raw)} MAP {len(mapped)} POINTERS_EQUAL {pointer_sets_equal} "
        f"SOURCE_IDS_EQUAL {source_ids_equal} ONE_TO_ONE {one_to_one}"
    )
    for raw_location, map_pointer, source_id in raw:
        print(
            f"raw_location={raw_location} map_pointer={map_pointer} "
            f"raw={source_id} map={map_by_pointer.get(map_pointer)}"
        )
    return 0 if len(raw) == 12 and len(mapped) == 12 and pointer_sets_equal and source_ids_equal and one_to_one else 1


if __name__ == "__main__":
    raise SystemExit(main())
