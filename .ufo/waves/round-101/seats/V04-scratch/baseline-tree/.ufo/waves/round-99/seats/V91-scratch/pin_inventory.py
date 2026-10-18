#!/usr/bin/env python3
"""Classify hash-shaped pins in durable docs against a named revision.

Read-only. Writes nothing. Prints a classification table.
"""
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
HEX = re.compile(r"(?<![0-9a-f])[0-9a-f]{12,64}(?![0-9a-f])")
HIST = re.compile(
    r"historical|superseded|in-flight|before \(|prior text|delivered history|"
    r"correction addendum|dated correction|unrewritten|r9[0-8] closure|"
    r"never committed|stale",
    re.I,
)

WATCH = [
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/README.md",
    "corpus/tools/map_obligations.py",
    "corpus/tools/map-obligations-contract.json",
    "corpus/tools/support_check.py",
    "corpus/tools/boundary_doc_check.py",
    "corpus/fixtures/check_bible.py",
    "SKILL.md",
    "corpus/fixtures/README.md",
    "corpus/README.md",
    "SCORECARD.md",
    "LOG.md",
    "corpus/knowledge/r95-aftermath-scope-note.md",
    "corpus/knowledge/r96-response-scope-note.md",
    "corpus/knowledge/r97-acknowledgment-scope-note.md",
    "corpus/knowledge/r98-clerk-scope-note.md",
    "corpus/knowledge/r99-lapse-scope-note.md",
    "corpus/knowledge/r99-gate-blind-spot-table.md",
    "corpus/knowledge/r91-c9-watch.md",
]


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def live_hash(rel: str):
    p = LANE / rel
    if not p.is_file():
        return None
    return sha_bytes(p.read_bytes())


def git_hash(rev: str, rel: str):
    try:
        data = subprocess.check_output(
            ["git", "-C", str(LANE), "show", f"{rev}:{rel}"],
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return None
    return sha_bytes(data)


def iter_docs():
    roots = [LANE / "corpus", LANE / "SKILL.md"]
    for root in roots:
        if root.is_file():
            yield root
            continue
        if not root.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in {".git", "__pycache__"}]
            for name in filenames:
                if name.endswith((".md", ".json")):
                    yield Path(dirpath) / name


def main():
    rev = sys.argv[1] if len(sys.argv) > 1 else "4265df5"
    print(f"# pin inventory against live bytes; baseline rev {rev}")
    known = {}
    for rel in WATCH:
        h = live_hash(rel)
        b = git_hash(rev, rel)
        known[rel] = h
        flag = "ABSENT" if h is None else ("SAME" if h == b else "DIFF")
        print(f"HASH {flag} live={h or '-'} base={b or '-'} {rel}")

    prefixes = []
    for rel, h in known.items():
        if h:
            prefixes.append((h, rel, "live"))
        b = git_hash(rev, rel)
        if b and b != h:
            prefixes.append((b, rel, f"base-{rev[:7]}"))

    # also index every fixture file hash (live) so content-digest fragments can match
    fix = LANE / "corpus" / "fixtures"
    if fix.is_dir():
        for dirpath, dirnames, filenames in os.walk(fix):
            for name in filenames:
                p = Path(dirpath) / name
                if p.suffix.lower() not in {".json", ".md"}:
                    continue
                rel = str(p.relative_to(LANE))
                prefixes.append((sha_bytes(p.read_bytes()), rel, "fixture-file"))

    hits = []
    for doc in iter_docs():
        try:
            text = doc.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        rel = str(doc.relative_to(LANE))
        for i, line in enumerate(text.splitlines(), 1):
            for m in HEX.finditer(line):
                token = m.group(0)
                if len(token) < 12:
                    continue
                # skip pure line-looking short tokens that are not hashes: require
                # at least one a-f and length >= 12 already; drop all-digit.
                if not re.search(r"[a-f]", token):
                    continue
                matches = []
                for full, src, kind in prefixes:
                    if full.startswith(token) or token.startswith(full[: len(token)]):
                        matches.append(f"{kind}:{src}:{full[:12]}")
                window = line.lower()
                hist = bool(HIST.search(window))
                hits.append((rel, i, token, hist, matches, line.strip()[:180]))

    print(f"PIN_HITS {len(hits)}")
    unmatched = 0
    for rel, i, token, hist, matches, snippet in hits:
        if not matches:
            unmatched += 1
            tag = "UNMATCHED-HIST" if hist else "UNMATCHED"
        else:
            tag = "MATCH-HIST" if hist else "MATCH"
        print(f"{tag}\t{rel}:{i}\t{token[:16]}\tm={len(matches)}\t{snippet}")
    print(f"UNMATCHED_COUNT {unmatched}")


if __name__ == "__main__":
    main()
