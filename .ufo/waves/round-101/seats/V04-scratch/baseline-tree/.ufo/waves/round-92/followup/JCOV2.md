# JCOV2 — Spence-rows judge (round 92 follow-up)

Seat: JCOV2. Judgment surface: committed tree `c4d4823` (tree clean; re-checked `git status --short | wc -l` → `0`), baseline `396c568`. Mission: whole-claim audit of the two new editorial rows (S1/S2) in `corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md`: (a) anchors hit `source-excerpt.md` at the cited lines; (b) the comparison scope is bounded per R9; (c) `editorial_rows=2` is honest. All work read-only; scratch probes in `/tmp` deleted in-command.

## Work performed

- Located the audited change: `git diff 396c568 c4d4823` on the map turns the two r91 prose bullets into table rows S1/S2 (`claim-excerpt-map.md:38–41`), each `Excerpt path:line = source-excerpt.md:5`, `R9 mode = verbatim`, exact-anchor cells; inventory declaration goes `10 JSON / 0 editorial / 10 total / 6 anchors` → `10 / 2 / 12 / 8`. The committed rows are byte-identical to what `patches/M1-spence-rows.patch` specifies (integration preserved the patch's content).
- Reproduced the delivered checker receipt on the committed tree (`support_check.py`, sha `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`). Result: both S rows `PASS`, `EDITORIAL-ANCHORS 2/2`, no `WARN`, `RESULT PASS`, exit 0.
- Byte-level anchor checks with `grep -nF` against the committed excerpt files (the same fixed-string method R9 prescribes) for both S-row anchors in `source-excerpt.md` and for the cited `symbolism-clause-map.md:7/:8` clauses.
- Paired control for the WARN-closure claim: extracted the baseline map from git (`git show 396c568:...` → scratch) and ran the **same delivered checker** against it, isolating the map change from the tool change.
- R9 bounding review: read the R9 decision row and the Manual R9 gate / receipt-boundary text in `corpus/knowledge/r88-sourced-inspiration-decision-table.md`, the map's R9 declarations table and section text, plus the cluster `inspiration-note.md` and `README.md` (checked for any further editorial comparisons that `editorial_rows=2` would miss).
- External verbatim spot-check of the source text against the cited edition: fetched Project Gutenberg eBook 53080 (`https://www.gutenberg.org/files/53080/53080-h/53080-h.htm`) and searched for both anchor clauses and the passage lead.
- Discrimination control: scratch copy of the committed map with the S1 anchor cell mutated (`He called out “Earth,”` → `He called out “EARTH,”`); ran the delivered checker against it to confirm the PASS is load-bearing on exactly these anchor cells.
- Structural replay of the cluster: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster`.
- Checker-freeze evidence: `sha256sum` of both delivered checkers; `git diff --name-only 396c568 c4d4823 -- corpus/fixtures/check_bible.py` confirms the `ff9fd2aa…` checker is untouched this round.
- Supplementary, out of my seat's primary scope: two probes of the support command's contract paths named in C2 (missing inventory; missing map).
- Out-of-seat observation confirmed against the committed blob: the doubled `**Failed-gate disposition (clarified r92):**` header in the decision table (`:40`), and its provenance (`grep -n "Failed-gate"` in `patches/E1-edges.md` / `patches/E2-wording.md` shows a single header in both patches).

## Before → after measurements

All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`.

1. **Committed-tree receipt (after).**
   `python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster`
   Observed: `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8`; `PASS S1: editorial-row; mode=verbatim; anchor=found; 5:> …He called out “Earth,” and the solid land appeared.`; `PASS S2: editorial-row; mode=verbatim; anchor=found; 5:> …`; `RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12`; `SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; … MODES 12/12; VALIDATED-ROWS 12/12`; `RESULT PASS`; `EXIT=0`. No `WARN` lines.

2. **Baseline control (before; same delivered checker, baseline map in scratch).**
   `git show 396c568:corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md > /tmp/jcov2-baseline-map.md && python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster --map /tmp/jcov2-baseline-map.md`
   Observed: `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6`; `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)`; `RESULT PASS WITH WARNINGS`; `EXIT=0`. This isolates the closure to the map change: same tool, same excerpts, warning gone and editorial 0→2 on the committed map.

3. **Anchor byte checks (cited lines).**
   `grep -nF 'He called out “Earth,”' source-excerpt.md` → single hit: `5:> The beginning of this interesting book … He called out “Earth,” and the solid land appeared.`
   `grep -nF 'and the solid land appeared.' source-excerpt.md` → single hit, same line 5.
   In the citation source: `grep -nF 'He called out “Earth,”' symbolism-clause-map.md` → line 7; `grep -nF 'and the solid land appeared.' …` → line 8. The S-row comparison cells' claimed clause pairs match the two rows of `symbolism-clause-map.md` exactly.
   The checker's own span enforcement covers this too: span parsed from `source-excerpt.md:5`; both hits at line 5, no `outside-span` note.

4. **`editorial_rows=2` count.** `grep -c '^| S' claim-excerpt-map.md` → `2` (lines 40, 41); checker `EDITORIAL-ROWS 2/2`; `symbolism-clause-map.md` has exactly two comparison rows (lines 7–8), both covered; cluster `README.md`/`inspiration-note.md` name no further comparisons. Inventory arithmetic `10+2=12` is enforced by the checker parser. Honest.

5. **External verbatim spot-check.** `curl -sL https://www.gutenberg.org/files/53080/53080-h/53080-h.htm` → decoded text contains `He called out &ldquo;Earth,&rdquo; and the solid land appeared.` and `The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that ev…`. The in-tree line 5 matches the cited Gutenberg text for the lead sentence and both anchor clauses; the intervening span is elided with an explicit `[…]` marker, not silently dropped.

6. **Mutation control (discrimination).** Scratch copy with S1 anchor cell → `He called out “EARTH,”`; delivered checker → `FAIL S1: editorial-row; mode=verbatim; anchor=not-found`; `EDITORIAL-ANCHORS 1/2`; `RESULT FAIL`; `EXIT=1`. The S1/S2 anchor cells are load-bearing for the PASS.

7. **Structural replay.** `python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster` → `CLEAN: schema, citations, relations, timeline; 0 violations`; `EXIT=0`.

8. **Checker freeze.** `sha256sum corpus/tools/support_check.py corpus/fixtures/check_bible.py` → `55a5eb27…` (support command, changed this round per M2) and `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (check_bible, unchanged; `git diff --name-only 396c568 c4d4823 -- corpus/fixtures/check_bible.py | wc -l` → `0`). The "r92 checker UNCHANGED (ff9fd2aa)" statement holds for `check_bible.py`.

9. **Supplementary contract probes (out of seat scope).** Inventory-line-stripped scratch map → `FAIL: map must contain exactly one expected inventory declaration` / `RESULT FAIL` / `EXIT=1`; `--map /tmp/jcov2-does-not-exist.md` → `FAIL: claim-to-excerpt map not found` / `RESULT ERROR` / `EXIT=2`. Both match the C2 wording.

10. **Out-of-seat artifact.** `grep -c` in `corpus/knowledge/r88-sourced-inspiration-decision-table.md` → `**Manual R9 gate` 1, `**Receipt boundary:**` 1, `**Required record:**` 1 (R9 paragraphs intact); the R8 failed-gate paragraph at `:40` carries the header twice (`…(clarified r92):** **Failed-gate disposition (clarified r92):** **Owner:**…`), present in the committed blob and single in both `patches/E1-edges.md:11` and `patches/E2-wording.md:11`.

## Findings & named debt

Per-claim verdicts on the audited slice:

- **(a) Anchors at the cited lines — CONFIRMED.** Both S-row anchors are single in-span hits on `source-excerpt.md:5` (checker PASS receipts + `grep -nF`), and the mutation control shows the rows fail when the anchor is wrong.
- **(b) Scope bounded per R9 — CONFIRMED.** `source-excerpt.md:5` declares `verbatim` once in the map's R9 declarations table and repeats it in both S rows (R9's "declare one delivery mode … and repeat it in each map entry"); the underlying K'iche primary text is stated as not reproduced (`external-only`) and the comparisons "bounded editorial readings, not claims about K'iche symbolism or extra in-world canon". The rows are editorial, not R5 JSON claims, so the Manual R9 translation gate is not triggered; and the new receipt-boundary rule (lexical PASS necessary-not-sufficient) is not violated — the map does not present the checker output as an R9 review receipt.
- **(c) `editorial_rows=2` honest — CONFIRMED.** Exactly 2 rows, both comparison rows of `symbolism-clause-map.md` covered, count and arithmetic enforced by the checker (2/2, 12/12, 8/8).
- **Seat verdict on the C2 Spence-row slice: improved (bounded).** The unreferenced-declaration WARN closes, both rows are load-bearing, no harm observed anywhere in the slice. Bound: this is lexical-preflight evidence only (per R9's own receipt boundary); external spot-check covers the anchor clauses and passage frame against Gutenberg, not a full-passage character diff.

Named debt / observations:

- **JCOV2-1 (out of seat, committed-tree defect):** doubled `**Failed-gate disposition (clarified r92):**` header at `corpus/knowledge/r88-sourced-inspiration-decision-table.md:40`. Both source patches carry a single header, so this is an integration composition artifact, not a patch defect. It sits in the C1 landing area (E1/E2 wording), not in the Spence rows; the R9 paragraphs are unaffected (each appears exactly once). Suggested repair: delete one duplicated fragment. No effect on any claim judged here.
- **JCOV2-2 (minor, no action required):** the r92 S rows keep the authored-side anchors (`fictional-excerpts.md:8` for S1, `:7` for S2) only in the comparison cell / declarations table (`fictional-excerpts.md:7–8`), not as per-row line locators. Both authored anchors verified present at those lines; precision at file level is retained through the declarations table.

## Handoff

The three C2 Spence-row claims are confirmed on the committed tree with receipts above: WARN closure (paired before/after on one delivered checker), in-span anchors, honest 2/2 editorial count, R9-consistent bounding, plus a mutation control proving the rows discriminate. Freeze evidence: `check_bible.py` untouched (`ff9fd2aa…`), support command delivered at `55a5eb27…`; supplementary probes confirm its `RESULT FAIL`/exit 1 and `RESULT ERROR`/exit 2 paths.

Gaps and boundaries for the round record: (1) the full Gutenberg character diff of the whole excerpt line was not performed — only the two anchor clauses and the lead sentence were spot-checked (the `[…]` elision is explicitly marked); (2) M2's complete failure-class matrix, the README alignment, and the C1 boundary-doc certification are outside this seat and were not judged here; (3) JCOV2-1 (doubled header) is a real committed-tree artifact worth a one-line repair seat, flagged to the parent since it lies outside my judgment surface.