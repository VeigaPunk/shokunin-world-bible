# Q4 — fixture-json (round 96)

Seat: Q4 fixture-json. Exclusive write scope per seat spec:
`corpus/fixtures/r96-crossing-response/` `{entities,relations,contradictions}.json` +
`{inspiration-note,source-excerpt}.md` (byte copies of `r95-crossing-aftermath` at
baseline `dcb2d92`) plus `{sources,timeline}.json` and `fictional-excerpts.md`
(byte-prefix extensions per spec). No other writes; no commits.

Baseline: HEAD `60dba0c` (r95 closure commit `dcb2d92`; `LOG.md` was already modified
by the round declaration before this seat ran).

Tool revisions in the working tree while receipts ran (2026-10-17T17:38–17:41-03:00):

- `corpus/tools/map_obligations.py` sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`
  (the r95 delivered revision; Q1's r96 hardening had not landed at receipt time)
- `corpus/fixtures/check_bible.py` sha256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
- `corpus/tools/map-obligations-contract.json` sha256 `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db`

## Step 1 — byte copies from dcb2d92 (before modification)

```
$ git show dcb2d92:corpus/fixtures/r95-crossing-aftermath/<f> > corpus/fixtures/r96-crossing-response/<f>
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do
    git show dcb2d92:corpus/fixtures/r95-crossing-aftermath/$f | sha256sum; sha256sum corpus/fixtures/r96-crossing-response/$f; done
