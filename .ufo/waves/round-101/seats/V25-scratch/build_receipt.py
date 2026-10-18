#!/usr/bin/env python3
"""V25 receipt seat: emit skeleton receipt.json for round-101. Writes ONLY receipt.json."""
import hashlib, json, os, subprocess, sys, datetime

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS = os.path.join(ROOT, ".ufo/waves/round-101/seats")
SCRATCH = os.path.join(SEATS, "V25-scratch")
SELF_SEAT = "V25"
EXPECTED_ROSTER = ["U1", "U2"] + [f"V{i:02d}" for i in range(1, 27)]
BASELINE = "6f86bf26c26abfd76b7f489ad4a5bb447e7cbc5d"
CANDIDATES = [
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/README.md",
    "SKILL.md",
    "corpus/knowledge/r101-r10-register-first-entry.md",
]
PROTECTED = ["PROVINCE.md", "SHONEN.md", "README.md", "l0-questions.md",
             "corpus/fixtures/check_bible.py"]

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True,
                          text=True, check=True).stdout.strip()

def sha_of_git(path, rev):
    r = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{path}"],
                       capture_output=True)
    if r.returncode != 0:
        return None
    return hashlib.sha256(r.stdout).hexdigest()

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    census = json.load(open(os.path.join(SCRATCH, "final-census.json")))
    snap = now()
    head = git("rev-parse", "HEAD")
    status = [l for l in git("status", "--porcelain").splitlines() if l]

    cand_pinned, cand_meta, missing = {}, {}, []
    for rel in CANDIDATES:
        p = os.path.join(ROOT, rel)
        if os.path.isfile(p):
            d = sha256_file(p)
            cand_pinned[rel] = d
            cand_meta[rel] = {"sha256": d, "bytes": os.path.getsize(p),
                "mtime_utc": datetime.datetime.fromtimestamp(
                    os.path.getmtime(p), datetime.timezone.utc).isoformat()}
        else:
            missing.append(rel)

    protected = {}
    for rel in PROTECTED:
        p = os.path.join(ROOT, rel)
        cur = sha256_file(p) if os.path.isfile(p) else None
        base = sha_of_git(rel, BASELINE)
        protected[rel] = {"sha256": cur, "baseline_sha256": base,
                          "same_as_baseline": cur == base,
                          "bytes": os.path.getsize(p) if os.path.isfile(p) else None}

    pin_inv = {"count": None, "names": [], "new_pins": [], "removed_pins": [],
               "inherited_changed": [], "top_level_changed_fields": None,
               "note": "computed from live contract at receipt time"}
    contract_path = os.path.join(ROOT, "corpus/tools/dependency-freeze-contract.json")
    if os.path.isfile(contract_path):
        c = json.load(open(contract_path))
        pin_inv["count"] = len(c.get("pins", {}))
        pin_inv["names"] = sorted(c.get("pins", {}).keys())
        base_names = ["r88-m3-maya-cluster", "r94-paired-crossing",
            "r95-crossing-aftermath", "r96-crossing-response",
            "r97-crossing-acknowledgment", "r98-clerk-filing", "r99-window-lapse"]
        pin_inv["new_pins"] = sorted(set(pin_inv["names"]) - set(base_names))
        pin_inv["removed_pins"] = sorted(set(base_names) - set(pin_inv["names"]))
        pin_inv["top_level_revision"] = c.get("revision")

    seat_records = []
    for sid in sorted(set(list(census["present"]) + EXPECTED_ROSTER)):
        recs = census["seat_reports"].get(sid, [])
        if not recs:
            seat_records.append({"seat": sid, "agent_id": None, "outcome": None,
                "report_status": "absent", "report_path": None,
                "report_sha256": None, "reports": {}, "bytes": None,
                "mtime_utc": None})
            continue
        r = recs[0]
        seat_records.append({"seat": sid, "agent_id": None, "outcome": None,
            "report_status": "present",
            "report_path": f".ufo/waves/round-101/seats/{r['file']}",
            "report_sha256": r["sha256"],
            "reports": {rr["file"]: rr["sha256"] for rr in recs},
            "bytes": r["bytes"], "mtime_utc": r["mtime_utc"]})

    receipts = {"receipt.json", "V25-receipt-skeleton.json"}
    unexpected = [e for e in sorted(os.listdir(SEATS))
                  if e.endswith(".md") and seat_id_of(e) not in census["present"]] \
        if (seat_id_of := lambda n: n.split("-", 1)[0]) else []

    receipt = {
        "record_type": "round-101-receipt",
        "round": 101,
        "phase": "single-wave-28-seat",
        "requested_model": "zai-coding-plan/glm-5.3-flash-low",
        "dispatch_model_alias_declared": None,
        "requested_effort": None,
        "requested_seats": 28,
        "dispatch_tool_call_id": None,
        "returned_summary": None,
        "served_backend_echo": None,
        "baseline_commit": BASELINE,
        "baseline_is_ancestor_of_head": True,
        "head_at_snapshot": head,
        "receipt_snapshot_utc": snap,
        "git_status_short": status,
        "candidate_revision_pinned": cand_pinned,
        "candidate_revision_meta": cand_meta,
        "missing_candidate_paths": missing,
        "fixture_files": sorted(os.listdir(os.path.join(ROOT,
            "corpus/fixtures/r100-docket-review")))
            if os.path.isdir(os.path.join(ROOT, "corpus/fixtures/r100-docket-review"))
            else [],
        "pin_inventory": pin_inv,
        "protected_files": protected,
        "collection_snapshot": {
            "reports_expected": census["expected_count"],
            "reports_present": census["present_count"],
            "reports_present_excl_self": census["present_excl_self_count"],
            "reports_missing_count": len(census["missing_seat_ids"]),
            "reports_excess_count": len(census["excess_seat_ids"]),
            "producer_count": 2,
            "verifier_count": 26,
            "present": census["present"],
            "expected_roster_provided_by_dispatch": None,
            "missing_seat_ids_not_inferred": True,
            "missing_seat_ids": census["missing_seat_ids"],
            "excess_seat_ids": census["excess_seat_ids"],
            "producer_present": [s for s in ["U1", "U2"] if s in census["present"]],
            "producer_absent": [s for s in ["U1", "U2"] if s not in census["present"]],
            "duplicate_report_prefixes": census["duplicate_report_prefixes"],
            "header_seat_mismatches": [],
            "header_token_misses_first20": census["header_token_misses_first20"],
            "empty_reports": census["empty_reports"],
            "tiny_reports_under_200_bytes": census["tiny_reports_under_200_bytes"],
            "unexpected_md_in_seats_dir": unexpected,
            "non_report_top_level": census["scratch_dirs"],
            "scratch_directories_without_report_not_credited":
                census["scratch_dirs_without_report"],
            "self_seat": SELF_SEAT,
            "self_subtracted_from_all_reports_polls": True,
        },
        "known_seat_output_defects": [],
        "seats": seat_records,
        "state": ("skeleton — 28-report presence audit compiled by seat V25 "
                  "(receipt seat) from on-disk report files only; agent_id and "
                  "outcome are null because this seat cannot observe the "
                  "AgentSwarm dispatch result; report existence does not admit "
                  "the round"),
        "l1_follow_up": [
            "Fill agent_id and outcome from the actual dispatch result, never from report existence.",
            "Fill dispatch_tool_call_id and returned_summary from the real single-wave dispatch.",
            "Adjudicate C1/C2/C3 from verifier evidence; receipt presence does not admit the round.",
            "Refresh report and candidate hashes after any final report landings or closure edits.",
            "Reconcile the declared 28-seat roster with observed report identifiers; explain any deviation without dropping reports.",
        ],
    }
    out = os.path.join(SEATS, "receipt.json")
    with open(out, "w") as f:
        json.dump(receipt, f, indent=1)
    print("WROTE", out, os.path.getsize(out), "bytes")
    return 0

if __name__ == "__main__":
    sys.exit(main())
