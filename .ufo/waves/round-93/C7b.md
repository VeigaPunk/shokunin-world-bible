# C7b — Coverage discipline (C2)

## Work performed

Axes: **whole-claim coverage**, **map/inventory fidelity**, and **honest R9 / sourced-inspiration boundaries**.

- Read the round-93 wave spec, the R8–R10 rules and support-check contract, S2's family recommendation, and the available M1 (Kojiki) and M3 (Ovid) candidate patches/reports. Read the new-cluster content directly from the patches; neither patch was applied to the repository.
- Polled the C2 M1–M6 reports/patches every 60 seconds for 1,200 seconds. Exact matching-receipt command:

```sh
set -u; elapsed=0; checks=0; while [ "$elapsed" -lt 1200 ]; do ready=0; details=''; for seat in M1 M2 M3 M4 M5 M6; do found=''; for p in ".ufo/waves/round-93/${seat}.md" .ufo/waves/round-93/patches/${seat}-*; do if [ -f "$p" ]; then found="$p"; break; fi; done; if [ -n "$found" ]; then details="$details ${seat}=$found"; ready=$((ready+1)); else details="$details ${seat}=pending"; fi; done; printf 'POLL_CHECK elapsed=%ss checks=%s ready=%s/6%s\n' "$elapsed" "$checks" "$ready" "$details"; if [ "$ready" -eq 6 ]; then printf 'POLL_HIT all-C2-seat-artifacts-present elapsed=%ss checks=%s\n' "$elapsed" "$checks"; exit 0; fi; sleep 60; elapsed=$((elapsed + 60)); checks=$((checks+1)); done; printf 'POLL_TERMINAL status=0 reason=deadline elapsed=%ss checks=%s\n' "$elapsed" "$checks"
```

Observed poll output (the process reached the 1,200-second runner timeout before printing a terminal line; last logged check was t=1,140s):

```text
POLL_CHECK elapsed=0s checks=0 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=60s checks=1 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=120s checks=2 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=180s checks=3 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=240s checks=4 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=300s checks=5 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=360s checks=6 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=420s checks=7 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=480s checks=8 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=540s checks=9 ready=0/6 M1=pending M2=pending M3=pending M4=pending M5=pending M6=pending
POLL_CHECK elapsed=600s checks=10 ready=1/6 M1=pending M2=pending M3=.ufo/waves/round-93/patches/M3-ovid-cluster.patch M4=pending M5=pending M6=pending
POLL_CHECK elapsed=660s checks=11 ready=1/6 M1=pending M2=pending M3=.ufo/waves/round-93/patches/M3-ovid-cluster.patch M4=pending M5=pending M6=pending
POLL_CHECK elapsed=720s checks=12 ready=1/6 M1=pending M2=pending M3=.ufo/waves/round-93/patches/M3-ovid-cluster.patch M4=pending M5=pending M6=pending
POLL_CHECK elapsed=780s checks=13 ready=1/6 M1=pending M2=pending M3=.ufo/waves/round-93/patches/M3-ovid-cluster.patch M4=pending M5=pending M6=pending
POLL_CHECK elapsed=840s checks=14 ready=2/6 M1=.ufo/waves/round-93/patches/M1-cluster3.patch M2=pending M3=.ufo/waves/round-93/patches/M3-ovid-cluster.patch M4=pending M5=pending M6=pending
POLL_CHECK elapsed=900s checks=15 ready=2/6 M1=.ufo/waves/round-93/patches/M1-cluster3.patch M2=pending M3=.ufo/waves/round-93/patches/M3-ovid-cluster.patch M4=pending M5=pending M6=pending
POLL_CHECK elapsed=960s checks=16 ready=2/6 M1=.ufo/waves/round-93/M1.md M2=pending M3=.ufo/waves/round-93/patches/M3-ovid-cluster.patch M4=pending M5=pending M6=pending
POLL_CHECK elapsed=1020s checks=17 ready=2/6 M1=.ufo/waves/round-93/M1.md M2=pending M3=.ufo/waves/round-93/M3.md M4=pending M5=pending M6=pending
POLL_CHECK elapsed=1080s checks=18 ready=2/6 M1=.ufo/waves/round-93/M1.md M2=pending M3=.ufo/waves/round-93/M3.md M4=pending M5=pending M6=pending
POLL_CHECK elapsed=1140s checks=19 ready=2/6 M1=.ufo/waves/round-93/M1.md M2=pending M3=.ufo/waves/round-93/M3.md M4=pending M5=pending M6=pending
```

- Among the M1–M6 C2 dependencies at the post-deadline inventory, only M1/M3 reports and their two candidate patches existed; M2, M4 receipt, M5 convergence, M6 independent review, and an integrated `corpus/fixtures/r93*` tree were absent. The S2 scout report was present and recommended M1's Japanese *Kojiki* candidate, but no M5 convergence artifact was available to make that the landed selection.

