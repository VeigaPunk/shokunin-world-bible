# Round 59 non-author reviewer — duplicate-member calibration

## Verdict

**PASS — MATERIAL CALIBRATION, narrowly.** The candidate addresses an observed order-dependent input decision: on the matched tick-1/empty-dependency pair, the pre-candidate last-wins checker reports double-booking for `harbor` then `tower`, but CLEAN for `tower` then `harbor`. The candidate rejects both with the same file-level duplicate-member diagnostic, rather than selecting either place. The equal-tick unique control remains independently checked and reports the expected double-booking. This improves calibration of the checker as an input validator; it does not establish which value or fictional location is true. Depth and coverage are unchanged.

## Independent replay and code review

I inspected the candidate diff, all four `r59-*` fixture directories, and current README. I ran the checker from repository root on both swapped duplicates, the corrected unique control, the nested duplicate, and all five r5 controls. Observed results match the executor report: both duplicate timeline files exit 1 with only `timeline.json: duplicate object member 'place_id'; cannot load JSON`; the unique control exits 1 with one `timeline[1]` double-booking; the nested case exits 1 with the duplicate `entities.json` diagnostic plus six dangling-reference findings in relations/timeline. All five r5 cases retain their recorded primary diagnostic and one-violation count (parser text remains environment-specific).

The implementation is a small recursive `object_pairs_hook`: any repeated member at any nesting level aborts loading that whole table, with a deterministic member/file diagnostic and no arbitrary partial object. This covers nested claim and ledger objects without inventing a row pointer. The README accurately states this newly chosen policy and the consequences. The checker does not assert source-text support or canon.

## Cascade and format-policy assessment

The nested probe is a real cost: unloading `entities.json` causes six dependent dangling-entity messages, which could be misread in isolation. Here the cascade is bounded, deterministic, explicitly demonstrated and documented as a consequence of unloaded rows, not proof of absence. It is not enough to outweigh the demonstrated clean-versus-violation flip. I do not recommend a broader cascade-suppression change: that would hide existing cross-file diagnostics and expand this narrow candidate. The README should remain clear that this is a new input policy, not a pre-existing documented format rule; neither r5 nor the older schema docs resolve repeated-member semantics. Reject-all is a defensible ambiguity policy, but its adoption is policy, not an inevitable JSON-schema consequence.

The r5 matrix is not harmed: missing file, invalid syntax, wrong top-level shape, non-object row and invalid citation still produce their recorded classes/counts. It does not test duplicate members and should not be cited as precedent for that rule. The executor's pinned 95-case raw stdout/stderr/exit replay remains unverified in its report; zero duplicate-member files among 474 active JSONs is reassuring but not a substitute for that replay. Treat regression preservation as a separate unresolved validation limit, not evidence against this specific calibration result.

## Falsifier and per-axis limits

Falsifier: an authoritative input contract or demonstrated supported producer convention says duplicate object members are intentionally legal and last-wins, or a pinned old-case replay reveals material collateral changes beyond this new policy. A material adverse cascade on ordinary unique-key inputs would also overturn this verdict. No source truth, chronology, canon, rights, or permission claim follows.

- **Calibration: improved** — order-only duplicate ambiguity no longer flips the checker between violation and CLEAN.
- **Depth: unchanged.**
- **Coverage: unchanged.**
- **Harm:** bounded nested unload cascade observed; documented and acceptable for this narrow candidate, subject to pinned replay.
