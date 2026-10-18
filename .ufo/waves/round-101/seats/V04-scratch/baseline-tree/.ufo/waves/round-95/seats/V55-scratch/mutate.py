#!/usr/bin/env python3
"""V55 scratch: build BR-02 mutation copies of r94-paired-crossing."""
import json
import shutil
import sys
from pathlib import Path

SRC = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r94-paired-crossing")
HERE = Path(__file__).resolve().parent


def build(name, entity_index, new_key, remove_pointer, keep_row=False):
    dst = HERE / name
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(SRC, dst)
    entities = json.loads((dst / "entities.json").read_text(encoding="utf-8"))
    record = entities[entity_index]
    assert "claims" in record, record
    record[new_key] = record.pop("claims")  # rename, content preserved
    (dst / "entities.json").write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")
    if not keep_row:
        map_path = dst / "claim-excerpt-map.md"
        lines = map_path.read_text(encoding="utf-8").splitlines(keepends=True)
        kept, removed = [], 0
        for line in lines:
            if f"`{remove_pointer}`" in line:
                removed += 1
                continue
            kept.append(line)
        assert removed == 1, f"removed={removed}"
        map_path.write_text("".join(kept), encoding="utf-8")
    print(f"built {name}: entity[{entity_index}] claims->{new_key}, row {remove_pointer} removed={not keep_row}")


if __name__ == "__main__":
    build("mut1-rename0-removerow", 0, "claim_list", "entities.json#/0/claims/0")
    build("mut2-rename2-removerow", 2, "assertions", "entities.json#/2/claims/0")
    build("mut3-rename0-keeprow", 0, "claim_list", "entities.json#/0/claims/0", keep_row=True)
    # mut4: benign extra key on entity 0, no map change (false-positive probe)
    dst = HERE / "mut4-benign-extrakey"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(SRC, dst)
    entities = json.loads((dst / "entities.json").read_text(encoding="utf-8"))
    entities[0]["notes"] = "editorial margin note"
    (dst / "entities.json").write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")
    print("built mut4-benign-extrakey: entity[0] notes added, map unchanged")
    # control: pristine copy
    dst = HERE / "control-pristine"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(SRC, dst)
    print("built control-pristine")
