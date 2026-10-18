# R5 — fixture-docs (round 97)

Seat: R5 fixture-docs. Exclusive write scope: `corpus/fixtures/r97-crossing-acknowledgment/README.md`
and `corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md`, plus scratch under
`.ufo/waves/round-97/seats/R5-scratch/` and this report. No other writes; no commits; no network.
Baseline HEAD `f3e09f9`; lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` for every path below.

## Deliverables

| File | Bytes | sha256 |
|---|---:|---|
| `corpus/fixtures/r97-crossing-acknowledgment/README.md` | 5304 | `d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f` |
| `corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md` | 12117 | `49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f` |

Map authored in canonical form: **17 JSON facts / 2 editorial rows / 19 total rows / 15 distinct
anchors**; one `## JSON facts (17 canonical pointers)` table (canonical `file.json#/pointer` cells,
one pointer per row, no legacy dialect); the 16 inherited rows are byte-copies of the r96
post-repair rows except the path-qualification column (`r96-crossing-response:` →
`r97-crossing-acknowledgment:`, 16 row lines rewritten, asserted); new row **J17**
`timeline.json#/5` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) →
`aru-acknowledgment-note`, span `44-53`, anchor line 48, mode `verbatim`. README carries replay
commands, counts 5 entities / 1 relation / 6 events / 6 sources, 17 obligations, and the
acknowledgment bound (receipt recorded; dispute unresolved; no reconciliation claimed).

## Poll-wait protocol (R4)

- r97 directory appeared 18:44:16 (10-file copy of r96); R4's authored three files landed 18:44:30.
  R4's producer report was polled on a 20 s cadence; my first poll (exact name `R4-fixture-json.md`)
  missed it — relaunched with an `R4*.md` glob: `READY try=11 report=.ufo/waves/round-97/seats/R4-fixture-author.md at 2026-10-17T18:50:28-03:00`.
- R4's report confirms the same bytes I receipted (r96 map post-repair sha `e851f068…`; r97 append
  `42a43,53`; new section lines 44-53; new source/event rows as quoted below).
- I never verified a plan: every check below ran against real files on disk.

## R4's r96 cosmetic repair (independent check, supporting C3-repair)

- Pre-repair committed bytes: `git show f3e09f9:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`
  sha `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` (== Q5's r96 delivered sha);
  current sha `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de`.
- `diff -u` = exactly two hunks: line 44 delimiter `|---|---|---|---|---|---:|---|---|` →
  `|---|---|---|---|---:|---|---|` (8→7 cells, matching its 7-cell header), and line 50's
  "The new relation encodes only the agreement for this crossing…" → the tick-12 event sentence.
- Data rows unchanged, proven with the tools' own parsers (imported `support_check.parse_map` /
  `map_obligations.parse_map_text`): `facts equal: True`, `pointers equal: True`,
  `inventory equal: True declared: [16, 2, 18, 14]`, `gating: []`.
