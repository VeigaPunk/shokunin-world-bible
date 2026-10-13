# Round 69 scribe — same-reference ledger check boundary

## Active behavior and decision table

The Round 69 declaration proposes a calibration check: compare claim references only when both sides have a usable event ID and an allowed assertion field. This is a proposed move, not a report of an implemented candidate. At this inspection the active checker still compares `.get()` values on any two dictionary sides after the side-validation loop.

| `claim_a` / `claim_b` inputs | Current active checker behavior | Bounded interpretation |
|---|---|---|
| Both dictionaries have the same nonempty string `event_id` and same allowed `field` (`place_id`, `tick`, `depends_on`) | Adds `claim_a and claim_b references must differ` (`check_bible.py:139-143`). | Same input pointer is rejected; this says nothing about whether the claims contradict in the story. |
| Both dictionaries have the same malformed/unsupported values (for example the same unsupported field) | Emits each side’s field diagnostic and also the same-reference diagnostic. | The extra finding is currently based on matching raw `.get()` values, not two valid references. |
| One or both sides are not dictionaries, or one side lacks a valid event ID / allowed field | Emits the respective side-local shape/field error. Non-dictionary sides are skipped by the pair check; dictionary sides with missing values can still compare equal via `.get()`. | A malformed pointer is not a usable event-field reference. |
| Structurally valid sides differ by event ID or field | No same-reference finding. Other pointer checks may still report timeline availability, event cardinality, or source-ID status. | Different input pointers only; no semantic independence or contradiction is proven. |

## Evidence

- `.shokunin/lore/LOG.md:1212-1215` declares the calibration hypothesis and exact scope: only suppress the same-reference finding unless both sides have a nonempty string event ID and an allowed field; retain side-local diagnostics and valid identical-reference behavior. It requires matched malformed-both, malformed-one, valid-identical, and valid-different controls plus inspection of 130 prior fixture outcomes. No r69 outcome is presumed here.
- `.shokunin/lore/corpus/fixtures/check_bible.py:111-126` defines the allowed fields and independently validates each dictionary side. Lines 139-143 perform the pair comparison using dictionary `.get()` equality, without checking the validated shape. The check occurs after the loop, regardless of whether each side passed its own checks.
- Reproduced active control: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r62-malformed-side` exits 1 with two unsupported-field findings **and** `claim_a and claim_b references must differ`. Raw input: `.shokunin/lore/corpus/fixtures/r62-malformed-side/contradictions.json` has the same event ID and same unsupported `bogus` field on both sides. `reports/r62-reviewer.md:15` and `reports/r62-axis-adjudicator.md:20` likewise record this existing behavior; the adjudicator says old and candidate were identical for this case, so this is baseline evidence, not a prior accepted fix.
- Valid comparison controls: `.shokunin/lore/corpus/fixtures/contradictions/contradictions.json` contains distinct allowed event-field pairs and emits no same-reference diagnostic in the verified run; `.shokunin/lore/corpus/fixtures/contradictions-ledger-malformed/contradictions.json` has a malformed pointer on one side but different references and emits no same-reference diagnostic. Both commands and outcomes are recorded below.
- The fixture contract in `.shokunin/lore/corpus/fixtures/README.md:45-54` describes ledger references and explicitly limits the checker to pointer/required-text validation; it does not establish a semantic contradiction. `reports/r62-scribe.md` distinguishes ledger shape and same-reference checks from timeline availability. `reports/r39-scribe.md` limits source-ID status to structural linkage, not support or authenticity.

## Replayed commands

From repository root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r62-malformed-side
# exit 1; two invalid-field findings plus same-reference finding (4 total)
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions
# exit 1; three existing fixture violations, no same-reference finding
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions-ledger-malformed
# exit 1; malformed event pointer plus three existing fixture violations, no same-reference finding
```

## Limits

These are diagnostics about the supplied JSON ledger’s structure and pointer equality only. They do not establish that either assertion is true, that the claims conflict, that source text supports a claim, or what is canon. Removing a same-reference diagnostic for malformed pairs would not validate either side; the side-local malformed findings must remain. This report documents active behavior and evidence only; it makes no candidate, verdict, or source-truth claim.
