import hashlib
import json
import subprocess
import unicodedata
from pathlib import Path

FIXTURES = Path("corpus/fixtures")
NAMES = (
    "r93-m2-kojiki-cluster",
    "r87-myth-cluster",
    "r88-m3-maya-cluster",
)


def key(value):
    value = unicodedata.normalize("NFKD", value).casefold()
    return "".join(
        char
        for char in value
        if not unicodedata.combining(char) and char.isalnum()
    )


def read_json(root, filename):
    return json.loads((root / filename).read_text(encoding="utf-8"))


def collect_alias_fields(value, filename, path="$", found=None):
    if found is None:
        found = []
    if isinstance(value, dict):
        for field, child in value.items():
            if field.casefold() in {"alias", "aliases", "epithet", "epithets"}:
                found.append({"file": filename, "path": f"{path}.{field}", "value": child})
            collect_alias_fields(child, filename, f"{path}.{field}", found)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            collect_alias_fields(child, filename, f"{path}[{index}]", found)
    return found


def review_input_sha256(root):
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name != "README.md":
            digest.update(path.relative_to(root).as_posix().encode("utf-8"))
            digest.update(b"\0")
            digest.update(path.read_bytes())
    return digest.hexdigest()


def inventory(name):
    root = FIXTURES / name
    entities = read_json(root, "entities.json")
    sources = read_json(root, "sources.json")
    timeline = read_json(root, "timeline.json")
    relations = read_json(root, "relations.json")
    entity_ids = {key(entity["id"]) for entity in entities}
    labels = {
        key(label)
        for entity in entities
        for label in [
            entity["name"],
            *entity.get("aliases", []),
            *entity.get("epithets", []),
        ]
    }
    event_ids = {key(event["id"]) for event in timeline}
    source_ids = {key(source["id"]) for source in sources}
    source_titles = {key(source["title"]) for source in sources}
    relation_endpoints = {
        key(value)
        for relation in relations
        for value in (relation["from"], relation["to"])
    }
    event_endpoints = {
        key(value)
        for event in timeline
        for value in (event["entity_id"], event["place_id"])
    }
    dependencies = {
        key(value)
        for event in timeline
        for value in event["depends_on"]
    }
    def reference_values(value):
        if isinstance(value, dict):
            direct = [
                child
                for field, child in value.items()
                if field in {"source_id", "first_appearance"} and isinstance(child, str)
            ]
            nested = [reference for child in value.values() for reference in reference_values(child)]
            return direct + nested
        if isinstance(value, list):
            return [reference for child in value for reference in reference_values(child)]
        return []

    source_refs = {
        key(value)
        for path in sorted(root.glob("*.json"))
        for value in reference_values(json.loads(path.read_text(encoding="utf-8")))
    }
    alias_fields = []
    for path in sorted(root.glob("*.json")):
        alias_fields.extend(
            collect_alias_fields(
                json.loads(path.read_text(encoding="utf-8")), path.name
            )
        )
    return {
        "name": name,
        "review_input_sha256": review_input_sha256(root),
        "entities": [
            {
                "id": entity["id"],
                "kind": entity["kind"],
                "name": entity["name"],
                "aliases": entity.get("aliases", []),
                "epithets": entity.get("epithets", []),
                "first_appearance": entity.get("first_appearance"),
                "claims": entity.get("claims", []),
            }
            for entity in entities
        ],
        "sources": sources,
        "events": timeline,
        "relations": relations,
        "alias_epithet_fields_found": alias_fields,
        "normalized": {
            "entity_ids": sorted(entity_ids),
            "entity_labels_aliases_epithets": sorted(labels),
            "event_ids": sorted(event_ids),
            "source_ids_bare": sorted(source_ids),
            "source_ids_path_qualified": sorted(f"{name}:{value}" for value in source_ids),
            "source_titles": sorted(source_titles),
            "source_references": sorted(source_refs),
            "relation_endpoints": sorted(relation_endpoints),
            "event_entity_place_endpoints": sorted(event_endpoints),
            "event_dependencies": sorted(dependencies),
        },
    }


def cross_compare(incoming, prior):
    a = incoming["normalized"]
    b = prior["normalized"]
    a_ids, b_ids = set(a["entity_ids"]), set(b["entity_ids"])
    a_labels, b_labels = set(a["entity_labels_aliases_epithets"]), set(
        b["entity_labels_aliases_epithets"]
    )
    a_entity_keys, b_entity_keys = a_ids | a_labels, b_ids | b_labels
    return {
        "prior_cluster": prior["name"],
        "entity_id_id": sorted(a_ids & b_ids),
        "entity_label_label": sorted(a_labels & b_labels),
        "entity_id_label_either_direction": sorted((a_ids & b_labels) | (b_ids & a_labels)),
        "event_id_id": sorted(set(a["event_ids"]) & set(b["event_ids"])),
        "source_id_bare": sorted(set(a["source_ids_bare"]) & set(b["source_ids_bare"])),
        "source_id_path_qualified": sorted(
            set(a["source_ids_path_qualified"]) & set(b["source_ids_path_qualified"])
        ),
        "source_title_title": sorted(set(a["source_titles"]) & set(b["source_titles"])),
        "source_reference_ids": sorted(set(a["source_references"]) & set(b["source_references"])),
        "m2_relation_or_event_endpoint_to_prior_entity_key": sorted(
            (set(a["relation_endpoints"]) | set(a["event_entity_place_endpoints"])) & b_entity_keys
        ),
        "prior_relation_or_event_endpoint_to_m2_entity_key": sorted(
            (set(b["relation_endpoints"]) | set(b["event_entity_place_endpoints"])) & a_entity_keys
        ),
        "m2_event_dependency_to_prior_event_id": sorted(
            set(a["event_dependencies"]) & set(b["event_ids"])
        ),
        "prior_event_dependency_to_m2_event_id": sorted(
            set(b["event_dependencies"]) & set(a["event_ids"])
        ),
        "m2_event_id_to_prior_entity_key": sorted(set(a["event_ids"]) & b_entity_keys),
        "prior_event_id_to_m2_entity_key": sorted(set(b["event_ids"]) & a_entity_keys),
    }


fixtures = {name: inventory(name) for name in NAMES}
m2 = fixtures[NAMES[0]]
result = {
    "measured_revision": subprocess.run(
        ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip(),
    "normalization": "Unicode NFKD; casefold; remove combining marks; retain alphanumeric code points",
    "scope": "all fixture JSON entity/source/event/relation records, aliases/epithets, source references, endpoints, dependencies, plus semantic review of delivered prose and parallel notes",
    "fixtures": list(fixtures.values()),
    "cross_cluster_keys": [
        cross_compare(m2, fixtures[name]) for name in NAMES[1:]
    ],
}
print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
