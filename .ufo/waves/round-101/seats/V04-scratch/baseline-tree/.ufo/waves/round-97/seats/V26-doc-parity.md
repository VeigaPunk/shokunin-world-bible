# V26 — doc-parity: pre-integration inventory (round 97)

Seat: V26 (doc-parity, verifier/judge wave). Repo: `/home/vgpnk/Projects/shokunin/lore-shokunin` (all writes absolute
under this repo). Baseline: r96 closure `f3e09f9` (HEAD `2393934`). Poll outcome: **POLL_READY try=40, reps=6** — all six
producer artifacts and all six producer reports present; nothing ABSENT.

This seat's deliverable is the pre-integration inventory: which doc surfaces must change at integration, with measured
evidence and the stale-wording list. None of those docs are producer-owned this round (they are integration-time files),
so this report does not edit them. Every number below was measured by this seat's own commands unless attributed.

## 0. Delivered revision pins (final, after all producer writes)

| Artifact | sha256 |
|---|---|
| `corpus/tools/map_obligations.py` | `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` |
| `corpus/tools/map-obligations-contract.json` | `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41` |
| `corpus/tools/dependency_freeze.py` | `b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130` |
| `corpus/tools/dependency-freeze-contract.json` | `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781` |
| `corpus/fixtures/check_bible.py` (C9 pin) | `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` |

Working tree at this write: `git status --short` shows `M LOG.md`, `M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`,
`M corpus/tools/{README.md,dependency-freeze-contract.json,dependency_freeze.py,map-obligations-contract.json,map_obligations.py}`,
`?? .ufo/waves/round-97/`, `?? corpus/fixtures/r97-crossing-acknowledgment/`, `?? corpus/knowledge/r97-acknowledgment-scope-note.md`.

## 1. Baseline measurements (r96-closure tool state, before producer writes)

```sh
python3 corpus/tools/map_obligations.py --self-test
# 24 SELF-TEST PASS lines; RESULT PASS; exit 0            (V26-scratch/mo-selftest-baseline.txt)
TMPDIR=$PWD/.ufo/waves/round-97/seats/V26-scratch/tmp python3 corpus/tools/dependency_freeze.py --self-test
# SELF-TEST 14/14; RESULT PASS; exit 0                    (V26-scratch/df-selftest-baseline.txt)
```

The first, unredirected `dependency_freeze --self-test` run **crashed**:
`OSError: [Errno 28] No space left on device: '/tmp/dependency-freeze-self-test-pl64fni3/reduction_edge_drop'`.
Measured cause: `df -i /tmp` → `tmpfs 1048576 inodes, 1048576 used, 0 free (100%)` — wave-wide inode exhaustion, not a
tool defect; `df -h /tmp` showed 8.5G free. With `TMPDIR` under the repo the same command passed 14/14. (R3's report
independently records the same condition and moved the tool's scratch to `dir=ROOT`; the delivered revision no longer
depends on `/tmp`.) **Integration-time self-test runs should still avoid `/tmp` while the wave drains.**

## 2. Delivered-revision measurements

### 2.1 C1 surface — `map_obligations`

- Loader tightening observed live: at 18:45 the R1 tool (then implemented 25 cases) ran against the still-24-case contract
  and failed closed: `FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer` / `RESULT ERROR`,
  exit 2 — exactly C1(b).
- Final: `python3 corpus/tools/map_obligations.py --self-test` → `SELF-TEST CASES 25/25 pinned` / 25 `SELF-TEST PASS` lines
  (last `dual_pointer exit=1 findings=['dual_pointer']`) / `RESULT PASS`, exit 0 (V26-scratch/mo-selftest-r2.txt).
- Contract case ids (25, `self_test.cases`): complete, missing, duplicate, phantom, source_id_mismatch, schema_drift,
  inventory_mismatch, malformed_json, co_mapped_grammar, legacy_grammar, invalid_pointer, empty_segment,
  noncanonical_index, noncanonical_claim_index, foreign_path, traversal_path, symlink_path, frozen_complete,
  frozen_tampered, frozen_missing_digests, frozen_expected_failure, frozen_verdict_mismatch, map_missing,
  invalid_arguments, dual_pointer.
- r97 run: `OBLIGATIONS raw=17 mapped=17` / `INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19` /
  `RESULT PASS`, exit 0.

### 2.2 C2 surface — `dependency_freeze` (final tool `b06275f3…`, contract `27273be2…`)

```sh
TMPDIR=… python3 corpus/tools/dependency_freeze.py --self-test
# CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
# CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
# SELF-TEST 16/16 / RESULT PASS   exit 0
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
# chain 4/4 RESULT PASS exit 0, digests: 15ef230e… / 2527beb9… / d541ae64… / d422a9b3…
```

