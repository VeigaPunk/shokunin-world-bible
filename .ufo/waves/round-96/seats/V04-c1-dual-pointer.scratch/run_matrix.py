#!/usr/bin/env python3
"""Run a map_obligations revision over the V04 scratch fixture matrix; print exact outputs."""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
tool = Path(sys.argv[1]).resolve()
repeat = int(sys.argv[2]) if len(sys.argv) > 2 else 1
fixtures = Path(sys.argv[3]).resolve() if len(sys.argv) > 3 else (HERE / "fixtures")
label = sys.argv[4] if len(sys.argv) > 4 else "run"
extra = sys.argv[5:] if len(sys.argv) > 5 else []

results = {}
for name in sorted(p.name for p in fixtures.iterdir() if p.is_dir()):
    runs = []
    for run_index in range(repeat):
        command = [sys.executable, str(tool), *extra, str(fixtures / name)]
        result = subprocess.run(command, capture_output=True, text=True)
        runs.append({"exit": result.returncode, "stdout": result.stdout, "stderr": result.stderr})
        print(f"=== {name} run {run_index + 1}: exit={result.returncode}")
        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print("STDERR:", result.stderr.rstrip())
    results[name] = runs

out = HERE / f"matrix-{label}.json"
out.write_text(json.dumps({"tool": str(tool), "repeat": repeat, "results": results}, indent=1) + "\n", encoding="utf-8")
print(f"--- wrote {out}")
