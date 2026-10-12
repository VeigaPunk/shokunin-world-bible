# Round 13 independent reviewer — actor occupancy guard

## Scope and evidence

Read-only review of the active guard in `.shokunin/lore/corpus/fixtures/check_bible.py`, raw fixture pair and run outputs, round-13 declaration/clarification in `.shokunin/lore/LOG.md`, and `corpus/fixtures/README.md` plus `corpus/knowledge/2026-10-12-lore-decision-table.md`. I made no code or fixture edits. Disposable probes were under `/tmp/r13-review-2_czkl8o/`.

The relevant implementation builds `entity_id_counts` from `data['entities']` (only rows passing required-field/type/nonempty checks), reports timeline dangling references, and then does occupancy only under `if actor_id_count == 1:`. For counts >1 it adds per-event `ambiguous actor entity`; for count 0 it retains per-event dangling output and skips occupancy. This is a count of required-field-screened rows, not necessarily character-kind rows.

## Replay and raw pair

I extracted baseline checker commit `97f766762ac78ab6bcf6523aadbd2ffa92d4f4f5` to `/tmp/r13-review-baseline.py`; ran baseline and working checker against all **28** fixture directories. The only output/exit difference is the intended `r13-missing-actor` diagnostic removal; stdout/stderr/exit match for the other 27. The pair's raw runs at `corpus/live/runs/20261012T180109Z/r13-{missing,unique}-actor.txt` show current exit 1: missing has two dangling findings and `2 violation(s)`, unique has `double-booked 'mira' at tick 7 ...` and `1 violation(s)`. Executor report records baseline missing output exactly, including the suppressed line `timeline[1]: double-booked 'unlisted' at tick 7 in timeline[0] ('harbor') and 'tower'`, and confirms baseline unique/current unique retain the same diagnostic. This matches my replay.

## Independent schedule and candidate probes

Disposable current-checker probes (all exit 1; source copied from `r12-unique-actor`; no repo inputs changed):

- `/tmp/r13-review-2_czkl8o/mixed-missing-unique`: two same-tick different-place `unlisted` events plus two such `mira` events. Current output keeps both `unlisted` dangling findings, suppresses only that ID's occupancy assertion, and emits `timeline[3]: double-booked 'mira' at tick 7 in timeline[2] ('harbor') and 'tower'`.
- `/tmp/r13-review-2_czkl8o/bad-kind-count-one`: a single required-field-complete entity with `kind: "unknown-kind"` and two events. It reports `entities[3].kind: unknown kind 'unknown-kind'` **and still double-books** `mira`. Thus `actor_id_count == 1` is not “one valid character”; clarify as one required-field-screened entity row. This matches round-13 post-scout clarification and README/decision-table language.
- `/tmp/r13-review-2_czkl8o/malformed-extra-candidate`: one complete `mira` plus a duplicate candidate missing `name`, with the same event pair. The malformed row yields `entities[4].name: required nonempty str`, is excluded from `data['entities']` and count, and the remaining single screened row still double-books. This is consistent with the count scout.

## Calibration challenge / judgment

The suppression does hide a *possible* definite finding if the two missing-ID events really do denote one actor in conflicting places. But baseline's definite `double-booked 'unlisted'` also attributes both unresolved references to the same actor without evidence. The inputs cannot distinguish one omitted/mistyped actor from two actors sharing a missing token. Therefore withholding that assertion is defensible calibration, **only** if described as “not assessed as a definite same-actor collision / possible conflict remains unassessed,” not “no conflict,” “compatible,” or proof that the events concern different actors. The retained dangling diagnostics and raw events plus the explicit README and decision-table caveat adequately preserve the uncertainty; no new warning appears necessary for this bounded move. The one-event case naturally has no pairwise collision to assert.

README states missing-reference behavior and explicitly says possible conflict is unassessed; the decision table row says the same. LOG clarification accurately says kind may be semantically invalid yet counted, malformed required-field candidates excluded. Scope remains local occupancy only; other diagnostics still run. No canon or source truth is implied.

**Reviewer finding:** the one-line guard does what the declared calibration change claims, with the above bounded interpretation. The exact-output regression is limited to the intended missing-ID fixture. No evidence of collateral change or a reason to reject this move.
