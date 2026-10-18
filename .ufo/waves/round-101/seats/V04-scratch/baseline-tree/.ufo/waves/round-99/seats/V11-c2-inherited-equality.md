# V11 c2-inherited-equality — round 99

Seat: V11 (verifier, C2 inherited-equality). Baseline: r98 closure `4265df5`
(`4265df5e86e4121bde4125b649b89bb1676676a5`). Pre-round bytes read via
`git show 4265df5:<path>` into
`.ufo/waves/round-99/seats/V11-scratch/baseline-r98/` (sha256-matched to the
worktree r98 files and to the commit blobs). All commands ran from the lane
root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` (3.14.7).
Leaf seat: no nested agents, no commits, no pushes, no network. Only writes:
this report (absolute path) and `.ufo/waves/round-99/seats/V11-scratch/`
(`parity.py`, `parity.out`, `poll.log`, `cmp.out`, `cmp-final.out`,
`mapdiff.out`, `recheck.out`, `freeze.out`, `junction.out`, `baseline-r98/`).
No producer-owned file was written by this seat.

Verification subject: inherited rows of `corpus/fixtures/r99-window-lapse/`
against `corpus/fixtures/r98-clerk-filing/` at `4265df5`, plus byte-prefix of
the copied files, plus the r98 directory remaining byte-untouched. Poll
target: S3 — `S3-fixture-author.md` was present and was read before any
verdict.

Axes named: parsed-value equality (key-order sensitive) of every inherited
row; r98 byte-untouched versus `4265df5`; `cmp` byte-prefix of copied files.
No axis of this seat was harmed by the checks below.

## 1. Poll record (stall-escape recorded, not fatal)

Poll script slept 20 s between tries, max 40. It required both the six S3
artifact files and `S3-fixture-author.md`. Log
`.ufo/waves/round-99/seats/V11-scratch/poll.log`:

```
try 1 2026-10-17 22:01:03 -0300 missing: S3-fixture-author.md
  dir-present files=claim-excerpt-map.md contradictions.json entities.json fictional-excerpts.md inspiration-note.md README.md relations.json source-excerpt.md sources.json timeline.json
