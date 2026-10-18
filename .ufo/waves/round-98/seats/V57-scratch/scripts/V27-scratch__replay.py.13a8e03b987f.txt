#!/usr/bin/env python3
"""V27 (round 98) replay battery 1: r97 -> r98 preservation + institutional-no-finding class."""
import hashlib
import json
import os
import subprocess
import sys

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
os.chdir(ROOT)

R97 = "corpus/fixtures/r97-crossing-acknowledgment"
R98 = "corpus/fixtures/r98-clerk-filing"


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()[:8]


def load(p):
    return json.load(open(p))


print("== tool hashes ==")
for p in ["corpus/fixtures/check_bible.py", "corpus/tools/support_check.py",
          "corpus/tools/map_obligations.py", "corpus/tools/map-obligations-contract.json"]:
    print(f"{sha(p)}  {p}")

print("== file hashes r97 / r98 ==")
for f in ["entities.json", "relations.json", "contradictions.json", "timeline.json",
          "sources.json", "inspiration-note.md", "source-excerpt.md",
          "fictional-excerpts.md", "README.md", "claim-excerpt-map.md"]:
    p97, p98 = f"{R97}/{f}", f"{R98}/{f}"
    h97 = sha(p97) if os.path.exists(p97) else "-"
    h98 = sha(p98) if os.path.exists(p98) else "-"
    print(f"{f:24s} r97={h97} r98={h98}")

print("== counts ==")
e98, r98_, t98, s98, c98 = (load(f"{R98}/entities.json"), load(f"{R98}/relations.json"),
                            load(f"{R98}/timeline.json"), load(f"{R98}/sources.json"),
                            load(f"{R98}/contradictions.json"))
e97, r97_, t97, s97, c97 = (load(f"{R97}/entities.json"), load(f"{R97}/relations.json"),
                            load(f"{R97}/timeline.json"), load(f"{R97}/sources.json"),
                            load(f"{R97}/contradictions.json"))
print(f"r98 counts e/r/ev/s/c: {len(e98)}/{len(r98_)}/{len(t98)}/{len(s98)}/{len(c98)}")
print(f"r97 counts e/r/ev/s/c: {len(e97)}/{len(r97_)}/{len(t97)}/{len(s97)}/{len(c97)}")

print("== byte-identity of inherited copies (r98 vs r97) ==")
for f in ["entities.json", "relations.json", "contradictions.json",
          "inspiration-note.md", "source-excerpt.md"]:
    b97 = open(f"{R97}/{f}", "rb").read()
    b98 = open(f"{R98}/{f}", "rb").read()
    print(f"{f:24s} byte-identical={b97 == b98}")

print("== parsed prefix ==")
print("r98 timeline[:-1] == r97 timeline:", t98[:-1] == t97)
print("r98 sources[:-1] == r97 sources:", s98[:-1] == s97)
print("r98 entities[:-1] == r97 entities:", e98[:-1] == e97)
print("r98 relations == r97 relations:", r98_ == r97_)
print("new entities entry:", json.dumps(e98[-1], ensure_ascii=False))
print("new timeline entry:", json.dumps(t98[-1], ensure_ascii=False))
print("new sources entry:", json.dumps(s98[-1], ensure_ascii=False))
print("r98 contradictions:", c98)

print("== excerpts byte-prefix ==")
x97 = open(f"{R97}/fictional-excerpts.md", "rb").read()
x98 = open(f"{R98}/fictional-excerpts.md", "rb").read()
print("r97 excerpts is byte-prefix of r98:", x98.startswith(x97))
print(f"sizes: r97={len(x97)}B r98={len(x98)}B delta={len(x98)-len(x97)}B")

print("== census ==")
n = subprocess.run(["bash", "-c", "ls -d corpus/fixtures/*/ | wc -l"],
                   capture_output=True, text=True).stdout.strip()
print("fixture dirs:", n)
