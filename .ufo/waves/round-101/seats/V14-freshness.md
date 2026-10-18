# V14 — freshness (2026-10-18)

Seat: V14, round 101 (28-seat single wave, `zai-coding-plan/glm-5.3-flash-low`). Axes: **freshness** — stale-pin sweep of the round's new bytes, **metadata header** on U2's knowledge entry, **C9 next-recheck state**. Scope: the delivered r101 producer bytes and freshness bookkeeping, not independent admission of C1/C2/C3 semantics. Baseline r100 closure `6f86bf2`; declaration commit `ebec6bb`; wave tree uncommitted.

**Result:** no stale pin and no stale current-count claim in any new byte; the eight-pin chain and the 19-case gate are fresh; the entry carries a complete four-line metadata header whose 30 cited paths all exist; C9's pointer correctly reads "Next re-check: r101" with the watch file baseline-equal and the live discriminator held. U2's producer report was ABSENT at the bounded poll and at a bounded extension; the entry itself was delivered, edited once mid-verification, and byte-stable at `370c4481…` thereafter — all entry checks quoted below were (re-)run on those final bytes. One carried navigation staleness outside producer ownership is recorded as follow-up.

## Ownership, waiting, scratch

Every command ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. V14 wrote only this report and its declared scratch: `.ufo/waves/round-101/seats/.v14-scratch/{audit.py,audit-output.txt}`. No corpus/tool/contract/watch file touched; no nested agents, network, commits, pushes, or live `--freeze` operation. Absolute resolution was asserted inside the poll script (`assert root == Path('/home/vgpnk/Projects/shokunin/lore-shokunin')`).

Bounded poll (artifacts AND producer reports; 20 s × 40):

```sh
python3 -u - <<'PY'   # glob seats/U1*.md + U2*.md non-empty; artifacts = entry + 4 U1 files; pin state via contract JSON
```

Observed terminal lines — all five artifacts present from poll 18, U1's report `U1-chain-eight.md` from poll 22, U2 never:

```text
2026-10-18T03:20:30+00:00 poll 18 reports {'U1': [], 'U2': []} missing [] pins 8:[...]
2026-10-18T03:21:50+00:00 poll 22 reports {'U1': ['U1-chain-eight.md'], 'U2': []} missing [] pins 8:[...]
2026-10-18T03:27:50+00:00 poll 40 reports {'U1': ['U1-chain-eight.md'], 'U2': []} missing [] pins 8:[...]
ABSENT bounded poll exhausted
```

Bounded stall-escape (recorded, not fatal): one extension, 30 s × 20, for U2's report or entry-byte stability:

```text
2026-10-18T03:29:40+00:00 ext 1 U2 [] entry 370c44812de3 stable-since-last False
2026-10-18T03:30:10+00:00 ext 2 U2 [] entry 370c44812de3 stable-since-last True
EXT_DONE entry-stable
```

U2's report: **ABSENT** at both bounded windows. The entry bytes were nonetheless delivered and are verified below; no plan was treated as implementation.

## Stale-pin sweep of the new bytes

Working tree vs baseline `6f86bf2` — exactly the four U1-owned files modified plus U2's untracked entry (`git status --porcelain`: `M SKILL.md`, `M corpus/tools/README.md`, `M corpus/tools/dependency-freeze-contract.json`, `M corpus/tools/dependency_freeze.py`, plus the new entry; `corpus/README.md`, `corpus/fixtures/README.md`, `corpus/knowledge/r91-c9-watch.md` baseline-equal):

```text
CHANGED corpus/tools/dependency_freeze.py                 60a78bc394409172…
CHANGED corpus/tools/dependency-freeze-contract.json      b8fc63c3500d626d…
CHANGED corpus/tools/README.md                            6d17bf0792123dc5…
CHANGED SKILL.md                                          040444511f10ac27…
CHANGED corpus/knowledge/r101-r10-register-first-entry.md 370c44812de349fa…
```

