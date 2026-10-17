# Q5 — fixture-docs (round 96)

Seat: Q5 fixture-docs. Exclusive write scope: `corpus/fixtures/r96-crossing-response/README.md`
and `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`, plus scratch under
`.ufo/waves/round-96/seats/Q5-scratch/`. No other writes; no commits. Baseline HEAD `60dba0c`
(r95 closure `dcb2d92`); lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` for every
path in this report.

## Deliverables

| File | Bytes | sha256 |
|---|---:|---|
| `corpus/fixtures/r96-crossing-response/README.md` | 4858 | `ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456` |
| `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` | 10172 | `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` |

README modeled on r95's: explicit-continuation opening, namespace/occasion comparison, the
unresolved-two-accounts bound, crossing-only bound, editorial tick/edge encodings,
`first_appearance` note, bounded Spence design prompt, 16 obligations (15 inherited + new
tick-12 row), and the three replay commands for `r96-crossing-response`.

Map authored in canonical form with **16 JSON facts / 2 editorial rows / 18 total rows /
14 distinct excerpt anchors** (`**Expected inventory:**` line), one `## JSON facts` table
(canonical `file.json#/pointer` cells, no legacy dialect, one pointer per row), the r95
`## R9 excerpt declarations` table extended (`fictional-excerpts.md:12-40`, four source
namespaces), and unchanged S01/S02 editorial rows.

## Poll-wait protocol

- First check 17:38: fixture dir absent. Byte copies landed 17:38; `fictional-excerpts.md`
  and `{sources,timeline}.json` landed by 17:38–17:39. Q4's producer report
  `Q4-fixture-json.md` appeared at +200s of polling; only then did I author against the
  frozen bytes. Q4's report confirms its mid-seat rewrite (joining comma off-line) happened
  at 17:39 before its receipts; my receipts were taken after that rewrite.

## Byte-prefix / inherited-row discipline (verified, not assumed)

- `head -c $(stat -c%s r95 fictional-excerpts.md) r96/fictional-excerpts.md | cmp - r95/fictional-excerpts.md`
  → `FULL r95 BYTES ARE PREFIX` (1845 B prefix of 2588 B; r96 lines 1–31 byte-identical,
  append starts line 32).
- Scratch `verify_inherited.py` (runs `grep -nF` per inherited anchor in the r96 excerpt):
  all 15 inherited anchors hit at their r95 line numbers — J01/J03/J06/J08/J12 `[12]`,
  J02/J04/J07/J09/J13 `[13]`, J05 `[17]`, J10 `[18]`, J11 `[19]`, J14 `[20]` (span 18-20),
  J15 `[26]` (span 22-31) → `INHERITED ALL-OK`.
- Scratch `compare_rows.py` (r95 map rows vs r96 map rows on pointer/span/anchor):
  `r95 fact rows=15 r96 fact rows=16`, J01–J15 all `SAME`, exactly one extra row:
  `('timeline.json#/4` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`,
  `source_id`)', '33-42', 'Tick 12: I was at Salt Court through the same agreed bell.')`
  → `ROWS ALL-OK`.
- Five inherited byte-copy files re-checked by me: `cmp` → IDENTICAL for
  `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`,
  `source-excerpt.md`. Parsed counts: entities 5, relations 1, contradictions 0,
  timeline 5, sources 5; `timeline[4].id == response-evin-salt-court`.

## Commands and observed outputs

`python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response` (revision
`55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`, r95-delivered,
unchanged during the round):

```
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
exit=0
```

All 18 rows `PASS` (16 JSON-facts rows + S01/S02); the four repeated references are the
inherited J01/J03/J12 and J02/J04/J13 shared anchors (same as r95, `DUPLICATE-ROWS 0`).

`python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response` — run at
four tool revisions while Q1's C1 hardening was landing (`d1c239cc…` r95 revision,
`99c7d764…`, `f9231239…`, and the pinned pair `8cbcdb51c3bdd90ab03fe175b69e58085e5161ca629d3e3d4acf3d2327fc50f3`
before and after the final run, unchanged). Every run, including the hardened revision:

```
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
exit=0
```

`python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response`:

```
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

`git status --short` after my writes: ` M LOG.md` (pre-seat), `?? .ufo/waves/round-96/`,
`?? corpus/fixtures/r96-crossing-response/`, `?? corpus/tools/dependency-freeze-contract.json`,
`?? corpus/tools/dependency_freeze.py` — no file outside my owned scope touched by this seat.

## Caveats for verifiers

- Q1's `map_obligations.py` was still changing during my receipts (contract
  `map-obligations-contract.json` still showed 22 self-test cases at my last check; the
  22→24 pin is Q2's artifact). My pinned PASS receipt is bracketed to revision
  `8cbcdb51…`; re-run under the final revision to pin the round's own record.
- Q4's `sources.json` / `timeline.json` mtimes (17:40) post-date the other byte copies
  (17:38) — consistent with Q4's documented pre-receipt rewrite; no post-receipt change
  was observed during my verification window.
- This seat verified structure and anchors only; whole-claim entailment and the
  unresolved-two-accounts bound are for adversarial verifier seats.

## Bottom line

PASS — both owned docs delivered; inherited 15 rows byte-discipline verified against r95
(anchors at identical line numbers, pointer/span/anchor identical), new row J16
`timeline.json#/4` span 33-42 anchored in the appended response section only; observed
`support_check` `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18` +
`RESULT PASS` exit 0, `map_obligations` `raw=16 mapped=16` `RESULT PASS` exit 0, `check_bible`
CLEAN exit 0.
