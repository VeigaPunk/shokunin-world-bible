# S5 knowledge-author — round 99

Seat: S5. Owned bytes: `corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md`. Report: this file. Scratch: `.ufo/waves/round-99/seats/S5-scratch/` (`replay.py`, `replay-log.txt`, `work/`, `work2/`, `work3/`, `work4/`). No other writes. No commits, no pushes, no network, no nested agents. Commands from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Baseline named in the declaration: `4265df5`. HEAD at measurement: `337f0fa52b02626b7687eedbb2d99fab30446fe4`.

## Poll

S3 artifacts were absent at the first check, then `corpus/fixtures/r99-window-lapse/` appeared as an r98 byte-copy plus lapse edits in `sources.json`, `timeline.json`, and `fictional-excerpts.md`. `S3-fixture-author.md` landed next (PASS: 6/1/8, `check_bible` CLEAN exit 0, seven files byte-identical to `4265df5` r98, README and map left for S4). `S4-fixture-docs.md` landed after that (map 21 rows, README rewritten). Freeze contract was still five-file when S3 landed; by the replay start it was payload schema 2 with ten files on all six chain pins. S1's report was absent through the quote window and present at handoff (`S1-full-file-pins.md`). Tool hash held at `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` and contract at `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` across a 20s poll and again at handoff. No ABSENT. No stall-escape.

## What was written

1. `corpus/knowledge/r99-gate-blind-spot-table.md` — sha256 `4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e`, 20526 bytes. Nine measured classes (emptied `depends_on`; non-empty edge reduction; wrong-but-earlier edge; deleted terminal row; F15 span-break; F15 source-id; dependency-wording removal, historical and C1; consistent regeneration; checker byte-freeze) plus the unknown-id/dangling classes `check_bible` does catch. Each row has catch/miss exits and a quoted command from this pass.
2. `corpus/knowledge/r99-lapse-scope-note.md` — sha256 `96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54`, 14990 bytes. Header is source/verified-at/recheck. Class: clerk lapse record that closes no one. Cross-refs `corpus/knowledge/r98-clerk-scope-note.md` and the r94 minute at `corpus/fixtures/r94-paired-crossing/fictional-excerpts.md:15-20` (crossing-only sentence at `:19`).

`git status --porcelain` shows those two paths as untracked. The only other corpus dirt is producer-owned (`dependency_freeze.py`, `dependency-freeze-contract.json`, `corpus/tools/README.md`, `corpus/fixtures/r99-window-lapse/`). This seat did not touch them.

## Measured, not recollected

Live r99 control: `check_bible` CLEAN exit 0; `support_check` `21/21` `RESULT PASS` exit 0; `map_obligations` `raw=21 mapped=21` `RESULT PASS` exit 0. Census `ls -d corpus/fixtures/*/ | wc -l` = 173. Timeline and sources prefixes parsed-equal to r98 (`True`). Excerpt byte-prefix of r98 (`True`, 4187 → 5114). `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` byte-identical to r98.

Chain on the delivered pin: r88 `acf677a7…`, r94 `048b8ff3…`, r95 `97cffd7b…`, r96 `43911900…`, r97 `a28b9ea0…`, r98 `5ecf84e1…`, each `RESULT PASS` exit 0 (6/6). Those digests match S1's report. `--self-test` `SELF-TEST 18/18` `RESULT PASS` exit 0, including `markdown_tamper` exit 2 `DIGEST-MISMATCH`. `r99-window-lapse` is `UNPINNED-FIXTURE` exit 2. S1 states that was intentional (chain stays the six). The lapse note records that bound.

Freeze catches were run on path-bound mirrors of pinned `r98-clerk-filing` using a copy of the delivered tool and contract, because a renamed scratch directory is an `UNPINNED-FIXTURE` name miss, not a semantic result.

- Emptied `depends_on`: `check_bible` CLEAN 0; support and map PASS 0; freeze `REDUCTION-DETECTED` exit 1 (`clerk-filing-open lost depends_on ['acknowledgment-aru-records']`).
- Wrong-but-earlier: bible/support/map green; freeze `ADDITION-DETECTED` + `REDUCTION-DETECTED` exit 1.
- Deleted terminal, map row kept: bible CLEAN 0; support PASS 0; map `phantom_obligation` exit 1; freeze `REDUCTION-DETECTED` exit 1.
- Span-break J05 `17`→`20`: support FAIL exit 1 (`outside-span=17`); bible CLEAN 0; map PASS 0; freeze `DIGEST-MISMATCH` exit 2 naming `claim-excerpt-map.md`. Span-break is not support_check-silent. Recorded as measured, not as the brief's hyphenation suggested.
- Source-id rebound to another declared source: support PASS 0; bible CLEAN 0; map `source_id_mismatch` exit 1; freeze `DIGEST-MISMATCH` exit 2 (digest only; `source_id` is outside the semantic inventory).
- Prose: baseline tool `4265df5` (`03d04365…`) on a coherent excerpt+anchor replacement of `depends on both ninth-bell entries` → `RESULT PASS` exit 0, digest still the JSON-only `59a0f4fa…`. Delivered pin, same edit: `DIGEST-MISMATCH` exit 2 naming `claim-excerpt-map.md` and `fictional-excerpts.md`; lexical gates stay green. Narrative-only map edit: lexical gates green, freeze `DIGEST-MISMATCH` exit 2 naming `claim-excerpt-map.md`. Excerpt-only removal, map anchor left stale: `support_check` FAIL exit 1 `J14: source-support anchor missing`. C1 detects the edit. It does not prove the sentence. S1's report records the same non-invisibility for an excerpt-only removal, on r94, with the same detail string (`pinned-file bytes changed outside the semantic inventory`).
- Consistent regeneration (drop terminal event, drop its map row, restate inventory): bible CLEAN 0, support PASS 0, map PASS 0; freeze still `REDUCTION-DETECTED` exit 1 on the JSON half.
- Checker pin: live `check_bible.py` sha256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` equals `boundary-doc-contract.json` `checker.sha256`. Default `boundary_doc_check` `CERTIFIED` exit 0. A one-comment scratch copy exits 1 `checker_drift`. Rows 1–3 cannot be closed in-checker without re-pinning that contract. Named in the table.

Unknown-id / dangling probes on the r99 terminal event all exit 1: unknown event, dangling entity, unknown source, missing `depends_on` key (`required nonempty list`), self dependency, repeated dependency, tick inversion, deleted predecessor (`unknown event 'clerk-filing-open'`).

Citation check after the write: 29/30 needles matched the cited line. The miss was a paraphrase needle (`assign blame`) against `claim-excerpt-map.md:69`; that line does contain `assigns blame to neither` (1153 characters; the first hit is `no-blame`). `README.md:11` carries the same bound. No citation was rewritten after that check because the cited lines support the sentences.

## Not done

S1's report was not an input to the table; the table was written from commands run here. It agrees with S1 on the chain digests, the 18/18 self-test, the `UNPINNED` r99 choice, and the excerpt-only support_check fail. If `dependency_freeze.py` moves off `fb9bb9ff…` or the contract off `8c2561b0…`, the table's recheck line applies; do not cite the freeze quotes past that byte change without re-running them. Scratch trees under `S5-scratch/work*` are replay residue, not corpus.

**Bottom line: PASS — both owned knowledge files are on disk, every cited path exists, the lapse class is bounded against the r98 note and the r94 minute, and each blind-spot row carries a command and observed exit from this pass (span-break is support_check-visible, recorded as measured; C1 names the prose edit as DIGEST-MISMATCH and does not prove the sentence).**
