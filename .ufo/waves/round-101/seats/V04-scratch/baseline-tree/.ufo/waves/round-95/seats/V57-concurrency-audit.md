# V57 — concurrency-audit (round 95)

Seat: V57 concurrency-audit. Scope per seat spec: after all seats land, survey
for any seat writing outside its declared paths (git status as ground truth);
confirm report-path exclusivity (no two seats share a file).

Baseline: HEAD `fb118c4` (r94 closure). Audit window 16:18:20 → 17:02:43 (-03);
terminal snapshot `2026-10-17T17:00:17-03:00` (`/tmp/v57-scratch/audit-final.txt`).

Method (all this seat's scratch under `/tmp/v57-scratch/`, zero repo footprint):

- watcher 1: `git status --porcelain=v1` every 20 s, 129 polls
  (`/tmp/v57-scratch/timeline.log`);
- watcher 2: sha256 of every `.ufo/waves/round-95/seats/*.md` every 20 s
  (`/tmp/v57-scratch/rep-hashes.log`) — overwrite/deletion detector;
- terminal mtime surveys (`find -newermt '2026-10-17 16:10'`) and byte
  compares (`cmp -s`) at audit time.

## 1. Write conformance — PASS

Terminal `git status --porcelain=v1` (17:00:17, re-confirmed 17:02:43):

```
 M LOG.md
 M corpus/tools/README.md
 M corpus/tools/map-obligations-contract.json
 M corpus/tools/map_obligations.py
?? .ufo/waves/round-95/
?? corpus/fixtures/r95-crossing-aftermath/
?? corpus/knowledge/r95-aftermath-scope-note.md
```

Classification against declared ownership (r95 LOG.md declaration):

| path | declared owner | evidence |
|---|---|---|
| LOG.md (+57-line declaration diff) | L1, pre-dispatch | mtime 16:09:57, already `M` in first poll 16:18:20, unchanged through 17:02:43 |
| corpus/tools/map_obligations.py | P1 | mtime 16:26:27 |
| corpus/tools/map-obligations-contract.json | P2 | mtime 16:27:02 |
| corpus/tools/README.md | P2 | mtime 16:28:26 |
| corpus/fixtures/r95-crossing-aftermath/ (10 files) | P3 (8) + P4 (2) | created 16:18:01–16:21:27 |
| corpus/knowledge/r95-aftermath-scope-note.md | P5 | mtime 16:25:15 |
| .ufo/waves/round-95/ | seat reports + scratch | see §2 |

- Distinct `git status` lines across the whole 129-poll window = the 7 lines
  above + the 6 transient entries in §1.1 — no other path ever appeared; no
  `D`/`R` status ever observed.
- Repo-wide mtime survey (excluding `.git` and `.ufo/waves/round-95`): only the
  corpus paths above; no other wave round (r87–r94) and no non-corpus file was
  touched at any poll.
- Fixture set is exactly the declared 10 files. `cmp -s` vs `r94-paired-crossing`:
  SAME (5 byte copies): contradictions.json, entities.json, inspiration-note.md,
  relations.json, source-excerpt.md; DIFF (3 modified per spec):
  fictional-excerpts.md, sources.json, timeline.json; NEW (2, P4): README.md,
  claim-excerpt-map.md. No extra files.
- `git diff --stat HEAD -- corpus` → only `corpus/tools/README.md` (+20),
  `corpus/tools/map-obligations-contract.json` (9 ±), `corpus/tools/map_obligations.py`
  (142 ±; total 158 insertions, 13 deletions).
- Machine artifact: `corpus/tools/__pycache__/map_obligations.cpython-314.pyc`
  regenerated 16:26:32 by tool execution; gitignored (`.gitignore:2:__pycache__/`),
  not part of the delivered revision; the directory pre-existed at round start.

### 1.1 Transient observation — `map-obligations-self-test-*/` at repo root

Six untracked temp dirs appeared transiently at repo root (each visible at
exactly one 20 s poll; none present at final audit):

```
poll  9 16:21:01 map-obligations-self-test-pevhytt0/
poll 12 16:22:01 map-obligations-self-test-v6evuk24/
poll 28 16:27:21 map-obligations-self-test-llb0lloe/
poll 30 16:28:01 map-obligations-self-test-dzwk_cuh/
poll 39 16:31:01 map-obligations-self-test-sdcd95bh/
poll 43 16:32:21 map-obligations-self-test-sde01bj7/
```

Cause (code evidence, not speculation): `map_obligations.py` runs its self-test
inside `with tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`
with `ROOT = Path(__file__).resolve().parents[2]` = repo root — present at HEAD
line 42 and delivered line 720. So every prescribed
`python3 corpus/tools/map_obligations.py --self-test` run briefly creates and
then removes a temp dir in the repo root. Pre-existing at baseline and
self-cleaning: each observed dir vanished within ≤40 s, zero leftovers at
17:00:17 and 17:02:43. Not a persistent out-of-path write; noted as a litter
risk only if such a run is SIGKILLed mid-test. (This seat did not execute the
tool; conclusion rests on code inspection plus the observed lifetimes.)

## 2. Report-path exclusivity — PASS (landed set)

At 17:02:43: 59 seat reports; 59 distinct seat IDs; zero duplicates. Expected
non-auditor set = 63 (P1–P5 + V01–V59 minus V57) → **ABSENT: V09, V18, V33,
V59** (V59 has an active `V59-scratch/` — `watch.txt` written 17:01,
`collection-curve.txt` 16:57, i.e. work in flight; V09/V18/V33 leave no trace
anywhere, including no scratch dir and no partial repo write).

- Self-ID check (`head -4 | grep -E "\b$id\b"`): 59/59 OK, 0 mismatch.
- No shared/duplicated file: 59 distinct files ever seen = 59 present; report
  count monotonic 1→59 across the 129 polls (never decreased); no report was
  deleted or re-created.
- Overwrite check: 23 reports show hash churn over time (max `V31-debt.md` 11
  distinct hashes; `V29-adjudicator.md` 6; `V20-doc-parity.md` 6) — all
  consistent with single-author incremental editing; every churned file's final
  content self-identifies as its own filename's seat. No evidence of a second
  writer. Residual limitation: an overwrite that preserved both path and
  self-ID would be undetectable from the filesystem, and no observation
  suggests one occurred.
- Non-report artifacts in `seats/`: `V31-debt.json` (structured ledger,
  `"seat": "V31"`; matches r94 `F29-debt.json` precedent) and
  `V23-scratch-poll.sh` (V23 poll helper). Scratch dirs, 15 total:
  `seats/scratch` (V14), `V01/V04/V06/V16/V23/V32/V34/V37/V39/V40/V44/V52/V55/V59-scratch`,
  plus `waves/round-95/scratch/V20`. All inside the round-95 tree; zero
  tracked-file impact.

## 3. Incidental

- `.ufo/waves/round-95/` grew to 1706 files, dominated by scratch fixtures
  (V14 dry/probe sets, V20 census copies) — all within the wave tree.
- LOG.md unchanged since 16:09:57 (diff still exactly +57 declaration lines);
  no seat appended to it.

Bottom line: PASS — every observed write stayed inside declared ownership paths
(the transient, self-cleaning `--self-test` temp dirs at repo root are
tool-inherent and pre-existing at baseline), report paths are exclusive across
all 59 landed seats, and 4 verifier seats (V09, V18, V33, V59) were ABSENT at
audit time with no partial repo writes attributable to them.
