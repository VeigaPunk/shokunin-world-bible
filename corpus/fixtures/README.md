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
