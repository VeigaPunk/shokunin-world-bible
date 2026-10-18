# V46 — inherited-tools (round 99)

Seat: **V46 inherited-tools** — verifier. Claim under test: `git diff 4265df5` shows
`check_bible` / `support_check` / `boundary_doc_check` / `discriminate_check`, plus every
fixture byte from r98 and older, untouched.

Baseline: r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree
HEAD at measurement was `337f0fa` (the blocked-dispatch commit; `git diff --stat 4265df5 HEAD`
is only `LOG.md` + `SCORECARD.md`). All commands ran from
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents, no
commits, no network. Writes: this report and
`.ufo/waves/round-99/seats/V46-scratch/` only.

Axes: (1) blob/byte identity of the inherited checkers vs `4265df5`; (2) blob identity of
every pre-r99 fixture file; (3) no stray write inside that set; (4) poll closure — certify
the delivered revision, not a plan. (1)–(3) held on every sample. (4) did not close.

Scope note: the brief says `boundary` / `discriminate`; the paths are
`corpus/tools/boundary_doc_check.py` and `corpus/tools/discriminate_check.py`.
`check_bible.py` is `corpus/fixtures/check_bible.py` (live copy
`corpus/live/rejected-r4/check_bible.py` included as corroboration, not a second claim).
`map_obligations.py` is unowned this round and was swept the same way.

## Poll — producers not closed

Corrected poll (v2), 20 s cadence, 40 tries, `2026-10-18T01:04:48Z` → `01:26:09Z`.
Exit condition required S1–S5 reports, both S5 knowledge files, r99 fixture ≥10 files,
inherited drift 0, stray 0, and two consecutive identical signatures.

```
$ grep -E 'POLL-|STALL-' .ufo/waves/round-99/seats/V46-scratch/poll.log
POLL-START 2026-10-18T01:04:08Z
POLL-V2-START 2026-10-18T01:04:48Z
STALL-ESCAPE harness-timeout-at-v2-try-30 2026-10-18T01:23:09Z; continuing tries 31-40
POLL-EXHAUSTED 2026-10-18T01:26:29Z
```

v1's first try was discarded: its stray filter counted S1's declared
`dependency_freeze.py` / contract edits as strays. The harness then killed the background
v2 process at the 600 s cap (try 30). That stall-escape is recorded, not treated as fatal;
tries 31–40 ran in the foreground. No second extension past 40.

Observed on all 40 v2 tries: `named_reports=2` (`S3-fixture-author.md`,
`S4-fixture-docs.md` only), `know=0`, `drift=0`, `stray=0` (declared S1 paths excluded).
Tool blob signature was constant and equal to `4265df5`. Absent at exhaustion, and still
absent at the post-poll check `2026-10-18T01:36:42Z`:

- `S1-freeze-hygiene.md` — ABSENT (S1 scratch gained `after/mirror` at 22:36:17 local,
  after exhaustion; tool/contract bytes had been stable since try ~23, but no report)
- `S2-tools-docs.md` — ABSENT (`S2-scratch` empty; `corpus/tools/README.md` and `SKILL.md`
  still baseline blobs)
- `S5-knowledge-notes.md` — ABSENT
- `corpus/knowledge/r99-gate-blind-spot-table.md` — ABSENT
- `corpus/knowledge/r99-lapse-scope-note.md` — ABSENT

Present: S3 and S4 reports; `corpus/fixtures/r99-window-lapse/` (10 files). That is not a
closed wave. This seat does not certify a delivered revision.

## What the exhaustion tree showed (not a verdict)

Final snapshot `2026-10-18T01:30:04Z`, re-checked by the checker run at `01:36:20Z`
(tool blobs identical before and after that run).

