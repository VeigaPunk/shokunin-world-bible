# V11 — c2-anchors (round 95)

Seat: V11 c2-anchors. Scope per seat spec: independently verify that ALL 15
anchors in `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`
resolve in-span via my own `grep -nF` implementation; every inherited anchor
must exist at the SAME line numbers as in r94's map (byte-prefix discipline);
the new aftermath anchor only inside the appended section; report any drift
with path:line.

Baseline: r94 closure `fb118c4`. Repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin`. No commits; no network; no
repo writes except this report (my checker script lived at `/tmp/v11_check.py`,
outside the repo). No nested agents.

## 0. Poll-wait evidence (target = P4's map + P4 report)

40-try background poll (20 s cadence), requiring P3's
`fictional-excerpts.md`/`source-excerpt.md`, P4's `claim-excerpt-map.md`, and
a `P4*.md` seat report, plus a 10 s byte-stability window:

```
try=1..4 16:20:00-16:21:00 map=n excerpts=y src=y p4rep=none
try=5..7 16:21:20-16:22:00 map=y excerpts=y src=y p4rep=none
try=8    16:22:20 map=y excerpts=y src=y p4rep=.ufo/waves/round-95/seats/P4-fixture-docs.md
READY stable at try=8 md5=0c20f6b102110e08b454309b1e0c9eb9
```

Verification ran on that frozen revision. Pins re-checked at 16:23:02
(unchanged after my run):

```
a872889e86a10127750ba0647e4829ff  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
169e0691fb45ed4c41c7b787bbcb5348  corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
b54e1d67f65bce6120086796499c0518  corpus/fixtures/r95-crossing-aftermath/source-excerpt.md
```

Reference r94 map (pristine, matches HEAD; `git diff HEAD -- corpus/fixtures/r94-paired-crossing/` empty):
`9ddad5753b04cae0196358e3005966bb  corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md`;
r94 excerpts `132cffac5c0c89a612c381d8323e9751` (1116 B).

## 1. Method

`python3 /tmp/v11_check.py` (kept outside the repo): parses both maps'
row tables, then for every r95 row runs
`grep -nF -e "<anchor>" -- <excerpt>` via `subprocess` and cross-checks the
line numbers against a pure-Python `line.find(anchor) != -1` scan; checks
in-span containment, outside-span occurrences, inherited-row byte equality
(anchor/span/path + resolved line sets r94 vs r95), new-row occurrence
placement, byte-prefix discipline, and the declared inventory. The parser was
validated first on r94↔r94 (16/16 rows IN-SPAN, `ALL-ANCHOR-CHECKS-PASS`,
exit 0), which reproduced the r94 map's declared inventory exactly
(14/2/16/12).

## 2. Result — full checker output (verbatim, condensed to per-row lines)

```
r94 rows: J01..J14, S01, S02
r95 rows: J01..J15, S01, S02
r95 parsed: 15 json rows, 2 editorial rows, 17 total, 13 distinct anchors
r94 parsed: 14 json rows, 2 editorial rows, 16 total, 12 distinct anchors

J01  span=12-12  fx grep=[12] py=[12] IN-SPAN outside-span=[]
J02  span=13-13  fx grep=[13] py=[13] IN-SPAN outside-span=[]
J03  span=12-12  fx grep=[12] py=[12] IN-SPAN outside-span=[]
J04  span=13-13  fx grep=[13] py=[13] IN-SPAN outside-span=[]
J05  span=17-17  fx grep=[17] py=[17] IN-SPAN outside-span=[]
J06  span=12-12  fx grep=[12] py=[12] IN-SPAN outside-span=[]
J07  span=13-13  fx grep=[13] py=[13] IN-SPAN outside-span=[]
J08  span=12-12  fx grep=[12] py=[12] IN-SPAN outside-span=[]
J09  span=13-13  fx grep=[13] py=[13] IN-SPAN outside-span=[]
J10  span=18-18  fx grep=[18] py=[18] IN-SPAN outside-span=[]
J11  span=19-19  fx grep=[19] py=[19] IN-SPAN outside-span=[]
J12  span=12-12  fx grep=[12] py=[12] IN-SPAN outside-span=[]
J13  span=13-13  fx grep=[13] py=[13] IN-SPAN outside-span=[]
J14  span=18-20  fx grep=[20] py=[20] IN-SPAN outside-span=[]
J15  span=22-31  fx grep=[26] py=[26] IN-SPAN outside-span=[]
S01  span=5-5    source-excerpt.md grep=[5] py=[5] IN-SPAN outside-span=[]
S02  span=5-5    source-excerpt.md grep=[5] py=[5] IN-SPAN outside-span=[]

== inherited rows vs r94 ==
J01..J14, S01, S02: anchor-identical=YES, lines r94=[..] == r95=[..] same=True (every row)

== new rows ==
new row ids: ['J15']
J15: excerpt=fictional-excerpts.md span=(22, 31) grep=[26]
     pre-appended(<=20)=[]  appended=[26]

== byte-prefix / copy discipline ==
fictional-excerpts.md: r94=1116B r95=1845B byte-prefix-ok=True
source-excerpt.md: byte-identical=True (640B)

