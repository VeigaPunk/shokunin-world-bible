# Round 37 regression-scout plan

## Scope and evidence

This is a replay plan, not a claim that replay has already passed. LOG r37 pins the baseline work commit to `95e7203270045f26e9beb2fcc37269563ef8acec` and report commit to `4e5dacf413d727595aec80ffc1f2e0e2a17f4f84` (`.shokunin/lore/LOG.md:595`). It requires exact prior CLI outcomes for 88 fixtures and byte identity for 439 prior JSON paths (`.shokunin/lore/LOG.md:596`). Use repository-root-relative paths and run from repository root; this avoids the path/cwd artifact documented for r35 (`.shokunin/lore/LOG.md:565`).

Relevant checker behavior: schema-valid timeline rows are indexed by ID; duplicate IDs emit a finding and overwrite the index (`.shokunin/lore/corpus/fixtures/check_bible.py:45-51`). Separately, every admitted timeline event contributes to `event_id_counts` (`check_bible.py:60-62`). For each ledger endpoint, count other than one emits the endpoint-local `expected exactly one timeline event` finding and skips event resolution (`check_bible.py:77-100`). Thus the duplicate's last-wins index is not used to certify this endpoint: its count guard makes endpoint identity ambiguous. r9 already demonstrates duplicate timeline IDs and a dependent consumer (`r9-dup-low-high/timeline.json:1-31`); it does not contain a ledger row (`r9-dup-low-high/contradictions.json` is empty). The r35 positive pair points `claim_a` to `tarin-envelope-observation` and `claim_b` to `sella-bell7-presence` (`r35-bell7-conflict/contradictions.json:1-14`); its corresponding events and citations are at `r35-bell7-conflict/timeline.json:16-39`.

## Pinned replay procedure

Pin and validate baseline availability first:

```sh
git cat-file -e 95e7203270045f26e9beb2fcc37269563ef8acec^{commit}
git cat-file -e 4e5dacf413d727595aec80ffc1f2e0e2a17f4f84^{commit}
```

Use the baseline checker bytes from the pinned work commit, not the working-tree checker. In a temporary directory, materialize `check_bible.py` with `git show 95e7203270045f26e9beb2fcc37269563ef8acec:.shokunin/lore/corpus/fixtures/check_bible.py`; enumerate the 88 baseline fixture directories and 439 tracked JSON paths from that same commit. For every fixture, invoke from repo root with root-relative argv, e.g. `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent`, capturing stdout, stderr, and exit status separately. Compare each tuple to the pinned-baseline capture; do not compare rendered absolute-path diagnostics from a different cwd. Hash or byte-compare every enumerated JSON path against its baseline blob. Report counts and list any mismatch rather than treating a partial loop as a pass.

For final-current verification, repeat the identical root-relative invocation and path inventory against the unchanged pre-r37 fixture tree; exclude only the newly introduced r37 fixture directory from current fixture enumeration. Do not edit fixtures or checker in this scout task. If the r37 pair is later created, test it separately from the 88-regression set: clean control must exit 0; duplicate case must have the exact full output inventoried, not merely the two predicted findings. Expected minimum negative findings are duplicate `timeline[4].id` and ambiguous `contradictions[0].claim_a.event_id`, as LOG specifies (`LOG.md:596`).

## Risks and falsifiable check

- Baseline pin may be unavailable or checkout may contain uncommitted prior changes; fail/stop the replay rather than silently substitute HEAD.
- Relative-path output makes cwd part of the evidence. Both baseline and current commands must run at repository root with the same argv spelling.
- The checker’s duplicate index overwrite could tempt a reader to select a row. The ledger count guard prevents endpoint resolution here; do not describe either row as the selected account or resolve canon.
- A duplicate ID makes this ledger endpoint ambiguous, not either testimony false. The two accounts and citations remain narrative material; no conclusion about truth or a canon winner follows. This distinction is required by LOG (`LOG.md:596`).
- Preserve exact stderr and exit code as well as stdout; distinguish CLI tuple equality from JSON byte equality. Include counts (88/88 and 439/439) and explicit zero-mismatch results.

Falsifiable acceptance: pinned baseline and current root-relative runs yield identical stdout/stderr/exit tuples for all 88 pre-existing fixture directories, and all 439 pre-existing JSON paths match byte-for-byte; any mismatch, missing path, altered cwd/argv, or incomplete count fails this regression check. The proposed r37 negative case separately must show both its duplicate-row and ledger-local endpoint-count diagnostics while the unique control is clean. This establishes coverage of an ambiguous ledger endpoint beyond r9’s duplicate-ID-without-ledger case, without implying false testimony or canon resolution.
