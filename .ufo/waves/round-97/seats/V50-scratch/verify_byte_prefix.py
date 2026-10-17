#!/usr/bin/env python3
"""V50 byte-prefix-2: r96-post-repair vs r97-copy byte identity, JSON append-only
diffs for sources/timeline, and strict byte-prefix for fictional-excerpts."""
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
R96 = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "corpus/fixtures/r96-crossing-response"
R97 = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "corpus/fixtures/r97-crossing-acknowledgment"

fail = []


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def head(t):
    print(f"\n=== {t} ===")


# 1. byte copies: cmp r96-post-repair vs r97 copied files
head("1. byte-copy identity (r96 working tree vs r97 copies)")
COPIES = [
    "entities.json",
    "relations.json",
    "contradictions.json",
    "inspiration-note.md",
    "source-excerpt.md",
]
for name in COPIES:
    a, b = R96 / name, R97 / name
    if not a.exists() or not b.exists():
        print(f"MISSING {name}: r96={a.exists()} r97={b.exists()}")
        fail.append(f"missing:{name}")
        continue
    ha, hb = sha(a), sha(b)
    r = subprocess.run(["cmp", "-s", str(a), str(b)])
    status = "IDENTICAL" if r.returncode == 0 else f"DIFFER(rc={r.returncode})"
    print(f"{name:24s} {status:16s} r96={ha[:16]} r97={hb[:16]} size {a.stat().st_size}/{b.stat().st_size}")
    if r.returncode != 0:
        out = subprocess.run(["cmp", str(a), str(b)], capture_output=True, text=True)
        print("  cmp:", out.stdout.strip(), out.stderr.strip())
        fail.append(f"copy-differs:{name}")

# 1b. r96 working-tree copies equal committed f3e09f9 blobs (repair must not touch them)
head("1b. r96 working-tree copies vs committed f3e09f9")
for name in COPIES:
    rel = f"corpus/fixtures/r96-crossing-response/{name}"
    blob = subprocess.run(
        ["git", "show", f"f3e09f9:{rel}"], cwd=ROOT, capture_output=True
    )
    live = (R96 / name).read_bytes()
    same = blob.returncode == 0 and blob.stdout == live
    print(f"{name:24s} {'MATCH-HEAD' if same else 'DIFFERS-FROM-HEAD'}")
    if not same:
        fail.append(f"head-drift:{name}")

# 2/3. JSON append-only diffs
head("2. sources.json append-only diff")
s96 = json.loads((R96 / "sources.json").read_text())
s97 = json.loads((R97 / "sources.json").read_text())
print(f"rows: r96={len(s96)} r97={len(s97)} delta={len(s97)-len(s96)}")
inherited_ok = s97[: len(s96)] == s96
print(f"inherited prefix deep-equal (order + values): {inherited_ok}")
appended_src = s97[len(s96):]
print("appended source row(s):", json.dumps(appended_src, ensure_ascii=False))
if not inherited_ok:
    for i, (a, b) in enumerate(zip(s96, s97)):
        if a != b:
            print(f"  first divergence at index {i}:\n   r96={json.dumps(a)}\n   r97={json.dumps(b)}")
            break
    fail.append("sources-inherited-changed")
if len(s97) != len(s96) + 1:
    fail.append("sources-delta-not-1")

head("3. timeline.json append-only diff")
t96 = json.loads((R96 / "timeline.json").read_text())
t97 = json.loads((R97 / "timeline.json").read_text())
print(f"rows: r96={len(t96)} r97={len(t97)} delta={len(t97)-len(t96)}")
t_ok = t97[: len(t96)] == t96
print(f"inherited prefix deep-equal (order + values): {t_ok}")
appended_ev = t97[len(t96):]
print("appended event row(s):", json.dumps(appended_ev, ensure_ascii=False))
if not t_ok:
    for i, (a, b) in enumerate(zip(t96, t97)):
        if a != b:
            print(f"  first divergence at index {i}:\n   r96={json.dumps(a)}\n   r97={json.dumps(b)}")
            break
    fail.append("timeline-inherited-changed")
if len(t97) != len(t96) + 1:
    fail.append("timeline-delta-not-1")

# 4. fictional-excerpts strict byte prefix
head("4. fictional-excerpts.md strict byte-prefix")
f96 = (R96 / "fictional-excerpts.md").read_bytes()
f97 = (R97 / "fictional-excerpts.md").read_bytes()
is_prefix = f97.startswith(f96)
strict = is_prefix and len(f97) > len(f96)
print(f"r96 bytes={len(f96)} r97 bytes={len(f97)} prefix={is_prefix} strict={strict}")
print(f"r96 sha={sha(R96/'fictional-excerpts.md')[:16]} r97 sha={sha(R97/'fictional-excerpts.md')[:16]}")
if not is_prefix:
    n = min(len(f96), len(f97))
    i = next((k for k in range(n) if f96[k] != f97[k]), n)
    print(f"first differing byte offset {i}: r96={f96[i:i+60]!r} r97={f97[i:i+60]!r}")
    fail.append("excerpts-not-prefix")
elif not strict:
    fail.append("excerpts-not-strict-no-appended-tail")
tail = f97[len(f96):] if is_prefix else b""
print("appended tail bytes:", len(tail))
print("---- appended tail ----")
sys.stdout.write(tail.decode("utf-8", "replace"))
print("---- end tail ----")

head("VERDICT")
print("FAILURES:", fail if fail else "none")
