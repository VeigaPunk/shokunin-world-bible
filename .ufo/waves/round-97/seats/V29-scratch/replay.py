#!/usr/bin/env python3
"""V29 verdict-depth replay battery: r96 -> r97 preservation + class check."""
import hashlib
import json
import os
import subprocess
import sys

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
os.chdir(ROOT)

R96 = "corpus/fixtures/r96-crossing-response"
R97 = "corpus/fixtures/r97-crossing-acknowledgment"


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()[:8]


def load(p):
    return json.load(open(p))


def report(label, value):
    print(f"{label}: {value}")


print("== tool hashes ==")
for p in ["corpus/tools/map_obligations.py", "corpus/tools/map-obligations-contract.json",
          "corpus/tools/dependency_freeze.py", "corpus/tools/dependency-freeze-contract.json",
          "corpus/fixtures/check_bible.py", "corpus/tools/support_check.py"]:
    print(f"{sha(p)}  {p}")

print("== file hashes r96 / r97 ==")
for f in ["entities.json", "relations.json", "contradictions.json", "timeline.json",
          "sources.json", "inspiration-note.md", "source-excerpt.md",
          "fictional-excerpts.md", "README.md", "claim-excerpt-map.md"]:
    p96, p97 = f"{R96}/{f}", f"{R97}/{f}"
    h96 = sha(p96) if os.path.exists(p96) else "-"
    h97 = sha(p97) if os.path.exists(p97) else "-"
    print(f"{f:24s} r96={h96} r97={h97}")

print("== counts ==")
e97, r97_, t97, s97, c97 = (load(f"{R97}/entities.json"), load(f"{R97}/relations.json"),
                            load(f"{R97}/timeline.json"), load(f"{R97}/sources.json"),
                            load(f"{R97}/contradictions.json"))
e96, r96_, t96, s96, c96 = (load(f"{R96}/entities.json"), load(f"{R96}/relations.json"),
                            load(f"{R96}/timeline.json"), load(f"{R96}/sources.json"),
                            load(f"{R96}/contradictions.json"))
report("r97 counts e/r/ev/s/c", f"{len(e97)}/{len(r97_)}/{len(t97)}/{len(s97)}/{len(c97)}")
report("r96 counts e/r/ev/s/c", f"{len(e96)}/{len(r96_)}/{len(t96)}/{len(s96)}/{len(c96)}")

print("== byte-identity of five copies (r97 vs post-repair r96) ==")
for f in ["entities.json", "relations.json", "contradictions.json",
          "inspiration-note.md", "source-excerpt.md"]:
    b96 = open(f"{R96}/{f}", "rb").read()
    b97 = open(f"{R97}/{f}", "rb").read()
    print(f"{f:24s} byte-identical={b96 == b97}")

print("== parsed prefix ==")
report("r97 timeline[:-1] == r96 timeline", t97[:-1] == t96)
report("r97 sources[:-1] == r96 sources", s97[:-1] == s96)
print("new timeline entry:", json.dumps(t97[-1], ensure_ascii=False))
print("new sources entry:", json.dumps(s97[-1], ensure_ascii=False))
report("r97 contradictions", c97)

print("== excerpts byte-prefix ==")
x96 = open(f"{R96}/fictional-excerpts.md", "rb").read()
x97 = open(f"{R97}/fictional-excerpts.md", "rb").read()
report("r96 excerpts is byte-prefix of r97", x97.startswith(x96))
report("sizes", f"r96={len(x96)}B r97={len(x97)}B delta={len(x97)-len(x96)}B")

print("== census ==")
n = subprocess.run(["bash", "-c", "ls -d corpus/fixtures/*/ | wc -l"],
                   capture_output=True, text=True).stdout.strip()
report("fixture dirs", n)
