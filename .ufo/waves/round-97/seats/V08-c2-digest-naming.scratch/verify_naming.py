import hashlib, json, re, shutil, subprocess, sys
from pathlib import Path
root = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
sc = root/".ufo/waves/round-97/seats/V08-c2-digest-naming.scratch"
ws = sc/"ws"
tool = ws/"corpus/tools/dependency_freeze.py"
contract = json.loads((ws/"corpus/tools/dependency-freeze-contract.json").read_text())
pin = contract["pins"]["r95-crossing-aftermath"]
real = root/"corpus/fixtures/r95-crossing-aftermath"
mirror = ws/"corpus/fixtures/r95-crossing-aftermath"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def case(label, edits):
    shutil.rmtree(mirror); shutil.copytree(real, mirror)
    for fname, (a, b) in edits.items():
        p = mirror/fname
        t = p.read_text(); t2 = t.replace(a, b, 1); assert t2 != t, fname
        p.write_text(t2)
    r = subprocess.run([sys.executable, str(tool), str(mirror)], capture_output=True, text=True)
    out = r.stdout
    print(f"### {label}: exit={r.returncode}")
    line = [l for l in out.splitlines() if l.startswith("FINDING DIGEST-MISMATCH")]
    print(line[0])
    m = re.search(r"changed: (.*?); fixture bytes", line[0])
    entries = re.findall(r"(\S+\.json) \(sha256 ([0-9a-f]{64}) -> ([0-9a-f]{64})\)", m.group(1))
    named = sorted(n for n, _, _ in entries)
    expected_named = sorted(edits)
    print(f"named files: {named} | expected: {expected_named} | exact_match={named==expected_named}")
    for fname, before, after in entries:
        pin_h = pin["files"].get(fname)
        actual = sha(mirror/fname)
        print(f"  {fname}: before==pin_hash={before==pin_h} after==actual_file_hash={after==actual} (pin={pin_h[:12]}… actual={actual[:12]}…)")

case("T1 sources.json", {"sources.json": ("note", "Note")})
case("T2 timeline.json", {"timeline.json": ("south bell at Salt Court", "South bell at Salt Court")})
case("T3 sources+entities", {"sources.json": ("note", "Note"), "entities.json": ("north lantern", "North lantern")})
