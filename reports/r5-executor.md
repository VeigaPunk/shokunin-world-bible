# Round 5 executor — non-author replay and measurement protocol

## Purpose and boundary

This is a replay protocol, not a result table. A verifier who did not author the fixtures or expected classifications should run it from the repository root, capture raw results, and report measurements before comparing them with the expected classes below. Do not edit the checker, fixtures, table, or expected classifications to make a mismatch disappear. Do not infer that the checker crashes merely from exit 1; record stderr, traceback, and normal violation summary separately.

The active checker is `.shokunin/lore/corpus/fixtures/check_bible.py`; it must remain byte-identical to the round-5 baseline (`b6ca1e902f2bf08b8acddaef665d9764f8636981`). Baseline control outcome already observed by scouts: `consistent` exits 0 and prints `CLEAN: schema, citations, relations, timeline; 0 violations`. Scout probes for malformed inputs were temporary `/tmp` copies and are not durable measurements. The round-5 fixture names proposed in early scout reports under `r5-malformed/` were not present at that inspection. The round's actual sibling paths now expected for replay are `.shokunin/lore/corpus/fixtures/r5-{missing-file,invalid-json,wrong-top-level,row-shape,invalid-citation}/`; at protocol preparation these directories are present, but their presence alone is not a replay result. If any required path is missing or differs from the mutation specification below, stop and report that; do not silently substitute another path or construct fixtures.

## Preflight: identity and isolated mutations

From repo root, establish the baseline commit and checker identity. Preserve the outputs in the run directory described below. `git diff` must show no checker change from the named baseline; if that commit is unavailable, record the issue rather than substitute a baseline silently.

```sh
BASE=b6ca1e902f2bf08b8acddaef665d9764f8636981
CHECK=.shokunin/lore/corpus/fixtures/check_bible.py
FIX=.shokunin/lore/corpus/fixtures
RUN=".shokunin/lore/corpus/live/runs/r5-verifier-$(date -u +%Y%m%dT%H%M%SZ)"
mkdir -p "$RUN"
git diff --exit-code "$BASE" -- "$CHECK"
sha256sum "$CHECK" | tee "$RUN/checker.before.sha256"
```

Before executing the CLI, verify each malformed directory is independently based on `consistent/`: all five files must match byte-for-byte except the single declared `contradictions.json` mutation/removal, or the single declared `relations.json` mutation for the citation case. The following paths were present at protocol preparation and an initial byte comparison found exactly these differences: `r5-missing-file`, `r5-invalid-json`, `r5-wrong-top-level`, and `r5-row-shape` differ only at `contradictions.json`; `r5-invalid-citation` differs only at `relations.json`. This is an observed filesystem comparison, not a CLI measurement or verification of the mutation's meaning. Recheck it yourself. The expected mutation details are:

| Case | Required difference from `consistent/` | Predicted diagnostic class (expectation, not measurement) |
|---|---|---|
| `r5-missing-file` | `contradictions.json` absent; other four JSON files identical | exit 1; `contradictions.json: cannot load JSON` |
| `r5-invalid-json` | only `contradictions.json` replaced by syntactically invalid JSON | exit 1; `contradictions.json: cannot load JSON` |
| `r5-wrong-top-level` | only `contradictions.json` changed from array to valid non-array JSON | exit 1; `contradictions.json: expected array` |
| `r5-row-shape` | only `contradictions.json` changed to an array containing a non-object row | exit 1; `contradictions[0]: expected object` |
| `r5-invalid-citation` | only existing relation's `source_id` changed to unresolved `absent-source` in `relations.json` | exit 1; `relations[0].source_id: unknown in-world source 'absent-source'` |

The four `contradictions.json` probes use the empty-table baseline specifically to avoid dependent-reference cascades. Do not generalize these results to malformed entity/source tables. For each case, save a manifest of SHA-256 hashes for all present fixture JSON files, plus an explicit `MISSING contradictions.json` entry where applicable. Compare against `consistent/` to confirm only the declared mutation. Hash the control and prior regression fixture inputs too. Hash all inputs again after replay; any difference invalidates the replay and must be reported. Never repair or normalize input files during verification.

## Replay and raw measurement

Run the following exact commands from the repository root. Store stdout, stderr, and numeric exit status separately for every command. Shell status capture is explicit so a failing checker does not prevent later cases from running. The `expected-*` columns above are predictions from the stated probe/code path; enter actual status, stable diagnostic class/location, stderr/traceback, and violation summary only from captured runs. Avoid treating absolute paths, JSON parser offsets, diagnostic ordering, or punctuation as portable assertions.

```sh
for case in consistent r5-missing-file r5-invalid-json r5-wrong-top-level r5-row-shape r5-invalid-citation; do
  set +e
  python3 "$CHECK" "$FIX/$case" >"$RUN/$case.stdout" 2>"$RUN/$case.stderr"
  status=$?
  set -e
  printf '%s
' "$status" >"$RUN/$case.status"
done
sha256sum "$CHECK" | tee "$RUN/checker.after.sha256"
```

For each run, record whether output contains the predicted diagnostic class and whether it contains the ordinary final violation summary; record any secondary diagnostics without suppressing them. `consistent` is expected to be status 0 / `CLEAN`; each malformed case is expected status 1 / its named class. These are expected outcomes only until measured. A mismatch, traceback, unexpected cascade, missing summary, or nonempty stderr is a finding, not a reason to edit the expected table. Preserve raw files and report exact relative paths in the verifier's report.

## Prior-outcome comparison

“Preserved old outcomes” requires rerunning the unchanged checker over the pre-existing cases, not relying on source identity or archived round-3/4 logs. Capture the same stdout/stderr/status format for these repository fixtures:

```sh
for case in contradictions ally-reciprocal ally-one-way contradictions-ledger-malformed; do
  set +e
  python3 "$CHECK" "$FIX/$case" >"$RUN/$case.stdout" 2>"$RUN/$case.stderr"
  status=$?
  set -e
  printf '%s
' "$status" >"$RUN/$case.status"
done
```

Compare measured outcomes against the round-5 declared prior outcomes: `consistent` 0/clean; `contradictions` 1 with the original three violations; `ally-reciprocal` 0/clean; `ally-one-way` 1 with missing-reciprocal relation finding; `contradictions-ledger-malformed` 1 with its ledger-local unknown-event finding plus the original three. Capture `contradictions` as above too if not already captured in the control run (it is not the `consistent` control). Compare stable classes and counts, not host-specific full output. Record every discrepancy; do not use rejected round-4 archived results as baseline.

Finally recheck checker hash and all input hashes against preflight. The verifier should state whether hashes remained stable and whether every malformed case and old outcome matched. This samples five malformed inputs only; it proves neither exhaustive malformed-input handling nor canon validity, citation support, or repair behavior. No checker behavior is being added by this protocol.
