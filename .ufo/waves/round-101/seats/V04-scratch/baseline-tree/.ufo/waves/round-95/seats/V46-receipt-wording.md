# V46 — receipt-wording (round 95)

Seat: V46 `receipt-wording`. Scope: after all seats, audit the exact claim wording in
LOG.md's r95 declaration (`LOG.md:2751-2806`) against measured outputs — denominator
discipline: what exactly does `15/15` count, what exactly does `12/12` count — and list
the wording corrections L1 should apply at closure. Leaf seat: no nested agents, no
commits, no network; only this report written; mutation scratch under `/tmp/v46/`.

Baseline: r94 closure `fb118c4`. All measurements below were taken by this seat on the
working tree; nothing was verified from a plan or from another seat's numbers.

## 0. Poll status and revision pins

Producer artifacts were all present and complete when I froze the audit (16:46), and all
five producer reports had landed (`P1-tool-code.md` … `P5-knowledge-note.md`). 57 of the
64 seat reports had landed at freeze; still absent at that time: V09, V18, V29, V33, V56,
V57, V59 (plus this seat). Producer bytes were stable from 16:28 to 16:46. At finalization
(16:48) the seat count was 60; all producer sha256 values were re-checked and were unchanged
from the freeze, so every measurement below stands on the final revision.

```
$ sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json \
    corpus/tools/README.md corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md \
    corpus/fixtures/r95-crossing-aftermath/README.md corpus/knowledge/r95-aftermath-scope-note.md
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  corpus/fixtures/r95-crossing-aftermath/README.md
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
```

`git status --porcelain` at freeze: `M LOG.md`, `M corpus/tools/README.md`,
`M corpus/tools/map-obligations-contract.json`, `M corpus/tools/map_obligations.py`,
`?? .ufo/waves/round-95/`, `?? corpus/fixtures/r95-crossing-aftermath/`,
`?? corpus/knowledge/r95-aftermath-scope-note.md` — exactly the declared write scope.

## 1. Denominator ledger — every figure the declaration cites

Raw-obligation composition measured with the delivered tool's own `raw_obligations()`
(`first_appearance` / claim / relation / timeline):

```
r88-m3-maya-cluster     total=10  first_appearance=4 claim=4 relation=0 timeline=2
r93-m2-kojiki-cluster   total=12  first_appearance=4 claim=4 relation=2 timeline=2
r94-paired-crossing     total=14  first_appearance=5 claim=5 relation=1 timeline=3
r95-crossing-aftermath  total=15  first_appearance=5 claim=5 relation=1 timeline=4
```

