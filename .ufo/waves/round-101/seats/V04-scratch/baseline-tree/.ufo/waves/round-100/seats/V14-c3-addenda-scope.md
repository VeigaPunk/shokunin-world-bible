# V14 — C3 addenda scope

Axes: exact three-row scope; historical byte preservation; dated, resolvable debt pointers.

Scope: independently verify T4's additions to `corpus/knowledge/r99-gate-blind-spot-table.md` against r99 closure `fe1ce46`. This is a scope/preservation verdict, not a fresh semantic replay of the three mutants or round-wide admission. All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`; Python commands used `python3`. Only this exclusive report was written by V14; no scratch, corpus edits, nested agents, network, commits, or pushes.

## Producer prerequisites and bounded wait

Read `LOG.md:3349-3404` before verifying. Initial direct Read of lane `AGENTS.md` returned absent; no instruction file was changed. Initially the table equaled the baseline and both new T4 knowledge artifacts and the T4 report were absent.

The actual first polling command was:

```sh
python3 -u - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import subprocess, time
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert root == Path.cwd().resolve()
base = subprocess.check_output(['git', 'show', 'fe1ce46:corpus/knowledge/r99-gate-blind-spot-table.md'], cwd=root)
for attempt in range(1, 15):
    artifacts = [root/'corpus/knowledge/r100-crossing-arc-synthesis.md', root/'corpus/knowledge/r100-provenance-semantics-boundary.md']
    table_changed = (root/'corpus/knowledge/r99-gate-blind-spot-table.md').read_bytes() != base
    seats = root/'.ufo/waves/round-100/seats'
    reports = sorted(p for p in seats.iterdir() if p.is_file() and p.name.startswith('T4') and p.suffix == '.md') if seats.is_dir() else []
    ready = all(p.is_file() and p.stat().st_size > 0 for p in artifacts) and table_changed and bool(reports)
    print(datetime.now(timezone.utc).isoformat(), f'POLL {attempt}/40', 'artifacts='+','.join(f'{p.name}:{p.is_file()}' for p in artifacts), f'table_changed={table_changed}', 'producer_reports='+repr([p.name for p in reports]), f'READY={ready}', flush=True)
    if ready:
        break
    if attempt < 14:
        time.sleep(20)
PY
```

Exit 0; 14 checks, 20 seconds apart, all not ready. Representative actual output:

```text
2026-10-18T02:32:20.200080+00:00 POLL 1/40 artifacts=r100-crossing-arc-synthesis.md:False,r100-provenance-semantics-boundary.md:False table_changed=False producer_reports=[] READY=False
2026-10-18T02:36:40.203817+00:00 POLL 14/40 artifacts=r100-crossing-arc-synthesis.md:False,r100-provenance-semantics-boundary.md:True table_changed=True producer_reports=[] READY=False
```

The continuation command was:

```sh
python3 -u - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import subprocess, time
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert root == Path.cwd().resolve()
base = subprocess.check_output(['git', 'show', 'fe1ce46:corpus/knowledge/r99-gate-blind-spot-table.md'], cwd=root)
for attempt in range(15, 29):
    time.sleep(20)
    artifacts = [root/'corpus/knowledge/r100-crossing-arc-synthesis.md', root/'corpus/knowledge/r100-provenance-semantics-boundary.md']
    table_changed = (root/'corpus/knowledge/r99-gate-blind-spot-table.md').read_bytes() != base
    seats = root/'.ufo/waves/round-100/seats'
    reports = sorted(p for p in seats.iterdir() if p.is_file() and p.name.startswith('T4') and p.suffix == '.md') if seats.is_dir() else []
    ready = all(p.is_file() and p.stat().st_size > 0 for p in artifacts) and table_changed and bool(reports)
    print(datetime.now(timezone.utc).isoformat(), f'POLL {attempt}/40', 'artifacts='+','.join(f'{p.name}:{p.is_file()}' for p in artifacts), f'table_changed={table_changed}', 'producer_reports='+repr([p.name for p in reports]), f'READY={ready}', flush=True)
    if ready:
        break
PY
```

Exit 0; ready at attempt 25/40, before the bound. Final actual line:

```text
2026-10-18T02:40:26.623337+00:00 POLL 25/40 artifacts=r100-crossing-arc-synthesis.md:True,r100-provenance-semantics-boundary.md:True table_changed=True producer_reports=['T4-knowledge-author.md'] READY=True
```

