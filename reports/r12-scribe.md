# Round 12 scribe — bounded actor-identity decision table and README proposal

Scope: documentation draft only. I changed no checker, fixture, README, other shared document, or commit. The round-12 LOG declaration names baseline report commit `954a1b712590f9b89aed6757e72a8bd4af5c8848` and baseline checker `.shokunin/lore/corpus/fixtures/check_bible.py`. This report distinguishes checked-in/raw behavior from recommendations; it does not claim the round-12 move has been probed or implemented.

## Observed checked-out behavior (not a proposed policy)

The checker builds `entities` from schema-valid entity rows, while separately collecting `entity_id_counts` for those rows. Its timeline loop tests whether `entity_id` and `place_id` are keys in `entities`; it then checks place-kind ambiguity using the count for `place_id`. But occupancy is tracked under `slot = (row['entity_id'], row['tick'])` without checking `entity_id_counts[row['entity_id']]`. A second event with the same actor string and tick but another place can therefore be reported as `double-booked` even when that actor string names multiple schema-valid entity rows. The checker does not resolve which row, person, or canon is intended.

The raw checked-in commands I ran:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
# CLEAN: schema, citations, relations, timeline; 0 violations
# exit 0
```

No `r12-*` fixtures exist in the checked-out fixture directory at time of writing. I have not reproduced the duplicate-actor occupancy premise with a CLI pair, compared round-12 raw output, or run a post-change regression. The report-commit baseline is named in LOG; current source inspection is not represented as an independent replay of that commit.

## Bounded decision table (recommendation; not active behavior unless separately implemented and verified)

| Timeline actor-ID condition | Recommended actor/occupancy conclusion | Preserve / boundary |
|---|---|---|
| `entity_id` has zero schema-valid entity rows | Keep the existing dangling entity-reference finding. Do not treat membership failure as evidence of an actor or occupancy identity. | Raw timeline row remains; unrelated place, citation, tick, dependency, and schema checks remain in scope. |
| `entity_id` has exactly one schema-valid entity row | Retain the existing occupancy rule: repeated `(entity_id, tick)` at different places can be reported as `double-booked`; same-place records do not trigger that different-place finding. | Unique-ID case should retain behavior. This structural rule does not prove the events true or establish a real-world clock. |
| `entity_id` names more than one schema-valid entity row | Recommend a field-local ambiguous actor-reference finding and skip using that identifier to infer a same-actor occupancy collision for the affected row(s). | Keep duplicate-entity-ID diagnostics and every entity/event row. Do not select first/last row, choose canon, or generalize to all identity consumers. |
| Duplicate ID appears only on malformed entity rows excluded from the schema-valid entity collection | Do not count those rows as a valid actor target under the proposed rule; retain whatever existing schema/input diagnostics apply. | Confirm exact loader filtering against implementation/test before documenting detailed malformed-row output. |
| `place_id` itself is duplicate/ambiguous | Outside this actor-identity proposal; existing round-11 place-reference rule is a separate field-local policy. | Do not conflate actor ambiguity with place ambiguity or suppress an independent place finding. |
| Relation endpoint, provenance holder, name/alias, or another identity-bearing reference is duplicated | Outside this round. | No promise of global entity-reference ambiguity detection or universal identity resolution. |

The proposed diagnostic phrase “ambiguous actor reference” describes a possible local input finding, not observed or required literal CLI text. Avoid calling the two records “one character” or claiming they are different people: duplicate IDs establish structural ambiguity only. Likewise, suppressing a collision inference is not a finding that the events are compatible, simultaneous, contradictory, or false.

## README wording proposal (recommendation only)

Suggested addition to `.shokunin/lore/corpus/fixtures/README.md` after its round-11 section, **only if** the paired fixtures, implementation, and independent replay support the declared rule:

> **Round 12: ambiguous timeline actor IDs.** A timeline `entity_id` that matches more than one schema-valid entity row does not identify a unique actor for the occupancy check. The checker reports the local ambiguous actor reference and does not infer a same-actor, different-place collision from that ambiguous ID. Duplicate-ID findings and all input rows remain. With exactly one matching entity row, the existing same-tick/different-place occupancy check still applies; an absent ID retains the dangling-reference finding. This rule concerns timeline actor occupancy only. It does not resolve identity from names, prove whether either event happened, determine canon, or extend ambiguity handling to every entity reference.
>
> Run the `r12-*` duplicate-actor pair and unique-actor control with the checker command above. The paired cases should differ only in actor uniqueness and demonstrate that the ambiguous pair is not diagnosed as a same-actor collision while the unique control is. Preserve exact observed outputs and exit statuses in the round run record.

Until validation and adjudication are complete, this paragraph is a draft, not documentation of current behavior. Do not append it as active README content based on source inspection alone. In particular, this scribe has no raw duplicate/unique actor CLI output to quote, and no claim that old fixture outputs remain unchanged.
