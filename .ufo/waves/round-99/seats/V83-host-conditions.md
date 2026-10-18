# V83 host-conditions

Seat: V83. Lane: lore-shokunin r99 re-dispatch. Observation only. No corpus edits, no claim verification.

Axes recorded: provider status codes, completion latency, rate-limit headroom, shim/process health, orphaned helpers, host resource pressure. Repo claim results are not judged here.

Clocks are local `-03` unless marked UTC. Host: `plazir27`, Linux `7.2.3-arch1-3` x86_64, 32 CPUs, 30 GiB RAM, 34 GiB swap. Observer window: `2026-10-17T22:00:58-03:00` through `2026-10-17T22:33:04-03:00`. The wave was still running at close (pollers alive, seat files still appearing). This is a mid-wave record, not a post-wave autopsy.

Raw samples: `.ufo/waves/round-99/seats/V83-scratch/samples.tsv` (20 s cadence, `22:02:55`–`22:13:09`). Early journal cut: `V83-scratch/journal-hist.txt` (superseded by the `22:31:03` histogram below).

## Provider status (journal of `xai-shim.service`, pid 1579)

Command (run `2026-10-17T22:31:03-03:00`):

```
journalctl --user -u xai-shim.service --since '2026-10-17 21:40:00' --no-pager -o short-iso
```

Parsed access lines: 5573. Codes: `502=2564`, `404=4`, `200=3005`. Zero `429`. Zero `503`. Zero `401`/`403`. Journal has status lines only; response bodies are not logged, so a `502` cause is not recoverable from the journal.

| window | what was observed |
| --- | --- |
| `21:41:16`–`21:54:30` | blocked-dispatch `502` storm. Per-minute: 21:41=370, 21:42=550, 21:43=222, 21:44=212, 21:45=209, 21:46=212, 21:47=221, 21:48=207, 21:49=217, 21:50=129, 21:51=13, 21:54=1. First `502` `21:41:16`, last storm `502` `21:54:30`. |
| `21:55:44` | `~/.hermes/auth.json` mtime (mode `600`, 1342 bytes). Contents not read. |
| `21:56:02`, `21:56:20`, `21:56:34` | three `POST /v1/chat/completions` `404`. Bodies not in the journal. |
| `21:56:52` | first `200`. |
| `21:59`–`22:19` | all `200`. Peak minute `22:01` = 695. Then 22:00=360, 22:02=388, 22:03=295, 22:04=269, 22:05=97, and 20–62/min through 22:19. |
| `22:20:07` | one isolated `502`: `127.0.0.1 - "POST /v1/chat/completions HTTP/1.1" 502 -`. No neighboring `429`/`503`. Cause not in the journal. |
| `22:21`–`22:30` | all `200` (23, 42, 20, 25, 27, 22, 30, 25, 47, 36). |
| `22:31:03` | the alias probe below (counted as the fourth `404`). |

Re-check at `22:33:03`: `journalctl ... --since '2026-10-17 22:00:00'` non-200 after 22:00 was only that one `22:20:07` `502`. `awk` count of `429`/`503` since `21:40` was `n=0`. No journal lines matching `shim busy`, `token helper`, or `rate limit` since `21:40`.

Paths in the early cut (`22:02:41`, 3955 lines): 3952 `/v1/chat/completions`, 3 `/v1/models`.

## Latency (localhost shim, which proxies `api.x.ai`)

Token helper at `22:01:31`: `/home/vgpnk/.local/bin/xai-oauth-token` exit 0, stdout 882 bytes, stderr 0. Token not printed. `/tmp/v83-tok.out` deleted; confirmed absent at `22:39:17`.

`GET http://127.0.0.1:8790/v1/models` at `22:01:32`: HTTP 200, 6316 bytes, Cloudflare `CF-RAY` suffix `GIG`. Catalog ids included `grok-4.7` (aliases empty). `grok-4.7-fast` was not in the 14-id list. Repeat at `22:14:45`: status 200, `elapsed_s=0.442`, 6316 bytes.

Completion probes, model `grok-4.7`, body "Reply with the single word pong.", `max_tokens` 8–16:

| time | effort | wall | upstream ttft | upstream e2e | result |
| --- | --- | --- | --- | --- | --- |
| `22:02:16` | unset | 5.048 s | not captured | not captured | 200, `model=grok-4.7`, finish `stop`, content `pong`, completion_tokens 1, reasoning_tokens 350 |
| `22:14:45` | `low` | 1.016 s | 249.4 ms | 648.1 ms | 200, content `pong`, reasoning_tokens 37 |
| `22:22:41` | `low` | 0.925 s | 244.0 ms | 573.8 ms | 200, completion_tokens 1, reasoning_tokens 29 |

The 5.048 s figure is not congestion: that call spent 350 reasoning tokens. Low-effort calls stayed under about 1 s wall and about 250 ms ttft while the wave was in flight.

Alias probe at `22:31:03`, same body, `model=grok-4.7-fast`: HTTP 404 in 0.385 s. Body prefix (team id redacted): `{"code":"not-found","error":"The model grok-4.7-fast does not exist or your team <redacted> does not have access to it. ...`. Wire id `grok-4.7` works; the `grok-4.7-fast` name does not, as of this probe.

## Rate limits

No `429`, no `Retry-After`, no `503 shim busy` in the window.

Headers on the `22:14:45` probe:

```
x-ratelimit-limit-tokens: 53000000
x-ratelimit-remaining-tokens: 50475711
x-ratelimit-limit-requests: 8300
x-ratelimit-remaining-requests: 8286
```

Same request limits on the `22:22:41` probe; remaining tokens had returned to `53000000`; remaining requests still `8286`. Headroom was large on both samples. The identical request-remaining value is reported as observed, not explained.

Shim ceiling: `SHIM_MAX_CONCURRENT=128` (`systemctl --user show xai-shim.service -p Environment` at `22:02:02`; token command redacted in the capture). Thread count (`ps -o nlwp -p 1579`) peaked at 122 at `22:09:49`, under the ceiling. No `503` followed.

## Shim and helper processes

`xai-shim.service` active since `2026-10-17 00:00:08 -03`, MainPID 1579, `NRestarts=0` at `22:02:02` and still 0 at `22:31:03`. Listen: `127.0.0.1:8790`. Upstream: `api.x.ai`. `SHIM_FIX_EFFORT=1`. CPU at `22:02:02`: 18.711 s over 22 h. RSS grew from about 240 MB (`22:02:55`) to 325704 KiB (`22:31:03`). fd count ranged 160–246. Not a restart, not a leak that threatened the box.

