# V41 — census-replica-2 (round 97)

Seat: V41 `census-replica-2`. Scope per seat spec: **independent second census**
of `corpus/fixtures` against a **`git archive` of `f3e09f9`**; expect **171**
dirs; enumerate new paths; require **0 unexpected inherited changes**;
**cross-check V21**. Baseline: r96 closure commit `f3e09f9` (working HEAD
`2393934` = `f3e09f9` + the r96 SCORECARD closure commit; `LOG.md` carried the
r97 declaration before any seat ran). All commands run from repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Writes: this
report plus declared scratch `.ufo/waves/round-97/seats/V41-scratch/`
(`census.py`, `census_delta.py`, `compare_pre.py`, `poll.sh`, `poll2.sh`,
`freeze.sh`, `freeze-manifest.sha256`, `census-archive.jsonl`,
`census-archive2.jsonl`, `census-work-{interim,postmap,final,frozen}.jsonl`,
`delta-{dryrun,interim,final,frozen}.json`, `archive-f3e09f9/`). No commits,
no pushes, no network, no nested agents, no other file touched. Stray-write
check (r94-F01 class): `/home/vgpnk/Projects/shokunin/.ufo/waves/round-97`
and `/home/vgpnk/Projects/shokunin/corpus` do not exist — no parent-tree
writes from this seat.

## 0. Method (fresh implementation, deliberately not V21's script)

- `census.py` (written by this seat, stdlib only): for every sorted **direct
  fixture directory** under `corpus/fixtures`, runs
  `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>` from the
  given root (archive root or repo root), records exit code, `VIOLATION:` line
  count, all non-empty output lines, and full stdout SHA-256. Summary prints
  dirs / exit counts / violation lines / stderr / unexpected exits.
- `census_delta.py` (written by this seat): `git archive f3e09f9 corpus/fixtures`
  → extract to scratch → SHA-256 every file on both sides → classify
  `inherited / modified / deleted / new`; top-dir sets compared; `--expected`
  dirs, allowed new dirs, and allowed modified paths are the machine-checked
  pass conditions.
- **Null control (baseline revision, before trusting the verdict):** the
  archive census reproduces the r96 closure census exactly —

  ```
  $ python3 .ufo/waves/round-97/seats/V41-scratch/census.py \
      .ufo/waves/round-97/seats/V41-scratch/archive-f3e09f9 \
      .ufo/waves/round-97/seats/V41-scratch/census-archive2.jsonl
  {"fixture_dirs": 170, "exit_counts": {"0": 36, "1": 134},
   "violation_lines": 421, "stderr_nonempty_count": 0,
   "unexpected_exit_count": 0}
  ```

  plus `lines_nonempty_total=591` (= 421 violations + 134 negative summaries +
  36 CLEAN lines) and `sha256sum` of `check_bible.py` identical on both sides:
  `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.
  Baseline archive: 170 fixture dirs, 1010 files.

## 1. Poll-wait record (20 s cadence; producer artifacts + reports)

- 18:41–18:43 first checks: `r97-crossing-acknowledgment` absent; zero seat
  reports; V21-scratch already present (baseline manifest 18:42, pre-census
  18:44).
- 18:44:16 r97 dir appears (10-file preserving copy; 5 byte-copy files at
  18:44:16, `sources.json`/`timeline.json`/`fictional-excerpts.md` at
  18:44:30); R5's first map/README versions same minute.
- 18:45–18:47 producers land tools: `map_obligations.py` 18:45,
  `map-obligations-contract.json` 18:46, tools `README.md` 18:47. Reports:
  R1 (seen by poll 18:48:18), R2 (18:48:58), R4 (18:50:28), R5, R6 note 18:52
  with R6 report by 18:54:39, R3 (`dependency_freeze.py` 18:53:00, contract
  18:54:38 then final 18:55:14, report 18:56:32).
- **Transient mid-wave observation (recorded exactly):** before R5 extended
  the r97 map (file mtime 18:48:56), `map_obligations` on the r97 fixture
  returned `OBLIGATIONS raw=17 mapped=16 … FINDING missing_obligation:
  timeline.json#/5 has no map row / RESULT FAIL` (exit 1); poll2's own log
  brackets it — try=1 (18:48:41) `map_exit=1` → try=2 (18:49:01)
  `map_exit=0`. The receipt is green thereafter (§5). Not a freeze-time
  defect — recorded as the observed mid-work state.
