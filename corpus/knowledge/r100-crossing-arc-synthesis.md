source: `corpus/fixtures/r94-paired-crossing/{README.md,entities.json,relations.json,timeline.json,sources.json,contradictions.json,claim-excerpt-map.md,fictional-excerpts.md}`; `corpus/fixtures/r95-crossing-aftermath/{README.md,entities.json,relations.json,timeline.json,sources.json,contradictions.json,claim-excerpt-map.md,fictional-excerpts.md}`; `corpus/fixtures/r96-crossing-response/{README.md,entities.json,relations.json,timeline.json,sources.json,contradictions.json,claim-excerpt-map.md,fictional-excerpts.md}`; `corpus/fixtures/r97-crossing-acknowledgment/{README.md,entities.json,relations.json,timeline.json,sources.json,contradictions.json,claim-excerpt-map.md,fictional-excerpts.md}`; `corpus/fixtures/r98-clerk-filing/{README.md,entities.json,relations.json,timeline.json,sources.json,contradictions.json,claim-excerpt-map.md,fictional-excerpts.md}`; `corpus/fixtures/r99-window-lapse/{README.md,entities.json,relations.json,timeline.json,sources.json,contradictions.json,claim-excerpt-map.md,fictional-excerpts.md}`; `corpus/fixtures/r100-docket-review/{README.md,entities.json,relations.json,timeline.json,sources.json,contradictions.json,claim-excerpt-map.md,fictional-excerpts.md,inspiration-note.md,source-excerpt.md}`; `corpus/knowledge/r98-clerk-scope-note.md`; `corpus/knowledge/r99-lapse-scope-note.md`; `corpus/knowledge/r100-provenance-semantics-boundary.md`; `corpus/tools/dependency-freeze-contract.json`
verified-at: 2026-10-17 — read the delivered excerpts, maps, README bounds, and source/event records; counted the raw tables and obligations; compared inherited JSON values and excerpt-byte prefixes on all six continuation steps this pass. Cited paths and ranges were checked locally; no external URL was fetched. This is an author-seat dossier, not an independent admission or canon finding.
recheck: before integrating any crossing-arc claim, and whenever a cited fixture, map, excerpt, source attribution, gate, pin, or receipt changes. Reinspect the whole proposition and its non-establishment bounds; a retained anchor is not whole-claim entailment.
citation-convention: in each table row, bare `file.json#/pointer` references and source IDs resolve inside that row's full fixture path. Other citations use lane-root-relative paths; ranges refer to the delivered file, not a web edition. Source IDs are cluster-local, so compare path-qualified pairs rather than bare IDs.

# Crossing-arc synthesis — seed and six continuation beats

The round's “six-beat arc” means the six continuation beats r95–r100 after the r94 minute. Its complete dossier therefore has **seven snapshot records**, not six: r94 minute → r95 aftermath → r96 response → r97 acknowledgment → r98 filing → r99 lapse → r100 review. This follows the earlier notes' numbering: r98 is the fourth continuation (`corpus/knowledge/r98-clerk-scope-note.md:14`), r99 the fifth (`corpus/knowledge/r99-lapse-scope-note.md:14`), and r100 the sixth. The inherited r88 paired-clock register is the precursor, not an extra continuation beat.

This is an arc of attributed records, not a progression toward a verdict. Its invariant is **unresolved throughout**: no continuation selects a winner, reconciles the two accounts, records a finding, or converts the crossing-only agreement into a standing duty. “Unresolved” describes the records' non-adjudication; it is not a testimony-truth finding or a claim that an OPEN docket literally existed before its r98 filing.

## Per-record docket

Counts `E/R/T` mean entities / relations / timeline events in that snapshot; sources count all records in `sources.json`; obligations count source-attributed JSON pointers, not narrative sentences or external editorial comparisons. The source and event pointer columns identify the record introduced at that step; inherited records remain in each later snapshot.

