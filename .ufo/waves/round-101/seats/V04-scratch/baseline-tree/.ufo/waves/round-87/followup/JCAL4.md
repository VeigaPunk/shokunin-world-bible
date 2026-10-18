# JCAL4 — Mixed-stop caveat characterizer (C5 follow-up)

Seat: JCAL4. Wave: round-87 follow-up (world-bible lane). Fleet root `/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.
Measured tree: HEAD `2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (work-wave evidence commit), clean when measurement started.
Mission: on the delivered tree, construct the mixed case — record `k` invalid via an **unknown source** (latches comparison off, no holder ambiguity), record `k+1` has an **ambiguous holder** — record exact output, classify the per-record disclosure at `k+1` (true / misleading / false), test whether the pre-existing global notice has the same attribution property at the pre-C1 revision, and propose named debt.

Machine-generated receipts: `.ufo/waves/round-87/followup/JCAL4-replay.json` (commands, stdout, exit codes, sha256 for every run; fixture file hashes).

## Method

- Nothing in the repo was modified. The checker was invoked read-only from the lane root against scratch fixture directories under `/tmp/jcal4/fixtures/` (HARD RULE: experiments in `/tmp`).
- Delivered checker: `corpus/fixtures/check_bible.py`, md5 `e088ac108b7f1e2dda8f1630d72cc161`, sha256 `3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237` — the delivered revision.
- Pre-C1 checker: `git show 28706dc:corpus/fixtures/check_bible.py > /tmp/jcal4/check_bible_prec1.py`. `git rev-parse 03c6746~1` → `28706dc73a9b7667851fd82adb71e905ae5eb896`, i.e. the revision whose only disclosure was the global notice. `diff` between that file and the delivered checker is exactly C1's additions and nothing else (6 hunks, all inside the provenance loop; `diff … | grep -c '^[0-9]'` → `6`).
- Revision note on "HEAD~1": `git rev-parse 2b48ca7~1` → `e4708cb` (the C3 fixture commit) and `git diff --stat e4708cb 2b48ca7 -- corpus/fixtures/check_bible.py` is empty; the checker at `2b48ca7~1` has md5 `e088ac108b7f1e2dda8f1630d72cc161`, identical to the delivered one. So literal `HEAD~1` still contains C1; the "pre-existing global notice" was therefore measured at the pre-C1 baseline `28706dc` (C1's parent), which is the revision the question can actually be answered on. Both facts are recorded in the JSON.
- Fixtures are authored test scaffolding, not recovered records, canon, or evidence about custody. All four fixtures share `sources.json`, `relations.json`, `timeline.json`, `contradictions.json` and differ only in the `seal` entity's `provenance` array.

## Fixture construction

Shared entities: `mira` (character), `harbor`/`tower` (places), `seal` (item, carries `provenance`), and two rows both with id `dup` (the identity-ambiguity scaffolding). Shared sources: `archive-ledger`, `courier-log`.

| fixture | provenance array (`tick`, `from_holder`, `to_holder`, `source_id`) | purpose |
|---|---|---|
| `jcal4-mixed-stop` | `(0, null, mira, missing-source)`, `(3, mira, dup, archive-ledger)`, `(4, harbor, tower, archive-ledger)`, `(2, mira, tower, archive-ledger)` | the mixed case: `[0]` unknown source (no holder ambiguity) → latch; `[1]` ambiguous `to_holder` → holder stop; `[2]` hidden break (`harbor` ≠ previous `dup`); `[3]` decreasing tick |
| `jcal4-mixed-stop-control` | identical to mixed except `[0].source_id = courier-log` | removes the earlier latch, keeps the ambiguity — isolates the holder cause |
| `jcal4-mixed-noambiguity` | identical to mixed except `[1].to_holder = tower` | removes the ambiguity, keeps the earlier latch — isolates the unknown-source cause |
| `jcal4-earlier-stop-only` | `(0, null, mira, missing-source)`, `(3, mira, harbor, archive-ledger)`, `(4, harbor, tower, archive-ledger)` | non-holder stop with no ambiguous reference anywhere |

Per-file sha256 for every fixture is in `JCAL4-replay.json` under `fixtures`.

## Exact output

### Delivered tree `2b48ca7`

```sh
python3 corpus/fixtures/check_bible.py /tmp/jcal4/fixtures/jcal4-mixed-stop
```

```text
VIOLATION: entities[5].id: duplicate entities id 'dup'
VIOLATION: entities[3].provenance[0].source_id: unknown in-world source 'missing-source'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'dup'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[1]
VIOLATION: entities[3].provenance[3]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[1]
7 violation(s); no canon changed
```

`exit=1` (recorded by the same run; the fence above is stdout verbatim — sha256 `2d0be64509d09dd675ef388b88d9a5b24a0e2a9723c1e0761a850e186cab7252`, key `runs["delivered:jcal4-mixed-stop"]` in `JCAL4-replay.json`).

Two mechanical facts visible here that are worth stating plainly:

- The stop record `[1]` receives **two** notices: the unchanged global one plus a new per-record one that names itself as the origin (`first occurred at entities[3].provenance[1]`). Records `[2]`, `[3]` receive one each. With the stop at index `s` in an `n`-record array the tail yields `n - s + 1` unassessed lines (2 at the stop record, 1 at each later record) — one more than the number of records after the stop, and never the single line the pre-C1 contract specified. Cross-check on the delivered C1 fixture `r87-masked-break-to-ambiguous` (`s = 0`, `n = 3`): 4 unassessed lines out of 6 violations, matching `n - s + 1 = 4`.
- **No disclosure of any kind is emitted for record `[0]`**, whose unknown source is what actually latched comparison off first. The new per-record line is emitted only for records at/after a *holder*-ambiguity stop.

Control (`jcal4-mixed-stop-control`) — 6 violations, same three disclosure lines; only the `[0]` unknown-source line is absent. No-ambiguity (`jcal4-mixed-noambiguity`) and earlier-stop-only — 2 violations each (`duplicate entities id`, `unknown in-world source`), i.e. records `[1..3]` / `[1..2]` carry **no** unassessed disclosure even though their continuity/tick comparisons never ran. Verbatim stdout for all four is in the JSON.

### Pre-C1 baseline `28706dc`

```sh
python3 /tmp/jcal4/check_bible_prec1.py /tmp/jcal4/fixtures/jcal4-mixed-stop
```

```text
VIOLATION: entities[5].id: duplicate entities id 'dup'
VIOLATION: entities[3].provenance[0].source_id: unknown in-world source 'missing-source'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'dup'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
4 violation(s); no canon changed
```

`exit=1` (same run; stdout verbatim, sha256 `5145e68176235efe9debdfcf291a1dd4cd13ca116de585029725721efdd019de`, key `runs["preC1:jcal4-mixed-stop"]` in `JCAL4-replay.json`).

## Classification of the per-record disclosure at `k+1`

The delivered string, decomposed:

- `entities[3].provenance[k]: provenance continuity and tick-order comparisons unassessed` — **true**. Measured: no `chain break` and no `provenance tick` finding is emitted for `[1]`, `[2]`, or `[3]`, and assessment never resumes.
- `because ambiguous holder identity to_holder 'dup' first occurred at entities[3].provenance[1]` — the identity is real, the field is right, and the first-occurrence location is right. As a *sufficiency* claim it is also true: the ambiguous `to_holder` sets `record_holder_ambiguous` → `valid = False` → `can_check_chain = False` at `[1]` (`corpus/fixtures/check_bible.py:226-230,237-241,260-263`), which independently blocks `[1]`'s and every later comparison.
- The same clause as an **operative-cause** claim ("the reason these comparisons are unassessed") — **false in the mixed input**. `[0]`'s unknown source already set `can_check_chain = False` before `[1]` was reached, so those comparisons were unassessed before the ambiguity existed.

**Verdict: misleading — true in literal content, unsound in causal framing; not false.** It is not a fabrication and does not mislocate anything, so calling it false would overstate the defect; but a reader who takes `because` as naming the first or sole stop cause is told something the input contradicts, and the sentence is the only disclosure attached to records `[2]` and `[3]`, which are the records an editor will actually go look at.

Falsification evidence for that verdict (three independent receipts):

1. **The wording cannot distinguish the two stop causes.** `mixed` and `control` differ only in whether an earlier non-holder latch exists, yet their per-record disclosure line sets are byte-identical (sha256 `c36f239397efd0fe0684571a1e5eba9053e1d325d8b5834a3f2c86af5022fc27` both). A message that is invariant to the presence of the earlier cause is not reporting the true first cause.
2. **The ambiguity is not necessary for the non-assessment it explains.** `jcal4-mixed-noambiguity` removes the ambiguity and keeps the latch: the tail comparisons still never run, and no disclosure line appears at all (2 violations). So in the mixed input the operative cause of `[2]`'s and `[3]`'s non-assessment is the `[0]` latch, not the ambiguity.
3. **The ambiguity is sufficient, not exclusive.** `control` removes the latch and keeps the ambiguity: the tail is still unassessed. Both causes independently suffice; the disclosure names one and implies it is the reason.

## Does the pre-existing global notice have the same attribution property? Yes.

The pre-C1 global notice is

```text
entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
```

It carries the same `because` framing, and it is likewise invariant to the earlier latch: at pre-C1, `mixed` and `control` produce byte-identical global-notice line sets (sha256 `f3bea7ad3b6ebda74ec2c6a6df87ef1c59b6d3b61b9b6ecba44551df5a48a648` both). The C1 `diff` shows the global notice string as an unchanged context line; C1 added lines and changed no existing wording.

So: **carried-over semantic, not a C1 regression.** What C1 changed is scale and precision, not the attribution property — one notice per item tail became `n-1` per-record lines (so the unsound `because` is now repeated once per later record), while the new line is in one respect *more* careful than the old one: it says the ambiguity "first occurred at `[1]`" rather than saying assessment stopped there, and it names the field (`to_holder`) and origin record. The boundary knowledge file's "What the output does NOT say" cell (`corpus/knowledge/holder-assessment-boundary.md:74`) — "That ambiguity is where assessment first stopped — an earlier invalid record may have stopped it sooner" — is still satisfied *literally* by the delivered string; the gap is that the delivered string still reads as a cause claim, and that same cell was written for the global notice, before the per-record lines existed.

## Named debt proposal

**Debt 1 (primary) — "mixed-stop attribution debt".** Both the pre-C1 global notice and the C1 per-record line present the first holder ambiguity as the reason the affected comparisons are unassessed. When a non-holder invalidity (unknown or ambiguous source, malformed key set, bad tick, dangling holder — `holder-assessment-boundary.md:74` lists the class) already latched comparison off earlier, the disclosure silently omits that cause and invites the false inference "dedup the identity and the tail is assessed". Owner: whichever seat next edits the checker's provenance branch (C1 author) plus the boundary-knowledge refresh (I2). Resolution options, cheapest first:

- **(a) wording-only (recommended, smallest).** Replace the causal `because … first occurred at` with an additive/status phrasing that does not claim priority, e.g. E1 candidate 3 (`.ufo/waves/round-87/patches/E1-wording.md`): `{record_label}: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); holder id {id!r} was ambiguous at {origin}`. This also fixes a second small gap: unlike the chain-break findings (`check_bible.py:267-271`), neither the global notice nor the per-record line carries the `input-structural finding, not sourced-canon` qualifier, so a reader can take them as canon statements.
- **(b) state-tracking.** Track the first record at which `can_check_chain` became false and report it (`unassessed since {first_stop_label} ({reason}); also ambiguous holder identity … at {origin}`). This is the same mechanism C5's X3 caveat named; it resolves the mixed-stop case exactly, at the cost of new checker state and a wider tuple-delta surface.
- **(c) doc-only acceptance.** Keep the string and require `holder-assessment-boundary.md` to state explicitly that `because` names a sufficient *additional* cause and never the first or sole one, plus a fixture pinning the mixed case so the claim stays checkable.

Verification for any option: the mixed fixture's disclosure must either differ from the control's, or the documentation must bound the claim; the receipt pair is `delivered:jcal4-mixed-stop` vs `delivered:jcal4-mixed-stop-control` in `JCAL4-replay.json`. The fixture should be landed as `corpus/fixtures/r87-probe-mixed-stop/` (plus the three variants) by the seat authorized to write `corpus/fixtures/r87-probe-*/` (I1); this seat has no tracked-file write authorization.

**Debt 2 (secondary) — scope of the C1 claim.** C1's commit message says "every record at/after the stop carries an explicit disclosure". Measured: that holds only for holder-ambiguity stops. An unknown-source stop produces no per-record disclosure at all (`jcal4-earlier-stop-only`: records `[1]`, `[2]` silent; `jcal4-mixed-stop`: record `[0]`, the actual first stop cause, silent). The claim is true for the case C1 scoped it to and should be read that way in the round record; the residual observability gap for non-holder stops predates C1 and is unclosed.

**Adjacent observation (not a debt of this seat, no claim made).** The two C1 fixtures' `README.md` files say the run "does not locally disclose that later record comparisons were skipped"; against the delivered checker that is true only of the pre-C1 baseline — the delivered run emits those lines (6 violations each, reproduced here and in `I3.md`'s declared-vs-observed table). At the delivered revision, `corpus/knowledge/holder-assessment-boundary.md:73` likewise still says the notice appears "at the first ambiguous-holder record only, the single … notice", which no longer matches the delivered output (all citations to that file in this report are to the `HEAD` blob; the working tree has an uncommitted I2 refresh in flight).

