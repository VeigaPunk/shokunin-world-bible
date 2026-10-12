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
