#!/usr/bin/env python3
"""Q1 poll: wait for Q2's 24-case contract, then run the tool self-test against it."""

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
CONTRACT = ROOT / "corpus/tools/map-obligations-contract.json"
TOOL = ROOT / "corpus/tools/map_obligations.py"


def case_ids():
    try:
        contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        cases = contract["self_test"]["cases"]
        return [item["id"] for item in cases]
    except Exception as error:  # noqa: BLE001 - poll loop reports the raw error
        return [f"UNREADABLE {error}"]


for attempt in range(1, 41):
    ids = case_ids()
    stamp = time.strftime("%H:%M:%S")
    print(f"[{stamp}] try {attempt}: {len(ids)} cases", flush=True)
    if len(ids) >= 24:
        print(f"[{stamp}] contract ids: {ids}", flush=True)
        result = subprocess.run(
            [sys.executable, str(TOOL), "--self-test"], cwd=ROOT, capture_output=True, text=True, check=False
        )
        print(result.stdout, flush=True)
        print(f"self-test exit={result.returncode}", flush=True)
        print(f"mtime={time.strftime('%H:%M:%S', time.localtime(CONTRACT.stat().st_mtime))}", flush=True)
        break
    time.sleep(20)
else:
    ids = case_ids()
    print(f"TIMEOUT after 40 tries; contract still {len(ids)} cases: {ids}", flush=True)
    print(f"mtime={time.strftime('%H:%M:%S', time.localtime(CONTRACT.stat().st_mtime))}", flush=True)
