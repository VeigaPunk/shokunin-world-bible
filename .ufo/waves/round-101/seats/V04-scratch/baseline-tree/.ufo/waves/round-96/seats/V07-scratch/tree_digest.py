#!/usr/bin/env python3
"""Digest the live corpus tree (excluding tool bytes owned by r96 producers) for write-hygiene checks."""

import hashlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
TARGET = ROOT / "corpus"
EXCLUDE = (
    "corpus/tools/map_obligations.py",
    "corpus/tools/map-obligations-contract.json",
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/__pycache__",
)


def main():
    entries = []
    for path in sorted(TARGET.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if any(rel == prefix or rel.startswith(prefix) for prefix in EXCLUDE):
            continue
        entries.append((rel, hashlib.md5(path.read_bytes()).hexdigest()))
    digest = hashlib.md5("\n".join(f"{rel} {md5}" for rel, md5 in entries).encode()).hexdigest()
    print(f"FILES {len(entries)} CORPUS-TREE-MD5 {digest}")
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w", encoding="utf-8") as handle:
            for rel, md5 in entries:
                handle.write(f"{md5} {rel}\n")


if __name__ == "__main__":
    main()
