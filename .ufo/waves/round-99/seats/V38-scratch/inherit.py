#!/usr/bin/env python3
"""Compare r99-window-lapse to r98-clerk-filing. Read-only."""
import json
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
A = ROOT / "corpus/fixtures/r98-clerk-filing"
B = ROOT / "corpus/fixtures/r99-window-lapse"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

print("=== JSON prefix ===")
for name in ("entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json"):
    ja, jb = load(A / name), load(B / name)
    print(name, "len", len(ja), "->", len(jb), "prefix_identical", ja == jb[:len(ja)] if isinstance(jb, list) else ja == jb)

print("=== byte-identical files ===")
for name in ("entities.json", "relations.json", "contradictions.json", "inspiration-note.md", "source-excerpt.md"):
    print(name, (A / name).read_bytes() == (B / name).read_bytes())

ex_a = (A / "fictional-excerpts.md").read_bytes()
ex_b = (B / "fictional-excerpts.md").read_bytes()
print("excerpt prefix byte-identical", ex_b.startswith(ex_a))
print("excerpt added bytes", len(ex_b) - len(ex_a))

print("=== counts ===")
ent, rel, tl, src = load(B/"entities.json"), load(B/"relations.json"), load(B/"timeline.json"), load(B/"sources.json")
print("entities", len(ent), "relations", len(rel), "events", len(tl), "sources", len(src))
print("new source", src[-1]["id"] if src else None)
print("new event", {k: tl[-1][k] for k in ("id", "tick", "entity_id", "place_id", "depends_on", "source_id")})

print("=== map rows ===")
def rows(p):
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.startswith("| J") or line.startswith("| S"):
            out.append(line)
    return out

ra, rb = rows(A / "claim-excerpt-map.md"), rows(B / "claim-excerpt-map.md")
print("r98 rows", len(ra), "r99 rows", len(rb))

def ns_swap(line):
    return line.replace("r98-clerk-filing:", "r99-window-lapse:")

same = 0
differ = []
for i, (a, b) in enumerate(zip(ra, rb)):
    if ns_swap(a) == b:
        same += 1
    else:
        differ.append((i, a[:80], b[:80]))
print("inherited rows identical modulo namespace", same, "of", len(ra))
print("differing inherited", len(differ))
for item in differ[:8]:
    print(" DIFF", item)
if len(rb) > len(ra):
    print("new rows:")
    for line in rb[len(ra):]:
        print(line)
