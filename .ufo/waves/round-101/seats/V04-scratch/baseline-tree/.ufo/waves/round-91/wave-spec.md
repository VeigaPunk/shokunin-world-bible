# Round-91 wave spec

Regimen: luna round 5 of 12. Baseline HEAD: `a7c6a17` (r90 closure; tree clean).
Phase 1: WORK wave, 32 seats, `openai-codex/gpt-6-luna-max`.
Phase 2: FOLLOW-UP on `alibaba-token-plan/deepseek-v4.1-flash`
(operator-directed 2026-10-17: "use alibaba for the deepseek v4.1 flash
swarm"; fallback order alibaba-tp-1 → alibaba-tp-2 → alibaba-tp-3 →
opencode-go → zai-glm; hyper remains exhausted).
Machine-readable companion: `wave-spec.json` (roster-as-data, r90-Q2-P2).

Wait protocol: committed helper pattern (r90-Q2-P1): poll every 60 s to a
20-minute deadline INSIDE one tool call, timestamp each check, trap a terminal
line; at deadline work with what exists and record the gap.
Scratch protocol (r90-Q2-P3): file-frugal; path-limited archives; `df -i`
pre-flight; sweep before finishing.

## Declared claims (L1, adopted from r90 SCORECARD planned)

- **C1 calibration** (lowest-axis obligation continues): (i) durable
  DISCRIMINATING fixtures pin the r90-repaired shapes — a null-chain fixture
  whose output differs between the e97613c checker and the delivered checker
  (`got None` definite), and a tick-under-genuinely-unresolved-holder fixture
  whose tick line differs (integer-only definite) while its chain-break stays
  qualified — so a silent revert of either gate fails the census; (ii) the
  shipped-checker hash + the C9 falsification trigger are pinned in a tracked
  artifact (corpus/knowledge/r91-c9-watch.md); (iii) the C9 watch names the
  exact probe that would falsify the ruling.
- **C2 coverage**: the support command is hardened against the two silent
  failure vectors the r90 follow-up found — (i) an expected-inventory
  assertion (map-declared row counts vs parsed rows; a header rename or
  dropped section cannot PASS silently); (ii) distinct-anchor/row reporting
  (duplicate-row inflation and unreferenced-row mode flips surface as
  WARN/FAIL); (iii) the r87 receipt wording splits JSON-fact count from
  editorial rows (the rows-not-facts correction lands in the map/README).
- **C3 depth**: JDEP2's three prospective edges get decided governance —
  (i) R8's failed-gate disposition (the element's state when the two-part R2
  gate fails) + withhold-scope precedence (element-level vs detail-level);
  (ii) R9's reprint boundary (a bibliographic tie that is itself a later
  reprint) + a reliability criterion for the tie; (iii) R10's source_id
  namespace scoping (a shared source_id across clusters is a namespace
  collision, not identity) — each as a decided clarification with owner,
  trigger, and worked example.

## Roster (32)

Recon: B1 census captain (+ before-state receipts), B2 independent census,
B3 repaired-shape before-state reproducer (e97613c checker outputs), S1
fixture-design scout + C9-watch design.
C1: X1 fixture implementer (2 discriminating fixtures + READMEs with
per-checker expected outputs), F2 alternative fixture author, C5
discrimination critic (both checkers), C8 verifier, C6 separability critic,
E1 wording panel, CB-prep drift scout (expected NEGATIVE: r91 does not touch
the checker).
C2: M1 hardening implementer, M2 independent hardening alternative, M4
attacker (all three r90 vectors must now fail/warn), M3 map/README wording
fix, S2 hardening spec scout, C7 discipline critic, K1 connector, V1
script-freeze verifier.
C3: D1 edge-decisions #1, D2 #2, T1 verifier, R1 reviewer, J3 register
re-check, E2 wording.
Record: W1 clerk (landing record), W2 scribe, Q1 debt auditor + r92
planner, SE1 sentinel, Q2 methodologist (did P1/P2/P3 land?).

Integration rule unchanged: patches in phase 1; parent integrates; phase 2
verifies the delivered tree (freeze-then-verify).

## Landing record

Snapshot cutoff: 2026-10-17T07:36:41-03:00 (poll 20 of 20; 15 of 30 named seats had at least one artifact, 26 seat artifacts).
Lane/attempt: `lane_requested=openai-codex/gpt-6-luna-max` (phase-1 declaration); `lane_served=unknown` (not exposed to W1); `attempt=1` (this clerk invocation only); `failover=unknown` (no per-seat dispatch record).

The spec declares 32 seats but names 30. Paths are repository-relative; mtimes are local time (`-0300`). This inventory excludes W1's report and patch, which are post-cutoff clerk outputs.

