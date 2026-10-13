# Runnable lore bible example

From the repo root, run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions
```

The first command exits 0; the second exits 1 and prints **all three** seeded
violations. Round 2 adds a narrowly scoped pair:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/ally-reciprocal
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/ally-one-way
```

The reciprocal pair exits 0; the one-way pair exits 1 with a relation-local
missing-reciprocal message. Both fictional faction entities and each alliance
edge cite `harbor-compact`, an invented bilateral treaty record whose title
states the mutually attested convention. The one-way fixture deliberately omits
one record; the checker does not invent it. Only `allied_with` edges between two
distinct, existing factions trigger the reciprocal-record rule. A valid reverse
record needs its own resolvable in-world source ID. Self-edges, non-faction
endpoints, and unrelated relation types are outside this rule; dangling
endpoints remain subject to the original check. This is a chosen data
convention, not proof that every alliance is symmetric in canon.

No file is modified by the checker. An event's `tick` is a
nonnegative integer in this invented world's local sequence; it is not an
absolute date. Dependency event IDs must have strictly earlier ticks. A
character cannot occupy different places at the same tick; simultaneous
records at the same place are allowed. A contradiction is evidence requiring
editorial review, not permission for this checker to choose a canon answer.

`source_id` and `first_appearance` refer to `sources.json` **in-world fictional
records**; the reference ledger for real-world inspiration is separate. The
schema requires every entity claim, relation, and event to cite an in-world
source. Omit uncertain assertions rather than present them as uncited canon.
All entries here are invented for this fixture. Do not infer any real-world
historical facts from them.

## Round 3: explicit contradiction records

Every example bible now includes a required `contradictions.json` array; bibles
with no asserted pair use `[]`. Omission is an input error, not evidence that
there are no contradictions. Each entry has a unique `id`, two references
`claim_a` and `claim_b` of the form `{ "event_id": "...", "field": "..." }`,
and nonempty `why`. Allowed fields are `place_id`, `tick`, `depends_on` in an
existing uniquely identified timeline event with a resolvable in-world
`source_id`. The event's own source is the citation for that assertion; the
ledger does not copy a source, text, or paraphrase that could disagree with it.
The checker validates pointers and required text, not the truth of citations
or whether `why` accurately explains a semantic contradiction.

The original `contradictions/contradictions.json` preserves two pairs: the
arrival versus false-sighting places, and the arrival dependency on later versus
the later event's tick. The dangling `missing-map` endpoint has no second
cited assertion, so remains an ordinary checker diagnostic **outside** the
two-sided ledger. A malformed reference sibling demonstrates a ledger-local
error while retaining all original records:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions-ledger-malformed
```

The valid contradictory fixture still exits 1 on the same original three
violations; the malformed sibling exits 1 with those three plus a ledger-local
unknown-event violation. Neither command chooses an in-world winner, edits
canon, or verifies game mechanics.

## Round 4 rejected experiment (not active checker behavior)

The exact-name detector and paired inputs are archived under
`../live/rejected-r4/`; the observed CLI output is preserved under
`../live/runs/20261012T163450Z/`. The experiment distinguished exact equal
strings, but wrongly emitted a hard `VIOLATION` / exit 1 for legitimate
homonyms. It was rejected for calibration harm and the active checker restored
to round 3. These archived inputs are **not** active fixtures. See
`../../LOG.md` round-4 closure and `../../reports/r4-axis-adjudicator.md`.

## Round 5: measured malformed-input matrix

The five `r5-*` directories each copy the clean five-table bible and change
only one file or field. From the repo root, run the checker against each
`r5-missing-file`, `r5-invalid-json`, `r5-wrong-top-level`, `r5-row-shape`, and
`r5-invalid-citation` directory with the command form above. The clean
`consistent` bible is the control. The observed exit codes, diagnostic classes,
exact mutation list and limits are in
`../knowledge/2026-10-12-malformed-error-patterns.md`; full stdout and exit
status are under `../live/runs/20261012T164316Z/`. These bibles exercise
input handling, not new checker behavior or canon truth. Do not treat the
absence of cascaded errors in these deliberately low-cascade probes as a
promise about other malformed files.

## Round 6: explicit item provenance chain

The two `item-chain-*` bibles copy `consistent/` and add an optional
`provenance` list only to item `seal`. Its first record is a source-cited
acquisition (null `from_holder`, `mira` as initial holder, tick 0). Later
records explicitly transfer it to `harbor` at tick 3 and `tower` at tick 4.
The valid and broken fixtures differ only at the last transfer's
`from_holder`: valid `harbor`; broken `mira`. Run from repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/item-chain-valid
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/item-chain-broken
```

The first should exit 0; the second reports the last record's chain break
without changing either cited assertion. Missing `provenance` on other items
means no chain is asserted, not a failed provenance check. A present malformed
list, ambiguous duplicate IDs, or equal/reversed ticks are not silently
interpreted as a valid chain. Tick order is local to these explicit records,
not linked automatically to timeline events. Holder IDs are entity IDs; their
kind need not mean legal ownership. A citation resolves to an invented in-world
record, but the checker does not inspect its text or prove a transfer happened.
No history is inferred from `carries`, entity claims, timeline descriptions,
or game mechanics; missing transfers do not prove an item was stationary.

## Round 7: duplicate source IDs are ambiguous, not qualifying citations

