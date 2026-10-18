# V52 claim-text-audit — round 98

- Seat: V52 claim-text-audit (verifier). Task: read the r98 LOG declaration against delivered reality; corrections list.
- Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648` (pre-round bytes via `git show 9a3d648:<path>`); HEAD during the round `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`. All commands from the lane root with `python3`.
- Writes: this report (absolute path) and `.ufo/waves/round-98/seats/V52-scratch/` only (`poll.sh`/`poll.log`, `census.py` + `census_receipts.json`, `probes.py`, `probeD.py`, `mirror/`). No commits, no pushes, no network, no nested agents.

## Revision pinned for every measurement

All results below were taken on the delivered wave tree at these sha256 values; a re-hash at 20:36–20:37 confirmed they were unchanged since each measurement run (the wave tree was still and no producer wrote after ~20:33:43).

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  corpus/tools/README.md
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827  corpus/knowledge/r95-aftermath-scope-note.md
a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048  corpus/knowledge/r96-response-scope-note.md
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  corpus/fixtures/r98-clerk-filing/README.md
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r98-clerk-filing/entities.json
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  corpus/fixtures/r98-clerk-filing/sources.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
```

## 0. Poll-wait record

`V52-scratch/poll.sh` (20 s cadence, 40 tries, checks artifacts AND producer reports). Final log line:

```
try=17 ts=20:35:23 fixfiles=10 note=1 nreports=5 reports=[S1-freeze-hygiene.md,S2-tools-docs.md,S3-fixture-author.md,S4-fixture-docs.md,S5-knowledge-notes.md,]
COMPLETE try=17
```

No ABSENT condition arose; no stall escape was needed; the endgame convention (subtract SELF) was never exercised because the loop's own all-five condition completed at try 17. First-pass audits were re-run after the last producer write (`corpus/tools/README.md` 20:33:43).

## 1. C1(a) — `SELF-TEST-MISMATCH` exits 2, pinned as case 16→17

Premise check (baseline). `git show 9a3d648:corpus/tools/dependency_freeze.py` line 544:

```
        emit(1, [("SELF-TEST-MISMATCH", f"cases failed: {sorted(failures)}")])
        return 1
```

and the map_obligations comparison target, `corpus/tools/map_obligations.py:877-879`:

```
        print("FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations")
        print("RESULT ERROR")
        return 2
```

So the declaration's "today it exits 1 in dependency_freeze vs 2 in map_obligations" was true at baseline.

Delivered. `git diff 9a3d648 -- corpus/tools/dependency_freeze.py` shows `emit(1, …)/return 1` → `emit(2, …)/return 2`, `FROZEN_CASES` grew 16 → 17 by append (`self_test_mismatch`), and the contract persists `self_test.expected.self_test_mismatch = {"exit": 2, "finding_ids": ["SELF-TEST-MISMATCH"], "forbid_traceback": true}`. Runs:

```
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -3
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 17/17
RESULT PASS                      # exit 0
```

Independent neutralization (not relying on the persisted case): a mirror tree with the contract copy's `self_test.expected.digest_tamper.exit` flipped 2 → 0 prints `SELF-TEST 16/17`, `FINDING SELF-TEST-MISMATCH: cases failed: ['digest_tamper']`, `RESULT ERROR`, **exit 2** — the mismatch class exits 2 for a case other than the pinned one too.

Inherited cases unchanged: programmatic compare of the 16 baseline expectations vs delivered — zero changed, one added. ✓ claim (a) holds.

## 2. C1(b) — path-less legacy pin migrated in place by `--freeze`

Baseline refusal branch (9a3d648 `freeze()`): `if isinstance(existing, dict) and existing.get("fixture") != fixture_label: fail("SCOPE-REFUSED", "… pin {name} already names None; …")` — i.e. `SCOPE-REFUSED … already names None`, matching the declaration's "today" quote.

