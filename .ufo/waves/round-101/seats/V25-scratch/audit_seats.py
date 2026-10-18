#!/usr/bin/env python3
"""V25 receipt seat: census of .ufo/waves/round-101/seats/. Read-only."""
import hashlib, json, os, sys, datetime

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS = os.path.join(ROOT, ".ufo/waves/round-101/seats")
SELF_SEAT = "V25"
EXPECTED_ROSTER = ["U1", "U2"] + [f"V{i:02d}" for i in range(1, 27)]  # 28

def seat_id_of(name):
    return name.split("-", 1)[0]

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    entries = sorted(os.listdir(SEATS))
    reports, scratches = [], []
    for e in entries:
        p = os.path.join(SEATS, e)
        if os.path.isdir(p):
            scratches.append(e)
        elif e.endswith(".md"):
            reports.append(e)
        else:
            print(f"NONMD-TOPLEVEL {e}", file=sys.stderr)

    seat_reports = {}
    for fn in reports:
        sid = seat_id_of(fn)
        p = os.path.join(SEATS, fn)
        head = ""
        with open(p, "r", errors="replace") as f:
            head = "".join([f.readline() for _ in range(20)])
        seat_reports.setdefault(sid, []).append({
            "file": fn,
            "sha256": sha256(p),
            "bytes": os.path.getsize(p),
            "mtime_utc": datetime.datetime.fromtimestamp(
                os.path.getmtime(p), datetime.timezone.utc).isoformat(),
            "header_has_seat_token": sid in head,
            "empty": os.path.getsize(p) == 0,
            "tiny_under_200": os.path.getsize(p) < 200,
        })

    present = sorted(seat_reports.keys())
    self_recs = seat_reports.get(SELF_SEAT, [])
    present_excl_self = [s for s in present if s != SELF_SEAT]
    dup = {s: [r["file"] for r in rs] for s, rs in seat_reports.items() if len(rs) > 1}
    missing = [s for s in EXPECTED_ROSTER if s not in present]
    excess = [s for s in present if s not in EXPECTED_ROSTER]

    snap = {
        "census_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "expected_roster": EXPECTED_ROSTER,
        "expected_count": len(EXPECTED_ROSTER),
        "present": present,
        "present_count": len(present),
        "present_excl_self": present_excl_self,
        "present_excl_self_count": len(present_excl_self),
        "self_seat": SELF_SEAT,
        "self_report_files": [r["file"] for r in self_recs],
        "missing_seat_ids": missing,
        "excess_seat_ids": excess,
        "duplicate_report_prefixes": dup,
        "scratch_dirs": scratches,
        "scratch_dirs_without_report": sorted(
            d for d in scratches if seat_id_of(d) not in present),
        "header_token_misses_first20": sorted(
            s for s, rs in seat_reports.items()
            for r in rs if not r["header_has_seat_token"]),
        "empty_reports": sorted(
            s for s, rs in seat_reports.items() for r in rs if r["empty"]),
        "tiny_reports_under_200_bytes": sorted(
            s for s, rs in seat_reports.items() for r in rs if r["tiny_under_200"]),
        "unexpected_md_in_seats_dir": [],
        "seat_reports": seat_reports,
        "complete_excl_self": len(present_excl_self) >= len(EXPECTED_ROSTER) - 1
            and not excess,
    }
    print(json.dumps(snap, indent=1))
    return 0 if snap["complete_excl_self"] else 1

if __name__ == "__main__":
    sys.exit(main())
