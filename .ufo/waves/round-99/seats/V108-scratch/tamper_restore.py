#!/usr/bin/env python3
"""Scratch-only tamper-then-restore for dependency_freeze. Does not touch the lane tree."""
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V108-scratch"
MIRROR = SCRATCH / "mirror"
PINNED = (
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
)
CHAIN = (
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
    "r99-window-lapse",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_files(root: Path):
    return sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file())


def run_verify(mirror: Path, fixture_name: str):
    tool = mirror / "corpus/tools/dependency_freeze.py"
    fixture = mirror / "corpus/fixtures" / fixture_name
    cmd = [sys.executable, str(tool), str(fixture)]
    print("CMD", " ".join(cmd))
    result = subprocess.run(cmd, cwd=mirror, capture_output=True, text=True)
    print("EXIT", result.returncode)
    print("STDOUT")
    print(result.stdout, end="" if result.stdout.endswith("\n") or not result.stdout else "\n")
    print("STDERR")
    print(result.stderr, end="" if result.stderr.endswith("\n") or not result.stderr else "\n")
    return result


def contract_sha(mirror: Path) -> str:
    return sha256(mirror / "corpus/tools/dependency-freeze-contract.json")


def main():
    live_tool = LANE / "corpus/tools/dependency_freeze.py"
    live_contract = LANE / "corpus/tools/dependency-freeze-contract.json"
    live_before = {
        "tool": sha256(live_tool),
        "contract": sha256(live_contract),
    }
    print("LIVE_BEFORE", live_before)

    if MIRROR.exists():
        shutil.rmtree(MIRROR)
    (MIRROR / "corpus/tools").mkdir(parents=True)
    (MIRROR / "corpus/fixtures").mkdir(parents=True)
    shutil.copy2(live_tool, MIRROR / "corpus/tools/dependency_freeze.py")
    shutil.copy2(live_contract, MIRROR / "corpus/tools/dependency-freeze-contract.json")
    copied = []
    for name in (*CHAIN, "r88-m3-maya-cluster"):
        src = LANE / "corpus/fixtures" / name
        if not src.is_dir():
            print("SKIP_MISSING_FIXTURE", name)
            continue
        shutil.copytree(src, MIRROR / "corpus/fixtures" / name)
        copied.append(name)
        present = [n for n in PINNED if (src / n).is_file()]
        print("COPIED", name, "pinned_present", len(present), "/", len(PINNED), "missing", [n for n in PINNED if n not in present])
    print("MIRROR", MIRROR)

    print("=== BASELINE ===")
    baseline = {}
    for name in copied:
        print("--- baseline", name)
        result = run_verify(MIRROR, name)
        baseline[name] = result.returncode
    print("BASELINE_EXITS", baseline)

    target = None
    for name in ("r98-clerk-filing", "r95-crossing-aftermath", "r94-paired-crossing", "r96-crossing-response", "r97-crossing-acknowledgment"):
        if baseline.get(name) == 0:
            target = name
            break
    if target is None:
        print("NO_CLEAN_DELIVERED_PIN")
        target = "r98-clerk-filing" if "r98-clerk-filing" in copied else copied[0]
        print("SCRATCH_FREEZE", target)
        tool = MIRROR / "corpus/tools/dependency_freeze.py"
        fixture = MIRROR / "corpus/fixtures" / target
        cmd = [sys.executable, str(tool), "--freeze", str(fixture)]
        print("CMD", " ".join(cmd))
        result = subprocess.run(cmd, cwd=MIRROR, capture_output=True, text=True)
        print("EXIT", result.returncode)
        print("STDOUT")
        print(result.stdout)
        print("STDERR")
        print(result.stderr)
        print("--- post-scratch-freeze")
        result = run_verify(MIRROR, target)
        if result.returncode != 0:
            print("SCRATCH_FREEZE_NOT_CLEAN")
            return 2

    fixture_dir = MIRROR / "corpus/fixtures" / target
    originals = {name: (fixture_dir / name).read_bytes() for name in PINNED}
    before_files = tree_files(MIRROR)
    pin_sha = contract_sha(MIRROR)
    print("TARGET", target)
    print("CONTRACT_SHA_BEFORE", pin_sha)

    def restore(name):
        path = fixture_dir / name
        path.write_bytes(originals[name])
        print("RESTORED", name, "bytes", len(originals[name]), "sha", hashlib.sha256(originals[name]).hexdigest())

    def tamper(name, extra: bytes):
        path = fixture_dir / name
        path.write_bytes(originals[name] + extra)
        print("TAMPERED", name, "extra", extra)

    failures = []

    def expect(label, result, exit_code, must_contain=(), must_not=()):
        ok = result.returncode == exit_code
        text = result.stdout + result.stderr
        for needle in must_contain:
            if needle not in text:
                ok = False
                print("MISSING", label, needle)
        for needle in must_not:
            if needle in text:
                ok = False
                print("UNEXPECTED", label, needle)
        print("CHECK", label, "ok" if ok else "FAIL")
        if not ok:
            failures.append(label)
        return ok

    print("=== CYCLE fictional-excerpts.md ===")
    tamper("fictional-excerpts.md", b"\nV108-TAMPER fictional-excerpts\n")
    result = run_verify(MIRROR, target)
    expect(
        "tamper-fictional",
        result,
        2,
        ("DIGEST-MISMATCH", "fictional-excerpts.md", "RESULT ERROR"),
        ("README.md (sha256", "claim-excerpt-map.md (sha256"),
    )
    restore("fictional-excerpts.md")
    result = run_verify(MIRROR, target)
    expect("restore-fictional", result, 0, ("RESULT PASS",), ("DIGEST-MISMATCH", "FINDING"))

    print("=== CYCLE README.md after prior restore ===")
    tamper("README.md", b"\nV108-TAMPER readme\n")
    result = run_verify(MIRROR, target)
    expect(
        "tamper-readme",
        result,
        2,
        ("DIGEST-MISMATCH", "README.md", "RESULT ERROR"),
        ("fictional-excerpts.md (sha256",),
    )
    restore("README.md")
    result = run_verify(MIRROR, target)
    expect("restore-readme", result, 0, ("RESULT PASS",), ("DIGEST-MISMATCH", "FINDING"))

    print("=== CYCLE two files, restore one, then the other ===")
    tamper("source-excerpt.md", b"\nV108-TAMPER source-excerpt\n")
    tamper("claim-excerpt-map.md", b"\nV108-TAMPER map\n")
    result = run_verify(MIRROR, target)
    expect(
        "tamper-two",
        result,
        2,
        ("DIGEST-MISMATCH", "source-excerpt.md", "claim-excerpt-map.md"),
        ("README.md (sha256", "fictional-excerpts.md (sha256"),
    )
    restore("source-excerpt.md")
    result = run_verify(MIRROR, target)
    expect(
        "restore-one-of-two",
        result,
        2,
        ("DIGEST-MISMATCH", "claim-excerpt-map.md"),
        ("source-excerpt.md (sha256",),
    )
    restore("claim-excerpt-map.md")
    result = run_verify(MIRROR, target)
    expect("restore-both", result, 0, ("RESULT PASS",), ("DIGEST-MISMATCH", "FINDING"))

    print("=== CYCLE inspiration-note.md re-tamper (no sticky clean) ===")
    tamper("inspiration-note.md", b"\nV108-TAMPER note\n")
    result = run_verify(MIRROR, target)
    expect("retamper-note", result, 2, ("DIGEST-MISMATCH", "inspiration-note.md"), ())
    restore("inspiration-note.md")
    result = run_verify(MIRROR, target)
    expect("restore-note", result, 0, ("RESULT PASS",), ("DIGEST-MISMATCH", "FINDING"))

    print("=== CYCLE contradictions.json trailing whitespace ===")
    tamper("contradictions.json", b"\n")
    result = run_verify(MIRROR, target)
    expect(
        "tamper-json",
        result,
        2,
        ("DIGEST-MISMATCH", "contradictions.json"),
        ("REDUCTION-DETECTED", "ADDITION-DETECTED", "ENDPOINT-CHANGE"),
    )
    restore("contradictions.json")
    result = run_verify(MIRROR, target)
    expect("restore-json", result, 0, ("RESULT PASS",), ("DIGEST-MISMATCH", "FINDING"))

    after_files = tree_files(MIRROR)
    pin_sha_after = contract_sha(MIRROR)
    print("CONTRACT_SHA_AFTER", pin_sha_after)
    print("CONTRACT_UNCHANGED", pin_sha == pin_sha_after)
    added = sorted(set(after_files) - set(before_files))
    removed = sorted(set(before_files) - set(after_files))
    print("TREE_ADDED", added)
    print("TREE_REMOVED", removed)
    byte_match = all((fixture_dir / name).read_bytes() == originals[name] for name in PINNED)
    print("FIXTURE_BYTES_RESTORED", byte_match)

    live_after = {
        "tool": sha256(live_tool),
        "contract": sha256(live_contract),
    }
    print("LIVE_AFTER", live_after)
    print("LIVE_UNCHANGED", live_before == live_after)
    print("FAILURES", failures)
    if failures or pin_sha != pin_sha_after or added or removed or not byte_match or live_before != live_after:
        print("HARNESS_RESULT FAIL")
        return 1
    print("HARNESS_RESULT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
