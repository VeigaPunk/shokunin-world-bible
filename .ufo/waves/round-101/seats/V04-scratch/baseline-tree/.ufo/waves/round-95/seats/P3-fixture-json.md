# P3 — fixture-json (round 95)

Seat: P3 fixture-json. Exclusive write scope per seat spec:
`corpus/fixtures/r95-crossing-aftermath/` `{entities,relations,contradictions}.json`,
`{inspiration-note,source-excerpt}.md` (byte copies of `r94-paired-crossing`) plus
`{sources,timeline}.json` and `fictional-excerpts.md` (byte copies modified per spec).
No other writes; no commits.

Baseline: HEAD `fb118c42038ed27a747eec704b9aab41bb4b2ebe` (r94 closure `fb118c4`).
Tool revisions in the working tree while receipts ran (2026-10-17T16:18–16:20-03:00):

- `corpus/tools/map_obligations.py` sha256 `cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790` (still the r94 revision at receipt time; P1 had not landed yet)
- `corpus/tools/support_check.py` sha256 `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`
- `corpus/fixtures/check_bible.py` sha256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`

## Step 1 — byte copies from fb118c4 (before modification)

```
$ git show fb118c4:corpus/fixtures/r94-paired-crossing/<f> > corpus/fixtures/r95-crossing-aftermath/<f>
$ for f in ...; do a=$(git show fb118c4:corpus/fixtures/r94-paired-crossing/$f | sha256sum | cut -d' ' -f1); b=$(sha256sum corpus/fixtures/r95-crossing-aftermath/$f | cut -d' ' -f1); ...
```

Observed: `SAME` for all eight files at copy time, including the three later modified.

| file | r94 sha256 (== copy sha256) |
|---|---|
| entities.json | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` |
| relations.json | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` |
| contradictions.json | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |
| inspiration-note.md | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` |
| source-excerpt.md | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` |
| sources.json | `2b627c4c166edf44e1e54bb006964a00e267ab4a4ce0b7b7c0681a0d9f0355d5` |
| timeline.json | `f0209f90a6ce795211369bd900ac1d333d16eb0af123f1b170831e192660533c` |
| fictional-excerpts.md | `585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2` |

Delivered (post-modification) sha256:

| file | delivered sha256 |
|---|---|
| entities.json | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` (unchanged) |
| relations.json | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` (unchanged) |
| contradictions.json | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` (unchanged) |
| inspiration-note.md | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` (unchanged) |
| source-excerpt.md | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` (unchanged) |
| sources.json | `fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a` |
| timeline.json | `3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177` |
| fictional-excerpts.md | `0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282` |

## Step 2 — modifications (diffs against fb118c4 r94 bytes)

`diff <(git show fb118c4:corpus/fixtures/r94-paired-crossing/sources.json) corpus/fixtures/r95-crossing-aftermath/sources.json`:

```
18a19,24
>   },
>   {
>     "id": "aru-aftermath-note",
>     "title": "Aru's Chalk Stair Aftermath Note",
>     "kind": "fictional first-person note",
>     "reliability_note": "Newly authored fictional note; Aru reports waiting at the Chalk Stair through the agreed bell and that Evin did not come. It records one crossing occasion only and is not evidence of a breach, a continuing duty, a perpetual obligation, or an external historical fact."
```

`diff` for `timeline.json`:

```
30a31,41
>   },
>   {
>     "id": "aftermath-missing-evin",
>     "tick": 11,
>     "entity_id": "aru",
>     "place_id": "chalk-stair",
>     "depends_on": [
>       "paired-crossing-decision"
>     ],
>     "description": "At the Chalk Stair at tick 11, Aru reports waiting through the agreed bell and that Evin did not come; the note scopes the agreement to this crossing only and asserts no other duty or breach.",
>     "source_id": "aru-aftermath-note"
```

`fictional-excerpts.md` — append only; r94's bytes preserved as a strict byte-prefix
(`cur[:1116] == git show fb118c4:...fictional-excerpts.md`, Python check → `True`;
r94 sha256 `585f4d07…f495c2`, r95 file now 1845 bytes). Appended text (lines 22–31):

