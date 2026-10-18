import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = Path(__file__).resolve().parent
SOURCE = ROOT / ".ufo/waves/round-94/frozen/map-obligations-r93"
FILES = ("entities.json", "relations.json", "timeline.json", "claim-excerpt-map.md", "expected.json")
TOOL = ROOT / "corpus/tools/map_obligations.py"

with tempfile.TemporaryDirectory(prefix="W02-frozen-demo-", dir=WORK) as temporary:
    snapshot = Path(temporary) / "map-obligations-r93"
    snapshot.mkdir()
    for name in FILES:
        shutil.copyfile(SOURCE / name, snapshot / name)
    command = [sys.executable, "-B", str(TOOL), "--frozen", str(snapshot)]
    baseline = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    baseline_result = [line for line in baseline.stdout.splitlines() if line.startswith("RESULT ")]
    (snapshot / "entities.json").write_bytes((snapshot / "entities.json").read_bytes() + b"\n")
    mutated = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    mutated_findings = [line for line in mutated.stdout.splitlines() if line.startswith("FINDING ")]
    mutated_result = [line for line in mutated.stdout.splitlines() if line.startswith("RESULT ")]
    passed = (
        baseline.returncode == 0 and baseline_result == ["RESULT PASS"] and not baseline.stderr
        and mutated.returncode == 2 and len(mutated_findings) == 1
        and mutated_findings[0].startswith("FINDING snapshot_tampered:")
        and mutated_result == ["RESULT ERROR"] and not mutated.stderr
    )
    print(f"frozen_baseline exit={baseline.returncode} terminal={baseline_result}")
    print(f"mutated_copy exit={mutated.returncode} finding={mutated_findings} terminal={mutated_result}")
    print(f"mutation_to_tamper={'PASS' if passed else 'FAIL'}")
    raise SystemExit(0 if passed else 1)
