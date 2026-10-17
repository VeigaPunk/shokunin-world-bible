# V18 — c3-anti-overclaim (round 97)

- Seat: V18, verifier, adversarial sweep of all new r97 bytes. Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin` (absolute paths throughout — session cwd is the parent repo). Baseline `f3e09f9`. All commands from the lane root with `python3`.
- Exclusive writes: this report + `.ufo/waves/round-97/seats/V18-scratch/`. No commits, no pushes, no network, no nested agents.
- Poll-wait: R4–R6. Reports actually landed under different names than the brief predicted (`R4-fixture-author.md`, `R5-fixture-docs.md`); a glob-based poll caught them. R6's note landed at 18:50; R6's seat report was still absent at my last check (see §7).
- Method: pre-repair bytes were captured from `git show f3e09f9:…` **before** R4 wrote, so the repair diff and receipt comparison are against a frozen baseline, not against a remembered state.

## 1. C3-repair half — r96 cosmetic repair (VERIFIED, byte-minimal)

Frozen pre-repair bytes: `git show f3e09f9:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` → sha256 `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` (identical to the working tree before the edit).

```
$ diff -u .ufo/waves/round-97/seats/V18-scratch/r96-map-pre-repair.md .ufo/.../r96-map-post-repair-18h43.md
@@ -41,13 +41,13 @@
-|---|---|---|---|---|---:|---|---|
+|---|---|---|---|---:|---|---|
-…The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
+…The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not perpetual performance or alliance.
$ diff (line-by-line, all 56 lines) -> DIFF line 44 / DIFF line 50 only
$ wc -l both -> 56 lines each
```

- **Delimiter:** line 44 `8 → 7` cells (header line 43 and data rows are 7). Post-repair cell census of the whole map: `4 / 8 / 7` cells at delimiter lines 10 / 21 / 44, matching their headers — every table delimiter now matches its header.
- **Data rows byte-unchanged:** all `|`-rows excluding pure-delimiter rows hash `1f58fdb9f407b70a59993f194172dcab7b7c1d5005e5812bace29b78069f83e5` before **and** after. The J01–J16 and S01–S02 cells (pointer, source ID, namespace, excerpt path, span, mode, anchor) are therefore byte-identical, and `rows.py` cell-parse confirms 21 shared rows with zero non-namespace diffs.
- **Non-pipe prose:** of the 11 non-pipe lines, only line 50 changed; lines 3, 5, 18, 41, 52, 54, 56 verified unchanged by direct string compare.
- **Receipts unchanged:** pre-repair fixture reconstructed from `f3e09f9` in scratch (`V18-scratch/pre-r96/`), then both it and the delivered post-repair fixture run at the same tool revisions (`support_check.py 55a5eb2753901be7`, `map_obligations.py 2b0ba815326b1cb3`, `check_bible.py ff9fd2aa6811a813`):

```
$ diff rcpt-support-pre.txt rcpt-support-post.txt   -> SUPPORT-RECEIPT-IDENTICAL   (exit 0 both)
$ diff rcpt-map-pre.txt rcpt-map-post.txt           -> MAP-RECEIPT-IDENTICAL       (exit 0 both)
support_check  INVENTORY 16/16; 2/2; 18/18; 14/14  SOURCE-SUPPORT 16/16; MODES 18/18; VALIDATED-ROWS 18/18  RESULT PASS
map_obligations OBLIGATIONS raw=16 mapped=16  INVENTORY 16/16; 2/2; 18/18  RESULT PASS
check_bible    CLEAN: schema, citations, relations, timeline; 0 violations
```

- r96 map re-hashed at the end of my run: still `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de` (no post-report drift); `git status` for the r96 directory shows only that one `M` file.
- **Wording-precision note (bounded, not a claim failure):** line 50 was not a two-word substitution — it is a full sentence replacement that adds three negative bounds ("asserts no reconciliation", "selects no winner", "adds no duty beyond this crossing"). The LOG's own requirement is to fix "the stale 'new relation' sentence" with pointers/anchors/spans/modes untouched, which the delivered edit satisfies exactly; the "data rows byte-unchanged" form of the claim also holds exactly. Recorded so the closure prose does not describe it as a mere phrase swap.
- **Cosmetic residual (pre-existing, bounded):** in the repaired delimiter the right-align colon sits on the "R9 delivery mode" cell (position 6) rather than "Line span" (position 5) for the 7-column editorial table. This misalignment predates the repair (the colon position is unchanged; the edit dropped the trailing cell) and is render-only — `support_check` parses and passes. Not introduced by this round.

## 2. C3-depth half — `r97-crossing-acknowledgment` (VERIFIED)

Byte identity vs r96 post-repair (the five declared byte copies):

```
IDENTICAL entities.json 026af0bc2cdab150   IDENTICAL contradictions.json 37517e5f3dc66819
IDENTICAL relations.json c279254bc7de0636  IDENTICAL inspiration-note.md 58f5390e5928ebad
IDENTICAL source-excerpt.md b5edc2fd3c2e3d4f
```

**Relation row byte-identical — verified stronger than asked:** `relations.json` sha256 `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` is byte-identical across **r94, r95, r96 and r97**. No relation was added, edited, or re-serialized in four rounds. `entities.json` / `contradictions.json` / `inspiration-note.md` / `source-excerpt.md` are likewise byte-identical across r95 → r96 → r97.

**Inherited JSON preserved as bytes, not re-serialized:**

```
sources.json : r96 1741 B -> r97 2235 B; common prefix 1738 B; divergence is ",\n  {new object}" then the same "\n]\n"
timeline.json: r96 1677 B -> r97 2173 B; common prefix 1674 B; same append-only shape
parsed: sources 5->6 ([:5] == r96 True), timeline 5->6 ([:5] == r96 True)
```

**Excerpt:** `fictional-excerpts.md` — r96's 2588 B are an exact byte prefix; append starts line 43; new section 44–53 with quoted lines 48–51 and a Scope line at 53, matching the r95/r96 folio convention (folio 7 after folio 6).

**New records exactly as claimed:**

```
source #5  aru-acknowledgment-note — "records receipt only and is not evidence of a resolution, a reconciliation, an accusation, a winner between the accounts, a continuing duty, or an external historical fact."
event  #5  acknowledgment-aru-records, tick 13, entity_id aru, place_id chalk-stair, depends_on ["response-evin-salt-court"], source_id aru-acknowledgment-note
counts: entities 5 / relations 1 / events 6 / sources 6 / contradictions 0 (ids unique; all source_ids and depends_on resolve; ticks 9,9,10,11,12,13)
```

**Delivered-revision battery (r97 and r96), tool revisions `check_bible ff9fd2aa…`, `support_check 55a5eb27…`, `map_obligations 86b52949…` (contract `2142b991…`):**

```
r97: check_bible    CLEAN: schema, citations, relations, timeline; 0 violations            exit 0
     map_obligations OBLIGATIONS raw=17 mapped=17  INVENTORY 17/17; 2/2; 19/19  RESULT PASS exit 0
     support_check   INVENTORY 17/17; 2/2; 19/19; DISTINCT-ANCHORS 15/15
                     SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19  RESULT PASS exit 0
