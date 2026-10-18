#!/usr/bin/env python3
"""V11 r98 prep: parsed-row inheritance + independent raw recount (read-only)."""
import json
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
sys.path.insert(0, str(ROOT / "corpus" / "tools"))
import support_check  # noqa: E402

r97 = ROOT / "corpus/fixtures/r97-crossing-acknowledgment"
r98 = ROOT / "corpus/fixtures/r98-clerk-filing"

rows97, modes97, inv97 = support_check.parse_map(r97 / "claim-excerpt-map.md")
rows98, modes98, inv98 = support_check.parse_map(r98 / "claim-excerpt-map.md")
print("inv97", inv97)
print("inv98", inv98)
print("rows97", len(rows97), "rows98", len(rows98))
print("inherited prefix parse-equal:", rows98[: len(rows97)] == rows97)
extra = rows98[len(rows97):]
for r in extra:
    print("EXTRA ROW:", r)

for fx in (r97, r98):
    e = json.loads((fx / "entities.json").read_text())
    rel = json.loads((fx / "relations.json").read_text())
    t = json.loads((fx / "timeline.json").read_text())
    s = json.loads((fx / "sources.json").read_text())
    fa = sum(1 for x in e if "first_appearance" in x)
    cl = sum(len(x.get("claims", [])) for x in e)
    print(f"{fx.name}: fa={fa} claims={cl} rel={len(rel)} timeline={len(t)} RAW_TOTAL={fa+cl+len(rel)+len(t)} sources={len(s)}")
