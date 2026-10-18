#!/usr/bin/env python3
"""V58 presence-final: 64-report audit + receipt finalization for round 97.

Roster: R1-R6 (producers) + V01-V58 (verifiers) = 64 seats.
Run from anywhere; all paths absolute. --write writes
.ufo/waves/round-97/receipt.json (assigned to this seat per seat spec:
'finalize receipt.json collection_snapshot (agent_id for L1)').
agent_id/outcome left null on every seat row for L1.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS = os.path.join(LANE, ".ufo/waves/round-97/seats")
RECEIPT = os.path.join(LANE, ".ufo/waves/round-97/receipt.json")
SELF = "V58-presence-final.md"
BASELINE = "f3e09f93ce9f2b047eb2b2089bf7b1c03d74a40f"

EXPECTED = [f"R{i}" for i in range(1, 7)] + [f"V{i:02d}" for i in range(1, 59)]

# producer artifacts (declared byte-ownership, r97 LOG declaration)
ARTIFACTS = {
    "R1": ["corpus/tools/map_obligations.py"],
    "R2": ["corpus/tools/map-obligations-contract.json", "corpus/tools/README.md"],
    "R3": ["corpus/tools/dependency_freeze.py", "corpus/tools/dependency-freeze-contract.json"],
    "R4": [
        "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md",
        "corpus/fixtures/r97-crossing-acknowledgment/entities.json",
        "corpus/fixtures/r97-crossing-acknowledgment/relations.json",
        "corpus/fixtures/r97-crossing-acknowledgment/contradictions.json",
        "corpus/fixtures/r97-crossing-acknowledgment/inspiration-note.md",
        "corpus/fixtures/r97-crossing-acknowledgment/source-excerpt.md",
        "corpus/fixtures/r97-crossing-acknowledgment/sources.json",
        "corpus/fixtures/r97-crossing-acknowledgment/timeline.json",
        "corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md",
    ],
    "R5": [
        "corpus/fixtures/r97-crossing-acknowledgment/README.md",
        "corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md",
    ],
    "R6": ["corpus/knowledge/r97-acknowledgment-scope-note.md"],
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    names = sorted(os.listdir(SEATS))
    report_re = re.compile(r"^(R[1-6]|V\d{2})-.*\.md$")
    reports = [
        n for n in names
        if report_re.match(n) and os.path.isfile(os.path.join(SEATS, n))
    ]
    md_all = [n for n in names if n.endswith(".md") and os.path.isfile(os.path.join(SEATS, n))]
    unexpected_md = sorted(n for n in md_all if not report_re.match(n))

    by_prefix = {}
    dupes = {}
    for n in reports:
        p = n.split("-", 1)[0]
        by_prefix.setdefault(p, []).append(n)
        if len(by_prefix[p]) > 1:
            dupes[p] = by_prefix[p]

    mismatches1 = []
    mismatches5 = []
    for n in reports:
        p = n.split("-", 1)[0]
        with open(os.path.join(SEATS, n), encoding="utf-8", errors="replace") as f:
            lines = [next(f, "") for _ in range(5)]
        if not re.match(r"^#\s+" + re.escape(p) + r"\b", lines[0].strip()):
            mismatches1.append({"file": n, "line1": lines[0].strip()[:120]})
        if not any(re.match(r"^#\s+" + re.escape(p) + r"\b", l.strip()) for l in lines):
            mismatches5.append(n)

    present = set(by_prefix)
    missing = [s for s in EXPECTED if s not in present]
    unexpected_prefixes = sorted(p for p in present if p not in EXPECTED)

    rows = []
    for s in EXPECTED:
        files = by_prefix.get(s, [])
        rows.append({
            "seat": s,
            "agent_id": None,
            "outcome": None,
            "reports": {f: sha256(os.path.join(SEATS, f)) for f in files},
        })

    artifact_state = {}
    pinned = {}
    for seat, paths in ARTIFACTS.items():
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

    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=LANE,
                          capture_output=True, text=True).stdout.strip()
    ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", BASELINE, head],
                              cwd=LANE, capture_output=True, text=True).returncode == 0
    status = subprocess.run(["git", "status", "--porcelain"], cwd=LANE,
                            capture_output=True, text=True).stdout

    curve = []
    curve_log = os.path.join(SEATS, "V58-scratch", "collection-curve.txt")
    if os.path.isfile(curve_log):
        with open(curve_log) as f:
            curve = [ln.strip() for ln in f if ln.strip()]

    now = datetime.now(timezone(timedelta(hours=-3)))
    snapshot_utc = now.strftime("%Y-%m-%dT%H:%M:%S%z")

    collection = {
        "reports_present": len([r for r in reports if r != SELF]),
        "reports_present_incl_self": len(reports),
        "reports_expected": 64,
        "reports_absent": missing,
        "unexpected_report_prefixes": unexpected_prefixes,
        "unexpected_md_in_seats_dir": unexpected_md,
        "duplicate_report_prefixes": dupes,
        "header_seat_mismatches_line1": mismatches1,
        "header_seat_mismatches_first5": mismatches5,
        "snapshot_note": (
            "Counts and hashes taken by V58-presence-final at the final snapshot; "
            "V58's own report row is included (hash of the file as written at snapshot time). "
            "agent_id/outcome left null for L1 to fill from the real AgentSwarm dispatch result."
        ),
    }

    prior = None
    if os.path.isfile(RECEIPT):
        with open(RECEIPT) as f:
            prior_raw = f.read()
        try:
            prior_json = json.loads(prior_raw)
        except Exception:
            prior_json = None
        prior = {
            "preserved_from": RECEIPT,
            "preserved_by": "V58-presence-final",
            "sha256_of_preserved_bytes": sha256(RECEIPT),
            "record_owner": (prior_json or {}).get("record_owner"),
            "collection": (prior_json or {}).get("collection")
            or (prior_json or {}).get("collection_snapshot"),
        }

    receipt = {
        "record_type": "round-97-receipt",
        "record_owner": "V58-presence-final",
        "round": 97,
        "phase": "single-wave-64-seat",
        "requested_model": "opencode-go/deepseek-v4.1-flash",
        "requested_seats": 64,
        "dispatch_tool_call_id": None,
        "returned_summary": None,
        "served_backend_echo": None,
        "baseline_commit": BASELINE,
        "baseline_is_ancestor_of_head": ancestor,
        "head_at_snapshot": head,
        "receipt_snapshot_utc": snapshot_utc,
        "candidate_revision_pinned": pinned,
        "collection": collection,
        "collection_snapshot": collection,
        "producer_artifacts": artifact_state,
        "agent_id_note": (
            "agent_id/outcome are null on every seat row; the integrator (L1) fills them from "
            "the real AgentSwarm dispatch result. dispatch_tool_call_id/returned_summary/"
            "served_backend_echo likewise left null; none invented. "
            "collection and collection_snapshot are identical alias objects (r94/r95 named it "
            "collection_snapshot; r96 receipt named it collection)."
        ),
        "known_seat_output_defects": [],
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
        "unexpected_prefixes": unexpected_prefixes,
        "unexpected_md": unexpected_md,
        "dupes": dupes,
        "mismatches1": mismatches1,
        "mismatches5": mismatches5,
        "artifacts_missing": {
            s: [p for p, v in d.items() if not v["exists"]]
            for s, d in artifact_state.items()
        },
        "head": head,
        "baseline_ancestor": ancestor,
        "prior_receipt": prior is not None,
        "receipt_written": "--write" in sys.argv,
    }, indent=1))


if __name__ == "__main__":
    sys.exit(main())
