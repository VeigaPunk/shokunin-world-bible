# JCAL5 — Calibration judge #5 (method-varied census, third reproduction of the 4+11 delta)

Seat mission: `git archive` of `1b09f3f`, `python3 -I`, shuffled seed 8901, an independently
regenerated baseline, a third reproduction of the 4 changed + 11 new delta, and a determinism
check. Deliver `followup/JCAL5.md` + `followup/JCAL5-delta.json`.

Judged tree: `1b09f3ff8016b26a2259e086f673d0112f4f54e5` (work commit; baseline
`51b286b5a1e503e6e6ace1f8da0bd606a3c10d94`). Judgement inputs were `git archive` extractions
under `/tmp` — the working tree was never used as a checker input. Repo writes are limited to
this seat's two `followup/` artifacts; sibling repos untouched; no commit/push.

## Work performed

- Extracted both commits: `git archive 1b09f3f | tar -x -C /tmp/lore-r89-JCAL5`,
  `git archive 51b286b | tar -x -C /tmp/lore-r89-JCAL5-base`. Checker hashes:
  delivered `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`,
  baseline `dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911`.
- Wrote my own census harness (`/tmp/lore-r89-JCAL5/census.py`), deliberately varied on three
  axes versus the earlier seats: **shuffled** traversal (`random.Random(seed)` over the direct
  children of `corpus/fixtures/`, seeds 8901 and 8902 — verified to produce different orders),
  the census harness itself run under `python3 -I` with `python3 -I` children, and a **baseline
  regenerated from the archive** rather than trusted from `B1-tuples.json`.
- Scope rule: every direct child of `corpus/fixtures/` holding at least one of
  `contradictions.json`, `entities.json`, `relations.json`, `sources.json`, `timeline.json`.
  Command template per directory (cwd = archive root):
  `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<dir>`.
- Reproduced the baseline, then diffed delivered-vs-baseline tuples
  (`exit`, `stdout_sha256`, `violation_count`), classified every changed line, and ran
  determinism, invocation-mode, invocation-form and implementation cross-checks.
- Cross-checked per-directory receipts against two sibling seats' independently produced maps
  (JCAL1, H2 — both scratch trees still present) and against a pure-shell re-census of my own.
- Spot-checked the C2/C3 deliverables that appear in this seat's artifacts (they are not this
  seat's axis, but nothing goes into `JCAL5-delta.json` unmeasured): re-ran all 14 r87-cluster
  anchor greps from `patches/S2-fact-map.json`, checked the four delivered excerpt files, the
  ETCSL `external-only` ledger marker, the R8/R9/R10 row presence, and the R9/R10 demo
  artifacts.

## Before → after measurements

**1. Baseline replay (`51b286b`).**

```text
python3 -I /tmp/lore-r89-JCAL5/census.py /tmp/lore-r89-JCAL5-base 8901 /tmp/lore-r89-JCAL5/JCAL5-base-8901.json
root=/tmp/lore-r89-JCAL5-base seed=8901 dirs=149 exits={0: 31, 1: 118} violations=367 skipped=0 map_sha256=0dca740a7a772ed268d7862e42471c8e5a82b40145bc46a56b2823a4ccf0ded9
```

Replay versus the round's reference artifact:

```text
B1-vs-replay: keys_equal=True b1_keys=149 replay_keys=149 mismatches=0 []
B1 file sha256=9a54d1e04e60b88f31019fb20ac3c9e424dbfd4cdbb30469fcf67eb2d101d7f0
```

The baseline reference is sound: 149 keys, zero differing rows, and the B1 file hash matches the
one declared in `patches/B1.md`.

**2. Delivered census (`1b09f3f`).**

```text
python3 -I /tmp/lore-r89-JCAL5/census.py /tmp/lore-r89-JCAL5 8901 /tmp/lore-r89-JCAL5/JCAL5-head-8901-run1.json
root=/tmp/lore-r89-JCAL5 seed=8901 dirs=160 exits={0: 32, 1: 128} violations=399 skipped=0 map_sha256=ba292360b7a094eda25822dfa39600d52b448e8664a2188ea40d004242dfee14
```

Scope filter is a no-op this round: `skipped=0` (all 160 directories qualify). Non-empty stderr
occurred for 0 of 160 runs.

**3. Delta — the claim reproduces a third time.**

