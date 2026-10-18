# V26 — verdict-coverage (round 98, single-wave)

**Seat scope (verbatim):** *V26 verdict-coverage — report
.ufo/waves/round-98/seats/V26-verdict-coverage.md — Read C2 seats; own chain
replay; one COVERAGE verdict with bounds.*

Claim under test — **C2 (coverage):** "extend the frozen chain through the
round's own fixture. After S3 authors `r98-clerk-filing`, S1 pins BOTH
`r97-crossing-acknowledgment` and `r98-clerk-filing` via the guarded
`--freeze`; the chain becomes six fixtures (r88-m3, r94, r95, r96, r97, r98)
verifying 6/6 clean; V46's recorded FAIL (the r97 tick-13 edge unfrozen) is
discharged by the pin, demonstrated by a scratch REDUCTION-DETECTED on the r97
edge."

Repo root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the PARENT repo; every path below absolute or lane-root
anchored). Baseline r97 closure `9a3d648`; HEAD during the wave `dd4df1b`
(wave tree uncommitted). Leaf seat: no nested agents, no commits, no pushes,
no network. Writes: this report plus `.ufo/waves/round-98/seats/V26-scratch/`
(`poll.sh`, `replay.py`, `mirror/`) only. Seats-dir realpath checked before
writing: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats`.

## 0. Revision pinned for every measurement (re-checked after all runs)

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py          (S1)
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json (S1, 6 pins, 17 cases)
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  corpus/fixtures/r97-crossing-acknowledgment/timeline.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
```

Mid-flight record (honest): S1's contract was first observed at
`c435239d…` (pins already present); S1 then edited it to `153ebc5b…`
(20:33:36) — the change is the r98 `provenance_note` paragraph only (pins and
self-test expectations byte-identical; V06 §"Mid-flight note" records the same
structural diff). My early chain/pins/self-test/mirror runs were on
`c435239d…`; **every number quoted below was re-run on the final revision
`153ebc5b…`** (chain/pins/self-test 20:35–20:36, mirror 20:36). No result
rests on superseded bytes.

## 1. Poll-wait record (20 s cadence, 40 tries; never verify a plan)

- 20:27–20:28 first inspection: seats dir near-empty; `r98-clerk-filing/`
  appeared 20:28 as a **byte-identical copy of r97** (placeholder phase; S3
  copies the 10-file tree, then extends 4, S4 rewrites README/map). My poll
  was **content-gated** (`clerk-maren` in entities, `clerk-filing-open` in
  timeline, both r97/r98 pins present), so the placeholder never satisfied it.
- 20:29:24–20:35:24 poll tries 1–19: S3 report try 6, S4 report try 10, pins
  present try 11, S1 report try 19 → **READY** (no stall escape needed; no
  timeout). SELF (V26) was never in any wait set; no all-reports poll was
  attempted.
- Consistent with V06/V54, which both recorded S1's *report file* ABSENT at
  their write time (artifacts present and hash-stable) — their bounded
  stall-escapes and my try-19 READY are the same endgame class, no
  contradiction.

## 2. Pre-state (baseline tree, contract `27273be2…`, ~20:29)

V46's recorded FAIL reproduced live before S1 landed — chain replay via the
unmodified tool:

```
r88 -> FREEZE … events 2/2 … RESULT PASS  EXIT=0
r94 -> events 3/3 … PASS  EXIT=0
r95 -> events 4/4 … PASS  EXIT=0
r96 -> events 5/5 … PASS  EXIT=0
r97 -> FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' … RESULT ERROR  EXIT=2
r98 -> FINDING UNPINNED-FIXTURE: no pin for 'r98-clerk-filing' … RESULT ERROR  EXIT=2
```

My independent digest recompute also matched all four baseline pins
(`15ef230e…`, `2527beb9…`, `d541ae64…`, `d422a9b3…`) — algorithm validated
against the tool's own recorded digests before any new pin existed.

## 3. Post-state — chain replay, pin recompute, self-test (final revision)

Six-fixture chain, delivered tool on delivered paths — **6/6 PASS exit 0**
(receipts and `DIGEST` lines):

```
r88-m3-maya-cluster          events 2/2; edges 0/0; relations 0/0   DIGEST 15ef230ef806ea7e…fc3fc279
r94-paired-crossing          events 3/3; edges 2/2; relations 1/1   DIGEST 2527beb938b474a2…7ecebe75
r95-crossing-aftermath       events 4/4; edges 3/3; relations 1/1   DIGEST d541ae641f3189e1…e66d2ec9
r96-crossing-response        events 5/5; edges 4/4; relations 1/1   DIGEST d422a9b3d95c4e0b…657d7f6
r97-crossing-acknowledgment  events 6/6; edges 5/5; relations 1/1   DIGEST 3c922d20a01bbd3f…f83abea6
r98-clerk-filing             events 7/7; edges 6/6; relations 1/1   DIGEST 59a0f4fa3d4a47e0…d9b9b133
```

