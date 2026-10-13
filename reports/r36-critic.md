# Round 36 critic — controlled date near-miss

## Falsification finding

The proposed r36 near-miss is a useful calibration contrast only if its sole changed prose actually makes the dates differ while leaving the five JSON tables unchanged. The working tree currently has no `r36-*` fixture or r36 reports (`find .shokunin/lore/corpus/fixtures/r36-*` yielded none); this report therefore evaluates the declared design against r35, not an implemented r36 artifact. Do not claim the contrast has been demonstrated until a reviewer inspects the final pair.

## Evidence

- `.shokunin/lore/LOG.md`, Round 35 closure: Tarin reports Sella at Harbor during a source-claimed sole Bell-7 on Embermonth 7, year 12; Sella reports Tower presence throughout that same ringing and no Harbor presence. Conflict is conditional and unresolved; dates/uniqueness are source claims, not authenticated chronology.
- `.shokunin/lore/reports/r35-reviewer.md`, “Blocking ambiguity under the LOG policy”: each “day of this note” could differ; same label or tick did not establish same occasion. This is the relevant precedent: date identity must be read from source text, not the label/tick.
- `.shokunin/lore/reports/r35-remediation-reviewer.md`, “Shared occasion and report conflict”: corrected excerpts explicitly name Embermonth 7, year 12 and the sole ringing; the incompatibility remains conditional on person/place alignment.
- `.shokunin/lore/reports/r35-independent-verifier.md`, “What validation does and does not establish”: checker validates structure, not shared date, semantic incompatibility, identity, source reliability, or truth.
- `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/tarin-note-excerpt.md:1` names Embermonth 7, year 12. `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/sella-bell7-note-excerpt.md:1` presently names the same date and same sole ringing.
- `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/timeline.json:13-22` encodes both event descriptions at tick 3, but tick is not a date or proof that the accounts share an occasion. The Sella event is still structurally tied to `sella-bell7-note`.

## Risks and limits

1. A true controlled near-miss requires the *only* source-text mutation to replace Sella's date with Embermonth 8, year 12. If Tarin remains on the seventh, the excerpts no longer establish same occasion; this does not establish that either report is false or that Sella was at Harbor on the seventh.
2. Five JSON tables byte-identical means the structured Sella event description and ledger rationale will continue to say/assume the seventh-day occasion while the cited excerpt says eighth. That is the intended source/record mismatch to expose, not corroboration. The excerpt citation does not resolve the inconsistency.
3. A clean checker run only indicates structural/citation validity under its rules. It cannot certify source entailment, resolve conflicting dates, prove semantic conflict, or establish canon.
4. The contrast is not novel merely because another fixture has a different date: it is a falsifiable calibration challenge to whether a reviewer notices that the source date and unchanged structured record diverge. Avoid calling the JSON “wrong” as a factual/canon finding; it is mismatched to that excerpt.
5. No conclusion about envelope contents, ownership, Blue Seal/carbon/route-strip association, rights, or AI-training permission follows.

## Falsifiable check

For the final r36 artifact, compare the five JSON byte streams against r35 and require exact equality; diff both excerpts and require the sole textual change to be Sella's date, seventh to eighth day, with Tarin still on the seventh. Inspect `timeline.json` and `contradictions.json` to confirm they are unchanged and thus still carry seventh-day rationale. Then ask a non-author reviewer: do these two excerpts establish the same Bell-7 occasion? Expected calibrated answer: no—the explicitly stated dates differ, despite unchanged tick 3, event description, citation, and ledger `why`. The checker may remain clean, but that is not source entailment or canon. If any additional source-prose clause changes, the JSON differs, or the reviewer infers either account false/true or selects canon, the controlled calibration claim fails.
