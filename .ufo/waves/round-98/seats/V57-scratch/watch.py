#!/usr/bin/env python3
"""V57 mutual-wait-guard-2 independent 20s sampler for round 98.

Appends one snapshot per ~20s to V57-scratch/watch.log:
- report counts + absent seat ids (S1-S5, V01-V59)
- live poll/wait processes (pid, age, truncated cmd)
- tails of every other seat's poll log
- new/changed seat scripts copied to V57-scratch/scripts/ (sha-pinned)

Relaunch-safe (append-only; seen-hashes persisted in seen.json).
Usage: python3 watch.py [max_seconds]   (default 3300)
"""
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
WAVE = ROOT / ".ufo/waves/round-98"
SEATS = WAVE / "seats"
SCRATCH = SEATS / "V57-scratch"
LOG = SCRATCH / "watch.log"
SCRIPTS = SCRATCH / "scripts"
SEEN_F = SCRATCH / "seen.json"


def now():
    return datetime.now(timezone.utc).strftime("%H:%M:%SZ")


def load_seen():
    try:
        return json.loads(SEEN_F.read_text())
    except Exception:
        return {}


def sample(i, seen):
    SCRIPTS.mkdir(parents=True, exist_ok=True)
    lines = [f"== t={now()} iter={i} =="]
    md = sorted(p.name for p in SEATS.glob("*.md"))
    s = [m for m in md if m.startswith("S") and len(m) > 1 and m[1].isdigit()]
    v = [m for m in md if m.startswith("V") and len(m) > 2 and m[1:3].isdigit()]
    lines.append(f"reports S={len(s)} V={len(v)} total={len(md)}")
    absent_s = [f"S{k}" for k in range(1, 6) if not any(m.startswith(f"S{k}-") for m in s)]
    absent_v = [f"V{k:02d}" for k in range(1, 60) if not any(m.startswith(f"V{k:02d}-") for m in v)]
    lines.append(f"absent_S={absent_s}")
    lines.append(f"absent_V={absent_v}")
    try:
        ps = subprocess.run(
            ["ps", "-eo", "pid,etimes,stat,cmd"],
            capture_output=True, text=True, timeout=15,
        ).stdout
    except Exception as e:
        ps = f"PS-ERROR {e!r}"
    procs = []
    for ln in ps.splitlines():
        if ("lore-shokunin" in ln or "round-98" in ln) and (
            "poll" in ln or "watch" in ln or "for i in" in ln or "while" in ln
            or "sleep 20" in ln or "seq 1" in ln
        ):
            if "V57-scratch/watch.py" in ln:
                continue
            procs.append(" ".join(ln.split()))
    lines.append(f"poll_procs={len(procs)}")
    for p in procs:
        lines.append(f"  P {p[:240]}")
    scan_dirs = list(SEATS.glob("*scratch*")) + list((WAVE / "scratch").glob("*"))
    scan_dirs += [d for d in ROOT.glob("*scratch*") if d.is_dir()]
    for d in sorted(scan_dirs):
        if not d.is_dir() or d.name == "V57-scratch":
            continue
        label = d.name if d.parent == SEATS else (
            f"root-scratch/{d.name}" if d.parent == ROOT else f"wave-scratch/{d.name}"
        )
        for f in sorted(set(d.glob("poll*.log")) | set(d.glob("*poll*.log")) | set(d.glob("poll*.out"))):
            try:
                tail = f.read_text(errors="replace").strip().splitlines()
                lines.append(f"  [{label}/{f.name}] last={tail[-1][:200] if tail else '<empty>'}")
            except OSError:
                pass
        for f in sorted(set(d.glob("*.sh")) | set(d.glob("*.py"))):
            try:
                h = hashlib.sha256(f.read_bytes()).hexdigest()[:12]
            except OSError:
                continue
            key = str(f)
            if seen.get(key) != h:
                seen[key] = h
                dest = SCRIPTS / f"{label}__{f.name}.{h}.txt"
                try:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(f.read_bytes())
                    lines.append(f"  [new/changed script] {label}/{f.name} sha={h}")
                except OSError:
                    pass
    lines.append("")
    with LOG.open("a") as fh:
        fh.write("\n".join(lines) + "\n")
    try:
        SEEN_F.write_text(json.dumps(seen))
    except OSError:
        pass


if __name__ == "__main__":
    max_s = int(sys.argv[1]) if len(sys.argv) > 1 else 3300
    start = time.time()
    i = 0
    seen = load_seen()
    while time.time() - start < max_s:
        try:
            sample(i, seen)
        except Exception as e:
            with LOG.open("a") as fh:
                fh.write(f"== t={now()} iter={i} ERROR {e!r} ==\n")
        i += 1
        time.sleep(20)
