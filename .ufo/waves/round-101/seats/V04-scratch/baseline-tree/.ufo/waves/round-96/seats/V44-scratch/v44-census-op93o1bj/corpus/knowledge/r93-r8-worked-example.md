# R8 worked-example dossier: seven threshold names

## Scope and limits

This is a replayable model record for the R8 scenario stated in the round-92 E1 wording patch (`.ufo/waves/round-92/patches/E1-edges.md:13`). It is not an observed submission, a finding that anyone consulted or copied a source, a rights assessment, or a canon assertion. The *Kesh Hymn* passage is not reproduced or independently authenticated here; the dossier records only the scenario's stated sequence match.

## Case

A proposed lore element consists entirely of the same seven threshold names in the same order as *Kesh Hymn* lines 12–19. In the scenario, the creator denies using a source. The reviewer records the contrary sequence evidence. Removing the sequence leaves no independently authored, independently supportable remainder.

## Illustrative R8 review record

| Field | Recorded value |
|---|---|
| Element and scope pointer | The entire proposed element in the seven-threshold-names scenario; no live corpus element ID is supplied. |
| Creator account | The hypothetical creator denies using a source. This is an account, not an adjudication. |
| Reviewer / record date | D2, world-bible dossier author, acting as the named example reviewer; 2026-10-17, the dossier date. Example-only: this does not claim that a live integration review or source inspection occurred. A real case must identify its actual named reviewer and date. |
| Gate result | R2 unavailable. The no-source-account limb is recorded, but the other limb fails: the sequence finding is contrary source-specific evidence, not only a commonplace motif. The failed gate does not establish R1 or prove source use. |
| Contrary evidence | The example reviewer records the same seven threshold names in the same order as *Kesh Hymn* lines 12–19. This is treated as contrary source-specific sequence evidence for the editorial screen; it is not evidence that the creator consulted the work. |
| Separability rationale | The proposed element consists entirely of that sequence; removing it leaves no independently authored, independently supportable remainder. The source-dependent detail is therefore inseparable from the element in this case. |
| Scope / disposition | Withhold the whole element from supported canon. Do not retain it as newly authored fiction by attaching an uncertainty notice. Preserve the neutral note and evidence in the inspiration note/map. This is an editorial support boundary, not a finding about source use, rights, or permission. |
| Next action | Keep a dated `possible influence: unverified` note and mark R2 unavailable. If influence or separability remains disputed, record the unresolved question and missing evidence in `l0-questions.md`. Re-derive without the dependency, or deliver permitted source text and obtain a separately reviewed R1 decision establishing a claim-specific basis. Do not use `external-only / unverified inspiration` on this failed-gate evidence alone. Remove the provisional note only after a later review records both R2 conditions passing or a confirmed R1 source-use decision. |

The whole-element disposition is specific to the inseparable/no-supportable-remainder branch. If the dependent detail is separable and a remainder is independently supportable, the decision table's smaller-detail withholding rule remains in force.

## Record-to-decision crosswalk

| Record field | Decision text to replay |
|---|---|
| Gate result | `corpus/knowledge/r88-sourced-inspiration-decision-table.md`, R8 appendix: R2 requires the creator's no-source account and no contrary source-specific evidence with only a commonplace motif; the clarified failed-gate paragraph marks R2 unavailable when a condition fails or remains unresolved. |
| Contrary evidence | Round-92 E1's copy-ready worked example names the same seven threshold names in the same order as *Kesh Hymn* lines 12–19; the delivered failed-gate paragraph requires the named reviewer to record contrary source-specific evidence. |
| Separability rationale | E1 states that no independently authored, supportable remainder survives removing the sequence; the decision's trigger is the inability to separate the dependency while leaving such a remainder. |
| Scope / disposition | The failed-gate paragraph says to withhold the whole element from supported canon in this branch; E1's example says to hold the whole element out of supported canon. |
| Next action | The decision requires the neutral note, R2-unavailable status, note/map fields, and `l0-questions.md` route for unresolved disputes; it permits re-derivation or a permitted-text, separately reviewed R1 basis and restricts note removal to a later cleared R2 or confirmed R1 decision. |

## Replay instructions

From the repository root, after applying this dossier patch, run the check below. It compares each of the five record fields to the R8 decision and the copy-ready round-92 example; it is a textual traceability check, not a source-use or rights determination.

