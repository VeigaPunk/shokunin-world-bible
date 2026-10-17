# V36 — whole-claim-replica-2: aftermath note vs JSON rows (scope discipline + description fidelity)

Seat: V36, round 95, lane `lore-shokunin`. Scope of this seat: second independent
whole-claim replica review of the r95 aftermath note (`fictional-excerpts.md` quoted
note, lines 26–29) against the JSON rows that carry it, with two explicit obligations:
(1) verify scope discipline and description fidelity, and (2) explicitly try to
construct a reading where the note asserts a broader duty — reporting it as a finding
if constructible.

Target artifact revision reviewed (hashes match producer claims exactly):

```
$ md5sum corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md corpus/fixtures/r95-crossing-aftermath/README.md
a872889e86a10127750ba0647e4829ff  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
5ccf979d845c20d00ad34e8462ef3b90  corpus/fixtures/r95-crossing-aftermath/README.md
$ sha256sum corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  .../claim-excerpt-map.md
$ wc -c corpus/fixtures/r95-crossing-aftermath/{sources.json,timeline.json,fictional-excerpts.md}
1225 sources.json / 1254 timeline.json / 1845 fictional-excerpts.md
```

These equal the values quoted by P3 (`sha256 30281ff1…`, sizes 1225/1254/1845) and P4
(`map a872889e…`, `README 5ccf979d…`); the revision I reviewed is the delivered one.

Poll-wait: first check at 16:18 found the directory with only the five byte-copies
present; README/map/modified JSONs landed at 16:21 (`ALL PRESENT after 10 checks
(16:21:41)`). No ABSENT condition arose for this seat's targets.

## 1. Delivered text under review (verbatim, `nl -ba`)

```
26  > Tick 11: I waited at the Chalk Stair through the agreed bell.
27  > Evin did not come.
28  > The agreement we chalked covered this crossing only.
29  > I assert no other duty, no breach, and no obligation beyond this crossing.
31  Scope: this appended section is Aru's first-person report of one non-arrival at the
    Chalk Stair. It asserts no breach and no perpetual or continuing obligation; the
    crossing-scoped agreement above is unchanged, and the record supplies no other duty.
```

JSON row that carries it (`timeline.json#/3`, `timeline.json:33-42`):

```
id aftermath-missing-evin; tick 11; entity_id aru; place_id chalk-stair;
depends_on ["paired-crossing-decision"]; source_id aru-aftermath-note;
description "At the Chalk Stair at tick 11, Aru reports waiting through the agreed
bell and that Evin did not come; the note scopes the agreement to this crossing only
and asserts no other duty or breach."
```

Source row `sources.json#/3` (`aru-aftermath-note`) reliability note: "…Aru reports
waiting at the Chalk Stair through the agreed bell and that Evin did not come. It
records one crossing occasion only and is not evidence of a breach, a continuing duty,
a perpetual obligation, or an external historical fact."

## 2. Field-by-field description fidelity (note → JSON) — HOLDS

| JSON field | Note evidence | Verdict |
|---|---|---|
| `tick: 11` | L26 "Tick 11:" | exact |
| `place_id: chalk-stair` | L26 "at the Chalk Stair" | exact |
| `entity_id: aru` | first-person "I" under source ID `aru-aftermath-note`; single-actor-slot encoding disclosed (`claim-excerpt-map.md:51`, `README.md:11`) | exact, disclosed |
| `depends_on: ["paired-crossing-decision"]` | L28 "The agreement we chalked" refers to the tick-10 decision; declared editorial encoding of order/reference (`claim-excerpt-map.md:49`, `README.md:13`) | exact, disclosed |
| `source_id: aru-aftermath-note` | `sources.json#/3` exists; `check_bible` resolves all citations CLEAN | exact |
| description clause 1 "waiting through the agreed bell" | L26 | exact |
| description clause 2 "Evin did not come" | L27 | exact |
| description clause 3 "scopes the agreement to this crossing only" | L28 | exact |
| description clause 4 "asserts no other duty or breach" | L29 | faithful (see §4 note on "other") |

