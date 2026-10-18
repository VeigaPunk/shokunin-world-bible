import json, pathlib, sys
target = pathlib.Path(sys.argv[1])
dual = len(sys.argv) > 2 and sys.argv[2] == "dual"
target.mkdir(parents=True, exist_ok=True)
files = {
    "entities.json": [{
        "id": "test-entity",
        "first_appearance": "fixture-source",
        "claims": [{"statement": "test claim", "source_id": "fixture-source"}],
    }],
    "relations.json": [{
        "from": "test-entity", "to": "other", "type": "linked", "source_id": "fixture-source",
    }],
    "timeline.json": [{"id": "test-event", "source_id": "fixture-source"}],
}
for name, value in files.items():
    (target / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
e2 = "`entities[0].claims[0]` (also `timeline[0]`)" if dual else "`entities[0].claims[0]`"
lines = [
    "# Isolated legacy-dialect fixture (hand-derived R2 r97)",
    "",
    "## JSON facts",
    "",
    "| ID | JSON fact and fields | In-world source ID |",
    "|---|---|---|",
    "| E1 | `entities[0].first_appearance` | `fixture-source` |",
    f"| E2 | {e2} | `fixture-source` |",
    "| R1 | `relations[0]` | `fixture-source` |",
    "| T1 | `timeline[0]` | `fixture-source` |",
    "",
]
(target / "claim-excerpt-map.md").write_text("\n".join(lines), encoding="utf-8")
print(f"built {target} dual={dual}")
