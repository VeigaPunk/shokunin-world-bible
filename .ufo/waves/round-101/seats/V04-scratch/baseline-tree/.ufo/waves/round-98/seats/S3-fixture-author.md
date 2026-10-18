# S3 fixture-author — round 98

Seat: S3 (producer, byte-ownership). Baseline: r97 closure `9a3d648` (pre-round bytes
via `git show 9a3d648:<path>`). All commands ran from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested
agents, no commits, no network. Only writes: the two owned fixture paths below, this
report (absolute path), and `.ufo/waves/round-98/seats/S3-scratch/` (receipts and
pre-repair scratch copy). No other file was written by this seat.

Owned and delivered:

1. `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` — repair only.
2. `corpus/fixtures/r98-clerk-filing/` — 10 files byte-copied from `9a3d648`
   (all verified byte-identical at copy time), then the 4 owned files extended:
   `entities.json`, `sources.json`, `timeline.json`, `fictional-excerpts.md`.
   (`README.md`, `claim-excerpt-map.md` were copied as placeholders and are S4's to
   rewrite; `contradictions.json`, `inspiration-note.md`, `relations.json`,
   `source-excerpt.md` remain byte-identical to r97.)

## A. r95 map one-sentence carried-wording repair

Defect (as declared in C3): line 49 of the r95 map carried r94's sentence
`The new relation encodes only the agreement for this crossing, not perpetual
performance or alliance.` — but r95's own new row is the tick-11 event, not a
relation (the relation was r94's addition and is inherited here). The r94 map's use
of the same sentence is correct for r94; r96 and r97 already name their own new
event (`corpus/knowledge/r97-acknowledgment-scope-note.md:32` records the same class
of repair for r96).

Repair (single in-place line edit, no line added or removed):

- before (tail of line 49): `… The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.`
- after (tail of line 49): `… The relation encodes only the agreement for this crossing, not perpetual performance or alliance; the new tick-11 aftermath event records one reported non-arrival on one occasion.`

Evidence — the whole-file diff against the closure revision is exactly that one line:

```
$ diff <(git show 9a3d648:corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md) \
       corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
49c49
< …The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
---
> …The relation encodes only the agreement for this crossing, not perpetual performance or alliance; the new tick-11 aftermath event records one reported non-arrival on one occasion.
$ wc -l   # closure blob and delivered file
     53 /dev/fd/63
     53 corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
$ sha256sum corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61
# closure blob sha256: 30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a
```

Data rows, JSON pointers, anchors, spans, and delivery modes are byte-unchanged
(single-line diff above; the changed line is prose in `## Timeline normalization and
scope`, not a table row, not the `**Expected inventory:**` line).

Receipts before vs after — identical, both exit 0. Method: the pre-repair map was
restored from `9a3d648` into a scratch copy of the cluster
(`.ufo/waves/round-98/seats/S3-scratch/r95-prerepair/`), both tools were run there
and on the delivered cluster, and the captured outputs were diffed:

```
$ diff S3-scratch/receipt-support-BEFORE.txt S3-scratch/receipt-support-AFTER.txt  -> IDENTICAL
$ diff S3-scratch/receipt-map-BEFORE.txt     S3-scratch/receipt-map-AFTER.txt      -> IDENTICAL
support BEFORE exit=0; support AFTER exit=0; map BEFORE exit=0; map AFTER exit=0
AFTER receipt (support_check): INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2;
  TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13 … SOURCE-SUPPORT 15/15; RESULT PASS
AFTER receipt (map_obligations): OBLIGATIONS raw=15 mapped=15; RESULT PASS
```

Cross-check that the repair harms no frozen axis — the r95 pin still verifies (the
map is not a pinned data file; the pinned content digest is over the 5 JSON tables):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS   (exit 0; digest equals the contract pin for r95)
```

Residual: r95's map sha256 moved `30281ff1…` → `80440d61…`; the freeze contract
`pins.r95-crossing-aftermath.content_sha256` is unaffected (data files only), so no
re-pin is required by this repair. S5 owns the dated addenda in
`corpus/knowledge/r95-aftermath-scope-note.md` / `r96-response-scope-note.md`.

## B. r98-clerk-filing authored (fourth beat: institutional filing, no finding)

Copy fidelity — all 10 files came from the r97 closure commit, and all 10 were
byte-identical to the then-current r97 tree (`cmp`/sha256 sets matched), so the copy
is closure-attributable:

```
$ for f in <10 files>; do git show 9a3d648:corpus/fixtures/r97-crossing-acknowledgment/$f > corpus/fixtures/r98-clerk-filing/$f; done
copy fidelity: README.md SAME; claim-excerpt-map.md SAME; contradictions.json SAME;
entities.json SAME; fictional-excerpts.md SAME; inspiration-note.md SAME;
relations.json SAME; source-excerpt.md SAME; sources.json SAME; timeline.json SAME
```

Additions (exact fields delivered):

- `entities.json` — appended `clerk-maren`: kind `character`, name `Maren`,
  `first_appearance` `clerk-filing-note`, one claim
  (`"The filing note names Maren, the clerk of the Chalk Stair registry, as the
  officer who filed both pending accounts."`, `source_id` `clerk-filing-note`).
- `sources.json` — appended `clerk-filing-note`, title `Maren's Chalk Stair Registry
  Filing Note`, kind `fictional first-person note`, reliability note asserting no
  finding, no verdict, no reconciliation, no resolution, and not evidence of a
  breach, a continuing duty, a winner, or an external historical fact.
- `timeline.json` — appended `clerk-filing-open`: tick 14, `entity_id` `clerk-maren`,
  `place_id` `chalk-stair`, `depends_on` `["acknowledgment-aru-records"]`,
  `source_id` `clerk-filing-note`, description `"At the Chalk Stair at tick 14, the
  clerk filed both pending accounts and recorded the matter OPEN, asserting no
  finding and no resolution."`
- `fictional-excerpts.md` — byte-prefix + new dated section. Prefix check:
  `head -c $(stat -c%s r97/fictional-excerpts.md) r98/fictional-excerpts.md | sha256sum`
  = `8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c`
  = r97 file sha256 (byte-identical prefix). New section occupies lines 54–64
  (heading 55; quote lines 59–62; scope 64); quote lines:
  `> Tick 14: I filed both pending accounts at the Chalk Stair registry.` /
  `> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.` /
  `> I assert no finding.` / `> I reach no verdict and reconcile nothing.`
  All five candidate anchors grep as fixed strings at lines 59/60/61/62.

Counts and inheritance (parsed values, not text):

```
entities rows=6; sources rows=7; timeline rows=7; relations rows=1; contradictions rows=0
entities: aru, evin, quiet-rise, salt-court, chalk-stair, clerk-maren
sources:  veil-verse, paired-clock, crossing-minute, aru-aftermath-note,
          evin-response-note, aru-acknowledgment-note, clerk-filing-note
events:   9,9,10,11,12,13,14 (clerk-filing-open last)
inherited parsed-value identity r98 vs r97: entities[0:5] True; sources[0:6] True;
  timeline[0:6] True; relations[0:1] True   (5/1/6/6 -> 6/1/7/7)
```

Gates on the delivered bytes:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations        (exit 0)
```

Delivered file hashes (this seat's four files):

```
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  sources.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  timeline.json
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  fictional-excerpts.md
```

Interim evidence while r98 still carried the copied r97 map (before S4's rewrite):
`map_obligations` failed with exactly the three expected `missing_obligation`
findings and nothing else — `entities.json#/5/first_appearance`,
`entities.json#/5/claims/0`, `timeline.json#/6`; `OBLIGATIONS raw=20 mapped=17`.
No phantom row, no extra obligation class: the new JSON creates exactly the three
declared obligations.

## C. Integration with S4's map (verified after S4's rewrite landed)

S4's `claim-excerpt-map.md` appeared at 20:30:28; all three r98 gates were then
re-run on the frozen bytes:

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
… PASS J18 (line 60, clerk/OPEN), PASS J19 and PASS J20 (line 59, tick-14 filing line)
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS    (exit 0)

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20; INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS    (exit 0)
```

So the declared C3 shape holds end-to-end on the delivered bytes: 6 entities / 1
relation / 7 events / 7 sources, 20 map obligations (17 inherited + first_appearance
+ claim + event), `check_bible` CLEAN.

## D. Cross-seat observations (evidence, not a verdict on other seats)

1. **Placeholder-poll hazard (r98 README/map).** The brief required copying r97's
   `README.md` and `claim-excerpt-map.md` into r98 as part of the 10-file byte copy;
   S4 rewrites both. Between my copy (20:28) and S4's map rewrite (20:30:28) the
   files existed with r97's bytes. V14's poll log
   (`.ufo/waves/round-98/V14-poll.log`, try 4/5) shows both paths no longer
   "missing" at that point, i.e. an existence-only poll can be satisfied by the
   placeholder. Verifiers must check content (e.g. `cmp` against r97, or that the
   map names `r98-clerk-filing`/20 rows) rather than existence alone. Both
   placeholders are now replaced: S4's map landed 20:30:28 and S4's `README.md`
   landed 20:31:05 (verified content: `# Round 98 clerk-filing continuation`,
   `6 entities / 1 relation / 7 events / 7 sources`, 29 lines, 4 mentions of
   `r98-clerk-filing`); `check_bible` re-run after the README rewrite is still
   `CLEAN … 0 violations`, exit 0.
