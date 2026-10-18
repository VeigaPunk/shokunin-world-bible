#!/usr/bin/env python3
"""Independent replay of r99-gate-blind-spot-table rows. Scratch only."""
import hashlib, json, shutil, subprocess
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCR = ROOT / ".ufo/waves/round-99/seats/V75-scratch/row-replay"
if SCR.exists():
    shutil.rmtree(SCR)
SCR.mkdir(parents=True)
LOG = []

def p(s=""):
    print(s)
    LOG.append(s)

def run(cmd, cwd=ROOT):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr

def tail_hits(stdout):
    keep = []
    for line in (stdout or "").splitlines():
        if line.startswith(("FINDING", "RESULT", "CLEAN", "FAIL", "FREEZE", "OBLIGATIONS", "SOURCE-SUPPORT", "VIOLATION", "CERTIFIED", "CERTIFICATION", "CHECK ")):
            keep.append(line)
    return keep

def bible(fix):
    rc, so, se = run(["python3", str(ROOT/"corpus/fixtures/check_bible.py"), str(fix)])
    return rc, tail_hits(so)

def support(fix):
    rc, so, se = run(["python3", str(ROOT/"corpus/tools/support_check.py"), str(fix)])
    return rc, tail_hits(so)

def mapa(fix):
    rc, so, se = run(["python3", str(ROOT/"corpus/tools/map_obligations.py"), str(fix)])
    return rc, tail_hits(so)

def freeze_mirror(name, mutate):
    m = SCR / name
    (m/"corpus/tools").mkdir(parents=True)
    shutil.copy2(ROOT/"corpus/tools/dependency_freeze.py", m/"corpus/tools/dependency_freeze.py")
    shutil.copy2(ROOT/"corpus/tools/dependency-freeze-contract.json", m/"corpus/tools/dependency-freeze-contract.json")
    fix = m/"corpus/fixtures/r98-clerk-filing"
    shutil.copytree(ROOT/"corpus/fixtures/r98-clerk-filing", fix)
    mutate(fix)
    rc, so, se = run(["python3", str(m/"corpus/tools/dependency_freeze.py"), str(fix)], cwd=m)
    return rc, tail_hits(so), fix

def copy_r99(name):
    fix = SCR / name
    shutil.copytree(ROOT/"corpus/fixtures/r99-window-lapse", fix)
    return fix

def copy_r98(name):
    fix = SCR / name
    shutil.copytree(ROOT/"corpus/fixtures/r98-clerk-filing", fix)
    return fix

def set_dep(fix, event_id, deps):
    path = fix/"timeline.json"
    data = json.loads(path.read_text())
    for rec in data:
        if rec["id"] == event_id:
            rec["depends_on"] = deps
    path.write_text(json.dumps(data, indent=2) + "\n")

def delete_event(fix, event_id):
    path = fix/"timeline.json"
    data = json.loads(path.read_text())
    data = [rec for rec in data if rec["id"] != event_id]
    path.write_text(json.dumps(data, indent=2) + "\n")

def set_source(fix, event_id, source_id):
    path = fix/"timeline.json"
    data = json.loads(path.read_text())
    for rec in data:
        if rec["id"] == event_id:
            rec["source_id"] = source_id
    path.write_text(json.dumps(data, indent=2) + "\n")

p("tool " + hashlib.sha256((ROOT/"corpus/tools/dependency_freeze.py").read_bytes()).hexdigest())
p("contract " + hashlib.sha256((ROOT/"corpus/tools/dependency-freeze-contract.json").read_bytes()).hexdigest())

# Row 1
p("== ROW 1 emptied depends_on ==")
rc, hits, _ = freeze_mirror("r1-freeze", lambda f: set_dep(f, "clerk-filing-open", []))
p(f"freeze EXIT {rc}")
for h in hits: p("  "+h)
fix = copy_r99("r1-r99")
set_dep(fix, "clerk-lapse-recorded", [])
for name, fn in (("bible", bible), ("support", support), ("map", mapa)):
    rc, hits = fn(fix)
    p(f"r99-twin {name} EXIT {rc} {hits[:4]}")
rc, hits = bible(SCR/"r1-freeze/corpus/fixtures/r98-clerk-filing")
p(f"r98-mirror bible EXIT {rc} {hits}")

# Row 1b
p("== ROW 1b edge reduction ==")
rc, hits, fix = freeze_mirror("r1b", lambda f: set_dep(f, "paired-crossing-decision", ["aru-ninth-bell"]))
p(f"freeze EXIT {rc}")
for h in hits: p("  "+h)
rc, hits = bible(fix)
p(f"bible EXIT {rc} {hits}")

