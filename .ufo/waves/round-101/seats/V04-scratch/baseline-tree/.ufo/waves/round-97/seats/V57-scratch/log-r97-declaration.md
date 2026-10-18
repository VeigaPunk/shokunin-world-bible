## Round 97 — declaration before dispatch (2026-10-17)

Operator 100-round regimen round 3 of 6. Baseline = r96 closure `f3e09f9`.
One batched AgentSwarm, 64 seats on `opencode-go/deepseek-v4.1-flash`: 6
producer seats (exclusive byte-ownership) + 58 verifier/judge seats on the
poll-wait protocol (20 s cadence, 40 tries; ABSENT, never verify a plan).
Seat reports exclusive under `.ufo/waves/round-97/seats/` (absolute paths —
the session cwd is the parent repo; the r94-F01 stray-write class). Scores
remain unmeasured. Owned axis set: depth, coverage, calibration;
operability/freshness/adjacency judged as witnessed.

**C1 — calibration:** pin the r96-carried calibration residuals in
`map_obligations`. (a) Add a persisted self-test case pinning `dual_pointer`
(contract 24→25); (b) tighten the contract loader — any pinned case missing
from the contract must FAIL the self-test (today 23/24 still passes:
dropping either r96-added pin stays green); (c) demonstrate the pin is
load-bearing: neutralizing the dual_pointer emission fails the self-test.
Non-regression: the full r87–r97 battery, frozen-r93 replay, r87/r89
fail-closed, 0/1/2 contract unchanged.

**C2 — coverage (tool hardening):** close the r96-carried `dependency_freeze`
hazards. (a) Scope guard: `--freeze` accepts only `corpus/fixtures/**`
targets (integration-time operation, now enforced); (b) path binding: pins
record the fixture's repo-relative path and verify compares the invoked
path — a byte-identical same-named copy at a foreign path exits 2
`PATH-MISMATCH` (today it verifies identically); (c) `DIGEST-MISMATCH` names
the changed file; (d) self-test grows 14→16 cases pinning the new classes.
After R4's cosmetic repair, the r96 fixture is re-frozen THROUGH the guarded
`--freeze` path (pin refresh), demonstrating the guard end-to-end; chain
verifies 4/4 clean at closure.

**C3 — depth:** third beat of the crossing arc, unresolved preserved. New
fixture `corpus/fixtures/r97-crossing-acknowledgment/` — a preserving copy of
`r96-crossing-response` plus one authored acknowledgment note
(`aru-acknowledgment-note`) and one tick-13 event
(`acknowledgment-aru-records`, actor `aru`, place `chalk-stair`,
`depends_on: ["response-evin-salt-court"]`) recording that Aru received
Evin's response and that both accounts stand; no resolution, no accusation,
no reconciliation claim. Before: 5/1/5, 5 sources at r96. After: 5/1/6,
6 sources, 17 map obligations (16 inherited rows unchanged + 1 new event
row; no new claims/entities/relations), `check_bible` CLEAN, inherited rows
parsed-value identical, census 170→171. Also (same claim, repair half): fix
the two r96-carried cosmetic map blemishes (8-cell delimiter row; the stale
"new relation" sentence) in `r96-crossing-response/claim-excerpt-map.md` —
pointers/anchors/spans/modes untouched — then re-freeze r96 under C2; r96's
`support_check` and `map_obligations` receipts must be unchanged by the
repair.

**Admission rule:** admit iff C1, C2, C3 each verify on the delivered
revision and no axis is harmed; per-axis verdicts, no scalars; harmed or
unprovable claims reported as such. Same-lane rule. r98 does not start on an
unclosed r97. Producer byte-ownership: R1 `corpus/tools/map_obligations.py`;
R2 `corpus/tools/map-obligations-contract.json` + `corpus/tools/README.md`;
R3 `corpus/tools/dependency_freeze.py` +
`corpus/tools/dependency-freeze-contract.json`; R4
`corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` (cosmetic repair
only) + `corpus/fixtures/r97-crossing-acknowledgment/` JSON tables +
`fictional-excerpts.md`; R5 `corpus/fixtures/r97-crossing-acknowledgment/README.md`
+ `claim-excerpt-map.md`; R6 `corpus/knowledge/r97-acknowledgment-scope-note.md`.
Everything else is read-only except seat reports.
