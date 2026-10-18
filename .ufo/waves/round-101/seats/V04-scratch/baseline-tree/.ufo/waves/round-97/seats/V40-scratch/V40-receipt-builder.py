#!/usr/bin/env python3
"""V40 receipt seat — round-97 presence audit + receipt skeleton builder.

Modes:
  --summary : print human-readable audit + per-report sha256
  --write   : write .ufo/waves/round-97/receipt.json (skeleton, agent_id null)
"""
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
LANE = os.path.join(ROOT, ".ufo/waves/round-97/seats")
PARENT_WAVE = "/home/vgpnk/Projects/shokunin/.ufo/waves/round-97"
RECEIPT = os.path.join(ROOT, ".ufo/waves/round-97/receipt.json")

ROSTER = [f"R{i}" for i in range(1, 7)] + [f"V{i:02d}" for i in range(1, 59)]
REPORT_RE = re.compile(r"^(R[1-6]|V[0-9]{2})-.*\.md$")

PINNED_PATHS = [
    "corpus/tools/map_obligations.py",
    "corpus/tools/map-obligations-contract.json",
    "corpus/tools/README.md",
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/fixtures/r96-crossing-response/entities.json",
    "corpus/fixtures/r96-crossing-response/relations.json",
    "corpus/fixtures/r96-crossing-response/contradictions.json",
    "corpus/fixtures/r96-crossing-response/timeline.json",
    "corpus/fixtures/r96-crossing-response/sources.json",
    "corpus/fixtures/r96-crossing-response/inspiration-note.md",
    "corpus/fixtures/r96-crossing-response/source-excerpt.md",
    "corpus/fixtures/r96-crossing-response/fictional-excerpts.md",
    "corpus/fixtures/r96-crossing-response/README.md",
    "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md",
    "corpus/fixtures/r97-crossing-acknowledgment/entities.json",
    "corpus/fixtures/r97-crossing-acknowledgment/relations.json",
    "corpus/fixtures/r97-crossing-acknowledgment/contradictions.json",
    "corpus/fixtures/r97-crossing-acknowledgment/timeline.json",
    "corpus/fixtures/r97-crossing-acknowledgment/sources.json",
    "corpus/fixtures/r97-crossing-acknowledgment/inspiration-note.md",
    "corpus/fixtures/r97-crossing-acknowledgment/source-excerpt.md",
    "corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md",
    "corpus/fixtures/r97-crossing-acknowledgment/README.md",
    "corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md",
    "corpus/knowledge/r97-acknowledgment-scope-note.md",
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def header_line(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.readline().rstrip("\n")
    except OSError:
        return ""


def collect():
    lane_files = {}
    unexpected = []
    for name in sorted(os.listdir(LANE)):
        p = os.path.join(LANE, name)
        if not os.path.isfile(p) or not name.endswith(".md"):
            continue
        m = REPORT_RE.match(name)
        if not m:
            unexpected.append(name)
            continue
        seat = m.group(1)
        lane_files.setdefault(seat, []).append(p)

    parent_files = []
    if os.path.isdir(PARENT_WAVE):
        for dirpath, _dirnames, filenames in os.walk(PARENT_WAVE):
            if "V40-scratch" in dirpath:
                continue
            for fn in sorted(filenames):
                if fn.endswith(".md") and REPORT_RE.match(fn):
                    parent_files.append(os.path.join(dirpath, fn))

    seats = []
    absent = []
    misplaced = []
    dup = {}
    mismatches = []
    for seat in ROSTER:
        files = lane_files.get(seat, [])
        if len(files) > 1:
            dup[seat] = [os.path.relpath(f, ROOT) for f in files]
        if files:
            primary = files[0]
            reports = {}
            for f in files:
                reports[os.path.basename(f)] = sha256(f)
            hdr = header_line(primary)
            if not re.match(r"^#\s*" + re.escape(seat) + r"\b", hdr):
                mismatches.append({"seat": seat, "file": os.path.basename(primary), "header": hdr})
            seats.append({
                "seat": seat,
                "agent_id": None,
                "outcome": None,
                "reports": reports,
            })
        else:
            absent.append(seat)
            seats.append({
                "seat": seat,
                "agent_id": None,
                "outcome": None,
                "reports": {},
            })
            for pf in parent_files:
                if os.path.basename(pf).startswith(seat + "-"):
                    misplaced.append({
                        "seat": seat,
                        "parent_path": pf,
                        "sha256": sha256(pf),
                    })
    extra_parent = []
    for pf in parent_files:
        base = os.path.basename(pf)
        seat = REPORT_RE.match(base).group(1)
        if any(pf.endswith(os.path.basename(f)) for f in lane_files.get(seat, [])):
            extra_parent.append(pf)
    return {
        "lane_present": len([s for s in seats if s["reports"]]),
        "absent": absent,
        "misplaced": misplaced,
        "parent_tree_files": extra_parent,
        "duplicates": dup,
        "header_mismatches": mismatches,
        "unexpected_md": unexpected,
        "seats": seats,
    }


def git(*args):
    try:
        return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception as exc:  # pragma: no cover
        return f"<error: {exc}>"


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--summary"
    data = collect()
    now = subprocess.run(["date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True).stdout.strip()

    if mode == "--summary":
        print(f"snapshot {now}")
        print(f"lane present: {data['lane_present']}/64")
        print(f"absent: {data['absent']}")
        print(f"misplaced(parent tree): {json.dumps(data['misplaced'], indent=1)}")
        print(f"parent-tree duplicate copies: {data['parent_tree_files']}")
        print(f"duplicates: {data['duplicates']}")
        print(f"header mismatches: {data['header_mismatches']}")
        print(f"unexpected .md: {data['unexpected_md']}")
        for s in data["seats"]:
            for fn, h in s["reports"].items():
                print(f"{s['seat']}\t{fn}\t{h}")
        return 0

    if mode == "--write":
        head = git("rev-parse", "HEAD")
        pinned = {}
        for rel in PINNED_PATHS:
            p = os.path.join(ROOT, rel)
            pinned[rel] = sha256(p) if os.path.isfile(p) else None
        prior_path = os.path.join(ROOT, ".ufo/waves/round-97/seats/V40-scratch/V58-receipt-prior.json")
        prior_block = None
        if os.path.isfile(prior_path):
            with open(prior_path, "r", encoding="utf-8") as f:
                prior = json.load(f)
            prior_block = {
                "preserved_byte_copy": ".ufo/waves/round-97/seats/V40-scratch/V58-receipt-prior.json",
                "sha256": sha256(prior_path),
                "record_owner": prior.get("record_owner"),
                "snapshot_utc": prior.get("receipt_snapshot_utc"),
                "collection": prior.get("collection"),
                "note": (
                    "V58-presence-final also wrote receipt.json per its own seat spec "
                    "(double-assignment with V40's receipt seat, same class as r96 V43/V58 and "
                    "r95 V33/V59). Its file was read and byte-copied before this seat wrote the "
                    "path; V58's seats[] snapshot is superseded by this seat's snapshot. "
                    "V58's own report row hash in its snapshot was a3fe83a755320e145de26ad08a8c246f52ec73c2b1cd650c5102a17d52159fa4."
                ),
            }
        receipt = {
            "record_type": "round-97-receipt",
            "round": 97,
            "phase": "single-wave-64-seat",
            "requested_model": "opencode-go/deepseek-v4.1-flash",
            "requested_seats": 64,
            "dispatch_tool_call_id": None,
            "returned_summary": None,
            "served_backend_echo": None,
            "baseline_commit": "f3e09f93ce9f2b047eb2b2089bf7b1c03d74a40f",
            "head_at_snapshot": head,
            "receipt_snapshot_utc": now,
            "candidate_revision_pinned": pinned,
            "collection": {
                "reports_present": data["lane_present"],
                "reports_absent": data["absent"],
                "misplaced_detected": data["misplaced"],
                "parent_tree_duplicate_copies": data["parent_tree_files"],
                "duplicate_report_prefixes": data["duplicates"],
                "header_seat_mismatches": data["header_mismatches"],
                "unexpected_md_in_seats_dir": data["unexpected_md"],
                "post_snapshot_edits_observed": [
                    {
                        "seat": "V58",
                        "file": "V58-presence-final.md",
                        "hash_at_V58_1916_snapshot": "a3fe83a755320e145de26ad08a8c246f52ec73c2b1cd650c5102a17d52159fa4",
                        "final_hash": "759cd9d308bbe31fce2193d8d7df3104b41f32c6e541cc11605032624a61d626",
                        "note": (
                            "V58's own report was edited after V58 wrote its receipt snapshot "
                            "(19:16:30); this receipt records the final bytes. No other report "
                            "changed between V58's snapshot and this snapshot."
                        ),
                    }
                ],
                "note": (
                    "Skeleton receipt written by V40 (receipt seat). "
                    "agent_id/outcome/dispatch_tool_call_id/returned_summary left null for the "
                    "integrator (L1) to fill from the real AgentSwarm dispatch result — none "
                    "invented. sha256 computed over the report files as found in "
                    ".ufo/waves/round-97/seats/ at receipt_snapshot_utc. V40's report row "
                    "carries the hash of V40-receipt.md as written."
                ),
            },
            "known_seat_output_defects": [],
            "prior_receipt_by_V58": prior_block,
            "seats": data["seats"],
        }
        with open(RECEIPT, "w", encoding="utf-8") as f:
            json.dump(receipt, f, indent=1, ensure_ascii=False)
            f.write("\n")
        print(f"wrote {RECEIPT} with {len(data['seats'])} seat rows at {now}")
        return 0

    print("usage: --summary | --write", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
