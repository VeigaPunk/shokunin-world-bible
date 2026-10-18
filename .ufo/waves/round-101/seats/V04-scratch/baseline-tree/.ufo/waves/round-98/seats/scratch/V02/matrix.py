#!/usr/bin/env python3
"""V02 matrix runner (absolute paths only). Rebuilds cases from LIVE repo bytes,
runs --freeze per case, records exit/output, hashes, and preservation checks."""
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys

REPO = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
V02 = REPO / ".ufo/waves/round-98/seats/scratch/V02"
CASES = V02 / "cases"
FIXTURE = "r95-crossing-aftermath"
PIN = "r95-crossing-aftermath"

VARIANTS = {
    "legacy_missing_key": lambda pin: pin.pop("fixture", None),
    "legacy_null": lambda pin: pin.__setitem__("fixture", None),
    "legacy_nonstring": lambda pin: pin.__setitem__("fixture", 123),
    "legacy_empty_string": lambda pin: pin.__setitem__("fixture", ""),
    "legacy_other_path": lambda pin: pin.__setitem__("fixture", "corpus/fixtures/r96-crossing-response"),
    "legacy_out_of_scope_path": lambda pin: pin.__setitem__("fixture", "corpus/knowledge"),
    "garbage_traversal": lambda pin: pin.__setitem__("fixture", "../../outside"),
}


def build(variant):
    root = (CASES / variant).resolve()
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    (root / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(REPO / "corpus/tools/dependency_freeze.py", root / "corpus/tools/dependency_freeze.py")
    shutil.copytree(REPO / "corpus/fixtures" / FIXTURE, root / "corpus/fixtures" / FIXTURE)
    contract = json.loads((REPO / "corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8"))
    VARIANTS[variant](contract["pins"][PIN])
    (root / "corpus/tools/dependency-freeze-contract.json").write_text(
        json.dumps(contract, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return root


def main():
    tool_sha = hashlib.sha256((REPO / "corpus/tools/dependency_freeze.py").read_bytes()).hexdigest()
    contract_sha = hashlib.sha256((REPO / "corpus/tools/dependency-freeze-contract.json").read_bytes()).hexdigest()
    print(f"VERIFIED-AGAINST tool_sha256={tool_sha}")
    print(f"VERIFIED-AGAINST contract_sha256={contract_sha}")
    for variant in VARIANTS:
        root = build(variant)
        tool = root / "corpus/tools/dependency_freeze.py"
        fixture = root / "corpus/fixtures" / FIXTURE
        cp = root / "corpus/tools/dependency-freeze-contract.json"
        c0 = json.loads(cp.read_text())
        pin_before = c0["pins"][PIN]
        h0 = hashlib.sha256(cp.read_bytes()).hexdigest()
        proc = subprocess.run([sys.executable, str(tool), "--freeze", str(fixture)],
                              cwd=root, capture_output=True, text=True)
        h1 = hashlib.sha256(cp.read_bytes()).hexdigest()
        c1 = json.loads(cp.read_text())
        pin_after = c1["pins"][PIN]
        print(f"\n=== {variant} ===")
        print(f"cmd: python3 {tool} --freeze {fixture}  (cwd={root})")
        print(f"pin before: fixture_key={'fixture' in pin_before} value={pin_before.get('fixture')!r} keys={sorted(pin_before)}")
        for line in (proc.stdout + proc.stderr).splitlines():
            print("  " + line)
        print(f"exit={proc.returncode} contract_hash {h0[:16]}… -> {h1[:16]}… unchanged={h0 == h1}")
        print(f"pin after: fixture_key={'fixture' in pin_after} value={pin_after.get('fixture')!r}")
        if variant == "legacy_missing_key":
            others_before = {k: v for k, v in c0["pins"].items() if k != PIN}
            others_after = {k: v for k, v in c1["pins"].items() if k != PIN}
            print("top-level keys same:", sorted(c0) == sorted(c1))
            print("other pins identical:", others_before == others_after)
            print("self_test block identical:", c0.get("self_test") == c1.get("self_test"))
            print("target pin content fields identical:", all(pin_after.get(k) == pin_before.get(k)
                  for k in ("content_sha256", "files", "events", "relations", "counts")))


if __name__ == "__main__":
    main()