No field asserts more than the note says. Nothing in the fixture converts the
non-arrival into fault, breach, absence-as-world-fact, or identity inference;
`README.md:9` says so explicitly ("does not … convert the non-arrival into a verdict").

## 3. Scope discipline — HOLDS (mechanical scan + clause analysis)

Mechanical deontic scan over the four quoted note lines (python regex, this pass):
the only deontic tokens present are `duty` and `obligation`, both inside the negation
of L29; no `must/should/ought/required/bound/promise/pledge/swore/committed` occurs.
Scope words present: `crossing only`, `beyond this crossing`, `no other`. The note
contains no recurrence or duration marker (`always`, `forever`, `perpetual`,
`continuing`, `from now on`) in its own voice — every such term in the fixture appears
only in disclaiming prose (`sources.json:24`, `fictional-excerpts.md:31`,
`claim-excerpt-map.md:51`, `README.md:11`), each negating it.

Independent receipts on the delivered revision (run by this seat, from the lane root):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations        exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; …; VALIDATED-ROWS 17/17
RESULT PASS                                                        exit=0
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
RESULT PASS                                                        exit=0
```

Inheritance and census checks (this seat):

```
$ python3 -c 'json compare r94 vs r95'
timeline.json r94_n=3 r95_n=4 prefix_identical= True
sources.json  r94_n=3 r95_n=4 prefix_identical= True
entities.json r94_n=5 r95_n=5 prefix_identical= True
relations.json r94_n=1 r95_n=1 prefix_identical= True
contradictions.json r94_n=0 r95_n=0 prefix_identical= True
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s r94-paired-crossing/$f r95-crossing-aftermath/$f; done
IDENTICAL: all five
$ git ls-tree -d --name-only fb118c4 corpus/fixtures/ | wc -l   -> 168
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l   -> 169
$ comm -13 <baseline dirs> <now dirs>                            -> corpus/fixtures/r95-crossing-aftermath  (exactly one)
$ git diff --stat fb118c4
 LOG.md | 57 + ; corpus/tools/map_obligations.py | 121 +/5 -