| seat | delivered artifact | mtime (`-0300`) |
|---|---|---|
| — | `.ufo/waves/round-91/wave-spec.md` | 2026-10-17 07:14:10.105027066 -0300 |
| B1 | `.ufo/waves/round-91/B1.md` | 2026-10-17 07:25:55.654691060 -0300 |
| B1 | `.ufo/waves/round-91/patches/B1-tuples.json` | 2026-10-17 07:23:14.015777417 -0300 |
| B2 | `.ufo/waves/round-91/B2.md` | 2026-10-17 07:29:51.189254354 -0300 |
| B2 | `.ufo/waves/round-91/patches/B2-tuples.json` | 2026-10-17 07:16:37.997147349 -0300 |
| B3 | `.ufo/waves/round-91/B3.md` | 2026-10-17 07:21:34.366760901 -0300 |
| B3 | `.ufo/waves/round-91/patches/B3-before-state.json` | 2026-10-17 07:17:56.825402142 -0300 |
| D2 | `.ufo/waves/round-91/D2.md` | 2026-10-17 07:34:10.048259861 -0300 |
| D2 | `.ufo/waves/round-91/patches/D2-edges.patch` | 2026-10-17 07:24:57.347157576 -0300 |
| E1 | `.ufo/waves/round-91/E1.md` | 2026-10-17 07:36:06.016946721 -0300 |
| E1 | `.ufo/waves/round-91/patches/E1-r91-wording.md` | 2026-10-17 07:32:46.902528932 -0300 |
| F2 | `.ufo/waves/round-91/F2.md` | 2026-10-17 07:34:16.067241929 -0300 |
| F2 | `.ufo/waves/round-91/patches/F2-fixtures.patch` | 2026-10-17 07:27:15.623129938 -0300 |
| J3 | `.ufo/waves/round-91/J3.md` | 2026-10-17 07:31:54.324721715 -0300 |
| M1 | `.ufo/waves/round-91/patches/M1-hardening.patch` | 2026-10-17 07:35:45.753996802 -0300 |
| M2 | `.ufo/waves/round-91/patches/M2-hardening-alt.patch` | 2026-10-17 07:27:08.149389552 -0300 |
| M3 | `.ufo/waves/round-91/M3.md` | 2026-10-17 07:28:48.789575028 -0300 |
| M3 | `.ufo/waves/round-91/patches/M3-mapwording.patch` | 2026-10-17 07:26:38.782377871 -0300 |
| S1 | `.ufo/waves/round-91/S1.md` | 2026-10-17 07:26:28.049453434 -0300 |
| S1 | `.ufo/waves/round-91/patches/S1-r91-c9-watch.patch` | 2026-10-17 07:25:49.122740779 -0300 |
| S2 | `.ufo/waves/round-91/S2.md` | 2026-10-17 07:26:46.853322061 -0300 |
| SE1 | `.ufo/waves/round-91/SE1.md` | 2026-10-17 07:26:11.343574141 -0300 |
| W2 | `.ufo/waves/round-91/W2.md` | 2026-10-17 07:35:46.759994272 -0300 |
| W2 | `.ufo/waves/round-91/patches/W2-log-r91.proposal.md` | 2026-10-17 07:31:03.633926267 -0300 |
| W2 | `.ufo/waves/round-91/patches/W2-report-r91.skeleton.md` | 2026-10-17 07:31:13.413885283 -0300 |
| W2 | `.ufo/waves/round-91/patches/W2-scorecard-r91.proposal.md` | 2026-10-17 07:30:50.270983483 -0300 |
| X1 | `.ufo/waves/round-91/patches/X1-fixtures.patch` | 2026-10-17 07:33:29.144387094 -0300 |

No artifact was present at cutoff for C5, C8, C6, CB-prep, M4, C7, K1, V1, D1, T1, R1, E2, W1, Q1, or Q2. Two of the 32 declared seats have no identity in the prose roster; their identities and delivery states are not inferred.

`wave-spec.json` was absent at cutoff. The new JSON companion therefore preserves the 32-declared / 30-enumerated / 15-delivered counts, all 30 named roster rows, per-seat target and lane fields, and the 26 cutoff artifact paths/mtimes. It does not claim an observed served lane or dispatch attempt where no dispatch record exists. No amendments or failovers were declared in the phase-1 input.

The one-call poll covered 2026-10-17T07:16:41-03:00 through 2026-10-17T07:36:41-03:00 (21 checks, 60 s apart) and emitted `TERMINAL deadline_reached=true` at the cutoff. Full timestamped stdout is preserved at `/home/vgpnk/.kimi-code/sessions/wd_shokunin_8c4a99c6228c/session_812e7ffb-509b-48a4-8999-22134315ef0e/agents/agent-313/tasks/bash-xlwtspv7/output.log`.

### Post-cutoff arrivals observed at 2026-10-17T07:42:47-03:00 (not part of the landing snapshot)

