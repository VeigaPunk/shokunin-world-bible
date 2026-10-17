# F38 — knowledge provenance (r94 follow-up)

**Seat role:** verify `corpus/knowledge/r94-cross-myth-design-comparison.md` (and any other r94 knowledge files) for (a) opening source/verified-at/recheck metadata, (b) bibliography-row consistency with the r88/r93 `reference-ledger.md` rows (ETCSL, Spence 1913, Kojiki), and (c) absence of new unregistered source claims. All commands run from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`; no network fetches were made (per scope); no corpus bytes were modified.

## 1. Metadata block — PASS

`sed -n '1,4p' corpus/knowledge/r94-cross-myth-design-comparison.md | cat -n` returned:

```
1  source: `corpus/fixtures/r87-myth-cluster/{inspiration-note.md,...}`; ... `corpus/knowledge/{r87-provenance-chain-decision-table.md,r88-sourced-inspiration-decision-table.md,r93-r8-worked-example.md,reference-ledger.md}`; `.ufo/waves/round-93/recovery/{R25.md,R26.md}`
2  verified-at: 2026-10-17 — inspected the cited local records and excerpts; external URLs were not fetched in this pass.
3  recheck: before integrating any r94 claim, and whenever a cited excerpt, delivery mode, locator, or attribution changes; independently inspect external text/edition before making a source-text or translation claim.
```

The required triple opens the file at lines 1–3 with no preceding content (wave-spec `.ufo/waves/round-94/wave-spec.md:33`: "Knowledge opens with source/verified-at/recheck metadata"). The same `source:/verified-at:/recheck:` pattern is the existing convention (`corpus/knowledge/holder-assessment-boundary.md:11,39,50`).

Every path named in the line-1 `source:` list exists — a 20-path existence loop over the listed r87/r88/r93 fixture files, the four knowledge files, and `.ufo/waves/round-93/recovery/{R25.md,R26.md}` printed `OK` for all 20, zero `MISSING`.

The `verified-at` scope claim is internally accurate: the file makes no external-fetch claim, and its addendum states "The external URLs remain unfetched" (line 21).

## 2. File identity and provenance — PASS

- `git show --name-only --diff-filter=A abbc3e0 | grep knowledge` lists exactly one knowledge file for r94: `corpus/knowledge/r94-cross-myth-design-comparison.md`. `grep -rln "r94" corpus/knowledge/` returns only that file plus `r91-c9-watch.md` (an incidental r94 mention, not an r94 knowledge record). **There are no other r94 knowledge files.**
- `git log --oneline --all -- corpus/knowledge/r94-cross-myth-design-comparison.md` → single commit `abbc3e0` (the r94 WORK checkpoint). `git diff abbc3e0 HEAD --stat -- corpus/knowledge/` → empty; `git status --porcelain corpus/knowledge/` → empty. The file is unchanged since `abbc3e0`; the follow-up declaration `65a9329` did not touch it.

## 3. Bibliography rows vs the reference ledger — PASS (consistent; three non-substantive form divergences)

Field-by-field comparison of each r94 comparator row against `corpus/knowledge/reference-ledger.md`:

| Field | r94 knowledge row | Ledger row | Verdict |
|---|---|---|---|
| ETCSL work/locator | line 11: "**ETCSL**, “Inana's descent to the nether world,” composition 1.4.1, composite text, lines 122–163; `<https://etcsl.orinst.ox.ac.uk/section1/tr141.htm>`" | line 8: "University of Oxford, Electronic Text Corpus of Sumerian Literature (ETCSL), … composition 1.4.1 (composite text), https://etcsl.orinst.ox.ac.uk/section1/tr141.htm, lines 122–163" | Consistent. Same URL, composition, "composite text", lines 122–163. r94 abbreviates the institution to the acronym the ledger itself defines; no added claim. |
| ETCSL delivery status | line 11: "**External-only**: `corpus/fixtures/r87-myth-cluster/inspiration-note.md:5,21-23` gives the locator and says the passage text is not delivered." | line 8: "external-only / text not delivered at lore" | Consistent. Verified: `r87-myth-cluster/inspiration-note.md:5` carries the locator; lines 21–23 carry "`external-only / unverified inspiration` — its locators are verified but its text is not delivered". |
| Spence work/locator | line 12: "**Lewis Spence**, *The Myths of Mexico & Peru* (1913), Ch. V, “The Maya,” “The Creation-Story,” printed p. 209" | line 13: "Lewis Spence, *The Myths of Mexico & Peru* (London: George G. Harrap & Co., 1913), Chapter V, … printed p. 209, delivered excerpt at `corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md:5`" | Consistent. r94 drops the publisher imprint (an omission, not a new claim; a prior seat noted the fetched Gutenberg HTML carries no publisher string — `.ufo/waves/round-90/followup/JCOV2.md:237`). |
| Spence delivery status | line 12: "**Delivered mediated English** … R9 mode `verbatim` … not a K'iche-language text" | line 13: "Text is delivered in-tree" | Consistent. The `verbatim` mode is declared for `source-excerpt.md:5` in `r88-m3-maya-cluster/claim-excerpt-map.md:40-41` (rows S1/S2, `R9 mode` = `verbatim`). |
| Kojiki attribution | line 13: "**The Kojiki**, Part III, “The Door of the Heavenly Rock-Dwelling,” Terebess page `<https://terebess.hu/english/kojiki.html>`, which labels “B.H. Chamberlain, translator 1882.”" | line 14 + correction line 16: page "labels the translator only “B.H. Chamberlain, translator 1882”; the expansion to the fuller name is not verified" | Consistent, and uses the **corrected** phrasing: r94 does not repeat the superseded "Basil Hall" expansion. |
| Kojiki delivery status | line 13: "**Delivered translation**, excerpt lines 8–10, R9 mode `translation` …; one intervening sentence is omitted and the second selection has an ellipsis. The exact printed copy is unidentified. … No R5 support or R9 manual-review PASS is claimed." | line 14: "translation text is delivered in the named fixture but is not an in-world source, canon, or R5 support"; correction line 16: "one source sentence omitted … exact printed copy/edition remains unidentified" | Consistent on every asserted point. Verified in-file: `r93-m2-kojiki-cluster/kojiki-chamberlain-excerpt.md:6` declares `translation`; lines 8–10 are the three clauses; line 16 states the omission/ellipsis and unidentified printed copy. |

