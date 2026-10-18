#!/usr/bin/env python3
"""V05 post-R1 runtime checks. Run from repo root: python3 .ufo/.../V05-scratch/post_checks.py"""
import json, pathlib, shutil, subprocess, sys

ROOT = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
S = ROOT / ".ufo/waves/round-97/seats/V05-scratch"
P = S / "post"
shutil.rmtree(P, ignore_errors=True)
(P / "tool").mkdir(parents=True)
shutil.copy(ROOT / "corpus/tools/map_obligations.py", P / "tool/map_obligations.py")
shutil.copy(ROOT / "corpus/tools/map-obligations-contract.json", P / "tool/map-obligations-contract.json")

TOOL = P / "tool/map_obligations.py"

def run(tool, args):
    r = subprocess.run([sys.executable, str(tool), *args], capture_output=True, text=True, cwd=ROOT)
    return r.returncode, r.stdout, r.stderr

print("== [A] full self-test on delivered revision ==")
code, out, err = run(TOOL, ["--self-test"])
(P / "full.txt").write_text(out + ("\nSTDERR:\n" + err if err else ""))
print(f"exit={code}")
print(out.splitlines()[0])
print("PASS count:", sum(1 for l in out.splitlines() if l.startswith("SELF-TEST PASS")))
print("FAIL count:", sum(1 for l in out.splitlines() if l.startswith("SELF-TEST FAIL")))
print([l for l in out.splitlines() if "dual_pointer" in l])
print("last:", out.splitlines()[-1])

print("\n== [B] loader-tightening variants (each: contract copy minus/plus one case) ==")
base_contract = json.loads((P / "tool/map-obligations-contract.json").read_text())
n0 = len(base_contract["self_test"]["cases"])
print(f"delivered contract cases: {n0}")

def variant(name, mutate):
    data = json.loads(json.dumps(base_contract))
    mutate(data)
    d = P / f"var-{name}"
    d.mkdir(exist_ok=True)
    (d / "map-obligations-contract.json").write_text(json.dumps(data, indent=2) + "\n")
    (d / "map_obligations.py").write_bytes(TOOL.read_bytes())
    code, out, err = run(d / "map_obligations.py", ["--self-test"])
    lines = out.splitlines()
    print(f"[{name}] exit={code} first={lines[0] if lines else '<none>'} last={lines[-1] if lines else '<none>'}")
    finding = [l for l in lines if l.startswith("FINDING ")]
    for l in finding[:2]:
        print("   ", l)
    if err.strip():
        print("    STDERR:", err.strip()[:200])

def drop(case_id):
    return lambda d: d["self_test"].update(cases=[c for c in d["self_test"]["cases"] if c["id"] != case_id])

variant("minus-dual-pointer", drop("dual_pointer"))
variant("minus-schema-drift", drop("schema_drift"))
variant("minus-inventory-mismatch", drop("inventory_mismatch"))
variant("minus-complete-core", drop("complete"))
variant("plus-unknown", lambda d: d["self_test"]["cases"].append({"id": "unknown_case", "exit": 2, "finding_ids": ["invalid_arguments"]}))

print("\n== [C] load-bearing: neutralize dual_pointer emission, re-run self-test ==")
src = TOOL.read_text()
needle = '    return None if match is None else match.group(0).strip("`")'
assert needle in src, "neutralization needle not found"
n = P / "neutralized"
n.mkdir(exist_ok=True)
(n / "map-obligations-contract.json").write_text(json.dumps(base_contract, indent=2) + "\n")
(n / "map_obligations.py").write_text(src.replace(needle, "    return None"))
code, out, err = run(n / "map_obligations.py", ["--self-test"])
lines = out.splitlines()
(P / "neutralized.txt").write_text(out)
print(f"exit={code}")
print("dual_pointer case:", [l for l in lines if "dual_pointer" in l])
print("last:", lines[-1] if lines else "<none>")
