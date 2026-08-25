#!/usr/bin/env bash
# Self-check for watch.sh: history stays silent, real events surface, noise does not.
set -u
here=$(cd "$(dirname "$0")" && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/tr" "$T/state"
A="$T/tr/aaaaaaaa-1111-2222-3333-444444444444.jsonl"

echo '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"already said"}}' >"$A"
OVERSIGHT_STATE="$T/state" bash "$here/watch.sh" "$T/tr" none 1 >"$T/out" 2>"$T/err" &
pid=$!; trap 'kill $pid 2>/dev/null; rm -rf "$T"' EXIT
sleep 2
{
  echo '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"no, not like that"}}'
  echo '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"<cross-session-message from=\"overseer\">stop</cross-session-message>"}}'
  echo '{"type":"user","isSidechain":false,"message":{"content":[{"type":"tool_result","content":"out"}]}}'
  echo '{"type":"assistant","isSidechain":false,"message":{"content":[{"type":"tool_use","name":"Task","input":{"description":"rework auth","prompt":"rewrite the whole module"}}]}}'
  echo '{"type":"assistant","isSidechain":true,"message":{"content":[{"type":"tool_use","name":"Task","input":{"description":"sidechain","prompt":"must stay silent"}}]}}'
} >>"$A"
sleep 2
echo '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"fresh session"}}' >"$T/tr/bbbbbbbb-1111-2222-3333-444444444444.jsonl"
sleep 2
kill $pid 2>/dev/null; wait $pid 2>/dev/null
out=$(cat "$T/out")

fail=0
want() { grep -q "$1" <<<"$out" || { echo "MISSING: $1"; fail=1; }; }
deny() { grep -q "$1" <<<"$out" && { echo "LEAKED: $1"; fail=1; }; }
want "HUMAN aaaaaaaa — no, not like that"
want "DISPATCH aaaaaaaa — rework auth"
want "NEW bbbbbbbb"
want "HUMAN bbbbbbbb — fresh session"
deny "already said"      # history before the overseer started
deny "cross-session"     # the overseer's own flag coming back at it
deny "tool_result"       # tool output is not an event
deny "must stay silent"  # subagent traffic
[ "$fail" = 0 ] && echo "watch.sh: ok" || { echo "watch.sh: FAILED"; exit 1; }
