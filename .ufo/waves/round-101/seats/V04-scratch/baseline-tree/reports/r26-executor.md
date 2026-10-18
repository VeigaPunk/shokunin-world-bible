# Round 26 executor report

Owned artifact: new `.shokunin/lore/corpus/fixtures/r26-to-malformed/` (five JSON files) and this report only. Copied all five files from `r25-to-ambiguous`; changed only the second `seal` row `name` value to `""`. No checker, LOG, README, or commit changes.

Commands and outputs (run from repository root):

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r26-to-malformed
VIOLATION: entities[4].name: required nonempty str
1 violation(s); no canon changed
(exit 1)

python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-ambiguous
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: relations[0].to: ambiguous entity 'seal'
2 violation(s); no canon changed
(exit 1)

python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-unique
CLEAN: schema, citations, relations, timeline; 0 violations
(exit 0)
```

`diff -u r25-to-ambiguous/entities.json r26-to-malformed/entities.json` (paths abbreviated):
```diff
-    "name": "Seal in courier ledger",
+    "name": "",
```
The only change is that value on the second seal row. The four other files are byte-identical copies. Malformed row still exists in raw fixture; checker reports its name schema violation and excludes it from admitted entities, hence no duplicate-ID finding and no `relations[0].to` ambiguity. This is strictly an admission/screening observation—not evidence that source evidence is false, that the seal is missing, or that the world has a unique/canonical seal. Checker itself says “no canon changed.”
