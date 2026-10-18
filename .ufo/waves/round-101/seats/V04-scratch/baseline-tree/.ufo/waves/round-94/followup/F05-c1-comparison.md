# F05 — c1-comparison (FOLLOW-UP verification seat)

**Seat scope.** Review `corpus/knowledge/r94-cross-myth-design-comparison.md` (39 lines) for: (a) comparators named exactly (ETCSL, Spence, Kojiki); (b) delivered-vs-external status correct per the r87/r88/r93 records; (c) each analogy boundary explicitly stated; (d) no cultural-fact / shared-canon / rights claims; (e) cross-check the cited Spence naming/place contrast against the r88-m3 delivered excerpt wording.

**Method and limits.** Read-only inspection of the cited local records plus re-runs of the two commands the doc quotes. All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`. No network calls were made, so this seat verifies the doc's internal consistency with the r87/r88/r93 local records (which is what the seat asks); it does **not** authenticate any external text, and the doc itself claims no such thing (`r94-cross-myth-design-comparison.md:2` "external URLs were not fetched in this pass"). No corpus file, tool, or other seat's report was touched.

---

## 1. Comparators named exactly — PASS

| Doc row | Doc text (r94 doc line) | Local record it matches |
|---|---|---|
| ETCSL | line 11: `**ETCSL**, “Inana's descent to the nether world,” composition 1.4.1, composite text, lines 122–163; <https://etcsl.orinst.ox.ac.uk/section1/tr141.htm>` | `r87-myth-cluster/inspiration-note.md:5` — `A motif-level parallel is the journey through a threshold in “Inana's descent to the nether world,” composition 1.4.1 in the University of Oxford's Electronic Text Corpus of Sumerian Literature (ETCSL), composite text: <https://etcsl.orinst.ox.ac.uk/section1/tr141.htm>` … `lines 122–163 describe entry through seven gates`; `reference-ledger.md:8` repeats the same URL and `lines 122–163`. |
| Spence | line 12: `**Lewis Spence**, *The Myths of Mexico & Peru* (1913), Ch. V, “The Maya,” “The Creation-Story,” printed p. 209; <https://www.gutenberg.org/files/53080/53080-h/53080-h.htm>` | `r88-m3-maya-cluster/inspiration-note.md:5` and `source-excerpt.md:3` — same work, 1913, `Chapter V, “The Maya,” subsection “The Creation-Story,” printed p. 209`, same files-URL. |
| Kojiki | line 13: `**The Kojiki**, Part III, “The Door of the Heavenly Rock-Dwelling,” Terebess page <https://terebess.hu/english/kojiki.html>, which labels “B.H. Chamberlain, translator 1882.”` | `r93-m2-kojiki-cluster/kojiki-chamberlain-excerpt.md:3-4` — `Work: *The Kojiki*, English translation attributed by the source page to Basil Hall Chamberlain (1882), transcription at <https://terebess.hu/english/kojiki.html>.` / `Passage-level locator: Part III, “The Door of the Heavenly Rock-Dwelling”.` |

Exact-name check on the translator label: the doc uses **only** the page's own label. `kojiki-chamberlain-excerpt.md:14-16` correction states: `The cited page labels the translator only “B.H. Chamberlain, translator 1882”; the expansion to the fuller name is not verified by that page, and no added full-name source claim is required or made.` The r94 doc's `which labels “B.H. Chamberlain, translator 1882.”` reproduces exactly that corrected label and never expands it to `Basil Hall Chamberlain` (grep below shows the only `Chamberlain` occurrence in the doc is that quoted label). Same correction exists at `r93-m2-kojiki-cluster/inspiration-note.md:25-27` and `reference-ledger.md:16`.

