import json, sys, pathlib
base = pathlib.Path(sys.argv[1]); base.mkdir(parents=True, exist_ok=True)
def ent(with_drift):
    e = {"id": "test-entity", "first_appearance": "fixture-source",
         "claims": [{"statement": "test claim", "source_id": "fixture-source"}]}
    if with_drift:
        e["claim_records"] = [{"statement": "drift claim", "source_id": "fixture-source"}]
    return [e]
files = {
    "relations.json": [{"from": "test-entity", "to": "other", "type": "linked", "source_id": "fixture-source"}],
    "timeline.json": [{"id": "test-event", "source_id": "fixture-source"}],
}
rows = [("E1", "entities.json#/0/first_appearance"), ("E2", "entities.json#/0/claims/0"),
        ("R1", "relations.json#/0"), ("T1", "timeline.json#/0")]
map_text = "\n".join(["# Isolated mapping fixture", "", "## JSON facts", "",
    "| ID | JSON fact pointer and fields | In-world source ID |", "|---|---|---|"] +
    [f"| {i} | `{p}` | `fixture-source` |" for i, p in rows]) + "\n"
for name, val in files.items():
    (base / name).write_text(json.dumps(val, indent=2) + "\n")
(base / "claim-excerpt-map.md").write_text(map_text)
(base / "entities-control.json").write_text(json.dumps(ent(False), indent=2) + "\n")
(base / "entities-drift.json").write_text(json.dumps(ent(True), indent=2) + "\n")
print("wrote", base)
