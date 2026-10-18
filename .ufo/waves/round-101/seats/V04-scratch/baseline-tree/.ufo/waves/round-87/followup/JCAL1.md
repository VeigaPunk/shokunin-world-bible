# JCAL1 — Calibration judge #1 (independent re-measure)

Seat: JCAL1. Wave: round-87 follow-up (world-bible lane), fleet root `/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.
Measured tree: HEAD `2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (`2b48ca7`, work-wave evidence commit), measured at `2026-10-17T01:41:49-03:00`.
Mission: independent re-measure of the **calibration** axis (C1, per-record unassessed disclosure for ambiguous provenance holders, commit `03c6746`) and a verdict recommendation. No files under version control were written by this seat; every artifact below is a `/tmp` scratch measurement or this untracked report.

Identity of the two artifacts under test:

```
e088ac108b7f1e2dda8f1630d72cc161  corpus/fixtures/check_bible.py                      (md5, delivered tree)
3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237  (sha256, delivered checker)
e8f241623aa84eb1dce192a03c9e70b8f4ba386344f0b22a99ba1ac0d4942132  (sha256, pre-C1 checker at 28706dc)
```

The pre-C1 checker was extracted by `git -C … show 28706dc:corpus/fixtures/check_bible.py > /tmp/jcal1/check_bible.baseline.py`; its sha256 equals the checker still present in B1's baseline worktree (`/tmp/r87-B1/corpus/fixtures/check_bible.py`, worktree HEAD `28706dc`). That equality is what makes Part A's byte-identity result a statement about the C1 change rather than about baseline self-consistency.

---

## Verdict recommendation

**Calibration axis — improved.**

The delivered checker adds a per-record disclosure line to **every** provenance record at and after the first ambiguous-holder record, naming the ambiguous holder field and id and the origin record, while the item-global latch is preserved and never resumes. Measured on the delivered tree, the change is **purely additive**: across 156 replayed cases (138 fixture dirs, 13 scratch probes, 5 r85 live probes) it removed zero findings, changed zero exit codes, and added no line outside its own disclosure signature. Every previously observed output — including all 133 inherited fixture tuples — is byte-identical.

Two qualifications, both recorded below as named debt rather than regressions:
1. the *stop* is only armed from well-shaped records, so a malformed record that carries the ambiguous holder id still leaves a later break silently unassessed and undisclosed (Part C, residual probes);
2. at the stop record the legacy item-global notice and the new per-record line both fire, so that record carries two near-duplicate disclosures (Part B).

---

## Part A — full 138-dir census and the 133-tuple diff

Command: `python3 /tmp/jcal1/census.py` (from anywhere; the script pins the repo root itself).

Script as run:

```python
import hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
FIX = ROOT / 'corpus' / 'fixtures'

dirs = sorted(p for p in FIX.iterdir() if p.is_dir())
tuples = {}
stdout_records = {}
for d in dirs:
    rel = 'corpus/fixtures/' + d.name
    cmd = ['python3', 'corpus/fixtures/check_bible.py', rel]
    p = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    vc = sum(1 for ln in p.stdout.splitlines() if ln.startswith('VIOLATION:'))
    tuples[rel] = {'exit': p.returncode,
                   'stdout_sha256': hashlib.sha256(p.stdout.encode('utf-8')).hexdigest(),
                   'violation_count': vc}
    stdout_records[rel] = {'command': ' '.join(cmd), 'exit': p.returncode,
                           'stdout': p.stdout, 'stderr': p.stderr}

prior = json.loads((ROOT / '.ufo/waves/round-87/patches/B1-tuples.json').read_text())
new_keys = sorted(set(tuples) - set(prior))
missing = sorted(set(prior) - set(tuples))
changed = sorted(k for k in prior if k in tuples and prior[k] != tuples[k])
```

The replay command form and working directory are identical to B1's (`python3 corpus/fixtures/check_bible.py corpus/fixtures/<name>` with the repo root as cwd), which is required for the byte comparison to mean anything.

Observed (`.ufo/waves/round-87/followup/JCAL1-census.json`):