# Row 2
p("== ROW 2 wrong-but-earlier ==")
rc, hits, fix = freeze_mirror("r2", lambda f: set_dep(f, "clerk-filing-open", ["response-evin-salt-court"]))
p(f"freeze EXIT {rc}")
for h in hits: p("  "+h)
rc, hits = bible(fix)
p(f"r98 bible EXIT {rc} {hits}")
fix = copy_r99("r2-r99")
set_dep(fix, "clerk-lapse-recorded", ["acknowledgment-aru-records"])
for name, fn in (("bible", bible), ("support", support), ("map", mapa)):
    rc, hits = fn(fix)
    p(f"r99-twin {name} EXIT {rc} {hits[:3]}")

# Row 3
p("== ROW 3 deleted terminal ==")
fix = copy_r99("r3-r99")
delete_event(fix, "clerk-lapse-recorded")
for name, fn in (("bible", bible), ("support", support), ("map", mapa)):
    rc, hits = fn(fix)
    p(f"r99 {name} EXIT {rc}")
    for h in hits: p("  "+h)
rc, hits, fix = freeze_mirror("r3", lambda f: delete_event(f, "clerk-filing-open"))
p(f"r98 freeze EXIT {rc}")
for h in hits: p("  "+h)
rc, hits = bible(fix)
p(f"r98 bible EXIT {rc} {hits}")

# Row 4 span break
p("== ROW 4 span-break ==")
fix = copy_r99("r4-r99")
text = (fix/"claim-excerpt-map.md").read_text()
old = "| J05 |"
# replace span cell 17 with 20 on the J05 line only
lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith("| J05 |"):
        cells = line.split("|")
        # cells[0] empty, 1 ID, ... span is the line-span column
        # header: ID | pointer | source | namespace | path | span | mode | anchor
        # split keeps leading empty
        p("J05 cells " + str(len(cells)) + " spancell=" + cells[6].strip())
        cells[6] = " 20 "
        lines[i] = "|".join(cells)
        break
(fix/"claim-excerpt-map.md").write_text("\n".join(lines) + "\n")
for name, fn in (("bible", bible), ("map", mapa), ("support", support)):
    rc, hits = fn(fix)
    p(f"r99 {name} EXIT {rc}")
    for h in hits:
        if "J05" in h or h.startswith("RESULT") or h.startswith("CLEAN") or h.startswith("OBLIGATIONS"):
            p("  "+h)
rc, hits, _ = freeze_mirror("r4", lambda f: None)
# redo with mutation inside mirror
def span_mut(f):
    path = f/"claim-excerpt-map.md"
    lines = path.read_text().splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| J05 |"):
            cells = line.split("|")
            cells[6] = " 20 "
            lines[i] = "|".join(cells)
    path.write_text("\n".join(lines)+"\n")
rc, hits, _ = freeze_mirror("r4b", span_mut)
p(f"r98 freeze EXIT {rc}")
for h in hits: p("  "+h[:240])

# Row 5 source id
p("== ROW 5 source-id ==")
fix = copy_r99("r5-r99")
set_source(fix, "clerk-lapse-recorded", "clerk-filing-note")
for name, fn in (("bible", bible), ("support", support), ("map", mapa)):
    rc, hits = fn(fix)
    p(f"r99 {name} EXIT {rc}")
    for h in hits:
        if h.startswith(("FINDING", "RESULT", "CLEAN", "SOURCE-SUPPORT", "OBLIGATIONS")):
            p("  "+h)
rc, hits = mapa(copy_r98("r5-r98-tmp"))  # placeholder overwritten
def src_mut(f):
    set_source(f, "clerk-filing-open", "aru-acknowledgment-note")
fix = copy_r98("r5-r98")
src_mut(fix)
rc, hits = mapa(fix)
p(f"r98 map EXIT {rc}")
for h in hits:
    if h.startswith(("FINDING", "RESULT")): p("  "+h)
rc, hits, _ = freeze_mirror("r5", src_mut)
p(f"r98 freeze EXIT {rc}")
for h in hits: p("  "+h[:220])

# Row 6 prose
p("== ROW 6 prose wording ==")
phrase = "depends on both ninth-bell entries"
repl = "follows both ninth-bell entries"

def prose_coherent(f):
    for name in ("fictional-excerpts.md", "claim-excerpt-map.md"):
        path = f/name
        text = path.read_text()
        if phrase not in text:
            raise SystemExit(f"phrase missing in {name}")
        path.write_text(text.replace(phrase, repl))

