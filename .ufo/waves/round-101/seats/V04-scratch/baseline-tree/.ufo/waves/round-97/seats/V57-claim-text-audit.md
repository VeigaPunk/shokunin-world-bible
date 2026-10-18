# V57 — claim-text-audit (round 97)

- **Seat:** V57 `claim-text-audit` (verifier). **Mandate:** read the r97 LOG declaration
  (`LOG.md`, section `## Round 97 — declaration before dispatch`, extracted copy sha256
  `40ee65e3476c993c128f3a181a93cf41c879cdc235fd96b82f491eccc62fd565`, LOG mtime 18:39:59,
  unchanged through the round) against delivered reality; flag overclaims / denominator slips
  for append-only correction.
- **Lane:** `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9` (HEAD `2393934`).
  Every command ran from the lane repo root with `python3`; every output below is observed,
  not projected. Scratch and all probe outputs: `.ufo/waves/round-97/seats/V57-scratch/`.
- **Method:** poll-wait (20 s cadence, 40 tries) for the r97 fixture + all six producer reports,
  then independent re-derivation of every checkable declaration clause on the frozen delivered
  revision. No producer-owned byte was written by this seat.

## 0. Poll-wait record

`V57-scratch/poll.sh` → `poll.log`:

```
2026-10-17T18:44:31-03:00 try=1 fixture=yes producer_reports=0
2026-10-17T18:44:51-03:00 try=2 fixture=yes producer_reports=0
...
2026-10-17T18:56:11-03:00 try=36 fixture=yes producer_reports=5
2026-10-17T18:56:31-03:00 try=37 fixture=yes producer_reports=6
ALL PRESENT
```

All six producer reports present: `R1-map-pinning.md`, `R2-contract-docs.md`,
`R3-freeze-hardening.md`, `R4-fixture-author.md`, `R5-fixture-docs.md`, `R6-knowledge-note.md`.
Nothing was verified against a plan or an unreported revision; the r96 control runs used frozen
`git show f3e09f9:` bytes.

## 1. Frozen delivered revisions audited (sha256)

| Artifact | sha256 |
|---|---|
| `corpus/tools/map_obligations.py` | `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9` |
| `corpus/tools/map-obligations-contract.json` | `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41` |
| `corpus/tools/dependency_freeze.py` | `b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130` |
| `corpus/tools/dependency-freeze-contract.json` | `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781` |
| `corpus/tools/README.md` | `6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992` |
| `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` | `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de` |
| `corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md` | `49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f` |
| `corpus/fixtures/r97-crossing-acknowledgment/README.md` | `d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f` |
| `corpus/knowledge/r97-acknowledgment-scope-note.md` | `5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5` |

Final `git status --short` (excluding `.ufo/`): exactly the declared surface — `M LOG.md`,
`M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`, `M corpus/tools/README.md`,
`M corpus/tools/dependency-freeze-contract.json`, `M corpus/tools/dependency_freeze.py`,
`M corpus/tools/map-obligations-contract.json`, `M corpus/tools/map_obligations.py`,
`?? corpus/fixtures/r97-crossing-acknowledgment/`,
`?? corpus/knowledge/r97-acknowledgment-scope-note.md`. No stray write.

## 2. Claim-by-claim audit

### C1 — calibration (4/4 clauses confirmed)

**(a) "persisted self-test case pinning `dual_pointer` (contract 24→25)"** — confirmed.
Baseline (committed tool + committed contract, scratch copies): `SELF-TEST CASES 24/24 pinned` /
`RESULT PASS`, exit 0. Delivered: `SELF-TEST CASES 25/25 pinned`, contract `self_test.cases`
length 25 with `{"id": "dual_pointer", "exit": 1, "finding_ids": ["dual_pointer"]}`, and
`SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']`; `RESULT PASS`, exit 0.

**(b) "loader tightened … today 23/24 still passes: dropping either r96-added pin stays green"** —
confirmed both directions. Baseline reproductions (scratch contract copy, one case dropped,
baseline tool): dropping `schema_drift` → `SELF-TEST CASES 23/24 pinned` / `RESULT PASS`,
exit 0; dropping `inventory_mismatch` → `SELF-TEST CASES 23/24 pinned` / `RESULT PASS`, exit 0.
Delivered (scratch copy of the delivered pair): dropping `dual_pointer`, `complete` (core), or
`inventory_mismatch` each prints
`FINDING self_test_contract: contract drops implemented self-test cases: <id>` / `RESULT ERROR`,
exit 2 — the loader now compares against the full implemented set
(`missing = sorted(set(SELF_TEST_CASES) - set(expected))`, delivered line 820).

**(c) "neutralizing the dual_pointer emission fails the self-test"** — confirmed. Scratch copy of
the delivered tool with the emission guard patched (`if mention is not None:` → `if False:`),
unmodified 25-case contract:

```
SELF-TEST CASES 25/25 pinned
SELF-TEST FAIL dual_pointer exit=0 findings=none
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR        exit=2
```

