# V44 c2-table-2 — round 99

Seat: V44. Task: independently re-derive three rows of `corpus/knowledge/r99-gate-blind-spot-table.md` and compare them with S5's rows. Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. No commits, no pushes, no network, no nested agents. Writes: this report and `.ufo/waves/round-99/seats/V44-scratch/` only.

Axes for this seat: artifact presence (the table file), producer-report presence (S5), and comparison fidelity (own mutations vs S5's quoted outputs). The third axis was not scored. A missing table is not a plan to verify.

## Poll-wait

Checked together, 20 s cadence, 40 tries: `corpus/knowledge/r99-gate-blind-spot-table.md` (non-empty), and any `seats/S5*.md` except SELF. Log: `.ufo/waves/round-99/seats/V44-scratch/poll.log`.

- try 1 at `2026-10-17T22:05:18-03:00`: `table=absent note=absent reports=none`
- tries 2–30: same absence. The poller process was killed by the host 600 s background timeout after try 30 (`2026-10-17T22:14:58-03:00`). Bounded stall-escape: resumed tries 31–40 at `2026-10-17T22:19:10-03:00`. Not a mutual wait; SELF was never counted.
- try 40 at `2026-10-17T22:22:10-03:00`: `table=absent note=absent reports=none`
- log line: `ABSENT after 40 tries t=2026-10-17T22:22:30-03:00`

Post-budget existence check (not an extra try, not a verification):

```
$ date -Iseconds
2026-10-17T22:25:11-03:00
$ ls -la corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
ls: cannot access '.../r99-gate-blind-spot-table.md': No such file or directory
ls: cannot access '.../r99-lapse-scope-note.md': No such file or directory
$ ls -la .ufo/waves/round-99/seats/S5*
ls: cannot access '.../seats/S5*': No such file or directory
```

`find` for `r99-gate-blind-spot-table.md` under the lane returned nothing. The only `S5-*.md` hits were round-98 reports. S3's `S3-fixture-author.md` and S4's `S4-fixture-docs.md` were present; they are not S5 and they are not the table.

## Comparison

Not performed. There are no S5 rows, no quoted commands, and no quoted outputs to compare against. Scratch mutations under `V44-scratch/` (a bible/map/support/freeze probe on copies of `r99-window-lapse`, and a freeze mirror of `r98-clerk-filing`) were not used as a substitute for the missing table and are not a verdict on C2 component 2.

## Bottom line

ABSENT — after 40 poll tries the blind-spot table and the S5 producer report were both missing, so three rows were not compared.