# baseline tool
base_tool = subprocess.run(["git","show","4265df5:corpus/tools/dependency_freeze.py"], cwd=ROOT, capture_output=True, check=True).stdout
base_c = subprocess.run(["git","show","4265df5:corpus/tools/dependency-freeze-contract.json"], cwd=ROOT, capture_output=True, check=True).stdout
m = SCR/"r6-before"
(m/"corpus/tools").mkdir(parents=True)
(m/"corpus/tools/dependency_freeze.py").write_bytes(base_tool)
(m/"corpus/tools/dependency-freeze-contract.json").write_bytes(base_c)
shutil.copytree(ROOT/"corpus/fixtures/r98-clerk-filing", m/"corpus/fixtures/r98-clerk-filing")
prose_coherent(m/"corpus/fixtures/r98-clerk-filing")
rc, so, se = run(["python3", str(m/"corpus/tools/dependency_freeze.py"), str(m/"corpus/fixtures/r98-clerk-filing")], cwd=m)
p(f"baseline coherent EXIT {rc}")
for h in tail_hits(so): p("  "+h)
rc, hits, fix = freeze_mirror("r6-after", prose_coherent)
p(f"delivered coherent EXIT {rc}")
for h in hits: p("  "+h[:300])
for name, fn in (("bible", bible), ("support", support), ("map", mapa)):
    rc, hits = fn(fix)
    p(f"coherent {name} EXIT {rc} { [h for h in hits if h.startswith(('RESULT','CLEAN','OBLIGATIONS','SOURCE-SUPPORT'))] }")

narr_old = "depends on both (`aru-ninth-bell` and `evin-ninth-bell`)"
narr_new = "is recorded after both (`aru-ninth-bell` and `evin-ninth-bell`)"
def narr(f):
    path = f/"claim-excerpt-map.md"
    text = path.read_text()
    if narr_old not in text:
        raise SystemExit("narrative phrase missing")
    path.write_text(text.replace(narr_old, narr_new, 1))
rc, hits, fix = freeze_mirror("r6-narr", narr)
p(f"narrative freeze EXIT {rc}")
for h in hits: p("  "+h[:240])
for name, fn in (("bible", bible), ("support", support), ("map", mapa)):
    rc, hits = fn(fix)
    p(f"narr {name} EXIT {rc}")

def excerpt_only(f):
    path = f/"fictional-excerpts.md"
    text = path.read_text()
    path.write_text(text.replace(phrase, repl, 1))
fix = copy_r98("r6-excerpt-only")
excerpt_only(fix)
rc, hits = support(fix)
p(f"excerpt-only support EXIT {rc}")
for h in hits:
    if "J14" in h or h.startswith("RESULT"): p("  "+h)

# Row 7 consistent regen
p("== ROW 7 consistent regen ==")
fix = copy_r99("r7-r99")
delete_event(fix, "clerk-lapse-recorded")
text = (fix/"claim-excerpt-map.md").read_text()
lines = [ln for ln in text.splitlines() if not ln.startswith("| J21 |")]
text = "\n".join(lines) + "\n"
text = text.replace(
    "**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.",
    "**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.",
)
(fix/"claim-excerpt-map.md").write_text(text)
for name, fn in (("bible", bible), ("support", support), ("map", mapa)):
    rc, hits = fn(fix)
    p(f"r99 regen {name} EXIT {rc}")
    for h in hits:
        if h.startswith(("RESULT","CLEAN","OBLIGATIONS","SOURCE-SUPPORT","INVENTORY","FINDING")): p("  "+h)

def regen98(f):
    delete_event(f, "clerk-filing-open")
    text = (f/"claim-excerpt-map.md").read_text()
    lines = [ln for ln in text.splitlines() if not ln.startswith("| J20 |")]
    text = "\n".join(lines)+"\n"
    text = text.replace(
        "**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.",
        "**Expected inventory:** 19 JSON facts; 2 editorial rows; 21 total mapped rows; 17 distinct excerpt anchors.",
    )
    (f/"claim-excerpt-map.md").write_text(text)
rc, hits, fix = freeze_mirror("r7", regen98)
p(f"r98 regen freeze EXIT {rc}")
for h in hits: p("  "+h)
for name, fn in (("bible", bible), ("support", support), ("map", mapa)):
    rc, hits = fn(fix)
    p(f"r98 regen {name} EXIT {rc}")
    for h in hits:
        if h.startswith(("RESULT","CLEAN","OBLIGATIONS","SOURCE-SUPPORT","FINDING")): p("  "+h)

