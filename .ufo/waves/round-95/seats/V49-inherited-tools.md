# V49 — inherited-tools byte-integrity seat report (round 95)

- Seat: V49 inherited-tools. Scope: verify via `git diff fb118c4` that
  `check_bible.py`, `support_check.py`, `boundary_doc_check.py`,
  `discriminate_check.py`, `boundary-doc-contract.json` are byte-untouched,
  and that the r95 tool changes are confined to `map_obligations.py` + its
  contract + declared docs.
- Baseline: r94 closure `fb118c4` (`git log -1` = `fb118c4 lore r94: close
  round — …`, commit date `2026-10-17T16:05:45-03:00`). HEAD still `fb118c4`
  at report time — no seat committed.
- Method: poll-wait for producers (P1 landed at ~16:22, P2 at ~16:28, P5 at
  ~16:25; P3/P4 earlier), then four byte snapshots bracketing the write window
  (≈16:18, 16:23, 16:29, 16:31) so a late write to an inherited tool could not
  slip through. Read-only; no scratch dir declared, nothing written except this
  report.

## 1. Path clarification (first observed fact)

`check_bible.py` is **not** under `corpus/tools/`. `find corpus -name
check_bible.py` returns two copies, both verified:

```
corpus/fixtures/check_bible.py          (canonical checker)
corpus/live/rejected-r4/check_bible.py  (frozen rejected-r4 copy)
```

The other four named artifacts are canonical at `corpus/tools/`. Both
check_bible copies were included in every byte check.

## 2. Byte-integrity of the five named artifacts (four snapshots, identical result)

Command (run at each snapshot; blob hash of working tree vs blob in `fb118c4`):

```
for p in corpus/fixtures/check_bible.py corpus/live/rejected-r4/check_bible.py \
         corpus/tools/support_check.py corpus/tools/boundary_doc_check.py \
         corpus/tools/discriminate_check.py corpus/tools/boundary-doc-contract.json; do
  cur=$(git hash-object "$p"); base=$(git rev-parse "fb118c4:$p"); ...
```

Observed at the final snapshot (16:31:37-03:00):

```
UNTOUCHED corpus/fixtures/check_bible.py         20c56dbb90d9f59ca4fb85971154c0774f5ce0d0
UNTOUCHED corpus/live/rejected-r4/check_bible.py 072402681f7cbe153b72866772ce3e9a1abf612b
UNTOUCHED corpus/tools/support_check.py          a69ae9d27ad1e848c3188fa832352d00b7c0ffc7
UNTOUCHED corpus/tools/boundary_doc_check.py     4daa9998023f247fef7ca07d7cf2723f95cab0be
UNTOUCHED corpus/tools/discriminate_check.py     aa601eee3ec288eccf21e5bb78cd01caaacfea7c
UNTOUCHED corpus/tools/boundary-doc-contract.json 9b73e150ceaf59225bb256006b1b3bcfa0ec0f91
```

Corroboration, all consistent:

- Modes unchanged: `git ls-tree fb118c4 <p>` vs `git ls-files -s <p>` = `100644`
  for all six paths; `git diff fb118c4 --summary` empty (no mode/rename events).
- `git diff fb118c4 -- <any of the six>` is empty; `git diff --diff-filter=D
  --name-only fb118c4` empty (no deletions anywhere).
- sha256 `corpus/fixtures/check_bible.py` =
  `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` — exact
  match to the checker pin recorded in the r94 closure (`wave-spec.json`
  `checker_sha256` and LOG.md r94 closure text).
- mtimes all predate the round and even the baseline commit:
  check_bible 06:50:47, discriminate 11:47:42, support 10:00:58,
  boundary_doc_check 13:40:47, boundary-doc-contract 13:40:28 (-03:00), vs
  baseline commit 16:05:45 and round start ~16:16.

## 3. Functional smoke of the inherited tools on the delivered revision

Not my primary mandate, but run once as corroboration that the untouched bytes
still behave as the r94 receipts recorded (r94-paired-crossing):

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
→ CLEAN: schema, citations, relations, timeline; 0 violations      exit=0

python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
→ RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
  SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; … MODES 16/16; VALIDATED-ROWS 16/16
  RESULT PASS                                                       exit=0

python3 corpus/tools/boundary_doc_check.py
→ … duplicate_headings=0 / instruction_markers=0 / CERTIFIED (bounded: …)  exit=0
python3 corpus/tools/boundary_doc_check.py --self-test
→ SELF-TEST PASS missing_checker … ; SELF-TEST PASS                 exit=0

python3 corpus/tools/discriminate_check.py
→ RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression  exit=0
```

(C3's "r88/r93/r94 support_check receipts unchanged" is V07's seat; my r94 run
is corroboration only.)

## 4. Confinement of the r95 tool changes

Final `git diff --numstat fb118c4` (whole repo, tracked):

```
57      0       LOG.md
20      0       corpus/tools/README.md
8       1       corpus/tools/map-obligations-contract.json
130     12      corpus/tools/map_obligations.py
```

Untracked non-scratch additions (whole repo): the 10 files of
`corpus/fixtures/r95-crossing-aftermath/` (P3+P4 ownership), 
`corpus/knowledge/r95-aftermath-scope-note.md` (P5), and seat reports under
`.ufo/waves/round-95/seats/`. Remaining untracked paths are seat scratch dirs
(`.ufo/waves/round-95/scratch/`, `.ufo/waves/round-95/seats/*scratch*/`,
1556 scratch paths counted) — non-deliverable by construction.

Every changed/added deliverable path maps to declared byte-ownership:

| Path | Owner | Declared |
|---|---|---|
| `corpus/tools/map_obligations.py` | P1 | yes |
| `corpus/tools/map-obligations-contract.json` | P2 | yes |
| `corpus/tools/README.md` | P2 | yes |
| `corpus/fixtures/r95-crossing-aftermath/**` (10 files) | P3/P4 | yes |
| `corpus/knowledge/r95-aftermath-scope-note.md` | P5 | yes |
| `LOG.md` | round declaration (integrator) | yes (round-95 declaration block) |
| `.ufo/waves/round-95/seats/**` | seat reports | yes (exclusive report paths) |

No other tool, contract, corpus fixture, README, or knowledge file changed.
Cross-check of producer honesty: P1's report claims `130 12` numstat for
`map_obligations.py`; observed numstat is exactly `130 12`.

## 5. Bounds of this verification

1. Byte integrity is proven by blob-hash equality against `fb118c4` at four
   snapshots between ≈16:18 and ≈16:31:37 (-03:00). A write after my final
   snapshot is not covered by me; the round's later closure should re-run the
   hash check if any producer seat resumes.
2. "Untouched" here = bytes + mode of the named artifacts. Their behavior was
   additionally smoked (§3) but their semantics are other seats' scope.
3. `corpus/live/rejected-r4/check_bible.py` is a second copy of the named
   artifact; it is also byte-untouched (included in all checks). No other
   corpus copy of the five named artifacts exists (`find corpus` verified).

## Bottom line

PASS — all five named inherited artifacts (plus the rejected-r4 check_bible
copy) are byte- and mode-identical to `fb118c4` across four snapshots, the
checker pin `ff9fd2aa…` reproduces exactly, inherited tools still exit as
recorded, and the r95 tool-tree writes are confined to
`map_obligations.py` + `map-obligations-contract.json` + `README.md` with all
other changes inside declared fixture/knowledge/report ownership.
