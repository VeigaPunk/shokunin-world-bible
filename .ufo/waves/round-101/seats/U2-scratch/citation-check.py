"""U2 scratch: verify every quoted clause and cited path in the r101 R10 entry."""
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
ENTRY = ROOT / "corpus/knowledge/r101-r10-register-first-entry.md"

# (file, 1-based line, exact substring expected on that line)
LINE_QUOTES = [
    ("corpus/knowledge/r88-sourced-inspiration-decision-table.md", 26, "compare overlapping source-attributed claims with relevant landed-cluster claims and confirm a shared referent, field, and occasion"),
    ("corpus/knowledge/r88-sourced-inspiration-decision-table.md", 26, "cross-cluster comparison and register-reference checks are an explicit manual integration gate"),
    ("corpus/knowledge/r88-sourced-inspiration-decision-table.md", 26, "a per-cluster `CLEAN` is not cross-cluster evidence"),
    ("corpus/knowledge/r88-sourced-inspiration-decision-table.md", 93, "Only a source-backed shared"),
    ("corpus/knowledge/r88-sourced-inspiration-decision-table.md", 94, "referent, field, and occasion with incompatible assertions enters"),
    ("corpus/knowledge/r88-sourced-inspiration-decision-table.md", 97, "the register's first real entry awaits a genuine conflict"),
    ("corpus/knowledge/r88-sourced-inspiration-decision-table.md", 99, "**Namespace scoping (decided r91):**"),
    ("corpus/knowledge/r88-sourced-inspiration-decision-table.md", 110, "R10's proposed corpus-level register is a manual procedure until a corpus-wide validator exists"),
    ("corpus/fixtures/r94-paired-crossing/fictional-excerpts.md", 19, "There, they agreed, for this crossing only, to share stewardship of the Chalk Stair."),
    ("corpus/fixtures/r94-paired-crossing/fictional-excerpts.md", 20, "ninth-bell entries"),
    ("corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md", 26, "Tick 11: I waited at the Chalk Stair through the agreed bell."),
    ("corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md", 27, "Evin did not come."),
    ("corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md", 28, "The agreement we chalked covered this crossing only."),
    ("corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md", 29, "I assert no other duty, no breach, and no obligation beyond this crossing."),
    ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 37, "Tick 12: I was at Salt Court through the same agreed bell."),
    ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 38, "I make no accusation against Aru."),
    ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 39, "I select no winner between our two accounts."),
    ("corpus/fixtures/r96-crossing-response/fictional-excerpts.md", 40, "Both accounts stand unresolved."),
    ("corpus/fixtures/r100-docket-review/fictional-excerpts.md", 26, "Tick 11: I waited at the Chalk Stair through the agreed bell."),
    ("corpus/fixtures/r100-docket-review/fictional-excerpts.md", 37, "Tick 12: I was at Salt Court through the same agreed bell."),
    ("corpus/fixtures/r94-paired-crossing/README.md", 5, "## Namespace and occasion comparison"),
    ("corpus/fixtures/r95-crossing-aftermath/README.md", 5, "## Namespace and occasion comparison"),
    ("corpus/fixtures/r96-crossing-response/README.md", 5, "## Namespace and occasion comparison"),
    ("corpus/fixtures/r96-crossing-response/README.md", 9, "records only Evin's second account of the same occasion"),
    ("corpus/fixtures/r95-crossing-aftermath/README.md", 11, "no breach, no continuing obligation"),
    ("corpus/knowledge/r100-crossing-arc-synthesis.md", 46, "The reviewed relation is still the one crossing-only agreement sourced to"),
    ("corpus/knowledge/r100-crossing-arc-synthesis.md", 50, "Different actors at different places do not, by themselves, assert one actor's incompatible occupancy"),
    ("corpus/knowledge/r96-response-scope-note.md", 31, "different actors at different places"),
    ("corpus/knowledge/r96-response-scope-note.md", 40, "r35 two-sided-preservation precedent"),
    ("corpus/knowledge/r96-response-scope-note.md", 13, "r35 Bell-7 class"),
    ("corpus/knowledge/r93-r8-worked-example.md", 75, "r93 correction"),
    ("corpus/fixtures/README.md", 761, "Neither wins."),
    ("corpus/fixtures/r35-bell7-conflict/manual-clause-pointer-map.md", 3, "editorial map"),
    ("LOG.md", 2657, "zero shared referents or supported conflicts"),
]

# whole-file substring checks (any line)
SUBSTR_QUOTES = [
    ("corpus/fixtures/r95-crossing-aftermath/timeline.json", '"id": "aftermath-missing-evin"'),
    ("corpus/fixtures/r95-crossing-aftermath/timeline.json", '"depends_on": [\n      "paired-crossing-decision"\n    ]'),
    ("corpus/fixtures/r96-crossing-response/timeline.json", '"id": "response-evin-salt-court"'),
    ("corpus/fixtures/r96-crossing-response/timeline.json", '"depends_on": [\n      "aftermath-missing-evin"\n    ]'),
    ("corpus/fixtures/r95-crossing-aftermath/sources.json", '"id": "aru-aftermath-note"'),
    ("corpus/fixtures/r96-crossing-response/sources.json", '"id": "evin-response-note"'),
    ("corpus/fixtures/r94-paired-crossing/sources.json", '"id": "crossing-minute"'),
    ("corpus/fixtures/r35-bell7-conflict/contradictions.json", '"field": "place_id"'),
    ("corpus/knowledge/r88-sourced-inspiration-decision-table.md", "add a durable entry to `corpus/knowledge/cross-cluster-contradictions.md`"),
    ("corpus/knowledge/r89-cross-cluster-contradiction.md", "the second cluster is explicitly hypothetical"),
]

