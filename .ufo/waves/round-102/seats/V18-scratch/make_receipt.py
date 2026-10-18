#!/usr/bin/env python3
"""V18 skeleton generator: round-102 receipt.json at the wave root.
agent_id left null in every seat row for the L1 to fill from the dispatch result.
Filled at adjudication time from V18's verified evidence; verdicts passed in
via verdicts.json in this scratch dir."""
import json, hashlib, os, subprocess, datetime, sys

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
WAVE = os.path.join(ROOT, ".ufo/waves/round-102")

def sh(*args):
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT).stdout.strip()

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()

verdicts = json.load(open(os.path.join(os.path.dirname(__file__), "verdicts.json")))

reports_dir = os.path.join(WAVE, "seats")
mds = sorted(f for f in os.listdir(reports_dir) if f.endswith(".md"))
self_report = "V18-adjudicator.md"
others = [f for f in mds if f != self_report]

seat_labels = ["U1", "U2"] + [f"V{i:02d}" for i in range(1, 20)]  # declared U1-U2 + V01-V18; V19 = observed-dispatch erratum candidate
seats = []
for lbl in seat_labels:
    match = [f for f in mds if f.startswith(lbl + "-") or f == lbl + ".md"]
    row = {
        "seat": lbl,
        "agent_id": None,
        "outcome": None,
        "report_status": "present" if match else "ABSENT",
        "report_path": (".ufo/waves/round-102/seats/" + match[0]) if match else None,
        "report_sha256": sha(os.path.join(reports_dir, match[0])) if match else None,
        "bytes": os.path.getsize(os.path.join(reports_dir, match[0])) if match else None,
        "mtime_utc": datetime.datetime.utcfromtimestamp(os.path.getmtime(os.path.join(reports_dir, match[0]))).isoformat() + "Z" if match else None,
    }
    seats.append(row)

know = os.path.join(ROOT, "corpus/knowledge")
artifacts = {}
for name in ["r102-push-synthesis-r95-r102.md", "r102-debt-ledger.json", "r102-freshness-sweep.md"]:
    p = os.path.join(know, name)
    if os.path.exists(p):
        st = os.stat(p)
        artifacts["corpus/knowledge/" + name] = {
            "sha256": sha(p), "bytes": st.st_size,
            "mtime_utc": datetime.datetime.utcfromtimestamp(st.st_mtime).isoformat() + "Z",
        }
    else:
        artifacts["corpus/knowledge/" + name] = None

receipt = {
    "record_type": "round-102-receipt",
    "round": 102,
    "phase": "single-wave-capstone",
    "requested_model": "zai-coding-plan/glm-5.3-flash-low",
    "dispatch_model_alias_declared": None,
    "requested_effort": None,
    "requested_seats": 20,
    "dispatch_tool_call_id": None,
    "returned_summary": None,
    "served_backend_echo": None,
    "baseline_commit": verdicts.get("baseline_commit_full"),
    "baseline_is_ancestor_of_head": None,
    "head_at_snapshot": sh("git", "rev-parse", "HEAD"),
    "receipt_snapshot_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "git_status_short": sh("git", "status", "--short").splitlines(),
    "candidate_revision_pinned": {k: (v or {}).get("sha256") for k, v in artifacts.items()},
    "candidate_revision_meta": artifacts,
    "collection_snapshot": {
        "reports_expected": 20,
        "reports_present": len(mds),
        "reports_present_excl_self": len(others),
        "reports_missing_count": max(0, 19 - len(others)),
        "producer_count": 2,
        "verifier_count": 18,
        "roster_erratum_note": verdicts.get("roster_note"),
        "present": [f.rsplit("-", 1)[0].split(".")[0] for f in mds],
    },
    "seats": seats,
    "adjudication": verdicts.get("adjudication"),
    "state": "SKELETON written by V18 adjudicator (FINAL seat) at adjudication time; agent_id/outcome/dispatch fields null for L1 to fill from the real AgentSwarm dispatch result. Verdicts are V18's own per-axis adjudication from delivered bytes.",
    "l1_follow_up": [
        "Fill agent_id and outcome for every seat row from the actual dispatch result, never from report existence.",
        "Fill dispatch_tool_call_id and returned_summary from the real single-wave dispatch.",
        "Reconcile the declared 20-seat roster (U1-U2, V01-V18) with observed report identifiers; a V19 seat/scratch was observed dispatched - explain the arithmetic without dropping reports (r100/r101 erratum class).",
        "Refresh report and candidate hashes after any final report landings or closure edits.",
        "Land the closure-commit bookkeeping (LOG/SCORECARD round-102 sections) this wave tree cannot write.",
    ],
}

out = os.path.join(WAVE, "receipt.json")
with open(out, "w") as f:
    json.dump(receipt, f, indent=1, ensure_ascii=False)
print("wrote", out)
