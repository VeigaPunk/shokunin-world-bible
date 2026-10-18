#!/usr/bin/env python3
"""Independent freshness measurement. Read-only. Prints evidence blocks."""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
os.chdir(LANE)

WATCH = [
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/README.md",
    "corpus/tools/map_obligations.py",
    "corpus/tools/map-obligations-contract.json",
    "corpus/tools/support_check.py",
    "corpus/tools/boundary_doc_check.py",
    "corpus/fixtures/check_bible.py",
    "SKILL.md",
    "corpus/fixtures/README.md",
    "corpus/README.md",
    "corpus/knowledge/r91-c9-watch.md",
    "corpus/knowledge/r95-aftermath-scope-note.md",
    "corpus/knowledge/r96-response-scope-note.md",
    "corpus/knowledge/r97-acknowledgment-scope-note.md",
    "corpus/knowledge/r98-clerk-scope-note.md",
    "corpus/knowledge/r99-lapse-scope-note.md",
    "corpus/knowledge/r99-gate-blind-spot-table.md",
]
FIX = "corpus/fixtures/r99-window-lapse"
FIX_FILES = [
    "README.md",
    "claim-excerpt-map.md",
    "contradictions.json",
    "entities.json",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "relations.json",
    "source-excerpt.md",
    "sources.json",
    "timeline.json",
]
HEX = re.compile(r"(?<![0-9a-f])[0-9a-f]{12,64}(?![0-9a-f])")


def sha(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def run(cmd):
    p = subprocess.run(cmd, cwd=LANE, text=True, capture_output=True)
    print(f"$ {' '.join(cmd)}")
    print(f"exit={p.returncode}")
    sys.stdout.write(p.stdout)
    if p.stderr:
        print("STDERR:")
        sys.stdout.write(p.stderr)
    print("---")
    return p.returncode


def main():
    print("=== HEAD ===")
    run(["git", "rev-parse", "HEAD"])
    run(["date", "+%Y-%m-%dT%H:%M:%S%z"])
    print("=== porcelain excluding .ufo ===")
    p = subprocess.run(
        ["git", "status", "--porcelain", "-uall"],
        cwd=LANE,
        text=True,
        capture_output=True,
    )
    lines = [
        ln
        for ln in p.stdout.splitlines()
        if ".ufo/" not in ln and not ln.endswith(".ufo")
    ]
    print("\n".join(lines) if lines else "(empty)")
    print(f"porcelain_non_ufo_count={len(lines)}")

    print("=== watched hashes ===")
    live = {}
    for rel in WATCH:
        path = LANE / rel
        if path.is_file():
            digest = sha(path)
            live[rel] = digest
            print(f"{digest}  {rel}")
        else:
            print(f"ABSENT  {rel}")

    print("=== r99 fixture hashes ===")
    for name in FIX_FILES:
        path = LANE / FIX / name
        if path.is_file():
            print(f"{sha(path)}  {FIX}/{name}  bytes={path.stat().st_size}")
        else:
            print(f"ABSENT  {FIX}/{name}")

    print("=== contract summary ===")
    cpath = LANE / "corpus/tools/dependency-freeze-contract.json"
    if cpath.is_file():
        data = json.loads(cpath.read_text())
        pins = data.get("pins", {})
        print("schema_version", data.get("schema_version"))
        print("payload_schema_version", data.get("payload_schema_version"))
        print("pinned_files", data.get("pinned_files"))
        print("pin_names", sorted(pins))
        print("self_test_cases", sorted((data.get("self_test") or {}).get("expected", {})))
        print("contract_revision", data.get("revision"))
        for name, pin in pins.items():
            files = pin.get("files") or {}
            print(
                f"PIN {name} nfiles={len(files)} schema={pin.get('payload_schema_version')} "
                f"revision={pin.get('revision')} content={str(pin.get('content_sha256',''))[:16]}"
            )
            missing = [f for f in (data.get("pinned_files") or []) if f not in files]
            if missing:
                print(f"  MISSING_IN_PIN {missing}")

    print("=== new-doc pin citations ===")
    docs = [
        LANE / "corpus/knowledge/r99-lapse-scope-note.md",
        LANE / "corpus/knowledge/r99-gate-blind-spot-table.md",
        LANE / "corpus/tools/README.md",
        LANE / "SKILL.md",
        LANE / "corpus/fixtures/r99-window-lapse/README.md",
    ]
    known = {v: k for k, v in live.items()}
    for doc in docs:
        if not doc.is_file():
            print(f"ABSENT {doc.relative_to(LANE)}")
            continue
        text = doc.read_text(encoding="utf-8")
        print(f"DOC {doc.relative_to(LANE)} bytes={doc.stat().st_size} lines={text.count(chr(10))+1}")
        # metadata header
        head = "\n".join(text.splitlines()[:8])
        print("HEAD:")
        print(head)
        for i, line in enumerate(text.splitlines(), 1):
            for m in HEX.finditer(line):
                token = m.group(0)
                if not re.search(r"[a-f]", token):
                    continue
                hit = None
                for full, rel in known.items():
                    if full.startswith(token):
                        hit = rel
                        break
                print(
                    f"CITE {doc.name}:{i} {token[:16]} "
                    f"{'LIVE:'+hit if hit else 'NO-LIVE-PREFIX'} | {line.strip()[:160]}"
                )

    print("=== receipts ===")
    fix = LANE / FIX
    if fix.is_dir():
        run(["python3", "corpus/fixtures/check_bible.py", FIX])
        run(["python3", "corpus/tools/map_obligations.py", FIX])
        run(["python3", "corpus/tools/support_check.py", FIX])
    if (LANE / "corpus/tools/dependency_freeze.py").is_file():
        run(["python3", "corpus/tools/dependency_freeze.py", "--self-test"])


if __name__ == "__main__":
    main()
