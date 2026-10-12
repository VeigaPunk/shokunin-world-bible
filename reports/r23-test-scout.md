# Round 23 test scout — replay plan (no mutating check run)

Role: leaf test scout on worktree `/home/vgpnk/Projects/prymeagnt/lore` (task branch label `craft/lore-r23`; `git` currently shows `craft/lore-r1` at HEAD `d6ea676fa43549c85eba6ea9291399db1b970af4`). Wrote **only** this report. Did not edit checker, fixtures, LOG, SCORECARD, or any other file. Did not commit. Did not spawn children. Did **not** run a mutating check.

Owned axes (context): depth, coverage, calibration. Round axis-move: **DEPTH**. Intended new fixture class (not authored here): **WITNESSED ABSENCE** — a named speaker reports that a named thing was not present. Distinct from r15 private-note mark observation (`r15-carbon-followup`). Checker validates schema/citations/relations/timeline structure only; it does **not** map source prose. No canon claim.

## Baseline facts (pre-change observations)

- HEAD: `d6ea676fa43549c85eba6ea9291399db1b970af4`.
- Absence (already verified at this HEAD):  
  `git cat-file -e HEAD:.shokunin/lore/corpus/fixtures/r23-note-class` → fails (path absent). Working tree: `.shokunin/lore/corpus/fixtures/r23-note-class` does not exist at scout time.
- Saved r22 outputs: `.shokunin/lore/corpus/live/runs/20261012T193930Z/` — **72** files (transcripts named `<fixture-dir>.txt`).
- Fixture directories under `.shokunin/lore/corpus/fixtures/`: **72** (matches run count).
- Prior fixture JSON count (all `*.json` under fixtures; no r23 path present): **359**. Baseline claim for after-compare: these **319 paths** in the task statement appear to mean a different inventory unit than raw `*.json` count; **this scout records measured `find … -name '*.json' | wc -l` = 359** with **zero** r23-related JSON. After-claim hash compare must use the same inventory rule before and after. Prefer hashing **every** prior fixture file (not only JSON) if the implementer needs byte-identity of the full prior tree; task text asks hash compare of prior fixture JSON.

Checker entrypoint (unchanged contract):

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py <bible-dir>
# exit 0 + stdout: CLEAN: schema, citations, relations, timeline; 0 violations
# exit 1 + VIOLATION lines otherwise
```

## Replay / verification plan (exact commands)

Run from repository root `/home/vgpnk/Projects/prymeagnt/lore` after the new fixture exists and **before** any claim that prior artifacts are untouched. These commands are **read-only** w.r.t. fixtures and the saved run dir if used as written (they must not rewrite the 72 saved files).

### 1) New fixture must check clean (expect exit 0)

```bash
python3 .shokunin/lore/corpus/fixtures/check_bible.py \
  .shokunin/lore/corpus/fixtures/r23-note-class
