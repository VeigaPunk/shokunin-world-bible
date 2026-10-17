#!/usr/bin/env python3
"""V50 pass2: byte-level line diff (pure insertion) for sources/timeline,
HEAD-drift checks for the r96 'before' side, cmp CLI receipts."""
import difflib
import pathlib
import subprocess
import sys

ROOT = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
R96 = ROOT / "corpus/fixtures/r96-crossing-response"
R97 = ROOT / "corpus/fixtures/r97-crossing-acknowledgment"
OUT = ROOT / ".ufo/waves/round-97/seats/V50-scratch"

print("=== A. cmp CLI receipts (r96 working tree vs r97 copies) ===")
for name in ["entities.json", "relations.json", "contradictions.json",
             "inspiration-note.md", "source-excerpt.md"]:
    r = subprocess.run(["cmp", str(R96 / name), str(R97 / name)],
                       capture_output=True, text=True)
    print(f"cmp {name:22s} rc={r.returncode} stdout={r.stdout.strip()!r} stderr={r.stderr.strip()!r}")

print("\n=== B. HEAD-drift on the r96 'before' side (f3e09f9) ===")
for name in ["entities.json", "relations.json", "contradictions.json",
             "inspiration-note.md", "source-excerpt.md", "fictional-excerpts.md",
             "sources.json", "timeline.json", "claim-excerpt-map.md"]:
    rel = f"corpus/fixtures/r96-crossing-response/{name}"
    blob = subprocess.run(["git", "show", f"f3e09f9:{rel}"], cwd=ROOT, capture_output=True)
    live = (R96 / name).read_bytes()
    tag = "MATCH-HEAD" if blob.returncode == 0 and blob.stdout == live else "DIFFERS-FROM-HEAD"
    print(f"r96/{name:22s} {tag}")

print("\n=== C. line-level diff: pure insertion at EOF? ===")
for name in ["sources.json", "timeline.json"]:
    a = (R96 / name).read_text().splitlines(keepends=True)
    b = (R97 / name).read_text().splitlines(keepends=True)
    d = list(difflib.unified_diff(a, b, fromfile=f"r96/{name}", tofile=f"r97/{name}", n=1))
    adds = [l for l in d if l.startswith("+") and not l.startswith("+++")]
    dels = [l for l in d if l.startswith("-") and not l.startswith("---")]
    print(f"--- {name}: added lines={len(adds)} removed lines={len(dels)} (context n=1)")
    sys.stdout.writelines(d if len(d) < 40 else d[:40] + ["...(truncated)\n"])
    # pure-insertion proof: r97 == r96[:k] + inserted + r96[k:]
    print(f"  hunk count={sum(1 for l in d if l.startswith('@@'))}")

print("\n=== D. append-position proof (r97 == r96 with one row inserted before closing bracket) ===")
import json
for name in ["sources.json", "timeline.json"]:
    a = (R96 / name).read_bytes()
    b = (R97 / name).read_bytes()
    # r96 ends with "}\n]\n" ; strip the trailing "]\n"
    assert a.endswith(b"}\n]\n"), a[-8:]
    head96 = a[: -len(b"}\n]\n")] + b"}\n"          # last row of r96 + newline
    prefix_ok = b.startswith(head96)
    tail = b[len(head96):] if prefix_ok else b""
    print(f"{name}: r97 startswith(r96-through-last-row)={prefix_ok}")
    print("  inserted bytes:", repr(tail[:120]))
    print("  r97 trailing bytes:", repr(b[-6:]))

print("\n=== E. appended-row field conformance to round declaration ===")
t97 = json.loads((R97 / "timeline.json").read_text())
ev = t97[-1]
expect = {"id": "acknowledgment-aru-records", "tick": 13, "entity_id": "aru",
          "place_id": "chalk-stair", "depends_on": ["response-evin-salt-court"]}
got = {k: ev.get(k) for k in expect}
print("expected:", expect)
print("got     :", got)
print("conforms:", got == expect, "| source_id:", ev.get("source_id"))
s97 = json.loads((R97 / "sources.json").read_text())
print("appended source id:", s97[-1].get("id"), "| referenced by event source_id:", ev.get("source_id") == s97[-1].get("id"))
