# V54 — relation-scope-2 (round 96)

Seat: V54 relation-scope-2. Task: (a) `corpus/fixtures/r96-crossing-response/relations.json`
byte-identical to r95's; (b) the map's relation row anchor unchanged; (c) no new relation semantics.

Baseline: r95 closure `dcb2d92`. All paths under `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent tree; nothing written outside this report and `V54-scratch/`).

Poll-wait: fixture JSON present 17:38 (relations.json 17:38; sources/timeline rewritten 17:40),
Q4 report 17:42, Q5 map/README 17:43, Q5 report 17:43-17:44, Q1 tool revision v1 17:45 / v2 17:49,
Q6 note 17:47, Q2 contract + tool README revisions 17:51. Verification ran 17:44-17:53;
relations.json re-checked identical at 17:40, 17:44, 17:47, 17:49, and 17:53 (final `cmp` exit 0).

Revisions inspected (sha256, this seat's own reads):

| Artifact | sha256 |
|---|---|
| `corpus/fixtures/r96-crossing-response/relations.json` | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` |
| `corpus/fixtures/r95-crossing-aftermath/relations.json` | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` |
| `corpus/fixtures/r94-paired-crossing/relations.json` | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` |
| `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` | `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` |
| `corpus/fixtures/r96-crossing-response/README.md` | `ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456` |
| `corpus/tools/map_obligations.py` (Q1 revision, final read) | `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` |
| `corpus/tools/map-obligations-contract.json` (Q2 revision) | `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` |
| `corpus/tools/README.md` (Q2 revision) | `965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24` |

## 1. relations.json byte-identical r95 → r96 (claim a) — CONFIRMED

```
$ sha256sum corpus/fixtures/r95-crossing-aftermath/relations.json corpus/fixtures/r96-crossing-response/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r95-crossing-aftermath/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r96-crossing-response/relations.json

$ cmp corpus/fixtures/r95-crossing-aftermath/relations.json corpus/fixtures/r96-crossing-response/relations.json && echo "CMP: byte-identical"
CMP: byte-identical          # exit 0 (re-run at 17:49:59, still exit 0)

$ git hash-object corpus/fixtures/r96-crossing-response/relations.json corpus/fixtures/r95-crossing-aftermath/relations.json corpus/fixtures/r94-paired-crossing/relations.json
2804ae91240dbf34753bf955d4fab9ffeab0a8df
2804ae91240dbf34753bf955d4fab9ffeab0a8df
2804ae91240dbf34753bf955d4fab9ffeab0a8df
```

All three are the same 139-byte blob. Content:

```
[
  {
    "from": "aru",
    "to": "evin",
    "type": "agreed_co_stewardship_for_this_crossing",
    "source_id": "crossing-minute"
  }
]
```