Scope-guard probes (each exit 2, contract byte-untouched, `sha256sum` `27273be2…` before and after):

```sh
python3 corpus/tools/dependency_freeze.py --freeze .ufo/waves/round-97/seats/V26-scratch/foreign-probe
# FINDING SCOPE-REFUSED: --freeze refuses … ; the frozen scope is corpus/fixtures/** (integration-time operation only)
python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures
# FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**
```

Path binding (byte-identical same-named copy at a foreign path):

```sh
mkdir -p .ufo/waves/round-97/seats/V26-scratch/foreign && cp -r corpus/fixtures/r96-crossing-response .ufo/waves/round-97/seats/V26-scratch/foreign/r96-crossing-response
python3 corpus/tools/dependency_freeze.py .ufo/waves/round-97/seats/V26-scratch/foreign/r96-crossing-response
# FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response (resolves to …); invoked fixture resolves to …   exit 2
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
# FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1 / DIGEST d422a9b3… / RESULT PASS   exit 0
```

Code-level facts (read-only inspection of the final revision): `scope_guard()` runs first in `freeze()`; `bind_path()`
compares the invoked fixture's resolved path to the pinned repo-relative `fixture`; `DIGEST-MISMATCH` names changed files
with before/after digests via `changed_files()`; `FROZEN_CASES` holds 16 ids (14 inherited + `scope_refused`,
`path_mismatch`). Pins: exactly the four chain fixtures, each carrying `fixture` (repo-relative), `revision`,
`content_sha256`, per-file digests, `events`, `relations`, `counts`; r97 is not in the chain, as declared. R3's report
records two further fail-closed behaviors beyond the four declared items: `--freeze` also refuses a same-named **in-scope**
target when a pin already names a different path, and `freeze` propagates the post-freeze verify exit code. Both are
worth one sentence in the SKILL.md row/README update (they are delivered behavior, currently undocumented).

### 2.3 C3 surface — `r97-crossing-acknowledgment` (delivered)

Shape: `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` byte-identical
to post-repair r96 (`cmp` clean); `timeline.json` adds tick-13 `acknowledgment-aru-records` (actor `aru`, place
`chalk-stair`, `depends_on: ["response-evin-salt-court"]`) → 6 events; `sources.json` adds `aru-acknowledgment-note` → 6
sources; `fictional-excerpts.md` appends the acknowledgment section (map span 44-53).

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
# INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
# RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
# SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19 / RESULT PASS   exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
# OBLIGATIONS raw=17 mapped=17; INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19 / RESULT PASS   exit 0
```

Map declares `17 JSON facts; 2 editorial rows; 19 total mapped rows; 15 distinct excerpt anchors`; new row J17 is
`timeline.json#/5` at `fictional-excerpts.md` span 44-53 (`Tick 13: I received Evin's response at the Chalk Stair.`).
R5's README states 5 entities / 1 relation / 6 events / 6 sources and 17 obligations.
Mid-write state observed at 18:45 (recorded for transparency, resolved): `raw=17 mapped=16` + `FINDING missing_obligation:
timeline.json#/5 has no map row`, exit 1, while the map was still the r96 16-row copy.

### 2.4 r96 cosmetic repair (R4) — receipt-neutrality