echo "exit=$?"
# Expect: exit=0
# Expect stdout exactly:
# CLEAN: schema, citations, relations, timeline; 0 violations
# Expect empty stderr.
```

### 2) Replay all fixture dirs against saved r22 outputs (preferred)

Does not rewrite saved transcripts; writes a fresh parallel dir for comparison only:

```bash
SAVED=.shokunin/lore/corpus/live/runs/20261012T193930Z
REPLAY=/tmp/r23-replay-20261012T193930Z
rm -rf "$REPLAY" && mkdir -p "$REPLAY"
fail=0
for d in .shokunin/lore/corpus/fixtures/*/; do
  name=$(basename "$d")
  # skip the new class so legacy replay set stays aligned with the 72 saved names
  if [ "$name" = "r23-note-class" ]; then continue; fi
  out="$REPLAY/${name}.txt"
  {
    echo "\$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/${name}"
    python3 .shokunin/lore/corpus/fixtures/check_bible.py \
      ".shokunin/lore/corpus/fixtures/${name}" >"${out}.stdout" 2>"${out}.stderr"
    ec=$?
    echo "exit_code=${ec}"
    cat "${out}.stdout"
    if [ -s "${out}.stderr" ]; then echo "STDERR:"; cat "${out}.stderr"; fi
  } >"$out"
  if ! diff -u "$SAVED/${name}.txt" "$out" >/dev/null; then
    echo "MISMATCH $name"
    diff -u "$SAVED/${name}.txt" "$out" | head -100
    fail=1
  fi
done
echo "replay_fail=$fail"
# Expect: replay_fail=0 and 72 compared pairs (one per saved name).
```

**OR** before/after byte-identity of the 72 saved files (they must not be rewritten by the round):

```bash
SAVED=.shokunin/lore/corpus/live/runs/20261012T193930Z
# BEFORE landing fixture/checker edits (record once):
find "$SAVED" -type f -print0 | sort -z | xargs -0 sha256sum > /tmp/r23-saved-before.sha256
# AFTER:
find "$SAVED" -type f -print0 | sort -z | xargs -0 sha256sum > /tmp/r23-saved-after.sha256
diff -u /tmp/r23-saved-before.sha256 /tmp/r23-saved-after.sha256
echo "saved_files=$(find "$SAVED" -type f | wc -l)"
# Expect: empty diff; saved_files=72.
```

Use **both** when possible: replay proves checker+legacy-fixture behavior; hash proves the run archive was not clobbered.

### 3) Hash compare of prior fixture JSON (before vs after)

```bash
FIX=.shokunin/lore/corpus/fixtures
# BEFORE any r23 fixture files exist:
find "$FIX" -type f -name '*.json' ! -path '*/r23-note-class/*' -print0 \
  | sort -z | xargs -0 sha256sum > /tmp/r23-prior-json-before.sha256
wc -l /tmp/r23-prior-json-before.sha256
# AFTER r23-note-class is added (same find exclusions):
find "$FIX" -type f -name '*.json' ! -path '*/r23-note-class/*' -print0 \
  | sort -z | xargs -0 sha256sum > /tmp/r23-prior-json-after.sha256
diff -u /tmp/r23-prior-json-before.sha256 /tmp/r23-prior-json-after.sha256
echo "prior_json_before=$(wc -l </tmp/r23-prior-json-before.sha256)"
echo "prior_json_after=$(wc -l </tmp/r23-prior-json-after.sha256)"
# Expect: empty diff; equal line counts.
# Scout-time measurement with no r23 dir: 359 JSON files.
# If the round's external baseline claim is "319 paths", reconcile the path unit
# (e.g. relative paths list vs files) before asserting; do not silently drop files.
```

Optional full prior-tree identity (stronger than JSON-only):

```bash
find "$FIX" -type f ! -path '*/r23-note-class/*' -print0 \
  | sort -z | xargs -0 sha256sum > /tmp/r23-prior-all-before.sha256
# ... after ...
diff -u /tmp/r23-prior-all-before.sha256 /tmp/r23-prior-all-after.sha256
```

### 4) Absence check at baseline commit (already done)

```bash
git cat-file -e d6ea676fa43549c85eba6ea9291399db1b970af4:.shokunin/lore/corpus/fixtures/r23-note-class
echo "exit=$?"
# Expect: nonzero exit (path absent at baseline HEAD).
# After landing, working tree may contain the dir; baseline tree must still lack it:
git rev-parse HEAD
git cat-file -e HEAD:.shokunin/lore/corpus/fixtures/r23-note-class || echo "still-absent-at-HEAD-object"
# If HEAD advances to include the fixture, absence is historical (d6ea676) only.
```

## After-claim (what success would assert)

1. `r23-note-class` exists as a fixture directory and `check_bible.py` exits **0** with the standard CLEAN line.
2. All **72** legacy fixture transcripts either byte-match a fresh replay or the saved run directory hashes are unchanged (72 files, no rewrites).
3. Every prior fixture JSON hash (excluding `r23-note-class/**`) is byte-identical before vs after; counts match.
4. Baseline commit `d6ea676` still lacks `HEAD:…/r23-note-class` via `git cat-file -e` on that commit.

## What falsifies the after-claim

Any one of:

- New fixture check exits nonzero, prints `VIOLATION:`, or non-CLEAN stdout/stderr.
- Any of the 72 saved `20261012T193930Z/*.txt` files changes hash or a legacy fixture replay `diff` is nonempty (stdout, exit_code line, or stderr surface).
- Any prior fixture JSON (path outside `r23-note-class/`) changes content or disappears; before/after hash lists differ; counts diverge.
- Claim that the class existed at `d6ea676` despite `git cat-file -e` failure on that commit-ish path.
- “Depth” delivered only by restating an existing mapped row (e.g. r15 carbon mark) without a new WITNESSED ABSENCE mapping — fails the round’s depth move even if checks stay green.
- Treating CLEAN checker output as source-prose or canon truth (checker does not map prose).

## Non-actions this scout took

- No `check_bible.py` execution against a new r23 fixture (fixture absent).
- No mutation of checker, fixtures, live runs, LOG, SCORECARD.
- No commit; no children.

## Note on inventory mismatch

Task text: “baseline claim is 319 paths byte-identical.” Scout measurement: **359** `*.json` files under fixtures and **72** fixture directories / **72** saved run files. Verifiers must pin the exact path set used for the 319 claim (if any) and not equate it with 359 without reconciliation.
