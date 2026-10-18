#!/usr/bin/env python3
"""V06 c1-negative-rerun (round 96): build accumulated negative-control cases.

Base = byte copy of corpus/fixtures/r93-m2-kojiki-cluster (same subject r94 F11
and r95 V04 used, so finding-ID deltas are the tool's, not the harness's).
Cases a-f replicate F11/V04 one-for-one; g/h/i add the r95-carried and r96
classes (schema_drift, inventory_mismatch deletion class, dual_pointer).
"""
import json
import shutil
from pathlib import Path

SC = Path(__file__).resolve().parent
BASE = SC / "base"
MAP_NAME = "claim-excerpt-map.md"
LEGACY_RAW = SC / "legacy-raw"


def fresh(name):
    target = SC / name
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(BASE, target)
    return target


def map_lines(case):
    return (case / MAP_NAME).read_text(encoding="utf-8").splitlines(keepends=True)


def write_map(case, lines):
    (case / MAP_NAME).write_text("".join(lines), encoding="utf-8")


def e1_index(lines):
    hits = [i for i, line in enumerate(lines)
            if line.startswith("| E1 |") and "entities.json#/0/first_appearance" in line]
    assert len(hits) == 1, hits
    return hits[0]


def e2_index(lines):
    hits = [i for i, line in enumerate(lines)
            if line.startswith("| E2 |") and "entities.json#/0/claims/0" in line]
    assert len(hits) == 1, hits
    return hits[0]


def read_entities(case):
    return json.loads((case / "entities.json").read_text(encoding="utf-8"))


def write_entities(case, entities):
    (case / "entities.json").write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- a-f (F11 set)
# (a) raw claim with no map row
case = fresh("case-a")
entities = read_entities(case)
entities[0]["claims"].append({
    "statement": "Teva adds a second unregistered note to the folio margin.",
    "source_id": "m2-record-archive",
})
write_entities(case, entities)

# (b) duplicate map row (exact copy of the E1 row)
case = fresh("case-b")
lines = map_lines(case)
lines.insert(e1_index(lines) + 1, lines[e1_index(lines)])
write_map(case, lines)

# (c) map row pointing at a non-obligation (well-formed pointer, no raw record)
case = fresh("case-c")
lines = map_lines(case)
row = lines[e1_index(lines)]
phantom = row.replace("`entities.json#/0/first_appearance`", "`entities.json#/99/first_appearance`")
phantom = phantom.replace("| E1 |", "| E99 |", 1)
lines.insert(e1_index(lines) + 1, phantom)
write_map(case, lines)

# (d) map row source ID differs from the raw source ID
case = fresh("case-d")
lines = map_lines(case)
idx = e1_index(lines)
assert lines[idx].count("`m2-record-archive`") == 1, lines[idx]
lines[idx] = lines[idx].replace("`m2-record-archive`", "`m2-other-archive`")
write_map(case, lines)

