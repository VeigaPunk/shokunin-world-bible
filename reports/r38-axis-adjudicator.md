# Round 38 — final non-author axis adjudication

**REJECT the proposed axis move.** The fixture pair is valid and reproducible, but no axis materially improves over prior evidence. A committed Bell-7 `claim_b` instance does not by itself create new coverage of the ledger source-ambiguity path already exercised by the round-7 reviewer's temporary `claim_a` probe. No axis is harmed; the admission rule still requires at least one improvement.

| Axis | Verdict | Reason |
| --- | --- | --- |
| Coverage | **unchanged** | Round 7's independent reviewer duplicated `archive-ledger`, made the uniquely identified `departure` event cite it, and added a two-sided ledger reference. Its complete probe included `contradictions[0].claim_a.source_id` ambiguity and an affected timeline citation. The current checker iterates `('claim_a', 'claim_b')` through the same event-count and source-status branch (`check_bible.py:77–100`). R38 duplicates `sella-bell7-note` and obtains the same class of ledger-side ambiguity on `claim_b`, plus its timeline consumer. Both ledger event pointers are unique here, but the r7 probe already reached the source check after its event pointer resolved. Bell-7 subject matter, opposite side, cleaner collateral, and a committed clean/negative fixture improve repeatability and presentation, not materially distinct branch or input-boundary coverage. R31 similarly credited prior relation ambiguity instead of calling the general mechanism new; r37's distinct event-ID cardinality guard is not this source-ID status branch. |
| Depth | **unchanged** | All nine inherited clean-control files are byte-identical to r35. The negative copies one existing source metadata row; excerpts, events, ledger rationale, and manually mapped accounts add no source or inference. |
| Calibration | **unchanged** | The reviewer, verifier, README, and complete output correctly separate identifier ambiguity from testimony, authenticity, textual support, semantic conflict, rights, and canon. That preserves the existing boundary, without a new calibration distinction. No harmful claim was found. |

## Independent evidence

I read the r38 LOG declaration and its explicit r7 prior-art correction, r7 reviewer temporary probe, r31 and r37 adjudications, r35/r38 fixture tables and excerpts/maps, fixture README, checker, and r38 critic/executor/reviewer/verifier. I extracted the fixture tree and checker from pinned baseline `ceb6ea7c2c609dfc332218ceb14f04994f5c28c6` outside the repository. For all **90** prior fixture directories I ran root-relative `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>` from both archived and current roots and compared the raw `(exit status, stdout bytes, stderr bytes)`: **90/90 identical**. Every baseline fixture JSON path remains byte-identical: **449/449**. This verifies regression preservation, not novelty or universal checker correctness.

The `r38-ledger-source-unique/` control matches r35 across all nine inherited files. The negative matches its control across eight files; only `sources.json` changes, retaining four original rows and appending an object-identical Sella row at index 4. `sella-bell7-note` has count one versus two. Each of the four timeline IDs occurs once in both, and unchanged ledger `claim_a=tarin-envelope-observation` and `claim_b=sella-bell7-presence` resolve uniquely. Tarin's source remains unique. No second witness was added.

Independent complete checker replay, with empty stderr in each case:

```text
r38-ledger-source-unique: exit 0
CLEAN: schema, citations, relations, timeline; 0 violations

r38-ledger-source-ambiguous: exit 1
VIOLATION: sources[4].id: duplicate sources id 'sella-bell7-note'
VIOLATION: contradictions[0].claim_b.source_id: ambiguous in-world source 'sella-bell7-note'
VIOLATION: timeline[3].source_id: ambiguous in-world source 'sella-bell7-note'
3 violation(s); no canon changed
```

The timeline line is real collateral, not an omitted or novel ledger result. No `claim_a` or event-ID diagnostic occurs. The r7 temporary probe's seven findings had additional entity consumers because it duplicated a differently cited source; that difference in citation footprint is not a new source-resolution rule. Its temporary status limits durable regression convenience, but not its evidential status as independently run prior art. The checker neither chooses a duplicate source row nor decides whether either attributed Bell-7 report is true, mutually incompatible as facts, authentic, or canon. A clean structural control cannot establish excerpt support. **Do not record a coverage/depth/calibration gain, SHONEN checkmark, promotion, push, or merge from this round.**
