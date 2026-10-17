#!/usr/bin/env python3
"""R5 scratch: dump fact rows from a fixture map using the real tools' parsers."""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sc = load("support_check", ROOT / "corpus/tools/support_check.py")
mo = load("map_obligations", ROOT / "corpus/tools/map_obligations.py")


def dump(map_path):
    map_path = Path(map_path)
    facts, modes, inv = sc.parse_map(map_path)
    rows, declared, malformed, editorial_rows, gating = mo.parse_map_text(
        map_path.read_text(encoding="utf-8")
    )
    return {
        "expected_inventory": inv,
        "declared": declared,
        "malformed": malformed,
        "editorial_row_count": editorial_rows,
        "gating": gating,
        "excerpt_modes": modes,
        "facts": facts,
        "pointers": rows,
    }


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(json.dumps({"path": p, "data": dump(p)}, indent=1, sort_keys=True))
