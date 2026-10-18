#!/usr/bin/env python3
"""V59 presence-final: generate .ufo/waves/round-95/receipt.json collection_snapshot.
Reads seats/*.md, extracts seat IDs from filename prefix and header line 1, hashes reports.
Leaves agent_id/outcome null for L1 fill. Run from repo root."""
import hashlib, json, os, subprocess, sys, time

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS_DIR = os.path.join(ROOT, ".ufo/waves/round-95/seats")
RECEIPT = os.path.join(ROOT, ".ufo/waves/round-95/receipt.json")
CURVE = os.path.join(SEATS_DIR, "V59-scratch/collection-curve.txt")

EXPECTED = ["P%d" % i for i in range(1, 6)] + ["V%02d" % i for i in range(1, 60)]

reports = {}
for name in sorted(os.listdir(SEATS_DIR)):
    if not name.endswith(".md"):
        continue
    p = os.path.join(SEATS_DIR, name)
    if not os.path.isfile(p):
        continue
    seat = name.split("-", 1)[0]
    with open(p, "rb") as f:
        data = f.read()
    sha = hashlib.sha256(data).hexdigest()
    first = data.decode("utf-8", "replace").splitlines()[0] if data else ""
    reports.setdefault(seat, []).append({
        "file": name, "path": ".ufo/waves/round-95/seats/" + name,
        "sha256": sha, "header_line1": first,
        "header_has_seat": seat in first,
    })

dups = {s: [r["file"] for r in rs] for s, rs in reports.items() if len(rs) > 1}
present = sorted(reports)
missing = [s for s in EXPECTED if s not in reports]
unexpected = [s for s in present if s not in EXPECTED]
hdr_mismatch = []
for s, rs in sorted(reports.items()):
    for r in rs:
        if not r["header_has_seat"]:
            hdr_mismatch.append({"seat": s, "file": r["file"], "header_line1": r["header_line1"][:120]})

curve = []
if os.path.exists(CURVE):
    curve = [l.strip() for l in open(CURVE) if l.strip()]
WATCH = os.path.join(SEATS_DIR, "V59-scratch/watch.txt")
watch_curve = []
if os.path.exists(WATCH):
    for l in open(WATCH):
        parts = l.split()
        if len(parts) >= 2 and parts[1].startswith("reports="):
            watch_curve.append("%s=%s" % (parts[0], parts[1].split("=", 1)[1]))
        elif "WATCH_TIMEOUT" in l:
            watch_curve.append("WATCH_TIMEOUT")

aux = []
for name in sorted(os.listdir(SEATS_DIR)):
    if not name.endswith(".md"):
        aux.append(name + ("/" if os.path.isdir(os.path.join(SEATS_DIR, name)) else ""))
top_scratch = os.path.join(ROOT, ".ufo/waves/round-95/scratch")
if os.path.isdir(top_scratch):
    for name in sorted(os.listdir(top_scratch)):
        aux.append("scratch/" + name + "/")

seat_rows = []
for s in present:
    for r in reports[s]:
        seat_rows.append({"seat": s, "report_path": r["path"],
                          "report_sha256": r["sha256"],
                          "agent_id": None, "outcome": None})

receipt = {
    "record_type": "round-95-receipt",
    "record_owner": "V59",
    "round": 95,
    "phase": "WORK",
    "requested_model": "opencode-go/deepseek-v4.1-flash",
    "requested_seats": 64,
    "baseline_commit": "fb118c4",
    "state": "collection snapshot finalized by V59 presence-final; agent IDs and outcomes left null for L1 fill after the AgentSwarm dispatch result returns",
    "agent_id_note": "Every agent_id is null by design: only the integrator fills actual agent IDs and outcomes after the batched dispatch returns. No agent ID, dispatch ID, or served-backend echo is invented here.",
    "collection_snapshot": {
        "snapshot_time_local": time.strftime("%Y-%m-%d %H:%M:%S %z"),
        "reports_present": sum(len(v) for v in reports.values()),
        "expected_seats": EXPECTED,
        "seats_present": present,
        "reports_missing": missing,
        "unexpected_seat_prefixes": unexpected,
        "duplicate_report_prefixes": dups,
        "header_seat_mismatches": hdr_mismatch,
        "collection_curve_20s_poller": curve,
        "collection_curve_30s_watcher": watch_curve,
        "auxiliary_artifacts": aux,
        "flagged_observation": "Three declared verifier seats produced no report and no scratch activity through the final snapshot (V09, V18, V33); collection growth stopped at 17:03 (V57) and this snapshot is final at the time below. The committed round-95 wave-spec.json does not exist at snapshot time; the roster used here is the LOG.md declaration (5 producers P1-P5 + 59 verifiers V01-V59).",
    },
    "seats": seat_rows,
}

with open(RECEIPT, "w") as f:
    json.dump(receipt, f, indent=1)
    f.write("\n")
print("WROTE", RECEIPT)
print("reports_present=%d missing=%s unexpected=%s dups=%s hdr_mismatch=%d"
      % (len(seat_rows), missing, unexpected, list(dups), len(hdr_mismatch)))
