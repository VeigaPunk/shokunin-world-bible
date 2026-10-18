#!/usr/bin/env python3
"""Independent replay of r99-gate-blind-spot-table rows. Scratch only."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V72-scratch"
WORK = SCRATCH / "table-replay"
if WORK.exists():
    shutil.rmtree(WORK)
WORK.mkdir()
PY = sys.executable


def run(argv, cwd=LANE):
    result = subprocess.run([str(a) for a in argv], cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def brief(code, out, err=""):
    lines = [ln for ln in out.splitlines() if ln.startswith(("FINDING", "RESULT", "FREEZE", "CLEAN", "OBLIGATIONS", "VIOLATION", "FAIL", "SOURCE-SUPPORT", "CERTIF", "CHECK "))]
    if not lines:
        lines = out.splitlines()[:4]
    print(f"  exit={code}")
    for ln in lines[:8]:
        print("  ", ln[:240])
    if err.strip():
        print("  stderr", err.strip().splitlines()[0][:200])


def copy_r99(name):
    dest = WORK / name
    shutil.copytree(LANE / "corpus/fixtures/r99-window-lapse", dest)
    return dest


def mirror_r98(name):
    root = WORK / name
    (root / "corpus/tools").mkdir(parents=True)
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py", root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(LANE / "corpus/tools/dependency-freeze-contract.json", root / "corpus/tools/dependency-freeze-contract.json")
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", root / "corpus/fixtures/r98-clerk-filing")
    return root, root / "corpus/fixtures/r98-clerk-filing"


def freeze(root):
    return run([PY, root / "corpus/tools/dependency_freeze.py", root / "corpus/fixtures/r98-clerk-filing"])


def gates(path):
    for tool in [
        LANE / "corpus/fixtures/check_bible.py",
        LANE / "corpus/tools/support_check.py",
        LANE / "corpus/tools/map_obligations.py",
    ]:
        code, out, err = run([PY, tool, path])
        print(" ", tool.name)
        brief(code, out, err)


def load_tl(path):
    return json.loads((path / "timeline.json").read_text())


def save_tl(path, data):
    (path / "timeline.json").write_text(json.dumps(data, indent=2) + "\n")


print("=== hashes ===")
tool = (LANE / "corpus/tools/dependency_freeze.py").read_bytes()
contract = (LANE / "corpus/tools/dependency-freeze-contract.json").read_bytes()
checker = (LANE / "corpus/fixtures/check_bible.py").read_bytes()
print("tool", hashlib.sha256(tool).hexdigest())
print("contract", hashlib.sha256(contract).hexdigest())
print("checker", hashlib.sha256(checker).hexdigest())
base_tool = SCRATCH / "baseline-4265df5-dependency_freeze.py"
print("baseline tool", hashlib.sha256(base_tool.read_bytes()).hexdigest() if base_tool.exists() else "MISSING")

print("\n=== ROW1 r98 emptied clerk-filing-open.depends_on ===")
root, fix = mirror_r98("r1")
tl = load_tl(fix)
for rec in tl:
    if rec["id"] == "clerk-filing-open":
        rec["depends_on"] = []
save_tl(fix, tl)
code, out, err = freeze(root)
brief(code, out, err)
code, out, err = run([PY, LANE / "corpus/fixtures/check_bible.py", fix])
print(" check_bible")
brief(code, out, err)

print("\n=== ROW1 r99 twin emptied clerk-lapse-recorded.depends_on ===")
fix = copy_r99("r1-r99")
tl = load_tl(fix)
for rec in tl:
    if rec["id"] == "clerk-lapse-recorded":
        rec["depends_on"] = []
save_tl(fix, tl)
gates(fix)

print("\n=== ROW1b drop evin-ninth-bell ===")
root, fix = mirror_r98("r1b")
tl = load_tl(fix)
for rec in tl:
    if rec["id"] == "paired-crossing-decision":
        rec["depends_on"] = [d for d in rec["depends_on"] if d != "evin-ninth-bell"]
save_tl(fix, tl)
code, out, err = freeze(root)
brief(code, out, err)
code, out, err = run([PY, LANE / "corpus/fixtures/check_bible.py", fix])
print(" check_bible")
brief(code, out, err)

print("\n=== ROW2 r98 wrong-but-earlier ===")
root, fix = mirror_r98("r2")
tl = load_tl(fix)
for rec in tl:
    if rec["id"] == "clerk-filing-open":
        rec["depends_on"] = ["response-evin-salt-court"]
save_tl(fix, tl)
code, out, err = freeze(root)
brief(code, out, err)
code, out, err = run([PY, LANE / "corpus/fixtures/check_bible.py", fix])
print(" check_bible")
brief(code, out, err)

print("\n=== ROW2 r99 twin ===")
fix = copy_r99("r2-r99")
tl = load_tl(fix)
for rec in tl:
    if rec["id"] == "clerk-lapse-recorded":
        rec["depends_on"] = ["acknowledgment-aru-records"]
save_tl(fix, tl)
gates(fix)

print("\n=== ROW3 r99 delete terminal keep map ===")
fix = copy_r99("r3-r99")
tl = load_tl(fix)
tl = [rec for rec in tl if rec["id"] != "clerk-lapse-recorded"]
save_tl(fix, tl)
gates(fix)

print("\n=== ROW3 r98 delete clerk-filing-open ===")
root, fix = mirror_r98("r3")
tl = load_tl(fix)
tl = [rec for rec in tl if rec["id"] != "clerk-filing-open"]
save_tl(fix, tl)
code, out, err = freeze(root)
brief(code, out, err)
code, out, err = run([PY, LANE / "corpus/fixtures/check_bible.py", fix])
print(" check_bible")
brief(code, out, err)

print("\n=== ROW4 r99 span 17->20 ===")
fix = copy_r99("r4-r99")
text = (fix / "claim-excerpt-map.md").read_text()
old = "| J05 | `entities.json#/4/first_appearance` (`chalk-stair`) | `crossing-minute` | `r99-window-lapse:crossing-minute` | `fictional-excerpts.md` | 17 | `verbatim` |"
new = old.replace("| 17 |", "| 20 |")
if old not in text:
    print(" J05 row pattern missing")
else:
    (fix / "claim-excerpt-map.md").write_text(text.replace(old, new, 1))
gates(fix)

print("\n=== ROW4 r98 span edit freeze ===")
root, fix = mirror_r98("r4")
text = (fix / "claim-excerpt-map.md").read_text()
old = "| J05 | `entities.json#/4/first_appearance` (`chalk-stair`) | `crossing-minute` | `r98-clerk-filing:crossing-minute` | `fictional-excerpts.md` | 17 | `verbatim` |"
if old not in text:
    print(" J05 r98 pattern missing")
    for line in text.splitlines():
        if line.startswith("| J05 "):
            print(" actual", line)
else:
    (fix / "claim-excerpt-map.md").write_text(text.replace(old, old.replace("| 17 |", "| 20 |"), 1))
code, out, err = freeze(root)
brief(code, out, err)

print("\n=== ROW5 r99 source_id rebound ===")
fix = copy_r99("r5-r99")
tl = load_tl(fix)
for rec in tl:
    if rec["id"] == "clerk-lapse-recorded":
        rec["source_id"] = "clerk-filing-note"
save_tl(fix, tl)
gates(fix)

print("\n=== ROW5 r98 source_id rebound freeze+map ===")
root, fix = mirror_r98("r5")
tl = load_tl(fix)
for rec in tl:
    if rec["id"] == "clerk-filing-open":
        rec["source_id"] = "aru-acknowledgment-note"
save_tl(fix, tl)
code, out, err = freeze(root)
brief(code, out, err)
code, out, err = run([PY, LANE / "corpus/tools/map_obligations.py", fix])
print(" map")
brief(code, out, err)
code, out, err = run([PY, LANE / "corpus/tools/support_check.py", fix])
print(" support")
brief(code, out, err)

print("\n=== ROW6 coherent excerpt+anchor before and after ===")
needle = "depends on both ninth-bell entries"
repl = "follows both ninth-bell entries"
root, fix = mirror_r98("r6-before")
# swap in baseline tool+contract
shutil.copy2(base_tool, root / "corpus/tools/dependency_freeze.py")
shutil.copy2(SCRATCH / "baseline-4265df5-contract.json", root / "corpus/tools/dependency-freeze-contract.json")
for name in ("fictional-excerpts.md", "claim-excerpt-map.md"):
    p = fix / name
    p.write_text(p.read_text().replace(needle, repl))
code, out, err = freeze(root)
print(" before")
brief(code, out, err)
root, fix = mirror_r98("r6-after")
for name in ("fictional-excerpts.md", "claim-excerpt-map.md"):
    p = fix / name
    p.write_text(p.read_text().replace(needle, repl))
code, out, err = freeze(root)
print(" after")
brief(code, out, err)
print(" lexical on after copy")
gates(fix)

print("\n=== ROW6 narrative-only ===")
root, fix = mirror_r98("r6-narr")
p = fix / "claim-excerpt-map.md"
text = p.read_text()
old = "depends on both (`aru-ninth-bell` and `evin-ninth-bell`)"
new = "is recorded after both (`aru-ninth-bell` and `evin-ninth-bell`)"
print(" narrative needle present", old in text)
p.write_text(text.replace(old, new, 1))
code, out, err = freeze(root)
brief(code, out, err)
gates(fix)

print("\n=== ROW6 excerpt-only ===")
fix = copy_r99("r6-excerpt")
p = fix / "fictional-excerpts.md"
p.write_text(p.read_text().replace(needle, repl, 1))
gates(fix)

print("\n=== ROW7 consistent regen r98 ===")
root, fix = mirror_r98("r7")
tl = load_tl(fix)
tl = [rec for rec in tl if rec["id"] != "clerk-filing-open"]
save_tl(fix, tl)
mp = (fix / "claim-excerpt-map.md").read_text()
lines = []
for line in mp.splitlines(keepends=True):
    if line.startswith("| J20 "):
        continue
    lines.append(line)
text = "".join(lines)
text = text.replace(
    "**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.",
    "**Expected inventory:** 19 JSON facts; 2 editorial rows; 21 total mapped rows; 17 distinct excerpt anchors.",
    1,
)
(fix / "claim-excerpt-map.md").write_text(text)
print(" J20 removed", "| J20 |" not in text)
gates(fix)
code, out, err = freeze(root)
print(" freeze")
brief(code, out, err)

print("\n=== ROW8 boundary ===")
code, out, err = run([PY, LANE / "corpus/tools/boundary_doc_check.py"])
brief(code, out, err)
drift = WORK / "check_bible-drift.py"
drift.write_text((LANE / "corpus/fixtures/check_bible.py").read_text() + "\n# v72 drift\n")
code, out, err = run([PY, LANE / "corpus/tools/boundary_doc_check.py", "--checker", drift])
brief(code, out, err)
pin = json.loads((LANE / "corpus/tools/boundary-doc-contract.json").read_text())
# find checker sha
def find_sha(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("sha256", "checker") or "sha" in k:
                if isinstance(v, str) and len(v) == 64:
                    print(" pin", path + "." + k, v)
                else:
                    find_sha(v, path + "." + k)
            else:
                find_sha(v, path + "." + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj[:20]):
            find_sha(v, f"{path}[{i}]")
find_sha(pin)

print("\n=== ROW9 check_bible classes on r99 copies ===")
probes = []
fix = copy_r99("r9-unknown-event")
tl = load_tl(fix)
tl[-1]["depends_on"] = ["no-such-event-id"]
save_tl(fix, tl)
probes.append(("unknown-event", fix))
fix = copy_r99("r9-dangling")
tl = load_tl(fix)
tl[-1]["entity_id"] = "no-such-entity"
save_tl(fix, tl)
probes.append(("dangling-entity", fix))
fix = copy_r99("r9-source")
tl = load_tl(fix)
tl[-1]["source_id"] = "no-such-source"
save_tl(fix, tl)
probes.append(("unknown-source", fix))
fix = copy_r99("r9-drop-key")
tl = load_tl(fix)
del tl[-1]["depends_on"]
save_tl(fix, tl)
probes.append(("drop-key", fix))
fix = copy_r99("r9-self")
tl = load_tl(fix)
tl[-1]["depends_on"] = ["clerk-lapse-recorded"]
save_tl(fix, tl)
probes.append(("self", fix))
fix = copy_r99("r9-repeat")
tl = load_tl(fix)
tl[-1]["depends_on"] = ["clerk-filing-open", "clerk-filing-open"]
save_tl(fix, tl)
probes.append(("repeat", fix))
fix = copy_r99("r9-invert")
tl = load_tl(fix)
tl[-1]["tick"] = 14
save_tl(fix, tl)
probes.append(("invert", fix))
fix = copy_r99("r9-delete-pred")
tl = load_tl(fix)
tl = [rec for rec in tl if rec["id"] != "clerk-filing-open"]
save_tl(fix, tl)
probes.append(("delete-pred", fix))
for label, path in probes:
    code, out, err = run([PY, LANE / "corpus/fixtures/check_bible.py", path])
    print(label)
    brief(code, out, err)

print("\n=== scope-note line citations ===")
checks = {
    "sources.json": [45, 46, 48],
    "fictional-excerpts.md": [66, 70, 71, 72, 73, 74, 76],
    "timeline.json": [77, 84],
    "entities.json": [63, 66, 69],
    "claim-excerpt-map.md": [5, 42, 55, 69],
    "README.md": [3, 11, 13, 15, 21],
}
fix = LANE / "corpus/fixtures/r99-window-lapse"
for name, nums in checks.items():
    lines = (fix / name).read_text().splitlines()
    print(name, "nlines", len(lines))
    for n in nums:
        if 1 <= n <= len(lines):
            print(f"  {n}: {lines[n-1][:180]}")
        else:
            print(f"  {n}: OUT OF RANGE")
r94 = (LANE / "corpus/fixtures/r94-paired-crossing/fictional-excerpts.md").read_text().splitlines()
print("r94 excerpt 15-20:")
for n in range(15, 21):
    print(f"  {n}: {r94[n-1][:160]}")
print("REPLAY_DONE")
