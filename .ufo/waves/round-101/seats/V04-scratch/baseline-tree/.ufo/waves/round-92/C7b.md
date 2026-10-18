# C7b — Coverage discipline (C2)

Axes: **whole-claim scope**, **inventory-count fidelity**, and **honest warning closure**.

## Work performed

- Read the r92 C2 claim, the R9 rule and appendix, the M1/M2 candidate patches, M2's report, and M4's composed-stack attack report. Checked the source excerpt, authored verse, and symbolism clause map directly. No tracked file or other seat's artifact was edited.
- Polled for the relevant M1/M2/M4 artifacts at 60-second intervals, with a 20-minute deadline. Exact command:

```sh
start=$(date +%s); deadline=$((start + 1200)); n=0; printf 'POLL_START at=%s deadline_seconds=1200 targets=M1,M2,M4\n' "$(date -Is)"; while [ "$(( $(date +%s) - start ))" -lt 1200 ]; do n=$((n + 1)); elapsed=$(( $(date +%s) - start )); ready=0; details=''; for seat in M1 M2 M4; do found=0; for p in ".ufo/waves/round-92/${seat}.md" .ufo/waves/round-92/patches/${seat}-*; do if [ -f "$p" ]; then details="$details ${seat}=$p"; found=1; fi; done; if [ "$found" -eq 1 ]; then ready=$((ready + 1)); else details="$details ${seat}=pending"; fi; done; printf 'POLL_CHECK elapsed=%ss checks=%s%s\n' "$elapsed" "$n" "$details"; if [ "$ready" -eq 3 ]; then printf 'POLL_HIT all-targets-present elapsed=%ss checks=%s\n' "$elapsed" "$n"; exit 0; fi; sleep 60; done; printf 'POLL_TERMINAL status=0 reason=deadline elapsed=%ss checks=%s\n' "$(( $(date +%s) - start ))" "$n"
```

Observed poll receipt (the M1 patch appeared on the first check; all three target artifacts were present after 360 seconds):

```text
POLL_START at=2026-10-17T08:58:57-03:00 deadline_seconds=1200 targets=M1,M2,M4
POLL_CHECK elapsed=0s checks=1 M1=.ufo/waves/round-92/patches/M1-spence-rows.patch M2=.ufo/waves/round-92/patches/M2-contract.patch M4=pending
POLL_CHECK elapsed=60s checks=2 M1=.ufo/waves/round-92/patches/M1-spence-rows.patch M2=.ufo/waves/round-92/patches/M2-contract.patch M4=pending
POLL_CHECK elapsed=120s checks=3 M1=.ufo/waves/round-92/patches/M1-spence-rows.patch M2=.ufo/waves/round-92/patches/M2-contract.patch M4=pending
POLL_CHECK elapsed=180s checks=4 M1=.ufo/waves/round-92/patches/M1-spence-rows.patch M2=.ufo/waves/round-92/patches/M2-contract.patch M4=pending
POLL_CHECK elapsed=240s checks=5 M1=.ufo/waves/round-92/patches/M1-spence-rows.patch M2=.ufo/waves/round-92/patches/M2-contract.patch M4=pending
POLL_CHECK elapsed=300s checks=6 M1=.ufo/waves/round-92/patches/M1-spence-rows.patch M2=.ufo/waves/round-92/patches/M2-contract.patch M4=pending
POLL_CHECK elapsed=360s checks=7 M1=.ufo/waves/round-92/patches/M1-spence-rows.patch M2=.ufo/waves/round-92/patches/M2-contract.patch M4=.ufo/waves/round-92/M4.md
POLL_HIT all-targets-present elapsed=360s checks=7
```

- Whole-claim manual scope cross-check command:

```sh
python3 - <<'PY'
from pathlib import Path
root = Path('corpus/fixtures/r88-m3-maya-cluster')
source = (root / 'source-excerpt.md').read_text(encoding='utf-8')
fiction = (root / 'fictional-excerpts.md').read_text(encoding='utf-8')
clause_map = (root / 'symbolism-clause-map.md').read_text(encoding='utf-8')
patch = Path('.ufo/waves/round-92/patches/M1-spence-rows.patch').read_text(encoding='utf-8')
checks = [
    ('S1', 'He called out “Earth,”', 'We leave its name unowned in the rain.', 'A name can be treated as provisional rather than as a claim of ownership.'),
    ('S2', 'and the solid land appeared.', 'The chalk stair stays a crossing, never a map.', 'The verse contrasts a mark or crossing with the making of a place.'),
]
for label, src, authored, reading in checks:
    assert src in source and authored in fiction and reading in clause_map
    assert src in patch and authored in patch
    print(f'{label}: source_clause=present authored_clause=present editorial_reading=present patch_row=present')
for boundary in ('not claims about K\'iche symbolism', 'does not attribute a naming custom or rule to K\'iche people', 'does not assert world-making, magic, or a historical event', 'not evidence of direct borrowing or of a general cultural meaning'):
    assert boundary in clause_map
print('R9_SCOPE_BOUNDARIES=4/4; source_representation=Spence English prose; underlying K\'iche text=external-only')
PY
```

Observed:

```text
S1: source_clause=present authored_clause=present editorial_reading=present patch_row=present
S2: source_clause=present authored_clause=present editorial_reading=present patch_row=present
R9_SCOPE_BOUNDARIES=4/4; source_representation=Spence English prose; underlying K'iche text=external-only
```

The initial M1 draft had a bad hunk count. Exact dry-run command:

```sh
patch --dry-run --batch --fuzz=0 -p1 -d "$scratch" < .ufo/waves/round-92/patches/M1-spence-rows.patch
```

Observed on that initial version: `checking file corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md`, then `patch: **** malformed patch at line 38:` (exit 2). M1 revised the hunk (`+19` to `+17`); the final patch hash is `74ecdcdcc175f726c1afa9676c5d027d990b2aeb429320f752acec703360fd9a`. The final M1 and M2 patches passed standard `git apply --check` and apply in the scratch composition below.

## Before → after measurements

Raw JSON support-pointer count command:

```sh
python3 -c 'import json; from pathlib import Path; p=Path("corpus/fixtures/r88-m3-maya-cluster"); e=json.loads((p/"entities.json").read_text()); t=json.loads((p/"timeline.json").read_text()); r=json.loads((p/"relations.json").read_text()); c=json.loads((p/"contradictions.json").read_text()); first=sum("first_appearance" in row for row in e); claims=sum(len(row.get("claims", [])) for row in e); print(f"JSON_SUPPORT_FACTS={first}+{claims}+{len(t)}={first+claims+len(t)}; entities={len(e)} timeline={len(t)} relations={len(r)} contradictions={len(c)}; editorial_rows=2; total=12")'
```

Observed: `JSON_SUPPORT_FACTS=4+4+2=10; entities=4 timeline=2 relations=0 contradictions=0; editorial_rows=2; total=12`. The two `sources.json` registry rows are not claim-support facts; the ten mapped JSON facts are four entity first-appearance pointers, four entity claims, and two timeline events.

Baseline support command:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
```

Observed relevant output before M1:

```text
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6
WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)
RESULT PASS WITH WARNINGS
EXIT=0
```

Composed after-state command (only the two checker/map files were copied to scratch; both patches were applied there; checker reads the real cluster excerpts):

```sh
set -eu
root=$PWD
scratch=$(mktemp -d /tmp/c7b-compose.XXXXXX)
trap 'rm -rf "$scratch"' EXIT
mkdir -p "$scratch/corpus/tools" "$scratch/corpus/fixtures/r88-m3-maya-cluster"
cp corpus/tools/support_check.py "$scratch/corpus/tools/support_check.py"
cp corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md "$scratch/corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md"
for patchfile in .ufo/waves/round-92/patches/M1-spence-rows.patch .ufo/waves/round-92/patches/M2-contract.patch; do
  (cd "$scratch" && git apply --check "$root/$patchfile" && git apply "$root/$patchfile")
  printf 'PATCH_APPLY %s=PASS\n' "${patchfile##*/}"
