#!/usr/bin/env python3
"""V23 poll extension — ONE bounded stall-escape (checks 61-70, 20s apart).

Poll #1 (poll.py, checks 1-40) terminated on deadline with artifacts=3/6,
reports=0/2 while the wave was demonstrably live (U1 bytes landed at
~00:11). This extension records the escape and continues the same six
conditions. Appends to poll-extension2.jsonl; never rewrites poll.jsonl.
"""
import glob, hashlib, json, os, subprocess, sys, time

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
BASE = "6f86bf2"
SCRATCH = os.path.join(LANE, ".ufo/waves/round-101/seats/V23-scratch")
SEATS = os.path.join(LANE, ".ufo/waves/round-101/seats")
TRACKED = [
    "SKILL.md",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/README.md",
    "corpus/tools/dependency_freeze.py",
]
NEW = "corpus/knowledge/r101-r10-register-first-entry.md"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    log = open(os.path.join(SCRATCH, "poll-extension2.jsonl"), "w")
    ready = False
    for i in range(61, 71):
        t = time.time()
        stamp = time.strftime("%H:%M:%S", time.localtime(t))
        r = subprocess.run(["git", "diff", "--name-only", BASE], cwd=LANE,
                           capture_output=True, text=True)
        changed = set(r.stdout.split())
        arts = {p: (p in changed) for p in TRACKED}
        kpath = os.path.join(LANE, NEW)
        k_ok = os.path.exists(kpath) and os.path.getsize(kpath) > 0
        pin_ok = False
        if arts["corpus/tools/dependency-freeze-contract.json"]:
            with open(os.path.join(LANE, "corpus/tools/dependency-freeze-contract.json")) as f:
                pin_ok = "r100-docket-review" in f.read()
        arts["NEW-knowledge"] = k_ok
        arts["contract-pin"] = pin_ok
        n_art = sum(1 for v in arts.values() if v)
        reports = {}
        for seat in ("U1", "U2"):
            reports[seat] = [p for p in sorted(glob.glob(os.path.join(SEATS, seat + "-*.md")))
                             if os.path.getsize(p) > 0]
        n_rep = sum(1 for v in reports.values() if v)
        line = {"check": i, "t": stamp, "artifacts": arts, "n_art": n_art,
                "reports": reports, "n_rep": n_rep,
                "stall_escape": "final bounded extension 61-70 (second recorded escape)"}
        if n_art == 6 and n_rep == 2:
            log.write(json.dumps(line) + "\n")
            log.close()
            print(f"READY artifacts={n_art}/6 producer_reports={n_rep}/2 (extended poll)")
            manifest = {
                "ready_at": stamp, "poll": "extension",
                "artifacts": {p: sha256(os.path.join(LANE, p)) for p in TRACKED + [NEW]},
                "reports": {s: {os.path.basename(p): sha256(p) for p in hits}
                            for s, hits in reports.items()},
            }
            with open(os.path.join(SCRATCH, "ready-manifest.json"), "w") as f:
                json.dump(manifest, f, indent=2)
            return 0
        log.write(json.dumps(line) + "\n")
        log.flush()
        print(f"CHECK {i} t={stamp} artifacts={n_art}/6 producer_reports={n_rep}/2")
        sys.stdout.flush()
        if i < 70:
            time.sleep(20)
    log.close()
    print(f"POLL_TERMINAL reason=deadline artifacts={n_art}/6 producer_reports={n_rep}/2")
    return 2


if __name__ == "__main__":
    sys.exit(main())
