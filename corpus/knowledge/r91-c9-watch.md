# Round 91 C9 watch

## Pinned checker and ruling

- Delivered checker: `corpus/fixtures/check_bible.py` at r90 closure `a7c6a1773d5994246a76e4eff30d645f161920e0`.
- SHA-256: `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.
- Ruling carried from r90 C9: after record-shape, source, and tick validation, an integer provenance tick inversion (`tick <= previous_tick`) is a definite input-structural finding. Holder identity is not an operand of this comparison. A holder that is not uniquely resolved can still make the separate chain-break identity comparison qualified; it does not by itself qualify the tick finding.
- This is a statement about the checker's local integer ordering rule, not real-world chronology, source reliability, ownership, or canon.

## Reproducible boundary probe

The durable pair is `r91-c1-null-chain` and `r91-c1-tick-unresolved`. Run from `lore-shokunin/`:

```sh
sha256sum corpus/fixtures/check_bible.py
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

The hash command must print the pinned SHA-256 above. The null-chain fixture must report `provenance chain break; expected from_holder 'mira', got None` (exit 1, one violation). The unresolved-tick fixture must emit the definite `provenance tick 1 must be greater than previous tick 3` line while retaining the separately qualified `possible provenance chain break` line (exit 1, three violations including its deliberate invalid-duplicate row diagnostic). The e97613c comparison is pinned in `.ufo/waves/round-91/patches/B3-before-state.json` and in the fixture READMEs; it hedges the tick line and the null-chain line.

## Falsification trigger

Reopen the ruling only when a demonstrated case shows that the integer tick finding itself needs holder-identity context. A qualifying counterexample must:

1. Contain a uniquely identified, structurally valid item and valid nonnegative integer ticks in one provenance list, so neither the item identity nor tick parsing is the reason the check stops.
2. Have a genuinely unresolved non-null compared holder, with the raw-row and resolved-index counts recorded; preserve a paired uniquely resolved control.
3. Include independently reviewable, source-backed evidence establishing that the compared tick values are not on one shared item-local sequence (for example, they are holder-local ordinals whose comparison is meaningful only after holder identity is known).
4. Show that the delivered checker reports a definite inversion that this evidence makes indeterminate. A holder mismatch or unresolved ID alone does not satisfy the trigger.

Probe to run from `lore-shokunin/` after adding such a durable counterexample:

```sh
sha256sum corpus/fixtures/check_bible.py
python3 corpus/fixtures/check_bible.py corpus/fixtures/<counterexample>
python3 corpus/fixtures/check_bible.py corpus/fixtures/<uniquely-resolved-control>
```

Record complete stdout, stderr, exit status, the source excerpts and their exact tick/holder mappings, plus the two checker hashes. If the counterexample meets all four gates, file a C1 follow-up proposing a narrowly scoped tick-qualification change; keep the chain-break qualification as a separate decision. Otherwise retain this ruling.

## Owner

S1 owns this watch design for round 91 and hands it to the next C1 calibration owner at closure. That owner runs and reviews any qualifying probe; no automatic checker change follows from a trigger report alone.

## Check log

| Date | Checker SHA-256 | Four-probe re-check |
|---|---|---|
| 2026-10-17 | `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` | **DISCRIMINATION HELD** — all four C5 scenarios retained their r91 distinctions; no drift alarm. |
| 2026-10-17 (r93) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 2 (seat X1, r93): all four gates reproduce; gate 3 not met; trigger unsatisfied; ruling retained. Next re-check: r94. |

### 2026-10-17 — first periodic re-check

Run from `lore-shokunin/` at HEAD `396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f`. Readiness polls (both pinned artifacts were present immediately):

```sh
bash .ufo/waves/poll_wait.sh corpus/fixtures/check_bible.py 1200
bash .ufo/waves/poll_wait.sh corpus/knowledge/r91-c9-watch.md 1200
```

```text
POLL_HIT path=corpus/fixtures/check_bible.py elapsed=0s checks=0
POLL_HIT path=corpus/knowledge/r91-c9-watch.md elapsed=0s checks=0
```

The pinned checker command and output:

```sh
sha256sum corpus/fixtures/check_bible.py
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

The watch's durable pair, run verbatim:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
```

```text
exit=1; stderr=empty
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed
```

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

```text
exit=1; stderr=empty
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
```

The four C5 semantic probes were reconstructed one at a time under `/tmp` from `corpus/fixtures/r89-fn2-unresolved-chain-break`, using the mutations in `.ufo/waves/round-90/patches/C9-rerun-probes.sh`; each temporary fixture was removed after its run. Commands below invoke the delivered checker at `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py` from cwd `/home/vgpnk/Projects/shokunin/lore-shokunin`.

