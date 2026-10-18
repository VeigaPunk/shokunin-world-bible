# V36 — receipt (round 98, completion-wave seat)

**Seat:** V36 `receipt`. **Role:** presence audit of all 64 declared round-98
seats and authoring of the round receipt at
`.ufo/waves/round-98/receipt.json`. V36 judges **no claim** (C1/C2/C3) and
**no axis** — presence, byte hashes and the dispatch process record only. It
does not re-adjudicate any seat's verdict and does not smooth any ABSENT into
a presence.

**Lane root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin`
(the session cwd is the parent repo, so every path below is absolute or
repo-relative to that lane root). **Baseline:** r97 closure `9a3d648`
(full `9a3d64846632163cb0db1efbc6788b15337a2a60`). **HEAD at snapshot:**
`dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` (`dd4df1b` r97 close). The wave
tree is uncommitted (`?? .ufo/waves/round-98/`). Leaf seat: no nested agents,
no commits, no pushes, no network. Writes confined to this report and the
declared receipt path.

## 1. Dispatch context — two waves

The round was declared as **one** batched 64-seat
`opencode-go/deepseek-v4.1-flash` wave: 5 producer seats (S1–S5,
exclusive byte-ownership) plus 59 verifier/judge seats (V01–V59). A host
interruption **aborted 6 endgame seats before they wrote their reports** —
**V20, V31, V36, V51, V57, V58**. Those six were re-dispatched as a separate
**6-seat completion wave on `hyper/deepseek-v4.1-flash`**; this report is the
**V36 re-dispatch**. The main wave's other 58 seats completed and their
reports are on disk. The receipt records both waves explicitly (see
`process_notes` in `receipt.json`); the aborted seats are marked
`re_dispatched_on_hyper: true` and are never recorded as "completed in the
main wave".

## 2. Method

Presence audit re-run at **2026-10-17T21:22-0300** and again at receipt write.
The aborted V36 left usable partial artifacts in `seats/V36-scratch/`:
`V36-receipt-builder.py`, `V36-summary-205436.txt` (a 20:54:36 snapshot
carrying 58 report hashes), `V36-poll.log` (poll to 21:04:43, "STALL READY
held, reports=58 unchanged for 60 tries"), and `V36-own-receipt-sha.txt`.
This seat reconciled against that 20:54 snapshot and re-audited live. The
`receipt.json` on disk before this seat was the aborted V36's **20:29:02
skeleton** (`collection.reports_present: 0`, state "Skeleton receipt written by
V36"); it is **superseded**, and its verbatim bytes are preserved inside the new
receipt under `skeleton_superseded` rather than silently overwritten.

Commands and observed output:

```sh
$ ls -1 .ufo/waves/round-98/seats/*.md | wc -l
58
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
172
$ git rev-parse HEAD
dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb
$ git merge-base --is-ancestor 9a3d648 HEAD && echo yes
yes
```

## 3. Presence audit — 64 declared seats

Declared roster = **S1–S5 (5) + V01–V59 (59) = 64**.

| Class | Count | Seats |
|---|---|---|
| Present at this seat's first audit (21:22 -0300) | 58 | S1–S5; V01–V19, V21–V30, V32–V35, V37–V50, V52–V56, V59 |
| Absent at 21:22 | 6 | V20, V31, V36, V51, V57, V58 |
| Present at the receipt's final snapshot | **64** | all S1–S5 and V01–V59 |

The 6 seats absent at 21:22 were **exactly** the completion-wave seats. They
landed during the receipt window, in this order: `V36-receipt.md` (this seat),
then `V20-scope-creep.md` and `V58-presence-final.md`, then
`V31-adjudicator.md`, `V51-endgame-monitor.md` and `V57-mutual-wait-guard-2.md`.
The receipt's `collection_snapshot` is the authoritative final presence record
(**64/64 present**); the 21:22 count of 58 is this seat's opening audit and is
superseded by the final snapshot. Absent seats are recorded, never inferred.

`V31-adjudicator.md` was **still being written during the window** — 33,520
bytes at 21:27:14, settled at 33,724 bytes (sha `5e933905…`) at 21:28:44. The
receipt waits for it to settle, records the drift in
`collection_snapshot.in_window_report_mutations`, and the final snapshot
carries the settled bytes; the superseded pre-settle build is listed in
`intermediate_receipts`.

Integrity checks (all clean at snapshot):

- duplicate report prefixes: **none** (no seat has two `*.md` reports);
- header/seat mismatch: **none** (every report's first line begins `# <seat>`);
- unexpected `.md` in `seats/`: **none**;
- parent-tree report strays (`r94-F01` class): **none**;
- misplaced top-level report files: **none**.

`seats/V33-debt.json` is a **data companion** to the report `V33-debt.md`, not
a second report; it is the only non-`.md` top-level entry in `seats/` besides
the `scratch/` directory. Companion files are not counted as reports.

## 4. Corroboration re-run at this snapshot (evidence, not this seat's verdict)

V36's seat does not adjudicate claims, but it re-ran the round's headline
measurements on the delivered revision so the receipt carries first-hand
observation rather than only other seats' quotations. All outputs below were
produced by this seat at the snapshot; they corroborate, and are not a
substitute for, the C1/C2/C3 seat verdicts.

```sh
$ python3 corpus/tools/dependency_freeze.py --self-test
SELF-TEST 17/17
RESULT PASS                                        # rc=0

$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath \
           r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d; done
FREEZE r88-m3-maya-cluster:        events 2/2; dependency-edges 0/0; relations 0/0   RESULT PASS rc=0
FREEZE r94-paired-crossing:        events 3/3; dependency-edges 2/2; relations 1/1   RESULT PASS rc=0
FREEZE r95-crossing-aftermath:     events 4/4; dependency-edges 3/3; relations 1/1   RESULT PASS rc=0
FREEZE r96-crossing-response:      events 5/5; dependency-edges 4/4; relations 1/1   RESULT PASS rc=0
FREEZE r97-crossing-acknowledgment:events 6/6; dependency-edges 5/5; relations 1/1   RESULT PASS rc=0
FREEZE r98-clerk-filing:           events 7/7; dependency-edges 6/6; relations 1/1   RESULT PASS rc=0
# chain 6/6 clean; r97 digest 3c922d20…, r98 digest 59a0f4fa…

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                        # rc=0

$ python3 corpus/tools/map_obligations.py --self-test   # RESULT PASS (tail)
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations   # EXIT-R98=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations   # EXIT-R97=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing   # tail
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS

$ python3 -c "import json; ..."   # r98-clerk-filing table sizes
entities 6; relations 1; contradictions 0; timeline 7; sources 7
```

Independent census (fresh loop over every `corpus/fixtures/*/` directory with
`check_bible.py`; violation lines = lines containing `VIOLATION`), reproducing
V17's declared figure exactly:

```sh
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
172
$ # loop: python3 corpus/fixtures/check_bible.py <dir> for every fixture dir
{"fixture_dirs":172,"clean_exit0":38,"negative_exit1":134,"violation_lines":421,"non_0_1_exits":0}
```

i.e. **172 dirs / 38 clean / 134 negative / 421 VIOLATION lines / zero
non-0/1 exits** — matches V17-preservation-census and the r97 closure census
plus the declared +1 dir / +1 clean.

## 5. Receipt artifact

`receipt.json` (this seat's declared output) carries:

- `record_type: "round-98-receipt"`, `round: 98`, `requested_seats: 64`,
  `requested_model: "opencode-go/deepseek-v4.1-flash"`, `phase` naming the
  two-wave dispatch;
- `baseline_commit`, `head_at_snapshot`, `receipt_snapshot_utc`;
- `candidate_revision_pinned` — sha256 of every delivered candidate file
  (tools + r98 fixture + knowledge notes); `missing_candidate_paths: []`;
- `collection_snapshot` — `reports_expected`, `reports_present`,
  `reports_missing`, the `present` / `missing` seat lists, and the integrity
  lists (duplicate prefixes, header mismatches, strays, unexpected files);
- `process_notes` — the two-wave record (main 64-seat opencode-go wave with 6
  aborts; this 6-seat hyper completion wave);
- `seats[]` — one row per declared seat with `report_path`, `report_sha256`,
  `agent_id: null` (left for the L1 to fill from the real AgentSwarm dispatch
  result — none invented), `outcome: null`, `dispatch_wave`, and
  `re_dispatched_on_hyper` for the six completion seats;
- `skeleton_superseded` — the aborted main-wave V36's 20:29 skeleton, verbatim;
- `intermediate_receipts` — metadata for snapshots this re-dispatch wrote and
  then superseded (the 61-present build), kept as a record rather than a
  silent overwrite.

The report does **not** quote `receipt.json`'s own sha256: doing so would make
the two artifacts mutually hash-dependent (the receipt stores this report's
hash in its `seats[V36]` row). To keep both byte-stable, the receipt records
this report's hash and this report names the receipt by path only.

## 6. Hygiene note (recorded, not judged)

`seats/V37-scratch/archive/` (9,043 `.md`) and `seats/V17-scratch/archive/`
(197 `.md`) hold **9,240 archived historical `.md` copies** (rounds 86–96)
inside scratch directories — 10,242 `.md` in `*-scratch/` overall. They are
**not** top-level report collisions, and **no nested `.git` repository is
present** anywhere under those archives (only a `.gitignore`), so the r97
mirror-freeze gitlink class does not recur; the copies live under seats' own
scratch trees and are outside the report namespace. Also recorded:
`V14-poll.sh` / `V14-poll.log` / `V14-poll2.log` sit at the **wave top level**
(`.ufo/waves/round-98/`), outside `seats/`. Both are process observations for
the L1; V36 attaches no defect verdict.

## 7. Honesty

V36 records presence and bytes. It adjudicates no claim and no axis. Absent
seats are recorded, never inferred. The pre-existing skeleton is superseded
explicitly, with its bytes preserved. The corroboration in §4 is first-hand
observation but is not a C1/C2/C3 verdict; the claim verdicts belong to the
verifier/judge seats and to the round's adjudicator.

**Bottom line:** PASS — 64 declared seats audited; **64/64 reports present at
the receipt's final snapshot** (the six completion-wave seats V20, V31, V36,
V51, V57, V58 were absent at the 21:22 opening audit and all landed during the
receipt window); `receipt.json` written with per-seat `report_path` +
`report_sha256`, present/missing lists, `agent_id: null`, the two-wave process
record, and the aborted V36 skeleton preserved.
