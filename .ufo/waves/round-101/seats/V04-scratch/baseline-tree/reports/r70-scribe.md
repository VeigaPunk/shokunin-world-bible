# Round 70 scribe — input-ledger boundary

## Scope and declaration

The Round 70 declaration in `.shokunin/lore/LOG.md` (Round 70 entry) proposes one calibration change: run the same-reference comparison only when both sides have a nonempty string `event_id`; retain the existing raw `field` equality check and per-side allowed-field diagnostics. It explicitly requires the R62 malformed-side pair warning to remain, valid identical references to remain flagged, valid different references to remain clean, and old fixture outcomes otherwise to be compared. This report records the input-ledger and interpretation boundary; it does not assess a candidate or authorize an implementation.

## What the checker compares

In `.shokunin/lore/corpus/fixtures/check_bible.py:111-126`, each side is independently checked for dictionary shape, a nonempty string `event_id`, and an allowed `field` (`place_id`, `tick`, or `depends_on`). At lines 139-143, the pair-level check separately compares the two dictionaries' raw `.get('event_id')` and `.get('field')` values. It does not use a source-text claim or decide whether two assertions conflict. Thus the proposed event-ID-only gate is narrower than R69's rejected gate: it can preserve the R62 case, whose event IDs match and are nonempty although both fields are invalid.

The R69 record in `.shokunin/lore/LOG.md` and `.shokunin/lore/reports/r69-axis-adjudicator.md` rejects gating on both event-ID and field validity because that would also suppress the R62 pair warning. The committed `.shokunin/lore/corpus/fixtures/r62-malformed-side/contradictions.json` has the same nonempty `tarin-envelope-observation` ID and invalid `bogus` field on both sides. The baseline R62 reports (`reports/r62-reviewer.md`, `reports/r62-axis-adjudicator.md`) document the pair warning alongside the two field diagnostics. This is a concrete required retention control for R70, not proof that every such warning is useful.

A nonempty string check is only a structural property of the supplied ledger value. It does not establish that the ID resolves to a timeline row, that a source supports either assertion, or that the assertions are true. The checker’s event membership/source-index diagnostics are separate checks (checker lines 127-138). Similarly, a same-reference finding is an input-pointer diagnostic, not evidence of a semantic contradiction.

## Evidence limits and controls

The declaration calls for matched missing/blank-ID cases and valid-identical / valid-different controls. The committed `r62-loaded` input has distinct valid pointers, not a valid-identical pair; the committed `r62-malformed-side` case is an invalid-field retention control and also has malformed timeline JSON. Neither alone is a matched test of the proposed missing/blank-ID behavior. No R70 scout reports or candidate evidence were present in `.shokunin/lore/reports/` at the time of this report. Therefore this report does not claim that the declared change is material, harmless, implemented, or validated, and does not claim an old-fixture replay result.

The fixture README's Round 3 description (`.shokunin/lore/corpus/fixtures/README.md:43-54`) says the ledger validates pointers and required text, not citation truth or whether `why` accurately explains a semantic contradiction. This report makes no inference from fixture prose to source support, fictional event occurrence, canon, chronology, rights, or game mechanics. No source text was evaluated.
