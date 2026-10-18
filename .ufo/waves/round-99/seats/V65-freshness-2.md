# V65 — freshness-2 (round 99)

Seat: V65 freshness-2. Brief: independent stale-pin sweep across ALL knowledge notes — every sha-like token re-verified or flagged. Leaf seat: no nested agents, no commits, no pushes, no network. Only write: this report and `.ufo/waves/round-99/seats/V65-scratch/`. All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` / `sha256sum` / `git`. Baseline r98 closure `4265df5`. HEAD during the round `337f0fa` (closure SCORECARD commit `111b9a3` plus the blocked-dispatch record; `git diff --stat 4265df5` is `LOG.md` only). Axes for this seat: completeness (every sha-like token in every knowledge note), independence (recompute, do not trust producer claims), non-harm (read-only except this report and scratch; never verify a plan).

## Poll-wait — artifacts absent

Protocol: 20 s cadence, 40 tries, artifacts AND producer reports, ABSENT rather than verify a plan. ENDGAME: the poll never waited on SELF (`V65-freshness-2.md` is not a producer report). A first poll was killed after 2 tries because its timeout cap was 300 s (recorded in `V65-scratch/poll.log` lines 1–3); the restart below is the 40-try record.

```text
poll-restart 2026-10-17T22:01:55-03:00
try=1  reports_n=1 names=[S3-fixture-author.md]
try=7  reports_n=2 names=[S3-fixture-author.md,S4-fixture-docs.md]
try=40 reports_n=2 names=[S3-fixture-author.md,S4-fixture-docs.md] arts=[fixture ]
TIMEOUT after 40 2026-10-17T22:15:15-03:00
```

Glob was non-recursive `seats/S*.md` (scratch directories were not counted as reports). Across all 40 tries: no `S1*.md`, no `S2*.md`, no `S5*.md`; `corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md` never appeared. `dependency_freeze.py` mtime settled at 22:07:33 and the contract at 22:08:46; `corpus/tools/README.md` and `SKILL.md` mtimes stayed at 21:32:05 and 21:34:23 (pre-round; unchanged in `git status`).

Bounded stall-escape (one post-timeout recheck, not another 40-loop), 2026-10-17T22:21:18-03:00:

```text
ls .ufo/waves/round-99/seats/S*.md
  S3-fixture-author.md   (5069 bytes, 22:01)
  S4-fixture-docs.md     (9303 bytes, 22:03)
ls corpus/knowledge/r99*          → cannot access (absent)
ls -ld seats/S1-scratch seats/S2-scratch
  S1-scratch  (contains only `before/`; no report)
  S2-scratch  (empty)
find corpus/knowledge -iname '*r99*' -o -iname '*blind-spot*' -o -iname '*lapse*'
  → no hits
git diff --exit-code 4265df5 -- corpus/knowledge
  DIFF_EXIT:0
git status --porcelain -- corpus/knowledge corpus/tools/dependency_freeze.py \
  corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md \
  corpus/fixtures/r99-window-lapse
  M corpus/tools/dependency-freeze-contract.json
  M corpus/tools/dependency_freeze.py
  ?? corpus/fixtures/r99-window-lapse/
