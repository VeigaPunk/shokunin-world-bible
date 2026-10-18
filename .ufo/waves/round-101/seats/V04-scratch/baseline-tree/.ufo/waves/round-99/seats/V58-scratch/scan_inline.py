#!/usr/bin/env python3
"""Scan live round-99 poller command lines for all-reports / mutual-wait patterns.

Read-only. Reads /proc/<pid>/cmdline for processes whose cmd mentions round-99.
Classifies:
  - counts of seats/*.md compared against a high threshold
  - SELF subtraction (grep -v own seat, or explicit SELF/nonself)
  - bounded loop (range/seq/for i in 1..N / MAX=)
Writes a snapshot under V58-scratch.
"""
import datetime
import glob
import os
import re

W = "/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99"
OUT = os.path.join(W, "seats/V58-scratch/inline-scan.txt")
PROC = "/proc"


def cmdline(pid):
    try:
        raw = open(f"{PROC}/{pid}/cmdline", "rb").read()
    except OSError:
        return ""
    return raw.replace(b"\x00", b" ").decode("utf-8", "replace")


def seat_from(cmd):
    m = re.search(r"round-99/seats/(S[1-5]|V\d{2,3})-scratch", cmd)
    if m:
        return m.group(1)
    m = re.search(r"\b(V\d{2,3}|S[1-5])\b", cmd)
    return m.group(1) if m else "?"


rows = []
for pid in os.listdir(PROC):
    if not pid.isdigit():
        continue
    cmd = cmdline(pid)
    if "round-99" not in cmd:
        continue
    if "V58-scratch/sampler.py" in cmd or "V58-scratch/scan_inline" in cmd:
        continue
    seat = seat_from(cmd)
    high = re.findall(r"(?:-ge|-gt|>=|>)\s*(1[0-9][0-9]|[5-9][0-9])", cmd)
    counts_md = bool(re.search(r"seats.*\*\.md|\*\.md|name=.?\\.md|glob\(.?\\.md", cmd)) or "*.md" in cmd
    self_named = bool(re.search(rf"grep\s+-v[^\n]*{seat}", cmd)) if seat != "?" else False
    self_generic = bool(re.search(r"\bSELF\b|nonself|subtract", cmd))
    tries = None
    mt = re.search(r"range\(\s*(\d+)\s*\)|seq 1 (\d+)|for .+ in \$\(seq 1 (\d+)\)|MAX\s*=\s*(\d+)", cmd)
    if mt:
        tries = next(g for g in mt.groups() if g)
    bounded = tries is not None or bool(re.search(r"TIMEOUT|DEADLINE|ABSENT|range\(40\)|range\(41\)", cmd))
    # only keep poll-like
    pollish = any(k in cmd for k in ("sleep 20", "sleep(20)", "poll", "for i in", "range("))
    if not pollish and not high:
        continue
    rows.append({
        "pid": pid,
        "seat": seat,
        "high": ",".join(high) if high else "-",
        "counts_md": "YES" if counts_md else "no",
        "self": "YES-named" if self_named else ("YES-generic" if self_generic else "NO"),
        "tries": tries or "-",
        "bounded": "YES" if bounded else "NO",
        "len": len(cmd),
        "head": cmd[:180].replace("\n", " "),
    })

now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
lines = [f"# inline-scan {now} rows={len(rows)}"]
# high-threshold subset
high_rows = [r for r in rows if r["high"] != "-"]
lines.append(f"high_threshold={len(high_rows)}")
for r in high_rows:
    lines.append(
        f"HIGH pid={r['pid']} seat={r['seat']} thr={r['high']} self={r['self']} "
        f"tries={r['tries']} bounded={r['bounded']} counts_md={r['counts_md']}"
    )
    lines.append(f"  head={r['head']}")
lines.append(f"pollish_total={len(rows)}")
# self-inclusive high
si = [r for r in high_rows if r["self"] == "NO" and int(r["high"].split(",")[0]) >= 100]
lines.append(f"self_inclusive_high={len(si)}")
for r in si:
    lines.append(f"  SI pid={r['pid']} seat={r['seat']} thr={r['high']}")
text = "\n".join(lines) + "\n"
open(OUT, "w").write(text)
print(text)
