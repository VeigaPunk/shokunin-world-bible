#!/usr/bin/env python3
"""V19 finalize .ufo/waves/round-102/receipt.json (collection_snapshot) from final-census.json."""
import hashlib, json, os, datetime, subprocess

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SCRATCH = os.path.join(ROOT, ".ufo/waves/round-102/seats/V19-scratch")
RECEIPT = os.path.join(ROOT, ".ufo/waves/round-102/receipt.json")

census = json.load(open(os.path.join(SCRATCH, "final-census.json")))

def sha256_full(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()

def meta(p):
    return {"bytes": os.path.getsize(p), "mtime_utc": mtime_utc(p), "sha256": sha256_full(p)}

def mtime_utc(p):
    return datetime.datetime.utcfromtimestamp(os.path.getmtime(p)).isoformat() + "+00:00"

DECLARED = ["U1", "U2"] + [f"V{i:02d}" for i in range(1, 19)]   # LOG declaration: 20 seats
SEAT_BRIEF = ["U1", "U2"] + [f"V{i:02d}" for i in range(1, 20)]  # V19 seat brief: 21 ids (erratum class)

reports = census["reports"]
others = [r for r in reports if not r["is_self"]]
present_ids = sorted({r["seat"] for r in reports})
other_ids = sorted({r["seat"] for r in others})
missing = [s for s in DECLARED if s not in other_ids and s != "V19"]
excess = [s for s in other_ids if s not in DECLARED]
producers = census["producer_artifacts"]
prod_present = [k for k, v in producers.items() if v.get("present")]
prod_absent = [k for k, v in producers.items() if not v.get("present")]

scratch_dirs = census["scratch_dirs"]
report_files = {r["file"] for r in reports}
scratch_no_report = [d for d in scratch_dirs
                     if not any(f.startswith(d.replace("-scratch", "")) for f in report_files)]

seats = []
for r in sorted(reports, key=lambda x: x["seat"]):
    p = os.path.join(ROOT, ".ufo/waves/round-102/seats", r["file"])
    full = sha256_full(p)
    seats.append({
        "seat": r["seat"], "agent_id": None, "outcome": None,
        "report_status": "present",
        "report_path": f".ufo/waves/round-102/seats/{r['file']}",
        "report_sha256": full,
        "reports": {r["file"]: full},
        "bytes": r["bytes"], "mtime_utc": r["mtime_utc"].replace("Z", "+00:00"),
        "is_self_V19": bool(r["is_self"]),
    })

candidate_pin, candidate_meta, missing_paths = {}, {}, []
for rel, v in producers.items():
    if v.get("present"):
        p = os.path.join(ROOT, rel)
        m = meta(p)
        candidate_pin[rel] = m["sha256"]
        candidate_meta[rel] = m
    else:
        missing_paths.append(rel)

protected = {}
for rel in ["PROVINCE.md", "SHONEN.md", "README.md", "l0-questions.md", "corpus/fixtures/check_bible.py"]:
    protected[rel] = sha256_full(os.path.join(ROOT, rel))

pins = {}
contract_path = os.path.join(ROOT, "corpus/tools/dependency-freeze-contract.json")
if os.path.isfile(contract_path):
    c = json.load(open(contract_path))
    pins = {"count": len(c.get("pins", {})), "names": sorted(c.get("pins", {}).keys())}

snap = {
    "reports_expected_declared_in_log": len(DECLARED),
    "roster_declared_in_log": DECLARED,
    "roster_in_V19_seat_brief": SEAT_BRIEF,
    "roster_arithmetic_note": ("seat brief said '2 producers + 18 verifiers, roster U1-U2 + V01-V19' "
                               "= 21 ids vs 20 declared in LOG; V19 brief poll target 18 others "
                               "honored; recorded as the standing roster-erratum class, unresolved here"),
    "reports_present": len(reports),
    "reports_present_excl_self": len(others),
    "reports_missing_count": len(missing),
    "reports_excess_count": len(excess),
    "present": present_ids,
    "present_excl_self": other_ids,
    "expected_roster_provided_by_dispatch": None,
    "missing_seat_ids_not_inferred": True,
    "missing_seat_ids": missing,
    "excess_seat_ids": excess,
    "producer_artifacts_present": prod_present,
    "producer_artifacts_absent": prod_absent,
    "duplicate_report_prefixes": census["duplicate_prefixes_excl_self"],
    "header_seat_mismatches": [r["file"] for r in reports if not r["header_token_first20"]],
    "header_token_misses_first20": [r["file"] for r in reports if not r["header_token_first20"]],
    "empty_reports": census["empty_reports"],
    "tiny_reports_under_200_bytes": census["tiny_reports_under_200_bytes"],
    "unexpected_md_in_seats_dir": [],
    "non_report_top_level": census["non_report_files_in_seats"],
    "scratch_directories": scratch_dirs,
    "scratch_directories_without_report_not_credited": scratch_no_report,
    "self_seat": "V19",
    "self_subtracted_from_all_reports_polls": True,
}

receipt = {
    "record_type": "round-102-receipt",
    "round": 102,
    "phase": "single-wave-20-seat-declared",
    "requested_model": "zai-coding-plan/glm-5.3-flash-low",
    "dispatch_model_alias_declared": None,
    "requested_effort": None,
    "requested_seats": 20,
    "dispatch_tool_call_id": None,
    "returned_summary": None,
    "served_backend_echo": None,
    "baseline_commit": "542021a5e54e86edc441577f93fa639082d02877",
    "baseline_is_ancestor_of_head": census["baseline_542021a_ancestor"],
    "head_at_snapshot": census["head"],
    "receipt_snapshot_utc": datetime.datetime.utcnow().isoformat() + "+00:00",
    "git_status_short": census["git_status_short"],
    "candidate_revision_pinned": candidate_pin,
    "candidate_revision_meta": candidate_meta,
    "missing_candidate_paths": missing_paths,
    "pin_inventory": pins,
    "protected_files": protected,
    "collection_snapshot": snap,
    "known_seat_output_defects": [],
    "seats": seats,
    "state": ("collection_snapshot finalized by V19 (presence-final) from file-level census; "
              "presence is not adjudication — C1/C2/C3 unadjudicated by this seat; "
              "agent_id/outcome/dispatch fields null for L1 fill"),
    "l1_follow_up": [
        "Fill agent_id and outcome from the actual dispatch result, never from report existence.",
        "Fill dispatch_tool_call_id and returned_summary from the real single-wave dispatch.",
        "Adjudicate C1/C2/C3 from verifier evidence; receipt presence does not admit the round.",
        "Reconcile the 20-seat LOG roster (U1-U2, V01-V18) with the V19 seat brief roster (U1-U2, V01-V19) and with observed report identifiers; standing roster-erratum class.",
        "Refresh report and candidate hashes after any final report landings or closure edits.",
    ],
}

with open(RECEIPT, "w") as f:
    json.dump(receipt, f, indent=1, ensure_ascii=False)
print("WROTE", RECEIPT, os.path.getsize(RECEIPT), "bytes")
print(json.dumps(snap, indent=1))
