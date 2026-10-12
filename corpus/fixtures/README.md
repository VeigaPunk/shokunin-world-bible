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
