# Round 15 simplifier report

## Raw observations

- The standing round-15 declaration says the active `r10-registry-witness` excerpt ends with Sella keeping the carbon after leaving Mira’s destination blank; it does not describe a later inspection or any mark. See `.shokunin/lore/LOG.md`, “Round 15 — 2026-10-12 (depth axis-move; declaration before dispatch)”.
- The active fixture’s `registrar-copy-excerpt.md` says: “At Mira’s request, I left the registry destination blank and kept the carbon.” The matching existing `timeline.json` row is `registry-entry`, tick 1, Sella at harbor, source `registrar-copy`; existing events `departure` and `arrival` have ticks 1 and 2. `sources.json` already describes `registrar-copy` as Sella’s handwritten register excerpt.
- The checker’s required timeline fields include `id`, integer `tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`; source rows require `id`, `title`, `kind`, `reliability_note`. Its dependency check requires referenced events to have strictly earlier ticks. See `corpus/fixtures/check_bible.py`.

## Recommendation (not an observation)

Smallest substantive addition in a **separate copy** of the r10 micro-bible: add one source row for a clearly invented Sella follow-up note, one cited event, and the short excerpt that states the event. Leave every inherited row intact. Do not add new entity claims or relations.

Suggested source: `sella-carbon-followup` (fictional private note; explicitly authored for the fixture, not recovered evidence). Suggested event: `carbon-followup`, tick 3, entity `sella`, place `harbor`, depends_on `["registry-entry"]`, source `sella-carbon-followup`, description: “Sella examines the kept carbon again and records a blurred blue oval mark; she cannot identify its origin.” Tick 3 is a local sequence choice after the existing tick-2 arrival, not a conversion of “first bell” into numeric time. The excerpt should match this bounded assertion and explicitly say that Sella does not identify the mark with Mira or the Blue Seal. Do not assert that the mark is a seal, that Mira made it, or that it was present at the first inspection.

This single observation introduces a new event and an unresolved physical detail in the otherwise blank-record thread; it is more than rewording existing rows. Depth remains a proposed gain pending non-author clause review. It would not establish the mark’s truth, provenance, or relation to the Blue Seal. A clean checker run only establishes schema/reference consistency. Preserve the r10 fixture and old rows; the proposed event belongs only in the separate new micro-bible.
