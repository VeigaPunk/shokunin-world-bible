# V35 — adjudicator (round 97, FINAL) — DRAFT v2

Seat: V35 adjudicator. Baseline r96 closure f3e09f9; HEAD 2393934.
Mandate: poll until the other 63 reports exist, read them all, reconcile conflicts, admit ONLY if C1/C2/C3 verify and no axis harmed; per-axis table; conditions; never re-roll harms.

## Delivered revision (frozen; my hashes)
- map_obligations.py 86b52949…; map-obligations-contract.json 2142b991… (25 cases, dual_pointer)
- dependency_freeze.py b06275f3…; dependency-freeze-contract.json 27273be2… (16 cases, path-bound pins)
- tools README 6278e59b…; r96 map e851f068…; check_bible ff9fd2aa…; support_check 55a5eb27…
- r97 fixture: README d9387b7d…, map 49d4834e…, timeline 73063a86…, sources 438fb513…, fictional-excerpts 8ba491cb…, entities 026af0bc…, relations c279254b…, contradictions 37517e5f…, inspiration-note 58f5390e…, source-excerpt b5edc2fd…
- corpus/knowledge/r97-acknowledgment-scope-note.md 5e3b4225…

## C1 (my runs)
- 25/25 pinned; dual_pointer PASS exit=1
- drop dual_pointer → exit 2; drop schema_drift → exit 2; baseline r96 tool 23/24 PASS (my run)
- neutralize emission → SELF-TEST FAIL dual_pointer exit=0 findings=none → exit 2
- battery r88/r93/r94/r95/r96/r97 PASS; r87/r89 exit 2; frozen r93 PASS

## C2 (my runs)
- --freeze out-of-scope → SCOPE-REFUSED exit 2, pins unchanged
- foreign same-named copy → PATH-MISMATCH exit 2; real path PASS
- tamper at pinned path → DIGEST-MISMATCH naming timeline.json (ea0225f9→2d5f5dd6)
- self-test 16/16 (no TMPDIR needed); chain 4/4 clean; r96 pin revision 60dba0c2→2393934, content d422a9b3 unchanged
- V12 FAIL (recorded, not re-rolled): "pin pins the post-repair map digest" FALSE — pin covers 5 JSON files only; grep e851f068 in contract → 0 (my run); R3 self-recorded; LOG wording ("pin refresh") holds.
- V46 FAIL (recorded, not re-rolled): tick-13 edge drop not caught as BR-01 because r97 unpinned (UNPINNED-FIXTURE exit 2 on intact+mutated); catch reproduces with an explicit in-mirror pin (REDUCTION-DETECTED 4/5, exit 1); other gates green either way. Declaration claims chain 4/4 (r88/r94/r95/r96) — holds.

## C3 (my runs + seats)
- check_bible CLEAN; support 17/17+19/19+15/15; map_obligations 17/17; census 171/37/134/421
- 5 copies byte-identical; timeline/sources prefix-equal; excerpts byte-prefix (2588→3410)
- J17 span 44-53 anchor line 48; repair exactly 2 lines; r96 receipts identical pre/post

## Other
- r94/r95/r88 fixtures zero diff; knowledge only +r97 note; no lane strays; parent tree clean
- Doc-parity closure list (V26 items 1-11 + V39 P1-P5): tools README C2 half missing; SKILL.md:87/89/100; corpus/README:37/38; fixtures/README census 170; C9 watch row 6 due
- R6 note receipt pins stale-vs-delivered (V25)
- Bounds: r97 unpinned; check_bible blind spots (V20/V29); support_check blind spots (V52); V31 canonical-dialect; V11 D1/D2; BR-05; repo-root self-test scratch (V32 D1/D6); /tmp inode exhaustion host condition
- V51 observation (relation-bound sentence); V18 colon cosmetic (pre-existing)
- Seat-level FAILs: V12, V46 (both brief-stricter-than-declaration)
- Verdict seats: V29 depth improved-bounded; V30 coverage PASS bounded; V31 calibration improved-bounded; V32 operability improved-bounded; V33 freshness unchanged; V34 adjacency PASS; V54 depth AGREE; V55 coverage PASS

## Per-axis
calibration improved (bounded); depth improved (bounded); coverage improved (bounded); operability improved (bounded); freshness unchanged/not harmed; adjacency not harmed.

## Verdict
ADMIT (conditional) with conditions C-1..C-6.
