#!/usr/bin/env python3
"""S5 scratch replays. Never writes under corpus/."""
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/S5-scratch"
WORK = SCRATCH / "work"
LOG = SCRATCH / "replay-log.txt"
R99 = LANE / "corpus/fixtures/r99-window-lapse"
R98 = LANE / "corpus/fixtures/r98-clerk-filing"
R94 = LANE / "corpus/fixtures/r94-paired-crossing"

lines = []


def emit(text=""):
    lines.append(text)
    print(text, flush=True)


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd, cwd=LANE):
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def show(title, code, out, err):
    emit(f"--- {title} exit={code}")
    if out:
        emit(out.rstrip("\n"))
    if err:
        emit("STDERR:")
        emit(err.rstrip("\n"))


def gates(label, fixture):
    emit(f"===== GATES {label} {fixture}")
    for cmd in (
        ["python3", "corpus/fixtures/check_bible.py", str(fixture)],
        ["python3", "corpus/tools/support_check.py", str(fixture)],
        ["python3", "corpus/tools/map_obligations.py", str(fixture)],
    ):
        code, out, err = run(cmd)
        # Keep full check_bible (short). For the other two, keep inventory/finding/result lines plus exit.
        if "check_bible.py" in cmd[1]:
            show("check_bible", code, out, err)
        else:
            kept = []
            for line in (out or "").splitlines():
                if line.startswith((
                    "INVENTORY", "OBLIGATIONS", "FINDING", "FAIL", "RESULT",
                    "SOURCE-SUPPORT", "VALIDATED-ROWS", "FREEZE", "DIGEST",
                )) or "outside-span" in line or "anchor=not-found" in line or line.startswith("WARN"):
                    kept.append(line)
            show(cmd[1], code, "\n".join(kept), err)


def copy_fixture(src, dest):
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    return dest


def load_timeline(fixture):
    path = fixture / "timeline.json"
    return json.loads(path.read_text(encoding="utf-8")), path


def save_timeline(path, rows):
    path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def pin_snapshot():
    contract_path = LANE / "corpus/tools/dependency-freeze-contract.json"
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    emit(f"contract schema_version={contract.get('schema_version')} payload_schema_version={contract.get('payload_schema_version')}")
    emit(f"contract pinned_files={contract.get('pinned_files')}")
    emit(f"contract sha256={sha256_file(contract_path)}")
    for name, pin in contract.get("pins", {}).items():
        files = sorted((pin.get("files") or {}))
        emit(f"pin {name} nfiles={len(files)} payload={pin.get('payload_schema_version')} files={files}")
    tool = LANE / "corpus/tools/dependency_freeze.py"
    emit(f"freeze tool sha256={sha256_file(tool)} bytes={tool.stat().st_size}")
    s1 = list((LANE / ".ufo/waves/round-99/seats").glob("S1*.md"))
    emit(f"S1 reports={ [str(p.relative_to(LANE)) for p in s1] }")


