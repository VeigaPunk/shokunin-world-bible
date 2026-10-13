# Round 36 executor report — wrong-date near-miss

## Artifacts and controlled change

Created `.shokunin/lore/corpus/fixtures/r36-bell7-wrong-date/` as a full copy of `r35-bell7-conflict/`. The sole changed inherited file is `sella-bell7-note-excerpt.md`: exactly `seventh day of Embermonth, year 12` became `eighth day of Embermonth, year 12`. Its “that same Bell-7 ringing” phrase and all other content remain unchanged. The five JSON files (`sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`) compare byte-for-byte identical to r35. Added `date-contrast-map.md` as editorial commentary; it records that the explicit source dates match in r35 but differ in r36, flags Sella's retained “that same” phrase as internally tense with her explicit date, and does not use that deictic phrase to establish the same sole ringing. It also flags the unchanged Sella timeline description and ledger rationale as unsupported by the changed excerpt. It makes no canon, falsity, or real-world chronology claim.

## Verification

JSON byte comparisons (r35 and r36 SHA-256):

- `sources.json`: identical — `65208b4214682494dbd48e0bbcba9061f621308d4d2f0e55baac64e15bc65e73`
- `entities.json`: identical — `0e0ab5b1dc078df4457d57739202911b8197e4aad08bcc4967d364147ee7dc5d`
- `relations.json`: identical — `d983a04cfa8d51dab5a2fc92032ab29696d80c3dc6d5384d724e6225b6fd0b4f`
- `timeline.json`: identical — `4ac5bb65cfa3d7a97799b63d3f234304990f5f55bfe934ee667ca0a891230cd4`
- `contradictions.json`: identical — `213445474f36cdd97ae629dc8fc09b4dcfcafb78c3714e68d2f780cb291037c`.

Inherited-file inventory: only `sella-bell7-note-excerpt.md` differs; diff is the one date-token substitution above (file size 351 → 350 bytes). No other inherited file changed.

Commands run from repository root, each with exact captured streams/status:

- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r35-bell7-conflict` — exit **0**; stdout `CLEAN: schema, citations, relations, timeline; 0 violations\n`; stderr empty.
- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r36-bell7-wrong-date` — exit **0**; stdout `CLEAN: schema, citations, relations, timeline; 0 violations\n`; stderr empty.

These clean results establish structural/citation checks only. They do not establish source-text support, a shared occasion, truth, or canon. No checker, README, LOG, other fixture, or other report was edited; no commit was made.
