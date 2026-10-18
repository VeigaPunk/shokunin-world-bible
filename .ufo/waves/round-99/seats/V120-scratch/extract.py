#!/usr/bin/env python3
"""Extract terminal verdict lines and divergence language from landed reports."""
from pathlib import Path
import hashlib
import re
import sys

SEATS = Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats")
TARGETS = [
    ("V28", "calibration", "verdict", "V28-verdict-calibration.md", "V52"),
    ("V29", "depth", "verdict", "V29-verdict-depth.md", "V51"),
    ("V30", "coverage", "verdict", "V30-verdict-coverage.md", "V69"),
    ("V31", "operability", "verdict", "V31-verdict-operability.md", "V82"),
    ("V32", "freshness", "verdict", "V32-verdict-freshness.md", "V91"),
    ("V33", "adjacency", "verdict", "V33-verdict-adjacency.md", "V107"),
    ("V51", "depth", "crosscheck", "V51-crosscheck-depth.md", "V29"),
    ("V52", "calibration", "crosscheck", "V52-crosscheck-calibration.md", "V28"),
    ("V69", "coverage", "crosscheck", "V69-crosscheck-coverage-2.md", "V30"),
    ("V82", "operability", "crosscheck", "V82-crosscheck-operability.md", "V31"),
    ("V91", "freshness", "crosscheck", "V91-crosscheck-freshness.md", "V32"),
    ("V107", "adjacency", "crosscheck", "V107-crosscheck-adjacency.md", "V33"),
]

TOKENS = re.compile(
    r"\b(improved|harmed|unchanged|unprovable|PASS|FAIL|INCONCLUSIVE|ABSENT|"
    r"concur|concurr|agree|agreem|diverg|contradict|disagree|mismatch|MISMATCH)\b",
    re.I,
)


def bottom(text: str) -> str:
    m = re.search(r"(?m)^##+\s*Bottom line\s*$", text)
    if not m:
        # last non-empty 12 lines as fallback, marked
        lines = [ln for ln in text.splitlines() if ln.strip()]
        return "NO-BOTTOM-HEADING\n" + "\n".join(lines[-12:])
    return text[m.start() :].strip()


def classify(blob: str) -> str:
    low = blob.lower()
    flags = []
    for word in ("harmed", "unprovable", "improved", "unchanged"):
        if re.search(rf"\b{word}\b", low):
            flags.append(word)
    for word in ("FAIL", "PASS", "INCONCLUSIVE", "ABSENT"):
        if re.search(rf"\b{word}\b", blob):
            flags.append(word)
    return ",".join(flags) if flags else "UNCLASSIFIED"


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    chunks = []
    for seat, axis, kind, name, pair in TARGETS:
        p = SEATS / name
        chunks.append(f"===== {seat} axis={axis} kind={kind} pair={pair} file={name}")
        if not p.is_file():
            chunks.append("STATUS ABSENT")
            chunks.append("")
            continue
        data = p.read_bytes()
        text = data.decode("utf-8", errors="replace")
        digest = hashlib.sha256(data).hexdigest()
        chunks.append(
            f"STATUS PRESENT bytes={len(data)} sha256={digest} lines={text.count(chr(10))+ (0 if text.endswith(chr(10)) else 1)}"
        )
        b = bottom(text)
        chunks.append("--- BOTTOM ---")
        chunks.append(b)
        chunks.append(f"CLASS {classify(b)}")
        # divergence-bearing lines anywhere
        hits = []
        for i, ln in enumerate(text.splitlines(), 1):
            if TOKENS.search(ln) and re.search(
                r"diverg|contradict|disagree|mismatch|harmed|concur|agree", ln, re.I
            ):
                hits.append(f"L{i}: {ln.strip()}")
        chunks.append(f"--- DIVERGENCE-ISH LINES ({len(hits)}) ---")
        chunks.extend(hits[:80])
        chunks.append("")
    body = "\n".join(chunks) + "\n"
    if out:
        out.write_text(body)
        print(f"wrote {out} bytes={len(body)}")
    else:
        print(body)


if __name__ == "__main__":
    main()
