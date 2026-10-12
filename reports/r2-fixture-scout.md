# Round 2 fixture scout: minimal reciprocal and one-way cases

## Recommendation

Use two small standalone fixture directories, `corpus/fixtures/ally-reciprocal/` and `corpus/fixtures/ally-one-way/`, each with the checker's required four JSON arrays. Keep `timeline.json` empty. Each should have only two faction entities and the relation rows needed for its case; no character/place/timeline records are needed. A clean/invalid pair differing only by the reverse edge makes the symmetry behavior easy to attribute.

Suggested fictional records (all invented):

- `sources.json`: one source, e.g. `{"id":"harbor-compact","title":"Lantern Harbor Compact, year 12","kind":"fictional treaty record","reliability_note":"in-world fiction; cited only as fixture evidence"}`.
- `entities.json`: `quay-guild` and `bell-wardens`, each `kind: "faction"`, names, `first_appearance: "harbor-compact"`, and `claims: []`. (Entity claims may be empty; the checker still requires the first-appearance source.)
- `ally-reciprocal/relations.json`: exactly `{from: "quay-guild", to: "bell-wardens", type: "allied_with", source_id: "harbor-compact"}` and the reverse row with the same source.
- `ally-one-way/relations.json`: only the first row.

The edge rows themselves cite their in-world source through `source_id`; no unsupported real-world references are involved. Retain the existing consistent fixture unchanged as a regression case. If implementing the narrowly scoped rule only for faction-to-faction `allied_with`, these examples test the declared contract without requiring an ontology for other relation types.

## Evidence paths inspected

- `.shokunin/lore/LOG.md` — Round 2 claim declares sourced reciprocal alliance required and forbids inferring alliance from prose.
- `.shokunin/lore/corpus/fixtures/check_bible.py` — `FIELDS` defines relation rows as `from`, `to`, `type`, `source_id`; relation validation checks both endpoints against entities and validates source IDs. It currently has no reciprocal rule. `KINDS` includes `faction`.
- `.shokunin/lore/corpus/fixtures/consistent/entities.json` — entity rows use `first_appearance` plus sourced `claims`; claims can be empty arrays in the schema.
- `.shokunin/lore/corpus/fixtures/consistent/sources.json` — source record shape and fictional-source style.
- `.shokunin/lore/corpus/fixtures/consistent/relations.json` — existing non-alliance `carries` example; preserve it as regression coverage.
- `.shokunin/lore/corpus/fixtures/README.md` — current command convention, citation boundary, and no-canon-mutation promise.

## Cautions

- The current checker requires all four JSON files even when a section is empty. Use `[]` for `timeline.json`; do not omit it.
- A reciprocal row is a separately sourced assertion, even if both rows cite one compact document. The checker can require the reverse tuple to exist; it should not fabricate that row or rewrite canon.
- Avoid broad requirements that all relation types be symmetric, that `allied_with` applies only to factions unless that scope is explicitly the declared rule, or that missing reverse edges prove an in-world fact is false. The one-way fixture only demonstrates a checker violation under the selected convention.
- The current code permits duplicate relation rows. This paired fixture does not test duplicate handling; avoid quietly adding deduplication or duplicate-policy behavior to the axis move.
