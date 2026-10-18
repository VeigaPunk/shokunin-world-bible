# Round 70 branch scout — event-ID-only same-reference gate

## Scope

Read the Round 70 declaration in `.shokunin/lore/LOG.md:1230-1233`, the active checker, the R69/R62 reports, and the R62 malformed-side fixture. This is a baseline branch map and minimal-predicate recommendation only. I did not run probes or edit checker, fixtures, README, LOG, or corpus.

## Existing branch and minimal gate

In `.shokunin/lore/corpus/fixtures/check_bible.py:111-138`, each side is validated independently. A side must be a dict (`:113-118`), have a nonblank string `event_id` (`:119-123`), and have a string `field` in `{'place_id', 'tick', 'depends_on'}` (`:124-126`). Its `continue` skips subsequent timeline-availability, event-count and source checks when the local ID or field is malformed. These diagnostics are separate from the pair comparison.

The existing comparison at `:139-143` runs after the side loop. It requires only that both values are dicts, then compares raw `.get('event_id')` and `.get('field')` for equality. It does not consult the side-validation results. Thus `{}`/`{}` compares `None == None` for both keys; equally blank IDs can also compare equal. The pair finding is `claim_a and claim_b references must differ`.

The minimal Round 70 gate is to add, for **each** dict side, the already-used event-ID predicate—`isinstance(event_id, str) and event_id.strip()`—to the pair condition, while leaving the existing raw event-ID and field equality checks intact. In logical form: both sides are dicts; each `.get('event_id')` is a nonempty string; and the two raw event IDs and fields compare equal. Do **not** add field-validity, timeline availability, event membership/cardinality, or source-resolvability requirements. The local field diagnostics and all per-side checks stay untouched. This eligibility guard is structural only; a nonempty string does not establish that an event exists.

## Relevant prior behavior and controls

- Round 70 declaration (`LOG.md:1231-1233`) expressly narrows the rejected R69 idea to event-ID nonemptiness alone and requires missing/blank-ID cases to lose only the pair finding, R62 to retain its warning despite invalid matching fields, valid-identical to retain the warning, and valid-distinct to remain clean.
- R69's declaration and closure (`LOG.md:1213-1228`) rejected a broader both-ID-and-field-validity gate. The R69 reviewer (`reports/r69-reviewer.md`, “Independent probes”) observed empty-both sides get required-ID errors plus the pair finding, and warned that suppressing the R62 warning could lose repair guidance. The R69 axis adjudicator rejected that broad proposal; it did not adjudicate the narrower R70 condition.
- `.shokunin/lore/corpus/fixtures/r62-malformed-side/contradictions.json` has identical nonempty IDs `tarin-envelope-observation` and identical invalid fields `bogus`. Its timeline is malformed. The R62 reviewer and verifier (`reports/r62-reviewer.md`, “Independent fixture replay”; `reports/r62-independent-verifier.md`, “Candidate behaviors observed”) record the loader error, two field errors, and retained pair warning. Since both IDs pass the nonempty-string predicate, the R70 gate as declared preserves this warning; field invalidity must not suppress it.
- Valid-identical and valid-distinct controls are specified in the R69 reviewer, which records focused baseline probes, and `.shokunin/lore/reports/r69-fixture-scout.md` proposes a matched matrix. The latter is a design report, not proof those cases exist as committed dedicated fixtures. R69's independent verifier (`reports/r69-independent-verifier.md`) reports its baseline matched probes and explicitly says no candidate was present or validated.

## Limits

This identifies the exact branch and minimal event-ID predicate from supplied code/declaration. It does not establish the calibration value of removing any finding, a candidate result, full fixture regression preservation, or user repair behavior. In particular, R69's empty-both observation supports that the current comparison has no supplied event-ID target there, while R62 is a counter-control that must retain the finding. No source-text, fictional-event, story-contradiction, canon, chronology, rights, or game-mechanics claim follows. No files other than this report were changed by me.
