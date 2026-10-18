# Round 2 citation scout — in-world source conventions

## Observed convention and evidence

- The fixture models an in-world source as a row in `sources.json` with `id`, `title`, `kind`, and `reliability_note`; the README explicitly calls these “in-world fictional records.” See `.shokunin/lore/corpus/fixtures/consistent/sources.json` and `.shokunin/lore/corpus/fixtures/README.md`.
- Entity assertions carry citations at claim granularity (`claims: [{statement, source_id}]`), and entity `first_appearance` also names a source. Examples: Mira’s “carried the blue seal” claim cites `courier-log`; the Harbor registry claim cites `archive-ledger` in `.shokunin/lore/corpus/fixtures/consistent/entities.json`.
- Relations use a single `source_id` on the edge, as in the `mira` → `seal` `carries` edge in `.shokunin/lore/corpus/fixtures/consistent/relations.json`. Timeline events likewise use `source_id` (`.shokunin/lore/corpus/fixtures/consistent/timeline.json`). The checker verifies that these IDs resolve to in-world sources, in `.shokunin/lore/corpus/fixtures/check_bible.py` (`source()` and the relation/timeline loops).
- Current available fictional source types illustrate different perspectives rather than universal truth: `archive-ledger` is a municipal registry recording movements, while `courier-log` is a first-person route log. Their explicit reliability notes are in `consistent/sources.json`; `.shokunin/lore/corpus/fixtures/README.md` warns that a citation does not mean the source is omniscient or that checker output chooses canon.
- Real-world method references are kept separate from story citations in `.shokunin/lore/corpus/knowledge/reference-ledger.md`; the decision table says the required local source-ID convention is editorial, not mandated by PROV-O (`.shokunin/lore/corpus/knowledge/2026-10-12-lore-decision-table.md`).

## Suitable pattern for faction records

For a faction claim, use the existing entity claim convention: faction entity with `kind: "faction"`, a `first_appearance` source ID, and each factual assertion represented as a claim with its own resolvable `source_id`. For a `allied_with` relation, cite that relation row itself with `source_id` for the in-world record that attests the alliance; if reciprocal edges are added, cite each row to evidence supporting that direction. Faction treaties, council minutes, orders, or correspondence could be modeled as fictional source records only when actually supplied/created as in-world evidence; the present corpus does not establish any such documents or facts. Current schema allows any nonempty `kind` for sources and faction as entity kind, but does not prescribe faction-specific source types or rules.

## Cautions / limits

- Do not cite a real-world reference-ledger entry as proof of an in-world faction fact. The two citation systems have distinct jobs.
- A source citation records provenance, not truth, neutrality, reliability, or agreement across sources. Preserve conflicting sourced claims; report the conflict for editorial review rather than infer the winning faction account.
- Do not invent a source or its contents just to complete a faction record. The fixture README directs authors to omit uncertain assertions rather than present uncited canon; seed guidance says unsupported material must not be presented as canon (`.shokunin/lore/corpus/knowledge/seed.md`).
- The checker verifies source-ID existence and basic claim structure, not whether the cited source text actually supports the statement, whether a source is biased, nor whether a faction relation is semantically true. Those checks remain editorial/manual.
- The round-2 declaration confines the proposed symmetry check to explicit `allied_with` edges; absence of a reciprocal edge is not itself a general lore contradiction. A reciprocal-edge requirement is a declared data convention, not proof that an alliance is true.
