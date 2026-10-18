#!/usr/bin/env python3
"""V14 c3-inherited-equality full battery (r97 vs POST-REPAIR r96)."""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
R96 = ROOT / "corpus/fixtures/r96-crossing-response"
R97 = Path(os.environ.get("V14_R97", str(ROOT / "corpus/fixtures/r97-crossing-acknowledgment")))
BASE = "f3e09f9"
fail = []


def os_(o):
    return json.dumps(o, sort_keys=False, ensure_ascii=False, separators=(",", ":"))


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def run(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, shell=isinstance(cmd, str))


print("## 0. r97 file inventory")
expected = ["entities.json", "relations.json", "contradictions.json", "timeline.json",
            "sources.json", "fictional-excerpts.md", "inspiration-note.md",
            "source-excerpt.md", "README.md", "claim-excerpt-map.md"]
for f in expected:
    ok = (R97 / f).is_file()
    print(f"  {f}: {'present' if ok else 'MISSING'}")
    if not ok:
        fail.append(f"missing {f}")
if not all((R97 / f).is_file() for f in expected):
    print("ABORT: r97 inventory incomplete")
    sys.exit(2)

print("\n## 1. r97 row counts and JSON validity")
for f, exp in [("entities.json", 5), ("relations.json", 1), ("contradictions.json", 0),
               ("timeline.json", 6), ("sources.json", 6)]:
    d = load(R97 / f)
    status = "OK" if len(d) == exp else f"UNEXPECTED (expected {exp})"
    print(f"  {f}: rows={len(d)} {status}")
    if len(d) != exp:
        fail.append(f"{f} rows={len(d)} != {exp}")

print("\n## 2. parsed-value equality, KEY-ORDER SENSITIVE (inherited rows)")
for f, n in [("entities.json", 5), ("relations.json", 1), ("contradictions.json", None),
             ("timeline.json", 5), ("sources.json", 5)]:
    a, b = load(R96 / f), load(R97 / f)
    nrows = len(a) if n is None else n
    ok = True
    for i in range(nrows):
        same = os_(a[i]) == os_(b[i])
        kord = (list(a[i].keys()) if isinstance(a[i], dict) else None) == \
               (list(b[i].keys()) if isinstance(b[i], dict) else None)
        if not (same and kord):
            ok = False
            print(f"  {f}[{i}] MISMATCH same={same} key-order={kord}")
            print(f"    r96: {os_(a[i])}")
            print(f"    r97: {os_(b[i])}")
    print(f"  {f}[:{nrows}] (r96 rows={len(a)}, r97 rows={len(b)}): "
          f"{'IDENTICAL (order-sensitive)' if ok else 'MISMATCH'}")
    if not ok:
        fail.append(f"{f} inherited mismatch")

print("\n## 3. byte-copy claims (cmp) for copied files")
for f in ["entities.json", "relations.json", "contradictions.json",
          "inspiration-note.md", "source-excerpt.md"]:
    ba, bb = (R96 / f).read_bytes(), (R97 / f).read_bytes()
    same = ba == bb
    print(f"  {f}: r96={len(ba)}B r97={len(bb)}B identical={same}")
    if not same:
        fail.append(f"{f} not byte-identical")

print("\n## 4. byte-prefix probe for extended tables")
for f in ["timeline.json", "sources.json"]:
    ba, bb = (R96 / f).read_bytes(), (R97 / f).read_bytes()
    core = ba.rstrip()[:-1].rstrip()  # drop final ']' and whitespace
    pref = bb.startswith(core)
    # where do they diverge?
    div = next((i for i, (x, y) in enumerate(zip(core, bb)) if x != y), min(len(core), len(bb)))
    print(f"  {f}: r96-core={len(core)}B r97-startswith-core={pref} first-divergence-at={div}")
    if not pref:
        fail.append(f"{f} not byte-prefix of r96 core")

print("\n## 5. new rows (r97 beyond r96 length) — observation")
for f in ["timeline.json", "sources.json"]:
    a, b = load(R96 / f), load(R97 / f)
    for i in range(len(a), len(b)):
        print(f"  {f}[{i}]: {os_(b[i])}")
    # schema parity of new row vs inherited row
    if len(b) > len(a):
        ka = set(a[0].keys())
        for i in range(len(a), len(b)):
            kb = set(b[i].keys())
            print(f"  {f}[{i}] key-set == inherited[0] key-set: {ka == kb} "
                  f"(diff {sorted(kb ^ ka)})")
            if ka != kb:
                fail.append(f"{f} new-row schema mismatch")

print("\n## 6. r96 JSON tables byte-unchanged vs f3e09f9")
r = run(f"git diff --stat {BASE} -- " + " ".join(
    f"corpus/fixtures/r96-crossing-response/{f}"
    for f in ["entities.json", "relations.json", "contradictions.json",
              "timeline.json", "sources.json"]))
print(f"  git diff --stat output: {r.stdout.strip()!r} (empty = unchanged), rc={r.returncode}")
if r.stdout.strip():
    fail.append("r96 JSON tables differ from baseline")
for f in ["entities.json", "relations.json", "contradictions.json", "timeline.json", "sources.json"]:
    wt = run(["git", "hash-object", f"corpus/fixtures/r96-crossing-response/{f}"]).stdout.strip()
    base = run(["git", "rev-parse", f"{BASE}:corpus/fixtures/r96-crossing-response/{f}"]).stdout.strip()
    if wt != base:
        fail.append(f"blob diff {f}")

print("\n## 7. supplementary: r96 map repair scope (out of primary mandate)")
r = run(f"git diff --numstat {BASE} -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md")
print(f"  numstat: {r.stdout.strip()!r}")
r = run(f"git diff -U0 {BASE} -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md")
for line in r.stdout.splitlines():
    if line.startswith(("@@", "-|", "+|", "-The new", "+The new")):
        print(f"  {line}")

print("\n## 8. whole-repo change surface vs f3e09f9")
r = run(f"git diff --stat {BASE}")
print(f"  git diff --stat {BASE}:\n{r.stdout}")
r = run("git status --porcelain")
print(f"  git status --porcelain:\n{r.stdout}")

print(f"\nFAILURES: {len(fail)}")
for f in fail:
    print(f"  - {f}")
sys.exit(1 if fail else 0)
