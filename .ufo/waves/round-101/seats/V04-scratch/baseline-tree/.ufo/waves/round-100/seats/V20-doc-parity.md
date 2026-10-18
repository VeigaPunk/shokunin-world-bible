# V20 — doc parity / pre-integration inventory (2026-10-17)

Axes: freshness (current navigation and dated supersessions), coverage (fixture census and frozen-chain scope), calibration (do not turn byte/lexical receipts into semantic findings). This is a read-only inventory for closure, not round-wide adjudication.

Baseline: r99 closure `fe1ce46`. Observed live HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (r100 declaration); producer deliverables are in the uncommitted wave tree. Every command below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, with `python3` for Python commands.

## Closure findings — three shared-document updates remain

1. **Fixtures index has no Round-100 section.** `corpus/fixtures/README.md` ends at line 1288 with Round 99. Its latest census at line 1286 is the accurate historical **173 / 39 clean / 134 negative / 421 violation lines** snapshot, not the delivered r100 census. Append a dated Round-100 section for `r100-docket-review`, the review-only/open-entry/no-resolution bound, 6/1/9 and 9 sources, 22 obligations, replay commands, and the freshly measured **174 / 40 / 134 / 421**, zero stderr and zero unexpected exits. State the seven-fixture chain through r99 separately from the new, unpinned r100 fixture. Supersede line 1282's `r99-window-lapse is not yet pinned (r100 candidate)` as current coverage without falsifying its history.
2. **Corpus navigation lacks r100 and carries an older freeze contract.** `corpus/README.md:26` is still the last fixture bullet (r99). Add the r100 fixture bullet and navigation to both new knowledge records. More importantly, the active verification bullet at `corpus/README.md:41` still says rounds 96–98, lists only r88/r94/r95/r96/r97/r98, says **17-case**, **JSON content digests**, and **five JSON tables only**. Delivered state is seven fixtures through r99, 18 persisted expectations, schema-2 hashes over ten declared files, and byte-change detection, not prose entailment. This active/current navigation wording is not rescued by historical-section disclaimers elsewhere.
3. **C9 r100 row is absent.** `corpus/knowledge/r91-c9-watch.md:335` is still re-check 8 / r99, next due r100; file ends at 337. Append dated **r100 / ninth re-check** with the current checker hash, delivered discriminator exit 0, historical `e97613c` control exit 2, ruling retained, and next re-check r101. The current pinned unresolved-tick fixture still has no excerpt files and describes fixture scaffolding only; the existing source-backed falsification trigger has not been established by these probes. Do not describe the two-fixture discriminator as execution of all four source-backed falsification gates.

All three files are byte-identical to `fe1ce46` at the final audit. These are pre-integration closure gaps, not claims that the producers violated their ownership: none of these three shared files belongs to T1–T4. V20 did not edit them.

## Stale-wording inventory and already-landed supersessions

- **Needs current-navigation repair:** `corpus/README.md:41`, as above. The r100 corpus bullet should describe the clerk's review, not copy r99's lapse text; it has 22 obligations, not 21.
- **Historical fixture sections, retain and supersede:** `corpus/fixtures/README.md:1236` (four pins, Markdown unpinned, prose half open) and `:1259` (six pins, five JSON files, 17 cases) are creation-time statements. Round 99 at `:1282` already supersedes the payload/semantics part. The new Round-100 section must additionally supersede the r99-unpinned bound and publish the new census; do not globally replace old historical census counts.
- **T1 freshness landed:** `corpus/tools/README.md:363-421` has the dated seven-chain addendum, guarded-write receipt, and explicit r100-unpinned boundary. `SKILL.md:96-102` lists the seventh fixture and states seven pins / 7/7. Its historical phrase about the six re-frozen at r99 remains historical and is explicitly followed by the r100 addition. No open gap in these owned rows was found.
- **T4 freshness landed:** the old unpinned/six-pin sentence at `corpus/knowledge/r99-gate-blind-spot-table.md:270` remains as history, but `:373-375` explicitly supersedes it. The old contract digest in its r99 `verified-at` metadata is historical; the r100 addendum at `:274` records the delivered contract `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5`. Do not report the retained old sentence/hash as an unsuperseded current claim.
- **Historical note to avoid quoting as live behavior:** `corpus/knowledge/r99-lapse-scope-note.md:65` records exit 2 `UNPINNED-FIXTURE` and six pins; `:67` records census 173. Those are the r99 pass's measurements. Actual current r99 verification is exit 0. The new boundary note `corpus/knowledge/r100-provenance-semantics-boundary.md:53-55` supersedes old r99-unpinned/six-fixture statements as current coverage; the synthesis `:61-63` names the live set. A local dated pointer in the old note would improve discoverability on its next authorized touch, but historical receipt text need not be rewritten.
- **Counting convention resolved, preserve it at closure:** `LOG.md:3376-3380` calls a list of r94 through r100 “six-beat.” `corpus/knowledge/r100-crossing-arc-synthesis.md:6-8` correctly makes r94 the seed plus six continuations r95–r100: **seven dossier snapshots**. These seven snapshots are NOT the seven frozen fixtures: dossier r94–r100 versus frozen r88 + r94–r99. Do not accidentally claim the new tick-16 edge is pinned.
- **No stale r99-copy README was accepted:** after T3's report, the delivered r100 README at `:1-29` names the review source/event, 6/1/9, 9 sources, and 22 obligations; all three documented r100 commands replayed successfully. The map states 24 total rows, not 22 total rows: 22 JSON + 2 editorial.

