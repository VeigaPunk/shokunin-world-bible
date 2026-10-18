# V08 — c3-sweep-audit (round 102 capstone)

Seat: V08, verifier (leaf). Date: 2026-10-18. Lane root:
`/home/vgpnk/Projects/shokunin/lore-shokunin`. Model:
zai-coding-plan/glm-5.3-flash-low. Audited object: U2's
`corpus/knowledge/r102-freshness-sweep.md` (landed 06:35 lane-local) +
seat report `.ufo/waves/round-102/seats/U2-freshness.md`. Measured
revision: HEAD `8fa2e87` (r102 declaration); tracked corpus clean at
HEAD except U2's own three knowledge writes (`M
2026-10-12-malformed-error-patterns.md`, `M r91-c9-watch.md`, `??
r102-freshness-sweep.md`; U1's `r102-debt-ledger.json` also untracked —
C2 is not this seat). No commits, no pushes, no network. Scratch:
`seats/V08-scratch/ground-truth.md` (full pre-sweep ground-truth
ledger).

## Poll record

Window 1 (40 × 20 s from 06:19): ABSENT at 06:31:47 (seats dir held
V11/V13 reports + U1 scratch; no U2 report, no sweep). Window 2
(recorded bounded stall-escape per endgame convention, 40 × 20 s from
~06:32): sweep + U2 report FOUND at ~06:36 (try ~13).

## Method

Before the sweep landed I built an independent ground-truth ledger
(pins, commits, receipts, census) so sweep claims could be checked
against my own measurements, not re-derived from U2's text. After
landing, I re-verified tokens/claims and re-ran quoted commands
verbatim from the lane root.

## Re-verified tokens/claims (16 sampled, ≥10 required)

| # | Sweep claim | My re-verification | Result |
|---|---|---|---|
| 1 | checker pin `ff9fd2aa…d1421` | `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` | EXACT |
| 2 | `support_check.py 55a5eb27…`, `map_obligations.py 86b52949…` live | sha256sum → `55a5eb2753901be7…`, `86b529496214493f…` | EXACT |
| 3 | freeze chain 8/8 digests (r88 `acf677a7…` … r100 `77debadf…`) | re-ran `dependency_freeze.py` per fixture; all 8 DIGEST lines byte-identical to the sweep's table | 8/8 EXACT |
| 4 | F1: `b6ca1e902f2bf08b8acddaef665d9764f8636981` dangling | `git cat-file -t` → fatal in lane repo AND parent `/home/vgpnk/Projects/shokunin`; `git log --all | grep -c` = 0 in both | CONFIRMED |
| 5 | F1 addendum's six-row re-run (`consistent` + 5 × `r5-*`) | re-ran all six: exit 0 CLEAN / five exit 1 with exactly the quoted primary diagnostics, stderr empty | EXACT |
| 6 | r93 record digest `da934a7…`, 5/5 fields | extracted the note's 98-line heredoc verbatim, ran it: `R8 replay: PASS`, `12/12 cells`, digest `da934a7eea6d108f…` exit 0; first block 5/5 fields exit 0 | EXACT |
| 7 | arc snapshots 7 × `c279254bc7de0636…` @ 139 B | re-ran the r101 note's own receipt heredoc over r94…r100 fixtures: all seven `c279254bc7de0636 139` | EXACT |
| 8 | repair pair `5093d72e`@f3e09f9 → `e851f068`@9d25df9 | `git show <rev>:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md \| sha256sum` → both prefixes exact; live r97 map `49d4834e124fa6cf` as per-note row claims | EXACT |
| 9 | historical blob digests (`3ae4134d`@03c6746+2b48ca7, `dcacffd6`@2ea9ef1, `e2bb9639`@1b09f3f, `cc1df4dc`@abbc3e0, `ea012b9c`@6f86bf2; plus `03d04365`/`153ebc5b`@4265df5, `fb9bb9ff`/`8c2561b0`@fe1ce46, `d1c239cc`/`8173bb97`@dcb2d92, `2b0ba815`/`97b76bb8`@f3e09f9) | `git show <rev>:<path> \| sha256sum` for each | ALL EXACT |
| 10 | per-pin contract revisions 6 × `337f0fa…` + `b5fe472…` + `ebec6bb…`; top-level `ebec6bb…` | dumped `dependency-freeze-contract.json`: `{'337f0fa5': 6, 'b5fe4729': 1, 'ebec6bbd': 1}`, top-level `ebec6bbd` | EXACT |
| 11 | boundary doc digest = contract `7f815a93…` | `sha256sum corpus/knowledge/holder-assessment-boundary.md` → `7f815a9389c415de…`; contract `document.sha256` field carries the same value (plus git-blob `revision` `65838f86…` — both forms consistent) | EXACT |
| 12 | census 174 dirs / 40 clean / 134 negative / 421 violation lines / 0 stderr / 0 other | full replay of check_bible over all 174 fixture dirs: `dirs=174 clean=40 negative=134 violation_lines=421 stderr=0 other_exits=0` | EXACT |
| 13 | provenance-carrying 29@1b09f3f / 33@ca7f9ef; 160 dirs@1b09f3f | `git archive` + entities.json `"provenance"` grep → 29 and 33; entities.json count at 1b09f3f → 160 | EXACT |
| 14 | r99 FREEZE receipt + DIGEST `7fe7e3b0…` | re-ran `dependency_freeze.py corpus/fixtures/r99-window-lapse`: `FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1`, `DIGEST 7fe7e3b065088e59…`, exit 0 | EXACT |
| 15 | distinct token count **98** | recount on pre-addenda bytes (HEAD copies of the two modified notes + on-disk rest), stated method `\b[0-9a-f]{7,64}\b`, 25-file scope: union distinct = **98** | EXACT |
| 16 | C9 r102 re-check landed (F2) | `r91-c9-watch.md` tail: dated 2026-10-18 (r102) row, re-check 11, DISCRIMINATION HELD, cadence-ends wording; append-only (r101 text intact, verified against my pre-landing full read) | LANDED |

## Quoted commands re-run (12 ≥ 5 required)

All from the sweep's receipt log; all reproduce: (1) checker sha256sum
(exact); (2) `discriminate_check.py` → `RESULT: DISCRIMINATION HELD`
exit 0 and `--checker e97613c` → `REGRESSION-DETECTED on
r91-c1-null-chain,r91-c1-tick-unresolved` exit 2; (3) freeze per-fixture
8/8 + `r101-repointed-edge` → `FINDING UNPINNED-FIXTURE …` exit 2 as
documented; (4) freeze `--self-test` → `SELF-TEST 19/19` / `RESULT
PASS` exit 0 (case 19 `repointed_edge` present); (5) map `--self-test`
→ 25 `SELF-TEST PASS` lines, `RESULT PASS` exit 0; (6) `boundary_doc_check.py`
→ 4 CHECK PASS, `CERTIFIED (bounded: …)` exit 0, and `--doc
<drifted copy>` → `FINDING document_drift` **exit 1**; (7) support_check
r94/r95/r99 receipts (14/16, 15/17, 21/23 + raw map lines) match; (8)
map_obligations r95/96/97/99 `raw=mapped` exact (15/16/17/21); (9) full
census replay (row 12 above); (10) `git show` blob-digest lineage (row
9); (11) r5 table six-row replay (row 5); (12) r93 heredoc replay
(row 6). Also spot-checked: `corpus/live/runs/20261012T164316Z/` exists;
`r100-crossing-arc-synthesis.md:46` carries the quoted sentence
verbatim.

## Disposition audit

- F1 disposition **correct**: pin genuinely dangling in every store I
  can reach; addendum landed dated/append-only and supersedes only the
  `git diff b6ca1e9` instruction; its fresh six-row table reproduced
  under my own run. LOG.md r5 reference correctly left to the log owner.
- F2 disposition **correct**: the watch's r101 row schedules "Next
  re-check: r102"; re-check 11 landed with both discriminator modes and
  the expected exits, which I reproduced independently at 06:2x.
- Waiver register **correct in substance**: in-flight pins
  (`9224a684`, `6634e176`, `8173bb97`, `c435239d`, `2142b991`, …) are
  each flagged in-file by dated addenda (r95 note :61–:71, r96 note
  :65–:75, r98 note :77–:79) — verified by reading them; `git show` at
  r95/r96 closures reproduces `d1c239cc`/`8173bb97` and
  `2b0ba815`/`97b76bb8` exactly as those addenda state; W05 mismatch
  covered by the dated pin note at `corpus/fixtures/README.md:1175`
  (W05 manifest entry `a13d1af3…` vs current bytes — mismatch real);
  historical probe post-images sampled (`03d04365…` baseline tool,
  `5ecf84e1…` live pin) verify.
- Per-note rows sampled (r95/r96/r97/r98/r99/r100/r101/holder/C9/
  fixtures-README/tools-README) all consistent with my measurements.

## Defects found in the sweep's own record (reported, not fixable from this seat — U2 owns the bytes)

- **D1 — inventory occurrence count not reproducible.** Sweep states
  "Token occurrences across the 25 swept files: **178**". Under its own
  stated method (`\b[0-9a-f]{7,64}\b`) I count **290** on pre-addenda
  bytes (HEAD copies of the two notes U2 modified after inventorying)
  and **304** on delivered bytes; alternates also miss (≥8 chars: 195;
  ≥16: 118; per-file distinct-sum: ~151; per-line raw/dedup: 353/348).
  The **distinct count 98 reproduces exactly** (row 15). Direction:
  undercount. Non-load-bearing — no disposition depends on it — but it
  is a falsifiable number in the C3 record that fails independent
  reproduction. Scope "25 files" itself is correct (22 notes + 3
  READMEs).
- **D2 — W05 row misstates the current digest.** Sweep: "W05 baseline
  pin `a13d1af3…` … file now hashes `3c1ee6bf…`". In fact
  `3c1ee6bf75402dbc…` is the **W05 manifest's own** sha256
  (`sha256sum .ufo/waves/round-94/work/W05-baseline-corpus.sha256` →
  `3c1ee6bf75402dbc…`, and `W05.md:17` names it "Manifest SHA-256");
  the pinned file `corpus/fixtures/README.md` currently hashes
  `9b729bfe55cfc35…` (untouched since Oct 17 23:55 per mtime). The
  mismatch claim itself ("no longer matches") is TRUE and the waiver
  disposition correct; only the row's wording points `3c1ee6bf…` at the
  wrong object.

## Verdict

Substance of C3 verifies: every live pin, receipt, census, self-test
and disposition I sampled reproduces against delivered bytes; F1 is a
real dangling pin correctly corrected by a dated addendum; F2 (the due
r102 C9 re-check) landed append-only; all waivers are justified and
in-file. Two non-load-bearing numeric/wording defects (D1, D2) exist in
the sweep's own inventory — reported above for the integrator/U2 to
amend if desired; neither flips a disposition nor hides a stale pin.
No axis harmed by the audited bytes: the two addenda are append-only
corrections, the sweep is a new knowledge record; no commits, no
pushes.

**Bottom line: PASS — C3 sweep verifies on the delivered revision (16
tokens/claims + 12 quoted commands re-verified, all dispositions
correct), with two reported non-load-bearing defects in the sweep's own
inventory counts (D1 occurrence total 178 irreproducible → 290/304; D2
W05 row cites the manifest digest as the pinned file's).**
