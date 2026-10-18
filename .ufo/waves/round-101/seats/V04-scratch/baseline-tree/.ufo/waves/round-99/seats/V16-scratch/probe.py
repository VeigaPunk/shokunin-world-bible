#!/usr/bin/env python3
"""V16 r99 dependency probes. Mutates scratch copies only. Never writes the live fixture."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
CHECKER = LANE / "corpus/fixtures/check_bible.py"
FREEZE = LANE / "corpus/tools/dependency_freeze.py"
LIVE = LANE / "corpus/fixtures/r99-window-lapse"
SCRATCH = Path(__file__).resolve().parent
EVENT = "clerk-lapse-recorded"
PRED = "clerk-filing-open"


def run(argv, cwd=LANE):
    result = subprocess.run(
        [sys.executable, *argv],
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


_copy_n = 0


def copy_fixture(tmp):
    global _copy_n
    _copy_n += 1
    dest = tmp / f"copy-{_copy_n}" / "r99-window-lapse"
    shutil.copytree(LIVE, dest)
    return dest


def load_timeline(fixture):
    path = fixture / "timeline.json"
    return path, json.loads(path.read_text(encoding="utf-8"))


def save_timeline(path, rows):
    path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def find_event(rows, event_id):
    hits = [row for row in rows if row.get("id") == event_id]
    if len(hits) != 1:
        raise SystemExit(f"expected exactly one {event_id}, found {len(hits)}")
    return hits[0]


def bible(fixture, label):
    code, out, err = run([str(CHECKER), str(fixture)])
    print(f"=== {label} check_bible exit={code} ===")
    print(out, end="" if out.endswith("\n") or not out else "\n")
    if err.strip():
        print("--- stderr ---")
        print(err, end="" if err.endswith("\n") else "\n")
    return code, out, err


def freeze_verify(fixture, label, tool=FREEZE, contract_note="live-tool"):
    code, out, err = run([str(tool), str(fixture)])
    print(f"=== {label} dependency_freeze ({contract_note}) exit={code} ===")
    print(out, end="" if out.endswith("\n") or not out else "\n")
    if err.strip():
        print("--- stderr ---")
        print(err, end="" if err.endswith("\n") else "\n")
    return code, out, err


def main():
    print(f"LIVE {LIVE}")
    print(f"CHECKER {CHECKER}")
    print(f"FREEZE {FREEZE}")
    if not LIVE.is_dir():
        print("ABSENT live fixture")
        return 2

    # Confirm the live tree is never a destination.
    before = {p.name: p.read_bytes() for p in LIVE.iterdir() if p.is_file()}

    with tempfile.TemporaryDirectory(prefix="v16-r99-", dir=SCRATCH) as raw:
        tmp = Path(raw)
        os.environ["TMPDIR"] = str(tmp)

        control = copy_fixture(tmp)
        bible(control, "P0 control copy")

        p1 = copy_fixture(tmp)
        path, rows = load_timeline(p1)
        row = find_event(rows, EVENT)
        had = "depends_on" in row
        row.pop("depends_on", None)
        save_timeline(path, rows)
        print(f"P1 mutation: dropped depends_on (was present={had}) from {EVENT}")
        bible(p1, "P1 drop depends_on")

        p2 = copy_fixture(tmp)
        path, rows = load_timeline(p2)
        row = find_event(rows, EVENT)
        row["depends_on"] = ["no-such-event-id"]
        save_timeline(path, rows)
        print(f"P2 mutation: {EVENT}.depends_on = ['no-such-event-id']")
        bible(p2, "P2 unknown id")

        p3 = copy_fixture(tmp)
        path, rows = load_timeline(p3)
        row = find_event(rows, EVENT)
        pred = find_event(rows, PRED)
        print(f"P3 before: {EVENT} tick={row['tick']} depends_on={row['depends_on']}; {PRED} tick={pred['tick']}")
        row["tick"] = 14
        save_timeline(path, rows)
        print(f"P3 mutation: {EVENT}.tick = 14 (dependency stays tick {pred['tick']})")
        bible(p3, "P3 tick 14 inversion")

        p4 = copy_fixture(tmp)
        path, rows = load_timeline(p4)
        before_n = len(rows)
        rows = [row for row in rows if row.get("id") != PRED]
        save_timeline(path, rows)
        print(f"P4 mutation: removed {PRED} ({before_n} -> {len(rows)} events); {EVENT} still depends_on it")
        bible(p4, "P4 remove clerk-filing-open")

        p5 = copy_fixture(tmp)
        path, rows = load_timeline(p5)
        row = find_event(rows, EVENT)
        lost = row.get("depends_on")
        row["depends_on"] = []
        save_timeline(path, rows)
        print(f"P5 mutation: {EVENT}.depends_on {lost} -> [] (dropped edge, key retained)")
        bible(p5, "P5 emptied depends_on (bible, discrimination)")
        freeze_verify(p5, "P5 dropped-edge copy")

        # Also drop the key entirely and freeze that copy, so both "dropped edge" shapes are quoted.
        p5b = copy_fixture(tmp)
        path, rows = load_timeline(p5b)
        find_event(rows, EVENT).pop("depends_on", None)
        save_timeline(path, rows)
        freeze_verify(p5b, "P5b key-removed copy")

    after = {p.name: p.read_bytes() for p in LIVE.iterdir() if p.is_file()}
    print(f"LIVE BYTE-STABLE {before == after} files_before={sorted(before)} files_after={sorted(after)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