(The entry's digest was `c8edb94fc534b30e…` at my first audit pass ~00:18, `370c4481…` at the final pass — U2 edited once mid-round; header and receipt checks were re-run on the final bytes. The final audit's token sweep found **zero** 64-hex digest tokens and **zero** count-claims in the entry's 122 lines.)

**Digest-token sweep** (every 64-hex token in the five new/changed byte sets, resolved against a 1086-file canonical digest map of `corpus/` + root docs, scratch/live excluded): every token classifies as (a) a pin per-file payload digest (re-verified in the payload recompute below), (b) a pin aggregate `content_sha256` (re-verified against live tool output below), or (c) carried-historical text — the contract `provenance_note` (`:953`) and the tools README Round-96-era gate transcripts (`:312`, `:322`), all present in the baseline bytes. **No NEW-not-current digest token in any new byte; no stale pin identified.**

**Pin integrity:** 8 pins (`r100-docket-review` added; none removed); all 7 inherited pins **field-identical** to baseline, including their historical revision `337f0fa52b02…`; the writer-managed top-level `revision` refresh `b5fe4729…` → `ebec6bbdeb1d9…` is the disclosed C1 exception, quoted in `corpus/tools/README.md:447`. Per-pin payload recompute over all 80 declared files: `PIN_PAYLOAD_MISMATCHES []`.

**Live chain (read-only verify, delivered bytes):** `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>` for all eight — `CHAIN_CLEAN 8/8`, every run `RESULT PASS` exit 0, and each printed `DIGEST` equals its pin's `content_sha256` (`AGG_MATCH 8/8`), e.g. `r100-docket-review` → `77debadf5c0f6e2c…` matching the new pin, and the seven inherited digests exactly their Round-99/Round-100 values. U1's independent receipts in `U1-chain-eight.md` agree digest-for-digest with these runs.

**Self-test (C3 freshness):** contract `self_test.expected` 18 → 19; added case only `repointed_edge` = `{"exit": 1, "finding_ids": ["ADDITION-DETECTED", "REDUCTION-DETECTED"], "forbid_traceback": true}`; no removed or value-changed inherited case. Live:

```text
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE repointed_edge: exit=1 expected=1 findings=['ADDITION-DETECTED', 'REDUCTION-DETECTED'] ok
SELF-TEST 19/19
RESULT PASS
exit=0
```

Exactly the claimed class: one run, both findings, exit 1.

**Count-claim scan** (`corpus/tools/README.md`, `SKILL.md`, entry; patterns for 18/19-cases, six/seven/eight-fixture, 6/6, 7/7, five-JSON): all 28 README + 4 SKILL hits are dated history inside superseded addenda or the new dated supersessions — the current values live only in the new Round-101 addendum (`README.md:423-461`: "The current chain is eight fixtures", "Persisted self-test: 19 cases, `repointed_edge`", `# SELF-TEST 19/19 / RESULT PASS, exit 0`) and `SKILL.md:98,:103` ("19 cases (… r101 added `repointed_edge` …)", "dated supersession (2026-10-18, round 101)"). No current-facing stale count in new bytes.

**Carried navigation staleness — follow-up, not a new-byte harm:** `corpus/README.md:42` (baseline-equal, outside r101 producer ownership) still describes the r100-era state — chain "r88-m3 → r94 → r95 → r96 → r97 → r98 → r99", "18-case persisted self-test", "`r100-docket-review` … outside the pins" — one round behind the delivered bytes. Same class as V19's r100 finding; refresh belongs to the authorized integrator on the next navigation touch. `corpus/fixtures/README.md` (baseline-equal) ends at the r100 closure census 174/40/134/421, which stays accurate — r101 adds no fixture.

## Entry metadata header

All four convention lines present at `corpus/knowledge/r101-r10-register-first-entry.md:1-4`:

```text
1 source: `corpus/fixtures/r94-paired-crossing/{README.md,entities.json,relations.json,…}`; … `LOG.md` (r93 closure R10 negative case; round-101 declaration C2)
2 verified-at: 2026-10-18T00:18-03:00 — read every cited local record this pass from the lane root; … confirmed `corpus/knowledge/cross-cluster-contradictions.md` does not exist. No external URL was fetched. …
3 recheck: before integrating any crossing-arc claim, and whenever a cited fixture, note, decision-table row, or the byte-identity chain changes; …
4 citation-convention: in the record table, bare `file.json#/pointer` references resolve inside the full fixture path named in the same row; …
```

Brace-expanding the `source:` line: **30/30 cited file paths exist**. `corpus/knowledge/cross-cluster-contradictions.md` is absent — **by requirement, not staleness**: the entry itself records the register destination "remains uncreated (verified absent this pass)" per the r88 appendix ("the register's first real entry awaits a genuine conflict", `r88-sourced-inspiration-decision-table.md:97`, which resolves). `verified-at` is current-dated (2026-10-18); `recheck:` names concrete re-derivation triggers.

Entry receipts independently spot-verified read-only this pass (fixture facts, valid regardless of U2's mid-round edit):

- `relations.json` byte-identity across all seven arc snapshots: `True`, sha256 `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9`.
- Excerpt prefix chain: `r95.startswith(r94)` True; `r96.startswith(r95)` True.
- `contradictions.json == []` in both compared clusters: True/True. Register absent: True.
- Claim pointers parse exactly as recorded: `r95 timeline.json#/3` = `aftermath-missing-evin` (tick 11, aru, chalk-stair, `depends_on ["paired-crossing-decision"]`, source `aru-aftermath-note`); `r96 timeline.json#/4` = `response-evin-salt-court` (tick 12, evin, salt-court, `["aftermath-missing-evin"]`, `evin-response-note`).
- Line cites resolve: `LOG.md:2656-2658` (r93 R10 negative case), r88 table `:26` / `:93-94` / `:97` / `:99-100`, `r89-cross-cluster-contradiction.md:5`.

## C9 next-recheck state

`corpus/knowledge/r91-c9-watch.md` is baseline-equal; its rows end at re-check 9 (r100 closure) with **"Next re-check: r101"** (`:351`); no r101 row exists yet — correct mid-round state; the tenth re-check is owed at r101 closure by the authorized integrator (same closure-bookkeeping pattern V19 recorded at r100). Runtime state fresh this pass:

```text
$ python3 corpus/tools/discriminate_check.py
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
exit=0
$ python3 corpus/tools/discriminate_check.py --checker e97613c   # control
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
exit=2   (expected negative control)
```

Live checker pin reproduced: `sha256(corpus/fixtures/check_bible.py)` = `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.

## Bounds

Freshness judgment on the delivered bytes: **not harmed; improved where the round touched** — dated supersessions carry the eight-fixture/19-case current state, and the entry adds a properly headered, absence-preserving record. Not claimed here: C1/C2/C3 semantic admission (verifier/adjudicator seats), the blind-spot table row-2 edit (correctly not edited — outside producer ownership; the dated closure record lives in the README addendum and SKILL supersession), any U2 report content (ABSENT). Open follow-ups recorded: U2's seat report; C9 re-check 10 at closure; `corpus/README.md:42` navigation refresh.

PASS — new bytes are stale-pin-free with 8/8 chain, 19/19 self-test, and aggregate digests verified live; the entry's metadata header is complete with 30/30 existing cites; C9's next-recheck state is correctly `r101` with the discriminator held — with U2's report ABSENT at the bounded poll and the carried `corpus/README.md:42` staleness recorded for authorized follow-up.
