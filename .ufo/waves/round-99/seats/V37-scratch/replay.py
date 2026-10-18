#!/usr/bin/env python3
"""Independent replay of r99-gate-blind-spot-table rows. Scratch only."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V37-scratch/replay"
if SCRATCH.exists():
    shutil.rmtree(SCRATCH)
SCRATCH.mkdir(parents=True)
TOOL = LANE / "corpus/tools/dependency_freeze.py"
CONTRACT = LANE / "corpus/tools/dependency-freeze-contract.json"


def run(cmd, cwd=LANE):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def tail(text, n=8):
    lines = [ln for ln in text.strip().splitlines() if ln.strip()]
    return "\n".join(lines[-n:])


def gates(label, fixture):
    print(f"\n--- gates {label} ---")
    for cmd in [
        [sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(fixture)],
        [sys.executable, str(LANE / "corpus/tools/support_check.py"), str(fixture)],
        [sys.executable, str(LANE / "corpus/tools/map_obligations.py"), str(fixture)],
    ]:
        rc, out, err = run(cmd)
        print(f"{Path(cmd[1]).name} rc={rc}")
        print(tail(out + err, 6))


def copy_fixture(name, dest_name=None):
    src = LANE / "corpus/fixtures" / name
    dest = SCRATCH / "plain" / (dest_name or name)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    return dest


def mirror(case):
    root = SCRATCH / "mirrors" / case
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    shutil.copy2(TOOL, root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(CONTRACT, root / "corpus/tools/dependency-freeze-contract.json")
    fix = root / "corpus/fixtures/r98-clerk-filing"
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", fix)
    return root, fix


def freeze(root, fix):
    rc, out, err = run([sys.executable, str(root / "corpus/tools/dependency_freeze.py"), str(fix)], cwd=root)
    print(f"freeze rc={rc}")
    print(out.strip())
    if err.strip():
        print("STDERR", err.strip()[:300])
    return rc, out


def load_timeline(path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump_timeline(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def mutate_event(fixture, event_id, **fields):
    path = fixture / "timeline.json"
    data = load_timeline(path)
    for record in data:
        if record.get("id") == event_id:
            record.update(fields)
            break
    else:
        raise SystemExit(f"missing {event_id}")
    dump_timeline(path, data)


def delete_event(fixture, event_id):
    path = fixture / "timeline.json"
    data = [r for r in load_timeline(path) if r.get("id") != event_id]
    dump_timeline(path, data)


print("===== row 1 emptied depends_on =====")
r99 = copy_fixture("r99-window-lapse", "r1-r99")
mutate_event(r99, "clerk-lapse-recorded", depends_on=[])
gates("r99 empty lapse edge", r99)
root, fix = mirror("r1")
mutate_event(fix, "clerk-filing-open", depends_on=[])
freeze(root, fix)
gates("r98 empty filing edge", fix)

print("\n===== row 1b drop one predecessor =====")
root, fix = mirror("r1b")
mutate_event(fix, "paired-crossing-decision", depends_on=["aru-ninth-bell"])
freeze(root, fix)
gates("r98 drop evin edge", fix)

print("\n===== row 2 wrong-but-earlier =====")
r99 = copy_fixture("r99-window-lapse", "r2-r99")
mutate_event(r99, "clerk-lapse-recorded", depends_on=["acknowledgment-aru-records"])
gates("r99 wrong-earlier", r99)
root, fix = mirror("r2")
mutate_event(fix, "clerk-filing-open", depends_on=["response-evin-salt-court"])
freeze(root, fix)
gates("r98 wrong-earlier", fix)

print("\n===== row 3 deleted terminal =====")
r99 = copy_fixture("r99-window-lapse", "r3-r99")
delete_event(r99, "clerk-lapse-recorded")
gates("r99 delete terminal keep map", r99)
root, fix = mirror("r3")
delete_event(fix, "clerk-filing-open")
freeze(root, fix)
gates("r98 delete terminal", fix)

print("\n===== row 4 span-break =====")
r99 = copy_fixture("r99-window-lapse", "r4-r99")
text = (r99 / "claim-excerpt-map.md").read_text(encoding="utf-8")
old = "| J05 |"
# span cell is the 6th pipe-field; do a unique replace of the J05 span token ` | 17 | `
needle = None
for line in text.splitlines():
    if line.startswith("| J05 |"):
        needle = line
        break
print("J05 line found", needle is not None)
if needle:
    # replace the span cell 17 with 20 only on this line
    parts = needle.split("|")
    # parts[0] empty, 1=J05, ... span is index 6 typically
    print("J05 parts", [p.strip() for p in parts])
    new_line = needle.replace("| 17 |", "| 20 |", 1)
    (r99 / "claim-excerpt-map.md").write_text(text.replace(needle, new_line, 1), encoding="utf-8")
gates("r99 span-break", r99)
root, fix = mirror("r4")
text = (fix / "claim-excerpt-map.md").read_text(encoding="utf-8")
for line in text.splitlines():
    if line.startswith("| J05 |"):
        new_line = line.replace("| 17 |", "| 20 |", 1)
        (fix / "claim-excerpt-map.md").write_text(text.replace(line, new_line, 1), encoding="utf-8")
        break
freeze(root, fix)

print("\n===== row 5 source-id =====")
r99 = copy_fixture("r99-window-lapse", "r5-r99")
mutate_event(r99, "clerk-lapse-recorded", source_id="clerk-filing-note")
gates("r99 source-id", r99)
root, fix = mirror("r5")
mutate_event(fix, "clerk-filing-open", source_id="aru-acknowledgment-note")
freeze(root, fix)
gates("r98 source-id", fix)

print("\n===== row 6 prose =====")
phrase = "depends on both ninth-bell entries"
repl = "follows both ninth-bell entries"
root, fix = mirror("r6")
for name in ("fictional-excerpts.md", "claim-excerpt-map.md"):
    path = fix / name
    raw = path.read_text(encoding="utf-8")
    print(name, "count", raw.count(phrase))
    path.write_text(raw.replace(phrase, repl), encoding="utf-8")
freeze(root, fix)
gates("coherent prose", fix)
# baseline tool
before = SCRATCH / "before"
(before / "corpus/tools").mkdir(parents=True)
(before / "corpus/tools/dependency_freeze.py").write_bytes(
    subprocess.check_output(["git", "show", "4265df5:corpus/tools/dependency_freeze.py"], cwd=LANE)
)
(before / "corpus/tools/dependency-freeze-contract.json").write_bytes(
    subprocess.check_output(["git", "show", "4265df5:corpus/tools/dependency-freeze-contract.json"], cwd=LANE)
)
bfix = before / "corpus/fixtures/r98-clerk-filing"
shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", bfix)
for name in ("fictional-excerpts.md", "claim-excerpt-map.md"):
    path = bfix / name
    path.write_text(path.read_text(encoding="utf-8").replace(phrase, repl), encoding="utf-8")
rc, out, err = run([sys.executable, str(before / "corpus/tools/dependency_freeze.py"), str(bfix)], cwd=before)
print("BASELINE coherent rc", rc)
print(out.strip())
# narrative-only
root, fix = mirror("r6narr")
mp = fix / "claim-excerpt-map.md"
raw = mp.read_text(encoding="utf-8")
narr = "depends on both (`aru-ninth-bell` and `evin-ninth-bell`)"
print("narr count", raw.count(narr))
mp.write_text(raw.replace(narr, "is recorded after both (`aru-ninth-bell` and `evin-ninth-bell`)", 1), encoding="utf-8")
freeze(root, fix)
gates("narrative-only", fix)
# excerpt-only
r99 = copy_fixture("r99-window-lapse", "r6-excerpt")
ex = r99 / "fictional-excerpts.md"
ex.write_text(ex.read_text(encoding="utf-8").replace(phrase, repl, 1), encoding="utf-8")
gates("excerpt-only", r99)

print("\n===== row 7 consistent regen =====")
r99 = copy_fixture("r99-window-lapse", "r7-r99")
delete_event(r99, "clerk-lapse-recorded")
mp = r99 / "claim-excerpt-map.md"
text = mp.read_text(encoding="utf-8")
lines = [ln for ln in text.splitlines() if not ln.startswith("| J21 |")]
text = "\n".join(lines) + "\n"
text = text.replace("21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors",
                    "20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors")
mp.write_text(text, encoding="utf-8")
gates("r99 coherent regen", r99)
root, fix = mirror("r7")
delete_event(fix, "clerk-filing-open")
mp = fix / "claim-excerpt-map.md"
text = mp.read_text(encoding="utf-8")
lines = [ln for ln in text.splitlines() if not ln.startswith("| J20 |")]
text = "\n".join(lines) + "\n"
text = text.replace("20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors",
                    "19 JSON facts; 2 editorial rows; 21 total mapped rows; 17 distinct excerpt anchors")
mp.write_text(text, encoding="utf-8")
freeze(root, fix)
gates("r98 coherent regen", fix)

print("\n===== row 8 checker pin =====")
import hashlib
checker = (LANE / "corpus/fixtures/check_bible.py").read_bytes()
print("checker", hashlib.sha256(checker).hexdigest())
contract = json.loads((LANE / "corpus/tools/boundary-doc-contract.json").read_text())
print("pin", contract.get("checker", contract.get("checker.sha256", "KEYS "+str(list(contract)[:12]))))
rc, out, err = run([sys.executable, "corpus/tools/boundary_doc_check.py"])
print("boundary rc", rc)
print(tail(out + err, 12))
drift = SCRATCH / "check_bible-drift.py"
drift.write_bytes(checker + b"\n# drift\n")
rc, out, err = run([sys.executable, "corpus/tools/boundary_doc_check.py", "--checker", str(drift)])
print("drift rc", rc)
print(tail(out + err, 8))

print("\n===== row 9 check_bible catches =====")
probes = [
    ("unknown-event", {"depends_on": ["no-such-event-id"]}),
    ("dangling-entity", {"entity_id": "no-such-entity"}),
    ("unknown-source", {"source_id": "no-such-source"}),
]
for name, fields in probes:
    fx = copy_fixture("r99-window-lapse", name)
    mutate_event(fx, "clerk-lapse-recorded", **fields)
    rc, out, err = run([sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(fx)])
    print(name, rc, tail(out + err, 3))
fx = copy_fixture("r99-window-lapse", "drop-key")
data = load_timeline(fx / "timeline.json")
for record in data:
    if record["id"] == "clerk-lapse-recorded":
        record.pop("depends_on", None)
dump_timeline(fx / "timeline.json", data)
rc, out, err = run([sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(fx)])
print("drop-key", rc, tail(out + err, 3))
fx = copy_fixture("r99-window-lapse", "self-dep")
mutate_event(fx, "clerk-lapse-recorded", depends_on=["clerk-lapse-recorded"])
rc, out, err = run([sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(fx)])
print("self-dep", rc, tail(out + err, 4))
fx = copy_fixture("r99-window-lapse", "repeat")
mutate_event(fx, "clerk-lapse-recorded", depends_on=["clerk-filing-open", "clerk-filing-open"])
rc, out, err = run([sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(fx)])
print("repeat", rc, tail(out + err, 3))
fx = copy_fixture("r99-window-lapse", "invert")
mutate_event(fx, "clerk-lapse-recorded", tick=14)
rc, out, err = run([sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(fx)])
print("invert", rc, tail(out + err, 3))
fx = copy_fixture("r99-window-lapse", "delete-pred")
delete_event(fx, "clerk-filing-open")
rc, out, err = run([sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(fx)])
print("delete-pred", rc, tail(out + err, 3))
