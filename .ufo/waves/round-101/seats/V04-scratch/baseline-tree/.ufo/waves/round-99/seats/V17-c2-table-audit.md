# V17 c2-table-audit — round 99

Seat: V17 (verifier, C2 blind-spot table audit). Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands from that root with `python3` unless noted. No commits, no pushes, no network. No nested agents. Live corpus bytes were not modified.

Exclusive writes: this report, and scratch under `.ufo/waves/round-99/seats/V17-scratch/` (poll log copy only).

## Axes

1. Presence — S5 artifacts and S5 producer report exist.
2. Replay fidelity — each table row's quoted command reproduces on the delivered revision.
3. Gate naming — each row names catching and non-catching gates with exits.
4. C1 dual record — the dependency-wording row records both historical invisibility and current detectability.
5. Frozen-checker boundary — that row names the boundary re-pin requirement.
6. Evidence integrity — quotes are from commands this seat ran.

Axes 2–5 were not scored. There was no delivered table to replay. This seat did not verify a plan, a scratch inventory, or another seat's draft.

## Poll-wait record

Required together: `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, and an `S5*.md` producer report under `.ufo/waves/round-99/seats/`. Cadence 20 s, 40 tries. ENDGAME: this poll waited on S5 only, not on all reports, and not on SELF.

Bounded stall-escape (recorded, not fatal): the first poller was killed by a 300 s tool cap after try 15 (`2026-10-17T22:05:17`). Tries 16–40 resumed at `2026-10-17T22:11:58` (gap 6 m 41 s, not counted as extra tries). Second poller exit code 2, stdout ended `ABSENT`. Full log: `.ufo/waves/round-99/seats/V17-scratch/poll.log` (40 lines; copy of `/tmp/v17-poll.log`).

Every try recorded `table=False note=False reports=[]`. First and last:

```
try=1 ts=2026-10-17T22:00:37 table=False note=False reports=[]
try=40 ts=2026-10-17T22:19:58 table=False note=False reports=[]
```

Post-budget confirmation (not a 41st try; still absent):

```
$ date '+%Y-%m-%dT%H:%M:%S%z'
2026-10-17T22:30:14-0300
$ ls -1 corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
ls: cannot access 'corpus/knowledge/r99-gate-blind-spot-table.md': No such file or directory
ls: cannot access 'corpus/knowledge/r99-lapse-scope-note.md': No such file or directory
$ ls -1 .ufo/waves/round-99/seats/S5*.md
ls: cannot access '.ufo/waves/round-99/seats/S5*.md': No such file or directory
$ ls -1 .ufo/waves/round-99/seats/S*.md
.ufo/waves/round-99/seats/S3-fixture-author.md
.ufo/waves/round-99/seats/S4-fixture-docs.md
$ git status --porcelain -- corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
$ git rev-parse --short HEAD
337f0fa
$ find corpus/knowledge .ufo/waves/round-99/seats -maxdepth 2 \( -name '*blind-spot*' -o -name 'S5*' -o -name 'r99-lapse*' -o -name 'r99-gate*' \) -print
.ufo/waves/round-99/seats/V53-scratch/r99-gates.txt
.ufo/waves/round-99/seats/V18-scratch/blind-spot-inventory.md
```

`git status --porcelain` on the two declared paths printed nothing. The two `find` hits are other seats' scratch, not S5 deliverables. They were not read and not audited.

Context only, not a finding against S5: at confirmation, S1 and S2 producer reports were also absent; S3 and S4 reports were present. `corpus/fixtures/r99-window-lapse/` existed (S3/S4 ownership). That fixture was not used as a stand-in for the table.

## Audit checklist (not executed)

No row was replayed. Zero gate commands were run for this audit. Nothing below is a reproduction failure; each item is unevaluable because the artifact is absent.

| Check | Result |
|---|---|
| Every row's replayed command runs and matches the quoted output (~8 rows expected) | NOT EVALUATED — no table |
| Every row names catching and non-catching gates with exits | NOT EVALUATED — no table |
| C1 / dependency-wording row records both historical invisibility and current detectability | NOT EVALUATED — no table |
| Frozen-checker row names the boundary re-pin requirement | NOT EVALUATED — no table |
| Row that fails to reproduce | none observed; no rows existed to replay |

Declared row classes from the r99 declaration in `LOG.md` (emptied `depends_on`; wrong-but-earlier edge; deleted terminal row; F15 support_check-silent mutants; dependency-wording removal; consistent-regeneration bound; checker's frozen-pin status) were not matched against a delivered table.

## Bottom line

ABSENT — after 40 poll tries plus a 22:30:14 confirmation, `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, and any `S5*.md` producer report were missing; the table was not audited.
