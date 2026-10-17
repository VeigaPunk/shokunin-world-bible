#!/usr/bin/env python3
"""V22 preservation-mutation harness: build mutated copies of the r97 fixture.

Writes ONLY under V22-scratch/mutants/. Never touches corpus/.
Each mutant is a full copy of corpus/fixtures/r97-crossing-acknowledgment with
one preservation violation applied. Prints a manifest of the exact bytes
changed so the report can quote them.
"""

import json
import os
import re
import shutil
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SCRATCH = REPO / ".ufo/waves/round-97/seats/V22-scratch"
SRC = Path(os.environ.get("V22_SRC", str(REPO / "corpus/fixtures/r97-crossing-acknowledgment")))
MUTANTS = Path(os.environ.get("V22_MUTANTS", str(SCRATCH / "mutants")))
MAP = "claim-excerpt-map.md"


def load(path):
    return path.read_text(encoding="utf-8")


def save(path, text):
    path.write_text(text, encoding="utf-8")


def fresh(name):
    target = MUTANTS / name
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(SRC, target)
    return target


def data_row_lines(lines):
    return [i for i, line in enumerate(lines) if re.match(r"^\|\s*J[0-9]+\s*\|", line)]


def last_row(lines):
    return data_row_lines(lines)[-1]


def row_cells(line):
    return line.strip().strip("|").split("|")


def rebuild_row(cells):
    return "|" + "|".join(cells) + "|"


def set_declaration(lines, facts, total, anchors=None):
    for i, line in enumerate(lines):
        if line.startswith("**Expected inventory:**"):
            new = re.sub(r"([0-9]+) JSON facts", f"{facts} JSON facts", line)
            new = re.sub(r"([0-9]+) total mapped rows", f"{total} total mapped rows", new)
            if anchors is not None:
                new = re.sub(r"([0-9]+) distinct excerpt anchors", f"{anchors} distinct excerpt anchors", new)
            lines[i] = new
            return new
    raise SystemExit("declaration line not found")


def manifest(name, note, detail):
    print(f"MUTANT {name}: {note}")
    print(f"  {detail}")


def m1_span_break():
    t = fresh("m1-span-break")
    p = t / MAP
    lines = load(p).splitlines()
    i = last_row(lines)
    cells = row_cells(lines[i])
    header = None
    for j in range(i):
        if re.match(r"^\|\s*ID\s*\|", lines[j]):
            header = [c.strip().strip("`").lower() for c in row_cells(lines[j])]
    span_index = next(k for k, h in enumerate(header) if h == "line span")
    old = cells[span_index].strip()
    if re.fullmatch(r"[0-9]+", old):
        new = str(int(old) + 1)
    else:
        new = "1"
    cells[span_index] = f" {new} "
    lines[i] = rebuild_row(cells)
    save(p, "\n".join(lines) + "\n")
    manifest("m1-span-break", f"last JSON-facts row span {old} -> {new} (anchor now outside span)",
             lines[i][:120])


def m1b_span_off_by_one():
    t = fresh("m1b-span-off-by-one")
    p = t / MAP
    lines = load(p).splitlines()
    header = None
    for j, line in enumerate(lines):
        if re.match(r"^\|\s*ID\s*\|", line):
            header = [c.strip().strip("`").lower() for c in row_cells(line)]
            break
    span_index = next(k for k, h in enumerate(header) if h == "line span")
    for i in data_row_lines(lines):
        cells = row_cells(lines[i])
        if re.fullmatch(r"[0-9]+", cells[span_index].strip()):
            old = cells[span_index].strip()
            cells[span_index] = f" {int(old) + 1} "
            lines[i] = rebuild_row(cells)
            save(p, "\n".join(lines) + "\n")
            manifest("m1b-span-off-by-one",
                     f"first single-line row {cells[0].strip()} span {old} -> {int(old) + 1}",
                     lines[i][:120])
            return
    raise SystemExit("no single-line span row found")


def drop_last_row(lines):
    i = last_row(lines)
    dropped = lines.pop(i)
    return dropped


def m2_row_drop():
    t = fresh("m2-row-drop")
    p = t / MAP
    lines = load(p).splitlines()
    dropped = drop_last_row(lines)
    save(p, "\n".join(lines) + "\n")
    manifest("m2-row-drop", "last JSON-facts row deleted; declaration untouched",
             dropped[:120])


def m2b_row_drop_declared():
    t = fresh("m2b-row-drop-declared")
    p = t / MAP
    lines = load(p).splitlines()
    drop_last_row(lines)
    new = set_declaration(lines, 16, 18)
    save(p, "\n".join(lines) + "\n")
    manifest("m2b-row-drop-declared", "last row deleted + declaration downgraded", new)


def delete_last_event(t):
    p = t / "timeline.json"
    data = json.loads(load(p))
    removed = data.pop()
    save(p, json.dumps(data, indent=2) + "\n")
    return removed["id"]


