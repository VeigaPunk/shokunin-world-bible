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
