# V53 — cross-seat-audit (round 97)

**Seat:** V53 cross-seat-audit (verifier, single-wave round-97 swarm, lore-shokunin lane).
**Scope (verbatim):** *Re-run 6 load-bearing quoted outputs from other seats; REPRODUCED/MISMATCHED.*
**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent
repo; every path below is absolute or `cd`-anchored there, and every write of this seat used an absolute
path under the lane repo).
**Baseline:** r96 closure `f3e09f9` (lane HEAD observed `2393934 lore r96: close round — SCORECARD admitted section`).
**Writes of this seat:** this report and `.ufo/waves/round-97/seats/V53-scratch/**` only. No commits, no
pushes, no network, no nested agents, no writes to any producer-owned path.

**STATUS: FINAL — all six audit items re-run independently: 6 REPRODUCED, 0 MISMATCHED.** R3's seat report
landed at 18:56:23 (after the contract it produced), so the C2 item is quoted from R3 and V26, both on disk at
the time of the re-runs; every item names the revision it ran against.

## 0. Revision binding

Hashes of the artifacts my re-runs actually executed against (taken at the moment of each run; re-checked
before every item, because R1/R2/R3 were editing under me):

```
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py            (R1 delivered)
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json (R2 delivered)
6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992  corpus/tools/README.md                     (R2 delivered)
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py          (R3 delivered)
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json (R3 delivered, 18:55:14)
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py             (unmodified)
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py              (unmodified)
```

R1's and R2's declared delivered hashes match these tool/contract/README hashes exactly (verified by
`sha256sum`, §A1). The `dependency_freeze.py`/contract pair moved several times while this seat ran
(`a3b57978…`/`c65ac3bd…` r96 → `fbaca38f…`/`c65ac3bd…` → `b06275f3…`/`8015e1f9…` → `b06275f3…`/`625ccfac…`
→ `b06275f3…`/`27273be2…`); every C2 statement below names the revision it ran against, and the C2 item was
re-run on the final pair quoted above.

## 1. Poll-wait record

Protocol: 20 s cadence, 40 tries; no artifact was verified before its producer's report existed on disk, and
no plan was ever verified. Poller: `.ufo/waves/round-97/seats/V53-scratch/poll.sh` (log tail quoted).

```
try=15 t=18:47:46 reports=1 producers=0
try=21 t=18:49:46 reports=10 producers=2
try=25 t=18:51:06 reports=14 producers=3
```

Producer reports observed on disk during the seat: `R1-map-pinning.md` (18:48), `R2-contract-docs.md` (18:47),
`R4-fixture-author.md` (18:50), `R5-fixture-docs.md` (18:51), `R6-knowledge-note.md`, `R3-freeze-hardening.md`
(18:56:23 — located by a second targeted poller, `.ufo/waves/round-97/seats/V53-scratch/poll-r3.sh`, which
reported `R3_READY` at try=14). Each audit item re-runs an output quoted by a seat whose report was on disk at
the time of the re-run.

## 2. Audit items

### A1 — C1: the persisted self-test is 25/25 with `dual_pointer` PASS — **REPRODUCED**

Quoted by **R2** (`R2-contract-docs.md` §(1)) and **R1** (`R1-map-pinning.md` §2):

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
… 25 × "SELF-TEST PASS <case> …"
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
exit=0
```

My re-run (command verbatim, repo root, delivered revision `86b52949…`):

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
exit=0
```

