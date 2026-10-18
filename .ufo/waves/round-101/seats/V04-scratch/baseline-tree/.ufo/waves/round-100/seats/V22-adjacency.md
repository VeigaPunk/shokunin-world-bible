# V22 — adjacency (2026-10-17)

Seat scope: PROVINCE byte-identity, write confinement, and rights/mechanics boundaries after production. Axes: charter preservation; lane confinement; rights/permission separation; no game-mechanics adjudication. Baseline `fe1ce46`; observed live HEAD `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`. This is a bounded adjacency verdict, not round-wide admission or a machine-wide filesystem audit.

## Delivery prerequisite

Required all ten r100 fixture files, both new knowledge notes, the existing blind-spot table, contract, tools README, SKILL, and all four producer reports. The actual lane-root `python3` poll used this loop with the concrete required-path list:

```python
for attempt in range(1,41):
 reports={f'T{i}':sorted(p.name for p in seats.glob(f'T{i}*.md') if p.is_file()) for i in range(1,5)}
 absent=[str(p.relative_to(root)) for p in required if not p.is_file() or not p.stat().st_size]
 print(json.dumps({'poll':attempt,'utc':datetime.now(timezone.utc).isoformat(),'producer_reports':reports,'missing_artifacts':absent}),flush=True)
 if all(reports.values()) and not absent:
  print('READY: all four producer reports and all required artifacts exist',flush=True)
  break
 if attempt==40:
  print('ABSENT: bounded 40-poll producer wait exhausted',flush=True)
  raise SystemExit(3)
 time.sleep(20)
```

Observed terminal stdout, exit 0, after 480 seconds (excerpt; all earlier polls were retained in the task output):

```text
{"poll": 25, "utc": "2026-10-18T02:40:30.821275+00:00", "producer_reports": {"T1": ["T1-chain-seven.md"], "T2": ["T2-fixture-author.md"], "T3": ["T3-fixture-docs.md"], "T4": ["T4-knowledge-author.md"]}, "missing_artifacts": []}
READY: all four producer reports and all required artifacts exist
```

The UTC timestamp above is the environment's observed clock; the round's declared local date is retained in this report title. Read all four actual producer reports and delivered artifacts. T2/T3-specific inspections began only after their respective reports existed; the final scope and knowledge inspections followed all-producer readiness. No plan was verified as implementation. No all-reports poll, self-inclusive wait, or stall escape. Background wait snapshots timed out while the producer poll continued; the required poll itself completed normally at 25/40, not ABSENT. No needed background task remains.

## 1. Charter preservation — PASS

Actual read-only child command, invoked from the lane root through `python3`/`subprocess.run`:

```sh
git diff --exit-code fe1ce46 -- PROVINCE.md corpus/fixtures/r99-window-lapse corpus/tools/dependency_freeze.py corpus/fixtures/check_bible.py corpus/tools/support_check.py corpus/tools/map_obligations.py
```

Observed exit 0, `STDOUT ''`, `STDERR ''`. Thus the charter, prior fixture, and those checker implementations are unchanged from the baseline, not merely consistent-looking prose.

Actual baseline bytes were obtained with:

```python
base=subprocess.check_output(['git','show','fe1ce46:PROVINCE.md'],cwd=root)
current=(root/'PROVINCE.md').read_bytes()
```

Observed SHA-256 and exact-byte comparison, repeated after production:

```text
PROVINCE_BASE_SHA256 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
PROVINCE_WORK_SHA256 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
PROVINCE_BYTE_IDENTICAL True
```

`PROVINCE.md:9` still refuses real-world rights claims and game-mechanics verification; line 11 keeps siblings and source trees read-only. SKILL's prefix before `### Dependency-edge freeze check` and the existing freeze scope line were independently byte-compared with baseline; the actual Python check printed:

```text
prefix_before_dependency_freeze_identical True
scope_line_unchanged True
```

