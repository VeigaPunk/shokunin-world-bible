#!/usr/bin/env python3
"""V37 spec-conformance probes. Writes only under this scratch directory."""
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V37-scratch"
OUT = SCRATCH / "probe-out"
OUT.mkdir(parents=True, exist_ok=True)
BASE = "4265df5"
CHAIN = [
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
]
TEN = [
    "entities.json",
    "relations.json",
    "timeline.json",
    "sources.json",
    "contradictions.json",
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
]


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(cmd, cwd=LANE, timeout=180):
    result = subprocess.run(
        cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout,
    )
    return result.returncode, result.stdout, result.stderr


def write(name, text):
    (OUT / name).write_text(text, encoding="utf-8")
    return text


def section(title):
    print(f"\n===== {title} =====", flush=True)


def main():
    section("hashes")
    tool = LANE / "corpus/tools/dependency_freeze.py"
    contract = LANE / "corpus/tools/dependency-freeze-contract.json"
    print("HEAD", run(["git", "rev-parse", "HEAD"])[1].strip())
    print("tool", sha256(tool), tool.stat().st_size)
    print("contract", sha256(contract), contract.stat().st_size)
    c = json.loads(contract.read_text(encoding="utf-8"))
    print("schema", c.get("schema_version"), "payload", c.get("payload_schema_version"))
    print("pinned_files", c.get("pinned_files"))
    exp = c["self_test"]["expected"]
    print("self_test", len(exp), sorted(exp))
    print("markdown_tamper", json.dumps(exp.get("markdown_tamper")))
    base_exp = json.loads(run(["git", "show", f"{BASE}:corpus/tools/dependency-freeze-contract.json"])[1])
    base_keys = set(base_exp["self_test"]["expected"])
    print("inherited_case_keys_equal", base_keys <= set(exp) and base_keys == set(exp) - {"markdown_tamper"})
    changed = []
    for key in sorted(base_keys):
        if base_exp["self_test"]["expected"][key] != exp.get(key):
            changed.append(key)
    print("inherited_expectation_values_changed", changed)

    section("chain-verify")
    for name in CHAIN:
        rc, out, err = run(["python3", "corpus/tools/dependency_freeze.py", f"corpus/fixtures/{name}"])
        print(f"--- {name} rc={rc}")
        print(out.strip())
        if err.strip():
            print("STDERR", err.strip())
        pin = c["pins"][name]
        print("pin_nfiles", len(pin.get("files", {})), "psv", pin.get("payload_schema_version"),
              "files", sorted(pin.get("files", {})))

    section("r99-unpinned")
    rc, out, err = run(["python3", "corpus/tools/dependency_freeze.py", "corpus/fixtures/r99-window-lapse"])
    print(f"rc={rc}")
    print(out.strip())
    if err.strip():
        print("STDERR", err.strip())

    section("self-test")
    rc, out, err = run(["python3", "corpus/tools/dependency_freeze.py", "--self-test"], timeout=240)
    print(f"rc={rc}")
    print(out)
    if err.strip():
        print("STDERR", err)
    write("self-test.txt", f"rc={rc}\n{out}\nSTDERR:\n{err}")

    section("per-file-tamper")
    mirror = SCRATCH / "tamper-mirror"
    if mirror.exists():
        shutil.rmtree(mirror)
    (mirror / "corpus/tools").mkdir(parents=True)
    (mirror / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(tool, mirror / "corpus/tools/dependency_freeze.py")
    shutil.copy2(contract, mirror / "corpus/tools/dependency-freeze-contract.json")
    # gitdir so --freeze revision matches, but tamper probes only verify
    (mirror / ".git").write_text(f"gitdir: {LANE / '.git'}\n", encoding="utf-8")
    base_fix = mirror / "corpus/fixtures/r95-crossing-aftermath"
    shutil.copytree(LANE / "corpus/fixtures/r95-crossing-aftermath", base_fix)
    tool_m = mirror / "corpus/tools/dependency_freeze.py"
    clean_rc, clean_out, clean_err = run([sys.executable, str(tool_m), str(base_fix)], cwd=mirror)
    print("mirror-clean", clean_rc)
    print(clean_out.strip())
    if clean_err.strip():
        print("STDERR", clean_err.strip())
    for name in TEN:
        fix = mirror / "corpus/fixtures" / f"tamper-{name}"
        if fix.exists():
            shutil.rmtree(fix)
        shutil.copytree(base_fix, fix)
        target = fix / name
        target.write_bytes(target.read_bytes() + b"\n")
        rc, out, err = run([sys.executable, str(tool_m), str(fix)], cwd=mirror)
        named = name in out
        print(f"TAMPER {name} rc={rc} names_file={named}")
        print(out.strip())
        if err.strip():
            print("STDERR", err.strip())

    section("prose-before-after")
    phrase = b"depends on"
    excerpt_live = (LANE / "corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md").read_bytes()
    print("phrase_count", excerpt_live.count(phrase))
    # after: new tool, excerpt phrase removed
    fix = mirror / "corpus/fixtures/prose-removed"
    if fix.exists():
        shutil.rmtree(fix)
    shutil.copytree(base_fix, fix)
    ex = fix / "fictional-excerpts.md"
    raw = ex.read_bytes()
    if phrase not in raw:
        print("PHRASE MISSING in r95 excerpt")
    else:
        ex.write_bytes(raw.replace(phrase, b"follows", 1))
    rc, out, err = run([sys.executable, str(tool_m), str(fix)], cwd=mirror)
    print("AFTER freeze rc", rc)
    print(out.strip())
    # other gates on the scratch copy (live tools, any directory)
    for gate in [
        ["python3", "corpus/fixtures/check_bible.py", str(fix)],
        ["python3", "corpus/tools/support_check.py", str(fix)],
        ["python3", "corpus/tools/map_obligations.py", str(fix)],
        ["python3", "corpus/tools/boundary_doc_check.py", str(fix)],
        ["python3", "corpus/tools/discriminate_check.py", str(fix)],
    ]:
        rc, out, err = run(gate, timeout=60)
        tail = "\n".join((out + err).strip().splitlines()[-8:])
        print(f"AFTER-GATE {' '.join(gate[1:2])} rc={rc}")
        print(tail)
    # non-anchor markdown: editorial sentence in the map
    fix2 = mirror / "corpus/fixtures/prose-map-editorial"
    if fix2.exists():
        shutil.rmtree(fix2)
    shutil.copytree(base_fix, fix2)
    mp = fix2 / "claim-excerpt-map.md"
    text = mp.read_text(encoding="utf-8")
    old = "depends on both"
    print("editorial_phrase_present", old in text)
    mp.write_text(text.replace(old, "is ordered after both", 1), encoding="utf-8")
    rc, out, err = run([sys.executable, str(tool_m), str(fix2)], cwd=mirror)
    print("AFTER map-editorial freeze rc", rc)
    print(out.strip())
    for gate in [
        ["python3", "corpus/fixtures/check_bible.py", str(fix2)],
        ["python3", "corpus/tools/support_check.py", str(fix2)],
        ["python3", "corpus/tools/map_obligations.py", str(fix2)],
    ]:
        rc, gout, gerr = run(gate, timeout=60)
        tail = "\n".join((gout + gerr).strip().splitlines()[-6:])
        print(f"AFTER-EDITORIAL-GATE {gate[1]} rc={rc}")
        print(tail)

    # before: 4265df5 tool+contract
    before = SCRATCH / "before-mirror"
    if before.exists():
        shutil.rmtree(before)
    (before / "corpus/tools").mkdir(parents=True)
    (before / "corpus/fixtures").mkdir(parents=True)
    tool_b = before / "corpus/tools/dependency_freeze.py"
    con_b = before / "corpus/tools/dependency-freeze-contract.json"
    tool_b.write_bytes(run(["git", "show", f"{BASE}:corpus/tools/dependency_freeze.py"])[1].encode("utf-8"))
    # git show text mode may not be bytes-identical if encoding; use binary via check_output
    tool_b.write_bytes(subprocess.check_output(["git", "show", f"{BASE}:corpus/tools/dependency_freeze.py"], cwd=LANE))
    con_b.write_bytes(subprocess.check_output(["git", "show", f"{BASE}:corpus/tools/dependency-freeze-contract.json"], cwd=LANE))
    print("before-tool", sha256(tool_b))
    print("before-contract", sha256(con_b))
    bfix = before / "corpus/fixtures/r95-crossing-aftermath"
    shutil.copytree(LANE / "corpus/fixtures/r95-crossing-aftermath", bfix)
    rc, out, err = run([sys.executable, str(tool_b), str(bfix)], cwd=before)
    print("BEFORE clean rc", rc)
    print(out.strip())
    if err.strip():
        print("STDERR", err.strip())
    # prose removal on excerpt
    bex = before / "corpus/fixtures/prose-removed"
    shutil.copytree(bfix, bex)
    (bex / "fictional-excerpts.md").write_bytes(
        (bex / "fictional-excerpts.md").read_bytes().replace(phrase, b"follows", 1)
    )
    rc, out, err = run([sys.executable, str(tool_b), str(bex)], cwd=before)
    print("BEFORE excerpt-removal freeze rc", rc)
    print(out.strip())
    if err.strip():
        print("STDERR", err.strip())
    for gate in [
        ["python3", "corpus/fixtures/check_bible.py", str(bex)],
        ["python3", "corpus/tools/support_check.py", str(bex)],
        ["python3", "corpus/tools/map_obligations.py", str(bex)],
        ["python3", "corpus/tools/boundary_doc_check.py", str(bex)],
        ["python3", "corpus/tools/discriminate_check.py", str(bex)],
    ]:
        rc, gout, gerr = run(gate, timeout=60)
        tail = "\n".join((gout + gerr).strip().splitlines()[-6:])
        print(f"BEFORE-GATE {gate[1]} rc={rc}")
        print(tail)
    # editorial-only removal, old freeze
    bed = before / "corpus/fixtures/prose-map-editorial"
    shutil.copytree(bfix, bed)
    mp = bed / "claim-excerpt-map.md"
    mp.write_text(mp.read_text(encoding="utf-8").replace(old, "is ordered after both", 1), encoding="utf-8")
    rc, out, err = run([sys.executable, str(tool_b), str(bed)], cwd=before)
    print("BEFORE map-editorial freeze rc", rc)
    print(out.strip())
    for gate in [
        ["python3", "corpus/fixtures/check_bible.py", str(bed)],
        ["python3", "corpus/tools/support_check.py", str(bed)],
        ["python3", "corpus/tools/map_obligations.py", str(bed)],
    ]:
        rc, gout, gerr = run(gate, timeout=60)
        tail = "\n".join((gout + gerr).strip().splitlines()[-4:])
        print(f"BEFORE-EDITORIAL-GATE {gate[1]} rc={rc}")
        print(tail)
    # newline tamper of each markdown under old tool: should be invisible (exit 0)
    for name in ["README.md", "claim-excerpt-map.md", "fictional-excerpts.md", "inspiration-note.md", "source-excerpt.md"]:
        dest = before / "corpus/fixtures" / f"md-{name}"
        shutil.copytree(bfix, dest)
        p = dest / name
        p.write_bytes(p.read_bytes() + b"\n")
        rc, out, err = run([sys.executable, str(tool_b), str(dest)], cwd=before)
        print(f"BEFORE newline {name} rc={rc} out={out.strip().splitlines()[-1] if out.strip() else err.strip()[:200]}")

    section("refreeze")
    ref = SCRATCH / "refreeze-mirror"
    if ref.exists():
        shutil.rmtree(ref)
    (ref / "corpus/tools").mkdir(parents=True)
    (ref / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(tool, ref / "corpus/tools/dependency_freeze.py")
    # start from baseline contract (schema 1, five-file pins) so --freeze is the upgrade path
    (ref / "corpus/tools/dependency-freeze-contract.json").write_bytes(
        subprocess.check_output(["git", "show", f"{BASE}:corpus/tools/dependency-freeze-contract.json"], cwd=LANE)
    )
    # but the new tool's self-test is not what we run; freeze() reads contract and rewrites pins.
    # The new tool's validate_pin requires payload_schema_version 2. Old contract pins will fail
    # validate inside freeze() AFTER it builds a new pin and writes it. freeze() replaces the pin
    # then validate_pin on the NEW pin. Old other pins stay. That is fine.
    # However read_contract may validate all pins on load. Check by running.
    (ref / ".git").write_text(f"gitdir: {LANE / '.git'}\n", encoding="utf-8")
    for name in CHAIN:
        shutil.copytree(LANE / f"corpus/fixtures/{name}", ref / "corpus/fixtures" / name)
    tool_r = ref / "corpus/tools/dependency_freeze.py"
    for name in CHAIN:
        rc, out, err = run([sys.executable, str(tool_r), "--freeze", f"corpus/fixtures/{name}"], cwd=ref)
        print(f"FREEZE {name} rc={rc}")
        print(out.strip())
        if err.strip():
            print("STDERR", err.strip()[:500])
    new_c = json.loads((ref / "corpus/tools/dependency-freeze-contract.json").read_text(encoding="utf-8"))
    live = json.loads(contract.read_text(encoding="utf-8"))
    for name in CHAIN:
        a = new_c["pins"][name]
        b = live["pins"][name]
        keys = ["payload_schema_version", "pinned_files", "content_sha256", "files", "events", "relations", "counts", "fixture"]
        same = {k: a.get(k) == b.get(k) for k in keys}
        print(f"PIN-EQ {name} {same} rev_ref={a.get('revision')} rev_live={b.get('revision')}")
    print("ref schema", new_c.get("schema_version"), new_c.get("payload_schema_version"))

    section("scope-guard")
    outside = SCRATCH / "outside-target"
    outside.mkdir(exist_ok=True)
    rc, out, err = run([sys.executable, str(tool_r), "--freeze", str(outside)], cwd=ref)
    print(f"rc={rc}")
    print(out.strip())
    if err.strip():
        print("STDERR", err.strip()[:300])

    section("hash-end")
    print("tool", sha256(tool))
    print("contract", sha256(contract))


if __name__ == "__main__":
    main()