```
## Round 95 aftermath note (2026-10-17)

Newly authored fictional first-person note, attributed to in-world source ID `aru-aftermath-note`, folio 5, lines 1–4. This section is appended after the preserved r94 text above; the inherited wording is unchanged.

> Tick 11: I waited at the Chalk Stair through the agreed bell.
> Evin did not come.
> The agreement we chalked covered this crossing only.
> I assert no other duty, no breach, and no obligation beyond this crossing.

Scope: this appended section is Aru's first-person report of one non-arrival at the Chalk Stair. It asserts no breach and no perpetual or continuing obligation; the crossing-scoped agreement above is unchanged, and the record supplies no other duty.
```

`diff` for the five byte-copy files: all report `identical` (no diff output).

## Step 3 — required gate: check_bible CLEAN

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

Control on the inherited fixture, same command shape:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

## Step 4 — structural checks (python3, values parsed from delivered files)

```
entities: r94=5 r95=5
  inherited rows value-identical: True
relations: r94=1 r95=1
  inherited rows value-identical: True
contradictions: r94=0 r95=0
  inherited rows value-identical: True
sources: r94=3 r95=4
  inherited rows value-identical: True
timeline: r94=3 r95=4
  inherited rows value-identical: True
source ids unique: True ['veil-verse', 'paired-clock', 'crossing-minute', 'aru-aftermath-note']
entity ids unique: True
new event: {"id": "aftermath-missing-evin", "tick": 11, "entity_id": "aru", "place_id": "chalk-stair", "depends_on": ["paired-crossing-decision"], "description": "At the Chalk Stair at tick 11, Aru reports waiting through the agreed bell and that Evin did not come; the note scopes the agreement to this crossing only and asserts no other duty or breach.", "source_id": "aru-aftermath-note"}
```

So: counts 5 entities / 1 relation / 3→4 events / 3→4 sources; no new claims, entities,
or relations (entities/relations/contradictions are byte-identical to r94); all 14
inherited rows are value-identical to their r94 counterparts.

## Step 5 — scope audit (no breach/perpetual assertion)

- `breach`, `perpetual`, `duty`, `obligation` occur only inside negating/scoping
  clauses ("is not evidence of a breach…", "asserts no other duty or breach",
  "I assert no other duty, no breach, and no obligation beyond this crossing",
  "no perpetual or continuing obligation").
- `alliance` 0 occurrences; `betray` 0 occurrences in the delivered excerpt file.
- Event `entity_id` is `aru` (schema has one actor slot); description is explicitly
  Aru's report ("Aru reports…") and the note's scope sentence carries the
  no-other-duty/no-breach bound. No claim that Evin was obligated beyond this crossing.
- `check_bible` double-booking check: `(aru, tick 11)` slot unique; no violation emitted.

## Step 6 — tool receipts (dependent on P4's map, which had not landed)

At 2026-10-17T16:19-03:00, `claim-excerpt-map.md` did not exist:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
FINDING map_missing: expected exactly one conventional claim-to-excerpt map
RESULT ERROR
exit=2

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
FAIL: claim-to-excerpt map not found
RESULT ERROR
exit=2
```

These are expected: the map is P4's artifact. Control with the r94 map and the same
working-tree tool:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS
exit=0
```

### Step 6b — after P4's map landed (poll result, 2026-10-17T16:21:17-03:00)

Bounded poll (20 s cadence) found `claim-excerpt-map.md` after 7 tries
(sha256 `30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a`).
Same tool revision (`map_obligations.py` still `cc1df4dc…`, the r94 revision — P1 had
not landed at this point), same commands:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
RESULT PASS
exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J14 (inherited rows; same anchors/lines as r94)
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
exit=0
```

(Full per-row output captured in the poll log; J01–J14 lines are byte-identical to the
r94 receipt quoted in Step 6, J15 is the new row anchored at my line 26.)

The exit-2 `map_missing` receipt in Step 6 is itself an independent live witness of the
`map_missing` finding class on a real unmapped cluster (relevant to C1/P2's persisted
`map_missing` self-test case).

### Step 6c — inherited map rows carried unchanged (cross-check of P4's map against r94's)

Parsed both maps' J-rows and compared cell-by-cell:

```
inherited rows byte-identical incl. namespace col: []
inherited rows identical ignoring namespace col: 14 ['J01'…'J14']
namespace-only differences: ['J01'…'J14']
```

Every inherited row differs only in column 4, the path-qualified source namespace
(`r94-paired-crossing:paired-clock` → `r95-crossing-aftermath:paired-clock`, and the
same for `crossing-minute`). Pointer, raw source ID, excerpt path, line span, mode, and
anchor are identical for all 14 inherited rows. The namespace cell is the fixture path
itself, so this is the documented cluster-local qualification convention, not a value
change. The new J15 row is `timeline.json#/3` (`tick`, `entity_id`, `place_id`,
`depends_on`, `description`, `source_id`), raw source `aru-aftermath-note`, span 22–31,
anchor `Tick 11: I waited at the Chalk Stair through the agreed bell.` — all pointing at
my delivered bytes.