r96: check_bible CLEAN exit 0; map_obligations raw=16 mapped=16 RESULT PASS exit 0; support_check 16/16; 2/2; 18/18; 14/14 RESULT PASS exit 0
```

**Inherited map rows unchanged:** `rows.py` compares every cell of the r96 post-repair map against the delivered r97 map — J01–J16 differ in **only** the path-qualification cell (pointer, in-world source ID, excerpt path, line span, mode and anchor are literally identical strings); the only new row is J17. The R9 declaration-table row correctly widened `fictional-excerpts.md:12-40 → 12-51` (expected; that table is not a J/S data row).

**Census independently reproduced** (full sweep, every fixture directory, `check_bible.py` per directory):

```
CENSUS dirs=171 clean=37 negative=134 violation_lines=421 non01=0      # r96 closure was 170/36/134/421
```

**Load-bearing proofs (two independent constructions):**

```
# (a) reconstruct the pre-R5 state: r97 JSON + the r96-copied map
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-97/seats/V18-scratch/r97-preR5
OBLIGATIONS raw=17 mapped=16
FINDING missing_obligation: timeline.json#/5 has no map row
RESULT FAIL   exit=1
# (same state) support_check still says RESULT PASS 16/16 — the lexical blind spot map_obligations closes
# (b) mutate the delivered J17 span 44-53 -> 44-46 in a scratch copy
FAIL: J17: anchor hit outside declared line span 44-46 (hit lines: 48)
SOURCE-SUPPORT 16/17 ... RESULT FAIL   exit=1
```

So the 17th row is not decorative: removing it fails the completeness gate, and corrupting its span fails the anchor gate.

## 3. Anti-overclaim sweep — reconciliation and blame readings

I tried to construct each reading; none survives the delivered bytes.

- **"acknowledgment = settlement/reconciliation":** closed in five places — source reliability note (`sources.json#/5`: "records receipt only… not evidence of a resolution, a reconciliation…"), excerpt Scope line 53 ("It records receipt only; it asserts no accusation, no reconciliation, no winner…"), event description (`timeline.json#/5`: "asserts no accusation, no reconciliation, no winner…"), map prose `claim-excerpt-map.md:51` and `:57`, README `:11` ("neither overturns, confirms, adjudicates, nor reconciles the accounts"). Not constructible.
- **"Aru holds to his own account ⇒ blame/refusal":** line 49 does preserve Aru's account, but line 50 asserts no accusation and no winner and line 51 asserts no reconciliation; the map `:57` quotes all three. The dispute is preserved *unresolved*, exactly as claimed — a blame reading is explicitly excluded by the same record. Not constructible.
- **"receipt confirms Evin's account":** receipt of a document is not confirmation of its content; the same note states both accounts stand unresolved and the README denies confirmation. Not constructible.
- **"linear tick chain implies the arc closes":** bounded by the editorial-encoding sentence, which now covers the new row (`claim-excerpt-map.md:51`, README `:13`). Not constructible.
- **"a claim/entity/relation was smuggled in":** entities and relations byte-identical; contradictions still `[]`; raw obligations rose by exactly one (the event), so no new obligation class exists. The first-person notes are carried as sources + timeline events, the same shape as r95/r96.
- **Structural contradiction:** none asserted anywhere; `contradictions.json` byte-identical `[]`, and no ledger pair was added (r35 class correctly distinguished in R6's note).

## 4. Adversarial check of the producers' reports

- **R4 (`R4-fixture-author.md`)** — every hash/number I re-derived matches: pre-repair `5093d72e…`, post-repair `e851f068…`, `2 2` numstat, excerpt append `42a43,53`, new section 44–53, census 171, and its pre-R5 `missing_obligation` FAIL (independently reproduced above). Its disclosed transient creation of the r97 README/map as byte-copy bases is confirmed by my snapshots and was replaced by R5.
- **R5 (`R5-fixture-docs.md`)** — claimed shas all match the actual bytes: README `d9387b7d…` (5304 B), map `49d4834e…` (12117 B), sources `438fb513…`, timeline `73063a86…`, excerpts `8ba491cb…`. Its caveat that `corpus/fixtures/README.md` still carries the r96 census text is accurate (line 1217 = "170 fixture directories").
- **R6 (`corpus/knowledge/r97-acknowledgment-scope-note.md`, final revision sha256 `5e3b4225c30de8a2…`, 70 lines, mtime 18:52)** — every cited line verified to exist and to say what is claimed: `sources.json:33`/`:36`, `timeline.json:55`, `claim-excerpt-map.md:38`/`:57`, `README.md:3`/`:11`/`:13`/`:21`, r35 `contradictions.json#/0` (`bell7-location-reports`), `manual-clause-pointer-map.md:3`/`:21`, `corpus/fixtures/README.md:761` ("Neither wins."), decision-table `:226-230`. The note was revised once during the round (18:50 → 18:52): the `citation-convention:` line was made explicit and the tool-revision line now cites the delivered `map_obligations 86b52949…` (with the earlier `70795150…` run noted as giving the identical result). No substantive claim changed; I re-verified the final revision, and its receipts reproduce byte-for-byte at the delivered revisions. Its bounds paragraph explicitly refuses resolution/fault readings, so the note does not overclaim its class.
- **R6 (`R6-knowledge-note.md`)** — its own poll-wait honesty note (a first glob matched scratch *directories*, not reports) matches what I saw from the outside; its adjacent C2 observation was correct at its measurement time and is now superseded (below).

## 5. Write-scope sweep

`git status --porcelain` over the whole lane shows modified/untracked entries confined to the declared scope: `LOG.md`, `corpus/tools/{map_obligations.py,map-obligations-contract.json,dependency_freeze.py,dependency-freeze-contract.json,README.md}`, `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`, `corpus/fixtures/r97-crossing-acknowledgment/`, `corpus/knowledge/r97-acknowledgment-scope-note.md`, `.ufo/waves/round-97/`. **No stray write outside the lane** (the r94-F01 class did not recur): nothing appeared under the parent repo or outside `lore-shokunin/`.

## 6. Bounded observations (do not block C3, but should reach the closure record)

1. `corpus/fixtures/README.md:1217` still declares the **r96** census (170 dirs / 36 clean). Measured state is **171 / 37 / 134 / 421 / 0**, independently reproduced by me. Closure-time text update needed; R5 flagged the same.
2. Tool churn during the round: `map_obligations.py` `2b0ba815 → c1881149 → 86b52949` (contract `2142b991`), `dependency_freeze.py` `a3b57978 → fbaca38f → b06275f3` (contract `c65ac3bd → 8015e1f9`). My r96 before/after receipt comparison was taken at a **single** revision (both sides), so the "receipts unchanged by the repair" result is not a tool-churn artifact; the final battery was re-run at the delivered revisions.
3. The r97 README/map existed as exact byte copies of the post-repair r96 files from 18:44:16 until R5 rewrote them (18:48:56 / 18:49:14). Disclosed by both R4 and R5; final state is R5's. The transient copy did **not** satisfy the 17th obligation — proven by the `missing_obligation` FAIL above.
4. **Adjacent C2 state (observed, not adjudicated — outside my seat).** At my sign-off: `dependency_freeze.py` `b06275f3…` / contract `8015e1f9…`; `--self-test` → `SELF-TEST 16/16` / `RESULT PASS` exit 0 (R6's mid-flight `CONTRACT-INVALID` observation is superseded); `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response` → `FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1`, `DIGEST d422a9b3d95c4e0b…`, `RESULT PASS` exit 0 — the r96 digest is unchanged by the cosmetic repair (consistent with the map not being a pinned file); `… corpus/fixtures/r97-crossing-acknowledgment` → `FINDING UNPINNED-FIXTURE … (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])`, `RESULT ERROR` exit 2 — the new r97 fixture's dependency chain is not frozen. C2's own seats own that verdict; recorded because it bears on closure (possible r98 item: pin r97, or declare it deliberately unpinned).

## 7. Poll-wait record

| Producer | Artifact | Status at my check |
|---|---|---|
| R4 | r96 repair + r97 JSON/excerpts | present; report `R4-fixture-author.md` read (name differed from the brief's prediction) |
| R5 | r97 README + map | present (authored, shas match); report `R5-fixture-docs.md` read |
| R6 | `corpus/knowledge/r97-acknowledgment-scope-note.md` | present; every citation verified against the final revision (`5e3b4225…`) |
| R6 | seat report | present — `R6-knowledge-note.md` (8195 B, 18:53), read; all three producer reports were on disk before this report was filed |

## Bottom line

**PASS** — r96 cosmetic repair proven byte-minimal (2 of 56 lines; data rows byte-identical `1f58fdb9…`; receipts diff-identical before/after at a single tool revision) and r97 verified end-to-end (`relations.json` byte-identical across r94–r97; inherited JSON/excerpts preserved as bytes; J01–J16 identical modulo the namespace column; `check_bible` CLEAN, `map_obligations` 17/17, `support_check` 17/17 · 19/19 · 15/15, all exit 0; census 171/37/134/421/0 independently reproduced), with the 17th row and its span proven load-bearing by two independent failure constructions and no reconciliation or blame reading constructible from any delivered byte; bounded residuals are the stale census text at `corpus/fixtures/README.md:1217`, the tool churn, and the unpinned r97 dependency chain (C2-side).
