# V23 — verdict-adjacency (round 101)

Seat: V23, leaf verifier in the 28-seat single wave. **One axis verdict: adjacency unchanged / not harmed (PASS, bounded).** Depth, coverage, calibration, operability, and freshness are named as non-regression witnesses, not independently scored or averaged here. This is not a round-admission, promotion, testimony-truth, rights, or canon verdict.

Subject: delivered uncommitted wave bytes against r100 closure `6f86bf2` (r99 closure freeze commit; r100 closure `a04f986` and the r101 declaration `ebec6bb` sit between baseline and HEAD and are committed, not wave writes). Battery commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Only V23 wrote this report and `.ufo/waves/round-101/seats/V23-scratch/` (manifest: `V23-scratch/file-manifest.json`, 1,138 files / 26,542,984 bytes before the manifest itself — the bulk is byte-identity mirror trees). No production file, other seat's scratch, commit, push, or network operation was written/performed by this seat. No nested agent.

## Producer gate, poll protocol, and two recorded bounded stall-escapes

Poll #1 (`V23-scratch/poll.py`, checks 1–40, 20 s apart, 00:05:16–00:18:47 -03:00) terminated on the 40-check deadline at **artifacts 3/6, producer reports 0/2** — but the wave was demonstrably live: U1's `dependency_freeze.py`/contract bytes landed mid-poll (first in `poll.jsonl` between checks ~18–20; contract pin present), and sibling seat scratch dirs kept appearing. Per the ENDGAME CONVENTION I took **escape #1**, a recorded extension (`poll2.py`, checks 41–60, 00:19:07–00:29:14): artifacts reached **6/6 at check 42 (00:23:34)** and `U1-chain-eight.md` appeared at 00:21:40, but U2's report was still absent at check 60. I took **escape #2**, a final probe (`poll3.py`, checks 61–70). Disclosure: my first poll3 launch was defective — a sed derivation left the sleep bound `if i < 60:` unmatched for range 61–70, so it burned all ten checks in 0.1 s at 00:29:02 with no waiting and terminated; I fixed the bound (`if i < 70:`) and reran; the defective run's log file (`poll-extension2.jsonl`) was overwritten by the corrected rerun, so the burned run survives only as this description. The corrected probe observed **READY at check 69 (00:32:17): artifacts 6/6, producer reports 2/2** (`U2-r10-register.md`, mtime 00:32:16); the loop took the READY branch there (checks 61–68 recorded 1/2 reports), exited 0, and wrote `ready-manifest.json`. No battery was run on any earlier incomplete state.

Readiness conditions were: `SKILL.md`, contract, tools README, `dependency_freeze.py` changed vs `6f86bf2`; contract contains the `r100-docket-review` pin; `corpus/knowledge/r101-r10-register-first-entry.md` exists nonempty; nonempty `U1-*.md` and `U2-*.md` in the seats dir.

## 1. Charter and byte-ownership boundary

Charter files byte-identical to their pre-wave (== baseline) SHA-256, captured at 00:05 before any producer byte landed:

```text
PROVINCE.md      94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
SHONEN.md        03b832c75efbf81300e87f6a95713a48b21b00d654c1222aee251a27c103d7d1
README.md        ad4adb1e6cfbec41c83281aa7dfe1439d453ab5cb4290a9d8c25c1a1b06c2caf
l0-questions.md  93105c95247bb80e6f2c4df0fca7f8cc31b271ca3f1777aa69302a9ea8d0cfdf
```

Actual `git diff --numstat 6f86bf2` (whole tree):

```text
46   0  LOG.md
35   0  SCORECARD.md
 4   3  SKILL.md
59   0  corpus/tools/README.md
142  1  corpus/tools/dependency-freeze-contract.json
18   0  corpus/tools/dependency_freeze.py
```

Attribution is exact. Worktree changes vs HEAD are **only** the four U1-owned files (`git diff --name-only HEAD`); the only untracked non-`.ufo`/non-`.scratch` path is U2's one knowledge file; `git diff --name-only HEAD -- LOG.md SCORECARD.md` is empty, so LOG +46 / SCORECARD +35 are the committed r100-closure and declaration bookkeeping, not wave writes. `git diff --check` is clean. Diffs per producer (saved under `V23-scratch/diff-*.patch`):

