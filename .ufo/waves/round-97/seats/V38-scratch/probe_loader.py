"""V38 isolated probes of the map_obligations self-test contract loader.

Copies the delivered tool to scratch with ROOT pinned to the repo root and a
modified contract beside it, so no repo byte is written. Usage:
    python3 probe_loader.py <probe-root> drop <case-id>
    python3 probe_loader.py <probe-root> neutralize
"""
import json
import pathlib
import shutil
import subprocess
import sys

R = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
probe_root = pathlib.Path(sys.argv[1])
mode = sys.argv[2]


def make_tool(target, mutate=None):
    src = (R / "corpus/tools/map_obligations.py").read_text()
    src = src.replace(
        "ROOT = Path(__file__).resolve().parents[2]", f"ROOT = Path({str(R)!r})"
    )
    if mutate:
        before = src
        src = mutate(src)
        assert src != before, "mutation did not apply"
    (target / "tools").mkdir(parents=True, exist_ok=True)
    (target / "tools/map_obligations.py").write_text(src)


def write_contract(target, drop=None):
    contract = json.loads(
        (R / "corpus/tools/map-obligations-contract.json").read_text()
    )
    if drop:
        contract["self_test"]["cases"] = [
            item for item in contract["self_test"]["cases"] if item["id"] != drop
        ]
    (target / "tools/map-obligations-contract.json").write_text(
        json.dumps(contract, indent=2) + "\n"
    )


def run(target):
    result = subprocess.run(
        [sys.executable, str(target / "tools/map_obligations.py"), "--self-test"],
        cwd=R,
        capture_output=True,
        text=True,
    )
    lines = result.stdout.splitlines()
    print("exit:", result.returncode)
    print("first:", lines[0] if lines else "(none)")
    for line in lines:
        if "FAIL" in line or line.startswith("FINDING") or line.startswith("RESULT"):
            print("  |", line)
    if result.stderr:
        print("stderr:", result.stderr[:400])


if mode == "drop":
    case_id = sys.argv[3]
    target = probe_root / f"probe_drop_{case_id}"
    shutil.rmtree(target, ignore_errors=True)
    make_tool(target)
    write_contract(target, drop=case_id)
    print(f"=== loader probe: contract with {case_id!r} dropped ===")
    run(target)
elif mode == "neutralize":
    target = probe_root / "probe_neutralized"
    shutil.rmtree(target, ignore_errors=True)
    make_tool(target, lambda s: s.replace(
        "if mention is not None:", "if mention is not None and False:"
    ))
    write_contract(target)
    print("=== load-bearing probe: dual_pointer emission neutralized ===")
    run(target)
else:
    raise SystemExit(f"unknown mode {mode}")
