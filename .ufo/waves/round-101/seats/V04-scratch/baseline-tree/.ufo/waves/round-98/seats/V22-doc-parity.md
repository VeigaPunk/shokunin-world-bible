# V22 — doc-parity (round 98)

Seat: **V22 doc-parity** — verifier. Scope: pre-integration documentation parity
inventory for the four closure-pass documents that no round-98 producer owns —
`corpus/fixtures/README.md`, `corpus/README.md`, `SKILL.md`,
`corpus/knowledge/r91-c9-watch.md` — plus the stale-wording list. Baseline: r97
closure `9a3d648`. Everything below is read-only outside this report and
`.ufo/waves/round-98/seats/V22-scratch/`.

## 1. Verified pre-integration state (no unowned doc drift)

All four inventory targets were byte-identical to baseline `9a3d648` when first
measured (20:28) and again after the fixture producers landed (20:36):

```sh
sha256sum SKILL.md corpus/README.md corpus/fixtures/README.md corpus/knowledge/r91-c9-watch.md
# 2b5bf27fd1bc49da1e5cad979b3ca93d410d03c8c52bd49d8bc8b29a1c428b00  SKILL.md
# 94f13ac02626843019326a25378fc87151e72d12710798a00ff9571185edfe14  corpus/README.md
# 00e0074862b48eaa3ffcf50157ba5c70f030c1e775e299ebe23e29cf26b508b6  corpus/fixtures/README.md
# 10245618b5eb8fb9258c20139a03897b5582582e7176a46113c549e80228c135  corpus/knowledge/r91-c9-watch.md
for f in SKILL.md corpus/README.md corpus/fixtures/README.md corpus/knowledge/r91-c9-watch.md; do
  echo -n "$f "; git show 9a3d648:$f | sha256sum; done
# identical hashes for all four (no drift; the byte-ownership rule held)
```

Round-tree state outside the declared ownership at first inventory: only
`LOG.md` (r98 declaration) and `SCORECARD.md` (r97 closure section) differed
from `9a3d648`; `git status --porcelain -uall | grep -v '^?? .ufo'` showed
exactly the r95 map repair + the ten new `r98-clerk-filing/` files. Zero
unowned doc edits.

## 2. Item inventory (pre-integration → expected post-round)

### 2a. `corpus/fixtures/README.md` — Round-98 section ABSENT; census 172 expected

- File ends at the Round-97 section (`:1221`) + census re-declaration (`:1238`)
  + pin note (`:1242`). No `## Round 98` heading; `grep -n 'Round 98\|r98\|clerk'`
  over the file returns nothing.
- `:1240` declares the r97 census: **171 dirs / 37 clean / 134 negative / 421
  violation lines / zero non-0/1 exits**. The Round-98 re-declaration must
  supersede it with **172 / 38 / 134 / 421 / zero non-0/1**.
- Independent measurement at the delivered fixture state (my own census,
  `.ufo/waves/round-98/seats/V22-scratch/census_v22.py`, repo-relative argv,
  `check_bible.py` per direct fixture dir, run 20:29:42):

  ```sh
  python3 .ufo/waves/round-98/seats/V22-scratch/census_v22.py
  # {"clean": 38, "dirs": 172, "negative": 134, "non01": [], "violation_lines": 421}
  ```

  `r98-clerk-filing` is present and exits 0 (clean 37→38, negative unchanged
  at 134, violation lines unchanged at 421, zero non-0/1 exits). The expected
  census increment is therefore **verified, not merely planned**.
- `:1236` (Round-97 section) carries two statements the Round-98 section must
  supersede in its own text (historical bytes stay): "the frozen chain is the
  declared four fixtures — `r97-crossing-acknowledgment` is not yet pinned
  (r98 candidate)" and "16 cases" for `dependency_freeze`. Post-round values:
  chain six (r88-m3, r94, r95, r96, r97, r98) and 17 cases — both delivered by
  S1 and independently verified in §2c/§3.