2. **r95 map sha change** `30281ff1…` → `80440d61…`; the r95 freeze pin's
   `content_sha256` (`d541ae64…`) is unchanged and still verifies PASS, so no re-pin
   is required for r95 by this repair. r96/r97 fixture bytes are untouched by this
   seat (r96 map sha still `e851f068…` per the r97 scope note; verified by the
   unchanged r98 copies of r97 files).
3. No doc outside the two scope notes references the repaired r95 sentence; the
   only remaining `new relation` sentences in `corpus/` are r94's (correct for r94)
   and the historical census note in `corpus/fixtures/README.md:1213` (read-only,
   describes the already-repaired r96 case).
4. Scratch for verifiers: `.ufo/waves/round-98/seats/S3-scratch/` holds
   `r95-prerepair/` (restored pre-repair cluster), the four BEFORE/AFTER receipts,
   the r98 receipts, and `r98-map-S4-revision.md` (copy of S4's map as verified).
5. **Stray write in the parent repo (not this seat).** `git status` in
   `/home/vgpnk/Projects/shokunin` (the session cwd, outside the lane) shows an
   untracked `baseline-analyze.txt` (105 bytes, mtime 20:30) whose content is
   `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2]
   No such file or directory` — a redirected shell output written into the parent
   repo root by some other seat, i.e. the r94-F01 stray-write class. This seat wrote
   nothing outside the lane; the file is left untouched for the L1 to attribute.

## Bottom line

**PASS** — r95 carried-wording repaired as exactly one prose line with support_check
and map_obligations receipts byte-identical before/after (both exit 0) and the r95
freeze pin still PASS at digest `d541ae64…`; r98-clerk-filing delivered as a 10-file
byte copy of r97 plus the declared entity/source/event/excerpt (6/1/7, 7 sources,
inherited rows parsed-value identical, excerpt prefix byte-identical), with
`check_bible` CLEAN exit 0 and, on S4's landed map and README, support_check 20/20
PASS and map_obligations raw=20 mapped=20 PASS; both S4 placeholders are now
rewritten, and the only cross-seat residue is a parent-repo stray file this seat did
not write (item D5).
