# V20 — doc-parity (round 95)

Seat: V20 doc-parity. Scope per seat spec: pre-integration inventory for L1 —
exactly which index/README additions the round still needs at closure, with the
measured census numbers to cite. Baseline HEAD `fb118c4`; working tree at seat
start: `M LOG.md` + untracked `.ufo/waves/round-95/` only.

This seat wrote only this report and its scratch dir
`.ufo/waves/round-95/scratch/V20/`. No corpus or tool file was modified; no
commits; no network.

## 1. Measured census (the numbers to cite)

Sweep recipe (repo root, repo-relative argv — the spelling the five
argv-echoing fixtures require):

```sh
python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>
```

run over `sorted(p.name for p in Path('corpus/fixtures').iterdir() if p.is_dir())`,
counting exit codes, `VIOLATION:` lines and non-empty stderr.

**Pre-integration** (r95 fixture absent; measured at HEAD `fb118c4` + `M LOG.md`):

```text
direct_fixture_dirs=168
exit0=34 exit1=134 other=0 violations=421 stderr_nonempty=0
```

This reproduces the r94 re-declaration verbatim
(`corpus/fixtures/README.md:1173`), i.e. the baseline is intact.

**Post-P3-tables** (r95 fixture JSON tables landed; P4 README/map still absent —
`check_bible` reads only the five JSON tables, so this measurement is valid for
the census):

```text
direct_fixture_dirs=169
exit0=35 exit1=134 other=0 violations=421 stderr_nonempty=[]
new_dirs=['r95-crossing-aftermath']
changed_inherited=[]
```

So the number the Round-95 README section must cite is **169 fixture
directories: 35 clean (exit 0), 134 intentional negative (exit 1), 421
violation lines, zero stderr**, with `r95-crossing-aftermath` as the single
added directory and **zero changed inherited tuples** vs the pre-integration
sweep. Per-directory tuples are saved at
`.ufo/waves/round-95/scratch/V20/census-pre.json` and `census-post.json`
(169 rows each: dir, exit, sha256(stdout), violation count).

Re-measured once more after **all** producers landed
(2026-10-17T16:28-03:00, `FINAL dirs=169 exit0=35 exit1=134 other=0
violations=421 stderr=[]`) — unchanged, so this is the integration-time figure.

Supporting fixture-state measurements (same tree):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
```

parsed counts `entities=5 relations=1 contradictions=0 timeline=4 sources=4`;
r94 prefix rows parsed-value identical for all five tables; `source-excerpt.md`
and `inspiration-note.md` byte-identical to r94; `fictional-excerpts.md`
differs only by the appended Round-95 aftermath section (`diff` = 20a21,31).
This matches C2's declaration exactly.

### 1b. Delivered-fixture doc-parity receipts (P3+P4 landed)

Measured after P4's `README.md` and `claim-excerpt-map.md` landed (census
re-measured and unchanged at 169/35/134/421):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
# INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
# SOURCE-SUPPORT 15/15; MODES 17/17; VALIDATED-ROWS 17/17 / RESULT PASS   exit 0
python3 .ufo/waves/round-95/scratch/V20/map_obligations.r94.py corpus/fixtures/r95-crossing-aftermath
# OBLIGATIONS raw=15 mapped=15 / RESULT PASS   exit 0
```

(`map_obligations.r94.py` is a scratch copy of `git show fb118c4:corpus/tools/map_obligations.py`,
the r94-delivered tool, used because P1's file was mid-edit at measurement time.)

README↔artifact claim checks — all TRUE:

- "counts 5 entities / 1 relation / 4 events / 4 sources" — parsed;
- "five inherited entity records and the one inherited relation are copied by
  JSON value" — parsed-identical; inherited timeline rows prefix-identical;
- "15 source-attributed JSON pointer obligations (the 14 inherited rows carried
  unchanged plus the new tick-11 event row)" — map has 15 `| J` rows, r94
  pointers/anchors/spans unchanged, only the new path-qualification column
  differs;
- timeline `depends_on` = `[]`, `[]`, `["aru-ninth-bell","evin-ninth-bell"]`,
  `["paired-crossing-decision"]`, matching the README's ordering sentences;
