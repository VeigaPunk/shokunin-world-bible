#!/usr/bin/env python3
"""Resolve path/line/JSON-pointer citations in a scope note. Read-only."""
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
note = Path(sys.argv[1])
text = note.read_text()
lines = text.splitlines()

# citation-convention: bare file:line resolves against this fixture dir
conv = ""
for ln in lines[:8]:
    if ln.startswith("citation-convention:"):
        m = re.search(r"`(corpus/fixtures/[^`]+/)`", ln)
        if m:
            conv = m.group(1)
print(f"citation-convention-base: {conv!r}")

# source: header paths
src = lines[0]
if not src.startswith("source:"):
    print("NO source: header")
else:
    paths = re.findall(r"`([^`]+)`", src)
    missing = []
    for p in paths:
        # strip {a,b} brace groups into concrete paths, and drop parentheticals
        p = re.sub(r"\s*\([^)]*\)\s*$", "", p).strip()
        if "{" in p and "}" in p:
            pre, rest = p.split("{", 1)
            inner, post = rest.split("}", 1)
            for name in inner.split(","):
                cand = (pre + name.strip() + post).strip()
                if not (ROOT / cand).exists():
                    missing.append(cand)
        else:
            # section qualifiers are not paths
            if p.startswith("corpus/") and not (ROOT / p.split()[0]).exists():
                # try path before space
                base = p.split()[0]
                if not (ROOT / base).exists():
                    missing.append(p)
    print(f"source-tokens: {len(paths)} missing: {missing}")

# every backtick token that looks like a path
backticks = re.findall(r"`([^`\n]+)`", text)
print(f"backtick-tokens: {len(backticks)}")

file_cache = {}

def load(rel):
    rel = rel.strip()
    if rel not in file_cache:
        p = ROOT / rel
        if not p.is_file():
            file_cache[rel] = None
        else:
            file_cache[rel] = p.read_text().splitlines()
    return file_cache[rel]


def resolve_json_pointer(rel, pointer):
    p = ROOT / rel
    if not p.is_file():
        return False, "missing-file"
    try:
        data = json.loads(p.read_text())
    except Exception as e:
        return False, f"json-error {e}"
    if not pointer.startswith("#/"):
        return False, "bad-pointer"
    cur = data
    for part in pointer[2:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except Exception:
                return False, f"index-miss {part}"
        elif isinstance(cur, dict):
            if part not in cur:
                return False, f"key-miss {part}"
            cur = cur[part]
        else:
            return False, f"scalar-at {part}"
    return True, type(cur).__name__


# Walk line by line, track most recently named path for bare :NN
path_re = re.compile(r"`((?:corpus/fixtures|corpus/knowledge|corpus/tools)/[^`]+?)`")
bare_file_re = re.compile(
    r"`((?:[A-Za-z0-9_.-]+\.(?:json|md|py))(?:#/[\w/~.-]+)?(?::\d+(?:-\d+)?)?)`"
)
cited = 0
bad = []
last_path = None

for i, ln in enumerate(lines, 1):
    # update last_path from any full path on this line
    for m in path_re.finditer(ln):
        raw = m.group(1)
        # strip trailing :line or #/pointer for existence of the file
        filepart = re.split(r"[:#]", raw, maxsplit=1)[0]
        if (ROOT / filepart).is_file() or (ROOT / filepart).is_dir():
            last_path = filepart
    # also a path that is the fixture-relative convention base + filename
    for m in re.finditer(r"`([A-Za-z0-9_.-]+\.(?:json|md))(#/[^`:]*)?(:\d+(?:-\d+)?)?`", ln):
        fname, pointer, linerange = m.group(1), m.group(2), m.group(3)
        # skip if this token is inside a full path already
        start = m.start()
        window = ln[max(0, start - 40): start + 1]
        if "corpus/" in window:
            continue
        cited += 1
        base = conv.rstrip("/") if conv else ""
        rel = f"{base}/{fname}" if base else fname
        flines = load(rel)
        if flines is None:
            bad.append((i, m.group(0), f"missing {rel}"))
            continue
        if pointer:
            ok, why = resolve_json_pointer(rel, pointer)
            if not ok:
                bad.append((i, m.group(0), f"pointer {why}"))
        if linerange:
            spec = linerange[1:]
            if "-" in spec:
                a, b = spec.split("-")
                a, b = int(a), int(b)
            else:
                a = b = int(spec)
            if a < 1 or b > len(flines) or a > b:
                bad.append((i, m.group(0), f"line-oob {a}-{b} of {len(flines)} in {rel}"))
        last_path = rel

print(f"bare-file-citations: {cited} bad: {len(bad)}")
for row in bad:
    print(" BAD", row)

# full-path citations with line ranges or pointers
full_bad = []
full_n = 0
full_re = re.compile(
    r"`((?:corpus/fixtures|corpus/knowledge|corpus/tools)/[A-Za-z0-9_./-]+\.(?:json|md|py))(#/[^`:]+)?(:\d+(?:-\d+)?)?`"
)
for i, ln in enumerate(lines, 1):
    for m in full_re.finditer(ln):
        full_n += 1
        rel, pointer, linerange = m.group(1), m.group(2), m.group(3)
        if not (ROOT / rel).is_file():
            full_bad.append((i, rel, "missing-file"))
            continue
        if pointer:
            ok, why = resolve_json_pointer(rel, pointer)
            if not ok:
                full_bad.append((i, m.group(0), f"pointer {why}"))
        if linerange:
            flines = load(rel)
            spec = linerange[1:]
            if "-" in spec:
                a, b = spec.split("-")
                a, b = int(a), int(b)
            else:
                a = b = int(spec)
            if flines is None or a < 1 or b > len(flines) or a > b:
                n = 0 if flines is None else len(flines)
                full_bad.append((i, m.group(0), f"line-oob {a}-{b} of {n}"))

print(f"full-path-citations: {full_n} bad: {len(full_bad)}")
for row in full_bad:
    print(" FULLBAD", row)

# quoted strings: compare each "..." of length >= 20 against the note's own cited files is done separately
print("NOTE_LINES", len(lines))
print("NOTE_SHA_PENDING")