| seat | late artifact | current mtime (`-0300`) |
|---|---|---|
| C5 | `.ufo/waves/round-91/C5.md` | 2026-10-17 07:39:43.219509605 -0300 |
| C5 | `.ufo/waves/round-91/patches/C5-discrimination.json` | 2026-10-17 07:39:43.219509605 -0300 |
| C8 | `.ufo/waves/round-91/C8.md` | 2026-10-17 07:42:41.901255031 -0300 |
| — | `.ufo/waves/round-91/CB1.md` | 2026-10-17 07:39:57.790485826 -0300 |
| D1 | `.ufo/waves/round-91/D1.md` | 2026-10-17 07:40:13.719460521 -0300 |
| D1 | `.ufo/waves/round-91/patches/D1-edges.patch` | 2026-10-17 07:37:59.867696814 -0300 |
| E2 | `.ufo/waves/round-91/patches/E2-wording.md` | 2026-10-17 07:42:00.375307549 -0300 |
| K1 | `.ufo/waves/round-91/K1.md` | 2026-10-17 07:41:34.465342211 -0300 |
| M4 | `.ufo/waves/round-91/M4.md` | 2026-10-17 07:42:22.986278506 -0300 |
| T1 | `.ufo/waves/round-91/T1.md` | 2026-10-17 07:40:40.738419113 -0300 |
| X1 | `.ufo/waves/round-91/X1.md` | 2026-10-17 07:40:48.500407567 -0300 |

`CB1.md` is not identified with roster ID `CB-prep`; E2 has a wording patch but no E2.md report in this sample. The X1 report arrived after cutoff; the X1 patch above was present at cutoff.

### Cutoff-path rewrites observed at 2026-10-17T07:42:47-03:00

| cutoff artifact | current mtime (`-0300`) |
|---|---|
| `.ufo/waves/round-91/B3.md` | 2026-10-17 07:41:31.701345998 -0300 |
| `.ufo/waves/round-91/D2.md` | 2026-10-17 07:42:38.965258627 -0300 |
| `.ufo/waves/round-91/patches/D2-edges.patch` | 2026-10-17 07:42:26.474274123 -0300 |
| `.ufo/waves/round-91/E1.md` | 2026-10-17 07:42:06.370299738 -0300 |
| `.ufo/waves/round-91/patches/E1-r91-wording.md` | 2026-10-17 07:39:24.656540805 -0300 |
| `.ufo/waves/round-91/F2.md` | 2026-10-17 07:37:36.707743631 -0300 |

These later current mtimes do not replace the poll-20 values in the cutoff table; the original byte state is not hash-stamped.

### Additional post-cutoff sample at 2026-10-17T07:49:20-03:00 (not part of the landing snapshot)

This sample records new late artifacts and changes since the 07:42:47 observation. The cutoff inventory and its counts remain unchanged.

| seat | artifact | current mtime (`-0300`) | observation |
|---|---|---|---|
| C5 | `.ufo/waves/round-91/C5.md` | 2026-10-17 07:44:45.218118503 -0300 | late artifact updated since prior sample |
| C5 | `.ufo/waves/round-91/patches/C5-discrimination.json` | 2026-10-17 07:44:45.218118503 -0300 | late artifact updated since prior sample |
| C6 | `.ufo/waves/round-91/C6.md` | 2026-10-17 07:47:47.510959589 -0300 | additional named-seat late artifact |
| C7 | `.ufo/waves/round-91/C7.md` | 2026-10-17 07:48:14.984939168 -0300 | additional named-seat late artifact |
| C8 | `.ufo/waves/round-91/C8.md` | 2026-10-17 07:42:55.775238273 -0300 | late artifact updated since prior sample |
| D1 | `.ufo/waves/round-91/D1.md` | 2026-10-17 07:42:56.953236867 -0300 | late artifact updated since prior sample |
| E2 | `.ufo/waves/round-91/E2.md` | 2026-10-17 07:49:00.168907266 -0300 | additional late report |
| E2 | `.ufo/waves/round-91/patches/E2-wording.md` | 2026-10-17 07:47:29.925973084 -0300 | late artifact updated since prior sample |
| M1 | `.ufo/waves/round-91/patches/M1-hardening.patch` | 2026-10-17 07:47:39.626965601 -0300 | cutoff artifact rewritten after cutoff |
| M2 | `.ufo/waves/round-91/patches/M2-hardening-alt.patch` | 2026-10-17 07:48:46.933916396 -0300 | cutoff artifact rewritten after cutoff |
| Q1 | `.ufo/waves/round-91/Q1.md` | 2026-10-17 07:48:16.213938273 -0300 | additional named-seat late artifact |
| Q1 | `.ufo/waves/round-91/patches/Q1-r91-debt.json` | 2026-10-17 07:48:16.213938273 -0300 | additional named-seat late artifact |
| Q1 | `.ufo/waves/round-91/patches/Q1-r92-proposal.md` | 2026-10-17 07:48:00.237950035 -0300 | additional named-seat late artifact |
| W2 | `.ufo/waves/round-91/W2.md` | 2026-10-17 07:47:42.888963103 -0300 | cutoff artifact rewritten after cutoff |

