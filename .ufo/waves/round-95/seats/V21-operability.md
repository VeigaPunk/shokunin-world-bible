# V21 — operability (round 95)

Seat: V21 operability. Exclusive write scope: this report only. No product file written, no
commit, no network. All commands run from the repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Baseline r94 closure `fb118c4`
(verified: `git rev-parse HEAD` → `fb118c42038ed27a747eec704b9aab41bb4b2ebe`).

Task as seated: run **every command documented in P4's r95 README and P5's note exactly as
written**, run the **tools README Round-95 addendum** commands, confirm the **0/1/2 exit
contract** holds on the paths the docs claim, note `--help` RESULT-less behavior consistency,
and report any documented command that fails as written.

## 0. Poll-wait and revision freeze

Two background polls (20 s cadence, 40 tries): a presence poll on the declared artifact paths
and a content-marker poll (tool contains `schema_drift`; contract has 22 cases incl.
`map_missing`/`invalid_arguments`; README contains `Round-95`; P4 README+map; P5 note; ≥5 P
seat reports). Landing order observed: P3 fixture JSON 16:18, P4 README+map 16:21, P5 note
16:22, P1 tool 16:22→16:26 (two writes), P2 contract 16:27, P2 README addendum 16:28; all five
P reports present at poll `try=34` (`ALL_PRESENT`). No producer artifact was verified before it
existed; mid-flight states were re-checked after landing (see §4).

Frozen revision used for every receipt below (sha256, re-verified at 16:31):

```
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  corpus/fixtures/r95-crossing-aftermath/README.md
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
```

## 1. P4's README replay block (README.md:26–28) — run exactly as written

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations        EXIT=0  stderr_bytes=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
... PASS J01..J15, PASS S01, PASS S02 ...
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                                                       EXIT=0  stderr_bytes=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                                                       EXIT=0  stderr_bytes=0
```

All three commands succeed as written. Every documented count is reproduced: README:21 says
"15 source-attributed JSON pointer obligations" → `raw=15 mapped=15`; the map's declared
inventory (map:5, `15 JSON facts; 2 editorial rows; 17 total mapped rows; 13 distinct excerpt
anchors`) matches the tool's `INVENTORY … 15/15; 2/2; 17/17` and support_check's
`DISTINCT-ANCHORS 13/13`; README:3 says "5 entities / 1 relation / 4 events / 4 sources" →
`json.load` counts 5/1/4/4/0 (contradictions `[]`).

## 2. P5's note receipts block (note:42–48) — run exactly as written

Same three commands, quoted in the note with `# … exit 0` comments. Observed:

- `check_bible` → `CLEAN: schema, citations, relations, timeline; 0 violations`, EXIT=0 — matches note:44.
- `support_check` → `JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13; MODES 17/17; VALIDATED-ROWS 17/17` / `RESULT PASS`, EXIT=0 — matches note:46 word for word.
- `map_obligations` → `OBLIGATIONS raw=15 mapped=15` / `RESULT PASS`, EXIT=0 — matches note:48.

No documented command in the note fails as written.

Additionally I checked every path/line the note cites (read-only `pathlib` probe): all exist and
land where claimed — `sources.json:21` = `"id": "aru-aftermath-note"`, `timeline.json:33` =
`"id": "aftermath-missing-evin"`, `claim-excerpt-map.md:36` = the J15 row, `:51` = the J15
span note, `fictional-excerpts.md:31` = the scope paragraph, `README.md:11`/`:13`,
`r94-paired-crossing/README.md:9`, `2026-10-12-lore-decision-table.md:226`, `corpus/fixtures/README.md:1154`/`:1173`,
`r23-note-class/{sella-absence-note-excerpt.md,timeline.json,sources.json,witnessed-absence-clause-map.md:1}`;
r23 timeline ids `['departure','arrival','strip-absence-note']` include the cited `strip-absence-note`.
`cmp` confirms `r95 relations.json` byte-identical to r94 as the note's table states.

## 3. Tools README Round-95 addendum — commands and claims

