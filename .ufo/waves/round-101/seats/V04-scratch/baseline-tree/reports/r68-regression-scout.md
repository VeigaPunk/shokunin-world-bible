# Round 68 regression scout — fixture inventory and replay plan

## Scope and baseline

Read-only inventory for the Round 68 declaration in `.shokunin/lore/LOG.md` and active checker `.shokunin/lore/corpus/fixtures/check_bible.py`. The declaration names baseline HEAD `c3b090fb6df57bbe8f6e2680b24045c2db33e4fe`; `git rev-parse HEAD` in this checkout matches. `git status --short .shokunin/lore/corpus` was empty at inspection, so corpus fixtures/checker were unchanged. No fixture or checker behavior was edited for this report.

The active dependency path is the loop in `check_bible.py` after `dependencies = row['depends_on']`: non-string members cause `expected event-id strings` (one list-local error); each string is then checked for self/repetition and event index membership, with missing ID reported `unknown event ...`. There is no blank/whitespace test at that point. The common required-field validation does strip-check top-level string fields, but `depends_on` elements are not covered by it. Thus the proposed distinction is structurally plausible at baseline, not yet a result about materiality.

## Fixture inventory

At baseline HEAD there are **130** fixture directories and **709** files under `corpus/fixtures` (one checker, one README, 125 five-table directories plus five four-table directories that omit `sources.json`). This matches the checked-out inventory. Files in each normal fixture are `sources.json`, `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json`; missing-source cases intentionally omit the source ledger. `README.md` documents the active fixture conventions and run commands. There are no Round 68 fixtures at baseline.

For this change, the most diagnostic existing coverage is:

- `.shokunin/lore/corpus/fixtures/r20-valid-order/`: valid nonempty dependency control; clean.
- `.shokunin/lore/corpus/fixtures/r20-valid-inversion/`, `r20-valid-equal/`: nonempty valid-ID inversion/equality behavior (the equal case also triggers occupancy).
- `.shokunin/lore/corpus/fixtures/r20-negative-prereq/`, `r20-negative-dependent/`, `r20-both-negative/`, and `r20-mixed-edges/`: negative tick guards and the rule that tick comparison is gated by nonnegative ticks.
- `.shokunin/lore/corpus/fixtures/r22-valid-order/` and `r22-clean-inversion/`: compact Round 22 valid/inversion pair, with fixture text explicitly limiting interpretation to input fields rather than source-text chronology.
- `.shokunin/lore/corpus/fixtures/r22-self-repeated/`: self/repeat behavior plus non-string input (not a minimal control).
- `.shokunin/lore/corpus/fixtures/r22-malformed-only/`: non-string-only control; `.shokunin/lore/corpus/fixtures/r22-unknown-mixed/`: non-string plus ordinary nonempty unknown ID, but not a clean isolated unknown case because of its `null` member.
- `.shokunin/lore/corpus/fixtures/r8-deps-distinct/` and `r8-deps-anomalous/`: older valid versus duplicate/self dependency pair.
- Wider fixture regression set: 130 directories total, including original round fixtures and later probes. `.shokunin/lore/corpus/fixtures/r67-*` cover claim source fields, not timeline dependencies; include them in whole-suite replay.

I ran current baseline CLI on the focused cases above. Observed raw outcomes: `r20-valid-order` and `r22-valid-order` clean exit 0; `r20-valid-inversion` and `r22-clean-inversion` report timeline inversion; `r20-valid-equal` reports double-booking and inversion; negative tick fixtures retain nonnegative-tick findings (and `r20-mixed-edges` retains inversion for its separate valid prerequisite edge); `r22-malformed-only` yields only `expected event-id strings`; `r22-unknown-mixed` yields that plus `unknown event 'missing'`; `r22-self-repeated` retains type, self, repeat, and inversion findings; r8 anomalous retains duplicate, self, and inversion findings while distinct is clean. Exact output should be captured fresh for comparison, not inferred from these summaries.

## Non-author replay plan

1. Freeze baseline inputs from declared HEAD, not a later working tree: archive the 130 baseline fixture directories and checker from `c3b090fb6df57bbe8f6e2680b24045c2db33e4fe` (or otherwise prove all original fixture bytes are unchanged). Enumerate directory paths from that archived fixture tree, rather than maintaining a hand list.
2. Before using candidate code, run archived HEAD checker against each archived directory from the same repository-root working directory. For every case save the exact command/path, raw stdout bytes, raw stderr bytes, and process exit status as the baseline tuple. Preserve the raw artifact for non-author comparison.
3. Run the candidate checker against the exact same archived input bytes and same paths/cwd. Compare each tuple byte-for-byte. Report count, mismatched fixture paths, and the actual byte/exit deltas; do not count only pass/fail or normalize away path-bearing loader errors.
4. In addition to the 130 original cases, run the proposed matched probes once they exist: a clean valid dependency control and otherwise-identical dependency values `""`, whitespace-only (e.g. `"   "`), and a nonempty absent ID. Each probe should have valid table structure and source IDs so dependency is the only intended variable. Ensure the two timeline rows have distinct valid ticks/locations (avoid accidental occupancy), and keep both target/dependent ticks nonnegative so tick gates do not mask the behavior. Require the blank cases to produce the stated field-local required-nonempty diagnostic, while the nonempty unknown case keeps the existing unknown-event diagnostic; assess preservation of clean/unknown results and absence of spurious self/repeat/inversion diagnoses.
5. Explicitly inspect post-change output for `r20-*`, `r22-*`, and `r8-*` controls above. This confirms that the existing policy for valid unknown, self, repeat, inversion, equal-tick, negative-tick, and non-string inputs was not displaced by the new blank guard. Run full 130-case tuple diff as the actual baseline regression evidence.
6. Keep report wording to supplied JSON structure, checker diagnostics, and the fixture's local tick convention. A missing nonempty ID is an index lookup result, not proof that a fictional event did or did not happen; no source-prose, truth, canon, rights, or game-mechanics verification follows from this replay.

## Limitations

This scout did not create Round 68 fixtures, run a candidate implementation, produce an archived raw tuple corpus, or perform independent candidate replay. The focused current-baseline commands are observations from the declared baseline only. Whole-suite behavior, matched-case control quality, candidate collateral, and the independent replay claim remain for later verifier evidence. The inventory is file/directory count, not a semantic audit of every fixture. No admission or canon conclusion is offered.