```text
python3 -I /tmp/lore-r89-JCAL5/delta.py JCAL5-head-8901-run1.json JCAL5-base-8901.json <repo>/.ufo/waves/round-89/patches/B1-tuples.json
delivered=160 baseline=149 added=11 removed=0 common=149
changed_tuples=4 unchanged_tuples=145
exit_status_changes=[]
violation_count_changes=[]
violations baseline=367 delivered=399 growth=32 new_dirs_violations=32 net_from_common=0
```

So: **4 changed + 11 new of 160 dirs, 0 exit changes** — exactly as claimed. Stronger
properties also hold: no shared directory changed its violation count, its exit status, or its
stderr; and the entire +32 finding growth is attributable to the 11 new directories
(4+3+3+3+4+4+4+4+1+2+0 = 32), with the 4 changed directories contributing a net of zero.

The 4 changed directories and their tuples (fields that changed: `stdout_sha256` only):

| directory | exit b→a | violations b→a | stdout sha (before → after) |
|---|---|---|---|
| `corpus/fixtures/r87-probe-multi-invalid` | 1→1 | 5→5 | `e73bb6fe…` → `254cc781…` |
| `corpus/fixtures/r87-probe-record-and-chain` | 1→1 | 46→46 | `0394cd33…` → `1e32d8ea…` |
| `corpus/fixtures/r88-mixed-stop` | 1→1 | 6→6 | `403a1c1b…` → `7179e0cc…` |
| `corpus/fixtures/r88-nonholder-stop` | 1→1 | 4→4 | `8a0756c3…` → `b5ff4b29…` |

**4. Every changed line classified, mechanically.**

```text
changed_line_buckets {'combined-summary': 2, 'FN-1 wording': 10, 'OTHER': 0}
```

Two combined-summary lines (`r87-probe-multi-invalid`: the ambiguous-holder first stop now also
names the second latching cause, `… from_holder 'vault'; source reference 'ghost-source' absent
from raw sources and absent from the resolved index …`) and ten FN-1 wording lines
(`unknown source '<id>'` → `source reference '<id>' absent from raw sources and absent from the
resolved index`). Zero `OTHER`, zero footer, zero new/removed findings.

**5. Stripped-clause invariance — the changes are confined to disclosure text.**

For each changed directory I removed the `; first stop: …` clause from every line and compared
the remaining text (order-sensitive) and the line counts:

```text
r87-probe-multi-invalid           left_parts_identical=True  lines 6→6   changed first stops 2
r87-probe-record-and-chain        left_parts_identical=True  lines 47→47 changed first stops 4
r88-mixed-stop                    left_parts_identical=True  lines 7→7   changed first stops 3
r88-nonholder-stop                left_parts_identical=True  lines 5→5   changed first stops 3
```

The finding set, ordering, footers and CLEAN line are untouched; only the named cause moved.

**6. Determinism.**

```text
run1 (seed 8901)      map_sha256 = ba292360b7a094eda25822dfa39600d52b448e8664a2188ea40d004242dfee14
run2 (seed 8901)      map_sha256 = ba292360b7a094eda25822dfa39600d52b448e8664a2188ea40d004242dfee14
run3 (seed 8902)      map_sha256 = ba292360b7a094eda25822dfa39600d52b448e8664a2188ea40d004242dfee14
plain python3 (no -I) map_sha256 = ba292360b7a094eda25822dfa39600d52b448e8664a2188ea40d004242dfee14
seeds 8901 vs 8902 gave different traversal orders: True
```

The tuple map is traversal-order independent, isolation-flag independent, and byte-reproducible.

**7. Implementation cross-check (independent of Python hashing).** A pure-shell census (`for`
loop over the fixture directories, `sha256sum` of each captured stdout) reproduced all 160
per-directory `(exit, stdout_sha256)` pairs with **0 mismatches** against my Python receipts.

**8. Cross-seat agreement at per-directory granularity.**

```text
vs /tmp/lore-r89-JCAL1/head-tuples.json : 160/160 keys, 0 mismatches (and base: 149/149, 0)
vs /tmp/H2/H2-tuples.json               : 160/160 keys, 0 mismatches on exit/stdout_sha256/violation_count
```

(An apparent 160-row disagreement with H2 under raw dict equality is only its extra
`stderr_len` field; field-wise the maps are identical.) Three independent censuses — JCAL1,
H2, JCAL5 — now agree on every per-directory receipt at `1b09f3f`.

**9. Invocation-form variance — new observation from varying the method.**

Re-running the same census with (a) an absolute fixture path, and (b) `cwd=corpus/fixtures`
with a bare directory name, changes the stdout of **5 of 160 directories**:

```text
corpus/fixtures/r5-missing-file
corpus/fixtures/r62-missing
corpus/fixtures/r67-claim-source-unavailable-control
corpus/fixtures/r67-claim-source-unavailable-empty
corpus/fixtures/r67-claim-source-unavailable-whitespace
  -VIOLATION: contradictions.json: cannot load JSON: [Errno 2] ... 'corpus/fixtures/r5-missing-file/contradictions.json'
  +VIOLATION: contradictions.json: cannot load JSON: [Errno 2] ... '/tmp/lore-r89-JCAL5/corpus/fixtures/r5-missing-file/contradictions.json'
```

Only the embedded path differs; exit status and violation counts are identical for all five.
The baseline/delivered delta and all arithmetic in this report are unaffected (canonical
relative-path form from the archive root). The caveat matters for reproduction:
`stdout_sha256` receipts for this missing-file family are form-sensitive, so a future judge
using absolute paths would see five spurious mismatches.

**10. Branch and wording evidence (spot receipts for the calibration claim).** The eight
cause-branch fixtures — seven single-cause plus `r89-c1-multi-cause-valid` — all exist and name
their cause as the first stop, e.g.:

```text
r89-c1-invalid-tick            first stop: malformed record (invalid tick)
r89-c1-invalid-from-holder     first stop: malformed record (invalid from_holder)
r89-c1-invalid-to-holder       first stop: malformed record (invalid to_holder)
r89-c1-malformed-source-id     first stop: malformed record (invalid source_id)
r89-f2-dangling-from           first stop: holder reference from_holder 'r89-f2-missing-from' absent from raw entities and absent from the resolved index
r89-f2-dangling-to             first stop: holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index
r89-f2-invalid-source-id       first stop: source reference 'r89-f2-unknown-source' absent from raw sources and absent from the resolved index
r89-c1-multi-cause-valid       first stop: malformed record (invalid tick); ambiguous holder identity to_holder 'r89-c1-multi-cause-valid-ambiguous-holder'
```

I confirmed by reading `check_bible.py:255-325` that the combined summary is produced on the
**valid-key** path (`first_stop = ('; '.join(record_stop_causes) …)`) — i.e. the delivered
fixture exercises the branch C1 claimed to add, not the older shape-invalid branch. That
record (`entities[2].provenance[0]`, keys `from_holder/source_id/tick/to_holder`) carries
exactly the two latching defects it discloses; there is no third dropped cause.

FN-2 receipts (my captured outputs):

```text
r89-fn2-unresolved-chain-break: … possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
r89-fn2-control:                … provenance chain break; expected from_holder 'f3-dup', got 'mira'
```

FN-1 two-sided wording: `absent from raw sources` occurs 15 times, `absent from raw entities`
6 times, and `present in raw` **0 times** across all 160 delivered outputs — the raw-present
half of FN-1 (implemented at `check_bible.py:272/285/306`) has no durable fixture.

**11. Documentation parity (independent read, corroborates JCAL1).**
`corpus/fixtures/README.md` has 0 occurrences of `r89` (the 11 new fixtures are undocumented
there); `corpus/knowledge/holder-assessment-boundary.md` was last touched by `51b286b` and is
untouched by `1b09f3f`, still opening with CB1's `PROPOSAL — not applied` banner and still
documenting pre-r89 causes (`unknown source {id!r}` at :156, :224, and pasted r88 output at
:338-341). Its row at :169 ("Only the shape-invalid branch combines two cause phrases") is now
**contradicted by the delivered tree** — the valid-key fixture emits a combined first stop.

**12. C2/C3 spot checks (not this seat's axis, but measured here).**

```text
grep -nF -- '<anchor_phrase>' corpus/fixtures/r87-myth-cluster/<source_id>-excerpt.md   # 14 rows from patches/S2-fact-map.json
ANCHORS 14 / 14   missing_excerpt_files []
```

Locations reproduce JCOV1's table exactly (e.g. E1 `gate-witness-excerpt.md:5`, E6
`tide-bell-tally-excerpt.md:9`, T4 `dune-register-excerpt.md:8`). The cluster runs `CLEAN`,
exit 0. `reference-ledger.md:8` carries the ETCSL `external-only / text not delivered at lore`
marker. The D1 table carries R8/R9/R10 at
`corpus/knowledge/r88-sourced-inspiration-decision-table.md:22/23/24`, each with an `Owner:`
string; `corpus/knowledge/r89-cross-cluster-contradiction.md` exists; and the R9 demo fixture
`r89-inspiration-paraphrase` declares `Delivery mode: paraphrase`
(`ash-ledger-excerpt.md:3`) and runs `CLEAN`, exit 0.

