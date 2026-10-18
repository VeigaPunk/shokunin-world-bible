# JCAL3 — Calibration judge #3: cause-branch fixture verification (round 89)

Judged tree: `1b09f3ff8016b26a2259e086f673d0112f4f54e5` (work commit; `git rev-parse HEAD`).
Baseline control: `51b286b` extracted with `git archive 51b286b | tar -x -C /tmp/jcal3/base`.
Tree state at judging: `git status --porcelain` → `?? .ufo/waves/round-89/followup/` only
(the permitted seat output directory); no tracked file modified. All scratch under `/tmp/jcal3/`.

## Work performed

- Replayed all 10 in-scope fixtures (8 cause-branch + the FN-2 pair) on the delivered tree and on a
  baseline control. The r89 fixture directories do not exist at `51b286b`, so the 10 directories were
  copied into the baseline archive before the control run; this is the only way the baseline run can
  exercise the same inputs, and it is stated rather than hidden.
- Verified every declared README expectation line by line: exit code, first-stop cause string,
  first-stop origin location, per-record disclosure range, and the "no later comparison" clause.
- Ran a 9-mutation matrix in `/tmp/jcal3/mut*` to test whether each fixture actually discriminates a
  wrong implementation (prose expectations are not machine-enforced, so discriminating power had to be
  measured, not assumed).
- Ran a disclosure-string coverage ledger over all 160 fixture directories for the four FN-1 raw-presence
  strings and the two FN-2 qualification strings.
- Ran an independent exit/violation-count census diff (delivered checker vs baseline checker) over the
  same 160 directories.
- Two 60 s wait-checks per the wave protocol: `2026-10-17T04:17:19-03:00 → 04:18:19-03:00` and
  `04:18:19-03:00 → 04:19:19-03:00`. Nothing was outstanding: the wave's work commit `1b09f3f` and a
  clean tree were already present at seat start, so both checks returned no new dependency and the seat
  proceeded on the delivered tree. No gap is owed.

## Before → after measurements

### Fixture replay on the delivered tree

Command (one directory per line; the loop below is the exact command form used):

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for d in r89-c1-invalid-tick r89-c1-invalid-from-holder r89-c1-invalid-to-holder \
         r89-c1-malformed-source-id r89-c1-multi-cause-valid r89-f2-dangling-to \
         r89-f2-dangling-from r89-f2-invalid-source-id r89-fn2-control \
         r89-fn2-unresolved-chain-break; do
  python3 corpus/fixtures/check_bible.py corpus/fixtures/$d; echo "exit=$?"
done
```

Observed, per fixture (first-stop disclosure lines only; local `VIOLATION` lines elided where repeated):

| fixture | exit | first stop (observed) | origin | records disclosing | README expectation met? |
|---|---|---|---|---|---|
| `r89-c1-invalid-tick` | 1 | `malformed record (invalid tick)` | `entities[3].provenance[1]` | `[1]`,`[2]`,`[3]` | yes, literally |
| `r89-c1-invalid-from-holder` | 1 | `malformed record (invalid from_holder)` | `entities[3].provenance[1]` | `[1]`,`[2]` | yes, literally |
| `r89-c1-invalid-to-holder` | 1 | `malformed record (invalid to_holder)` | `entities[3].provenance[1]` | `[1]`,`[2]` | yes, literally |
| `r89-c1-malformed-source-id` | 1 | `malformed record (invalid source_id)` | `entities[2].provenance[1]` | `[1]`,`[2]` | yes, literally |
| `r89-c1-multi-cause-valid` | 1 | `malformed record (invalid tick); ambiguous holder identity to_holder 'r89-c1-multi-cause-valid-ambiguous-holder'` | `entities[2].provenance[0]` | `[0]` | yes — both causes named |
| `r89-f2-dangling-to` | 1 | `holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index` | `entities[3].provenance[1]` | `[1]`,`[2]`,`[3]` | **no — quoted string differs** |
| `r89-f2-dangling-from` | 1 | `holder reference from_holder 'r89-f2-missing-from' absent from raw entities and absent from the resolved index` | `entities[3].provenance[1]` | `[1]`,`[2]`,`[3]` | **no — quoted string differs** |
| `r89-f2-invalid-source-id` | 1 | `source reference 'r89-f2-unknown-source' absent from raw sources and absent from the resolved index` | `entities[3].provenance[1]` | `[1]`,`[2]`,`[3]` | **no — quoted string differs** |
| `r89-fn2-control` | 1 | `provenance chain break; expected from_holder 'f3-dup', got 'mira'` (unqualified) | `entities[3].provenance[1]` | `[1]` | yes, literally |
| `r89-fn2-unresolved-chain-break` | 1 | `input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'` | `entities[4].provenance[1]` | `[1]` | yes, literally |

