#!/usr/bin/env python3
"""V07: compare each new pin against an independent recomputation of its fixture."""
import json, subprocess, sys

CONTRACT = "corpus/tools/dependency-freeze-contract.json"
contract = json.load(open(CONTRACT))

for name in ("r97-crossing-acknowledgment", "r98-clerk-filing"):
    pin = contract["pins"][name]
    fixture = pin["fixture"]
    out = subprocess.run(["python3", ".ufo/waves/round-98/seats/V07-scratch/recompute_pin.py", fixture],
                         capture_output=True, text=True)
    exp = json.loads(out.stdout)
    print(f"=== {name} ({fixture}) ===")
    for key in ("content_sha256", "files", "events", "relations", "counts"):
        match = pin.get(key) == exp.get(key)
        print(f"  {key}: MATCH={match}")
        if not match:
            print(f"    pin: {json.dumps(pin.get(key), sort_keys=True)}")
            print(f"    exp: {json.dumps(exp.get(key), sort_keys=True)}")
    print(f"  pin revision: {pin.get('revision')}")
    print(f"  fixture path in-scope: {fixture.startswith('corpus/fixtures/')}")
