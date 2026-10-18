#!/usr/bin/env python3
"""V58 presence-final: 64-report audit + receipt skeleton for round 96.

Run from lane root. Writes receipt.json to .ufo/waves/round-96/receipt.json
(assigned to this seat per seat spec: 'finalize receipt.json collection_snapshot
(agent_id left for L1)'). agent_id/outcome left null everywhere.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS = os.path.join(LANE, ".ufo/waves/round-96/seats")
RECEIPT = os.path.join(LANE, ".ufo/waves/round-96/receipt.json")
SELF = "V58-presence-final.md"

EXPECTED = [f"Q{i}" for i in range(1, 7)] + [f"V{i:02d}" for i in range(1, 59)]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    names = sorted(os.listdir(SEATS))
    reports = [n for n in names if re.match(r"^(Q[1-6]|V\d{2})-.*\.md$", n) and os.path.isfile(os.path.join(SEATS, n))]
    by_prefix = {}
    dupes = {}
    for n in reports:
        p = n.split("-", 1)[0]
        by_prefix.setdefault(p, []).append(n)
        if len(by_prefix[p]) > 1:
            dupes[p] = by_prefix[p]

    headers = {}
    mismatches = []
    for n in reports:
        p = n.split("-", 1)[0]
        with open(os.path.join(SEATS, n), encoding="utf-8", errors="replace") as f:
            first = f.readline().strip()
        headers[n] = first
        if not re.match(r"^#\s+" + re.escape(p) + r"\b", first):
            mismatches.append({"file": n, "line1": first[:120]})

    present = set(by_prefix)
    missing = [s for s in EXPECTED if s not in present]
    unexpected = sorted(p for p in present if p not in EXPECTED)

    rows = []
    for s in EXPECTED:
        files = by_prefix.get(s, [])
        rows.append({
            "seat": s,
            "agent_id": None,
            "outcome": None,
            "reports": {f: sha256(os.path.join(SEATS, f)) for f in files},
        })

    # producer artifacts (declared byte-ownership)
    artifacts = {
        "Q1": ["corpus/tools/map_obligations.py"],
        "Q2": ["corpus/tools/map-obligations-contract.json", "corpus/tools/README.md"],
        "Q3": ["corpus/tools/dependency_freeze.py", "corpus/tools/dependency-freeze-contract.json"],
        "Q4": [
            "corpus/fixtures/r96-crossing-response/entities.json",
            "corpus/fixtures/r96-crossing-response/relations.json",
            "corpus/fixtures/r96-crossing-response/contradictions.json",
            "corpus/fixtures/r96-crossing-response/inspiration-note.md",
            "corpus/fixtures/r96-crossing-response/source-excerpt.md",
            "corpus/fixtures/r96-crossing-response/sources.json",
            "corpus/fixtures/r96-crossing-response/timeline.json",
            "corpus/fixtures/r96-crossing-response/fictional-excerpts.md",
        ],
        "Q5": [
            "corpus/fixtures/r96-crossing-response/README.md",
            "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md",
        ],
        "Q6": ["corpus/knowledge/r96-response-scope-note.md"],
    }
    artifact_state = {}
    pinned = {}
    for seat, paths in artifacts.items():
        artifact_state[seat] = {}
        for p in paths:
            full = os.path.join(LANE, p)
            exists = os.path.isfile(full)
            artifact_state[seat][p] = {
                "exists": exists,
                "bytes": os.path.getsize(full) if exists else None,
                "sha256": sha256(full) if exists else None,
            }
            if exists:
                pinned[p] = artifact_state[seat][p]["sha256"]

    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=LANE, capture_output=True, text=True).stdout.strip()
    status = subprocess.run(["git", "status", "--porcelain"], cwd=LANE, capture_output=True, text=True).stdout

    poll_log = os.path.join(SEATS, "V58-scratch", "poll.log")
    curve = []
    if os.path.isfile(poll_log):
        with open(poll_log) as f:
            curve = [ln.strip() for ln in f if ln.strip()][:400]

    collection = {
        "reports_present": len([r for r in reports if r != SELF]),
        "reports_present_incl_self": len(reports),
        "reports_expected": 64,
        "reports_absent": missing,
        "unexpected_report_prefixes": unexpected,
        "duplicate_report_prefixes": dupes,
        "header_seat_mismatches": mismatches,
        "snapshot_note": (
            "Counts and hashes taken by V58-presence-final at the final snapshot; "
            "V58's own report row is included (hash of the file as written). "
            "agent_id/outcome left null for L1 to fill from the real dispatch result."
        ),
    }
    prior = None
    if os.path.isfile(RECEIPT):
        with open(RECEIPT) as f:
            prior = json.load(f)
        prior = {
            "preserved_from": RECEIPT,
            "preserved_by": "V58-presence-final (double-assignment disclosure; r95 V33/V59 class)",
            "record_owner": prior.get("record_owner"),
            "collection": prior.get("collection") or prior.get("collection_snapshot"),
            "sha256_of_preserved_bytes": sha256(RECEIPT),
        }
    receipt = {
        "record_type": "round-96-receipt",
        "record_owner": "V58-presence-final",
        "round": 96,
        "phase": "single-wave-64-seat",
        "requested_model": "opencode-go/deepseek-v4.1-flash",
        "requested_seats": 64,
        "dispatch_tool_call_id": None,
        "returned_summary": None,
        "served_backend_echo": None,
        "baseline_commit": "dcb2d928f53f35673744feaf114e3ac65e3d25ca",
        "lane_head_at_snapshot": head,
        "candidate_revision_pinned": pinned,
        "collection": collection,
        "producer_artifacts": artifact_state,
        "known_seat_output_defects": [
            {"seat": "unfilled", "detail": "L1 to fill from real dispatch result; agent_id/outcome null by construction."}
        ],
        "collection_curve": curve,
        "lane_status_porcelain_at_snapshot": status.splitlines(),
        "seats": rows,
    }
    if prior is not None:
        receipt["prior_receipt_preserved"] = prior
    if "--write" in sys.argv:
        with open(RECEIPT, "w") as f:
            json.dump(receipt, f, indent=1)
    print(json.dumps({
        "reports_present_excl_self": collection["reports_present"],
        "reports_present_incl_self": collection["reports_present_incl_self"],
        "missing": missing,
        "dupes": dupes,
        "mismatches": mismatches,
        "unexpected": unexpected,
        "artifact_missing": {
            s: [p for p, v in d.items() if not v["exists"]] for s, d in artifact_state.items()
        },
        "receipt_written": "--write" in sys.argv,
        "receipt": RECEIPT,
    }, indent=1))


if __name__ == "__main__":
    sys.exit(main())
