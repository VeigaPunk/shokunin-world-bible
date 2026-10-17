# PROPOSAL ONLY — Round 90 SCORECARD section (W2)

Do not append this draft to `SCORECARD.md` without integration and L1 review. This is a phase-1 scribe proposal, not a closure record. All three claim verdicts remain **PENDING-L1**; scores remain unassigned. A declared requirement or patch is not evidence that it was delivered or verified.

## Round 90 — proposed claim rows (all verdicts pending)

| # | axis / claim | proposed verdict | before → after | evidence and limit |
|---|---|---|---|---|
| C1 | calibration — repair both r89 hedges; pin FN-1 raw-present variants and a ≥3-cause valid-key record; register the FN-2 pair in the canonical census | **PENDING-L1** | **Before at `e97613c`:** 160 fixture dirs, exits `{0: 32, 1: 128}`, 399 violation lines, empty stderr (receipt below). **After:** TODO — no delivered r90 state has been measured by W2. | Required comparison is the complete baseline tuple set against delivered state, with every changed/new/missing path enumerated and **0 exit changes**. The null-from chain must return to definite wording; only identity-dependent comparisons with non-null unresolved IDs may stay qualified; unrelated-identity tick findings must be definite. The fixtures must exercise raw-present/schema-invalid `to_holder`, `from_holder`, and `source_id`, plus ≥3 simultaneous causes under valid keys. The FN-2 pair must be visible in the canonical manifest. Patches, screenshots, and expected output are not a delivered replay. TODO: read the measurement artifacts, independently check exact commands/output and their scope, and leave unmeasured items unresolved. |
| C2 | coverage — in-corpus claim→excerpt maps and R9 modes for r87 and r88-m3; one reproducible support command that enforces R9 | **PENDING-L1** | **Before:** r87 has 5 excerpt-named Markdown files, 0 with a `Delivery mode` label; r88-m3 has 2, 0 labelled. Both clusters have only `symbolism-clause-map.md` among `*map*.md`; these are not the required claim→excerpt maps. **After:** TODO — no delivered r90 state measured by W2. | The r87 map must cover all 22 facts and identify path, line span, and delivery mode; the four delivered r89 excerpts and hymn need mode labels. The r88-m3 map must cover its complete source-attributed set. One committed support script/command must print its observed `N/N` receipt and reject paraphrase/summary-only anchors as source support. `CLEAN` is structural, not prose support; an anchor match is only lexical preflight. The baseline inventory command/output appears below. TODO: verify all map entries against excerpts, replay the single command on the delivered tree, and record any unsupported claims. |
| C3 | depth — govern JDEP2's R8 general-motif/unrecorded-influence, R9 named translator/unknown-version, and R10 same referent name/different occasions cases; re-verify the cross-cluster register is correctly empty | **PENDING-L1** | **Before:** the decision table has 14 pipe-prefixed lines, with R8/R9/R10 rows at lines 24–26; the live register path does not exist. **After:** TODO — no r90 decision or delivered register verification measured by W2. | The baseline table rows and register-path probe are inventoried below; JDEP2's prior probes show the checker is silent and cannot adjudicate these governance cases. Each final decision must state the trigger, owner, and a worked example, without turning a general motif into claimed influence, treating an unknown translation version as identified source text, or treating a shared name as proof of one referent/occasion. An absent register file alone does not prove that no real shared referent exists. TODO: inspect D1/D2 and cross-verification, manually compare both landed clusters, and preserve an empty register only if that comparison supports it. |

### Phase-1 artifact notes (candidate-only; not delivered)

