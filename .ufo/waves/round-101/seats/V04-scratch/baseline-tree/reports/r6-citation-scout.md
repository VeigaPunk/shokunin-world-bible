# Round 6 citation scout — item holder and transfer source granularity

## Observed in the repository

- The entity schema lists `item` as an allowed kind, but an item has only an ID/name, `first_appearance`, and free-text `claims`; the checker validates each claim’s nonempty `statement` and resolvable `source_id`. It does not parse holder identity, dates, acquisition, or transfer from claim text. Evidence: `.shokunin/lore/corpus/fixtures/consistent/entities.json` (`seal`, claim “The seal accompanied Mira.”); `.shokunin/lore/corpus/fixtures/check_bible.py` (`KINDS`, entity claim loop).
- The clean fixture has one holder-like assertion at two places: entity claim “Mira carried the blue seal.” and relation `mira` → `seal`, type `carries`; both cite `courier-log`. The relation row has no tick or event reference, and the entity claim has no structured subject/item/time fields. Evidence: `.shokunin/lore/corpus/fixtures/consistent/entities.json`, `.shokunin/lore/corpus/fixtures/consistent/relations.json`.
- In-world source rows are identified by `id`, with `title`, `kind`, and `reliability_note`. Here `courier-log` is a fictional first-person route log; `archive-ledger` is a fictional municipal record. These notes characterize perspective, not the contents of a particular passage or its support for a holder assertion. Evidence: `.shokunin/lore/corpus/fixtures/consistent/sources.json`.
- Timeline events have `id`, `tick`, `entity_id`, `place_id`, description, and `source_id`, but no item or holder field. Relations and timeline rows cite individually. Evidence: `.shokunin/lore/corpus/fixtures/consistent/timeline.json`; checker `FIELDS` and timeline/relation loops in `.shokunin/lore/corpus/fixtures/check_bible.py`.
- The contradiction ledger can point only to timeline event fields `place_id`, `tick`, or `depends_on`; it does not represent holder assertions or item transfers. The checker verifies the referenced event/source pointer, not whether cited text supports a statement. Evidence: `.shokunin/lore/corpus/fixtures/check_bible.py` (`allowed_assertion_fields`, ledger loop); `.shokunin/lore/corpus/fixtures/README.md` (citation/truth limitations).
- The README says citations are fictional in-world records, not proof of omniscient truth, and uncertain assertions should be omitted rather than asserted uncited. The checker resolves source IDs; it does not authenticate documents, inspect their contents, or establish textual entailment. Evidence: `.shokunin/lore/corpus/fixtures/README.md`; `.shokunin/lore/corpus/fixtures/check_bible.py` (`source()`).

## Recommendation (not current behavior)

If a later convention records transfers, make each explicit transfer assertion independently source-addressable: identify the item, prior holder, new holder, ordering point (such as the existing local `tick` convention), and its own in-world `source_id`. Any initial acquisition/known starting holder should likewise be an explicit cited assertion if the chain rule needs it. Do not treat an entity’s free-text claim, an undated `carries` relation, or a prose implication as a transfer record unless an explicit data convention says so. Current examples do not establish a transfer-record schema or actual transfer events.

Keep source granularity at the assertion/record level: each step should point to its own source rather than borrowing the prior step’s citation. A resolvable ID only establishes a pointer, not that a source text attests the exact holder, item, direction, or ordering. Preserve disagreements between separately cited assertions for editorial review; do not select a winner based on source kind/reliability note or silently repair a chain.

A bible with no explicit transfer records currently means only that the corpus contains no modeled transfer data; it is not evidence that no transfer occurred and should not become a violation solely for absence. Distinguish that absence from multiple incompatible, explicitly sourced holder assertions. Any future chain check should be bounded to the declared record convention and report the conflicting/broken local record without claiming exhaustive provenance semantics. None of this asserts rights or game mechanics.

## Boundary

This is a source-granularity map and recommendation only. No checker behavior, fixtures, or shared documentation were changed.