## Interpretation flags (for verifiers)

1. Seat spec said the new source is "(kind note, required fields per schema, unique id)".
   I read "kind note" as the note kind with the fixture family's `fictional` disclosure
   prefix (r94: `fictional poem` / `fictional register` / `fictional minute`; corpus
   precedent `fictional first-person note`, 59 uses, incl. r87) and wrote
   `"kind": "fictional first-person note"`. If the criterion is a literal
   `"kind": "note"` string, this is a one-token divergence — flagged, not hidden.
2. The excerpt's "agreed bell" wording comes verbatim from the seat spec ("waited at
   the Chalk Stair through the agreed bell"); it is the minute's tick-10 agreement
   occasion, not a new object or entity (no entity/relation added).

## Facts P4/verifiers may need

- `fictional-excerpts.md` line map: heading 22; attribution line 24; quoted note lines
  26–29; scope paragraph 31. Inherited anchors keep their r94 line numbers (12–20)
  because the append starts after line 20.
- New JSON pointer candidates: `timeline.json#/3` (id `aftermath-missing-evin`),
  `sources.json#/3` (id `aru-aftermath-note`). Inherited pointers `#/0…#/2` and
  `entities.json#/0…#/4`, `relations.json#/0` are value-unchanged.
- `wc -c`: sources.json 1225 B, timeline.json 1254 B, fictional-excerpts.md 1845 B.
- P4's map sha256 at verification time: `30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a`.
- All receipts in Steps 6 and 6b ran against `map_obligations.py` sha256
  `cc1df4dc…bab790` (r94 revision) and `support_check.py` sha256 `55a5eb27…b442c`;
  `check_bible.py` sha256 `ff9fd2aa…d1421`.

### Step 6d — re-check under the delivered P1 tool (2026-10-17T16:22:30-03:00)

Polling for P1's landing succeeded after 2 tries: `corpus/tools/map_obligations.py`
sha256 became `c37f298b909150d1055a8ed8bdfb50258efda80da78213833dccb9ad239e9537`.
Same commands, no fixture change (my three modified-file hashes are unchanged):

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
RESULT PASS
exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
…
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS
exit=0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

Mid-wave transient observed and reported exactly (NOT a fixture or r95 finding): at the
same timestamp the persisted contract was still P2's predecessor,
`corpus/tools/map-obligations-contract.json` sha256 `349a1956…7a50` (20 cases), so

```
$ python3 corpus/tools/map_obligations.py --self-test
FINDING self_test_contract: contract self-test cases do not match the implemented cases
RESULT ERROR
exit=2
```

This is the expected P1-landed/P2-pending window: the new tool implements 22 cases while
the persisted contract still declares 20. It does not touch the r95 fixture receipts
above, which pass under the delivered tool. P2's contract landing should clear it;
re-check after P2 lands.

## Bottom line

PASS — all eight owned files delivered; required gate `check_bible` CLEAN exit 0
(5 entities / 1 relation / 0 contradictions / 4 events / 4 sources), inherited rows
value-identical, five byte-copy files byte-identical, r94 excerpt bytes preserved as a
strict byte-prefix; under both the r94 tool revision and the delivered P1 revision
(`c37f298b…9537`), `map_obligations` reports `OBLIGATIONS raw=15 mapped=15 RESULT PASS`
exit 0 and `support_check` reports `SOURCE-SUPPORT 15/15 … RESULT PASS` exit 0, with all
14 inherited rows identical to r94's (namespace column aside) and the new J15 anchored
at the delivered note line 26. Mid-wave transient `self_test_contract` exit 2 observed
at 16:22:34 (contract still 20 cases, P2 pending) — reported, not a fixture finding.