## Producer readiness receipt

No all-reports poll was used; no self-inclusive wait or stall escape occurred. One bounded 20-second / 40-attempt poll checked all ten r100 fixture files, both new knowledge records, the r99 pin, and actual T1–T4 report files. It completed at **attempt 24/40, 460 seconds**, exit 0. The initial absent artifacts/reports were readiness observations, not failed implementation verdicts.

Actual poll command:

```sh
python3 -u - <<'PY'
from pathlib import Path
import json
import time
root = Path.cwd().resolve()
assert root == Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
seats = root / '.ufo/waves/round-100/seats'
files = ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
artifacts = [root / 'corpus/fixtures/r100-docket-review' / name for name in files]
artifacts += [root / 'corpus/knowledge/r100-crossing-arc-synthesis.md', root / 'corpus/knowledge/r100-provenance-semantics-boundary.md']
for attempt in range(1, 41):
    missing = [p.relative_to(root).as_posix() for p in artifacts if not p.is_file() or p.stat().st_size == 0]
    reports = {f'T{i}': sorted(p.name for p in seats.glob(f'T{i}*.md') if p.is_file() and p.stat().st_size) for i in range(1, 5)}
    absent_reports = [seat for seat, paths in reports.items() if not paths]
    contract = json.loads((root / 'corpus/tools/dependency-freeze-contract.json').read_text())
    pinned = 'r99-window-lapse' in contract['pins']
    print(f'POLL {attempt}/40 missing_artifacts={missing} missing_reports={absent_reports} r99_pinned={pinned}', flush=True)
    if not missing and not absent_reports and pinned:
        print('READY producer artifacts and T1-T4 reports present', flush=True)
        print('REPORTS ' + json.dumps(reports, sort_keys=True), flush=True)
        break
    if attempt == 40:
        print('ABSENT bounded poll exhausted', flush=True)
        raise SystemExit(3)
    time.sleep(20)
PY
```

Selected observed output:

```text
POLL 1/40 missing_artifacts=['corpus/knowledge/r100-crossing-arc-synthesis.md', 'corpus/knowledge/r100-provenance-semantics-boundary.md'] missing_reports=['T1', 'T2', 'T3', 'T4'] r99_pinned=True
POLL 5/40 missing_artifacts=['corpus/knowledge/r100-crossing-arc-synthesis.md', 'corpus/knowledge/r100-provenance-semantics-boundary.md'] missing_reports=['T1', 'T3', 'T4'] r99_pinned=True
POLL 9/40 missing_artifacts=['corpus/knowledge/r100-crossing-arc-synthesis.md'] missing_reports=['T3', 'T4'] r99_pinned=True
POLL 15/40 missing_artifacts=['corpus/knowledge/r100-crossing-arc-synthesis.md'] missing_reports=['T4'] r99_pinned=True
POLL 17/40 missing_artifacts=[] missing_reports=['T4'] r99_pinned=True
POLL 24/40 missing_artifacts=[] missing_reports=[] r99_pinned=True
READY producer artifacts and T1-T4 reports present
REPORTS {"T1": ["T1-chain-seven.md"], "T2": ["T2-fixture-author.md"], "T3": ["T3-fixture-docs.md"], "T4": ["T4-knowledge-author.md"]}
```

T2's report preceded the first new-fixture census; T1's preceded the seven-pin verification; T3's preceded the map/support verification. The final batch below ran after all four reports. Reports and finished documents were read; no producer plan was treated as a delivery.

