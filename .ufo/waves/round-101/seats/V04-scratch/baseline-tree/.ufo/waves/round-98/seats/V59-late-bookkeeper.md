# V59 — late-bookkeeper (round 98)

**Seat:** V59 `late-bookkeeper` — failsafe/presence seat of the round-98 single wave (64 seats:
S1–S5 producers + V01–V59 verifiers). Scope per seat spec: poll until the round's artifacts and
seat reports land (20 s cadence, 40 tries, bounded); record **which seats were still missing at my
cutoff**; record **whether any mutual-wait pair exists**; **reconcile against the V36 and V58
receipts** when they appear. This seat also re-ran the round's C1/C2/C3 spot-checks against the
delivered revision with baseline controls where the artifacts landed inside its window — every such
check is labeled below, and none of them is an admission verdict.

LEAF seat: no nested agents, no commits, no pushes, no network, no corpus edits. Writes by this
seat: this report (absolute path) and `.ufo/waves/round-98/seats/V59-scratch/` only
(`poll.sh`, `poll.log`, `waitgraph.py`, `census.py`, `verify_all.sh`, `legacy_pin.sh`,
`edge_demo.sh`, `base/` baseline bytes). All commands run from
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`; session cwd is the parent repo, so
every path used here is lane-anchored or absolute (r94-F01 class).

**Environment pin:** lane HEAD `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` ("lore r97: close round —
SCORECARD admitted section"), baseline `9a3d648` (declared; `git show 9a3d648:<path>` used for all
pre-round bytes). Uncommitted tree at open and through the watch (r97's own closure commit is
HEAD, so `git diff 9a3d648` includes committed r97-closure bytes — stray detection uses
`git status --porcelain`, not the baseline diff):

```
 M LOG.md
 M corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
 M corpus/knowledge/r95-aftermath-scope-note.md
 M corpus/knowledge/r96-response-scope-note.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? .ufo/waves/round-98/
