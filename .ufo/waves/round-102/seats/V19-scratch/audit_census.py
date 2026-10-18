#!/usr/bin/env python3
"""V19 presence-final census (read-only except scratch JSON output)."""
import hashlib, json, os, subprocess, datetime

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
SEATS = os.path.join(ROOT, ".ufo/waves/round-102/seats")
SELF = "V19"
OUT = os.path.join(SEATS, "V19-scratch", "final-census.json")

def sha16(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:16]

def mtime_utc(p):
    return datetime.datetime.utcfromtimestamp(os.path.getmtime(p)).isoformat() + "Z"

def head20_token(p, token):
    with open(p, "r", errors="replace") as f:
        head = "".join(f.readline() for _ in range(20))
    return token in head

def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)

snap = {}
snap["snapshot_utc"] = datetime.datetime.utcnow().isoformat() + "Z"
snap["head"] = git("rev-parse", "HEAD").stdout.strip()
snap["baseline_542021a_ancestor"] = git("merge-base", "--is-ancestor", "542021a", "HEAD").returncode == 0
snap["git_status_short"] = git("status", "--porcelain").stdout.splitlines()

reports, scratches, non_report = [], [], []
for name in sorted(os.listdir(SEATS)):
    p = os.path.join(SEATS, name)
    if os.path.isdir(p):
        scratches.append(name)
        continue
    if name.endswith(".md"):
        seat = name.split("-", 1)[0].rstrip(".")
        size = os.path.getsize(p)
        reports.append({
            "file": name, "seat": seat, "is_self": name.startswith(SELF + "-"),
            "bytes": size, "sha16": sha16(p), "mtime_utc": mtime_utc(p),
            "header_token_first20": head20_token(p, seat),
        })
    else:
        non_report.append(name)

others = [r for r in reports if not r["is_self"]]
prefixes = [r["seat"] for r in others]
dups = sorted({s for s in prefixes if prefixes.count(s) > 1})
empty = [r["file"] for r in reports if r["bytes"] == 0]
tiny = [r["file"] for r in reports if 0 < r["bytes"] < 200]
token_miss = [r["file"] for r in reports if not r["header_token_first20"]]

snap["all_reports_incl_self"] = len(reports)
snap["others_excl_self"] = len(others)
snap["seat_ids_excl_self"] = sorted(prefixes)
snap["self_file"] = [r["file"] for r in reports if r["is_self"]]
snap["duplicate_prefixes_excl_self"] = dups
snap["empty_reports"] = empty
snap["tiny_reports_under_200_bytes"] = tiny
snap["header_token_misses"] = token_miss
snap["non_report_files_in_seats"] = non_report
snap["scratch_dirs"] = scratches
snap["reports"] = reports

producers = {}
for rel in ["corpus/knowledge/r102-push-synthesis-r95-r102.md",
            "corpus/knowledge/r102-debt-ledger.json",
            "corpus/knowledge/r102-freshness-sweep.md"]:
    p = os.path.join(ROOT, rel)
    producers[rel] = ({"present": False} if not os.path.isfile(p) else
                      {"present": True, "bytes": os.path.getsize(p),
                       "sha16": sha16(p), "mtime_utc": mtime_utc(p)})
snap["producer_artifacts"] = producers
snap["receipt_json_present"] = os.path.isfile(os.path.join(ROOT, ".ufo/waves/round-102/receipt.json"))

with open(OUT, "w") as f:
    json.dump(snap, f, indent=1)
print(json.dumps({k: v for k, v in snap.items() if k != "reports"}, indent=1))
print("---REPORTS---")
for r in reports:
    print(r["file"], r["bytes"], r["sha16"], r["mtime_utc"], "token_ok" if r["header_token_first20"] else "TOKEN_MISS")