- 18:56:42 poll2 exit: `POLL2_OK try=25 reports=6 map_exit=0`. poll1 was cut
  by the 600 s background-task wall cap before its 40-try window elapsed; the
  six-report state was confirmed manually at 18:56:32 and by poll2. **All six
  producer reports were present at freeze; nothing in this seat's scope was
  ABSENT.**
- **Freeze at 18:56:39:** `sha256sum -c freeze-manifest.sha256` → **18/18 OK**
  (10 r97 files + r96 map + `check_bible.py` + 5 tools files + R6 note).

## 2. Final census — 171 dirs (primary receipt)

```
$ python3 .ufo/waves/round-97/seats/V41-scratch/census.py . \
    .ufo/waves/round-97/seats/V41-scratch/census-work-frozen.jsonl
{"fixture_dirs": 171, "exit_counts": {"0": 37, "1": 134},
 "violation_lines": 421, "stderr_nonempty_count": 0,
 "unexpected_exit_count": 0}
```

- 171 dirs = **37 clean (exit 0) + 134 intentional negative (exit 1)**, 421
  violation lines, zero stderr, zero non-0/1 exits — exactly the declared
  after-state (170/36/134 → 171/37/134, violations unchanged at 421).
- **Snapshot stability:** four full sweeps — interim 18:47, post-map 18:50,
  final 18:55, frozen 18:56 — are pairwise **byte-identical per-dir records**
  (exit, violation count, line count, stdout SHA-256).
- **vs archive:** the 170 common dirs show **0 mismatches** on all four fields;
  `only_work = ["r97-crossing-acknowledgment"]`, `only_archive = []`.
- `corpus/fixtures` holds exactly two non-dir entries (`check_bible.py`,
  `README.md`), so dir counts are unambiguous across methods: python walker
  171, `find -mindepth 1 -maxdepth 1 -type d` 171, `ls -d corpus/fixtures/*/`
  171.

## 3. Delta receipt vs `f3e09f9` (0 unexpected inherited changes)

```
$ python3 .ufo/waves/round-97/seats/V41-scratch/census_delta.py f3e09f9 corpus/fixtures \
    171 r97-crossing-acknowledgment r96-crossing-response/claim-excerpt-map.md \
    .ufo/waves/round-97/seats/V41-scratch/delta-frozen.json
CENSUS PASS: dirs=171 files=1020 modified=1 deleted=0 new=10
```

- baseline_top_dirs 170 → work 171; files 1010 → 1020; inherited files 1009
  (byte-identical); **modified_inherited = [`r96-crossing-response/claim-excerpt-map.md`]
  — exactly the declared cosmetic repair, nothing else**; deleted 0; new 10
  files, all under the one new dir:

  ```
  r97-crossing-acknowledgment/{README.md, claim-excerpt-map.md,
  contradictions.json, entities.json, fictional-excerpts.md,
  inspiration-note.md, relations.json, source-excerpt.md, sources.json,
  timeline.json}
  ```

- **Second, git-native method:** `git ls-tree -d --name-only f3e09f9
  corpus/fixtures/ | wc -l` → 170; `git ls-tree -r --name-only f3e09f9
  corpus/fixtures | wc -l` → 1010; `find corpus/fixtures -mindepth 1 -maxdepth
  1 -type d | wc -l` → 171; `git diff --name-status f3e09f9 -- corpus/fixtures`
  → one line, `M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`;
  `git status --porcelain -- corpus/fixtures` → ` M …claim-excerpt-map.md` and
  `?? corpus/fixtures/r97-crossing-acknowledgment/`.
- The r97 dir has no nested subdirectories; its 10 files are the complete
  declared set. 5 of the 10 are byte-identical to their r96 counterparts
  (entities, relations, contradictions, inspiration-note, source-excerpt —
  the declared byte copies); sources.json / timeline.json /
  fictional-excerpts.md / map / README differ (declared additions).