| # | Declaration (LOG line) | Measured receipt | What the denominator counts | Verdict |
|---|---|---|---|---|
| D1 | "the self-test covers 20 cases" (2767-2768) | baseline contract = 20 cases; 20 `SELF-TEST` lines | persisted self-test cases | TRUE |
| D2 | "22 self-test cases including `map_missing` and `invalid_arguments`" (2769) | contract 22 cases (`map_missing` exit 2/`['map_missing']`; `invalid_arguments` exit 2/`['invalid_arguments']`); `--self-test` → 22 `SELF-TEST PASS` lines + `RESULT PASS` exit 0 | persisted self-test cases | TRUE |
| D3 | "exit 1 with a stable `schema_drift` FINDING ID" (2768) | `FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claim_records'` / `RESULT FAIL` exit 1; byte-identical across 3 runs; old tool on the same copy → `OBLIGATIONS raw=13 mapped=13` / `RESULT PASS` exit 0 | finding ID | TRUE (ID stable; detail text embeds the renamed key — see WC-6) |
| D4 | "r93 12/12, r94 14/14 … unchanged" (2770) | `OBLIGATIONS raw=12 mapped=12` PASS; `OBLIGATIONS raw=14 mapped=14` PASS | raw source-attributed obligations = mapped JSON-fact rows | TRUE (tool attribution needed — WC-4) |
| D5 | "frozen-r93 digest replay … unchanged" (2770-2771) | `SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS` exit 0 | pinned input digests | TRUE |
| D6 | "r87/r89 fail-closed behavior must be unchanged" (2771) | both exit 2 `unsupported_map` | exit code + finding ID | TRUE (r87 detail string changed — WC-5) |
| D7 | C2 before "5 entities / 1 relation / 3 events / 3 sources, 14 map obligations" (2782-2783) | r94: entities 5, relations 1, timeline 3, sources 3; `raw=14 mapped=14` | JSON record counts / obligations | TRUE |
| D8 | C2 after "5/1/4, 4 sources, 15 map obligations" (2783-2784) | r95: 5 / 1 / 4, sources 4 (`veil-verse`, `paired-clock`, `crossing-minute`, `aru-aftermath-note`); `OBLIGATIONS raw=15 mapped=15` PASS; `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17` | **15/15 = 15 raw obligations = 15 mapped JSON-fact rows** (5 `first_appearance` + 5 claims + 1 relation + 4 timeline). It is not the map's row total: the same map has 17 rows (15 + 2 editorial) | TRUE (see WC-4 for the 17/17 companion figure) |
| D9 | "14 inherited rows carried unchanged" (2784) | 14 shared pointers; parsed `(pointer, source_id)` pairs identical; exactly 14 differing cells across those rows, all in the path-qualification column (`r94-paired-crossing:*` → `r95-crossing-aftermath:*`) | parsed map values | TRUE as parsed-value; not byte-identical rows (WC-3) |
| D10 | "no new claims, no new entities/relations" (2784-2785) | `entities.json` / `relations.json` byte-identical to r94; 5 claims and 1 relation on both sides | record counts | TRUE |
| D11 | "`check_bible` CLEAN exit 0" (2785) | `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0 | checker verdict | TRUE |
| D12 | "census 168→169" (2786) | `git ls-tree -d --name-only fb118c4 corpus/fixtures/ \| wc -l` → 168; `ls -d corpus/fixtures/*/ \| wc -l` → 169 | fixture directories | TRUE |
| D13 | C3 before "exits 2 `unsupported_map`" (2791-2792) | baseline r88 → `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` / `RESULT ERROR` exit 2 | exit code + finding ID | TRUE |
| D14 | C3 after "**12/12 PASS over the r88 map's obligations**" (2792) | `OBLIGATIONS raw=10 mapped=10` / `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` / `RESULT PASS` exit 0 | **12/12 = total mapped rows (10 JSON-fact rows + 2 editorial rows)**; the obligations count is **10/10** (4 `first_appearance` + 4 claims + 0 relations + 2 timeline) | **DENOMINATOR ERROR — WC-1 required** |
| D15 | "with the same anchors/spans/modes" (2792-2793) | `map_obligations` reads neither the excerpt-path, line-span, mode, nor anchor columns (only the declared anchor *count* is parsed, then discarded); r88's anchors/spans/modes are covered by the unchanged `support_check` receipt `MODES 12/12` | tool scope | MISATTRIBUTED — WC-2 required |
| D16 | "`support_check` receipts on r88 (10 JSON + 2 editorial) and on r93/r94 unchanged" (2794-2795) | r88: `RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12` + `SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; MODES 12/12; VALIDATED-ROWS 12/12`; r93: 12/12 + 3/3 + 15/15 + 15/15; r94: 14/14 + 2/2 + 16/16 + 16/16 — identical before and after delivery; `support_check.py` bytes unchanged | row classes | TRUE |

Supporting commands and exact outputs:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
rc=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
rc=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath | tail -2
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS

$ python3 /tmp/v46/old_map_obligations.py /tmp/v46/br02b     # git fb118c4 tool, renamed claims key + row removed
OBLIGATIONS raw=13 mapped=13
RESULT PASS
rc=0

$ python3 corpus/tools/map_obligations.py /tmp/v46/br02b     # delivered tool, same scratch
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/13; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/15
FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claim_records'
RESULT FAIL
rc=1

$ python3 corpus/tools/map_obligations.py /tmp/v46/inv        # clean r94 copy, declared inventory decremented only
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/13; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16 MISMATCH
RESULT PASS
rc=0
```

The `/tmp/v46/br02b` copy keeps the map self-consistent (declared inventory decremented to
13 JSON facts / 15 total rows) so that the only finding is `schema_drift`: the BR-02 class
is caught by the drift detector itself, not by the inventory receipt. The looser variant
(row removed without touching the inventory line) additionally prints a `MISMATCH` and
still exits 1.

## 2. Collision ledger — same digits, different units

| fixture | map_obligations obligations | map row total (`TOTAL-ROWS`) | support_check `SOURCE-SUPPORT` | support_check `MODES` / `VALIDATED-ROWS` |
|---|---|---|---|---|
| r88 | **10/10** | **12/12** | 10/10 | **12/12** |
| r93 | **12/12** | 15/15 | **12/12** | 15/15 |
| r94 | 14/14 | 16/16 | 14/14 | 16/16 |
| r95 | **15/15** | 17/17 | 15/15 | 17/17 |

`12/12` has three distinct referents in this round (r88 rows; r88 modes; r93 obligations),
`15/15` has two (r93 rows/modes; r95 obligations), `14/14` has two (r94 obligations;
r94 source-support). Any closure sentence must name the tool, the unit, and the fixture.

## 3. Wording corrections for L1's closure note

**WC-1 (required, `LOG.md:2792`).** Replace "After: 12/12 PASS over the r88 map's
obligations" with e.g.:

> After: r88 `OBLIGATIONS raw=10 mapped=10` PASS exit 0 (`INVENTORY JSON-FACTS 10/10;
> EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12`). The obligation count is 10; the 12 is the map's
> total row count (10 JSON facts + 2 editorial rows), not an obligation count.

P2's own delivered addendum already states `OBLIGATIONS raw=10 mapped=10`, so the LOG
sentence contradicts the round's own documentation.

**WC-2 (required, `LOG.md:2792-2793`).** "with the same anchors/spans/modes" is outside the
tool's scope. Replace with: "with the r88 map unmodified; anchors/spans/modes are not read
by `map_obligations` (it parses only pointer and source-ID cells) and remain covered by the
unchanged `support_check` receipt (`MODES 12/12`)."

**WC-3 (precision, `LOG.md:2784`).** "14 inherited rows carried unchanged" → "14 inherited
rows carried with parsed (pointer, source-ID) pairs, spans, modes, and anchors unchanged;
only the path-qualification namespace column was re-namespaced to `r95-crossing-aftermath`."
(The delivered r95 map states exactly this.)

**WC-4 (precision, `LOG.md:2770` and `2783-2784`).** Attribute every bare ratio: "r93 12/12,
r94 14/14" → "`map_obligations` `OBLIGATIONS raw=mapped` r93 12/12, r94 14/14"; "15 map
obligations" → "15 obligations (`raw=15 mapped=15`); the same fixture's map has 17 rows
(15 + 2 editorial), matching `support_check`'s `MODES 17/17`".

**WC-5 (precision, `LOG.md:2771`).** "r87/r89 fail-closed behavior must be unchanged" holds
for exit code (2) and finding ID (`unsupported_map`); r87's *detail string* changed
(baseline "table needs one JSON fact pointer and one source-ID column" → delivered "pointer
cells must contain one canonical inline-code pointer"). Say "exit 2 `unsupported_map`
unchanged" rather than "behavior unchanged".

**WC-6 (precision, `LOG.md:2768`).** The `schema_drift` FINDING ID is stable; the detail
text embeds the unexpected key name, so quoted demo outputs legitimately differ per rename
target (P1 used `'assertions'`, V58 `'claims_renamed'`, this seat `'claim_records'`).

**WC-7 (optional).** Record the new receipt surface: the `INVENTORY …` line appears on any
map declaring `**Expected inventory:**` and is a receipt, not a gate — a tampered declared
inventory prints ` MISMATCH` at exit 0 (measured above). Without this, a later reader may
assume the inventory declaration is enforced.

## 4. Propagation note

V01's bottom line (`.ufo/waves/round-95/seats/V01-c1-before-after.md:175`) repeats "r88 now
12/12 PASS"; if closure text is drafted from seat bottom lines, the denominator slip
propagates. The correct figure is already stated by P1 (`P1-tool-code.md:111`), P2
(`P2-contract-docs.md:150`), V05, V24, V32, V31 (`NB-04`), and V58 (`F1`).

## 5. Bounds

This seat measured wording against outputs; it did not re-derive r88's row-by-row
anchor/span/mode correctness (V05/V35), the r95 note's scope semantics (V13/V43), doc parity
(V20), or the full 169-fixture sweep (V01/V15). No repo writes were made except this report;
mutation copies lived under `/tmp/v46/`. The 7 seat reports listed in §0 had not landed at
freeze, so nothing here depends on them.

**Bottom line: PASS** — C1, C2, and C3 all verify against measured receipts on the pinned
revision (tool `d1c239cc…`, contract `8173bb97…`); the declaration's C3 ratio and
anchors/spans/modes clause are the two required wording corrections (WC-1, WC-2), with
WC-3…WC-7 as precision items for L1's closure note.
