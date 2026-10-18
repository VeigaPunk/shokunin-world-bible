# V92 — cross-seat-2 (round 99)

**Seat:** V92 cross-seat-2 (verifier, single-wave round-99 re-dispatch, lore-shokunin).
**Scope (verbatim):** *Second cross-seat audit: 8 different quoted outputs than V50; REPRODUCED/MISMATCHED.*
**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin`. Session cwd is the parent repo; every path below is absolute or `cd`-anchored at the lane root. All commands used `python3`.
**Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD during this seat: `337f0fa` (blocked-dispatch log commit; not used as a wave floor).
**Writes of this seat:** this report and `.ufo/waves/round-99/seats/V92-scratch/` only (`poll.sh`, `poll.log`, `poll.stdout`, `rerun.txt`, `r98-blob/`). No commits, no pushes, no network, no nested agents. No producer-owned path was written. A throwaway `/tmp/v92-base` from the five-file `cmp` was removed.

**STATUS: FINAL on the eight re-runs — 7 REPRODUCED, 1 MISMATCHED.** V50's report never landed. Non-overlap is a recorded stall-escape against V50 scratch, not a report-to-report diff. C1 and the knowledge table were not verified (S1/S5 reports and both knowledge files still absent; freeze tool hash moved after the poll).

## 0. Poll-wait (40 tries, then stop)

Cadence 20 s, max 40. Gate: `S1`–`S5` and `V50` reports (maxdepth-1 `*.md`, not scratch dirs) plus the r99 fixture timeline and both knowledge files. Log: `.ufo/waves/round-99/seats/V92-scratch/poll.log`. First process was killed by the host 600 s cap after try 30 (`22:16:44`); resumed at try 31 (`22:28:11`). Tries are numbered 1–40 across both processes. Not an all-reports poll, so SELF subtraction was not required.

```
try 1  22:07:04 reports=6  present=[ S3 S4] missing: REPORT:S1 REPORT:S2 REPORT:S5 REPORT:V50 ART:r99-gate-blind-spot-table.md ART:r99-lapse-scope-note.md
try 30 22:16:44 reports=13 present=[ S3 S4] missing: REPORT:S1 REPORT:S2 REPORT:S5 REPORT:V50 ART:r99-gate-blind-spot-table.md ART:r99-lapse-scope-note.md
try 31 22:28:11 reports=21 present=[ S3 S4] missing: REPORT:S1 REPORT:S2 REPORT:S5 REPORT:V50 ART:r99-gate-blind-spot-table.md ART:r99-lapse-scope-note.md
try 40 22:31:11 reports=26 present=[ S3 S4] missing: REPORT:S1 REPORT:S2 REPORT:S5 REPORT:V50 ART:r99-gate-blind-spot-table.md ART:r99-lapse-scope-note.md
TIMEOUT after 40
```

Post-budget check at `22:42:43` and again at `22:44:43`: still no `V50*.md`, no `S1*.md`, no `S2*.md`, no `S5*.md`, no `corpus/knowledge/r99*`. V50's own poll (`V50-scratch/poll.log`) hit `TIMEOUT after 40` at `22:17:15` with the same producer gap; their `stall-escape.log` records `ESCAPE-EXHAUSTED 22:29:53` and still no report. Bounded stall-escape, not a 41st try: non-overlap below is judged against the only V50 quoted-output evidence on disk, `V50-scratch/`.

**V50 scratch set (excluded from these eight):**

- `rerun-s4.txt` (22:04:26): `support_check` full receipt on r99, `map_obligations` `raw=21 mapped=21`, `check_bible` CLEAN on r99, `grep` of the Tick 15 anchor at line 70, JSON counts 6/1/8/8/0 plus last event/source.
- `inherited-rows.txt`: map J-row line comparison, `changed_inherited 0`, `new_ids ['J21']`.
- `census_receipts.json`: `check_bible` exit + stdout sha256 for every fixture dir, including r98 and r99.

None of the eight commands below is in that set. S3 and S4 reports existed before the first re-run. No plan was verified. Freeze bytes were not treated as delivered: at poll end the tool was `6f81f8be…`; at `22:42:43` it had moved to `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` while the contract stayed `8c2561b0…`. S1 was still writing. `--self-test` was not run.

## 1. Revision binding (re-run at 22:32:46)

```
585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2  r94 fictional-excerpts.md
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  r95 fictional-excerpts.md
06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3  r96 fictional-excerpts.md
8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c  r97 fictional-excerpts.md
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  r98 fictional-excerpts.md
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  r99 fictional-excerpts.md
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  r99 entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  r99 relations.json
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  r99 sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  r99 timeline.json
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  map_obligations.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  check_bible.py
```

r94–r98 excerpt hashes match V80's quoted chain. r99 excerpt/entities/relations/sources/timeline match S3/S4/V10/V11 declared hashes. Full transcript: `V92-scratch/rerun.txt`.

## 2. Eight items

### A1 — V80 `wc -c` of the six excerpt files — **REPRODUCED**

Quoted by V80 (`V80-c2-prose-prefix.md` §1): sizes `1116 1845 2588 3410 4187 5114`, total `18260`, `rc=0`.

```
$ wc -c corpus/fixtures/r94-paired-crossing/fictional-excerpts.md \
        corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md \
        corpus/fixtures/r96-crossing-response/fictional-excerpts.md \
        corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md \
        corpus/fixtures/r98-clerk-filing/fictional-excerpts.md \
        corpus/fixtures/r99-window-lapse/fictional-excerpts.md
 1116 …/r94-paired-crossing/fictional-excerpts.md
 1845 …/r95-crossing-aftermath/fictional-excerpts.md
 2588 …/r96-crossing-response/fictional-excerpts.md
 3410 …/r97-crossing-acknowledgment/fictional-excerpts.md
 4187 …/r98-clerk-filing/fictional-excerpts.md
 5114 …/r99-window-lapse/fictional-excerpts.md
