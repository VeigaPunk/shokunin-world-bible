#!/usr/bin/env python3
"""V50 pass3: corrected pure-insertion proof (D-fix) + r96 map repair scope check."""
import pathlib
import subprocess

ROOT = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
R96 = ROOT / "corpus/fixtures/r96-crossing-response"
R97 = ROOT / "corpus/fixtures/r97-crossing-acknowledgment"

print("=== D-fix. pure-insertion proof before the closing bracket ===")
for name in ["sources.json", "timeline.json"]:
    a = (R96 / name).read_bytes()
    b = (R97 / name).read_bytes()
    close = b"  }\n]\n"
    assert a.endswith(close), a[-10:]
    X = a[: -len(close)]
    print(f"{name}: r96 == X + {close!r}; X len={len(X)}")
    print(f"  r97 startswith X: {b.startswith(X)}  | r96 startswith X: {a.startswith(X)}")
    print(f"  inserted bytes ({len(b)-len(X)}): {b[len(X):][:80]!r} ... {b[len(X):][-40:]!r}")
    print(f"  r97 ends with {close!r}: {b.endswith(close)}")

print("\n=== F. r96 map repair scope: which lines changed vs f3e09f9 ===")
rel = "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md"
head = subprocess.run(["git", "show", f"f3e09f9:{rel}"], cwd=ROOT,
                      capture_output=True, text=True).stdout.splitlines()
live = (R96 / "claim-excerpt-map.md").read_text().splitlines()
import difflib
changed = [l for l in difflib.unified_diff(head, live, n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
print(f"changed lines: {len(changed)}")
for l in changed:
    print("  ", l[:160])
print("head lines:", len(head), "live lines:", len(live))
data_rows_head = [l for l in head if l.startswith("| J") or l.startswith("| S")]
data_rows_live = [l for l in live if l.startswith("| J") or l.startswith("| S")]
print("data rows (J*/S*): head", len(data_rows_head), "live", len(data_rows_live),
      "byte-identical:", data_rows_head == data_rows_live)