Independent check of the revision binding R2 declared (all three equal R2's stated hashes):

```
$ sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992  corpus/tools/README.md
$ git diff --numstat HEAD -- corpus/tools/README.md
49	0	corpus/tools/README.md
$ git diff HEAD -- corpus/tools/README.md | grep -c '^-[^-]'
0
```

Contract case ids re-parsed independently: 25 ids, `dual_pointer` present exactly once.
**Verdict: REPRODUCED** (identical output, identical revision).

### A2 — C1: a contract that drops a pinned case now fails closed — **REPRODUCED**

Quoted by **R2** (`R2-contract-docs.md` §(2), "After (delivered revision)"):

```
$ (scratch contract: dropped 'schema_drift', cases 25 -> 24)
FINDING self_test_contract: contract drops implemented self-test cases: schema_drift
RESULT ERROR
probe_drop_schema_drift_exit=2
```

My re-run — byte-identical copy of the delivered tool (`86b52949…`) beside a scratch copy of the delivered
contract with the single `schema_drift` case removed (25 → 24), so the delivered contract was never mutated:

```
$ python3 a2/map_obligations.py --self-test
FINDING self_test_contract: contract drops implemented self-test cases: schema_drift
RESULT ERROR
exit=2
```

Before-state control from the frozen r96 tool (`2b0ba815…`, extracted from `f3e09f9` before R1 landed), with
the same one-case removal — this is the tolerance the claim closes:

```
$ python3 b1/map_obligations.py --self-test      # r96 tool, contract 24 -> 23 cases
SELF-TEST CASES 23/24 pinned
RESULT PASS
exit=0
```

**Verdict: REPRODUCED** — the r96 tolerance is real, and the delivered loader closes it with exit 2.

### A3 — C1: the new pin is load-bearing under neutralization — **REPRODUCED**

Quoted by **R2** (`R2-contract-docs.md` §(3)):

```
SELF-TEST CASES 25/25 pinned
SELF-TEST FAIL dual_pointer exit=0 findings=none
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR
exit=2
```

My re-run — copy of the delivered tool with `second_pointer_mention()` short-circuited to `return None`
(the same neutralization R2 describes), delivered contract untouched:

```
$ python3 a3/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
SELF-TEST FAIL dual_pointer exit=0 findings=none
RESULT PASS
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR
exit=2
```

The two terminal `RESULT` lines and exit 2 match R2's quote exactly (the `RESULT PASS` is the last per-case
line; `RESULT ERROR` is the tool's verdict). Before-state control: the same neutralization applied to the
frozen r96 tool left `--self-test` green (`SELF-TEST CASES 24/24 pinned` / `RESULT PASS` / exit 0), because
r96 had no persisted `dual_pointer` case — i.e. the pin, not the emission, is what makes this red.
**Verdict: REPRODUCED.**

### A4 — C3-repair: R4's cosmetic repair is byte-minimal and receipt-neutral — **REPRODUCED**

Quoted by **V19** (`V19-c3-r96-repair-scope.md`, Claim 1):

```
$ git diff --numstat f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
2	2	corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
$ git diff -U0 f3e09f9 -- … | grep -c '^@@'
2
$ cmp pre-rows post-rows            → DATAROWS-IDENTICAL 18 rows  (block sha256 1ff29a75…)
```

My re-run (all three commands, repo root):

```
$ git diff --numstat f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
2	2	corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
$ git diff -U0 f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | grep -c '^@@'
2
$ git show f3e09f9:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | grep -E '^\| (J[0-9]{2}|S[0-9]{2}) ' > pre-rows.txt
$ grep -E '^\| (J[0-9]{2}|S[0-9]{2}) ' corpus/fixtures/r96-crossing-response/claim-excerpt-map.md > post-rows.txt
$ cmp pre-rows.txt post-rows.txt && echo "DATAROWS-IDENTICAL $(wc -l < post-rows.txt) rows"
DATAROWS-IDENTICAL 18 rows
$ sha256sum post-rows.txt
1ff29a751c8b15231d87ad91ff10f7c6dbe396cf93c622f462a49df92ff9231f  post-rows.txt
```

The data-row block hash reproduces V19's quoted `1ff29a75…` exactly.

Receipt invariance (quoted by **R1** §5 and **R4** "Receipts unchanged by the repair") — I ran the delivered
tool against two scratch clusters that differ only in the map revision (pre-repair bytes from
`git show f3e09f9:…`, post-repair bytes from the working tree; identical JSON tables in both):

```
$ python3 corpus/tools/map_obligations.py repair/pre    # pre-repair map
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                             exit=0
$ python3 corpus/tools/map_obligations.py repair/post   # post-repair map
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                             exit=0
$ diff <(…) <(…)   → BYTE-IDENTICAL RECEIPTS
```

**Verdict: REPRODUCED** — two changed lines, two hunks, data rows byte-identical, r96 receipts unmoved.

### A5 — C3: the census delta 170 → 171 with 421 violation lines — **REPRODUCED**

Quoted by **V13** (`V13-c3-checker.md`, "Census (independent repo-relative replica, fresh implementation)"):

```
pre-r97 : {'fixture_dirs': 170, 'clean_exit0': 36,  'negative_exit1': 134, 'violation_lines': 421, 'non_0_1_exits': []}
post-r97: {'fixture_dirs': 171, 'clean_exit0': 37,  'negative_exit1': 134, 'violation_lines': 421, 'non_0_1_exits': []}
```

My re-run — own loop over `corpus/fixtures/*/` with repo-relative `check_bible.py` arguments (the convention
`corpus/fixtures/README.md:1046` mandates), counting exits and `^VIOLATION` lines
(`.ufo/waves/round-97/seats/V53-scratch/census.sh`):

```
$ .ufo/waves/round-97/seats/V53-scratch/census.sh
CENSUS dirs=171 clean=37 negative=134 violation_lines=421 non01=0
```

**Verdict: REPRODUCED** — 171 dirs, 37 clean, 134 negative, 421 violation lines, zero non-0/1 exits.

### A6 — C2: `dependency_freeze` hardening (scope guard, path binding, 16/16) — **REPRODUCED**

Quoted by **R3** (producer, `R3-freeze-hardening.md` §(a) scope guard, §(d) self-test, §(b) path binding,
"Final receipts"):

```
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/tools            -> SCOPE-REFUSED exit 2
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures         -> "refuses corpus/fixtures itself" SCOPE-REFUSED exit 2
contract sha before=8015e1f9… after=8015e1f9… unchanged=YES
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V38-scratch/d3/r94-paired-crossing   # delivered
FINDING PATH-MISMATCH: pin r94-paired-crossing names corpus/fixtures/r94-paired-crossing (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r94-paired-crossing); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V38-scratch/d3/r94-paired-crossing
RESULT ERROR
exit=2
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -2
SELF-TEST 16/16
RESULT PASS
```

and by **V26** (`V26-doc-parity.md` §2.2, same findings with the long path text elided `…`).

My re-runs on the delivered revision (`dependency_freeze.py` `b06275f3…`, contract `27273be2…`), commands
verbatim:

```
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/tools
FINDING SCOPE-REFUSED: --freeze refuses corpus/tools (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools); the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
exit=2
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**
RESULT ERROR
exit=2
$ sha256sum corpus/tools/dependency-freeze-contract.json     # after both refusals
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V38-scratch/d3/r94-paired-crossing
FINDING PATH-MISMATCH: pin r94-paired-crossing names corpus/fixtures/r94-paired-crossing (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r94-paired-crossing); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V38-scratch/d3/r94-paired-crossing
RESULT ERROR
exit=2
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 16/16
RESULT PASS
exit=0
```

R3's `PATH-MISMATCH` line reproduces character-for-character, and the contract hash is unchanged across both
refusals (the refusals are read-only: `SCOPE-REFUSED` fires before any write). I also ran the foreign-path
shadow probe independently (byte-identical same-named copy at a scratch path, §A6 earlier revision) and a
scope-guard probe against a byte-identical tool/contract pair in a scratch fakerepo, so the producer-owned
contract could not be rewritten even had the guard failed. The chain half was re-run on the real tree with
digests unchanged (`15ef230e…`, `2527beb9…`, `d541ae64…`, `d422a9b3…`, all `RESULT PASS` exit 0).

**The declared "r96 re-frozen through the guarded path" is present and measurable, and R3 self-reports the one
claim discrepancy.** A `--freeze` at this HEAD records `git rev-parse HEAD` in the pin (verified in the scratch
fakerepo: an in-scope refresh wrote `revision: 2393934237ea076366f3db6dceeff033edb52ab1`); the delivered
contract's `pins.r96-crossing-response.revision` moved `60dba0c2…` (r95 closure) → `2393934…` (r96 closure
commit) while its digest stayed `d422a9b3…`, and the r88/r94/r95 pins kept `60dba0c2…` (untouched) — the exact
pin-refresh signature, also recorded in the contract's own `provenance_note`. R3's report states the claim's
"digest changes by the repair" wording is **not** what happens (the repair touched `claim-excerpt-map.md`, which
is not a pinned data file, so the digest cannot move); it reports the refresh as a guard/format/revision refresh
instead. My measurements agree with R3's reading, not with the claim's stated cause. A mid-flight state was
observed first (tool landed 18:51:24, contract still `c65ac3bd…`), where the tool failed closed:
`FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['path_mismatch', 'scope_refused'] extra=[]`
/ `RESULT ERROR` exit 2 — recorded here as observed, and superseded by the delivered pair.

