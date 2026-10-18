# V45 — anchor-replica-2 (round 96)

Seat: V45 `anchor-replica-2`. Scope per seat spec: **third independent anchor
verification of r96's map using a pure-Python line-slice method (not grep)**: all
16 anchors in-span, inherited line numbers preserved; report the count verified
and any miss.

Baseline: HEAD `60dba0c` (r95 closure commit `dcb2d92`); working tree carried
`M LOG.md` plus untracked `.ufo/waves/round-96/` and
`corpus/fixtures/r96-crossing-response/` (producer outputs). Repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin` for every path below. Writes by
this seat: this report plus declared scratch
`.ufo/waves/round-96/seats/V45-scratch/` (`v45_check.py`, `v45_pointers.py`,
`run-full.txt`, `run-frozen.txt`, `run-control.txt`, `run-pointers.txt`,
`calib-a-r95.txt`, `calib-b-r95-vs-r94.txt`, `calib-c-control.txt`). No commits,
no pushes, no network, no nested agents, no other file touched.

## Step 0 — poll-wait

Target: `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` + Q5's seat
report. 20 s cadence, up to 40 tries. First poll attempt was defective (`ls
.../Q5*` matched the `Q5-scratch` **directory** contents, a false-READY risk); it
was stopped and restarted with `find .ufo/waves/round-96/seats -maxdepth 1 -type
f -name 'Q5*.md'`.

```
try=1..9  17:40:26-17:43:06 map=n rep=none
try=10..16 17:43:26-17:45:26 map=y rep=none     (map landed between try 9 and 10)
READY try=17 17:45:56 map=corpus/fixtures/r96-crossing-response/claim-excerpt-map.md rep=.ufo/waves/round-96/seats/Q5-fixture-docs.md
711e59f0f69482c795d87b1b9261a843  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
```

The loop slept a further 10 s before READY (byte-stability window). All checks
below were run on that frozen revision; the map was first read 17:43:26 and its
sha256 was identical at 17:44 (preliminary run) and 17:46:11/17:46:49 (frozen
runs), so the verified bytes did not move during this seat.

Verified revision (sha256, frozen at report time, re-checked unchanged after the
runs):

```
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  claim-excerpt-map.md        (10172 B, md5 711e59f0f69482c795d87b1b9261a843)
06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3  fictional-excerpts.md      (2588 B)
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md          (640 B)
ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456  README.md                  (4858 B)
9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d  sources.json
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  timeline.json
```

Reference r95 files were not modified this round (`git status --short
corpus/fixtures/` → only `?? corpus/fixtures/r96-crossing-response/`); r95 map
sha256 `30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a`
matches the value pinned in r95's V35 report, and r95
`fictional-excerpts.md` `0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282`.

## Step 1 — method (independent of grep, support_check, and map_obligations)

`V45-scratch/v45_check.py` (written by this seat, stdlib only): parses the `## JSON
facts` markdown table itself (rows matching `^\| J\d+ \|`, 8 cells), reads each
excerpt file once with `Path.read_text().split("\n")`, and resolves every anchor
by **line index** (`[i+1 for i,l in enumerate(lines) if anchor in l]`), asserting
at least one hit with `start <= line <= end`. It also compares inherited rows
against the r95 map (span + anchor + pointer + excerpt + mode equality), compares
the **physical line numbers** of each inherited anchor in the r95 file vs the r96
file, checks the new row's occurrences against the r95 file length, hashes the
byte-prefix of `fictional-excerpts.md`, and re-parses the declared inventory line.

Calibration (run before the r96 map existed, proving the green is not trivial):

```
calib-a  r95 map, 15 JSON rows      -> ANCHOR CHECK: 15/15 in-span; misses=[]      exit 0
calib-b  r95 map vs r94 ref map     -> INHERITED: 14 rows; cell mismatches=[]; changed physical lines=[]
                                       new row J15: pre-appended(<= 21)=[] appended=[26]
