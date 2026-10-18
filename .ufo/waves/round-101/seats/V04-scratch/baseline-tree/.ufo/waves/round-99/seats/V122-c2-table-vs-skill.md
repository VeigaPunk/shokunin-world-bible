# V122 — c2-table-vs-skill (round 99)

Seat: V122 c2-table-vs-skill. Leaf verifier. No nested agents, no commits, no pushes, no network. Exclusive write: this report. Scratch: `.ufo/waves/round-99/seats/V122-scratch/poll.log` only. All commands from lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` unless an absolute path is quoted. Baseline named in the standing r99 declaration: `4265df5`. Working-tree HEAD at the final check: `337f0fa` (the blocked-dispatch zero-increment commit; the declaration itself is unchanged).

Question: do the blind-spot table's gate names and claims match the `SKILL.md` registry rows' scope statements, with no contradiction between those knowledge surfaces?

Answer: not evaluated. The table was never delivered. This seat did not compare the declaration, a plan, or scratch against `SKILL.md`.

## Poll-wait

Protocol: artifact `corpus/knowledge/r99-gate-blind-spot-table.md` AND producer report `seats/S5*.md` (not scratch), 20 s cadence, 40 tries. ENDGAME CONVENTION: this poll did not wait on other verifier reports and did not wait on SELF. No stall-escape. Bounded exhaustion of the 40 tries is the result, not a process fault.

Poll log: `.ufo/waves/round-99/seats/V122-scratch/poll.log` (41 lines).

```
try=1 ts=2026-10-17T22:06:15-03:00 table=0 note=0 s5=0 s2=0 skill=22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5 s5files=[] s2files=[]
try=40 ts=2026-10-17T22:19:15-03:00 table=0 note=0 s5=0 s2=0 skill=22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5 s5files=[] s2files=[]
ABSENT after 40 tries 2026-10-17T22:19:35-03:00
```

Counts from that log: `table=0` 40, `table=1` 0, `s5=0` 40, `s5=1` 0. `SKILL.md` sha256 was the same value on all 40 tries.

Post-window recheck at `2026-10-17T22:25:55-03:00` (presence only, no extra wait):

```
ls -la corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md
ls: cannot access '.../corpus/knowledge/r99-gate-blind-spot-table.md': No such file or directory
ls: cannot access '.../corpus/knowledge/r99-lapse-scope-note.md': No such file or directory

ls corpus/knowledge | grep -E 'r99|blind'
NO r99/blind knowledge files in lane

ls .ufo/waves/round-99/seats/S5*.md .ufo/waves/round-99/seats/S2*.md
ls: cannot access '.../seats/S5*.md': No such file or directory
ls: cannot access '.../seats/S2*.md': No such file or directory
```

`find` under the lane for `r99-gate-blind-spot-table.md` and `r99-lapse-scope-note.md` returned no hits. Parent-cwd strays `/home/vgpnk/Projects/shokunin/corpus/knowledge/r99-gate-blind-spot-table.md` and `/home/vgpnk/Projects/shokunin/r99-gate-blind-spot-table.md` also absent. `.ufo/waves/round-99/seats/S5*` does not exist (no S5 scratch directory). `S2-scratch/` exists and is empty (directory mtime 22:00). Name hits for `S5-*.md` / `S2-*.md` were only round-98 reports and a V40 archive copy of those round-98 reports.

Wave was otherwise live. Top-level producer reports present at the recheck:

```
find .ufo/waves/round-99/seats -maxdepth 1 -name 'S*.md' -printf '%f %s\n'
S3-fixture-author.md 5069
S4-fixture-docs.md 9303
```

`git status --porcelain` at the recheck, scoped to the surfaces this seat cares about plus the freeze tool S1 owns:

```
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
```

`SKILL.md` and `corpus/knowledge/` were clean. S2 had not edited the freeze row. That is context, not a table-vs-registry verdict.

## Other surface (readable, not a substitute for the table)

`SKILL.md` sha256 `22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5`, 16802 bytes, 101 lines. Registry rows observed (python extract of headings, `name`, and `scope`):

- `boundary_doc_check` (line 50) — frozen document/checker digests, receipts, numeric anchor ranges, fences and limited structure. No semantic, AST, or general prose validation; no whole-claim support or source review. (line 56)
- `discriminate_check` (line 61) — read-only comparison of the delivered checker and pinned `e97613c` on two durable fixtures; not a world-bible or source-support verdict. (line 67)
- `support_check` (line 72) — one cluster's inventory, row shape, delivery-mode, exact anchors, excerpt paths and line spans; does not decide whole-claim entailment, translation identity/fidelity, rights, permission, or canon. (line 78)
- `map_obligations` (line 83) — canonical one-obligation-per-row completeness and source-ID agreement; `inventory_mismatch` gating with the bound that a consistently regenerated declaration still exits 0; no entailment/fidelity/chronology/rights/permission/canon. (line 89)
- `dependency_freeze` (line 94) — JSON-layer edges, relation endpoints, and content digests over the five JSON tables only. Scope line 100 still says fixture Markdown is not pinned and BR-01's markdown/prose half remains open. Self-test line still says 17 cases. Pinned-values line still says content SHA-256 over the five JSON tables. Chain list still ends at `r98-clerk-filing` (no `r99-window-lapse`).

Those five names are the registry. No row was added or rewritten during the poll. Because `corpus/knowledge/r99-gate-blind-spot-table.md` does not exist, there are no table gate names or catch/do-not-catch claims to match against those scope statements. Declared row classes in `LOG.md` (emptied `depends_on`, wrong-but-earlier edge, deleted terminal row, F15 `support_check`-silent mutants, dependency-wording removal, consistent-regeneration bound, checker frozen-pin status) were not treated as the table.

## What was not done

No replay of table commands. No contradiction matrix. No judgment of whether a future C1 freeze-row edit would agree with a future table. S1's in-progress `dependency_freeze.py` comment about a ten-file pin was not used as a knowledge surface.

ABSENT — `corpus/knowledge/r99-gate-blind-spot-table.md` and the S5 producer report were absent through 40 polls (22:06:15–22:19:35) and a 22:25:55 recheck; gate-name/scope comparison was not run.