A source ID is a usable citation witness only if exactly one valid row in
`sources.json` has that ID. An absent ID remains `unknown`; a repeated ID
retains the global duplicate-ID violation **and** gets a local `ambiguous
in-world source` report at each reference. Both source rows remain untouched;
array order does not choose one. This checks ID identity only, not whether
the cited fictional record supports an assertion.

Run the isolated new cases:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r7-item-ambiguous
```

The first has a uniquely cited forward faction alliance but a reverse edge
whose `harbor-compact` ID appears twice; it reports duplicate ID, local
ambiguous reverse citation, and a missing **qualified** reciprocal. The
second copies the valid item chain but duplicates cited `archive-ledger`; it
reports duplicate ID and affected local first-appearance/claim/provenance
citations. A structural holder-chain finding (if any) refers to input fields,
not sourced canon when citations are ambiguous. Old unique-source fixtures
remain unchanged. Multiple local reports are intentional and do not imply
multiple underlying duplicate IDs. No source is selected or rewritten.

## Round 8: dependency-list integrity

`r8-deps-distinct/` and `r8-deps-anomalous/` are fictional copies of the
consistent bible. Only `timeline[1].depends_on` differs: `['departure']` in
the control and `['departure', 'departure', 'arrival']` in the anomaly. Both
event rows keep their in-world `courier-log` source ID. Run from the repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r8-deps-distinct
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r8-deps-anomalous
```

The repeated earlier `departure` is an input-list duplicate that the old
checker accepted; the explicit self `arrival` is a list anomaly and also
retains the existing equal-tick inversion diagnostic. Each repeated
occurrence is reported locally; the checker does not remove an entry or
interpret causal truth. Existing unknown-ID/tick checks apply once to each
distinct dependency ID so repeated entries do not duplicate the same lookup
error. The event's cited source ID is checked for uniqueness, not for
textual support of the dependency claim. Duplicate timeline event IDs remain
an ambiguity outside this round's rule; no graph-cycle or game-mechanics
verification is claimed.

## Round 9: ambiguous prerequisite event IDs

`r9-dup-low-high/` and `r9-dup-high-low/` contain the same three
fictional timeline event records; only the order of the two `same` target
rows (ticks 1 and 5) changes. `consumer` at tick 3 depends on `same`.
`r9-unique-control/` retains one tick-1 target and the same consumer. Run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r9-dup-low-high
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r9-dup-high-low
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r9-unique-control
```

A prerequisite ID resolves only when exactly one schema-valid timeline
event has that ID. An absent ID keeps its unknown-event report; multiple
matching events get a local ambiguous-dependency report and **no tick
comparison** for that reference. Both duplicate event rows and their
duplicate-ID finding remain; array order does not choose a canonical target.
Unique targets retain the strict-earlier rule. Every event cites the
fictional `courier-log` ID, which is checked for unique identity, not
source-text support for an event or dependency. This does not establish
causal truth, a graph cycle, or game mechanics.

## Round 10: a bounded second account of the departure

`r10-registry-witness/` copies the five `consistent/` JSON tables, retaining
all original rows, and adds one source, one character, one relation, and one
timeline event. Its `registrar-copy-excerpt.md` is **invented fictional in-world
text**, not recovered evidence. Run from the repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r10-registry-witness
```

The excerpt says Sella, a registrar at Lantern Harbor, recorded seeing Mira
leave at first bell. At Mira's request, Sella left the registry destination
blank and kept the carbon. The new entity claim, `records_departure` relation,
and `registry-entry` event cite `registrar-copy` and correspond to those
clauses. The private `courier-log` route remains separately cited and
unchanged. The blank public destination does **not** assert a different
destination or settle whether Sella's report is true. Both the new entry
and departure are assigned local tick 1 as an authoring convention, not proof
of exact simultaneity, within-tick ordering, or a conversion from `first bell`;
no dependency joins equal ticks.
The clean checker result validates structure and citation-ID resolution only.
A reader must compare excerpt wording with claims; even that comparison does
not establish independent corroboration, witness honesty, or canon truth.

## Round 11: ambiguous place entity IDs

The fictional `r11-place-character/` and `r11-character-place/` fixtures
copy the clean bible and add a second schema-valid entity row with ID
`harbor` but kind `character`. Only the order of the `harbor` place and
character rows differs. `r11-unique-nonplace/` changes the departure's
`place_id` to the unique character `mira`; `r11-dangling-place/` changes it
to missing `unlisted`. The original `consistent/` is the unique-place control.
From the repo root run the checker on each fixture directory:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-place-character
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-character-place
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-unique-nonplace
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-dangling-place
```

When a timeline `place_id` names more than one **schema-valid** entity row,
the checker reports an ambiguous place entity at that field and retains the
duplicate-entity-ID finding, rather than choosing a kind from the last row.
For exactly one target it still checks `kind == place`; an absent ID keeps
its dangling-reference report. This does not change relation endpoints,
actor identity or occupancy rules, resolve duplicate entities, reject equal
display names, or prove the source text supports either entity record.

## Round 12: uncertain actor identity in occupancy reports

`r12-unique-actor/` and `r12-ambiguous-actor/` both describe two distinct
event records for actor ID `mira` at tick 7, one at `harbor` and one at
`tower`. The second fixture differs only by adding a schema-valid, cited
entity row that **reuses** ID `mira`; this is input identity ambiguity, not
evidence of a second canon Mira. Run from the repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-unique-actor
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-ambiguous-actor
```