```
$ python3 corpus/tools/map_obligations.py --self-test
22 × "SELF-TEST PASS <case> exit=<0|1|2> findings=[...]"
RESULT PASS                                                       EXIT=0  stderr_bytes=0
```

The 22 printed cases were compared programmatically against the persisted contract: persisted
cases = 22, observed PASS cases = 22, missing/extra = none, exit+finding mismatches = none,
`map_missing` and `invalid_arguments` both present, terminal line `RESULT PASS`. (r94 baseline was
20 cases — reproduced before P1/P2 landed: 20 lines, same shape.)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS                                                       EXIT=0   (before: EXIT=2 unsupported_map)

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster
FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
RESULT ERROR                                                      EXIT=2

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR                                                      EXIT=2

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
RESULT PASS                                                       EXIT=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS                                                       EXIT=0

$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS                                                       EXIT=0
```

Every addendum sentence of the form "X now exits N with output Y" is reproduced verbatim,
including the r88 `TOTAL-ROWS 12/12` (the C3 "12/12"), the r87/r89 fail-closed pair, and the
frozen replay. The r94 addendum block above it (README:93–96) is retained as history and its
commands still run: r94 14/14 PASS exit 0, r93 12/12 PASS exit 0; its `--self-test` comment
"20/20" is superseded by the Round-95 addendum, which says so explicitly ("now persists 22
expectations"), and its `--frozen` line still holds.

Two further addendum claims were tested on `/tmp` scratch copies (never in-repo corpus):

- "Keeping the map row while renaming the key reports `phantom_obligation` and `schema_drift`
  together, still exit 1" — reproduced:
  `FINDING phantom_obligation: entities.json#/0/claims/0 is not a raw source-attributed obligation`
  + `FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'`,
  `RESULT FAIL`, EXIT=1.