**(d) non-regression** — confirmed on the delivered revision: r88 10/10, r93 12/12, r94 14/14,
r95 15/15, r96 16/16, r97 17/17 all `RESULT PASS` exit 0; frozen r93 replay
(`--frozen .ufo/waves/round-94/frozen/map-obligations-r93`) `RESULT PASS` exit 0; r87/r89 exit 2
`unsupported_map`; `--help` exit 0 with no `RESULT` line; `--self-test extra` →
`FINDING invalid_arguments` exit 2 (0/1/2 contract unchanged).

### C2 — coverage (4/4 clauses + re-freeze confirmed)

**(a) "`--freeze` accepts only `corpus/fixtures/**` targets"** — confirmed. Delivered tool,
foreign target: `FINDING SCOPE-REFUSED: --freeze refuses <path> …; the frozen scope is
corpus/fixtures/** (integration-time operation only)` / `RESULT ERROR`, exit 2; in-scope scratch
target (mirror root `probe-r3`, fixture under its `corpus/fixtures/`): `FROZEN …` / `RESULT PASS`,
exit 0. Contract self-test case `scope_refused` persisted.

**(b) "a byte-identical same-named copy at a foreign path exits 2 PATH-MISMATCH (today it verifies
identically)"** — confirmed both directions. Delivered tool on the foreign copy of
`r96-crossing-response`: `FINDING PATH-MISMATCH: pin r96-crossing-response names
corpus/fixtures/r96-crossing-response (resolves to …); invoked fixture resolves to …` /
`RESULT ERROR`, exit 2 (reproduced on the real repo copy and on the scratch mirror). Baseline
tool on the same byte-identical copy: `FREEZE r96-crossing-response: events 5/5;
dependency-edges 4/4; relations 1/1` / `DIGEST d422a9b3…` / `RESULT PASS`, exit 0 — the "today"
clause reproduced exactly.

**(c) "`DIGEST-MISMATCH` names the changed file"** — confirmed. Scratch pinned copy with one
appended space in `timeline.json[3].description`:

```
FINDING DIGEST-MISMATCH: content digest eeb1c595… != pin d422a9b3…; changed: timeline.json
(sha256 ea0225f9… -> a737a3d1…); fixture bytes changed outside the frozen inventory
RESULT ERROR        exit=2
```

**(d) "self-test grows 14→16 cases pinning the new classes"** — confirmed. Baseline (committed
tool): `SELF-TEST 14/14` / `RESULT PASS`. Delivered: `SELF-TEST 16/16` / `RESULT PASS`, exit 0;
contract `self_test.expected` ids = 16, including `scope_refused` and `path_mismatch`.

**"the r96 fixture is re-frozen THROUGH the guarded `--freeze` path (pin refresh) … chain verifies
4/4 clean at closure"** — confirmed. Before refresh the contract top-level revision and the r96
pin revision were `60dba0c2aa344860b10a2fc63e00468d1b134f27`; after the refresh both are
`2393934237ea076366f3db6dceeff033edb52ab1` (HEAD), the r96 pin digest is unchanged
(`d422a9b3…` — `claim-excerpt-map.md` is not one of the five pinned data files, so the repair is
digest-neutral), the other three pins keep revision `60dba0c2…`, and all four chain fixtures
verify `RESULT PASS` exit 0 after the refresh (4/4).

### C3 — depth (9/9 clauses confirmed, repair half included)

- **"Before: 5/1/5, 5 sources at r96"** — confirmed: r96 `entities.json` 5 / `relations.json` 1 /
  `timeline.json` 5 / `sources.json` 5 (`contradictions.json` 0).
- **"After: 5/1/6, 6 sources"** — confirmed: r97 5 / 1 / 6 / 6 / 0.
- **"one authored acknowledgment note (`aru-acknowledgment-note`)"** — confirmed in
  `sources.json` (6th entry) and the appended `fictional-excerpts.md` section (lines 44–53;
  quoted lines 48–51; the file is a pure byte-prefix of r96's plus 822 appended bytes).
- **"one tick-13 event (`acknowledgment-aru-records`, actor `aru`, place `chalk-stair`,
  `depends_on: ["response-evin-salt-court"]`)"** — confirmed verbatim, `source_id`
  `aru-acknowledgment-note`.
- **"17 map obligations (16 inherited rows unchanged + 1 new event row)"** — confirmed:
  `OBLIGATIONS raw=17 mapped=17`; `INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS
  19/19`; `support_check` `SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19;
  VALIDATED-ROWS 19/19`, `DISTINCT-ANCHORS 15/15`; both exit 0. Row-level parser diff r96→r97:
  J01–J16 each differ in exactly one cell (index 3, the path-qualification namespace column);
  pointer / source-ID / excerpt path / span / mode / anchor cells are identical; J17 is the only
  added row (`timeline.json#/5`).
- **"no new claims/entities/relations"** — confirmed: `entities.json` (`026af0bc…`),
  `relations.json` (`c279254b…`), `contradictions.json` (`37517e5f…`) are byte-identical to r96;
  claims total 5.
- **"`check_bible` CLEAN"** — confirmed: `CLEAN: schema, citations, relations, timeline;
  0 violations`, exit 0.
