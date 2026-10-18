#!/usr/bin/env python3
"""V23 parent/sibling boundary sweep (metadata + bounded content-leak grep).

Sweeps the fleet root for regular files modified since the r101 declaration
commit time, excluding the lore lane, VCS metadata, dependency/build dirs,
and sensitive names. Also captures parent-repo git status and runs a bounded
content-leak grep for r101-specific strings across sibling text files.
"""
import datetime, json, os, subprocess, sys

FLEET = "/home/vgpnk/Projects/shokunin"
LANE = os.path.join(FLEET, "lore-shokunin")
SCRATCH = os.path.join(LANE, ".ufo/waves/round-101/seats/V23-scratch")
DECL = datetime.datetime(2026, 10, 17, 23, 59, 55).timestamp()
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv",
             "target", "dist", "build", ".cache"}
SENSITIVE = {".env", "id_rsa", "id_ed25519", "credentials", ".netrc"}
TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml", ".txt", ".sh", ".toml"}
LEAK_PATTERNS = ["r101-r10-register-first-entry", "r101 register-first-entry"]


def git_status(repo):
    r = subprocess.run(["git", "status", "--short"], cwd=repo,
                       capture_output=True, text=True)
    return r.stdout.strip()


def main():
    out = {"sweep_since": "2026-10-17T23:59:55-03:00 (declaration ebec6bb)",
           "lane": LANE}
    out["parent_git_status"] = git_status(FLEET)
    out["parent_round101_wave_exists"] = os.path.exists(
        os.path.join(FLEET, ".ufo", "waves", "round-101"))
    recent = {}
    strays = []
    leak_hits = []
    scanned = 0
    for root, dirs, files in os.walk(FLEET):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if any(s in name for s in SENSITIVE):
                continue
            path = os.path.join(root, name)
            try:
                st = os.lstat(path)
            except OSError:
                continue
            if os.path.islink(path):
                continue
            rel = os.path.relpath(path, FLEET)
            if rel.startswith("lore-shokunin" + os.sep) or rel == "lore-shokunin":
                continue
            scanned += 1
            if st.st_mtime > DECL:
                top = rel.split(os.sep)[0]
                recent[top] = recent.get(top, 0) + 1
                if st.st_mtime > DECL and os.path.getsize(path) > 0 and \
                        os.path.splitext(name)[1] in TEXT_SUFFIXES and \
                        os.path.getsize(path) < 2_000_000:
                    try:
                        with open(path, "rb") as f:
                            blob = f.read().decode("utf-8", "replace")
                    except OSError:
                        continue
                    if any(p in blob for p in LEAK_PATTERNS):
                        leak_hits.append(rel)
    out["scanned_files_outside_lane"] = scanned
    out["recent_counts_by_top"] = dict(sorted(recent.items()))
    out["leak_hits"] = leak_hits
    # any lore-attributable path inside other repos' wave dirs
    r101_strays = [rel for rel, n in recent.items()
                   if "round-101" in rel or "round101" in rel]
    out["round101_strays_outside_lane"] = r101_strays
    with open(os.path.join(SCRATCH, "outside.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({k: out[k] for k in
                      ("parent_git_status", "parent_round101_wave_exists",
                       "scanned_files_outside_lane", "recent_counts_by_top",
                       "leak_hits", "round101_strays_outside_lane")}, indent=1))


if __name__ == "__main__":
    sys.exit(main())
