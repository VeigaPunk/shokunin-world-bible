"""R6 scratch: verify every path/line citation used in r97-acknowledgment-scope-note.md."""
import json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(".")
BAD = []


def line(path, n, must_contain):
    p = ROOT / path
    if not p.exists():
        BAD.append(f"MISSING {path}")
        return
    lines = p.read_text().splitlines()
    if not (1 <= n <= len(lines)):
        BAD.append(f"OUT-OF-RANGE {path}:{n} (file has {len(lines)})")
        return
    if must_contain not in lines[n - 1]:
        BAD.append(f"CONTENT {path}:{n} expected {must_contain!r} got {lines[n-1][:100]!r}")


def exists(path):
    if not (ROOT / path).exists():
        BAD.append(f"MISSING {path}")


F = "corpus/fixtures/r97-crossing-acknowledgment"
R96 = "corpus/fixtures/r96-crossing-response"
R95 = "corpus/fixtures/r95-crossing-aftermath"
R35 = "corpus/fixtures/r35-bell7-conflict"

for f in ["sources.json", "timeline.json", "entities.json", "relations.json",
          "contradictions.json", "fictional-excerpts.md", "README.md",
          "claim-excerpt-map.md", "inspiration-note.md", "source-excerpt.md"]:
    exists(f"{F}/{f}")

# --- sources.json ---
line(f"{F}/sources.json", 33, '"id": "aru-acknowledgment-note"')
line(f"{F}/sources.json", 36, "receipt only")
line(f"{F}/sources.json", 27, '"id": "evin-response-note"')
# --- timeline.json ---
line(f"{F}/timeline.json", 55, '"id": "acknowledgment-aru-records"')
line(f"{F}/timeline.json", 56, '"tick": 13')
line(f"{F}/timeline.json", 57, '"entity_id": "aru"')
line(f"{F}/timeline.json", 58, '"place_id": "chalk-stair"')
line(f"{F}/timeline.json", 60, '"response-evin-salt-court"')
line(f"{F}/timeline.json", 63, '"source_id": "aru-acknowledgment-note"')
line(f"{F}/timeline.json", 44, '"id": "response-evin-salt-court"')
line(f"{F}/timeline.json", 33, '"id": "aftermath-missing-evin"')
# --- fictional-excerpts.md ---
line(f"{F}/fictional-excerpts.md", 48, "Tick 13: I received Evin's response at the Chalk Stair.")
line(f"{F}/fictional-excerpts.md", 49, "I hold to my own account; both accounts stand unresolved.")
line(f"{F}/fictional-excerpts.md", 50, "I make no accusation against Evin, and I select no winner between us.")
line(f"{F}/fictional-excerpts.md", 51, "I assert no reconciliation, no new duty, and no obligation beyond this crossing.")
line(f"{F}/fictional-excerpts.md", 19, "for this crossing only")
line(f"{F}/fictional-excerpts.md", 26, "Tick 11: I waited at the Chalk Stair through the agreed bell.")
line(f"{F}/fictional-excerpts.md", 37, "Tick 12: I was at Salt Court through the same agreed bell.")
line(f"{F}/fictional-excerpts.md", 40, "Both accounts stand unresolved.")
# --- r35 precedent ---
exists(f"{R35}/contradictions.json")
line("corpus/fixtures/README.md", 761, "Neither wins.")
exists(f"{R35}/manual-clause-pointer-map.md")
# --- r95/r96 notes ---
exists("corpus/knowledge/r95-aftermath-scope-note.md")
exists("corpus/knowledge/r96-response-scope-note.md")

print("BASIC BAD:", len(BAD))
for b in BAD:
    print(" ", b)

# --- parsed equality / byte identity ---
r96, r97 = ROOT / R96, ROOT / F
for f in ["entities.json", "relations.json", "contradictions.json", "inspiration-note.md", "source-excerpt.md"]:
    same = (r96 / f).read_bytes() == (r97 / f).read_bytes()
    print(f"byte-identical r96/r97 {f}: {same}")
t96 = json.loads((r96 / "timeline.json").read_text())
t97 = json.loads((r97 / "timeline.json").read_text())
s96 = json.loads((r96 / "sources.json").read_text())
s97 = json.loads((r97 / "sources.json").read_text())
print("r97 timeline[:5]==r96:", t97[:5] == t96, "| events", len(t97))
print("r97 sources[:5]==r96:", s97[:5] == s96, "| sources", len(s97))
print("contradictions r97:", (r97 / "contradictions.json").read_text().strip())
e97 = json.loads((r97 / "entities.json").read_text())
rel97 = json.loads((r97 / "relations.json").read_text())
print("entities:", len(e97), "relations:", len(rel97))