```
$ grep -nE "Chamberlain|Basil" corpus/knowledge/r94-cross-myth-design-comparison.md; echo "exit=$?"
13:| **The Kojiki**, Part III, “The Door of the Heavenly Rock-Dwelling,” Terebess page <https://terebess.hu/english/kojiki.html>, which labels “B.H. Chamberlain, translator 1882.” Three non-contiguous clauses are selected: “eternal night prevailed,” the deities assemble, and the lands “again became light.” | **Delivered translation**, excerpt lines 8–10, R9 mode `translation` (`corpus/fixtures/r93-m2-kojiki-cluster/kojiki-chamberlain-excerpt.md:3-16`); one intervening sentence is omitted and the second selection has an ellipsis. The exact printed copy is unidentified. Existing fictional support is `m2-record-archive` (`sources.json`), the newly authored M-17 register at `archive-record-excerpt.md:5-12`; the editorial mappings are separately listed at `claim-excerpt-map.md:33-41`. No R5 support or R9 manual-review PASS is claimed. | … (rest of row 13 elided here; full row seen in §2/§3)
exit=0
```

One matching line only; `Basil` appears nowhere in the doc, so the unverified full-name expansion from the r93 correction is not reintroduced.

## 2. Delivered-vs-external status per the r87/r88/r93 records — PASS

**ETCSL row — doc says `**External-only**: … gives the locator and says the passage text is not delivered.`** Observed source record (`r87-myth-cluster/inspiration-note.md:21-23`):

```
21| Element marker (R8, r89): the ETCSL parallel is recorded as `external-only / unverified inspiration` —
22| its locators are verified but its text is not delivered; every canon claim in this cluster is independently
23| supported by the delivered in-world excerpts (see the four *-excerpt.md files).
```

Doc's cited span `inspiration-note.md:5,21-23` resolves exactly to those lines (verified by printing lines 5, 21, 22, 23). Doc's `lines 122–163` locator matches `inspiration-note.md:5`. No ETCSL text is claimed delivered anywhere.

**Spence row — doc says `**Delivered mediated English**: the in-tree excerpt is Spence's English prose, R9 mode `verbatim` for that wording (`…/source-excerpt.md:3-7`), not a K'iche-language text.`** Observed source record (`r88-m3-maya-cluster/source-excerpt.md:5,7`):

```
5| > The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
7| This is Spence's English prose about a story he labels “Kiche,” not a quotation from a K'iche-language edition. The locator resolves to the printed-page marker `[209]` in the linked text.
```

`r88-m3-maya-cluster/claim-excerpt-map.md:15` records the same split with the literal marker: `Delivered in-tree, verbatim from Spence's English prose; external comparison, not an in-world source. The underlying K'iche primary text is not reproduced (`external-only`).` Doc's `fictional-excerpts.md:7-8`, `symbolism-clause-map.md:7-8`, `claim-excerpt-map.md:40-41` all resolve to the correct rows (printed lines 7/8, 7/8, 40/41 respectively). Doc's statement `Factual register JSON claims instead cite `paired-clock`; it is not support for this comparison.` matches `r88-m3-maya-cluster/claim-excerpt-map.md:13` (`no JSON fact points to this source` for `veil-verse`) and the r88 JSON (all 10 facts cite `paired-clock`).

**Kojiki row — doc says `**Delivered translation**, excerpt lines 8–10, R9 mode `translation` (…/kojiki-chamberlain-excerpt.md:3-16); one intervening sentence is omitted and the second selection has an ellipsis. The exact printed copy is unidentified. … No R5 support or R9 manual-review PASS is claimed.`** Observed source records:

- `kojiki-chamberlain-excerpt.md:6` — `Delivery mode (R9): translation`; `:8-10` — the three clauses (`eternal night prevailed`, `eight hundred myriad deities assemble in a divine assembly`, `again became light`); `:5` — `its specific printed copy was not independently identified`; `:14-16` — the non-contiguity/ellipsis correction.
- `r93-m2-kojiki-cluster/claim-excerpt-map.md:12` — status cell: `External editorial comparison only; no R5 JSON support is claimed.`; `:14` — ``translation` describes Chamberlain's English rendering, not the source-language text.`
- `r93-m2-kojiki-cluster/inspiration-note.md:7` — `No JSON fact cites it, and this note does not claim R5 source support or an R9 manual-review PASS for the translation.`

