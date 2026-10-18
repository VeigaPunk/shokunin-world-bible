#!/usr/bin/env python3
"""V58 mutual-wait-guard sampler. Read-only except its own log.

Samples every `interval` seconds for up to `duration` seconds:
  report count, absent producers, scratch-dir count, poll-script count,
  live poll/watch processes, and tails of poll logs that mention
  TIMEOUT / STALL / CAP / ABSENT / mutual / nonself.
"""
import glob
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

R = "/home/vgpnk/Projects/shokunin/lore-shokunin"
W = os.path.join(R, ".ufo/waves/round-99")
SEATS = os.path.join(W, "seats")
LOG = os.path.join(SEATS, "V58-scratch/sampler.log")
PRODUCERS = [f"S{i}" for i in range(1, 6)]
# expected report basenames are unknown until they land; we count *.md excluding scratch.

INTERVAL = int(sys.argv[1]) if len(sys.argv) > 1 else 20
DURATION = int(sys.argv[2]) if len(sys.argv) > 2 else 780  # ~13 min


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def report_names():
    names = []
    for p in glob.glob(os.path.join(SEATS, "*.md")):
        names.append(os.path.basename(p))
    return sorted(names)


def producer_present(names):
    present = []
    absent = []
    for s in PRODUCERS:
        hits = [n for n in names if n.startswith(s + "-") or n.startswith(s + ".")]
        # also S1.md style
        hits += [n for n in names if n == s + ".md"]
        if hits:
            present.append(s)
        else:
            absent.append(s)
    return present, absent


def poll_scripts():
    out = []
    for pat in ("*scratch*/*.sh", "*scratch*/*.py", "scratch/*/*.sh"):
        out.extend(glob.glob(os.path.join(SEATS, pat)))
        out.extend(glob.glob(os.path.join(W, pat)))
    # unique
    return sorted(set(out))


def live_procs():
    try:
        r = subprocess.run(
            ["ps", "-eo", "pid,ppid,etimes,stat,cmd"],
            capture_output=True, text=True, timeout=10,
        )
    except Exception as e:
        return [f"ps-error {e}"]
    lines = []
    for line in r.stdout.splitlines():
        if "round-99" in line and "grep" not in line:
            lines.append(line.strip())
    return lines


def interesting_tails():
    hits = []
    logs = glob.glob(os.path.join(SEATS, "*scratch*/*.log"))
    logs += glob.glob(os.path.join(W, "scratch/*/*.log"))
    keys = ("TIMEOUT", "STALL", "CAP ", "ABSENT", "mutual", "nonself",
            "DEADLINE", "POLL-TIMEOUT", "POLL_HIT", "READY")
    for p in logs:
        try:
            with open(p, errors="replace") as f:
                # last 8k
                f.seek(0, os.SEEK_END)
                sz = f.tell()
                f.seek(max(0, sz - 4000))
                tail = f.read()
        except OSError:
            continue
        for key in keys:
            if key in tail:
                # last matching line
                last = ""
                for line in tail.splitlines():
                    if key in line:
                        last = line.strip()[:220]
                hits.append(f"{os.path.basename(os.path.dirname(p))}/{os.path.basename(p)} {key}: {last}")
                break
    return hits[:40]


def main():
    t0 = time.time()
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG, "a") as log:
        log.write(f"== sampler start {now()} interval={INTERVAL} duration={DURATION} ==\n")
        log.flush()
        n = 0
        while time.time() - t0 < DURATION:
            n += 1
            names = report_names()
            present, absent = producer_present(names)
            scripts = poll_scripts()
            procs = live_procs()
            arts = []
            for a in (
                "corpus/tools/dependency_freeze.py",
                "corpus/tools/dependency-freeze-contract.json",
                "corpus/fixtures/r99-window-lapse/timeline.json",
                "corpus/fixtures/r99-window-lapse/sources.json",
                "corpus/fixtures/r99-window-lapse/fictional-excerpts.md",
                "corpus/fixtures/r99-window-lapse/README.md",
                "corpus/fixtures/r99-window-lapse/claim-excerpt-map.md",
                "corpus/knowledge/r99-gate-blind-spot-table.md",
                "corpus/knowledge/r99-lapse-scope-note.md",
            ):
                p = os.path.join(R, a)
                arts.append("1" if os.path.exists(p) else "0")
            scratch_dirs = [
                d for d in os.listdir(SEATS)
                if os.path.isdir(os.path.join(SEATS, d))
            ]
            line = (
                f"== t={now()} iter={n} reports={len(names)} "
                f"producers_present={','.join(present) or '-'} "
                f"producers_absent={','.join(absent) or '-'} "
                f"scratch_dirs={len(scratch_dirs)} scripts={len(scripts)} "
                f"procs={len(procs)} arts={''.join(arts)} ==\n"
            )
            log.write(line)
            if names:
                log.write("  reports=" + ",".join(names[:30]) + ("..." if len(names) > 30 else "") + "\n")
            if procs:
                for pl in procs[:12]:
                    log.write("  proc " + pl[:240] + "\n")
            hits = interesting_tails()
            for h in hits[:12]:
                log.write("  tail " + h + "\n")
            log.flush()
            # stop early only if 128 reports exist AND no live pollers remain for 2 iters — never, we just sample
            time.sleep(INTERVAL)
        log.write(f"== sampler end {now()} iters={n} ==\n")
        log.flush()


if __name__ == "__main__":
    main()
