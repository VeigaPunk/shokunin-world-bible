#!/usr/bin/env python3
"""Independent raw-obligation enumerator for V77.

Does not import map_obligations.py. Grammar (from map-obligations-contract.json):
one obligation per entity first_appearance, one per entity claim, one per
relation record, one per timeline record. Pointer form is file.json#/<index>[/...].
"""

import json
import re
import sys
from pathlib import Path


def raw_obligations(cluster: Path):
    entities = json.loads((cluster / "entities.json").read_text(encoding="utf-8"))
    relations = json.loads((cluster / "relations.json").read_text(encoding="utf-8"))
    timeline = json.loads((cluster / "timeline.json").read_text(encoding="utf-8"))
    if not all(isinstance(x, list) for x in (entities, relations, timeline)):
        raise SystemExit("roots must be arrays")
    out = []
    for i, entity in enumerate(entities):
        fa = entity.get("first_appearance")
        if not isinstance(fa, str) or not fa.strip():
            raise SystemExit(f"entities/{i}/first_appearance missing")
        out.append((f"entities.json#/{i}/first_appearance", fa, "first_appearance", entity.get("id")))
        claims = entity.get("claims", [])
        if not isinstance(claims, list):
            raise SystemExit(f"entities/{i}/claims not a list")
        for j, claim in enumerate(claims):
            sid = claim.get("source_id")
            if not isinstance(sid, str) or not sid.strip():
                raise SystemExit(f"entities/{i}/claims/{j}/source_id missing")
            out.append((f"entities.json#/{i}/claims/{j}", sid, "claim", entity.get("id")))
    for i, rel in enumerate(relations):
        sid = rel.get("source_id")
        if not isinstance(sid, str) or not sid.strip():
            raise SystemExit(f"relations/{i}/source_id missing")
        out.append((f"relations.json#/{i}", sid, "relation", rel.get("type")))
    for i, event in enumerate(timeline):
        sid = event.get("source_id")
        if not isinstance(sid, str) or not sid.strip():
            raise SystemExit(f"timeline/{i}/source_id missing")
        out.append((f"timeline.json#/{i}", sid, "event", event.get("id")))
    return out


ROW = re.compile(r"^\| (J\d+) \|")


def map_rows(path: Path):
    rows = []
    in_facts = False
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("## JSON facts"):
            in_facts = True
            continue
        if in_facts and line.startswith("## "):
            break
        if not in_facts or not line.startswith("| J"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        pointer = re.search(r"`([^`]+)`", cells[1])
        source = cells[2].strip("`")
        anchor = cells[7].strip()
        span = cells[5]
        excerpt = cells[4]
        rows.append({
            "line": n,
            "id": cells[0],
            "pointer": pointer.group(1) if pointer else None,
            "source_id": source,
            "excerpt": excerpt,
            "span": span,
            "anchor": anchor,
        })
    return rows


def main():
    cluster = Path(sys.argv[1])
    raw = raw_obligations(cluster)
    rows = map_rows(cluster / "claim-excerpt-map.md")
    print(f"INDEPENDENT raw={len(raw)} mapped_rows={len(rows)}")
    kinds = {}
    for pointer, sid, kind, label in raw:
        kinds[kind] = kinds.get(kind, 0) + 1
        print(f"RAW {kind} {pointer} source_id={sid!r} label={label!r}")
    print("KINDS " + " ".join(f"{k}={v}" for k, v in kinds.items()))
    by_pointer = {p: (sid, kind, label) for p, sid, kind, label in raw}
    print("--- map rows ---")
    for row in rows:
        raw_hit = by_pointer.get(row["pointer"])
        bind = "UNBOUND"
        if raw_hit is not None:
            bind = "BIND-OK" if raw_hit[0] == row["source_id"] else f"BIND-MISMATCH raw={raw_hit[0]!r}"
        print(
            f"MAP {row['id']} line={row['line']} pointer={row['pointer']} "
            f"source_id={row['source_id']!r} span={row['span']} {bind}"
        )
        print(f"    excerpt={row['excerpt']} anchor={row['anchor']}")
    mapped_pointers = [r["pointer"] for r in rows]
    missing = [p for p, *_ in raw if p not in mapped_pointers]
    phantom = [p for p in mapped_pointers if p not in by_pointer]
    print(f"MISSING {missing}")
    print(f"PHANTOM {phantom}")
    print(f"ROW_IDS {[r['id'] for r in rows]}")


if __name__ == "__main__":
    main()
