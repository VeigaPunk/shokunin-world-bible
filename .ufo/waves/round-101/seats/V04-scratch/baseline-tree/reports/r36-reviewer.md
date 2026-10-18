# Round 36 non-author review

## Verdict: PASS for date-mismatch calibration; FAIL for shared-occasion support in r36

I compared both excerpts and maps in `r35-bell7-conflict/` and `r36-bell7-wrong-date/`, all five JSON tables, the r35 initial failure and corrected review, and the r36 ledger rationale.

### Source entailment

The r35 positive pair explicitly agrees: Tarin says Bell-7 is “the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12”; Sella says she was at Tower “throughout that same Bell-7 ringing” and defines it as sounding on “the seventh day of Embermonth, year 12.” The corrected r35 review accordingly says the excerpts “expressly assert the same single ringing,” while preserving this as fictional, attributed testimony and a conditional report conflict.

R36 changes Sella's date to “the eighth day of Embermonth, year 12” while Tarin remains on the seventh. Sella's retained “that same Bell-7 ringing” is deictic tension—not a repair: her sentence identifies that ringing as an eighth-day ringing, unlike Tarin's seventh-day ringing. Therefore the r36 source pair does **not** support r35's conditional shared-ringing conflict. The appropriate conclusion is only that these excerpts do not establish a shared occasion. I do not infer either account false, Sella at Harbor on the seventh, or any real-world date truth/canon.

This matches the r35 initial failure's caution: separately scoped note dates did not “independently identify the referent across notes.” R35 passed only after both excerpts named the same explicit seventh-day date and sole ringing. R36 withdraws precisely that support.

### Structured data and pointers (distinct question)

All five JSON files are byte-identical between r35 and r36. In particular, `timeline.json`'s Sella event still says Bell-7 sounded on “the seventh day of Embermonth, year 12,” and the ledger `why` still conditions its apparent conflict on both reports referring to that seventh-day ringing. Those copied assertions are unsupported by the altered Sella excerpt; they cannot make its eighth-day source text entail the seventh-day premise. The date-contrast map correctly calls this a prose/record mismatch and says the retained phrase cannot establish one shared sole ringing.

Separately, JSON pointer/reference validity is not disproved by this semantic mismatch. The two ledger pointers still resolve to the Tarin event's `place_id` and the Sella event's `place_id`; a structural checker can validate schema and references without validating that the cited excerpt supports the event description or rationale. Thus pointer validity may pass while source-to-record entailment and shared-occasion support fail. Neither the copied event/ledger nor JSON is declared canonically false.

## Judgment

**PASS**: controlled near-miss succeeds as a calibration case; the source dates differ and the inherited structured rationale is exposed as unsupported by Sella's changed excerpt.

**FAIL**: r36 cannot inherit r35's conditional same-occasion conflict inference from these excerpts. No adjudication of either account, Sella's seventh-day location, or real-world chronology follows.