The unique actor triggers the existing definite same-actor `double-booked`
rule. If multiple schema-valid entity rows share the actor ID, each affected
timeline row instead gets an `ambiguous actor entity` finding and no
**definite** occupancy inference. The raw event rows and duplicate-ID
finding stay. This does not show that the events refer to different actors
or that an occupancy conflict is impossible: the duplicate rows might also
describe one actor. Dangling actor IDs retain older output in this round,
including a possible `double-booked` message; that separate known limitation
is not evidence of one real actor. Unique in-world citation IDs resolve
source identity only, not actor identity or source-text/canon truth.

## Round 13: absent actor ID in occupancy

`r13-missing-actor/` and `r13-unique-actor/` copy the round-12 unique-actor
fixture with the same two tick-7 event records and valid place/source IDs.
Only their `entity_id` fields differ: `unlisted` resolves to no entity row;
`mira` resolves to one. Run from the repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r13-missing-actor
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r13-unique-actor
```

A missing actor keeps a dangling finding at each event but does not enter
the definite same-actor occupancy comparison. This means its possible
conflict is **unassessed**, not disproven. One identified actor still gets
`double-booked` at two places on one tick; multiple matching rows retain
round-12 `ambiguous actor entity` findings. Entity-ID counts use rows that
pass the checker’s required-field shape gate, not an independently proven
character identity: a string `kind` outside the allowed kinds still counts
and is separately flagged. Raw events and in-world citations remain; source
ID resolution does not prove actor identity or either event’s truth.

## Round 15: Sella's later carbon note

`r15-carbon-followup/` is a separate fictional micro-bible copied from
`r10-registry-witness/`: all old JSON rows and the original registrar excerpt
remain intact. It adds the invented `sella-carbon-followup` private note and
one Sella event at local tick 3 depending on `registry-entry` (tick 1). Run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r15-carbon-followup
```

In the **newly authored, not recovered** excerpt, Sella reports looking
again at the carbon she kept, seeing a blurred blue oval mark, and not
knowing its origin. She expressly does **not** attribute the mark to Mira's
Blue Seal. The text does not say who made the mark, when it appeared, why
Sella looked again, whether it indicates a destination, or whether the
account is true. Its blue appearance alone is not seal provenance. Tick 3
and the dependency express author-chosen later ordering, not an elapsed
interval, first-bell conversion, or causal link to Mira's arrival. The clean
checker result validates schema/IDs and stated local timeline rules only;
manual comparison of excerpt and event wording establishes internal
correspondence, not independent corroboration or canon.

## Round 16: absent place IDs and occupancy certainty

`r16-valid-places/` has one uniquely identified `mira` at tick 7 in
`harbor` and `tower`; `r16-missing-place/` changes only the second
`place_id` to missing `unlisted`; `r16-missing-first/` puts missing place
in the first event. `r16-mixed-three/` has known `harbor`, missing
`unlisted`, then known `tower` on the same actor/tick. Run from repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r16-valid-places
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r16-missing-place
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r16-missing-first
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r16-mixed-three
```

An absent place ID retains its dangling finding and event row but cannot
participate in a **definite different resolved places** occupancy comparison.
The known harbor/tower pair still double-books, even with a missing row
between them. Skipping the unresolved row means the possible conflict is
not assessed, not disproven. This round does not change existing behavior
for duplicate place IDs or unique non-place entities, which have separate
diagnostics but may still enter raw-ID occupancy comparisons; it does not
claim a general place-identity resolver or source-text/canon truth.

## Round 17: unique wrong-kind place IDs and occupancy certainty

`r17-valid-places/` and `r17-wrong-after/` are a paired input: only
second-row `place_id` differs (`tower` versus `mira`, an indexed
`character`). `r17-wrong-before/` puts the wrong-kind row first.
`r17-wrong-{first,middle,last}/` place it before, between, or after
the distinct known `harbor` and `tower` rows. Run, for example:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r17-valid-places
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r17-wrong-after
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r17-wrong-first
```

A uniquely indexed non-place entity remains a `not a place` finding but
is not a resolved place for a **definite different resolved places**
occupancy comparison. The known harbor/tower pair remains reportable
in the three tested orders. Each fixture description is about the input
row, not an assertion from `courier-log`. Withholding a finding involving
`mira` as a place does not prove its actual location or absence of a
conflict. Count-zero missing IDs retain round-16 behavior; duplicate or
ambiguous place IDs still have their old raw-ID occupancy behavior.
The checker does not establish source-text support or canon.

## Round 18: ambiguous place IDs and occupancy certainty

