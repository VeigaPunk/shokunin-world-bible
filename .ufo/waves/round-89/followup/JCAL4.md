# JCAL4 — Calibration judge #4: wording / overclaim audit (round 89)

Seat mission: audit the r89 cause strings on the delivered tree — combined-summary join
(`'; '` between causes; overclaim when a cause is speculative?), the FN-2 qualification
clause (`possible` wording), the FN-1 raw-presence phrasing (accurate for schema-rejected
rows? for raw-absent?), qualifier presence on all disclosure lines, voice consistency —
against `.ufo/waves/round-89/patches/E1-r89-wording.md`. Deliver `followup/JCAL4.md` and
`followup/JCAL4-wording.json`.

Judged tree: `1b09f3f` — `git rev-parse HEAD` →
`1b09f3ff8016b26a2259e086f673d0112f4f54e5`; `sha256sum corpus/fixtures/check_bible.py` →
`e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556` (435 lines).
`git status --porcelain` at judging time: ` M l0-questions.md` (K1's authorised one-line
L0 append, uncommitted — not this seat's write) and `?? .ufo/waves/round-89/followup/`.
All scratch, probe fixtures and captures are under `/tmp/lore-r89-JCAL4/`; the only repo
writes are this seat's two `followup/` artifacts. No commit, no push, no sibling-repo
access.

## Work performed

- Captured the complete stdout of all 160 delivered fixture directories with the delivered
  checker into `/tmp/lore-r89-JCAL4/out/` and ran census greps over that corpus (66
  disclosure lines, 21 distinct first-stop cause strings, 11 chain-break lines, 4 tick
  lines, 1 identity-clause line).
- Byte-level conformance check of every delivered cause template against the authoritative
  wording spec `patches/E1-r89-wording.md` (spec lines 15, 26, 40–43).
- Built 16 scratch probes under `/tmp/lore-r89-JCAL4/probes/` for states no durable
  fixture covers — raw-present-but-schema-rejected holder, raw-present-but-schema-rejected
  source, null `from_holder` on a later record, first-record identity detail, observed-side
  identity detail, same unresolved id on both sides (with and without tick inversion),
  semicolon-bearing holder id, three simultaneous causes, shape-invalid record with a fully
  absent holder, shape-invalid record with an indexed duplicate holder, two different
  unresolved ids, non-string raw id, sources table missing — and ran every probe against
  **both** the delivered checker and the baseline checker
  (`git show 51b286b:corpus/fixtures/check_bible.py > /tmp/lore-r89-JCAL4/base-check_bible.py`)
  to obtain before → after receipts.
- Reproduced E1's follow-up drift items DR-5 and DR-6 independently and confirmed DR-7 by
  static reading; read and cited the sibling follow-up reports JCAL1, JCAL3, V2 and E1.
- Two 60 s wait-checks per the wave protocol (`2026-10-17T04:29:55-03:00 → 04:30:55` and
  `04:30:55 → 04:31:55`, `/tmp/lore-r89-JCAL4/wait.txt`). Nothing was outstanding: the
  wave's work commit `1b09f3f` was already present at seat start, so both checks returned
  no new dependency and the seat proceeded on the delivered tree. No gap is owed.

## Before → after measurements

### 1. Template conformance to the E1 wording spec (delivered tree)

Command (exact fragments checked against the spec file):

```sh
python3 - <<'EOF'
import pathlib
spec = pathlib.Path('.ufo/waves/round-89/patches/E1-r89-wording.md').read_text().splitlines()
for n in (15, 26, 40, 41, 42, 43): print(n, spec[n-1])
EOF
```

Observed: `:15` `'; '.join(causes)`; `:26` the FN-2 clause
`input-structural finding, not sourced-canon; possible provenance chain break, not a
definite identity mismatch: expected from_holder 'dup' is not uniquely resolvable (2 raw
entity rows carry this id, but only 1 is in the resolved index); got 'mira'`; `:40–43` the
four FN-1 forms. Delivered code emits all six verbatim:

- `check_bible.py:316` `first_stop = ('; '.join(record_stop_causes) or 'malformed record', record_label)` — spec `:15`.
- `check_bible.py:342/348` — spec `:26`, byte-identical for the covered case (see §2).
- `check_bible.py:272-273 / :285-286` render spec `:40`/`:41` exactly via the `raw_presence`
  ternary; `:306-307` render spec `:42`/`:43` exactly.

So FN-1's four forms, FN-2's clause and the combined join are **verbatim conformant** to
the spec; there is no drift between the spec and the delivered code (E1-drift's items are
doc/README drift, not code drift).

### 2. Qualifier presence and the absence of speculative causes in summaries

Census over the 160 delivered directories (`/tmp/lore-r89-JCAL4/out/`):

```text
line kind                              total   missing "input-structural finding, not sourced-canon"
remain unassessed disclosure            66      0
identity clause (not uniquely resolvable) 1     0
provenance chain break                  11      7   (the 7 are the definite unqualified form, unchanged from r88)
tick inversion                           4      3   (the 3 are the definite unqualified form, unchanged from r88)
first-stop clauses containing a hedge    0      -   ("possible" or "not uniquely resolvable")
"present in raw" occurrences             0      -   (FN-1's raw-present half still fixtureless)
```

Same checks over all 16 probes: `hedged_in_first_stop=0` and `unqualified_identity_lines=0`
for every probe. The hedged clauses are emitted only on the comparison path, which is gated
by `first_stop is None` (`check_bible.py:320`), while every `record_stop_causes` append site
is a definite predicate reached under `valid = False` (`:260, :264, :268, :273, :297, :301,
:307, :310`, plus `:297` via `record_holder_ambiguous`) — so **a speculative cause cannot
enter a combined summary** by construction, and measurement agrees on all 160 dirs and all
probes.

### 3. Before → after receipts for every branch my audit touches

Baseline command form: `python3 /tmp/lore-r89-JCAL4/base-check_bible.py <probe-dir>`;
delivered: `python3 corpus/fixtures/check_bible.py <probe-dir>`. Full outputs are in
`/tmp/lore-r89-JCAL4/probe-outputs.txt`; the load-bearing lines:

| probe (state) | baseline `51b286b` | delivered `1b09f3f` |
|---|---|---|
| p1 — raw entity row present but schema-rejected, referenced as `to_holder` | `entities[3].provenance[1].to_holder: dangling entity 'ghost'` + `first stop: dangling holder to_holder 'ghost'` | local line **unchanged** `… dangling entity 'ghost'`; first stop `holder reference to_holder 'ghost' present in raw entities but absent from the resolved index` |
| p2 — raw source row present but schema-rejected, cited from a record | `…source_id: unknown in-world source 'ghost-src'` + `first stop: unknown source 'ghost-src'` | local line **unchanged** `… unknown in-world source 'ghost-src'`; first stop `source reference 'ghost-src' present in raw sources but absent from the resolved index` |
| p3 — later record with `from_holder: null` | definite `provenance chain break; expected from_holder 'j4-holder', got None` | `input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'j4-holder'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)` |
| p4 — first record with a non-null raw-duplicated `from_holder` | `provenance chain break; first record must have from_holder null` | `input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); first record must have from_holder null` |
| p5 — arriving `from_holder` raw-duplicated, expected unique | `provenance chain break; expected from_holder 'j4-holder', got 'dup'` | `… possible provenance chain break, not a definite identity mismatch: expected from_holder 'j4-holder'; got 'dup'; from_holder 'dup' is not uniquely resolvable (2 raw … only 1 …)` |
| p6b — same unresolved id both sides + tick inversion | `entities[4].provenance[1].tick: provenance tick 0 must be greater than previous tick 0` | `… tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'dup' is not uniquely resolvable (2 raw … only 1 …); from_holder 'dup' is not uniquely resolvable (2 raw … only 1 …); provenance tick 0 must be greater than previous tick 0` |
| p8 — three simultaneous causes + one source defect | `first stop: malformed record (invalid tick)` (later causes masked) | `first stop: malformed record (invalid tick); holder reference to_holder 'missing-holder' absent from raw entities and absent from the resolved index; source reference 'missing-src' absent from raw sources and absent from the resolved index` — all three, validation order, none dropped |
| p11 — shape-invalid record whose `to_holder` is entirely absent from raw | `first stop: malformed record (unexpected field set)` | **identical** — the dangling condition is never evaluated on this branch (`:223-248` `continue`s) |
| p12 — shape-invalid record with an indexed duplicate holder | `first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'dup'` | identical — same `'; '` join as the valid-key branch |
| p13 — different unresolved id on each side | `provenance chain break; expected from_holder 'dup', got 'dup2'` | both sides named with their own clause (no duplication) |
| p7 — holder id containing `'; '` plus a second cause | `first stop: malformed record (invalid from_holder)` (no second cause) | `first stop: malformed record (invalid from_holder); holder reference to_holder 'a; b' absent from raw entities and absent from the resolved index` — `!r` keeps the id quoted, so the separator stays parseable |
| p14 — raw entity row whose `id` is the integer `5`, referenced as `'5'` | `first stop: dangling holder to_holder '5'` | `first stop: holder reference to_holder '5' absent from raw entities and absent from the resolved index` (the raw counts are string-id keyed, `:72-76`) |
| p10 — sources table missing | `first stop: source table unavailable` | identical — raw-absence wording is never used for an unloaded table |

## Findings & named debt

**F1 (headline) — the FN-1 fix is half-applied: the adjacent local diagnostic line still
claims absence for an id that is present in raw.** On p1 the delivered tree prints, in one
output, `entities[3].provenance[1].to_holder: dangling entity 'ghost'` (`:270`, `:283`) and
`first stop: holder reference to_holder 'ghost' present in raw entities but absent from the
resolved index`. The E1 FN-1 rule is explicit — "do not use `dangling` or `unknown` as
though an ID were absent from the input when it is present there" (`E1-r89-wording.md:37`,
over-claim bound at `:48`)
— and the local sink line (`unknown in-world source`, `:113`) is the same class. This is a
pre-existing imprecision at the local line, but r89 turned it into an *internal
contradiction* between two lines of the same output (baseline was consistently wrong in both
places; delivered is right in one and wrong in the other). It is latent on the delivered
tree only because no fixture reaches the raw-present half (`present in raw` = 0 occurrences
across 160 dirs — JCAL3 Debt 3). E1-drift lists the local diagnostics as "clean on
inspection"; that is true against the stale contract doc, but not against the FN-1 rule.
Fix in r90: align the local wording (or state the local-vs-cause split explicitly, which is
E1's DR-1/DR-2 `proposed_action`).

**F2 — a partial clause and a complete clause carry the same `first stop:` label.** After
C1, the valid-key branch guarantees a complete latching-cause list (p8 receipt), while the
early-exit branches do not and cannot: p11 shows a shape-invalid record whose `to_holder` is
absent from raw entirely, reported as only `malformed record (unexpected field set)` — the
dangling condition is never evaluated. Both produce a `'; '`-joined clause in the same
envelope. The checker never says "complete" anywhere, so nothing in the output is false; the
risk is reader inference, and it is exactly the risk E1 recorded
(`E1-r89-wording.md:19`). Mitigation is documentation-level (E1's proposed doc update states
the bound); no code change is required.

**F3 — FN-2 wording in the three sub-branches no durable fixture covers.**

- **(a) Regression vs baseline — null `from_holder` (p3, reproduces E1 DR-5).** The delivered
  line invents an unresolved-identity claim about `None` (`0 raw entity rows carry this id,
  but only 0 is in the resolved index`) and downgrades the baseline's definite `provenance
  chain break; expected from_holder 'j4-holder', got None` to a "possible" one. The hedge
  premise in the spec (`:23`) is "a referenced holder ID occurs more than once in raw entity
  rows"; for `None` it does not hold, so the qualification is over-applied and the definite
  finding is under-claimed. One-line fix: `holder_identity_detail` returns `None` for
  `holder_id is None`.
- **(b) Category mix — first record with a raw-duplicated `from_holder` (p4, `:348`).** The
  clause opens `possible provenance chain break …` and ends `first record must have
  from_holder null`; there is no predecessor link to break, and the definite rule is stated
  after the hedge. Information content is an improvement over the baseline, the sentence
  frames it as the wrong finding class.
- **(c) Separator/voice overload — observed-side detail and same-id-both-sides (p5, p6b,
  reproduces DR-6).** Within one finding, `'; '` now separates the expected/observed split,
  the identity sub-clauses, and (in p6b) a duplicated pair with two labels for the same id.
  p6b's clause repeats the same 2-raw/1-indexed explanation twice.
- Pluralisation latency: the template `{n} raw entity rows carry this id, but only {m} is in
  the resolved index` is only ever reached with `(2,1)` in a correct state; `(0,0)` becomes
  reachable solely through F3(a) (`0 raw entity rows … only 0 is`). `(1,0)`/`(2,2)` are
  unreachable: the index is a subset of raw rows, and any record that reaches the comparison
  path requires an indexed-unique holder on both sides. Static reasoning (path enumeration),
  not a runtime probe.

**F4 — no overclaim in the delivered fixture-covered surface (recorded so r90 does not
re-chase it).** All six delivered forms match the spec verbatim; the `'; '` join is
unambiguous (no delivered cause contains a `';'`; ids are `!r`-quoted, p7); no hedged cause
can enter a combined summary (measured 0 on 160 dirs + 16 probes, and structurally gated);
every disclosure line and every identity-clause line carries `input-structural finding, not
sourced-canon` (0 gaps); the FN-2 control pair still splits correctly (JCAL3 verified, V2
verified the delivered checker is byte-identical to the X1 patch on `51b286b`).

**F5 — brief-vs-tree phrase mismatch (judged against the spec, not the brief).** The seat
brief's FN-1 phrase `absent from the raw table and resolved index` occurs nowhere in the
tree; the only occurrences of that string are the sibling reports quoting the brief
(`followup/H2.md:223`, `followup/JCAL1.md:210-211`, `JCAL1-delta.json`). The delivered text
is `absent from raw entities and absent from the resolved index` (holders) /
`absent from raw sources and absent from the resolved index` (sources), matching
`E1-r89-wording.md:40-43`. Accuracy verdict: correct for schema-rejected rows (p1/p2,
"present in raw … but absent from the resolved index") and correct for genuinely raw-absent
ids (the delivered `r89-f2-*` fixtures); an unloaded table is reported as `source table
unavailable` (p10) and cannot yield a raw-absence claim for entities because no provenance
record survives a failed entities load — a structural guarantee, not an explicit guard, so
it is a latent refactor risk worth one comment in r90.

**Debt owed to r90 (all cheap, none blocking):** F1 local-line wording or the doc's
local-vs-cause split; F3(a) one-line `holder_id is None` guard + a durable fixture; F3(b)
rephrase the first-record clause; F3(c) dedupe; F5 explicit `entities_available` guard
comment. Cross-round debt restated from siblings and still open: FN-1's raw-present half has
no durable fixture (JCAL3 Debt 3), FN-2 is invisible to the 149-dir manifest (JCAL1), three
`r89-f2-*` READMEs declare pre-FN-1 wording (JCAL3 Debt 1 / E1 DR-8), the contract doc is
stale (E1 DR-1…DR-4, DR-9…DR-12), and `corpus/fixtures/README.md` has no Round 89 section
(JCAL3 Debt 5 / E1 DR-13).

## Verdict recommendation

**Calibration (wording sub-axis): improved (bounded)** — on everything the delivered
fixtures pin, and across the whole 149-directory baseline population, every wording change
is an accuracy gain: FN-1 now distinguishes raw absence from schema-rejected presence, the
valid-key summary is complete and in validation order (p8), and the FN-2 hedge is correct
where the spec's premise holds, with a control that stays unqualified. One state got worse
than the baseline — a later record with `from_holder: null` (F3a, p3), where a definite
finding was downgraded and a nonsense identity clause was added — and one wording rule is
only half-applied (F1). Because the round's judging rule says a trade anywhere is not an
improvement, this recommendation carries that bound explicitly: **record the axis as
improved (bounded), and treat F3(a)'s one-line fix plus F1's local-line alignment as
conditions of a clean "improved" in the r89 closure record; absent that fix, the honest
reading is improved-with-a-named-regression.** No fabricated or inferred receipts: every
statement above is either a replay on `1b09f3f`, a baseline replay on a probe input, or a
path-enumeration argument that is labelled as such.

## Handoff

- `lore-shokunin/.ufo/waves/round-89/followup/JCAL4.md` — this report.
- `lore-shokunin/.ufo/waves/round-89/followup/JCAL4-wording.json` — machine-readable
  wording audit: spec-conformance map, qualifier census, the 16-probe before → after matrix,
  and the findings with receipts.
- Scratch evidence retained: `/tmp/lore-r89-JCAL4/out/` (160 delivered stdout captures),
  `/tmp/lore-r89-JCAL4/probes/` + `probes.py` (16 probe fixtures), `probe-outputs.txt`,
  `base-check_bible.py` (baseline `51b286b` checker), `wait.txt` (two timestamped 60 s
  wait-checks, nothing outstanding).
- Verified on the delivered tree only: no probe fixture, doc, README or checker file was
  modified in the repo; the only repo writes are the two `followup/` artifacts above. No
  commit, no push, no sibling-repo writes.
- Left undone deliberately: no fix applied for F1/F3 (checker and docs are integration
  scope); C2/C3 wording surfaces beyond this seat's brief were not re-audited (covered by
  JCOV*/JDEP*/E1).
- Nothing left unverified within this seat's scope; no blockers.