`git diff` is exactly 2 lines: the editorial delimiter row `|---|---|---|---|---|---:|---|---|` → `|---|---|---|---|---:|---|---|`
(8→7 cells) and `The new relation encodes only the agreement…` → `The new tick-12 event encodes only Evin's second
account…`. Data rows untouched. Receipts unchanged:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response   # RECEIPT JSON-FACTS 16; TOTAL-ROWS 18 / RESULT PASS exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response # raw=16 mapped=16 / RESULT PASS exit 0
```

R1's report independently confirms the r96 tool output is byte-identical to the r96-era capture; R4's report confirms the
re-freeze was a pin-format/guard refresh, not a digest change forced by the repair.

### 2.5 Census (method validated; stable for the delivered revision)

```sh
bash .ufo/waves/round-97/seats/V26-scratch/census.sh
# CENSUS dirs=171 clean=37 negative=134 other=0 violation_lines=421
```
Exactly the expected r97 numbers (170→171 dirs, 36→37 clean, 134 negative, 421 lines, zero non-0/1 exits). `check_bible`
does not read the R5-written markdown, so the census is unchanged by the final doc writes. R6's note independently
records `ls -d corpus/fixtures/*/ | wc -l` = 171.

### 2.6 C9 watch receipts (measured 18:46)

```sh
sha256sum corpus/fixtures/check_bible.py   # ff9fd2aa…d1421 (pin fresh)
python3 corpus/tools/discriminate_check.py                    # RESULT: DISCRIMINATION HELD   exit 0
python3 corpus/tools/discriminate_check.py --checker e97613c  # REGRESSION-DETECTED (expected control)   exit 2
```

## 3. Doc inventory — required integration-time updates

### 3.1 `corpus/fixtures/README.md` — append Round-97 section after line 1219

1. `## Round 97 — r97-crossing-acknowledgment (2026-10-17)`: third beat of the crossing arc — Aru's acknowledgment note
   (`aru-acknowledgment-note`) + tick-13 event (`acknowledgment-aru-records`, actor `aru`, place `chalk-stair`,
   `depends_on: ["response-evin-salt-court"]`); records receipt only, dispute preserved unresolved; 5/1/5→5/1/6, sources
   5→6, 17 map obligations (16 inherited rows unchanged + 1 new event row); inherited records parsed-value identical.
2. Replay commands + receipts measured at closure (numbers above): `check_bible` CLEAN exit 0; `support_check` 17/17 and
   19/19 exit 0; `map_obligations` `raw=17 mapped=17` PASS exit 0.
3. Note the r96 cosmetic repair and the re-freeze through the guarded `--freeze` path; r96's
   `support_check`/`map_obligations` receipts are unchanged (measured).
4. `### 2026-10-17 census re-declaration`: 171 dirs / 37 clean / 134 negative / 421 violation lines / zero non-0/1 exits,
   superseding Round-96 (170/36/134/421); one directory added; zero inherited tuples changed.
5. `Dated pin note:` — this append changes the file's bytes; the W05 pin no longer matches (fourth consecutive round).

### 3.2 `corpus/README.md` — three bullets

- Line 37: "`tools/map_obligations.py` (rounds 94–96) — … `--self-test` (24 persisted cases)" → rounds 94–97, **25
  persisted cases**; may note the loader is strict (any pinned case missing fails closed) and `dual_pointer` is pinned.
- Line 38: "`tools/dependency_freeze.py` (round 96) — … 14-case persisted self-test" → **16-case** + guard/path-binding:
  `--freeze` restricted to `corpus/fixtures/**` (`SCOPE-REFUSED` exit 2, including the scope dir itself); pins record the
  repo-relative path and verify enforces it (foreign same-named copy → `PATH-MISMATCH` exit 2); `DIGEST-MISMATCH` names
  the changed file(s).
- Insert a new r97 fixture bullet after line 23 (r96 bullet), e.g.: "`fixtures/r97-crossing-acknowledgment/README.md` —
  third beat of the crossing arc: Aru's acknowledgment note records receipt of Evin's response; dispute preserved
  unresolved (tick-13 event depending on the tick-12 response). Navigate `claim-excerpt-map.md` (17 obligations) and
  `fictional-excerpts.md`."
- R6's `r97-acknowledgment-scope-note.md` is not required here: this section lists no r95/r96 scope notes either.

### 3.3 `SKILL.md` — both gate-registry rows

- `map_obligations` (83–90): line 87 "24 cases" → **25 cases**, and the two "r97 debt" notes (unpinned `dual_pointer`;
  droppable pins) → closed state (loader fails closed on any missing pinned case; `dual_pointer` pinned as case 25).
  Line 89: coverage "(r93–r96 clusters)" → include r97; "Bounded residuals: … round-95/96 r97-debt items" → update
  (only round-94 BR-16 / BR-05 scratch residual remains per the tools README addendum). Line 86 already lists
  `dual_pointer` — no change.
- `dependency_freeze` (92–101): line 96 entry command — frozen chain stays the four fixtures; may note the `--freeze`
  scope guard. Line 98 "14 cases" → **16 cases** (added `scope_refused`, `path_mismatch`). Line 97 `code → class` —
  exit-2 surface should name `SCOPE-REFUSED` and `PATH-MISMATCH` alongside the existing exit-1 classes. Line 100 scope —
  drop "Not path-bound (a same-named copy verifies identically)", "(no scope guard — r97 debt)", "`DIGEST-MISMATCH` does
  not name the changed file"; replace with the guarded/path-bound/naming facts; optionally note the two extra
  fail-closed behaviors from R3's report (same-named in-scope `--freeze` refusal; freeze propagates the verify exit).
- The "Error signatures and response" section has no rows for these two gates — nothing to update there.

### 3.4 `corpus/knowledge/r91-c9-watch.md` — r97 (sixth) re-check row due

Line 287's r96 row ends "Next re-check: r97". Required append (pattern of r95/r96 sections): sixth re-check, dated,
checker pin reproduced (`ff9fd2aa…d1421`, measured fresh), discriminator pair receipts (exit 0 `DISCRIMINATION HELD`;
exit 2 control `REGRESSION-DETECTED`), gate 3 remains not met, table row, "Next re-check: r98".

### 3.5 `corpus/tools/README.md` — C2 half of the Round-97 addendum still missing

The landed Round-97 addendum (lines 177–225) covers only C1 (`dual_pointer` pinned, loader tightened, 25 cases). The
dependency_freeze C2 half (scope guard, path binding, `DIGEST-MISMATCH` naming, 16 cases, re-frozen pins, the two extra
fail-closed behaviors) is **not yet written** — file last modified 18:47:13, before R3's final tool/contract writes
(18:53/18:55); `grep` finds no Round-97 dependency_freeze section. This is the one producer-owned doc gap observed; it is
integration/closure work (R2 owns the file; R3 owns the tool).

## 4. Stale-wording list (exact file:line → required change; status at this write)

| # | Location | Current wording (abridged) | Required | Status |
|---|---|---|---|---|
| 1 | `corpus/fixtures/README.md:1213` | "Known cosmetic debts (no gate reads them; r97 candidates): … one extra cell … 'new relation' …" | Resolved by R4's repair; dated Round-97 note (append-only) | Open (integration) |
| 2 | `corpus/fixtures/README.md:1217` | census "170 fixture directories: 36 clean" | Superseded by 171/37 (append) | Open (integration) |
| 3 | `corpus/fixtures/README.md:1219` | pin note "third consecutive round" | Fourth consecutive round (append) | Open (integration) |
| 4 | `corpus/tools/README.md:173` | "Residuals (r97 debt): … droppable … `dual_pointer` has no persisted self-test case" | Superseded by Round-97 addendum | Closed by R2 (addendum landed) |
| 5 | `corpus/tools/README.md:175` | "Hazards (r97 debt): `--freeze` … no scope guard … not path-bound … `DIGEST-MISMATCH` does not name the changed file" | Superseded by Round-97 addendum C2 half | Open (addendum C2 half missing, §3.5) |
| 6 | `SKILL.md:87` | "24 cases … `dual_pointer` … not pinned … 23/24 still passes — both r97 debt" | 25 cases; debts closed | Open (integration) |
| 7 | `SKILL.md:89` | "(r93–r96 clusters)"; "round-95/96 r97-debt items" | Include r97; residual list updated | Open (integration) |
| 8 | `SKILL.md:100` | "Not path-bound … (no scope guard — r97 debt) … `DIGEST-MISMATCH` does not name the changed file" | Guarded/path-bound/naming facts | Open (integration) |
| 9 | `corpus/README.md:37` | "(rounds 94–96) … 24 persisted cases" | "(rounds 94–97) … 25 persisted cases" | Open (integration) |
| 10 | `corpus/README.md:38` | "(round 96) … 14-case persisted self-test" | 16-case + guard/path-binding | Open (integration) |
| 11 | `corpus/knowledge/r91-c9-watch.md:287` | "Next re-check: r97" | r97 row due; append "Next re-check: r98" | Open (integration) |
| 12 | `corpus/fixtures/README.md:1209-1210` | r96 freeze receipt `FREEZE r96-crossing-response: events 5/5 …` | Receipt's first line is unchanged; a replay on the delivered tool also prints a `DIGEST <sha256>` line | Confirmed — add a dated note if desired |
| 13 | `SCORECARD.md` r96 section (≈478–480) | r97-debt bounds listed | Historical; r97 closure adds its own section | No rewrite needed |

## 5. Environment and state notes

- `/tmp` inode exhaustion during the wave (`IFree 0`, `IUse% 100`) crashed one baseline self-test run; workaround
  `TMPDIR` off `/tmp`. R3's final tool no longer uses `/tmp` for its self-test scratch (creates under `ROOT`).
- Mid-write states observed and resolved (recorded as states, not failures): R1 tool vs 24-case contract → exit 2 by
  design (18:45); r97 map 16/17 → exit 1 (18:45–18:48); R3 tool vs 14-case contract → `CONTRACT-INVALID`
  `missing=['path_mismatch','scope_refused']` (18:52–18:53); R3 second pass (18:53/18:55) re-measured here.
- This seat wrote only its report and `.ufo/waves/round-97/seats/V26-scratch/` (poll script, census script, self-test
  logs, two foreign fixture copies for the PATH-MISMATCH probe). No writes under `corpus/`, no commits, no network.
- Scope: this seat did not adjudicate C1/C2/C3 admission or verify claim semantics — it measured doc-relevant receipts
  and enumerated doc deltas. C-claim verdicts belong to the other verifier seats and the integrator.

## 6. Bottom line

**PASS** — pre-integration doc inventory complete and fully measured on the delivered revision (C1 25/25, C2 16/16 +
guard/path-binding probes + chain 4/4, C3 17/17 receipts, census 171/37/134/421, C9 pin fresh and discrimination held);
all producer artifacts and all six reports present; the enumerated doc updates (§3.1–3.4, §4) remain for integration,
with one producer-owned gap recorded — the `corpus/tools/README.md` Round-97 dependency_freeze (C2) half is not yet written.