`r18-unique-pair/` has one uniquely indexed `harbor` and one `tower`
row for uniquely indexed actor `mira` at tick 9. `r18-duplicate-pair/`
differs only by an additional complete place entity with ID `harbor`;
`r18-duplicate-reverse/` reverses event order. `r18-mixed-kind/` duplicates
that ID with a character instead. `r18-known-through-ambiguous/` and
`r18-duplicate-first-known/` use fixture-only uniquely indexed `quay`
to check the known tower/quay pair with ambiguous harbor between or first.
Run from repo root, for example:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r18-unique-pair
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r18-duplicate-pair
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r18-known-through-ambiguous
```

The duplicate-ID and ambiguous-place findings remain. An ambiguously
indexed `place_id` neither compares nor enters a **definite different
uniquely resolved places** occupied slot; the known tower/quay pair
still yields its own finding in these tested orders. Count-zero IDs and
unique wrong-kind IDs retain rounds 16 and 17 behavior. Fixture event
descriptions describe input fields only. The extra `quay` and duplicate
entity are test rows, not attested fictional facts; `source_id` identity
does not attest them. Exclusion leaves any actual conflict involving an
ambiguous row unassessed, not disproved, and the checker does not
establish source-text support or canon.

## Round 19: negative timeline ticks and occupancy certainty

`r19-valid-tick/` and `r19-negative-tick/` differ only in both
`timeline.tick` values (`9` versus `-1`), with a unique actor and
two uniquely indexed places. `r19-valid-around-negative/` has
valid/invalid/valid ticks `9,-1,9` with known distinct valid places;
`r19-negative-first-valid/` has invalid/valid/valid ticks `-1,9,9`.
Run from repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r19-valid-tick
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r19-negative-tick
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r19-valid-around-negative
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r19-negative-first-valid
```

A negative integer tick retains `must be nonnegative` and its raw
event row but does not compare/store occupied slots. Distinct known
places at nonnegative tick still report `double-booked` across an
invalid-time row in these orders. Only occupancy changes; dependency
inversion still uses raw admitted integer ticks. Bool/float ticks fail
the earlier exact-`int` required-field screen and are not examples of
this rule. The suppressed negative-time comparison is unassessed, not
proof the events could not occur or conflict. Fixture descriptions
are input-scoped, not source testimony; no source-text/canon claim.

## Round 20: invalid negative tick in dependency ordering

`r20-valid-order/` uses prerequisite/dependent ticks `0,1`;
`r20-negative-dependent/` differs only in dependent tick `-1`.
`r20-negative-prereq/` differs from valid order only in prerequisite
tick `-1`. `r20-valid-inversion/` (`2,1`) and `r20-valid-equal/`
(`1,1`) preserve nonnegative ordering findings; `r20-both-negative/`
retains both tick diagnostics. `r20-mixed-edges/` tests an invalid
prerequisite edge and a separate valid-to-valid inversion on one row.
Run from repo root, for example:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r20-negative-dependent
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r20-negative-prereq
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r20-valid-inversion
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r20-mixed-edges
```

An indexed negative integer tick retains its invalid-tick finding
and event/dependency references, but no **definite timeline inversion**
comparison is made on an edge with either endpoint negative. Other
dependency-ID diagnostics (self, repeated, unknown, ambiguous) are
unchanged; each valid-to-valid edge still compares independently. The
valid-equal fixture also has a separate same-tick occupancy finding;
this round changes neither occupancy nor global tick schema. Withheld
ordering is unassessed, not proof a dependency is satisfied, absent, or
canonically false. Fixture descriptions describe input fields, not
source testimony; citation IDs do not prove chronology or event truth.

## Round 21: malformed dependency member must not mask occupancy

`r21-clean/` and `r21-malformed/` differ only in second-row
`depends_on` (`[]` versus `[null]`). Both rows otherwise have one
resolved actor, distinct uniquely indexed places and tick 9. The
`r21-*-reverse/` pair reverses place order; `r21-same-place/`,
`r21-invalid-tick/`, `r21-wrong-kind-place/`, and
`r21-ambiguous-actor/` test that malformed-list recovery does not
weaken occupancy's certainty guards. Run from repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r21-clean
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r21-malformed
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r21-malformed-reverse
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r21-invalid-tick
```

A list containing a non-string dependency member still reports
`expected event-id strings`; **all** member-wise dependency processing
for that row is skipped. Independent occupied-slot comparison/store
continues under the same unique-actor, unique-place-kind, nonnegative
tick guards. The paired malformed input therefore retains the list
error and adds its known-place booking; same-place and ineligible
actor/place/time controls do not gain an unsupported booking. This is
checker-input coverage, not evidence that either fixture event or its
location is source-attested or canon.

## Round 22: string dependencies beside malformed members

`r22-clean-inversion/` has one string edge (`r20-prereq` tick 2
to `r20-dependent` tick 1). `r22-mixed-last/` differs only by adding
`null`; `r22-mixed-first/` reverses member order.
`r22-multiple-invalid/` includes `null`, an object and an array before
a valid string edge; `r22-unknown-mixed/` and `r22-self-repeated/`
check existing string-ID findings. `r22-valid-order/` remains clean
and `r22-malformed-only/` has no string edge to inspect. Run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r22-clean-inversion
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r22-mixed-last
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r22-multiple-invalid
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r22-self-repeated
```

Any non-string member retains **one row-level** `expected event-id
strings` diagnostic before member findings. Each non-string is skipped
before ID/set lookup; string siblings are inspected in input order
under existing self/repeated/unknown/ambiguous/tick-valid inversion
rules. Neither malformed-member coercion nor a claim that its edge is
satisfied is made. Occupancy remains independent. These are fixture
inputs, not quoted chronology from `courier-log`; citation identity
does not establish event truth or canon.

## Round 23: witnessed-absence note class

`r23-note-class/` is a separate fictional micro-bible. Sella reports that
she looked for Mira’s outbound route strip on the registry hook rack at
Lantern Harbor and did not find it. That is a witnessed-absence note:
a named speaker reports a named thing was not present. It is not the
r15 mark observation. The clause map is
`r23-note-class/witnessed-absence-clause-map.md`. The checker does not
read that file. Run from repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r23-note-class
```

