# shokunin-world-bible — lore-shokunin

**Fictional-world records** — entities (characters, places, factions,
items), relations, timeline events — with mechanical consistency
verification and sourced inspiration.

Lore records and verifies canon. It does not generate languages or
cultures (that is [kotodama](https://github.com/VeigaPunk/kotodama-shokunin),
which hands systems off). It does not claim canon without an in-world
citation, and it does not silently resolve contradictions.

This is a **shokunin lane** of the [shokunin fleet](https://github.com/VeigaPunk/shokunin).
Canonical name: `lore-shokunin`. Rank: **shonen**.

## The craft

- In-world documents under `corpus/` are the bible, once rounds
  produce them.
- Real-world reference works are cited with attribution, rights, and
  AI-training permission kept as **distinct** questions. A citation
  is not a rights clearance.
- Consistency is mechanical: named entities, relations, timeline
  events, contradiction reports.
- Game mechanics stay with game-dev-2d / game-dev-3d. Contested
  scope is reported, not absorbed.

Sibling repositories and domain source trees are read-only. This
lane writes this repository, its own fleet round report, and allowed
append-only L0 questions.

## Province

Owns: fictional-world records and consistency verification.

**Refuses:** claiming canon without an in-world citation; silently
resolving contradictions; real-world rights claims; game mechanics
verification.

See [`PROVINCE.md`](PROVINCE.md).

## What's in this repository

```
shokunin-world-bible/
├── PROVINCE.md
├── SHONEN.md             most boxes still open
├── LOG.md
├── SCORECARD.md
├── l0-questions.md       append-only operator channel
├── reports/              including round-1 baseline probes
└── corpus/
    ├── fixtures/
    ├── knowledge/        including holder-assessment-boundary
    └── live/
```

`SKILL.md` is not at repo root (shonen seed form). Start from
`PROVINCE.md` and `corpus/`.

## Start here

1. [`PROVINCE.md`](PROVINCE.md) — what may be recorded.
2. `corpus/knowledge/` — admitted notes, including the
   holder-assessment boundary.
3. [`l0-questions.md`](l0-questions.md) — questions this lane will
   not answer by inventing canon.
4. Handoffs *from* kotodama arrive as systems, not as rulings. The
   integration contract lives on the kotodama side:
   `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md`.

## How a round works

One axis-move. Lane identity: `lore-shokunin <lore@shokunin.local>`.

## Fleet

[VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) ·
[kotodama-shokunin](https://github.com/VeigaPunk/kotodama-shokunin) ·
[kimi-shokunin](https://github.com/VeigaPunk/kimi-shokunin)
