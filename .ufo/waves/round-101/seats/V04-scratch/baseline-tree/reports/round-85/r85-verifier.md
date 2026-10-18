# Round 85 — non-author verifier report (host: devin)

Scope: independent re-verification of the mechanical claims in
`.shokunin/lore/reports/round-85/r85-author.md`. I did not author round 85 and
do not mark axis verdicts; this is raw-evidence agreement/disagreement only.

## Claim 1 — checker mechanism (AGREE)

Re-read `.shokunin/lore/corpus/fixtures/check_bible.py` lines 202-247:

- L212-214: `to_holder` resolving to **zero** rows →
  `dangling entity` diagnostic + `valid = False`.
- L215-216: `to_holder` resolving to **>1** rows → `valid = False` with **no
  appended error** (silent).
- L220-222: non-null `from_holder` resolving to **zero** rows →
  `dangling entity` diagnostic + `valid = False`.
- L223-224: non-null `from_holder` resolving to **>1** rows → `valid = False`,
  silent.
- L234-237: `if not valid:` resets `previous_holder`/`previous_tick` AND sets
  `can_check_chain = False` before `continue` — chain comparison is disabled
  for **all later records of that item**, not only the offending record.

Confirmed exactly as reported. Contrast confirmed: sources (L108), relation
endpoints (L167-168), timeline actor (L279), place (L281), dependency (L313)
all emit local `ambiguous ...` findings; the two holder sites are the only
silent `valid = False` ambiguity branches.

## Claim 2 — strict matched pair (AGREE)

Probe inputs under
`.shokunin/lore/corpus/live/runs/round-85/probe-inputs/` already exist (I did
not recreate them; I verified and re-ran them in place).

- `diff r85-masked-ambiguous/entities.json r85-unique-break-control/entities.json`
  → `81,92d80`, exactly **12** `>`/`<` lines: one duplicated `vault` object.
  The four non-entities files are `cmp -s` byte-identical between the pair;
  provenance records identical in both (`[0] null→mira`, `[1] mira→vault`,
  `[2] harbor→tower`).
- Independent run, stderr captured separately:

| probe | exit | stdout |
|---|---|---|
| `r85-unique-break-control` | 1 | `VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'` + `1 violation(s); no canon changed` |
| `r85-masked-ambiguous` | 1 | `VIOLATION: entities[5].id: duplicate entities id 'vault'` + `1 violation(s); no canon changed` |

In the masked run the `provenance[2]` chain break is **entirely absent** — no
line anywhere reports it. stderr empty in both runs. Matches the author table
byte-for-byte (modulo the `VIOLATION: ` prefix the report elides).

## Claim 3 — `r85-harbor-repro` (AGREE)

- `entities.json`: `harbor` appears twice (ids list
  `['mira','harbor','tower','seal','harbor']`); `seal` provenance consumes it
  at `provenance[1].to_holder='harbor'` and `provenance[2].from_holder='harbor'`;
  `timeline.json` place_ids `['harbor','tower']`.
- Run: exit 1, **2** violations, stderr empty:

```
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
```

The timeline site reports `ambiguous place entity 'harbor'` while both
provenance holder references to the same duplicated id report nothing —
single-run asymmetry confirmed.

## Claim 4 — baseline replay + pin (AGREE)

- HEAD `3f601981b1a28299c0b5498d6070584f26de3428`.
- `git ls-tree -r 596f70e --name-only -- .shokunin/lore/corpus | wc -l` →
  **1368**; `git diff --stat 596f70e HEAD -- .shokunin/lore/corpus` → empty.
  `git status --porcelain` shows only untracked `corpus/live/runs/round-85/`
  and `reports/round-85/` additions — no modified/deleted tracked corpus file.
  Since the diff covers content, all 1,368 pinned files are byte-identical
  (not merely a sample). Checker sha256 at pin and worktree both
  `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.
- I independently replayed all **133** fixture dirs root-relative
  (`python3 .shokunin/lore/corpus/fixtures/check_bible.py
  .shokunin/lore/corpus/fixtures/<name>`, stdout/stderr captured separately,
  outputs in `/tmp/r85-verify/`): **28 exit0 / 105 exit1**, stderr empty for
  all 133 — matches the r84 pin and the author claim.
- Tuple-for-tuple comparison of my 133 `(exit_code, stdout)` tuples against
  the author's recorded `corpus/live/runs/round-85/<fixture>.txt`:
  **0 mismatches** (author files interleave `exit_code` before stdout;
  compared semantically).

## Claim 5 — `r85-isolated-ambiguous` collateral check (AGREE)

`vault` count = 2; the only consumer is `provenance[2].to_holder='vault'`
(no `vault` reference in timeline/relations/contradictions/sources). Output is
the single `entities[5].id: duplicate entities id 'vault'` line — no
provenance-local finding, no other collateral, matching the report. `r85-control`
exits 0 `CLEAN`.

## Disagreements

None on any mechanical claim. Note (presentation, not substance): the report's
probe table shows violation text without the literal `VIOLATION: ` output
prefix; raw lines above carry it.

## UNKNOWNs (verifier)

- Whether the author's probe dirs were constructed exactly as described
  (`item-chain-valid` clones): I verified the *resulting* inputs and outputs,
  not the construction steps; `r85-control` equals a clean `item-chain-valid`
  run and the non-entities files are byte-identical across probes, consistent
  with the claim.
- The falsifier's operator-action prong (whether a non-author operator
  actually repairs differently given a local `ambiguous entity` line) is
  untested here by design — left to the sealed reviewer wave.
- I did not diff probe-input JSON against `fixtures/item-chain-valid` row by
  row beyond the confirmed seeded differences; the four non-entities files
  were verified byte-identical across all five probes.

## Commands (verbatim)

```
git rev-parse HEAD ; git diff --stat 596f70e HEAD -- .shokunin/lore/corpus
git ls-tree -r 596f70e --name-only -- .shokunin/lore/corpus | wc -l   # 1368
sha256sum .shokunin/lore/corpus/fixtures/check_bible.py                # 88c9b1d0...
git show 596f70e:.shokunin/lore/corpus/fixtures/check_bible.py | sha256sum  # same
python3 .shokunin/lore/corpus/fixtures/check_bible.py \
  .shokunin/lore/corpus/live/runs/round-85/probe-inputs/<probe>  # x5, stdout/stderr separate
diff probe-inputs/r85-masked-ambiguous/entities.json \
     probe-inputs/r85-unique-break-control/entities.json          # 81,92d80 (12 lines)
for d in .shokunin/lore/corpus/fixtures/*/; do
  python3 .shokunin/lore/corpus/fixtures/check_bible.py "$d"      # 133 replays -> /tmp/r85-verify
done                                                              # 28 exit0 / 105 exit1, stderr empty
cmp -s on all non-entities probe files; tuple compare vs author *.txt # 0 mismatches
```

No commit, no corpus/checker/LOG/SCORECARD/verdict edits; my replay artifacts
live only in `/tmp/r85-verify/` and `/tmp/r85-*.out|.err`.
