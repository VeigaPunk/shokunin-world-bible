#!/usr/bin/env python3
"""V101 presence-final audit. Read-only unless --write-snapshot.

Roster: S1-S5 + V01-V123 = 128. Self is V101.
Writes scratch JSON always. Writes receipt.json collection_snapshot only
with --write-snapshot, and only when V39 has not already finalized a
snapshot that matches this live count.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
WAVE = ROOT / ".ufo/waves/round-99"
SEATS = WAVE / "seats"
RECEIPT = WAVE / "receipt.json"
SCRATCH = SEATS / "V101-scratch"
PARENT_WAVE = Path("/home/vgpnk/Projects/shokunin/.ufo/waves/round-99")
SELF = "V101"
ROSTER = ["S1", "S2", "S3", "S4", "S5"] + [f"V{i:02d}" for i in range(1, 124)]
assert len(ROSTER) == 128 and ROSTER[5] == "V01" and ROSTER[-1] == "V123"
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


def head_lines(path: Path, n: int = 20) -> list[str]:
    lines = []
    with path.open("rb") as f:
        for _ in range(n):
            raw = f.readline()
            if not raw:
                break
            lines.append(raw.decode("utf-8", errors="replace").rstrip("\r\n"))
    return lines


def seat_of(name: str) -> str | None:
    m = PREFIX_RE.match(name)
    return m.group(1) if m else None


def canonical(seat: str) -> str:
    if seat.startswith("S"):
        return seat
    n = int(seat[1:])
    return f"V{n:02d}" if n < 100 else f"V{n}"


def audit() -> dict:
    now = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    reports: dict[str, list[Path]] = {}
    unexpected_md = []
    non_report_top = []
    raw_prefix_anomalies = []
    for entry in sorted(SEATS.iterdir(), key=lambda p: p.name):
        if entry.is_dir():
            non_report_top.append(entry.name + "/")
            continue
        if entry.suffix != ".md":
            non_report_top.append(entry.name)
            continue
        seat = seat_of(entry.name)
        if seat is None:
            unexpected_md.append(entry.name)
            continue
        canon = canonical(seat)
        if canon != seat:
            raw_prefix_anomalies.append({"file": entry.name, "raw": seat, "canonical": canon})
        if canon not in ROSTER:
            unexpected_md.append(entry.name)
            continue
        reports.setdefault(canon, []).append(entry)

    duplicate = {
        seat: [p.name for p in paths]
        for seat, paths in reports.items()
        if len(paths) > 1
    }
    header_mismatches = []
    header_token_misses = []
    tiny = []
    hashed = {}
    for seat, paths in reports.items():
        hashed[seat] = {}
        for p in paths:
            lines = head_lines(p, 20)
            first = lines[0] if lines else ""
            if not first.startswith(f"# {seat}"):
                header_mismatches.append(
                    {"file": p.name, "seat": seat, "first_line": first[:180]}
                )
            blob = "\n".join(lines)
            if not re.search(r"\b" + re.escape(seat) + r"\b", blob):
                header_token_misses.append({"file": p.name, "seat": seat})
            st = p.stat()
            if st.st_size < 80:
                tiny.append({"file": p.name, "bytes": st.st_size})
            hashed[seat][p.name] = {
                "sha256": sha256(p),
                "bytes": st.st_size,
                "mtime": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(st.st_mtime)),
            }

    present = [s for s in ROSTER if s in reports]
    absent = [s for s in ROSTER if s not in reports]
    present_excl_self = [s for s in present if s != SELF]

    pinned = {}
    missing_candidates = []
    for rel in CANDIDATES:
        p = ROOT / rel
        if p.is_file():
            st = p.stat()
            pinned[rel] = {
                "sha256": sha256(p),
                "bytes": st.st_size,
                "mtime": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(st.st_mtime)),
            }
        else:
            missing_candidates.append(rel)

    parent_md = []
    if PARENT_WAVE.exists():
        for p in PARENT_WAVE.rglob("*"):
            if p.is_file():
                parent_md.append(str(p))

    fixture_files = []
    fix = ROOT / "corpus/fixtures/r99-window-lapse"
    if fix.is_dir():
        fixture_files = sorted(
            (
                {
                    "name": x.name,
                    "bytes": x.stat().st_size,
                    "sha256": sha256(x),
                }
                for x in fix.iterdir()
                if x.is_file()
            ),
            key=lambda row: row["name"],
        )

    head = git("rev-parse", "HEAD")
    baseline = git("rev-parse", "4265df5")
    ancestor = subprocess.call(
        ["git", "merge-base", "--is-ancestor", "4265df5", "HEAD"], cwd=ROOT
    ) == 0
    status = subprocess.check_output(
        ["git", "status", "--porcelain=v1"], cwd=ROOT, text=True
    )

    receipt_state = {"exists": RECEIPT.is_file()}
    if RECEIPT.is_file():
        raw = RECEIPT.read_text(encoding="utf-8", errors="replace")
        receipt_state["bytes"] = RECEIPT.stat().st_size
        receipt_state["sha256"] = sha256(RECEIPT)
        try:
            doc = json.loads(raw)
        except json.JSONDecodeError as exc:
            doc = None
            receipt_state["json_error"] = str(exc)
        receipt_state["top_keys"] = sorted(doc) if isinstance(doc, dict) else None
        snap = None
        if isinstance(doc, dict):
            snap = doc.get("collection_snapshot") or doc.get("collection")
            receipt_state["record_owner"] = doc.get("record_owner")
            receipt_state["state"] = doc.get("state")
        receipt_state["snapshot_present_count"] = None
        receipt_state["snapshot_absent_count"] = None
        if isinstance(snap, dict):
            receipt_state["snapshot_keys"] = sorted(snap)
            for key in ("reports_present", "reports_present_incl_self", "reports_present_excl_self"):
                if key in snap:
                    receipt_state["snapshot_present_count"] = snap.get(key)
                    break
            if "reports_absent" in snap and isinstance(snap["reports_absent"], list):
                receipt_state["snapshot_absent_count"] = len(snap["reports_absent"])
            elif "missing" in snap and isinstance(snap["missing"], list):
                receipt_state["snapshot_absent_count"] = len(snap["missing"])
            elif "absent" in snap and isinstance(snap["absent"], list):
                receipt_state["snapshot_absent_count"] = len(snap["absent"])

    return {
        "receipt_snapshot_utc": now,
        "baseline_commit": baseline,
        "head_at_snapshot": head,
        "baseline_is_ancestor_of_head": ancestor,
        "git_status_porcelain": status.splitlines(),
        "roster_expected": 128,
        "reports_present_incl_self": len(present),
        "reports_present_excl_self": len(present_excl_self),
        "present": present,
        "absent": absent,
        "producer_present": [s for s in PRODUCERS if s in reports],
        "producer_absent": [s for s in PRODUCERS if s not in reports],
        "duplicate_report_prefixes": duplicate,
        "header_seat_mismatches_h1": header_mismatches,
        "header_token_misses_first20": header_token_misses,
        "raw_prefix_anomalies": raw_prefix_anomalies,
        "tiny_reports": tiny,
        "unexpected_md_in_seats_dir": unexpected_md,
        "non_report_top_level": non_report_top,
        "parent_tree_files": parent_md,
        "reports": {seat: hashed[seat] for seat in ROSTER if seat in hashed},
        "candidate_revision_pinned": pinned,
        "missing_candidate_paths": missing_candidates,
        "fixture_files": fixture_files,
        "receipt_state": receipt_state,
    }


def snapshot_matches_live(doc: dict, data: dict) -> bool:
    snap = doc.get("collection_snapshot") if isinstance(doc, dict) else None
    if not isinstance(snap, dict):
        return False
    live_present = set(data["present"])
    live_absent = set(data["absent"])
    snap_present = set(snap.get("present") or [])
    snap_absent = set(snap.get("absent") or snap.get("reports_absent") or snap.get("missing") or [])
    if not snap_present and not snap_absent:
        return False
    # A finalized snapshot matches this live roster exactly, including self
    # only if self has already been written.
    return snap_present == live_present and snap_absent == live_absent


def main() -> None:
    data = audit()
    out = SCRATCH / "audit.json"
    out.write_text(json.dumps(data, indent=1) + "\n")
    summary = {
        "snapshot": data["receipt_snapshot_utc"],
        "present_incl_self": data["reports_present_incl_self"],
        "present_excl_self": data["reports_present_excl_self"],
        "absent": data["absent"],
        "producer_absent": data["producer_absent"],
        "missing_candidates": data["missing_candidate_paths"],
        "duplicates": data["duplicate_report_prefixes"],
        "header_mismatches": data["header_seat_mismatches_h1"],
        "header_token_misses": data["header_token_misses_first20"],
        "unexpected_md": data["unexpected_md_in_seats_dir"],
        "tiny": data["tiny_reports"],
        "parent_tree_files": data["parent_tree_files"],
        "fixture_files": [f["name"] for f in data["fixture_files"]],
        "receipt_state": data["receipt_state"],
        "head": data["head_at_snapshot"],
        "baseline_ancestor": data["baseline_is_ancestor_of_head"],
    }
    (SCRATCH / "audit-summary.json").write_text(json.dumps(summary, indent=1) + "\n")
    print(json.dumps(summary, indent=1))

    if "--write-snapshot" not in sys.argv:
        return

    prior = None
    doc = {}
    if RECEIPT.is_file():
        prior_bytes = RECEIPT.read_bytes()
        prior = {
            "sha256": hashlib.sha256(prior_bytes).hexdigest(),
            "bytes": len(prior_bytes),
        }
        try:
            doc = json.loads(prior_bytes)
        except json.JSONDecodeError:
            doc = {"_unparseable_prior": True}
        if isinstance(doc, dict) and snapshot_matches_live(doc, data):
            print("SKIP write: existing collection_snapshot matches live roster")
            return
        preserved = SCRATCH / "prior-receipt.json"
        preserved.write_bytes(prior_bytes)
        prior["preserved_at"] = str(preserved)

    collection = {
        "reports_expected": 128,
        "reports_present": data["reports_present_incl_self"],
        "reports_present_excl_self": data["reports_present_excl_self"],
        "reports_missing": len(data["absent"]),
        "present": data["present"],
        "absent": data["absent"],
        "reports_absent": data["absent"],
        "missing": data["absent"],
        "producer_present": data["producer_present"],
        "producer_absent": data["producer_absent"],
        "duplicate_report_prefixes": data["duplicate_report_prefixes"],
        "header_seat_mismatches": data["header_seat_mismatches_h1"],
        "header_token_misses_first20": data["header_token_misses_first20"],
        "unexpected_md_in_seats_dir": data["unexpected_md_in_seats_dir"],
        "tiny_reports": data["tiny_reports"],
        "parent_tree_files": data["parent_tree_files"],
        "non_report_top_level_count": len(data["non_report_top_level"]),
        "snapshot_utc": data["receipt_snapshot_utc"],
        "snapshot_owner": "V101-presence-final",
        "candidate_revision_pinned_live": {
            rel: meta["sha256"] for rel, meta in data["candidate_revision_pinned"].items()
        },
        "missing_candidate_paths_live": data["missing_candidate_paths"],
        "head_at_snapshot": data["head_at_snapshot"],
        "baseline_commit": data["baseline_commit"],
        "poll_bound": {
            "stall_escape_utc": "2026-10-17T23:13:45-0300",
            "stall_escape_others": 126,
            "stall_escape_missing": ["V34"],
            "note": (
                "try2=90 of the 30-min RESUME2 poll recorded V34 absent. "
                "V34-adjudicator.md landed at 23:14:46, during the post-bound "
                "stability window. The live roster in this object is the "
                "23:15 stable audit, not the 23:13:45 cutoff."
            ),
        },
        "v39_collection_left_untouched": True,
        "v39_collection_reports_present_at_225141": 85,
        "snapshot_note": (
            "collection_snapshot written by V101-presence-final because receipt.json "
            "had no collection_snapshot key. V39's collection object (85 present at "
            "2026-10-17T22:51:41-0300, producer_absent S2/S5, knowledge paths listed "
            "missing) is left untouched and is not the final presence count. "
            "V39 seats[] report_status values are likewise the 22:51 skeleton and "
            "were not rewritten. Absent seats are recorded, never inferred. "
            "agent_id/outcome are not invented. Live hashes in "
            "candidate_revision_pinned_live are from this snapshot, not from V39's "
            "candidate_revision_pinned."
        ),
    }
    if not isinstance(doc, dict):
        doc = {}
    if prior is not None:
        doc["prior_receipt_preserved_by_v101"] = prior
    doc.setdefault("record_type", "round-99-receipt")
    doc.setdefault("round", 99)
    doc.setdefault("requested_model", "xai-oauth/grok-4.7-fast")
    doc.setdefault("requested_seats", 128)
    doc["collection_snapshot"] = collection
    doc["collection_snapshot_finalized_by"] = "V101-presence-final"
    # Do not overwrite V39's collection, candidate_revision_pinned, seats, or state.
    if "seats" not in doc:
        doc["seats"] = [
            {
                "seat": seat,
                "agent_id": None,
                "outcome": None,
                "report_path": (
                    f".ufo/waves/round-99/seats/{next(iter(data['reports'][seat]))}"
                    if seat in data["reports"] else None
                ),
                "report_sha256": (
                    next(iter(data["reports"][seat].values()))["sha256"]
                    if seat in data["reports"] else None
                ),
                "report_status": "present" if seat in data["reports"] else "ABSENT",
            }
            for seat in ROSTER
        ]
        doc["agent_id_note"] = (
            "agent_id/outcome left null; L1 fills them from the AgentSwarm result. "
            "V101 did not invent dispatch ids."
        )
    RECEIPT.write_text(json.dumps(doc, indent=1) + "\n")
    print(f"WROTE {RECEIPT} sha256={sha256(RECEIPT)}")


if __name__ == "__main__":
    main()