```

Observed: SAME for all five (git-show hash == delivered hash).

| file | r95 baseline sha256 (== delivered sha256) |
|---|---|
| entities.json | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` |
| relations.json | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` |
| contradictions.json | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |
| inspiration-note.md | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` |
| source-excerpt.md | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` |

## Step 2 — modifications (diffs against dcb2d92 r95 bytes)

`diff <(git show dcb2d92:corpus/fixtures/r95-crossing-aftermath/sources.json) corpus/fixtures/r96-crossing-response/sources.json`:

```
24a25,30
>   },
>   {
>     "id": "evin-response-note",
>     "title": "Evin's Salt Court Response Note",
>     "kind": "fictional first-person note",
>     "reliability_note": "Newly authored fictional note; Evin reports being at Salt Court through the same agreed bell. It asserts no accusation against Aru, selects no winner, and states that both first-person accounts stand unresolved. It records one crossing occasion only and is not evidence of a breach, a continuing duty, a perpetual obligation, or an external historical fact."
```

`diff` for `timeline.json`:

```
41a42,52
>   },
>   {
>     "id": "response-evin-salt-court",
>     "tick": 12,
>     "entity_id": "evin",
>     "place_id": "salt-court",
>     "depends_on": [
>       "aftermath-missing-evin"
>     ],
>     "description": "Evin reports being at Salt Court through the same agreed bell; the note asserts no accusation against Aru, selects no winner, and states that both first-person accounts stand unresolved.",
>     "source_id": "evin-response-note"
```

`diff` for `fictional-excerpts.md` (append only; r95's bytes are a strict byte-prefix,
1845 → 2588 B, verified with `cmp -n` and a Python `startswith` check):

```
31a32,42
> 
> ## Round 96 response note (2026-10-17)
> 
> Newly authored fictional first-person note, attributed to in-world source ID `evin-response-note`, folio 6, lines 1–4. This section is appended after the preserved r95 text above; the inherited wording is unchanged.
> 
> > Tick 12: I was at Salt Court through the same agreed bell.
> > I make no accusation against Aru.
> > I select no winner between our two accounts.
> > Both accounts stand unresolved.
> 
> Scope: this appended section is Evin's first-person report of one crossing occasion. It asserts no accusation and no breach, selects no winner, and does not resolve the two first-person accounts against each other; the crossing-scoped agreement above is unchanged, and the record supplies no other duty.
```

The five byte-copy files: `cmp` → byte-identical, no diff output.

Mid-seat correction (before any receipt in this report): the first append placed the
joining comma on its own line (`  }\n,\n  {` — valid JSON but off-convention). Both
files were rewritten at 17:39 to `  },\n  {` before the receipts below ran; no receipt
quoted here was taken against the discarded intermediate.

## Step 3 — required gate: check_bible CLEAN

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

Control on the inherited fixture, same tool revision:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

## Step 4 — structural checks (python3, values parsed from delivered files)

```
entities.json: rows 5->5 inherited parsed-value identical=True
relations.json: rows 1->1 inherited parsed-value identical=True
contradictions.json: rows 0->0 inherited parsed-value identical=True
sources.json: rows 4->5 inherited parsed-value identical=True
timeline.json: rows 4->5 inherited parsed-value identical=True
byte-prefix (up to the last inherited row close) identical:
  sources.json True (1225 -> 1741 B); timeline.json True (1254 -> 1677 B)
fictional-excerpts.md byte-prefix identical: True (1845 -> 2588 B)
source ids unique: True ['veil-verse','paired-clock','crossing-minute','aru-aftermath-note','evin-response-note']
event ids unique: True ['aru-ninth-bell','evin-ninth-bell','paired-crossing-decision','aftermath-missing-evin','response-evin-salt-court']
entity ids unique: True
new source unique id: True; new event unique id: True
depends_on resolves: True ['aftermath-missing-evin']; tick order 11 < 12: True
contradictions rows: 0
raw source-attributed obligations: 16 (entities first_appearance 5 + claims 5 + relations 1 + timeline 5)
```

Counts match the C2 declaration: 5 entities / 1 relation / 4→5 events / 4→5 sources;
16 obligations (15 inherited unchanged + 1 new event row); no new claims/entities/
relations (entities.json, relations.json, contradictions.json byte-identical to r95).

## Step 5 — scope audit (appended section only)

- All assertions are negating/scoping: `no accusation` (2×), `no winner` (2×),
  `both accounts stand unresolved` (1×), `no breach`, `no other duty`.
- `alliance` 0, `betray` 0, `perpetual` 0, `continuing` 0 occurrences in the new section.
- No winner selected; no contradiction asserted (`contradictions.json` empty); event
  description explicitly scoped to Evin's report; no canon-truth or rights inference.
- Event is `entity_id` `evin`, `place_id` `salt-court`, `depends_on`
  `["aftermath-missing-evin"]` per spec, tick 12 after its dependency's tick 11.

## Step 6 — tool receipts (Q5's map had not landed)

At 2026-10-17T17:40-03:00, `claim-excerpt-map.md` did not exist in the fixture:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
FINDING map_missing: expected exactly one conventional claim-to-excerpt map
RESULT ERROR
exit=2
```

This is expected: the map is Q5's artifact. Control with the same working-tree tool
(r95 revision `d1c239cc…`) on the inherited fixture, whose map exists:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0
```

## Step 6b — after Q5's map landed (poll result, 2026-10-17T17:43:18-03:00)

Bounded poll (20 s cadence) found `claim-excerpt-map.md` after 12 tries; Q5's
`README.md` also landed at 17:43. Artifact hashes at receipt time:

- `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` sha256
  `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8`
- `corpus/fixtures/r96-crossing-response/README.md` sha256
  `ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456`
- `corpus/tools/map_obligations.py` still `d1c239cc…4212108` (the r95 revision;
  Q1's r96 hardening had not landed at 17:43; a bounded poll for it was still running
  at report finalization — a Step 6c re-run will be appended if it lands)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J15 (inherited rows, same anchors/lines as r95's receipt: 12, 13, 17, 18, 19, 20, 26)
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book …
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book …
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
exit=0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

Inherited map rows cross-checked against r95's map, parsed cell-by-cell:

```
inherited rows compared: 15 -> J01…J15
rows differing at all: J01…J15
rows differing beyond the namespace column (index 3): []
J15 namespace: `r95-crossing-aftermath:aru-aftermath-note` -> `r96-crossing-response:aru-aftermath-note`
new row J16: pointer `timeline.json#/4`, source `evin-response-note`, span 33-42, anchor `Tick 12: I was at Salt Court through the same agreed bell.`
```

Every inherited row differs only in the path-qualified namespace cell; pointer, raw
source ID, excerpt path, span, mode, and anchor are identical. J16 points at my
delivered bytes (excerpts lines 33–42, anchor line 37). The declared "16 map
obligations (15 inherited unchanged + 1 new event)" is confirmed end-to-end:
`OBLIGATIONS raw=16 mapped=16`, `INVENTORY JSON-FACTS 16/16`.

## Step 6c — re-run under the hardened Q1 revision (2026-10-17T17:46)

The r96 tool was mid-edit at 17:44:41 (hash `8729f1f3…`), and at that instant it raised
a Python traceback — `ValueError: too many values to unpack (expected 4, got 5)` in
`run_cluster` (a partial rewrite: `parse_map` already returned 5 values). Both r96 and
r95 invocations exited 1 with that traceback (not the documented 0/1/2 contract).
Recorded exactly as observed: a mid-write snapshot during concurrent production, not a
delivered-revision defect.

A stability poll (two consecutive identical hashes with the r95 control passing) saw the
tool settle at 17:46:16 on sha256
`c2c284c0118cf66bed019c43dde87caabcdce8ccda957a82230d7c5b35d029da` (unchanged at
17:46:38). Receipts under that revision:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

At the same revision the tool reports `SELF-TEST CASES 22/24 pinned` and
`--self-test` → `RESULT PASS` exit 0, while `map-obligations-contract.json` is still
`8173bb97…` with 22 cases — i.e. the C1(b) 24-case pinning had not landed at 17:46.
Reported as an observed in-progress state of the C1 bundle (Q1/Q2 seats), not a
fixture finding.

## Facts for verifiers

- Delivered sha256: entities.json `026af0bc…2ae03b`, relations.json `c279254b…4a6ff9`,
  contradictions.json `37517e5f…0985b570`, inspiration-note.md `58f5390e…bcc82d37`,
  source-excerpt.md `b5edc2fd…4d76d4cd`, sources.json
  `9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d`, timeline.json
  `ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9`,
  fictional-excerpts.md `06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3`.
- r95 baseline (dcb2d92) hashes of the three extended files: sources.json
  `fd9e30e8…1927e64a`, timeline.json `3c0faad6…b00ea177`, fictional-excerpts.md
  `0ef6734a…0880b282`.
- Q5 artifact hashes (not owned by this seat): `claim-excerpt-map.md`
  `5093d72e…3045bfd8`, `README.md` `ff52ced4…3558c456`.
- Census: `git ls-tree -d --name-only dcb2d92 corpus/fixtures/ | wc -l` → 169;
  `find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l` → 170 (this fixture
  is the +1). No parent-tree strays: `find /home/vgpnk/Projects/shokunin -maxdepth 3
  -name r96-crossing-response` returns nothing outside `lore-shokunin/`.
- Pointer candidates: `sources.json#/4` (id `evin-response-note`, id line 27),
  `timeline.json#/4` (id `response-evin-salt-court`, id line 44). Inherited pointers
  `sources.json#/0…#/3`, `timeline.json#/0…#/3`, `entities.json#/0…#/4`,
  `relations.json#/0` are value-unchanged.
- Excerpt line map: heading 33, attribution 35, quoted lines 37–40, scope 42; the r95
  section and its quotes keep their original line numbers (append starts at line 32).
- `wc`: sources.json 1741 B / 32 lines, timeline.json 1677 B / 54 lines,
  fictional-excerpts.md 2588 B / 42 lines.
- No other paths written: `git status --porcelain` shows only ` M LOG.md` (pre-seat),
  `?? .ufo/waves/round-96/` (seat scratch/reports), and
  `?? corpus/fixtures/r96-crossing-response/`.

## Bottom line

PASS — all eight owned files delivered; required gate `check_bible` CLEAN exit 0;
counts 5/1/0/5/5 with 16 raw obligations; inherited r95 rows parsed-value identical and
byte-prefix preserved; five byte-copy files byte-identical; end-to-end
`map_obligations` `OBLIGATIONS raw=16 mapped=16` + `support_check`
`SOURCE-SUPPORT 16/16 … RESULT PASS` exit 0 under both the r95 revision `d1c239cc` and
the stabilized r96-in-progress revision `c2c284c0`; census 169→170; all 15 inherited map
rows identical to r95's apart from the namespace column; J16 anchored at the delivered
tick-12 line 37. (Observed mid-edit transient at 17:44:41: tool `8729f1f3…` raised a
Python `ValueError` traceback on both fixtures — an in-progress Q1 write, reported, not
a fixture finding; C1's 24-case pinning had not landed at 17:46 — `SELF-TEST CASES
22/24 pinned`.)