# (e) malformed raw JSON (entities.json truncated mid-array)
case = fresh("case-e")
text = (case / "entities.json").read_text(encoding="utf-8")
(case / "entities.json").write_text(text[: len(text) // 2], encoding="utf-8")

# (f) invalid map path: base copy intact; only the --map argument varies
case = fresh("case-f")
outside = SC / "outside-map"
if outside.exists():
    shutil.rmtree(outside)
outside.mkdir()
shutil.copy2(BASE / MAP_NAME, outside / MAP_NAME)

# ------------------------------------------------- g: schema_drift (r95 class)
# g1: rename entities[0] 'claims' key (content preserved) AND remove its map row
case = fresh("case-g1")
entities = read_entities(case)
entities[0]["claim_records"] = entities[0].pop("claims")
write_entities(case, entities)
lines = map_lines(case)
del lines[e2_index(lines)]
write_map(case, lines)

# g2: rename entities[0] 'claims' key, keep its map row (row becomes phantom)
case = fresh("case-g2")
entities = read_entities(case)
entities[0]["claim_records"] = entities[0].pop("claims")
write_entities(case, entities)

# --------------------------------- h: inventory deletion class (r96 class C1a)
# h1: delete entities[0] 'claims' key AND its map row -> declared 12 vs observed 11
case = fresh("case-h1")
entities = read_entities(case)
del entities[0]["claims"]
write_entities(case, entities)
lines = map_lines(case)
del lines[e2_index(lines)]
write_map(case, lines)

# h2: delete one claim entry (entities[1].claims[0]) AND its map row -> 12 vs 11
case = fresh("case-h2")
entities = read_entities(case)
entities[1]["claims"].pop(0)
write_entities(case, entities)
lines = map_lines(case)
hits = [i for i, line in enumerate(lines)
        if line.startswith("| E4 |") and "entities.json#/1/claims/0" in line]
assert len(hits) == 1, hits
del lines[hits[0]]
write_map(case, lines)

# ------------------------------- i: dual_pointer probes (r96 class C1c, V37-D1)
# small legacy-dialect cluster (header "JSON fact and fields"), raw copied from
# V37's probe raw files; maps vary only in the pointer cell.
legacy = SC / "legacy-base"
if legacy.exists():
    shutil.rmtree(legacy)
legacy.mkdir()
for name in ("entities.json", "relations.json", "timeline.json"):
    shutil.copy2(LEGACY_RAW / name, legacy / name)

LEGACY_MAP_HEAD = (
    "# probe\n\n## JSON facts\n\n"
    "| ID | JSON fact and fields | In-world source ID |\n"
    "|---|---|---|\n"
)


def legacy_case(name, rows):
    target = SC / name
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(legacy, target)
    (target / MAP_NAME).write_text(LEGACY_MAP_HEAD + rows, encoding="utf-8")
    return target


# i1: parenthetical names a canonical second pointer (V37 legacy-paren-hidden-canonical)
legacy_case("case-i1",
            "| P1 | `entities[0].first_appearance` (also `relations.json#/0`) | `paired-clock` |\n"
            "| P2 | `entities.json#/0/claims/0` | `paired-clock` |\n"
            "| P3 | `timeline.json#/0` | `paired-clock` |\n")

# i2: parenthetical names a legacy second pointer (V37 legacy-paren-hidden-legacy)
legacy_case("case-i2",
            "| P1 | `entities[0].first_appearance` (also `entities[9].claims[0]`) | `paired-clock` |\n"
            "| P2 | `entities.json#/0/claims/0` | `paired-clock` |\n"
            "| P3 | `timeline.json#/0` | `paired-clock` |\n")

# i3: colon prose names a legacy second pointer (V37 legacy-colon-hidden-pointer)
legacy_case("case-i3",
            "| P1 | `entities[0].first_appearance`: also `entities[9].claims[0]` | `paired-clock` |\n"
            "| P2 | `entities.json#/0/claims/0` | `paired-clock` |\n"
            "| P3 | `timeline.json#/0` | `paired-clock` |\n")

# i4: colon prose names an already-mapped second pointer (V37 legacy-colon-hidden-mapped)
legacy_case("case-i4",
            "| P1 | `entities[0].first_appearance`: also `entities[0].claims[0]` | `paired-clock` |\n"
            "| P3 | `timeline.json#/0` | `paired-clock` |\n")

# i5 (boundary): colon prose names a second token WITHOUT backticks
legacy_case("case-i5",
            "| P1 | `entities[0].first_appearance`: also entities[9].claims[0] | `paired-clock` |\n"
            "| P2 | `entities.json#/0/claims/0` | `paired-clock` |\n"
            "| P3 | `timeline.json#/0` | `paired-clock` |\n")

# i6 (boundary): parenthetical repeats the SAME pointer token
legacy_case("case-i6",
            "| P1 | `entities[0].first_appearance` (also `entities[0].first_appearance`) | `paired-clock` |\n"
            "| P2 | `entities.json#/0/claims/0` | `paired-clock` |\n"
            "| P3 | `timeline.json#/0` | `paired-clock` |\n")

# i7 (boundary): parenthetical names a malformed second token
legacy_case("case-i7",
            "| P1 | `entities[0].first_appearance` (also `entities[00].claims[0]`) | `paired-clock` |\n"
            "| P2 | `entities.json#/0/claims/0` | `paired-clock` |\n"
            "| P3 | `timeline.json#/0` | `paired-clock` |\n")

# ------------------------------------------------------------- controls (no false-fire)
# ctrl-1: legacy cell with a non-pointer parenthetical note
legacy_case("ctrl-legacy-note",
            "| P1 | `entities[0].first_appearance` (Aru) | `paired-clock` |\n"
            "| P2 | `entities.json#/0/claims/0` | `paired-clock` |\n"
            "| P3 | `timeline.json#/0` | `paired-clock` |\n")

# ctrl-2: legacy cell with non-pointer colon prose
legacy_case("ctrl-legacy-prose",
            "| P1 | `entities[0].first_appearance`: Aru's first row | `paired-clock` |\n"
            "| P2 | `entities.json#/0/claims/0` | `paired-clock` |\n"
            "| P3 | `timeline.json#/0` | `paired-clock` |\n")

# ctrl-3: canonical header, parenthetical names a pointer -> must stay unsupported_map exit 2
ctrl = fresh("ctrl-canonical-note")
lines = map_lines(ctrl)
idx = e1_index(lines)
lines[idx] = lines[idx].replace("(`teva`)", "(`teva`; also `relations.json#/0`)")
write_map(ctrl, lines)

# ctrl-4: declared inventory wrong on an otherwise-clean cluster (V37 inv-declared-wrong
#         style): declared 12 -> 99 in a copy of the r93 map, rows untouched.
ctrl = fresh("ctrl-inv-declared-wrong")
lines = map_lines(ctrl)
for i, line in enumerate(lines):
    if line.startswith("**Expected inventory:**"):
        lines[i] = "**Expected inventory:** 99 JSON facts; 3 editorial rows; 102 total mapped rows; 15 distinct excerpt anchors.\n"
write_map(ctrl, lines)

# ctrl-5: malformed inventory declaration (V37 inv-malformed style)
ctrl = fresh("ctrl-inv-malformed")
lines = map_lines(ctrl)
for i, line in enumerate(lines):
    if line.startswith("**Expected inventory:**"):
        lines[i] = "**Expected inventory:** twelve JSON facts; three editorial rows.\n"
write_map(ctrl, lines)

# ctrl-6: control for the h1 deletion shape on the NEW r96 fixture is added later
#         (build-h-on-r96.py) once Q4's fixture lands.

print("built:", sorted(p.name for p in SC.iterdir() if p.is_dir()))