Then read the completed `.ufo/waves/round-100/seats/T4-knowledge-author.md` and delivered table addendum. No plan was verified, no all-reports/self-inclusive poll was used, and no stall escape or background task was needed. UTC poll timestamps are literal tool output; the authored rows carry their declared `2026-10-17 / r100` date.

## Independent git-diff and byte audit

Actual commands:

```sh
git diff --numstat fe1ce46 -- corpus/knowledge/r99-gate-blind-spot-table.md
git diff --no-ext-diff --unified=3 fe1ce46 -- corpus/knowledge/r99-gate-blind-spot-table.md
```

Both exited 0. Numstat printed:

```text
105	0	corpus/knowledge/r99-gate-blind-spot-table.md
```

The diff had a single append-only hunk beginning `@@ -268,3 +268,108 @@`. Its five added pipe-prefixed lines consist of one header, one separator, and exactly these three numbered data rows:

- `corpus/knowledge/r99-gate-blind-spot-table.md:278`: row 10, `2026-10-17 / r100`, mapped-verbatim-anchor removal, `r99 AC-2`.
- `corpus/knowledge/r99-gate-blind-spot-table.md:279`: row 11, `2026-10-17 / r100`, simultaneous dropped edge/prose edit, `r99 AC-1`.
- `corpus/knowledge/r99-gate-blind-spot-table.md:280`: row 12, `2026-10-17 / r100`, combined invocation, `r99 AC-3`.

An independent byte-level audit counted actual git-diff rows rather than relying on T4's receipt. Full actual command:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib, re, subprocess
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert root == Path.cwd().resolve()
rel = 'corpus/knowledge/r99-gate-blind-spot-table.md'
base = subprocess.check_output(['git', 'show', 'fe1ce46:' + rel], cwd=root)
now = (root / rel).read_bytes()
diff = subprocess.check_output(['git', 'diff', '--no-ext-diff', '--unified=0', 'fe1ce46', '--', rel], cwd=root)
added = [line[1:] for line in diff.splitlines() if line.startswith(b'+') and not line.startswith(b'+++')]
removed = [line[1:] for line in diff.splitlines() if line.startswith(b'-') and not line.startswith(b'---')]
added_table = [line for line in added if line.startswith(b'|')]
def cells(line):
    return [x.strip() for x in line.strip().strip(b'|').split(b'|')]
def is_data(line):
    cs = cells(line)
    return cs[0] not in (b'#', b'Probe') and not all(re.fullmatch(rb':?-+:?', x) for x in cs)
new_rows = [line for line in added_table if is_data(line)]
old_table = [line for line in base.splitlines(keepends=True) if line.startswith(b'|')]
current_table = [line for line in now.splitlines(keepends=True) if line.startswith(b'|')]
preserved = sum(a == b for a, b in zip(old_table, current_table))
old_data = [line for line in old_table if is_data(line)]
current_data = [line for line in current_table if is_data(line)]
print('BASELINE_COMMIT fe1ce46')
print('BASELINE_SHA256', hashlib.sha256(base).hexdigest())
print('DELIVERED_SHA256', hashlib.sha256(now).hexdigest())
print('BASELINE_BYTES', len(base), 'DELIVERED_BYTES', len(now), 'APPENDED_BYTES', len(now) - len(base))
print('EXACT_BASELINE_PREFIX', now[:len(base)] == base)
print('DIFF_LINES added=' + str(len(added)) + ' removed=' + str(len(removed)))
print('DIFF_TABLE_LINES', len(added_table), 'HEADER_OR_SEPARATOR', len(added_table) - len(new_rows), 'DATA_ROWS', len(new_rows))
print('NEW_ROW_IDS', ','.join(cells(line)[0].decode() for line in new_rows))
print('PRIOR_TABLE_LINES_BYTE_IDENTICAL', str(preserved) + '/' + str(len(old_table)))
print('TABLE_DATA_ROWS before=' + str(len(old_data)) + ' after=' + str(len(current_data)))
log = (root / 'LOG.md').read_text().splitlines()
addendum = now[len(base):].decode()
print('COMMON_DEBT_CITATION', 'LOG.md:3303-3313' in addendum)
expected = {'10':'AC-2', '11':'AC-1', '12':'AC-3'}
for row in new_rows:
    cs = cells(row)
    row_id = cs[0].decode()
    debt = expected[row_id]
    print('ROW', row_id, 'DATE', cs[1].decode(), 'DEBT', 'r99 ' + debt, 'POINTER_PRESENT', ('r99 ' + debt).encode() in row, 'LOG_RANGE_EXISTS', len(log) >= 3313)
