import json, sys, os, subprocess, hashlib
CT = "corpus/tools/dependency-freeze-contract.json"
ref = json.load(open(".ufo/waves/round-96/seats/V23-scratch/ref_inventory.json"))
c = json.load(open(CT))
print("== contract top-level keys ==", sorted(c.keys()))
# find the fixture-bearing structure
def find_fixture_maps(o, path="root"):
    hits = []
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(k, str) and k.startswith("r") and os.path.isdir(os.path.join("corpus/fixtures", k)):
                hits.append((path + "/" + k, k))
            hits += find_fixture_maps(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            hits += find_fixture_maps(v, f"{path}[{i}]")
    return hits
hits = find_fixture_maps(c)
print("== fixture-key locations ==")
for p, k in hits:
    print("  ", p)
print("== distinct fixture keys ==", sorted({k for _, k in hits}))