The doc's `Delivered translation` label is also the correct side of the governing rule in `r88-sourced-inspiration-decision-table.md:58-59`: `Do not label the delivered / translation itself `not delivered`.` The doc does not. `archive-record-excerpt.md:5-12` and `claim-excerpt-map.md:33-41` (existing fictional support / editorial mappings) both resolve correctly (`m2-record-archive` declaration is `archive-record-excerpt.md:5-12` in the r93 map).

## 3. Analogy boundaries explicitly stated — PASS

Every row carries both a bounded-choice cell and a stop cell; no row leaves the boundary implicit:

- ETCSL (line 11): bounded choice `Keep the shore threshold, shell ring, and bowl as original local imagery; use at most a broad threshold motif as an editorial prompt. No one-to-one gate mapping or imported sequence.` / stop `Do not infer a shared event, gate identity/history, source characters or plot, objective supernatural return, or Sumerian cultural meaning from this comparison.`
- Spence (line 12): bounded choice `Keep a local authorial contrast about naming versus a crossing/place; do not adopt the creation outcome.` / stop `Spence's English retelling does not establish a K'iche-language source, a naming custom, all Maya/K'iche belief, direct borrowing, magic, or a historical event in the fiction. Do not turn the outside passage into an in-world witness.`
- Kojiki (line 13): bounded choice `Translate the comparison only into archive-record design: represent uncertainty, allow separately attributed annotations, and make the evidence limit explicit.` / stop `Do not infer original-language wording, translation fidelity, printed-edition identity, Japanese/Shinto cultural meaning, imported plot/ritual, or a historical claim.`
- Cross-row limits (line 17) close the set: `they do not merge the three fictional clusters or add a fourth source/canon link`.

Record shape matches the bounded artifact proposed by the cited r93 recovery seat (`r93/recovery/R26.md`, `## Bounded future artifact`): source work + exact locator; whether its text is delivered and in what form; the exact bounded clause or an explicit `external-only` marker; authored element path/line; classification as analogy/contrast; the fictional in-world source; and a sentence naming the inference that must stop — all seven requested fields are present as columns/cells.

## 4. No cultural-fact / shared-canon / rights claims — PASS

Reproducible scan:

```
$ grep -nE "canon|cultural|rights|permission|belief|Shinto|Maya|K.iche|Sumerian|Japanese|borrowing|authentication|fidelity" corpus/knowledge/r94-cross-myth-design-comparison.md
7| … not merged canon or a cultural-history claim. … An outside passage never becomes an in-world witness. “Delivered” below describes the local corpus representation, not authentication, fidelity, rights, or permission.
11| … Do not infer a shared event, gate identity/history, … or Sumerian cultural meaning from this comparison.
12| … not a K'iche-language text. … Spence's English retelling does not establish a K'iche-language source, a naming custom, all Maya/K'iche belief, direct borrowing, magic, or a historical event in the fiction.
13| … Do not infer original-language wording, translation fidelity, printed-edition identity, Japanese/Shinto cultural meaning, imported plot/ritual, or a historical claim.
17| … they do not merge the three fictional clusters or add a fourth source/canon link. … Rights and AI-training permission are not assessed by this record; keep their separate questions as recorded in the reference ledger. This is not original-language authentication, a rights/training-permission determination, or evidence that an external passage supports fictional canon.
25| **How the three comparisons inform design (without transferring canon).** … no outside text is an in-world source or witness. The three source families and their fictional namespaces remain separate.
```

