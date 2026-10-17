import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WORK = Path(__file__).resolve().parent
SOURCE = ROOT / "corpus/fixtures/r93-m2-kojiki-cluster"
FILES = (
    "entities.json",
    "relations.json",
    "timeline.json",
    "claim-excerpt-map.md",
    "archive-record-excerpt.md",
    "kojiki-chamberlain-excerpt.md",
)

with tempfile.TemporaryDirectory(prefix="W02-unmapped-demo-", dir=WORK) as temporary:
    cluster = Path(temporary) / "cluster"
    cluster.mkdir()
    for name in FILES:
        shutil.copyfile(SOURCE / name, cluster / name)
    entities_path = cluster / "entities.json"
    entities = json.loads(entities_path.read_text(encoding="utf-8"))
    entities[0]["claims"].append({
        "statement": "isolated unmapped raw claim",
        "source_id": "m2-record-archive",
    })
    entities_path.write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")
    support = subprocess.run(
        [sys.executable, "-B", str(ROOT / "corpus/tools/support_check.py"), str(cluster)],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    mapping = subprocess.run(
        [sys.executable, "-B", str(ROOT / "corpus/tools/map_obligations.py"), str(cluster)],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    support_terminal = [line for line in support.stdout.splitlines() if line.startswith("RESULT ")]
    mapping_terminal = [line for line in mapping.stdout.splitlines() if line.startswith("RESULT ")]
    findings = [line for line in mapping.stdout.splitlines() if line.startswith("FINDING ")]
    expected_finding = "FINDING missing_obligation: entities.json#/0/claims/1 has no map row"
    passed = (
        support.returncode == 0 and support_terminal == ["RESULT PASS"] and not support.stderr
        and mapping.returncode == 1 and mapping_terminal == ["RESULT FAIL"]
        and findings == [expected_finding] and not mapping.stderr
    )
    print(f"support_check exit={support.returncode} terminal={support_terminal}")
    print(f"map_obligations exit={mapping.returncode} findings={findings} terminal={mapping_terminal}")
    print(f"counterexample={'PASS' if passed else 'FAIL'}")
    raise SystemExit(0 if passed else 1)
