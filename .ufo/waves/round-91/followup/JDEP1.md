# JDEP1 — edge-decision verification (R8 failed-gate, R9 reprint boundary, R10 namespace)

## Work performed

Axes: (1) replay fidelity — every example/verification command the three r91 edge
decisions cite reproduces on the delivered tree; (2) governance completeness —
owner/trigger/worked-example presence against `wave-spec.md:35-42`; (3)
retroactivity — the three named unaffected records hold, the prospective boundary
intact, no silent corpus retro-edit by C3.

Read on c2ab3d0: the delivered `corpus/knowledge/r88-sourced-inspiration-decision-table.md`
(R8-r91 block at lines 40-47, R9 appendix at 49-90 with Owner at 51, Trigger at 55,
Decision at 59, Worked example at 78, Verification command at 87; R10-r91 block at
105-108), the three seat reports D1.md/D2.md/R1.md, `.ufo/waves/round-91/wave-spec.md`
(C3 requirement, lines 35-42), `patches/D1-edges.patch` + `patches/D2-edges.patch`, and
the persisted r90 JDEP2 probes (`/tmp/lore-r90-JDEP2.j3q8l6/`). Replayed every command
those artifacts cite (10 command groups; below), checked owner/trigger/worked-example
presence by exact-string extraction, and audited retroactivity against the three
records the provenance line names. Wrote only this report and `JDEP1-replay.json`;
no tracked edits, no scratch files, no commit or push.

Dependency state: HEAD was already `c2ab3d0` with a clean tracked tree at the first
check; the two 60s wait-checks ran to completion (see below) and no dependency
artifact was missing. The work commit `6332115` + the R8/R10 follow-up commit
`c2ab3d0` are both present.

## Before → after measurements

### Baseline identity and the two 60s dependency checks

```sh
git rev-parse HEAD && git status --porcelain=v1 --untracked-files=no | wc -l
```

```text
c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7
0
```

Two 60s checks (one Bash call, background): `check-01 head=c2ab3d0 clean=0` at
08:33:29-03:00 and `check-02 head=c2ab3d0 clean=1` at 08:34:29-03:00 (the `clean`
count includes untracked files: between the checks the follow-up siblings H4-*.json
and JCAL5-delta.json appeared under `.ufo/waves/round-91/followup/`). The background
wrapper reported exit 1 only because the loop's final arithmetic test returned
non-zero; both check lines printed, and the tracked tree stayed clean
(`--untracked-files=no` → 0).

### What the three delivered edge decisions cite

A decision-text extraction of the delivered table shows the r91 blocks contain these
explicit element labels:

```sh
python3 - <<'PY'
from pathlib import Path
text=Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md').read_text()
b=text.split('**Failed-gate disposition (decided r91):**',1)[1].split('\n### R9 appendix',1)[0]
r=text.split('### R9 appendix',1)[1].split('### R10 appendix',1)[0]
t=text.split('**Namespace scoping (decided r91):**',1)[1]
for name,blk in (('R8-r91',b),('R9',r),('R10-r91',t)):
    print(name,len(blk),[(k,k in blk) for k in ('**Owner:**','**Trigger:**','**Worked example:**','**Verification command')])
PY
```

```text
R8-r91 700 [('**Owner:**', False), ('**Trigger:**', False), ('**Worked example:**', False), ('**Verification command', False)]
R9 3558 [('**Owner:**', True), ('**Trigger:**', True), ('**Worked example:**', True), ('**Verification command', True)]
R10-r91 1798 [('**Owner:**', False), ('**Trigger:**', False), ('**Worked example:**', False), ('**Verification command', False)]
```

Consequence for replay scope: the delivered R9 appendix cites exactly one runnable
command (the patch-text completeness check over `patches/D2-edges.patch`); the
delivered R8-r91 and R10-r91 blocks cite no command at all. The remaining commands
replayed below are cited by the D1/D2/R1 seat reports that produced these decisions
(all committed at c2ab3d0).

