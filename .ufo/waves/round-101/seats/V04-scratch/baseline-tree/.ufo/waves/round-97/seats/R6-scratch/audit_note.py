"""R6 scratch: audit every path/line citation inside the delivered knowledge note."""
import json, pathlib, re

ROOT = pathlib.Path(".")
NOTE = ROOT / "corpus/knowledge/r97-acknowledgment-scope-note.md"
text = NOTE.read_text()
BAD = []

# 1) every backticked path:line citation
cite = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|json|py)):(\d+)(?:-(\d+))?`")
n = 0
for m in cite.finditer(text):
    path, a, b = m.group(1), int(m.group(2)), m.group(3)
    p = ROOT / path
    if not p.exists():
        BAD.append(f"MISSING {path}")
        continue
    lines = p.read_text().splitlines()
    hi = int(b) if b else a
    if not (1 <= a <= len(lines)) or not (1 <= hi <= len(lines)):
        BAD.append(f"OUT-OF-RANGE {path}:{a}-{hi} (file {len(lines)})")
    n += 1
print(f"path:line citations found: {n}")

# 2) bare path citations (no line)
for m in re.finditer(r"`(corpus/[A-Za-z0-9_./-]+)`", text):
    p = ROOT / m.group(1)
    if not p.exists():
        BAD.append(f"MISSING bare path {m.group(1)}")

# 3) JSON pointer citations
for m in re.finditer(r"`([A-Za-z0-9_./-]+\.json)#(/\d+)`", text):
    path, ptr = m.group(1), m.group(2)
    p = ROOT / path
    if not p.exists():
        BAD.append(f"MISSING {path}"); continue
    obj = json.loads(p.read_text())
    idx = int(ptr.split("/")[1])
    if not isinstance(obj, list) or idx >= len(obj):
        BAD.append(f"POINTER {path}#{ptr} out of range (len {len(obj)})")

# 4) content probes at exact lines claimed in the note
probes = [
    ("corpus/fixtures/r97-crossing-acknowledgment/sources.json", 33, '"id": "aru-acknowledgment-note"'),
    ("corpus/fixtures/r97-crossing-acknowledgment/sources.json", 36, "receipt only"),
    ("corpus/fixtures/r97-crossing-acknowledgment/timeline.json", 55, '"id": "acknowledgment-aru-records"'),
    ("corpus/fixtures/r97-crossing-acknowledgment/timeline.json", 44, '"id": "response-evin-salt-court"'),
    ("corpus/fixtures/r97-crossing-acknowledgment/timeline.json", 33, '"id": "aftermath-missing-evin"'),
    ("corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md", 48, "Tick 13: I received Evin's response at the Chalk Stair."),
    ("corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md", 49, "both accounts stand unresolved"),
    ("corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md", 50, "I make no accusation against Evin, and I select no winner between us."),
    ("corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md", 51, "no reconciliation, no new duty"),
    ("corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md", 19, "for this crossing only"),
    ("corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md", 37, "Tick 12: I was at Salt Court through the same agreed bell."),
    ("corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md", 40, "Both accounts stand unresolved."),
    ("corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md", 53, "records receipt only"),
    ("corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md", 38, "Tick 13: I received Evin's response at the Chalk Stair."),
    ("corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md", 57, "no-reconciliation"),
    ("corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md", 51, "new tick-13 acknowledgment event"),
    ("corpus/fixtures/r97-crossing-acknowledgment/README.md", 3, "6 events / 6 sources"),
    ("corpus/fixtures/r97-crossing-acknowledgment/README.md", 7, "aru-acknowledgment-note"),
    ("corpus/fixtures/r97-crossing-acknowledgment/README.md", 11, "asserts no reconciliation"),
    ("corpus/fixtures/r97-crossing-acknowledgment/README.md", 13, "editorial encodings"),
    ("corpus/fixtures/r97-crossing-acknowledgment/README.md", 21, "17 source-attributed JSON pointer obligations"),
    ("corpus/fixtures/r96-crossing-response/claim-excerpt-map.md", 44, "|---|---|---|---|---:|---|---|"),
    ("corpus/fixtures/r96-crossing-response/claim-excerpt-map.md", 50, "The new tick-12 event encodes only Evin's second account"),
    ("corpus/fixtures/r35-bell7-conflict/manual-clause-pointer-map.md", 3, "editorial map"),
    ("corpus/fixtures/r35-bell7-conflict/manual-clause-pointer-map.md", 21, "Neither report is declared true/false"),
    ("corpus/fixtures/README.md", 761, "Neither wins."),
    ("corpus/knowledge/2026-10-12-lore-decision-table.md", 226, ""),
]
for path, ln, s in probes:
    p = ROOT / path
    lines = p.read_text().splitlines()
    ok = 1 <= ln <= len(lines) and (s == "" or s in lines[ln - 1])
    if not ok:
        BAD.append(f"PROBE {path}:{ln} expected {s!r}")

# 5) r96 map repair claims
r96map = (ROOT / "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md").read_text().splitlines()
if r96map[43].count("|") - 1 != 7:
    BAD.append("r96 :44 delimiter not 7 cells")
if r96map[19].count("|") - 1 != 8 or r96map[21].count("|") - 1 != 8:
    BAD.append("r96 facts table header/data not 8 cells")

print("BAD:", len(BAD))
for b in BAD:
    print(" ", b)
