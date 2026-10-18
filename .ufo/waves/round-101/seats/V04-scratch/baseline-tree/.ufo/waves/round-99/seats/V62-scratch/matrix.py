#!/usr/bin/env python3
"""V62 independent Markdown-tamper matrix. Copies only; never writes the lane corpus."""

import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = LANE / ".ufo/waves/round-99/seats/V62-scratch"
MIRROR = SCRATCH / "mirror"
TOOL_SRC = LANE / "corpus/tools/dependency_freeze.py"
CONTRACT_SRC = LANE / "corpus/tools/dependency-freeze-contract.json"
CHAIN = [
    "r88-m3-maya-cluster",
    "r94-paired-crossing",
    "r95-crossing-aftermath",
    "r96-crossing-response",
    "r97-crossing-acknowledgment",
    "r98-clerk-filing",
]
MARKDOWN = [
    "README.md",
    "claim-excerpt-map.md",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "source-excerpt.md",
]
PY = sys.executable


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run_verify(tool, fixture):
    cmd = [PY, str(tool), str(fixture)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "cmd": cmd,
        "exit": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def finding_lines(stdout):
    return [line for line in stdout.splitlines() if line.startswith("FINDING ") or line.startswith("RESULT ")]


def names_changed(stdout):
    text = "\n".join(finding_lines(stdout))
    return text


results = []


def record(case, fixture, extra, outcome):
    row = {
        "case": case,
        "fixture": fixture,
        **extra,
        "exit": outcome["exit"],
        "stdout": outcome["stdout"],
        "stderr": outcome["stderr"],
        "cmd": outcome["cmd"],
    }
    results.append(row)
    print(f"CASE {case} fixture={fixture} exit={outcome['exit']}")
    print("CMD " + " ".join(outcome["cmd"]))
    print("STDOUT:")
    print(outcome["stdout"].rstrip() or "<empty>")
    if outcome["stderr"].strip():
        print("STDERR:")
        print(outcome["stderr"].rstrip())
    print("---")
    return row


def main():
    print(f"python3 {PY}")
    print(f"lane {LANE}")
    live_tool_sha = sha256_file(TOOL_SRC)
    live_contract_sha = sha256_file(CONTRACT_SRC)
    print(f"LIVE_TOOL_SHA {live_tool_sha}")
    print(f"LIVE_CONTRACT_SHA {live_contract_sha}")
    contract = json.loads(CONTRACT_SRC.read_text(encoding="utf-8"))
    print(f"schema_version {contract.get('schema_version')}")
    print(f"payload_schema_version {contract.get('payload_schema_version')}")
    print(f"top_pinned_files {contract.get('pinned_files')}")
    print(f"self_test_n {len(contract.get('self_test', {}).get('expected', {}))}")
    print(f"markdown_tamper_expected {contract['self_test']['expected'].get('markdown_tamper')}")
    for name in CHAIN:
        pin = contract["pins"][name]
        print(
            f"PIN {name} payload={pin.get('payload_schema_version')} "
            f"nfiles={len(pin.get('files', {}))} files={sorted(pin.get('files', {}))}"
        )

    if MIRROR.exists():
        shutil.rmtree(MIRROR)
    (MIRROR / "corpus/tools").mkdir(parents=True)
    shutil.copy2(TOOL_SRC, MIRROR / "corpus/tools/dependency_freeze.py")
    shutil.copy2(CONTRACT_SRC, MIRROR / "corpus/tools/dependency-freeze-contract.json")
    for name in CHAIN:
        shutil.copytree(LANE / "corpus/fixtures" / name, MIRROR / "corpus/fixtures" / name)
    tool = MIRROR / "corpus/tools/dependency_freeze.py"
    print(f"MIRROR_TOOL_SHA {sha256_file(tool)}")
    print(f"MIRROR_CONTRACT_SHA {sha256_file(MIRROR / 'corpus/tools/dependency-freeze-contract.json')}")

    for name in CHAIN:
        fixture = MIRROR / "corpus/fixtures" / name
        outcome = run_verify(tool, fixture)
        record("clean-copy", name, {}, outcome)

    for name in CHAIN:
        fixture = MIRROR / "corpus/fixtures" / name
        for filename in MARKDOWN:
            path = fixture / filename
            original = path.read_bytes()
            # Interior byte insertion, not only a trailing newline.
            mutated = original[:1] + b"V62" + original[1:]
            path.write_bytes(mutated)
            try:
                outcome = run_verify(tool, fixture)
            finally:
                path.write_bytes(original)
            record(
                "md-interior",
                name,
                {"file": filename, "delta": "insert V62 after byte 0"},
                outcome,
            )
            if path.read_bytes() != original:
                print(f"RESTORE-FAIL {name}/{filename}")

    for name in ("r95-crossing-aftermath", "r98-clerk-filing"):
        fixture = MIRROR / "corpus/fixtures" / name
        path = fixture / "fictional-excerpts.md"
        original = path.read_bytes()
        needle = b"depends on"
        if needle not in original:
            print(f"WORDING-NEEDLE-ABSENT {name}")
            continue
        mutated = original.replace(needle, b"follows", 1)
        path.write_bytes(mutated)
        try:
            outcome = run_verify(tool, fixture)
        finally:
            path.write_bytes(original)
        record(
            "wording-removal",
            name,
            {"file": "fictional-excerpts.md", "delta": "first 'depends on' -> 'follows'"},
            outcome,
        )

    for name in CHAIN:
        fixture = MIRROR / "corpus/fixtures" / name
        paths = [fixture / "README.md", fixture / "fictional-excerpts.md"]
        originals = {path: path.read_bytes() for path in paths}
        for path in paths:
            path.write_bytes(originals[path] + b"\nV62-TWO\n")
        try:
            outcome = run_verify(tool, fixture)
        finally:
            for path, raw in originals.items():
                path.write_bytes(raw)
        record(
            "two-file",
            name,
            {"files": ["README.md", "fictional-excerpts.md"], "delta": "append newline+V62-TWO to both"},
            outcome,
        )

    # Five Markdown files at once on the chain tail.
    name = "r98-clerk-filing"
    fixture = MIRROR / "corpus/fixtures" / name
    paths = [fixture / filename for filename in MARKDOWN]
    originals = {path: path.read_bytes() for path in paths}
    for path in paths:
        path.write_bytes(originals[path] + b"\n")
    try:
        outcome = run_verify(tool, fixture)
    finally:
        for path, raw in originals.items():
            path.write_bytes(raw)
    record("five-md", name, {"files": MARKDOWN, "delta": "append newline to all five"}, outcome)

    # Permission-only, still readable, every Markdown file of r98.
    for filename in MARKDOWN:
        path = fixture / filename
        before = stat.S_IMODE(path.stat().st_mode)
        digest_before = sha256_file(path)
        path.chmod(0o600)
        during = stat.S_IMODE(path.stat().st_mode)
        digest_during = sha256_file(path)
        try:
            outcome = run_verify(tool, fixture)
        finally:
            path.chmod(before)
        after = stat.S_IMODE(path.stat().st_mode)
        record(
            "perm-readable",
            name,
            {
                "file": filename,
                "mode_before": oct(before),
                "mode_during": oct(during),
                "mode_after": oct(after),
                "sha_unchanged": digest_before == digest_during,
                "sha": digest_before,
            },
            outcome,
        )

    # Unreadable permission-only on r98 README.
    path = fixture / "README.md"
    before = stat.S_IMODE(path.stat().st_mode)
    path.chmod(0o000)
    during = stat.S_IMODE(path.stat().st_mode)
    try:
        outcome = run_verify(tool, fixture)
    finally:
        path.chmod(before)
    record(
        "perm-unreadable",
        name,
        {"file": "README.md", "mode_before": oct(before), "mode_during": oct(during), "mode_restored": oct(stat.S_IMODE(path.stat().st_mode))},
        outcome,
    )

    # mtime-only sibling observation.
    path = fixture / "source-excerpt.md"
    before_mtime = path.stat().st_mtime_ns
    os.utime(path, None)
    after_mtime = path.stat().st_mtime_ns
    outcome = run_verify(tool, fixture)
    record(
        "mtime-only",
        name,
        {"file": "source-excerpt.md", "mtime_changed": before_mtime != after_mtime, "before": before_mtime, "after": after_mtime},
        outcome,
    )

    # Unpinned extra Markdown on r88.
    extra = MIRROR / "corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md"
    if extra.is_file():
        original = extra.read_bytes()
        extra.write_bytes(original + b"\nV62-UNPINNED\n")
        try:
            outcome = run_verify(tool, extra.parent)
        finally:
            extra.write_bytes(original)
        record(
            "unpinned-md",
            "r88-m3-maya-cluster",
            {"file": "symbolism-clause-map.md", "delta": "append V62-UNPINNED"},
            outcome,
        )
    else:
        print("UNPINNED-FILE-ABSENT")

    # Same-bytes rewrite control.
    path = fixture / "inspiration-note.md"
    original = path.read_bytes()
    path.write_bytes(original)
    outcome = run_verify(tool, fixture)
    record("same-bytes-rewrite", name, {"file": "inspiration-note.md"}, outcome)

    print("==== SELF-TEST ====")
    self_cmd = [PY, str(tool), "--self-test"]
    self_result = subprocess.run(self_cmd, capture_output=True, text=True)
    print("CMD " + " ".join(self_cmd))
    print(f"EXIT {self_result.returncode}")
    print("STDOUT:")
    print(self_result.stdout.rstrip())
    if self_result.stderr.strip():
        print("STDERR:")
        print(self_result.stderr.rstrip())
    results.append({
        "case": "self-test",
        "cmd": self_cmd,
        "exit": self_result.returncode,
        "stdout": self_result.stdout,
        "stderr": self_result.stderr,
    })

    end_tool = sha256_file(TOOL_SRC)
    end_contract = sha256_file(CONTRACT_SRC)
    print(f"END_LIVE_TOOL_SHA {end_tool}")
    print(f"END_LIVE_CONTRACT_SHA {end_contract}")
    print(f"LIVE_STABLE {end_tool == live_tool_sha and end_contract == live_contract_sha}")
    s1 = sorted(p.name for p in (LANE / ".ufo/waves/round-99/seats").glob("S1*.md"))
    print(f"S1_REPORTS {s1 or 'ABSENT'}")

    out = SCRATCH / "matrix-results.json"
    out.write_text(json.dumps({
        "live_tool_sha_start": live_tool_sha,
        "live_contract_sha_start": live_contract_sha,
        "live_tool_sha_end": end_tool,
        "live_contract_sha_end": end_contract,
        "s1_reports": s1,
        "results": results,
    }, indent=2), encoding="utf-8")
    print(f"WROTE {out}")


if __name__ == "__main__":
    main()