```

S1 bytes exist in the working tree but are unreported and still a six-pin chain (no `r99-window-lapse` pin). That is an in-flight plan, not a delivered revision. Not verified as delivered.

## What was swept (existing notes only)

17 files in `corpus/knowledge/*.md`, byte-identical to `4265df5`. Seven contain no sha-like token: `2026-10-12-lore-consistency-checklist.md`, `2026-10-12-lore-decision-table.md` (the only hex-shaped hit is the date stamp `20261012` inside `20261012T163450Z`, not a pin), `r74-slate-wording-decision-table.md`, `r89-cross-cluster-contradiction.md`, `r94-cross-myth-design-comparison.md`, `reference-ledger.md`, `seed.md`. The same date stamp appears in `2026-10-12-malformed-error-patterns.md:9` and is not a pin.

Extractor: `[0-9a-fA-F]{7,64}`, drop pure-digit tokens shorter than 12 unless they are an explicit hash citation. That filter dropped one real pin, recovered by a second pass: `r97-acknowledgment-scope-note.md:64` `` `70795150…` `` (all digits, length 8). Count after recovery: **144** sha-like tokens (143 from the letter-requiring pass + this one). Ledger: `V65-scratch/pin-ledger-pre.json` (the 143; `70795150` is in this report, not that JSON).

Classification against the working tree at classification time, git history of the named tool/checker/map files, and `git rev-parse --verify <token>^{commit}`:

| class | n | meaning |
|---|---:|---|
| CURRENT-FILE | 44 | prefix matches a working-tree sha256 (stable tools; see below) |
| COMMIT | 67 | resolves as a commit; not a current file hash |
| HISTORICAL-BLOB | 20 | matches a committed blob of a named file, not the working tree |
| UNRESOLVED by file/commit index | 12 | re-checked individually below |
| recovered all-digit pin | 1 | `70795150`, re-checked below |

No token was both a current file hash and a commit (`CURRENT-FILE+COMMIT` count 0).

### Current file pins — match delivered stable bytes

Recomputed 2026-10-17T22:21:18-03:00:

```text
sha256sum corpus/fixtures/check_bible.py corpus/tools/support_check.py \
  corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
```

Every `ff9fd2aa` / `ff9fd2aa6811…d1421` citation (holder-assessment-boundary, r91-c9-watch including the full 64-hex pin, r95–r98 notes), every `55a5eb27`, every `86b52949` / full `86b529496214…74a9`, every `2142b991` / full `2142b9917694…2c41`, and `e851f068` (`r97-acknowledgment-scope-note.md:32` → `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` `e851f068cfd7…`) match those bytes. `check_bible.py` is unchanged from `ca7f9ef` (`git show ca7f9ef:corpus/fixtures/check_bible.py | sha256sum` → `ff9fd2aa6811…`, 428 lines, matching the holder note's line count).

C9 watch pin, replayed (checker still `ff9fd2aa…` at the 22:21 recheck):

```text
python3 corpus/tools/discriminate_check.py
# mode=delivered checker_sha256=ff9fd2aa6811… matches_pin=True
# RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
# EXIT:0
python3 corpus/tools/discriminate_check.py --checker e97613c
# REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved
# EXIT:2
```

The tool prints the *delivered* checker hash in both modes (it always hashes `corpus/fixtures/check_bible.py`). The historical blob was hashed separately:

```text
git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | sha256sum
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
```

That matches the holder note's r89 checker pin `e2bb9639` at commit `1b09f3f`. `e97613c` in the watch is a commit pin, not a file-hash pin. It resolves: `git rev-parse --verify e97613c^{commit}` → `e97613cc276f`.

### Commit pins — all resolve except one flagged below

Unique commit prefixes in the notes, each `git rev-parse --verify <token>^{commit}` exit 0: `ca7f9ef`, `5eb9451` / `5eb9451baff217c19d5786405f9b2aa500b7c1b7`, `03c6746`, `2b48ca7` / `2b48ca72033dfd1060b6f81c4cf27ad83deae57f`, `2ea9ef1`, `1b09f3f`, `396c568` / `396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f`, `28706dc`, `a7c6a17` / `a7c6a1773d5994246a76e4eff30d645f161920e0`, `e97613c` / `e97613cc276f5fa9cac49ff1900798cf6863c020`, `dcb2d92`. Holder note line counts checked: `git show 5eb9451:corpus/fixtures/check_bible.py` is 330 lines; `ca7f9ef` is 428. Both match the note.

### Historical blob pins — match the commit they name

```text
git show 2b48ca72033dfd1060b6f81c4cf27ad83deae57f:corpus/fixtures/check_bible.py | sha256sum
  3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237   # r87 table:11 exact
git show 2ea9ef1:corpus/fixtures/check_bible.py | sha256sum → dcacffd6981e…   # holder:130
git show 1b09f3f:corpus/fixtures/check_bible.py | sha256sum → e2bb9639a324…   # holder:130/143
git show f3e09f9:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | sha256sum
  5093d72eb3f2…   # r97 note:32 pre-repair pin
git show abbc3e0:corpus/tools/map_obligations.py | sha256sum → cc1df4dc4068…  # r94, as the r95 addendum says
git show dcb2d92:corpus/tools/map_obligations.py | sha256sum → d1c239ccb214…  # r95 delivered
git show f3e09f9:corpus/tools/map_obligations.py | sha256sum → 2b0ba815326b…  # r96 delivered
git show dcb2d92:corpus/tools/map-obligations-contract.json | sha256sum → 8173bb97592a…
git show f3e09f9:corpus/tools/map-obligations-contract.json | sha256sum → 97b76bb8b1fe…
git show 4265df5:corpus/tools/dependency_freeze.py | sha256sum
  03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b
git show 4265df5:corpus/tools/dependency-freeze-contract.json | sha256sum
  153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947
```

`03d04365` and `153ebc5b` in `r98-clerk-scope-note.md` are accurate as **r98-delivered** pins (the dated correction at `:74-82` says so, and says to re-derive before citing). They are **not** the working-tree bytes at the stall-escape:

```text
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
```

No knowledge note cites `6f81f8be` or `8c2561b0`. The in-flight contract (read only to see whether a note's pin had been superseded) has `schema_version` 2, `payload_schema_version` 2, 10 `pinned_files`, pins still the six r88–r98 fixtures, `revision` `337f0fa52b02626b7687eedbb2d99fab30446fe4`. No r99 knowledge note exists to record or correct that. Flagged, not scored as a delivered-revision stale pin: the notes' own claim is r98-delivered, and that claim matches `4265df5`.

### Flagged (unresolved by file/commit index, each re-checked)

1. **`b6ca1e902f2bf08b8acddaef665d9764f8636981` / `b6ca1e9`** — `2026-10-12-malformed-error-patterns.md:9`, claimed as a baseline report commit. Does not resolve:

```text
git rev-parse --verify b6ca1e902f2bf08b8acddaef665d9764f8636981^{commit}
  fatal: Needed a single revision
git cat-file -t b6ca1e902f2bf08b8acddaef665d9764f8636981
  fatal: git cat-file: could not get object info
git log --all --oneline | grep b6ca1e9
  (no hit)
```

Carried, not introduced this round: the file's only history line is `60f4956 lore r5: measured malformed-input error patterns`, and `git diff --exit-code 4265df5 -- corpus/knowledge` is empty. **FLAG: unresolved commit pin. Pre-existing. Not a round-99 pin.**

2. **Labeled in-flight hashes, never in the committed history of the file they name.** `git log --all` blob hashes for `corpus/tools/map_obligations.py` are exactly `cc1df4dc4068`, `d1c239ccb214`, `2b0ba815326b`, `86b529496214`. For `dependency-freeze-contract.json`: `c65ac3bd4fc0`, `27273be27d33`, `153ebc5b2092`. None of these prefixes appear:

- `9224a684`, `ca05159e` — `r95-aftermath-scope-note.md:51`, restated as stale at `:61` and `:71` ("do not cite `9224a684…` as current"). Addendum's current pins `86b529496214…` / `2142b9917694…` match the working tree.
- `6634e176` — `r96-response-scope-note.md:55`, restated as stale at `:65` and `:75`. Same addendum pattern; current pins match.
- `c435239d` — `r98-clerk-scope-note.md:64` and `:78`. The dated correction (`:74-82`) says this was the in-flight contract measurement and supersedes it with `153ebc5b` for the r98 delivery. Not in contract history. **FLAG: labeled historical, not current. Accurate as labeled. No r99 correction exists because the r99 note is absent.**
- `70795150` — `r97-acknowledgment-scope-note.md:64`, "an earlier run the same pass". Not in `map_obligations.py` history. The same sentence's receipt pin is `86b52949`, which matches the working tree. **FLAG: labeled in-flight, not current, not in history. Not a silent stale-current pin.**

3. **`da934a7eea6d108f60c71534e8beb218a532eb55b20217a04ab86d82bc6c7e05`** — `r93-r8-worked-example.md:116`, `EXPECTED_RECORD_SHA256`. Not a file hash (the file's own sha256 is `ddac48a1c7690ea3…`). It is the UTF-8 JSON digest of the 12 normalized cells under `### Corrected illustrative R8 review record`, as the note specifies. Replay from the lane root:

```text
D2_DOSSIER=corpus/knowledge/r93-r8-worked-example.md python3 - <<'PY'
# parser as specified in the note: FIELDS order, whitespace-collapsed cells,
# json.dumps(..., ensure_ascii=False, separators=(',', ':'))
# fields 12 missing []
# digest da934a7eea6d108f60c71534e8beb218a532eb55b20217a04ab86d82bc6c7e05
# MATCH
# payload_len 3228
PY
```

**Re-verified. Not stale. Not a file pin.**

## Not done (would be verifying a plan)

- No verdict on `r99-gate-blind-spot-table.md` or `r99-lapse-scope-note.md` — both absent at try 40 and at the 22:21 recheck.
- No verdict that the in-flight `dependency_freeze.py` `6f81f8be…` / contract `8c2561b0…` is the delivered revision. S1's report is absent. The contract still has six pins and `revision` `337f0fa` (HEAD), not a frozen r99 chain.
- S3 and S4 reports exist; they were not used as evidence for any pin. This seat does not score C1 or C2.

## Bottom line

**ABSENT** — after 40 poll tries (22:01:55–22:15:15) and one post-timeout recheck (22:21:18), `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, and producer reports S1/S2/S5 were still absent, so there is no delivered-revision freshness verdict; the 17 existing notes (byte-identical to `4265df5`) were swept anyway — 144 sha-like tokens re-verified or flagged, with `b6ca1e9` the only unresolved commit pin and it is pre-existing, not a round-99 pin.
