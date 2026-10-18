#!/usr/bin/env python3
"""Atomic V123 presence-final-2 report. Read-only except the report path and this scratch."""
import hashlib
import re
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SEATS = ROOT / ".ufo/waves/round-99/seats"
ROSTER = SEATS / "V99-scratch/roster.txt"
REPORT = SEATS / "V123-presence-final-2.md"
POLL = SEATS / "V123-scratch/poll.log"

V39_HASHES = {
    "S3-fixture-author.md": "3d81a75e0f154ed6c2297da8a9521391797a81740e0ede5443070b0c471cf73a",
    "S4-fixture-docs.md": "61bfdec1f5b7bbcdda653230bb4be1b6c1913683af67e2ae02e4ee46a327f72f",
    "V10-c2-checker.md": "9ee8c876b7ff1be1481c7219b06307163ed5a0553ef168bdda23e677f99f7f45",
    "V11-c2-inherited-equality.md": "a2f60b65b440efd0b178c5c314fc51ded510e8b8bd80db3c0ce6fd87b2d20e03",
    "V12-c2-support-map.md": "b559cdb76adbebc6791e3b784d92188437f4195a828120ac9c9b522028fc9246",
    "V13-c2-anchors.md": "a7ef2d47c29e97cfe41f93800f0fc1a24ca6ad6a636734f4517300d70c2778dd",
    "V41-anchor-replica-2.md": "40af4141891fe1d0a91017080d5ce232e2e252743811ec61dc8c751e984ea0d6",
    "V47-byte-prefix-2.md": "321491fb9b0757f867b5e0cc45338bc106960908f64eb3b8c37aed47ab8c5410",
    "V68-adjacency-2.md": "d1ab2308693704bcb848559e051ede400414cac29807fe8a52f8a734b6d1ae97",
    "V77-c2-map-inventory.md": "e51103276a7db11c4a5c9ed188ec396c34962d320efd1910f0cbea151c8ce7f1",
    "V80-c2-prose-prefix.md": "aaf5b0d1c47b44478bcac40af92c81bb2bce1025d41add69e1494283b08d2cee",
    "V86-c2-no-new-entity.md": "775bd16a31f906bc3cc2f4a14139504598ddd9c907725e4e864412d258b0a38f",
    "V105-c2-event-description.md": "3668a34e84ee36a5ce2e3cdbffe9ce4eb34982f786b53f13013b0bcf39d0d1e2",
    "V109-c2-inherited-map-rows.md": "8bcbd46a1f5888cc99bb7a8e29947a6ae5a81e5455b917ac00d7c5e25495c362",
    "V119-c2-anchors-3.md": "9206493b7fe5fb982f53756d2f1d260d91e6ce265d3c7c7f14277a82efc66b35",
}
V39_TOOL_HASHES = {
    "corpus/tools/dependency_freeze.py": "6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067",
    "corpus/tools/dependency-freeze-contract.json": "8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628",
    "corpus/tools/README.md": "294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207",
    "SKILL.md": "22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5",
}

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


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sh(cmd):
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    out = (p.stdout or "") + (p.stderr or "")
    return p.returncode, out.rstrip("\n")


def iso(ts):
    return datetime.fromtimestamp(ts).astimezone().isoformat(timespec="seconds")


