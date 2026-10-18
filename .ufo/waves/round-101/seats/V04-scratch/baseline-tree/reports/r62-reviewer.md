# Round 62 independent reviewer — timeline availability

## Verdict

**PASS, narrowly, for material calibration; depth and coverage unchanged.** The candidate corrects a specific certainty error in a ledger consumer: after the entire timeline index fails to load, “expected exactly one timeline event” looks like a membership result even though no index was available. The replacement is per-pointer and explicitly unassessable, retaining affected locations. This is more than borrowing the r60/r61 status pattern: those rounds gated entity/source-derived membership; this tests the distinct timeline event-ID ledger consumer. The r7/r39 prior does not establish this failure state. This verdict concerns supplied-table diagnostics only.

## Independent fixture replay

Ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>` on all ten `r62-*` directories. The eight core fixtures share byte-identical `sources.json`, `entities.json`, `relations.json`, and `contradictions.json` (one SHA-256 per file across all eight); only timeline state differs, with `r62-missing` containing exactly four JSON files and no timeline file.

- Missing, malformed JSON, duplicate-member JSON, and nonarray each retain their direct loader/shape diagnostic and replace the two ledger `expected exactly one` findings with two pointer-specific `cannot assess event …: timeline.json unavailable` findings. Each exits 1.
- Loaded empty retains both existing exact-one findings (2 total); loaded partial retains only the absent `sella-bell7-presence` finding (1 total). This preserves distinction between unavailable and successfully loaded index.
- Loaded duplicate retains duplicate-ID, dependent ambiguity, the independent ledger `claim_b` no-resolvable-source finding, and unknown source (4 total). It does not pretend duplicate IDs resolve uniquely.
- Matched `r62-loaded` retains the r39 loaded-event source behavior: `claim_b` no-resolvable-source and timeline unknown-source (2 total). The ledger IDs do match timeline IDs; this directly corrects the pair-scout's earlier unmatched-r39 caveat, as the parent correction noted.
- Unavailable `r62-malformed-side` retains both invalid-field findings and same-reference finding, and emits no unassessable pointer because each side fails field validation first. The valid sides in unavailable core cases receive the pointer-specific status only after local ID/field validation. Thus this replacement does not bypass those validations.
- `r62-independent` retains the loader error, both valid pointer statuses, and independent dangling relation endpoint.

All ten exit 1 as expected due to these deliberate violations. Whole-file timeline failure supplies no timeline rows; no dependency findings are invented. The control table exercises parse/shape variants, but does not separately test an unreadable file or malformed timeline rows within a successfully parsed array; the declared behavior and code leave decoded arrays available over admitted rows.

## Diff and scope audit

The checker diff is localized: initializes `timeline_available=False`, sets it only when the timeline table is loaded as an array, and gates the ledger membership lookup after local event-ID and field validation. Loaded index lookup and subsequent source-status check are unchanged. The README describes the same boundary. I found no indication that source/entity/relation checks, claim distinctness, or loaded timeline dependency behavior is gated by this flag. No speculative dependency cascade is introduced.

The executor reports, and this review's direct candidate runs corroborate the fixture outputs, that all 115 old fixture tuples and all 574 old JSON byte contents match the pinned r61 baseline. I did not independently rerun the entire 115-case historical suite in this leaf review; treat that preservation claim as executor evidence pending the separately assigned independent verifier, not as my independent replay. This review also makes no claim to full corpus path inventory preservation.

## Materiality, cost, and falsifiers

The delta is not fewer failures or a clean status: the broken-table diagnostic remains, and each affected valid ledger pointer remains visible. It removes the unsupported implication that a zero match was observed in a loaded index while preserving a repair/recheck location. That is a bounded but meaningful calibration improvement beyond the known general availability-vs-empty principle. The replacement lines are somewhat longer and repeat the table-unavailable status per pointer; this adds output volume for large ledgers. That cost is justified here because it preserves the exact affected locations rather than silently withholding hints. No observed independent finding was lost.

Falsifiers: a full verifier finds old fixture bytes/output changed; any unavailable case omits its primary loader error or valid pointer location; local malformed ID/field or same-reference checks disappear; independent table diagnostics disappear; loaded empty/partial or duplicate behavior changes; or loaded matched r39 source-status behavior changes. If full-ledger volume makes repeated status materially unmanageable, reconsider presentation without reverting to an absent-event claim.

**Axes:** calibration materially improved; depth unchanged; coverage unchanged. Limits: no source truth, world/event existence, chronology, canon, ownership, license, permission, or rights conclusions. No edits beyond this reviewer report.