The tools README delta is the round-100 append-only coverage addendum. SKILL changes are confined to the freeze registry. No rights/mechanics expansion is hidden in those edits.

## 2. Observable write confinement — PASS, bounded

Actual lane-root `python3` scope audit (read-only):

```python
tracked=subprocess.check_output(['git','diff','--name-only','HEAD','--'],cwd=root,text=True).splitlines()
untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=root,text=True).splitlines()
allowed_tracked={'SKILL.md','corpus/tools/README.md','corpus/tools/dependency-freeze-contract.json','corpus/knowledge/r99-gate-blind-spot-table.md'}
allowed_new={'corpus/knowledge/r100-crossing-arc-synthesis.md','corpus/knowledge/r100-provenance-semantics-boundary.md','.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md'}
seat_scratch=('.ufo/waves/round-100/seats/','.ufo/waves/round-100/scratch/')
unauthorized=[p for p in tracked if p not in allowed_tracked]+[p for p in untracked if p not in allowed_new and not p.startswith(('corpus/fixtures/r100-docket-review/',)+seat_scratch)]
print('SCOPE_AUDIT_INCLUDES_NAMED_PER_SEAT_SCRATCH',json.dumps(seat_scratch))
print('UNAUTHORIZED_LANE_PATHS',json.dumps(unauthorized))
print('OUTSIDE_RESOLUTIONS',json.dumps([p for p in set(tracked+untracked) if not (root/p).resolve().is_relative_to(root)]))
print('NAMED_WAVE_SCRATCH',json.dumps(sorted({str(Path(p).parents[0]) for p in untracked if p.startswith('.ufo/waves/round-100/scratch/')})))
```

Observed exit 0:

```text
SCOPE_AUDIT_INCLUDES_NAMED_PER_SEAT_SCRATCH [".ufo/waves/round-100/seats/", ".ufo/waves/round-100/scratch/"]
UNAUTHORIZED_LANE_PATHS []
OUTSIDE_RESOLUTIONS []
NAMED_WAVE_SCRATCH [".ufo/waves/round-100/scratch/V08-c2-anchors", ".ufo/waves/round-100/scratch/V19-freshness"]
```

Tracked wave deltas observed at `2026-10-18T02:40:40.995489+00:00` were exactly:

```text
SKILL.md
corpus/knowledge/r99-gate-blind-spot-table.md
corpus/tools/README.md
corpus/tools/dependency-freeze-contract.json
```

The twelve new production files are the declared ten-file r100 fixture and two r100 knowledge notes. Other observed additions were wave reports/named per-seat scratch and the **pre-existing** r98 V58 resume note (present in the very first status). Relative to `fe1ce46`, committed LOG/SCORECARD deltas predate the wave: `git diff --name-status fe1ce46 HEAD --` printed only `M LOG.md` and `M SCORECARD.md`.

Audit correction, not concealed: the first allowlist admitted only `seats/` scratch and therefore printed three `OUT_OF_OWNERSHIP_DRIFT` entries: V08's independent anchor script and V19's audit script/output under `round-100/scratch/`. These are named per-seat scratch, not outside-lane writes. V08 explicitly declares its exact scratch path at `.ufo/waves/round-100/seats/V08-c2-anchors.md:11-17`. Including the permitted named scratch class produced the empty unauthorized list above. No foreign file was removed or modified by V22.

Checked the parent-tree wrong-cwd candidates with `Path.exists()` from the lane-root Python audit. All printed `False`:

```text
.ufo/waves/round-100
corpus/fixtures/r100-docket-review
corpus/knowledge/r100-crossing-arc-synthesis.md
corpus/knowledge/r100-provenance-semantics-boundary.md
```

A dedicated Glob of parent `.ufo/waves/round-100/**`, including ignored files, also found no matches. No r100 fixture file is a symlink; none resolves outside the lane. The final ten-artifact stability check additionally rejected symlinks and outside resolutions for its reviewed artifact set.