Non-substantive divergences observed (no conflict, reported for completeness):
1. **Spence URL form** — r94 line 12 cites the direct text URL `https://www.gutenberg.org/files/53080/53080-h/53080-h.htm`; the ledger row cites the landing page `https://www.gutenberg.org/ebooks/53080`. Both are Project Gutenberg eBook 53080; the direct form is exactly the one used by the cited in-tree fixtures (`r88-m3-maya-cluster/inspiration-note.md:5` and `source-excerpt.md:3`; identically in `r94-paired-crossing/inspiration-note.md:5`). Same work, no new source claim.
2. **Kojiki excerpt pointer span** — r94 line 13 writes "excerpt lines 8–10 … (`…/kojiki-chamberlain-excerpt.md:3-16`)"; the ledger registers `:8-10`. The prose line numbers match the ledger and the actual clause lines; the parenthetical file span also covers the work/locator/mode header (3–6), limit note (12), and correction (14–16). Pointer-form divergence only.
3. **Ledger-side blemish, not an r94 defect** — the ledger's Spence row (line 13) itself repeats `subsection “The Creation-Story,” “The Creation-Story,”`; the r94 row states the subsection once. r94 does not inherit the duplication.

## 4. Every cited pointer in the r94 knowledge file resolves — PASS

Observed content at each cited local pointer (all read in this pass):

- `r87-myth-cluster/lowwater-hymn-excerpt.md:5-7` = the three authored verse lines; `:3` declares `verbatim` — matches r94 line 11 ("newly authored `verbatim` fiction at `:5-7`"). `lowwater-hymn` present in `r87-myth-cluster/sources.json` (ids: shell-charter, lowwater-hymn, gate-witness, dune-register, tide-bell-tally).
- `r87-myth-cluster/symbolism-clause-map.md:7-14` = the eight clause rows; `claim-excerpt-map.md:46-53` = rows H1–H8 — matches r94 line 11.
- `r88-m3-maya-cluster/source-excerpt.md:3-7` = citation line 3, quoted Spence sentence line 5 ("He called out “Earth,” and the solid land appeared."), K'iche-prose limit line 7 — matches r94 line 12 and its quoted “Earth” / “solid land appeared” wording.
- `r88-m3-maya-cluster/fictional-excerpts.md:7-8` = the `veil-verse` lines "The chalk stair stays a crossing, never a map." / "We leave its name unowned in the rain."; `veil-verse` and `paired-clock` are the two ids in that fixture's `sources.json` — matches r94 line 12.
- `r88-m3-maya-cluster/symbolism-clause-map.md:7-8` = the two cited-clause rows; `claim-excerpt-map.md:40-41` = editorial rows S1/S2 — matches r94 line 12.
- `r93-m2-kojiki-cluster/archive-record-excerpt.md:5-12` = the M-17 register content; `m2-record-archive` is the fixture's single source id — matches r94 line 13.
- `r93-m2-kojiki-cluster/symbolism-clause-map.md:7-9` = the three clause rows; `claim-excerpt-map.md:33-41` = the editorial-rows section (heading line 33, rows S1–S3 at 37–39, closing limit line 41) — matches r94 line 13.
- Addendum pointers (lines 23–25): `r94-paired-crossing/sources.json#/2` = `{"id": "crossing-minute", "title": "Chalk Stair Crossing Minute", …}`; `fictional-excerpts.md:17-20` = the four minute lines naming Chalk Stair between Quiet Rise and Salt Court (17), the tick-10 meeting after both tick-9 entries (18), the one-crossing-only agreement (19), the both-entries dependency and one temporary midpoint mark (20); `entities.json#/4` = `chalk-stair` place with `first_appearance: crossing-minute` and one claim; `entities.json#/4/claims/0`; `relations.json#/0` = `{from: aru, to: evin, type: agreed_co_stewardship_for_this_crossing, source_id: crossing-minute}`; `timeline.json#/2` = tick 10, `depends_on: ["aru-ninth-bell","evin-ninth-bell"]`, `source_id: crossing-minute`. Counts printed `5 1 3` — matches the wave-spec's expected candidate counts.
- The claim that `paired-clock` is cluster-local under two path-qualified references (line 23) is consistent with the tree: both `r88-m3-maya-cluster/sources.json` and `r94-paired-crossing/sources.json#/1` carry `paired-clock`.

