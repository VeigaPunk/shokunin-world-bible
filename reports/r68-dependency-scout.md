# Round 68 dependency scout — checker path and baseline behavior

## Scope

This is a read-only map of the declared Round 68 claim in `.shokunin/lore/LOG.md` and the current baseline checker/fixtures. It makes no implementation or canon claim.

## Exact dependency code path

In `.shokunin/lore/corpus/fixtures/check_bible.py`:

1. `FIELDS['timeline']` at lines 29–30 requires `depends_on` to be a `list` (and requires the other listed timeline fields). The common row validator at lines 65–76 rejects a row if a required field has the wrong exact type; for strings it also rejects empty/whitespace-only *row fields* via `.strip()` at line 72. It does **not** validate elements of the dependency list there.
2. `check()` indexes schema-screened timeline rows at lines 91–95, building `events` (a last-wins map) and `event_id_counts` (valid-row counts). Thus the dependency loop operates on rows that passed the timeline row-field gate.
3. For each event, lines 295–297 bind `row['depends_on']`; if any element is not a string, the checker adds one list-local `expected event-id strings` error. Lines 299–301 then skip each non-string element individually.
4. Each string is processed at `timeline[i].depends_on[j]` (line 302). The checker emits self-dependency at lines 303–304 and repeated-entry diagnostics at lines 305–308. It validates ID membership/count only on a dependency's first occurrence in that list: count zero yields `timeline[i].depends_on: unknown event ...` (lines 309–312); count above one yields an indexed `ambiguous dependency event` finding (lines 312–313); exactly one target is compared for tick inversion at lines 314–316. A repeated occurrence still gets its repeated diagnostic, but does not repeat membership/tick lookup.
5. The CLI prints each error as `VIOLATION`, exits 1 if any exist, otherwise prints `CLEAN` and exits 0 (lines 324–330).

## Baseline observations

The declared baseline is clean HEAD `c3b090fb6df57bbe8f6e2680b24045c2db33e4fe` in the Round 68 declaration. In the checked-out baseline, a string dependency is not stripped or tested for nonemptiness before membership lookup. Therefore an empty string, whitespace-only string, and ordinary nonempty unknown string all take the same unknown-event branch. I confirmed this by copying `.shokunin/lore/corpus/fixtures/consistent/` to temporary directories, changing only `timeline[1].depends_on` to each single value, and running the repository-root CLI below:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py <temporary-copy>
```

Observed outputs (all exit 1; one violation each):

```text
"":       VIOLATION: timeline[1].depends_on: unknown event ''
"   ":    VIOLATION: timeline[1].depends_on: unknown event '   '
"ghost":  VIOLATION: timeline[1].depends_on: unknown event 'ghost'
```

The corresponding baseline control `consistent/` exits 0 with `CLEAN: schema, citations, relations, timeline; 0 violations`.

Committed fixtures independently show nearby behavior in `.shokunin/lore/corpus/fixtures/`:

- `r22-unknown-mixed/timeline.json` has `['missing', null]`; CLI reports the aggregate `expected event-id strings` and `unknown event 'missing'` (two findings, exit 1). A non-string is skipped for lookup.
- `r22-malformed-only/timeline.json` has `[null]`; CLI reports only `expected event-id strings` (exit 1).
- `r22-self-repeated/timeline.json` has a self ID twice plus `null`; CLI reports the aggregate malformed-list finding, self diagnostics for both strings, a repeated-dependency diagnostic for the second, and an inversion for the first occurrence (five findings, exit 1).
- `r22-valid-order/timeline.json` exits 0; `r20-valid-inversion/timeline.json` reports the existing strict-earlier inversion (exit 1).

These are current committed examples of the baseline/current implementation; the empty/whitespace probes above were temporary and were not written into the repository.

## Limits

This maps checker behavior only. An `unknown event` diagnostic means the string does not match an indexed schema-screened timeline ID; it does not establish that an event is absent from fictional canon or source text. The temporary probes establish the specific empty/whitespace/nonempty-unknown behavior, not an exhaustive malformed-list matrix. I did not alter fixtures, checker, documentation, or any other path.
