#!/bin/sh
# poll_wait.sh <path> [deadline-seconds] — poll every 60s INSIDE one call; trap a terminal line.
# r90-Q2-P1 committed helper. Usage: poll_wait.sh patches/X1.patch 1200
p="${1:?path}"; d="${2:-1200}"; s=0
trap 'echo "POLL_TERMINAL status=1 reason=trap elapsed=${s}s checks=${n:-0}"; exit 1' TERM INT
n=0
while [ "$s" -lt "$d" ]; do
  if [ -e "$p" ]; then echo "POLL_HIT path=$p elapsed=${s}s checks=$n"; exit 0; fi
  sleep 60; s=$((s+60)); n=$((n+1))
  echo "POLL_CHECK t=${s}s path=$p present=no"
done
echo "POLL_TERMINAL status=0 reason=deadline elapsed=${s}s checks=$n"
exit 0