`type` still encodes "for this crossing only"; no endpoint, type, or `source_id` changed. Also
byte-identical to r95 in the same fixture: `entities.json`, `contradictions.json`
(`cmp` exit 0; Q4's report independently declares the same hashes).

## 2. Map relation row anchor (claim b) — CONFIRMED (one rule-mandated cell change)

r96 map line 32 vs r95 map line 32, cell-by-cell parse of both delivered files:

```
SAME  ID                       'J11'
SAME  pointer+fields           '`relations.json#/0` (`from`, `to`, `type`, `source_id`)'
SAME  in-world source ID       '`crossing-minute`'
DIFF  qualified namespace      r95='`r95-crossing-aftermath:crossing-minute`' r96='`r96-crossing-response:crossing-minute`'
SAME  excerpt path             '`fictional-excerpts.md`'
SAME  line span                '19'
SAME  R9 mode                  '`verbatim`'
SAME  exact anchor             '`There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.`'
anchor byte-equal: True
cells equal except index 3: True
```

Exactly one relation row in the r96 map (`grep -c 'relations\.json#/'` → `1`). The only differing
cell is the path-qualification column, mandated by the map's own scope rule (map line 3) and applied
to all inherited rows (map line 16: "The 15 inherited rows carry the r94 JSON pointers, excerpt
anchors, spans, and delivery modes unchanged; only the path-qualification column names this fixture's
cluster path."). The anchor resolves at the same line number (r96 excerpts are a strict byte-prefix
extension of r95's; bytes 1-1845 preserved, append starts at line 32):

```
$ grep -nF 'There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.' corpus/fixtures/r96-crossing-response/fictional-excerpts.md
19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.

$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response | grep -E "J11|RESULT"
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
RESULT PASS                  # exit 0
```

`map_obligations.py` receipt (final Q1 revision `2b0ba815…`):

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                  # exit 0
```

Controls with the same revision: r95 `raw=15 mapped=15` PASS exit 0; r94 `raw=14 mapped=14` PASS
exit 0; r93 `raw=12 mapped=12` PASS exit 0; r88-m3 `raw=10 mapped=10` PASS exit 0; frozen r93 replay
`SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched` / PASS exit 0;
r87-myth-cluster exit 2 `unsupported_map`; r89-inspiration-paraphrase exit 2 `unsupported_map`
(both fail-closed, unchanged). Same receipts held on Q1's interim revision `44a6ffd4…`.

## 3. No new relation semantics anywhere (claim c) — CONFIRMED (fixture, map, tool, docs)

- **Repo-wide relation census** (python3 over all `corpus/fixtures/*/relations.json`): excluding r96
  156 rows / 10 distinct types (`agreed_co_stewardship_for_this_crossing` = 2); including r96 157
  rows / 10 distinct types (same type = 3). New types added: none. The single added row is the byte
  copy above.
- **No tracked relations file modified**: `git diff dcb2d92 --name-only` → `LOG.md`, `SCORECARD.md`
  only; `git status --porcelain` shows `?? corpus/fixtures/r96-crossing-response/` and
  `?? .ufo/waves/round-96/`. No other fixture's relations changed.
- **The new tick-12 row is a timeline event, not a relation**: `timeline.json#/4`
  `response-evin-salt-court`, actor `evin`, place `salt-court`, `depends_on:
  ["aftermath-missing-evin"]`; `relations.json` still holds exactly 1 record. Raw obligations = 5
  first-appearances + 5 claims + 1 relation + 5 events = 16.
- **Map scope unchanged in kind**: map line 3 still reads "one relation" (16 JSON facts declared,
  line 5); no editorial row touches the relation (S01/S02 remain the two Spence comparisons).
- **Checker**: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response` →
  `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0.
- **Tool diff (Q1 `2b0ba815…`; `git diff dcb2d92 -- corpus/tools/map_obligations.py`)**: relation
  records are still read exactly as `{from,to,type,source_id}` with only `source_id` extracted — the
  `raw_obligations_values` relation loop is behaviorally unchanged (`relations.json#/i` pointer +
  `source_value(record.get("source_id"), …)`). The only added relation-token lines are in the new
  `POINTER_MENTION` regex (`map_obligations.py:37-41`), a pointer-grammar detector for the
  legacy-dialect `dual_pointer` gate. The delta between Q1's two revisions is one regex tweak in that
  same detector (`` `[^`]*\.json# `` → `` `[^`]*\.json#[^`]*` ``). No new relation validation,
  typing, endpoint, or reciprocity rules; the three new findings (`schema_drift` entity-side,
  `inventory_mismatch` map counts, `dual_pointer` pointer mentions) never inspect relation content.
- **`dual_pointer` cannot change any relation-row verdict**: the detector fires only in legacy-header
  tables. The only legacy maps are r88-m3 (no relation rows; `relations.json` empty) and r87 (already
  exit 2 `unsupported_map`, unchanged). r93/r94/r95/r96 relation rows use the canonical header
  (`JSON fact pointer and fields`), so the mention path is never taken; all four exit 0 with the new
  tool. Scratch probe (`.ufo/waves/round-96/seats/V54-scratch/dual-probe2`, a copy of r88-m3 with
  `` (Aru; see `relations[0]`) `` appended to P1's cell):

  ```
  $ python3 corpus/tools/map_obligations.py .ufo/waves/round-96/seats/V54-scratch/dual-probe2
  FINDING dual_pointer: row P1 (line 23) names a second pointer token 'relations[0]' alongside entities.json#/0/first_appearance
  RESULT FAIL                  # exit 1
  ```

  The stable finding works and is pointer-level, not relation-level. (A control probe that put both
  tokens in one backticked cell hit the pre-existing `unsupported_map` exit 2 path, unchanged.)
- **Contract (Q2 revision `97b76bb8…`, landed 17:51)**: parsed against the r95 revision
  (`8173bb97…`): `scope`, `raw_files`, `map_grammar`, `legacy_pointer_dialect`, and `exit_codes` all
  IDENTICAL; the only change is `self_test.cases` 22 → 24, adding `{"id": "schema_drift", "exit": 1,
  "finding_ids": ["schema_drift"]}` and `{"id": "inventory_mismatch", "exit": 1, "finding_ids":
  ["inventory_mismatch"]}`. The contract's only relation tokens remain the unchanged scope sentence,
  the `relations.json` entries in `raw_files`/`allowed_pointer_files`, and the unchanged
  `legacy_pointer_dialect.pointer` description listing `relations[i]` — no relation semantics added.
  `python3 corpus/tools/map_obligations.py --self-test` now prints `SELF-TEST CASES 24/24 pinned`,
  24 `SELF-TEST PASS` lines, `RESULT PASS` exit 0; the r96 receipt is unchanged (`raw=16 mapped=16`,
  PASS exit 0).
- **Tool README (Q2 revision `965b29cd…`, landed 17:51; `git diff dcb2d92 --stat` = +50 lines, all
  additions)**: the only new relation-token line is the `dual_pointer` documentation ("a second
  backticked or bare legacy token — field path or bare entity/relation/timeline index"), i.e.
  documentation of the pointer-grammar scan, not relation semantics. The addendum also supersedes
  the r95 sentence "The inventory line is a receipt, not a gate" (line 144: "this addendum
  supersedes the r95 sentence"), documents the 24-case contract (line 161), and lists the
  non-regression set (line 169: r88/r93/r94/r95/r96 exit 0, frozen r93 replay exit 0, r87/r89
  fail-closed exit 2).
- **Docs**: r96 `README.md:3` — "the one inherited relation" copied by JSON value; counts "5
  entities / 1 relation / 5 events / 5 sources". `README.md:11` — "The crossing-only bound is
  likewise retained … It is not evidence of an alliance, a continuing practice, perpetual
  performance, a standing duty, or an external historical fact."
  `corpus/knowledge/r96-response-scope-note.md:23` records the scope bound as `relations.json#/0`
  "byte-identical to `corpus/fixtures/r95-crossing-aftermath/relations.json#/0`"; `:26` states no
  relation row changed. The r96 response note (`fictional-excerpts.md:33-42`) asserts no accusation,
  no winner, no new duty; its scope line states "the crossing-scoped agreement above is unchanged".

## 4. Observations and flags (reported exactly)

1. **C1b pinning resolved during verification (not this seat's axis).** At 17:50 the tool printed
   `SELF-TEST CASES 22/24 pinned`; after Q2's contract landed (17:51) the same command prints
   `SELF-TEST CASES 24/24 pinned` / `RESULT PASS`. Relation-relevant: no — neither added case
   (`schema_drift`, `inventory_mismatch`) touches relations. Reported for the C1 seats.
2. **Stale adjective carried again (same as r95 V51's flag).** r96 map line 50 retains "The new
   relation encodes only the agreement for this crossing…" although the map frames the inherited
   rows and the fixture adds no relation. Wording staleness only; the bound it states is unchanged
   and accurate.
3. **Strict-reading caveat for claim (b)**: the J11 row is not byte-identical as a whole — the
   path-qualification cell changes (`r95-crossing-aftermath:` → `r96-crossing-response:`), which the
   map's own declared rule requires. The anchor cell and all other cells are byte-identical.
4. **Q2's `corpus/tools/README.md` landed at 17:51 (`965b29cd…`, +50 lines).** The stale r95 sentence
   "The inventory line is a receipt, not a gate" remains in the historical text at line 119 but is
   explicitly superseded by the addendum (line 144: "this addendum supersedes the r95 sentence …").
   Relation-relevant: no — the added relation token is documentation of the pointer-grammar
   `dual_pointer` scan only.

## 5. Bottom line

PASS — r96 `relations.json` is byte-identical to r95's and r94's (sha256/cmp/git blob `2804ae91`,
139 bytes, re-checked at 17:49:59), the map's J11 relation row keeps its pointer, source ID, span 19,
mode, and anchor cell byte-identical (only the rule-mandated path-qualification cell changes,
exactly 1 relation row, support_check J11 PASS), and no new relation semantics appear in the
fixture, map, checker, tool revision, contract revision, or docs; the only remaining non-blocking
observation is the stale "new relation" adjective carried in map line 50 (bound itself unchanged and
accurate).
