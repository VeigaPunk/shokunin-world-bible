#!/usr/bin/env python3
"""V36 receipt builder (round 98). Presence audit + skeleton receipt.

Read-only over the lane tree; writes only into V36-scratch/ (byte copies) and,
when invoked with --write-receipt, the receipt path .ufo/waves/round-98/receipt.json.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
PARENT = "/home/vgpnk/Projects/shokunin"
SEATS = os.path.join(LANE, ".ufo/waves/round-98/seats")
RECEIPT = os.path.join(LANE, ".ufo/waves/round-98/receipt.json")
SCRATCH = os.path.join(SEATS, "V36-scratch")
BASELINE = "9a3d648"

ROSTER = ["S%d" % i for i in range(1, 6)] + ["V%02d" % i for i in range(1, 60)]
SELF = "V36"

PIN_PATHS = [
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/README.md",
    "corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md",
    "corpus/knowledge/r98-clerk-scope-note.md",
    "corpus/knowledge/r95-aftermath-scope-note.md",
    "corpus/knowledge/r96-response-scope-note.md",
]
R98_DIR = "corpus/fixtures/r98-clerk-filing"


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def run(cmd, cwd=LANE):
    r = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def collect():
    reports = {}
    dup = {}
    unexpected = []
    for name in sorted(os.listdir(SEATS)):
        p = os.path.join(SEATS, name)
        if not os.path.isfile(p) or not name.endswith(".md"):
            continue
        m = re.match(r"^(S[1-5]|V\d{2})-", name)
        if not m:
            unexpected.append(name)
            continue
        seat = m.group(1)
        if seat not in ROSTER:
            unexpected.append(name)
            continue
        reports.setdefault(seat, []).append(name)
    for seat, names in reports.items():
        if len(names) > 1:
            dup[seat] = names

    header_mismatch = []
    hashes = {}
    for seat, names in sorted(reports.items()):
        for name in names:
            p = os.path.join(SEATS, name)
            hashes[name] = sha256_file(p)
            try:
                first = open(p, encoding="utf-8", errors="replace").readline().strip()
            except OSError:
                first = ""
            if not first.startswith("# " + seat):
                header_mismatch.append({"seat": seat, "file": name, "first_line": first[:120]})

    present = sorted(reports.keys())
    absent = [s for s in ROSTER if s not in reports]

    # parent-tree strays (r94-F01 class)
    _, out, _ = run("find %s/.ufo/waves/round-98 -name '*.md' 2>/dev/null" % PARENT)
    parent_md = [l for l in out.splitlines() if l.strip()]
    _, out2, _ = run(
        "find %s -maxdepth 2 -name 'V[0-9][0-9]-*.md' -o -maxdepth 2 -name 'S[1-5]-*.md' 2>/dev/null" % PARENT
    )
    parent_root_reports = [l for l in out2.splitlines() if l.strip()]

    pins = {}
    missing_pins = []
    for rel in PIN_PATHS:
        p = os.path.join(LANE, rel)
        if os.path.exists(p):
            pins[rel] = sha256_file(p)
        else:
            missing_pins.append(rel)
    if os.path.isdir(os.path.join(LANE, R98_DIR)):
        for name in sorted(os.listdir(os.path.join(LANE, R98_DIR))):
            p = os.path.join(LANE, R98_DIR, name)
            if os.path.isfile(p):
                pins[R98_DIR + "/" + name] = sha256_file(p)

    rc, head, _ = run("git rev-parse HEAD")
    rc2, status, _ = run("git status --short")
    rc3, anc, _ = run("git merge-base --is-ancestor %s HEAD && echo yes" % BASELINE)
    rc4, base_full, _ = run("git rev-parse %s" % BASELINE)

    # prior receipt by another seat
    prior = None
    if os.path.exists(RECEIPT):
        with open(RECEIPT, "rb") as f:
            raw = f.read()
        prior = {
            "path": os.path.relpath(RECEIPT, LANE),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
            "mtime": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(os.path.getmtime(RECEIPT))),
        }
        try:
            pj = json.loads(raw.decode("utf-8"))
            prior["record_type"] = pj.get("record_type")
            prior["collection_reports_present"] = (pj.get("collection") or {}).get("reports_present")
            prior["note"] = (pj.get("collection") or {}).get("note")
            blob = str(prior.get("note") or "") + str(pj.get("state") or "")
            prior["written_by"] = "V36" if "V36" in blob else "other/unknown"
        except Exception as e:  # noqa: BLE001
            prior["parse_error"] = repr(e)
            prior["written_by"] = "unknown"

    return {
        "snapshot_utc": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "head": head,
        "baseline_commit_full": base_full,
        "baseline_ancestor": anc == "yes",
        "git_status": status.splitlines(),
        "present": present,
        "present_count": len(present),
        "present_incl_self": len(present),
        "absent": absent,
        "duplicate_prefixes": dup,
        "unexpected_md": unexpected,
        "header_seat_mismatches": header_mismatch,
        "hashes": hashes,
        "parent_tree_md": parent_md,
        "parent_root_reports": parent_root_reports,
        "pins": pins,
        "missing_pins": missing_pins,
        "prior_receipt": prior,
    }


def build_receipt(snap, state_note):
    seats = []
    for seat in ROSTER:
        entry = {"seat": seat, "agent_id": None, "outcome": None, "reports": {}}
        for name, h in snap["hashes"].items():
            if re.match(r"^%s-" % re.escape(seat), name):
                entry["reports"][name] = h
        if not entry["reports"]:
            entry["reports"] = None
        seats.append(entry)

    collection = {
        "reports_present": snap["present_count"],
        "reports_present_incl_self": snap["present_count"],
        "reports_expected": 64,
        "reports_absent": snap["absent"],
        "misplaced_detected": snap["parent_tree_md"],
        "parent_tree_duplicate_copies": snap["parent_root_reports"],
        "duplicate_report_prefixes": snap["duplicate_prefixes"],
        "header_seat_mismatches": snap["header_seat_mismatches"],
        "unexpected_md_in_seats_dir": snap["unexpected_md"],
        "snapshot_note": (
            "Counts and hashes taken by V36-receipt at %s; V36's own report row is included "
            "when present. Absent seats are recorded, never inferred." % snap["snapshot_utc"]
        ),
    }
    receipt = {
        "record_type": "round-98-receipt",
        "round": 98,
        "phase": "single-wave-64-seat",
        "requested_model": "opencode-go/deepseek-v4.1-flash",
        "requested_seats": 64,
        "dispatch_tool_call_id": None,
        "returned_summary": None,
        "served_backend_echo": None,
        "baseline_commit": snap["baseline_commit_full"],
        "head_at_snapshot": snap["head"],
        "receipt_snapshot_utc": snap["snapshot_utc"],
        "candidate_revision_pinned": snap["pins"],
        "missing_candidate_paths": snap["missing_pins"],
        "collection": collection,
        "known_seat_output_defects": [],
        "seats": seats,
        "state": state_note,
    }
    if snap["prior_receipt"]:
        if snap["prior_receipt"].get("written_by") == "V36":
            receipt["skeleton_superseded"] = snap["prior_receipt"]
        else:
            receipt["prior_receipt_by_other_seat"] = snap["prior_receipt"]
    if snap.get("post_snapshot_edits_observed") is not None:
        receipt["collection"]["post_snapshot_edits_observed"] = snap["post_snapshot_edits_observed"]
    return receipt


def main():
    snap = collect()
    args = sys.argv[1:]
    if "--final" in args:
        refs = sorted(f for f in os.listdir(SCRATCH) if f.startswith("V36-summary-"))
        if refs:
            best = max(refs, key=lambda f: len(json.load(open(os.path.join(SCRATCH, f))).get("hashes", {})))
            ref = json.load(open(os.path.join(SCRATCH, best)))
            edits = []
            for name, h in sorted(ref.get("hashes", {}).items()):
                cur = snap["hashes"].get(name)
                if cur is None:
                    edits.append({"file": name, "state": "vanished", "ref_hash": h})
                elif cur != h:
                    edits.append({"file": name, "ref_hash": h, "final_hash": cur})
            snap["post_snapshot_edits_observed"] = edits
            snap["post_snapshot_ref"] = best
    print(json.dumps({k: v for k, v in snap.items() if k not in ("hashes", "pins")}, indent=1))
    print("pins=%d missing=%s" % (len(snap["pins"]), snap["missing_pins"]))
    if "--summary" in args:
        with open(os.path.join(SCRATCH, "V36-summary-%s.txt" % time.strftime("%H%M%S")), "w") as f:
            f.write(json.dumps(snap, indent=1, sort_keys=True))
    if "--write-receipt" in args:
        prior = snap["prior_receipt"]
        if prior:
            # preserve bytes of a receipt written by another seat
            dst = os.path.join(SCRATCH, "prior-receipt-%s.json" % prior["sha256"][:12])
            if not os.path.exists(dst):
                with open(RECEIPT, "rb") as f:
                    raw = f.read()
                with open(dst, "wb") as f:
                    f.write(raw)
                prior["preserved_byte_copy"] = os.path.relpath(dst, LANE)
                prior["preserved"] = True
            else:
                prior["preserved_byte_copy"] = os.path.relpath(dst, LANE)
                prior["preserved"] = "already"
        note = (
            "Skeleton receipt written by V36 (receipt seat) at %s. agent_id/outcome/"
            "dispatch_tool_call_id/returned_summary left null for the L1 to fill from the "
            "AgentSwarm dispatch result. Presence audit only; V36 judges no claim (C1/C2/C3) "
            "and no axis." % snap["snapshot_utc"]
        )
        receipt = build_receipt(snap, note)
        with open(RECEIPT, "w") as f:
            json.dump(receipt, f, indent=1, sort_keys=False)
            f.write("\n")
        print("wrote", RECEIPT, "present=%d absent=%s" % (snap["present_count"], snap["absent"]))
    if "--copy-report-hashes" in args:
        pass


if __name__ == "__main__":
    main()