- `:1213` (Round-96 section) records the r96 map cosmetic debt as an "r97
  candidate"; the r95 map's carried sentence is not recorded anywhere in this
  file as carried debt. The Round-98 section should record the r95 repair
  (S3): exactly one sentence at `claim-excerpt-map.md:49`, data rows
  byte-unchanged, r95 receipts unchanged (independently re-run below).

### 2b. `corpus/README.md` — bullets stale (r98 fixture; chain six; 17 cases)

- **Missing fixture bullets (carried gap + new):** the "Myth-comparison
  fixture clusters" list ends at `fixtures/r96-crossing-response/README.md`
  (`:29`). There is **no r97 bullet and no r98 bullet** — `grep -n 'r97\|r98'
  corpus/README.md` returns nothing at all. The r97 closure doc pass updated
  only the tools bullets, not the fixture navigation; r98 adds a second gap.
  Expected post-round: an `r97-crossing-acknowledgment` bullet and an
  `r98-clerk-filing` bullet (6 entities / 1 relation / 7 events / 7 sources,
  20 obligations, clerk-maren / clerk-filing-note / tick-14 clerk-filing-open,
  no finding / no resolution).
- **`:38` `tools/dependency_freeze.py` bullet — three stale clauses:**
  (i) "frozen dependency-edge regression check for the continuation chain
  (r88-m3 → r94 → r95 → r96)" → **chain six** (`… → r96 → r97 → r98`);
  (ii) "16-case persisted self-test" → **17-case** (delivered, verified);
  (iii) "the r97 fixture is not yet pinned" → **stale after C2** (both r97 and
  r98 pinned). The bullet label "(rounds 96–97)" should become "(rounds
  96–98)".
- **`:37` `tools/map_obligations.py` bullet:** "(rounds 94–97)", "25 persisted
  cases" — unchanged by the r98 claims (C1 owns only `dependency_freeze`);
  leave unless S1's delivery touches it (it must not).
- **`:31` C9 bullet:** "`knowledge/r91-c9-watch.md` — … including the r93
  re-check entry" — stale by four rounds; the log holds rows through r97 and
  an r98 row is due. Expected: "including the r93–r98 re-check entries" (or
  equivalent) after the closure row lands.

### 2c. `SKILL.md` — freeze row update (`:94`–`:100`)

Current row text and the exact stale tokens:

- `:96` "frozen chain: r88-m3-maya-cluster, r94-paired-crossing,
  r95-crossing-aftermath, r96-crossing-response" → **six fixtures** (add
  r97-crossing-acknowledgment, r98-clerk-filing).
- `:98` "16 cases (r97 added `SCOPE-REFUSED`, `PATH-MISMATCH`)" → **17 cases**
  with the r98-added case names (S1's contract is authoritative; C1 declares
  the `SELF-TEST-MISMATCH` exit-2 pin and the path-less legacy migration).
- `:99` "exactly the four chain fixtures" → **six**; the r97 `revision`-refresh
  sentence remains historical but the row should note the r98 re-freeze if S1
  performs one.
- `:100` bounds: "the frozen chain is the declared four fixtures
  (r97-crossing-acknowledgment unpinned as of r97 closure — r98 candidate)"
  → **stale** (pinned this round); "a path-less legacy pin cannot be refreshed
  in place (manual contract edit)" → **stale after C1(b)** (`--freeze`
  migrates it). "BR-01's markdown/prose half remains open" stays.
- `:87` (`map_obligations` self-test "25 cases") — no change expected.