def main():
    if WORK.exists():
        shutil.rmtree(WORK)
    WORK.mkdir(parents=True)
    emit("## snapshot")
    pin_snapshot()
    for rel in (
        "corpus/fixtures/check_bible.py",
        "corpus/tools/support_check.py",
        "corpus/tools/map_obligations.py",
        "corpus/tools/boundary_doc_check.py",
        "corpus/tools/boundary-doc-contract.json",
        "corpus/knowledge/r98-clerk-scope-note.md",
        "corpus/fixtures/r94-paired-crossing/fictional-excerpts.md",
        "corpus/fixtures/r94-paired-crossing/sources.json",
        "corpus/fixtures/r99-window-lapse/timeline.json",
        "corpus/fixtures/r99-window-lapse/sources.json",
        "corpus/fixtures/r99-window-lapse/fictional-excerpts.md",
        "corpus/fixtures/r99-window-lapse/entities.json",
        "corpus/fixtures/r99-window-lapse/relations.json",
        "corpus/fixtures/r99-window-lapse/claim-excerpt-map.md",
        "corpus/fixtures/r99-window-lapse/README.md",
    ):
        path = LANE / rel
        emit(f"exists {rel} {path.is_file()} {sha256_file(path) if path.is_file() else '-'}")
    code, out, err = run(["bash", "-lc", "ls -d corpus/fixtures/*/ | wc -l"])
    emit(f"census dirs exit={code} out={out.strip()} err={err.strip()}")
    code, out, err = run(["git", "rev-parse", "HEAD"])
    emit(f"HEAD {out.strip()}")
    code, out, err = run(["git", "rev-parse", "4265df5"])
    emit(f"baseline {out.strip()} exit={code}")

    emit("\n## control r99 live")
    gates("control-r99", R99)

    # --- M1 emptied depends_on ---
    m = copy_fixture(R99, WORK / "m1-empty-deps")
    rows, path = load_timeline(m)
    assert rows[-1]["id"] == "clerk-lapse-recorded"
    rows[-1]["depends_on"] = []
    save_timeline(path, rows)
    gates("m1-empty-deps", m)

    # --- M2 wrong-but-earlier ---
    m = copy_fixture(R99, WORK / "m2-wrong-earlier")
    rows, path = load_timeline(m)
    rows[-1]["depends_on"] = ["acknowledgment-aru-records"]
    save_timeline(path, rows)
    gates("m2-wrong-earlier", m)

    # --- M3 deleted terminal ---
    m = copy_fixture(R99, WORK / "m3-delete-terminal")
    rows, path = load_timeline(m)
    removed = rows.pop()
    assert removed["id"] == "clerk-lapse-recorded"
    save_timeline(path, rows)
    gates("m3-delete-terminal", m)

    # --- M4 span-break J05 17 -> 20 ---
    m = copy_fixture(R99, WORK / "m4-span-break")
    map_path = m / "claim-excerpt-map.md"
    text = map_path.read_text(encoding="utf-8")
    old = "| J05 | `entities.json#/4/first_appearance` (`chalk-stair`) | `crossing-minute` | `r99-window-lapse:crossing-minute` | `fictional-excerpts.md` | 17 | `verbatim` |"
    new = old.replace("| 17 |", "| 20 |")
    assert text.count(old) == 1
    map_path.write_text(text.replace(old, new), encoding="utf-8")
    gates("m4-span-break", m)

    # --- M5 source-id mutant ---
    m = copy_fixture(R99, WORK / "m5-source-id")
    rows, path = load_timeline(m)
    assert rows[-1]["source_id"] == "clerk-lapse-note"
    rows[-1]["source_id"] = "clerk-filing-note"
    save_timeline(path, rows)
    gates("m5-source-id", m)

    # --- M6 consistent regeneration: drop terminal event + J21 + restate inventory ---
    m = copy_fixture(R99, WORK / "m6-consistent-regen")
    rows, path = load_timeline(m)
    rows.pop()
    save_timeline(path, rows)
    map_path = m / "claim-excerpt-map.md"
    text = map_path.read_text(encoding="utf-8")
    inv = "**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors."
    inv2 = "**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors."
    assert text.count(inv) == 1
    text = text.replace(inv, inv2)
    j21 = [line for line in text.splitlines() if line.startswith("| J21 |")]
    assert len(j21) == 1, j21
    text = "\n".join(line for line in text.splitlines() if not line.startswith("| J21 |")) + "\n"
    map_path.write_text(text, encoding="utf-8")
    gates("m6-consistent-regen", m)

    # --- M7 prose: excerpt+anchor coherent wording removal ---
    needle = "depends on both ninth-bell entries"
    repl = "follows both ninth-bell entries"
    m = copy_fixture(R98, WORK / "m7-prose-coherent")
    for name in ("fictional-excerpts.md", "claim-excerpt-map.md"):
        path = m / name
        text = path.read_text(encoding="utf-8")
        count = text.count(needle)
        emit(f"m7 {name} needle count={count}")
        assert count >= 1
        path.write_text(text.replace(needle, repl), encoding="utf-8")
    gates("m7-prose-coherent-r98copy", m)

    # excerpt-only (anchor broken)
    m = copy_fixture(R98, WORK / "m7b-excerpt-only")
    path = m / "fictional-excerpts.md"
    text = path.read_text(encoding="utf-8")
    assert text.count(needle) == 1
    path.write_text(text.replace(needle, repl), encoding="utf-8")
    gates("m7b-excerpt-only", m)

    # narrative-only map prose, anchors untouched
    m = copy_fixture(R99, WORK / "m7c-narrative-only")
    path = m / "claim-excerpt-map.md"
    text = path.read_text(encoding="utf-8")
    narr = "depends on both (`aru-ninth-bell` and `evin-ninth-bell`)"
    narr2 = "is recorded after both (`aru-ninth-bell` and `evin-ninth-bell`)"
    emit(f"m7c narrative count={text.count(narr)}")
    assert text.count(narr) == 1
    path.write_text(text.replace(narr, narr2), encoding="utf-8")
    gates("m7c-narrative-only", m)

    # --- M8 checker byte drift ---
    emit("\n## boundary pin")
    code, out, err = run(["python3", "corpus/tools/boundary_doc_check.py"])
    show("boundary default", code, out, err)
    checker = LANE / "corpus/fixtures/check_bible.py"
    drifted = WORK / "check_bible-drift.py"
    drifted.write_bytes(checker.read_bytes() + b"\n# s5 drift probe\n")
    emit(f"live checker sha256={sha256_file(checker)}")
    emit(f"drift checker sha256={sha256_file(drifted)}")
    code, out, err = run(["python3", "corpus/tools/boundary_doc_check.py", "--checker", str(drifted)])
    show("boundary checker-drift", code, out, err)

    # --- M9 classes check_bible DOES catch ---
    probes = {
        "unknown-event": lambda rows: rows[-1].__setitem__("depends_on", ["no-such-event-id"]),
        "dangling-entity": lambda rows: rows[-1].__setitem__("entity_id", "no-such-entity"),
        "unknown-source": lambda rows: rows[-1].__setitem__("source_id", "no-such-source"),
        "drop-depends-key": lambda rows: rows[-1].pop("depends_on"),
        "self-dep": lambda rows: rows[-1].__setitem__("depends_on", ["clerk-lapse-recorded"]),
        "repeated-dep": lambda rows: rows[-1].__setitem__("depends_on", ["clerk-filing-open", "clerk-filing-open"]),
        "tick-inversion": lambda rows: rows[-1].__setitem__("tick", 14),
        "delete-predecessor": lambda rows: rows.pop(6),  # clerk-filing-open, index 6; lapse remains and dangles
    }
    for name, mutate in probes.items():
        m = copy_fixture(R99, WORK / f"m9-{name}")
        rows, path = load_timeline(m)
        mutate(rows)
        save_timeline(path, rows)
        code, out, err = run(["python3", "corpus/fixtures/check_bible.py", str(m)])
        show(f"m9-{name} check_bible", code, out, err)

    # --- freeze before/after on isolated mirrors ---
    emit("\n## freeze mirrors")
    base_tool = WORK / "baseline-tool.py"
    base_contract = WORK / "baseline-contract.json"
    code, out, err = run(["git", "show", "4265df5:corpus/tools/dependency_freeze.py"])
    assert code == 0, err
    base_tool.write_text(out, encoding="utf-8")
    code, out, err = run(["git", "show", "4265df5:corpus/tools/dependency-freeze-contract.json"])
    assert code == 0, err
    base_contract.write_text(out, encoding="utf-8")
    emit(f"baseline tool sha256={sha256_file(base_tool)} bytes={base_tool.stat().st_size}")
    emit(f"baseline contract sha256={sha256_file(base_contract)}")

    def make_mirror(name, tool_src, contract_src, fixture_src, fixture_name):
        root = WORK / name
        if root.exists():
            shutil.rmtree(root)
        (root / "corpus/tools").mkdir(parents=True)
        shutil.copy2(tool_src, root / "corpus/tools/dependency_freeze.py")
        shutil.copy2(contract_src, root / "corpus/tools/dependency-freeze-contract.json")
        shutil.copytree(fixture_src, root / "corpus/fixtures" / fixture_name)
        return root

    def freeze_verify(root, fixture_rel, title):
        tool = root / "corpus/tools/dependency_freeze.py"
        fixture = root / fixture_rel
        code, out, err = run(["python3", str(tool), str(fixture)], cwd=root)
        show(title, code, out, err)
        return code

    # historical: baseline tool, markdown tamper, JSON unchanged
    root = make_mirror("base-mirror", base_tool, base_contract, R98, "r98-clerk-filing")
    freeze_verify(root, "corpus/fixtures/r98-clerk-filing", "baseline-clean-r98")
    excerpt = root / "corpus/fixtures/r98-clerk-filing/fictional-excerpts.md"
    mapf = root / "corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md"
    excerpt.write_text(excerpt.read_text(encoding="utf-8").replace(needle, repl), encoding="utf-8")
    mapf.write_text(mapf.read_text(encoding="utf-8").replace(needle, repl), encoding="utf-8")
    freeze_verify(root, "corpus/fixtures/r98-clerk-filing", "baseline-after-prose-tamper")

    # delivered tool: freeze then tamper
    delivered_tool = LANE / "corpus/tools/dependency_freeze.py"
    delivered_contract = LANE / "corpus/tools/dependency-freeze-contract.json"
    root = make_mirror("deliv-mirror", delivered_tool, delivered_contract, R98, "r98-clerk-filing")
    tool = root / "corpus/tools/dependency_freeze.py"
    fixture = root / "corpus/fixtures/r98-clerk-filing"
    code, out, err = run(["python3", str(tool), "--freeze", str(fixture)], cwd=root)
    show("delivered --freeze r98 mirror", code, out, err)
    freeze_verify(root, "corpus/fixtures/r98-clerk-filing", "delivered-postfreeze-clean")
    excerpt = fixture / "fictional-excerpts.md"
    mapf = fixture / "claim-excerpt-map.md"
    excerpt.write_text(excerpt.read_text(encoding="utf-8").replace(needle, repl), encoding="utf-8")
    mapf.write_text(mapf.read_text(encoding="utf-8").replace(needle, repl), encoding="utf-8")
    freeze_verify(root, "corpus/fixtures/r98-clerk-filing", "delivered-after-prose-tamper")

    # narrative-only tamper after a fresh freeze
    root = make_mirror("deliv-narr", delivered_tool, delivered_contract, R99, "r99-window-lapse")
    tool = root / "corpus/tools/dependency_freeze.py"
    fixture = root / "corpus/fixtures/r99-window-lapse"
    code, out, err = run(["python3", str(tool), "--freeze", str(fixture)], cwd=root)
    show("delivered --freeze r99 mirror", code, out, err)
    narr_path = fixture / "claim-excerpt-map.md"
    text = narr_path.read_text(encoding="utf-8")
    narr = "depends on both (`aru-ninth-bell` and `evin-ninth-bell`)"
    narr2 = "is recorded after both (`aru-ninth-bell` and `evin-ninth-bell`)"
    assert text.count(narr) == 1
    narr_path.write_text(text.replace(narr, narr2), encoding="utf-8")
    freeze_verify(root, "corpus/fixtures/r99-window-lapse", "delivered-r99-narrative-tamper")

    # live verify of r98 (may be CONTRACT-INVALID until S1 re-freezes)
    code, out, err = run(["python3", "corpus/tools/dependency_freeze.py", "corpus/fixtures/r98-clerk-filing"])
    show("live freeze verify r98", code, out, err)
    code, out, err = run(["python3", "corpus/tools/dependency_freeze.py", "corpus/fixtures/r99-window-lapse"])
    show("live freeze verify r99", code, out, err)

    emit("\n## snapshot end")
    pin_snapshot()
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    emit(f"WROTE {LOG}")


if __name__ == "__main__":
    main()