18260 total
rc=0
```

### A2 — V80 `cmp -n 4187` rc=0 and `cmp -s` rc=1 (r98 vs r99) — **REPRODUCED**

Quoted by V80 §1.

```
$ cmp -n 4187 corpus/fixtures/r98-clerk-filing/fictional-excerpts.md \
              corpus/fixtures/r99-window-lapse/fictional-excerpts.md
cmp_n_rc=0
$ cmp -s corpus/fixtures/r98-clerk-filing/fictional-excerpts.md \
         corpus/fixtures/r99-window-lapse/fictional-excerpts.md
cmp_s_rc=1
```

Empty `cmp -n` stdout, same as V80. Strict prefix, not a copy.

### A3 — V80 `bytes.startswith` chain, hashes, and deltas — **REPRODUCED**

Quoted by V80 §1: six sha256 values, `startswith=True strict=True`, deltas `729 743 822 777 927`, r98→r99 delta begins `b'\n## Round 99 lapse note (2026-10-17)\n\nNe'`.

Observed (own python, same files, 22:32:46): the six hashes and lengths match V80 character for character; all five `startswith=True strict=True`; deltas `729, 743, 822, 777, 927`; `delta_head b'\n## Round 99 lapse note (2026-10-17)\n\nNe'`.

### A4 — V80 lapse section exactly once, at the end — **REPRODUCED**

Quoted by V80 §2: `count '## Round 99 lapse note' = 1`, `clerk-lapse-note = 1`, `Tick 15: = 1`, headings after the section `[]`, file ends with newline, trailing bytes `b' matter stays open.\n'`, r94–r98 contain zero `lapse` / `clerk-lapse-note` / `Tick 15:` / `## Round 99`, case-insensitive `lapse` in r99 is exactly 3.

```
bytes 5114 lines 76
count '## Round 99 lapse note' = 1
count 'clerk-lapse-note' = 1
count 'Tick 15:' = 1
lapse heading line 66
headings after the lapse section: []
file ends with newline: True
r94..r98 lapse/clerk-lapse-note/Tick 15:/## Round 99 = 0/0/0/0 each
```

Follow-up slice at 22:42:43 (same file, hash unchanged from the bind): `p.read_bytes()[-20:] == b' matter stays open.\n'` and `text.lower().count("lapse") == 3`. The first transcript printed `[-24:]` (`b' the matter stays open.\n'`), which contains V80's quoted 20-byte tail; the 20-byte slice matches exactly.

### A5 — V47 five unchanged files identical to r98 and to `4265df5` — **REPRODUCED**

Quoted by V47 (`V47-byte-prefix-2.md` §1): `cmp` rc=0 for `contradictions.json`, `entities.json`, `inspiration-note.md`, `relations.json`, `source-excerpt.md` against the r98 worktree, and both r98 worktree and r99 identical to `git show 4265df5:corpus/fixtures/r98-clerk-filing/<f>`.

```
$ for f in contradictions.json entities.json inspiration-note.md relations.json source-excerpt.md; do
    cmp -s corpus/fixtures/r98-clerk-filing/$f corpus/fixtures/r99-window-lapse/$f
    git show 4265df5:corpus/fixtures/r98-clerk-filing/$f | cmp -s - corpus/fixtures/r99-window-lapse/$f
  done
cmp-rc0 contradictions.json
r99 IDENTICAL-to-4265df5 contradictions.json
r98-wt IDENTICAL-to-4265df5 contradictions.json
cmp-rc0 entities.json
r99 IDENTICAL-to-4265df5 entities.json
r98-wt IDENTICAL-to-4265df5 entities.json
cmp-rc0 inspiration-note.md
r99 IDENTICAL-to-4265df5 inspiration-note.md
r98-wt IDENTICAL-to-4265df5 inspiration-note.md
cmp-rc0 relations.json
r99 IDENTICAL-to-4265df5 relations.json
r98-wt IDENTICAL-to-4265df5 relations.json
cmp-rc0 source-excerpt.md
r99 IDENTICAL-to-4265df5 source-excerpt.md
r98-wt IDENTICAL-to-4265df5 source-excerpt.md
```

Not the same check as V50's map-row line comparison.

### A6 — V86 `map_obligations` on the `4265df5` r98 blob is 20/20 — **REPRODUCED**

