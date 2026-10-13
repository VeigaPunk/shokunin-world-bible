# Round 27 final non-author axis adjudication

**Verdict: admit.** Coverage **improved**; depth **unchanged**; calibration **unchanged**. At least one owned axis improved and none was harmed. This is one bounded fixture-only coverage move, not a checker change or a claim about canon.

I read the pre-dispatch claim and post-scout policy in `LOG.md`, the non-author reviewer and independent verifier reports, the checker, the fixture pair, and the fixtures README. The independent verifier replayed the baseline checker at `bb4c6c971faeaed48c7dbdf57ceb90fcfc873a21` versus the current checker on **76/76** old fixture directories with exactly equal stdout bytes, stderr bytes, and exit status (zero mismatches). I independently confirmed that baseline lists 76 directories and 379 JSON files, that the checker is unchanged, and that the Git blob hash of every one of those **379/379** old JSON paths equals its current byte content. These checks corroborate the verifier's regression result; my separate checker replay below is limited to the new pair.

The pair differs only by the added sixth `entities.json` row in `r27-both-ambiguous/`: a structurally admitted `mira` character with nonempty name, `courier-log` first appearance and empty claims. Its first five entity rows equal `r27-target-only/`; the four other JSON tables are byte-identical. Both cases retain the same `relations[0]` record, `mira -> seal`, type `carries`, source ID `courier-log`. I independently replayed each fixture using `python3 .shokunin/lore/corpus/fixtures/check_bible.py <directory>`. Each exited **1** with empty stderr. Exact stdout:

```text
r27-target-only:
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: relations[0].to: ambiguous entity 'seal'
2 violation(s); no canon changed

r27-both-ambiguous:
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: entities[5].id: duplicate entities id 'mira'
VIOLATION: relations[0].from: ambiguous entity 'mira'
VIOLATION: relations[0].to: ambiguous entity 'seal'
VIOLATION: timeline[0].entity_id: ambiguous actor entity 'mira'
VIOLATION: timeline[1].entity_id: ambiguous actor entity 'mira'
6 violation(s); no canon changed
```

The both-case relation findings attach independently to **both fields of the same unchanged relation**, while the target-only control reports `.to` and not `.from`. The two extra timeline findings are collateral to the new `mira` ID collision against two **unchanged** timeline actor references. They are counted in the six, not hidden or presented as additional relation findings. This extends observed checker-input coverage beyond the earlier separate endpoint cases; no new semantic reasoning or depth is shown. The README names the two timeline findings and limits its interpretation, so calibration is not harmed.

This evidence addresses schema-admitted ID multiplicity in this matched fictional input only. The checker and its citations do **not** verify source text, select a canonical row, establish distinct real-world identities, prove that `mira carries seal` is true, or settle canon. It does not justify generalizing to malformed rows, other relation types, or all consumers of entity IDs.