```sh
D2_DOSSIER=corpus/knowledge/r93-r8-worked-example.md python3 - <<'PY'
import os
from pathlib import Path

table = Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md').read_text()
r8 = table.split('### R8 appendix', 1)[1].split('### R9 appendix', 1)[0]
e1 = Path('.ufo/waves/round-92/patches/E1-edges.md').read_text()
dossier = Path(os.environ['D2_DOSSIER']).read_text()
checks = {
    'gate_result': ('**Gate result**' in dossier and 'R2 unavailable' in dossier and 'requires BOTH' in r8 and 'mark R2 unavailable' in r8),
    'contrary_evidence': ('**Contrary evidence**' in dossier and 'contrary source-specific evidence' in r8 and 'same seven threshold names in the same order as *Kesh Hymn* lines 12–19' in e1),
    'separability_rationale': ('**Separability rationale**' in dossier and 'cannot separate the source-dependent detail' in r8 and 'no independently authored, supportable remainder survives removing that sequence' in e1),
    'scope': ('**Scope / disposition**' in dossier and 'withhold the **whole element from supported canon**' in r8 and 'Hold the whole element out of supported canon' in e1),
    'next_action': ('**Next action**' in dossier and 'l0-questions.md' in r8 and 're-derived without the source-dependent material' in r8),
}
for field, passed in checks.items():
    print(f'{field}: {"PASS" if passed else "FAIL"}')
print(f'R8 record fields: {sum(checks.values())}/{len(checks)}')
if not all(checks.values()):
    raise SystemExit(1)
PY
```

Expected output:

```text
gate_result: PASS
contrary_evidence: PASS
separability_rationale: PASS
scope: PASS
next_action: PASS
R8 record fields: 5/5
```

## r93 correction — R8 record and replay (2026-10-17)

This dated correction supersedes the replay instructions above. The earlier substring checks did not parse the recorded table cells: a blank cell could pass because the labels and required phrases appeared elsewhere in this dossier, including inside the checker itself. The old text remains as filed; use only this corrected record and replay below.

The source for this repair is the delivered `### R8 appendix` in `corpus/knowledge/r88-sourced-inspiration-decision-table.md`, not the round-92 wave patch. This remains a hypothetical editorial example: no source-use, rights, or canon finding is made, and no live integration review or source inspection is claimed.

### Corrected illustrative R8 review record

| Field | Recorded value |
|---|---|
| Element and scope pointer | Hypothetical proposed element: the entire element consisting of the same seven threshold names in the same order as *Kesh Hymn* lines 12–19; no live corpus element ID is supplied. |
| Creator account | The hypothetical creator denies using a source. This is an account, not an adjudication. |
| Reviewer / record date | D2, this dossier's author, acts only as the named example reviewer; 2026-10-17. Example-only: no live integration review or source inspection occurred. |
| Gate result | R2 unavailable. The hypothetical creator's no-source account is recorded, but contrary source-specific sequence evidence defeats the gate; this does not prove source use and does not establish R1. |
| Contrary evidence | The hypothetical reviewer records the scenario-stipulated same seven threshold names in the same order as *Kesh Hymn* lines 12–19; this is contrary source-specific evidence for the editorial screen, not evidence that the creator consulted that work. |
| Separability rationale | The hypothetical element consists entirely of that sequence; removing it leaves no independently authored, independently supportable remainder. The source-dependent detail is inseparable in this case. |
| Scope / disposition | Withhold the whole element from supported canon until it is re-derived without the dependency or a permitted source text is delivered and a separately reviewed R1 decision establishes a claim-specific basis. Preserve the neutral note and evidence. This does not itself prove copying, source use, rights status, or canon. |
| Next action | Keep a dated `possible influence: unverified` note and mark R2 unavailable. If influence or separability remains disputed, record the unresolved question and missing evidence in `l0-questions.md`. Re-derive without the dependency, or deliver permitted source text and obtain a separately reviewed R1 decision with a claim-specific basis. Remove the provisional note only after a later review records both R2 conditions passing or a confirmed R1 source-use decision. |
| Owner | Normative owner: the lore integration editor records the two-part R2 gate result, affected element, and separability decision. Illustrative case owner: D2, this dossier's author, acting only as the hypothetical integration editor; no real integration owner or live review is claimed. The creator supplies the provenance account; a named reviewer assesses contrary source-specific evidence and whether an independently authored, independently supportable remainder exists. |
| Trigger | Both conjuncts are required: (1) either R2 condition fails or remains unresolved; AND (2) the reviewer cannot separate the source-dependent detail from the element while leaving an independently authored, independently supportable remainder. |
| Inspiration note target | Separate inspiration-note target: create or update the hypothetical element's dated `possible influence: unverified` note; record the gate result, affected element, contrary evidence, separability rationale, whole-element hold, and next action. Preserve the neutral note and evidence; this does not state that influence occurred. |
| Element-map target | Separate element-map target: create or update a distinct map entry for the same hypothetical element; record its affected aspect, gate result, contrary evidence, separability rationale, whole-element hold, and next action. The inspiration-note entry does not substitute for this element-map record. |

### Corrected replay

This is an **exact frozen-record replay**, not a general meaning evaluator. It checks the delivered R8 appendix and compares the parsed cells in this illustrative record against one fixed SHA-256. The expected digest was independently calculated from the 12 canonical values and is a literal below; it is never derived from the candidate being checked.

Whitespace policy: Unicode whitespace runs inside each cell collapse to one ASCII space and leading/trailing whitespace is ignored. Field order, spelling, case, punctuation, and Markdown markers remain exact. The digest payload is the UTF-8 JSON array of normalized cell values in `FIELDS` order, serialized with `ensure_ascii=False` and separators `(',', ':')`.

From the repository root, run:

```sh
D2_DOSSIER=corpus/knowledge/r93-r8-worked-example.md python3 - <<'PY'
import hashlib
import json
import os
import re
from pathlib import Path

TABLE_PATH = Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md')
DOSSIER_PATH = Path(os.environ.get('D2_DOSSIER', 'corpus/knowledge/r93-r8-worked-example.md'))
EXPECTED_RECORD_SHA256 = 'da934a7eea6d108f60c71534e8beb218a532eb55b20217a04ab86d82bc6c7e05'
FIELDS = (
    'Element and scope pointer', 'Creator account', 'Reviewer / record date',
    'Gate result', 'Contrary evidence', 'Separability rationale',
    'Scope / disposition', 'Next action', 'Owner', 'Trigger',
    'Inspiration note target', 'Element-map target',
)
FILLER = re.compile(r'\b(?:tbd|todo|placeholder|lorem ipsum|generic filler|fill in later|example goes here)\b', re.I)
EMPTY_VALUES = {'', '-', '—', 'n/a', 'na', 'none', 'unknown', 'tbd', 'todo', 'placeholder'}


def cells(line):
    if not (line.startswith('|') and line.endswith('|')):
        return []
    return [part.strip() for part in line[1:-1].split('|')]


def normalize(value):
    return re.sub(r'\s+', ' ', value).strip()


def read_record(text):
    marker = '### Corrected illustrative R8 review record'
    if marker not in text:
        return None
    tail = text.split(marker, 1)[1]
    tail = re.split(r'(?m)^#{2,6}\s+', tail, maxsplit=1)[0]
    rows = [cells(line) for line in tail.splitlines() if line.startswith('|') and line.endswith('|')]
    if not rows or rows[0] != ['Field', 'Recorded value']:
        return None
    result = {}
    for row in rows[1:]:
        if len(row) != 2:
            return None
        if re.fullmatch(r':?-{3,}:?', row[0]) and re.fullmatch(r':?-{3,}:?', row[1]):
            continue
        result[row[0]] = result.get(row[0], []) + [row[1]]
    return result


def validate(path):
    text = path.read_text()
    source = TABLE_PATH.read_text()
    if '### R8 appendix' not in source or '### R9 appendix' not in source:
        return 1, 'R8_SOURCE_MISSING', 0
    r8 = source.split('### R8 appendix', 1)[1].split('### R9 appendix', 1)[0]
    source_checks = (
        '**Owner:** the lore integration editor records the two-part R2 gate result',
        '**Trigger:** either R2 condition fails or remains unresolved, and the reviewer cannot separate',
        'in the inspiration note and element map',
        'withhold the **whole element from supported canon**',
        'same seven threshold names in the same order as *Kesh Hymn* lines 12–19',
        'creator denies using a source',
        'no independently authored, supportable remainder survives removing that sequence',
        'does not itself prove copying or source use',
    )
    if any(term not in r8 for term in source_checks):
        return 1, 'R8_SOURCE_CONTENT', 0
    if 'no source-use, rights, or canon finding is made' not in text or 'no live integration review or source inspection is claimed' not in text:
        return 1, 'R8_EXAMPLE_LIMITS', 0

    record = read_record(text)
    if record is None or any(len(record.get(field, ())) != 1 for field in FIELDS) or set(record) != set(FIELDS):
        return 1, 'R8_RECORD_FIELDS', 0
    values = {field: record[field][0] for field in FIELDS}
    for value in values.values():
        normalized = normalize(value)
        if normalized.strip('`*_ .') in EMPTY_VALUES or not normalized:
            return 1, 'R8_CELL_EMPTY', len(values)
        if FILLER.search(normalized):
            return 1, 'R8_CELL_FILLER', len(values)

    payload = json.dumps([normalize(values[field]) for field in FIELDS], ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    actual_digest = hashlib.sha256(payload).hexdigest()
    if actual_digest != EXPECTED_RECORD_SHA256:
        return 1, 'R8_RECORD_DRIFT', len(values)
    return 0, 'R8_RECORD_VALID', len(values)


code, finding, count = validate(DOSSIER_PATH)
if code:
    print('R8 replay: FAIL')
    print(f'finding: {finding}')
    raise SystemExit(code)
print('R8 replay: PASS')
print('delivered R8 appendix: VERIFIED')
print(f'record cells: {count}/{len(FIELDS)}')
print(f'canonical record SHA-256: {EXPECTED_RECORD_SHA256}')
PY
```

Expected result: the four lines above, exit 0. For scratch candidates, blank cells remain `R8_CELL_EMPTY` and generic filler remains `R8_CELL_FILLER`; any other noncanonical cell edit returns `R8_RECORD_DRIFT`, exit 1. For example, appending `Both conditions passed; R2 passes and is available.` to `Gate result` or appending `The whole element should remain in supported canon with an uncertainty notice.` to `Scope / disposition` must drift. Replacing scope with a hold inversion must also drift. A harmless whitespace-only mutation (for example, changing `R2 unavailable.` to `R2    unavailable.`) must pass under the stated normalization. Use isolated scratch copies and remove them after the run.
