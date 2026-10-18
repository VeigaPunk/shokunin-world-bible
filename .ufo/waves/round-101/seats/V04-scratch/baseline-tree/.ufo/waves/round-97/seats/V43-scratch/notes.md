# V43 notes (whole-claim-replica-2)

## Deliverables
- Report: .ufo/waves/round-97/seats/V43-whole-claim-replica-2.md
- Core obligation: construct reconciliation/blame readings over delivered r97 bytes; report constructibility.

## Checks (status)
- [x] r96 repair diff vs committed baseline f3e09f9: exactly 2 lines (:44 delimiter 8->7 cells; :50 stale "new relation" sentence replaced). Data rows 18/18 byte-identical.
- [x] r96 receipts unchanged (prelim): support_check + map_obligations outputs identical baseline-map vs repaired-map; R4 before/after snapshots diff clean.
- [x] r97 counts: entities 5 / relations 1 / timeline 6 / sources 6; independent obligations 17; census 171; check_bible CLEAN; inherited parsed-equal True; r96 excerpts prefix True; JSON seam `,\n  {`.
- [ ] R5 r97 README/map frozen; R1-R6 reports landed
- [ ] Gate receipts at freeze (check_bible, support_check, map_obligations; exit codes via PIPESTATUS)
- [ ] Whole-proposition trace lines 48-51 -> timeline#/5, sources#/5, map J17, README
- [ ] Lexical scan at freeze (scan.py)
- [ ] Structural scan (done prelim: no same-actor same-tick diff-place pairs; all depends_on resolve backward)
- [ ] Schema probes (probes.py): reconciliation / blame / contradiction rows pass check_bible? => restraint editorial
- [ ] Map row inheritance J01-J16 vs r96 (normalized)
- [ ] Cross-check producer reports

## Preliminary observations
- New note: L48 receipt; L49 "I hold to my own account; both accounts stand unresolved."; L50 "no accusation against Evin, and I select no winner between us."; L51 "no reconciliation, no new duty, no obligation beyond this crossing."
- Closest reconciliation constructions to test: receipt-as-acceptance; acknowledgment-as-recognition; return to Chalk Stair; "between us"/"both accounts" shared-frame.
- Closest blame constructions: inherited "Evin did not come" (r95, bounded); "I hold to my own account" as implicit dispute; no positive blame tokens in new bytes.
- sources.json#/5 reliability note: "not evidence of a resolution, a reconciliation, an accusation, a winner between the accounts, a continuing duty, or an external historical fact."
- timeline#/5 description: "At the Chalk Stair at tick 13, Aru reports receiving Evin's response and states that both first-person accounts stand unresolved; the note asserts no accusation, no reconciliation, no winner between the accounts, and no new duty beyond this crossing."
- Note: timeline#/5 description does NOT record "I hold to my own account" clause -> trace note candidate (clause without JSON counterpart), check map J17/README handling.
