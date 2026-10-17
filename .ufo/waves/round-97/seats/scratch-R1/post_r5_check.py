#!/usr/bin/env python3
"""R1 post-R5 check: r97 battery run + inherited-row parsed-value comparison (r96 vs r97)."""
import hashlib
import importlib.util
import pathlib
import subprocess
import sys

REPO = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
TOOL = REPO / "corpus/tools/map_obligations.py"
R96 = REPO / "corpus/fixtures/r96-crossing-response"
R97 = REPO / "corpus/fixtures/r97-crossing-acknowledgment"

spec = importlib.util.spec_from_file_location("map_obligations_r1", TOOL)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

result = subprocess.run(
    [sys.executable, str(TOOL), str(R97)], cwd=str(REPO), capture_output=True, text=True, check=False)
print("=== r97 CLI ===")
print(result.stdout.rstrip())
print(f"EXIT={result.returncode}")
if result.stderr:
    print("STDERR", result.stderr.rstrip())
print()

rows96 = mod.parse_map(R96 / "claim-excerpt-map.md")[0]
rows97 = mod.parse_map(R97 / "claim-excerpt-map.md")[0]
d96 = dict(rows96)
d97 = dict(rows97)
print(f"parsed rows: r96={len(rows96)} r97={len(rows97)}")
inherited = sorted(set(d96) & set(d97))
print(f"inherited pointers: {len(inherited)}; identical source binding: "
      f"{all(d96[p] == d97[p] for p in inherited)}")
new_pointers = sorted(set(d97) - set(d96))
print(f"new pointers in r97: {new_pointers} -> {[d97[p] for p in new_pointers]}")
dropped = sorted(set(d96) - set(d97))
print(f"dropped pointers: {dropped}")
print(f"row order preserved for inherited rows: "
      f"{[p for p, _ in rows97 if p in d96] == [p for p, _ in rows96]}")
obligations, drift = mod.raw_obligations(R97)
print(f"r97 raw obligations={len(obligations)} drift={drift}")
missing = sorted(set(obligations) - set(d97))
print(f"unmapped raw obligations: {missing}")
print(f"map sha256 r97={hashlib.sha256((R97 / 'claim-excerpt-map.md').read_bytes()).hexdigest()}")
print(f"timeline sha256 r97={hashlib.sha256((R97 / 'timeline.json').read_bytes()).hexdigest()}")