- **"inherited rows parsed-value identical"** — confirmed (see the row diff above).
- **"census 170→171"** — confirmed: `find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l`
  → 170 at baseline, 171 on the delivered revision.
- **repair half: "fix the two r96-carried cosmetic map blemishes (8-cell delimiter row; the stale
  'new relation' sentence) … pointers/anchors/spans/modes untouched … r96's support_check and
  map_obligations receipts must be unchanged"** — confirmed. `git diff f3e09f9 --
  corpus/fixtures/r96-crossing-response/` → only `claim-excerpt-map.md`, `2 insertions(+),
  2 deletions(-)`: line 44 delimiter 8→7 cells (`|---|---|---|---|---|---:|---|---|` →
  `|---|---|---|---|---:|---|---|`), line 50 sentence replaced with tick-12 event wording; map sha256
  `5093d72e…` → `e851f068…`. Receipts captured before the repair landed (18:43) and re-run after:
  `support_check` `SOURCE-SUPPORT 16/16; … VALIDATED-ROWS 18/18` / `RESULT PASS` and
  `map_obligations` `raw=16 mapped=16` / `RESULT PASS`, identical on both sides.

## 3. Discrepancies / denominator slips for append-only correction

1. **Doc-parity gap, freshness (no LOG falsehood).** The delivered `corpus/tools/README.md:175`
   still says `dependency_freeze.py` self-test "14/14" and lists the three r96 hazards as open
   r97 debt ("`--freeze <dir>` … has no `corpus/fixtures/` scope guard"; "receipts are not
   path-bound"; "`DIGEST-MISMATCH` does not name the changed file") — all three are closed in the
   delivered tool, and the Round-97 addendum (`README.md:177`) covers only `map_obligations`.
   R2's report never mentions `dependency_freeze`; R3 records the same gap. **Suggested
   append-only correction:** a Round-97 addendum paragraph for `dependency_freeze` in the tools
   README (or a closure-side errata line) so the delivered documentation does not contradict the
   delivered tool. The LOG declaration itself does not claim README parity, so this is a
   freshness/doc gap, not an overclaim of the audited text.
2. **R3's "digest changes by the repair" discrepancy is not a LOG-text issue.** R3
   (`R3-freeze-hardening.md`, "Pin refresh …") records that a parenthetical claiming the digest
   moves with the repair is inaccurate. That parenthetical does **not** appear in the LOG
   declaration (LOG: "re-frozen THROUGH the guarded `--freeze` path (pin refresh)"), so no LOG
   correction is needed; recorded here so the item is not double-counted by the adjudicator.
3. **Minor wording note (no correction required).** C2(b)'s "pins record the fixture's
   repo-relative path and verify compares the invoked path" reads as if both halves were new; the
   baseline pins already carried `"fixture": "corpus/fixtures/…"`. The r97-new work is the
   read-validation of that field plus the verify-time comparison. The delivered outcome matches
   the sentence.
4. **Denominator watch — no slip found.** "16 inherited rows unchanged" is exact in the
   parsed-value sense (namespace column excepted), and the declaration itself supplies the
   qualifier ("inherited rows parsed-value identical"); the r97 map text and R5's report both
   state the namespace-column qualification explicitly. All other counts in the declaration
   (24→25, 23/24, 14→16, 5/1/5→5/1/6, 5→6 sources, 17 obligations, 170→171, 4/4 chain) match
   measured values.

## 4. Observations (not declaration claims; for the record)

- **r97 is not pinned in the freeze chain:** `dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment`
  → `FINDING UNPINNED-FIXTURE …` / `RESULT ERROR`, exit 2. The declaration claims chain 4/4 only,
  so this is consistent; R3 lists pinning r97 as an r98 candidate.
- **`corpus/fixtures/README.md` is closure-side stale:** its last census re-declaration is r96
  (170 dirs) and `:1213` still lists the r96 cosmetic debts as "r97 candidates" (now repaired).
  Neither is part of the LOG declaration's claims; closure should update them.
- **Host condition:** `/tmp` inode exhaustion (`IUse% 100`, 1048576/1048576 inodes; ~8.5 GB
  free) — same class as the r96 host note. All V57 outputs were rerouted to lane scratch;
  R3 records the same condition.
- **Self-disclosure (process):** while staging a baseline probe layout I briefly created
  `.ufo/waves/round-97/seats/corpus/` — outside my declared scratch. It was removed within the
  same minute and the probe re-rooted under `V57-scratch/`; no producer-owned path was touched
  and the final `git status` shows only declared paths.
- Cross-checks (not relied on): V14 (inherited equality) and V19 (r96 repair scope) reach the
  same byte/parse-level conclusions on the same artifacts.

## 5. Bottom line

**PASS** — every checkable clause of the r97 LOG declaration verified independently on the
frozen delivered revision (C1 4/4, C2 4/4 + guarded re-freeze, C3 9/9 including the repair
half); no LOG overclaim or denominator slip found; the one actionable item is a doc-parity
correction for `corpus/tools/README.md:175` (stale `dependency_freeze` paragraph), and R3's
flagged "digest changes" parenthetical is not present in the LOG text.
