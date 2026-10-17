#!/usr/bin/env python3
"""Enumerate the pointer-cell surface of every delivered map (false-positive hunt input)."""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
MAPS = sorted(ROOT.glob("corpus/**/claim-*excerpt-map.md"))
BACKTICK = re.compile(r"`([^`]+)`")
POINTERISH = re.compile(r"(entities|relations|timeline|sources|contradictions)\.json#|"
                        r"(entities|relations|timeline)\[[0-9]+\]")

for path in MAPS:
    lines = path.read_text(encoding="utf-8").splitlines()
    heading = next((i for i, line in enumerate(lines)
                    if re.match(r"^##\s+JSON facts(?:\s|$|\()", line, re.IGNORECASE)), None)
    print(f"=== {path.relative_to(ROOT)} heading_line={heading + 1 if heading is not None else None}")
    if heading is None:
        continue
    end = next((i for i in range(heading + 1, len(lines)) if re.match(r"^#{1,6}\s+", lines[i])), len(lines))
    table_start = next((i for i in range(heading + 1, end) if lines[i].lstrip().startswith("|")), None)
    if table_start is None:
        continue
    header = [cell.strip() for cell in lines[table_start].strip().strip("|").split("|")]
    pointer_index = next((i for i, cell in enumerate(header)
                          if re.sub(r"[^a-z0-9]+", " ", cell.strip().strip("`").casefold()).strip()
                          in {"json fact pointer", "json fact pointer and fields", "json fact and fields"}), None)
    print(f"    header={header} pointer_column={pointer_index}")
    for index in range(table_start + 1, end):
        line = lines[index]
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells):
            continue
        cell = cells[pointer_index] if pointer_index is not None and pointer_index < len(cells) else "?"
        tokens = BACKTICK.findall(cell)
        pointer_tokens = [token for token in tokens if POINTERISH.search(token)]
        flag = " MULTI-TOKEN" if len(tokens) > 1 else ""
        flag += " POINTERISH>1" if len(pointer_tokens) > 1 else ""
        flag += " BARE-POINTERISH" if POINTERISH.search(BACKTICK.sub("", cell)) else ""
        print(f"    row{index + 1} tokens={tokens} {flag}")
        print(f"        cell={cell}")
    sys.stdout.flush()
