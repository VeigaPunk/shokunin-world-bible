# V80 c2-prose-prefix — round 99

Seat: V80 (verifier, c2-prose-prefix). Baseline: r98 closure `4265df5`
(`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD at verification:
`337f0fa52b02626b7687eedbb2d99fab30446fe4`. All commands ran from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested
agents, no commits, no pushes, no network. Writes: this report (absolute path)
and `.ufo/waves/round-99/seats/V80-scratch/` (`hashes-1.txt`, `final-verify.txt`).
No producer-owned file was written by this seat.

Scope: strict byte-prefix chain of the six fixtures' `fictional-excerpts.md`:

`r94-paired-crossing` ⊂ `r95-crossing-aftermath` ⊂ `r96-crossing-response` ⊂
`r97-crossing-acknowledgment` ⊂ `r98-clerk-filing` ⊂ `r99-window-lapse`

and that the lapse section appears exactly once, at the end of the r99 file.

## 0. Poll-wait record (SELF subtracted; no stall-escape)

First look (22:01:14) found the r99 fixture directory already present, but
`fictional-excerpts.md` was still an r98-sized copy (4187 bytes, `cmp -s` vs r98
identical) and `S3-fixture-author.md` was absent. That was the in-flight copy,
not a finished delivery, so it was not judged.

S3 landed during the same minute:

- 22:01:13 `corpus/fixtures/r99-window-lapse/fictional-excerpts.md` mtime, 5114 bytes.
- 22:01:40 `S3-fixture-author.md` present (5069 bytes).
- 22:01:46 hash snapshot `V80-scratch/hashes-1.txt`.
- 22:02:19 second snapshot, 20 s later: all six sha256 values unchanged
  (`ALL_STABLE True`). S3 report still present.

No unbounded stall. Tries used: 1 (artifact incomplete) + 1 stability recheck.
Producer report required for this seat (`S3-fixture-author.md`) was present
before the verdict. S4 was not required for this comparison (S4 owns README and
claim-excerpt-map, not `fictional-excerpts.md`).

## 1. Strict byte-prefix chain

`cmp -n <predecessor-length>` compares only the first N bytes. rc=0 means those
bytes match. `cmp -s` on the whole files returns rc=1, so each successor is
strictly longer (not a copy).

```
$ wc -c corpus/fixtures/r94-paired-crossing/fictional-excerpts.md \
        corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md \
        corpus/fixtures/r96-crossing-response/fictional-excerpts.md \
        corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md \
        corpus/fixtures/r98-clerk-filing/fictional-excerpts.md \
        corpus/fixtures/r99-window-lapse/fictional-excerpts.md
 1116 corpus/fixtures/r94-paired-crossing/fictional-excerpts.md
 1845 corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
 2588 corpus/fixtures/r96-crossing-response/fictional-excerpts.md
 3410 corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md
 4187 corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
 5114 corpus/fixtures/r99-window-lapse/fictional-excerpts.md
18260 total
rc=0

$ cmp -n 1116 corpus/fixtures/r94-paired-crossing/fictional-excerpts.md \
              corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
rc=0
$ cmp -s  …r94…/fictional-excerpts.md …r95…/fictional-excerpts.md
rc=1

$ cmp -n 1845 …r95…/fictional-excerpts.md …r96…/fictional-excerpts.md
rc=0
$ cmp -s  …r95… …r96…
rc=1

$ cmp -n 2588 …r96…/fictional-excerpts.md …r97…/fictional-excerpts.md
rc=0
$ cmp -s  …r96… …r97…
rc=1

$ cmp -n 3410 …r97…/fictional-excerpts.md …r98…/fictional-excerpts.md
rc=0
$ cmp -s  …r97… …r98…
rc=1

$ cmp -n 4187 …r98…/fictional-excerpts.md …r99…/fictional-excerpts.md
rc=0
$ cmp -s  …r98… …r99…
rc=1
```

Python `bytes.startswith` on the same files (22:02:29, sha256 identical to the
22:01:46 snapshot):

```
585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2  1116  r94
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  1845  r95
06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3  2588  r96
8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c  3410  r97
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  4187  r98
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  5114  r99

r94 ⊂ r95  startswith=True strict=True delta=729
r95 ⊂ r96  startswith=True strict=True delta=743
r96 ⊂ r97  startswith=True strict=True delta=822
r97 ⊂ r98  startswith=True strict=True delta=777
r98 ⊂ r99  startswith=True strict=True delta=927
```

Each delta begins with `\n## Round NN …`. The r98→r99 delta is exactly:

```
b'\n## Round 99 lapse note (2026-10-17)\n\nNewly authored fictional first-person note, attributed to in-world source ID `clerk-lapse-note`, folio 9, lines 1–5. …'
```

Inherited files are the baseline bytes, not a rewritten working-tree copy:

```
$ git rev-parse HEAD
337f0fa52b02626b7687eedbb2d99fab30446fe4
$ git rev-parse 4265df5
4265df5e86e4121bde4125b649b89bb1676676a5

git show 4265df5:<path> == working tree:
  r94 fictional-excerpts.md  True
  r95 fictional-excerpts.md  True
  r96 fictional-excerpts.md  True
  r97 fictional-excerpts.md  True
  r98 fictional-excerpts.md  True
```

r99 is untracked (`git cat-file -e HEAD:corpus/fixtures/r99-window-lapse/fictional-excerpts.md`
rc=128). All six files are `text/plain; charset=utf-8` and end with a single
newline. No CRLF. The chain is raw bytes, not a normalized text compare.

## 2. Lapse section exactly once, at the end

In `r99-window-lapse/fictional-excerpts.md` (5114 bytes, 76 lines):

```
count '## Round 99 lapse note' = 1     byte offset 4188 (first byte after the r98 prefix)
count 'clerk-lapse-note'       = 1     line 68
count 'Tick 15:'               = 1     line 70
headings after the lapse section: []
file ends with newline: True
trailing bytes: b' matter stays open.\n'
```

Case-insensitive `lapse` matches: exactly 3, all inside that terminal section:

- line 66: `## Round 99 lapse note (2026-10-17)`
- line 68: `` `clerk-lapse-note` ``
- line 76: `the clerk's first-person lapse record`

r94–r98 contain zero occurrences of `lapse`, `clerk-lapse-note`, `Tick 15:`, or
`## Round 99`. Each earlier round heading appears once in r99 and once in every
successor that should inherit it (`## Round 95` ×1 from r95 on, through
`## Round 98 clerk filing` ×1 in r98 and r99). Nothing is duplicated by the append.

The section is terminal: it starts at the first byte past the preserved r98
prefix, no later `## ` heading exists, and the file ends on that section's
scope sentence.

## 3. Agreement with S3

S3's report states excerpt base 4187 / now 5114, `excerpt byte-prefix True`,
`excerpt starts with base then newline True`. Observed here: r98 is 4187,
r99 is 5114, `cmp -n 4187` rc=0, delta begins `\n## Round 99 lapse note`.
No contradiction with the producer report on this seat's scope.

Not claimed here: map-obligation count, census, `check_bible`, freeze pins,
or resolution/blame semantics. Those belong to other seats. This seat only
compared excerpt bytes.

PASS: r94⊂r95⊂r96⊂r97⊂r98⊂r99 fictional-excerpts.md strict byte-prefix chain intact; the lapse section appears exactly once, at the end.