### Concurrent sibling activity: do not overstate this pass

Actual status command, spawned by the lane-root Python wrapper for the parent and every sibling repository:

```python
result=subprocess.run(['git','status','--short','--untracked-files=all'],cwd=directory,capture_output=True,text=True)
```

Every invocation exited 0 with empty stderr. Parent and all siblings except kotodama were clean at both sweeps. Initial kotodama stdout:

```text
 M tools/harness/packet_links.py
```

At the final sweep it was:

```text
 M tools/harness/packet_links.py
?? reports/round-16/civ/048-059.md
?? reports/round-16/fixes/edge-source.md
?? reports/round-16/scope.md
```

The already-dirty sibling file's actual `hashlib.sha256(p.read_bytes()).hexdigest()` changed during the observation window:

```text
initial f136d30a74fe5ad6f46ccf63c1475b8e8773a10f00a0c57b29cceae5f686f244
final   66d854cc710f0b143e0a254d03e7f59ebce2c6b759d336ca368a9689babbd899
```

Read the delivered sibling record `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-16/scope.md`. Lines 1-8 identify an independent 16-worker round-16; lines 56-61 identify the harness edit as assigned claim-O fixer work; lines 127-132 identify that scribe's own report ownership. This is corroborating evidence of concurrent independent work, **not** proof that all sibling bytes were stationary. There is no observed lore-owned artifact or lore producer delta outside the lore repository. The bounded confinement PASS must not be quoted as an absolute claim that no process wrote anywhere outside lore; a machine-wide no-write claim is not established by these Git snapshots. No sibling content was changed or absorbed.

## 3. Rights/permission and mechanics boundaries — PASS

Read the entire delivered r100 README, map, excerpts, source/event records, both new knowledge notes, the dated blind-spot addendum, and the T1 documentation diff. The rights and AI-training questions remain distinct and unanswered; no age/public-access/attribution-to-permission inference or license grant was found.

Independent baseline-byte check used this actual lane-root Python loop:

```python
for name in ['inspiration-note.md','source-excerpt.md','entities.json','relations.json','contradictions.json']:
 old=subprocess.run(['git','show',f'fe1ce46:corpus/fixtures/r99-window-lapse/{name}'],cwd=root,capture_output=True,check=True).stdout
 current=(fixture/name).read_bytes()
 print(f'BASELINE_BYTE_IDENTITY {name} identical={old==current} sha256={hashlib.sha256(current).hexdigest()}')
 assert old==current
```

Observed all five `identical=True`, exit 0. The two provenance hashes, repeated at the final scope audit, were:

```text
inspiration-note.md 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37
source-excerpt.md   b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd
```

Specific delivered boundaries:

- `corpus/fixtures/r100-docket-review/inspiration-note.md:13-19`: rights not determined for all jurisdictions; AI-training permission unassessed, separate, and not implied by public accessibility or attribution.
- `corpus/fixtures/r100-docket-review/README.md:19-21`: external English-prose design comparison only, neither authenticated K'iche primary text nor in-world witness; no rights/permission grant; lexical/map receipts are not semantic or canon review.
- `corpus/fixtures/r100-docket-review/fictional-excerpts.md:82-88`: review after lapse, entry open, no new filings, no finding, no resolution, both accounts unresolved. No new duty or agreement term is introduced.
- `corpus/fixtures/r100-docket-review/sources.json:51-54` and README lines 11-13: testimony truth and chronology authentication expressly not established; ticks/event IDs are editorial encodings. They are not mechanics validation.
- `corpus/knowledge/r100-crossing-arc-synthesis.md:54-59`: testimony/chronology/authority/canon/rights bounds; neither attribution, age, public access, nor pinning grants permission.
- `corpus/knowledge/r100-provenance-semantics-boundary.md:24-28`: modeled inventory/byte detectability is not whole-claim entailment, truth, canon, copyright status, reuse or training permission, or cultural authority.
- Blind-spot addendum lines 272-375 contains gate corrections and replays only; no rights/mechanics expansion. Its old 20,526 bytes remain an exact prefix; the final Python audit printed `BLIND_SPOT_HISTORICAL_PREFIX True baseline_bytes 20526 added_bytes 8907`.

