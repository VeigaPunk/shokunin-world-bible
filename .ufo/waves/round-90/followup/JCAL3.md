# JCAL3 — calibration judge #3 (round-90 follow-up)

Seat scope: line-by-line verification of the four r90 fixture READMEs against the
delivered tree at `ca7f9ef` (baseline `e97613c`), regression-check of the r89
fixtures (r89-fn2 pair, r89-c1/f2 sets) against the r90 baseline tuples, plus the
judging-lane freeze check (delivered checker vs X2+X3 composed on `e97613c`).

Delivered commit under test: `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13` (tree clean;
only untracked follow-up artifacts present). All verdict evidence below comes from
that tree; scratch (`/tmp`) was used only for the freeze build, the README control,
and the probe matrix. No commit or push was made. Repo writes are limited to this
report and `followup/JCAL3-census-after.json`.

## Work performed

1. **Freeze-then-verify (blocking-if-mismatch).** Rebuilt the checker from
   `e97613c`, applied `X2-c1-nullonly.patch` then `X3-c1-tickonly.patch`, and
   compared SHA-256 against the delivered `corpus/fixtures/check_bible.py`.
2. **Delivered census.** Ran the exact B1 command template
   `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` from the repo
   root over every fixture directory (164), captured exit/stdout-SHA/violation
   count/stderr for each, and compared the three tuple fields field-wise against
   the B1 baseline manifest (160 rows) and the B2 manifest. Persisted the 164-row
   delivered census as `followup/JCAL3-census-after.json`.
3. **README line-by-line.** For each of `r90-c1-rawpresent-from`,
   `r90-c1-rawpresent-source`, `r90-c1-rawpresent-to`, `r90-c1-three-causes`:
   extracted the declared `Expected complete stdout` block from the README,
   ran the delivered checker and the unpatched `e97613c` checker on the fixture,
   and compared byte-for-byte (plus exit code and stderr). Independently verified
   every prose data claim (ID-occurrence isolation, key set, absence claims) by
   parsing the fixture JSON. Reproduced the to-holder true-absence control in
   scratch.
4. **r89 regression.** For all 11 `corpus/fixtures/r89-*` directories: compared
   `git ls-tree -r e97613c -- <dir>` against `git ls-tree -r ca7f9ef -- <dir>`
   (file bytes) and compared delivered tuples against the B1/B2 baselines.
5. **Repaired-shape probes.** Built C9-recipe probes from
   `r89-fn2-unresolved-chain-break` in `/tmp/jcal3-probes` (shared files
   symlinked) and ran both the unpatched and delivered checker on the four
   shapes: `chain-unresolved`, `tick-relevant-unresolved`, `null-from-chain`,
   `unrelated-duplicate-tick`.
6. **Integration fidelity.** Reconstructed all 24 files added by
   `F1-fixtures.patch` from the patch text and byte-compared them to the
   delivered fixtures (integrator-amendment check).
7. Cross-read the sibling follow-up receipts (`JCAL2-receipts.json`,
   `H4-census.json`, both untracked at read time) as peer corroboration.

No dependency wait-checks applied to this seat: the wave is committed and every
input artifact (B1/B2 manifests, X2/X3 patches, F1 fixtures, C9 ruling) is
present in the delivered tree.

## Before → after measurements

### Freeze check — PASS (no blocking finding)

```sh
S=/tmp/jcal3-freeze; mkdir -p $S/corpus/fixtures
git show e97613c:corpus/fixtures/check_bible.py > $S/corpus/fixtures/check_bible.py
cd $S
git apply --verbose $REPO/.ufo/waves/round-90/patches/X2-c1-nullonly.patch
git apply --verbose $REPO/.ufo/waves/round-90/patches/X3-c1-tickonly.patch
sha256sum $S/corpus/fixtures/check_bible.py $REPO/corpus/fixtures/check_bible.py
```

```text
X2: Applied patch corpus/fixtures/check_bible.py cleanly.
X3: Hunk #1 succeeded at 321 (offset 2 lines). Applied patch ... cleanly.
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  baseline e97613c checker
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  composed X2+X3
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  delivered checker
```

