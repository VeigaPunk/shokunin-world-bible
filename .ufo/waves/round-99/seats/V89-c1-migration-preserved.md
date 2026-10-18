# V89 c1-migration-preserved — round 99

- Seat: V89 c1-migration-preserved (verifier). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5`
  (wave tree uncommitted; HEAD during the round
  `337f0fa52b02626b7687eedbb2d99fab30446fe4`, the blocked-dispatch zero-increment
  record). All commands from the lane root with `python3`.
- Claim this seat was to confirm: the r98 path-less legacy-pin migration
  survives the r99 payload upgrade — a path-less scratch pin still migrates
  under `--freeze`, quoted. r98 closed behavior (V02, tool `03d04365…`,
  contract `153ebc5b…`): missing / `null` / non-string / empty `fixture`
  prints `MIGRATED <name>: path-less legacy pin now names <path>` and exits 0;
  a different non-empty recorded path stays `SCOPE-REFUSED` exit 2.
- Axes named: existence (S1 artifacts AND S1 report), migration fidelity
  (path-less scratch pin still migrates), evidence (quoted commands),
  non-interference (this report + `V89-scratch` only).
- Scratch: `.ufo/waves/round-99/seats/V89-scratch/` (baseline copies of the
  r98 tool/contract taken at 22:01 before the upgrade landed, plus `poll.log`).
  Leaf seat: no nested agents, no commits, no pushes, no network. No migration
  probe was run.

## Poll record (20 s cadence, 40 tries; never verify a plan)

Poll started 22:01:52 -0300 against
`corpus/tools/dependency_freeze.py`,
`corpus/tools/dependency-freeze-contract.json`, and any
`.ufo/waves/round-99/seats/S1*.md`. Log:
`.ufo/waves/round-99/seats/V89-scratch/poll.log`.

```
try 1  22:01:52 changed=[] s_reports=['S3-fixture-author.md'] s1_any=[]
try 2  22:02:12 changed=['dependency_freeze.py:1792285324.079078'] s_reports=['S3-fixture-author.md'] s1_any=[]
try 6  22:03:32 changed=['dependency_freeze.py:1792285401.8454537'] …
try 9  22:04:32 changed=['dependency_freeze.py:1792285401.8454537', 'dependency-freeze-contract.json:1792285468.2057745'] s_reports=['S3-fixture-author.md', 'S4-fixture-docs.md'] s1_any=[]
try 19 22:07:52 changed=['dependency_freeze.py:1792285653.5066693', 'dependency-freeze-contract.json:1792285468.2057745'] s1_any=[]
try 22 22:08:52 changed=['dependency_freeze.py:1792285653.5066693', 'dependency-freeze-contract.json:1792285726.2482495'] s1_any=[]
try 40 22:14:52 changed=['dependency_freeze.py:1792285653.5066693', 'dependency-freeze-contract.json:1792285726.2482495'] s_reports=['S3-fixture-author.md', 'S4-fixture-docs.md'] s1_any=[]
ABSENT after 40
```

Tool and contract bytes stopped moving at try 22 (22:08:52) and stayed at
those mtimes through try 40. `S1*.md` was absent on every try. Producer
reports that did land are S3 and S4 only — not the freeze owner.

Post-cap checks (bounded stall-escape, recorded, not a second 40-try poll;
still no probe):

```
$ date; ls -la .ufo/waves/round-99/seats/S1*.md
Sat Oct 17 10:22:49 PM -03 2026
ls: cannot access '.ufo/waves/round-99/seats/S1*.md': No such file or directory

$ date; ls -la .ufo/waves/round-99/seats/S1*.md
Sat Oct 17 10:27:05 PM -03 2026
ls: cannot access '.ufo/waves/round-99/seats/S1*.md': No such file or directory

$ date '+%Y-%m-%d %H:%M:%S %z'; ls -la .ufo/waves/round-99/seats/S1*.md
2026-10-17 22:30:51 -0300
ls: cannot access '.ufo/waves/round-99/seats/S1*.md': No such file or directory
```

`find .ufo/waves/round-99 -name 'S1*'` at 22:22 found only
`.ufo/waves/round-99/seats/S1-scratch` (a `before/mirror/` tree, not a
report) plus other seats' archives. No `S1-freeze-hygiene.md` and no other
`S1*.md` under the round-99 seats directory. S1 process pids recorded by
V58 (`1675325`, `1668137`, `1666590`) were not alive at 22:27 (`ps -p` empty).

## What is on disk, and why it was not verified

Pre-upgrade snapshot (this seat, before try 1), matching the r98 delivered
hashes V02 quoted:

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
```

At 22:30:51 the files had been stable since 22:07:33 / 22:08:46:

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
$ stat -c '%y %s %n' corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
2026-10-17 22:07:33.506669398 -0300 29104 corpus/tools/dependency_freeze.py
2026-10-17 22:08:46.248249589 -0300 25987 corpus/tools/dependency-freeze-contract.json
```

Those bytes are an in-flight artifact, not a producer-declared revision. S1's
report never landed, so this seat did not run `--freeze` on a path-less
scratch pin and does not quote a `MIGRATED` line from this round. No
migration PASS or FAIL is claimed.

## Bottom line

ABSENT — S1 producer report never landed (40 polls 22:01:52–22:14:52, plus checks at 22:22:49, 22:27:05, and 22:30:51; only S3/S4 reports exist); path-less migration was not probed.