**P1 — unresolved chain stays qualified**

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py /tmp/lore-X1-r92-zjkj_k4x
```

```text
exit=1; stderr=empty
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
2 violation(s); no canon changed
```

**P2 — unresolved holder does not qualify the integer tick inversion under the r91 ruling**

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py /tmp/lore-X1-r92-u3xijxsr
```

```text
exit=1; stderr=empty
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
2 violation(s); no canon changed
```

**P3 — null `from_holder` chain break is definite**

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py /tmp/lore-X1-r92-dr9v6jdu
```

```text
exit=1; stderr=empty
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1]: provenance chain break; expected from_holder 'mira', got None
2 violation(s); no canon changed
```

**P4 — unrelated duplicate does not qualify the tick inversion (paired resolved-holder control)**

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py /tmp/lore-X1-r92-bg523m6k
```

```text
exit=1; stderr=empty
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
2 violation(s); no canon changed
```

Each nonzero exit retains the base fixture's deliberate invalid `entities[1].first_appearance` row; all four expected target findings are present. The r90 X1 candidate's P2 identity qualifier is not the current expected output: the r91 pinned ruling above makes this integer comparison independent of holder identity.

The four falsification-trigger gates were checked separately. The exact count command and output:

```sh
python3 - <<'PY'
import json
from pathlib import Path

def admitted(row):
    fields={'id':str,'kind':str,'name':str,'first_appearance':str,'claims':list}
    return isinstance(row,dict) and all(field in row and type(row[field]) is kind and (kind is not str or bool(row[field].strip())) for field,kind in fields.items())
for label,path,holder,ticks in [
    ('P2 unresolved','corpus/fixtures/r91-c1-tick-unresolved','f3-dup',None),
    ('P4 control','corpus/fixtures/r89-fn2-unresolved-chain-break','mira',[3,1]),
]:
    rows=json.loads((Path(path)/'entities.json').read_text(encoding='utf-8'))
    item_rows=[r for r in rows if r.get('id')=='f3-seal' and r.get('kind')=='item' and admitted(r)]
    holder_rows=[r for r in rows if r.get('id')==holder]
    indexed=[r for r in holder_rows if admitted(r)]
    if ticks is None:
        ticks=[r.get('tick') for r in item_rows[0].get('provenance',[])] if len(item_rows)==1 else []
    print(f'{label}: item=f3-seal admitted_matches={len(item_rows)} ticks={ticks} holder={holder} raw_rows={len(holder_rows)} resolved_rows={len(indexed)}')
PY
```

```text
P2 unresolved: item=f3-seal admitted_matches=1 ticks=[3, 1] holder=f3-dup raw_rows=2 resolved_rows=1
P4 control: item=f3-seal admitted_matches=1 ticks=[3, 1] holder=mira raw_rows=1 resolved_rows=1
```

The sequence-scope evidence check command and output:

```sh
python3 - <<'PY'
from pathlib import Path
root=Path('corpus/fixtures/r91-c1-tick-unresolved')
print('excerpt_files='+','.join(sorted(p.name for p in root.glob('*excerpt*'))))
print('readme_line3='+root.joinpath('README.md').read_text(encoding='utf-8').splitlines()[2])
PY
```

```text
excerpt_files=
readme_line3=Fixture scaffolding only; not sourced story evidence.
```

- Gate 1: met by the uniquely admitted `f3-seal` item and nonnegative integer ticks `[3, 1]`.
- Gate 2: met by P2's non-null `f3-dup` reference (2 raw rows, 1 resolved row) and P4's same-tick-pair `mira` control (1 raw and 1 resolved row).
- Gate 3: **not met** — these fixture records provide no independently reviewable, source-backed evidence that the compared ticks belong to different sequences; the README describes fixture structure only.
- Gate 4: the delivered checker emits a definite inversion in P2, but no evidence establishes that it is indeterminate. The four-gate falsification trigger is therefore not satisfied; retain the ruling. **Alarm: none.**

**Census path convention:** Run from the repository root and pass each fixture as the repository-relative `corpus/fixtures/<name>` argument; the five missing-file fixtures echo that argv path in stdout.
**B1 tuple assumption:** Replay B1 tuples with the same repository-relative fixture paths and argv spelling; absolute or differently prefixed paths alter the five captured stdout hashes.

## 2026-10-17 — r93 clarification / replacement

This append-only clarification replaces the imprecise wording in check-log row 2 (`2026-10-17 (r93)`); it does **not** add a third check-log row. The first dated row is the first periodic re-check in r92; row 2 is the distinct second re-check in r93, executed by seat X1. The r92 and r93 check identities are distinct even though both use the calendar date 2026-10-17.