## 4. Cross-check V21 (four layers, all exact)

V21's scratch artifacts were taken independently (its own `census.sh` glob +
`grep -c .` line metric + per-dir receipts). Cross-checks:

1. **Pre-census vs my archive census:** V21 `census_pre.txt` (170 dirs, 36
   clean / 134 negative / 0 other, LINES=591) compared per-dir against my
   archive records —
   `v21_dirs=170 mine_dirs=170 only_v21=[] only_mine=[] rc_or_lines_mismatches=0`.
2. **Per-dir stdout hashes:** V21 `census_pre_receipts.json` (171 entries,
   including r97) vs a fresh rerun by this seat — exit codes match and
   **stdout SHA-256 matches 171/171** after normalizing one capture artifact:
   V21 captured stdout via shell `$(…)`, which strips trailing newlines
   (raw matches 0, trailing-newline-stripped matches 171, mismatches 0).
3. **Post-producer byte snapshots:** V21 `snap-a.sha256` (18:56:54, 19 changed
   paths) vs my freeze manifest — **17/17 shared paths identical**; V21's two
   extras are `LOG.md` / `SCORECARD.md` (outside my manifest). `snap-a` vs
   `snap-b` are byte-identical (V21's two post-producer snapshots agree), and
   `snap-b` also matches my freeze manifest 17/17.
4. **Inventory counts:** V21 `dirs-now.txt` = 171 dirs, `files-base.txt` =
   1010, `files-now.txt` = 1020 — identical to my walker and git-native
   counts.

V21's final report (`V21-preservation-census.md`) landed at 19:01, after my
freeze; its text confirms the same final census this seat measured —
`{"fixture_dirs": 171, "clean_exit0": 37, "negative_exit1": 134,
"violation_lines": 421, "non_0_1_exits": []}` with the 170-dir null control
`170/36/134/421` — and the same inventory delta (170→171 dirs, 1010→1020
files, 0 removed). Its `census_final_receipts.json` carries the per-dir stdout
hashes already matched in layer 2. The cross-check verdict therefore rests on
V21's published artifacts **and** its report text.

## 5. Corroborating receipts at freeze (context, not this seat's verdict)

- r97: `map_obligations` → `OBLIGATIONS raw=17 mapped=17; INVENTORY
  JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19 / RESULT PASS`;
  `support_check` → `SOURCE-SUPPORT 17/17 … MODES 19/19 / RESULT PASS`.
  Structure observed: 5 entities / 1 relation / 6 events / 6 sources, new
  event `acknowledgment-aru-records` depending on `response-evin-salt-court`,
  `contradictions.json` `[]` (unresolved preserved).
- r96 post-repair: `map_obligations` 16/16 PASS; `support_check` 16/16 PASS;
  `dependency_freeze` `DIGEST d422a9b3… RESULT PASS`.
- Producer-declared hashes match the frozen bytes: r96 post-repair map
  `e851f068…` (R4), r97 README `d9387b7d…` and map `49d4834e…` (R5);
  `dependency_freeze --self-test` observed `SELF-TEST 16/16 / RESULT PASS`.

## 6. Limits

- The census is **structural** (exit codes, line counts, check_bible stdout
  bytes). It does not read map/README prose and makes no semantic, support,
  canon, or rights claim; the checker validates structure, not testimony.
- The r96 map repair is invisible to check_bible (0 output changes across the
  170 inherited dirs) but is the single byte-level modified inherited file.
- Freeze manifest pins 18 paths (census scope + tools + R6 note); `LOG.md` /
  `SCORECARD.md` are declaration/closure-side and outside it.

## Bottom line

**PASS** — the independent census reproduces **171 dirs / 37 clean / 134
negative / 421 violation lines / 0 unexpected exits** on the frozen revision
with **0 inherited changes** vs the `f3e09f9` archive (+1 dir, +10 files,
exactly 1 declared repair modification, 0 deletions); all six producer reports
present at freeze; cross-check V21 exact on all four layers (pre-census
per-dir, 171/171 stdout hashes, 17/17 post-producer byte hashes ×2 snapshots,
inventory counts 171/1010/1020).