Delivered probe (mirror root: delivered tool + contract + r97 fixture; the mirror contract's r97 pin `fixture` key deleted):

```
MIGRATED r97-crossing-acknowledgment: path-less legacy pin now names corpus/fixtures/r97-crossing-acknowledgment
FROZEN r97-crossing-acknowledgment: events 6; dependency-edges 5; relations 1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
RESULT PASS                      # exit 0
pin fixture after: corpus/fixtures/r97-crossing-acknowledgment
```

Retained refusal: same-named in-scope target at a different path still exits 2 `SCOPE-REFUSED … already names 'corpus/fixtures/r97-crossing-acknowledgment'; freezing a same-named path elsewhere would rewrite the delivered pin` (probe B2). ✓ claim (b) holds.

## 3. C1(c) — contract `precedence` names the full exit-2 order and FINDING IDs

Delivered `corpus/tools/dependency-freeze-contract.json` `precedence` (verbatim): "semantic inventory findings decide first (exit 1: REDUCTION-DETECTED, ADDITION-DETECTED, ENDPOINT-CHANGE); a content digest change the frozen inventory does not model exits 2 (DIGEST-MISMATCH). Exit-2 (could-not-evaluate) checks run in this order and the first failing check decides: UNPINNED-FIXTURE (no pin for the fixture name) or CONTRACT-INVALID (unreadable contract or invalid pin), FIXTURE-MISSING (fixture directory absent), PATH-MISMATCH (invoked path differs from the pin's recorded path), FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL (model build), DIGEST-MISMATCH (inventory clean, bytes changed outside the frozen inventory), INVALID-ARGUMENTS (CLI usage), SELF-TEST-MISMATCH (--self-test observed outcome differs from the persisted case expectation); --freeze additionally raises SCOPE-REFUSED (target outside corpus/fixtures/**, or a same-named in-scope target that would rewrite an existing pin's recorded path). A path-less legacy pin is migrated in place by --freeze instead of refused."

Completeness: every exit-2 finding ID raised in the delivered tool (enumerated from all `fail(...)`/`emit(2, ...)` sites: INVALID-ARGUMENTS, FILE-MISSING, MALFORMED-JSON, FIXTURE-MISSING, MALFORMED-MODEL, CONTRACT-INVALID, SCOPE-REFUSED, PATH-MISMATCH, UNPINNED-FIXTURE, DIGEST-MISMATCH, SELF-TEST-MISMATCH) is named in the text. Order: the delivered `verify()` flow is `pin_for` (UNPINNED-FIXTURE/CONTRACT-INVALID) → `FIXTURE-MISSING` → `bind_path` (PATH-MISMATCH) → `build_model` (FILE-MISSING/MALFORMED-JSON/MALFORMED-MODEL) → `compare` (semantic findings, exit 1 first) → `DIGEST-MISMATCH` — identical to the declared order, with semantic-first over digest verified in code. ✓ claim (c) holds.

## 4. C2 — chain extended; pins via guarded `--freeze`; V46 discharged

Pins: delivered contract has six pins, adding `r97-crossing-acknowledgment` and `r98-clerk-filing` (revision `dd4df1b…` = HEAD), while the four inherited pins are byte-identical to the baseline contract (programmatic compare: all `True`).

Guarded `--freeze` / reproducibility: a mirror root holding the delivered tool + contract + both fixtures, frozen again with `--freeze`, produced pin entries **byte-equal to the delivered pins** for both:

```
r97-crossing-acknowledgment mirror-freeze pin == delivered pin: True
r98-clerk-filing           mirror-freeze pin == delivered pin: True
```

Chain 6/6 (delivered revision):

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f | tail -1; echo "$f exit=$?"; done
RESULT PASS / exit=0   (x6)
```

New receipts: `FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1` digest `3c922d20…`; `FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1` digest `59a0f4fa…` — both match S1's report and S2's README quotes.

V46 discharge reproduced independently: mirror copy of pinned r97 with the tick-13 edge dropped (`acknowledgment-aru-records` loses `response-evin-salt-court`):

```
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL                      # exit 1
```

Pre-state (V46, r97): `UNPINNED-FIXTURE`, exit 2 — the edge was unreachable; now it is caught as BR-01. S1's mutation bytes match V46's recorded sha (`37a425b9…`), and the r97 pin digest equals the digest V46 froze in its r97 scratch mirror (`3c922d20…`). ✓ C2 holds.

## 5. C3 — fourth beat fixture, counts, obligations, census, r95 repair

Counts and inheritance (delivered): entities 6 / relations 1 / timeline 7 / sources 7; `contradictions.json` `[]`. Parsed-prefix identity vs r97: `entities.json[:5] == r97`, `sources.json[:6] == r97`, `timeline.json[:6] == r97` all `True` (diffs are pure appends). New rows: entity `clerk-maren` (`kind: character`, `first_appearance: clerk-filing-note`, one claim citing `clerk-filing-note`), source `clerk-filing-note`, event `clerk-filing-open` (tick 14, actor `clerk-maren`, place `chalk-stair`, `depends_on: ["acknowledgment-aru-records"]`, description "…the clerk filed both pending accounts and recorded the matter OPEN, asserting no finding and no resolution."). The excerpt's own lines: "I assert no finding." / "I reach no verdict and reconcile nothing." (fictional-excerpts.md:61-62); sources.json reliability note names "no resolution". The declaration's "explicitly asserting no finding and no resolution" is supported. ✓

Byte-copy reality vs "a preserving copy": 4 files byte-identical to r97 (`contradictions.json`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`), 4 extended by S3 (entities/sources/timeline/fictional-excerpts), 2 rewritten by S4 (README, map). Matches "preserving copy plus additions".