Every hit is a disclaimer or a citation label; no sentence asserts a cultural fact, a shared canon link, or a rights/permission finding. The pointer `keep their separate questions as recorded in the reference ledger` is accurate: `corpus/knowledge/reference-ledger.md` has separate `Rights question` and `AI-training permission question` columns for the ETCSL row (`:8`), Spence row (`:13`) and Kojiki row (`:14`), each `not assessed` / `open question`.

Shared-canon check on the addendum's strongest statement — line 23: `The copied `paired-clock` source is cluster-local: `(r88-m3-maya-cluster, paired-clock)` and `(r94-paired-crossing, paired-clock)` are distinct path-qualified references, not identity evidence.` This reproduces the governing rule in `r88-sourced-inspiration-decision-table.md:99-102`: `source_id values are cluster-local identifiers. A source_id shared across clusters is a NAMESPACE COLLISION, not identity evidence — comparison keys are `(cluster-relative path, source_id)` pairs`. Observed data agrees: `r88-m3-maya-cluster/sources.json` and `r94-paired-crossing/sources.json` both define `paired-clock` with the same title/reliability note but under distinct fixture paths, and `r94-paired-crossing/claim-excerpt-map.md:18` labels them `r94-paired-crossing:paired-clock` vs `r88-m3-maya-cluster:paired-clock`.

## 5. Spence naming/place contrast vs the r88 delivered excerpt wording — PASS

Command and observed output:

```
$ python3 - <<'PY'
from pathlib import Path
ex = Path("corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md").read_text(encoding="utf-8").splitlines()
fic = Path("corpus/fixtures/r88-m3-maya-cluster/fictional-excerpts.md").read_text(encoding="utf-8").splitlines()
doc = Path("corpus/knowledge/r94-cross-myth-design-comparison.md").read_text(encoding="utf-8")
for q in ('\u201cEarth,\u201d', 'and the solid land appeared.'):
    print(f"quote {q!r}: in source-excerpt.md line 5? {q in ex[4]}")
for q in ('We leave its name unowned in the rain.', 'The chalk stair stays a crossing, never a map.'):
    print(f"{q!r}: line 7? {q in fic[6]}; line 8? {q in fic[7]}")
for q in ('\u201cEarth\u201d', '\u201csolid land appeared\u201d', 'never a map', 'name left unowned'):
    print(f"doc fragment {q!r}: {q in doc}")
PY
quote '“Earth,”': in source-excerpt.md line 5? True
quote 'and the solid land appeared.': in source-excerpt.md line 5? True
'We leave its name unowned in the rain.': line 7? False; line 8? True
'The chalk stair stays a crossing, never a map.': line 7? True; line 8? False
doc fragment '“Earth”': True
doc fragment '“solid land appeared”': True
doc fragment 'never a map': True
doc fragment 'name left unowned': True
```

Both quoted fragments the doc attributes to Spence occur verbatim in the delivered excerpt at `r88-m3-maya-cluster/source-excerpt.md:5`; both fictional counterparts occur verbatim at `r88-m3-maya-cluster/fictional-excerpts.md:7-8` (line 7 = crossing/"never a map", line 8 = unowned name). The doc's pairing order matches the r88 map exactly: `symbolism-clause-map.md:7` maps `“He called out “Earth,””` → `“We leave its name unowned in the rain.”`, and `:8` maps `“and the solid land appeared.”` → `“The chalk stair stays a crossing, never a map.”` (also `claim-excerpt-map.md:40-41`, S1/S2). The doc's line 37 restates the same anchors: `their exact anchors in the delivered Spence English excerpt at `source-excerpt.md:5` are contrasted with the local “crossing, never a map” / unowned-name wording`.