**Convergence with I2 (independent).** I2's uncommitted refresh of `holder-assessment-boundary.md` already rewrites that row and records the same property — its decision-table row for "ambiguity after an earlier invalid record" now reads "the per-record disclosure names the ambiguity as cause even when an earlier invalidity had already latched the gate (`I2.md` probe `p3`)". Two seats, separate probes, same conclusion: the mixed-stop attribution is real and was found independently. So the documentation half of Debt 1 is being closed concurrently; the checker-string half remains open, and the choice among Debt 1 options (a)/(b)/(c) is the open decision.

## Bounds

- Verdicts here are bounded to the provenance-disclosure branch and the four fixtures above. I did not re-run the 138-dir census (I3 did), did not measure any axis scalar, and did not modify any repo file.
- The mixed case was exercised with an **unknown source** as the earlier latch, per the mission. The other latch causes in `holder-assessment-boundary.md:74` (malformed key set, bad tick, dangling holder) share the same `valid = False → can_check_chain = False` path at `check_bible.py:260-263`, so the finding generalizes by code inspection — that generalization is **static, not measured**; only the unknown-source case has a runtime receipt here.
- Pre-C1 evidence was produced from a `git show`-extracted copy of the checker, not from a checked-out worktree; the extracted file is byte-identical to `03c6746~1`'s blob by construction and its diff against the delivered checker is exactly C1's hunks (recorded in the JSON).

## Handoff

- Landed: `.ufo/waves/round-87/followup/JCAL4.md` and `.ufo/waves/round-87/followup/JCAL4-replay.json`. No other file written, nothing committed, nothing pushed.
- Scratch fixtures and the pre-C1 checker live under `/tmp/jcal4/` and are ephemeral; the JSON carries their file hashes and every command/output pair.
- Nothing was blocked; no seat dependency was needed.
