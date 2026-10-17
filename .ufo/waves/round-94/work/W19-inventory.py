#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def collect(cluster):
    base = Path("corpus/fixtures") / cluster
    rows = []

    def add(file_name, pointer, source_id):
        if not isinstance(source_id, str) or not source_id:
            raise ValueError(f"missing source ID at {base / file_name}#/{pointer}")
        rows.append({
            "pointer": (base / file_name).as_posix() + "#/" + pointer,
            "source_id": source_id,
        })

    entities = load_json(ROOT / base / "entities.json")
    for index, entity in enumerate(entities):
        add("entities.json", f"{index}/first_appearance", entity["first_appearance"])
        for claim_index, claim in enumerate(entity["claims"]):
            add("entities.json", f"{index}/claims/{claim_index}", claim["source_id"])

    for file_name in ("relations.json", "timeline.json"):
        for index, record in enumerate(load_json(ROOT / base / file_name)):
            add(file_name, str(index), record["source_id"])

    rows.sort(key=lambda row: (row["pointer"], row["source_id"]))
    if len({row["pointer"] for row in rows}) != len(rows):
        raise ValueError(f"duplicate obligation pointer in {base}")
    return rows


def main():
    observed_at = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    inventories = []
    expected_counts = {
        "r93-m2-kojiki-cluster": 12,
        "r88-m3-maya-cluster": 10,
    }
    for cluster, expected_count in expected_counts.items():
        pairs = collect(cluster)
        inventories.append({
            "snapshot": cluster,
            "tree_revision": "9c2eea3b58a090f8820c7a723d2f6a22b46ae52b",
            "expected_count": expected_count,
            "observed_count": len(pairs),
            "pairs": pairs,
        })

    r94_path = Path("corpus/fixtures/r94-paired-crossing")
    actual_r94 = {"path": r94_path.as_posix(), "observed_at_utc": observed_at}
    if not (ROOT / r94_path).exists():
        actual_r94["status"] = "absent"
    else:
        try:
            pairs = collect("r94-paired-crossing")
            actual_r94.update({
                "status": "observed",
                "expected_count": 14,
                "observed_count": len(pairs),
                "matches_declared_count": len(pairs) == 14,
                "pairs": pairs,
            })
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            actual_r94.update({
                "status": "could_not_evaluate",
                "error": f"{type(exc).__name__}: {exc}",
            })

    result = {
        "seat": "W19",
        "purpose": "independent raw JSON source-attributed obligation denominator",
        "observed_at_utc": observed_at,
        "counting_rule": "Entities contribute first_appearance and each claim; relations and timeline contribute each record; only raw source-attributed pointers are counted.",
        "inventories": inventories,
        "r94_declared": {
            "basis": "round-94 wave-spec.md C1 declared continuation",
            "expected_count": 14,
            "decomposition": {
                "entity_first_appearance": 5,
                "entity_claim": 5,
                "relation": 1,
                "timeline_event": 3,
            },
            "actual_candidate": actual_r94,
        },
        "scope_limit": "These are raw source-attributed obligation counts, not universal semantic coverage or entailment findings.",
    }
    output = Path(__file__).with_name("W19-obligations.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    counts = ", ".join(f"{row['snapshot']}={row['observed_count']}/{row['expected_count']}" for row in inventories)
    print(f"W19 raw inventory: {counts}; r94 candidate={actual_r94['status']} at {observed_at}")
    return 0 if all(row["observed_count"] == row["expected_count"] for row in inventories) else 1


if __name__ == "__main__":
    raise SystemExit(main())