Clean output means schema, citations, relations, and timeline structure
only. It does not mean the absence report is true, that the strip never
existed, or that the note says anything about Mira’s Blue Seal.

## Round 24: ambiguous relation endpoint IDs

A relation endpoint names an entity ID, not a chosen row. The checker reports
`relations[i].from` or `.to: ambiguous entity` when that ID occurs in more
than one structurally admitted entity row. It retains the existing duplicate
entity-ID finding; it does not select the first or last row or adjudicate
which cited claim is true. The same endpoint has exactly one of these input
outcomes:

| Matching admitted entity rows | Endpoint finding |
|---|---|
| 0 | `dangling entity` (existing) |
| 1 | None |
| More than 1 | `ambiguous entity` at the relation endpoint |

Run `r12-ambiguous-actor` and `r12-unique-actor` with the checker command
above. Their `relations.json` records cite the fictional `courier-log`; the
ambiguous fixture duplicates `mira`, which the `from` endpoint names. The
unique control does not. This tests identifier resolution, not whether the
source text supports the relation. No real-world reference or rights claim
is involved.

## Round 25: separate `to`-endpoint probe

`r25-to-unique/` is a byte-for-byte copy of the five `consistent/` JSON
tables. `r25-to-ambiguous/` differs only by one extra structurally admitted
`seal` item row in `entities.json`, whose `first_appearance` cites the local
fictional `courier-log` source and whose `claims` list is empty. Both retain
identical cited `mira -> seal` relations; the extra row tests ID collision,
not a second established seal or an endorsed relation. Run from repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-ambiguous
```

The unique control exits 0. The ambiguous input reports the duplicate entity
ID and a `relations[0].to` ambiguity, while its `from` endpoint stays unique.
The checker does not select a row, verify story text, or resolve canon.

## Round 26: malformed duplicate target is not an admitted target

`r26-to-malformed/` copies `r25-to-ambiguous/` and changes only the
second raw `seal` row's required `name` value to `""`. The checker reports
`entities[4].name: required nonempty str`, screens that row out of its
admitted entity set, and therefore does **not** report a duplicate admitted
ID or ambiguous `relations[0].to`. Contrast the unmodified admitted-duplicate
fixture and the clean unique-target control:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r26-to-malformed
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-ambiguous
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-unique
```

The malformed raw row remains present and invalid. No endpoint-ambiguity
finding is a statement about **schema-admitted rows only**, not a finding
that the world contains one seal, that the rejected row is false, or that
`courier-log` supports either claim. No canon is resolved.

## Round 27: two ambiguous endpoints of the same relation

`r27-target-only/` copies the admitted duplicate-`seal` case.
`r27-both-ambiguous/` adds only one admitted duplicate `mira` entity row
with a locally resolvable fictional `courier-log` first-appearance ID and
no claims. Both keep the same cited `mira -> seal` relation and all other
tables unchanged. Compare them with:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r27-target-only
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r27-both-ambiguous
```

The both case reports `relations[0].from` and `relations[0].to` ambiguity
for that **one** relation. It also reports both duplicate IDs and two
independent timeline actor-ambiguity findings because existing events name
`mira`. Those findings are retained, not silently resolved. The target-only
control retains only the relation `to` ambiguity. None of these diagnostics
proves the relation or either duplicated row is true or canonical; the
checker does not choose an entity row.

## Round 28: constructed courier-log clause map

`r28-courier-excerpt/` copies all five `consistent/` JSON tables and adds
`courier-log-excerpt.md` and `relation-clause-map.md`. The first is a **newly
authored fictional** one-sentence excerpt, “I, Mira, carried the blue seal.”
The second manually maps only the sentence's carrying action to the existing
`relations[0]` `carries` relation. Matching the named speaker and object to
IDs `mira` and `seal` is a fixture-local editorial choice, not a conclusion
from the sentence alone. The near-miss “the seal was near Mira” would not
support `carries`. Other entity claims and timeline events copied from the
clean fixture remain outside this excerpt's support. Run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt
```

Exit 0 establishes only existing schema/citation-reference consistency.
The checker never reads the Markdown and cannot establish prose support,
source authenticity, carrying truth, ownership, chronology, or canon.

## Round 29: clean structure is not prose support

`r29-near-miss/` preserves all five `r28-courier-excerpt/` JSON tables
byte-for-byte. Its newly authored fictional excerpt instead says “The blue
seal was near Mira.” The manual `negative-clause-map.md` marks only
`relations[0].type=carries` **unsupported by this excerpt**: proximity
does not entail carrying. It does not mark the unchanged relation false
or contradicted. The names-to-IDs match remains a fixture-local editorial
choice. Compare the two clauses and structural runs:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r29-near-miss
```

Both exit 0 because the checker only reads JSON and does not inspect prose.
A human clause check accepts the r28 lexical `carried` conditional on the
editorial ID alignments and rejects r29 proximity as support for `carries`;
neither result authenticates a source or decides canon. Other JSON claims
are unassessed by these two sentences.

## Round 30: explicit textual conflict is not canon falsity

`r30-explicit-negation/` copies the five JSON tables from the r28 positive
and r29 proximity fixtures byte-for-byte. Its newly authored fictional
excerpt says “I, Mira, did not carry the blue seal.” The manual
`textual-conflict-map.md` labels a conflict with only the unchanged
`relations[0].type=carries` claim, **conditional** on editorial Mira/seal
ID matching and the same proposition/occasion. It neither resolves the
record nor says Mira never carried the seal. Compare all three:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r29-near-miss
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r30-explicit-negation
```