Quoted by V86 (`V86-c2-no-new-entity.md` check 3). V50 re-ran `map_obligations` on the r99 fixture (`raw=21`), not on the baseline blob.

```
$ git archive 4265df5 corpus/fixtures/r98-clerk-filing | tar -x --strip-components=3 -C V92-scratch/r98-blob
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-99/seats/V92-scratch/r98-blob
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS
EXIT:0
```

Matches V86's `-- r98 blob --` block. Delta vs the delivered r99 map (21/21, already in V50's scratch, not re-claimed here) is +1.

### A7 — V11 inherited parsed-value equality, `FAILS: 0` — **REPRODUCED**

Quoted by V11 (`V11-c2-inherited-equality.md` §2): entities len 6 and parsed-equal (key-order sensitive), relations parsed-equal, timeline len 8 with `[:7]` parsed-equal, sources len 8 with `[:7]` parsed-equal, contradictions `[]`, no new entity id, only new source `clerk-lapse-note`, only new timeline id `clerk-lapse-recorded`, `FAILS: 0`.

Own `json.loads(..., object_pairs_hook=OrderedDict)` against the worktree r98 (itself identical to `4265df5` on these tables, A5) and r99, 22:32:46:

```
PASS entities len==6 :: got 6 r98=6
PASS entities parsed-equal :: ids98=['aru', 'evin', 'quiet-rise', 'salt-court', 'chalk-stair', 'clerk-maren'] ids99=[same]
PASS relations parsed-equal
PASS timeline len==8 :: got 8 r98=7
PASS timeline[:7] parsed-equal :: r98 len 7
PASS sources len==8 :: got 8 r98=7
PASS sources[:7] parsed-equal :: r98 len 7
PASS contradictions parsed-equal ([]) :: []
PASS no new entity id :: only_new=[]
PASS only new source id is clerk-lapse-note
PASS only new timeline id is clerk-lapse-recorded
FAILS: 0
```

Every verdict line V11 quoted reproduced. Relation detail rendering differs (`OrderedDict` repr vs V11's compact JSON); the equality result does not. This is JSON parsed-value equality, not V50's map-line comparison.

### A8 — V105 quoted `IN_QUOTES=True` for four lowercase phrases — **MISMATCHED**

Quoted by V105 (`V105-c2-event-description.md`, "Clause check", fenced block run at 22:05:05). Method stated: "Python containment against the quote lines (70-74)". No casefold is declared.

```
IN_QUOTES=False  'At the Chalk Stair at tick 15'
IN_QUOTES=False  'the clerk records that'
IN_QUOTES=True   'the crossing-window named in the original minute has closed'
IN_QUOTES=True   'the agreement was unfulfilled'
IN_QUOTES=True   'no claim was lodged'
IN_QUOTES=True   'the matter stands as a historical open entry'
```

Re-run at 22:32:46 and again at 22:42:43, exact `in` on `"\n".join(lines[69:74])` (1-based lines 70-74 of `fictional-excerpts.md`, hash `fefebaf9…` unchanged):

```
> Tick 15: The crossing-window named in the original minute has closed.
> The agreement was unfulfilled.
> No claim was lodged.
> The matter stands as a historical open entry.
> I record no resolution, assign no blame, and reconcile nothing.

exact=False  'the crossing-window named in the original minute has closed'
exact=False  'the agreement was unfulfilled'
exact=False  'no claim was lodged'
exact=False  'the matter stands as a historical open entry'
```

The four `IN_QUOTES=True` lines do not reproduce. The quote lines capitalize the first letter (`The` / `No`). Casefold containment is True for all four (`casefold=True` observed 22:42:43), so the sentences are present and V105's later prose table ("yes, line 70/71/72/73") is true only case-insensitively. The fenced booleans, as printed, are not.

Adjacent V105 quotes that were re-run and did reproduce, recorded so the mismatch is not widened:

- `grep -nF "historical open entry"` hits `timeline.json:84`, `fictional-excerpts.md:73`, `fictional-excerpts.md:76`, `grep_rc=0`.
- Scope line 76 exact containment: the four lowercase phrases are `IN_SCOPE=True`; `'At the Chalk Stair at tick 15'` and `'the clerk records that'` are `IN_SCOPE=False`.
- `lapse_section_has_Chalk_Stair False` and `lapse_section_has_chalk_stair_ci False` on lines 66-76.

Those three are not counted in the eight. The eight is the fenced `IN_QUOTES` block.

## 3. Not verified (ABSENT, not a plan)

- V50 report: absent at try 40 and at 22:44:43. Non-overlap is scratch-only.
- S1 report, S2 report, S5 report: absent. Freeze tool still moving (`6f81f8be…` → `fb9bb9ff…`). No `--self-test`, no `--freeze`, no Markdown-tamper replay.
- `corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md`: absent. No blind-spot row replayed.
- Census 172→173: not quoted by a landed seat in a form this seat re-ran, and not in the eight.

## Bottom line

**FAIL** — 7 REPRODUCED, 1 MISMATCHED (V105 fenced `IN_QUOTES=True` is exact-containment False; casefold True); V50 report ABSENT after 40 tries, so "different than V50" is a stall-escape against V50 scratch only.
