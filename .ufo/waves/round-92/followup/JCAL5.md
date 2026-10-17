# JCAL5 — method-varied census (seed 9201, regenerated baseline)

Seat: JCAL5 (round-92 follow-up wave, world-bible lane). Delivered tree: `c4d4823` (judgment surface; `git status --porcelain` shows no tracked modifications). Baseline: `396c568`.
Receipt: `.ufo/waves/round-92/followup/JCAL5-delta.json` (85,839 bytes, SHA-256 `deef24821abbca49af388ec7b79296351080089d8b333f2dbb3b7636744ee4c5`, `json.tool` parse PASS).

## Work performed

Axes: **reproducibility of the r92 census claim**, **evidence integrity**, **calibration of the r92 path-convention note**, **no-harm**.

Method variation from B1/B2: the baseline was **regenerated from `396c568` blobs** (per-fixture `git archive` extract → run → delete; the checker extracted once — never trusted from the B1/B2 receipts), the delivered census ran on the committed `c4d4823` tree, driver and every checker subprocess under `python3 -I` with repo-relative `corpus/fixtures/<name>` argv and cwd = repo root; iteration order = 166 direct child dir names shuffled with `random.Random(9201)`, plus a replicate with seed 9401. Discovery was cross-checked two ways (`pathlib.iterdir` vs `os.scandir`). Four all-166 arms varied the argv spelling (`absolute`, `./`-prefix, `corpus/./fixtures`, `corpus//fixtures`, `../lore-shokunin/`-prefix) and one five-fixture arm used a trailing slash — this calibrates the r92 README/C9-watch path-convention note. Receipts were cross-checked against the committed `patches/B1-tuples.json`/`B2-tuples.json` and, read-only, against peer `followup/H4-census.json` and `followup/JCAL1-delta.json`.

Dependency wait-checks (per seat protocol): first 60 s check **hit** — `POLL_HIT t=60s peer_artifacts='H4-census.json H4-probes.json JCAL1-delta.json'` (helper early-exit semantics, as r90-B1 precedent); the second check ran at t=120 s as a directory snapshot (`POLL_CHECK t=120s`; 20 files incl. `JCAL1.md`, `JDEP1.md`, `JDEP4.md`, `JCAL2.md`). No gap in needed evidence.

Exact driver command (heredoc, run twice — second generation added the C4–C6 arms; the final 85,839-byte receipt is from the complete run, no partial states left):

```sh
cd lore-shokunin && PYTHONDONTWRITEBYTECODE=1 python3 -I - <<'PY'  # driver: see JCAL5-delta.json keys for full logic
PY
```

## Before → after measurements

**Tree and checker identity.** `git rev-parse HEAD` → `c4d4823b9a8165a88e8199af136e62d6e961b6b9`; `git status --porcelain` → only `?? .ufo/waves/round-92/followup/…` entries (zero tracked modifications, before and after the runs). Checker: delivered worktree = `git show 396c568:` = extracted baseline = C9 pin `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; the pin string is present in both `corpus/fixtures/README.md` and `corpus/knowledge/r91-c9-watch.md`. Direct fixture dirs: 166 at `396c568` and 166 at `c4d4823` (git tree count); `iterdir` == `scandir` sets.

**Regenerated baseline (A) vs delivered (B), seeded order 9201** (`order_sha256=e8e665aa82de0c0a…`, first8 `['r87-probe-multi-invalid','r22-mixed-first','r59-duplicate-harbor-tower','r91-c1-tick-unresolved','r9-unique-control','r61-direct-nonarray','item-chain-valid','r16-missing-first']`):

```text
A_baseline  dirs=166 exits={0:32, 1:134} violations=421 stderr_nonempty=0
B_delivered dirs=166 exits={0:32, 1:134} violations=421 stderr_nonempty=0
D_replicate seed=9401 mismatches_vs_B=[]           (order_sha256=51c8fa15fb58a38c…)
DELTA_AB shared=166 changed_shared=[] added=[] removed=[]
```

So the r92 claim **"Census: 166 dirs, 0 changed"** reproduces under a regenerated baseline and a shuffled order: 0 changed / 0 added / 0 removed, 0 stderr bytes anywhere.

**Cross-checks vs committed receipts:** B vs B1 `0` mismatches, B vs B2 `0`, A vs B1 `0`, A vs B2 `0`, A vs B `0` (all 166, triple fields). B1 and B2 are byte-identical and committed at HEAD. Canonical digest `sha256(json.dumps({path:{exit,stdout_sha256,violation_count}}, sort_keys=True, separators=(',',':')))`:

```text
canonical_A = canonical_B = a92a4f222804db5cbdc88a558568aa81cc62f459f2aa6b6a7981400c455203df
B1 dict digest matches; JCAL1 census_canonical_sha256 == same value (canonical_equal=true)
```

**Cross-seat (read-only snapshot at run time):** `H4-census.json` (file sha256 `377a3e7c…`, head `c4d4823`, 166 rows) — 0 tuple mismatches vs my A rows and 0 vs my B rows. `JCAL1-delta.json` (file sha256 `0e673837…`) — 166 dirs, exits {0:32, 1:134}, 421 violation lines, same canonical digest; its verdict ("unchanged") is consistent with mine.

**Path-convention arms (stdout hash vs B; exit/violation/stderr changes were empty in every arm):**

```text
C1 absolute  all-166: changed=5  == the five named fixtures; exit_changes=[] violation_changes=[] stderr_changes=[]
C6 ../lore-shokunin/ prefix all-166: changed=5 == the five; exit_changes=[] ...
C2 ./ prefix all-166: changed=0
C4 corpus/./fixtures all-166: changed=0
C5 corpus//fixtures  all-166: changed=0
C3 trailing slash (five): changed=0 of 5
```

The five: `r5-missing-file`, `r62-missing`, `r67-claim-source-unavailable-{control,empty,whitespace}`. Example (r5-missing-file, old → new under C1):

```text
- … No such file or directory: 'corpus/fixtures/r5-missing-file/contradictions.json'
+ … No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r5-missing-file/contradictions.json'
```

exit stays 1 and the violation count stays 1; the same fixture under `./`-prefix and trailing slash renders the identical old string (normalized). Mechanism: `check_bible.py:420` parses argv as `type=Path` and `check_bible.py:49/53` echo the `Path` rendering, so `./`, inner `./`, `//`, and trailing-slash spellings normalize away; absolute and `../`-prefixed forms survive.