```json
{
  "revision": "2b48ca7",
  "dir_count": 138,
  "prior_tuple_count": 133,
  "prior_tuples_changed": [],
  "prior_tuples_missing": [],
  "new_dirs": ["corpus/fixtures/r87-chain-unique-broken", "corpus/fixtures/r87-chain-unique-valid",
               "corpus/fixtures/r87-masked-break-from-ambiguous", "corpus/fixtures/r87-masked-break-to-ambiguous",
               "corpus/fixtures/r87-myth-cluster"],
  "exit_counts": {"0": 30, "1": 108},
  "violation_total": 272,
  "prior_violation_total": 259,
  "new_violation_total": 13,
  "stderr_nonempty": [],
  "corpus_json_count": 730,
  "fixture_json_count": 685
}
```

- **133/133 prior tuples byte-identical** on all three components (`exit`, raw-stdout `stdout_sha256`, `violation_count`); 0 changed, 0 missing. Because B1's tuples were produced by the pre-C1 checker (hash above), this is a direct statement that C1 altered no inherited fixture output.
- Census arithmetic: `133 + 5 = 138` dirs; exits `28×0 + 105×1 = 133` inherited, `30×0 + 108×1 = 138` delivered; `259 + 13 = 272` violations; the whole 13-violation delta belongs to the 5 new dirs (`1 + 0 + 6 + 6 + 0`).
- Corpus JSON `705 + 25 = 730`, fixture JSON `660 + 25 = 685` — the 25 new JSON files are exactly 5 per new dir.
- Zero nonempty stderr on all 138 runs.
- Independent cross-checks: `git diff --name-only 28706dc..HEAD -- corpus/` = `check_bible.py` + 33 files in the 5 new dirs (34 total), so **no inherited fixture bytes moved**; `sha256sum .ufo/rounds/r86/diagnostic.stdout.json` = `471054be46458c3116201fa487b5c8fa343be0a18a203f5b8c8a44dbffa5e405`, matching the pin recorded in `patches/S4-census-extension.md`; `git diff --name-only 5eb9451..HEAD -- corpus/live/` = 0 files, so the r85 live probes are still baseline-byte-identical.
- The per-record disclosure signature (`ambiguous holder identity`) appears in exactly 2 of the 138 census dirs — the two new masked-break fixtures. No inherited fixture exercises the new path, which is consistent with S1's finding that no pre-r87 active fixture contains an ambiguous holder.

## Part B — masked-break disclosure verification (both fixtures)

Command (repo root): `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous` and the `…-from-ambiguous` sibling. Observed (`JCAL1-disclosure-coverage.json`):

```
VIOLATION: entities[5].id: duplicate entities id 'dup'
VIOLATION: entities[3].provenance[0].to_holder: ambiguous entity 'dup'
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[0]
6 violation(s); no canon changed
EXIT=1
```

The `from_ambiguous` fixture is identical except that the stop is on `from_holder 'dup'` at `provenance[0]`. Both fixtures are 3 provenance records with the ambiguous holder at record 0.

Coverage check (script `/tmp/jcal1/verify_disclosure.py`, output `JCAL1-disclosure-coverage.json`), per fixture:

| property | to-ambiguous | from-ambiguous |
|---|---|---|
| records / stop index / records at-or-after stop | 3 / 0 / 3 | 3 / 0 / 3 |
| legacy item-global notice lines | 1 | 1 |
| per-record disclosure lines | 3 | 3 |
| disclosure labels | `[0]`, `[1]`, `[2]` | `[0]`, `[1]`, `[2]` |
| exactly one per covered record | yes | yes |
| names holder field + id (`to_holder 'dup'` / `from_holder 'dup'`) | yes, all 3 | yes, all 3 |
| names the origin record (`first occurred at entities[3].provenance[0]`) | yes, all 3 | yes, all 3 |
| disclosure is the first line bearing that record label | `[1]`,`[2]` yes; `[0]` no (see below) | `[1]`,`[2]` yes; `[0]` no |

So "each record at/after the stop carries one disclosure naming the holder id + origin" **holds**. The single exception to the "first line" property is the stop record itself, where the pre-existing item-global notice is printed before the new line — the two lines are near-duplicates ("… unassessed at this and all later records because holder identity is ambiguous" vs "… unassessed because ambiguous holder identity to_holder 'dup' first occurred at …"). Duplicative, not contradictory; flagged as debt item 2.

## Part C — the 7 r86-class adversarial probes

All probes were generated and run entirely in scratch (`/tmp/jcal1/probes.py`, `probes/`), never in the repo. Base fixture is `corpus/fixtures/consistent` with a duplicated `dup` entity added to create ambiguity. Commands are `python3 corpus/fixtures/check_bible.py /tmp/jcal1/probes/<case>` from the repo root; full stdout in `JCAL1-probes.json`.