## Before → after measurements

**Baseline receipts.** Exact commands and observed summary lines:

```text
$ python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS

$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
```

**M1 / Japanese *Kojiki* candidate.** The patch was applied only in a temporary tree. Exact command sequence:

```sh
set -eu
root=$PWD
patchfile=.ufo/waves/round-93/patches/M1-cluster3.patch
scratch=$(mktemp -d /tmp/c7b-r93-m1.XXXXXX)
trap 'rm -rf "$scratch"' EXIT
git archive --format=tar HEAD corpus/fixtures corpus/tools | tar -xf - -C "$scratch"
git -C "$scratch" apply --check "$root/$patchfile"
printf 'PATCH_APPLY_CHECK M1-cluster3.patch=PASS\n'
git -C "$scratch" apply "$root/$patchfile"
printf 'PATCH_APPLY M1-cluster3.patch=PASS\n'
python3 "$scratch/corpus/fixtures/check_bible.py" "$scratch/corpus/fixtures/r93-myth-cluster3"
python3 "$scratch/corpus/tools/support_check.py" "$scratch/corpus/fixtures/r93-myth-cluster3"
```

Observed relevant output:

```text
PATCH_APPLY_CHECK M1-cluster3.patch=PASS
CLEAN: schema, citations, relations, timeline; 0 violations
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 3/3; TOTAL-ROWS 13/13; DISTINCT-ANCHORS 13/13
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 3/3; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 13/13; VALIDATED-ROWS 13/13
RESULT PASS
```

Independent map-pointer coverage command (the seven entity first-appearance pointers are co-mapped with the seven entity claims, so 10 JSON rows represent 17 pointer fields):

```sh
python3 - "$scratch" <<'PY'
import json, re, sys
from pathlib import Path
cluster = Path(sys.argv[1]) / 'corpus/fixtures/r93-myth-cluster3'
entities = json.loads((cluster/'entities.json').read_text())
relations = json.loads((cluster/'relations.json').read_text())
timeline = json.loads((cluster/'timeline.json').read_text())
expected = {f'entities[{i}].first_appearance' for i in range(len(entities))}
expected |= {f'entities[{i}].claims[{j}]' for i, row in enumerate(entities) for j in range(len(row.get('claims', [])))}
expected |= {f'relations[{i}]' for i in range(len(relations))}
expected |= {f'timeline[{i}]' for i in range(len(timeline))}
text = (cluster/'claim-excerpt-map.md').read_text()
section = text.split('## JSON facts', 1)[1].split('## Editorial rows', 1)[0]
rows = [line for line in section.splitlines() if line.startswith('| ') and not line.startswith('|---')]
pointers = []
for line in rows[1:]:
    cells = [cell.strip() for cell in line.strip('|').split('|')]
    pointers.extend(re.findall(r'entities\[\d+\]\.(?:first_appearance|claims\[\d+\])|relations\[\d+\]|timeline\[\d+\]', cells[1]))
actual = set(pointers)
print(f'JSON_MAP_ROWS={len(rows)-1}; expected_pointer_fields={len(expected)} mapped_pointer_fields={len(actual)} exact={actual == expected} duplicate_pointers={len(pointers)-len(actual)}')
PY
```

Observed: `JSON_MAP_ROWS=10; expected_pointer_fields=17 mapped_pointer_fields=17 exact=True duplicate_pointers=0`.

**M3 / Roman Ovid candidate.** Exact scratch application/check sequence:

```sh
set -eu
root=$PWD
patchfile=.ufo/waves/round-93/patches/M3-ovid-cluster.patch
scratch=$(mktemp -d /tmp/c7b-r93.XXXXXX)
trap 'rm -rf "$scratch"' EXIT
git archive --format=tar HEAD corpus/fixtures/check_bible.py corpus/tools/support_check.py corpus/knowledge/reference-ledger.md | tar -xf - -C "$scratch"
git -C "$scratch" apply --check "$root/$patchfile"
git -C "$scratch" apply "$root/$patchfile"
python3 "$scratch/corpus/fixtures/check_bible.py" "$scratch/corpus/fixtures/r93-m3-ovid-cluster"
python3 "$scratch/corpus/tools/support_check.py" "$scratch/corpus/fixtures/r93-m3-ovid-cluster"
```

Observed relevant output:

```text
PATCH_APPLY_CHECK M3-ovid-cluster.patch=PASS
PATCH_APPLY M3-ovid-cluster.patch=PASS
CLEAN: schema, citations, relations, timeline; 0 violations
INVENTORY JSON-FACTS 13/13; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 10/10
SOURCE-SUPPORT 13/13; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 2 entries (2/2 anchors); MODES 15/15; VALIDATED-ROWS 15/15
RESULT PASS
```

