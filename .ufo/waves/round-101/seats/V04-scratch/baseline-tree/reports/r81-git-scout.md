# Round 81 git identity scout

## Evidence (read-only)

At this checkout, `git status --short --branch` showed `## craft/lore` and an already-modified `.shokunin/lore/LOG.md`; I did not alter it. Git config inspection showed global `user.name=ci`, `user.email=ci@local`, overridden by the parent repository `.git/config` with `games-engine-mechanics-shokunin` / `games-engine-mechanics@shokunin.local`. Thus the effective default is the wrong lane identity, irrespective of the lower-priority global values.

`git var GIT_AUTHOR_IDENT` and `git var GIT_COMMITTER_IDENT` both returned `games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local> ...`. Running the same queries with `git -c user.name=lore-shokunin -c user.email=lore@shokunin.local` returned `lore-shokunin <lore@shokunin.local> ...` for both. I executed the following shell check read-only: inherited identity failed with exit 1; explicit overrides passed both checks with exit 0. `git var` only resolves identities; these checks did not create commits or alter configuration.

## Proposed exact preflight

Run in the repository immediately before any authorized commit, without setting config:

```sh
#!/bin/sh
set -eu
expected='lore-shokunin <lore@shokunin.local>'
check_identity() {
  label=$1
  shift
  for kind in GIT_AUTHOR_IDENT GIT_COMMITTER_IDENT; do
    actual=$("$@" var "$kind")
    case "$actual" in
      "$expected "*) printf 'PASS %s %s: %s\n' "$label" "$kind" "$actual" ;;
      *) printf 'FAIL %s %s: expected %s; got %s\n' "$label" "$kind" "$expected" "$actual" >&2; return 1 ;;
    esac
  done
}
check_identity inherited git
check_identity explicit git -c user.name=lore-shokunin -c user.email=lore@shokunin.local
```

This intentionally stops at the inherited check when defaults are wrong. To proceed, use explicit `-c user.name=... -c user.email=...` on the actual authorized Git commit command too; a successful preflight alone does not bind a later separate Git process to those values. Check both author and committer because `GIT_AUTHOR_*` and `GIT_COMMITTER_*` environment overrides can independently affect the resolved identities. A shell role check can additionally say: **report-only worker → do not commit or push; return report to parent.** Parent-controlled authorized commit → run identity preflight and use explicit identity on that commit. No push should follow absent explicit authorization.

## Limits

This verifies the effective local identity resolution at the time of the query, not who actually authored report contents, whether a future command uses the overrides, whether any commit is authorized, or whether a push reached a remote. It makes no source-truth, canon, rights, or mechanics inference. I made no config changes, commits, pushes, merges, or edits outside this report.