## 5. No new unregistered source claims — PASS

`grep -n "http" corpus/knowledge/r94-cross-myth-design-comparison.md` returns exactly **three** URLs, one per row: `etcsl.orinst.ox.ac.uk/section1/tr141.htm` (ledger line 8), `gutenberg.org/files/53080/…` (eBook 53080, ledger line 13), `terebess.hu/english/kojiki.html` (ledger line 14). No other real-world work, edition, translator, or tradition is named anywhere in the file; no fourth source family is introduced (the file itself states at line 17 that the record "do[es] not merge the three fictional clusters or add a fourth source/canon link"). All in-world source ids cited (`lowwater-hymn`, `veil-verse`, `paired-clock`, `m2-record-archive`, `crossing-minute`) are fictional `sources.json` records, not real-world references requiring ledger registration.

The addendum's two quoted receipts reproduce exactly on re-run:
- `python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing` → `CLEAN: schema, citations, relations, timeline; 0 violations` (exit 0) — verbatim as quoted at r94 line 27.
- `python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing` → `RESULT PASS` (exit 0), with `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12`, `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; MODES 16/16; VALIDATED-ROWS 16/16`, and anchors J05→line 17, J10→18, J11→19, J14→20 — every figure quoted at r94 line 29 matches the observed output.
- `python3 -c "json.load('.ufo/waves/round-94/wave-spec.json')"` shows `"followup": {"requested_model": "opencode-go/deepseek-v4.1-flash", "requested_seats": 32, "status": "not-dispatched", "result": null}` — the statement at r94 line 39 ("records the required DeepSeek follow-up as `not-dispatched` with no result") is accurate **as of this run**.

## 6. Notes for the integrator (non-blocking)

1. The line-1 `source:` list does not include `corpus/fixtures/r94-paired-crossing/*`, although the 2026-10-17 addendum relies on that delivered fixture ("the delivered local fixture was inspected for this update", line 21). The addendum names the r94 paths inline, and the metadata triple is authoring-time state, so this is a completeness observation, not a false claim. Extending line 1 when the addendum is integrated would remove the gap.
2. Line 39's `not-dispatched` statement will become stale as this follow-up wave lands; it is accurate now and should be treated as authoring-time state.
3. Scope limit of this seat: external pages were not fetched (no network per scope), so ETCSL/Spence/Terebess *attribution* claims are verified only for consistency with the registered ledger rows and the delivered in-tree excerpts — not against the live pages. The r94 file itself makes the same disclosure ("external URLs were not fetched in this pass", line 2; "no external body text was reviewed in this pass", line 37).

## Bottom line

**PASS** — `corpus/knowledge/r94-cross-myth-design-comparison.md` (the only r94 knowledge file, added at `abbc3e0` and unchanged since) opens with the required source/verified-at/recheck triple, every bibliography row is consistent with the registered ETCSL/Spence/Kojiki `reference-ledger.md` rows (using the corrected "B.H. Chamberlain" phrasing), all cited local pointers resolve to the claimed content, the two quoted receipts reproduce exactly, and no new unregistered source claim exists; only three non-substantive form divergences (Spence URL variant, Kojiki pointer span `:3-16` vs `:8-10`, omitted publisher imprint) and one metadata-completeness note were observed.
