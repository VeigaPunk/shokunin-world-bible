# F03 — c1-map (r94 FOLLOW-UP seat)

**Seat role:** FOLLOW-UP leaf, C1 map auditor. Scope: `corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md` — every source-attributed record (5 first-appearance pointers, 5 claims, 1 relation, 3 events = 14 obligations, plus separate editorial comparison rows) uses canonical `file.json#/pointer` syntax with exact in-span anchors and R9 modes, and each anchor string actually appears inside its declared excerpt span. Not in scope (other seats): raw-JSON/tool behavior of C2, whole-claim entailment, chronology truth, source authenticity.

**Environment pin:** lane HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8` (`git rev-parse HEAD`); WORK candidate `abbc3e0`; baseline `9c2eea3`. All commands run from repo root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Only this report was written by this seat; `git status --porcelain` shows only `?? .ufo/waves/round-94/followup/` (no corpus byte touched).

**Pinned input digests** (`sha256sum corpus/fixtures/r94-paired-crossing/<file>`):

```
ed9527c551049a6964adc872fbff722b4bdd6a53aa8713fbb6a5d92254e89a47  claim-excerpt-map.md
585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2  fictional-excerpts.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
f0209f90a6ce795211369bd900ac1d333d16eb0af123f1b170831e192660533c  timeline.json
```

---

## 1. Obligation inventory and one-to-one binding — PASS

Independent enumeration from the parsed raw JSON (my own script, not the C2 tool):

```
$ python3 - <<'PY'  (enumerate first_appearance + each claim + relations + timeline)
raw obligations: 14
by file: {'entities.json': 10, 'relations.json': 1, 'timeline.json': 3}
pointer resolution: all 14 resolve to their raw source_id
```

That is exactly the declared 5 first-appearance + 5 claim + 1 relation + 3 event split. The map's J-rows bind one-to-one to the raw obligations:

```
$ python3 - <<'PY'  (regex-extract J-row pointer cells, set-compare against raw)
raw==mapped (one-to-one): True
missing from map: []
phantom in map: []
rows: 14 distinct pointers: 14
```

Row counts by section, from my own table parse: `JSON rows: 14  editorial rows: 2` — matching the map's own declaration at `claim-excerpt-map.md:5` (`14 JSON facts; 2 editorial rows; 16 total mapped rows; 12 distinct excerpt anchors`). The "12 distinct excerpt anchors" figure recomputes to exactly 12 under my parser (`distinct anchors across all 16 rows: 12`).

## 2. Canonical pointer syntax, resolution, source-ID and namespace agreement — PASS

Every J-row pointer cell matches `` `<file>.json#/<segments>` `` with optional `(field, list)` note, resolves in the parsed JSON, and its raw `source_id` equals both the row's in-world source ID and the namespace qualification `r94-paired-crossing:<source_id>`:

```
OK J01: entities.json#/0/first_appearance span=12 hits=[12] mode=verbatim
OK J02: entities.json#/1/first_appearance span=13 hits=[13] mode=verbatim
OK J03: entities.json#/2/first_appearance span=12 hits=[12] mode=verbatim
OK J04: entities.json#/3/first_appearance span=13 hits=[13] mode=verbatim
OK J05: entities.json#/4/first_appearance span=17 hits=[17] mode=verbatim
OK J06: entities.json#/0/claims/0 span=12 hits=[12] mode=verbatim
OK J07: entities.json#/1/claims/0 span=13 hits=[13] mode=verbatim
OK J08: entities.json#/2/claims/0 span=12 hits=[12] mode=verbatim
OK J09: entities.json#/3/claims/0 span=13 hits=[13] mode=verbatim
OK J10: entities.json#/4/claims/0 span=18 hits=[18] mode=verbatim
OK J11: relations.json#/0 span=19 hits=[19] mode=verbatim
OK J12: timeline.json#/0 span=12 hits=[12] mode=verbatim
OK J13: timeline.json#/1 span=13 hits=[13] mode=verbatim
OK J14: timeline.json#/2 span=18-20 hits=[20] mode=verbatim
...
FAILS: none
```