```
$ git diff --stat 4265df5 -- corpus/fixtures/check_bible.py corpus/tools/support_check.py \
      corpus/tools/boundary_doc_check.py corpus/tools/discriminate_check.py \
      corpus/tools/map_obligations.py corpus/live/rejected-r4/check_bible.py
(no output)

$ git diff --name-status 4265df5 -- corpus/fixtures
(no output; untracked r99-window-lapse does not appear)

$ # git rev-parse 4265df5:$f vs git hash-object, plus git show 4265df5:$f | cmp -s
IDENTICAL CMP-EQUAL corpus/fixtures/check_bible.py          20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
IDENTICAL CMP-EQUAL corpus/tools/support_check.py           a69ae9d27ad1e848c3188fa832352d00b7c0ffc7
IDENTICAL CMP-EQUAL corpus/tools/boundary_doc_check.py      4daa9998023f247fef7ca07d7cf2723f95cab0be
IDENTICAL CMP-EQUAL corpus/tools/discriminate_check.py      aa601eee3ec288eccf21e5bb78cd01caaacfea7c
IDENTICAL CMP-EQUAL corpus/tools/map_obligations.py         9509c849db222867896b32bbece568c92086bcba
IDENTICAL CMP-EQUAL corpus/live/rejected-r4/check_bible.py  072402681f7cbe153b72866772ce3e9a1abf612b

$ sha256sum corpus/fixtures/check_bible.py corpus/tools/support_check.py \
      corpus/tools/boundary_doc_check.py corpus/tools/discriminate_check.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
ebb6a0843e67bfaa3118eda7fbf69bac124aca8f5b87cd0b9721b5e6346b0053  corpus/tools/boundary_doc_check.py
6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef  corpus/tools/discriminate_check.py
```

Pin layer (boundary contract still the baseline blob `9b73e150…`; checker pin matches
observed bytes):

```
checker_MATCH True ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
document_MATCH True 7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e
```

Fixture sweep against `git ls-tree -r 4265df5 -- corpus` (1826 corpus paths; 1030 under
`corpus/fixtures/`):

```
FINAL fixture_baseline_paths=1030 json=855 other=175 changed=0 missing=0 new=10
NEW corpus/fixtures/r99-window-lapse/{README,claim-excerpt-map,contradictions,entities,
    fictional-excerpts,inspiration-note,relations,source-excerpt,sources,timeline}
```

The only new fixture path is the declared r99 directory. Chain fixtures inside that 1030
were also 0-changed on the earlier pass (`r88-m3-maya-cluster` 11, `r93-m2-kojiki-cluster`
11, `r94-paired-crossing` 10, `r95-crossing-aftermath` 10, `r96-crossing-response` 10,
`r97-crossing-acknowledgment` 10, `r98-clerk-filing` 10). The 11 intentionally malformed
JSON fixtures (`r5-invalid-json`, `r60-unavailable*`, `r61-*-malformed/unavailable`,
`r62-malformed*`) are inside the unchanged 855; invalidity is inherited, not introduced.

Lane porcelain at the snapshot, excluding gitignored `__pycache__`:

```
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? corpus/fixtures/r99-window-lapse/   (10 files)
```

Those two modifications are S1's declared paths, not this seat's untouched set. They are
not certified: no S1 report. Blobs at the snapshot:
`dependency_freeze.py` base `623b3501…` cur `ec55c2a1…`; contract base `d4553282…` cur
`7da596be…`. `corpus/tools/README.md` and `SKILL.md` were still
`IDENTICAL` to `4265df5` (`0c4de1c8…`, `39d4c548…`).

Checker behavior on those unchanged bytes (`01:36:20Z`):

```
$ python3 corpus/tools/boundary_doc_check.py
CERTIFIED ... replay_receipts=3/3 replay_cases=14/14 anchors=2/2   EXIT:0
$ python3 corpus/tools/boundary_doc_check.py --self-test
SELF-TEST PASS   EXIT:0
$ python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa… matches_pin=True
RESULT: DISCRIMINATION HELD   EXIT:0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS   EXIT:0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations   EXIT:0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations   EXIT:0
```

Tool blobs after that run were the same four SHAs as before it.

## Out of scope (evidence only)

Parent tree `/home/vgpnk/Projects/shokunin` (not the lane) gained
`.ufo/waves/round-99/seats/V69-scratch/` and `V73-scratch/` (baseline copies of
`dependency_freeze.py` / the contract, plus self-test stdout). That is the cwd-confusion
class. Not written by this seat. Lane stray count inside the inherited set was 0.
`corpus/tools/__pycache__/*.pyc` is gitignored (`__pycache__/`) and is not a source edit.

## Bottom line

**ABSENT** — after 40 poll tries (`01:04:48Z`–`01:26:09Z`, one recorded harness-timeout stall-escape) S1/S2/S5 reports and both S5 knowledge artifacts were still absent, and S1 was still writing after exhaustion, so this seat does not certify a delivered revision; the exhaustion tree's inherited checkers and all 1030 pre-r99 fixture files were byte-identical to `4265df5`, but that observation is not a closed-wave pass.
