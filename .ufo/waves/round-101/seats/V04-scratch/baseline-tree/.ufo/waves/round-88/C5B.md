## Work performed

- Axes: **first-cause attribution**, **shape-invalid holder detection**, and **false-positive disclosure**.
- Applied the shipped `patches/X1-c1.patch` to a scratch archive of pinned baseline `dfd1fbc3711f2b28597d74444819aca91fe6bc31` at `/tmp/lore-shokunin-C5B-X1-wgAObU`; all probes and checker runs stayed under `/tmp`.
- Compared the original r87 fixture with controls: shape-invalid/ambiguous holder; shape-invalid/unique holder; a minimal garbage-keyed dict with top-level duplicate `to_holder`; unique and nested-value controls; valid shape/ambiguous holder; and valid-key-set/invalid-tick plus ambiguous holder.
- No checker, fixture, other seat artifact, or sibling repo was changed. No commit or push.

## Before → after measurements

**Patch application and compile.** Exact command, run from `/home/vgpnk/Projects/shokunin/lore-shokunin`:

```sh
scratch=$(mktemp -d /tmp/lore-shokunin-C5B-X1-XXXXXX) && git archive dfd1fbc3711f2b28597d74444819aca91fe6bc31 | tar -x -C "$scratch" && printf 'SCRATCH=%s\n' "$scratch" && patch --dry-run --batch -p1 -d "$scratch" < /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-88/patches/X1-c1.patch && patch --batch -p1 -d "$scratch" < /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-88/patches/X1-c1.patch && sha256sum "$scratch/corpus/fixtures/check_bible.py" && PYTHONPYCACHEPREFIX="$scratch/pycache" python3 -m py_compile "$scratch/corpus/fixtures/check_bible.py"
```

Observed output:

```text
SCRATCH=/tmp/lore-shokunin-C5B-X1-wgAObU
checking file corpus/fixtures/check_bible.py
patching file corpus/fixtures/check_bible.py
efe581057b79bbd3dda3d7085686ade31d01363d66c7fcd40affea4753b29ae4  /tmp/lore-shokunin-C5B-X1-wgAObU/corpus/fixtures/check_bible.py
```

The command exited 0; `py_compile` emitted no output.

**Probe matrix.** Probes are copies of `corpus/fixtures/r87-probe-shape-ambiguous` in `/tmp/lore-shokunin-C5B-X1-wgAObU/probes`. Mutations changed only `entities[5].provenance[0]`: `shape-dup` retains `extra: 1`; `shape-unique` changes its `to_holder` to `mira`; `garbage-top-*` replaces the object with `{ "junk": {"x": 1}, "to_holder": <id> }`; `garbage-nested-dup` replaces it with `{ "junk": {"to_holder": "dup"} }`; `valid-shape-dup` removes `extra`; `valid-shape-dup-invalid-tick` removes `extra` and sets `tick=-1`. Baseline checker is from the pinned archive; candidate checker is the patched scratch copy.

Exact matrix command (the subprocess command for each case is `python3 <baseline-or-candidate-checker> <scratch>/probes/<case>`):

```sh
scratch=/tmp/lore-shokunin-C5B-X1-wgAObU && python3 - "$scratch" <<'PY'
import pathlib, subprocess, sys
root = pathlib.Path(sys.argv[1])
cases = ('shape-dup', 'shape-unique', 'garbage-top-dup', 'garbage-top-unique', 'garbage-nested-dup', 'valid-shape-dup', 'valid-shape-dup-invalid-tick')
for variant, checker in (
    ('base', root / 'base/corpus/fixtures/check_bible.py'),
    ('candidate', root / 'corpus/fixtures/check_bible.py'),
):
    for case in cases:
        command = ['python3', str(checker), str(root / 'probes' / case)]
        result = subprocess.run(command, text=True, capture_output=True)
        lines = result.stdout.splitlines()
        selected = [line for line in lines if 'expected exactly tick' in line or '.to_holder: ambiguous entity' in line or 'first stop:' in line or 'because ambiguous holder identity' in line]
        print(f'{variant} {case} exit={result.returncode} findings={sum(line.startswith("VIOLATION:") for line in lines)} stderr={"empty" if not result.stderr else "nonempty"}')
        for line in selected:
            print('  ' + line)
PY
```

