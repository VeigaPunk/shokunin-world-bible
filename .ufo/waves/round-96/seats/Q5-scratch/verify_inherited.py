#!/usr/bin/env python3
"""Q5 scratch: verify r96 fictional-excerpts.md is a preserving copy of r95 lines 1-31
and that every inherited anchor still greps at its r95 line number."""
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
R95 = ROOT / "corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md"
R96 = ROOT / "corpus/fixtures/r96-crossing-response/fictional-excerpts.md"

INHERITED = [
    ("J01", "Aru carried the north lantern at Quiet Rise", (12, 12)),
    ("J02", "Evin held the south bell at Salt Court", (13, 13)),
    ("J03", "Aru carried the north lantern at Quiet Rise", (12, 12)),
    ("J04", "Evin held the south bell at Salt Court", (13, 13)),
    ("J05", "The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.", (17, 17)),
    ("J06", "Tick 9: Aru carried the north lantern at Quiet Rise.", (12, 12)),
    ("J07", "Tick 9: Evin held the south bell at Salt Court.", (13, 13)),
    ("J08", "north lantern at Quiet Rise", (12, 12)),
    ("J09", "south bell at Salt Court", (13, 13)),
    ("J10", "After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.", (18, 18)),
    ("J11", "There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.", (19, 19)),
    ("J12", "Aru carried the north lantern at Quiet Rise", (12, 12)),
    ("J13", "Evin held the south bell at Salt Court", (13, 13)),
    ("J14", "Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.", (18, 20)),
    ("J15", "Tick 11: I waited at the Chalk Stair through the agreed bell.", (22, 31)),
]

def grep_hits(anchor, path):
    r = subprocess.run(["grep", "-nF", "--", anchor, str(path)], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return [int(line.split(":", 1)[0]) for line in r.stdout.splitlines()]

def main():
    r95_lines = R95.read_text(encoding="utf-8").splitlines(keepends=True)
    r96_lines = R96.read_text(encoding="utf-8").splitlines(keepends=True)
    print(f"r95 lines={len(r95_lines)} r96 lines={len(r96_lines)}")
    prefix = min(31, len(r96_lines))
    identical = r95_lines[:prefix] == r96_lines[:prefix]
    print(f"PREFIX lines 1-{prefix} byte-identical={identical}")
    if not identical:
        for i, (a, b) in enumerate(zip(r95_lines[:prefix], r96_lines[:prefix]), 1):
            if a != b:
                print(f"  DIFF line {i}: r95={a!r} r96={b!r}")
    ok = identical
    for row_id, anchor, (lo, hi) in INHERITED:
        hits = grep_hits(anchor, R96)
        inside = hits is not None and all(lo <= h <= hi for h in hits)
        print(f"{'OK ' if inside else 'BAD'} {row_id} hits={hits} span={lo}-{hi}")
        ok = ok and inside
    print("INHERITED", "ALL-OK" if ok else "PROBLEM")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
