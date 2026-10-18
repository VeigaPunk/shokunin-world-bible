#!/usr/bin/env python3
"""V71 receipt-audit-2: recompute hashes and counts claimed by V39.

Read-only against corpus and other seats. Writes only under V71-scratch.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SEATS = LANE / ".ufo/waves/round-99/seats"
SCR = SEATS / "V71-scratch"
ROSTER = [f"S{i}" for i in range(1, 6)] + [f"V{i:02d}" for i in range(1, 124)]
PRODUCER_PATHS = [
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
HEX64 = re.compile(r"\b([0-9a-f]{64})\b")


def sha256_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def seat_reports() -> dict[str, list[Path]]:
    found: dict[str, list[Path]] = {s: [] for s in ROSTER}
    unexpected = []
    if not SEATS.is_dir():
        return found
    for p in sorted(SEATS.glob("*.md")):
        m = re.match(r"^(S[1-5]|V\d{2,3})-", p.name)
        if not m:
            unexpected.append(str(p.relative_to(LANE)))
            continue
        seat = m.group(1)
        if seat not in found:
            unexpected.append(str(p.relative_to(LANE)))
            continue
        found[seat].append(p)
    return found


def main() -> int:
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    reports = seat_reports()
    present = [s for s, ps in reports.items() if ps]
    missing = [s for s, ps in reports.items() if not ps]
    dup = {s: [p.name for p in ps] for s, ps in reports.items() if len(ps) > 1}

    v39_paths = reports.get("V39", [])
    v39 = v39_paths[0] if v39_paths else None
    receipt_path = LANE / ".ufo/waves/round-99/receipt.json"

    out: dict = {
        "audited_at": now,
        "v39_report": str(v39) if v39 else None,
        "v39_report_sha256": sha256_file(v39) if v39 else None,
        "v39_bytes": v39.stat().st_size if v39 else None,
        "receipt_path": str(receipt_path) if receipt_path.is_file() else None,
        "receipt_sha256": sha256_file(receipt_path) if receipt_path.is_file() else None,
        "receipt_bytes": receipt_path.stat().st_size if receipt_path.is_file() else None,
        "roster_expected": 128,
        "reports_present_top_level": len(present),
        "reports_missing": missing,
        "duplicate_prefixes": dup,
        "producer_hashes_live": {},
        "producer_missing": [],
        "hash_mismatches": [],
        "count_mismatches": [],
        "flags": [],
        "corrections": [],
    }

    for rel in PRODUCER_PATHS:
        p = LANE / rel
        digest = sha256_file(p)
        if digest is None:
            out["producer_missing"].append(rel)
        else:
            out["producer_hashes_live"][rel] = digest

    # live report hashes
    live_report_hashes = {}
    for seat, ps in reports.items():
        if len(ps) == 1:
            live_report_hashes[seat] = {
                "path": str(ps[0].relative_to(LANE)),
                "sha256": sha256_file(ps[0]),
                "bytes": ps[0].stat().st_size,
            }
    out["live_report_hashes"] = live_report_hashes

    if not receipt_path.is_file():
        out["flags"].append("receipt.json ABSENT")
    else:
        try:
            receipt = json.loads(receipt_path.read_text())
        except json.JSONDecodeError as e:
            out["flags"].append(f"receipt.json not valid JSON: {e}")
            receipt = None
        if isinstance(receipt, dict):
            pinned = receipt.get("candidate_revision_pinned") or {}
            if isinstance(pinned, dict):
                for rel, claimed in pinned.items():
                    live = out["producer_hashes_live"].get(rel)
                    if live is None:
                        # path may be absolute or differently keyed
                        live = sha256_file(LANE / rel) if not Path(rel).is_absolute() else sha256_file(Path(rel))
                    if live is None:
                        out["hash_mismatches"].append({
                            "kind": "pinned-missing",
                            "path": rel,
                            "claimed": claimed,
                            "live": None,
                        })
                    elif str(claimed).lower() != live:
                        out["hash_mismatches"].append({
                            "kind": "pinned-digest",
                            "path": rel,
                            "claimed": claimed,
                            "live": live,
                        })
                for rel, live in out["producer_hashes_live"].items():
                    if rel not in pinned:
                        out["flags"].append(f"live producer path not in candidate_revision_pinned: {rel}")
            snap = receipt.get("collection_snapshot") or {}
            claimed_present = snap.get("reports_present")
            claimed_expected = snap.get("reports_expected")
            claimed_missing = snap.get("reports_missing")
            if claimed_expected is not None and claimed_expected != 128:
                out["count_mismatches"].append({
                    "field": "collection_snapshot.reports_expected",
                    "claimed": claimed_expected,
                    "live": 128,
                })
            if claimed_present is not None and claimed_present != len(present):
                out["count_mismatches"].append({
                    "field": "collection_snapshot.reports_present",
                    "claimed": claimed_present,
                    "live": len(present),
                    "note": "live count is top-level seats/*.md matching roster at audit time; SELF (V71) included if its report exists",
                })
            if isinstance(claimed_missing, int) and claimed_missing != len(missing):
                out["count_mismatches"].append({
                    "field": "collection_snapshot.reports_missing",
                    "claimed": claimed_missing,
                    "live": len(missing),
                })
            if isinstance(claimed_missing, list):
                live_missing_set = set(missing)
                claimed_set = set(claimed_missing)
                if claimed_set != live_missing_set:
                    out["count_mismatches"].append({
                        "field": "collection_snapshot.missing",
                        "claimed_not_live": sorted(claimed_set - live_missing_set),
                        "live_not_claimed": sorted(live_missing_set - claimed_set),
                    })
            seats = receipt.get("seats") or []
            if isinstance(seats, list):
                seen = []
                for row in seats:
                    if not isinstance(row, dict):
                        continue
                    seat = row.get("seat")
                    seen.append(seat)
                    claimed_sha = row.get("report_sha256")
                    claimed_path = row.get("report_path")
                    live = live_report_hashes.get(seat)
                    if claimed_sha and live and claimed_sha != live["sha256"]:
                        out["hash_mismatches"].append({
                            "kind": "report-sha256",
                            "seat": seat,
                            "claimed": claimed_sha,
                            "live": live["sha256"],
                            "claimed_path": claimed_path,
                            "live_path": live["path"],
                        })
                    elif claimed_sha and not live:
                        out["hash_mismatches"].append({
                            "kind": "report-sha256-missing-file",
                            "seat": seat,
                            "claimed": claimed_sha,
                            "claimed_path": claimed_path,
                        })
                    if claimed_path and live and Path(claimed_path).name != Path(live["path"]).name:
                        out["flags"].append(
                            f"path name mismatch {seat}: claimed {claimed_path} live {live['path']}"
                        )
                if len(seats) != 128:
                    out["count_mismatches"].append({
                        "field": "seats.length",
                        "claimed": len(seats),
                        "live_roster": 128,
                    })

    # scan V39 report text for 64-hex hashes and compare to known live hashes
    quoted_hash_checks = []
    if v39:
        text = v39.read_text(errors="replace")
        known = {}
        for rel, digest in out["producer_hashes_live"].items():
            known[digest] = rel
        for seat, info in live_report_hashes.items():
            known[info["sha256"]] = info["path"]
        # also index by filename mentioned near a hash is too fuzzy; record unknown hashes
        for m in HEX64.finditer(text):
            digest = m.group(1)
            # skip if it is a git-looking short? no, 64 only
            quoted_hash_checks.append(digest)
        unknown = []
        known_hits = []
        for digest in sorted(set(quoted_hash_checks)):
            if digest in known:
                known_hits.append({"sha256": digest, "matches": known[digest]})
            else:
                # recompute against any path mentioned in a window? leave unknown for manual
                unknown.append(digest)
        out["v39_quoted_sha256_count"] = len(set(quoted_hash_checks))
        out["v39_quoted_sha256_matched_live"] = known_hits
        out["v39_quoted_sha256_unmatched"] = unknown

    # declared round counts to recompute if tools are stable enough — recorded separately by shell
    out["summary"] = {
        "hash_mismatch_count": len(out["hash_mismatches"]),
        "count_mismatch_count": len(out["count_mismatches"]),
        "flag_count": len(out["flags"]),
        "producer_missing_count": len(out["producer_missing"]),
        "reports_present": len(present),
        "reports_missing": len(missing),
    }
    dest = SCR / "audit-result.json"
    dest.write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out["summary"], indent=1))
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
