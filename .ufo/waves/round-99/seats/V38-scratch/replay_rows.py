#!/usr/bin/env python3
"""Independent replay of r99-gate-blind-spot-table rows. Scratch only."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCR = LANE / ".ufo/waves/round-99/seats/V38-scratch/replay"
PY = sys.executable


def run(cmd, cwd=LANE):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def show(label, code, out, err):
    print(f"--- {label} exit={code} ---")
    text = (out + (("\nSTDERR " + err) if err.strip() else "")).rstrip()
    print(text)
    return code, out


def copy_r99(name):
    dest = SCR / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(LANE / "corpus/fixtures/r99-window-lapse", dest)
    return dest


def mirror_r98(name):
    root = SCR / name
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py", root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(LANE / "corpus/tools/dependency-freeze-contract.json", root / "corpus/tools/dependency-freeze-contract.json")
    fix = root / "corpus/fixtures/r98-clerk-filing"
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", fix)
    return root, fix


def set_dep(fix, event_id, deps):
    path = fix / "timeline.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    for rec in rows:
        if rec["id"] == event_id:
            rec["depends_on"] = deps
    path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def delete_event(fix, event_id):
    path = fix / "timeline.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(json.dumps([r for r in rows if r["id"] != event_id], indent=2) + "\n", encoding="utf-8")


def set_source(fix, event_id, source_id):
    path = fix / "timeline.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    for rec in rows:
        if rec["id"] == event_id:
            rec["source_id"] = source_id
    path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def set_tick(fix, event_id, tick):
    path = fix / "timeline.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    for rec in rows:
        if rec["id"] == event_id:
            rec["tick"] = tick
    path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def drop_key(fix, event_id, key):
    path = fix / "timeline.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    for rec in rows:
        if rec["id"] == event_id:
            rec.pop(key, None)
    path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def set_field(fix, event_id, key, value):
    path = fix / "timeline.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    for rec in rows:
        if rec["id"] == event_id:
            rec[key] = value
    path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def replace_span(fix, old, new):
    path = fix / "claim-excerpt-map.md"
    text = path.read_text(encoding="utf-8")
    # J05 span cell is the standalone | 17 | before verbatim
    needle = "| `fictional-excerpts.md` | 17 | `verbatim` | `The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.` |"
    repl = needle.replace("| 17 |", f"| {new} |", 1)
    if needle not in text:
        raise SystemExit("J05 span needle missing")
    path.write_text(text.replace(needle, repl, 1), encoding="utf-8")


def delete_map_row(fix, row_id):
    path = fix / "claim-excerpt-map.md"
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = [ln for ln in lines if not ln.startswith(f"| {row_id} |")]
    path.write_text("".join(out), encoding="utf-8")


def restate_inventory(fix, old, new):
    path = fix / "claim-excerpt-map.md"
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"inventory needle missing: {old}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def gates(fix, label):
    for tool, args in (
        ("check_bible", [PY, str(LANE / "corpus/fixtures/check_bible.py"), str(fix)]),
        ("support_check", [PY, str(LANE / "corpus/tools/support_check.py"), str(fix)]),
        ("map_obligations", [PY, str(LANE / "corpus/tools/map_obligations.py"), str(fix)]),
    ):
        code, out, err = run(args)
        # keep last lines that carry the receipt
        interesting = [ln for ln in (out + err).splitlines() if ln.startswith(("CLEAN", "VIOLATION", "FINDING", "RESULT", "OBLIGATIONS", "FAIL", "INVENTORY", "SOURCE-SUPPORT"))]
        print(f"{label} {tool} exit={code} :: {' || '.join(interesting[:8])}")


def freeze(root, fix, label):
    tool = root / "corpus/tools/dependency_freeze.py"
    code, out, err = run([PY, str(tool), str(fix)], cwd=root)
    interesting = [ln for ln in (out + err).splitlines() if ln.startswith(("FREEZE", "FINDING", "RESULT", "DIGEST"))]
    print(f"{label} freeze exit={code} :: {' || '.join(interesting)}")


def main():
    if SCR.exists():
        shutil.rmtree(SCR)
    SCR.mkdir(parents=True)
    print("TOOL", __import__("hashlib").sha256((LANE/"corpus/tools/dependency_freeze.py").read_bytes()).hexdigest())
    print("CONTRACT", __import__("hashlib").sha256((LANE/"corpus/tools/dependency-freeze-contract.json").read_bytes()).hexdigest())

    print("\n== ROW 1 ==")
    f = copy_r99("r1-r99")
    set_dep(f, "clerk-lapse-recorded", [])
    gates(f, "r1-r99")
    root, fix = mirror_r98("r1-r98")
    set_dep(fix, "clerk-filing-open", [])
    freeze(root, fix, "r1-r98")
    gates(fix, "r1-r98")

    print("\n== ROW 1b ==")
    root, fix = mirror_r98("r1b")
    set_dep(fix, "paired-crossing-decision", ["aru-ninth-bell"])
    freeze(root, fix, "r1b")
    gates(fix, "r1b")

    print("\n== ROW 2 ==")
    f = copy_r99("r2-r99")
    set_dep(f, "clerk-lapse-recorded", ["acknowledgment-aru-records"])
    gates(f, "r2-r99")
    root, fix = mirror_r98("r2-r98")
    set_dep(fix, "clerk-filing-open", ["response-evin-salt-court"])
    freeze(root, fix, "r2-r98")
    gates(fix, "r2-r98")

    print("\n== ROW 3 ==")
    f = copy_r99("r3-r99")
    delete_event(f, "clerk-lapse-recorded")
    gates(f, "r3-r99")
    root, fix = mirror_r98("r3-r98")
    delete_event(fix, "clerk-filing-open")
    freeze(root, fix, "r3-r98")
    gates(fix, "r3-r98")

    print("\n== ROW 4 ==")
    f = copy_r99("r4-r99")
    replace_span(f, 17, 20)
    gates(f, "r4-r99")
    root, fix = mirror_r98("r4-r98")
    replace_span(fix, 17, 20)
    freeze(root, fix, "r4-r98")

    print("\n== ROW 5 ==")
    f = copy_r99("r5-r99")
    set_source(f, "clerk-lapse-recorded", "clerk-filing-note")
    gates(f, "r5-r99")
    root, fix = mirror_r98("r5-r98")
    set_source(fix, "clerk-filing-open", "aru-acknowledgment-note")
    freeze(root, fix, "r5-r98")
    gates(fix, "r5-r98")

    print("\n== ROW 6 ==")
    old = "depends on both ninth-bell entries"
    new = "follows both ninth-bell entries"
    # baseline tool
    base = SCR / "r6-baseline"
    if base.exists():
        shutil.rmtree(base)
    (base / "corpus/tools").mkdir(parents=True)
    tool = base / "corpus/tools/dependency_freeze.py"
    contract = base / "corpus/tools/dependency-freeze-contract.json"
    tool.write_bytes(subprocess.check_output(["git", "show", "4265df5:corpus/tools/dependency_freeze.py"], cwd=LANE))
    contract.write_bytes(subprocess.check_output(["git", "show", "4265df5:corpus/tools/dependency-freeze-contract.json"], cwd=LANE))
    bfix = base / "corpus/fixtures/r98-clerk-filing"
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", bfix)
    for name in ("fictional-excerpts.md", "claim-excerpt-map.md"):
        p = bfix / name
        p.write_text(p.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
    freeze(base, bfix, "r6-baseline")
    root, fix = mirror_r98("r6-delivered")
    for name in ("fictional-excerpts.md", "claim-excerpt-map.md"):
        p = fix / name
        p.write_text(p.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
    freeze(root, fix, "r6-delivered")
    gates(fix, "r6-delivered")
    # narrative-only
    root, fix = mirror_r98("r6-narr")
    p = fix / "claim-excerpt-map.md"
    narr_old = "depends on both (`aru-ninth-bell` and `evin-ninth-bell`)"
    text = p.read_text(encoding="utf-8")
    if narr_old not in text:
        print("NARR NEEDLE MISSING")
        # show nearby
        for i, ln in enumerate(text.splitlines(), 1):
            if "aru-ninth-bell" in ln and "evin-ninth-bell" in ln and not ln.startswith("| J"):
                print("CANDIDATE", i, ln[:180])
    else:
        p.write_text(text.replace(narr_old, "is recorded after both (`aru-ninth-bell` and `evin-ninth-bell`)", 1), encoding="utf-8")
        freeze(root, fix, "r6-narr")
        gates(fix, "r6-narr")
    # excerpt-only
    f = copy_r99("r6-excerpt-only")
    p = f / "fictional-excerpts.md"
    p.write_text(p.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")
    gates(f, "r6-excerpt-only")

    print("\n== ROW 7 ==")
    f = copy_r99("r7-r99")
    delete_event(f, "clerk-lapse-recorded")
    delete_map_row(f, "J21")
    restate_inventory(
        f,
        "**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.",
        "**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.",
    )
    gates(f, "r7-r99")
    root, fix = mirror_r98("r7-r98")
    delete_event(fix, "clerk-filing-open")
    delete_map_row(fix, "J20")
    restate_inventory(
        fix,
        "**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.",
        "**Expected inventory:** 19 JSON facts; 2 editorial rows; 21 total mapped rows; 17 distinct excerpt anchors.",
    )
    gates(fix, "r7-r98")
    freeze(root, fix, "r7-r98")

    print("\n== ROW 8 ==")
    code, out, err = run([PY, str(LANE / "corpus/tools/boundary_doc_check.py")])
    show("r8-live", code, out, err)
    drift = SCR / "check_bible-drift.py"
    drift.write_text((LANE / "corpus/fixtures/check_bible.py").read_text(encoding="utf-8") + "\n# drift\n", encoding="utf-8")
    code, out, err = run([PY, str(LANE / "corpus/tools/boundary_doc_check.py"), "--checker", str(drift)])
    show("r8-drift", code, out, err)

    print("\n== ROW 9 ==")
    probes = [
        ("unknown-event", lambda f: set_dep(f, "clerk-lapse-recorded", ["no-such-event-id"])),
        ("dangling-entity", lambda f: set_field(f, "clerk-lapse-recorded", "entity_id", "no-such-entity")),
        ("unknown-source", lambda f: set_source(f, "clerk-lapse-recorded", "no-such-source")),
        ("drop-key", lambda f: drop_key(f, "clerk-lapse-recorded", "depends_on")),
        ("self-dep", lambda f: set_dep(f, "clerk-lapse-recorded", ["clerk-lapse-recorded"])),
        ("repeated", lambda f: set_dep(f, "clerk-lapse-recorded", ["clerk-filing-open", "clerk-filing-open"])),
        ("inversion", lambda f: set_tick(f, "clerk-lapse-recorded", 14)),
        ("delete-pred", lambda f: delete_event(f, "clerk-filing-open")),
    ]
    for name, mut in probes:
        f = copy_r99("r9-" + name)
        mut(f)
        code, out, err = run([PY, str(LANE / "corpus/fixtures/check_bible.py"), str(f)])
        viol = [ln for ln in out.splitlines() if "VIOLATION" in ln or ln.startswith("CLEAN")]
        print(f"r9 {name} exit={code} :: {' || '.join(viol)}")


if __name__ == "__main__":
    main()
