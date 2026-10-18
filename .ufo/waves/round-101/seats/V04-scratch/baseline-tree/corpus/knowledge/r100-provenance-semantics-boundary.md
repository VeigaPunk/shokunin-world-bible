source: `corpus/tools/dependency_freeze.py`; `corpus/tools/dependency-freeze-contract.json`; `corpus/tools/support_check.py`; `corpus/tools/map_obligations.py`; `corpus/fixtures/check_bible.py`; `corpus/tools/README.md` (Round-99 addendum); `corpus/knowledge/r99-gate-blind-spot-table.md` (row 6 and dated round-100 rows 10–12); `LOG.md:3303-3313` (r99 AC-1/AC-2/AC-3 corrections); `corpus/fixtures/r95-crossing-aftermath/{fictional-excerpts.md,claim-excerpt-map.md}`; `corpus/fixtures/r98-clerk-filing/{timeline.json,fictional-excerpts.md}`
verified-at: 2026-10-17 — the three correction classes and a prose-only control were replayed this pass on isolated copies of the delivered tool and contract; the pre-r99 comparison used `git show 4265df5:<path>`. Every cited local path was checked; no network request, live fixture mutation, or live `--freeze` write was made by this author.
recheck: whenever a cited tool, pin, payload schema, fixture, or correction changes, and before treating a receipt as evidence for any semantic claim. Re-run on the delivered revision; this record is not a new gate or independent admission.
citation-convention: bare tool filenames resolve to the full paths in `source:` above; a bare `:NN` continues the preceding tool path in the same sentence. The ten bare payload filenames are relative to the invoked pinned fixture, not to this knowledge directory.

# Provenance is not semantics — round 100

**BR-01's prose half is byte-change-detectable, not dependency-semantics-provable.** Full-file pinning records identity to selected bytes. A prose edit can be detected without the checker understanding either the removed sentence or its replacement. In the tool's term “semantic inventory,” semantic means a modeled JSON inventory, not natural-language understanding.

## What the delivered pin establishes