Pin recompute (my own algorithm: per-file sha256 over the five JSON tables →
compact sorted-JSON digest) — **6/6 `match=True`**; the four inherited pins'
digests unchanged vs baseline; pin set is exactly six, no extras; r97/r98 pin
revisions are `dd4df1b…` (= HEAD at freeze), r88/r94/r95 `60dba0c2…`, r96
`23939342…`; the r98 pin carries `clerk-filing-open` tick 14,
`depends_on ['acknowledgment-aru-records']`, endpoint
`{tick: 14, entity_id: clerk-maren, place_id: chalk-stair}`.

`--self-test` on the final revision: `SELF-TEST 17/17`, `RESULT PASS`,
exit 0 (the 17th case is C1's; quoted as revision sanity, not this seat's
verdict).

## 4. V46 discharge — own mirror replay (final revision)

Mirror root `V26-scratch/mirror/` holds byte copies of the delivered tool +
contract and the r97/r98 fixtures at their pinned repo-relative paths; the
delivered contract is never written.

```
$ python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r97-crossing-acknowledgment   # intact
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
RESULT PASS                                                                                   EXIT=0
$ # drop the tick-13 edge (V46's exact mutation), then:
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL                                                                                   EXIT=1
```

The mutated `timeline.json` sha256 is
`37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1` — **byte-identical
to the sha V46 recorded** for its r97 scratch copy (V46 report §1; S1 §4;
V06 §1 `cmp`). The same mutation at the delivered path verifies clean
(chain above). The r98 edge drop reproduces the same class
(`FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on
['acknowledgment-aru-records']`, exit 1; mutated sha
`ddec7a072fa21919ca1faeae49f7ee7b7f1eae20bcd36653942eee58cceec34f`, matching
V54's independent probe). Delivered controls after all mirror writes: r97 and
r98 both `RESULT PASS` exit 0.

## 5. "Via the guarded `--freeze`" — what I can and cannot show

- **Guard still armed:** `--freeze` on an out-of-scope target →
  `FINDING SCOPE-REFUSED … the frozen scope is corpus/fixtures/**`,
  exit 2, and the mirror contract was byte-unchanged (`unchanged: True`).
- **Pins reproducible through the guarded path:** re-freezing r97 and r98 in
  the mirror printed `FROZEN …` + `DIGEST` and the resulting pin digests equal
  the delivered pins exactly (`3c922d20…` == `3c922d20…` True;
  `59a0f4fa…` == `59a0f4fa…` True). The r97 digest also equals the digest V46
  produced when it froze the fixture in its own r97 scratch mirror — the
  delivered pin is the same inventory on the same bytes V46 demonstrated the
  catch with.
- **Bound:** I did not witness S1's original invocation. The "guarded
  `--freeze`" claim rests on (a) S1's report §4 quoting the two freeze
  commands and receipts, (b) the contract `provenance_note` r98 paragraph
  (same receipts, revision `dd4df1b…`, the V46 mutation sha), and (c) my
  reproduction of the digests through the guarded path on identical bytes.
  No contradiction found.

## 6. Bounds probes (coverage edges, demonstrated on r98 in the mirror)

- **Digest half:** appending bytes to `clerk-filing-open.description` (not
  modelled by the inventory) →
  `FINDING DIGEST-MISMATCH: content digest bcf0e047… != pin 59a0f4fa…;
  changed: timeline.json (sha256 eb24e084… -> 14f77aab…)`, exit 2. So
  non-inventory JSON changes are caught, but as could-not-evaluate (exit 2),
  not as an exit-1 finding.
- **Markdown unpinned:** appending a line to the r98 `README.md` (markdown is
  outside the five-JSON-table payload) → still `RESULT PASS` exit 0. The pin
  payload bound is real and matches the README/contract declarations; BR-01's
  markdown/prose half remains open (documented, unchanged).

## 7. Cross-checks against the C2 seats and neighbors

- **S1-freeze-hygiene.md:** tool/contract shas, freeze receipts (`3c922d20…`,
  `59a0f4fa…`), chain 6/6 digests, and the V46 mutation sha `37a425b9…` all
  match my independent runs character for character.
- **S3-fixture-author.md:** r98 timeline sha `eb24e084…`, entities
  `db2d8e5d…`, sources `32ee15b1…` match my on-disk hashes; its freeze
  cross-check (`d541ae64…` PASS) matches mine.
- **V06-c2-v46-discharge.md / V54-six-chain-integrity.md:** both PASS; their
  numbers (pins 6/6, revisions, mutation shas `37a425b9…`/`ddec7a07…`,
  `PATH-MISMATCH` control, 17/17 self-test) agree with mine on every shared
  value. V54's independent raw-JSON recompute adds a second method to my
  replay.
- **S2-tools-docs.md (README addendum):** its chain/self-test/receipt claims
  verified against my runs; the claim "the 16 inherited cases with
  byte-identical expectations" verified by a parsed diff vs
  `git show 9a3d648:…` (`added: ['self_test_mismatch']`, `removed: []`,
  `changed among inherited: []`).
- **Minor contradiction (doc wording, three places):** S2's README addendum
  (`corpus/tools/README.md:284`), S2's report §"Unchanged" (line 146, quoting
  the `--stat` form) and S1's report §6 all state that
  `git diff 9a3d648 -- corpus/tools/` "lists only `dependency_freeze.py` and
  `dependency-freeze-contract.json`". Actual outputs:

  ```
  $ git diff 9a3d648 --name-only -- corpus/tools/
  corpus/tools/README.md
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/dependency_freeze.py
  $ git diff --stat 9a3d648 -- corpus/tools/
   corpus/tools/README.md                       |  56 ++++++++
   corpus/tools/dependency-freeze-contract.json | 193 ++++++++++++++++++++++++++-
   corpus/tools/dependency_freeze.py            |  42 +++++-
   3 files changed, 281 insertions(+), 10 deletions(-)
  ```

  Three files — the third is S2's own addendum (trivially self-referential;
  the claim would be exact for `corpus/tools/*.py` or with the README
  excluded). The substance ("`map_obligations.py`,
  `map-obligations-contract.json`, `support_check.py`, `boundary_doc_check.py`
  byte-unchanged") is true. Recorded as a wording slip, not a coverage defect.
- **Placeholder-poll hazard (evidence, not a verdict):** between S3's copy
  (20:28) and S4's rewrites, r98's README/map existed with r97 bytes; an
  existence-only poll is satisfied there (S3 §D1, S4 §A record it; my poll was
  content-gated). No impact on C2 (JSON-only tool).
- **Parent-repo stray (r94-F01 class, observed directly):**
  `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (105 bytes, mtime
  20:30) contains `python3: can't open file '…/analyze.py': [Errno 2] No such
  file or directory` — a redirected shell output written outside the lane,
  unattributed; not written by this seat; left untouched for the L1.

## 8. Bounds of this coverage verdict

1. The pin payload covers the five JSON tables only; markdown
   (`README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`) is not
   pinned (demonstrated in §6; declared in README/contract). Coverage of
   fixture docs rests on other gates, not this pin set.
2. Exit-1 findings cover `depends_on` edges, event endpoints, and relation
   triples; every other JSON change is at most exit-2 `DIGEST-MISMATCH`.
3. The chain is a declared list, not self-enforcing: nothing enumerates
   `corpus/fixtures/**`; an unpinned fixture is only refused when invoked
   (`UNPINNED-FIXTURE` exit 2).
4. Pin `revision` names HEAD `dd4df1b` while the wave bytes are uncommitted —
   the byte binding is the content digest, which I reproduced through the
   guarded path; it does not prove S1's original command history (§5).
5. "Discharged" here means: the pin exists, the delivered fixture verifies
   clean, and V46's exact mutation bytes are caught as `REDUCTION-DETECTED`
   exit 1 — verified independently by me and by V06/V54. V46's r97 FAIL
   remains recorded in r97 history; the discharge is a fact of this revision.
6. No canon-truth, rights, identity, or entailment inference anywhere; this
   verdict is about the frozen dependency inventory only.

## 9. Write audit

`git status --porcelain` at write time shows, besides `LOG.md`, exactly the
declared producer paths (`corpus/tools/dependency_freeze.py`,
`dependency-freeze-contract.json`, `corpus/tools/README.md`,
`r95-crossing-aftermath/claim-excerpt-map.md`, the two scope notes,
untracked `r98-clerk-filing/` + `r98-clerk-scope-note.md`) — nothing else,
no strays. Final hash sweep after all my runs: tool `03d04365…`, contract
`153ebc5b…`, README `1d299c16…`, r97 timeline `73063a86…`, r98 timeline
`eb24e084…` — all unchanged across my measurement window. My writes live only
under `.ufo/waves/round-98/seats/V26-scratch/` plus this report.

## Bottom line

**PASS — COVERAGE verdict: improved and verified (bounded).** On the frozen
revision (tool `03d04365…`, contract `153ebc5b…`, six pins) the chain verifies
6/6 clean with all six pin digests recompute-matched, the r97/r98 pins
reproduce exactly through the guarded `--freeze` in a mirror, and V46's
recorded r97 FAIL is discharged — its exact mutation bytes (`37a425b9…`)
now yield `REDUCTION-DETECTED` exit 1 where round-97 yielded
`UNPINNED-FIXTURE` exit 2; bounded to the five-JSON-table pin payload, the
declared six-fixture list, and exit-2-only detection for non-inventory JSON
changes, with BR-01's markdown/prose half still open.