Gates:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations                      # exit 0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20 / INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                                                      # exit 0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
SOURCE-SUPPORT 20/20; … VALIDATED-ROWS 22/22 / RESULT PASS                       # exit 0
```

Map rows: 17 inherited rows J01–J17 parsed-value identical to r97's rows (0 diffs outside the declared namespace column, which re-qualifies `r97-crossing-acknowledgment:` → `r98-clerk-filing:`), plus exactly J18 first_appearance / J19 claim / J20 event. ✓ "17 inherited rows unchanged + first_appearance + claim + event rows".

Census (V21-method replication over every `corpus/fixtures/*/`):

```
{"fixture_dirs": 172, "clean_exit0": 38, "negative_exit1": 134, "violation_lines": 421, "non_0_1_exits": []}
```

171 → 172 with +1 clean, zero inherited tuple changes, zero non-0/1 exits. ✓

r95 repair: delivered r95 map differs from `9a3d648` by exactly one prose line (the stale sentence; before: "The new relation encodes only…", after: "The relation encodes only…; the new tick-11 aftermath event records one reported non-arrival on one occasion."). Table lines byte-identical (22/22). Receipts pre/post (mirror with baseline map vs delivered map): `check_bible`, `support_check`, `map_obligations` outputs all byte-identical, all exit 0 (`raw=15 mapped=15` etc.). ✓ "data rows byte-unchanged, r95 receipts unchanged".

## 6. Corrections list (the deliverable)

- **C-1 (minor, delivered doc — text error).** `corpus/tools/README.md:284` says "`git diff 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and `dependency-freeze-contract.json`". Observed:
  ```
  $ git diff --name-only 9a3d648 -- corpus/tools/
  corpus/tools/README.md
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/dependency_freeze.py
  ```
  The README itself is also listed (it is the file carrying the addendum). Suggested fix: name all three, or qualify ("among the tool scripts"). The same wording recurs in S1's report §6 ("git diff 9a3d648 -- corpus/tools/ lists only …"), though S1's preceding sentence does list `corpus/tools/README.md` as a modified seat path; the README sentence is the one in the delivered tree.
- **C-2 (minor, delivered doc — superseded hash).** `corpus/knowledge/r98-clerk-scope-note.md` (Receipts) records S1's revisions as "`dependency_freeze.py` `03d04365…`, contract `c435239d…` at 20:32:51-03:00". The tool hash matches the delivered revision; the contract hash does not: the delivered contract is `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947` (S1's later `--freeze` of r97/r98 rewrote it; S2's report shows the chain `b06275f3… → 3a940a9f… → c435239d… → 153ebc5b…`). Suggested fix: cite `153ebc5b…` or annotate `c435239d…` as the pre-pin intermediate. The note's own "re-measure before citing" instruction partially covers this, but the citation as written names a non-delivered contract revision.
- **C-3 (freshness/closure item).** `corpus/fixtures/README.md` still declares the r97 census (171/37/134/421) while the measured r98 state is 172/38/134/421. The r98 declaration claims the census measurement but assigns no producer to the fixtures README (its r97 precedent was a closure doc pass). Closure should re-declare; not a contradiction of the declaration text.
- **C-4 (hygiene, outside the lane — recorded, not owned).** Stray write at the parent root `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (105 B, mtime 20:30:10, content `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py'`) — the r94-F01 stray-write class, unattributed (S3's report item D5 and S1's report also record it). Also a root-level gitignored scratch `v05-self-test-scratch/` (mtime 20:36:16, contents `c1probe*`) created by seat V05 outside the seats-scratch convention; zero delivered-tree impact (`*-self-test-*/` ignores it).
- **Note N-1 (no correction).** The declaration's "harbor clerk of the Chalk Stair registry" appears in the fixture's own prose (`README.md:7`, `fictional-excerpts.md:64` scope line: "the harbor clerk's first-person filing record") while the JSON claim/statement says "the clerk of the Chalk Stair registry". No substantive divergence; if exact JSON-level wording is wanted, "clerk of the Chalk Stair registry (prose: harbor clerk)" is the precise form.

## 7. Other observations

- Byte-ownership compliance: `git status --porcelain` lists exactly the declared paths (S1's two files, S2's README, S3's r95 map + r98 fixture dir, S5's three notes, LOG.md, `.ufo/waves/round-98/`). No commits (`git log -1` still `dd4df1b`).
- Verifier wave activity observed consistent with the declared 59-seat verifier side: `V05` root scratch (`c1probe*`), `V14-poll.sh`, and V06/V11/V17/V20 scratch dirs; no verdicts from them are claimed here.
- `--self-test` scratch hygiene: no `dependency-freeze-self-test-*` leftovers at the repo root after my runs; `v05-self-test-scratch` is the only root scratch seen.

## Bottom line

**PASS** — every C1/C2/C3 statement in the r98 LOG declaration verified true on the hash-pinned delivered revision (self-test 17/17 and mismatch exits 2; legacy pin migrates while the different-path refusal stays; precedence names all exit-2 IDs in code order; six-pin chain 6/6 with both new pins byte-reproducible by guarded `--freeze`; r97-edge REDUCTION-DETECTED reproduces V46's exact mutation; r98 fixture 6/1/7 + 7 sources, 20/20 obligations, CLEAN, census 172, r95 repair receipts identical), with a three-item corrections list (two minor delivered-doc text errors: README:284 git-diff sentence, S5 note's `c435239d…` contract citation; one closure freshness item: fixtures README census still 171) and two recorded hygiene strays outside the lane.