Consistency of the addendum's extension: line 25 says the Spence row informs `the inherited local contrast between an unowned name / crossing (`r88-m3-maya-cluster:veil-verse`, `fictional-excerpts.md:7-8`) and a named, bounded place in the new minute`. Observed: `r94-paired-crossing/fictional-excerpts.md:17` — `The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.` The named-and-bounded framing also matches the fixture's own editorial rows (`r94-paired-crossing/claim-excerpt-map.md:43-44`: `the fiction's named Chalk Stair is a bounded crossing, not a world-making act`; `a limited design contrast rather than a shared cosmology`). No conflation of the inherited unowned-name line with the new named place; the doc states both sides explicitly.

## 6. Reproduction of the addendum's quoted receipts — PASS (outputs match exactly)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J02: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J03: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J04: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
PASS J06: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J07: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J08: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J09: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J10: source-support; mode=verbatim; anchor=found; 18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
PASS J12: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J13: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J14: source-support; mode=verbatim; anchor=found; 20:> Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS
exit=0
```

The doc's line 29 tally (`JSON facts 14/14, editorial rows 2/2, total rows 16/16, distinct anchors 12/12, source support 14/14, editorial anchors 2/2, modes 16/16, validated rows 16/16`) and its cited anchors (J05@17, J10@18, J11@19, J14@20) reproduce exactly. Its line 27 structural receipt reproduces exactly. Its line 29 self-description (`it is a lexical/mode/span receipt, not a semantic verdict`) is consistent with `r88-sourced-inspiration-decision-table.md:77` (`support_check.py` is a lexical preflight) — the doc does not present either command as an admission verdict.

Addendum pointer check (all confirmed against the JSON):

- `sources.json#/2` → third entry `{"id": "crossing-minute", "title": "Chalk Stair Crossing Minute", "kind": "fictional minute", …}`.
- `entities.json#/4` → `chalk-stair`, `first_appearance: crossing-minute`; `entities.json#/4/claims/0` → `The crossing minute places Aru and Evin together at the Chalk Stair after both tick-9 entries.`
- `relations.json#/0` → `from aru, to evin, type agreed_co_stewardship_for_this_crossing, source_id crossing-minute`.
- `timeline.json#/2` → `paired-crossing-decision`, `tick 10`, `depends_on ["aru-ninth-bell","evin-ninth-bell"]` — both distinct tick-9 events, as the addendum states.
- `fictional-excerpts.md:17-20` is the minute's four lines; the addendum's line-by-line paraphrase (17 crossing identity, 18 tick-10 meeting after both entries, 19 one-crossing-only co-stewardship, 20 dependency + temporary midpoint mark) matches the delivered text.
- Line 39 `Required FOLLOW-UP — pending, not a result` matches `.ufo/waves/round-94/wave-spec.json`: `"followup": {… "status": "not-dispatched", "result": null}` and `work-receipt.json:54` `"followup": {"status":"not-dispatched","completed_seats":0,"admission":"pending"}`. The doc's override clause (line 21: `This addendum overrides only the preceding prospective statements that the minute was not yet delivered or checked`) covers both prospective statements I found (line 12 `The planned r94 minute may reuse this contrast only after its authored excerpt is delivered…`; line 17 `The planned r94 minute is an intended design target only until delivered and checked…`), so the filed prospective text is not left misleading.

## 7. Observations (non-blocking, no verdict impact)

