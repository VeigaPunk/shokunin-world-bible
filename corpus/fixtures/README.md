# Runnable lore bible example

From the repo root, run:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions
```

The first command exits 0; the second exits 1 and prints **all three** seeded
violations. No file is modified by the checker. An event's `tick` is a
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
