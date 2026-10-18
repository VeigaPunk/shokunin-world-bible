#!/usr/bin/env python3
"""V54 seat: independent recompute of the dependency-freeze six-chain pins.

Reads raw JSON bytes from each fixture on disk and recomputes, independently of
the tool's code path (re-implemented from the contract's declared semantics):
  - per-file sha256 of raw bytes (hashlib, separate code path; cross-checked
    against sha256sum CLI separately)
  - content digest: sha256 of the compact sorted-JSON {name: per-file sha256}
    map (the operational definition the contract pins carry)
  - event inventory: event id -> {depends_on: sorted set, endpoint: {tick,
    entity_id, place_id}}
  - relation endpoint triples [from, to, type], sorted
  - counts {events, dependency_edges, relations, entities, sources}
and compares one-to-one against corpus/tools/dependency-freeze-contract.json
pins, per aspect.

Usage: recompute.py <repo-root> [--json <out.json>] [--baseline <contract.json>]
"""

import hashlib
import json
import sys
from pathlib import Path

DATA_FILES = ("entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json")
SIX = [
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
]


def sha256_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def content_digest(files):
    payload = json.dumps({n: sha256_bytes(r) for n, r in files.items()}, sort_keys=True, separators=(",", ":"))
    return sha256_bytes(payload.encode("utf-8"))


def build(fx: Path):
    files = {}
    for name in DATA_FILES:
        p = fx / name
        if p.is_file():
            files[name] = p.read_bytes()
    parsed = {n: json.loads(files[n].decode("utf-8")) for n in sorted(files)}
    events = {}
    for rec in parsed["timeline.json"]:
        events[rec["id"]] = {
            "depends_on": sorted(set(rec.get("depends_on", []))),
            "endpoint": {k: rec.get(k) for k in ("tick", "entity_id", "place_id")},
        }
    triples = sorted([r["from"], r["to"], r["type"]] for r in parsed["relations.json"])
    counts = {
        "events": len(events),
        "dependency_edges": sum(len(e["depends_on"]) for e in events.values()),
        "relations": len(triples),
    }
    for name, key in (("entities.json", "entities"), ("sources.json", "sources")):
        v = parsed.get(name)
        if isinstance(v, list):
            counts[key] = len(v)
    return {
        "files": {n: sha256_bytes(r) for n, r in sorted(files.items())},
        "content_sha256": content_digest(files),
        "events": events,
        "relations": triples,
        "counts": counts,
    }


def main():
    args = sys.argv[1:]
    root = Path(args[0]).resolve()
    json_out = None
    baseline = None
    i = 1
    while i < len(args):
        if args[i] == "--json":
            json_out = Path(args[i + 1])
            i += 2
        elif args[i] == "--baseline":
            baseline = json.loads(Path(args[i + 1]).read_text(encoding="utf-8"))
            i += 2
        else:
            raise SystemExit(f"unknown arg {args[i]}")
    contract = json.loads((root / "corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8"))
    pins = contract.get("pins", {})
    report = {"root": str(root), "contract_revision": contract.get("revision"), "fixtures": {}}
    verdict = 0
    for name in SIX:
        fx = root / "corpus/fixtures" / name
        entry = {"fixture_dir": str(fx), "aspects": {}}
        report["fixtures"][name] = entry
        pin = pins.get(name)
        if pin is None:
            entry["aspects"]["pin"] = "UNPINNED"
            verdict = 1
            continue
        if not fx.is_dir():
            entry["aspects"]["fixture_dir"] = "FIXTURE-MISSING"
            verdict = 1
            continue
        obs = build(fx)
        entry["observed"] = obs
        entry["pin_payload"] = pin
        entry["aspects"]["fixture_path"] = (
            "PASS" if pin.get("fixture") == f"corpus/fixtures/{name}" else
            f"FAIL pin={pin.get('fixture')!r} expected={'corpus/fixtures/' + name!r}"
        )
        entry["aspects"]["files"] = "PASS" if pin.get("files") == obs["files"] else "FAIL"
        entry["aspects"]["content_sha256"] = (
            "PASS" if pin.get("content_sha256") == obs["content_sha256"] else
            f"FAIL pin={pin.get('content_sha256')} observed={obs['content_sha256']}"
        )
        entry["aspects"]["events"] = "PASS" if pin.get("events") == obs["events"] else "FAIL"
        entry["aspects"]["relations"] = "PASS" if pin.get("relations") == obs["relations"] else "FAIL"
        entry["aspects"]["counts"] = (
            "PASS" if pin.get("counts") == obs["counts"] else
            f"FAIL pin={pin.get('counts')} observed={obs['counts']}"
        )
        if baseline is not None:
            bp = baseline.get("pins", {}).get(name)
            entry["baseline_pin"] = bp
            entry["baseline_equals_new"] = bp == pin
        if any(v != "PASS" for v in entry["aspects"].values()):
            verdict = 1
    if baseline is not None:
        report["baseline_revision"] = baseline.get("revision")
        report["baseline_pin_names"] = sorted(baseline.get("pins", {}))
        report["new_pin_names"] = sorted(pins)
    print(json.dumps({n: report["fixtures"][n].get("aspects", {}) for n in SIX}, indent=2))
    if baseline is not None:
        for name in SIX:
            e = report["fixtures"][name]
            if "baseline_pin" in e:
                print(f"BASELINE-EQUAL {name}: {e['baseline_equals_new']}")
            elif name in pins:
                print(f"NEW-PIN {name}: absent from baseline")
    if json_out:
        json_out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"VERDICT {'PASS' if verdict == 0 else 'FAIL'}")
    return verdict


if __name__ == "__main__":
    sys.exit(main())
