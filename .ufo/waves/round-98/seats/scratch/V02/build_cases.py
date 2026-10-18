#!/usr/bin/env python3
"""V02 case builder: stage S1's delivered tool+contract with mutated legacy pins.

Reads the LIVE repo bytes (S1 delivery) and builds self-contained scratch roots
under .ufo/waves/round-98/seats/scratch/V02/cases/<case>/ so each --freeze run
resolves ROOT to its own root and can never touch the delivered contract.
"""
import json
import pathlib
import shutil
import sys

REPO = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
BASE = REPO / ".ufo/waves/round-98/seats/scratch/V02"
CASES = BASE / "cases"
FIXTURE = "r95-crossing-aftermath"
PIN = "r95-crossing-aftermath"

VARIANTS = {
    "legacy_missing_key": lambda pin: pin.pop("fixture", None),
    "legacy_null": lambda pin: pin.__setitem__("fixture", None),
    "legacy_nonstring": lambda pin: pin.__setitem__("fixture", 123),
    "legacy_empty_string": lambda pin: pin.__setitem__("fixture", ""),
    "legacy_other_path": lambda pin: pin.__setitem__("fixture", "corpus/fixtures/r96-crossing-response"),
    "legacy_out_of_scope_path": lambda pin: pin.__setitem__("fixture", "corpus/knowledge"),
    "garbage_traversal": lambda pin: pin.__setitem__("fixture", "../../outside"),
    "legacy_verify_only": lambda pin: pin.pop("fixture", None),
}


def build(variant):
    root = CASES / variant
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    (root / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(REPO / "corpus/tools/dependency_freeze.py", root / "corpus/tools/dependency_freeze.py")
    shutil.copytree(REPO / "corpus/fixtures" / FIXTURE, root / "corpus/fixtures" / FIXTURE)
    contract = json.loads((REPO / "corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8"))
    VARIANTS[variant](contract["pins"][PIN])
    (root / "corpus/tools/dependency-freeze-contract.json").write_text(
        json.dumps(contract, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return root


if __name__ == "__main__":
    names = sys.argv[1:] or list(VARIANTS)
    for name in names:
        print("built", build(name))
