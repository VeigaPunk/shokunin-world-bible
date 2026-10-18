# V12 — c2-whole-claim (round 95)

Seat: V12 `c2-whole-claim`. Scope per seat spec: independent manual whole-proposition
review of the C2 fixture — trace every proposition in the appended aftermath note to
exact excerpt clauses and to the event/source JSON rows; verify the scope discipline
holds (crossing-only; no other-duty, breach, perpetual-obligation, or identity
assertion anywhere in the new bytes); verify the description fields do not out-claim
the excerpt. Poll-wait for P3+P4 per protocol. Leaf seat: no nested agents, no commits,
no network, only this report written.

Baseline: r94 closure `fb118c4`. Working tree at seat start: `M LOG.md` +
`?? .ufo/waves/round-95/` only. All commands from repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin`.

## Poll-wait record (observed, 20 s cadence)

```
CHECK t=20s fixture_dir=absent p3=0 p4=0
CHECK t=40s fixture_dir=absent p3=0 p4=0
CHECK t=60s missing=[ README.md claim-excerpt-map.md] p3=[] p4=[]     # P3 preserving copy staged
CHECK t=80s..180s  missing=[ README.md claim-excerpt-map.md] p3=[] p4=[]   # P3 modified bytes landed ~t=100-140s
CHECK t=200s missing=[ README.md claim-excerpt-map.md] p3=[P3-fixture-json.md] p4=[]
CHECK t=240s missing=[ README.md claim-excerpt-map.md] p3=[P3-fixture-json.md] p4=[]
CHECK t=260s missing=[ README.md] p3=[P3-fixture-json.md] p4=[]        # P4 map landed
CHECK t=280s missing=[] p3=[P3-fixture-json.md] p4=[]                  # P4 README landed
CHECK t=320s missing=[] p3=[P3-fixture-json.md] p4=[P4-fixture-docs.md]
POLL_READY
```

No plan was verified; nothing was reviewed until the bytes existed. All 10 fixture
files plus both producer reports were present before the review below was finalized.

## Artifacts reviewed (frozen sha256, 2026-10-17 ~16:24 -03:00)

| File | sha256 |
|---|---|
| entities.json | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` |
| relations.json | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` |
| contradictions.json | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |
| inspiration-note.md | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` |
| source-excerpt.md | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` |
| sources.json | `fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a` |
| timeline.json | `3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177` |
| fictional-excerpts.md | `0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282` |
| README.md | `9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b` |
| claim-excerpt-map.md | `30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a` |

Producer reports read: `.ufo/waves/round-95/seats/P3-fixture-json.md`,
`.ufo/waves/round-95/seats/P4-fixture-docs.md`.

## 1. Inheritance integrity — byte copies and value identity

```
$ cd corpus/fixtures/r95-crossing-aftermath && sha256sum entities.json relations.json \
    contradictions.json inspiration-note.md source-excerpt.md
