# F02 — c1-support (round-94 FOLLOW-UP verification seat, lore-shokunin)

**Seat role:** FOLLOW-UP verifier for the r94 C1/depth candidate `corpus/fixtures/r94-paired-crossing/` — run `support_check.py`, record exact inventory/support/mode rows, confirm R9 delivery modes are inline/in-map, and confirm the relation row exists in the map as an agreement-only encoding. LEAF scope: no corpus edits, no other seat reports, no commits.

**Revision tested:** lane HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8` (`65a9329 lore r94: declare DeepSeek FOLLOW-UP before dispatch`), candidate commit `abbc3e0 lore r94: checkpoint Luna WORK candidate pending DeepSeek review`. Working tree clean for the tested paths:

```
$ git status --porcelain corpus/fixtures/r94-paired-crossing/ corpus/tools/support_check.py
(no output, exit 0)
```

All commands run from the lane root with `python3`.

## 1. Primary command — RESULT PASS, exit 0

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing; echo "EXIT=$?"
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
EXIT=0
```

Exact receipt rows requested by the seat, verbatim: `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12`; `RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16`; `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16`; `RESULT PASS`, exit 0. All 16 rows report `PASS`; `DUPLICATE-ROWS 0`.

## 2. R9 delivery modes — inline and in-map

Independent structural probe of the map parser (read-only, imports the delivered tool):

```
$ python3 - <<'PY'  # imports corpus/tools/support_check.py, parses the map, prints modes
INLINE fictional-excerpts.md: ['verbatim']
INLINE source-excerpt.md: []
MAP expected-inventory: (14, 2, 16, 12)
MAP excerpt-declaration modes: {'fictional-excerpts.md': 'verbatim', 'source-excerpt.md': 'verbatim'}
MAP rows: 16
  J01..J14 kind=json mode=verbatim path=fictional-excerpts.md spans 12,13,12,13,17,12,13,12,13,18,19,12,13,18-20
  S01,S02 kind=editorial mode=verbatim path=source-excerpt.md span=5
```

- **Inline (in the excerpt file):** `corpus/fixtures/r94-paired-crossing/fictional-excerpts.md:3` → `**Delivery mode (R9):** \`verbatim\` — newly authored fictional text.` The tool's `MODE_DECLARATION` regex (`corpus/tools/support_check.py:12-16`) reads exactly this line; the probe confirms it resolves to `['verbatim']` for the in-world excerpt.
- **In-map (declaration table):** `claim-excerpt-map.md:7-12` (`## R9 excerpt declarations`) declares `fictional-excerpts.md:12-20` → `verbatim` (paired-clock + crossing-minute namespace) and `source-excerpt.md:5` → `verbatim` (Spence, delivered external comparison only).
- **In-map (per row):** every one of the 16 rows repeats its mode in the `R9 delivery mode` column; `MODES 16/16` means each row's declared mode matches its excerpt's resolved mode (`support_check.py:264-289`).
- **Observed nuance, not smoothed:** `source-excerpt.md` carries **no inline** `Delivery mode (R9)` line (probe: `INLINE source-excerpt.md: []`; `grep -rn "Delivery mode" corpus/fixtures/r94-paired-crossing/` returns only `fictional-excerpts.md:3` and the map table header at `claim-excerpt-map.md:9`). For S01/S02 the checker therefore takes the mode from the map declaration table via its documented fallback branch (`support_check.py:281-289`). This is inherited, not introduced by r94: `diff corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md corpus/fixtures/r94-paired-crossing/source-excerpt.md` → identical (exit 0), and the r88 baseline has the same shape and also passes (`python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster` → `RESULT PASS`, exit 0, `MODES 12/12`). The 14 in-world JSON rows satisfy the stronger inline-plus-map form; the 2 external editorial rows are map-declared only. Reported as observed for the parent's judgment; no defect claim is made beyond this fact.

## 3. Relation row exists in the map — agreement only

- **Row present exactly once:** `claim-excerpt-map.md:32` is `| J11 | \`relations.json#/0\` (\`from\`, \`to\`, \`type\`, \`source_id\`) | \`crossing-minute\` | \`r94-paired-crossing:crossing-minute\` | \`fictional-excerpts.md\` | 19 | \`verbatim\` | \`There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.\` |`. Parser probe classifies it `kind=json mode=verbatim path=fictional-excerpts.md span=19`; `DUPLICATE-ROWS 0`. Pointer uses canonical `file.json#/pointer` syntax and the row is counted inside the 14 JSON facts.
- **Raw relation matches:** `corpus/fixtures/r94-paired-crossing/relations.json` holds one relation: `{"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing", "source_id": "crossing-minute"}`.
- **Bounded to agreement, not perpetual performance:** the mapped anchor itself says "for this crossing only" (line 19); `claim-excerpt-map.md:48` states "The new relation encodes only the agreement for this crossing, not perpetual performance or alliance."; `sources.json:18` bounds `crossing-minute` to "one bounded crossing decision and agreement, not evidence of continuing performance, a standing alliance, or an external historical fact"; `README.md:9` repeats the same limit. A case-insensitive sweep `grep -rniE "perpetual|ongoing|forever|standing alliance|alliance|always share|indefinite" corpus/fixtures/r94-paired-crossing/` returns **only these bounding/negating statements** (sources.json:18, README.md:9, claim-excerpt-map.md:48) — no affirmative perpetual-performance or alliance assertion exists in the fixture.

## 4. Corroboration and limits

- Corroboration from the C2 tool (not this seat's primary check, run read-only for the relation mapping): `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing` → `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS` / exit 0.
- **Limits of this receipt:** `support_check.py` is documented as lexical preflight (fixed-string anchors, declared spans, R9 mode consistency) — it does not establish whole-claim entailment, mode fidelity, source authentication, chronology truth, rights, permission, or canon, and this seat does not claim those. This report verifies delivery/inventory/relation-row facts only; the independent whole-claim proposition review required by the spec is a separate FOLLOW-UP obligation (W31's minimal acceptance control) and is not discharged here.

## Bottom line

**PASS** — `support_check.py corpus/fixtures/r94-paired-crossing` → `RESULT PASS`, exit 0, with JSON-FACTS 14/14, EDITORIAL-ROWS 2/2, TOTAL-ROWS 16/16, MODES 16/16, VALIDATED-ROWS 16/16; the R9 modes are declared inline (`fictional-excerpts.md:3`) and repeated in-map for all 16 rows, and the single relation row `J11 = relations.json#/0` exists once and encodes only the bounded agreement ("for this crossing only"), with the sole nuance that the inherited external `source-excerpt.md` carries its mode in-map only (byte-identical to the passing r88 baseline).