- **C1:** B1/B2 independently provide 160-entry baseline manifests; W2's read-only JSON comparison reports them equal. `X1-tuple-delta.json` labels its candidate `e97613c+X1-scratch` and reports 160 unchanged, 0 changed, 0 added/removed dirs, 0 exit/stderr changes, and both FN-2 pair entries. It carries no patch hash, so it is candidate-only evidence, not a delivered result or a confirmed replay of the latest patch. The current `X1-c1.patch` (SHA-256 `c3573aa082b213e54b2cdf23e92d86dad3f7adc84c76a4de1d8542dac29f5ba5`) returns no identity detail for `None`, gates transition-holder details on both IDs being non-null, and makes the first-record null requirement definite; it still gates tick qualification on `chain_has_ambiguous_source` or non-null transition-holder details. `X1.md` reports a 160-tuple candidate replay and focused null/non-null probes, but its line 6 calls the patch null-only while later sections describe broader gates; reconcile this internal/version mismatch before relying on it as a current-patch receipt. `X2.md` reports a null-only alternative preserving 160 baseline tuples but leaves non-null identity/tick cases unresolved. `X3.md` reports its tick-gating candidate left the 160 baseline tuples unchanged; `S1.md` reports a different candidate changed only `r87-probe-source-prefix` with zero exit changes, leaving an unresolved boundary about source ambiguity versus holder-identity ambiguity. `C8.md`/`C8-delta.json` record 160 unchanged for patch hash `a8b1efd4f36d1d070f4059eac5fb74970d2cac0c05b919267113529c16ed16d5`; that hash does not match the current X1 patch, so it is a compatibility receipt for the older null-only version, not the current patch. F1.md/F1-fixtures.patch report three raw-present variants plus a valid-key three-cause fixture replayed against the unpatched baseline; phase 2 must apply the selected fix with these fixtures and independently replay the delivered tree. No delivered post-fix 160-tuple comparison is available to W2.

  Exact read-only JSON-inspection command (from the lore repo root):

  ```sh
  PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
  import json
  from pathlib import Path
  root = Path('.ufo/waves/round-90/patches')
  b1 = json.loads((root / 'B1-tuples.json').read_text())
  b2 = json.loads((root / 'B2-tuples.json').read_text())
  delta = json.loads((root / 'X1-tuple-delta.json').read_text())
  print(f'B1_count={len(b1)} B2_count={len(b2)} B1_B2_equal={b1 == b2}')
  print('X1_candidate=' + delta['candidate_revision'])
  print(f"X1_unchanged={delta['unchanged_tuple_count']} changed={delta['changed_tuple_count']} added={len(delta['added_directories'])} removed={len(delta['removed_directories'])} exit_changes={len(delta['exit_status_changes'])} stderr_changes={len(delta['stderr_changes'])} fn2_pair_entries={len(delta['fn2_pair_present'])}")
  print('X1_changes=' + repr(sorted(delta['changes'])))
  PY
  ```

  Observed output:

  ```text
  B1_count=160 B2_count=160 B1_B2_equal=True
  X1_candidate=e97613c+X1-scratch
  X1_unchanged=160 changed=0 added=0 removed=0 exit_changes=0 stderr_changes=0 fn2_pair_entries=2
  X1_changes=[]
  ```

  This comparison only validates agreement of candidate-only manifests and reports the contents of the X1 scratch delta artifact; it is not an independent post-fix replay or delivered after-state.
- **C2:** `M1.md` reports a scratch replay of `M1-r87-map.patch` and candidate checks of 22/22 map rows, modes, and declared-line anchors plus 5/5 excerpt labels; these are peer candidate receipts, not a W2 audit or delivered map. `M2-r88m3-map.patch` proposes ten source-attributed JSON facts (four first-appearance pointers, four entity claims, two timeline events) plus two symbolism comparisons; it remains an unreviewed patch, not a delivered map. `M3-support-script.patch` has now landed as a candidate script/README patch, but there is no M3.md or delivered-tree execution receipt. The single support command's exit, `N/N` output, and rejection behavior are therefore unmeasured by W2; no source-support verdict is claimed.
- **C3:** `D1.md` and `D1-decisions.md` now report/propose owners, triggers, and worked examples for R8/R9/R10; `D2-decisions.md` provides a competing proposal. D1.md's 6/6, 7/7, and 9/9 checks are proposal-text completeness only, not governance verification. D1 and D2 materially disagree on R9: D1 withholds R5 support until the source text/version is identified, while D2 permits a narrowly attributed claim about a translation's wording if a reliable tie to the named source work is verified even when its edition is unknown. R10 also differs on the required destination for dismissed name overlaps (D1 requires an incoming-cluster README outcome record; D2 does not). Reconciliation and independent review are TODO; do not silently select either policy. No current cross-cluster register verification has been established.