026af0bc…ae03b  entities.json
c279254b…a6ff9  relations.json
37517e5f…5b570  contradictions.json
58f5390e…82d37  inspiration-note.md
b5edc2fd…76d4cd source-excerpt.md
```

All five are byte-identical to `r94-paired-crossing/` originals (same `sha256sum` run
over `../r94-paired-crossing/<f>` → same digests). The three modified files are pure
additions against r94 (`diff` against the r94 originals):

```
18a19,24     (sources.json: one new source row appended)
30a31,41     (timeline.json: one new event row appended)
20a21,31     (fictional-excerpts.md: appended section, lines 21-31)
```

Inherited rows are value-identical (parsed JSON comparison):

```
entities.json r94: 5 r95: 5 inherited-value-identical: True
relations.json r94: 1 r95: 1 inherited-value-identical: True
contradictions.json r94: 0 r95: 0 inherited-value-identical: True
sources.json r94: 3 r95: 4 inherited-value-identical: True
timeline.json r94: 3 r95: 4 inherited-value-identical: True
new source rows: 1    new event rows: 1
event keys: ['depends_on','description','entity_id','id','place_id','source_id','tick']
source keys: ['id','kind','reliability_note','title']
```

The r94 excerpt text is an exact byte prefix of the r95 excerpt file:

```
r94 bytes: 1116 r95 bytes: 1845
r94 is exact prefix of r95: True
r94 sha256: 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2
r95 prefix sha256: 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2
```

So the preamble claim at `fictional-excerpts.md:24` ("This section is appended after
the preserved r94 text above; the inherited wording is unchanged.") is verified true,
and inherited map spans (lines 12-20) keep their line numbers.

## 2. Whole-proposition trace — appended aftermath note

The appended section (`fictional-excerpts.md:22-31`) contains four in-world quoted
propositions (lines 26-29) plus paratext (heading 22, attribution 24, scope 31). Every
proposition traced to excerpt clauses and to the JSON rows:

| # | Proposition (excerpt line) | JSON row/field it maps to | Trace verdict |
|---|---|---|---|
| N1 | "Tick 11: I waited at the Chalk Stair through the agreed bell." (26) | `timeline.json#/3`: `tick=11`, `place_id=chalk-stair`, `entity_id=aru` | literal "Tick 11", literal "at the Chalk Stair"; "I"=aru via source attribution (see O3); "the agreed bell" = new-source content (see O1) |
| N2 | "Evin did not come." (27) | `timeline.json#/3` `description` ("that Evin did not come"); `sources.json#/3` `reliability_note` ("that Evin did not come") | literal; recorded as a report of non-arrival, no breach wording anywhere |
| N3 | "The agreement we chalked covered this crossing only." (28) | `timeline.json#/3` `depends_on=["paired-crossing-decision"]` (editorial encoding of the reference + posteriority) | "crossing only" and "chalked" trace literally to inherited minute lines 19-20 ("for this crossing only", "chalked one temporary route mark"); "the agreement" = the tick-10 decision (see O2) |
| N4 | "I assert no other duty, no breach, and no obligation beyond this crossing." (29) | `timeline.json#/3` `description` ("asserts no other duty or breach"); `sources.json#/3` `reliability_note` | scope disclaimer, self-supported by the note's own text; echoed by README:11, map:51, excerpt scope line 31 |

