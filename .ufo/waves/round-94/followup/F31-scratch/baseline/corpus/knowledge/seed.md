# lore seed knowledge

A lore shokunin's corpus is a world bible plus the discipline that keeps it
honest. Adapted from the art-east-asian-design ledger's citation discipline
(attribution / rights / AI-training kept as distinct questions) and the
fleet's evidence rules (provenance or it didn't happen).

## World-bible schema (proposal, first round falsifies/refines it)
- `entities.json` — every entity: {id, kind (character|place|faction|item),
  name, first_appearance (source id), claims: [{statement, source_id}]}
- `relations.json` — directed edges {from, to, type, source_id}
- `timeline.json` — events {id, when (in-world dating + ordering), what,
  source_id}
- `sources.json` — in-world documents {id, title, kind, reliability_note}
- Every claim carries a source_id; a claim without one is flagged
  `invented` and must never be presented as canon.

## Consistency discipline
- Contradictions are surfaced as contradiction records {claim_a, claim_b,
  why}, never silently resolved; resolution is an editorial decision with
  its own source.
- Timeline ordering is checked mechanically (topological check) once the
  corpus has ≥2 dated events.
- Names/aliases index-checked: two entities sharing a name must disambiguate.

## Sourced inspiration
- Real-world references enter through a reference ledger with the art
  lane's three distinct questions (attribution / rights / training
  permission), kept separate from in-world canon.