def main():
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    rc_head, head = sh(["git", "rev-parse", "HEAD"])
    rc_base, base = sh(["git", "rev-parse", "4265df5"])
    rc_anc, anc = sh(["git", "merge-base", "--is-ancestor", "4265df5", "HEAD"])
    rc_st, porcelain = sh(["git", "status", "--porcelain"])
    rc_log, logdiff = sh(["git", "diff", "--stat", "HEAD", "--", "LOG.md"])

    roster = []
    expected_name = {}
    for line in ROSTER.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^(S[1-5]|V\d+)\b.*?report\s+(\S+)", line)
        if not m:
            m2 = re.match(r"^(S[1-5]|V\d+)\b", line)
            if m2:
                roster.append(m2.group(1))
            continue
        sid, path = m.group(1), m.group(2)
        roster.append(sid)
        expected_name[sid] = Path(path).name

    # snapshot file list once
    reports = sorted(p for p in SEATS.glob("*.md") if p.is_file() and p.name != REPORT.name)
    by_prefix = {}
    stray = []
    for p in reports:
        m = re.match(r"^(S[1-5]|V\d+)-", p.name)
        if not m:
            stray.append(p.name)
            continue
        by_prefix.setdefault(m.group(1), []).append(p)

    rows = []
    present = []
    absent = []
    header_miss = []
    for sid in roster:
        hits = by_prefix.get(sid, [])
        scratch = (SEATS / f"{sid}-scratch").is_dir()
        if sid == "V123":
            rows.append((sid, "THIS", REPORT.name, "-", "-", "-", "yes"))
            continue
        if not hits:
            absent.append(sid)
            rows.append((sid, "ABSENT", expected_name.get(sid, ""), "-", "-", "-", "yes" if scratch else "no"))
            continue
        p = hits[0]
        digest = sha256(p)
        head_line = p.read_text(encoding="utf-8", errors="replace").splitlines()[:1]
        first = head_line[0] if head_line else ""
        if not re.search(rf"\b{re.escape(sid)}\b", first):
            # fall back: first 20 lines
            blob = "\n".join(p.read_text(encoding="utf-8", errors="replace").splitlines()[:20])
            if not re.search(rf"\b{re.escape(sid)}\b", blob):
                header_miss.append(p.name)
        present.append((sid, p, digest))
        rows.append((sid, "PRESENT", p.name, str(p.stat().st_size), digest, iso(p.stat().st_mtime), "yes" if scratch else "no"))

    extra = sorted(set(by_prefix) - set(roster))
    dups = {k: [x.name for x in v] for k, v in by_prefix.items() if len(v) > 1}

    art_lines = []
    for rel in PRODUCERS:
        p = ROOT / rel
        if not p.is_file():
            art_lines.append(f"ABSENT  {rel}")
            continue
        digest = sha256(p)
        base_note = ""
        if rel in (
            "corpus/tools/dependency_freeze.py",
            "corpus/tools/dependency-freeze-contract.json",
            "corpus/tools/README.md",
            "SKILL.md",
        ):
            rc, blob = sh(["git", "show", f"4265df5:{rel}"])
            if rc == 0:
                bsha = hashlib.sha256(blob.encode() if False else subprocess.check_output(["git", "show", f"4265df5:{rel}"], cwd=ROOT)).hexdigest()
                base_note = " SAME-as-4265df5" if bsha == digest else " DIFF-vs-4265df5"
        v39 = V39_TOOL_HASHES.get(rel)
        v39_note = ""
        if v39:
            v39_note = " MATCH-V39" if v39 == digest else " DRIFT-vs-V39"
        art_lines.append(f"PRESENT {digest} bytes={p.stat().st_size} mtime={iso(p.stat().st_mtime)}{base_note}{v39_note}  {rel}")

    receipt = ROOT / ".ufo/waves/round-99/receipt.json"
    receipt_state = "ABSENT"
    receipt_sha = ""
    if receipt.is_file():
        receipt_sha = sha256(receipt)
        receipt_state = f"PRESENT bytes={receipt.stat().st_size} sha256={receipt_sha}"

    v39 = SEATS / "V39-receipt.md"
    v99 = list(SEATS.glob("V99-*.md"))
    v101 = list(SEATS.glob("V101-*.md"))

    v39_cmp = []
    for name, expected in V39_HASHES.items():
        p = SEATS / name
        if not p.is_file():
            v39_cmp.append(f"MISSING-NOW {name} (V39 hashed {expected})")
            continue
        live = sha256(p)
        if live == expected:
            v39_cmp.append(f"MATCH {name} {live}")
        else:
            v39_cmp.append(f"DRIFT {name} V39={expected} now={live} bytes={p.stat().st_size}")

    poll_tail = ""
    if POLL.is_file():
        lines = POLL.read_text(encoding="utf-8", errors="replace").splitlines()
        poll_tail = "\n".join(lines[:2] + ["..."] + lines[-6:])

    v101_log = SEATS / "V101-scratch/poll.log"
    v101_tail = ""
    v101_mtime = "absent"
    if v101_log.is_file():
        v101_mtime = iso(v101_log.stat().st_mtime)
        v101_lines = v101_log.read_text(encoding="utf-8", errors="replace").splitlines()
        v101_tail = "\n".join(v101_lines[-4:])

    v99_status = SEATS / "V99-scratch/poll-status.json"
    v99_status_txt = v99_status.read_text(encoding="utf-8", errors="replace") if v99_status.is_file() else "ABSENT"

    v39_summary = SEATS / "V39-scratch/audit-summary.txt"
    v39_summary_txt = v39_summary.read_text(encoding="utf-8", errors="replace") if v39_summary.is_file() else "ABSENT"

    # post-hash drift: files that appeared during hashing
    after = sorted(p.name for p in SEATS.glob("*.md") if p.is_file())
    before_names = {p.name for p in reports}
    appeared = [n for n in after if n not in before_names and n != REPORT.name]

    n_present_others = len(present)
    n_absent_others = len(absent)  # excludes V123
    # roster includes V123
    assert "V123" in roster

    table = ["| seat | status | file | bytes | sha256 | mtime | scratch |", "|---|---|---|---:|---|---|---|"]
    for sid, status, fname, nbytes, digest, mtime, scratch in rows:
        shown = digest if digest in ("-",) else digest
        table.append(f"| {sid} | {status} | `{fname}` | {nbytes} | `{shown}` | {mtime} | {scratch} |")

    present_list = ", ".join(sid for sid, _, _ in present)
    absent_list = ", ".join(absent)

    producers_absent_reports = [s for s in ("S1", "S2", "S5") if s in absent]
    knowledge_absent = [rel for rel in PRODUCERS if rel.startswith("corpus/knowledge/") and not (ROOT / rel).is_file()]

    text = f"""# V123 — presence-final-2 (round 99)

**Seat:** V123 `presence-final-2`. **Role:** final failsafe presence audit. Write regardless of whether the wave has closed. 128-seat table, honest ABSENTs, producer artifact hashes, reconcile against V39 / V99 / V101 receipts. Judges **no claim** (C1/C2) and **no axis**. Does not verify a plan. Does not infer a missing report from scratch.

**Axes for this seat:** presence completeness (every declared seat accounted), byte honesty (sha256 only of files that exist), non-interference (this report and `V123-scratch/` only), cutoff honesty (protocol bound quoted; later landings not back-filled into the table).

**Lane root:** `/home/vgpnk/Projects/shokunin/lore-shokunin`. **Baseline:** r98 closure `4265df5`. **HEAD:** `{head}`. Ancestor check exit `{rc_anc}` (`git merge-base --is-ancestor 4265df5 HEAD`). Wave tree uncommitted. Leaf seat: no nested agents, no commits, no pushes, no network.

Roster: **S1–S5 + V01–V123 = 128**, taken from `V99-scratch/roster.txt` (128 lines, prefixes parsed). Report presence = a top-level `seats/<SEAT>-*.md`. Scratch is not a report. This file is excluded from the pre-write count and listed as THIS.

## 1. Poll-wait (SELF subtracted)

Protocol: 20 s cadence, max 40 tries, ~13 min. Early stop only if reports ≥ 127 (others; SELF subtracted). That condition never fired.

Stall-escape 1 (recorded, not fatal): the first poll process was killed by a 300 s tool timeout after try 15 (`2026-10-17T22:07:23-03:00`). Tries 16–40 were restarted in a second process. Numbering in `V123-scratch/poll.log` is continuous.

Stall-escape 2 (recorded, not fatal): try 40 closed at `2026-10-17T22:21:05-03:00` with **14** top-level reports (`S=2 V=12`), V39/V99/V101 reports absent, `receipt.json` absent, knowledge files absent. This report was not written at that second because the reconciliation target (`V39-receipt.md`) had not landed. V39's own poll exhausted at 22:16:26 and their report landed at 22:30:30. Observation continued only long enough to read that receipt, then this snapshot was locked. The wave was still landing; this table is a cutoff, not a closed census. Not extended to V101's 30-minute escape.

Quoted poll log (`V123-scratch/poll.log`):

```
{poll_tail}
```

`arts` flag order: dependency_freeze.py, contract, tools README, SKILL.md, blind-spot table, lapse-scope note, fixture README, fixture map. `YYYYNNYY` through try 40 means the two knowledge files were absent on every try and the other six paths existed as files (existence ≠ producer delivery).

## 2. Write-time snapshot commands

Cutoff timestamp (script start, before hashing): `{now}`.

```
$ git rev-parse HEAD
{head}
$ git rev-parse 4265df5
{base}
$ git merge-base --is-ancestor 4265df5 HEAD; echo exit:$?
exit:{rc_anc}
$ git diff --stat HEAD -- LOG.md
{logdiff or "(empty)"}
$ git status --porcelain
{porcelain or "(empty)"}
```

Pre-write top-level `*.md` count (this file not yet written): **{len(reports)}**. Roster present excluding V123: **{n_present_others}**. Roster absent excluding V123: **{n_absent_others}**. After this write, V123 is present, so on-disk reports become at least {len(reports)+1} if nothing else lands during the write. Files that appeared while hashing (not folded into the table): {appeared or "none"}.

Duplicate prefixes: {dups or "none"}. Unexpected prefixes: {extra or "none"}. Stray `*.md` (no seat prefix): {stray or "none"}. Header/filename mismatches (seat token absent from the first line and the first 20 lines): {header_miss or "none"}.

## 3. 128-seat table

Status PRESENT means the report file existed at the listdir that opened this snapshot. ABSENT means it did not. Scratch yes/no is not presence. sha256 is of the bytes hashed immediately after that listdir. V123 is THIS (this file).

{chr(10).join(table)}

Present others ({n_present_others}): {present_list}

ABSENT others ({n_absent_others}): {absent_list}

Producer reports absent: {producers_absent_reports or "none"}. S1 scratch exists; S2 scratch exists; S5 scratch does not (checked as directory presence at snapshot: S5-scratch is_dir={ (SEATS / "S5-scratch").is_dir() }).

## 4. Producer artifact hashes

Existence and bytes only. Not a C1 or C2 verdict. A file whose owner report is ABSENT is not a confirmed delivery.

```
{chr(10).join(art_lines)}
```

Knowledge files ABSENT: {knowledge_absent or "none"}.

`corpus/tools/README.md` and `SKILL.md` match `4265df5` and HEAD. Their mtimes (21:32 and 21:34) predate this re-dispatch (~22:00). S2 has not delivered an edit. `dependency_freeze.py` and `dependency-freeze-contract.json` differ from `4265df5` / HEAD and match the hashes V39 quoted at 22:22:17; S1's report is still ABSENT, so those bytes are an in-flight tree, not a confirmed S1 delivery.

`corpus/fixtures/r99-window-lapse/` has the ten declared files. S3 and S4 reports are PRESENT. This seat does not re-run `check_bible`, `support_check`, or `map_obligations`.

## 5. Reconciliation against V39 / V99 / V101

### V39 receipt

`V39-receipt.md` at snapshot: {"PRESENT bytes="+str(v39.stat().st_size)+" sha256="+sha256(v39)+" mtime="+iso(v39.stat().st_mtime) if v39.is_file() else "ABSENT"}.

V39's report (read before this snapshot) states a 22:22:17 audit of **15/128** present, **113** absent, producer reports S1/S2/S5 absent, both knowledge files absent, duplicate prefixes none, header mismatches none, and says `.ufo/waves/round-99/receipt.json` is the skeleton. `V39-scratch/audit-summary.txt`:

```
{v39_summary_txt.rstrip()}
```

`receipt.json` at this snapshot: **{receipt_state}**.

That is a claim-vs-disk check, not a rewrite of V39. If `receipt.json` is ABSENT here, V39's prose that the skeleton was written is not matched by the filesystem at this cutoff. If it is PRESENT, its sha256 is above and it was not treated as a finalized L1 receipt (V39 leaves `agent_id` null).

Byte reconciliation of the 15 reports V39 hashed at 22:22:17, re-hashed now:

```
{chr(10).join(v39_cmp)}
```

Tool/doc hashes V39 quoted vs this snapshot are in §4 (`MATCH-V39` / `DRIFT-vs-V39`).

Count drift vs V39's 15: this snapshot has {n_present_others} other reports. The difference is later landings, not a contradiction of V39's earlier audit. V39 said the wave was still landing and that a later seat may supersede the skeleton. That prediction holds.

### V99 receipt-3

`V99-*.md` at snapshot: { [p.name for p in v99] or "ABSENT" }.

`V99-scratch/poll-status.json` (their poll, not a receipt):

```
{v99_status_txt.rstrip()}
```

No V99 receipt to compare 1:1. Their poll, when last read, had not produced `V99-receipt-3.md`. Absence is recorded. Their scratch roster was used only as the seat-name source; it is not a receipt.

### V101 presence-final

`V101-*.md` at snapshot: { [p.name for p in v101] or "ABSENT" }.

`V101-scratch/poll.log` mtime `{v101_mtime}`. Last lines:

```
{v101_tail or "(no log)"}
```

The log stops at try 15 / 22:08:09 and was not updated through this cutoff. No V101 report. No evidence in that log that they finalized `receipt.json`. ABSENT. Not inferred from the frozen log.

## 6. What this seat does not claim

- Not 128/128. Not a closed wave.
- Not a C1 verdict (full-file pins, 18/18, 6/6) and not a C2 verdict (lapse fixture, blind-spot table). The blind-spot table and lapse-scope note were absent, so those claims were not verified. No plan was verified in their place.
- Not an adjudication. Later seats (V101's 30-minute escape, V99 if it writes after this cutoff, the L1) may supersede these counts.
- No `receipt.json` was written by this seat. That path belongs to V39 / V101.

## 7. Honesty

Try 40 (22:21:05) saw 14 reports. This write-time table sees {n_present_others} other reports plus this file. Both numbers are quoted from commands, not smoothed. S1, S2, and S5 reports stayed absent from try 1 through this snapshot. Both knowledge files stayed absent. `receipt.json` state is the filesystem state above, not V39's intention.

**Bottom line: INCONCLUSIVE — failsafe presence audit written at cutoff {now}; {n_present_others}/127 other reports on disk (V123 is this file); S1, S2, S5 reports and both knowledge files honestly ABSENT; V39-receipt.md present but its 22:22:17 census (15 present) is already stale against this later count; receipt.json {receipt_state}; V99 and V101 reports ABSENT; wave still landing after the 40-try bound, so this is not a closed 128-seat census.**
"""
    REPORT.write_text(text, encoding="utf-8")
    print(f"WROTE {REPORT} bytes={REPORT.stat().st_size} present_others={n_present_others} absent_others={n_absent_others} receipt={receipt_state} appeared_during_hash={appeared}")


if __name__ == "__main__":
    main()
