import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[4]
old = root / "corpus/fixtures/r88-m3-maya-cluster"
new = root / "corpus/fixtures/r94-paired-crossing"


def load(directory, name):
    return json.loads((directory / name).read_text(encoding="utf-8"))


old_entities = load(old, "entities.json")
new_entities = load(new, "entities.json")
old_timeline = load(old, "timeline.json")
new_timeline = load(new, "timeline.json")
old_sources = load(old, "sources.json")
new_sources = load(new, "sources.json")
new_relations = load(new, "relations.json")

assert len(old_entities) == 4 and new_entities[:4] == old_entities
assert load(old, "relations.json") == []
assert len(new_relations) == 1
assert len(old_timeline) == 2 and new_timeline[:2] == old_timeline
assert new_entities[-1]["id"] == "chalk-stair"
assert new_timeline[2]["id"] == "paired-crossing-decision"
assert new_timeline[2]["tick"] == 10
assert new_timeline[2]["depends_on"] == ["aru-ninth-bell", "evin-ninth-bell"]
assert new_sources[:2] == old_sources
for name in ("source-excerpt.md", "inspiration-note.md"):
    assert (new / name).read_bytes() == (old / name).read_bytes()
assert (new / "fictional-excerpts.md").read_text(encoding="utf-8").splitlines()[:13] == (
    old / "fictional-excerpts.md"
).read_text(encoding="utf-8").splitlines()

map_lines = (new / "claim-excerpt-map.md").read_text(encoding="utf-8").splitlines()
json_rows = [line for line in map_lines if re.match(r"\| J\d{2} \|", line)]
pointers = [re.match(r"\| J\d{2} \| `([^`]+)`", line).group(1) for line in json_rows]
assert len(json_rows) == 14 and len(set(pointers)) == 14
assert all(re.fullmatch(r"(?:entities|relations|timeline)\.json#/(?:\d+)(?:/(?:first_appearance|claims/\d+))?", pointer) for pointer in pointers)
assert len(new_entities) == 5 and len(new_relations) == 1 and len(new_timeline) == 3

print("INHERITED: 4/4 entity records, 2/2 timeline events, and 2/2 source records parsed-value equal")
print("INHERITED CONTEXT: source-excerpt.md and inspiration-note.md byte-identical; fictional excerpt lines 1-13 identical")
print("COUNTS: 4/0/2 -> 5/1/3 entities/relations/events")
print("TICK 10: both aru-ninth-bell and evin-ninth-bell dependencies present")
print("MAP: 14 unique canonical JSON pointers")
