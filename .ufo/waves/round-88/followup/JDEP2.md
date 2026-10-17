# JDEP2 — Depth judge #2 (ledger verification)

Judged on the DELIVERED tree at `2ea9ef1` (baseline `dfd1fbc`), never on intent or scratch patches.
Scope: `corpus/knowledge/reference-ledger.md` — ETCSL row, heading broadening, diff scope, seed contract.
Method: read-only `git show` / `git diff` / `grep` / live-URL fetch; no tracked-file writes.

## Work performed

- Confirmed the tree under judgement: `git log --oneline -3` → HEAD `2ea9ef1`; `git status --porcelain` empty (clean).
- Diffed the ledger across the round: `git diff dfd1fbc..2ea9ef1 -- corpus/knowledge/reference-ledger.md` and `--numstat`.
- Isolated table rows in both revisions and diffed them alone (row-level, not line-level) to prove no existing row was altered.
- Byte-compared each pre-existing data row (PROV-O, JSON Schema, graphlib) across the two revisions via `md5sum`.
- Compared the header + separator lines across revisions.
- Ran a column census of the delivered table (row count, per-row column count, empty-cell scan).
- Verified the ETCSL locator claim (`lines 122–163`) against the live ETCSL page.
- Checked whether the checker reads the ledger; grepped all live (non-`reports/`) docs for the old heading text.
- Cross-checked the ledger's completeness against the real-world references cited by the delivered corpus (r87 cluster + new r88 M3 cluster).

## Before → after measurements

**Diff scope — exactly the intended additions, no existing row altered.**

Command: `git diff --numstat dfd1fbc..2ea9ef1 -- corpus/knowledge/reference-ledger.md`
Observed: `3	2	corpus/knowledge/reference-ledger.md` (3 insertions, 2 deletions — 1 new row + 2 reworded prose lines).

Command: `git diff dfd1fbc..2ea9ef1 -- corpus/knowledge/reference-ledger.md` (row-only view via `grep '^|'` on both revisions, then `diff`)
Observed: `5a6` — a single pure append; the only changed table line is the new ETCSL row. No `c`/`d` hunks on any existing row.

Command: md5 of each pre-existing data row, old vs new:
```
PROV-O      old=5ebf508c4df3e22825cd4db592d6e6b5  new=5ebf508c4df3e22825cd4db592d6e6b5
JSON Schema old=9d8c186fda1a169565435047f7035e95  new=9d8c186fda1a169565435047f7035e95
graphlib    old=e09812ba7bdcd2febd3af6ef6e3c06fe  new=e09812ba7bdcd2febd3af6ef6e3c06fe
```
All three byte-identical. Header + separator (`diff <(… sed -n '3,4p') …`) → "header/separator identical".

**Row shape / column census on the delivered tree.**

Command: python column census over `corpus/knowledge/reference-ledger.md`
Observed: 12 total lines; 6 table lines = 1 header + 1 separator + **4 data rows** (was 3); every data row `ncols=4`; `EMPTYCELLS: []` for all four rows → four columns populated on the ETCSL row, matching the header `Work / attribution | Rights question | AI-training permission question | Use here`.

**ETCSL row content (four columns, rights/training open, use bounded).**

- Col 1 (attribution): `University of Oxford, ETCSL, "Inana's descent to the nether world," composition 1.4.1 (composite text), <url>, lines 122–163` — institution-level attribution, no invented individual author.
- Col 2 (rights): "…has **not been determined here**; consult the corpus's credits/copyright information and applicable terms before reproducing protected expression." → open question, no rights grant asserted.
- Col 3 (training): "AI-training permission **has not been assessed or established**; public accessibility and attribution do not imply permission." → open question, three questions kept in separate cells.
- Col 4 (use): "Motif-level comparison only … Not an in-world source or canon." → scope bounded.

**Locator accuracy — verified against the live page.** Fetched `https://etcsl.orinst.ox.ac.uk/section1/tr141.htm`: the composite text's line span **122–163** runs from the tail of Erec-ki-gala's gate order (114–122: "let the seven gates … be bolted … had her clothes removed") through the **seven gate removals** — 129–133 (first gate, turban), 134–138 (beads), 139–143 (egg-shaped beads), 144–148 (pectoral), 149–153 (ring), 154–158 (measuring rod/line), 159–163 (seventh gate, *pala* dress). The row's description "entry through seven gates and removal of dress and regalia" is **accurate**, and the span endpoints are exact (122 = last instruction line; 163 = last line of the seventh gate). The row faithfully mirrors `corpus/fixtures/r87-myth-cluster/inspiration-note.md:5` (same framing, same rights wording), so the ledger entry is traceable to its in-repo source.

**seed.md:26–29 contract.** `cat -n corpus/knowledge/seed.md` → lines 26–29 = `## Sourced inspiration` + "enter through a reference ledger with the art lane's three distinct questions (attribution / rights / training permission), kept separate from in-world canon." The delivered row keeps the three questions in three separate cells and keeps the ledger separate from canon (heading parenthetical + closing paragraph). The contract is **satisfied**. (seed does not define row syntax; the new decision table says so explicitly and defers to the existing four-column format — confirmed at `r88-sourced-inspiration-decision-table.md:16`.)