- **O1 — literal marker not reused in the Spence row.** The row conveys the r88 split in prose (`Delivered mediated English` + `not a K'iche-language text` + stop sentence) but does not carry the literal `external-only` token for the underlying K'iche primary text that both fixture maps use (`r88-m3-maya-cluster/claim-excerpt-map.md:15,46`; `r94-paired-crossing/claim-excerpt-map.md:12`). The distinction is stated and nothing is misstated; only the token is absent from the knowledge row.
- **O2 — one header citation points at a superseded record.** Line 1 cites `corpus/knowledge/r87-provenance-chain-decision-table.md`, whose own banner (`:1-5`) reads `SUPERSEDED (round-88 closure) … Do not cite this table's notice/disclosure rows as delivered behavior.` The doc never relies on that table inline (its ETCSL status claim is grounded in `r87-myth-cluster/inspiration-note.md:21-23`), so the citation is non-load-bearing rather than wrong.
- **O3 — wording `The existing fictional support is `lowwater-hymn`` (line 11) uses "support" for "the fictional element being compared"; the column header (`Delivery and supported fictional source`) and the same row's `The comparison does not rely on ETCSL as delivered support` bound it, but the phrase alone could be skimmed as R5 source support.
- **O4 —** the acronym `ETCSL` is used unexpanded (the r87 note and `reference-ledger.md:8` expand it); the comparator is still named exactly as the corpus names it elsewhere.
- **O5 —** line 12 cites the whole-file span `source-excerpt.md:3-7` for the mode declaration where the r88 anchor is line 5; line 37 of the doc uses the precise `source-excerpt.md:5`, so no ambiguity results.
- **O6 — bare relative paths are disambiguated in-cell (verified, not a defect).** Several rows use fixture-relative paths (`fictional-excerpts.md:7-8`, `source-excerpt.md:5`, `symbolism-clause-map.md:7-8`, `claim-excerpt-map.md:40-41`), and those same relative names exist in more than one fixture (`fictional-excerpts.md:7-8` and `source-excerpt.md:5` are byte-identical in `r88-m3-maya-cluster` and `r94-paired-crossing`). Each occurrence is nevertheless qualified inside the same cell/parenthetical: line 12 names `r88-m3-maya-cluster/source-excerpt.md:3-7` before the bare paths, and addendum line 25 pairs `r88-m3-maya-cluster:veil-verse` with its `fictional-excerpts.md:7-8`. I found no unqualified bare path that could be read against the wrong fixture.

## Verification of this report's own citations

Every `path:line` pointer above was printed from the file at that line before being quoted; the lines for `r87-myth-cluster/inspiration-note.md:5,21-23`, `r87-myth-cluster/claim-excerpt-map.md:46,53`, `r88-m3-maya-cluster/source-excerpt.md:3,5,7`, `r88-m3-maya-cluster/fictional-excerpts.md:7,8`, `r88-m3-maya-cluster/symbolism-clause-map.md:7,8`, `r88-m3-maya-cluster/claim-excerpt-map.md:13,15,40,41,46`, `r93-m2-kojiki-cluster/archive-record-excerpt.md:5,12`, `r93-m2-kojiki-cluster/claim-excerpt-map.md:12,14,33,41`, `r93-m2-kojiki-cluster/kojiki-chamberlain-excerpt.md:3,4,5,6,8,10,14,16`, `r94-paired-crossing/claim-excerpt-map.md:12,18,43-44`, `r94-paired-crossing/fictional-excerpts.md:17`, `reference-ledger.md:8,14,16`, `r88-sourced-inspiration-decision-table.md:58-59,77,99-102`, `r87-provenance-chain-decision-table.md:1-5` and `work-receipt.json:54` all matched the text quoted here.

## What this seat did not check

- No external URL was fetched (scope rule: no network calls); "delivered" vs "external" was verified only against the local records and delivered excerpt files.
- The C1 JSON/prose entailment of the new minute is F06/F01/F34 territory; this seat only used the two receipts and the pointer checks above as corroboration of the comparison doc's own claims.
- `corpus/knowledge/r94-cross-myth-design-comparison.md`'s `verified-at: 2026-10-17` self-description was not independently time-stamped; only its content claims were checked.

## Bottom line

**PASS** — all three comparators are named exactly (including the corrected `B.H. Chamberlain, translator 1882` label), each row's delivered-vs-external status matches its r87/r88/r93 record, every analogy boundary and inference stop is explicit, the doc makes no cultural-fact/shared-canon/rights claim, the cited Spence contrast matches the r88-m3 delivered excerpt wording verbatim, and both quoted receipts reproduce exactly; six minor non-blocking precision observations are listed above (O1–O6, none affecting the verdict).