# Row 8
p("== ROW 8 checker pin ==")
checker = (ROOT/"corpus/fixtures/check_bible.py").read_bytes()
p("checker " + hashlib.sha256(checker).hexdigest())
contract = json.loads((ROOT/"corpus/tools/boundary-doc-contract.json").read_text())
pin = contract.get("checker", {}).get("sha256") if isinstance(contract.get("checker"), dict) else None
if pin is None:
    # search
    blob = json.dumps(contract)
    p("pin_present " + ("ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421" in blob))
else:
    p("pin " + pin + " match " + str(pin == hashlib.sha256(checker).hexdigest()))
rc, so, se = run(["python3", str(ROOT/"corpus/tools/boundary_doc_check.py")])
p(f"boundary EXIT {rc}")
for h in tail_hits(so):
    if "CERTIFIED" in h or h.startswith("FINDING"): p("  "+h)
drift = SCR/"check_bible-drift.py"
drift.write_bytes(checker + b"\n# v75 drift\n")
rc, so, se = run(["python3", str(ROOT/"corpus/tools/boundary_doc_check.py"), "--checker", str(drift)])
p(f"drift EXIT {rc}")
for h in tail_hits(so):
    if h.startswith("FINDING") or "CERTIFICATION" in h: p("  "+h)

# Row 9
p("== ROW 9 check_bible catches ==")
probes = []
fix = copy_r99("r9-unknown-event")
set_dep(fix, "clerk-lapse-recorded", ["no-such-event-id"])
probes.append(("unknown-event", fix))
fix = copy_r99("r9-dangling")
data = json.loads((fix/"timeline.json").read_text())
for rec in data:
    if rec["id"] == "clerk-lapse-recorded":
        rec["entity_id"] = "no-such-entity"
(fix/"timeline.json").write_text(json.dumps(data, indent=2)+"\n")
probes.append(("dangling-entity", fix))
fix = copy_r99("r9-unknown-source")
set_source(fix, "clerk-lapse-recorded", "no-such-source")
probes.append(("unknown-source", fix))
fix = copy_r99("r9-missing-key")
data = json.loads((fix/"timeline.json").read_text())
for rec in data:
    if rec["id"] == "clerk-lapse-recorded":
        rec.pop("depends_on", None)
(fix/"timeline.json").write_text(json.dumps(data, indent=2)+"\n")
probes.append(("missing-key", fix))
fix = copy_r99("r9-self")
set_dep(fix, "clerk-lapse-recorded", ["clerk-lapse-recorded"])
probes.append(("self-dep", fix))
fix = copy_r99("r9-repeat")
set_dep(fix, "clerk-lapse-recorded", ["clerk-filing-open", "clerk-filing-open"])
probes.append(("repeat", fix))
fix = copy_r99("r9-inversion")
data = json.loads((fix/"timeline.json").read_text())
for rec in data:
    if rec["id"] == "clerk-lapse-recorded":
        rec["tick"] = 14
(fix/"timeline.json").write_text(json.dumps(data, indent=2)+"\n")
probes.append(("inversion", fix))
fix = copy_r99("r9-delete-pred")
delete_event(fix, "clerk-filing-open")
probes.append(("delete-pred", fix))
for name, fix in probes:
    rc, hits = bible(fix)
    viol = [h for h in (hits if hits else [])]
    # bible() only keeps VIOLATION-starting and CLEAN. Good.
    p(f"{name} EXIT {rc} {viol}")

# line spot-checks for scope note
p("== scope-note line spot ==")
fix = ROOT/"corpus/fixtures/r99-window-lapse"
ex = (fix/"fictional-excerpts.md").read_text().splitlines()
p(f"excerpt[70]={ex[69]!r}")
p(f"excerpt[74]={ex[73]!r}")
src = (fix/"sources.json").read_text().splitlines()
p(f"sources[45]={src[44]!r}")
p(f"sources[46]={src[45]!r}")
tl = (fix/"timeline.json").read_text().splitlines()
p(f"timeline[77]={tl[76]!r}")
p(f"timeline[84]={tl[83]!r}")
mp = (fix/"claim-excerpt-map.md").read_text().splitlines()
p(f"map[5]={mp[4]!r}")
p(f"map[42]={mp[41][:80]!r}")

(ROOT/".ufo/waves/round-99/seats/V75-scratch/row-replay.txt").write_text("\n".join(LOG)+"\n")
p("WROTE row-replay")