checks = [now.startswith(base), not removed, len(new_rows) == 3, [cells(x)[0] for x in new_rows] == [b'10',b'11',b'12'], len(added_table) == 5, preserved == len(old_table), current_table[:len(old_table)] == old_table, 'LOG.md:3303-3313' in addendum]
checks.extend(cells(row)[1] == b'2026-10-17 / r100' and ('r99 ' + expected[cells(row)[0].decode()]).encode() in row for row in new_rows)
print('SCOPE_AUDIT', 'PASS' if all(checks) else 'FAIL')
raise SystemExit(0 if all(checks) else 1)
PY
```

Observed complete output; exit 0:

```text
BASELINE_COMMIT fe1ce46
BASELINE_SHA256 4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e
DELIVERED_SHA256 f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff
BASELINE_BYTES 20526 DELIVERED_BYTES 29433 APPENDED_BYTES 8907
EXACT_BASELINE_PREFIX True
DIFF_LINES added=105 removed=0
DIFF_TABLE_LINES 5 HEADER_OR_SEPARATOR 2 DATA_ROWS 3
NEW_ROW_IDS 10,11,12
PRIOR_TABLE_LINES_BYTE_IDENTICAL 22/22
TABLE_DATA_ROWS before=18 after=21
COMMON_DEBT_CITATION True
ROW 10 DATE 2026-10-17 / r100 DEBT r99 AC-2 POINTER_PRESENT True LOG_RANGE_EXISTS True
ROW 11 DATE 2026-10-17 / r100 DEBT r99 AC-1 POINTER_PRESENT True LOG_RANGE_EXISTS True
ROW 12 DATE 2026-10-17 / r100 DEBT r99 AC-3 POINTER_PRESENT True LOG_RANGE_EXISTS True
SCOPE_AUDIT PASS
```

The preservation result is stronger than row equality: all 20,526 original bytes, including all prose, headers, row bytes, and line endings, remain an exact file prefix. The 22 original table lines include four header/separator lines and 18 data rows across the original decision and probe tables; those 18 data rows become 21, not 23. The new five table lines are not five new data rows.

## Debt-pointer resolution and bounds

The new table has no separate `Debt` column. Each row instead carries its explicit `r99 AC-N` pointer in the mutation/invocation cell, and the addendum intro at `corpus/knowledge/r99-gate-blind-spot-table.md:274` resolves all three via `LOG.md:3303-3313`.

Read that exact log range independently. Its observed content maps correctly:

- `LOG.md:3304-3307`: correction (1), inventory findings precede digest mismatch — row 11 / AC-1.
- `LOG.md:3307-3311`: correction (2), mapped-anchor removal already failed support checking — row 10 / AC-2.
- `LOG.md:3311-3313`: correction (3), combined invocation emits INVALID-ARGUMENTS only — row 12 / AC-3.

Thus the pointers are traceable adjudication/debt references, not unexplained new labels. This verdict does not reinterpret these references as new standalone BR/NB identifiers and does not require a column name that the seat contract did not prescribe. The corresponding replay sections are present at table lines 282-371; their runtime outcomes are outside this seat's scope and are not independently credited here.

Additional actual command:

```sh
git diff --check fe1ce46 -- corpus/knowledge/r99-gate-blind-spot-table.md
```

Exit 0, no stdout/stderr.

Before writing this exclusive report, a lane-root `python3` path-resolution guard confirmed the absolute target resolved under the lane, did not already exist, and that the table's final hash was still `f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff`. It also re-observed both T4 knowledge artifacts and the actual producer report as nonempty files (17,698 / 10,815 / 14,319 bytes). No failing scope check, contradiction, missing pointer, unresolved seat blocker, or scope expansion was found.

PASS — exactly three dated data rows added by git diff; every historical byte preserved; all three new rows carry resolvable r99 AC debt pointers.
