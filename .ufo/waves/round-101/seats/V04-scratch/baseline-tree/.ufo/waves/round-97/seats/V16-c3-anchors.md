# V16 — c3-anchors (round 97)

Seat: V16 c3-anchors. Scope per seat spec: independently verify that ALL 17
anchors in `corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md`
resolve in-span via my own implementation; every inherited anchor must exist
at the SAME line numbers as in r96's map; the new anchor only inside the
appended section; report any drift with path:line.

Baseline: r96 closure `f3e09f9`. Repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin`. No commits; no network; no repo
writes except this report and my declared scratch dir
`.ufo/waves/round-97/seats/V16-scratch/` (checker, pointer resolver, poll
script, logs; all paths absolute under the lane repo). No nested agents.

## 0. Poll-wait evidence (target = R4 payload + R5 map/README + R4/R5 reports)

40-try background poll (20 s cadence), requiring R4's seven payload files,
R5's `README.md`/`claim-excerpt-map.md`, and the R4/R5 seat reports, plus a
20 s byte-stability window (log `.ufo/waves/round-97/seats/V16-scratch/poll.log`):

```
try=1..2   18:43:45-18:44:05 payload=n r4=none r5=none
try=3..20  18:44:25-18:50:05 payload=y r4=none r5=none
try=21..24 18:50:25-18:51:25 payload=y r4=.ufo/waves/round-97/seats/R4-fixture-author.md r5=none
try=25     18:51:45 READY-STABLE md5set=1e6741013be4fbe9cf336e89cde98e56 r5=.ufo/waves/round-97/seats/R5-fixture-docs.md
```

Verification ran on that frozen revision. Pins re-checked after my run
(unchanged):

```
81e351a95ca366f712f8611103e752b7  corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md
3f04fd6a502ead31f899a38df2c96354  corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md
3ad888e13c48ff08de352380b5910fed  corpus/fixtures/r97-crossing-acknowledgment/README.md
5080b2604cddde502d0870d77f61e0d8  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
```

## 1. Method

Checker: `.ufo/waves/round-97/seats/V16-scratch/v16_check.py` (my own
implementation; full output archived at `V16-scratch/final-run.txt`). It
parses both maps' row tables, then for every r97 row runs
`grep -nF -e "<anchor>" -- <excerpt>` via `subprocess` and cross-checks the
line numbers against a pure-Python substring scan; checks in-span
containment, outside-span occurrences, inherited-row anchor/span equality +
resolved line sets r96 (and r95) vs r97, new-row occurrence placement,
byte-prefix discipline, and the declared inventory. Parser validated first on
r96↔r95 (`--validate` mode): `ALL-ANCHOR-CHECKS-PASS`, inventory declared
`[16, 2, 18, 14]` == parsed, exit 0 — reproducing r96's map exactly
(`V16-scratch/validate-r96-vs-r95.txt`).

Supplementary: `V16-scratch/v16_pointer_check.py` resolves every J row's JSON
pointer in the fixture (all 17 OK; S rows carry no pointer by design).

## 2. Result — checker output (run mode, verbatim, condensed to per-row lines)

```
== V16 checker: NEW=r97-crossing-acknowledgment (19 rows) vs REF=r96-crossing-response (18 rows) ==
new rows (vs ref): ['J17']
J01  span=12-12  grep=[12] py=[12] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[12] == this=[12] same=True ref2(r95-crossing-aftermath)=[12] same2=True
J02  span=13-13  grep=[13] py=[13] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[13] == this=[13] same=True ref2(r95-crossing-aftermath)=[13] same2=True
J03  span=12-12  grep=[12] py=[12] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[12] == this=[12] same=True ref2(r95-crossing-aftermath)=[12] same2=True
J04  span=13-13  grep=[13] py=[13] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[13] == this=[13] same=True ref2(r95-crossing-aftermath)=[13] same2=True
J05  span=17-17  grep=[17] py=[17] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[17] == this=[17] same=True ref2(r95-crossing-aftermath)=[17] same2=True
J06  span=12-12  grep=[12] py=[12] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[12] == this=[12] same=True ref2(r95-crossing-aftermath)=[12] same2=True
J07  span=13-13  grep=[13] py=[13] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[13] == this=[13] same=True ref2(r95-crossing-aftermath)=[13] same2=True
J08  span=12-12  grep=[12] py=[12] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[12] == this=[12] same=True ref2(r95-crossing-aftermath)=[12] same2=True
J09  span=13-13  grep=[13] py=[13] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[13] == this=[13] same=True ref2(r95-crossing-aftermath)=[13] same2=True
J10  span=18-18  grep=[18] py=[18] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[18] == this=[18] same=True ref2(r95-crossing-aftermath)=[18] same2=True
J11  span=19-19  grep=[19] py=[19] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[19] == this=[19] same=True ref2(r95-crossing-aftermath)=[19] same2=True
J12  span=12-12  grep=[12] py=[12] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[12] == this=[12] same=True ref2(r95-crossing-aftermath)=[12] same2=True
J13  span=13-13  grep=[13] py=[13] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[13] == this=[13] same=True ref2(r95-crossing-aftermath)=[13] same2=True
J14  span=18-20  grep=[20] py=[20] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[20] == this=[20] same=True ref2(r95-crossing-aftermath)=[20] same2=True
J15  span=22-31  grep=[26] py=[26] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[26] == this=[26] same=True ref2(r95-crossing-aftermath)=[26] same2=True
J16  span=33-42  grep=[37] py=[37] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[37] == this=[37] same=True
J17  span=44-53  grep=[48] py=[48] occ=1 IN-SPAN=True outside-span=[]  appended-only=True (ref file 42 lines; ref-has-anchor=False; file has 53 lines)
S01  span=5-5  grep=[5] py=[5] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[5] == this=[5] same=True ref2(r95-crossing-aftermath)=[5] same2=True
S02  span=5-5  grep=[5] py=[5] occ=1 IN-SPAN=True outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[5] == this=[5] same=True ref2(r95-crossing-aftermath)=[5] same2=True
inventory declared='17 JSON facts; 2 editorial rows; 19 total mapped rows; 15 distinct excerpt anchors.'
inventory parsed={'json': 17, 'editorial': 2, 'total': 19, 'distinct': 15}
inventory match=True declared=(17, 2, 19, 15) parsed=(17, 2, 19, 15)
fictional-excerpts.md: ref=2588B this=3410B byte-prefix-ok=True
FAILURES: none
RESULT: ALL-ANCHOR-CHECKS-PASS
```

All 17 JSON anchors (J01–J17) plus both editorial anchors (S01, S02) resolve
in-span. `grep -nF` and the pure-Python scan agreed on the exact line-number
set for every one of the 19 rows; every row has occurrence count 1 (`occ=1`)
and no occurrence outside its declared span (`outside-span=[]` everywhere —
so no inherited anchor leaked into the appended section and no appended
anchor appears earlier).

## 3. Inherited anchors — same line numbers as r96 (and r95)

For each of the 18 inherited rows (J01–J16, S01, S02): the anchor string is
identical to the r96 map's anchor, the declared span is unchanged, and the
resolved line numbers in the r97 copy equal those in the r96 fixture exactly
(every `vs-ref` line above: `same=True`); for J01–J15 and S01/S02 they also
equal the r95 fixture's resolved lines (`ref2` fields). Resolved lines:

| rows | resolved lines (r95 == r96 == r97) |
|---|---|
| J01/J03/J06/J08/J12 | 12 |
| J02/J04/J07/J09/J13 | 13 |
| J05 | 17 |
| J10 | 18 |
| J11 | 19 |
| J14 | 20 (span 18-20) |
| J15 | 26 (span 22-31) |
| J16 | 37 (span 33-42; added in r96, no r95 counterpart) |
| S01/S02 | 5 (`source-excerpt.md`, span 5-5) |

Raw `grep -nF` samples (r97):

```
$ grep -nF -e 'Aru carried the north lantern at Quiet Rise' -- corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md
12:> Tick 9: Aru carried the north lantern at Quiet Rise.
$ grep -nF -e 'Tick 12: I was at Salt Court through the same agreed bell.' -- corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md
37:> Tick 12: I was at Salt Court through the same agreed bell.
```

## 4. New acknowledgment anchor — only in the appended section

J17 (map row verbatim):

```
| J17 | `timeline.json#/5` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `aru-acknowledgment-note` | `r97-crossing-acknowledgment:aru-acknowledgment-note` | `fictional-excerpts.md` | 44-53 | `verbatim` | `Tick 13: I received Evin's response at the Chalk Stair.` |
```

```
$ grep -nF -e "Tick 13: I received Evin's response at the Chalk Stair." -- corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md
48:> Tick 13: I received Evin's response at the Chalk Stair.
$ grep -nF -e "Tick 13: I received Evin's response at the Chalk Stair." -- corpus/fixtures/r96-crossing-response/fictional-excerpts.md
(no output, exit 1)
$ grep -rnF -e "Tick 13: I received Evin's response at the Chalk Stair." corpus/fixtures/r97-crossing-acknowledgment/ | grep -v claim-excerpt-map.md
corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md:48:> Tick 13: I received Evin's response at the Chalk Stair.
```

The anchor occurs exactly once in the fixture (at line 48), inside the
appended Round 97 section (line 44 heading → line 53 scope close, file has 53
lines; r96 file has 42 lines); the declared span 44-53 covers exactly the
appended section; checker fields `appended-only=True`, `ref-has-anchor=False`.
Pointer cross-check: `timeline.json#/5` resolves to
`{"id": "acknowledgment-aru-records", "tick": 13, "entity_id": "aru", "place_id": "chalk-stair", "depends_on": ["response-evin-salt-court"], ...}`
(all 17 J pointers resolve; `V16-scratch/final-pointer.txt`,
`RESULT: ALL-POINTERS-RESOLVE`, exit 0).