**Verdict: REPRODUCED** — `SCOPE-REFUSED` exit 2 with the contract byte-untouched, `PATH-MISMATCH` exit 2 for a
byte-identical foreign-path copy (r96 behaviour was exit 0), self-test 16/16 green, chain 4/4 clean, pin refresh
present. Digest-file naming re-run separately on a path-correct tampered copy (R3 §(c) quotes the same shape):

```
FINDING DIGEST-MISMATCH: content digest d7abd8be… != pin d422a9b3…; changed: sources.json (sha256 9f973f63… -> 43bb7a06…); fixture bytes changed outside the frozen inventory
RESULT ERROR   exit=2
```

**The `/tmp` host condition is fixed by the delivered revision, not worked around:** R3's harness now builds its
scratch under `dir=ROOT` (`dependency_freeze.py:517`), and with `/tmp` recovered (2% inodes used at this check)
the unredirected `python3 corpus/tools/dependency_freeze.py --self-test` passes `SELF-TEST 16/16` / `RESULT PASS`
exit 0. My earlier `OSError: [Errno 28]` observation was against the pre-hardening revision.

## 3. Extra corroboration (beyond the six, all re-run here)

- **r97 fixture gates** (quoted by R4/R5/V13/V20): `check_bible` → `CLEAN: schema, citations, relations,
  timeline; 0 violations` exit 0; `map_obligations` → `OBLIGATIONS raw=17 mapped=17` /
  `INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19` / `RESULT PASS` exit 0;
  `support_check` → `SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0
  anchors); MODES 19/19; VALIDATED-ROWS 19/19` / `RESULT PASS` exit 0. All three REPRODUCED.