### Replay 1 — delivered R9 verification command (cited in the table, lines 87-90)

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-91/patches/D2-edges.patch").read_text(); keys=("**Owner:**","**Trigger:**","later reprint can qualify","item-specific record","source work","verify the passage against that exact copy","identified reprint","earlier printing","**Worked example:**","Source text/version: unidentified; unverified","**Verification command"); missing=[k for k in keys if k not in s]; print(f"R9 reprint decision completeness: {len(keys)-len(missing)}/{len(keys)}"); raise SystemExit(bool(missing))'
```

```text
R9 reprint decision completeness: 11/11
rc=0
```

### Replay 2 — D1/R1 patch-text completeness commands (D1-edges.patch)

R8 (cited in D1.md, re-run in R1.md):

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-91/patches/D1-edges.patch").read_text(); a=s.split("**R8 — failed R2 gate",1)[1].split("**R9 — later-reprint boundary",1)[0]; keys=("**Owner:**","**Trigger:**","**Worked example:**","two-part R2 gate","does not prove source use","affected detail","whole element","l0-questions.md","remove the provisional note"); missing=[k for k in keys if k not in a]; print(f"R8 text completeness: {len(keys)-len(missing)}/{len(keys)}"); raise SystemExit(bool(missing))'
```

```text
R8 text completeness: 9/9
rc=0
```

R9 (D1 variant) and R10 (R1-cited variant):

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-91/patches/D1-edges.patch").read_text(); a=s.split("**R9 — later-reprint boundary",1)[1].split("**R10 — cluster-local source_id",1)[0]; keys=("**Owner:**","**Trigger:**","**Worked example:**","item-specific record","stable identifier or copy locator","ties the cited passage","that exact copy","identified reprint","earlier printing","edition-specific variant","Source text/version: unidentified; unverified"); missing=[k for k in keys if k not in a]; print(f"R9 text completeness: {len(keys)-len(missing)}/{len(keys)}"); raise SystemExit(bool(missing))'
python3 - <<'PY'
from pathlib import Path
s=Path('.ufo/waves/round-91/patches/D1-edges.patch').read_text()
a=s.split('**R10 — cluster-local `source_id` namespace',1)[1].split('+ ## Integration boundary',1)[0]
keys=('**Owner:**','**Trigger:**','**Worked example:**',"Each cluster's `sources.json`",'cluster-relative path, source_id','namespace collision','incoming cluster README','live register','Verification command')
missing=[key for key in keys if key not in a]
print(f'R10 text completeness: {len(keys)-len(missing)}/{len(keys)}')
raise SystemExit(bool(missing))
PY
```

```text
R9 text completeness: 11/11
rc=0
R10 text completeness: 9/9
rc=0
```

All three patch-text receipts reproduce exactly; note they read the unapplied D1
patch, not the delivered prose (see merge-fidelity below).

### Replay 3 — r90 JDEP2 probe replays cited by D1.md/D2.md/R1.md

R8 probe:

```sh
python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r8-denial; rc=$?; printf 'exit=%s\n' "$rc"
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

R9 probe (checker then support command):

```sh
python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r9-reprint; rc=$?; printf 'checker_exit=%s\n' "$rc"; python3 corpus/tools/support_check.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r9-reprint; rc=$?; printf 'support_exit=%s\n' "$rc"
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
checker_exit=0
FAIL: fact table must be under a JSON facts or Editorial rows heading
support_exit=2
```

The checker exit matches the recorded receipt; the support-command exit does NOT
(recorded in D1.md/D2.md/R1.md: `PASS T1: ... / SOURCE-SUPPORT 1/1; RETELLING-SUPPORT-ONLY
0 entries (0/0 anchors); MODES 1/1 / RESULT PASS` and `support_exit=0`). Control run
with the pre-hardening tool (`git show a7c6a17:corpus/tools/support_check.py`,
delivered through process substitution so no scratch file is created):

```sh
python3 <(git show a7c6a17:corpus/tools/support_check.py) /tmp/lore-r90-JDEP2.j3q8l6/probes-r9-reprint; echo "old_support_exit=$?"
```