## 5. Copy discipline and r96 repair scope (supporting evidence)

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s $R96/$f $R97/$f && echo "$f BYTE-IDENTICAL"; done
entities.json BYTE-IDENTICAL ... source-excerpt.md BYTE-IDENTICAL  (all five)
sources.json  ref_len=5 new_len=6 prefix_ok=True appended=['aru-acknowledgment-note']
timeline.json ref_len=5 new_len=6 prefix_ok=True appended=['acknowledgment-aru-records']
fictional-excerpts.md ref=2588B new=3410B byte_prefix_ok=True   (42 -> 53 lines)
```

r96 cosmetic repair (R4), independently characterized against HEAD
(`711e59f0…`, the r96 closure state that matches r96-V11's recorded pin):
working tree `5080b260…`; `diff` vs HEAD shows exactly 2 changed lines —
line 44 editorial delimiter 8 cells → 7 cells (matching its 7-cell
header/rows) and line 50's stale "The new relation encodes only the
agreement for this crossing…" → "The new tick-12 event encodes only Evin's
second account of the same crossing occasion…"; `grep '^| J\|^| S'` diff of
HEAD vs working tree is empty (`DATA-ROWS-BYTE-IDENTICAL`); the two excerpt
files are byte-unchanged (`8760854b…`, `b54e1d67…`). The r97 map table
structure is 4/8/7 cells with 0 occurrences of `new relation`.

## 6. Corroboration (not this seat's claim)

The in-repo `support_check.py` on the same frozen revision:

```
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS
```

Its found-line numbers (12, 13, 12, 13, 17, 12, 13, 12, 13, 18, 19, 12, 13,
20, 26, 37, 48; S at 5, 5) match my independent `grep -nF` results exactly.
`map_obligations.py` (working-tree r97 revision): `OBLIGATIONS raw=17
mapped=17; INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19;
RESULT PASS`.

## 7. Drift findings

None. No anchor drift, no line-number drift, no span drift, no path drift, no
out-of-span occurrence, no inventory inconsistency. Nothing to report as
`path:line`.

Observation (not drift): the inherited rows' path-qualification column was
re-qualified `r96-crossing-response:*` → `r97-crossing-acknowledgment:*`
(J01 sample: r95 map `r95-crossing-aftermath:paired-clock` → r96 map
`r96-crossing-response:paired-clock` → r97 map
`r97-crossing-acknowledgment:paired-clock`), consistent with the established
per-round convention; anchor/span/line columns are untouched.

## 8. Boundaries (not verified by this seat)

- Anchor resolution is lexical (`grep -nF` + substring scan); it is not
  semantic entailment of the JSON facts, chronology, or canon judgment.
- The r96 repair's "receipts unchanged" property is R4's claim; I verified
  only its 2-line change scope and data-row byte-identity as supporting
  evidence, not the tool receipts.
- The namespace-column re-qualification naming correctness is R5's claim;
  I only recorded it as an observation.
- JSON counts (5 entities / 1 relation / 6 events / 6 sources) and sibling
  copy discipline are supporting evidence, not the seat's anchor claim.

## Bottom line

PASS — all 17 JSON anchors (J01–J17) + 2 editorial anchors resolve in-span
via my own grep -nF + pure-Python implementation; all 18 inherited anchors
are identical and resolve at the same line numbers as r96 (J01–J15/S also vs
r95); the new acknowledgment anchor occurs only at
`corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md:48` inside
the appended Round 97 section (span 44-53); zero drift.
