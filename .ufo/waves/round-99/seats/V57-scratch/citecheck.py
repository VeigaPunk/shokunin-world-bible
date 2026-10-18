#!/usr/bin/env python3
"""Resolve citations in an S5 knowledge note against the lane tree.

Bare file:line and file#/N citations resolve against --base (the r99 fixture)
when the citation-convention says so. Full-path citations resolve from the
lane root. A bare :NN continues the most recently named path in the same
sentence, matching the r97/r98 citation-convention.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")

# path with optional line, line-range, or JSON pointer
CITE = re.compile(
    r"(?P<path>(?:corpus/|\\.ufo/)[A-Za-z0-9_./-]+?\.(?:md|json|py))"
    r"(?P<tail>(?::\d+(?:-\d+)?)?(?:#/[A-Za-z0-9_./-]+)?)?"
)
BARE_FILE = re.compile(
    r"(?<![A-Za-z0-9_./-])(?P<path>[A-Za-z0-9_.-]+\.(?:md|json|py))"
    r"(?P<tail>(?::\d+(?:-\d+)?)?(?:#/[A-Za-z0-9_./-]+)?)"
)
BARE_CONT = re.compile(r"(?<![A-Za-z0-9_])(?P<tail>:\d+(?:-\d+)?|#/[A-Za-z0-9_./-]+)")
ROW_PTR = re.compile(r"\b(?:row\s+)?([A-Z]?\d{1,3}|J\d{2}|S\d{2}|F15-[A-Za-z0-9-]+|BR-\d+|P\d+)\b")


def load_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def resolve_json_pointer(data, pointer: str):
    if not pointer.startswith("#/"):
        raise ValueError(pointer)
    cur = data
    for part in pointer[2:].split("/"):
        if part == "":
            continue
        if isinstance(cur, list):
            cur = cur[int(part)]
        elif isinstance(cur, dict):
            if part not in cur:
                raise KeyError(part)
            cur = cur[part]
        else:
            raise TypeError(type(cur).__name__)
    return cur


def check_target(path: Path, tail: str) -> str:
    if not path.is_file():
        return f"MISSING {path}"
    if not tail:
        return "ok"
    problems = []
    line_m = re.search(r":(\d+)(?:-(\d+))?", tail)
    ptr_m = re.search(r"#/([A-Za-z0-9_./-]+)", tail)
    if line_m:
        lines = load_lines(path)
        start = int(line_m.group(1))
        end = int(line_m.group(2) or start)
        if start < 1 or end > len(lines) or end < start:
            problems.append(f"LINE-RANGE {start}-{end} of {len(lines)}")
    if ptr_m:
        if path.suffix != ".json":
            problems.append(f"POINTER-ON-NON-JSON {tail}")
        else:
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                resolve_json_pointer(data, "#/" + ptr_m.group(1))
            except Exception as exc:  # noqa: BLE001 — report, do not hide
                problems.append(f"POINTER {tail}: {type(exc).__name__}: {exc}")
    return "ok" if not problems else "; ".join(problems)


def iter_cites(text: str, base: Path):
    """Yield (kind, display, path, tail) in reading order, per sentence."""
    # split on sentence boundaries but keep markdown tables as their own units
    chunks = re.split(r"(?<=[.\n])\s+", text)
    for chunk in chunks:
        last_path = None
        # full paths first
        occupied = [False] * len(chunk)
        for m in CITE.finditer(chunk):
            for i in range(m.start(), m.end()):
                occupied[i] = True
            path = LANE / m.group("path")
            tail = m.group("tail") or ""
            last_path = path
            yield "full", m.group(0), path, tail
        # bare file citations not overlapping a full path
        for m in BARE_FILE.finditer(chunk):
            if any(occupied[i] for i in range(m.start(), m.end())):
                continue
            for i in range(m.start(), m.end()):
                occupied[i] = True
            path = base / m.group("path")
            tail = m.group("tail") or ""
            last_path = path
            yield "bare", m.group(0), path, tail
        # continuation :NN / #/N after a named path, not already consumed
        if last_path is not None:
            for m in BARE_CONT.finditer(chunk):
                if any(occupied[i] for i in range(m.start(), min(m.end(), len(occupied)))):
                    continue
                yield "cont", m.group(0), last_path, m.group("tail")


def metadata(text: str) -> dict:
    lines = text.splitlines()
    keys = {}
    for line in lines[:12]:
        if ":" in line and not line.startswith("#") and not line.startswith("|"):
            k, _, v = line.partition(":")
            if k.strip() in {"source", "verified-at", "recheck", "citation-convention", "snapshot", "measured-at"} or k.strip().endswith("-at"):
                keys[k.strip()] = v.strip()
    return keys


def source_paths(source_line: str) -> list[str]:
    return re.findall(r"(?:corpus/|\.ufo/)[A-Za-z0-9_./-]+?\.(?:md|json|py)", source_line)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("note")
    ap.add_argument("--base", default="corpus/fixtures/r99-window-lapse")
    args = ap.parse_args()
    note = Path(args.note)
    if not note.is_absolute():
        note = LANE / note
    text = note.read_text(encoding="utf-8")
    base = LANE / args.base
    meta = metadata(text)
    print("METADATA-KEYS", sorted(meta))
    for k, v in meta.items():
        print(f"  {k}: {v[:180]}")
    if "source" in meta:
        missing = []
        paths = source_paths(meta["source"])
        print(f"SOURCE-PATHS {len(paths)}")
        for p in paths:
            target = LANE / p
            if not target.exists():
                missing.append(p)
        print("SOURCE-MISSING", missing)
    bad = []
    seen = 0
    for kind, display, path, tail in iter_cites(text, base):
        seen += 1
        status = check_target(path, tail)
        if status != "ok":
            bad.append((kind, display, status))
    print(f"CITATIONS checked={seen} bad={len(bad)}")
    for item in bad:
        print(" BAD", item)
    # table rows: markdown tables with a pointer-like cell
    rows = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("|") and not re.match(r"^\|\s*-+", line):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if any(c.lower() in {"#", "id", "row", "class", "mutation"} for c in cells):
                continue
            rows.append((i, cells))
    print(f"TABLE-ROWS {len(rows)}")
    for i, cells in rows:
        joined = " | ".join(cells)
        print(f" ROW {i}: {joined[:240]}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