Observed output:

```text
base shape-dup exit=1 findings=2 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
base shape-unique exit=1 findings=2 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
base garbage-top-dup exit=1 findings=2 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
base garbage-top-unique exit=1 findings=2 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
base garbage-nested-dup exit=1 findings=2 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
base valid-shape-dup exit=1 findings=5 stderr=empty
  VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[5].provenance[0]
base valid-shape-dup-invalid-tick exit=1 findings=6 stderr=empty
  VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[5].provenance[0]
candidate shape-dup exit=1 findings=5 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
  VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
candidate shape-unique exit=1 findings=4 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set) at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set) at entities[5].provenance[0]
candidate garbage-top-dup exit=1 findings=5 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
  VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
candidate garbage-top-unique exit=1 findings=4 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set) at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set) at entities[5].provenance[0]
candidate garbage-nested-dup exit=1 findings=4 stderr=empty
  VIOLATION: entities[5].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set) at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set) at entities[5].provenance[0]
candidate valid-shape-dup exit=1 findings=4 stderr=empty
  VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
candidate valid-shape-dup-invalid-tick exit=1 findings=5 stderr=empty
  VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
  VIOLATION: entities[5].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick) at entities[5].provenance[0]
  VIOLATION: entities[5].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick) at entities[5].provenance[0]
```

**Verdict from the probes:** exit statuses are unchanged. X1 arms disclosure for the required shape-invalid ambiguity, but the cause selected for the original record is `ambiguous holder identity to_holder 'dup'`, not `malformed record (unexpected field set)`. The unique-holder shape control latches malformed shape; changing only the holder value to duplicated changes the named cause. The minimal top-level garbage-keyed record does the same. By contrast, a nested `junk.to_holder` does not trigger ambiguity, and an invalid tick in a correctly keyed record remains the first named cause even when `to_holder` is ambiguous.

## Findings & named debt

- **Verdict: X1 fails same-record first-cause accuracy.** The exact-key-set gate has already rejected the record before X1 scans holder fields. X1 nevertheless chooses the later-discovered holder ambiguity over that shape stop and calls it the `first stop`; it repeats that cause on the tail. The ambiguity finding itself is true for the top-level field, but the exclusive causal attribution overstates why assessment stopped. To satisfy both C1 requirements, preserve the malformed-shape first stop and separately report the ambiguous holder as a same-record structural finding (or otherwise represent both causes without claiming ambiguity was first).
- **Top-level garbage-key false attribution confirmed; recursive garbage scan falsified.** A record `{ "junk": {"x": 1}, "to_holder": "dup" }` produces the same holder-first disclosure as the fixture; the unique `to_holder: "mira"` control reports malformed shape instead. This is over-disclosure of the operative first cause on a rejected object, not evidence that the duplicate-ID diagnostic is factually false. A nested `{ "junk": {"to_holder": "dup"} }` did not emit a holder ambiguity.
- **Strongest falsification / defensible reading:** because `to_holder` is a recognized top-level key and its value really resolves to duplicated entity IDs, emitting the ambiguity finding is defensible—and the C1 claim explicitly says ambiguous holder ids on shape-invalid dicts must arm disclosure. If “first cause” treats all defects on one record as simultaneous/co-equal, X1's choice can be defended as a deterministic priority. But the patch provides no such documented priority; the key-set gate precedes holder inspection, the shape-only control names shape, and the regular invalid-tick path preserves the earlier cause. Under the wave's actual-first-cause / no-overclaim requirement, that falsification does not rescue the unqualified `first stop: ambiguous holder identity` wording.
- Scope: this is a targeted design attack, not a 145-fixture census or a claim about other C1 residuals. Durable fixture changes, the broader regression census, and assessment of other stop causes remain for the integrating verifier.

## Handoff

- Only `.ufo/waves/round-88/C5B.md` was written in the repo. Scratch archive, applied candidate, and probes: `/tmp/lore-shokunin-C5B-X1-wgAObU`.
- Apply result: dry run and patch application succeeded; patched checker compiled. No patch or code fix is proposed by this critic seat.
