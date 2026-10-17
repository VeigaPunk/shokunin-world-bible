# shokunin-world-bible — lore-shokunin

**Fictional-world records — entities, relations, timeline — with
mechanical consistency verification and sourced inspiration.**

This is a [shokunin](https://github.com/VeigaPunk/shokunin) lane. Rank:
shonen. Canonical lane name: `lore-shokunin`. Lore *records and
verifies* canon. It does not generate languages or cultural systems
(that is [kotodama](https://github.com/VeigaPunk/kotodama-shokunin),
which hands systems off and never edits this bible). It does not verify
game mechanics (that is
[game-dev-2d](https://github.com/VeigaPunk/shokunin-godot-2d)).

Canon without an in-world citation is refused. Contradictions are
reported, never silently resolved. Real-world rights, attribution, and
AI-training permission are kept as distinct questions on any cited
reference.

## Province

**Owns:** fictional-world records — characters, places, factions,
items; relations; timeline events; consistency verification; sourced
inspiration under the art-ledger discipline.

**Refuses:** claiming canon without an in-world citation; silently
resolving contradictions; real-world rights claims; game-mechanics
verification.

Writes only this repository, its own fleet round report, and allowed
append-only L0 questions. Sibling repositories and domain source trees
remain read-only. The kotodama handoff format lives on that lane
(`corpus/knowledge/synthesis/worldbible-integration-contract.md`); this
lane admits or rejects, it does not generate. Full boundary:
[`PROVINCE.md`](PROVINCE.md).

## Start here

1. [`PROVINCE.md`](PROVINCE.md) — owns / refuses / write scope.
2. [`corpus/fixtures/check_bible.py`](corpus/fixtures/check_bible.py) — mechanical consistency gate.
3. [`corpus/fixtures/`](corpus/fixtures/) — consistent, contradictory, and ledger-malformed cases.
4. [`SHONEN.md`](SHONEN.md) — promotion checklist.
5. [`l0-questions.md`](l0-questions.md) — append-only questions for the integrator.

This lane is still in shonen seed form: distilled `SKILL.md` lives in
the corpus until promotion. In-world documents accumulate under
`corpus/` as rounds produce them.

## The bible checker

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/consistent
python3 corpus/fixtures/check_bible.py corpus/fixtures/contradictions
```

The first exits 0. The second exits 1 and prints the seeded violations.
The checker validates a small cited fictional-world bible and
**reports, never resolves, contradictions**. Expected kinds:
`character`, `place`, `faction`, `item`. Required field shapes for
`sources`, `entities`, `relations`, and `timeline` are declared in the
script. Duplicate JSON members are errors, not merges. Paths in
`corpus/fixtures/README.md` still name the historical
`.shokunin/lore/` prefix; from this repo root the fixture directories
are `corpus/fixtures/<name>`.

A clean check is structural consistency against the named sources. It
is not a claim that the world is finished, that a contradiction has
been authored away, or that a kotodama packet has been admitted.

## What's in the repo

```
shokunin-world-bible/
├── PROVINCE.md       domain boundary
├── SHONEN.md         promotion checklist
├── LOG.md            append-only audit trail
├── SCORECARD.md      axis verdicts
├── l0-questions.md   integrator questions
├── reports/          verifier / adjudicator reports
└── corpus/
    ├── fixtures/     check_bible.py + consistent / contradiction cases
    ├── knowledge/
    └── lessons/
```

Protocol: append-only corpus; every claim separates observation /
inference / unknown; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme) for how a lane
learns.