All exit 0 structurally because the checker ignores Markdown. A human
clause check distinguishes conditional lexical support (`carried`), no
support but no denial (`near`), and an explicitly negated clause (`did not
carry`) in this constructed text. None of these judges source authenticity,
world truth, canon, or other copied JSON facts.

## Round 31: ambiguous source ID on a `carries` relation

`r31-source-unique/` copies the five JSON tables from `consistent/`.
`r31-source-ambiguous/` adds only one admitted `sources.json` row reusing
`courier-log`; its other four tables, including `mira -> seal / carries`,
are unchanged. Run both:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r31-source-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r31-source-ambiguous
```

The unique control exits 0. The ambiguous input reports **eight** input
findings: duplicate source ID, four entity citation references, one
`relations[0].source_id` ambiguity, and two timeline citation references.
This is a controlled *non-alliance relation* case.
`r7-ally-reverse-ambiguous/` already tests a reverse `allied_with`
relation with an ambiguous source ID; this round neither invents a new
checker rule nor claims to be the first ambiguous relation citation.
Duplicated in-world IDs do not establish whether source prose supports
`carries`, whether the relation is true or false, or any real-world rights
or AI-training permission. No canon is resolved.

## Round 32: malformed duplicate source row is still raw input

`r32-source-malformed/` copies `r31-source-ambiguous/` and changes only
the **second** raw `courier-log` source row's required `title` value to
`""`. Its `id` is still `courier-log`; all other fields and the four
non-source JSON tables are unchanged. Compare:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r32-source-malformed
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r31-source-ambiguous
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r31-source-unique
```

The malformed case exits 1 with `sources[2].title: required nonempty str`
only: this checker excludes the invalid raw row before indexing admitted
source IDs and resolving citations. The admitted duplicate still produces
one duplicate-ID plus seven ambiguous references; the unique control is
clean. Lack of reference-ambiguity findings in the malformed case does **not**
make the raw row disappear or prove unique in-world evidence, source truth,
canon, real-world rights, or AI-training permission.

## Round 33: Tarin's reported placement observation

`r33-tarin-envelope/` copies the clean five-table bible and appends one
fictional source `tarin-note`, two cited character rows (`tarin`, `sella`),
and a source-cited event in which **Tarin reports seeing** Sella place an
unlabeled paper envelope on the Lantern Harbor registry desk. The separate
newly authored `tarin-note-excerpt.md` gives that single first-person
sentence; `clause-map.md` maps speaker, participant, action, object and
location by hand. Names-to-IDs are fixture-local editorial alignments.
The new event's tick 3 is a local sequence label, not an observed time or
assertion of causation. Run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r33-tarin-envelope
```

A clean checker result establishes only structural and source-ID-reference
validity; it never reads the excerpt. This observation is distinct from
Sella's own registry entry in r10 and her non-finding report in r23. The
envelope is not identified as the carbon, route strip, Blue Seal, or a
carrier of any particular contents. No owner, recipient, motive, truth or
canon is inferred from the report.

## Round 34: hearing a report is not seeing the action

`r34-tarin-hearsay/` keeps all five r33 JSON tables byte-for-byte but
changes its newly authored fictional excerpt to “I, Tarin, heard that Sella
placed an unlabeled paper envelope on the Lantern Harbor registry desk.”
`modality-contrast-map.md` marks unchanged `reports seeing` character and
event text **unsupported by this excerpt as direct sight**. It supports only
Tarin's report of hearing a placement assertion; the informant, their
knowledge and the event's truth remain unknown. Compare:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r33-tarin-envelope
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r34-tarin-hearsay
```

Both exit 0 because the checker ignores prose and maps. A human reviewer
must distinguish r33's direct-sighting **report** from r34's hearsay
**report**. Neither proves the placement occurred, makes the unchanged
JSON canonically false, identifies envelope contents, or authenticates a
source. Names-to-IDs and event tick remain fixture-local choices.

## Round 35: two cited reports, one unresolved Bell-7 conflict

`r35-bell7-conflict/` derives from the r33 direct-sighting report. Its
newly authored Tarin excerpt says Tarin saw Sella place an unlabeled paper
envelope on the Lantern Harbor registry desk during Bell-7, claimed to be
the sole seventh-watch registry-bell sounding on the seventh day of
Embermonth, year 12. A separately authored
Sella excerpt names that same date/ringing and says she was physically at
North Tower throughout it and never at Lantern Harbor during it. The date
and unique-ringing status are claims in these fictional notes, not
authenticated chronology.
`manual-clause-pointer-map.md` maps both accounts and the editorial
`contradictions.json` pair: Tarin's `place_id` is the reported observation
scene, not a second actor=Sella event; Sella's `place_id` is her own
reported location. Under the stated identity, place and unique-occasion
assumptions, the accounts conflict as **reports**. Neither wins.

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r35-bell7-conflict
```

A clean result validates schema and resolvable pointers, not the semantic
conflict, source reliability or canon. Both source texts require manual
review. The equal local tick 3 is not a Bell-7 time conversion or proof of
external synchronization. Nothing identifies the envelope's contents,
owner, recipient, motive or any Blue Seal/carbon/route-strip connection.

## Round 36: wrong-date source near-miss

`r36-bell7-wrong-date/` copies the r35 fixture byte-for-byte except
that Sella's newly authored excerpt says the **eighth** rather than the
**seventh** day of Embermonth, year 12, and adds an editorial
`date-contrast-map.md`. All five JSON tables, including the Sella event
and contradiction rationale still claiming the seventh, remain identical.
Tarin's excerpt still says the seventh. Sella's retained “that same Bell-7
ringing” conflicts with her explicit eighth-day clause; the source texts
do not establish a shared unique occasion. That is a prose/record mismatch,
not a finding that either report or the JSON is canonically false.

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r35-bell7-conflict
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r36-bell7-wrong-date
```

