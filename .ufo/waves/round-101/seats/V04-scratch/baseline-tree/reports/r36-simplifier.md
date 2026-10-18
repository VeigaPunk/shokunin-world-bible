# Round 36 simplifier — controlled wrong-date near-miss

## Minimal artifact

Use one r35-derived negative fixture and preserve all five JSON tables byte-for-byte. The minimal negative signal is one source-prose edit in Sella’s excerpt: change its date from the seventh to the eighth day of Embermonth, year 12. Keep Tarin’s excerpt, every JSON table (including Sella’s event description and ledger rationale), and the r35 baseline untouched. Do not rewrite date-laden structured fields to make the prose agree; their mismatch is the test.

The excerpt is `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/sella-bell7-note-excerpt.md:1`. Its current account says Tower presence and Harbor absence throughout “that same Bell-7 ringing,” then defines Bell-7 as the sole seventh-watch sounding on the **seventh** day. In the near-miss, only that date changes to **eighth**. Its qualification at line 3 already says the date is an unauthenticated source claim, not chronology, clock time, or tick.

## Evidence and expected reading

Tarin’s source dates its Bell-7 to the seventh day (`.shokunin/lore/corpus/fixtures/r35-bell7-conflict/tarin-note-excerpt.md:1`). The structured Sella event still dates her alleged presence/absence to the seventh (`timeline.json:32-38`), and ledger rationale still assumes both reports concern the sole seventh-day ringing (`contradictions.json:12`). The changed Sella excerpt instead reports the eighth-day ringing. Thus the near-miss is deliberately checker-clean but source-text does not establish a shared occasion; a reviewer should decline r35’s conditional same-ringing conflict based on these two excerpts. The unchanged structured rows cannot repair the source-prose mismatch without treating the checker or ledger as source truth.

This is the one calibration axis: distinguish a same-date positive pair from a different-date near-miss despite identical JSON. Falsifiable check: compare the r35 and r36 fixture’s five JSON files byte-for-byte, confirm the only source-text delta is “seventh”→“eighth” in Sella’s date, run the checker and record its clean structural result, then have a non-author reviewer inspect the excerpts blind to the intended outcome. Pass only if the reviewer declines a shared-occasion conflict from the source prose while acknowledging that JSON/checker remain unchanged and clean. Any other prose or JSON delta, or reviewer acceptance of same occasion from source text alone, falsifies the controlled calibration claim.

## Risks and limits

The source text does not authenticate either date; this demonstrates an attribution/occasion mismatch, not that either report is false, not Sella’s location on the seventh, and not a factual location conflict. “Same Bell-7” language in Sella’s excerpt is undercut by its own eighth-day definition; that tension should remain visible rather than silently harmonized. Equal timeline tick 3 is editorial only. A clean checker proves neither source entailment nor canon. Preserve all five JSON files and avoid implying envelope contents, Blue Seal/carbon/route-strip links, source truth, or a winner.