The schema-2 pin in `corpus/tools/dependency-freeze-contract.json` names a repo-relative fixture path and hashes these ten declared files: `entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, and `source-excerpt.md`. The tool requires that payload shape (`dependency_freeze.py:297-337`), enforces the named path (`:340-355`), builds the fixture model, then compares it with the recorded inventory (`:370-398`).

For a valid verification invocation whose pin, path, files, and model can be evaluated:

- **Byte identity, bounded to the declared set.** A clean inventory plus equal content digest produces `RESULT PASS`, exit 0. The content digest is SHA-256 over the sorted file-name→SHA-256 payload (`dependency_freeze.py:109-116`). This is an identity check against recorded bytes, not source authentication or an endorsement of the bytes.
- **Named-file change detectability.** If the modeled inventory is clean but a pinned file's bytes differ, verification reports `DIGEST-MISMATCH`, exit 2 `RESULT ERROR`, naming the changed file and its before/after hashes (`dependency_freeze.py:358-367`, `:388-394`). The name locates a byte difference; it does not identify which proposition changed or whether the replacement entails the JSON.
- **Modeled-inventory precedence.** Lost/gained dependency edges, modeled event endpoints, and relation triples are compared first (`dependency_freeze.py:220-262`). A finding such as `REDUCTION-DETECTED`, `ADDITION-DETECTED`, or `ENDPOINT-CHANGE` produces exit 1 `RESULT FAIL` before the digest branch (`:384-387`), even if prose bytes changed too. No named `DIGEST-MISMATCH` is promised in that case. This is r99 **AC-1**, recorded at `LOG.md:3303-3307` and qualified in `corpus/tools/README.md:310`.

The initial guards and CLI validation still matter. A malformed or missing model, invalid contract, wrong path, or invalid invocation is not a clean-inventory prose comparison. In particular, r99 **AC-3** (`LOG.md:3311-3313`) scopes the historical precedence prose: `fixture --freeze fixture` is rejected before verification or freezing (`dependency_freeze.py:640-648`), with only `INVALID-ARGUMENTS` and exit 2.

## What it does not establish

- **Dependency meaning or adequacy.** A frozen `depends_on` list can be preserved exactly while the source does not entail it. The tool compares recorded sets and fields; it does not infer a causal relation, choose the correct predecessor from the prose, or establish that a pin was semantically correct when written. Re-freezing can record new bytes; it does not prove the old or new record true.
- **Whole-claim entailment.** A hash cannot tell whether a note supports a description, whether a paraphrase is faithful, or whether an exact lexical anchor supports the whole mapped proposition. `support_check.py` supplies fixed-string/span/mode/inventory receipts; `map_obligations.py` supplies raw-pointer completeness and source-ID binding receipts; neither turns byte identity into semantic proof.
- **Testimony truth or chronology authentication.** `check_bible.py` checks schema, citations, relations, and timeline structure. Editorial tick integers, event IDs, and recorded edge order are not authenticated chronology. Neither a structural CLEAN nor a byte-identical fixture decides whose account is true, resolves a dispute, establishes identity or institutional authority, assigns blame, or supplies canon.
- **Unlimited file coverage or permanent immutability.** The pin covers the declared ten, not every neighboring file. `corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md` is outside that set (the measured bound in `corpus/tools/README.md:338`). The guarded `--freeze` is an integration-time contract-writing operation, not a read-only verification command or an independently authenticated history.
- **Rights or permission.** No receipt establishes copyright status, reuse permission, AI-training permission, cultural authority, or source authenticity. These remain separate, unassessed questions; public accessibility and attribution do not settle them.

## The historical “invisible to every gate” bound

The r98-era prose blind spot is preserved as **row 6** in `corpus/knowledge/r99-gate-blind-spot-table.md:158-194`. That row distinguishes coherent excerpt+anchor replacements and non-anchor prose edits from excerpt-only removal of a mapped verbatim anchor. It is not a separate r98 table file.

r99 **AC-2** (`LOG.md:3308-3311`) corrects the overbroad phrase: removing a mapped verbatim anchor was already visible to `support_check`, exit 1, before full-file pinning. The historical freeze's JSON-only payload missed that edit, but not every gate did. The genuinely all-green historical class was prose outside checked anchors or a coherent excerpt+anchor replacement. Delivered full-file pinning detects the bytes of such edits on pinned fixtures; it still does not validate dependency semantics.

The distinction is lexical, not semantic: a missing fixed string fails even when its replacement might mean the same thing; a coherent restatement can retain all lexical receipts without proving the JSON proposition. Row 6's before/after measurements and round-100 row 10 must be read with that scope, not as claims that `support_check` understands dependency meaning.

## Replays on this delivered revision

Commands were run from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. The delivered freeze tool was SHA-256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`; the contract was `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5` both before and after the replay. Complete commands/stdout/exits are in `.ufo/waves/round-100/seats/T4-scratch/replay-output.txt`; mutation definitions and individual commands are also recorded in dated rows 10–12 of `corpus/knowledge/r99-gate-blind-spot-table.md`.

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replay.py run
```

Observed, exit 0 for the replay harness (the negative probes' own expected non-zero exits are shown separately):

- **AC-2 / mapped-anchor control:** replace only excerpt wording `depends on both ninth-bell entries` with `follows both ninth-bell entries` in an r95 copy, leaving J14 unchanged. The `4265df5` support tool and the delivered support tool each printed `FAIL: J14: source-support anchor missing`, `RESULT FAIL`, exit 1. They are byte-identical, SHA-256 `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`. The historical freeze printed `RESULT PASS`, exit 0; the delivered freeze printed `DIGEST-MISMATCH` naming `fictional-excerpts.md`, exit 2. Delivered `check_bible` stayed CLEAN, exit 0; `map_obligations` stayed `OBLIGATIONS raw=15 mapped=15` / `RESULT PASS`, exit 0.
- **AC-1 / simultaneous edge+prose edit:** drop `evin-ninth-bell` from `paired-crossing-decision.depends_on` in an r98 mirror and make the same prose replacement. The delivered freeze printed `FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1`, `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']`, `RESULT FAIL`, exit 1, with no `DIGEST-MISMATCH`. The prose-only twin, with its inventory unchanged, printed `DIGEST-MISMATCH` naming `fictional-excerpts.md`, `RESULT ERROR`, exit 2.
- **AC-3 / invalid combined invocation:** `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing --freeze corpus/fixtures/r98-clerk-filing` printed only `FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both` and `RESULT ERROR`, exit 2. The live contract hash was unchanged.
- **Persisted regression control:** the byte-identical delivered tool and contract ran `--self-test` inside `.ufo/waves/round-100/seats/T4-scratch/replays/delivered-self-test/`, with its own r95 base and temporary files contained under this seat's scratch. It printed `SELF-TEST 18/18`, `RESULT PASS`, exit 0, including `markdown_tamper` with exit 2 and finding `DIGEST-MISMATCH`. This is capability evidence, not semantic certification.

## Coverage is a separate claim

This pass independently ran `python3 corpus/tools/dependency_freeze.py corpus/fixtures/<name>` for the delivered names `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`, and `r99-window-lapse`: all seven printed `RESULT PASS`, exit 0. The r99 receipt was `FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1`, digest `7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`. This supersedes the old r99-unpinned/six-fixture statements as current coverage; their dated historical text remains intact. It establishes pin coverage through r99, not that the new r100 review fixture is pinned or that any testimony is true.
