#!/usr/bin/env python3
"""Hash lore-shokunin before/after dependency_freeze --self-test and list new entries.

Writes only under this scratch directory. Does not invoke the self-test itself.
"""
from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = ROOT / ".ufo/waves/round-99/seats/V97-scratch"
SEATS = ROOT / ".ufo/waves/round-99/seats"

# Content-hash everything except git metadata, this seat's scratch (our own
# measurement writes), and other seats' exclusive report trees (concurrent
# writers). Name inventory still covers the whole repo so new entries are listed.
SKIP_CONTENT_PREFIXES = (
    ROOT / ".git",
    SCRATCH,
    SEATS,
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def skip_content(path: Path) -> bool:
    for prefix in SKIP_CONTENT_PREFIXES:
        try:
            path.relative_to(prefix)
            return True
        except ValueError:
            continue
    return False


def snapshot(dest: Path) -> None:
    names = []
    hashed = []
    for dirpath, dirnames, filenames in os.walk(ROOT, followlinks=False):
        dirnames.sort()
        filenames.sort()
        current = Path(dirpath)
        # Do not descend into .git (huge, not a self-test write target) or this
        # scratch (the snapshot files themselves). Still record the directory name.
        rel_current = rel(current) if current != ROOT else ""
        if rel_current in (".git", ".ufo/waves/round-99/seats/V97-scratch") or rel_current.startswith(
            ".git/"
        ) or rel_current.startswith(".ufo/waves/round-99/seats/V97-scratch/"):
            dirnames[:] = []
            continue
        for name in dirnames:
            path = current / name
            kind = "l" if path.is_symlink() else "d"
            names.append(f"{kind}\t{rel(path)}")
        for name in filenames:
            path = current / name
            if path.is_symlink():
                names.append(f"l\t{rel(path)}")
                continue
            try:
                st = path.stat()
            except OSError as exc:
                names.append(f"?\t{rel(path)}\t{exc}")
                continue
            names.append(f"f\t{rel(path)}\t{st.st_size}\t{st.st_mtime_ns}")
            if skip_content(path):
                continue
            digest = hashlib.sha256()
            with path.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
            hashed.append(f"{digest.hexdigest()}  {rel(path)}")
    names.sort()
    hashed.sort(key=lambda line: line.split("  ", 1)[1])
    name_blob = ("\n".join(names) + "\n").encode()
    hash_blob = ("\n".join(hashed) + "\n").encode()
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "names.txt").write_bytes(name_blob)
    (dest / "content.sha256").write_bytes(hash_blob)
    rollup = hashlib.sha256(hash_blob).hexdigest()
    name_rollup = hashlib.sha256(name_blob).hexdigest()
    (dest / "rollup.txt").write_text(
        f"content_manifest_sha256 {rollup}\n"
        f"name_inventory_sha256 {name_rollup}\n"
        f"content_files {len(hashed)}\n"
        f"name_entries {len(names)}\n",
        encoding="utf-8",
    )
    print(f"snapshot {dest.name}: files={len(hashed)} names={len(names)} content={rollup} names={name_rollup}")


def main() -> int:
    label = sys.argv[1]
    snapshot(SCRATCH / label)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