**Delivered contract state (S1, verified 20:31–20:33):** `self_test.expected`
now holds 17 named cases (`clean` … `path_mismatch`, `self_test_mismatch`) and
`python3 corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 17/17` /
`RESULT PASS` exit 0, with the new case reporting
`exit=2 expected=2 findings=['SELF-TEST-MISMATCH']`. The `precedence` text now
names the full exit-2 order (`UNPINNED-FIXTURE`/`CONTRACT-INVALID`,
`FIXTURE-MISSING`, `PATH-MISMATCH`, `FILE-MISSING`/`MALFORMED-JSON`/
`MALFORMED-MODEL`, `DIGEST-MISMATCH`, `INVALID-ARGUMENTS`,
`SELF-TEST-MISMATCH`) plus `SCOPE-REFUSED` for `--freeze`, and states "A
path-less legacy pin is migrated in place by `--freeze` instead of refused."
**The `pins` object held six fixtures by 20:32:49** — the C2 chain extension
landed after my first read (my 20:31–20:32 read showed the four-pin mid-write
state; final
delivery: `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`,
`r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`, each
with a repo-relative `fixture` path; r97/r98 pinned at revision `dd4df1b36a64`,
r96's revision-only refresh `2393934237ea` preserved). Delivered hashes (final,
re-measured 20:36): `dependency_freeze.py` `03d04365…`,
`dependency-freeze-contract.json` `153ebc5b…` — an earlier read at 20:32:45
showed `c435239d…`; the contract was rewritten by S1's `--freeze` runs at
~20:33, and S1's report and my final read agree on `153ebc5b…` (S5's r98
scope-note cites the earlier `c435239d…`, stale as of the final delivery).
Chain verification at this delivery: all six fixtures `RESULT PASS` exit 0
(events 2/2, 3/3, 4/4, 5/5,
6/6, 7/7); self-test 17/17 PASS; a scratch copy of the r97 fixture with the
tick-13 `depends_on` dropped reports
`FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on
['response-evin-salt-court']` / `RESULT FAIL` exit 1 — the r97 pin is
load-bearing and V46's recorded FAIL is discharged as declared.

### 2d. `corpus/knowledge/r91-c9-watch.md` — r98 row ABSENT (due)

- Last check-log row is `:303` (r97, re-check 6) ending "Next re-check: r98".
  No r98 section exists; the file ends there. The r98 row is a closure-pass
  item (no round-98 producer owns the watch).
- Pre-verified content for that row — I reproduced the pair independently at
  the delivered checker revision (20:31, re-confirmed 20:36):

  ```sh
  sha256sum corpus/fixtures/check_bible.py
  # ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
  python3 corpus/tools/discriminate_check.py
  # RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression   (exit 0)
  python3 corpus/tools/discriminate_check.py --checker e97613c
  # REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present   (exit 2, expected control)
  ```

  So the r98 row's expected content (checker pin fresh `ff9fd2aa…d1421`;
  DISCRIMINATION HELD; control REGRESSION-DETECTED; ruling retained; next
  re-check r99) is verified in advance; only the append itself is pending.

