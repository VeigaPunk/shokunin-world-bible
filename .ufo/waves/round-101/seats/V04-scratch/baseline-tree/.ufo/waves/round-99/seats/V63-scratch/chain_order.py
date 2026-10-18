#!/usr/bin/env python3
"""V63 independent chain-order + freeze-edge enumeration. Does not import the tool."""
import hashlib, json, os, sys

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
CHAIN = [
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
    "r99-window-lapse",
]
EXPECTED_TICKS = [9, 9, 10, 11, 12, 13, 14, 15]

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def load_timeline(name):
    p = os.path.join(LANE, "corpus/fixtures", name, "timeline.json")
    raw = open(p, "rb").read()
    data = json.loads(raw.decode("utf-8"))
    if not isinstance(data, list):
        raise SystemExit(f"{name}: timeline root is {type(data).__name__}, expected list")
    return data, raw

def edges_of(events):
    """Edge set as sorted (src, dst) pairs from raw depends_on lists, order-preserving within a row but set-compared."""
    out = []
    by_id = {}
    for e in events:
        by_id[e["id"]] = e
        for dep in e.get("depends_on") or []:
            out.append((dep, e["id"]))
    return out, by_id

def main():
    contract_path = os.path.join(LANE, "corpus/tools/dependency-freeze-contract.json")
    contract = json.load(open(contract_path))
    pins = contract.get("pins", {})
    print("schema_version", contract.get("schema_version"))
    print("pin_keys", list(pins.keys()))
    print("data_files", contract.get("data_files"))
    print("---")
    failures = []
    for name in CHAIN:
        tl_path = os.path.join(LANE, "corpus/fixtures", name, "timeline.json")
        if not os.path.exists(tl_path):
            print(f"ABSENT {name}")
            failures.append(f"absent:{name}")
            continue
        events, raw = load_timeline(name)
        ticks = [e.get("tick") for e in events]
        ids = [e.get("id") for e in events]
        edge_list, by_id = edges_of(events)
        print(f"FIXTURE {name}")
        print(f"  ids={ids}")
        print(f"  ticks={ticks}")
        print(f"  n_events={len(events)} n_edges={len(edge_list)}")
        # strictly backward
        bad = []
        missing = []
        for dep, dst in edge_list:
            if dep not in by_id:
                missing.append((dep, dst))
                continue
            dt = by_id[dep].get("tick")
            st = by_id[dst].get("tick")
            if not (isinstance(dt, int) and isinstance(st, int) and dt < st):
                bad.append((dep, dt, dst, st))
        print(f"  edges={edge_list}")
        print(f"  backward={'OK' if not bad and not missing else 'FAIL'} bad={bad} missing_targets={missing}")
        if bad or missing:
            failures.append(f"order:{name}")
        # expected prefix of 9,9,10,...
        if ticks != EXPECTED_TICKS[:len(ticks)]:
            print(f"  TICK-SEQUENCE MISMATCH expected {EXPECTED_TICKS[:len(ticks)]} got {ticks}")
            failures.append(f"ticks:{name}")
        else:
            print(f"  tick-sequence OK (prefix of 9,9,10,11,12,13,14,15)")
        # pin edge set
        pin = pins.get(name)
        if pin is None:
            print(f"  PIN ABSENT")
            failures.append(f"unpin:{name}")
            continue
        pin_events = pin.get("events") or {}
        pin_edges = []
        for eid, body in pin_events.items():
            for dep in body.get("depends_on") or []:
                pin_edges.append((dep, eid))
        pin_edges_sorted = sorted(pin_edges)
        raw_edges_sorted = sorted(edge_list)
        match = pin_edges_sorted == raw_edges_sorted
        print(f"  pin_edges={pin_edges_sorted}")
        print(f"  raw_edges={raw_edges_sorted}")
        print(f"  EDGE-SET {'MATCH' if match else 'MISMATCH'}")
        if not match:
            failures.append(f"edges:{name}")
            only_pin = [e for e in pin_edges_sorted if e not in raw_edges_sorted]
            only_raw = [e for e in raw_edges_sorted if e not in pin_edges_sorted]
            print(f"    only_pin={only_pin} only_raw={only_raw}")
        # also compare per-event depends_on lists exactly (sorted, as pin stores sorted)
        for e in events:
            eid = e["id"]
            raw_deps = list(e.get("depends_on") or [])
            pin_deps = list((pin_events.get(eid) or {}).get("depends_on") or [])
            if sorted(raw_deps) != pin_deps and sorted(raw_deps) != sorted(pin_deps):
                print(f"    dep-list mismatch {eid} raw={raw_deps} pin={pin_deps}")
                failures.append(f"deplist:{name}:{eid}")
            elif eid not in pin_events:
                print(f"    event missing from pin: {eid}")
                failures.append(f"missing-event:{name}:{eid}")
        extra = set(pin_events) - {e["id"] for e in events}
        if extra:
            print(f"    pin has extra events {extra}")
            failures.append(f"extra-event:{name}")
        # endpoint ticks
        for e in events:
            pe = (pin_events.get(e["id"]) or {}).get("endpoint") or {}
            if pe.get("tick") != e.get("tick"):
                print(f"    endpoint tick mismatch {e['id']} raw={e.get('tick')} pin={pe.get('tick')}")
                failures.append(f"endpoint:{name}:{e['id']}")
        print(f"  pin_counts={pin.get('counts')}")
        print(f"  pin_nfiles={len(pin.get('files') or {})} file_keys={sorted((pin.get('files') or {}).keys())}")
    print("---")
    print("FAILURES", failures if failures else "NONE")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