**File-level diff `git diff --raw 396c568 HEAD -- corpus/fixtures`:**

```text
M corpus/fixtures/README.md
M corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
```

Both are documentation/map files the checker never reads; no fixture JSON or checker bytes changed — this, with the pinned checker, explains the 0-tuple delta.

## Findings & named debt

- **The r92 census claim is reproduced under a fourth method** (regenerated `git archive` baseline, seeded shuffle + replicate, five spelling arms) with exact row-level agreement to B1/B2 and to peers H4 (rows) and JCAL1 (canonical digest). Verdict for this seat's mandate: confirmed, no drift, evidence broadened.
- **Calibration finding — the path-convention note's wording is overbroad.** README/C9-watch say "absolute or differently prefixed paths alter stdout". Measured: only *absolute* and *`../`-prefixed* spellings alter the five stdout hashes; `./`-prefix, `corpus/./fixtures`, `corpus//fixtures` and a trailing slash change **nothing** (0/166), because argv is a `Path` and its rendering is normalized. The operational instruction ("keep the repo-relative spelling when replaying the manifests") remains correct and was honored. **Named debt:** reword the note next round to "absolute paths (and any prefix pathlib does not normalize away, e.g. `../`)", or add the same `./`-normalization bound; not repaired here — this seat has no authorized write to `corpus/`.
- **Tuple-level scope (carried, same as r91):** the census is output-level; it is deliberately blind to the two modified `.md` files above. "0 changed" must not be read as "no file changed".
- **Wait-check note:** dependency satisfied at the first 60 s check (early exit); the second t=120 s snapshot is recorded above. Peer artifacts were still landing (JCAL1.md, JDEP1/4 appeared between the two checks) — the snapshot is a point-in-time comparison only.
- **Method honesty:** the first delta generation (78,318 bytes) covered arms A–D + C1–C3; it was wholly regenerated with the C4–C6 arms added, and only the final 85,839-byte file remains. Scratch (`/tmp/lore-r92-JCAL5`, `/tmp/lore-r92-JCAL5v2`) cleaned; extraction was per-fixture to respect `/tmp` inode pressure (15,481 free at preflight). No tracked file written by this seat beyond the two follow-up artifacts; no commit, no push; no `l0-questions.md` write.

## Handoff

- Artifacts: `.ufo/waves/round-92/followup/JCAL5.md` (this file) and `.ufo/waves/round-92/followup/JCAL5-delta.json` — full A/B rows (166 each), D replicate, all spelling arms (changed rows with old/new lines), cross-checks, canonical digests, cross-seat snapshot, file-level diff, seed/order receipts.
- For the r92 landing record: the census claim "166 dirs, 0 changed" stands — verified by regenerated baseline + seed-9201 shuffle + seed-9401 replicate + spelling arms, 0 mismatches vs B1/B2, and cross-seat row-level agreement (H4) and canonical-digest agreement (JCAL1).
- Open item for the round's own docs: the path-convention note's "differently prefixed" clause is inaccurate (`./`-prefixed and trailing-slash spellings do not alter stdout; absolute and `../` do). Nothing else within the mandate is left unverified.