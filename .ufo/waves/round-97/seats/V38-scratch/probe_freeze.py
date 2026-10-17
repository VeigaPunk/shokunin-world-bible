"""V38 isolated probes of dependency_freeze guards.

All contract writes go to scratch copies; the repo contract is never mutated.
Usage: python3 probe_freeze.py <scratch-root>
"""
import hashlib
import importlib.util
import json
import pathlib
import shutil
import subprocess
import sys

R = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
S = pathlib.Path(sys.argv[1])
TOOL = R / "corpus/tools/dependency_freeze.py"
CONTRACT = R / "corpus/tools/dependency-freeze-contract.json"
FIXTURE = "r96-crossing-response"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_tool(contract_path=None):
    spec = importlib.util.spec_from_file_location("df_probe", TOOL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if contract_path is not None:
        mod.CONTRACT_PATH = contract_path
    return mod


print("=== A. foreign-path same-named copy, real CLI + real contract ===")
foreign = S / "foreign" / FIXTURE
result = subprocess.run(
    [sys.executable, str(TOOL), str(foreign)], cwd=R, capture_output=True, text=True
)
print("exit:", result.returncode)
print(result.stdout.strip() or "(no stdout)")
print(result.stderr.strip()[:300] or "(no stderr)")

print()
print("=== B. --freeze on a foreign path, real CLI, contract digest watched ===")
before = sha(CONTRACT)
result = subprocess.run(
    [sys.executable, str(TOOL), "--freeze", str(foreign)],
    cwd=R, capture_output=True, text=True,
)
after = sha(CONTRACT)
print("exit:", result.returncode)
print(result.stdout.strip() or "(no stdout)")
print("contract sha before:", before[:16])
print("contract sha after :", after[:16])
print("contract unchanged:", before == after)

print()
print("=== C. DIGEST-MISMATCH file naming, scratch contract (path bound to scratch) ===")
probe = S / "probe_digest"
shutil.rmtree(probe, ignore_errors=True)
shutil.copytree(R / "corpus/fixtures" / FIXTURE, probe / FIXTURE)
entities = probe / FIXTURE / "entities.json"
records = json.loads(entities.read_text())
records[0]["name"] = records[0].get("name", "") + " (byte probe)"
entities.write_text(json.dumps(records, indent=2) + "\n")
scratch_contract = probe / "contract.json"
contract = json.loads(CONTRACT.read_text())
pin = contract["pins"][FIXTURE]
if "path" in pin:
    pin["path"] = str(probe / FIXTURE).replace(str(R) + "/", "")
scratch_contract.write_text(json.dumps(contract, indent=2) + "\n")
mod = load_tool(scratch_contract)
try:
    rc = mod.verify(probe / FIXTURE, mod.read_contract())
    print("verify rc:", rc)
except SystemExit as error:
    print("verify SystemExit:", error)

print()
print("=== D. --freeze on a corpus/fixtures path, scratch contract (guard end-to-end) ===")
contract2 = probe / "contract2.json"
contract2.write_text(CONTRACT.read_text())
mod2 = load_tool(contract2)
try:
    rc = mod2.freeze(R / "corpus/fixtures" / FIXTURE, mod2.read_contract())
    print("freeze rc:", rc)
except SystemExit as error:
    print("freeze SystemExit:", error)