done
printf 'COMMAND: python3 %s %s --map %s\n' "$scratch/corpus/tools/support_check.py" "$root/corpus/fixtures/r88-m3-maya-cluster" "$scratch/corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md"
python3 "$scratch/corpus/tools/support_check.py" "$root/corpus/fixtures/r88-m3-maya-cluster" --map "$scratch/corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md"
printf 'EXIT=%s\n' "$?"
printf 'SCRATCH_SWEPT=YES_ON_EXIT\n'
```

Observed output (temporary directory was `/tmp/c7b-compose.e8l5sB`):

```text
PATCH_APPLY M1-spence-rows.patch=PASS
PATCH_APPLY M2-contract.patch=PASS
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS P1: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS P2: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS P3: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS P4: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS E1: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS E2: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS E3: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS E4: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS T1: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS T2: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS S1: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S2: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
EXIT=0
SCRATCH_SWEPT=YES_ON_EXIT
```

M4 independently tested the Spence declaration mode-flip on this composed stack. Its exact mutation/run statements are in `.ufo/waves/round-92/M4.md` (lines 214–217); observed output there (lines 274–281) is exit 1, `FAIL: S1: delivery mode missing or mismatched`, `FAIL: S2: delivery mode missing or mismatched`, `RESULT FAIL`. Thus a now-referenced excerpt is not silently treated as unreferenced: a declaration mismatch fails both rows.

## Findings & named debt

- **Inventory improved and matches the raw data:** 10 JSON facts + 2 editorial comparison rows = 12 total; the distinct `(excerpt path, exact anchor)` pairs move 6→8. The ten JSON rows remain the 10 source-attributed entity/timeline facts; the two new rows do not inflate that JSON count or become in-world facts.
- **The two Spence comparisons are bounded editorial readings.** S1 maps the delivered English clause “He called out ‘Earth,’” to the newly authored line “We leave its name unowned in the rain”; S2 maps “and the solid land appeared” to “The chalk stair stays a crossing, never a map.” The map identifies the reading as about the authored verse, not K’iche symbolism, and explicitly keeps the underlying K’iche primary text `external-only`. The R9 mode applies to Spence’s delivered English prose, not to an absent K’iche-language edition. No whole-culture, historical, magic, or canon claim is warranted.
- **WARN closed by a real reference, not suppression.** Before the rows, `source-excerpt.md` was declared but unused. Afterward both S1/S2 rows name `source-excerpt.md:5`, and the composed receipt is `RESULT PASS` with no warning. M4’s mode-flip probe shows the declared source excerpt is actively checked; the wrong mode becomes `RESULT FAIL` rather than disappearing behind warning logic.
- **Named manual-review limit:** the support checker’s `EDITORIAL-ANCHORS 2/2` validates only each row’s source-side lexical anchor. It does not validate the authored-side wording or decide whether the editorial interpretation follows from the juxtaposition. Those lines/readings were manually matched to `fictional-excerpts.md` and `symbolism-clause-map.md`; this remains an R9 editorial screen, not a semantic or cultural-fidelity certification.
- `M1.md` was absent at the latest artifact check; the final M1 patch was present and composed successfully. `M2.md` and `M4.md` were present. No dependency deadline was reached: the C2 artifacts arrived at 360 seconds.

## Handoff

- Deliverable: `.ufo/waves/round-92/C7b.md` only. No project-tracked files were modified; no commit or push. HEAD remained `396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f`; `git diff --quiet HEAD --` and `git diff --cached --quiet` both returned 0.
- `/tmp` preflight command: `df -i /tmp`; observed `tmpfs 1048576 1033089 15487 99% /tmp`. Scratch was limited to a small composition tree and removed by the trap (`C7B_SCRATCH_SWEPT=YES`).
- Verification: final M1/M2 standard patch application and the end-to-end r88 checker run passed in scratch. No general project test suite was run; this seat verified the C2 coverage surfaces only.
