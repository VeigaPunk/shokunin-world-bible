#!/usr/bin/env python3
"""V06 bonus: deletion-class case on the delivered r96 fixture.

Copies corpus/fixtures/r96-crossing-response -> case-r96-del and removes
entities[0]'s claims key plus every map row that binds entities.json#/0/claims/N
(the C1(a) deletion class shape), then the caller runs the new tool on it.
Run only when the fixture exists.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SC = ROOT / ".ufo/waves/round-96/seats/V06-scratch"
SRC = ROOT / "corpus/fixtures/r96-crossing-response"
DST = SC / "case-r96-del"

if not SRC.is_dir():
    sys.exit("r96 fixture absent")
if DST.exists():
    shutil.rmtree(DST)
shutil.copytree(SRC, DST)

ents = json.loads((DST / "entities.json").read_text(encoding="utf-8"))
removed = ents[0].pop("claims", None)
(DST / "entities.json").write_text(json.dumps(ents, indent=2) + "\n", encoding="utf-8")

MAP = DST / "claim-excerpt-map.md"
lines = MAP.read_text(encoding="utf-8").splitlines(keepends=True)
kept = [l for l in lines
        if not (l.lstrip().startswith("|") and re.search(r"entities\.json#/0/claims/[0-9]+", l))]
MAP.write_text("".join(kept), encoding="utf-8")
print(f"case-r96-del built; removed claims key with {len(removed or [])} entries; "
      f"map rows dropped={len(lines) - len(kept)}")