## Final executable snapshot

Actual final audit command (exit 0). It launches all 174 structural invocations plus the seven freeze verifications, r100 map/support gates, and two discriminator modes concurrently, then prints the relevant real command/output receipts. The support output is intentionally reduced to selected observed inventory/summary lines; all subprocess stdout/stderr was captured.

```sh
python3 - <<'PY'
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from pathlib import Path
import hashlib
import json
import subprocess
root = Path.cwd().resolve()
assert root == Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
seats = root / '.ufo/waves/round-100/seats'
for seat in range(1, 5):
    assert any(seats.glob(f'T{seat}*.md'))
docs = ['corpus/fixtures/README.md', 'corpus/README.md', 'corpus/knowledge/r91-c9-watch.md']
tracked_inputs = [root / path for path in docs + ['SKILL.md', 'corpus/tools/README.md', 'corpus/tools/dependency-freeze-contract.json', 'corpus/tools/dependency_freeze.py', 'corpus/fixtures/check_bible.py', 'corpus/tools/support_check.py', 'corpus/tools/map_obligations.py', 'corpus/knowledge/r100-crossing-arc-synthesis.md', 'corpus/knowledge/r100-provenance-semantics-boundary.md', 'corpus/knowledge/r99-gate-blind-spot-table.md']]
tracked_inputs += sorted((root / 'corpus/fixtures/r100-docket-review').iterdir())
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
before = {path: sha(path) for path in tracked_inputs}
contract = json.loads((root / 'corpus/tools/dependency-freeze-contract.json').read_text())
fixtures = sorted(path for path in (root / 'corpus/fixtures').iterdir() if path.is_dir())
commands = [['python3', 'corpus/fixtures/check_bible.py', path.relative_to(root).as_posix()] for path in fixtures]
commands += [['python3', 'corpus/tools/dependency_freeze.py', pin['fixture']] for pin in contract['pins'].values()]
commands += [['python3', f'corpus/tools/{tool}.py', 'corpus/fixtures/r100-docket-review'] for tool in ['support_check', 'map_obligations']]
commands += [['python3', 'corpus/tools/discriminate_check.py'], ['python3', 'corpus/tools/discriminate_check.py', '--checker', 'e97613c']]
def run(cmd):
    return cmd, subprocess.run(cmd, cwd=root, capture_output=True, text=True)
with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(run, commands))
census = results[:len(fixtures)]
print('HEAD', subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip())
for rel in docs:
    print('DOC_BASELINE_IDENTICAL', rel, (root / rel).read_bytes() == subprocess.check_output(['git', 'show', 'fe1ce46:' + rel]), 'SHA256', sha(root / rel))
f = (root / docs[0]).read_text(); c = (root / docs[1]).read_text(); w = (root / docs[2]).read_text()
print('FIXTURES_ROUND100_SECTION', any(line.startswith('## Round 100') for line in f.splitlines()))
print('CORPUS_R100_BULLET', any(line.startswith('- `fixtures/r100-docket-review/README.md`') for line in c.splitlines()))
print('C9_R100_ROW', any(line.startswith('| 2026-10-17 (r100) |') for line in w.splitlines()))
print('CENSUS', len(fixtures), 'EXITS', dict(sorted(Counter(done.returncode for cmd, done in census).items())), 'VIOLATIONS', sum(sum(line.startswith('VIOLATION:') for line in done.stdout.splitlines()) for cmd, done in census), 'STDERR_CASES', sum(bool(done.stderr) for cmd, done in census), 'UNEXPECTED', [cmd[-1] for cmd, done in census if done.returncode not in [0, 1] or done.stderr])
for cmd, done in results:
    if cmd[1] == 'corpus/fixtures/check_bible.py' and cmd[-1] != 'corpus/fixtures/r100-docket-review':
        continue
    print('$', ' '.join(cmd))
    if cmd[1] == 'corpus/tools/support_check.py':
        print('\n'.join(line for line in done.stdout.splitlines() if line.startswith(('INVENTORY ', 'SOURCE-SUPPORT ', 'RESULT '))))
    else:
        print(done.stdout, end='')
    print('EXIT', done.returncode, 'STDERR', repr(done.stderr))
baseline = json.loads(subprocess.check_output(['git', 'show', 'fe1ce46:corpus/tools/dependency-freeze-contract.json']))
print('SIX_PRIOR_PINS_UNCHANGED', all(contract['pins'][name] == value for name, value in baseline['pins'].items()))
print('PIN_COUNT', len(contract['pins']), 'PERSISTED_SELF_TEST_EXPECTATIONS', len(contract['self_test']['expected']), 'R100_UNPINNED', 'r100-docket-review' not in contract['pins'])
probe = root / 'corpus/fixtures/r91-c1-tick-unresolved'
print('C9_SCOPE_EXCERPT_FILES', ','.join(sorted(path.name for path in probe.glob('*excerpt*'))))
print('C9_SCOPE_README_LINE3', (probe / 'README.md').read_text().splitlines()[2])
print('INPUT_BYTES_STABLE', all(sha(path) == value for path, value in before.items()), 'FILES', len(before))
PY
```

