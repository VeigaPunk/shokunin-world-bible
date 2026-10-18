#!/usr/bin/env python3
"""Mirror-root dependency_freeze probe. Never writes the live fixture or the live contract."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
LIVE = LANE / "corpus/fixtures/r99-window-lapse"
TOOL = LANE / "corpus/tools/dependency_freeze.py"
CONTRACT = LANE / "corpus/tools/dependency-freeze-contract.json"
SCRATCH = Path(__file__).resolve().parent
MIRROR = SCRATCH / "mirror-r99"
FOREIGN = SCRATCH / "r99-depdropped"
EVENT = "clerk-lapse-recorded"
EDGE = "clerk-filing-open"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv):
    result = subprocess.run([sys.executable, *map(str, argv)], cwd=LANE, capture_output=True, text=True)
    print(f"$ python3 {' '.join(str(a) for a in argv)}")
    print(result.stdout, end="" if result.stdout.endswith("\n") or not result.stdout else "\n")
    if result.stderr.strip():
        print("--- stderr ---")
        print(result.stderr, end="" if result.stderr.endswith("\n") else "\n")
    print(f"EXIT={result.returncode}")
    return result.returncode


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    pin = contract.get("pins", {}).get("r99-window-lapse")
    if not isinstance(pin, dict):
        print("PIN_ABSENT")
        print("pinned:", sorted(contract.get("pins", {})))
        return 3
    lapse = (pin.get("events") or {}).get(EVENT)
    print("PIN fixture", pin.get("fixture"))
    print("PIN payload_schema", pin.get("payload_schema_version"), "contract", contract.get("payload_schema_version"))
    print("PIN files", sorted((pin.get("files") or {})))
    print("PIN counts", pin.get("counts"))
    print("PIN lapse", lapse)
    tool_sha = sha256(TOOL)
    contract_sha = sha256(CONTRACT)
    print("TOOL", tool_sha)
    print("CONTRACT", contract_sha)
    before = {p.name: p.read_bytes() for p in LIVE.iterdir() if p.is_file()}
    print("LIVE timeline", sha256(LIVE / "timeline.json"))

    if MIRROR.exists():
        shutil.rmtree(MIRROR)
    if FOREIGN.exists():
        shutil.rmtree(FOREIGN)
    (MIRROR / "corpus/tools").mkdir(parents=True)
    shutil.copy2(TOOL, MIRROR / "corpus/tools/dependency_freeze.py")
    shutil.copy2(CONTRACT, MIRROR / "corpus/tools/dependency-freeze-contract.json")
    mirrored = MIRROR / "corpus/fixtures/r99-window-lapse"
    shutil.copytree(LIVE, mirrored)
    shutil.copytree(LIVE, FOREIGN)

    # Control: intact mirror must be evaluated by the mirrored tool (path binds inside the mirror root).
    print("=== intact mirror ===")
    run([MIRROR / "corpus/tools/dependency_freeze.py", mirrored])

    # Dropped-edge copy: keep the key, empty the list (BR-01 class).
    timeline_path = mirrored / "timeline.json"
    rows = json.loads(timeline_path.read_text(encoding="utf-8"))
    target = [row for row in rows if row.get("id") == EVENT]
    if len(target) != 1:
        print(f"expected one {EVENT}, found {len(target)}")
        return 2
    print(f"DROP before {EVENT}.depends_on={target[0].get('depends_on')!r}")
    target[0]["depends_on"] = [dep for dep in target[0].get("depends_on", []) if dep != EDGE]
    timeline_path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(f"DROP after {EVENT}.depends_on={target[0].get('depends_on')!r}")
    print("MUTATED timeline", sha256(timeline_path))

    # Same mutation on the foreign copy, for the live-tool PATH-MISMATCH quote.
    foreign_timeline = FOREIGN / "timeline.json"
    foreign_timeline.write_bytes(timeline_path.read_bytes())

    print("=== dropped-edge mirror ===")
    code = run([MIRROR / "corpus/tools/dependency_freeze.py", mirrored])

    print("=== live tool on foreign dropped-edge copy ===")
    run([TOOL, FOREIGN])

    after = {p.name: p.read_bytes() for p in LIVE.iterdir() if p.is_file()}
    print(f"LIVE BYTE-STABLE {before == after}")
    print(f"TOOL UNCHANGED {sha256(TOOL) == tool_sha}")
    print(f"CONTRACT UNCHANGED {sha256(CONTRACT) == contract_sha}")
    return 0 if code == 1 else 1


if __name__ == "__main__":
    sys.exit(main())