The row-2 checker abbreviation `ff9fd2aa…d1421` is replaced here by the full checker SHA-256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`. The historical comparison baseline is commit `e97613cc276f5fa9cac49ff1900798cf6863c020`.

The phrase `all four gates reproduce` in row 2 is superseded as ambiguous: the r93 discriminator commands below verify the two stable fixtures, not the four falsification-trigger gates. From `lore-shokunin/`, `python3 corpus/tools/discriminate_check.py` exited 0 with `DISCRIMINATION HELD`; `python3 corpus/tools/discriminate_check.py --checker e97613c` exited 2 with `REGRESSION-DETECTED`. These modes compare the delivered checker with the historical baseline on `corpus/fixtures/r91-c1-null-chain` and `corpus/fixtures/r91-c1-tick-unresolved`.

Gate 3 remains **not met**: the `sequence-scope evidence check` recorded above was rerun from the repository root and produced `excerpt_files=` and `readme_line3=Fixture scaffolding only; not sourced story evidence.` Thus the unresolved-tick fixture has no `*excerpt*` files and supplies no independently reviewable, source-backed evidence that the compared ticks belong to different sequences. Gate 4's claim that this evidence makes the definite inversion indeterminate is therefore also not established; the four-gate falsification trigger has **not** passed, and the ruling remains unchanged.

**Ongoing calibration owner:** the lore-shokunin calibration lane owns this C9 watch and its follow-up; X1 was the r93 re-check executor. The next re-check is due in r94. This replaces the prior §Owner handoff wording, “the next C1 calibration owner at closure,” with an explicit lane owner and due round.

## 2026-10-17 — r94 re-check (third) and line-54 erratum

Third periodic re-check, executed at the r94 closure (2026-10-17). Checker byte pin verified fresh at the delivered revision:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair, run verbatim from the repository root:

```sh
python3 corpus/tools/discriminate_check.py
```

```text
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
```

(exit 0; both durable fixtures: semantic gate PASS, README/exit pins exact)

```sh
python3 corpus/tools/discriminate_check.py --checker e97613c
```

```text
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
```

(exit 2, expected control)

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r94) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 3 (r94 closure): delivered discrimination held; the `e97613c` control reported REGRESSION-DETECTED as expected; ruling retained. Next re-check: r95. |

Gate 3 remains **not met** and the four-gate falsification trigger remains unsatisfied; nothing in r94 changes the sequence-scope evidence state recorded in the r93 clarification above.

**Erratum (dated, append-only):** the first periodic re-check section above opens "Run from `lore-shokunin/` at HEAD `396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f`." That HEAD-bound premise is stale at the delivered revision (r94 closure HEAD per the round-94 LOG entry). The section's actionable pin — the checker SHA-256 — remains fresh and was reproduced above; the discriminator commands are content-pinned inside `corpus/tools/discriminate_check.py` and replay at any later HEAD. This erratum supersedes only the stale HEAD phrase, following the R10 erratum pattern; the historical section text remains unrewritten.

## 2026-10-17 — r95 re-check (fourth)

Fourth periodic re-check, executed at the r95 closure (2026-10-17). Checker byte pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2, expected control).

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r95) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 4 (r95 closure): delivered discrimination held; `e97613c` control REGRESSION-DETECTED as expected; ruling retained. Next re-check: r96. |

Gate 3 remains **not met**; the four-gate falsification trigger remains unsatisfied; nothing in r95 changes the sequence-scope evidence state.

## 2026-10-17 — r96 re-check (fifth)

Fifth periodic re-check, executed at the r96 closure (2026-10-17). Checker byte pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2, expected control).

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r96) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 5 (r96 closure): delivered discrimination held; `e97613c` control REGRESSION-DETECTED as expected; ruling retained. Next re-check: r97. |

Gate 3 remains **not met**; the four-gate falsification trigger remains unsatisfied; nothing in r96 changes the sequence-scope evidence state.

## 2026-10-17 — r97 re-check (sixth)

Sixth periodic re-check, executed at the r97 closure (2026-10-17). Checker byte pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2, expected control).

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r97) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 6 (r97 closure): delivered discrimination held; `e97613c` control REGRESSION-DETECTED as expected; ruling retained. Next re-check: r98. |

Gate 3 remains **not met**; the four-gate falsification trigger remains unsatisfied; nothing in r97 changes the sequence-scope evidence state.

## 2026-10-17 — r98 re-check (seventh)

Seventh periodic re-check, executed at the r98 closure (2026-10-17). Checker byte pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2, expected control).

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r98) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 7 (r98 closure): delivered discrimination held; `e97613c` control REGRESSION-DETECTED as expected; ruling retained. Next re-check: r99. |

Gate 3 remains **not met**; the four-gate falsification trigger remains unsatisfied; nothing in r98 changes the sequence-scope evidence state.
