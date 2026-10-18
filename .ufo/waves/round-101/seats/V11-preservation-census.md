# V11 — preservation-census (round 101)

Seat: V11, preservation census. Baseline: `6f86bf2` (r100 freeze commit, verified ancestor of HEAD `ebec6bb`; two commits between: `a04f986` r100-closure → touches only `SCORECARD.md`, `ebec6bb` r101-declare → touches only `LOG.md`). All commands run from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with python3 available; no writes outside this report.

## Method

Census = (a) top-level enumeration of `corpus/fixtures`; (b) full path-level diff of every inherited path vs `6f86bf2`, covering both the committed range (`git diff 6f86bf2..HEAD`) and the uncommitted wave tree (`git diff 6f86bf2` for tracked files + `git ls-files --others --exclude-standard` for untracked).

## Poll-wait record

- Main poll: 40 tries × 20s (800s). At exhaustion: U1 report present, all four U1 files modified, U2 knowledge record present, **U2 report ABSENT** (poller exit 3, observed output `STILL ABSENT after 40 tries ... U2 report: ABSENT`).
- Bounded stall-escape: 6 tries × 20s (120s) for the U2 report only — still ABSENT (exit 3), recorded, not fatal. Total 46 tries ≈ 15.3 min.
- U2's report `U2-r10-register.md` appeared during the final shape-check pass (present in the seats listing at census close). Both producer reports present before this report was written.

## C1 — fixture census: 174, no new fixture — PASS

```
$ find corpus/fixtures -mindepth 1 -maxdepth 1 ! -name check_bible.py ! -name README.md -type d | wc -l
174
$ find corpus/fixtures -mindepth 1 -maxdepth 1 ! -type d
corpus/fixtures/check_bible.py
corpus/fixtures/README.md
```

176 top-level entries = 174 fixture directories + the two long-standing helpers. Expected count hit exactly.

Byte-immutability across the whole baseline delta (committed + uncommitted):

```
$ git diff --name-status 6f86bf2 -- corpus/fixtures
(empty — zero changed paths, no additions, no deletions)
```

`corpus/fixtures` is byte-identical to `6f86bf2`. The now-pinned `r100-docket-review` fixture already existed at baseline (created r100); r101 added no fixture and touched none.

## C2 — full inherited-path diff vs 6f86bf2 — PASS, expected changes only

```
$ git diff --name-status 6f86bf2            # tracked, committed + uncommitted
M	LOG.md
M	SCORECARD.md
M	SKILL.md
M	corpus/tools/README.md
M	corpus/tools/dependency-freeze-contract.json
M	corpus/tools/dependency_freeze.py

$ git ls-files --others --exclude-standard | grep -v -e '^\.ufo/' -e '^\.scratch/'
corpus/knowledge/r101-r10-register-first-entry.md
```

No `D` entries anywhere; `corpus/live/`, tracked `corpus/knowledge/`, and every other inherited path are untouched. Classification of all seven changed paths:

| Path | Delta source | Classification |
|---|---|---|
| `SCORECARD.md` | committed `a04f986` only (r100 closure); zero working-tree delta | pre-round closure doc — expected |
| `LOG.md` | committed `ebec6bb` only (r101 declare); zero working-tree delta | pre-round declaration doc — expected |
| `corpus/tools/dependency_freeze.py` | working tree (U1-owned) | expected |
| `corpus/tools/dependency-freeze-contract.json` | working tree (U1-owned) | expected |
| `corpus/tools/README.md` | working tree (U1-owned) | expected |
| `SKILL.md` | working tree (U1-owned) | expected |
| `corpus/knowledge/r101-r10-register-first-entry.md` (new, untracked, 122 lines) | working tree (U2-owned) | expected |

**Findings of unexpected inherited changes: none.** The wave-tree delta is exactly U1's four owned files plus U2's one owned record — the task's expected set, nothing more, nothing less.

### Diff-shape corroboration (census-level, not claim verification)

`git diff --stat 6f86bf2 -- SKILL.md corpus/tools/` → `SKILL.md | 7 +-`, `corpus/tools/README.md | 59 ++ (insertions only)`, `dependency-freeze-contract.json | 143 +-`, `dependency_freeze.py | 18 ++ (insertions only)`; 223 insertions, 4 deletions total. Observed shapes match the declared footprints:

- `dependency_freeze.py`: `FROZEN_CASES` gains `"repointed_edge"`; one new self-test case block repoints `aftermath-missing-evin`'s `depends_on` from `paired-crossing-decision` to `aru-ninth-bell`, expected exit 1.
- `dependency-freeze-contract.json`: top-level `revision` refresh `b5fe472…` → `ebec6bb…` (the writer-managed refresh disclosed since r100) + one new pin block `r100-docket-review` (10 `pinned_files`, per-file SHA-256, `content_sha256`, events).
- `SKILL.md`: freeze row chain seven→eight (`…, r99-window-lapse, r100-docket-review`), self-test 18→19 cases with `repointed_edge`, new dated supersession row (2026-10-18, round 101).
- `corpus/tools/README.md`: append-only round-101 addendum section; prior receipts kept.

## Verdict

- Fixture census: **PASS** (174, unchanged bytes, no new fixture).
- Preservation diff: **PASS** (expected producer set only; LOG/SCORECARD deltas fully attributed to the pre-round closure/declare commits; zero unexpected inherited changes; zero deletions).
- Poll record: U2 report ABSENT through 46 tries (~15.3 min), landed before census close — bounded stall-escape recorded, non-fatal.

Bottom line: **PASS — fixtures 174 and byte-identical to 6f86bf2; inherited delta is exactly U1's four owned files + U2's new knowledge record (plus pre-round committed LOG/SCORECARD closure docs); no unexpected inherited changes.**