**13. Note on the pre-existing partial artifact.** An untracked `followup/JCAL5-delta.json`
existed before this seat wrote, with no matching `JCAL5.md`. Its narrative blocks
(`c1_probes`, `c2_anchors`, `c3_rows`) were not measured by this seat, so they are not
presented as this seat's receipts: they are retained verbatim in the delivered JSON under
`inherited_from_pre_existing_partial_artifact`, explicitly marked as not regenerated. Every
other block in that file comes from this seat's runs. Its recorded digests are nevertheless
corroborated — under the seat's default `json.dumps(tuples, sort_keys=True)` canonicalization
my independently produced head map hashes to
`eff1fc1202a4ff0288a31294f2c9ea9dc283a6fb0e58caaa311e7b34049a57c7` and my baseline map to
`a2285a3ca4d7cd9811203b058e6d2f7366b48eb5a14bf7c0a3f8817a30703c05`, matching the two digests
that artifact recorded.

## Findings & named debt

- **Calibration verdict: improved.** On the delivered tree the C1 delta reproduces exactly under
  a third, method-varied implementation; the change is confined to disclosure text (proved by
  stripped-clause invariance); no exit, violation-count, footer, CLEAN or stderr regression
  exists on any of the 149 baseline directories; and the previously unexercised valid-key
  combined-summary branch plus six cause branches now have durable fixtures.
- **Named debt — invocation-form sensitivity (new, low severity).** `stdout_sha256` receipts for
  the five missing-file-family directories depend on the path form passed to the checker
  (absolute path or alternate cwd changes the embedded path). Exit and violation counts are
  stable. Any future census comparison should pin the invocation form, or compare
  `(exit, violation_count)` for those five.
- **Named debt — FN-1 raw-present branch unexercised** (`present in raw` = 0 across 160 outputs),
  confirming JCAL1's finding with an independent grep. The two-sided wording is durable only in
  its "absent from raw" half.
- **Named debt — FN-2 is invisible to the 149-directory manifest**: the qualification string
  occurs in exactly one delivered directory, so a regression in it is detectable only via the
  two `r89-fn2-*` fixtures.
- **Named debt — the multi-cause fixture demonstrates 2 simultaneous causes, not ≥3.** The
  claim's "names ALL simultaneous latching causes" property for three or more causes rests on
  JCAL1's scratch probe (4 causes, scratch-only), not on durable delivered evidence.
- **Named debt — the live contract doc contradicts the delivered checker.** Beyond the stale
  wording rows, `holder-assessment-boundary.md:169` asserts the shape-invalid branch is the
  only combining branch, which `r89-c1-multi-cause-valid` now falsifies. The doc is the
  checker's user-facing contract, so this is a real (bounded) harm on the calibration axis and
  should be repaired or bannered in the closure.
- **No trade found on the measured axes.** Everything the baseline emitted still emits; the
  deltas are enumerable, same-count, and stronger in accuracy.

## Handoff

- `lore-shokunin/.ufo/waves/round-89/followup/JCAL5.md` — this report.
- `lore-shokunin/.ufo/waves/round-89/followup/JCAL5-delta.json` — regenerated with this seat's
  own receipts: baseline replay, delivered census, delta, changed-line buckets, stripped-clause
  invariance, determinism digests, invocation-form variance, branch/FN-1/FN-2 receipts,
  cross-seat corroboration, doc-parity read, C2/C3 spot checks, limits. The pre-existing
  partial file's unmeasured narrative blocks are kept only under the clearly marked
  `inherited_from_pre_existing_partial_artifact` key.
- Scratch retained under `/tmp/lore-r89-JCAL5/` (`census.py`, `delta.py`, `variant.py`,
  `assemble.py`, tuple maps for head/base runs including the plain-mode and seed-8902 runs,
  `outs/` with all 160 stdout/stderr/exit captures, `shell-head.tsv`), and
  `/tmp/lore-r89-JCAL5-base/` (baseline archive).
- For the integrator: recommend (1) pinning the canonical checker invocation form in the census
  recipe, (2) repairing or bannering `corpus/knowledge/holder-assessment-boundary.md` (its
  combining-branch row is now false), (3) one durable fixture for the raw-present FN-1 half and
  for a ≥3-cause valid-key record if the claim's strong reading is to be kept.
- Untouched by this seat: `l0-questions.md` remains modified in the working tree from K1's
  authorized append; all verdicts here come from the `1b09f3f` archive, so that file is not an
  input. No commit/push performed.
