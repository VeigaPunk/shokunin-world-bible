# Round 64 row-scout — rejected entity-row ID hypothesis

## Verdict: NO-GO on the stated material calibration claim

**Observed path:** `.shokunin/lore/corpus/fixtures/check_bible.py:65-76` validates each object and appends it to `data[section]` only when every required field passes. A rejected row's string `id` is not retained in a raw-ID index. `index()` at `:78-84` and the entity counts at `:157-160` use admitted rows only. `entities_available` at `:58-60` means top-level array successfully loaded, not that every row passed schema.

## Temporary probes (no repository fixture edits)

I copied `consistent/` to temporary directories and changed only `entities.json`.

- Existing valid `mira` row removed, replaced by `{"id":"mira"}`: checker emitted four required-field errors and three `dangling entity 'mira'` findings (relation from, two timeline actors). This matches current filtering/index behavior.
- Same valid-absent control without malformed row: emitted the same three dangling findings.
- Malformed row without an ID (`{"kind":"thing"}`) plus valid-absent control: four row schema errors and the same three dangling findings.
- Valid `mira` row plus an additional schema-rejected `{"id":"mira"}`: only four row errors, no duplicate/ambiguous-ID diagnostic; checker exited CLEAN in this probe. This is a separate gap: because the invalid row is excluded, it cannot establish duplicate ambiguity either.

These probes establish input-index behavior, not fictional entity existence. The candidate policy—retain usable raw IDs as “uncertain” while keeping invalid rows from qualifying for kind/holder/occupancy—would at minimum replace the three dangling findings in the first case with a distinct cannot-assess status. That distinction is plausible, but the experiments do not establish that it materially helps an operator: current output already points to the rejected row and identifies its missing required fields, and these dangling messages may be useful pointers to check whether the bad row was intended to define the referenced ID.

## Prior-art and harm check

R60 explicitly distinguishes whole-table availability from loaded arrays, and its adjudicator notes the remaining boundary: rejected malformed rows are not part of lookup, so an ID present only in one can still yield dangling. This is an acknowledged limitation, not a demonstrated defect repair should suppress. R16–18 concern occupancy comparison with resolved/ambiguous references; they do not establish benefit for raw rejected IDs. R56 rejected extra holder diagnostics for ambiguous IDs because they added no material operator benefit beyond duplicate-ID and withheld-chain findings. The proposed “cannot assess” status similarly risks adding noise or obscuring a repair pointer; without a consequential matched case or consumer evidence, no material calibration improvement is proved.

## Falsifier / revisit condition

GO would become supportable if a matched, pinned replay shows that `dangling` on a schema-rejected raw ID is materially misleading to a repair operator, while a location-specific `cannot assess … matching entity row invalid` preserves a useful correction path and does not mask a valid absent-ID finding, valid duplicate-ID ambiguity, or dependent kind/holder/occupancy constraints. Required controls: valid present, valid absent, malformed matching ID, malformed different/missing ID, valid duplicate, and unavailable `entities.json`; exercise relation endpoints, timeline actor/place, and provenance holders. The malformed row must remain ineligible as a unique entity or kind witness. Until then: **NO-GO**, not a claim that the fictional entity exists or does not exist.

No world/canon/rights inference. No checker, fixture, README, LOG, or commit changes.
