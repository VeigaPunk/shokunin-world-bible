#!/usr/bin/env python3
"""V72 scratch probes. Never writes under corpus/ or live tools."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V72-scratch"
MIRRORS = SCRATCH / "mirrors"
MIRRORS.mkdir(parents=True, exist_ok=True)
PY = sys.executable
CHAIN = [
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
]
PINNED = [
    "contradictions.json",
    "entities.json",
    "relations.json",
    "sources.json",
    "timeline.json",
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
]


def run(argv, cwd=LANE):
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mirror_delivered(name):
    root = MIRRORS / name
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    (root / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(LANE / "corpus/tools/dependency_freeze.py", root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(
        LANE / "corpus/tools/dependency-freeze-contract.json",
        root / "corpus/tools/dependency-freeze-contract.json",
    )
    return root


def copy_fixture(root, fixture_name):
    dest = root / "corpus/fixtures" / fixture_name
    shutil.copytree(LANE / "corpus/fixtures" / fixture_name, dest)
    return dest


def tool_of(root):
    return root / "corpus/tools/dependency_freeze.py"


def finding_lines(stdout):
    return [line for line in stdout.splitlines() if line.startswith("FINDING ") or line.startswith("RESULT ") or line.startswith("FREEZE ") or line.startswith("DIGEST ") or line.startswith("FROZEN ") or line.startswith("MIGRATED ")]


print("=== HEAD ===")
code, out, err = run(["git", "rev-parse", "HEAD"])
print(out.strip(), "exit", code)

print("=== delivered pin shape ===")
contract = json.loads((LANE / "corpus/tools/dependency-freeze-contract.json").read_text())
print("schema_version", contract.get("schema_version"), "payload_schema_version", contract.get("payload_schema_version"))
print("revision", contract.get("revision"))
expected = contract["self_test"]["expected"]
print("self_test", len(expected), "markdown_tamper", expected.get("markdown_tamper"))
for name in CHAIN:
    pin = contract["pins"][name]
    files = pin.get("files", {})
    print(
        name,
        "payload", pin.get("payload_schema_version"),
        "pinned_files", pin.get("pinned_files"),
        "nfiles", len(files),
        "revision", pin.get("revision"),
        "counts", pin.get("counts"),
        "content", pin.get("content_sha256"),
    )
    missing = [n for n in PINNED if n not in files]
    extra = [n for n in files if n not in PINNED]
    print("  missing", missing, "extra", extra)

print("=== ten-file byte edits on r98 mirror (delivered tool) ===")
root = mirror_delivered("ten-file")
base = copy_fixture(root, "r98-clerk-filing")
# semantic-neutral JSON edits: a space inside a non-endpoint string, or trailing space on []
edits = {
    "contradictions.json": lambda raw: raw.replace(b"[]", b"[ ]", 1),
    "entities.json": lambda raw: raw.replace(b"north lantern", b"north  lantern", 1),
    "relations.json": lambda raw: raw.replace(b"shares_stewardship_of", b"shares_stewardship_of", 1) or raw,  # placeholder
    "sources.json": lambda raw: raw.replace(b"Courier", b"Courier", 1),
    "timeline.json": lambda raw: raw.replace(b"south bell", b"south  bell", 1),
    "README.md": lambda raw: raw + b"\n",
    "claim-excerpt-map.md": lambda raw: raw + b"\n",
    "fictional-excerpts.md": lambda raw: raw + b"\n",
    "inspiration-note.md": lambda raw: raw + b"\n",
    "source-excerpt.md": lambda raw: raw + b"\n",
}
# relations.json has no safe string I know yet; use whitespace after [ if pretty
rel = (base / "relations.json").read_bytes()
print("relations.json head", rel[:80])
src = (base / "sources.json").read_bytes()
print("sources.json head", src[:80])

def relation_edit(raw):
    return raw.replace(b"\n", b"\n ", 1)

def source_edit(raw):
    return raw.replace(b"Maren", b"Maren ", 1)

edits["relations.json"] = relation_edit
edits["sources.json"] = source_edit

saved = {name: (base / name).read_bytes() for name in PINNED}
for name in PINNED:
    for other, blob in saved.items():
        (base / other).write_bytes(blob)
    target = base / name
    target.write_bytes(edits[name](saved[name]))
    code, out, err = run([PY, str(tool_of(root)), str(base)])
    named = name in out
    print(f"EDIT {name}: exit={code} named={named}")
    for line in finding_lines(out):
        print("   ", line)
    if err.strip():
        print("   stderr", err.strip().splitlines()[:3])

print("=== prose removal before (4265df5 tool) vs after (delivered tool) ===")
base_tool = SCRATCH / "baseline-4265df5-dependency_freeze.py"
base_contract = SCRATCH / "baseline-4265df5-contract.json"
if not base_tool.exists():
    code, out, err = run(["git", "show", "4265df5:corpus/tools/dependency_freeze.py"])
    base_tool.write_text(out)
    code, out, err = run(["git", "show", "4265df5:corpus/tools/dependency-freeze-contract.json"])
    base_contract.write_text(out)
    print("extracted baseline tool bytes", base_tool.stat().st_size, "contract", base_contract.stat().st_size)

def make_old_mirror():
    root = MIRRORS / "before-4265"
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    shutil.copy2(base_tool, root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(base_contract, root / "corpus/tools/dependency-freeze-contract.json")
    copy_fixture(root, "r98-clerk-filing")
    return root

old = make_old_mirror()
excerpt = old / "corpus/fixtures/r98-clerk-filing/fictional-excerpts.md"
text = excerpt.read_text(encoding="utf-8")
needle = "depends on"
print("old excerpt contains depends-on", needle in text, "count", text.count(needle))
excerpt.write_text(text.replace(needle, "follows from", 1), encoding="utf-8")
print("--- old freeze ---")
code, out, err = run([PY, str(tool_of(old)), str(old / "corpus/fixtures/r98-clerk-filing")])
print("exit", code)
print(out)
print("stderr", err)
print("--- live gates on the mutated old-mirror fixture (path is outside live pins) ---")
mut = old / "corpus/fixtures/r98-clerk-filing"
for cmd in [
    [PY, str(LANE / "corpus/fixtures/check_bible.py"), str(mut)],
    [PY, str(LANE / "corpus/tools/support_check.py"), str(mut)],
    [PY, str(LANE / "corpus/tools/map_obligations.py"), str(mut)],
]:
    code, out, err = run(cmd)
    print("CMD", cmd[1].split("/")[-1], "exit", code)
    print("\n".join(out.splitlines()[:8]))
    if "FINDING" in out or "RESULT" in out or "missing" in out.lower() or "VIOLATION" in out:
        interesting = [ln for ln in out.splitlines() if any(k in ln for k in ("FINDING", "RESULT", "missing", "VIOLATION", "CLEAN", "OBLIGATIONS", "SOURCE-SUPPORT", "PASS J14", "FAIL"))]
        print("interesting:")
        for ln in interesting[:12]:
            print("  ", ln)

print("--- after: delivered tool, same prose replacement ---")
new = mirror_delivered("after-prose")
copy_fixture(new, "r98-clerk-filing")
excerpt = new / "corpus/fixtures/r98-clerk-filing/fictional-excerpts.md"
excerpt.write_text(excerpt.read_text(encoding="utf-8").replace("depends on", "follows from", 1), encoding="utf-8")
code, out, err = run([PY, str(tool_of(new)), str(new / "corpus/fixtures/r98-clerk-filing")])
print("exit", code)
print(out)
print("stderr", err)

print("=== non-anchor prose removal (README sentence only) before vs after ===")
old = make_old_mirror()
readme = (old / "corpus/fixtures/r98-clerk-filing/README.md").read_text(encoding="utf-8")
print("readme depends-on count", readme.lower().count("depend"))
# remove one non-excerpt sentence containing depend
old_readme = old / "corpus/fixtures/r98-clerk-filing/README.md"
old_readme.write_text(readme.replace("depends on", "is ordered after", 1), encoding="utf-8")
code, out, err = run([PY, str(tool_of(old)), str(old / "corpus/fixtures/r98-clerk-filing")])
print("old freeze on README depend-wording removal exit", code)
print(out)
code, out, err = run([PY, str(LANE / "corpus/tools/support_check.py"), str(old / "corpus/fixtures/r98-clerk-filing")])
print("support_check exit", code, "tail", [ln for ln in out.splitlines() if ln.startswith("RESULT") or ln.startswith("SOURCE-SUPPORT") or ln.startswith("FINDING")][:6])
code, out, err = run([PY, str(LANE / "corpus/fixtures/check_bible.py"), str(old / "corpus/fixtures/r98-clerk-filing")])
print("check_bible exit", code, out.strip().splitlines()[:2])
code, out, err = run([PY, str(LANE / "corpus/tools/map_obligations.py"), str(old / "corpus/fixtures/r98-clerk-filing")])
print("map exit", code, [ln for ln in out.splitlines() if ln.startswith("RESULT") or ln.startswith("OBLIGATIONS")][:4])

new = mirror_delivered("after-readme")
copy_fixture(new, "r98-clerk-filing")
rp = new / "corpus/fixtures/r98-clerk-filing/README.md"
rp.write_text(rp.read_text(encoding="utf-8").replace("depends on", "is ordered after", 1), encoding="utf-8")
code, out, err = run([PY, str(tool_of(new)), str(new / "corpus/fixtures/r98-clerk-filing")])
print("after README removal exit", code)
print(out)

print("=== re-freeze reproducibility (scratch mirror, pins deleted then --freeze) ===")
root = mirror_delivered("refreeze")
for name in CHAIN:
    copy_fixture(root, name)
contract_path = root / "corpus/tools/dependency-freeze-contract.json"
delivered = json.loads(contract_path.read_text())
saved_pins = delivered["pins"]
delivered["pins"] = {}
contract_path.write_text(json.dumps(delivered, indent=2, ensure_ascii=False) + "\n")
for name in CHAIN:
    code, out, err = run([PY, str(tool_of(root)), "--freeze", str(root / "corpus/fixtures" / name)])
    print(f"FREEZE {name} exit={code}")
    print(out)
    if err.strip():
        print("stderr", err.strip()[:400])
rewritten = json.loads(contract_path.read_text())
for name in CHAIN:
    got = rewritten["pins"].get(name)
    want = saved_pins[name]
    print(name, "pin_equal", got == want)
    if got != want and isinstance(got, dict) and isinstance(want, dict):
        gk, wk = set(got), set(want)
        print("  key diff", gk ^ wk)
        for key in sorted(gk & wk):
            if got[key] != want[key]:
                print("  field differs", key)

print("=== scope refuse does not rewrite live contract ===")
before = sha256_file(LANE / "corpus/tools/dependency-freeze-contract.json")
outside = SCRATCH / "not-a-fixture"
outside.mkdir(exist_ok=True)
code, out, err = run([PY, str(LANE / "corpus/tools/dependency_freeze.py"), "--freeze", str(outside)])
after = sha256_file(LANE / "corpus/tools/dependency-freeze-contract.json")
print("exit", code)
print(out)
print("contract_unchanged", before == after, before)

print("=== inherited JSON vs r98 and vs 4265df5 ===")
r99 = LANE / "corpus/fixtures/r99-window-lapse"
r98 = LANE / "corpus/fixtures/r98-clerk-filing"
for name in ["entities.json", "relations.json", "contradictions.json", "sources.json", "timeline.json"]:
    a = json.loads((r99 / name).read_text())
    b = json.loads((r98 / name).read_text())
    blob = subprocess.run(["git", "show", f"4265df5:corpus/fixtures/r98-clerk-filing/{name}"], cwd=LANE, capture_output=True, text=True)
    c = json.loads(blob.stdout)
    print(name, "r99==r98", a == b, "r98==4265df5", b == c, "r99_prefix_eq_r98", a[:len(b)] == b if isinstance(a, list) else a == b, "lens", len(a) if isinstance(a, list) else None, len(b) if isinstance(b, list) else None)

print("=== byte identity of untouched r99 files vs 4265df5 r98 ===")
for name in ["entities.json", "relations.json", "contradictions.json", "inspiration-note.md", "source-excerpt.md"]:
    blob = subprocess.run(["git", "show", f"4265df5:corpus/fixtures/r98-clerk-filing/{name}"], cwd=LANE, capture_output=True)
    now = (r99 / name).read_bytes()
    print(name, "byte_identical", now == blob.stdout, "now", len(now), "base", len(blob.stdout))

print("=== excerpt prefix ===")
base_ex = subprocess.run(["git", "show", "4265df5:corpus/fixtures/r98-clerk-filing/fictional-excerpts.md"], cwd=LANE, capture_output=True).stdout
now_ex = (r99 / "fictional-excerpts.md").read_bytes()
print("prefix", now_ex.startswith(base_ex), "base", len(base_ex), "now", len(now_ex), "next_bytes", now_ex[len(base_ex):len(base_ex)+20])

print("=== map row identity modulo namespace ===")
import re
def rows(text):
    out = {}
    for line in text.splitlines():
        if not line.startswith("| J"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 8 or not parts[0].startswith("J"):
            continue
        out[parts[0]] = parts
    return out
r98_map = (r98 / "claim-excerpt-map.md").read_text()
r99_map = (r99 / "claim-excerpt-map.md").read_text()
a, b = rows(r98_map), rows(r99_map)
print("r98 rows", sorted(a), "r99 rows", sorted(b))
changed = []
for key in sorted(set(a) & set(b)):
    left = a[key][:]
    right = b[key][:]
    # namespace column index 3
    left[3] = left[3].replace("r98-clerk-filing", "NS")
    right[3] = right[3].replace("r99-window-lapse", "NS")
    if left != right:
        changed.append((key, left, right))
print("changed_inherited", len(changed))
for item in changed:
    print(item[0], item[1], item[2])
print("new", sorted(set(b) - set(a)))

print("=== prose negation scan ===")
needles = ("resolution", "blame", "reconcil")
for name in PINNED:
    text = (r99 / name).read_text(encoding="utf-8", errors="replace")
    low = text.lower()
    if not any(n in low for n in needles):
        continue
    print("--", name)
    for i, line in enumerate(text.splitlines(), 1):
        if any(n in line.lower() for n in needles):
            print(f"  {i}: {line.strip()[:240]}")

print("=== event/source exact ===")
tl = json.loads((r99 / "timeline.json").read_text())
src = json.loads((r99 / "sources.json").read_text())
print(json.dumps(tl[-1], indent=2))
print(json.dumps(src[-1], indent=2))
print("PROBE_DONE")