**No live-document breakage from the heading change.** Grep of all non-`reports/` docs for the old heading text found no live quote of `Real-world method references`; only `reports/r33…r42-*.md` (archival round records) quote the old heading. `corpus/README.md:6` describes the ledger as "real-world method citations" (a description, not a heading quote). `corpus/fixtures/check_bible.py` does **not** read the ledger (grep for `ledger|reference` → only unrelated `claim_a/claim_b references` and `ambiguous_holder_references` code paths), so nothing mechanically depends on the heading string.

## Findings & named debt

**F1 — ETCSL row is well-formed, accurate, and contract-matching (the change under test).** Four columns populated; rights and training both recorded as open questions with no inference; use bounded to motif-level and explicitly not canon; locator verified against the live source. Diff is a pure append (`5a6`) with all three prior rows byte-identical and header/separator untouched. Heading broadening ("method references" → "references") and the closing-paragraph reword ("attribute method inspiration, not specific story facts" → "record real-world references, not fictional canon") are justified by the new non-method motif row and **preserve the boundary that matters** — the "(not in-world canon)" parenthetical and "No reference work is ingested as fictional canon" are retained. No live doc or checker depends on the old heading string.

**Verdict recommendation: IMPROVED.** The ledger gains a verified, contract-conforming real-world reference row with no harm to existing rows, to the canon boundary, or to any live consumer. The only qualitative loss is the dropped "method" qualifier in the heading/paragraph, which is required for consistency with the new motif-level row and does not weaken the canon/non-canon separation.

**F2 (named debt) — the ledger is incomplete against the delivered corpus: the r88 M3 Spence reference is unregistered.** The work commit lands `corpus/fixtures/r88-m3-maya-cluster`, whose `inspiration-note.md:5` and `source-excerpt.md:3` cite Lewis Spence, *The Myths of Mexico & Peru* (1913), p. 209, with a **delivered excerpt**. But `grep -c Spence corpus/knowledge/reference-ledger.md` → `0`: no Spence row exists on `2ea9ef1`. The newly landed decision table itself predicted this and asked for it — `r88-sourced-inspiration-decision-table.md:16`: "The available M1, M2, and M3 references (Kojiki, Völuspá, and Spence) are not in D3's ETCSL-only append; register the selected new reference(s) at integration and recheck all ledger rows." Integration registered only the r87 ETCSL citation (per the wave-spec C3 wording: "register the r87 ETCSL citation"). Net asymmetry on the delivered tree: the reference with **no** delivered text (ETCSL, external-only) is registered, while the reference **with** a delivered excerpt (Spence) is not. This is not a defect of the ETCSL row (which is exactly as specified) and does not make the ledger axis "harmed" — it is an integration-completeness gap. Recommend the r89 work wave (or a follow-up) add the Spence row using the same four-column format and the open-question rights/training defaults, then re-check all rows.

**F3 (soft debt) — the ETCSL row omits the delivery-status statement the decision table's own ledger rule asks for.** `r88-sourced-inspiration-decision-table.md:16` says the ledger's final cell should "state the limited purpose and passage/element, **and whether text is delivered or external-only**", and the passage row (line 14) requires external-only passages be marked `external-only / unverified`. The ETCSL row's Use cell states the purpose, the passage (lines 122–163), and the element, but does **not** state delivery status and does not carry the literal `external-only / unverified` marker. Delivery status is inferable (no ETCSL text is delivered anywhere in the corpus — grep confirms ETCSL appears only in the fixture note and this ledger row; the fixture excerpt is its own verse), so the omission is not misleading, but it is a literal inconsistency between two artifacts landed in the same commit. Low severity; fold into the F2 re-check.

**Note on the heading/paragraph broadening (no verdict impact).** Archival reports `reports/r33-…r42-*.md` quote the old heading `Real-world method references (not in-world canon)` and the old line "attribute method inspiration". These are historical round records, not live contracts, and were correctly left untouched; they now quote a superseded heading string. Flagging only so a future reader does not treat the stale quote as the live ledger text.

## Handoff

- **Seat:** JDEP2 — Depth judge #2 (ledger verification).
- **Deliverable:** this file, `.ufo/waves/round-88/followup/JDEP2.md`. No other repo writes; no commit; no push.
- **Verdict recommendation for `corpus/knowledge/reference-ledger.md` on `2ea9ef1`: IMPROVED.** Receipts: `git diff --numstat` = `3 2`; row-only diff = `5a6` (pure append); all 3 prior rows md5-identical; header/separator identical; 4 data rows × 4 populated columns; ETCSL rights/training recorded as open; use bounded; locator `122–163` verified against the live ETCSL page.
- **Contract check:** row format satisfies `seed.md:26–29` (three distinct questions, separate from canon); seed defines no row syntax, and the ledger's existing four-column format is the reference format per `r88-sourced-inspiration-decision-table.md:16`.
- **Named debt for the round record:** (F2) the r88 M3 Spence reference (delivered excerpt) is **not** registered in the ledger — carry to r89/integration; (F3) the ETCSL row omits the decision table's requested delivery-status/"external-only" marker. Neither harms the ETCSL row itself.
- **Gaps/limits of this seat:** verification is textual + one live-URL fetch; I did not re-run the C2 cluster checker (out of seat) and did not fetch the Project Gutenberg 53080 page to confirm the Spence p. 209 locator (only its in-repo citation form was checked). No test suite exists for the ledger; nothing mechanically validates it, so "no live breakage" rests on the grep evidence above.