?? corpus/fixtures/r98-clerk-filing/
?? corpus/knowledge/r98-clerk-scope-note.md
```

Every changed path above is inside a declared producer byte-ownership set (S1 tools pair, S2
`tools/README.md`, S3 r95 map repair + r98 fixture, S4 r98 `README.md`/`claim-excerpt-map.md`,
S5 r98 note + two addenda) or is L1's `LOG.md` declaration. **No stray writes beyond ownership;
no parent-tree strays** (`find /home/vgpnk/Projects/shokunin/.ufo -path '*round-98*' -name '*.md'`
→ empty; the parent has no `corpus/` tree).

## 1. Method (commands actually run)

- Poller `V59-scratch/poll.sh` (background, 45 × 20 s): per try logs report count, missing S1–S5
  artifacts and missing S1–S5 reports to `V59-scratch/poll.log`; present-verifier list to
  `present-v.txt`.
- Wait-graph analyzer `V59-scratch/waitgraph.py` (maxdepth 2 under `seats/`, mirrors excluded):
  parses every r98 `*scratch*/*.sh`, extracts each seat's awaited seats, prints direct edges,
  direct mutual pairs, and all-reports waiters.
- Baseline byte capture into `V59-scratch/base/` from `9a3d648` (dependency_freeze.py,
  dependency-freeze-contract.json, tools/README.md, r95 map, r95/r96 notes) for diffing.
- Mirror-root probes (`mktemp -d`, copies of the delivered tool + contract + fixture) for the C1a
  self-test-mismatch demo, the C1b legacy-pin demo, and the C2 r97-edge demo, each with a
  same-mutation control against the `9a3d648` tool/contract. Delivered files were never modified.
- Census replica `V59-scratch/census.py` (same convention as r94–r97: violation lines = lines
  containing `VIOLATION`; `check_bible.py` per fixture dir), plus a null control excluding
  `r98-clerk-filing`.

## 2. Presence ledger at cutoff

Cutoff snapshot **`2026-10-17T23:41:50Z`** (my 40-try deadline fired at `23:41:46Z`,
`try=40 reports=56`; final `ls` + roster diff at `23:41:50Z`).

```
$ ls .ufo/waves/round-98/seats/*.md | wc -l          → 56
$ tail -2 V59-scratch/poll.log
try=40 t=23:41:26 reports=56 missArtifacts:[ ] missProducerReports:[ ]
try=41 t=23:41:46 reports=56 missArtifacts:[ ] missProducerReports:[ ]
```

- **Present: 56 reports including this one; all 5 producer reports (S1–S5) present.** Producer
  artifacts: all 13 polled paths present by `23:32:46Z` (`missArtifacts: [ ]`).
- **Missing at cutoff (8 seats, SELF excluded): `V20 V24 V31 V32 V36 V51 V57 V58`** (roster
  S1–S5 + V01–V59; command: roster diff over `seats/*.md` with `V59` subtracted).
- Liveness of the missing eight at cutoff (all observed, none fabricated):
  `V20` poll ended `POLL-TIMEOUT 23:41:27 reports=56` (40 tries) with no report yet;
  `V24` poll ended `POLL_END 2026-10-17 20:41:46 -0300 tries=40` with no report yet;
  `V31` poll alive (240-try all-reports condition, pid 1466958);
  `V32` poll alive (40-try fleet-file condition, pid 1469503);
  `V36` poll alive (`try=39 reports=56 producers=5 r98fix=10 know=1 freeze=MOD`, pid 1471325);
  `V51` log `count=56` at `23:41:40`; `V57` snapshot tool ran `23:40:30`; `V58` poll alive
  (`try 37 23:41:39 nonself=56 total=56`, pid 1477615).
- Landing curve (reports incl. SELF, from `poll.log`): `23:30:06=1 … 23:33:46=15, 23:35:46=24,
  23:37:46=41, 23:39:46=52, 23:41:46=56` — the classic endgame tail: the last seats are the
  all-reports/quiescence waiters plus two polls that hit their own 40-try caps without a report.

## 3. Mutual-wait analysis

Direct wait edges observed among r98 poll scripts (producer-directed edges collapsed):

- Cross-verifier **report** edges: `V43 → V19` and `V50 → V27` — both one-way and both satisfied
  when V19 and V27 landed (V19's scratch contains no poll script; neither V19 nor V27 waits back).
  `V57`'s `snap.sh` names 17 seat prefixes but reads their **scratch artifacts**, not their reports.
- All-reports waiters: `V58` (`nonself ≥ 63`, 90 × 20 s), `V31`
  (`.ufo/waves/round-98/scratch/V31/poll.sh`: `n ≥ 63`, 240 × 20 s), and `V36` (its
  producer/artifact READY condition plus a quiescence stall-escape: exit after the all-reports
  count is unchanged for 60 tries; hard cap 150 tries).
- **Direct mutual pairs (A→B ∧ B→A): none** at every sample taken (23:28–23:41Z, 9 samples). No
  two seats each block on the other's report.
- **All-reports co-wait cluster `{V31, V36, V58}`** — the r96/r97 endgame class in co-dependency
  form rather than pairwise form: each member's completion condition includes the other members'
  reports (V31 and V58 need `n ≥ 63` reports; V36 needs the count to stop changing, which cannot
  happen before V31's and V58's reports land). This is **not a deadlock**: all three carry bounded
  caps (V58 90 tries ≈ 30 min, V36 stall-escape 60 stable tries ≈ 20 min / hard cap ≈ 50 min,
  V31 240 tries ≈ 80 min), and any one landing reduces the set. The r96/r97 endgame convention
  (all-reports polls must subtract SELF) was followed by V58 (`nonself`) and V36/V31 (they count
  other seats' reports only after subtracting their own name where applicable); recorded here so
  the class is not re-learned.

## 4. Independent spot-checks on the delivered revision (with baseline controls)

All run after S1's second landing (pins) — revision in the tree as listed in the environment pin.

**C1a — `SELF-TEST-MISMATCH` exits 2 (pinned 17th case).** Tampered-expectation mirror
(`self_test.expected.clean.exit` 0 → 1) against the delivered tool vs the `9a3d648` tool:

```
delivered: SELF-TEST 16/17 / FINDING SELF-TEST-MISMATCH: cases failed: ['clean'] / RESULT ERROR / EXIT=2
baseline : SELF-TEST 15/16 / FINDING SELF-TEST-MISMATCH: cases failed: ['clean'] / RESULT FAIL  / EXIT=1
```

Shipped self-test on the delivered tree: `SELF-TEST 17/17`, `RESULT PASS`, exit 0. The 16 inherited
expectations are byte-identical to `9a3d648` case-by-case; the only added key is
`self_test_mismatch`; `exit_codes` and `scope` unchanged.

**C1b — path-less legacy pin migrated by `--freeze`.** Mirror with
`pins.r95-crossing-aftermath.fixture` removed (and, separately, set to `null`):

```
delivered, key absent : MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath / RESULT PASS / EXIT=0
delivered, key = null : MIGRATED … / FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1 / RESULT PASS / EXIT=0
baseline 9a3d648      : FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names None; … / RESULT ERROR / EXIT=2
```

Verification alone with a path-less pin still fails closed: `FINDING CONTRACT-INVALID: pin
r95-crossing-aftermath needs a repo-relative fixture path`, exit 2 — matches the contract text.
Race note: at 23:31Z the then-current in-flight tool revision migrated **silently** (no `MIGRATED`
line); the delivered revision prints it for both path-less variants. Recorded as an in-flight
observation, not a defect of the delivered bytes.

**C1c — precedence text.** `precedence` now names the exit-1 finding IDs
(`REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE`), the ordered exit-2 sequence
(`UNPINNED-FIXTURE`/`CONTRACT-INVALID` → `FIXTURE-MISSING` → `PATH-MISMATCH` →
`FILE-MISSING`/`MALFORMED-JSON`/`MALFORMED-MODEL` → `DIGEST-MISMATCH` → `INVALID-ARGUMENTS` →
`SELF-TEST-MISMATCH`, plus `--freeze`'s `SCOPE-REFUSED`) and the legacy-pin migration sentence.
Spot-checked against the tool's own emit sites; consistent.

**C2 — chain six fixtures, 6/6 clean.** Contract pins = 6 with repo-relative paths
(`r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`,
`r97-crossing-acknowledgment`, `r98-clerk-filing`); per-fixture verify on the delivered tree:

```
r88-m3-maya-cluster rc=0 PASS   r94-paired-crossing rc=0 PASS   r95-crossing-aftermath rc=0 PASS
r96-crossing-response rc=0 PASS r97-crossing-acknowledgment rc=0 PASS r98-clerk-filing rc=0 PASS
```

Pinned edge counts rise 0/2/3/4/5/6 across the chain (events 2→7). r98 digest
`59a0f4fa3d4a47e0…` matches S2's README claim; r97 digest `3c922d20a01bbd3f…` likewise.
**V46 discharge demo (independent):** scratch mirror, r97 fixture with
`acknowledgment-aru-records.depends_on` emptied → `FINDING REDUCTION-DETECTED: event
acknowledgment-aru-records lost depends_on ['response-evin-salt-court']`, `RESULT FAIL`, exit 1;
unmodified mirror copy → `RESULT PASS`, exit 0. Before the pin, the same mutation could only reach
`UNPINNED-FIXTURE` (exit 2) — the discharge is real, not vacuous.

**C3 — depth claims.** Independent counts on `corpus/fixtures/r98-clerk-filing/`:
entities **6** / relations **1** / events **7** / sources **7**; `check_bible.py` →
`CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0. The three JSON additions are
exactly `clerk-maren` (character, `first_appearance: clerk-filing-note`, one claim),
`clerk-filing-note` (source), and `clerk-filing-open` (tick 14, `entity_id clerk-maren`,
`place_id chalk-stair`, `depends_on ["acknowledgment-aru-records"]`), with the inherited arrays
byte-identical as prefixes (5→6, 6→7, 6→7). Map: 20 J-rows (17 inherited parsed-value identical
outside the namespace column + J18/J19/J20), 2 editorial rows, 22 rows total, **18 distinct
anchors** — every declared anchor resolves inside its declared line span; lines 61–62 carry
`I assert no finding.` / `I reach no verdict and reconcile nothing.` **Census (independent
replica): 172 fixture dirs / 38 clean / 134 negative / 421 violation lines; null control over the
171 pre-r98 dirs reproduces r97's 171/37/134/421 exactly** (+1 dir, +1 clean, 0 new violation
lines). **r95 repair half:** `git diff 9a3d648 -- …/r95-crossing-aftermath/claim-excerpt-map.md`
is exactly one line (the carried sentence), and the 25 data rows are byte-identical pre/post.

## 5. Reconciliation against V36 and V58 receipts

- `.ufo/waves/round-98/receipt.json` exists and is **V36's skeleton** (`state` names V36 as receipt
  seat, snapshot `2026-10-17T20:29:02-0300`, `collection.reports_present: 0`, `reports_absent` =
  all 64, `missing_candidate_paths` etc.). Re-checked at cutoff **and again at `23:44:33Z`**: still
  byte-level the round-start skeleton, not yet updated with endgame counts — V36's report and its
  final receipt pass had not landed by then.
- V58 (r97-class presence seat) was still mid-poll at every sample: `try 14 nonself=15` (23:33:58Z)
  → `try 37 nonself=56` (23:41:39Z) → `try 45 nonself=57` (23:44:19Z). Its final report/receipt had
  **not** landed when this report was written; the numbers in §2 are this seat's own count, taken
  independently of V58 (method: roster diff over `seats/*.md`, not V58's `audit.py`).
- V36 and V58 receipts could therefore not be reconciled *against* — the comparison recorded here
  is the reverse direction: my independent counts are the fallback record if V36's receipt pass or
  V58's audit is lost. Where the two disagree, trust the later of the two and the underlying `ls`.
- Post-cutoff drift (recorded, not a correction): at `23:44:33Z` and again at `23:46:46Z` the count
  was **58** and the missing set had shrunk to `V20 V31 V36 V51 V57 V58` (V24, V32 landed after the
  cutoff; V36/V58 and the receipt's endgame pass still had not landed at `23:46:46Z`).
- No seat was found fabricating presence: every landed report's header names its own seat, and the
  reports I sampled (V15, V22, S3, S4) cite pre-write baselines captured before the artifacts
  landed, consistent with their claimed poll order.

## 6. Bottom line

**PASS (failsafe presence seat)** — all 13 producer artifacts and all 5 producer reports present;
C1/C2/C3 spot-checks independently reproduced on the delivered revision with baseline controls
(17/17 self-test, MIGRATED vs `SCOPE-REFUSED`, 6/6 chain, REDUCTION-DETECTED on the r97 edge,
census 172/38/134/421 with an exact 171/37/134/421 null control); **no mutual-wait pair exists** —
the endgame took the co-wait-cluster form `{V31, V36, V58}` with bounded caps, not a deadlock;
**8 seats were still missing at my 23:41:50Z cutoff** (`V20 V24 V31 V32 V36 V51 V57 V58`, all with
observed liveness, none fabricated), and the V36/V58 receipts were not yet available to reconcile
against, so §2's independent ledger stands as the fallback record.