Actual dedicated Grep calls used this pattern:

```text
(?i)\bmechanics?\b|\bcombat\b|\bdamage\b|\bcooldown\b|hit.?points?|stat.?blocks?|win.?conditions?|\bphysics\b|rules engine
```

- Path `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r100-docket-review`, content mode: `No non-sensitive matches found` (repeated after T3 delivery).
- Path `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/knowledge`, glob `r100*.md`, content mode: `No non-sensitive matches found`.

A separate combined rights/mechanics Grep on those two r100 knowledge files returned exactly the rights-refusal statements at semantics-boundary line 28 and synthesis lines 58-59. The same combined scan on `r99-gate-blind-spot-table.md` returned no matches. These scans are discovery aids, not semantic proof; the complete changed prose was manually read. No gameplay rules, combat/stat balance, simulation correctness, or mechanics-verification conclusion was found. No network fetch or rights adjudication was performed.

## 4. Delivered scenario replay and artifact stability

V22 independently ran these real CLIs concurrently via a lane-root `python3` `ThreadPoolExecutor(max_workers=3)` and captured stdout/stderr/exit:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
```

Complete stdout, exit 0:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
```

Complete stdout, exit 0:

```text
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
```

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

Observed exit 0; excerpt of actual stdout (all J01-J22 and S01-S02 rows were PASS):

```text
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
PASS J22: source-support; mode=verbatim; anchor=found; 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
```

These are structural, inventory, and lexical receipts, not evidence of rights, whole-claim entailment, authenticated chronology, or mechanics. V22 did not re-freeze any contract, mutate fixtures, run live-tree self-test scratch, or claim independent verification of every C1/C3 probe.

Final hash-stability assertions checked charter, r100 README/map/excerpts, both new knowledge records, blind-spot table, contract, SKILL, and tools README against the exact hashes inspected above. Observed exit 0:

```text
REVIEWED_ARTIFACT_STABILITY 10/10; all resolved inside lane; no symlinks
PROVINCE_BYTE_IDENTICAL True
REPORT_PATH_VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V22-adjacency.md
```

Knowledge/contract hashes at final audit:

```text
r100-crossing-arc-synthesis.md       6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc
r100-provenance-semantics-boundary.md 29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36
r99-gate-blind-spot-table.md         f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff
dependency-freeze-contract.json     ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
```

## Seat ownership and residuals

V22 wrote only this absolute report path; no per-seat scratch was created. Before Write, resolved lane root, report parent, exact resolved report path, nonexistence, and non-symlink status were asserted. All shell commands used the lane cwd; Python used `python3`. No production edit, sibling edit, nested agent, commit, push, or network call. Initial AGENTS Read found no lane-root file and recursive Glob found none; an out-of-lane AGENTS reminder followed a read-only sibling inspection, and no changes were made there.

No delivered adjacency failure remains. Explicit residuals: snapshots are not a syscall audit; concurrent sibling round-16 changes were observed and are not silently called unchanged; source authenticity, rights, permission, testimony truth, chronology, whole-proposition semantics, and game mechanics were not adjudicated. The new r100 tick-16 edge remains unpinned by the declared seven-fixture C1 scope, and both knowledge records say so. None of those bounds is converted into a green semantic claim.

PASS — bounded adjacency: PROVINCE byte-identical; no observed lore-owned outside-lane delta; authorized production/report/scratch paths only; rights and AI-training refusals preserved, no game-mechanics claim introduced; concurrent independent sibling drift explicitly excluded from any machine-wide no-write guarantee.