$ git diff --stat fb118c4 -- corpus/fixtures/r94-paired-crossing corpus/tools/support_check.py corpus/fixtures/check_bible.py
(empty)
```

So: no new claims/entities/relations; 14 inherited rows carried unchanged; exactly one
new fixture directory; the r94 parent, `support_check.py` and `check_bible.py` are
untouched at the reviewed revision.

## 4. Explicit attempt to construct a broader-duty reading — constructed, but it fails as an assertion (NOT a finding)

I attacked the note with the strongest reading I could build. Five constructions were
tried; each fails, and the two that get closest are recorded as bounded ambiguities
rather than findings.

**(A) The strongest construction — the "agreed bell" referent gap.** L26 uses a
definite description, "the agreed bell", which presupposes that a bell was agreed. No
row in the fixture establishes a bell agreement: the inherited register has a bell that
is *held*, not agreed (`paired-clock`, "Evin held the south bell at Salt Court", tick 9),
and the inherited minute's agreement is "for this crossing only, to share stewardship"
with no bell term. A reader can therefore resolve "the agreed bell" to an agreement
*other* than "the agreement we chalked" — a separate bell agreement whose scope the
note never states. Under that resolution the note would carry a bell-derived
expectation that is not bounded by L28, i.e. the seed of a broader duty.
**Why it fails as an assertion:** L28 names the operative agreement ("the agreement we
chalked") and bounds it ("covered this crossing only"), and L29 negates the residue
("no other duty … no obligation beyond this crossing"). The construction only survives
by deleting L28–L29, i.e. by not reading the note. It is an unresolved referent, not an
asserted duty. Recorded below as a bounded ambiguity for a future round.

**(B) "no other duty" presupposition.** "No other duty" presupposes at least one duty
exists. That duty is supplied by the crossing-scoped stewardship agreement (within the
declared bound, carried unchanged from r94). No broader referent is needed or implied;
L28 immediately identifies the bound. Fails as a broader-duty reading.

**(C) Distributing "other" across "breach".** Parsing L29 as "no other duty, no *other*
breach…" would leave a within-crossing breach possible. That is *narrower* than the
natural parallel reading ("no breach" unqualified), not broader; it asserts no extra
duty. Worth one line of fidelity bookkeeping: the JSON description's "asserts no other
duty or breach" is the same shared-"other" phrasing, so the row summary is at most
slightly weaker than the note; the map (`:51`) and the scope paragraph (`:31`) state
the unqualified "asserts no breach", matching the note's natural reading. No over-claim
exists in either direction.

**(D) "Evin did not come" as implicit fault.** The juxtaposition of L26–L27 with an
agreement invites the *reader inference* that Evin failed a term. But the note asserts
only a non-arrival; it names no duty to attend, no fault, no verdict; and every
describing surface denies it (`README.md:9` "does not … convert the non-arrival into a
verdict"; `sources.json:24` "not evidence of a breach"). A reader inference that the
text explicitly declines to assert is not a note-asserted broader duty.

**(E) Recurring-bell reading of "through the agreed bell".** If the bell were a
recurring clock signal, waiting "through" it would imply a standing duty. The note never
says the bell recurs; the inherited register's bell is a one-tick entry; L28–L29 block
the standing reading. Fails.

**Result:** no reading survives in which the *note* (or any r95 JSON row describing it)
asserts a duty, obligation, or breach beyond this crossing. The round's C2 wording —
"crossing-only scope, no breach/other-duty assertion" — is accurate on the delivered
bytes.

## 5. Bounded observations (not failures; for later rounds / other seats)

1. **"the agreed bell" has no provenance row.** The note is a new in-world source, so
   introducing the bell is legitimate and is declared in C2; but no r95 file states
   which agreement established the bell or that it is a term of the chalked crossing
   agreement. A future round could name the bell's provenance in the note or map to
   close the referent gap identified in §4(A). This does not harm C2 as declared.
2. **Two span semantics coexist, both disclosed.** The R9 declaration row declares
   `fictional-excerpts.md:12-29` (first to last quoted line), while J15's own span is
   `22-31` (the whole appended section, heading through scope line); the anchor line 26
   lies inside both, and `claim-excerpt-map.md:51` discloses the J15 span choice
   explicitly. I independently corroborate V35's observation; it is
   declaration-granularity, not an anchor or fidelity miss.
3. **`entity_id: aru` with Evin named only in the description** is the schema's single
   actor slot; disclosed at `claim-excerpt-map.md:51` and `README.md:11` and not a
   silent exclusion of the second participant.
4. `map-obligations-self-test-rkkqvbmr/` appeared briefly as an untracked repo-root
   directory during the round and was gone by the final sweep (`git status --porcelain`
   final untracked set: `.ufo/waves/round-95/`, `corpus/fixtures/r95-crossing-aftermath/`,
   `corpus/knowledge/r95-aftermath-scope-note.md`). No stray artifact remains.

## 6. Limits of this seat

This is a same-lane replica review on the delivered bytes; it is lexical/structural
plus hand clause analysis, not source authentication, not canon truth, not rights or
permission review, and not an admission decision. P5's knowledge note
(`corpus/knowledge/r95-aftermath-scope-note.md`, present by 16:22) was read for
cross-consistency only; it is a producer artifact and its claims are not verified here
beyond the paths I re-ran. I wrote only this report file.

**Bottom line: PASS — the aftermath note's whole claim matches its JSON rows field-for-field, contains exactly two deontic tokens and both are negated, and every attempted broader-duty reading required deleting the note's own crossing-only bound and no-breach clause; the closest construction ("the agreed bell" referent gap) is a bounded ambiguity, not an asserted broader duty.**
