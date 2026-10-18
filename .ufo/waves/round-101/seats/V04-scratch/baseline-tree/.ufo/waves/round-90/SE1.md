## Work performed

- Axes: **candidate provenance** (which patch bytes each receipt actually tested); **coverage and operability** (whether C1/C2 claims are pinned and reproducible); **governance integrity** (R8–R10 policy and register boundaries); and **process fidelity** (cutoffs, roster, and write scope).
- Audited the round-90 spec, all 28 peer seat reports, and the current 22-file `patches/` inventory. Read only phase-1 round-90 artifacts; did not open `followup/` or Q1's referenced follow-up JSON. No candidate patch was applied, no tracked file was changed, and no commit or push was made.
- The audited baseline remains `e97613cc276f5fa9cac49ff1900798cf6863c020`. Candidate measurements below are scratch/candidate receipts, not an integrated or frozen after-state.

## Before → after measurements

### Current inventory and tracked-tree boundary

Exact command from `lore-shokunin/`:

```sh
git rev-parse HEAD; git status --short; git diff --quiet; printf 'tracked_worktree_diff_exit=%s\n' "$?"; git diff --cached --quiet; printf 'tracked_index_diff_exit=%s\n' "$?"; python3 - <<'PY'
from pathlib import Path
import re
root=Path('.ufo/waves/round-90')
spec=(root/'wave-spec.md').read_text()
declared=int(re.search(r'Phase 1 \(this spec\): WORK wave, (\d+) seats',spec).group(1))
roster=re.findall(r'^\| ([A-Z]+\d+) \| 1 \|',spec,re.M)
reports=sorted(p.stem for p in root.glob('*.md') if p.name!='wave-spec.md')
patches=sorted(p.name for p in (root/'patches').iterdir() if p.is_file())
print(f'declared_seats={declared} roster_rows={len(roster)} roster_ids={roster}')
print(f'peer_reports={len(reports)} peer_report_ids={reports}')
print(f'missing_reports={sorted(set(roster)-set(reports))}')
print(f'patch_files={len(patches)} se1_report_exists={(root/"SE1.md").exists()}')
PY
```

Observed before writing this report:

```text
e97613cc276f5fa9cac49ff1900798cf6863c020
?? .ufo/waves/round-90/
tracked_worktree_diff_exit=0
tracked_index_diff_exit=0
declared_seats=32 roster_rows=29 roster_ids=['B1', 'B2', 'B3', 'S1', 'S2', 'X1', 'X2', 'X3', 'F1', 'C5', 'C6', 'C8', 'E1', 'M1', 'M2', 'M3', 'M4', 'C7', 'K1', 'D1', 'D2', 'T1', 'R1', 'J3', 'E2', 'W1', 'W2', 'Q1', 'SE1']
peer_reports=28 peer_report_ids=['B1', 'B2', 'B3', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'E1', 'E2', 'F1', 'J3', 'K1', 'M1', 'M2', 'M3', 'M4', 'Q1', 'R1', 'S1', 'S2', 'T1', 'W1', 'W2', 'X1', 'X2', 'X3']
missing_reports=['SE1']
patch_files=22 se1_report_exists=False
```

The spec's 32-seat declaration therefore exceeds its 29 roster rows by three; all 28 peer seats in the actual roster now have reports. The W1 landing-record patch is a `06:12:29-03:00` cutoff snapshot (17/29 listed seats had an artifact then), not the later inventory above.

### C1 baseline and current X1 candidate receipt

C8's recorded baseline command and output:

```sh
python3 /tmp/lore-r90-C8-measure.py capture --root /tmp/lore-r90-C8-baseline.PG9K4w --output /tmp/lore-r90-C8-baseline.PG9K4w.baseline.json --revision e97613c
```

```text
directories=160 exit_counts={"0": 32, "1": 128} stderr_cases=0 violation_lines=399
capture=/tmp/lore-r90-C8-baseline.PG9K4w.baseline.json
checker_sha256=e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
```

Exact current-byte reconciliation command:

```sh
sha256sum .ufo/waves/round-90/patches/B1-tuples.json .ufo/waves/round-90/patches/B2-tuples.json .ufo/waves/round-90/patches/X1-c1.patch .ufo/waves/round-90/patches/C8-delta.json .ufo/waves/round-90/patches/M1-r87-map.patch .ufo/waves/round-90/patches/M2-r88m3-map.patch .ufo/waves/round-90/patches/M3-support-script.patch .ufo/waves/round-90/patches/F1-fixtures.patch; cmp -s .ufo/waves/round-90/patches/B1-tuples.json .ufo/waves/round-90/patches/B2-tuples.json; printf 'B1_B2_bytes_equal_exit=%s\n' "$?"; python3 - <<'PY'
import json
from pathlib import Path
p=Path('.ufo/waves/round-90/patches/C8-delta.json')
d=json.loads(p.read_text())
print(f"C8_receipt_patch_sha256={d['patch']['sha256']}")
print(f"C8_receipt_checker_sha256={d['captures']['after']['checker_sha256']}")
print(f"C8_receipt_unchanged={d['delta']['unchanged_tuple_count']} changed={d['delta']['changed_tuple_count']} exit_changes={len(d['delta']['exit_status_changes'])} stderr_changes={len(d['delta']['stderr_changes'])}")
print(f"C8_receipt_changed_fixture={d['delta']['changed_fixture_names']}")
PY
```

Observed:

```text
80bdc3b45ea785ea7e04dea776d95da0bd6dad088f60ae95100f21039cae42ad  .ufo/waves/round-90/patches/B1-tuples.json
80bdc3b45ea785ea7e04dea776d95da0bd6dad088f60ae95100f21039cae42ad  .ufo/waves/round-90/patches/B2-tuples.json
6d37eccfb913155aabd6e4e883870eab68676920dca1142d6d4482ae79316223  .ufo/waves/round-90/patches/X1-c1.patch
e867eb8d945b17809db646ddfa73850e59df137a38a4bcff2d2372bc7f47df95  .ufo/waves/round-90/patches/C8-delta.json
7ce7487466e048a1e656b7e9bcf594392f3b1c51286650ab0c955b156bcc4187  .ufo/waves/round-90/patches/M1-r87-map.patch
8fc7973d38d261f946235a1483a1b325fbb43c98e4122e4ff1ebdd19f9d48ad6  .ufo/waves/round-90/patches/M2-r88m3-map.patch
988cac6a4b7ea2f85feaeb034e0adb0a85b3d9c089525685118d6e3a888aef6e  .ufo/waves/round-90/patches/M3-support-script.patch
5590f3b636dd5fe5e311f96a87e89c2a1dc7e3e163dbda5df662d6957cd92119  .ufo/waves/round-90/patches/F1-fixtures.patch
B1_B2_bytes_equal_exit=0
C8_receipt_patch_sha256=6d37eccfb913155aabd6e4e883870eab68676920dca1142d6d4482ae79316223
C8_receipt_checker_sha256=12866e734beb0e8fdfb641e9dab7cdaae7518fc0fdb8749a5e086981a0d1ae18
C8_receipt_unchanged=159 changed=1 exit_changes=0 stderr_changes=0
C8_receipt_changed_fixture=['corpus/fixtures/r87-probe-source-prefix']
```

C8's final replay command was `python3 /tmp/lore-r90-C8-measure.py compare --before /tmp/lore-r90-C8-baseline.PG9K4w.baseline.json --after /tmp/lore-r90-C8-X1stable.sBAwBm.after.json --output .ufo/waves/round-90/patches/C8-delta.json --patch .ufo/waves/round-90/patches/X1-c1.patch --patch-sha256 6d37eccfb913155aabd6e4e883870eab68676920dca1142d6d4482ae79316223`; C8 recorded `unchanged_tuples=159 changed_tuples=1 added_fixtures=0 removed_fixtures=0 exit_status_changes=0 stderr_changes=0`, with the only change `r87-probe-source-prefix`. This is a candidate replay, not a delivered-tree measurement.

### Artifact-wait timing

The resumed one-call poll was:

```sh
for check in {3..20}; do sleep 60; printf 'check %s at ' "$check"; date --iso-8601=seconds; printf '%s\n' 'round-90 entries:'; ls -1A .ufo/waves/round-90; if [ -d .ufo/waves/round-90/patches ]; then printf '%s\n' 'patch entries:'; ls -1A .ufo/waves/round-90/patches; else printf '%s\n' 'patches directory absent'; fi; done
```

The exact log-summary command was:

```sh
python3 - <<'PY'
from pathlib import Path
import re
p=Path('/home/vgpnk/.kimi-code/sessions/wd_shokunin_8c4a99c6228c/session_812e7ffb-509b-48a4-8999-22134315ef0e/agents/agent-251/tasks/bash-vpyukv22/output.log')
lines=p.read_text().splitlines()
checks=[]
for i,line in enumerate(lines):
 m=re.fullmatch(r'check (\d+) at (\S+)',line)
 if m: checks.append((int(m.group(1)),m.group(2)))
print(f'logged_checks={len(checks)} first_logged={checks[0]} last_logged={checks[-1]}')
print('milestone_checks='+repr([item for item in checks if item[0] in (3,15,20)]))
PY
```

Observed:

```text
logged_checks=18 first_logged=(3, '2026-10-17T06:00:56-03:00') last_logged=(20, '2026-10-17T06:17:56-03:00')
milestone_checks=[(3, '2026-10-17T06:00:56-03:00'), (15, '2026-10-17T06:12:56-03:00'), (20, '2026-10-17T06:17:56-03:00')]
```

Two earlier checks were at `05:52:56` and `05:53:56` and saw only `wave-spec.md`; the resumed loop therefore had an approximately seven-minute sampling gap. Check 15 sampled the 20-minute mark; check 20 continued beyond it. W1's cutoff was `06:12:29`, between checks 14 and 15. Later phase-1 reports, including C6/C7/M4/T1, arrived after that cutoff, so their absence in W1's snapshot is not evidence of seat failure.

### C2 and C3 denominators / candidate checks

S2's exact fact-inventory command and output:

```sh
python3 - <<'PY'
import json
from pathlib import Path
root = Path('corpus/fixtures')
for cluster in ('r87-myth-cluster', 'r88-m3-maya-cluster'):
    base = root / cluster
    entities = json.loads((base / 'entities.json').read_text())
    relations = json.loads((base / 'relations.json').read_text())
    timeline = json.loads((base / 'timeline.json').read_text())
    first = sum(bool(entity.get('first_appearance')) for entity in entities)
    claims = sum(len(entity.get('claims', [])) for entity in entities)
    total = first + claims + len(relations) + len(timeline)
    print(f'{cluster}: first_appearance={first} entity_claims={claims} relations={len(relations)} timeline={len(timeline)} total={total}')
PY
```

```text
r87-myth-cluster: first_appearance=7 entity_claims=7 relations=4 timeline=4 total=22
r88-m3-maya-cluster: first_appearance=4 entity_claims=4 relations=0 timeline=2 total=10
```

M4's exact R9 attack harness is recorded in `M4.md:117-165`; it changed the E1 map locator from line 7 to line 6 in scratch and invoked the candidate checker. Observed attack output:

```text
wrong-line: exit=0
PASS E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.
SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS
```

T1's bounded baseline identity comparison command and output:

```sh
python3 - <<'PY'
from pathlib import Path
import json
root = Path('corpus/fixtures')
clusters = ('r87-myth-cluster', 'r88-m3-maya-cluster')
def load(cluster, name):
    return json.loads((root / cluster / name).read_text())
a, b = (load(c, 'entities.json') for c in clusters)
a_ids, b_ids = ({row['id'] for row in rows} for rows in (a, b))
a_names, b_names = ({row['name'].casefold() for row in rows} for rows in (a, b))
a_events, b_events = (load(c, 'timeline.json') for c in clusters)
a_event_ids, b_event_ids = ({row['id'] for row in rows} for rows in (a_events, b_events))
print('clusters=' + '|'.join(clusters))
print('shared_entity_ids=' + repr(sorted(a_ids & b_ids)))
print('shared_entity_names_casefold=' + repr(sorted(a_names & b_names)))
print('shared_timeline_event_ids=' + repr(sorted(a_event_ids & b_event_ids)))
PY
```

```text
clusters=r87-myth-cluster|r88-m3-maya-cluster
shared_entity_ids=[]
shared_entity_names_casefold=[]
shared_timeline_event_ids=[]
```

J3's broader patch-replay comparison additionally found empty intersections for source IDs, places, timeline place references, and normalized relation tuples; the live register remained absent. These are identity-screen results on the two named clusters, not a general semantic proof.

## Findings & named debt