```text
PASS T1: source-support; mode=translation; anchor=found; 8:The keeper set the ring upon the fourth stair in slow measure.
SOURCE-SUPPORT 1/1; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 1/1
RESULT PASS
old_support_exit=0
```

So the recorded receipt was correct for the phase-1 tool; the divergence is caused by
the C2 support-command hardening landed in `6332115` (`corpus/tools/support_check.py`
+104/−21 between a7c6a17 and c2ab3d0), whose parse now requires an expected-inventory
declaration and a `JSON facts`/`Editorial rows` section heading
(`corpus/tools/support_check.py:114,129-132`), which the r90 probe lacks. The tool
itself is healthy: it PASSes the delivered fixtures (r87 `INVENTORY JSON-FACTS 14/14;
EDITORIAL-ROWS 8/8`, `RESULT PASS`; r88-m3 `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS
0/0`, `RESULT PASS WITH WARNINGS` — the expected unreferenced-declaration WARN).

R10 probes:

```sh
python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-a; rc=$?; printf 'A_exit=%s\n' "$rc"; python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-b; rc=$?; printf 'B_exit=%s\n' "$rc"; python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-a /tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-b; rc=$?; printf 'two_dir_exit=%s\n' "$rc"
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
A_exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
B_exit=0
usage: check_bible.py [-h] bible
check_bible.py: error: unrecognized arguments: /tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-b
two_dir_exit=2
```

R10 comparison receipt (D1.md/R1.md form):

```sh
CLUSTER_A=/tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-a; CLUSTER_B=/tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-b; python3 corpus/fixtures/check_bible.py "$CLUSTER_A" && python3 corpus/fixtures/check_bible.py "$CLUSTER_B" && python3 -c 'import json,sys;from pathlib import Path;a,b=[Path(p) for p in sys.argv[1:3]];A={r["id"]:r for r in json.loads((a/"sources.json").read_text())};B={r["id"]:r for r in json.loads((b/"sources.json").read_text())};shared=sorted(A.keys()&B.keys());print("shared source_id strings:",shared);[print(k,"A=",A[k],"B=",B[k],"equal=",A[k]==B[k]) for k in shared]' "$CLUSTER_A" "$CLUSTER_B"; echo "rc=$?"
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
CLEAN: schema, citations, relations, timeline; 0 violations
shared source_id strings: ['registrar-copy', 'salt-chronicle']
registrar-copy A= {'id': 'registrar-copy', 'title': 'Sella’s Harbor Register carbon, year 12', ...} B= {...} equal= True
salt-chronicle A= {'id': 'salt-chronicle', 'title': 'Salt Chronicle, year 12 — municipal registry copy', ...} B= {'id': 'salt-chronicle', 'title': "Salt Chronicle, year 12 — courier's route log", ...} equal= False
rc=0
```

Matches the recorded receipt verbatim (identical and non-identical repeated IDs).

### Replay 4 — D2.md baseline completeness (recorded pre-landing, replayed post-landing)

```sh
python3 - <<'PY'
from pathlib import Path
text=Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md').read_text()
r9=text.split('\n### R9 appendix',1)[1].split('\n### R10 appendix',1)[0]
checks={
    'r9_reprint_boundary':'reprint' in r9.lower(),
    'r9_reliability_criteria':'item-specific' in r9.lower() or 'authoritative' in r9.lower(),
    'r9_owner_trigger_example':'**Trigger:**' in r9 and '**Worked example:**' in r9,
    'r9_verification_command':'**Verification command' in r9,
}
for key,value in checks.items():
    print(f'{key}={value}')
PY
```

```text
r9_reprint_boundary=True
r9_reliability_criteria=True
r9_owner_trigger_example=True
r9_verification_command=True
```

D2.md recorded all four `False` at a7c6a17; the delivered tree flips all four `True`
as expected for the landed clarification.

### Replay 5 — R1 prospective-boundary and duplicate-ID checks