def m3_key_row_deletion():
    t = fresh("m3-key-row-deletion")
    event = delete_last_event(t)
    p = t / MAP
    lines = load(p).splitlines()
    dropped = drop_last_row(lines)
    save(p, "\n".join(lines) + "\n")
    manifest("m3-key-row-deletion",
             f"timeline.json record {event} deleted + its map row deleted; declaration untouched",
             dropped[:120])


def m3c_key_row_deletion_declared():
    t = fresh("m3c-key-row-deletion-declared")
    event = delete_last_event(t)
    p = t / MAP
    lines = load(p).splitlines()
    drop_last_row(lines)
    new = set_declaration(lines, 16, 18)
    save(p, "\n".join(lines) + "\n")
    manifest("m3c-key-row-deletion-declared",
             f"record {event} + row deleted + declaration downgraded (self-consistent tamper)",
             new)


def m3d_key_row_deletion_fully_declared():
    t = fresh("m3d-key-row-deletion-fully-declared")
    event = delete_last_event(t)
    p = t / MAP
    lines = load(p).splitlines()
    drop_last_row(lines)
    new = set_declaration(lines, 16, 18, anchors=14)
    save(p, "\n".join(lines) + "\n")
    manifest("m3d-key-row-deletion-fully-declared",
             f"record {event} + row deleted + facts/rows/anchors all downgraded", new)


def m4_deps_reduction():
    t = fresh("m4-deps-reduction")
    p = t / "timeline.json"
    data = json.loads(load(p))
    target = data[-1]
    before = list(target.get("depends_on", []))
    target["depends_on"] = []
    save(p, json.dumps(data, indent=2) + "\n")
    manifest("m4-deps-reduction",
             f"timeline.json record {target['id']} depends_on {before} -> []",
             json.dumps(target, ensure_ascii=False)[:160])


def m5a_legacy_token_canonical():
    t = fresh("m5a-legacy-token-canonical")
    p = t / MAP
    lines = load(p).splitlines()
    i = last_row(lines)
    cells = row_cells(lines[i])
    old = cells[1].strip()
    m = re.fullmatch(r"`timeline\.json#/([0-9]+)`(.*)", old)
    cells[1] = f" `timeline[{m.group(1)}]`{m.group(2)} "
    lines[i] = rebuild_row(cells)
    save(p, "\n".join(lines) + "\n")
    manifest("m5a-legacy-token-canonical", f"canonical cell {old} -> legacy token", lines[i][:120])


def m5b_hidden_second_pointer_canonical():
    t = fresh("m5b-hidden-second-pointer-canonical")
    p = t / MAP
    lines = load(p).splitlines()
    i = last_row(lines)
    cells = row_cells(lines[i])
    old = cells[1].strip()
    m = re.fullmatch(r"`(timeline\.json#[^`]+)`.*", old)
    cells[1] = f" `{m.group(1)}` (also `relations.json#/0`) "
    lines[i] = rebuild_row(cells)
    save(p, "\n".join(lines) + "\n")
    manifest("m5b-hidden-second-pointer-canonical",
             f"hidden second pointer injected into canonical cell (was {old})", lines[i][:120])


def m5c_legacy_form_hidden_pointer():
    t = fresh("m5c-legacy-form-hidden-pointer")
    p = t / MAP
    lines = load(p).splitlines()
    for i, line in enumerate(lines):
        if re.match(r"^\|\s*ID\s*\|", line):
            cells = row_cells(line)
            for k, c in enumerate(cells):
                if c.strip().strip("`").lower() == "json fact pointer and fields":
                    cells[k] = " JSON fact and fields "
            lines[i] = rebuild_row(cells)
    i = last_row(lines)
    cells = row_cells(lines[i])
    m = re.fullmatch(r"`timeline\.json#/([0-9]+)`.*", cells[1].strip())
    cells[1] = f" `timeline[{m.group(1)}]` (also `relations.json#/0`) "
    lines[i] = rebuild_row(cells)
    save(p, "\n".join(lines) + "\n")
    manifest("m5c-legacy-form-hidden-pointer",
             "map switched to legacy pointer grammar + last row carries a hidden second pointer",
             lines[i][:120])


def main():
    if not SRC.is_dir():
        raise SystemExit(f"source fixture missing: {SRC}")
    MUTANTS.mkdir(parents=True, exist_ok=True)
    m1_span_break()
    m1b_span_off_by_one()
    m2_row_drop()
    m2b_row_drop_declared()
    m3_key_row_deletion()
    m3c_key_row_deletion_declared()
    m3d_key_row_deletion_fully_declared()
    m4_deps_reduction()
    m5a_legacy_token_canonical()
    m5b_hidden_second_pointer_canonical()
    m5c_legacy_form_hidden_pointer()
    print("MUTANTS READY under", MUTANTS)


if __name__ == "__main__":
    sys.exit(main())