| # | probe | what it isolates | observed | correct? |
|---|---|---|---|---|
| 1 | `r87-jcal1-direction-to-clean` | ambiguous `to_holder` at `[0]`, later records unique and continuous | stop notice + per-record line at `[0]`; one disclosure at `[1]` and `[2]`; 6 violations, exit 1 | yes |
| 2 | `r87-jcal1-direction-from-clean` | ambiguous `from_holder` at `[0]`, same tail | same, with `from_holder 'dup'` named; 6 violations, exit 1 | yes |
| 3 | `r87-jcal1-per-item-reset` | latch must be per item: item A ambiguous at `[0]`, item B has a genuine unique-holder break | item A: 3 disclosures; **item B: `entities[6].provenance[1]: provenance chain break; expected from_holder 'mira', got 'tower'` still reported**, no disclosure lines on B; 8 violations | yes — no cross-item suppression |
| 4 | `r87-jcal1-prefix-findings` | findings before the stop survive | `[0]` dangling finding kept, stop at `[1]`, disclosures at `[1]` and `[2]` only; 6 violations | yes |
| 5 | `r87-jcal1-dangling-controls` | dangling holders must not be mistaken for ambiguity | only 2 dangling findings; **no stop, no disclosure**; 2 violations both before and after | yes |
| 6 | `r87-jcal1-both-fields-invalid` | both fields ambiguous on one record | cause names both: `ambiguous holder identity to_holder 'dup', from_holder 'dup'`; both stop lines; `[2]` disclosure repeats both; 6 violations | yes |
| 7 | `r87-jcal1-post-stop-null-from` | post-stop `from_holder: null` | `[1]` and `[2]` disclosed; **no spurious "first record must have from_holder null" chain-break claim**; 6 violations | yes |

Six additional probes beyond the required seven:

| probe | observed | correct? |
|---|---|---|
| `r87-jcal1-direction-to` (repeat ambiguity at a later record, `[1].from_holder = 'dup'`) | field-local ambiguity finding at `[1]` added, but **no second stop line**; the `[0]`-origin disclosure is still the one used at `[1]`/`[2]` | yes |
| `r87-jcal1-post-stop-nondict` (post-stop record is a string) | disclosure line emitted for the non-object record, then `[1]: expected object`; 7 violations | yes — the disclosure is unconditional |
| `r87-jcal1-post-stop-wrongkeys` (post-stop record missing `source_id`) | disclosure line, then `[1]: expected exactly tick, from_holder, to_holder, source_id`; 7 violations | yes |
| `r87-jcal1-residual-wrongkeys-ambiguous` (**the ambiguous-holder record itself** has a wrong key set) | only `[1]: expected exactly tick, from_holder, to_holder, source_id`; **no stop, no disclosure at `[1]`/`[2]`, and the deliberate `[2]` break is silently unreported**; 2 violations, identical pre- and post-C1 | **residual gap — see below** |
| `r87-jcal1-residual-extrac-ambiguous` (ambiguous-holder record has an extra key) | same as above | residual gap |
| `r87-jcal1-dangling-controls` | (listed above as #5) | — |

**Residual masked-break vector (pre-existing, not introduced by C1).** In `check_bible.py` the per-record key-set check and the object check both `continue` before the holder-resolution block, so a record that carries an ambiguous holder id *and* a shape violation never reaches `record_holder_ambiguous`, never arms `holder_ambiguity_stop`, and (via `can_check_chain = False`) silently disables all later comparisons. Result: a genuine later break is neither reported as a break nor disclosed as unassessed — the same silent path C1 closed for well-shaped records. Both baseline and delivered checkers produce identical output here (2 violations, exit 1), so this is an unclosed gap, not a regression. Whether to close it is an integration decision (it would require resolving holders independently of record shape, or arming the stop from the shape-failure path).

## Part D — independent before/after on identical inputs

The strongest available calibration evidence is the same input judged by the pre-C1 and post-C1 checkers. Script `/tmp/jcal1/before_after.py`, output `JCAL1-before-after.json`.

Cases where the per-record disclosure is new (`baseline → head` violations, `+` = added disclosure lines; exits unchanged `1/1` in every row):

| case | base | head | added |
|---|---|---|---|
| `r87-masked-break-to-ambiguous` (delivered) | 3 | 6 | +3 |
| `r87-masked-break-from-ambiguous` (delivered) | 3 | 6 | +3 |
| `r87-jcal1-direction-to-clean` | 3 | 6 | +3 |
| `r87-jcal1-direction-from-clean` | 3 | 6 | +3 |
| `r87-jcal1-direction-to` | 4 | 7 | +3 |
| `r87-jcal1-per-item-reset` | 5 | 8 | +3 |
| `r87-jcal1-post-stop-nondict` | 4 | 7 | +3 |
| `r87-jcal1-post-stop-wrongkeys` | 4 | 7 | +3 |
| `r87-jcal1-post-stop-null-from` | 3 | 6 | +3 |
| `r87-jcal1-prefix-findings` | 4 | 6 | +2 |
| `r87-jcal1-both-fields-invalid` | 4 | 6 | +2 |
| `r85-masked-ambiguous` (live probe) | 3 | 5 | +2 |
| `r85-harbor-repro` (live probe) | 5 | 7 | +2 |
| `r85-isolated-ambiguous` (live probe) | 3 | 4 | +1 |

The three r85 live probes are byte-identical to the round-85 baseline (`git diff 5eb9451..HEAD -- corpus/live/` empty) and are the only *pre-existing* inputs in the tree that exercise the new path; they confirm the change generalises beyond the two new fixtures, including to a case where a *second* record later carries its own ambiguous `from_holder` (`r85-harbor-repro`, disclosed with the `[1]` origin).

## Part E — harm sweep

Over all 156 replayed cases (138 fixture dirs + 13 scratch probes + 5 r85 live probes), comparing the pre-C1 and delivered checkers:

```json
{"cases": 156, "cases_with_removed_lines": 0, "exit_code_changes": 0,
 "added_lines_outside_disclosure_signature": 0,
 "cases_where_disclosure_appears_only_after": 15}
```

- **0 violation lines removed** anywhere, so no previously visible finding was traded away.
- **0 exit-code changes** anywhere.
- **0 added lines outside** the exact per-record disclosure signature.
- The 133 inherited fixture tuples are byte-identical (Part A), and the only cases gaining lines are the 15 ambiguity cases above.
- `corpus/fixtures/r87-myth-cluster` (the C3 coverage fixture) is unaffected: exit 0, `CLEAN`, sha `afe570fc…` — the same clean-output hash as `consistent`.

## Named debt / gaps (no action taken by this seat)

1. **Malformed-ambiguous residual vector** (Part C): the stop is only armed from well-shaped records, so a shape-violating record carrying an ambiguous holder id leaves later comparisons silently unassessed and undisclosed, and a later real break unreported. Pre-existing; identical in both checkers.
2. **Duplicated disclosure at the stop record** (Part B): the legacy item-global notice and the new per-record line both fire there, saying nearly the same thing. Wording/verbosity, not a correctness problem; E1/CB1 already flag that `corpus/knowledge/holder-assessment-boundary.md`'s "exactly one notice per item" wording needs revision now that C1 has landed.
3. **Coverage of the new path is fixture-thin**: only the 2 new masked-break dirs (plus 3 live probes outside the census) exercise the disclosure, so a future regression in this path would be caught by 2 of 138 census dirs. C3's cluster and the other 3 new dirs do not touch it.
4. The disclosure states that comparisons were *unassessed*; it does not and should not assert that a break occurred. A reader must interpret it that way — that is the intended semantics (assessment never resumes, no identity is chosen), and C1's commit message is scoped correctly to it.

## Handoff / artifacts

- `lore-shokunin/.ufo/waves/round-87/followup/JCAL1.md` — this report (untracked; nothing committed).
- `lore-shokunin/.ufo/waves/round-87/followup/JCAL1-census.json` — 138-dir tuple diff summary.
- `lore-shokunin/.ufo/waves/round-87/followup/JCAL1-disclosure-coverage.json` — per-fixture disclosure coverage.
- `lore-shokunin/.ufo/waves/round-87/followup/JCAL1-probes.json` — full stdout for all 13 scratch probes.
- `lore-shokunin/.ufo/waves/round-87/followup/JCAL1-before-after.json` — per-case pre-C1 vs delivered comparison (156 cases).
- Scratch scripts retained at `/tmp/jcal1/{census.py,verify_disclosure.py,probes.py,before_after.py,check_bible.baseline.py}`.
- For the integrating seat: the calibration axis can be scored **improved** on the evidence above; debt items 1–3 belong in the round record, and item 1 is the one that deserves an explicit decision (accept as documented debt, or close in a later round).