Both should exit 0 because the checker reads JSON, not excerpts or maps.
A human must decline r35's conditional same-ringing conflict **from the
r36 source pair**; neither matching tick 3, valid citation IDs nor ledger
`why` settles the date, truth, source authenticity or canon.

## Round 37: ambiguous contradiction-ledger endpoint

`r37-ledger-unique/` is a byte-identical copy of r35's Bell-7 fixture.
`r37-ledger-ambiguous/` differs only by appending a second, identical
`tarin-envelope-observation` timeline row at index 4; the existing
`bell7-location-reports` ledger still points `claim_a` at that event ID
and `claim_b` at the unique `sella-bell7-presence` ID. Run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r37-ledger-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r37-ledger-ambiguous
```

The control exits 0. The duplicate exits 1 with a timeline duplicate-ID
finding **and** a ledger-local `claim_a.event_id` exact-one finding; `claim_b`
remains uniquely resolved. This exercises the ledger count guard, not a new
checker rule: r9 already covers generic duplicate timeline IDs. A duplicated
input ID cannot select which event assertion `claim_a` means. Neither this
error nor a clean control settles the two attributed reports, authenticates
sources, tests their prose or chooses canon. The Harbor pointer remains
Tarin's reported sighting scene, not a second Sella-actor occupancy row.

## Round 38: rejected source-ambiguity experiment (not active fixtures)

The proposed `r38-ledger-source-{unique,ambiguous}/` pair is archived at
`../live/rejected-r38/`, not in this active fixture directory. The unique
case copies r35; the negative appends a second row with the
`sella-bell7-note` source ID. From the repo root, inspect the archived
experiment with:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/rejected-r38/r38-ledger-source-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/live/rejected-r38/r38-ledger-source-ambiguous
```

The control exits 0; the negative exits 1 with duplicate source-ID,
ledger `claim_b.source_id`, and `timeline[3].source_id` ambiguity findings.
The experiment is reproducible, but **not an admitted coverage gain**:
round 7's independent reviewer already exercised the same ledger source-
ambiguity branch in a temporary `claim_a` probe. Opposite ledger side and
committed audit artifact do not constitute a new checker input boundary.
Neither result chooses a source row, a true testimony or canon. See round
38 LOG closure and `reports/r38-axis-adjudicator.md`.

## Round 39: unresolved event source at a ledger endpoint

`r39-ledger-source-unique/` is a byte-identical r35 Bell-7 copy.
`r39-ledger-source-missing/` differs only at Sella's timeline event
`source_id`: `sella-bell7-note` becomes absent `missing-sella-note`.
The cited fictional excerpt still exists, but this event's ID pointer to
an in-world source row no longer resolves. Both ledger event IDs remain
unique. Run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r39-ledger-source-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r39-ledger-source-missing
```

The control exits 0. The negative exits 1 with a ledger `claim_b` “event
has no resolvable source_id” finding and a `timeline[3].source_id` unknown-
source finding. This probes zero matching source rows, not the duplicated-
source ambiguity tested in r7's temporary ledger `claim_a` probe and
r38's rejected audit. It is an existing checker path, not a new rule or
proof that Sella lied, that her excerpt is false or that canon is settled.

## Round 40: Vela's attributed auditory report

`r40-vela-listener/` derives from r35, preserving Tarin's and Sella's
fictional excerpts and their unresolved ledger. A newly authored Vela note
reports that she heard two strokes **she took to be** the registry bell
while on Lantern Harbor's east steps during her source-claimed Bell-7. She
reports that she did not see Sella or an envelope. The fixture appends a
separately cited Vela character and report event; `vela-clause-map.md`
traces the wording. Run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r40-vela-listener
```

A clean result checks JSON structure and citation IDs, not the excerpt's
truth. Vela's tentative sound identification does not establish which bell
sounded. Her non-sighting does not establish absence, refute Tarin or
support Sella; a shared local tick 3 does not authenticate the Bell-7 date
or synchronize accounts. No envelope contents or canon outcome follows.

## Round 41: tentative versus direct identification in an attributed report

