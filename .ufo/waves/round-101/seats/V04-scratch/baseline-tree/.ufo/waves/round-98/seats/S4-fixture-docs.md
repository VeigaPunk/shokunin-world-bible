# S4 fixture-docs — round 98

Seat: S4 (producer, byte-ownership). Baseline: r97 closure `9a3d648` (pre-round
bytes via `git show 9a3d648:<path>`). All commands ran from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested
agents, no commits, no pushes, no network. Writes: the two owned fixture paths below
(absolute), this report, and `.ufo/waves/round-98/seats/S4-scratch/`
(`inherited-rows-draft.txt`, `verify_rows.py`).

Owned and delivered (both rewritten from the r97 placeholder copies S3 left in the
new directory):

1. `corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md` — 15,028 bytes;
   sha256 `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba`
2. `corpus/fixtures/r98-clerk-filing/README.md` — 5,829 bytes;
   sha256 `32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926`

## A. Poll-wait record

- 20:27–20:28: `corpus/fixtures/r98-clerk-filing/` absent; `ls` polls every 20 s.
- 20:28:24: directory appeared with 10 files byte-identical to r97 (placeholder
  phase — S3 copies the 10-file tree, then extends 4). My first background poll
  (existence of `fictional-excerpts.md`/`timeline.json`/`sources.json`) hit at
  t=20 s on the placeholder.
- 20:28:55: S3's data edits landed (`clerk-maren`, `clerk-filing-open`,
  `clerk-filing-note`, new excerpt section). Second background poll, content-gated
  (`grep -q clerk-maren entities.json` AND `grep -q clerk-filing-open timeline.json`
  AND `grep -q clerk-filing-note sources.json fictional-excerpts.md`): POLL_HIT
  t=20 s, checks=1.
- 20:31: `S3-fixture-author.md` appeared. S3's report independently re-ran both
  tools on my map and got receipts identical to mine (its section C).
- No ABSENT condition arose and no stall-escape was needed. Hazard observed for
  verifiers (content, not existence): an existence-only poll is satisfied by the
  r97 placeholder copy — between 20:28:24 and my map write 20:30:21 the map and
  README existed with r97 bytes. My writes were gated on S3's data markers and
  re-verified afterwards.

## B. Map: canonical form, ALL 20 obligations

`claim-excerpt-map.md` declares `**Expected inventory:** 20 JSON facts; 2 editorial
rows; 22 total mapped rows; 18 distinct excerpt anchors.` and carries 20 canonical
`file.json#/pointer` rows in `## JSON facts` (six `first_appearance`, six claims,
one relation, seven timeline events).

**17 inherited rows (J01–J17) unchanged.** Row-by-row comparison against the r97
map (scratch script):

```
$ python3 .ufo/waves/round-98/seats/S4-scratch/verify_rows.py \
    corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md \
    corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
rows_a=17 rows_b=20
same-ID rows in b: 17
changed_inherited=0
```

Whole-line check that each inherited row differs from r97 only by the
path-qualification namespace string:

```
inherited_rows=17 identical_modulo_namespace=17 differing=[]
new_rows_in_r98=['J18', 'J19', 'J20']
map_line_numbers_identical: True
```

The inherited rows also keep identical map line numbers (J01–J17 at lines 22–38 in
both maps; e.g. `J17` at line 38 in each), because the three new rows are appended
after them — row order is not part of the `map_obligations` one-to-one comparison
(set comparison), and the tool PASSes.

**Anchor line numbers unchanged** (grep -nF on the r98 excerpt, first hit each):

```
$ for a in <the 13 inherited anchors>; do grep -nF -- "$a" corpus/fixtures/r98-clerk-filing/fictional-excerpts.md | head -1; done
12:> Tick 9: Aru carried the north lantern at Quiet Rise.
13:> Tick 9: Evin held the south bell at Salt Court.
17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
12:> Tick 9: Aru carried the north lantern at Quiet Rise.
13:> Tick 9: Evin held the south bell at Salt Court.
12:> Tick 9: Aru carried the north lantern at Quiet Rise.
13:> Tick 9: Evin held the south bell at Salt Court.
18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
20:> Their tick-10 decision depends on both ninth-bell entries: …
26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
37:> Tick 12: I was at Salt Court through the same agreed bell.
48:> Tick 13: I received Evin's response at the Chalk Stair.
```

Each hit falls inside the row's declared span (checked per row for all 17 rows;
`bad_rows = 0`), matching r97's spans 12, 13, 17, 12, 13, 12, 13, 18, 19, 20, 22-31,
33-42, 44-53.

**Excerpt is append-only** (inherited lines byte-preserved):

```
$ diff <(git show 9a3d648:corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md) \
       corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
53a54,64
> (blank line)
> ## Round 98 clerk filing (2026-10-17)
> (blank line)
> Newly authored fictional first-person note, attributed to in-world source ID `clerk-filing-note`, folio 8, lines 1–4. …
> (blank line)
> > Tick 14: I filed both pending accounts at the Chalk Stair registry.
> > I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
> > I assert no finding.
> > I reach no verdict and reconcile nothing.
> (blank line)
> Scope: this appended section is the harbor clerk's first-person filing record. …
(diff exit 1; the only hunks are additions 54-64)
```