Prospective boundary (R1.md form): `r8_r10_prospective=True`, `r9_starts_at_r89=True`,
`r87_external_only_marker=True`, `m3_spence_text_delivered=True`,
`r10_demo_explicitly_hypothetical=True`, `live_register_present=False` — all six match
R1's recorded values.

Duplicate decision-ID check (R1.md form) on the delivered table:

```text
R8: baseline_table_rows=1 baseline_appendix_headings=1 D1_added_clarification_rows=1
R9: baseline_table_rows=1 baseline_appendix_headings=1 D1_added_clarification_rows=1
R10: baseline_table_rows=1 baseline_appendix_headings=1 D1_added_clarification_rows=1
D1_additive_table_repeats_decision_ids=True
D2_replaces_existing_R9_heading=True
```

R1's integration end-state holds: one table row and one appendix heading per ID, no
duplicate clarification table was landed.

### Owner / trigger / worked example against the spec

`wave-spec.md:35-42` requires each of the three r91 edge clarifications to land "with
owner, trigger, and worked example". Delivered state:

- R9: complete — Owner (line 51), Trigger (55), Decision (59), Worked example (78),
  Verification command (87-90).
- R8-r91 (lines 40-47): no Owner/Trigger/Worked example/Verification labels; the
  Owner exists only at r90 appendix level (line 38, "the lore lane"), and the
  failed-gate condition is inline prose only.