- r96 receipts unchanged by the repair (my run, post-repair, tool revisions pinned below):
  `support_check` `SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18` / `RESULT PASS` exit 0;
  `map_obligations` `OBLIGATIONS raw=16 mapped=16` / `RESULT PASS` exit 0; `check_bible` `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0.
  (R4 additionally proved this under frozen `f3e09f9` tool revisions — agrees.)

## Inherited-row discipline (verified, not assumed)

- Byte-prefix: r96 `fictional-excerpts.md` (2588 B) is a strict byte-prefix of r97's (3410 B);
  append starts line 43 (`prefix: True`).
- All 16 inherited anchors `grep -nF` at identical line numbers in r97: J01/J03/J06/J08/J12 `[12]`,
  J02/J04/J07/J09/J13 `[13]`, J05 `[17]`, J10 `[18]`, J11 `[19]`, J14 `[20]` (span 18-20), J15 `[26]`
  (span 22-31), J16 `[37]` (span 33-42) → `INHERITED ANCHORS ALL-OK`. The excerpts/JSON lines are
  unchanged; the inherited rows' spans therefore still resolve to the same excerpt lines.
- Parsed-value identity: `sources.json` r96 rows=5 / r97 rows=6, `inherited-identical=True`;
  `timeline.json` same; new rows exactly `aru-acknowledgment-note` and `acknowledgment-aru-records`.
- Parser-level row diff (r96 map vs r97 map): `inherited J01-J16 identical (id/kind/mode/anchor/path/span): True`,
  `inherited pointers+source ids identical: True`, `extra rows in r97: ['J17']`,
  `new pointer row: [('timeline.json#/5', 'aru-acknowledgment-note')]`, `r97 gating findings: []`.
- Five byte-copy files (`entities/relations/contradictions.json`, `inspiration-note.md`,
  `source-excerpt.md`) are sha-identical between r96 and r97 (hashes below; matches R4's `cmp` claim).
- Structural checks: entities=5, relations=1, events=6, sources=6, contradictions=0; event fields
  id/tick/entity_id/place_id/depends_on/source_id all `True` (`depends_on: ["response-evin-salt-court"]`).

## Commands and observed outputs

All from the lane repo root, with `python3`.

`python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment`:

```
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

`python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment`:

```
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 ... PASS J16 (all inherited rows, anchors found at the same line numbers as r96)
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> ... He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> ... (same line)
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS
exit=0
```

`python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment`:

```
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS
exit=0
```

Post-write re-checks at 18:50:36 gave the same three results (byte state unchanged).

Fixture/file hashes at receipt time (stable across 18:45:07 → 18:50:36):

```
438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73  sources.json
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  timeline.json
8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c  fictional-excerpts.md
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
c279254bc7de0636d91823b6f336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
```

Tool revisions my receipts are pinned to: `support_check.py` `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`
(unchanged from the r96 frozen revision), `map_obligations.py` `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`
(R1's in-tree revision at receipt; R4 documents churn `2b0ba815…` → `c1881149…` → `86b52949…`),
`check_bible.py` `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.

`git status --short` shows no writes by this seat outside its scope (my files live inside the
untracked `corpus/fixtures/r97-crossing-acknowledgment/`; the `M` entries are R1/R2/R3/R4's).

## Caveats for verifiers

- `support_check`/`map_obligations` receipts are lexical preflight (inventory, anchors, spans, modes,
  pointer/source binding) — not whole-claim entailment and not a verdict on the acknowledgment
  bound; that reading is for adversarial verifier seats.
- R4 created the r97 `README.md`/`claim-excerpt-map.md` as byte-copy bases (r96 copies) before this
  seat landed; I replaced both. No post-report change to the fixture bytes was observed in my
  verification window (18:44:30 → 18:50:36 hashes identical).
- `corpus/fixtures/README.md`'s census text still states the r96 census (170 dirs, line 1217);
  `ls -d corpus/fixtures/*/ | wc -l` = 171 now (per R4). That file is read-only for this seat; the
  170→171 text update is not mine.
- `map_obligations.py` was still moving during the round (R1/R2); re-run the two tool commands under
  the closure revision to pin the round's own record.

## Bottom line

**PASS** — both owned docs delivered; 16 inherited rows carried byte-exact (namespace column only,
anchors at identical line numbers, parsed values identical, verified with the tools' own parsers),
J17 `timeline.json#/5` span 44-53 anchored in the new section only; r97 `support_check`
`INVENTORY 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15` +
`SOURCE-SUPPORT 17/17 … MODES 19/19; VALIDATED-ROWS 19/19` `RESULT PASS` exit 0, `map_obligations`
`raw=17 mapped=17` `RESULT PASS` exit 0, `check_bible` `CLEAN … 0 violations` exit 0; r96 receipts
independently confirmed unchanged by R4's cosmetic repair.
