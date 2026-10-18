# V35 — anchor-replica-2 (round 95)

Seat: V35 anchor-replica-2. Scope per seat spec: **third independent anchor
verification of r95's map using a python line-slice method (not grep)**: all 15
anchors in-span, inherited line numbers preserved; report the count verified
and any miss.

Baseline: HEAD `fb118c4` (r94 closure); working tree at verification time had
`M LOG.md` plus untracked `.ufo/waves/round-95/` and
`corpus/fixtures/r95-crossing-aftermath/` (P3/P4 outputs). No repo writes by
this seat except this report; the checker script lives at `/tmp/v35_check.py`
(outside the repo).

## Step 0 — poll-wait

Poll for `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` +
P4's seat report, 20 s cadence (background task `bash-ivmf8ug3`):

```
READY at try 15 (16:22:36): map + .ufo/waves/round-95/seats/P4-fixture-docs.md
```

First sighting of the fixture dir was 16:18:01 (P3's 8 files, then still exact
r94 copies of the 3 to-be-modified files); the modified `sources.json` /
`timeline.json` / `fictional-excerpts.md` landed 16:18:34 and the map 16:21:10.
All checks below were re-run after P4's report existed; results identical.

Verified revision (sha256, frozen at report time):

```
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  claim-excerpt-map.md
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  fictional-excerpts.md
3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177  timeline.json
fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a  sources.json
```

## Step 1 — method (independent of grep, support_check, and map_obligations)

`/tmp/v35_check.py` parses the `## JSON facts` markdown table itself (rows
matching `^\| J\d+ \|`, 8 cells), reads each excerpt file once with
`Path.read_text().split("\n")`, and for every row searches the declared span by
**line index** (`[i+1 for i,l in enumerate(lines) if anchor in l]`), asserting
at least one hit with `start <= line <= end`. It also compares J01–J14 against
the r94 map (span + anchor + excerpt equality), hashes the declared byte copies,
and resolves the JSON pointers directly.

Calibration (run before the artifact existed, proving the green is not trivial):

```
r94 baseline rows: 14
r94 baseline in-span: 14 / 14 misses: []
control: J01 anchor hits [12] declared span 12 -> shifted span (13, 13) in-span? False
```

i.e. the same method on r94 is 14/14, and a one-line span shift makes it report
a miss.

## Step 2 — anchor check on r95 (the seat's claim)

Command: `python3 /tmp/v35_check.py` → `V35 VERDICT: PASS`, script exit 0.
Quoted observed output (abridged to the per-row lines):

```
PARSED r95 JSON-fact rows: 15 (ids: J01, J02, J03, J04, J05, J06, J07, J08, J09, J10, J11, J12, J13, J14, J15)
DECLARED: **Expected inventory:** 15 JSON facts; 2 editorial rows; 17 total mapped rows; 13 distinct excerpt anchors.
OK   J01 span    12 anchor found at line(s) [12]
OK   J02 span    13 anchor found at line(s) [13]
OK   J03 span    12 anchor found at line(s) [12]
OK   J04 span    13 anchor found at line(s) [13]
OK   J05 span    17 anchor found at line(s) [17]
OK   J06 span    12 anchor found at line(s) [12]
OK   J07 span    13 anchor found at line(s) [13]
OK   J08 span    12 anchor found at line(s) [12]
OK   J09 span    13 anchor found at line(s) [13]
OK   J10 span    18 anchor found at line(s) [18]
OK   J11 span    19 anchor found at line(s) [19]
OK   J12 span    12 anchor found at line(s) [12]
OK   J13 span    13 anchor found at line(s) [13]
OK   J14 span 18-20 anchor found at line(s) [20]
OK   J15 span 22-31 anchor found at line(s) [26]
ANCHOR CHECK: 15/15 in-span; misses=0
```

- **Count verified: 15/15 anchors in-span. Misses: 0.** No anchor had any
  occurrence outside its declared span either (the checker reports
  `[also outside span: …]` when that happens; it never did).
- Independent row-count cross-check by line prefix (count only, not the anchor
  method): `grep -c '^| J'` → 15; `grep -c '^| S'` → 2. Declared inventory
  "15 JSON facts; 2 editorial rows; 17 total mapped rows; 13 distinct excerpt
  anchors" matches: set of the 15 JSON + 2 editorial anchor strings has
  cardinality 13 (J01=J03=J12 and J02=J04=J13 repeat).
- Editorial bonus rows: `S01 source-excerpt.md span 5-5: hits=[5] in-span=[5]`,
  same for S02.

## Step 3 — inherited line numbers preserved

```
INHERITED PRESERVATION: 14/14 identical (span+anchor+excerpt) vs r94 map; mismatches=0
NEW rows vs r94: ['J15']
  J15 pointer=timeline.json#/3 excerpt=fictional-excerpts.md span=22-31 src=aru-aftermath-note ns=r95-crossing-aftermath:aru-aftermath-note mode=verbatim
```