Composed = delivered, byte-identical. For the record, X1's own patch result
(`12866e734beb0e8fdfb641e9dab7cdaae7518fc0fdb8749a5e086981a0d1ae18`) differs
from the delivered file in the tick section only — consistent with the C9 ruling
to ship the X2+X3 composition instead. The delivered `X1-c1.patch` on disk hashes
`6d37eccfb913155aabd6e4e883870eab68676920dca1142d6d4482ae79316223`, matching
C8's receipt and the C9 rerun-script expectation.

### Delivered census (164 dirs) vs baseline

Command template (repo root, relative invocation, matching B1's form):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>
```

Observed aggregate (full per-dir tuples in `followup/JCAL3-census-after.json`):

```text
fixture_count=164 exit_counts={0: 32, 1: 132} total_violations=417 stderr_nonempty=0
changed_vs_baseline=[]  new_dirs=4  removed_dirs=[]  exit_status_changes=[]
baseline 160: exit_counts={0: 32, 1: 128} total_violations=399
```

- New dirs (all exit 1): `r90-c1-rawpresent-from`, `r90-c1-rawpresent-source`,
  `r90-c1-rawpresent-to`, `r90-c1-three-causes` (18 added violation lines:
  5+4+5+4).
- Zero changed tuples and zero exit changes across the 160 baseline paths.
- B1 and B2 manifests are byte-identical (both SHA-256
  `80bdc3b45ea785ea7e04dea776d95da0bd6dad088f60ae95100f21039cae42ad`).
- `followup/JCAL3-census-after.json` SHA-256
  `1ca18e34c3449e6767c3ddf26bc2746cdf767552246569f8874cd923f4ae6b31`.
- Peer corroboration: `JCAL2-receipts.json` reports the same 164/`{0:32,1:132}`/417
  census, empty changed/exit-flip lists, and the same freeze hashes.

This is the **first persisted 164-row delivered after-census**; the pre-existing
manifests (`B1/B2-tuples.json`, `X1-tuple-delta.json`, `C8-delta.json`) all cover
160 rows (and X1/C8 measure X1's candidate, not the delivered composition).

### README verification (4/4 exact)

Driver: extract the ```text block from each README; run delivered and unpatched
checkers; compare complete stdout bytes, exit code, stderr.

```text
r90-c1-rawpresent-from    after_vs_readme_exact=True before_vs_readme_exact=True exit=1 stderr='' after_stdout_sha256=9441ff58d63b35a82ffa9ce4693446775673759a2a9b6d045ccbd5a5575fa9c5
r90-c1-rawpresent-source  after_vs_readme_exact=True before_vs_readme_exact=True exit=1 stderr='' after_stdout_sha256=339592dabb98af2c8cae8ca44e7d57a030a3a72f41b03f6a431830684615cc28
r90-c1-rawpresent-to      after_vs_readme_exact=True before_vs_readme_exact=True exit=1 stderr='' after_stdout_sha256=01c7da74c8e0359b6ef1f8985a944fa027d73f989462e179c71827ca820ffcd2
r90-c1-three-causes       after_vs_readme_exact=True before_vs_readme_exact=True exit=1 stderr='' after_stdout_sha256=97723e8fe516a9086834a678a394a7b454ddcb05f87a8a9025149b16bd892148
```

Each README's "Checker exit: `1`" and "N violation(s); no canon changed" bullets
match the measured run (5, 4, 5, 4). The READMEs' before-state claim ("the
unpatched checker at e97613c was replayed before the C1 fix; its before-state
output matched this expectation") holds independently: unpatched output is
byte-equal to the declared block for all four.

Prose claims verified by parsing the fixture JSON:

- `rawpresent-from`: ghost id occurs exactly twice — `entities[0].provenance[0].from_holder`
  and the schema-invalid `entities[2].id` — and nowhere else in any JSON table.
- `rawpresent-source`: ghost id occurs exactly twice — `entities[0].provenance[0].source_id`
  and the schema-invalid `sources[1].id` — and nowhere else.
- `rawpresent-to`: ghost id occurs exactly twice — `entities[0].provenance[0].to_holder`
  and the schema-invalid `entities[1].id` — and nowhere else.
- `three-causes`: `entities[0].provenance[0]` has exactly the four required keys
  (`tick`, `from_holder`, `to_holder`, `source_id`) with values
  `tick=-1, from_holder=None, to_holder='r90-c1-three-causes-absent-holder',
  source_id='r90-c1-three-causes-absent-source'`; entity ids are `['r90-c1-three-causes-seal']`
  and source ids `['r90-c1-three-causes-source']`; both absent ids occur nowhere in
  their corresponding raw tables (only as the provenance references).

True-absence control (rebuilt in `/tmp/jcal3-ctl` from `rawpresent-to` with the
ghost raw row removed and the reference renamed, run with the unpatched checker,
scratch deleted afterwards):

```text
VIOLATION: entities[0].provenance[0].to_holder: dangling entity 'r90-c1-rawpresent-to-absent'
VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference to_holder 'r90-c1-rawpresent-to-absent' absent from raw entities and absent from the resolved index at entities[0].provenance[0]
2 violation(s); no canon changed
exit=1
```

This reproduces the README's quoted control line exactly.

### r89 regression (11/11 clean)

File bytes — `git ls-tree -r e97613c -- corpus/fixtures/<dir>` vs `ca7f9ef`:
aggregate hashes equal for all 11 dirs (no tracked file changed; also
`git diff --name-only e97613c ca7f9ef -- 'corpus/fixtures/r89-*'` is empty).

Tuples — delivered vs baseline (exit / stdout_sha256 / violations), all `SAME`:

```text
r89-fn2-unresolved-chain-break  1  66ed1438c6d1af003492d29569492ec0990e5b01b041fba1b4e21147eab4327a  2
r89-fn2-control                 1  4283f6955f40d49f6036ad61f55ab94e682cdb3c475af73c3d8350920cf06951  1
r89-c1-invalid-from-holder      1  ee7421731d2eadd33c7a98de6a738a348718c85c2855346494d4c7c9169a0cf9  3
r89-c1-invalid-tick             1  a137426b79585989e99d65688e201add6f0ab1f6d76c550fe36609aa94aa9e63  4
r89-c1-invalid-to-holder        1  6d1bb923c15a298d40d455fed9a5f4cfd3647c0eb152a503923c6b63d74c1a83  3
r89-c1-malformed-source-id      1  d34de40a91d986a75fb1718c6a44a1a6ebeb4f8e94bc86c588dee540ac275143  3
r89-c1-multi-cause-valid        1  35db96cd3891b33bf51573eed4dc8bf2f5414bd97b56b6a11bd08292cc14e66d  4
r89-f2-dangling-from            1  3c58ea3c26ff025e9ae1fbce13f77504902c9a1fc0b7448494740b7145804838  4
r89-f2-dangling-to              1  e0002f47309838a7632370de77d650329404f3cbe8f8feb960406828a8b0262c  4
r89-f2-invalid-source-id        1  68f8b0e8e72f89f359d9e86bc1ad956e2d586e89ce4c2a4013af02275230a6b3  4
r89-inspiration-paraphrase      0  afe570fcebf45fe3913b8b87c65a2e0408e99e9c69854757a2498d5be420c07e  0
```

The FN-2 pair keeps its qualified/first-stop behavior unchanged (the FN-2
qualification remains regression-visible, now inside a 164-row census).

### Repaired-shape probe matrix (delivered vs unpatched)

Built with C9's construction recipe on `r89-fn2-unresolved-chain-break`
(`/tmp/jcal3-probes`, shared tables symlinked), one run per shape per checker:

```text
chain-unresolved            stock == delivered (qualified wording stays):
  entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'

null-from-chain             stock (hedged) -> delivered (definite):
  stock:     ... possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
  delivered: provenance chain break; expected from_holder 'mira', got None

tick-relevant-unresolved    stock (hedged) -> delivered (definite):
  stock:     ...tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'f3-dup' is not uniquely resolvable (...); from_holder 'f3-dup' is not uniquely resolvable (...); provenance tick 1 must be greater than previous tick 3
  delivered: ...tick: provenance tick 1 must be greater than previous tick 3

unrelated-duplicate-tick    stock == delivered (definite control):
  ...tick: provenance tick 1 must be greater than previous tick 3
```

All four runs exit 1 with empty stderr; exit and non-tick violation lines are
unchanged, confirming the fixes are wording-only on these shapes. This
independently verifies both halves of the C1 repair ("null chains and tick
findings definite; genuinely unresolved non-null holder breaks qualified") against
the delivered checker.

### Integration fidelity

Reconstructed all 24 files added by `F1-fixtures.patch` from patch text and
byte-compared to the delivered tree: `24/24 byte-equal, mismatches: NONE`. No
integrator amendment of the fixture payload.

## Findings & named debt

1. **All seat checks pass; no blocking finding.** Freeze hash matches exactly;
   the C1 census claim ("0 changed + 4 new of 164, 0 exit changes") is confirmed
   by direct replay; the four READMEs are byte-exact against delivered behavior
   and against the claimed before-state; the r89 sets are byte- and tuple-identical
   to baseline; new definite/qualified wordings verified on the delivered checker.
2. **Named debt (doc-parity, registry):** `corpus/fixtures/README.md` has no
   Round 90 section — the last round section is Round 89 (line ~1014) — so the
   four new fixtures are not registered in the fixture index the way r89's were.
   This does not violate any C1 claim (the "canonical census manifest" is the
   census path set, and the FN-2 pair is present in the 160-row baseline), but it
   is a documentation-parity residue for closure/r91.
3. **Named debt (durable coverage of the repaired wordings):** the census delta is
   zero, i.e. no durable fixture exercises either repaired branch
   (`null-from-chain` definite wording, tick definite wording); their verification
   rests on scratch receipts (B3/X2/X3/C9 and this seat's matrix). The new
   fixtures pin the FN-1 raw-present variants and the ≥3-cause record, exactly as
   claimed. If r91 wants regression-visible definite wordings, two durable
   fixtures (one per shape) are the obvious carry.
4. **Info (stale artifacts, not defects):** W2's scorecard proposal carries
   pre-integration figures (`X1_unchanged=160 changed=0`; X1 patch hash
   `c3573aa0…`; "no delivered post-fix comparison available"). The delivered
   artifacts say otherwise: `X1-tuple-delta.json` = 159/1,
   `X1-c1.patch` = `6d37eccf…`, and the delivered census = 0 changed of 160 (+4
   new). Closure prose should use the delivered numbers and
   `followup/JCAL3-census-after.json`. `Q1-r90-debt.json` is likewise a
   pre-integration audit (its C1 rows read "open"); expected, superseded by
   closure.
5. **Info (baseline independence):** B1 and B2 manifests are byte-identical, so
   their agreement adds no independent entropy beyond process separation; the
   delivered census was compared field-wise against both regardless.

Seat-level verdict for the calibration axis: **improved** — the hedged shapes are
repaired and verified against the delivered checker, the census claim holds
exactly, READMEs are exact, r89 regression is clean, and no harmed or traded
measurement was found. Bounded by named debts 2 and 3. (Axis verdict is L1's;
this is this seat's evidence-based judgment.)

## Handoff

- Files written by this seat: `followup/JCAL3.md` (this report),
  `followup/JCAL3-census-after.json` (164 delivered tuples + delta summary,
  SHA-256 `1ca18e34c3449e6767c3ddf26bc2746cdf767552246569f8874cd923f4ae6b31`).
  No commits, no pushes, no other repo writes.
- Reproduction: freeze — `git show e97613c:corpus/fixtures/check_bible.py` +
  `git apply` of the X2/X3 patches and hash comparison; census — run
  `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` for every fixture
  dir and compare `(exit, stdout_sha256, violation_count)` against
  `patches/B1-tuples.json`; READMEs — extract the ```text block and byte-compare
  to the delivered checker's stdout; r89 — `git ls-tree -r` equality plus the
  tuple table above; probes — rebuild `/tmp/jcal3-probes` per C9's construction
  and run both checkers.
- Open questions for L1: whether the fixtures-README Round 90 registration
  (debt 2) and durable fixtures for the two definite wordings (debt 3) enter the
  r91 plan; whether closure replaces W2's stale figures with the delivered census
  artifact (debt 4). No blocking issue prevents an improved calibration verdict.