| Record | Fixture | Added event (pointer, editorial tick) | Added in-world source | E/R/T | Sources | Map obligations |
|---|---|---|---|---:|---:|---:|
| Seed — minute | `corpus/fixtures/r94-paired-crossing/` | `paired-crossing-decision`, `timeline.json#/2`, tick 10 | `crossing-minute`, `sources.json#/2` | 5/1/3 | 3 | 14 |
| Beat 1 — aftermath | `corpus/fixtures/r95-crossing-aftermath/` | `aftermath-missing-evin`, `timeline.json#/3`, tick 11 | `aru-aftermath-note`, `sources.json#/3` | 5/1/4 | 4 | 15 |
| Beat 2 — response | `corpus/fixtures/r96-crossing-response/` | `response-evin-salt-court`, `timeline.json#/4`, tick 12 | `evin-response-note`, `sources.json#/4` | 5/1/5 | 5 | 16 |
| Beat 3 — acknowledgment | `corpus/fixtures/r97-crossing-acknowledgment/` | `acknowledgment-aru-records`, `timeline.json#/5`, tick 13 | `aru-acknowledgment-note`, `sources.json#/5` | 5/1/6 | 6 | 17 |
| Beat 4 — filing | `corpus/fixtures/r98-clerk-filing/` | `clerk-filing-open`, `timeline.json#/6`, tick 14 | `clerk-filing-note`, `sources.json#/6` | 6/1/7 | 7 | 20 |
| Beat 5 — lapse | `corpus/fixtures/r99-window-lapse/` | `clerk-lapse-recorded`, `timeline.json#/7`, tick 15 | `clerk-lapse-note`, `sources.json#/7` | 6/1/8 | 8 | 21 |
| Beat 6 — first-passage review | `corpus/fixtures/r100-docket-review/` | `clerk-review-first-passage`, `timeline.json#/8`, tick 16 | `clerk-review-note`, `sources.json#/8` | 6/1/9 | 9 | 22 |

The r98 obligation increase is three, not one: the new `clerk-maren` entity contributes its first appearance and one sourced claim, in addition to the filing event. The other continuation steps add one event obligation and one source apiece. The new r100 review adds neither an entity, a claim, a relation, nor a contradiction. Its 22 raw obligations are six first appearances + six claims + one relation + nine events; its two editorial comparison rows are counted separately.

## What each beat records, without upgrading its testimony

All seven excerpt sections remain present in the delivered `corpus/fixtures/r100-docket-review/fictional-excerpts.md` at the inherited line numbers:

- **Seed / r94 minute, lines 15–20.** One bounded agreement: “for this crossing only,” followed by one temporary route mark. The tick-10 decision names both inherited tick-9 entries as dependencies. It neither promises continuing performance nor contains the later lapse assertions; the minute does not itself say the crossing-window closed. The original record is `corpus/fixtures/r94-paired-crossing/fictional-excerpts.md:15-20`.
- **Beat 1 / r95 aftermath, lines 22–31.** Aru reports waiting at the Chalk Stair through the agreed bell and says Evin did not come. “I assert no other duty, no breach, and no obligation beyond this crossing” bounds that report. It is reported non-arrival, not proof of a breach or a verdict against Evin (`corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md:26-31`).
- **Beat 2 / r96 response, lines 33–42.** Evin reports being at Salt Court through the same agreed bell, makes no accusation, selects no winner, and states “Both accounts stand unresolved.” This is the first explicit two-account unresolved statement, not a correction of Aru's earlier report (`corpus/fixtures/r96-crossing-response/fictional-excerpts.md:37-42`).
- **Beat 3 / r97 acknowledgment, lines 44–53.** Aru records receipt of Evin's response while holding to his own account. Receipt does not mean agreement, corroboration, retraction, reconciliation, accusation, or selection of a winner (`corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md:48-53`).
- **Beat 4 / r98 filing, lines 55–64.** The clerk files both pending accounts and records the matter OPEN; “I assert no finding” and “I reach no verdict and reconcile nothing” delimit the institutional act. Filing is not adjudication. Maren's office is the note's attributed self-description, not independently authenticated authority (`corpus/fixtures/r98-clerk-filing/fictional-excerpts.md:59-64`).
- **Beat 5 / r99 lapse, lines 66–76.** The clerk's record says the crossing-window closed, the agreement was unfulfilled, no claim was lodged, and the matter stands as a historical open entry. “I record no resolution, assign no blame, and reconcile nothing” is a negation, not a positive resolution. **Window closed is not matter closed**; the lapse closes no one (`corpus/fixtures/r99-window-lapse/fictional-excerpts.md:70-76`).
- **Beat 6 / r100 review, lines 78–88.** The clerk records a first-passage docket review “After my lapse record.” “The entry remains open,” “No new filings have been lodged,” “I make no finding and resolve nothing,” and “Both accounts stand unresolved” are the delivered note's own assertions. Review is not a new filing, renewed agreement, finding, resolution, or reconciliation (`corpus/fixtures/r100-docket-review/fictional-excerpts.md:82-88`).

