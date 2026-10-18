#!/usr/bin/env python3
"""V12 scratch harness: run the FINAL dependency_freeze tool against a SCRATCH
copy of the contract, re-freezing every pin, and diff the resulting pin entries
against the delivered contract. Never touches producer-owned files.

Usage: python3 refreeze_harness.py <tool.py> <contract.json> <outdir>
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")


def main():
    tool_src, contract_src, outdir = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    outdir.mkdir(parents=True, exist_ok=True)
    scratch_contract = outdir / "contract-scratch.json"
    scratch_tool = outdir / "dependency_freeze_scratch.py"
    shutil.copy(contract_src, scratch_contract)
    text = tool_src.read_text()
    patched, n = re.subn(
        r'CONTRACT_PATH\s*=\s*ROOT\s*/\s*"[^"]+"',
        f'CONTRACT_PATH = Path({str(scratch_contract)!r})',
        text,
    )
    patched, n2 = re.subn(
        r'ROOT\s*=\s*Path\(__file__\)\.resolve\(\)\.parents\[2\]',
        f'ROOT = Path({str(ROOT)!r})',
        patched,
    )
    print(f"patched CONTRACT_PATH occurrences: {n}; ROOT occurrences: {n2}")
    scratch_tool.write_text(patched)

    delivered = json.load(open(contract_src))
    results = {}
    for name, pin in delivered["pins"].items():
        fixture = pin["fixture"]
        proc = subprocess.run(
            [sys.executable, str(scratch_tool), "--freeze", fixture],
            cwd=ROOT, capture_output=True, text=True,
        )
        results[name] = proc
        print(f"--- freeze {name} rc={proc.returncode}")
        print(proc.stdout.strip())
        if proc.stderr.strip():
            print("STDERR:", proc.stderr.strip())

    scratch = json.load(open(scratch_contract))
    print("=== pin-by-pin comparison: scratch refreeze vs delivered ===")
    for name in delivered["pins"]:
        a = delivered["pins"][name]
        b = scratch["pins"].get(name)
        same = a == b
        print(f"{name}: identical={same}")
        if not same:
            ka, kb = set(a), set(b or {})
            print(f"  key sets equal: {ka == kb}; only-in-delivered={ka - kb}; only-in-scratch={kb - ka}")
            for k in sorted(ka & kb):
                if a[k] != b[k]:
                    print(f"  differs [{k}]:\n    delivered={json.dumps(a[k])[:300]}\n    scratch  ={json.dumps(b[k])[:300]}")
    print("=== global keys ===")
    for k in sorted(set(delivered) | set(scratch)):
        if k == "pins":
            continue
        same = delivered.get(k) == scratch.get(k)
        print(f"{k}: identical={same}")
        if not same:
            print(f"  delivered={json.dumps(delivered.get(k))[:300]}")
            print(f"  scratch  ={json.dumps(scratch.get(k))[:300]}")


if __name__ == "__main__":
    main()
