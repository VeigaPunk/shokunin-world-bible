# Round 7 source-ID membership scout

## Scope and method

Observed the working-tree checker at `.shokunin/lore/corpus/fixtures/check_bible.py`, fixture JSON under the same directory, baseline checker via `git show 4f6eaba9c7f4807b4a28ba9883af5bf479252294:.shokunin/lore/corpus/fixtures/check_bible.py`, and direct CLI runs from repo root. I made no checker or fixture changes. The synthetic duplicate-source probe lived only under `/tmp/lore-source-scout-4tb0txne/dup`.

## Source-ID membership map (observed working-tree code)

- `index('sources')` at checker lines 36–42 builds a dictionary keyed by ID. On a repeated ID it appends `sources[N].id: duplicate sources id ...`, then unconditionally assigns `result[row['id']] = row`. Therefore the retained dictionary value is the **last** record for that ID. This is actual duplicate validation plus last-wins index behavior; the chosen record is not otherwise inspected by citation checks.
- The helper `source(source_id, location)` at lines 61–63 only tests `source_id not in sources`, emitting “unknown in-world source” when absent. This is membership validation, not source-text support validation and not uniqueness validation.
- Entity `first_appearance` (line 96) and each structurally acceptable claim `.source_id` (lines 97–102) use that helper. A malformed claim can fail its own shape condition and skip source membership checking.
- Relations `.source_id` (line 108) and timeline `.source_id` (line 215) use the helper.
- Provenance records check nonempty string shape (lines 168–170), call the helper (172), and separately set `valid = False` only when ID is absent from `sources` (173). Thus an existing duplicate ID leaves that record eligible for chain continuity checks; no uniqueness condition is applied.
- Contradiction-ledger references do not call the helper: after requiring exactly one timeline event, the event's source is tested with `event['source_id'] not in sources` (lines 83–86). If absent, the finding says the event has “no resolvable source_id.” A duplicate source key passes this membership test.
- Reciprocal-alliance witness logic (lines 193–203) uses `candidate['source_id'] in sources` in its `any(...)` predicate. A reverse relation with a duplicate source ID can therefore qualify as the “sourced reciprocal relation.” This is witness use rather than a uniqueness validation. The outer relation's own source is independently checked by the ordinary helper.

These uses establish only that an ID is present in the dictionary. They do not establish that the referenced source text supports a claim, that a source is true/reliable, or that a duplicate ID denotes one unambiguous record. No other `sources` membership expressions appear in the checker source search: the use sites are the helper and the direct contradiction, provenance, and reciprocal-witness checks listed above.

## Duplicate behavior observed

The baseline committed checker has the same `index()` loop and the same membership patterns; `git show` at the baseline hash confirms it reports duplicates, then overwrites the earlier dictionary value with the later row.

I copied `ally-reciprocal` to `/tmp`, appended a second `harbor-compact` row to `sources.json` (different title, same ID), and ran:

`python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-source-scout-4tb0txne/dup`

Observed exit 1 and exactly:

```
VIOLATION: sources[1].id: duplicate sources id 'harbor-compact'
1 violation(s); no canon changed
```

There was no ambiguous-source diagnostic and no missing-reciprocal diagnostic. The latter is significant: `ally-reciprocal/relations.json` contains both directions, each with `source_id: harbor-compact`, so the duplicate-ID reverse edge continued to satisfy the witness predicate. This demonstrates the existing witness consequence, not an assertion that either duplicate document supports the alliance.

Other unmodified CLI observations, from repo root:

```
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
CLEAN: schema, citations, relations, timeline; 0 violations

.../ally-reciprocal
CLEAN: schema, citations, relations, timeline; 0 violations

.../ally-one-way
VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation
1 violation(s); no canon changed

.../item-chain-valid
CLEAN: schema, citations, relations, timeline; 0 violations

.../item-chain-broken
VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
1 violation(s); no canon changed
```

The valid and broken item-chain fixtures use `courier-log` and `archive-ledger` as provenance IDs; the checker verifies dictionary membership, then its holder/tick rule. The alliance fixtures use `harbor-compact`; `ally-one-way` has no reverse edge, so it fails independently of source ambiguity. Existing fixture outcomes above do not test duplicate IDs.

## Distinction: validations vs witnesses

**Validation/reporting:** duplicate-key finding from `index`; unknown-ID checks for first appearances, entity claims, relation citations, timeline citations, and provenance citations; contradiction-ledger event-source resolvability check. These validate ID shape/presence (and elsewhere duplicate IDs), not documentary support. In particular the source helper does not complain when the ID is duplicated.

**Witness qualification:** reciprocal alliance logic treats a reverse relation as a sourced witness when its source ID is in the dictionary. A duplicate ID passes. Separately, citations on claims/events/provenance are checked as references; they are not used to establish the reciprocal witness. There is no general rule that all citations must resolve uniquely.

## Bounded proposal (not observed behavior)

To match the round-7 claim without selecting a source record, retain all duplicate source rows and the duplicate-ID violation, but track source-ID counts (or an equivalent unique-ID set) and reject ambiguous IDs as qualifying citations. Emit local ambiguous-reference findings at the relevant source-ID location; ensure direct-membership paths (especially contradiction-ledger and reciprocal witness) follow the same uniqueness policy. Keep missing-ID findings distinct from ambiguity. Do not claim textual support or truth verification. This is a proposal only; I did not implement or test it.
