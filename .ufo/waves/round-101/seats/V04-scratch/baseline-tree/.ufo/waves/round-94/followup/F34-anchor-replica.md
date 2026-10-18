# F34 — anchor-span-replica (FOLLOW-UP verification seat, r94)

Role: independent second implementer for anchor resolution. Re-verified, with a from-scratch span-checker (no reuse of F03's method, no reuse of `support_check.py` logic), that every anchor in `corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md` resolves inside its declared excerpt file and line span.

Write scope observed: this report only. No scratch files created (seat did not authorize a scratch dir); all checkers ran as in-memory heredoc scripts. No `corpus/` bytes were modified — verified by `git status` at the end.

## Method (mine, independent)

Inline python (heredoc, stdlib only), in three passes:

1. Parse `claim-excerpt-map.md` structurally: find `## JSON facts`, `## Editorial rows`, `## R9 excerpt declarations` by heading prefix; collect table data rows (skipping header/separator); extract the backticked exact anchor, excerpt path, and line span (`N` or `N-M`, inclusive); read each declared excerpt file's real line array.
2. Resolution test: join the declared span's raw lines with `\n` and test the anchor as a **literal substring** of that span text (not a normalized/whitespace-tolerant match); independently record every line number in the whole file containing the anchor, to detect resolution *outside* the declared span and duplicate-hit ambiguity.
3. Cross-checks with other implementations and with the raw JSON, plus negative controls on my own checker.

## Result 1 — inventory matches the map's own declaration

`claim-excerpt-map.md:5` claims `14 JSON facts; 2 editorial rows; 16 total mapped rows; 12 distinct excerpt anchors`.

Observed (my parser):

```
JSON-facts data rows: 14 | Editorial data rows: 2 | total: 16
distinct exact anchors: 12
R9 declaration rows: 2
row-class distribution: {'first_appearance': 5, 'claim': 5, 'relation': 1, 'event': 3} | total 14
namespace column distribution: {'r94-paired-crossing:paired-clock': 10, 'r94-paired-crossing:crossing-minute': 4}
```

The class split (5 first-appearance / 5 claims / 1 relation / 3 events) matches the scope sentence at `claim-excerpt-map.md:3`. Anchor sharing is intentional and matches the map's "12 distinct" claim: the anchor `Aru carried the north lantern at Quiet Rise` is used by J01/J03/J12 and `Evin held the south bell at Salt Court` by J02/J04/J13 (each ×3, no other duplicates).

## Result 2 — all 14 obligations' anchors resolve in their declared span (16/16 rows)

Every row, with the resolving line numbers actually observed:

```
J01  fictional-excerpts.md:12     resolve=YES  span_hit_lines=[12]   outside_span=[]  mode=`verbatim`
J02  fictional-excerpts.md:13     resolve=YES  span_hit_lines=[13]   outside_span=[]  mode=`verbatim`
J03  fictional-excerpts.md:12     resolve=YES  span_hit_lines=[12]   outside_span=[]  mode=`verbatim`
J04  fictional-excerpts.md:13     resolve=YES  span_hit_lines=[13]   outside_span=[]  mode=`verbatim`
J05  fictional-excerpts.md:17     resolve=YES  span_hit_lines=[17]   outside_span=[]  mode=`verbatim`
J06  fictional-excerpts.md:12     resolve=YES  span_hit_lines=[12]   outside_span=[]  mode=`verbatim`
J07  fictional-excerpts.md:13     resolve=YES  span_hit_lines=[13]   outside_span=[]  mode=`verbatim`
J08  fictional-excerpts.md:12     resolve=YES  span_hit_lines=[12]   outside_span=[]  mode=`verbatim`
J09  fictional-excerpts.md:13     resolve=YES  span_hit_lines=[13]   outside_span=[]  mode=`verbatim`
J10  fictional-excerpts.md:18     resolve=YES  span_hit_lines=[18]   outside_span=[]  mode=`verbatim`
J11  fictional-excerpts.md:19     resolve=YES  span_hit_lines=[19]   outside_span=[]  mode=`verbatim`
J12  fictional-excerpts.md:12     resolve=YES  span_hit_lines=[12]   outside_span=[]  mode=`verbatim`
J13  fictional-excerpts.md:13     resolve=YES  span_hit_lines=[13]   outside_span=[]  mode=`verbatim`
J14  fictional-excerpts.md:18-20  resolve=YES  span_hit_lines=[20]   outside_span=[]  mode=`verbatim`
S01  source-excerpt.md:5          resolve=YES  span_hit_lines=[5]    outside_span=[]  mode=`verbatim`
S02  source-excerpt.md:5          resolve=YES  span_hit_lines=[5]    outside_span=[]  mode=`verbatim`

RESOLVED_IN_SPAN total: 16/16   JSON-facts: 14/14   editorial: 2/2
MISSES: none
rows resolving OUTSIDE their declared span: none
rows whose declared span has empty lines: none
non-verbatim modes: none
```

**Verified count: 14/14 obligations (plus 2/2 editorial rows = 16/16 total). Zero misses.**

Declaration rows also check out against real bytes: `fictional-excerpts.md:12-20` (map line 11) is non-empty and contains exactly the two `paired-clock` lines (12, 13) and the four `crossing-minute` lines (17–20); `source-excerpt.md:5` (map line 12) exists and contains the Spence sentence `He called out “Earth,” and the solid land appeared.` (`True`, line length 199 chars).

## Result 3 — negative controls: the checker discriminates

A checker that passes everything is worthless, so I probed it with deliberately wrong inputs:

```
N1 anchor-mutation 'north'->'south' vs fictional-excerpts.md:12   resolve= False (expect False)
N2 J14 anchor vs tightened span 18-19                             resolve= False (expect False)
N3 J14 anchor vs declared span 18-20                              resolve= True  (expect True)
N4 in-world anchor against source-excerpt.md:1-7                  resolve= False (expect False)
N5 'Tick 9: Aru carried the north lantern at Quiet Rise.' in L12  resolve= True  (expect True)
N6 same anchor vs line 11 only                                    resolve= False (expect False)
```

All six behaved as expected, so the PASS above is a discriminating result, not a vacuous one.

## Result 4 — corroboration from two independent implementations

Different code paths, run as-is on the live fixture:

- `python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing` → `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12`, `ANCHORS repeated-references=4; DUPLICATE-ROWS 0`, then `PASS J01 … PASS S02`, `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; MODES 16/16; VALIDATED-ROWS 16/16`, `RESULT PASS`, `SUPPORT_CHECK_EXIT=0`.
- `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing` → `OBLIGATIONS raw=14 mapped=14`, `RESULT PASS`, `MAP_OBLIGATIONS_EXIT=0`.

My independent anchor/span verdict agrees with both; neither tool was used as my method.

## Result 5 — corroborating cross-checks (secondary, beyond the seat's core claim)

- **Pointer + source-ID binding** (my own JSON walk of `entities.json`, `relations.json`, `timeline.json`): all 14 pointers resolve to the stated target, listed fields exist, and the bound `source_id`/`first_appearance` equals the map's "In-world source ID" column for every row. `POINTER/BINDING FAILURES: none`.
- **Inherited-lineage claim** (`claim-excerpt-map.md:18` says inherited rows retain r88 anchors): `r88-m3-maya-cluster/fictional-excerpts.md` lines 12 and 13 are byte-identical to the r94 fixture's lines 12 and 13 (`True True`), and all six inherited anchor strings resolve verbatim in both files. The r94-only lines (15–20, the `crossing-minute` block) are absent from r88, as expected for a continuation.
- `git status` (run after all checks): no `corpus/` file reported modified; only this report file is new.

## Observations (non-failures, recorded for the parent)

1. **J14's span is a superset**: it declares `fictional-excerpts.md:18-20` but the anchor text resolves entirely on line 20; lines 18 and 19 are separately mapped by J10 and J11. This is a wider-than-needed but non-violating span — no miss, no out-of-span hit. Flagged only because a stricter reader might expect the span to start at 20.
2. Every anchor resolves on exactly one line and no anchor resolves anywhere outside its declared span, so no row is ambiguous between two candidate excerpts.
3. This seat verified **anchor resolution only** — not whole-claim entailment, source authenticity, rights, or canon (out of scope here).

## Bottom line

**PASS** — my independent from-scratch span-checker resolved 14/14 obligation anchors (16/16 rows including the 2 editorial comparisons) inside their declared excerpt files and line spans, with zero misses and zero out-of-span hits, confirmed by passing negative controls and by `support_check.py` (exit 0) and `map_obligations.py` (exit 0).
