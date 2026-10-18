#!/usr/bin/env python3
"""V31 calibration demos on the DELIVERED revision (copies only; producer bytes read-only)."""
import json, shutil, subprocess, sys, hashlib, re
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
TOOL = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "corpus/tools/map_obligations.py"
CONTRACT = Path(sys.argv[2]) if len(sys.argv) > 2 else REPO / "corpus/tools/map-obligations-contract.json"
SCRATCH = Path(sys.argv[3]) if len(sys.argv) > 3 else REPO / ".ufo/waves/round-97/seats/V31-scratch/delivered"
PY = sys.executable

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def run(cmd, cwd=REPO):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr

def main():
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    SCRATCH.mkdir(parents=True)
    tool_sha, contract_sha = sha(TOOL), sha(CONTRACT)
    print(f"DELIVERED map_obligations.py sha256={tool_sha}")
    print(f"DELIVERED contract sha256={contract_sha}")
    contract = json.loads(CONTRACT.read_text())
    ids = [c["id"] for c in contract["self_test"]["cases"]]
    print(f"CONTRACT cases n={len(ids)} ids={ids}")
    print(f"dual_pointer pinned: {'dual_pointer' in ids}")

    # A. pristine delivered copy: self-test should pass N/N
    a = SCRATCH / "pristine"
    a.mkdir()
    shutil.copy(TOOL, a / TOOL.name)
    shutil.copy(CONTRACT, a / CONTRACT.name)
    rc, out, err = run([PY, str(a / TOOL.name), "--self-test"])
    tail = [l for l in out.splitlines() if l.startswith(("SELF-TEST CASES", "RESULT", "FINDING"))]
    print("A pristine:", rc, tail, "stderr:", err[:200])
    dual_line = [l for l in out.splitlines() if l.startswith("SELF-TEST") and "dual_pointer" in l]
    print("A dual_pointer line:", dual_line)

    # B. loader sweep: drop each pinned case -> self-test must fail (exit != 0)
    sweep = []
    for cid in ids:
        d = SCRATCH / f"drop-{cid}"
        d.mkdir()
        shutil.copy(TOOL, d / TOOL.name)
        c2 = json.loads(CONTRACT.read_text())
        c2["self_test"]["cases"] = [x for x in c2["self_test"]["cases"] if x["id"] != cid]
        (d / CONTRACT.name).write_text(json.dumps(c2, indent=2) + "\n")
        rc, out, err = run([PY, str(d / TOOL.name), "--self-test"])
        first = next((l for l in out.splitlines() if l.startswith(("FINDING", "RESULT"))), "")
        names_case = cid in out
        sweep.append((cid, rc, first[:120], names_case))
        print(f"B drop-{cid}: exit={rc} first={first[:110]!r} names_dropped_case={names_case}")
    bad = [s for s in sweep if s[1] == 0]
    print(f"B sweep: {len(sweep)} drops, still-green={len(bad)} -> {[s[0] for s in bad]}")

    # C. load-bearing: neutralize second_pointer_mention in a copy -> self-test must FAIL on dual_pointer
    c = SCRATCH / "neutralized"
    c.mkdir()
    text = TOOL.read_text()
    target = 'return None if match is None else match.group(0).strip("`")'
    if target in text:
        neutral = text.replace(target, "return None  # V31 neutralized dual_pointer emission")
        mode = "function-body replace"
    else:
        neutral = None
    if neutral is None:
        # fallback: kill the gating append block
        pat = re.compile(r'gating\.append\(\(\s*\n\s*"dual_pointer".*?\n\s*\)\)', re.S)
        if pat.search(text):
            neutral = pat.sub("pass  # V31 neutralized", text)
            mode = "gating.append replace"
        else:
            mode = "NO NEUTRALIZATION TARGET FOUND"
    if neutral is not None:
        (c / TOOL.name).write_text(neutral)
        shutil.copy(CONTRACT, c / CONTRACT.name)
        rc, out, err = run([PY, str(c / TOOL.name), "--self-test"])
        lines = [l for l in out.splitlines() if l.startswith(("SELF-TEST FAIL", "RESULT", "FINDING"))]
        print(f"C neutralized ({mode}): exit={rc}")
        for l in lines:
            print("  ", l[:140])
        print(f"C neutralized sha256={sha(c / TOOL.name)}")
    else:
        print("C:", mode)

    # D. expectation-flip: keep dual_pointer pinned but flip its expectation -> case must FAIL
    d = SCRATCH / "flip-dual-pointer"
    d.mkdir()
    shutil.copy(TOOL, d / TOOL.name)
    c3 = json.loads(CONTRACT.read_text())
    flipped = False
    for case in c3["self_test"]["cases"]:
        if case["id"] == "dual_pointer":
            case["exit"] = 0
            case["finding_ids"] = []
            flipped = True
    assert flipped, "dual_pointer case not found for flip"
    (d / CONTRACT.name).write_text(json.dumps(c3, indent=2) + "\n")
    rc, out, err = run([PY, str(d / TOOL.name), "--self-test"])
    lines = [l for l in out.splitlines() if l.startswith(("SELF-TEST FAIL", "RESULT", "FINDING"))]
    print(f"D flip-dual-pointer: exit={rc}")
    for l in lines:
        print("  ", l[:140])

if __name__ == "__main__":
    main()