- **C1 — current patch and receipt are version-aligned, but the wider probe record is not.** Current `X1-c1.patch` is `6d37eccf…`; C8's current receipt names that same hash and checker `12866e73…`. C5 instead reports its five-probe “final” patch as `c3573aa0…` and checker `2f3ca9f1…`. Do not transfer C5's PASS—especially its first-record case—to the current patch. The current patch contains the null-ID guard and narrows the tick qualifier to unresolved transition-holder details, but does not edit the first-record branch; X1's `first-unresolved` probe remains qualified. Decide explicitly whether the positional first-record rule also loses an identity hedge.
- **C1 — tick semantics remain a policy choice.** X1/S1 retain qualification when a genuinely unresolved non-null holder is part of the compared transition; X3 removes holder-identity qualification from tick findings. The persisted “identity-dependent comparisons only” wording and the separate “genuinely unresolved compared holders stay qualified” clause need one explicit interpretation before integration. F1's three raw-present cases (`to_holder`, `from_holder`, `source_id`) and ≥3-cause record were replayed only against the unpatched baseline; rerun them with the selected checker and the 160-fixture census after integration.
- **C2 — `22/22` does not yet mean all 22 R87 JSON facts.** The current R87 map table/receipt counts 14 JSON-fact rows plus eight editorial hymn interpretations. Six first-appearance pointers are co-mapped in those rows; the remaining first-appearance pointer and the hymn-sourced JSON claim are described in prose, not separately validated by the checker. Keep the 22-pointer JSON denominator separate from H1–H8 and require complete pointer/source-ID validation. The revised M1 locators were checked as 22/22 exact lines by C7; M3's earlier stale E1 `:6` concern was corrected in the current M1 patch. The checker defect remains: it parses/stores `span` but does not pass or enforce it, as M4's wrong-line attack confirms.
- **C2 — R9 scope and receipt shape remain open.** M2 labels the delivered Spence excerpt `external-only` in a `Delivery mode` field, but R9 modes are `verbatim`, `translation`, `paraphrase`, and `summary`; external/in-world status is a separate scope dimension. Keep R3's charter wording bounded to a pledge, not proof of performance. M3 README supplies one command per cluster rather than one aggregate invocation; S2's proposed receipt is per-cluster 22/22 + 10/10 plus aggregate 32/32. Resolve whether “one command” means the script utility or one invocation/aggregate receipt. Also make a required paraphrase/summary row fail full-fact N/N rather than allowing a PASS over only eligible source rows.
- **C3 — proposals are not policy.** D1 and D2 differ on R8's provisional marker (D1 uses `external-only / unverified inspiration` at review trigger; D2 uses a neutral `possible influence: unverified` note) and R9's unknown-version threshold (D1 requires identified source/version; D2 allows a narrowly scoped claim with a reliable tie to a named work). R1 recommends D1-style appendices with D2's safer gates; the JDEP2 translation example without a reliable work-level tie fails either approach. D1, D2, and T1 all point R10 comparison outcomes to the incoming cluster README; W2's statement that D2 omits that destination is contradicted by D2's actual patch. Integrate one non-duplicative rule set and preserve the prospective r87/r88 boundary.
- **R10 register — no entry is justified on the inspected evidence.** J3 and T1 find no shared IDs/names/places/relation tuples or occasion across r87/r88-m3; R87's Hara/Sen conflict is local, and the r89 demonstration is explicitly hypothetical. Keep the live register absent unless source-backed evidence establishes the same referent, field, and occasion with incompatible assertions.
- **Process debt:** the roster count discrepancy (32 declared vs 29 listed) is data debt. W1's patch is only a cutoff landing record; use the current inventory for phase-2 selection. No candidate was integrated or frozen here, so no delivered-tree after-state or final C1/C2/C3 closure is claimed.

## Handoff

- Before closure, select and apply the C1 behavior, resolve the first-record and tick boundaries, integrate F1, and rerun all baseline fixtures plus the four new fixtures with exact exit/stdout/stderr receipts and zero exit flips.
- Repair C2's 22-pointer denominator, separate delivery mode from external scope, enforce line spans and complete pointer/source-ID coverage, clarify aggregate-command expectations, and replay R9 negative controls on the integrated tree.
- Integrate one R8–R10 policy set, record R10 comparison outcomes in incoming-cluster READMEs, verify the live register stays absent on the frozen tree, then perform the spec's freeze-then-verify pass.
- SE1's only repository write is `.ufo/waves/round-90/SE1.md`. No patch was applied; no tracked file, commit, or push was produced.