calib-c  r95 map, control           -> MISS J01 (span shifted 12-12 -> 13-13); exit 1
```

## Step 2 — anchor check on r96 (the seat's claim)

Command: `python3 .ufo/waves/round-96/seats/V45-scratch/v45_check.py
corpus/fixtures/r96-crossing-response/claim-excerpt-map.md --ref-map
corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md --json-expect 16`
→ `V45 VERDICT: PASS`, script exit 0. Observed output (abridged to the per-row
lines; full text in `V45-scratch/run-frozen.txt`):

```
PARSED r96 JSON-fact rows: 16 (ids: J01, J02, J03, J04, J05, J06, J07, J08, J09, J10, J11, J12, J13, J14, J15, J16)
DECLARED: **Expected inventory:** 16 JSON facts; 2 editorial rows; 18 total mapped rows; 14 distinct excerpt anchors.
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
OK   J16 span 33-42 anchor found at line(s) [37]
ANCHOR CHECK: 16/16 in-span; misses=[]; outside-span=[]
```

- **Count verified: 16/16 anchors in-span. Misses: 0.** No anchor had any
  occurrence outside its declared span either (`outside-span=[]` for all 16).
- Editorial bonus rows (checked by the same line-slice method): `S01
  span 5-5 in-span=[5] OK`, `S02 span 5-5 in-span=[5] OK`.

## Step 3 — inherited line numbers preserved (J01–J15)

```
INHERITED: 15 rows; cell mismatches=[]; changed physical lines=[]
  J01 span (12, 12)==(12, 12) anchor-identical=True lines r95=[12] r96=[12] PRESERVED
  J02 span (13, 13)==(13, 13) anchor-identical=True lines r95=[13] r96=[13] PRESERVED
  J03 span (12, 12)==(12, 12) anchor-identical=True lines r95=[12] r96=[12] PRESERVED
  J04 span (13, 13)==(13, 13) anchor-identical=True lines r95=[13] r96=[13] PRESERVED
  J05 span (17, 17)==(17, 17) anchor-identical=True lines r95=[17] r96=[17] PRESERVED
  J06 span (12, 12)==(12, 12) anchor-identical=True lines r95=[12] r96=[12] PRESERVED
  J07 span (13, 13)==(13, 13) anchor-identical=True lines r95=[13] r96=[13] PRESERVED
  J08 span (12, 12)==(12, 12) anchor-identical=True lines r95=[12] r96=[12] PRESERVED
  J09 span (13, 13)==(13, 13) anchor-identical=True lines r95=[13] r96=[13] PRESERVED
  J10 span (18, 18)==(18, 18) anchor-identical=True lines r95=[18] r96=[18] PRESERVED
  J11 span (19, 19)==(19, 19) anchor-identical=True lines r95=[19] r96=[19] PRESERVED
  J12 span (12, 12)==(12, 12) anchor-identical=True lines r95=[12] r96=[12] PRESERVED
  J13 span (13, 13)==(13, 13) anchor-identical=True lines r95=[13] r96=[13] PRESERVED
  J14 span (18, 20)==(18, 20) anchor-identical=True lines r95=[20] r96=[20] PRESERVED
  J15 span (22, 31)==(22, 31) anchor-identical=True lines r95=[26] r96=[26] PRESERVED
```

Every inherited row's pointer, span, anchor, excerpt path, and mode cell equals
the r95 map's; the resolved physical line numbers in the r96 excerpt copy equal
those in the r95 file exactly. No inherited anchor gained an occurrence inside
the appended section (`outside-span=[]` everywhere).

## Step 4 — new J16 row: only in the appended section

```
new row ids: ['J16']
  J16: excerpt=fictional-excerpts.md span=(33, 42) hits=[37] pre-appended(<= 32)=[] appended=[37]
```

The r95 file ends at split-line 32 (31 newlines + trailing empty); the r96 file
adds lines 33–42, i.e. line 33 = `## Round 96 response note (2026-10-17)`, line
37 = the J16 anchor `> Tick 12: I was at Salt Court through the same agreed
bell.`, line 42 = the section's scope sentence. Declared span 33-42 is exactly
that appended section.

## Step 5 — byte-prefix / copy discipline

```
fictional-excerpts.md r95=1845B r96=2588B prefix-ok=True
source-excerpt.md identical=True (640B)
```

`head -c 1845`-style byte comparison inside the checker: the first 1845 bytes of
the r96 file equal the whole r95 file. Pre-scan also found the five byte-copy
files identical to r95 (`entities.json`, `relations.json`, `contradictions.json`,
`inspiration-note.md`, `source-excerpt.md`).

## Step 6 — declared inventory vs parsed; independent count cross-check

```
declared=(16, 2, 18, 14) parsed=(16, 2, 18, 14) match=True
COUNT CHECK: 16 JSON rows == expected 16
```

Independent count-only cross-check (line prefixes, not the anchor method):
`grep -c '^| J'` → 16; `grep -c '^| S'` → 2; distinct J anchors by raw extraction
→ 12, plus S01/S02 = 14 distinct, matching the declared 14 (J01=J03=J12 and
J02=J04=J13 are the repeated references).

## Step 7 — bonus: pointer resolution (corroboration, not the seat's claim)

`V45-scratch/v45_pointers.py` resolves every row's pointer directly and compares
the bound `source_id` with the row's declared in-world source ID:

```
POINTER CHECK: 16/16 rows resolve and bind; bad=[]     exit 0
  J16 timeline.json#/4: exists, source_id='evin-response-note' row='evin-response-note' match=True
       ns=r96-crossing-response:evin-response-note ns-ok=True
```

## Step 8 — negative control on the frozen r96 revision

`python3 .../v45_check.py <r96 map> --control` → `MISS J01 span 13-13 anchor
found at line(s) [12]  [also outside span: [12]]`; `ANCHOR CHECK: 15/16 in-span;
misses=['J01']`; `V45 VERDICT: FAIL`, exit 1 (`run-control.txt`). A one-line span
shift in the real revision is reported as a miss, so the 16/16 green above is not
vacuous. Post-run re-hash at 17:46:49: map sha256 unchanged.

## Cross-checks

Q5's producer report (`Q5-fixture-docs.md`) independently declares the same map
sha256 `5093d72e…` / README sha256 `ff52ced4…`, the same inventory (16/2/18/14),
and the same inherited line numbers (via its own grep-based scratch scripts).
No disagreement with this seat's python line-slice method; no miss, no
outside-span occurrence, no ABSENT artifact. The seat's own scope — all 16
in-span, line numbers preserved — verifies on the delivered revision.

**Bottom line: PASS** — all 16 JSON-fact anchors in-span (misses=0, no
outside-span occurrences), all 15 inherited rows byte-identical in span/anchor
and preserved at identical physical line numbers, new J16 only inside the
appended section (span 33-42, line 37), byte-prefix and inventory checks clean,
negative control correctly fails.
