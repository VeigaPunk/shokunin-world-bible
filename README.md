# lore-shokunin — 伝

Repo: `shokunin-world-bible`.

**Fictional-world records.** Entities (characters, places, factions,
items), relations, timeline events — with mechanical consistency
verification and sourced inspiration.

A **shokunin lane**: an expert agent for one domain, minted and trained
under the [shokunin skill](https://github.com/VeigaPunk/shokunin).
Rank: **shonen**. Promotion is a named non-author review of
[`SHONEN.md`](SHONEN.md), never self-attestation.

This lane answers: *do these in-world records stay consistent under the
checker — and is every canon claim cited from an in-world document
rather than from the agent's confidence?*

## Domain

From [`PROVINCE.md`](PROVINCE.md): the world bible, once rounds produce
it; real-world reference works cited with attribution / rights /
AI-training permission kept as **distinct questions**.

**Refuses:** claiming canon without an in-world citation; silently
resolving contradictions; real-world rights claims; game mechanics
verification (→
[game-dev-2d](https://github.com/VeigaPunk/shokunin-godot-2d)).

Generative linguistic-cultural systems (conlang, myth, costume lexicon)
are produced by
[kotodama](https://github.com/VeigaPunk/kotodama-shokunin) and **handed
off** here. kotodama does not edit this bible; this lane does not
generate those systems.

Sibling repositories and domain source trees remain read-only. This
lane writes only this repository, its own fleet round report, and
allowed append-only L0 questions.

## What's here

| Path | Role |
|---|---|
| [`PROVINCE.md`](PROVINCE.md) | owned records and the no-silent-resolution rule |
| [`corpus/fixtures/check_bible.py`](corpus/fixtures/check_bible.py) | mechanical consistency checker |
| [`corpus/fixtures/README.md`](corpus/fixtures/README.md) | how to invoke the checker |
| [`corpus/knowledge/`](corpus/knowledge/) | sourced notes (entities, relations, inspiration discipline) |
| [`corpus/live/`](corpus/live/) | run inputs and rejected drafts |
| [`reports/`](reports/) | verifier / adjudicator reports |
| [`SCORECARD.md`](SCORECARD.md) · [`LOG.md`](LOG.md) · [`SHONEN.md`](SHONEN.md) | axes, trail, promotion |

(`SKILL.md` is still in shonen seed form — see `corpus/`.)

## The checker

From this repository root (the historical `.shokunin/lore/` prefix in
`corpus/fixtures/README.md` does not resolve here):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/consistent
python3 corpus/fixtures/check_bible.py corpus/fixtures/contradictions
```

The first exits 0; the second exits 1 and prints the seeded violations.
No file is modified. Duplicate holder identities, tick order, and
continuity are mechanical properties of the records, not proof that the
fiction is “correct.” A green check is consistency of the file in hand,
not canon.

## How a lane learns

Append-only corpus; every claim separates observation / inference /
unknown; rounds are non-author-verified. See the fleet
[README](https://github.com/VeigaPunk/shokunin#readme).
