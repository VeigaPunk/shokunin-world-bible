#!/usr/bin/env python3
"""Independent replay of r99-gate-blind-spot-table rows. Scratch only."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = ROOT / ".ufo/waves/round-99/seats/V51-scratch/table-replay"
R99 = ROOT / "corpus/fixtures/r99-window-lapse"
R98 = ROOT / "corpus/fixtures/r98-clerk-filing"
PY = sys.executable


def run(args, cwd=ROOT):
    r = subprocess.run([PY, *args], cwd=cwd, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    return r.returncode, out


def show(label, code, out, needles):
    hit = [n for n in needles if n not in out and n not in f"exit={code}"]
    # needles checked against combined text
    text = out + f"\nexit={code}"
    missing = [n for n in needles if n not in text]
    tag = "OK" if not missing else "MISS"
    print(f"\n## {tag} {label} exit={code}")
    if missing:
        print("  MISSING:", missing)
    # print last non-empty lines, capped
    lines = [ln for ln in out.splitlines() if ln.strip()]
    for ln in lines[:8]:
        print("  " + ln[:220])
    if len(lines) > 8:
        print(f"  ... ({len(lines)} lines)")
        for ln in lines[-4:]:
            print("  " + ln[:220])


def copy_r99(name):
    dest = SCRATCH / name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(R99, dest)
    return dest


def copy_r98_mirror(name):
    """Path-bound mirror: corpus/fixtures/r98-clerk-filing plus tool+contract."""
    dest = SCRATCH / name
    if dest.exists():
        shutil.rmtree(dest)
    fix = dest / "corpus/fixtures/r98-clerk-filing"
    tools = dest / "corpus/tools"
    fix.parent.mkdir(parents=True)
    shutil.copytree(R98, fix)
    tools.mkdir(parents=True)
    shutil.copy(ROOT / "corpus/tools/dependency_freeze.py", tools / "dependency_freeze.py")
    shutil.copy(ROOT / "corpus/tools/dependency-freeze-contract.json", tools / "dependency-freeze-contract.json")
    return dest, fix


def gates(label, dest, expect):
    rel = str(dest.relative_to(ROOT))
    for tool, args in (
        ("bible", ["corpus/fixtures/check_bible.py", rel]),
        ("support", ["corpus/tools/support_check.py", rel]),
        ("map", ["corpus/tools/map_obligations.py", rel]),
    ):
        code, out = run(args)
        needles = expect.get(tool, [])
        show(f"{label} {tool}", code, out, needles + [f"exit={expect['exit'][tool]}"])


def freeze(label, mirror, needles, expect_exit):
    tool = mirror / "corpus/tools/dependency_freeze.py"
    fix = mirror / "corpus/fixtures/r98-clerk-filing"
    code, out = run([str(tool), str(fix)], cwd=mirror)
    show(label, code, out, needles + [f"exit={expect_exit}"])


def main():
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    SCRATCH.mkdir(parents=True)

    print("=== LIVE CONTROLS ===")
    code, out = run(["corpus/fixtures/check_bible.py", "corpus/fixtures/r99-window-lapse"])
    show("live r99 bible", code, out, ["CLEAN", "exit=0"])
    code, out = run(["corpus/tools/map_obligations.py", "corpus/fixtures/r99-window-lapse"])
    show("live r99 map", code, out, ["raw=21 mapped=21", "RESULT PASS", "exit=0"])
    code, out = run(["corpus/tools/support_check.py", "corpus/fixtures/r99-window-lapse"])
    show("live r99 support", code, out, ["SOURCE-SUPPORT 21/21", "RESULT PASS", "exit=0"])
    code, out = run(["corpus/tools/dependency_freeze.py", "corpus/fixtures/r99-window-lapse"])
    show("live r99 freeze", code, out, ["UNPINNED-FIXTURE", "exit=2"])
    code, out = run(["corpus/tools/dependency_freeze.py", "--self-test"])
    show("self-test", code, out, ["SELF-TEST 18/18", "markdown_tamper", "DIGEST-MISMATCH", "RESULT PASS", "exit=0"])
    for name in (
        "r88-m3-maya-cluster",
        "r94-paired-crossing",
        "r95-crossing-aftermath",
        "r96-crossing-response",
        "r97-crossing-acknowledgment",
        "r98-clerk-filing",
    ):
        code, out = run(["corpus/tools/dependency_freeze.py", f"corpus/fixtures/{name}"])
        show(f"chain {name}", code, out, ["RESULT PASS", "exit=0"])
    code, out = run(["corpus/tools/boundary_doc_check.py"])
    show("boundary live", code, out, ["CERTIFIED", "exit=0"])

    print("\n=== ROW 1 emptied depends_on (r99 twin) ===")
    d = copy_r99("r1-empty")
    tl = json.loads((d / "timeline.json").read_text())
    tl[-1]["depends_on"] = []
    (d / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
    gates("r1", d, {"bible": ["CLEAN"], "support": ["RESULT PASS"], "map": ["raw=21 mapped=21", "RESULT PASS"], "exit": {"bible": 0, "support": 0, "map": 0}})

    print("\n=== ROW 1 freeze on r98 path-bound ===")
    mirror, fix = copy_r98_mirror("r1-freeze")
    tl = json.loads((fix / "timeline.json").read_text())
    for ev in tl:
        if ev["id"] == "clerk-filing-open":
            ev["depends_on"] = []
    (fix / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
    freeze("r1 freeze", mirror, ["REDUCTION-DETECTED", "clerk-filing-open", "acknowledgment-aru-records", "RESULT FAIL"], 1)
    code, out = run([str(ROOT / "corpus/fixtures/check_bible.py"), str(fix)])
    show("r1 freeze bible", code, out, ["CLEAN", "exit=0"])

    print("\n=== ROW 1b edge reduction ===")
    mirror, fix = copy_r98_mirror("r1b")
    tl = json.loads((fix / "timeline.json").read_text())
    for ev in tl:
        if ev["id"] == "paired-crossing-decision":
            ev["depends_on"] = ["aru-ninth-bell"]
    (fix / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
    freeze("r1b freeze", mirror, ["REDUCTION-DETECTED", "evin-ninth-bell", "RESULT FAIL"], 1)
    code, out = run([str(ROOT / "corpus/fixtures/check_bible.py"), str(fix)])
    show("r1b bible", code, out, ["CLEAN", "exit=0"])

    print("\n=== ROW 2 wrong-but-earlier r99 ===")
    d = copy_r99("r2")
    tl = json.loads((d / "timeline.json").read_text())
    tl[-1]["depends_on"] = ["acknowledgment-aru-records"]
    (d / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
    gates("r2", d, {"bible": ["CLEAN"], "support": ["RESULT PASS"], "map": ["raw=21 mapped=21", "RESULT PASS"], "exit": {"bible": 0, "support": 0, "map": 0}})

    print("\n=== ROW 2 freeze r98 ===")
    mirror, fix = copy_r98_mirror("r2-freeze")
    tl = json.loads((fix / "timeline.json").read_text())
    for ev in tl:
        if ev["id"] == "clerk-filing-open":
            ev["depends_on"] = ["response-evin-salt-court"]
    (fix / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
    freeze("r2 freeze", mirror, ["ADDITION-DETECTED", "REDUCTION-DETECTED", "response-evin-salt-court", "acknowledgment-aru-records", "RESULT FAIL"], 1)

    print("\n=== ROW 3 delete terminal r99 keep map ===")
    d = copy_r99("r3")
    tl = json.loads((d / "timeline.json").read_text())
    tl.pop()
    (d / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
    gates("r3", d, {"bible": ["CLEAN"], "support": ["RESULT PASS"], "map": ["phantom_obligation", "timeline.json#/7", "RESULT FAIL"], "exit": {"bible": 0, "support": 0, "map": 1}})

    print("\n=== ROW 3 freeze r98 delete terminal ===")
    mirror, fix = copy_r98_mirror("r3-freeze")
    tl = json.loads((fix / "timeline.json").read_text())
    tl = [ev for ev in tl if ev["id"] != "clerk-filing-open"]
    (fix / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
    freeze("r3 freeze", mirror, ["REDUCTION-DETECTED", "clerk-filing-open", "RESULT FAIL"], 1)

    print("\n=== ROW 4 span-break r99 ===")
    d = copy_r99("r4")
    text = (d / "claim-excerpt-map.md").read_text()
    old = "| J05 | `entities.json#/4/first_appearance` (`chalk-stair`) | `crossing-minute` | `r99-window-lapse:crossing-minute` | `fictional-excerpts.md` | 17 | `verbatim` |"
    new = old.replace("| 17 |", "| 20 |", 1)
    if old not in text:
        print("J05 row not found exactly")
    else:
        (d / "claim-excerpt-map.md").write_text(text.replace(old, new, 1))
        gates("r4", d, {"bible": ["CLEAN"], "support": ["outside-span", "RESULT FAIL"], "map": ["RESULT PASS"], "exit": {"bible": 0, "support": 1, "map": 0}})

    print("\n=== ROW 5 source-id mutant r99 ===")
    d = copy_r99("r5")
    tl = json.loads((d / "timeline.json").read_text())
    assert tl[-1]["source_id"] == "clerk-lapse-note"
    tl[-1]["source_id"] = "clerk-filing-note"
    (d / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
    gates("r5", d, {"bible": ["CLEAN"], "support": ["RESULT PASS"], "map": ["source_id_mismatch", "RESULT FAIL"], "exit": {"bible": 0, "support": 0, "map": 1}})

    print("\n=== ROW 6 prose coherent on r98, delivered pin ===")
    mirror, fix = copy_r98_mirror("r6")
    ex = (fix / "fictional-excerpts.md").read_text()
    mp = (fix / "claim-excerpt-map.md").read_text()
    phrase = "depends on both ninth-bell entries"
    repl = "follows both ninth-bell entries"
    print(f"  excerpt hits {ex.count(phrase)} map hits {mp.count(phrase)}")
    (fix / "fictional-excerpts.md").write_text(ex.replace(phrase, repl))
    (fix / "claim-excerpt-map.md").write_text(mp.replace(phrase, repl))
    freeze("r6 delivered", mirror, ["DIGEST-MISMATCH", "claim-excerpt-map.md", "fictional-excerpts.md", "RESULT ERROR"], 2)

    print("\n=== ROW 6 baseline tool same edit ===")
    base_tool = SCRATCH / "baseline-tool.py"
    base_tool.write_bytes(subprocess.check_output(["git", "show", "4265df5:corpus/tools/dependency_freeze.py"], cwd=ROOT))
    base_contract = SCRATCH / "baseline-contract.json"
    base_contract.write_bytes(subprocess.check_output(["git", "show", "4265df5:corpus/tools/dependency-freeze-contract.json"], cwd=ROOT))
    bmirror = SCRATCH / "r6-baseline"
    if bmirror.exists():
        shutil.rmtree(bmirror)
    bfix = bmirror / "corpus/fixtures/r98-clerk-filing"
    btools = bmirror / "corpus/tools"
    bfix.parent.mkdir(parents=True)
    shutil.copytree(R98, bfix)
    btools.mkdir()
    shutil.copy(base_tool, btools / "dependency_freeze.py")
    shutil.copy(base_contract, btools / "dependency-freeze-contract.json")
    ex = (bfix / "fictional-excerpts.md").read_text().replace(phrase, repl)
    mp = (bfix / "claim-excerpt-map.md").read_text().replace(phrase, repl)
    (bfix / "fictional-excerpts.md").write_text(ex)
    (bfix / "claim-excerpt-map.md").write_text(mp)
    code, out = run([str(btools / "dependency_freeze.py"), str(bfix)], cwd=bmirror)
    show("r6 baseline", code, out, ["RESULT PASS", "59a0f4fa", "exit=0"])

    print("\n=== ROW 8 drift ===")
    drift = SCRATCH / "check_bible-drift.py"
    drift.write_text((ROOT / "corpus/fixtures/check_bible.py").read_text() + "\n# v51 drift comment\n")
    code, out = run(["corpus/tools/boundary_doc_check.py", "--checker", str(drift.relative_to(ROOT))])
    show("r8 drift", code, out, ["checker_drift", "exit=1"])

    print("\n=== ROW 9 catches ===")
    probes = {
        "unknown-event": lambda tl: tl[-1].__setitem__("depends_on", ["no-such-event-id"]),
        "dangling-entity": lambda tl: tl[-1].__setitem__("entity_id", "no-such-entity"),
        "unknown-source": lambda tl: tl[-1].__setitem__("source_id", "no-such-source"),
        "drop-key": lambda tl: tl[-1].pop("depends_on"),
        "self": lambda tl: tl[-1].__setitem__("depends_on", ["clerk-lapse-recorded"]),
        "repeat": lambda tl: tl[-1].__setitem__("depends_on", ["clerk-filing-open", "clerk-filing-open"]),
        "invert": lambda tl: tl[-1].__setitem__("tick", 14),
    }
    for name, fn in probes.items():
        d = copy_r99(f"r9-{name}")
        tl = json.loads((d / "timeline.json").read_text())
        fn(tl)
        (d / "timeline.json").write_text(json.dumps(tl, indent=2) + "\n")
        code, out = run(["corpus/fixtures/check_bible.py", str(d.relative_to(ROOT))])
        show(f"r9 {name}", code, out, ["VIOLATION", "exit=1"])

    print("\n=== LIVE UNTOUCHED ===")
    import hashlib
    for rel in ("corpus/fixtures/r99-window-lapse/timeline.json", "corpus/fixtures/r98-clerk-filing/timeline.json"):
        h = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        print(rel, h[:16])


if __name__ == "__main__":
    main()
