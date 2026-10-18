# V25 — CALIBRATION verdict (2026-10-17)

**CALIBRATION: IMPROVED, bounded — C3 verified on the delivered revision.** The new boundary record separates byte-change detection from dependency meaning, and all three dated corrections reproduce independently. This is one calibration verdict, not round-wide admission or a blanket no-axis-harm finding. The separate strict-baseline preservation FAIL in V15 is retained below for parent adjudication.

Axes named: calibration precision, replay fidelity, explicit non-establishment, and preservation as a guardrail. All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`; Python commands used `python3`. Required comparison baseline: `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`. Observed live HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`; `git merge-base --is-ancestor fe1ce46 HEAD` exited 0. The declaration HEAD was not silently substituted for the required baseline.

## Delivery prerequisite and report reconciliation

The first bounded poll checked both new T4 artifacts and an actual top-level `T4*.md` producer report, every 20 seconds, at most 40 attempts. It completed at attempt 25, after 480 seconds:

```text
POLL 25/40 artifacts={'corpus/knowledge/r100-crossing-arc-synthesis.md': True, 'corpus/knowledge/r100-provenance-semantics-boundary.md': True} producer_reports=['T4-knowledge-author.md']
READY: C3 artifacts and T4 producer report exist
```

The dated table rows were also present and inspected. I read the completed `.ufo/waves/round-100/seats/T4-knowledge-author.md` and re-read the final boundary record before the independent delivered-revision replays. Earlier missing-path observations and preparation of isolated controls were not treated as delivery or a verified plan.

A second bounded 20-second poll covered the narrow report superset V11–V15, explicitly excluding SELF V25. It completed at attempt 8, after 140 seconds. The actual roles resolved as V11 C2 synthesis, V12/V13/V14 C3, and V15 preservation/census; this was not an all-reports poll. Both polls completed before handoff; neither exhausted its cap, and no stall escape or needed background task remains.

Direct C3 reports read and reconciled:

- `.ufo/waves/round-100/seats/V12-c3-boundary.md`: PASS. Its final boundary hash matches mine; cited artifacts/ranges and the AC-1/AC-2/AC-3 distinctions are supported, with independent real gate replays and no byte-identity-to-semantics overclaim.
- `.ufo/waves/round-100/seats/V13-c3-addenda.md`: PASS. Independently ran the exact nine documented commands; complete commands/stdout/stderr/exits matched 9/9, with unchanged table/tool/contract hashes.
- `.ufo/waves/round-100/seats/V14-c3-addenda-scope.md`: PASS. Exactly three new dated data rows; 105 additions and zero removals; all 20,526 historical bytes preserved; AC pointers resolve to `LOG.md:3303-3313`.

Their successful conclusions agree with my independently constructed scratch mutants, not merely with T4's reported intent. Supplemental reports read: V11 C2 synthesis, V15 preservation/census, V17 gates-boundary, and V26 operability. V15's separate FAIL is not erased by the C3 agreement.

## Delivered bytes and append-only scope

Actual command:

```sh
python3 .ufo/waves/round-100/seats/V25-scratch/audit.py
```

Exit 0. Selected observed output:

```text
TABLE-HISTORICAL-PREFIX PASS baseline_bytes=20526 added_bytes=8907
TABLE-THREE-DATED-ROWS PASS [rows 10, 11, 12, each 2026-10-17 / r100]
HISTORICAL-SUPPORT-IDENTITY PASS 55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c
SAVED-REPLAY-RECEIPTS PASS 17/17 expected observations; tracked live and mirror hashes unchanged
SAVED-CONTROL-RECEIPTS PASS 7/7 expected observations; contract unchanged
AUDIT-CHECKS 37 / 37
```

The row-list line above abbreviates only the printed row text, not its pass condition. The complete raw rows, checks, exact live gate commands, stdout/stderr/exits, and expected hashes are retained in `V25-scratch/audit-delivered.json`. The table is 29,433 bytes, and the complete baseline remains its exact byte prefix. Exactly rows 10–12 are new dated data rows; their replay sections and current-coverage supersession follow without rewriting the old text.

The audit compared all four live gate/checker files byte-for-byte with actual `git show fe1ce46:<path>` output: all identical. Final SHA-256 values, also rechecked after all replays:

```text
corpus/knowledge/r100-crossing-arc-synthesis.md 6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc
corpus/knowledge/r100-provenance-semantics-boundary.md 29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36
corpus/knowledge/r99-gate-blind-spot-table.md f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff
corpus/tools/dependency_freeze.py fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c
corpus/tools/dependency-freeze-contract.json ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
corpus/tools/support_check.py 55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c
corpus/tools/map_obligations.py 86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9
corpus/fixtures/check_bible.py ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
```

