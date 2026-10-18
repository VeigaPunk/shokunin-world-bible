#!/usr/bin/env python3
"""V23 poll: wait for r101 producer artifacts AND producer reports.

Checks every 20s, max 40 checks. READY requires:
  - 5 artifact conditions (tracked changes vs baseline 6f86bf2 for
    SKILL.md, contract, tools README, dependency_freeze.py; contract
    contains the r100-docket-review pin; new U2 knowledge file nonempty)
  - 2 producer reports: nonempty U1-*.md and U2-*.md in the seats dir.
Logs every check to poll.jsonl; on READY writes ready-manifest.json.
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


def sh(*args):
    return subprocess.run(args, cwd=LANE, capture_output=True, text=True)


def changed_vs_base():
    r = sh("git", "diff", "--name-only", BASE)
    return set(r.stdout.split())


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    log = open(os.path.join(SCRATCH, "poll.jsonl"), "w")
    ready = False
    for n in range(1, 41):
        t = time.time()
        stamp = time.strftime("%H:%M:%S", time.localtime(t))
        changed = changed_vs_base()
        arts = {p: (p in changed) for p in TRACKED}
        kpath = os.path.join(LANE, NEW)
        k_ok = os.path.exists(kpath) and os.path.getsize(kpath) > 0
        contract_changed = arts["corpus/tools/dependency-freeze-contract.json"]
        pin_ok = False
        if contract_changed:
            with open(os.path.join(LANE, "corpus/tools/dependency-freeze-contract.json")) as f:
                pin_ok = "r100-docket-review" in f.read()
        arts["NEW-knowledge"] = k_ok
        arts["contract-pin"] = pin_ok
        n_art = sum(1 for v in arts.values() if v)
        reports = {}
        for seat in ("U1", "U2"):
            hits = [p for p in sorted(glob.glob(os.path.join(SEATS, seat + "-*.md")))
                    if os.path.getsize(p) > 0]
            reports[seat] = hits
        n_rep = sum(1 for v in reports.values() if v)
        line = {"check": n, "t": stamp, "artifacts": arts, "n_art": n_art,
                "reports": reports, "n_rep": n_rep}
        if n_art == 6 and n_rep == 2:
            line["READY"] = True
            log.write(json.dumps(line) + "\n")
            log.close()
            print(f"READY artifacts={n_art}/6 producer_reports={n_rep}/2")
            manifest = {
                "ready_at": stamp,
                "artifacts": {p: sha256(os.path.join(LANE, p)) for p in TRACKED + [NEW]},
                "reports": {s: {os.path.basename(p): sha256(p) for p in hits}
                            for s, hits in reports.items()},
            }
            with open(os.path.join(SCRATCH, "ready-manifest.json"), "w") as f:
                json.dump(manifest, f, indent=2)
            return 0
        log.write(json.dumps(line) + "\n")
        log.flush()
        print(f"CHECK {n} t={stamp} artifacts={n_art}/6 producer_reports={n_rep}/2")
        sys.stdout.flush()
        if n < 40:
            time.sleep(20)
    log.close()
    print(f"POLL_TERMINAL reason=deadline artifacts={n_art}/6 producer_reports={n_rep}/2")
    return 2


if __name__ == "__main__":
    sys.exit(main())
