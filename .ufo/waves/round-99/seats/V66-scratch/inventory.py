#!/usr/bin/env python3
"""V66 second inventory: README / registry / index surfaces vs delivered bytes."""
import hashlib
import os
import re
import subprocess
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
OUT = REPO / ".ufo/waves/round-99/seats/V66-scratch"
SKIP_PREFIXES = (
    ".ufo/",
    ".git/",
    "v05-self-test-scratch/",
)

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()

def git_sha(rel: str):
    p = subprocess.run(
        ["git", "show", f"4265df5:{rel}"],
        cwd=REPO, capture_output=True,
    )
    if p.returncode != 0:
        return None
    return hashlib.sha256(p.stdout).hexdigest()

def rel(p: Path) -> str:
    return str(p.relative_to(REPO))

surfaces = []

# Root and corpus markdown that function as indexes/registries.
named = [
    "README.md",
    "PROVINCE.md",
    "SCORECARD.md",
    "SHONEN.md",
    "LOG.md",
    "l0-questions.md",
    "SKILL.md",
    "corpus/README.md",
    "corpus/fixtures/README.md",
    "corpus/tools/README.md",
]
for n in named:
    surfaces.append(REPO / n)

# Every corpus README outside scratch/ufo.
for p in sorted((REPO / "corpus").rglob("README.md")):
    r = rel(p)
    if r.startswith(SKIP_PREFIXES):
        continue
    if p not in surfaces:
        surfaces.append(p)

# Knowledge notes (registry / decision tables / watch / scope).
for p in sorted((REPO / "corpus/knowledge").glob("*.md")):
    if p not in surfaces:
        surfaces.append(p)

# Pin registries.
for n in [
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/map-obligations-contract.json",
    "corpus/tools/boundary-doc-contract.json",
]:
    surfaces.append(REPO / n)

# Claim maps and excerpt indexes on the continuation chain + r10 registry.
for n in [
    "corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md",
    "corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md",
    "corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md",
    "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md",
    "corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md",
    "corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md",
    "corpus/fixtures/r99-window-lapse/claim-excerpt-map.md",
    "corpus/fixtures/r10-registry-witness/README.md",
]:
    p = REPO / n
    if p.exists() and p not in surfaces:
        surfaces.append(p)

# r99 knowledge if present.
for p in sorted((REPO / "corpus/knowledge").glob("r99-*")):
    if p not in surfaces:
        surfaces.append(p)

lines = []
lines.append("# V66 surface inventory raw")
lines.append("")
for p in surfaces:
    r = rel(p)
    if not p.exists():
        lines.append(f"ABSENT {r}")
        continue
    data = p.read_bytes()
    text = data.decode("utf-8", errors="replace")
    base = git_sha(r)
    wt = sha256(p)
    same = "BASELINE" if base == wt else ("NEW" if base is None else "DRIFT")
    hits = []
    for pat in [
        r"r99",
        r"r98",
        r"Round 99",
        r"Round 98",
        r"172 fixture",
        r"173 fixture",
        r"17 cases",
        r"18 cases",
        r"five JSON",
        r"ten files",
        r"six fixtures",
        r"BR-01",
    ]:
        n = len(re.findall(pat, text))
        if n:
            hits.append(f"{pat}={n}")
    lines.append(f"{same}\t{len(data)}\t{wt[:16]}\t{r}\t{','.join(hits)}")

(OUT / "surfaces.txt").write_text("\n".join(lines) + "\n")
print(f"surfaces={len(surfaces)} written={OUT / 'surfaces.txt'}")
# also dump r99 mentions outside owned producer paths and .ufo
print("--- r99 mentions in tracked-or-corpus md excluding .ufo ---")