The review source's reliability note is `corpus/fixtures/r100-docket-review/sources.json:51-54`; its exact new event is `corpus/fixtures/r100-docket-review/timeline.json:88-96`: actor `clerk-maren`, place `chalk-stair`, tick 16, `depends_on: ["clerk-lapse-recorded"]`, `source_id: clerk-review-note`. Map row J22 is `corpus/fixtures/r100-docket-review/claim-excerpt-map.md:43`, span 78–88, exact anchor at excerpt line 82; its whole-proposition bounds are at map line 72. The anchor does not by itself establish the other four quoted sentences; those must be read in the delivered section.

## Preservation and the unresolved-throughout invariant

On each adjacent snapshot step r94→r95→r96→r97→r98→r99→r100, this author compared the inherited entity prefix, the full relation table, the inherited timeline/source prefixes, and the entire previous fictional excerpt as a byte prefix: all were preserved. The external `source-excerpt.md` and `inspiration-note.md` bytes were also unchanged at every step. Earlier records were accumulated, not rewritten into later conclusions.

The stronger r99→r100 check has six entity rows, one relation, eight timeline rows, and eight source rows inherited unchanged. `contradictions.json`, `entities.json`, `relations.json`, `inspiration-note.md`, and `source-excerpt.md` are byte-identical between these two fixtures; the 5,114-byte r99 fictional excerpt is an exact prefix of the 5,961-byte r100 file. The clerk's `first_appearance` remains `clerk-filing-note`; the review is not a second first appearance. The reviewed relation is still the one crossing-only agreement sourced to `crossing-minute`.

The invariant has a bounded temporal reading: r94 sets the crossing-only agreement and r95 introduces the first report, so neither can literally adjudicate a pair of accounts not yet present. From r96 onward the two-account unresolved status is explicit or inherited and reasserted. The later receipt, institutional filing, recorded lapse, and docket review add no verdict and revise neither account. OPEN is first recorded at r98, remains a historical open entry at r99, and remains open at r100. Closing the named crossing-window does not close the entry.

Every snapshot's `contradictions.json` is `[]`. This is a fact about the authored records, not a logical proof that no incompatibility could ever be found. Aru's account places Aru at the Chalk Stair; Evin's account places Evin at Salt Court. Different actors at different places do not, by themselves, assert one actor's incompatible occupancy, and this arc files no contradiction between them.

## Non-establishment bounds