Source-ID agreement observed in the same run: ten rows bind `paired-clock` (J01–J04, J06–J09, J12, J13), four bind `crossing-minute` (J05, J10, J11, J14); each row's namespace cell is exactly `` `r94-paired-crossing:<id>` ``. The map's own scope statement at `claim-excerpt-map.md:3` ("`source_id` values remain cluster-local in JSON and are qualified in the map as `(cluster path, source ID)` pairs") matches this layout, and the r88 namespace note at `claim-excerpt-map.md:18` is consistent with the inherited snapshot: `python3 -c "import json;print([s['id'] for s in json.load(open('corpus/fixtures/r88-m3-maya-cluster/sources.json'))])"` → `['veil-verse', 'paired-clock']`.

The field-annotation convention also matches the r93 canonical map: r94 `claim-excerpt-map.md:33-35` annotate timeline rows as `(tick, entity_id, place_id, depends_on, description, source_id)`, byte-identical in content to `corpus/fixtures/r93-m2-kojiki-cluster/claim-excerpt-map.md:30-31`.

## 3. Anchor-in-span mechanical verification — PASS (all 16 rows)

Method: my own parser reads the map table rows, then for each row tests `anchor in line` over the literal excerpt-file lines and checks that every hit line lies inside the declared span (independent of `grep`, `support_check.py`, and `map_obligations.py`). Result: `FAILS: none`, with every row reporting hits exactly inside its span (e.g. J01 hits=[12] span=12; J14 hits=[20] span=18-20; S01/S02 hits=[5] span=5).

**New-minute anchors (quote `grep -nF` evidence, all inside declared spans):**

```
$ grep -nF -- 'The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.' corpus/fixtures/r94-paired-crossing/fictional-excerpts.md
17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.        # J05, span 17
$ grep -nF -- 'After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.' ...
18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.           # J10, span 18
$ grep -nF -- 'There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.' ...
19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.       # J11, span 19
$ grep -nF -- "Their tick-10 decision depends on both ninth-bell entries: ... midpoint." ...
20:> Their tick-10 decision depends on both ninth-bell entries: ... at the midpoint.             # J14, span 18-20
```

(each command exited `exit=0`; the J14 command's full quoted anchor is the map's `claim-excerpt-map.md:35` anchor verbatim.)

**Inherited-anchor spot-check (4 required, 6 executed — all single-hit, in-span):**

```
$ grep -nF -- 'Aru carried the north lantern at Quiet Rise' .../fictional-excerpts.md
12:> Tick 9: Aru carried the north lantern at Quiet Rise.     # J01/J03/J12, span 12
$ grep -nF -- 'Evin held the south bell at Salt Court' ...
13:> Tick 9: Evin held the south bell at Salt Court.          # J02/J04/J13, span 13
$ grep -nF -- 'Tick 9: Aru carried the north lantern at Quiet Rise.' ...
12:> Tick 9: Aru carried the north lantern at Quiet Rise.     # J06, span 12
$ grep -nF -- 'south bell at Salt Court' ...
13:> Tick 9: Evin held the south bell at Salt Court.          # J09, span 13
$ grep -nF -- 'north lantern at Quiet Rise' ...
12:> Tick 9: Aru carried the north lantern at Quiet Rise.     # J08, span 12
$ grep -nF -- 'Tick 9: Evin held the south bell at Salt Court.' ...
13:> Tick 9: Evin held the south bell at Salt Court.          # J07, span 13
```

The inherited excerpt lines are byte-identical to the r88 snapshot — `diff -u corpus/fixtures/r88-m3-maya-cluster/fictional-excerpts.md corpus/fixtures/r94-paired-crossing/fictional-excerpts.md` shows only an appended hunk (`@@ -11,3 +11,10 @@`) adding the new minute; the diff exits 1 solely because of that addition, and the four inherited entity records and both inherited events are parsed-value identical (`diff -u` on `entities.json` first four records → exit 0; `timeline.json[:2]` → exit 0).

