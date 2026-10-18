# V11 — c2-anchors (round 96)

Seat: V11 c2-anchors. Scope per seat spec: independently verify that ALL 16
anchors in `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`
resolve in-span via my own `grep -nF` implementation; every inherited anchor
must exist at the SAME line numbers as in r95's map; the new anchor only
inside the appended response section; report any drift with path:line.

Baseline: r95 closure `dcb2d92`. Repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin`. No commits; no network; no
repo writes except this report and my declared scratch dir
`.ufo/waves/round-96/seats/V11-scratch/` (checker, poll script, logs; all
paths absolute under the lane repo). No nested agents.

## 0. Poll-wait evidence (target = Q5's map + Q4/Q5 reports)

40-try background poll (20 s cadence), requiring Q4's
`fictional-excerpts.md`/`source-excerpt.md`, Q5's `claim-excerpt-map.md`, and
Q4/Q5 seat reports, plus a 20 s byte-stability window (log
`.ufo/waves/round-96/seats/V11-scratch/poll.log`):

```
try=1..7  20:40:01-20:42:01 map=n fx=y src=y q4rep=none q5rep=none
try=8..10 20:42:21-20:43:01 map=n fx=y src=y q4rep=.ufo/waves/round-96/seats/Q4-fixture-json.md q5rep=none
try=11..17 20:43:21-20:45:21 map=y fx=y src=y q4rep=.ufo/waves/round-96/seats/Q4-fixture-json.md q5rep=none
try=18 20:45:41 stability-wait md5set=cde9ec564697a6dc8ad77a54f95422fe q5rep=.ufo/waves/round-96/seats/Q5-fixture-docs.md
try=19 20:46:01 READY-STABLE md5set=cde9ec564697a6dc8ad77a54f95422fe
```

Verification ran on that frozen revision. Pins re-checked at 20:46:36
(unchanged after my run):

```
711e59f0f69482c795d87b1b9261a843  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
8760854b75221c941a5e58281a4511b7  corpus/fixtures/r96-crossing-response/fictional-excerpts.md
b54e1d67f65bce6120086796499c0518  corpus/fixtures/r96-crossing-response/source-excerpt.md
```

`git status --porcelain corpus/fixtures/r96-crossing-response/` → `??`
(untracked, pre-closure state; expected — no commits in this wave).

## 1. Method

Checker: `.ufo/waves/round-96/seats/V11-scratch/v11_check.py` (my own
implementation; output archived at `V11-scratch/run-output.txt`). It parses
both maps' row tables, then for every r96 row runs
`grep -nF -e "<anchor>" -- <excerpt>` via `subprocess` and cross-checks the
line numbers against a pure-Python `line.count(anchor)` scan; checks in-span
containment, outside-span occurrences, inherited-row anchor/span equality +
resolved line sets r95 vs r96, new-row occurrence placement, byte-prefix
discipline, and the declared inventory. Parser validated first on r95↔r94
(`validate` mode): `ALL-ANCHOR-CHECKS-PASS`, inventory declared
`[15, 2, 17, 13]` == parsed, exit 0 — reproducing r95's map exactly.

## 2. Result — checker output (run mode, verbatim, condensed to per-row lines)

```
== RUN r96 vs r95: parsed 16 json rows, 2 editorial rows ==
J01  span=12-12  grep=[12] py=[12] IN-SPAN outside-span=[]  vs-ref: anchor-identical=True span-same=True lines ref=[12] == this=[12] same=True
J02  span=13-13  grep=[13] py=[13] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[13]==this=[13] True
J03  span=12-12  grep=[12] py=[12] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[12]==this=[12] True
J04  span=13-13  grep=[13] py=[13] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[13]==this=[13] True
J05  span=17-17  grep=[17] py=[17] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[17]==this=[17] True
J06  span=12-12  grep=[12] py=[12] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[12]==this=[12] True
J07  span=13-13  grep=[13] py=[13] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[13]==this=[13] True
J08  span=12-12  grep=[12] py=[12] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[12]==this=[12] True
J09  span=13-13  grep=[13] py=[13] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[13]==this=[13] True
J10  span=18-18  grep=[18] py=[18] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[18]==this=[18] True
J11  span=19-19  grep=[19] py=[19] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[19]==this=[19] True
J12  span=12-12  grep=[12] py=[12] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[12]==this=[12] True
J13  span=13-13  grep=[13] py=[13] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[13]==this=[13] True
J14  span=18-20  grep=[20] py=[20] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[20]==this=[20] True
J15  span=22-31  grep=[26] py=[26] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[26]==this=[26] True
J16  span=33-42  grep=[37] py=[37] IN-SPAN outside-span=[]  pre95=[] appended-only=True
S01  span=5-5    grep=[5] py=[5] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[5]==this=[5] True   (source-excerpt.md)
S02  span=5-5    grep=[5] py=[5] IN-SPAN outside-span=[]  vs-ref: True/True/ref=[5]==this=[5] True   (source-excerpt.md)
new row ids (vs ref): ['J16']
inventory declared=[16, 2, 18, 14] parsed=[16, 2, 18, 14] match=True
declared-line: **Expected inventory:** 16 JSON facts; 2 editorial rows; 18 total mapped rows; 14 distinct excerpt anchors.
fictional-excerpts.md: ref=1845B this=2588B byte-prefix-ok=True
ALL-ANCHOR-CHECKS-PASS  EXIT=0
```

(Full uncondensed lines, including each `vs-ref` line verbatim, are in
`V11-scratch/run-output.txt`.) All 16 JSON anchors (J01–J16) plus both
editorial anchors (S01, S02) resolve in-span. `grep -nF` and the pure-Python
scan agreed on the exact line-number set for every one of the 18 rows; every
row has occurrence count 1 (`occ=1`) and no occurrence outside its declared
span (`outside-span=[]` everywhere — so no inherited anchor leaked into the
appended section).

## 3. Inherited anchors — same line numbers as r95

For each of the 17 inherited rows (J01–J15, S01, S02): the anchor string is
identical to the r95 map's anchor, the declared span is unchanged, and the
resolved line numbers in the r96 copy equal those in the r95 fixture exactly
(every `vs-ref` line above: `same=True`). Resolved lines:

| rows | resolved lines (r95 == r96) |
|---|---|
| J01/J03/J06/J08/J12 | 12 |
| J02/J04/J07/J09/J13 | 13 |
| J05 | 17 |
| J10 | 18 |
| J11 | 19 |
| J14 | 20 (span 18-20) |
| J15 | 26 (span 22-31) |
| S01/S02 | 5 (source-excerpt.md) |

Raw `grep -nF` samples (r96 vs r95):

```
$ grep -nF -e 'Aru carried the north lantern at Quiet Rise' -- <r96>/fictional-excerpts.md
12:> Tick 9: Aru carried the north lantern at Quiet Rise.
$ grep -nF -e 'Aru carried the north lantern at Quiet Rise' -- <r95>/fictional-excerpts.md
12:> Tick 9: Aru carried the north lantern at Quiet Rise.
$ grep -nF -e 'Their tick-10 decision ... at the midpoint.' -- <r96>/fictional-excerpts.md
20:> Their tick-10 decision depends on both ninth-bell entries: ... at the midpoint.
$ grep -nF -e 'Their tick-10 decision ... at the midpoint.' -- <r95>/fictional-excerpts.md
20:> ... same line 20 ...
$ grep -nF -e 'Tick 11: I waited at the Chalk Stair through the agreed bell.' -- <r96>/fictional-excerpts.md
26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
```

Byte-prefix check of the excerpt file (r95 text = lines 1–31, `wc -l` 31;
r96 = 42 lines):

```
$ wc -l <r95>/fictional-excerpts.md <r96>/fictional-excerpts.md
  31 <r95>/fictional-excerpts.md
  42 <r96>/fictional-excerpts.md