## 3. Independent receipt runs (delivered state, 20:31–20:36)

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
# OBLIGATIONS raw=20 mapped=20; INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22 / RESULT PASS   exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
# SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22 / RESULT PASS   exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
# raw=15 mapped=15; TOTAL-ROWS 17/17 / RESULT PASS   exit 0   (unchanged by the repair)
python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
# SOURCE-SUPPORT 15/15; MODES 17/17 / RESULT PASS   exit 0   (unchanged by the repair)
```

Fixture shape read from the delivered tables: 6 entities / 1 relation / 7
events / 7 sources / 0 contradictions; `clerk-maren` (first_appearance
`clerk-filing-note`, one claim), source `clerk-filing-note`, event
`clerk-filing-open` tick 14 at `chalk-stair` with
`depends_on: ["acknowledgment-aru-records"]` — exactly the C3 declaration.
S4's fixture README states the same counts and the 20-obligation map, and the
map's 22 data rows cite the `r98-clerk-filing:` namespace (2 remaining
`r97-crossing-acknowledgment:` mentions are prose, not row citations).
Inherited-row parity: r98's first 5 entities / 1 relation / 6 events /
6 sources are parsed-value identical to r97's (python3 list-slice comparison;
no inherited row changed).

C1 probes (the doc rows in §2c depend on these; verified independently):

- (a) `--self-test` → `SELF-TEST 17/17` / `RESULT PASS` exit 0; the new
  `self_test_mismatch` case reports `exit=2 expected=2
  findings=['SELF-TEST-MISMATCH']`.
- (b) Scratch-cluster probe (`.ufo/waves/round-98/seats/V22-scratch/c1b/`,
  contract copy with the r95 pin's `fixture` key stripped): `--freeze` printed
  `MIGRATED r95-crossing-aftermath: path-less legacy pin now names
  corpus/fixtures/r95-crossing-aftermath` and exited 0; the pin then carried
  the repo-relative path and a verify run printed `RESULT PASS` exit 0.
- (c) Contract `precedence` text quoted in §2c (full exit-2 order + finding
  IDs + the migration sentence).

S2 tools-README addendum (delivered 20:33:50, sha256 `1d299c16…`): its claims
re-verify against the delivered tool — 17-case self-test, six-fixture chain
6/6 PASS, r97 digest `3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6`
and r98 digest `59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133`
reproduced exactly, the `MIGRATED …` sentence matching my scratch probe, the
precedence list matching the contract text, and `map_obligations.py
--self-test` still `SELF-TEST CASES 25/25 pinned` / `RESULT PASS` exit 0. Two
residual wording defects in that file are recorded as stale item 12 below.

Note (mid-flight observation, recorded not fatal): at 20:31 the map was still
the r97 byte-copy and `map_obligations` reported `raw=20 mapped=17` with three
`missing_obligation` findings (entities `#/5/first_appearance`, `#/5/claims/0`,
`timeline.json#/6`) and RESULT FAIL exit 1 — the correct fail-closed
pre-integration state, cleared when S4's map landed at 20:30:23.

## 4. Stale-wording list (for the closure doc pass)

1. `corpus/fixtures/README.md:1240` — census 171/37/134/421; needs the Round-98
   re-declaration 172/38/134/421 (measured above) + a Round-98 section (absent).
2. `corpus/fixtures/README.md:1236` — "declared four fixtures … r97 … not yet
   pinned (r98 candidate)"; "16 cases".
3. `corpus/fixtures/README.md` — no record anywhere of the r95 map carried
   sentence (now repaired); Round-98 section should carry it.
4. `corpus/README.md:38` — chain four; 16-case; "r97 fixture is not yet pinned".
5. `corpus/README.md:31` — C9 bullet "including the r93 re-check entry".
6. `corpus/README.md` — r97 and r98 fixture navigation bullets missing
   (r97 gap carried from the r97 closure).
7. `SKILL.md:96` — frozen chain four fixtures.
8. `SKILL.md:98` — "16 cases".
9. `SKILL.md:99` — "exactly the four chain fixtures".
10. `SKILL.md:100` — "four fixtures (r97 … unpinned … r98 candidate)";
    "a path-less legacy pin cannot be refreshed in place (manual contract
    edit)".
11. `corpus/knowledge/r91-c9-watch.md` — no r98 row (due; content pre-verified
    in §2d).
12. `corpus/tools/README.md` (S2-owned; Round-98 addendum delivered 20:33:50,
    sha256 `1d299c16…`) — addendum landed and its numbers verify, but the file
    carries two residual wording defects:
    (a) `:232` repeats the carried boilerplate "the self-test scratch still
    lives under the repository root and is not gitignored — unchanged in
    r98", which is **contradicted by the delivered tree**: `.gitignore:4` is
    `*-self-test-*/`; `git check-ignore -v dependency-freeze-self-test-probe/
    map-obligations-self-test-probe/` resolves both to `.gitignore:4`; and the
    tools' prefixes are `dependency-freeze-self-test-`
    (`dependency_freeze.py:544`) and `map-obligations-self-test-`
    (`map_obligations.py:831`), both matching. SKILL.md:98/100 and
    `corpus/fixtures/README.md:1236` already state the scratch is gitignored
    (the r97 closure condition C-4), so the tools-README clause is stale by
    one round (the same clause repeats at `:103`/`:123`/`:179` as history).
    (b) `:284` quotes `git diff 9a3d648 -- corpus/tools/` as listing only
    `dependency_freeze.py` and `dependency-freeze-contract.json`; the command
    also lists `corpus/tools/README.md` (the file the sentence lives in).