**Three new rows, anchored in the new section only (lines 55-64):**

| ID | pointer | span | anchor |
|---|---|---:|---|
| J18 | `entities.json#/5/first_appearance` (`clerk-maren`) | 60 | `I am Maren, clerk of the Chalk Stair registry` |
| J19 | `entities.json#/5/claims/0` (`statement`, `source_id`) | 59-60 | `I filed both pending accounts at the Chalk Stair registry.` |
| J20 | `timeline.json#/6` (all six fields) | 55-64 | `Tick 14: I filed both pending accounts at the Chalk Stair registry.` |

```
$ grep -nF -- "I am Maren, clerk of the Chalk Stair registry" corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
$ grep -nF -- "I filed both pending accounts at the Chalk Stair registry." corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
$ grep -nF -- "Tick 14: I filed both pending accounts at the Chalk Stair registry." corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
```

All three source IDs resolve as `r98-clerk-filing:clerk-filing-note`; the new
`depends_on` edge `clerk-filing-open → acknowledgment-aru-records` is described in
the map's `## Timeline normalization and scope` (with J18/J19/J20 paragraphs naming
the no-finding/no-verdict/no-reconciliation lines 61-62), and the filing bound (no
finding; accounts unresolved) is stated there and in the README.

Inherited JSON parsed-value identity (r98 vs r97 closure blobs):

```
entities.json: inherited_prefix_identical=True len_a=5 len_b=6
timeline.json: inherited_prefix_identical=True len_a=6 len_b=7
sources.json: inherited_prefix_identical=True len_a=6 len_b=7
relations.json: inherited_prefix_identical=True len_a=1 len_b=1
contradictions.json: inherited_prefix_identical=True len_a=0 len_b=0
```

## C. Gates on the delivered r98 bytes (final run 20:31:30)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations          (exit 0)

$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
… PASS J01–J17 (inherited lines 12/13/17/18/19/20/26/37/48), PASS J18 (line 60),
  PASS J19 and PASS J20 (line 59), PASS S01, PASS S02
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors);
MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS                                                          (exit 0)

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                                          (exit 0)
```

## D. README

Line 3 states the counts `6 entities / 1 relation / 7 events / 7 sources` (confirmed
against the JSON: `entities=6 relations=1 events=7 sources=7`); line 11 states the
clerk bound ("an institutional filing record that asserts no finding and no
resolution; it reaches no verdict, reconciles nothing, and selects no winner … the
two first-person accounts … stand unresolved"); line 21 states 20 source-attributed
JSON pointer obligations (17 inherited + 3 new); lines 26-29 are the three replay
commands against `corpus/fixtures/r98-clerk-filing`. It is not the r97 placeholder:

```
$ git show 9a3d648:corpus/fixtures/r97-crossing-acknowledgment/README.md | sha256sum
d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f  -
$ sha256sum corpus/fixtures/r98-clerk-filing/README.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  corpus/fixtures/r98-clerk-filing/README.md
```

## E. Cross-checks, contradictions, bounds

- S3's report (section C) re-ran both tools on my map at the frozen bytes and
  reports receipts identical to mine (`support_check` 20/20 PASS, `map_obligations`
  raw=20 mapped=20 PASS); S3's interim run while the map was still the r97 copy
  showed exactly the three expected `missing_obligation` findings
  (`entities.json#/5/first_appearance`, `entities.json#/5/claims/0`,
  `timeline.json#/6`), which the delivered map discharges.
- S3's report (D1) says "At report time `README.md` is still byte-identical to
  r97's README (S4's rewrite not yet landed)". That was true at their check time
  but is stale for the delivered tree: my README rewrite landed 20:30:41 with
  sha256 `32efc78f…` (r97's was `d9387b7d…`). No action needed; recorded for
  verifiers who read that note.
- Read-only observation of S3's r95 repair: the whole-file diff is exactly one
  prose line (map line 49, no table row, no inventory line); I re-ran neither r95
  gate (out of my scope) but S3 records both r95 receipts byte-identical before and
  after with the freeze pin unchanged.
- Bounds of my receipts: `support_check`/`map_obligations` are lexical preflight and
  one-to-one mapping checks, not whole-claim entailment, source authenticity,
  chronology truth, rights, permission, or canon review. The J18/J19/J20 prose
  paragraphs in the map are my authored reading of the appended section (lines
  55-64); a verifier should re-read that section against them. Row order: the three
  new rows are appended after the inherited rows by design so every inherited row
  keeps its r97 map position and line number; the tools compare as sets and PASS.

## Bottom line

**PASS** — r98 `claim-excerpt-map.md` carries all 20 canonical pointer rows with the
17 inherited rows identical modulo namespace at unchanged map line numbers and
anchors verified by `grep -nF` at the same excerpt line numbers, the three new rows
anchored only in the appended filing-note section (lines 55-64); README states the
6/1/7 counts, 7 sources, 20 obligations, clerk bound, and replay commands; and on the
delivered bytes `check_bible` is CLEAN (exit 0), `support_check` is 20/20 PASS
(exit 0), `map_obligations` is raw=20 mapped=20 PASS (exit 0).