# JSON pointer value checks
import json
def jpointer(path, idx, expect_keys):
    data = json.loads((ROOT / path).read_text())
    row = data[idx]
    return all(row.get(k) == v for k, v in expect_keys.items())

fails = []
lines = {}
for path, lineno, frag in LINE_QUOTES:
    if path not in lines:
        lines[path] = (ROOT / path).read_text().splitlines()
    actual = lines[path][lineno - 1] if lineno - 1 < len(lines[path]) else "<EOF>"
    ok = frag in actual
    if not ok:
        fails.append(f"LINE-MISS {path}:{lineno} expected fragment: {frag!r}\n  actual: {actual!r}")

for path, frag in SUBSTR_QUOTES:
    text = (ROOT / path).read_text()
    if frag not in text:
        fails.append(f"SUB-MISS {path}: {frag!r}")

if not jpointer("corpus/fixtures/r95-crossing-aftermath/timeline.json", 3,
                {"id": "aftermath-missing-evin", "tick": 11, "entity_id": "aru",
                 "place_id": "chalk-stair", "depends_on": ["paired-crossing-decision"],
                 "source_id": "aru-aftermath-note"}):
    fails.append("POINTER-MISS r95 timeline.json#/3")
if not jpointer("corpus/fixtures/r96-crossing-response/timeline.json", 4,
                {"id": "response-evin-salt-court", "tick": 12, "entity_id": "evin",
                 "place_id": "salt-court", "depends_on": ["aftermath-missing-evin"],
                 "source_id": "evin-response-note"}):
    fails.append("POINTER-MISS r96 timeline.json#/4")
rel = json.loads((ROOT / "corpus/fixtures/r94-paired-crossing/relations.json").read_text())
if rel[0] != {"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing",
              "source_id": "crossing-minute"}:
    fails.append("POINTER-MISS r94 relations.json#/0")
if json.loads((ROOT / "corpus/fixtures/r95-crossing-aftermath/contradictions.json").read_text()) != []:
    fails.append("r95 contradictions.json not []")
if json.loads((ROOT / "corpus/fixtures/r96-crossing-response/contradictions.json").read_text()) != []:
    fails.append("r96 contradictions.json not []")
c35 = json.loads((ROOT / "corpus/fixtures/r35-bell7-conflict/contradictions.json").read_text())
t35 = json.loads((ROOT / "corpus/fixtures/r35-bell7-conflict/timeline.json").read_text())
if c35[0]["id"] != "bell7-location-reports" or c35[0]["claim_a"]["field"] != "place_id" or c35[0]["claim_b"]["field"] != "place_id":
    fails.append("r35 ledger #/0 shape")
if t35[2]["id"] != "tarin-envelope-observation" or t35[3]["id"] != "sella-bell7-presence":
    fails.append("r35 timeline #/2-3 ids")
if (ROOT / "corpus/knowledge/cross-cluster-contradictions.md").exists():
    fails.append("register file exists but entry claims absent")
src95 = json.loads((ROOT / "corpus/fixtures/r95-crossing-aftermath/sources.json").read_text())
src96 = json.loads((ROOT / "corpus/fixtures/r96-crossing-response/sources.json").read_text())
src94 = json.loads((ROOT / "corpus/fixtures/r94-paired-crossing/sources.json").read_text())
if src95[3]["id"] != "aru-aftermath-note": fails.append("r95 sources#/3 id")
if src96[4]["id"] != "evin-response-note": fails.append("r96 sources#/4 id")
if src94[2]["id"] != "crossing-minute": fails.append("r94 sources#/2 id")

# claimed sha prefixes
import hashlib
for fx in ["r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response",
           "r97-crossing-acknowledgment","r98-clerk-filing","r99-window-lapse","r100-docket-review"]:
    h = hashlib.sha256((ROOT / f"corpus/fixtures/{fx}/relations.json").read_bytes()).hexdigest()
    if not h.startswith("c279254bc7de0636"):
        fails.append(f"SHA-MISS {fx}: {h[:16]}")

# prefix chain claims
r94 = (ROOT / "corpus/fixtures/r94-paired-crossing/fictional-excerpts.md").read_bytes()
r95b = (ROOT / "corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md").read_bytes()
r96b = (ROOT / "corpus/fixtures/r96-crossing-response/fictional-excerpts.md").read_bytes()
if not r95b.startswith(r94): fails.append("r94 not prefix of r95")
if not r96b.startswith(r95b): fails.append("r95 not prefix of r96")

print(f"line-quote checks: {len(LINE_QUOTES)}, substring checks: {len(SUBSTR_QUOTES)}, pointer/derived checks: 15")
if fails:
    print(f"CITATION-CHECK FAIL ({len(fails)}):")
    for f in fails:
        print(" -", f)
    raise SystemExit(1)
print("CITATION-CHECK PASS: every cited line quote, path, JSON pointer, byte-identity, prefix-chain, and absence claim in the entry verified against the delivered tree.")
