#!/usr/bin/env python3
"""Scratch-only before/after probes. Does not write the live corpus."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCR = LANE / ".ufo/waves/round-99/seats/V31-scratch/mirrors"
BASE = "4265df5"


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def show(rev, rel, dest):
    data = subprocess.check_output(["git", "show", f"{rev}:{rel}"], cwd=LANE)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)


def make_root(name, tool_bytes, contract_bytes):
    root = SCR / name
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    (root / "corpus/fixtures").mkdir(parents=True)
    (root / "corpus/tools/dependency_freeze.py").write_bytes(tool_bytes)
    (root / "corpus/tools/dependency-freeze-contract.json").write_bytes(contract_bytes)
    return root


def copy_fixture(root, fixture_name):
    src = LANE / "corpus/fixtures" / fixture_name
    dest = root / "corpus/fixtures" / fixture_name
    shutil.copytree(src, dest)
    return dest


def freeze(root, fixture):
    tool = root / "corpus/tools/dependency_freeze.py"
    code, out, err = run([sys.executable, str(tool), str(fixture)], root)
    return code, out, err


def main():
    if SCR.exists():
        shutil.rmtree(SCR)
    SCR.mkdir(parents=True)
    old_tool = subprocess.check_output(["git", "show", f"{BASE}:corpus/tools/dependency_freeze.py"], cwd=LANE)
    old_contract = subprocess.check_output(
        ["git", "show", f"{BASE}:corpus/tools/dependency-freeze-contract.json"], cwd=LANE
    )
    new_tool = (LANE / "corpus/tools/dependency_freeze.py").read_bytes()
    new_contract = (LANE / "corpus/tools/dependency-freeze-contract.json").read_bytes()
    print("old_tool", hashlib.sha256(old_tool).hexdigest())
    print("new_tool", hashlib.sha256(new_tool).hexdigest())
    print("old_contract", hashlib.sha256(old_contract).hexdigest())
    print("new_contract", hashlib.sha256(new_contract).hexdigest())

    # Before: README dependency-wording removal is invisible to the r98 freeze.
    root = make_root("before-readme", old_tool, old_contract)
    fix = copy_fixture(root, "r98-clerk-filing")
    readme = fix / "README.md"
    text = readme.read_text(encoding="utf-8")
    needle = "explicitly dependent on"
    if needle not in text:
        print("BEFORE-NEEDLE-MISSING")
    else:
        readme.write_text(text.replace(needle, "ordered after", 1), encoding="utf-8")
    code, out, err = freeze(root, fix)
    print("BEFORE-README-WORDING-REMOVAL exit", code)
    print(out.strip())
    if err.strip():
        print("stderr", err.strip())

    # After: same edit, delivered tool+contract.
    root = make_root("after-readme", new_tool, new_contract)
    fix = copy_fixture(root, "r98-clerk-filing")
    readme = fix / "README.md"
    readme.write_text(
        readme.read_text(encoding="utf-8").replace("explicitly dependent on", "ordered after", 1),
        encoding="utf-8",
    )
    code, out, err = freeze(root, fix)
    print("AFTER-README-WORDING-REMOVAL exit", code)
    print(out.strip())
    if err.strip():
        print("stderr", err.strip())

    # Excerpt dependency-wording removal that is NOT an anchor (scope sentence),
    # plus the anchor-bearing sentence removed and the map anchor regenerated.
    root = make_root("before-excerpt-scope", old_tool, old_contract)
    fix = copy_fixture(root, "r98-clerk-filing")
    excerpt = fix / "fictional-excerpts.md"
    scope_needle = "the crossing-scoped agreement above is unchanged"
    excerpt.write_text(
        excerpt.read_text(encoding="utf-8").replace(scope_needle, "the agreement above is unchanged", 1),
        encoding="utf-8",
    )
    code, out, err = freeze(root, fix)
    print("BEFORE-EXCERPT-SCOPE-WORDING exit", code)
    print(out.strip().splitlines()[-3:])

    root = make_root("after-excerpt-scope", new_tool, new_contract)
    fix = copy_fixture(root, "r98-clerk-filing")
    excerpt = fix / "fictional-excerpts.md"
    excerpt.write_text(
        excerpt.read_text(encoding="utf-8").replace(scope_needle, "the agreement above is unchanged", 1),
        encoding="utf-8",
    )
    code, out, err = freeze(root, fix)
    print("AFTER-EXCERPT-SCOPE-WORDING exit", code)
    print(out.strip())

    # Other gates on the after-excerpt-scope fixture (live tools, scratch fixture path).
    for cmd in (
        [sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(fix)],
        [sys.executable, str(LANE / "corpus/tools/support_check.py"), str(fix)],
        [sys.executable, str(LANE / "corpus/tools/map_obligations.py"), str(fix)],
    ):
        code, out, err = run(cmd, LANE)
        last = [line for line in out.splitlines() if line.startswith("RESULT") or line.startswith("CLEAN")]
        print("OTHER-GATE", Path(cmd[1]).name, "exit", code, last[-1] if last else out.strip().splitlines()[-1:])

    # Anchor-bearing dependency sentence removed, map anchor regenerated so lexical gates stay green.
    root = make_root("before-anchor-regen", old_tool, old_contract)
    fix = copy_fixture(root, "r98-clerk-filing")
    excerpt = (fix / "fictional-excerpts.md").read_text(encoding="utf-8")
    old_anchor = "Their tick-10 decision depends on both ninth-bell entries"
    new_anchor = "Their tick-10 decision follows both ninth-bell entries"
    if old_anchor not in excerpt:
        print("ANCHOR-NEEDLE-MISSING")
    (fix / "fictional-excerpts.md").write_text(excerpt.replace(old_anchor, new_anchor, 1), encoding="utf-8")
    map_text = (fix / "claim-excerpt-map.md").read_text(encoding="utf-8")
    (fix / "claim-excerpt-map.md").write_text(map_text.replace(old_anchor, new_anchor), encoding="utf-8")
    code, out, err = freeze(root, fix)
    print("BEFORE-ANCHOR-REGEN exit", code)
    print(out.strip().splitlines()[-2:])
    code, out, err = run([sys.executable, str(LANE / "corpus/tools/support_check.py"), str(fix)], LANE)
    last = [line for line in out.splitlines() if line.startswith("RESULT")]
    print("BEFORE-ANCHOR-REGEN support_check exit", code, last[-1] if last else "NO-RESULT")

    root = make_root("after-anchor-regen", new_tool, new_contract)
    fix = copy_fixture(root, "r98-clerk-filing")
    (fix / "fictional-excerpts.md").write_text(
        (fix / "fictional-excerpts.md").read_text(encoding="utf-8").replace(old_anchor, new_anchor, 1),
        encoding="utf-8",
    )
    (fix / "claim-excerpt-map.md").write_text(
        (fix / "claim-excerpt-map.md").read_text(encoding="utf-8").replace(old_anchor, new_anchor),
        encoding="utf-8",
    )
    code, out, err = freeze(root, fix)
    print("AFTER-ANCHOR-REGEN exit", code)
    print(out.strip())
    code, out, err = run([sys.executable, str(LANE / "corpus/tools/support_check.py"), str(fix)], LANE)
    last = [line for line in out.splitlines() if line.startswith("RESULT")]
    print("AFTER-ANCHOR-REGEN support_check exit", code, last[-1] if last else "NO-RESULT")
    code, out, err = run([sys.executable, str(LANE / "corpus/tools/map_obligations.py"), str(fix)], LANE)
    last = [line for line in out.splitlines() if line.startswith("RESULT") or line.startswith("OBLIGATIONS")]
    print("AFTER-ANCHOR-REGEN map", code, last)

    # Each pinned file, one-byte append, delivered tool.
    pinned = [
        "entities.json", "relations.json", "timeline.json", "sources.json", "contradictions.json",
        "README.md", "claim-excerpt-map.md", "fictional-excerpts.md", "inspiration-note.md", "source-excerpt.md",
    ]
    for name in pinned:
        root = make_root(f"tamper-{name}", new_tool, new_contract)
        fix = copy_fixture(root, "r98-clerk-filing")
        target = fix / name
        target.write_bytes(target.read_bytes() + b"\n")
        code, out, err = freeze(root, fix)
        named = name in out
        finding = next((line for line in out.splitlines() if line.startswith("FINDING")), "")
        print(f"TAMPER {name} exit={code} names_file={named} {finding}")

    # Semantic edge drop still exits 1, ahead of the digest.
    root = make_root("edge-drop", new_tool, new_contract)
    fix = copy_fixture(root, "r98-clerk-filing")
    timeline = json.loads((fix / "timeline.json").read_text(encoding="utf-8"))
    for record in timeline:
        if record.get("id") == "clerk-filing-open":
            record["depends_on"] = []
    (fix / "timeline.json").write_text(json.dumps(timeline, indent=2) + "\n", encoding="utf-8")
    code, out, err = freeze(root, fix)
    print("EDGE-DROP exit", code)
    print(out.strip())

    # Missing pinned markdown.
    root = make_root("missing-md", new_tool, new_contract)
    fix = copy_fixture(root, "r98-clerk-filing")
    (fix / "source-excerpt.md").unlink()
    code, out, err = freeze(root, fix)
    print("MISSING-MD exit", code)
    print(out.strip())

    # Foreign path copy of unmodified fixture.
    root = make_root("foreign", new_tool, new_contract)
    foreign = root / "foreign" / "r98-clerk-filing"
    shutil.copytree(LANE / "corpus/fixtures/r98-clerk-filing", foreign)
    code, out, err = freeze(root, foreign)
    print("FOREIGN exit", code)
    print(out.strip())

    print("MIRRORS-DONE")


if __name__ == "__main__":
    main()