- R10-r91 (lines 105-108): no Owner/Trigger/Worked example/Verification labels; Owner
  only at r90 appendix level (line 102); the trigger condition is inline ("a bare
  shared id triggers the namespace check").

Merge-fidelity key count (the D1 patch's own completeness keys against the delivered
r91 blocks):

```text
R8 delivered-block key hits: ['two-part R2 gate'] missing: ['**Owner:**','**Trigger:**','**Worked example:**','does not prove source use','affected detail','whole element','l0-questions.md','remove the provisional note']
R10 delivered-block key hits: ['cluster-relative path, source_id'] missing: ['**Owner:**','**Trigger:**','**Worked example:**',"Each cluster's `sources.json`",'namespace collision','incoming cluster README','live register','Verification command']
R8 appendix-level has Owner: True | Trigger label: False | Worked example label: False
R10 appendix-level has Owner: True | Trigger label: False | Worked example label: False
```

The D1 patch carries the spec elements unapplied; the landed prose merge dropped them
(R1 had recommended transplanting into the existing appendices, and no rule content
itself is missing — the traceability labels and worked examples are).

### Retroactivity

- r87 ETCSL marker: `corpus/fixtures/r87-myth-cluster/inspiration-note.md:21` —
  "Element marker (R8, r89): the ETCSL parallel is recorded as `external-only /
  unverified inspiration`" with locators verified, text undelivered, and all canon
  claims independently supported. R8's r91 failed-gate rule addresses the R2 gate
  (no-source account), not this recorded external-only marker; disposition unchanged.
- r88-m3 Spence passage: `corpus/fixtures/r88-m3-maya-cluster/source-excerpt.md`
  exists and delivers the Spence English prose (1913, printed p. 209, Gutenberg
  53080); the map declares `verbatim` for it and scopes `external-only` to the
  underlying K'iche text (`claim-excerpt-map.md:14-15,44`). No translator/reprint tie
  exists, so R9's r91 reprint boundary has no retroactive effect.
- r87 Hara/Sen record: `corpus/fixtures/r87-myth-cluster/contradictions.json:12`
  still reports the Hara gate-witness vs Sen dune-register disagreement as
  unresolved, with both source IDs resolving inside the same fixture (intra-cluster);
  R10's r91 namespace rule is cross-cluster, so the record is unchanged.
- Prospective boundary and register: `R8–R10 are prospective.` and `clusters landed
  from r89 onward` both present; `corpus/knowledge/cross-cluster-contradictions.md`
  still absent (the register awaits a genuine conflict).
- Checker untouched: `sha256sum corpus/fixtures/check_bible.py` =
  `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (the pinned
  ff9fd2aa), and `git diff --stat a7c6a17..c2ab3d0 -- corpus/fixtures/check_bible.py
  corpus/tools/support_check.py` shows only `support_check.py` (C2) changed.
- Corpus-change audit: in `6332115` the only r87/r88 corpus touches are the two
  C2/M3 claim-excerpt-map wording edits (inventory headings, JSON-facts/editorial
  split); the diffs preserve the ETCSL `external-only / unverified inspiration`
  line and the m3 Spence `verbatim` declaration. C3's own corpus edits in the two
  commits are the decision table (both commits) and the r89 paraphrase demo's
  Inventory line (c2ab3d0). No r87/r88 record was retro-edited on a C3 rule.

## Findings & named debt

1. **Replay fidelity — reproduces, with one attributed divergence.** Every command
   cited by the three edge decisions' artifacts replays with the recorded output
   except the r9 support-command receipt: D1/D2/R1 recorded `RESULT PASS` /
   `support_exit=0`; on c2ab3d0 the same command returns
   `FAIL: fact table must be under a JSON facts or Editorial rows heading` /
   `support_exit=2`. The pre-hardening control reproduces the recorded output, so
   this is the landed C2 hardening (documented contract change), not a fabrication or
   a broken tool. The r90 probe predates the hardened contract and must be re-pointed
   (expected-inventory declaration + section heading) before the R9 receipt-parity
   question can be re-tested on the delivered tool.
2. **Owner/trigger/worked example — incomplete for R8/R10.** R9 landed complete; the
   R8-r91 and R10-r91 blocks landed without the spec-required Owner/Trigger/Worked
   example/Verification labels (`wave-spec.md:41-42`), and without any replayable
   example command (the D1 patch holds them, unapplied by design). Rule content is
   present; the traceability element is not.
3. **Retroactivity holds.** All three named records are unchanged and undisturbed
   (evidence above); the prospective boundary and absent register are intact; the
   checker hash is unchanged; C3 made no retroactive corpus edit.
4. **Verdict recommendation (for the judging seat, no scalar).** On decided-rule
   content and replay fidelity, C3 depth is improved: all three r91 clarifications
   landed, every patch-text and probe replay reproduces (with the one attributed
   support-command divergence), and retroactivity holds. But the round's own spec
   requires owner, trigger, and worked example per decision, and R8/R10 did not land
   them — so per the "a trade anywhere is NOT an improvement" rule, C3 should not be
   ruled an unqualified improvement: recommend **improved (bounded)** for C3 depth
   with the two named debts below, and if the judge counts the spec's per-decision
   element set inside the claim, the R8/R10 traceability element is unmet.
5. **Named debt (r92 candidates):**
   - Transplant the R8/R10 Owner/Trigger/Worked-example (and, if kept, the D1
     verification commands) into their appendix blocks — the D1 patch text at
     `.ufo/waves/round-91/patches/D1-edges.patch` already holds all three elements;
     no new drafting needed.
   - Re-point the R9 receipt-parity probe at the hardened support command contract
     and re-test whether an unidentified-version translation still passes
     `SOURCE-SUPPORT`; the debt as written in D1/D2/R1 ("still counts ... RESULT
     PASS") no longer describes the delivered tree.
6. Limits: textual/replay-level verification only; I did not adjudicate translation
   fidelity, bibliographic quality, or rights. The CB1 boundary-doc reconstruction
   and the C1/C2 claims (fixtures, census, hardening deviations) are other seats'
   scope and were not re-verified here.

## Handoff

- `.ufo/waves/round-91/followup/JDEP1.md` — this report with all receipts.
- `.ufo/waves/round-91/followup/JDEP1-replay.json` — the same measurements in compact
  machine-readable form (head, tracked-clean, per-command recorded-vs-replayed,
  owner/trigger matrix, retroactivity booleans, verdict recommendation, debts).
- Open items for the judging/integration seat: the R8/R10 traceability transplant;
  the R9 probe re-pointing before receipt parity is re-tested. No tracked file, other
  seat's artifact, or sibling repo was modified; no commit or push.