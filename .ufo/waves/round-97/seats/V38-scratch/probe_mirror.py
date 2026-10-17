"""V38 mirror-root probes of the delivered dependency_freeze guards.

The delivered tool binds paths to its own ROOT, so the digest-naming and
in-scope-freeze cases are exercised in a byte-identical mirror root under the
V38 scratch tree. The delivered tool sha is asserted against the mirror copy.
"""
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys

R = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
S = pathlib.Path(sys.argv[1]).resolve()
M = S / "mirror"
FIXTURE = "r96-crossing-response"

shutil.rmtree(M, ignore_errors=True)
(M / "corpus/tools").mkdir(parents=True)
(M / "corpus/fixtures").mkdir(parents=True)
shutil.copy2(R / "corpus/tools/dependency_freeze.py", M / "corpus/tools/dependency_freeze.py")
shutil.copy2(R / "corpus/tools/dependency-freeze-contract.json", M / "corpus/tools/dependency-freeze-contract.json")
shutil.copytree(R / "corpus/fixtures" / FIXTURE, M / "corpus/fixtures" / FIXTURE)

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
print("mirror tool sha == delivered tool sha:", sha(M / "corpus/tools/dependency_freeze.py") == sha(R / "corpus/tools/dependency_freeze.py"))
print("mirror tool sha:", sha(M / "corpus/tools/dependency_freeze.py")[:16])
TOOL = M / "corpus/tools/dependency_freeze.py"


def run(args):
    result = subprocess.run([sys.executable, str(TOOL), *args], cwd=M, capture_output=True, text=True)
    print("  exit:", result.returncode)
    for line in result.stdout.splitlines():
        print("  |", line)
    if result.stderr.strip():
        print("  stderr:", result.stderr.strip()[:200])
    return result


print()
print("=== C2c: byte change invisible to the inventory (description only) ===")
timeline = M / "corpus/fixtures" / FIXTURE / "timeline.json"
records = json.loads(timeline.read_text())
records[-1]["description"] = records[-1]["description"] + " (probe drift)"
timeline.write_text(json.dumps(records, indent=2) + "\n")
run([str(M / "corpus/fixtures" / FIXTURE)])

print()
print("=== C2b: byte-identical same-named copy at a foreign path (mirror) ===")
foreign = M / ".ufo/foreign" / FIXTURE
shutil.copytree(M / "corpus/fixtures" / FIXTURE, foreign)
run([str(foreign)])

print()
print("=== C2a: --freeze on the foreign path (mirror contract digest watched) ===")
before = sha(M / "corpus/tools/dependency-freeze-contract.json")
run(["--freeze", str(foreign)])
after = sha(M / "corpus/tools/dependency-freeze-contract.json")
print("  mirror contract unchanged:", before == after)

print()
print("=== C2a control: --freeze on the canonical in-scope path (mirror) ===")
run(["--freeze", str(M / "corpus/fixtures" / FIXTURE)])

print()
print("=== C2a: --freeze on the scope root itself (mirror) ===")
run(["--freeze", str(M / "corpus/fixtures")])
