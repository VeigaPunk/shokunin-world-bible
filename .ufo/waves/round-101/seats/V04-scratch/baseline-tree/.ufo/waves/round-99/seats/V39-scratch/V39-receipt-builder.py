#!/usr/bin/env python3
"""Presence audit for the round-99 128-seat wave. Writes scratch JSON only."""

import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
WAVE = ROOT / ".ufo/waves/round-99"
SEATS = WAVE / "seats"
SCRATCH = SEATS / "V39-scratch"
PARENT_WAVE = Path("/home/vgpnk/Projects/shokunin/.ufo/waves/round-99")
ROSTER = ["S1", "S2", "S3", "S4", "S5"] + [f"V{i:02d}" for i in range(1, 124)]
assert len(ROSTER) == 128, len(ROSTER)
PRODUCERS = ["S1", "S2", "S3", "S4", "S5"]
PREFIX_RE = re.compile(r"^(S[1-5]|V\d+)")
CANDIDATES = [
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/README.md",
    "SKILL.md",
    "corpus/fixtures/r99-window-lapse/README.md",
    "corpus/fixtures/r99-window-lapse/claim-excerpt-map.md",
    "corpus/fixtures/r99-window-lapse/contradictions.json",
    "corpus/fixtures/r99-window-lapse/entities.json",
    "corpus/fixtures/r99-window-lapse/fictional-excerpts.md",
    "corpus/fixtures/r99-window-lapse/inspiration-note.md",
    "corpus/fixtures/r99-window-lapse/relations.json",
    "corpus/fixtures/r99-window-lapse/source-excerpt.md",
    "corpus/fixtures/r99-window-lapse/sources.json",
    "corpus/fixtures/r99-window-lapse/timeline.json",
    "corpus/knowledge/r99-gate-blind-spot-table.md",
    "corpus/knowledge/r99-lapse-scope-note.md",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def first_line(path: Path) -> str:
    with path.open("rb") as f:
        raw = f.readline(4096)
    return raw.decode("utf-8", errors="replace").rstrip("\r\n")


def seat_of(name: str) -> str | None:
    m = PREFIX_RE.match(name)
    return m.group(1) if m else None


def audit() -> dict:
    now = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    reports = {}
    unexpected_md = []
    non_report_top = []
    for entry in sorted(SEATS.iterdir(), key=lambda p: p.name):
        if entry.name == "V39-scratch" and entry.is_dir():
            continue
        if entry.is_dir():
            non_report_top.append(entry.name + "/")
            continue
        if entry.suffix != ".md":
            non_report_top.append(entry.name)
            continue
        seat = seat_of(entry.name)
        if seat is None or seat not in ROSTER:
            unexpected_md.append(entry.name)
            continue
        reports.setdefault(seat, []).append(entry)

    duplicate = {
        seat: [p.name for p in paths]
        for seat, paths in reports.items()
        if len(paths) > 1
    }
    header_mismatches = []
    hashed = {}
    for seat, paths in reports.items():
        hashed[seat] = {}
        for p in paths:
            line = first_line(p)
            if not line.startswith(f"# {seat}"):
                header_mismatches.append(
                    {"file": p.name, "seat": seat, "first_line": line[:160]}
                )
            hashed[seat][p.name] = {
                "sha256": sha256(p),
                "bytes": p.stat().st_size,
                "mtime": time.strftime(
                    "%Y-%m-%dT%H:%M:%S%z", time.localtime(p.stat().st_mtime)
                ),
            }

    present = [s for s in ROSTER if s in reports]
    absent = [s for s in ROSTER if s not in reports]
    present_excl_self = [s for s in present if s != "V39"]

    pinned = {}
    missing_candidates = []
    for rel in CANDIDATES:
        p = ROOT / rel
        if p.is_file():
            pinned[rel] = {
                "sha256": sha256(p),
                "bytes": p.stat().st_size,
                "mtime": time.strftime(
                    "%Y-%m-%dT%H:%M:%S%z", time.localtime(p.stat().st_mtime)
                ),
            }
        else:
            missing_candidates.append(rel)

    parent_md = []
    if PARENT_WAVE.exists():
        for p in PARENT_WAVE.rglob("*.md"):
            parent_md.append(str(p))

    fixture_files = []
    fix = ROOT / "corpus/fixtures/r99-window-lapse"
    if fix.is_dir():
        fixture_files = sorted(x.name for x in fix.iterdir() if x.is_file())

    head = git("rev-parse", "HEAD")
    baseline = git("rev-parse", "4265df5")
    ancestor = subprocess.call(
        ["git", "merge-base", "--is-ancestor", "4265df5", "HEAD"], cwd=ROOT
    )
    status = subprocess.check_output(
        ["git", "status", "--porcelain=v1"], cwd=ROOT, text=True
    )

    return {
        "receipt_snapshot_utc": now,
        "baseline_commit": baseline,
        "head_at_snapshot": head,
        "baseline_is_ancestor_of_head": ancestor == 0,
        "git_status_porcelain": status.splitlines(),
        "roster_expected": 128,
        "reports_present_incl_self": len(present),
        "reports_present_excl_self": len(present_excl_self),
        "present": present,
        "absent": absent,
        "producer_present": [s for s in PRODUCERS if s in reports],
        "producer_absent": [s for s in PRODUCERS if s not in reports],
        "duplicate_report_prefixes": duplicate,
        "header_seat_mismatches": header_mismatches,
        "unexpected_md_in_seats_dir": unexpected_md,
        "non_report_top_level": non_report_top,
        "parent_tree_md": parent_md,
        "reports": {
            seat: hashed[seat] for seat in ROSTER if seat in hashed
        },
        "candidate_revision_pinned": pinned,
        "missing_candidate_paths": missing_candidates,
        "fixture_files": fixture_files,
    }


def main() -> None:
    data = audit()
    out = SCRATCH / "audit.json"
    out.write_text(json.dumps(data, indent=1) + "\n")
    print(
        json.dumps(
            {
                "snapshot": data["receipt_snapshot_utc"],
                "present_incl_self": data["reports_present_incl_self"],
                "present_excl_self": data["reports_present_excl_self"],
                "absent": len(data["absent"]),
                "producer_absent": data["producer_absent"],
                "missing_candidates": data["missing_candidate_paths"],
                "duplicates": data["duplicate_report_prefixes"],
                "header_mismatches": len(data["header_seat_mismatches"]),
                "unexpected_md": data["unexpected_md_in_seats_dir"],
                "parent_tree_md": data["parent_tree_md"],
                "fixture_files": data["fixture_files"],
                "head": data["head_at_snapshot"],
                "baseline_ancestor": data["baseline_is_ancestor_of_head"],
            },
            indent=1,
        )
    )


if __name__ == "__main__":
    main()