**M3 pointer coverage.** Exact command in the M3 scratch tree:

```sh
python3 - "$scratch/m3" <<'PY'
import json, re, sys
from pathlib import Path
cluster = Path(sys.argv[1]) / 'corpus/fixtures/r93-m3-ovid-cluster'
entities = json.loads((cluster/'entities.json').read_text())
relations = json.loads((cluster/'relations.json').read_text())
timeline = json.loads((cluster/'timeline.json').read_text())
expected = {f'entities[{i}].first_appearance' for i in range(len(entities))}
expected |= {f'entities[{i}].claims[{j}]' for i, row in enumerate(entities) for j in range(len(row.get('claims', [])))}
expected |= {f'relations[{i}]' for i in range(len(relations))}
expected |= {f'timeline[{i}]' for i in range(len(timeline))}
text = (cluster/'claim-excerpt-map.md').read_text()
section = text.split('## JSON facts', 1)[1].split('## Editorial rows', 1)[0]
rows = [line for line in section.splitlines() if line.startswith('| ') and not line.startswith('|---')]
pointers = []
for line in rows[1:]:
    cells = [cell.strip() for cell in line.strip('|').split('|')]
    pointers.extend(re.findall(r'entities\[\d+\]\.(?:first_appearance|claims\[\d+\])|relations\[\d+\]|timeline\[\d+\]', cells[1]))
actual = set(pointers)
print(f'JSON_MAP_ROWS={len(rows)-1}; expected_pointer_fields={len(expected)} mapped_pointer_fields={len(actual)} exact={actual == expected} duplicate_pointers={len(pointers)-len(actual)}')
PY
```

Observed: `JSON_MAP_ROWS=13; expected_pointer_fields=13 mapped_pointer_fields=13 exact=True duplicate_pointers=0`. 

**M1 normalized referent-key comparison.** Exact command after scratch-applying M1:

```sh
python3 - "$scratch" <<'PY'
import json, unicodedata, sys
from pathlib import Path
base = Path(sys.argv[1]) / 'corpus/fixtures'
def key(value):
    value = unicodedata.normalize('NFKD', value).casefold()
    return ''.join(ch for ch in value if not unicodedata.combining(ch) and ch.isalnum())
def collect(cluster):
    load = lambda name: json.loads((cluster/name).read_text(encoding='utf-8'))
    entities, sources, timeline, relations = (load(x) for x in ('entities.json','sources.json','timeline.json','relations.json'))
    ids = {key(r['id']) for r in entities}; names = {key(r['name']) for r in entities}
    aliases = {key(a) for r in entities for a in r.get('aliases',[])}
    return {'ids':ids,'names':names,'aliases':aliases,'all':ids|names|aliases,
            'sources':{key(r['id']) for r in sources},'events':{key(r['id']) for r in timeline},
            'places':{key(r['place_id']) for r in timeline},
            'relations':{tuple(key(v) for v in (r['from'],r['type'],r['to'])) for r in relations}}
new = collect(base/'r93-myth-cluster3')
for name in ('r87-myth-cluster','r88-m3-maya-cluster'):
    old = collect(base/name)
    print(f'{name}: entity_ids={sorted(new["ids"] & old["ids"])}; display_names={sorted(new["names"] & old["names"])}; aliases={sorted(new["aliases"] & old["aliases"])}; all_entity_keys={sorted(new["all"] & old["all"])}; source_ids={sorted(new["sources"] & old["sources"])}; event_ids={sorted(new["events"] & old["events"])}; place_ids={sorted(new["places"] & old["places"])}; relation_tuples={sorted(new["relations"] & old["relations"])}')
PY
```

Observed:

```text
r87-myth-cluster: entity_ids=[]; display_names=[]; aliases=[]; all_entity_keys=[]; source_ids=[]; event_ids=[]; place_ids=[]; relation_tuples=[]
r88-m3-maya-cluster: entity_ids=[]; display_names=[]; aliases=[]; all_entity_keys=[]; source_ids=[]; event_ids=[]; place_ids=[]; relation_tuples=[]
```

This is a normalized key scan, not the independent semantic sign-off assigned to M6. M1's README records the sole lexical lookalike: external-only “Reed-Plains” versus r87's in-world “Reed Bell” / “Reedwardens,” explicitly dismissed as non-identity. S2 recommends the M1 family, but the M6 receipt was not present at deadline.

**M3 timeline whole-claim venue check.** Exact command on M3's scratch-applied candidate:

```sh
python3 - "$scratch" <<'PY'
import json, sys
from pathlib import Path
p = Path(sys.argv[1]) / 'corpus/fixtures/r93-m3-ovid-cluster'
events = json.loads((p/'timeline.json').read_text())
entities = {x['id']:x['name'] for x in json.loads((p/'entities.json').read_text())}
lines = (p/'fictional-excerpts.md').read_text().splitlines()
rows = [line for line in (p/'claim-excerpt-map.md').read_text().splitlines() if line.startswith('| T')]
for row_id, excerpt_line, index in (('T1',12,0),('T2',17,1)):
    row = next(row for row in rows if row.startswith(f'| {row_id} |'))
    pointer = row.split('|')[2].strip(); event = events[index]
    place = entities[event['place_id']]; text = lines[excerpt_line-1]
    print(f"{row_id}={event['id']} pointer={pointer}; place_id={event['place_id']} ({place}); cited_line_{excerpt_line}_names_place={'yes' if place in text else 'no'}; file_header_names_place={'yes' if place in lines[0] else 'no'}")
PY
```

Observed:

```text
T1=meal-chit-offered pointer=`timeline[0].description`, `.source_id`; place_id=moth-slate-office (Moth-Slate Office); cited_line_12_names_place=no; file_header_names_place=yes
T2=shift-four-closed pointer=`timeline[1].description`, `.source_id`; place_id=moth-slate-office (Moth-Slate Office); cited_line_17_names_place=no; file_header_names_place=yes
```

The file header identifies the record set but neither mapped event line says that event occurred at the office; this is an unresolved whole-claim support gap in M3, notwithstanding its lexical `RESULT PASS`.

## Findings & named debt

- **M1 is the strongest available C2 candidate, not a landed result.** Its Japanese *Kojiki* family is distinct from the landed Sumerian/ETCSL and Maya/Spence families. The map covers all 17 source-attributed pointer fields (first appearances plus claims, relation, and timeline) in 10 JSON rows, with three separate translation-clause editorial rows. All 13 mapped rows have declared, honest R9 modes and in-span anchors. The excerpt's `translation` rows are editorial only; the fictional JSON claims cite the authored `archive-slip` in `verbatim` mode, so no translation-backed R5 support or manual R9 PASS is asserted.
- M1's inspiration note keeps attribution/version, rights, and AI-training permission separate. It leaves the exact printing/source-version open, rights not assessed/no grant asserted, and training permission not assessed/no permission inferred. I found no positive rights or permission claim. See `.ufo/waves/round-93/patches/M1-cluster3.patch` (note and map additions around lines 207–300).
- **Zero shared referents is not independently certified.** M1's normalized identifier/name/alias/source/event/place/relation-key scan is empty, and its README disambiguates “Reed-Plains” from r87's Reed referents. But M6's independent semantic/alias review is missing; do not report the wave claim's zero-referent gate as closed. M5 convergence and M4's receipt are also missing, and the candidate remains only a patch.
- M1's bounded reading is explicit, but a separate R8 materiality statement—how consulting the passage changed the design, whether a source-specific sequence is dependency, and what remains if removed—remains integration debt, also named by S2 (`.ufo/waves/round-93/S2.md:15`). The exact translation printing/source-version remains open; no rights or training clearance follows from the delivered translation or its mode.
- M3/Ovid is a distinct, valid alternative with a passing support receipt. Its two `summary` rows are honestly marked retelling-only (not support for Ovid's undelivered wording). The manual audit found its T1/T2 mapped action lines do not state the `place_id` venue; M3 therefore is not a whole-claim-clean fallback until the venue evidence/map is repaired or those event fields change.
- The receipt outputs are scratch-candidate measurements, not evidence that any patch landed in the corpus. The post-deadline `corpus/fixtures/r93*/*` glob returned no matches.

## Handoff

- Deliverable: `.ufo/waves/round-93/C7b.md` only. No tracked file was edited; no other seat artifact was changed; no commit or push was made. Candidate composition directories were temporary and removed by exit traps.
- Patch hashes at handoff: M1 `fd0a57ec448a07c65e64a4c85a5bbc728ab7c70933dbb6ba5a012698c0e4325d`; M3 `e47a0104373a8b2b7e2a0577f48ea97a1120b2889d0b6654c1baa0f946938c5a`.
- Baseline/after tracked-state command: `git status --short --branch && git diff --quiet HEAD --; printf 'TRACKED_WORKTREE_DIFF_EXIT=%s\n' "$?"; git diff --cached --quiet; printf 'INDEX_DIFF_EXIT=%s\n' "$?"`. Observed before this report: `## main...origin/main [ahead 15]`, `?? .ufo/waves/round-93/`, `TRACKED_WORKTREE_DIFF_EXIT=0`, `INDEX_DIFF_EXIT=0`. No broad project suite was run; the two candidate patches were checked with `check_bible.py` and `support_check.py` in `/tmp` only.