`git diff --check -- corpus/knowledge/r99-gate-blind-spot-table.md` separately exited 0 with no output. New-document newline/trailing-whitespace checks were performed directly by `audit.py`, rather than claiming tracked diff checking covers untracked files.

## Own independent addenda replays

Actual parent command, after T4 completion:

```sh
python3 .ufo/waves/round-100/seats/V25-scratch/replay.py delivered
```

Observed exit 0, `REPLAY-CHECKS 17 / 17` and `TRACKED-HASHES-UNCHANGED True`. Every child command was a real CLI call, dispatched concurrently; complete exact argv, stdout, stderr, exits, before/after hashes, and expectation checks are in `V25-scratch/replay-delivered.json`. These are my isolated tool/contract/fixture mirrors, not producer-owned scratch outputs.

### Row 10 / AC-2: mapped-anchor removal was already support-visible

Two independently constructed r95 mirrors received only the excerpt replacement `depends on both ninth-bell entries` → `follows both ninth-bell entries`; J14 and every JSON byte were unchanged. Their excerpt SHA-256 was `b0725e215a8c51bd0dda5b384396913a6d8ea36e58caa928d5b0315d47fc1aae`, exactly the dated row's mutant. Historical files were extracted using actual `git show 4265df5:corpus/tools/<name>` calls for `dependency_freeze.py`, `support_check.py`, and `dependency-freeze-contract.json`. Historical support is byte-identical to delivered support.

Actual support commands:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/r95-historical-anchor-removal/corpus/tools/support_check.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/r95-historical-anchor-removal/corpus/fixtures/r95-crossing-aftermath
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/r95-delivered-anchor-removal/corpus/tools/support_check.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/r95-delivered-anchor-removal/corpus/fixtures/r95-crossing-aftermath
```

Both exit 1, with these observed lines:

```text
FAIL J14: source-support; mode=verbatim; anchor=not-found
SOURCE-SUPPORT 14/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 16/17
FAIL: J14: source-support anchor missing
RESULT FAIL
```

Actual historical/delivered freeze commands are the same two fixture paths with their respective mirrored `dependency_freeze.py`; their complete literal argv are in `replay-delivered.json`. Historical freeze exited 0, digest `d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9`, `RESULT PASS`. Delivered freeze exited 2, `DIGEST-MISMATCH` naming `fictional-excerpts.md`, content digest `b97a3b80df29110f6f369c7bd52ee09cd733e46f3f7d84420563c931744f7dca`, `RESULT ERROR`. Both complete freeze stdout streams occur verbatim in the delivered table. Additional real checker/map calls on my delivered r95 mutant exited 0: CLEAN and `OBLIGATIONS raw=15 mapped=15` / `RESULT PASS`.

Thus historical freeze blindness was not all-gate blindness for an unmatched mapped verbatim anchor. The failure is lexical, not evidence that support checking understands dependency meaning.

### Row 11 / AC-1: structural findings precede digest reporting

My path-bound r98 mirror drops only `evin-ninth-bell` from `paired-crossing-decision.depends_on` and makes the same excerpt-only replacement. Actual command:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/semantic-precedence/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/semantic-precedence/corpus/fixtures/r98-clerk-filing
```

Complete observed stdout, exit 1:

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
```

There is no `DIGEST-MISMATCH` despite the additional prose edit. The inventory-clean prose-only twin was independently run:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/mapped-anchor-removal/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/mapped-anchor-removal/corpus/fixtures/r98-clerk-filing
```

It exited 2, `DIGEST-MISMATCH` naming `fictional-excerpts.md`, content digest `c811669ea2534d48122939e270599376160b8f5936eecb2e766c141464b6808b`, `RESULT ERROR`. These reproduce the table's full structural stdout and prose-control digest. The words “semantic inventory” mean modeled JSON comparison, not prose entailment.

### Row 12 / AC-3: combined invocation is invalid only

Actual command, using my byte-identical delivered tool/contract mirror:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/combined-arguments/corpus/tools/dependency_freeze.py /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/combined-arguments/corpus/fixtures/r98-clerk-filing --freeze /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/combined-arguments/corpus/fixtures/r98-clerk-filing
```

Complete observed stdout, exit 2:

```text
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
```

Exactly one finding; no FREEZE/DIGEST receipt or structural/digest finding. Every tracked live and mirrored contract hash was unchanged. This exercises CLI rejection before selecting verification/freezing, not a valid guarded write.

## Calibration controls and non-establishment bounds

Seven supplementary real CLI calls were dispatched concurrently; all seven expected observations matched. Complete literal commands and outputs are in `V25-scratch/controls-delivered.json`:

- Coherent r98 excerpt+J14 replacement: checker CLEAN 0, support `SOURCE-SUPPORT 20/20` / `VALIDATED-ROWS 22/22` / PASS 0, map `OBLIGATIONS raw=20 mapped=20` / PASS 0, freeze `DIGEST-MISMATCH` 2 naming both Markdown files, digest `1f73326f38eb20f75d6c2541df5ec67ae20e157e5b4c1053dc10464ae88d67f2`. This empirically separates lexical coherence from byte identity; neither is asserted to prove entailment.
- Two r95 checker/map controls on the anchor mutant: CLEAN/PASS, exits 0, as noted above.
- Actual scratch-contained regression command:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/clean/corpus/tools/dependency_freeze.py --self-test
```

