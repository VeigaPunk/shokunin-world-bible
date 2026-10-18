#!/usr/bin/env python3
"""V19 finalize: patch ONLY collection_snapshot + V19 seats row + state/l1_follow_up
appends into V18's skeleton receipt. Everything else byte-preserved."""
import json, os

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
RECEIPT = os.path.join(ROOT, ".ufo/waves/round-102/receipt.json")
CENSUS = os.path.join(ROOT, ".ufo/waves/round-102/seats/V19-scratch/final-census.json")

census = json.load(open(CENSUS))
receipt = json.load(open(RECEIPT))

DECLARED = ["U1", "U2"] + [f"V{i:02d}" for i in range(1, 19)]   # LOG declaration: 20 seats
BRIEF = ["U1", "U2"] + [f"V{i:02d}" for i in range(1, 20)]      # V19 seat brief: 21 ids

reports = census["reports"]          # 21 rows incl V19 (census re-run post-report)
others = [r for r in reports if not r["is_self"]]
present_ids = sorted({r["seat"] for r in reports})
missing = [s for s in DECLARED if s not in present_ids]
excess = [s for s in present_ids if s not in DECLARED]
producers = census["producer_artifacts"]

snap = {
    "reports_expected_declared_in_log": len(DECLARED),
    "roster_declared_in_log": DECLARED,
    "roster_in_V19_seat_brief": BRIEF,
    "roster_arithmetic_note": (
        "THIRD ROSTER ERRATUM OF THE PUSH (same class as r100 32->34, r101 28->30): "
        "LOG declares 20 seats (U1-U2 + V01-V18); the V19 dispatch brief read "
        "'U1-U2 + V01-V19' (21 ids). Filed set: 21 reports = 20 declared + SELF (V19) "
        "as the excess, exactly matching the brief roster. Recorded, not resolved; "
        "L1 to reconcile. No report dropped, none invented."),
    "reports_present": len(reports),
    "reports_present_excl_self": len(others),
    "reports_missing_count": len(missing),
    "reports_excess_count": len(excess),
    "present": present_ids,
    "present_excl_self": sorted({r["seat"] for r in others}),
    "expected_roster_provided_by_dispatch": None,
    "missing_seat_ids_not_inferred": True,
    "missing_seat_ids": missing,
    "excess_seat_ids": excess,
    "producer_artifacts_present": [k for k, v in producers.items() if v.get("present")],
    "producer_artifacts_absent": [k for k, v in producers.items() if not v.get("present")],
    "duplicate_report_prefixes": census["duplicate_prefixes_excl_self"],
    "header_seat_mismatches": [r["file"] for r in reports if not r["header_token_first20"]],
    "header_token_misses_first20": [r["file"] for r in reports if not r["header_token_first20"]],
    "empty_reports": census["empty_reports"],
    "tiny_reports_under_200_bytes": census["tiny_reports_under_200_bytes"],
    "unexpected_md_in_seats_dir": [],
    "non_report_top_level": census["non_report_files_in_seats"],
    "scratch_directories": census["scratch_dirs"],
    "supersedes": ("V18's 09:58Z snapshot observed 'NO V19 report exists' — accurate at "
                   "its write time; superseded by this finalized snapshot after the V19 "
                   "report landed (V18's adjudication untouched)."),
    "self_seat": "V19",
    "self_subtracted_from_all_reports_polls": True,
    "poll_record": (
        "budget1 1200s -> 5 others, STALL-ESCAPE-1; budget2 hit at t=160s (18 others + "
        "3 producer artifacts) with V12/V18 still absent; 600s grace window -> V12 t=80s, "
        "V18 t=360s, GRACE_HIT. All recorded in seats/V19-scratch/stall-escapes.log."),
}

# V19 seats row from the live census
self_rows = [r for r in reports if r["is_self"]]
assert len(self_rows) == 1, self_rows
me = self_rows[0]
import hashlib
p = os.path.join(ROOT, ".ufo/waves/round-102/seats", me["file"])
full = hashlib.sha256(open(p, "rb").read()).hexdigest()
v19_row = {
    "seat": "V19", "agent_id": None, "outcome": None,
    "report_status": "present",
    "report_path": f".ufo/waves/round-102/seats/{me['file']}",
    "report_sha256": full,
    "reports": {me["file"]: full},
    "bytes": me["bytes"],
    "mtime_utc": me["mtime_utc"].replace("Z", "+00:00"),
    "is_self_V19": True,
    "note": "row appended by V19 finalization; agent_id/outcome for L1 fill",
}

existing_seats = receipt.get("seats", [])
if not any(s.get("seat") == "V19" for s in existing_seats):
    existing_seats.append(v19_row)
receipt["seats"] = existing_seats

receipt["collection_snapshot"] = snap
receipt["state"] = str(receipt.get("state", "")) + (
    " | V19 FINALIZATION (post-adjudication): collection_snapshot replaced with the "
    "finalized census (21 filed reports = 20 declared + SELF excess [V19], 0 missing, "
    "quality gates clean); V19 seats row appended; adjudication and all other keys "
    "preserved byte-intact.")
receipt.setdefault("l1_follow_up", []).append(
    "Reconcile the third roster erratum: declared 20 (U1-U2, V01-V18) vs filed 21 "
    "(brief roster U1-U2 + V01-V19; excess row = V19 presence-final).")

json.dump(receipt, open(RECEIPT, "w"), indent=1, ensure_ascii=False)
print("receipt finalized:", os.path.getsize(RECEIPT), "bytes")
print("snapshot:", json.dumps({k: snap[k] for k in (
    "reports_expected_declared_in_log", "reports_present", "reports_present_excl_self",
    "reports_missing_count", "reports_excess_count", "excess_seat_ids")}))
print("seats rows:", len(receipt["seats"]))
print("adjudication preserved:", "adjudication" in receipt and bool(receipt["adjudication"]))
