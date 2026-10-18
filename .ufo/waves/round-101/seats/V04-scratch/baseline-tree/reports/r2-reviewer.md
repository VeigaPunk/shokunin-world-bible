# Round 2 reviewer report — implementation, evidence, and scope

## Verdict

The observed implementation supports the declared narrow coverage move: the checker recognizes a cited reverse `allied_with` edge only for distinct, unambiguous faction endpoints, reports a one-way edge at its original relation location, and leaves other relation types alone. I found no false real-world source or rights claim. The fixtures and documentation consistently label the treaty and lore as invented. The main limitation is that the round-2 archived/live evidence does not include the executor’s claimed malformed-source probes; the checker logic appears to address that case, but it is not independently evidenced by checked-in artifacts.

## Replayed evidence

From the repository root, I ran the four documented CLI commands against the working tree:

- `consistent`: exit 0, `CLEAN ... 0 violations`.
- `contradictions`: exit 1, exactly three violations: dangling `missing-map`, timeline inversion (`later` tick 3 before `arrival` tick 2), and double booking of Mira at tick 2.
- `ally-reciprocal`: exit 0, `CLEAN ... 0 violations`.
- `ally-one-way`: exit 1, one relation-local diagnostic: `relations[0] ... 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation`.

No fixture was modified by these CLI runs. The implementation in `fixtures/check_bible.py` first validates relation endpoints and sources, then checks exact `allied_with` rows. It excludes self-edges, dangling or duplicate/ambiguous entity IDs, and non-faction endpoints; reciprocal candidates must have reversed IDs, the same type, and a source ID in the source index. `carries` and other relation types are not subjected to reciprocity.

## Source and documentation integrity

`ally-reciprocal` and `ally-one-way` use the same explicitly fictional `harbor-compact` source, with fictional source title/reliability note, faction claims, and individually cited relation rows. The positive/negative fixtures differ by the reverse relation row, as intended. The README and decision table describe this as a local convention, not a universal law about alliances or proof that an absent edge is false; they state the checker does not infer prose, modify canon, or establish source authenticity. The reference ledger is kept separate from in-world evidence. These boundaries are consistent with the artifacts I read.

The implementation and docs choose an explicit **distinct endpoints** rule for alliance reciprocity. This resolves the scout’s self-edge ambiguity without introducing a separate self-alliance prohibition; self-edges are simply outside this rule. The README and decision table state this limit.

## Caveat / smallest follow-up

One narrow source-index edge case is not covered by fixtures or archived run evidence: `index('sources')` reports duplicate source IDs but still keeps the last row in its dictionary. The symmetry pass checks membership in that dictionary, so a reverse row citing a duplicated ID can count as a witness even though the source table itself has a duplicate-ID violation. The overall run still exits 1 for that source-table error, so this does not make the fixture pass cleanly; it can suppress the additional “lacks a sourced reciprocal” finding. This is a minor diagnostic precision gap, not a blocker for the demonstrated clean/reciprocal/one-way claim. Avoid broadening this round unless the orchestrator considers that exact meaning of “resolvable” essential; otherwise record it as an uncovered edge case.

The executor report says an unknown-source reverse-edge probe was run and behaved correctly, but its temporary input/output is not preserved in `corpus/live/runs/`. The checked-in implementation’s source-membership predicate is consistent with that claim, but this reviewer did not independently replay that temporary probe. The live run artifacts available here are the four fixture outputs above.

## Axis/scope assessment

For the stated one-rule move, coverage is supported: a formerly absent faction-reciprocity case now has a clean reciprocal fixture and a failing one-way fixture, while the prior consistent and contradiction cases retain their observed outcomes. The work remains a local data convention, not generalized relation validation. No evidence here supports broader claims about arbitrary relations, semantic source support, or canon truth.