try 2 2026-10-17 22:01:23 -0300 missing: S3-fixture-author.md
try 3 2026-10-17 22:01:43 -0300 ALL-PRESENT
```

Try 1 saw a 10-file directory whose sizes still matched r98 (placeholder copy:
entities 1793, sources 2725, timeline 2552, fictional-excerpts 4187). The
report was absent, so that state was not verified. By try 3 the report
existed (`S3-fixture-author.md`, 5069 bytes, mtime 22:01:40) and the three
extended files had already moved (sources 3293, timeline 2998,
fictional-excerpts 5114, mtime 22:01:13). No wait for ALL reports was
performed, so no self-subtraction hazard arose. Bounded stall: 2 misses, then
present; not exhausted.

## 2. Parsed-value equality, every inherited row (r99 vs r98)

Method: `json.loads(..., object_pairs_hook=OrderedDict)` on the `4265df5`
extract for r98 and on the worktree for r99. `OrderedDict` equality is
key-order sensitive on this interpreter (harness check: `OrderedDict([('id','x'),('kind','y')]) != OrderedDict([('kind','y'),('id','x')])`).
Per-row `list(keys())` was compared as well, including nested `claims`.
Harness: `V11-scratch/parity.py`. Full output: `V11-scratch/parity.out`
(94 PASS, `FAILS: 0`, exit 0). Quoted core:

```
PASS entities len==6 :: got 6 r98=6
PASS entities parsed-equal (all 6, key-order sensitive) :: r98 ids=['aru', 'evin', 'quiet-rise', 'salt-court', 'chalk-stair', 'clerk-maren'] r99 ids=['aru', 'evin', 'quiet-rise', 'salt-court', 'chalk-stair', 'clerk-maren']
PASS entities[0] keys equal and ordered :: r98=['id', 'kind', 'name', 'first_appearance', 'claims'] r99=['id', 'kind', 'name', 'first_appearance', 'claims']
PASS entities[0].claims[0] key-order :: r98=['statement', 'source_id'] r99=['statement', 'source_id']
… entities[1]..entities[5] same key order, including clerk-maren and its one claim …
PASS relations len==1 :: got 1
PASS relations parsed-equal (key-order sensitive) :: r99=[{"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing", "source_id": "crossing-minute"}]
PASS relations[0] keys ordered :: r98=['from', 'to', 'type', 'source_id'] r99=['from', 'to', 'type', 'source_id']
PASS timeline len==8 :: got 8 r98=7
PASS timeline[:7] parsed-equal (key-order sensitive) :: r98 len 7
PASS timeline[0]..timeline[6] keys equal and ordered :: ['id', 'tick', 'entity_id', 'place_id', 'depends_on', 'description', 'source_id']
PASS sources len==8 :: got 8 r98=7
PASS sources[:7] parsed-equal (key-order sensitive) :: r98 len 7
PASS sources[0]..sources[6] keys equal and ordered :: ['id', 'title', 'kind', 'reliability_note']
PASS contradictions parsed-equal ([]) :: []
PASS no new entity id
PASS only new source id is clerk-lapse-note
PASS only new timeline id is clerk-lapse-recorded
FAILS: 0
```

Inherited slices are exactly the declared ones: entities all 6 (not a prefix
of a longer list), relations the single row, `timeline[:7]`, `sources[:7]`,
contradictions `[]`. No inherited row was reordered, no key was reordered,
no nested claim changed. The only new rows are appended:

- `sources[7]`: `id` `clerk-lapse-note`, title `Maren's Chalk Stair Lapse Note`, kind `fictional first-person note`, keys `['id', 'title', 'kind', 'reliability_note']`.
- `timeline[7]`: `id` `clerk-lapse-recorded`, tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id` `clerk-lapse-note`, keys matching the inherited event key order. Description records that the crossing-window named in the original minute has closed, the agreement was unfulfilled, no claim was lodged, and the matter stands as a historical open entry. The words resolution / blame / reconciliation appear only as negations (`asserts no resolution, no blame, and no reconciliation`), not as positive findings.

Counts: entities 6→6, relations 1→1, events 7→8, sources 7→8, contradictions 0→0. Ticks `[9, 9, 10, 11, 12, 13, 14, 15]`.

## 3. r98 directory byte-untouched versus 4265df5

```
$ git diff --stat 4265df5 -- corpus/fixtures/r98-clerk-filing
(empty)
$ git diff --exit-code 4265df5 -- corpus/fixtures/r98-clerk-filing
diff_exit=0
$ git status --porcelain -- corpus/fixtures/r98-clerk-filing
(empty)
```

Re-run at 22:01 (pre-verdict), 22:02:40, 22:03:14, 22:03:58, and 22:04:55.
All ten r98 worktree sha256s equal the `4265df5` blobs (e.g. entities
`db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984`, timeline
`eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af`, sources
`32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3`). HEAD at
verification was `337f0fa` (the blocked-dispatch note, ahead of `4265df5`);
that commit does not change the r98 fixture. Census: `git ls-tree -d 4265df5
corpus/fixtures/` = 172; worktree `ls -d corpus/fixtures/*/` = 173; the only
set difference is `corpus/fixtures/r99-window-lapse`.

## 4. Byte-prefix (`cmp`) of copied files

S3's delivery (report read at 22:01:46, before S4 rewrote anything): all ten
files existed; the seven files S3 declared as unchanged copies were
`cmp`-identical to r98 (`README.md`, `claim-excerpt-map.md`,
`contradictions.json`, `entities.json`, `inspiration-note.md`,
`relations.json`, `source-excerpt.md`). The three extended files differed.

At the settled subject revision (22:04:55), shell `cmp`:

```
$ for f in contradictions.json entities.json inspiration-note.md relations.json source-excerpt.md; do
    cmp -s corpus/fixtures/r98-clerk-filing/$f corpus/fixtures/r99-window-lapse/$f \
      && echo IDENTICAL $f || echo DIFFERS $f
  done
IDENTICAL contradictions.json
IDENTICAL entities.json
IDENTICAL inspiration-note.md
IDENTICAL relations.json
IDENTICAL source-excerpt.md
```

The same five are `IDENTICAL-to-4265df5` when compared against
`git show 4265df5:corpus/fixtures/r98-clerk-filing/$f`.

Extended files, `cmp -n` at the inherited prefix, whole-file `cmp` expected
to differ:

```
$ cmp -n 2722 corpus/fixtures/r98-clerk-filing/sources.json corpus/fixtures/r99-window-lapse/sources.json
cmp -n 2722 rc=0
whole cmp rc=1
$ cmp -n 2549 corpus/fixtures/r98-clerk-filing/timeline.json corpus/fixtures/r99-window-lapse/timeline.json
cmp -n 2549 rc=0
whole cmp rc=1
$ cmp -n 4187 corpus/fixtures/r98-clerk-filing/fictional-excerpts.md corpus/fixtures/r99-window-lapse/fictional-excerpts.md
cmp -n rc=0
whole cmp rc=1
```

Limits are `len(r98) - 3` for the JSON tables (the start of the trailing
`"\n]\n"`) and `len(r98)` for the excerpt. Python LCP agrees:

```
sources.json:  LCP=2722 == len(r98)-3 (2722); r99 divergence b',\n'; r99 still ends b'\n]\n'; len 2725 → 3293
timeline.json: LCP=2549 == len(r98)-3 (2549); r99 divergence b',\n'; r99 still ends b'\n]\n'; len 2552 → 2998
fictional-excerpts.md: r99 startswith r98 (4187 bytes); appended 927 bytes beginning b'\n## Round 99 lapse note (2026-10-17)\n'
```

So every inherited JSON row is byte-identical, not merely value-identical,
and the new rows are appended at the end of each array. The excerpt is a
strict byte-prefix; the appended section is lines 66–76 (heading 66, quote
lines 70–74, scope 76; file ends with a newline; 76 lines total).

**S4 rewrite, recorded so it is not mistaken for an inherited-row mutation.**
Between 22:02:39 and 22:03:19, `claim-excerpt-map.md` and `README.md` stopped
being r98 copies. At 22:04:55 they are S4 rewrites, not byte-prefixes of r98
(map 15028 → 17119 bytes, sha256
`d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`; README
5829 → 6176 bytes, sha256
`b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049`). That is
S4's declared ownership. It does not touch the five JSON tables or
`fictional-excerpts.md`, whose hashes were stable from 22:01:13 through
22:07:59. S3's claim that those two files were byte-identical copies was true
at the moment the S3 report was read (22:01:46); it is not true of the
post-S4 tree, and S3's own report says S4 owns them.

Informational map-row check (not the seat's JSON axis, run because the
declaration says "20 inherited rows unchanged"): r98 map JSON-fact rows = 20,
r99 = 21. Across the first 20 rows the only differing column is the
path-qualification column (column 3), 20/20 rows, and substituting
`r98-clerk-filing` → `r99-window-lapse` in that column makes all 20 rows
equal (`other=0`). The two editorial `| S` rows are equal. The only new row
is J21 (`timeline.json#/7`, `r99-window-lapse:clerk-lapse-note`, span 66-76),
which sits inside the appended excerpt region. Output:
`V11-scratch/mapdiff.out`.

## 5. S3 claim cross-checks

Every checkable claim in `S3-fixture-author.md` that is on this seat's axis
was re-run:

- entities 6, relations 1, sources 8, timeline 8, contradictions 0: confirmed.
- `sources.json[:-1]` / `timeline.json[:-1]` parsed-equal to r98, and the
  raw prefix is the `cmp -n` result above: confirmed.
- `fictional-excerpts.md` startswith the r98 bytes, then a newline and the
  Round 99 heading: confirmed.
- seven files byte-identical to `4265df5` r98 at S3 delivery: confirmed at
  22:01:46; five of those seven remain identical after S4 (see §4).
- `python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse`
  → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0
  (re-run 22:02:40 and 22:04:55).
- `git status --porcelain -- corpus/fixtures/r98-clerk-filing` empty: confirmed.

Not re-verified here (other seats): the 21-obligation `map_obligations` /
`support_check` receipts, the freeze pin, and census ownership. Census
172→173 was observed (`git ls-tree` 172, worktree 173, sole extra dir
`r99-window-lapse`) but is not this seat's verdict.

## 6. Frozen subject hashes (worktree, stable 22:03:58, 22:04:55, and 22:07:59)

```
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  timeline.json
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  sources.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
```

r98 counterparts (worktree = `4265df5`): entities `db2d8e5d…` (same),
relations `c279254b…` (same), contradictions `37517e5f…` (same),
inspiration-note `58f5390e…` (same), source-excerpt `b5edc2fd…` (same),
sources `32ee15b1…`, timeline `eb24e084…`, fictional-excerpts `29e384bf…`.

A later `sha256sum` of those eight files at 22:07:59 matched the list above
byte-for-byte, and `git diff --exit-code 4265df5 -- corpus/fixtures/r98-clerk-filing`
was still exit 0. If a later producer rewrites `entities.json`,
`relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, or
`fictional-excerpts.md` after 22:07:59, this verdict is superseded for those
bytes. README and claim-excerpt-map are S4's and were already rewritten
before this freeze; their hashes are informational only.

## Bottom line

**PASS** — on the delivered r99 subject revision (hashes stable 22:01:13–22:07:59): every inherited row is parsed-value identical to r98 at `4265df5` and key-order sensitive (`entities` all 6, `relations` the 1 row, `timeline[:7]`, `sources[:7]`, `contradictions` `[]`; 94/94 harness checks, 0 fails), the r98 directory is byte-untouched (`git diff --exit-code 4265df5` exit 0, porcelain empty), and `cmp` shows the five remaining copies identical and the three extensions a pure prefix (`cmp -n` rc 0; JSON divergence is the appended `,\n` row; excerpt is a strict 4187-byte prefix).
