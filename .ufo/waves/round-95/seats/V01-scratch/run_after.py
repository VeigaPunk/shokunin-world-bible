#!/usr/bin/env python3
"""After-phase runner for seat V01: NEW tool on BR-02 mutation + sweep.

Usage: python3 run_after.py   (run from repo root, after P1 delivery)
Writes raw outputs under scratch/after/ and prints a summary table.
"""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = REPO / ".ufo/waves/round-95/seats/V01-scratch"
OUT = SCRATCH / "after"
TOOL = REPO / "corpus/tools/map_obligations.py"

SWEEP = [
    "r87-myth-cluster",
    "r87-chain-unique-valid",
    "r88-m3-maya-cluster",
    "r89-inspiration-paraphrase",
    "r93-m2-kojiki-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
]


def run(args, tag):
    result = subprocess.run(
        [sys.executable, str(TOOL), *args],
        cwd=REPO, capture_output=True, text=True, check=False,
    )
    text = result.stdout + (("--- STDERR ---\n" + result.stderr) if result.stderr else "")
    (OUT / f"{tag}.out").write_text(text, encoding="utf-8")
    findings = sorted(
        line[len("FINDING "):].split(":", 1)[0]
        for line in result.stdout.splitlines() if line.startswith("FINDING ")
    )
    return result.returncode, findings, text


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(TOOL.read_bytes()).hexdigest()
    print(f"NEW tool sha256={digest}")
    print(f"NEW tool size={TOOL.stat().st_size}")
    print()
    print("=== BR-02 mutation through NEW (stability: 3 independent copies) ===")
    for tag, cluster in (
        ("new-br02-run1", "br02-new"),
        ("new-br02-run2", "br02-new"),
        ("new-br02-run3-copy2", "br02-new-2"),
    ):
        code, findings, text = run([str(SCRATCH / cluster)], tag)
        print(f"{tag}: exit={code} findings={findings}")
        print(text.rstrip())
        print("-" * 60)
    print()
    print("=== Sweep of current fixtures through NEW ===")
    rows = []
    for name in SWEEP:
        cluster = REPO / "corpus/fixtures" / name
        if not cluster.is_dir():
            print(f"{name}: MISSING fixture directory")
            rows.append((name, None, None))
            continue
        code, findings, text = run([str(cluster)], f"sweep-{name}")
        schema = "SCHEMA_DRIFT" if "schema_drift" in findings else ""
        first = text.splitlines()[0] if text.splitlines() else ""
        last = text.splitlines()[-1] if text.splitlines() else ""
        print(f"{name}: exit={code} findings={findings or 'none'} {schema}")
        print(f"    first: {first}")
        print(f"    last : {last}")
        rows.append((name, code, findings))
    print()
    print("=== Full map-bearing fixture sweep (schema_drift check) ===")
    drift = []
    for cluster in sorted((REPO / "corpus/fixtures").iterdir()):
        if not cluster.is_dir():
            continue
        if not any((cluster / n).is_file() for n in ("claim-excerpt-map.md", "claim-to-excerpt-map.md")):
            continue
        code, findings, _ = run([str(cluster)], f"all-{cluster.name}")
        if "schema_drift" in findings:
            drift.append(cluster.name)
            print(f"{cluster.name}: exit={code} findings={findings}  <-- SCHEMA_DRIFT")
    print(f"fixtures tripping schema_drift: {drift or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