## 4. R9 modes — PASS

All 16 rows declare a mode drawn from the R9 set {verbatim, translation, paraphrase, summary}; all declare `verbatim`. Consistency with the excerpt surfaces: `fictional-excerpts.md:3` declares `**Delivery mode (R9):** `verbatim`` inline; the map's declaration table (`claim-excerpt-map.md:11-12`) declares `verbatim` for both `fictional-excerpts.md` and `source-excerpt.md`, and the mode is repeated in every row (per R9 "declare once, repeat in each map entry"). `support_check.py` resolves the mode for every row: `MODES 16/16`.

## 5. Editorial rows are separately labeled — PASS

`claim-excerpt-map.md:37` heads the section "Editorial rows (2 bounded Spence comparisons; not JSON facts)" and `claim-excerpt-map.md:39` disclaims in-world witness status. S01/S02 (`claim-excerpt-map.md:43-44`) carry anchors verified present at `source-excerpt.md:5`:

```
$ grep -nF -- 'He called out “Earth,”' corpus/fixtures/r94-paired-crossing/source-excerpt.md
5:> ... […] He called out “Earth,” and the solid land appeared.      # S01, span 5, exit=0
$ grep -nF -- 'and the solid land appeared.' ...
5:> ... He called out “Earth,” and the solid land appeared.          # S02, span 5, exit=0
```

They are not counted among the 14 obligations (my parser: `JSON rows: 14  editorial rows: 2`).

## 6. Cross-tool receipts (independent corroboration, not a substitute for §1–§3)

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

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing; echo "EXIT=$?"
OBLIGATIONS raw=14 mapped=14
RESULT PASS
EXIT=0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing; echo "EXIT=$?"
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

## 7. Observations and residual limits (none is a defect)

- J14 declares span `18-20` while its anchor text lives only on line 20; the span is a valid inclusive bound (my check and `support_check`'s rule are "all hits inside span"), but a reader should not infer that the anchor spans three lines. `claim-excerpt-map.md:48` and `:50` correctly bound what the receipt proves (lexical preflight, not entailment).
- `source-excerpt.md` carries no inline `Delivery mode` line (`grep -n "Delivery mode" source-excerpt.md` → exit 1); its `verbatim` mode is declared by the map's own declaration table (`claim-excerpt-map.md:12`) and accepted by `support_check.py` on that basis. This is the same structural pattern the r88 map uses and is within R9's "declare one delivery mode for each excerpt" wording, but the mode is the map's assertion, not the excerpt file's self-declaration.
- The r94 declaration table bundles both fictional namespaces into one row (`fictional-excerpts.md:12-20`) where the r88 map had one row per source (`r88-.../claim-excerpt-map.md:13-14`). No mapped row is affected (per-row spans still pin 12/13/17/18/19/18-20); it is a presentation deviation from the inherited style, not a coverage gap.
- `veil-verse` is not declared in the r94 map (grep for `veil-verse` in `claim-excerpt-map.md` → exit 1) and no JSON fact points at it; `support_check.py` emits no warning because it only flags declared-but-unreferenced paths. Consistent with the map's stated scope (`claim-excerpt-map.md:3`), and it does not affect the 14 obligations.
- Scope of this seat's verdict: mapping completeness, pointer syntax, anchor-in-span and mode presence only. It does not assert whole-claim entailment, translation fidelity, source authenticity, chronology truth, rights, permission, or canon.

**Bottom line: PASS** — all 14 source-attributed obligations plus 2 editorial rows carry canonical `file.json#/pointer` pointers that resolve to their raw `source_id`s under the declared `r94-paired-crossing:` namespace, every anchor string occurs only inside its declared excerpt span (new-minute anchors grep-verified at `fictional-excerpts.md:17-20`, inherited anchors at `:12-13`), all 16 rows declare R9 mode `verbatim`, and `support_check.py` (RESULT PASS, 16/16), `map_obligations.py` (raw=14 mapped=14, PASS) and `check_bible.py` (CLEAN) agree.