- **Preserving-copy structure** (quoted by V50/V14): `entities.json`, `relations.json`,
  `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` byte-identical r96↔r97 (`cmp -s`),
  `timeline.json` and `sources.json` pure appends (+1 event, +1 source), `fictional-excerpts.md` a strict
  byte-prefix append. REPRODUCED.
- **r97 map inheritance** (quoted by R5): the r97 map vs the r96 map, namespace-normalized, differs in
  exactly the header/scope/inventory/declaration lines plus one new `J17` row; the 16 inherited J-rows are
  unchanged. REPRODUCED by `diff` of the two maps.
- **Before-state hazards** (quoted by V45's "before-state evidence" section, independently reproduced here
  from a frozen r96 tool in a scratch fakerepo): a byte-identical same-named copy at a foreign path verified
  `RESULT PASS` exit 0; `DIGEST-MISMATCH` named only digests, not the changed file; `--freeze` on an
  out-of-scope directory exited 0 and rewrote the pin path to `foreign/r96-crossing-response`. All three
  REPRODUCED — the hazards C2 declares are real in the r96 tool.

## 4. Observations (not verdicts; reported exactly as seen)

1. **Host condition (observed, then repaired in-round):** `/tmp` was inode-exhausted while this seat ran
   (`df -i /tmp` → `1048576` inodes, `1048575` used, 1 free). The `dependency_freeze` revision on disk at that
   moment built its self-test tree with `tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-")`
   and no `dir=`, so the unredirected self-test aborted:
   `OSError: [Errno 28] No space left on device: '/tmp/dependency-freeze-self-test-yevc0bav/reduction_edge_drop'`.
   The delivered revision passes `dir=ROOT` (`dependency_freeze.py:517`), and by the end of this seat's run
   `/tmp` had recovered (`15694` inodes used, 2%), so the unredirected `--self-test` passes 16/16. `map_obligations.py:831`
   already passed `dir=ROOT`. V09/V26 report the same condition. Host condition, not a repo finding.
2. **Doc staleness flagged by R2, confirmed present and outside any producer's byte-ownership:** `SKILL.md:87`
   and `corpus/README.md:37` still say "24 cases"/"24 persisted cases" after the contract moved to 25. Closure-side
   doc work, not a claim failure.
3. **r97 is intentionally not in the freeze chain:** `dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment`
   → `FINDING UNPINNED-FIXTURE … (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath',
   'r96-crossing-response'])`, exit 2. Consistent with the declared four-fixture frozen set; recorded so the exit 2
   is not misread as a regression.
4. **One claim-vs-artifact wording discrepancy, self-reported by R3 and confirmed here:** the round claim says the
   r96 pin refresh happens because "the digest changes by the repair". The digest does **not** change
   (`d422a9b3…` before and after; `claim-excerpt-map.md` is not a pinned data file), and only the pin `revision`
   moved. R3 records this in its own report; the deliverable is present either way.
5. **Transient self-test scratch at the repo root, observed once and gone on re-check:** `git status --porcelain`
   showed `?? map-obligations-self-test-s39eou49/` while another seat's `--self-test` was mid-run; a re-check
   seconds later found the directory removed and no `map_obligations.py --self-test` process running. This matches
   R1's hygiene claim (`TemporaryDirectory` under `ROOT`, removed on exit) and the carried BR-05 note that the
   self-test scratch lives under the repository root and is not gitignored — a transient window, not residue.

## Bottom line

**PASS — 6/6 load-bearing quoted outputs from other seats re-run independently: 6 REPRODUCED, 0 MISMATCHED**
(R1/R2 self-test 25/25 + `dual_pointer`; R2 loader fail-closed on a dropped pin; R2 pin load-bearing under
neutralization; V19/R4 byte-minimal receipt-neutral r96 repair; V13 census 171/37/134/421; R3/V26 C2 scope
guard, `PATH-MISMATCH`, 16/16, chain 4/4, pin refresh). One claim-wording discrepancy (pin refresh cause, not
outcome) is recorded in §4.4; no axis is harmed by anything measured here.