The two README clauses that assert a *negative* were also checked and hold: for
`r89-c1-invalid-tick`/`-from-holder`/`-to-holder`/`-malformed-source-id` and for all three `r89-f2-*`
fixtures, no chain-break or tick-order comparison line appears after the stop (the only lines are the
local defect plus the `remain unassessed` disclosures).

### Baseline control (same inputs, `51b286b` checker)

Command:

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for d in r89-c1-invalid-tick ... r89-fn2-unresolved-chain-break; do
  cp -r corpus/fixtures/$d /tmp/jcal3/base/corpus/fixtures/
done
cd /tmp/jcal3/base && python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>
```

Observed first-stop disclosures at baseline vs delivered:

| fixture | baseline first stop | delivered first stop | delta |
|---|---|---|---|
| `r89-c1-invalid-tick` | `malformed record (invalid tick)` | identical | none |
| `r89-c1-invalid-from-holder` | `malformed record (invalid from_holder)` | identical | none |
| `r89-c1-invalid-to-holder` | `malformed record (invalid to_holder)` | identical | none |
| `r89-c1-malformed-source-id` | `malformed record (invalid source_id)` | identical | none |
| `r89-c1-multi-cause-valid` | `malformed record (invalid tick)` — ambiguity omitted | `malformed record (invalid tick); ambiguous holder identity to_holder '…'` | **both causes now named** |
| `r89-f2-dangling-to` | `dangling holder to_holder 'r89-f2-missing-to'` | `holder reference to_holder '…' absent from raw entities and absent from the resolved index` | wording replaced (FN-1) |
| `r89-f2-dangling-from` | `dangling holder from_holder 'r89-f2-missing-from'` | `holder reference from_holder '…' absent from raw entities and absent from the resolved index` | wording replaced (FN-1) |
| `r89-f2-invalid-source-id` | `unknown source 'r89-f2-unknown-source'` | `source reference '…' absent from raw sources and absent from the resolved index` | wording replaced (FN-1) |
| `r89-fn2-control` | `provenance chain break; expected from_holder 'f3-dup', got 'mira'` | identical (unqualified) | none — control behaves as designed |
| `r89-fn2-unresolved-chain-break` | `provenance chain break; expected from_holder 'f3-dup', got 'mira'` | qualified `possible provenance chain break, not a definite identity mismatch: … not uniquely resolvable (2 raw … only 1 …)` | **qualifier added (FN-2)** |

### Independent census diff (delivered vs baseline), 160 directories

Command:

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin && python3 - <<'EOF'
import subprocess,pathlib
root=pathlib.Path('corpus/fixtures'); dirs=sorted(d for d in root.iterdir() if d.is_dir())
diff=[]
for d in dirs:
    a=subprocess.run(['python3','corpus/fixtures/check_bible.py',str(d)],capture_output=True,text=True)
    b=subprocess.run(['python3','/tmp/jcal3/base/corpus/fixtures/check_bible.py',str(d.absolute())],capture_output=True,text=True)
    na=len([l for l in a.stdout.splitlines() if l.startswith('VIOLATION:')])
    nb=len([l for l in b.stdout.splitlines() if l.startswith('VIOLATION:')])
    if (a.returncode,na)!=(b.returncode,nb): diff.append((d.name,b.returncode,nb,a.returncode,na))
print(f"dirs={len(dirs)}  changed={len(diff)}"); [print(' ',*x) for x in diff]
EOF
```

Observed: `dirs=160  changed=0` (`changed` = differing exit code or violation count). The first run of
this loop printed `dirs=161` because a transient directory existed during that loop and was gone
immediately after; the loop was re-run cleanly and the confirming counts are
`ls -d corpus/fixtures/*/ | wc -l` → `160`, `git status --porcelain corpus/fixtures` → empty, and the
re-run → `dirs=160  changed=0`. Only the clean re-run is reported here. Independent of C8's own delta
predictor, this reproduces the claim's
"0 exit changes" and adds "0 violation-count changes" across all 160 directories. The separate
`clean=32 violations=128` census was also reproduced by direct replay.

### Mutation matrix (discriminating-power test)

Each mutation was applied to a copy of the delivered checker in `/tmp/jcal3/mut*`; a fixture "catches"
a mutation when its output changes against the delivered checker. Commands are the heredoc scripts in
`/tmp/jcal3/` runs; the anchors are the exact delivered source lines.