Observed `SELF-TEST 18/18`, `RESULT PASS`, exit 0, including `markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`. The self-test base and all transient trees were inside V25 scratch; temporary trees were automatically removed.

The boundary record's lines 8, 14–28, 32–36, and 55 are appropriately limited: hash identity is not dependency adequacy, whole-claim entailment, testimony truth, authenticated chronology, source or institutional identity, rights/permission, cultural authority, resolution, or canon. Re-freezing is a mutable integration-time operation, not authenticated immutable history. Named-file digest reporting is conditional on valid guards and a clean modeled inventory; it is not a universal exit-2 promise.

The declared ten-file set is not every neighboring file. The r88 `symbolism-clause-map.md` exclusion remains explicit. The separate r100 tick-16 edge is also not silently credited: my `audit.py` ran all seven live pinned-fixture commands, each PASS 0, and this actual negative bound command:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review
```

Observed `FINDING UNPINNED-FIXTURE: no pin for 'r100-docket-review'` listing exactly the seven declared pins, `RESULT ERROR`, exit 2. This is the stated coverage limit, not a new calibration failure. The dossier's seven snapshots are a different set from the seven frozen fixtures.

The dated addendum qualifies historical text rather than deleting it. It does not claim every older broad sentence has been rewritten, and future claims must not drop these conditions. All intentional non-zero probe results above are expected evidence, not suppressed failures or unresolved red tests. No C3 replay contradiction or unsupported boundary guarantee was found.

## Separate preservation finding retained for parent adjudication

`V15-preservation-census.md:11-15,406-457,494` reports strict baseline preservation **FAIL**: `LOG.md` and `SCORECARD.md` differ from `fe1ce46` outside its producer allowlist, although both changes were committed before dispatch and producer-only worktree scope passes. I do not override or silently rebase that finding.

I independently ran these exact read-only Git commands via lane-root `python3` subprocess calls:

```sh
git diff --name-only fe1ce46 HEAD -- LOG.md SCORECARD.md
git diff --name-only HEAD -- LOG.md SCORECARD.md
git log '--format=%h %s' --name-only fe1ce46..HEAD -- LOG.md SCORECARD.md
```

All exited 0. The first printed `LOG.md` and `SCORECARD.md`; the second printed nothing. The third printed:

```text
b5fe472 lore r100: declare sol-max 32-seat round before dispatch

LOG.md
ae67105 lore r99: close round — SCORECARD admitted section

SCORECARD.md
```

Thus the attribution is confirmed, but literal baseline/allowlist reconciliation remains with parent all-axis adjudication. A calibration improvement is not permission to conceal a separate strict FAIL or declare the entire round admitted.

## Exclusive write inventory and handoff

Only this absolute report and declared scratch `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V25-scratch/` were written. No corpus path, producer-owned byte, other seat's path, commit, push, or network endpoint was changed. No nested agent was dispatched. Initial direct `AGENTS.md` Read returned absent and the recursive lane glob found none; initial seat-directory listing returned absent, resolved by the bounded producer wait.

Scratch consists of `replay.py`, `audit.py`, `replay-delivered.json`, `controls-delivered.json`, `audit-delivered.json`, the generated exhaustive `file-manifest.json`, and these isolated mirror roots: `clean/`, `mapped-anchor-removal/`, `semantic-precedence/`, `combined-arguments/`, `coherent-prose/`, `r95-delivered-anchor-removal/`, `r95-historical-anchor-removal/`. Each mirror has copied tool/contract/fixture files only; `clean/` additionally contains the r95 self-test base. The manifest enumerates every persistent written path. No archive or repo-root temporary was created.

The delivered C3 hashes were stable through the final audit and subsequent report reconciliation. No calibration implementation/replay blocker remains. Round-wide admission, the retained V15 strict preservation finding, and future expansion of the pin set remain outside this verdict.

PASS — CALIBRATION improved, bounded: C3's boundary and three dated corrections independently verify on stable delivered bytes; byte detection is not semantics, and V15's separate strict-baseline FAIL remains for parent adjudication.
