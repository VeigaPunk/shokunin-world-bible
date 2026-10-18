# V101 — presence-final (round 99)

**Seat:** V101 `presence-final`. **Role:** last seat of the round-99 128-seat wave. Scope: 128-report presence audit (exclusive paths, prefix duplicates, header/filename match), producer-artifact presence with hashes, and finalizing `receipt.json` `collection_snapshot` because V39 had not written that key. This seat judges **no claim** (C1/C2) and **no axis**.

**Axes for this seat:** presence completeness, hash honesty, snapshot freshness, non-interference with V39's earlier `collection` object.

**Lane root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo). **Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). **HEAD:** `337f0fa52b02626b7687eedbb2d99fab30446fe4`. `git merge-base --is-ancestor 4265df5 HEAD` exited 0. Wave tree uncommitted. Leaf seat: no nested agents, no commits, no pushes, no network.

Writes: this report, `collection_snapshot` on `.ufo/waves/round-99/receipt.json` (V39 had not written that key), and `.ufo/waves/round-99/seats/V101-scratch/`. V39's `collection`, `seats[]`, and `candidate_revision_pinned` are not rewritten.

Roster from the LOG.md round-99 declaration (unchanged; `git diff --stat HEAD -- LOG.md` was empty in V39's audit and HEAD is still `337f0fa`): **S1–S5 + V01–V123 = 128**. Report presence = a top-level `seats/<SEAT>-*.md`. Scratch directories are not reports. All-reports polls subtract SELF (V101).

## 1. Poll

Cadence 20 s. Bound: poll until 127 other reports exist, stall-escape 30 min, recorded not fatal.

The first poll process was killed by a 300 s tool timeout at try 15 (22:08:09, 7 others). A resume at 22:34:27 used a deadline of 22:33:29 that had already passed, so the script substituted a 60 s deadline and exited at 22:35:27 with 42 others. That exit was deadline-math, not a stall: the count was still rising (42 at 22:35, 64 by 22:41). RESUME2 then ran 90 real tries (30 min) from 22:41 and is the bound that counts.

Observed `V101-scratch/poll.log` lines:

```
START 2026-10-17T22:03:29.576299-03:00 roster_others=127 max_tries=90
try=1 ts=22:03:29 others=3 missing=124 dups=0 extra=[] prod_missing=['S1', 'S2', 'S4', 'S5'] art_missing=2 receipt=0
try=15 ts=22:08:09 others=7 missing=120 dups=0 extra=[] prod_missing=['S1', 'S2', 'S5'] art_missing=2 receipt=0
RESUME 2026-10-17T22:34:27.455359-03:00 deadline=2026-10-17T22:35:27.455359-03:00 reason=tool-timeout-killed-first-poll-at-try15
try=16 ts=22:34:27 others=41 missing=86 ...
STALL_ESCAPE try=19 ts=2026-10-17T22:35:27.456975-03:00 others=42 missing=85 deadline=2026-10-17T22:35:27.455359-03:00
RESUME2 ... max_tries=90 reason=prior-resume-deadline-math-fired-60s-not-a-stall; count still rising; continuing the 30-min bound as real tries
try2=90 ts=23:13:45 others=126 missing=1 dups=0 extra=[] prod_missing=[] art_missing=0 receipt=1 delta=0
  missing_seats=V34
STALL_ESCAPE try2=90 ts=2026-10-17T23:13:45.045403-03:00 others=126 missing=1 — 90 tries / 30 min bound, ABSENT recorded not inferred
MISSING=V34
```

V34 was absent at that bound. It was not inferred. `V34-adjudicator.md` then appeared during the post-bound stability window (mtime `2026-10-17T23:14:46-0300`, 21509 bytes, first line `# V34 — adjudicator (round 99)`, sha256 `c5aae42f930ebe1766c78e171208644da7eaea3a4b82caecc6c756987ee28e1f`). No `V34-scratch/` existed at 23:14:00, before that file landed.

## 2. Presence audit

Commands at lane root, after the stability window:

```
$ date '+%Y-%m-%dT%H:%M:%S%z'
2026-10-17T23:15:44-0300
$ find .ufo/waves/round-99/seats -maxdepth 1 -name '*.md' -type f | wc -l
127
$ find .ufo/waves/round-99/seats -maxdepth 1 -name 'S*.md' -type f | wc -l
5
$ find .ufo/waves/round-99/seats -maxdepth 1 -name 'V*.md' -type f | wc -l
122
$ git rev-parse HEAD
337f0fa52b02626b7687eedbb2d99fab30446fe4
$ git rev-parse 4265df5
4265df5e86e4121bde4125b649b89bb1676676a5
$ git merge-base --is-ancestor 4265df5 HEAD && echo baseline_is_ancestor=yes
baseline_is_ancestor=yes
```

`python3 .ufo/waves/round-99/seats/V101-scratch/audit.py` (read-only; writes only scratch JSON):

```
AUDIT2 2026-10-17T23:15:24-0300 incl 127 excl 127 absent ['V101']
dups {}
h1 []
token []
unexpected []
tiny []
prod_absent []
missing_cand []
```

Twenty seconds later, same command:

```
AUDIT3 2026-10-17T23:15:44-0300 incl 127 absent ['V101']
new_seats []
gone_seats []
changed_reports []
changed_arts []
h1 0 dups {} tiny []
```

At that snapshot, before this file existed: **127/128 present, only V101 unwritten, V34 present**. Header check: first line must start with `# <seat>`, and the seat token must appear in the first 20 lines. Both miss lists were empty. No duplicate prefixes. No unexpected top-level `*.md`. No report under 80 bytes.

Producer reports: `S1-full-file-pins.md`, `S2-tools-docs.md`, `S3-fixture-author.md`, `S4-fixture-docs.md`, `S5-knowledge-author.md`. S2's first line is `# S2 tools-docs — round-99 seat report`; S5's is `# S5 knowledge-author — round 99`. Both match the prefix rule.

Non-report top-level file that is not a `*-scratch/` directory: `V36-debt.json` (companion data, not a report). 120 `*-scratch/` directories were also present; they are not counted as reports.

After this file is written the live roster is 128/128. The `collection_snapshot` written in the next step includes this file. This report does not embed that snapshot's sha256 of itself (quoting it would change the bytes).

## 3. Strays

Parent tree `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/` exists. It is scratch, not a second report set. `find` of that tree returned 8 files and no top-level `*.md`:

```
.../seats/V69-scratch/before/baseline-root/corpus/tools/dependency_freeze.py
.../seats/V69-scratch/before/baseline-root/corpus/tools/dependency-freeze-contract.json
.../seats/V73-scratch/selftests/boundary.out
.../seats/V73-scratch/selftests/boundary.err
.../seats/V73-scratch/selftests/map.out
.../seats/V73-scratch/selftests/map.err
.../seats/V73-scratch/selftests/freeze.out
.../seats/V73-scratch/selftests/freeze.err
```

`/home/vgpnk/Projects/shokunin/corpus` does not exist. No parent-tree copy of a seat report.

`git status --porcelain` at 23:14 also showed `?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`. That path is outside this wave's seats directory. This seat did not write it and does not count it as a round-99 report.

## 4. Producer artifacts

All 16 declared paths existed at the 23:15:44 audit. `missing_candidate_paths` was `[]`. Fixture directory has exactly the ten expected names.

Hashes (sha256, bytes, mtime) from that audit:

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c   29110  2026-10-17T22:38:11-0300  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628   25987  2026-10-17T22:08:46-0300  corpus/tools/dependency-freeze-contract.json
837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c   39310  2026-10-17T23:08:16-0300  corpus/tools/README.md
e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443   17287  2026-10-17T22:51:39-0300  SKILL.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049    6176  2026-10-17T22:03:19-0300  corpus/fixtures/r99-window-lapse/README.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d   17119  2026-10-17T22:02:39-0300  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570       3  2026-10-17T21:36:10-0300  corpus/fixtures/r99-window-lapse/contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984    1793  2026-10-17T21:36:10-0300  corpus/fixtures/r99-window-lapse/entities.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d    5114  2026-10-17T22:01:13-0300  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37    1956  2026-10-17T21:36:10-0300  corpus/fixtures/r99-window-lapse/inspiration-note.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9     139  2026-10-17T21:36:10-0300  corpus/fixtures/r99-window-lapse/relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd     640  2026-10-17T21:36:10-0300  corpus/fixtures/r99-window-lapse/source-excerpt.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15    3293  2026-10-17T22:01:13-0300  corpus/fixtures/r99-window-lapse/sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069    2998  2026-10-17T22:01:13-0300  corpus/fixtures/r99-window-lapse/timeline.json
4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e   20526  2026-10-17T22:57:50-0300  corpus/knowledge/r99-gate-blind-spot-table.md
96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54   14990  2026-10-17T22:57:50-0300  corpus/knowledge/r99-lapse-scope-note.md
```

A mid-poll hash at 23:06:10 matched every path above except `corpus/tools/README.md`, which moved `646784ae7407…` → `837a7f5dfe91…` (mtime 23:08:16) before the stable window. The 23:15:24 and 23:15:44 audits hashed identical artifact bytes. Presence only; this seat does not judge whether the freeze row or the lapse prose is correct.

## 5. Receipt

V39 wrote `.ufo/waves/round-99/receipt.json` (mtime `2026-10-17 22:51:41`, 67825 bytes, sha256 `7b0b5ef2b7308449469923e6286f98e45147d632dcb33b89b90a79c9e1304038`). Its `state` field calls it a skeleton. It has a `collection` object and **no `collection_snapshot` key**.

Observed `collection` at that file, re-read at 23:14 and still unchanged at 23:15 (`stat` mtime still 22:51:41):

```
collection.reports_present = 85
collection.reports_present_excl_self = 84
collection.reports_absent_count = 43
collection.producer_absent = ['S2', 'S5']
missing_candidate_paths = ['corpus/knowledge/r99-gate-blind-spot-table.md', 'corpus/knowledge/r99-lapse-scope-note.md']
receipt_snapshot_utc = 2026-10-17T22:51:41-0300
```

That collection does not match the live roster (127 others at 23:15:44, both knowledge files present, S2 and S5 reports present). It is left in place as V39's snapshot. `collection_snapshot` is the later field.

Write, run after this file exists so the snapshot can hash it:

```
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V101-scratch/audit.py --write-snapshot
```

The writer adds `collection_snapshot` and `collection_snapshot_finalized_by` only. It copies the pre-write receipt bytes to `V101-scratch/prior-receipt.json`. It does not invent `agent_id` or `outcome`. If a later reader needs the post-write receipt digest, it is the sha256 of `receipt.json` after that command; this report does not quote it.

## 6. Verdict

| Check | Result |
|---|---|
| 127 others at poll bound 23:13:45 | no — V34 absent, recorded, not inferred |
| V34 at stable audit 23:15:44 | present (`V34-adjudicator.md`) |
| Roster reports before this file | 127/128, only V101 unwritten |
| Duplicate prefixes | none |
| Header/filename mismatches | none (H1 and first-20 token) |
| Producer artifacts | 16/16 present, hashes above, stable across 20 s |
| Parent seat-report copies | none (8 scratch files only) |
| `collection_snapshot` before this seat | absent; V39 `collection` is the 22:51 skeleton (85 present) |

**Bottom line: PASS — 127 other reports were present and hash-stable at 23:15:44 (V34 landed at 23:14:46, after the 23:13:45 stall-escape that had correctly recorded it ABSENT); producer artifacts 16/16 present; no duplicate prefixes or header mismatches; `collection_snapshot` is written because V39 had not, without rewriting V39's stale `collection`.**
