# V06 c1-refreeze-scope — round 99

- Seat: V06 c1-refreeze-scope (verifier, leaf). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5`
  (wave tree uncommitted; HEAD during the wait
  `337f0fa52b02626b7687eedbb2d99fab30446fe4`, which is a descendant of
  `4265df5` — the blocked-dispatch zero-increment commit, not an r99 freeze).
- Seat bar (not scored): after S1, `git diff` the contract vs `4265df5` is
  payload upgrade + the new case + version fields only; no pin path/digest
  regression for unchanged files; the r95/r96/r97/r98 pins' pre-existing
  fields preserved.
- Dependency: S1 producer report under
  `.ufo/waves/round-99/seats/` (S1 owns
  `corpus/tools/dependency_freeze.py` +
  `corpus/tools/dependency-freeze-contract.json`) AND those artifacts.
  Both required. A plan or an in-flight contract is not a delivered revision.
- Writes: this report only. No scratch files. Leaf seat: no nested agents,
  no commits, no pushes, no network. No lane corpus bytes written.

## Poll-wait record (20 s cadence, max 40; artifacts AND producer report)

Poll started `2026-10-17T22:00:52-0300`. Baseline contract sha256 from
`git show 4265df5:corpus/tools/dependency-freeze-contract.json` was
`153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`.
Ready condition: a seats-dir file matching `S1*.md` (also probed
`S1-freeze-hygiene.md`, `S1.md`, `S1-c1.md`) AND the on-disk contract
bytes differing from that baseline. The first 300 s of the loop were
foreground-capped by the tool timeout and the same process continued in
the background through try 40 (wall 780 s). No stall-escape. This was
not an all-reports poll, so the subtract-SELF convention did not apply.

Quoted tail of the poll log (tries 25–40; contract sha had already
settled at try 25, tool sha at try 22):

```
try=25 ts=2026-10-17T22:08:52-0300 seats_dir=True n_files=7 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=26 ts=2026-10-17T22:09:12-0300 seats_dir=True n_files=7 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=27 ts=2026-10-17T22:09:32-0300 seats_dir=True n_files=7 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=28 ts=2026-10-17T22:09:52-0300 seats_dir=True n_files=7 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=29 ts=2026-10-17T22:10:12-0300 seats_dir=True n_files=7 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=30 ts=2026-10-17T22:10:32-0300 seats_dir=True n_files=7 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=31 ts=2026-10-17T22:10:52-0300 seats_dir=True n_files=8 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=32 ts=2026-10-17T22:11:12-0300 seats_dir=True n_files=9 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=33 ts=2026-10-17T22:11:32-0300 seats_dir=True n_files=9 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=34 ts=2026-10-17T22:11:52-0300 seats_dir=True n_files=10 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=35 ts=2026-10-17T22:12:12-0300 seats_dir=True n_files=10 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=36 ts=2026-10-17T22:12:32-0300 seats_dir=True n_files=11 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=37 ts=2026-10-17T22:12:52-0300 seats_dir=True n_files=11 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=38 ts=2026-10-17T22:13:12-0300 seats_dir=True n_files=11 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=39 ts=2026-10-17T22:13:32-0300 seats_dir=True n_files=11 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
try=40 ts=2026-10-17T22:13:52-0300 seats_dir=True n_files=11 s1=ABSENT contract_changed=True contract_sha=8c2561b043c25db7 tool_sha=6f81f8be19742372
ABSENT_AFTER_40
SEAT_FILES S3-fixture-author.md S4-fixture-docs.md V10-c2-checker.md V105-c2-event-description.md V11-c2-inherited-equality.md V119-c2-anchors-3.md V13-c2-anchors.md V68-adjacency-2.md V77-c2-map-inventory.md V80-c2-prose-prefix.md V86-c2-no-new-entity.md
```

Earlier movement inside the same loop (not a close): try=1
(`22:00:52`) contract still baseline `153ebc5b2092948e`, tool
`03d04365cf00903e`; try=4 tool sha moved; try=12 contract sha moved to
`8f9c1f5316141b61`; try=22 tool sha settled at `6f81f8be19742372`;
try=25 contract sha settled at `8c2561b043c25db7`. S1 report column
was `ABSENT` on every try.

## Post-budget confirmation (not an extra poll)

`2026-10-17T22:30:02-03:00`, sixteen minutes after try 40. Command and
observed output:

```
$ date -Is; find .ufo/waves/round-99/seats -maxdepth 1 \( -iname 'S1*' -o -iname 's1*' \) -printf '%y %T+ %s %p\n'; find .ufo/waves/round-99/seats -maxdepth 1 -type f -name 'S*.md' -printf '%T+ %s %f\n'; stat -c '%y %s %n' corpus/tools/dependency-freeze-contract.json corpus/tools/dependency_freeze.py; sha256sum corpus/tools/dependency-freeze-contract.json corpus/tools/dependency_freeze.py; git rev-parse HEAD
2026-10-17T22:30:02-03:00
d 2026-10-17+22:08:46.2850207740 12 .ufo/waves/round-99/seats/S1-scratch
2026-10-17+22:01:40.6929649330 5069 S3-fixture-author.md
2026-10-17+22:03:54.7336127620 9303 S4-fixture-docs.md
2026-10-17 22:08:46.248249589 -0300 25987 corpus/tools/dependency-freeze-contract.json
2026-10-17 22:07:33.506669398 -0300 29104 corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  corpus/tools/dependency_freeze.py
337f0fa52b02626b7687eedbb2d99fab30446fe4
```

The only maxdepth-1 `S1*` entry is the directory `S1-scratch` (12 bytes,
mtime `22:08:46`), not a report. Producer markdown on disk: S3 and S4
only. No `S1*.md`, no `s1*.md`. A `22:20:28` `find .ufo/waves/round-99
-iname '*S1*'` hit only `S1-scratch` plus historical copies under
`V40-scratch/archive/` (prior rounds). Those archive files are not this
wave's producer report. V58-noted pids `1666590`, `1668137`, `1675325`
were not alive at the `22:20` `ps -p` check (header only).

## Not scored

Contract and tool bytes were present and stable from try 25
(`22:08:52`) through the `22:30:02` confirmation (contract
`8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`,
25987 bytes; tool
`6f81f8be19742372ddc6819f6cf50dad985fe2b6e7c579613f5f4067`, 29104
bytes). That is artifact presence, not an S1 close. The seat bar is
"After S1". The producer report never landed, so the contract diff vs
`4265df5` was not scored: no path inventory, no pin path/digest
regression verdict, no r95/r96/r97/r98 pre-existing-field verdict.
In-flight reads during the wait are not a result.

ABSENT — S1 producer report never appeared under `.ufo/waves/round-99/seats/` after 40 tries (22:00:52–22:13:52) and was still absent at 22:30:02; contract diff vs 4265df5 not scored.