Paratext checks: attribution line 24 "attributed to in-world source ID
`aru-aftermath-note`, folio 5, lines 1-4" — 4 quoted lines, ID matches
`sources.json#/3.id`; scope line 31 ("one non-arrival", "asserts no breach", "no
perpetual or continuing obligation", "the record supplies no other duty") traces to
lines 27-29 and adds no new assertion.

## 3. Description fields vs excerpt — no out-claiming

`timeline.json#/3.description` clause-by-clause against the excerpt:

| Description clause | Excerpt counterpart | Verdict |
|---|---|---|
| "At the Chalk Stair at tick 11" | L26 "Tick 11: … at the Chalk Stair" | exact |
| "Aru reports waiting through the agreed bell" | L26 "I waited … through the agreed bell" + attribution (Aru's note) | exact (adds only the attribution frame "reports") |
| "and that Evin did not come" | L27 | exact |
| "the note scopes the agreement to this crossing only" | L28 | exact |
| "and asserts no other duty or breach" | L29 | exact |

Every description clause has an excerpt counterpart; no clause lacks one.
`sources.json#/3.reliability_note` ("Aru reports waiting at the Chalk Stair through the
agreed bell and that Evin did not come. It records one crossing occasion only and is not
evidence of a breach, a continuing duty, a perpetual obligation, or an external
historical fact.") likewise restates L26-28 plus disclaimers; `title`/`kind`
("Aru's Chalk Stair Aftermath Note", "fictional first-person note") trace to the
attribution line and first-person voice. No description field out-claims the excerpt.

## 4. Scope-discipline audit (new bytes)

Command:

```
$ grep -n -i -E "duty|breach|perpetual|forever|always|standing|identity|alliance|betray|promise|obligat|continuing|verdict|canon" \
    README.md claim-excerpt-map.md sources.json timeline.json fictional-excerpts.md
```

All 18 hit lines classified by polarity (README.md:7,9,11,19,21,28;
claim-excerpt-map.md:1,3,16,40,49,51,53; sources.json:18,24; timeline.json:40;
fictional-excerpts.md:29,31):

- **other-duty**: "asserts no other duty or breach" (timeline:40), "no other duty, no
  breach" (excerpt:29), "no other duty" (excerpt:31), "asserts no other duty, no
  breach" (README:11), "no-other-duty/no-breach assertion" (map:51),
  "supplies no other duty" (map:51) — every one negated. "not evidence of a
  breach, a continuing duty" (sources:24) negated.
- **breach**: "no breach" (excerpt:29,31; README:11; map:51), "not evidence of a
  breach" (sources:24), "asserts no other duty or breach" (timeline:40, README:11) —
  all negated. No positive breach assertion anywhere.
- **perpetual/continuing obligation**: "no perpetual or continuing obligation"
  (excerpt:31), "a perpetual obligation" inside a "not evidence of" list (sources:24),
  "no continuing obligation" (README:11), "not perpetual performance" (map:49),
  "no continuing duty" (map:51) — all negated.
- **identity**: one occurrence, README:7 "does not imply a separate source, entity
  identity, or contradiction" — negated.
- **alliance**: "a standing alliance" in a "not evidence of" list (sources:18,
  inherited row), "not … alliance" (map:49) — negated.
- **verdict**: README:9 "does not … convert the non-arrival into a verdict",
  map:53 "not … a verdict on source authenticity" — negated/disclaimer.
- **canon**: README:19 "supplies no … fictional canon" negated; map:40 "do not … add
  canon" negated; README:21 and map:53 carry "canon review" inside "not …" disclaimers.
- Zero occurrences of `always`, `forever`, `promise`, `betray` in the new bytes.
- The only non-negated `obligation` hits are the technical term "map obligations"
  (README:21, map:3, map:16) — not in-world obligations.

**Crossing-only**: present in excerpt L28/L29, description, reliability_note,
README:11 ("the agreement covered this crossing only"), map:51 ("no obligation beyond
this crossing"). No byte asserts any duty, breach, obligation, or identity beyond the
single crossing occasion. Verdict: scope discipline holds in every new byte.

## 5. Tool receipts (commands + observed outputs)

Tool revisions at receipt time (recorded because P1 edits the tool concurrently):

```
$ sha256sum corpus/tools/map_obligations.py corpus/tools/support_check.py corpus/fixtures/check_bible.py
cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790  corpus/tools/map_obligations.py   # pre-P1 (r94 revision)
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
… PASS J01..J14 (inherited anchors, spans 12/13/17/18/19/20 unchanged) …
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> …
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> …
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
EXIT=0
```

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
RESULT PASS
EXIT=0
```

Controls at the same revisions: r94 `map_obligations` → `OBLIGATIONS raw=14 mapped=14`
`RESULT PASS` exit 0; r94 `check_bible` CLEAN exit 0. Re-run of `map_obligations` at a
later working-tree revision (`28d308be…`) again gave r95 15/15 PASS exit 0 and r94 14/14
PASS exit 0.

**Concurrent-edit observation (not attributed to any delivered revision):** during my
final probe (~16:23-16:24) the working-tree `map_obligations.py` was mid-edit by P1
(sha256 `74a88346…`, then `feea13c9…` at 16:24:03, size growing 32988→33241 B) and in
that transient state crashed on both clusters:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
Traceback (most recent call last):
  …
  File "…/map_obligations.py", line 418, in compare
    counts = Counter(pointer for pointer, _ in rows)
ValueError: too many values to unpack (expected 2, got 15)
EXIT=1
$ python3 corpus/tools/map_obligations.py --self-test
FINDING self_test_contract: contract self-test cases do not match the implemented cases
RESULT ERROR
```

This is in-flight producer state; the C2 fixture receipts above were taken at stable
revisions. Follow-up probe at ~16:25: the tool stabilized at `9224a684…` and runs the
fixture cleanly again —

```
$ sha256sum corpus/tools/map_obligations.py
9224a68410aea890e875a9ec55786dc009a22a442a36adc5eeb399a130e7bb70  corpus/tools/map_obligations.py
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS   (exit 0)
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS   (exit 0)
$ python3 corpus/tools/map_obligations.py --self-test
FINDING self_test_contract: contract self-test cases do not match the implemented cases
RESULT ERROR   (exit 2)
```

The `--self-test` contract mismatch at `9224a684…` is P1/P2's C1 work in flight
(contract cases not yet re-persisted), not a C2 artifact; the C1/C3 seats and the
integrator should re-take the `map_obligations` receipts at the frozen P1 revision.
This report does not judge C1.

## 6. Observations (non-blocking, for the round record)

- **O1 — "the agreed bell" presupposition (disclosed by P3, flag 2).** Excerpt L26
  "the agreed bell" references a bell agreement that no inherited clause records (the
  tick-10 minute records the stewardship agreement and the route mark, not a bell).
  Sole witness is the new note itself; no byte claims a prior source recorded it. It
  introduces no new entity/relation/claim, is declared by the C2 seat spec ("waited
  through the agreed bell"), and triggers none of the four banned assertion classes.
  Reported as a trace note, not a defect.
- **O2 — dependence-edge wording.** Map:49 / README:13 say the `depends_on` edges are
  "editorial encodings of the excerpts' explicit tick/order/dependence wording". At r94
  that was literally true for J14 ("Their tick-10 decision depends on both ninth-bell
  entries"). For J15 the note has no literal "depends on" clause; the edge encodes
  posteriority (tick 11 after 10) plus the note's reference to the chalked agreement
  (L28). Both files also state the edges are "editorial encodings … not literal JSON
  syntax", so this is a minor precision note on the word "explicit", not an out-claim.
- **O3 — actor identity of "I".** Anchor line 26 contains no "Aru" token; `entity_id:
  aru` traces through the source attribution (`sources.json#/3` title "Aru's Chalk
  Stair Aftermath Note", kind "fictional first-person note"; excerpt line 24
  "attributed to in-world source ID `aru-aftermath-note`"), consistent with the
  actor-slot convention disclosed at README:11 and map:51. Not an out-claim.
- **O4 — P3 kind flag verified.** P3 flagged `"kind": "fictional first-person note"`
  vs the seat spec's "(kind note …)". Corpus precedent confirmed: `grep -rh '"kind":
  "fictional first-person note"' corpus/fixtures/ | wc -l` → `60` rows (incl.
  r33-r37 fixtures). Disclosed divergence with precedent; not a C2 defect.

## 7. Cross-checks against producer reports

- P3's delivered hashes recomputed independently and match exactly
  (`sources.json fd9e30e8…`, `timeline.json 3c0faad6…`, `fictional-excerpts.md
  0ef6734a…`); P3's claimed counts (5/1/4 events, 4 sources), byte-copy claims, and
  check_bible receipt all reproduced.
- P4's claims reproduced: J01-J14 rows unchanged modulo path qualification (verified
  by `diff <(sed 's/r94-paired-crossing/r95-crossing-aftermath/g' r94 map) r95 map` —
  table rows J01-J14 show no differences; only title, scope counts, R9 table row,
  section intro, J15 row, and the normalization paragraph differ); span 22-31 is the
  appended section (append = lines 21-31; line 21 is the blank separator); J15 pointer
  `timeline.json#/3` correct.
- P4's report "Addendum — post-P1 re-run" is empty ("pending P1 landing") as of my
  read; that is P4's receipt to fill, not a C2 fixture defect.

## Bottom line

PASS — every proposition of the appended aftermath note traces to exact excerpt
clauses and the new event/source JSON rows; the crossing-only bound holds with every
duty/breach/perpetual/identity mention negated in the new bytes; description fields do
not out-claim the excerpt; inheritance is byte/value-exact; check_bible CLEAN exit 0,
support_check 15/15 + 2/2 PASS exit 0, map_obligations 15/15 PASS exit 0 at stable tool
revisions (O1-O4 are disclosed, non-blocking trace notes).
