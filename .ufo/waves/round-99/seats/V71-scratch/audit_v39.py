#!/usr/bin/env python3
"""Independent recompute of V39 receipt hashes and counts. Read-only outside scratch."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
WAVE = LANE / ".ufo/waves/round-99"
SEATS = WAVE / "seats"
RECEIPT = WAVE / "receipt.json"
REPORT = SEATS / "V39-receipt.md"
AUDIT = SEATS / "V39-scratch/audit.json"
OUT = SEATS / "V71-scratch/audit-result.json"
ROSTER = [f"S{i}" for i in range(1, 6)] + [f"V{i:02d}" for i in range(1, 124)]
PREFIX = re.compile(r"^(S[1-5]|V\d+)")
TABLE_ROW = re.compile(
    r"^\| (S\d|V\d+) \| ([^|]+) \| (\d+) \| `([0-9a-f]{64})` \|$"
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def mtime_iso(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime).astimezone().isoformat(timespec="seconds")


def live_reports() -> dict[str, list[Path]]:
    found: dict[str, list[Path]] = {}
    unexpected = []
    for p in sorted(SEATS.glob("*.md")):
        m = PREFIX.match(p.name)
        seat = m.group(1) if m else None
        if seat not in ROSTER:
            unexpected.append(p.name)
            continue
        found.setdefault(seat, []).append(p)
    return found


def main() -> None:
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    receipt = json.loads(RECEIPT.read_text())
    report_text = REPORT.read_text()
    audit = json.loads(AUDIT.read_text()) if AUDIT.is_file() else None
    live = live_reports()
    flags = []
    corrections = []
    hash_ok = []
    hash_bad = []

    coll = receipt["collection"]
    seats = receipt["seats"]
    present_list = coll["present"]
    absent_list = coll["absent"]

    # internal count consistency
    counts = {
        "roster": len(ROSTER),
        "seats_rows": len(seats),
        "reports_expected": coll["reports_expected"],
        "reports_present": coll["reports_present"],
        "present_len": len(present_list),
        "reports_present_excl_self": coll["reports_present_excl_self"],
        "reports_absent_count": coll["reports_absent_count"],
        "absent_len": len(absent_list),
        "present_plus_absent": len(present_list) + len(absent_list),
        "seat_status_present": sum(1 for s in seats if s.get("report_status") == "present"),
        "seat_status_absent": sum(1 for s in seats if s.get("report_status") == "absent"),
        "seat_with_sha": sum(1 for s in seats if s.get("report_sha256")),
    }
    if counts["seats_rows"] != 128:
        flags.append(f"seats rows {counts['seats_rows']} != 128")
    if counts["reports_expected"] != 128:
        flags.append(f"reports_expected {counts['reports_expected']} != 128")
    if counts["reports_present"] != counts["present_len"]:
        flags.append(
            f"reports_present {counts['reports_present']} != len(present) {counts['present_len']}"
        )
    if counts["reports_absent_count"] != counts["absent_len"]:
        flags.append(
            f"reports_absent_count {counts['reports_absent_count']} != len(absent) {counts['absent_len']}"
        )
    if counts["present_plus_absent"] != 128:
        flags.append(f"present+absent {counts['present_plus_absent']} != 128")
    if set(present_list) & set(absent_list):
        flags.append(f"overlap {sorted(set(present_list) & set(absent_list))}")
    if set(present_list) | set(absent_list) != set(ROSTER):
        flags.append("present|absent != roster")
    if "V39" not in present_list:
        flags.append("V39 missing from present list")
    if counts["reports_present_excl_self"] != counts["reports_present"] - (1 if "V39" in present_list else 0):
        flags.append(
            f"excl_self {counts['reports_present_excl_self']} inconsistent with present"
        )
    if counts["seat_status_present"] != counts["reports_present"]:
        flags.append(
            f"seat_status_present {counts['seat_status_present']} != reports_present {counts['reports_present']}"
        )
    if counts["seat_with_sha"] != counts["reports_present"]:
        flags.append(
            f"rows with sha {counts['seat_with_sha']} != reports_present {counts['reports_present']}"
        )

    by_seat = {s["seat"]: s for s in seats}
    if list(by_seat) != [s["seat"] for s in seats]:
        flags.append("duplicate seat keys in seats[]")
    if set(by_seat) != set(ROSTER):
        flags.append(f"seats[] roster mismatch missing={sorted(set(ROSTER)-set(by_seat))} extra={sorted(set(by_seat)-set(ROSTER))}")

    prod_present = coll["producer_present"]
    prod_absent = coll["producer_absent"]
    if prod_present != [s for s in ["S1", "S2", "S3", "S4", "S5"] if s in present_list]:
        flags.append(f"producer_present {prod_present} != derived {[s for s in ['S1','S2','S3','S4','S5'] if s in present_list]}")
    if prod_absent != [s for s in ["S1", "S2", "S3", "S4", "S5"] if s in absent_list]:
        flags.append(f"producer_absent {prod_absent} != derived")

    # hash each claimed present report
    snap = receipt["receipt_snapshot_utc"]
    for seat in present_list:
        row = by_seat[seat]
        rel = row.get("report_path")
        claimed = row.get("report_sha256")
        claimed_bytes = row.get("bytes")
        claimed_mtime = row.get("mtime")
        reports_map = row.get("reports") or {}
        path = LANE / rel if rel else None
        if path is None or not path.is_file():
            hash_bad.append({
                "kind": "missing-file",
                "seat": seat,
                "claimed_path": rel,
                "claimed_sha256": claimed,
            })
            corrections.append({
                "seat": seat,
                "issue": "receipt names a report path that is not a file now",
                "claimed_sha256": claimed,
                "live_sha256": None,
            })
            continue
        live_sha = sha256(path)
        live_bytes = path.stat().st_size
        live_mtime = mtime_iso(path)
        map_name = path.name
        map_sha = reports_map.get(map_name)
        rec = {
            "seat": seat,
            "path": rel,
            "claimed_sha256": claimed,
            "live_sha256": live_sha,
            "claimed_bytes": claimed_bytes,
            "live_bytes": live_bytes,
            "claimed_mtime": claimed_mtime,
            "live_mtime": live_mtime,
            "reports_map_sha": map_sha,
            "match": live_sha == claimed and live_bytes == claimed_bytes and map_sha == claimed,
        }
        if rec["match"]:
            hash_ok.append(seat)
        else:
            hash_bad.append(rec)
            # post-snapshot rewrite is a staleness flag, not an arithmetic error, if mtime is after snapshot
            after = live_mtime > snap
            corrections.append({
                "seat": seat,
                "issue": "post-snapshot rewrite" if after and live_sha != claimed else "hash/bytes/map mismatch",
                "claimed_sha256": claimed,
                "live_sha256": live_sha,
                "claimed_bytes": claimed_bytes,
                "live_bytes": live_bytes,
                "claimed_mtime": claimed_mtime,
                "live_mtime": live_mtime,
                "reports_map_sha": map_sha,
                "snapshot": snap,
            })

    # seats claimed absent but file exists now
    late = []
    for seat in absent_list:
        paths = live.get(seat, [])
        if paths:
            late.append({
                "seat": seat,
                "files": [p.name for p in paths],
                "sha256": sha256(paths[0]) if len(paths) == 1 else None,
                "bytes": paths[0].stat().st_size if len(paths) == 1 else None,
                "mtime": mtime_iso(paths[0]) if len(paths) == 1 else None,
            })

    # markdown table vs current and vs audit.json
    table = []
    for line in report_text.splitlines():
        m = TABLE_ROW.match(line.strip())
        if m:
            table.append({
                "seat": m.group(1),
                "file": m.group(2).strip(),
                "bytes": int(m.group(3)),
                "sha256": m.group(4),
            })
    table_checks = []
    audit_reports = (audit or {}).get("reports") or {}
    for row in table:
        path = SEATS / row["file"]
        live_sha = sha256(path) if path.is_file() else None
        live_bytes = path.stat().st_size if path.is_file() else None
        live_mtime = mtime_iso(path) if path.is_file() else None
        audit_entry = (audit_reports.get(row["seat"]) or {}).get(row["file"])
        table_checks.append({
            "seat": row["seat"],
            "file": row["file"],
            "claimed_sha256": row["sha256"],
            "claimed_bytes": row["bytes"],
            "live_sha256": live_sha,
            "live_bytes": live_bytes,
            "live_mtime": live_mtime,
            "live_match": live_sha == row["sha256"] and live_bytes == row["bytes"],
            "audit_json_sha256": None if not audit_entry else audit_entry.get("sha256"),
            "audit_json_bytes": None if not audit_entry else audit_entry.get("bytes"),
            "audit_json_match": (
                None if not audit_entry else
                audit_entry.get("sha256") == row["sha256"] and audit_entry.get("bytes") == row["bytes"]
            ),
            "unchanged_since_2222": live_mtime is not None and live_mtime <= "2026-10-17T22:22:17-03:00",
        })

    # pinned hashes
    pin_checks = []
    pinned = receipt.get("candidate_revision_pinned") or {}
    meta = receipt.get("candidate_revision_meta") or {}
    for rel, claimed in pinned.items():
        path = LANE / rel
        live_sha = sha256(path) if path.is_file() else None
        meta_row = meta.get(rel) or {}
        pin_checks.append({
            "path": rel,
            "claimed": claimed,
            "live": live_sha,
            "match_now": live_sha == claimed,
            "meta_sha": meta_row.get("sha256"),
            "meta_match": meta_row.get("sha256") == claimed,
            "meta_bytes": meta_row.get("bytes"),
            "live_bytes": path.stat().st_size if path.is_file() else None,
            "live_mtime": mtime_iso(path) if path.is_file() else None,
            "meta_mtime": meta_row.get("mtime"),
        })
    missing_claimed = receipt.get("missing_candidate_paths") or []
    missing_now = []
    for rel in [
        "corpus/knowledge/r99-gate-blind-spot-table.md",
        "corpus/knowledge/r99-lapse-scope-note.md",
    ]:
        missing_now.append({"path": rel, "exists_now": (LANE / rel).is_file()})

    # V39 self hash
    v39_row = by_seat.get("V39") or {}
    v39_live = sha256(REPORT)
    v39_check = {
        "claimed": v39_row.get("report_sha256"),
        "live": v39_live,
        "match": v39_row.get("report_sha256") == v39_live,
        "claimed_bytes": v39_row.get("bytes"),
        "live_bytes": REPORT.stat().st_size,
        "report_does_not_quote_own_receipt_sha": "5d74851756c407864643281eb3b738d5a0fad00ea3052a1d39a615a0ddc205c7" not in report_text,
    }

    # report prose counts
    prose = {
        "says_15_other": "15 other reports hashed" in report_text or "15/128" in report_text,
        "table_rows": len(table),
        "says_113_absent": "113 absent" in report_text,
        "says_S1_S2_S5_absent": "S1, S2, and S5" in report_text or "S1, S2, S5" in report_text,
    }

    # pre-receipt audit list vs table
    pre = coll.get("pre_receipt_present") or []
    table_seats = [r["seat"] for r in table]
    pre_vs_table = {
        "pre_len": len(pre),
        "table_len": len(table_seats),
        "pre_not_table": sorted(set(pre) - set(table_seats)),
        "table_not_pre": sorted(set(table_seats) - set(pre)),
    }

    changed = coll.get("changed_since_pre_receipt_audit") or []

    # git status claimed lines still true?
    status = subprocess.check_output(["git", "status", "--porcelain=v1"], cwd=LANE, text=True).splitlines()
    claimed_status = receipt.get("git_status_short") or []
    status_check = []
    for line in claimed_status:
        status_check.append({"line": line, "present_now": line in status})

    # duplicate prefixes now
    dups_now = {s: [p.name for p in ps] for s, ps in live.items() if len(ps) > 1}

    # header check for receipt-present files
    header_bad = []
    for seat in present_list:
        row = by_seat[seat]
        rel = row.get("report_path")
        if not rel:
            continue
        path = LANE / rel
        if not path.is_file():
            continue
        first = path.read_text(errors="replace").splitlines()[0] if path.stat().st_size else ""
        if not first.startswith(f"# {seat}"):
            header_bad.append({"seat": seat, "first": first[:160]})

    result = {
        "audited_at": now,
        "receipt_sha256": sha256(RECEIPT),
        "receipt_bytes": RECEIPT.stat().st_size,
        "receipt_mtime": mtime_iso(RECEIPT),
        "receipt_snapshot_utc": snap,
        "v39_report_sha256": v39_live,
        "counts": counts,
        "count_flags": flags,
        "hash_ok_seats": hash_ok,
        "hash_ok_count": len(hash_ok),
        "hash_bad": hash_bad,
        "late_landings_after_receipt_absent_list": late,
        "late_count": len(late),
        "live_present_now": sorted(live),
        "live_present_now_count": len(live),
        "dups_now": dups_now,
        "header_bad_on_receipt_present": header_bad,
        "table_checks": table_checks,
        "table_live_mismatch": [r for r in table_checks if not r["live_match"]],
        "table_audit_json_mismatch": [r for r in table_checks if r["audit_json_match"] is not True],
        "pin_checks": pin_checks,
        "pin_mismatch_now": [r for r in pin_checks if not r["match_now"] or not r["meta_match"]],
        "missing_claimed": missing_claimed,
        "missing_now": missing_now,
        "v39_check": v39_check,
        "prose": prose,
        "pre_vs_table": pre_vs_table,
        "changed_since_pre_len": len(changed),
        "status_check": status_check,
        "producer_present": prod_present,
        "producer_absent": prod_absent,
    }
    OUT.write_text(json.dumps(result, indent=1) + "\n")
    summary = {
        "count_flags": flags,
        "hash_ok": len(hash_ok),
        "hash_bad": len(hash_bad),
        "late": len(late),
        "table_rows": len(table),
        "table_live_mismatch": len(result["table_live_mismatch"]),
        "table_audit_json_mismatch": len(result["table_audit_json_mismatch"]),
        "pin_mismatch_now": len(result["pin_mismatch_now"]),
        "v39_self_match": v39_check["match"],
        "header_bad": len(header_bad),
        "live_present_now": len(live),
        "receipt_present": counts["reports_present"],
    }
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
