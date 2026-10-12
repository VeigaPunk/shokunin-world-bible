# r23 independent verifier (non-author)

Repo: `/home/vgpnk/Projects/prymeagnt/lore`  
Baseline commit: `d6ea676fa43549c85eba6ea9291399db1b970af4`  
Verifier role: non-author replay and path compare only.  
No claim of source-text truth or canon.  
Did not edit fixtures, checker, LOG, or SCORECARD. Did not commit. Did not spawn.

## 1. check_bible on r23-note-class

Command:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r23-note-class
```

- exit code: `0`
- stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

## 2. Live transcript replay (72 runs)

Directory: `.shokunin/lore/corpus/live/runs/20261012T193930Z/`  
File count: **72**

Saved format per file: line 1 `$ <command>`, line 2 `exit_code=N`, remainder = stdout (byte-compared including trailing newline).

Replay method: re-run each saved command via `subprocess` from repo root; compare exit code and stdout to the saved body after the `exit_code` line.

| metric | value |
|---|---|
| transcripts | 72 |
| exact match (exit + stdout) | **72** |
| mismatches | **0** |

## 3. Fixture JSON vs baseline `d6ea676`

Measured with `git ls-tree -r --name-only d6ea676 -- .shokunin/lore/corpus/fixtures` and byte compare of each baseline `*.json` to the working tree via `git show d6ea676:<path>`.

| metric | count |
|---|---|
| baseline fixture files (all types) | 364 |
| baseline JSON paths | **359** |
| working-tree JSON under fixtures | 364 |
| baseline JSON same as working tree | **359** |
| baseline JSON content-changed | **0** |
| baseline JSON missing in working tree | **0** |
| working-tree JSON not in baseline | **5** (all under `r23-note-class/`) |

New JSON paths (not in baseline; expected for this round’s pack):

- `.shokunin/lore/corpus/fixtures/r23-note-class/contradictions.json`
- `.shokunin/lore/corpus/fixtures/r23-note-class/entities.json`
- `.shokunin/lore/corpus/fixtures/r23-note-class/relations.json`
- `.shokunin/lore/corpus/fixtures/r23-note-class/sources.json`
- `.shokunin/lore/corpus/fixtures/r23-note-class/timeline.json`

Note: prior r22 report cited 319 baseline JSON paths; **this baseline tree measures 359 JSON paths** (364 fixture files). Count used here is the measured 359.

## 4. Absence of r23-note-class at baseline

```text
git cat-file -e d6ea676fa43549c85eba6ea9291399db1b970af4:.shokunin/lore/corpus/fixtures/r23-note-class
```

- exit code: `128`
- stderr: `fatal: path '.shokunin/lore/corpus/fixtures/r23-note-class' exists on disk, but not in 'd6ea676fa43549c85eba6ea9291399db1b970af4'`

Confirmed: path **absent** in baseline commit (present only on disk as new work).

## 5. Excerpt and clause map (non-author trace)

Files read:

- `.shokunin/lore/corpus/fixtures/r23-note-class/sella-absence-note-excerpt.md`
- `.shokunin/lore/corpus/fixtures/r23-note-class/witnessed-absence-clause-map.md`
- supporting JSON: `entities.json`, `timeline.json`, `sources.json`, `relations.json`, `contradictions.json`

Excerpt (authored fixture prose, not recovered evidence per its own header):

> Later at Lantern Harbor, I, Sella, looked for Mira’s outbound route strip on the registry hook rack. I did not find it there.

### Clause → fixture field (verifier judgment)

| clause | map says | non-author can trace? |
|---|---|---|
| Later | `timeline` entry `strip-absence-note` tick 3, `depends_on: ["departure"]` | **Yes** — order fields exist; map correctly labels this as fixture order only, not a clock/duration fact |
| at Lantern Harbor | `timeline[strip-absence-note].place_id` = `harbor`; entity `harbor` name Lantern Harbor | **Yes** |
| I, Sella | `timeline[...].entity_id` = `sella`; entity name Sella | **Yes** — identity inside this pack only |
| looked for Mira’s outbound route strip on the registry hook rack | `entities` claim on `sella` + timeline description | **Yes** — same wording appears in claim/description; strip is not its own entity row (map states that) |
| I did not find it there | same claim/description | **Yes** — non-finding predicate is in those fields |
| (no cause) | none / must-not-imply | **Yes as negative** — no cause field or causal wording in claim/description/relations |
| (no proof of world-absence) | `sources[sella-absence-note].reliability_note` | **Yes** — reliability_note states report ≠ proof of absence |
| (no Blue Seal link / no mark / carbon) | none | **Yes as negative** — see below |

### Mark / Blue Seal / cause

- Excerpt text: **does not** mention a mark, carbon, or Mira’s Blue Seal; **does not** state a cause for the non-finding.
- Clause map: explicitly classes this as **witnessed absence**, distinguishes r15 mark observation, and marks cause / Blue Seal / mark / carbon as deliberately unmapped.
- Fixture JSON: Mira/Blue Seal appear only via separate `courier-log`-sourced entity/relation rows (`mira` carries `seal`). The `sella` claim, `strip-absence-note` timeline description, and `sella-absence-note` reliability_note **do not** attribute a mark to Mira’s Blue Seal and **do not** state a cause (theft, removal, motive, etc.).
- `contradictions.json` is `[]`. `relations.json` has only `mira`→`seal` `carries` from `courier-log`.

**Verdict (traceability only):** As non-author, each positive excerpt clause has a clear fixture field landing; negative constraints (no cause, no Blue Seal/mark attribution for this note) hold in the excerpt, clause map, and JSON inspected. This is structural/fixture consistency only — **not** source-text or canon truth.

## Summary counts

| check | result |
|---|---|
| check_bible r23-note-class | exit **0**, CLEAN, 0 violations |
| transcript exact matches | **72 / 72** |
| baseline JSON paths measured | **359** |
| baseline JSON same | **359 / 359** |
| baseline JSON changed | **0** |
| new JSON (r23-note-class) | **5** |
| cat-file baseline path | **fails** (exit 128; absent in d6ea676) |
| clause trace (non-author) | positive clauses traceable; no cause; no mark→Blue Seal attribution in note class fields |

## Limits

- Did not re-author or mutate any fixture or checker code.
- Did not validate literary/canon truth of any source string.
- Working tree HEAD short hash observed during run: `d6ea676` (same as baseline label in this workspace snapshot).