- map declares "15 JSON facts; 2 editorial rows; 17 total mapped rows; 13
  distinct excerpt anchors" = the tool's measured inventory.

**Transient observation, not a defect:** while P1 was mid-write, the live
`corpus/tools/map_obligations.py` crashed on all three cluster maps
(r93/r94/r95) with `ValueError: too many values to unpack (expected 2, got N)`
at `compare()` (the file grew 784→802 lines between two reads). The
r94-delivered tool from git parses the r95 map correctly (receipt above), so
this was an in-flight edit state, not a map-grammar or P4 defect. L1 should
confirm the final P1 file passes r93/r94/r95 after it lands.

Note for the P2 contract wording: the r95 map adds one column
("Path-qualified source namespace") over r94's table; the r94-delivered
grammar already parses it.

### 1c. P5 scope-note citation audit (all cited paths resolve)

Every path/line cited in `corpus/knowledge/r95-aftermath-scope-note.md` was
opened and resolves to the claimed content:

- `claim-excerpt-map.md:36` = the J15 row (`timeline.json#/3`,
  `aru-aftermath-note`, anchor `Tick 11: I waited…`); `:49` and `:51` exist as
  cited (timeline normalization and J15 span 22-31);
- `README.md:9` (occasion comparison), `:11` (crossing-only bound), `:13`
  (editorial tick/ID encodings) — all present;
- `fictional-excerpts.md:19` (`for this crossing only`), `:22` (Round-95
  section heading), `:26-29` (the quoted note lines), `:31` (scope sentence);
- `sources.json:21` = `"id": "aru-aftermath-note"` (`sources.json#/3`);
  `timeline.json:33` = `"id": "aftermath-missing-evin"` (`timeline.json#/3`);
- `corpus/fixtures/README.md:1154-1173` = the Round-94 section it cites;
- `2026-10-12-lore-decision-table.md:226-230` = the Round-23 witnessed-absence
  class it cites; `corpus/fixtures/r23-note-class/` exists with
  `sella-absence-note-excerpt.md` and `witnessed-absence-clause-map.md`.

Map-row inheritance check (regex row diff of the two maps): r94 has J01-J14,
r95 has J01-J15; **all 14 shared rows differ only in the added
path-qualification column** (`r94-paired-crossing:` → `r95-crossing-aftermath:`)
— pointers, source IDs, excerpt paths, spans, modes and anchors are identical;
J15 is the sole new row. This is exactly what P4's README and P5's note claim.

## 2. Closure additions still needed (exact sites)

### A. `corpus/fixtures/README.md` — append a Round-95 section (REQUIRED)

State at seat time: 1175 lines; Round-94 section occupies `:1154-1175` (EOF);
`grep -n "r95\|Round 95" corpus/fixtures/README.md` → no match. The r94 closure
landed the Round-94 section (`ac69044`), so the precedent for r95 is an
append-only section after line 1175.

Content requirements for `## Round 95 — \`r95-crossing-aftermath\` (2026-10-17)`:

- preserving copy of `r94-paired-crossing` + one aftermath note
  (`aru-aftermath-note`) + one tick-11 event (`aftermath-missing-evin`, actor
  `aru`, place `chalk-stair`, `depends_on: ["paired-crossing-decision"]`);
- counts 5 entities / 1 relation / 4 events, 4 sources (was 3);
- 15 map obligations = 14 inherited rows unchanged + 1 new event row; no new
  claims, entities, or relations; crossing-only scope, no breach/other-duty
  assertion;
- replay receipts measured on the delivered revision: `check_bible` CLEAN
  exit 0; `support_check.py` receipt; `map_obligations.py` 15/15 PASS;
- **census re-declaration: 169 / 35 / 134 / 421 / zero stderr** (supersedes the
  Round-94 `168/34/134/421` at `:1173`);
- dated pin note: this append changes the file's bytes again — the r94 W05
  preservation pin for this file (`a13d1af3…`) was already invalidated by the
  Round-94 append and stays invalid; the r95 append must be declared the same
  way (same pattern as `:1175`).

