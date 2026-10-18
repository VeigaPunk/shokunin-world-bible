# V18 inclusion set (prepared before S5 landed)

Criterion: a ledger item is a demonstrated gate blind spot iff (1) a concrete
mutation or omission was run, (2) at least one gate returned CLEAN / RESULT
PASS / exit 0 while the changed fact remained, and (3) the ledger characterizes
it as a blind spot, silent pass, undetectable class, or unscanned key — not a
docs, process, roster, or host item. A later ledger marking the exact class
CLOSED removes it from the gap set (historical close may still be cited by a
status row).

## Declaration-minimum rows (absence = gap)

1. emptied depends_on — r97 V37 NB-15; r98 V33 NB-05 / CO-13. V16 P5 CLEAN.
2. wrong-but-earlier edge — same ledgers. V16 P8 CLEAN.
3. deleted terminal row — same. V16 P9 CLEAN.
4. F15 support_check-silent mutants — F15 mut-b/b2, mut-a, mut-d; V47 names
   b2/a/d still silent in support_check; r98 V33 NB-05. r94 F29 has no
   separate id; BR-01 covers mut-a only.
5. dependency-wording removal (BR-01 prose half) — r94 F29 BR-01; r96 V40
   NB-07; r97 V37 CO-07 and NB-17 (JSON-only payload); r98 V33 CO-19 and
   CO-02. OPEN at r98. Row must record historical invisibility and the C1
   close.
6. consistent-regeneration — r96 V40 NB-21; r97 V37 NB-09; r98 V33 CO-09
   OPEN/accepted.
7. checker's frozen-pin status — r97 V37 NB-01 (unpinned fixture; drop not
   caught until pinned) CLOSED by r98 V33 CO-01 for the pin itself; checker
   still does not consult pins (NB-05). Status row expected.

## Still-open demonstrated classes outside the declaration parenthetical
(absence = gap against the ledgers, labeled extra-declaration)

8. canonical-dialect bare second token silent — r97 V37 NB-08; r98 V33 CO-08
   OPEN/accepted. Legacy dual_pointer closed in r96 (V40 CO-03); this
   remainder was not.
9. schema_drift scope / D2 evasion — r95 V31 NB-01 and NB-13 (probes exit 0);
   r96 V40 NB-20 UNCHANGED; r97 V37 CO-14 OPEN/accepted. Not marked CLOSED
   in r98 (dropped from the carried restatement, not closed).
10. array-positional pointer rebinding — r94 F29 BR-16; r95 V31 NB-10; r96
    V40 CO-09 UNCHANGED. Not restated in r97/r98. Borderline (mis-bind, not
    a silent miss of a checked fact). Report as borderline, not a hard gap,
    unless the table claims every calibration silent-pass.

## Not gaps

- inventory deletion class: CLOSED r96 V40 CO-01.
- D1 legacy hidden pointer: CLOSED r96 V40 CO-03.
- freeze scope guard, basename pins, digest file-naming, pin-set validation:
  CLOSED r97 V37 CO-02/03/04/05.
- r97 fixture unpinned: CLOSED r98 V33 CO-01.
- SELF-TEST-MISMATCH exit divergence: CLOSED r98 CO-16.
- BR-01 JSON-edge half: CLOSED r96 V40 CO-04 (prose half remains row 5).
- MALFORMED-MODEL unpinned (r98 CO-20): self-test coverage, not a content miss.
- contradiction/accusation/winner gate-invisibility (r96 V40 NB-12): accepted
  editorial bound, no mutation replay quoted as CLEAN. Note, not a hard gap.
- docs/process/roster/host items in all five ledgers.

Debt pointer: a citation naming a ledger item id from F29 / V31 / V40 / V37 /
V33 (BR-*, NB-*, CO-*, CR-*) or a path to one of the five debt.json files plus
an item id. A seat-report citation alone is an evidence pointer, not a debt
pointer.