| mutation | fixtures whose output changes (i.e. would catch it) |
|---|---|
| M1 stop-cause `'; '.join(...)` → first-wins | `r89-c1-multi-cause-valid` |
| M2 FN-2 qualification branch disabled (`if expected_detail or from_detail:` → `if False:`) | `r89-fn2-unresolved-chain-break` |
| M3 revert FN-1 `to_holder` wording to `dangling holder to_holder` | `r89-f2-dangling-to` |
| M3b revert FN-1 `from_holder` wording to `dangling holder from_holder` | `r89-f2-dangling-from` |
| M4 revert FN-1 source wording to `unknown source` | `r89-f2-invalid-source-id` |
| M5 rename `malformed record (invalid tick)` | `r89-c1-invalid-tick`, `r89-c1-multi-cause-valid` |
| M6 rename `malformed record (invalid from_holder)` | `r89-c1-invalid-from-holder` |
| M7 rename `malformed record (invalid to_holder)` | `r89-c1-invalid-to-holder` |
| M8 rename `malformed record (invalid source_id)` | `r89-c1-malformed-source-id` |

Result: each of the 9 non-control fixtures is caught by at least one mutation, so each is a real
discriminator against some wrong implementation. `r89-fn2-control` is caught by no mutation, which is
its designed role (it must stay unqualified under M2).

### Disclosure-string coverage ledger, all 160 fixture directories

Command: replay every directory, count the four FN-1 raw-presence strings and the two FN-2 strings.

Observed:

```text
absent from raw entities and absent from the resolved index : total=6  dirs=2  (r89-f2-dangling-to, r89-f2-dangling-from)
present in raw entities but                                : total=0  dirs=0
absent from raw sources and absent from the resolved index : total=15 dirs=5  (r87-probe-multi-invalid, r87-probe-record-and-chain, r88-mixed-stop, r88-nonholder-stop, r89-f2-invalid-source-id)
present in raw sources but                                 : total=0  dirs=0
possible provenance chain break, not a definite identity mismatch : total=1 dirs=1 (r89-fn2-unresolved-chain-break)
is not uniquely resolvable (                               : total=1  dirs=1 (r89-fn2-unresolved-chain-break)
```

## Findings & named debt

**Verdict recommendation — calibration: improved (bounded).** The delivered tree's three C1
amendments are all observable and all fixture-pinned: the valid-key combined-cause summary
(`r89-c1-multi-cause-valid` names both `malformed record (invalid tick)` and
`ambiguous holder identity to_holder '…'`, where the baseline named only the tick); the FN-2
qualification (`r89-fn2-unresolved-chain-break` gains `possible provenance chain break, not a definite
identity mismatch` while the matched `r89-fn2-control` stays byte-identical and unqualified — a proper
control pair, verified by `diff` of the two `entities.json`: identical except one inserted `f3-dup`
row with `"first_appearance": ""`); and the FN-1 wording (raw-presence-aware disclosure in both
`to_holder`/`from_holder` and source variants). 0 exit changes and 0 violation-count changes across
160 directories, reproduced independently. The bound is the declared-expectation surface below.

**Debt 1 — three `r89-f2-*` fixture READMEs declare the pre-FN-1 wording (declared expectation not
emitted on the delivered tree).** `corpus/fixtures/r89-f2-dangling-to/README.md:9` declares
`` `dangling holder to_holder 'r89-f2-missing-to'` ``, `r89-f2-dangling-from/README.md:9` declares
`` `dangling holder from_holder 'r89-f2-missing-from'` ``, and `r89-f2-invalid-source-id/README.md:9`
declares `` `unknown source 'r89-f2-unknown-source'` ``. On the delivered tree none of those literal
strings appears in any output; the delivered disclosures are `holder reference <field> '…' absent from
raw entities and absent from the resolved index` and `source reference '…' absent from raw sources and
absent from the resolved index`. The fixtures' *substance* is correct (right cause class, right
`entities[3].provenance[1]` origin, right `[1]`–`[3]` disclosure range), so this is a documentation
parity defect, not a behavioural one — the same class r88 closure repaired at `51b286b`. These three
READMEs were authored by F2 against the pre-FN-1 checker and were integrated unchanged alongside X1's
FN-1 patch; F2's own seat report (`.ufo/waves/round-89/F2.md`) records the same pre-FN-1 strings as its
measured "after patch" output, so the staleness is visible in the wave evidence and was not caught at
integration.

**Debt 2 — `corpus/knowledge/holder-assessment-boundary.md` is stale and in one place directly
contradicted.** The r87 fixture README points to this file as "the current contract", and it was not
touched in r89 (`git diff --stat 51b286b 1b09f3f -- corpus/knowledge/` lists only
`r88-sourced-inspiration-decision-table.md`, `r89-cross-cluster-contradiction.md`,
`reference-ledger.md`; `grep -n r89` in the file returns nothing). Concrete contradictions:

- `:152`–`:153` cause-table rows 9/10 still declare `dangling holder to_holder {id!r}` /
  `dangling holder from_holder {id!r}`; the delivered code emits `holder reference … absent from raw
  entities and absent from the resolved index`.
- `:156` row 13 still declares `unknown source {id!r}`; delivered emits `source reference … absent from
  raw sources and absent from the resolved index`.
- `:165` decision-table row "Dangling holder, either field" still contracts
  `` first stop: dangling holder {field} {id!r} at {record_label} ``.
- `:221`–`:228` (cause-precedence block) states "Cause precedence inside a shape-valid record (first
  failing check wins, and later causes are NOT appended to the clause) … The only combined clause is the
  shape-invalid one", and `:169` repeats "the named `first stop:` clause names only the FIRST check in
  precedence order — a bad tick masks a simultaneous ambiguity … Only the shape-invalid branch combines
  two cause phrases". The delivered `r89-c1-multi-cause-valid` output is a **shape-valid** record whose
  clause names **both** causes, so the contract document now asserts the opposite of the delivered
  behaviour on the exact case C1(ii) was created to change.
- `:338`–`:348` sample outputs still show `first stop: unknown source '…'`.

**Debt 3 — FN-1's "present in raw … but absent from the resolved index" branch has zero fixture
coverage.** The coverage ledger shows 0 occurrences of `present in raw entities but` and 0 of
`present in raw sources but` across all 160 directories, versus 6/15 for the truly-absent half. The
delivered code does implement the distinction (the `raw_presence` ternaries), but only the
"absent from raw" half is pinned by a durable fixture. A fixture with a schema-rejected entity row
(e.g. an invalid `kind`) referenced as a provenance `to_holder` would exercise the other half.

**Debt 4 (bound, not defect) — 4 of the 8 cause-branch fixtures are not delta-discriminators against
the baseline.** `r89-c1-invalid-tick`, `-invalid-from-holder`, `-invalid-to-holder` and
`-malformed-source-id` produce byte-identical output on the baseline and delivered checkers, because
those four cause branches were already correct before C1. They are genuine mutation-discriminators
(M5–M8 catch them) and they pin the cause vocabulary, but they cannot detect a regression of the r89
change itself; only `r89-c1-multi-cause-valid` and `r89-fn2-unresolved-chain-break` are
delta-discriminating among the eight.

**Debt 5 (owed at closure, not a work-wave defect) — the fixture registry has no Round 89 section.**
`corpus/fixtures/README.md` ends at `## Round 88: stop-cause disclosure + second cluster` and contains
no `r89` mention. Precedent: the Round 88 section was added at the r88 *closure* commit
(`git log -S "Round 88: stop-cause disclosure" --oneline -- corpus/fixtures/README.md` → `51b286b`),
not at the work commit. The same closure-time registry update is therefore owed for r89, listing the
10 new fixtures and carrying the revision note that the `dangling holder` / `unknown source` disclosure
strings were superseded at r89 (the registry already carries the analogous r87→r88 note).

**Debt 6 (pre-existing pattern, unchanged) — the prose expectations are not machine-enforced.** No
harness compares fixture output to the READMEs; `grep -rln "expect" corpus/fixtures/ .ufo/` finds only
README prose and the checker source. All 10 fixtures are durable pins enforced by manual replay only.
This is the r87/r88 status quo and is not a regression, but it is why Debt 1 could survive integration
unnoticed.

## Handoff

- Report: `lore-shokunin/.ufo/waves/round-89/followup/JCAL3.md`; machine-readable matrix:
  `lore-shokunin/.ufo/waves/round-89/followup/JCAL3-fixtures.json`.
- Verdict recommendation to the L1: **calibration improved (bounded)**. No `harmed` finding; no trade
  found. The bound is Debt 1 + Debt 2 (stale declared-expectation surface: 3 fixture READMEs and the
  contract document), Debt 3 (uncovered FN-1 raw-present branch), Debt 4 (4 of 8 fixtures not
  delta-discriminating). Debts 1, 2 and 5 are cheap, mechanical, closure-time repairs — the checker
  itself needs no further change for any of them.
- Evidence path: baseline archive `/tmp/jcal3/base` (51b286b + the 10 r89 fixture dirs copied in),
  mutation copies `/tmp/jcal3/mut`, `/tmp/jcal3/mut2`, wait-check log `/tmp/jcal3/wait{1,2}.txt`.
- No commit, no push, no tracked write outside the two permitted files; sibling repos untouched; the
  tree was clean before and after judging (`git status --porcelain` → only the untracked
  `.ufo/waves/round-89/followup/` directory).
- Nothing left unverified within this seat's scope. Debt 1/2/5 repairs are the parent's decision; this
  seat did not apply them (they are outside the permitted write path).
