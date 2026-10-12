# Round 14 ledger excerpt scout — registry and watch bell

## Observed baseline (raw fixture paths)

- `.shokunin/lore/corpus/fixtures/r10-registry-witness/sources.json` has source ID `archive-ledger`, title “Lantern Harbor Registry, year 12,” and metadata calling it a fictional municipal record that “records movements, not omniscient truth.” This is metadata; it contains no ledger excerpt wording.
- `.shokunin/lore/corpus/fixtures/r10-registry-witness/entities.json` assigns `harbor` and `tower` first appearance to `archive-ledger`. Their exact claims are “Lantern Harbor has a registry.” and “North Tower has a watch bell.”
- `.shokunin/lore/corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md` is separately labeled invented fixture text. Its text says Sella leaves the registry destination blank at Mira’s request; it does not supply `archive-ledger` wording.
- These paths contain designed fixture assertions and source metadata, not independently recovered evidence. The checker does not validate prose against claims.

## Bounded draft (recommendation only; not written to the fixture)

> **Fictional source excerpt — newly authored fixture text, not recovered evidence**  
> Source ID: `archive-ledger`  
>  
> Registry note: Lantern Harbor has a registry. North Tower has a watch bell.

This deliberately states only the two existing place claims. It supplies no event, date, order, bell schedule, registry procedure, route, or connection between the registry and tower. “Year 12” appears in the source metadata title, but the proposed wording does not infer when either feature was established or when this note was made. This is a proposed fixture rendering, not an observed quotation or corroboration.

## Proposed manual map (recommendation, not fact)

| Existing raw JSON row | Exact existing assertion | Proposed phrase | Limit |
|---|---|---|---|
| `entities.json` `$[1].first_appearance` (`harbor`, source `archive-ledger`) | Lantern Harbor is indexed as first appearing in this source | “Lantern Harbor has a registry.” | Names the place; does not establish literal historical first appearance or completeness of the archive. |
| `entities.json` `$[1].claims[0].statement` | “Lantern Harbor has a registry.” | “Lantern Harbor has a registry.” | Direct wording match in the proposed invented text only. |
| `entities.json` `$[2].first_appearance` (`tower`, source `archive-ledger`) | North Tower is indexed as first appearing in this source | “North Tower has a watch bell.” | Names the place; does not establish literal historical first appearance or completeness of the archive. |
| `entities.json` `$[2].claims[0].statement` | “North Tower has a watch bell.” | “North Tower has a watch bell.” | Direct wording match in the proposed invented text only. |

No relations or timeline rows in `.shokunin/lore/corpus/fixtures/r10-registry-witness/relations.json` or `timeline.json` cite `archive-ledger`; this draft therefore maps no relation or event. In particular, it must not be used to fill the destination Sella left blank in `registrar-copy-excerpt.md` or to imply that the registry and tower were visited in any order.

The phrase-to-row correspondence is editorial traceability for a newly authored fictional fixture. It is not evidence that an earlier source contained these words, proof that the claims are true, or independent corroboration. Whether this legibility alone meets the round’s depth criterion is for review, not established by this draft.
