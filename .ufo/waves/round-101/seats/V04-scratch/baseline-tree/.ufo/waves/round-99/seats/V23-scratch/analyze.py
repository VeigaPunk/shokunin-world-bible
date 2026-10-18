#!/usr/bin/env python3
"""V23 scope-creep bucketer. Read-only. Writes only under V23-scratch/snap/."""
import os
import subprocess
import time
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
PARENT = Path("/home/vgpnk/Projects/shokunin")
SNAP = ROOT / ".ufo/waves/round-99/seats/V23-scratch/snap"
SNAP.mkdir(parents=True, exist_ok=True)

PRODUCER = {
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/README.md",
    "SKILL.md",
}
FIXTURE_PREFIX = "corpus/fixtures/r99-window-lapse/"
KNOWLEDGE = {
    "corpus/knowledge/r99-gate-blind-spot-table.md",
    "corpus/knowledge/r99-lapse-scope-note.md",
}
EXPECTED_FIXTURE = {
    "README.md",
    "claim-excerpt-map.md",
    "contradictions.json",
    "entities.json",
    "fictional-excerpts.md",
    "inspiration-note.md",
    "relations.json",
    "source-excerpt.md",
    "sources.json",
    "timeline.json",
}

def run(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr

def main(label):
    ts = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    rc, porc, err = run(["git", "status", "--porcelain", "-uall"], ROOT)
    (SNAP / f"porcelain-{label}.txt").write_text(porc)
    rc2, diff, _ = run(["git", "diff", "--name-status"], ROOT)
    (SNAP / f"diff-name-status-{label}.txt").write_text(diff)
    rc3, cached, _ = run(["git", "diff", "--cached", "--name-status"], ROOT)
    (SNAP / f"diff-cached-{label}.txt").write_text(cached)
    rc4, parent, perr = run(["git", "status", "--porcelain", "-uall"], PARENT)
    (SNAP / f"parent-{label}.txt").write_text(parent)
    head = run(["git", "rev-parse", "HEAD"], ROOT)[1].strip()
    log = run(["git", "log", "-1", "--format=%H %ci %s"], ROOT)[1].strip()

    buckets = {
        "producer_tracked_or_untracked": [],
        "fixture": [],
        "knowledge": [],
        "log_md": [],
        "seat_reports": [],
        "seat_scratch": [],
        "wave_other": [],
        "other": [],
    }
    non_untracked = []
    for line in porc.splitlines():
        if not line:
            continue
        status = line[:2]
        path = line[3:]
        if status != "??":
            non_untracked.append(line)
        if path in PRODUCER or path.startswith("corpus/tools/dependency_freeze") or path == "SKILL.md" or path == "corpus/tools/README.md":
            buckets["producer_tracked_or_untracked"].append(line)
        elif path.startswith(FIXTURE_PREFIX):
            buckets["fixture"].append(line)
        elif path in KNOWLEDGE or path.startswith("corpus/knowledge/r99-"):
            buckets["knowledge"].append(line)
        elif path == "LOG.md":
            buckets["log_md"].append(line)
        elif path.startswith(".ufo/waves/round-99/seats/") and path.endswith(".md") and path.count("/") == 4:
            buckets["seat_reports"].append(line)
        elif path.startswith(".ufo/waves/round-99/seats/"):
            buckets["seat_scratch"].append(line)
        elif path.startswith(".ufo/waves/round-99/"):
            buckets["wave_other"].append(line)
        else:
            buckets["other"].append(line)

    # fixture extras
    fixdir = ROOT / "corpus/fixtures/r99-window-lapse"
    extras = []
    missing = []
    if fixdir.is_dir():
        names = {p.name for p in fixdir.iterdir()}
        extras = sorted(names - EXPECTED_FIXTURE)
        missing = sorted(EXPECTED_FIXTURE - names)

    # seats top-level classification
    seats = ROOT / ".ufo/waves/round-99/seats"
    top_files = []
    top_dirs = []
    if seats.is_dir():
        for p in sorted(seats.iterdir()):
            if p.is_file():
                top_files.append(p.name)
            elif p.is_dir():
                top_dirs.append(p.name)

    # pycache committable?
    rc_ig, ignored, _ = run(["git", "status", "--porcelain", "--ignored", "-uall"], ROOT)
    pyc_lines = [ln for ln in ignored.splitlines() if "__pycache__" in ln or ln.endswith(".pyc")]
    # only corpus + round-99
    pyc_interest = [ln for ln in pyc_lines if "corpus/" in ln or "round-99" in ln]
    (SNAP / f"pycache-interest-{label}.txt").write_text("\n".join(pyc_interest) + ("\n" if pyc_interest else ""))

    # committable pyc: appears in normal porcelain
    pyc_committable = [ln for ln in porc.splitlines() if "__pycache__" in ln or ln.endswith(".pyc")]

    lines = []
    lines.append(f"label={label}")
    lines.append(f"ts={ts}")
    lines.append(f"head={head}")
    lines.append(f"log={log}")
    lines.append(f"porcelain_rc={rc} lines={len(porc.splitlines())}")
    lines.append(f"parent_rc={rc4} parent_lines={len(parent.splitlines())} parent_err={perr.strip()!r}")
    lines.append(f"cached={cached.strip()!r}")
    lines.append("DIFF_NAME_STATUS:")
    lines.append(diff.rstrip())
    lines.append("NON_UNTRACKED:")
    lines.append("\n".join(non_untracked) if non_untracked else "(none)")
    lines.append("COUNTS:")
    for k, v in buckets.items():
        lines.append(f"  {k}={len(v)}")
    lines.append("OTHER:")
    lines.append("\n".join(buckets["other"]) if buckets["other"] else "(none)")
    lines.append("WAVE_OTHER:")
    lines.append("\n".join(buckets["wave_other"]) if buckets["wave_other"] else "(none)")
    lines.append("PRODUCER_LINES:")
    lines.append("\n".join(buckets["producer_tracked_or_untracked"]) if buckets["producer_tracked_or_untracked"] else "(none)")
    lines.append("KNOWLEDGE_LINES:")
    lines.append("\n".join(buckets["knowledge"]) if buckets["knowledge"] else "(none)")
    lines.append("LOG_LINES:")
    lines.append("\n".join(buckets["log_md"]) if buckets["log_md"] else "(none)")
    lines.append(f"FIXTURE_EXTRAS={extras}")
    lines.append(f"FIXTURE_MISSING={missing}")
    lines.append(f"SEAT_TOP_FILES={top_files}")
    lines.append(f"SEAT_TOP_DIRS_N={len(top_dirs)}")
    nonscratch = [d for d in top_dirs if not d.endswith("-scratch") and d != "scratch"]
    lines.append(f"SEAT_NONSCRATCH_DIRS={nonscratch}")
    odd_files = [f for f in top_files if not f.endswith(".md")]
    lines.append(f"SEAT_NON_MD_FILES={odd_files}")
    lines.append(f"PYC_COMMITTABLE={pyc_committable}")
    lines.append(f"PYC_INTEREST_N={len(pyc_interest)}")
    text = "\n".join(lines) + "\n"
    (SNAP / f"buckets-{label}.txt").write_text(text)
    print(text)

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "mid")