== inventory declaration vs parsed ==
declared r95 inventory numbers=[15, 2, 17, 13]; parsed=(15, 2, 17, 13)
ALL-ANCHOR-CHECKS-PASS  EXIT=0
```

All 15 JSON anchors (J01–J15) plus both editorial anchors (S01, S02) resolve
in-span. `grep -nF` and the pure-Python scan agreed on the exact line-number
set for every one of the 17 rows. No anchor has any occurrence outside its
declared span (outside-span=[] everywhere).

## 3. Inherited anchors — same line numbers (byte-prefix discipline)

For each of J01–J14 and S01–S02, the anchor string is byte-identical to the
r94 map's anchor, the declared span is unchanged, and the resolved line
numbers in the r95 excerpt copy equal those in the r94 file exactly:

| rows | resolved lines (r94 == r95) |
|---|---|
| J01/J03/J06/J08/J12 | 12 |
| J02/J04/J07/J09/J13 | 13 |
| J05 | 17 |
| J10 | 18 |
| J11 | 19 |
| J14 | 20 (span 18-20) |
| S01/S02 | 5 (source-excerpt.md) |

Raw `grep -nF` samples (r95 vs r94):

```
$ grep -nF -e 'Aru carried the north lantern at Quiet Rise' <r95>/fictional-excerpts.md
12:> Tick 9: Aru carried the north lantern at Quiet Rise.
$ grep -nF -e 'Aru carried the north lantern at Quiet Rise' <r94>/fictional-excerpts.md
12:> Tick 9: Aru carried the north lantern at Quiet Rise.
$ grep -nF -e 'There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.' <r95>...
19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
```

Because every inherited anchor's r95 line set equals its r94 line set, no
inherited anchor gained an occurrence inside the appended section either.

Byte-prefix check of the excerpt file itself:

```
$ A=corpus/fixtures/r94-paired-crossing/fictional-excerpts.md
$ B=corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
$ head -c "$(stat -c%s "$A")" "$B" | cmp - "$A" && echo BYTE-PREFIX-OK
BYTE-PREFIX-OK          # first 1116 bytes of r95 == whole r94 file
```

Additionally (cell-level comparison of the two maps): for every inherited row
the pointer, source-ID, excerpt-path, span, mode, and anchor cells are
identical to r94's, and the namespace cell is the expected
`r94-paired-crossing:` → `r95-crossing-aftermath:` re-qualification
(`cell diffs (expect none): NONE`). S01/S02 comparison/citation cells also
identical.

## 4. New aftermath anchor — only in the appended section

J15: pointer `timeline.json#/3`, source `aru-aftermath-note`, excerpt
`fictional-excerpts.md`, span 22-31, anchor
`Tick 11: I waited at the Chalk Stair through the agreed bell.`

```
$ grep -nF -e 'Tick 11: I waited at the Chalk Stair through the agreed bell.' <r95>/fictional-excerpts.md
26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
$ grep -nF -e 'Tick 11: I waited at the Chalk Stair through the agreed bell.' <r94>/fictional-excerpts.md
(no output, exit 1)
```

The anchor occurs only at line 26, which is inside the appended section
(r94 text = lines 1–20; appended lines 21–31, file `wc -l` = 31; line 21 is
the blank separator, line 22 the section heading, line 26 the first quoted
sentence). It is absent from the r94 file entirely and present nowhere
outside the appended section. Span 22-31 lies within the file (31 lines) and
covers only appended lines.

## 5. Copy discipline for the anchor target files

```
$ cmp <r94>/source-excerpt.md <r95>/source-excerpt.md && echo SOURCE-EXCERPT-IDENTICAL
SOURCE-EXCERPT-IDENTICAL
$ for f in entities.json relations.json contradictions.json inspiration-note.md; do cmp -s <r94>/$f <r95>/$f && echo "$f IDENTICAL"; done
entities.json IDENTICAL
relations.json IDENTICAL
contradictions.json IDENTICAL
inspiration-note.md IDENTICAL
```

## 6. Drift findings

None. No anchor drift, no line-number drift, no span drift, no path drift, no
out-of-span occurrence, no inventory inconsistency. Nothing to report as
`path:line`.

## 7. Boundaries (not verified by this seat)

- Anchor resolution is lexical (`grep -nF` + substring scan); it is not
  semantic entailment of the JSON facts, source-id binding correctness beyond
  inherited-row equality, chronology, or canon judgment.
- `support_check.py` / `map_obligations.py` receipts and `check_bible` were
  not re-run by me; the map's claimed inventory was checked against my own
  parse (15/2/17/13), not against those tools.
- The namespace-column re-qualification was checked only as the expected
  change; its naming correctness is P4's claim.
- P1 landed `corpus/tools/map_obligations.py` during my window (git status
  shows `M corpus/tools/map_obligations.py` at 16:23:02); this does not affect
  the fixture bytes verified here (fixture md5s unchanged before/after).

## Bottom line

PASS — all 15 JSON anchors + 2 editorial anchors resolve in-span; every
inherited anchor is byte-identical and resolves at the same line numbers as
r94; the new aftermath anchor occurs only at
`corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md:26` inside the
appended section; zero drift.