13. Carried knowledge-note tool pins — **already repaired by S5 this round**
    (dated addenda in `r95-aftermath-scope-note.md` and
    `r96-response-scope-note.md`, 14 added lines each; their hash claims
    re-verified by me: `map_obligations.py 86b52949…`,
    `map-obligations-contract.json 2142b991…`, `check_bible.py ff9fd2aa…`,
    `support_check.py 55a5eb27…` — all match).

## 5. Poll record and producer-report state

Polls (20 s cadence, artifact + report watch; logs `V22-scratch/poll.log`,
`poll2.log`, `poll3.log`):

- try=1 20:29:42 — r98 map still an r97 byte-copy (17 rows), no seat reports.
- try=2 20:30:03 — first report (`V15-c3-r95-repair.md`).
- try=3 20:30:23 — S4's map landed (20 J-rows).
- try=6 20:31:25 — S1's tool + contract landed (`corpus/tools/dependency_freeze.py`,
  `corpus/tools/dependency-freeze-contract.json`); the self-test then failed
  with `KeyError: 'self_test_mismatch'` for a few seconds (mid-write), green at
  20:31:44 (`SELF-TEST 17/17`).
- poll3 p1 20:32:49 — contract at six pins; S5's `r98-clerk-scope-note.md` on
  disk.
- poll3 p4 20:33:50 — S2's `corpus/tools/README.md` Round-98 addendum landed
  (sha256 `1d299c16…`); poll loop ended READY.
- 20:34:58 — 20 seat reports on disk.

Producer artifacts observed landing: S3's JSON tables + excerpts (~20:28–20:31),
S4's README + map (by 20:30:23), S5's two knowledge addenda (by 20:31) and its
`r98-clerk-scope-note.md` (by 20:32:49), S1's tools (20:31:25; the contract was
rewritten again by S1's `--freeze` runs ~20:33), S2's tools README (20:33:50).
All five producer reports were on disk by 20:35:36 (`S1-freeze-hygiene.md`,
`S2-tools-docs.md`, `S3-fixture-author.md`, `S4-fixture-docs.md`,
`S5-knowledge-notes.md`) — S1's was the last to land and is consistent with my
reads (its contract hash `153ebc5b…` matches the final bytes; the earlier
`c435239d…` in S5's note is stale as of the final delivery). Verifier reports
present: V06, V09, V10, V11, V12, V14, V15, V16, V22, V38, V44, V45, V46, V47,
V50, V55, V59. Final re-verification at 20:35–20:36 on the final contract
bytes: `--self-test` 17/17 PASS; chain six 6/6 PASS; pins 6; cases 17. Endgame
convention noted: any all-reports poll must subtract SELF.

## 6. Bottom line

**PASS (pre-integration doc-parity inventory)** — all four unowned closure docs
verified byte-identical to `9a3d648` (no unowned drift); the Round-98 census
increment 172/38/134/421 independently measured; the r98 fixture's 20/20 + 22/22
receipts, the r95 repair's unchanged receipts, the C9 r98 row's content, the
C1 probes (17/17 self-test, `SELF-TEST-MISMATCH` exit 2, path-less migration),
the six-fixture chain 6/6 with the r97-edge REDUCTION-DETECTED discharge, and
S2's addendum numbers and digests all independently reproduced on the final
bytes. Thirteen stale-wording items are enumerated with exact anchors for the
closure pass — the four closure docs (fixtures README Round-98, corpus README
bullets, SKILL.md freeze row, C9 r98 row) are the round's remaining
documentation work, plus the two wording defects in `corpus/tools/README.md`
recorded as item 12. All five producer reports were on disk by 20:35:36.
