#!/usr/bin/env python3
"""V123 presence audit snapshot. Read-only. Writes only under V123-scratch."""
import hashlib
import os
import re
import json
from datetime import datetime
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SEATS = ROOT / ".ufo/waves/round-99/seats"
ROSTER = SEATS / "V99-scratch/roster.txt"
OUT = SEATS / "V123-scratch"

PRODUCERS = [
    "corpus/tools/dependency_freeze.py",
    "corpus/tools/dependency-freeze-contract.json",
    "corpus/tools/README.md",
    "SKILL.md",
    "corpus/fixtures/r99-window-lapse/README.md",
    "corpus/fixtures/r99-window-lapse/claim-excerpt-map.md",
    "corpus/fixtures/r99-window-lapse/contradictions.json",
    "corpus/fixtures/r99-window-lapse/entities.json",
    "corpus/fixtures/r99-window-lapse/fictional-excerpts.md",
    "corpus/fixtures/r99-window-lapse/inspiration-note.md",
    "corpus/fixtures/r99-window-lapse/relations.json",
    "corpus/fixtures/r99-window-lapse/source-excerpt.md",
    "corpus/fixtures/r99-window-lapse/sources.json",
    "corpus/fixtures/r99-window-lapse/timeline.json",
    "corpus/knowledge/r99-gate-blind-spot-table.md",
    "corpus/knowledge/r99-lapse-scope-note.md",
]

EXPECTED_REPORT = {
    "S1": "S1-full-file-pins.md",
    "S2": "S2-tools-docs.md",
    "S3": "S3-fixture-author.md",
    "S4": "S4-fixture-docs.md",
    "S5": "S5-knowledge-author.md",
    "V39": "V39-receipt.md",
    "V99": "V99-receipt-3.md",
    "V101": "V101-presence-final.md",
    "V123": "V123-presence-final-2.md",
}

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def seat_id_from_name(name: str):
    m = re.match(r"^(S[1-5]|V\d+)-", name)
    return m.group(1) if m else None

def main():
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    roster_ids = []
    if ROSTER.exists():
        for line in ROSTER.read_text(encoding="utf-8", errors="replace").splitlines():
            m = re.match(r"^(S[1-5]|V\d+)\b", line)
            if m:
                roster_ids.append(m.group(1))
    else:
        roster_ids = ["S1", "S2", "S3", "S4", "S5"] + [f"V{i:02d}" if i < 100 else f"V{i}" for i in range(1, 124)]
        # V01-V09 are zero-padded in expected.json; roster uses V01..V09 and V100+
        # rebuild properly below if roster missing

    reports = sorted(p for p in SEATS.glob("*.md") if p.is_file())
    by_prefix = {}
    stray = []
    for p in reports:
        sid = seat_id_from_name(p.name)
        if not sid:
            stray.append(p.name)
            continue
        by_prefix.setdefault(sid, []).append(p)

    lines = []
    lines.append(f"SNAPSHOT {now}")
    lines.append(f"roster_ids {len(roster_ids)}")
    lines.append(f"md_reports {len(reports)}")
    lines.append(f"stray_md {stray}")
    dup = {k: [x.name for x in v] for k, v in by_prefix.items() if len(v) > 1}
    lines.append(f"duplicate_prefixes {dup}")

    present = []
    absent = []
    for sid in roster_ids:
        hits = by_prefix.get(sid, [])
        if hits:
            p = hits[0]
            st = p.stat()
            present.append(sid)
            lines.append(
                f"SEAT {sid} PRESENT {p.name} bytes={st.st_size} mtime={datetime.fromtimestamp(st.st_mtime).astimezone().isoformat(timespec='seconds')} n={len(hits)}"
            )
        else:
            absent.append(sid)
            scratch = list(SEATS.glob(f"{sid}-scratch"))
            lines.append(f"SEAT {sid} ABSENT scratch={'yes' if scratch else 'no'}")

    extra = sorted(set(by_prefix) - set(roster_ids))
    lines.append(f"extra_prefixes {extra}")
    lines.append(f"present_count {len(present)}")
    lines.append(f"absent_count {len(absent)}")
    lines.append("ABSENT_LIST " + ",".join(absent))

    # header/filename check for present reports
    mism = []
    for sid, hits in by_prefix.items():
        p = hits[0]
        head = p.read_text(encoding="utf-8", errors="replace").splitlines()[:25]
        blob = "\n".join(head)
        # require the seat token to appear
        if not re.search(rf"\b{re.escape(sid)}\b", blob):
            mism.append(p.name)
    lines.append(f"header_prefix_mismatch {mism}")

    lines.append("--- PRODUCER ARTIFACTS ---")
    for rel in PRODUCERS:
        p = ROOT / rel
        if not p.is_file():
            lines.append(f"ART ABSENT {rel}")
            continue
        st = p.stat()
        lines.append(
            f"ART PRESENT {sha256(p)} bytes={st.st_size} mtime={datetime.fromtimestamp(st.st_mtime).astimezone().isoformat(timespec='seconds')} {rel}"
        )

    receipt = ROOT / ".ufo/waves/round-99/receipt.json"
    if receipt.is_file():
        lines.append(f"RECEIPT PRESENT {sha256(receipt)} bytes={receipt.stat().st_size}")
        try:
            data = json.loads(receipt.read_text(encoding="utf-8"))
            lines.append("RECEIPT_KEYS " + ",".join(list(data)[:40]))
            # pull collection-ish fields if present
            def walk(obj, prefix=""):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        if k in ("reports_present", "reports_absent", "reports_present_incl_self", "state", "collection"):
                            if k == "collection" and isinstance(v, dict):
                                lines.append("RECEIPT_COLLECTION_KEYS " + ",".join(v.keys()))
                                for ck in ("reports_present", "reports_absent", "reports_present_incl_self", "state"):
                                    if ck in v:
                                        val = v[ck]
                                        if isinstance(val, list):
                                            lines.append(f"RECEIPT collection.{ck} n={len(val)} {val[:8]}{'...' if len(val)>8 else ''}")
                                        else:
                                            lines.append(f"RECEIPT collection.{ck} {val}")
                            elif not isinstance(v, (dict, list)):
                                lines.append(f"RECEIPT {prefix}{k} {v}")
                            elif isinstance(v, list) and k == "reports_absent":
                                lines.append(f"RECEIPT {prefix}{k} n={len(v)}")
            walk(data)
        except Exception as e:
            lines.append(f"RECEIPT_PARSE_ERROR {e}")
    else:
        lines.append("RECEIPT ABSENT .ufo/waves/round-99/receipt.json")

    for sid, fname in EXPECTED_REPORT.items():
        p = SEATS / fname
        lines.append(f"EXPECTED_NAME {sid} {fname} {'PRESENT' if p.is_file() else 'ABSENT'}")

    text = "\n".join(lines) + "\n"
    stamp = datetime.now().strftime("%H%M%S")
    outp = OUT / f"audit-{stamp}.txt"
    outp.write_text(text, encoding="utf-8")
    latest = OUT / "audit-latest.txt"
    latest.write_text(text, encoding="utf-8")
    print(text)
    print(f"WROTE {outp}")

if __name__ == "__main__":
    main()