- **No testimony truth.** The dossier records who says what. It authenticates neither the reports, the filing, the lapse, the review, the alleged absence, nor the clerk's identity or authority. Neither account is chosen as true or false. “No claim was lodged” and “No new filings have been lodged” are statements in their respective notes, not proof of a global absence in every possible record.
- **No chronology authentication.** Integer ticks, event IDs, and `depends_on` arrays are editorial normalizations of excerpt labels and order/dependence wording, not literal JSON quotations or independently authenticated dates. The new edge encodes the note's “After my lapse record”; it does not independently establish the history it models. An inherited empty list means no earlier dependency is represented in this sequence, not that nothing earlier ever occurred.
- **No expansion of duty.** The original relation covers this crossing only. Non-performance, response, receipt, filing, lapse, and review supply no standing alliance, perpetual performance, breach finding, renewed agreement, continuing obligation, blame, or adjudication. The single `entity_id` actor slot does not exclude the other participants or assign fault.
- **No automatic source identity.** Reused IDs are intentional continuation-local lookups. Compare, for example, `(r99-window-lapse, clerk-lapse-note)` with `(r100-docket-review, clerk-lapse-note)` as path-qualified records; neither bare-name equality nor namespace changes are independent identity evidence. The inherited “chalk stair” verse is not retroactively a map or a first presentation of a specific place.
- **No semantic or canon certification by gates.** Structural CLEAN, lexical support, obligation completeness, and byte identity establish different bounded properties. None proves whole-claim entailment, dependency meaning, source authenticity, truth, chronology, rights, permission, or canon. The exact distinction and r99 AC-1/AC-2 corrections are in `corpus/knowledge/r100-provenance-semantics-boundary.md`.
- **Rights and AI-training permission unassessed.** The copied design prompt is Spence's English prose, not an authenticated K'iche-language primary text. It is external editorial comparison, not an in-world witness, a cultural rule, or fictional canon (`corpus/fixtures/r100-docket-review/README.md:19`; `corpus/fixtures/r100-docket-review/inspiration-note.md:7-21`; `corpus/fixtures/r100-docket-review/source-excerpt.md:3-7`). Attribution, age, public access, and a byte pin do not grant reuse or AI-training permission.

## Coverage boundary

The seven dossier snapshots r94–r100 are **not the same set** as the seven frozen-chain fixtures. The delivered pin set is r88 plus r94–r99; r99's lapse is now pinned, while r100's review is not (`corpus/tools/dependency-freeze-contract.json`, `pins`; current-chain receipt in `corpus/knowledge/r100-provenance-semantics-boundary.md`). This dossier does not silently claim freeze coverage for the new tick-16 edge. Coverage and the arc's increased authored depth remain separate claims.

This author-seat synthesis is bounded to the cited local records. It neither admits the round independently nor promotes an authored report, a clean gate result, or a byte-preserved snapshot into a resolved world fact.

## Delivered-revision receipts (2026-10-17)

The producer artifacts and reports existed before this final replay: T2 was ready at poll 6/40 (100 seconds) and T3 at poll 7/40 (120 seconds), with 20-second spacing. This is a replay of delivered bytes, not a verification of a producer plan. The author ran this command from `/home/vgpnk/Projects/shokunin/lore-shokunin`:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/arc_audit.py
```

Observed exit 0, `ARC-AUDIT failures=[]`. The harness ran `check_bible.py`, `support_check.py`, and `map_obligations.py` concurrently against each of the seven full fixture paths in the docket table. All 21 real gate calls exited 0: every checker run printed `CLEAN: schema, citations, relations, timeline; 0 violations`; every support/map run printed `RESULT PASS`. Map receipts were `OBLIGATIONS raw=14 mapped=14`, `15/15`, `16/16`, `17/17`, `20/20`, `21/21`, and `22/22` respectively (the latter pairs abbreviate the same `raw=N mapped=N` output form). All six steps' inherited map rows matched after normalizing only the namespace column, and all eight preservation checks per step were `True`.

The exact r100 calls and selected observed output were:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

Exit 0.

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

```text
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
```

Exit 0. Individual PASS rows are omitted here, not counted as semantic findings.

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
```

```text
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
```

Exit 0. The harness counted `CENSUS 174` fixture directories, compared with 173 recorded at r99 closure (`LOG.md:3343-3344`): one new fixture. The census is a directory count, not evidence of greater truth or resolution. The delivered tools at these receipts were SHA-256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (`corpus/fixtures/check_bible.py`), `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` (`corpus/tools/support_check.py`), and `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` (`corpus/tools/map_obligations.py`). Complete commands, stdout, exits, raw counts, preservation checks, and final r100 file digests are in `.ufo/waves/round-100/seats/T4-scratch/arc-output.txt` and `.ufo/waves/round-100/seats/T4-scratch/arc-results.json`. These scratch receipts are measurements of this pass; regenerate them if the scratch tree is absent or any cited input changes.