`r41-vela-direct-bell/` keeps all five r40 JSON files byte-for-byte but
changes Vela's fictional excerpt from “heard two strokes I took to be the
registry bell” to “heard the registry bell strike twice.” Its new editorial
`strength-contrast-map.md` notes that the fixed claim/event still says
“she took to be.” That remains a *compatible weaker summary*, not a false
record; it loses the stronger excerpt's reported confidence. Neither
excerpt establishes that the registry bell objectively rang.

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r40-vela-listener
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r41-vela-direct-bell
```

Both exit 0 because the checker reads JSON, not Vela's prose. A human
must assess attribution and strength fidelity; the date/non-sighting,
source authenticity, external bell origin, Sella/envelope absence and
canon remain unverified. This is not an automated prose check.

## Round 43: another attributed view of Vela’s reported location

`r43-jorin-vela-sighting/` retains the r41 fixture and adds a fictional
first-person `jorin-note` excerpt, source, Jorin character claim and one
Jorin-attributed event. Jorin says he saw Vela on the Lantern Harbor east
steps from the registry doorway during what **he called** Bell-7, and did not
see who, if anyone, struck a bell. `jorin-clause-map.md` traces the exact
phrases. The current r41 and r43 `vela-clause-map.md` files were corrected in
r48 to quote their local direct excerpts; older creation-time reports accurately
describe the formerly stale inherited maps. Use `strength-contrast-map.md` for
the r40 tentative versus r41 direct wording and its fixed, weaker but compatible
JSON summary—not as an objective bell claim.

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r41-vela-direct-bell
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting
```

Both exit 0 **structurally**. The new cross-account comparison concerns
Vela’s **reported** position only, conditional on referent and occasion. The
shared Bell-7 label and tick 3 do not verify one occasion or objective ringing,
striker, Sella/envelope absence, chronology, authenticity or canon. Neither
checker nor citation decides those questions.


## Round 59: repeated JSON object member names

The checker parses each table with an object-pairs hook. If **any** object in a
JSON file repeats a member name (including nested `claims`, ledger references,
or provenance objects), that whole file is treated as unloadable. It reports
`<file>: duplicate object member '<name>'; cannot load JSON` and does not choose
either value. The parser hook has no reliable row/path context, so the message
names the file and member only. Other files are still checked; as shown by
`r59-nested-duplicate/`, unloading an entity table can consequently produce
dangling-reference findings in other tables. Those are consequences of missing
loaded rows, not proof that entities are absent. Unique-member files retain the
existing validation behavior.

The isolated `r59-duplicate-harbor-tower/` and
`r59-duplicate-tower-harbor/` fixtures begin from the five consistent tables. Both
set arrival tick to 1 and `depends_on` to `[]`; only the order of duplicate,
valid `place_id` values differs. `r59-unique-control/` keeps the same equal-tick, empty-dependency rows
with a single tower choice; it reports the expected input-field double-booking. The previous checker silently used the final duplicate member: in this
controlled equal-tick case the two orders flipped between a double-booking
finding and CLEAN. The candidate instead rejects both files, without making a
place choice. This is a parser/input rule, not a story truth, chronology, canon,
source-support, or rights determination.

The `r5-*` malformed-input matrix exercises missing files, invalid JSON,
wrong top-level shape, row shape, and citations; it does not define duplicate
member policy. This candidate retains the invalid-JSON handling path and adds a
separate stable duplicate-member diagnostic. No claim is made that r5's limited
probes prove all malformed inputs are cascade-free. See
`../../reports/r59-executor.md` for raw candidate output and replay limits.


## Round 60: unavailable entity index

Entity-reference conclusions require a successfully parsed `entities.json` top-level array. If the file is missing, invalid JSON (including rejected duplicate members), or has a non-array top level, the checker retains its load/shape diagnostic and does not call referenced entities dangling, ambiguous, the wrong kind, or infer occupancy/alliance conclusions from the unavailable index. It still validates other tables, source citations, timeline tick and dependency rules, and independent schema. Provenance entity lookups naturally have no rows to process when the full entity file is unavailable.

A successfully loaded empty array is available and therefore referenced IDs are checked as dangling. A loaded array is available even if row validation rejects some rows: only retained valid rows enter the index, so a reference present only in a rejected row can still be reported dangling from the loaded input. A valid partial array likewise reports absent IDs as dangling; duplicate valid IDs retain prior ambiguity behavior. These findings are about loaded input rows, not a complete fictional-world registry. This policy is limited to entity-table availability; it does not suppress checks because sources or timeline tables are unavailable and does not establish fictional-world absence, canon, source truth, or rights. The `r60-unavailable`, `r60-empty`, and `r60-partial` fixtures share the other four tables to isolate that distinction. `r60-unavailable-independent` keeps the same unavailable `entities.json` but adds a negative tick, unknown source and unknown dependency to confirm those independent diagnostics survive.

## Round 61: source-index availability

The checker distinguishes an unavailable `sources.json` (missing, unreadable, invalid JSON, duplicate object member, or a parsed non-array) from a successfully loaded array. On unavailable input it retains the file/shape diagnostic but does not infer unknown/ambiguous source membership, ledger “no resolvable source_id,” sourced provenance-chain certainty, or a missing sourced alliance reciprocal from that absent index. Independent record, pointer, holder, tick, dependency, entity and schema findings remain active. A loaded empty array still reports absent IDs; loaded partial arrays resolve only retained IDs; duplicate admitted IDs remain ambiguous. An array with rejected rows is still available over the rows admitted by existing validation, so an ID present only in a rejected row can still be reported unknown. Withholding citation findings also removes their per-reference repair pointers: use the loader error to repair the table, then rerun. These checks establish input-index membership only, not source-text support, fictional-world absence, truth, canon, or rights.

Matched controls: `r61-direct-*` vary only the source table against `consistent`; `r61-independent-unavailable` and `r61-independent-empty` share their other four tables and retain independent provenance holder/shape and timeline tick/dependency faults; `r61-allied-*` test reciprocal gating; `r61-ledger-unavailable` checks independent ledger pointer and timeline findings.