### B. `corpus/README.md` — navigation bullets (REQUIRED; 37 lines total)

State at seat time: no r95 mention anywhere. Four edits:

1. after `:21` (`fixtures/r94-paired-crossing/README.md` bullet, cluster list):
   add the `fixtures/r95-crossing-aftermath/README.md` bullet — the r95 fixture
   is the r94 continuation, so it belongs in the same
   "Myth-comparison fixture clusters" list;
2. after `:30` (`knowledge/r94-cross-myth-design-comparison.md` bullet): add a
   `knowledge/r95-aftermath-scope-note.md` bullet (P5's file);
3. `:29` (`knowledge/r91-c9-watch.md` bullet) says "including the **r93**
   re-check entry" — stale by two rows (r94 landed in `ac69044`); update to the
   r95 re-check;
4. `:35` (`tools/map_obligations.py` bullet) says "(round 94)" and
   "`--self-test` (**20** persisted cases)" — both go stale at r95; it also
   needs the new surface: `schema_drift` (exit 1) and the r88 map dialect
   (12/12 PASS, r87/r89 still exit 2 fail-closed).

Optional (not required by any claim): `:34` (`fixtures/README.md` bullet)
currently names "the C9 pair and r93 authored cluster" and could mention the
r94/r95 clusters; `:36` (`tools/README.md` bullet) is generic and stays true.

### C. `corpus/knowledge/r91-c9-watch.md` — r95 re-check row (REQUIRED, UNOWNED)

State at seat time: 257 lines; last check-log row is r94 and it reads
"Next re-check: **r95**" — so the fourth periodic re-check is **due this
round**. No r95 producer byte-owns this file (P1-P5 ownership covers
`map_obligations.py`, `map-obligations-contract.json` + `tools/README.md`, the
fixture files, the fixture README/map, and the new scope note). L1 must assign
or perform this append at closure, following the r94 pattern (`ac69044`).

Receipts this seat already captured read-only at the r95 tree (replayable,
unaffected by P1's `map_obligations.py` change because the watch pins
`check_bible.py`, which no r95 seat owns):

```sh
sha256sum corpus/fixtures/check_bible.py
# ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
python3 corpus/tools/discriminate_check.py
# mode=delivered checker_sha256=ff9fd2aa…d1421 matches_pin=True
# r91-c1-null-chain: run_exit=1 stderr_empty=True … pinned_semantic_gate=PASS
# r91-c1-tick-unresolved: run_exit=1 stderr_empty=True … pinned_semantic_gate=PASS
# RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression   (exit 0)
python3 corpus/tools/discriminate_check.py --checker e97613c
# REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present   (exit 2, expected control)
```

The r95 row should therefore read **DISCRIMINATION HELD**, re-check 4, with the
`e97613c` control at exit 2 REGRESSION-DETECTED, "Next re-check: r96". The
four-gate falsification trigger state is unchanged (gate 3 not met), same as
r93/r94 — but that wording must be re-verified by whoever writes the row, not
copied blind.

### D. `corpus/tools/README.md` + contract — P2's addendum (byte-owned by P2)

**Landed and verified by 2026-10-17T16:28-03:00** (P2's report file was still
absent from `seats/` at that time — the artifacts, not the report, are what
this seat checked). The Round-95 addendum
("`schema_drift`, 22-case self-test, r88 map dialect") documents exactly the
three surfaces, keeps the r94 text as delivered history, and the contract now
persists the two new cases:

```sh
python3 -c "import json;d=json.load(open('corpus/tools/map-obligations-contract.json'));c=d['self_test']['cases'];print(len(c),[x['id'] for x in c][-2:])"
# 22 ['map_missing', 'invalid_arguments']
# map_missing: {'id': 'map_missing', 'exit': 2, 'finding_ids': ['map_missing']}
# invalid_arguments: {'id': 'invalid_arguments', 'exit': 2, 'finding_ids': ['invalid_arguments']}
```

Final tool receipts at the delivered revision
(`map_obligations.py` sha256
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`;
contract sha256
`8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db`):

```text
--self-test: RESULT PASS, exit 0 (22 SELF-TEST PASS lines)
r88-m3-maya-cluster: exit 0 (10/10 JSON-FACTS; 2/2 EDITORIAL; 12/12 TOTAL)   ← C3 met
r87-myth-cluster: exit 2    r89-inspiration-paraphrase: exit 2               ← fail-closed retained
r93: exit 0 (12/12)   r94: exit 0 (14/14)   r95: exit 0 (15/15)
--frozen .ufo/waves/round-94/frozen/map-obligations-r93: exit 0, digests=verified
```

One documentation consequence worth carrying into §A: the addendum states the
r93/r94 receipts now print an additional
`INVENTORY JSON-FACTS a/b; EDITORIAL-ROWS c/d; TOTAL-ROWS e/f` line, so the
Round-95 section of `corpus/fixtures/README.md` should quote the **new** receipt
shape rather than copy the r94 block. The inventory line is declared a receipt,
not a gate (a declared-count mismatch appends ` MISMATCH` without changing the
exit code).

### E. `SKILL.md` — gate-registry row (UNOWNED, EXTRA FINDING)

The root `SKILL.md` "Raw-obligation mapping completeness" row (`:83-89`) carries
the same facts as the tools README and goes stale the same way:

- `:86` exit-class list "`1 → failed` (failed obligation comparison:
  `missing_obligation` / `duplicate_mapping` / `phantom_obligation` /
  `source_id_mismatch`)" — missing `schema_drift`;
- `:87` "**20 cases** with independently persisted expected exits and finding
  IDs" — becomes 22;
- `:89` scope "for the canonical map form used by the **r93 and r94** clusters"
  — the r88 dialect is now supported (C3); and "Bounded residuals BR-01…BR-04
  and BR-16 of the round-94 debt ledger apply" — BR-02/BR-03 are the r95 head
  items and close if C1 verifies.

No r95 producer byte-owns `SKILL.md`. r94 closure landed the equivalent
gate-registry row as condition C-1 (`ac69044`); r95 needs the same treatment or
an explicit deferral.

## 3. Final stale-site confirmation (post-integration, 16:28-03:00)

```sh
grep -c "r95\|Round-95" corpus/README.md                    # 0
grep -c "Round 95\|r95-crossing" corpus/fixtures/README.md  # 0
grep -n "r95" corpus/knowledge/r91-c9-watch.md              # only :253 = the r94 row's "Next re-check: r95"
grep -c "20 cases" SKILL.md                                 # 1
git status --porcelain                                      # READMEs + SKILL.md + c9 watch unmodified
```

So at integration time the round has **not** yet touched: `corpus/README.md`,
`corpus/fixtures/README.md`, `corpus/knowledge/r91-c9-watch.md`, `SKILL.md`.
`corpus/tools/README.md` and the contract are done (P2); the fixture and the
knowledge note are done (P3/P4/P5); the tool is done (P1).

## 4. What this seat did NOT verify

- No verdict on any axis; this is an inventory, not an adjudication. The
  receipts quoted are doc-parity evidence, not an admission decision.
- `corpus/fixtures/README.md` Round-95 text, `corpus/README.md` bullets, the
  C9 row and the SKILL.md row do not exist yet, so nothing about their eventual
  wording is verified here — only the sites and the measured numbers they must
  cite.
- The `--frozen` snapshot lives under the r94 wave dir; this seat did not check
  whether r95 needs its own frozen dir (not a doc-parity item).

## Bottom line

PASS — closure inventory complete and measured: census **169 directories / 35
clean / 134 negative / 421 violation lines / zero stderr** (one added directory,
zero inherited changes; `r95-crossing-aftermath` CLEAN). Still to write at
closure: `corpus/fixtures/README.md` Round-95 append (after `:1175`, quoting the
new INVENTORY-line receipt shape), `corpus/README.md` bullets
`:21/:29/:30/:35`, `corpus/knowledge/r91-c9-watch.md` r95 re-check append at EOF
(receipts captured in §C: DISCRIMINATION HELD exit 0; `e97613c` control
REGRESSION-DETECTED exit 2), plus the unowned `SKILL.md:86-89` gate-registry
update; `corpus/tools/README.md` is done by P2 and verified.
