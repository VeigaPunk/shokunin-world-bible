#!/usr/bin/env python3
"""V18: cross-check contract pins against independent oracle + actual bytes."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
sys.path.insert(0, str(ROOT / ".ufo/waves/round-96/V18-scratch"))
import oracle  # noqa: E402

CHAIN = ["r88-m3-maya-cluster", "r94-paired-crossing", "r95-crossing-aftermath", "r96-crossing-response"]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    contract = json.loads((ROOT / "corpus/tools/dependency-freeze-contract.json").read_text())
    ok = True
    for name in CHAIN:
        d = ROOT / "corpus/fixtures" / name
        o = oracle.oracle(d)
        pin = contract["pins"].get(name)
        if pin is None:
            print(f"{name}: NO PIN"); ok = False; continue
        pin_edges = {k: sorted(v["depends_on"]) for k, v in pin["events"].items()}
        pin_endpoints = sorted(tuple(t[:2]) for t in pin["relations"])
        oracle_endpoints = sorted(tuple(t) for t in o["endpoints"])
        edges_match = pin_edges == o["edges"]
        endpoints_match = pin_endpoints == oracle_endpoints
        counts = pin.get("counts", {})
        real_counts = {
            "events": len(o["edges"]),
            "dependency_edges": sum(len(v) for v in o["edges"].values()),
            "relations": len(o["endpoints"]),
            "entities": len(json.loads((d / "entities.json").read_text())),
            "sources": len(json.loads((d / "sources.json").read_text())),
        }
        counts_match = all(counts.get(k) == v for k, v in real_counts.items())
        digests_match = all(
            sha(d / fn) == dig for fn, dig in pin["files"].items() if (d / fn).is_file()
        ) and all((d / fn).is_file() for fn in pin["files"])
        print(f"{name}: edges_match={edges_match} endpoints_match={endpoints_match} "
              f"counts_match={counts_match} per_file_digests_match={digests_match}")
        if not (edges_match and endpoints_match and counts_match and digests_match):
            ok = False
            print(f"  pin_edges={pin_edges}")
            print(f"  oracle   ={o['edges']}")
            print(f"  pin_counts={counts} real_counts={real_counts}")
    # stray pins: any pin whose fixture path is not a corpus/fixtures dir
    for name, pin in contract["pins"].items():
        fx = pin.get("fixture", "")
        if not fx.startswith("corpus/fixtures/"):
            exists = (ROOT / fx).is_dir() if not fx.startswith("/") else Path(fx).is_dir()
            print(f"STRAY PIN {name}: fixture={fx!r} path_exists_now={exists}")
    print("ORACLE-CROSSCHECK", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