- **U1** — contract: exactly three changes, the new `r100-docket-review` pin (fixture path, revision `ebec6bb…`, `payload_schema_version` 2, ten per-file digests, `content_sha256 77debadf…`, events 9 / edges 8 / relations 1, tick-16 edge `clerk-review-first-passage` → `clerk-lapse-recorded`), the new `self_test.expected.repointed_edge` case, and the writer-managed top-level `revision` refresh `b5fe472…` → `ebec6bb…` (disclosed since r100). Parsed comparison: `pins_added=['r100-docket-review']`, `pins_removed=[]`, `prior_pins_changed=[]`. Tool: exactly three hunks — a dated docstring paragraph, `"repointed_edge"` appended to `FROZEN_CASES`, and the case body (mirror of `r95-crossing-aftermath`; `aftermath-missing-evin`'s `depends_on` entry `paired-crossing-decision` replaced by valid earlier `aru-ninth-bell`, tick 9 < 11; expected exit 1). SKILL.md: the freeze-row `entry command` line gains `r100-docket-review`; `self-test command` becomes 19 cases with `r101 added repointed_edge`; `pinned-values path` becomes "exactly the eight chain fixtures, verifying 8/8 clean … The seven inherited pins retain every field from r100 closure `6f86bf2`"; one new dated supersession bullet (2026-10-18, round 101); the r100 bullet kept as history. Tools README +59: append-only Round-101 addendum; the prior text is a byte prefix.
- **U2** — the new knowledge record only (20,823 bytes, 122 lines).

`corpus/knowledge/r99-gate-blind-spot-table.md` and the r88 decision table are **not edited** — confirmed by the numstat (absent) and by U1's explicit disclosure that C3's "dated row update" is delivered as documentation-of-record in the README addendum and SKILL supersession bullet, not as a table edit.

## 2. Parent/sibling boundary

Actual command, exit 0:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-101/seats/V23-scratch/outside.py
```

Metadata sweep at 00:41 over 194,025 regular files outside the lore lane (excluding `.git`, dependency/build dirs, sensitive names) since the declaration instant 2026-10-17T23:59:55-03:00:

```text
parent_git_status: ""
parent_round101_wave_exists: false
recent_counts_by_top: {"kotodama-shokunin": 10}
leak_hits: []
round101_strays_outside_lane: []
```

The 10 recent Kotodama paths are its own concurrent activity; the bounded content-leak grep (`r101-r10-register-first-entry` strings) found nothing outside the lane. No lore-attributable parent or sibling write was found. This is fleet-root metadata plus a bounded search, not a machine-wide forensic guarantee.

## 3. Fiction/external-source separation and refusal scan

The scan input `round-new-bytes.txt` (diff bytes of the four changed producer files + full bytes of the new knowledge record) contains **zero** matches for mechanics vocabulary (`mechanics?|gameplay|ruleset|damage|stats|balancing|combat|dice|hit-points`), zero for rights grants (`public domain|fair use|permission is granted|licensed under|all rights reserved`), and zero external URLs or foreign `/home/` paths. Seven `canon` mentions, all inspected: every one is a refusal or bound ("no semantics, chronology-truth, or canon claim is added"; "not a canon assertion"; "settles nothing about canon and grants no permission"), none a canon certification.

The C2 record keeps the R10 boundary: the live register `corpus/knowledge/cross-cluster-contradictions.md` is absent now **and** absent from the baseline tree (`git ls-tree 6f86bf2` contains no such path); no `contradictions.json` pair is added (both compared clusters parse `[]`); no `unresolved` status is used; both claims are preserved byte-exact (independently re-measured, §4). The charter's refusals (canon-without-citation, silent contradiction resolution, rights claims, game mechanics) hold on the delivered bytes.

## 4. Full running battery and negative boundaries

Actual battery command (exit 0; 212 recorded invocations; complete argv/stdout/stderr/exit in `battery-results.json` and `battery-transcript.txt`, summary in `battery-summary.json`):

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-101/seats/V23-scratch/battery.py
```

Disclosure: the first battery launch crashed in 0.04 s on an internal argument-passing bug in my harness (`sh()` signature), recorded nothing, and was fixed before the recorded run; the recorded run is the one above.

Representative observed results:

```text
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review
FREEZE r100-docket-review: events 9/9; dependency-edges 8/8; relations 1/1
DIGEST 77debadf5c0f6e2c27f18902f0710278eb4305c633ff73158df7082936325c19
RESULT PASS        exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
OBLIGATIONS raw=22 mapped=22        exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
SOURCE-SUPPORT 22/22; ... exit=0
```

- **Frozen chain 8/8**: every pin verifies `RESULT PASS` exit 0 — r88-m3 2/2, r94 3/3·2/2·1/1, r95 4/4, r96 5/5, r97 6/6, r98 7/7, r99 8/8·7/7 (digest `7fe7e3b0…`, the inherited r100 value — none re-frozen), r100 9/9·8/8 (`77debadf…`, matching U1's receipt). r87-myth-cluster live verify returns `UNPINNED-FIXTURE`/2 as expected.
- **Census**: `check_bible` over all 174 fixture directories → **40 clean, 134 intentional negatives, 421 VIOLATION lines, no other exits or stderr** — the inherited r100 census is preserved exactly; r101 adds no fixture.
- **Self-tests on byte-identical mirrors** (tool and contract SHA-256 equality with live bytes explicitly checked, both true): freeze `--self-test` → `SELF-TEST 19/19`, `RESULT PASS`, exit 0, including `CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok`; map `--self-test` exit 0 with 25 per-case `SELF-TEST PASS` lines; `boundary_doc_check.py` exit 0 and `--self-test` exit 0 (9 case-PASS lines; TMPDIR pointed at V23 scratch).
- **Live gates on r94 and r99** (the C2 referent fixture and the newest inherited pin): bible/map/support all exit 0.
- **Regression and replay controls**: `discriminate_check.py` → `DISCRIMINATION HELD` exit 0; `--checker e97613c` → expected `REGRESSION-DETECTED` exit 2; `map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93` → exit 0.
- **Negative/boundary controls** (repo-structured mirrors in scratch, since `bind_path` pins each fixture to the tool-derived ROOT):
  - clean r99 mirror verify → PASS/0;
  - **row-2 class demonstrated live on the delivered gate**: repointing `clerk-lapse-recorded` from `clerk-filing-open` to the valid earlier `acknowledgment-aru-records` → `RESULT FAIL` exit 1 with exactly `ADDITION-DETECTED` and `REDUCTION-DETECTED` in one run, while `check_bible` on the same mutated copy stays `CLEAN` exit 0 — the checker blind spot and the freeze gate's detection both re-confirmed (C3's persisted case is the same class);
  - newline appended to a pinned excerpt → `DIGEST-MISMATCH` exit 2 naming `fictional-excerpts.md` with both sha256 values;
  - fixture + `--freeze` combined → `INVALID-ARGUMENTS` exit 2; `--freeze` on a scratch dir → `SCOPE-REFUSED` exit 2 with the contract SHA-256 unchanged afterwards; foreign same-named copy → `PATH-MISMATCH` exit 2.

**C2 independent spot-checks** (all observed, not accepted on author assertion): `relations.json` is one byte string across all seven arc snapshots — single tuple in the identity set, sha256 `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9`, 139 bytes each; `r95 timeline.json#/3` parses to exactly `aftermath-missing-evin` (tick 11, aru, chalk-stair, `["paired-crossing-decision"]`, `aru-aftermath-note`) and `r96 timeline.json#/4` to exactly `response-evin-salt-court` (tick 12, evin, salt-court, `["aftermath-missing-evin"]`, `evin-response-note`); excerpt prefix chain r94⊂r95⊂r96 both `True`; all five quoted in-world lines present verbatim at their cited fixtures; both `contradictions.json` parse `[]`.

## 5. Ordering, corrections, and limits

Per-producer artifact-before-report ordering holds: U1's artifacts span 00:07:59–00:20:30 with its report at 00:21:40; U2's entry (final mtime 00:31:08) precedes its report at 00:32:16. My battery's aggregate `max(artifacts) <= min(reports)` check printed false only because U2's artifact postdates U1's report across producers — the coarse predicate was mine, the per-producer invariant holds.

One interim-state observation, resolved in U2's favor and recorded because I saw both bytes: at ~00:24 I read the entry citing `corpus/fixtures/r96-crossing-response/README.md:11` for "records only Evin's second account of the same occasion", but the phrase is at `:9`. The delivered entry (final bytes, 20,823 bytes) cites `:9`, verified against `README.md:9`, and its Checker-limits bound attributes `:26` clauses correctly and quotes `:110`'s actual clause — exactly the two corrections U2's report discloses as fixed during its citation self-check. No pointer variance remains open in the delivered bytes.

Limits: gates establish their declared structural, lexical, mapping, inventory, byte, and regression properties only; a per-cluster `CLEAN` is not cross-cluster evidence; the C2 compatibility finding is a relation between authored accounts, not a world fact. Outside-write evidence is bounded to the stated fleet-root sweep. r101 claims C1 (8/8 chain) and C3 (19/19 self-test, row-2 class persisted) verified above; C2's byte receipts verified, its semantic reading witnessed as consistent and bounded. SHONEN remains four `[~]`, no `[x]`; same-lane verifier dispatch is not outside promotion verification. No commits, no pushes, no network, no nested agents; no needed background task remains.

## Bottom line

PASS — ADJACENCY unchanged / not harmed on the delivered r101 bytes: charter and all 174 prior fixtures byte-preserved, changes confined exactly to the declared U1/U2 ownership, no lore-attributable parent/sibling breach found, external material and rights/mechanics/canon refusals hold, the frozen chain verifies 8/8 with inherited pins field-identical, the full battery and all negative-boundary controls match their declared bounded outcomes, and the round's new bytes (pin, repointed-edge case, R10 non-conflict record) absorb nothing from adjacent provinces.
