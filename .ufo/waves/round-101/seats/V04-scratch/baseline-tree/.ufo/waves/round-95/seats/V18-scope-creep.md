# V18 — scope-creep (round 95)

- Seat: V18 scope-creep. Baseline: r94 closure `fb118c4`. Scan window 2026-10-17 16:16–16:35 -0300.
- Mandate: bucket every working-tree path after all producers land; any persistent path outside the declared buckets = scope-creep finding; verify no new `__pycache__` under `corpus/` (report, do not clean). Report-only seat: no commits, no cleanup, no scratch dir declared (scratch used under `/tmp` only).

## Protocol compliance

- Poll-wait for P1–P5 reports at 20 s cadence. Landed: P3 (final mtime 16:22, first seen 16:20), P5 16:25, P4 (final 16:27; first seen 16:22 at 6472 B, rewritten to 9634 B), P1 16:28, P2 16:29. Two reports (P3, P4) were rewritten after first appearance — observed via mtime/size changes.
- Producer-artifact stability re-check before final scan:
  `find corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md corpus/fixtures/r95-crossing-aftermath corpus/knowledge/r95-aftermath-scope-note.md -printf '%T@ %s %p\n' | sort` snapshotted twice 75 s apart → byte-identical, output `PRODUCER ARTIFACTS STABLE across 75s`.
- Final scans: `git status --porcelain -uall` and `git diff --name-status` at 16:33:39, re-scan at 16:35:06 for churn.

## 1. Tracked modifications — `git diff --name-status` (16:33:39)

```
M	LOG.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py
```

Staged changes: none (`git diff --cached --name-status` empty). `git diff --stat`: 4 files, +215/−13 (LOG.md +57, tools/README.md +20, contract 9 changed, tool +142). No other tracked file is modified.

## 2. Bucketing of all untracked paths — `git status --porcelain -uall`

16:33:39 scan: 1674 entries; 16:35:06 scan: 1712 entries. Buckets:

| Count (16:35:06) | Bucket |
|---|---|
| 3 | B1 declared-producer-modified (`corpus/tools/{map_obligations.py,map-obligations-contract.json,README.md}`) |
| 10 | B2a fixture-new `corpus/fixtures/r95-crossing-aftermath/*` — all declared (entities/relations/contradictions/inspiration-note/source-excerpt + sources/timeline/fictional-excerpts + README/claim-excerpt-map); `ls -la` confirmed no hidden or extra files |
| 1 | B2b knowledge-note-new `corpus/knowledge/r95-aftermath-scope-note.md` |
| 1697 | B3 seat reports/scratch under `.ufo/waves/round-95/` (54 `*.md` reports in `seats/`, 14 `*-scratch/` dirs under `seats/`, `round-95/scratch/V20/` with 4 files) |
| 1 | B4 orchestrator declaration `LOG.md` |
| 0 | OTHER — **none** |

Churn 16:33:39 → 16:35:06: +38 entries, 0 deletions; filtering the diff for any path outside `.ufo/waves/round-95/` returned nothing (grep exit 1). Verifier seats were still landing reports at scan time (54 reports at 16:35:06); all churn confined to B3.

## 3. Transient out-of-bucket observation (repo root) — explained, not persistent

- At ~16:31–16:32 `git status -uall` listed `?? map-obligations-self-test-m1iivb4a/…` — 24 files across 6 case dirs (`complete`, `duplicate`, `malformed_json`, `missing`, `phantom`, `source_id_mismatch`), 4 files each (`claim-excerpt-map.md`, `entities.json`, `relations.json`, `timeline.json`). The dir was actively growing between two parallel scans (`malformed_json` appeared after the first), i.e. a live `--self-test` run.
- By the 16:33:39 scan it was gone; `ls -d map-obligations-self-test-*` → `(none)` at 16:33 and 16:35.
- Cause: `corpus/tools/map_obligations.py:720` — `with tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT) as temporary:`, with `ROOT = Path(__file__).resolve().parents[2]` (line 56) = repo root. Auto-cleans on normal context exit; a killed/interrupted `--self-test` run would leave a repo-root scratch dir. Same construct is inherited from baseline: `git show fb118c4:corpus/tools/map_obligations.py` line 604 is identical.
- Classification: **not** a persistent scope-creep finding — transient, self-cleaning, inherited behavior exercised by the declared `--self-test` verification path. Recorded as an operability observation. Nothing left to clean.

## 4. `__pycache__` under corpus/ (reported, not cleaned)

- Only `corpus/tools/__pycache__/` exists; 3 `.pyc` files, all ignored via `.gitignore:2` (`__pycache__/`) so they never appear in git status.
- Pre-round (16:17): `boundary_doc_check` 14:04:33 / 52190 B; `support_check` 15:41:07 / 24721 B; `map_obligations` 15:42:10 / 52190 B.
- Final (16:35): `map_obligations.cpython-314.pyc` updated in-round → 16:26:32 / 52223 B (recompiled after P1's source edit and subsequent tool runs); the other two unchanged. **No new `.pyc` files appeared.** Reported per instruction; not cleaned.

## 5. `LOG.md` (bucket B4)

`M LOG.md`, +57 lines, content is exactly the `## Round 95 — declaration before dispatch` block (round setup appended by the orchestrator pre-dispatch — the same text my seat brief quotes). Not a seat artifact; classified B4 rather than scope-creep. Adjudicator may confirm the classification.

## Caveats / boundary

- Snapshot boundary: final scan 16:35:06; verifier seats were still landing reports then. All observed churn stayed inside B3. Writes after 16:35:06 are outside this report's window.
- Method limitation: self-cleaning transient writes are only observable when a scan coincides with them; one such (the self-test scratch dir) was caught and is documented above.

Bottom line: PASS — every persistent working-tree path at the 16:35:06 scan falls inside a declared bucket (producer paths / seat reports+scratch / orchestrator LOG.md declaration); no scope-creep found; one transient self-cleaning repo-root self-test scratch dir was observed mid-run and explained (inherited tool behavior); one in-round `__pycache__` `.pyc` update reported, not cleaned.
