import json, sys
from pathlib import Path
root = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
c = json.loads((root/"corpus/tools/dependency-freeze-contract.json").read_text())
pins = c["pins"]
print("pin count:", len(pins))
ok = True
for name in sorted(pins):
    p = pins[name]
    fx = p.get("fixture")
    named = isinstance(fx, str) and fx == f"corpus/fixtures/{name}"
    print(f"pin {name!r}: fixture={fx!r} path_named={named} revision={p.get('revision')!r} digest={p.get('content_sha256','')[:12]}…")
    ok = ok and named
print("ALL_FOUR_NAME_PATHS" if ok and len(pins)==4 else "PIN_PATH_CHECK_FAILED")
print("expected:", sorted(["r88-m3-maya-cluster","r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response"]))
print("keys match:", sorted(pins)==sorted(["r88-m3-maya-cluster","r94-paired-crossing","r95-crossing-aftermath","r96-crossing-response"]))