Other long-running shims (not this wave's workers): oauth-shim pid 1573 `:8789`, devin-shim 1574 `:8787`, ds-flash 1577 `:8791`, glm-flash 1578 `:8793`, cursor-shim 1580 `:8788`. All started `00:00:07` with the user session. codex app-server pid 16546 since `00:04:16`. opencode serve pid 1277097 since `18:56:46`. These are co-tenants, not r99 orphans.

Parent of this wave's tool children: `kimi` pid 668105, started `15:21:21`, parent 667942. At `22:31:03`: elapsed `07:09:41`, 15.8% CPU, 4.0% MEM, NLWP 43, RSS 1274656 KiB, state `Sl+`. Direct children: 50 at `22:02:16`, 72–81 through `22:04:55`, down to 17 at `22:31:03`. Poll-wait loops (`poll.sh` / `sleep 20` / `POLL` in argv): 43 at `22:02:16`, peak 69 at `22:03:55`, 10 at `22:31:03`, 8 still alive at `22:33:04` with etimes `12:10`, `03:03`, `02:56`, `02:45`, `02:27`, `01:26`, `00:07`, `00:00`. They are live children of 668105 inside the 40×20 s poll window, not detached orphans. Child zombies of 668105: 0 after `22:01:23`.

One transient defunct at the first snapshot (`22:00:58`): pid 1667539, ppid 668105, `rg <defunct>`, etime `00:00`. Gone by `22:01:23`. Reaped, not an orphaned helper.

Desktop zombies, unrelated to the wave, still present at `22:31:03`:

```
1746    1736    22:30:52 Z    uwsm-app
1751    1739    22:30:52 Z    uwsm-app
1533569 1533567 01:57:27 Z    uwsm-app
```

Parents are the session/waybar tree, etimes match boot and a waybar restart, not r99.

Co-tenant `kimi` pid 878959 (started `16:57:31`, parent 59406) had a kotodama `reports/round-15` sleep loop at `22:01:43` (pid 1664498). That child was gone by `22:22:41`. Not an r99 helper.

No process whose start time was `21:40`–`21:59` and whose command matched kimi/shim/oauth/agent/grok/python was still alive at `22:22:41`. The failed dispatch did not leave a helper behind that this scan could see.

## Host resources

| time | load 1/5/15 | mem used | mem available | swap used | shim NLWP | kimi children | pollish |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22:00:58` | 0.66 / 0.38 / 0.37 | 6.7 Gi | 23 Gi | 977 Mi | — | — | — |
| `22:02:16` | 3.06 / 1.04 / 0.59 | 7.5 Gi | 22 Gi | 977 Mi | 98 | 50 | 43 |
| `22:02:55` | 2.11 / 1.06 / 0.62 | 7434 Mi | 23544 Mi | 977 Mi | 88 | 72 | 59 |
| `22:04:55` | 0.87 / 0.94 / 0.64 | 7462 Mi | 23515 Mi | 977 Mi | 85 | 81 | 68 |
| `22:09:49` | 0.39 / 0.75 / 0.65 | 7288 Mi | 23689 Mi | 977 Mi | 122 | 44 | 35 |
| `22:22:42` | 0.70 / 0.76 / 0.70 | — | — | — | 110 | 26 | 17 |
| `22:31:03` | 0.52 / 0.61 / 0.64 | 7.0 Gi | 23 Gi | 977 Mi | 105 | 17 | 10 |
| `22:33:04` | 0.67 / 0.63 / 0.64 | — | 24233652 kB | 1000 Mi used (SwapTotal−SwapFree) | — | — | 8 |

Load spike to 3.06 coincided with the dispatch burst (695 completions in minute `22:01`) and fell back under 1.1 within about two minutes. On 32 CPUs that is not saturation. Swap stayed flat at 977 MiB for the whole live window (1000 MiB at `22:33` is the same pool, not growth). `dmesg -T --since '2026-10-17 21:30:00'` matched no OOM/kill lines. Disk at `22:01:23`: `/home` 132G/930G (15%), `/tmp` tmpfs 1.2G/16G (8%).

## Process presence (not a claim verdict)

Counted so a later seat can see whether producers were still absent while the host was healthy. Contents not read. Not a C1/C2 result.

- `22:01:43`: one seat report, `S3-fixture-author.md`. `corpus/knowledge/r99*` absent. Fixture dir `corpus/fixtures/r99-window-lapse/` already present (several files mtime `21:36:10`, three files mtime `22:01:13`).
- Tool mtimes during sampling: `dependency_freeze.py` moved `22:02:04` → `22:03:21` → `22:07:33`. Contract moved `20:33:36` → `22:04:28` → `22:08:46`.
- `22:05:15`: seat md files = 5 (`S3`, `S4`, `V80`, `V68`, `V10`). Knowledge `r99*` still absent.
- `22:22:42`: 16 seat md files. Still only `S3-fixture-author.md` and `S4-fixture-docs.md` among `S*.md`. Knowledge `r99*` absent.
- `22:31:03`: 26 seat md files. `S1*`, `S2*`, `S5*` still absent. Knowledge `r99*` absent.
- `22:39:17`: seats directory mtime `22:39` (5208 bytes). Wave still writing after this snapshot. `S1`/`S2`/`S5` and the knowledge notes were ABSENT at the last explicit check (`22:31:03`). Not verified later. Not treated as a plan.

LOG.md mtime stayed `2026-10-17 21:53:33` during the window (the blocked-dispatch note). `git rev-parse --short HEAD` at `22:01:43` was `337f0fa`. Those are anchors only.

## What this seat did not do

Did not read `auth.json`. Did not print the token. Did not verify freeze pins, the lapse fixture, or the blind-spot table. Did not wait out every poller (8 still inside their windows at `22:33:04`). Did not attribute the single `22:20:07` `502` — the journal does not carry a body.

PASS — host record for 22:00:58–22:33:04 -03: grok-4.7 served 200 with no 429/503 and ~244–249 ms ttft on low-effort probes; one isolated 502 at 22:20:07 (body not logged); alias grok-4.7-fast still 404 at 22:31:03; no orphaned r99 helpers.