**W2 baseline receipts (read-only; no scratch files)**

**C1 fixture census.** Command, from the lore repo root at `e97613cc276f5fa9cac49ff1900798cf6863c020`:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from collections import Counter
from pathlib import Path
import subprocess, sys
root = Path('corpus/fixtures')
fixtures = sorted(p for p in root.iterdir() if p.is_dir())
exits = Counter()
violations = 0
stderr_nonempty = 0
for fixture in fixtures:
    result = subprocess.run([sys.executable, str(root / 'check_bible.py'), str(fixture)], capture_output=True, text=True)
    exits[result.returncode] += 1
    violations += sum(line.startswith('VIOLATION:') for line in result.stdout.splitlines())
    stderr_nonempty += bool(result.stderr)
print('baseline=e97613cc276f5fa9cac49ff1900798cf6863c020')
print(f'fixtures={len(fixtures)} exits={dict(sorted(exits.items()))} violation_lines={violations} stderr_nonempty={stderr_nonempty}')
PY
```

Observed output:

```text
baseline=e97613cc276f5fa9cac49ff1900798cf6863c020
fixtures=160 exits={0: 32, 1: 128} violation_lines=399 stderr_nonempty=0
```

This ran read-only against the current tracked baseline with bytecode writing disabled; it is not a post-fix measurement.

**C2/C3 inventory.** Command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
for name in ('r87-myth-cluster', 'r88-m3-maya-cluster'):
    root = Path('corpus/fixtures') / name
    excerpts = sorted(p for p in root.glob('*.md') if 'excerpt' in p.name)
    labelled = [p.name for p in excerpts if any('delivery mode' in line.casefold() for line in p.read_text().splitlines())]
    maps = sorted(p.name for p in root.glob('*map*.md'))
    print(f'{name}: excerpt_files={len(excerpts)} labelled={len(labelled)} labels={labelled} maps={maps}')
table = Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md').read_text().splitlines()
rows = [line for line in table if line.startswith('|')]
print(f'decision_table_pipe_rows={len(rows)} R8_R9_R10={[i + 1 for i, line in enumerate(table) if line.startswith("| R8 ") or line.startswith("| R9 ") or line.startswith("| R10 ")]}')
print(f'cross_cluster_register_exists={Path("corpus/knowledge/cross-cluster-contradictions.md").exists()}')
PY
```

Observed output:

```text
r87-myth-cluster: excerpt_files=5 labelled=0 labels=[] maps=['symbolism-clause-map.md']
r88-m3-maya-cluster: excerpt_files=2 labelled=0 labels=[] maps=['symbolism-clause-map.md']
decision_table_pipe_rows=14 R8_R9_R10=[24, 25, 26]
cross_cluster_register_exists=False
```

`cross_cluster_register_exists=False` describes path presence only; it is not a completed shared-referent comparison.

### TODO before SCORECARD integration

- **C1:** collect the selected candidate and independent replay receipts; compare all 160 prior tuples, enumerate all deltas, verify 0 exit changes, exercise each raw-present variant and ≥3-cause fixture, and demonstrate the FN-2 pair in the canonical manifest.
- **C2:** inspect the delivered r87 22-fact map and complete r88-m3 map; check every line and R9 mode against actual excerpt text; run the one committed support command and retain its exact command, exit code, and `N/N` output, including a paraphrase/summary rejection case.
- **C3:** cite final governed rows for each JDEP2 case with owner, trigger, and worked example; independently compare the clusters and record the evidence for a correctly empty cross-cluster register.
- Keep all verdicts **PENDING-L1** until phase-2 review of the delivered/frozen tree. Do not infer an after-state or award scores from a proposal, missing artifact, or W2 baseline receipt.