Physical-line check against the r94 excerpt file (not just the r94 map):

```
J01 anchor-lines r94=[12] r95=[12] PRESERVED
J02 anchor-lines r94=[13] r95=[13] PRESERVED
J05 anchor-lines r94=[17] r95=[17] PRESERVED
J06 anchor-lines r94=[12] r95=[12] PRESERVED
J07 anchor-lines r94=[13] r95=[13] PRESERVED
J08 anchor-lines r94=[12] r95=[12] PRESERVED
J09 anchor-lines r94=[13] r95=[13] PRESERVED
J10 anchor-lines r94=[18] r95=[18] PRESERVED
J11 anchor-lines r94=[19] r95=[19] PRESERVED
J14 anchor-lines r94=[20] r95=[20] PRESERVED
inherited anchors with changed physical lines: 0
J15 anchor in r94 file? []
```

`fictional-excerpts.md`: r94 21 lines → r95 32 lines, **common prefix 21/21
lines** (pure append; r94 lines 12,13,17,18,19,20 byte-preserved). The new
content starts at line 22 (`## Round 95 aftermath note (2026-10-17)`), anchor
line 26 is `> Tick 11: I waited at the Chalk Stair through the agreed bell.`
(unique in the file).

Byte copies (P3's declared preserving copy): `entities.json`, `relations.json`,
`contradictions.json`, `inspiration-note.md`, `source-excerpt.md` all
**sha256 IDENTICAL** to r94 (e.g. entities `026af0bc2cdab150…`, source-excerpt
`b5edc2fd3c2e3d4f…`). Modified JSON files are additive at the JSON level:
`timeline[0:3] == r94` → `True` (len 4 now); `sources[0:3] == r94` → `True`
(new source `aru-aftermath-note` appended); `timeline[3]` =
`{"id": "aftermath-missing-evin", "tick": 11, "entity_id": "aru", "place_id":
"chalk-stair", "depends_on": ["paired-crossing-decision"], "source_id":
"aru-aftermath-note", …}`. (Line-level prefix checks for those two JSON files
necessarily diverge mid-file — indentation/commas — which is expected and not
an anchor issue.)

Pointer resolution (independent, direct JSON reads): J06–J15 resolve to dicts
whose `source_id` **matches** the map's In-world source ID column; J01–J05
resolve to the scalar `first_appearance` strings (no `source_id` field there —
expected).

## Step 4 — cross-evidence from the round's own tools (not my method)

Receipts below are from the **revised** (r95, P1) tool, taken 16:28:57 after
P1's report `P1-tool-code.md` existed; the map under test was unchanged
(`30281ff1a497bbe6`).

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                      (exit 0)
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS                      (exit 0)
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
RESULT PASS                      (exit 0)
$ python3 corpus/tools/map_obligations.py --self-test   # 22 'SELF-TEST PASS' lines
RESULT PASS

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                      (exit 0)
```

The revised tool's own inventory counts agree with my independent line-slice
count (15 JSON facts / 2 editorial / 17 total). An earlier receipt taken at
16:23:2x against a **partially written** `map_obligations.py` (file mtime
16:23:37) is recorded here only as an observed transient, not a defect claim:
it exited 1 with `ValueError: too many values to unpack (expected 2, got 15)`
from `compare()` and `--self-test` printed
`FINDING self_test_contract: contract self-test cases do not match the implemented cases`.
That state resolved by 16:28:57 with P1's report present; P2's contract file
was still unmodified at 16:23:42 (`map-obligations-contract.json` mtime
15:01:17), consistent with the mid-edit window.

## Step 5 — bounded observations (not anchor failures; for other seats)

1. The R9 declarations row declares `fictional-excerpts.md:12-29`, while J15's
   own span is 22-31. The J15 anchor (line 26) is inside both, so there is no
   anchor miss; the 29-vs-31 endpoint difference is a declaration-granularity
   observation for the contract/doc seats, recorded here, not counted against
   the seat claim.
2. J15's span 22-31 is the whole appended section while its anchor is the
   single line-26 sentence; the map's own line 51 discloses exactly this
   (span = appended section, anchor = tick-11 waiting sentence). Consistent.
3. `timeline[3]` uses `entity_id: "aru"` while its description names Evin's
   non-arrival; the map line 51 discloses the one-actor-slot encoding. No
   breach/other-duty assertion is made by the record.

## Bottom line

PASS — 15/15 r95 map anchors verified in-span by independent python line-slice
(0 misses; 2/2 editorial bonus rows also in-span), 14/14 inherited rows
identical to r94 in span+anchor+excerpt and physically at the same line
numbers, on the frozen revision `claim-excerpt-map.md` sha256 `30281ff1…`.