$ head -c 1845 <r96>/fictional-excerpts.md | cmp - <r95>/fictional-excerpts.md && echo BYTE-PREFIX-OK
BYTE-PREFIX-OK
```

## 4. New response anchor — only in the appended section

J16: pointer `timeline.json#/4`, source `evin-response-note`, excerpt
`fictional-excerpts.md`, span 33-42, anchor
`Tick 12: I was at Salt Court through the same agreed bell.`

```
$ grep -nF -e 'Tick 12: I was at Salt Court through the same agreed bell.' -- <r96>/fictional-excerpts.md
37:> Tick 12: I was at Salt Court through the same agreed bell.
$ grep -nF -e 'Tick 12: I was at Salt Court through the same agreed bell.' -- <r95>/fictional-excerpts.md
(no output, exit 1)
```

The anchor occurs exactly once, at line 37, inside the appended response
section (r95 text = lines 1–31; appended lines 32–42; line 33 heading, line
37 the first quoted sentence, line 42 the scope line). Checker fields:
`pre95=[] appended-only=True` (absent from the r95 file entirely; all r96
occurrences > line 31). Span 33-42 lies within the file (42 lines) and covers
only appended lines.

## 5. Copy discipline and corroboration

```
$ for f in source-excerpt.md entities.json relations.json contradictions.json inspiration-note.md; do cmp -s <r95>/$f <r96>/$f && echo "$f IDENTICAL"; done
source-excerpt.md IDENTICAL
entities.json IDENTICAL
relations.json IDENTICAL
contradictions.json IDENTICAL
inspiration-note.md IDENTICAL
```

`sources.json` / `timeline.json` prefix discipline (python `r96[:4] == r95`
for both → True): the r95 four entries are unchanged; r96 appends exactly
`evin-response-note` (source 5) and `response-evin-salt-court` (tick 12,
evin, salt-court, depends_on [aftermath-missing-evin]).

Corroboration only (not my seat's claim): the in-repo `support_check.py`
(not owned by any r96 producer) on the same frozen revision:

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
... PASS J16 ... anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS   EXIT=0
```

Its found-line numbers (12,13,17,18,19,20,26,37; S at 5) match my
independent `grep -nF` results exactly.

## 6. Drift findings

None. No anchor drift, no line-number drift, no span drift, no path drift, no
out-of-span occurrence, no inventory inconsistency. Nothing to report as
`path:line`.

## 7. Boundaries (not verified by this seat)

- Anchor resolution is lexical (`grep -nF` + substring scan); it is not
  semantic entailment of the JSON facts, chronology, or canon judgment.
- `map_obligations.py` and `check_bible` were not re-run by me; the map's
  declared inventory was checked against my own parse (16/2/18/14), and
  `support_check.py` was run only as corroboration.
- The namespace-column re-qualification (`r95-crossing-aftermath:` →
  `r96-crossing-response:`) was checked only as the expected change; its
  naming correctness is Q5's claim.
- JSON counts (5 entities / 1 relation / 5 events / 5 sources) and sibling
  copy discipline are supporting evidence, not the seat's anchor claim.

## Bottom line

PASS — all 16 JSON anchors (J01–J16) + 2 editorial anchors resolve in-span;
all 17 inherited anchors are identical and resolve at the same line numbers
as r95's map; the new response anchor occurs only at
`corpus/fixtures/r96-crossing-response/fictional-excerpts.md:37` inside the
appended response section; zero drift.