Observed census and document state:

```text
HEAD b5fe472957ab1e4e9c90f5613acc14cd24a288ae
DOC_BASELINE_IDENTICAL corpus/fixtures/README.md True SHA256 d92c9d2a5db2d10f7e55240a5f3a2875fe188fba1eb90a0772ad9998bc6705a3
DOC_BASELINE_IDENTICAL corpus/README.md True SHA256 975ebd9f0c1108e183af749d50e9529b89d13b55426801e550508ef32f6f6522
DOC_BASELINE_IDENTICAL corpus/knowledge/r91-c9-watch.md True SHA256 76c2d39e523eb6ef4673756a1a30d07722dff2de5a0e4008232ec92be24fc064
FIXTURES_ROUND100_SECTION False
CORPUS_R100_BULLET False
C9_R100_ROW False
CENSUS 174 EXITS {0: 40, 1: 134} VIOLATIONS 421 STDERR_CASES 0 UNEXPECTED []
```

The earlier inherited-only sweep, with the same repo-relative argv convention and `r100-docket-review` deliberately excluded, observed `INHERITED_DIRECT_FIXTURES 173`, `EXIT_COUNTS {0: 39, 1: 134}`, `VIOLATION_LINES 421`, `STDERR_CASES 0`, `UNEXPECTED []`. The census increase is one clean fixture; V20 does not claim a byte-for-byte baseline comparison of all 173 stdout tuples.

Observed final r100 receipts:

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT 0 STDERR ''
$ python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
EXIT 0 STDERR ''
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
EXIT 0 STDERR ''
```

Observed final seven-chain receipts:

```text
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXIT 0 STDERR ''
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
EXIT 0 STDERR ''
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
EXIT 0 STDERR ''
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
EXIT 0 STDERR ''
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
EXIT 0 STDERR ''
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
EXIT 0 STDERR ''
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
EXIT 0 STDERR ''
```

Observed final C9 modes and bounded scope:

```text
$ python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
EXIT 0 STDERR ''
$ python3 corpus/tools/discriminate_check.py --checker e97613c
mode=e97613c checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=False baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=FAIL
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
EXIT 2 STDERR ''
SIX_PRIOR_PINS_UNCHANGED True
PIN_COUNT 7 PERSISTED_SELF_TEST_EXPECTATIONS 18 R100_UNPINNED True
C9_SCOPE_EXCERPT_FILES 
C9_SCOPE_README_LINE3 Fixture scaffolding only; not sourced story evidence.
INPUT_BYTES_STABLE True FILES 23
```

The 23 sampled tool/document/r100-file inputs were byte-stable across this final batch. The expected negative fixtures and historical discriminator control are not unexpected test failures. V20 counted the 18 persisted freeze expectations; it did not run a self-test that would create out-of-ownership repo-root scratch. C3's dated wording and coverage supersession were inspected, but V20 does not independently certify the author's scratch mutation replays.

## Ownership and final handoff

Only authored write: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V20-doc-parity.md`. No per-seat scratch, shared-file edits, fixture mutations, contract writes, nested agents, network, commits, or pushes. The report path was resolved and checked immediately before Write. The sole failed discovery was the initial direct Read of nonexistent lane-root `AGENTS.md`; a recursive AGENTS glob also found none. No needed background task remains.

The three shared-document closure items above remain undone by design under V20's read-only byte ownership. Authorize and perform them at integration, then re-run the quoted document checks; retain this pre-integration finding rather than pretending the gaps were absent.

FAIL — pre-integration doc parity is not yet landed: missing fixtures Round-100/census section, missing corpus r100/current-seven-chain navigation, and missing C9 r100 row; delivered census 174/40/134/421, seven freeze receipts, and r100 structural/map/lexical gates all pass.