- "a declared count that disagrees with the parsed rows appends ` MISMATCH` … but does not by
  itself change the exit code" — reproduced on a copy with `**Expected inventory:** 15 JSON
  facts` (map otherwise clean): `INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16 MISMATCH`
  / `RESULT PASS`, EXIT=0. So the INVENTORY line is a receipt, not a gate, exactly as documented.

## 4. Exit contract 0/1/2 on the paths the docs claim

| Path (as documented) | Documented | Observed exit | Observed terminal line |
|---|---|---|---|
| r95-crossing-aftermath (P4 README, P5 note, tools addendum scope) | 0 | 0 | `RESULT PASS` |
| r88-m3-maya-cluster (addendum) | 0 | 0 | `RESULT PASS` |
| r93-m2-kojiki-cluster (r94 + r95 addenda) | 0 | 0 | `RESULT PASS` |
| r94-paired-crossing (r94 + r95 addenda) | 0 | 0 | `RESULT PASS` |
| `--frozen` r93 snapshot (both addenda) | 0 | 0 | `RESULT PASS` |
| r87-myth-cluster (addendum fail-closed) | 2 | 2 | `RESULT ERROR` |
| r89-inspiration-paraphrase (addendum fail-closed) | 2 | 2 | `RESULT ERROR` |
| r89-c1-multi-cause-valid, r89-fn2-control (spot check) | — | 2 | `FINDING map_missing` / `RESULT ERROR` |
| BR-02 mutation scratch (addendum §schema-drift) | 1 | 1 | `RESULT FAIL` (stable across two runs) |
| `--self-test` | 0 | 0 | `RESULT PASS` |

CLI-contract probes on the same revision (all zero stderr, one terminal RESULT line):
no args → EXIT=2 `FINDING invalid_arguments: cluster directory is required`;
`--self-test` + cluster → EXIT=2 `invalid_arguments`;
`--frozen` + cluster → EXIT=2 `invalid_arguments`;
`--bogus` → EXIT=2 `unrecognized arguments: --bogus`;
nonexistent cluster → EXIT=2 `FINDING cluster_missing`.

`--help` consistency (the seat's "RESULT-less" note): every documented tool behaves the same —
`map_obligations.py`, `support_check.py`, `boundary_doc_check.py`, `discriminate_check.py`,
`check_bible.py` all give `--help` EXIT=0 with **zero** `RESULT` lines. This is consistent with
README:99 ("note `--help` exits 0 with zero RESULT lines, so exit 0 alone is not a PASS") and
with the addendum's "one terminal RESULT line on operational paths".

## 5. Operability findings, doc-fidelity notes, and residuals

1. **No documented command failed as written.** All P4, P5, and tools-README Round-95 commands
   reproduce their documented exit codes and result text.
2. **Quoted receipts are subsets, not wrong.** P4 README:21 and P5 note:48 quote
   `OBLIGATIONS raw=15 mapped=15 / RESULT PASS`; the delivered tool additionally prints one
   `INVENTORY …` line (addendum documents this line and its ` MISMATCH` behavior). The quoted
   lines remain literally true.
3. **Stale prose outside the producers' write scope:** `corpus/README.md:35` still says
   "`--self-test` (20 persisted cases)" while the delivered contract persists 22. `corpus/README.md`
   is not owned by P2 this round (P2 owns `corpus/tools/README.md` + contract), so the sentence is
   read-only-stale, not an unfulfilled ownership claim. Flagged for the round's admission review.
4. **Mid-flight states were real and are not evidence of the delivered revision:** at 16:22–16:26
   the in-progress tool emitted `FINDING self_test_contract: contract self-test cases do not match
   the implemented cases` / `RESULT ERROR` EXIT=2 for `--self-test` (P2's 22-case contract had not
   landed) and still EXIT=2 `unsupported_map` on r88 (P1 mid-write). Both were re-run after landing
   and pass; no receipt above was taken on a mid-flight revision.
5. **BR-05 witnessed live:** the addendum states the self-test scratch "still lives under the
   repository root and is not gitignored". `corpus/tools/map_obligations.py:720` uses
   `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)` with `ROOT =
   parents[2]` (repo root), i.e. it is created in the repo root and removed on normal exit. During
   a concurrent seat's self-test I observed `?? map-obligations-self-test-h03y07kz/` in
   `git status --porcelain` and the directory was gone seconds later — so a concurrent run is
   visible as an untracked repo-root directory for the duration. No leftover remained after my
   own runs (`ls -d map-obligations-self-test-*` → none). Residual remains open, as documented.
6. **Preservation evidence at this revision:** all 35 baseline digests (r88/r93/r94 fixture files,
   `.ufo/waves/round-94/frozen/map-obligations-r93/expected.json`, `check_bible.py`,
   `support_check.py`) verify `: OK` — zero corpus modification on those paths. support_check
   receipts unchanged: r88 `SOURCE-SUPPORT 10/10 … MODES 12/12; VALIDATED-ROWS 12/12` PASS exit 0,
   r93 `12/12 … 15/15` PASS exit 0, r94 `14/14 … 16/16` PASS exit 0. `git status --porcelain` at
   freeze: ` M LOG.md`, ` M corpus/tools/{README.md,map-obligations-contract.json,map_obligations.py}`,
   `?? .ufo/waves/round-95/`, `?? corpus/fixtures/r95-crossing-aftermath/`,
   `?? corpus/knowledge/r95-aftermath-scope-note.md`.
7. **Census (operability witness of C2's 168→169):** my own loop over `corpus/fixtures/*/` with
   repo-relative `check_bible.py` invocations reproduces the r94 census method exactly and yields
   `dirs=169 clean=35 negative=134 violation_prefix_lines=421 summary_sum=421 stderr_nonempty=0`
   (r94 baseline, same script, before the fixture landed: `dirs=168 clean=34 negative=134 … 421`).
   The delta is the one new clean fixture.

## Bottom line

PASS — every command documented in P4's r95 README, P5's r95 note, and the tools README
Round-95 addendum runs as written on the frozen revision (r95 15/15, r88 12/12, r87/r89 exit-2
fail-closed, r93 12/12, r94 14/14, frozen replay, 22/22 self-test), the documented 0/1/2 exit
contract and `--help` RESULT-less behavior hold on all claimed paths, no documented command
failed, and the only drifts found are disclosed prose residuals outside producer write scope
(`corpus/README.md:35` "20 persisted cases") and the still-open BR-05 repo-root scratch.
