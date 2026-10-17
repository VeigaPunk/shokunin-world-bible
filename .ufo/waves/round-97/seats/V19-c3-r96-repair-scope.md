# V19 — c3-r96-repair-scope (round 97)

Seat: **V19 c3-r96-repair-scope** — verifier. Claim under test (C3 repair half): after R4's
cosmetic repair, `git diff f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`
shows **exactly the two declared cosmetic changes and nothing else**; the r96 `support_check`
receipt is **identical**; the r96 `map_obligations` receipt is **identical**.

Baseline: r96 closure `f3e09f9` (lane HEAD at start `2393934`; working tree clean for the fixture).
Pre-repair map byte-identical to `f3e09f9`: `sha256 5093d72e…` (verified by comparing the working
tree against `git show f3e09f9:…` — both `5093d72e…`). Post-repair map: `sha256 e851f068…`.

Protocol: poll-wait honoured — pre-repair receipts were captured **before** the repair landed
(18:42, map still `5093d72e…`, tools frozen), then the poll waited for both the map change and
R4's report (`READY try=21` of 40, 18:49:55; R4 report `R4-fixture-author.md` written 18:50).
All final checks re-run on the frozen post-repair revision (map mtime 18:43:42, before R4's report).

Nothing was written outside this report and `.ufo/waves/round-97/seats/V19-scratch/`.

## Claim 1 — the diff is exactly the two declared cosmetic changes

Commands and observed output (final revision):

```
$ git diff --numstat f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
2	2	corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
$ git diff -U0 f3e09f9 -- … | grep -c '^@@'
2
$ git diff --check f3e09f9 -- …        # exit 0, no output
$ wc -l  pre 56 / post 56 ; tail -c 1 pre 0a / post 0a   # line count and trailing newline unchanged
$ file …   → Unicode text, UTF-8 text, with very long lines (1034); CR count 0
```

The only two changed lines (`git diff -U0 … | grep -E '^[-+][^-+]'`, verbatim):

```
-|---|---|---|---|---|---:|---|---|
+|---|---|---|---|---:|---|---|
-The inherited tick-9 entries … not that no earlier event exists anywhere. The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
+The inherited tick-9 entries … not that no earlier event exists anywhere. The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not perpetual performance or alliance.
```

Change (a), delimiter: pre line 44 carried **8 cells** (`|---|---|---|---|---|---:|---|---|`) under a
**7-column** editorial header/rows (`awk -F'|'` field counts: lines 43/45/46 = 7, line 44 = 8
pre → 7 post); the repair makes it 7, matching the table. The 8-column JSON-facts table
(lines 20/21 = 8/8) is untouched.

Change (b), wording: the line-50 stale closing sentence "The new relation encodes only the
agreement for this crossing, not perpetual performance or alliance." → "The new tick-12 event
encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation,
selects no winner between the accounts, and adds no duty beyond this crossing, not perpetual
performance or alliance." (r96's new row J16 is an event, not a relation; r94's relation J11 is
inherited.) The rest of line 50, including the sentence cited by
`corpus/knowledge/r96-response-scope-note.md:34` ("editorial encodings … not literal JSON
syntax"), is byte-unchanged.

Nothing else moved:

```
$ grep -E '^\| (J[0-9]{2}|S[0-9]{2}) ' baseline > pre-rows ; same > post-rows
$ cmp pre-rows post-rows            → DATAROWS-IDENTICAL 18 rows  (block sha256 1ff29a75…)
$ diff <(grep -vE '^\| (J[0-9]{2}|S[0-9]{2}) ' baseline) <(… post)  → only the two lines above
$ git diff --stat f3e09f9 -- corpus/fixtures/r96-crossing-response/
 corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

So all 16 J rows and 2 S rows (pointers, source IDs, namespaces, excerpt paths, spans, R9 modes,
anchors) are byte-identical, and no other r96 fixture file changed. Because the line count is
unchanged (56) and only lines 44/50 differ, the cross-references in
`corpus/knowledge/r96-response-scope-note.md` (`:37`, `:50`, `:54`) still resolve to the same
content (spot-checked: post line 37 = J16 row, line 54 = J16 bounded-reading paragraph).

## Claim 2 — `support_check` r96 receipt identical

Pre (captured 18:42 against the pristine `f3e09f9` tree; tool `support_check.py` sha256
`55a5eb27…` = frozen) vs post (same tool revision):

```
$ diff r96-support-pre.txt r96-support-post.txt   → empty   → SUPPORT-RECEIPT-IDENTICAL
  exit 0 both; tail of both:
  RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
  SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
  RESULT PASS
```

Re-proven map-only: the pre-repair map copied into a scratch cluster
(`V19-scratch/precluster/`) and re-run under the current tool reproduces the same output
(`SUPPORT identical under current tool`). `support_check.py` never changed this round
(`55a5eb27…` = `f3e09f9`). Cross-check against the r96-closure record
`corpus/knowledge/r96-response-scope-note.md:49-50`: every recorded field
(`INVENTORY … DISTINCT-ANCHORS 14/14`; `SOURCE-SUPPORT 16/16 … VALIDATED-ROWS 18/18 / RESULT PASS`)
matches the observed post-repair output.

## Claim 3 — `map_obligations` r96 receipt identical

Pre (frozen tool `2b0ba815…` = `f3e09f9`) vs post (same revision):

```
$ diff r96-mapobl-pre.txt r96-mapobl-post.txt   → empty   → MAPOBL-RECEIPT-IDENTICAL
  exit 0 both; output both sides:
  OBLIGATIONS raw=16 mapped=16
  INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
  RESULT PASS
```

R1's C1 revision landed mid-round (`map_obligations.py` now `86b52949…`), so I re-proved the
invariance across tool revisions: pre-map (scratch copy) and post-map both re-run under
`86b52949…` → identical to each other **and** byte-identical to the frozen-tool receipts
(`SUPPORT == frozen-tool receipt`, `MAPOBL == frozen-tool receipt`). Both original receipts were
produced while the tool was still the frozen revision, so the comparison isolates the map change.

## Observations / residuals (outside this seat's verdict, reported as evidence)

- The same stale "new relation" sentence still exists in the r94 and r95 maps
  (`corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md:48`,
  `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md:49`). It is accurate in r94 (its
  new row is relation J11) but the same staleness class in r95 (its new row is event J15). Round-97
  byte scope covers only r96's map, so this is a residual, not a defect of this repair.
- `claim-excerpt-map.md` is not a pinned file in `corpus/tools/dependency-freeze-contract.json`
  (the r96 pin's `files` map lists only the five JSON tables), so this cosmetic repair cannot move
  the r96 freeze digest; the C2 "re-freeze through the guarded path" is digest-neutral with respect
  to the map (R4 reports the same; R3 owns that verdict).
- The new sentence's assertions are consistent with the fixture's own record
  (`corpus/knowledge/r96-response-scope-note.md:19`: "asserts no accusation against Aru, selects no
  winner, and states that both first-person accounts stand unresolved") and with the J16
  bounded-reading paragraph (map line 54). Wording quality is other seats' call; observed
  consistent, no contradiction introduced.

## Bottom line

**PASS** — the r96 map repair is byte-minimal (exactly the two declared cosmetic lines; all 18 data rows, anchors, spans and modes byte-identical; nothing else in the r96 fixture changed) and both r96 receipts (`support_check` 18/18 PASS, `map_obligations` raw=16 mapped=16 PASS) are byte-identical before vs after, under both the frozen and the current tool revisions.
