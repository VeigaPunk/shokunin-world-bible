# Round 37 critic — coverage claim

## Finding

The narrow diagnostic claim is plausible but not yet demonstrated as *new semantic coverage*. `r9-dup-low-high` and `r9-dup-high-low` already exercise duplicate timeline IDs plus an ambiguous dependency on `same`; the checker reports a duplicate-ID finding and refuses to resolve that dependency (checker lines 49–50, 60–62, 188–204). Thus duplicate identifier ambiguity itself is not new. The potentially distinct surface is a contradiction-ledger endpoint that targets a duplicated timeline ID: checker lines 92–94 add an endpoint-local “expected exactly one timeline event” finding and `continue`, so it does not use the `events` dictionary’s last-row value at lines 58 and 95.

## Risks / limits

- If the duplicate row is introduced by cloning Tarin’s event verbatim, it can add unrelated/overlapping collateral findings (including a duplicate timeline ID at line 49 and potentially a double-booking at lines 228–250, depending on row values). Inventory the complete output against control; do not describe only the expected two diagnostics as the whole result.
- The ledger is itself already a pointer, not a truth adjudicator: r35 says its `why` is an editorial apparent conflict, not checker-proven contradiction or canon verdict (`.shokunin/lore/corpus/fixtures/r35-bell7-conflict/contradictions.json:1–22`). Duplicate Tarin IDs make `claim_a`’s endpoint non-unique; they do not make Tarin’s prose false, establish Sella’s account, or settle the accounts. This distinction is also explicit in the round-37 declaration (`.shokunin/lore/LOG.md:594–599` round 37 section): endpoint ambiguity is not a canon winner or testimony falsity.
- `events = index('timeline')` overwrites a duplicate key with the later row (checker lines 45–50, 57–62). The ledger loop guards on `event_id_counts != 1` before lookup (lines 92–95); therefore the local endpoint error is a useful guard diagnostic, but not proof that all other consumers of the same ID are safe. Check dependency diagnostics too if the duplicated event is referenced from `depends_on`.

## Falsifiable check

Run `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r35-bell7-conflict` as control, then the proposed single-duplicate variant. Record full stdout/stderr/exit for both. A successful narrow probe has (1) the control clean; (2) variant duplicate timeline ID at the actual duplicate row; (3) `contradictions[0].claim_a.event_id: expected exactly one timeline event 'tarin-envelope-observation'`; (4) the unique `claim_b` endpoint produces no corresponding endpoint error; and (5) all additional output explicitly enumerated and explained (not omitted). Confirm by inspecting source lines 92–100 that the ambiguous endpoint skips source lookup, and verify the r9 fixtures already cover duplicate-ID / ambiguous-dependency behavior. If the endpoint-specific finding does not appear, or the claimed novelty is framed as duplicate IDs generally, the coverage claim is falsified. If only that distinct endpoint diagnostic is established, retain the narrow wording “ledger endpoint ambiguity diagnostic,” not “new contradiction detection” or “new testimony coverage.”

## Evidence references

- Checker duplicate index/count behavior: `.shokunin/lore/corpus/fixtures/check_bible.py:45–62`.
- Contradiction endpoint uniqueness guard and source handling: `.shokunin/lore/corpus/fixtures/check_bible.py:77–105`.
- Dependency handling of duplicate IDs: `.shokunin/lore/corpus/fixtures/check_bible.py:188–204`.
- Timeline duplicate-ID and occupancy handling: `.shokunin/lore/corpus/fixtures/check_bible.py:228–250`.
- r9 duplicate order controls: `.shokunin/lore/corpus/fixtures/r9-dup-low-high/timeline.json:1–29`; `.shokunin/lore/corpus/fixtures/r9-dup-high-low/timeline.json:1–29`; unique control `.shokunin/lore/corpus/fixtures/r9-unique-control/timeline.json:1–20`.
- Two-sided Bell-7 ledger and its express non-canon scope: `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/contradictions.json:1–22`.
- Declared round-37 bounded claim and caveat: `.shokunin/lore/LOG.md: Round 37 declaration` (section is headed “Round 37 — 2026-10-13T02:14:17.789304+00:00”).
