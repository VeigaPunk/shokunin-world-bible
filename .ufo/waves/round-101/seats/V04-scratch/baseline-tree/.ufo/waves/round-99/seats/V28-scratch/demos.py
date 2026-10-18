#!/usr/bin/env python3
"""V28 own demos. Frozen copies only. Does not touch lane producer files."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCR = LANE / ".ufo/waves/round-99/seats/V28-scratch"
FROZEN_TOOL = SCR / "frozen-r99/dependency_freeze.py"
FROZEN_CONTRACT = SCR / "frozen-r99/dependency-freeze-contract.json"
BASE_TOOL = SCR / "baseline-r98/dependency_freeze.py"
BASE_CONTRACT = SCR / "baseline-r98/dependency-freeze-contract.json"
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
SENTENCE = (
    "Their tick-10 decision depends on both ninth-bell entries: "
    "Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court."
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def make_root(name, tool, contract, fixtures):
    root = SCR / "demos" / name
    if root.exists():
        shutil.rmtree(root)
    (root / "corpus/tools").mkdir(parents=True)
    (root / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(tool, root / "corpus/tools/dependency_freeze.py")
    shutil.copy2(contract, root / "corpus/tools/dependency-freeze-contract.json")
    for fixture in fixtures:
        shutil.copytree(LANE / "corpus/fixtures" / fixture, root / "corpus/fixtures" / fixture)
    return root


def verify(root, fixture):
    tool = root / "corpus/tools/dependency_freeze.py"
    target = root / "corpus/fixtures" / fixture
    return run([sys.executable, str(tool), str(target)], root)


def show(label, code, stdout, stderr):
    print(f"===== {label} EXIT={code} =====")
    print(stdout.rstrip())
    if stderr.strip():
        print("--- stderr ---")
        print(stderr.rstrip())
    print()


def main():
    print("FROZEN_TOOL", sha(FROZEN_TOOL))
    print("FROZEN_CONTRACT", sha(FROZEN_CONTRACT))
    print("BASE_TOOL", sha(BASE_TOOL))
    print("BASE_CONTRACT", sha(BASE_CONTRACT))
    contract = json.loads(FROZEN_CONTRACT.read_text(encoding="utf-8"))
    base = json.loads(BASE_CONTRACT.read_text(encoding="utf-8"))
    print("schema", contract.get("schema_version"), "payload", contract.get("payload_schema_version"))
    expected = contract["self_test"]["expected"]
    base_expected = base["self_test"]["expected"]
    print("expected", len(expected), "added", sorted(set(expected) - set(base_expected)),
          "removed", sorted(set(base_expected) - set(expected)))
    changed = []
    for name in sorted(set(expected) & set(base_expected)):
        if expected[name] != base_expected[name]:
            changed.append(name)
    print("inherited expected changed", changed)
    print("markdown_tamper", json.dumps(expected.get("markdown_tamper"), sort_keys=True))
    for name in CHAIN:
        pin = contract["pins"][name]
        files = sorted(pin["files"])
        print(f"PIN {name} n={len(files)} schema={pin.get('payload_schema_version')} digest={pin['content_sha256']}")
        if files != sorted(TEN):
            print("  FILESET", files)
        old = base["pins"][name]
        json_same = all(pin["files"][f] == old["files"][f] for f in old["files"])
        inv_same = pin["events"] == old["events"] and pin["relations"] == old["relations"] and pin["counts"] == old["counts"]
        print(f"  json_digests_same={json_same} inventory_same={inv_same}")

    # after control + chain
    root = make_root("after-chain", FROZEN_TOOL, FROZEN_CONTRACT, CHAIN)
    for name in CHAIN:
        code, stdout, stderr = verify(root, name)
        show(f"AFTER chain {name}", code, stdout, stderr)

    # after: dependency sentence replaced (S1's mutation, independent copy)
    root = make_root("after-wording", FROZEN_TOOL, FROZEN_CONTRACT, ["r94-paired-crossing"])
    excerpt = root / "corpus/fixtures/r94-paired-crossing/fictional-excerpts.md"
    text = excerpt.read_text(encoding="utf-8")
    assert text.count(SENTENCE) == 1, text.count(SENTENCE)
    excerpt.write_text(text.replace(SENTENCE, SENTENCE.replace("depends on both", "follows both", 1), 1), encoding="utf-8")
    assert "depends on both ninth-bell" not in excerpt.read_text(encoding="utf-8")
    assert "follows both ninth-bell" in excerpt.read_text(encoding="utf-8")
    code, stdout, stderr = verify(root, "r94-paired-crossing")
    show("AFTER wording-replace r94", code, stdout, stderr)
    for gate, argv in (
        ("support", [sys.executable, str(LANE / "corpus/tools/support_check.py"), str(root / "corpus/fixtures/r94-paired-crossing")]),
        ("map", [sys.executable, str(LANE / "corpus/tools/map_obligations.py"), str(root / "corpus/fixtures/r94-paired-crossing")]),
        ("bible", [sys.executable, str(LANE / "corpus/fixtures/check_bible.py"), str(root / "corpus/fixtures/r94-paired-crossing")]),
    ):
        code, stdout, stderr = run(argv, LANE)
        tail = "\n".join((stdout + stderr).strip().splitlines()[-4:])
        show(f"AFTER wording-replace gate {gate}", code, tail, "")

    # before non-anchor (baseline tool) and after non-anchor (frozen tool)
    heading = "# Authored in-world excerpts"
    for label, tool, contract in (
        ("BEFORE", BASE_TOOL, BASE_CONTRACT),
        ("AFTER", FROZEN_TOOL, FROZEN_CONTRACT),
    ):
        root = make_root(f"{label.lower()}-nonanchor", tool, contract, ["r94-paired-crossing"])
        excerpt = root / "corpus/fixtures/r94-paired-crossing/fictional-excerpts.md"
        text = excerpt.read_text(encoding="utf-8")
        assert text.count(heading) == 1, (label, text.count(heading))
        excerpt.write_text(text.replace(heading, heading + " (dependency wording left intact)", 1), encoding="utf-8")
        code, stdout, stderr = verify(root, "r94-paired-crossing")
        show(f"{label} nonanchor freeze", code, stdout, stderr)
        for gate, rel in (
            ("support", "corpus/tools/support_check.py"),
            ("map", "corpus/tools/map_obligations.py"),
            ("bible", "corpus/fixtures/check_bible.py"),
        ):
            code, stdout, stderr = run(
                [sys.executable, str(LANE / rel), str(root / "corpus/fixtures/r94-paired-crossing")],
                LANE,
            )
            tail = "\n".join((stdout + stderr).strip().splitlines()[-3:])
            show(f"{label} nonanchor {gate}", code, tail, "")

    # each pinned markdown file: trailing newline
    for name in TEN[5:]:
        root = make_root(f"nl-{name}", FROZEN_TOOL, FROZEN_CONTRACT, ["r98-clerk-filing"])
        path = root / "corpus/fixtures/r98-clerk-filing" / name
        path.write_bytes(path.read_bytes() + b"\n")
        code, stdout, stderr = verify(root, "r98-clerk-filing")
        show(f"AFTER newline {name}", code, stdout, stderr)

    # delete fictional-excerpts.md
    root = make_root("delete-excerpt", FROZEN_TOOL, FROZEN_CONTRACT, ["r98-clerk-filing"])
    (root / "corpus/fixtures/r98-clerk-filing/fictional-excerpts.md").unlink()
    code, stdout, stderr = verify(root, "r98-clerk-filing")
    show("AFTER delete fictional-excerpts.md", code, stdout, stderr)

    # unpinned extra file on r88
    root = make_root("extra-r88", FROZEN_TOOL, FROZEN_CONTRACT, ["r88-m3-maya-cluster"])
    extra = root / "corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md"
    assert extra.is_file()
    extra.write_bytes(extra.read_bytes() + b"\n")
    code, stdout, stderr = verify(root, "r88-m3-maya-cluster")
    show("AFTER r88 extra-file newline (not in the ten)", code, stdout, stderr)

    # self-test on frozen tool, isolated root with r95 only
    root = make_root("selftest", FROZEN_TOOL, FROZEN_CONTRACT, ["r95-crossing-aftermath"])
    tool = root / "corpus/tools/dependency_freeze.py"
    code, stdout, stderr = run([sys.executable, str(tool), "--self-test"], root)
    show("AFTER self-test", code, stdout, stderr)

    # confirm frozen copies unchanged and live hashes
    print("FROZEN_TOOL_STILL", sha(FROZEN_TOOL))
    print("FROZEN_CONTRACT_STILL", sha(FROZEN_CONTRACT))
    print("LIVE_TOOL", sha(LANE / "corpus/tools/dependency_freeze.py"))
    print("LIVE_CONTRACT", sha(LANE / "corpus/tools/dependency-freeze-contract.json"))
    print("DEMOS-DONE")


if __name__ == "__main__":
    main()
