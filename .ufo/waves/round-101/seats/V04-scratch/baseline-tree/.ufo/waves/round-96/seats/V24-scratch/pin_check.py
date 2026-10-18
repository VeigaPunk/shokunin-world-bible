#!/usr/bin/env python3
"""V24 scratch: verify the r94 W05 pin manifest against the working tree."""
import hashlib
import sys
from pathlib import Path

PIN = Path(".ufo/waves/round-94/work/W05-baseline-corpus.sha256")
rows = []
for line in PIN.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    expected, path = line.split("  ", 1)
    rows.append((expected, path))

ok = changed = missing = 0
problems = []
fixture_rows = tool_rows = 0
for expected, path in rows:
    if path.startswith("corpus/fixtures/"):
        fixture_rows += 1
    else:
        tool_rows += 1
    p = Path(path)
    if not p.exists():
        missing += 1
        problems.append(("MISSING", path, expected, None))
        continue
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    if actual == expected:
        ok += 1
    else:
        changed += 1
        problems.append(("CHANGED", path, expected, actual))

print(f"pin_file={PIN}")
print(f"pin_rows={len(rows)} (fixture_rows={fixture_rows} tool_rows={tool_rows})")
print(f"ok={ok} changed={changed} missing={missing}")
for kind, path, expected, actual in problems:
    print(f"{kind} {path}")
    print(f"  pin {expected}")
    print(f"  now {actual if actual else '(absent)'}")
sys.exit(0 if not problems else 1)
